# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-16 10:59 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$57.81/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-rep` — BUY at the best price, ~$44.21/day for 200 contracts. Runners-up: `ewc-usse-tx-2026-11-03-dem` (~$20.24/day), `ewc-usgub-ga-2026-11-03-dem` (~$18.69/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$57.81/day (~$2.41/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-uspres-nom-dem-2028-kamhar` | SELL | 21.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~99.5% of ask side (85,791 resting ≥ 20,000 ✓) ≈ $13.82/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | SELL | 16.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~94.0% of ask side (73,408 resting ≥ 20,000 ✓) ≈ $13.05/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 11.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~93.8% of bid side (180,493 resting ≥ 20,000 ✓) ≈ $13.02/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-jossha` | BUY | 8.0¢ | 1 | 1 | $1,000.00 | ✅ scoring — ~38.7% of bid side (104,453 resting ≥ 20,000 ✓) ≈ $5.37/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 9.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~37.0% of bid side (180,453 resting ≥ 20,000 ✓) ≈ $5.14/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 8.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~16.1% of bid side (76,481 resting ≥ 20,000 ✓) ≈ $2.23/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 7.0¢ | 1 | 3 | $1,000.00 | ✅ scoring — ~11.1% of bid side (104,454 resting ≥ 20,000 ✓) ≈ $1.55/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 7.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~7.8% of bid side (180,454 resting ≥ 20,000 ✓) ≈ $1.08/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-jossha` | BUY | 7.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~7.7% of bid side (104,453 resting ≥ 20,000 ✓) ≈ $1.07/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-markel` | BUY | 7.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~3.8% of bid side (176,454 resting ≥ 20,000 ✓) ≈ $0.53/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 9.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~3.8% of bid side (180,493 resting ≥ 20,000 ✓) ≈ $0.52/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 8.0¢ | 1 | 3 | $1,000.00 | ✅ scoring — ~0.8% of bid side (180,493 resting ≥ 20,000 ✓) ≈ $0.10/day (program pool ÷ 36 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 7.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~0.7% of bid side (415,452 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 12 markets) |
| `ewc-usp-2028-11-07-gavnew` | BUY | 10.0¢ | 1 | 6 | $1,000.00 | ✅ scoring — ~0.6% of bid side (96,485 resting ≥ 20,000 ✓) ≈ $0.08/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 17.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~0.5% of ask side (72,680 resting ≥ 20,000 ✓) ≈ $0.07/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 5.0¢ | 1 | 5 | $1,000.00 | ✅ scoring — ~0.4% of bid side (104,454 resting ≥ 20,000 ✓) ≈ $0.06/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 5.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~0.2% of bid side (176,452 resting ≥ 20,000 ✓) ≈ $0.02/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-wesmoo` | BUY | 4.0¢ | 1 | 1 | $1,000.00 | ✅ scoring — ~0.1% of bid side (180,455 resting ≥ 20,000 ✓) ≈ $0.01/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 4.0¢ | 1 | 5 | $1,000.00 | ✅ scoring — ~0.1% of bid side (180,454 resting ≥ 20,000 ✓) ≈ $0.01/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 5.0¢ | 1 | 4 | $1,000.00 | ✅ scoring — ~0.1% of bid side (180,453 resting ≥ 20,000 ✓) ≈ $0.01/day (program pool ÷ 36 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 4.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~0.0% of bid side (340,377 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-markel` | BUY | 4.0¢ | 1 | 3 | $1,000.00 | ✅ scoring — ~0.0% of bid side (176,454 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-gavnew` | BUY | 8.0¢ | 1 | 8 | $1,000.00 | ✅ scoring — ~0.0% of bid side (96,485 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 3.0¢ | 1 | 7 | $1,000.00 | ✅ scoring — ~0.0% of bid side (104,454 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 3.0¢ | 1 | 6 | $1,000.00 | ✅ scoring — ~0.0% of bid side (180,454 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 3.0¢ | 1 | 6 | $1,000.00 | ✅ scoring — ~0.0% of bid side (180,454 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-micoba` | SELL | 16.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~0.0% of ask side (76,881 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-stasmi` | SELL | 18.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~0.0% of ask side (62,590 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 36 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 3.0¢ | 1 | 1 | $100.00 | ✅ scoring — ~0.0% of bid side (340,377 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-kamhar` | SELL | 27.0¢ | 1 | 6 | $1,000.00 | ✅ scoring — ~0.0% of ask side (85,791 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 36 markets) |
| …and 78 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-uspres-nom-dem-2028-kamhar</code> SELL 1 @ 21¢ → $13.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 27¢ | 1 | ×0.2^6 = 0.0 |
|  | 30¢ | 30 | ×0.2^9 = 0.0 |
|  | 31¢ | 50,967 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.5%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 99.5% = $13.82/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar` ← this one
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> SELL 1 @ 16¢ → $13.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 23¢ | 30 | ×0.2^7 = 0.0 |
|  | 24¢ | 24,871 | ×0.2^8 = 0.1 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 94.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 94.0% = $13.05/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 11¢ → $13.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 2¢ | 30 | ×0.2^9 = 0.0 |
|  | 1¢ | 180,460 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 93.8%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 93.8% = $13.02/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> BUY 1 @ 8¢ → $5.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 8¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 104,450 | ×0.2^8 = 0.3 |
| | | **Σ** | **0.5** |

`yours 0.2 / Σ 0.5 = 38.7%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 38.7% = $5.37/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 1 @ 9¢ → $5.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2 (1 yours) | ×0.2^0 = 2.2 |
|  | 5¢ | 1 | ×0.2^4 = 0.0 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **2.7** |

`yours 1.0 / Σ 2.7 = 37.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 37.0% = $5.14/day`  

<details><summary>÷ 36 markets in this race (14 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 1 @ 8¢ → $2.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.2^0 = 1.3 |
|  | 3¢ | 30 | ×0.2^5 = 0.0 |
|  | 2¢ | 76,250 | ×0.2^6 = 4.9 |
| | | **Σ** | **6.2** |

`yours 1.0 / Σ 6.2 = 16.1%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 16.1% = $2.23/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 1 @ 7¢ → $1.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 3¢ | 1 | ×0.2^7 = 0.0 |
|  | 2¢ | 1 | ×0.2^8 = 0.0 |
|  | 1¢ | 104,450 | ×0.2^9 = 0.1 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 11.1%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 11.1% = $1.55/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> BUY 1 @ 7¢ → $1.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
|  | 3¢ | 2 | ×0.2^6 = 0.0 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **0.5** |

`yours 0.0 / Σ 0.5 = 7.8%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 7.8% = $1.08/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> BUY 1 @ 7¢ → $1.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
|  | 8¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 2¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 104,450 | ×0.2^8 = 0.3 |
| | | **Σ** | **0.5** |

`yours 0.0 / Σ 0.5 = 7.7%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 7.7% = $1.07/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> BUY 1 @ 7¢ → $0.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (1 yours) | ×0.2^0 = 1.7 |
|  | 4¢ | 1 | ×0.2^3 = 0.0 |
|  | 3¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 76,000 | ×0.2^5 = 24.3 |
| | | **Σ** | **26.0** |

`yours 1.0 / Σ 26.0 = 3.8%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 3.8% = $0.53/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 9¢ → $0.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 9¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 2¢ | 30 | ×0.2^9 = 0.0 |
|  | 1¢ | 180,460 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.1** |

`yours 0.0 / Σ 1.1 = 3.8%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 3.8% = $0.52/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 8¢ → $0.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 1.0 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 8¢ | 1 (1 yours) | ×0.2^3 = 0.0 |
|  | 2¢ | 30 | ×0.2^9 = 0.0 |
|  | 1¢ | 180,460 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.1** |

`yours 0.0 / Σ 1.1 = 0.8%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.8% = $0.10/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 1 @ 7¢ → $0.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 4¢ | 1 | ×0.2^3 = 0.0 |
|  | 3¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 415,249 | ×0.2^5 = 132.9 |
| | | **Σ** | **133.9** |

`yours 1.0 / Σ 133.9 = 0.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.7% = $0.03/day`  

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
<details><summary><code>ewc-usp-2028-11-07-gavnew</code> BUY 1 @ 10¢ → $0.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 10¢ | 1 (1 yours) | ×0.2^6 = 0.0 |
|  | 8¢ | 1 | ×0.2^8 = 0.0 |
|  | 7¢ | 1 | ×0.2^9 = 0.0 |
|  | 6¢ | 10,032 | ×0.2^10 = 0.0 |
|  | 5¢ | 16,000 | ×0.2^11 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 0.6%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.6% = $0.08/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 1 @ 17¢ → $0.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 19¢ | 30 | ×0.2^2 = 1.2 |
|  | 20¢ | 23,470 | ×0.2^3 = 187.8 |
| | | **Σ** | **190.0** |

`yours 1.0 / Σ 190.0 = 0.5%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.5% = $0.07/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 1 @ 5¢ → $0.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
| ▶ | 5¢ | 1 (1 yours) | ×0.2^5 = 0.0 |
|  | 3¢ | 1 | ×0.2^7 = 0.0 |
|  | 2¢ | 1 | ×0.2^8 = 0.0 |
|  | 1¢ | 104,450 | ×0.2^9 = 0.1 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 0.4%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.4% = $0.06/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 1 @ 5¢ → $0.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 1 | ×0.2^0 = 0.7 |
| ▶ | 5¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 2¢ | 76,000 | ×0.2^5 = 24.3 |
| | | **Σ** | **25.1** |

`yours 0.0 / Σ 25.1 = 0.2%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.2% = $0.02/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-wesmoo</code> BUY 1 @ 4¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 4 | ×0.2^0 = 3.6 |
| ▶ | 4¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 1¢ | 180,450 | ×0.2^4 = 288.7 |
| | | **Σ** | **292.5** |

`yours 0.2 / Σ 292.5 = 0.1%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.1% = $0.01/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> BUY 1 @ 4¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 4¢ | 1 (1 yours) | ×0.2^5 = 0.0 |
|  | 3¢ | 2 | ×0.2^6 = 0.0 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **0.5** |

`yours 0.0 / Σ 0.5 = 0.1%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.1% = $0.01/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 1 @ 5¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 2 | ×0.2^0 = 2.2 |
| ▶ | 5¢ | 1 (1 yours) | ×0.2^4 = 0.0 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **2.7** |

`yours 0.0 / Σ 2.7 = 0.1%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.1% = $0.01/day`  

<details><summary>÷ 36 markets in this race (14 known) — tap to list</summary>

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 1 @ 4¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 3¢ | 1 | ×0.2^1 = 0.2 |
|  | 2¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 340,374 | ×0.2^3 = 2,723.0 |
| | | **Σ** | **2,724.2** |

`yours 1.0 / Σ 2,724.2 = 0.0%`  
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
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> BUY 1 @ 4¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 2 | ×0.2^0 = 1.7 |
| ▶ | 4¢ | 1 (1 yours) | ×0.2^3 = 0.0 |
|  | 3¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 76,000 | ×0.2^5 = 24.3 |
| | | **Σ** | **26.0** |

`yours 0.0 / Σ 26.0 = 0.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.0% = $0.00/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-gavnew</code> BUY 1 @ 8¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
|  | 10¢ | 1 | ×0.2^6 = 0.0 |
| ▶ | 8¢ | 1 (1 yours) | ×0.2^8 = 0.0 |
|  | 7¢ | 1 | ×0.2^9 = 0.0 |
|  | 6¢ | 10,032 | ×0.2^10 = 0.0 |
|  | 5¢ | 16,000 | ×0.2^11 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 0.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.0% = $0.00/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 1 @ 3¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
| ▶ | 3¢ | 1 (1 yours) | ×0.2^7 = 0.0 |
|  | 2¢ | 1 | ×0.2^8 = 0.0 |
|  | 1¢ | 104,450 | ×0.2^9 = 0.1 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 0.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.0% = $0.00/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

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
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
| ▶ | 3¢ | 2 (1 yours) | ×0.2^6 = 0.0 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **0.5** |

`yours 0.0 / Σ 0.5 = 0.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.0% = $0.00/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> BUY 1 @ 3¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
| ▶ | 3¢ | 2 (1 yours) | ×0.2^6 = 0.0 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **0.5** |

`yours 0.0 / Σ 0.5 = 0.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.0% = $0.00/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-micoba</code> SELL 1 @ 16¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 51 (1 yours) | ×0.2^0 = 51.0 |
|  | 17¢ | 42,571 | ×0.2^1 = 8,514.2 |
| | | **Σ** | **8,565.2** |

`yours 1.0 / Σ 8,565.2 = 0.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.0% = $0.00/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-stasmi</code> SELL 1 @ 18¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 345 (1 yours) | ×0.2^0 = 345.0 |
|  | 19¢ | 43,474 | ×0.2^1 = 8,694.8 |
| | | **Σ** | **9,039.8** |

`yours 1.0 / Σ 9,039.8 = 0.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.0% = $0.00/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
16. `enwc-uspres-nom-dem-2028-stasmi` ← this one
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 1 @ 3¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 3¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 2¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 340,374 | ×0.2^3 = 2,723.0 |
| | | **Σ** | **2,724.2** |

`yours 0.2 / Σ 2,724.2 = 0.0%`  
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
<details><summary><code>enwc-uspres-nom-dem-2028-kamhar</code> SELL 1 @ 27¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 27¢ | 1 (1 yours) | ×0.2^6 = 0.0 |
|  | 30¢ | 30 | ×0.2^9 = 0.0 |
|  | 31¢ | 50,967 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.0** |

`yours 0.0 / Σ 1.0 = 0.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.0% = $0.00/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar` ← this one
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,065 resting) | ~58.9% | ~$44.21 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (631,205 resting) | ~27.0% | ~$20.24 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,070 resting) | ~24.9% | ~$18.69 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (277,249 resting) | ~10.4% | ~$7.81 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,721 resting) | ~27.8% | ~$6.94 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (35,637 resting) | ~10.7% | ~$2.67 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (58,654 resting) | ~36.3% | ~$1.51 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (887,310 resting) | ~2.0% | ~$1.49 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (281,931 resting) | ~2.0% | ~$1.47 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,401 resting) | ~1.9% | ~$1.44 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (359,299 resting) | ~21.9% | ~$1.37 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (65,519 resting) | ~17.8% | ~$1.11 |

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
| 2026-08-16 10:59 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:47 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:38 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:22 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:18 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:56 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:33 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:28 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:31 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:25 AM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
