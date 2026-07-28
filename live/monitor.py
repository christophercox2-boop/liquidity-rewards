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
import datetime as dt
import gzip
import json
import os
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


def tracker_day_integral(day_et: str) -> tuple[float, dict[str, float]] | None:
    """Rebuild 'earned so far today' from the hourly tracker's estimate
    snapshots (data/estimates.csv on main) — piecewise-constant integration
    from midnight ET to now. Independent of this process, so it survives any
    monitor outage or state loss."""
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
        if r.status_code != 200:
            return None
        import csv as _csv
        import io as _io
        runs: dict[str, dict[str, float]] = {}  # utc run ts -> market -> est $/day
        for row in _csv.DictReader(_io.StringIO(r.text)):
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
        now = dt.datetime.now(dt.timezone.utc)

        def _utc(ts: str) -> dt.datetime:
            return dt.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)

        total, per_market = 0.0, {}
        for i, ts in enumerate(times):
            start = midnight.astimezone(dt.timezone.utc) if i == 0 else _utc(ts)
            end = _utc(times[i + 1]) if i + 1 < len(times) else now
            frac = max((end - start).total_seconds(), 0.0) / 86400.0
            for m, est in runs[ts].items():
                total += est * frac
                per_market[m] = per_market.get(m, 0.0) + est * frac
        return round(total, 2), {m: round(v, 4) for m, v in per_market.items()}
    except Exception:  # noqa: BLE001
        return None


def load_winners() -> tuple[list[dict], float]:
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
            return [], 0.0
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
        return winners, round(sum(tot.values()), 2)
    except Exception:  # noqa: BLE001
        return [], 0.0


WINNERS: list[dict] = []


class Monitor:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.state: dict = {"day": None, "earned": 0.0, "per_market": {}, "history": [],
                            "saved_at": 0.0, "rate": 0.0, "market_rates": {}, "ts": None}
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
                qty = f"{t['filled']:g}" if t.get("filled") else "?"
                if t.get("qty") and t.get("filled") and t["qty"] > t["filled"]:
                    qty += f" of {t['qty']:g}"
                px = f" @ {t['price_cents']:g}¢" if t.get("price_cents") is not None else ""
                lines.append(f"{t.get('side') or ''} {qty}{px} — {t.get('market', '')}")
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
            # …then roll the day over at midnight ET.
            old_day_earned = None
            if self.state["day"] != day:
                if self.state["day"]:
                    old_day_earned = round(self.state["earned"], 2)
                    self.state["history"] = (self.state["history"] + [
                        {"day": self.state["day"], "earned": old_day_earned}
                    ])[-30:]
                self.state.update({"day": day, "earned": 0.0, "per_market": {},
                                   "earned_series": [], "rate_series": []})
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
            # Cumulative earned-today curve for the overall graph.
            es = self.state.setdefault("earned_series", [])
            if es and es[-1][0] == minute:
                es[-1][1] = round(self.state["earned"], 4)
            else:
                es.append([minute, round(self.state["earned"], 4)])
            del es[:-1500]
            # Overall earning-rate curve ($/day) — what the big graph plots.
            rs = self.state.setdefault("rate_series", [])
            if rs and rs[-1][0] == minute:
                rs[-1][1] = round(self.rate, 4)
            else:
                rs.append([minute, round(self.rate, 4)])
            del rs[:-1500]
            self.last_ts = now_utc
            self.orders = orders
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
                "earned_today": round(self.state["earned"], 4),
                "rate_per_day": round(self.rate, 2),
                "per_market_today": {m: round(v, 4) for m, v in sorted(
                    self.state["per_market"].items(), key=lambda kv: -kv[1])},
                "orders": [
                    {**{k: o.get(k) for k in ("id", "market", "side", "price", "size", "ticks", "share",
                                              "est_day", "verdict", "window", "window_more",
                                              "window_more_score", "denom", "df", "calc",
                                              "event_n", "siblings")},
                     "batch": o.get("id") in batch_ids}
                    for o in self.orders
                ],
                "history": self.state["history"][-7:][::-1],
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
                "actions": ACTIONS[-10:][::-1],
                "trades": self.trades[:60],
                "drops": self._drops(),
                "winners": self._missed_winners(),
                "new_mkts": (self.state.get("new_mkts") or [])[::-1],
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


def _verify_resting(market: str, side: str, price_value: str) -> tuple[bool, str]:
    """After a modify, confirm an order is actually resting at the new price."""
    try:
        time.sleep(1.0)  # give the exchange a beat to settle the replace
        path = "/v1/orders/open"
        r = requests.request(
            "GET", tr.TRADE_API + path,
            headers=tr.auth_headers(KEY_ID, SECRET_KEY, "GET", path), timeout=20,
        )
        if r.status_code >= 400:
            return False, f"verify fetch HTTP {r.status_code}"
        want = float(price_value)
        for o in r.json().get("orders") or []:
            slug = o.get("marketSlug") or (o.get("marketMetadata") or {}).get("slug") or ""
            oside = "BUY" if str(o.get("side", "")).upper().endswith("BUY") else "SELL"
            if slug == market and oside == side and abs(tr._num(o.get("price")) - want) < 0.0005:
                return True, f"verified resting at {want * 100:g}¢ (id {o.get('id')})"
        return False, "NO order found at the new price — it may have been cancelled; check the app"
    except Exception as e:  # noqa: BLE001
        return False, f"verify failed: {type(e).__name__}: {e}"[:150]


PLAN_CACHE: dict = {"politics": {"ts": 0.0, "data": None}, "golf": {"ts": 0.0, "data": None},
                    "tt": {"ts": 0.0, "data": None}}
PLAN_FILES = {"politics": "data/scan.json", "golf": "data/scan_golf.json",
              "tt": "data/scan_tt.json"}


def fetch_plan(which: str = "politics") -> dict:
    """A scan plan file from the repo's main branch (via GITHUB_TOKEN)."""
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
                or bool(plan_row.get("join_ok")))  # 1-share touch plans join by design
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
            thr = min(0.08, max(0.01, 0.5 * planned)) if planned else 0.08
            if est < thr:
                res.update(status="skipped",
                           note=f"drifted — est now ${est:.2f}/day (planned ${planned or 0:.2f})")
                return res
            res["est_day"] = round(est, 2)
        intent = "ORDER_INTENT_BUY_LONG"
        if side == "SELL":  # sell inventory if we hold enough, else open a short
            net = tr._num((MONITOR.positions.get(slug) or {}).get("netPosition"))
            intent = "ORDER_INTENT_SELL_LONG" if net >= size else "ORDER_INTENT_SELL_SHORT"
            res["intent"] = intent
        path = "/v1/orders"
        value = f"{price:.3f}".rstrip("0").rstrip(".")
        r = requests.request(
            "POST", tr.TRADE_API + path,
            headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", path),
                     "Content-Type": "application/json"},
            json={"marketSlug": slug, "intent": intent,
                  "type": "ORDER_TYPE_LIMIT",
                  "price": {"value": value, "currency": "USD"},
                  "quantity": size, "tif": "TIME_IN_FORCE_DAY",
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


def _collect_fills(t: dict, fills_by_order: dict[str, dict]) -> None:
    """One trade activity = one (often 1-share) execution. Keep only real
    executions — shares actually traded, never mere order placements — and
    collapse them to one row per ORDER. Activities arrive newest first, so
    the first sighting of an order carries its latest cumulative fill,
    average price and state."""
    rows_this = []
    for ex in (t.get("aggressorExecution") or {}, t.get("passiveExecution") or {}):
        o = ex.get("order") or {}
        oid = o.get("id")
        if not oid or tr._num(ex.get("lastShares")) <= 0:
            continue  # not an accepted execution of one of our orders
        row = fills_by_order.get(oid)
        if row is None:
            if len(fills_by_order) >= 80:
                continue
            ts_s, when = _fill_ts(str(ex.get("transactTime") or ""))
            state = str(o.get("state") or "")
            fills_by_order[oid] = row = {
                "oid": oid,
                "market": o.get("marketSlug") or t.get("marketSlug") or "",
                "side": "SELL" if "SELL" in str(o.get("side") or "") else "BUY",
                "qty": tr._num(o.get("quantity")) or None,
                "filled": tr._num(o.get("cumQuantity")) or None,
                "price_cents": round(tr._num(o.get("avgPx") or o.get("price")) * 100, 2),
                "done": state == "ORDER_STATE_FILLED",
                "ts_s": ts_s, "when": when, "pnl": 0.0}
        rows_this.append(row)
    if not rows_this and t.get("marketSlug"):  # older flat shape (qty/price)
        qty = tr._num(t.get("qty"))
        if qty > 0:
            key = str(t.get("id") or len(fills_by_order))
            ts_s, when = _fill_ts(str(t.get("updateTime") or t.get("createTime") or ""))
            fills_by_order[key] = row = {
                "oid": key,
                "market": t["marketSlug"], "side": None, "qty": qty, "filled": qty,
                "price_cents": (round(tr._num(t.get("price")) * 100, 2)
                                if t.get("price") is not None else None),
                "done": True, "ts_s": ts_s, "when": when, "pnl": 0.0}
            rows_this.append(row)
    pnl = tr._num(t.get("realizedPnl"))
    if rows_this and pnl:
        rows_this[0]["pnl"] += pnl


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
                                   {"realized": 0.0, "ts": "", "resolved": False, "final": None})
                e["realized"] += tr._num(t.get("realizedPnl"))
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
        trades.append(row)
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
    """Modify one of OUR resting orders to a new price. The order must be in
    the latest snapshot (can't touch anything else) and the price sane.
    Modify is cancel-and-replace on the exchange, so the request carries the
    FULL replacement (price and remaining quantity) and the result is
    verified against the open-orders list before reporting success."""
    known = {o.get("id"): o for o in MONITOR.orders if o.get("id")}
    o = known.get(order_id)
    if o is None:
        return 400, {"ok": False, "error": "unknown order id — wait for the next refresh"}
    if not (0.1 <= price_cents <= 99.9):
        return 400, {"ok": False, "error": "price out of range (0.1–99.9¢)"}
    qty = int(quantity) if quantity else int(round(o["size"]))
    if not (1 <= qty <= 20000):
        return 400, {"ok": False, "error": "size out of range (1–20,000)"}
    path = f"/v1/order/{order_id}/modify"
    value = f"{price_cents / 100:.3f}".rstrip("0").rstrip(".")
    record = {"ts": dt.datetime.now(ET).strftime("%Y-%m-%d %I:%M:%S %p ET"),
              "market": o["market"], "side": o["side"],
              "from": round(o["price"] * 100, 1), "to": price_cents,
              "size": (qty if qty == int(round(o["size"]))
                       else f"{int(round(o['size']))}→{qty}")}
    try:
        r = requests.request(
            "POST", tr.TRADE_API + path,
            headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", path),
                     "Content-Type": "application/json"},
            json={"marketSlug": o["market"],
                  "price": {"value": value, "currency": "USD"},
                  "quantity": qty},
            timeout=20,
        )
        record["status"] = r.status_code
        record["response"] = " ".join(r.text.split())[:300]
        ok = r.status_code < 300
        if verify:  # batches verify once at the end instead — one orders fetch, not N
            verified, note = _verify_resting(o["market"], o["side"], value) if ok else (False, "")
            if ok and not verified:
                notify("Reprice NOT verified", f"{o['market']} → {price_cents}¢: {note}", "high")
        else:
            verified, note = ok, ""
        record["verified"] = verified
        record["note"] = note
        POLL_KICK.set()
        payload = {"ok": ok and verified, "status": r.status_code,
                   "detail": (note or record["response"])[:250]}
        return (200 if ok else 502), payload
    except Exception as e:  # noqa: BLE001
        record["status"] = "error"
        record["response"] = f"{type(e).__name__}: {e}"[:300]
        record["verified"] = False
        return 502, {"ok": False, "error": record["response"][:200]}
    finally:
        ACTIONS.append(record)
        del ACTIONS[:-20]

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
    mine = [{k: o.get(k) for k in ("id", "side", "price", "size", "est_day", "verdict")}
            for o in MONITOR.orders if o.get("market") == slug]
    net = tr._num((MONITOR.positions.get(slug) or {}).get("netPosition"))
    return 200, {"market": slug, "tick": book.get("tick") or 0.01,
                 "bids": [[p, q] for p, q in (book.get("bids") or [])[:6]],
                 "asks": [[p, q] for p, q in (book.get("asks") or [])[:6]],
                 "orders": mine, "net": net, "buying_power": MONITOR.buying_power}


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


def manual_place(slug: str, side: str, price_cents: float, size: int) -> tuple[int, dict]:
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
        intent = "ORDER_INTENT_SELL_LONG" if net >= size else "ORDER_INTENT_SELL_SHORT"
    path = "/v1/orders"
    value = f"{price_cents / 100:.3f}".rstrip("0").rstrip(".")
    try:
        r = requests.request(
            "POST", tr.TRADE_API + path,
            headers={**tr.auth_headers(KEY_ID, SECRET_KEY, "POST", path),
                     "Content-Type": "application/json"},
            json={"marketSlug": slug, "intent": intent, "type": "ORDER_TYPE_LIMIT",
                  "price": {"value": value, "currency": "USD"},
                  "quantity": size, "tif": "TIME_IN_FORCE_DAY",
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
                                float(body["price_cents"]), int(body["size"]))
        except (KeyError, TypeError, ValueError):
            return 400, {"ok": False, "error": "bad request"}
    return 400, {"ok": False, "error": "op must be place, modify or cancel"}


DASH_HTML = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Liquidity rewards — live</title>
<style>
 body{font-family:-apple-system,system-ui,sans-serif;margin:0;padding:16px;background:#0d1117;color:#e6edf3}
 .big{font-size:56px;font-weight:700;margin:8px 0}
 .sub{color:#8b949e;font-size:14px}
 .err{background:#3d1418;color:#ffa198;padding:8px 12px;border-radius:8px;margin:10px 0;display:none}
 table{width:100%;border-collapse:collapse;margin-top:14px;font-size:13px}
 td,th{padding:6px 4px;text-align:left;border-bottom:1px solid #21262d}
 td.r,th.r{text-align:right}
 .mkt{color:#8b949e;font-size:11px;word-break:break-all}
 h3{margin:18px 0 4px;font-size:15px}
 .bk{width:auto;min-width:60%;margin:6px 0;font-family:ui-monospace,monospace;font-size:12px}
 .bk td{padding:2px 10px 2px 0;border-bottom:none;color:#8b949e}
 .bk tr.me td{color:#58a6ff;font-weight:600}
 .calc{font-family:ui-monospace,monospace;font-size:12px;color:#e6edf3;margin:2px 0}
 .ord{margin:8px 0 14px}
 .oh{font-size:12px;color:#e6edf3;margin-bottom:2px}
 .rp{margin:6px 0}
 .rp input{width:70px;background:#0d1117;color:#e6edf3;border:1px solid #30363d;border-radius:6px;padding:5px;font-size:14px}
 .rp button{background:#238636;color:#fff;border:none;border-radius:6px;padding:6px 12px;font-size:13px;margin-left:6px}
 .rp button.alt{background:#21262d;color:#8b949e}
 .tab{background:#21262d;color:#8b949e;border:none;border-radius:8px;padding:8px 16px;font-size:14px}
 .tab.on{background:#238636;color:#fff}
 .pos{color:#3fb950}
 .neg{color:#f85149}
 .bdg{background:#1f3a5f;color:#79b8ff;border-radius:5px;padding:1px 6px;font-size:10px;vertical-align:middle}
</style></head><body>
<div style="display:flex;gap:8px;margin-bottom:12px">
 <button class="tab on" id="tabH" onclick="showTab('H')">Home</button>
 <button class="tab" id="tabR" onclick="showTab('R')">Markets</button>
 <button class="tab" id="tabP" onclick="showTab('P')">P/L</button>
 <button class="tab" id="tabL" onclick="showTab('L')">Plan</button>
</div>
<div id="viewH">
<div class="sub">Earned today (ET) — live estimate</div>
<div class="big" id="earned">…</div>
<div class="sub" id="rate"></div>
<div class="sub" id="updated"></div>
<div class="err" id="err"></div>
<div id="ovg" style="margin:10px 0"></div>
<h3>Since you last checked <button class="tab" style="font-size:11px;padding:4px 10px" onclick="clearTxns()">Clear</button></h3>
<table id="txns"></table>
<h3>Biggest drops <span class="sub">(vs their peak over the last ~8h)</span></h3>
<table id="drops"></table>
<h3>Earners you're not in <span class="sub">(paid you before · no order resting now)</span></h3>
<table id="winners"></table>
<h3>New markets <span class="sub">(golf shown per tournament)</span></h3>
<table id="newm"></table>
<div class="mkt" style="margin-top:8px">Tap any market to place, modify or cancel an order there.</div>
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
<h3>By market <span class="sub">(sorted by current rate · tap a row for the math)</span></h3><table id="markets"></table>
<h3>Previous days</h3><table id="history"></table>
<div id="acts"></div>
</div>
<div id="viewP" style="display:none">
<div class="sub">Profit / loss on filled orders</div>
<div class="big" id="pnlTotal">…</div>
<div class="sub" id="pnlSub"></div>
<table id="pnl"></table>
<div class="mkt" id="pnlNote" style="margin-top:10px">Sorted by most recent trade. Value =
what the open position is worth at current prices. Unreal. = value − what it cost.
Real. = P/L the exchange has already booked (closed trades and resolved markets).
Refreshes every 2 min.</div>
</div>
<div id="viewL" style="display:none">
<div class="sub">Passive placement plan <span id="planGen"></span></div>
<div style="margin:8px 0">
 <label class="sub"><input type="radio" name="pwhich" value="politics" checked onchange="switchPlan()"> Politics</label>
 <label class="sub"><input type="radio" name="pwhich" value="golf" onchange="switchPlan()"> Golf (cheap YES)</label>
 <label class="sub"><input type="radio" name="pwhich" value="tt" onchange="switchPlan()"> Table tennis (1@touch)</label></div>
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
<div style="margin-top:26px;border-top:1px solid #30363d;padding-top:12px">
 <button class="tab" style="background:#8b1a1a;color:#fff" onclick="cancelAll()">⚠ Cancel ALL open orders</button>
</div>
</div>
<div id="sheet" style="display:none;position:fixed;inset:0;background:rgba(1,4,9,.88);overflow:auto;z-index:10" onclick="closeSheet()">
 <div id="sheetIn" style="max-width:560px;margin:24px auto;background:#161b22;border:1px solid #30363d;border-radius:12px;padding:16px" onclick="event.stopPropagation()"></div>
</div>
<script>
let OPEN = {}, GOPEN = {}, SERIES = null, RATES = {};
let SEEN = JSON.parse(localStorage.getItem('seenRates') || '{}');
function showTab(t){
  ['H','R','P','L'].forEach(k => {
    document.getElementById('view'+k).style.display = k===t ? '' : 'none';
    document.getElementById('tab'+k).className = 'tab' + (k===t ? ' on' : '');
  });
  if(t==='L') loadPlan();
}
let PLAN = null, PSEL = {}, BP = null, OLOCK = {};
function pwhich(){ const el = document.querySelector('input[name="pwhich"]:checked'); return el ? el.value : 'politics'; }
function switchPlan(){ PLAN = null; PSEL = {};
  document.getElementById('golfCapRow').style.display = pwhich() === 'golf' ? '' : 'none';
  document.getElementById('polCapRow').style.display = pwhich() === 'politics' ? '' : 'none';
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
    const d = await (await fetch('plan.json?which=' + pwhich())).json();
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
      if(pwhich() === 'tt') return true;  // 1-share touch orders: sliders don't apply
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
  const tt = pwhich() === 'tt';
  const capC = tt ? 99.9 : +document.getElementById('capSlider').value;
  const sMin = tt ? 0.1 : +document.getElementById('sellSlider').value;
  const sel = planRows().filter(r => PSEL[pkey(r)]);
  if(!sel.length){ alert('Nothing selected'); return; }
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
    if(!d.ok){ alert('Failed: ' + (d.error || '')); return; }
    if(d.precheck_skipped && d.precheck_skipped.length)
      alert(d.precheck_skipped.length + ' order(s) skipped by the sliders:\\n' +
            d.precheck_skipped.slice(0,5).join('\\n'));
    pollPlace();
  }catch(e){ alert('Failed: ' + e); }
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
  if(!sel.length){ alert('Nothing selected'); return; }
  const gain = sel.reduce((s,r)=>s+(r.est_after-r.est_now),0);
  if(!confirm('Reprice ' + sel.length + ' orders to their optimal prices?\\nEstimated gain ~$' +
              gain.toFixed(2) + '/day. Each move is checked against the live book first.')) return;
  try{
    const r = await fetch('reprice_batch', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify({orders: sel.map(r => ({id: r.id, to_cents: r.to_cents, to_size: r.to_size}))})});
    const d = await r.json();
    if(!d.ok){ alert('Failed: ' + (d.error || '')); return; }
    RPLAN = null; document.getElementById('rpl').innerHTML = '';
    pollReprice();
  }catch(e){ alert('Failed: ' + e); }
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
  if(!sel.length){ alert('Nothing selected'); return; }
  const freed = sel.reduce((s,r)=>s+r.locked,0);
  if(!confirm('Cancel ' + sel.length + ' resting orders earning ~$0/day?\\nFrees ~$' +
              freed.toFixed(0) + ' of locked collateral. Positions are untouched — this only ' +
              'removes unfilled orders.')) return;
  try{
    const r = await fetch('cancel_batch', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify({orders: sel.map(r => ({id: r.id}))})});
    const d = await r.json();
    if(!d.ok){ alert('Failed: ' + (d.error || '')); return; }
    DPLAN = null; document.getElementById('rpl').innerHTML = '';
    pollCancelDead();
  }catch(e){ alert('Failed: ' + e); }
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
    alert(d.ok ? 'All orders cancelled' : 'Failed: ' + (d.error || ('HTTP ' + r.status)));
  }catch(e){ alert('Failed: ' + e); }
  setTimeout(refresh, 1500);
}
function usd(v){ return (v<0?'-$':'$') + Math.abs(v||0).toFixed(2); }
function cls(v){ return v>0.004 ? 'pos' : (v<-0.004 ? 'neg' : ''); }
function renderPnl(pn){
  const t = (pn && pn.totals) || {};
  const big = document.getElementById('pnlTotal');
  big.textContent = usd(t.total); big.className = 'big ' + cls(t.total);
  document.getElementById('pnlSub').textContent =
    usd(t.realized) + ' realized · ' + usd(t.unrealized) + ' unrealized · positions worth ' + usd(t.cash) +
    (pn && pn.updated ? ' · as of ' + pn.updated : '') + (pn && pn.error ? ' · ' + pn.error : '');
  document.getElementById('pnl').innerHTML =
    '<tr><th>Market</th><th class="r">Pos</th><th class="r">Avg</th><th class="r">Value</th>'+
    '<th class="r">Real.</th><th class="r">Unreal.</th><th class="r">P/L</th></tr>' +
    ((pn && pn.rows) || []).map(r =>
      '<tr><td class="mkt">' + esc(r.market) +
      (r.expired ? ' <span class="sub">(resolved)</span>' : (r.closed ? ' <span class="sub">(closed)</span>' : '')) +
      (r.traded ? '<div class="sub" style="font-size:10px">traded ' + esc(r.traded) + '</div>' : '') + '</td>' +
      '<td class="r">' + (r.net||0).toLocaleString() + '</td>' +
      '<td class="r">' + (r.avg_cents==null ? '—' : r.avg_cents.toFixed(1) + '¢') + '</td>' +
      '<td class="r">' + usd(r.cash) + '</td>' +
      '<td class="r ' + cls(r.realized) + '">' + usd(r.realized) + '</td>' +
      '<td class="r ' + cls(r.unrealized) + '">' + usd(r.unrealized) + '</td>' +
      '<td class="r ' + cls(r.total) + '"><b>' + usd(r.total) + '</b></td></tr>').join('');
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
  return '<svg width="'+w+'" height="'+h+'" style="background:#010409;border-radius:8px;max-width:100%">'+
    '<path d="'+dpath+'" fill="none" stroke="#58a6ff" stroke-width="2"/></svg>'+
    '<div class="mkt">$/day over last '+hrs+'h · min $'+r0.toFixed(2)+' · max $'+r1.toFixed(2)+
    ' · now $'+rs[rs.length-1].toFixed(2)+'</div>';
}
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
  return '<svg viewBox="0 0 '+w+' '+h+'" style="width:100%;background:#010409;border-radius:8px">'+
    '<path d="'+trend+'" fill="none" stroke="#3fb950" stroke-width="1.5" stroke-dasharray="5,4"/>'+
    '<path d="'+curve+'" fill="none" stroke="#58a6ff" stroke-width="2.5"/></svg>'+
    '<div class="mkt">rate, last '+hrs+'h: now <b style="color:#58a6ff">$'+now.toFixed(2)+'/day</b>'+
    ' · avg $'+avg.toFixed(2)+'/day · range $'+ymin.toFixed(2)+'–$'+ymax.toFixed(2)+'</div>';
}
function tint(m, cur){
  const seen = SEEN[m];
  if(seen === undefined) return '';
  const delta = cur - seen;
  if(Math.abs(delta) < Math.max(0.5, 0.25*Math.max(seen, 0.01))) return '';
  return delta < 0 ? 'background:#3d1418' : 'background:#12341c';
}
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;'); }
async function reprice(id, label){
  const inp = document.getElementById('p'+id);
  const cents = parseFloat(inp.value);
  if(!(cents >= 0.1 && cents <= 99.9)){ alert('Price out of range (0.1–99.9¢)'); return; }
  if(!confirm('Reprice ' + label + ' to ' + cents + '¢?')) return;
  try{
    const r = await fetch('reprice', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify({order_id:id, price_cents:cents})});
    const d = await r.json().catch(()=>({ok:false,error:'HTTP '+r.status}));
    alert(d.ok ? 'Repriced ✓' : 'Failed: ' + (d.detail || d.error || ('HTTP '+r.status)));
  }catch(e){ alert('Failed: '+e); }
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
function mrow(m, mid, right){
  return '<tr onclick="openMkt(\\''+esc(m)+'\\')"><td class="mkt">'+esc(m)+'</td>'+
         (mid||'')+'<td class="r" style="white-space:nowrap">'+right+'</td></tr>';
}
function renderHome(d){
  LASTD = d;
  const seen = txnSeen();
  const tx = (d.trades || []).filter(t => t.ts_s > seen);
  document.getElementById('txns').innerHTML = tx.length ? tx.slice(0, 25).map(t => {
      const f = t.filled != null ? (+t.filled).toLocaleString() : '';
      const part = (t.qty != null && t.filled != null && t.qty > t.filled)
        ? ' of ' + (+t.qty).toLocaleString() : '';
      return mrow(t.market,
        '<td class="r" style="white-space:nowrap">'+
        (t.side ? '<span'+(t.side === 'SELL' ? ' style="color:#f0883e"' : '')+'>'+t.side+'</span> ' : '')+
        f + part +
        (t.price_cents != null ? ' @ ' + (+t.price_cents).toFixed(2) + '¢' : '')+
        (t.pnl ? '<br><span class="'+(t.pnl > 0 ? 'pos' : 'neg')+'">'+(t.pnl > 0 ? '+' : '')+
                 t.pnl.toFixed(2)+'</span>' : '')+'</td>',
        '<span class="sub" style="font-size:11px">'+esc(t.when || '')+'</span>');
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
      '<tr><td class="mkt" onclick="openMkt(\\''+esc(w.market)+'\\')">'+esc(w.market)+'</td>'+
      '<td class="r" style="white-space:nowrap" onclick="openMkt(\\''+esc(w.market)+'\\')">'+
      '<b class="pos">$'+w.total.toFixed(2)+'</b><br><span class="sub" style="font-size:11px">last paid '+esc(w.last)+'</span></td>'+
      '<td class="r" style="width:30px"><button class="alt" style="border:none;border-radius:6px;padding:4px 8px;background:#21262d;color:#8b949e" '+
      'onclick="hideWinner(\\''+esc(w.market)+'\\')">✕</button></td></tr>').join('')
    : '<tr><td class="sub">you have orders everywhere you have earned lately</td></tr>') +
    (nHid ? '<tr><td colspan="3" class="sub" style="font-size:11px">'+nHid+
            ' dismissed · <a href="#" style="color:#58a6ff" onclick="unhideWinners();return false">unhide all</a></td></tr>' : '');
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
  if(!lv.length){ alert('That side of the book is empty — no best price to match.'); return; }
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
  const ords = (d.orders || []).map(o =>
    '<div class="rp" style="margin:10px 0">'+o.side+' '+o.size.toLocaleString()+' @ '+
    (+(o.price*100).toFixed(2))+'¢'+(o.est_day ? ' · $'+o.est_day.toFixed(2)+'/day' : ' · $0/day')+
    '<br><input id="mp'+o.id+'" type="number" step="0.1" min="0.1" max="99.9" value="'+(o.price*100).toFixed(1)+'">¢ '+
    '<button class="alt" onclick="qBump(\\'mq'+o.id+'\\',-1)">−</button>'+
    '<input id="mq'+o.id+'" type="number" step="1" min="1" max="20000" value="'+Math.round(o.size)+'">'+
    '<button class="alt" onclick="qBump(\\'mq'+o.id+'\\',1)">+</button>'+
    '<button onclick="mModify(\\''+o.id+'\\',\\''+esc(m)+'\\')">Modify</button>'+
    '<button class="alt" style="background:#8b1a1a;color:#fff" onclick="mCancel(\\''+o.id+'\\',\\''+esc(m)+'\\')">Cancel</button>'+
    '</div>').join('') || '<div class="sub">no resting orders here</div>';
  document.getElementById('sheetIn').innerHTML =
    '<div class="mkt" style="font-size:13px">'+esc(m)+'</div>'+
    (d.net ? '<div class="sub">position: '+d.net.toLocaleString()+' contracts</div>' : '')+
    '<div style="display:flex;gap:18px;margin-top:8px">'+
    '<div style="flex:1"><div class="sub">Bids</div><table class="bk">'+lv(d.bids)+'</table></div>'+
    '<div style="flex:1"><div class="sub">Asks</div><table class="bk">'+lv(d.asks)+'</table></div></div>'+
    '<h3>Your orders</h3>'+ords+
    '<h3>Place new</h3><div class="rp">'+
    '<select id="mSide" style="background:#0d1117;color:#e6edf3;border:1px solid #30363d;border-radius:6px;padding:5px">'+
    '<option>BUY</option><option>SELL</option></select> '+
    '<input id="mPrice" type="number" step="0.1" min="0.1" max="99.9" placeholder="price ¢"> '+
    '<button class="alt" onclick="qBump(\\'mSize\\',-1)">−</button>'+
    '<input id="mSize" type="number" step="1" min="1" max="20000" placeholder="qty">'+
    '<button class="alt" onclick="qBump(\\'mSize\\',1)">+</button> '+
    '<button class="alt" onclick="mBest()">match best</button> '+
    '<button onclick="mPlace(\\''+esc(m)+'\\')">Place</button></div>'+
    '<div class="rp" style="margin-top:4px"><span class="sub">± step:</span> '+
    '<input id="qStepIn" type="number" step="1" min="1" max="20000" value="'+qStep()+'" '+
    'style="width:60px" oninput="qStepSet(this.value)"></div>'+
    '<div class="mkt">post-only — the order rests or is rejected; it can never cross the spread and fill on arrival</div>'+
    '<div class="rp" style="margin-top:12px"><button class="alt" onclick="closeSheet()">Close</button></div>';
}
async function mact(body, m){
  try{
    const r = await fetch('maction', {method:'POST',
      headers:{'Content-Type':'application/json','X-Reprice':'1'},
      body: JSON.stringify(body)});
    const d = await r.json().catch(() => ({ok:false, error:'HTTP '+r.status}));
    alert(d.ok ? 'Done ✓' : 'Failed: ' + (d.detail || d.error || ('HTTP '+r.status)));
  }catch(e){ alert('Failed: '+e); }
  setTimeout(function(){ openMkt(m); refresh(); }, 1200);
}
function mModify(id, m){
  const c = parseFloat(document.getElementById('mp'+id).value);
  const q = parseInt(document.getElementById('mq'+id).value, 10);
  if(!(c >= 0.1 && c <= 99.9)){ alert('Price out of range (0.1–99.9¢)'); return; }
  if(!(q >= 1 && q <= 20000)){ alert('Size out of range (1–20,000)'); return; }
  if(!confirm('Modify this order to '+q.toLocaleString()+' @ '+c+'¢?')) return;
  mact({op:'modify', order_id:id, price_cents:c, size:q}, m);
}
function mCancel(id, m){
  if(!confirm('Cancel this order?')) return;
  mact({op:'cancel', order_id:id}, m);
}
function mPlace(m){
  const side = document.getElementById('mSide').value;
  const c = parseFloat(document.getElementById('mPrice').value);
  const q = parseInt(document.getElementById('mSize').value, 10);
  if(!(c >= 0.1 && c <= 99.9)){ alert('Price out of range (0.1–99.9¢)'); return; }
  if(!(q >= 1 && q <= 20000)){ alert('Size out of range (1–20,000)'); return; }
  const cap = side === 'BUY' ? c/100*q : (1 - c/100)*q;
  if(!confirm('Place post-only '+side+' '+q.toLocaleString()+' @ '+c+'¢? Locks ~$'+cap.toFixed(2)+'.')) return;
  mact({op:'place', market:m, side:side, price_cents:c, size:q}, m);
}
async function refresh(){
  try{
    const r = await fetch('data.json'); const d = await r.json();
    document.getElementById('earned').textContent = '$' + d.earned_today.toFixed(2);
    const nMkts = new Set(d.orders.map(o => o.market).filter(Boolean)).size;
    document.getElementById('rate').textContent =
      'current rate ~$' + d.rate_per_day.toFixed(2) + '/day across ' + nMkts +
      ' markets (' + d.orders.length + ' orders)';
    document.getElementById('updated').textContent = 'updated ' + d.updated + ' · day resets midnight ET · saves: ' + d.persistence + ' · alerts: ' + d.alerts +
      (d.warming ? ' · ⏳ warming up: ' + d.warming + ' markets on saved rates' : '') +
      (d.backfilled ? ' · ♻️ counter rebuilt from tracker data ($' + d.backfilled.toFixed(2) + ' at boot)' : '');
    const err = document.getElementById('err');
    const diag = Object.entries(d.diag || {}).map(([k,v]) => k.replace(/^_/,'') + ': ' + v).join(' · ');
    const msg = [d.error, diag].filter(Boolean).join(' · ');
    err.style.display = msg ? 'block' : 'none'; err.textContent = msg;
    document.getElementById('ovg').innerHTML = bigSpark(d.rate_series);
    renderHome(d);
    renderPnl(d.pnl);
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
    document.getElementById('markets').innerHTML =
      Object.entries(allMarkets)
        .sort((a,b) => (RATES[b[0]]||0) - (RATES[a[0]]||0) || b[1] - a[1])
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
        const rateTxt = dead ? '<b style="color:#d29922">⚠️ $0.00/day</b>'
                             : '<b>$'+rate.toFixed(2)+'/day</b>';
        const hasBatch = d.orders.some(o => o.market === m && o.batch);
        return '<tr id="r'+i+'" onclick="tgl('+i+',\\''+esc(m)+'\\')" style="'+tint(m, rate)+'">'+
          '<td class="mkt">'+m+(hasBatch?' <span class="bdg">batch</span>':'')+
          '</td><td class="r" style="white-space:nowrap">'+rateTxt+
          '<br><span class="sub" style="font-size:11px">$'+v.toFixed(2)+' today</span>'+
          ' <button class="alt" style="border:none;border-radius:6px;padding:4px 8px;background:#21262d;color:#8b949e" '+
          'onclick="event.stopPropagation();tglGraph('+i+',\\''+esc(m)+'\\')">📈</button>'+
          ' <button class="alt" style="border:none;border-radius:6px;padding:4px 8px;background:#21262d;color:#8b949e" '+
          'onclick="event.stopPropagation();openMkt(\\''+esc(m)+'\\')">⚙</button></td></tr>' +
          '<tr id="g'+i+'" style="display:'+(GOPEN[m]?'':'none')+'"><td colspan="2" style="background:#161b22">'+gcell+'</td></tr>' +
          '<tr id="d'+i+'" style="display:'+(OPEN[m]?'':'none')+'"><td colspan="2" ' +
          'style="background:#161b22">'+detail+'</td></tr>';
      }).join('') || '<tr><td>nothing yet today</td></tr>';
    document.getElementById('history').innerHTML =
      d.history.map(h => '<tr><td>'+h.day+'</td><td class="r">$'+h.earned.toFixed(2)+'</td></tr>').join('')
      || '<tr><td>collecting…</td></tr>';
    document.getElementById('acts').innerHTML = (d.actions && d.actions.length) ?
      '<h3>Recent actions</h3>' + d.actions.map(a =>
        '<div class="mkt" style="margin:4px 0">'+(a.verified?'✅':'⚠️')+' '+a.ts+' — '+esc(a.market)+' '+a.side+
        ' '+a.from+'¢ → '+a.to+'¢ ('+a.size+') · HTTP '+a.status+' · '+esc(a.note||a.response||'')+'</div>').join('') : '';
  }catch(e){}
}
refresh(); setInterval(refresh, 15000);
</script></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def _authed(self) -> bool:
        if not DASH_PASSWORD:
            return False
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
        if self.path.startswith("/widget.json"):
            # The topline-only endpoint also accepts ?key=<password> — widget
            # apps and Shortcuts often can't set an Authorization header.
            from urllib.parse import parse_qs, urlparse
            key = (parse_qs(urlparse(self.path).query).get("key") or [""])[0]
            if not (self._authed() or key == DASH_PASSWORD):
                self.send_response(401)
                self.send_header("WWW-Authenticate", 'Basic realm="rewards"')
                self.end_headers()
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
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="rewards"')
            self.end_headers()
            return
        if self.path.startswith("/data.json"):
            self._send(200, "application/json", json.dumps(MONITOR.snapshot()).encode())
        elif self.path.startswith("/plan.json"):
            try:
                from urllib.parse import parse_qs, urlparse
                which = (parse_qs(urlparse(self.path).query).get("which") or ["politics"])[0]
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
        elif self.path.startswith("/market.json"):
            from urllib.parse import parse_qs, urlparse
            slug = (parse_qs(urlparse(self.path).query).get("slug") or [""])[0]
            code, payload = market_info(slug)
            self._send(code, "application/json", json.dumps(payload).encode())
        else:
            self._send(200, "text/html; charset=utf-8", DASH_HTML.encode())

    def do_POST(self) -> None:  # noqa: N802 — http.server API
        if not DASH_PASSWORD or not self._authed():
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="rewards"')
            self.end_headers()
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
            if time.time() - winners_refreshed > 3600:  # career totals + payout alert
                winners_refreshed = time.time()
                try:
                    winners, rew_total = load_winners()
                    if winners:
                        WINNERS = winners
                    if rew_total:
                        MONITOR.note_rewards_total(rew_total)
                except Exception:  # noqa: BLE001
                    pass
            orders = tr.fetch_live_orders(key_id, secret_key, event_sizes)
            MONITOR.sample(dt.datetime.now(dt.timezone.utc), orders)
            MONITOR.error = None
            err_streak = 0
            last_ok = time.time()
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
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"live monitor on :{PORT}, polling every {POLL_SECONDS}s")
    server.serve_forever()


if __name__ == "__main__":
    main()
