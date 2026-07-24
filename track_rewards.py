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

try:
    from zoneinfo import ZoneInfo
    ET = ZoneInfo("America/New_York")  # Polymarket's reward day runs midnight–midnight ET
except Exception:  # noqa: BLE001 — no tz database: fall back to fixed EDT offset
    ET = dt.timezone(dt.timedelta(hours=-4), "ET")


def _et_str(utc_str: str | None = None) -> str:
    """A UTC 'YYYY-mm-dd HH:MM:SS' timestamp (or now) rendered in Eastern Time."""
    if utc_str:
        t = dt.datetime.strptime(utc_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)
    else:
        t = dt.datetime.now(dt.timezone.utc)
    loc = t.astimezone(ET)
    return loc.strftime("%Y-%m-%d %I:%M %p ET").replace(" 0", " ")


def _et_day(utc_str: str) -> str:
    """The Eastern-Time reward day a UTC timestamp belongs to."""
    t = dt.datetime.strptime(utc_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)
    return t.astimezone(ET).strftime("%Y-%m-%d")

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
EST_CSV = DATA / "estimates.csv"
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
    order["window"] = []       # [[price_cents, resting, is_your_level], ...]
    order["window_more"] = 0   # window levels beyond the first 10
    calc: list[str] = []       # bare arithmetic, no prose
    order["calc"] = calc
    if book is None:
        order["verdict"] = "⚠️ book unavailable"
        calc.append("no book data → can't score")
        return
    levels = book["bids"] if order["side"] == "BUY" else book["asks"]
    side_name = "bid" if order["side"] == "BUY" else "ask"
    if not levels:
        order["verdict"] = "⚠️ empty book side"
        calc.append(f"{side_name} side empty → score 0")
        return
    tick = book["tick"]
    best = levels[0][0]
    ticks = round(abs(best - order["price"]) / tick)
    order["ticks"] = ticks

    def mine(px: float) -> bool:
        return abs(px - order["price"]) < tick / 2

    if prog is None:
        order["verdict"] = "❌ no active reward program on this market"
        calc.append("no reward program → $0")
        return
    if not prog.get("df"):
        order["verdict"] = "⚠️ program has no Discount Factor — can't score"
        return
    df, target = prog["df"], prog.get("target") or 0.0

    order["df"] = df

    def scored(lvls: list[tuple[float, float]]) -> list[tuple[float, float, int, float]]:
        out = []
        for px, qty in lvls:
            t = round(abs(best - px) / tick)
            out.append((px, qty, t, qty * df ** t))
        return out

    side_total = sum(q for _, q in levels)
    if target and side_total < target:
        order["verdict"] = f"❌ side has {side_total:,.0f} of {target:,.0f} Target Size — side not qualifying"
        order["window"] = [
            [round(px * 100, 1), q, mine(px), t, round(c, 1)] for px, q, t, c in scored(levels[:10])
        ]
        calc.append(f"side {side_total:,.0f} < target {target:,.0f} → side pays nobody")
        return
    window: list[tuple[float, float]] = []
    cum = 0.0
    for px, qty in levels:
        window.append((px, qty))
        cum += qty
        if target and cum >= target:
            break
    window_end_ticks = round(abs(best - window[-1][0]) / tick)
    window_scored = scored(window)
    denom = sum(c for _, _, _, c in window_scored)
    order["window"] = [
        [round(px * 100, 1), q, mine(px), t, round(c, 1)] for px, q, t, c in window_scored[:10]
    ]
    order["window_more"] = max(len(window) - 10, 0)
    order["window_more_score"] = round(sum(c for *_, c in window_scored[10:]), 1)
    order["denom"] = round(denom, 1)
    if not any(mine(px) for px, _ in window):
        order["verdict"] = (
            f"❌ outside Target Size window (order {ticks} tick{'s' if ticks != 1 else ''} "
            f"from best; window ends {window_end_ticks})"
        )
        calc.append(f"you {ticks}t from best, window ends {window_end_ticks}t → score 0")
        return
    score = order["size"] * df ** ticks
    # The orders and book snapshots are seconds apart, so the book may not
    # fully contain this order — never report a share above 100%.
    if score > denom:
        calc.append("(book missing your order — capped at 100%)")
    denom = max(denom, score)
    share = score / denom if denom else 0.0
    order["share"] = share
    calc.append(f"yours {score:,.1f} / Σ {denom:,.1f} = {share * 100:.1f}%")
    verdict = f"✅ scoring — ~{share * 100:.1f}% of {side_name} side"
    if target:  # show the qualification check so it's verifiable at a glance
        verdict += f" ({side_total:,.0f} resting ≥ {target:,.0f} ✓)"
    if prog.get("pool"):
        order["est_day"] = share * _daily_pool(prog) / 2  # pool assumed split per side
        verdict += f" ≈ {_usd(order['est_day'])}/day"
        n = prog.get("event_n") or 1
        order["event_n"] = n
        order["siblings"] = prog.get("siblings") or []
        if n > 1:
            verdict += f" (pool ÷ {n} markets)"
        side_pool = _daily_pool(prog) / 2
        calc.append(
            f"${prog['pool']:,.0f} ÷ {n} ÷ 2 = {_usd(side_pool)} × {share * 100:.1f}% "
            f"= {_usd(order['est_day'])}/day"
        )
    order["verdict"] = verdict


def _daily_pool(prog: dict) -> float:
    """Reward pool normalized to $/day using the time period's start/end,
    prorated across the open markets of the event it covers (the pool is per
    event, not per candidate market). Missing/sub-day periods count as one day."""
    days = 1.0
    try:
        s, e = prog.get("start"), prog.get("end")
        if s and e:
            sd = dt.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
            ed = dt.datetime.fromisoformat(str(e).replace("Z", "+00:00"))
            days = max((ed - sd).total_seconds() / 86400.0, 1.0)
    except Exception:  # noqa: BLE001 — fall back to daily
        pass
    return (prog.get("pool") or 0.0) / days / max(prog.get("event_n") or 1, 1)


EVENT_DEBUG: dict[str, str] = {}  # per-slug event lookup outcomes, for live_raw.json
RACE_MEMBERS: dict[str, list[str]] = {}  # per-slug: the sibling markets its divisor counted
SEARCH_KEY_MEMBERS: dict[str, list[str]] = {}  # per race-key: slugs found by prefix search


def _note_members(slug: str, members: list[str]) -> None:
    """Remember the largest known sibling list for a market — it's what the
    proration divisor counted, shown so the division can be audited."""
    if len(members) > len(RACE_MEMBERS.get(slug, [])):
        RACE_MEMBERS[slug] = sorted(members)


def _event_size(slug: str) -> int | None:
    """Number of open markets in the event this market belongs to."""
    try:
        r = requests.get(f"{GATEWAY}/v1/market/slug/{slug}", timeout=15)
        if r.status_code >= 400:
            EVENT_DEBUG[slug] = f"market detail HTTP {r.status_code}"
            return None
        j = r.json()
        md = j.get("market") or j.get("marketData") or j
        ev_slug = (
            md.get("eventSlug")
            or (md.get("event") or {}).get("slug")
            or (md.get("marketMetadata") or {}).get("eventSlug")
        )
        if ev_slug:
            r = requests.get(f"{GATEWAY}/v1/events/slug/{ev_slug}", timeout=15)
            if r.status_code < 400:
                ev = r.json().get("event") or r.json()
                open_slugs = [m["slug"] for m in ev.get("markets") or []
                              if m.get("slug") and not m.get("closed")]
                if open_slugs:
                    EVENT_DEBUG[slug] = f"event {ev_slug}: {len(open_slugs)} open markets"
                    _note_members(slug, open_slugs)
                    return len(open_slugs)
        # Market details carry no eventSlug in practice, but race siblings
        # share the exact `question` text — search for it and count the open
        # markets of the event that contains this market.
        return _race_size_for(slug, md.get("question") or md.get("title"))
    except Exception as e:  # noqa: BLE001
        EVENT_DEBUG[slug] = f"{type(e).__name__}: {e}"
        return None


def _race_size_for(slug: str, question: str | None) -> int | None:
    """Find the event containing this market via search (by its question,
    then by race slug prefix) and count that event's open markets."""
    queries = [q for q in (question, slug.rsplit("-", 1)[0]) if q]
    for query in queries:
        try:
            r = requests.get(
                GATEWAY + "/v1/search", params={"query": query, "limit": 20}, timeout=15
            )
            if r.status_code >= 400:
                continue
            for ev in r.json().get("events") or []:
                mkts = [m for m in ev.get("markets") or [] if m.get("slug")]
                if any(m["slug"] == slug for m in mkts):
                    open_slugs = [m["slug"] for m in mkts if not m.get("closed")]
                    if open_slugs:
                        EVENT_DEBUG[slug] = (
                            f"search '{str(query)[:40]}': event {ev.get('slug', '?')} "
                            f"with {len(open_slugs)} open markets"
                        )
                        _note_members(slug, open_slugs)
                        return len(open_slugs)
        except Exception as e:  # noqa: BLE001
            EVENT_DEBUG[slug] = f"search {type(e).__name__}: {e}"
    EVENT_DEBUG.setdefault(slug, f"no event found via search for {slug}")
    return None


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


def fetch_politics_events() -> tuple[list[str], dict[str, int]]:
    """From events tagged politics/elections (authoritative, unlike slug
    heuristics): (ordered open market slugs, market slug -> number of open
    markets in its event). The event size prorates the event-level pool."""
    slugs: list[str] = []
    sizes: dict[str, int] = {}
    for tag in ("politics", "elections"):
        offset = 0
        for _ in range(30):  # events paginate with limit/offset, not pageToken
            r = requests.get(
                GATEWAY + "/v1/events",
                params={"tagSlug": tag, "active": "true", "limit": 100, "offset": offset},
                timeout=30,
            )
            if r.status_code >= 400:
                break
            events = r.json().get("events") or []
            for ev in events:
                open_mkts = [m["slug"] for m in ev.get("markets") or []
                             if m.get("slug") and not m.get("closed")]
                for s in open_mkts:
                    slugs.append(s)
                    sizes[s] = len(open_mkts)
                    _note_members(s, open_mkts)
            if len(events) < 100:
                break
            offset += 100
    slugs = list(dict.fromkeys(slugs))
    # Candidate markets of one race are sometimes modeled as separate
    # single-market events, but the pool covers the whole race — also group by
    # the slug minus its last token and prorate by the larger grouping.
    race_map: dict[str, list[str]] = {}
    for s in slugs:
        race_map.setdefault(s.rsplit("-", 1)[0], []).append(s)
    for s in slugs:
        group = race_map[s.rsplit("-", 1)[0]]
        if len(group) > sizes.get(s, 1):
            sizes[s] = len(group)
            _note_members(s, group)
    return slugs, sizes


def _race_size(race_key: str) -> int | None:
    """Count open markets whose slug starts with the race prefix, via search.
    Slugs follow a naming convention: everything before the final token names
    the race, so this finds all sibling markets sharing one reward pool."""
    try:
        r = requests.get(
            GATEWAY + "/v1/search", params={"query": race_key, "limit": 50}, timeout=15
        )
        r.raise_for_status()
        seen: set[str] = set()
        for ev in r.json().get("events") or []:
            for m in ev.get("markets") or []:
                s = m.get("slug", "")
                if (s.startswith(race_key + "-") or s == race_key) and not m.get("closed"):
                    seen.add(s)
        if seen:
            SEARCH_KEY_MEMBERS[race_key] = sorted(seen)
        return len(seen) or None
    except Exception:  # noqa: BLE001 — search is a best-effort refinement
        return None


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


def fetch_opportunities(
    exclude: set[str],
    pol_slugs: list[str],
    event_sizes: dict[str, int],
    probe: float = 200.0,
) -> list[dict]:
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
             "start": tp.get("start"), "end": tp.get("end"),
             "event_n": event_sizes.get(slug, 1)}
        )

    candidates: list[dict] = []
    # Preferred path: markets from events tagged politics, then their programs
    # via the symbols filter — avoids crawling the sports-dominated program list.
    stats["tag_slugs"] = len(pol_slugs)
    pol_slugs = [s for s in pol_slugs if s not in exclude][:150]
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


PROG_TTL_SECONDS = 300  # reuse fetched program params this long between polls
_PROG_CACHE: dict = {"ts": 0.0, "progs": {}, "slugs": ()}


def fetch_live_orders(key_id: str, secret_key: str, event_sizes: dict[str, int] | None = None) -> list[dict]:
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
                "id": str(o.get("id") or ""),
                "market": slug,
                "side": "BUY" if str(o.get("side", "")).upper().endswith("BUY") else "SELL",
                "price": _num(o.get("price")),
                "size": size,
            }
        )

    slugs = sorted({o["market"] for o in orders if o["market"]})
    debug: dict[str, str] = {}
    if len(slugs) > 100:  # safety bound — never truncate silently
        debug["_slug_cap"] = f"{len(slugs)} markets with orders; scoring the first 100"
        slugs = slugs[:100]

    # Full order books (public) — needed for ticks-from-best and the window walk.
    books: dict[str, dict] = {}
    for slug in slugs:
        try:
            books[slug] = _fetch_book(slug)
        except Exception as e:  # noqa: BLE001 — a market without a book still gets listed
            debug[slug] = f"book {type(e).__name__}: {e}"

    # Program parameters: Discount Factor, Target Size, reward pool.
    # Cached between calls: the params change ~daily, while the live monitor
    # calls this every poll — refetching each time both wastes rate limit and
    # turns one failed request into a page full of "no rewards program".
    progs: dict[str, dict] = {}
    if slugs:
        now = time.time()
        cache_ok = (now - _PROG_CACHE["ts"] < PROG_TTL_SECONDS
                    and set(slugs) <= set(_PROG_CACHE["slugs"]))
        if cache_ok:
            progs = {s: _PROG_CACHE["progs"][s] for s in slugs if s in _PROG_CACHE["progs"]}
        else:
            fetched: dict[str, dict] | None = None
            for host in HOSTS:  # try each host before giving up
                try:
                    r = requests.get(
                        host + "/v1/incentives", params={"symbols": slugs, "pageSize": 100}, timeout=20
                    )
                    if r.status_code >= 400:
                        debug["_incentives"] = f"{host}: HTTP {r.status_code}: {' '.join(r.text.split())[:150]}"
                        continue
                    fetched = {}
                    for p in r.json().get("programs") or []:
                        periods = p.get("timePeriods") or []
                        current = [
                            tp for tp in periods
                            if str(tp.get("status", "")).upper() in ("LIVE", "ACTIVE", "STATUS_LIVE")
                        ] or periods
                        if current:
                            tp = current[-1]
                            fetched[p.get("marketSlug", "")] = {
                                "df": _num(tp.get("discountFactor")),
                                "target": _num(tp.get("targetSize")),
                                "pool": _num(tp.get("rewardPool")),
                                "start": tp.get("start"),
                                "end": tp.get("end"),
                            }
                    break
                except Exception as e:  # noqa: BLE001 — params are needed for verdicts but not fatal
                    debug["_incentives"] = f"{host}: {type(e).__name__}: {e}"
            if fetched is not None:
                progs = fetched
                _PROG_CACHE.update(ts=now, progs=dict(fetched), slugs=tuple(slugs))
            elif _PROG_CACHE["progs"]:  # fetch failed — stale params beat none at all
                progs = {s: _PROG_CACHE["progs"][s] for s in slugs if s in _PROG_CACHE["progs"]}
                debug["_incentives_note"] = "programs fetch failed — using cached parameters"

    # Event sizes prorate the event-level pool; look up any market the
    # politics-tag map doesn't cover (bounded).
    event_sizes = dict(event_sizes or {})
    lookups = 0
    for slug in progs:
        if slug not in event_sizes and lookups < 20:
            lookups += 1
            n = _event_size(slug)
            if n:
                event_sizes[slug] = n
    # Race grouping across everything known (tag map + our own markets):
    # candidate markets of one race share the pool even when modeled as
    # separate single-market events the tag map missed.
    race_map: dict[str, list[str]] = {}
    for s in set(event_sizes) | set(progs):
        race_map.setdefault(s.rsplit("-", 1)[0], []).append(s)
    for slug in progs:
        group = race_map.get(slug.rsplit("-", 1)[0], [])
        progs[slug]["event_n"] = max(event_sizes.get(slug, 1), len(group))
        if len(group) >= progs[slug]["event_n"]:
            _note_members(slug, group)
    # Definitive pass: search the race prefix to find ALL sibling markets,
    # including ones neither the tag map nor our portfolio knows about.
    race_search: dict[str, int | None] = {}
    for slug in progs:
        key = slug.rsplit("-", 1)[0]
        if key not in race_search:
            race_search[key] = _race_size(key) if len(race_search) < 10 else None
        if race_search[key]:
            progs[slug]["event_n"] = max(progs[slug]["event_n"], race_search[key])
            _note_members(slug, SEARCH_KEY_MEMBERS.get(key, []))
    for slug in progs:
        progs[slug]["siblings"] = RACE_MEMBERS.get(slug, [])[:40]

    DATA.mkdir(exist_ok=True)
    (DATA / "live_raw.json").write_text(  # schema + failure reference for debugging
        json.dumps(
            {"orders": payload, "programs": progs, "debug": debug, "event_debug": EVENT_DEBUG},
            indent=2,
        )
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


def append_estimates(live_orders: list[dict]) -> None:
    """Record each run's per-market estimated $/day so days can later be
    reconciled against what Polymarket actually paid."""
    DATA.mkdir(exist_ok=True)
    rows: list[dict] = []
    if EST_CSV.exists():
        with EST_CSV.open(newline="") as f:
            rows = list(csv.DictReader(f))
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    for o in live_orders:
        if o.get("est_day"):
            rows.append({"checked_at_utc": ts, "market": o["market"], "est_day": f"{o['est_day']:.4f}"})
    rows = rows[-30000:]
    with EST_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["checked_at_utc", "market", "est_day"])
        writer.writeheader()
        writer.writerows(rows)


def _estimate_days() -> dict[str, dict]:
    """Per day: time-averaged estimated $/day, total and per market."""
    if not EST_CSV.exists():
        return {}
    samples: dict[str, set[str]] = {}
    sums: dict[str, dict[str, float]] = {}
    with EST_CSV.open(newline="") as f:
        for r in csv.DictReader(f):
            day = _et_day(r["checked_at_utc"])  # reward days are Eastern Time
            samples.setdefault(day, set()).add(r["checked_at_utc"])
            sums.setdefault(day, {})
            sums[day][r["market"]] = sums[day].get(r["market"], 0.0) + float(r["est_day"])
    out: dict[str, dict] = {}
    for day, per_market in sums.items():
        n = max(len(samples[day]), 1)
        avg = {m: v / n for m, v in per_market.items()}
        out[day] = {"per_market": avg, "total": sum(avg.values()), "samples": n}
    return out


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
            f,
            fieldnames=["market", "side", "price", "size", "ticks", "share", "est_day", "pool", "verdict"],
            extrasaction="ignore",
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
    now = _et_str()
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

    # ---- the answer up top; all supporting detail lives below the divider ----
    lines.append("## 📌 Summary")
    lines.append("")
    if live_orders:
        rate = sum(o["est_day"] for o in live_orders if o.get("est_day"))
        lines.append(f"**Earning right now:** ~{_usd(rate)}/day estimated (ceiling, not promise — details below)")
    else:
        lines.append("**Earning right now:** couldn't be estimated this run — see details below")
    lines.append("")
    recent = sorted(by_day)[-3:][::-1]
    if recent:
        days_out = " · ".join(f"{d}: **{_usd(by_day[d])}**" for d in recent)
        lines.append(
            f"**Earned:** {_usd(total)} lifetime ({_usd(by_status.get('PAID', 0))} paid). "
            f"Last three recorded days — {days_out} _(Polymarket reports ~1–2 days behind)_"
        )
    else:
        lines.append(f"**Earned:** {_usd(total)} lifetime")
    lines.append("")
    recs = [c for c in (opportunities or []) if c.get("share") is not None][:3]
    if recs:
        first = recs[0]
        rest = ", ".join(f"`{c['market']}` (~{_usd(c['est_day'])}/day)" for c in recs[1:])
        lines.append(
            f"**What else to join:** `{first['market']}` — {first['side']} at the best price, "
            f"~{_usd(first['est_day'])}/day for 200 contracts"
            + (f". Runners-up: {rest}" if rest else "")
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# The details (how the numbers above are computed)")
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
                "both sides keep qualifying, each pool covers its whole event/race (so it's "
                "divided across that race's open markets), and splits evenly between bid and ask. "
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
            lines.append("**Tap an order for its book window and the math:**")
            lines.append("")
            for o in live_orders[:30]:
                if not o.get("calc") and not o.get("window"):
                    continue
                est = f"{_usd(o['est_day'])}/day" if o.get("est_day") else "$0"
                lines.append(
                    f"<details><summary><code>{o['market']}</code> {o['side']} "
                    f"{o['size']:,.0f} @ {o['price'] * 100:g}¢ → {est}</summary>"
                )
                lines.append("")
                if o.get("window"):
                    side_label = "Bids" if o["side"] == "BUY" else "Asks"
                    df = o.get("df")
                    lines.append(f"| | {side_label} | Resting | Score |")
                    lines.append("|---|---:|---:|---:|")
                    for px, qty, is_mine, t, c in o["window"]:
                        marker = "▶" if is_mine else ""
                        yours = f" ({o['size']:,.0f} yours)" if is_mine else ""
                        cell = f"×{df:g}^{t} = {c:,.1f}" if df is not None else ""
                        lines.append(f"| {marker} | {px:g}¢ | {qty:,.0f}{yours} | {cell} |")
                    if o.get("window_more"):
                        lines.append(
                            f"| | … | +{o['window_more']} levels | {o.get('window_more_score', 0):,.1f} |"
                        )
                    if o.get("denom") is not None:
                        lines.append(f"| | | **Σ** | **{o['denom']:,.1f}** |")
                    lines.append("")
                for c in o.get("calc", []):
                    lines.append(f"`{c}`  ")
                sibs = o.get("siblings") or []
                n = o.get("event_n") or 1
                if n > 1 and sibs:
                    note = "" if len(sibs) == n else f" ({len(sibs)} known)"
                    lines.append("")
                    lines.append(f"<details><summary>÷ {n} markets in this race{note} — tap to list</summary>")
                    lines.append("")
                    for i, s in enumerate(sibs, 1):
                        marker = " ← this one" if s == o["market"] else ""
                        lines.append(f"{i}. `{s}`{marker}")
                    lines.append("")
                    lines.append("</details>")
                lines.append("")
                lines.append("</details>")
        lines.append("")

    lines.append("## 📊 Estimate vs. actual — where the gap is")
    lines.append("")
    est_days = _estimate_days()
    actual_by_day_market: dict[str, dict[str, float]] = {}
    for r in rows:
        actual_by_day_market.setdefault(r["date"], {})
        actual_by_day_market[r["date"]][r["market"]] = (
            actual_by_day_market[r["date"]].get(r["market"], 0.0) + r["reward_usd"]
        )
    reconciled = sorted(set(est_days) & set(by_day))[-3:]
    if reconciled:
        lines.append(
            "Time-averaged estimate for each day (across that day's hourly snapshots) "
            "vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, "
            "matching the reward day. Low capture = your position decayed between snapshots "
            "(competition joining the best price, prices moving away, fills)."
        )
        lines.append("")
        lines.append("| Day | Estimated | Recorded | Captured |")
        lines.append("|---|---:|---:|---:|")
        for day in reversed(reconciled):
            est = est_days[day]["total"]
            act = by_day[day]
            pct = f"{act / est * 100:.0f}%" if est else "—"
            lines.append(f"| {day} | ~{_usd(est)} | {_usd(act)} | {pct} |")
        lines.append("")
        latest = reconciled[-1]
        gaps = []
        for m, est in est_days[latest]["per_market"].items():
            act = actual_by_day_market.get(latest, {}).get(m, 0.0)
            gaps.append((est - act, m, est, act))
        gaps.sort(reverse=True)
        if gaps and gaps[0][0] > 0.5:
            worst = ", ".join(
                f"`{m}` (est ~{_usd(e)} → got {_usd(a)})" for _, m, e, a in gaps[:3]
            )
            lines.append(f"Biggest gaps on {latest}: {worst}")
            lines.append("")
    else:
        lines.append(
            "_Collecting estimate history (started 2026-07-18). This comparison fills in "
            "once Polymarket posts results for a day with estimate coverage — about two days._"
        )
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
            n = c.get("event_n") or 1
            pool_cell = f"{_usd(c['pool'])} ÷ {n}" if n > 1 else _usd(c["pool"])
            lines.append(
                f"| `{c['market']}` | {pool_cell} | {c['df']:.2f} | {c['target']:,.0f} "
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
    lines.append("| Checked (ET) | Result | Rows | Total |")
    lines.append("|---|---|---:|---:|")
    for b in reversed(beats[-10:]):
        icon = "✅" if b["result"] == "ok" else "❌"
        lines.append(f"| {_et_str(b['checked_at_utc'])} | {icon} {b['result']} | {b['reward_rows']} | ${b['total_usd']} |")
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
        pol_slugs: list[str] = []
        event_sizes: dict[str, int] = {}
        try:
            pol_slugs, event_sizes = fetch_politics_events()
        except Exception as e:  # noqa: BLE001 — proration then falls back to 1
            print(f"politics events fetch failed: {type(e).__name__}: {e}", file=sys.stderr)
        try:
            live_orders = fetch_live_orders(key_id, secret_key, event_sizes)
            write_live_csv(live_orders)
            append_estimates(live_orders)
        except Exception as e:  # noqa: BLE001 — live view is informational only
            live_error = f"{type(e).__name__}: {e}"
        try:
            my_markets = {o["market"] for o in live_orders or [] if o["market"]}
            opportunities = fetch_opportunities(my_markets, pol_slugs, event_sizes)
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
