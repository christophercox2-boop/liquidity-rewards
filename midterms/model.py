#!/usr/bin/env python3
"""2026 U.S. House midterm forecast.

Two independent fundamentals models, combined by Monte Carlo simulation:

  Model A ("referendum"): regresses the president's party's House seat
  change in every midterm since 1946 on (a) presidential approval and
  (b) how many seats the party holds going in (exposure).

  Model B ("seats-votes"): takes the current generic-congressional-ballot
  average, adds historical polling error plus time-to-election drift to get
  a national House popular-vote margin, then maps margin to seats with a
  regression fit on the single-member-district era (2002-2022 midterms).

Everything runs on the Python standard library — no numpy required.

Usage:
    python3 midterms/model.py               # reads midterms/inputs_2026.json
    python3 midterms/model.py --approval 43 --generic-ballot 2.0
    python3 midterms/model.py --sims 100000 --seed 7

Output: prints a summary and rewrites midterms/FORECAST.md.
"""

import argparse
import csv
import json
import math
import random
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
ELECTION_DAY = date(2026, 11, 3)
MAJORITY = 218

# ---------------------------------------------------------------------------
# tiny linear-algebra helpers (OLS via normal equations)
# ---------------------------------------------------------------------------

def solve(a, b):
    """Solve a @ x = b by Gaussian elimination with partial pivoting."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(col + 1, n):
            f = m[r][col] / m[col][col]
            for c in range(col, n + 1):
                m[r][c] -= f * m[col][c]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (m[r][n] - sum(m[r][c] * x[c] for c in range(r + 1, n))) / m[r][r]
    return x


def ols(xs, ys):
    """Fit y = b0 + b1*x1 + ... on rows xs (list of predictor tuples).

    Returns (coefs, fitted, residuals, residual_se)."""
    rows = [(1.0,) + tuple(x) for x in xs]
    k = len(rows[0])
    xtx = [[sum(r[i] * r[j] for r in rows) for j in range(k)] for i in range(k)]
    xty = [sum(r[i] * y for r, y in zip(rows, ys)) for i in range(k)]
    coefs = solve(xtx, xty)
    fitted = [sum(c * v for c, v in zip(coefs, r)) for r in rows]
    resid = [y - f for y, f in zip(ys, fitted)]
    dof = len(ys) - k
    se = math.sqrt(sum(e * e for e in resid) / dof)
    return coefs, fitted, resid, se


def loo_rmse(xs, ys):
    """Leave-one-out cross-validated RMSE — an honest error estimate."""
    errs = []
    for i in range(len(ys)):
        xs_i = xs[:i] + xs[i + 1:]
        ys_i = ys[:i] + ys[i + 1:]
        coefs, _, _, _ = ols(xs_i, ys_i)
        pred = coefs[0] + sum(c * v for c, v in zip(coefs[1:], xs[i]))
        errs.append(ys[i] - pred)
    return math.sqrt(sum(e * e for e in errs) / len(errs))


def student_t(rng, df):
    """Sample from Student's t with integer df."""
    chi2 = sum(rng.gauss(0, 1) ** 2 for _ in range(df))
    return rng.gauss(0, 1) / math.sqrt(chi2 / df)


def quantile(sorted_vals, q):
    idx = q * (len(sorted_vals) - 1)
    lo = int(idx)
    hi = min(lo + 1, len(sorted_vals) - 1)
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (idx - lo)


# ---------------------------------------------------------------------------
# data + inputs
# ---------------------------------------------------------------------------

def load_csv(name):
    with open(HERE / "data" / name, newline="") as f:
        return list(csv.DictReader(f))


def load_inputs(args):
    with open(HERE / "inputs_2026.json") as f:
        inp = json.load(f)
    if args.approval is not None:
        inp["approval"] = args.approval
    if args.generic_ballot is not None:
        inp["generic_ballot_dem_margin"] = args.generic_ballot
    if args.map_shift is not None:
        inp["map_shift_dem_seats"] = args.map_shift
    if inp.get("days_to_election") is None:
        inp["days_to_election"] = max((ELECTION_DAY - date.today()).days, 0)
    return inp


# ---------------------------------------------------------------------------
# the two models
# ---------------------------------------------------------------------------

def fit_model_a(history):
    """Seat change of president's party ~ approval + exposure."""
    xs, ys = [], []
    for row in history:
        approval = float(row["approval"]) - 50.0
        exposure = float(row["pp_seats_before"]) - 218.0
        xs.append((approval, exposure))
        ys.append(float(row["pp_seat_change"]))
    coefs, _, _, se = ols(xs, ys)
    cv = loo_rmse(xs, ys)
    return {
        "coefs": coefs,
        "resid_se": se,
        "loo_rmse": cv,
        "df": len(ys) - 3,
        "n": len(ys),
    }


def fit_model_b(gb_history):
    """Polling error stats + seats-votes curve from 2002-2022 midterms."""
    errors = [float(r["actual_dem_margin"]) - float(r["final_poll_dem_margin"])
              for r in gb_history]
    n = len(errors)
    err_mean = sum(errors) / n
    err_sd = math.sqrt(sum((e - err_mean) ** 2 for e in errors) / (n - 1))

    xs = [(float(r["actual_dem_margin"]),) for r in gb_history]
    ys = [float(r["dem_seats_won"]) for r in gb_history]
    coefs, _, _, se = ols(xs, ys)
    return {
        "err_mean": err_mean,
        "err_sd": err_sd,
        "sv_coefs": coefs,       # dem_seats = b0 + b1 * dem_margin
        "sv_se": se,
        "sv_df": len(ys) - 2,
        "n": n,
    }


def simulate(ma, mb, inp, sims, seed):
    rng = random.Random(seed)
    pres_r = inp["president_party"] == "R"
    approval_c = inp["approval"] - 50.0
    exposure = inp["pres_party_seats_now"] - 218.0
    mean_change = (ma["coefs"][0]
                   + ma["coefs"][1] * approval_c
                   + ma["coefs"][2] * exposure)
    scale_a = max(ma["resid_se"], ma["loo_rmse"])

    gb = inp["generic_ballot_dem_margin"]
    days = inp["days_to_election"]
    # Polls this far out are noisier than final averages; historical drift in
    # the generic ballot is roughly proportional to sqrt(time remaining).
    drift_sd = min(0.25 * math.sqrt(days), 4.0)
    b0, b1 = mb["sv_coefs"]

    # Mid-decade redistricting: both models are fit on stable-map eras, so a
    # net map shift (in Dem seats, negative = helps GOP) is applied on top.
    map_mu = inp.get("map_shift_dem_seats", 0.0)
    map_sd = inp.get("map_shift_sd", 0.0)

    total = inp["total_seats"]
    dem_seats_a, dem_seats_b, combined = [], [], []
    for _ in range(sims):
        map_shift = rng.gauss(map_mu, map_sd) if map_sd > 0 else map_mu

        # Model A draw: president's-party seat change with t-distributed error
        change = mean_change + student_t(rng, ma["df"]) * scale_a
        pp_after = inp["pres_party_seats_now"] + change
        dem_a = total - pp_after if pres_r else pp_after
        dem_a = min(max(dem_a + map_shift, 0), total)

        # Model B draw: poll -> vote margin -> seats
        margin = (gb + mb["err_mean"]
                  + student_t(rng, mb["n"] - 1) * mb["err_sd"]
                  + rng.gauss(0, drift_sd))
        dem_b = b0 + b1 * margin + student_t(rng, mb["sv_df"]) * mb["sv_se"]
        dem_b = min(max(dem_b + map_shift, 0), total)

        dem_seats_a.append(dem_a)
        dem_seats_b.append(dem_b)
        combined.append(dem_a if rng.random() < 0.5 else dem_b)

    return dem_seats_a, dem_seats_b, combined, {
        "mean_change": mean_change, "scale_a": scale_a, "drift_sd": drift_sd,
    }


# ---------------------------------------------------------------------------
# reporting
# ---------------------------------------------------------------------------

def summarize(draws):
    s = sorted(draws)
    return {
        "p_dem": sum(1 for d in s if d >= MAJORITY) / len(s),
        "median": quantile(s, 0.5),
        "p10": quantile(s, 0.10),
        "p90": quantile(s, 0.90),
    }


def histogram(draws, lo=175, hi=280, bin_w=5, width=40):
    n_bins = (hi - lo) // bin_w
    bins = {}
    for d in draws:
        b = int(min(max(d, lo), hi - 1) - lo) // bin_w
        bins[b] = bins.get(b, 0) + 1
    peak = max(bins.values())
    lines = []
    for b in range(n_bins):
        n = bins.get(b, 0)
        bar = "#" * round(width * n / peak)
        if b == 0:
            lab = f"<={lo + bin_w - 1}"
        elif b == n_bins - 1:
            lab = f">={hi - bin_w}"
        else:
            lab = f"{lo + b * bin_w}-{lo + (b + 1) * bin_w - 1}"
        pct = 100.0 * n / len(draws)
        marker = " <- 218" if lo + b * bin_w <= MAJORITY < lo + (b + 1) * bin_w else ""
        lines.append(f"{lab:>8} | {bar:<{width}} {pct:4.1f}%{marker}")
    return "\n".join(lines)


def sensitivity_grid(ma, mb, inp, seed, sims=8000):
    """P(Dem majority) across an approval x generic-ballot grid."""
    approvals = [35, 39, 43, 47]
    margins = [0, 3, 6, 9]
    rows = []
    for ap in approvals:
        cells = []
        for gb in margins:
            scenario = dict(inp)
            scenario["approval"] = ap
            scenario["generic_ballot_dem_margin"] = gb
            _, _, comb, _ = simulate(ma, mb, scenario, sims, seed + ap * 100 + gb)
            cells.append(sum(1 for d in comb if d >= MAJORITY) / len(comb))
        rows.append((ap, cells))
    lines = ["| Approval \\ Generic ballot | "
             + " | ".join(f"D+{m}" for m in margins) + " |",
             "|---|" + "---|" * len(margins)]
    for ap, cells in rows:
        mark = " (now)" if ap == round(inp["approval"]) else ""
        lines.append(f"| **{ap}%**{mark} | "
                     + " | ".join(f"{c:.0%}" for c in cells) + " |")
    return "\n".join(lines)


def write_report(path, inp, ma, mb, diag, sa, sb, sc, combined, sims, grid):
    p_dem = sc["p_dem"]
    fav = "Democrats" if p_dem >= 0.5 else "Republicans"
    fav_p = max(p_dem, 1 - p_dem)
    lines = [
        "# 2026 House Midterm Forecast",
        "",
        f"_Generated by `midterms/model.py` on {date.today().isoformat()} — "
        f"{sims:,} simulations. Not investment advice; garbage in, garbage out._",
        "",
        "## Bottom line",
        "",
        f"**{fav} favored to control the House: {fav_p:.0%}.**",
        "",
        f"| | P(Dem majority) | Median Dem seats | 80% interval |",
        f"|---|---|---|---|",
        f"| **Combined** | **{sc['p_dem']:.0%}** | **{sc['median']:.0f}** | "
        f"{sc['p10']:.0f} – {sc['p90']:.0f} |",
        f"| Model A (referendum) | {sa['p_dem']:.0%} | {sa['median']:.0f} | "
        f"{sa['p10']:.0f} – {sa['p90']:.0f} |",
        f"| Model B (seats-votes) | {sb['p_dem']:.0%} | {sb['median']:.0f} | "
        f"{sb['p10']:.0f} – {sb['p90']:.0f} |",
        "",
        "218 seats = majority.",
        "",
        "## Seat distribution (combined)",
        "",
        "```",
        histogram(combined),
        "```",
        "",
        "## What moves the needle",
        "",
        "P(Dem majority) under alternative inputs, everything else held at",
        "current values:",
        "",
        grid,
        "",
        "## Inputs used",
        "",
        f"- Presidential approval ({inp['president']}): **{inp['approval']}%**",
        f"- Generic ballot (Dem − Rep): **{inp['generic_ballot_dem_margin']:+.1f}**",
        f"- Days to election: {inp['days_to_election']} "
        f"(poll-drift σ ±{diag['drift_sd']:.1f} pts)",
        f"- Redistricting shift: **{inp.get('map_shift_dem_seats', 0):+.1f} Dem "
        f"seats** (σ ±{inp.get('map_shift_sd', 0):.1f}) vs the 2022 maps, from "
        "the 2025–26 mid-decade re-maps",
        f"- Current House: {inp['dem_seats_now']} D / "
        f"{inp['total_seats'] - inp['dem_seats_now']} R",
        f"- Inputs as of: {inp.get('as_of', 'n/a')}",
        "",
        "## Model details",
        "",
        "**Model A — midterm referendum (n = 20 midterms, 1946–2022).**",
        "President's-party seat change regressed on approval and seats held:",
        "",
        f"```",
        f"seat_change = {ma['coefs'][0]:+.1f} "
        f"{ma['coefs'][1]:+.2f} x (approval - 50) "
        f"{ma['coefs'][2]:+.2f} x (seats_held - 218)",
        f"```",
        "",
        f"Residual SE {ma['resid_se']:.1f} seats; leave-one-out RMSE "
        f"{ma['loo_rmse']:.1f} seats (used as the simulation scale). "
        f"Point estimate for {inp['election_year']}: "
        f"{diag['mean_change']:+.0f} seats for the president's party.",
        "",
        "**Model B — generic ballot → seats (n = 6 midterms, 2002–2022).**",
        "Final-poll error: mean "
        f"{mb['err_mean']:+.1f}, SD {mb['err_sd']:.1f} pts, plus drift for "
        "time remaining. Seats-votes curve: "
        f"`dem_seats = {mb['sv_coefs'][0]:.1f} + {mb['sv_coefs'][1]:.2f} x "
        f"dem_margin` (residual SE {mb['sv_se']:.1f} seats).",
        "",
        "## Caveats",
        "",
        "- Fundamentals only — no district-level data, candidate quality,",
        "  or incumbency effects.",
        "- Tiny samples (20 and 6 elections). Uncertainty is wide on purpose;",
        "  t-distributed errors give fat tails.",
        "- Mid-decade redistricting enters only as the single net-shift input",
        "  above — a crude summary of a fight still moving through courts and",
        "  legislatures. Revisit `map_shift_dem_seats` as maps settle.",
        "- Update `inputs_2026.json` before relying on any number here",
        "  (`fetch_inputs.py` can do the polling inputs automatically).",
    ]
    path.write_text("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser(description="2026 House midterm forecast")
    ap.add_argument("--approval", type=float, help="presidential approval %%")
    ap.add_argument("--generic-ballot", type=float,
                    help="generic ballot margin, Dem minus Rep")
    ap.add_argument("--map-shift", type=float,
                    help="net redistricting shift in Dem seats (neg = helps GOP)")
    ap.add_argument("--sims", type=int, default=50000)
    ap.add_argument("--seed", type=int, default=2026)
    args = ap.parse_args()

    inp = load_inputs(args)
    ma = fit_model_a(load_csv("midterm_history.csv"))
    mb = fit_model_b(load_csv("generic_ballot_history.csv"))
    a, b, comb, diag = simulate(ma, mb, inp, args.sims, args.seed)
    sa, sb, sc = summarize(a), summarize(b), summarize(comb)
    grid = sensitivity_grid(ma, mb, inp, args.seed)

    report = HERE / "FORECAST.md"
    write_report(report, inp, ma, mb, diag, sa, sb, sc, comb, args.sims, grid)

    fav = "Democrats" if sc["p_dem"] >= 0.5 else "Republicans"
    print(f"P(Democratic House majority): {sc['p_dem']:.1%}  "
          f"({fav} favored)")
    print(f"Median Dem seats: {sc['median']:.0f}  "
          f"(80% interval {sc['p10']:.0f}-{sc['p90']:.0f})")
    print(f"Model A: P(Dem)={sa['p_dem']:.1%} median={sa['median']:.0f} | "
          f"Model B: P(Dem)={sb['p_dem']:.1%} median={sb['median']:.0f}")
    print(f"Report written to {report}")


if __name__ == "__main__":
    main()
