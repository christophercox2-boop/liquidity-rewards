# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 9:28 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$70.75/day estimated (ceiling, not promise — details below)

**Earned:** $5,595.00 lifetime ($5,593.52 paid). Last three recorded days — 2026-08-19: **$0.60** · 2026-08-18: **$181.52** · 2026-08-17: **$295.29** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$22.38/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$11.50/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$4.59/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$70.75/day (~$2.95/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 91.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (65,143 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-mt-2026-11-03-rep` | BUY | 65.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~99.8% of bid side (502,617 resting ≥ 2,000 ✓) ≈ $4.16/day (event pool ÷ 3 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~72.1% of ask side (54,635 resting ≥ 20,000 ✓) ≈ $2.67/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~67.1% of bid side (52,791 resting ≥ 20,000 ✓) ≈ $2.48/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 37 | 1 | $200.00 | ✅ scoring — ~64.2% of ask side (47,006 resting ≥ 20,000 ✓) ≈ $4.59/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 9.0¢ | 50 | 1 | $200.00 | ✅ scoring — ~50.1% of bid side (103,421 resting ≥ 20,000 ✓) ≈ $1.86/day (event pool ÷ 27 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~40.5% of ask side (67,403 resting ≥ 2,000 ✓) ≈ $2.53/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-thomas` | BUY | 1.0¢ | 19,311 | 3 | $200.00 | ✅ scoring — ~40.5% of bid side (42,304 resting ≥ 20,000 ✓) ≈ $2.89/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~39.6% of bid side (87,584 resting ≥ 20,000 ✓) ≈ $1.46/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 9.0¢ | 10 | 1 | $25.00 | ✅ scoring — ~32.3% of ask side (67,338 resting ≥ 2,000 ✓) ≈ $2.02/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | SELL | 95.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~27.9% of ask side (3,952 resting ≥ 2,000 ✓) ≈ $1.74/day (event pool ÷ 2 markets) |
| `ussewc-usse-wv-2026-11-03-dem` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~25.8% of ask side (137,814 resting ≥ 2,000 ✓) ≈ $1.61/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 19,263 | 3 | $200.00 | ✅ scoring — ~25.6% of bid side (44,362 resting ≥ 20,000 ✓) ≈ $1.83/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~24.0% of ask side (54,635 resting ≥ 20,000 ✓) ≈ $0.89/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 8.0¢ | 100 | 2 | $200.00 | ✅ scoring — ~20.1% of bid side (103,421 resting ≥ 20,000 ✓) ≈ $0.74/day (event pool ÷ 27 markets) |
| `ussewc-usse-co-2026-11-03-rep` | SELL | 6.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~17.8% of ask side (61,019 resting ≥ 2,000 ✓) ≈ $1.11/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-jdvan` | BUY | 50.0¢ | 70 | 1 | $200.00 | ✅ scoring — ~15.2% of bid side (76,003 resting ≥ 20,000 ✓) ≈ $1.09/day (event pool ÷ 14 markets) |
| `ussewc-usse-fl-2026-11-03-rep` | BUY | 84.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~14.2% of bid side (510,638 resting ≥ 2,000 ✓) ≈ $0.88/day (event pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | SELL | 2.0¢ | 85 | 0 | $25.00 | ✅ scoring — ~13.0% of ask side (310,768 resting ≥ 2,000 ✓) ≈ $0.81/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 9.0¢ | 20 | 2 | $200.00 | ✅ scoring — ~12.4% of bid side (45,729 resting ≥ 20,000 ✓) ≈ $0.73/day (event pool ÷ 17 markets) |
| `ewc-usgub-ca-2026-11-03-xavbec` | SELL | 95.0¢ | 200 | 0 | $300.00 | ✅ scoring — ~10.8% of ask side (27,053 resting ≥ 10,000 ✓) ≈ $8.12/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,693 | 0 | $25.00 | ✅ scoring — ~10.7% of bid side (15,799 resting ≥ 2,000 ✓) ≈ $0.67/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-tuccar` | BUY | 4.0¢ | 200 | 1 | $200.00 | ✅ scoring — ~10.1% of bid side (80,816 resting ≥ 20,000 ✓) ≈ $0.38/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 19,336 | 3 | $200.00 | ✅ scoring — ~10.1% of bid side (154,566 resting ≥ 20,000 ✓) ≈ $0.72/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 7.0¢ | 100 | 2 | $200.00 | ✅ scoring — ~9.6% of bid side (53,723 resting ≥ 20,000 ✓) ≈ $0.35/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-markel` | BUY | 11.0¢ | 50 | 2 | $200.00 | ✅ scoring — ~9.2% of bid side (122,357 resting ≥ 20,000 ✓) ≈ $0.54/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 1.0¢ | 19,484 | 4 | $200.00 | ✅ scoring — ~9.1% of bid side (87,584 resting ≥ 20,000 ✓) ≈ $0.34/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-al-2026-11-03-dem` | BUY | 12.0¢ | 0 | 1 | $25.00 | ✅ scoring — ~9.1% of bid side (42,110 resting ≥ 2,000 ✓) ≈ $0.57/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 87.0¢ | 0 | 1 | $25.00 | ✅ scoring — ~9.1% of bid side (502,152 resting ≥ 2,000 ✓) ≈ $0.57/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 3.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~8.7% of ask side (47,006 resting ≥ 20,000 ✓) ≈ $0.62/day (event pool ÷ 14 markets) |
| …and 362 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 10 @ 91¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 97¢ | 5,193 | ×0.1^6 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.9% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-mt-2026-11-03-rep</code> BUY 0 @ 65¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 0 (0 yours) | ×0.1^0 = 0.1 |
|  | 60¢ | 10 | ×0.1^5 = 0.0 |
|  | 53¢ | 607 | ×0.1^12 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^63 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 99.8%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 99.8% = $4.16/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `ussewc-usse-mt-2026-11-03-dem`
2. `ussewc-usse-mt-2026-11-03-rep` ← this one
3. `ussewc-usse-mt-2026-11-03-setbod`

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
|  | 1¢ | 52,397 | ×0.2^7 = 0.7 |
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
|  | 13¢ | 3 | ×0.2^10 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 50 @ 9¢ → $1.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 6 | ×0.2^0 = 5.8 |
| ▶ | 9¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 8¢ | 101 | ×0.2^2 = 4.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 5 | ×0.2^5 = 0.0 |
|  | 3¢ | 25 | ×0.2^7 = 0.0 |
|  | 2¢ | 111 | ×0.2^8 = 0.0 |
|  | 1¢ | 103,122 | ×0.2^9 = 0.1 |
| | | **Σ** | **19.9** |

`yours 10.0 / Σ 19.9 = 50.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 50.1% = $1.86/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-thomas</code> BUY 19,311 @ 1¢ → $2.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 2 | ×0.2^0 = 2.0 |
|  | 3¢ | 213 | ×0.2^1 = 42.6 |
| ▶ | 1¢ | 42,089 (19,311 yours) | ×0.2^3 = 336.7 |
| | | **Σ** | **381.3** |

`yours 154.5 / Σ 381.3 = 40.5%`  
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
11. `enwc-uspres-nom-rep-2028-thomas` ← this one
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 178 (135 yours) | ×0.2^0 = 177.9 |
|  | 4¢ | 118 | ×0.2^1 = 23.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
|  | 1¢ | 87,275 | ×0.2^4 = 139.6 |
| | | **Σ** | **341.3** |

`yours 135.0 / Σ 341.3 = 39.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 39.6% = $1.46/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 10 @ 9¢ → $2.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 9¢ | 11 (10 yours) | ×0.1^1 = 1.1 |
|  | 16¢ | 50 | ×0.1^8 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^90 = 0.0 |
| | | **Σ** | **3.1** |

`yours 1.0 / Σ 3.1 = 32.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 32.3% = $2.02/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> SELL 10 @ 95¢ → $1.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 26 (10 yours) | ×0.1^0 = 26.0 |
|  | 96¢ | 52 | ×0.1^1 = 5.2 |
|  | 97¢ | 429 | ×0.1^2 = 4.3 |
|  | 99¢ | 3,445 | ×0.1^4 = 0.3 |
| | | **Σ** | **35.8** |

`yours 10.0 / Σ 35.8 = 27.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.9% = $1.74/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wv-2026-11-03-dem</code> SELL 1 @ 5¢ → $1.61/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 7¢ | 288 | ×0.1^2 = 2.9 |
|  | 45¢ | 5,000 | ×0.1^40 = 0.0 |
| | | **Σ** | **3.9** |

`yours 1.0 / Σ 3.9 = 25.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 25.8% = $1.61/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wv-2026-11-03-dem` ← this one
2. `ussewc-usse-wv-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 19,263 @ 1¢ → $1.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 249 | ×0.2^0 = 249.0 |
| ▶ | 1¢ | 44,113 (19,263 yours) | ×0.2^3 = 352.9 |
| | | **Σ** | **601.9** |

`yours 154.1 / Σ 601.9 = 25.6%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 25.6% = $1.83/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 100 @ 8¢ → $0.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 6 | ×0.2^0 = 5.8 |
|  | 9¢ | 50 | ×0.2^1 = 10.0 |
| ▶ | 8¢ | 101 (100 yours) | ×0.2^2 = 4.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 5 | ×0.2^5 = 0.0 |
|  | 3¢ | 25 | ×0.2^7 = 0.0 |
|  | 2¢ | 111 | ×0.2^8 = 0.0 |
|  | 1¢ | 103,122 | ×0.2^9 = 0.1 |
| | | **Σ** | **19.9** |

`yours 4.0 / Σ 19.9 = 20.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 20.1% = $0.74/day`  

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
<details><summary><code>ussewc-usse-co-2026-11-03-rep</code> SELL 10 @ 6¢ → $1.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 56 (10 yours) | ×0.1^0 = 56.1 |
|  | 9¢ | 50 | ×0.1^3 = 0.1 |
|  | 98¢ | 58,888 | ×0.1^92 = 0.0 |
| | | **Σ** | **56.1** |

`yours 10.0 / Σ 56.1 = 17.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 17.8% = $1.11/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem`
2. `ussewc-usse-co-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-jdvan</code> BUY 70 @ 50¢ → $1.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 51¢ | 37 | ×0.2^0 = 37.3 |
| ▶ | 50¢ | 269 (70 yours) | ×0.2^1 = 53.8 |
|  | 48¢ | 120 | ×0.2^3 = 1.0 |
|  | 43¢ | 581 | ×0.2^8 = 0.0 |
|  | 32¢ | 108 | ×0.2^19 = 0.0 |
|  | 31¢ | 50 | ×0.2^20 = 0.0 |
|  | 5¢ | 100 | ×0.2^46 = 0.0 |
|  | 3¢ | 2,238 | ×0.2^48 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^49 = 0.0 |
| | | **Σ** | **92.1** |

`yours 14.0 / Σ 92.1 = 15.2%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 15.2% = $1.09/day`  

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
<details><summary><code>ussewc-usse-fl-2026-11-03-rep</code> BUY 10 @ 84¢ → $0.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 67 (10 yours) | ×0.1^0 = 67.3 |
|  | 82¢ | 250 | ×0.1^2 = 2.5 |
|  | 81¢ | 830 | ×0.1^3 = 0.8 |
|  | 79¢ | 2,000 | ×0.1^5 = 0.0 |
| | | **Σ** | **70.6** |

`yours 10.0 / Σ 70.6 = 14.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 14.2% = $0.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem`
2. `ussewc-usse-fl-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> SELL 85 @ 2¢ → $0.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 655 (85 yours) | ×0.1^0 = 655.0 |
|  | 6¢ | 50 | ×0.1^4 = 0.0 |
|  | 49¢ | 5,000 | ×0.1^47 = 0.0 |
| | | **Σ** | **655.0** |

`yours 85.0 / Σ 655.0 = 13.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 13.0% = $0.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 20 @ 9¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 6 | ×0.2^0 = 5.6 |
| ▶ | 9¢ | 21 (20 yours) | ×0.2^2 = 0.8 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 64 | ×0.2^6 = 0.0 |
|  | 4¢ | 226 | ×0.2^7 = 0.0 |
|  | 3¢ | 110 | ×0.2^8 = 0.0 |
|  | 2¢ | 22,500 | ×0.2^9 = 0.0 |
| | | **Σ** | **6.5** |

`yours 0.8 / Σ 6.5 = 12.4%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 12.4% = $0.73/day`  

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
<details><summary><code>ewc-usgub-ca-2026-11-03-xavbec</code> SELL 200 @ 95¢ → $8.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 1,682 (200 yours) | ×0.2^0 = 1,682.3 |
|  | 97¢ | 39 | ×0.2^2 = 1.6 |
|  | 98¢ | 20,332 | ×0.2^3 = 162.7 |
| | | **Σ** | **1,846.5** |

`yours 200.0 / Σ 1,846.5 = 10.8%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 10.8% = $8.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usgub-ca-2026-11-03-stehil`
2. `ewc-usgub-ca-2026-11-03-xavbec` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> BUY 1,693 @ 1¢ → $0.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 15,799 (1,693 yours) | ×0.1^0 = 15,799.0 |
| | | **Σ** | **15,799.0** |

`yours 1,693.0 / Σ 15,799.0 = 10.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 10.7% = $0.67/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

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
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 19,336 @ 1¢ → $0.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 255 | ×0.2^0 = 255.0 |
|  | 3¢ | 200 | ×0.2^1 = 40.0 |
| ▶ | 1¢ | 154,111 (19,336 yours) | ×0.2^3 = 1,232.9 |
| | | **Σ** | **1,527.9** |

`yours 154.7 / Σ 1,527.9 = 10.1%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 10.1% = $0.72/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> BUY 50 @ 11¢ → $0.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 18 | ×0.2^0 = 18.1 |
| ▶ | 11¢ | 50 (50 yours) | ×0.2^2 = 2.0 |
|  | 9¢ | 986 | ×0.2^4 = 1.6 |
|  | 8¢ | 193 | ×0.2^5 = 0.1 |
|  | 7¢ | 110 | ×0.2^6 = 0.0 |
|  | 2¢ | 48,500 | ×0.2^11 = 0.0 |
| | | **Σ** | **21.8** |

`yours 2.0 / Σ 21.8 = 9.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 9.2% = $0.54/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 19,484 @ 1¢ → $0.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 178 | ×0.2^0 = 177.9 |
|  | 4¢ | 118 | ×0.2^1 = 23.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
| ▶ | 1¢ | 87,275 (19,484 yours) | ×0.2^4 = 139.6 |
| | | **Σ** | **341.3** |

`yours 31.2 / Σ 341.3 = 9.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 9.1% = $0.34/day`  

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
<details><summary><code>usgubewc-usgub-al-2026-11-03-dem</code> BUY 0 @ 12¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 0 | ×0.1^0 = 0.1 |
| ▶ | 12¢ | 0 (0 yours) | ×0.1^1 = 0.0 |
|  | 1¢ | 42,110 | ×0.1^12 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 9.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 9.1% = $0.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem` ← this one
2. `usgubewc-usgub-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 0 @ 87¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 88¢ | 0 | ×0.1^0 = 0.0 |
| ▶ | 87¢ | 0 (0 yours) | ×0.1^1 = 0.0 |
|  | 85¢ | 0 | ×0.1^3 = 0.0 |
|  | 84¢ | 0 | ×0.1^4 = 0.0 |
|  | 75¢ | 50 | ×0.1^13 = 0.0 |
|  | 74¢ | 102 | ×0.1^14 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^86 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 9.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 9.1% = $0.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 1 @ 3¢ → $0.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 4¢ | 52 | ×0.2^1 = 10.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 3 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **11.5** |

`yours 1.0 / Σ 11.5 = 8.7%`  
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
9. `enwc-uspres-nom-rep-2028-rondes` ← this one
10. `enwc-uspres-nom-rep-2028-tedcru`
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
| 2026-08-19 | ~$28.44 | $0.60 | 2% |

Biggest gaps on 2026-08-19: `ussewc-usse-de-2026-11-03-dem` (est ~$3.83 → got $0.00), `ussewc-usse-il-2026-11-03-dem` (est ~$3.78 → got $0.00), `ussewc-usse-ok-2026-11-03-rep` (est ~$2.67 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (86,557 resting) | ~29.8% | ~$22.38 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (152,214 resting) | ~15.3% | ~$11.50 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,572 resting) | ~18.4% | ~$4.59 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,688 resting) | ~5.4% | ~$4.08 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (921,992 resting) | ~4.6% | ~$3.48 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (391,465 resting) | ~4.0% | ~$2.98 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (69,854 resting) | ~9.3% | ~$2.32 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (638,219 resting) | ~7.9% | ~$1.98 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (93,317 resting) | ~1.5% | ~$1.11 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (695,733 resting) | ~1.5% | ~$1.10 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (84,947 resting) | ~17.5% | ~$1.09 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (155,945 resting) | ~1.3% | ~$0.99 |

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
| 2026-08-20 9:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 8:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 7:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 6:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 5:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 4:10 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:42 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 11:41 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 10:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 9:32 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
