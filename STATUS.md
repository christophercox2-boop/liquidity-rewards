# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-19 5:21 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$257.28/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `paccc-usho-midterms-2026-11-03-rep` — BUY at the best price, ~$41.06/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$24.88/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$15.14/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$257.28/day (~$10.72/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~99.4% of ask side (66,194 resting ≥ 2,000 ✓) ≈ $6.21/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~93.7% of bid side (2,031 resting ≥ 2,000 ✓) ≈ $5.86/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | BUY | 23.0¢ | 37 | 0 | $200.00 | ✅ scoring — ~91.0% of bid side (221,852 resting ≥ 20,000 ✓) ≈ $5.35/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~89.8% of bid side (50,361 resting ≥ 20,000 ✓) ≈ $3.33/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 0 | $25.00 | ✅ scoring — ~85.7% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $5.35/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (196,042 resting ≥ 2,000 ✓) ≈ $5.20/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 10.0¢ | 82 | 1 | $200.00 | ✅ scoring — ~82.8% of bid side (61,221 resting ≥ 20,000 ✓) ≈ $5.91/day (event pool ÷ 14 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | SELL | 11.0¢ | 75 | 1 | $25.00 | ✅ scoring — ~78.9% of ask side (2,500 resting ≥ 2,000 ✓) ≈ $1.41/day (event pool ÷ 7 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~78.3% of bid side (4,292 resting ≥ 2,000 ✓) ≈ $4.89/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 80 | 0 | $200.00 | ✅ scoring — ~74.4% of bid side (91,923 resting ≥ 20,000 ✓) ≈ $4.37/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 8.0¢ | 13 | 0 | $100.00 | ✅ scoring — ~72.3% of ask side (77,741 resting ≥ 5,000 ✓) ≈ $2.78/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 82.0¢ | 5 | 2 | $25.00 | ✅ scoring — ~71.4% of bid side (502,170 resting ≥ 2,000 ✓) ≈ $4.46/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~67.4% of ask side (92,843 resting ≥ 5,000 ✓) ≈ $2.59/day (event pool ÷ 13 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 87.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~60.1% of ask side (2,559 resting ≥ 2,000 ✓) ≈ $3.75/day (event pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~52.6% of ask side (65,603 resting ≥ 2,000 ✓) ≈ $3.29/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | SELL | 94.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~44.5% of ask side (2,713 resting ≥ 2,000 ✓) ≈ $2.78/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-rep` | BUY | 91.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~44.4% of bid side (500,280 resting ≥ 2,000 ✓) ≈ $2.78/day (event pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~41.7% of bid side (23,205 resting ≥ 5,000 ✓) ≈ $10.42/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 9.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~40.3% of bid side (20,492 resting ≥ 20,000 ✓) ≈ $1.49/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-ma-2026-11-03-rep` | SELL | 2.0¢ | 133 | 0 | $25.00 | ✅ scoring — ~39.6% of ask side (11,918 resting ≥ 2,000 ✓) ≈ $2.47/day (event pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 95.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~38.1% of bid side (500,496 resting ≥ 2,000 ✓) ≈ $2.38/day (event pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~34.1% of bid side (600,299 resting ≥ 2,000 ✓) ≈ $2.13/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 22.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~33.2% of ask side (91,922 resting ≥ 5,000 ✓) ≈ $1.28/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 91.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~31.9% of bid side (500,681 resting ≥ 2,000 ✓) ≈ $2.00/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 91.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~31.9% of bid side (500,681 resting ≥ 2,000 ✓) ≈ $2.00/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 91.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~31.9% of bid side (500,681 resting ≥ 2,000 ✓) ≈ $2.00/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 2 | $25.00 | ✅ scoring — ~31.5% of bid side (4,783 resting ≥ 2,000 ✓) ≈ $1.97/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 13.0¢ | 92 | 1 | $100.00 | ✅ scoring — ~30.5% of bid side (300,608 resting ≥ 5,000 ✓) ≈ $1.17/day (event pool ÷ 13 markets) |
| `ussewc-usse-il-2026-11-03-rep` | SELL | 5.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~28.1% of ask side (330,233 resting ≥ 2,000 ✓) ≈ $1.76/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-kamhar` | SELL | 5.0¢ | 286 | 0 | $200.00 | ✅ scoring — ~27.3% of ask side (67,801 resting ≥ 20,000 ✓) ≈ $1.01/day (event pool ÷ 27 markets) |
| …and 2682 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $6.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 10¢ | 1 | ×0.1^2 = 0.0 |
|  | 11¢ | 2 | ×0.1^3 = 0.0 |
|  | 13¢ | 2 | ×0.1^5 = 0.0 |
|  | 14¢ | 2 | ×0.1^6 = 0.0 |
|  | 15¢ | 160 | ×0.1^7 = 0.0 |
|  | 18¢ | 50 | ×0.1^10 = 0.0 |
|  | 45¢ | 500 | ×0.1^37 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^90 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 99.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.4% = $6.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 10 @ 12¢ → $5.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 11¢ | 5 | ×0.1^1 = 0.5 |
|  | 10¢ | 17 | ×0.1^2 = 0.2 |
|  | 1¢ | 1,999 | ×0.1^11 = 0.0 |
| | | **Σ** | **10.7** |

`yours 10.0 / Σ 10.7 = 93.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.7% = $5.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 150 (135 yours) | ×0.2^0 = 149.6 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **150.3** |

`yours 135.0 / Σ 150.3 = 89.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 89.8% = $3.33/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 82 @ 10¢ → $5.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 3 | ×0.2^0 = 2.8 |
| ▶ | 10¢ | 85 (82 yours) | ×0.2^1 = 17.0 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 3¢ | 1 | ×0.2^8 = 0.0 |
|  | 2¢ | 10,472 | ×0.2^9 = 0.0 |
|  | 1¢ | 50,659 | ×0.2^10 = 0.0 |
| | | **Σ** | **19.8** |

`yours 16.4 / Σ 19.8 = 82.8%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 82.8% = $5.91/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 13 @ 8¢ → $2.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 18 (13 yours) | ×0.2^0 = 18.0 |
|  | 15¢ | 562 | ×0.2^7 = 0.0 |
|  | 22¢ | 100 | ×0.2^14 = 0.0 |
|  | 24¢ | 50 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^89 = 0.0 |
| | | **Σ** | **18.0** |

`yours 13.0 / Σ 18.0 = 72.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 72.3% = $2.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 15 @ 18¢ → $2.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 22 (15 yours) | ×0.2^0 = 21.6 |
|  | 19¢ | 0 | ×0.2^1 = 0.0 |
|  | 22¢ | 27 | ×0.2^4 = 0.0 |
|  | 23¢ | 25 | ×0.2^5 = 0.0 |
|  | 24¢ | 5 | ×0.2^6 = 0.0 |
|  | 25¢ | 10 | ×0.2^7 = 0.0 |
|  | 26¢ | 5 | ×0.2^8 = 0.0 |
|  | 27¢ | 5 | ×0.2^9 = 0.0 |
|  | 29¢ | 50 | ×0.2^11 = 0.0 |
|  | 35¢ | 1 | ×0.2^17 = 0.0 |
| | … | +5 levels | 0.0 |
| | | **Σ** | **21.7** |

`yours 14.6 / Σ 21.7 = 67.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.4% = $2.59/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 1 @ 87¢ → $3.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 88¢ | 1 | ×0.1^1 = 0.1 |
|  | 89¢ | 1 | ×0.1^2 = 0.0 |
|  | 90¢ | 555 | ×0.1^3 = 0.6 |
|  | 92¢ | 2 | ×0.1^5 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^12 = 0.0 |
| | | **Σ** | **1.7** |

`yours 1.0 / Σ 1.7 = 60.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.1% = $3.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 1 @ 4¢ → $3.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 5¢ | 9 | ×0.1^1 = 0.9 |
|  | 9¢ | 50 | ×0.1^5 = 0.0 |
|  | 22¢ | 1 | ×0.1^18 = 0.0 |
|  | 25¢ | 1 | ×0.1^21 = 0.0 |
|  | 26¢ | 1 | ×0.1^22 = 0.0 |
|  | 33¢ | 1 | ×0.1^29 = 0.0 |
|  | 44¢ | 1 | ×0.1^40 = 0.0 |
|  | 52¢ | 63 | ×0.1^48 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^94 = 0.0 |
| | | **Σ** | **1.9** |

`yours 1.0 / Σ 1.9 = 52.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 52.6% = $3.29/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

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
<details><summary><code>ussewc-usse-la-2026-11-03-rep</code> BUY 4 @ 91¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 9 (4 yours) | ×0.1^0 = 9.0 |
|  | 83¢ | 50 | ×0.1^8 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 50 @ 9¢ → $1.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 124 (50 yours) | ×0.2^0 = 124.0 |
|  | 1¢ | 20,368 | ×0.2^8 = 0.1 |
| | | **Σ** | **124.1** |

`yours 50.0 / Σ 124.1 = 40.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 40.3% = $1.49/day`  

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
<details><summary><code>usgubewc-usgub-ma-2026-11-03-rep</code> SELL 133 @ 2¢ → $2.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 335 (133 yours) | ×0.1^0 = 335.0 |
|  | 6¢ | 9,531 | ×0.1^4 = 1.0 |
| | | **Σ** | **336.0** |

`yours 133.0 / Σ 336.0 = 39.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 39.6% = $2.47/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem`
2. `usgubewc-usgub-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 35 @ 95¢ → $2.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 91 (35 yours) | ×0.1^0 = 91.0 |
|  | 94¢ | 4 | ×0.1^1 = 0.4 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 58¢ | 1 | ×0.1^37 = 0.0 |
|  | 12¢ | 150 | ×0.1^83 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **91.9** |

`yours 35.0 / Σ 91.9 = 38.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 38.1% = $2.38/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> BUY 3 @ 95¢ → $2.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 8 (3 yours) | ×0.1^0 = 8.0 |
|  | 94¢ | 3 | ×0.1^1 = 0.3 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 46¢ | 13 | ×0.1^49 = 0.0 |
|  | 40¢ | 25 | ×0.1^55 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **8.8** |

`yours 3.0 / Σ 8.8 = 34.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 34.1% = $2.13/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 1 @ 22¢ → $1.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 3 (1 yours) | ×0.2^0 = 3.0 |
|  | 28¢ | 126 | ×0.2^6 = 0.0 |
|  | 29¢ | 50 | ×0.2^7 = 0.0 |
|  | 67¢ | 51 | ×0.2^45 = 0.0 |
|  | 68¢ | 1 | ×0.2^46 = 0.0 |
|  | 69¢ | 1 | ×0.2^47 = 0.0 |
|  | 70¢ | 1 | ×0.2^48 = 0.0 |
|  | 71¢ | 1 | ×0.2^49 = 0.0 |
|  | 72¢ | 1 | ×0.2^50 = 0.0 |
|  | 73¢ | 1 | ×0.2^51 = 0.0 |
| | … | +24 levels | 0.0 |
| | | **Σ** | **3.0** |

`yours 1.0 / Σ 3.0 = 33.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.2% = $1.28/day`  

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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 3 @ 91¢ → $2.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 9 (3 yours) | ×0.1^0 = 9.0 |
|  | 88¢ | 398 | ×0.1^3 = 0.4 |
|  | 75¢ | 50 | ×0.1^16 = 0.0 |
|  | 44¢ | 1 | ×0.1^47 = 0.0 |
|  | 43¢ | 17 | ×0.1^48 = 0.0 |
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
|  | 43¢ | 17 | ×0.1^48 = 0.0 |
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
|  | 43¢ | 17 | ×0.1^48 = 0.0 |
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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $1.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 2 | ×0.1^0 = 2.0 |
|  | 2¢ | 82 | ×0.1^1 = 8.2 |
| ▶ | 1¢ | 4,699 (1,799 yours) | ×0.1^2 = 47.0 |
| | | **Σ** | **57.2** |

`yours 18.0 / Σ 57.2 = 31.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 31.5% = $1.97/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 92 @ 13¢ → $1.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 42 | ×0.2^0 = 42.0 |
| ▶ | 13¢ | 92 (92 yours) | ×0.2^1 = 18.5 |
|  | 1¢ | 300,474 | ×0.2^13 = 0.0 |
| | | **Σ** | **60.5** |

`yours 18.5 / Σ 60.5 = 30.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.5% = $1.17/day`  

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
<details><summary><code>ussewc-usse-il-2026-11-03-rep</code> SELL 2 @ 5¢ → $1.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 7 (2 yours) | ×0.1^0 = 7.0 |
|  | 6¢ | 1 | ×0.1^1 = 0.1 |
|  | 9¢ | 50 | ×0.1^4 = 0.0 |
|  | 29¢ | 1 | ×0.1^24 = 0.0 |
|  | 44¢ | 1 | ×0.1^39 = 0.0 |
|  | 60¢ | 1 | ×0.1^55 = 0.0 |
|  | 98¢ | 132,784 | ×0.1^93 = 0.0 |
| | | **Σ** | **7.1** |

`yours 2.0 / Σ 7.1 = 28.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.1% = $1.76/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem`
2. `ussewc-usse-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-kamhar</code> SELL 286 @ 5¢ → $1.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1,048 (286 yours) | ×0.2^0 = 1,048.0 |
|  | 14¢ | 61 | ×0.2^9 = 0.0 |
|  | 19¢ | 31,724 | ×0.2^14 = 0.0 |
| | | **Σ** | **1,048.0** |

`yours 286.0 / Σ 1,048.0 = 27.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 27.3% = $1.01/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (819,587 resting) | ~54.7% | ~$41.06 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (41,297 resting) | ~99.5% | ~$24.88 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (26,966 resting) | ~60.6% | ~$15.14 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (66,373 resting) | ~16.8% | ~$12.57 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (202,046 resting) | ~11.9% | ~$8.92 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (556,769 resting) | ~12.8% | ~$3.21 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (301,997 resting) | ~39.6% | ~$2.48 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (553,954 resting) | ~7.7% | ~$1.93 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (780,961 resting) | ~2.3% | ~$1.69 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,241,612 resting) | ~25.2% | ~$1.57 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (288,275 resting) | ~1.9% | ~$1.42 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (77,097 resting) | ~22.1% | ~$1.38 |

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
| 2026-08-19 5:21 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 4:20 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 3:20 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 1:36 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 10:41 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:41 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:37 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:34 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:30 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:26 PM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
