# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-19 4:20 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$296.71/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `paccc-usho-midterms-2026-11-03-rep` — BUY at the best price, ~$44.05/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$24.88/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$15.01/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$296.71/day (~$12.36/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 57.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,589 resting ≥ 5,000 ✓) ≈ $4.17/day (event pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 8.0¢ | 13 | 0 | $100.00 | ✅ scoring — ~99.9% of ask side (77,836 resting ≥ 5,000 ✓) ≈ $3.84/day (event pool ÷ 13 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~98.9% of ask side (66,194 resting ≥ 2,000 ✓) ≈ $6.18/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~98.8% of bid side (50,347 resting ≥ 20,000 ✓) ≈ $3.66/day (event pool ÷ 27 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~98.5% of ask side (92,836 resting ≥ 5,000 ✓) ≈ $3.79/day (event pool ÷ 13 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~93.9% of bid side (2,029 resting ≥ 2,000 ✓) ≈ $5.87/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 10.0¢ | 82 | 1 | $200.00 | ✅ scoring — ~91.1% of bid side (61,219 resting ≥ 20,000 ✓) ≈ $6.50/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | BUY | 23.0¢ | 37 | 0 | $200.00 | ✅ scoring — ~91.0% of bid side (221,852 resting ≥ 20,000 ✓) ≈ $5.35/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 9.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~88.6% of bid side (50,414 resting ≥ 5,000 ✓) ≈ $3.41/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~84.5% of bid side (2,013 resting ≥ 2,000 ✓) ≈ $5.28/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (196,042 resting ≥ 2,000 ✓) ≈ $5.20/day (event pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | SELL | 11.0¢ | 75 | 1 | $25.00 | ✅ scoring — ~78.9% of ask side (2,500 resting ≥ 2,000 ✓) ≈ $1.41/day (event pool ÷ 7 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~78.3% of bid side (4,292 resting ≥ 2,000 ✓) ≈ $4.89/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~78.3% of bid side (2,029 resting ≥ 2,000 ✓) ≈ $4.89/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 80 | 0 | $200.00 | ✅ scoring — ~74.4% of bid side (91,923 resting ≥ 20,000 ✓) ≈ $4.37/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 82.0¢ | 5 | 2 | $25.00 | ✅ scoring — ~71.4% of bid side (502,170 resting ≥ 2,000 ✓) ≈ $4.46/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 11.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~59.7% of bid side (126,823 resting ≥ 20,000 ✓) ≈ $3.51/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 17.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~54.3% of bid side (51,045 resting ≥ 5,000 ✓) ≈ $2.09/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 88.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~50.0% of ask side (65,235 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 21.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~50.0% of bid side (200,997 resting ≥ 5,000 ✓) ≈ $1.92/day (event pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 20.0¢ | 5 | 1 | $100.00 | ✅ scoring — ~50.0% of bid side (200,997 resting ≥ 5,000 ✓) ≈ $1.92/day (event pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | SELL | 5.0¢ | 32 | 0 | $200.00 | ✅ scoring — ~48.8% of ask side (48,349 resting ≥ 20,000 ✓) ≈ $2.87/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | SELL | 5.0¢ | 32 | 0 | $200.00 | ✅ scoring — ~48.2% of ask side (48,349 resting ≥ 20,000 ✓) ≈ $2.84/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~44.7% of bid side (500,281 resting ≥ 2,000 ✓) ≈ $2.80/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~44.7% of bid side (500,281 resting ≥ 2,000 ✓) ≈ $2.80/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~44.4% of ask side (65,530 resting ≥ 2,000 ✓) ≈ $2.78/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~44.4% of ask side (65,530 resting ≥ 2,000 ✓) ≈ $2.78/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-rep` | BUY | 91.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~44.4% of bid side (500,310 resting ≥ 2,000 ✓) ≈ $2.78/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 9.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~44.3% of bid side (20,481 resting ≥ 20,000 ✓) ≈ $1.64/day (event pool ÷ 27 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~41.7% of bid side (23,205 resting ≥ 5,000 ✓) ≈ $10.42/day (event pool ÷ 2 markets) |
| …and 2638 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 1 @ 57¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 55¢ | 0 | ×0.2^2 = 0.0 |
|  | 42¢ | 138 | ×0.2^15 = 0.0 |
|  | 2¢ | 300,250 | ×0.2^55 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 13 @ 8¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 13 (13 yours) | ×0.2^0 = 13.0 |
|  | 15¢ | 562 | ×0.2^7 = 0.0 |
|  | 22¢ | 100 | ×0.2^14 = 0.0 |
|  | 24¢ | 150 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^89 = 0.0 |
| | | **Σ** | **13.0** |

`yours 13.0 / Σ 13.0 = 99.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.9% = $3.84/day`  

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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $6.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 10¢ | 2 | ×0.1^2 = 0.0 |
|  | 11¢ | 2 | ×0.1^3 = 0.0 |
|  | 13¢ | 2 | ×0.1^5 = 0.0 |
|  | 14¢ | 1 | ×0.1^6 = 0.0 |
|  | 15¢ | 160 | ×0.1^7 = 0.0 |
|  | 18¢ | 50 | ×0.1^10 = 0.0 |
|  | 45¢ | 500 | ×0.1^37 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^90 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 98.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.9% = $6.18/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 15 @ 18¢ → $3.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 15 (15 yours) | ×0.2^0 = 14.6 |
|  | 19¢ | 0 | ×0.2^1 = 0.0 |
|  | 21¢ | 20 | ×0.2^3 = 0.2 |
|  | 22¢ | 27 | ×0.2^4 = 0.0 |
|  | 23¢ | 5 | ×0.2^5 = 0.0 |
|  | 24¢ | 5 | ×0.2^6 = 0.0 |
|  | 25¢ | 10 | ×0.2^7 = 0.0 |
|  | 26¢ | 5 | ×0.2^8 = 0.0 |
|  | 27¢ | 5 | ×0.2^9 = 0.0 |
|  | 29¢ | 50 | ×0.2^11 = 0.0 |
| | … | +6 levels | 0.0 |
| | | **Σ** | **14.9** |

`yours 14.6 / Σ 14.9 = 98.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.5% = $3.79/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 10 @ 12¢ → $5.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 11¢ | 5 | ×0.1^1 = 0.5 |
|  | 10¢ | 15 | ×0.1^2 = 0.2 |
|  | 1¢ | 1,999 | ×0.1^11 = 0.0 |
| | | **Σ** | **10.7** |

`yours 10.0 / Σ 10.7 = 93.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.9% = $5.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 82 @ 10¢ → $6.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 10¢ | 85 (82 yours) | ×0.2^1 = 17.0 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 3¢ | 1 | ×0.2^8 = 0.0 |
|  | 2¢ | 10,472 | ×0.2^9 = 0.0 |
|  | 1¢ | 50,659 | ×0.2^10 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1 @ 9¢ → $3.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 1¢ | 50,413 | ×0.2^8 = 0.1 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.6% = $3.41/day`  

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
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $5.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 13 | ×0.1^0 = 13.0 |
| ▶ | 1¢ | 2,000 (1,799 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **213.0** |

`yours 179.9 / Σ 213.0 = 84.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 84.5% = $5.28/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 10 @ 13¢ → $5.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 12 (10 yours) | ×0.1^0 = 12.0 |
|  | 15¢ | 1 | ×0.1^2 = 0.0 |
|  | 25¢ | 50 | ×0.1^12 = 0.0 |
|  | 35¢ | 3 | ×0.1^22 = 0.0 |
|  | 40¢ | 1 | ×0.1^27 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^85 = 0.0 |
| | | **Σ** | **12.0** |

`yours 10.0 / Σ 12.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 5 @ 82¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 84¢ | 0 | ×0.1^0 = 0.0 |
| ▶ | 82¢ | 5 (5 yours) | ×0.1^2 = 0.1 |
|  | 74¢ | 152 | ×0.1^10 = 0.0 |
|  | 65¢ | 8 | ×0.1^19 = 0.0 |
|  | 60¢ | 1 | ×0.1^24 = 0.0 |
|  | 10¢ | 5 | ×0.1^74 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^82 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 1 @ 11¢ → $3.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
|  | 8¢ | 5 | ×0.2^3 = 0.0 |
|  | 6¢ | 255 | ×0.2^5 = 0.1 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 4¢ | 40,110 | ×0.2^7 = 0.5 |
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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 1 @ 17¢ → $2.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 16¢ | 0 | ×0.2^1 = 0.0 |
|  | 15¢ | 0 | ×0.2^2 = 0.0 |
|  | 14¢ | 100 | ×0.2^3 = 0.8 |
|  | 12¢ | 21 | ×0.2^5 = 0.0 |
|  | 11¢ | 473 | ×0.2^6 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^15 = 0.0 |
| | | **Σ** | **1.8** |

`yours 1.0 / Σ 1.8 = 54.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 54.3% = $2.09/day`  

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 1 @ 88¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 97¢ | 5,328 | ×0.1^9 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 21¢ → $1.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 20¢ | 5 | ×0.2^1 = 1.0 |
|  | 15¢ | 30 | ×0.2^6 = 0.0 |
|  | 14¢ | 2 | ×0.2^7 = 0.0 |
|  | 11¢ | 54 | ×0.2^10 = 0.0 |
|  | 10¢ | 70 | ×0.2^11 = 0.0 |
|  | 2¢ | 326 | ×0.2^19 = 0.0 |
|  | 1¢ | 200,509 | ×0.2^20 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 50.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 50.0% = $1.92/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5 @ 20¢ → $1.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 20¢ | 5 (5 yours) | ×0.2^1 = 1.0 |
|  | 15¢ | 30 | ×0.2^6 = 0.0 |
|  | 14¢ | 2 | ×0.2^7 = 0.0 |
|  | 11¢ | 54 | ×0.2^10 = 0.0 |
|  | 10¢ | 70 | ×0.2^11 = 0.0 |
|  | 2¢ | 326 | ×0.2^19 = 0.0 |
|  | 1¢ | 200,509 | ×0.2^20 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 50.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 50.0% = $1.92/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> SELL 32 @ 5¢ → $2.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 66 (32 yours) | ×0.2^0 = 66.4 |
|  | 15¢ | 30,483 | ×0.2^10 = 0.0 |
| | | **Σ** | **66.4** |

`yours 32.4 / Σ 66.4 = 48.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 48.8% = $2.87/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri` ← this one
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
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> SELL 32 @ 5¢ → $2.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 66 (32 yours) | ×0.2^0 = 66.4 |
|  | 15¢ | 30,483 | ×0.2^10 = 0.0 |
| | | **Σ** | **66.4** |

`yours 32.0 / Σ 66.4 = 48.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 48.2% = $2.84/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri` ← this one
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
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 3 @ 95¢ → $2.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 6 (3 yours) | ×0.1^0 = 6.0 |
|  | 94¢ | 7 | ×0.1^1 = 0.7 |
|  | 91¢ | 50 | ×0.1^4 = 0.0 |
|  | 15¢ | 18 | ×0.1^80 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **6.7** |

`yours 3.0 / Σ 6.7 = 44.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.7% = $2.80/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 3 @ 95¢ → $2.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 6 (3 yours) | ×0.1^0 = 6.0 |
|  | 94¢ | 7 | ×0.1^1 = 0.7 |
|  | 91¢ | 50 | ×0.1^4 = 0.0 |
|  | 15¢ | 18 | ×0.1^80 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **6.7** |

`yours 3.0 / Σ 6.7 = 44.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.7% = $2.80/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 1 @ 6¢ → $2.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 7¢ | 2 | ×0.1^1 = 0.2 |
|  | 9¢ | 50 | ×0.1^3 = 0.1 |
|  | 28¢ | 1 | ×0.1^22 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 44.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.4% = $2.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 1 @ 6¢ → $2.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 7¢ | 2 | ×0.1^1 = 0.2 |
|  | 9¢ | 50 | ×0.1^3 = 0.1 |
|  | 28¢ | 1 | ×0.1^22 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 44.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.4% = $2.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-rep</code> BUY 4 @ 91¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 9 (4 yours) | ×0.1^0 = 9.0 |
|  | 83¢ | 80 | ×0.1^8 = 0.0 |
|  | 68¢ | 5 | ×0.1^23 = 0.0 |
|  | 31¢ | 1 | ×0.1^60 = 0.0 |
|  | 15¢ | 15 | ×0.1^76 = 0.0 |
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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (819,567 resting) | ~58.7% | ~$44.05 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (41,299 resting) | ~99.5% | ~$24.88 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (26,969 resting) | ~60.0% | ~$15.01 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (66,373 resting) | ~16.8% | ~$12.57 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (282,167 resting) | ~6.7% | ~$5.03 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (78,645 resting) | ~57.1% | ~$3.57 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (634,202 resting) | ~7.0% | ~$1.76 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (780,378 resting) | ~2.3% | ~$1.69 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,242,574 resting) | ~25.2% | ~$1.57 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (287,162 resting) | ~1.9% | ~$1.40 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (77,097 resting) | ~22.1% | ~$1.38 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (58,061 resting) | ~1.7% | ~$1.24 |

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
| 2026-08-19 4:20 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 3:20 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 1:36 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 10:41 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:41 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:37 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:34 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:30 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:23 PM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
