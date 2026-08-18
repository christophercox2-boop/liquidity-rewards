# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-18 6:33 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$269.78/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$20.51/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$19.04/day), `ewc-usgub-ga-2026-11-03-dem` (~$10.58/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$269.78/day (~$11.24/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-ok-2026-11-03-rep` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,268 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 93.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,287 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (66,184 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 14.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (17,117 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 20.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (203,214 resting ≥ 5,000 ✓) ≈ $3.84/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-ma-2026-11-03-dem` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~98.4% of bid side (2,264 resting ≥ 2,000 ✓) ≈ $6.15/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 9.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~96.8% of bid side (65,768 resting ≥ 20,000 ✓) ≈ $6.91/day (event pool ÷ 14 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 10.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~91.9% of bid side (305,763 resting ≥ 5,000 ✓) ≈ $3.54/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~88.1% of bid side (500,261 resting ≥ 2,000 ✓) ≈ $5.51/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 14.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~87.5% of bid side (305,858 resting ≥ 5,000 ✓) ≈ $3.37/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~85.7% of bid side (500,357 resting ≥ 2,000 ✓) ≈ $5.36/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rokha` | SELL | 5.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~83.3% of ask side (50,946 resting ≥ 20,000 ✓) ≈ $3.09/day (event pool ÷ 27 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~78.9% of bid side (4,290 resting ≥ 2,000 ✓) ≈ $4.93/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~78.3% of bid side (2,029 resting ≥ 2,000 ✓) ≈ $4.89/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 27.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~78.1% of bid side (104,299 resting ≥ 20,000 ✓) ≈ $4.60/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~76.6% of bid side (2,035 resting ≥ 2,000 ✓) ≈ $3.19/day (event pool ÷ 3 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (2,055 resting ≥ 2,000 ✓) ≈ $4.17/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tn-2026-11-03-dem` | SELL | 5.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~66.3% of ask side (2,054 resting ≥ 2,000 ✓) ≈ $4.15/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~62.9% of ask side (130,789 resting ≥ 2,000 ✓) ≈ $3.93/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-aleocc` | BUY | 21.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~60.5% of bid side (71,008 resting ≥ 20,000 ✓) ≈ $3.56/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 87.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~60.0% of ask side (27,352 resting ≥ 2,000 ✓) ≈ $3.75/day (event pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 95.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~59.2% of bid side (500,439 resting ≥ 2,000 ✓) ≈ $3.70/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~57.1% of ask side (208,346 resting ≥ 2,000 ✓) ≈ $3.57/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ma-2026-11-03-rep` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~55.5% of ask side (2,062 resting ≥ 2,000 ✓) ≈ $3.47/day (event pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~51.7% of bid side (600,305 resting ≥ 2,000 ✓) ≈ $3.23/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-dem` | SELL | 6.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~50.0% of ask side (134,220 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~50.0% of ask side (130,782 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 95.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~47.6% of bid side (500,377 resting ≥ 2,000 ✓) ≈ $2.98/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | SELL | 23.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~43.9% of ask side (42,276 resting ≥ 20,000 ✓) ≈ $2.58/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 12.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~43.8% of bid side (105,636 resting ≥ 5,000 ✓) ≈ $1.69/day (event pool ÷ 13 markets) |
| …and 1443 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> BUY 3 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 86¢ | 50 | ×0.1^8 = 0.0 |
|  | 74¢ | 3 | ×0.1^20 = 0.0 |
|  | 56¢ | 5 | ×0.1^38 = 0.0 |
|  | 35¢ | 1 | ×0.1^59 = 0.0 |
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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 3 @ 93¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 86¢ | 30 | ×0.1^7 = 0.0 |
|  | 84¢ | 50 | ×0.1^9 = 0.0 |
|  | 10¢ | 4 | ×0.1^83 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 15¢ | 157 | ×0.1^7 = 0.0 |
|  | 18¢ | 50 | ×0.1^10 = 0.0 |
|  | 45¢ | 500 | ×0.1^37 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^90 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 3 @ 14¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 3 (3 yours) | ×0.1^0 = 3.4 |
|  | 10¢ | 1 | ×0.1^4 = 0.0 |
|  | 7¢ | 16 | ×0.1^7 = 0.0 |
|  | 2¢ | 15,000 | ×0.1^12 = 0.0 |
| | | **Σ** | **3.4** |

`yours 3.4 / Σ 3.4 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5 @ 20¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 15¢ | 30 | ×0.2^5 = 0.0 |
|  | 14¢ | 2 | ×0.2^6 = 0.0 |
|  | 12¢ | 326 | ×0.2^8 = 0.0 |
|  | 11¢ | 2,272 | ×0.2^9 = 0.0 |
|  | 10¢ | 70 | ×0.2^10 = 0.0 |
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
<details><summary><code>usgubewc-usgub-ma-2026-11-03-dem</code> BUY 3 @ 94¢ → $6.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 91¢ | 50 | ×0.1^3 = 0.1 |
|  | 43¢ | 5 | ×0.1^51 = 0.0 |
|  | 31¢ | 1 | ×0.1^63 = 0.0 |
|  | 10¢ | 5 | ×0.1^84 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 98.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.4% = $6.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 135 @ 9¢ → $6.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 136 (135 yours) | ×0.2^0 = 136.0 |
|  | 5¢ | 2,001 | ×0.2^4 = 3.2 |
|  | 2¢ | 12,972 | ×0.2^7 = 0.2 |
|  | 1¢ | 50,659 | ×0.2^8 = 0.1 |
| | | **Σ** | **139.5** |

`yours 135.0 / Σ 139.5 = 96.8%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 96.8% = $6.91/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 10¢ → $3.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 0 | ×0.2^1 = 0.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 2 | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 4¢ | 5 | ×0.2^6 = 0.0 |
|  | 3¢ | 2 | ×0.2^7 = 0.0 |
|  | 2¢ | 5,200 | ×0.2^8 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 91.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 91.9% = $3.54/day`  

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
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 3 @ 95¢ → $5.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 94¢ | 4 | ×0.1^1 = 0.4 |
|  | 91¢ | 50 | ×0.1^4 = 0.0 |
|  | 15¢ | 4 | ×0.1^80 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.4** |

`yours 3.0 / Σ 3.4 = 88.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 88.1% = $5.51/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 7 @ 14¢ → $3.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 8 (7 yours) | ×0.2^0 = 8.0 |
|  | 2¢ | 5,476 | ×0.2^12 = 0.0 |
| | | **Σ** | **8.0** |

`yours 7.0 / Σ 8.0 = 87.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 87.5% = $3.37/day`  

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
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> BUY 3 @ 95¢ → $5.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 15¢ | 104 | ×0.1^80 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.5** |

`yours 3.0 / Σ 3.5 = 85.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 85.7% = $5.36/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rokha</code> SELL 1 @ 5¢ → $3.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 6¢ | 1 | ×0.2^1 = 0.2 |
|  | 14¢ | 64 | ×0.2^9 = 0.0 |
|  | 20¢ | 314 | ×0.2^15 = 0.0 |
|  | 21¢ | 50 | ×0.2^16 = 0.0 |
|  | 25¢ | 30,266 | ×0.2^20 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 83.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 83.3% = $3.09/day`  

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
20. `ewc-usp-2028-11-07-rokha` ← this one
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 2 @ 7¢ → $4.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 6¢ | 5 | ×0.1^1 = 0.5 |
|  | 3¢ | 285 | ×0.1^4 = 0.0 |
|  | 2¢ | 200 | ×0.1^5 = 0.0 |
|  | 1¢ | 3,798 | ×0.1^6 = 0.0 |
| | | **Σ** | **2.5** |

`yours 2.0 / Σ 2.5 = 78.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 78.9% = $4.93/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 1 @ 27¢ → $4.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 26¢ | 1 | ×0.2^1 = 0.2 |
|  | 25¢ | 2 | ×0.2^2 = 0.1 |
|  | 17¢ | 62 | ×0.2^10 = 0.0 |
|  | 15¢ | 697 | ×0.2^12 = 0.0 |
|  | 13¢ | 1,923 | ×0.2^14 = 0.0 |
|  | 10¢ | 51,250 | ×0.2^17 = 0.0 |
| | | **Σ** | **1.3** |

`yours 1.0 / Σ 1.3 = 78.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 78.1% = $4.60/day`  

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 3 @ 95¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 4 (3 yours) | ×0.1^0 = 4.0 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 39¢ | 1 | ×0.1^56 = 0.0 |
|  | 9¢ | 1 | ×0.1^86 = 0.0 |
|  | 1¢ | 1,999 | ×0.1^94 = 0.0 |
| | | **Σ** | **4.5** |

`yours 3.0 / Σ 4.5 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-dem</code> SELL 2 @ 5¢ → $4.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 3 (2 yours) | ×0.1^0 = 3.0 |
|  | 7¢ | 1 | ×0.1^2 = 0.0 |
|  | 9¢ | 50 | ×0.1^4 = 0.0 |
|  | 58¢ | 1 | ×0.1^53 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^94 = 0.0 |
| | | **Σ** | **3.0** |

`yours 2.0 / Σ 3.0 = 66.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.3% = $4.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> SELL 1 @ 6¢ → $3.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 8¢ | 59 | ×0.1^2 = 0.6 |
|  | 21¢ | 1 | ×0.1^15 = 0.0 |
|  | 26¢ | 1 | ×0.1^20 = 0.0 |
|  | 57¢ | 1 | ×0.1^51 = 0.0 |
|  | 68¢ | 1 | ×0.1^62 = 0.0 |
|  | 96¢ | 0 | ×0.1^90 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.6** |

`yours 1.0 / Σ 1.6 = 62.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 62.9% = $3.93/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-aleocc</code> BUY 20 @ 21¢ → $3.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 22 (20 yours) | ×0.2^0 = 22.0 |
|  | 18¢ | 612 | ×0.2^3 = 4.9 |
|  | 17¢ | 3,822 | ×0.2^4 = 6.1 |
|  | 13¢ | 16,250 | ×0.2^8 = 0.0 |
| | | **Σ** | **33.1** |

`yours 20.0 / Σ 33.1 = 60.5%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 60.5% = $3.56/day`  

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 3 @ 87¢ → $3.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 5 (3 yours) | ×0.1^0 = 5.0 |
|  | 92¢ | 9 | ×0.1^5 = 0.0 |
|  | 97¢ | 5,348 | ×0.1^10 = 0.0 |
| | | **Σ** | **5.0** |

`yours 3.0 / Σ 5.0 = 60.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.0% = $3.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 35 @ 95¢ → $3.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 54 (35 yours) | ×0.1^0 = 54.0 |
|  | 94¢ | 46 | ×0.1^1 = 4.6 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 58¢ | 1 | ×0.1^37 = 0.0 |
|  | 12¢ | 88 | ×0.1^83 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **59.1** |

`yours 35.0 / Σ 59.1 = 59.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 59.2% = $3.70/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 2 @ 7¢ → $3.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 3 (2 yours) | ×0.1^0 = 3.0 |
|  | 9¢ | 50 | ×0.1^2 = 0.5 |
|  | 93¢ | 5 | ×0.1^86 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^91 = 0.0 |
| | | **Σ** | **3.5** |

`yours 2.0 / Σ 3.5 = 57.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.1% = $3.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ma-2026-11-03-rep</code> SELL 1 @ 7¢ → $3.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 8¢ | 3 | ×0.1^1 = 0.3 |
|  | 9¢ | 50 | ×0.1^2 = 0.5 |
|  | 11¢ | 8 | ×0.1^4 = 0.0 |
|  | 29¢ | 1 | ×0.1^22 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.8** |

`yours 1.0 / Σ 1.8 = 55.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 55.5% = $3.47/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem`
2. `usgubewc-usgub-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> BUY 3 @ 95¢ → $3.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 94¢ | 23 | ×0.1^1 = 2.3 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 46¢ | 4 | ×0.1^49 = 0.0 |
|  | 40¢ | 25 | ×0.1^55 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **5.8** |

`yours 3.0 / Σ 5.8 = 51.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 51.7% = $3.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-dem</code> SELL 2 @ 6¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 4 (2 yours) | ×0.1^0 = 4.0 |
|  | 15¢ | 0 | ×0.1^9 = 0.0 |
|  | 16¢ | 50 | ×0.1^10 = 0.0 |
|  | 21¢ | 603 | ×0.1^15 = 0.0 |
|  | 22¢ | 500 | ×0.1^16 = 0.0 |
|  | 25¢ | 20 | ×0.1^19 = 0.0 |
|  | 98¢ | 132,818 | ×0.1^92 = 0.0 |
| | | **Σ** | **4.0** |

`yours 2.0 / Σ 4.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem` ← this one
2. `usgubewc-usgub-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 2 @ 8¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 4 (2 yours) | ×0.1^0 = 4.0 |
|  | 14¢ | 50 | ×0.1^6 = 0.0 |
|  | 51¢ | 3 | ×0.1^43 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^90 = 0.0 |
| | | **Σ** | **4.0** |

`yours 2.0 / Σ 4.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 4 @ 95¢ → $2.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 4 (4 yours) | ×0.1^0 = 4.0 |
|  | 94¢ | 44 | ×0.1^1 = 4.4 |
|  | 92¢ | 1 | ×0.1^3 = 0.0 |
|  | 90¢ | 50 | ×0.1^5 = 0.0 |
|  | 41¢ | 78 | ×0.1^54 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **8.4** |

`yours 4.0 / Σ 8.4 = 47.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 47.6% = $2.98/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> SELL 3 @ 23¢ → $2.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 23¢ | 6 (3 yours) | ×0.2^0 = 6.3 |
|  | 27¢ | 1 | ×0.2^4 = 0.0 |
|  | 29¢ | 4 | ×0.2^6 = 0.0 |
|  | 30¢ | 39,465 | ×0.2^7 = 0.5 |
| | | **Σ** | **6.8** |

`yours 3.0 / Σ 6.8 = 43.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 43.9% = $2.58/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 1 @ 12¢ → $1.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 10¢ | 7 | ×0.2^2 = 0.3 |
|  | 4¢ | 2 | ×0.2^8 = 0.0 |
|  | 3¢ | 5 | ×0.2^9 = 0.0 |
|  | 2¢ | 5,200 | ×0.2^10 = 0.0 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 43.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.8% = $1.69/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47` ← this one
3. `scc-senate-gop-2026-11-03-48`
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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,427 resting) | ~82.0% | ~$20.51 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,778 resting) | ~76.1% | ~$19.04 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (79,909 resting) | ~14.1% | ~$10.58 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (74,731 resting) | ~45.3% | ~$2.83 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,489 resting) | ~3.6% | ~$2.69 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (632,347 resting) | ~9.4% | ~$2.34 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (278,312 resting) | ~2.5% | ~$1.89 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (66,778 resting) | ~6.4% | ~$1.61 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,246,813 resting) | ~22.3% | ~$1.40 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,329 resting) | ~1.8% | ~$1.37 |
| `ewc-usse-ak-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (377,291 resting) | ~21.5% | ~$1.34 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,351 resting) | ~1.7% | ~$1.24 |

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
| 2026-08-18 6:33 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:30 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:22 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:19 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:15 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:11 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:08 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:04 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:00 PM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
