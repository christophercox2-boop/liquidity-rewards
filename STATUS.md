# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 6:27 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$137.55/day estimated (ceiling, not promise — details below)

**Earned:** $5,595.00 lifetime ($5,593.52 paid). Last three recorded days — 2026-08-19: **$0.60** · 2026-08-18: **$181.52** · 2026-08-17: **$295.29** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — SELL at the best price, ~$15.94/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$14.56/day), `ewc-usgub-ga-2026-11-03-rep` (~$10.98/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$137.55/day (~$5.73/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-ri-2026-11-03-kenblo` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.8% of ask side (2,150 resting ≥ 2,000 ✓) ≈ $4.16/day (event pool ÷ 3 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 14.0¢ | 14 | 0 | $200.00 | ✅ scoring — ~99.0% of bid side (93,037 resting ≥ 20,000 ✓) ≈ $5.82/day (event pool ÷ 17 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 1,925 | 0 | $25.00 | ✅ scoring — ~96.2% of bid side (2,001 resting ≥ 2,000 ✓) ≈ $6.01/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~94.0% of ask side (57,301 resting ≥ 20,000 ✓) ≈ $3.48/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~93.6% of bid side (50,355 resting ≥ 20,000 ✓) ≈ $3.47/day (event pool ÷ 27 markets) |
| `ussewc-usse-va-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 0 | $25.00 | ✅ scoring — ~85.7% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $5.35/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 37 | 1 | $200.00 | ✅ scoring — ~77.7% of ask side (44,699 resting ≥ 20,000 ✓) ≈ $5.55/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | SELL | 5.0¢ | 32 | 0 | $200.00 | ✅ scoring — ~62.7% of ask side (48,320 resting ≥ 20,000 ✓) ≈ $3.69/day (event pool ÷ 17 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~62.5% of ask side (65,577 resting ≥ 2,000 ✓) ≈ $3.91/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | SELL | 9.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~52.3% of ask side (71,476 resting ≥ 20,000 ✓) ≈ $1.94/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-thomas` | SELL | 3.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~49.9% of ask side (71,551 resting ≥ 20,000 ✓) ≈ $1.85/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 108 | 0 | $200.00 | ✅ scoring — ~46.7% of bid side (75,562 resting ≥ 20,000 ✓) ≈ $1.73/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 1 | $200.00 | ✅ scoring — ~44.6% of bid side (85,165 resting ≥ 20,000 ✓) ≈ $1.65/day (event pool ÷ 27 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~41.7% of bid side (23,290 resting ≥ 5,000 ✓) ≈ $10.43/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-tulgab` | BUY | 1.0¢ | 19,238 | 2 | $200.00 | ✅ scoring — ~40.5% of bid side (42,018 resting ≥ 20,000 ✓) ≈ $2.89/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-jonste` | SELL | 7.0¢ | 35 | 0 | $200.00 | ✅ scoring — ~40.2% of ask side (53,578 resting ≥ 20,000 ✓) ≈ $2.37/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | SELL | 93.0¢ | 9 | 0 | $25.00 | ✅ scoring — ~39.1% of ask side (2,014 resting ≥ 2,000 ✓) ≈ $2.45/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rondes` | SELL | 10.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~37.5% of ask side (65,456 resting ≥ 20,000 ✓) ≈ $1.39/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rondes` | SELL | 10.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~37.5% of ask side (65,456 resting ≥ 20,000 ✓) ≈ $1.39/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-tuccar` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~36.3% of ask side (55,904 resting ≥ 20,000 ✓) ≈ $1.35/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 9.0¢ | 1 | 2 | $200.00 | ✅ scoring — ~34.2% of bid side (43,364 resting ≥ 20,000 ✓) ≈ $2.01/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ct-2026-11-03-rep` | SELL | 3.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~33.3% of ask side (199,538 resting ≥ 2,000 ✓) ≈ $2.08/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | SELL | 95.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~31.7% of ask side (2,389 resting ≥ 2,000 ✓) ≈ $1.98/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-micoba` | BUY | 1.0¢ | 9,253 | 2 | $200.00 | ✅ scoring — ~30.7% of bid side (30,030 resting ≥ 20,000 ✓) ≈ $1.81/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 19,263 | 3 | $200.00 | ✅ scoring — ~28.8% of bid side (42,013 resting ≥ 20,000 ✓) ≈ $2.06/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 19,336 | 3 | $200.00 | ✅ scoring — ~28.6% of bid side (42,017 resting ≥ 20,000 ✓) ≈ $2.04/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 5.0¢ | 10 | 0 | $200.00 | ✅ scoring — ~28.6% of ask side (58,345 resting ≥ 20,000 ✓) ≈ $1.68/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-wesmoo` | SELL | 5.0¢ | 26 | 0 | $200.00 | ✅ scoring — ~27.9% of ask side (48,365 resting ≥ 20,000 ✓) ≈ $1.64/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-wesmoo` | SELL | 5.0¢ | 25 | 0 | $200.00 | ✅ scoring — ~26.9% of ask side (48,365 resting ≥ 20,000 ✓) ≈ $1.58/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-tedcru` | BUY | 1.0¢ | 19,349 | 2 | $200.00 | ✅ scoring — ~25.5% of bid side (72,019 resting ≥ 20,000 ✓) ≈ $1.82/day (event pool ÷ 14 markets) |
| …and 1078 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-ri-2026-11-03-kenblo</code> SELL 1 @ 5¢ → $4.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 8¢ | 2 | ×0.1^3 = 0.0 |
|  | 10¢ | 1 | ×0.1^5 = 0.0 |
|  | 12¢ | 7 | ×0.1^7 = 0.0 |
|  | 15¢ | 150 | ×0.1^10 = 0.0 |
|  | 99¢ | 1,989 | ×0.1^94 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 99.8% = $4.16/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo` ← this one
3. `usgubewc-usgub-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 14 @ 14¢ → $5.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 14 (14 yours) | ×0.2^0 = 14.3 |
|  | 12¢ | 3 | ×0.2^2 = 0.1 |
|  | 11¢ | 2 | ×0.2^3 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 8¢ | 6 | ×0.2^6 = 0.0 |
|  | 7¢ | 25 | ×0.2^7 = 0.0 |
|  | 6¢ | 112 | ×0.2^8 = 0.0 |
|  | 5¢ | 13 | ×0.2^9 = 0.0 |
|  | 4¢ | 6,250 | ×0.2^10 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^12 = 0.0 |
| | | **Σ** | **14.4** |

`yours 14.3 / Σ 14.4 = 99.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 99.0% = $5.82/day`  

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
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 1,925 @ 1¢ → $6.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,001 (1,925 yours) | ×0.1^0 = 2,001.0 |
| | | **Σ** | **2,001.0** |

`yours 1,925.0 / Σ 2,001.0 = 96.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 96.2% = $6.01/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 1 @ 6¢ → $3.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 1 | ×0.2^6 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 14¢ | 458 | ×0.2^8 = 0.0 |
|  | 15¢ | 36,415 | ×0.2^9 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 94.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 94.0% = $3.48/day`  

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
13. `ewc-usp-2028-11-07-jossha` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 144 (135 yours) | ×0.2^0 = 143.5 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **144.2** |

`yours 135.0 / Σ 144.2 = 93.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 93.6% = $3.47/day`  

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (1,799 yours) | ×0.1^0 = 2,100.0 |
| | | **Σ** | **2,100.0** |

`yours 1,799.0 / Σ 2,100.0 = 85.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 85.7% = $5.35/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 37 @ 4¢ → $5.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 4¢ | 42 (37 yours) | ×0.2^1 = 8.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 6 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **9.5** |

`yours 7.4 / Σ 9.5 = 77.7%`  
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
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> SELL 32 @ 5¢ → $3.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 51 (32 yours) | ×0.2^0 = 51.0 |
|  | 15¢ | 30,469 | ×0.2^10 = 0.0 |
| | | **Σ** | **51.0** |

`yours 32.0 / Σ 51.0 = 62.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 62.7% = $3.69/day`  

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 30 @ 2¢ → $3.91/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 48 (30 yours) | ×0.1^0 = 48.0 |
|  | 5¢ | 4 | ×0.1^3 = 0.0 |
|  | 9¢ | 50 | ×0.1^7 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^96 = 0.0 |
| | | **Σ** | **48.0** |

`yours 30.0 / Σ 48.0 = 62.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 62.5% = $3.91/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> SELL 1 @ 9¢ → $1.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 10¢ | 3 | ×0.2^1 = 0.6 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 3 | ×0.2^3 = 0.0 |
|  | 13¢ | 154 | ×0.2^4 = 0.2 |
|  | 15¢ | 14 | ×0.2^6 = 0.0 |
|  | 22¢ | 51,050 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.9** |

`yours 1.0 / Σ 1.9 = 52.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 52.3% = $1.94/day`  

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
<details><summary><code>ewc-usp-2028-11-07-thomas</code> SELL 3 @ 3¢ → $1.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 6 (3 yours) | ×0.2^0 = 6.0 |
|  | 7¢ | 1 | ×0.2^4 = 0.0 |
|  | 8¢ | 17 | ×0.2^5 = 0.0 |
|  | 20¢ | 206 | ×0.2^17 = 0.0 |
|  | 21¢ | 51,071 | ×0.2^18 = 0.0 |
| | | **Σ** | **6.0** |

`yours 3.0 / Σ 6.0 = 49.9%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 49.9% = $1.85/day`  

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
23. `ewc-usp-2028-11-07-thomas` ← this one
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 108 @ 5¢ → $1.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 110 (108 yours) | ×0.2^0 = 110.5 |
|  | 4¢ | 4 | ×0.2^1 = 0.8 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 75,443 | ×0.2^4 = 120.7 |
| | | **Σ** | **232.1** |

`yours 108.5 / Σ 232.1 = 46.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 46.7% = $1.73/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 5¢ | 158 (135 yours) | ×0.2^1 = 31.6 |
|  | 4¢ | 18 | ×0.2^2 = 0.7 |
|  | 2¢ | 13 | ×0.2^4 = 0.0 |
|  | 1¢ | 84,975 | ×0.2^5 = 27.2 |
| | | **Σ** | **60.5** |

`yours 27.0 / Σ 60.5 = 44.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 44.6% = $1.65/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $10.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,366 (1,000 yours) | ×0.2^0 = 2,365.5 |
|  | 8¢ | 150 | ×0.2^1 = 30.0 |
|  | 5¢ | 501 | ×0.2^4 = 0.8 |
|  | 3¢ | 74 | ×0.2^6 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^7 = 0.3 |
| | | **Σ** | **2,396.6** |

`yours 1,000.0 / Σ 2,396.6 = 41.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 41.7% = $10.43/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-tulgab</code> BUY 19,238 @ 1¢ → $2.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 230 | ×0.2^0 = 230.3 |
| ▶ | 1¢ | 41,788 (19,238 yours) | ×0.2^2 = 1,671.5 |
| | | **Σ** | **1,901.9** |

`yours 769.5 / Σ 1,901.9 = 40.5%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 40.5% = $2.89/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonste</code> SELL 35 @ 7¢ → $2.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 87 (35 yours) | ×0.2^0 = 87.0 |
|  | 13¢ | 4 | ×0.2^6 = 0.0 |
|  | 14¢ | 7 | ×0.2^7 = 0.0 |
|  | 19¢ | 4 | ×0.2^12 = 0.0 |
|  | 21¢ | 147 | ×0.2^14 = 0.0 |
|  | 22¢ | 50,529 | ×0.2^15 = 0.0 |
| | | **Σ** | **87.0** |

`yours 35.0 / Σ 87.0 = 40.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 40.2% = $2.37/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste` ← this one
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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> SELL 9 @ 93¢ → $2.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 23 (9 yours) | ×0.1^0 = 23.0 |
|  | 99¢ | 1,991 | ×0.1^6 = 0.0 |
| | | **Σ** | **23.0** |

`yours 9.0 / Σ 23.0 = 39.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 39.1% = $2.45/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rondes</code> SELL 1 @ 10¢ → $1.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 12¢ | 7 | ×0.2^2 = 0.3 |
|  | 16¢ | 31 | ×0.2^6 = 0.0 |
|  | 17¢ | 30,917 | ×0.2^7 = 0.4 |
| | | **Σ** | **2.7** |

`yours 1.0 / Σ 2.7 = 37.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 37.5% = $1.39/day`  

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
21. `ewc-usp-2028-11-07-rondes` ← this one
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rondes</code> SELL 1 @ 10¢ → $1.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 12¢ | 7 | ×0.2^2 = 0.3 |
|  | 16¢ | 31 | ×0.2^6 = 0.0 |
|  | 17¢ | 30,917 | ×0.2^7 = 0.4 |
| | | **Σ** | **2.7** |

`yours 1.0 / Σ 2.7 = 37.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 37.5% = $1.39/day`  

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
21. `ewc-usp-2028-11-07-rondes` ← this one
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tuccar</code> SELL 3 @ 6¢ → $1.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 8 (3 yours) | ×0.2^0 = 8.1 |
|  | 7¢ | 1 | ×0.2^1 = 0.2 |
|  | 14¢ | 1 | ×0.2^8 = 0.0 |
|  | 21¢ | 50 | ×0.2^15 = 0.0 |
|  | 26¢ | 21,289 | ×0.2^20 = 0.0 |
| | | **Σ** | **8.3** |

`yours 3.0 / Σ 8.3 = 36.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 36.3% = $1.35/day`  

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
24. `ewc-usp-2028-11-07-tuccar` ← this one
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 9¢ → $2.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 0 | ×0.2^0 = 0.1 |
| ▶ | 9¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 6¢ | 1 | ×0.2^5 = 0.0 |
|  | 5¢ | 64 | ×0.2^6 = 0.0 |
|  | 4¢ | 226 | ×0.2^7 = 0.0 |
|  | 3¢ | 110 | ×0.2^8 = 0.0 |
|  | 2¢ | 22,500 | ×0.2^9 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 34.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 34.2% = $2.01/day`  

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
<details><summary><code>usgubewc-usgub-ct-2026-11-03-rep</code> SELL 1 @ 3¢ → $2.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 3 (1 yours) | ×0.1^0 = 3.0 |
|  | 6¢ | 1 | ×0.1^3 = 0.0 |
|  | 9¢ | 1 | ×0.1^6 = 0.0 |
|  | 10¢ | 50 | ×0.1^7 = 0.0 |
|  | 12¢ | 83 | ×0.1^9 = 0.0 |
|  | 98¢ | 199,175 | ×0.1^95 = 0.0 |
| | | **Σ** | **3.0** |

`yours 1.0 / Σ 3.0 = 33.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 33.3% = $2.08/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem`
2. `usgubewc-usgub-ct-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> SELL 10 @ 95¢ → $1.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 27 (10 yours) | ×0.1^0 = 27.0 |
|  | 97¢ | 438 | ×0.1^2 = 4.4 |
|  | 99¢ | 1,924 | ×0.1^4 = 0.2 |
| | | **Σ** | **31.6** |

`yours 10.0 / Σ 31.6 = 31.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 31.7% = $1.98/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-micoba</code> BUY 9,253 @ 1¢ → $1.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 4 | ×0.2^0 = 4.0 |
|  | 2¢ | 3 | ×0.2^1 = 0.6 |
| ▶ | 1¢ | 30,023 (9,253 yours) | ×0.2^2 = 1,200.9 |
| | | **Σ** | **1,205.5** |

`yours 370.1 / Σ 1,205.5 = 30.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 30.7% = $1.81/day`  

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
12. `enwc-uspres-nom-dem-2028-micoba` ← this one
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 19,263 @ 1¢ → $2.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 200 | ×0.2^0 = 200.0 |
| ▶ | 1¢ | 41,813 (19,263 yours) | ×0.2^3 = 334.5 |
| | | **Σ** | **534.5** |

`yours 154.1 / Σ 534.5 = 28.8%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 28.8% = $2.06/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 19,336 @ 1¢ → $2.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 206 | ×0.2^0 = 206.0 |
| ▶ | 1¢ | 41,811 (19,336 yours) | ×0.2^3 = 334.5 |
| | | **Σ** | **540.5** |

`yours 154.7 / Σ 540.5 = 28.6%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 28.6% = $2.04/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 10 @ 5¢ → $1.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 35 (10 yours) | ×0.2^0 = 35.0 |
|  | 13¢ | 4 | ×0.2^8 = 0.0 |
|  | 18¢ | 3 | ×0.2^13 = 0.0 |
|  | 19¢ | 3 | ×0.2^14 = 0.0 |
|  | 20¢ | 40,501 | ×0.2^15 = 0.0 |
| | | **Σ** | **35.0** |

`yours 10.0 / Σ 35.0 = 28.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 28.6% = $1.68/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal` ← this one
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
<details><summary><code>enwc-uspres-nom-dem-2028-wesmoo</code> SELL 26 @ 5¢ → $1.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 92 (26 yours) | ×0.2^0 = 92.0 |
|  | 7¢ | 16 | ×0.2^2 = 0.7 |
|  | 11¢ | 4 | ×0.2^6 = 0.0 |
|  | 12¢ | 30,453 | ×0.2^7 = 0.4 |
| | | **Σ** | **93.0** |

`yours 26.0 / Σ 93.0 = 27.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 27.9% = $1.64/day`  

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
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-wesmoo</code> SELL 25 @ 5¢ → $1.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 92 (25 yours) | ×0.2^0 = 92.0 |
|  | 7¢ | 16 | ×0.2^2 = 0.7 |
|  | 11¢ | 4 | ×0.2^6 = 0.0 |
|  | 12¢ | 30,453 | ×0.2^7 = 0.4 |
| | | **Σ** | **93.0** |

`yours 25.0 / Σ 93.0 = 26.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 26.9% = $1.58/day`  

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
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-tedcru</code> BUY 19,349 @ 1¢ → $1.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 120 | ×0.2^0 = 120.3 |
|  | 2¢ | 250 | ×0.2^1 = 50.0 |
| ▶ | 1¢ | 71,649 (19,349 yours) | ×0.2^2 = 2,866.0 |
| | | **Σ** | **3,036.3** |

`yours 774.0 / Σ 3,036.3 = 25.5%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 25.5% = $1.82/day`  

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
10. `enwc-uspres-nom-rep-2028-tedcru` ← this one
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-19 | ~$4.52 | $0.60 | 13% |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (70,853 resting) | ~21.3% | ~$15.94 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (11,820 resting) | ~19.4% | ~$14.56 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (11,003 resting) | ~14.6% | ~$10.98 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (830,860 resting) | ~14.6% | ~$10.92 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (25,596 resting) | ~14.2% | ~$10.67 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (11,590 resting) | ~11.6% | ~$8.68 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (17,642 resting) | ~8.7% | ~$6.50 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (71,095 resting) | ~7.7% | ~$5.79 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (612,774 resting) | ~7.4% | ~$5.55 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (4,172 resting) | ~59.6% | ~$3.72 |
| `ewc-usse-nc-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (8,133 resting) | ~11.3% | ~$2.81 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (24,374 resting) | ~10.3% | ~$2.57 |

## Totals

| | Amount |
|---|---:|
| Paid | $5,593.52 |
| Skipped | $1.48 |
| **Total earned** | **$5,595.00** |

3188 reward rows · 48 days with rewards · 586 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-19 | $0.60 | `█` |
| 2026-08-18 | $181.52 | `███` |
| 2026-08-17 | $295.29 | `████` |
| 2026-08-16 | $197.03 | `███` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $4,131.68 | `████████████████████` |
| 2026-07 | $1,463.32 | `███████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $190.39 |
| `apdc-alito-2026-12-31` | $120.07 |
| `ewc-usp-party-2028-11-07-rep` | $110.48 |
| `ewc-usp-party-2028-11-07-dem` | $102.28 |
| `opdc-mcconnell-resign-2026-11-02` | $79.42 |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | $66.06 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $63.61 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $62.40 |
| `enwc-uspres-nom-rep-2028-rondes` | $49.72 |
| `enwc-uspres-nom-dem-2028-stasmi` | $47.79 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.60 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.51 |
| `enwc-uspres-nom-dem-2028-jamtal` | $40.91 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-20 6:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 5:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 4:10 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:42 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 11:41 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 10:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 9:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 8:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 7:30 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 6:13 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
