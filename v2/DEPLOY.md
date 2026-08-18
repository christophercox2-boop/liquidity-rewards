# Shipping 2.0 — what happens and what to check

One page for the deploy that puts 2.0 in the container next to 1.0.
2.0 ships with the engine included but **everything that can place an
order sits behind the master switch on /v2/switch, which starts OFF**.
Until you arm and confirm it (two taps), 2.0 watches and measures only.

## What changes when this branch reaches the deployed branch

- The container starts through `launcher.py`, which runs **both**
  processes: 1.0's monitor exactly as before (same port, same pages,
  same switches), and `python -m v2.main` beside it. Either one dying
  restarts by itself.
- 1.0's dashboard gains one route: **/v2** — 2.0's page. Same password,
  and a phone that is already logged in to the dashboard is already
  logged in to /v2.
- The image finally contains `scan_markets.py`. 1.0 imports it for golf
  tournament discovery inside a silent try/except, so this discovery
  has never actually run on the server; after this deploy it will.
  Discovery only — placing anything stays behind the switches, all of
  which survive the deploy in saved state.
- No new secrets or env vars. 2.0 reuses POLYMARKET_KEY_ID /
  POLYMARKET_SECRET_KEY, DASH_PASSWORD, GITHUB_TOKEN and NTFY_TOPIC.
  (Optional: `V2_ENABLED=0` turns the 2.0 process off entirely.)

## After the deploy, from the phone

1. Open the dashboard as usual — everything should look exactly the
   same. That is the main check.
2. Open **/v2**. You should see "2.0 — read-only", a green live dot,
   and an earned-today figure that starts from $0 and begins climbing
   within a minute or two.
3. If /v2 says "2.0 is not running in this container": 1.0 is fine and
   unaffected; the launcher's logs (DigitalOcean → Runtime Logs) say
   why 2.0 didn't start.

## What 2.0 does with the switch OFF (the state it deploys in)

Every 30 seconds it reads the same open orders 1.0 is managing, keeps
its own books (WebSocket + rotation), tracks reward terms with change
alerts, and integrates ONE earned-today number — sampled on its own
clock, never woken by order activity, no correction factor. State
(including the switch) survives redeploys on the `v2-state` branch.

Let this run a few days: compare 2.0's number against 1.0's and, two
days later, against the actual payouts in `data/rewards.csv`.

## The seats test (when you're ready — two taps)

Open **/v2/switch**, tap ARM, tap CONFIRM. From then on the engine
works the two seats families only, under the **$100 ceiling**:

- **Where**: near the touch where the Silver seat model and the market
  agree; 1-share scouts where they disagree (the tails, and all House
  rungs — no per-district model exists for the House ladder).
- **How much**: every placement fits inside $100 of capital at risk,
  shown on the switch page as used / ceiling / headroom.
- **Sell side**: anything that fills is relisted as an ask at
  max(break-even + a tick, the ask touch) so it earns while it waits.
- **Exits**: a market whose program stops paying, or that resolves
  today, gets our orders pulled.
- **EXP-1**: every placement where the window-boundary readings
  disagree records both predictions, pooled for grading against
  `rewards.csv` — small payouts included.
- Repricing is always place -> verify by order id -> cancel; the
  modify endpoint does not exist in this codebase.

One tap on TURN OFF stops all placement immediately. Every flip is
logged and pushed to your phone. If a new build ever boots with the
switch on, you get one push saying so.
