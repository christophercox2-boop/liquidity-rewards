#!/usr/bin/env python3
"""Always-on live earnings monitor.

Runs on any small server (Dockerfile provided — see live/README.md). Every
POLL_SECONDS it scores your resting orders with the same official-formula
code the hourly tracker uses, then integrates the rate over time the way the
exchange does: earned_today += rate x elapsed. Serves a phone-friendly
dashboard with a running "earned today" counter and per-market breakdown.

Environment:
    POLYMARKET_KEY_ID / POLYMARKET_SECRET_KEY   API credentials (required)
    DASH_PASSWORD                               dashboard password (required)
    PORT                                        web port (default 8080)
    POLL_SECONDS                                sample interval (default 30)

The reward day runs midnight-to-midnight Eastern Time, matching Polymarket's
daily pools. State persists to state.json so restarts don't zero the counter
(a full redeploy replaces the disk and starts the day fresh).
"""

from __future__ import annotations

import base64
import csv
import datetime as dt
import gzip
import io
import json
import os
import math
import random
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import track_rewards as tr  # noqa: E402 — reuse the tracker's scoring code

POLL_SECONDS = int(os.environ.get("POLL_SECONDS", "30"))
POS_REFRESH_SECONDS = int(os.environ.get("POS_REFRESH_SECONDS", "120"))  # P/L tab data
PORT = int(os.environ.get("PORT", "8080"))
DASH_PASSWORD = os.environ.get("DASH_PASSWORD", "")
STATE_PATH = Path(os.environ.get("STATE_PATH", "state.json"))
ET = ZoneInfo("America/New_York")
MAX_GAP_SECONDS = 300  # an outage never extrapolates more than 5 minutes
# How long one tracker snapshot may stand in for. The tracker runs roughly
# hourly, so 2h leaves normal cadence untouched while a real blackout stops
# being charged at whatever rate happened to be showing when it began.
EST_MAX_GAP = float(os.environ.get("EST_MAX_GAP", "7200"))
# How many Poisson samples today before the headline figures switch off the
# old action-triggered accrual and onto the unbiased one. At the 5s mean this
# is ~20 minutes of sampling — long enough that a fresh boot shows the
# familiar number rather than a counter climbing from zero, short enough that
# the honest figure is what you see for all but the first minutes of a day.
# Same reason as the note below: read from Monitor methods, so defined here.
# Retired: this counted samples, which says how DENSELY the day was measured
# and nothing about how MUCH of it was. Superseded by HF_MIN_COVER below.
HF_RATE_TAU = float(os.environ.get("HF_RATE_TAU", "600"))  # rate smoothing, seconds
# A book older than this is not evidence of anything; see _rescore_rate.
BOOK_MAX_AGE = float(os.environ.get("BOOK_MAX_AGE", "180"))
# Fraction of scorable orders needing a fresh book before a sample counts.
HF_MIN_FRESH = float(os.environ.get("HF_MIN_FRESH", "0.5"))
# A displayed rate older than this has no evidence behind it; see
# has_live_data(). Four poll intervals, so a couple of missed polls do not
# blank the dashboard but a real outage does.
STALE_AFTER = float(os.environ.get("STALE_AFTER", str(POLL_SECONDS * 4)))
# Fraction of the DAY the sampler must actually have measured before its
# figure is treated as that day's earnings.
#
# This replaces a sample-count threshold, which asked the wrong question. On
# 2026-08-10 the sampler had 863 samples — far past the old 240 — so the day
# closed on earned_hf = $51.73. But 863 samples at a 5s mean is ~72 minutes:
# it had measured about an hour of a 24-hour day, and that hour was recorded
# as the day's total against a tracker integral of $455.38. Sample count says
# how DENSELY you measured; it says nothing about HOW MUCH of the day. A
# partial measurement of a day is not a smaller day, it is an unknown one, so
# short coverage now falls back to the tracker figure instead.
HF_MIN_COVER = float(os.environ.get("HF_MIN_COVER", "0.90"))
# Raw samples kept for the graph. At the 5s mean this is ~50 minutes of dots —
# enough to see the scatter and how tight the smoothed line sits inside it,
# without making every dashboard refresh carry a large payload.
HF_POINTS_KEPT = int(os.environ.get("HF_POINTS_KEPT", "600"))
# Defined up here, not with the other DEFEND_* constants further down: the
# defend-seed runs from Monitor.__init__, which executes long before that
# block, so leaving it there raised NameError on boot.
DEFEND_MAX_MARKETS = int(os.environ.get("DEFEND_MAX_MARKETS", "260"))

# Optional: phone notifications via ntfy (https://ntfy.sh). Install the ntfy
# app, subscribe to a long random topic, set NTFY_TOPIC to the same string.
NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()
NTFY_SERVER = os.environ.get("NTFY_SERVER", "https://ntfy.sh").rstrip("/")


def notify(title: str, message: str, priority: str = "default") -> None:
    if not NTFY_TOPIC:
        return
    try:
        requests.request(
            "POST", f"{NTFY_SERVER}/{NTFY_TOPIC}", data=message.encode(),
            headers={"Title": title, "Priority": priority}, timeout=10,
        )
    except Exception:  # noqa: BLE001 — alerts must never break the monitor
        pass


# Optional but recommended: persist the counter to the repo so redeploys
# (which replace this container's disk) don't reset "earned today".
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
GITHUB_REPO = os.environ.get("GITHUB_REPO", "wfco223/Liquidity-rewards")
STATE_BRANCH = os.environ.get("STATE_BRANCH", "live-state")
SAVE_INTERVAL = int(os.environ.get("SAVE_INTERVAL", "120"))
GH_API = "https://api.github.com"


def _gh(method: str, path: str, **kw):
    return requests.request(
        method, GH_API + path,
        headers={"Authorization": f"Bearer {GITHUB_TOKEN}", "Accept": "application/vnd.github+json"},
        timeout=15, **kw,
    )


SAVE_STATUS = {"ok_ts": 0.0, "err": ""}  # surfaced in the dashboard footer
SLIM_EXCLUDE = ("series",)  # per-market graph history: huge, rebuilds in hours


def load_remote_state() -> dict | None:
    if not GITHUB_TOKEN:
        return None
    try:
        raw = b""
        r = _gh("GET", f"/repos/{GITHUB_REPO}/contents/state.json", params={"ref": STATE_BRANCH})
        if r.status_code == 200:
            raw = base64.b64decode(r.json().get("content") or "")
        if not raw:  # files >1MB return empty content — refetch as raw media
            r = requests.get(
                f"{GH_API}/repos/{GITHUB_REPO}/contents/state.json",
                params={"ref": STATE_BRANCH},
                headers={"Authorization": f"Bearer {GITHUB_TOKEN}",
                         "Accept": "application/vnd.github.raw+json"},
                timeout=30,
            )
            if r.status_code != 200:
                return None
            raw = r.content
        try:
            raw = gzip.decompress(raw)
        except Exception:  # noqa: BLE001 — older saves were plain JSON
            pass
        return json.loads(raw)
    except Exception:  # noqa: BLE001
        return None


def save_remote_state(state: dict) -> bool:
    """Store state.json (gzipped, without the bulky graph series) as a single
    orphan commit, force-updating the state branch — no history accumulates.
    GitHub rejects ~1MB+ request bodies, which is how saves silently died as
    the portfolio grew."""
    if not GITHUB_TOKEN:
        return False
    try:
        slim = {k: v for k, v in state.items() if k not in SLIM_EXCLUDE}
        payload = base64.b64encode(gzip.compress(json.dumps(slim).encode())).decode()
        r = _gh("POST", f"/repos/{GITHUB_REPO}/git/blobs",
                json={"content": payload, "encoding": "base64"})
        if r.status_code >= 300:
            SAVE_STATUS["err"] = f"blob HTTP {r.status_code}"
            return False
        blob = r.json()["sha"]
        r = _gh("POST", f"/repos/{GITHUB_REPO}/git/trees",
                json={"tree": [{"path": "state.json", "mode": "100644", "type": "blob", "sha": blob}]})
        tree = r.json()["sha"]
        r = _gh("POST", f"/repos/{GITHUB_REPO}/git/commits",
                json={"message": "live counter state", "tree": tree, "parents": []})
        commit = r.json()["sha"]
        r = _gh("PATCH", f"/repos/{GITHUB_REPO}/git/refs/heads/{STATE_BRANCH}",
                json={"sha": commit, "force": True})
        if r.status_code in (404, 422):  # branch doesn't exist yet
            r = _gh("POST", f"/repos/{GITHUB_REPO}/git/refs",
                    json={"ref": f"refs/heads/{STATE_BRANCH}", "sha": commit})
        if r.status_code < 300:
            SAVE_STATUS.update(ok_ts=time.time(), err="")
            return True
        SAVE_STATUS["err"] = f"ref HTTP {r.status_code}"
        return False
    except Exception as e:  # noqa: BLE001
        SAVE_STATUS["err"] = f"{type(e).__name__}: {e}"[:120]
        return False


def _estimates_csv_text() -> str | None:
    """data/estimates.csv from main, or None."""
    if not GITHUB_TOKEN:
        return None
    try:
        r = requests.get(
            f"{GH_API}/repos/{GITHUB_REPO}/contents/data/estimates.csv",
            params={"ref": "main"},
            headers={"Authorization": f"Bearer {GITHUB_TOKEN}",
                     "Accept": "application/vnd.github.raw+json"},
            timeout=30,
        )
        return r.text if r.status_code == 200 else None
    except Exception:  # noqa: BLE001
        return None


# --- in-process tracker (replaced the hourly Actions run, 2026-08-15) -------
# The hourly "Track liquidity rewards" workflow burned ~85 Actions minutes a
# day against a 2,000/month plan. This thread runs the SAME track_rewards.py,
# unchanged, as a subprocess (its own interpreter — no shared module state
# with the poll loop), then pushes every output to main as ONE commit via the
# git data API. Append-history files are seeded from main first, so container
# restarts never reset them. The Actions workflow still runs every 4 hours as
# an independent heartbeat: if this container dies, that run still stamps the
# ❌ freshness banner into STATUS.md and emails the owner.
TRACKER_INTERVAL = float(os.environ.get("TRACKER_INTERVAL", "3600"))
TRACKER_ENABLED = os.environ.get("TRACKER_IN_MONITOR", "1") != "0"
APP_DIR = Path(__file__).resolve().parent.parent
TRACKER_SEED = ("data/estimates.csv", "data/checks.csv", "data/estimate_runs.csv",
                "data/family_day.csv")
TRACKER_PUSH = ("STATUS.md", "data/rewards.csv", "data/checks.csv",
                "data/estimates.csv", "data/estimate_runs.csv",
                "data/family_day.csv", "data/live_orders.csv",
                "data/latest_response.json")
TRACKER_STATUS = {"ok_ts": 0.0, "err": "", "runs": 0}


def _tracker_commit(files: dict[str, bytes]) -> str:
    """One fast-forward commit on main. Returns '' or a short error."""
    for attempt in range(2):
        r = _gh("GET", f"/repos/{GITHUB_REPO}/git/ref/heads/main")
        if r.status_code >= 300:
            return f"head HTTP {r.status_code}"
        head = r.json()["object"]["sha"]
        r = _gh("GET", f"/repos/{GITHUB_REPO}/git/commits/{head}")
        if r.status_code >= 300:
            return f"head commit HTTP {r.status_code}"
        base_tree = r.json()["tree"]["sha"]
        tree = []
        for path, data in files.items():
            rb = _gh("POST", f"/repos/{GITHUB_REPO}/git/blobs",
                     json={"content": base64.b64encode(data).decode(),
                           "encoding": "base64"})
            if rb.status_code >= 300:
                return f"blob {path} HTTP {rb.status_code}"
            tree.append({"path": path, "mode": "100644", "type": "blob",
                         "sha": rb.json()["sha"]})
        rt = _gh("POST", f"/repos/{GITHUB_REPO}/git/trees",
                 json={"base_tree": base_tree, "tree": tree})
        if rt.status_code >= 300:
            return f"tree HTTP {rt.status_code}"
        if rt.json()["sha"] == base_tree:
            return ""          # nothing actually changed — no empty commit
        rc = _gh("POST", f"/repos/{GITHUB_REPO}/git/commits",
                 json={"message": "Liquidity rewards check [skip ci]",
                       "tree": rt.json()["sha"], "parents": [head]})
        if rc.status_code >= 300:
            return f"commit HTTP {rc.status_code}"
        rr = _gh("PATCH", f"/repos/{GITHUB_REPO}/git/refs/heads/main",
                 json={"sha": rc.json()["sha"]})   # fast-forward only, no force
        if rr.status_code < 300:
            return ""
        if attempt == 0 and rr.status_code in (409, 422):
            continue           # lost a push race — rebuild on the new head
        return f"ref HTTP {rr.status_code}"
    return "ref race"


def _tracker_once() -> str:
    import subprocess
    for path in TRACKER_SEED:
        txt = _gh_text(path, ref="main")
        if txt:
            p = APP_DIR / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(txt)
    proc = subprocess.run([sys.executable, str(APP_DIR / "track_rewards.py")],
                          cwd=str(APP_DIR), capture_output=True, text=True,
                          timeout=1800)
    tail = " ".join(((proc.stdout or "") + " " + (proc.stderr or "")).split())[-300:]
    files = {}
    for path in TRACKER_PUSH:
        p = APP_DIR / path
        if p.exists():
            files[path] = p.read_bytes()
    if not files:
        return ("tracker wrote nothing: " + tail)[:250]
    err = _tracker_commit(files)
    if err.startswith("blob data/estimates.csv") and "data/estimates.csv" in files:
        # the one file big enough to trip a request-body limit — commit the
        # rest; the 4-hourly Actions run still refreshes it
        del files["data/estimates.csv"]
        err = _tracker_commit(files) or "estimates.csv skipped (too big for the API)"
    if err:
        return err[:250]
    # a failed fetch still commits its ❌ banner (same as Actions did) but is
    # still a failure worth surfacing
    return "" if proc.returncode == 0 else (f"tracker exit {proc.returncode}: {tail}")[:250]


def tracker_loop() -> None:
    time.sleep(120)            # let the poll loop warm its caches first
    while True:
        if TRACKER_ENABLED and GITHUB_TOKEN:
            try:
                err = _tracker_once()
            except Exception as e:  # noqa: BLE001 — the loop must survive anything
                err = f"{type(e).__name__}: {e}"[:200]
            TRACKER_STATUS["runs"] += 1
            TRACKER_STATUS["err"] = err
            if not err:
                TRACKER_STATUS["ok_ts"] = time.time()
                # the run just rewrote rewards.csv — refresh the paid-days
                # table NOW instead of waiting for the hourly sweep (the
                # owner caught 'not posted yet' beside freshly posted rows)
                try:
                    winners, rew_total, day_paid = load_winners()
                    if winners:
                        global WINNERS
                        WINNERS = winners
                    MONITOR.day_paid = day_paid
                    if rew_total:
                        MONITOR.note_rewards_total(rew_total)
                except Exception:  # noqa: BLE001
                    pass
        time.sleep(TRACKER_INTERVAL)


def tracker_day_integral(day_et: str,
                         text: str | None = None) -> tuple[float, dict[str, float]] | None:
    """Rebuild a day's earnings from the hourly tracker's estimate snapshots
    (data/estimates.csv on main) — piecewise-constant integration from
    midnight ET to now, capped at the day's end for finished days.
    Independent of this process, so it survives any monitor outage or state
    loss. Pass `text` to reuse one fetched copy across several days."""
    if text is None:
        text = _estimates_csv_text()
    if not text:
        return None
    try:
        import csv as _csv
        import io as _io
        runs: dict[str, dict[str, float]] = {}  # utc run ts -> market -> est $/day
        for row in _csv.DictReader(_io.StringIO(text)):
            try:
                if tr._et_day(row["checked_at_utc"]) != day_et:
                    continue
                mkts = runs.setdefault(row["checked_at_utc"], {})
                mkts[row["market"]] = mkts.get(row["market"], 0.0) + float(row["est_day"])
            except Exception:  # noqa: BLE001 — one bad row must not kill the rebuild
                continue
        if not runs:
            return None
        times = sorted(runs)
        midnight = dt.datetime.strptime(day_et, "%Y-%m-%d").replace(tzinfo=ET)
        # for a finished day the last snapshot's rate holds only to midnight
        now = min(dt.datetime.now(dt.timezone.utc),
                  (midnight + dt.timedelta(days=1)).astimezone(dt.timezone.utc))

        def _utc(ts: str) -> dt.datetime:
            return dt.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)

        total, per_market = 0.0, {}
        for i, ts in enumerate(times):
            start = midnight.astimezone(dt.timezone.utc) if i == 0 else _utc(ts)
            end = _utc(times[i + 1]) if i + 1 < len(times) else now
            # A snapshot's rate is evidence for at most EST_MAX_GAP. Beyond
            # that we simply had no data, and unmeasured time earns zero.
            #
            # Without this, an outage is charged at whatever rate happened to
            # be showing when the feed died: on 2026-08-11 the last reading
            # before maintenance (10:14 UTC, $324/day) was extended across the
            # whole 4.8h blackout, which is why this rebuild kept undoing the
            # 6:00 ET clamp every time the anchor ran.
            span = max((end - start).total_seconds(), 0.0)
            frac = min(span, EST_MAX_GAP) / 86400.0
            for m, est in runs[ts].items():
                total += est * frac
                per_market[m] = per_market.get(m, 0.0) + est * frac
        return round(total, 2), {m: round(v, 4) for m, v in per_market.items()}
    except Exception:  # noqa: BLE001
        return None


def intraday_profile(text: str | None = None, days: int = 10) -> list[float] | None:
    """How this account's earnings actually distribute across the ET day,
    from the last `days` of tracker snapshots: returns a 25-point cumulative
    curve (0.0 at midnight → 1.0 at midnight) used to project 'on pace'
    honestly — competitive US afternoons and rich overnight hours weigh in
    as they really are, instead of assuming every hour earns the same."""
    if text is None:
        text = _estimates_csv_text()
    if not text:
        return None
    try:
        import csv as _csv
        import io as _io
        totals: dict[str, float] = {}  # snapshot ts -> total $/day
        for row in _csv.DictReader(_io.StringIO(text)):
            try:
                totals[row["checked_at_utc"]] = (totals.get(row["checked_at_utc"], 0.0)
                                                 + float(row["est_day"]))
            except Exception:  # noqa: BLE001
                continue
        if not totals:
            return None
        cutoff = (dt.datetime.now(dt.timezone.utc)
                  - dt.timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
        buckets: list[list[float]] = [[] for _ in range(24)]
        for ts, tot in totals.items():
            if ts < cutoff:
                continue
            t = dt.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=dt.timezone.utc).astimezone(ET)
            buckets[t.hour].append(tot)
        filled = [sum(b) / len(b) for b in buckets if b]
        if len(filled) < 6:  # not enough coverage to be better than flat
            return None
        overall = sum(filled) / len(filled)
        w = [(sum(b) / len(b)) if b else overall for b in buckets]
        s = sum(w)
        if s <= 0:
            return None
        cum = [0.0]
        for h in range(24):
            cum.append(cum[-1] + w[h] / s)
        cum[-1] = 1.0
        return [round(c, 4) for c in cum]
    except Exception:  # noqa: BLE001
        return None


def day_shape_digest(text: str | None = None) -> str | None:
    """The morning report: how YESTERDAY's earnings distributed across the
    day versus your typical shape, plus where today stands so far. Sent as
    one compact phone notification at ~8:05am ET."""
    if text is None:
        text = _estimates_csv_text()
    if not text:
        return None
    try:
        import csv as _csv
        import io as _io
        now_et = dt.datetime.now(ET)
        yday = (now_et - dt.timedelta(days=1)).strftime("%Y-%m-%d")
        runs: dict[str, float] = {}  # snapshot ts -> total $/day (yesterday ET)
        for row in _csv.DictReader(_io.StringIO(text)):
            try:
                if tr._et_day(row["checked_at_utc"]) == yday:
                    runs[row["checked_at_utc"]] = (runs.get(row["checked_at_utc"], 0.0)
                                                   + float(row["est_day"]))
            except Exception:  # noqa: BLE001
                continue
        if len(runs) < 4:
            return None
        times = sorted(runs)
        midnight = dt.datetime.strptime(yday, "%Y-%m-%d").replace(tzinfo=ET)
        day_end = midnight + dt.timedelta(days=1)
        hours = [0.0] * 24  # $ earned in each ET hour yesterday

        def _utc(ts: str) -> dt.datetime:
            return dt.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)

        for i, ts in enumerate(times):
            start = midnight if i == 0 else _utc(ts).astimezone(ET)
            end = _utc(times[i + 1]).astimezone(ET) if i + 1 < len(times) else day_end
            rate = runs[ts]
            t = max(start, midnight)
            while t < min(end, day_end):
                nxt = min((t.replace(minute=0, second=0, microsecond=0)
                           + dt.timedelta(hours=1)), end, day_end)
                hours[t.hour] += rate * (nxt - t).total_seconds() / 86400.0
                t = nxt
        total = sum(hours)
        if total <= 0:
            return None
        prof = MONITOR.day_profile if MONITOR else None
        have_prof = bool(prof and len(prof) == 25)
        best = max(range(24), key=lambda h: hours[h])
        worst = min(range(24), key=lambda h: hours[h])

        def h12(h: int) -> str:
            return f"{(h % 12) or 12}{'am' if h < 12 else 'pm'}"

        parts = [f"Yesterday {yday[5:]}: ${total:.2f} tracked."]
        segs = [("overnight", 0, 6), ("morning", 6, 12),
                ("afternoon", 12, 18), ("evening", 18, 24)]
        bits = []
        for name, a, b in segs:
            s = sum(hours[a:b]) / total * 100
            t_s = f" (typ {(prof[b] - prof[a]) * 100:.0f}%)" if have_prof else ""
            bits.append(f"{name} {s:.0f}%{t_s}")
        parts.append("Shape: " + ", ".join(bits) + ".")
        parts.append(f"Best hour {h12(best)} ${hours[best]:.2f}; "
                     f"slowest {h12(worst)} ${hours[worst]:.2f}.")
        if MONITOR:
            with MONITOR.lock:
                earned = MONITOR.headline()[0]
                hist = [x.get("earned") or 0.0
                        for x in (MONITOR.state.get("history") or [])[-5:]]
            hf = now_et.hour + now_et.minute / 60.0
            if have_prof:
                i = int(hf)
                frac = prof[i] + (prof[min(i + 1, 24)] - prof[i]) * (hf - i)
            else:
                frac = hf / 24.0
            if hist and frac > 0.03:
                typical = sum(hist) / len(hist) * frac
                if typical > 0.5:
                    d = (earned / typical - 1) * 100
                    parts.append(f"Today so far ${earned:.2f} — "
                                 + (f"{d:+.0f}% vs your usual pace."
                                    if abs(d) >= 1 else "right on your usual pace."))
        return " ".join(parts)
    except Exception:  # noqa: BLE001
        return None


def load_winners() -> tuple[list[dict], float, dict]:
    """Career paid rewards per market from data/rewards.csv — fresh copy from
    GitHub when a token is available, else the file shipped with the deploy.
    Returns (winners, lifetime total credited): winners drop markets not
    paid in 14 days (likely resolved or de-listed); the total feeds the
    'LP rewards paid' phone alert."""
    text = None
    if GITHUB_TOKEN:
        try:
            r = requests.get(
                f"{GH_API}/repos/{GITHUB_REPO}/contents/data/rewards.csv",
                params={"ref": "main"},
                headers={"Authorization": f"Bearer {GITHUB_TOKEN}",
                         "Accept": "application/vnd.github.raw+json"},
                timeout=30,
            )
            if r.status_code == 200:
                text = r.text
        except Exception:  # noqa: BLE001 — fall back to the local file
            pass
    if text is None:
        try:
            text = (Path(__file__).resolve().parent.parent / "data" / "rewards.csv").read_text()
        except Exception:  # noqa: BLE001
            return [], 0.0, {}
    try:
        import csv as _csv
        import io as _io
        tot: dict[str, float] = {}
        last: dict[str, str] = {}
        for row in _csv.DictReader(_io.StringIO(text)):
            m = row.get("market") or ""
            try:
                tot[m] = tot.get(m, 0.0) + float(row.get("reward_usd") or 0)
            except ValueError:
                continue
            last[m] = max(last.get(m, ""), row.get("date") or "")
        cutoff = (dt.date.today() - dt.timedelta(days=14)).isoformat()
        winners = sorted(
            [{"market": m, "total": round(v, 2), "last": last[m]}
             for m, v in tot.items() if m and v >= 2.0 and last[m] >= cutoff],
            key=lambda w: -w["total"])
        days: dict[str, dict] = {}
        for row in _csv.DictReader(_io.StringIO(text)):
            d = row.get("date") or ""
            try:
                v = float(row.get("reward_usd") or 0)
            except ValueError:
                continue
            e = days.setdefault(d, {"paid": 0.0, "pending": False})
            e["paid"] += v
            if str(row.get("status", "")).upper() == "PENDING":
                e["pending"] = True
        for e in days.values():
            e["paid"] = round(e["paid"], 2)
        return winners, round(sum(tot.values()), 2), days
    except Exception:  # noqa: BLE001
        return [], 0.0, {}


WINNERS: list[dict] = []


class Monitor:
    def hf_covers_day(self, full_day: bool = False) -> bool:
        """Has the sampler measured enough of the day to speak for it?

        full_day=False asks about the day so far (for the live dashboard);
        full_day=True asks about a whole 24h (for closing a day into history).
        Caller must hold the lock.
        """
        covered = self.state.get("hf_covered_s") or 0.0
        if full_day:
            return covered >= HF_MIN_COVER * 86400.0
        day = self.state.get("day")
        if not day:
            return False
        try:
            midnight = dt.datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=ET)
        except Exception:  # noqa: BLE001 — malformed day never gates on garbage
            return False
        elapsed = (dt.datetime.now(ET) - midnight).total_seconds()
        if elapsed <= 0:
            return False
        return covered >= HF_MIN_COVER * min(elapsed, 86400.0)

    def headline(self) -> tuple[float, dict[str, float], float, str]:
        """The figures shown to the user: (earned today, per-market, $/day, basis).

        Prefers the Poisson-sampled accrual once it has actually measured most
        of the day so far. The old accrual is woken by POLL_KICK the instant we
        place or reprice, so it sampled our share at its peak and read
        1.58x-2.03x above real payouts; this one samples on a clock nothing we
        do can pull. Falls back to the old figures when coverage is short — a
        sampler that started mid-day, or one that has just come back from an
        outage, holds a real number for a fraction of a day, and showing that
        as the day's total is how 2026-08-10 came to read $51.73.
        Caller must hold the lock.
        """
        live = self.has_live_data()
        if self.hf_covers_day():
            rate = self.hf_rate if self.hf_rate is not None else self.rate
            return (self.state.get("earned_hf") or 0.0,
                    self.state.get("per_market_hf") or {},
                    rate if live else 0.0, "hf")
        return (self.state.get("earned") or 0.0,
                self.state.get("per_market") or {},
                self.rate if live else 0.0, "sparse")

    def has_live_data(self) -> bool:
        """Is there current evidence of a rate at all? Caller holds the lock.

        Both displayed rates are last-known values that only move when their
        producer runs: self.rate updates in sample(), self.hf_rate in the
        sampler. When the exchange stops answering, neither updates and both
        sit at whatever they last were — which is how the dashboard came to
        advertise $374/day against ZERO open orders during the post-maintenance
        401s. A rate is a claim about right now, so it needs evidence from
        right now.
        """
        if not self.orders:
            return False        # nothing resting can be earning anything
        if self.last_ts is None:
            return False        # no successful poll yet this process
        age = (dt.datetime.now(dt.timezone.utc) - self.last_ts).total_seconds()
        if age > STALE_AFTER:
            return False        # polls are failing; the last rate is history
        fresh, considered = self.hf_fresh
        if considered and fresh < considered * HF_MIN_FRESH:
            return False        # books have gone quiet even if polls have not
        return True

    def __init__(self) -> None:
        self.lock = threading.Lock()
        self._hf_samples = 0        # samples behind earned_hf, reset each day
        self.hf_rate: float | None = None   # EWMA of the Poisson-sampled rate
        # Raw Poisson samples for the graph: [epoch_seconds, $/day]. Held in
        # memory only, never in self.state — state.json is saved to GitHub on
        # a timer and this would bloat every write for something that is
        # purely a live view and rebuilds within minutes of a restart.
        self.hf_points: list[list[float]] = []
        self.hf_fresh: tuple[int, int] = (0, 0)   # books fresh / orders considered
        self.state: dict = {"day": None, "earned": 0.0, "per_market": {}, "history": [],
                            "saved_at": 0.0, "rate": 0.0, "market_rates": {}, "ts": None,
                            # High-frequency accrual: the same integration as
                            # `earned`, but never overwritten by the hourly
                            # rebuild. The exchange scores a random snapshot
                            # EVERY SECOND and weights all 86,400 equally, so
                            # what matters is sampling density. This process
                            # samples every POLL_SECONDS (2,880/day at the
                            # default 30s); the tracker's estimates.csv managed
                            # 31 on 2026-08-09. Kept side by side so the two
                            # can be scored against real payouts instead of
                            # argued about.
                            "earned_hf": 0.0, "per_market_hf": {}, "hf_covered_s": 0.0}
        local: dict = {}
        if STATE_PATH.exists():
            try:
                local = json.loads(STATE_PATH.read_text())
            except Exception:  # noqa: BLE001 — corrupt state: start fresh
                pass
        remote = load_remote_state() or {}
        # A redeploy replaces the local disk — take whichever copy is newest.
        best = max((local, remote), key=lambda s: s.get("saved_at", 0.0) or 0.0)
        self.state.update(best)
        # One-time: drop today's earnings accrued after 2026-08-11 06:00 ET.
        #
        # The exchange entered maintenance at 06:00 ET and then began rejecting
        # our key, so everything after that point was integrated against a book
        # that had stopped moving — the accrual kept running on a frozen cache
        # until the staleness guard shipped. Integrating estimates.csv from
        # midnight ET to that cutoff gives $142.06, the last figure with live
        # data behind it.
        #
        # Runs once: the marker stops it clipping legitimate accrual after the
        # feed returns, and it only ever lowers, never raises.
        try:
            if self.state.get("day") == "2026-08-11" and not self.state.get("clamp_0811"):
                cap = 142.06
                cur = self.state.get("earned") or 0.0
                for key, pm in (("earned", "per_market"), ("earned_hf", "per_market_hf")):
                    val = self.state.get(key) or 0.0
                    if val > cap:
                        scale = cap / val if val else 0.0
                        self.state[key] = cap
                        self.state[pm] = {m: v * scale
                                          for m, v in (self.state.get(pm) or {}).items()}
                self.state["clamp_0811"] = True
                print(f"[clamp] 2026-08-11 trimmed to the 06:00 ET cutoff: "
                      f"{cur:.2f} -> {self.state.get('earned'):.2f}")
        except Exception as e:  # noqa: BLE001 — never block boot over a one-off
            print(f"[clamp] skipped: {type(e).__name__}: {e}")
        # One-time repair of days closed by the old sample-count gate.
        #
        # That gate let a day close on earned_hf after merely 240 samples, so
        # 2026-08-10 — where the sampler had been alive about an hour — was
        # recorded as $51.73 against a tracker integral of $455.38. Rows
        # written by the fixed gate carry hf_covered_s; rows that have an
        # earned_hf but no hf_covered_s are exactly the damaged ones. Rebuild
        # those from the tracker's own data, which is complete for those days,
        # and mark them so the repair cannot run twice or touch anything else.
        try:
            for h in self.state.get("history") or []:
                if "earned_hf" not in h or "hf_covered_s" in h or h.get("hf_repaired"):
                    continue
                reb = tracker_day_integral(h.get("day"))
                if not reb:
                    continue
                was = h.get("earned")
                h["earned"] = reb[0]
                h["earned_sparse"] = reb[0]
                h["hf_repaired"] = {"was": was, "reason": "partial-day earned_hf"}
                print(f"[history] {h['day']}: repaired {was} -> {reb[0]:.2f} "
                      f"(earned_hf covered only part of the day)")
        except Exception as e:  # noqa: BLE001 — a failed repair never blocks boot
            print(f"[history] repair skipped: {type(e).__name__}: {e}")
        # Backfill: if the restored counter is materially below what the
        # hourly tracker's data says today has produced, rebuild from that —
        # outages and state loss stop costing the day's number.
        self.backfilled: float | None = None
        try:
            today = dt.datetime.now(ET).strftime("%Y-%m-%d")
            if self.state.get("day") in (None, today):
                rebuilt = tracker_day_integral(today)
                cur = self.state.get("earned") or 0.0
                if rebuilt and rebuilt[0] > cur + 1.0:
                    self.state["day"] = today
                    self.state["earned"] = rebuilt[0]
                    pm = self.state.setdefault("per_market", {})
                    for m, v in rebuilt[1].items():
                        pm[m] = max(pm.get(m, 0.0), v)
                    self.backfilled = rebuilt[0]
                elif rebuilt and cur > max(rebuilt[0], 0.5) * 1.5:
                    # Counter grossly ABOVE what the (corrected) tracker data
                    # supports — e.g. a mispriced pool inflated the accrual.
                    # Adopt the rebuilt figure and rescale today's curves so
                    # the graph keeps its shape at the honest height.
                    scale = rebuilt[0] / cur if cur > 0 else 0.0
                    self.state["day"] = today
                    self.state["earned"] = rebuilt[0]
                    self.state["per_market"] = rebuilt[1]
                    self.state["rate"] = round((self.state.get("rate") or 0.0) * scale, 4)
                    self.state["market_rates"] = {
                        m: round(v * scale, 4)
                        for m, v in (self.state.get("market_rates") or {}).items()}
                    for key in ("earned_series", "rate_series"):
                        self.state[key] = [[t, round(v * scale, 4)]
                                           for t, v in self.state.get(key) or []]
                    self.backfilled = rebuilt[0]
        except Exception:  # noqa: BLE001 — backfill is best-effort
            pass
        self.last_ts: dt.datetime | None = None
        self.rate = float(self.state.get("rate") or 0.0)
        self.market_rates: dict[str, float] = dict(self.state.get("market_rates") or {})
        if self.state.get("ts"):
            try:  # credit the (capped) deploy gap using the pre-restart rate
                self.last_ts = dt.datetime.fromisoformat(self.state["ts"])
            except Exception:  # noqa: BLE001
                pass
        self.orders: list[dict] = []
        self.error: str | None = None
        self.updated: dt.datetime | None = None
        self._last_remote_save = 0.0
        self.persistence = "github" if GITHUB_TOKEN else "local only — resets on redeploy"
        self.positions: dict[str, dict] = {}  # raw /v1/portfolio/positions, for the P/L tab
        self.activity_pnl: dict[str, dict] = {}  # closed/settled markets, from activities
        self.trades: list[dict] = []  # recent fills, for the landing page
        self.order_snaps: list[dict] = []  # rolling 2-min order snapshots (24h, memory-only)
        self.day_paid: dict = {}  # date -> {paid, pending} from the rewards history
        self.day_profile: list[float] | None = None  # 25-pt cumulative ET curve
        self._last_snap = 0.0
        self.pnl_updated: dt.datetime | None = None
        self.pnl_error: str | None = None
        self.buying_power: float | None = None  # available cash, for the Plan tab
        # Warm-up: books refill gradually after a reboot; until each market's
        # book arrives, its last saved rate stands in so a deploy doesn't look
        # like earnings collapsing to zero.
        self._boot_rates: dict[str, float] = dict(self.state.get("market_rates") or {})
        self._boot_ts: float = time.time()
        self.warming: int = 0
        self.pending_alerts: list[tuple[str, str, str]] = []
        # Auto-defend config survives deploys with the rest of the state.
        self.state.setdefault("defend", {})
        self._apply_defend_seed()
        tr.PRIORITY_SLUGS = set(self.state["defend"])

    def _apply_defend_seed(self, seed: dict | None = None) -> None:
        """Adopt the defend seed once, per version bump.

        `seed` lets the poll loop hand in a copy fetched from GitHub, so a
        config change lands within a poll instead of waiting for a redeploy.
        With no argument the file baked into the image is used (boot path).

        Lets a batch of markets be armed from a commit instead of twenty taps on
        a phone. Version-gated — nothing happens until the file's version rises.

        On a bump: markets not currently defended are armed, and caps the seed
        itself last wrote are moved to the new value. A cap you changed by hand
        is recognised (it no longer matches what the seed last wrote) and left
        alone. Note a market you stopped defending IS re-armed by a bump, since
        the seed is the declared intent for these markets — stop it again after,
        or drop it from the file.
        """
        if seed is None:
            path = Path(__file__).with_name("defend_seed.json")
            if not path.exists():
                return
            try:
                seed = json.loads(path.read_text())
            except Exception as e:  # noqa: BLE001 — a bad seed must never block boot
                print(f"[defend-seed] unreadable, ignored: {e}", flush=True)
                return
        if not isinstance(seed, dict):
            return
        version = int(seed.get("version") or 0)
        if version <= int(self.state.get("defend_seed_v") or 0):
            return
        # what this seed wrote last time, so hand edits can be told apart
        prior = self.state.setdefault("defend_seed_caps", {})
        added = updated = kept = 0
        hit_ceiling = False
        for slug, sides in (seed.get("defend") or {}).items():
            clean = {}
            for side in ("BUY", "SELL"):
                cap = ((sides or {}).get(side) or {}).get("cap")
                if cap is None:
                    continue
                try:
                    c = float(cap)
                except (TypeError, ValueError):
                    continue
                if 0.1 <= c <= 99.9:
                    clean[side] = {"cap": c}
                    sh = ((sides or {}).get(side) or {}).get("share")
                    if sh is not None:
                        try:
                            shv = float(sh)
                        except (TypeError, ValueError):
                            shv = None
                        if shv is not None and 0.05 <= shv <= 0.95:
                            clean[side]["share"] = shv
            if not clean:
                continue
            wrote: dict = {}
            cur = self.state["defend"].get(slug)
            if cur is None:
                if len(self.state["defend"]) >= DEFEND_MAX_MARKETS:
                    print(f"[defend-seed] cap {DEFEND_MAX_MARKETS} reached — "
                          f"{slug} and any after it skipped; version NOT recorded "
                          f"so a later pass can finish", flush=True)
                    hit_ceiling = True
                    break
                self.state["defend"][slug] = clean
                wrote = {s_: dict(c_) for s_, c_ in clean.items()}
                added += 1
            else:
                was = prior.get(slug) or {}
                for side, cfg in clean.items():
                    live_cap = (cur.get(side) or {}).get("cap")
                    seeded_cap = (was.get(side) or {}).get("cap")
                    # Is this cap ours to move? Either it matches what we last
                    # wrote, or it matches a cap this seed is known to have
                    # shipped (prior_caps) — which covers markets armed before
                    # the bookkeeping existed, and records that went stale.
                    owned = (live_cap is not None and seeded_cap is not None
                             and abs(live_cap - seeded_cap) < 1e-9)
                    if not owned and live_cap is not None:
                        for pc in (seed.get("prior_caps") or []):
                            try:
                                if abs(live_cap - float(pc)) < 1e-9:
                                    owned = True
                                    break
                            except (TypeError, ValueError):
                                continue
                    if live_cap is None:
                        cur[side] = dict(cfg); updated += 1
                        wrote[side] = dict(cfg)
                    elif owned:
                        if abs(live_cap - cfg["cap"]) > 1e-9:
                            cur[side] = dict(cfg); updated += 1
                        wrote[side] = dict(cfg)
                    else:
                        kept += 1   # set by hand — the seed does not touch it
            # Record ONLY what was actually written. Recording the seed's
            # intent for a market it skipped makes the next run believe the
            # seed owns a cap it never set, freezing that market forever.
            if wrote:
                prior.setdefault(slug, {}).update(wrote)
        # Only bank the version if the whole seed was applied. Stopping at the
        # ceiling and recording it anyway would strand every market after the
        # cut-off, since the version never rises again to retry them.
        if not hit_ceiling:
            self.state["defend_seed_v"] = version
        print(f"[defend-seed] v{version}: armed {added}, raised {updated}, "
              f"left {kept} hand-set; now defending {len(self.state['defend'])}",
              flush=True)

    def merge_fills(self, rows: list[dict]) -> None:
        """Merge a quick fills page (newest first) into the fills list —
        updating orders that filled further, prepending new ones — without
        losing the older history the full sweep collected."""
        if not rows:
            return
        with self.lock:
            fresh_oids = {r.get("oid") for r in rows}
            self.trades = (rows + [t for t in self.trades
                                   if t.get("oid") not in fresh_oids])[:120]

    def note_fills_alert(self) -> None:
        """Phone alert for fills (bought/sold something), by request. The
        fills list is per-order with the newest execution time; anything
        newer than the persisted marker is announced once. First run seeds
        the marker silently so history isn't replayed."""
        with self.lock:
            seen = self.state.get("fill_seen_ts")
            newest = max((t.get("ts_s") or 0.0 for t in self.trades), default=0.0)
            if seen is None:
                self.state["fill_seen_ts"] = newest
                return
            fresh = [t for t in self.trades if (t.get("ts_s") or 0.0) > seen]
            if not fresh:
                return
            self.state["fill_seen_ts"] = max(newest, seen)
            lines = []
            for t in fresh[:4]:
                px = f" at {t['price_cents']:g}¢" if t.get("price_cents") is not None else ""
                n = f"{t.get('filled') or 0:g}"
                pnl = t.get("pnl")
                ptxt = (f" ({'profit +' if pnl > 0 else 'loss -'}${abs(pnl):.2f})"
                        if pnl else "")
                lines.append(f"{t.get('verb', 'Traded')} {n} {t.get('yesno', '')}"
                             f"{px}{ptxt} — {t.get('market', '')}")
            if len(fresh) > 4:
                lines.append(f"+{len(fresh) - 4} more")
            title = "Order filled" if len(fresh) == 1 else f"{len(fresh)} orders filled"
            self.pending_alerts.append((title, "\n".join(lines), "high"))

    def note_rewards_total(self, total: float) -> None:
        """Phone alert when LP rewards were paid: lifetime credited total
        (from the tracker's rewards history) grew since last seen."""
        with self.lock:
            prev = self.state.get("rew_total")
            if prev is None:
                self.state["rew_total"] = round(total, 2)
                return
            if total > prev + 0.005:
                self.pending_alerts.append(
                    ("LP rewards paid",
                     f"+${total - prev:.2f} credited (lifetime ${total:,.2f})", "default"))
            self.state["rew_total"] = round(total, 2)

    def note_markets(self, keys: list[str], kind: str) -> None:
        """Track the universe of markets (or golf tournaments) we can see, and
        record anything newly listed for the landing page. The very first
        sighting of a kind seeds the known set silently — otherwise every
        market would be 'new' on day one."""
        keys = [k for k in keys if k]
        if not keys:
            return
        with self.lock:
            known = self.state.setdefault("known_mkts", {})
            first = kind not in known
            seen = set(known.get(kind) or [])
            fresh = sorted(set(keys) - seen)
            if not fresh:
                return
            known[kind] = sorted(seen | set(fresh))[-5000:]
            if first:
                return
            now = time.time()
            lst = self.state.setdefault("new_mkts", [])
            for k in fresh:
                lst.append({"ts": round(now, 1),
                            "when": dt.datetime.now(ET).strftime("%b %d"),
                            "label": k, "kind": kind})
            cutoff = now - 14 * 86400
            self.state["new_mkts"] = [e for e in lst if e["ts"] >= cutoff][-120:]
            what = "market" if kind == "politics" else "golf tournament"
            title = (f"New {what}" if len(fresh) == 1
                     else f"{len(fresh)} new {what}s")
            body = "\n".join(fresh[:5]) + (f"\n+{len(fresh) - 5} more" if len(fresh) > 5 else "")
            self.pending_alerts.append((title, body, "default"))

    def note_batch_order(self, order_id: str) -> None:
        """Remember an order the Plan tab placed, so the earnings list can badge it."""
        if not order_id:
            return
        with self.lock:
            ids = self.state.setdefault("batch_ids", [])
            if order_id not in ids:
                ids.append(order_id)
                del ids[:-2000]

    def set_positions(self, positions: dict[str, dict]) -> None:
        with self.lock:
            self.positions = positions
            self.pnl_updated = dt.datetime.now(dt.timezone.utc)

    def _pnl(self) -> dict:
        """P/L per market from the portfolio positions (called under lock).
        Unrealized = current cash value − cost of the open position; the
        exchange reports realized P/L (closed trades + resolutions) directly."""
        rows = []
        totals = {"cash": 0.0, "realized": 0.0, "unrealized": 0.0, "total": 0.0}
        for slug, p in self.positions.items():
            net = tr._num(p.get("netPosition"))
            bought, sold = tr._num(p.get("qtyBought")), tr._num(p.get("qtySold"))
            cost, cash = tr._num(p.get("cost")), tr._num(p.get("cashValue"))
            realized = tr._num(p.get("realized"))
            if not (net or bought or sold or realized or cash):
                continue  # never traded at all — nothing to show
            unrealized = cash - cost
            ts, traded = 0.0, None
            if p.get("updateTime"):
                try:
                    t = dt.datetime.fromisoformat(str(p["updateTime"]).replace("Z", "+00:00"))
                    ts = t.timestamp()
                    traded = t.astimezone(ET).strftime("%b %d %I:%M %p ET")
                except Exception:  # noqa: BLE001
                    pass
            rows.append({
                "market": slug,
                "net": net,
                "avg_cents": round(cost / net * 100, 2) if net else None,
                "cost": round(cost, 2), "cash": round(cash, 2),
                "realized": round(realized, 2), "unrealized": round(unrealized, 2),
                "total": round(realized + unrealized, 2),
                "expired": bool(p.get("expired")),
                "traded": traded, "_ts": ts,
            })
            totals["cash"] += cash
            totals["realized"] += realized
            totals["unrealized"] += unrealized
            totals["total"] += realized + unrealized
        # Closed/settled markets the positions endpoint no longer returns:
        # realized P/L reconstructed from trade + resolution activity.
        for slug, e in (self.activity_pnl or {}).items():
            if slug in self.positions:
                continue
            realized = e["final"] if e.get("final") is not None else e["realized"]
            if abs(realized) < 0.005 and not e.get("resolved"):
                continue
            ts, traded = 0.0, None
            if e.get("ts"):
                try:
                    t = dt.datetime.fromisoformat(str(e["ts"]).replace("Z", "+00:00"))
                    ts = t.timestamp()
                    traded = t.astimezone(ET).strftime("%b %d %I:%M %p ET")
                except Exception:  # noqa: BLE001
                    pass
            rows.append({"market": slug, "net": 0, "avg_cents": None,
                         "cost": 0.0, "cash": 0.0,
                         "realized": round(realized, 2), "unrealized": 0.0,
                         "total": round(realized, 2),
                         "expired": bool(e.get("resolved")), "closed": True,
                         "traded": traded, "_ts": ts})
            totals["realized"] += realized
            totals["total"] += realized
        rows.sort(key=lambda r: (-r["_ts"], -r["total"]))  # most recently traded first
        for r in rows:
            r.pop("_ts")
        return {
            "rows": rows,
            "totals": {k: round(v, 2) for k, v in totals.items()},
            "updated": (self.pnl_updated.astimezone(ET).strftime("%I:%M:%S %p ET")
                        if self.pnl_updated else None),
            "error": self.pnl_error,
        }

    def drain_alerts(self) -> list[tuple[str, str, str]]:
        with self.lock:
            out = self.pending_alerts[:]
            self.pending_alerts.clear()
        return out

    def sample(self, now_utc: dt.datetime, orders: list[dict]) -> None:
        """Integrate earnings since the previous sample, then adopt the new rate."""
        day = now_utc.astimezone(ET).strftime("%Y-%m-%d")
        with self.lock:
            # Integrate the elapsed interval into the day it belongs to…
            if self.last_ts is not None:
                frac = min((now_utc - self.last_ts).total_seconds(), MAX_GAP_SECONDS) / 86400.0
                if frac > 0:
                    self.state["earned"] += self.rate * frac
                    for m, r in self.market_rates.items():
                        self.state["per_market"][m] = self.state["per_market"].get(m, 0.0) + r * frac
            # earned_hf is NOT accrued here. This loop is woken by POLL_KICK the
            # instant we place, reprice or cancel, so its sample times are
            # correlated with our own tending — exactly when our share is at its
            # peak. hf_sampler_loop() accrues it instead, on a Poisson clock
            # that nothing we do can pull.
            # …then roll the day over at midnight ET.
            old_day_earned = None
            if self.state["day"] != day:
                if self.state["day"]:
                    # Days close on the hourly record for continuity, but that
                    # figure is NOT trustworthy: measured against actual
                    # payouts it ran 1.58x-2.03x high, not the ~98% once
                    # claimed here. It rebuilds the day from estimates.csv,
                    # which held 31 snapshots on 2026-08-09 — 0.04% of the
                    # 86,400 the exchange scores, and taken right after we
                    # place or defend, when our share is at its peak.
                    # `earned_hf` is the same integral at ~93x the sampling
                    # density. Both are recorded; the day both are compared
                    # against enough real payouts is the day one gets retired.
                    old_day_earned = round(self.state["earned"], 2)
                    try:
                        reb = tracker_day_integral(self.state["day"])
                        if reb is not None:
                            old_day_earned = reb[0]
                    except Exception:  # noqa: BLE001 — fall back to accrual
                        pass
                    hf_day = round(self.state.get("earned_hf", 0.0), 2)
                    covered = self.state.get("hf_covered_s") or 0.0
                    enough = self.hf_covers_day(full_day=True)
                    self.state["history"] = (self.state["history"] + [
                        # `earned` is the headline the history chart draws;
                        # the other two are kept so estimator_check.yml can
                        # keep scoring both methods against real payouts.
                        # hf_covered_s records WHY earned is what it is, and
                        # its presence marks a row written by the fixed gate.
                        {"day": self.state["day"],
                         "earned": hf_day if enough else old_day_earned,
                         "earned_sparse": old_day_earned,
                         "earned_hf": hf_day,
                         "hf_samples": self._hf_samples,
                         "hf_covered_s": round(covered)}
                    ])[-30:]
                self.state.update({"day": day, "earned": 0.0, "per_market": {},
                                   "earned_hf": 0.0, "per_market_hf": {},
                                   "hf_covered_s": 0.0,
                                   "earned_series": [], "rate_series": []})
                self._hf_samples = 0
            self._hf_samples = getattr(self, "_hf_samples", 0) + 1
            self.rate = sum(o.get("est_day") or 0.0 for o in orders)
            self.market_rates = {}
            for o in orders:
                if o.get("est_day"):
                    self.market_rates[o["market"]] = self.market_rates.get(o["market"], 0.0) + o["est_day"]
            # Warm-up substitution: a market whose orders are ALL unscored only
            # because its book hasn't been fetched yet keeps its last saved
            # rate for up to 20 minutes after boot.
            warming: dict[str, float] = {}
            if time.time() - self._boot_ts < 1200 and self._boot_rates:
                by_mkt: dict[str, list] = {}
                for o in orders:
                    if o.get("market"):
                        by_mkt.setdefault(o["market"], []).append(o)
                for m, os_ in by_mkt.items():
                    if m in self._boot_rates and m not in self.market_rates \
                            and all(o.get("est_day") is None for o in os_) \
                            and any("book" in (o.get("verdict") or "") for o in os_):
                        warming[m] = self._boot_rates[m]
            self.warming = len(warming)
            for m, r in warming.items():
                self.market_rates[m] = r
                self.rate += r
            # Per-market rate history for the graphs: 1-minute buckets, ~8h,
            # including zero-rate markets so dead orders chart their flatline.
            rates_all: dict[str, float] = {}
            for o in orders:
                if o.get("market"):
                    rates_all[o["market"]] = rates_all.get(o["market"], 0.0) + (o.get("est_day") or 0.0)
            minute = int(now_utc.timestamp() // 60) * 60
            series = self.state.setdefault("series", {})
            for mkt, r in rates_all.items():
                s = series.setdefault(mkt, [])
                if s and s[-1][0] == minute:
                    s[-1][1] = round(r, 4)
                else:
                    s.append([minute, round(r, 4)])
                del s[:-480]
            cutoff = minute - 8 * 3600
            self.state["series"] = {
                mkt: [p for p in s if p[0] >= cutoff]
                for mkt, s in series.items() if s and s[-1][0] >= cutoff
            }
            # The full series is excluded from the saved state — it is large
            # and rebuilds in hours. But the dilution signal built on it would
            # then be blind for hours after every restart, which on a night of
            # frequent deploys means blind almost always. Peak and current per
            # market is two floats each, so that much is worth carrying.
            self.state["rate_peak"] = {
                mkt: [round(max(v for _, v in s), 4), round(s[-1][1], 4)]
                for mkt, s in self.state["series"].items() if len(s) >= 5
            }
            # Cumulative earned-today curve for the overall graph. Plots the
            # same basis as the hero number, so the curve and the figure above
            # it can never disagree.
            g_earned, _, g_rate, _ = self.headline()
            es = self.state.setdefault("earned_series", [])
            if es and es[-1][0] == minute:
                es[-1][1] = round(g_earned, 4)
            else:
                es.append([minute, round(g_earned, 4)])
            del es[:-1500]
            # Overall earning-rate curve ($/day) — what the big graph plots.
            rs = self.state.setdefault("rate_series", [])
            if rs and rs[-1][0] == minute:
                rs[-1][1] = round(g_rate, 4)
            else:
                rs.append([minute, round(g_rate, 4)])
            del rs[:-1500]
            self.last_ts = now_utc
            self.orders = orders
            # Rolling restore snapshots: what was resting, every ~2 minutes.
            if now_utc.timestamp() - self._last_snap >= 120:
                self._last_snap = now_utc.timestamp()
                self.order_snaps.append({"ts": self._last_snap, "orders": [
                    {"id": o.get("id"), "market": o.get("market"), "side": o.get("side"),
                     "price": o.get("price"), "size": o.get("size"),
                     "intent": o.get("intent")} for o in orders if o.get("id")]})
                del self.order_snaps[:-720]  # ~24h
            self.updated = now_utc
            self.state["saved_at"] = now_utc.timestamp()
            self.state["rate"] = self.rate
            self.state["market_rates"] = self.market_rates
            self.state["ts"] = now_utc.isoformat()
            try:
                STATE_PATH.write_text(json.dumps(self.state))
            except Exception:  # noqa: BLE001 — read-only disk: keep running in memory
                pass

    def maybe_save_remote(self) -> None:
        """Called from the poll loop (outside the lock) — throttled remote save."""
        if not GITHUB_TOKEN or time.time() - self._last_remote_save < SAVE_INTERVAL:
            return
        with self.lock:
            copy = json.loads(json.dumps(self.state))
        if save_remote_state(copy):
            self._last_remote_save = time.time()

    def snapshot(self) -> dict:
        with self.lock:
            _h_earned, _h_per, _h_rate, _h_basis = self.headline()
            batch_ids = set(self.state.get("batch_ids") or [])
            day_end = None
            if self.state.get("day"):
                try:
                    d0 = dt.datetime.strptime(self.state["day"], "%Y-%m-%d").replace(tzinfo=ET)
                    day_end = (d0 + dt.timedelta(days=1)).timestamp()
                except Exception:  # noqa: BLE001
                    pass
            return {
                "day": self.state["day"],
                "earned_series": self.state.get("earned_series", []),
                "rate_series": self.state.get("rate_series", []),
                "day_end": day_end,
                "earned_today": round(_h_earned, 4),
                "rate_per_day": round(_h_rate, 2),
                "earned_basis": _h_basis,   # "hf" = unbiased sampler, "sparse" = old accrual
                "hf_points": list(self.hf_points),   # raw Poisson samples for the graph
                "per_market_today": {m: round(v, 4) for m, v in sorted(
                    _h_per.items(), key=lambda kv: -kv[1])},
                "orders": [
                    {**{k: o.get(k) for k in ("id", "market", "side", "price", "size", "ticks", "share",
                                              "est_day", "verdict", "window", "window_more",
                                              "window_more_score", "denom", "df", "calc",
                                              "event_n", "siblings", "side_pool")},
                     "batch": o.get("id") in batch_ids}
                    for o in self.orders
                ],
                "history": [
                    {**h, **({"paid": self.day_paid[h["day"]]["paid"],
                              "pending": self.day_paid[h["day"]]["pending"]}
                             if h.get("day") in self.day_paid else {"paid": None})}
                    for h in self.state["history"][-7:][::-1]],
                "updated": (
                    self.updated.astimezone(ET).strftime("%Y-%m-%d %I:%M:%S %p ET")
                    if self.updated else None
                ),
                "error": self.error,
                "diag": {k: v for k, v in tr.LAST_DEBUG.items() if k.startswith("_")},
                "pnl": self._pnl(),
                "buying_power": self.buying_power,
                "warming": self.warming,
                "backfilled": self.backfilled,
                "poll_seconds": POLL_SECONDS,
                "persistence": (
                    f"github — SAVES FAILING ({SAVE_STATUS['err']})"
                    if GITHUB_TOKEN and SAVE_STATUS["err"]
                    and time.time() - SAVE_STATUS["ok_ts"] > 600
                    else self.persistence
                ),
                "alerts": "ntfy" if NTFY_TOPIC else "off",
                "pace_cum": getattr(self, "day_profile", None),
                "ws": {"live": (WS_STATUS["state"] == "live"
                                and time.time() - WS_STATUS["last_msg"] < 300),
                       "markets": WS_STATUS["markets"],
                       "state": WS_STATUS["state"],
                       "err": WS_STATUS["err"]},
                "actions": ACTIONS[-10:][::-1],
                # Every fill carries WHOSE order it was. Owner, 2026-08-16:
                # "I'm getting fills but don't know if they are from the earner
                # or others — I'm tempted to just cancel all my orders so I can
                # be sure." Cancelling everything to identify a fill is an
                # expensive way to ask a question the feed can already answer,
                # so each loop keeps the ids it placed and the answer is
                # attached here. Registries are cleared when an order retires,
                # so this reads the durable id sets, not the live registries.
                "trades": [{**t, "src": _fill_src(str(t.get("oid") or ""))}
                           for t in self.trades[:60]],
                "drops": self._drops(),
                "winners": self._missed_winners(),
                "new_mkts": (self.state.get("new_mkts") or [])[::-1],
                "defend": sorted(self.state.get("defend") or {}),
            }

    def _drops(self) -> list[dict]:
        """Markets earning well below their peak of the stored (~8h) window —
        called under lock."""
        out = []
        for m, s in (self.state.get("series") or {}).items():
            if len(s) < 5:
                continue
            peak = max(v for _, v in s)
            cur = s[-1][1]
            if peak >= 0.25 and peak - cur >= max(0.25, 0.3 * peak):
                out.append({"market": m, "was": round(peak, 2), "now": round(cur, 2)})
        out.sort(key=lambda d: -(d["was"] - d["now"]))
        return out[:10]

    def _missed_winners(self) -> list[dict]:
        """Historical earners (paid rewards) with no current resting order —
        called under lock. Sends extra rows so client-side dismissals
        ('no good anymore') don't shrink the list below ten."""
        cur = {o.get("market") for o in self.orders}
        return [w for w in WINNERS if w["market"] not in cur][:25]


MONITOR = Monitor()
KEY_ID = ""
SECRET_KEY = ""
POLL_KICK = threading.Event()  # set after a reprice so the next poll runs immediately

# ---- Unbiased earnings sampler ---------------------------------------------
# The exchange scores a RANDOM snapshot of the book every second and weights
# all 86,400 equally. Two things made our own sampling a biased estimator of
# that average, both of them self-inflicted:
#
#   1. POLL_KICK wakes the poll loop the moment we place, reprice or cancel,
#      so we sampled precisely when our order had just been pushed to the
#      touch and our share was at its maximum.
#   2. A fixed cadence can beat against anything else periodic — the defend
#      cooldown, a rival's bot on a round interval — and lock onto one phase
#      of a repeating cycle.
#
# This sampler fixes both. It runs on its own thread with EXPONENTIAL waits,
# which makes the sample times a Poisson process: memoryless, so the next
# sample is independent of when the last one fell and of anything we just did.
# It never reads POLL_KICK. It costs no API calls — it re-scores the orders we
# already hold against the WebSocket-fresh book cache — so the mean interval
# can be short without spending request budget.
SAMPLE_MEAN_SECONDS = float(os.environ.get("SAMPLE_MEAN_SECONDS", "5"))


def _rescore_rate() -> tuple[float, dict[str, float], int, int]:
    """(rate, per-market, books fresh enough to score, orders considered).

    Only scores against books newer than BOOK_MAX_AGE. The cache keeps its
    last value forever when the stream and REST both stop — during an exchange
    maintenance window every book goes quiet at once — and re-scoring a frozen
    book returns the same number indefinitely. That reads as a beautifully
    stable rate and is really just our own feed standing still, so the caller
    must know how much of the book it is actually seeing before accruing.
    """
    progs = tr._PROG_CACHE.get("progs") or {}
    now = time.time()
    total = 0.0
    per: dict[str, float] = {}
    fresh = considered = 0
    for o in list(MONITOR.orders):
        slug = o.get("market")
        if not slug:
            continue
        cached = tr._BOOK_CACHE.get(slug)
        prog = progs.get(slug)
        if not prog or not prog.get("pool"):
            continue
        considered += 1
        if not cached or now - cached[0] > BOOK_MAX_AGE:
            continue
        fresh += 1
        probe = {"market": slug, "side": o["side"], "price": o["price"], "size": o["size"]}
        try:
            tr._score_order(probe, cached[1], prog)
        except Exception:  # noqa: BLE001 — one unscorable order never stops the sweep
            continue
        est = probe.get("est_day") or 0.0
        if est:
            total += est
            per[slug] = per.get(slug, 0.0) + est
    return total, per, fresh, considered


def hf_sampler_loop() -> None:
    """Accrue earned_hf on a Poisson clock, independent of everything we do."""
    last = time.time()
    while True:
        time.sleep(random.expovariate(1.0 / SAMPLE_MEAN_SECONDS))
        now = time.time()
        # advance the clock even on a skipped tick, or a quiet stretch would
        # later be charged in full at whatever rate happens to come next
        elapsed = min(now - last, MAX_GAP_SECONDS)
        last = now
        if not MONITOR.orders or elapsed <= 0:
            continue
        try:
            rate, per, fresh, considered = _rescore_rate()
        except Exception:  # noqa: BLE001 — measurement never kills its own thread
            continue
        # A dead feed must not be recorded as a steady rate. When most books
        # have gone stale — maintenance, a dropped stream, a rate-limit stall —
        # accrue NOTHING and bank the elapsed time as a gap instead. Carrying
        # on at the last known rate would quietly invent hours of earnings
        # during exactly the windows we least understand.
        if considered and fresh < considered * HF_MIN_FRESH:
            with MONITOR.lock:
                MONITOR.state["hf_stale_s"] = MONITOR.state.get("hf_stale_s", 0.0) + elapsed
                MONITOR.hf_fresh = (fresh, considered)
            continue
        frac = elapsed / 86400.0
        with MONITOR.lock:
            MONITOR.state["earned_hf"] = MONITOR.state.get("earned_hf", 0.0) + rate * frac
            # Wall time genuinely measured today. Stale ticks are NOT counted:
            # time we could not see is not time we covered.
            MONITOR.state["hf_covered_s"] = MONITOR.state.get("hf_covered_s", 0.0) + elapsed
            pm = MONITOR.state.setdefault("per_market_hf", {})
            for m, r in per.items():
                pm[m] = pm.get(m, 0.0) + r * frac
            MONITOR._hf_samples += 1
            # Smooth the displayed $/day over ~HF_RATE_TAU. A single Poisson
            # sample is an honest instant but a jumpy headline: in a deep book
            # scoring flips between full and zero second to second, so the raw
            # number would flicker even though the day's rate is steady.
            a = 1.0 - pow(2.718281828459045, -elapsed / HF_RATE_TAU)
            MONITOR.hf_rate = rate if MONITOR.hf_rate is None else \
                MONITOR.hf_rate + a * (rate - MONITOR.hf_rate)
            MONITOR.hf_fresh = (fresh, considered)
            MONITOR.hf_points.append([round(now, 1), round(rate, 2)])
            del MONITOR.hf_points[:-HF_POINTS_KEPT]


ACTIONS: list[dict] = []  # audit log of every reprice: request + raw response + verification


def fetch_buying_power(key_id: str, secret_key: str) -> float | None:
    """Available buying power from /v1/account/balances (authenticated)."""
    path = "/v1/account/balances"
    r = requests.get(
        tr.TRADE_API + path,
        headers=tr.auth_headers(key_id, secret_key, "GET", path), timeout=20,
    )
    if r.status_code >= 400:
        raise RuntimeError(f"{path} -> {tr._http_err(r)}")
    for b in r.json().get("balances") or []:
        if b.get("buyingPower") is not None:
            return float(b["buyingPower"])
    return None


def fetch_positions(key_id: str, secret_key: str) -> dict[str, dict]:
    """All portfolio positions keyed by market slug (paginated, authenticated)."""
    path = "/v1/portfolio/positions"
    out: dict[str, dict] = {}
    cursor = None
    for _ in range(20):
        params: dict = {"limit": 100}
        if cursor:
            params["cursor"] = cursor
        r = requests.get(
            tr.TRADE_API + path,
            headers=tr.auth_headers(key_id, secret_key, "GET", path),
            params=params, timeout=20,
        )
        if r.status_code >= 400:
            raise RuntimeError(f"{path} -> {tr._http_err(r)}")
        j = r.json()
        out.update(j.get("positions") or {})
        cursor = j.get("nextCursor")
        if j.get("eof") or not cursor:
            break
    return out


def _verify_resting(market: str, side: str, price_value: str,
                    want_id: str | None = None,
                    min_qty: float | None = None) -> tuple[bool, str, float]:
    """Confirm an order is actually resting at the new price.

    Matching on market+side+price alone is not enough once quantity can
    change. The replacement sits at the SAME price and side as the original,
    so a price-only match can be satisfied by the original itself — and the
    exchange caps placement size (a 2,000 request has come back as 273), so a
    replacement can rest far smaller than asked. Verifying by the id the
    placement returned, and reporting the size actually resting, is what stops
    an increase from silently shrinking the position.
    """
    # One look after one second was not enough. On 2026-08-14 the open-order
    # list was lagging placements by several seconds — with ~4,600 orders on
    # it — so replacements that HAD rested were reported missing, the defender
    # gave up, and every stuck ask drifted further from the touch while the
    # alert said the order "may have been cancelled". A controlled test placed
    # six asks in the two worst markets: all six rested, and all six needed
    # about four seconds to appear. So poll instead of glancing.
    deadline = time.time() + VERIFY_MAX_WAIT
    delay = 1.0
    last = "no attempt made"
    try:
        while True:
            time.sleep(delay)
            found, msg, qty, decided = _verify_once(market, side, price_value,
                                                    want_id, min_qty)
            if decided:
                return found, msg, qty
            last = msg
            if time.time() >= deadline:
                return False, last, 0.0
            delay = min(delay * 1.6, 4.0)
    except Exception as e:  # noqa: BLE001
        return False, f"verify failed: {type(e).__name__}: {e}"[:150], 0.0


VERIFY_MAX_WAIT = float(os.environ.get("VERIFY_MAX_WAIT", "12"))


def _verify_once(market: str, side: str, price_value: str,
                 want_id: str | None, min_qty: float | None):
    """One look at the open-order list. `decided` is False only when the
    order simply is not there yet — the caller keeps polling on that."""
    try:
        path = "/v1/orders/open"
        r = requests.request(
            "GET", tr.TRADE_API + path,
            headers=tr.auth_headers(KEY_ID, SECRET_KEY, "GET", path), timeout=20,
        )
        if r.status_code >= 400:
            return False, f"verify fetch HTTP {r.status_code}", 0.0, False
        want = float(price_value)
        for o in r.json().get("orders") or []:
            # a dead record at the target price must not count as "resting" —
            # exactly that false positive is how destroyed replacements passed
            if str(o.get("state") or "") in tr.DEAD_ORDER_STATES:
                continue
            slug = o.get("marketSlug") or (o.get("marketMetadata") or {}).get("slug") or ""
            oside = "BUY" if str(o.get("side", "")).upper().endswith("BUY") else "SELL"
            if slug != market or oside != side:
                continue
            if abs(tr._num(o.get("price")) - want) >= 0.0005:
                continue
            # when the placement handed back an id, only that order counts —
            # otherwise the original, still resting at this price, matches
            if want_id is not None and str(o.get("id")) != str(want_id):
                continue
            qty = tr._num(o.get("leavesQuantity")) or tr._num(o.get("quantity"))
            if min_qty is not None and qty + 1e-9 < min_qty:
                return (False,
                        f"rested at only {qty:,.0f} of the {min_qty:,.0f} asked for",
                        qty, True)
            return True, f"verified resting at {want * 100:g}¢ (id {o.get('id')})", qty, True
        return (False, "NO order found at the new price — it may have been "
                "cancelled; check the app", 0.0, False)
    except Exception as e:  # noqa: BLE001
        return False, f"verify failed: {type(e).__name__}: {e}"[:150], 0.0, True


PLAN_CACHE: dict = {"politics": {"ts": 0.0, "data": None}, "golf": {"ts": 0.0, "data": None},
                    "tt": {"ts": 0.0, "data": None}}
PLAN_FILES = {"politics": "data/scan.json", "golf": "data/scan_golf.json",
              "tt": "data/scan_tt.json"}
RESTORE_LAST: dict = {"ts": 0.0, "data": None}


def _restore_plan(ago: float) -> dict:
    """What was resting ~`ago` seconds back that is neither resting nor
    filled now — rebuilt from the monitor's own rolling snapshots, no
    outside help needed."""
    ago = max(120.0, min(float(ago or 1800), 24 * 3600.0))
    now = time.time()
    with MONITOR.lock:
        snaps = list(MONITOR.order_snaps)
        cur_ids = {o.get("id") for o in MONITOR.orders if o.get("id")}
    target = now - ago
    if not snaps:
        return {"generated": "no snapshots yet since the last deploy — ask the assistant "
                             "to rebuild from the hourly archive instead", "results": []}
    snap = min(snaps, key=lambda s: abs(s["ts"] - target))
    filled = {t.get("oid") for t in MONITOR.trades if (t.get("ts_s") or 0) >= snap["ts"]}
    rows = []
    when = dt.datetime.fromtimestamp(snap["ts"], ET).strftime("%I:%M %p ET")
    for o in snap["orders"]:
        if o["id"] in cur_ids or o["id"] in filled:
            continue  # still resting, or it FILLED (do not re-place a filled order)
        price, size = o.get("price") or 0.0, int(o.get("size") or 0)
        if not (0.001 <= price <= 0.999) or size < 1:
            continue
        side = o.get("side") or "BUY"
        row = {"market": o["market"], "side": side, "restore_ok": True,
               "pick": {"side": side, "price": price, "size": size,
                        "capital": round((price if side == "BUY" else 1 - price) * size, 2),
                        "covered": False, "est_day": 0.0, "share": 0.0},
               "max": None, "risk": None,
               "note": f"was resting at {when}"}
        if "SELL_SHORT" in str(o.get("intent") or ""):
            row["close_short"] = True
        rows.append(row)
    rows.sort(key=lambda r: -r["pick"]["capital"])
    plan = {"generated": f"snapshot {when} — {len(rows)} orders missing", "results": rows}
    RESTORE_LAST.update(ts=now, data=plan)
    return plan


def _spread_plan(pol: dict) -> dict:
    """Derived from the politics scan: markets with the widest bid-ask
    spreads, entered on BOTH sides at the reward Target Size. The advertised
    price is the current touch; the placer re-optimizes each order against
    the live book for maximum reward per dollar (join vs step inside)."""
    rows, seen = [], set()
    for r in pol.get("results") or []:
        m = r.get("market")
        bb, ba = r.get("best_bid"), r.get("best_ask")
        tick = r.get("tick") or 0.01
        prog = r.get("prog") or {}
        target = int(prog.get("target") or 0)
        if not m or m in seen or not bb or not ba or not target or not prog.get("pool"):
            continue
        seen.add(m)
        ticks = round((ba - bb) / tick)
        if ticks < 3:
            continue  # need a tick inside each side AND a gap between our quotes
        pb, pa = round(bb, 4), round(ba, 4)  # baseline: the touch (placer optimizes)
        side_pool = round(tr._daily_pool(prog, m) / 2, 2)  # ~100% share when we ARE the window
        common = {"market": m, "spread_ok": True, "tick": tick,
                  "best_bid": bb, "best_ask": ba,
                  "spread_cents": round((ba - bb) * 100, 1),
                  "side_pool": side_pool, "held": 0, "risk": r.get("risk"),
                  "note": r.get("note"), "prog": prog}
        rows.append({**common, "side": "BUY",
                     "pick": {"side": "BUY", "price": pb, "size": target,
                              "capital": round(pb * target, 2),
                              "covered": False, "est_day": side_pool, "share": 100.0},
                     "max": None})
        rows.append({**common, "side": "SELL",
                     "pick": {"side": "SELL", "price": pa, "size": target,
                              "capital": round((1 - pa) * target, 2),
                              "covered": False, "est_day": side_pool, "share": 100.0},
                     "max": None})
    rows.sort(key=lambda r: (-r["spread_cents"], r["market"], r["side"]))
    return {"generated": pol.get("generated"), "results": rows}


def fetch_plan(which: str = "politics") -> dict:
    """A scan plan file from the repo's main branch (via GITHUB_TOKEN)."""
    if which == "spread":
        return _spread_plan(fetch_plan("politics"))
    if which == "restore":
        # placement validates against the SAME plan the user just viewed
        if RESTORE_LAST["data"] and time.time() - RESTORE_LAST["ts"] < 600:
            return RESTORE_LAST["data"]
        return _restore_plan(1800)
    which = which if which in PLAN_FILES else "politics"
    slot = PLAN_CACHE[which]
    if slot["data"] and time.time() - slot["ts"] < 300:
        return slot["data"]
    if not GITHUB_TOKEN:
        raise RuntimeError("GITHUB_TOKEN not set — the Plan tab needs it to read the scan")
    r = requests.get(
        f"https://api.github.com/repos/{GITHUB_REPO}/contents/{PLAN_FILES[which]}",
        params={"ref": "main"},
        headers={"Authorization": f"Bearer {GITHUB_TOKEN}",
                 "Accept": "application/vnd.github.raw+json"},
        timeout=20,
    )
    if r.status_code >= 400:
        raise RuntimeError(f"{PLAN_FILES[which]} fetch failed: HTTP {r.status_code}"
                           + (" — run the Market scan workflow once" if r.status_code == 404 else ""))
    slot.update(ts=time.time(), data=r.json())
    return slot["data"]


# One batch at a time; progress is polled by the dashboard.
PLACER: dict = {"running": False, "results": [], "total": 0, "abort": False, "summary": ""}
BATCH_SPACING_SECONDS = 2.5  # ~2 requests per order -> stays under the safe req/min


def _place_one(spec: dict, plan_row: dict) -> dict:
    """Revalidate against the LIVE book, then place ONE post-only resting order."""
    slug = spec["market"]
    side = spec.get("side", "BUY")
    price = round(spec["price_cents"] / 100.0, 4)
    size = int(spec["size"])
    res: dict = {"market": slug, "side": side, "price_cents": spec["price_cents"], "size": size}
    try:
        ev = plan_row.get("event_start")
        if ev:  # timed events (table tennis games): never quote once started
            try:
                if dt.datetime.fromisoformat(str(ev).replace("Z", "+00:00")) \
                        <= dt.datetime.now(dt.timezone.utc):
                    res.update(status="skipped", note="event has started — re-run the scan")
                    return res
            except Exception:  # noqa: BLE001 — unparseable start: fall through
                pass
        book = tr._fetch_book(slug)
        bids = book.get("bids") or []
        asks = book.get("asks") or []
        if plan_row.get("join_ok"):  # join-the-touch plans track the LIVE best
            lv = bids if side == "BUY" else asks
            if lv:
                price = lv[0][0]
                res["price_cents"] = round(price * 100, 2)
        if plan_row.get("spread_ok"):
            # Spread entries: spend the approved budget where it earns the
            # MOST — candidates are 1 tick behind the live touch, joining it,
            # and 1-2 ticks inside; each is scored on the merged book at the
            # size the budget buys (capped at Target Size — contracts beyond
            # the window add cost, not reward). Joining is cheaper per
            # contract; stepping inside crushes competitors' df weight. The
            # scorer decides per market.
            tickb = book.get("tick") or 0.01
            bb = bids[0][0] if bids else None
            ba = asks[0][0] if asks else None
            if bb is not None and ba is not None and round((ba - bb) / tickb) < 3:
                res.update(status="skipped", note="spread closed — under 3 ticks now")
                return res
            prog_sp = dict(plan_row.get("prog") or {})
            target_sp = int(prog_sp.get("target") or 0) or 20000
            lockf = (lambda p: p) if side == "BUY" else (lambda p: 1.0 - p)
            budget = lockf(price) * size
            base = (bb if side == "BUY" else ba)
            if base is None:
                base = price
            cands = []
            for off in (-1, 0, 1, 2):  # behind, join, inside, further inside
                p = round(base + (off if side == "BUY" else -off) * tickb, 4)
                if p < 0.001 or p > 0.999:
                    continue
                if side == "BUY" and ba is not None and p >= ba - 1e-9:
                    continue
                if side == "SELL" and bb is not None and p <= bb + 1e-9:
                    continue
                cands.append(p)
            if not cands:
                res.update(status="skipped", note="spread closed — no room to quote")
                return res
            best_c = None
            for p in cands:
                q = max(1, min(int(budget / max(lockf(p), 1e-4)), target_sp, 20000))
                e = 0.0
                if prog_sp.get("pool"):
                    key = "bids" if side == "BUY" else "asks"
                    levels = dict(book.get(key) or [])
                    levels[p] = levels.get(p, 0) + q
                    merged = dict(book)
                    merged[key] = sorted(levels.items(),
                                         key=lambda x: (-x[0] if side == "BUY" else x[0]))
                    probe = {"market": slug, "side": side, "price": p, "size": float(q)}
                    tr._score_order(probe, merged, prog_sp)
                    e = probe.get("est_day") or 0.0
                rank = (round(e, 4), -p if side == "BUY" else p)  # tie: farther from danger
                if best_c is None or rank > best_c[0]:
                    best_c = (rank, p, q, e)
            _, price, size, est_sp = best_c
            res.update(price_cents=round(price * 100, 2), size=size,
                       est_day=round(est_sp, 2))
        crosses = (asks and price >= asks[0][0]) if side == "BUY" else (bids and price <= bids[0][0])
        if crosses:
            res.update(status="skipped", note="would cross the spread now")
            return res
        prog = dict(plan_row.get("prog") or {})
        # Never stand at (or better than) a THIN touch — the book may have
        # moved since the plan. Joining is only safe behind a wall that
        # already holds the full Target Size (price-time: we fill last).
        # Deep quotes are FULLY exempt (buys <= 1.1c, sells >= 98.9c):
        # improving a 0.1c best to 0.2c risks a tenth of a cent per contract,
        # and the cheap-YES strategy accepts fills by design.
        target = prog.get("target") or 0
        deep = ((side == "BUY" and price <= 0.011) or (side == "SELL" and price >= 0.989)
                or bool(plan_row.get("join_ok"))     # 1-share touch plans join by design
                or bool(plan_row.get("spread_ok"))   # spread entries improve by design
                or bool(plan_row.get("restore_ok")))  # restoring what WAS resting there
        if not deep:
            if side == "BUY" and bids and price >= bids[0][0] - 1e-9:
                level = sum(q for px, q in bids if abs(px - price) < 1e-9)
                if price > bids[0][0] + 1e-9 or level < target:
                    res.update(status="skipped", note="book moved — would stand at/above a thin best bid")
                    return res
            if side == "SELL" and asks and price <= asks[0][0] + 1e-9:
                level = sum(q for px, q in asks if abs(px - price) < 1e-9)
                if price < asks[0][0] - 1e-9 or level < target:
                    res.update(status="skipped", note="book moved — would stand at/below a thin best ask")
                    return res
        if prog.get("pool") and not plan_row.get("join_ok"):
            # drift check: still worth placing at today's book? (join-the-touch
            # plans are presence plays — a 1-share order has no est bar to clear)
            probe = {"market": slug, "side": side, "price": price, "size": float(size)}
            key = "bids" if side == "BUY" else "asks"
            levels = dict(book.get(key) or [])
            levels[price] = levels.get(price, 0) + size
            merged = dict(book)
            merged[key] = sorted(levels.items(), key=lambda x: (-x[0] if side == "BUY" else x[0]))
            tr._score_order(probe, merged, prog)
            est = probe.get("est_day") or 0.0
            # The drift floor is relative to what the plan promised for THIS
            # order — small per-golfer allocations legitimately earn cents/day
            # and must not be judged against a politics-sized bar. The size may
            # be a rescale of the planned one (the golf-cap slider): match on
            # price and scale the promise linearly; an exact size match wins.
            planned = None
            for k in ("pick", "max"):
                v = plan_row.get(k) or {}
                if (abs((v.get("price") or -1) - price) < 1e-9
                        and v.get("size") and v.get("est_day")):
                    planned = v["est_day"] * (size / float(v["size"]))
                    if int(v["size"]) == size:
                        planned = v["est_day"]
                        break
            # purely relative when the plan promised pennies (golf floor bids)
            thr = min(0.08, 0.5 * planned) if planned else 0.08
            if est < thr:
                res.update(status="skipped",
                           note=f"drifted — est now ${est:.2f}/day (planned ${planned or 0:.2f})")
                return res
            res["est_day"] = round(est, 2)
        intent = "ORDER_INTENT_BUY_LONG"
        if side == "SELL":  # sell inventory if we hold enough, else open a short
            net = tr._num((MONITOR.positions.get(slug) or {}).get("netPosition"))
            # BUY_SHORT opens a short and rests as an ASK; SELL_SHORT would
            # rest as a BID (it CLOSES a short) — the bidding-against-yourself bug
            intent = "ORDER_INTENT_SELL_LONG" if net >= size else "ORDER_INTENT_BUY_SHORT"
            res["intent"] = intent
        elif plan_row.get("close_short"):  # a restored buy-back of a short
            net = tr._num((MONITOR.positions.get(slug) or {}).get("netPosition"))
            if net >= 0:
                res.update(status="skipped", note="no short position to buy back any more")
                return res
            intent = "ORDER_INTENT_SELL_SHORT"
            res["intent"] = intent
        path = "/v1/orders"
        value = f"{price:.3f}".rstrip("0").rstrip(".")
        # GTC: DAY orders silently expire at 5:00 PM ET (the vanished-orders
        # incident). Only join-the-touch game plans stay DAY — a stale 1-share
        # quote must not rest into a live match.
        tif = ("TIME_IN_FORCE_DAY" if plan_row.get("join_ok")
               else "TIME_IN_FORCE_GOOD_TILL_CANCEL")
        r = requests.request(
            "POST", tr.TRADE_API + path,
            headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", path),
                     "Content-Type": "application/json"},
            json={"marketSlug": slug, "intent": intent,
                  "type": "ORDER_TYPE_LIMIT",
                  "price": {"value": value, "currency": "USD"},
                  "quantity": size, "tif": tif,
                  "participateDontInitiate": True},  # post-only: rest or reject, never fill
            timeout=20,
        )
        if r.status_code < 300:
            oid = ""
            try:
                oid = (r.json() or {}).get("id") or ""
            except Exception:  # noqa: BLE001
                pass
            res.update(status="placed", id=oid)
        else:
            res.update(status="rejected", note=f"HTTP {r.status_code}: {' '.join(r.text.split())[:150]}")
    except Exception as e:  # noqa: BLE001
        res.update(status="error", note=f"{type(e).__name__}: {e}"[:150])
    return res


def run_batch(specs: list[dict], plan_rows: dict[str, dict]) -> None:
    placed = skipped = failed = 0
    consec_err = 0
    try:
        for spec in specs:
            if PLACER["abort"]:
                PLACER["summary"] = "stopped by user"
                break
            res = _place_one(spec, plan_rows.get((spec["market"], spec.get("side", "BUY")), {}))
            PLACER["results"].append(res)
            ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                            "market": res["market"], "side": f"{res.get('side', 'BUY')} (new)", "from": "—",
                            "to": res["price_cents"], "size": res["size"],
                            "status": res["status"],
                            "response": (res.get("note") or res.get("id") or "")[:150],
                            "verified": res["status"] == "placed"})
            if res["status"] == "placed":
                placed += 1
                consec_err = 0
                MONITOR.note_batch_order(res.get("id") or "")
            elif res["status"] == "skipped":
                skipped += 1
            else:
                failed += 1
                if "429" in (res.get("note") or "") or "rate limited" in (res.get("note") or ""):
                    PLACER["summary"] = "rate limited — stopped; wait a few minutes and retry"
                    break  # hammering a rate limiter keeps the ban alive
                consec_err += 1
                if consec_err >= 3:
                    PLACER["summary"] = "stopped after 3 consecutive failures"
                    break
            time.sleep(BATCH_SPACING_SECONDS)
    finally:
        PLACER["summary"] = PLACER["summary"] or "done"
        PLACER["running"] = False
        POLL_KICK.set()  # rescore right away so the new orders show up
        notify("Batch placement finished",
               f"{placed} placed, {skipped} skipped, {failed} failed ({PLACER['summary']})",
               "high" if failed else "default")


def start_batch(payload: dict) -> tuple[int, dict]:
    if PLACER["running"]:
        return 409, {"ok": False, "error": "a batch is already running"}
    try:
        plan = fetch_plan(str(payload.get("which") or "politics"))
    except Exception as e:  # noqa: BLE001
        return 502, {"ok": False, "error": f"can't load plan: {e}"[:200]}
    plan_rows = {(r["market"], r.get("side", "BUY")): r
                 for r in plan.get("results") or [] if r.get("pick")}
    try:
        max_c = float(payload.get("max_price_cents") or 0)
        min_s = float(payload.get("min_sell_cents") or 99)
        specs = payload.get("orders") or []
        assert 0.1 <= max_c <= 99.9, "bad max buy price"
        assert 0.1 <= min_s <= 99.9, "bad min sell price"
        assert 1 <= len(specs) <= 400, "1-400 orders per batch"
        open_now = {(o.get("market"), o.get("side"), round((o.get("price") or 0) * 100, 1))
                    for o in MONITOR.orders}
        clean, precheck_skips = [], []
        for s in specs:
            m, side = str(s.get("market")), str(s.get("side") or "BUY")
            pc, q = float(s.get("price_cents")), int(s.get("size"))
            # security checks stay hard failures — these should be impossible
            assert side in ("BUY", "SELL"), f"{m}: bad side"
            assert (m, side) in plan_rows, f"{m} {side}: not in the scan plan"
            assert 0.1 <= pc <= 99.9 and 1 <= q <= 20000, f"{m}: price/size out of range"
            # slider caps are user config — skip and report, don't kill the batch
            if side == "BUY" and pc > max_c:
                precheck_skips.append(f"{m}: {pc:g}¢ over the max-buy slider")
                continue
            if side == "SELL" and pc < min_s:
                precheck_skips.append(f"{m}: {pc:g}¢ under the min-sell slider")
                continue
            if any(mm == m and ss == side and abs(ppc - pc) <= 1.0 for mm, ss, ppc in open_now):
                continue  # an order already rests within a tick — never double up
            clean.append({"market": m, "side": side, "price_cents": pc, "size": q})
        assert clean, "nothing to place — every order duplicates an existing one or missed the sliders"
    except (AssertionError, TypeError, ValueError, KeyError) as e:
        return 400, {"ok": False, "error": str(e)[:200]}
    PLACER.update(running=True, results=[], total=len(clean), abort=False, summary="")
    threading.Thread(target=run_batch, args=(clean, plan_rows), daemon=True).start()
    return 200, {"ok": True, "started": len(clean),
                 "precheck_skipped": precheck_skips[:20]}


def compute_dead_orders() -> list[dict]:
    """Resting orders earning ~nothing for a DEFINITIVE reason — scored
    against a real book (no program, outside the window, ~0% share). Orders
    whose book simply hasn't been fetched yet are never flagged."""
    out = []
    for o in MONITOR.orders:
        if not o.get("id"):
            continue
        if (o.get("est_day") or 0.0) >= 0.01:
            continue
        v = o.get("verdict") or ""
        if not (v.startswith("❌") or v.startswith("✅")):
            continue  # book unavailable/pending — can't judge, leave alone
        locked = o["price"] * o["size"] if o["side"] == "BUY" else (1 - o["price"]) * o["size"]
        out.append({"id": o["id"], "market": o["market"], "side": o["side"],
                    "price_cents": round(o["price"] * 100, 1), "size": o["size"],
                    "locked": round(locked, 2), "why": v[:90]})
    out.sort(key=lambda r: -r["locked"])
    return out


def run_cancel_batch(specs: list[dict]) -> None:
    done = failed = 0
    consec_err = 0
    try:
        for spec in specs:
            if PLACER["abort"]:
                PLACER["summary"] = "stopped by user"
                break
            res = {"market": spec["market"], "side": spec["side"],
                   "price_cents": spec["price_cents"], "size": spec["size"]}
            try:
                path = f"/v1/order/{spec['id']}/cancel"
                r = requests.request(
                    "POST", tr.TRADE_API + path,
                    headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", path),
                             "Content-Type": "application/json"},
                    json={"marketSlug": spec["market"]}, timeout=20,
                )
                if r.status_code < 300:
                    res["status"] = "cancelled"
                else:
                    res.update(status="rejected", note=tr._http_err(r))
            except Exception as e:  # noqa: BLE001
                res.update(status="error", note=f"{type(e).__name__}: {e}"[:150])
            PLACER["results"].append(res)
            ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                            "market": res["market"], "side": f"{res['side']} (cancel)",
                            "from": res["price_cents"], "to": "—", "size": res["size"],
                            "status": res["status"], "response": (res.get("note") or "")[:150],
                            "verified": res["status"] == "cancelled"})
            if res["status"] == "cancelled":
                done += 1
                consec_err = 0
            else:
                failed += 1
                if "429" in (res.get("note") or "") or "rate limited" in (res.get("note") or ""):
                    PLACER["summary"] = "rate limited — stopped; wait a few minutes and retry"
                    break
                consec_err += 1
                if consec_err >= 3:
                    PLACER["summary"] = "stopped after 3 consecutive failures"
                    break
            time.sleep(BATCH_SPACING_SECONDS)
    finally:
        PLACER["summary"] = PLACER["summary"] or "done"
        PLACER["running"] = False
        POLL_KICK.set()
        notify("Dead-order cleanup finished",
               f"{done} cancelled, {failed} failed ({PLACER['summary']})",
               "high" if failed else "default")


def start_cancel_batch(payload: dict) -> tuple[int, dict]:
    if PLACER["running"]:
        return 409, {"ok": False, "error": "a batch is already running"}
    known = {o.get("id"): o for o in MONITOR.orders if o.get("id")}
    try:
        specs = payload.get("orders") or []
        assert 1 <= len(specs) <= 400, "1-400 orders per batch"
        clean = []
        for s in specs:
            oid = str(s.get("id"))
            o = known.get(oid)
            assert o is not None, f"{oid}: not one of your resting orders"
            clean.append({"id": oid, "market": o["market"], "side": o["side"],
                          "price_cents": round(o["price"] * 100, 1), "size": o["size"]})
    except (AssertionError, TypeError, ValueError) as e:
        return 400, {"ok": False, "error": str(e)[:200]}
    PLACER.update(running=True, results=[], total=len(clean), abort=False, summary="")
    threading.Thread(target=run_cancel_batch, args=(clean,), daemon=True).start()
    return 200, {"ok": True, "started": len(clean)}


def _fill_ts(iso: str) -> tuple[float, str]:
    try:
        d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return round(d.timestamp(), 1), d.astimezone(ET).strftime("%b %d %I:%M %p")
    except Exception:  # noqa: BLE001
        return 0.0, ""


_INTENT_WORDS = {  # intent -> (verb, Yes/No, price is in NO terms?)
    "ORDER_INTENT_BUY_LONG": ("Bought", "Yes", False),
    "ORDER_INTENT_SELL_LONG": ("Sold", "Yes", False),
    "ORDER_INTENT_BUY_SHORT": ("Bought", "No", True),
    "ORDER_INTENT_SELL_SHORT": ("Sold", "No", True),
}


def _collect_fills(t: dict, fills_by_order: dict[str, dict]) -> None:
    """One trade activity = one (often 1-share) execution. Real executions
    only (shares traded, never placements), collapsed to one row per ORDER
    — except when BOTH sides of the trade are ours (our bid and our ask
    crossing each other): that is ONE event, shown as a single 'own orders
    crossed' row instead of a buy plus a sell."""
    # The feed returns BOTH sides of every trade: ours and the counterparty's.
    # Two executions is the normal case, not a self-cross. Treating it as one
    # dropped every fill that had a counterparty -- 1623 of 1623 across the
    # whole history -- which is why the fills list and its alerts went quiet.
    #
    # Ours is the passive side. Every order we place is post-only
    # (participateDontInitiate) and a post-only order can only rest; it can
    # never cross and take. The commission agrees: the aggressor pays a taker
    # fee, the passive side collects a maker rebate. Checked against the live
    # book, the passive order id matched our open orders and the aggressor's
    # never did.
    # OUR side of a trade is the one whose order carries a real intent —
    # the API redacts the counterparty's to ORDER_INTENT_UNDEFINED. The old
    # passive-first pick assumed we always rest; the sniper (which takes on
    # purpose) and the owner's own manual crosses broke that, attributing
    # those fills to the counterparty's order.
    def _ours(ex):
        o_ = (ex or {}).get("order") or {}
        it_ = str(o_.get("intent") or "")
        return o_.get("id") and it_ and not it_.endswith("UNDEFINED")
    pick = t.get("passiveExecution") or {}
    if not _ours(pick):
        pick = t.get("aggressorExecution") or {}
    if not _ours(pick):
        pick = t.get("passiveExecution") or {}
        if not (pick.get("order") or {}).get("id"):
            pick = t.get("aggressorExecution") or {}
    execs = []
    _o = pick.get("order") or {}
    if _o.get("id") and tr._num(pick.get("lastShares")) > 0:
        execs.append((pick, _o))
    rows_this = []
    if True:
        for ex, o in execs:
            oid = str(o.get("id"))
            shares = tr._num(ex.get("lastShares"))
            verb, yesno, no_terms = _INTENT_WORDS.get(
                str(o.get("intent") or ""), ("Bought" if str(o.get("side") or "").endswith("BUY")
                                             else "Sold", "Yes", False))
            px = tr._num(ex.get("lastPx") or o.get("avgPx") or o.get("price"))
            if no_terms:
                px = 1.0 - px  # show No fills at the No price, like the app
            row = fills_by_order.get(oid)
            if row is None:
                if len(fills_by_order) >= 80:
                    continue
                ts_s, when = _fill_ts(str(ex.get("transactTime") or ""))
                fills_by_order[oid] = row = {
                    "oid": oid, "kind": "fill", "verb": verb, "yesno": yesno,
                    "intent": str(o.get("intent") or ""),
                    "market": o.get("marketSlug") or t.get("marketSlug") or "",
                    "filled": 0.0, "_val": 0.0, "price_cents": None,
                    "ts_s": ts_s, "when": when, "pnl": 0.0}
            row["filled"] += shares
            row["_val"] += shares * px
            row["price_cents"] = round(row["_val"] / row["filled"] * 100, 2)
            rows_this.append(row)
    if not rows_this and t.get("marketSlug"):  # older flat shape (qty/price)
        qty = tr._num(t.get("qty"))
        if qty > 0:
            key = str(t.get("id") or len(fills_by_order))
            ts_s, when = _fill_ts(str(t.get("updateTime") or t.get("createTime") or ""))
            fills_by_order[key] = row = {
                "oid": key, "kind": "fill", "verb": "Traded", "yesno": "Yes",
                "market": t["marketSlug"], "filled": qty, "_val": 0.0,
                "price_cents": (round(tr._num(t.get("price")) * 100, 2)
                                if t.get("price") is not None else None),
                "ts_s": ts_s, "when": when, "pnl": 0.0}
            rows_this.append(row)
    # realizedPnl is the ORDER's running total, restated on every execution —
    # summing it across 50 one-share fills inflates ~25x (triangular numbers).
    # Activities arrive newest first: the first NONZERO value seen per row IS
    # the order's total realized.
    pnl = tr._num(t.get("realizedPnl"))
    for row in rows_this:
        if pnl and not row.get("_pnl_locked"):
            row["pnl"] = pnl
            row["_pnl_locked"] = True


def fetch_recent_fills(key_id: str, secret_key: str) -> list[dict]:
    """ONE cheap page of the newest trade activities — so a fill reaches the
    phone in ~a minute instead of waiting for the 10-minute P/L sweep."""
    path = "/v1/portfolio/activities"
    r = requests.get(tr.TRADE_API + path,
                     headers=tr.auth_headers(key_id, secret_key, "GET", path),
                     params={"limit": 25, "sortOrder": "SORT_ORDER_DESCENDING",
                             "types": ["ACTIVITY_TYPE_TRADE"]}, timeout=20)
    if r.status_code >= 400:
        raise RuntimeError(f"{path} -> {tr._http_err(r)}")
    fills: dict[str, dict] = {}
    for a in r.json().get("activities") or []:
        t = a.get("trade") or {}
        if t:
            _collect_fills(t, fills)
    out = list(fills.values())
    for row in out:
        row["pnl"] = round(row["pnl"], 2) or None
        row.pop("_val", None)
        row.pop("_pnl_locked", None)
    return out


def fetch_activity_pnl(key_id: str, secret_key: str) -> tuple[dict[str, dict], list[dict]]:
    """Per-market realized P/L rebuilt from trade/resolution history — covers
    positions the exchange no longer returns once fully closed or settled.
    Also returns the individual fills (newest first) for the landing page's
    since-you-last-checked list."""
    path = "/v1/portfolio/activities"
    agg: dict[str, dict] = {}
    fills_by_order: dict[str, dict] = {}
    cursor = None
    for _ in range(10):  # up to 1000 most recent activities
        params: dict = {"limit": 100, "sortOrder": "SORT_ORDER_DESCENDING",
                        "types": ["ACTIVITY_TYPE_TRADE", "ACTIVITY_TYPE_POSITION_RESOLUTION"]}
        if cursor:
            params["cursor"] = cursor
        r = requests.get(tr.TRADE_API + path,
                         headers=tr.auth_headers(key_id, secret_key, "GET", path),
                         params=params, timeout=20)
        if r.status_code >= 400:
            raise RuntimeError(f"{path} -> {tr._http_err(r)}")
        j = r.json()
        for a in j.get("activities") or []:
            t = a.get("trade") or {}
            pr = a.get("positionResolution") or {}
            if t:
                _collect_fills(t, fills_by_order)
            if t.get("marketSlug"):
                e = agg.setdefault(t["marketSlug"],
                                   {"realized": 0.0, "ts": "", "resolved": False,
                                    "final": None, "_ord": {}})
                pnl_t = tr._num(t.get("realizedPnl"))
                oid = None
                for exk in ("aggressorExecution", "passiveExecution"):
                    o_ = (t.get(exk) or {}).get("order") or {}
                    if o_.get("id"):
                        oid = str(o_["id"])
                        break
                if oid:  # running total per order: newest-first, first one wins
                    if pnl_t and oid not in e.setdefault("_ord", {}):
                        e["_ord"][oid] = pnl_t
                else:  # legacy flat rows carried per-trade values
                    e["realized"] += pnl_t
                e["ts"] = max(e["ts"], str(t.get("updateTime") or t.get("createTime") or ""))
            elif pr.get("marketSlug"):
                e = agg.setdefault(pr["marketSlug"],
                                   {"realized": 0.0, "ts": "", "resolved": False, "final": None})
                e["resolved"] = True
                after = pr.get("afterPosition") or {}
                if e["final"] is None and after:  # newest activity wins (descending order)
                    e["final"] = tr._num(after.get("realized"))
                e["ts"] = max(e["ts"], str(pr.get("updateTime") or ""))
        cursor = j.get("nextCursor")
        if j.get("eof") or not cursor:
            break
    trades = []
    for row in fills_by_order.values():
        row["pnl"] = round(row["pnl"], 2) or None
        row.pop("_val", None)
        row.pop("_pnl_locked", None)
        trades.append(row)
    for e in agg.values():  # per-order running totals -> per-market realized
        e["realized"] += sum(e.pop("_ord", {}).values())
    return agg, trades


def _book_without(book: dict, side: str, price: float, size: float) -> dict:
    """The book with OUR resting order removed — scoring candidates against a
    book that still contains us double-counts our size."""
    b = dict(book)
    key = "bids" if side == "BUY" else "asks"
    levels = []
    for px, q in b.get(key) or []:
        if abs(px - price) < 1e-9:
            q -= size
            if q <= 0:
                continue
        levels.append((px, q))
    b[key] = levels
    return b


TARGET_ORDER_EST = 0.15  # ~$4.50/month per order — the churn-threshold baseline
EASY_KEEP = 0.8  # take the deepest price still earning this share of the safe max


def _optimal_price(order: dict, book: dict, prog: dict,
                   min_off: int = 1) -> tuple[float | None, float]:
    """Take what the market gives WITHOUT leaving the safe zone: among
    cushioned candidates (>= min_off ticks behind the touch, deep quote
    included), find the max earning, then pick the DEEPEST price still making
    >= EASY_KEEP of it. Easy markets (uncontested sides) yield their full
    money at the deep quote; contested ones step up only when stepping up
    genuinely multiplies the earnings. Joins the touch only as a last resort
    (window entirely at the best level — queued behind the wall)."""
    side, size = order["side"], order["size"]
    base = _book_without(book, side, order["price"], size)
    tick = book.get("tick") or 0.01
    bids, asks = base.get("bids") or [], base.get("asks") or []
    offs = range(min_off, min_off + 6)
    if side == "BUY":
        best = bids[0][0] if bids else None
        near = [round(best - o * tick, 4) for o in offs] if best else []
        cands = [0.01] + [p for p in reversed(near) if p >= 0.01]  # deepest first
        if asks:
            cands = [p for p in cands if p <= round(asks[0][0] - tick, 4)]
    else:
        best = asks[0][0] if asks else None
        near = [round(best + o * tick, 4) for o in offs] if best else []
        cands = [0.99] + [p for p in reversed(near) if p <= 0.99]  # deepest first
        if bids:
            cands = [p for p in cands if p >= round(bids[0][0] + tick, 4)]
    key = "bids" if side == "BUY" else "asks"
    scored: list[tuple[float, float]] = []  # (price, est) — deepest first
    for p in dict.fromkeys(cands):
        levels = dict(base.get(key) or [])
        levels[p] = levels.get(p, 0) + size
        merged = dict(base)
        merged[key] = sorted(levels.items(), key=lambda x: (-x[0] if side == "BUY" else x[0]))
        probe = {"market": order["market"], "side": side, "price": p, "size": float(size)}
        tr._score_order(probe, merged, prog)
        scored.append((p, probe.get("est_day") or 0.0))
    mx = max((e for _, e in scored), default=0.0)
    if mx <= 0:
        if min_off > 0:
            # The touch holds the whole Target Size window — behind it everything
            # scores zero, so joining (queued behind the wall) is the only play.
            return _optimal_price(order, book, prog, 0)
        return (scored[0][0] if scored else None), 0.0
    for p, est in scored:  # deepest price keeping >= EASY_KEEP of the safe max
        if est >= EASY_KEEP * mx:
            return p, est
    return scored[-1]


def _resize_for_risk(side: str, size: float, from_price: float, to_price: float,
                     market: str) -> int:
    """Quantity that keeps the LOCKED capital ~level across a price move —
    a buy walking 10c -> 26c would otherwise lock 2.6x the cash. Covered
    sells lock nothing new, so their size never changes; moves that would
    resize by under 10% aren't worth the churn."""
    size = int(round(size))
    if side == "SELL":
        net = tr._num((MONITOR.positions.get(market) or {}).get("netPosition"))
        if net >= size:
            return size  # covered by inventory — price doesn't change the risk
        lock0, lock1 = 1.0 - from_price, 1.0 - to_price
    else:
        lock0, lock1 = from_price, to_price
    if lock0 <= 0 or lock1 <= 0:
        return size
    q = max(1, min(int(size * lock0 / lock1 + 1e-6), 20000))
    return size if abs(q - size) < 0.10 * max(size, 1) else q


def compute_reprice_plan(min_off: int = 1) -> list[dict]:
    """Orders whose current price leaves meaningful money on the table.
    Price moves carry a matching size move (see _resize_for_risk) so the
    total amount at risk stays where it was."""
    out = []
    progs = tr._PROG_CACHE.get("progs") or {}
    for o in MONITOR.orders:
        if not o.get("id"):
            continue
        cached = tr._BOOK_CACHE.get(o["market"])
        prog = progs.get(o["market"])
        if not cached or not prog or not prog.get("pool"):
            continue
        book = cached[1]
        cur = o.get("est_day") or 0.0
        p, est = _optimal_price(o, book, prog, min_off)
        tick = book.get("tick") or 0.01
        if p is None or abs(p - o["price"]) < tick / 2:
            continue  # already optimal
        to_size = _resize_for_risk(o["side"], o["size"], o["price"], p, o["market"])
        if to_size != int(round(o["size"])):
            # honesty: the advertised gain must reflect the resized order
            base = _book_without(book, o["side"], o["price"], o["size"])
            key = "bids" if o["side"] == "BUY" else "asks"
            levels = dict(base.get(key) or [])
            levels[p] = levels.get(p, 0) + to_size
            merged = dict(base)
            merged[key] = sorted(levels.items(), key=lambda x: (-x[0] if o["side"] == "BUY" else x[0]))
            probe = {"market": o["market"], "side": o["side"], "price": p, "size": float(to_size)}
            tr._score_order(probe, merged, prog)
            est = probe.get("est_day") or 0.0
        # Below target: any $0.05/day gain is worth it. At/above target: move
        # only for meaningfully more (easy-market upside), never for pennies.
        threshold = 0.05 if cur < TARGET_ORDER_EST else max(0.25, cur * 0.25)
        if est - cur < threshold:
            continue
        out.append({"id": o["id"], "market": o["market"], "side": o["side"],
                    "size": o["size"], "to_size": to_size,
                    "from_cents": round(o["price"] * 100, 1),
                    "to_cents": round(p * 100, 1),
                    "est_now": round(cur, 2), "est_after": round(est, 2)})
    out.sort(key=lambda r: -(r["est_after"] - r["est_now"]))
    return out


def run_reprice_batch(specs: list[dict]) -> None:
    done = skipped = failed = 0
    consec_err = 0
    try:
        for spec in specs:
            if PLACER["abort"]:
                PLACER["summary"] = "stopped by user"
                break
            res = {"market": spec["market"], "side": spec["side"],
                   "price_cents": spec["to_cents"], "size": spec.get("size", 0)}
            try:  # fresh-book cross guard: a reprice that crosses fills instantly
                book = tr._fetch_book(spec["market"])
                price = spec["to_cents"] / 100.0
                bids, asks = book.get("bids") or [], book.get("asks") or []
                crosses = ((asks and price >= asks[0][0]) if spec["side"] == "BUY"
                           else (bids and price <= bids[0][0]))
                if crosses:
                    res.update(status="skipped", note="would cross the spread now")
                else:
                    code, payload = do_reprice(spec["id"], spec["to_cents"], verify=False,
                                               quantity=spec.get("to_size"))
                    res.update(status="repriced" if payload.get("ok") else "rejected",
                               note=str(payload.get("detail") or payload.get("error") or "")[:150])
            except Exception as e:  # noqa: BLE001
                res.update(status="error", note=f"{type(e).__name__}: {e}"[:150])
            PLACER["results"].append(res)
            if res["status"] == "repriced":
                done += 1
                consec_err = 0
            elif res["status"] == "skipped":
                skipped += 1
            else:
                failed += 1
                if "429" in (res.get("note") or "") or "rate limited" in (res.get("note") or ""):
                    PLACER["summary"] = "rate limited — stopped; wait a few minutes and retry"
                    break  # hammering a rate limiter keeps the ban alive
                consec_err += 1
                if consec_err >= 3:
                    PLACER["summary"] = "stopped after 3 consecutive failures"
                    break
            time.sleep(BATCH_SPACING_SECONDS)
    finally:
        unverified = 0
        if done:  # verification sweep — patient: replacements need a moment to settle
            try:
                for attempt in range(3):
                    time.sleep(3.0 if attempt == 0 else 5.0)
                    path = "/v1/orders/open"
                    r = requests.get(tr.TRADE_API + path,
                                     headers=tr.auth_headers(KEY_ID, SECRET_KEY, "GET", path),
                                     timeout=30)
                    open_now = [(o.get("marketSlug"),
                                 "BUY" if str(o.get("side", "")).upper().endswith("BUY") else "SELL",
                                 tr._num(o.get("price")))
                                for o in (r.json().get("orders") or [])]
                    unverified = 0
                    for res in PLACER["results"]:
                        if res.get("status") in ("repriced", "unverified"):
                            want = res["price_cents"] / 100.0
                            hit = any(m == res["market"] and s == res["side"]
                                      and p is not None and abs(p - want) < 0.0005
                                      for m, s, p in open_now)
                            res["status"] = "repriced" if hit else "unverified"
                            if not hit:
                                res["note"] = "not seen resting at the new price yet — check the app"
                                unverified += 1
                    if unverified == 0:
                        break
            except Exception:  # noqa: BLE001 — verification is best-effort
                unverified = -1
        PLACER["summary"] = PLACER["summary"] or "done"
        PLACER["running"] = False
        POLL_KICK.set()
        vtxt = ("" if unverified == 0 else
                f", {unverified} UNVERIFIED — check the app!" if unverified > 0 else
                ", verification sweep failed — check the app")
        notify("Batch reprice finished",
               f"{done} repriced, {skipped} skipped, {failed} failed ({PLACER['summary']}){vtxt}",
               "high" if failed or unverified else "default")


def start_reprice_batch(payload: dict) -> tuple[int, dict]:
    if PLACER["running"]:
        return 409, {"ok": False, "error": "a batch is already running"}
    known = {o.get("id"): o for o in MONITOR.orders if o.get("id")}
    try:
        specs = payload.get("orders") or []
        assert 1 <= len(specs) <= 400, "1-400 orders per batch"
        clean = []
        for s in specs:
            oid, tc = str(s.get("id")), float(s.get("to_cents"))
            o = known.get(oid)
            assert o is not None, f"{oid}: not one of your resting orders"
            assert 0.1 <= tc <= 99.9, f"{o['market']}: price out of range"
            ts_ = int(s.get("to_size") or round(o["size"]))
            assert 1 <= ts_ <= 20000, f"{o['market']}: size out of range"
            clean.append({"id": oid, "market": o["market"], "side": o["side"],
                          "size": o["size"], "to_cents": tc, "to_size": ts_})
    except (AssertionError, TypeError, ValueError) as e:
        return 400, {"ok": False, "error": str(e)[:200]}
    PLACER.update(running=True, results=[], total=len(clean), abort=False, summary="")
    threading.Thread(target=run_reprice_batch, args=(clean,), daemon=True).start()
    return 200, {"ok": True, "started": len(clean)}


def do_cancel_all() -> tuple[int, dict]:
    """Emergency stop: cancel every open order on the account."""
    path = "/v1/orders/open/cancel"
    try:
        r = requests.request(
            "POST", tr.TRADE_API + path,
            headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", path),
                     "Content-Type": "application/json"},
            json={}, timeout=30,
        )
        ok = r.status_code < 300
        ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                        "market": "ALL", "side": "CANCEL ALL", "from": "—", "to": "—",
                        "size": "", "status": r.status_code,
                        "response": " ".join(r.text.split())[:150], "verified": ok})
        notify("CANCEL ALL sent", f"HTTP {r.status_code} — all resting orders cancelled",
               "high")
        POLL_KICK.set()
        return (200 if ok else 502), {"ok": ok, "status": r.status_code}
    except Exception as e:  # noqa: BLE001
        return 502, {"ok": False, "error": f"{type(e).__name__}: {e}"[:200]}


def do_reprice(order_id: str, price_cents: float, verify: bool = True,
               quantity: int | None = None) -> tuple[int, dict]:
    """Move one of OUR resting orders to a new price — WITHOUT /modify.

    The exchange's modify endpoint is cancel-and-replace, and since the
    2026-08-11 maintenance it returns 200, cancels the original, and never
    places the replacement. Proven with a controlled test: a non-crossing
    0.99 -> 0.98 modify on a fresh 273-share ask answered 200 {} and the
    order was simply gone. Every modify that day destroyed its order — the
    restore's 89 ask top-ups and each defend nudge alike.

    So the order of operations is inverted and nothing is ever cancelled on
    faith: place the replacement first (post-only), poll until it is VERIFIED
    resting, and only then cancel the original. Any failure before the cancel
    leaves the original untouched; a failure of the cancel itself leaves two
    resting orders, which costs a little doubled size, never a lost rung.
    The `verify` parameter is kept for callers but ignored — verification is
    the mechanism now, not an option.
    """
    known = {o.get("id"): o for o in MONITOR.orders if o.get("id")}
    o = known.get(order_id)
    if o is None:
        return 400, {"ok": False, "error": "unknown order id — wait for the next refresh"}
    if not (0.1 <= price_cents <= 99.9):
        return 400, {"ok": False, "error": "price out of range (0.1–99.9¢)"}
    # Sizes are fractional. int(round(...)) turned a 273.04 order into 273,
    # which then FAILED its own verification — the check demands the
    # replacement match the original's size, and 273 is short of 273.04. Every
    # reprice of a fractional order was unwinnable that way.
    qty = round(float(quantity) if quantity else float(o["size"] or 0), 2)
    if not (0.01 <= qty <= 20000):
        return 400, {"ok": False, "error": "size out of range (0.01–20,000)"}
    # A post-only replacement that would cross the opposite touch can never
    # rest — refuse up front, which is a pure no-op for the resting order.
    ent = tr._BOOK_CACHE.get(o["market"])
    if ent:
        bids, asks = ent[1].get("bids") or [], ent[1].get("asks") or []
        newpx = price_cents / 100.0
        if o["side"] == "SELL" and bids and newpx <= bids[0][0] + 1e-9:
            return 400, {"ok": False,
                         "error": f"refused: {price_cents}¢ would cross the {bids[0][0]*100:g}¢ bid"}
        if o["side"] == "BUY" and asks and newpx >= asks[0][0] - 1e-9:
            return 400, {"ok": False,
                         "error": f"refused: {price_cents}¢ would cross the {asks[0][0]*100:g}¢ ask"}
    value = f"{price_cents / 100:.3f}".rstrip("0").rstrip(".")
    record = {"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
              "market": o["market"], "side": o["side"],
              "from": round(o["price"] * 100, 1), "to": price_cents,
              "size": (qty if abs(qty - float(o["size"] or 0)) < 0.005
                       else f"{float(o['size'] or 0):g}→{qty:g}")}

    def _api(method, path, body=None):
        return requests.request(
            method, tr.TRADE_API + path,
            headers={**tr.auth_headers(KEY_ID, SECRET_KEY, method, path),
                     "Content-Type": "application/json"},
            json=body, timeout=20)

    try:
        # 1) place the replacement
        r = _api("POST", "/v1/orders",
                 {"marketSlug": o["market"],
                  "intent": o.get("intent") or ("ORDER_INTENT_BUY_LONG" if o["side"] == "BUY"
                                                else "ORDER_INTENT_BUY_SHORT"),
                  "type": "ORDER_TYPE_LIMIT",
                  "price": {"value": value, "currency": "USD"},
                  "quantity": qty,
                  "tif": "TIME_IN_FORCE_GOOD_TILL_CANCEL",
                  "participateDontInitiate": True})
        record["status"] = r.status_code
        record["response"] = " ".join(r.text.split())[:300]
        if r.status_code >= 300:
            record["verified"] = False
            record["note"] = "replacement rejected — original untouched"
            return 502, {"ok": False, "status": r.status_code,
                         "detail": record["response"][:250]}
        # the id the exchange just handed back, so verification cannot be
        # satisfied by the original order still resting at this same price
        new_id = None
        try:
            j = r.json()
            new_id = ((j.get("order") or {}).get("id") if isinstance(j.get("order"), dict)
                      else None) or j.get("id") or j.get("orderId")
        except Exception:  # noqa: BLE001 — no id is survivable, it just weakens the check
            pass
        # 2) confirm it is genuinely resting before touching the original.
        #    An increase must actually achieve the old size before the old
        #    order is retired; the exchange caps placements, and cancelling on
        #    a short fill would leave less size than we started with.
        old_qty = float(o["size"] or 0)
        need = old_qty if qty >= old_qty else None
        verified, note, rested = _verify_resting(o["market"], o["side"], value,
                                                 want_id=str(new_id) if new_id else None,
                                                 min_qty=need)
        if not verified:
            record["verified"] = False
            keep_both = rested > 0
            # The replacement was accepted. If it is resting and we simply
            # could not confirm it, retiring it is the honest thing to do:
            # leaving it creates a duplicate rung nobody is tracking, and a
            # day of failed verifications is how the book quietly grew by
            # hundreds of orphan orders. The ORIGINAL is never touched here.
            orphan = ""
            if new_id and not keep_both:
                try:
                    rc = _api("POST", f"/v1/order/{new_id}/cancel",
                              {"marketSlug": o["market"]})
                    orphan = (" replacement withdrawn"
                              if rc.status_code < 300 else
                              f" replacement left (cancel HTTP {rc.status_code})")
                except Exception:  # noqa: BLE001
                    orphan = " replacement left (cancel failed)"
            record["note"] = (f"replacement {note} — original left in place"
                              if keep_both else
                              f"replacement did not rest ({note}) — original untouched;"
                              + (orphan or " no id to withdraw"))
            notify("Reprice replacement did not rest",
                   f"{o['market']} → {price_cents}¢: {note}", "high")
            return 502, {"ok": False, "status": r.status_code,
                         "detail": (record["note"] if keep_both else note)[:250]}
        # 3) only now retire the original
        rc = _api("POST", f"/v1/order/{order_id}/cancel", {"marketSlug": o["market"]})
        if rc.status_code >= 300:
            time.sleep(1.0)
            rc = _api("POST", f"/v1/order/{order_id}/cancel", {"marketSlug": o["market"]})
        record["verified"] = True
        record["note"] = note + (
            "" if rc.status_code < 300 else
            f" (old order cancel HTTP {rc.status_code} — both resting, harmless)")
        POLL_KICK.set()
        return 200, {"ok": True, "status": r.status_code, "detail": record["note"][:250]}
    except Exception as e:  # noqa: BLE001
        record["status"] = "error"
        record["response"] = f"{type(e).__name__}: {e}"[:300]
        record["verified"] = False
        return 502, {"ok": False, "error": record["response"][:200]}
    finally:
        ACTIONS.append(record)
        del ACTIONS[:-20]

# ---- Live book stream: the exchange's markets WebSocket ---------------------
# One authenticated connection replaces minutes-stale polled books with
# push updates for every market we quote. Strictly additive: the stream only
# writes fresher entries into the shared book cache; if it drops, cache ages
# grow past the REST rotation's 15s threshold and polling resumes untouched.
WS_URL = "wss://api.polymarket.us/v1/ws/markets"
WS_PATH = "/v1/ws/markets"
WS_STATUS: dict = {"state": "off", "markets": 0, "last_msg": 0.0, "err": ""}


def _ws_apply(text: str) -> str | None:
    """Apply one stream message to the shared book cache; returns the slug."""
    try:
        md = (json.loads(text) or {}).get("marketData") or {}
        slug = md.get("marketSlug")
        if not slug:
            return None
        bids = [(tr._num((l.get("px") or {}).get("value")), tr._num(l.get("qty")))
                for l in md.get("bids") or []]
        asks = [(tr._num((l.get("px") or {}).get("value")), tr._num(l.get("qty")))
                for l in md.get("offers") or md.get("asks") or []]
        tr._BOOK_CACHE[slug] = (time.time(), tr._normalize_book(bids, asks))
        WS_STATUS["last_msg"] = time.time()
        return slug
    except Exception:  # noqa: BLE001 — one bad frame never kills the stream
        return None


def _ws_slugs() -> set[str]:
    return ({o.get("market") for o in MONITOR.orders if o.get("market")}
            | set(MONITOR.state.get("defend") or {}))


def ws_stream_loop(key_id: str, secret_key: str) -> None:
    try:
        import asyncio
        import websockets
    except Exception as e:  # noqa: BLE001 — no lib: polling carries on alone
        WS_STATUS.update(state="unavailable", err=str(e)[:80])
        return

    async def run() -> None:
        while True:
            slugs = sorted(_ws_slugs())
            if not slugs:
                await asyncio.sleep(30)
                continue
            try:
                headers = tr.auth_headers(key_id, secret_key, "GET", WS_PATH)
                kw = {"open_timeout": 15, "close_timeout": 3, "ping_interval": 20}
                # websockets renamed extra_headers -> additional_headers in v14
                try:
                    major = int(websockets.__version__.split(".")[0])
                except Exception:  # noqa: BLE001
                    major = 14
                kw["additional_headers" if major >= 14 else "extra_headers"] = headers
                async with websockets.connect(WS_URL, **kw) as ws:
                    await ws.send(json.dumps({"subscribe": {
                        "requestId": "books",
                        "subscriptionType": "SUBSCRIPTION_TYPE_MARKET_DATA",
                        "marketSlugs": slugs[:200]}}))
                    WS_STATUS.update(state="live", markets=len(slugs), err="")
                    sub_set, last_check = set(slugs), time.time()
                    while True:
                        try:
                            _ws_apply(await asyncio.wait_for(ws.recv(), timeout=60))
                        except asyncio.TimeoutError:
                            pass  # quiet books — pings keep the socket alive
                        if time.time() - last_check > 60:
                            last_check = time.time()
                            if _ws_slugs() - sub_set:
                                break  # new markets: reconnect to resubscribe
            except Exception as e:  # noqa: BLE001 — reconnect with backoff
                WS_STATUS.update(state="reconnecting",
                                 err=f"{type(e).__name__}: {e}"[:100])
                await asyncio.sleep(15)

    try:
        asyncio.run(run())
    except Exception as e:  # noqa: BLE001
        WS_STATUS.update(state="dead", err=str(e)[:100])


# ---- Auto-defend: keep price-setting orders at the front of thin books -----
# The whole reward edge in a df-0.2 book is being the SOLE best price: everyone
# a tick behind scores at 20%. Defend watches a defended market's book and
# moves our best order one tick forward whenever our share of that side's
# rewards falls under DEFEND_SHARE_FLOOR — because someone outbid us, matched
# us with real size, or parked a massive order right behind us. Sharing the
# front with a reasonably sized order (share still healthy) is left alone.
# Hard rails: the user's cap, a 2-tick gap to the opposite touch, a cooldown,
# fresh books only, reprice-only (never places orders or adds size), and
# floor/ceiling qualifier blocks are never touched.
DEFEND_SHARE_FLOOR = 0.25        # act only under 25% of the side's rewards
# A market may ask for more than the default via its defend config
# ({"SELL": {"cap": 25.0, "share": 0.33}}). The 2028 presidential slate runs at
# 0.33: those are longshots, so an ask well above fair value is worth holding,
# and a third of the side's score is the stake we want in each.
DEFEND_COOLDOWN_SECONDS = 90.0   # per market+side between improvements
DEFEND_MAX_PER_POLL = 10         # request-budget bound on a busy poll
# Where the last pass stopped. The budget above is spent in dict order, and
# the pass RETURNS once it is used up — so with 175 armed markets the ones
# near the front consumed every move and the 2028 slate, armed last, was
# never reached at all. Resuming from where the previous pass left off gives
# every armed market its turn.
DEFEND_CURSOR = 0
DEFEND_DEEP_BUY = 0.011          # floor-bid qualifiers: never repriced
DEFEND_DEEP_SELL = 0.989         # ceiling-ask qualifiers: never repriced
DEFEND_MOVED: dict[str, float] = {}


def _defend_share_at(side: str, levels: list, best_mine: dict, price: float,
                     df: float, target: float, tick: float) -> float:
    """Our share of this side's score if our best order sat at `price`.

    Rebuilds the level map with that one order moved, then applies the
    official rule — walk out from the best price until Target Size has
    accumulated, score each level as size x df^ticks — so the answer matches
    what the exchange will actually pay rather than an approximation.
    """
    lv: dict[float, float] = {}
    for px, q in levels or []:
        lv[round(float(px), 4)] = lv.get(round(float(px), 4), 0.0) + float(q)
    old = round(float(best_mine["price"]), 4)
    sz = float(best_mine.get("size") or 0)
    if sz <= 0:
        return 0.0
    lv[old] = lv.get(old, 0.0) - sz
    if lv[old] <= 0.5:
        lv.pop(old, None)
    new = round(float(price), 4)
    lv[new] = lv.get(new, 0.0) + sz
    ordered = sorted(lv.items(), key=(lambda kv: -kv[0]) if side == "BUY" else (lambda kv: kv[0]))
    if not ordered:
        return 0.0
    best = ordered[0][0]
    win, cum = [], 0.0
    for px, q in ordered:
        win.append((px, q)); cum += q
        if target and cum >= target:
            break
    den = sum(q * df ** round(abs(best - px) / tick) for px, q in win)
    if den <= 0:
        return 0.0
    mine = sz * df ** round(abs(best - new) / tick) if any(abs(px - new) < 1e-9 for px, _ in win) else 0.0
    return mine / den


def _others_best(levels: list, mine_sz: dict) -> float | None:
    """Best price on a book side that isn't just our own resting size."""
    for lvl in levels or []:
        p, q = float(lvl[0]), float(lvl[1])
        if q - mine_sz.get(round(p, 4), 0.0) > 0.5:
            return p
    return None


# ---- Hot-reload the defend seed straight from GitHub ----------------------
# The app redeploys on every push to main, and the hourly tracker pushes data
# dozens of times a day, so a config-only change can sit behind a long queue of
# unrelated deploys. Pulling the seed over the API instead means arming a market
# takes effect on the next poll — no rebuild, no restart.
SEED_POLL_SECONDS = 60.0
SEED_FETCH = {"ts": 0.0, "err": ""}


def refresh_defend_seed() -> None:
    if not GITHUB_TOKEN:
        return
    now = time.time()
    if now - SEED_FETCH["ts"] < SEED_POLL_SECONDS:
        return
    SEED_FETCH["ts"] = now
    try:
        r = requests.get(
            f"{GH_API}/repos/{GITHUB_REPO}/contents/live/defend_seed.json",
            params={"ref": "main"},
            headers={"Authorization": f"Bearer {GITHUB_TOKEN}",
                     "Accept": "application/vnd.github.raw+json"},
            timeout=15,
        )
        if r.status_code != 200:
            SEED_FETCH["err"] = f"HTTP {r.status_code}"
            return
        seed = json.loads(r.text)
    except Exception as e:  # noqa: BLE001 — never let this break the poll
        SEED_FETCH["err"] = f"{type(e).__name__}: {e}"[:120]
        return
    SEED_FETCH["err"] = ""
    if int(seed.get("version") or 0) <= int(MONITOR.state.get("defend_seed_v") or 0):
        return
    with MONITOR.lock:
        MONITOR._apply_defend_seed(seed)
        tr.PRIORITY_SLUGS = set(MONITOR.state["defend"])


# ---- Watch for reward pools arriving on markets that had none -------------
# A market can be listed days before its incentive program is attached: the
# governor slate listed 2026-08-10 had live books and no pool. Entering one of
# those early earns nothing, but the moment a pool appears the front of a thin
# book is worth having, so this notices the transition and pushes a phone alert.
PROGRAM_WATCH_BATCH = 25         # symbols per /v1/incentives call
PROGRAM_WATCH_MAX = 300          # slugs examined per pass, keeps the poll cheap


def watch_program_arrivals(pol_slugs: list[str]) -> None:
    """Alert once when a US-politics market gains a reward pool it lacked.

    The first pass over a market only records its state, so a fresh deploy does
    not announce hundreds of pre-existing programs as if they were new.
    """
    if not pol_slugs:
        return
    cands = [s for s in pol_slugs
             if tr._is_us_politics(s) and not tr._is_econ(s)][:PROGRAM_WATCH_MAX]
    if not cands:
        return
    with MONITOR.lock:
        known = dict(MONITOR.state.get("prog_seen") or {})
    seeded = bool(known)
    live: dict[str, dict] = {}
    for i in range(0, len(cands), PROGRAM_WATCH_BATCH):
        batch = cands[i:i + PROGRAM_WATCH_BATCH]
        try:
            r = requests.get(tr.HOSTS[0] + "/v1/incentives",
                             params={"symbols": batch, "pageSize": 100}, timeout=20)
            if r.status_code >= 400:
                continue
            for p in r.json().get("programs") or []:
                slug = p.get("marketSlug", "")
                tp = tr._pick_period(p.get("timePeriods") or [], slug)
                if slug and tp is not None:
                    live[slug] = tr._prog_of(tp)
        except Exception:  # noqa: BLE001 — best-effort, never break the poll
            continue
        time.sleep(0.05)

    arrived = []
    for slug in cands:
        had = bool(known.get(slug))
        has = slug in live
        if has and not had and seeded:
            arrived.append(slug)
        known[slug] = bool(has)

    with MONITOR.lock:
        MONITOR.state["prog_seen"] = known
    if not arrived:
        return
    arrived.sort()
    for slug in arrived[:6]:
        pr = live.get(slug) or {}
        MONITOR.pending_alerts.append((
            "Reward pool attached",
            f"{slug} — ${pr.get('pool', 0):,.0f}/day pool, target "
            f"{pr.get('target', 0):,.0f}, df {pr.get('df')}",
            "high"))
    if len(arrived) > 6:
        MONITOR.pending_alerts.append((
            "Reward pools attached",
            f"…and {len(arrived) - 6} more markets gained a pool", "high"))
    print(f"[prog-watch] {len(arrived)} market(s) gained a pool: "
          f"{', '.join(arrived[:8])}", flush=True)


# ---- Qualification keeper --------------------------------------------------
# The owner's priority order, stated 2026-08-11: where a side already holds
# Target Size (from anyone's orders), what matters is having a SCORING order
# near the touch — that is what earns. Deep 1c/99c size matters only where the
# book would otherwise fall below target and the side would pay nobody.
# So each poll, per funded side: (1) if the side qualifies but none of our
# orders score, place one small order a tick inside the field, bounded by the
# defend cap; (2) if the side's TOTAL resting size (every participant, from
# the live book) is short of target, stack a deep qualifier chunk.
# Placements only — post-only — never modify; defend handles repricing.
KEEP_MAX_PER_POLL = int(os.environ.get("KEEP_MAX_PER_POLL", "4"))
KEEP_SCORE_SIZE = int(os.environ.get("KEEP_SCORE_SIZE", "40"))
KEEP_COOLDOWN = float(os.environ.get("KEEP_COOLDOWN", "600"))
_KEEP_LAST: dict = {}


def _keep_place(m: str, side: str, px: float, qty: int) -> bool:
    body = {"marketSlug": m,
            "intent": "ORDER_INTENT_BUY_LONG" if side == "BUY" else "ORDER_INTENT_BUY_SHORT",
            "type": "ORDER_TYPE_LIMIT",
            "price": {"value": f"{px:.2f}", "currency": "USD"},
            "quantity": int(qty),
            "tif": "TIME_IN_FORCE_GOOD_TILL_CANCEL",
            "participateDontInitiate": True}
    try:
        r = requests.request(
            "POST", tr.TRADE_API + "/v1/orders",
            headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", "/v1/orders"),
                     "Content-Type": "application/json"},
            json=body, timeout=20)
        ok = r.status_code < 300
        ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                        "market": m, "side": f"KEEP {side}", "from": "—",
                        "to": round(px * 100, 1), "size": qty,
                        "status": r.status_code,
                        "response": " ".join(r.text.split())[:120], "verified": ok})
        del ACTIONS[:-20]
        return ok
    except Exception:  # noqa: BLE001 — keeper must never kill the poll
        return False


# The two loops that place orders on their own each poll -- the defender and
# the qualification keeper -- are now separate, owner-controlled switches.
#
# Each is OFF unless the owner turned it on from the dashboard button. The
# setting lives in persisted state, so a restart keeps the owner's choice
# instead of silently resetting it, and a fresh deploy defaults to off. The
# env pauses (DEFEND_PAUSE / KEEP_PAUSE) remain a host-side veto on top.
#
# History that motivated this: the two loops shared one switch, so turning
# defend on for the night also turned on the keeper, which placed orders the
# owner never chose. Never again -- one switch per loop, owner's button only.
def _auto_on(which: str) -> bool:
    """Is this placement loop enabled? `which` is 'defend' or 'keeper'."""
    auto = MONITOR.state.get("auto") or {}
    return bool(auto.get(which) is True)


def keep_qualified() -> None:
    if not _auto_on("keeper"):
        return
    if os.environ.get("KEEP_PAUSE", "") == "1":
        return
    progs = tr._PROG_CACHE.get("progs") or {}
    cfg = dict(MONITOR.state.get("defend") or {})
    now = time.time()
    placed = 0
    by_mkt: dict = {}
    for o in MONITOR.orders:
        if o.get("market"):
            by_mkt.setdefault(o["market"], []).append(o)
    for m, orders in by_mkt.items():
        if placed >= KEEP_MAX_PER_POLL:
            return
        # Only markets that are actually armed to defend.
        #
        # The scoring branch below already required a sanctioned cap, so it
        # never acted outside this list. The deep-qualifier branch did not:
        # it ran on every market we hold orders in that has a pool, so the
        # keeper was stacking 1c and 99c size into books the owner had never
        # armed -- pandc-anydis and enwc-usgubp-wi among them on 2026-08-12.
        # That is activity nobody asked for, in markets nobody chose.
        if m not in cfg:
            continue
        pr = progs.get(m)
        if not pr or not pr.get("pool") or not pr.get("target"):
            continue
        ent = tr._BOOK_CACHE.get(m)
        if not ent or now - ent[0] > 300:
            continue
        book = ent[1]
        tick = book.get("tick") or 0.01
        target = float(pr["target"])
        for side, levels, opp in (("BUY", book.get("bids") or [], book.get("asks") or []),
                                  ("SELL", book.get("asks") or [], book.get("bids") or [])):
            if placed >= KEEP_MAX_PER_POLL:
                return
            key = (m, side)
            if now - _KEEP_LAST.get(key, 0.0) < KEEP_COOLDOWN:
                continue
            total = sum(q for _, q in levels)
            mine = [o for o in orders if o.get("side") == side]
            deep_px = 0.01 if side == "BUY" else 0.99
            if total < target - 1:
                # (2) the side does not qualify — stack deep size; each
                # placement lands ~273 for shorts, so the shortfall closes
                # over successive polls without any modify.
                qty = int(min(target - total, 2000))
                if qty >= 1 and _keep_place(m, side, deep_px, qty):
                    placed += 1
                    _KEEP_LAST[key] = now
                continue
            # (1) the side qualifies — make sure something of OURS scores.
            if any((o.get("est_day") or 0) > 0.001 for o in mine):
                continue
            scfg = (cfg.get(m) or {}).get(side) or {}
            try:
                cap = float(scfg.get("cap")) / 100.0
            except (TypeError, ValueError):
                continue  # no sanctioned price bound — never invent one
            if not levels:
                continue
            best = float(levels[0][0])
            px = min(best + tick, cap) if side == "BUY" else max(best - tick, cap)
            # never cross the opposite touch — post-only could not rest there
            if opp:
                ob = float(opp[0][0])
                if side == "BUY" and px >= ob - 1e-9:
                    px = ob - tick
                if side == "SELL" and px <= ob + 1e-9:
                    px = ob + tick
            if not (0.005 <= px <= 0.995):
                continue
            # The order must actually be able to SCORE, or this loop places a
            # fresh one every cooldown forever — the "does anything of ours
            # score?" test keeps failing, so it never stops. That is exactly
            # what happened on 2026-08-12: caps below the market's touch
            # produced 188 stacked 40-share orders, $1,815 of capital, all at
            # 0.00% share. Two conditions, both required:
            #   * the sanctioned price must reach the touch — a cap behind the
            #     best price cannot compete, and raising it is the owner's call
            #   * we must not already hold an order at that price
            if abs(px - deep_px) < 1e-9:
                continue
            if side == "BUY" and px < best - 1e-9:
                continue
            if side == "SELL" and px > best + 1e-9:
                continue
            if any(abs(float(o.get("price") or 0) - px) < 1e-9 for o in mine):
                continue
            if side == "BUY" and px > cap + 1e-9:
                continue
            if side == "SELL" and px < cap - 1e-9:
                continue
            if _keep_place(m, side, round(px, 2), KEEP_SCORE_SIZE):
                placed += 1
                _KEEP_LAST[key] = now


def auto_defend() -> None:
    """One pass over the defended markets after each poll."""
    # Resumed 2026-08-11 after the /modify incident. The exchange's modify
    # endpoint has returned 200 while cancelling the original and never
    # placing the replacement since the morning maintenance (proven with a
    # controlled non-crossing test: 0.99 -> 0.98 on a fresh 273-share ask,
    # answer 200 {}, order gone), which let the old defend shred 100+ orders.
    # do_reprice no longer touches modify: it places the replacement, VERIFIES
    # it rests, and only then cancels the original — the worst remaining
    # failure is a briefly doubled rung, never a lost one.
    if not _auto_on("defend"):
        return
    if os.environ.get("DEFEND_PAUSE", "") == "1":
        return
    global DEFEND_CURSOR
    cfg = dict(MONITOR.state.get("defend") or {})
    if not cfg or not KEY_ID:
        return
    now = time.time()
    moves = 0
    # start where the last pass stopped and wrap, so the move budget rotates
    # across every armed market instead of always landing on the same few
    order = list(cfg.items())
    # named rot_start, not start: the move logic below uses `start` for a
    # starting PRICE, and letting that float overwrite this index killed the
    # whole pass on the next poll with "slice indices must be integers"
    rot_start = int(DEFEND_CURSOR) % len(order)
    order = order[rot_start:] + order[:rot_start]
    scanned = 0
    for m, sides in order:
        scanned += 1
        DEFEND_CURSOR = (rot_start + scanned) % len(cfg)
        ent = tr._BOOK_CACHE.get(m)
        if not ent or now - ent[0] > 300:
            continue  # stale book — never act on old prices
        book = ent[1]
        tick = book.get("tick") or 0.01
        bids = book.get("bids") or []
        asks = book.get("asks") or []
        bb = float(bids[0][0]) if bids else None
        ba = float(asks[0][0]) if asks else None
        mine_all = [o for o in MONITOR.orders if o.get("market") == m]
        for side, scfg in (sides or {}).items():
            if moves >= DEFEND_MAX_PER_POLL:
                return
            try:
                cap = float(scfg.get("cap")) / 100.0
            except (TypeError, ValueError):
                continue
            all_side = [o for o in mine_all if o.get("side") == side]
            # Floor/ceiling qualifier blocks hold the side's Target Size —
            # Defend must never move them, up or down.
            side_orders = [o for o in all_side if o.get("id")
                           and not (o["price"] <= DEFEND_DEEP_BUY if side == "BUY"
                                    else o["price"] >= DEFEND_DEEP_SELL)]
            if not side_orders:
                continue
            best_mine = (max if side == "BUY" else min)(side_orders,
                                                        key=lambda o: o["price"])
            mine_sz: dict[float, float] = {}
            for o in all_side:
                k = round(float(o["price"]), 4)
                mine_sz[k] = mine_sz.get(k, 0.0) + float(o.get("size") or 0)
            others = _others_best(bids if side == "BUY" else asks, mine_sz)
            if others is None:
                continue  # alone on this side — nothing to defend against
            # Our scored share of this side (computed by the last poll's
            # scoring pass against the same fresh book).
            shares = [o.get("share") for o in all_side]
            share_known = any(s is not None for s in shares)
            my_share = sum(s or 0.0 for s in shares)
            want = DEFEND_SHARE_FLOOR
            try:
                if scfg.get("share") is not None:
                    want = float(scfg["share"])
            except (TypeError, ValueError):
                pass
            in_front = (best_mine["price"] > others + 1e-9 if side == "BUY"
                        else best_mine["price"] < others - 1e-9)
            if share_known:
                if my_share >= want:
                    continue
            elif in_front:
                continue  # share unknown: only retake when matched/beaten
            # Where to move to. The old rule always stepped one tick past the
            # best other order, which can give away far more than the job
            # needs. Instead, walk out from where we are and stop at the FIRST
            # price that reaches the wanted share — for an ask that is the
            # highest such price, so we never cut the offer further than it
            # takes. Falls back to the one-tick step if the book has no
            # program to score against.
            pr = (tr._PROG_CACHE.get("progs") or {}).get(m) or {}
            df = float(pr.get("df") or 0)
            tgt_size = float(pr.get("target") or 0)
            levels = bids if side == "BUY" else asks
            step = tick if side == "BUY" else -tick
            target = None
            if df and tgt_size:
                start = best_mine["price"] if not in_front else others
                for k in range(1, int(abs(start - cap) / tick) + 2):
                    cand = round(start + step * k, 4)
                    if side == "BUY" and cand > cap + 1e-9:
                        break
                    if side == "SELL" and cand < cap - 1e-9:
                        break
                    if not 0.001 <= cand <= 0.999:
                        break
                    if _defend_share_at(side, levels, best_mine, cand,
                                        df, tgt_size, tick) >= want:
                        target = cand
                        break
            if target is None:
                base = ((max if side == "BUY" else min)(best_mine["price"], others)
                        if share_known else others)
                target = round(base + step, 4)
            blocked = (target > cap + 1e-9) if side == "BUY" else (target < cap - 1e-9)
            squeezed = (ba is not None and target > ba - 2 * tick + 1e-9) if side == "BUY" \
                else (bb is not None and target < bb + 2 * tick - 1e-9)
            if not 0.001 <= target <= 0.999:
                continue
            if blocked:
                continue  # price ran past the user's limit — never chase it
            if squeezed:
                continue  # spread too tight to step in front — wait it out
            key = f"{m}|{side}"
            if now - DEFEND_MOVED.get(key, 0.0) < DEFEND_COOLDOWN_SECONDS:
                continue
            DEFEND_MOVED[key] = now
            do_reprice(best_mine["id"], round(target * 100, 2), verify=False)
            moves += 1


# ---------------------------------------------------------------------------
# The bid sniper. Somebody keeps parking one- and two-contract bids well above
# fair value on the 2028 longshots — 15c and up on candidates the market
# otherwise prices near a cent. Two reasons to take them:
#
#   1. it is money. A contract sold at 20c on a name worth 1c is 19c.
#   2. it unblocks our own scoring. That tiny bid SETS THE TOUCH, and our
#      10,000-share block at 1c is then twenty-odd ticks behind it, scoring
#      nothing on a side worth $5-10 a day. Clearing a 1-contract order at
#      20c can switch a whole bid side back on.
#
# This is the one loop here that CROSSES the spread — it is a taker, not a
# rester, and it pays the taker fee. It is deliberately narrow: only the 2028
# slate, only touch levels under SNIPE_MAX_LEVEL contracts, only at or above
# SNIPE_MIN_PRICE, never the three candidates the owner named as real
# contenders, and bounded per cycle in both count and dollars.
#
# Like every other loop that places orders, it does nothing at all until the
# owner turns its switch on from /map. Off by default, persisted, audit-logged.
# A touch level strictly under this many contracts is fair game, and the
# WHOLE level is taken — 4.9 contracts is under five just as much as 1 is,
# and leaving 0.9 behind would leave the touch exactly where it was.
SNIPE_MAX_LEVEL = float(os.environ.get("SNIPE_MAX_LEVEL", "5"))
SNIPE_MIN_PRICE = float(os.environ.get("SNIPE_MIN_PRICE", "0.15"))
SNIPE_MAX_PER_CYCLE = int(os.environ.get("SNIPE_MAX_PER_CYCLE", "6"))
SNIPE_MAX_SPEND = float(os.environ.get("SNIPE_MAX_SPEND", "25"))
SNIPE_COOLDOWN = float(os.environ.get("SNIPE_COOLDOWN", "300"))
SNIPE_PREFIXES = ("enwc-uspres-nom-rep-2028-", "enwc-uspres-nom-dem-2028-",
                  "ewc-usp-2028-11-07-")
# The owner's own read on who is a real contender. Selling a longshot at 15c+
# is selling well above fair; selling one of these is not, so the sniper never
# touches them. Vance, Rubio and Harris were the original three; Ossoff and
# Buttigieg added 2026-08-14.
SNIPE_EXCLUDE = {"jdvan", "marrub", "kamhar", "jonoss", "petbut"}
_SNIPE_LAST: dict = {}


def auto_snipe() -> None:
    """Take the tiny over-priced bids sitting on the 2028 longshots."""
    if not _auto_on("snipe"):
        return
    if os.environ.get("SNIPE_PAUSE", "") == "1":
        return
    now = time.time()
    took = 0
    spent = 0.0
    for m, ent in list(tr._BOOK_CACHE.items()):
        if took >= SNIPE_MAX_PER_CYCLE or spent >= SNIPE_MAX_SPEND:
            return
        if not m.startswith(SNIPE_PREFIXES):
            continue
        if m.rsplit("-", 1)[-1] in SNIPE_EXCLUDE:
            continue
        if now - _SNIPE_LAST.get(m, 0.0) < SNIPE_COOLDOWN:
            continue
        if not ent or now - ent[0] > 120:
            continue          # only ever act on a fresh book
        bids = (ent[1] or {}).get("bids") or []
        if not bids:
            continue
        px, q = float(bids[0][0]), float(bids[0][1])
        # only the TOUCH level, and only if it is both small and rich. A big
        # bid at 20c is somebody's real opinion; a handful of contracts is not.
        # Sizes here are FRACTIONAL — books carry levels like 0.06 and 273.04.
        # Rounding them away broke this twice over: a 0.4-contract bid was
        # skipped entirely as "under one", and a 1.5-contract level was taken
        # as 1, leaving 0.5 resting and the touch exactly where it was. The
        # whole point is to CLEAR the level, so work in fractions throughout.
        if q >= SNIPE_MAX_LEVEL or q <= 0:
            continue
        # Overpriced by whose measure? When the Bayesian band is usable
        # (any real trade, reasonably tight), the bid must clear the band's
        # TOP plus a margin — which both unlocks snipes below the static
        # 15c line (a 9c bait bid on a 3c-fair longshot is profit) and
        # blocks unprofitable ones the static rule would have taken (a 16c
        # bid when fair is modeled at 15c is no edge). With no usable band
        # the static floor stands.
        b = _bayes_fair(m)
        if b and b.get("med") and b.get("fills", 0) >= 1 and (b["hi"] - b["lo"]) <= 6:
            if px * 100 < b["hi"] + 2:
                continue
        elif px < SNIPE_MIN_PRICE:
            continue
        # never trade with ourselves
        ours = sum(o.get("size") or 0 for o in MONITOR.orders
                   if o.get("market") == m and o.get("side") == "BUY"
                   and abs(float(o.get("price") or 0) - px) < 1e-9)
        qty = round(q - ours, 2)      # the whole level, fractions included
        if qty <= 0 or spent + px * qty > SNIPE_MAX_SPEND:
            continue
        _SNIPE_LAST[m] = now
        try:
            r = requests.request(
                "POST", tr.TRADE_API + "/v1/orders",
                headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", "/v1/orders"),
                         "Content-Type": "application/json"},
                json={"marketSlug": m, "intent": "ORDER_INTENT_BUY_SHORT",
                      "type": "ORDER_TYPE_LIMIT",
                      "price": {"value": f"{px:.2f}", "currency": "USD"},
                      "quantity": qty,                     # may be fractional
                      "tif": "TIME_IN_FORCE_GOOD_TILL_CANCEL",
                      "participateDontInitiate": False},   # crosses on purpose
                timeout=20)
            ok = r.status_code < 300
            ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                            "market": m, "side": "SNIPE sell", "from": "—",
                            "to": round(px * 100, 1), "size": qty,
                            "status": r.status_code,
                            "response": " ".join(r.text.split())[:120],
                            "verified": ok})
            del ACTIONS[:-20]
            if ok:
                took += 1
                spent += px * qty
        except Exception:  # noqa: BLE001 — a sniper must never kill the poll
            continue


# --- price prober (owner, 2026-08-15; reworked same day) --------------------
# Fair-price discovery by tiny probes, run as a CLOSED LOOP over the owner's
# existing inventory and its own info fund (state["probe_budget"]):
#
#   * SELL scouts are SELL_LONG of shares we ALREADY HOLD (never shorts, no
#     collateral) — markets with a net long position of at least 2 are the
#     ammo. A sell that fills credits its proceeds to the fund AND is
#     information: a real buyer at that price.
#   * BUY scouts (and flip buy-backs) spend ONLY the fund — no fund, no
#     bids. A buy that fills debits the fund; its flip sale credits it
#     back plus the gap. Nothing else in the account touches the fund, in
#     either direction. When it runs dry, only sell scouts continue (they
#     refill it); when inventory runs out too, the prober waits.
#
# Placement is unchanged: one-share post-only orders at random ticks inside
# the de-baited spread (levels under 5 shares ignored). Every event lands in
# the journal and the Bayesian bands. Owner switch: auto["probe"], off by
# default.
# Owner, 2026-08-16: extended beyond the 2028 slate to the race families —
# governor, senate, the ewc singles, seat-count ladders, house — where the
# tier pools have reconciled ~100% all week, so the earner's deal test runs
# on validated (small, honest) numbers. Scouts only ever appear in markets
# the book cache holds, i.e. where we already trade.
# Every US politics family the owner trades: the 2028 presidential slate
# (nominations, the winner market AND the party market, which was missing and
# is as much a 2028 market as the rest), the governor and senate races and
# their primaries, and the house/senate seat-count ladders. Audited against
# the live program list: this covers 176 of the 181 markets carrying a reward
# program. The five left out are deliberate — college basketball, a measles
# market, a pandemic market, and the Powell/Fed governor market, which is an
# econ market and off limits.
PROBE_PREFIXES = ("enwc-uspres-nom-rep-2028-", "enwc-uspres-nom-dem-2028-",
                  "ewc-usp-2028-11-07-", "ewc-usp-party-2028-11-07-",
                  "ussewc-", "usgubewc-", "ewc-usse-", "ewc-usgub-",
                  "scc-", "ushrewc-", "enwc-usgubp-", "enwc-ushrp-",
                  "enwc-ussep-", "vsc-usgubp-")
PROBE_SIZE = 1
PROBE_REAL_MIN = 5.0          # book levels smaller than this are bait — ignore
PROBE_MIN_GAP = 3             # need at least this many interior ticks to learn
PROBE_MAX_PX = 0.60           # never probe-bid above this
PROBE_FLIP_TICKS = 2
# PACE. The binding limit was never the placement rate — it was turnover.
# 60 scouts each sitting for 45 minutes retire at 80/hour however often the
# poll runs, and 176 markets at 3 scouts each is 528 slots, so a full sweep
# took 6.6 hours. More scouts alive at once, retiring sooner, cuts that to
# under two hours.
#
# The cost of a shorter TTL is evidence quality: "held 30 minutes with no
# taker" says less than "held 45". It is still the same KIND of evidence and
# the model already weights a resting scout by how long it has sat, so a
# shorter sit simply counts for less rather than counting wrongly.
PROBE_TTL = float(os.environ.get("PROBE_TTL", "1800"))     # rotate after 30 min
PROBE_ACTIVE_MAX = int(os.environ.get("PROBE_ACTIVE_MAX", "140"))
PROBE_MAX_PER_POLL = 5
# Several scouts may sit in one market at DIFFERENT prices (owner, 2026-08-16:
# "it can stack the single orders so that it can increase its confidence in the
# info it is getting"). One scout per market gives one observation per 45-minute
# TTL; three at different ticks bracket the fair price in the same wait. Same
# price twice would teach nothing, so distinct ticks are enforced.
PROBE_PER_MARKET = int(os.environ.get("PROBE_PER_MARKET", "3"))
# A FILL IS A LOSS, not a success (owner, 2026-08-16: "fills should be seen as
# bad, high stable earnings are good"). The scout still learns from being taken
# — that is real evidence about fair value — but the market goes quiet for a
# while afterwards instead of being probed straight back into the same taker.
PROBE_FILL_COOLDOWN = float(os.environ.get("PROBE_FILL_COOLDOWN", "5400"))
# Where in the gap a scout rests. A bid nearer the ask fills sooner; a bid
# nearer the bid touch rests and earns. Weighting the draw toward the safe half
# buys information more slowly and much more cheaply than a uniform draw.
PROBE_SAFE_BIAS = float(os.environ.get("PROBE_SAFE_BIAS", "0.7"))
# How far a candidate price must sit from the Silver forecast before the model
# decides which side we take rather than the coin.
PROBE_SILVER_EDGE = float(os.environ.get("PROBE_SILVER_EDGE", "2"))
# HARD CEILING ON ANY BID, INDEPENDENT OF EVERY MODEL AND LOOKUP.
#
# Two 54c and 58c scout bids filled after the model-based guards shipped. Each
# of those guards asks _silver_fair() first, and it returns None for anything
# it cannot map to a state-level race — the 2028 slate, the seat ladders, the
# primaries, and any race whose table is missing. A guard that answers "no
# opinion" by allowing the trade FAILS OPEN, which is the wrong direction for
# a control whose whole job is to stop bad trades.
#
# This one fails closed and depends on nothing. Above this price a bid needs
# POSITIVE model support to exist at all; with no forecast, the answer is no.
MAX_UNBACKED_BID_C = float(os.environ.get("MAX_UNBACKED_BID_C", "15"))
# A race the model normally prices but currently has no number for: token
# bids only. Missing data is a reason to stop, not a license to guess.
RACE_NO_MODEL_BID_C = float(os.environ.get("RACE_NO_MODEL_BID_C", "2"))


def _bid_allowed(m: str, price_c: float) -> bool:
    """May we rest a BUY here at all? One rule for every loop and the sweep.

    Where the model HAS a number it binds at every price — under the old
    shape a 10c bid on a 0.6% race was 'allowed' merely for being under the
    unbacked cap, and only a separate earner-only check stood in the way.
    Where the model SHOULD have a number and does not (a race family with a
    missing table), that is missing data and it fails closed above token
    size. Only markets the model was never meant to cover — the 2028 slate,
    the seat ladders — fall back to the flat unbacked cap."""
    sv = _silver_fair(m)
    if sv is not None:
        return price_c <= sv + EARN_SILVER_MARGIN
    if _race_family(m):
        return price_c <= RACE_NO_MODEL_BID_C
    return price_c <= MAX_UNBACKED_BID_C
# Per market between new scouts. At 300s a market took over ten minutes to
# collect its three scouts; at 90s it takes three, so a market gets bracketed
# while its book still looks the way it did when the first scout went in.
PROBE_COOLDOWN = 90.0
_PROBE: dict = {"active": {}, "last": {}, "cancelled": set(), "pending": {}}
PROBE_CONFIRM_WAIT = 300.0   # fills feed lag allowance before "vanished"


def _on_book(m: str, side: str, px: float, qty: float,
             placed_ts: float | None = None):
    """Layer-three verification: does the PUBLIC book — the only thing that
    scores — actually show a level at our price big enough to contain our
    order? True/False, or None when no snapshot can fairly judge: cached
    book too stale, OR the snapshot predates the order (a book photographed
    before the order existed cannot contain it — every fresh placement
    showed a false 'NOT ON BOOK' at 0m until this check, 2026-08-16)."""
    ent = tr._BOOK_CACHE.get(m)
    if not ent or time.time() - ent[0] > 300:
        return None
    if placed_ts and ent[0] < placed_ts + 8:   # book must postdate the order
        return None
    lv = (ent[1] or {}).get("bids" if side == "BUY" else "asks") or []
    at = sum(q for p, q in lv if abs(p - px) < 0.005)
    return at >= qty * 0.9


def _probe_log(m: str, ev: str, side: str, px: float, note: str = "") -> None:
    """One line in the prober's own journal, shown on the /map Prober card."""
    with MONITOR.lock:
        log = MONITOR.state.setdefault("probe_log", [])
        log.append({"ts": dt.datetime.now(ET).strftime("%m-%d %I:%M:%S %p"),
                    "m": m, "ev": ev, "side": side,
                    "px": round(px * 100, 1), "note": note})
        del log[:-200]


def _probe_real_touches(book: dict):
    """Best REAL level on each side, with its size: ((px, q) | None) x 2.
    Levels under PROBE_REAL_MIN shares are bait and ignored."""
    bb = next(((p, q) for p, q in book.get("bids") or [] if q >= PROBE_REAL_MIN), None)
    ba = next(((p, q) for p, q in book.get("asks") or [] if q >= PROBE_REAL_MIN), None)
    return bb, ba


def _probe_place(m: str, side: str, px: float, intent: str, note: str) -> str | None:
    # One retry on a rate-limit or a server wobble. At the old pace a dropped
    # scout barely mattered; running several times faster, silently losing
    # placements to 429s would quietly cap the very throughput the pace change
    # is meant to buy, and look like nothing at all in the journal.
    try:
        r = None
        for attempt in range(2):
            r = requests.request(
                "POST", tr.TRADE_API + "/v1/orders",
                headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", "/v1/orders"),
                         "Content-Type": "application/json"},
                json={"marketSlug": m, "intent": intent,
                      "type": "ORDER_TYPE_LIMIT",
                      "price": {"value": f"{px:.2f}", "currency": "USD"},
                      "quantity": PROBE_SIZE,
                      "tif": "TIME_IN_FORCE_GOOD_TILL_CANCEL",
                      "participateDontInitiate": True},
                timeout=20)
            if r.status_code not in (429, 500, 502, 503, 504) or attempt:
                break
            with MONITOR.lock:
                sb = MONITOR.state.setdefault("probe_scoreboard", {})
                sb["throttled"] = int(sb.get("throttled") or 0) + 1
            time.sleep(1.5)
        ok = r.status_code < 300
        oid = None
        if ok:
            try:
                j = r.json()
                o = j.get("order")
                oid = (o.get("id") if isinstance(o, dict) else None) \
                      or j.get("id") or j.get("orderId")
            except Exception:  # noqa: BLE001
                pass
        if ok and oid:
            _own_id("probe", str(oid))
        ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                        "market": m, "side": f"PROBE {note}", "from": "—",
                        "to": round(px * 100, 1), "size": PROBE_SIZE,
                        "status": r.status_code,
                        "response": " ".join(r.text.split())[:100], "verified": ok})
        del ACTIONS[:-20]
        return str(oid) if oid else None
    except Exception:  # noqa: BLE001 — the prober must never kill the poll
        return None


def auto_probe() -> None:
    # one-time owner grants into the info fund, applied exactly once each
    # (the applied list persists with the saved state, surviving restarts)
    granted = False
    with MONITOR.lock:
        grants = MONITOR.state.setdefault("probe_grants", [])
        if "2026-08-15-owner-10usd" not in grants:
            grants.append("2026-08-15-owner-10usd")
            MONITOR.state["probe_budget"] = round(
                float(MONITOR.state.get("probe_budget") or 0.0) + 10.0, 2)
            granted = True
    if granted:   # log outside the lock — _probe_log takes it too
        _probe_log("[owner]", "grant", "+", 0.0, "+$10.00 into the info fund")
    # 2026-08-16 owner reset: the pre-classification-fix evidence is poisoned
    # (phantom fills fed the bands as real trades) and the fund's history is
    # equally suspect. Discard all of it, set the fund to exactly $20, and
    # rebuild every band from post-fix, confirmed-only evidence. Applied
    # once; live resting orders keep their registries — they are real and
    # verified on the book — only the LEARNING starts over.
    reset = False
    with MONITOR.lock:
        grants = MONITOR.state.setdefault("probe_grants", [])
        if "2026-08-16-reset-20usd" not in grants:
            grants.append("2026-08-16-reset-20usd")
            MONITOR.state["probe_log"] = []
            MONITOR.state["probe"] = {}
            MONITOR.state["earn_log"] = []
            MONITOR.state["earn_stats"] = {}
            MONITOR.state.pop("probe_credited", None)
            MONITOR.state["probe_budget"] = 20.0
            reset = True
    if reset:
        _probe_log("[owner]", "reset", "+", 0.0,
                   "old evidence discarded — fund set to $20.00, learning restarts "
                   "on confirmed-only data")
    # 2026-08-16 owner: fund raised to $100 so the prober can stack several
    # scouts per market and tighten its bands overnight. Sets the fund to
    # exactly $100 rather than adding to it — "increase the budget to $100".
    topped = False
    with MONITOR.lock:
        grants = MONITOR.state.setdefault("probe_grants", [])
        if "2026-08-16-owner-100usd" not in grants:
            grants.append("2026-08-16-owner-100usd")
            was = float(MONITOR.state.get("probe_budget") or 0.0)
            MONITOR.state["probe_budget"] = 100.0
            topped = was
    if topped is not False:
        _probe_log("[owner]", "grant", "+", 0.0,
                   f"info fund set to $100.00 (was ${topped:,.2f})")
    # After a rebuild the in-memory registry is empty but our scouts still
    # rest on the exchange. Re-adopt from the mirror saved in state, keeping
    # only orders that still exist — so fills keep moving the fund and TTLs
    # keep rotating across container replacements.
    if not _PROBE["active"]:
        saved = MONITOR.state.get("probe_active_reg") or {}
        if saved:
            live = {str(o.get("id")) for o in MONITOR.orders if o.get("id")}
            for oid, r in saved.items():
                if oid in live and len(r) == 5:
                    _PROBE["active"][oid] = (r[0], r[1], float(r[2]), float(r[3]), r[4])
    if not _auto_on("probe"):
        return
    if os.environ.get("PROBE_PAUSE", "") == "1":
        return
    now = time.time()
    open_ids = {str(o.get("id")) for o in MONITOR.orders if o.get("id")}
    est = MONITOR.state.setdefault("probe", {})
    # 0. settle earlier disappearances: back on the list -> flicker, readopt;
    #    confirmed by the fills feed -> requeue so the fill logic below runs;
    #    neither, past the wait -> a silent exchange cancel, no fund movement
    for oid, (rec, ts_gone) in list(_PROBE["pending"].items()):
        if oid in open_ids or _fill_confirmed(oid):
            _PROBE["active"][oid] = rec
            del _PROBE["pending"][oid]
        elif now - ts_gone > PROBE_CONFIRM_WAIT:
            del _PROBE["pending"][oid]
            _probe_log(rec[0], "vanished", rec[1], rec[2],
                       "gone without a trade — exchange-side cancel")
    # 1. reconcile: a probe missing from open orders that we did not cancel
    #    was FILLED — record the price and place the flip
    for oid, rec in list(_PROBE["active"].items()):
        m, side, px, ts, kind = rec
        if oid in open_ids:
            if now - ts > PROBE_TTL:      # rotate a stale probe
                try:
                    requests.request(
                        "POST", tr.TRADE_API + f"/v1/order/{oid}/cancel",
                        headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST",
                                                   f"/v1/order/{oid}/cancel"),
                                 "Content-Type": "application/json"},
                        json={"marketSlug": m}, timeout=15)
                    _PROBE["cancelled"].add(oid)
                    del _PROBE["active"][oid]
                    # untouched for the whole TTL: fair is beyond this price
                    e = est.setdefault(m, {})
                    if side == "BUY":
                        e["rested_bid"] = max(float(e.get("rested_bid") or 0), px)
                    else:
                        e["rested_ask"] = min(float(e.get("rested_ask") or 1), px)
                    _probe_log(m, "rested", side, px,
                               "no taker for 45 min — rotating")
                except Exception:  # noqa: BLE001
                    pass
            continue
        del _PROBE["active"][oid]
        if oid in _PROBE["cancelled"]:
            _PROBE["cancelled"].discard(oid)
            continue
        # disappearance is a claim — the fills feed decides (silent
        # exchange cancels must not move the fund or feed the model)
        if not _fill_confirmed(oid):
            _PROBE["pending"][oid] = (rec, now)
            continue
        # filled — a real trade happened at px
        e = est.setdefault(m, {})
        e["last_fill"] = {"side": side, "px": px,
                          "ts": dt.datetime.now(ET).strftime("%m-%d %I:%M %p")}
        # A fill is a cost, and it is counted as one. The evidence it carries
        # is still worth having, but the scoreboard the owner reads must show
        # what the information cost, not just what it taught.
        e["fill_ts"] = now
        e["fills"] = int(e.get("fills") or 0) + 1
        with MONITOR.lock:
            sp = MONITOR.state.setdefault("probe_scoreboard", {})
            sp["fills"] = int(sp.get("fills") or 0) + 1
            if kind == "probe":
                # opening fills tie up capital at px; the flip below tries to
                # get it back, and a completed round trip nets out here
                sp["fill_cost_usd"] = round(float(sp.get("fill_cost_usd") or 0)
                                            + (px if side == "BUY" else 0.0), 4)
            else:
                sp["fill_cost_usd"] = round(float(sp.get("fill_cost_usd") or 0)
                                            - (px if side == "SELL" else 0.0), 4)
        _probe_log(m, "FILLED" if kind == "probe" else "round trip", side, px,
                   f"taken at {px*100:.0f}c — a fill is a loss, not a win"
                   if kind == "probe" else "flip filled — position closed out")
        # the info fund moves ONLY on prober activity: its sales and its
        # scouts' reward earnings in, its buys out
        with MONITOR.lock:
            bud = float(MONITOR.state.get("probe_budget") or 0.0)
            bud += px if side == "SELL" else -px
            MONITOR.state["probe_budget"] = round(max(0.0, bud), 4)
        if side == "BUY":
            e["traded_at_bid"] = px       # a seller exists at px: fair <= px
            fpx = round(px + PROBE_FLIP_TICKS * 0.01, 2)
            if kind == "probe" and 0.01 <= fpx <= 0.99:
                fid = _probe_place(m, "SELL", fpx, "ORDER_INTENT_SELL_LONG",
                                   f"flip sell (bid {px*100:.0f}c filled)")
                if fid:
                    _PROBE["active"][fid] = (m, "SELL", fpx, now, "flip")
                    _probe_log(m, "flip", "SELL", fpx,
                               f"reselling the fill from {px*100:.0f}c")
        else:
            e["traded_at_ask"] = px       # a buyer exists at px: fair >= px
            fpx = round(px - PROBE_FLIP_TICKS * 0.01, 2)
            # buy back the sold share only if the fund can pay for it
            if kind == "probe" and 0.01 <= fpx <= 0.99 and \
                    float(MONITOR.state.get("probe_budget") or 0.0) >= fpx:
                fid = _probe_place(m, "BUY", fpx, "ORDER_INTENT_BUY_LONG",
                                   f"flip buy-back (sale at {px*100:.0f}c filled)")
                if fid:
                    _PROBE["active"][fid] = (m, "BUY", fpx, now, "flip")
                    _probe_log(m, "flip", "BUY", fpx,
                               f"re-buying the share sold at {px*100:.0f}c")
    # 1b. outbid/undercut: a competitor resting REAL size at a better price
    # than our scout is revealed preference — someone else's money saying
    # fair is beyond our scout's price (owner, 2026-08-15: "the probe found
    # a good price but was outbid — that IS the information"). One event
    # per scout, so a hovering competitor doesn't flood the journal.
    beaten = _PROBE.setdefault("beaten", set())
    for oid, rec in list(_PROBE["active"].items()):
        m, side, px, ts, kind = rec
        if kind != "probe" or oid in beaten or oid not in open_ids:
            continue
        ent = tr._BOOK_CACHE.get(m)
        if not ent or now - ent[0] > 300:
            continue
        rbb, rba = _probe_real_touches(ent[1])
        if side == "BUY" and rbb and rbb[0] > px + 1e-9:
            beaten.add(oid)
            _probe_log(m, "outbid", "BUY", rbb[0],
                       f"{rbb[1]:,.0f} real shares bidding above our "
                       f"{px*100:.0f}c scout")
        elif side == "SELL" and rba and rba[0] < px - 1e-9:
            beaten.add(oid)
            _probe_log(m, "undercut", "SELL", rba[0],
                       f"{rba[1]:,.0f} real shares asking below our "
                       f"{px*100:.0f}c scout")
    beaten &= set(_PROBE["active"])   # forget scouts that are gone

    # 2. seed new probes at random interior ticks
    if len(_PROBE["active"]) >= PROBE_ACTIVE_MAX:
        return
    placed = 0
    # Cover the WHOLE universe rather than sampling it. A random shuffle kept
    # re-picking markets the prober had already mapped while others were never
    # visited at all, so the map filled in slowly and unevenly. Unvisited
    # markets go first, then least-recently-scouted, with the shuffle kept only
    # to break ties so identical-looking markets do not always order the same.
    mkts = [m for m in tr._BOOK_CACHE if m.startswith(PROBE_PREFIXES)]
    random.shuffle(mkts)
    mkts.sort(key=lambda m_: (1 if (est.get(m_) or _PROBE["last"].get(m_)) else 0,
                              _PROBE["last"].get(m_, 0.0)))
    for m in mkts:
        if placed >= PROBE_MAX_PER_POLL or len(_PROBE["active"]) >= PROBE_ACTIVE_MAX:
            break
        if now - _PROBE["last"].get(m, 0.0) < PROBE_COOLDOWN:
            continue
        # a fill here cost us money — let the market settle before going back
        if now - float((est.get(m) or {}).get("fill_ts") or 0) < PROBE_FILL_COOLDOWN:
            continue
        here = [r for r in _PROBE["active"].values() if r[0] == m and r[4] == "probe"]
        if len(here) >= PROBE_PER_MARKET:
            continue
        ent = tr._BOOK_CACHE.get(m)
        if not ent or now - ent[0] > 300:
            continue
        rbb, rba = _probe_real_touches(ent[1])
        if rbb is None or rba is None:
            continue
        bb, ba = rbb[0], rba[0]
        lo_t = round(bb / 0.01) + 1
        hi_t = round(ba / 0.01) - 1
        if hi_t - lo_t + 1 < PROBE_MIN_GAP:
            continue          # spread too tight to learn anything
        # never two scouts of ours at the same tick — a repeated price is a
        # repeated observation, which adds cost without adding confidence
        taken = {round(r[2] / 0.01) for r in here}
        free = [t for t in range(lo_t, hi_t + 1) if t not in taken]
        if not free:
            continue
        # Draw toward the safe end of the gap. Two draws, keep the one further
        # from the touch that would take us: cheap way to bias without ever
        # excluding the informative middle entirely.
        t = random.choice(free)
        alt = random.choice(free)
        if random.random() < PROBE_SAFE_BIAS:
            t = min(t, alt)          # a BUY scout wants the LOWER tick
        px = round(t * 0.01, 2)
        px_sell = round(max(t, alt) * 0.01, 2) if random.random() < PROBE_SAFE_BIAS \
            else round(t * 0.01, 2)
        # which sides can this market afford?
        #   SELL: only from inventory we already hold (net long >= 2, keeping
        #         a share so a scout never zeroes the position)
        #   BUY : only what the info fund covers, counting scouts resting
        net = tr._num((MONITOR.positions.get(m) or {}).get("netPosition")) or 0
        can_sell = net >= PROBE_SIZE + 1
        fund = float(MONITOR.state.get("probe_budget") or 0.0)
        resting_buys = sum(r[2] for r in _PROBE["active"].values() if r[1] == "BUY")
        can_buy = px <= PROBE_MAX_PX and resting_buys + px <= fund
        # THE MODEL PICKS THE SIDE WHEN IT HAS A VIEW. A random tick in the gap
        # is fine when we know nothing, but bidding 54c for a contract Silver
        # puts at 0.4c is not a probe, it is a donation — and it is certain to
        # be taken, because the other side of that trade is free money (owner,
        # 2026-08-16: "just go on the other side if the gap is that big, it's
        # better to be on the side with an edge").
        #
        # Above the forecast we want to be SELLING, below it BUYING. If the
        # edge is on a side we cannot take — no inventory to sell, or no fund
        # to buy — we skip the market rather than take the losing side of our
        # own analysis.
        svp = _silver_fair(m)
        want = None
        if svp is not None:
            if px * 100 > svp + PROBE_SILVER_EDGE:
                want = "SELL"
            elif px * 100 < svp - PROBE_SILVER_EDGE:
                want = "BUY"
        if not _bid_allowed(m, px * 100):
            can_buy = False       # too dear to bid without a forecast behind it
        if want == "BUY" and not can_buy:
            continue
        if want == "SELL" and can_sell:
            side = "SELL"
        elif want == "BUY" and can_buy:
            side = "BUY"
        elif want is not None:
            continue              # edge is on a side we cannot take — leave it
        elif can_sell and can_buy:
            side = "BUY" if random.random() < 0.5 else "SELL"
        elif can_sell:
            side = "SELL"
        elif can_buy:
            side = "BUY"
        else:
            continue              # no ammo here: no inventory, fund can't cover a bid
        # a sell scout's danger is a buyer lifting it, so its safe end is the
        # HIGH side of the gap — the mirror of the bid case
        if side == "SELL":
            px = px_sell
            if round(px / 0.01) in taken:
                continue
        intent = "ORDER_INTENT_BUY_LONG" if side == "BUY" else "ORDER_INTENT_SELL_LONG"
        oid = _probe_place(m, side, px, intent,
                           f"{side.lower()} scout" +
                           (" (inventory)" if side == "SELL" else " (fund)"))
        _PROBE["last"][m] = now
        if oid:
            _PROBE["active"][oid] = (m, side, px, now, "probe")
            _probe_log(m, "scout", side, px, "resting inside the gap")
            placed += 1
    # mirror the registry so a rebuild can re-adopt (see top of function)
    with MONITOR.lock:
        MONITOR.state["probe_active_reg"] = {k: list(v) for k, v in _PROBE["active"].items()}


def _race_family(m: str) -> bool:
    """Is this a market the Silver model is SUPPOSED to cover? Used to tell
    'no forecast because it is a 2028 nomination' (fine, other rules apply)
    from 'no forecast for a Senate race the model normally prices' (not fine
    — that is missing data, and missing data must fail closed)."""
    parts = m.split("-")
    fam = any(t in ("usse", "ussep", "usgub", "usgubp") for t in parts)
    party = any(t in ("dem", "rep") for t in parts)
    st = any(len(t) == 2 and t.isalpha() and t != "us" for t in parts)
    return fam and party and st


def _silver_fair(m: str) -> float | None:
    """Model prior for race markets, in cents. None for anything the model
    does not cover — the callers decide what None means for them.

    Loads its own table. It used to read the SILVER global and the only
    thing that ever FILLED that global was a /map page render — so after
    every restart the loops ran with no model until somebody happened to
    open the map, and every model-based guard quietly became a coin flip.
    The CO governor scouts bought at 10c and 14c against a 0.2% forecast
    came from exactly that window. _silver_races() self-throttles on a
    6-hour TTL, so this costs one fetch per boot, not one per call."""
    try:
        races = _silver_races() or {}
        parts = m.split("-")
        fam = ("senate" if any(t in ("usse", "ussep") for t in parts)
               else "governor" if any(t in ("usgub", "usgubp") for t in parts)
               else None)
        if not fam:
            return None
        party = next((t for t in parts if t in ("dem", "rep")), None)
        st = next((t for t in parts if len(t) == 2 and t.isalpha()
                   and t not in ("us",)), None)
        if not party or not st:
            return None
        row = (races.get(fam) or {}).get(st.upper()) or {}
        v = row.get(party)
        return float(v) * 100.0 if v is not None else None
    except Exception:  # noqa: BLE001
        return None


def _bayes_fair(m: str) -> dict | None:
    """A deliberately simple Bayesian read of a market's fair price from the
    prober's evidence. Grid prior over 1..99c; every journal event is a soft
    one-sided observation through a logistic likelihood (scale ~2 ticks):

      probe bid FILLED at p   -> a seller accepted p   -> fair likely <= p
      probe ask FILLED at p   -> a buyer paid p        -> fair likely >= p
      flip (round trip) fills -> the same, from the flip's side
      probe rested 45 min     -> weak opposite evidence (thin flow means
                                 absence of a taker proves little — 0.35x)

    plus the current de-baited real touches as gentle anchors (someone
    risks actual size there). Returns the posterior median and the 10-90%
    credible interval, in cents."""
    evs = [l for l in (MONITOR.state.get("probe_log") or []) if l.get("m") == m]
    ent = tr._BOOK_CACHE.get(m)
    bb = ba = None
    bbw = baw = 0.5
    if ent and time.time() - ent[0] < 900:
        rbb, rba = _probe_real_touches(ent[1])
        # size-weighted anchors: a big resting level is stronger revealed
        # preference than a small one
        def _aw(q: float) -> float:
            return 0.4 if q < 100 else (0.8 if q < 1000 else 1.2)
        if rbb:
            bb, bbw = rbb[0], _aw(rbb[1])
        if rba:
            ba, baw = rba[0], _aw(rba[1])
    # scouts still resting are evidence too, growing with age: no taker at
    # that price for this long pushes fair away from it. Weighted up to the
    # same 0.35 a completed rotation earns, pro-rated by age/TTL.
    nowp = time.time()
    partial = []
    for r in _PROBE["active"].values():
        if r[0] != m or r[4] != "probe":
            continue
        w = 0.35 * min((nowp - r[3]) / PROBE_TTL, 1.0)
        if w > 0.02:
            partial.append((r[1], r[2] * 100, w))
    sv = _silver_fair(m)
    if not evs and not partial and bb is None and ba is None and sv is None:
        return None
    S = 2.0
    def sig(x: float) -> float:
        return 1.0 / (1.0 + math.exp(-max(-30.0, min(30.0, x))))
    def llog(v: float) -> float:
        return math.log(max(v, 1e-9))
    logp = [0.0] * 100
    for f in range(1, 100):
        lp = 0.0
        for l in evs:
            p = float(l.get("px") or 0)
            side = l.get("side")
            ev = l.get("ev")
            if ev == "FILLED":
                lp += llog(sig((p - f) / S)) if side == "BUY" else llog(sig((f - p) / S))
            elif ev == "round trip":
                # the FLIP filled: a SELL flip filling means a buyer at p
                lp += llog(sig((f - p) / S)) if side == "SELL" else llog(sig((p - f) / S))
            elif ev == "rested":
                if side == "BUY":
                    lp += 0.35 * llog(1.0 - 0.8 * sig((p - f) / S))
                else:
                    lp += 0.35 * llog(1.0 - 0.8 * sig((f - p) / S))
            elif ev == "outbid":     # real money bidding above our scout: fair >= p
                lp += 0.5 * llog(sig((f - p) / S))
            elif ev == "undercut":   # real money asking below our scout: fair <= p
                lp += 0.5 * llog(sig((p - f) / S))
        for side, p, w in partial:
            if side == "BUY":
                lp += w * llog(1.0 - 0.8 * sig((p - f) / S))
            else:
                lp += w * llog(1.0 - 0.8 * sig((f - p) / S))
        if bb is not None:
            lp += bbw * llog(sig((f - bb * 100) / S))
        if ba is not None:
            lp += baw * llog(sig((ba * 100 - f) / S))
        if sv is not None:
            # Window scaled to the forecast's own uncertainty, and weighted to
            # match the heaviest book anchor.
            #
            # A flat +/-6c was wrong at the extremes. On New Mexico Senate,
            # which Silver puts at 0.62%, it licensed anything from 1c to 6.6c
            # and left a median of 5c — an order of magnitude out — before the
            # book was even consulted. The uncertainty of a probability
            # estimate scales with sqrt(p(1-p)), so the window does too: about
            # +/-6c near a coin flip, about +/-1.5c on a race nobody thinks is
            # close. At weight 0.6 against touch anchors at 1.2 the book also
            # outvoted the model two to one per term; matched at 1.2, a
            # forecast and a wall of resting size carry equal say, and it takes
            # real trades to move fair value away from the forecast.
            sd = math.sqrt(max(0.0, (sv / 100.0) * (1 - sv / 100.0)))
            win = max(1.5, 6.0 * sd / 0.5)
            lp += 1.2 * (llog(sig((f - (sv - win)) / S))
                         + llog(sig(((sv + win) - f) / S)))
        logp[f] = lp
    mx = max(logp[1:])
    ps = [0.0] + [math.exp(l - mx) for l in logp[1:]]
    tot = sum(ps) or 1.0
    cum, lo, med, hi = 0.0, None, None, None
    for i in range(1, 100):
        cum += ps[i] / tot
        if lo is None and cum >= 0.10:
            lo = i
        if med is None and cum >= 0.50:
            med = i
        if hi is None and cum >= 0.90:
            hi = i
    n_hard = sum(1 for l in evs if l.get("ev") in ("FILLED", "round trip"))
    n_rest = sum(1 for l in evs if l.get("ev") == "rested") \
             + sum(1 for _, _, w in partial if w >= 0.175)   # half-aged or more
    return {"med": med, "lo": lo, "hi": hi, "n": len(evs), "fills": n_hard,
            "rested": n_rest,
            "bb": round(bb * 100, 1) if bb is not None else None,
            "ba": round(ba * 100, 1) if ba is not None else None}


# --- earner: model-confident small bids (owner, 2026-08-15) -----------------
# When the Bayesian band is TIGHT and built on real trades, rest a small bid
# at fair-or-better and collect the side's scoring. Bid side only — the ask
# side is already defender-managed, and two loops steering the same orders
# would fight. Price = min(posterior median − 1 tick, the de-baited real
# touch): joining real money when fair supports it, otherwise resting alone
# BELOW fair, where being picked off is a purchase at better than fair — the
# opposite of the tuccar trap. Sizes are worst-case-dollar capped per market
# and in total, far under the buying-power ceiling.
# INVARIANT (owner, 2026-08-15): the earner and the prober's info fund are
# SEPARATE BOOKS. state["probe_budget"] moves only on the prober's own
# fills (its sales in, its buys out — see auto_probe's reconcile). Earner
# sales and purchases never credit or debit it, and earner journal entries
# ("earn ...") are deliberately ignored by _bayes_fair — an earn fill sits
# at fair-1 because the model put it there, so counting it as evidence
# would let the model confirm itself. Earner sizing stays small: EARN_MAX_USD
# per market, EARN_TOTAL_USD across all.
#
# The /map switches are the OWNER'S controls and the code never overrules
# them (the short-lived CONSERVE_BP override taught that lesson on
# 2026-08-15: "I'll turn it off if that is what I want"). Buying-power
# discipline lives in each loop's own hard caps instead.
# Aggression raised 2026-08-15 late (owner: "surely there's more value out
# there based on what the prober is finding"): double the per-market and
# total budgets, twice the placement cadence, and a GRADUATED confidence
# gate — one real trade is enough when the band is very tight (<=3 ticks),
# two when it's merely tight (<=6). The price rule stays: never above
# median minus a tick, never above the real touch. Aggression buys more
# coverage, not worse prices.
# v3 (owner, 2026-08-16): "the earner is not meant to sit — it's meant to
# earn using what we know." The deal test replaced the fair test: at penny
# prices an order's INCOME dwarfing its TOTAL-LOSS worst case is the real
# safety (a 1-share bid at a thin 7c touch earns $2.48/day against a 7c
# ruin). Price may go through and past the band; size shrinks as
# confidence does — proven zone gets full exposure, the stretch zone 40%,
# the speculative zone above the band 15%. The penny ceiling keeps "total
# loss is trivial" true; expensive markets are not the earner's game.
EARN_MAX_USD = float(os.environ.get("EARN_MAX_USD", "6.0"))
EARN_TOTAL_USD = float(os.environ.get("EARN_TOTAL_USD", "100.0"))
EARN_MAX_SHARES = 200
EARN_PX_MAX_C = int(os.environ.get("EARN_PX_MAX_C", "10"))
# Above the penny ceiling the earner may only act on KNOWLEDGE, never on hope
# (owner, 2026-08-16: "earner should use what probe is learning to place where
# it can earn"). Two conditions together, and it is the pair that makes it safe:
#   * the price sits at or under the band's 10th percentile — the model says
#     fair value is clearly above us, so a taker coming down to us is unlikely
#   * real size is already queued at or above that price — we rest BEHIND other
#     people's money, the owner's wall-join rule: "if there is a big wall you
#     can still join that, it won't get taken because it will be behind the rest"
# Without the queue this is just a bid at the touch, which is what the bait
# anchors farm. With it, the order earns while somebody else absorbs the flow.
EARN_SAFE_MAX_C = int(os.environ.get("EARN_SAFE_MAX_C", "60"))
# How far above a Silver forecast the earner may still pay. Reward income can
# justify a few cents of premium over fair value; it cannot justify sixteen
# times it.
EARN_SILVER_MARGIN = float(os.environ.get("EARN_SILVER_MARGIN", "3"))
EARN_QUEUE_MIN = float(os.environ.get("EARN_QUEUE_MIN", "1000"))
# A filled earner order is a loss. The market goes quiet for two hours rather
# than being re-entered at the price that just proved takeable.
EARN_FILL_COOLDOWN = float(os.environ.get("EARN_FILL_COOLDOWN", "7200"))
# Stand-down after an exchange-side cancel, multiplied by how many times it has
# happened in that market (capped at 6x) — a market that keeps eating orders
# gets left alone for the night instead of absorbing every attempt.
EARN_VANISH_COOLDOWN = float(os.environ.get("EARN_VANISH_COOLDOWN", "1800"))
# Flipping a fill back out. Once a bid fills we HOLD the stock, and selling
# stock we hold is a SELL_LONG, which costs no buying power — the exchange only
# trims a new ask against BP when it opens a short. So the flip is the cheapest
# order on the book: it recovers the cash the fill just spent, and it earns
# rewards on the ask side the whole time it waits (owner, 2026-08-16: "you can
# be more aggressive with those because they don't decrease buying power").
# It is therefore exempt from the earner's dollar cap, which exists to limit
# money at RISK — a flip is money already spent, coming back.
EARN_FLIP_TICKS = int(os.environ.get("EARN_FLIP_TICKS", "2"))
EARN_FLIP_RETRY = float(os.environ.get("EARN_FLIP_RETRY", "1800"))
# Ceiling on one market's flip order, so a mis-read position can never turn
# into an enormous ask in a single step.
EARN_FLIP_MAX_SHARES = int(os.environ.get("EARN_FLIP_MAX_SHARES", "400"))
# LADDER DOWN RATHER THAN HOLD OUT. A flip two ticks above a 5c cost is asking
# for a double, and doubles on a longshot rarely come — meanwhile the capital
# is idle and the prober has most of the universe still to map (owner,
# 2026-08-16: "don't sit on all the shares trying to make a 2x profit because
# that rarely happens... maybe you only sell a portion of them to find out
# where someone will actually pick them up").
#
# So every half hour a flip that has not sold moves HALF its size to the
# midpoint between its price and its floor. The other half is freed and the
# normal flip path re-places it at the touch, which turns one stubborn rung
# into a ladder without any special code for ladders: cheap size that actually
# transacts, dearer size that keeps the upside. Each rung that sells or holds
# is also a price observation the prober gets for free.
EARN_FLIP_STEP_AFTER = float(os.environ.get("EARN_FLIP_STEP_AFTER", "1800"))
# AFTER THIS LONG, STOP ANCHORING TO WHAT WE PAID. Our cost is sunk; it says
# nothing about what the stock is worth now. If the price genuinely moved
# against us, a floor at cost+1 means the shares never sell and the fill is
# recovered at zero percent — which is exactly where the earner sits today
# (owner, 2026-08-16: "selling at a loss isn't terrible, that reduces the net
# cost of fills, which is 100% not because we haven't flipped anything").
#
# Past this point the floor becomes the MARKET's price rather than ours: one
# tick above the best bid, the lowest an ask can rest without crossing. That
# is not giving the shares away — it is selling them for what somebody is
# actually willing to pay, which beats holding them at a price nobody is.
EARN_FLIP_LOSS_AFTER = float(os.environ.get("EARN_FLIP_LOSS_AFTER", "7200"))
# GRADUATION. The point of the earner is to find where the money is, not to
# sit on the first thing it finds — but an order that has PROVED it earns and
# stays put should not keep occupying the search budget while it does so
# (owner, 2026-08-16: "once we found it, move on to others while those orders
# earn"). A proven order graduates: it keeps resting and keeps earning, and it
# stops counting against the dollar cap, which frees that money to go looking.
#
# It has to have earned the label, not merely survived: an hour on the book,
# still visibly there, paying enough to cover its own worst case inside two
# days, in a market that has never taken a fill off us. If a graduate stops
# earning it is demoted back under the cap and judged like anything else.
#
# Graduates carry their own ceiling. They are the orders least likely to fill,
# but "uncapped" and "real money" do not belong in the same sentence.
EARN_GRAD_AGE = float(os.environ.get("EARN_GRAD_AGE", "3600"))
EARN_GRAD_MIN_RATE = float(os.environ.get("EARN_GRAD_MIN_RATE", "0.50"))
EARN_GRAD_PAYBACK = float(os.environ.get("EARN_GRAD_PAYBACK", "2.0"))
EARN_GRAD_MAX_USD = float(os.environ.get("EARN_GRAD_MAX_USD", "150.0"))
# Same idea for an order we pulled ourselves: it was not earning, so the market
# should wait its turn behind untried ones rather than being re-entered at once.
EARN_WITHDRAW_COOLDOWN = float(os.environ.get("EARN_WITHDRAW_COOLDOWN", "3600"))
# Continual search. The scarce resource is DOLLARS, not slots — the earner can
# hold EARN_TOTAL_USD of worst case and no more — so once it is close to full,
# a mediocre order that merely clears the entry test would otherwise squat on
# capital forever while better markets go untried. Every half hour at capacity,
# the worst few by yield are abandoned to free the money for somewhere better
# (owner, 2026-08-16: "there should be a continual search to try and find
# something better; if we get full on earners, periodically take the three or
# four worst and abandon them").
#
# Ranked by earnings per dollar committed, not by raw $/day: the cap is a
# dollar budget, so a small order earning well is worth more of it than a big
# one earning slightly more in absolute terms.
EARN_ROTATE_EVERY = float(os.environ.get("EARN_ROTATE_EVERY", "1800"))
EARN_ROTATE_N = int(os.environ.get("EARN_ROTATE_N", "3"))
EARN_FULL_FRAC = float(os.environ.get("EARN_FULL_FRAC", "0.85"))
EARN_MAX_PER_POLL = 4
EARN_COOLDOWN = 300.0
_EARN: dict = {"orders": {}, "last": {}, "cancelled": set(), "pending": {}}
EARN_CONFIRM_WAIT = 300.0    # fills feed lag allowance before "vanished"


def _own_id(bucket: str, oid: str) -> None:
    """Remember that `bucket` (earn/probe) placed this order id, for as long as
    it might turn up in the fills feed. Kept in state so the answer survives a
    rebuild, and capped so it cannot grow without bound."""
    if not oid:
        return
    with MONITOR.lock:
        ids = MONITOR.state.setdefault("loop_ids", {}).setdefault(bucket, [])
        ids.append(str(oid))
        del ids[:-3000]


def _fill_src(oid: str) -> str:
    """Which of our loops placed the order behind a fill — '' if none did,
    which means it was one of the resting rungs or a hand-placed order."""
    if not oid:
        return ""
    li = MONITOR.state.get("loop_ids") or {}
    if oid in _EARN["orders"] or oid in set(li.get("earn") or []):
        return "earner"
    if oid in _PROBE["active"] or oid in set(li.get("probe") or []):
        return "prober"
    return ""


def _fill_confirmed(oid: str) -> bool:
    """Is this order id in the exchange's own trade records? Disappearance
    from the open-order list is NOT a fill — the exchange silently cancels
    resting orders (the 2026-08-15 floor episode) and the list flickers.
    Only the fills feed decides."""
    return any(str(t.get("oid")) == oid for t in (MONITOR.trades or []))




def _earn_log(m: str, ev: str, px: float, qty: int, note: str = "") -> None:
    """The earner's own journal and tallies — separate from the prober's,
    like its money. Shown on the /map Earner card."""
    with MONITOR.lock:
        log = MONITOR.state.setdefault("earn_log", [])
        log.append({"ts": dt.datetime.now(ET).strftime("%m-%d %I:%M:%S %p"),
                    "m": m, "ev": ev, "px": round(px * 100, 1),
                    "qty": qty, "note": note})
        del log[:-150]
        st = MONITOR.state.setdefault("earn_stats", {})
        st[ev] = int(st.get(ev) or 0) + 1
        if ev == "filled":
            st["spent_usd"] = round(float(st.get("spent_usd") or 0) + px * qty, 2)


def _rate_trend(m: str) -> tuple[float, float]:
    """(peak, current) $/day for a market over the stored ~8h window.

    This is the series behind the "Biggest drops" card. A market whose rate has
    collapsed against its own peak is one somebody else has moved into: the
    side got diluted, or the touch walked away from our order. It shows up here
    before our own payback test notices, which is the whole value of watching
    it (owner, 2026-08-16: "look at this from time to time to see where to look
    for changes in earning rate").

    Only meaningful where we currently hold something — with no order resting,
    the rate is zero for the dull reason that we are not there."""
    ser = (MONITOR.state.get("series") or {}).get(m) or []
    if len(ser) >= 5:
        return max(v for _, v in ser), ser[-1][1]
    # fall back to the slim peak/current map, which survives a restart
    pc = (MONITOR.state.get("rate_peak") or {}).get(m)
    if pc and len(pc) == 2:
        return float(pc[0]), float(pc[1])
    return 0.0, 0.0


def _earn_outstanding_usd() -> float:
    """Money the earner has at risk AND still charged to its search budget.
    Graduates are excluded on purpose — they have proved themselves, so the
    budget they were using goes back to looking for the next one."""
    grad = _EARN.get("grad") or set()
    return sum(px / 100.0 * q for oid, (_, _, px, q, _) in _EARN["orders"].items()
               if oid not in grad)


def _earn_graduated_usd() -> float:
    grad = _EARN.get("grad") or set()
    return sum(px / 100.0 * q for oid, (_, _, px, q, _) in _EARN["orders"].items()
               if oid in grad)


def auto_earn() -> None:
    # accrue what the earner's resting bids are EARNING (reward-scoring
    # rate integrated over time, same formula as the headline counter but
    # filtered to the earner's own order ids) — runs even while the switch
    # is off so a resting order's income is never lost from the tally
    if _EARN["orders"] or _PROBE["active"] or _EARN.get("flips"):
        nowa = time.time()
        by_id = {str(o.get("id")): o for o in MONITOR.orders if o.get("id")}
        rate = sum(float((by_id.get(oid) or {}).get("est_day") or 0)
                   for oid in _EARN["orders"])
        # A FLIP EARNS WHILE IT WAITS. It is a resting order on the ask side
        # and the exchange scores it like any other, but it lived in its own
        # registry and the accrual only ever summed the bids — so every reward
        # a flip earned went uncounted, and the earner's economics read worse
        # than they were (owner, 2026-08-16, asking exactly this). Tallied
        # separately from the bids because it answers a different question:
        # the bids say whether hunting for markets pays, the flips say whether
        # recovering from a fill pays for itself on the way out.
        flip_rate = sum(float((by_id.get(oid) or {}).get("est_day") or 0)
                        for oid in (_EARN.get("flips") or {}))
        # the prober's scouts earn rewards too while they rest — counted in
        # the same tracker, and their share is CREDITED TO THE INFO FUND so
        # scouting pays for more scouting (owner, 2026-08-16)
        probe_rate = sum(float((by_id.get(oid) or {}).get("est_day") or 0)
                         for oid in _PROBE["active"])
        with MONITOR.lock:
            st = MONITOR.state.setdefault("earn_stats", {})
            last = float(st.get("_acc_ts") or 0)
            if last:
                dtd = (nowa - last) / 86400.0
                if rate > 0:
                    st["earned_usd"] = round(float(st.get("earned_usd") or 0)
                                             + rate * dtd, 4)
                if flip_rate > 0:
                    st["flip_earned_usd"] = round(
                        float(st.get("flip_earned_usd") or 0) + flip_rate * dtd, 4)
                if probe_rate > 0:
                    inc = probe_rate * dtd
                    st["probe_earned_usd"] = round(
                        float(st.get("probe_earned_usd") or 0) + inc, 4)
                    MONITOR.state["probe_budget"] = round(
                        float(MONITOR.state.get("probe_budget") or 0.0) + inc, 4)
            st["_acc_ts"] = nowa
    # Re-adopt the registry FIRST. It used to happen after the switch check,
    # so with the earner off the in-memory registry stayed empty and the
    # cleanup below iterated nothing at all — it ran every poll and did
    # nothing, while the bad orders sat on the book filling.
    if not _EARN["orders"]:
        for oid_, r_ in (MONITOR.state.get("earn_orders_reg") or {}).items():
            if len(r_) == 5:
                _EARN["orders"][oid_] = (r_[0], r_[1], int(r_[2]), int(r_[3]), float(r_[4]))

    # WITHDRAW ANYTHING THE MODEL SAYS WE SHOULD NEVER HAVE BID, and do it
    # whether or not the switch is on. The price cap only gated NEW orders, so
    # the bids already resting at 10c on a 0.62% race kept filling after the
    # cap shipped — three more while the owner was reading about the first.
    # Turning the earner off stopped new placements and, until now, also
    # stopped the cleanup, which left the bad orders resting.
    #
    # Cancelling is not placing. It only ever reduces exposure, so it is not
    # gated on the switch.
    sweep = []
    for o_ in MONITOR.orders:
        oid_ = str(o_.get("id") or "")
        m_ = o_.get("market") or ""
        if not oid_ or not m_ or o_.get("side") != "BUY":
            continue                      # an ask above fair is a good ask
        px_ = float(o_.get("price") or 0) * 100
        qty_ = float(o_.get("size") or 0)
        if _bid_allowed(m_, px_):
            continue
        sweep.append((oid_, m_, px_, qty_))
    for oid, m, px, qty in sweep:
        sv_ = _silver_fair(m) or 0.0
        try:
            requests.request(
                "POST", tr.TRADE_API + f"/v1/order/{oid}/cancel",
                headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST",
                                           f"/v1/order/{oid}/cancel"),
                         "Content-Type": "application/json"},
                json={"marketSlug": m}, timeout=15)
            _EARN["cancelled"].add(oid)
            _EARN["orders"].pop(oid, None)
            (_EARN.get("grad") or set()).discard(oid)
            _EARN["last"][m] = time.time() + 86400          # done with this market
            _earn_log(m, "pulled off-model", px / 100.0, qty,
                      f"bid {px:.0f}¢ against a model fair of {sv_:.1f}¢ — "
                      "never should have rested here")
        except Exception:  # noqa: BLE001
            pass
    if not _auto_on("earn"):
        return
    if os.environ.get("EARN_PAUSE", "") == "1":
        return
    if not _EARN["orders"]:
        saved = MONITOR.state.get("earn_orders_reg") or {}
        if saved:
            live = {str(o.get("id")) for o in MONITOR.orders if o.get("id")}
            for oid, r in saved.items():
                if oid in live and len(r) == 5:
                    _EARN["orders"][oid] = (r[0], r[1], int(r[2]), int(r[3]), float(r[4]))
    if not _EARN.get("flips"):
        live = {str(o.get("id")) for o in MONITOR.orders if o.get("id")}
        for oid, r in (MONITOR.state.get("earn_flips_reg") or {}).items():
            if oid in live and len(r) >= 4:
                _EARN.setdefault("flips", {})[oid] = (
                    r[0], float(r[1]), int(r[2]), float(r[3]),
                    float(r[4]) if len(r) > 4 else float(r[1]) - EARN_FLIP_TICKS,
                    float(r[5]) if len(r) > 5 else float(r[3]))
    if not _EARN.get("toflip"):
        _EARN["toflip"] = [list(j) for j in (MONITOR.state.get("earn_toflip") or [])
                           if len(j) == 4]
    if not _EARN.get("grad"):
        _EARN["grad"] = set(MONITOR.state.get("earn_grad") or [])
    if not _EARN.get("adopt"):
        _EARN["adopt"] = [list(j) for j in (MONITOR.state.get("earn_adopt") or [])
                          if len(j) >= 5]
    now = time.time()
    open_ids = {str(o.get("id")) for o in MONITOR.orders if o.get("id")}
    # FILL ACCOUNTING COMES FROM THE FILLS FEED, the only place the truth
    # lives. The old counters incremented when an order VANISHED from the open
    # list, and a partial fill never vanishes: a 60-share bid that fills 50
    # still rests with 10 on it, so $5.00 of stock was bought and booked as
    # nothing. The card read "2 fills costing $2.77" against $7.77 really
    # spent. The feed aggregates per order id, carries the true filled
    # quantity, and _fill_src already says which loop owns each id.
    #
    # Totals come from a per-order ledger held in state rather than a sum over
    # the feed, because the feed is a rolling window and anything ageing out of
    # it would quietly subtract itself from the totals.
    with MONITOR.lock:
        led = MONITOR.state.setdefault("earn_ledger", {})
        for t in (MONITOR.trades or []):
            oid_ = str(t.get("oid") or "")
            if not oid_ or _fill_src(oid_) != "earner":
                continue
            q_ = float(t.get("filled") or 0)
            pc_ = float(t.get("price_cents") or 0)
            if q_ <= 0 or pc_ <= 0:
                continue
            led[oid_] = [t.get("market") or "", pc_, q_,
                         1 if str(t.get("verb")) == "Bought" else 0]
        for k_ in list(led)[:max(0, len(led) - 400)]:
            del led[k_]
        bought = sum(r[1] / 100.0 * r[2] for r in led.values() if r[3])
        sold = sum(r[1] / 100.0 * r[2] for r in led.values() if not r[3])
        st_ = MONITOR.state.setdefault("earn_stats", {})
        st_["fills"] = sum(1 for r in led.values() if r[3])
        st_["bought_usd"] = round(bought, 4)
        st_["recovered_usd"] = round(sold, 4)
        st_["fill_cost_usd"] = round(bought - sold, 4)
        # WHAT STILL NEEDS FLIPPING is derived from current state every poll,
        # not from a one-shot list of order ids. The one-shot version wedged:
        # when the self-correction below pulled a set of flips, their ids were
        # already marked done, so nothing re-placed them and 84 shares sat with
        # no ask against them. Recomputing means a cancelled, vanished or
        # partial flip simply comes back round.
        want = {}
        for oid_, (m_, pc_, q_, isbuy) in led.items():
            if not m_:
                continue
            a = want.setdefault(m_, [0.0, 0.0, 0.0])   # bought, sold, top price
            if isbuy:
                a[0] += q_
                a[2] = max(a[2], pc_)
            else:
                a[1] += q_
        newflips = []
        for m_, (bq, sq, topc) in want.items():
            # any recorded buy makes this a market the earner put stock in;
            # the SIZE comes from the position below, never from this count
            if bq < 1:
                continue
            pos_ = MONITOR.positions.get(m_)
            if pos_ is None:
                continue                      # no reading: do not guess
            held = tr._num(pos_.get("netPosition")) or 0
            committed = sum(float(o.get("size") or 0) for o in MONITOR.orders
                            if o.get("market") == m_
                            and str(o.get("intent") or "").endswith("SELL_LONG"))
            queued = sum(j[2] for j in (_EARN.get("toflip") or []) if j[0] == m_)
            # Flips ALREADY RESTING count against what still needs flipping.
            # Without this, `outstanding` only fell when a flip actually SOLD,
            # so in a market where we hold a big position for other reasons the
            # position bound never bit and the same 60 shares were re-queued
            # every poll: 361 shares of ask piled up against 60 the earner had
            # bought, selling the owner's own inventory out from under them.
            # THE POSITION IS THE TRUTH, NOT THE LEDGER. The ledger only knows
            # fills it happened to see: it was introduced part-way through the
            # night and rebuilds from a rolling feed, so it read 60 shares in a
            # market where the earner had actually bought 364. Capping flips by
            # it pulled 301 shares of correct asks off stock we were still
            # holding. What we hold, less the inventory asks already standing
            # against it, is the honest figure — and because `committed`
            # includes those asks, this converges instead of re-queueing.
            need = int(min(held - committed - queued, EARN_FLIP_MAX_SHARES))
            if need >= 1:
                _EARN.setdefault("toflip", []).append([m_, topc, need, now])
                newflips.append((m_, topc, need))
    for m_, pc_, q_ in newflips:          # log outside the lock
        _earn_log(m_, "to flip", pc_ / 100.0, q_,
                  "queued to sell back — inventory, so no buying power used")
    # settle disappearances: real fill (in the fills feed) vs silent cancel
    for oid, (rec, ts_gone) in list(_EARN["pending"].items()):
        m, side, px, qty, ts = rec
        if oid in open_ids:      # the list flickered — the order is back
            _EARN["orders"][oid] = rec
            del _EARN["pending"][oid]
        elif _fill_confirmed(oid):
            del _EARN["pending"][oid]
            _earn_log(m, "filled", px / 100.0, qty,
                      f"taken at {px:.0f}c — ${px/100.0*qty:.2f} of stock bought "
                      "we did not want; standing off this market")
            # a fill is the outcome to avoid, so the cooldown is hours, not
            # minutes — never straight back in at a price that just got hit
            # cost, count and the flip all come from the fills feed above;
            # this branch only journals the disappearance and stands down
            _EARN["last"][m] = now + EARN_FILL_COOLDOWN - EARN_COOLDOWN
            # A fill on a price the model calls absurd is not an ordinary cost,
            # it is evidence the reasoning was wrong — somebody was happy to
            # sell us something we should not have been bidding for. Shut the
            # market down for the day and say so loudly.
            sv2 = _silver_fair(m)
            if sv2 is not None and px > sv2 + EARN_SILVER_MARGIN:
                _EARN["last"][m] = now + 86400
                _earn_log(m, "OFF-MODEL FILL", px / 100.0, qty,
                          f"filled at {px:.0f}¢ where the model says {sv2:.1f}¢ — "
                          "someone sold us junk; market closed for the day")
                notify("Off-model fill",
                       f"{m}: filled {qty} at {px:.0f}c, model fair {sv2:.1f}c",
                       "high")
        elif now - ts_gone > EARN_CONFIRM_WAIT:
            del _EARN["pending"][oid]
            # The exchange keeps silently cancelling in some markets. Re-placing
            # straight back into one is how 41 orders vanished overnight while
            # four names absorbed every attempt. Count it, and stand the market
            # down for longer each time rather than feeding it again.
            nv = _EARN.setdefault("vanished", {})
            nv[m] = int(nv.get(m, 0)) + 1
            hold = EARN_VANISH_COOLDOWN * min(nv[m], 6)
            _EARN["last"][m] = now + hold - EARN_COOLDOWN
            _earn_log(m, "vanished", px / 100.0, qty,
                      f"gone without a trade — exchange-side cancel "
                      f"({nv[m]}x here; standing off {hold / 3600:.1f}h)")
    # reconcile: fills and drift
    for oid, rec in list(_EARN["orders"].items()):
        m, side, px, qty, ts = rec
        if oid not in open_ids:
            del _EARN["orders"][oid]
            if oid in _EARN["cancelled"]:
                _EARN["cancelled"].discard(oid)
            else:
                # disappearance is a CLAIM, not a fill — park it until the
                # fills feed confirms or denies
                _EARN["pending"][oid] = (rec, now)
            continue
        # Withdrawal is by PERFORMANCE now, not price drift: the monitor
        # already scores every resting order (est_day). An order that keeps
        # earning stays put whatever the median does — "the earner is not
        # meant to sit; it's meant to earn." Withdraw only when its income
        # no longer justifies its worst case (payback beyond ~4 days), with
        # a 10-minute grace so fresh orders aren't judged before scoring.
        if now - ts < 600:
            continue
        o = next((x for x in MONITOR.orders if str(x.get("id")) == oid), None)
        est = float((o or {}).get("est_day") or 0)
        pk_, cur_ = _rate_trend(m)
        diluted = pk_ >= 1.0 and cur_ < 0.4 * pk_
        if est < 0.25 * (px / 100.0) * qty or diluted:
            try:
                requests.request(
                    "POST", tr.TRADE_API + f"/v1/order/{oid}/cancel",
                    headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST",
                                               f"/v1/order/{oid}/cancel"),
                             "Content-Type": "application/json"},
                    json={"marketSlug": m}, timeout=15)
                _EARN["cancelled"].add(oid)
                del _EARN["orders"][oid]
                _EARN["last"][m] = now + EARN_WITHDRAW_COOLDOWN - EARN_COOLDOWN
                _earn_log(m, "withdrawn", px / 100.0, qty,
                          (f"market fell ${pk_:.2f} to ${cur_:.2f}/day — diluted, "
                           "moving on for an hour") if diluted else
                          (f"earning ${est:.2f}/d — payback beyond 4 days; "
                           "moving on for an hour"))
            except Exception:  # noqa: BLE001
                pass
    # Settle flips. A flip that fills is the good outcome — the stock a fill
    # forced on us is gone and the cash is back — so it CREDITS the fill cost
    # that the earner card nets against its earnings. Without this the cost
    # only ever grows and the net line lies about how the day went.
    for foid, (fm, fpxc, fq, fts, *_c) in list((_EARN.get("flips") or {}).items()):
        if foid in open_ids:
            continue
        del _EARN["flips"][foid]
        if not _fill_confirmed(foid):
            _earn_log(fm, "flip vanished", fpxc / 100.0, fq,
                      "exchange-side cancel — still holding the stock")
            _EARN.setdefault("toflip", []).append([fm, fpxc - EARN_FLIP_TICKS, fq, now])
            continue
        # EVIDENCE, not just money. A flip that sells means a real buyer was
        # willing to pay that price, which is exactly what a sell scout goes
        # looking for — and this one cost nothing to run and was far bigger
        # than the prober's one-share probes, so it is better evidence than
        # anything the prober can buy (owner, 2026-08-16, asking for it).
        with MONITOR.lock:
            e_ = MONITOR.state.setdefault("probe", {}).setdefault(fm, {})
            e_["traded_at_ask"] = fpxc / 100.0
            e_["last_fill"] = {"side": "SELL", "px": fpxc / 100.0,
                               "ts": dt.datetime.now(ET).strftime("%m-%d %I:%M %p")}
        _probe_log(fm, "round trip", "SELL", fpxc / 100.0,
                   f"the earner's flip of {fq} sold here — a real buyer at this price")
        _earn_log(fm, "recovered", fpxc / 100.0, fq,
                  f"sold the {fq} back at {fpxc:.0f}¢ — position closed")
    # A flip that has rested a long time without a taker says fair value is
    # BELOW its price, the same thing the prober learns from a sell scout
    # ageing out — and this one is free and much larger. Recorded once per
    # market per price so a long-lived flip does not shout.
    for foid, (fm2, fpc2, fq2, fts2, *_c2) in list((_EARN.get("flips") or {}).items()):
        if now - fts2 < PROBE_TTL:
            continue
        with MONITOR.lock:
            e2 = MONITOR.state.setdefault("probe", {}).setdefault(fm2, {})
            prev = e2.get("rested_ask")
            if prev is None or fpc2 / 100.0 < prev - 1e-9:
                e2["rested_ask"] = fpc2 / 100.0
                fresh_ = True
            else:
                fresh_ = False
        if fresh_:
            _probe_log(fm2, "rested", "SELL", fpc2 / 100.0,
                       f"the earner's flip of {int(fq2)} held here with no buyer")

    # Pick up a repriced flip once the order list shows it.
    for job3 in list(_EARN.get("adopt") or []):
        am, apx, aq, acost, ats = job3[0], job3[1], job3[2], job3[3], job3[4]
        asince = job3[5] if len(job3) > 5 else ats
        if now - ats > 600:
            _EARN["adopt"].remove(job3)
            continue
        hit = next((str(o.get("id")) for o in MONITOR.orders
                    if o.get("market") == am
                    and str(o.get("intent") or "").endswith("SELL_LONG")
                    and abs(float(o.get("price") or 0) * 100 - apx) < 0.51
                    and abs(float(o.get("size") or 0) - aq) < 0.51
                    and str(o.get("id")) not in (_EARN.get("flips") or {})), None)
        if hit:
            _EARN["adopt"].remove(job3)
            _own_id("earn", hit)
            _EARN.setdefault("flips", {})[hit] = (
                am, float(apx), int(aq), now, acost, asince)

    # NEVER SIT OUTBID ON A FLIP. A flip exists to get the money back, and an
    # ask that somebody has undercut sells nothing and, once it falls out of
    # the scoring window, earns nothing either — the worst of both. So follow
    # the touch down, but only while the price is still fair: never below the
    # cost the fill left us with, so chasing can turn a flip into a smaller
    # gain but never into a loss (owner, 2026-08-16: "you don't want to sell
    # for peanuts, but the goal is to get money back").
    for foid, rec_ in list((_EARN.get("flips") or {}).items()):
        fm3, fpc3, fq3, fts3 = rec_[0], rec_[1], rec_[2], rec_[3]
        cost3 = rec_[4] if len(rec_) > 4 else fpc3 - EARN_FLIP_TICKS
        since3 = rec_[5] if len(rec_) > 5 else fts3
        if now - fts3 < 300 or foid not in open_ids:
            continue                      # let a fresh flip settle first
        ent3 = tr._BOOK_CACHE.get(fm3)
        if not ent3 or now - ent3[0] > 300:
            continue
        asks3 = ent3[1].get("asks") or []
        if not asks3:
            continue
        best3 = round(float(asks3[0][0]) * 100)
        # Held long enough that our cost has stopped being the right anchor?
        # Then the floor is the market: a tick above the best bid, the lowest
        # an ask can rest without crossing.
        bids3 = ent3[1].get("bids") or []
        if now - since3 >= EARN_FLIP_LOSS_AFTER and bids3:
            floor3_ = max(1.0, round(float(bids3[0][0]) * 100) + 1)
        else:
            floor3_ = cost3 + 1
        if best3 >= fpc3:
            # Not undercut — but is it just sitting there? Step half of it
            # down toward the floor so we find out where a buyer actually is
            # instead of waiting out a double that probably never comes.
            if now - fts3 >= EARN_FLIP_STEP_AFTER and fpc3 > floor3_ + 1 and fq3 >= 2:
                step_ = max(floor3_, round((fpc3 + floor3_) / 2))
                half_ = max(1, int(fq3) // 2)
                code_, res_ = do_reprice(foid, float(step_), quantity=half_)
                if code_ == 200 and res_.get("ok"):
                    del _EARN["flips"][foid]
                    _EARN.setdefault("adopt", []).append(
                        [fm3, float(step_), half_, cost3, now, since3])
                    _earn_log(fm3, "flip laddered", step_ / 100.0, half_,
                              f"no taker at {fpc3:.0f}¢ for 30m — {half_} moved to "
                              f"{step_:.0f}¢" +
                              (f", BELOW the {cost3:.0f}¢ it cost, to get the "
                               "money back" if step_ < cost3 else
                               f" (cost {cost3:.0f}¢)"))
            continue                      # we are at or better than the touch
        floor3 = floor3_                  # a flip must still make money
        if best3 < floor3:
            _earn_log(fm3, "flip held", fpc3 / 100.0, int(fq3),
                      f"undercut at {best3:.0f}¢, under our floor of "
                      f"{floor3_:.0f}¢ — holding for now")
            _EARN["flips"][foid] = (fm3, fpc3, fq3, now, cost3, since3)
            continue
        code, res = do_reprice(foid, float(best3), quantity=int(fq3))
        if code == 200 and res.get("ok"):
            # do_reprice places a replacement and cancels the original, but it
            # does not hand back the new id. Left there the repriced flip would
            # drop out of the registry: its earnings would stop being counted
            # and its sale would never be credited. Adopt it next poll by an
            # exact market/price/quantity match instead.
            del _EARN["flips"][foid]
            _EARN.setdefault("adopt", []).append(
                [fm3, float(best3), int(fq3), cost3, now, since3])
            _earn_log(fm3, "flip chased", best3 / 100.0, int(fq3),
                      f"undercut — moved {fpc3:.0f}¢ to {best3:.0f}¢, still above "
                      f"the {cost3:.0f}¢ it cost us")

    # Self-correct an over-sold market: if our inventory asks exceed what we
    # actually hold, pull the newest until they do not. Cancelling here only
    # ever REDUCES exposure, and leaves the oldest flip — the one nearest the
    # front of the queue — in place.
    for fm_ in {r[0] for r in (_EARN.get("flips") or {}).values()}:
        pos_ = MONITOR.positions.get(fm_)
        if pos_ is None:
            continue          # an absent reading is not a zero position
        net_ = tr._num(pos_.get("netPosition")) or 0
        # A flip may sell only what a fill forced on us, and only what we own.
        # The second bound alone was not enough: where the owner holds a large
        # position anyway, asks far beyond anything the earner bought looked
        # perfectly affordable, and were quietly liquidating that position.
        # Bounded by the POSITION only. Bounding by the ledger's idea of what
        # we bought was the mistake that pulled good asks off held stock.
        mine_ = [(o_, r_) for o_, r_ in (_EARN.get("flips") or {}).items() if r_[0] == fm_]
        excess = sum(r_[2] for _, r_ in mine_) - max(0.0, net_)
        if excess <= 0:
            continue
        for o_, r_ in sorted(mine_, key=lambda x: -x[1][3]):
            if excess <= 0:
                break
            try:
                requests.request(
                    "POST", tr.TRADE_API + f"/v1/order/{o_}/cancel",
                    headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST",
                                               f"/v1/order/{o_}/cancel"),
                             "Content-Type": "application/json"},
                    json={"marketSlug": fm_}, timeout=15)
                _EARN["flips"].pop(o_, None)
                excess -= r_[2]
                _earn_log(fm_, "flip pulled", r_[1] / 100.0, int(r_[2]),
                          f"selling {int(excess + r_[2])} more than the "
                          f"{int(max(0.0, net_))} we hold")
            except Exception:  # noqa: BLE001
                pass
    # Flip out anything that filled. Retried each poll until the position
    # snapshot catches up with the fill, then given up on so a stale entry
    # cannot place an order against stock we no longer hold.
    for job in list(_EARN.get("toflip") or []):
        fm, fpx_c, fqty, fts = job
        if now - fts > EARN_FLIP_RETRY:
            _EARN["toflip"].remove(job)
            _earn_log(fm, "flip missed", fpx_c / 100.0, fqty,
                      "position never showed the stock — left holding it")
            continue
        net = tr._num((MONITOR.positions.get(fm) or {}).get("netPosition")) or 0
        # Asks we ALREADY have resting against this stock. Without this the
        # same shares get sold twice: the pending-queue flipped 60 CT governor
        # at 12:59, the feed-driven queue flipped the same 60 again at 01:02,
        # and 144 shares of ask stood against 84 held. A flip beyond the
        # position is not a flip at all — it opens a short, which is the one
        # thing that DOES consume buying power.
        committed = sum(float(o.get("size") or 0) for o in MONITOR.orders
                        if o.get("market") == fm
                        and str(o.get("intent") or "").endswith("SELL_LONG"))
        fq = int(min(fqty, net - committed))
        if fq < 1:
            continue
        out = min(0.99, round((fpx_c + EARN_FLIP_TICKS) / 100.0, 2))
        ent_ = tr._BOOK_CACHE.get(fm)
        asks_ = (ent_[1].get("asks") or []) if ent_ else []
        if asks_:
            ba_ = float(asks_[0][0])
            # join the touch when it sits between our cost and our target:
            # earlier in the queue, and never below what we paid
            if (fpx_c + 1) / 100.0 <= ba_ < out:
                out = round(ba_, 2)
        try:
            r = requests.request(
                "POST", tr.TRADE_API + "/v1/orders",
                headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", "/v1/orders"),
                         "Content-Type": "application/json"},
                json={"marketSlug": fm, "intent": "ORDER_INTENT_SELL_LONG",
                      "type": "ORDER_TYPE_LIMIT",
                      "price": {"value": f"{out:.2f}", "currency": "USD"},
                      "quantity": fq,
                      "tif": "TIME_IN_FORCE_GOOD_TILL_CANCEL",
                      "participateDontInitiate": True},
                timeout=20)
            ok = r.status_code < 300
            oid2 = None
            if ok:
                try:
                    j = r.json()
                    o_ = j.get("order")
                    oid2 = (o_.get("id") if isinstance(o_, dict) else None) \
                           or j.get("id") or j.get("orderId")
                except Exception:  # noqa: BLE001
                    pass
            ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                            "market": fm, "side": "EARN flip", "from": fpx_c,
                            "to": round(out * 100, 1), "size": fq,
                            "status": r.status_code,
                            "response": " ".join(r.text.split())[:100], "verified": ok})
            del ACTIONS[:-20]
            if ok:
                if fq >= fqty:
                    _EARN["toflip"].remove(job)
                else:
                    job[2] = fqty - fq          # partial: flip the rest later
                if oid2:
                    _own_id("earn", str(oid2))
                    _EARN.setdefault("flips", {})[str(oid2)] = (
                        fm, round(out * 100), fq, now, float(fpx_c), now)
                _earn_log(fm, "flipped", out, fq,
                          f"selling back the {fq} bought at {fpx_c:.0f}¢ — "
                          "inventory, so no buying power used")
        except Exception:  # noqa: BLE001 — a flip never kills the poll
            pass
    # Graduate the proven, demote the faded. Runs before rotation so a market
    # that has just earned its place is never picked as one of the worst.
    est_pm = MONITOR.state.get("probe") or {}
    grad = _EARN.setdefault("grad", set())
    for oid, (m, side, px, qty, ts) in list(_EARN["orders"].items()):
        o = next((x for x in MONITOR.orders if str(x.get("id")) == oid), None)
        est = float((o or {}).get("est_day") or 0)
        cost = px / 100.0 * qty
        if oid in grad:
            # a graduate that stops paying goes back under the cap and takes
            # its chances with everything else. Two ways to stop paying: our
            # own order fading, or the whole market being diluted out from
            # under it — the second shows in the rate series first.
            pk, cur = _rate_trend(m)
            if est < EARN_GRAD_MIN_RATE / 2:
                grad.discard(oid)
                _earn_log(m, "demoted", px / 100.0, qty,
                          f"down to ${est:.2f}/day — back on the search budget")
            elif pk >= 1.0 and cur < 0.4 * pk:
                grad.discard(oid)
                _earn_log(m, "demoted", px / 100.0, qty,
                          f"market fell ${pk:.2f} to ${cur:.2f}/day — being "
                          "diluted, back on the search budget")
            continue
        if now - ts < EARN_GRAD_AGE or est < EARN_GRAD_MIN_RATE:
            continue
        if cost > 0 and est * EARN_GRAD_PAYBACK < cost:
            continue                      # cannot cover its own worst case
        if (est_pm.get(m) or {}).get("fills"):
            continue                      # this market has taken money off us
        if _on_book(m, "BUY", px / 100.0, qty, ts) is False:
            continue                      # not visibly resting, so not proven
        if _earn_graduated_usd() + cost > EARN_GRAD_MAX_USD:
            continue
        grad.add(oid)
        _earn_log(m, "graduated", px / 100.0, qty,
                  f"earning ${est:.2f}/day for {int((now - ts) / 60)}m — "
                  "off the search budget, still earning")
    grad &= set(_EARN["orders"])          # forget orders that are gone

    # Rotation: at capacity, abandon the worst few so the search can continue.
    # Skips anything inside the scoring grace — a fresh order has no rate yet
    # and would rank bottom purely for being new.
    if (now - float(_EARN.get("rot_ts") or 0) >= EARN_ROTATE_EVERY
            and _earn_outstanding_usd() >= EARN_FULL_FRAC * EARN_TOTAL_USD):
        _EARN["rot_ts"] = now
        ranked = []
        for oid, (m, side, px, qty, ts) in _EARN["orders"].items():
            if now - ts < 600 or oid in (_EARN.get("grad") or set()):
                continue
            o = next((x for x in MONITOR.orders if str(x.get("id")) == oid), None)
            est = float((o or {}).get("est_day") or 0)
            usd = px / 100.0 * qty
            ranked.append((est / usd if usd > 0 else 0.0, oid, m, px, qty, est))
        ranked.sort(key=lambda r: r[0])
        for yld, oid, m, px, qty, est in ranked[:EARN_ROTATE_N]:
            try:
                requests.request(
                    "POST", tr.TRADE_API + f"/v1/order/{oid}/cancel",
                    headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST",
                                               f"/v1/order/{oid}/cancel"),
                             "Content-Type": "application/json"},
                    json={"marketSlug": m}, timeout=15)
                _EARN["cancelled"].add(oid)
                del _EARN["orders"][oid]
                _EARN["last"][m] = now + EARN_WITHDRAW_COOLDOWN - EARN_COOLDOWN
                _earn_log(m, "rotated", px / 100.0, qty,
                          f"worst of the book at ${est:.2f}/d on ${px/100.0*qty:.2f} "
                          f"({yld*100:.1f}%/day) — freeing the capital to look elsewhere")
            except Exception:  # noqa: BLE001 — rotation never kills the poll
                pass
    # place where the model is confident and we hold nothing yet
    placed = 0
    have = {rec[0] for rec in _EARN["orders"].values()}
    # Work the pool LEAST-RECENTLY-TRIED FIRST. Sorting by name meant the
    # scan restarted from the same end of the alphabet every poll, so the
    # 2028 nomination markets were reconsidered forever and the race families
    # further down were never reached at all: 100 placements landed in 5
    # markets out of a pool of 76. Ordering by last attempt makes the earner
    # sweep the whole pool and move on (owner, 2026-08-16: "the earner seems
    # stuck on these markets, just have it move on to somewhere else").
    cands = sorted({l.get("m") for l in (MONITOR.state.get("probe_log") or [])
                    if l.get("m")},
                   key=lambda m_: (_EARN["last"].get(m_, 0.0), m_))
    for m in cands:
        if placed >= EARN_MAX_PER_POLL:
            break
        if m in have or now - _EARN["last"].get(m, 0.0) < EARN_COOLDOWN:
            continue
        if _earn_outstanding_usd() >= EARN_TOTAL_USD:
            break
        b = _bayes_fair(m)
        # minimum knowledge: anything real — one trade, two rested scouts,
        # or three observations. Size, not certainty, carries the risk.
        if not (b and b.get("med")
                and (b.get("fills", 0) >= 1 or b.get("rested", 0) >= 2
                     or b.get("n", 0) >= 3)):
            continue
        pr = (tr._PROG_CACHE.get("progs") or {}).get(m) or {}
        target = float(pr.get("target") or 0)
        per = (float(pr.get("pool") or 0)
               / max(int(pr.get("pool_n") or pr.get("event_n") or 1), 1) / 2)
        df = float(pr.get("df") or 0.2)
        ent = tr._BOOK_CACHE.get(m)
        if not target or per <= 0 or not ent or now - ent[0] > 300:
            continue
        real_bids = [(round(p_ * 100), q_) for p_, q_ in ent[1].get("bids") or []
                     if q_ >= PROBE_REAL_MIN]
        # A SIDE BELOW TARGET SIZE PAYS NOBODY, so an order resting on one
        # earns exactly zero however well placed it is. The scoring walk below
        # fills its window up to `target` and never asked whether the side
        # actually HAS that much, so it produced a confident positive estimate
        # for sides paying nothing: 79 small bids were sitting on sides like
        # "403 of 2,000" and "10,582 of 20,000" when the owner asked whether
        # this was being checked. It was not.
        #
        # Counted over the WHOLE book, not the de-baited levels — the exchange
        # counts every resting contract towards Target Size, including the
        # one- and two-share bait the rest of this function ignores.
        side_total = sum(q_ for _, q_ in (ent[1].get("bids") or []))
        # candidate prices: from the real touch up through the band and two
        # ticks of stretch, never above the penny ceiling where a total
        # loss stops being trivial
        base = real_bids[0][0] if real_bids else max(1, b["lo"])
        top = min(b["hi"] + 2, EARN_PX_MAX_C)
        # Model-backed extension past the penny ceiling: never above the band's
        # 10th percentile, and never above the hard safety cap.
        if b["lo"] > top:
            top = min(b["lo"], EARN_SAFE_MAX_C)
        if top < base:
            continue
        # queued size at or better than each candidate price — the wall we
        # would be resting behind
        def _queue(pc_: int) -> float:
            return sum(q_ for p_, q_ in real_bids if p_ >= pc_)
        # WHERE A REAL FORECAST EXISTS, IT CAPS THE PRICE. The earner bought NM
        # Senate Rep at 10c on a day the Silver model had it at 0.62% — 16x
        # fair, an expected loss of $7.88 on an $8.40 purchase — because the
        # fair-value gate only applied ABOVE the penny ceiling. Below it the
        # only question asked was whether the reward income beat the worst
        # case, and in a reward-farmed book it always does.
        #
        # The Bayesian band is no defence here: it read ~10c because a 9c bid
        # of ours had rested untouched, and a bid resting in these markets
        # means people are farming rewards, not that anyone values the
        # contract at 9c. The band measures the crowd; Silver measures the
        # race. Where Silver has an opinion it wins, with a few cents of
        # margin so reward income can still justify a small premium.
        sv = _silver_fair(m)
        sv_cap = int(sv + EARN_SILVER_MARGIN) if sv is not None else None
        best = None
        for pc in range(base, top + 1):
            if not _bid_allowed(m, pc):
                continue
            if sv_cap is not None and pc > sv_cap:
                continue
            # past the penny ceiling both knowledge conditions must hold
            if pc > EARN_PX_MAX_C and (pc > b["lo"] or _queue(pc) < EARN_QUEUE_MIN):
                continue
            # confidence tier sets the exposure: proven / stretch / speculative
            if pc <= b["med"]:
                cap = EARN_MAX_USD
                tier = "proven"
            elif pc <= b["hi"]:
                cap = EARN_MAX_USD * 0.4
                tier = "stretch"
            else:
                cap = EARN_MAX_USD * 0.15
                tier = "speculative"
            # SIZE FALLS AWAY FROM THE MODEL. Even inside the cap, paying
            # above a forecast is paying a premium, and the premium should buy
            # a smaller position, not the same one. At the model's own number
            # the full tier is available; at the cap it is a token.
            if sv is not None and pc > sv:
                over = (pc - sv) / max(1.0, EARN_SILVER_MARGIN)
                cap = cap * max(0.15, 1.0 - 0.85 * min(1.0, over))
            q = max(1, min(EARN_MAX_SHARES, int(cap * 100 / pc)))
            # score with us resting at pc: merge, walk the window from the
            # best price, sum discounted takes
            lv = sorted(real_bids + [(pc, float(q))], key=lambda x: -x[0])
            anchor = lv[0][0]
            den = cum = ours_sc = 0.0
            for p_, q_ in lv:
                take = min(q_, max(0.0, target - cum))
                if take <= 0:
                    break
                w = df ** (anchor - p_)
                den += take * w
                if p_ == pc:
                    ours_sc += min(take, float(q)) * w
                cum += q_
            # our own size counts towards Target Size too, so a side just
            # short of it can be tipped over by the order we are about to
            # place — but only just short, and this rarely applies
            est = (per * ours_sc / den) if (den and side_total + q >= target) else 0.0
            # the deal test: income must dwarf the worst case — total-loss
            # payback within two days
            if est >= 0.5 * (pc / 100.0) * q:
                if best is None or est > best[0]:
                    best = (est, pc, q, tier)
        if best is None:
            continue
        est, tgt, qty, tier = best
        px = round(tgt / 100.0, 2)
        if px * qty + _earn_outstanding_usd() > EARN_TOTAL_USD:
            continue
        try:
            r = requests.request(
                "POST", tr.TRADE_API + "/v1/orders",
                headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", "/v1/orders"),
                         "Content-Type": "application/json"},
                json={"marketSlug": m, "intent": "ORDER_INTENT_BUY_LONG",
                      "type": "ORDER_TYPE_LIMIT",
                      "price": {"value": f"{px:.2f}", "currency": "USD"},
                      "quantity": qty,
                      "tif": "TIME_IN_FORCE_GOOD_TILL_CANCEL",
                      "participateDontInitiate": True},
                timeout=20)
            ok = r.status_code < 300
            oid = None
            if ok:
                try:
                    j = r.json()
                    o = j.get("order")
                    oid = (o.get("id") if isinstance(o, dict) else None) \
                          or j.get("id") or j.get("orderId")
                except Exception:  # noqa: BLE001
                    pass
            ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                            "market": m, "side": "EARN bid", "from": "—",
                            "to": tgt, "size": qty, "status": r.status_code,
                            "response": " ".join(r.text.split())[:100],
                            "verified": ok})
            del ACTIONS[:-20]
            # Mark the market TRIED whatever the outcome. This was missing, so
            # `last` stayed 0 for any market that never filled and the cooldown
            # test below could never bite — the same names were re-entered on
            # every poll. It also drives the least-recently-tried ordering.
            _EARN["last"][m] = now
            if ok and oid:
                _EARN["orders"][str(oid)] = (m, "BUY", tgt, qty, now)
                _own_id("earn", str(oid))
                _earn_log(m, "placed", px, qty,
                          f"{tier}: est ${est:.2f}/d vs ${px*qty:.2f} worst case "
                          f"(band {b['lo']}–{b['hi']}¢, {b['fills']}t/{b.get('rested',0)}r)")
                placed += 1
        except Exception:  # noqa: BLE001 — the earner must never kill the poll
            continue
    # mirror the registries so a rebuild can re-adopt (see top of function).
    # The flip queue and the resting flips belong here too: a container
    # replacement between a fill and its flip would otherwise leave us holding
    # stock nobody remembers buying, and an untracked ask resting against it.
    with MONITOR.lock:
        MONITOR.state["earn_orders_reg"] = {k: list(v) for k, v in _EARN["orders"].items()}
        MONITOR.state["earn_flips_reg"] = {k: list(v) for k, v in (_EARN.get("flips") or {}).items()}
        MONITOR.state["earn_toflip"] = [list(j) for j in (_EARN.get("toflip") or [])]
        MONITOR.state["earn_grad"] = sorted(_EARN.get("grad") or set())
        MONITOR.state["earn_adopt"] = [list(j) for j in (_EARN.get("adopt") or [])]


# --- slate health watch (in-process; replaced the slate_watch.yml cron) ----
# Moved out of GitHub Actions 2026-08-15: the 30-minute cron was burning
# ~120 Actions minutes a day against a 2,000/month plan, and the monitor
# already holds every book, target, and order in memory — the same check
# here costs nothing and can actually reach ntfy. Alerts when a slate
# side's TOTAL size drops under Target Size (that side pays nobody) or the
# open-order count collapses (the mass-cancel signature). OUR size alone
# below target is the designed state since the chunk cull — not alerted.
WATCH_PREFIXES = ("enwc-uspres-nom-rep-2028-", "enwc-uspres-nom-dem-2028-",
                  "ewc-usp-2028-11-07-", "ewc-usp-party-2028-11-07-")
WATCH_INTERVAL = float(os.environ.get("WATCH_INTERVAL", "600"))
WATCH_REALERT = float(os.environ.get("WATCH_REALERT", "21600"))  # per finding
_WATCH: dict = {"last_run": 0.0, "alerted": {}, "prev_orders": 0}


def slate_health_check() -> None:
    now = time.time()
    if now - _WATCH["last_run"] < WATCH_INTERVAL:
        return
    _WATCH["last_run"] = now
    progs = tr._PROG_CACHE.get("progs") or {}
    ours: dict = {}
    for o in MONITOR.orders:
        m = o.get("market") or ""
        if m.startswith(WATCH_PREFIXES):
            k = (m, o.get("side"))
            ours[k] = ours.get(k, 0.0) + float(o.get("size") or 0)
    problems = []
    for m, ent in list(tr._BOOK_CACHE.items()):
        if not m.startswith(WATCH_PREFIXES):
            continue
        if now - ent[0] > 900:      # stale book — never alarm on old data
            continue
        target = float((progs.get(m) or {}).get("target") or 0)
        if not target:
            continue
        for side, key in (("BUY", "bids"), ("SELL", "asks")):
            # the book lags our own placements; take the larger read
            tot = max(sum(q for _, q in (ent[1] or {}).get(key) or []),
                      ours.get((m, side), 0.0))
            if tot < target:
                problems.append((f"{m}|{side}",
                                 f"{m.rsplit('-', 1)[-1]} {side} {tot:,.0f}/{target:,.0f}"))
    n = len(MONITOR.orders)
    if _WATCH["prev_orders"] and n < _WATCH["prev_orders"] * 0.85:
        problems.append(("open-orders",
                         f"open orders fell {_WATCH['prev_orders']:,} -> {n:,}"))
    _WATCH["prev_orders"] = n
    fresh = [(k, txt) for k, txt in problems
             if now - _WATCH["alerted"].get(k, 0.0) > WATCH_REALERT]
    if fresh:
        for k, _ in fresh:
            _WATCH["alerted"][k] = now
        body = " | ".join(txt for _, txt in fresh[:6])
        if len(fresh) > 6:
            body += f" (+{len(fresh) - 6} more)"
        with MONITOR.lock:
            MONITOR.pending_alerts.append(
                ("Slate watch: sides not paying", body[:900], "high"))


def _race_prefix(slug: str) -> str:
    """Sibling-group key: seat ladders group by their ladder prefix, everything
    else by the slug minus its last token (the candidate/outcome)."""
    sp = _seat_split(slug)
    return sp[0] if sp else slug.rsplit("-", 1)[0]


def _race_risk(positions: dict, known: list[str]) -> list[dict]:
    """Worst/best case per RACE (one outcome resolves YES) across your
    positions, longs AND shorts. A short (No) pays its size in every
    scenario EXCEPT its own outcome winning. 'Locked' = even the worst
    scenario beats total cost — profit no matter who wins (negative risk)."""
    known_by_prefix: dict[str, int] = {}
    known_labels: dict[str, list[str]] = {}
    for s in known:
        known_by_prefix[_race_prefix(s)] = known_by_prefix.get(_race_prefix(s), 0) + 1
        sp = _seat_split(s)
        if sp:
            known_labels.setdefault(sp[0], []).append(sp[2])
    groups: dict[str, list] = {}
    for slug, p in positions.items():
        net = tr._num(p.get("netPosition"))
        if abs(net) < 1:
            continue
        groups.setdefault(_race_prefix(slug), []).append(
            (slug, net, tr._num(p.get("cost"))))
    races = []
    for prefix, held in groups.items():
        if len(held) < 2:
            continue  # negative risk takes positions across several outcomes
        total = max(known_by_prefix.get(prefix, 0), len(held))
        cost = sum(c for _, _, c in held)

        # THRESHOLD ladders (every rung ≥N or every rung ≤N — e.g. House
        # gte180/gte195/...): several rungs resolve YES together, so the
        # scenarios are the RANGES of the underlying count between thresholds,
        # not one-winner outcomes.
        fam_labels = known_labels.get(prefix, [])
        held_sp = {s: _seat_split(s) for s, _, _ in held}
        all_labels = fam_labels + [sp[2] for sp in held_sp.values() if sp]
        for sign in ("≥", "≤"):
            if (all_labels and all(sp is not None for sp in held_sp.values())
                    and all(lbl.startswith(sign) for lbl in all_labels)):
                thr = sorted({int(lbl[1:]) for lbl in all_labels})
                reps = [thr[0] - 1] + thr  # one representative count per range
                scenarios = []
                for idx, rep in enumerate(reps):
                    label = ("<" + str(thr[0]) if idx == 0 else
                             "≥" + str(thr[-1]) if idx == len(reps) - 1 else
                             f"{thr[idx - 1]}–{thr[idx] - 1}")
                    pay = 0.0
                    for s, n, _ in held:
                        t = int(held_sp[s][2][1:])
                        yes = rep >= t if sign == "≥" else rep <= t
                        pay += n if (yes and n > 0) else (-n if (not yes and n < 0) else 0.0)
                    scenarios.append({"outcome": label, "held": 0,
                                      "pl": round(pay - cost, 2)})
                pls = [sc["pl"] for sc in scenarios]
                races.append({
                    "race": prefix, "held": len(held), "outcomes": len(thr),
                    "cost": round(cost, 2),
                    "worst": min(pls), "best": max(pls),
                    "locked": min(pls) >= 0,
                    "scenarios": scenarios, "other_pl": None,
                    "rows": [{"market": s, "net": int(n), "cost": round(c, 2)}
                             for s, n, c in sorted(held)],
                })
                break
        else:
            pass  # not a threshold ladder — fall through to one-winner math
        if races and races[-1]["race"] == prefix:
            continue
        shorts_pay = sum(-n for _, n, _ in held if n < 0)  # all Nos pay...
        scen = []
        for _, n, _ in held:  # ...minus the shorted outcome when IT wins
            scen.append(shorts_pay + (n if n > 0 else n))  # long adds, short deducts its own
        covers_all = len(held) >= total
        if not covers_all:
            scen.append(shorts_pay)  # an unheld outcome wins: longs 0, all Nos pay
        worst_pay, best_pay = min(scen), max(scen)

        def _ord(item):  # seat ladders in seat order, else by name
            sp = _seat_split(item[0])
            return (0, sp[1]) if sp else (1, item[0])

        scenarios = []
        for s, n, _ in sorted(held, key=_ord):
            tail = s[len(prefix) + 1:] if s.startswith(prefix + "-") else s
            sp = _seat_split(s)
            scenarios.append({"outcome": sp[2] if sp else tail, "held": int(n),
                              "pl": round(shorts_pay + n - cost, 2)})
        races.append({
            "race": prefix, "held": len(held), "outcomes": total,
            "cost": round(cost, 2),
            "worst": round(worst_pay - cost, 2),
            "best": round(best_pay - cost, 2),
            "locked": worst_pay - cost >= 0,
            "scenarios": scenarios,
            "other_pl": None if covers_all else round(shorts_pay - cost, 2),
            "rows": [{"market": s, "net": int(n), "cost": round(c, 2)}
                     for s, n, c in sorted(held)],
        })
    races.sort(key=lambda r: r["worst"])
    return races


def positions_overview() -> dict:
    """Every long position with its take-profit state. Target = one tick
    inside the best ask that ISN'T ours: 'good' means the whole position is
    covered by a resting sell that is the best ask; 'fix' means attention."""
    with MONITOR.lock:
        positions = dict(MONITOR.positions)
        orders = list(MONITOR.orders)
    rows = []
    fetched = 0
    for slug, p in sorted(positions.items()):
        net = tr._num(p.get("netPosition"))
        if abs(net) < 1:
            continue
        mag = abs(net)
        short = net < 0
        cost = tr._num(p.get("cost"))
        if short:  # exit = BUY BACK: close orders carry the SELL_SHORT intent
            mine = [o for o in orders
                    if o.get("market") == slug and o.get("side") == "BUY"
                    and "SELL_SHORT" in str(o.get("intent") or "") and o.get("price")]
        else:
            mine = [o for o in orders
                    if o.get("market") == slug and o.get("side") == "SELL" and o.get("price")]
        book = None
        cached = tr._BOOK_CACHE.get(slug)
        if cached and time.time() - cached[0] < 600:
            book = cached[1]
        elif fetched < 15:  # bounded burst — the rest resolve on the next open
            try:
                book = tr._fetch_book(slug)
                fetched += 1
                time.sleep(0.1)
            except Exception:  # noqa: BLE001
                book = None
        row = {"market": slug, "net": int(net), "short": short,
               "avg_cents": round(cost / mag * 100, 2) if mag else None,
               "sells": [{"id": o.get("id"), "price_cents": round(o["price"] * 100, 2),
                          "size": o.get("size")} for o in mine]}
        if book is not None:
            # What a TAKER exit would fill against right now: the best level
            # on the opposite side that isn't our own resting size.
            hit_key = "asks" if short else "bids"
            my_hit = [o for o in orders
                      if o.get("market") == slug and o.get("price")
                      and o.get("side") == ("SELL" if short else "BUY")]
            for px, q in book.get(hit_key) or []:
                q -= sum(o["size"] for o in my_hit if abs(px - o["price"]) < 1e-9)
                if q > 1e-9:
                    row["hit_cents"] = round(px * 100, 2)
                    row["hit_size"] = int(q)
                    break
        if book is None:
            row["status"] = "unknown"
        else:
            tick = book.get("tick") or 0.01
            own_key = "bids" if short else "asks"
            others = []
            for px, q in book.get(own_key) or []:
                q -= sum(o["size"] for o in mine if abs(px - o["price"]) < 1e-9)
                if q > 1e-9:
                    others.append((px, q))
            covered = sum(o["size"] for o in mine)
            if short:
                # stand one tick ABOVE the best bid that isn't ours
                asks_b = book.get("asks") or []
                ba = asks_b[0][0] if asks_b else None
                target = round((others[0][0] + tick) if others else
                               ((ba - tick) if ba is not None else 0.01), 4)
                target = min(max(target, tick), 0.999)
                row["target_cents"] = round(target * 100, 2)
                best_my = max((o["price"] for o in mine), default=None)
                good = (best_my is not None
                        and covered >= min(mag, 20000) - 1e-9
                        and (not others or best_my >= others[0][0] + 1e-9))
                blocked = (others and ba is not None and target >= ba - 1e-9)
            else:
                target = round((others[0][0] - tick) if others else 0.99, 4)
                target = min(max(target, tick), 0.999)
                row["target_cents"] = round(target * 100, 2)
                best_my = min((o["price"] for o in mine), default=None)
                bids_b = book.get("bids") or []
                bb = bids_b[0][0] if bids_b else None
                good = (best_my is not None
                        and covered >= min(mag, 20000) - 1e-9
                        and (not others or best_my <= others[0][0] - 1e-9))
                blocked = (others and bb is not None and target <= bb + 1e-9)
            if good:
                row["status"] = "good"
            elif blocked:
                # the spread leaves no room to stand inside — wait for it to widen
                row["status"] = "wait"
            else:
                row["status"] = "fix"
        rows.append(row)
    rows.sort(key=lambda r: ({"fix": 0, "unknown": 1, "wait": 2, "good": 3}[r["status"]],
                             r["market"]))
    with MONITOR.lock:
        known = list((MONITOR.state.get("known_mkts") or {}).get("politics") or [])
    return {"rows": rows, "races": _race_risk(positions, known)}


def _seat_token(tok: str) -> tuple[float, str] | None:
    """(sort key, label) for a seat-count slug tail: '47', 'lte45', 'gte52',
    '100-105m'. None if the tail isn't a seat count."""
    t = tok[:-1] if tok.endswith("m") else tok
    if t.isdigit():
        return float(t), t
    if t.startswith("lte") and t[3:].isdigit():
        return int(t[3:]) - 0.5, "≤" + t[3:]
    if t.startswith("gte") and t[3:].isdigit():
        return int(t[3:]) + 0.5, "≥" + t[3:]
    a, _, b = t.partition("-")
    if a.isdigit() and b.isdigit() and int(a) < int(b):
        return float(a), a + "–" + b
    return None


def _seat_split(slug: str) -> tuple[str, float, str] | None:
    """(family prefix, sort key, label) when the slug ends in a seat count."""
    p2 = slug.rsplit("-", 2)
    if len(p2) == 3 and p2[2].endswith("m"):  # ranges like ...-100-105m
        st = _seat_token(p2[1] + "-" + p2[2])
        if st:
            return p2[0], st[0], st[1]
    p1 = slug.rsplit("-", 1)
    if len(p1) == 2:
        st = _seat_token(p1[1])
        if st:
            return p1[0], st[0], st[1]
    return None


def _seat_family_title(prefix: str) -> str:
    low = prefix.lower()
    if "senate" in low or "usse" in low:
        base = "Senate seats"
    elif "hrep" in low or "house" in low:
        base = "House seats"
    else:
        base = prefix
    for party in ("gop", "rep", "dem"):
        if f"-{party}" in low:
            return f"{base} ({party.upper()})"
    return base


def seats_overview() -> dict:
    """The seat-count ladders (House / Senate), each ordered by increasing
    seats, with position, resting orders (best-price flagged) and spread."""
    with MONITOR.lock:
        known = list((MONITOR.state.get("known_mkts") or {}).get("politics") or [])
        orders = list(MONITOR.orders)
        positions = dict(MONITOR.positions)
    all_slugs = set(known) | {o.get("market") for o in orders if o.get("market")} | set(positions)
    fams: dict[str, list] = {}
    for s in sorted(all_slugs):
        if not s or s.startswith(("tec-", "aec-")):
            continue
        sp = _seat_split(s)
        if sp:
            fams.setdefault(sp[0], []).append((sp[1], sp[2], s))
    out = []
    fetched = 0
    for prefix, members in sorted(fams.items()):
        if len(members) < 3:
            continue  # a real ladder has several rungs
        rows = []
        for key, label, slug in sorted(members):
            p = positions.get(slug) or {}
            net = tr._num(p.get("netPosition"))
            cost = tr._num(p.get("cost"))
            mine = [o for o in orders if o.get("market") == slug and o.get("price")]
            book = None
            cached = tr._BOOK_CACHE.get(slug)
            if cached and time.time() - cached[0] < 600:
                book = cached[1]
            elif fetched < 15:
                try:
                    book = tr._fetch_book(slug)
                    fetched += 1
                    time.sleep(0.1)
                except Exception:  # noqa: BLE001
                    book = None
            bb = ba = None
            tick = 0.01
            bid_total = ask_total = None
            if book:
                tick = book.get("tick") or 0.01
                bids_, asks_ = book.get("bids") or [], book.get("asks") or []
                bb = bids_[0][0] if bids_ else None
                ba = asks_[0][0] if asks_ else None
                bid_total = sum(q for _, q in bids_)
                ask_total = sum(q for _, q in asks_)

            def _deep(o) -> bool:  # the floor bid / ceiling ask qualifiers
                return bool((o["side"] == "BUY" and o["price"] <= tick + 1e-9)
                            or (o["side"] == "SELL" and o["price"] >= 1 - tick - 1e-9))

            # A side pays NOBODY until it holds Target Size — the qualify
            # button fills the gap with the cheapest possible order.
            prog_s = (tr._PROG_CACHE.get("progs") or {}).get(slug) or {}
            target_s = int(prog_s.get("target") or 0)
            need_bid = need_ask = None
            if book and target_s:
                gap_b = max(0, target_s - int(bid_total or 0))
                gap_a = max(0, target_s - int(ask_total or 0))
                if gap_b:
                    need_bid = {"price_cents": round(tick * 100, 1),
                                "size": min(gap_b, 20000),
                                "capital": round(tick * min(gap_b, 20000), 2)}
                if gap_a:
                    need_ask = {"price_cents": round((1 - tick) * 100, 1),
                                "size": min(gap_a, 20000),
                                "capital": round(tick * min(gap_a, 20000), 2)}
            rows.append({
                "label": label, "market": slug,
                "net": int(net) if net else 0,
                "avg_cents": round(cost / abs(net) * 100, 1) if net else None,
                "tick_cents": round(tick * 100, 1),
                "target": target_s or None,
                "bid_total": int(bid_total) if bid_total is not None else None,
                "ask_total": int(ask_total) if ask_total is not None else None,
                "need_bid": need_bid, "need_ask": need_ask,
                "has_deep_bid": any(_deep(o) and o["side"] == "BUY" for o in mine),
                "has_deep_ask": any(_deep(o) and o["side"] == "SELL" for o in mine),
                "orders": [{"side": o["side"],
                            "price_cents": round(o["price"] * 100, 1),
                            "size": o.get("size"),
                            "deep": _deep(o),
                            "best": bool(
                                (o["side"] == "BUY" and bb is not None
                                 and o["price"] >= bb - 1e-9)
                                or (o["side"] == "SELL" and ba is not None
                                    and o["price"] <= ba + 1e-9))}
                           for o in mine],
                "best_bid_cents": round(bb * 100, 1) if bb is not None else None,
                "best_ask_cents": round(ba * 100, 1) if ba is not None else None,
                "spread_cents": (round((ba - bb) * 100, 1)
                                 if bb is not None and ba is not None else None),
            })
        out.append({"title": _seat_family_title(prefix), "prefix": prefix, "rows": rows})
    out.sort(key=lambda f: f["title"])
    return {"families": out}


def _slug_known(slug: str) -> bool:
    """Only operate on markets we can see: currently quoted, in the tracked
    politics/golf universe, or on a scan plan — never a free-typed slug."""
    if any(o.get("market") == slug for o in MONITOR.orders):
        return True
    with MONITOR.lock:
        known = dict(MONITOR.state.get("known_mkts") or {})
    if slug in (known.get("politics") or []):
        return True
    if any(slug.startswith(t + "-") for t in known.get("golf") or []):
        return True
    for which in ("politics", "golf"):
        try:
            plan = fetch_plan(which)
            if any(r.get("market") == slug for r in plan.get("results") or []):
                return True
        except Exception:  # noqa: BLE001 — plan cache empty is fine
            pass
    return False


# A side pays NOBODY until it holds Target Size in resting contracts — every
# trader's size counts, not just ours. These bounds apply to the qualify
# button on the market sheet, which closes that gap on demand.
#
# It is a button, not a loop: it acts once, when the owner taps it, and
# places nothing on its own. The keeper loop has a branch that does the same
# thing automatically, but turning the keeper on also turns on its second
# branch (40-share orders near the touch), which is why this exists
# separately.
# Buying power is a per-side, per-book ceiling — resting orders do not draw
# it down, only fills do, and the same balance backs every market at once.
# So this caps what one side of one book can take, not a budget shared across
# markets: qualifying market A leaves market B just as fundable.
QUALIFY_MAX_USD = float(os.environ.get("QUALIFY_MAX_USD", "250"))
QUALIFY_MAX_ORDERS = int(os.environ.get("QUALIFY_MAX_ORDERS", "60"))
QUALIFY_RESERVE_USD = float(os.environ.get("QUALIFY_RESERVE_USD", "5"))
QUALIFY_BID_MAX = int(os.environ.get("QUALIFY_BID_MAX", "10000"))
# Below this, an order is not worth its own slot in the book. A balance that
# can only carry a handful of shares per order would otherwise dribble out
# forty near-empty orders and still leave the side short.
QUALIFY_MIN_CHUNK = int(os.environ.get("QUALIFY_MIN_CHUNK", "25"))


def _qual_per_order(side: str, price: float, bp: float) -> int:
    """How many shares ONE order can actually carry, at this price, with this
    buying power.

    The two sides are limited differently, and the ask side is the surprising
    one: opening a short is capped at one share per DOLLAR of buying power,
    not by the 1c per share it ties up while resting. A 2,000-share ask at
    99c came back resting 273.04 — a fractional share count, because it is a
    balance, not a size limit. Asking for more does not fail; it silently
    rests short, which is why a gap has to be split into buying-power-sized
    orders rather than sent as one.

    A bid has no such limit — the whole gap goes in a single order, up to the
    exchange's per-order ceiling. A 2,000-share bid at 1c rested in full.
    """
    if bp <= 0 or price <= 0:
        return 0
    if side == "SELL":
        return int(bp)                                  # one share per dollar
    return QUALIFY_BID_MAX                              # bids go in one order


def _qual_view(slug: str, book: dict) -> dict:
    """Target Size against what is actually resting on each side, plus the
    cheapest way to close any gap: the floor bid (one tick) or the ceiling
    ask (one tick off the top), where a contract ties up the least capital —
    a bid locks price x size, an ask locks (1 - price) x size."""
    prog = (tr._PROG_CACHE.get("progs") or {}).get(slug) or {}
    target = int(prog.get("target") or 0)
    tick = float(book.get("tick") or 0.01)
    bid_total = int(sum(q for _, q in (book.get("bids") or [])))
    ask_total = int(sum(q for _, q in (book.get("asks") or [])))
    out = {"target": target or None, "pool": prog.get("pool"),
           "bid_total": bid_total, "ask_total": ask_total,
           "floor_c": round(tick * 100, 1), "ceil_c": round((1 - tick) * 100, 1),
           "need_bid": 0, "need_ask": 0, "cost_bid": 0.0, "cost_ask": 0.0}
    if target:
        out["need_bid"] = max(0, target - bid_total)
        out["need_ask"] = max(0, target - ask_total)
        out["cost_bid"] = round(out["need_bid"] * tick, 2)
        out["cost_ask"] = round(out["need_ask"] * tick, 2)
    return out


def do_qualify(slug: str, side: str) -> tuple[int, dict]:
    """Bring ONE side up to Target Size with the cheapest post-only orders.

    The gap is recomputed here from a fresh book — the client sends only the
    market and the side, never a size or a price, so a stale sheet can never
    place more than the book currently needs. Bounded by a dollar cap per
    tap, an order count per tap, and live buying power; an ask placement is
    capped near 273 by the exchange, so a wide gap closes over several taps
    and the reply says how much is left.
    """
    if not _slug_known(slug):
        return 400, {"ok": False, "error": "unknown market"}
    if side not in ("BUY", "SELL"):
        return 400, {"ok": False, "error": "side must be BUY or SELL"}
    try:
        book = tr._fetch_book(slug)
    except Exception as e:  # noqa: BLE001
        return 502, {"ok": False, "error": f"book unavailable: {type(e).__name__}"}
    q = _qual_view(slug, book)
    name = "bid" if side == "BUY" else "ask"
    if not q["target"]:
        return 400, {"ok": False,
                     "error": "no active reward program here — nothing to qualify"}
    need = q["need_bid"] if side == "BUY" else q["need_ask"]
    if need <= 0:
        return 200, {"ok": True, "placed": 0,
                     "note": f"{name} side already holds Target Size"}
    px = (q["floor_c"] if side == "BUY" else q["ceil_c"]) / 100.0

    def live_bp(fallback: float) -> float:
        try:
            v = fetch_buying_power(KEY_ID, SECRET_KEY)
            return float(v) if v is not None else fallback
        except Exception:  # noqa: BLE001 — fall back rather than stall
            return fallback

    bp = live_bp(float(MONITOR.buying_power or 0.0))
    unit = px if side == "BUY" else 1 - px      # notional a share holds while resting
    # Buying power is NOT drawn down by resting orders — only a fill moves it.
    # It is a ceiling on ONE side of ONE book, and the same balance backs
    # every other market at the same time. So the bound here is this side of
    # this book; there is no budget being shared across a slate of markets,
    # and nothing to reserve for the next market.
    room = max(0.0, min(bp, QUALIFY_MAX_USD) - QUALIFY_RESERVE_USD)
    affordable = int(room / unit) if unit > 0 else 0
    if affordable < 1:
        return 400, {"ok": False,
                     "error": f"no headroom on this side — buying power ${bp:,.2f}"}
    want = min(need, affordable)
    placed = 0
    done = 0
    errs: list[str] = []
    # One tap closes the whole gap, in as many orders as that takes: an ask
    # order can only carry `buying power` shares, so a 1,200-share gap on a
    # $120 balance is ten orders, not one. A bid goes in one.
    for _ in range(QUALIFY_MAX_ORDERS):
        if done >= want:
            break
        short = want - done
        qty = int(min(short, _qual_per_order(side, px, bp)))
        # finishing the gap is always worth an order; a dribble is not
        if qty < 1 or (qty < QUALIFY_MIN_CHUNK and qty < short):
            errs.append(f"buying power ${bp:,.2f} carries only {qty:,} shares per order "
                        f"— {short:,} still needed, so it would take "
                        f"{-(-short // max(qty, 1)):,} orders")
            break
        code, res = manual_place(slug, side, round(px * 100, 1), qty)
        if not res.get("ok"):
            errs.append(str(res.get("detail") or res.get("error") or f"HTTP {code}"))
            break
        placed += 1
        done += qty
        time.sleep(1.0)
        # only a fill moves buying power, but one can land mid-run
        bp = live_bp(bp)
    if want < need:
        errs.append(f"this side of this book tops out at {want:,} shares "
                    f"(${room:,.2f} of room) — {need - want:,} short of Target Size")
    spent = done * unit
    remaining = need - done
    # Report where the side actually ended up, not where we hoped it would.
    # The public book can lag a placement by a beat, so give it one, then
    # clamp what we report to what the arithmetic allows: never claim a
    # bigger gap than (what was missing - what we just placed). A lagging
    # book that still shows the old depth would otherwise invite a second
    # tap and place the size twice.
    left = None
    try:
        time.sleep(2.0)
        after = _qual_view(slug, tr._fetch_book(slug))
        left = after["need_bid"] if side == "BUY" else after["need_ask"]
        left = max(0, min(int(left), remaining))
    except Exception:  # noqa: BLE001 — the placements already happened
        pass
    POLL_KICK.set()
    return (200 if placed else 502), {
        "ok": bool(placed), "placed": placed, "size": done,
        "price_cents": round(px * 100, 1), "spent": round(spent, 2),
        "buying_power": round(bp, 2), "short_of_gap": remaining,
        "remaining_gap": left, "detail": "; ".join(errs)[:200]}


def market_info(slug: str) -> tuple[int, dict]:
    """Book + my orders + position for the tap-a-market action sheet."""
    if not slug or len(slug) > 120:
        return 400, {"error": "bad slug"}
    if not _slug_known(slug):
        return 404, {"error": "unknown market — not in the tracked universe"}
    try:
        book = tr._fetch_book(slug)
    except Exception as e:  # noqa: BLE001
        return 502, {"error": f"book unavailable: {type(e).__name__}: {e}"[:200]}
    mine = [{k: o.get(k) for k in ("id", "side", "price", "size", "est_day",
                                   "verdict", "created", "manual")}
            for o in MONITOR.orders if o.get("market") == slug]
    # Which of our loops placed it, where we know. The prober and earner keep
    # registries by order id; everything else is either the owner's own tap
    # (the exchange flags those MANUAL) or one of the placement loops.
    for o in mine:
        oid = str(o.get("id") or "")
        o["src"] = ("prober" if oid in _PROBE["active"] else
                    "earner" if oid in _EARN["orders"] else
                    "you" if o.get("manual") == "MANUAL" else "")
    net = tr._num((MONITOR.positions.get(slug) or {}).get("netPosition"))
    return 200, {"market": slug, "tick": book.get("tick") or 0.01,
                 "bids": [[p, q] for p, q in (book.get("bids") or [])[:6]],
                 "asks": [[p, q] for p, q in (book.get("asks") or [])[:6]],
                 "orders": mine, "net": net, "buying_power": MONITOR.buying_power,
                 # depth here is the WHOLE side, not the six levels above —
                 # Target Size counts every resting contract on the side
                 "qual": _qual_view(slug, book),
                 "defend": (MONITOR.state.get("defend") or {}).get(slug)}


def do_cancel_order(order_id: str) -> tuple[int, dict]:
    """Cancel ONE of our resting orders (whitelisted against the snapshot)."""
    o = next((o for o in MONITOR.orders if o.get("id") == order_id), None)
    if o is None:
        return 400, {"ok": False, "error": "unknown order id — wait for the next refresh"}
    path = f"/v1/order/{order_id}/cancel"
    try:
        r = requests.request(
            "POST", tr.TRADE_API + path,
            headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", path),
                     "Content-Type": "application/json"},
            json={"marketSlug": o["market"]}, timeout=20,
        )
        ok = r.status_code < 300
        ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                        "market": o["market"], "side": f"{o['side']} (cancel)",
                        "from": round(o["price"] * 100, 1), "to": "—", "size": o["size"],
                        "status": r.status_code,
                        "response": " ".join(r.text.split())[:150], "verified": ok})
        del ACTIONS[:-20]
        POLL_KICK.set()
        return (200 if ok else 502), {"ok": ok, "status": r.status_code,
                                      "detail": "" if ok else tr._http_err(r)[:200]}
    except Exception as e:  # noqa: BLE001
        return 502, {"ok": False, "error": f"{type(e).__name__}: {e}"[:200]}


def manual_place(slug: str, side: str, price_cents: float, size: int,
                 close_short: bool = False) -> tuple[int, dict]:
    """Place ONE post-only order from the market sheet. Same protections as
    the batch placer minus the plan checks: known market, sane price, post-
    only (rests or rejects — can never cross and fill on arrival)."""
    if not _slug_known(slug):
        return 400, {"ok": False, "error": "unknown market"}
    if side not in ("BUY", "SELL"):
        return 400, {"ok": False, "error": "side must be BUY or SELL"}
    if not (0.1 <= price_cents <= 99.9):
        return 400, {"ok": False, "error": "price out of range (0.1–99.9¢)"}
    if not (1 <= size <= 20000):
        return 400, {"ok": False, "error": "size out of range (1–20,000)"}
    intent = "ORDER_INTENT_BUY_LONG"
    if side == "SELL":
        net = tr._num((MONITOR.positions.get(slug) or {}).get("netPosition"))
        # BUY_SHORT opens a short and rests as an ASK; SELL_SHORT would
        # rest as a BID (it CLOSES a short) — the bidding-against-yourself bug
        intent = "ORDER_INTENT_SELL_LONG" if net >= size else "ORDER_INTENT_BUY_SHORT"
    elif close_short:  # buy back a short: SELL_SHORT rests as a BID
        net = tr._num((MONITOR.positions.get(slug) or {}).get("netPosition"))
        if net >= 0:
            return 400, {"ok": False, "error": "no short position to buy back here"}
        intent = "ORDER_INTENT_SELL_SHORT"
    path = "/v1/orders"
    value = f"{price_cents / 100:.3f}".rstrip("0").rstrip(".")
    try:
        r = requests.request(
            "POST", tr.TRADE_API + path,
            headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", path),
                     "Content-Type": "application/json"},
            json={"marketSlug": slug, "intent": intent, "type": "ORDER_TYPE_LIMIT",
                  "price": {"value": value, "currency": "USD"},
                  "quantity": size, "tif": "TIME_IN_FORCE_GOOD_TILL_CANCEL",
                  "participateDontInitiate": True},
            timeout=20,
        )
        ok = r.status_code < 300
        ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                        "market": slug, "side": f"{side} (manual)", "from": "—",
                        "to": price_cents, "size": size, "status": r.status_code,
                        "response": " ".join(r.text.split())[:150], "verified": ok})
        del ACTIONS[:-20]
        POLL_KICK.set()
        return (200 if ok else 502), {"ok": ok, "status": r.status_code,
                                      "detail": "" if ok else tr._http_err(r)[:200]}
    except Exception as e:  # noqa: BLE001
        return 502, {"ok": False, "error": f"{type(e).__name__}: {e}"[:200]}


def take_close(slug: str, size: int, close_short: bool = False) -> tuple[int, dict]:
    """CLOSE part of a position by TAKING the standing touch — the one action
    that is not post-only, so it fills immediately against resting orders.
    Only ever reduces exposure: a sell is capped at the long position, a
    buy-back at the short. Our own resting orders at or better than the take
    price are canceled first so we never trade with ourselves; any unfilled
    remainder rests at the touch price (visible in open orders)."""
    if not _slug_known(slug):
        return 400, {"ok": False, "error": "unknown market"}
    if not (1 <= size <= 20000):
        return 400, {"ok": False, "error": "size out of range (1–20,000)"}
    net = tr._num((MONITOR.positions.get(slug) or {}).get("netPosition"))
    if close_short:
        if net >= 0:
            return 400, {"ok": False, "error": "no short position to buy back here"}
        if size > -net:
            return 400, {"ok": False,
                         "error": f"only short {-net:g} — can't buy back {size}"}
    else:
        if net <= 0:
            return 400, {"ok": False, "error": "no long position to sell here"}
        if size > net:
            return 400, {"ok": False, "error": f"only hold {net:g} — can't sell {size}"}
    try:
        book = tr._fetch_book(slug)
    except Exception as e:  # noqa: BLE001
        return 502, {"ok": False, "error": f"book unavailable: {type(e).__name__}: {e}"[:200]}
    hit_key = "asks" if close_short else "bids"
    my_side = "SELL" if close_short else "BUY"
    mine = [o for o in MONITOR.orders
            if o.get("market") == slug and o.get("side") == my_side and o.get("id")]
    price = None
    for px, q in book.get(hit_key) or []:
        q -= sum(o["size"] for o in mine if abs(px - o["price"]) < 1e-9)
        if q > 1e-9:
            price = px
            break
    if price is None:
        word = "ask" if close_short else "bid"
        return 400, {"ok": False, "error": f"no resting {word} to fill against"}
    # cancel our own orders that sit at-or-better than the take price —
    # otherwise the exchange would happily match us against ourselves
    blockers = [o for o in mine
                if (o["price"] <= price + 1e-9 if close_short
                    else o["price"] >= price - 1e-9)]
    for o in blockers[:5]:
        do_cancel_order(o["id"])
    intent = "ORDER_INTENT_SELL_SHORT" if close_short else "ORDER_INTENT_SELL_LONG"
    path = "/v1/orders"
    value = f"{price:.3f}".rstrip("0").rstrip(".")
    try:
        r = requests.request(
            "POST", tr.TRADE_API + path,
            headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", path),
                     "Content-Type": "application/json"},
            json={"marketSlug": slug, "intent": intent, "type": "ORDER_TYPE_LIMIT",
                  "price": {"value": value, "currency": "USD"},
                  "quantity": size, "tif": "TIME_IN_FORCE_GOOD_TILL_CANCEL",
                  "participateDontInitiate": False},
            timeout=20,
        )
        ok = r.status_code < 300
        ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                        "market": slug,
                        "side": ("BUY BACK" if close_short else "SELL") + " (take)",
                        "from": "—", "to": round(price * 100, 2), "size": size,
                        "status": r.status_code,
                        "response": " ".join(r.text.split())[:150], "verified": ok})
        del ACTIONS[:-20]
        POLL_KICK.set()
        return (200 if ok else 502), {"ok": ok, "status": r.status_code,
                                      "canceled_first": len(blockers[:5]),
                                      "detail": "" if ok else tr._http_err(r)[:200]}
    except Exception as e:  # noqa: BLE001
        return 502, {"ok": False, "error": f"{type(e).__name__}: {e}"[:200]}


def do_maction(body: dict) -> tuple[int, dict]:
    """Single-order actions from the tap-a-market sheet."""
    op = body.get("op")
    if op == "cancel":
        return do_cancel_order(str(body.get("order_id") or ""))
    if op == "modify":
        try:
            return do_reprice(str(body["order_id"]), float(body["price_cents"]),
                              quantity=int(body["size"]) if body.get("size") else None)
        except (KeyError, TypeError, ValueError):
            return 400, {"ok": False, "error": "bad request"}
    if op == "place":
        try:
            return manual_place(str(body["market"]), str(body.get("side") or "BUY"),
                                float(body["price_cents"]), int(body["size"]),
                                close_short=bool(body.get("close_short")))
        except (KeyError, TypeError, ValueError):
            return 400, {"ok": False, "error": "bad request"}
    if op == "take":
        try:
            return take_close(str(body["market"]), int(body["size"]),
                              close_short=bool(body.get("close_short")))
        except (KeyError, TypeError, ValueError):
            return 400, {"ok": False, "error": "bad request"}
    if op == "qualify":
        # market + side only: the size and price are computed server-side
        # from a fresh book, so a stale sheet cannot oversize a placement
        return do_qualify(str(body.get("market") or ""), str(body.get("side") or ""))
    if op == "auto":
        # The owner's on/off button for a placement loop. Auth and the
        # X-Reprice CSRF header are already enforced by the POST handler.
        which = str(body.get("which") or "")
        if which not in ("defend", "keeper", "snipe", "probe", "earn"):
            return 400, {"ok": False,
                         "error": "which must be defend, keeper, snipe, probe or earn"}
        on = bool(body.get("on"))
        with MONITOR.lock:
            auto = MONITOR.state.setdefault("auto", {})
            auto[which] = on
        # audit line in Recent actions, so every flip is visible in the app
        ACTIONS.append({"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
                        "market": f"[{which}]", "side": "switch",
                        "from": "on" if not on else "off",
                        "to": "on" if on else "off", "size": "",
                        "status": 200, "response": "owner toggle", "verified": True})
        del ACTIONS[:-20]
        POLL_KICK.set()   # save + payload refresh promptly
        return 200, {"ok": True, "which": which, "on": on}
    if op == "defend":
        slug = str(body.get("market") or "")
        if not _slug_known(slug):
            return 400, {"ok": False, "error": "unknown market"}
        sides: dict = {}
        for side, k in (("BUY", "bid_cap_c"), ("SELL", "ask_floor_c")):
            v = body.get(k)
            if v in (None, "", False):
                continue
            try:
                c = float(v)
            except (TypeError, ValueError):
                return 400, {"ok": False, "error": "bad cap"}
            if not (0.1 <= c <= 99.9):
                return 400, {"ok": False, "error": "cap out of range (0.1–99.9¢)"}
            sides[side] = {"cap": c}
        if not sides:
            return 400, {"ok": False, "error": "set a bid cap, an ask floor, or both"}
        with MONITOR.lock:
            d = MONITOR.state.setdefault("defend", {})
            if slug not in d and len(d) >= DEFEND_MAX_MARKETS:
                return 400, {"ok": False,
                             "error": f"already defending {DEFEND_MAX_MARKETS} markets "
                                      "— stop one first"}
            d[slug] = sides
            tr.PRIORITY_SLUGS = set(d)
        POLL_KICK.set()
        return 200, {"ok": True, "defend": sides}
    if op == "undefend":
        slug = str(body.get("market") or "")
        with MONITOR.lock:
            d = MONITOR.state.setdefault("defend", {})
            d.pop(slug, None)
            tr.PRIORITY_SLUGS = set(d)
        return 200, {"ok": True}
    return 400, {"ok": False,
                 "error": "op must be place, modify, cancel, qualify, defend or undefend"}


# ---------------------------------------------------------------------------
# Silver Bulletin per-race model, and the per-state view built on top of it
# ---------------------------------------------------------------------------
#
# The forecasts sit behind Datawrapper's CDN, which this host can reach, so the
# monitor pulls them itself on a slow timer rather than depending on a repo
# checkout that only refreshes on deploy. The committed CSVs are the fallback,
# so the map still renders -- flagged stale, with its true date shown -- when
# the CDN is unreachable.

SILVER_SOURCES = {
    "senate": ("https://static.dwcdn.net/data/kNspD.csv",
               tr.DATA / "silver_senate_races.csv"),
    "governor": ("https://static.dwcdn.net/data/N13WX.csv",
                 tr.DATA / "silver_gov_races.csv"),
}
SILVER_TTL = 6 * 3600
SILVER: dict = {"races": {}, "ts": 0.0, "source": "none", "err": ""}

# a fill this far the wrong side of the model is real money, not rounding
MAP_CONFLICT = 0.10
# below this a market is holding capital without paying for it
MAP_IDLE_RATE = 1.00
# The estimate has run anywhere from 2x to 94x above what actually paid, so a
# healthy estimated rate is not evidence a market is earning. These gate a
# separate test that compares the estimate against what the sampler actually
# measured over the same window: only look once enough of the day has been
# sampled, and flag when the take is far below what the estimate implied.
MAP_PAY_MIN_COVER = 7200.0   # seconds of sampled day before the test means anything
MAP_PAY_RATIO = 0.25         # earned this far under the implied take is a flag
MAP_PAY_MIN_IMPLIED = 0.10   # ignore markets whose implied take is pocket change


def _gh_text(path: str, ref: str = "main") -> str:
    """A file's contents from the repo. The monitor runs from a deploy branch
    checkout that carries no data/, so anything the daily workflows produce
    has to be read over the API rather than off disk."""
    if not GITHUB_TOKEN:
        return ""
    try:
        r = requests.get(
            f"{GH_API}/repos/{GITHUB_REPO}/contents/{path}",
            params={"ref": ref},
            headers={"Authorization": f"Bearer {GITHUB_TOKEN}",
                     "Accept": "application/vnd.github.raw+json"},
            timeout=20)
        return r.text if r.status_code == 200 else ""
    except Exception:  # noqa: BLE001 — never kill the poll over this
        return ""


def _parse_silver(text: str) -> dict:
    """Datawrapper race table -> {state abbr: {dem, rep, name}} as fractions."""
    out: dict = {}
    for row in csv.DictReader(io.StringIO(text)):
        abbr = (row.get("abbr") or "").strip().lower()
        if not abbr:
            continue
        try:
            dem = float(row.get("winner_Dparty") or "") / 100.0
            rep = float(row.get("winner_Rparty") or "") / 100.0
        except ValueError:
            continue
        out[abbr] = {"dem": dem, "rep": rep,
                     "name": (row.get("state") or "").strip()}
    return out


def _silver_races() -> dict:
    """{'senate': {...}, 'governor': {...}}, refreshed at most every SILVER_TTL."""
    now = time.time()
    if SILVER["races"] and now - SILVER["ts"] < SILVER_TTL:
        return SILVER["races"]
    races, source, errs = {}, "cdn", []
    for office, (url, fallback) in SILVER_SOURCES.items():
        table = {}
        try:
            r = requests.get(url, timeout=20,
                             headers={"User-Agent": "liquidity-rewards monitor"})
            if r.status_code < 400:
                table = _parse_silver(r.text)
        except Exception as e:  # noqa: BLE001 — the map must never kill the poll
            errs.append(f"{office}: {type(e).__name__}")
        if not table:
            # The container has no data/ directory at all — the Dockerfile
            # copies only live/ and track_rewards.py — so the disk fallback
            # below could never work in production, and whenever the CDN was
            # unreachable the map simply had no model. Read the copy the daily
            # Actions fetch commits to main instead; that is the whole reason
            # that workflow exists.
            try:
                txt = _gh_text(f"data/{Path(fallback).name}")
                if txt:
                    table = _parse_silver(txt)
                    source = "github"
            except Exception as e:  # noqa: BLE001
                errs.append(f"{office} github: {type(e).__name__}")
        if not table:
            try:
                table = _parse_silver(Path(fallback).read_text())
                source = "disk"
            except Exception as e:  # noqa: BLE001
                errs.append(f"{office} fallback: {type(e).__name__}")
        races[office] = table
    SILVER.update({"races": races, "ts": now, "source": source,
                   "err": "; ".join(errs)})
    return races


# slug prefix -> office, and the position of the state code inside the slug
_MAP_FAMILIES = (("ussewc-usse-", "senate"), ("usgubewc-usgub-", "governor"))


def _map_office(slug: str) -> tuple[str, str] | None:
    """(office, state abbr) for a race slug, or None when it is not one."""
    for prefix, office in _MAP_FAMILIES:
        if slug.startswith(prefix):
            parts = slug.split("-")
            if len(parts) > 2 and len(parts[2]) == 2:
                return office, parts[2].lower()
    return None


def _map_payload() -> dict:
    """Per-state roll-up of model, resting orders and earnings.

    Every state the model knows about gets a row, including ones we hold no
    orders in -- a race we never entered is exactly the kind of thing this
    screen exists to surface, and it cannot show up if the rows are built
    from our orders alone.
    """
    races = _silver_races()
    with MONITOR.lock:
        orders = [dict(o) for o in MONITOR.orders]
        earned = dict(MONITOR.state.get("per_market_hf")
                      or MONITOR.state.get("per_market") or {})
        covered_s = float(MONITOR.state.get("hf_covered_s") or 0.0)
        updated = (MONITOR.updated.astimezone(ET).strftime("%I:%M %p ET")
                   if MONITOR.updated else None)
    # what a day's estimated rate implies over the window actually sampled
    day_frac = max(0.0, min(1.0, covered_s / 86400.0))

    states: dict = {}

    def cell(abbr: str) -> dict:
        return states.setdefault(abbr, {
            "abbr": abbr.upper(), "name": "", "offices": {},
            "orders": 0, "est_day": 0.0, "earned": 0.0,
            "worst_edge": None, "worst_market": "", "status": "none",
        })

    # seed from the model so unentered races are visible
    for office, table in races.items():
        for abbr, race in table.items():
            c = cell(abbr)
            c["name"] = c["name"] or race["name"]
            c["offices"][office] = {"dem": round(race["dem"], 4),
                                    "rep": round(race["rep"], 4),
                                    "orders": 0, "est_day": 0.0,
                                    "earned": 0.0, "worst_edge": None,
                                    "markets": {}}

    # Every tracked market in these families, whether or not we hold orders in
    # it. Building the market list from our own orders alone would mean a race
    # we never entered offers nothing to act on, which is precisely the case
    # this screen exists to catch. Sourced from known_mkts because that is the
    # same list manual_place whitelists against, so anything offered here is
    # something the placer will actually accept.
    with MONITOR.lock:
        catalogue = list((MONITOR.state.get("known_mkts") or {}).get("politics") or [])
    for slug in catalogue:
        hit = _map_office(slug)
        if not hit:
            continue
        office, abbr = hit
        if abbr not in states:
            continue
        oc = states[abbr]["offices"].get(office)
        if oc is None:
            # a real market in a race the model has no row for (no Senate
            # contest in this state this cycle, a special, a late addition).
            # Still tradeable, so still offered -- just with no model price.
            oc = states[abbr]["offices"][office] = {
                "dem": None, "rep": None, "orders": 0, "est_day": 0.0,
                "earned": 0.0, "worst_edge": None, "markets": {}}
        if slug in oc["markets"]:
            continue
        race = (races.get(office) or {}).get(abbr)
        fair = None
        if race:
            fair = race["dem"] if slug.endswith("-dem") else (
                race["rep"] if slug.endswith("-rep") else None)
        oc["markets"][slug] = {"orders": 0, "est_day": 0.0,
                               "earned": round(earned.get(slug, 0.0), 2),
                               "fair": None if fair is None else round(fair, 4),
                               "worst_edge": None, "list": []}

    for o in orders:
        slug = o.get("market") or ""
        hit = _map_office(slug)
        if not hit:
            continue
        office, abbr = hit
        race = (races.get(office) or {}).get(abbr)
        c = cell(abbr)
        oc = c["offices"].setdefault(office, {
            "dem": None, "rep": None, "orders": 0, "est_day": 0.0,
            "earned": 0.0, "worst_edge": None, "markets": {}})
        est = float(o.get("est_day") or 0.0)
        c["orders"] += 1
        c["est_day"] += est
        oc["orders"] += 1
        oc["est_day"] += est

        fair = None
        if race:
            if slug.endswith("-dem"):
                fair = race["dem"]
            elif slug.endswith("-rep"):
                fair = race["rep"]
        px = float(o.get("price") or 0.0)
        side = str(o.get("side") or "").upper()
        edge = None
        if fair is not None and px:
            edge = (fair - px) if side.startswith("BUY") else (px - fair)
            for holder in (c, oc):
                if holder["worst_edge"] is None or edge < holder["worst_edge"]:
                    holder["worst_edge"] = edge
            if c["worst_edge"] is not None and edge <= c["worst_edge"]:
                c["worst_market"] = slug

        m = oc["markets"].setdefault(slug, {
            "orders": 0, "est_day": 0.0, "earned": round(earned.get(slug, 0.0), 2),
            "fair": None if fair is None else round(fair, 4), "worst_edge": None,
            "list": []})
        m["orders"] += 1
        m["est_day"] = round(m["est_day"] + est, 2)
        if edge is not None and (m["worst_edge"] is None or edge < m["worst_edge"]):
            m["worst_edge"] = round(edge, 4)
        # the id is what makes a row actionable — /maction addresses orders by it
        m["list"].append({"id": o.get("id"), "side": side,
                          "price": round(px, 4),
                          "size": int(round(float(o.get("size") or 0))),
                          "est_day": round(est, 2),
                          "edge": None if edge is None else round(edge, 4)})

    # earnings are keyed by market, so fold them in per state
    for slug, amount in earned.items():
        hit = _map_office(slug)
        if not hit:
            continue
        office, abbr = hit
        if abbr not in states:
            continue
        states[abbr]["earned"] += float(amount or 0.0)
        oc = states[abbr]["offices"].get(office)
        if oc is not None:
            oc["earned"] = round(oc["earned"] + float(amount or 0.0), 2)

    # classify. Order matters: money at risk outranks money not being made,
    # which outranks a race we simply never entered.
    counts = {"conflict": 0, "notpaying": 0, "idle": 0, "gap": 0, "ok": 0, "none": 0}
    for c in states.values():
        c["est_day"] = round(c["est_day"], 2)
        c["earned"] = round(c["earned"], 2)
        if c["worst_edge"] is not None:
            c["worst_edge"] = round(c["worst_edge"], 4)
        for oc in c["offices"].values():
            oc["est_day"] = round(oc["est_day"], 2)
            if oc["worst_edge"] is not None:
                oc["worst_edge"] = round(oc["worst_edge"], 4)
        implied = round(c["est_day"] * day_frac, 2)
        c["implied"] = implied
        c["covered_h"] = round(covered_s / 3600.0, 1)

        # Per market, not per state. A state total hides a dead market behind a
        # live one -- Wyoming's governor book paying while its senate book pays
        # nothing would still average out to "fine", which is the same masking
        # one level down.
        dead = []
        for office, oc in c["offices"].items():
            for slug, m in oc["markets"].items():
                m_implied = round(m["est_day"] * day_frac, 2)
                m["implied"] = m_implied
                m["paying"] = True
                if (m["orders"] and covered_s >= MAP_PAY_MIN_COVER
                        and m_implied >= MAP_PAY_MIN_IMPLIED
                        and m["earned"] < MAP_PAY_RATIO * m_implied):
                    m["paying"] = False
                    dead.append((slug, office, m))
        c["dead_markets"] = [d[0] for d in dead]

        if c["worst_edge"] is not None and c["worst_edge"] < -MAP_CONFLICT:
            c["status"] = "conflict"
            c["why"] = (f"an order rests {abs(c['worst_edge']):.0%} the wrong side of "
                        f"the model — a fill costs that per share")
        elif dead:
            c["status"] = "notpaying"
            if len(dead) == 1:
                slug, office, m = dead[0]
                c["why"] = (f"the {office} market has taken ${m['earned']:.2f} against "
                            f"${m['implied']:.2f} implied by its ${m['est_day']:.2f}/day "
                            f"estimate over {covered_s / 3600:.1f}h measured")
            else:
                tot_e = sum(m["earned"] for _, _, m in dead)
                tot_i = sum(m["implied"] for _, _, m in dead)
                c["why"] = (f"{len(dead)} markets here have taken ${tot_e:.2f} against "
                            f"${tot_i:.2f} implied over {covered_s / 3600:.1f}h measured")
        elif c["orders"] and c["est_day"] < MAP_IDLE_RATE:
            c["status"] = "idle"
            c["why"] = (f"{c['orders']} order{'s' if c['orders'] != 1 else ''} "
                        f"resting but only ${c['est_day']:.2f}/day estimated")
        elif not c["orders"]:
            c["status"] = "gap"
            c["why"] = "the model covers this race and we hold no orders here"
        else:
            c["status"] = "ok"
            c["why"] = (f"${c['est_day']:.2f}/day estimated across {c['orders']} orders; "
                        f"${c['earned']:.2f} in so far")
        counts[c["status"]] = counts.get(c["status"], 0) + 1

    return {
        "states": sorted(states.values(), key=lambda c: c["abbr"]),
        "counts": counts,
        "updated": updated,
        "model": {"source": SILVER["source"], "err": SILVER["err"],
                  "senate": len(races.get("senate") or {}),
                  "governor": len(races.get("governor") or {}),
                  "age_s": int(time.time() - SILVER["ts"]) if SILVER["ts"] else None},
        "thresholds": {"conflict": MAP_CONFLICT, "idle_rate": MAP_IDLE_RATE},
        # Effective state: the owner's toggle AND the host env veto AND, for
        # defend, whether any market is armed. The page shows the toggles and
        # the reason the loop is not actually running when they disagree.
        # Every switch the page draws must appear here. A key missing from
        # this dict reads as undefined in the browser, so the button repaints
        # OFF on the next refresh even though the loop is running.
        "auto": {"defend": _auto_on("defend"), "keeper": _auto_on("keeper"),
                 "snipe": _auto_on("snipe"), "probe": _auto_on("probe"),
                 "earn": _auto_on("earn")},
        "defend_live": bool(_auto_on("defend")
                            and os.environ.get("DEFEND_PAUSE", "") != "1"
                            and (MONITOR.state.get("defend") or {})),
        "keeper_live": bool(_auto_on("keeper")
                            and os.environ.get("KEEP_PAUSE", "") != "1"),
        "snipe_live": bool(_auto_on("snipe")
                           and os.environ.get("SNIPE_PAUSE", "") != "1"),
        "probe_live": bool(_auto_on("probe")
                           and os.environ.get("PROBE_PAUSE", "") != "1"),
        "earn_live": bool(_auto_on("earn")
                          and os.environ.get("EARN_PAUSE", "") != "1"),
        "probe_budget": round(float(MONITOR.state.get("probe_budget") or 0.0), 2),
        # `rate` is what each bid is earning per day — the owner asked to see
        # it per market, not just as one total. `grad` marks the proven ones,
        # which rest on their own ceiling instead of the search budget.
        "earn_active": [{"m": r[0], "px": r[2], "qty": r[3],
                         "age_m": int((time.time() - r[4]) / 60),
                         "rate": round(float(next(
                             (x.get("est_day") or 0 for x in MONITOR.orders
                              if str(x.get("id")) == oid), 0) or 0), 2),
                         "grad": oid in (_EARN.get("grad") or set()),
                         "on_book": _on_book(r[0], "BUY", r[2] / 100.0, r[3], r[4])}
                        for oid, r in _EARN["orders"].items()],
        # Flips rest on the ASK side out of stock we already hold, so they are
        # listed apart from the bids and never counted against the dollar cap.
        "earn_flips": [{"m": r[0], "px": r[1], "qty": r[2],
                        "age_m": int((time.time() - r[3]) / 60)}
                       for r in (_EARN.get("flips") or {}).values()],
        "earn_toflip": len(_EARN.get("toflip") or []),
        "earn_log": list(reversed((MONITOR.state.get("earn_log") or [])[-30:])),
        "earn_stats": MONITOR.state.get("earn_stats") or {},
        "probe_scoreboard": MONITOR.state.get("probe_scoreboard") or {},
        "earn_caps": {"per_mkt": EARN_MAX_USD, "total": EARN_TOTAL_USD,
                      "outstanding": round(_earn_outstanding_usd(), 2),
                      "grad_usd": round(_earn_graduated_usd(), 2),
                      "grad_max": EARN_GRAD_MAX_USD},
        # slug -> human label, from the exchange's own naming
        "labels": {o["market"]: (
                       (o.get("subject") or "").strip()
                       or (o.get("title") or "").strip())
                   for o in MONITOR.orders
                   if o.get("market") and (o.get("subject") or o.get("title"))},
        "probe_est": MONITOR.state.get("probe") or {},
        "probe_bayes": {m: b for m in sorted(
                            {l.get("m") for l in (MONITOR.state.get("probe_log") or [])}
                            | set((MONITOR.state.get("probe") or {}))
                            | {r[0] for r in _PROBE["active"].values()})
                        if m and (b := _bayes_fair(m))},
        # What each charted market is actually WORTH: `rate` is what our
        # orders there are earning right now ($/day, the same figure the
        # headline counter integrates), `per_side` is the pool a side can win
        # in a day. Sorting by confidence in "stable and high earnings" needs
        # the earnings half measured, not inferred from the price alone.
        "probe_meta": {
            m: {"rate": round(float((MONITOR.market_rates or {}).get(m) or 0.0), 3),
                "peak": round(_rate_trend(m)[0], 3),
                "per_side": round(
                    float(((tr._PROG_CACHE.get("progs") or {}).get(m) or {}).get("pool") or 0.0)
                    / max(int(((tr._PROG_CACHE.get("progs") or {}).get(m) or {}).get("pool_n")
                              or ((tr._PROG_CACHE.get("progs") or {}).get(m) or {}).get("event_n")
                              or 1), 1) / 2, 2)}
            for m in ({l.get("m") for l in (MONITOR.state.get("probe_log") or [])}
                      | set((MONITOR.state.get("probe") or {}))
                      | {r[0] for r in _PROBE["active"].values()}) if m},
        "probe_log": list(reversed((MONITOR.state.get("probe_log") or [])[-40:])),
        # `beaten` marks a scout somebody has since outbid or undercut with
        # real size — the chart draws those amber, because a beaten scout is
        # evidence about fair value rather than a scout still gathering it.
        "probe_active": [{"m": r[0], "side": r[1], "px": round(r[2] * 100, 1),
                          "age_m": int((time.time() - r[3]) / 60), "kind": r[4],
                          "beaten": oid in _PROBE.get("beaten", set()),
                          "on_book": _on_book(r[0], r[1], r[2], PROBE_SIZE, r[3])}
                         for oid, r in _PROBE["active"].items()],
        "defend_markets": len(MONITOR.state.get("defend") or {}),
        "defend_note": ("switched off"
                        if not _auto_on("defend") else
                        "DEFEND_PAUSE=1 is set on the host"
                        if os.environ.get("DEFEND_PAUSE", "") == "1" else
                        "no markets are armed to defend"
                        if not (MONITOR.state.get("defend") or {}) else ""),
    }


MAP_HTML = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Map</title>
<style>
:root{--bg:#1a202b;--surface:#232b38;--surface2:#2b3442;--line:#3a4454;--ink:#eef2f7;
--dim:#93a0b4;--good:#34c07c;--bad:#e5645f;--warn:#d9a132;--accent:#5aa2ff;--r:14px}
*{box-sizing:border-box}
/* /map is the control surface — tiles, order actions, switches. /lab carries
   the prober and earner read-outs, which are analysis, not controls. One
   template serves both so the renderers and the /map.json payload stay
   single-copy; the route decides which sections are on screen. */
body.lab #gridCard,body.lab #listCard,body.lab #det,body.lab #chips,
body.lab .autorow,body.lab #navLab{display:none!important}
body:not(.lab) #probeCard,body:not(.lab) #earnCard{display:none!important}
body.lab #navMap{display:inline-block!important}
.navrow{margin:14px 0 4px;display:flex;gap:10px;flex-wrap:wrap}
body{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
padding:14px 12px 40px;-webkit-text-size-adjust:100%}
h1{font-size:19px;margin:0 0 2px}
.sub{color:var(--dim);font-size:12.5px;margin-bottom:12px}
a{color:var(--accent);text-decoration:none}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);
padding:12px;margin-bottom:12px}
/* summary chips */
.chips{display:grid;grid-template-columns:repeat(5,1fr);gap:5px;margin-bottom:12px}
.chip{background:var(--surface);border:1px solid var(--line);
border-radius:10px;padding:7px 2px;text-align:center;min-width:0}
.chip b{display:block;font-size:18px;font-variant-numeric:tabular-nums;line-height:1.1}
.chip span{font-size:9px;color:var(--dim);text-transform:uppercase;letter-spacing:.02em;
display:block;line-height:1.2;overflow-wrap:anywhere}
.chip.on{outline:2px solid var(--accent)}
.c-conflict b{color:var(--bad)} .c-idle b{color:var(--warn)} .c-notpaying b{color:#e07a3f}
.c-gap b{color:var(--accent)} .c-ok b{color:var(--good)}
/* tile map: fixed 12-col grid, squares, so it holds on a narrow phone */
.grid{display:grid;grid-template-columns:repeat(12,1fr);gap:3px}
.t{aspect-ratio:1;border-radius:5px;border:1px solid transparent;background:transparent;
display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:600;
color:var(--dim);padding:0;font-family:inherit;letter-spacing:.02em}
.t.has{cursor:pointer}
.t.none{background:#212836;color:#4d5768}
.t.ok{background:rgba(52,192,124,.20);color:#8fe3b8;border-color:rgba(52,192,124,.35)}
.t.gap{background:rgba(90,162,255,.16);color:#9cc7ff;border-color:rgba(90,162,255,.32)}
.t.idle{background:rgba(217,161,50,.24);color:#f2cd7f;border-color:rgba(217,161,50,.45)}
.t.notpaying{background:rgba(224,122,63,.55);color:#ffe0cc;border-color:#e07a3f}
.t.conflict{background:var(--bad);color:#fff;border-color:#ff8b86}
.t.sel{outline:2px solid var(--ink);outline-offset:1px}
.t:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
/* legend */
.leg{display:flex;gap:12px;flex-wrap:wrap;margin-top:10px;font-size:11.5px;color:var(--dim)}
.leg i{width:10px;height:10px;border-radius:3px;display:inline-block;margin-right:5px;
vertical-align:-1px}
/* detail + list */
.det h2{font-size:16px;margin:0 0 2px}
.why{font-size:13px;color:var(--dim);margin-bottom:10px}
.off{border-top:1px solid var(--line);padding-top:9px;margin-top:9px}
.off h3{font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);
margin:0 0 6px}
.row{display:flex;justify-content:space-between;gap:10px;font-size:13px;padding:3px 0}
.row span{color:var(--dim)}
.row b{font-variant-numeric:tabular-nums;font-weight:600}
.mkt{font-size:12px;padding:6px 0;border-top:1px dashed var(--line)}
.mkt code{font-size:11px;color:var(--dim);word-break:break-all}
.neg{color:var(--bad)} .pos{color:var(--good)}
.deadmk{background:rgba(224,122,63,.18);border-left:3px solid #e07a3f;color:#ffc9a6;
border-radius:0 6px 6px 0;padding:5px 8px;font-size:11.5px;margin:5px 0}
.item{display:flex;align-items:center;gap:9px;padding:9px 0;border-top:1px solid var(--line);
cursor:pointer}
.item:first-of-type{border-top:0}
.dot{width:9px;height:9px;border-radius:50%;flex:0 0 auto}
.d-conflict{background:var(--bad)} .d-idle{background:var(--warn)} .d-notpaying{background:#e07a3f}
.d-gap{background:var(--accent)} .d-ok{background:var(--good)}
.item .nm{font-weight:600;min-width:30px}
.item .tx{color:var(--dim);font-size:12.5px;flex:1}
.muted{color:var(--dim);font-size:12.5px}
.gaps{display:flex;flex-wrap:wrap;gap:6px;padding:10px 0 2px}
.gchip{background:rgba(90,162,255,.16);border:1px solid rgba(90,162,255,.32);
color:#9cc7ff;border-radius:7px;padding:7px 9px;font:600 12px inherit;cursor:pointer;
font-family:inherit}
.ord{border-top:1px dashed var(--line);padding:8px 0}
.ordhd{display:flex;justify-content:space-between;gap:8px;align-items:baseline;font-size:13px}
.ordhd b{font-variant-numeric:tabular-nums}
.side{font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;padding:2px 6px;
border-radius:5px;background:var(--surface2);color:var(--dim)}
.ctl{display:flex;gap:6px;align-items:center;margin-top:7px}
.ctl input{flex:1;min-width:0;width:auto;padding:8px;font-size:16px;text-align:right}
.ctl .unit{color:var(--dim);font-size:12px;margin-left:-2px}
.btn{border:0;border-radius:8px;padding:9px 11px;font:700 13px inherit;font-family:inherit;
cursor:pointer}
.btn.mv{background:var(--accent);color:#06213f}
.btn.cx{background:rgba(229,100,95,.16);color:#ffb3af;border:1px solid rgba(229,100,95,.4)}
.btn.cx.arm{background:var(--bad);color:#fff}
.btn[disabled]{opacity:.45;cursor:default}
.hint{font-size:11.5px;color:var(--dim);margin-top:5px}
.res{font-size:12px;margin-top:6px;padding:7px 8px;border-radius:8px;display:none}
.res.ok{display:block;background:rgba(52,192,124,.16);color:#8fe3b8}
.res.err{display:block;background:rgba(229,100,95,.16);color:#ffb3af}
.banner{background:rgba(217,161,50,.16);border:1px solid rgba(217,161,50,.4);
color:#f2cd7f;border-radius:11px;padding:9px 11px;font-size:12.5px;margin-bottom:12px}
.banner.ok{background:rgba(52,192,124,.14);border-color:rgba(52,192,124,.4);color:#8fe3b8}
.autorow{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px}
.autosw{background:var(--surface);border:1px solid var(--line);border-radius:11px;
padding:10px 12px;text-align:left;cursor:pointer;font-family:inherit}
.autosw .nm{font-size:13px;font-weight:700;color:var(--ink);display:block}
.autosw .st{font-size:11.5px;color:var(--dim);display:block;margin-top:2px}
.autosw.on{border-color:rgba(52,192,124,.5);background:rgba(52,192,124,.10)}
.autosw.on .st{color:#8fe3b8}
.autosw.arm{border-color:var(--warn);background:rgba(217,161,50,.14)}
.autosw.arm .st{color:#f2cd7f}
.autosw[disabled]{opacity:.5}
.bkbtn{background:var(--surface2);color:var(--ink);border:1px solid var(--line);
border-radius:8px;padding:6px 10px;font:600 12px inherit;font-family:inherit;cursor:pointer;
margin-top:7px}
.newbox{margin-top:8px;border:1px dashed var(--line);border-radius:10px;padding:9px}
.newbox .ttl{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);
margin-bottom:7px}
.seg{display:flex;gap:0;margin-bottom:7px;border:1px solid var(--line);border-radius:8px;
overflow:hidden}
.seg button{flex:1;background:none;border:0;color:var(--dim);padding:9px 0;
font:700 12px inherit;font-family:inherit;cursor:pointer}
.seg button.on.buy{background:rgba(52,192,124,.25);color:#8fe3b8}
.seg button.on.sell{background:rgba(229,100,95,.22);color:#ffb3af}
.nrow{display:flex;gap:6px;align-items:center}
.nrow input{flex:1;min-width:0;padding:8px;font-size:16px;text-align:right}
.nrow .unit{color:var(--dim);font-size:12px}
.btn.new{background:var(--good);color:#0b2417}
.book{margin-top:8px;border:1px solid var(--line);border-radius:10px;overflow:hidden}
.brow{display:grid;grid-template-columns:52px 1fr 62px;align-items:center;gap:8px;
padding:4px 8px;font-size:12px;font-variant-numeric:tabular-nums;position:relative}
.brow .px{font-weight:700}
.brow .bar{height:15px;border-radius:3px;min-width:2px}
.brow .qt{text-align:right;color:var(--dim);font-size:11px}
.ask .px{color:#ffb3af} .ask .bar{background:rgba(229,100,95,.42)}
.bid .px{color:#8fe3b8} .bid .bar{background:rgba(52,192,124,.42)}
.brow.me{background:rgba(90,162,255,.16)}
.brow.me .qt{color:#9cc7ff;font-weight:700}
.spread{padding:4px 8px;font-size:11px;color:var(--dim);background:rgba(10,14,20,.4);
text-align:center;letter-spacing:.03em}
.fair{padding:3px 8px;font-size:11px;font-weight:700;color:#f2cd7f;
background:rgba(217,161,50,.18);border-top:1px dashed rgba(217,161,50,.5);
border-bottom:1px dashed rgba(217,161,50,.5);text-align:center}
input{background:var(--surface2);border:1px solid var(--line);color:var(--ink);
border-radius:9px;padding:9px 10px;font-size:16px;width:100%}
button.go{background:var(--accent);color:#06213f;border:0;border-radius:9px;
padding:10px 14px;font-weight:700;font-size:14px;margin-top:8px;cursor:pointer}
</style></head><body>
<h1>Where to manage orders</h1>
<div class="sub"><a href="/">&larr; dashboard</a> &nbsp;·&nbsp; <span id="meta">loading…</span></div>
<div id="login" class="card" style="display:none">
  <div style="margin-bottom:8px">Dashboard key</div>
  <input id="k" type="password" autocomplete="current-password" placeholder="key">
  <button class="go" onclick="saveKey()">Unlock</button>
</div>
<div id="app" style="display:none">
  <div class="autorow">
    <button class="autosw" id="sw_defend" onclick="swTap('defend')" disabled>
      <span class="nm">Defender</span><span class="st">loading…</span></button>
    <button class="autosw" id="sw_keeper" onclick="swTap('keeper')" disabled>
      <span class="nm">Keeper</span><span class="st">loading…</span></button>
    <button class="autosw" id="sw_snipe" onclick="swTap('snipe')" disabled>
      <span class="nm">Sniper</span><span class="st">loading…</span></button>
    <button class="autosw" id="sw_probe" onclick="swTap('probe')" disabled>
      <span class="nm">Prober</span><span class="st">loading…</span></button>
    <button class="autosw" id="sw_earn" onclick="swTap('earn')" disabled>
      <span class="nm">Earner</span><span class="st">loading…</span></button>
  </div>
  <div class="banner" id="banner" style="display:none"></div>
  <div class="chips" id="chips"></div>
  <div class="card" id="gridCard">
    <div class="grid" id="grid"></div>
    <div class="leg">
      <span><i style="background:var(--bad)"></i>fix now</span>
      <span><i style="background:#e07a3f"></i>not paying</span>
      <span><i style="background:var(--warn)"></i>low estimate</span>
      <span><i style="background:var(--accent)"></i>not entered</span>
      <span><i style="background:var(--good)"></i>fine</span>
      <span><i style="background:#212836"></i>no race</span>
    </div>
  </div>
  <div class="card det" id="det" style="display:none"></div>
  <div class="card" id="probeCard" style="display:none">
    <div style="font-size:12px;text-transform:uppercase;letter-spacing:.06em;
    color:var(--dim);margin-bottom:6px">🔍 Prober — what the scouts found</div>
    <div id="probeBody"></div>
  </div>
  <div class="card" id="earnCard" style="display:none">
    <div style="font-size:12px;text-transform:uppercase;letter-spacing:.06em;
    color:var(--dim);margin-bottom:6px">💰 Earner — model-confident bids</div>
    <div id="earnBody"></div>
  </div>
  <div class="card" id="listCard">
    <div style="font-size:12px;text-transform:uppercase;letter-spacing:.06em;
    color:var(--dim);margin-bottom:6px">Needs attention</div>
    <div id="list"></div>
  </div>
  <div class="navrow">
    <button class="alt" id="navLab" onclick="location.href='/lab'">
      🔬 Prober &amp; Earner</button>
    <button class="alt" id="navMap" onclick="location.href='/map'"
      style="display:none">🗺 Back to the map</button>
  </div>
</div>
<script>
// Approximate geographic tile grid. A real projection would put Rhode Island
// under a fingertip on a phone; equal squares stay tappable and legible, which
// is what this screen is for.
const GRID = [
 ["AK","","","","","","","","","","","ME"],
 ["","","","","","","","","","","VT","NH"],
 ["WA","ID","MT","ND","MN","IL","WI","MI","","NY","RI","MA"],
 ["OR","NV","WY","SD","IA","IN","OH","PA","NJ","CT","",""],
 ["CA","UT","CO","NE","MO","KY","WV","VA","MD","DE","",""],
 ["","AZ","NM","KS","AR","TN","NC","SC","DC","","",""],
 ["","","","OK","LA","MS","AL","GA","","","",""],
 ["HI","","","TX","","","","","FL","","",""]
];
// order is urgency: money at risk, then a market whose estimate is not
// materialising, then one the estimate itself says is barely worth holding
const RANK = {conflict:0, notpaying:1, idle:2, gap:3, ok:4};
const LABEL = {conflict:"fix now", notpaying:"not paying", idle:"low estimate",
               gap:"not entered", ok:"fine"};
let DATA=null, SEL=null, FILTER=null, SHOWGAPS=false;
// Which route is this? /lab shows the prober and earner read-outs; /map keeps
// the control surface uncluttered. Set before the first paint so neither page
// flashes the other's sections.
const LAB = location.pathname.indexOf('/lab') === 0;
if (LAB) { document.body.classList.add('lab'); document.title = 'Prober & Earner'; }

function hdrs(){ const h=new Headers(); h.set('X-Dash-Key', localStorage.getItem('dashKey')||''); return h; }
function saveKey(){ localStorage.setItem('dashKey', document.getElementById('k').value); load(); }
function money(v){ return '$'+(v||0).toFixed(2); }

async function load(){
  let r;
  try { r = await fetch('/map.json', {headers:hdrs()}); }
  catch(e){ document.getElementById('meta').textContent='offline'; return; }
  if(r.status===401){ document.getElementById('login').style.display='block';
                      document.getElementById('app').style.display='none'; return; }
  DATA = await r.json();
  document.getElementById('login').style.display='none';
  document.getElementById('app').style.display='block';
  render();
}

function render(){
  const st={}; DATA.states.forEach(s=>st[s.abbr]=s);
  const c=DATA.counts;
  document.getElementById('chips').innerHTML = ['conflict','notpaying','idle','gap','ok'].map(k=>
    `<button class="chip c-${k} ${FILTER===k?'on':''}" onclick="setFilter('${k}')">
     <b>${c[k]||0}</b><span>${LABEL[k]}</span></button>`).join('');

  document.getElementById('grid').innerHTML = GRID.map(row=>row.map(ab=>{
    if(!ab) return '<div class="t"></div>';
    const s=st[ab];
    if(!s) return `<div class="t none">${ab}</div>`;
    const dim = FILTER && s.status!==FILTER ? 'opacity:.25;' : '';
    return `<button class="t has ${s.status} ${SEL===ab?'sel':''}" style="${dim}"
            onclick="pick('${ab}')" aria-label="${s.name}: ${s.why}">${ab}</button>`;
  }).join('')).join('');

  swRender();
  renderProbe();
  renderEarn();
  const bn=document.getElementById('banner');
  if(DATA.auto && DATA.auto.defend===true && DATA.defend_live===false){
    // switched on but vetoed by something else -- say what
    bn.style.display='block'; bn.className='banner';
    bn.textContent='Defender is switched on but NOT running — '
      + (DATA.defend_note||'reason unknown');
  } else if(DATA.defend_live===true){
    bn.style.display='block'; bn.className='banner ok';
    bn.textContent='Defender running across ' + DATA.defend_markets + ' markets.';
  } else { bn.style.display='none'; }

  const m=DATA.model;
  document.getElementById('meta').textContent =
    `${m.senate} Senate + ${m.governor} Governor races · model from ${m.source==='cdn'?'live feed':'last saved copy'}`
    + (DATA.updated? ` · orders ${DATA.updated}`:'');

  // Only things needing a decision get a row. Unentered races are a single
  // collapsed line: they all say the same sentence, and 40 copies of it would
  // bury the two orders that are actually losing money.
  const act = DATA.states.filter(s=>s.status==='conflict'||s.status==='notpaying'||s.status==='idle')
    .sort((a,b)=> RANK[a.status]-RANK[b.status] || (b.orders-a.orders) || a.abbr.localeCompare(b.abbr));
  const gaps = DATA.states.filter(s=>s.status==='gap').sort((a,b)=>a.abbr.localeCompare(b.abbr));
  let out = act.map(s=>
    `<div class="item" onclick="pick('${s.abbr}')">
       <span class="dot d-${s.status}"></span>
       <span class="nm">${s.abbr}</span>
       <span class="tx">${s.why}</span>
     </div>`).join('');
  if(gaps.length){
    out += `<div class="item" onclick="tglGaps()">
       <span class="dot d-gap"></span>
       <span class="nm">${gaps.length}</span>
       <span class="tx">race${gaps.length===1?'':'s'} the model covers with no orders of ours
         &nbsp;<a href="#">${SHOWGAPS?'hide':'show'}</a></span></div>`;
    if(SHOWGAPS) out += `<div class="gaps">` + gaps.map(s=>
       `<button class="gchip" onclick="pick('${s.abbr}')">${s.abbr}</button>`).join('') + `</div>`;
  }
  if(!act.length && !gaps.length)
    out = '<div class="muted">Nothing flagged — every modelled race is entered and paying.</div>';
  else if(!act.length)
    out = '<div class="muted" style="padding-bottom:8px">No order is mispriced or idle.</div>' + out;
  document.getElementById('list').innerHTML = out;
  if(SEL) detail(SEL);
}

// Owner switches for the two placement loops. Off is one tap and takes
// effect immediately. On requires a second tap within 5 seconds -- turning a
// loop that places real orders on is the direction that deserves friction.
const SWDESC = {
  defend: {on:'repricing orders in armed markets', off:'not placing anything'},
  keeper: {on:'placing size to hold qualification', off:'not placing anything'},
  snipe: {on:'taking tiny over-priced 2028 bids', off:'not taking anything'},
  probe: {on:'1-share scouts mapping fair prices', off:'not scouting'},
  earn: {on:'small bids where the model is confident', off:'not placing'},
};
const SWARM = {};
function renderProbe(){
  const card = document.getElementById('probeCard'); if(!card) return;
  const est = DATA.probe_est || {}, act = DATA.probe_active || [], log = DATA.probe_log || [];
  const on = DATA.auto && DATA.auto.probe === true;
  if(!on && !Object.keys(est).length && !act.length && !log.length){
    card.style.display = 'none'; return;
  }
  card.style.display = 'block';
  const nm = m => m.replace(/^enwc-uspres-nom-/, 'nom·').replace(/^ewc-usp-2028-11-07-/, 'win·');
  const bayes = DATA.probe_bayes || {};
  // ONE PICTURE PER MARKET, on a common 0-100c axis so markets can be read
  // against each other at a glance. Everything the prober knows is on it:
  //
  //   above the axis   sell scouts as down-arrows, and any real trade
  //   the axis itself  the posterior — a wide 10-90% band with a brighter
  //                    core, so certainty reads as a narrow bright shape and
  //                    doubt as a wide dim one, without needing a number
  //   on the axis      the real de-baited touches, blue bid and red ask; the
  //                    dark space between them is the gap nobody is quoting
  //   below the axis   buy scouts as up-arrows, earner bids as green blocks,
  //                    and hollow ticks where a scout sat untouched
  //
  // Scale is 1 SVG unit = 1 cent, so a price maps straight to an x with no
  // arithmetic to get wrong.
  // A 0-100c axis was the mistake: these markets live between 2c and 30c, so
  // every mark landed in the left quarter on top of every other mark. Each
  // chart now ZOOMS to its own market — the window is whatever that market
  // has marks in, padded — and both ends are labelled in cents so a zoomed
  // axis can never be mistaken for the full one.
  const LB = DATA.labels || {};
  const nice = m => {
    if (LB[m]) return LB[m];
    let r = m.match(/-(usse|usgub|ushr)p?-([a-z]{2})-\d{4}-\d{2}-\d{2}-(dem|rep)$/);
    if (r) return r[2].toUpperCase() + ' ' +
      ({usse: 'Senate', usgub: 'Governor', ushr: 'House'}[r[1]]) +
      ' · ' + r[3].toUpperCase();
    r = m.match(/^enwc-uspres-nom-(dem|rep)-2028-(\w+)$/);
    if (r) return r[2] + ' · ' + r[1].toUpperCase() + ' nomination';
    r = m.match(/^ewc-usp-2028-11-07-(\w+)$/);
    if (r) return r[1] + ' · president 2028';
    r = m.match(/^scc-(senate|hrep)-(gop|rep|dem)-\d{4}-\d{2}-\d{2}-(\w+)$/);
    if (r) return (r[1] === 'senate' ? 'Senate' : 'House') + ' seats · ' + r[3];
    return m;
  };
  const mktChart = (b, e, sc, eb) => {
    // everything this market wants to show, so the window can contain it
    const pts = [b.lo, b.hi, b.med];
    if (b.bb != null) pts.push(b.bb);
    if (b.ba != null) pts.push(b.ba);
    [e.traded_at_bid, e.traded_at_ask, e.rested_bid, e.rested_ask].forEach(v => {
      if (v != null) pts.push(v * 100); });
    sc.forEach(a => pts.push(a.px));
    eb.forEach(p => pts.push(p));
    let w0 = Math.min.apply(null, pts), w1 = Math.max.apply(null, pts);
    const pad = Math.max(1.5, (w1 - w0) * 0.18);
    w0 = Math.max(0, w0 - pad); w1 = Math.min(100, w1 + pad);
    if (w1 - w0 < 4) { const c = (w0 + w1) / 2; w0 = Math.max(0, c - 2); w1 = Math.min(100, c + 2); }
    // cents -> viewBox x. Marks are sized in viewBox units, not cents, so they
    // stay the same size on screen however tight the zoom is.
    const X = v => Math.max(0, Math.min(100, (v - w0) / (w1 - w0) * 100));
    const g = [];
    if (b.bb != null && b.ba != null && b.ba > b.bb)
      g.push('<rect x="' + X(b.bb) + '" y="2.4" width="' + Math.max(0, X(b.ba) - X(b.bb)) +
             '" height="3.8" fill="#161c26"/>');
    const bl = X(b.lo), bh = X(b.hi), q = (bh - bl) / 4;
    g.push('<rect x="' + bl + '" y="2.4" width="' + Math.max(1, bh - bl) +
           '" height="3.8" fill="rgba(63,185,80,.20)"/>');
    g.push('<rect x="' + Math.max(0, X(b.med) - q) + '" y="2.4" width="' + Math.max(1, 2 * q) +
           '" height="3.8" fill="rgba(63,185,80,.42)"/>');
    g.push('<rect x="' + (X(b.med) - 0.5) + '" y="1.2" width="1" height="6.2" fill="#3fb950"/>');
    if (b.bb != null) g.push('<rect x="' + (X(b.bb) - 0.4) + '" y="2.2" width="0.8" height="4.2" fill="#58a6ff"/>');
    if (b.ba != null) g.push('<rect x="' + (X(b.ba) - 0.4) + '" y="2.2" width="0.8" height="4.2" fill="#e5645f"/>');
    [e.traded_at_bid, e.traded_at_ask].forEach(v => { if (v != null)
      g.push('<rect x="' + (X(v * 100) - 1) + '" y="0" width="2" height="1.6" fill="#f0883e"/>'); });
    [e.rested_bid, e.rested_ask].forEach(v => { if (v != null)
      g.push('<rect x="' + (X(v * 100) - 0.35) + '" y="6.4" width="0.7" height="1.5" fill="#93a0b4"/>'); });
    sc.forEach(a => {
      const x = X(a.px);
      const col = a.beaten ? '#f2cd7f' : a.on_book === false ? '#e5645f' : '#58a6ff';
      g.push(a.side === 'BUY'
        ? '<path d="M' + (x - 1.7) + ' 10 L' + (x + 1.7) + ' 10 L' + x + ' 6.6 Z" fill="' + col + '"/>'
        : '<path d="M' + (x - 1.7) + ' 0 L' + (x + 1.7) + ' 0 L' + x + ' 3.4 Z" fill="' + col + '"/>');
    });
    eb.forEach(p => g.push('<rect x="' + (X(p) - 0.9) + '" y="7.4" width="1.8" height="2.4" fill="#3fb950"/>'));
    return '<svg viewBox="0 0 100 10" width="100%" height="36" ' +
      'preserveAspectRatio="none" style="display:block">' +
      '<rect x="0" y="4.1" width="100" height="0.35" fill="#3a4454"/>' + g.join('') + '</svg>' +
      '<div class="sub" style="font-size:9.5px;display:flex;justify-content:space-between;' +
      'margin-top:-1px"><span>' + w0.toFixed(0) + '¢</span><span>' + w1.toFixed(0) + '¢</span></div>';
  };
  const chartLegend =
    '<details style="margin:2px 0 8px"><summary class="sub" style="cursor:pointer;' +
    'font-size:11px">what the marks mean</summary>' +
    '<div class="sub" style="font-size:10.5px;line-height:1.7;margin-top:4px">' +
    '<span style="color:#3fb950">▌</span> our fair estimate · ' +
    '<span style="color:#3fb950">▓</span> its likely range<br>' +
    '<span style="color:#58a6ff">▌</span> best bid · ' +
    '<span style="color:#e5645f">▌</span> best ask · between them is the untraded gap<br>' +
    '<span style="color:#58a6ff">▲</span> our buy scout · ' +
    '<span style="color:#58a6ff">▼</span> sell scout · ' +
    '<span style="color:#f2cd7f">▲</span> outbid · ' +
    '<span style="color:#e5645f">▲</span> not on the book<br>' +
    '<span style="color:#f0883e">■</span> a scout got traded here · ' +
    '<span style="color:#93a0b4">▕</span> held with no taker · ' +
    '<span style="color:#3fb950">■</span> earner bid<br>' +
    'each chart is zoomed to its own market — the cents at either end say how far' +
    '</div></details>';
  // ORDER BY CONFIDENCE IN STABLE, HIGH EARNINGS. One signed score:
  //
  //   +1  we are sure this market pays and our order will sit there
  //    0  we do not know yet
  //   -1  we are sure it cannot pay, or cannot pay us
  //
  // It is a product of two things, which is what makes the middle behave.
  // `conf` is how much we actually know — evidence count, sharpened by how
  // narrow the band is. `good` is what we know, from -1 to +1. A market we
  // are certain is hopeless scores strongly negative; a market with a great
  // story and two observations behind it scores near zero and stays in the
  // middle where it belongs, instead of jumping the queue on a guess.
  const META = DATA.probe_meta || {};
  const verdict = m => {
    const b = bayes[m], e = est[m] || {}, mt = META[m] || {};
    const sc = act.filter(a => a.m === m);
    const eb_ = (DATA.earn_active || []).filter(x => x.m === m);
    const beaten = sc.filter(a => a.beaten).length;
    const fills = (b.fills || 0) + (e.fills || 0);
    const rested = b.rested || 0;
    const ev = fills * 3 + rested * 2 + (b.n || 0);
    const tight = 1 - Math.min(1, (b.hi - b.lo) / 20);
    const conf = Math.min(1, ev / 12) * (0.35 + 0.65 * tight);
    const why = [];
    let good = 0;
    if (rested) { good += 0.5 * Math.min(1, rested / 3);
                  why.push(rested + ' held with no taker'); }
    if (fills)  { good -= 0.9 * Math.min(1, fills);
                  why.push(fills + ' got traded'); }
    // HIGH earnings, not merely non-zero. Real rates here run from nothing to
    // $8.40/day, so the scale is set against $4 rather than $1 — otherwise
    // every market that earns a few cents claims the top zone and the ranking
    // stops telling the owner anything.
    if (mt.rate >= 0.25) { good += 0.6 * Math.min(1, mt.rate / 4);
                           why.push('earning $' + mt.rate.toFixed(2) + '/day now'); }
    else if (sc.length || eb_.length) { good -= 0.45;
                           why.push('we are resting there and earning nothing'); }
    if (beaten) { good -= 0.4 * Math.min(1, beaten / 2);
                  why.push('outbid ' + beaten + 'x'); }
    // A market well below its own 8h peak is one somebody else has moved
    // into. Only counted where we still hold something, because with nothing
    // resting the rate is zero for the dull reason that we are not there.
    if ((sc.length || eb_.length) && mt.peak >= 1 && mt.rate < 0.4 * mt.peak) {
      good -= 0.45;
      why.push('rate fell $' + mt.peak.toFixed(2) + ' → $' + mt.rate.toFixed(2) + '/day');
    }
    if (mt.per_side >= 1) { good += 0.2 * Math.min(1, mt.per_side / 10);
                            why.push('$' + mt.per_side.toFixed(2) + '/side/day on offer'); }
    else if (mt.per_side != null) { good -= 0.5;
                                    why.push('only $' + (mt.per_side || 0).toFixed(2) + '/side/day here'); }
    good = Math.max(-1, Math.min(1, good));
    return {score: conf * good, conf: conf, why: why};
  };
  const V = {};
  const mktSet = Object.keys(Object.assign({}, est, bayes))
    .filter(m => bayes[m] && bayes[m].med != null);
  mktSet.forEach(m => { V[m] = verdict(m); });
  mktSet.sort((a, c) => V[c].score - V[a].score);
  const ZONE = sc_ => sc_ >= 0.25 ? 0 : sc_ <= -0.15 ? 2 : 1;
  const ZHEAD = [
    ['✅ Worth resting in', 'earns, and our orders stay put', '#3fb950'],
    ['◻︎ Not sure yet', 'too little evidence to call either way', '#93a0b4'],
    ['⛔️ Not worth it', 'cannot pay, or will not leave us alone', '#e5645f'],
  ];
  // Each zone folds. The top one is open — it is the answer to "where is the
  // money" — and the other two stay shut until asked for, so 176 markets do
  // not arrive as one endless scroll on a phone.
  const bands = (() => {
    let out = '', zone = -1;
    const counts = [0, 0, 0];
    mktSet.forEach(m => { counts[ZONE(V[m].score)]++; });
    mktSet.forEach(m => {
      const b = bayes[m], e = est[m] || {}, v = V[m];
      const z = ZONE(v.score);
      if (z !== zone) {
        if (zone !== -1) out += '</details>';
        zone = z;
        out += '<details' + (z === 0 ? ' open' : '') +
          ' style="margin-top:10px;border-top:1px solid var(--line);padding-top:8px">' +
          '<summary style="cursor:pointer;list-style:none">' +
          '<b style="font-size:12px;color:' + ZHEAD[z][2] + '">' + ZHEAD[z][0] +
          ' (' + counts[z] + ')</b>' +
          '<span class="sub" style="font-size:10px"> — ' + ZHEAD[z][1] + '</span></summary>';
      }
      const sc = act.filter(a => a.m === m);
      const eb = (DATA.earn_active || []).filter(x => x.m === m).map(x => x.px);
      out += '<div style="margin:0 0 14px">' +
        '<div style="display:flex;align-items:baseline;gap:6px">' +
        '<b style="font-size:13px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;' +
        'flex:1 1 auto;min-width:0">' + nice(m) + '</b>' +
        '<span style="font-size:14px;color:#3fb950;font-weight:700;flex:0 0 auto">' +
        b.med + '¢</span></div>' +
        '<div class="sub" style="font-size:10px;margin-bottom:3px">' +
        (v.why.length ? v.why.join(' · ') : 'nothing observed yet') +
        '<br>fair ' + b.lo + '–' + b.hi + '¢ · ' + Math.round(v.conf * 100) + '% sure</div>' +
        mktChart(b, e, sc, eb) + '</div>';
    });
    return out + (zone !== -1 ? '</details>' : '');
  })();
  const scouts = act.map(a =>
    '<span style="display:inline-block;background:var(--surface2);border-radius:6px;' +
    'padding:2px 8px;margin:2px;font-size:11px">' + nm(a.m) + ' ' +
    (a.kind === 'flip' ? '↩' : '') + a.side + ' @ ' + a.px + '¢ · ' + a.age_m + 'm' +
    (a.on_book === false ? ' <b style="color:#e5645f">✗dark</b>'
     : a.on_book === true ? ' <span style="color:#3fb950">✓</span>' : '') + '</span>').join('');
  const lines = log.map(l =>
    '<div style="font-size:11px;padding:3px 0;border-top:1px dashed var(--line)">' +
    '<span class="sub">' + l.ts + '</span> <b>' + nm(l.m) + '</b> ' +
    (l.ev === 'FILLED' ? '<span style="color:#f0883e">FILLED</span>' :
     l.ev === 'round trip' ? '<span style="color:#3fb950">round trip ✓</span>' : l.ev) +
    ' ' + l.side + ' @ ' + l.px + '¢' +
    (l.note ? ' <span class="sub">— ' + l.note + '</span>' : '') + '</div>').join('');
  const wallet =
    '<div class="sub" style="margin-bottom:4px">info fund: <b style="color:' +
    ((DATA.probe_budget || 0) > 0.5 ? '#3fb950' : '#ff9d99') + '">$' +
    (DATA.probe_budget || 0).toFixed(2) +
    '</b> — prober sales in, prober buys out; sell scouts use your existing shares</div>';
  // Charts first — they are what the page is for. The fund, the scout chips
  // and the journal are supporting detail and fold underneath.
  const nGood = mktSet.filter(m => V[m].score >= 0.25).length;
  const nBad = mktSet.filter(m => V[m].score <= -0.15).length;
  const headline = mktSet.length
    ? '<div style="font-size:13px;margin-bottom:2px">' + mktSet.length +
      ' market' + (mktSet.length === 1 ? '' : 's') + ' mapped · <b style="color:#3fb950">' +
      nGood + '</b> worth resting in · <b style="color:#e5645f">' + nBad +
      '</b> ruled out · ' + (mktSet.length - nGood - nBad) + ' undecided</div>'
    : '<div class="sub">no market has enough evidence for a fair-price estimate yet' +
      (on ? ' — scouts are out' : ' — Prober is off') + '</div>';
  document.getElementById('probeBody').innerHTML = headline +
    (bands ? chartLegend + bands : '') +
    '<details style="margin-top:2px"><summary class="sub" style="cursor:pointer">' +
    'fund, scouts and journal</summary>' + wallet +
    (act.length ? '<div class="sub" style="margin:6px 0 4px">' + act.length +
      ' scout' + (act.length > 1 ? 's' : '') + ' resting</div>' + scouts :
      '<div class="sub">no scouts resting' + (on ? ' — placing as books allow' : ' — Prober is off') + '</div>') +
    (lines ? '<div style="margin-top:8px">' + lines + '</div>' : '') +
    '</details>';
}

function renderEarn(){
  const card = document.getElementById('earnCard'); if(!card) return;
  const act = DATA.earn_active || [], log = DATA.earn_log || [];
  const st = DATA.earn_stats || {}, caps = DATA.earn_caps || {};
  const on = DATA.auto && DATA.auto.earn === true;
  if(!on && !act.length && !log.length){ card.style.display = 'none'; return; }
  card.style.display = 'block';
  const nm = m => m.replace(/^enwc-uspres-nom-/, 'nom·').replace(/^ewc-usp-2028-11-07-/, 'win·');
  const bayes = DATA.probe_bayes || {};
  const status = !on ? 'switch OFF' :
    (DATA.earn_live ? '<span style="color:#3fb950">live</span>' : 'paused by host');
  // Each bid says what it is earning, because "how much is this one making"
  // is the question the whole card exists to answer.
  const mkRow = a => {
    const b = bayes[a.m];
    const bk = a.on_book === true ? ' <span style="color:#3fb950">on book ✓</span>'
             : a.on_book === false ? ' <span style="color:#e5645f;font-weight:700">NOT ON BOOK</span>'
             : a.age_m < 3 ? ' <span class="sub">settling…</span>'
             : ' <span class="sub">book stale</span>';
    const hrs = a.age_m >= 90 ? (a.age_m / 60).toFixed(1) + 'h' : a.age_m + 'm';
    return '<tr><td class="mkt" style="word-break:normal"><b>' + nm(a.m) + '</b>' +
      '<div style="font-size:12px;color:' + (a.rate > 0 ? '#3fb950' : 'var(--dim)') +
      ';font-weight:600">$' + (a.rate || 0).toFixed(2) + '/day</div></td>' +
      '<td class="r" style="font-size:11px">' + a.qty + ' @ ' + a.px + '¢ · ' + hrs + bk +
      (b && b.med != null ? '<div class="sub" style="font-size:10px">model now: ~' +
        b.med + '¢ (' + b.lo + '–' + b.hi + '¢)</div>' : '') + '</td></tr>';
  };
  const byRate = (x, y) => (y.rate || 0) - (x.rate || 0);
  const gradA = act.filter(a => a.grad).sort(byRate);
  const searchA = act.filter(a => !a.grad).sort(byRate);
  const tbl = (arr, label, openIt) => arr.length
    ? '<details' + (openIt ? ' open' : '') + ' style="margin-top:6px">' +
      '<summary class="sub" style="cursor:pointer;font-size:11px">' + label +
      ' — $' + arr.reduce((t, a) => t + (a.rate || 0), 0).toFixed(2) + '/day total</summary>' +
      '<table style="width:100%;border-collapse:collapse">' +
      arr.map(mkRow).join('') + '</table></details>'
    : '';
  const rows = tbl(gradA, '🎓 graduated (' + gradA.length + ') — proven, off the search budget', true) +
               tbl(searchA, '🔍 still proving (' + searchA.length + ')', true);
  const lines = log.map(l =>
    '<div style="font-size:11px;padding:3px 0;border-top:1px dashed var(--line)">' +
    '<span class="sub">' + l.ts + '</span> <b>' + nm(l.m) + '</b> ' +
    (l.ev === 'filled' ? '<span style="color:#f0883e">FILLED</span>' :
     l.ev === 'placed' ? '<span style="color:#3fb950">placed</span>' : l.ev) +
    ' ' + l.qty + ' @ ' + l.px + '¢' +
    (l.note ? ' <span class="sub">— ' + l.note + '</span>' : '') + '</div>').join('');
  document.getElementById('earnBody').innerHTML =
    (function(){
      const e = st.earned_usd || 0, p = st.probe_earned_usd || 0,
            fe = st.flip_earned_usd || 0, t = e + p + fe;
      // Rewards earned against stock we were forced to buy. A fill is the bad
      // outcome here, so the two numbers sit side by side and the net is what
      // actually says whether any of this is working.
      const fc = (st.fill_cost_usd || 0) + ((DATA.probe_scoreboard || {}).fill_cost_usd || 0);
      const nf = (st.fills || 0) + ((DATA.probe_scoreboard || {}).fills || 0);
      return '<div style="font-size:15px;font-weight:700;margin-bottom:2px">earned $' +
        (t >= 0.1 ? t.toFixed(2) : t.toFixed(3)) +
        ' <span class="sub" style="font-weight:400;font-size:11px">in rewards — $' +
        (e >= 0.1 ? e.toFixed(2) : e.toFixed(3)) + ' its bids, $' +
        (p >= 0.1 ? p.toFixed(2) : p.toFixed(3)) +
        ' the prober\\'s scouts (credited to the info fund), $' +
        (fe >= 0.1 ? fe.toFixed(2) : fe.toFixed(3)) +
        ' its flips while they wait to sell</span></div>' +
        '<div style="font-size:13px;margin-bottom:4px;color:' +
        (t - fc >= 0 ? '#8fe3b8' : '#ff9d99') + '">net $' + (t - fc).toFixed(2) +
        ' <span class="sub" style="font-weight:400">after ' + nf + ' fill' +
        (nf === 1 ? '' : 's') + ' costing $' + fc.toFixed(2) +
        ' — fills are losses, resting income is the win</span></div>';
    })() +
    (function(){
      const fl = DATA.earn_flips || [], pend = DATA.earn_toflip || 0;
      if (!fl.length && !pend) return '';
      const rec = st.recovered_usd || 0;
      const fearn = st.flip_earned_usd || 0;
      return '<div style="font-size:11.5px;margin-bottom:4px;color:#f2cd7f">↩ ' +
        (fl.length ? fl.length + ' flip' + (fl.length === 1 ? '' : 's') +
          ' resting (' + fl.reduce((t2, f) => t2 + f.qty, 0) + ' shares)' : '') +
        (pend ? (fl.length ? ' · ' : '') + pend + ' waiting on the position' : '') +
        (rec ? ' · $' + rec.toFixed(2) + ' recovered' : '') +
        (fearn ? ' · $' + fearn.toFixed(2) + ' earned while waiting' : '') +
        '<br><span class="sub">selling back what fills forced on us — inventory, ' +
        'so no buying power, and they earn rewards the whole time they rest</span></div>';
    })() +
    '<div class="sub" style="margin-bottom:4px">' + status +
    ' · searching with $' + (caps.outstanding || 0).toFixed(2) +
    ' of $' + (caps.total || 0).toFixed(0) + ' ($' + (caps.per_mkt || 0).toFixed(0) +
    '/market) · graduated $' + (caps.grad_usd || 0).toFixed(2) +
    ' of $' + (caps.grad_max || 0).toFixed(0) + ' — proven orders keep earning ' +
    'without using the search budget</div>' +
    (rows || '<div class="sub">no bids resting</div>') +
    (lines ? '<details style="margin-top:8px"><summary class="sub" style="cursor:pointer">' +
      'journal (' + log.length + ')</summary>' + lines + '</details>' : '');
}

function swRender(){
  if(!DATA || !DATA.auto) return;
  ['defend','keeper','snipe','probe','earn'].forEach(k=>{
    const b=document.getElementById('sw_'+k); if(!b) return;
    b.disabled=false;
    const on = DATA.auto[k]===true;
    // A switch the server does not report at all is NOT off -- it is unknown.
    // Painting it OFF would hide a running loop, which is how the sniper
    // switch appeared to snap back the moment it was turned on.
    const missing = DATA.auto[k]===undefined;
    b.className='autosw'+(SWARM[k]?' arm':(on?' on':''));
    b.querySelector('.st').textContent =
      SWARM[k] ? 'tap again to turn ON' :
      missing ? 'state not reported — reload' :
      (on ? 'ON — '+SWDESC[k].on : 'OFF — '+SWDESC[k].off);
  });
}
async function swTap(k){
  const on = DATA && DATA.auto && DATA.auto[k]===true;
  if(!on && !SWARM[k]){                      // arming the ON direction
    SWARM[k]=1; swRender();
    setTimeout(()=>{ if(SWARM[k]){ delete SWARM[k]; swRender(); } }, 5000);
    return;
  }
  delete SWARM[k];
  const b=document.getElementById('sw_'+k); if(b) b.disabled=true;
  const r=await act({op:'auto', which:k, on:!on});
  if(r.ok && DATA && DATA.auto) DATA.auto[k]=!on;
  swRender();
  if(!r.ok && b){ b.querySelector('.st').textContent='failed: '+r.msg; b.disabled=false; }
  setTimeout(load, 1500);
}
function tglGaps(){ SHOWGAPS=!SHOWGAPS; render(); }
// --- new order ----------------------------------------------------------
// Placement goes through the same /maction route as everything else, so it
// inherits the key check, the CSRF header, the known-market whitelist, the
// price and size bounds, and post-only (an order that would cross is
// rejected rather than filled on arrival).
const OPENNEW={}, NEWSIDE={};
// results must outlive the re-render that a successful action triggers,
// otherwise the confirmation vanishes the instant it is earned
const MSG={};
function note(key, ok, txt){ MSG[key]={ok:ok, txt:txt};
  const el=document.getElementById(key);
  if(el){ el.className='res '+(ok?'ok':'err'); el.textContent=txt; } }
function msgHTML(key){ const m=MSG[key]; return m? ` class="res ${m.ok?'ok':'err'}">${m.txt}` : '>'; }
function tglNew(slug){ OPENNEW[slug]=!OPENNEW[slug]; if(SEL) detail(SEL); }
function nside(slug, s){ NEWSIDE[slug]=s; if(SEL) detail(SEL); }
function newHTML(slug, fair){
  const id=cssid(slug), side=NEWSIDE[slug]||'BUY';
  const b=BOOKS[slug];
  // default to a price that rests rather than one that would be rejected:
  // a tick inside the touch on the side being quoted
  let sug='';
  if(b && !b.error){
    const tick=(b.tick||0.01)*100;
    const bestBid=(b.bids||[]).length? Math.max(...b.bids.map(r=>r[0]))*100 : null;
    const bestAsk=(b.asks||[]).length? Math.min(...b.asks.map(r=>r[0]))*100 : null;
    if(side==='BUY'  && bestBid!=null) sug=(bestBid+tick).toFixed(1);
    if(side==='SELL' && bestAsk!=null) sug=(bestAsk-tick).toFixed(1);
    if(side==='BUY'  && bestAsk!=null && sug && parseFloat(sug)>=bestAsk) sug=(bestAsk-tick).toFixed(1);
    if(side==='SELL' && bestBid!=null && sug && parseFloat(sug)<=bestBid) sug=(bestBid+tick).toFixed(1);
  }
  const warn = (fair!=null && sug) ? (()=>{
      const e = side==='BUY' ? (fair*100-parseFloat(sug)) : (parseFloat(sug)-fair*100);
      return e < -10 ? `<div class="hint neg">that price is ${Math.abs(e).toFixed(1)}c the wrong
        side of the model — a fill would cost that per share</div>` : '';
    })() : '';
  return `<div class="newbox">
    <div class="ttl">new order</div>
    <div class="seg">
      <button class="buy ${side==='BUY'?'on':''}"  onclick="nside('${slug}','BUY')">BUY</button>
      <button class="sell ${side==='SELL'?'on':''}" onclick="nside('${slug}','SELL')">SELL</button>
    </div>
    <div class="nrow">
      <input id="np_${id}" type="number" inputmode="decimal" step="0.1" min="0.1" max="99.9"
             value="${sug}" placeholder="price" aria-label="price in cents"><span class="unit">c</span>
      <input id="nq_${id}" type="number" inputmode="numeric" step="1" min="1" max="20000"
             placeholder="size" aria-label="size"><span class="unit">sh</span>
      <button class="btn new" onclick="place('${slug}')">Place</button>
    </div>
    ${warn}
    <div class="hint">${b&&!b.error?'Suggested price is one tick inside the touch. ':
      'Open the book to get a suggested price. '}Post-only: if it would cross it is
      rejected, never filled on arrival.</div>
    <div id="nr_${id}"${msgHTML('nr_'+id)}</div>
  </div>`;
}
async function place(slug){
  const id=cssid(slug);
  const c=parseFloat((document.getElementById('np_'+id)||{}).value);
  const q=parseInt((document.getElementById('nq_'+id)||{}).value,10);
  const say=(ok,msg)=>note('nr_'+id, ok, msg);
  if(!(c>=0.1&&c<=99.9)) return say(false,'price must be between 0.1 and 99.9c');
  if(!(q>=1&&q<=20000))  return say(false,'size must be between 1 and 20,000');
  say(true,'placing…');
  const r=await act({op:'place', market:slug, side:NEWSIDE[slug]||'BUY',
                     price_cents:c, size:q});
  say(r.ok, r.ok ? `placed ${NEWSIDE[slug]||'BUY'} ${q.toLocaleString()} @ ${c.toFixed(1)}c` : r.msg);
  // refresh rather than drop: the price suggestion in this very form is
  // derived from the cached book, and dropping it blanks the field
  if(r.ok){ if(BOOKS[slug]) reBook(slug); setTimeout(load, 2500); }
}

// --- order book ---------------------------------------------------------
// /market.json already returns the top of book, our orders in it and the
// position, behind the same key check. Reusing it keeps one fetch path for
// book data instead of a second one that could drift.
const BOOKS={}, OPENBK={};
function cssid(s){ return s.replace(/[^A-Za-z0-9_-]/g,'_'); }
async function fetchBook(slug){
  try{
    const r = await fetch('/market.json?slug='+encodeURIComponent(slug), {headers:hdrs()});
    BOOKS[slug] = r.ok ? await r.json() : {error:'HTTP '+r.status};
  }catch(e){ BOOKS[slug] = {error:'offline'}; }
}
async function tglBook(slug){
  OPENBK[slug] = !OPENBK[slug];
  if(OPENBK[slug] && !BOOKS[slug]){
    const el=document.getElementById('bk_'+cssid(slug));
    if(el) el.innerHTML = '<div class="muted" style="padding:8px 0">loading book…</div>';
    await fetchBook(slug);
  }
  if(SEL) detail(SEL);
}
async function reBook(slug){ await fetchBook(slug); if(SEL) detail(SEL); }
function bookHTML(slug, fair){
  const b = BOOKS[slug];
  if(!b) return '<div class="muted" style="padding:8px 0">loading book…</div>';
  if(b.error) return `<div class="muted" style="padding:8px 0">book unavailable — ${b.error}</div>`;
  const asks=(b.asks||[]).slice(), bids=(b.bids||[]).slice();
  if(!asks.length && !bids.length)
    return '<div class="muted" style="padding:8px 0">no resting size on either side</div>';
  // our own size at each price, so a level we are in is obvious at a glance
  const mineAt={};
  (b.orders||[]).forEach(o=>{ const key=(o.side||'')+'@'+Math.round(o.price*1000);
                              mineAt[key]=(mineAt[key]||0)+(o.size||0); });
  const mx = Math.max(...asks.map(r=>r[1]), ...bids.map(r=>r[1]), 1);
  const row=(p,q,side)=>{
    const key=(side==='ask'?'SELL':'BUY')+'@'+Math.round(p*1000);
    const mineQ=mineAt[key]||0;
    return `<div class="brow ${side} ${mineQ?'me':''}">
      <span class="px">${(p*100).toFixed(1)}c</span>
      <span class="bar" style="width:${Math.max(2,(q/mx)*100).toFixed(1)}%"></span>
      <span class="qt">${q.toLocaleString()}${mineQ?`<br>you ${Math.round(mineQ).toLocaleString()}`:''}</span>
    </div>`;
  };
  // one continuous ladder, highest price at the top, with the model's own
  // price slotted in where it belongs so "which side of fair are we on" is
  // a matter of looking rather than arithmetic
  const fairC = fair==null ? null : fair;
  let rows=[];
  asks.sort((a,b)=>b[0]-a[0]).forEach(r=>rows.push({p:r[0],q:r[1],s:'ask'}));
  const bestAsk = asks.length? Math.min(...asks.map(r=>r[0])) : null;
  const bestBid = bids.length? Math.max(...bids.map(r=>r[0])) : null;
  bids.sort((a,b)=>b[0]-a[0]).forEach(r=>rows.push({p:r[0],q:r[1],s:'bid'}));
  let out='<div class="book">';
  let placedFair=false, placedSpread=false;
  rows.forEach((r,i)=>{
    if(fairC!=null && !placedFair && r.p <= fairC){
      out += `<div class="fair">model ${(fairC*100).toFixed(1)}c</div>`; placedFair=true; }
    if(!placedSpread && r.s==='bid' && bestAsk!=null && bestBid!=null){
      out += `<div class="spread">spread ${((bestAsk-bestBid)*100).toFixed(1)}c</div>`;
      placedSpread=true; }
    out += row(r.p,r.q,r.s);
  });
  if(fairC!=null && !placedFair) out += `<div class="fair">model ${(fairC*100).toFixed(1)}c</div>`;
  out += '</div>';
  if(b.net) out += `<div class="hint">position: ${Math.round(b.net).toLocaleString()} contracts</div>`;
  out += `<div class="hint">Top ${Math.max(asks.length,bids.length)} levels a side.
    <a href="#" onclick="event.preventDefault();reBook('${slug}')">refresh</a></div>`;
  return out;
}

// Every write goes through /maction, which already carries the auth check,
// the X-Reprice CSRF header requirement, the 0.1-99.9c price bounds and the
// crossing guard. A new endpoint here would mean re-earning all of that.
async function act(body){
  const h = hdrs(); h.set('Content-Type','application/json'); h.set('X-Reprice','1');
  const r = await fetch('/maction', {method:'POST', headers:h, body:JSON.stringify(body)});
  let j={}; try{ j = await r.json(); }catch(e){}
  return {ok: r.ok && j.ok !== false, msg: j.error || j.note || (r.ok?'done':'HTTP '+r.status)};
}
function show(id, ok, msg){ note('r_'+id, ok, msg); }
function setp(id, c){ const el=document.getElementById('p_'+id); if(el) el.value=c.toFixed(1); }
function busy(id, on){
  ['p_','q_','c_'].forEach(p=>{ const e=document.getElementById(p+id); if(e) e.disabled=on; });
  const b=document.querySelector('#o_'+id+' .btn.mv'); if(b){ b.disabled=on; b.textContent=on?'…':'Move'; }
}
async function mv(id){
  const el=document.getElementById('p_'+id); if(!el) return;
  const c=parseFloat(el.value);
  const q=parseInt((document.getElementById('q_'+id)||{}).value,10);
  if(!(c>=0.1 && c<=99.9)) return show(id,false,'price must be between 0.1 and 99.9c');
  if(!(q>=1 && q<=20000))  return show(id,false,'size must be between 1 and 20,000');
  busy(id,true);
  const r=await act({op:'modify', order_id:id, price_cents:c, size:q});
  busy(id,false);
  show(id, r.ok, r.ok ? `now ${q.toLocaleString()} @ ${c.toFixed(1)}c` : r.msg);
  if(r.ok) setTimeout(load, 2500);
}
// two taps to cancel: this is a phone, and a mis-tap here removes a real order
const ARM={};
async function cx(id){
  const b=document.getElementById('c_'+id); if(!b) return;
  if(!ARM[id]){ ARM[id]=1; b.classList.add('arm'); b.textContent='Sure?';
    setTimeout(()=>{ if(ARM[id]){ delete ARM[id]; b.classList.remove('arm'); b.textContent='Cancel'; } }, 4000);
    return; }
  delete ARM[id]; b.classList.remove('arm'); b.textContent='…'; busy(id,true);
  const r=await act({op:'cancel', order_id:id});
  busy(id,false); b.textContent='Cancel';
  show(id, r.ok, r.ok ? 'cancelled' : r.msg);
  if(r.ok) setTimeout(load, 2500);
}
function setFilter(k){ FILTER = (FILTER===k? null : k); render(); }
function pick(ab){ SEL=ab; render(); detail(ab);
  document.getElementById('det').scrollIntoView({behavior:'smooth',block:'nearest'}); }

function detail(ab){
  const s = DATA.states.find(x=>x.abbr===ab);
  const d = document.getElementById('det');
  if(!s){ d.style.display='none'; return; }
  d.style.display='block';
  let h = `<h2>${s.name||s.abbr}</h2><div class="why">${s.why}</div>`;
  h += `<div class="row"><span>resting orders</span><b>${s.orders}</b></div>`;
  h += `<div class="row"><span>estimated rate</span><b>${money(s.est_day)}/day</b></div>`;
  h += `<div class="row"><span>earned today</span><b class="${
    (s.implied>0 && s.earned < 0.25*s.implied)?'neg':''}">${money(s.earned)}</b></div>`;
  if(s.implied>0) h += `<div class="row"><span>estimate implied by now</span>
    <b>${money(s.implied)} over ${s.covered_h}h measured</b></div>`;
  ['senate','governor'].forEach(off=>{
    const o = s.offices[off]; if(!o) return;
    h += `<div class="off"><h3>${off}</h3>`;
    if(o.dem!=null) h += `<div class="row"><span>model</span><b>D ${(o.dem*100).toFixed(1)}% ·
      R ${(o.rep*100).toFixed(1)}%</b></div>`;
    h += `<div class="row"><span>orders / rate</span><b>${o.orders} · ${money(o.est_day)}/day</b></div>`;
    const mk = Object.keys(o.markets||{});
    if(!mk.length) h += `<div class="muted" style="padding-top:4px">no orders here</div>`;
    mk.sort().forEach(k=>{
      const m=o.markets[k];
      const e=m.worst_edge;
      const tag = e==null ? '' :
        `<span class="${e<0?'neg':'pos'}">${e<0?'':'+'}${(e*100).toFixed(1)}c vs model</span>`;
      const dead = (m.paying===false);
      h += `<div class="mkt"><code>${k}</code>${dead?
        `<div class="deadmk">not paying — ${money(m.earned)} in against ${money(m.implied)}
         implied by the ${money(m.est_day)}/day estimate</div>`:''}<div class="row">
        <span>${m.orders} order${m.orders===1?'':'s'} · ${money(m.est_day)}/day</span>${tag}</div>
        <button class="bkbtn" onclick="tglBook('${k}')">${OPENBK[k]?'hide book':'show book'}</button>
        <button class="bkbtn" onclick="tglNew('${k}')">${OPENNEW[k]?'close':'new order'}</button>
        <div id="bk_${cssid(k)}">${OPENBK[k]?bookHTML(k, m.fair):''}</div>
        <div id="nw_${cssid(k)}">${OPENNEW[k]?newHTML(k, m.fair):''}</div>`;
      // one actionable row per resting order. The model's own price sits on
      // the button, so moving an order to fair value is a single tap rather
      // than mental arithmetic on a phone.
      (m.list||[]).slice().sort((a,b)=>(a.edge??0)-(b.edge??0)).forEach(od=>{
        if(!od.id) return;
        const fc = m.fair==null ? null : (m.fair*100);
        const ed = od.edge;
        h += `<div class="ord" id="o_${od.id}">
          <div class="ordhd">
            <span><span class="side">${od.side}</span> <b>${(od.price*100).toFixed(1)}c</b>
              &times; ${od.size.toLocaleString()}</span>
            <span>${money(od.est_day)}/day ${ed==null?'':
              `<span class="${ed<0?'neg':'pos'}">${ed<0?'':'+'}${(ed*100).toFixed(1)}c</span>`}</span>
          </div>
          <div class="ctl">
            <input id="p_${od.id}" type="number" inputmode="decimal" step="0.1" min="0.1" max="99.9"
                   value="${(od.price*100).toFixed(1)}" aria-label="new price in cents">
            <span class="unit">c</span>
            <input id="q_${od.id}" type="number" inputmode="numeric" step="1" min="1" max="20000"
                   value="${od.size}" aria-label="new size">
            <span class="unit">sh</span>
          </div>
          <div class="ctl">
            <button class="btn mv" onclick="mv('${od.id}')">Move</button>
            ${(fc==null || !(ed<0))?'':`<button class="btn"
               style="background:var(--surface2);color:var(--ink)"
               onclick="setp('${od.id}',${fc.toFixed(1)})">model ${fc.toFixed(1)}c</button>`}
            <button class="btn cx" id="c_${od.id}" onclick="cx('${od.id}')">Cancel</button>
          </div>
          <div class="hint">${(ed!=null && ed>=0)
            ? 'Right side of the model already, so no shortcut button. ' : ''}Places,
            waits until it rests, then cancels this one. An increase only retires the
            old order if the new one rests at full size.</div>
          <div id="r_${od.id}"${msgHTML('r_'+od.id)}</div>
        </div>`;
      });
      h += `</div>`;
    });
    h += `</div>`;
  });
  d.innerHTML = h;
}
load();
// Do not refresh out from under someone mid-edit: re-rendering rebuilds the
// detail panel and would silently discard a price being typed, or a cancel
// that is armed and waiting for its second tap.
setInterval(()=>{
  const a=document.activeElement;
  if(a && (a.tagName==='INPUT' || a.tagName==='BUTTON')) return;
  if(Object.keys(ARM).length) return;
  load();
}, 60000);
</script></body></html>"""


DASH_HTML = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rewards</title>
<meta name="theme-color" content="#1a202b">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Rewards">
<link rel="manifest" href="/manifest.json">
<link rel="apple-touch-icon" href="/icon.png">
<style>
 :root{
  --bg:#1a202b; --surface:#232b38; --surface2:#2c3543; --line:#3a4454;
  --ink:#eef2f7; --ink2:#a7b1c2; --ink3:#707d92;
  --good:#34c07c; --bad:#e5645f; --warn:#d9a132; --accent:#5aa2ff;
  --r:14px;
 }
 *{box-sizing:border-box}
 html{-webkit-text-size-adjust:100%}
 body{font-family:-apple-system,system-ui,'Segoe UI',sans-serif;margin:0;
  padding:14px 14px calc(76px + env(safe-area-inset-bottom));
  background:var(--bg);color:var(--ink)}
 .big{font-size:52px;font-weight:800;letter-spacing:-1px;margin:2px 0;
  font-variant-numeric:tabular-nums}
 .sub{color:var(--ink2);font-size:13px;line-height:1.45}
 .err{background:rgba(229,100,95,.14);color:#ffb3af;padding:10px 14px;border-radius:12px;margin:10px 0;display:none;font-size:13px}
 .card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);
  padding:12px 14px;margin:12px 0}
 .card h3{margin:0 0 6px}
 table{width:100%;border-collapse:collapse;margin-top:8px;font-size:13px}
 td,th{padding:8px 4px;text-align:left;border-bottom:1px solid var(--line)}
 tr:last-child td{border-bottom:none}
 th{color:var(--ink2);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.4px}
 td.r,th.r{text-align:right}
 .mkt{color:var(--ink2);font-size:11px;word-break:break-all;line-height:1.5}
 h3{margin:20px 0 4px;font-size:15px;font-weight:700}
 h3 .sub{font-weight:400}
 .bk{width:auto;min-width:60%;margin:6px 0;font-family:ui-monospace,SFMono-Regular,monospace;font-size:12px}
 .bk td{padding:2px 10px 2px 0;border-bottom:none;color:var(--ink2)}
 .bk tr.me td{color:var(--accent);font-weight:600}
 .calc{font-family:ui-monospace,SFMono-Regular,monospace;font-size:12px;color:var(--ink);margin:2px 0}
 .ord{margin:8px 0 14px}
 .oh{font-size:12px;color:var(--ink);margin-bottom:2px}
 .rp{margin:8px 0;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
 input[type=number],input[type=password],input[type=text],select{
  background:var(--surface2);color:var(--ink);border:1px solid var(--line);
  border-radius:10px;padding:9px 10px;font-size:15px;min-height:40px}
 .rp input{width:76px}
 button{font-family:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
 .rp button, .ctlrow button{background:var(--good);color:#0b2417;font-weight:600;border:none;
  border-radius:10px;padding:10px 14px;font-size:14px;min-height:40px}
 button.alt{background:rgba(10,14,20,.45);color:var(--ink2);font-weight:500;
  border:1px solid var(--line);border-radius:10px;padding:9px 13px;font-size:14px;min-height:40px}
 button.armed{background:var(--warn) !important;color:#241a05 !important}
 .tab{background:var(--surface2);color:var(--ink2);border:1px solid var(--line);
  border-radius:10px;padding:9px 14px;font-size:13px;min-height:38px}
 .tab.on{background:var(--good);border-color:var(--good);color:#0b2417;font-weight:600}
 .pos{color:var(--good)} .neg{color:var(--bad)}
 .bdg{background:#1c3252;color:#79b8ff;border-radius:6px;padding:2px 7px;font-size:10px;vertical-align:middle}
 input[type=range]{accent-color:var(--good)}
 /* bottom navigation */
 .nav{position:fixed;left:0;right:0;bottom:0;z-index:20;display:flex;
  background:rgba(26,32,43,.96);backdrop-filter:blur(12px);
  border-top:1px solid var(--line);padding:6px 8px calc(6px + env(safe-area-inset-bottom))}
 .nb{flex:1;background:none;border:none;color:var(--ink3);font-size:11px;
  padding:7px 0 5px;border-radius:12px;display:flex;flex-direction:column;
  align-items:center;gap:2px;min-height:48px}
 .nb span{font-size:21px;line-height:1}
 .nb.on{color:var(--good);background:rgba(52,192,124,.12)}
 #moreMenu{position:fixed;right:10px;bottom:calc(72px + env(safe-area-inset-bottom));
  z-index:21;background:var(--surface);border:1px solid var(--line);border-radius:14px;
  padding:6px;box-shadow:0 12px 40px rgba(0,0,0,.5);min-width:170px}
 #moreMenu button{display:flex;width:100%;background:none;border:none;color:var(--ink);
  font-size:15px;padding:12px 14px;border-radius:10px;gap:10px;align-items:center}
 #moreMenu button:active{background:var(--surface2)}
 /* one-time login */
 #login{position:fixed;inset:0;z-index:40;background:var(--bg);display:none;
  align-items:center;justify-content:center;flex-direction:column;gap:14px;padding:24px}
 #login .big{font-size:26px}
 #login input{width:min(320px,80vw);text-align:center;font-size:18px}
 #login button{background:var(--good);color:#0b2417;font-weight:700;border:none;
  border-radius:12px;padding:13px 34px;font-size:16px}
 button.armed{background:var(--warn) !important;color:#241a05 !important;font-weight:700}
 .osub{background:var(--surface2);border-radius:12px;padding:10px 12px;margin:10px 0}
 .ctlrow{display:flex;gap:8px;align-items:center;margin-top:8px;flex-wrap:wrap}
 .ctl{display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
 .ctl label{font-size:10px;color:var(--ink3);text-transform:uppercase;letter-spacing:.4px;margin-right:2px}
 .ctl input{width:76px}
 .bump{min-width:42px;padding:9px 0 !important;text-align:center}
 #toast{position:fixed;left:50%;transform:translateX(-50%);
  bottom:calc(86px + env(safe-area-inset-bottom));background:var(--surface2);
  color:var(--ink);padding:11px 18px;border-radius:99px;border:1px solid var(--line);
  box-shadow:0 8px 30px rgba(0,0,0,.35);opacity:0;transition:opacity .25s;
  z-index:50;pointer-events:none;max-width:86vw;font-size:14px}
 #toast.show{opacity:1}
 .hero{margin:2px 0 0}
 .chips{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 2px}
 .chip{background:var(--surface2);border:1px solid var(--line);color:var(--ink2);
  border-radius:99px;padding:6px 12px;font-size:12px;min-height:0}
 .chipon{border-color:var(--good);color:var(--good)}
</style></head><body>
<div id="login">
 <div class="big">Liquidity rewards</div>
 <div class="sub">Enter your dashboard password once — this device remembers it.</div>
 <input id="loginKey" type="password" placeholder="password" autocomplete="current-password"
        onkeydown="if(event.key==='Enter')doLogin()">
 <button onclick="doLogin()">Open dashboard</button>
</div>
<nav class="nav">
 <button class="nb on" id="tabH" onclick="showTab('H')"><span>⌂</span>Home</button>
 <button class="nb" id="tabR" onclick="showTab('R')"><span>▤</span>Markets</button>
 <button class="nb" id="tabP" onclick="showTab('P')"><span>◆</span>Positions</button>
 <button class="nb" id="tabM" onclick="toggleMore()"><span>⋯</span>More</button>
</nav>
<div id="moreMenu" style="display:none">
 <button onclick="showTab('L')">🧭 Plan &amp; Restore</button>
 <button onclick="showTab('S')">↔️ Spreads</button>
 <button onclick="showTab('E')">🏛 Seats</button>
 <button onclick="location.href='/map'">🗺 Map</button>
 <button onclick="location.href='/lab'">🔬 Prober &amp; Earner</button>
</div>
<div id="viewE" style="display:none">
<div class="sub">Seat-count ladders — House &amp; Senate, in seat order</div>
<div style="margin:6px 0"><button class="tab" onclick="SEATSD=null;loadSeats()">↻ Refresh</button></div>
<div class="err" id="seatErr"></div>
<div id="seatWrap"></div>
<div class="mkt" style="margin-top:8px">★ = that order is the best price on its side right
now; "behind" means someone is ahead of you. Own = contracts held @ average cost. Your
qualifier quotes (the floor bid and ceiling ask) are hidden from the order list. A side pays
NOBODY until it holds Target Size — each row shows bid/ask depth vs target, and ⚓ places the
cheapest possible orders (floor bid / ceiling ask) sized to exactly close the gap;
"Qualify all missing" does a whole ladder. Tap any row to place, modify or cancel. Books
load in batches — if a row shows "…", refresh once.</div>
</div>
<div id="viewS" style="display:none">
<div class="sub">Widest politics spreads — enter ONE tick inside both sides <span id="spGen"></span></div>
<div style="margin:10px 0">Min spread: <b id="spCutLbl">25¢</b>
 <input type="range" id="spCutSlider" min="2" max="80" value="25" style="width:55%;vertical-align:middle"
        oninput="spCut(this.value)"></div>
<div style="margin:6px 0">
 <button class="tab" onclick="spAll(true)">Select all</button>
 <button class="tab" onclick="spAll(false)">Clear</button></div>
<div class="sub" id="spSel"></div>
<div class="err" id="spErr"></div>
<table id="sptab"></table>
<div class="rp" style="margin-top:10px">
 <button onclick="spPlace()">Enter selected (both sides)</button>
 <button class="alt" onclick="abortBatch()">Stop batch</button></div>
<div id="spProg" class="mkt" style="margin:8px 0"></div>
<div class="mkt">Each entry quotes BOTH sides of the spread, post-only, sized to the reward
Target Size (clamped to your per-market buying power, split across the two sides). At
placement each order is re-optimized against the LIVE book for maximum reward per dollar:
it joins the touch when that's cheapest, or steps 1-2 ticks inside when pushing competitors
a tick deeper multiplies your share more than the extra capital costs. Quoting at or near
the touch means you can FILL: if both sides fill you pocket the spread; if one fills you own
the position. Markets whose spread has closed below 3 ticks are skipped.</div>
</div>
<div id="viewH">
<div class="hero">
<div class="sub">Earned today</div>
<div class="big" id="earned">…</div>
<div class="sub" id="rate"></div>
<div class="sub" id="pace" style="margin-top:2px"></div>
<div class="sub" id="fresh" style="margin-top:2px"></div>
<div class="err" id="err"></div>
<div id="ovg" style="margin:10px 0"></div>
</div>
<div class="card">
<h3>Since you last checked <button class="tab" style="font-size:11px;padding:5px 12px;min-height:0" onclick="clearTxns()">Clear</button></h3>
<table id="txns"></table>
</div>
<div class="card">
<h3>Biggest drops <span class="sub">(vs their ~8h peak)</span></h3>
<table id="drops"></table>
</div>
<div class="card">
<h3>Earners you're not in <span class="sub">(paid you before · nothing resting now)</span></h3>
<table id="winners"></table>
</div>
<div class="card">
<h3>New markets <span class="sub">(golf shown per tournament)</span></h3>
<table id="newm"></table>
</div>
<div class="mkt" style="margin-top:8px">Tap any market to place, modify or cancel an order there.</div>
<div class="mkt" id="updated" style="margin-top:6px"></div>
</div>
<div id="viewR" style="display:none">
<div style="margin:8px 0"><button class="tab" onclick="loadReprice()">⚡ Optimize prices</button>
 <button class="tab" onclick="loadDead()">🧹 Cancel dead orders</button>
 <span class="sub" style="margin-left:8px">distance:
  <label><input type="radio" name="qdist" value="0"> join</label>
  <label><input type="radio" name="qdist" value="1" checked> 1 back</label>
  <label><input type="radio" name="qdist" value="2"> 2 back</label></span></div>
<div id="rpl"></div>
<div id="rpProg" class="mkt"></div>
<div class="card">
<h3>By market <span class="sub">(tap a row for the math)</span></h3>
<div id="catBar" style="margin:4px 0"></div>
<table id="markets"></table>
</div>
<div class="card">
<h3>Previous days</h3><table id="history"></table>
</div>
<div id="acts"></div>
</div>
<div id="viewP" style="display:none">
<div class="sub">Positions — take-profit ask one tick inside the best ask</div>
<div class="sub" id="posSub"></div>
<div style="margin:6px 0">
 <button class="tab" onclick="posFixAll()">Price all flagged</button>
 <button class="tab" onclick="loadPositions()">↻ Refresh</button></div>
<div class="err" id="posErr"></div>
<table id="posList"></table>
<div id="posProg" class="mkt" style="margin:6px 0"></div>
<h3>Race risk <span class="sub">(worst / best case per race — negative-risk check)</span></h3>
<table id="raceList"></table>
<div class="mkt">Two kinds of race: one-winner fields (candidates, exact seat counts —
exactly one resolves YES) and THRESHOLD ladders (House ≥N brackets — every threshold at or
under the result resolves YES together). Threshold races are scored by the RANGE the final
count lands in; one-winner races by the winning outcome, including ones you don't hold.
🔒 = even the worst scenario beats your total cost: guaranteed profit however it lands.</div>
<div class="mkt" style="margin-top:8px">Green: the whole position has a resting exit that IS
the best price on its side — nothing to worry about. Red: no exit resting, partial coverage,
or you've been undercut — the button places (or reprices) a post-only exit of the full
position one tick inside the touch: a SELL for longs, a BUY-BACK for shorts (No positions,
shown in orange). Gray: the spread leaves no room to price inside — wait for it to widen.
Exiting inventory locks no new capital.</div>
</div>
<div id="viewL" style="display:none">
<div class="sub">Passive placement plan <span id="planGen"></span></div>
<div style="margin:8px 0">
 <label class="sub"><input type="radio" name="pwhich" value="politics" checked onchange="switchPlan()"> Politics</label>
 <label class="sub"><input type="radio" name="pwhich" value="golf" onchange="switchPlan()"> Golf (cheap YES)</label>
 <label class="sub"><input type="radio" name="pwhich" value="tt" onchange="switchPlan()"> Table tennis (1@touch)</label>
 <label class="sub"><input type="radio" name="pwhich" value="restore" onchange="switchPlan()"> Restore</label></div>
<div style="margin:10px 0;display:none" id="restoreRow">Restore what was resting:
 <button class="tab" onclick="setRago(900)">15m</button>
 <button class="tab" onclick="setRago(1800)">30m</button>
 <button class="tab" onclick="setRago(3600)">1h</button>
 <button class="tab" onclick="setRago(7200)">2h</button>
 <button class="tab" onclick="setRago(14400)">4h</button> ago</div>
<div class="sub" id="planBP"></div>
<div style="margin:10px 0">Max buy price: <b id="capLbl">10¢</b>
 <input type="range" id="capSlider" min="1" max="99" value="10" style="width:55%;vertical-align:middle"
        oninput="planCap(this.value)"></div>
<div style="margin:10px 0">Min sell price: <b id="sellLbl">85¢</b>
 <input type="range" id="sellSlider" min="10" max="99" value="85" style="width:55%;vertical-align:middle"
        oninput="planSell(this.value)"></div>
<div style="margin:10px 0;display:none" id="golfCapRow">Max $ per golfer: <b id="golfCapLbl">$1.00</b>
 <input type="range" id="golfCapSlider" min="25" max="1000" step="25" value="100" style="width:55%;vertical-align:middle"
        oninput="golfCap(this.value)"></div>
<div style="margin:10px 0" id="polCapRow">Max $ locked per market: <b id="polCapLbl">off (buying power only)</b>
 <input type="range" id="polCapSlider" min="5" max="205" step="5" value="205" style="width:55%;vertical-align:middle"
        oninput="polCapSet(this.value)"></div>
<div style="margin:6px 0">
 <label class="sub"><input type="checkbox" id="hideRisk" checked onchange="renderPlan()"> hide ⚠ risky</label>
 &nbsp; <label class="sub"><input type="radio" name="szmode" value="pick" checked onchange="renderPlan()"> minimal size</label>
 <label class="sub"><input type="radio" name="szmode" value="max" onchange="renderPlan()"> full size (20k)</label></div>
<div style="margin:6px 0">
 <button class="tab" onclick="planAll(true)">Select all shown</button>
 <button class="tab" onclick="planAll(false)">Clear</button></div>
<div class="sub" id="planSel"></div>
<div class="err" id="planErr"></div>
<table id="plan"></table>
<div class="rp" style="margin-top:10px">
 <button onclick="placeBatch()">Place selected</button>
 <button class="alt" onclick="abortBatch()">Stop batch</button></div>
<div id="placeProg" class="mkt" style="margin:8px 0"></div>
<div class="mkt">Every order is post-only — it can never cross the spread and fill on
placement. Each is revalidated against the live book just before placing; anything that
drifted below ~$0.08/day is skipped, and same-side orders already resting within 1¢ are
never doubled up (✔ = market you're already in). Capital = price for buys, max loss
(100¢ − price) for shorts, nothing for sells covered by inventory (📦 — placed as
sell-your-position, doubling as a take-profit). Sells you aren't covered for are shorts:
they win if the outcome doesn't happen and lose up to 100¢ − price per contract if it
does.</div>
<div style="margin-top:26px;border-top:1px solid var(--line);padding-top:12px">
 <button class="tab" style="background:rgba(229,100,95,.18);color:#ff9d99" onclick="cancelAll()">⚠ Cancel ALL open orders</button>
</div>
</div>
<div id="sheet" style="display:none;position:fixed;inset:0;background:rgba(9,12,18,.88);overflow:auto;z-index:30" onclick="closeSheet()">
 <div id="sheetIn" style="max-width:560px;margin:18px auto calc(90px + env(safe-area-inset-bottom));background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:16px" onclick="event.stopPropagation()"></div>
</div>
<script>
// Every request carries the remembered key — sign in once, never again.
const _fetch = window.fetch.bind(window);
window.fetch = function(url, opts){
  opts = opts || {};
  const h = new Headers(opts.headers || {});
  h.set('X-Dash-Key', localStorage.getItem('dashKey') || '');
  opts.headers = h;
  return _fetch(url, opts).then(r => { if(r.status === 401) showLogin(); return r; });
};
function showLogin(){
  document.getElementById('login').style.display = 'flex';
  setTimeout(() => document.getElementById('loginKey').focus(), 50);
}
function doLogin(){
  const v = document.getElementById('loginKey').value.trim();
  if(!v) return;
  localStorage.setItem('dashKey', v);
  document.getElementById('login').style.display = 'none';
  refresh();
}
let OPEN = {}, GOPEN = {}, SERIES = null, RATES = {};
let LAST_OK = 0;
function toast(msg){
  let t = document.getElementById('toast');
  if(!t){ t = document.createElement('div'); t.id = 'toast'; document.body.appendChild(t); }
  t.textContent = String(msg); t.classList.add('show');
  clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('show'), 2600);
}
// two-tap confirm: first tap turns THE BUTTON into an amber 'Confirm?',
// second tap on the same button within 5s executes; anything else disarms
let ARMK = '', ARMT = 0, ARMBTN = null, ARMOLD = '';
function disarm(){
  if(ARMBTN){ ARMBTN.innerHTML = ARMOLD; ARMBTN.classList.remove('armed'); }
  ARMBTN = null; ARMK = '';
}
function arm(key, msg){
  if(ARMK === key && Date.now() - ARMT < 5000){ disarm(); return true; }
  disarm();
  ARMK = key; ARMT = Date.now();
  const ev = window.event;
  const b = ev && ev.target && ev.target.closest ? ev.target.closest('button') : null;
  if(b){
    ARMBTN = b; ARMOLD = b.innerHTML;
    b.innerHTML = 'Confirm?'; b.classList.add('armed');
    setTimeout(() => { if(ARMK === key && Date.now() - ARMT >= 4900) disarm(); }, 5100);
  }
  if(msg) toast(msg);
  return false;
}
let PSY = null;
document.addEventListener('touchstart', e => { PSY = (window.scrollY <= 0) ? e.touches[0].clientY : null; }, {passive: true});
document.addEventListener('touchend', e => {
  if(PSY != null && e.changedTouches[0].clientY - PSY > 90){ refresh(); toast('Refreshed'); }
  PSY = null;
}, {passive: true});
// The big number ticks LIVE and SMOOTHLY: it advances at a displayed rate
// that eases toward the real rate over ~10s, while a gentle rolling pull
// keeps it converging on the server's figure — no visible jumps at
// refresh, no jerks when the rate changes, and it never runs backward
// (it just slows until reality catches up). Hard reset only on day
// rollover or a large correction.
let SRV_E = null, SRV_R = 0, SRV_TS = 0;
let DISP = null, DR = 0, TICK_TS = 0;
function setEarned(v, rate){
  SRV_E = v; SRV_R = rate || 0; SRV_TS = Date.now();
}
setInterval(function(){
  if(SRV_E == null) return;
  const el = document.getElementById('earned');
  if(!el) return;
  const now = Date.now();
  const dt = TICK_TS ? Math.min((now - TICK_TS) / 1000, 2) : 0.15;
  TICK_TS = now;
  const target = SRV_E + SRV_R * (now - SRV_TS) / 86400000;
  if(DISP == null || Math.abs(target - DISP) > 2){
    DISP = target; DR = SRV_R;           // rollover / big correction: snap
  } else {
    DR += (SRV_R - DR) * 0.02;           // rate eases in over ~10s
    let next = DISP + DR * dt / 86400 + (target - DISP) * 0.006;
    if(next < DISP){                     // anchor moved us down: sag gently
      next = DISP + (target - DISP) * 0.001;
      if(next > DISP) next = DISP;
    }
    DISP = next;
  }
  const s = Math.max(DISP, 0).toFixed(4);
  el.innerHTML = '$' + s.slice(0, -2) +
    '<span style="font-size:.45em;color:var(--ink2);font-weight:600">' + s.slice(-2) + '</span>';
}, 150);
setInterval(function(){
  const el = document.getElementById('fresh');
  if(!el || !LAST_OK) return;
  const s = Math.round((Date.now() - LAST_OK)/1000);
  el.innerHTML = s < 45 ? '<span style="color:var(--good)">●</span> live · updated '+s+'s ago'
    : s < 150 ? '<span style="color:var(--warn)">●</span> updating… last data '+s+'s ago'
    : '<span style="color:var(--bad)">●</span> stale — last data '+Math.round(s/60)+'m ago';
}, 1000);
let SEEN = JSON.parse(localStorage.getItem('seenRates') || '{}');
function showTab(t){
  ['H','R','P','L','S','E'].forEach(k => {
    const v = document.getElementById('view'+k);
    if(v) v.style.display = k===t ? '' : 'none';
    const b = document.getElementById('tab'+k);
    if(b) b.className = 'nb' + (k===t ? ' on' : '');
  });
  const more = document.getElementById('tabM');
  if(more) more.className = 'nb' + ('LSE'.indexOf(t) >= 0 ? ' on' : '');
  const mm = document.getElementById('moreMenu');
  if(mm) mm.style.display = 'none';
  window.scrollTo(0, 0);
  if(t==='L') loadPlan();
  if(t==='S') loadSpread();
  if(t==='P') loadPositions();
  if(t==='E') loadSeats();
}
function toggleMore(){
  const mm = document.getElementById('moreMenu');
  mm.style.display = mm.style.display === 'none' ? '' : 'none';
}
let SEATSD = null;
async function loadSeats(){
  if(SEATSD){ renderSeats(); return; }
  document.getElementById('seatWrap').innerHTML = '<div class="sub">loading ladders…</div>';
  try{
    const d = await (await fetch('seats.json')).json();
    SEATSD = d.families || [];
    renderSeats();
  }catch(e){
    const err = document.getElementById('seatErr');
    err.textContent = 'seats load failed: ' + e; err.style.display = 'block';
  }
}
async function seatQualify(fi, ri, ask){
  const r = SEATSD[fi].rows[ri];
  const jobs = [];
  if(r.need_bid) jobs.push({op:'place', market: r.market, side:'BUY',
    price_cents: r.need_bid.price_cents, size: r.need_bid.size, cap: r.need_bid.capital});
  if(r.need_ask) jobs.push({op:'place', market: r.market, side:'SELL',
    price_cents: r.need_ask.price_cents, size: r.need_ask.size, cap: r.need_ask.capital});
  if(!jobs.length) return true;
  const capT = jobs.reduce((s, j) => s + (j.cap || 0), 0);
  if(ask && !confirm('Fill '+r.market+' to Target Size ('+
      (r.target || 0).toLocaleString()+')?\\n'+
      jobs.map(j => j.side+' '+j.price_cents+'¢ × '+j.size.toLocaleString()).join(' + ')+
      ' — the cheapest orders that qualify the side'+(jobs.length > 1 ? 's' : '')+
      ', ~$'+capT.toFixed(2)+' locked, post-only.')) return false;
  jobs.forEach(j => { delete j.cap; });
  for(const j of jobs){
    try{
      const resp = await fetch('maction', {method:'POST',
        headers:{'Content-Type':'application/json','X-Reprice':'1'},
        body: JSON.stringify(j)});
      const d = await resp.json().catch(() => ({ok:false, error:'HTTP '+resp.status}));
      if(!d.ok){ toast(r.market+' '+j.side+' failed: '+(d.detail || d.error || '')); return false; }
    }catch(e){ toast('Failed: '+e); return false; }
    await new Promise(res => setTimeout(res, 1500));
  }
  if(ask){ SEATSD = null; setTimeout(loadSeats, 1200); }
  return true;
}
async function seatQualifyAll(fi){
  const rows = SEATSD[fi].rows.map((r, i) => [r, i])
    .filter(([r]) => r.need_bid || r.need_ask);
  if(!rows.length){ toast('Every market here already holds Target Size on both sides.'); return; }
  const capT = rows.reduce((s, [r]) => s +
    ((r.need_bid && r.need_bid.capital) || 0) + ((r.need_ask && r.need_ask.capital) || 0), 0);
  if(!confirm('Fill '+rows.length+' markets to Target Size with the cheapest possible orders (~$'+
      capT.toFixed(2)+' locked in total, post-only)?')) return;
  let done = 0;
  for(const [r, i] of rows){
    if(await seatQualify(fi, i, false)) done++;
  }
  toast('Qualifiers placed on '+done+'/'+rows.length+' markets.');
  SEATSD = null; loadSeats();
}
function renderSeats(){
  document.getElementById('seatWrap').innerHTML = (SEATSD || []).map((f, fi) =>
    '<h3>'+esc(f.title)+' <span class="sub" style="font-size:11px">'+f.rows.length+' markets</span> '+
    '<button class="tab" style="font-size:11px;padding:4px 10px" onclick="seatQualifyAll('+fi+')">⚓ Qualify all missing</button></h3>'+
    '<table><tr><th>Seats</th><th class="r">Own</th><th class="r">My orders</th><th class="r">Spread</th></tr>'+
    f.rows.map((r, ri) => {
      const own = r.net
        ? (r.net > 0
            ? '<b class="pos">'+r.net.toLocaleString()+'</b>'
            : '<b style="color:#f0883e">No '+Math.abs(r.net).toLocaleString()+'</b>')+
          (r.avg_cents != null ? '<br><span class="sub" style="font-size:10px">@ '+r.avg_cents.toFixed(1)+'¢</span>' : '')
        : '<span class="sub">—</span>';
      const shown = (r.orders || []).filter(o => !o.deep);  // qualifier quotes stay out of the way
      const missing = r.need_bid || r.need_ask;
      const qual = (r.target && r.bid_total != null)
        ? '<br><span class="sub" style="font-size:9px">bid '+r.bid_total.toLocaleString()+
          ' / ask '+r.ask_total.toLocaleString()+' of '+r.target.toLocaleString()+'</span>' : '';
      const ords = (shown.map(o =>
        '<span'+(o.side === 'SELL' ? ' style="color:#f0883e"' : '')+'>'+
        (o.side === 'SELL' ? 'S' : 'B')+' '+o.price_cents.toFixed(1)+'¢×'+(o.size||0).toLocaleString()+'</span>'+
        (o.best ? ' <b class="pos">★</b>' : ' <span class="sub" style="font-size:10px">behind</span>'))
        .join('<br>') || '<span class="sub">—</span>') +
        qual +
        (missing ? '<br><button class="alt" style="border:none;border-radius:6px;padding:3px 8px;background:#1f3a5f;color:#79b8ff;font-size:10px" '+
          'onclick="event.stopPropagation();seatQualify('+fi+','+ri+', true)">⚓ fill to target</button>' : '');
      const sp = (r.best_bid_cents != null && r.best_ask_cents != null)
        ? r.best_bid_cents.toFixed(0)+'⇄'+r.best_ask_cents.toFixed(0)+
          '<br><span class="sub" style="font-size:10px">'+r.spread_cents.toFixed(1)+'¢ wide</span>'
        : '<span class="sub">…</span>';
      return '<tr onclick="openMkt(\\''+esc(r.market)+'\\')">'+
        '<td><b>'+esc(r.label)+'</b><div class="mkt" style="font-size:9px">'+esc(r.market)+'</div></td>'+
        '<td class="r">'+own+'</td>'+
        '<td class="r" style="font-size:11px;white-space:nowrap">'+ords+'</td>'+
        '<td class="r" style="white-space:nowrap">'+sp+'</td></tr>';
    }).join('')+'</table>').join('')
    || '<div class="sub">no seat-count ladders found among tracked markets</div>';
}
let PLAN = null, PSEL = {}, BP = null, OLOCK = {};
function pwhich(){ const el = document.querySelector('input[name="pwhich"]:checked'); return el ? el.value : 'politics'; }
let RAGO = 1800;
function setRago(v){ RAGO = v; PLAN = null; PSEL = {}; loadPlan(); }
function switchPlan(){ PLAN = null; PSEL = {};
  document.getElementById('golfCapRow').style.display = pwhich() === 'golf' ? '' : 'none';
  document.getElementById('polCapRow').style.display = pwhich() === 'politics' ? '' : 'none';
  document.getElementById('restoreRow').style.display = pwhich() === 'restore' ? '' : 'none';
  loadPlan(); }
function polCap(){  // user cap on locked capital per market, null = off
  const v = +document.getElementById('polCapSlider').value;
  return v > 200 ? null : v;
}
function polCapSet(v){
  localStorage.setItem('polCap', v);
  document.getElementById('polCapLbl').textContent = +v > 200 ? 'off (buying power only)' : '$' + v;
  renderPlan();
}
(function(){ const v = localStorage.getItem('polCap');
  if(v){ document.getElementById('polCapSlider').value = v;
         document.getElementById('polCapLbl').textContent = +v > 200 ? 'off (buying power only)' : '$' + v; } })();
function mlimit(){  // per-market budget: buying power AND the politics cap
  const c = pwhich() === 'politics' ? polCap() : null;
  if(BP == null) return c;
  return c == null ? BP : Math.min(BP, c);
}
function mroom(m){  // per-market budget left after existing resting orders
  const lim = mlimit();
  return lim == null ? null : lim - (OLOCK[m] || 0);
}
async function loadPlan(){
  if(PLAN) return;
  try{
    const d = await (await fetch('plan.json?which=' + pwhich() +
      (pwhich() === 'restore' ? '&ago=' + RAGO : ''))).json();
    const err = document.getElementById('planErr');
    if(d.error){ err.textContent = d.error; err.style.display = 'block'; return; }
    PLAN = d; renderPlan();
  }catch(e){
    const err = document.getElementById('planErr');
    err.textContent = 'plan load failed: ' + e; err.style.display = 'block';
  }
}
function planCap(v){ document.getElementById('capLbl').textContent = v + '¢'; renderPlan(); }
function planSell(v){ document.getElementById('sellLbl').textContent = v + '¢'; renderPlan(); }
function golfCap(v){ localStorage.setItem('golfCap', v);
  document.getElementById('golfCapLbl').textContent = '$' + (v/100).toFixed(2); renderPlan(); }
(function(){ const v = localStorage.getItem('golfCap');
  if(v){ document.getElementById('golfCapSlider').value = v;
         document.getElementById('golfCapLbl').textContent = '$' + (+v/100).toFixed(2); } })();
function gfac(){  // chosen per-golfer cap vs the cap the scan allocated with
  const base = (PLAN && PLAN.plan && PLAN.plan.max_risk) || 1;
  return (+document.getElementById('golfCapSlider').value / 100) / base;
}
function gscale(v){  // rescale one planned order to the chosen golf cap
  const f = gfac(); if(!v || Math.abs(f - 1) < 1e-9) return v;
  const q = Math.max(1, Math.round(v.size * f));
  const s0 = Math.min(v.share/100, 0.999), sq = shareAt(v, q);
  return Object.assign({}, v, {size: q, capital: +(v.price * q).toFixed(2),
    est_day: +(v.est_day * (s0 > 0 ? sq/s0 : 0)).toFixed(2), share: +(sq*100).toFixed(1)});
}
function pkey(r){ return r.market + '|' + (r.side || 'BUY'); }
function szmode(){ const el = document.querySelector('input[name="szmode"]:checked'); return el ? el.value : 'pick'; }
function shareAt(m, q){
  // share = kS/(D+kS): recover D/k from the known (size, share) point, rescale
  const s = Math.min(m.share/100, 0.999);
  if(s <= 0) return 0;
  const Dk = m.size * (1 - s) / s;
  return q / (Dk + q);
}
function afford(r){
  // the full-size order, shrunk to what's LEFT of this market's buying power
  // after the orders already resting there
  const m = r.max; if(!m) return null;
  const room = mroom(r.market);
  if(room == null || m.covered || m.capital <= room) return (room != null && room < 1 && !m.covered) ? null : m;
  const unit = r.side === 'SELL' ? (1 - m.price) : m.price;  // lock per contract
  const q = Math.min(m.size, Math.floor(room / Math.max(unit, 0.0001)));
  if(q < 1) return null;
  const s0 = Math.min(m.share/100, 0.999), sq = shareAt(m, q);
  return {side: m.side, price: m.price, size: q, covered: m.covered,
          capital: +(unit * q).toFixed(2),
          est_day: +(m.est_day * (s0 > 0 ? sq / s0 : 0)).toFixed(2),
          share: +(sq * 100).toFixed(1), sized_down: true};
}
function ord(r){
  if(pwhich() === 'golf') return gscale((szmode() === 'max' && r.max) ? r.max : r.pick);
  return (szmode() === 'max' && r.max) ? afford(r) : r.pick;
}
function planRows(){
  const cap = +document.getElementById('capSlider').value;
  const sMin = +document.getElementById('sellSlider').value;
  const hide = document.getElementById('hideRisk').checked;
  return ((PLAN && PLAN.plan.results) || [])
    .filter(r => r.pick && !(hide && r.risk))
    .filter(r => {
      const room = mroom(r.market);
      if(room != null && room < 1) return false;  // maxed out — drop the market
      const o = ord(r);  // filter on the price actually being placed
      if(!o) return false;
      if(room != null && szmode() !== 'max' && !o.covered && o.capital > room + 0.01)
        return false;  // even the minimal entry doesn't fit what's left
      if(pwhich() === 'tt' || pwhich() === 'restore') return true;  // sliders don't apply
      return r.side === 'SELL' ? o.price*100 >= sMin : o.price*100 <= cap;
    })
    .sort((a,b) => (ord(b).est_day) - (ord(a).est_day));
}
function renderPlan(){
  if(!PLAN) return;
  document.getElementById('planGen').textContent = '· scanned ' + (PLAN.plan.generated || '');
  const mine = new Set(PLAN.mine || []);
  document.getElementById('plan').innerHTML =
    '<tr><th></th><th>Market</th><th>Side</th><th class="r">@</th><th class="r">Size</th><th class="r">Cap.</th><th class="r">$/day</th></tr>' +
    planRows().map(r => { const p = ord(r), k = pkey(r);
      const mx = (pwhich() === 'golf') ? gscale(r.max) : r.max;
      const upTo = (szmode() !== 'max' && mx) ?
        '<div class="sub" style="font-size:10px">up to $'+mx.est_day.toFixed(2)+'</div>' : '';
      return '<tr><td><input type="checkbox" '+(PSEL[k]?'checked':'')+
        ' onchange="PSEL[\\''+k+'\\']=this.checked;planSum()"></td>'+
        '<td class="mkt">'+esc(r.market)+(mine.has(r.market)?' ✔':'')+
        (r.prog&&r.prog.tier?' <span class="bdg">'+r.prog.tier+'</span>':'')+
        (r.risk?'<div style="color:#d29922">⚠ '+esc(r.risk)+'</div>':'')+'</td>'+
        '<td'+(r.side==='SELL'?' style="color:#f0883e"':'')+'>'+(r.side==='SELL'?'SELL':'BUY')+
        (p.covered?' 📦':'')+'</td>'+
        '<td class="r" style="white-space:nowrap">'+(+(p.price*100).toFixed(2))+'¢'+
        ((r.side==='SELL' ? p.price >= 0.989 : p.price <= (r.tick||0.01)+1e-9)
          ? ' <span class="bdg">'+(r.side==='SELL'?'deep':'floor')+'</span>' : '')+'</td>'+
        '<td class="r">'+p.size.toLocaleString()+(p.sized_down?' <span class="sub">↓fit</span>':'')+'</td>'+
        '<td class="r">$'+p.capital.toFixed(0)+'</td>'+
        '<td class="r">$'+p.est_day.toFixed(2)+upTo+'</td></tr>'; }).join('');
  planSum();
}
function perMktCap(rows){
  const m = {};
  rows.forEach(r => { m[r.market] = (m[r.market] || 0) + ord(r).capital; });
  return m;
}
function planAll(on){
  const used = {};  // starts from what existing orders already lock per market
  planRows().forEach(r => {
    if(!on){ PSEL[pkey(r)] = false; return; }
    if(r.risk) return;
    const c = ord(r).capital;
    const u = used[r.market] !== undefined ? used[r.market] : (OLOCK[r.market] || 0);
    const lim = mlimit();
    if(lim != null && u + c > lim) return;
    used[r.market] = u + c;
    PSEL[pkey(r)] = true;
  });
  renderPlan();
}
function planSum(){
  const sel = planRows().filter(r => PSEL[pkey(r)]);
  const worst = Math.max(0, ...Object.values(perMktCap(sel)));
  const est = sel.reduce((s,r)=>s+ord(r).est_day,0);
  document.getElementById('planSel').textContent =
    sel.length + ' selected (' + szmode() + ' size) · max $' + worst.toFixed(0) +
    ' locked in any one market · ~$' + est.toFixed(2) + '/day at current books';
}
async function placeBatch(){
  const tt = pwhich() === 'tt' || pwhich() === 'restore';
  const capC = tt ? 99.9 : +document.getElementById('capSlider').value;
  const sMin = tt ? 0.1 : +document.getElementById('sellSlider').value;
  const sel = planRows().filter(r => PSEL[pkey(r)]);
  if(!sel.length){ toast('Nothing selected'); return; }
  const est = sel.reduce((s,r)=>s+ord(r).est_day,0);
  const worst = Math.max(0, ...Object.values(perMktCap(sel)));
  const nS = sel.filter(r=>r.side==='SELL').length;
  const nRisk = sel.filter(r=>r.risk).length;
  let capLine;
  if(pwhich() === 'golf'){
    const byG = {};
    sel.forEach(r => { const g = r.market.split('-').pop();
      byG[g] = (byG[g]||0) + ord(r).capital; });
    const gWorst = Math.max(0, ...Object.values(byG));
    const gTot = sel.reduce((s,r)=>s+ord(r).capital,0);
    const gCap = +document.getElementById('golfCapSlider').value / 100;
    capLine = Object.keys(byG).length + ' golfers (cap $' + gCap.toFixed(2) + '/golfer) · max $' +
      gWorst.toFixed(2) + ' on any one golfer · $' + gTot.toFixed(2) + ' total at risk if every bid filled';
  } else {
    capLine = 'Max $' + worst.toFixed(0) +
      ' locked in any one market (buying power applies per market' +
      (polCap() != null ? ', your cap $' + polCap() + '/market' : '') + ')';
  }
  if(!confirm('Place ' + sel.length + ' post-only orders (' + (sel.length-nS) + ' buys, ' + nS +
              ' sells)?\\n' + capLine + ', ~$' +
              est.toFixed(2) + '/day at current books.' +
              (BP != null && worst > BP ? '\\n⚠ at least one market exceeds your $' + BP.toFixed(0) +
               ' buying power — its excess orders will be rejected!' : '') +
              (nRisk ? '\\n⚠ includes ' + nRisk + ' flagged-risky order' + (nRisk>1?'s':'') + '!' : ''))) return;
  try{
    const r = await fetch('place', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify({max_price_cents: capC, min_sell_cents: sMin, which: pwhich(),
        orders: sel.map(r => ({market: r.market, side: r.side || 'BUY',
          price_cents: +(ord(r).price*100).toFixed(1), size: ord(r).size}))})});
    const d = await r.json();
    if(!d.ok){ toast('Failed: ' + (d.error || '')); return; }
    if(d.precheck_skipped && d.precheck_skipped.length)
      toast(d.precheck_skipped.length + ' order(s) skipped by the sliders:\\n' +
            d.precheck_skipped.slice(0,5).join('\\n'));
    pollPlace();
  }catch(e){ toast('Failed: ' + e); }
}
async function pollPlace(){
  try{
    const d = await (await fetch('place_status')).json();
    const done = d.results.length;
    const placed = d.results.filter(x=>x.status==='placed').length;
    const skip = d.results.filter(x=>x.status==='skipped').length;
    document.getElementById('placeProg').textContent =
      (d.running ? 'placing… ' : 'batch ' + (d.summary || 'done') + ': ') +
      done + '/' + d.total + ' — ' + placed + ' placed, ' + skip + ' skipped, ' +
      (done - placed - skip) + ' failed';
    if(d.running) setTimeout(pollPlace, 2000);
    else { PSEL = {}; setTimeout(refresh, 1500); }
  }catch(e){ setTimeout(pollPlace, 3000); }
}
async function abortBatch(){
  try{ await fetch('place_abort', {method:'POST', headers:{'X-Reprice':'1'}}); }catch(e){}
  pollPlace();
}
let SPLAN = null, SPSEL = {};
function spCut(v){
  localStorage.setItem('spCut', v);
  document.getElementById('spCutLbl').textContent = v + '¢';
  renderSpread();
}
(function(){ const v = localStorage.getItem('spCut');
  if(v){ document.getElementById('spCutSlider').value = v;
         document.getElementById('spCutLbl').textContent = v + '¢'; } })();
async function loadSpread(){
  if(SPLAN){ renderSpread(); return; }
  try{
    const d = await (await fetch('plan.json?which=spread')).json();
    const err = document.getElementById('spErr');
    if(d.error){ err.textContent = d.error; err.style.display = 'block'; return; }
    SPLAN = d; renderSpread();
  }catch(e){
    const err = document.getElementById('spErr');
    err.textContent = 'spread plan load failed: ' + e; err.style.display = 'block';
  }
}
function spMarkets(){
  const by = {};
  ((SPLAN && SPLAN.plan.results) || []).forEach(r => {
    const e = by[r.market] = by[r.market] ||
      {market: r.market, spread: r.spread_cents, pool: r.side_pool, risk: r.risk, note: r.note};
    e[r.side] = r;
  });
  const cut = +document.getElementById('spCutSlider').value;
  return Object.values(by).filter(x => x.BUY && x.SELL && x.spread >= cut)
    .sort((a,b) => b.spread - a.spread);
}
function spOrd(r){  // one side of an entry, clamped to HALF the market's room
  const p = r.pick;
  const lock = r.side === 'SELL' ? (1 - p.price) : p.price;
  const room = mroom(r.market);
  const q = room == null ? p.size
    : Math.min(p.size, Math.floor((room / 2) / Math.max(lock, 0.0001)));
  return q < 1 ? null : {price: p.price, size: q, capital: +(lock * q).toFixed(2),
                         full: q >= p.size};
}
function renderSpread(){
  if(!SPLAN) return;
  document.getElementById('spGen').textContent = '· scanned ' + (SPLAN.plan.generated || '');
  const mine = new Set(SPLAN.mine || []);
  document.getElementById('sptab').innerHTML =
    '<tr><th></th><th>Market</th><th class="r">Spread</th><th class="r">Entry</th><th class="r">$/day</th></tr>' +
    spMarkets().map(x => {
      const b = spOrd(x.BUY), s = spOrd(x.SELL);
      if(!b && !s) return '';
      const entry = (b ? 'buy ' + (+(x.BUY.pick.price*100).toFixed(1)) + '¢ ×' + b.size.toLocaleString() : '') +
        (b && s ? '<br>' : '') +
        (s ? 'sell ' + (+(x.SELL.pick.price*100).toFixed(1)) + '¢ ×' + s.size.toLocaleString() : '');
      const cap = (b ? b.capital : 0) + (s ? s.capital : 0);
      const full = (!b || b.full) && (!s || s.full);
      return '<tr><td><input type="checkbox" '+(SPSEL[x.market]?'checked':'')+
        ' onchange="SPSEL[\\''+esc(x.market)+'\\']=this.checked;spSum()"></td>'+
        '<td class="mkt" onclick="openMkt(\\''+esc(x.market)+'\\')">'+esc(x.market)+(mine.has(x.market)?' ✔':'')+
        (x.risk?'<div style="color:#d29922">⚠ '+esc(x.risk)+'</div>':'')+'</td>'+
        '<td class="r" style="white-space:nowrap">'+(+(x.BUY.best_bid*100).toFixed(1))+'¢ ⇄ '+
        (+(x.BUY.best_ask*100).toFixed(1))+'¢<br><b>'+x.spread.toFixed(1)+'¢ wide</b></td>'+
        '<td class="r" style="white-space:nowrap;font-size:12px">'+entry+
        '<br><span class="sub" style="font-size:10px">$'+cap.toFixed(0)+' locked'+(full?'':' ↓fit')+'</span></td>'+
        '<td class="r">'+(full ? '$'+(2*x.pool).toFixed(2) : 'up to $'+(2*x.pool).toFixed(2))+'</td></tr>';
    }).join('') || '<tr><td class="sub">no politics market has a spread this wide — lower the min-spread slider</td></tr>';
  spSum();
}
function spAll(on){ spMarkets().forEach(x => { if(!on || !x.risk) SPSEL[x.market] = on; }); renderSpread(); }
function spSum(){
  let n = 0, cap = 0, est = 0;
  spMarkets().forEach(x => {
    if(!SPSEL[x.market]) return;
    const b = spOrd(x.BUY), s = spOrd(x.SELL);
    if(!b && !s) return;
    n++; cap += (b ? b.capital : 0) + (s ? s.capital : 0); est += 2 * x.pool;
  });
  document.getElementById('spSel').textContent =
    n + ' markets selected · ~$' + cap.toFixed(0) + ' locked · up to ~$' + est.toFixed(2) + '/day';
}
async function spPlace(){
  const orders = [];
  let cap = 0;
  spMarkets().forEach(x => {
    if(!SPSEL[x.market]) return;
    const b = spOrd(x.BUY), s = spOrd(x.SELL);
    if(b){ orders.push({market: x.market, side: 'BUY',
                        price_cents: +(x.BUY.pick.price*100).toFixed(1), size: b.size}); cap += b.capital; }
    if(s){ orders.push({market: x.market, side: 'SELL',
                        price_cents: +(x.SELL.pick.price*100).toFixed(1), size: s.size}); cap += s.capital; }
  });
  if(!orders.length){ toast('Nothing selected'); return; }
  if(!confirm('Enter ' + orders.length + ' post-only orders one tick inside the spread?\\n~$' +
              cap.toFixed(0) + ' locked while they rest. You will be BEST PRICE on both sides — ' +
              'first to earn, first to fill.')) return;
  try{
    const r = await fetch('place', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify({max_price_cents: 99.9, min_sell_cents: 0.1, which: 'spread',
                            orders: orders})});
    const d = await r.json();
    if(!d.ok){ toast('Failed: ' + (d.error || '')); return; }
    spPoll();
  }catch(e){ toast('Failed: ' + e); }
}
async function spPoll(){
  try{
    const d = await (await fetch('place_status')).json();
    const done = d.results.length;
    const placed = d.results.filter(x=>x.status==='placed').length;
    const skip = d.results.filter(x=>x.status==='skipped').length;
    document.getElementById('spProg').textContent =
      (d.running ? 'placing… ' : 'batch ' + (d.summary || 'done') + ': ') +
      done + '/' + d.total + ' — ' + placed + ' placed, ' + skip + ' skipped, ' +
      (done - placed - skip) + ' failed';
    if(d.running) setTimeout(spPoll, 2000);
    else { SPSEL = {}; SPLAN = null; setTimeout(refresh, 1500); }
  }catch(e){ setTimeout(spPoll, 3000); }
}
let RPLAN = null, RSEL = {};
(function(){ const v = localStorage.getItem('qdist');
  if(v !== null){ const el = document.querySelector('input[name="qdist"][value="'+v+'"]'); if(el) el.checked = true; } })();
async function loadReprice(){
  document.getElementById('rpl').innerHTML = '<div class="mkt">computing…</div>';
  const off = (document.querySelector('input[name="qdist"]:checked')||{value:'1'}).value;
  localStorage.setItem('qdist', off);
  try{
    const d = await (await fetch('reprice_plan?offset=' + off)).json();
    RPLAN = d.plan || [];
  }catch(e){ document.getElementById('rpl').innerHTML = '<div class="mkt">failed: '+e+'</div>'; return; }
  if(!RPLAN.length){
    document.getElementById('rpl').innerHTML =
      '<div class="mkt">All resting orders are already at (or within $0.05/day of) their best price 👍</div>';
    return;
  }
  RSEL = {}; RPLAN.forEach(r => RSEL[r.id] = true);
  renderRpl();
}
function renderRpl(){
  const sel = RPLAN.filter(r => RSEL[r.id]);
  const gain = sel.reduce((s,r)=>s+(r.est_after-r.est_now),0);
  document.getElementById('rpl').innerHTML =
    '<table><tr><th></th><th>Market</th><th class="r">Move</th><th class="r">$/day</th></tr>'+
    RPLAN.map(r =>
      '<tr><td><input type="checkbox" '+(RSEL[r.id]?'checked':'')+
      ' onchange="RSEL[\\''+r.id+'\\']=this.checked;renderRpl()"></td>'+
      '<td class="mkt">'+esc(r.market)+'<div class="sub" style="font-size:10px">'+r.side+' '+r.size.toLocaleString()+'</div></td>'+
      '<td class="r" style="white-space:nowrap">'+r.from_cents+'¢ → <b>'+r.to_cents+'¢</b>'+
      (r.to_size && r.to_size !== Math.round(r.size) ?
        '<br><span class="sub" style="font-size:10px">'+r.size.toLocaleString()+' → '+r.to_size.toLocaleString()+' (same $ at risk)</span>' : '')+'</td>'+
      '<td class="r">$'+r.est_now.toFixed(2)+' → <b class="pos">$'+r.est_after.toFixed(2)+'</b></td></tr>').join('')+
    '</table><div class="rp"><button onclick="goReprice()">Reprice '+sel.length+
    ' orders (+$'+gain.toFixed(2)+'/day)</button>'+
    '<button class="alt" onclick="RPLAN=null;document.getElementById(\\'rpl\\').innerHTML=\\'\\'">Close</button></div>';
}
async function goReprice(){
  const sel = RPLAN.filter(r => RSEL[r.id]);
  if(!sel.length){ toast('Nothing selected'); return; }
  const gain = sel.reduce((s,r)=>s+(r.est_after-r.est_now),0);
  if(!confirm('Reprice ' + sel.length + ' orders to their optimal prices?\\nEstimated gain ~$' +
              gain.toFixed(2) + '/day. Each move is checked against the live book first.')) return;
  try{
    const r = await fetch('reprice_batch', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify({orders: sel.map(r => ({id: r.id, to_cents: r.to_cents, to_size: r.to_size}))})});
    const d = await r.json();
    if(!d.ok){ toast('Failed: ' + (d.error || '')); return; }
    RPLAN = null; document.getElementById('rpl').innerHTML = '';
    pollReprice();
  }catch(e){ toast('Failed: ' + e); }
}
async function pollReprice(){
  try{
    const d = await (await fetch('place_status')).json();
    const done = d.results.length;
    const ok = d.results.filter(x=>x.status==='repriced').length;
    const skip = d.results.filter(x=>x.status==='skipped').length;
    const unv = d.results.filter(x=>x.status==='unverified').length;
    document.getElementById('rpProg').textContent =
      (d.running ? 'repricing… ' : 'batch ' + (d.summary || 'done') + ': ') +
      done + '/' + d.total + ' — ' + ok + ' repriced, ' + skip + ' skipped, ' +
      (done - ok - skip - unv) + ' failed' +
      (unv ? ', ' + unv + ' accepted but unconfirmed (check the app)' : '');
    if(d.running) setTimeout(pollReprice, 2000); else setTimeout(refresh, 1500);
  }catch(e){ setTimeout(pollReprice, 3000); }
}
let DPLAN = null, DSEL = {};
async function loadDead(){
  document.getElementById('rpl').innerHTML = '<div class="mkt">checking…</div>';
  try{
    const d = await (await fetch('dead_plan')).json();
    DPLAN = d.plan || [];
  }catch(e){ document.getElementById('rpl').innerHTML = '<div class="mkt">failed: '+e+'</div>'; return; }
  if(!DPLAN.length){
    document.getElementById('rpl').innerHTML =
      '<div class="mkt">No definitively dead orders — everything is earning or awaiting its book 🎉</div>';
    return;
  }
  DSEL = {}; DPLAN.forEach(r => DSEL[r.id] = true);
  renderDead();
}
function renderDead(){
  const sel = DPLAN.filter(r => DSEL[r.id]);
  const freed = sel.reduce((s,r)=>s+r.locked,0);
  document.getElementById('rpl').innerHTML =
    '<table><tr><th></th><th>Market</th><th class="r">Order</th><th class="r">Locked</th></tr>'+
    DPLAN.map(r =>
      '<tr><td><input type="checkbox" '+(DSEL[r.id]?'checked':'')+
      ' onchange="DSEL[\\''+r.id+'\\']=this.checked;renderDead()"></td>'+
      '<td class="mkt">'+esc(r.market)+'<div class="sub" style="font-size:10px">'+esc(r.why)+'</div></td>'+
      '<td class="r" style="white-space:nowrap">'+r.side+' '+r.size.toLocaleString()+' @ '+r.price_cents+'¢</td>'+
      '<td class="r">$'+r.locked.toFixed(0)+'</td></tr>').join('')+
    '</table><div class="rp"><button onclick="goCancelDead()">Cancel '+sel.length+
    ' orders (frees ~$'+freed.toFixed(0)+')</button>'+
    '<button class="alt" onclick="DPLAN=null;document.getElementById(\\'rpl\\').innerHTML=\\'\\'">Close</button></div>';
}
async function goCancelDead(){
  const sel = DPLAN.filter(r => DSEL[r.id]);
  if(!sel.length){ toast('Nothing selected'); return; }
  const freed = sel.reduce((s,r)=>s+r.locked,0);
  if(!confirm('Cancel ' + sel.length + ' resting orders earning ~$0/day?\\nFrees ~$' +
              freed.toFixed(0) + ' of locked collateral. Positions are untouched — this only ' +
              'removes unfilled orders.')) return;
  try{
    const r = await fetch('cancel_batch', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify({orders: sel.map(r => ({id: r.id}))})});
    const d = await r.json();
    if(!d.ok){ toast('Failed: ' + (d.error || '')); return; }
    DPLAN = null; document.getElementById('rpl').innerHTML = '';
    pollCancelDead();
  }catch(e){ toast('Failed: ' + e); }
}
async function pollCancelDead(){
  try{
    const d = await (await fetch('place_status')).json();
    const done = d.results.length;
    const ok = d.results.filter(x=>x.status==='cancelled').length;
    document.getElementById('rpProg').textContent =
      (d.running ? 'cancelling… ' : 'cleanup ' + (d.summary || 'done') + ': ') +
      done + '/' + d.total + ' — ' + ok + ' cancelled, ' + (done - ok) + ' failed';
    if(d.running) setTimeout(pollCancelDead, 2000); else setTimeout(refresh, 1500);
  }catch(e){ setTimeout(pollCancelDead, 3000); }
}
async function cancelAll(){
  if(!confirm('Cancel EVERY open order on your account?')) return;
  if(!confirm('Are you SURE? All reward earning stops until you re-place orders.')) return;
  try{
    const r = await fetch('cancel_all', {method:'POST', headers:{'X-Reprice':'1'}});
    const d = await r.json().catch(()=>({}));
    toast(d.ok ? 'All orders cancelled' : 'Failed: ' + (d.error || ('HTTP ' + r.status)));
  }catch(e){ toast('Failed: ' + e); }
  setTimeout(refresh, 1500);
}
function usd(v){ return (v<0?'-$':'$') + Math.abs(v||0).toFixed(2); }
function cls(v){ return v>0.004 ? 'pos' : (v<-0.004 ? 'neg' : ''); }
let POSD = [];
async function loadPositions(){
  document.getElementById('posSub').textContent = 'loading…';
  try{
    const d = await (await fetch('positions.json')).json();
    POSD = d.rows || [];
    RACED = d.races || [];
    renderPositions();
  }catch(e){
    const err = document.getElementById('posErr');
    err.textContent = 'positions load failed: ' + e; err.style.display = 'block';
  }
}
let RACED = [], RCOPEN = {};
function tglRace(i){ RCOPEN[i] = !RCOPEN[i]; renderRaces(); }
function renderRaces(){
  document.getElementById('raceList').innerHTML = (RACED || []).length ?
    '<tr><th>Race</th><th class="r">Held</th><th class="r">Cost</th><th class="r">Worst</th><th class="r">Best</th></tr>' +
    RACED.map((rc, i) => {
      const bar = (pl) => {  // little signed bar so the distribution reads at a glance
        const span = Math.max(Math.abs(rc.worst), Math.abs(rc.best), 0.01);
        const w = Math.min(60, Math.abs(pl) / span * 60);
        return '<span style="display:inline-block;height:8px;border-radius:3px;width:'+w.toFixed(0)+
          'px;background:'+(pl >= 0 ? '#3fb950' : '#f85149')+';vertical-align:middle"></span>';
      };
      const scen = (rc.scenarios || []).map(sc =>
        '<tr><td class="sub" style="font-size:11px;white-space:nowrap">'+esc(sc.outcome)+' wins</td>'+
        '<td class="r sub" style="font-size:11px;white-space:nowrap">'+
        (sc.held > 0 ? 'Yes '+sc.held.toLocaleString()
         : sc.held < 0 ? '<span style="color:#f0883e">No '+(-sc.held).toLocaleString()+'</span>' : '—')+'</td>'+
        '<td style="width:70px">'+bar(sc.pl)+'</td>'+
        '<td class="r '+(sc.pl >= 0 ? 'pos' : 'neg')+'" style="white-space:nowrap"><b>'+
        (sc.pl >= 0 ? '+' : '')+sc.pl.toFixed(2)+'</b></td></tr>').join('') +
        (rc.other_pl != null ?
          '<tr><td class="sub" style="font-size:11px">any unheld outcome wins</td><td></td>'+
          '<td style="width:70px">'+bar(rc.other_pl)+'</td>'+
          '<td class="r '+(rc.other_pl >= 0 ? 'pos' : 'neg')+'"><b>'+
          (rc.other_pl >= 0 ? '+' : '')+rc.other_pl.toFixed(2)+'</b></td></tr>' : '');
      return '<tr'+(rc.locked ? ' style="background:#12341c"' : '')+' onclick="tglRace('+i+')">'+
        '<td class="mkt">'+esc(rc.race)+(rc.locked ? ' 🔒' : '')+
        '<div class="sub" style="font-size:10px">'+(RCOPEN[i] ? 'tap to collapse' : 'tap for per-outcome breakdown')+'</div></td>'+
        '<td class="r">'+rc.held+'/'+rc.outcomes+'</td>'+
        '<td class="r">$'+rc.cost.toFixed(2)+'</td>'+
        '<td class="r '+(rc.worst >= 0 ? 'pos' : 'neg')+'"><b>'+(rc.worst >= 0 ? '+' : '')+rc.worst.toFixed(2)+'</b></td>'+
        '<td class="r '+(rc.best >= 0 ? 'pos' : 'neg')+'">'+(rc.best >= 0 ? '+' : '')+rc.best.toFixed(2)+'</td></tr>'+
        '<tr style="display:'+(RCOPEN[i] ? '' : 'none')+'"><td colspan="5" style="background:var(--surface2)">'+
        '<table class="bk" style="width:100%">'+scen+'</table></td></tr>';
    }).join('')
    : '<tr><td class="sub">no race with positions in 2+ outcomes</td></tr>';
}
function renderPositions(){
  const nFix = POSD.filter(r => r.status === 'fix').length;
  document.getElementById('posSub').textContent =
    POSD.length + ' positions · ' + (nFix ? nFix + ' need attention' : 'all priced to sell ✓');
  renderRaces();
  document.getElementById('posList').innerHTML =
    POSD.map((r, i) => {
      const bg = r.status === 'good' ? 'background:rgba(63,185,80,.08)'
               : r.status === 'fix' ? 'background:rgba(248,81,73,.09)'
               : r.status === 'wait' ? 'background:rgba(152,163,179,.06)' : '';
      const sells = (r.sells || []).map(s =>
        s.size.toLocaleString() + ' @ ' + s.price_cents.toFixed(1) + '¢').join(', ');
      const mag = Math.min(Math.abs(Math.round(r.net)), 20000);
      const qty = r.target_cents
        ? '<div onclick="event.stopPropagation()" style="white-space:nowrap;margin-bottom:4px">'+
          '<button class="alt" onclick="qBump(\\'pq'+i+'\\',-1)">−</button>'+
          '<input id="pq'+i+'" type="number" step="1" min="1" max="'+mag+'" value="'+mag+'" '+
          'style="width:64px">'+
          '<button class="alt" onclick="qBump(\\'pq'+i+'\\',1)">+</button></div>'
        : '';
      const takeBtn = r.hit_cents
        ? '<br><button style="background:#8b5a00;color:#fff;border:none;border-radius:6px;'+
          'padding:6px 10px;margin-top:4px" '+
          'onclick="event.stopPropagation();posTake('+i+')">'+
          (r.short ? 'Buy back NOW' : 'Sell NOW')+' @ '+r.hit_cents.toFixed(1)+'¢</button>'+
          '<br><span class="sub" style="font-size:10px">'+r.hit_size.toLocaleString()+
          ' resting there</span>'
        : '';
      const btn = (r.target_cents && r.status !== 'wait')
        ? qty +
          '<button style="background:'+(r.status === 'fix' ? 'var(--good)' : 'var(--surface2)')+
          ';color:'+(r.status === 'fix' ? '#0b2417' : 'var(--ink2)')+
          ';border:none;border-radius:6px;padding:6px 10px" '+
          'onclick="event.stopPropagation();posFix('+i+', true)">'+
          (r.short ? 'Buy back' : 'Sell')+' @ '+r.target_cents.toFixed(1)+'¢</button>'+
          (r.status === 'good' ? ' ✓' : '') + takeBtn
        : (r.status === 'good' ? '✓'
          : r.status === 'wait' ? qty + '<span class="sub" style="font-size:10px">tight spread —<br>wait</span>' + takeBtn
          : '<span class="sub" style="font-size:10px">book pending<br>↻ refresh</span>' + takeBtn);
      const ownTxt = r.short
        ? '<b style="color:#f0883e">No '+Math.abs(r.net).toLocaleString()+'</b>'
        : r.net.toLocaleString();
      // One cell per position, not four columns. On a phone the button column
      // demands ~300px, and a four-column row answers that by squeezing the
      // name to a single character per line. Name gets its own full-width
      // line; the numbers and the buttons share the line below and wrap.
      return '<tr style="'+bg+'">'+
        '<td style="padding:8px 0">'+
        '<div onclick="openMkt(\\''+esc(r.market)+'\\')">'+
          '<b style="color:var(--ink);font-size:13px;line-height:1.3">'+esc(mname(r.market))+'</b>'+
          '<div class="sub" style="font-size:9px;word-break:break-all">'+esc(r.market)+'</div>'+
        '</div>'+
        '<div style="display:flex;flex-wrap:wrap;align-items:flex-start;'+
             'justify-content:space-between;gap:10px;margin-top:6px">'+
          '<div style="flex:1 1 120px;min-width:110px">'+ownTxt+
            (r.avg_cents != null ? '<span class="sub" style="font-size:10px"> @ '+r.avg_cents.toFixed(1)+'¢ avg</span>' : '')+
            '<div class="sub" style="font-size:11px;margin-top:2px">'+
            (sells ? esc(sells) : 'no sell resting')+'</div>'+
          '</div>'+
          '<div style="flex:0 0 auto;text-align:right">'+btn+'</div>'+
        '</div></td></tr>';
    }).join('') || '<tr><td class="sub">no open positions</td></tr>';
}
async function posFix(i, ask){
  const r = POSD[i];
  if(!r || !r.target_cents) return false;
  const mag = Math.min(Math.abs(Math.round(r.net)), 20000);
  const el = document.getElementById('pq'+i);
  let q = el ? parseInt(el.value, 10) : mag;
  if(!(q >= 1)) q = mag;
  q = Math.min(q, mag);  // never sell more than held / buy back more than short
  const verb = r.short ? 'Buy back' : 'Sell';
  if(ask && !arm('fix'+i, verb+' '+q.toLocaleString()+' @ '+r.target_cents.toFixed(1)+'¢, resting order')) return false;
  const body = (r.sells && r.sells.length)
    ? {op:'modify', order_id: r.sells[0].id, price_cents: r.target_cents, size: q}
    : (r.short
        ? {op:'place', market: r.market, side: 'BUY', price_cents: r.target_cents, size: q, close_short: true}
        : {op:'place', market: r.market, side: 'SELL', price_cents: r.target_cents, size: q});
  try{
    const resp = await fetch('maction', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify(body)});
    const d = await resp.json().catch(() => ({ok:false, error:'HTTP '+resp.status}));
    if(!d.ok){ toast(r.market+' failed: '+(d.detail || d.error || '')); return false; }
    if(ask){ setTimeout(loadPositions, 1200); }
    return true;
  }catch(e){ toast('Failed: '+e); return false; }
}
async function posTake(i){
  const r = POSD[i];
  if(!r || !r.hit_cents) return;
  const mag = Math.min(Math.abs(Math.round(r.net)), 20000);
  const el = document.getElementById('pq'+i);
  let q = el ? parseInt(el.value, 10) : mag;
  if(!(q >= 1)) q = mag;
  q = Math.min(q, mag);
  const verb = r.short ? 'Buy back' : 'Sell';
  const cash = (r.hit_cents/100*q).toFixed(2);
  if(!arm('take'+i, verb+' '+q.toLocaleString()+' NOW at '+r.hit_cents.toFixed(1)+'¢ (≈ $'+cash+', fills instantly)')) return;
  try{
    const resp = await fetch('maction', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify({op:'take', market:r.market, size:q, close_short:!!r.short})});
    const d = await resp.json().catch(() => ({ok:false, error:'HTTP '+resp.status}));
    toast(d.ok ? 'Done ✓'+(d.canceled_first ? ' ('+d.canceled_first+' of your resting orders canceled first)' : '')
               : 'Failed: '+(d.detail || d.error || ''));
  }catch(e){ toast('Failed: '+e); }
  setTimeout(loadPositions, 1500);
}
async function posFixAll(){
  const flagged = POSD.map((r, i) => i).filter(i => POSD[i].status === 'fix' && POSD[i].target_cents);
  if(!flagged.length){ toast('Nothing flagged — everything is already priced to sell.'); return; }
  if(!confirm('Price '+flagged.length+' positions to sell, each one tick inside its best ask?')) return;
  let done = 0;
  for(const i of flagged){
    document.getElementById('posProg').textContent = 'pricing… '+done+'/'+flagged.length;
    if(await posFix(i, false)) done++;
    await new Promise(res => setTimeout(res, 1500));
  }
  document.getElementById('posProg').textContent = 'done — '+done+'/'+flagged.length+' priced';
  loadPositions();
}
function tgl(i, m){ OPEN[m] = !OPEN[m];
  const e = document.getElementById('d'+i); if(e) e.style.display = OPEN[m] ? '' : 'none';
  if(OPEN[m]){ SEEN[m] = RATES[m] || 0; localStorage.setItem('seenRates', JSON.stringify(SEEN));
    const row = document.getElementById('r'+i); if(row) row.style.background=''; } }
async function tglGraph(i, m){ GOPEN[m] = !GOPEN[m];
  const e = document.getElementById('g'+i); if(!e) return;
  if(GOPEN[m]){ if(!SERIES){ try{ SERIES = (await (await fetch('series.json')).json()).series || {}; }catch(_){ SERIES = {}; } }
    e.cells[0].innerHTML = spark(SERIES[m]); e.style.display = ''; }
  else e.style.display = 'none'; }
function spark(pts){
  if(!pts || pts.length < 2) return '<div class="mkt">not enough history yet — collecting a point per minute</div>';
  const w = 330, h = 96, p = 10;
  const ts = pts.map(q=>q[0]), rs = pts.map(q=>q[1]);
  const t0 = Math.min(...ts), t1 = Math.max(...ts);
  const r0 = Math.min(...rs), r1 = Math.max(...rs);
  const X = t => p + (w-2*p)*(t-t0)/Math.max(t1-t0,1);
  const Y = r => h-p - (h-2*p)*(r-r0)/Math.max(r1-r0,1e-9);
  const dpath = pts.map((q,i)=>(i?'L':'M')+X(q[0]).toFixed(1)+' '+Y(q[1]).toFixed(1)).join(' ');
  const hrs = ((t1-t0)/3600).toFixed(1);
  return '<svg width="'+w+'" height="'+h+'" style="background:#141a23;border-radius:12px;max-width:100%">'+
    '<path d="'+dpath+'" fill="none" stroke="var(--accent)" stroke-width="2"/></svg>'+
    '<div class="mkt">$/day over last '+hrs+'h · min $'+r0.toFixed(2)+' · max $'+r1.toFixed(2)+
    ' · now $'+rs[rs.length-1].toFixed(2)+'</div>';
}
function cumAt(cf, hf){
  if(!(cf && cf.length === 25)) return hf / 24;
  const i = Math.floor(hf);
  return cf[i] + (cf[Math.min(i + 1, 24)] - cf[i]) * (hf - i);
}
function dayGraph(d){
  const pts = d.earned_series || [];
  if(pts.length < 3) return '<div class="mkt">collecting today’s curve — back in a few minutes…</div>';
  const w = 360, h = 110, p = 10;
  const et = new Date(new Date().toLocaleString('en-US', {timeZone: 'America/New_York'}));
  const hf = et.getHours() + et.getMinutes() / 60;
  const midMs = Date.now() - hf * 3600000;
  const eNow = pts[pts.length - 1][1];
  const fNow = cumAt(d.pace_cum, hf);
  const proj = [];
  if(fNow > 0.02){
    const scale = eNow / fNow;
    for(let x = 0; x <= 24.001; x += 0.25) proj.push([Math.min(x, 24), scale * cumAt(d.pace_cum, Math.min(x, 24))]);
  }
  const end = proj.length ? proj[proj.length - 1][1] : eNow;
  const ymax = Math.max(end, eNow, 0.5) * 1.08;
  const X = x => p + (w - 2 * p) * x / 24;
  const Y = v => h - p - (h - 2 * p) * v / ymax;
  const hx = ts => Math.min(Math.max((ts * 1000 - midMs) / 3600000, 0), 24);
  const curve = pts.map((q, i) => (i ? 'L' : 'M') + X(hx(q[0])).toFixed(1) + ' ' + Y(q[1]).toFixed(1)).join(' ');
  const pcurve = proj.map((q, i) => (i ? 'L' : 'M') + X(q[0]).toFixed(1) + ' ' + Y(q[1]).toFixed(1)).join(' ');
  return '<svg viewBox="0 0 ' + w + ' ' + h + '" style="width:100%;background:#141a23;border-radius:12px">' +
    '<line x1="' + X(hf).toFixed(1) + '" y1="' + p + '" x2="' + X(hf).toFixed(1) + '" y2="' + (h - p) +
    '" stroke="var(--ink3)" stroke-width="1" stroke-dasharray="2,4"/>' +
    (pcurve ? '<path d="' + pcurve + '" fill="none" stroke="var(--good)" stroke-width="2" stroke-dasharray="4,5" opacity=".9"/>' : '') +
    '<path d="' + curve + '" fill="none" stroke="var(--accent)" stroke-width="2.5"/>' +
    '</svg>' +
    '<div class="mkt">midnight → midnight ET · solid: earned so far' +
    (proj.length ? ' · dotted: your typical day → <b style="color:var(--good)">≈ $' + end.toFixed(2) + '</b> by midnight' : '') + '</div>';
}
function rateDayGraph(d){
  const all = d.rate_series || [];
  const et = new Date(new Date().toLocaleString('en-US', {timeZone: 'America/New_York'}));
  const hf = et.getHours() + et.getMinutes() / 60;
  const midMs = Date.now() - hf * 3600000;
  const pts = all.filter(q => q[0] * 1000 >= midMs);
  if(pts.length < 3) return '<div class="mkt">collecting today’s rate curve — back in a few minutes…</div>';
  const w = 360, h = 110, p = 10;
  // light smoothing so the solid line reads as a shape, not static
  const sm = pts.map((q, i) => {
    const a = Math.max(0, i - 7), win = pts.slice(a, i + 1);
    return [q[0], win.reduce((s, x) => s + x[1], 0) / win.length];
  });
  // expected rate ahead: the profile's hourly weights, scaled so the area
  // from now to midnight equals the same projected remainder as the
  // cumulative view (identical midnight total, different lens)
  const eNow = (d.earned_series && d.earned_series.length)
    ? d.earned_series[d.earned_series.length - 1][1] : d.earned_today;
  const fNow = cumAt(d.pace_cum, hf);
  const proj = [];
  if(d.pace_cum && d.pace_cum.length === 25 && fNow > 0.02){
    const scale = eNow / fNow;
    const hr = [];  // hourly rates, sampled at hour centers, linearly blended
    for(let i = 0; i < 24; i++) hr.push(scale * (d.pace_cum[i + 1] - d.pace_cum[i]) * 24);
    const rAt = x => {
      const c = Math.min(Math.max(x - 0.5, 0), 23);
      const i = Math.min(Math.floor(c), 22);
      return hr[i] + (hr[i + 1] - hr[i]) * (c - i);
    };
    for(let x = 0; x <= 24.001; x += 0.25) proj.push([Math.min(x, 24), rAt(Math.min(x, 24))]);
  }
  // Raw Poisson samples — the individual measurements the day's figure is
  // built from. Scale to their 95th percentile, not their max: in a deep book
  // scoring flips to full whenever we hold the touch, so a handful of spikes
  // would otherwise flatten the whole chart. Anything above is clamped to the
  // top edge and drawn hollow so a clipped point is visibly clipped.
  const dots = (d.hf_points || []).filter(q => q[0] * 1000 >= midMs);
  const dsort = dots.map(q => q[1]).sort((a, b) => a - b);
  const p95 = dsort.length ? dsort[Math.floor(dsort.length * 0.95)] : 0;
  const ys = sm.map(q => q[1]).concat(proj.map(q => q[1])).concat(p95 ? [p95] : []);
  const ymax = Math.max(...ys, 1) * 1.1;
  const X = x => p + (w - 2 * p) * x / 24;
  const Y = v => h - p - (h - 2 * p) * v / ymax;
  const hx = ts => Math.min(Math.max((ts * 1000 - midMs) / 3600000, 0), 24);
  const dotSvg = dots.map(q => {
    const over = q[1] > ymax;
    return '<circle cx="' + X(hx(q[0])).toFixed(1) + '" cy="' + Y(Math.min(q[1], ymax)).toFixed(1) +
      '" r="' + (over ? 1.6 : 1.3) + '" ' +
      (over ? 'fill="none" stroke="var(--accent)" stroke-width=".8" opacity=".55"'
            : 'fill="var(--accent)" opacity=".22"') + '/>';
  }).join('');
  const curve = sm.map((q, i) => (i ? 'L' : 'M') + X(hx(q[0])).toFixed(1) + ' ' + Y(q[1]).toFixed(1)).join(' ');
  const pcurve = proj.map((q, i) => (i ? 'L' : 'M') + X(q[0]).toFixed(1) + ' ' + Y(q[1]).toFixed(1)).join(' ');
  const clipped = dots.filter(q => q[1] > ymax).length;
  return '<svg viewBox="0 0 ' + w + ' ' + h + '" style="width:100%;background:#141a23;border-radius:12px">' +
    '<line x1="' + X(hf).toFixed(1) + '" y1="' + p + '" x2="' + X(hf).toFixed(1) + '" y2="' + (h - p) +
    '" stroke="var(--ink3)" stroke-width="1" stroke-dasharray="2,4"/>' +
    dotSvg +
    (pcurve ? '<path d="' + pcurve + '" fill="none" stroke="var(--good)" stroke-width="2" stroke-dasharray="4,5" opacity=".9"/>' : '') +
    '<path d="' + curve + '" fill="none" stroke="var(--accent)" stroke-width="2.5"/>' +
    '</svg>' +
    '<div class="mkt">earning rate, midnight → midnight ET · solid: today, smoothed over ~8 min' +
    (dots.length ? ' · dots: ' + dots.length + ' raw samples (last ~50 min)' +
                   (clipped ? ', ' + clipped + ' hollow = above the top edge' : '') : '') +
    (proj.length ? ' · dashed: your typical pattern (above it = beating your usual hour)' : '') + '</div>';
}
function rateZoomGraph(d){
  // The last 15 minutes at full resolution: every Poisson sample as its own
  // dot, no percentile scaling. The day view has to compress spikes to stay
  // readable; here the spikes ARE the point — they show how much of the time
  // we actually hold the touch, which is what the day's figure averages over.
  const MINS = 15;
  const nowS = Date.now() / 1000;
  const t0 = nowS - MINS * 60;
  const pts = (d.hf_points || []).filter(q => q[0] >= t0).sort((a, b) => a[0] - b[0]);
  if(pts.length < 3) return '<div class="mkt">collecting samples — the zoom fills in over a minute or two…</div>';
  const w = 360, h = 110, p = 10;
  const ys = pts.map(q => q[1]);
  const lo = Math.min(...ys), hi = Math.max(...ys);
  const pad = Math.max((hi - lo) * 0.10, 0.01);
  const y0 = Math.max(0, lo - pad), y1 = hi + pad;
  const X = t => p + (w - 2 * p) * Math.min(Math.max((t - t0) / (MINS * 60), 0), 1);
  const Y = v => h - p - (h - 2 * p) * (v - y0) / Math.max(y1 - y0, 1e-9);
  // trailing mean over ~1 minute of samples — at this zoom the headline's
  // ~10 min smoothing is a flat line and shows nothing
  const W = 12;
  const sm = pts.map((q, i) => {
    const win = pts.slice(Math.max(0, i - W + 1), i + 1);
    return [q[0], win.reduce((s, x) => s + x[1], 0) / win.length];
  });
  const mean = ys.reduce((a, b) => a + b, 0) / ys.length;
  const dotSvg = pts.map(q =>
    '<circle cx="' + X(q[0]).toFixed(1) + '" cy="' + Y(q[1]).toFixed(1) +
    '" r="1.7" fill="var(--accent)" opacity=".45"/>').join('');
  const curve = sm.map((q, i) => (i ? 'L' : 'M') + X(q[0]).toFixed(1) + ' ' + Y(q[1]).toFixed(1)).join(' ');
  // minute gridlines, so the gaps between samples are readable as time
  let grid = '';
  for(let k = 1; k < MINS; k++){
    if(k % 5) continue;
    const gx = X(t0 + k * 60).toFixed(1);
    grid += '<line x1="' + gx + '" y1="' + p + '" x2="' + gx + '" y2="' + (h - p) +
            '" stroke="var(--ink3)" stroke-width=".5" opacity=".45"/>';
  }
  const gapS = (pts[pts.length - 1][0] - pts[0][0]) / Math.max(pts.length - 1, 1);
  return '<svg viewBox="0 0 ' + w + ' ' + h + '" style="width:100%;background:#141a23;border-radius:12px">' +
    grid +
    '<line x1="' + p + '" y1="' + Y(mean).toFixed(1) + '" x2="' + (w - p) + '" y2="' + Y(mean).toFixed(1) +
    '" stroke="var(--good)" stroke-width="1" stroke-dasharray="4,4" opacity=".85"/>' +
    dotSvg +
    '<path d="' + curve + '" fill="none" stroke="var(--accent)" stroke-width="2"/>' +
    '</svg>' +
    '<div class="mkt">last ' + MINS + ' min · ' + pts.length + ' samples, one every ' +
    gapS.toFixed(1) + 's · dashed: window mean <b style="color:var(--good)">$' + mean.toFixed(2) +
    '</b>/day · range $' + lo.toFixed(2) + '–$' + hi.toFixed(2) +
    ' · solid: trailing 1 min. Gridlines every 5 min.</div>';
}
function heroMode(){ return localStorage.getItem('heroG') || 'day'; }
function setHeroMode(m){ localStorage.setItem('heroG', m); refresh(); }
function bigSpark(pts){
  if(!pts || pts.length < 3) return '<div class="mkt">collecting today’s rate curve — one point per minute…</div>';
  const w = 360, h = 110, p = 10;
  // Plots the overall earning RATE ($/day) through the day. Frame ONLY the
  // data — x spans first..last sample, y spans the day's min..max rate — so
  // the moves fill the chart.
  const t0 = pts[0][0], t1 = pts[pts.length-1][0];
  const ys = pts.map(q=>q[1]);
  const ymin = Math.min(...ys), ymax = Math.max(...ys);
  const pad = Math.max((ymax - ymin) * 0.06, 0.01);
  const y0 = ymin - pad, y1 = ymax + pad;
  let n = pts.length, sx = 0, sy = 0, sxx = 0, sxy = 0;
  pts.forEach(([x,y]) => { sx += x; sy += y; sxx += x*x; sxy += x*y; });
  const den = n*sxx - sx*sx;
  const slope = den ? (n*sxy - sx*sy)/den : 0, icept = (sy - slope*sx)/n;
  const X = t => p + (w-2*p)*(t-t0)/Math.max(t1-t0, 1);
  const Y = y => h-p - (h-2*p)*(y-y0)/Math.max(y1-y0, 1e-9);
  const curve = pts.map((q,i)=>(i?'L':'M')+X(q[0]).toFixed(1)+' '+Y(q[1]).toFixed(1)).join(' ');
  const trend = 'M'+X(t0).toFixed(1)+' '+Y(slope*t0+icept).toFixed(1)+
                ' L'+X(t1).toFixed(1)+' '+Y(slope*t1+icept).toFixed(1);
  const now = pts[pts.length-1][1];
  const avg = sy / n;
  const hrs = ((t1-t0)/3600).toFixed(1);
  return '<svg viewBox="0 0 '+w+' '+h+'" style="width:100%;background:#141a23;border-radius:12px">'+
    '<path d="'+trend+'" fill="none" stroke="var(--good)" stroke-width="1.5" stroke-dasharray="5,4"/>'+
    '<path d="'+curve+'" fill="none" stroke="var(--accent)" stroke-width="2.5"/></svg>'+
    '<div class="mkt">rate, last '+hrs+'h: now <b style="color:var(--accent)">$'+now.toFixed(2)+'/day</b>'+
    ' · avg $'+avg.toFixed(2)+'/day · range $'+ymin.toFixed(2)+'–$'+ymax.toFixed(2)+'</div>';
}
function tint(m, cur){
  const seen = SEEN[m];
  if(seen === undefined) return '';
  const delta = cur - seen;
  if(Math.abs(delta) < Math.max(0.5, 0.25*Math.max(seen, 0.01))) return '';
  return delta < 0 ? 'background:rgba(229,100,95,.10)' : 'background:rgba(52,192,124,.10)';
}
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;'); }
function mcat(m){
  const s = String(m);
  if(/^tec-(pga|liv|golf)-/.test(s)) return 'Golf';
  if(s.indexOf('tec-nba-') === 0) return 'NBA';
  if(s.indexOf('tec-cbb-') === 0) return 'College BB';
  if(s.indexOf('tec-') === 0) return 'Other sports';
  if(s.indexOf('aec-') === 0) return 'Table tennis';
  return 'Politics';
}
function hidCats(){ try{ return JSON.parse(localStorage.getItem('hidCats') || '{}'); }catch(e){ return {}; } }
function tglCat(c){
  const h = hidCats();
  if(h[c]) delete h[c]; else h[c] = 1;
  localStorage.setItem('hidCats', JSON.stringify(h));
  refresh();
}
function sortCat(){ return localStorage.getItem('sortCat') === '1'; }
function tglSortCat(){ localStorage.setItem('sortCat', sortCat() ? '0' : '1'); refresh(); }
let PCTS = {}, PCTBASE = null;
function pctMode(){ return localStorage.getItem('pctMode') === '1'; }
function tglPct(){ localStorage.setItem('pctMode', pctMode() ? '0' : '1'); refresh(); }
function mSort(){ return localStorage.getItem('mktSort') || 'rate'; }
function setMSort(v){ localStorage.setItem('mktSort', v); refresh(); }
function pctChg(m){
  const c = PCTS[m], b = PCTBASE ? PCTBASE[m] : null;
  return (c == null || b == null) ? 0 : c - b;
}
function pctArrow(m){
  const dd = pctChg(m);
  if(Math.abs(dd) < 1) return '';
  return dd > 0 ? ' <span class="pos">▲'+dd.toFixed(0)+'</span>'
                : ' <span class="neg">▼'+Math.abs(dd).toFixed(0)+'</span>';
}
async function reprice(id, label){
  const inp = document.getElementById('p'+id);
  const cents = parseFloat(inp.value);
  if(!(cents >= 0.1 && cents <= 99.9)){ toast('Price out of range (0.1–99.9¢)'); return; }
  if(!confirm('Reprice ' + label + ' to ' + cents + '¢?')) return;
  try{
    const r = await fetch('reprice', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify({order_id:id, price_cents:cents})});
    const d = await r.json().catch(()=>({ok:false,error:'HTTP '+r.status}));
    toast(d.ok ? 'Repriced ✓' : 'Failed: ' + (d.detail || d.error || ('HTTP '+r.status)));
  }catch(e){ toast('Failed: '+e); }
  setTimeout(refresh, 1500);
}
let LASTD = null;
function txnSeen(){ return +(localStorage.getItem('txnSeen') || 0); }
function clearTxns(){
  localStorage.setItem('txnSeen', '' + Math.floor(Date.now()/1000));
  if(LASTD) renderHome(LASTD);
}
function hidW(){ try{ return JSON.parse(localStorage.getItem('hidWinners') || '{}'); }catch(e){ return {}; } }
function hideWinner(m){
  const h = hidW(); h[m] = 1;
  localStorage.setItem('hidWinners', JSON.stringify(h));
  if(LASTD) renderHome(LASTD);
}
function unhideWinners(){ localStorage.removeItem('hidWinners'); if(LASTD) renderHome(LASTD); }
// Human names for market codes — the raw slug stays visible in the sheet.
const MTOK = {usse:'Senate', ussep:'Senate primary', usgub:'Governor',
  usgubp:'Governor primary', housepopw:'House popular vote', uspres28:'President 2028',
  hrep:'House', ref:'Referendum', dem:'· Dem', rep:'· Rep', pass:'· passes'};
function mname(m){
  const s = String(m);
  let mm = s.match(/^scc-senate-gop-.*?-(gte|lte)?(\d+)$/);
  if(mm) return 'Senate GOP '+(mm[1]==='gte'?'≥':mm[1]==='lte'?'≤':'')+mm[2]+' seats';
  mm = s.match(/^scc-hrep-rep-.*?-(gte|lte)?(\d+)$/);
  if(mm) return 'House GOP '+(mm[1]==='gte'?'≥':mm[1]==='lte'?'≤':'')+mm[2]+' seats';
  const parts = s.split('-');
  const out = [];
  for(let i = 1; i < parts.length; i++){
    if(/^\d{4}$/.test(parts[i]) && /^\d{1,2}$/.test(parts[i+1]||'') && /^\d{1,2}$/.test(parts[i+2]||'')){
      i += 2; continue;  // strip the embedded event date
    }
    const p = parts[i];
    out.push(MTOK[p] || (p.length === 2 ? p.toUpperCase() : p));
  }
  const t = out.join(' ');
  return t ? t.charAt(0).toUpperCase() + t.slice(1) : s;
}
function mcell(m){
  return '<td class="mkt"><b style="color:var(--ink);font-size:12px">'+esc(mname(m))+'</b></td>';
}
function mrow(m, mid, right){
  return '<tr onclick="openMkt(\\''+esc(m)+'\\')">'+mcell(m)+
         (mid||'')+'<td class="r" style="white-space:nowrap">'+right+'</td></tr>';
}
function renderHome(d){
  LASTD = d;
  const seen = txnSeen();
  const tx = (d.trades || []).filter(t => t.ts_s > seen);
  document.getElementById('txns').innerHTML = tx.length ? tx.slice(0, 25).map(t => {
      const n = t.filled != null ? (+t.filled).toLocaleString() : '?';
      const px = t.price_cents != null ? ' at ' + (+t.price_cents).toFixed(1) + '¢' : '';
      const sold = t.verb === 'Sold';
      const line = '<span'+(sold ? ' style="color:#f0883e"' : '')+'>'+esc(t.verb || 'Traded')+'</span> '+
             n+' <b>'+esc(t.yesno || '')+'</b>'+px+
             (t.pnl ? '<br><span class="'+(t.pnl > 0 ? 'pos' : 'neg')+'">'+
               (t.pnl > 0 ? 'profit +$' : 'loss −$')+Math.abs(t.pnl).toFixed(2)+'</span>' : '');
      // whose order this was — the whole point of the question "is this the
      // earner or something else"; blank means one of the resting rungs
      const src = t.src ? '<span style="font-size:10px;padding:1px 5px;border-radius:4px;'+
            'background:'+(t.src === 'earner' ? 'rgba(90,162,255,.18);color:#9cc7ff'
                                              : 'rgba(217,161,50,.20);color:#f2cd7f')+
            '">'+esc(t.src)+'</span> '
          : '<span class="sub" style="font-size:10px">resting order</span> ';
      return mrow(t.market,
        '<td class="r">'+line+'</td>',
        src+'<span class="sub" style="font-size:11px">'+esc(t.when || '')+'</span>');
    }).join('') + (tx.length > 25 ? '<tr><td class="sub">+' + (tx.length - 25) + ' more</td></tr>' : '')
    : '<tr><td class="sub">no fills since you last cleared ✓</td></tr>';
  document.getElementById('drops').innerHTML = (d.drops || []).length ?
    d.drops.map(x => mrow(x.market,
      '', '<span class="sub">was $'+x.was.toFixed(2)+'</span> → <b class="neg">$'+x.now.toFixed(2)+'/day</b>'))
      .join('')
    : '<tr><td class="sub">nothing has dropped meaningfully</td></tr>';
  const hidden = hidW();
  const win = (d.winners || []).filter(w => !hidden[w.market]);
  const nHid = (d.winners || []).length - win.length;
  document.getElementById('winners').innerHTML = (win.length ?
    win.slice(0, 10).map(w =>
      '<tr><td class="mkt" onclick="openMkt(\\''+esc(w.market)+'\\')"><b style="color:var(--ink);font-size:12px">'+esc(mname(w.market))+'</b></td>'+
      '<td class="r" style="white-space:nowrap" onclick="openMkt(\\''+esc(w.market)+'\\')">'+
      '<b class="pos">$'+w.total.toFixed(2)+'</b><br><span class="sub" style="font-size:11px">last paid '+esc(w.last)+'</span></td>'+
      '<td class="r" style="width:30px"><button class="alt" style="border:none;border-radius:6px;padding:4px 8px;background:var(--surface2);color:var(--ink2)" '+
      'onclick="hideWinner(\\''+esc(w.market)+'\\')">✕</button></td></tr>').join('')
    : '<tr><td class="sub">you have orders everywhere you have earned lately</td></tr>') +
    (nHid ? '<tr><td colspan="3" class="sub" style="font-size:11px">'+nHid+
            ' dismissed · <a href="#" style="color:var(--accent)" onclick="unhideWinners();return false">unhide all</a></td></tr>' : '');
  document.getElementById('newm').innerHTML = (d.new_mkts || []).length ?
    d.new_mkts.map(e => {
      const click = e.kind === 'politics' ? ' onclick="openMkt(\\''+esc(e.label)+'\\')"' : '';
      return '<tr'+click+'><td class="mkt">'+esc(e.label)+
        (e.kind === 'golf' ? ' <span class="bdg">tournament</span>' : '')+'</td>'+
        '<td class="r sub" style="font-size:11px;white-space:nowrap">'+esc(e.when || '')+'</td></tr>';
    }).join('')
    : '<tr><td class="sub">nothing new since tracking began</td></tr>';
}
function closeSheet(){ document.getElementById('sheet').style.display = 'none'; }
let MSHEET = null;
function qStep(){ const v = parseInt(localStorage.getItem('qStep') || '10', 10); return v >= 1 ? v : 10; }
function qStepSet(v){ const n = parseInt(v, 10); if(n >= 1 && n <= 20000) localStorage.setItem('qStep', '' + n); }
function qBump(id, dir){
  const el = document.getElementById(id);
  el.value = Math.max(1, Math.min(20000, (parseInt(el.value, 10) || 0) + dir * qStep()));
}
function mBest(){
  if(!MSHEET) return;
  const side = document.getElementById('mSide').value;
  const lv = side === 'BUY' ? (MSHEET.bids || []) : (MSHEET.asks || []);
  if(!lv.length){ toast('That side of the book is empty — no best price to match.'); return; }
  document.getElementById('mPrice').value = +(lv[0][0]*100).toFixed(2);
}
async function openMkt(m){
  document.getElementById('sheet').style.display = 'block';
  const el = document.getElementById('sheetIn');
  el.innerHTML = '<div class="mkt">'+esc(m)+'</div><div class="sub">loading live book…</div>';
  try{
    const d = await (await fetch('market.json?slug=' + encodeURIComponent(m))).json();
    if(d.error){
      el.innerHTML = '<div class="mkt">'+esc(m)+'</div><div class="err" style="display:block">'+esc(d.error)+
        '</div><div class="rp"><button class="alt" onclick="closeSheet()">Close</button></div>';
      return;
    }
    renderSheet(d);
  }catch(e){
    el.innerHTML = '<div class="err" style="display:block">load failed: '+esc(e)+'</div>';
  }
}
function renderSheet(d){
  MSHEET = d;
  const m = d.market;
  const lv = a => (a && a.length ? a : []).map(x =>
    '<tr><td>'+(+(x[0]*100).toFixed(2))+'¢</td><td class="r">'+x[1].toLocaleString()+'</td></tr>').join('')
    || '<tr><td class="sub">empty</td></tr>';
  // Every order collapses to one line (tap to open its controls), and the
  // deep qualifier blocks — 1c floor bids and 99c ceiling asks, dozens of
  // chunks on some markets — fold behind a single count-and-size line.
  const isQual = o => (o.side === 'BUY' && o.price <= 0.015)
                   || (o.side !== 'BUY' && o.price >= 0.985);
  // How long this order has been resting. A reprice replaces the order, so a
  // small age can mean "the defender just moved an old rung", not "new money".
  const age = iso => {
    if (!iso) return '';
    const s = (Date.now() - Date.parse(iso)) / 1000;
    if (!isFinite(s) || s < 0) return '';
    if (s < 90) return Math.round(s)+'s ago';
    if (s < 5400) return Math.round(s/60)+'m ago';
    if (s < 172800) return (s/3600).toFixed(s < 36000 ? 1 : 0)+'h ago';
    return Math.round(s/86400)+'d ago';
  };
  const mkOrd = o =>
    '<details class="osub"><summary style="cursor:pointer;display:flex;align-items:center;gap:10px;list-style:none">'+
    '<input type="checkbox" class="mck" data-oid="'+o.id+'" onchange="mSelUpd()" '+
    'onclick="event.stopPropagation()" style="width:22px;height:22px;flex:0 0 auto">'+
    '<span style="font-size:14px;font-weight:600">'+o.side+' '+o.size.toLocaleString()+' @ '+
    (+(o.price*100).toFixed(2))+'¢ <span class="sub" style="font-weight:400">· '+
    (o.est_day ? '$'+o.est_day.toFixed(2)+'/day' : '$0/day')+
    (age(o.created) ? ' · placed '+age(o.created) : '')+
    (o.src ? ' · '+o.src : '')+'</span></span>'+
    '<span class="sub" style="margin-left:auto">▾</span></summary>'+
    '<div class="ctlrow" style="margin-top:8px">'+
    '<span class="ctl"><label>price</label><input id="mp'+o.id+'" type="number" step="0.1" min="0.1" max="99.9" value="'+(o.price*100).toFixed(1)+'"><span class="sub">¢</span></span>'+
    '<span class="ctl"><label>qty</label><button class="alt bump" onclick="qBump(\\'mq'+o.id+'\\',-1)">−</button>'+
    '<input id="mq'+o.id+'" type="number" step="1" min="1" max="20000" value="'+Math.round(o.size)+'">'+
    '<button class="alt bump" onclick="qBump(\\'mq'+o.id+'\\',1)">+</button></span></div>'+
    '<div class="ctlrow rp" style="margin-top:10px">'+
    '<button onclick="mModify(\\''+o.id+'\\',\\''+esc(m)+'\\')">Modify</button>'+
    '<button class="alt" style="background:rgba(229,100,95,.18);color:#ff9d99" onclick="mCancel(\\''+o.id+'\\',\\''+esc(m)+'\\')">Cancel</button>'+
    '</div></details>';
  const work = (d.orders || []).filter(o => !isQual(o));
  const qual = (d.orders || []).filter(isQual);
  const qb = qual.filter(o => o.side === 'BUY').reduce((a, o) => a + o.size, 0);
  const qa = qual.filter(o => o.side !== 'BUY').reduce((a, o) => a + o.size, 0);
  const qualParts = [];
  if(qb) qualParts.push(Math.round(qb).toLocaleString()+' bid @ 1¢');
  if(qa) qualParts.push(Math.round(qa).toLocaleString()+' ask @ 99¢');
  const ords =
    (work.map(mkOrd).join('') || (qual.length ? '' : '<div class="sub">no resting orders here</div>'))+
    (qual.length ?
      '<details class="osub"><summary style="cursor:pointer;list-style:none">'+
      '<span style="font-size:13px;font-weight:600">⚓ '+qual.length+' qualifying order'+
      (qual.length > 1 ? 's' : '')+'</span> <span class="sub">· '+qualParts.join(' · ')+
      ' · holds Target Size, earns ~nothing — tap to manage</span></summary>'+
      qual.map(mkOrd).join('')+'</details>' : '');
  document.getElementById('sheetIn').innerHTML =
    '<div style="font-size:17px;font-weight:700">'+esc(mname(m))+'</div>'+
    '<div class="mkt">'+esc(m)+'</div>'+
    (d.net ? '<div class="sub">position: '+d.net.toLocaleString()+' contracts</div>' : '')+
    '<div style="display:flex;gap:18px;margin-top:8px">'+
    '<div style="flex:1"><div class="sub">Bids</div><table class="bk">'+lv(d.bids)+'</table></div>'+
    '<div style="flex:1"><div class="sub">Asks</div><table class="bk">'+lv(d.asks)+'</table></div></div>'+
    '<h3>Your orders</h3>'+
    ((d.orders || []).length > 1 ?
      '<div class="ctlrow" style="margin-bottom:8px;align-items:center">'+
      '<button class="alt" onclick="mSelAll()">Select all</button>'+
      '<button class="alt" id="mSelBtn" disabled '+
      'style="background:rgba(229,100,95,.18);color:#ff9d99" '+
      'onclick="mCancelSel(\\''+esc(m)+'\\')">Cancel selected</button>'+
      '<span class="sub" id="mSelNote"></span></div>' : '')+
    ords+
    '<h3>Place new</h3><div class="osub">'+
    '<div class="ctlrow">'+
    '<span class="ctl"><label>side</label><select id="mSide">'+
    '<option>BUY</option><option>SELL</option></select></span>'+
    '<span class="ctl"><label>price</label><input id="mPrice" type="number" step="0.1" min="0.1" max="99.9" placeholder="0.0"><span class="sub">¢</span></span>'+
    '<button class="alt" style="min-height:40px" onclick="mBest()">match best</button></div>'+
    '<div class="ctlrow">'+
    '<span class="ctl"><label>qty</label><button class="alt bump" onclick="qBump(\\'mSize\\',-1)">−</button>'+
    '<input id="mSize" type="number" step="1" min="1" max="20000" placeholder="0">'+
    '<button class="alt bump" onclick="qBump(\\'mSize\\',1)">+</button></span>'+
    '<span class="ctl"><label>± step</label><input id="qStepIn" type="number" step="1" min="1" max="20000" value="'+qStep()+'" '+
    'style="width:58px" oninput="qStepSet(this.value)"></span></div>'+
    '<div class="ctlrow rp" style="margin-top:10px"><button onclick="mPlace(\\''+esc(m)+'\\')">Place</button></div>'+
    '</div>'+
    '<div class="mkt">post-only — the order rests or is rejected; it can never cross the spread and fill on arrival</div>'+
    qualBlock(d)+
    defendBlock(d)+
    '<div class="rp" style="margin-top:12px"><button class="alt" onclick="closeSheet()">Close</button></div>';
}
function qualBlock(d){
  const q = d.qual || null;
  const m = d.market;
  if(!q || !q.target){
    return '<h3>Qualify</h3><div class="mkt">No active reward program on this market — '+
      'there is no Target Size to reach, so nothing here would earn.</div>';
  }
  const tgt = q.target.toLocaleString();
  const bp = (typeof d.buying_power === 'number') ? d.buying_power : null;
  function row(side, tot, need, priceC, cost){
    const nm = side === 'BUY' ? 'Bid' : 'Ask';
    if(!need){
      return '<div class="mkt" style="color:#3fb950">'+nm+' side ✓ '+tot.toLocaleString()+
        ' of '+tgt+' — qualifying, this side pays</div>';
    }
    // An ask carries one share per DOLLAR of buying power, so a wide gap is
    // several orders. A bid goes in one.
    let per = null, orders = null;
    if(bp !== null && bp > 0){
      per = (side === 'SELL') ? Math.floor(bp) : 10000;
      if(per > 0) orders = Math.ceil(need / per);
    }
    const plan = (orders && orders > 1)
      ? ' in '+orders+' orders of '+per.toLocaleString()
      : '';
    return '<div class="mkt" style="color:#ff9d99">'+nm+' side ✗ '+tot.toLocaleString()+' of '+tgt+
      ' — short '+need.toLocaleString()+', so this side pays nobody</div>'+
      '<div class="rp" style="margin-bottom:8px"><button onclick="mQualify(\\''+esc(m)+'\\',\\''+side+'\\')">'+
      '⚓ Qualify '+nm.toLowerCase()+' — '+need.toLocaleString()+' @ '+priceC+'¢ ≈ $'+cost.toFixed(2)+
      '</button></div>'+
      (plan ? '<div class="mkt">one tap places it'+plan+'</div>' : '');
  }
  return '<h3>Qualify</h3>'+
    '<div class="mkt">A side pays NOBODY until it holds Target Size ('+tgt+' resting contracts, '+
    'everyone\\'s size counted, not just yours). This places the cheapest post-only orders that close '+
    'the gap — floor bid at '+q.floor_c+'¢, ceiling ask at '+q.ceil_c+'¢, where a contract ties up the '+
    'least capital. It unlocks the pool for the side; on its own it earns you almost nothing, because '+
    'an order that far from the touch scores about zero. It pays when you also hold an order near the '+
    'touch on the same side. Size and price are recomputed from the live book when you tap. A bid goes '+
    'in as one order; an ask can only carry one share per dollar of buying power, so a wide ask gap '+
    'goes in as several — one tap does them all, re-reading buying power between each.</div>'+
    row('BUY', q.bid_total, q.need_bid, q.floor_c, q.cost_bid)+
    row('SELL', q.ask_total, q.need_ask, q.ceil_c, q.cost_ask);
}
async function mQualify(m, side){
  const nm = side === 'BUY' ? 'bid' : 'ask';
  if(!arm('ql'+m+side, 'Qualify the '+nm+' side — cheapest orders to reach Target Size')) return;
  try{
    const r = await fetch('maction', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify({op:'qualify', market:m, side:side})});
    const d = await r.json().catch(() => ({ok:false, error:'HTTP '+r.status}));
    if(!d.ok){
      toast('Failed: ' + (d.detail || d.error || ('HTTP '+r.status)));
    } else if(!d.placed){
      toast(d.note || 'Nothing to do');
    } else {
      let msg = 'Placed '+d.placed+' order'+(d.placed>1?'s':'')+' — '+
        (d.size||0).toLocaleString()+' @ '+d.price_cents+'¢, ~$'+(d.spent||0).toFixed(2)+' locked';
      if(d.remaining_gap) msg += ' · '+d.remaining_gap.toLocaleString()+' still short, tap again';
      else if(d.remaining_gap === 0) msg += ' · side qualifying ✓';
      if(d.capped_by_budget) msg += ' (capped by buying power)';
      toast(msg);
    }
  }catch(e){ toast('Failed: '+e); }
  setTimeout(function(){ openMkt(m); refresh(); }, 1500);
}
function defendBlock(d){
  const m = d.market;
  const df = d.defend || null;
  const tick = (d.tick || 0.01) * 100;
  const bb = (d.bids && d.bids.length) ? d.bids[0][0]*100 : null;
  const ba = (d.asks && d.asks.length) ? d.asks[0][0]*100 : null;
  const dfb = df && df.BUY ? df.BUY.cap : (bb != null ? +(bb + 3*tick).toFixed(2) : '');
  const dfa = df && df.SELL ? df.SELL.cap : (ba != null ? +(ba - 3*tick).toFixed(2) : '');
  return '<h3>Defend'+(df ? ' — <span style="color:#3fb950">on 🛡</span>' : '')+'</h3>'+
    '<div class="mkt">Moves your best order one tick forward whenever it\\'s earning under 25% of '+
    'this side\\'s rewards — outbid, matched by real size, or a big order parked right behind you. '+
    'A healthy share is left alone. Same size, never a new order; stops at your limits below; '+
    'stands down when the spread gets tight; floor/ceiling qualifier orders are never touched.</div>'+
    '<div class="rp">bid up to <input id="dfBid" type="number" step="0.1" min="0.1" max="99.9" '+
    'value="'+dfb+'" style="width:72px">¢ · ask down to <input id="dfAsk" type="number" step="0.1" '+
    'min="0.1" max="99.9" value="'+dfa+'" style="width:72px">¢ '+
    '<button onclick="mDefend(\\''+esc(m)+'\\')">'+(df ? 'Update' : 'Defend')+'</button>'+
    (df ? '<button class="alt" style="background:rgba(229,100,95,.18);color:#ff9d99" onclick="mUndefend(\\''+esc(m)+'\\')">Stop</button>' : '')+
    '</div>'+
    '<div class="mkt">clear a box to leave that side undefended · if the price runs past your limit it simply stops following</div>';
}
function mDefend(m){
  const b = document.getElementById('dfBid').value;
  const a = document.getElementById('dfAsk').value;
  const body = {op:'defend', market:m};
  if(b !== '') body.bid_cap_c = parseFloat(b);
  if(a !== '') body.ask_floor_c = parseFloat(a);
  if(body.bid_cap_c === undefined && body.ask_floor_c === undefined){
    toast('Enter a bid cap, an ask floor, or both.'); return;
  }
  const parts = [];
  if(body.bid_cap_c !== undefined) parts.push('bid to '+body.bid_cap_c+'¢');
  if(body.ask_floor_c !== undefined) parts.push('ask to '+body.ask_floor_c+'¢');
  if(!arm('df'+m, 'Defend '+parts.join(' + '))) return;
  mact(body, m);
}
function mUndefend(m){
  if(!arm('udf'+m, 'Stop defending this market')) return;
  mact({op:'undefend', market:m}, m);
}
async function mact(body, m){
  try{
    const r = await fetch('maction', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify(body)});
    const d = await r.json().catch(() => ({ok:false, error:'HTTP '+r.status}));
    toast(d.ok ? 'Done ✓' : 'Failed: ' + (d.detail || d.error || ('HTTP '+r.status)));
  }catch(e){ toast('Failed: '+e); }
  setTimeout(function(){ openMkt(m); refresh(); }, 1200);
}
function mModify(id, m){
  const c = parseFloat(document.getElementById('mp'+id).value);
  const q = parseInt(document.getElementById('mq'+id).value, 10);
  if(!(c >= 0.1 && c <= 99.9)){ toast('Price out of range (0.1–99.9¢)'); return; }
  if(!(q >= 1 && q <= 20000)){ toast('Size out of range (1–20,000)'); return; }
  if(!arm('mod'+id, 'Modify to '+q.toLocaleString()+' @ '+c+'¢')) return;
  mact({op:'modify', order_id:id, price_cents:c, size:q}, m);
}
function mCancel(id, m){
  if(!arm('can'+id, 'Cancel this order')) return;
  mact({op:'cancel', order_id:id}, m);
}
// --- batch cancel: tick boxes, one armed confirm, sequential cancels ----
function mSel(){
  return Array.from(document.querySelectorAll('.mck:checked')).map(c => c.dataset.oid);
}
function mSelUpd(){
  const n = mSel().length;
  const b = document.getElementById('mSelBtn');
  if(!b) return;
  b.disabled = !n;
  b.textContent = n ? 'Cancel selected ('+n+')' : 'Cancel selected';
}
function mSelAll(){
  const all = document.querySelectorAll('.mck');
  const on = mSel().length < all.length;   // any unchecked -> check all; else clear
  all.forEach(c => { c.checked = on; });
  mSelUpd();
}
async function mCancelSel(m){
  const ids = mSel();
  if(!ids.length) return;
  if(!arm('bcx'+m, 'Cancel '+ids.length+' order'+(ids.length>1?'s':''))) return;
  const b = document.getElementById('mSelBtn');
  if(b) b.disabled = true;
  let ok = 0, bad = 0;
  for(let i = 0; i < ids.length; i++){
    if(b) b.textContent = 'cancelling '+(i+1)+'/'+ids.length+'…';
    try{
      const r = await fetch('maction', {method:'POST',
        headers:{'Content-Type':'application/json','X-Reprice':'1'},
        body: JSON.stringify({op:'cancel', order_id:ids[i]})});
      const d = await r.json().catch(() => ({ok:false}));
      d.ok ? ok++ : bad++;
    }catch(e){ bad++; }
    await new Promise(res => setTimeout(res, 350));
  }
  toast('Cancelled '+ok+' ✓'+(bad ? ' · '+bad+' failed' : ''));
  setTimeout(function(){ openMkt(m); refresh(); }, 1200);
}
function mPlace(m){
  const side = document.getElementById('mSide').value;
  const c = parseFloat(document.getElementById('mPrice').value);
  const q = parseInt(document.getElementById('mSize').value, 10);
  if(!(c >= 0.1 && c <= 99.9)){ toast('Price out of range (0.1–99.9¢)'); return; }
  if(!(q >= 1 && q <= 20000)){ toast('Size out of range (1–20,000)'); return; }
  const cap = side === 'BUY' ? c/100*q : (1 - c/100)*q;
  if(!arm('pl'+m, side+' '+q.toLocaleString()+' @ '+c+'¢, locks ~$'+cap.toFixed(2))) return;
  mact({op:'place', market:m, side:side, price_cents:c, size:q}, m);
}
async function renderAll(d){
  try{
    setEarned(d.earned_today, d.rate_per_day);
    try{
      const et = new Date(new Date().toLocaleString('en-US', {timeZone: 'America/New_York'}));
      const hf = et.getHours() + et.getMinutes() / 60;
      let frac = hf / 24;
      const cf = d.pace_cum;
      if(cf && cf.length === 25){
        const i = Math.floor(hf);
        frac = cf[i] + (cf[Math.min(i + 1, 24)] - cf[i]) * (hf - i);
      }
      const pace = frac > 0.03 ? d.earned_today / frac : null;
      const y = (d.history || [])[0];
      document.getElementById('pace').textContent =
        (pace ? 'on pace for ~$' + pace.toFixed(0) + ' today' : '') +
        (y ? (pace ? '  ·  ' : '') + 'yesterday $' + y.earned.toFixed(2) +
             (y.paid != null ? ' (paid $' + y.paid.toFixed(2) + ')' : '') : '');
    }catch(_){}
    const nMkts = new Set(d.orders.map(o => o.market).filter(Boolean)).size;
    document.getElementById('rate').textContent =
      'current rate ~$' + d.rate_per_day.toFixed(2) + '/day across ' + nMkts +
      ' markets (' + d.orders.length + ' orders)';
    document.getElementById('updated').textContent = 'updated ' + d.updated + ' · day resets midnight ET · saves: ' + d.persistence + ' · alerts: ' + d.alerts +
      ' · books: ' + (d.ws && d.ws.live ? '⚡ streaming ('+d.ws.markets+')'
                      : 'polling' + (d.ws && d.ws.err ? ' — stream ' + d.ws.state + ': ' + d.ws.err : '')) +
      (d.warming ? ' · ⏳ warming up: ' + d.warming + ' markets on saved rates' : '') +
      (d.backfilled ? ' · ♻️ counter rebuilt from tracker data ($' + d.backfilled.toFixed(2) + ' at boot)' : '');
    const err = document.getElementById('err');
    const diag = Object.entries(d.diag || {}).map(([k,v]) => k.replace(/^_/,'') + ': ' + v).join(' · ');
    const msg = [d.error, diag].filter(Boolean).join(' · ');
    err.style.display = msg ? 'block' : 'none'; err.textContent = msg;
    document.getElementById('ovg').innerHTML =
      '<div class="chips" style="margin:2px 0 6px">'+
      '<button class="chip'+(heroMode()==='day' ? ' chipon' : '')+'" onclick="setHeroMode(\\'day\\')">earnings</button>'+
      '<button class="chip'+(heroMode()==='rate' ? ' chipon' : '')+'" onclick="setHeroMode(\\'rate\\')">rate</button>'+
      '<button class="chip'+(heroMode()==='zoom' ? ' chipon' : '')+'" onclick="setHeroMode(\\'zoom\\')">live 15m</button></div>'+
      (heroMode() === 'day' ? dayGraph(d)
        : heroMode() === 'zoom' ? rateZoomGraph(d) : rateDayGraph(d));
    renderHome(d);
    BP = d.buying_power;
    document.getElementById('planBP').textContent =
      BP != null ? 'Buying power: $' + BP.toFixed(2) + ' per market, minus what your existing orders there already lock — maxed-out markets are hidden' : '';
    const allMarkets = {};
    d.orders.forEach(o => { if(o.market) allMarkets[o.market] = 0; });
    Object.entries(d.per_market_today).forEach(([m,v]) => { allMarkets[m] = v; });
    RATES = {};
    d.orders.forEach(o => { if(o.market) RATES[o.market] = (RATES[o.market]||0) + (o.est_day||0); });
    OLOCK = {};  // capital your resting orders already lock, per market
    d.orders.forEach(o => { if(o.market){
      const l = o.side === 'SELL' ? (1 - o.price) * o.size : o.price * o.size;
      OLOCK[o.market] = (OLOCK[o.market] || 0) + l; } });
    if(Object.values(GOPEN).some(v=>v)){
      try{ SERIES = (await (await fetch('series.json')).json()).series || {}; }catch(_){}
    }
    const SPOOL = {};
    d.orders.forEach(o => { if(o.market && o.side_pool) SPOOL[o.market] = o.side_pool; });
    PCTS = {};
    Object.keys(allMarkets).forEach(mm => {
      const sp = SPOOL[mm];
      PCTS[mm] = sp ? Math.min(100, (RATES[mm]||0) / (2*sp) * 100) : null;
    });
    if(PCTBASE === null){  // baseline = the pcts as of your LAST visit
      try{ PCTBASE = JSON.parse(localStorage.getItem('pctSeen') || '{}'); }catch(e){ PCTBASE = {}; }
    }
    const pstore = {};
    Object.keys(PCTS).forEach(k => { if(PCTS[k] != null) pstore[k] = +PCTS[k].toFixed(1); });
    localStorage.setItem('pctSeen', JSON.stringify(pstore));
    const cats = {};
    Object.keys(allMarkets).forEach(mm => { const c = mcat(mm); cats[c] = (cats[c]||0)+1; });
    const hc = hidCats();
    const DEFENDED = new Set(d.defend || []);
    document.getElementById('catBar').innerHTML =
      '<label class="sub" style="margin-right:8px"><input type="checkbox" '+(pctMode()?'checked':'')+
      ' onchange="tglPct()"> % of rewards</label>' +
      '<select onchange="setMSort(this.value)" style="background:var(--surface2);color:var(--ink2);'+
      'border:1px solid var(--line);border-radius:8px;padding:6px;font-size:11px;margin-right:8px">'+
      '<option value="rate"'+(mSort()==='rate'?' selected':'')+'>sort: rate</option>'+
      '<option value="chg-desc"'+(mSort()==='chg-desc'?' selected':'')+'>sort: biggest % gain</option>'+
      '<option value="chg-asc"'+(mSort()==='chg-asc'?' selected':'')+'>sort: biggest % drop</option></select>'+
      '<label class="sub" style="margin-right:8px"><input type="checkbox" '+(sortCat()?'checked':'')+
      ' onchange="tglSortCat()"> group by category</label>' +
      Object.keys(cats).sort().map(c =>
        '<button class="tab" style="font-size:11px;padding:4px 10px;margin:2px'+
        (hc[c]?';opacity:.4':'')+'" onclick="tglCat(\\''+esc(c)+'\\')">'+esc(c)+' ('+cats[c]+')'+
        (hc[c]?' ✕':'')+'</button>').join('');
    document.getElementById('markets').innerHTML =
      Object.entries(allMarkets)
        .filter(([m]) => !hc[mcat(m)])
        .sort((a,b) => {
          if(sortCat() && mcat(a[0]) !== mcat(b[0])) return mcat(a[0]) < mcat(b[0]) ? -1 : 1;
          if(mSort() === 'chg-desc') return pctChg(b[0]) - pctChg(a[0]);
          if(mSort() === 'chg-asc') return pctChg(a[0]) - pctChg(b[0]);
          return (RATES[b[0]]||0) - (RATES[a[0]]||0) || b[1] - a[1];
        })
        .map(([m,v],i) => {
        const rate = RATES[m] || 0;
        const dead = d.orders.some(o => o.market === m) &&
                     d.orders.filter(o => o.market === m).every(o => !o.est_day);
        const detail = d.orders.filter(o => o.market === m).map(o => {
          const est = o.est_day ? '$' + o.est_day.toFixed(2) + '/day' : '$0';
          const rows = (o.window || []).map(([px,qty,me,t,c]) =>
            '<tr'+(me?' class="me"':'')+'><td>'+(me?'▶ ':'')+px+'¢</td><td class="r">'+qty.toLocaleString()+
            (me?' ('+o.size.toLocaleString()+' yours)':'')+'</td><td class="r">×'+o.df+'^'+t+' = '+c.toFixed(1)+'</td></tr>').join('') +
            (o.window_more ? '<tr><td>…</td><td class="r">+'+o.window_more+' levels</td><td class="r">'+
              (o.window_more_score||0).toFixed(1)+'</td></tr>' : '') +
            (o.denom != null ? '<tr><td></td><td class="r">Σ</td><td class="r"><b>'+o.denom.toFixed(1)+'</b></td></tr>' : '');
          const calc = (o.calc || []).map(c => '<div class="calc">'+esc(c)+'</div>').join('');
          const sibs = (o.event_n > 1 && o.siblings && o.siblings.length) ?
            '<details><summary class="mkt">÷ '+o.event_n+' markets in this race — list</summary>'+
            '<div class="mkt" style="padding:4px 0 0 8px">'+
            o.siblings.map((s,j)=>(j+1)+'. '+esc(s)+(s===o.market?' ←':'')).join('<br>')+
            '</div></details>' : '';
          const best = (o.window && o.window.length) ? o.window[0][0] : null;
          const rp = o.id ?
            '<div class="rp"><input id="p'+o.id+'" type="number" step="0.1" min="0.1" max="99.9" value="'+
            (o.price*100).toFixed(1)+'">¢'+
            (best !== null ? '<button class="alt" onclick="event.stopPropagation();document.getElementById(\\'p'+o.id+'\\').value='+best+'">best '+best+'¢</button>' : '')+
            '<button onclick="event.stopPropagation();reprice(\\''+o.id+'\\',\\''+esc(o.market)+' '+o.side+'\\')">Reprice</button></div>' : '';
          return '<div class="ord" onclick="event.stopPropagation()"><div class="oh">'+o.side+' '+o.size.toLocaleString()+' @ '+
            (o.price*100).toFixed(1)+'¢ → '+est+
            (o.batch?' <span class="bdg">batch</span>':'')+
            '</div><table class="bk">'+rows+'</table>'+calc+sibs+rp+'</div>';
        }).join('');
        const gcell = GOPEN[m] && SERIES ? spark(SERIES[m]) : '';
        const pct = PCTS[m];
        const rateTxt = pctMode()
          ? (dead ? '<b style="color:#d29922">⚠️ 0%</b>' + pctArrow(m)
                  : (pct == null ? '<b>—</b>'
                     : '<b>'+pct.toFixed(0)+'%</b>' + pctArrow(m) +
                       '<br><span class="sub" style="font-size:10px">of this market\\'s daily rewards</span>'))
          : (dead ? '<b style="color:#d29922">⚠️ $0.00/day</b>'
                  : '<b>$'+rate.toFixed(2)+'/day</b>');
        const hasBatch = d.orders.some(o => o.market === m && o.batch);
        return '<tr id="r'+i+'" onclick="tgl('+i+',\\''+esc(m)+'\\')" style="'+tint(m, rate)+'">'+
          '<td class="mkt"><b style="color:var(--ink);font-size:12px">'+esc(mname(m))+'</b>'+(hasBatch?' <span class="bdg">batch</span>':'')+
          (DEFENDED.has(m)?' 🛡':'')+'<div style="font-size:9px">'+m+'</div>'+
          '</td><td class="r" style="white-space:nowrap">'+rateTxt+
          '<br><span class="sub" style="font-size:11px">$'+v.toFixed(2)+' today</span>'+
          ' <button class="alt" style="border:none;border-radius:6px;padding:4px 8px;background:var(--surface2);color:var(--ink2)" '+
          'onclick="event.stopPropagation();tglGraph('+i+',\\''+esc(m)+'\\')">📈</button>'+
          ' <button class="alt" style="border:none;border-radius:6px;padding:4px 8px;background:var(--surface2);color:var(--ink2)" '+
          'onclick="event.stopPropagation();openMkt(\\''+esc(m)+'\\')">⚙</button></td></tr>' +
          '<tr id="g'+i+'" style="display:'+(GOPEN[m]?'':'none')+'"><td colspan="2" style="background:var(--surface2)">'+gcell+'</td></tr>' +
          '<tr id="d'+i+'" style="display:'+(OPEN[m]?'':'none')+'"><td colspan="2" ' +
          'style="background:var(--surface2)">'+detail+'</td></tr>';
      }).join('') || '<tr><td>nothing yet today</td></tr>';
    document.getElementById('history').innerHTML =
      '<tr><th>Day</th><th class="r">Tracked</th><th class="r">Polymarket paid</th></tr>' +
      d.history.map(h => {
        let cap = '';
        if(h.paid != null && h.earned > 0){
          const p = h.paid / h.earned * 100;
          const c = p >= 85 ? 'var(--good)' : p >= 60 ? 'var(--warn)' : 'var(--bad)';
          cap = ' <span style="color:'+c+';font-size:11px;font-weight:600">'+p.toFixed(0)+'%</span>';
        }
        return '<tr><td>'+h.day+'</td><td class="r">$'+h.earned.toFixed(2)+'</td>'+
          '<td class="r">'+(h.paid == null ? '<span class="sub">not posted yet</span>'
            : '<b>$'+h.paid.toFixed(2)+'</b>'+cap+(h.pending ? ' <span class="sub">(pending)</span>' : ''))+
          '</td></tr>';
      }).join('')
      || '<tr><td>collecting…</td></tr>';
    document.getElementById('acts').innerHTML = (d.actions && d.actions.length) ?
      '<h3>Recent actions</h3>' + d.actions.map(a =>
        '<div class="mkt" style="margin:4px 0">'+(a.verified?'✅':'⚠️')+' '+a.ts+' — '+esc(a.market)+' '+a.side+
        ' '+a.from+'¢ → '+a.to+'¢ ('+a.size+') · HTTP '+a.status+' · '+esc(a.note||a.response||'')+'</div>').join('') : '';
  }catch(e){}
}
async function refresh(){
  try{
    const r = await fetch('data.json');
    if(!r.ok) return;
    const t = await r.text();
    try{ localStorage.setItem('lastData', t); }catch(_){}
    LAST_OK = Date.now();
    renderAll(JSON.parse(t));
  }catch(e){}
}
// paint instantly from the last visit's data, then refresh live
try{ const c = localStorage.getItem('lastData'); if(c) renderAll(JSON.parse(c)); }catch(_){}
refresh(); setInterval(refresh, 15000);
</script></body></html>"""


_ICON_CACHE: bytes | None = None


def _icon_png() -> bytes:
    """The home-screen icon, drawn in code (no image libs): four rising
    emerald bars on the app's slate background — 180×180 truecolor PNG."""
    global _ICON_CACHE
    if _ICON_CACHE is not None:
        return _ICON_CACHE
    import struct
    import zlib
    w = h = 180
    bg, bar, bar_hi = (23, 28, 38), (52, 192, 124), (90, 162, 255)
    px = [[bg] * w for _ in range(h)]
    base = 146
    for x0, top, col in ((26, 104, bar), (64, 84, bar), (102, 62, bar_hi), (140, 38, bar)):
        for y in range(top, base):
            for x in range(x0, x0 + 22):
                px[y][x] = col
    raw = b"".join(b"\x00" + bytes(c for p in row for c in p) for row in px)

    def chunk(tag: bytes, data: bytes) -> bytes:
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))

    _ICON_CACHE = (b"\x89PNG\r\n\x1a\n"
                   + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                   + chunk(b"IDAT", zlib.compress(raw, 9))
                   + chunk(b"IEND", b""))
    return _ICON_CACHE


class Handler(BaseHTTPRequestHandler):
    def _authed(self) -> bool:
        """The page remembers the password once (X-Dash-Key header from
        localStorage) — no more browser login popups. ?key= works for
        widgets/Shortcuts, and legacy Basic auth still passes."""
        if not DASH_PASSWORD:
            return False
        if self.headers.get("X-Dash-Key") == DASH_PASSWORD:
            return True
        from urllib.parse import parse_qs, urlparse
        if (parse_qs(urlparse(self.path).query).get("key") or [""])[0] == DASH_PASSWORD:
            return True
        header = self.headers.get("Authorization", "")
        if header.startswith("Basic "):
            try:
                decoded = base64.b64decode(header[6:]).decode()
                return decoded.split(":", 1)[1] == DASH_PASSWORD
            except Exception:  # noqa: BLE001
                return False
        return False

    def do_GET(self) -> None:  # noqa: N802 — http.server API
        if not DASH_PASSWORD:
            self._send(503, "text/plain", b"Set the DASH_PASSWORD environment variable to enable the dashboard.")
            return
        if self.path == "/" or self.path.startswith("/index"):
            # The shell holds no data — serve it instantly, unauthenticated.
            # The page's own login card gates the data underneath.
            self._send(200, "text/html; charset=utf-8", DASH_HTML.encode())
            return
        if ((self.path.startswith("/map") and not self.path.startswith("/map.json"))
                or self.path.startswith("/lab")):
            # shell only, no data — same pattern as "/": the page's own login
            # card gates everything underneath it. /lab is the same shell on a
            # different route: the prober and earner read-outs are analysis and
            # do not belong on the control surface (owner, 2026-08-16).
            self._send(200, "text/html; charset=utf-8", MAP_HTML.encode())
            return
        if self.path.startswith("/garden"):
            # The garden view: same shell pattern — the page itself is
            # public, every data fetch inside it carries the key header.
            try:
                with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       "garden.html"), "rb") as f:
                    body = f.read()
            except OSError:
                body = b"garden view not deployed"
            self._send(200, "text/html; charset=utf-8", body)
            return
        if self.path.startswith("/assets/"):
            # Static sprite art for the garden (CC0, see ATTRIBUTION.txt).
            name = os.path.basename(self.path.split("?")[0])
            p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", name)
            if name.endswith(".png") and os.path.isfile(p):
                with open(p, "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-Type", "image/png")
                    self.send_header("Cache-Control", "public, max-age=86400")
                    body = f.read()
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
            else:
                self._send(404, "text/plain", b"not found")
            return
        if self.path.startswith("/manifest.json"):
            self._send(200, "application/json", json.dumps({
                "name": "Liquidity Rewards", "short_name": "Rewards",
                "display": "standalone", "start_url": "/",
                "background_color": "#1a202b", "theme_color": "#1a202b",
                "icons": [{"src": "/icon.png", "sizes": "180x180",
                           "type": "image/png"}]}).encode())
            return
        if self.path.startswith("/icon.png"):
            self._send(200, "image/png", _icon_png())
            return
        if self.path.startswith("/widget.json"):
            if not self._authed():
                self._send(401, "application/json", b'{"error": "key required"}')
                return
            with MONITOR.lock:
                payload = {
                    "earned_today": round(MONITOR.state.get("earned") or 0.0, 2),
                    "rate_per_day": round(MONITOR.rate, 2),
                    "markets": len({o.get("market") for o in MONITOR.orders if o.get("market")}),
                    "updated": (MONITOR.updated.astimezone(ET).strftime("%I:%M %p ET")
                                if MONITOR.updated else None),
                    "error": bool(MONITOR.error),
                }
            self._send(200, "application/json", json.dumps(payload).encode())
            return
        if not self._authed():
            # plain 401, no WWW-Authenticate: the page shows its own login
            # card instead of the browser interrupting with a popup
            self._send(401, "application/json", b'{"error": "key required"}')
            return
        if self.path.startswith("/map.json"):
            self._send(200, "application/json", json.dumps(_map_payload()).encode())
            return
        if self.path.startswith("/data.json"):
            self._send(200, "application/json", json.dumps(MONITOR.snapshot()).encode())
        elif self.path.startswith("/plan.json"):
            try:
                from urllib.parse import parse_qs, urlparse
                q = parse_qs(urlparse(self.path).query)
                which = (q.get("which") or ["politics"])[0]
                if which == "restore":
                    plan = _restore_plan(float((q.get("ago") or ["1800"])[0]))
                else:
                    plan = fetch_plan(which)
                mine = sorted({o.get("market") for o in MONITOR.orders if o.get("market")})
                self._send(200, "application/json",
                           json.dumps({"plan": plan, "mine": mine}).encode())
            except Exception as e:  # noqa: BLE001
                self._send(502, "application/json",
                           json.dumps({"error": str(e)[:200]}).encode())
        elif self.path.startswith("/place_status"):
            self._send(200, "application/json", json.dumps(
                {k: PLACER[k] for k in ("running", "results", "total", "summary")}).encode())
        elif self.path.startswith("/dead_plan"):
            self._send(200, "application/json",
                       json.dumps({"plan": compute_dead_orders()}).encode())
        elif self.path.startswith("/reprice_plan"):
            try:
                from urllib.parse import parse_qs, urlparse
                q = parse_qs(urlparse(self.path).query)
                min_off = max(0, min(3, int(q.get("offset", ["1"])[0])))
            except Exception:  # noqa: BLE001
                min_off = 1
            self._send(200, "application/json",
                       json.dumps({"plan": compute_reprice_plan(min_off)}).encode())
        elif self.path.startswith("/series.json"):
            with MONITOR.lock:
                payload = json.dumps({"series": MONITOR.state.get("series", {})})
            self._send(200, "application/json", payload.encode())
        elif self.path.startswith("/seats.json"):
            self._send(200, "application/json", json.dumps(seats_overview()).encode())
        elif self.path.startswith("/positions.json"):
            self._send(200, "application/json", json.dumps(positions_overview()).encode())
        elif self.path.startswith("/market.json"):
            from urllib.parse import parse_qs, urlparse
            slug = (parse_qs(urlparse(self.path).query).get("slug") or [""])[0]
            code, payload = market_info(slug)
            self._send(code, "application/json", json.dumps(payload).encode())
        else:
            self._send(200, "text/html; charset=utf-8", DASH_HTML.encode())

    def do_POST(self) -> None:  # noqa: N802 — http.server API
        if not DASH_PASSWORD or not self._authed():
            self._send(401, "application/json", b'{"error": "key required"}')
            return
        if self.path not in ("/reprice", "/place", "/place_abort", "/cancel_all",
                             "/reprice_batch", "/cancel_batch", "/maction"):
            self._send(404, "text/plain", b"not found")
            return
        # Cross-origin requests can't set custom headers without a CORS
        # preflight (which we never grant) — this blocks CSRF.
        if self.headers.get("X-Reprice") != "1":
            self._send(403, "text/plain", b"missing X-Reprice header")
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length)) if length else {}
        except Exception:  # noqa: BLE001
            self._send(400, "application/json", b'{"ok": false, "error": "bad request"}')
            return
        if self.path == "/place":
            code, payload = start_batch(body)
        elif self.path == "/reprice_batch":
            code, payload = start_reprice_batch(body)
        elif self.path == "/cancel_batch":
            code, payload = start_cancel_batch(body)
        elif self.path == "/place_abort":
            PLACER["abort"] = True
            code, payload = 200, {"ok": True}
        elif self.path == "/cancel_all":
            code, payload = do_cancel_all()
        elif self.path == "/maction":
            code, payload = do_maction(body)
        else:
            try:
                order_id, cents = str(body["order_id"]), float(body["price_cents"])
            except Exception:  # noqa: BLE001
                self._send(400, "application/json", b'{"ok": false, "error": "bad request"}')
                return
            code, payload = do_reprice(order_id, cents)
        self._send(code, "application/json", json.dumps(payload).encode())

    def _send(self, code: int, ctype: str, body: bytes) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        # gzip everything sizeable — data.json shrinks ~10x, the single
        # biggest first-load win on a phone connection
        if len(body) > 500 and "gzip" in (self.headers.get("Accept-Encoding") or ""):
            body = gzip.compress(body, 6)
            self.send_header("Content-Encoding", "gzip")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args) -> None:  # quiet
        pass


def _golf_tournament(slug: str) -> str | None:
    """Collapse a golfer market slug to its tournament (through the date)."""
    parts = slug.split("-")
    for i in range(len(parts) - 2):
        if (parts[i].isdigit() and len(parts[i]) == 4
                and parts[i + 1].isdigit() and parts[i + 2].isdigit()):
            return "-".join(parts[:i + 3])
    return None


def poll_loop(key_id: str, secret_key: str) -> None:
    global WINNERS
    event_sizes: dict[str, int] = {}
    events_refreshed = 0.0
    pos_refreshed = 0.0
    act_refreshed = 0.0
    act_quick = 0.0
    golf_refreshed = 0.0
    winners_refreshed = 0.0
    profile_refreshed = 0.0
    anchor_refreshed = 0.0
    last_ok = time.time()
    err_notified = 0.0
    err_streak = 0
    while True:
        if PLACER["running"]:  # a batch owns the request budget — pause polling
            POLL_KICK.wait(10)
            POLL_KICK.clear()
            continue
        try:
            if time.time() - events_refreshed > 900:  # refresh proration map every 15 min
                events_refreshed = time.time()
                try:
                    pol_slugs, event_sizes = tr.fetch_politics_events()
                    MONITOR.note_markets(list(pol_slugs), "politics")
                    watch_program_arrivals(list(pol_slugs))
                except Exception:  # noqa: BLE001 — keep last known map
                    pass
            if time.time() - golf_refreshed > 3600:  # new-tournament check hourly
                golf_refreshed = time.time()
                try:
                    import scan_markets as sm
                    golf_slugs, _ = sm.fetch_tag_events(sm.GOLF_TAGS)
                    tours = sorted({t for t in (_golf_tournament(s) for s in golf_slugs) if t})
                    MONITOR.note_markets(tours, "golf")
                except Exception:  # noqa: BLE001 — discovery is best-effort
                    pass
            if time.time() - anchor_refreshed > 1800:  # hourly-record anchor
                anchor_refreshed = time.time()
                try:
                    today_a = dt.datetime.now(ET).strftime("%Y-%m-%d")
                    reb = tracker_day_integral(today_a)
                    if reb is not None:
                        with MONITOR.lock:
                            if MONITOR.state.get("day") == today_a:
                                MONITOR.state["earned"] = reb[0]
                                MONITOR.state["per_market"] = reb[1]
                except Exception:  # noqa: BLE001 — accrual carries on unanchored
                    pass
            now_et_dig = dt.datetime.now(ET)
            if (now_et_dig.hour * 60 + now_et_dig.minute >= 485  # 8:05am ET
                    and MONITOR.state.get("digest_day") != now_et_dig.strftime("%Y-%m-%d")):
                MONITOR.state["digest_day"] = now_et_dig.strftime("%Y-%m-%d")
                try:
                    digest = day_shape_digest()
                    if digest:
                        notify("Daily earnings shape", digest, "default")
                except Exception:  # noqa: BLE001 — the report never breaks the loop
                    pass
            if time.time() - profile_refreshed > 6 * 3600:  # intraday pace curve
                profile_refreshed = time.time()
                try:
                    MONITOR.day_profile = intraday_profile() or MONITOR.day_profile
                except Exception:  # noqa: BLE001 — pace falls back to flat
                    pass
            if time.time() - winners_refreshed > 3600:  # career totals + payout alert
                winners_refreshed = time.time()
                try:
                    winners, rew_total, day_paid = load_winners()
                    if winners:
                        WINNERS = winners
                    MONITOR.day_paid = day_paid
                    if rew_total:
                        MONITOR.note_rewards_total(rew_total)
                except Exception:  # noqa: BLE001
                    pass
            # keep the probe universe's books flowing even when no orders
            # rest there — discovery must not depend on being invested
            try:
                # prefix match alone gives 1,173 markets, most resolved or
                # dead; the ones worth a book are those carrying a reward
                # program (~176). The program cache knows which those are.
                progs_ = (tr._PROG_CACHE.get("progs") or {})
                tr.EXTRA_SLUGS = {
                    m for m in progs_
                    if m.startswith(PROBE_PREFIXES)} or {
                    m for m in ((MONITOR.state.get("known_mkts") or {})
                                .get("politics") or [])
                    if m.startswith(PROBE_PREFIXES)
                    and "2028" in m}      # cold start: the slate alone, bounded
            except Exception:  # noqa: BLE001 — never let this stop the poll
                pass
            orders = tr.fetch_live_orders(key_id, secret_key, event_sizes)
            MONITOR.sample(dt.datetime.now(dt.timezone.utc), orders)
            MONITOR.error = None
            err_streak = 0
            last_ok = time.time()
            try:
                refresh_defend_seed()   # config changes land without a redeploy
            except Exception:  # noqa: BLE001 — config refresh never kills the poll
                pass
            try:
                auto_defend()
                try:
                    keep_qualified()
                except Exception as e:  # noqa: BLE001 — keeper never kills the poll
                    MONITOR.error = f"keeper: {type(e).__name__}: {e}"[:150]
                try:
                    auto_snipe()
                except Exception as e:  # noqa: BLE001 — sniper never kills the poll
                    MONITOR.error = f"snipe: {type(e).__name__}: {e}"[:150]
                try:
                    slate_health_check()
                except Exception:  # noqa: BLE001 — the watch never kills the poll
                    pass
                try:
                    auto_probe()
                except Exception as e:  # noqa: BLE001 — prober never kills the poll
                    MONITOR.error = f"probe: {type(e).__name__}: {e}"[:150]
                try:
                    auto_earn()
                except Exception as e:  # noqa: BLE001 — earner never kills the poll
                    MONITOR.error = f"earn: {type(e).__name__}: {e}"[:150]
            except Exception as e:  # noqa: BLE001 — defense never kills the poll
                MONITOR.error = f"defend: {type(e).__name__}: {e}"[:150]
            MONITOR.maybe_save_remote()
            if time.time() - pos_refreshed > POS_REFRESH_SECONDS:  # P/L + Plan tab data
                pos_refreshed = time.time()
                try:
                    MONITOR.set_positions(fetch_positions(key_id, secret_key))
                    MONITOR.pnl_error = None
                except Exception as e:  # noqa: BLE001 — shown on the P/L tab
                    MONITOR.pnl_error = f"{type(e).__name__}: {e}"
                try:
                    MONITOR.buying_power = fetch_buying_power(key_id, secret_key)
                except Exception:  # noqa: BLE001 — plan tab just shows no number
                    pass
            if time.time() - act_refreshed > 600:  # closed-market P/L + fills
                act_refreshed = time.time()
                act_quick = time.time()  # the full sweep covers the quick check too
                try:
                    MONITOR.activity_pnl, MONITOR.trades = fetch_activity_pnl(key_id, secret_key)
                    MONITOR.note_fills_alert()
                except Exception:  # noqa: BLE001 — closed rows just go stale
                    pass
            elif time.time() - act_quick > 60:  # cheap 1-page fills check
                act_quick = time.time()
                try:
                    MONITOR.merge_fills(fetch_recent_fills(key_id, secret_key))
                    MONITOR.note_fills_alert()
                except Exception:  # noqa: BLE001 — the 10-min sweep still covers it
                    pass
        except Exception as e:  # noqa: BLE001 — shown on the dashboard, loop survives
            MONITOR.error = f"{type(e).__name__}: {e}"
            err_streak += 1
            if time.time() - last_ok > 600 and time.time() - err_notified > 3600:
                notify("Live monitor failing", MONITOR.error, "high")
                err_notified = time.time()
        for title, msg, prio in MONITOR.drain_alerts():
            notify(title, msg, prio)
        # Back off while failing — retrying a rate limiter every poll keeps
        # the block alive. 30s -> 1m -> 2m ... capped at 10 minutes.
        wait = POLL_SECONDS if not err_streak else min(POLL_SECONDS * 2 ** err_streak, 600)
        POLL_KICK.wait(wait)  # a reprice wakes the loop immediately
        POLL_KICK.clear()


def main() -> None:
    global KEY_ID, SECRET_KEY
    key_id = os.environ.get("POLYMARKET_KEY_ID", "").strip()
    secret_key = os.environ.get("POLYMARKET_SECRET_KEY", "").strip()
    if not key_id or not secret_key:
        print("Set POLYMARKET_KEY_ID and POLYMARKET_SECRET_KEY", file=sys.stderr)
        sys.exit(1)
    KEY_ID, SECRET_KEY = key_id, secret_key
    # A reboot must not burst hundreds of book fetches at the rate limiter —
    # let the 15-per-poll rotation fill the cache instead (full in ~10 min).
    tr.BOOK_COLD_FETCH_ALL = False
    threading.Thread(target=poll_loop, args=(key_id, secret_key), daemon=True).start()
    threading.Thread(target=ws_stream_loop, args=(key_id, secret_key), daemon=True).start()
    threading.Thread(target=hf_sampler_loop, daemon=True).start()
    threading.Thread(target=tracker_loop, daemon=True).start()
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"live monitor on :{PORT}, polling every {POLL_SECONDS}s")
    server.serve_forever()


if __name__ == "__main__":
    main()
