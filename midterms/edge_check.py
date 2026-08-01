#!/usr/bin/env python3
"""Compare YOUR Polymarket House-midterm positions against the model.

Prices every 2026 House market it recognizes off the model's simulated
seat distribution, then lines that up against the market's current price
and your actual exposure (positions + resting orders), and ranks where
the model thinks you are most off base — in dollars, worst first.

Market slugs it can price:
    hrep-rep-2026-11-03 / hrep-dem-2026-11-03      House control
    scc-hrep-rep-2026-11-03-gteNNN (and -dem-)     party wins >= NNN seats

Data sources (each independently falls back to the repo's cached files, so
the script also works fully offline):
    prices     GET gateway /v1/markets/{slug}/book     else data/scan*.json
    positions  GET /v1/portfolio/positions (authed)    else data/probe_positions.json
    orders     GET /v1/orders/open        (authed)     else data/live_orders.csv

Usage:
    python3 midterms/edge_check.py               # live where possible
    python3 midterms/edge_check.py --offline     # cached data only
    python3 midterms/edge_check.py --sims 200000

Output: prints the ranking and rewrites midterms/EDGE.md.
"""

import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = ROOT / "data"

sys.path.insert(0, str(HERE))
import model  # noqa: E402  (the forecast model in this directory)

TOTAL = 435
CONTROL_RE = re.compile(r"^hrep-(rep|dem)-2026-11-03$")
THRESH_RE = re.compile(r"^scc-hrep-(rep|dem)-2026-11-03-gte(\d+)$")
UNPRICEABLE_HINT = "hrep"  # House-ish markets we hold but can't price (turnout etc.)


# ---------------------------------------------------------------------------
# model side: P(Yes) for a slug, from the simulated Dem-seat draws
# ---------------------------------------------------------------------------

def slug_prob(slug, draws):
    """P(Yes) under a set of Dem-seat draws, or None if unrecognized."""
    m = CONTROL_RE.match(slug)
    if m:
        thr = 218
        party = m.group(1)
    else:
        m = THRESH_RE.match(slug)
        if not m:
            return None
        party = m.group(1)
        thr = int(m.group(2))
    if party == "rep":
        hits = sum(1 for d in draws if TOTAL - d >= thr)
    else:
        hits = sum(1 for d in draws if d >= thr)
    return hits / len(draws)


def run_model(sims, seed):
    args = SimpleNamespace(approval=None, generic_ballot=None, map_shift=None)
    inp = model.load_inputs(args)
    ma = model.fit_model_a(model.load_csv("midterm_history.csv"))
    mb = model.fit_model_b(model.load_csv("generic_ballot_history.csv"))
    a, b, comb, _ = model.simulate(ma, mb, inp, sims, seed)
    return inp, a, b, comb


# ---------------------------------------------------------------------------
# market side: prices, positions, orders (live with cached fallback)
# ---------------------------------------------------------------------------

def live_mid(slug):
    import track_rewards as tr
    book = tr._fetch_book(slug)
    bid = book["bids"][0][0] if book["bids"] else None
    ask = book["asks"][0][0] if book["asks"] else None
    return bid, ask


def cached_prices():
    """slug -> (bid, ask, source) from the newest scan file that has it."""
    out = {}
    for name in ("scan_restore.json", "scan.json"):  # scan.json wins (newer)
        path = DATA / name
        if not path.exists():
            continue
        try:
            doc = json.loads(path.read_text())
        except ValueError:
            continue
        stamp = doc.get("generated", name) if isinstance(doc, dict) else name
        for r in (doc.get("results") if isinstance(doc, dict) else doc) or []:
            slug = r.get("market")
            if slug and (r.get("best_bid") or r.get("best_ask")):
                out[slug] = (r.get("best_bid"), r.get("best_ask"), str(stamp))
    return out


def get_prices(slugs, offline):
    cached = cached_prices()
    prices = {}
    for slug in slugs:
        if not offline:
            try:
                bid, ask = live_mid(slug)
                prices[slug] = (bid, ask, "live")
                continue
            except Exception:
                pass
        if slug in cached:
            prices[slug] = cached[slug]
    return prices


def get_positions(offline):
    """slug -> position dict (netPositionDecimal etc.)."""
    if not offline:
        try:
            import os
            import requests
            import track_rewards as tr
            key, sec = os.environ["POLYMARKET_KEY_ID"], os.environ["POLYMARKET_SECRET_KEY"]
            path, out, cursor = "/v1/portfolio/positions", {}, None
            for _ in range(20):
                params = {"limit": 100, **({"cursor": cursor} if cursor else {})}
                r = requests.get(tr.TRADE_API + path, params=params, timeout=20,
                                 headers=tr.auth_headers(key, sec, "GET", path))
                r.raise_for_status()
                j = r.json()
                out.update(j.get("positions") or {})
                cursor = j.get("nextCursor")
                if j.get("eof") or not cursor:
                    break
            return out, "live"
        except Exception:
            pass
    probe = DATA / "probe_positions.json"
    if probe.exists():
        return json.loads(probe.read_text()), f"cached {probe.name}"
    return {}, "none"


def get_orders(offline):
    """List of {market, side, price, size} resting orders."""
    if not offline:
        try:
            import os
            import requests
            import track_rewards as tr
            key, sec = os.environ["POLYMARKET_KEY_ID"], os.environ["POLYMARKET_SECRET_KEY"]
            path = "/v1/orders/open"
            r = requests.get(tr.TRADE_API + path, timeout=20,
                             headers=tr.auth_headers(key, sec, "GET", path))
            r.raise_for_status()
            orders = []
            for o in r.json().get("orders") or []:
                size = model_num(o.get("qtyRemaining")) or model_num(o.get("size"))
                orders.append({
                    "market": o.get("marketSlug", ""),
                    "side": "BUY" if "BUY" in str(o.get("side", "")) else "SELL",
                    "price": model_num((o.get("price") or {}).get("value")
                                       if isinstance(o.get("price"), dict) else o.get("price")),
                    "size": size,
                })
            return orders, "live"
        except Exception:
            pass
    lo = DATA / "live_orders.csv"
    if lo.exists():
        # The CSV is an appended log — the same resting order shows up once
        # per tracker run, so collapse to unique (market, side, price, size).
        seen, rows = set(), []
        with open(lo, newline="") as f:
            for r in csv.DictReader(f):
                key = (r["market"], r["side"], r["price"], r["size"])
                if key in seen:
                    continue
                seen.add(key)
                rows.append({"market": r["market"], "side": r["side"],
                             "price": float(r["price"]), "size": float(r["size"])})
        return rows, f"cached {lo.name} (deduped)"
    return [], "none"


def model_num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------------------
# the comparison
# ---------------------------------------------------------------------------

def analyze(offline, sims, seed):
    inp, dr_a, dr_b, draws = run_model(sims, seed)

    positions, pos_src = get_positions(offline)
    orders, ord_src = get_orders(offline)

    held = {s: p for s, p in positions.items()
            if abs(model_num(p.get("netPositionDecimal")) or 0) >= 0.01}
    my_slugs = set(held) | {o["market"] for o in orders}
    priceable = sorted(
        {s for s in set(positions) | {o["market"] for o in orders}
         if slug_prob(s, draws[:100]) is not None},
        key=lambda s: (len(s), s))
    unpriceable_held = sorted(s for s in my_slugs
                              if UNPRICEABLE_HINT in s and slug_prob(s, draws[:100]) is None)

    prices = get_prices(priceable, offline)

    rows = []
    for slug in priceable:
        p_model = slug_prob(slug, draws)
        p_a = slug_prob(slug, dr_a)
        p_b = slug_prob(slug, dr_b)
        bid, ask, src = prices.get(slug, (None, None, "no price"))
        mid = (bid + ask) / 2 if bid and ask else bid or ask
        pos = held.get(slug)
        net = model_num(pos.get("netPositionDecimal")) if pos else 0.0
        avg = model_num((pos.get("avgPx") or {}).get("value")) if pos else None
        edge_share = None if mid is None else p_model - mid
        dollar = None
        if mid is not None and net:
            dollar = net * (p_model - mid)  # net<0 (long No) flips the sign itself
        rows.append({
            "slug": slug, "p_model": p_model, "p_a": p_a, "p_b": p_b,
            "bid": bid, "ask": ask, "mid": mid, "price_src": src,
            "net": net or 0.0, "avg": avg,
            "edge_share": edge_share, "dollar": dollar,
        })

    order_rows = []
    for o in orders:
        p_model = slug_prob(o["market"], draws)
        if p_model is None or o["price"] is None or not o.get("size"):
            continue
        ev = (p_model - o["price"]) if o["side"] == "BUY" else (o["price"] - p_model)
        order_rows.append({**o, "p_model": p_model, "ev_share": ev,
                           "ev_total": ev * o["size"]})
    order_rows.sort(key=lambda r: r["ev_total"])

    return {
        "inp": inp, "rows": rows, "orders": order_rows,
        "pos_src": pos_src, "ord_src": ord_src,
        "unpriceable": unpriceable_held,
    }


# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

def fmt_pct(x):
    return "—" if x is None else f"{x:.0%}"


def fmt_px(x):
    return "—" if x is None else f"{x:.2f}"


def stance(net):
    if net > 0:
        return f"long {net:g} Yes"
    return f"long {-net:g} No"


def write_report(res):
    rows = res["rows"]
    held_rows = sorted((r for r in rows if r["net"]),
                       key=lambda r: (r["dollar"] is None, r["dollar"] or 0))
    lines = [
        "# Your positions vs. the model",
        "",
        f"_Generated by `midterms/edge_check.py` on {date.today().isoformat()}. "
        f"Positions: {res['pos_src']}; orders: {res['ord_src']}. "
        "Positive $ edge = the model agrees with holding; negative = the model "
        "would sell at today's price. Not investment advice._",
        "",
        "## Where the model thinks you're most off base",
        "",
        "Ranked worst-first by model-implied $ edge of holding versus selling",
        "at the current market price:",
        "",
        "| Market | Your stance (avg px) | Mkt mid | Model P(Yes) | $ edge |",
        "|---|---|---|---|---|",
    ]
    for r in held_rows:
        avg = f" @ {fmt_px(r['avg'])}" if r["avg"] is not None else ""
        dollar = "—" if r["dollar"] is None else f"{r['dollar']:+.2f}"
        lines.append(f"| `{r['slug']}` | {stance(r['net'])}{avg} | "
                     f"{fmt_px(r['mid'])} | {fmt_pct(r['p_model'])} | {dollar} |")
    worst = [r for r in held_rows if (r["dollar"] or 0) < -0.5]
    if worst:
        lines += ["", "Reading the worst offenders:", ""]
        for r in worst[:4]:
            side = "Yes" if r["net"] > 0 else "No"
            want = "lower" if r["net"] > 0 else "higher"
            lines.append(
                f"- **`{r['slug']}`** — you hold {abs(r['net']):g} {side} shares "
                f"with the market at {fmt_px(r['mid'])}, but the model puts "
                f"P(Yes) at only {fmt_pct(r['p_model'])}"
                if r["net"] > 0 else
                f"- **`{r['slug']}`** — you hold {abs(r['net']):g} {side} shares "
                f"with the market at {fmt_px(r['mid'])}, but the model puts "
                f"P(Yes) at {fmt_pct(r['p_model'])}, {want} than the market implies"
            )
    if res["orders"]:
        lines += [
            "",
            "## Your resting orders, if they fill",
            "",
            "EV per share = model fair value minus fill price (flipped for",
            "sells). Small negative EV can still be worth it for liquidity",
            "rewards — that judgement is yours; the model only prices the",
            "resolution.",
            "",
            "| Market | Order | Model P(Yes) | EV/share | EV total |",
            "|---|---|---|---|---|",
        ]
        for o in res["orders"]:
            lines.append(f"| `{o['market']}` | {o['side']} {o['size']:g} @ "
                         f"{fmt_px(o['price'])} | {fmt_pct(o['p_model'])} | "
                         f"{o['ev_share']:+.2f} | {o['ev_total']:+.2f} |")
    lines += [
        "",
        "## Full ladder: market vs. model",
        "",
        "All recognized House markets, including ones you don't hold —",
        "positive gap = model says Yes is cheap. Where Model A and Model B",
        "disagree hardest, trust the gap least.",
        "",
        "| Market | Mkt mid | Model P(Yes) | Gap | Model A | Model B | Price src |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        gap = "—" if r["mid"] is None else f"{r['p_model'] - r['mid']:+.0%}"
        lines.append(f"| `{r['slug']}` | {fmt_px(r['mid'])} | "
                     f"{fmt_pct(r['p_model'])} | {gap} | {fmt_pct(r['p_a'])} | "
                     f"{fmt_pct(r['p_b'])} | {r['price_src']} |")
    if res["unpriceable"]:
        lines += ["", "House-related markets you hold that this model cannot "
                      "price (turnout etc.): "
                      + ", ".join(f"`{s}`" for s in res["unpriceable"]) + "."]
    inp = res["inp"]
    lines += [
        "",
        "## Model inputs behind these numbers",
        "",
        f"Approval {inp['approval']}%, generic ballot "
        f"D{inp['generic_ballot_dem_margin']:+.1f}, map shift "
        f"{inp.get('map_shift_dem_seats', 0):+.1f} seats "
        f"(as of: {inp.get('as_of', 'n/a')}). Re-run `model.py` inputs first "
        "if these look stale. The model's seat distribution is wide — "
        "single-market gaps under ~10 points are noise, not signal.",
    ]
    (HERE / "EDGE.md").write_text("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser(description="positions vs. model edge check")
    ap.add_argument("--offline", action="store_true",
                    help="cached repo data only, no network")
    ap.add_argument("--sims", type=int, default=50000)
    ap.add_argument("--seed", type=int, default=2026)
    args = ap.parse_args()

    res = analyze(args.offline, args.sims, args.seed)
    write_report(res)

    held = [r for r in res["rows"] if r["net"] and r["dollar"] is not None]
    held.sort(key=lambda r: r["dollar"])
    print(f"positions: {res['pos_src']} | orders: {res['ord_src']}")
    for r in held:
        print(f"{r['dollar']:+8.2f}$  {r['slug']:40s} {stance(r['net']):>18s}"
              f"  mkt {fmt_px(r['mid'])}  model {fmt_pct(r['p_model'])}")
    print(f"report written to {HERE / 'EDGE.md'}")


if __name__ == "__main__":
    main()
