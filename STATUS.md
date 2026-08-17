# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-17 12:32 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$918.44/day estimated (ceiling, not promise — details below)

**Earned:** $4,920.49 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-15: **$1,352.63** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-14: **$274.92** · 2026-08-13: **$223.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — BUY at the best price, ~$4.02/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$3.70/day), `ewc-usgub-ga-2026-11-03-rep` (~$3.08/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$918.44/day (~$38.27/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ushrp-fl19-2026-08-18-jimobe` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-madcaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `ussewc-usse-il-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (330,178 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 12.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,477 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-chrcol` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-catlau` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (208,292 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-pa-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (5,360 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,478 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,005 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (130,731 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (208,293 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (130,728 resting ≥ 2,000 ✓) ≈ $6.24/day (event pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-johstr` | BUY | 1.0¢ | 1,994 | 0 | $25.00 | ✅ scoring — ~99.7% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.78/day (event pool ÷ 7 markets) |
| `usgubewc-usgub-tn-2026-11-03-dem` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.0% of ask side (4,003 resting ≥ 2,000 ✓) ≈ $6.19/day (event pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 12.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.0% of ask side (66,034 resting ≥ 2,000 ✓) ≈ $6.19/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-kamhar` | BUY | 13.0¢ | 209 | 0 | $1,000.00 | ✅ scoring — ~99.0% of bid side (70,661 resting ≥ 20,000 ✓) ≈ $18.32/day (event pool ÷ 27 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | SELL | 11.0¢ | 76 | 0 | $25.00 | ✅ scoring — ~98.7% of ask side (3,758 resting ≥ 2,000 ✓) ≈ $1.76/day (event pool ÷ 7 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 9.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~98.5% of ask side (208,340 resting ≥ 2,000 ✓) ≈ $6.16/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | BUY | 5.0¢ | 45 | 0 | $25.00 | ✅ scoring — ~97.4% of bid side (2,046 resting ≥ 2,000 ✓) ≈ $6.09/day (event pool ÷ 2 markets) |
| `ussewc-usse-de-2026-11-03-rep` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~97.1% of ask side (130,730 resting ≥ 2,000 ✓) ≈ $6.07/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 14.0¢ | 0 | 0 | $1,000.00 | ✅ scoring — ~92.8% of bid side (27,509 resting ≥ 20,000 ✓) ≈ $17.19/day (event pool ÷ 27 markets) |
| `ussewc-usse-ma-2026-11-03-rep` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.9% of ask side (65,486 resting ≥ 2,000 ✓) ≈ $5.68/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.8% of ask side (70,528 resting ≥ 2,000 ✓) ≈ $5.68/day (event pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-dem` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.1% of ask side (203,880 resting ≥ 2,000 ✓) ≈ $5.63/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-kenblo` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.0% of ask side (2,001 resting ≥ 2,000 ✓) ≈ $3.75/day (event pool ÷ 3 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,001 resting ≥ 2,000 ✓) ≈ $5.59/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | BUY | 1.0¢ | 1,798 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,001 resting ≥ 2,000 ✓) ≈ $5.59/day (event pool ÷ 2 markets) |
| …and 820 more | | | | | | |

**Tap an order for its book window and the math:**

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
<details><summary><code>ussewc-usse-il-2026-11-03-rep</code> SELL 1 @ 6¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 30¢ | 1 | ×0.1^24 = 0.0 |
|  | 42¢ | 1 | ×0.1^36 = 0.0 |
|  | 44¢ | 1 | ×0.1^38 = 0.0 |
|  | 60¢ | 1 | ×0.1^54 = 0.0 |
|  | 94¢ | 1 | ×0.1^88 = 0.0 |
|  | 98¢ | 132,784 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem`
2. `ussewc-usse-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 1 @ 12¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 94¢ | 1 | ×0.1^82 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^86 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-chrcol</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol` ← this one
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

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
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> SELL 1 @ 6¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 57¢ | 1 | ×0.1^51 = 0.0 |
|  | 83¢ | 1 | ×0.1^77 = 0.0 |
|  | 84¢ | 1 | ×0.1^78 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-pa-2026-11-03-rep</code> SELL 1 @ 6¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 32¢ | 1 | ×0.1^26 = 0.0 |
|  | 48¢ | 1 | ×0.1^42 = 0.0 |
|  | 50¢ | 100 | ×0.1^44 = 0.0 |
|  | 97¢ | 32 | ×0.1^91 = 0.0 |
|  | 99¢ | 5,225 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem`
2. `usgubewc-usgub-pa-2026-11-03-rep` ← this one

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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 1 @ 6¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 28¢ | 1 | ×0.1^22 = 0.0 |
|  | 89¢ | 1 | ×0.1^83 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> SELL 1 @ 7¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 22¢ | 1 | ×0.1^15 = 0.0 |
|  | 26¢ | 1 | ×0.1^19 = 0.0 |
|  | 50¢ | 1 | ×0.1^43 = 0.0 |
|  | 62¢ | 1 | ×0.1^55 = 0.0 |
|  | 66¢ | 1 | ×0.1^59 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> SELL 1 @ 6¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 16¢ | 1 | ×0.1^10 = 0.0 |
|  | 26¢ | 1 | ×0.1^20 = 0.0 |
|  | 35¢ | 1 | ×0.1^29 = 0.0 |
|  | 68¢ | 1 | ×0.1^62 = 0.0 |
|  | 94¢ | 1 | ×0.1^88 = 0.0 |
|  | 96¢ | 0 | ×0.1^90 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> SELL 1 @ 5¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 13¢ | 1 | ×0.1^8 = 0.0 |
|  | 21¢ | 1 | ×0.1^16 = 0.0 |
|  | 52¢ | 1 | ×0.1^47 = 0.0 |
|  | 95¢ | 1 | ×0.1^90 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 1 @ 6¢ → $6.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 9¢ | 1 | ×0.1^3 = 0.0 |
|  | 66¢ | 1 | ×0.1^60 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.9% = $6.24/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-johstr</code> BUY 1,994 @ 1¢ → $1.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (1,994 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 1,994.0 / Σ 2,000.0 = 99.7%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 99.7% = $1.78/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr` ← this one
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-dem</code> SELL 1 @ 5¢ → $6.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 7¢ | 1 | ×0.1^2 = 0.0 |
|  | 58¢ | 1 | ×0.1^53 = 0.0 |
|  | 82¢ | 1 | ×0.1^77 = 0.0 |
|  | 98¢ | 2,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.0% = $6.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 1 @ 12¢ → $6.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 14¢ | 1 | ×0.1^2 = 0.0 |
|  | 38¢ | 57 | ×0.1^26 = 0.0 |
|  | 45¢ | 500 | ×0.1^33 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^86 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.0% = $6.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-kamhar</code> BUY 209 @ 13¢ → $18.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 211 (209 yours) | ×0.2^0 = 211.2 |
|  | 3¢ | 70,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **211.2** |

`yours 209.0 / Σ 211.2 = 99.0%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 99.0% = $18.32/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

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
14. `ewc-usp-2028-11-07-kamhar` ← this one
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
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 1 @ 9¢ → $6.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 11¢ | 1 | ×0.1^2 = 0.0 |
|  | 13¢ | 50 | ×0.1^4 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^89 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.5% = $6.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> BUY 45 @ 5¢ → $6.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 46 (45 yours) | ×0.1^0 = 46.0 |
|  | 2¢ | 2 | ×0.1^3 = 0.0 |
|  | 1¢ | 1,998 | ×0.1^4 = 0.2 |
| | | **Σ** | **46.2** |

`yours 45.0 / Σ 46.2 = 97.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 97.4% = $6.09/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-de-2026-11-03-rep</code> SELL 1 @ 7¢ → $6.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 0 | ×0.1^3 = 0.0 |
|  | 28¢ | 1 | ×0.1^21 = 0.0 |
|  | 68¢ | 1 | ×0.1^61 = 0.0 |
|  | 71¢ | 1 | ×0.1^64 = 0.0 |
|  | 85¢ | 1 | ×0.1^78 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^91 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 97.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 97.1% = $6.07/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-de-2026-11-03-dem`
2. `ussewc-usse-de-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 0 @ 14¢ → $17.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 0 (0 yours) | ×0.2^0 = 0.1 |
|  | 7¢ | 1 | ×0.2^7 = 0.0 |
|  | 5¢ | 4 | ×0.2^9 = 0.0 |
|  | 4¢ | 2 | ×0.2^10 = 0.0 |
|  | 3¢ | 3 | ×0.2^11 = 0.0 |
|  | 2¢ | 2 | ×0.2^12 = 0.0 |
|  | 1¢ | 27,497 | ×0.2^13 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 92.8%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 92.8% = $17.19/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

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
<details><summary><code>ussewc-usse-ma-2026-11-03-rep</code> SELL 1 @ 5¢ → $5.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 6¢ | 1 | ×0.1^1 = 0.1 |
|  | 31¢ | 9 | ×0.1^26 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.9% = $5.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem`
2. `ussewc-usse-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> SELL 1 @ 8¢ → $5.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 9¢ | 1 | ×0.1^1 = 0.1 |
|  | 11¢ | 1 | ×0.1^3 = 0.0 |
|  | 16¢ | 50 | ×0.1^8 = 0.0 |
|  | 32¢ | 5,000 | ×0.1^24 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.8% = $5.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-dem</code> SELL 1 @ 5¢ → $5.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 6¢ | 1 | ×0.1^1 = 0.1 |
|  | 7¢ | 1 | ×0.1^2 = 0.0 |
|  | 9¢ | 1 | ×0.1^4 = 0.0 |
|  | 12¢ | 325 | ×0.1^7 = 0.0 |
|  | 18¢ | 0 | ×0.1^13 = 0.0 |
|  | 51¢ | 1 | ×0.1^46 = 0.0 |
|  | 98¢ | 203,325 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.1% = $5.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem` ← this one
2. `ussewc-usse-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-kenblo</code> SELL 1 @ 8¢ → $3.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 9¢ | 1 | ×0.1^1 = 0.1 |
|  | 10¢ | 1 | ×0.1^2 = 0.0 |
|  | 11¢ | 1 | ×0.1^3 = 0.0 |
|  | 12¢ | 7 | ×0.1^4 = 0.0 |
|  | 37¢ | 1 | ×0.1^29 = 0.0 |
|  | 99¢ | 1,989 | ×0.1^91 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.0%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 90.0% = $3.75/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo` ← this one
3. `usgubewc-usgub-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 2,000 (1,799 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **201.0** |

`yours 179.9 / Σ 201.0 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.59/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> BUY 1,798 @ 1¢ → $5.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 2,000 (1,798 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **201.0** |

`yours 179.8 / Σ 201.0 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.59/day`  

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
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (278,662 resting) | ~5.4% | ~$4.02 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,733 resting) | ~14.8% | ~$3.70 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (64,033 resting) | ~4.1% | ~$3.08 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (281,927 resting) | ~3.5% | ~$2.62 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (89,155 resting) | ~3.3% | ~$2.51 |
| `ewc-usse-mi-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (630,014 resting) | ~38.9% | ~$2.43 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,864 resting) | ~8.5% | ~$2.12 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (357,650 resting) | ~27.7% | ~$1.73 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (68,236 resting) | ~27.6% | ~$1.73 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,239,953 resting) | ~24.8% | ~$1.55 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,265 resting) | ~6.0% | ~$1.49 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (74,182 resting) | ~30.2% | ~$1.26 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $3,031.05 |
| Skipped | $1.41 |
| **Total earned** | **$4,920.49** |

2700 reward rows · 44 days with rewards · 552 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-15 ⚠️ multi-day pending bucket | $1,352.63 | `████████████████████` |
| 2026-08-14 | $274.92 | `████` |
| 2026-08-13 | $223.24 | `███` |
| 2026-08-12 | $213.04 | `███` |
| 2026-08-11 | $409.60 | `██████` |
| 2026-08-10 | $557.62 | `████████` |
| 2026-08-09 | $62.24 | `█` |
| 2026-08-08 | $54.78 | `█` |
| 2026-08-07 | $60.33 | `█` |
| 2026-08-06 | $52.21 | `█` |
| 2026-08-05 | $31.46 | `█` |
| 2026-08-04 | $53.94 | `█` |
| 2026-08-03 | $44.81 | `█` |
| 2026-08-02 | $14.05 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $3,457.17 | `████████████████████` |
| 2026-07 | $1,463.32 | `████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $176.70 |
| `apdc-alito-2026-12-31` | $115.00 |
| `ewc-usp-party-2028-11-07-rep` | $83.48 |
| `opdc-mcconnell-resign-2026-11-02` | $79.41 |
| `ewc-usp-party-2028-11-07-dem` | $69.70 |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | $66.06 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $63.61 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $60.43 |
| `enwc-uspres-nom-rep-2028-rondes` | $45.09 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.58 |
| `enwc-uspres-nom-dem-2028-stasmi` | $42.80 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.51 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.04 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-17 12:32 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 12:20 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 12:07 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-16 10:44 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:26 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:44 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:20 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:15 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:08 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:14 PM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
