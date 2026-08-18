# 2.0 design — how it gets built

Written 2026-08-18, after a full review of 1.0: all 15,002 lines of
`live/monitor.py` mapped, `track_rewards.py` read line by line, and all 65
workflows plus 117 data files traced to what actually reads them.

`REBUILD.md` says what 2.0 must do and why. This file says how, in what
order, and what the review found that REBUILD.md did not know.

---

## What the review added to REBUILD.md

Three problems the brief does not mention:

1. **There is currently no way to ship code to the running 1.0.**
   DigitalOcean builds from the `deploy` branch. The only thing that ever
   advanced `deploy` was a GitHub Action (`sync_deploy.yml`), its push
   trigger is commented out, and Actions have been dead since 2026-08-16.
   `deploy` sits at whatever it last held. Any 1.0 fix, however urgent,
   cannot reach the server until this is unblocked (DigitalOcean can simply
   be pointed at `main` instead — a settings change from the phone).

2. **Golf discovery has never worked on the server.** The Dockerfile does
   not copy `scan_markets.py` into the image, `monitor.py` imports it
   inside a silent try/except, so the hourly golf-tournament discovery
   quietly does nothing in production and always has.

3. **Nothing watches the watcher.** The 4-hourly Action that stamped ❌ on
   STATUS.md when the monitor died went down with Actions. A dead monitor
   now looks like a timestamp that quietly stops moving. 2.0 needs an
   external dead-man's check (a free uptime pinger pointed at the app URL
   is enough — it notices the process being gone, which is the case the
   process itself can never report).

The two "known broken, not fixed" items are now located precisely:

- **Buying power $0**: `fetch_buying_power` returns the first balance row
  that has a `buyingPower` field at all — with several balance rows (a
  zero row before the funded one) it returns the wrong row. It gates only
  the qualifier paths; the earner and prober never consult it. 2.0 reads
  balances once, correctly, in one place.
- **Earner queue bug**: `_earn_scan` appends our candidate order as a
  *second tuple at the same price*, then credits every tuple at that price
  as ours — counting other people's size as our score, as if first in
  line. The fixed pattern (merge into one entry per price) existed in
  `_defend_share_at` but was never carried across. In 2.0 there is exactly
  one join-estimate function and it is queue-aware (see `scoring.py`,
  already built and tested).

Worth keeping from 1.0 (verified good, port rather than reinvent):

- The **book feed**: WebSocket (200-slug cap, held+defended markets first)
  writing into an age-stamped cache, with REST rotation that only fetches
  books older than 15 s — so polling resumes by itself when the stream
  dies. Staleness × churn refresh priority. Every consumer checks age.
- The **place → verify → cancel** reprice: place post-only, poll the open
  orders up to 12 s for the new order **id** with at least the required
  quantity, only then cancel the original. `/modify` is never called.
- The **state trick**: gzipped JSON force-pushed as an orphan commit to the
  `live-state` branch — survives redeploys, keeps no history, dodges the
  1 MB API limit.
- The **alert dedupe**: per-message repeat window, 5-minute global floor,
  an always-through list for money events, and every send/suppress logged.
  (One 1.0 gap to fix: "LP rewards paid" is not on the always-through
  list, so money-in can be delayed while fills are not.)
- The exchange quirk list — encoded in `v2/` as it becomes relevant:
  GTC only (DAY orders silently expire 5 PM ET), price serialized as a
  string, fractional sizes (2 dp), opening shorts capped at roughly one
  share per dollar of buying power, dead orders returned by
  `/v1/orders/open` (denylist filter), the open-order list lagging
  placements ~4 s, silent exchange-side cancels (only the fills feed
  proves a fill), the activities feed returning both sides of every trade.

---

## Shape of 2.0

One process, deployable exactly like 1.0 (Docker on DigitalOcean), all
scheduling in-process because Actions are unavailable. Small modules, each
answering to one sentence:

| module | job | state |
|---|---|---|
| `scoring.py` | the reward formula: window walk, share, queue-aware join estimate | **built, 38 tests green** |
| `programs.py` | pick the paying program, normalize pools to $/day per event per side | **built, tested** |
| `intents.py` | the four order intents, which side each rests on, capital at risk | **built, tested** |
| `api.py` | Ed25519 auth + one HTTP client with the retry/rate-limit discipline; every endpoint wrapper | next |
| `books.py` | the WS + rotation book cache, ported | next |
| `orders.py` | place (post-only, GTC, whitelisted, bounded), cancel, reprice as place-verify-cancel | next |
| `terms.py` | reward terms as first-class data: one store, timestamped history, change alerts — the same store the estimator reads (no split brain) | next |
| `estimator.py` | ONE earned-today number | next |
| `state.py` | local JSON + live-state branch persistence; publishes touch prices, positions, terms, build hash | next |
| `alerts.py` | ntfy with the 1.0 dedupe design | next |
| `engine.py` | probe → earn → sell | after the owner's answers |
| `web.py` | the small pages | with the engine |
| `main.py` | wiring and threads | last |

### The one estimator

1.0 kept three "earned today" figures that disagreed. The root cause of
the plain sampler's bias was that order placements *woke* it, so it
sampled at exactly the moments our book looked best. 2.0 has **one
sampler on its own fixed clock that nothing else can wake**. It scores
the resting book against fresh books and current terms, integrates
rate × elapsed into "earned today", refuses to accrue when too few books
are fresh (banking the stale seconds visibly, as 1.0's HF sampler did),
and rolls the day at midnight ET. No correction factor — wrong output
means a wrong input, and the terms store is built so the inputs stay
fresh.

### The engine

- **One risk number.** `capital at risk = Σ capital_at_risk(intent,
  price, qty)` over every resting opening order. It must stay under the
  ceiling the owner sets. Every placement is sized to fit inside it.
  No per-market caps, ladders, or graduated budgets unless the owner asks.
- **Confidence decides where, the ceiling decides how much.** Never both.
- **Both sides, queue-aware.** Every opportunity is scored with
  `estimate_join`, which assumes we rest last at our level (everyone
  already there is ahead of us — if the scoring window fills before it
  reaches us, we earn nothing). That often makes a one-tick improvement
  score better than joining a crowded level; but improving the touch also
  raises fill risk, so the reward is always weighed against the expected
  cost of getting filled. Reward math alone never decides a placement.
- **Qualifying is just another opportunity**: "this side is dead, $X
  revives it and we take most of the pool" ranks in the same list.
- **Board-relative decay, absolute-zero exit.** A market is only
  "fading" relative to the median of the board — a pool cut moves
  everything at once and must not trigger a mass withdrawal (2026-08-17).
  But a market whose own program closed or whose pool went to zero earns
  nothing by arithmetic, and leaving it is correct whatever the board is
  doing. The general rule underneath both: stay only where the reward
  earned exceeds the expected cost of getting filled.
- **Resolution-day exclusion.** Markets resolving today are excluded
  from placement and flagged for exit. The date comes from the slug when
  it carries one; when it does not, from the market's own rules/end date
  on the exchange; if it is still unclear, the market is held out and
  the owner is asked — never guessed.
- **The seller works everywhere**, including markets otherwise closed to
  automation: fills get resold, idle stock rests as asks.

### The master switch

One switch instead of seven. Turning on takes two deliberate taps, off
takes one, every flip is logged with a timestamp. It lives on its own
page (`/switch`), not on any status page.

The switch **persists across deploys** (owner's decision — it is saved
state, like everything else). Two guards replace off-by-default: when a
new build boots with the switch on, the owner gets one push saying so
("new build <hash> running, switch is ON"); and a build that changes
order-touching behavior in a way worth a pause can declare itself
breaking in code, which starts that one build switched off. The rails
that do not depend on the switch (auth, CSRF header, whitelist, price
bounds, post-only) hold on every endpoint regardless.

### The pages

Each answers one question, phone-first:

| page | question |
|---|---|
| `/` | am I earning right now, and is the data fresh? |
| `/orders` | what is resting where, and what is each order worth? |
| `/markets` | the browser: what exists and what state is it in? |
| `/market?slug=` | one market: book, my orders, terms, move/cancel |
| `/opps` | what is worth joining or qualifying next? |
| `/switch` | the master switch, the risk ceiling, one line of usage |
| `/log` | what did the system do and alert recently? |

`/markets` is not one flat list — a list is often the worst way to see
these markets (owner's request). It offers views fitted to the market's
shape, drawn from what already worked in 1.0:

- **map** — state-by-state tiles for Senate/Governor races, colored by
  status (earning / idle / gap / conflict);
- **slate** — candidate grids with faces for nominee/winner fields
  (the exchange sends a photo per market; 1.0 already used them);
- **ladder** — seat-count families in ascending numeric order, so the
  distribution reads left to right (House ≥N seats, Senate seat counts);
- **list** — the fallback, filterable by market type (senate / governor /
  seats / 2028 / other), searchable.

Same auth as 1.0 (password header + custom CSRF header on every mutating
route, no-store caching everywhere).

---

## Running 1.0 and 2.0 together

Split by market (REBUILD.md option 1). 2.0 places only in markets on its
own whitelist; those same markets are marked hands-off in 1.0. The two
sets never overlap, so neither system sees the other's orders as foreign
liquidity in a market it trades. 2.0's capital allowance is the risk
ceiling, set before its first order.

Deploy: **no second subscription** (owner's decision). Both run in the
one existing DigitalOcean app: the container's start command becomes a
small launcher that starts 1.0's monitor and the 2.0 process side by
side. The app exposes one HTTP port, so 1.0's server stays the front
door and gains one ~20-line route that forwards `/v2/*` to the 2.0
process on localhost — 1.0 is the battle-tested one, so it holds the
door while 2.0 is young. When 2.0 has earned trust the roles flip, and
eventually 1.0 drops out of the launcher. Getting this live requires one
deploy, which first requires unsticking the deploy path (point the app
at `main`). The 512 MB instance is shared; 2.0 stays lean and its memory
use gets checked before the flip.

---

## Cleanup (owner asked: delete what is unnecessary)

Traced every file to what reads it. Nothing deleted yet — the plan:

- **Delete**: 49 one-off workflows (dated fixes, answered probes), ~101
  `data/` files that exactly one dead workflow wrote and nothing reads
  (~19 MB), `midterms/` entirely (nothing live references it), `PLAN.md` /
  `PLAN-GOLF.md` / `PLAN-TT.md` / `PLAN-ENTRY.md` (generated or
  superseded), `poke.txt` (no workflow watches it any more — the
  dashboard button replaced it).
- **Mine first, then delete**: 16 workflows whose comments hold real
  findings (price-as-string, the placement-failure taxonomy, the
  thin-book bait guard), and `HANDOFF.md` — the conclusions live there;
  git history keeps everything anyway.
- **Keep**: `data/rewards.csv` (ground truth), `estimates.csv`,
  `checks.csv`, `estimate_runs.csv`, `family_day.csv`, `live_orders.csv`,
  `latest_response.json`, `data/scan*.json` (monitor reads them),
  `data/silver_*_races.csv` (baked into the Docker image), STATUS.md,
  CLAUDE.md, REBUILD.md, `scan_markets.py` (monitor imports it),
  `live/defend_seed.json`, the widget, `/garden` and its assets.
- **Decide**: `data/books_log.jsonl` (19 MB) and `data/live_raw.json`
  (5 MB) — written every run, read never, half the repo's size between
  them.

---

## Build order

1. **Core math** — done: `scoring.py`, `programs.py`, `intents.py`, 38
   tests. Ported closely from the validated 1.0 code, queue-aware
   everywhere by construction.
2. **Exchange layer** — `api.py`, `books.py`, `orders.py`, `terms.py`,
   with the full quirk list encoded and tests against recorded payloads.
   Read-only parts can run against the live exchange immediately.
3. **Estimator + state + alerts + pages** — 2.0 running read-only next to
   1.0: same account, no orders, its one number comparable daily against
   both 1.0's figure and, two days later, the exchange's actuals in
   `rewards.csv`. This proves the estimate before any money moves.
4. **Engine** — after the owner's three answers below, on 2.0's exclusive
   markets, under the master switch and the ceiling.
5. **Cleanup + docs** — the deletion list above, a rewritten README,
   retire 1.0 loops as 2.0 takes their markets over.

---

## Answers from the owner (2026-08-18)

1. **Capital**: decide from an earning goal, not the other way round.
   The analysis is in `v2/CAPITAL.md` — the owner picks the goal, the
   goal picks the ceiling.
2. **2.0's first exclusive markets: the two seats families** —
   `scc-senate-gop-2026-11-03-*` and `scc-hrep-rep-2026-11-03-gte*`.
   Seats-market state as of 2026-08-18 is in `v2/CAPITAL.md`.
3. **The Silver model stays** as a fair-value input (it updates with
   polling). One implementation in 2.0 — the monitor's Datawrapper
   fetch survives, `silver_model.py`'s seat-CDF/ladder logic gets
   extracted into it, and the duplicate dies.
