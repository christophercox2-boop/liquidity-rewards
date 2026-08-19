# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-19 9:44 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$315.88/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — SELL at the best price, ~$24.61/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$14.54/day), `ewc-usse-tx-2026-11-03-rep` (~$11.27/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$315.88/day (~$13.16/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-tn-2026-11-03-rep` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~98.4% of bid side (2,060 resting ≥ 2,000 ✓) ≈ $6.15/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 37.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~95.2% of bid side (400,602 resting ≥ 5,000 ✓) ≈ $3.97/day (event pool ÷ 12 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | SELL | 17.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.9% of ask side (141,963 resting ≥ 2,000 ✓) ≈ $5.68/day (event pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~90.4% of ask side (66,198 resting ≥ 2,000 ✓) ≈ $5.65/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~89.0% of bid side (50,362 resting ≥ 20,000 ✓) ≈ $3.30/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 10.0¢ | 135 | 1 | $200.00 | ✅ scoring — ~85.9% of bid side (126,956 resting ≥ 20,000 ✓) ≈ $5.05/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 0 | $25.00 | ✅ scoring — ~85.7% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $5.35/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~85.2% of bid side (500,327 resting ≥ 2,000 ✓) ≈ $5.33/day (event pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | SELL | 11.0¢ | 75 | 1 | $25.00 | ✅ scoring — ~78.9% of ask side (2,500 resting ≥ 2,000 ✓) ≈ $1.41/day (event pool ÷ 7 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 10.0¢ | 82 | 1 | $200.00 | ✅ scoring — ~77.7% of bid side (61,222 resting ≥ 20,000 ✓) ≈ $5.55/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 80 | 0 | $200.00 | ✅ scoring — ~74.4% of bid side (91,923 resting ≥ 20,000 ✓) ≈ $4.37/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ma-2026-11-03-rep` | BUY | 1.0¢ | 1,666 | 0 | $25.00 | ✅ scoring — ~73.5% of bid side (2,266 resting ≥ 2,000 ✓) ≈ $4.59/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-tulgab` | BUY | 1.0¢ | 19,238 | 2 | $200.00 | ✅ scoring — ~71.3% of bid side (21,900 resting ≥ 20,000 ✓) ≈ $5.09/day (event pool ÷ 14 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 8.0¢ | 13 | 0 | $100.00 | ✅ scoring — ~68.5% of ask side (77,742 resting ≥ 5,000 ✓) ≈ $2.63/day (event pool ÷ 13 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~63.9% of bid side (2,135 resting ≥ 2,000 ✓) ≈ $3.99/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 87.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~63.5% of ask side (2,559 resting ≥ 2,000 ✓) ≈ $3.97/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | BUY | 21.0¢ | 23 | 0 | $200.00 | ✅ scoring — ~56.6% of bid side (221,851 resting ≥ 20,000 ✓) ≈ $3.33/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 10.0¢ | 55 | 0 | $200.00 | ✅ scoring — ~55.7% of bid side (41,004 resting ≥ 20,000 ✓) ≈ $3.28/day (event pool ÷ 17 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~55.5% of ask side (196,049 resting ≥ 2,000 ✓) ≈ $3.47/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-rep` | BUY | 91.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (500,306 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-kamhar` | SELL | 5.0¢ | 286 | 0 | $200.00 | ✅ scoring — ~49.4% of ask side (67,332 resting ≥ 20,000 ✓) ≈ $1.83/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 26.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~46.2% of bid side (96,846 resting ≥ 20,000 ✓) ≈ $2.72/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 26.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~46.2% of bid side (96,846 resting ≥ 20,000 ✓) ≈ $2.72/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | SELL | 94.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~44.5% of ask side (2,713 resting ≥ 2,000 ✓) ≈ $2.78/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | SELL | 6.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~44.4% of ask side (130,801 resting ≥ 2,000 ✓) ≈ $2.78/day (event pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~41.7% of bid side (23,205 resting ≥ 5,000 ✓) ≈ $10.42/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 9.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~39.9% of bid side (20,493 resting ≥ 20,000 ✓) ≈ $1.48/day (event pool ÷ 27 markets) |
| `ussewc-usse-al-2026-11-03-dem` | SELL | 5.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~39.7% of ask side (203,608 resting ≥ 2,000 ✓) ≈ $2.48/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 19,263 | 3 | $200.00 | ✅ scoring — ~38.9% of bid side (22,035 resting ≥ 20,000 ✓) ≈ $2.78/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 19,336 | 3 | $200.00 | ✅ scoring — ~38.8% of bid side (22,035 resting ≥ 20,000 ✓) ≈ $2.77/day (event pool ÷ 14 markets) |
| …and 2762 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-tn-2026-11-03-rep</code> BUY 3 @ 94¢ → $6.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 91¢ | 50 | ×0.1^3 = 0.1 |
|  | 83¢ | 3 | ×0.1^11 = 0.0 |
|  | 64¢ | 4 | ×0.1^30 = 0.0 |
|  | 32¢ | 1 | ×0.1^62 = 0.0 |
|  | 10¢ | 5 | ×0.1^84 = 0.0 |
|  | 1¢ | 1,994 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.1** |

`yours 3.0 / Σ 3.1 = 98.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.4% = $6.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem`
2. `usgubewc-usgub-tn-2026-11-03-rep` ← this one

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> SELL 1 @ 17¢ → $5.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 18¢ | 1 | ×0.1^1 = 0.1 |
|  | 23¢ | 45 | ×0.1^6 = 0.0 |
|  | 24¢ | 30 | ×0.1^7 = 0.0 |
|  | 26¢ | 50 | ×0.1^9 = 0.0 |
|  | 85¢ | 6,000 | ×0.1^68 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.9% = $5.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $5.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 9¢ | 2 | ×0.1^1 = 0.2 |
|  | 10¢ | 1 | ×0.1^2 = 0.0 |
|  | 11¢ | 2 | ×0.1^3 = 0.0 |
|  | 12¢ | 1 | ×0.1^4 = 0.0 |
|  | 13¢ | 3 | ×0.1^5 = 0.0 |
|  | 14¢ | 2 | ×0.1^6 = 0.0 |
|  | 15¢ | 160 | ×0.1^7 = 0.0 |
|  | 18¢ | 50 | ×0.1^10 = 0.0 |
|  | 45¢ | 500 | ×0.1^37 = 0.0 |
| | … | +1 levels | 0.0 |
| | | **Σ** | **2.2** |

`yours 2.0 / Σ 2.2 = 90.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.4% = $5.65/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 151 (135 yours) | ×0.2^0 = 151.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **151.7** |

`yours 135.0 / Σ 151.7 = 89.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 89.0% = $3.30/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 135 @ 10¢ → $5.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 4 | ×0.2^0 = 3.9 |
| ▶ | 10¢ | 135 (135 yours) | ×0.2^1 = 27.0 |
|  | 7¢ | 1 | ×0.2^4 = 0.0 |
|  | 6¢ | 255 | ×0.2^5 = 0.1 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 4¢ | 40,110 | ×0.2^7 = 0.5 |
| | | **Σ** | **31.4** |

`yours 27.0 / Σ 31.4 = 85.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 85.9% = $5.05/day`  

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
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $5.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (1,799 yours) | ×0.1^0 = 2,100.0 |
| | | **Σ** | **2,100.0** |

`yours 1,799.0 / Σ 2,100.0 = 85.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 85.7% = $5.35/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> BUY 3 @ 95¢ → $5.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 15¢ | 74 | ×0.1^80 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.5** |

`yours 3.0 / Σ 3.5 = 85.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 85.2% = $5.33/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> SELL 75 @ 11¢ → $1.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 11¢ | 75 (75 yours) | ×0.1^1 = 7.5 |
|  | 99¢ | 2,423 | ×0.1^89 = 0.0 |
| | | **Σ** | **9.5** |

`yours 7.5 / Σ 9.5 = 78.9%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 78.9% = $1.41/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 82 @ 10¢ → $5.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 4 | ×0.2^0 = 4.1 |
| ▶ | 10¢ | 85 (82 yours) | ×0.2^1 = 17.0 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 3¢ | 1 | ×0.2^8 = 0.0 |
|  | 2¢ | 10,472 | ×0.2^9 = 0.0 |
|  | 1¢ | 50,659 | ×0.2^10 = 0.0 |
| | | **Σ** | **21.1** |

`yours 16.4 / Σ 21.1 = 77.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 77.7% = $5.55/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 80 @ 12¢ → $4.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 107 (80 yours) | ×0.2^0 = 107.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 8¢ | 6 | ×0.2^4 = 0.0 |
|  | 7¢ | 60 | ×0.2^5 = 0.0 |
|  | 6¢ | 125 | ×0.2^6 = 0.0 |
|  | 5¢ | 5,000 | ×0.2^7 = 0.1 |
|  | 3¢ | 171 | ×0.2^9 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **107.6** |

`yours 80.0 / Σ 107.6 = 74.4%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 74.4% = $4.37/day`  

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
<details><summary><code>usgubewc-usgub-ma-2026-11-03-rep</code> BUY 1,666 @ 1¢ → $4.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,266 (1,666 yours) | ×0.1^0 = 2,265.7 |
| | | **Σ** | **2,265.7** |

`yours 1,665.7 / Σ 2,265.7 = 73.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 73.5% = $4.59/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem`
2. `usgubewc-usgub-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-tulgab</code> BUY 19,238 @ 1¢ → $5.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 212 | ×0.2^0 = 212.0 |
| ▶ | 1¢ | 21,688 (19,238 yours) | ×0.2^2 = 867.5 |
| | | **Σ** | **1,079.5** |

`yours 769.5 / Σ 1,079.5 = 71.3%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 71.3% = $5.09/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab` ← this one
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 13 @ 8¢ → $2.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 19 (13 yours) | ×0.2^0 = 19.0 |
|  | 15¢ | 562 | ×0.2^7 = 0.0 |
|  | 22¢ | 100 | ×0.2^14 = 0.0 |
|  | 24¢ | 50 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^89 = 0.0 |
| | | **Σ** | **19.0** |

`yours 13.0 / Σ 19.0 = 68.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.5% = $2.63/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 10 @ 12¢ → $3.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 15 (10 yours) | ×0.1^0 = 15.0 |
|  | 11¢ | 5 | ×0.1^1 = 0.5 |
|  | 10¢ | 16 | ×0.1^2 = 0.2 |
|  | 1¢ | 2,099 | ×0.1^11 = 0.0 |
| | | **Σ** | **15.7** |

`yours 10.0 / Σ 15.7 = 63.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.9% = $3.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 1 @ 87¢ → $3.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 89¢ | 2 | ×0.1^2 = 0.0 |
|  | 90¢ | 555 | ×0.1^3 = 0.6 |
|  | 92¢ | 2 | ×0.1^5 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^12 = 0.0 |
| | | **Σ** | **1.6** |

`yours 1.0 / Σ 1.6 = 63.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.5% = $3.97/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> BUY 23 @ 21¢ → $3.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 33 (23 yours) | ×0.2^0 = 33.1 |
|  | 20¢ | 1 | ×0.2^1 = 0.2 |
|  | 19¢ | 8 | ×0.2^2 = 0.3 |
|  | 18¢ | 36 | ×0.2^3 = 0.3 |
|  | 17¢ | 112 | ×0.2^4 = 0.2 |
|  | 16¢ | 21,110 | ×0.2^5 = 6.8 |
| | | **Σ** | **40.9** |

`yours 23.1 / Σ 40.9 = 56.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 56.6% = $3.33/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 55 @ 10¢ → $3.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 96 (55 yours) | ×0.2^0 = 95.9 |
|  | 9¢ | 1 | ×0.2^1 = 0.2 |
|  | 8¢ | 64 | ×0.2^2 = 2.5 |
|  | 4¢ | 273 | ×0.2^6 = 0.0 |
|  | 3¢ | 110 | ×0.2^7 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^8 = 0.1 |
| | | **Σ** | **98.7** |

`yours 55.0 / Σ 98.7 = 55.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 55.7% = $3.28/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 10 @ 13¢ → $3.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 18 (10 yours) | ×0.1^0 = 18.0 |
|  | 15¢ | 1 | ×0.1^2 = 0.0 |
|  | 25¢ | 50 | ×0.1^12 = 0.0 |
|  | 35¢ | 4 | ×0.1^22 = 0.0 |
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
<details><summary><code>ussewc-usse-la-2026-11-03-rep</code> BUY 4 @ 91¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 8 (4 yours) | ×0.1^0 = 8.0 |
|  | 83¢ | 80 | ×0.1^8 = 0.0 |
|  | 68¢ | 5 | ×0.1^23 = 0.0 |
|  | 31¢ | 1 | ×0.1^60 = 0.0 |
|  | 15¢ | 12 | ×0.1^76 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^89 = 0.0 |
| | | **Σ** | **8.0** |

`yours 4.0 / Σ 8.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem`
2. `ussewc-usse-la-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-kamhar</code> SELL 286 @ 5¢ → $1.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 579 (286 yours) | ×0.2^0 = 579.0 |
|  | 14¢ | 61 | ×0.2^9 = 0.0 |
|  | 19¢ | 31,724 | ×0.2^14 = 0.0 |
| | | **Σ** | **579.0** |

`yours 286.0 / Σ 579.0 = 49.4%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 49.4% = $1.83/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 1 @ 26¢ → $2.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 2 (1 yours) | ×0.2^0 = 2.1 |
|  | 22¢ | 1 | ×0.2^4 = 0.0 |
|  | 21¢ | 30 | ×0.2^5 = 0.0 |
|  | 20¢ | 181 | ×0.2^6 = 0.0 |
|  | 19¢ | 1 | ×0.2^7 = 0.0 |
|  | 17¢ | 62 | ×0.2^9 = 0.0 |
|  | 15¢ | 747 | ×0.2^11 = 0.0 |
|  | 14¢ | 178 | ×0.2^12 = 0.0 |
|  | 10¢ | 45,443 | ×0.2^16 = 0.0 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 46.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 46.2% = $2.72/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 1 @ 26¢ → $2.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 2 (1 yours) | ×0.2^0 = 2.1 |
|  | 22¢ | 1 | ×0.2^4 = 0.0 |
|  | 21¢ | 30 | ×0.2^5 = 0.0 |
|  | 20¢ | 181 | ×0.2^6 = 0.0 |
|  | 19¢ | 1 | ×0.2^7 = 0.0 |
|  | 17¢ | 62 | ×0.2^9 = 0.0 |
|  | 15¢ | 747 | ×0.2^11 = 0.0 |
|  | 14¢ | 178 | ×0.2^12 = 0.0 |
|  | 10¢ | 45,443 | ×0.2^16 = 0.0 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 46.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 46.2% = $2.72/day`  

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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> SELL 1 @ 94¢ → $2.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 95¢ | 2 | ×0.1^1 = 0.2 |
|  | 96¢ | 2 | ×0.1^2 = 0.0 |
|  | 99¢ | 2,707 | ×0.1^5 = 0.0 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 44.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.5% = $2.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> SELL 2 @ 6¢ → $2.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 3 (2 yours) | ×0.1^0 = 3.0 |
|  | 7¢ | 9 | ×0.1^1 = 0.9 |
|  | 8¢ | 60 | ×0.1^2 = 0.6 |
|  | 21¢ | 1 | ×0.1^15 = 0.0 |
|  | 26¢ | 1 | ×0.1^20 = 0.0 |
|  | 57¢ | 1 | ×0.1^51 = 0.0 |
|  | 68¢ | 1 | ×0.1^62 = 0.0 |
|  | 96¢ | 0 | ×0.1^90 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^92 = 0.0 |
| | | **Σ** | **4.5** |

`yours 2.0 / Σ 4.5 = 44.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.4% = $2.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $10.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,399 (1,000 yours) | ×0.2^0 = 2,399.0 |
|  | 5¢ | 501 | ×0.2^4 = 0.8 |
|  | 3¢ | 80 | ×0.2^6 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^7 = 0.3 |
| | | **Σ** | **2,400.1** |

`yours 1,000.0 / Σ 2,400.1 = 41.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 41.7% = $10.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 50 @ 9¢ → $1.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 125 (50 yours) | ×0.2^0 = 125.3 |
|  | 1¢ | 20,368 | ×0.2^8 = 0.1 |
| | | **Σ** | **125.4** |

`yours 50.0 / Σ 125.4 = 39.9%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 39.9% = $1.48/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr` ← this one
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
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-dem</code> SELL 2 @ 5¢ → $2.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 5 (2 yours) | ×0.1^0 = 5.0 |
|  | 8¢ | 50 | ×0.1^3 = 0.1 |
|  | 9¢ | 1 | ×0.1^4 = 0.0 |
|  | 18¢ | 0 | ×0.1^13 = 0.0 |
|  | 32¢ | 1 | ×0.1^27 = 0.0 |
|  | 51¢ | 1 | ×0.1^46 = 0.0 |
|  | 98¢ | 203,325 | ×0.1^93 = 0.0 |
| | | **Σ** | **5.0** |

`yours 2.0 / Σ 5.0 = 39.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 39.7% = $2.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem` ← this one
2. `ussewc-usse-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 19,263 @ 1¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 222 | ×0.2^0 = 221.6 |
| ▶ | 1¢ | 21,813 (19,263 yours) | ×0.2^3 = 174.5 |
| | | **Σ** | **396.1** |

`yours 154.1 / Σ 396.1 = 38.9%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 38.9% = $2.78/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre` ← this one
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 19,336 @ 1¢ → $2.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 224 | ×0.2^0 = 223.8 |
| ▶ | 1¢ | 21,811 (19,336 yours) | ×0.2^3 = 174.5 |
| | | **Σ** | **398.2** |

`yours 154.7 / Σ 398.2 = 38.8%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 38.8% = $2.77/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus` ← this one
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (41,599 resting) | ~98.4% | ~$24.61 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,039 resting) | ~58.1% | ~$14.54 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (920,145 resting) | ~15.0% | ~$11.27 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (66,476 resting) | ~8.7% | ~$6.54 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (537,088 resting) | ~7.6% | ~$5.70 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (26,373 resting) | ~5.6% | ~$4.18 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,006 resting) | ~4.7% | ~$3.51 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (103,591 resting) | ~53.1% | ~$3.32 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (391,695 resting) | ~41.7% | ~$2.61 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (825,780 resting) | ~2.8% | ~$2.10 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (794,910 resting) | ~2.4% | ~$1.82 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (632,890 resting) | ~6.7% | ~$1.69 |

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
| 2026-08-19 9:44 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 8:44 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 7:22 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 6:21 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 5:21 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 4:20 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 3:20 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 1:36 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 10:41 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:41 PM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
