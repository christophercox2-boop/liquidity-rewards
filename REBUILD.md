# Rebuild brief

What this system is for, what must survive a rewrite, and what should not.
Written 2026-08-18 for whoever builds the next version. Read `CLAUDE.md` first
for the owner's standing preferences; this file is the technical brief.

---

## 1. The business, in one paragraph

The owner earns Polymarket US **liquidity rewards** by resting limit orders
near the touch and not trading. Fills are usually losses here, not wins — a
fill means the market moved against a resting order. The whole job is: sit in
the right markets, at the right prices, in the right size, and collect the
reward pool without getting hit. Everything else in the codebase is
scaffolding around that sentence.

Scale today: **$150–$550 a day** of rewards on a few hundred dollars of
capital at risk. Paid daily, per market, in USDC.

---

## 2. The only formula that matters

From the exchange docs, implemented in `track_rewards.py::_score_order`:

```
Score = DiscountFactor ^ (ticks from the best price on your side) × Size
```

You are paid `your Score ÷ Σ Scores in the window` of the side's pool. Four
gates decide whether an order earns anything at all:

1. **The side must hold Target Size.** Sum every participant's resting size on
   your side. Under Target Size, **that side pays NOBODY** — not you, not
   them. This is the single most misunderstood rule in the system.
2. **Your order must be inside the Target Size window.** Walk out from the
   best price accumulating size until you reach Target Size. Levels beyond
   that point score zero.
3. **The program must be live.** A closed program pays nothing; do not fall
   back to one.
4. `df` is typically 0.2–0.3, so each tick away from the touch cuts your score
   by 70–80%. Distance is punished brutally.

**Pool scope — settled by data, do not re-litigate.** The pool belongs to the
**event**, split across the event's markets and then across the two sides:

```
per side per day = pool ÷ event_n ÷ 2
```

`event_n` is the number of markets in the event, not the number sharing a
`programId`. This was proven on 2026-08-15 when 35 markets paid more than the
old per-programId convention said their entire daily pool contained. There is
a `pool_n` fallback for programs with no event size; keep it, ignore it
otherwise.

Pools change without warning. On 2026-08-18 the standard event pool was cut
from ~$500 to $200 mid-day and the system had no idea — it only recorded
*whether* a pool existed, never its terms. **Store pool, target and df per
market and diff them.** A pool cut is the single biggest thing that can happen
to daily income.

---

## 3. Order intents — get these wrong and you lose money

Polymarket US has four intents and two of them rest on the side you would not
guess:

| intent | rests as | what it does |
|---|---|---|
| `ORDER_INTENT_BUY_LONG` | **bid** | buy stock |
| `ORDER_INTENT_BUY_SHORT` | **ask** | open a short |
| `ORDER_INTENT_SELL_LONG` | **ask** | sell stock you hold |
| `ORDER_INTENT_SELL_SHORT` | **bid** | buy back a short |

Using `SELL_SHORT` to place an ask puts a **bid** on the book — you end up
bidding against yourself. This has happened.

**Cost of an order is side-dependent.** A bid at 5¢ risks 5¢ a share. An ask
at 5¢ is an opening short and risks **95¢** a share. Any budget that prices
both sides the same funds twenty times the risk it thinks it does:

```python
def cost(side, price_cents, qty):
    return ((100 - price_cents) if side == "SELL" else price_cents) / 100 * qty
```

---

## 4. Never use `/modify`

The exchange's modify endpoint is cancel-and-replace, and since the 2026-08-11
maintenance it **returns 200, cancels the original, and never places the
replacement.** Proven with a controlled test on a fresh 273-share ask.

To reprice or resize: **place the replacement first (post-only), poll until it
is verified resting by order id and minimum quantity, and only then cancel the
original.** Any failure before the cancel leaves the original untouched. A
failed cancel leaves two orders, which costs a little doubled size — never a
lost rung. This inversion is not optional.

---

## 5. What to build

Four loops. Nothing else.

**Prober** — learns fair value. Rests small scouts, watches what fills, what
rests untouched, what gets outbid or undercut, and maintains a probability
band per market. Everything downstream depends on this being honest.

**Earner** — the money. Ranks candidate markets by income per dollar at risk,
prices **both sides** of each book and takes the better one, rests near the
touch, and rotates out of markets that stop paying.

**Qualifier** — a side under Target Size pays nobody, so sometimes the
difference between earning and not is putting size on a dead side. Keep it.

**Seller** — unwinds anything that fills, and rests idle stock as asks so it
earns while it sits. This is the one loop the owner never wants gated: they
are frequently "out of a market except for selling open positions".

Deleted: defender, sniper, inventory-as-separate-loop (fold into the seller),
hunt, slate, seats, plan/restore, garden, spreads, the `/lab` and `/hunt` and
`/why` pages.

---

## 6. One risk number

**Total capital at risk across the whole book.** One dollar ceiling. Every
order is sized to fit under it, and the number is visible on one line.

Not a per-market cap with no total; not both. The system currently has a
per-market cap, a preferred-market cap, an ask cap, a total budget, a
graduated budget, a share ladder and a confidence multiplier — seven limits,
and the binding one on 2026-08-17 turned out to be a share ladder nobody had
asked for, holding 28 markets to one share each while the authorised cap was
$15 a market. **One number that binds is worth more than seven that argue.**

---

## 7. The master switch

One switch. On it runs — enters, sizes, rotates, exits — inside the risk
envelope, and only asks about things outside it. Off it stops.

**It must not live on `/map`.** That page accreted every control in the system
and became the reason everything had to be on one screen. Put the switch
somewhere it belongs on its own; let the pages stay small.

Design rules that carried over from the current system and should survive:

- **Off by default.** A fresh deploy places nothing until the switch is on.
- **On takes two taps, off takes one.** Stopping must always be easier than
  starting.
- **Every flip is audit-logged** with a timestamp.

---

## 8. Guards on anything that touches an order

These are not negotiable and cost almost nothing to keep:

- **Auth** on every order-touching endpoint, plus the `X-Reprice` CSRF header
  (cross-origin requests cannot set custom headers without a preflight that is
  never granted).
- **Known-market whitelist** — refuse any slug not in the catalogue.
- **Price bounds 0.1–99.9¢.**
- **Post-only** (`participateDontInitiate: true`) on every placement. It rests
  or it is rejected; it can never cross and fill on arrival.
- **Never rest through the other side** — a bid stays under the best ask, an
  ask over the best bid. Post-only would reject it anyway, but the scan should
  not propose it.

---

## 9. Bugs already paid for

Do not rediscover these.

**A market resolving today is the worst place to rest.** The price moves on
the result, not on anything a model knows, and the reward day ends at
settlement. Extract the date from the slug (`...-2026-08-18-jonkre`) and
refuse anything resolving today or earlier.

**Never judge a market only against its own past.** The earner withdrew from
65 of its 66 markets inside 90 seconds on 2026-08-17 because each had fallen
below 40% of its own peak. The whole board had fallen together — a pool cut —
so a rule meant to catch "this market got crowded, go elsewhere" fired
everywhere at once, and there was no elsewhere. Compare a market to the board
before concluding it died.

**Size already resting at your price is ahead of you in the queue.** Joining a
level someone else already fills earns you nothing, at any size. Merge levels
before computing your share, and only count the part of the window that is
actually yours. Getting this wrong reports 100% of a window you hold a seventh
of.

**Confidence should decide WHERE you rest, not how much.** Applying a
confidence multiplier to both the price standoff and the size compounds into
1-share orders that can never build a track record, because the track record
is what would lift the multiplier.

**An estimate is not a payment.** The monitor's integrated estimate has run
between 0.27× and 1.22× of what was actually paid, across 23 days. Anything
that acts on `est_day` as if it were money will eventually act on a 3.7×
overestimate. Always keep the actual-vs-estimate ratio visible.

**Verify against the public book, on the right side.** `_on_book` checks
whether the book shows size at your price. Pass it the order's actual side —
checking an ask against the bids finds nothing and reports a false NOT ON
BOOK, which is the one thing that would make the owner cancel a healthy order.

**A retry with no stand-off is an infinite loop.** Anything that can fail and
still qualify on the next poll — an upsize, a flip, a re-place — needs a
backoff, or it runs every 30 seconds forever.

**Alerts need a rate ceiling, not just dedupe.** Deduping identical text does
nothing against a message carrying a changing number. Cap total pushes, keep a
never-hold list for fills and money events, and log every push and suppression
so the source is findable without the owner's phone.

**Inline `onclick` handlers with quoted arguments have blanked this dashboard
twice.** Pass an index, or bind from a data attribute.

**Nothing is cacheable.** The pages carry their own JavaScript, so a cached
page runs old code against a live payload and every new field reads as
missing — indistinguishable from a deploy that never landed. Send `no-store`
on everything except images.

---

## 10. Deploy and verification

`main` → force-push to `deploy` → DigitalOcean redeploys → **the process picks
up code only on restart.** Flipping a switch reloads nothing.

Half of 2026-08-17 was spent guessing whether a deploy had landed. The fix,
which must survive: the monitor computes a **build hash** of its own source at
boot and writes it into `state.json`, which is pushed to the `live-state`
branch every ~2 minutes. Anyone with repo access can then answer "what code is
running" in seconds, with no dashboard and no phone.

Put the same things in that state file: positions, the touch for markets held
or quoted, the reward-terms snapshot, and the alert log. The owner works
entirely from a phone; anything only visible through the dashboard is
invisible to whoever is helping them.

---

## 11. Scope and secrets

- **US politics only.** Plus categories the owner explicitly asks about.
  **Never econ markets.**
- Secrets (`POLYMARKET_KEY_ID`, `POLYMARKET_SECRET_KEY`, `DASH_PASSWORD`,
  `GITHUB_TOKEN`, `NTFY_TOPIC`) exist only as encrypted env/Actions secrets.
  Never in code, commits, or output files.
- `wfco223/welcome` is a group-visible fork. **No tracker data, activity,
  balances or market info ever goes there.**
- GitHub Actions has not dispatched since 2026-08-16 (billing). Anything that
  depended on a workflow — the Silver forecast fetch, the position snapshot —
  must run in-process or not at all. Do not design new work into Actions.

---

## 12. Known-unfixed, for the next model

- **Buying power reads $0** while the info fund shows ~$209. Flagged twice
  this week, never investigated. It may be gating placements silently.
- **The earner's own scan double-counts** its size at a level others already
  occupy — the same bug described in §9, fixed in the scope tooling but *not*
  in `_earn_scan` / `_earn_ask_scan`. Every `est_day` it reports is inflated
  wherever it joins an occupied price.
- **The reward-terms snapshot seeds silently**, so changes are detected from
  first run forward, never retroactively.
- **`estimates.csv` holds ~2 days**, so estimate-vs-actual can only be
  calibrated from `state["history"]`, not from the CSV.

---

## 13. What the current code is

For scale, so the target is concrete:

```
live/monitor.py    15,002 lines   776 KB
                      145 top-level functions
                      195 constants, 144 environment knobs
                        6 automation loops, 15 action ops, 4 pages
                   auto_earn alone: 1,367 lines
track_rewards.py    1,940 lines
```

`track_rewards.py` is worth reading before deleting anything: `_score_order`
and `_daily_pool` are the exchange's rules expressed correctly, and they were
expensive to get right. Port them close to verbatim.
