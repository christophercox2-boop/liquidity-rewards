# Entry plan — where to put new orders

Built 2026-08-13 evening from a completed pool crawl, a fresh book scan, a
fresh order census, and a fresh fill history. **Nothing has been placed.**
Every order below needs your yes first.

## Read this part first

Your book changed a lot in the last day and a half, and it changed by
**fills, not by cancellations**:

| | Tue 5pm | Now (Wed 8:53pm) |
|---|---:|---:|
| Live orders | 418 | **223** |
| Capital in resting orders | $5,254.40 | **$1,690.61** |
| Buying power | $131.16 | **$104.18** |

195 orders left the book and $3,564 of committed capital went with them, but
buying power went **down** $27. Cancelled orders return their capital to
buying power; filled orders turn it into positions. So most of that was
filled. The fill log agrees: **250 fills across Aug 12–13, net cash
−$1,633.58** — money paid out to acquire contracts.

In this strategy fills are usually losses, not wins. So the honest framing:
adding orders is a smaller question than why the book is being eaten. The
plan below is deliberately small — $82 of a $104 buying power — because
committing more while that is unexplained would be the wrong bet.

## The opportunity, in one line

There are **318 politics markets with a live reward pool that you hold no
order in** (250 of them US-scope). Taking every qualifying side would need
about **$477,000**. You have $104. Capital, not opportunity, is the binding
constraint, so the only question worth answering is which $82 of seats are
the best ones.

## The plan — 12 orders, $82.09, estimated ~$28/day

Every one of these: the side already meets its Target Size (so the side
qualifies and pays), your order rests **at the current best price** (0 ticks
off, maximum score), and the market has had **zero fills in the last two
days**.

| # | Market | Side | Price | Size | Cost | Your share | Est. $/day | Spread |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 11¢ | 10 | $8.90 | 59% | $3.68 | 5¢ |
| 2 | `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 32¢ | 10 | $6.80 | 50% | $3.12 | 26¢ |
| 3 | `ussewc-usse-co-2026-11-03-rep` | SELL | 27¢ | 10 | $7.30 | 50% | $3.10 | 21¢ |
| 4 | `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 65¢ | 10 | $6.50 | 47% | $2.91 | 22¢ |
| 5 | `ussewc-usse-mt-2026-11-03-dem` | SELL | 9¢ | 10 | $9.10 | 67% | $2.78 | 5¢ |
| 6 | `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 10¢ | 10 | $9.00 | 40% | $2.50 | 4¢ |
| 7 | `usgubewc-usgub-ct-2026-11-03-rep` | SELL | 25¢ | 10 | $7.50 | 33% | $2.08 | 19¢ |
| 8 | `ussewc-usse-ky-2026-11-03-rep` | BUY | 81¢ | 10 | $8.10 | 33% | $2.08 | 7¢ |
| 9 | `usgubewc-usgub-id-2026-11-03-dem` | SELL | 42¢ | 12 | $6.96 | 26% | $1.60 | 36¢ |
| 10 | `ussewc-usse-al-2026-11-03-rep` | SELL | 94¢ | 27 | $1.62 | 25% | $1.57 | 40¢ |
| 11 | `ussewc-usse-ms-2026-11-03-rep` | SELL | 88¢ | 21 | $2.52 | 25% | $1.57 | 5¢ |
| 12 | `vsc-usgubp-fl-fshbck-atl-11pct` | BUY | 19¢ | 41 | $7.79 | 25% | $1.25 | 37¢ |
| | **Total** | | | | **$82.09** | | **$28.24** | |

That leaves **$22 of buying power untouched** as headroom.

### Treat the $28/day as a ceiling, not a promise

Your own payout history says this kind of seat *under*-performs its estimate.
HANDOFF records that thin dominated markets — exactly this pattern, where a
small order owns most of a near-empty side — **paid about 0.5x estimate**,
while busy race markets paid 3–5x. So plan on something like **$14–20/day**
and treat anything above that as upside. Even at 0.5x, $82 returning $14/day
is a better rate than the current book ($1,690 committed returning ~$88/day).

The share numbers are exact, not guesses: for 11 of these 12, the saved book
levels already cover the whole Target Size window, so the denominator is
fully known. The huge depth sitting deeper in these books (500,000 contracts
at 2¢, and so on) scores essentially zero because it is 40+ ticks from the
best price and the discount factor is 0.10 per tick.

## What I am NOT recommending, and why

**The biggest single-market numbers.** `ewc-usgub-ca-2026-11-03-stehil` looks
like the best thing on the board — about $21.60 buys an estimated $18.75/day,
and STATUS.md has been flagging it independently. But its spread is **1 tick**.
The ask sits one cent above your bid, so it fills easily, and a fill here is
the loss you are trying to avoid. Same for the other $300-pool `ewc` races:
big pools, 1¢ spreads. Say the word and I will price one as a deliberate
exception, but it does not belong in a low-fill-risk tranche.

**The Florida primary markets** (`enwc-usgubp-fl-2026-08-18-*`, $300 pools).
They resolve **August 18, five days out**. Primaries move hard near the date.
That is the opposite of a calm book.

**The `cranc` 2028 presidential block.** I pointed you at these earlier as the
interesting find — that was wrong and I withdraw it. Their $100 pool splits
across **33 candidate markets**, so a whole side is worth $1.52/day even if
you own all of it. Not worth the capital.

**Six markets that otherwise made the shortlist**, cut because they filled in
the last two days: `ussewc-usse-ks-2026-11-03-dem` (7 fills),
`scc-hrep-rep-2026-11-03-gte220` (3), `enwc-ushrp-fl25-2026-08-18-dem-olilar`
(3), `usgubewc-usgub-nh-2026-11-03-rep` (2), `usgubewc-usgub-wy-2026-11-03-dem`
(2), `usgubewc-usgub-fl-2026-11-03-dem` (2). A wide spread in a single snapshot
is weaker evidence than the fill log, and these disagreed.

**House districts** (`ushrewc`). The completed crawl confirms **no `ushrewc`
market carries any reward program**. Any capital resting there earns exactly
zero. Worth cancelling, not adding to.

**Foreign races and econ markets.** 68 foreign markets with pools (Argentina,
Israel, a UK by-election, Venezuela) are outside your scope, and econ markets
are excluded by your standing rule.

## Two gaps I have not closed

1. **24 `apdc` and some `scc` markets were never book-scanned.** The discover
   workflow filters with `_is_us_politics`, which rejects `apdc-alito-*` and
   `scc-senate-gop-*` as non-US even though they are US markets you hold. So
   the scan covered about 210 of 250 candidates. Fixable, not yet fixed.
2. **The fill wave has no explanation yet.** 250 fills in two days, net
   −$1,634, with the defender and keeper both off since Tuesday. Worth
   understanding before adding capital, not after.

## If you want these placed

Reply with which numbers — "all 12", or "1, 2, 5", or your own sizes. Then,
per your standing rules:

- Post-only, so nothing crosses the spread and every fill is passive.
- One market at a time, verified resting by order ID and minimum quantity
  before moving to the next.
- No `/modify`, ever.
- The defender and keeper switches stay **off**. Nothing here turns on any
  automation, and none of these orders will be repriced by anything unless
  you switch a loop on from /map yourself.
