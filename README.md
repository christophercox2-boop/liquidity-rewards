# Polymarket Liquidity Rewards Tracker

Automatically records your [Polymarket US liquidity rewards](https://docs.polymarket.us/incentives/liquidity)
every hour and keeps a running history in this private repo.

## Setup (once)

1. **Get an API key** — on polymarket.us go to **Settings → API** and create a
   key. Copy the two values it gives you.
2. **Add them to this repo** — on this repo's GitHub page go to
   **Settings → Secrets and variables → Actions → New repository secret** and
   add both, with exactly these names:
   - `POLYMARKET_KEY_ID`
   - `POLYMARKET_SECRET_KEY`

That's it. It runs by itself every hour.

(It also runs immediately whenever anything is pushed to `main`, so any edit —
even to this README — kicks off a fresh check.)

## Checking it's working

Open **[STATUS.md](STATUS.md)**. That one page tells you everything:

- ✅ and a recent timestamp (under 2 hours old) → **working**
- ❌ or an old timestamp → **broken** (GitHub will have also emailed you)

It shows **"Right now"** — each resting order scored with Polymarket's
official reward formula (`DiscountFactor ^ ticks-from-best × size`, inside
the Target Size window), with a ✅/❌ verdict and your estimated share of
that side's score — then your total earnings, the last 14 days, monthly
totals, and top markets. The full history lives in
[`data/rewards.csv`](data/rewards.csv).

## Refreshing on demand (works on your phone)

The page updates hourly by itself. To refresh it *right now*: open
[`poke.txt`](poke.txt), tap the pencil (edit) icon, type anything, and
commit. That push triggers an immediate run — STATUS.md is fresh about a
minute later.

---

<details>
<summary>Technical details (optional reading)</summary>

- One script, [`track_rewards.py`](track_rewards.py), fetches your complete
  earnings history from the official Incentives API:
  `GET https://api.prod.polymarketexchange.com/v1/incentives/earnings`
- Auth: Ed25519 signature over `timestamp + method + path`, sent as
  `X-PM-Access-Key` / `X-PM-Timestamp` / `X-PM-Signature` — identical to the
  official `polymarket-us` SDK.
- Each run rewrites `data/rewards.csv` from the full history (idempotent — a
  missed run loses nothing), appends a heartbeat to `data/checks.csv`, and
  regenerates `STATUS.md`. A failed run writes the error into STATUS.md and
  fails the workflow so GitHub emails you.
- The schedule lives in
  [`.github/workflows/liquidity-rewards.yml`](.github/workflows/liquidity-rewards.yml).
- Run locally:
  `POLYMARKET_KEY_ID=... POLYMARKET_SECRET_KEY=... python track_rewards.py`
  (needs `pip install -r requirements.txt`).

</details>
