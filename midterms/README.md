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
python3 midterms/model.py --map-shift -5     # bearish redistricting scenario
python3 midterms/model.py --sims 200000 --seed 7
```

## Keeping it fresh

The forecast is driven by three numbers in `inputs_2026.json`:

| Field | What it is | Where to get it |
|---|---|---|
| `approval` | Presidential approval % | Gallup, Silver Bulletin average |
| `generic_ballot_dem_margin` | Generic ballot, Dem − Rep, in points | RealClearPolling / Silver Bulletin averages |
| `map_shift_dem_seats` | Net Dem seat change from the 2025–26 mid-decade re-maps (negative = helps GOP) | Ballotpedia / news redistricting trackers |

**Automatic:** the [`midterm-forecast.yml`](../.github/workflows/midterm-forecast.yml)
workflow refreshes the polling inputs and regenerates `FORECAST.md` every
Tuesday (and whenever anything in `midterms/` is pushed to `main`).
`fetch_inputs.py` pulls recent polls from the VoteHub API and takes a
45-day median; if the fetch fails for any reason it leaves the committed
inputs untouched, so a flaky source can never corrupt the forecast. Test
the parser offline with:

```bash
python3 midterms/fetch_inputs.py --fixture data/votehub_fixture.json --dry-run
```

**Manual:** edit the fields (and `as_of`), re-run, commit. The
redistricting number is the one that always needs a human — court rulings
don't show up in polling averages.

## Your positions vs. the model

```bash
python3 midterms/edge_check.py             # live prices/positions where possible
python3 midterms/edge_check.py --offline   # cached repo data only
```

Prices every House market it recognizes (`hrep-…` control,
`scc-hrep-…-gteNNN` seat thresholds) straight off the model's simulated
seat distribution, matches that against the market price and your actual
Polymarket positions and resting orders, and writes **[EDGE.md](EDGE.md)**
ranking where the model thinks you're most off base — in dollars, worst
first. Live fetching reuses the tracker's API auth (same
`POLYMARKET_KEY_ID` / `POLYMARKET_SECRET_KEY` env vars); anything it can't
fetch falls back to the repo's cached `data/` files. The weekly workflow
refreshes EDGE.md too.

Grain of salt: where Model A and Model B disagree hardest (the mid-ladder
thresholds), the gap column is more model uncertainty than market
inefficiency — EDGE.md prints both models per market so you can see it.

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

On top of both models, each simulation draws a **redistricting shift**
(`map_shift_dem_seats` ± `map_shift_sd`): both models are fit on
stable-map eras, and the 2025–26 mid-decade re-map fight (Texas,
California, Missouri, North Carolina, Ohio, Utah, …) moves seats in a way
no historical regression can see. The default (net R+3, σ 2) reflects the
state of play as of mid-2026 — revisit it as court rulings land.

Errors are drawn from Student's t distributions (fat tails — 20 and 6
data points do not justify thin ones). Combined P(majority) comes from
mixing both models' draws 50/50. The report also includes a sensitivity
grid showing P(Dem majority) across approval × generic-ballot scenarios,
so you can see instantly what a polling move does to the bottom line.

Historical data lives in [`data/`](data/) as plain CSV: seat changes and
Gallup approval for every midterm 1946–2022, and final generic-ballot
averages vs. actual national House margins 2002–2022. Figures are the
commonly cited values (Gallup, Vital Statistics on Congress, RCP); a
point or two of disagreement between sources doesn't move the forecast
materially.

## Honest limitations

- Pure fundamentals: no district-level polling, candidate quality,
  incumbency, or retirements. Redistricting enters only as one net-shift
  number — a crude summary of dozens of maps and lawsuits still in motion.
- 20 elections (Model A) and 6 (Model B) are tiny samples. The wide
  intervals are the honest part of the output — treat the point estimates
  with suspicion and the intervals with respect.
- A probability is not a certainty. 81% favorites lose ~1 time in 5.
