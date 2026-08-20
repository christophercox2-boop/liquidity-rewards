# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 7:28 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$56.34/day estimated (ceiling, not promise — details below)

**Earned:** $5,595.00 lifetime ($5,593.52 paid). Last three recorded days — 2026-08-19: **$0.60** · 2026-08-18: **$181.52** · 2026-08-17: **$295.29** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$22.48/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$11.51/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$11.24/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$56.34/day (~$2.35/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 92.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,576 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~87.6% of bid side (50,404 resting ≥ 20,000 ✓) ≈ $3.24/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~73.8% of ask side (57,334 resting ≥ 20,000 ✓) ≈ $2.73/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 37 | 1 | $200.00 | ✅ scoring — ~70.3% of ask side (44,703 resting ≥ 20,000 ✓) ≈ $5.02/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-thomas` | BUY | 1.0¢ | 19,311 | 3 | $200.00 | ✅ scoring — ~54.6% of bid side (30,004 resting ≥ 20,000 ✓) ≈ $3.90/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 9.0¢ | 20 | 2 | $200.00 | ✅ scoring — ~46.5% of bid side (40,884 resting ≥ 20,000 ✓) ≈ $2.74/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~42.5% of bid side (85,184 resting ≥ 20,000 ✓) ≈ $1.57/day (event pool ÷ 27 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~40.5% of ask side (65,603 resting ≥ 2,000 ✓) ≈ $2.53/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 19,263 | 3 | $200.00 | ✅ scoring — ~26.4% of bid side (42,062 resting ≥ 20,000 ✓) ≈ $1.89/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | SELL | 95.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~26.3% of ask side (4,551 resting ≥ 2,000 ✓) ≈ $1.64/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 19,336 | 3 | $200.00 | ✅ scoring — ~26.2% of bid side (42,066 resting ≥ 20,000 ✓) ≈ $1.87/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~24.6% of ask side (57,334 resting ≥ 20,000 ✓) ≈ $0.91/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-rokha` | SELL | 10.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~24.0% of ask side (39,699 resting ≥ 20,000 ✓) ≈ $1.41/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-jdvan` | BUY | 50.0¢ | 70 | 1 | $200.00 | ✅ scoring — ~20.4% of bid side (73,664 resting ≥ 20,000 ✓) ≈ $1.46/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,693 | 0 | $25.00 | ✅ scoring — ~14.1% of bid side (11,999 resting ≥ 2,000 ✓) ≈ $0.88/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 9.0¢ | 50 | 1 | $200.00 | ✅ scoring — ~13.7% of bid side (80,253 resting ≥ 20,000 ✓) ≈ $0.51/day (event pool ÷ 27 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | SELL | 2.0¢ | 85 | 0 | $25.00 | ✅ scoring — ~13.1% of ask side (308,964 resting ≥ 2,000 ✓) ≈ $0.82/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 90.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~11.0% of bid side (500,957 resting ≥ 2,000 ✓) ≈ $0.69/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-tuccar` | BUY | 4.0¢ | 200 | 1 | $200.00 | ✅ scoring — ~10.1% of bid side (78,469 resting ≥ 20,000 ✓) ≈ $0.38/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 1.0¢ | 19,484 | 4 | $200.00 | ✅ scoring — ~9.8% of bid side (85,184 resting ≥ 20,000 ✓) ≈ $0.36/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 7.0¢ | 100 | 2 | $200.00 | ✅ scoring — ~9.8% of bid side (51,323 resting ≥ 20,000 ✓) ≈ $0.36/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 3.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~9.5% of ask side (44,703 resting ≥ 20,000 ✓) ≈ $0.68/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 5 | 1 | $200.00 | ✅ scoring — ~9.5% of ask side (44,703 resting ≥ 20,000 ✓) ≈ $0.68/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 87.0¢ | 0 | 1 | $25.00 | ✅ scoring — ~9.1% of bid side (500,352 resting ≥ 2,000 ✓) ≈ $0.57/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-vivram` | BUY | 4.0¢ | 100 | 1 | $200.00 | ✅ scoring — ~8.7% of bid side (20,923 resting ≥ 20,000 ✓) ≈ $0.62/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 4.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~8.6% of bid side (42,062 resting ≥ 20,000 ✓) ≈ $0.61/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 4.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~8.5% of bid side (42,066 resting ≥ 20,000 ✓) ≈ $0.61/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-jonoss` | BUY | 18.0¢ | 50 | 1 | $200.00 | ✅ scoring — ~7.7% of bid side (202,263 resting ≥ 20,000 ✓) ≈ $0.29/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-thomas` | BUY | 3.0¢ | 100 | 1 | $200.00 | ✅ scoring — ~7.1% of bid side (30,004 resting ≥ 20,000 ✓) ≈ $0.50/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-vivram` | BUY | 1.0¢ | 9,983 | 4 | $200.00 | ✅ scoring — ~6.9% of bid side (20,923 resting ≥ 20,000 ✓) ≈ $0.50/day (event pool ÷ 14 markets) |
| …and 335 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 1 @ 92¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 84¢ | 50 | ×0.1^8 = 0.0 |
|  | 83¢ | 325 | ×0.1^9 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^90 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 144 (135 yours) | ×0.2^0 = 143.5 |
|  | 7¢ | 50 | ×0.2^1 = 10.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **154.2** |

`yours 135.0 / Σ 154.2 = 87.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 87.6% = $3.24/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 3 @ 6¢ → $2.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 4 (3 yours) | ×0.2^0 = 4.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 1 | ×0.2^6 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 14¢ | 473 | ×0.2^8 = 0.0 |
|  | 15¢ | 36,415 | ×0.2^9 = 0.0 |
| | | **Σ** | **4.1** |

`yours 3.0 / Σ 4.1 = 73.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 73.8% = $2.73/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 37 @ 4¢ → $5.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 4¢ | 47 (37 yours) | ×0.2^1 = 9.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **10.5** |

`yours 7.4 / Σ 10.5 = 70.3%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 70.3% = $5.02/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-thomas</code> BUY 19,311 @ 1¢ → $3.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 2 | ×0.2^0 = 2.0 |
|  | 3¢ | 213 | ×0.2^1 = 42.6 |
| ▶ | 1¢ | 29,789 (19,311 yours) | ×0.2^3 = 238.3 |
| | | **Σ** | **282.9** |

`yours 154.5 / Σ 282.9 = 54.6%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 54.6% = $3.90/day`  

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
11. `enwc-uspres-nom-rep-2028-thomas` ← this one
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 20 @ 9¢ → $2.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 0.9 |
| ▶ | 9¢ | 21 (20 yours) | ×0.2^2 = 0.8 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 64 | ×0.2^6 = 0.0 |
|  | 4¢ | 226 | ×0.2^7 = 0.0 |
|  | 3¢ | 110 | ×0.2^8 = 0.0 |
|  | 1¢ | 40,460 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.7** |

`yours 0.8 / Σ 1.7 = 46.5%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 46.5% = $2.74/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 178 (135 yours) | ×0.2^0 = 177.9 |
|  | 4¢ | 18 | ×0.2^1 = 3.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
|  | 1¢ | 84,975 | ×0.2^4 = 136.0 |
| | | **Σ** | **317.6** |

`yours 135.0 / Σ 317.6 = 42.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 42.5% = $1.57/day`  

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 30 @ 2¢ → $2.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 74 (30 yours) | ×0.1^0 = 74.0 |
|  | 5¢ | 4 | ×0.1^3 = 0.0 |
|  | 9¢ | 50 | ×0.1^7 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^96 = 0.0 |
| | | **Σ** | **74.0** |

`yours 30.0 / Σ 74.0 = 40.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 40.5% = $2.53/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 19,263 @ 1¢ → $1.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 249 | ×0.2^0 = 249.0 |
| ▶ | 1¢ | 41,813 (19,263 yours) | ×0.2^3 = 334.5 |
| | | **Σ** | **583.5** |

`yours 154.1 / Σ 583.5 = 26.4%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 26.4% = $1.89/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> SELL 10 @ 95¢ → $1.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 28 (10 yours) | ×0.1^0 = 28.0 |
|  | 96¢ | 53 | ×0.1^1 = 5.3 |
|  | 97¢ | 439 | ×0.1^2 = 4.4 |
|  | 99¢ | 4,031 | ×0.1^4 = 0.4 |
| | | **Σ** | **38.1** |

`yours 10.0 / Σ 38.1 = 26.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.3% = $1.64/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 19,336 @ 1¢ → $1.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 255 | ×0.2^0 = 255.0 |
| ▶ | 1¢ | 41,811 (19,336 yours) | ×0.2^3 = 334.5 |
| | | **Σ** | **589.5** |

`yours 154.7 / Σ 589.5 = 26.2%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 26.2% = $1.87/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 1 @ 6¢ → $0.91/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 4 (1 yours) | ×0.2^0 = 4.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 1 | ×0.2^6 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 14¢ | 473 | ×0.2^8 = 0.0 |
|  | 15¢ | 36,415 | ×0.2^9 = 0.0 |
| | | **Σ** | **4.1** |

`yours 1.0 / Σ 4.1 = 24.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 24.6% = $0.91/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-rokha</code> SELL 1 @ 10¢ → $1.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 3 (1 yours) | ×0.2^0 = 2.8 |
|  | 15¢ | 30 | ×0.2^5 = 0.0 |
|  | 16¢ | 21,866 | ×0.2^6 = 1.4 |
| | | **Σ** | **4.2** |

`yours 1.0 / Σ 4.2 = 24.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 24.0% = $1.41/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-jdvan</code> BUY 70 @ 50¢ → $1.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 51¢ | 18 | ×0.2^0 = 17.8 |
| ▶ | 50¢ | 249 (70 yours) | ×0.2^1 = 49.8 |
|  | 48¢ | 120 | ×0.2^3 = 1.0 |
|  | 43¢ | 581 | ×0.2^8 = 0.0 |
|  | 32¢ | 108 | ×0.2^19 = 0.0 |
|  | 31¢ | 50 | ×0.2^20 = 0.0 |
|  | 5¢ | 100 | ×0.2^46 = 0.0 |
|  | 3¢ | 2,238 | ×0.2^48 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^49 = 0.0 |
| | | **Σ** | **68.6** |

`yours 14.0 / Σ 68.6 = 20.4%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 20.4% = $1.46/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan` ← this one
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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> BUY 1,693 @ 1¢ → $0.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,999 (1,693 yours) | ×0.1^0 = 11,999.0 |
| | | **Σ** | **11,999.0** |

`yours 1,693.0 / Σ 11,999.0 = 14.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 14.1% = $0.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 50 @ 9¢ → $0.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 63 | ×0.2^0 = 62.9 |
| ▶ | 9¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 5 | ×0.2^5 = 0.0 |
|  | 2¢ | 111 | ×0.2^8 = 0.0 |
|  | 1¢ | 80,022 | ×0.2^9 = 0.0 |
| | | **Σ** | **73.0** |

`yours 10.0 / Σ 73.0 = 13.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 13.7% = $0.51/day`  

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
19. `ewc-usp-2028-11-07-rahema` ← this one
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
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> SELL 85 @ 2¢ → $0.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 651 (85 yours) | ×0.1^0 = 651.0 |
|  | 6¢ | 50 | ×0.1^4 = 0.0 |
|  | 49¢ | 5,000 | ×0.1^47 = 0.0 |
| | | **Σ** | **651.0** |

`yours 85.0 / Σ 651.0 = 13.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 13.1% = $0.82/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 1 @ 90¢ → $0.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 88¢ | 705 | ×0.1^2 = 7.1 |
|  | 75¢ | 50 | ×0.1^15 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^88 = 0.0 |
| | | **Σ** | **9.1** |

`yours 1.0 / Σ 9.1 = 11.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 11.0% = $0.69/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tuccar</code> BUY 200 @ 4¢ → $0.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 6 | ×0.2^0 = 6.0 |
| ▶ | 4¢ | 201 (200 yours) | ×0.2^1 = 40.2 |
|  | 2¢ | 43,580 | ×0.2^3 = 348.6 |
| | | **Σ** | **394.8** |

`yours 40.0 / Σ 394.8 = 10.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 10.1% = $0.38/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 19,484 @ 1¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 178 | ×0.2^0 = 177.9 |
|  | 4¢ | 18 | ×0.2^1 = 3.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
| ▶ | 1¢ | 84,975 (19,484 yours) | ×0.2^4 = 136.0 |
| | | **Σ** | **317.6** |

`yours 31.2 / Σ 317.6 = 9.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 9.8% = $0.36/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 100 @ 7¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 37 | ×0.2^0 = 36.8 |
| ▶ | 7¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 2 | ×0.2^5 = 0.0 |
|  | 2¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 51,182 | ×0.2^8 = 0.1 |
| | | **Σ** | **40.9** |

`yours 4.0 / Σ 40.9 = 9.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 9.8% = $0.36/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 1 @ 3¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 4¢ | 47 | ×0.2^1 = 9.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **10.5** |

`yours 1.0 / Σ 10.5 = 9.5%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 9.5% = $0.68/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 5 @ 4¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 4¢ | 47 (5 yours) | ×0.2^1 = 9.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **10.5** |

`yours 1.0 / Σ 10.5 = 9.5%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 9.5% = $0.68/day`  

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 0 @ 87¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 88¢ | 0 | ×0.1^0 = 0.0 |
| ▶ | 87¢ | 0 (0 yours) | ×0.1^1 = 0.0 |
|  | 85¢ | 0 | ×0.1^3 = 0.0 |
|  | 84¢ | 0 | ×0.1^4 = 0.0 |
|  | 74¢ | 152 | ×0.1^14 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^86 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 9.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 9.1% = $0.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-vivram</code> BUY 100 @ 4¢ → $0.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 177 | ×0.2^0 = 177.0 |
| ▶ | 4¢ | 100 (100 yours) | ×0.2^1 = 20.0 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
|  | 1¢ | 20,633 | ×0.2^4 = 33.0 |
| | | **Σ** | **230.1** |

`yours 20.0 / Σ 230.1 = 8.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 8.7% = $0.62/day`  

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
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 50 @ 4¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 249 (50 yours) | ×0.2^0 = 249.0 |
|  | 1¢ | 41,813 | ×0.2^3 = 334.5 |
| | | **Σ** | **583.5** |

`yours 50.0 / Σ 583.5 = 8.6%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 8.6% = $0.61/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 50 @ 4¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 255 (50 yours) | ×0.2^0 = 255.0 |
|  | 1¢ | 41,811 | ×0.2^3 = 334.5 |
| | | **Σ** | **589.5** |

`yours 50.0 / Σ 589.5 = 8.5%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 8.5% = $0.61/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jonoss</code> BUY 50 @ 18¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 18¢ | 641 (50 yours) | ×0.2^1 = 128.1 |
|  | 15¢ | 5 | ×0.2^4 = 0.0 |
|  | 11¢ | 61 | ×0.2^8 = 0.0 |
|  | 2¢ | 1,000 | ×0.2^17 = 0.0 |
|  | 1¢ | 200,556 | ×0.2^18 = 0.0 |
| | | **Σ** | **129.1** |

`yours 10.0 / Σ 129.1 = 7.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 7.7% = $0.29/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-thomas</code> BUY 100 @ 3¢ → $0.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 3¢ | 213 (100 yours) | ×0.2^1 = 42.6 |
|  | 1¢ | 29,789 | ×0.2^3 = 238.3 |
| | | **Σ** | **282.9** |

`yours 20.0 / Σ 282.9 = 7.1%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 7.1% = $0.50/day`  

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
11. `enwc-uspres-nom-rep-2028-thomas` ← this one
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-vivram</code> BUY 9,983 @ 1¢ → $0.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 177 | ×0.2^0 = 177.0 |
|  | 4¢ | 100 | ×0.2^1 = 20.0 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
| ▶ | 1¢ | 20,633 (9,983 yours) | ×0.2^4 = 33.0 |
| | | **Σ** | **230.1** |

`yours 16.0 / Σ 230.1 = 6.9%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 6.9% = $0.50/day`  

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
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-19 | ~$143.67 | $0.60 | 0% |

Biggest gaps on 2026-08-19: `usgubewc-usgub-id-2026-11-03-rep` (est ~$7.88 → got $0.00), `usgubewc-usgub-ct-2026-11-03-dem` (est ~$6.08 → got $0.00), `enwc-uspres-nom-dem-2028-petbut` (est ~$6.04 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,254 resting) | ~30.0% | ~$22.48 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (149,916 resting) | ~15.3% | ~$11.51 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (67,886 resting) | ~44.9% | ~$11.24 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (25,902 resting) | ~11.7% | ~$8.79 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (905,634 resting) | ~7.0% | ~$5.26 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (80,427 resting) | ~5.8% | ~$4.38 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (49,507 resting) | ~10.2% | ~$2.56 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (635,917 resting) | ~7.9% | ~$1.97 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (689,838 resting) | ~2.4% | ~$1.76 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (107,058 resting) | ~1.7% | ~$1.26 |
| `ewc-usse-nc-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (77,431 resting) | ~4.1% | ~$1.02 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (153,900 resting) | ~1.3% | ~$0.97 |

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
| 2026-08-20 7:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 6:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 5:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 4:10 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:42 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 11:41 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 10:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 9:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 8:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 7:30 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
