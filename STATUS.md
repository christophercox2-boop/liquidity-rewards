# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 10:29 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$91.52/day estimated (ceiling, not promise — details below)

**Earned:** $5,595.00 lifetime ($5,593.52 paid). Last three recorded days — 2026-08-19: **$0.60** · 2026-08-18: **$181.52** · 2026-08-17: **$295.29** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$27.72/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$11.49/day), `ewc-usse-ga-2026-11-03-rep` (~$7.68/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$91.52/day (~$3.81/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 91.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (64,944 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~93.7% of ask side (67,361 resting ≥ 2,000 ✓) ≈ $5.86/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~72.1% of ask side (54,635 resting ≥ 20,000 ✓) ≈ $2.67/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~67.1% of bid side (53,791 resting ≥ 20,000 ✓) ≈ $2.48/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 37 | 1 | $200.00 | ✅ scoring — ~64.2% of ask side (47,008 resting ≥ 20,000 ✓) ≈ $4.59/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 11.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~60.7% of bid side (45,772 resting ≥ 20,000 ✓) ≈ $3.57/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 9.0¢ | 50 | 1 | $200.00 | ✅ scoring — ~52.6% of bid side (103,395 resting ≥ 20,000 ✓) ≈ $1.95/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~50.0% of ask side (67,329 resting ≥ 2,000 ✓) ≈ $3.12/day (event pool ÷ 2 markets) |
| `ussewc-usse-co-2026-11-03-rep` | SELL | 6.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~49.7% of ask side (60,983 resting ≥ 2,000 ✓) ≈ $3.11/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-vt-2026-11-03-dem` | BUY | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~49.6% of bid side (16,602 resting ≥ 2,000 ✓) ≈ $3.10/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 5.0¢ | 10 | 0 | $200.00 | ✅ scoring — ~49.5% of ask side (60,636 resting ≥ 20,000 ✓) ≈ $2.91/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~38.4% of bid side (87,595 resting ≥ 20,000 ✓) ≈ $1.42/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 5.0¢ | 8 | 0 | $25.00 | ✅ scoring — ~37.4% of bid side (3,820 resting ≥ 2,000 ✓) ≈ $2.34/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-markel` | BUY | 13.0¢ | 10 | 0 | $200.00 | ✅ scoring — ~31.5% of bid side (122,367 resting ≥ 20,000 ✓) ≈ $1.85/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | SELL | 95.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~30.1% of ask side (4,377 resting ≥ 2,000 ✓) ≈ $1.88/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 19,263 | 3 | $200.00 | ✅ scoring — ~26.0% of bid side (43,262 resting ≥ 20,000 ✓) ≈ $1.86/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 16.0¢ | 16 | 0 | $25.00 | ✅ scoring — ~25.7% of bid side (37,208 resting ≥ 2,000 ✓) ≈ $1.60/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~24.0% of ask side (54,635 resting ≥ 20,000 ✓) ≈ $0.89/day (event pool ÷ 27 markets) |
| `ussewc-usse-ma-2026-11-03-rep` | SELL | 6.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~21.8% of ask side (67,435 resting ≥ 2,000 ✓) ≈ $1.36/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 8.0¢ | 100 | 2 | $200.00 | ✅ scoring — ~21.0% of bid side (103,395 resting ≥ 20,000 ✓) ≈ $0.78/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-rokha` | BUY | 10.0¢ | 8 | 0 | $200.00 | ✅ scoring — ~21.0% of bid side (25,568 resting ≥ 20,000 ✓) ≈ $1.24/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-jdvan` | BUY | 50.0¢ | 70 | 1 | $200.00 | ✅ scoring — ~20.9% of bid side (75,978 resting ≥ 20,000 ✓) ≈ $1.49/day (event pool ÷ 14 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | SELL | 2.0¢ | 85 | 0 | $25.00 | ✅ scoring — ~18.8% of ask side (310,566 resting ≥ 2,000 ✓) ≈ $1.17/day (event pool ÷ 2 markets) |
| `ewc-usgub-ca-2026-11-03-xavbec` | SELL | 95.0¢ | 200 | 0 | $300.00 | ✅ scoring — ~16.1% of ask side (26,449 resting ≥ 10,000 ✓) ≈ $12.08/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-thomas` | BUY | 1.0¢ | 19,311 | 3 | $200.00 | ✅ scoring — ~12.2% of bid side (152,304 resting ≥ 20,000 ✓) ≈ $0.87/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 10.0¢ | 20 | 1 | $200.00 | ✅ scoring — ~12.1% of bid side (45,772 resting ≥ 20,000 ✓) ≈ $0.71/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-tuccar` | BUY | 4.0¢ | 200 | 1 | $200.00 | ✅ scoring — ~10.2% of bid side (80,316 resting ≥ 20,000 ✓) ≈ $0.38/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 19,336 | 3 | $200.00 | ✅ scoring — ~10.2% of bid side (153,566 resting ≥ 20,000 ✓) ≈ $0.73/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | SELL | 5.0¢ | 32 | 0 | $200.00 | ✅ scoring — ~10.1% of ask side (50,886 resting ≥ 20,000 ✓) ≈ $0.60/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 7.0¢ | 100 | 2 | $200.00 | ✅ scoring — ~9.6% of bid side (53,723 resting ≥ 20,000 ✓) ≈ $0.35/day (event pool ÷ 27 markets) |
| …and 368 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 10 @ 91¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 97¢ | 4,994 | ×0.1^6 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 30 @ 2¢ → $5.86/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 32 (30 yours) | ×0.1^0 = 32.0 |
|  | 5¢ | 4 | ×0.1^3 = 0.0 |
|  | 9¢ | 50 | ×0.1^7 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^96 = 0.0 |
| | | **Σ** | **32.0** |

`yours 30.0 / Σ 32.0 = 93.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.7% = $5.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 3 @ 6¢ → $2.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 4 (3 yours) | ×0.2^0 = 4.0 |
|  | 7¢ | 0 | ×0.2^1 = 0.1 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 1 | ×0.2^6 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 14¢ | 473 | ×0.2^8 = 0.0 |
|  | 15¢ | 26,415 | ×0.2^9 = 0.0 |
| | | **Σ** | **4.2** |

`yours 3.0 / Σ 4.2 = 72.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 72.1% = $2.67/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $2.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 180 (135 yours) | ×0.2^0 = 180.5 |
|  | 7¢ | 100 | ×0.2^1 = 20.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 53,397 | ×0.2^7 = 0.7 |
| | | **Σ** | **201.2** |

`yours 135.0 / Σ 201.2 = 67.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 67.1% = $2.48/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 37 @ 4¢ → $4.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 4¢ | 52 (37 yours) | ×0.2^1 = 10.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **11.5** |

`yours 7.4 / Σ 11.5 = 64.2%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 64.2% = $4.59/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 20 @ 11¢ → $3.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 28 (20 yours) | ×0.2^0 = 28.1 |
|  | 10¢ | 20 | ×0.2^1 = 4.0 |
|  | 9¢ | 21 | ×0.2^2 = 0.8 |
|  | 8¢ | 2 | ×0.2^3 = 0.0 |
|  | 5¢ | 64 | ×0.2^6 = 0.0 |
|  | 4¢ | 226 | ×0.2^7 = 0.0 |
|  | 3¢ | 110 | ×0.2^8 = 0.0 |
|  | 2¢ | 22,500 | ×0.2^9 = 0.0 |
| | | **Σ** | **32.9** |

`yours 20.0 / Σ 32.9 = 60.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 60.7% = $3.57/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 50 @ 9¢ → $1.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 5 | ×0.2^0 = 4.9 |
| ▶ | 9¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 8¢ | 101 | ×0.2^2 = 4.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 5 | ×0.2^5 = 0.0 |
|  | 2¢ | 111 | ×0.2^8 = 0.0 |
|  | 1¢ | 103,122 | ×0.2^9 = 0.1 |
| | | **Σ** | **19.0** |

`yours 10.0 / Σ 19.0 = 52.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 52.6% = $1.95/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 2 @ 8¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 4 (2 yours) | ×0.1^0 = 4.0 |
|  | 16¢ | 50 | ×0.1^8 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^90 = 0.0 |
| | | **Σ** | **4.0** |

`yours 2.0 / Σ 4.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-co-2026-11-03-rep</code> SELL 10 @ 6¢ → $3.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 20 (10 yours) | ×0.1^0 = 20.1 |
|  | 9¢ | 50 | ×0.1^3 = 0.1 |
|  | 98¢ | 58,888 | ×0.1^92 = 0.0 |
| | | **Σ** | **20.1** |

`yours 10.0 / Σ 20.1 = 49.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.7% = $3.11/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem`
2. `ussewc-usse-co-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-vt-2026-11-03-dem</code> BUY 1 @ 8¢ → $3.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 2¢ | 14,600 | ×0.1^6 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 49.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.6% = $3.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-vt-2026-11-03-dem` ← this one
2. `usgubewc-usgub-vt-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 10 @ 5¢ → $2.91/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 20 (10 yours) | ×0.2^0 = 20.0 |
|  | 6¢ | 1 | ×0.2^1 = 0.2 |
|  | 13¢ | 9 | ×0.2^8 = 0.0 |
|  | 19¢ | 3 | ×0.2^14 = 0.0 |
|  | 20¢ | 40,501 | ×0.2^15 = 0.0 |
| | | **Σ** | **20.2** |

`yours 10.0 / Σ 20.2 = 49.5%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 49.5% = $2.91/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 188 (135 yours) | ×0.2^0 = 188.3 |
|  | 4¢ | 118 | ×0.2^1 = 23.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
|  | 1¢ | 87,275 | ×0.2^4 = 139.6 |
| | | **Σ** | **351.7** |

`yours 135.0 / Σ 351.7 = 38.4%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 38.4% = $1.42/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> BUY 8 @ 5¢ → $2.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 21 (8 yours) | ×0.1^0 = 21.0 |
|  | 1¢ | 3,799 | ×0.1^4 = 0.4 |
| | | **Σ** | **21.4** |

`yours 8.0 / Σ 21.4 = 37.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 37.4% = $2.34/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> BUY 10 @ 13¢ → $1.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 28 (10 yours) | ×0.2^0 = 28.1 |
|  | 11¢ | 50 | ×0.2^2 = 2.0 |
|  | 9¢ | 986 | ×0.2^4 = 1.6 |
|  | 8¢ | 193 | ×0.2^5 = 0.1 |
|  | 7¢ | 110 | ×0.2^6 = 0.0 |
|  | 2¢ | 48,500 | ×0.2^11 = 0.0 |
| | | **Σ** | **31.8** |

`yours 10.0 / Σ 31.8 = 31.5%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 31.5% = $1.85/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> SELL 10 @ 95¢ → $1.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 26 (10 yours) | ×0.1^0 = 26.0 |
|  | 96¢ | 52 | ×0.1^1 = 5.2 |
|  | 97¢ | 166 | ×0.1^2 = 1.7 |
|  | 99¢ | 4,133 | ×0.1^4 = 0.4 |
| | | **Σ** | **33.3** |

`yours 10.0 / Σ 33.3 = 30.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 30.1% = $1.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 19,263 @ 1¢ → $1.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 249 | ×0.2^0 = 249.0 |
| ▶ | 1¢ | 43,013 (19,263 yours) | ×0.2^3 = 344.1 |
| | | **Σ** | **593.1** |

`yours 154.1 / Σ 593.1 = 26.0%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 26.0% = $1.86/day`  

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 16 @ 16¢ → $1.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 63 (16 yours) | ×0.1^0 = 63.2 |
|  | 10¢ | 10 | ×0.1^6 = 0.0 |
|  | 9¢ | 10 | ×0.1^7 = 0.0 |
|  | 6¢ | 125 | ×0.1^10 = 0.0 |
|  | 2¢ | 15,000 | ×0.1^14 = 0.0 |
| | | **Σ** | **63.2** |

`yours 16.2 / Σ 63.2 = 25.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 25.7% = $1.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 1 @ 6¢ → $0.89/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 4 (1 yours) | ×0.2^0 = 4.0 |
|  | 7¢ | 0 | ×0.2^1 = 0.1 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 1 | ×0.2^6 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 14¢ | 473 | ×0.2^8 = 0.0 |
|  | 15¢ | 26,415 | ×0.2^9 = 0.0 |
| | | **Σ** | **4.2** |

`yours 1.0 / Σ 4.2 = 24.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 24.0% = $0.89/day`  

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
<details><summary><code>ussewc-usse-ma-2026-11-03-rep</code> SELL 0 @ 6¢ → $1.36/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 0 (0 yours) | ×0.1^0 = 0.1 |
|  | 7¢ | 0 | ×0.1^1 = 0.0 |
|  | 9¢ | 159 | ×0.1^3 = 0.2 |
|  | 32¢ | 1 | ×0.1^26 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.1 / Σ 0.2 = 21.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 21.8% = $1.36/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem`
2. `ussewc-usse-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 100 @ 8¢ → $0.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 5 | ×0.2^0 = 4.9 |
|  | 9¢ | 50 | ×0.2^1 = 10.0 |
| ▶ | 8¢ | 101 (100 yours) | ×0.2^2 = 4.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 5 | ×0.2^5 = 0.0 |
|  | 2¢ | 111 | ×0.2^8 = 0.0 |
|  | 1¢ | 103,122 | ×0.2^9 = 0.1 |
| | | **Σ** | **19.0** |

`yours 4.0 / Σ 19.0 = 21.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 21.0% = $0.78/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-rokha</code> BUY 8 @ 10¢ → $1.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 38 (8 yours) | ×0.2^0 = 38.0 |
|  | 7¢ | 2 | ×0.2^3 = 0.0 |
|  | 6¢ | 6 | ×0.2^4 = 0.0 |
|  | 5¢ | 21 | ×0.2^5 = 0.0 |
|  | 4¢ | 2 | ×0.2^6 = 0.0 |
|  | 2¢ | 22,610 | ×0.2^8 = 0.1 |
| | | **Σ** | **38.1** |

`yours 8.0 / Σ 38.1 = 21.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 21.0% = $1.24/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-jdvan</code> BUY 70 @ 50¢ → $1.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 51¢ | 12 | ×0.2^0 = 12.2 |
| ▶ | 50¢ | 269 (70 yours) | ×0.2^1 = 53.8 |
|  | 48¢ | 120 | ×0.2^3 = 1.0 |
|  | 43¢ | 581 | ×0.2^8 = 0.0 |
|  | 32¢ | 108 | ×0.2^19 = 0.0 |
|  | 31¢ | 50 | ×0.2^20 = 0.0 |
|  | 5¢ | 100 | ×0.2^46 = 0.0 |
|  | 3¢ | 2,238 | ×0.2^48 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^49 = 0.0 |
| | | **Σ** | **66.9** |

`yours 14.0 / Σ 66.9 = 20.9%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 20.9% = $1.49/day`  

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
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> SELL 85 @ 2¢ → $1.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 453 (85 yours) | ×0.1^0 = 453.0 |
|  | 6¢ | 50 | ×0.1^4 = 0.0 |
|  | 49¢ | 5,000 | ×0.1^47 = 0.0 |
| | | **Σ** | **453.0** |

`yours 85.0 / Σ 453.0 = 18.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 18.8% = $1.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usgub-ca-2026-11-03-xavbec</code> SELL 200 @ 95¢ → $12.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 1,078 (200 yours) | ×0.2^0 = 1,077.9 |
|  | 97¢ | 40 | ×0.2^2 = 1.6 |
|  | 98¢ | 20,332 | ×0.2^3 = 162.7 |
| | | **Σ** | **1,242.1** |

`yours 200.0 / Σ 1,242.1 = 16.1%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 16.1% = $12.08/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usgub-ca-2026-11-03-stehil`
2. `ewc-usgub-ca-2026-11-03-xavbec` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-thomas</code> BUY 19,311 @ 1¢ → $0.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 2 | ×0.2^0 = 2.0 |
|  | 3¢ | 213 | ×0.2^1 = 42.6 |
| ▶ | 1¢ | 152,089 (19,311 yours) | ×0.2^3 = 1,216.7 |
| | | **Σ** | **1,261.3** |

`yours 154.5 / Σ 1,261.3 = 12.2%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 12.2% = $0.87/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 20 @ 10¢ → $0.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 28 | ×0.2^0 = 28.1 |
| ▶ | 10¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 9¢ | 21 | ×0.2^2 = 0.8 |
|  | 8¢ | 2 | ×0.2^3 = 0.0 |
|  | 5¢ | 64 | ×0.2^6 = 0.0 |
|  | 4¢ | 226 | ×0.2^7 = 0.0 |
|  | 3¢ | 110 | ×0.2^8 = 0.0 |
|  | 2¢ | 22,500 | ×0.2^9 = 0.0 |
| | | **Σ** | **32.9** |

`yours 4.0 / Σ 32.9 = 12.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 12.1% = $0.71/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tuccar</code> BUY 200 @ 4¢ → $0.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 6 | ×0.2^0 = 6.0 |
| ▶ | 4¢ | 201 (200 yours) | ×0.2^1 = 40.2 |
|  | 2¢ | 43,080 | ×0.2^3 = 344.6 |
| | | **Σ** | **390.8** |

`yours 40.0 / Σ 390.8 = 10.2%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 10.2% = $0.38/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 19,336 @ 1¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 255 | ×0.2^0 = 255.0 |
|  | 3¢ | 200 | ×0.2^1 = 40.0 |
| ▶ | 1¢ | 153,111 (19,336 yours) | ×0.2^3 = 1,224.9 |
| | | **Σ** | **1,519.9** |

`yours 154.7 / Σ 1,519.9 = 10.2%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 10.2% = $0.73/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> SELL 32 @ 5¢ → $0.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 316 (32 yours) | ×0.2^0 = 316.0 |
|  | 6¢ | 1 | ×0.2^1 = 0.2 |
|  | 15¢ | 30,469 | ×0.2^10 = 0.0 |
| | | **Σ** | **316.2** |

`yours 32.0 / Σ 316.2 = 10.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 10.1% = $0.60/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 100 @ 7¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 37 | ×0.2^0 = 36.8 |
| ▶ | 7¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 6¢ | 101 | ×0.2^3 = 0.8 |
|  | 4¢ | 2 | ×0.2^5 = 0.0 |
|  | 2¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 53,482 | ×0.2^8 = 0.1 |
| | | **Σ** | **41.7** |

`yours 4.0 / Σ 41.7 = 9.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 9.6% = $0.35/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-19 | ~$12.77 | $0.60 | 5% |

Biggest gaps on 2026-08-19: `usgubewc-usgub-tn-2026-11-03-rep` (est ~$2.26 → got $0.00), `ussewc-usse-de-2026-11-03-dem` (est ~$1.21 → got $0.00), `usgubewc-usgub-il-2026-11-03-dem` (est ~$1.21 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (71,111 resting) | ~37.0% | ~$27.72 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (152,027 resting) | ~15.3% | ~$11.49 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (80,737 resting) | ~10.2% | ~$7.68 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (922,028 resting) | ~6.7% | ~$5.03 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,599 resting) | ~18.3% | ~$4.56 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (391,699 resting) | ~3.8% | ~$2.83 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (69,056 resting) | ~9.3% | ~$2.32 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (90,522 resting) | ~28.4% | ~$1.77 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (692,992 resting) | ~2.1% | ~$1.60 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (638,233 resting) | ~6.3% | ~$1.58 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (90,953 resting) | ~28.0% | ~$1.17 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (77,123 resting) | ~18.3% | ~$1.14 |

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
| 2026-08-20 10:29 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 9:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 8:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 7:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 6:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 5:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 4:10 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:42 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 11:41 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 10:40 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
