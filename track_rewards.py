#!/usr/bin/env python3
"""Polymarket US liquidity-rewards tracker.

Fetches your full liquidity-rewards history from the official Incentives API
(https://docs.polymarket.us/incentives/liquidity) and writes:

    data/rewards.csv           every per-day / per-market reward row
    data/checks.csv            one heartbeat row per run (proof of life)
    data/latest_response.json  raw API response from the last successful run
    STATUS.md                  human-readable summary + freshness banner

Each run re-fetches the complete history and rewrites rewards.csv, so the
script is idempotent and self-healing — a missed run loses nothing.

Usage:
    POLYMARKET_KEY_ID=<uuid> POLYMARKET_SECRET_KEY=<base64> python track_rewards.py

Exits non-zero on any failure (after recording it in STATUS.md), so the
GitHub Actions run goes red and GitHub emails you.
"""

from __future__ import annotations

import base64
import csv
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path

import requests
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

# The documented incentives host, then the main API host as a fallback.
HOSTS = [
    "https://api.prod.polymarketexchange.com",
    "https://api.polymarket.us",
]
EARNINGS_PATH = "/v1/incentives/earnings"
# Trading API (authenticated) and public gateway, per the polymarket-us SDK.
TRADE_API = "https://api.polymarket.us"
GATEWAY = "https://gateway.polymarket.us"
# Earliest date the earnings endpoint serves (its documented default).
START_DATE = os.environ.get("REWARDS_START_DATE", "2026-03-21")
RUN_EVERY_HOURS = 1  # keep in sync with .github/workflows/liquidity-rewards.yml
# Set automatically by GitHub Actions; fallback for local runs.
REPO = os.environ.get("GITHUB_REPOSITORY", "wfco223/liquidity-rewards")
WORKFLOW_URL = f"https://github.com/{REPO}/actions/workflows/liquidity-rewards.yml"

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REWARDS_CSV = DATA / "rewards.csv"
CHECKS_CSV = DATA / "checks.csv"
RAW_JSON = DATA / "latest_response.json"
LIVE_CSV = DATA / "live_orders.csv"
STATUS_MD = HERE / "STATUS.md"

MAX_HEARTBEATS = 1000  # cap checks.csv so it never grows unbounded


# --------------------------------------------------------------------------
# API
# --------------------------------------------------------------------------

def auth_headers(key_id: str, secret_key: str, method: str, path: str) -> dict[str, str]:
    """Sign ``timestamp+method+path`` with the account's Ed25519 key.

    Matches the official polymarket-us SDK: the secret is a base64-encoded
    32-byte seed (or 64-byte key, of which the first 32 bytes are the seed).
    """
    timestamp = str(int(time.time() * 1000))
    seed = base64.b64decode(secret_key)
    if len(seed) == 64:
        seed = seed[:32]
    key = Ed25519PrivateKey.from_private_bytes(seed)
    signature = key.sign(f"{timestamp}{method}{path}".encode())
    return {
        "X-PM-Access-Key": key_id,
        "X-PM-Timestamp": timestamp,
        "X-PM-Signature": base64.b64encode(signature).decode(),
    }


def fetch_all_rewards(key_id: str, secret_key: str) -> tuple[list[dict], dict]:
    """Return (normalized reward rows, last raw response page).

    Tries each host in HOSTS; if all fail, raises with each host's actual
    response body plus a no-auth probe of the public /v1/incentives endpoint,
    so a red run is a complete diagnostic.
    """
    errors: list[str] = []
    for host in HOSTS:
        try:
            return _fetch_from_host(host, key_id, secret_key)
        except Exception as e:  # noqa: BLE001 — collect and try next host
            errors.append(str(e))
    for host in HOSTS:  # is the API itself up? (public endpoint, no auth)
        try:
            r = requests.get(host + "/v1/incentives", params={"pageSize": 1}, timeout=15)
            errors.append(f"probe {host}/v1/incentives (no auth) -> HTTP {r.status_code}")
        except Exception as pe:  # noqa: BLE001
            errors.append(f"probe {host}/v1/incentives (no auth) -> {type(pe).__name__}: {pe}")
    raise RuntimeError("\n".join(errors))


def _fetch_from_host(host: str, key_id: str, secret_key: str) -> tuple[list[dict], dict]:
    rows: list[dict] = []
    params: dict = {"startDate": START_DATE}
    raw: dict = {}
    for _ in range(50):  # bounded pagination
        resp = requests.get(
            host + EARNINGS_PATH,
            params=params,
            headers=auth_headers(key_id, secret_key, "GET", EARNINGS_PATH),
            timeout=30,
        )
        if resp.status_code >= 400:
            body = " ".join(resp.text.split())[:300]
            raise RuntimeError(f"{host}{EARNINGS_PATH} -> HTTP {resp.status_code}: {body}")
        raw = resp.json()
        for r in raw.get("rewards") or []:
            rows.append(
                {
                    "date": str(r.get("date", ""))[:10],
                    "market": r.get("marketSlug", ""),
                    "program_type": r.get("programType", ""),
                    "reward_usd": float(r.get("reward", 0) or 0),
                    "status": str(r.get("status", "")).upper(),
                }
            )
        token = raw.get("nextPageToken")
        if not token:
            break
        params["pageToken"] = token
    rows.sort(key=lambda r: (r["date"], r["market"], r["program_type"]))
    return rows, raw


def _num(x) -> float:
    """Best-effort numeric parse: plain numbers, numeric strings, and the
    protobuf-style dict encodings the trading API uses (units/nanos, value)."""
    if x is None:
        return 0.0
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        try:
            return float(x)
        except ValueError:
            return 0.0
    if isinstance(x, dict):
        if "units" in x or "nanos" in x:
            return float(x.get("units", 0) or 0) + float(x.get("nanos", 0) or 0) / 1e9
        for key in ("value", "amount", "px", "price", "qty", "quantity", "decimal"):
            if key in x:
                return _num(x[key])
    return 0.0


def _score_order(order: dict, book: dict | None, prog: dict | None) -> None:
    """Score one resting order per the official program rules
    (https://docs.polymarket.us/incentives/liquidity):

        Score = DiscountFactor ^ (ticks from best price on your side) x Size

    scored only if the order sits inside the Target Size window — the levels
    reached while walking from the best price outward until Target Size
    contracts (raw size, all participants) have accumulated — and only if the
    side holds at least Target Size in total. Sets ticks/share/verdict.
    """
    order["ticks"] = None
    order["share"] = None
    order["est_day"] = None
    if book is None:
        order["verdict"] = "⚠️ book unavailable"
        return
    levels = book["bids"] if order["side"] == "BUY" else book["asks"]
    if not levels:
        order["verdict"] = "⚠️ empty book side"
        return
    tick = book["tick"]
    best = levels[0][0]
    ticks = round(abs(best - order["price"]) / tick)
    order["ticks"] = ticks
    if prog is None:
        order["verdict"] = "❌ no active reward program on this market"
        return
    if not prog.get("df"):
        order["verdict"] = "⚠️ program has no Discount Factor — can't score"
        return
    df, target = prog["df"], prog.get("target") or 0.0

    side_total = sum(q for _, q in levels)
    if target and side_total < target:
        order["verdict"] = f"❌ side has {side_total:,.0f} of {target:,.0f} Target Size — side not qualifying"
        return
    window: list[tuple[float, float]] = []
    cum = 0.0
    for px, qty in levels:
        window.append((px, qty))
        cum += qty
        if target and cum >= target:
            break
    window_end_ticks = round(abs(best - window[-1][0]) / tick)
    if not any(abs(px - order["price"]) < tick / 2 for px, _ in window):
        order["verdict"] = (
            f"❌ outside Target Size window (order {ticks} tick{'s' if ticks != 1 else ''} "
            f"from best; window ends {window_end_ticks})"
        )
        return
    denom = sum(q * df ** round(abs(best - px) / tick) for px, q in window)
    score = order["size"] * df ** ticks
    # The orders and book snapshots are seconds apart, so the book may not
    # fully contain this order — never report a share above 100%.
    denom = max(denom, score)
    share = score / denom if denom else 0.0
    order["share"] = share
    side_name = "bid" if order["side"] == "BUY" else "ask"
    verdict = f"✅ scoring — ~{share * 100:.1f}% of {side_name} side"
    if target:  # show the qualification check so it's verifiable at a glance
        verdict += f" ({side_total:,.0f} resting ≥ {target:,.0f} ✓)"
    if prog.get("pool"):
        order["est_day"] = share * _daily_pool(prog) / 2  # pool assumed split per side
        verdict += f" ≈ {_usd(order['est_day'])}/day"
    order["verdict"] = verdict


def _daily_pool(prog: dict) -> float:
    """Reward pool normalized to $/day using the time period's start/end.
    Missing or sub-day periods are treated as one day."""
    days = 1.0
    try:
        s, e = prog.get("start"), prog.get("end")
        if s and e:
            sd = dt.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
            ed = dt.datetime.fromisoformat(str(e).replace("Z", "+00:00"))
            days = max((ed - sd).total_seconds() / 86400.0, 1.0)
    except Exception:  # noqa: BLE001 — fall back to daily
        pass
    return (prog.get("pool") or 0.0) / days


# Slug tokens that mark U.S. politics markets (elections, primaries,
# nominations, appointments). Everything else — sports, foreign elections —
# is filtered out of the suggestions.
US_POLITICS_HINTS = ("midterm", "attgen", "housepop")


def _is_us_politics(slug: str) -> bool:
    """Token-based check — substring matching is too loose (a tennis player
    code like 'russer' contains 'usse'). US-only: dem/rep tokens, us*-prefixed
    race codes (usse, usgub, ussep, …), or US-specific terms."""
    tokens = slug.split("-")
    if {"dem", "rep"} & set(tokens):
        return True
    return any(t.startswith("us") or t.startswith(US_POLITICS_HINTS) or t.endswith("gov") for t in tokens)


def _political_market_slugs(stats: dict) -> list[str]:
    """Open market slugs from events tagged politics/elections (authoritative,
    unlike slug heuristics)."""
    slugs: list[str] = []
    for tag in ("politics", "elections"):
        params: dict = {"tagSlug": tag, "active": True, "pageSize": 100}
        for _ in range(10):
            r = requests.get(GATEWAY + "/v1/events", params=params, timeout=30)
            if r.status_code >= 400:
                break
            data = r.json()
            for ev in data.get("events") or []:
                for m in ev.get("markets") or []:
                    if m.get("slug") and not m.get("closed"):
                        slugs.append(m["slug"])
            token = data.get("nextPageToken")
            if not token:
                break
            params["pageToken"] = token
    slugs = list(dict.fromkeys(slugs))
    stats["tag_slugs"] = len(slugs)
    return slugs


def _fetch_book(slug: str) -> dict:
    """Fetch a market's order book: sorted (price, qty) levels + tick size."""
    r = requests.get(f"{GATEWAY}/v1/markets/{slug}/book", timeout=15)
    if r.status_code >= 400:
        raise RuntimeError(f"book HTTP {r.status_code}: {' '.join(r.text.split())[:150]}")
    b = r.json()
    md = b.get("book") or b.get("marketData") or b  # tolerate wrappers
    bids = [(_num(l.get("px")), _num(l.get("qty"))) for l in md.get("bids") or []]
    asks = [(_num(l.get("px")), _num(l.get("qty"))) for l in md.get("offers") or md.get("asks") or []]
    bids = sorted([(p, q) for p, q in bids if p > 0 and q > 0], key=lambda x: -x[0])
    asks = sorted([(p, q) for p, q in asks if p > 0 and q > 0], key=lambda x: x[0])
    all_px = [p for p, _ in bids + asks]
    tick = 0.001 if any(round(p * 1000) % 10 for p in all_px) else 0.01
    return {"bids": bids, "asks": asks, "tick": tick}


def _probe_share(levels: list[tuple[float, float]], tick: float, df: float,
                 target: float, probe: float) -> float | None:
    """Estimated share of a side's score if you joined the best price with
    `probe` contracts. None = the side (even with your order) misses Target
    Size, so it wouldn't qualify at all."""
    if not levels:
        return 1.0 if (not target or probe >= target) else None
    best = levels[0][0]
    merged = [(best, levels[0][1] + probe)] + levels[1:]
    if target and sum(q for _, q in merged) < target:
        return None
    window: list[tuple[float, float]] = []
    cum = 0.0
    for px, qty in merged:
        window.append((px, qty))
        cum += qty
        if target and cum >= target:
            break
    denom = sum(q * df ** round(abs(best - px) / tick) for px, q in window)
    return probe / denom if denom else None


def fetch_opportunities(exclude: set[str], probe: float = 200.0) -> list[dict]:
    """Markets with active reward pools you're NOT in, ranked by the share of
    a side's score a `probe`-contract order at the best price would capture.

    Familiar market families (same slug prefix as markets you trade) are
    probed first; book probing is capped to keep runs fast.
    """
    stats = {"tag_slugs": 0, "programs": 0, "pages": 0, "excluded": 0, "not_politics": 0,
             "no_pool_or_df": 0, "candidates": 0, "book_failures": 0, "listed": 0}

    def add_candidate(p: dict) -> None:
        slug = p.get("marketSlug", "")
        if not slug or slug in exclude:
            stats["excluded"] += 1
            return
        if not _is_us_politics(slug):  # tags include foreign races; US only
            stats["not_politics"] += 1
            return
        periods = p.get("timePeriods") or []
        current = [
            tp for tp in periods
            if str(tp.get("status", "")).upper() in ("LIVE", "ACTIVE", "STATUS_LIVE")
        ] or periods
        if not current:
            return
        tp = current[-1]
        try:  # skip programs whose current period already ended
            end = tp.get("end")
            if end and dt.datetime.fromisoformat(str(end).replace("Z", "+00:00")) < dt.datetime.now(dt.timezone.utc):
                stats["ended"] = stats.get("ended", 0) + 1
                return
        except Exception:  # noqa: BLE001 — unparseable end date: keep the candidate
            pass
        df, target, pool = _num(tp.get("discountFactor")), _num(tp.get("targetSize")), _num(tp.get("rewardPool"))
        if pool < 25 or not df:
            stats["no_pool_or_df"] += 1
            return
        candidates.append(
            {"market": slug, "df": df, "target": target, "pool": pool,
             "start": tp.get("start"), "end": tp.get("end")}
        )

    candidates: list[dict] = []
    # Preferred path: markets from events tagged politics, then their programs
    # via the symbols filter — avoids crawling the sports-dominated program list.
    pol_slugs = [s for s in _political_market_slugs(stats) if s not in exclude][:150]
    for i in range(0, len(pol_slugs), 25):
        r = requests.get(
            HOSTS[0] + "/v1/incentives",
            params={"symbols": pol_slugs[i:i + 25], "pageSize": 100},
            timeout=30,
        )
        if r.status_code >= 400:
            continue
        for p in r.json().get("programs") or []:
            stats["programs"] += 1
            add_candidate(p)

    if not candidates:
        # Fallback: deep alphabetical crawl of the program list with the slug
        # classifier. Sports fill the first thousands of entries, hence the cap
        # and early exit.
        params = {"pageSize": 100}
        for _ in range(100):
            r = requests.get(HOSTS[0] + "/v1/incentives", params=params, timeout=30)
            if r.status_code >= 400:
                raise RuntimeError(f"/v1/incentives -> HTTP {r.status_code}")
            data = r.json()
            stats["pages"] += 1
            for p in data.get("programs") or []:
                stats["programs"] += 1
                add_candidate(p)
            token = data.get("nextPageToken")
            if not token or len(candidates) >= 60:
                break
            params["pageToken"] = token

    familiar = {s.split("-")[0] for s in exclude if s}
    candidates.sort(key=lambda c: (c["market"].split("-")[0] not in familiar, -c["pool"]))

    stats["candidates"] = len(candidates)
    out: list[dict] = []
    for c in candidates[:30]:  # cap book probes
        try:
            book = _fetch_book(c["market"])
        except Exception:  # noqa: BLE001 — skip unreadable books
            stats["book_failures"] += 1
            continue
        best: tuple[str, float, float] | None = None
        best_gap: tuple[str, float] | None = None
        for side, levels in (("BUY", book["bids"]), ("SELL", book["asks"])):
            share = _probe_share(levels, book["tick"], c["df"], c["target"], probe)
            if share is not None:
                if best is None or share > best[1]:
                    best = (side, share, sum(q for _, q in levels))
            else:
                # Side can't reach Target Size even with the probe — the pool
                # pays nobody on this side until someone brings the missing size.
                gap = (c["target"] or 0) - (sum(q for _, q in levels) + probe)
                if gap > 0 and (best_gap is None or gap < best_gap[1]):
                    best_gap = (side, gap)
        if best:
            c["side"], c["share"], c["side_depth"] = best
            c["est_day"] = c["share"] * _daily_pool(c) / 2
            out.append(c)
        elif best_gap:
            c["side"], c["gap"] = best_gap
            c["share"] = c["est_day"] = None
            out.append(c)
    out.sort(key=lambda c: (c["est_day"] is None, -(c["est_day"] or 0.0), c.get("gap") or 0.0))
    stats["listed"] = min(len(out), 12)
    try:  # append to the debug file the live snapshot already wrote
        raw_path = DATA / "live_raw.json"
        raw = json.loads(raw_path.read_text()) if raw_path.exists() else {}
        raw["suggestion_stats"] = stats
        raw_path.write_text(json.dumps(raw, indent=2))
    except Exception:  # noqa: BLE001 — diagnostics only
        pass
    return out[:12]


def fetch_live_orders(key_id: str, secret_key: str) -> list[dict]:
    """Snapshot of resting orders scored with the official reward formula.

    This is the "where am I earning right now" view. Informational only — a
    failure here shows a warning in STATUS.md but never fails the run.
    """
    path = "/v1/orders/open"
    resp = requests.get(
        TRADE_API + path,
        headers=auth_headers(key_id, secret_key, "GET", path),
        timeout=30,
    )
    if resp.status_code >= 400:
        raise RuntimeError(f"{path} -> HTTP {resp.status_code}: {' '.join(resp.text.split())[:200]}")
    payload = resp.json()
    orders: list[dict] = []
    for o in payload.get("orders") or []:
        slug = o.get("marketSlug") or (o.get("marketMetadata") or {}).get("slug") or ""
        size = _num(o.get("leavesQuantity"))
        if not size:
            size = _num(o.get("quantity"))
        orders.append(
            {
                "market": slug,
                "side": "BUY" if str(o.get("side", "")).upper().endswith("BUY") else "SELL",
                "price": _num(o.get("price")),
                "size": size,
            }
        )

    slugs = sorted({o["market"] for o in orders if o["market"]})[:25]

    # Full order books (public) — needed for ticks-from-best and the window walk.
    books: dict[str, dict] = {}
    debug: dict[str, str] = {}
    for slug in slugs:
        try:
            books[slug] = _fetch_book(slug)
        except Exception as e:  # noqa: BLE001 — a market without a book still gets listed
            debug[slug] = f"book {type(e).__name__}: {e}"

    # Program parameters: Discount Factor, Target Size, reward pool.
    progs: dict[str, dict] = {}
    if slugs:
        try:
            r = requests.get(
                HOSTS[0] + "/v1/incentives", params={"symbols": slugs, "pageSize": 100}, timeout=20
            )
            if r.status_code < 400:
                for p in r.json().get("programs") or []:
                    periods = p.get("timePeriods") or []
                    current = [
                        tp for tp in periods
                        if str(tp.get("status", "")).upper() in ("LIVE", "ACTIVE", "STATUS_LIVE")
                    ] or periods
                    if current:
                        tp = current[-1]
                        progs[p.get("marketSlug", "")] = {
                            "df": _num(tp.get("discountFactor")),
                            "target": _num(tp.get("targetSize")),
                            "pool": _num(tp.get("rewardPool")),
                            "start": tp.get("start"),
                            "end": tp.get("end"),
                        }
            else:
                debug["_incentives"] = f"HTTP {r.status_code}: {' '.join(r.text.split())[:150]}"
        except Exception as e:  # noqa: BLE001 — params are needed for verdicts but not fatal
            debug["_incentives"] = f"{type(e).__name__}: {e}"

    DATA.mkdir(exist_ok=True)
    (DATA / "live_raw.json").write_text(  # schema + failure reference for debugging
        json.dumps({"orders": payload, "programs": progs, "debug": debug}, indent=2)
    )

    for o in orders:
        prog = progs.get(o["market"])
        o["pool"] = prog.get("pool") if prog else None
        _score_order(o, books.get(o["market"]), prog)
    orders.sort(key=lambda o: (o["share"] is None, -(o["share"] or 0.0), o["ticks"] if o["ticks"] is not None else 999))
    return orders


# --------------------------------------------------------------------------
# Files
# --------------------------------------------------------------------------

def write_rewards_csv(rows: list[dict]) -> None:
    DATA.mkdir(exist_ok=True)
    with REWARDS_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "market", "program_type", "reward_usd", "status"])
        writer.writeheader()
        writer.writerows(rows)


def append_heartbeat(result: str, n_rows: int, total: float, note: str) -> list[dict]:
    """Append one line to checks.csv and return all heartbeats (newest last)."""
    DATA.mkdir(exist_ok=True)
    beats: list[dict] = []
    if CHECKS_CSV.exists():
        with CHECKS_CSV.open(newline="") as f:
            beats = list(csv.DictReader(f))
    beats.append(
        {
            "checked_at_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
            "result": result,
            "reward_rows": str(n_rows),
            "total_usd": f"{total:.2f}",
            "note": " ".join(note.split())[:400],
        }
    )
    beats = beats[-MAX_HEARTBEATS:]
    with CHECKS_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["checked_at_utc", "result", "reward_rows", "total_usd", "note"])
        writer.writeheader()
        writer.writerows(beats)
    return beats


# --------------------------------------------------------------------------
# STATUS.md
# --------------------------------------------------------------------------

def _usd(x: float) -> str:
    return f"${x:,.2f}"


def _bar(value: float, max_value: float, width: int = 20) -> str:
    if max_value <= 0:
        return ""
    n = round(width * value / max_value)
    return "█" * max(n, 1 if value > 0 else 0)


def _group_sum(rows: list[dict], key) -> dict[str, float]:
    out: dict[str, float] = {}
    for r in rows:
        k = key(r)
        out[k] = out.get(k, 0.0) + r["reward_usd"]
    return out


def write_live_csv(orders: list[dict]) -> None:
    DATA.mkdir(exist_ok=True)
    with LIVE_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["market", "side", "price", "size", "ticks", "share", "est_day", "pool", "verdict"]
        )
        writer.writeheader()
        writer.writerows(orders)


def write_status(
    rows: list[dict],
    beats: list[dict],
    error: str | None,
    live_orders: list[dict] | None = None,
    live_error: str | None = None,
    opportunities: list[dict] | None = None,
) -> None:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total = sum(r["reward_usd"] for r in rows)
    by_status = _group_sum(rows, lambda r: r["status"] or "UNKNOWN")
    by_day = _group_sum(rows, lambda r: r["date"])
    by_month = _group_sum(rows, lambda r: r["date"][:7])
    by_market = _group_sum(rows, lambda r: r["market"])

    lines: list[str] = []
    lines.append("# Polymarket US — Liquidity Rewards")
    lines.append("")
    lines.append(f"[![Track liquidity rewards]({WORKFLOW_URL}/badge.svg)]({WORKFLOW_URL})")
    lines.append("")
    if error:
        lines.append(f"## ❌ Last check FAILED — {now}")
        lines.append("")
        lines.append(f"```\n{error}\n```")
        lines.append("")
        lines.append(f"The data below is from the last successful run. See the [Actions tab]({WORKFLOW_URL}) for logs.")
    else:
        lines.append(f"## ✅ Last successful check: {now}")
        lines.append("")
        lines.append(
            f"This runs automatically every {'hour' if RUN_EVERY_HOURS == 1 else f'{RUN_EVERY_HOURS} hours'}. "
            f"**If the timestamp above is more than ~{RUN_EVERY_HOURS + 1} hours old, something is broken** — "
            f"check the [Actions tab]({WORKFLOW_URL})."
        )
    lines.append("")

    if live_orders is not None or live_error:
        lines.append("## 📍 Right now — your resting orders")
        lines.append("")
        if live_error:
            lines.append(f"⚠️ Couldn't fetch live orders this run: `{live_error}`")
        elif not live_orders:
            lines.append("_No resting orders on the book right now._")
        else:
            rate = sum(o["est_day"] for o in live_orders if o.get("est_day"))
            lines.append(f"### Estimated earning rate: ~{_usd(rate)}/day (~{_usd(rate / 24)}/hour)")
            lines.append("")
            lines.append(
                "Rough estimate — assumes the books, pools, and your orders stay as they are, "
                "both sides keep qualifying, and each pool splits evenly between bid and ask. "
                "Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, "
                "counting only orders inside the Target Size window. Earning orders first."
            )
            lines.append("")
            lines.append("| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |")
            lines.append("|---|---|---:|---:|---:|---:|---|")
            for o in live_orders[:30]:
                ticks = f"{o['ticks']}" if o.get("ticks") is not None else "—"
                pool = _usd(o["pool"]) if o.get("pool") else "—"
                lines.append(
                    f"| `{o['market']}` | {o['side']} | {o['price'] * 100:.1f}¢ "
                    f"| {o['size']:,.0f} | {ticks} | {pool} | {o.get('verdict', '—')} |"
                )
            if len(live_orders) > 30:
                lines.append(f"| …and {len(live_orders) - 30} more | | | | | | |")
        lines.append("")

    if opportunities:
        lines.append("## 💡 Suggested U.S. political markets — active pools you're not in")
        lines.append("")
        lines.append(
            "U.S. politics only. Ranked by what a **200-contract order at the best price** "
            "would earn today, using each market's real book, Discount Factor, and "
            "Target Size (same assumptions as the earning rate above)."
        )
        lines.append("")
        lines.append("| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |")
        lines.append("|---|---:|---:|---:|---|---:|---:|")
        for c in opportunities:
            if c.get("share") is not None:
                entry = f"{c['side']} side ({c['side_depth']:,.0f} resting)"
                share, est = f"~{c['share'] * 100:.1f}%", f"~{_usd(c['est_day'])}"
            else:
                entry = f"{c['side']} — needs +{c['gap']:,.0f} contracts to unlock the pool"
                share = est = "—"
            lines.append(
                f"| `{c['market']}` | {_usd(c['pool'])} | {c['df']:.2f} | {c['target']:,.0f} "
                f"| {entry} | {share} | {est} |"
            )
        lines.append("")
    elif opportunities is not None:
        lines.append("## 💡 Suggested U.S. political markets")
        lines.append("")
        lines.append("_No U.S. political markets with reachable pools found this run._")
        lines.append("")

    lines.append("## Totals")
    lines.append("")
    lines.append("| | Amount |")
    lines.append("|---|---:|")
    for status in sorted(by_status):
        lines.append(f"| {status.title()} | {_usd(by_status[status])} |")
    lines.append(f"| **Total earned** | **{_usd(total)}** |")
    lines.append("")
    lines.append(f"{len(rows)} reward rows · {len(by_day)} days with rewards · {len(by_market)} markets · since {START_DATE}")
    lines.append("")

    if by_day:
        lines.append("## Last 14 days")
        lines.append("")
        lines.append("| Date | Rewards | |")
        lines.append("|---|---:|---|")
        recent = sorted(by_day)[-14:]
        peak = max(by_day[d] for d in recent)
        for d in reversed(recent):
            lines.append(f"| {d} | {_usd(by_day[d])} | `{_bar(by_day[d], peak)}` |")
        lines.append("")

        lines.append("## By month")
        lines.append("")
        lines.append("| Month | Rewards | |")
        lines.append("|---|---:|---|")
        peak_m = max(by_month.values())
        for m in sorted(by_month, reverse=True):
            lines.append(f"| {m} | {_usd(by_month[m])} | `{_bar(by_month[m], peak_m)}` |")
        lines.append("")

        lines.append("## Top markets (lifetime)")
        lines.append("")
        lines.append("| Market | Rewards |")
        lines.append("|---|---:|")
        for market, amount in sorted(by_market.items(), key=lambda kv: -kv[1])[:15]:
            lines.append(f"| `{market}` | {_usd(amount)} |")
        lines.append("")
    else:
        lines.append("_No rewards recorded yet. Once your resting orders start earning, they will show up here._")
        lines.append("")

    lines.append("## Recent checks")
    lines.append("")
    lines.append("| Checked (UTC) | Result | Rows | Total |")
    lines.append("|---|---|---:|---:|")
    for b in reversed(beats[-10:]):
        icon = "✅" if b["result"] == "ok" else "❌"
        lines.append(f"| {b['checked_at_utc']} | {icon} {b['result']} | {b['reward_rows']} | ${b['total_usd']} |")
    lines.append("")
    lines.append("Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)")
    lines.append("")

    STATUS_MD.write_text("\n".join(lines))


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def load_existing_rows() -> list[dict]:
    if not REWARDS_CSV.exists():
        return []
    with REWARDS_CSV.open(newline="") as f:
        return [
            {**r, "reward_usd": float(r["reward_usd"])}
            for r in csv.DictReader(f)
        ]


def main() -> int:
    key_id = os.environ.get("POLYMARKET_KEY_ID", "").strip()
    secret_key = os.environ.get("POLYMARKET_SECRET_KEY", "").strip()

    error: str | None = None
    rows: list[dict] = []

    if not key_id or not secret_key:
        error = (
            "Missing credentials. Set POLYMARKET_KEY_ID and POLYMARKET_SECRET_KEY "
            "(repo Settings → Secrets and variables → Actions). Create keys at "
            "polymarket.us → Settings → API."
        )
    else:
        try:
            rows, raw = fetch_all_rewards(key_id, secret_key)
            write_rewards_csv(rows)
            RAW_JSON.write_text(json.dumps(raw, indent=2))
        except Exception as e:  # noqa: BLE001 — any failure must go red, not crash silently
            error = f"{type(e).__name__}: {e}"

    if error:
        rows = load_existing_rows()  # keep showing last good data

    live_orders: list[dict] | None = None
    live_error: str | None = None
    opportunities: list[dict] | None = None
    if not error:
        try:
            live_orders = fetch_live_orders(key_id, secret_key)
            write_live_csv(live_orders)
        except Exception as e:  # noqa: BLE001 — live view is informational only
            live_error = f"{type(e).__name__}: {e}"
        try:
            my_markets = {o["market"] for o in live_orders or [] if o["market"]}
            opportunities = fetch_opportunities(my_markets)
        except Exception as e:  # noqa: BLE001 — suggestions are informational only
            opportunities = None
            print(f"suggestions failed: {type(e).__name__}: {e}", file=sys.stderr)

    total = sum(r["reward_usd"] for r in rows)
    beats = append_heartbeat("ok" if not error else "error", len(rows), total, error or "")
    write_status(rows, beats, error, live_orders, live_error, opportunities)

    if error:
        print(f"FAILED: {error}", file=sys.stderr)
        return 1
    print(f"OK: {len(rows)} reward rows, total {_usd(total)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
