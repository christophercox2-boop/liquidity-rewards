# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-19 8:33 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$446.13/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `paccc-usho-midterms-2026-11-03-rep` — BUY at the best price, ~$31.68/day for 200 contracts. Runners-up: `ewc-usse-tx-2026-11-03-rep` (~$5.32/day), `ewc-usse-mi-2026-11-03-rep` (~$4.21/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$446.13/day (~$18.59/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-49` | SELL | 21.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,878 resting ≥ 5,000 ✓) ≈ $3.85/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | SELL | 19.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (141,839 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (68,979 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 14.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (37,155 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (70,482 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-kamhar` | SELL | 5.0¢ | 286 | 0 | $200.00 | ✅ scoring — ~98.6% of ask side (67,104 resting ≥ 20,000 ✓) ≈ $3.65/day (event pool ÷ 27 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 38 | 0 | $100.00 | ✅ scoring — ~98.5% of bid side (54,798 resting ≥ 5,000 ✓) ≈ $3.79/day (event pool ÷ 13 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 87.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~98.0% of ask side (2,099 resting ≥ 2,000 ✓) ≈ $6.13/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 10.0¢ | 112 | 0 | $200.00 | ✅ scoring — ~97.2% of bid side (98,181 resting ≥ 20,000 ✓) ≈ $5.72/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-tulgab` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~96.8% of ask side (70,837 resting ≥ 20,000 ✓) ≈ $3.59/day (event pool ÷ 27 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 37.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~95.2% of bid side (400,552 resting ≥ 5,000 ✓) ≈ $3.97/day (event pool ÷ 12 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~94.7% of ask side (66,145 resting ≥ 2,000 ✓) ≈ $5.92/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 15.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~93.5% of bid side (805,593 resting ≥ 5,000 ✓) ≈ $3.90/day (event pool ÷ 12 markets) |
| `ussewc-usse-ma-2026-11-03-rep` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.7% of ask side (65,488 resting ≥ 2,000 ✓) ≈ $5.67/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~89.6% of bid side (50,361 resting ≥ 20,000 ✓) ≈ $3.32/day (event pool ÷ 27 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 63.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~89.3% of bid side (400,535 resting ≥ 5,000 ✓) ≈ $3.72/day (event pool ÷ 12 markets) |
| `ussewc-usse-de-2026-11-03-rep` | BUY | 1.0¢ | 1,798 | 1 | $25.00 | ✅ scoring — ~88.6% of bid side (2,002 resting ≥ 2,000 ✓) ≈ $5.54/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 120 | 0 | $200.00 | ✅ scoring — ~77.6% of bid side (20,573 resting ≥ 20,000 ✓) ≈ $2.87/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 7.0¢ | 83 | 0 | $200.00 | ✅ scoring — ~73.8% of bid side (36,181 resting ≥ 20,000 ✓) ≈ $2.74/day (event pool ÷ 27 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~73.2% of bid side (2,033 resting ≥ 2,000 ✓) ≈ $4.58/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 55 | 0 | $200.00 | ✅ scoring — ~66.6% of bid side (96,868 resting ≥ 20,000 ✓) ≈ $3.91/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 5.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~66.0% of ask side (208,294 resting ≥ 2,000 ✓) ≈ $4.13/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | SELL | 9.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~62.0% of ask side (71,371 resting ≥ 20,000 ✓) ≈ $2.30/day (event pool ÷ 27 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~61.9% of bid side (4,090 resting ≥ 2,000 ✓) ≈ $3.87/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 5.0¢ | 79 | 0 | $100.00 | ✅ scoring — ~57.2% of ask side (77,485 resting ≥ 5,000 ✓) ≈ $2.20/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 7.0¢ | 24 | 0 | $25.00 | ✅ scoring — ~56.9% of ask side (65,519 resting ≥ 2,000 ✓) ≈ $3.55/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-rokha` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~55.3% of ask side (38,713 resting ≥ 20,000 ✓) ≈ $3.25/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 11.0¢ | 86 | 0 | $200.00 | ✅ scoring — ~55.1% of ask side (44,751 resting ≥ 20,000 ✓) ≈ $3.94/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 12.0¢ | 42 | 0 | $200.00 | ✅ scoring — ~53.8% of ask side (38,956 resting ≥ 20,000 ✓) ≈ $3.16/day (event pool ÷ 17 markets) |
| `ussewc-usse-il-2026-11-03-rep` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~49.9% of ask side (330,183 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| …and 2917 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 1 @ 21¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 66¢ | 134 | ×0.2^45 = 0.0 |
|  | 67¢ | 51 | ×0.2^46 = 0.0 |
|  | 68¢ | 1 | ×0.2^47 = 0.0 |
|  | 69¢ | 1 | ×0.2^48 = 0.0 |
|  | 70¢ | 1 | ×0.2^49 = 0.0 |
|  | 71¢ | 1 | ×0.2^50 = 0.0 |
|  | 72¢ | 1 | ×0.2^51 = 0.0 |
|  | 73¢ | 1 | ×0.2^52 = 0.0 |
|  | 74¢ | 1 | ×0.2^53 = 0.0 |
| | … | +23 levels | 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> SELL 1 @ 19¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 29¢ | 1 | ×0.1^10 = 0.0 |
|  | 66¢ | 1 | ×0.1^47 = 0.0 |
|  | 85¢ | 6,000 | ×0.1^66 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> SELL 1 @ 5¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 12¢ | 1 | ×0.1^7 = 0.0 |
|  | 23¢ | 1 | ×0.1^18 = 0.0 |
|  | 27¢ | 1 | ×0.1^22 = 0.0 |
|  | 48¢ | 3,000 | ×0.1^43 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 3 @ 14¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 3 (3 yours) | ×0.1^0 = 3.4 |
|  | 10¢ | 1 | ×0.1^4 = 0.0 |
|  | 8¢ | 10 | ×0.1^6 = 0.0 |
|  | 7¢ | 144 | ×0.1^7 = 0.0 |
|  | 2¢ | 15,000 | ×0.1^12 = 0.0 |
| | | **Σ** | **3.4** |

`yours 3.4 / Σ 3.4 = 100.0%`  
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
|  | 15¢ | 2 | ×0.1^7 = 0.0 |
|  | 17¢ | 3 | ×0.1^9 = 0.0 |
|  | 32¢ | 5,000 | ×0.1^24 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-kamhar</code> SELL 286 @ 5¢ → $3.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 290 (286 yours) | ×0.2^0 = 290.0 |
|  | 14¢ | 61 | ×0.2^9 = 0.0 |
|  | 18¢ | 111 | ×0.2^13 = 0.0 |
|  | 19¢ | 31,724 | ×0.2^14 = 0.0 |
| | | **Σ** | **290.0** |

`yours 286.0 / Σ 290.0 = 98.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 98.6% = $3.65/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 38 @ 15¢ → $3.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 38 (38 yours) | ×0.2^0 = 38.4 |
|  | 14¢ | 0 | ×0.2^1 = 0.0 |
|  | 13¢ | 3 | ×0.2^2 = 0.1 |
|  | 12¢ | 22 | ×0.2^3 = 0.2 |
|  | 11¢ | 164 | ×0.2^4 = 0.3 |
|  | 10¢ | 1 | ×0.2^5 = 0.0 |
|  | 9¢ | 1 | ×0.2^6 = 0.0 |
|  | 8¢ | 540 | ×0.2^7 = 0.0 |
|  | 7¢ | 3,572 | ×0.2^8 = 0.0 |
|  | 6¢ | 1 | ×0.2^9 = 0.0 |
| | … | +4 levels | 0.0 |
| | | **Σ** | **39.0** |

`yours 38.4 / Σ 39.0 = 98.5%`  
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
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 1 @ 87¢ → $6.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 89¢ | 2 | ×0.1^2 = 0.0 |
|  | 92¢ | 2 | ×0.1^5 = 0.0 |
|  | 94¢ | 1 | ×0.1^7 = 0.0 |
|  | 98¢ | 65 | ×0.1^11 = 0.0 |
|  | 99¢ | 2,028 | ×0.1^12 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.0% = $6.13/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 112 @ 10¢ → $5.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 114 (112 yours) | ×0.2^0 = 114.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 6¢ | 255 | ×0.2^4 = 0.4 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 4¢ | 11,360 | ×0.2^6 = 0.7 |
|  | 2¢ | 16,000 | ×0.2^8 = 0.0 |
| | | **Σ** | **115.2** |

`yours 112.0 / Σ 115.2 = 97.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 97.2% = $5.72/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> SELL 3 @ 6¢ → $3.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 3 (3 yours) | ×0.2^0 = 3.0 |
|  | 9¢ | 12 | ×0.2^3 = 0.1 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 20¢ | 303 | ×0.2^14 = 0.0 |
|  | 25¢ | 50,266 | ×0.2^19 = 0.0 |
| | | **Σ** | **3.1** |

`yours 3.0 / Σ 3.1 = 96.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 96.8% = $3.59/day`  

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
25. `ewc-usp-2028-11-07-tulgab` ← this one
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

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
|  | 11¢ | 2 | ×0.1^3 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 43 @ 15¢ → $3.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 46 (43 yours) | ×0.2^0 = 46.2 |
|  | 2¢ | 5,347 | ×0.2^13 = 0.0 |
| | | **Σ** | **46.3** |

`yours 43.2 / Σ 46.3 = 93.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 93.5% = $3.90/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220` ← this one
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>ussewc-usse-ma-2026-11-03-rep</code> SELL 1 @ 5¢ → $5.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 6¢ | 1 | ×0.1^1 = 0.1 |
|  | 8¢ | 2 | ×0.1^3 = 0.0 |
|  | 9¢ | 3 | ×0.1^4 = 0.0 |
|  | 14¢ | 1 | ×0.1^9 = 0.0 |
|  | 22¢ | 1 | ×0.1^17 = 0.0 |
|  | 98¢ | 65,254 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.7% = $5.67/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem`
2. `ussewc-usse-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 150 (135 yours) | ×0.2^0 = 150.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **150.7** |

`yours 135.0 / Σ 150.7 = 89.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 89.6% = $3.32/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 1 @ 63¢ → $3.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 63¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 56¢ | 25 | ×0.2^7 = 0.0 |
|  | 49¢ | 0 | ×0.2^14 = 0.0 |
|  | 3¢ | 59 | ×0.2^60 = 0.0 |
|  | 2¢ | 400,250 | ×0.2^61 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 89.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 89.3% = $3.72/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195` ← this one
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>ussewc-usse-de-2026-11-03-rep</code> BUY 1,798 @ 1¢ → $5.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 3 | ×0.1^0 = 3.0 |
| ▶ | 1¢ | 1,999 (1,798 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **202.9** |

`yours 179.8 / Σ 202.9 = 88.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 88.6% = $5.54/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-de-2026-11-03-dem`
2. `ussewc-usse-de-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 120 @ 5¢ → $2.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 121 (120 yours) | ×0.2^0 = 121.0 |
|  | 4¢ | 4 | ×0.2^1 = 0.8 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 20,443 | ×0.2^4 = 32.7 |
| | | **Σ** | **154.6** |

`yours 120.0 / Σ 154.6 = 77.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 77.6% = $2.87/day`  

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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 83 @ 7¢ → $2.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 98 (83 yours) | ×0.2^0 = 98.2 |
|  | 6¢ | 27 | ×0.2^1 = 5.4 |
|  | 5¢ | 31 | ×0.2^2 = 1.2 |
|  | 3¢ | 250 | ×0.2^4 = 0.4 |
|  | 2¢ | 22,500 | ×0.2^5 = 7.2 |
| | | **Σ** | **112.4** |

`yours 83.0 / Σ 112.4 = 73.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 73.8% = $2.74/day`  

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
18. `ewc-usp-2028-11-07-petbut` ← this one
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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 10 @ 12¢ → $4.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 13 (10 yours) | ×0.1^0 = 13.0 |
|  | 11¢ | 5 | ×0.1^1 = 0.5 |
|  | 10¢ | 16 | ×0.1^2 = 0.2 |
|  | 1¢ | 1,999 | ×0.1^11 = 0.0 |
| | | **Σ** | **13.7** |

`yours 10.0 / Σ 13.7 = 73.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 73.2% = $4.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 55 @ 12¢ → $3.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 82 (55 yours) | ×0.2^0 = 82.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 8¢ | 6 | ×0.2^4 = 0.0 |
|  | 7¢ | 30 | ×0.2^5 = 0.0 |
|  | 6¢ | 125 | ×0.2^6 = 0.0 |
|  | 5¢ | 10,000 | ×0.2^7 = 0.1 |
|  | 3¢ | 171 | ×0.2^9 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **82.6** |

`yours 55.0 / Σ 82.6 = 66.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 66.6% = $3.91/day`  

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
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 2 @ 5¢ → $4.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 3 (2 yours) | ×0.1^0 = 3.0 |
|  | 7¢ | 3 | ×0.1^2 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.0** |

`yours 2.0 / Σ 3.0 = 66.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.0% = $4.13/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> SELL 1 @ 9¢ → $2.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 10¢ | 2 | ×0.2^1 = 0.4 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 1 | ×0.2^3 = 0.0 |
|  | 13¢ | 102 | ×0.2^4 = 0.2 |
|  | 15¢ | 14 | ×0.2^6 = 0.0 |
|  | 22¢ | 51,000 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.6** |

`yours 1.0 / Σ 1.6 = 62.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 62.0% = $2.30/day`  

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
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 2 @ 7¢ → $3.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 3 (2 yours) | ×0.1^0 = 3.0 |
|  | 6¢ | 2 | ×0.1^1 = 0.2 |
|  | 5¢ | 2 | ×0.1^2 = 0.0 |
|  | 3¢ | 42 | ×0.1^4 = 0.0 |
|  | 2¢ | 243 | ×0.1^5 = 0.0 |
|  | 1¢ | 3,798 | ×0.1^6 = 0.0 |
| | | **Σ** | **3.2** |

`yours 2.0 / Σ 3.2 = 61.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.9% = $3.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 79 @ 5¢ → $2.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 79 (79 yours) | ×0.2^0 = 79.0 |
|  | 6¢ | 295 | ×0.2^1 = 59.0 |
|  | 15¢ | 100 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^92 = 0.0 |
| | | **Σ** | **138.0** |

`yours 79.0 / Σ 138.0 = 57.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 57.2% = $2.20/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46` ← this one
2. `scc-senate-gop-2026-11-03-47`
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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 24 @ 7¢ → $3.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 42 (24 yours) | ×0.1^0 = 42.0 |
|  | 8¢ | 2 | ×0.1^1 = 0.2 |
|  | 98¢ | 65,250 | ×0.1^91 = 0.0 |
| | | **Σ** | **42.2** |

`yours 24.0 / Σ 42.2 = 56.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 56.9% = $3.55/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-rokha</code> SELL 3 @ 6¢ → $3.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 5 (3 yours) | ×0.2^0 = 5.0 |
|  | 7¢ | 2 | ×0.2^1 = 0.4 |
|  | 9¢ | 1 | ×0.2^3 = 0.0 |
|  | 10¢ | 11 | ×0.2^4 = 0.0 |
|  | 15¢ | 30 | ×0.2^9 = 0.0 |
|  | 16¢ | 20,914 | ×0.2^10 = 0.0 |
| | | **Σ** | **5.4** |

`yours 3.0 / Σ 5.4 = 55.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 55.3% = $3.25/day`  

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
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha` ← this one
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 86 @ 11¢ → $3.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 89 (86 yours) | ×0.2^0 = 89.0 |
|  | 12¢ | 3 | ×0.2^1 = 0.6 |
|  | 13¢ | 6 | ×0.2^2 = 0.2 |
|  | 14¢ | 65 | ×0.2^3 = 0.5 |
|  | 15¢ | 40,995 | ×0.2^4 = 65.6 |
| | | **Σ** | **156.0** |

`yours 86.0 / Σ 156.0 = 55.1%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 55.1% = $3.94/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> SELL 42 @ 12¢ → $3.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 70 (42 yours) | ×0.2^0 = 70.0 |
|  | 13¢ | 40 | ×0.2^1 = 8.0 |
|  | 16¢ | 13 | ×0.2^4 = 0.0 |
|  | 17¢ | 62 | ×0.2^5 = 0.0 |
|  | 19¢ | 4 | ×0.2^7 = 0.0 |
|  | 26¢ | 21,017 | ×0.2^14 = 0.0 |
| | | **Σ** | **78.1** |

`yours 42.0 / Σ 78.1 = 53.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 53.8% = $3.16/day`  

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
<details><summary><code>ussewc-usse-il-2026-11-03-rep</code> SELL 1 @ 6¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 9¢ | 3 | ×0.1^3 = 0.0 |
|  | 22¢ | 1 | ×0.1^16 = 0.0 |
|  | 24¢ | 1 | ×0.1^18 = 0.0 |
|  | 29¢ | 1 | ×0.1^23 = 0.0 |
|  | 44¢ | 1 | ×0.1^38 = 0.0 |
|  | 60¢ | 1 | ×0.1^54 = 0.0 |
|  | 76¢ | 1 | ×0.1^70 = 0.0 |
|  | 98¢ | 132,784 | ×0.1^92 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 49.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.9% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem`
2. `ussewc-usse-il-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (821,975 resting) | ~42.2% | ~$31.68 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (918,406 resting) | ~7.1% | ~$5.32 |
| `ewc-usse-mi-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (625,516 resting) | ~67.3% | ~$4.21 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (26,603 resting) | ~5.1% | ~$3.85 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,058,162 resting) | ~4.0% | ~$3.03 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (629,746 resting) | ~11.9% | ~$2.97 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (33,820 resting) | ~10.3% | ~$2.58 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (95,883 resting) | ~3.0% | ~$2.23 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (779,761 resting) | ~2.7% | ~$2.05 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,215,304 resting) | ~29.0% | ~$1.81 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (90,052 resting) | ~27.8% | ~$1.74 |
| `ewc-usgub-mi-2026-11-03-dem` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (90,015 resting) | ~34.9% | ~$1.46 |

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
| 2026-08-19 8:33 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 7:01 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 3:37 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 2:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 11:59 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 10:58 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 9:44 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 8:44 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 7:22 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 6:21 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
