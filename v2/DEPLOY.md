# Shipping the read-only 2.0 — what happens and what to check

One page for the deploy that puts 2.0 in the container next to 1.0.
2.0 in this phase **watches and measures only** — it has no code path
to an order endpoint, so nothing about this deploy can place, move or
cancel anything.

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

## What 2.0 does while read-only

Every 30 seconds it reads the same open orders 1.0 is managing, keeps
its own books (WebSocket + rotation), tracks reward terms with change
alerts, and integrates ONE earned-today number — sampled on its own
clock, never woken by order activity, no correction factor. State
survives redeploys on the `v2-state` branch.

The point of the phase: compare 2.0's number against 1.0's and, two
days later, against the actual payouts in `data/rewards.csv`. When the
number has proven itself, the engine phase starts — probe -> earn ->
sell on the two seats families, behind the master switch, under the
$100 buying-power ceiling.
