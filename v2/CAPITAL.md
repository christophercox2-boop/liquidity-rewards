# Capital vs earnings — what it takes to meet a goal

Written 2026-08-18 evening. Data used: live monitor state saved 4:03 PM
ET today (touch prices, program terms), today's 3:09 PM ET order table
(1,356 resting orders), book ladders from the last committed snapshot
(Aug 16 — flagged wherever it matters), and published payouts through
Aug 16. All arithmetic uses the v2 scoring code, queue-aware.

## The short answer

**Capital is not the main constraint. Placement is.** Near the touch, a
few dollars buys most of a side's score: today's single best example is
3 shares at 76¢ — $2.28 at risk — earning an estimated $6.25/day. What
limits income is the size of the pools, the other bots competing for the
same front spots, the exchange paying less than the formula on very deep
sides, and fills (a fill can cost more in one moment than the order earns
in weeks).

Goal → capital, for well-placed near-touch orders against today's board
(1.0's own orders counted as competition, so this is what NEW money
faces):

| goal | formula says | realistic capital, after calibration |
|---|---|---|
| $50/day | ~$100 | **$150–$400** |
| $100/day | ~$400 | **$500–$1,200** |
| $150/day | ~$1,200 | **$1,500–$3,000** |
| $250/day | — | fighting for the whole board (see ceiling below) |

The calibration: the formula curve below assumes competitors freeze and
every window share pays as written. Neither is true — daily
estimate-vs-paid has run 0.27x to 1.22x (usually within ~10%, recent
days ~0.8x), and only about half the board's sides were measurable with
the stale ladders (the half that moved is also the half the owner's
low-volatility style avoids). Treat the right-hand column as planning
bands, not promises.

**Board ceiling with today's pools: $5,550/day across 89 tracked
events.** That is everything, for everyone, at 100% share of every side
— the theoretical maximum the whole game currently pays per day.

## The verified anchors

- The whole 1.0 book right now: **$6,950 at risk → estimated $247/day**.
  Most of that capital is 1¢/99¢ qualifier walls; the near-touch orders
  that drive the estimate are a small fraction of it.
- Actually paid: **$274.92** (Aug 14), **$1,352.63** (Aug 15, the
  outlier), **$197.03** (Aug 16, still-growing pending bucket that
  covers the days since). Historical run-rate $150–550/day.
- The formula curve (greedy, one tick inside the touch, queue-aware,
  today's pools, only sides whose ladder still matched today's touch —
  53 of 116): $100 → ~$56/day, $250 → ~$83, $500 → ~$108,
  $1,000 → ~$136, $2,000 → ~$171.

Two things surfaced while computing this, both worth remembering:

- The first pass of this analysis used the Aug-17 program terms and got
  a curve ~4x too high — the pool cut had happened in between. Stale
  terms silently poisoning arithmetic is exactly the failure REBUILD.md
  describes, and it cost this analysis one wrong table before the fresh
  terms caught it.
- 1.0's terms tracker (`prog_terms`) holds **no senate-seats markets at
  all** — its 300-slug politics watch list never included them. Their
  terms exist only in the Aug-17 snapshot. v2's terms store covers
  every market it quotes, by construction.

## The two seats families (2.0's first markets)

Both are $100/day event pools, Target Size 5,000, discount factor 0.2.
Senate splits its pool across 13 markets (~$3.85 per side per day at
100% share), House across 12 (~$4.17).

**Are they earning today?** Senate: yes, modestly — paid $6.15 on Aug 16
(down from $10–18/day in early August), with 40 small orders resting
(~$135 at risk, est $5.14/day). House: essentially no — **$0.00 on Aug
15 and $0.27 on Aug 16** despite 22 resting orders that score on paper
(est $1.21/day). So the owner's instinct is right about House and close
about Senate.

**The House gap matters beyond House.** House-seat sides hold 14–160x
their Target Size, and 1.0's own reconciliation found the formula
overestimates worst exactly there (median 2.84x high when depth exceeds
100x target). House paying ~nothing while the formula says $1.21/day is
the most extreme case of that pattern we have. Two caveats before
calling it proven: Aug 15 was the day after the order-shredding
incident (House orders may simply not have been resting), and Aug 16 is
still a growing pending bucket.

**What full coverage would look like** (10 shares, one tick inside, both
sides of every market, on the Aug-16 ladders):

- Senate: ~$26/day by formula for ~$116 at risk across 12 measurable
  markets. The yield concentrates mid-ladder (-48 through -51: $3.4–3.9
  per side per day) — which is also where the price actually moves, so
  fill risk is highest exactly where the formula pays best.
- House: ~$12/day by formula for ~$69 at risk — but see the gap above.
  House is as much an experiment as an earner: rest properly, watch
  what actually pays, and settle whether deep sides really pay below
  formula.

**Recommendation:** give 2.0 a **$200–300 ceiling** for the seats test.
That covers both families' near-touch coverage with room to defend, and
the wings (cheap 3–8¢ markets) carry low fill risk while the mid-ladder
gets sized by the prober's confidence, not by the formula's enthusiasm.
Expected honest outcome: Senate $10–25/day, House unknown until the
payouts answer — measured against `rewards.csv` within two days of each
reward day.

## Fill risk, so it is never forgotten

The formula's favorite spots are the worst fills. A bid one tick inside
the touch of a 45¢ House-seats market earns ~$4/day by formula on $4.40
at risk — and loses tens of cents per share the day the polls move
through it. The wings are the reverse: a 4¢ bid rarely fills, but a 4¢
**ask** is an opening short risking 96¢ a share. The engine prices every
placement as reward minus expected fill cost; this document only priced
the reward half.

## What sharpens this analysis

Once 2.0 runs read-only next to 1.0 it will have live books instead of
two-day-old ladders, its own terms history instead of snapshots, and a
daily estimate-vs-paid record per market. The goal→capital table should
be recomputed from that — this version is built to be replaced.
