# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-16 10:47 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$34.39/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-rep` — BUY at the best price, ~$41.73/day for 200 contracts. Runners-up: `ewc-usse-tx-2026-11-03-dem` (~$20.24/day), `ewc-usgub-ga-2026-11-03-dem` (~$18.69/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$34.39/day (~$1.43/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-uspres-nom-dem-2028-petbut` | SELL | 16.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~93.7% of ask side (73,460 resting ≥ 20,000 ✓) ≈ $15.11/day (program pool ÷ 31 markets) |
| `ewc-usp-2028-11-07-jossha` | BUY | 8.0¢ | 1 | 1 | $1,000.00 | ✅ scoring — ~41.9% of bid side (104,451 resting ≥ 20,000 ✓) ≈ $6.76/day (program pool ÷ 31 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 9.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~37.1% of bid side (180,452 resting ≥ 20,000 ✓) ≈ $5.99/day (program pool ÷ 31 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 8.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~30.2% of bid side (180,491 resting ≥ 20,000 ✓) ≈ $4.87/day (program pool ÷ 31 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 7.0¢ | 1 | 3 | $1,000.00 | ✅ scoring — ~9.8% of bid side (104,453 resting ≥ 20,000 ✓) ≈ $1.58/day (program pool ÷ 31 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 5.0¢ | 1 | 5 | $1,000.00 | ✅ scoring — ~0.4% of bid side (104,453 resting ≥ 20,000 ✓) ≈ $0.06/day (program pool ÷ 31 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 4.0¢ | 1 | 5 | $1,000.00 | ✅ scoring — ~0.1% of bid side (180,452 resting ≥ 20,000 ✓) ≈ $0.01/day (program pool ÷ 31 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 4.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~0.0% of bid side (340,376 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 3.0¢ | 1 | 7 | $1,000.00 | ✅ scoring — ~0.0% of bid side (104,453 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 31 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 3.0¢ | 1 | 6 | $1,000.00 | ✅ scoring — ~0.0% of bid side (180,452 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 31 markets) |
| `enwc-uspres-nom-dem-2028-markel` | BUY | 3.0¢ | 1 | 4 | $1,000.00 | ✅ scoring — ~0.0% of bid side (176,452 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 31 markets) |
| `ewc-usp-2028-11-07-gavnew` | BUY | 7.0¢ | 1 | 9 | $1,000.00 | ✅ scoring — ~0.0% of bid side (96,483 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 31 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 2.0¢ | 1 | 2 | $100.00 | ✅ scoring — ~0.0% of bid side (340,376 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-tuccar` | SELL | 13.0¢ | 1 | 6 | $1,000.00 | ✅ scoring — ~0.0% of ask side (72,144 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 31 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 3.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~0.0% of bid side (415,450 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 5.0¢ | 1 | 42 | $100.00 | ✅ scoring — ~0.0% of bid side (50,206 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 6.0¢ | 1 | 0 | $1,000.00 | ❌ side has 453 of 20,000 Target Size — side not qualifying |
| `enwc-uspres-nom-dem-2028-jamtal` | BUY | 13.0¢ | 1 | 0 | $1,000.00 | ❌ side has 481 of 20,000 Target Size — side not qualifying |
| `ewc-usp-2028-11-07-dwajoh` | BUY | 5.0¢ | 1 | 0 | $1,000.00 | ❌ side has 451 of 20,000 Target Size — side not qualifying |
| `ewc-usp-2028-11-07-wesmoo` | BUY | 4.0¢ | 1 | 0 | $1,000.00 | ❌ side has 451 of 20,000 Target Size — side not qualifying |
| `ewc-usp-2028-11-07-rokha` | BUY | 7.0¢ | 1 | 0 | $1,000.00 | ❌ side has 452 of 20,000 Target Size — side not qualifying |
| `ewc-usp-2028-11-07-elomus` | BUY | 12.0¢ | 1 | 0 | $1,000.00 | ❌ side has 5,951 of 20,000 Target Size — side not qualifying |
| `ewc-usp-2028-11-07-dontru` | BUY | 6.0¢ | 1 | 0 | $1,000.00 | ❌ side has 451 of 20,000 Target Size — side not qualifying |
| `ewc-usp-2028-11-07-markel` | BUY | 10.0¢ | 1 | 0 | $1,000.00 | ❌ side has 452 of 20,000 Target Size — side not qualifying |
| `ewc-usp-2028-11-07-micoba` | BUY | 7.0¢ | 1 | 0 | $1,000.00 | ❌ side has 451 of 20,000 Target Size — side not qualifying |
| `ewc-usp-2028-11-07-stasmi` | BUY | 2.0¢ | 1 | 0 | $1,000.00 | ❌ side has 451 of 20,000 Target Size — side not qualifying |
| `ewc-usp-2028-11-07-vivram` | BUY | 4.0¢ | 1 | 0 | $1,000.00 | ❌ side has 452 of 20,000 Target Size — side not qualifying |
| `ewc-usp-2028-11-07-petbut` | BUY | 8.0¢ | 1 | 0 | $1,000.00 | ❌ side has 1,451 of 20,000 Target Size — side not qualifying |
| `usgubewc-usgub-ne-2026-11-03-dem` | BUY | 2.0¢ | 1 | 0 | $25.00 | ❌ side has 201 of 2,000 Target Size — side not qualifying |
| `enwc-uspres-nom-dem-2028-stasmi` | BUY | 5.0¢ | 1 | 0 | $1,000.00 | ❌ side has 531 of 20,000 Target Size — side not qualifying |
| …and 18 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> SELL 1 @ 16¢ → $15.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 22¢ | 50 | ×0.2^6 = 0.0 |
|  | 23¢ | 30 | ×0.2^7 = 0.0 |
|  | 24¢ | 24,871 | ×0.2^8 = 0.1 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 93.7%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 93.7% = $15.11/day`  

<details><summary>÷ 31 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> BUY 1 @ 8¢ → $6.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 8¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 1¢ | 104,450 | ×0.2^8 = 0.3 |
| | | **Σ** | **0.5** |

`yours 0.2 / Σ 0.5 = 41.9%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 41.9% = $6.76/day`  

<details><summary>÷ 31 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 1 @ 9¢ → $5.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2 (1 yours) | ×0.2^0 = 2.2 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **2.7** |

`yours 1.0 / Σ 2.7 = 37.1%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 37.1% = $5.99/day`  

<details><summary>÷ 31 markets in this race (14 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 8¢ → $4.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 2¢ | 30 | ×0.2^6 = 0.0 |
|  | 1¢ | 180,460 | ×0.2^7 = 2.3 |
| | | **Σ** | **3.3** |

`yours 1.0 / Σ 3.3 = 30.2%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 30.2% = $4.87/day`  

<details><summary>÷ 31 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 1 @ 7¢ → $1.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 3¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 104,450 | ×0.2^9 = 0.1 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 9.8%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 9.8% = $1.58/day`  

<details><summary>÷ 31 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes` ← this one
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
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 1 @ 5¢ → $0.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
| ▶ | 5¢ | 1 (1 yours) | ×0.2^5 = 0.0 |
|  | 3¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 104,450 | ×0.2^9 = 0.1 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 0.4%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 0.4% = $0.06/day`  

<details><summary>÷ 31 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes` ← this one
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
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> BUY 1 @ 4¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 4¢ | 1 (1 yours) | ×0.2^5 = 0.0 |
|  | 3¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **0.5** |

`yours 0.0 / Σ 0.5 = 0.1%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 0.1% = $0.01/day`  

<details><summary>÷ 31 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 1 @ 4¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 2¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 340,374 | ×0.2^3 = 2,723.0 |
| | | **Σ** | **2,724.0** |

`yours 1.0 / Σ 2,724.0 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 1 @ 3¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
| ▶ | 3¢ | 1 (1 yours) | ×0.2^7 = 0.0 |
|  | 1¢ | 104,450 | ×0.2^9 = 0.1 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 0.0%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 0.0% = $0.00/day`  

<details><summary>÷ 31 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes` ← this one
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
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> BUY 1 @ 3¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
| ▶ | 3¢ | 1 (1 yours) | ×0.2^6 = 0.0 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **0.5** |

`yours 0.0 / Σ 0.5 = 0.0%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 0.0% = $0.00/day`  

<details><summary>÷ 31 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> BUY 1 @ 3¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 1 | ×0.2^0 = 0.7 |
| ▶ | 3¢ | 1 (1 yours) | ×0.2^4 = 0.0 |
|  | 2¢ | 76,000 | ×0.2^5 = 24.3 |
| | | **Σ** | **25.0** |

`yours 0.0 / Σ 25.0 = 0.0%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 0.0% = $0.00/day`  

<details><summary>÷ 31 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-gavnew</code> BUY 1 @ 7¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^9 = 0.0 |
|  | 6¢ | 10,032 | ×0.2^10 = 0.0 |
|  | 5¢ | 16,000 | ×0.2^11 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 0.0%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 0.0% = $0.00/day`  

<details><summary>÷ 31 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 1 @ 2¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 2¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 1¢ | 340,374 | ×0.2^3 = 2,723.0 |
| | | **Σ** | **2,724.0** |

`yours 0.0 / Σ 2,724.0 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tuccar</code> SELL 1 @ 13¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 5 | ×0.2^0 = 4.6 |
| ▶ | 13¢ | 1 (1 yours) | ×0.2^6 = 0.0 |
|  | 25¢ | 300 | ×0.2^18 = 0.0 |
|  | 26¢ | 21,262 | ×0.2^19 = 0.0 |
| | | **Σ** | **4.6** |

`yours 0.0 / Σ 4.6 = 0.0%`  
`$1,000 ÷ 31 ÷ 2 = $16.13 × 0.0% = $0.00/day`  

<details><summary>÷ 31 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 1 @ 3¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 2¢ | 415,249 | ×0.2^1 = 83,049.8 |
| | | **Σ** | **83,050.8** |

`yours 1.0 / Σ 83,050.8 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225` ← this one
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 1 @ 5¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 47¢ | 0 | ×0.2^0 = 0.0 |
|  | 46¢ | 0 | ×0.2^1 = 0.0 |
|  | 45¢ | 0 | ×0.2^2 = 0.0 |
|  | 40¢ | 0 | ×0.2^7 = 0.0 |
| ▶ | 5¢ | 1 (1 yours) | ×0.2^42 = 0.0 |
|  | 2¢ | 50,000 | ×0.2^45 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 1 @ 6¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 5¢ | 1 | ×0.2^1 = 0.2 |
|  | 3¢ | 1 | ×0.2^3 = 0.0 |
|  | 1¢ | 450 | ×0.2^5 = 0.1 |

`side 453 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> BUY 1 @ 13¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 5¢ | 30 | ×0.2^8 = 0.0 |
|  | 1¢ | 450 | ×0.2^12 = 0.0 |

`side 481 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>ewc-usp-2028-11-07-dwajoh</code> BUY 1 @ 5¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 1¢ | 450 | ×0.2^4 = 0.7 |

`side 451 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>ewc-usp-2028-11-07-wesmoo</code> BUY 1 @ 4¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 1¢ | 450 | ×0.2^3 = 3.6 |

`side 451 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>ewc-usp-2028-11-07-rokha</code> BUY 1 @ 7¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 2¢ | 1 | ×0.2^5 = 0.0 |
|  | 1¢ | 450 | ×0.2^6 = 0.0 |

`side 452 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 1 @ 12¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 1¢ | 5,950 | ×0.2^11 = 0.0 |

`side 5,951 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>ewc-usp-2028-11-07-dontru</code> BUY 1 @ 6¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 5¢ | 250 | ×0.2^1 = 50.0 |
|  | 1¢ | 200 | ×0.2^5 = 0.1 |

`side 451 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>ewc-usp-2028-11-07-markel</code> BUY 1 @ 10¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 450 | ×0.2^9 = 0.0 |

`side 452 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>ewc-usp-2028-11-07-micoba</code> BUY 1 @ 7¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 1¢ | 450 | ×0.2^6 = 0.0 |

`side 451 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>ewc-usp-2028-11-07-stasmi</code> BUY 1 @ 2¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 1¢ | 450 | ×0.2^1 = 90.0 |

`side 451 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 1 @ 4¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 3¢ | 1 | ×0.2^1 = 0.2 |
|  | 1¢ | 450 | ×0.2^3 = 3.6 |

`side 452 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 1 @ 8¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 3¢ | 1,250 | ×0.2^5 = 0.4 |
|  | 1¢ | 200 | ×0.2^7 = 0.0 |

`side 1,451 < target 20,000 → side pays nobody`  

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> BUY 1 @ 2¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 1¢ | 200 | ×0.1^1 = 20.0 |

`side 201 < target 2,000 → side pays nobody`  

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-stasmi</code> BUY 1 @ 5¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 2¢ | 80 | ×0.2^3 = 0.6 |
|  | 1¢ | 450 | ×0.2^4 = 0.7 |

`side 531 < target 20,000 → side pays nobody`  

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,084 resting) | ~55.6% | ~$41.73 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (631,205 resting) | ~27.0% | ~$20.24 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,070 resting) | ~24.9% | ~$18.69 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (277,297 resting) | ~10.4% | ~$7.80 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,747 resting) | ~27.7% | ~$6.92 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (35,662 resting) | ~10.5% | ~$2.63 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (279,789 resting) | ~2.1% | ~$1.56 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (73,654 resting) | ~36.3% | ~$1.51 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,401 resting) | ~1.9% | ~$1.44 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (359,296 resting) | ~21.9% | ~$1.37 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (65,519 resting) | ~17.8% | ~$1.11 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (891,073 resting) | ~1.4% | ~$1.08 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $1,678.09 |
| Skipped | $1.41 |
| **Total earned** | **$3,567.53** |

2562 reward rows · 43 days with rewards · 550 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-14 ⚠️ multi-day pending bucket | $274.59 | `██████████` |
| 2026-08-13 | $223.24 | `████████` |
| 2026-08-12 | $213.04 | `████████` |
| 2026-08-11 | $409.60 | `███████████████` |
| 2026-08-10 | $557.62 | `████████████████████` |
| 2026-08-09 | $62.24 | `██` |
| 2026-08-08 | $54.78 | `██` |
| 2026-08-07 | $60.33 | `██` |
| 2026-08-06 | $52.21 | `██` |
| 2026-08-05 | $31.46 | `█` |
| 2026-08-04 | $53.94 | `██` |
| 2026-08-03 | $44.81 | `██` |
| 2026-08-02 | $14.05 | `█` |
| 2026-08-01 | $52.30 | `██` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $2,104.21 | `████████████████████` |
| 2026-07 | $1,463.32 | `██████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $172.95 |
| `apdc-alito-2026-12-31` | $115.00 |
| `opdc-mcconnell-resign-2026-11-02` | $79.41 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $63.61 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $55.91 |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | $51.17 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.44 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.51 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.04 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `scc-senate-gop-2026-11-03-49` | $32.00 |
| `scc-senate-gop-2026-11-03-52` | $31.83 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-16 10:47 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:38 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:22 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:18 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:56 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:33 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:28 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:31 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:25 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:19 AM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
