# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-18 5:30 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$216.38/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$21.54/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$18.61/day), `ewc-usgub-ga-2026-11-03-dem` (~$10.52/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$216.38/day (~$9.02/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-id-2026-11-03-dem` | SELL | 21.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (208,290 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tn-2026-11-03-rep` | BUY | 82.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,042 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | BUY | 21.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,207 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (66,134 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 12.0¢ | 45 | 0 | $200.00 | ✅ scoring — ~100.0% of bid side (63,676 resting ≥ 20,000 ✓) ≈ $7.14/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 25.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~99.9% of bid side (81,193 resting ≥ 20,000 ✓) ≈ $5.88/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 20.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (200,942 resting ≥ 5,000 ✓) ≈ $3.84/day (event pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-markel` | SELL | 11.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~98.0% of ask side (30,310 resting ≥ 20,000 ✓) ≈ $5.77/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | SELL | 7.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~94.3% of ask side (33,686 resting ≥ 20,000 ✓) ≈ $5.55/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-jonoss` | BUY | 15.0¢ | 100 | 0 | $200.00 | ✅ scoring — ~93.4% of bid side (55,432 resting ≥ 20,000 ✓) ≈ $3.46/day (event pool ÷ 27 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 10.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~93.1% of bid side (305,512 resting ≥ 5,000 ✓) ≈ $3.58/day (event pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 8.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~91.3% of bid side (24,000 resting ≥ 20,000 ✓) ≈ $3.38/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~82.5% of bid side (500,285 resting ≥ 2,000 ✓) ≈ $5.16/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~78.3% of bid side (2,029 resting ≥ 2,000 ✓) ≈ $4.89/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~76.6% of bid side (2,035 resting ≥ 2,000 ✓) ≈ $3.19/day (event pool ÷ 3 markets) |
| `ewc-usp-2028-11-07-gavnew` | SELL | 13.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~71.3% of ask side (50,910 resting ≥ 20,000 ✓) ≈ $2.64/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-aleocc` | BUY | 21.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~62.4% of bid side (71,007 resting ≥ 20,000 ✓) ≈ $3.67/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 87.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~60.0% of ask side (27,351 resting ≥ 2,000 ✓) ≈ $3.75/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 6.0¢ | 5 | 2 | $100.00 | ✅ scoring — ~55.2% of bid side (10,454 resting ≥ 5,000 ✓) ≈ $2.12/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 0 | $25.00 | ✅ scoring — ~51.9% of bid side (3,465 resting ≥ 2,000 ✓) ≈ $3.24/day (event pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | BUY | 83.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (500,307 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | BUY | 83.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (500,307 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 12.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~43.1% of bid side (30,219 resting ≥ 20,000 ✓) ≈ $1.60/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 12.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~43.1% of bid side (30,219 resting ≥ 20,000 ✓) ≈ $1.60/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | BUY | 21.0¢ | 45 | 2 | $200.00 | ✅ scoring — ~42.0% of bid side (168,625 resting ≥ 20,000 ✓) ≈ $2.47/day (event pool ÷ 17 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 95.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~40.5% of bid side (500,478 resting ≥ 2,000 ✓) ≈ $2.53/day (event pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~40.0% of bid side (600,528 resting ≥ 2,000 ✓) ≈ $2.50/day (event pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~40.0% of bid side (600,528 resting ≥ 2,000 ✓) ≈ $2.50/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 87.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~40.0% of ask side (27,351 resting ≥ 2,000 ✓) ≈ $2.50/day (event pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~39.9% of bid side (31,241 resting ≥ 5,000 ✓) ≈ $9.97/day (event pool ÷ 2 markets) |
| …and 1260 more | | | | | | |

**Tap an order for its book window and the math:**

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
<details><summary><code>usgubewc-usgub-tn-2026-11-03-rep</code> BUY 3 @ 82¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 64¢ | 39 | ×0.1^18 = 0.0 |
|  | 32¢ | 1 | ×0.1^50 = 0.0 |
|  | 10¢ | 5 | ×0.1^72 = 0.0 |
|  | 1¢ | 1,994 | ×0.1^81 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem`
2. `usgubewc-usgub-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> BUY 3 @ 21¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 15¢ | 4 | ×0.1^6 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^19 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 15¢ | 157 | ×0.1^7 = 0.0 |
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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 45 @ 12¢ → $7.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 45 (45 yours) | ×0.2^0 = 45.0 |
|  | 2¢ | 12,972 | ×0.2^10 = 0.0 |
|  | 1¢ | 50,659 | ×0.2^11 = 0.0 |
| | | **Σ** | **45.0** |

`yours 45.0 / Σ 45.0 = 100.0%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 100.0% = $7.14/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 1 @ 25¢ → $5.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 18¢ | 1 | ×0.2^7 = 0.0 |
|  | 17¢ | 62 | ×0.2^8 = 0.0 |
|  | 15¢ | 3,363 | ×0.2^10 = 0.0 |
|  | 13¢ | 6,153 | ×0.2^12 = 0.0 |
|  | 10¢ | 21,250 | ×0.2^15 = 0.0 |
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
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> SELL 20 @ 11¢ → $5.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 12¢ | 2 | ×0.2^1 = 0.4 |
|  | 26¢ | 113 | ×0.2^15 = 0.0 |
|  | 45¢ | 50 | ×0.2^34 = 0.0 |
|  | 99¢ | 30,125 | ×0.2^88 = 0.0 |
| | | **Σ** | **20.4** |

`yours 20.0 / Σ 20.4 = 98.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 98.0% = $5.77/day`  

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
11. `enwc-uspres-nom-dem-2028-markel` ← this one
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> SELL 1 @ 7¢ → $5.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 11¢ | 38 | ×0.2^4 = 0.1 |
|  | 24¢ | 17,165 | ×0.2^17 = 0.0 |
|  | 30¢ | 17 | ×0.2^23 = 0.0 |
|  | 33¢ | 13,714 | ×0.2^26 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 94.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 94.3% = $5.55/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jonoss</code> BUY 100 @ 15¢ → $3.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 105 (100 yours) | ×0.2^0 = 104.7 |
|  | 13¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 74 | ×0.2^3 = 0.6 |
|  | 11¢ | 920 | ×0.2^4 = 1.5 |
|  | 9¢ | 2,777 | ×0.2^6 = 0.2 |
|  | 8¢ | 5 | ×0.2^7 = 0.0 |
|  | 2¢ | 1,000 | ×0.2^13 = 0.0 |
|  | 1¢ | 50,550 | ×0.2^14 = 0.0 |
| | | **Σ** | **107.0** |

`yours 100.0 / Σ 107.0 = 93.4%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 93.4% = $3.46/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 10¢ → $3.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 0 | ×0.2^1 = 0.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 4¢ | 5 | ×0.2^6 = 0.0 |
|  | 3¢ | 2 | ×0.2^7 = 0.0 |
|  | 2¢ | 5,200 | ×0.2^8 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 93.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 93.1% = $3.58/day`  

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
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 3 @ 8¢ → $3.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 3 (3 yours) | ×0.2^0 = 3.2 |
|  | 2¢ | 3 | ×0.2^6 = 0.0 |
|  | 1¢ | 23,994 | ×0.2^7 = 0.3 |
| | | **Σ** | **3.5** |

`yours 3.2 / Σ 3.5 = 91.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 91.3% = $3.38/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus` ← this one
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
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 3 @ 95¢ → $5.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 94¢ | 4 | ×0.1^1 = 0.4 |
|  | 93¢ | 23 | ×0.1^2 = 0.2 |
|  | 91¢ | 50 | ×0.1^4 = 0.0 |
|  | 15¢ | 5 | ×0.1^80 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.6** |

`yours 3.0 / Σ 3.6 = 82.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 82.5% = $5.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

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
<details><summary><code>ewc-usp-2028-11-07-gavnew</code> SELL 3 @ 13¢ → $2.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 4 (3 yours) | ×0.2^0 = 4.0 |
|  | 14¢ | 1 | ×0.2^1 = 0.2 |
|  | 21¢ | 1 | ×0.2^8 = 0.0 |
|  | 22¢ | 16,158 | ×0.2^9 = 0.0 |
|  | 25¢ | 757 | ×0.2^12 = 0.0 |
|  | 34¢ | 13,739 | ×0.2^21 = 0.0 |
| | | **Σ** | **4.2** |

`yours 3.0 / Σ 4.2 = 71.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 71.3% = $2.64/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew` ← this one
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
<details><summary><code>enwc-uspres-nom-dem-2028-aleocc</code> BUY 20 @ 21¢ → $3.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 18¢ | 612 | ×0.2^3 = 4.9 |
|  | 17¢ | 3,822 | ×0.2^4 = 6.1 |
|  | 13¢ | 16,250 | ×0.2^8 = 0.0 |
| | | **Σ** | **32.1** |

`yours 20.0 / Σ 32.1 = 62.4%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 62.4% = $3.67/day`  

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
|  | 92¢ | 8 | ×0.1^5 = 0.0 |
|  | 97¢ | 5,348 | ×0.1^10 = 0.0 |
| | | **Σ** | **5.0** |

`yours 3.0 / Σ 5.0 = 60.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.0% = $3.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 5 @ 6¢ → $2.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 0 | ×0.2^1 = 0.0 |
| ▶ | 6¢ | 5 (5 yours) | ×0.2^2 = 0.2 |
|  | 4¢ | 3 | ×0.2^4 = 0.0 |
|  | 1¢ | 10,446 | ×0.2^7 = 0.1 |
| | | **Σ** | **0.4** |

`yours 0.2 / Σ 0.4 = 55.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.2% = $2.12/day`  

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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $3.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,465 (1,799 yours) | ×0.1^0 = 3,465.0 |
| | | **Σ** | **3,465.0** |

`yours 1,799.0 / Σ 3,465.0 = 51.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 51.9% = $3.24/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> BUY 3 @ 83¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 83¢ | 6 (3 yours) | ×0.1^0 = 6.0 |
|  | 67¢ | 1 | ×0.1^16 = 0.0 |
|  | 65¢ | 100 | ×0.1^18 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^81 = 0.0 |
| | | **Σ** | **6.0** |

`yours 3.0 / Σ 6.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> BUY 3 @ 83¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 83¢ | 6 (3 yours) | ×0.1^0 = 6.0 |
|  | 67¢ | 1 | ×0.1^16 = 0.0 |
|  | 65¢ | 100 | ×0.1^18 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^81 = 0.0 |
| | | **Σ** | **6.0** |

`yours 3.0 / Σ 6.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 12¢ → $1.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 11¢ | 1 | ×0.2^1 = 0.2 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 9¢ | 5 | ×0.2^3 = 0.0 |
|  | 2¢ | 112 | ×0.2^10 = 0.0 |
|  | 1¢ | 30,097 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 43.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 43.1% = $1.60/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 12¢ → $1.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 11¢ | 1 | ×0.2^1 = 0.2 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 9¢ | 5 | ×0.2^3 = 0.0 |
|  | 2¢ | 112 | ×0.2^10 = 0.0 |
|  | 1¢ | 30,097 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 43.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 43.1% = $1.60/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> BUY 45 @ 21¢ → $2.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 1 | ×0.2^0 = 1.0 |
|  | 22¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 21¢ | 69 (45 yours) | ×0.2^2 = 2.8 |
|  | 20¢ | 1 | ×0.2^3 = 0.0 |
|  | 19¢ | 23 | ×0.2^4 = 0.0 |
|  | 18¢ | 207 | ×0.2^5 = 0.1 |
|  | 17¢ | 97 | ×0.2^6 = 0.0 |
|  | 16¢ | 16,110 | ×0.2^7 = 0.2 |
|  | 15¢ | 1,666 | ×0.2^8 = 0.0 |
|  | 2¢ | 250 | ×0.2^21 = 0.0 |
| | … | +1 levels | 0.0 |
| | | **Σ** | **4.3** |

`yours 1.8 / Σ 4.3 = 42.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 42.0% = $2.47/day`  

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
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 35 @ 95¢ → $2.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 86 (35 yours) | ×0.1^0 = 86.0 |
|  | 94¢ | 4 | ×0.1^1 = 0.4 |
|  | 58¢ | 1 | ×0.1^37 = 0.0 |
|  | 12¢ | 187 | ×0.1^83 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **86.4** |

`yours 35.0 / Σ 86.4 = 40.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 40.5% = $2.53/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> BUY 3 @ 94¢ → $2.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 6 (3 yours) | ×0.1^0 = 6.0 |
|  | 92¢ | 150 | ×0.1^2 = 1.5 |
|  | 46¢ | 147 | ×0.1^48 = 0.0 |
|  | 40¢ | 25 | ×0.1^54 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **7.5** |

`yours 3.0 / Σ 7.5 = 40.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 40.0% = $2.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> BUY 3 @ 94¢ → $2.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 6 (3 yours) | ×0.1^0 = 6.0 |
|  | 92¢ | 150 | ×0.1^2 = 1.5 |
|  | 46¢ | 147 | ×0.1^48 = 0.0 |
|  | 40¢ | 25 | ×0.1^54 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **7.5** |

`yours 3.0 / Σ 7.5 = 40.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 40.0% = $2.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 2 @ 87¢ → $2.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 5 (2 yours) | ×0.1^0 = 5.0 |
|  | 92¢ | 8 | ×0.1^5 = 0.0 |
|  | 97¢ | 5,348 | ×0.1^10 = 0.0 |
| | | **Σ** | **5.0** |

`yours 2.0 / Σ 5.0 = 40.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 40.0% = $2.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $9.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,399 (1,000 yours) | ×0.2^0 = 2,399.0 |
|  | 7¢ | 1,408 | ×0.2^2 = 56.3 |
|  | 6¢ | 6,628 | ×0.2^3 = 53.0 |
| | | **Σ** | **2,508.4** |

`yours 1,000.0 / Σ 2,508.4 = 39.9%`  
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
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (25,856 resting) | ~86.2% | ~$21.54 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,033 resting) | ~74.4% | ~$18.61 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (64,867 resting) | ~14.0% | ~$10.52 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,925 resting) | ~6.9% | ~$5.19 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (74,580 resting) | ~68.9% | ~$4.31 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (65,109 resting) | ~7.2% | ~$1.79 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (288,877 resting) | ~2.2% | ~$1.65 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (632,147 resting) | ~6.6% | ~$1.64 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (69,279 resting) | ~1.8% | ~$1.37 |
| `ewc-usse-ak-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (377,291 resting) | ~21.5% | ~$1.34 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,244,542 resting) | ~20.6% | ~$1.29 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,401 resting) | ~1.7% | ~$1.24 |

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
| 2026-08-18 5:30 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 3:09 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 2:59 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 1:58 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 1:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 12:44 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 12:34 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 11:57 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 10:56 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:32 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
