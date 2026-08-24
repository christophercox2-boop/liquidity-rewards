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

## P7 — the owner's replacement orders will stop being sold over
*Written 2026-08-24, before the fix ships.*

**Claim.** After the adoption change, no market will ever again show
BOTH an owner order reducing a position AND an engine `sell` order,
where the two together offer more shares than the position holds.

**Why.** `api.open_orders()` sets `manual=True` from the exchange's
`manualOrderIndicator`. `Family.adoptable()` skipped exactly those
orders, so they never entered `self.orders` — and the cover math in
`_sell()` counts only orders it can see (`purpose in ("sell",
"manual")`). A hand-placed replacement was therefore invisible: the
engine read the position as bare and rested its own exit on top.
Observed 2026-08-24 in `brisho` — owner cancelled the engine's
SELL 120 @ 5.5c, placed his own, and the engine re-placed
SELL 120 @ 5.46067c, with two more of the same in limbo. Recording
the order (still `purpose="manual"`, still never touched) closes it.

**Falsifier.** Any single market on /map showing a manual reduce-side
order plus an engine `sell` order whose quantities sum above the held
size. One instance falsifies this outright.

**Check.** Read the order list per market for the next seven days.

---

# Graded 2026-08-24

## P1 — WRONG, and by a lot
Predicted Aug-21 would pay **at least $295.90**. It paid **$93.02**
(politics $76.45, college football $16.57). Off by 3.2x.

**What it taught.** I was reading "no PAID rows yet" as "the exchange
has not told us." It had. Aug-20, 21 and 22 have been sitting in
rewards.csv as PENDING rows the whole time — 387, 175 and 238 of them.
PENDING is not "unknown", it is the number, waiting to settle. Aug-20
read $143.85 on Aug-22 and $143.92 today: seven cents in two days.
Pending totals are final for grading purposes.

I spent four days telling the owner these days were "unposted and
blocking grading" when the answer was in a file I write myself. This
is the second time the same mistake has cost real information — the
first was reading five of the exchange's twenty-four order fields.
**Check the file before reporting an absence.**

## P2 — RIGHT
Predicted college football would stay under $100 all-time. It is at
**$99.11** over three paying days. Right, but by $0.89 — call it
provisionally right and re-grade at the end of the week.

## P4 — RIGHT
Predicted NBA would pay under $1/day. NBA has paid **$0.01, once**,
against 121 resting orders and $48.08 of the $50 cap committed.

## The finding that matters more than any of these
The politics estimate is not slightly high, it is **~3.4x** high:

| day | politics estimated | politics paid | ratio |
|-----|-------------------|---------------|-------|
| Aug-20 | — | $110.19 | |
| Aug-21 | $255.22 | $76.45 | 3.3x |
| Aug-22 | $366.17 | $101.14 | 3.6x |

College football over the same window: estimated $47.66, paid $54.33 —
accurate to 14%. So this is not a broken estimator, it is something
specific to politics.

And the direction is worse than the level. Politics paid $181.52 on
Aug-18, $122.97, $110.19, $76.45, $101.14 — roughly halved in five
days — while orders grew and risk went to the $250 cap. **More money
resting, more orders, less earned.**

## P8 — the politics estimate is wrong because the pool is shared
**Claim.** The politics over-estimate comes from the pool divisor, not
from uptime or spread. Markets in the same race share one pool; the
estimator credits each bracket its own share, so a race we hold five
brackets of is counted about five times.

**Why this fits.** College football markets are one-per-pool and its
estimate is accurate. Politics 2028 nomination markets are dozens of
candidates against a single pool, and they are exactly where the
estimate is largest. Aug 20-22: 225 politics markets paid anything,
only 88 paid more than 50c.

**Falsifier.** Group the Aug 20-22 paid rows by race prefix and
compare each race's total against the sum of its brackets' estimates.
If the gap is flat across races rather than proportional to how many
brackets we hold in each, the divisor is not the cause and this is
wrong.

**Check.** Runnable now against rewards.csv and estimates.csv — no
waiting on the exchange.

### P8 — first check, and an admission
Pay per bracket does not collapse as we hold more brackets of a race,
which is what pool-splitting would look like:

| brackets held | races | paid per bracket |
|---------------|-------|------------------|
| 1 | 56 | $0.60 |
| 2 | 39 | $0.97 |
| 3 | 3 | $1.81 |

And the widest: 23 brackets of `ewc-usp-2028-11-07` paid $1.80 each,
12 of `enwc-uspres-nom-rep-2028` paid $3.50 each. Wide races pay MORE
per bracket, not less. If one pool were being counted once per
bracket, this column would fall like 1/N. It rises.

**But that is not the falsifier I wrote.** The stated test needs each
race's ESTIMATE, and estimates.csv only stores a per-family total. I
cannot grade a market or a race against its own prediction, which
means P8 is undecided rather than refuted — and the reason is a hole
in my own record-keeping, not in the exchange's.

The owner asked on 2026-08-23 that estimates stay written down until
the actual numbers come in. I wrote them down per family. Per market
is what makes them testable. That is the next thing to build.

---

## 2026-08-24, later — I was wrong about what we have

The owner asked whether we have per-market estimates or fill data at
all. We have both, and I had just said otherwise.

* **data/fills.csv — 633 fills.** Each one carries the market's
  estimated daily rate AT THE MOMENT WE WERE RESTING THERE, plus our
  fair, the band, the confidence, both sides of the touch, hours
  rested and the order id.
* **data/trades.csv — 2,739 trades**, with realized P/L, placement
  time, hours rested, commission, maker/taker role.
* **data/rewards.csv — 4,108 market-day payout rows** over 51 days.

So the join I said was impossible runs today. 73 market-days have
both our estimate and the exchange's money:

| | market-days | estimated | paid | ratio |
|---|---|---|---|---|
| politics | 55 | $172.56 | $58.18 | 2.97x |
| college football | 18 | $31.27 | $6.59 | 4.74x |
| **all** | **73** | **$203.83** | **$64.77** | **3.15x** |

**Read this carefully — the sample is biased.** fills.csv only
records markets where we were FILLED, which are the markets that
moved. So the honest claim is narrow and still useful: *on the
markets where we got filled, our estimate was about 3x the money.*
Getting filled and over-estimating travel together.

Note college football is 4.74x over here while its FAMILY estimate
for Aug-22 was accurate to 14% ($47.66 est, $54.33 paid). Both are
true — of different samples. The family number averages over the
quiet markets that pay as predicted; this one is the filled tail.

**The actual gap** is narrower than I claimed: we have no stored
estimate for markets we rested in and were NOT filled — the good
ones. data/market_est.csv, deployed today, records exactly those.

## P9 — realized trading P/L is about -$31, not -$3,110
`realized_pnl` in the activity feed is in **cents**, not dollars.

Four trades at one instant on 2026-08-17 in
`ewc-usp-party-2028-11-07-rep` (37, 128, 2 and 183 shares at 39c)
report -108.93, -376.84, -5.89 and -538.75 — exactly -2.944 per
share each. At $2.94/share that is impossible on a 39c contract; at
2.9c/share it is ordinary. Confirmed independently: 400 bought at
41c on Aug-15, 50 sold at 28c the next day, field says -6.37 on 50
= 12.74c/share against a 13c predicted move.

**So: -$31.11 of realized trading loss across 2,739 trades, against
$6,118.30 of rewards paid.** The trading side is roughly flat and
the rewards are close to net profit. I was one report away from
telling the owner we had lost $3,110.

**Unexplained, flagged not resolved.** `scc-hrep-rep-2026-11-03-gte200`
contributes -$1.64 with per-share numbers that need a cost basis
above 100c (bought 1 at 67c, sold 1 at 68c, reported -55.91c). That
only makes sense if the shares arrived through a negative-risk
bracket conversion rather than a purchase. One market, 5% of the
file's total. Do not average it in without understanding it.

**Falsifier for P9.** Any trade whose realized_pnl/shares falls
outside +/-100. All 659 non-zero rows are inside it today.
