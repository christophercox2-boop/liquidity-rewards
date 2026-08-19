# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-19 11:59 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$389.42/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$20.98/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$11.44/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$9.01/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$389.42/day (~$16.23/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 89.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.8% of ask side (2,057 resting ≥ 2,000 ✓) ≈ $6.24/day (event pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.7% of ask side (330,182 resting ≥ 2,000 ✓) ≈ $6.23/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~99.3% of bid side (500,217 resting ≥ 2,000 ✓) ≈ $6.21/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.0% of ask side (70,585 resting ≥ 2,000 ✓) ≈ $6.19/day (event pool ÷ 2 markets) |
| `ussewc-usse-ma-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~98.7% of ask side (65,482 resting ≥ 2,000 ✓) ≈ $6.17/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 37.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~95.2% of bid side (400,552 resting ≥ 5,000 ✓) ≈ $3.97/day (event pool ÷ 12 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~94.7% of ask side (66,146 resting ≥ 2,000 ✓) ≈ $5.92/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 89.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.9% of ask side (65,235 resting ≥ 2,000 ✓) ≈ $5.68/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~89.0% of bid side (50,362 resting ≥ 20,000 ✓) ≈ $3.30/day (event pool ÷ 27 markets) |
| `ussewc-usse-de-2026-11-03-rep` | BUY | 1.0¢ | 1,798 | 1 | $25.00 | ✅ scoring — ~88.2% of bid side (2,003 resting ≥ 2,000 ✓) ≈ $5.51/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 0 | $25.00 | ✅ scoring — ~85.7% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $5.35/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~83.2% of ask side (65,484 resting ≥ 2,000 ✓) ≈ $5.20/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 10.0¢ | 134 | 0 | $200.00 | ✅ scoring — ~80.1% of bid side (133,231 resting ≥ 20,000 ✓) ≈ $4.71/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 9.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~75.6% of bid side (35,614 resting ≥ 5,000 ✓) ≈ $2.91/day (event pool ÷ 13 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~75.0% of bid side (600,237 resting ≥ 2,000 ✓) ≈ $4.69/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 10.0¢ | 82 | 1 | $200.00 | ✅ scoring — ~73.8% of bid side (73,649 resting ≥ 20,000 ✓) ≈ $5.27/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 77 | 0 | $200.00 | ✅ scoring — ~73.6% of bid side (98,170 resting ≥ 20,000 ✓) ≈ $4.33/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ma-2026-11-03-rep` | BUY | 1.0¢ | 1,666 | 1 | $25.00 | ✅ scoring — ~73.2% of bid side (2,267 resting ≥ 2,000 ✓) ≈ $4.57/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | BUY | 21.0¢ | 23 | 0 | $200.00 | ✅ scoring — ~72.6% of bid side (223,508 resting ≥ 20,000 ✓) ≈ $4.27/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-tulgab` | BUY | 1.0¢ | 19,238 | 2 | $200.00 | ✅ scoring — ~71.0% of bid side (22,000 resting ≥ 20,000 ✓) ≈ $5.07/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~70.3% of ask side (65,520 resting ≥ 2,000 ✓) ≈ $4.40/day (event pool ÷ 2 markets) |
| `ussewc-usse-ma-2026-11-03-dem` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~69.0% of bid side (600,420 resting ≥ 2,000 ✓) ≈ $4.31/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 13.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~67.8% of ask side (38,851 resting ≥ 20,000 ✓) ≈ $3.99/day (event pool ÷ 17 markets) |
| `ussewc-usse-la-2026-11-03-rep` | BUY | 91.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (500,223 resting ≥ 2,000 ✓) ≈ $4.17/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 85.0¢ | 2 | 2 | $25.00 | ✅ scoring — ~66.5% of bid side (502,114 resting ≥ 2,000 ✓) ≈ $4.16/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~63.9% of bid side (2,134 resting ≥ 2,000 ✓) ≈ $3.99/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~55.5% of ask side (195,999 resting ≥ 2,000 ✓) ≈ $3.47/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 120 | 0 | $200.00 | ✅ scoring — ~55.1% of bid side (60,572 resting ≥ 20,000 ✓) ≈ $2.04/day (event pool ÷ 27 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~53.6% of bid side (4,095 resting ≥ 2,000 ✓) ≈ $3.35/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 93.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (500,210 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| …and 2796 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 1 @ 89¢ → $6.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 92¢ | 2 | ×0.1^3 = 0.0 |
|  | 98¢ | 55 | ×0.1^9 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^10 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.8% = $6.24/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-rep</code> SELL 1 @ 6¢ → $6.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 9¢ | 3 | ×0.1^3 = 0.0 |
|  | 29¢ | 1 | ×0.1^23 = 0.0 |
|  | 44¢ | 1 | ×0.1^38 = 0.0 |
|  | 48¢ | 1 | ×0.1^42 = 0.0 |
|  | 60¢ | 1 | ×0.1^54 = 0.0 |
|  | 70¢ | 1 | ×0.1^64 = 0.0 |
|  | 93¢ | 1 | ×0.1^87 = 0.0 |
|  | 98¢ | 132,784 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.7% = $6.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem`
2. `ussewc-usse-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> BUY 3 @ 95¢ → $6.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 15¢ | 14 | ×0.1^80 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 99.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.3% = $6.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> SELL 1 @ 8¢ → $6.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 1 | ×0.1^2 = 0.0 |
|  | 12¢ | 1 | ×0.1^4 = 0.0 |
|  | 13¢ | 2 | ×0.1^5 = 0.0 |
|  | 15¢ | 2 | ×0.1^7 = 0.0 |
|  | 17¢ | 103 | ×0.1^9 = 0.0 |
|  | 32¢ | 5,000 | ×0.1^24 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.0% = $6.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ma-2026-11-03-rep</code> SELL 1 @ 6¢ → $6.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 8¢ | 1 | ×0.1^2 = 0.0 |
|  | 9¢ | 3 | ×0.1^3 = 0.0 |
|  | 72¢ | 1 | ×0.1^66 = 0.0 |
|  | 89¢ | 1 | ×0.1^83 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.7% = $6.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem`
2. `ussewc-usse-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 1 @ 37¢ → $3.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 9¢ | 100 | ×0.2^28 = 0.0 |
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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $5.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 9¢ | 1 | ×0.1^1 = 0.1 |
|  | 10¢ | 1 | ×0.1^2 = 0.0 |
|  | 11¢ | 3 | ×0.1^3 = 0.0 |
|  | 13¢ | 2 | ×0.1^5 = 0.0 |
|  | 14¢ | 2 | ×0.1^6 = 0.0 |
|  | 15¢ | 160 | ×0.1^7 = 0.0 |
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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 1 @ 89¢ → $5.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 90¢ | 1 | ×0.1^1 = 0.1 |
|  | 97¢ | 5,328 | ×0.1^8 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.9% = $5.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

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
<details><summary><code>ussewc-usse-de-2026-11-03-rep</code> BUY 1,798 @ 1¢ → $5.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 4 | ×0.1^0 = 4.0 |
| ▶ | 1¢ | 1,999 (1,798 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **203.9** |

`yours 179.8 / Σ 203.9 = 88.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 88.2% = $5.51/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-de-2026-11-03-dem`
2. `ussewc-usse-de-2026-11-03-rep` ← this one

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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 1 @ 6¢ → $5.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 7¢ | 2 | ×0.1^1 = 0.2 |
|  | 9¢ | 2 | ×0.1^3 = 0.0 |
|  | 28¢ | 1 | ×0.1^22 = 0.0 |
|  | 75¢ | 1 | ×0.1^69 = 0.0 |
|  | 82¢ | 1 | ×0.1^76 = 0.0 |
|  | 86¢ | 1 | ×0.1^80 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 83.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.2% = $5.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 134 @ 10¢ → $4.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 164 (134 yours) | ×0.2^0 = 164.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 6¢ | 255 | ×0.2^4 = 0.4 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 4¢ | 46,360 | ×0.2^6 = 3.0 |
| | | **Σ** | **167.4** |

`yours 134.0 / Σ 167.4 = 80.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 80.1% = $4.71/day`  

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
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> BUY 3 @ 94¢ → $4.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 4 (3 yours) | ×0.1^0 = 4.0 |
|  | 54¢ | 1 | ×0.1^40 = 0.0 |
|  | 49¢ | 1 | ×0.1^45 = 0.0 |
|  | 46¢ | 6 | ×0.1^48 = 0.0 |
|  | 40¢ | 25 | ×0.1^54 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **4.0** |

`yours 3.0 / Σ 4.0 = 75.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.0% = $4.69/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 82 @ 10¢ → $5.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 5 | ×0.2^0 = 5.2 |
| ▶ | 10¢ | 85 (82 yours) | ×0.2^1 = 17.0 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 3¢ | 1 | ×0.2^8 = 0.0 |
|  | 2¢ | 22,972 | ×0.2^9 = 0.0 |
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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 77 @ 12¢ → $4.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 104 (77 yours) | ×0.2^0 = 104.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 8¢ | 6 | ×0.2^4 = 0.0 |
|  | 7¢ | 60 | ×0.2^5 = 0.0 |
|  | 6¢ | 125 | ×0.2^6 = 0.0 |
|  | 5¢ | 5,000 | ×0.2^7 = 0.1 |
|  | 4¢ | 6,250 | ×0.2^8 = 0.0 |
|  | 3¢ | 171 | ×0.2^9 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **104.6** |

`yours 77.0 / Σ 104.6 = 73.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 73.6% = $4.33/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> BUY 23 @ 21¢ → $4.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 24 (23 yours) | ×0.2^0 = 24.1 |
|  | 20¢ | 1 | ×0.2^1 = 0.2 |
|  | 19¢ | 8 | ×0.2^2 = 0.3 |
|  | 18¢ | 36 | ×0.2^3 = 0.3 |
|  | 17¢ | 112 | ×0.2^4 = 0.2 |
|  | 16¢ | 21,110 | ×0.2^5 = 6.8 |
| | | **Σ** | **31.9** |

`yours 23.1 / Σ 31.9 = 72.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 72.6% = $4.27/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-tulgab</code> BUY 19,238 @ 1¢ → $5.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 212 | ×0.2^0 = 212.0 |
| ▶ | 1¢ | 21,788 (19,238 yours) | ×0.2^2 = 871.5 |
| | | **Σ** | **1,083.5** |

`yours 769.5 / Σ 1,083.5 = 71.0%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 71.0% = $5.07/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 1 @ 5¢ → $4.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 7¢ | 42 | ×0.1^2 = 0.4 |
|  | 8¢ | 2 | ×0.1^3 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.4** |

`yours 1.0 / Σ 1.4 = 70.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.3% = $4.40/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ma-2026-11-03-dem</code> BUY 3 @ 94¢ → $4.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 4 (3 yours) | ×0.1^0 = 4.0 |
|  | 92¢ | 35 | ×0.1^2 = 0.4 |
|  | 3¢ | 181 | ×0.1^91 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **4.3** |

`yours 3.0 / Σ 4.3 = 69.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 69.0% = $4.31/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem` ← this one
2. `ussewc-usse-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> SELL 3 @ 13¢ → $3.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 4 (3 yours) | ×0.2^0 = 4.0 |
|  | 16¢ | 41 | ×0.2^3 = 0.3 |
|  | 17¢ | 62 | ×0.2^4 = 0.1 |
|  | 19¢ | 4 | ×0.2^6 = 0.0 |
|  | 26¢ | 20,990 | ×0.2^13 = 0.0 |
| | | **Σ** | **4.4** |

`yours 3.0 / Σ 4.4 = 67.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 67.8% = $3.99/day`  

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
<details><summary><code>ussewc-usse-la-2026-11-03-rep</code> BUY 4 @ 91¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 6 (4 yours) | ×0.1^0 = 6.0 |
|  | 68¢ | 5 | ×0.1^23 = 0.0 |
|  | 31¢ | 1 | ×0.1^60 = 0.0 |
|  | 15¢ | 11 | ×0.1^76 = 0.0 |
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
|  | 74¢ | 102 | ×0.1^13 = 0.0 |
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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 10 @ 12¢ → $3.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 15 (10 yours) | ×0.1^0 = 15.0 |
|  | 11¢ | 5 | ×0.1^1 = 0.5 |
|  | 10¢ | 15 | ×0.1^2 = 0.2 |
|  | 1¢ | 2,099 | ×0.1^11 = 0.0 |
| | | **Σ** | **15.7** |

`yours 10.0 / Σ 15.7 = 63.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.9% = $3.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 10 @ 13¢ → $3.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 18 (10 yours) | ×0.1^0 = 18.0 |
|  | 15¢ | 1 | ×0.1^2 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 120 @ 5¢ → $2.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 120 (120 yours) | ×0.2^0 = 120.0 |
|  | 4¢ | 4 | ×0.2^1 = 0.8 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 60,443 | ×0.2^4 = 96.7 |
| | | **Σ** | **217.6** |

`yours 120.0 / Σ 217.6 = 55.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 55.1% = $2.04/day`  

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
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 2 @ 7¢ → $3.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 3 (2 yours) | ×0.1^0 = 3.0 |
|  | 6¢ | 7 | ×0.1^1 = 0.7 |
|  | 5¢ | 2 | ×0.1^2 = 0.0 |
|  | 3¢ | 42 | ×0.1^4 = 0.0 |
|  | 2¢ | 243 | ×0.1^5 = 0.0 |
|  | 1¢ | 3,798 | ×0.1^6 = 0.0 |
| | | **Σ** | **3.7** |

`yours 2.0 / Σ 3.7 = 53.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 53.6% = $3.35/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 3 @ 93¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 6 (3 yours) | ×0.1^0 = 6.0 |
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
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,284 resting) | ~83.9% | ~$20.98 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (61,429 resting) | ~15.3% | ~$11.44 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,842 resting) | ~36.0% | ~$9.01 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (925,258 resting) | ~9.9% | ~$7.46 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (522,108 resting) | ~7.7% | ~$5.77 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (89,117 resting) | ~71.0% | ~$4.43 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (26,432 resting) | ~5.4% | ~$4.03 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (269,984 resting) | ~3.7% | ~$2.79 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (373,122 resting) | ~41.5% | ~$2.59 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (632,073 resting) | ~8.9% | ~$2.24 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (828,009 resting) | ~2.7% | ~$2.05 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (794,648 resting) | ~2.5% | ~$1.91 |

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
| 2026-08-19 11:59 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 10:58 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 9:44 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 8:44 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 7:22 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 6:21 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 5:21 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 4:20 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 3:20 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 1:36 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
