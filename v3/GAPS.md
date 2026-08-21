# What 3.0 does not have yet (and where it still lives)

Owner asked 2026-08-21: "Make a list of other things that are missing
from v1 and v2." Ordered by how much they matter to money. "Covered by"
means the old process still does the job while it runs — those become
real gaps only if 1.0/2.0 are retired.

## From 1.0

1. **WebSocket book stream.** 1.0 streams up to 200 books live; 3.0
   polls REST on a budget, so its books lag minutes where 1.0's lag
   seconds. Matters for join-the-touch timing and estimate freshness.
   Covered by: nothing — 3.0's own gap. Biggest single build-back.
2. **Manual order form.** The map can place a brand-new order by hand;
   3.0's pages only move/cancel existing ones. (Owner taps bypass
   switches on both.)
3. **The prober / evidence model.** Small scouts building a
   probability band per market from what fills and what sits. 3.0
   currently trusts the book plus Silver instead.
4. **Deep-blocks exposure alerts.** The card that lists big resting
   walls and warns when an opposing touch drifts near them. Covered by:
   1.0 still runs the read-only alerts.
5. **Whole-board estimate + STATUS.md.** The phone front page and
   rewards.csv fetch are still 1.0's tracker. 3.0 only measures its own
   book. Covered by: 1.0.
6. **Daily digest push.** The evening summary ntfy. Covered by: 1.0.
7. **The unwind ladder.** Guided position exit with staged take levels;
   3.0's seller is one resting order at break-even-or-better.
8. **Golf and surveyed side categories.** scan_markets discovery.
   Deliberately out of scope for now.

## From 2.0

1. **The seats EV engine.** Fill-probability model, fill-cost, EV-ranked
   placement, calibration pages. 3.0 treats seats markets as ordinary
   reward ground. The Silver model itself is back (2026-08-21) as a
   wrong-side-of-value filter, but the EV machinery is not.
2. **Rewards watcher.** The 5-minute poll that pushes "rewards paid"
   the moment the exchange posts. Covered by: 2.0 still runs it.
3. **The independent high-frequency sampler.** 2.0 measured earnings on
   a clock uncorrelated with its own actions; 3.0 has one accrual with
   a coverage quorum. REBUILD.md says the plain sampler alone reads
   high — worth porting before trusting 3.0's earned-today deeply.
4. **Whole-exchange survey.** The catalogue of every family's terms and
   yields (the "give me more options" tool). Covered by: 2.0.
5. **Negative-risk accounting.** 2.0's ceiling understood that bids
   across all brackets of one event can't all lose; 3.0's ceiling is
   gross per-order.
6. **Order drill-down page.** The per-order window/ladder visual.
7. **Estimate-vs-actual history.** estimates.csv grading each day's
   estimate against payouts. Covered by: the data files keep accruing;
   3.0 just doesn't chart them.

## Environmental (nobody has it)

- GitHub Actions are dead (billing) — Silver race tables on disk froze
  Aug 18; 3.0 now fetches the CDN/sheets live instead, so this mostly
  matters for the archived copies.
- Aug 19-20 reward postings still filling in at the exchange.
