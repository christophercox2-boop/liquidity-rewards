# Predictions

Owner, 2026-08-23: "We want verifiable and testable predictions and we
want to keep getting closer to the goal of stable and high earnings."

Every claim here is falsifiable, dated, and resolved against the
exchange's own data — `data/rewards.csv` for payouts, `data/trades.csv`
for executions. A prediction that was wrong stays on the page with what
it taught. Nothing is quietly deleted.

State when these were made: politics est $192/day (meter $267/day),
cfb est $228/day (meter $69/day), NBA est $0.30/day (meter $0.08/day).

---

## OPEN

### P1 — Aug-21 pays at least its estimate
**Claim:** when Aug-21 posts, paid ≥ $295.90.
**Why:** the estimate accrues only while books are fresh, and 17.7 of
that day's 24 hours went unmeasured. The book rested through the gap
and the exchange pays for resting, not for our measuring.
**Falsified if:** paid < $295.90.
**Resolves:** when Aug-21 posts (already 3 days late).

### P2 — cfb's estimate is inflated by the own-the-side claim
**Claim:** cfb's Aug-23 payout comes in under $100, against a claimed
$228/day.
**Why:** $232.65/day of cfb's $261.43/day claim comes from 116 orders
that each own >50% of their side. Owning a side only pays if the pool
is real; the independent meter says $69/day, a 3.3x gap. One of the two
is wrong and the payout decides which.
**Falsified if:** cfb Aug-23 pays ≥ $100.
**Resolves:** when Aug-23 posts.

### P3 — the fair cap stops junk buys
**Status 2026-08-23 20:25Z:** 2 breaches already, both explained and
one now fixed. cfb 0 of 130 fills past fair; NBA 0 of 1; politics 2 of
171 after the cap deployed — jdvan BUY 1@57c against a fair the owner
had *just* set (the sweep had not reached the order; fixed by the
priority sweep), and ne-dem BUY 1@8c on a 4.2c fair. Watch whether the
count reaches zero now that owner-set fairs act promptly.

**Claim:** from Aug-24, zero earn fills on MODELED markets land past
fair (conc > 0).
**Why:** the symmetric hard cap refuses those prices outright.
**Falsified if:** any modeled-market earn fill shows conc > 0.005.
**Resolves:** daily from the fills journal.
**Note:** unmodeled markets are excluded — they have no fair line, which
is exactly why the owner-set fair control exists.

### P4 — NBA earns almost nothing for its capital
**Claim:** NBA pays under $1.00 on Aug-24 against ~$47 of capital.
**Why:** joining 400-900k share walls buys a ~0.02% slice of each pool.
This is the accepted price of the stability the owner asked for; the
number is written down so the trade-off is judged on data.
**Falsified if:** NBA pays ≥ $1.00.
**Resolves:** when Aug-24 posts.

### P5 — the exchange will name why orders vanish — **WRONG**
**Claimed:** `cancel_reason` would explain the silent cancels.
**Settled 2026-08-24:** all 2,626 rows read
`UNSOLICITED_CXL_REASON_UNDEFINED`. The field exists and is useless
here, for a reason I should have seen before predicting: the activity
feed carries TRADES. An order cancelled without trading never
produces a trade row, so the trade feed structurally cannot explain a
silent cancel. The field only ever describes orders that DID trade.
**Taught:** check that a data source can contain the answer before
predicting it will. The next probe is the ORDER endpoint, not the
activity feed — the order object carries `state`, so a query over
orders (not activities) is where a cancelled order's fate lives.

---

### P6 — resting is paid twice, taking is taxed  *(new, 2026-08-24)*
**Claim:** over the next week the maker rebate stays near -47 bps of
passive notional and taker fees near +166 bps, so the EV model
understates resting and understates the cost of a dump.
**Why:** measured over 2,626 executions and $7,250 of notional since
Aug-14 — passive trades earned $30.01, the 63 taker dumps paid $14.33.
**Falsified if:** either rate moves more than 20 bps from those.
**Resolves:** Aug-31, from data/trades.csv.

## RESOLVED

### R1 — "the walls are what score" (2026-08-21) — WRONG, and disproven
A group chat claimed the exchange scores from declared best bid/ask
rather than the raw touch. Checked against the reward docs and 185
live markets on the Lite feed: 0 divergences. No change made.

### R2 — "the Texas 50-share exit filled and we lost the record"
(2026-08-23) — WRONG. The transaction history shows no such sale; the
order was cancelled. Taught: infer nothing about fills that the
exchange's own record can settle. This is why data/trades.csv exists.
