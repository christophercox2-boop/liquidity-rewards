#!/usr/bin/env python3
"""Read the touch-size experiment.

Nine scc markets on one programId (same pool, discount factor and Target
Size), each holding exactly ONE scoring order, every order at the best bid so
ticks-from-best is 0 everywhere. Only size varies: 10 / 100 / 1000.

Predictions were fixed before the data arrived:

  flat across arms   the model is right — at the touch, size barely matters,
                     and the estimate's error lies somewhere else entirely
  1 : 10 : 100       size matters roughly linearly, so df^ticks is massively
                     over-weighting whoever holds the touch
  all near zero      holding the touch with one order is worth little however
                     large, and the error is upstream of size

Run after the payout lands (~2 days):  python3 analyse_touch.py
"""
import collections
import csv
import json
import pathlib
import statistics

HERE = pathlib.Path(__file__).parent
DATA = HERE / "data"


def main() -> int:
    setup = json.loads((DATA / "experiment_touch_setup.json").read_text())
    day = setup["taken_at"][:10]
    arms = {m: v["arm"] for m, v in setup["markets"].items()}
    sizes = {m: v["target_size"] for m, v in setup["markets"].items()}

    paid: dict[str, dict[str, float]] = collections.defaultdict(dict)
    for r in csv.DictReader((DATA / "rewards.csv").open()):
        if r["market"] in arms:
            paid[r["date"]][r["market"]] = paid[r["date"]].get(r["market"], 0.0) + float(
                r["reward_usd"])

    days = sorted(d for d in paid if d >= day)
    if not days:
        print(f"set up on {day}; no payout for that day or later yet.")
        print("Payouts lag ~2 days — re-run once rewards.csv reaches", day)
        return 1

    for d in days:
        got = paid[d]
        print(f"\n=== payouts for {d} ===")
        print(f"{'arm':5s} {'size':>5s} {'market':38s} {'paid':>8s} {'$/share':>9s}")
        by_arm: dict[str, list[float]] = collections.defaultdict(list)
        for m in sorted(arms, key=lambda x: (arms[x], x)):
            v = got.get(m)
            if v is None:
                print(f"{arms[m]:5s} {sizes[m]:5d} {m[:38]:38s} {'—':>8s}")
                continue
            by_arm[arms[m]].append(v)
            print(f"{arms[m]:5s} {sizes[m]:5d} {m[:38]:38s} {v:8.3f} {v / sizes[m]:9.5f}")

        print(f"\n{'arm':5s} {'n':>2s} {'median paid':>12s} {'mean':>8s}")
        med = {}
        for arm in ("TINY", "MID", "BIG"):
            g = by_arm.get(arm) or []
            if not g:
                continue
            med[arm] = statistics.median(g)
            print(f"{arm:5s} {len(g):2d} {med[arm]:12.3f} {statistics.mean(g):8.3f}")

        if len(med) == 3 and med["TINY"] > 0:
            r1 = med["MID"] / med["TINY"]
            r2 = med["BIG"] / med["TINY"]
            print(f"\nratios vs TINY:  MID {r1:.2f}x (size 10x)   BIG {r2:.2f}x (size 100x)")
            if r2 < 2:
                print("VERDICT: flat in size — the model's 'touch takes the side' is right,")
                print("         so the estimate's error is NOT about size.")
            elif r2 > 30:
                print("VERDICT: scales with size — df^ticks is over-weighting the touch,")
                print("         and share should be much closer to size-proportional.")
            else:
                print("VERDICT: partial scaling — size matters but sublinearly; neither")
                print("         the pure model nor pure size-proportionality fits.")
        elif med:
            print("\nnot all three arms paid — treat with caution, see per-market rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
