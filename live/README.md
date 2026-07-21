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
   - `GITHUB_TOKEN` — so the counter survives redeploys (below)

### The GITHUB_TOKEN (keeps "earned today" from resetting)

Every code update redeploys the server with a fresh disk. With this token the
monitor saves its counter to a `live-state` branch of this repo every ~2
minutes and reloads it on boot, so a redeploy costs at most ~5 minutes of
counting instead of the whole day.

On your phone: GitHub → **Settings → Developer settings → Fine-grained
tokens → Generate new token**. Repository access: **only this repo**.
Permissions: **Contents → Read and write**. Nothing else. Copy the token into
the `GITHUB_TOKEN` variable on your hosting app. (Without it, everything
still works — the dashboard just notes "saves: local only".)
6. Tap **Create App**. In a couple of minutes you get a URL like
   `https://liquidity-rewards-xxxxx.ondigitalocean.app`.
7. Open it on your phone, enter any username + your `DASH_PASSWORD`, and
   add it to your home screen. Done.

(Railway.app works the same way — connect repo, add the three variables,
~$5/mo — if you prefer it.)

### Phone notifications (optional, free — ntfy)

1. Install the **ntfy** app (App Store / Play Store).
2. In the app, tap **+ Subscribe to topic** and enter a long random name
   nobody could guess, e.g. `wf-rewards-k93jx2rq8v`. (The topic name acts as
   the password — anyone who knows it can read your alerts.)
3. Add the same string as a `NTFY_TOPIC` environment variable on your
   hosting app.

You'll then get pushed:

- your overall earning rate dropping **10% below what the app last showed
  you** — and again at every further 10% step — until you open the dashboard,
  which resets the baseline to the current rate;
- any market that was making **more than $1/day going to $0** (including its
  order disappearing from the book);
- plus two safety alerts: a reprice that failed verification, and the
  monitor being unable to fetch data for 10+ minutes.

The dashboard footer shows "alerts: ntfy" when active.

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
