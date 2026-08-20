# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 5:27 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$166.76/day estimated (ceiling, not promise — details below)

**Earned:** $5,595.00 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-19: **$0.60** · 2026-08-18: **$181.52** · 2026-08-17: **$295.29** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$43.54/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$19.44/day), `ewc-usgub-ca-2026-11-03-xavbec` (~$10.46/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$166.76/day (~$6.95/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~94.2% of ask side (57,300 resting ≥ 20,000 ✓) ≈ $3.49/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | SELL | 5.0¢ | 32 | 0 | $200.00 | ✅ scoring — ~94.1% of ask side (48,303 resting ≥ 20,000 ✓) ≈ $5.54/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~93.6% of bid side (50,355 resting ≥ 20,000 ✓) ≈ $3.47/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-ri-2026-11-03-kenblo` | SELL | 4.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.9% of ask side (2,150 resting ≥ 2,000 ✓) ≈ $3.79/day (event pool ÷ 3 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 14.0¢ | 14 | 0 | $200.00 | ✅ scoring — ~88.9% of bid side (93,028 resting ≥ 20,000 ✓) ≈ $5.23/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 37 | 0 | $200.00 | ✅ scoring — ~86.8% of ask side (44,696 resting ≥ 20,000 ✓) ≈ $6.20/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (65,530 resting ≥ 2,000 ✓) ≈ $5.20/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,700 | 1 | $25.00 | ✅ scoring — ~78.0% of bid side (2,107 resting ≥ 2,000 ✓) ≈ $3.25/day (event pool ÷ 3 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | SELL | 95.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~68.1% of ask side (3,261 resting ≥ 2,000 ✓) ≈ $4.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~62.5% of ask side (65,577 resting ≥ 2,000 ✓) ≈ $3.91/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jonste` | SELL | 7.0¢ | 35 | 0 | $200.00 | ✅ scoring — ~60.3% of ask side (53,529 resting ≥ 20,000 ✓) ≈ $3.55/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 7.0¢ | 83 | 0 | $200.00 | ✅ scoring — ~58.4% of bid side (64,510 resting ≥ 20,000 ✓) ≈ $2.16/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-tulgab` | BUY | 1.0¢ | 19,238 | 2 | $200.00 | ✅ scoring — ~58.2% of bid side (29,919 resting ≥ 20,000 ✓) ≈ $4.16/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 5.0¢ | 10 | 0 | $200.00 | ✅ scoring — ~50.0% of ask side (58,328 resting ≥ 20,000 ✓) ≈ $2.94/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 119 | 0 | $200.00 | ✅ scoring — ~49.2% of bid side (75,572 resting ≥ 20,000 ✓) ≈ $1.82/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-thomas` | SELL | 3.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~42.8% of ask side (71,552 resting ≥ 20,000 ✓) ≈ $1.59/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 19,263 | 3 | $200.00 | ✅ scoring — ~42.3% of bid side (29,939 resting ≥ 20,000 ✓) ≈ $3.02/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 19,336 | 3 | $200.00 | ✅ scoring — ~41.8% of bid side (29,943 resting ≥ 20,000 ✓) ≈ $2.98/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-elomus` | SELL | 5.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~41.7% of ask side (51,589 resting ≥ 20,000 ✓) ≈ $1.54/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 9.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~41.1% of bid side (20,490 resting ≥ 20,000 ✓) ≈ $1.52/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-wesmoo` | SELL | 5.0¢ | 26 | 0 | $200.00 | ✅ scoring — ~40.0% of ask side (48,337 resting ≥ 20,000 ✓) ≈ $2.35/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | SELL | 93.0¢ | 9 | 0 | $25.00 | ✅ scoring — ~39.1% of ask side (2,014 resting ≥ 2,000 ✓) ≈ $2.45/day (event pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~39.0% of bid side (24,765 resting ≥ 5,000 ✓) ≈ $9.76/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-wesmoo` | SELL | 5.0¢ | 25 | 0 | $200.00 | ✅ scoring — ~38.4% of ask side (48,337 resting ≥ 20,000 ✓) ≈ $2.26/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-wesmoo` | SELL | 3.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~38.1% of ask side (62,066 resting ≥ 20,000 ✓) ≈ $1.41/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 12.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~37.2% of ask side (38,819 resting ≥ 20,000 ✓) ≈ $2.19/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-tuccar` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~36.3% of ask side (55,877 resting ≥ 20,000 ✓) ≈ $1.35/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 10.0¢ | 1 | 1 | $200.00 | ✅ scoring — ~35.4% of bid side (93,364 resting ≥ 20,000 ✓) ≈ $2.08/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~31.2% of bid side (85,299 resting ≥ 20,000 ✓) ≈ $1.16/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~31.2% of bid side (85,299 resting ≥ 20,000 ✓) ≈ $1.16/day (event pool ÷ 27 markets) |
| …and 1694 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 1 @ 6¢ → $3.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 1 | ×0.2^6 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 14¢ | 458 | ×0.2^8 = 0.0 |
|  | 15¢ | 36,415 | ×0.2^9 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 94.2%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 94.2% = $3.49/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> SELL 32 @ 5¢ → $5.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 34 (32 yours) | ×0.2^0 = 34.0 |
|  | 15¢ | 30,469 | ×0.2^10 = 0.0 |
| | | **Σ** | **34.0** |

`yours 32.0 / Σ 34.0 = 94.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 94.1% = $5.54/day`  

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
<details><summary><code>usgubewc-usgub-ri-2026-11-03-kenblo</code> SELL 1 @ 4¢ → $3.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 5¢ | 1 | ×0.1^1 = 0.1 |
|  | 8¢ | 2 | ×0.1^4 = 0.0 |
|  | 12¢ | 7 | ×0.1^8 = 0.0 |
|  | 15¢ | 150 | ×0.1^11 = 0.0 |
|  | 99¢ | 1,989 | ×0.1^95 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.9%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 90.9% = $3.79/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo` ← this one
3. `usgubewc-usgub-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 14 @ 14¢ → $5.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 16 (14 yours) | ×0.2^0 = 15.9 |
|  | 12¢ | 3 | ×0.2^2 = 0.1 |
|  | 11¢ | 2 | ×0.2^3 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 8¢ | 6 | ×0.2^6 = 0.0 |
|  | 7¢ | 25 | ×0.2^7 = 0.0 |
|  | 6¢ | 112 | ×0.2^8 = 0.0 |
|  | 5¢ | 13 | ×0.2^9 = 0.0 |
|  | 4¢ | 6,250 | ×0.2^10 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^12 = 0.0 |
| | | **Σ** | **16.1** |

`yours 14.3 / Σ 16.1 = 88.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 88.9% = $5.23/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 37 @ 4¢ → $6.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 42 (37 yours) | ×0.2^0 = 42.0 |
|  | 5¢ | 3 | ×0.2^1 = 0.6 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 3 | ×0.2^8 = 0.0 |
|  | 13¢ | 4 | ×0.2^9 = 0.0 |
|  | 14¢ | 5 | ×0.2^10 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^11 = 0.0 |
| | | **Σ** | **42.6** |

`yours 37.0 / Σ 42.6 = 86.8%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 86.8% = $6.20/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 1 @ 7¢ → $5.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 8¢ | 2 | ×0.1^1 = 0.2 |
|  | 10¢ | 1 | ×0.1^3 = 0.0 |
|  | 16¢ | 50 | ×0.1^9 = 0.0 |
|  | 25¢ | 1 | ×0.1^18 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^91 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> BUY 1,700 @ 1¢ → $3.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 8 | ×0.1^0 = 8.0 |
| ▶ | 1¢ | 2,099 (1,700 yours) | ×0.1^1 = 209.9 |
| | | **Σ** | **217.9** |

`yours 170.0 / Σ 217.9 = 78.0%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 78.0% = $3.25/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> SELL 10 @ 95¢ → $4.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 97¢ | 441 | ×0.1^2 = 4.4 |
|  | 99¢ | 2,810 | ×0.1^4 = 0.3 |
| | | **Σ** | **14.7** |

`yours 10.0 / Σ 14.7 = 68.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 68.1% = $4.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonste</code> SELL 35 @ 7¢ → $3.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 58 (35 yours) | ×0.2^0 = 58.0 |
|  | 13¢ | 4 | ×0.2^6 = 0.0 |
|  | 14¢ | 7 | ×0.2^7 = 0.0 |
|  | 19¢ | 4 | ×0.2^12 = 0.0 |
|  | 21¢ | 127 | ×0.2^14 = 0.0 |
|  | 22¢ | 50,529 | ×0.2^15 = 0.0 |
| | | **Σ** | **58.0** |

`yours 35.0 / Σ 58.0 = 60.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 60.3% = $3.55/day`  

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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 83 @ 7¢ → $2.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 95 (83 yours) | ×0.2^0 = 95.4 |
|  | 6¢ | 27 | ×0.2^1 = 5.4 |
|  | 5¢ | 31 | ×0.2^2 = 1.2 |
|  | 3¢ | 18,582 | ×0.2^4 = 29.7 |
|  | 2¢ | 32,500 | ×0.2^5 = 10.4 |
| | | **Σ** | **142.2** |

`yours 83.0 / Σ 142.2 = 58.4%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 58.4% = $2.16/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-tulgab</code> BUY 19,238 @ 1¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 131 | ×0.2^0 = 131.3 |
| ▶ | 1¢ | 29,788 (19,238 yours) | ×0.2^2 = 1,191.5 |
| | | **Σ** | **1,322.9** |

`yours 769.5 / Σ 1,322.9 = 58.2%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 58.2% = $4.16/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 10 @ 5¢ → $2.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 20 (10 yours) | ×0.2^0 = 20.0 |
|  | 13¢ | 4 | ×0.2^8 = 0.0 |
|  | 18¢ | 3 | ×0.2^13 = 0.0 |
|  | 20¢ | 40,501 | ×0.2^15 = 0.0 |
| | | **Σ** | **20.0** |

`yours 10.0 / Σ 20.0 = 50.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 50.0% = $2.94/day`  

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
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 119 @ 5¢ → $1.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 120 (119 yours) | ×0.2^0 = 120.0 |
|  | 4¢ | 4 | ×0.2^1 = 0.8 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 75,443 | ×0.2^4 = 120.7 |
| | | **Σ** | **241.6** |

`yours 119.0 / Σ 241.6 = 49.2%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 49.2% = $1.82/day`  

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
<details><summary><code>ewc-usp-2028-11-07-thomas</code> SELL 3 @ 3¢ → $1.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 7 (3 yours) | ×0.2^0 = 7.0 |
|  | 7¢ | 1 | ×0.2^4 = 0.0 |
|  | 8¢ | 17 | ×0.2^5 = 0.0 |
|  | 20¢ | 206 | ×0.2^17 = 0.0 |
|  | 21¢ | 51,071 | ×0.2^18 = 0.0 |
| | | **Σ** | **7.0** |

`yours 3.0 / Σ 7.0 = 42.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 42.8% = $1.59/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 19,263 @ 1¢ → $3.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 126 | ×0.2^0 = 125.8 |
| ▶ | 1¢ | 29,813 (19,263 yours) | ×0.2^3 = 238.5 |
| | | **Σ** | **364.3** |

`yours 154.1 / Σ 364.3 = 42.3%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 42.3% = $3.02/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 19,336 @ 1¢ → $2.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 132 | ×0.2^0 = 131.8 |
| ▶ | 1¢ | 29,811 (19,336 yours) | ×0.2^3 = 238.5 |
| | | **Σ** | **370.2** |

`yours 154.7 / Σ 370.2 = 41.8%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 41.8% = $2.98/day`  

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
<details><summary><code>ewc-usp-2028-11-07-elomus</code> SELL 3 @ 5¢ → $1.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 7 (3 yours) | ×0.2^0 = 7.0 |
|  | 6¢ | 1 | ×0.2^1 = 0.2 |
|  | 10¢ | 2 | ×0.2^5 = 0.0 |
|  | 12¢ | 3 | ×0.2^7 = 0.0 |
|  | 14¢ | 1 | ×0.2^9 = 0.0 |
|  | 16¢ | 4 | ×0.2^11 = 0.0 |
|  | 17¢ | 275 | ×0.2^12 = 0.0 |
|  | 20¢ | 31,021 | ×0.2^15 = 0.0 |
| | | **Σ** | **7.2** |

`yours 3.0 / Σ 7.2 = 41.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 41.7% = $1.54/day`  

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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 50 @ 9¢ → $1.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 122 (50 yours) | ×0.2^0 = 121.5 |
|  | 1¢ | 20,368 | ×0.2^8 = 0.1 |
| | | **Σ** | **121.6** |

`yours 50.0 / Σ 121.6 = 41.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 41.1% = $1.52/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-wesmoo</code> SELL 26 @ 5¢ → $2.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 64 (26 yours) | ×0.2^0 = 64.0 |
|  | 7¢ | 16 | ×0.2^2 = 0.7 |
|  | 11¢ | 4 | ×0.2^6 = 0.0 |
|  | 12¢ | 30,453 | ×0.2^7 = 0.4 |
| | | **Σ** | **65.0** |

`yours 26.0 / Σ 65.0 = 40.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 40.0% = $2.35/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $9.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,475 (1,000 yours) | ×0.2^0 = 2,474.8 |
|  | 8¢ | 150 | ×0.2^1 = 30.0 |
|  | 7¢ | 1,390 | ×0.2^2 = 55.6 |
|  | 5¢ | 501 | ×0.2^4 = 0.8 |
|  | 3¢ | 50 | ×0.2^6 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^7 = 0.3 |
| | | **Σ** | **2,561.5** |

`yours 1,000.0 / Σ 2,561.5 = 39.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 39.0% = $9.76/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-wesmoo</code> SELL 25 @ 5¢ → $2.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 64 (25 yours) | ×0.2^0 = 64.0 |
|  | 7¢ | 16 | ×0.2^2 = 0.7 |
|  | 11¢ | 4 | ×0.2^6 = 0.0 |
|  | 12¢ | 30,453 | ×0.2^7 = 0.4 |
| | | **Σ** | **65.0** |

`yours 25.0 / Σ 65.0 = 38.4%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 38.4% = $2.26/day`  

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
<details><summary><code>ewc-usp-2028-11-07-wesmoo</code> SELL 1 @ 3¢ → $1.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 4¢ | 3 | ×0.2^1 = 0.6 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 7¢ | 635 | ×0.2^4 = 1.0 |
|  | 8¢ | 1 | ×0.2^5 = 0.0 |
|  | 9¢ | 3 | ×0.2^6 = 0.0 |
|  | 13¢ | 101 | ×0.2^10 = 0.0 |
|  | 19¢ | 41,021 | ×0.2^16 = 0.0 |
| | | **Σ** | **2.6** |

`yours 1.0 / Σ 2.6 = 38.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 38.1% = $1.41/day`  

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
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> SELL 3 @ 12¢ → $2.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 8 (3 yours) | ×0.2^0 = 8.0 |
|  | 14¢ | 1 | ×0.2^2 = 0.0 |
|  | 16¢ | 16 | ×0.2^4 = 0.0 |
|  | 19¢ | 4 | ×0.2^7 = 0.0 |
|  | 26¢ | 21,040 | ×0.2^14 = 0.0 |
| | | **Σ** | **8.1** |

`yours 3.0 / Σ 8.1 = 37.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 37.2% = $2.19/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tuccar</code> SELL 3 @ 6¢ → $1.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 8 (3 yours) | ×0.2^0 = 8.1 |
|  | 7¢ | 1 | ×0.2^1 = 0.2 |
|  | 14¢ | 1 | ×0.2^8 = 0.0 |
|  | 21¢ | 50 | ×0.2^15 = 0.0 |
|  | 26¢ | 21,262 | ×0.2^20 = 0.0 |
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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 10¢ → $2.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 0 | ×0.2^0 = 0.3 |
| ▶ | 10¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
|  | 6¢ | 1 | ×0.2^5 = 0.0 |
|  | 5¢ | 64 | ×0.2^6 = 0.0 |
|  | 4¢ | 226 | ×0.2^7 = 0.0 |
|  | 3¢ | 110 | ×0.2^8 = 0.0 |
|  | 2¢ | 72,500 | ×0.2^9 = 0.0 |
| | | **Σ** | **0.6** |

`yours 0.2 / Σ 0.6 = 35.4%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 35.4% = $2.08/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 293 (135 yours) | ×0.2^0 = 292.9 |
|  | 4¢ | 18 | ×0.2^1 = 3.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
|  | 1¢ | 84,975 | ×0.2^4 = 136.0 |
| | | **Σ** | **432.6** |

`yours 135.0 / Σ 432.6 = 31.2%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 31.2% = $1.16/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 293 (135 yours) | ×0.2^0 = 292.9 |
|  | 4¢ | 18 | ×0.2^1 = 3.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
|  | 1¢ | 84,975 | ×0.2^4 = 136.0 |
| | | **Σ** | **432.6** |

`yours 135.0 / Σ 432.6 = 31.2%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 31.2% = $1.16/day`  

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

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-19 | ~$4.53 | $0.60 | 13% |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,027 resting) | ~58.1% | ~$43.54 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,833 resting) | ~77.8% | ~$19.44 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (24,635 resting) | ~13.9% | ~$10.46 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (150,577 resting) | ~13.7% | ~$10.31 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (926,204 resting) | ~11.0% | ~$8.28 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (49,284 resting) | ~10.0% | ~$2.50 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (631,029 resting) | ~7.2% | ~$1.79 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (690,768 resting) | ~2.2% | ~$1.63 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (83,853 resting) | ~2.0% | ~$1.53 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (150,186 resting) | ~2.0% | ~$1.52 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (75,281 resting) | ~21.8% | ~$1.36 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (82,866 resting) | ~21.3% | ~$1.33 |

## Totals

| | Amount |
|---|---:|
| Paid | $4,919.08 |
| Pending | $674.51 |
| Skipped | $1.41 |
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
| 2026-08-20 5:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 4:10 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:42 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 11:41 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 10:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 9:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 8:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 7:30 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 6:13 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 4:57 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
