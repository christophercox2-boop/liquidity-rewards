# Live monitor — real-time "earned today" counter (~$5/month)

A small always-on server that checks your resting orders **every 30 seconds**,
scores them with the official reward formula, and adds up your estimated
earnings second-by-second — the way the exchange actually does it. You get a
phone dashboard with a big running **"Earned today: $X.XX"** number, the
per-market breakdown, and the last 7 days.

Everything it needs is in this repo (this folder + the `Dockerfile`).
No command line required — you deploy it by connecting this GitHub repo to a
hosting service from your phone's browser.

## Setup on DigitalOcean App Platform (~5 minutes, ~$5/month)

1. Sign up at **digitalocean.com** (needs a card).
2. Tap **Create → App Platform**.
3. Connect your **GitHub** account and pick the **Liquidity-rewards** repo,
   branch `main`. Leave "Autodeploy" on — future updates deploy themselves.
4. It will detect the **Dockerfile** automatically. Pick the cheapest
   **Basic** instance (512 MB, ~$5/mo).
5. In the app's settings, add three **environment variables** (mark them
   encrypted):
   - `POLYMARKET_KEY_ID` — same value as your GitHub secret
   - `POLYMARKET_SECRET_KEY` — same value as your GitHub secret
   - `DASH_PASSWORD` — any password you choose for the dashboard
6. Tap **Create App**. In a couple of minutes you get a URL like
   `https://liquidity-rewards-xxxxx.ondigitalocean.app`.
7. Open it on your phone, enter any username + your `DASH_PASSWORD`, and
   add it to your home screen. Done.

(Railway.app works the same way — connect repo, add the three variables,
~$5/mo — if you prefer it.)

## What you'll see

- **Earned today** — integrated in real time, resetting at midnight Eastern
  (Polymarket's reward day). This is the number that should track your actual
  daily payouts far more closely than any single snapshot.
- **Current rate** (~$/day) and every order's contribution.
- **Previous days** — each completed day's integrated total, ready to compare
  against what Polymarket actually pays for that day.

## Notes

- Same estimate assumptions as STATUS.md (pool ÷ race markets ÷ 2 sides);
  the difference is it samples ~2,880×/day instead of 24, so decay between
  snapshots — the gap you noticed — is captured instead of missed.
- A redeploy or platform restart starts the day's counter from that moment
  (state survives ordinary process restarts, not disk replacement).
- The hourly GitHub tracker keeps running independently — STATUS.md remains
  the permanent record and the failure-alert system.
