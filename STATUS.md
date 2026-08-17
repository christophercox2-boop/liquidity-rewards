# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-17 8:06 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$972.24/day estimated (ceiling, not promise — details below)

**Earned:** $4,920.49 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-15: **$1,352.63** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-14: **$274.92** · 2026-08-13: **$223.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$7.11/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$6.16/day), `ewc-usse-mi-2026-11-03-rep` (~$4.49/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$972.24/day (~$40.51/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ushrp-fl19-2026-08-18-catlau` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `ussewc-usse-co-2026-11-03-dem` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,220 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-dem` | BUY | 95.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (550,216 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ma-2026-11-03-rep` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,001 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,208 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 79.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,240 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,003 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 79.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,003 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 90.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,220 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (130,726 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-pa-2026-11-03-dem` | BUY | 94.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (7,012 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-chrcol` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `usgubewc-usgub-tn-2026-11-03-rep` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,008 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimobe` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 30.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (210,291 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-pa-2026-11-03-rep` | SELL | 10.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (5,360 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 94.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,218 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `ussewc-usse-ma-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,476 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | SELL | 12.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,000 resting ≥ 2,000 ✓) ≈ $4.17/day (event pool ÷ 3 markets) |
| `enwc-ushrp-fl19-2026-08-18-madcaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `ussewc-usse-tn-2026-11-03-dem` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (527,337 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-rep` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,217 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | SELL | 21.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (208,290 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ma-2026-11-03-dem` | BUY | 81.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,221 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-dem` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,220 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tn-2026-11-03-dem` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (4,003 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 31.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (92,040 resting ≥ 5,000 ✓) ≈ $3.85/day (event pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 13.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (10,590 resting ≥ 2,000 ✓) ≈ $12.50/day |
| …and 913 more | | | | | | |

**Tap an order for its book window and the math:**

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
<details><summary><code>ussewc-usse-co-2026-11-03-dem</code> BUY 3 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 16¢ | 1 | ×0.1^78 = 0.0 |
|  | 14¢ | 4 | ×0.1^80 = 0.0 |
|  | 3¢ | 12 | ×0.1^91 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem` ← this one
2. `ussewc-usse-co-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-dem</code> BUY 5 @ 95¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 5 (5 yours) | ×0.1^0 = 5.0 |
|  | 58¢ | 10 | ×0.1^37 = 0.0 |
|  | 14¢ | 1 | ×0.1^81 = 0.0 |
|  | 2¢ | 550,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem` ← this one
2. `ussewc-usse-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ma-2026-11-03-rep</code> SELL 1 @ 5¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 29¢ | 1 | ×0.1^24 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^94 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem`
2. `usgubewc-usgub-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> BUY 3 @ 95¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 52¢ | 1 | ×0.1^43 = 0.0 |
|  | 44¢ | 1 | ×0.1^51 = 0.0 |
|  | 39¢ | 1 | ×0.1^56 = 0.0 |
|  | 36¢ | 1 | ×0.1^59 = 0.0 |
|  | 18¢ | 1 | ×0.1^77 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> BUY 5 @ 79¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 5 (5 yours) | ×0.1^0 = 5.0 |
|  | 57¢ | 1 | ×0.1^22 = 0.0 |
|  | 46¢ | 9 | ×0.1^33 = 0.0 |
|  | 40¢ | 25 | ×0.1^39 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^77 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> SELL 1 @ 8¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 26¢ | 1 | ×0.1^18 = 0.0 |
|  | 50¢ | 1 | ×0.1^42 = 0.0 |
|  | 62¢ | 1 | ×0.1^54 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^91 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 3 @ 79¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 17¢ | 1 | ×0.1^62 = 0.0 |
|  | 1¢ | 1,999 | ×0.1^78 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 4 @ 90¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 4 (4 yours) | ×0.1^0 = 4.0 |
|  | 58¢ | 1 | ×0.1^32 = 0.0 |
|  | 52¢ | 1 | ×0.1^38 = 0.0 |
|  | 51¢ | 1 | ×0.1^39 = 0.0 |
|  | 44¢ | 1 | ×0.1^46 = 0.0 |
|  | 38¢ | 7 | ×0.1^52 = 0.0 |
|  | 29¢ | 1 | ×0.1^61 = 0.0 |
|  | 10¢ | 4 | ×0.1^80 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^88 = 0.0 |
| | | **Σ** | **4.0** |

`yours 4.0 / Σ 4.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 1 @ 5¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 98¢ | 130,500 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-pa-2026-11-03-dem</code> BUY 4 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 4 (4 yours) | ×0.1^0 = 4.0 |
|  | 60¢ | 1 | ×0.1^34 = 0.0 |
|  | 54¢ | 1 | ×0.1^40 = 0.0 |
|  | 51¢ | 6 | ×0.1^43 = 0.0 |
|  | 50¢ | 100 | ×0.1^44 = 0.0 |
|  | 2¢ | 100 | ×0.1^92 = 0.0 |
|  | 1¢ | 6,800 | ×0.1^93 = 0.0 |
| | | **Σ** | **4.0** |

`yours 4.0 / Σ 4.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem` ← this one
2. `usgubewc-usgub-pa-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-tn-2026-11-03-rep</code> BUY 3 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 61¢ | 4 | ×0.1^33 = 0.0 |
|  | 59¢ | 1 | ×0.1^35 = 0.0 |
|  | 32¢ | 1 | ×0.1^62 = 0.0 |
|  | 10¢ | 5 | ×0.1^84 = 0.0 |
|  | 1¢ | 1,994 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem`
2. `usgubewc-usgub-tn-2026-11-03-rep` ← this one

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
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 1 @ 30¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 78¢ | 1 | ×0.1^48 = 0.0 |
|  | 94¢ | 1 | ×0.1^64 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^67 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-pa-2026-11-03-rep</code> SELL 1 @ 10¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 42¢ | 1 | ×0.1^32 = 0.0 |
|  | 43¢ | 1 | ×0.1^33 = 0.0 |
|  | 50¢ | 100 | ×0.1^40 = 0.0 |
|  | 97¢ | 32 | ×0.1^87 = 0.0 |
|  | 99¢ | 5,225 | ×0.1^89 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem`
2. `usgubewc-usgub-pa-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 4 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 4 (4 yours) | ×0.1^0 = 4.0 |
|  | 58¢ | 1 | ×0.1^36 = 0.0 |
|  | 39¢ | 1 | ×0.1^55 = 0.0 |
|  | 27¢ | 1 | ×0.1^67 = 0.0 |
|  | 24¢ | 5 | ×0.1^70 = 0.0 |
|  | 7¢ | 6 | ×0.1^87 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **4.0** |

`yours 4.0 / Σ 4.0 = 100.0%`  
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
<details><summary><code>ussewc-usse-ma-2026-11-03-rep</code> SELL 1 @ 6¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem`
2. `ussewc-usse-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> SELL 1 @ 12¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 99¢ | 1,999 | ×0.1^87 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

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
<details><summary><code>ussewc-usse-tn-2026-11-03-dem</code> SELL 1 @ 7¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 98¢ | 132,784 | ×0.1^91 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem` ← this one
2. `ussewc-usse-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> BUY 3 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 61¢ | 4 | ×0.1^33 = 0.0 |
|  | 56¢ | 1 | ×0.1^38 = 0.0 |
|  | 42¢ | 1 | ×0.1^52 = 0.0 |
|  | 35¢ | 1 | ×0.1^59 = 0.0 |
|  | 32¢ | 1 | ×0.1^62 = 0.0 |
|  | 13¢ | 1 | ×0.1^81 = 0.0 |
|  | 10¢ | 5 | ×0.1^84 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem`
2. `usgubewc-usgub-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> SELL 1 @ 21¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 95¢ | 1 | ×0.1^74 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^77 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ma-2026-11-03-dem</code> BUY 5 @ 81¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 81¢ | 5 (5 yours) | ×0.1^0 = 5.0 |
|  | 64¢ | 8 | ×0.1^17 = 0.0 |
|  | 59¢ | 1 | ×0.1^22 = 0.0 |
|  | 43¢ | 1 | ×0.1^38 = 0.0 |
|  | 31¢ | 1 | ×0.1^50 = 0.0 |
|  | 10¢ | 5 | ×0.1^71 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^80 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-dem</code> BUY 3 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 59¢ | 1 | ×0.1^35 = 0.0 |
|  | 57¢ | 5 | ×0.1^37 = 0.0 |
|  | 53¢ | 1 | ×0.1^41 = 0.0 |
|  | 50¢ | 10 | ×0.1^44 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem` ← this one
2. `ussewc-usse-va-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-dem</code> SELL 1 @ 7¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 20¢ | 1 | ×0.1^13 = 0.0 |
|  | 58¢ | 1 | ×0.1^51 = 0.0 |
|  | 63¢ | 1 | ×0.1^56 = 0.0 |
|  | 98¢ | 2,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 1 @ 31¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 31¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 49¢ | 244 | ×0.2^18 = 0.0 |
|  | 50¢ | 100 | ×0.2^19 = 0.0 |
|  | 60¢ | 0 | ×0.2^29 = 0.0 |
|  | 63¢ | 0 | ×0.2^32 = 0.0 |
|  | 66¢ | 0 | ×0.2^35 = 0.0 |
|  | 67¢ | 0 | ×0.2^36 = 0.0 |
|  | 70¢ | 0 | ×0.2^39 = 0.0 |
|  | 71¢ | 0 | ×0.2^40 = 0.0 |
|  | 73¢ | 0 | ×0.2^42 = 0.0 |
| | … | +1 levels | 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48` ← this one
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 30 @ 13¢ → $12.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 30 (30 yours) | ×0.1^0 = 30.0 |
|  | 5¢ | 30 | ×0.1^8 = 0.0 |
|  | 4¢ | 80 | ×0.1^9 = 0.0 |
|  | 2¢ | 10,250 | ×0.1^11 = 0.0 |
| | | **Σ** | **30.0** |

`yours 30.0 / Σ 30.0 = 100.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 100.0% = $12.50/day`  

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,085 resting) | ~28.4% | ~$7.11 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (274,838 resting) | ~8.2% | ~$6.16 |
| `ewc-usse-mi-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (630,475 resting) | ~71.9% | ~$4.49 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (64,642 resting) | ~3.1% | ~$2.36 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,853 resting) | ~8.5% | ~$2.13 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (76,444 resting) | ~29.3% | ~$1.83 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (304,142 resting) | ~2.4% | ~$1.81 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (100,576 resting) | ~2.1% | ~$1.60 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,242,682 resting) | ~24.9% | ~$1.55 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (358,458 resting) | ~24.4% | ~$1.53 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,266 resting) | ~6.0% | ~$1.49 |
| `enwc-usgubp-fl-2026-08-18-rep-jaycol` | $300.00 ÷ 3 | 0.20 | 10,000 | SELL side (161,009 resting) | ~2.8% | ~$1.42 |

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
| 2026-08-17 8:06 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 7:50 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 7:04 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 6:54 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 6:38 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 6:34 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 6:19 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 5:35 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 4:34 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 3:34 AM ET | ✅ ok | 2700 | $4920.49 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
