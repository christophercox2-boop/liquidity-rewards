# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-16 4:54 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$592.26/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — BUY at the best price, ~$23.15/day for 200 contracts. Runners-up: `ewc-usse-tx-2026-11-03-dem` (~$9.19/day), `ewc-usgub-oh-2026-11-03-dem` (~$6.40/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$592.26/day (~$24.68/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 60.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,227 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | BUY | 58.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,208 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-catlau` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 20.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (132,728 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (67,477 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | SELL | 15.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,226 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ma-2026-11-03-dem` | BUY | 27.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,201 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | SELL | 26.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (132,726 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimobe` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `usgubewc-usgub-il-2026-11-03-dem` | BUY | 34.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,208 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 56.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,206 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | BUY | 54.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,209 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-rep` | BUY | 46.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,203 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 40.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (197,978 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | BUY | 60.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,204 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-dem` | BUY | 60.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,204 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | SELL | 12.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,228 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 3 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 53.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,203 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `usgubewc-usgub-tn-2026-11-03-dem` | SELL | 47.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,229 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 67.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (210,290 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-madcaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | BUY | 47.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,208 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-rep` | SELL | 60.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (332,175 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | SELL | 14.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (70,476 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-dem` | BUY | 49.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (550,204 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tn-2026-11-03-rep` | BUY | 21.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (3,008 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 57.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,203 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ma-2026-11-03-rep` | SELL | 86.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,227 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| …and 551 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> BUY 1 @ 60¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 40¢ | 26 | ×0.1^20 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^58 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> BUY 1 @ 58¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 40¢ | 1 | ×0.1^18 = 0.0 |
|  | 18¢ | 1 | ×0.1^40 = 0.0 |
|  | 10¢ | 5 | ×0.1^48 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^56 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-catlau</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau` ← this one
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 1 @ 20¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 52¢ | 1 | ×0.1^32 = 0.0 |
|  | 95¢ | 1 | ×0.1^75 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^77 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 1 @ 7¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 94¢ | 1 | ×0.1^87 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^90 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> SELL 1 @ 15¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 98¢ | 2,000 | ×0.1^83 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ma-2026-11-03-dem</code> BUY 1 @ 27¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 2¢ | 600,000 | ×0.1^25 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem` ← this one
2. `ussewc-usse-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> SELL 1 @ 26¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 96¢ | 0 | ×0.1^70 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^71 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimobe</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe` ← this one
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-dem</code> BUY 1 @ 34¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 5 | ×0.1^24 = 0.0 |
|  | 9¢ | 1 | ×0.1^25 = 0.0 |
|  | 8¢ | 1 | ×0.1^26 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^32 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem` ← this one
2. `usgubewc-usgub-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 1 @ 56¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 56¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 13¢ | 1 | ×0.1^43 = 0.0 |
|  | 10¢ | 4 | ×0.1^46 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^54 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> BUY 1 @ 54¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 54¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 11¢ | 2 | ×0.1^43 = 0.0 |
|  | 10¢ | 5 | ×0.1^44 = 0.0 |
|  | 4¢ | 1 | ×0.1^50 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^52 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-rep</code> BUY 1 @ 46¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 15¢ | 1 | ×0.1^31 = 0.0 |
|  | 4¢ | 1 | ×0.1^42 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^44 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem`
2. `ussewc-usse-la-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 1 @ 40¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 62¢ | 1 | ×0.1^22 = 0.0 |
|  | 96¢ | 1 | ×0.1^56 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^57 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> BUY 1 @ 60¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 39¢ | 1 | ×0.1^21 = 0.0 |
|  | 23¢ | 1 | ×0.1^37 = 0.0 |
|  | 3¢ | 1 | ×0.1^57 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^58 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-dem</code> BUY 1 @ 60¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 30¢ | 1 | ×0.1^30 = 0.0 |
|  | 15¢ | 1 | ×0.1^45 = 0.0 |
|  | 11¢ | 1 | ×0.1^49 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^58 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem` ← this one
2. `ussewc-usse-va-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> SELL 1 @ 12¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 58¢ | 1 | ×0.1^46 = 0.0 |
|  | 82¢ | 1 | ×0.1^70 = 0.0 |
|  | 98¢ | 2,000 | ×0.1^86 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 1 @ 53¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 53¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 27¢ | 1 | ×0.1^26 = 0.0 |
|  | 7¢ | 1 | ×0.1^46 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^51 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimsch</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch` ← this one
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-dem</code> SELL 1 @ 47¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 90¢ | 1 | ×0.1^43 = 0.0 |
|  | 97¢ | 2,002 | ×0.1^50 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 1 @ 67¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 92¢ | 1 | ×0.1^25 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^30 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-madcaw</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw` ← this one
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> BUY 1 @ 47¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 24¢ | 1 | ×0.1^23 = 0.0 |
|  | 10¢ | 5 | ×0.1^37 = 0.0 |
|  | 9¢ | 1 | ×0.1^38 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^45 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-rep</code> SELL 1 @ 60¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 77¢ | 1 | ×0.1^17 = 0.0 |
|  | 97¢ | 2,001 | ×0.1^37 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem`
2. `ussewc-usse-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> SELL 1 @ 14¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 32¢ | 5,000 | ×0.1^18 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-dem</code> BUY 1 @ 49¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 35¢ | 1 | ×0.1^14 = 0.0 |
|  | 20¢ | 1 | ×0.1^29 = 0.0 |
|  | 7¢ | 1 | ×0.1^42 = 0.0 |
|  | 2¢ | 550,000 | ×0.1^47 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem` ← this one
2. `ussewc-usse-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-rep</code> BUY 1 @ 21¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 8¢ | 1 | ×0.1^13 = 0.0 |
|  | 1¢ | 3,006 | ×0.1^20 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem`
2. `usgubewc-usgub-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 1 @ 57¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 47¢ | 1 | ×0.1^10 = 0.0 |
|  | 10¢ | 1 | ×0.1^47 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^55 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ma-2026-11-03-rep</code> SELL 1 @ 86¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 86¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 98¢ | 2,001 | ×0.1^12 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem`
2. `usgubewc-usgub-ma-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (275,593 resting) | ~30.9% | ~$23.15 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (631,418 resting) | ~12.3% | ~$9.19 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (278,482 resting) | ~8.5% | ~$6.40 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (78,204 resting) | ~5.1% | ~$3.81 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,599 resting) | ~14.6% | ~$3.66 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (81,790 resting) | ~3.5% | ~$2.62 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (621,525 resting) | ~3.0% | ~$2.23 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,900 resting) | ~8.4% | ~$2.10 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (889,189 resting) | ~2.6% | ~$1.95 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (19,809 resting) | ~3.0% | ~$1.51 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (359,950 resting) | ~22.1% | ~$1.38 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (59,275 resting) | ~20.9% | ~$1.31 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $1,678.09 |
| Skipped | $1.41 |
| **Total earned** | **$3,567.53** |

2562 reward rows · 43 days with rewards · 550 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-14 ⚠️ multi-day pending bucket | $274.59 | `██████████` |
| 2026-08-13 | $223.24 | `████████` |
| 2026-08-12 | $213.04 | `████████` |
| 2026-08-11 | $409.60 | `███████████████` |
| 2026-08-10 | $557.62 | `████████████████████` |
| 2026-08-09 | $62.24 | `██` |
| 2026-08-08 | $54.78 | `██` |
| 2026-08-07 | $60.33 | `██` |
| 2026-08-06 | $52.21 | `██` |
| 2026-08-05 | $31.46 | `█` |
| 2026-08-04 | $53.94 | `██` |
| 2026-08-03 | $44.81 | `██` |
| 2026-08-02 | $14.05 | `█` |
| 2026-08-01 | $52.30 | `██` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $2,104.21 | `████████████████████` |
| 2026-07 | $1,463.32 | `██████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $172.95 |
| `apdc-alito-2026-12-31` | $115.00 |
| `opdc-mcconnell-resign-2026-11-02` | $79.41 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $63.61 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $55.91 |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | $51.17 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.44 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.51 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.04 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `scc-senate-gop-2026-11-03-49` | $32.00 |
| `scc-senate-gop-2026-11-03-52` | $31.83 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-16 4:54 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 4:06 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 3:05 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:57 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:37 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:30 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:12 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:05 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 1:50 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 1:26 PM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
