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
- DigitalOcean rebuilds the app on EVERY push to main — including the
  tracker's own "Liquidity rewards check" commits and [skip ci] does not
  stop it. A tracker that runs a check on boot therefore restarts itself:
  boot → check at +2min → commit → rebuild → boot, one lap every ~3.6
  minutes. It ran from 17:30 ET Aug 18 (ten minutes after the first
  one-container deploy) to 21:43 ET — 68 laps, v1 AND v2 restarting
  together — and looked like memory pressure until the boot times were
  laid beside the commit times: they matched one to one, ~70s apart.
  Fix (Aug 19): tracker_loop waits out the remainder of TRACKER_INTERVAL
  since main's newest STATUS.md commit before its first pass, so a boot
  resumes the hourly cadence instead of resetting it. Don't add anything
  that commits to main on a boot path without the same guard.
  Second fix, same night: the DO app tracks the `deploy` branch again
  (owner flipped it back 21:55 ET Aug 19). Releases are now an explicit
  `git push origin origin/main:deploy` — merges and data commits to main
  no longer restart anything. Keep deploy a fast-forward of main; if the
  push refuses, someone released out of order — reconcile, don't force.
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

### 2026-08-17 — the bottleneck was the search budget, not the universe

Owner: "there are a lot of juicy markets out there... what is a way to
eliminate the bottleneck". The universe widening the day before took the
earner's candidate list from 40 markets to 225 and changed nothing, because
the placement loop spent the budget in candidate order and `break`ed the
moment it was full. Measured on the board, from real files on disk:

- 181 markets in the newest `data/books_log.jsonl` snapshot; every one has an
  active program in `data/new_pools.json`.
- 93 of those 181 are priced by the Silver model (35 senate rows + 36 governor
  rows in `data/silver_*.csv`). Model coverage is NOT the bottleneck.
- `EARN_TOTAL_USD` = $100 of allowed worst case, `EARN_MAX_USD` = $6 a market.
  That is the number that decides how many markets we can be in.

Two changes, both in `auto_earn`:

1. **Entry is an auction.** Every candidate is priced first and ranked by
   `est / cost` — income per dollar of worst case — and the budget is spent
   from the top. Cheap markets win on this measure for a real reason: reward
   score is `df^ticks x size` and does not care what a share cost, while
   worst case is `price x size`. A 3c market and a 40c market with the same
   size score the same and risk 13x apart.
2. **Displacement.** When the budget is full, a candidate worth
   `EARN_DISPLACE_RATIO` (1.6x) more per dollar than the weakest non-graduated
   holding takes its place, subject to `EARN_DISPLACE_MIN_AGE` (30 min on the
   book) and `EARN_DISPLACE_PER_POLL` (2). Rotation still runs on its timer as
   the backstop; displacement only fires when something better is actually
   waiting. Graduates are never displaced — they are off the search budget.

The turned-away candidates are published as `earn_caps.waiting` and listed on
the /map earner card, best first, with what each would earn and why it did not
get in. That list IS the bottleneck, priced.

The budget itself is now a dial the owner can reach: `state["earn_budget"]`,
moved by `{"op":"budget","dir":"up"|"down"}` in `$EARN_BUDGET_STEP` steps up to
`EARN_BUDGET_MAX` ($500). The client sends a DIRECTION, never an amount — the
server owns the step and the ceiling. Raising takes two taps, lowering one.
Moving it places nothing by itself; the earn switch still has to be on and
every rule still applies.

### 2026-08-17 — the 2028 pool scope question is SETTLED: per event, not program-wide

The Aug-15 payout landed (written 08-16 22:55–23:00 in five commits) and it
decides the question STATUS.md had been flagging. The two predictions and what
arrived, for the day:

| family | program-wide est | per-event est | actual Aug-15 |
|---|---|---|---|
| nominee-2028 | ~$108/day | ~$400/day | **$683.74** |
| winner-2028 | ~$140/day | ~$310/day | **$412.29** |
| party-2028 | ~$4.35/day | ~$130/day | **$147.55** |

Program-wide is wrong by 6x, 3x and 34x. Per-event is right to within 1.1–1.7x
and errs LOW. The exchange's program sheet ("Daily, per event", $1,000 per
event) is correct and `_daily_pool`'s `/ (pool_n or event_n)` divisor should
not apply to the 2028 slate.

Aug-15 is still PARTIAL: 95 of an expected ~182 rows. The slate is complete
(31 nominee + 27 winner + 2 party rows, identical counts to Aug-14); the
senate and governor rows have not landed yet. Do not read Aug-15 senate
($9.36) or governor ($17.06) as real — they are unwritten, not zero.

Aug-15 is NOT an accumulator bucket, whatever `accum_day` says. Every earlier
day appears in a burst ~1–1.5 days late, fills over a few fetches, then
freezes: 08-13 froze at 147 rows/$223.24, 08-14 at 182 rows/$274.92. The
`accum_day` heuristic (all-PENDING + `days_since >= 2`) misfires here.

**APPLIED 2026-08-17.** Every divisor now prefers `event_n` over `pool_n`:
`_daily_pool` and `_score_order` in track_rewards.py, `_earn_scan`'s
`per_side_pool` and the `/map` `probe_meta.per_side` in monitor.py. `pool_n` is
still computed and still written to live_raw.json — it is a diagnostic now, and
`scope_x` (pool_n / event_n) records how far the old reading was out per market.

60 of 181 programs changed value; the other 121 are untouched, which is why the
race families reconciled at ~100% throughout. The headline rate goes from
~$522/day to ~$987/day on the same book — that is the fix, not new earnings.

The proof is arithmetic, not a fit: **35 markets were paid more on Aug 15 than
the old convention says their entire daily pool contained.** The party pair took
$147.55 against an old ceiling of $33.33 for both sides and every participant
combined. Under per-event no market exceeds its pool. (`t_scope.py` runs this
check against the real live_raw.json and rewards.csv.)

Two behavioural consequences of the corrected numbers, both intended but worth
watching:
- Slate markets clear `EARN_GRAD_MIN_RATE` far more easily, so they graduate
  off the search budget onto the $150 graduate budget faster.
- The deal test (`est >= 0.5 x worst case`) passes at prices it used to reject
  there, and the yield auction now ranks slate markets near the top.

**Still blocked, and it is now the expensive one:** `MAX_UNBACKED_BID_C` = 15c.
Silver prices no party-control market, so `ewc-usp-party-2028-11-07-*` is
"unbacked" and the earner may not bid above 15c — while the books touch at 36c
and 53c. Those two markets are the richest on the board at $500/side/day each.
The cap is the guard that stopped the NM Senate 10c purchase, so do NOT just
raise it; the market needs a model or an explicit owner exception.

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

### 2026-08-16 — pull the rest on a fill (owner)

"If someone fills me, might as well pull the rest, and then evaluate. See if
something is moving. Get info. Then see whether the confidence level justifies
going back in at a smaller amount or if it's best to back out and probe some
more."

On a CONFIRMED earner fill the earner now cancels its other resting orders in
that market. One fill says a taker was willing to come to our price; the other
rungs sit at prices no better informed than the one that just got hit, so
leaving them out is choosing to be filled again before learning anything.

Only the earner's OWN orders — the qualifier's floor bids, the keeper's rungs
and anything placed by hand are not its to cancel.

The rest of the owner's sequence was already in place and is worth recording
so it is not rebuilt: the prober is NOT locked out by an earner fill
(`fill_ts` is set on prober fills only), so it goes and gets the information
while the earner stands off for EARN_FILL_COOLDOWN (2h). Re-entry is smaller
by construction — a fill resets the rung to EARN_START_SHARES (5) — and is
gated by `_earn_confidence`, which is exactly "whether the confidence level
justifies going back in at a smaller amount".

### 2026-08-16 — the sniper sells inventory before shorting (owner)

"You can add the shares from the sniper to the flipper pool."

The sniper crosses into over-priced bids on the 2028 longshots and had
`ORDER_INTENT_BUY_SHORT` HARDCODED — so it opened a short even in markets
where we were already long. Same trade and same price either way, but a short
ties up (1 - price) per share of buying power and an inventory sale ties up
nothing. It now sells from stock when the position covers the size, which is
what makes the sniper and the flipper draw on one pool instead of the sniper
shorting beside inventory the flipper was trying to sell.

ANSWERED and BUILT (owner, 2026-08-17: "yes, what I mean is sell short bids").
The sniper's shorts are now closed the way the flipper closes longs, mirrored:
the flip sells stock we HOLD as an ask, the close buys back stock we OWE as a
bid, using ORDER_INTENT_SELL_SHORT which closes a short and rests as a BID.

Queue is `_EARN["toclose"]`, persisted as `earn_toclose`. Same guards as the
flip loop, because it can go wrong the same ways: bounded by the actual SHORT
position (a negative netPosition), minus buy-backs already resting, minus what
this pass placed; one order per market per pass; dropped after
EARN_FLIP_RETRY. It also never pays at or above the sale price — the buy-back
exists to realise the profit — and joins a bid that sits between our target
and that ceiling.

One thing that had to change with it: a SELL_SHORT rests as a BID, so the
off-model sweep saw it as a buy and judged it with `_bid_allowed`. It would
have cancelled every buy-back the moment the price sat above model fair, which
is precisely when we most want out, and the close loop would have re-placed it
— the same fight the 2028 party flips were losing. The sweep now skips
SELL_SHORT outright: closing a short reduces exposure, so the bid cap has no
business judging it.

### 2026-08-17 — the earner's universe was the prober's journal (FIXED)

Owner: "there are a lot of juicy markets out there for the probe/earner to get
into. What is a way to eliminate the bottleneck so that we're in more markets
where money can be made."

MEASURED, not guessed. The earner's candidate list was
`{l["m"] for l in probe_log}` — and `_probe_log` keeps only the last 200 lines
(`del log[:-200]`). So the earner's entire world was whatever markets the
prober had touched most recently, and a burst of events in a few markets
evicted the rest. On a 225-market board with the prober having touched 40, the
earner could consider 40. It now considers 225.

WHY THE COUPLING WAS UNNECESSARY. The prober visit stood in for "we know
something here". Since the Silver lookup was fixed (see above) we know
something about every modelled race with or without a scout: an unvisited
Texas Senate dem prices at 51-56-62c and scores 0.25 confidence off the
forecast plus a live two-sided book — comfortably over the 0.15 floor. Nothing
downstream was relaxed; every market still faces the confidence floor, the
model price cap, the overpay payback, the deal test, Target Size and the
dollar caps. The change only decides which markets get ASKED.

Cost checked before shipping, because not checking is what caused the 504: a
full 225-market scan is 47 ms, 0.2% of one 30-second poll.

THE NEXT BOTTLENECK, measured over the 142 modelled race markets with a spread
of realistic book shapes — 14% would place, and what blocks the rest:

     74  the side is under Target Size   <- 52%, and it pays NOBODY
     31  deal test (income too small for the worst case)
     17  penny ceiling / the 1000-share queue rule

So the single biggest remaining lever is not the earner at all: it is the
QUALIFIER. Half the board cannot pay us anything until the side reaches Target
Size, and the qualifier exists precisely to close that gap with 1c/99c orders.
Turning it on converts those 74 markets from unpayable to payable; the earner
then has somewhere to rest. The other 48 are the value guards doing their job
and should not be touched.

### 2026-08-17 — "Flip it": donate a hand-bought position to the flipper

Owner: "occasionally I'll buy some shares I think are mis-priced by hand.
Give me the option on the since you last checked to donate those to the
flipper to make some money back."

A "Flip it" button on every BOUGHT row of the since-you-last-checked list on
the homepage. Two taps, and the first says exactly what will rest — "Tap again
— rest 40 at 10.0c". It calls `stopPropagation` because the row itself opens
the market sheet.

`do_donate_flip` puts the job on the SAME `_EARN["toflip"]` queue the fill
path uses, so it inherits every guard already on it — position-bounded, one
order per market per pass, dropped after EARN_FLIP_RETRY, never selling more
than we hold. Two things are specific to a donation:

  * the size is checked against the LIVE position at donate time — net long,
    minus inventory asks already resting, minus anything already queued — so a
    mistake is refused on the spot with a reason instead of being silently
    trimmed to nothing half an hour later. Asking for more than is free
    queues the free part and says so;
  * the job carries a 5th element, `"owner"`, and a tagged job is EXEMPT from
    FLIP_SKIP_PREFIXES. Automatic flipping is banned in the 2028 party markets
    because those positions are the owner's own — a donation is the owner
    saying to sell this one. Re-adoption now accepts `len(j) >= 4`.

### 2026-08-17 — /hunt: worst prices on the board, worked BY HAND

Owner: "set up a big sniper with the worst positions you can find so that I
can go after them by hand. Give me a button to press for me to tell the
program to clear the area so I don't buy my own shares."

`/hunt`, linked from the map nav as "Worst prices". It PLACES NOTHING — the
automatic sniper stays as it was, small and narrow with its own switch. This
is a ranked list.

`hunt_targets()` walks every cached book and reports resting orders far from
model fair: a BID above fair is someone paying too much (we could sell to
them), an ASK below fair is someone selling too cheap (we could buy from
them). Edge per share, value = edge x the size actually there, sorted by
value. Defaults HUNT_MIN_EDGE_C 5c, HUNT_MIN_USD $1. Silver first; a market
without a forecast is only included when the posterior is TIGHT (<=6 ticks)
and built on at least one real trade — a wide guess is not a basis for telling
the owner to attack. Built entirely from caches, because it is a web request.

OUR OWN SIZE IS SUBTRACTED FROM EVERY LEVEL. A level that is entirely ours
disappears from the list; a level that is half ours reports only their half.
Without that the list would cheerfully point at our own qualifying stacks.
Each card also states how much of ours is resting in that market, and at that
exact price.

"Clear the area" cancels EVERY order of ours in that market — loop orders,
qualifier floors, keeper rungs, and the owner's own. The usual "automation
never touches the owner's orders" rule is inverted here on purpose: the owner
is the one clearing the room. Two taps, and the first tap says how many orders
will go. Then `state["hunt_hold"][market]` keeps every PLACING loop out for
HUNT_CLEAR_HOLD (30 min) — earner, prober, keeper, qualifier and sniper all
check `_hunt_held` — so nothing wanders back in behind them. Cancelling is
still allowed during a hold; that only ever helps.

### 2026-08-17 — /map 504: a web request was doing a blocking CDN fetch

Follow-on from the blank page above. With the error reporting fixed, the page
stopped hanging and started SAYING what was wrong — HTTP 504, a gateway
timeout, not the 500 I had assumed.

Root cause: `_map_payload` opens with `_silver_races()`, and on a cold cache
that fetched two Datawrapper sources INLINE, each with a GitHub and a disk
fallback at up to 20s apiece. `_silver_races` is reached from `_silver_fair`,
which the guards, the sweep and the earner all call — so it sits on the
request path. After every deploy the caches are cold, and the first person to
open /map paid for the whole fetch and got a gateway timeout instead of a
page. A web request must never do that.

`_silver_races()` now NEVER BLOCKS: it returns whatever is cached, even if
that is nothing, and kicks a background refresh with an in-flight guard so
fifty callers start one fetch, not fifty. `_silver_refresh` swallows
everything and always clears the flag — leaving it set would mean no further
refresh ever. An empty table means the guards fail CLOSED onto the no-model
ceilings, which is the right way to be wrong while the model loads.

The page also stopped lying about which fault it was: 502/503/504 come from
the gateway and now read "did not answer in time — busy or restarting", with
a quiet retry (4s, 8s, 12s…) since a cold start clears itself; only a 500 is
reported as the payload failing to build. Saying the wrong one sends the next
person looking in the wrong place.

### 2026-08-17 — /map blanked on "loading…" — MY BUG, and the real lesson

Owner: "this is happening again." The page showed its header and
`loading…` and nothing else.

Cause: I had just added `watched_h` to the /map payload and computed it with
`float(l.get("ts"))` over probe_log rows. `ts` is a HUMAN string —
`"08-17 09:06:12 AM"` — so float() raised, /map.json returned 500, and the
page's `r.json()` threw unhandled. probe_log rows now also carry `ts_s`, a
real epoch, and `_watched_h()` reads only that, ignores rows without it (older
rows predate the field), and cannot raise.

The lesson is the second fault, not the first. The card renderers had been
isolated for a while — but everything AROUND them was not, so one unexpected
field anywhere in /map.json blanked the page, and a phone has no console to
read. Fixed in two places:
  * `load()` catches a failed `r.json()` and says the monitor returned HTTP
    N instead of data, so a server-side problem is distinguishable from a dead
    monitor;
  * `render()` is now a try/catch wrapper around `renderInner()`, so whatever
    managed to draw stays on screen and the status line names what broke.
Both are covered by t_mapload, which drives the real page against a 500 and
against a payload missing `states`/`counts`.

### 2026-08-17 — "nothing new" now says nothing new SINCE WHEN

Owner: "when I check rewards, when it says there is nothing new, just print
the date of the last line so I can verify I didn't miss anything."

`_rewards_once` records `TRACKER_STATUS["latest"]` on EVERY run — the last
line's date, how many rows carry that date, and the total row count — and the
no-change message reads: "checked in 8s — no new reward rows. History ends
2026-08-16 (4 rows that day, 1,532 in total)." It matters beyond convenience:
a silently stale fetch would otherwise produce the same reassuring "nothing
new" as a genuinely up-to-date one.

### 2026-08-17 — being outbid is not a verdict, and what "ruled out" means

Owner, in three parts: "a lot of the markets the prober has ruled out are ones
where it just got outbid. More examination might still find a fruitful
position"; "the markets that should be ruled out are those that are so
volatile that getting filled at bad prices outweighs the potential benefits";
"because you want to compete, just not in a way that is going to get
exploited."

WHAT WAS WRONG. The /lab verdict docked a market up to 0.4 for being outbid —
comparable to the penalty for a FILL — which dropped contested markets into
"Not worth it". That was incoherent with the model right next to it:
`_bayes_fair` treats an outbid as evidence fair value is HIGHER (someone's
real money is bidding above us). One half of the system read it as
information, the other as a black mark. And behaviourally nothing happened:
the beaten scout sat out its full 30-minute TTL at a price the touch had
already passed, holding one of the market's three slots while testing nothing
— "nobody took it at 6c" says nothing once the best bid is 8c.

RULING OUT is now the owner's test, computed rather than felt:

    cost    = what fills here have lost against fair, per day
    benefit = the reward income on offer, per day
    ruled out  <=>  cost > benefit

`e["fill_loss"]` accumulates the SIGNED loss per fill — (px - fair) on a buy,
(fair - px) on a sell — so fills that went in our favour count as negative,
and a market that fills us WELL is not punished for it. It needs two fills or
a loss already past a day's income, since one expensive fill is not a pattern.
Everything else was removed from the verdict: none of it was evidence of
danger. Income is now scaled by the DRAG fills impose rather than by whether
any fill happened, so a nickel lost against $15/day is correctly noise.

Zones are: worth resting in / worth another look / fills cost more than it
pays. The middle one is deliberately not a rejection.

COMPETING WITHOUT BEING WALKED. Outbid now sets the market eligible for an
immediate re-scout into the NEW gap, and a beaten scout rotates at
PROBE_BEATEN_TTL (5 min) instead of 30 so the slot is freed. But the chase is
COUNTED: after PROBE_CHASE_MAX (3) consecutive outbids in a market we stop
jumping the queue for it and let it take its turn in the ordinary rotation.
Otherwise someone with a one-tick order walks us up the book a tick at a time
and leaves us holding the top — which is precisely the exploitation the owner
named. An hour of quiet (PROBE_CHASE_RESET) forgives the counter.

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

REVISED same day, owner: "all I want to see is newly added rows parsed but
otherwise raw. Then I can click a button and see a summary." So the DEFAULT
view is now the rows the reading actually appended to data/*.csv — split into
columns, otherwise untouched — and the computed summary sits behind a Show
summary button. `_tracker_once` diffs each append-history file as a SET of
lines (not by index) before and after the run, so a file that is rewritten
rather than appended still yields only genuinely new rows.

REWARDS ONLY (owner, 2026-08-17: "the only rewards I care about for the
button is the rewards.csv. Just run the program to update that"). The button
no longer runs the full pass. `_rewards_once` refreshes data/rewards.csv
alone: it seeds from main so the diff is against the COMMITTED state, calls
`tr.fetch_all_rewards` (one authenticated endpoint, no book fetching, no
STATUS.md rebuild), writes with the real `write_rewards_csv`, and commits ONLY
when rows actually changed — a push with no new rows is noise. Seconds instead
of a minute or two. The hourly wake still runs the full `_tracker_once`; the
loop tells them apart because `Event.wait()` returns True when the flag was
SET and False on timeout, and that has to be captured at the wait, since the
flag is cleared before the pass runs.

NO CAP (owner, 2026-08-17: "I'll need a lot more than 60 lines. I'll want to
see whatever is added no matter how long"). Neither the row count nor the line
length is limited — a shortened line is not the raw row. That is exactly why
the rows do NOT ride on data.json, which every open page refetches every 30
seconds: that payload carries per-file COUNTS only, and /track_rows.json
serves the rows once, when a reading lands. Each file renders in its own
scrollable pane with a sticky header so ten thousand rows cannot bury the
page. Tested at 901 rows with a 900-character cell, nothing dropped or cut.

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

### 2026-08-17 — the app fetches its own Silver model; the Action is optional

`fetch_silver.yml` has not dispatched since 2026-08-16 03:34 UTC (Actions
minutes / spending limit) and the copy of `data/silver_*_races.csv` on main
froze at 08-15 12:56. The monitor was already reading the CDN live every six
hours, so the TABLE was fine — but the moment a CDN fetch failed it fell back
to that frozen copy, and every guard built on the model went on arguing from
a two-day-old forecast with nothing saying so.

`_silver_fetch` now commits what the CDN returned back to main, so the fallback
is at most six hours old whether or not Actions ever runs again. Rules:

- Commits ONLY when the CDN answered AND the bytes differ from main. A failed
  fetch commits nothing — a stale fallback beats one overwritten with nothing.
- `SILVER["cdn_ts"]` is when the forecast itself last moved, as distinct from
  `SILVER["ts"]`, when we last looked at our copy. `/map`'s `model` block
  carries both (`cdn_age_s` and `age_s`) plus any commit error.
- Over `SILVER_STALE_H` (18h) without a successful CDN fetch, one ntfy a day.
  Never before the first successful fetch, so a cold start is quiet.

The workflow is left in place: it also pulls the four senate-WIDE series the
monitor does not, and it is the recovery path if the droplet loses CDN egress.
Both running is safe — the monitor commits only on a real change.

Note for whoever tries to verify this from a Claude session: the agent egress
proxy blocks static.dwcdn.net, so a curl from the session will fail while the
droplet is fine. Check `/map`'s model block, not your own network.

### 2026-08-17 — 2028 preference, and idle shares put to work

**Preference.** `PREFER_PREFIXES` (env-overridable, default the four 2028
families: both nomination slugs, winner, party control) sorts first in the
prober's scouting queue and in the earner's auction. Preference is ORDERING,
not permission — every rule still applies and preference never displaces a
holding on its own; the 1.6x yield rule still decides that.

The prober half is the part that does the work. The 2028 board has no Silver
forecast, so the only way a market there clears `EARN_CONF_MIN` is evidence our
own scouts gather. Putting it at the front of the prober's queue is what
eventually lets the earner in.

Dry run against the newest book snapshot, with the corrected per-event pools:
of the 60 2028 markets, **43 can be rested at the touch right now** and every
side is qualified (all hold 20,000+ against a 20,000 Target Size). 17 are
blocked by `EARN_PX_MAX_C` (10c), including both party markets at 36c and 53c —
the owner declined an exception for those on 2026-08-17.

The rich ones are thin books, not big ones: 5 shares at the touch in
`enwc-uspres-nom-dem-2028-micoba` estimates $10.14/day against 50 cents of
worst case. 43 markets at the starting rung costs about $21 of exposure, so the
$100 budget is NOT the constraint on this board — `EARN_MAX_PER_POLL` (4) is,
and that clears the whole list in about eleven polls.

**Idle inventory** — new loop `auto_inventory`, new switch `inventory`, OFF by
default like every other. Owner: "place sell orders on any of the shares I have
just sitting around... you won't get that much for them though so it may be
better to use them to earn."

It rests held shares that are not already resting or queued, as SELL_LONG,
post-only. Inventory costs no buying power, so the score is free — the shares
are already bought and already at risk. It is NOT a selling loop: a fill is a
side effect, not the goal.

`_ask_allowed` is the guard that matters. Where the best ask is below the
model's floor it rests AT THE FLOOR instead of joining the touch — it earns
less rather than giving the position away. Caps: 5 shares minimum, 273 an order
(the exchange's ask ceiling), 3 markets a pass, 20 minutes per market, and it
never touches a market `_hunt_held` has cleared for the owner.

**NOT built, deliberately:** moving EXISTING far-out asks closer to the touch.
The 99c stacks are the position (see the hard-won facts above) and they are
also what holds ask-side Target Size in the slate. Repricing them turns "will
never fill" into "might fill" AND can un-qualify the side, which pays nobody.
That needs its own decision, not a loop.

### 2026-08-17 — the penny ceiling is gone as a price cap

Owner: "the 10 cent ceiling doesn't make any sense." It didn't. It was
justified as keeping a total loss trivial, and that inverts the real risk:
buying Tennessee governor at 87c against a 99.7% forecast risks 0.26c a share
in expectation, while a 5c longshot the model puts at 2c risks 3c a share.

What was true underneath it is that expensive markets buy less reward score per
dollar — score is `df^ticks x size` and ignores what a share cost. That is a
RANKING question and the yield auction now measures it directly.

The census that settled it, from the newest snapshot: 93 modelled markets have
a live bid; 34 touch at or under 10c; of the 59 above it only 12 carried the
1,000-share wall, so **47 were blocked outright**, and 51 of the 59 have bid
sides already holding Target Size — they would have paid.

Four changes in `_earn_scan`:

1. `EARN_PX_MAX_C` no longer caps the price window. It survives as the level
   above which a LOSING fill must rest behind a wall.
2. The deal test prices the loss it insures against: `(1 - fair_mean/100) x
   stake` instead of the whole stake, with trust scaled by confidence so a
   market we cannot read still faces the old total-loss version verbatim.
   **This, not the ceiling, was what really excluded favourites.** It relaxes
   nothing for longshots — a 2c fair value means a 98% chance of losing the
   stake and the bar is unchanged.
3. The wall is required only where `edge_c < 0`. Below `EARN_PX_MAX_C` nothing
   changed and that is deliberate: the richest 2028 markets carry 24-33 shares
   at the touch, which is exactly why our size scores there, and a blanket wall
   test would have shut 25 of the 43 enterable ones.
4. `EARN_SAFE_MAX_C` 60 -> 95, MODELLED markets only. 49 of the 126 markets the
   owner armed for the defender allow BUY up to 95c, so a 60c stop on the
   earner contradicted the owner's own posture in the same races. Unmodelled
   markets are untouched, held at `MAX_UNBACKED_BID_C`.

**New guard, and it is not optional.** The scan never checked the ask side.
While the ceiling held the window under 10c almost nothing offered that low, so
it never bit; the first run of the favourite case after removing the ceiling
produced a 95c bid against a 90c offer, which post-only would reject outright.
The window now stops one tick under the best real ask.

Not built: a prior source for the 2028 board. Silver covers senate and governor
only, so every 2028 market is "unmodelled" and capped at 15c — which is why the
party pair at 36c/53c stays out of reach whatever happens to this ceiling. The
owner asked for a source; nothing has been chosen yet.

### 2026-08-17 — prober fund $200, and placing from the slate

**Info fund set to $200**, once, keyed `2026-08-17-owner-200usd` in
`probe_grants`. Owner: "make the prober budget just 200 dollars and don't worry
about adding to it. It looks like it will grow too anyways" — it does; probe
rewards are credited straight back into the fund. **This is the last scheduled
grant.** Do not add another that re-applies per poll: a grant that refills
faster than the prober spends is not a budget, which is why every one of these
blocks is one-shot and keyed by name.

**Order form on the market detail panel** the slate opens (`openMkt`). Same
/maction `place` route as every other order-touching control, so it inherits
the dashboard key, the X-Reprice header, the known-market whitelist, the
0.1–99.9c bounds and post-only. Price defaults to the touch on the chosen side,
from the book already drawn above it. Two taps: the first arms and states side,
size, price and dollars committed; the second sends. `t_slateorder.py` drives
the real page in node and asserts that one tap sends nothing.

### 2026-08-17 — owner-set fair values, the 2028 prior source

Silver prices senate and governor races and nothing else, so the whole 2028
board is "unbacked" and capped at `MAX_UNBACKED_BID_C` (15c) whatever else
changes. That cap is a refusal to guess, not an estimate. Owner: "I'll set the
fair value by hand for now. My numbers should not get the same weight as the
Nate silver model, but it can get us started."

`state["owner_fair"] = {slug: {"c": cents, "ts": epoch}}`, set from a chip under
each face on the slate. `_owner_fair(m)` reads it; `_any_fair(m)` returns
`(cents, source)` and **the forecast always wins** — a hand number stands in for
a missing model, it never overrides a live one.

Worth LESS than the model everywhere, deliberately:

| | Silver | owner |
|---|---|---|
| margin before a bid/ask is refused | 3c | `OWNER_FAIR_MARGIN` 6c |
| weight in the posterior | 1.2 | `OWNER_FAIR_W` 0.7 |
| window in the posterior | 1.5–6c | `OWNER_FAIR_WIN` 8c |
| credit toward confidence | 0.15 | `OWNER_FAIR_CONF` 0.08 |

What it DOES unlock: `_bid_allowed` / `_ask_allowed` bind to it instead of the
15c blanket, and `_earn_scan`'s hard ceiling becomes `EARN_SAFE_MAX_C` rather
than `MAX_UNBACKED_BID_C`. That is the whole point — without a number the board
is unreachable however good the book looks. The size taper still keys off
`sv` (Silver alone): it tightens around a real forecast and must not tighten
around a guess.

`op: "fair"` on /maction, audit-logged in Recent actions and the probe journal,
0.1–99.9c bounds, known-market whitelist, `cents: null` clears it. Places
nothing by itself — but it decides what the loops may pay, which is why it is
logged like an order.

The chip shows the distance from the midpoint (owner: "when I set the number
show me how far it is from the current midpoint"), live as you type and on the
tile afterwards: green under 4c, amber to 10c, red beyond, with "that is a long
way, check it" past 10c. `_slate_touch` puts the real bid/ask on each slate row
for it — bait-sized levels excluded, same as everywhere.

**Harness note.** Five test files broke on this because they stub namespaces,
and the fix was to exec the REAL `_owner_fair`/`_any_fair` into each against an
empty table rather than stub them. Stubbing is exactly what hid the Silver
uppercase bug for a day; do not stub these.

### 2026-08-17 — 2028-only filter on the market lists

One preference, `localStorage.only2028`, with a checkbox on both the Markets
tab (in `#catBar`, alongside the category chips) and the Positions tab (in
`#posSub`). Ticking it in one place applies in the other. `is2028()` in the page
names the same four families `PREFER_PREFIXES` names on the server, kept as a
single predicate so the two cannot drift apart.

**The trap, for whoever touches this next.** The Positions rows are rendered
with an index that `posTake(i)` and the qty boxes (`pq<i>`) use to reach into
`POSD` — and `posTake` PLACES AN ORDER. The first version mapped over the
filtered array, which renumbered every row: with the filter on, "Sell NOW" on
the first row would have acted on `POSD[0]`, a different market entirely. The
index is now looked up against the unfiltered array (`ALL.indexOf(r)`), and
`t_filter2028.py` asserts that the one filtered row still carries index 1.

### 2026-08-17 — odds totals on the slate, and re-scout on demand

**Totals.** Only one candidate wins a nomination, so the hand-set numbers across
an event should add to about 100c. They are typed one market at a time with
nothing tying them together, so the group total is the only thing that catches a
slate priced at 140c — every number individually plausible, the set impossible.
Each group heading now carries "your odds total N¢", green within 8c of 100,
amber to 25c, red beyond, and says which way it is off. Each face carries its
own number as a share of the group, so a slate adding to 140c still says what
each person is really being given.

**Re-scout.** `op: "rescout"` zeroes `_PROBE["last"]` for the preferred families
and nothing else, with a button on the prober card. It places NOTHING — it
clears a timer. The prober orders its queue by how long ago it last looked at a
market, so a board whose fair values just changed still waits its turn behind
markets nothing has changed about; this puts the 2028 families at the front
immediately. The reply says plainly when the Prober switch is off, because
otherwise a cleared timer looks like nothing happened.

Coverage maths, for expectations: `PROBE_MAX_PER_POLL` 5 at a 30s poll,
`PROBE_PER_MARKET` 3, `PROBE_ACTIVE_MAX` 140. Sixty 2028 markets wanting three
scouts each is 180, over the 140 cap, and it fills at 5 a poll — so roughly
half an hour to saturate, not minutes. Each scout is one share.

### 2026-08-17 — the re-scout note vanished (shipped broken, fixed same hour)

Owner: "I pressed the button and the status bar went away immediately." It did.
`rescout2028` wrote the confirmation into `#rescoutNote` and then scheduled
`load()`, and two seconds later `renderProbe` rebuilt the whole card from the
new payload, span and all. The page had already learnt this once — see `MSG`
in MAP_HTML, "results must outlive the re-render that a successful action
triggers" — and the new button did not use it.

The result now lives in `RESCOUT` (message, ok, timestamp) and `rescoutNote()`
re-emits it on every render for 45 minutes, with live progress appended: how
many 2028 markets have scouts resting right now. So the note answers "is it
working" rather than flashing "done".

**Harness lesson, worth more than the fix.** The first version of the test
assigned `DATA` directly and reported the bug still present after the fix. It
was not: the page's own startup `load()` resolved mid-await and replaced `DATA`
with `{}`, so `renderProbe` early-returned and `probeBody` was written exactly
once — the "identical snapshots" were the pre-press render three times over.
The stub now SERVES the payload from `fetch` and the test calls `load()` where
the page calls it. Any DASH/MAP test that sets `DATA` by hand has this trap.

### 2026-08-17 — the gap gate is gone, and the 2028 board runs off-budget

Four owner instructions, one commit.

**1. `PROBE_MIN_GAP` 3 -> 0.** Owner: "eliminate the gap limit. Obviously it is
more attractive the larger the gap, but that is just a factor." At 3 it excluded
79 of 180 markets outright (45 with no interior tick, 19 with one, 15 with two).
Width is now a SORT KEY in the prober's queue — wider first — not a filter.
Where there is no room between the touches the scout JOINS the touch: resting
behind it never fills and teaches nothing, while joining measures the one thing
a tight book has left to say, which is whether resting there gets you taken.

**2. The 2028 board is outside every budget.** `_earn_outstanding_usd` and
`_earn_graduated_usd` both skip preferred markets, the placement loop treats
their room as unlimited, they are never displacement victims, and the
graduation cap does not apply. A preferred market is no longer rationed against
the 2026 board.

**3. Per-market cap $15, growing to 3x with confidence.** `_earn_cap_usd`:
`EARN_PREF_USD` (15) x `1 + (EARN_PREF_GROW-1) * min(1, conf/EARN_CONF_FULL)`,
so $15 at zero confidence and $45 at full. The `cap *= qmul` confidence shrink
is SKIPPED for preferred markets — confidence is already in the cap, and
applying it twice would put a new market below the $15 the owner set as its
starting size. Every other market keeps $6 and the shrink.

**WHAT THIS COSTS, and nothing bounds it any more:** 43 reachable markets at $15
is $645 of worst case, against a $100 budget for everything else. At full
confidence the ceiling is $45 x 43 = $1,935. The earner card now prints the live
figure — "2028 board: $X at risk across N markets - outside every budget" — and
`earn_caps.pref_usd` carries it in the payload. That line is the check.

**4. The flipper is much more aggressive on the 2028 board.** `_flip_ticks` /
`_flip_step_after` / `_flip_loss_after` return preferred-specific values: sell
one tick over cost instead of two, step the ladder down every 5 minutes instead
of 30, stop anchoring to what we paid after an hour instead of a day. The
reasoning is the same as the off-budget change — we are there to rest, a fill is
the failure mode, and held stock ties up a per-market cap meant to be working.
`FLIP_SKIP_PREFIXES` is untouched: the party markets are still never flipped.

**Harness note, again.** Seven test files broke, all NameErrors for the new
helpers. Every one was fixed by exec'ing the REAL function from source into the
namespace, never by stubbing it. `t_offbudget.py` also read as an exemption leak
until the victims were given a real `est_day` — with `MONITOR.orders` empty
every holding yields 0 and any candidate displaces it.

### 2026-08-17 — "Sell below fair?" now has somewhere to be answered

Owner: "this is working but I don't see where to go to accept this proposal."
There was nowhere. The ntfy carried no buttons, and the advice it gave — "move
it to bid+1¢ on /map" — was a NO-OP in the exact case that triggers the alert:
a flip that has laddered down to the market's floor is already resting at
bid+1. That is the price it is stuck at.

**The reason it is stuck is worth knowing.** An ask AT the bid price crosses,
and every order this app places is post-only, so the exchange rejects it.
Moving a resting order can never reach the bid. Only `take_close` can — the one
deliberately aggressive, non-post-only path in the app. That is why this is a
decision and not a loop, and why the alert needed a button rather than better
wording.

`state["sell_queue"]` now holds each ask (market, qty, cost, resting price, best
bid, and the dollar loss against cost). `/map` renders it as a "💸 Sell below
fair?" card above the qualification card, with a button that names the size and
the price — "Sell 120 at 40¢" — and a "Keep it". `op: "sell"` takes only the key
and approve/deny: the size and price come from the queued job and the live book,
so a stale phone cannot sell more than was asked about. A failed take leaves the
ask on the queue rather than dropping it silently.

The notification now says what taking the bid costs and points at /map instead
of naming a price to move to.

**Shipped broken and fixed straight after.** Owner: "I'm still not seeing a
card." The queue was written INSIDE the once-a-day notify guard, so an ask that
had already fired — which is every ask you get a notification about — left
nothing to approve, and would not come round again for 24 hours. The queue is
LIVE STATE and the notification is an EVENT; they need separate conditions. It
is now rebuilt from the live test on every pass, with the dedupe applied only to
the ntfy, and `SELL_ASK_STALE` (15 min) drops any ask the loop stops
re-confirming — the stock sold, the position earning again, cash no longer
short — so the card clears itself rather than offering to sell what we no
longer hold. `t_sellask.py` asserts the ordering of the two blocks directly.

### 2026-08-17 — the prober was starving its own queue (my bug)

Owner: "reverse the order that the prober goes through the 2028 market. I think
some are getting left out." They were, and it was the `_width` key I added when
spread stopped being a gate. Width is STABLE and recency is not, so the widest
markets sorted to the front on every pass and the narrow tail never came up
while the scout slots were full.

Simulated on 12 markets with 3 slots over 8 passes:

| ordering | visits per market |
|---|---|
| width above recency (what shipped) | 5,5,5,1,1,1,1,1,1,1,1,1 |
| recency above width (the fix) | 2,2,2,2,2,2,2,2,2,2,2,2 |

Two changes. Width is now the tie-break BELOW `_PROBE["last"]`, which is what
"a factor, not a gate" was supposed to mean. And the sweep ALTERNATES direction
each pass (`_PROBE["sweep_rev"]`), each tier reversed independently so preferred
markets never fall behind the rest — reversing once would only have moved the
starvation to the other end, which is the same complaint a day later.

`t_prefer.py` now runs the real sweep block over 8 passes and fails if any
market goes unvisited, and separately asserts that the widest market does NOT
lead when it was just scouted.

### 2026-08-17 — the flip ladder was selling the best orders we own

Owner: "there are shares that got filled that are being flipped, especially in
the 2028 markets." They are, and the data reframes what a flip IS on that board.

From `data/live_orders.csv`: the 2028 board's SELL side earns **$369/day against
$191 on the BUY side — 66% of everything the board earns**. The top ask-side
orders are flipped fills of 45–61 shares making $22–24/day EACH. A fill there is
not the failure mode I assumed when I made the flipper aggressive that morning;
it is how we get onto the side that pays.

**The bug:** the ladder that steps a flip down toward the floor had NO earning
check. Its whole justification is idle capital — "waiting out a double that
probably never comes" — and an ask collecting $23/day is not idle. The
aggression added the same day made it fire every 5 minutes instead of every 30.
It now requires `not earning3`, like the other two decisions that give up price.
`t_flipaggr.py` asserts all three.

Self-cross check on the same data: 0 markets where our best bid is at or above
our own best ask. Nothing is trading with itself.

### 2026-08-17 — hand-set fair values are BLOCKING the 2028 bid side

Owner: "these markets seem to be left out because they don't seem to be earning
much at all." Not a bug — it is `OWNER_FAIR_MARGIN` doing exactly what it was
built to do. Every fair value on the slate sits 5–12c BELOW the midpoint, and
the bid cap is fair + 6c:

| | your fair | market mid | bid cap | |
|---|---|---|---|---|
| Ro Khanna | 2.0c | 13.5c | 8.0c | blocked |
| J.B. Pritzker | 2.0c | 14.5c | 8.0c | blocked |
| Jon Ossoff | 13.0c | 24.0c | 19.0c | blocked |
| Michelle Obama | 6.0c | 7.5c | 12.0c | reaches |

**13 of the 15 visible markets cannot be bid anywhere near the touch**, and a
bid 5–12c back scores `df^ticks` — essentially zero.

The owner's board is internally coherent (the "% of your board" figures imply
~123c across the full slate, normal for a nomination field). The market's mids
for the same 15 names sum to 3.5x the owner's numbers for those names. So either
the field is grossly overpriced or the estimates are systematically low.

**The trap worth knowing:** setting a LOW fair value makes a market less
reachable than setting NONE. With no number, `MAX_UNBACKED_BID_C` caps at 15c —
which for mids of 6.5–14.5c reaches the touch fine. With a 2c number, the cap is
8c and the market is shut. Clearing a fair value can therefore INCREASE what we
can earn there, which is the opposite of what anyone would expect.

## 2026-08-20 — the qualifier goes board-wide (the "unprobed markets")

The owner: "massive spread in the governor, senate, and slate markets where
there is definitely money to be made, but I'm not even probing it," then "Do
the unprobed markets first," then — on being shown the deploy plan — "don't
auto set for now, especially in families where I'm not familiar. The
existing systems should remain unchanged."

Diagnosis from the live state: 138 of 223 program-carrying US-politics
markets had NO book in the tracker's cache — `fetch_live_orders` only
fetches books for markets with orders, and `auto_qualify` only computed gaps
from that cache, so it could only ever act where 1.0 already was. A side
below Target Size in an OH/GA/CA governor race, a midterms-control slate, or
the 2028 presidential slate was invisible: it paid nobody, and nothing of
ours could ever see it.

What changed in `auto_qualify` (live/monitor.py):

* **Scope**: every market in `prog_terms` (the program watcher's whole-board
  snapshot) plus the tracker's cache — not just what happens to have orders.
  Hands-off (2.0's seats families, unwind markets, resolving today), econ,
  and anything resolving within `QUAL_MIN_DAYS_OUT` (2) days stay out.
* **Books**: the qualifier fetches its own (`QUAL_BOOKS_PER_PASS` = 6 per
  5-minute pass, least-recently-tried first, own cache — the tracker's cache
  evicts anything without orders). Whole board rotates in ~3h.
* **"New ground" never places itself.** A market whose book only the
  qualifier's own rotation has seen routes to the /map queue no matter how
  cheap — the tracker's cache covers exactly the markets 1.0 already works,
  so gating on it keeps the status quo flows (including the 2026-08-16
  far-dated/non-primary/≤$50 auto rule) unchanged. New ground also only
  takes EMPTY sides: a floor block behind someone else's quote scores
  `df^ticks` from THEIR best ≈ zero and would qualify the side for
  strangers.
* **Queue mechanics**: capped at `QUAL_QUEUE_MAX` (12) rows sorted richest
  side pool first (each row shows side pool $/day and days out), denials
  stick for 7 days (`qual_denied`), a placed side is not re-tried for 6h,
  and Approve re-checks against a book fetched AT TAP TIME.
* **Bug fixes that only bit at sub-cent ticks**: prices serialized `:.2f`
  (a 0.1c floor became "0.00") and the ask ceiling rounded to 2 decimals
  (1 − 0.001 became 1.0). Now `:.3f` with trailing zeros stripped, ceiling
  rounded to 3. NOTE: an empty book's tick is unknowable from levels, so it
  defaults to 0.01 — a 5,000-target side shows as $50 on the card; if the
  market's real tick turns out to be 0.001 the same side costs $5.

The stakes, measured from the live snapshot: 258 empty sides across 129
paying markets; if the scoring formula pays a lone floor block as written,
~$2,990/day gross (~$1,500–1,940/day at the measured 50–65% realization).
Whether it DOES pay a lone block is unproven — the first queue approvals
answer it for the cost of their collateral, graded by rewards.csv within
days. Verified with a stubbed-network harness driving the real state
snapshot: new-ground hold, status-quo auto path, redo guard, deny
stickiness, queue hygiene, sub-cent serialization, ask chunking under low
buying power. v2 untouched; its 210 tests still green.

## 2026-08-20 — college football win totals: the second family (v2/cfb.py)

Owner: "I like the football idea... max $1 per market... 5-10% per side on
average" / "Just make college football for now." Universe measured by the
survey: `aachc-cfb-wins-*` — 375 paying team-season win-total markets, every
one $25/day pool per team-event of 5 lines (side pool $2.50/day), Target
Size 5,000, df 0.5.

Fully separate by construction: its own switch (OFF by default, two-tap arm
on /v2/switch which now shows both switches), its own OrderDesk whitelisted
to exactly that prefix, its own BookCache and TermsStore, its own $1/market
budget. The seats engine and 1.0 cannot touch these markets and this module
can touch nothing else. Hosted inside the 2.0 process to spare the shared
box another Python process.

Behavior: only sides that already hold Target Size are entered (a tiny
order can't qualify a side, and topping one up gifts the pool to closer
quotes). Price ladder steps back from the touch; in junk-wall books it may
step in FRONT of the wall, capped 5 ticks clear of the other side's touch —
df 0.5 means a wall 1 tick back still scores half, so share only exists
several ticks in front. Size is the largest on a small grid keeping share
<= 10% (share_hi) and cost <= $0.50/side; with no opposing quote the spend
is clamped to probe money ($0.05). Game days belong to others: every
non-exit order is pulled Thursday 17:00 ET - Sunday 06:00 ET. Fills ping
the phone and the exit seller re-offers at break-even+tick. First tranche
capped at 40 markets (cfb_max via CfbConfig.max_markets).

Tests: v2/tests/test_cfb.py (11) through the real desk rails against the
fake exchange; whole suite 222 green. Switch page, status card, and orders
fold verified in a headless phone-width browser.

## 2026-08-20 — NFL futures family; the family engine generalizes

Owner: "Go ahead with NFL, but I'm seeing that a lot of these college
orders are being placed alone. I thought the idea was to place them behind
the touch because of the df. The collateral is low, so I wouldn't change
anything for now, but maybe going forward with the new families you can
model that way."

The college module became v2/family.py (Family + FamilyConfig, one engine,
one config per family; v2/cfb.py is now a shim keeping the old names and
the college behavior bit-for-bit — its `allow_improve` stays ON, which is
the documented reason some college orders rest alone in front of junk
walls). Every newer family sets `allow_improve=False`: join the touch or
rest behind it, never in front, so a side with no real competition is
skipped instead of colonized.

NFL futures (family.nfl): prefixes tec-nfl- (MVP/DPOY/OPOY/ROY awards,
division/conference/champ winners — 335 markets, ~$8/side/day, target
15,000, df 0.3), aqc-nfl- (makes-the-playoffs, 32 markets all measured
alive at $4.6-4.7/day), ftsc-/fptc-nfl- (586 season stat futures, books
unpriced at build time). Resting window Tuesday 06:00 -> Thursday 17:00 ET
(NFL plays Thu/Sun/Mon; preseason weekends too). Own switch (off), own
desk/whitelist/cache/terms, $1/market, share <= 10%, 40-market first
tranche. /v2/switch shows all three switches; status and orders pages
render each live family's card/fold.

Suite: 227 tests green (college's 11 unchanged on the shared engine; NFL's
behind-the-touch rule pinned: wall-only books skipped entirely, no plan
ever prices in front of the touch).

## 2026-08-20 early hours — two live fixes from the first family night

1. **The qualifier leaked into a 2.0 family.** The widened scan's sources
   include `tr._PROG_CACHE` — every market the ACCOUNT has orders in. When
   the owner turned the CFB switch on, its markets gained tracker books,
   which made them "known ground," and at 02:12 ET the qualifier
   auto-closed the ask side of `aachc-cfb-wins-2026-11-28-ala-8pt5wins`
   (4,552 at 99c, $45.52 collateral) under the far-dated/<=$50 rule. Fixed:
   the qualifier scan now requires `tr._is_us_politics(m)` — 1.0 is the
   politics app; the sports families are 2.0's alone. The stray order was
   left resting pending the owner's word (bounded $45.52, currently
   earning most of that market's ask-side pool).

2. **CFB repriced too eagerly and the box caught HTTP 429s.** First night:
   ~a dozen reprices per pass chasing 1-tick touch wobbles for +$0.02/day,
   each a multi-call place-verify-cancel; /v1/orders/open returned 429
   twice. FamilyConfig manners tightened: reprice_gain_day 0.02 -> 0.06,
   cooldown 30m -> 60m per market-side, actions 4 -> 3/cycle, books 8 -> 6.

Also learned: the "258 empty sides" claimable estimate was wrong in the
happy direction it hoped for — v1's missing books were CACHE gaps, not
exchange gaps. After the full sweep, exactly ONE truly empty new-ground
side exists (ewc-usse-ne-2026-11-03-dem, ~$4.17/day side pool, $20 to
claim at 1c) plus one known-market partial (ewc-usp-party-2028-11-07-rep,
~$50/day side, $192.43 to finish at 1c). The governor/slate books all
carry real quotes; presence there is an earner/prober problem, not a
qualification one.

Owner corrections, 2026-08-20 morning: (1) `season_start` on FamilyConfig —
no game-day pulls before the season plays (CFB Week 0 is Sat 2026-08-29, so
college's window arms Thu 2026-08-27; NFL preseason is already live). The
first Thursday-evening pull would otherwise have fired on a weekend with no
games. (2) max_markets 40 -> 400 ("a 40 market cap leaves out 90% of
what's available") — college can now cover all ~375 paying win-total
markets; ramp is bounded by 3 actions and 2 scan books per 60s cycle.

Owner, 2026-08-20: "I'm fine with the qualifier bringing sides of the
markets over their target size, I just need a list of where I'm exposed so
that I can get out if there is ever a risk of those positions becoming
impossible" — and "There should be no market limit."

* **Deep blocks card** on /map (`block_exposure()` in live/monitor.py):
  every resting order >= 100 shares at <= 2c (bid) or >= 98c (ask),
  whatever placed it, with $ locked, the live book, days out, and a danger
  read — AT RISK when the opposing touch is within 10c of the block (the
  market walking toward certainty on the side that fills it), watch within
  20c or resolution week. One-tap Cancel per row through the existing
  /maction rails. A high-priority phone push fires when a block first
  turns AT RISK, repeated at most every 6h per block.
* Family `max_markets` is now None (no limit); pacing, the $1/market cap,
  and the share band are the bounds.

Owner, 2026-08-20 midday: "Go through and cancel all the orders in markets
that recently lost their rewards program" and "limit the access to any sort
of automated probing or placing of orders on any markets without rewards."

* **cancel_dead_programs workflow** (.github/workflows/): fetches every
  resting order, batch-checks live programs with the same period-picking
  the estimates trust, cancels reward-seeking orders in markets that pay
  nothing, KEEPS position exits (the 2026-08-19 lesson), and aborts on a
  sanity rail if the API claims most of the board is dead. Report lands in
  data/cancel_dead_programs.txt. Push-path + manual dispatch.
* **1.0**: `_no_live_program(m)` folded into `_hands_off` — every placing
  loop (defend, snipe, probe, earn, qualify) now refuses markets known to
  pay nothing, in one place.
* **2.0 families**: the live-terms refresh also covers the scan's next ~20
  picks, and a candidate whose fresh terms read dead is dropped from the
  scoreboard before anything places. Seats engine and calibration probes
  already required a live pool.

Owner, 2026-08-20 afternoon: "More rewards are dropping. Can you make it a
continual scan" — cancel_dead_sweep is now a standing loop (every 10 min,
DEAD_SWEEP_EVERY_S). A market must read dead on TWO consecutive checks
before anything cancels (one API flake can't fire it), cancelled ids are
remembered so nothing double-fires, exits go too (owner's earlier word),
and the rails held: a partial mass-death reading (>70% of the board) holds
and notifies; a totally blank program response exits before judging.
Notify per batch; cumulative counts in state["cancel_dead"].

## 2026-08-20 — no estimate without a confirmed divisor

The owner spotted a market card reading "$1.50/day · max $23.30" where the
whole side pool is $1.61/day: "How could the max rate earned per day ever
approach what is stated here when the market only pays out a little over a
dollar." It could not. The card's own arithmetic showed why —
`$100 ÷ 2 ÷ 2 × 93.2% = $23.30` six minutes earlier vs
`$100 ÷ 31 ÷ 2 × 93.2% = $1.50` now. Only the divisor moved.

`event_n` resolves in three passes: the exchange's event/tag map (politics
only), then a count of the siblings we happen to know about, then a
definitive prefix search bounded to 10 new races per call. For a market the
tag map doesn't cover — every sports market v2's families place in, which
1.0 also scores — the middle pass produced 2 (the two orders we had just
placed) and the estimate ran 15x high until the search caught up.

Owner: "Just don't estimate until you have a grasp of everything you need
to know. If you miss a few seconds that is fine." So:

* `progs[slug]["event_n_ok"]` is set ONLY by the exchange's event map or
  the prefix search. Counting known siblings is a guess and never confirms.
* `_score_order` holds the estimate when the divisor is unconfirmed:
  est_day stays None (every consumer already reads that as unscored, so it
  leaves the rate, the market rates and the dead-order list alone) and the
  verdict reads "⏳ … holding the estimate until I know how many markets
  share this pool". The ⏳ prefix keeps it off the dead-order list, which
  keys on ✅/❌.
* Both earner sides refuse to enter on an unconfirmed divisor — that path
  is not cosmetic, it is the yield auction that decides which markets get
  the budget, and a low guess is exactly the one that wins it.

2.0 was already safe: the seats engine's sizes come from the politics event
map and the families' from the survey's real event membership.

Owner, 2026-08-20 late afternoon: "Don't hold the dead market scan. I don't
want to be in markets if there are no rewards." That answers the dry-run
question the scan had been asking since the race board went dark:

* `DEAD_SCAN_ARMED` now defaults to 1 — the scan cancels rather than
  reporting. `DEAD_SCAN_ARMED=0` parks it again without a deploy.
* The two-consecutive-readings requirement and the >70%-of-board hold are
  gone. Both existed to guard against partial or garbage program data,
  which track_rewards already prevents: a failed batch discards the WHOLE
  refresh and the previous cache stands, so the scan only ever sees one
  complete successful response. What remains is the requirement to HAVE
  data (orders, positions, a cache covering the order book).
* A batch that clears more than half the markets we hold orders in still
  says so in the push, but it acts first.

The trade the owner accepted, stated once: a wrong reading costs queue
position and a re-place, which the loops do by themselves; sitting in a
market that pays nothing is the worse side.
