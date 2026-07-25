"""One-shot scan of EVERY politics market: book + reward program, then the
cheapest passive BUY order that would earn ~$3-5/month in each market.

Strategy per market (capital-efficient, low-touch):
- Prefer LOW-PRICED bids: a deep 1 cent bid costs pennies per contract and
  almost never fills; joining or sitting 1-2 ticks behind the best bid keeps
  50%/25% of full weight under the current 0.50 discount factor.
- Sizes are chosen as the smallest that clears the per-market earnings target.
- Sell-side quoting is out of scope: it needs inventory or full collateral,
  so it is never the cheapest way to reach a few dollars a month.

Writes PLAN.md (human list) and data/scan.json (everything, for auditing).
Run by .github/workflows/scan.yml — the Actions runner has API access.
"""

from __future__ import annotations

import copy
import json
import os
import sys
import time

import requests

import track_rewards as tr

TARGET_EST_DAY = 0.15   # ~$4.50/month per market — the middle of the $3-5 goal
MIN_EST_DAY = 0.08      # below this a market is listed as "not worth an order"
SIZES = [100, 200, 500, 1000, 2000, 5000, 10000]
DEEP_SIZES = [20000]    # only tried at <= 2 cents, where capital stays tiny


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


def _merged_bids(book: dict, price: float, size: float) -> dict:
    """The book as it would look with our order resting at `price`."""
    b = copy.deepcopy(book)
    bids = dict(b.get("bids") or [])
    bids[price] = bids.get(price, 0) + size
    b["bids"] = sorted(bids.items(), key=lambda x: -x[0])
    return b


def evaluate_market(slug: str, book: dict, prog: dict) -> dict:
    """Cheapest passive BUY that clears the target in this market."""
    tick = book.get("tick") or 0.01
    bids = book.get("bids") or []
    asks = book.get("asks") or []
    best_bid = bids[0][0] if bids else None
    best_ask = asks[0][0] if asks else None
    side_pool = tr._daily_pool(prog) / 2

    prices = []
    if best_bid:
        for off in (0, 1, 2):  # join, 1 back, 2 back — DF 0.5 keeps 100/50/25%
            p = round(best_bid - off * tick, 4)
            if p >= 0.01:
                prices.append(p)
    prices.append(0.01)  # the deep bid — near-zero capital and fill risk
    seen: set[float] = set()
    prices = [p for p in prices if not (p in seen or seen.add(p))]
    if best_ask:  # never cross the spread — that's a fill, not a resting order
        prices = [p for p in prices if p <= round(best_ask - tick, 4)]

    best = None  # (meets_target, capital, -est) minimized
    for p in prices:
        for q in SIZES + (DEEP_SIZES if p <= 0.02 else []):
            o = {"market": slug, "side": "BUY", "price": p, "size": float(q)}
            tr._score_order(o, _merged_bids(book, p, q), prog)
            est = o.get("est_day") or 0.0
            if est < MIN_EST_DAY:
                continue
            cand = {"price": p, "size": q, "capital": round(p * q, 2),
                    "est_day": round(est, 3), "share": round((o.get("share") or 0) * 100, 1),
                    "ticks": o.get("ticks")}
            key = (est < TARGET_EST_DAY, cand["capital"], -est)
            if best is None or key < best[0]:
                best = (key, cand)
            if est >= TARGET_EST_DAY:
                break  # sizes grow monotonically — first hit is the cheapest at this price
    out = {"market": slug, "side_pool": round(side_pool, 2),
           "best_bid": best_bid, "best_ask": best_ask,
           "bid_depth": round(sum(q for _, q in bids), 0),
           "pick": best[1] if best else None}
    if best and best[1]["est_day"] < TARGET_EST_DAY:
        out["note"] = "below target — best available"
    return out


def main() -> None:
    key_id = os.environ.get("POLYMARKET_KEY_ID", "").strip()
    secret_key = os.environ.get("POLYMARKET_SECRET_KEY", "").strip()
    slugs, event_sizes = tr.fetch_politics_events()
    race: dict[str, list[str]] = {}
    for s in slugs:
        race.setdefault(s.rsplit("-", 1)[0], []).append(s)
    progs = fetch_programs(sorted(slugs), key_id, secret_key)
    mine = my_open_market_slugs(key_id, secret_key) if key_id else set()
    print(f"{len(slugs)} politics markets, {len(progs)} with programs, {len(mine)} already quoted")

    results, skipped = [], []
    for i, slug in enumerate(sorted(progs)):
        prog = progs[slug]
        if not prog.get("pool"):
            continue
        prog = dict(prog)
        prog["event_n"] = max(event_sizes.get(slug, 1), len(race.get(slug.rsplit("-", 1)[0], [])))
        try:
            book = tr._fetch_book(slug)
        except Exception as e:  # noqa: BLE001 — record and continue
            skipped.append({"market": slug, "error": f"{type(e).__name__}: {e}"})
            continue
        r = evaluate_market(slug, book, prog)
        r["event_n"] = prog["event_n"]
        r["already_in"] = slug in mine
        results.append(r)
        if i % 25 == 0:
            print(f"  scanned {i}...")
        time.sleep(0.05)

    picks = [r for r in results if r.get("pick")]
    picks.sort(key=lambda r: (r["pick"]["est_day"] < TARGET_EST_DAY,
                              -r["pick"]["est_day"] / max(r["pick"]["capital"], 0.01)))
    none_worth = [r for r in results if not r.get("pick")]
    tot_day = sum(r["pick"]["est_day"] for r in picks)
    tot_cap = sum(r["pick"]["capital"] for r in picks)

    lines = ["# Passive placement plan — every politics market", ""]
    lines.append(f"_Scanned {len(results)} markets with live reward pools "
                 f"({len(skipped)} unreadable). Generated {tr._et_str()}._")
    lines.append("")
    lines.append(f"**If you place everything below:** ~${tot_day:,.2f}/day "
                 f"(~${tot_day * 30:,.0f}/month) for ~${tot_cap:,.0f} of resting bid capital.")
    lines.append("")
    lines.append("Every suggestion is a BUY resting below the spread — sized as the "
                 "smallest order that clears ~$0.15/day (≈$4.50/month) in that market, "
                 "preferring cheap prices (a 1¢ bid rarely fills; 1-2 ticks behind best "
                 "keeps 50%/25% weight under DF 0.50). ✔ = you already quote this market.")
    lines.append("")
    lines.append("| # | Market | Buy @ | Size | Capital | Est $/day | ≈$/mo | Share | Note |")
    lines.append("|--:|---|--:|--:|--:|--:|--:|--:|---|")
    for i, r in enumerate(picks, 1):
        p = r["pick"]
        note = ("✔ already in · " if r["already_in"] else "") + (r.get("note") or "")
        lines.append(f"| {i} | `{r['market']}` | {p['price'] * 100:g}¢ | {p['size']:,} "
                     f"| ${p['capital']:,.0f} | ${p['est_day']:.2f} | ${p['est_day'] * 30:,.0f} "
                     f"| {p['share']:.0f}% | {note} |")
    if none_worth:
        lines.append("")
        lines.append(f"**Not worth an order right now ({len(none_worth)}):** even a large bid "
                     f"earns under ${MIN_EST_DAY}/day (crowded side or tiny prorated pool):")
        lines.append("")
        lines.append(", ".join(f"`{r['market']}`" for r in none_worth))
    if skipped:
        lines.append("")
        lines.append(f"_Unreadable books ({len(skipped)}): "
                     + ", ".join(f"`{s['market']}`" for s in skipped[:15]) + "_")
    lines.append("")

    with open("PLAN.md", "w") as f:
        f.write("\n".join(lines))
    os.makedirs("data", exist_ok=True)
    with open("data/scan.json", "w") as f:
        json.dump({"generated": tr._et_str(), "results": results, "skipped": skipped}, f, indent=1)
    print(f"PLAN.md: {len(picks)} placements, ~${tot_day:,.2f}/day for ~${tot_cap:,.0f} capital")


if __name__ == "__main__":
    sys.exit(main())
