# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-19 3:20 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$310.29/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `paccc-usho-midterms-2026-11-03-rep` — BUY at the best price, ~$44.05/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$15.65/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$14.60/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$310.29/day (~$12.93/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 87.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,296 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-rep` | BUY | 93.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,268 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 57.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,688 resting ≥ 5,000 ✓) ≈ $4.17/day (event pool ÷ 12 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~98.8% of bid side (50,347 resting ≥ 20,000 ✓) ≈ $3.66/day (event pool ÷ 27 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~94.2% of ask side (66,196 resting ≥ 2,000 ✓) ≈ $5.89/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 10.0¢ | 82 | 1 | $200.00 | ✅ scoring — ~91.1% of bid side (73,645 resting ≥ 20,000 ✓) ≈ $6.50/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | BUY | 23.0¢ | 37 | 0 | $200.00 | ✅ scoring — ~91.0% of bid side (223,518 resting ≥ 20,000 ✓) ≈ $5.35/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~85.7% of bid side (500,257 resting ≥ 2,000 ✓) ≈ $5.36/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 0 | $25.00 | ✅ scoring — ~85.7% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $3.57/day (event pool ÷ 3 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 0 | $25.00 | ✅ scoring — ~85.7% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $5.35/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 85.0¢ | 4 | 2 | $25.00 | ✅ scoring — ~79.9% of bid side (502,172 resting ≥ 2,000 ✓) ≈ $5.00/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~78.3% of bid side (4,292 resting ≥ 2,000 ✓) ≈ $4.89/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 9.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~75.6% of bid side (35,614 resting ≥ 5,000 ✓) ≈ $2.91/day (event pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 80 | 0 | $200.00 | ✅ scoring — ~74.3% of bid side (96,923 resting ≥ 20,000 ✓) ≈ $4.37/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 8.0¢ | 13 | 0 | $100.00 | ✅ scoring — ~68.5% of ask side (77,742 resting ≥ 5,000 ✓) ≈ $2.63/day (event pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~67.5% of ask side (92,817 resting ≥ 5,000 ✓) ≈ $2.60/day (event pool ÷ 13 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~60.0% of bid side (2,036 resting ≥ 2,000 ✓) ≈ $3.75/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jonoss` | SELL | 20.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~57.8% of ask side (36,745 resting ≥ 20,000 ✓) ≈ $2.14/day (event pool ÷ 27 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~55.5% of ask side (196,049 resting ≥ 2,000 ✓) ≈ $3.47/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 11.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~55.0% of ask side (38,902 resting ≥ 20,000 ✓) ≈ $3.24/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 5.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~48.3% of ask side (208,357 resting ≥ 2,000 ✓) ≈ $3.02/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 21.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~48.2% of bid side (205,639 resting ≥ 5,000 ✓) ≈ $1.86/day (event pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 20.0¢ | 5 | 1 | $100.00 | ✅ scoring — ~48.2% of bid side (205,639 resting ≥ 5,000 ✓) ≈ $1.86/day (event pool ÷ 13 markets) |
| `ussewc-usse-la-2026-11-03-rep` | BUY | 91.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~44.4% of bid side (500,279 resting ≥ 2,000 ✓) ≈ $2.78/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 9.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~44.3% of bid side (20,481 resting ≥ 20,000 ✓) ≈ $1.64/day (event pool ÷ 27 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 5.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~44.1% of ask side (130,791 resting ≥ 2,000 ✓) ≈ $2.76/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | SELL | 94.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~43.9% of ask side (2,715 resting ≥ 2,000 ✓) ≈ $2.74/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 17.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~43.5% of bid side (56,953 resting ≥ 5,000 ✓) ≈ $1.67/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 6.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~42.0% of ask side (65,534 resting ≥ 2,000 ✓) ≈ $2.62/day (event pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~39.9% of bid side (31,223 resting ≥ 5,000 ✓) ≈ $9.97/day (event pool ÷ 2 markets) |
| …and 2650 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 3 @ 87¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 69¢ | 85 | ×0.1^18 = 0.0 |
|  | 15¢ | 4 | ×0.1^72 = 0.0 |
|  | 10¢ | 4 | ×0.1^77 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> BUY 3 @ 93¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 75¢ | 50 | ×0.1^18 = 0.0 |
|  | 74¢ | 3 | ×0.1^19 = 0.0 |
|  | 63¢ | 4 | ×0.1^30 = 0.0 |
|  | 56¢ | 1 | ×0.1^37 = 0.0 |
|  | 35¢ | 1 | ×0.1^58 = 0.0 |
|  | 13¢ | 1 | ×0.1^80 = 0.0 |
|  | 10¢ | 5 | ×0.1^83 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem`
2. `usgubewc-usgub-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 1 @ 57¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 55¢ | 0 | ×0.2^2 = 0.0 |
|  | 42¢ | 50 | ×0.2^15 = 0.0 |
|  | 2¢ | 300,437 | ×0.2^55 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200` ← this one
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 136 (135 yours) | ×0.2^0 = 136.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **136.7** |

`yours 135.0 / Σ 136.7 = 98.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 98.8% = $3.66/day`  

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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $5.89/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 9¢ | 1 | ×0.1^1 = 0.1 |
|  | 10¢ | 2 | ×0.1^2 = 0.0 |
|  | 11¢ | 3 | ×0.1^3 = 0.0 |
|  | 13¢ | 2 | ×0.1^5 = 0.0 |
|  | 14¢ | 1 | ×0.1^6 = 0.0 |
|  | 15¢ | 160 | ×0.1^7 = 0.0 |
|  | 18¢ | 50 | ×0.1^10 = 0.0 |
|  | 45¢ | 500 | ×0.1^37 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^90 = 0.0 |
| | | **Σ** | **2.1** |

`yours 2.0 / Σ 2.1 = 94.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.2% = $5.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 82 @ 10¢ → $6.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 10¢ | 85 (82 yours) | ×0.2^1 = 17.0 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 3¢ | 1 | ×0.2^8 = 0.0 |
|  | 2¢ | 22,972 | ×0.2^9 = 0.0 |
| | | **Σ** | **18.0** |

`yours 16.4 / Σ 18.0 = 91.1%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 91.1% = $6.50/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> BUY 37 @ 23¢ → $5.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 23¢ | 39 (37 yours) | ×0.2^0 = 39.0 |
|  | 22¢ | 2 | ×0.2^1 = 0.4 |
|  | 21¢ | 24 | ×0.2^2 = 1.0 |
|  | 20¢ | 1 | ×0.2^3 = 0.0 |
|  | 19¢ | 8 | ×0.2^4 = 0.0 |
|  | 18¢ | 6 | ×0.2^5 = 0.0 |
|  | 17¢ | 112 | ×0.2^6 = 0.0 |
|  | 16¢ | 21,110 | ×0.2^7 = 0.3 |
| | | **Σ** | **40.7** |

`yours 37.0 / Σ 40.7 = 91.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 91.0% = $5.35/day`  

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
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> BUY 3 @ 95¢ → $5.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 15¢ | 4 | ×0.1^80 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.5** |

`yours 3.0 / Σ 3.5 = 85.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 85.7% = $5.36/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $3.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (1,799 yours) | ×0.1^0 = 2,100.0 |
| | | **Σ** | **2,100.0** |

`yours 1,799.0 / Σ 2,100.0 = 85.7%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 85.7% = $3.57/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 4 @ 85¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 87¢ | 0 | ×0.1^0 = 0.0 |
| ▶ | 85¢ | 4 (4 yours) | ×0.1^2 = 0.0 |
|  | 82¢ | 5 | ×0.1^5 = 0.0 |
|  | 74¢ | 152 | ×0.1^13 = 0.0 |
|  | 65¢ | 6 | ×0.1^22 = 0.0 |
|  | 60¢ | 1 | ×0.1^27 = 0.0 |
|  | 10¢ | 5 | ×0.1^77 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 79.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 79.9% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 2 @ 7¢ → $4.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 6¢ | 5 | ×0.1^1 = 0.5 |
|  | 5¢ | 2 | ×0.1^2 = 0.0 |
|  | 3¢ | 285 | ×0.1^4 = 0.0 |
|  | 2¢ | 200 | ×0.1^5 = 0.0 |
|  | 1¢ | 3,798 | ×0.1^6 = 0.0 |
| | | **Σ** | **2.6** |

`yours 2.0 / Σ 2.6 = 78.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 78.3% = $4.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1 @ 9¢ → $2.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 2¢ | 25,167 | ×0.2^7 = 0.3 |
| | | **Σ** | **1.3** |

`yours 1.0 / Σ 1.3 = 75.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 75.6% = $2.91/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 80 @ 12¢ → $4.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 107 (80 yours) | ×0.2^0 = 107.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 8¢ | 6 | ×0.2^4 = 0.0 |
|  | 7¢ | 60 | ×0.2^5 = 0.0 |
|  | 6¢ | 125 | ×0.2^6 = 0.0 |
|  | 5¢ | 10,000 | ×0.2^7 = 0.1 |
|  | 3¢ | 171 | ×0.2^9 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **107.7** |

`yours 80.0 / Σ 107.7 = 74.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 74.3% = $4.37/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 15 @ 18¢ → $2.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 22 (15 yours) | ×0.2^0 = 21.6 |
|  | 19¢ | 0 | ×0.2^1 = 0.0 |
|  | 22¢ | 21 | ×0.2^4 = 0.0 |
|  | 23¢ | 5 | ×0.2^5 = 0.0 |
|  | 24¢ | 5 | ×0.2^6 = 0.0 |
|  | 25¢ | 10 | ×0.2^7 = 0.0 |
|  | 26¢ | 5 | ×0.2^8 = 0.0 |
|  | 27¢ | 5 | ×0.2^9 = 0.0 |
|  | 29¢ | 50 | ×0.2^11 = 0.0 |
|  | 35¢ | 1 | ×0.2^17 = 0.0 |
| | … | +5 levels | 0.0 |
| | | **Σ** | **21.7** |

`yours 14.6 / Σ 21.7 = 67.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.5% = $2.60/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 10 @ 12¢ → $3.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 16 (10 yours) | ×0.1^0 = 16.0 |
|  | 11¢ | 5 | ×0.1^1 = 0.5 |
|  | 10¢ | 16 | ×0.1^2 = 0.2 |
|  | 1¢ | 1,999 | ×0.1^11 = 0.0 |
| | | **Σ** | **16.7** |

`yours 10.0 / Σ 16.7 = 60.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.0% = $3.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jonoss</code> SELL 1 @ 20¢ → $2.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 22¢ | 18 | ×0.2^2 = 0.7 |
|  | 23¢ | 1 | ×0.2^3 = 0.0 |
|  | 26¢ | 10 | ×0.2^6 = 0.0 |
|  | 29¢ | 30 | ×0.2^9 = 0.0 |
|  | 30¢ | 16,435 | ×0.2^10 = 0.0 |
|  | 35¢ | 25 | ×0.2^15 = 0.0 |
|  | 99¢ | 20,225 | ×0.2^79 = 0.0 |
| | | **Σ** | **1.7** |

`yours 1.0 / Σ 1.7 = 57.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 57.8% = $2.14/day`  

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
12. `ewc-usp-2028-11-07-jonoss` ← this one
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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> SELL 1 @ 11¢ → $3.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 12¢ | 4 | ×0.2^1 = 0.8 |
|  | 16¢ | 41 | ×0.2^5 = 0.0 |
|  | 17¢ | 62 | ×0.2^6 = 0.0 |
|  | 19¢ | 4 | ×0.2^8 = 0.0 |
|  | 26¢ | 21,040 | ×0.2^15 = 0.0 |
| | | **Σ** | **1.8** |

`yours 1.0 / Σ 1.8 = 55.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 55.0% = $3.24/day`  

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
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 2 @ 5¢ → $3.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 4 (2 yours) | ×0.1^0 = 4.0 |
|  | 7¢ | 14 | ×0.1^2 = 0.1 |
|  | 9¢ | 50 | ×0.1^4 = 0.0 |
|  | 93¢ | 1 | ×0.1^88 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^93 = 0.0 |
| | | **Σ** | **4.1** |

`yours 2.0 / Σ 4.1 = 48.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 48.3% = $3.02/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 21¢ → $1.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 20¢ | 5 | ×0.2^1 = 1.0 |
|  | 15¢ | 208 | ×0.2^6 = 0.0 |
|  | 14¢ | 4,644 | ×0.2^7 = 0.1 |
|  | 11¢ | 54 | ×0.2^10 = 0.0 |
|  | 10¢ | 218 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 48.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.2% = $1.86/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5 @ 20¢ → $1.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 20¢ | 5 (5 yours) | ×0.2^1 = 1.0 |
|  | 15¢ | 208 | ×0.2^6 = 0.0 |
|  | 14¢ | 4,644 | ×0.2^7 = 0.1 |
|  | 11¢ | 54 | ×0.2^10 = 0.0 |
|  | 10¢ | 218 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 48.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.2% = $1.86/day`  

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
<details><summary><code>ussewc-usse-la-2026-11-03-rep</code> BUY 4 @ 91¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 9 (4 yours) | ×0.1^0 = 9.0 |
|  | 83¢ | 50 | ×0.1^8 = 0.0 |
|  | 68¢ | 5 | ×0.1^23 = 0.0 |
|  | 31¢ | 1 | ×0.1^60 = 0.0 |
|  | 15¢ | 14 | ×0.1^76 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^89 = 0.0 |
| | | **Σ** | **9.0** |

`yours 4.0 / Σ 9.0 = 44.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.4% = $2.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem`
2. `ussewc-usse-la-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 50 @ 9¢ → $1.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 113 (50 yours) | ×0.2^0 = 112.8 |
|  | 1¢ | 20,368 | ×0.2^8 = 0.1 |
| | | **Σ** | **112.8** |

`yours 50.0 / Σ 112.8 = 44.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 44.3% = $1.64/day`  

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
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 3 @ 5¢ → $2.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 6 (3 yours) | ×0.1^0 = 6.0 |
|  | 6¢ | 3 | ×0.1^1 = 0.3 |
|  | 7¢ | 50 | ×0.1^2 = 0.5 |
|  | 93¢ | 7 | ×0.1^88 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^93 = 0.0 |
| | | **Σ** | **6.8** |

`yours 3.0 / Σ 6.8 = 44.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.1% = $2.76/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> SELL 1 @ 94¢ → $2.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 95¢ | 2 | ×0.1^1 = 0.2 |
|  | 96¢ | 5 | ×0.1^2 = 0.1 |
|  | 99¢ | 2,706 | ×0.1^5 = 0.0 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 43.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 43.9% = $2.74/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 1 @ 17¢ → $1.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 16¢ | 0 | ×0.2^1 = 0.0 |
|  | 15¢ | 0 | ×0.2^2 = 0.0 |
|  | 14¢ | 100 | ×0.2^3 = 0.8 |
|  | 12¢ | 333 | ×0.2^5 = 0.1 |
|  | 11¢ | 6,069 | ×0.2^6 = 0.4 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 43.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.5% = $1.67/day`  

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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 3 @ 6¢ → $2.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 7 (3 yours) | ×0.1^0 = 7.0 |
|  | 7¢ | 1 | ×0.1^1 = 0.1 |
|  | 9¢ | 50 | ×0.1^3 = 0.1 |
|  | 28¢ | 1 | ×0.1^22 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **7.2** |

`yours 3.0 / Σ 7.2 = 42.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 42.0% = $2.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (821,650 resting) | ~58.7% | ~$44.05 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,736 resting) | ~62.6% | ~$15.65 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,199 resting) | ~58.4% | ~$14.60 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (66,381 resting) | ~17.1% | ~$12.84 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (634,806 resting) | ~10.6% | ~$2.66 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (286,724 resting) | ~2.6% | ~$1.94 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (381,468 resting) | ~29.8% | ~$1.87 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (780,340 resting) | ~2.3% | ~$1.70 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,242,602 resting) | ~26.9% | ~$1.68 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (286,163 resting) | ~2.1% | ~$1.60 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (79,236 resting) | ~22.2% | ~$1.39 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (76,514 resting) | ~22.2% | ~$1.39 |

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
| 2026-08-19 3:20 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 1:36 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 10:41 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:41 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:37 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:34 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:30 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:23 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:19 PM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
