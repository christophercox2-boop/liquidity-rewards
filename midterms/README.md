# 2026 House Midterm Prediction Model

A small, self-contained fundamentals model for the November 3, 2026 House
elections. No external dependencies — plain Python 3.

**Current forecast: [FORECAST.md](FORECAST.md)**

## Run it

```bash
python3 midterms/model.py
```

That reads [`inputs_2026.json`](inputs_2026.json), fits both models, runs
50,000 Monte Carlo simulations, prints a summary, and rewrites
[`FORECAST.md`](FORECAST.md).

Override inputs from the command line without editing the file:

```bash
python3 midterms/model.py --approval 43 --generic-ballot 2.5
python3 midterms/model.py --sims 200000 --seed 7
```

## Keeping it fresh

The forecast is only as good as two numbers in `inputs_2026.json`:

| Field | What it is | Where to get it |
|---|---|---|
| `approval` | Presidential approval % | Gallup, Silver Bulletin average |
| `generic_ballot_dem_margin` | Generic ballot, Dem − Rep, in points | RealClearPolling / Silver Bulletin averages |

Update those (and `as_of`), re-run, commit.

## How it works

Two independent models, each contributing half the simulation draws:

- **Model A — midterm referendum.** All 20 midterms since 1946: the
  president's party's seat change regressed on presidential approval and
  seat exposure (how many seats the party holds going in). Captures the
  "midterms are a referendum on the president" regularity. Knows nothing
  about the district map.
- **Model B — generic ballot → seats.** Converts today's generic-ballot
  average into a national popular-vote margin (adding historical final-poll
  error *and* extra drift proportional to time remaining), then maps margin
  to seats with a seats-votes regression fit on the 2002–2022 midterms.
  Captures the map's structural bias, which Model A misses.

Errors are drawn from Student's t distributions (fat tails — 20 and 6
data points do not justify thin ones). Combined P(majority) comes from
mixing both models' draws 50/50.

Historical data lives in [`data/`](data/) as plain CSV: seat changes and
Gallup approval for every midterm 1946–2022, and final generic-ballot
averages vs. actual national House margins 2002–2022. Figures are the
commonly cited values (Gallup, Vital Statistics on Congress, RCP); a
point or two of disagreement between sources doesn't move the forecast
materially.

## Honest limitations

- Pure fundamentals: no district-level polling, candidate quality,
  incumbency, retirements, or the 2025–26 mid-decade redistricting wars.
  The seats-votes curve assumes a map resembling 2002–2022; aggressive
  re-maps shift it in ways this model cannot see.
- 20 elections (Model A) and 6 (Model B) are tiny samples. The wide
  intervals are the honest part of the output — treat the point estimates
  with suspicion and the intervals with respect.
- A probability is not a certainty. 81% favorites lose ~1 time in 5.
