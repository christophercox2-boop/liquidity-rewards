# Session handoff — 2026-08-12 evening

Read this first in a new session. It is the owner's operating rules plus
everything learned the hard way. The owner is phone-only; talk plainly, no
characterizing; lead with numbers; when a claim matters, verify it against
data before asserting it (three wrong assertions in one day came from
reasoning ahead of the data).

## Standing rules (owner's, do not relax)
- Keep ALL tracker data and activity OUT of the group-visible wfco223/welcome
  fork. Everything lives in wfco223/Liquidity-rewards (private).
- Secrets (POLYMARKET_KEY_ID / POLYMARKET_SECRET_KEY / DASH_PASSWORD /
  GITHUB_TOKEN / NTFY_TOPIC) only as encrypted Actions/env secrets. The ntfy
  topic is a password.
- Order-touching endpoints keep auth + X-Reprice CSRF header + known-market
  whitelist + 0.1–99.9c price bounds + post-only.
- Markets: US politics plus categories the owner explicitly asked about.
  Never econ markets.
- NOTHING places orders automatically unless the owner turned its switch on
  from the /map buttons. No new automation that places orders without a
  per-loop owner switch, off by default, persisted, audit-logged.

## Current state (as of ~6pm ET Aug 12)
- 364 live orders, ~$5,254 committed, buying power ~$216.
- Zero ghost orders (health check verifies; census in data/health.txt).
- Defender and keeper both OFF. They are now separate owner switches on /map
  (top of page): ON needs two taps, OFF is one tap, choice persists in
  state["auto"], every flip is audit-logged in Recent actions. Env pauses
  (DEFEND_PAUSE/KEEP_PAUSE) remain a host-side veto; the /map banner reports
  the EFFECTIVE state and names any veto.
- origin/main == origin/deploy. The DO monitor picks up builds only on
  restart; the /map banner is the way to confirm which build is live.
- Defend caps: seed v8 (live/defend_seed.json). 43 favourite caps raised to
  model-fair-minus-3c (ceiling 95c), 4 above-fair caps lowered to fair-minus-3
  (FL sen 75.4, KS sen 79.9, FL gov 81.3, NH gov 81.8). Idaho excluded by
  request. Lowering a cap never moves existing orders. The monitor polls the
  seed from main every 60s; version-gated.

## Hard-won facts (violating these has cost real money)
- The exchange /modify endpoint DESTROYS orders (200, cancels, never
  replaces). Never call it. do_reprice = place replacement → verify by the
  returned ORDER ID and MINIMUM QUANTITY → only then cancel the original.
  Verification by price alone false-positives on the original order.
- SELL orders rest at most ~273 shares each (short-size cap). The 99c ask
  stacks (up to 19 orders at one price) ARE the position — never dedupe
  them. BUY orders rest up to 10,000; merge_buy_rungs.yml collapses buy
  stacks with a never-shrink invariant (ran clean: 412→364, zero rungs lost
  size).
- /v1/portfolio/activities returns BOTH sides of each trade. Ours is the
  PASSIVE execution (all our orders are post-only; aggressor pays taker fee,
  passive collects rebate; verified against live order ids). The monitor's
  fill parser was fixed for this on Aug 12; before that it dropped all fills
  and the app looked quiet while 103 fills (-$1,074 net) happened overnight.
- price.value must be a JSON STRING; `symbols` must be a LIST param;
  git fetch needs an explicit refspec; verify pushes with
  `git show origin/main:<file>`; estimates.csv keeps only the last 30k rows;
  the dashboard's Recent actions list is 20 in-memory entries and dies on
  restart — the exchange's activity feed (fill_history.yml) is the real
  transaction record.
- The keeper has TWO branches: deep 1c/99c qualifiers AND a scoring branch
  that places 40-share orders a tick inside the touch under the defend cap.
  It is now gated to armed markets only, but re-enabling it re-enables both
  behaviours.

## Economics learned (numbers, not vibes)
- Aug 11 payout: $406.66 PENDING, 135 markets — 2nd best day (Aug 10 paid
  $557.62). Gov races $229 + Senate $109 = 83%.
- Estimator error is COMPRESSION: race markets paid 3–5x the estimate
  (dozens paid a flat $5.3–5.9 ≈ 44% of each $12.50/day per-market pool,
  regardless of estimated share), while thin dominated markets (scc ladders,
  WY dem, ID rep, Becerra) paid ~0.5x. Hypothesis to test with the Aug 12
  payout: actual payout weights qualified presence more evenly than the
  tick-proximity score model assumes.
- Pool structure: senate/gov races $25/day per race (2 mkts) = $6.25/side;
  scc $100 over 13; college bb $500 over 73 ($3.42/side, thick books, only
  the ~20 cheapest bid sides are worth entering: ~$54 for est $3.42/day);
  NBA East $1000 over 15 but every spread is 1 tick with 100k+ queues —
  unquotable; WNBA MVP $250 over 4 ($31/side): Clark bid (2.9k resting) and
  Bueckers bid (2.8k) are the cheap entries (~$12 total for est ~$3/day) —
  NOT placed, and the survey's 1c-bid filter bug hides Bueckers (bug not yet
  fixed).
- Fill-rate by family (fills per 100 market-days): iarc/vtc 0, nphc 3.5,
  dipcc 6.9 ... scc 98, opdc 280. College bb is 53 — mid, not calm. The
  owner's stated preference: rest near the touch with low fill risk.

## Open items

### 2026-08-16 — earner stopped by the owner. Read this before restarting it.

The owner cancelled every order by hand and switched all five loops off
after the earner bought ~133 shares of New Mexico Senate REPUBLICAN at
10c. Silver has that race at 0.62%. We paid roughly sixteen times fair
value, and it kept happening while it was being discussed.

What actually went wrong, in the order it matters:

1. **The model was outvoted by the order book.** At 1c vs 10c the
   bid-touch anchor favoured 10c by 4.25 in log-likelihood; the Silver
   prior favoured 1c by 1.06. The anchor was heavy because the bid side
   holds thousands of shares — but those are reward farmers at 1-9c, not
   people who think a Republican wins New Mexico. DEPTH WAS BEING READ AS
   BELIEF. In a reward-farmed book that is exactly backwards: the more
   crowded the farming, the more certain the model became.
2. **No fair-value gate below 10c at all.** The check only applied above
   the penny ceiling. Under it the only question was whether reward
   income beat the worst case, which in a farmed book is always yes.
3. **Guards that shipped but never ran.** The price cap only gated NEW
   orders while the bad ones kept resting and filling. The cleanup meant
   to pull them iterated a registry that is re-adopted AFTER the switch
   check, so with the earner off it looped over nothing, every poll,
   silently. A guard that no-ops is worse than no guard: it reads as
   protection in the log and in the code.

All three are fixed in code (Silver price cap with a 3c margin, prior
rescaled to sqrt(p(1-p)) and weighted 1.2, size tapering away from the
forecast, off-model sweep over every resting BUY that runs switch-off).
None of it is proven, because the owner stopped it before the sweep fired.

**THE THING TO CHECK FIRST when restarting.** Every one of those guards
calls _silver_fair(), which returns None when the monitor's SILVER table
is empty — and then all of them pass everything through in silence. The
daily Silver fetch is a GitHub Action, and Actions have been failing on
exhausted minutes since 2026-08-15. Before the earner goes back on,
confirm the monitor has a live Silver table (the /map payload's `model`
block shows senate/governor counts) and make the earner REFUSE to bid in
a race where the model has no opinion, rather than proceeding blind.

Still unbuilt, and the better half of the owner's instruction: where our
side is badly overpriced the edge is on the OTHER side, and the earner
should rest there rather than simply decline to trade.


### Owner-requested, NOT yet built (2026-08-16)
- **Auto-qualify markets resolving Nov 2026 or later.** Owner: for anything
  resolving that far out it is fine to qualify BOTH sides automatically,
  because the chance of being filled at the 1c/99c floors is very small.
  For anything sooner, or when buying power will not cover it, the market
  goes into a pending list the owner approves or denies by hand. Needs its
  own /map switch (nothing places orders without one), a resolution-date
  parse per market, a buying-power reserve, and an approve/deny queue.

  Owner settled the open questions 2026-08-16: watch out for PRIMARIES,
  which carry a distinct slug, and it is fine to hold the ~$200 qualifiers
  aside for manual approval.

  Classification is written and verified against the live program list —
  172 auto, 9 to approval:
    * primary = slug contains usgubp / ussep / ushrp / uspresp. Catches all
      9, including the two vsc-usgubp Florida vote-share markets that carry
      no date at all.
    * far-dated = a full YYYY-MM-DD in the slug at 2026-11 or later, ELSE a
      bare 4-digit year >= 2027. The bare-year branch matters: the 31 2028
      nomination slugs have no YYYY-MM-DD, only "2028", and a naive date
      parse sends the most obviously far-dated markets on the board to the
      approval queue.
    * auto covers 60 of the 2028 slate, 46 senate, 42 governor, 19 seat
      ladders; the 9 needing approval are all primaries (OK governor, FL
      house, MA and NH senate, FL vote-share).
  Still to build: the switch, the cost estimate per side, the spend cap
  that routes ~$200-class jobs to the queue, and the approve/deny UI.
### 2026-08-16 — third-candidate races lost their model backing (SHIPPED)

Owner flagged Rhode Island governor: a third candidate is in the race and
the Silver model does not know it, and we had bought Yes shares anyway.

What was wrong. `data/silver_gov_races.csv` carries RI as
`Helena Foulkes 99.2075 / Aaron Guckian 0.7825` — two candidates summing to
exactly 100. All 36 governor rows sum to 100, so a sum check finds nothing;
the model normalises to two ways whether or not the race IS two ways. The
exchange event holds THREE markets: `-dem`, `-rep` and `-kenblo` (Ken Block).
So `_silver_fair` found no party token in the kenblo slug and returned None,
`_race_family` also wanted a party token and said False, and kenblo fell
through to the loose `MAX_UNBACKED_BID_C` = 15c ceiling. That is what let a
blind 7c Yes bid exist. Worse, the D and R numbers were never valid for the
`-dem` and `-rep` markets either — they divide a 100% that Block is standing
inside of.

The fix. `_third_candidate_race(m)` reads the event's siblings and returns
True if any tail is neither `dem`/`rep` nor a number (seat-ladder rungs).
`_silver_fair` returns None for the WHOLE event — not just the market the
model forgot — and `_race_family` returns True for it, so bids fail closed
at `RACE_NO_MODEL_BID_C` = 2c instead of 15c. Qualifier bids at 1c still fit.

Asks are the deliberate asymmetry: `_ask_allowed` returns True for these
events. The flip loop places SELL_LONG WITHOUT consulting `_ask_allowed`, so
blocking asks would only have the sweep cancel every flip the flip loop
placed, on a loop, and leave us holding stock in the one kind of market we
had just decided we cannot price. Getting out is the safe direction.

It is not one race. Eight events on the board carry a non-party candidate:
  CA gov (stehil, xavbec — no party markets at all), MI gov (mikdug),
  NE sen (danosb), AK gov (SEVEN named candidates, no party markets),
  RI gov (kenblo), ID sen (todach), MT sen (setbod), SD sen (briben).
Nebraska matters most — Osborn is the real contender there and the Silver
D/R split is meaningless. All eight now bid at 2c maximum.

Memoised on `_PROG_CACHE["ts"]`. Without it the fallback sibling scan runs
per order in the sweep and per market in the earner: 0.33us cached.

Not fixed by this: the 1 kenblo share already held. The guard stops new
bids; it does not unwind a position.

### 2026-08-16 — GitHub Actions is not running ANY job (OWNER ACTION NEEDED)

Owner was being flooded with "Sync deploy branch" failure emails. The workflow
is not the fault.

Evidence: since ~03:34 UTC on 2026-08-16, every run of every workflow in the
repo fails. The jobs report `runner_id: 0`, `runner_name: ""`, no logs at all
(the log download 404s), and finish in three or four seconds — including the
`track` job, which installs Python and pip-installs requirements and cannot
possibly finish in four seconds. Jobs are never being dispatched to a runner.
The last successful run was 02:51 UTC; 141 sync_deploy runs, 1,410 runs in the
repo overall.

For a private repo that signature means the account's included Actions minutes
are spent, or the spending limit is zero. **Fix at github.com/settings/billing
— nothing in this repo can fix it.**

Do not be fooled by the data commits still landing in main. Those are authored
by `wfco223`, not `github-actions[bot]`: they come from live/monitor.py on
DigitalOcean, which took over the hourly tracker on 2026-08-15. Actions is
contributing nothing right now.

**Reward tracking itself is NOT affected and needs nothing.** It moved into
live/monitor.py on 2026-08-15 (`tracker_loop`): the monitor runs the same
track_rewards.py as a subprocess every hour and commits STATUS.md plus every
data/*.csv to main through the git data API. Verified 2026-08-16 18:24 UTC —
STATUS.md stamped 2:12 PM ET, twelve minutes old. That is why data commits keep
landing authored by `wfco223` while every Actions run fails.

The real casualty is the DEAD-MAN'S SWITCH. The 4-hourly Actions run existed
to stamp a ❌ into STATUS.md and email if the container died. With Actions
dead, a dead monitor now looks like a timestamp that quietly stops moving and
no email arrives. An external watcher is needed — DigitalOcean App Platform
alerts on the existing health check are the cheapest fix since that account
already exists; a free uptime pinger against the monitor's health endpoint
also works. Not built: it needs an owner decision and a signup.

STATUS.md was lying about all of this and is fixed. The header carried the
Actions badge — permanently RED while tracking ran perfectly — and told the
owner to "check the Actions tab" if the timestamp went stale, which is the
wrong place even when Actions is healthy. It now names whoever actually wrote
it (`GITHUB_ACTIONS` decides), shows the badge ONLY on an Actions-written run
so it comes back by itself if minutes are restored, points at /map otherwise,
and carries a standing warning that nothing is watching the watcher.

Other things degraded while Actions is down: the 4-hourly heartbeat that
posts the ❌ freshness banner, the daily estimator scoreboard, the silver
report and races jobs, and every manual-dispatch workflow (the poke.txt
pattern). The Silver MODEL itself is fine — the monitor fetches it from
Datawrapper's CDN directly, not from fetch_silver.yml.

The push trigger on sync_deploy.yml is commented out (not deleted) because
that one workflow fired on every code push and was 26 of the last 30 failures.
Restore it once minutes are back. Nothing is lost meanwhile: deploy is
force-aligned onto main by hand at each deploy, and the monitor only picks up
code on restart anyway.

Its git logic was wrong regardless and is now fixed. It used to run
`git push origin origin/main:refs/heads/deploy`, which can only fast-forward,
so any rewrite of main's history left deploy stuck. deploy is a MIRROR that
nobody commits to, so it now force-updates with `--force-with-lease` against
the SHA it just read — which still refuses if someone else moved deploy. All
three paths (already in sync, needs updating, does not exist) are tested
against a stubbed git.

### 2026-08-16 — Refresh button on the homepage (owner)

"Build a button (like the poke file) that lets me get an updated reading of my
liquidity rewards manually... prominently featured on the homepage." Then:
"when I press it, I should see a loading process bar... if everything is
unchanged, it can say that briefly before disappearing, but if there is an
update show me what is new in detail."

Full-width button in the hero on `/`. `tracker_loop` now waits on
`TRACKER_KICK` instead of sleeping, so POST `/track_now` starts a reading
immediately rather than at the end of the hour. Auth + the X-Reprice CSRF
header like every other POST; it touches NO orders, it runs the same
track_rewards.py the hourly loop runs.

The bar is INDETERMINATE on purpose — a reading walks every market's programs
and has no progress to report, so a percentage would be invented. Elapsed
seconds beside it give the real scale.

The diff is the interesting part. It snapshots earned today, the rate, order
and market counts, buying power, per-market earnings and the paid/earned
history BEFORE kicking, then compares after. Nothing changed → one line that
clears itself after six seconds. Something changed → a persistent list:
money first, then newly posted payouts (the thing most worth surfacing), then
counts, then the eight biggest per-market moves with the rest counted.

t_button drives the real page in node across all three outcomes.

### 2026-08-16 — what makes the loops DUMP orders, and how fast (audit)

Owner asked what can make the earner or prober dump orders and how quickly.
Every path, with its real trigger and cadence:

EARNER
  * off-model sweep — EVERY POLL (30s), ignores the switches, because
    cancelling only reduces exposure. Trigger: `_bid_allowed` / `_ask_allowed`
    fails. Marks the market untouchable for 24h.
  * withdrawal — every poll after a 10-minute grace per order. Trigger:
    income under 25% of the order's cost per day (payback beyond 4 days), or
    the market diluted to <40% of a >=$1/day peak. 1h stand-down after.
  * rotation — at most every EARN_ROTATE_EVERY (30 min) AND only at >=85% of
    the $100 budget. Cancels the worst EARN_ROTATE_N (3) by yield per dollar.
    Skips graduates and anything under 10 minutes old.
  * flip over-sell puller — every poll, cancels newest flips beyond the
    position.
PROBER
  * TTL rotation at PROBE_TTL (30 min) per scout.
  * immediate pull when the market has no reward program, or is a primary.
  * the same off-model sweep (it judges prober orders too).

THE ANSWER TO "HOW QUICKLY" WAS: everything, inside one 30-second poll. The
sweep had no limit. That was survivable while the gates barely bound, and is
not now — `_silver_fair` returned None for every market until today, so every
loop order is being judged against a real forecast for the FIRST TIME, and a
wrong model could have emptied the book before anyone saw it.

`EARN_SWEEP_MAX_PER_POLL` (12) now caps it, worst-first by distance from fair,
with the deferred count written to the journal. A genuine mass problem still
clears fast — 40 orders in 4 polls, about two minutes — but nothing disappears
in one go unseen. Tested in t_sweep.

### 2026-08-16 — can a graduate fall back down? Yes, but two exits were missing

Owner: "Can a graduated market ever fall back down? If it's not based on
confidence I don't see how."

It can, and it always could — demotion just had nothing to do with knowledge.
Graduation grants ONE thing: exemption from `EARN_TOTAL_USD`, so the order
keeps earning without consuming the search budget. It is never a licence to
place more.

Entry needs five things: an hour on the book, >= EARN_GRAD_MIN_RATE, payback
of its own worst case inside EARN_GRAD_PAYBACK days, NO fill ever taken in
that market, visibly on the book, and room under EARN_GRAD_MAX_USD.

Demotion tested only the first two, which made the other three a ONE-WAY
RATCHET: a graduate could start taking fills, or go dark on the book, and keep
its cap exemption forever. Both now demote, so every condition of entry is a
condition of staying. Full trigger list, all tested in t_grad:
  * its own rate falls below half the floor;
  * the market is diluted to under 40% of an >= $1/day peak;
  * the market takes a fill after graduating  (NEW);
  * the order is no longer visibly on the book (NEW — explicit False only, an
    unknown book reading is not evidence);
  * the order disappears (`grad &= set(_EARN["orders"])`);
  * the off-model sweep pulls it — that pass does NOT exempt graduates, and
    discards from `grad` when it cancels. Now that `_silver_fair` actually
    works, this is the route by which the race model reaches a graduate.

CONFIDENCE STILL PLAYS NO PART, on the way in or out. The loop never calls
`_earn_confidence` or `_bayes_fair`. That is defensible — a quiet market gives
low confidence AND low fill risk for the same reason — but it means exempt
capital can sit in markets we cannot price. Deliberately NOT changed: demoting
on low confidence would demote nearly every quiet market at once and gut the
point of graduation. If the owner wants it, the better shape is a separate cap
on how much GRADUATED capital may sit below the confidence floor, rather than
a blanket demotion.

### 2026-08-16 — a SHORT is not a SALE, and my own carve-out let one through

Owner's receipt: "Rhode Island Governor Election Winner / Democratic Party ·
No", bought at 48c. That is not a sale — it is the prober OPENING A SHORT at
~52c on the RI Democrat, in a race Silver reads as ~99% Democratic.

It went through a hole I opened hours earlier. `_ask_allowed` returned True
for every ask in a third-candidate race, and I wrote that carve-out
explicitly so the flip loop could SELL STOCK WE HOLD without the sweep
fighting it. But one gate served both trades, and they are opposites:

  * SELL_LONG unwinds a position — risk DOWN, and the right thing to allow in
    a market we have declared unpriceable;
  * BUY_SHORT opens a brand new position on the other side — risk UP, and at
    price p it risks (1 - p) to win p.

`_ask_allowed(m, price_c, opening=False)` now splits them. With a forecast,
both still need `price >= fair - margin`. With NO forecast an opening short
gets the MIRROR of the unbacked bid ceiling: a race the model should price
gets no new shorts at all, and anywhere else the short must sit at or above
`100 - MAX_UNBACKED_BID_C` (85c). The rule in one line: without a model we may
only ever take the cheap tail of a market, never pay up into an uncertain one.
A bid may cost at most 15c a share; so may a short. 48c fails by a mile.

auto_probe passes `opening=not can_sell_inv`, which is the same flag that
already decided SELL_LONG vs BUY_SHORT two lines later. The sweep only ever
judges SELL_LONG, so it keeps the inventory semantics.

Also audited, since the owner asked whether anything else goes far afield:
  * auto_snipe opens shorts and never consulted the model. It now refuses to
    short into a bid below `fair - margin` — it sells to people bidding ABOVE
    fair, so a bid UNDER fair means they have the good end. Its own band check
    only ever bound when the band was tight AND had a fill.
  * the qualification keeper can open shorts too, but its per-market caps are
    the OWNER'S hand-set config, and CLAUDE.md is explicit that the code never
    overrules those. Left alone deliberately — flag it if you want it gated.
  * manual_place is the owner's own tap and is left alone by design.

### 2026-08-16 — THE SILVER MODEL WAS NEVER ONCE REACHED (FIXED)

Owner spotted it: the /why page said "no Silver number for this market" for
`usgubewc-usgub-ar-2026-11-03-dem` while Silver plainly publishes Arkansas at
Dem 0.2% / Rep 99.8%.

It was not Arkansas. `_silver_fair` returned None for EVERY market on the
board. `_parse_silver` keys the table by `abbr.strip().lower()` — `'ar'` — and
the lookup asked for `st.upper()` — `'AR'` — so it missed every row. One
character.

It shipped in 0cd7202 at 02:48 UTC on 2026-08-16, the very commit that
introduced `_silver_fair` for the prober and earner, and was live all day.
That means every guard built on the forecast was inert for its entire
existence: the price cap, `EARN_SILVER_MARGIN`, the size taper away from
fair, the sv_cap in the earner scan, and the third-candidate withdrawal. What
actually held the line all day was the FALLBACK — `_race_family` sending
unpriced races to `RACE_NO_MODEL_BID_C` (2c) and everything else to
`MAX_UNBACKED_BID_C` (15c). Those are why the day was not much worse.

Verified after the fix against the real files: all 72 governor markets and the
senate table resolve; Arkansas dem reads 0.205c, Arkansas rep 99.795c,
Kentucky rep 99.5575c.

**Why the tests did not catch it, which matters more than the bug.** Every
stub built its Silver table by hand with UPPERCASE state keys, so the tests
encoded my assumption instead of the real contract and agreed with the broken
code. All of them now run the real `_parse_silver` over the real
`data/silver_*.csv`, and t_ri asserts outright that a known state resolves to
a known number. A stub that invents the shape of its input cannot catch a
disagreement about the shape of that input.

Expect real behavioural change now that the model is actually live: race
markets move off the flat 2c no-model cap onto fair+3c, which is far tighter
on longshots (Arkansas dem: 3c, not 2c... but Kentucky rep: 99.9c, not 2c) and
newly permits sensible bids on heavy favourites. Asks in modelled races are
now bounded below by fair-3c, so the sweep will pull inventory asks sitting
under a favourite's forecast.

### 2026-08-16 — the standoff was measuring the wrong distance (FIXED)

Owner: "couldn't all that be true for buying a few cents closer to fair
value? Why be so far off when you're not confident, and there seems to be no
analysis of alternatives." Both halves were right and both were my bugs.

**The standoff bit in exactly the wrong case.** By the time the touch-standoff
applied, `top` had ALREADY been capped at the band's 10th percentile by the
rung ladder. So `min(top, touch - back)` could only bind when the touch sat
BELOW the 10th percentile — precisely when bidding at the touch means buying
under the bottom of the fair range, which is the outcome we want. It bought no
safety and cost about 91% of the reward score (df 0.3, two ticks). Distance
from the touch was never the protection; distance BELOW FAIR is. The standoff
now only trims the part of the range reaching ABOVE the value-safe level, and
at or under `b["lo"]` the price itself is the protection. Measured: 8 of 400
randomised low-confidence markets now price nearer the touch than the old rule
allowed, every one of them under the 10th percentile.

**There was no analysis of alternatives.** The scan ranked candidates purely
by income, so it always took the dearest allowed price and never compared what
being wrong would cost. Every row now carries the expected edge against the
posterior MEAN (the mean, not the median — expected profit on a fill is a sum
over the whole distribution), and a fill that would buy above fair must have
that overpay paid back by income inside a window that shrinks with confidence
(`EARN_EDGE_PAYBACK`, scaled by score/EARN_CONF_FULL). The old deal test only
ever asked whether income beat a TOTAL loss, which in a reward-farmed book it
always does and which is the wrong risk anyway. Selection now prefers a price
that buys under fair over a dearer one that scores more. The /why page shows
the edge per candidate and names the runner-up.

### 2026-08-16 — the flipper is off the 2028 party markets (owner)

"The flipper should ignore the 2028 party markets." `FLIP_SKIP_PREFIXES =
("ewc-usp-party-2028-",)`, enforced at all three points where the flipper can
act: it will not queue one, will not place one (and DROPS jobs queued before
the rule rather than leaving them retrying for the window), and will not
re-queue one that vanished. Those markets hold size for the owner's own
reasons, so an automatic sell-back is not recovering a fill, it is liquidating
inventory that was never the earner's to sell.

NOT done: flip asks already resting in those markets are left alone. Pulling
them is an order-touching action and needs the owner's yes.

### 2026-08-16 — the flip loop ran away on the 2028 party market (FIXED)

Owner's screenshot: `ewc-usp-party-2028-11-07-rep` repeated a dozen-plus
times, every row identical — 350 @ 40¢, cost 38¢, age 0m, NOT ON BOOK. The
list is keyed by ORDER ID, so those were real distinct orders, not a render
bug: ~4,900 shares of ask against a 350-share position.

Two defects compounding, and a third loop closing the circle:

1. **`committed` was blind to the current pass.** The placement loop summed
   resting SELL_LONG from `MONITOR.orders`, a snapshot from the last poll. With
   several jobs queued for one market, every one computed the same
   `net - committed` and placed the FULL size. Fixed: a per-pass accumulator
   plus anything in the flips registry the snapshot has not caught up with,
   and at most one flip per market per pass.
2. **Vanished flips were re-queued unconditionally.** `place → exchange kills
   it → seen missing → re-queue → place` had nothing damping it. Fixed with
   `EARN_FLIP_VANISH_MAX` (3) and a `EARN_FLIP_VANISH_RESET` (1h) forgiveness
   window, persisted to state so a container replace cannot forgive the market
   and restart the loop.
3. The excess-flip puller was cancelling the over-sold asks every poll, which
   is why they read NOT ON BOOK — so the system was fighting itself, cancel
   and re-place, burning rate limit. That puller was working correctly; it was
   cleaning up after a bug rather than causing one.

Reproduced and fixed under test (t_flip): 14 queued jobs for one market now
place ONE order of 350 rather than fourteen.

### 2026-08-16 — graduated orders can sit at 8% confidence (EXPLAINED, not changed)

Owner noticed a graduated order on `ewc-usp-2028-11-07-andbes` scoring 8%.
Not a contradiction — the two measure different things. Graduation tests the
ORDER (an hour old, ≥$0.50/day, payback inside two days, visibly on the book,
no fill ever taken in that market, under the $150 cap) and never consults the
model. Confidence measures how well we know what the contract is WORTH.

In a quiet market they anticorrelate: nobody trading means no evidence
accumulates AND nothing reaches down to take our order. Low confidence there
is partly a symptom of the same calm that makes the order safe.

The real exposure is narrow but genuine: a graduate is exempt from the dollar
cap, so the least-understood markets can hold a position indefinitely, and if
one ever fills we have no idea whether the price was good. The /why page now
states this in the earner card whenever an order has graduated. Adding a
confidence floor to graduation would trade earnings for safety — an owner
decision, not taken.

### 2026-08-16 — /why, one page per market (SHIPPED)

Owner: "Give me some insight into where the confidence numbers come from. Let
me click and see a whole page for each market that breaks down what's going
into it. This should be for the probe and the earners."

`/why?slug=...`, reached by a "why?" chip on every market row in the PROBER
and EARNER lists on /lab. Deliberately NOT on the order sheets — owner,
2026-08-16: "just make it on the probe / earner page for each market in the
lists. I don't need it on an order modification screen." The sheets are for
moving and cancelling; the breakdown belongs where the numbers are read. A
test asserts the link is present on both lists and absent from both sheets.
Eight sections:
confidence with every component, fair value with the evidence, the race
forecast, the reward program, the earner's scan, the prober's gates, and our
own position. Card rendering is isolated so one failure cannot blank the page.

Two things make it honest rather than decorative:

* **Leave-one-out.** Every observation is re-scored WITH IT REMOVED and what
  the page prints is how far the median moves when it goes. A weight on its
  own answers nothing — a heavy term agreeing with everything else moves the
  answer by zero. On a live example the 7c fill was worth -4c and the Silver
  forecast +4c, while three of the seven terms changed nothing at all.
* **One code path.** The earner section calls `_earn_scan`, the same function
  `auto_earn` calls. The page reports the real decision including every
  rejection reason, not a second implementation that can drift.

`_bayes_fair` was split into `_bayes_terms` (the evidence, each with a
plain-English note) and `_bayes_posterior` (the grid) to make that possible.
400 randomised evidence sets confirm the split reproduces the old lo/med/hi
EXACTLY. Two bugs were caught by that test and both were mine: rounding the
term weights before they entered the log-likelihood moved a median by a cent.
Weights stay full precision; rounding is the page's job.

One deliberate difference: `n` used to count every journal row for a market
including "scout" and "pulled" rows that carry no information, so three
information-free rows could satisfy the old `n >= 3` gate. It now counts
actual evidence.

### 2026-08-16 — confidence is a dial, not a cliff (SHIPPED)

Owner: "if a market is struggling to get to an adequate confidence level, it
can just back down a price level or two or reduce quantity. Likelihood of
getting picked off goes down the further you are from the touch."

The old gate was pass/fail — one trade OR two rested scouts OR three rows —
so a market just under the bar got nothing and one just over it got the same
exposure as a market with a forecast and four fills. `_earn_confidence` scores
0..1 over six components (real trades, rested scouts, observation count, band
width, race forecast, two-sided book) and buys two things:

* distance: below 0.50, the whole price window drops 1-2 ticks BELOW the real
  touch, so somebody else's money must be eaten before ours;
* size: the dollar cap and the rung size both scale with the score.

Below 0.15 nothing is placed at any price.

**What the numbers actually say about the standoff.** Reward score decays by
the program's discount factor per tick from the best price, and df is 0.3 in
most of these markets: one tick back keeps 30% of the score, two keeps 9%.
Worse, the scoring window walks from the best price and stops at Target Size,
so if the depth AHEAD of you already exceeds Target Size you score exactly
zero however close you are. In a deep farmed book the standoff therefore earns
nothing and the deal test rejects every price. It only pays in a specific
shape: a thin touch with the deep size sitting BELOW where we rest.

That made the first version worse than what it replaced — it silently stopped
entering markets. So the owner's second lever is the fallback: when the
standoff comes back empty, the scan re-runs at the touch on half the size,
CAPPED AT THE TOUCH. Without that cap the fallback reached above the touch and
the least-understood markets got the most aggressive bid on the board; a
400-case randomised invariant now enforces that a low-confidence market never
bids above the touch by either route.

### 2026-08-16 — prober is off the primaries (SHIPPED)

Owner: "Do not probe the primaries!" `auto_probe` now filters `_is_primary`
out of its market list, and scouts already resting in one are pulled
immediately rather than waiting out the 30-minute TTL — a primary can settle
inside that window. Primaries stay open to the QUALIFIER, which rests token
size at the floors to collect the pool; what they are closed to is the
prober, which is trying to get filled.

- **Negative risk.** Owner wants the concept incorporated — remind them.
  In a mutually exclusive event set, holding No on every outcome (or Yes
  across a complete set) caps the downside, because at most one can
  resolve Yes. Worth working out how it changes the earner's worst case,
  which is currently priced as if every position could lose in full.

1. Cancel leftover Ralph Norman ask (enwc-ussep-sc-2026-08-11-rep-ralnor,
   10sh @29c) — primary already happened; frees $7.10. Owner said include in
   next cleanup.
2. Longshot-side caps were never model-checked (only favourite BUY caps
   were). Overnight fills lost ~$19 on ID senate rep asks at 83c vs a 99.9%
   model; live ID senate caps are hand-set BUY 81 / SELL 83 and unchanged.
3. Existing orders resting above model fair in FL/KS/NH survived the cap
   lowering (caps don't move orders). Repricing them = manual, owner awake.
4. Event-survey 1c-bid filter bug (skips quotable sides whose best bid is
   1c) — hides the cheapest WNBA entry.
5. Aug 12 payout (~lands Aug 13/14) tests the flat-payout hypothesis and
   measures the cost of defender/keeper being off since ~1pm.
6. estimator_check.yml grades estimate vs payout daily; silver fetch 08:10 ET,
   ladder report 08:40, race screen 08:45 (all read-only).

## Where things live
- Monitor + dashboard: live/monitor.py, served on DO from `deploy` branch.
  Pages: / (dashboard), /map (map + switches + per-order controls + books).
  All writes via /maction (auth + CSRF).
- State: `live-state` branch, state.json (gzipped; single forced commit).
  state["auto"] = the owner's switches. SLIM_EXCLUDE only drops "series".
- Data: data/rewards.csv (payouts; PENDING→PAID), data/fill_history.txt
  (full transaction log), data/health.txt (ghost census, dupes, BP),
  data/silver_* (Nate Silver model series + screens), data/estimates.csv.
- silver_model.py maps Silver Bulletin per-race CSVs (Senate kNspD,
  Governor N13WX, chamber KQI8W et al) onto slugs; fetched daily by Actions
  because this session's egress blocks static.dwcdn.net.
- Workflows: read-only (health, fill_history, cbb_survey=event survey,
  silver_*, estimator_check, liquidity-rewards tracker) vs order-touching
  (merge_buy_rungs, add_thin_sides, dedupe_orders, thin_out, requalify,
  maint_restore, enter_* ... all push-path/dispatch only, never cron).
- Caps-vs-model reference page (artifact):
  https://claude.ai/code/artifact/95365720-2d1c-4641-b948-5871dca83699
