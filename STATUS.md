# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-18 10:41 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$270.19/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `paccc-usho-midterms-2026-11-03-rep` — BUY at the best price, ~$28.22/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$16.49/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$16.35/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$270.19/day (~$11.26/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 82.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (502,170 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 57.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,875 resting ≥ 5,000 ✓) ≈ $4.17/day (event pool ÷ 12 markets) |
| `ewc-usp-2028-11-07-dwajoh` | SELL | 5.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~99.8% of ask side (56,145 resting ≥ 20,000 ✓) ≈ $3.70/day (event pool ÷ 27 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~98.9% of ask side (66,199 resting ≥ 2,000 ✓) ≈ $6.18/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 37.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~95.2% of bid side (400,602 resting ≥ 5,000 ✓) ≈ $3.97/day (event pool ÷ 12 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~93.8% of bid side (2,030 resting ≥ 2,000 ✓) ≈ $5.86/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~86.8% of bid side (4,294 resting ≥ 2,000 ✓) ≈ $5.42/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 0 | $25.00 | ✅ scoring — ~85.7% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $5.35/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~84.5% of bid side (2,013 resting ≥ 2,000 ✓) ≈ $5.28/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 10.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~84.1% of bid side (313,872 resting ≥ 5,000 ✓) ≈ $3.24/day (event pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 25.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~83.3% of bid side (96,514 resting ≥ 20,000 ✓) ≈ $4.90/day (event pool ÷ 17 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (196,042 resting ≥ 2,000 ✓) ≈ $5.20/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-markel` | SELL | 12.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~80.6% of ask side (20,108 resting ≥ 20,000 ✓) ≈ $4.74/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~76.6% of bid side (2,035 resting ≥ 2,000 ✓) ≈ $3.19/day (event pool ÷ 3 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 88 | 0 | $200.00 | ✅ scoring — ~75.5% of bid side (106,902 resting ≥ 20,000 ✓) ≈ $4.44/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | BUY | 23.0¢ | 46 | 0 | $200.00 | ✅ scoring — ~71.1% of bid side (221,876 resting ≥ 20,000 ✓) ≈ $4.18/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~70.3% of bid side (53,763 resting ≥ 5,000 ✓) ≈ $2.70/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (107,055 resting ≥ 2,000 ✓) ≈ $4.17/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 87.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~59.7% of ask side (2,560 resting ≥ 2,000 ✓) ≈ $3.73/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 9.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~54.0% of bid side (23,747 resting ≥ 5,000 ✓) ≈ $2.08/day (event pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 21.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~48.6% of bid side (203,854 resting ≥ 5,000 ✓) ≈ $1.87/day (event pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 20.0¢ | 5 | 1 | $100.00 | ✅ scoring — ~48.6% of bid side (203,854 resting ≥ 5,000 ✓) ≈ $1.87/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 87.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~48.5% of ask side (27,355 resting ≥ 2,000 ✓) ≈ $3.03/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 87.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~48.5% of ask side (27,355 resting ≥ 2,000 ✓) ≈ $3.03/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~46.9% of bid side (84,241 resting ≥ 20,000 ✓) ≈ $1.74/day (event pool ÷ 27 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 17.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~46.4% of bid side (54,681 resting ≥ 5,000 ✓) ≈ $1.79/day (event pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 9.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~44.3% of bid side (20,456 resting ≥ 20,000 ✓) ≈ $1.64/day (event pool ÷ 27 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 8.0¢ | 13 | 0 | $100.00 | ✅ scoring — ~40.7% of ask side (77,755 resting ≥ 5,000 ✓) ≈ $1.56/day (event pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~39.9% of bid side (31,223 resting ≥ 5,000 ✓) ≈ $9.97/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-tulgab` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~39.8% of ask side (70,930 resting ≥ 20,000 ✓) ≈ $1.47/day (event pool ÷ 27 markets) |
| …and 1777 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 5 @ 82¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 5 (5 yours) | ×0.1^0 = 5.0 |
|  | 74¢ | 152 | ×0.1^8 = 0.0 |
|  | 65¢ | 8 | ×0.1^17 = 0.0 |
|  | 60¢ | 1 | ×0.1^22 = 0.0 |
|  | 10¢ | 5 | ×0.1^72 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^80 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 1 @ 57¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 55¢ | 0 | ×0.2^2 = 0.0 |
|  | 42¢ | 50 | ×0.2^15 = 0.0 |
|  | 2¢ | 300,624 | ×0.2^55 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-dwajoh</code> SELL 1 @ 5¢ → $3.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 11¢ | 18 | ×0.2^6 = 0.0 |
|  | 12¢ | 15 | ×0.2^7 = 0.0 |
|  | 13¢ | 231 | ×0.2^8 = 0.0 |
|  | 14¢ | 10 | ×0.2^9 = 0.0 |
|  | 15¢ | 10 | ×0.2^10 = 0.0 |
|  | 16¢ | 10 | ×0.2^11 = 0.0 |
|  | 17¢ | 10 | ×0.2^12 = 0.0 |
|  | 18¢ | 10 | ×0.2^13 = 0.0 |
|  | 20¢ | 288 | ×0.2^15 = 0.0 |
| | … | +2 levels | 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 99.8% = $3.70/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh` ← this one
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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $6.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 10¢ | 2 | ×0.1^2 = 0.0 |
|  | 11¢ | 2 | ×0.1^3 = 0.0 |
|  | 12¢ | 1 | ×0.1^4 = 0.0 |
|  | 13¢ | 2 | ×0.1^5 = 0.0 |
|  | 14¢ | 2 | ×0.1^6 = 0.0 |
|  | 15¢ | 163 | ×0.1^7 = 0.0 |
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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 10 @ 12¢ → $5.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 11¢ | 5 | ×0.1^1 = 0.5 |
|  | 10¢ | 16 | ×0.1^2 = 0.2 |
|  | 1¢ | 1,999 | ×0.1^11 = 0.0 |
| | | **Σ** | **10.7** |

`yours 10.0 / Σ 10.7 = 93.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.8% = $5.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 2 @ 7¢ → $5.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 6¢ | 2 | ×0.1^1 = 0.2 |
|  | 5¢ | 7 | ×0.1^2 = 0.1 |
|  | 3¢ | 285 | ×0.1^4 = 0.0 |
|  | 2¢ | 200 | ×0.1^5 = 0.0 |
|  | 1¢ | 3,798 | ×0.1^6 = 0.0 |
| | | **Σ** | **2.3** |

`yours 2.0 / Σ 2.3 = 86.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 86.8% = $5.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 13 | ×0.1^0 = 13.0 |
| ▶ | 1¢ | 2,000 (1,799 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **213.0** |

`yours 179.9 / Σ 213.0 = 84.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 84.5% = $5.28/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 10¢ → $3.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 0 | ×0.2^1 = 0.0 |
|  | 3¢ | 13,320 | ×0.2^7 = 0.2 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 84.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 84.1% = $3.24/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 1 @ 25¢ → $4.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 24¢ | 1 | ×0.2^1 = 0.2 |
|  | 19¢ | 1 | ×0.2^6 = 0.0 |
|  | 17¢ | 62 | ×0.2^8 = 0.0 |
|  | 15¢ | 697 | ×0.2^10 = 0.0 |
|  | 10¢ | 45,443 | ×0.2^15 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 83.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 83.3% = $4.90/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> SELL 1 @ 12¢ → $4.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 13¢ | 1 | ×0.2^1 = 0.2 |
|  | 14¢ | 1 | ×0.2^2 = 0.0 |
|  | 25¢ | 14 | ×0.2^13 = 0.0 |
|  | 26¢ | 50 | ×0.2^14 = 0.0 |
|  | 45¢ | 63 | ×0.2^33 = 0.0 |
|  | 99¢ | 19,978 | ×0.2^87 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 80.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 80.6% = $4.74/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 88 @ 12¢ → $4.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 116 (88 yours) | ×0.2^0 = 116.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 8¢ | 6 | ×0.2^4 = 0.0 |
|  | 6¢ | 125 | ×0.2^6 = 0.0 |
|  | 4¢ | 30 | ×0.2^8 = 0.0 |
|  | 3¢ | 171 | ×0.2^9 = 0.0 |
|  | 2¢ | 86,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **116.5** |

`yours 88.0 / Σ 116.5 = 75.5%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 75.5% = $4.44/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> BUY 46 @ 23¢ → $4.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 23¢ | 63 (46 yours) | ×0.2^0 = 63.0 |
|  | 22¢ | 2 | ×0.2^1 = 0.4 |
|  | 21¢ | 24 | ×0.2^2 = 1.0 |
|  | 20¢ | 1 | ×0.2^3 = 0.0 |
|  | 19¢ | 8 | ×0.2^4 = 0.0 |
|  | 18¢ | 6 | ×0.2^5 = 0.0 |
|  | 17¢ | 112 | ×0.2^6 = 0.0 |
|  | 16¢ | 21,110 | ×0.2^7 = 0.3 |
| | | **Σ** | **64.7** |

`yours 46.0 / Σ 64.7 = 71.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 71.1% = $4.18/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 1 @ 18¢ → $2.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 17¢ | 1 | ×0.2^1 = 0.2 |
|  | 16¢ | 0 | ×0.2^2 = 0.0 |
|  | 14¢ | 0 | ×0.2^4 = 0.0 |
|  | 12¢ | 3,456 | ×0.2^6 = 0.2 |
|  | 3¢ | 105 | ×0.2^15 = 0.0 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **1.4** |

`yours 1.0 / Σ 1.4 = 70.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 70.3% = $2.70/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48` ← this one
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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 3 @ 95¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 4 (3 yours) | ×0.1^0 = 4.0 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 39¢ | 1 | ×0.1^56 = 0.0 |
|  | 9¢ | 1 | ×0.1^86 = 0.0 |
|  | 2¢ | 5,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **4.5** |

`yours 3.0 / Σ 4.5 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 1 @ 87¢ → $3.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 88¢ | 1 | ×0.1^1 = 0.1 |
|  | 89¢ | 2 | ×0.1^2 = 0.0 |
|  | 90¢ | 555 | ×0.1^3 = 0.6 |
|  | 92¢ | 2 | ×0.1^5 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^12 = 0.0 |
| | | **Σ** | **1.7** |

`yours 1.0 / Σ 1.7 = 59.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 59.7% = $3.73/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1 @ 9¢ → $2.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 3¢ | 13,300 | ×0.2^6 = 0.9 |
| | | **Σ** | **1.9** |

`yours 1.0 / Σ 1.9 = 54.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 54.0% = $2.08/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 21¢ → $1.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 20¢ | 5 | ×0.2^1 = 1.0 |
|  | 15¢ | 356 | ×0.2^6 = 0.0 |
|  | 14¢ | 2,859 | ×0.2^7 = 0.0 |
|  | 11¢ | 54 | ×0.2^10 = 0.0 |
|  | 10¢ | 70 | ×0.2^11 = 0.0 |
|  | 1¢ | 200,509 | ×0.2^20 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 48.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.6% = $1.87/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5 @ 20¢ → $1.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 20¢ | 5 (5 yours) | ×0.2^1 = 1.0 |
|  | 15¢ | 356 | ×0.2^6 = 0.0 |
|  | 14¢ | 2,859 | ×0.2^7 = 0.0 |
|  | 11¢ | 54 | ×0.2^10 = 0.0 |
|  | 10¢ | 70 | ×0.2^11 = 0.0 |
|  | 1¢ | 200,509 | ×0.2^20 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 48.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.6% = $1.87/day`  

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 2 @ 87¢ → $3.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 4 (2 yours) | ×0.1^0 = 4.0 |
|  | 88¢ | 1 | ×0.1^1 = 0.1 |
|  | 89¢ | 2 | ×0.1^2 = 0.0 |
|  | 90¢ | 1 | ×0.1^3 = 0.0 |
|  | 92¢ | 9 | ×0.1^5 = 0.0 |
|  | 97¢ | 5,348 | ×0.1^10 = 0.0 |
| | | **Σ** | **4.1** |

`yours 2.0 / Σ 4.1 = 48.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 48.5% = $3.03/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 2 @ 87¢ → $3.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 4 (2 yours) | ×0.1^0 = 4.0 |
|  | 88¢ | 1 | ×0.1^1 = 0.1 |
|  | 89¢ | 2 | ×0.1^2 = 0.0 |
|  | 90¢ | 1 | ×0.1^3 = 0.0 |
|  | 92¢ | 9 | ×0.1^5 = 0.0 |
|  | 97¢ | 5,348 | ×0.1^10 = 0.0 |
| | | **Σ** | **4.1** |

`yours 2.0 / Σ 4.1 = 48.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 48.5% = $3.03/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 8¢ → $1.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 3¢ | 30 | ×0.2^5 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 84,097 | ×0.2^7 = 1.1 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 46.9%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 46.9% = $1.74/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 1 @ 17¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 16¢ | 0 | ×0.2^1 = 0.0 |
|  | 15¢ | 0 | ×0.2^2 = 0.0 |
|  | 14¢ | 100 | ×0.2^3 = 0.8 |
|  | 12¢ | 333 | ×0.2^5 = 0.1 |
|  | 11¢ | 3,797 | ×0.2^6 = 0.2 |
|  | 2¢ | 50,250 | ×0.2^15 = 0.0 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 46.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 46.4% = $1.79/day`  

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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 50 @ 9¢ → $1.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 113 (50 yours) | ×0.2^0 = 112.8 |
|  | 1¢ | 20,343 | ×0.2^8 = 0.1 |
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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 13 @ 8¢ → $1.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 32 (13 yours) | ×0.2^0 = 32.0 |
|  | 15¢ | 562 | ×0.2^7 = 0.0 |
|  | 22¢ | 100 | ×0.2^14 = 0.0 |
|  | 24¢ | 50 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^89 = 0.0 |
| | | **Σ** | **32.0** |

`yours 13.0 / Σ 32.0 = 40.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.7% = $1.56/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> SELL 3 @ 6¢ → $1.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 7 (3 yours) | ×0.2^0 = 7.0 |
|  | 9¢ | 67 | ×0.2^3 = 0.5 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 20¢ | 287 | ×0.2^14 = 0.0 |
|  | 21¢ | 50 | ×0.2^15 = 0.0 |
|  | 25¢ | 50,266 | ×0.2^19 = 0.0 |
| | | **Σ** | **7.5** |

`yours 3.0 / Σ 7.5 = 39.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 39.8% = $1.47/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (820,166 resting) | ~37.6% | ~$28.22 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (26,101 resting) | ~66.0% | ~$16.49 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,472 resting) | ~65.4% | ~$16.35 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (66,184 resting) | ~17.1% | ~$12.81 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (89,033 resting) | ~48.3% | ~$3.02 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (285,175 resting) | ~3.1% | ~$2.31 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (286,232 resting) | ~2.8% | ~$2.13 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (634,548 resting) | ~6.8% | ~$1.70 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (780,756 resting) | ~2.2% | ~$1.69 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,242,555 resting) | ~25.8% | ~$1.61 |
| `ewc-usse-ak-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (374,784 resting) | ~23.3% | ~$1.46 |
| `ewc-usgub-ia-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (58,280 resting) | ~23.2% | ~$1.45 |

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
| 2026-08-18 10:41 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:41 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:37 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:34 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:30 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:23 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:19 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:15 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 9:12 PM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
