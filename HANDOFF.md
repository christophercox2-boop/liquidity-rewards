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
