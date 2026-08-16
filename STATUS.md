# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-16 7:54 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$461.19/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — BUY at the best price, ~$5.59/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$3.81/day), `ewc-usgub-oh-2026-11-03-dem` (~$2.82/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$461.19/day (~$19.22/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 50.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (208,291 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 53.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,207 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | SELL | 12.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (3,998 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 3 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 17.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (195,977 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tn-2026-11-03-dem` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,000 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-rep` | BUY | 58.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,208 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | SELL | 19.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (208,289 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-rep` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (330,176 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ma-2026-11-03-dem` | BUY | 57.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,206 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 46.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,202 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (208,290 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-catlau` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `ussewc-usse-nm-2026-11-03-dem` | BUY | 60.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (550,207 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (130,727 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 50.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,007 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | BUY | 57.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,207 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | BUY | 37.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,206 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | SELL | 9.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,001 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 60.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,207 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 60.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,207 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 12.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (130,727 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `usgubewc-usgub-tn-2026-11-03-rep` | BUY | 59.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,189 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ma-2026-11-03-dem` | BUY | 45.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,206 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 57.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,227 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 46.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,478 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | SELL | 14.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (3,893 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-rep` | BUY | 24.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,208 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 19.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,006 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| …and 686 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 1 @ 50¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 82¢ | 1 | ×0.1^32 = 0.0 |
|  | 92¢ | 1 | ×0.1^42 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^48 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 1 @ 53¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 53¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 6 | ×0.1^43 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^51 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

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
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> SELL 1 @ 12¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 99¢ | 3,997 | ×0.1^87 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 1 @ 17¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 40¢ | 1 | ×0.1^23 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^81 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-dem</code> SELL 1 @ 5¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 55¢ | 1 | ×0.1^50 = 0.0 |
|  | 99¢ | 1,998 | ×0.1^94 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> BUY 1 @ 58¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 21¢ | 1 | ×0.1^37 = 0.0 |
|  | 13¢ | 1 | ×0.1^45 = 0.0 |
|  | 10¢ | 5 | ×0.1^48 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^56 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem`
2. `usgubewc-usgub-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> SELL 1 @ 19¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 98¢ | 208,063 | ×0.1^79 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-rep</code> SELL 1 @ 5¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 60¢ | 1 | ×0.1^55 = 0.0 |
|  | 77¢ | 1 | ×0.1^72 = 0.0 |
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
<details><summary><code>usgubewc-usgub-ma-2026-11-03-dem</code> BUY 1 @ 57¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 4 | ×0.1^47 = 0.0 |
|  | 5¢ | 1 | ×0.1^52 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^56 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 1 @ 46¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 20¢ | 1 | ×0.1^26 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^44 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> SELL 1 @ 6¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 38¢ | 1 | ×0.1^32 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

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
<details><summary><code>ussewc-usse-nm-2026-11-03-dem</code> BUY 1 @ 60¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 25¢ | 1 | ×0.1^35 = 0.0 |
|  | 10¢ | 5 | ×0.1^50 = 0.0 |
|  | 2¢ | 550,000 | ×0.1^58 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem` ← this one
2. `ussewc-usse-nm-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 1 @ 50¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 24¢ | 1 | ×0.1^26 = 0.0 |
|  | 10¢ | 5 | ×0.1^40 = 0.0 |
|  | 2¢ | 1 | ×0.1^48 = 0.0 |
|  | 1¢ | 1,999 | ×0.1^49 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> BUY 1 @ 57¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 5 | ×0.1^47 = 0.0 |
|  | 5¢ | 1 | ×0.1^52 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^55 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> BUY 1 @ 37¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 5 | ×0.1^27 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^35 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> SELL 1 @ 9¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 41¢ | 1 | ×0.1^32 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^90 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 1 @ 60¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 15¢ | 1 | ×0.1^45 = 0.0 |
|  | 10¢ | 5 | ×0.1^50 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^58 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 1 @ 12¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 35¢ | 1 | ×0.1^23 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^86 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-tn-2026-11-03-rep</code> BUY 1 @ 59¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 59¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 13¢ | 1 | ×0.1^46 = 0.0 |
|  | 10¢ | 5 | ×0.1^49 = 0.0 |
|  | 1¢ | 2,182 | ×0.1^58 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem`
2. `usgubewc-usgub-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ma-2026-11-03-dem</code> BUY 1 @ 45¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 5 | ×0.1^35 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^43 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem` ← this one
2. `ussewc-usse-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> BUY 1 @ 57¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 40¢ | 26 | ×0.1^17 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^55 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 1 @ 46¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 58¢ | 1 | ×0.1^12 = 0.0 |
|  | 92¢ | 1 | ×0.1^46 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^52 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> SELL 1 @ 14¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 26¢ | 30 | ×0.1^12 = 0.0 |
|  | 99¢ | 3,862 | ×0.1^85 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-rep</code> BUY 1 @ 24¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 15¢ | 1 | ×0.1^9 = 0.0 |
|  | 10¢ | 5 | ×0.1^14 = 0.0 |
|  | 9¢ | 1 | ×0.1^15 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^22 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem`
2. `ussewc-usse-la-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 1 @ 19¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 13¢ | 1 | ×0.1^6 = 0.0 |
|  | 10¢ | 5 | ×0.1^9 = 0.0 |
|  | 1¢ | 1,999 | ×0.1^18 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (278,987 resting) | ~7.5% | ~$5.59 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,544 resting) | ~15.2% | ~$3.81 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (281,448 resting) | ~3.8% | ~$2.82 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (85,204 resting) | ~3.7% | ~$2.81 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,898 resting) | ~8.4% | ~$2.10 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (105,946 resting) | ~2.6% | ~$1.99 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (91,463 resting) | ~25.9% | ~$1.62 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,846 resting) | ~5.4% | ~$1.35 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (359,722 resting) | ~21.4% | ~$1.34 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (60,387 resting) | ~20.8% | ~$1.30 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (74,192 resting) | ~30.2% | ~$1.26 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (59,540 resting) | ~1.6% | ~$1.19 |

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
| 2026-08-16 7:54 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 7:51 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 7:42 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 6:42 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 5:55 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 4:54 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 4:06 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 3:05 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:57 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:37 PM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
