"""One-shot scan of EVERY politics market: book + reward program, then the
cheapest passive resting order per SIDE that would earn ~$3-5/month.

Capital is what the exchange locks while the order rests or fills:
- BUY at price p: p per contract.
- SELL (short) at price p: the max loss, (1 - p) per contract — so quoting
  high-priced stable markets is cheap (95c ask locks 5c/contract).
- SELL covered by inventory you already hold: nothing new locked.

Candidates per side: join best, 1-2 ticks behind (DF 0.50 keeps 50%/25%
weight), and the deep quote (1c bid / 99c ask) that almost never fills.
Sizes are the smallest that clear the per-market target. Orders that would
cross the spread are never suggested.

Writes PLAN.md (human list) and data/scan.json (everything, for auditing).
Run by .github/workflows/scan.yml — the Actions runner has API access.
"""

from __future__ import annotations

import copy
import datetime as dt
import json
import os
import re
import sys
import time

import requests

import track_rewards as tr

TARGET_EST_DAY = 0.15   # ~$4.50/month per market-side — middle of the $3-5 goal
MIN_EST_DAY = 0.08      # below this a side is listed as "not worth an order"
SIZES = [100, 200, 500, 1000, 2000, 5000, 10000]
DEEP_SIZES = [20000]    # only tried where capital stays tiny (<= 2c of risk)


def fetch_programs(slugs: list[str], key_id: str, secret_key: str) -> dict[str, dict]:
    """Reward program params for many markets, batched (same parsing as the tracker)."""
    progs: dict[str, dict] = {}
    for i in range(0, len(slugs), 40):
        batch = slugs[i:i + 40]
        for host in tr.HOSTS:
            try:
                headers = (tr.auth_headers(key_id, secret_key, "GET", "/v1/incentives")
                           if host == tr.TRADE_API else {})
                r = requests.get(host + "/v1/incentives",
                                 params={"symbols": batch, "pageSize": 100},
                                 headers=headers, timeout=20)
                if r.status_code >= 400:
                    continue
                for p in r.json().get("programs") or []:
                    periods = p.get("timePeriods") or []
                    current = [tp for tp in periods
                               if str(tp.get("status", "")).upper() in ("LIVE", "ACTIVE", "STATUS_LIVE")
                               ] or periods
                    if current:
                        tp = current[-1]
                        progs[p.get("marketSlug", "")] = {
                            "df": tr._num(tp.get("discountFactor")),
                            "target": tr._num(tp.get("targetSize")),
                            "pool": tr._num(tp.get("rewardPool")),
                            "start": tp.get("start"),
                            "end": tp.get("end"),
                        }
                break
            except Exception:  # noqa: BLE001 — try the next host
                continue
        time.sleep(0.05)
    return progs


def my_open_market_slugs(key_id: str, secret_key: str) -> set[str]:
    try:
        path = "/v1/orders/open"
        r = requests.get(tr.TRADE_API + path,
                         headers=tr.auth_headers(key_id, secret_key, "GET", path), timeout=30)
        if r.status_code >= 400:
            return set()
        return {o.get("marketSlug") or "" for o in r.json().get("orders") or []} - {""}
    except Exception:  # noqa: BLE001 — marking is optional
        return set()


def my_positions(key_id: str, secret_key: str) -> dict[str, float]:
    """Net long inventory per market — a covered sell locks no new capital."""
    out: dict[str, float] = {}
    try:
        path = "/v1/portfolio/positions"
        cursor = None
        for _ in range(20):
            params: dict = {"limit": 100}
            if cursor:
                params["cursor"] = cursor
            r = requests.get(tr.TRADE_API + path,
                             headers=tr.auth_headers(key_id, secret_key, "GET", path),
                             params=params, timeout=20)
            if r.status_code >= 400:
                return out
            j = r.json()
            for slug, p in (j.get("positions") or {}).items():
                net = tr._num(p.get("netPosition"))
                if net > 0:
                    out[slug] = net
            cursor = j.get("nextCursor")
            if j.get("eof") or not cursor:
                break
    except Exception:  # noqa: BLE001 — coverage marking is optional
        pass
    return out


_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
           "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}


def _resolution_date(slug: str) -> dt.date | None:
    """Best-effort resolution date from the slug (2026-08-04, 12-31-2026, aug31)."""
    m = re.search(r"(20\d{2})-(\d{2})-(\d{2})", slug)
    if m:
        try:
            return dt.date(int(m[1]), int(m[2]), int(m[3]))
        except ValueError:
            pass
    m = re.search(r"(\d{1,2})-(\d{1,2})-(20\d{2})", slug)
    if m:
        try:
            return dt.date(int(m[3]), int(m[1]), int(m[2]))
        except ValueError:
            pass
    m = re.search(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)(\d{1,2})", slug)
    if m:
        today = dt.date.today()
        try:
            d = dt.date(today.year, _MONTHS[m[1]], int(m[2]))
            return d if d >= today - dt.timedelta(days=45) else d.replace(year=today.year + 1)
        except ValueError:
            pass
    return None


def _risk(slug: str, side: str, pick: dict,
          best_bid: float | None, best_ask: float | None) -> str | None:
    """Why a passive quote here might get sniped — None if nothing stands out."""
    notes = []
    rd = _resolution_date(slug)
    if rd is not None:
        days = (rd - dt.date.today()).days
        if days <= 14:
            notes.append(f"resolves ~{rd.isoformat()} ({max(days, 0)}d)")
    if side == "BUY" and pick["price"] <= 0.02 and best_ask is not None and best_ask <= 0.05:
        notes.append("market priced near 0 — deep bid sits in the exit path (snipe risk)")
    if side == "SELL" and best_bid is not None and best_bid >= 0.95:
        notes.append("near-certain outcome — a resting ask will get lifted")
    return "; ".join(notes) or None


def _merged(book: dict, side: str, price: float, size: float) -> dict:
    """The book as it would look with our order resting at `price`."""
    b = copy.deepcopy(book)
    key = "bids" if side == "BUY" else "asks"
    levels = dict(b.get(key) or [])
    levels[price] = levels.get(price, 0) + size
    b[key] = sorted(levels.items(), key=lambda x: (-x[0] if side == "BUY" else x[0]))
    return b


def _capital(side: str, price: float, size: float, held: float) -> tuple[float, bool]:
    """(locked capital, covered_by_inventory) for a resting order."""
    if side == "BUY":
        return round(price * size, 2), False
    if held >= size:  # SELL_LONG against inventory — nothing new locked
        return 0.0, True
    return round((1.0 - price) * size, 2), False


def evaluate_side(slug: str, book: dict, prog: dict, side: str, held: float = 0.0) -> dict | None:
    """Cheapest passive resting order on ONE side that clears the target."""
    tick = book.get("tick") or 0.01
    bids = book.get("bids") or []
    asks = book.get("asks") or []
    best_bid = bids[0][0] if bids else None
    best_ask = asks[0][0] if asks else None

    # Conservative candidates: stay >= 1 tick behind the touch. Joining the
    # best price is allowed ONLY when that level already holds the full Target
    # Size — a wall you queue behind (price-time priority: you fill last).
    target = prog.get("target") or 0
    prices: list[float] = []
    if side == "BUY":
        prices.append(0.01)  # the deep bid — deepest first
        if best_bid:
            for off in (3, 2, 1):
                p = round(best_bid - off * tick, 4)
                if p >= 0.01:
                    prices.append(p)
            if bids[0][1] >= target > 0:
                prices.append(best_bid)  # queued wall-join
        if best_ask:  # never cross the spread
            prices = [p for p in prices if p <= round(best_ask - tick, 4)]
        deep_ok = lambda p: p <= 0.02  # noqa: E731
    else:
        prices.append(0.99)  # the deep ask — max loss 1c/contract, deepest first
        if best_ask:
            for off in (3, 2, 1):
                p = round(best_ask + off * tick, 4)
                if p <= 0.99:
                    prices.append(p)
            if asks[0][1] >= target > 0:
                prices.append(best_ask)  # queued wall-join
        if best_bid:  # never cross the spread
            prices = [p for p in prices if p >= round(best_bid + tick, 4)]
        deep_ok = lambda p: p >= 0.98  # noqa: E731
    seen: set[float] = set()
    prices = [p for p in prices if not (p in seen or seen.add(p))]

    best = None  # (misses_target, capital, -est) minimized
    for p in prices:
        for q in SIZES + (DEEP_SIZES if deep_ok(p) else []):
            o = {"market": slug, "side": side, "price": p, "size": float(q)}
            tr._score_order(o, _merged(book, side, p, q), prog)
            est = o.get("est_day") or 0.0
            if est < MIN_EST_DAY:
                continue
            cap, covered = _capital(side, p, q, held)
            cand = {"side": side, "price": p, "size": q, "capital": cap, "covered": covered,
                    "est_day": round(est, 3), "share": round((o.get("share") or 0) * 100, 1),
                    "ticks": o.get("ticks")}
            key = (est < TARGET_EST_DAY, cap, -est)
            if best is None or key < best[0]:
                best = (key, cand)
            if est >= TARGET_EST_DAY:
                break  # sizes grow monotonically — first hit is cheapest at this price
    if not best:
        return None
    # What the side yields if you commit big: the same cushioned candidates at
    # the 20,000-contract cap, keeping the DEEPEST price that makes >= 80% of
    # the best — never standing at the touch just to squeeze the last 20%.
    scored_big = []
    for p in prices:  # deepest first by construction
        q = 20000
        o = {"market": slug, "side": side, "price": p, "size": float(q)}
        tr._score_order(o, _merged(book, side, p, q), prog)
        est = o.get("est_day") or 0.0
        cap, covered = _capital(side, p, q, held)
        scored_big.append({"side": side, "price": p, "size": q, "capital": cap,
                           "covered": covered, "est_day": round(est, 3),
                           "share": round((o.get("share") or 0) * 100, 1)})
    mx = None
    peak = max((c["est_day"] for c in scored_big), default=0.0)
    if peak > 0:
        mx = next(c for c in scored_big if c["est_day"] >= 0.8 * peak)
    out = {"market": slug, "side": side, "pick": best[1], "max": mx,
           "side_pool": round(tr._daily_pool(prog) / 2, 2),
           "best_bid": best_bid, "best_ask": best_ask, "held": held,
           "risk": _risk(slug, side, best[1], best_bid, best_ask)}
    if best[1]["est_day"] < TARGET_EST_DAY:
        out["note"] = "below target — best available"
    return out


GOLF_TAGS = ("golf", "pga", "pga-tour", "masters", "liv-golf", "the-open")


def fetch_tag_events(tags: tuple[str, ...]) -> tuple[list[str], dict[str, int]]:
    """Open market slugs + event sizes for arbitrary event tags, with a text
    search fallback when the tags come up empty."""
    slugs: list[str] = []
    sizes: dict[str, int] = {}

    def _take(ev: dict) -> None:
        open_mkts = [m["slug"] for m in ev.get("markets") or []
                     if m.get("slug") and not m.get("closed")]
        for s in open_mkts:
            if s not in sizes:
                slugs.append(s)
            sizes[s] = max(sizes.get(s, 0), len(open_mkts))

    for tag in tags:
        offset = 0
        for _ in range(30):
            r = requests.get(tr.GATEWAY + "/v1/events",
                             params={"tagSlug": tag, "active": "true",
                                     "limit": 100, "offset": offset}, timeout=30)
            if r.status_code >= 400:
                break
            events = r.json().get("events") or []
            for ev in events:
                _take(ev)
            if len(events) < 100:
                break
            offset += 100
        time.sleep(0.05)
    if len(slugs) < 5:  # unknown tag names — fall back to search
        try:
            r = requests.get(tr.GATEWAY + "/v1/search",
                             params={"query": "golf", "limit": 50}, timeout=20)
            if r.status_code < 400:
                for ev in r.json().get("events") or []:
                    _take(ev)
        except Exception:  # noqa: BLE001
            pass
    return slugs, sizes


def evaluate_cheap_yes(slug: str, book: dict, prog: dict) -> dict | None:
    """Golf strategy: the cheapest possible resting YES bid — the one-tick
    price floor (0.1c on fine-tick books) — sized to clear the earnings
    target. Fills are accepted by design: a filled floor bid is a tiny-cost
    lottery ticket, and the reward flow is meant to cover those losses."""
    tick = book.get("tick") or 0.01
    bids = book.get("bids") or []
    asks = book.get("asks") or []
    floor = round(max(tick, 0.001), 4)
    cands = [floor, round(floor + tick, 4)]
    if bids and bids[0][0] > floor + tick:
        cands.append(round(bids[0][0] - tick, 4))  # 1 behind best when best is higher
    if asks:
        cands = [p for p in cands if p <= round(asks[0][0] - tick, 4)]
    cands = [p for p in dict.fromkeys(cands) if p <= 0.02]  # cheap YES only
    best = None
    for p in cands:  # cheapest first
        for q in SIZES + DEEP_SIZES:
            o = {"market": slug, "side": "BUY", "price": p, "size": float(q)}
            tr._score_order(o, _merged(book, "BUY", p, q), prog)
            est = o.get("est_day") or 0.0
            if est < MIN_EST_DAY:
                continue
            cand = {"side": "BUY", "price": p, "size": q, "capital": round(p * q, 2),
                    "covered": False, "est_day": round(est, 3),
                    "share": round((o.get("share") or 0) * 100, 1)}
            key = (est < TARGET_EST_DAY, cand["capital"], -est)
            if best is None or key < best[0]:
                best = (key, cand)
            if est >= TARGET_EST_DAY:
                break
    if not best:
        return None
    p = best[1]["price"]
    o = {"market": slug, "side": "BUY", "price": p, "size": 20000.0}
    tr._score_order(o, _merged(book, "BUY", p, 20000), prog)
    est = o.get("est_day") or 0.0
    mx = {"side": "BUY", "price": p, "size": 20000, "capital": round(p * 20000, 2),
          "covered": False, "est_day": round(est, 3),
          "share": round((o.get("share") or 0) * 100, 1)} if est > 0 else None
    rd = _resolution_date(slug)
    return {"market": slug, "side": "BUY", "pick": best[1], "max": mx,
            "side_pool": round(tr._daily_pool(prog) / 2, 2),
            "best_bid": bids[0][0] if bids else None,
            "best_ask": asks[0][0] if asks else None, "held": 0,
            "risk": None,  # fills are the accepted cost of this strategy
            "note": f"resolves ~{rd.isoformat()}" if rd else None,
            "prog": {k: prog.get(k) for k in ("df", "target", "pool", "event_n")}}


def golf_main() -> None:
    key_id = os.environ.get("POLYMARKET_KEY_ID", "").strip()
    secret_key = os.environ.get("POLYMARKET_SECRET_KEY", "").strip()
    slugs, event_sizes = fetch_tag_events(GOLF_TAGS)
    progs = fetch_programs(sorted(slugs), key_id, secret_key)
    mine = my_open_market_slugs(key_id, secret_key) if key_id else set()
    print(f"golf: {len(slugs)} markets found, {len(progs)} with programs, {len(mine)} already quoted")

    results, no_pool = [], 0
    for slug in sorted(progs):
        prog = dict(progs[slug])
        if not prog.get("pool"):
            no_pool += 1
            continue
        prog["event_n"] = max(event_sizes.get(slug, 1), 1)
        try:
            book = tr._fetch_book(slug)
        except Exception:  # noqa: BLE001
            continue
        r = evaluate_cheap_yes(slug, book, prog)
        if r:
            r["event_n"] = prog["event_n"]
            r["already_in"] = slug in mine
            results.append(r)
        time.sleep(0.05)

    results.sort(key=lambda r: -((r.get("max") or r["pick"])["est_day"]))
    tot = sum(r["pick"]["est_day"] for r in results)
    cap = sum(r["pick"]["capital"] for r in results)
    lines = ["# Golf plan — cheap YES bids at the price floor", ""]
    lines.append(f"_{len(slugs)} golf markets found; {len(progs)} carry reward programs "
                 f"({no_pool} without pools); {len(results)} placeable. Generated {tr._et_str()}._")
    lines.append("")
    if results:
        lines.append(f"**Everything below:** ~${tot:,.2f}/day for ~${cap:,.0f} at risk if every bid filled.")
        lines.append("")
        lines.append("| # | Market | @ | Size | At risk | Est $/day | Share | Note |")
        lines.append("|--:|---|--:|--:|--:|--:|--:|---|")
        for i, r in enumerate(results, 1):
            p = r["pick"]
            lines.append(f"| {i} | `{r['market']}` | {p['price'] * 100:g}¢ | {p['size']:,} "
                         f"| ${p['capital']:,.0f} | ${p['est_day']:.2f} | {p['share']:.0f}% "
                         f"| {('✔ ' if r['already_in'] else '') + (r.get('note') or '')} |")
    else:
        lines.append("_No placeable golf markets this run — either no reward pools on golf "
                     "right now, or no book allows a sub-2¢ resting bid._")
    lines.append("")
    with open("PLAN-GOLF.md", "w") as f:
        f.write("\n".join(lines))
    os.makedirs("data", exist_ok=True)
    with open("data/scan_golf.json", "w") as f:
        json.dump({"generated": tr._et_str(), "results": results}, f, indent=1)
    print(f"PLAN-GOLF.md: {len(results)} placements, ~${tot:,.2f}/day, ${cap:,.0f} max at risk")


def main() -> None:
    key_id = os.environ.get("POLYMARKET_KEY_ID", "").strip()
    secret_key = os.environ.get("POLYMARKET_SECRET_KEY", "").strip()
    slugs, event_sizes = tr.fetch_politics_events()
    race: dict[str, list[str]] = {}
    for s in slugs:
        race.setdefault(s.rsplit("-", 1)[0], []).append(s)
    progs = fetch_programs(sorted(slugs), key_id, secret_key)
    mine = my_open_market_slugs(key_id, secret_key) if key_id else set()
    held = my_positions(key_id, secret_key) if key_id else {}
    print(f"{len(slugs)} politics markets, {len(progs)} with programs, "
          f"{len(mine)} already quoted, inventory in {len(held)}")

    results, no_pick, skipped = [], [], []
    econ_skipped = 0
    for i, slug in enumerate(sorted(progs)):
        prog = progs[slug]
        if not prog.get("pool"):
            continue
        if tr._is_econ(slug):  # no econ-data markets, per standing instruction
            econ_skipped += 1
            continue
        prog = dict(prog)
        prog["event_n"] = max(event_sizes.get(slug, 1), len(race.get(slug.rsplit("-", 1)[0], [])))
        try:
            book = tr._fetch_book(slug)
        except Exception as e:  # noqa: BLE001 — record and continue
            skipped.append({"market": slug, "error": f"{type(e).__name__}: {e}"})
            continue
        got_any = False
        for side in ("BUY", "SELL"):
            r = evaluate_side(slug, book, prog, side, held.get(slug, 0.0))
            if r:
                r["event_n"] = prog["event_n"]
                r["already_in"] = slug in mine
                r["prog"] = {k: prog.get(k) for k in ("df", "target", "pool", "event_n")}
                results.append(r)
                got_any = True
        if not got_any:
            no_pick.append(slug)
        if i % 25 == 0:
            print(f"  scanned {i}...")
        time.sleep(0.05)

    results.sort(key=lambda r: -((r.get("max") or r["pick"])["est_day"]))
    tot_day = sum(r["pick"]["est_day"] for r in results)
    tot_cap = sum(r["pick"]["capital"] for r in results)

    lines = ["# Passive placement plan — every politics market, both sides", ""]
    lines.append(f"_Scanned {len(results)} market-sides with live reward pools "
                 f"({len(skipped)} unreadable books; {econ_skipped} econ-data markets "
                 f"excluded by request). Generated {tr._et_str()}._")
    lines.append("")
    lines.append(f"**If you place everything below:** ~${tot_day:,.2f}/day "
                 f"(~${tot_day * 30:,.0f}/month) for ~${tot_cap:,.0f} of locked capital.")
    lines.append("")
    lines.append("Capital = what the exchange locks: price for bids, max loss (1 − price) "
                 "for shorts, nothing for sells covered by inventory (marked 📦). "
                 "Deep quotes (1¢ bid / 99¢ ask) almost never fill; join/1-2-ticks-back "
                 "keeps 100/50/25% weight under DF 0.50. ✔ = market you already quote.")
    lines.append("")
    lines.append("Sorted by what the side could pay **at full size** (a 20,000-contract "
                 "order — the placement cap); the Entry columns are the smallest order "
                 "that clears the monthly target.")
    lines.append("")
    lines.append("| # | Market | Side | Entry @ | Size | Cap. | Est $/day "
                 "| Full-size $/day | Full-size cap. | Note |")
    lines.append("|--:|---|---|--:|--:|--:|--:|--:|--:|---|")
    risky = sum(1 for r in results if r.get("risk"))
    if risky:
        lines.append(f"⚠ {risky} rows are flagged risky (soon-to-resolve market, or a deep "
                     f"quote that's actually fillable) — they're listed but excluded from "
                     f"the dashboard's Select-all; pick them only deliberately.")
        lines.append("")
    for i, r in enumerate(results, 1):
        p = r["pick"]
        note = ("✔ " if r["already_in"] else "") + ("📦 covered " if p.get("covered") else "") \
               + (f"⚠ {r['risk']} " if r.get("risk") else "") + (r.get("note") or "")
        mx = r.get("max") or p
        lines.append(f"| {i} | `{r['market']}` | {r['side']} | {p['price'] * 100:g}¢ "
                     f"| {p['size']:,} | ${p['capital']:,.0f} | ${p['est_day']:.2f} "
                     f"| ${mx['est_day']:.2f} | ${mx['capital']:,.0f} | {note} |")
    if no_pick:
        lines.append("")
        lines.append(f"**Not worth an order on either side ({len(no_pick)}):** "
                     + ", ".join(f"`{m}`" for m in no_pick))
    if skipped:
        lines.append("")
        lines.append(f"_Unreadable books ({len(skipped)}): "
                     + ", ".join(f"`{s['market']}`" for s in skipped[:15]) + "_")
    lines.append("")

    with open("PLAN.md", "w") as f:
        f.write("\n".join(lines))
    os.makedirs("data", exist_ok=True)
    with open("data/scan.json", "w") as f:
        json.dump({"generated": tr._et_str(), "results": results,
                   "no_pick": no_pick, "skipped": skipped}, f, indent=1)
    print(f"PLAN.md: {len(results)} placements, ~${tot_day:,.2f}/day for ~${tot_cap:,.0f} locked")


if __name__ == "__main__":
    sys.exit(golf_main() if os.environ.get("SCAN_PLAN") == "golf" else main())
