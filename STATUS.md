# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-16 7:51 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$420.36/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — BUY at the best price, ~$6.98/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$3.81/day), `ewc-usgub-ga-2026-11-03-dem` (~$2.81/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$420.36/day (~$17.51/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ussewc-usse-il-2026-11-03-dem` | BUY | 33.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,203 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 59.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,007 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (208,290 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-dem` | BUY | 60.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (550,202 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 60.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,207 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-rep` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (330,175 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 46.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,232 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ma-2026-11-03-dem` | BUY | 45.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,201 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (130,727 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 22.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,202 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (203,552 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | SELL | 14.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,998 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 38.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,478 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-dem` | BUY | 55.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,313 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 9.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (130,727 resting ≥ 2,000 ✓) ≈ $6.24/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (130,727 resting ≥ 2,000 ✓) ≈ $6.24/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | SELL | 11.0¢ | 76 | 0 | $25.00 | ✅ scoring — ~98.7% of ask side (3,758 resting ≥ 2,000 ✓) ≈ $1.76/day (pool ÷ 7 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 14.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~97.8% of bid side (29,108 resting ≥ 20,000 ✓) ≈ $9.41/day (program pool ÷ 52 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 17.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~96.6% of ask side (196,012 resting ≥ 2,000 ✓) ≈ $6.04/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 14.0¢ | 0 | 0 | $1,000.00 | ✅ scoring — ~92.8% of bid side (27,504 resting ≥ 20,000 ✓) ≈ $8.93/day (program pool ÷ 52 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | BUY | 52.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.9% of bid side (500,208 resting ≥ 2,000 ✓) ≈ $5.68/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ma-2026-11-03-dem` | BUY | 57.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.9% of bid side (2,303 resting ≥ 2,000 ✓) ≈ $5.68/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-kenblo` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.8% of ask side (2,003 resting ≥ 2,000 ✓) ≈ $3.78/day (pool ÷ 3 markets) |
| `ewc-usp-2028-11-07-gleyou` | BUY | 10.0¢ | 58 | 0 | $1,000.00 | ✅ scoring — ~90.0% of bid side (30,061 resting ≥ 20,000 ✓) ≈ $8.65/day (program pool ÷ 52 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 12.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~89.6% of ask side (66,134 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.1% of bid side (2,001 resting ≥ 2,000 ✓) ≈ $5.57/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.1% of bid side (2,001 resting ≥ 2,000 ✓) ≈ $5.57/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | BUY | 1.0¢ | 1,798 | 1 | $25.00 | ✅ scoring — ~89.0% of bid side (2,002 resting ≥ 2,000 ✓) ≈ $5.56/day (pool ÷ 2 markets) |
| …and 668 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 1 @ 33¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 1 | ×0.1^23 = 0.0 |
|  | 8¢ | 1 | ×0.1^25 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^31 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 1 @ 59¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 59¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 19¢ | 1 | ×0.1^40 = 0.0 |
|  | 13¢ | 1 | ×0.1^46 = 0.0 |
|  | 10¢ | 5 | ×0.1^49 = 0.0 |
|  | 1¢ | 1,999 | ×0.1^58 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 1 @ 8¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 82¢ | 1 | ×0.1^74 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^90 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-dem</code> BUY 1 @ 60¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 25¢ | 1 | ×0.1^35 = 0.0 |
|  | 2¢ | 550,000 | ×0.1^58 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem` ← this one
2. `ussewc-usse-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 1 @ 60¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 21¢ | 1 | ×0.1^39 = 0.0 |
|  | 10¢ | 5 | ×0.1^50 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^58 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-rep</code> SELL 1 @ 5¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 60¢ | 1 | ×0.1^55 = 0.0 |
|  | 93¢ | 1 | ×0.1^88 = 0.0 |
|  | 98¢ | 132,784 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem`
2. `ussewc-usse-il-2026-11-03-rep` ← this one

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 1 @ 46¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 20¢ | 31 | ×0.1^26 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^44 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ma-2026-11-03-dem</code> BUY 1 @ 45¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 2¢ | 600,000 | ×0.1^43 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem` ← this one
2. `ussewc-usse-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 1 @ 8¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 80¢ | 1 | ×0.1^72 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^90 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 1 @ 22¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 8¢ | 1 | ×0.1^14 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^20 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-dem</code> SELL 1 @ 8¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 18¢ | 0 | ×0.1^10 = 0.0 |
|  | 64¢ | 1 | ×0.1^56 = 0.0 |
|  | 98¢ | 203,325 | ×0.1^90 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem` ← this one
2. `ussewc-usse-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> SELL 1 @ 14¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 26¢ | 30 | ×0.1^12 = 0.0 |
|  | 99¢ | 2,967 | ×0.1^85 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 1 @ 38¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 46¢ | 1 | ×0.1^8 = 0.0 |
|  | 92¢ | 1 | ×0.1^54 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^60 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-dem</code> BUY 1 @ 55¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 55¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 50¢ | 10 | ×0.1^5 = 0.0 |
|  | 49¢ | 100 | ×0.1^6 = 0.0 |
|  | 3¢ | 2 | ×0.1^52 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^53 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem` ← this one
2. `ussewc-usse-va-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 1 @ 9¢ → $6.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 12¢ | 1 | ×0.1^3 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^89 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.9% = $6.24/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> SELL 1 @ 7¢ → $6.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 1 | ×0.1^3 = 0.0 |
|  | 96¢ | 0 | ×0.1^89 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^91 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.9% = $6.24/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> SELL 76 @ 11¢ → $1.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 77 (76 yours) | ×0.1^0 = 77.0 |
|  | 99¢ | 3,681 | ×0.1^88 = 0.0 |
| | | **Σ** | **77.0** |

`yours 76.0 / Σ 77.0 = 98.7%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 98.7% = $1.76/day`  

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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 1 @ 14¢ → $9.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 13¢ | 0 | ×0.2^1 = 0.0 |
|  | 6¢ | 10 | ×0.2^8 = 0.0 |
|  | 3¢ | 250 | ×0.2^11 = 0.0 |
|  | 1¢ | 28,847 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 97.8%`  
`$1,000 ÷ 52 ÷ 2 = $9.62 × 97.8% = $9.41/day`  

<details><summary>÷ 52 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut` ← this one
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 1 @ 17¢ → $6.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 20¢ | 35 | ×0.1^3 = 0.0 |
|  | 40¢ | 1 | ×0.1^23 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^81 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 96.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 96.6% = $6.04/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 0 @ 14¢ → $8.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 0 (0 yours) | ×0.2^0 = 0.1 |
|  | 7¢ | 1 | ×0.2^7 = 0.0 |
|  | 4¢ | 4 | ×0.2^10 = 0.0 |
|  | 3¢ | 2 | ×0.2^11 = 0.0 |
|  | 1¢ | 27,497 | ×0.2^13 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 92.8%`  
`$1,000 ÷ 52 ÷ 2 = $9.62 × 92.8% = $8.93/day`  

<details><summary>÷ 52 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus` ← this one
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> BUY 1 @ 52¢ → $5.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 52¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 51¢ | 1 | ×0.1^1 = 0.1 |
|  | 26¢ | 1 | ×0.1^26 = 0.0 |
|  | 10¢ | 5 | ×0.1^42 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^50 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.9% = $5.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ma-2026-11-03-dem</code> BUY 1 @ 57¢ → $5.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 56¢ | 1 | ×0.1^1 = 0.1 |
|  | 49¢ | 100 | ×0.1^8 = 0.0 |
|  | 5¢ | 1 | ×0.1^52 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^56 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.9% = $5.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-kenblo</code> SELL 1 @ 5¢ → $3.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 6¢ | 1 | ×0.1^1 = 0.1 |
|  | 8¢ | 1 | ×0.1^3 = 0.0 |
|  | 9¢ | 2 | ×0.1^4 = 0.0 |
|  | 10¢ | 1 | ×0.1^5 = 0.0 |
|  | 12¢ | 7 | ×0.1^7 = 0.0 |
|  | 37¢ | 1 | ×0.1^32 = 0.0 |
|  | 99¢ | 1,989 | ×0.1^94 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.8%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 90.8% = $3.78/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo` ← this one
3. `usgubewc-usgub-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-gleyou</code> BUY 58 @ 10¢ → $8.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 64 (58 yours) | ×0.2^0 = 64.5 |
|  | 6¢ | 1 | ×0.2^4 = 0.0 |
|  | 1¢ | 29,996 | ×0.2^9 = 0.0 |
| | | **Σ** | **64.5** |

`yours 58.0 / Σ 64.5 = 90.0%`  
`$1,000 ÷ 52 ÷ 2 = $9.62 × 90.0% = $8.65/day`  

<details><summary>÷ 52 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou` ← this one
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 1 @ 12¢ → $5.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 13¢ | 1 | ×0.1^1 = 0.1 |
|  | 16¢ | 157 | ×0.1^4 = 0.0 |
|  | 45¢ | 500 | ×0.1^33 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^86 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 89.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.6% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **201.9** |

`yours 179.9 / Σ 201.9 = 89.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.1% = $5.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **201.9** |

`yours 179.9 / Σ 201.9 = 89.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.1% = $5.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> BUY 1,798 @ 1¢ → $5.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 1¢ | 2,000 (1,798 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **202.0** |

`yours 179.8 / Σ 202.0 = 89.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.0% = $5.56/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (277,619 resting) | ~9.3% | ~$6.98 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,567 resting) | ~15.3% | ~$3.81 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (85,204 resting) | ~3.7% | ~$2.81 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (281,897 resting) | ~3.5% | ~$2.59 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,898 resting) | ~8.4% | ~$2.10 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (105,946 resting) | ~2.6% | ~$1.99 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,843 resting) | ~5.4% | ~$1.35 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (359,722 resting) | ~21.4% | ~$1.34 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (59,540 resting) | ~1.6% | ~$1.19 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (91,840 resting) | ~17.4% | ~$1.09 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (68,688 resting) | ~17.2% | ~$1.07 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (74,343 resting) | ~24.6% | ~$1.02 |

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
| 2026-08-16 7:51 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 7:42 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 6:42 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 5:55 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 4:54 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 4:06 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 3:05 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:57 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:37 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:30 PM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
