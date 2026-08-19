# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-18 8:38 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$241.86/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$10.67/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$10.59/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$5.61/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$241.86/day (~$10.08/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-pa-2026-11-03-rep` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (5,358 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ma-2026-11-03-dem` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,215 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,207 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | BUY | 84.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (700,205 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-rep` | BUY | 74.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,215 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 25.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~99.9% of bid side (102,349 resting ≥ 20,000 ✓) ≈ $5.88/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 20.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (200,996 resting ≥ 5,000 ✓) ≈ $3.84/day (event pool ÷ 13 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~99.5% of ask side (66,139 resting ≥ 2,000 ✓) ≈ $6.22/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 37.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~95.2% of bid side (400,602 resting ≥ 5,000 ✓) ≈ $3.97/day (event pool ÷ 12 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~93.9% of ask side (265,861 resting ≥ 2,000 ✓) ≈ $5.87/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 9.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~88.5% of bid side (50,414 resting ≥ 5,000 ✓) ≈ $3.40/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 7.0¢ | 27 | 0 | $25.00 | ✅ scoring — ~87.1% of ask side (65,557 resting ≥ 2,000 ✓) ≈ $5.44/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 10.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~83.9% of bid side (340,539 resting ≥ 5,000 ✓) ≈ $3.23/day (event pool ÷ 13 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~81.8% of bid side (4,290 resting ≥ 2,000 ✓) ≈ $5.11/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~78.3% of bid side (2,029 resting ≥ 2,000 ✓) ≈ $4.89/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~76.6% of bid side (2,035 resting ≥ 2,000 ✓) ≈ $3.19/day (event pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 14.0¢ | 86 | 0 | $100.00 | ✅ scoring — ~75.2% of bid side (301,490 resting ≥ 5,000 ✓) ≈ $2.89/day (event pool ÷ 13 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 9.0¢ | 135 | 2 | $200.00 | ✅ scoring — ~74.9% of bid side (51,272 resting ≥ 20,000 ✓) ≈ $5.35/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | BUY | 22.0¢ | 63 | 1 | $200.00 | ✅ scoring — ~73.2% of bid side (216,980 resting ≥ 20,000 ✓) ≈ $4.31/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~59.7% of bid side (86,918 resting ≥ 20,000 ✓) ≈ $3.51/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-aleocc` | BUY | 21.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~52.7% of bid side (67,197 resting ≥ 20,000 ✓) ≈ $3.10/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-kamhar` | SELL | 5.0¢ | 286 | 0 | $200.00 | ✅ scoring — ~44.8% of ask side (57,341 resting ≥ 20,000 ✓) ≈ $1.66/day (event pool ÷ 27 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~40.4% of bid side (2,046 resting ≥ 2,000 ✓) ≈ $2.52/day (event pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~39.9% of bid side (31,223 resting ≥ 5,000 ✓) ≈ $9.97/day (event pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 95.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~39.4% of bid side (500,487 resting ≥ 2,000 ✓) ≈ $2.46/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~36.7% of ask side (92,811 resting ≥ 5,000 ✓) ≈ $1.41/day (event pool ÷ 13 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~34.5% of ask side (196,063 resting ≥ 2,000 ✓) ≈ $2.15/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 91.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~31.9% of bid side (500,664 resting ≥ 2,000 ✓) ≈ $2.00/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 91.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~31.9% of bid side (500,664 resting ≥ 2,000 ✓) ≈ $2.00/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 91.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~31.9% of bid side (500,664 resting ≥ 2,000 ✓) ≈ $2.00/day (event pool ÷ 2 markets) |
| …and 1569 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-pa-2026-11-03-rep</code> SELL 1 @ 7¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 50¢ | 100 | ×0.1^43 = 0.0 |
|  | 97¢ | 32 | ×0.1^90 = 0.0 |
|  | 99¢ | 5,225 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem`
2. `usgubewc-usgub-pa-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ma-2026-11-03-dem</code> BUY 3 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 54¢ | 1 | ×0.1^40 = 0.0 |
|  | 48¢ | 4 | ×0.1^46 = 0.0 |
|  | 43¢ | 1 | ×0.1^51 = 0.0 |
|  | 31¢ | 1 | ×0.1^63 = 0.0 |
|  | 10¢ | 5 | ×0.1^84 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 3 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 10¢ | 4 | ×0.1^84 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> BUY 2 @ 84¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 7¢ | 3 | ×0.1^77 = 0.0 |
|  | 2¢ | 700,000 | ×0.1^82 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> BUY 3 @ 74¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 63¢ | 4 | ×0.1^11 = 0.0 |
|  | 56¢ | 1 | ×0.1^18 = 0.0 |
|  | 35¢ | 1 | ×0.1^39 = 0.0 |
|  | 13¢ | 1 | ×0.1^61 = 0.0 |
|  | 10¢ | 5 | ×0.1^64 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^72 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem`
2. `usgubewc-usgub-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 1 @ 25¢ → $5.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 20¢ | 1 | ×0.2^5 = 0.0 |
|  | 17¢ | 62 | ×0.2^8 = 0.0 |
|  | 15¢ | 697 | ×0.2^10 = 0.0 |
|  | 10¢ | 51,250 | ×0.2^15 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 99.9% = $5.88/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss` ← this one
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5 @ 20¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 15¢ | 30 | ×0.2^5 = 0.0 |
|  | 14¢ | 2 | ×0.2^6 = 0.0 |
|  | 11¢ | 54 | ×0.2^9 = 0.0 |
|  | 10¢ | 70 | ×0.2^10 = 0.0 |
|  | 2¢ | 326 | ×0.2^18 = 0.0 |
|  | 1¢ | 200,509 | ×0.2^19 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 99.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.8% = $3.84/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49` ← this one
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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $6.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 10¢ | 1 | ×0.1^2 = 0.0 |
|  | 13¢ | 1 | ×0.1^5 = 0.0 |
|  | 15¢ | 160 | ×0.1^7 = 0.0 |
|  | 45¢ | 500 | ×0.1^37 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^90 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 99.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.5% = $6.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 1 @ 37¢ → $3.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 9¢ | 150 | ×0.2^28 = 0.0 |
|  | 2¢ | 400,250 | ×0.2^35 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 95.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 95.2% = $3.97/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215` ← this one
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> SELL 1 @ 8¢ → $5.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 11¢ | 65 | ×0.1^3 = 0.1 |
|  | 17¢ | 1 | ×0.1^9 = 0.0 |
|  | 25¢ | 2 | ×0.1^17 = 0.0 |
|  | 98¢ | 265,567 | ×0.1^90 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 93.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.9% = $5.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1 @ 9¢ → $3.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 0 | ×0.2^2 = 0.0 |
|  | 1¢ | 50,413 | ×0.2^8 = 0.1 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.5% = $3.40/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54` ← this one
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 27 @ 7¢ → $5.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 31 (27 yours) | ×0.1^0 = 31.0 |
|  | 16¢ | 50 | ×0.1^9 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^91 = 0.0 |
| | | **Σ** | **31.0** |

`yours 27.0 / Σ 31.0 = 87.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 87.1% = $5.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 10¢ → $3.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 0 | ×0.2^1 = 0.0 |
|  | 1¢ | 340,538 | ×0.2^9 = 0.2 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 83.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 83.9% = $3.23/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52` ← this one
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 2 @ 7¢ → $5.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 6¢ | 4 | ×0.1^1 = 0.4 |
|  | 5¢ | 1 | ×0.1^2 = 0.0 |
|  | 3¢ | 285 | ×0.1^4 = 0.0 |
|  | 2¢ | 200 | ×0.1^5 = 0.0 |
|  | 1¢ | 3,798 | ×0.1^6 = 0.0 |
| | | **Σ** | **2.4** |

`yours 2.0 / Σ 2.4 = 81.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 81.8% = $5.11/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $4.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 30 | ×0.1^0 = 30.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **229.9** |

`yours 179.9 / Σ 229.9 = 78.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 78.3% = $4.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $3.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 35 | ×0.1^0 = 35.0 |
| ▶ | 1¢ | 2,000 (1,799 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **235.0** |

`yours 179.9 / Σ 235.0 = 76.6%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 76.6% = $3.19/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 86 @ 14¢ → $2.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 107 (86 yours) | ×0.2^0 = 106.7 |
|  | 11¢ | 909 | ×0.2^3 = 7.3 |
|  | 1¢ | 300,474 | ×0.2^13 = 0.0 |
| | | **Σ** | **114.0** |

`yours 85.7 / Σ 114.0 = 75.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 75.2% = $2.89/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51` ← this one
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 135 @ 9¢ → $5.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 1.0 |
|  | 10¢ | 4 | ×0.2^1 = 0.8 |
| ▶ | 9¢ | 135 (135 yours) | ×0.2^2 = 5.4 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 2¢ | 472 | ×0.2^9 = 0.0 |
|  | 1¢ | 50,659 | ×0.2^10 = 0.0 |
| | | **Σ** | **7.2** |

`yours 5.4 / Σ 7.2 = 74.9%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 74.9% = $5.35/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes` ← this one
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> BUY 63 @ 22¢ → $4.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 3 | ×0.2^0 = 3.0 |
| ▶ | 22¢ | 65 (63 yours) | ×0.2^1 = 13.0 |
|  | 21¢ | 24 | ×0.2^2 = 1.0 |
|  | 20¢ | 1 | ×0.2^3 = 0.0 |
|  | 19¢ | 8 | ×0.2^4 = 0.0 |
|  | 18¢ | 21 | ×0.2^5 = 0.0 |
|  | 17¢ | 298 | ×0.2^6 = 0.0 |
|  | 16¢ | 16,110 | ×0.2^7 = 0.2 |
|  | 5¢ | 50,000 | ×0.2^18 = 0.0 |
| | | **Σ** | **17.2** |

`yours 12.6 / Σ 17.2 = 73.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 73.2% = $4.31/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew` ← this one
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 1 @ 12¢ → $3.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 8¢ | 138 | ×0.2^4 = 0.2 |
|  | 6¢ | 112 | ×0.2^6 = 0.0 |
|  | 4¢ | 30 | ×0.2^8 = 0.0 |
|  | 3¢ | 184 | ×0.2^9 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.7** |

`yours 1.0 / Σ 1.7 = 59.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 59.7% = $3.51/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut` ← this one
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-aleocc</code> BUY 20 @ 21¢ → $3.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 33 (20 yours) | ×0.2^0 = 33.0 |
|  | 18¢ | 612 | ×0.2^3 = 4.9 |
|  | 13¢ | 16,250 | ×0.2^8 = 0.0 |
|  | 1¢ | 50,303 | ×0.2^20 = 0.0 |
| | | **Σ** | **37.9** |

`yours 20.0 / Σ 37.9 = 52.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 52.7% = $3.10/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc` ← this one
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-kamhar</code> SELL 286 @ 5¢ → $1.66/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 638 (286 yours) | ×0.2^0 = 638.0 |
|  | 14¢ | 61 | ×0.2^9 = 0.0 |
|  | 19¢ | 21,724 | ×0.2^14 = 0.0 |
| | | **Σ** | **638.0** |

`yours 286.0 / Σ 638.0 = 44.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 44.8% = $1.66/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 10 @ 12¢ → $2.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 24 (10 yours) | ×0.1^0 = 24.0 |
|  | 11¢ | 6 | ×0.1^1 = 0.6 |
|  | 10¢ | 17 | ×0.1^2 = 0.2 |
|  | 1¢ | 1,999 | ×0.1^11 = 0.0 |
| | | **Σ** | **24.8** |

`yours 10.0 / Σ 24.8 = 40.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 40.4% = $2.52/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $9.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,399 (1,000 yours) | ×0.2^0 = 2,399.0 |
|  | 7¢ | 1,390 | ×0.2^2 = 55.6 |
|  | 6¢ | 6,628 | ×0.2^3 = 53.0 |
| | | **Σ** | **2,507.7** |

`yours 1,000.0 / Σ 2,507.7 = 39.9%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 39.9% = $9.97/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 35 @ 95¢ → $2.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 88 (35 yours) | ×0.1^0 = 88.0 |
|  | 94¢ | 4 | ×0.1^1 = 0.4 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 58¢ | 1 | ×0.1^37 = 0.0 |
|  | 12¢ | 144 | ×0.1^83 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **88.9** |

`yours 35.0 / Σ 88.9 = 39.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 39.4% = $2.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 15 @ 18¢ → $1.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 40 (15 yours) | ×0.2^0 = 39.6 |
|  | 19¢ | 0 | ×0.2^1 = 0.0 |
|  | 21¢ | 20 | ×0.2^3 = 0.2 |
|  | 22¢ | 27 | ×0.2^4 = 0.0 |
|  | 23¢ | 5 | ×0.2^5 = 0.0 |
|  | 24¢ | 5 | ×0.2^6 = 0.0 |
|  | 25¢ | 10 | ×0.2^7 = 0.0 |
|  | 26¢ | 5 | ×0.2^8 = 0.0 |
|  | 27¢ | 5 | ×0.2^9 = 0.0 |
|  | 35¢ | 1 | ×0.2^17 = 0.0 |
| | … | +5 levels | 0.0 |
| | | **Σ** | **39.9** |

`yours 14.6 / Σ 39.9 = 36.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 36.7% = $1.41/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50` ← this one
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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 10 @ 13¢ → $2.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 29 (10 yours) | ×0.1^0 = 29.0 |
|  | 15¢ | 1 | ×0.1^2 = 0.0 |
|  | 25¢ | 50 | ×0.1^12 = 0.0 |
|  | 35¢ | 7 | ×0.1^22 = 0.0 |
|  | 40¢ | 1 | ×0.1^27 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^85 = 0.0 |
| | | **Σ** | **29.0** |

`yours 10.0 / Σ 29.0 = 34.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 34.5% = $2.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 3 @ 91¢ → $2.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 9 (3 yours) | ×0.1^0 = 9.0 |
|  | 88¢ | 398 | ×0.1^3 = 0.4 |
|  | 75¢ | 50 | ×0.1^16 = 0.0 |
|  | 44¢ | 1 | ×0.1^47 = 0.0 |
|  | 38¢ | 1 | ×0.1^53 = 0.0 |
|  | 29¢ | 1 | ×0.1^62 = 0.0 |
|  | 10¢ | 4 | ×0.1^81 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^89 = 0.0 |
| | | **Σ** | **9.4** |

`yours 3.0 / Σ 9.4 = 31.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 31.9% = $2.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 3 @ 91¢ → $2.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 9 (3 yours) | ×0.1^0 = 9.0 |
|  | 88¢ | 398 | ×0.1^3 = 0.4 |
|  | 75¢ | 50 | ×0.1^16 = 0.0 |
|  | 44¢ | 1 | ×0.1^47 = 0.0 |
|  | 38¢ | 1 | ×0.1^53 = 0.0 |
|  | 29¢ | 1 | ×0.1^62 = 0.0 |
|  | 10¢ | 4 | ×0.1^81 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^89 = 0.0 |
| | | **Σ** | **9.4** |

`yours 3.0 / Σ 9.4 = 31.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 31.9% = $2.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 3 @ 91¢ → $2.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 9 (3 yours) | ×0.1^0 = 9.0 |
|  | 88¢ | 398 | ×0.1^3 = 0.4 |
|  | 75¢ | 50 | ×0.1^16 = 0.0 |
|  | 44¢ | 1 | ×0.1^47 = 0.0 |
|  | 38¢ | 1 | ×0.1^53 = 0.0 |
|  | 29¢ | 1 | ×0.1^62 = 0.0 |
|  | 10¢ | 4 | ×0.1^81 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^89 = 0.0 |
| | | **Σ** | **9.4** |

`yours 3.0 / Σ 9.4 = 31.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 31.9% = $2.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (79,896 resting) | ~14.2% | ~$10.67 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,021 resting) | ~42.3% | ~$10.59 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,932 resting) | ~22.4% | ~$5.61 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (57,968 resting) | ~66.7% | ~$4.17 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (71,041 resting) | ~66.0% | ~$4.12 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (288,276 resting) | ~3.5% | ~$2.65 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (10,322 resting) | ~8.2% | ~$2.05 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (287,903 resting) | ~2.4% | ~$1.81 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (632,439 resting) | ~7.1% | ~$1.77 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,244,731 resting) | ~25.0% | ~$1.56 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (83,879 resting) | ~1.9% | ~$1.43 |
| `ewc-usse-ak-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (360,741 resting) | ~21.4% | ~$1.33 |

## Totals

| | Amount |
|---|---:|
| Paid | $4,919.08 |
| Pending | $197.10 |
| Skipped | $1.41 |
| **Total earned** | **$5,117.59** |

2859 reward rows · 45 days with rewards · 559 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-16 ⚠️ multi-day pending bucket | $197.03 | `███` |
| 2026-08-15 | $1,352.63 | `████████████████████` |
| 2026-08-14 | $274.92 | `████` |
| 2026-08-13 | $223.24 | `███` |
| 2026-08-12 | $213.04 | `███` |
| 2026-08-11 | $409.60 | `██████` |
| 2026-08-10 | $557.62 | `████████` |
| 2026-08-09 | $62.24 | `█` |
| 2026-08-08 | $54.83 | `█` |
| 2026-08-07 | $60.34 | `█` |
| 2026-08-06 | $52.22 | `█` |
| 2026-08-05 | $31.46 | `█` |
| 2026-08-04 | $53.94 | `█` |
| 2026-08-03 | $44.81 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $3,654.27 | `████████████████████` |
| 2026-07 | $1,463.32 | `████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $178.70 |
| `apdc-alito-2026-12-31` | $115.00 |
| `ewc-usp-party-2028-11-07-rep` | $100.01 |
| `ewc-usp-party-2028-11-07-dem` | $79.48 |
| `opdc-mcconnell-resign-2026-11-02` | $79.41 |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | $66.06 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $63.61 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $62.40 |
| `enwc-uspres-nom-rep-2028-rondes` | $48.49 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.60 |
| `enwc-uspres-nom-dem-2028-stasmi` | $44.12 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.51 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.04 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-18 8:38 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:34 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:31 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:27 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:23 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:18 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:14 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:11 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:07 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:03 PM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
