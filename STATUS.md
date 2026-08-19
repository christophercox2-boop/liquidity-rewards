# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-19 3:37 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$399.58/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$20.80/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$11.16/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$11.13/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$399.58/day (~$16.65/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 45.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (400,602 resting ≥ 5,000 ✓) ≈ $4.17/day (event pool ÷ 12 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | SELL | 18.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (141,887 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (70,536 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 21.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.8% of ask side (91,911 resting ≥ 5,000 ✓) ≈ $3.84/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | BUY | 95.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~99.6% of bid side (500,398 resting ≥ 2,000 ✓) ≈ $6.23/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 10.0¢ | 122 | 0 | $200.00 | ✅ scoring — ~98.8% of bid side (96,940 resting ≥ 20,000 ✓) ≈ $5.81/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 65 | 0 | $200.00 | ✅ scoring — ~96.3% of bid side (106,823 resting ≥ 20,000 ✓) ≈ $5.66/day (event pool ÷ 17 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~94.7% of ask side (66,195 resting ≥ 2,000 ✓) ≈ $5.92/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~94.3% of bid side (4,087 resting ≥ 2,000 ✓) ≈ $5.90/day (event pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.8% of ask side (69,029 resting ≥ 2,000 ✓) ≈ $5.67/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 8.0¢ | 64 | 1 | $200.00 | ✅ scoring — ~89.6% of bid side (150,908 resting ≥ 20,000 ✓) ≈ $5.27/day (event pool ÷ 17 markets) |
| `ussewc-usse-il-2026-11-03-rep` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~89.6% of ask side (330,232 resting ≥ 2,000 ✓) ≈ $5.60/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~89.5% of bid side (50,361 resting ≥ 20,000 ✓) ≈ $3.31/day (event pool ÷ 27 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 22.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~86.6% of ask side (92,795 resting ≥ 5,000 ✓) ≈ $3.33/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~82.5% of bid side (2,108 resting ≥ 2,000 ✓) ≈ $5.16/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 14.0¢ | 3 | 2 | $25.00 | ✅ scoring — ~77.2% of bid side (37,152 resting ≥ 2,000 ✓) ≈ $4.82/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 10.0¢ | 82 | 1 | $200.00 | ✅ scoring — ~73.8% of bid side (71,223 resting ≥ 20,000 ✓) ≈ $5.27/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-ma-2026-11-03-rep` | BUY | 1.0¢ | 1,666 | 1 | $25.00 | ✅ scoring — ~73.2% of bid side (2,267 resting ≥ 2,000 ✓) ≈ $4.57/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | BUY | 21.0¢ | 23 | 0 | $200.00 | ✅ scoring — ~73.1% of bid side (221,796 resting ≥ 20,000 ✓) ≈ $4.30/day (event pool ÷ 17 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 95.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~68.5% of bid side (600,246 resting ≥ 2,000 ✓) ≈ $4.28/day (event pool ÷ 2 markets) |
| `ussewc-usse-ma-2026-11-03-dem` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~68.2% of bid side (600,470 resting ≥ 2,000 ✓) ≈ $4.26/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-rep` | BUY | 91.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (500,301 resting ≥ 2,000 ✓) ≈ $4.17/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 85.0¢ | 2 | 2 | $25.00 | ✅ scoring — ~66.5% of bid side (502,164 resting ≥ 2,000 ✓) ≈ $4.16/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~61.5% of bid side (2,123 resting ≥ 2,000 ✓) ≈ $3.84/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 7.0¢ | 24 | 0 | $25.00 | ✅ scoring — ~56.9% of ask side (65,569 resting ≥ 2,000 ✓) ≈ $3.55/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~55.5% of ask side (196,045 resting ≥ 2,000 ✓) ≈ $3.47/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 120 | 1 | $200.00 | ✅ scoring — ~52.4% of bid side (64,573 resting ≥ 20,000 ✓) ≈ $1.94/day (event pool ÷ 27 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 95.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~50.6% of bid side (500,461 resting ≥ 2,000 ✓) ≈ $3.17/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 93.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (500,260 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 93.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (500,260 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| …and 2859 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 1 @ 45¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 25¢ | 1 | ×0.2^20 = 0.0 |
|  | 19¢ | 150 | ×0.2^26 = 0.0 |
|  | 2¢ | 400,250 | ×0.2^43 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210` ← this one
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> SELL 1 @ 18¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 26¢ | 50 | ×0.1^8 = 0.0 |
|  | 83¢ | 0 | ×0.1^65 = 0.0 |
|  | 85¢ | 6,000 | ×0.1^67 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> SELL 1 @ 8¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 12¢ | 1 | ×0.1^4 = 0.0 |
|  | 13¢ | 2 | ×0.1^5 = 0.0 |
|  | 15¢ | 3 | ×0.1^7 = 0.0 |
|  | 16¢ | 1 | ×0.1^8 = 0.0 |
|  | 17¢ | 53 | ×0.1^9 = 0.0 |
|  | 32¢ | 5,000 | ×0.1^24 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 1 @ 21¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 28¢ | 117 | ×0.2^7 = 0.0 |
|  | 29¢ | 50 | ×0.2^8 = 0.0 |
|  | 67¢ | 51 | ×0.2^46 = 0.0 |
|  | 68¢ | 1 | ×0.2^47 = 0.0 |
|  | 69¢ | 1 | ×0.2^48 = 0.0 |
|  | 70¢ | 1 | ×0.2^49 = 0.0 |
|  | 71¢ | 1 | ×0.2^50 = 0.0 |
|  | 72¢ | 1 | ×0.2^51 = 0.0 |
|  | 73¢ | 1 | ×0.2^52 = 0.0 |
| | … | +24 levels | 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
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
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> BUY 5 @ 95¢ → $6.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 5 (5 yours) | ×0.1^0 = 5.0 |
|  | 15¢ | 8 | ×0.1^80 = 0.0 |
|  | 2¢ | 500,185 | ×0.1^93 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 99.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.6% = $6.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 122 @ 10¢ → $5.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 123 (122 yours) | ×0.2^0 = 123.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 6¢ | 255 | ×0.2^4 = 0.4 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 4¢ | 110 | ×0.2^6 = 0.0 |
|  | 2¢ | 26,000 | ×0.2^8 = 0.1 |
| | | **Σ** | **123.5** |

`yours 122.0 / Σ 123.5 = 98.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 98.8% = $5.81/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha` ← this one
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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 65 @ 12¢ → $5.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 67 (65 yours) | ×0.2^0 = 67.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 8¢ | 6 | ×0.2^4 = 0.0 |
|  | 6¢ | 112 | ×0.2^6 = 0.0 |
|  | 3¢ | 184 | ×0.2^9 = 0.0 |
|  | 2¢ | 86,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **67.5** |

`yours 65.0 / Σ 67.5 = 96.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 96.3% = $5.66/day`  

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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $5.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 9¢ | 1 | ×0.1^1 = 0.1 |
|  | 10¢ | 1 | ×0.1^2 = 0.0 |
|  | 11¢ | 2 | ×0.1^3 = 0.0 |
|  | 13¢ | 2 | ×0.1^5 = 0.0 |
|  | 14¢ | 2 | ×0.1^6 = 0.0 |
|  | 15¢ | 160 | ×0.1^7 = 0.0 |
|  | 18¢ | 50 | ×0.1^10 = 0.0 |
|  | 45¢ | 500 | ×0.1^37 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^90 = 0.0 |
| | | **Σ** | **2.1** |

`yours 2.0 / Σ 2.1 = 94.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.7% = $5.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 2 @ 7¢ → $5.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 6¢ | 1 | ×0.1^1 = 0.1 |
|  | 5¢ | 1 | ×0.1^2 = 0.0 |
|  | 3¢ | 42 | ×0.1^4 = 0.0 |
|  | 2¢ | 243 | ×0.1^5 = 0.0 |
|  | 1¢ | 3,798 | ×0.1^6 = 0.0 |
| | | **Σ** | **2.1** |

`yours 2.0 / Σ 2.1 = 94.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.3% = $5.90/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> SELL 1 @ 8¢ → $5.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 9¢ | 1 | ×0.1^1 = 0.1 |
|  | 11¢ | 1 | ×0.1^3 = 0.0 |
|  | 12¢ | 1 | ×0.1^4 = 0.0 |
|  | 13¢ | 50 | ×0.1^5 = 0.0 |
|  | 48¢ | 3,000 | ×0.1^40 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.8% = $5.67/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 64 @ 8¢ → $5.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 8¢ | 64 (64 yours) | ×0.2^1 = 12.7 |
|  | 4¢ | 273 | ×0.2^5 = 0.1 |
|  | 3¢ | 110 | ×0.2^6 = 0.0 |
|  | 1¢ | 150,460 | ×0.2^8 = 0.4 |
| | | **Σ** | **14.2** |

`yours 12.7 / Σ 14.2 = 89.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 89.6% = $5.27/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes` ← this one
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
<details><summary><code>ussewc-usse-il-2026-11-03-rep</code> SELL 1 @ 5¢ → $5.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 6¢ | 1 | ×0.1^1 = 0.1 |
|  | 7¢ | 1 | ×0.1^2 = 0.0 |
|  | 8¢ | 1 | ×0.1^3 = 0.0 |
|  | 9¢ | 53 | ×0.1^4 = 0.0 |
|  | 29¢ | 1 | ×0.1^24 = 0.0 |
|  | 44¢ | 1 | ×0.1^39 = 0.0 |
|  | 60¢ | 1 | ×0.1^55 = 0.0 |
|  | 98¢ | 132,784 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 89.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.6% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem`
2. `ussewc-usse-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 150 (135 yours) | ×0.2^0 = 150.1 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **150.8** |

`yours 135.0 / Σ 150.8 = 89.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 89.5% = $3.31/day`  

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
10. `ewc-usp-2028-11-07-jbpri` ← this one
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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 1 @ 22¢ → $3.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 23¢ | 1 | ×0.2^1 = 0.1 |
|  | 24¢ | 1 | ×0.2^2 = 0.0 |
|  | 25¢ | 1 | ×0.2^3 = 0.0 |
|  | 26¢ | 1 | ×0.2^4 = 0.0 |
|  | 27¢ | 1 | ×0.2^5 = 0.0 |
|  | 28¢ | 1 | ×0.2^6 = 0.0 |
|  | 29¢ | 88 | ×0.2^7 = 0.0 |
|  | 30¢ | 1 | ×0.2^8 = 0.0 |
|  | 31¢ | 1 | ×0.2^9 = 0.0 |
| | … | +9 levels | 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 86.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 86.6% = $3.33/day`  

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
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $5.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 8 | ×0.1^0 = 8.0 |
| ▶ | 1¢ | 2,100 (1,799 yours) | ×0.1^1 = 210.0 |
| | | **Σ** | **218.0** |

`yours 179.9 / Σ 218.0 = 82.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 82.5% = $5.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 3 @ 14¢ → $4.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.1^0 = 0.0 |
| ▶ | 14¢ | 3 (3 yours) | ×0.1^2 = 0.0 |
|  | 12¢ | 1 | ×0.1^4 = 0.0 |
|  | 11¢ | 1 | ×0.1^5 = 0.0 |
|  | 10¢ | 1 | ×0.1^6 = 0.0 |
|  | 7¢ | 26 | ×0.1^9 = 0.0 |
|  | 4¢ | 123 | ×0.1^12 = 0.0 |
|  | 2¢ | 15,000 | ×0.1^14 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 77.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 77.2% = $4.82/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 82 @ 10¢ → $5.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 5 | ×0.2^0 = 5.2 |
| ▶ | 10¢ | 85 (82 yours) | ×0.2^1 = 17.0 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 3¢ | 1 | ×0.2^8 = 0.0 |
|  | 2¢ | 472 | ×0.2^9 = 0.0 |
|  | 1¢ | 70,659 | ×0.2^10 = 0.0 |
| | | **Σ** | **22.2** |

`yours 16.4 / Σ 22.2 = 73.8%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 73.8% = $5.27/day`  

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
<details><summary><code>usgubewc-usgub-ma-2026-11-03-rep</code> BUY 1,666 @ 1¢ → $4.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 2,266 (1,666 yours) | ×0.1^1 = 226.6 |
| | | **Σ** | **227.6** |

`yours 166.6 / Σ 227.6 = 73.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 73.2% = $4.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem`
2. `usgubewc-usgub-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> BUY 23 @ 21¢ → $4.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 24 (23 yours) | ×0.2^0 = 24.1 |
|  | 20¢ | 1 | ×0.2^1 = 0.2 |
|  | 19¢ | 8 | ×0.2^2 = 0.3 |
|  | 18¢ | 6 | ×0.2^3 = 0.0 |
|  | 17¢ | 112 | ×0.2^4 = 0.2 |
|  | 16¢ | 21,110 | ×0.2^5 = 6.8 |
| | | **Σ** | **31.6** |

`yours 23.1 / Σ 31.6 = 73.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 73.1% = $4.30/day`  

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
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> BUY 5 @ 95¢ → $4.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 7 (5 yours) | ×0.1^0 = 7.0 |
|  | 94¢ | 3 | ×0.1^1 = 0.3 |
|  | 46¢ | 11 | ×0.1^49 = 0.0 |
|  | 40¢ | 25 | ×0.1^55 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **7.3** |

`yours 5.0 / Σ 7.3 = 68.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 68.5% = $4.28/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ma-2026-11-03-dem</code> BUY 3 @ 94¢ → $4.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 4 (3 yours) | ×0.1^0 = 4.0 |
|  | 92¢ | 35 | ×0.1^2 = 0.4 |
|  | 91¢ | 50 | ×0.1^3 = 0.1 |
|  | 3¢ | 181 | ×0.1^91 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **4.4** |

`yours 3.0 / Σ 4.4 = 68.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 68.2% = $4.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem` ← this one
2. `ussewc-usse-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-rep</code> BUY 4 @ 91¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 6 (4 yours) | ×0.1^0 = 6.0 |
|  | 83¢ | 80 | ×0.1^8 = 0.0 |
|  | 68¢ | 5 | ×0.1^23 = 0.0 |
|  | 31¢ | 1 | ×0.1^60 = 0.0 |
|  | 15¢ | 9 | ×0.1^76 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^89 = 0.0 |
| | | **Σ** | **6.0** |

`yours 4.0 / Σ 6.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem`
2. `ussewc-usse-la-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 2 @ 85¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 87¢ | 0 | ×0.1^0 = 0.0 |
| ▶ | 85¢ | 2 (2 yours) | ×0.1^2 = 0.0 |
|  | 84¢ | 0 | ×0.1^3 = 0.0 |
|  | 82¢ | 5 | ×0.1^5 = 0.0 |
|  | 74¢ | 152 | ×0.1^13 = 0.0 |
|  | 60¢ | 1 | ×0.1^27 = 0.0 |
|  | 10¢ | 5 | ×0.1^77 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 66.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.5% = $4.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 10 @ 12¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 16 (10 yours) | ×0.1^0 = 16.0 |
|  | 11¢ | 2 | ×0.1^1 = 0.2 |
|  | 10¢ | 6 | ×0.1^2 = 0.1 |
|  | 1¢ | 2,099 | ×0.1^11 = 0.0 |
| | | **Σ** | **16.3** |

`yours 10.0 / Σ 16.3 = 61.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.5% = $3.84/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 24 @ 7¢ → $3.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 42 (24 yours) | ×0.1^0 = 42.0 |
|  | 8¢ | 2 | ×0.1^1 = 0.2 |
|  | 16¢ | 50 | ×0.1^9 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^91 = 0.0 |
| | | **Σ** | **42.2** |

`yours 24.0 / Σ 42.2 = 56.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 56.9% = $3.55/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 10 @ 13¢ → $3.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 18 (10 yours) | ×0.1^0 = 18.0 |
|  | 15¢ | 1 | ×0.1^2 = 0.0 |
|  | 25¢ | 50 | ×0.1^12 = 0.0 |
|  | 40¢ | 1 | ×0.1^27 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^85 = 0.0 |
| | | **Σ** | **18.0** |

`yours 10.0 / Σ 18.0 = 55.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 55.5% = $3.47/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 120 @ 5¢ → $1.94/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 5¢ | 120 (120 yours) | ×0.2^1 = 24.0 |
|  | 4¢ | 4 | ×0.2^2 = 0.2 |
|  | 3¢ | 3 | ×0.2^3 = 0.0 |
|  | 2¢ | 2 | ×0.2^4 = 0.0 |
|  | 1¢ | 64,443 | ×0.2^5 = 20.6 |
| | | **Σ** | **45.8** |

`yours 24.0 / Σ 45.8 = 52.4%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 52.4% = $1.94/day`  

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
26. `ewc-usp-2028-11-07-vivram` ← this one
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 35 @ 95¢ → $3.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 63 (35 yours) | ×0.1^0 = 63.0 |
|  | 94¢ | 46 | ×0.1^1 = 4.6 |
|  | 93¢ | 151 | ×0.1^2 = 1.5 |
|  | 58¢ | 1 | ×0.1^37 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **69.1** |

`yours 35.0 / Σ 69.1 = 50.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.6% = $3.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 3 @ 93¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 6 (3 yours) | ×0.1^0 = 6.0 |
|  | 84¢ | 50 | ×0.1^9 = 0.0 |
|  | 63¢ | 0 | ×0.1^30 = 0.0 |
|  | 10¢ | 4 | ×0.1^83 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **6.0** |

`yours 3.0 / Σ 6.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 3 @ 93¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 6 (3 yours) | ×0.1^0 = 6.0 |
|  | 84¢ | 50 | ×0.1^9 = 0.0 |
|  | 63¢ | 0 | ×0.1^30 = 0.0 |
|  | 10¢ | 4 | ×0.1^83 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **6.0** |

`yours 3.0 / Σ 6.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,337 resting) | ~83.2% | ~$20.80 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,007 resting) | ~14.9% | ~$11.16 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,036 resting) | ~44.5% | ~$11.13 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (65,628 resting) | ~13.5% | ~$10.15 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (80,043 resting) | ~98.1% | ~$6.13 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (522,011 resting) | ~7.8% | ~$5.86 |
| `ewc-usse-mi-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (632,617 resting) | ~71.6% | ~$4.48 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (26,301 resting) | ~5.8% | ~$4.34 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (285,589 resting) | ~3.4% | ~$2.57 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (388,247 resting) | ~41.0% | ~$2.56 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (669,219 resting) | ~2.8% | ~$2.11 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (825,913 resting) | ~2.8% | ~$2.06 |

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
| 2026-08-19 3:37 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 2:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 11:59 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 10:58 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 9:44 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 8:44 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 7:22 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 6:21 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 5:21 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 4:20 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
