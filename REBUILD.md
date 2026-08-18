# Version 2.0 — build brief

Written 2026-08-18, at the end of the 1.0 era, for whoever builds 2.0.

Read `CLAUDE.md` first — it holds the owner's standing preferences and they
do not change. This file is everything else: what the system does, what state
each part is in, what is genuinely broken, and what 2.0 should do differently.

**Treat 1.0 as a first draft.** It works and it earns money, but it was built
fast, under pressure, one patch at a time. There are lazy solutions in it that
a more deliberate pass should replace outright rather than inherit. Where this
document describes how 1.0 does something, that is context, not a
specification to copy.

---

## The business

The owner earns **liquidity rewards** on Polymarket US by resting limit orders
near the best price and not trading. The exchange pays a daily pool to people
who provide liquidity. You collect a share of it for sitting there.

Getting filled is normally a **loss**, not a win — a fill means the market
moved through your order. So the goal is not to trade well. The goal is to
sit in the right markets, at the right prices, in the right size, collect the
pool, and not get hit.

Current scale: roughly **$150–$550 a day**, on a few hundred dollars of
capital at risk. The owner runs this entirely from a phone.

---

## The seven things the system must do

This is the owner's own list of core functionality. Everything else in the
repo is scaffolding around these.

### 1. Enter, exit and modify orders

Place a resting order, cancel it, move it to a new price, change its size.

**Where it stands:** works, and the safety rails around it are sound. Keep the
rails; rebuild the plumbing.

**The one thing that must carry over:** the exchange's modify endpoint is
broken and has been since 2026-08-11. It reports success, cancels your
original order, and never places the replacement. Every order it touched that
day was destroyed. So 2.0 must never call it. To change a price or a size:
place the new order first, confirm it is genuinely resting by checking its
order id and quantity, and only then cancel the old one. If anything fails
before the cancel, the original is still there. If the cancel itself fails you
briefly have two orders, which costs a little size and is far better than
losing your place.

### 2. Qualify a market

Put size on a side that does not currently hold enough to earn.

**Why this exists:** the exchange only pays a side that holds at least the
market's Target Size in total, counting everyone's orders. Below that
threshold, **that entire side pays nothing to anybody**. So on a thin market,
adding size is sometimes the difference between the whole side earning and the
whole side earning zero — and if you are the one who qualifies it, you take
most of what it pays.

**Where it stands:** works, but it is bolted on as a separate loop with its own
approval queue. In 2.0 this should be a decision the earner makes naturally —
"this side is dead, and I can revive it for $X and take most of it" is just
another way of scoring an opportunity.

### 3. See the order book

Bids, asks, sizes, the spread, and where our own orders sit in it.

**Where it stands:** the data is good. There is a live WebSocket feed with a
polling fallback, and books are cached with an age stamp so nothing acts on a
stale one. This part of 1.0 is worth studying before replacing.

**The weak point:** book data lives only in memory. Anyone trying to help the
owner — or any model debugging a problem — cannot see a book without the
dashboard password. A late patch started publishing the best bid and ask into
the saved state file. Do more of that.

### 4. See reward information

For each market: the pool, the Target Size, the discount factor, whether the
program is live.

**Where it stands: recently improved, and this was a real failure.** Until
2026-08-18 the system only recorded a yes/no — does this market have a reward
program. It never stored the terms. So when the exchange cut the standard pool
from about $500 per event to $200, the system had no idea. The owner
discovered it by reading the exchange himself, and the day's income dropped by
more than half with no explanation available from the code.

It now stores pool, Target Size and discount factor per market, timestamped,
and reports changes. **2.0 should treat reward terms as first-class data that
is tracked over time**, not as a flag. A pool change is the single largest
thing that can happen to daily income.

### 5. Estimate what we are earning right now

A live estimate of dollars per day, integrated into a running "earned today"
number.

**Where it stands:** works, and it is the number the owner looks at most. But
be honest about its accuracy. Measured against 23 days of actual payouts, the
estimate has landed anywhere between 0.27× and 1.22× of what was really paid.
Most days it is within about 10%. Some days it is not remotely close.

**What 2.0 should do differently:** show the estimate next to its own track
record. If the system knew that its recent estimates had been running 35%
high, the owner would have known to discount today's number. Right now the
calibration data exists but nothing uses it.

### 6. Collect the published rewards data

Once the exchange publishes what it actually paid, fetch it and commit it to
GitHub so there is a permanent record.

**Where it stands:** works, and it is the most valuable data in the project —
it is the only ground truth. `data/rewards.csv` has a month of daily payouts
per market. Do not lose it, do not restructure it casually, and keep appending
in the same shape.

**Note on plumbing:** this used to run as a GitHub Action. Actions stopped
dispatching on 2026-08-16 for billing reasons and have not run since, so the
monitor now does the fetch itself. Anything 2.0 builds should assume Actions
are unavailable.

### 7. Keep the owner informed, easily

Phone alerts for things that matter, a readable page for everything else.

**Where it stands: the weakest area, and the one with the most churn.** The
alerting had no rate limit at all, so any repeating condition sent one push a
minute. That got fixed on 2026-08-18 with a dedupe, a five-minute ceiling on
total pushes, and a list of alert types that always go through immediately
(fills, money events, reward pool changes). Every push and every suppression
is now logged so the source of a noise problem is findable.

**The deeper problem, which is not fixed:** every control ended up on one page
called `/map`. Order tiles, the order book, a new-order form, the automation
switches, the prober read-out, the earner read-out, a sell-approval queue, a
2028 candidate slate, alerts. It became unreadable, and it became the reason
every new feature had to go on that same page. The owner has explicitly said
he does not want this. **2.0 should have a small number of small pages, each
answering one question.**

---

## The heart of 2.0: probe → earn → sell

The owner wants this built up deliberately, as a model that gathers evidence
and acts on confidence thresholds. It does not need to be perfect. It needs to
reliably place **low-risk — not no-risk — orders that earn at a high and
consistent rate**, and to do it without him.

**The prober** learns what a contract is actually worth. It rests small
scouts, watches what fills, what sits untouched, what gets outbid or
undercut, and maintains a probability band per market. It should be genuinely
evidential: a real trade is strong evidence, an order resting quietly is weak
evidence, and the model should say how sure it is, not just what it thinks.

**The earner** decides where to put money. It should rank opportunities by
income per dollar at risk, consider both sides of every book rather than
assuming the bid, and size according to how sure the prober is.

**The seller** unwinds. Anything that fills gets sold back; anything sitting
idle gets rested as an ask so it earns while it waits. The owner is frequently
"out of a market except for selling what I hold", so the seller must be able
to work in markets that are otherwise closed to automation.

### What 1.0 got wrong here, so 2.0 does not repeat it

**Too many limits, all arguing.** Order size was the minimum of seven
different caps: a per-market dollar cap, a preferred-market cap, an ask cap, a
total budget, a graduated budget, a share ladder, and a confidence multiplier.
When the owner asked why his 2028 markets were not earning, the answer was
that a share ladder nobody had asked for was holding 28 markets to one or two
shares each, while the dollar cap he had actually set was $15 a market. Seven
limits meant nobody could say which one was binding.

**2.0 should have one risk number that binds: total capital at risk across the
whole book.** One ceiling, visible on one line, and every order sized to fit
inside it.

**Confidence was applied twice.** Low confidence both pushed the order further
from the touch and shrank its size. Those compound, and the result was
one-share orders that could never build the track record that would have
raised the confidence. Let confidence decide *where* to rest. Let the risk
ceiling decide *how much*.

**Nothing was compared to the board.** The earner withdrew from 65 of its 66
markets in about ninety seconds on 2026-08-17, because each one had fallen
below 40% of its own recent peak. What had actually happened was that the
whole board fell together — the pool cut. A rule meant to catch "this
particular market got crowded, go somewhere else" fired everywhere at once,
and there was nowhere else. It then locked itself out of all of them for an
hour. Any judgement about a market decaying has to be made relative to how
everything else is doing.

**Queue position was ignored.** When you join a price level that other people
already occupy, their size is ahead of yours. If the scoring window fills
before it reaches you, you earn nothing regardless of how large your order is.
1.0 counted its own size as though it were first in line, which reported 100%
of a window it actually held a seventh of. This was fixed in one place and is
**still wrong in the earner's own scan**, so every estimate it produces is
inflated wherever it joins an occupied level.

**Markets resolving today were treated like any other.** On settlement day the
price moves on the result, not on anything a model knows, and the reward day
ends when the market does. Both are reasons to be somewhere else. The date is
in the market slug and is trivial to check.

---

## Rules that must not break

These are cheap to keep and expensive to rediscover.

**Order intents.** The exchange has four, and two of them rest on the opposite
side from what the name suggests. `BUY_LONG` rests as a bid. `BUY_SHORT` opens
a short and rests as an **ask**. `SELL_LONG` sells stock you hold and rests as
an ask. `SELL_SHORT` buys back a short and rests as a **bid**. Using
`SELL_SHORT` to place an ask puts a bid on the book and has you bidding
against yourself. This has happened.

**An ask is not a cheap bid.** A bid at 5¢ risks 5¢ a share. An ask at 5¢ is
an opening short and risks 95¢ a share — nineteen times as much. Any budget
that prices them the same funds far more risk than it believes. Cost is
`price × qty` for a bid and `(100 − price) × qty` for an ask.

**Post-only on every placement.** The order rests or it is rejected. It can
never cross the spread and fill the instant it arrives.

**Never rest through the other side.** A bid stays below the best ask, an ask
above the best bid.

**Price bounds 0.1¢ to 99.9¢, and a known-market whitelist.** Refuse any
market slug not in the catalogue.

**Authentication plus a custom header on every order-touching endpoint.** The
custom header is the CSRF defence — a cross-origin request cannot set one
without a preflight that is never granted.

**Nothing places an order until the owner switches it on.** 2.0 collapses this
to a single master switch instead of one per loop, but the properties stay:
off by default after any deploy, turning it on takes two deliberate taps,
turning it off takes one, and every flip is logged. Stopping must always be
easier than starting. **The switch should not live on the map page.**

**Secrets** — the exchange key and secret, the dashboard password, the GitHub
token, the alert topic — exist only as encrypted environment variables. Never
in code, never in a commit, never in an output file.

**Scope.** US politics, plus categories the owner has specifically asked about.
Never economics markets. There is a second repository, `wfco223/welcome`,
which other people can see: no tracker data, balances, positions or market
information ever goes there.

---

## The reward formula

Implemented correctly in `track_rewards.py`, in `_score_order` and
`_daily_pool`. This part of 1.0 was expensive to get right and is worth
porting closely rather than rewriting from the docs.

Your score on an order is:

```
discount_factor ^ (ticks away from the best price on your side) × size
```

You are paid your score divided by the sum of all scores inside the window.
The discount factor is usually 0.2 to 0.3, so every tick away from the touch
costs you 70–80% of your score. Distance is punished hard.

Four things gate whether an order earns anything:

1. The side must hold at least Target Size in total across all participants.
   Below that, the side pays nobody.
2. Your order must be inside the window — walk out from the best price
   accumulating size until you reach Target Size; anything beyond that point
   scores zero.
3. The reward program must be live. A closed program pays nothing.
4. Your queue position at your own price level matters, as described above.

**How the pool is divided** — this was contested and is now settled by payout
data. The pool belongs to the **event**, and is split across the event's
markets and then across the two sides:

```
per side per day = pool ÷ number of markets in the event ÷ 2
```

On 2026-08-15, 35 markets paid more than the old convention said their entire
daily pool contained, which disproved it. Do not re-open this.

---

## Status: what is fixed, what is not

### Fixed and working

- Pool division per event, and the historical estimates were recalculated.
- Both sides of the book are considered, not just the bid.
- Order cost is calculated correctly per side.
- Reward terms are stored and changes are reported.
- Alerts are rate-limited, with fills and money events always getting through.
- Positions, book prices and the running build hash are published to the saved
  state file, so they can be read without the dashboard.
- Markets can be marked hands-off, and no automated loop will place there.
- Pages are no longer cacheable, so a phone cannot silently run old code.

### Known broken, not fixed

- **Buying power reads $0** while the info fund shows about $209. Flagged
  twice, never investigated. It may be silently blocking placements.
- **The earner's scan double-counts its own size** at a price level others
  already occupy, so its dollar-per-day estimates are inflated wherever it
  joins a crowded level. Fixed in one helper, not in the scan itself.
- **Reward-term tracking only sees changes from first run forward.** Anything
  that changed before the feature shipped is invisible.
- **Estimate accuracy is not surfaced.** The data to calibrate exists; nothing
  uses it.
- **The map page is overloaded.** Acknowledged, not addressed.

### Environmental

GitHub Actions have not dispatched since 2026-08-16 because of billing. Assume
they are unavailable. Anything that needs to run on a schedule must run inside
the monitor process.

---

## Clearing out the repository

The owner has asked for this explicitly: much of what is in the repo is
unexplained and unused, and 2.0 should delete anything it judges unnecessary.
The current state:

| what | scale | assessment |
|---|---|---|
| GitHub workflows | **65 files** | Most are one-off fixes from a specific afternoon — `finish_ranpau`, `fix_asks`, `test_one_modify`, `diag_body`, and dozens more. Actions do not run any more anyway. Nearly all can go. |
| `data/` | **117 files, 47 MB** | Mixed. `rewards.csv` is irreplaceable ground truth. `books_log.jsonl` alone is 20 MB of raw capture. Many are one-run diagnostic dumps. |
| Markdown docs | **4,195 lines** | `HANDOFF.md` is 1,446 lines and `PLAN.md` is 994 — both accreted rather than being written. `STATUS.md` is the phone-readable front page and must survive. |
| Standalone scripts | `scan_markets.py` 707 lines, `midterms/` ~970 lines, `silver_model.py` 303, `analyse_touch.py` 88 | Investigate before deleting. The Silver forecast model feeds fair values; the midterms model may be dead. |

**Do not delete without checking:** `data/rewards.csv` (the payout record),
`data/estimates.csv` and the state history (estimate accuracy over time),
`STATUS.md`, `CLAUDE.md`, and `track_rewards.py`'s scoring functions.

---

## Running 1.0 and 2.0 at the same time

1.0 keeps running and earning until the owner is satisfied with 2.0.

The problem to solve first is that both would be trading the **same exchange
account**. Two systems on one account will confuse each other: 2.0 will see
1.0's resting orders as other people's liquidity, and a fill from one will
appear in the other's position data with no explanation.

Three ways to handle it, in the order I would try them:

1. **Split by market.** 2.0 gets an exclusive set of markets that 1.0 is
   blocked from. 1.0 already has a hands-off mechanism that does exactly this,
   so the plumbing exists. Cheapest and safest.
2. **Separate credentials**, if the exchange allows a second key with its own
   balance. Cleanest, but unknown whether it is possible.
3. **Cancel everything in 1.0 for a defined test window.** The owner has
   already raised this. It gives 2.0 a clean read but stops all income for the
   duration, so it should be a short, deliberate test rather than the default.

The owner is willing to allocate money to 2.0 separately for real-world
testing. Decide the amount before the first order, and make it the total
capital-at-risk ceiling described above.

---

## Expanding beyond politics

The owner wants to spread the earning base into other futures markets. **This
is not the first priority** — get the core working well on politics first.

Two things to keep in mind while building, so the expansion is not a rewrite:
do not hard-code politics-specific market slug patterns into the core logic,
and keep the "never economics markets" rule, which is a standing preference
rather than a technical limit.

---

## Questions for the owner

1. How much money should 2.0 have for its real-world test?
2. Does the exchange support a second set of API credentials with a separate
   balance? If so, that is the cleanest way to run both versions at once.
3. Which markets, if any, should 2.0 get exclusively while 1.0 keeps running?
4. Is the Silver forecast model still wanted as an input to fair value, or
   should 2.0's own evidence model stand alone?
