# Owner preferences — read before doing anything

This file loads automatically in every session.

**Building version 2.0? Read REBUILD.md next.** It is the brief: what the
system does, what state each part is in, what is actually broken, and the
decisions already made about the rebuild. Start there, not in the code.

Working on the running 1.0? HANDOFF.md has the operational history — it is
long and accreted, so search it rather than reading it through.

## How to talk to the owner
- Plainly. No characterizing, no hype, no hedging language. Lead with the
  numbers and what happened.
- Verify claims against data before asserting them. If the exchange or a
  file can answer the question, check it first.
- The owner works ENTIRELY from a phone. No command line, no laptop.
  Anything the owner must operate has to work as: tap a link, tap a button,
  or edit a file in the GitHub mobile UI (the poke.txt pattern).

## How the app is built (owner's choices — keep them)
- Two repos. wfco223/Liquidity-rewards (private) holds everything.
  wfco223/welcome is a group-visible fork: NO tracker data, activity,
  balances, or market info ever goes there.
- STATUS.md is the phone-readable front page: one ✅/❌ freshness line up
  top, summary before detail, plain-English explanations of every number.
- The live monitor (live/monitor.py) runs on DigitalOcean from the `deploy`
  branch and only picks up code on restart. The /map page is the owner's
  control surface: tiles by state, per-order Move/Cancel, order book,
  new-order form, and the automation switches.
- Automation switches: NOTHING places orders unless the owner turned that
  loop's switch on from /map. Off by default, persisted in state["auto"],
  every flip audit-logged. Turning ON takes two taps; OFF takes one.
  Never add automation that places orders without such a switch.
- Order-touching endpoints keep: auth, X-Reprice CSRF header, known-market
  whitelist, 0.1–99.9c price bounds, post-only placement.
- Heavy or blocked-egress work (Silver CSV fetches, exchange surveys) runs
  as GitHub Actions workflows that commit results to data/*.txt — the owner
  reads the output files, not logs. Order-touching workflows trigger only
  by push-path or manual dispatch, never cron.
- Alerts go through ntfy; the topic name is a password.

## Scope and secrets
- Markets: US politics, plus only categories the owner explicitly asked
  about (some sports futures have been surveyed). NEVER econ markets.
- Secrets (POLYMARKET_KEY_ID, POLYMARKET_SECRET_KEY, DASH_PASSWORD,
  GITHUB_TOKEN, NTFY_TOPIC) exist only as encrypted Actions/env secrets.
  Never in code, commits, or output files.
- Never put the assistant model identifier in commits, comments, or any
  pushed file.

## Trading style
- The owner earns liquidity rewards by resting orders, not by trading.
  Preference: rest near the touch in LOW-volatility markets where fill
  risk is small. Fills are usually losses here, not wins.
- Positions and orders are real money. Before anything that places,
  moves, or cancels orders: say exactly what will change and get a yes,
  unless the owner already approved that specific action.
- When repricing: place the replacement, verify it rested by ORDER ID and
  minimum quantity, only then cancel the original. Never use /modify — it
  destroys orders (details in HANDOFF.md).
