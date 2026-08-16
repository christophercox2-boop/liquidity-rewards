# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-16 11:10 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$73.36/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-rep` — BUY at the best price, ~$40.79/day for 200 contracts. Runners-up: `ewc-usse-tx-2026-11-03-dem` (~$20.11/day), `ewc-usgub-ga-2026-11-03-dem` (~$18.69/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$73.36/day (~$3.06/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-uspres-nom-dem-2028-kamhar` | SELL | 17.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~99.8% of ask side (85,796 resting ≥ 20,000 ✓) ≈ $13.87/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jonste` | SELL | 13.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~97.5% of ask side (68,394 resting ≥ 20,000 ✓) ≈ $13.54/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | SELL | 16.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~94.0% of ask side (73,409 resting ≥ 20,000 ✓) ≈ $13.05/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 11.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~93.8% of bid side (180,493 resting ≥ 20,000 ✓) ≈ $13.02/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 9.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~39.4% of bid side (100,455 resting ≥ 20,000 ✓) ≈ $5.47/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-jossha` | BUY | 8.0¢ | 1 | 1 | $1,000.00 | ✅ scoring — ~38.7% of bid side (104,453 resting ≥ 20,000 ✓) ≈ $5.37/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 7.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~17.4% of bid side (70,453 resting ≥ 20,000 ✓) ≈ $2.41/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 7.0¢ | 1 | 3 | $1,000.00 | ✅ scoring — ~11.1% of bid side (104,453 resting ≥ 20,000 ✓) ≈ $1.55/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~9.7% of bid side (26,531 resting ≥ 20,000 ✓) ≈ $1.35/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-jossha` | BUY | 7.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~7.7% of bid side (104,453 resting ≥ 20,000 ✓) ≈ $1.07/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-markel` | BUY | 7.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~4.4% of bid side (166,454 resting ≥ 20,000 ✓) ≈ $0.61/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 7.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~4.4% of bid side (166,454 resting ≥ 20,000 ✓) ≈ $0.61/day (program pool ÷ 36 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 7.0¢ | 1 | 2 | $100.00 | ✅ scoring — ~4.2% of bid side (340,443 resting ≥ 5,000 ✓) ≈ $0.16/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 9.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~3.8% of bid side (180,493 resting ≥ 20,000 ✓) ≈ $0.52/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 7.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~1.6% of bid side (100,455 resting ≥ 20,000 ✓) ≈ $0.22/day (program pool ÷ 36 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 6.0¢ | 1 | 3 | $100.00 | ✅ scoring — ~0.8% of bid side (340,443 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 8.0¢ | 1 | 3 | $1,000.00 | ✅ scoring — ~0.8% of bid side (180,493 resting ≥ 20,000 ✓) ≈ $0.10/day (program pool ÷ 36 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 7.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~0.7% of bid side (415,452 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 12 markets) |
| `ewc-usp-2028-11-07-gavnew` | BUY | 10.0¢ | 1 | 6 | $1,000.00 | ✅ scoring — ~0.6% of bid side (96,485 resting ≥ 20,000 ✓) ≈ $0.08/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 17.0¢ | 1 | 1 | $1,000.00 | ✅ scoring — ~0.5% of ask side (72,683 resting ≥ 20,000 ✓) ≈ $0.07/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 5.0¢ | 1 | 5 | $1,000.00 | ✅ scoring — ~0.4% of bid side (104,453 resting ≥ 20,000 ✓) ≈ $0.06/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 13.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~0.4% of bid side (26,531 resting ≥ 20,000 ✓) ≈ $0.05/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 5.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~0.2% of bid side (166,454 resting ≥ 20,000 ✓) ≈ $0.02/day (program pool ÷ 36 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 5.0¢ | 1 | 4 | $100.00 | ✅ scoring — ~0.2% of bid side (340,443 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-kamhar` | SELL | 21.0¢ | 1 | 4 | $1,000.00 | ✅ scoring — ~0.2% of ask side (85,796 resting ≥ 20,000 ✓) ≈ $0.02/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-wesmoo` | BUY | 4.0¢ | 1 | 1 | $1,000.00 | ✅ scoring — ~0.1% of bid side (180,457 resting ≥ 20,000 ✓) ≈ $0.01/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 5.0¢ | 1 | 4 | $1,000.00 | ✅ scoring — ~0.1% of bid side (100,455 resting ≥ 20,000 ✓) ≈ $0.01/day (program pool ÷ 36 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 4.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~0.0% of bid side (340,377 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-markel` | BUY | 4.0¢ | 1 | 3 | $1,000.00 | ✅ scoring — ~0.0% of bid side (166,454 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 4.0¢ | 1 | 3 | $1,000.00 | ✅ scoring — ~0.0% of bid side (166,454 resting ≥ 20,000 ✓) ≈ $0.00/day (program pool ÷ 36 markets) |
| …and 104 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-uspres-nom-dem-2028-kamhar</code> SELL 1 @ 17¢ → $13.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 1 | ×0.2^4 = 0.0 |
|  | 25¢ | 1 | ×0.2^8 = 0.0 |
|  | 27¢ | 1 | ×0.2^10 = 0.0 |
|  | 28¢ | 1 | ×0.2^11 = 0.0 |
|  | 30¢ | 30 | ×0.2^13 = 0.0 |
|  | 31¢ | 50,967 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 99.8% = $13.87/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonste</code> SELL 1 @ 13¢ → $13.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 80 | ×0.2^8 = 0.0 |
|  | 22¢ | 49,542 | ×0.2^9 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 97.5%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 97.5% = $13.54/day`  

<details><summary>÷ 36 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 1 @ 9¢ → $5.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2 (1 yours) | ×0.2^0 = 2.2 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 5¢ | 1 | ×0.2^4 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
|  | 1¢ | 100,450 | ×0.2^8 = 0.3 |
| | | **Σ** | **2.5** |

`yours 1.0 / Σ 2.5 = 39.4%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 39.4% = $5.47/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> BUY 1 @ 7¢ → $2.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 3¢ | 2 | ×0.2^6 = 0.0 |
|  | 1¢ | 70,450 | ×0.2^8 = 0.2 |
| | | **Σ** | **0.2** |

`yours 0.0 / Σ 0.2 = 17.4%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 17.4% = $2.41/day`  

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 1 @ 7¢ → $1.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 1 @ 15¢ → $1.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 14¢ | 46 | ×0.2^1 = 9.2 |
|  | 13¢ | 1 | ×0.2^2 = 0.0 |
|  | 11¢ | 1 | ×0.2^4 = 0.0 |
|  | 8¢ | 1 | ×0.2^7 = 0.0 |
|  | 3¢ | 30 | ×0.2^12 = 0.0 |
|  | 2¢ | 26,250 | ×0.2^13 = 0.0 |
| | | **Σ** | **10.3** |

`yours 1.0 / Σ 10.3 = 9.7%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 9.7% = $1.35/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> BUY 1 @ 7¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (1 yours) | ×0.2^0 = 1.7 |
|  | 4¢ | 1 | ×0.2^3 = 0.0 |
|  | 3¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 66,000 | ×0.2^5 = 21.1 |
| | | **Σ** | **22.8** |

`yours 1.0 / Σ 22.8 = 4.4%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 4.4% = $0.61/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 1 @ 7¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (1 yours) | ×0.2^0 = 1.7 |
|  | 5¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^3 = 0.0 |
|  | 2¢ | 66,000 | ×0.2^5 = 21.1 |
| | | **Σ** | **22.9** |

`yours 1.0 / Σ 22.9 = 4.4%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 4.4% = $0.61/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 7¢ → $0.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^4 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
|  | 3¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 340,438 | ×0.2^8 = 0.9 |
| | | **Σ** | **0.9** |

`yours 0.0 / Σ 0.9 = 4.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 4.2% = $0.16/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 1 @ 7¢ → $0.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 2 | ×0.2^0 = 2.2 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 5¢ | 1 | ×0.2^4 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
|  | 1¢ | 100,450 | ×0.2^8 = 0.3 |
| | | **Σ** | **2.5** |

`yours 0.0 / Σ 2.5 = 1.6%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 1.6% = $0.22/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 6¢ → $0.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 6¢ | 1 (1 yours) | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^4 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
|  | 3¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 340,438 | ×0.2^8 = 0.9 |
| | | **Σ** | **0.9** |

`yours 0.0 / Σ 0.9 = 0.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.8% = $0.03/day`  

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
|  | 16¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 17¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 19¢ | 30 | ×0.2^3 = 0.2 |
|  | 20¢ | 23,470 | ×0.2^4 = 37.6 |
| | | **Σ** | **40.0** |

`yours 0.2 / Σ 40.0 = 0.5%`  
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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 1 @ 13¢ → $0.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 15¢ | 1 | ×0.2^0 = 1.0 |
|  | 14¢ | 46 | ×0.2^1 = 9.2 |
| ▶ | 13¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 11¢ | 1 | ×0.2^4 = 0.0 |
|  | 8¢ | 1 | ×0.2^7 = 0.0 |
|  | 3¢ | 30 | ×0.2^12 = 0.0 |
|  | 2¢ | 26,250 | ×0.2^13 = 0.0 |
| | | **Σ** | **10.3** |

`yours 0.0 / Σ 10.3 = 0.4%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 0.4% = $0.05/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 1 @ 5¢ → $0.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 2 | ×0.2^0 = 1.7 |
| ▶ | 5¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^3 = 0.0 |
|  | 2¢ | 66,000 | ×0.2^5 = 21.1 |
| | | **Σ** | **22.9** |

`yours 0.0 / Σ 22.9 = 0.2%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 5¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
| ▶ | 5¢ | 1 (1 yours) | ×0.2^4 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
|  | 3¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 340,438 | ×0.2^8 = 0.9 |
| | | **Σ** | **0.9** |

`yours 0.0 / Σ 0.9 = 0.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.2% = $0.01/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-kamhar</code> SELL 1 @ 21¢ → $0.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 21¢ | 1 (1 yours) | ×0.2^4 = 0.0 |
|  | 25¢ | 1 | ×0.2^8 = 0.0 |
|  | 27¢ | 1 | ×0.2^10 = 0.0 |
|  | 28¢ | 1 | ×0.2^11 = 0.0 |
|  | 30¢ | 30 | ×0.2^13 = 0.0 |
|  | 31¢ | 50,967 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.0** |

`yours 0.0 / Σ 1.0 = 0.2%`  
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
<details><summary><code>enwc-uspres-nom-dem-2028-wesmoo</code> BUY 1 @ 4¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 4 | ×0.2^0 = 3.6 |
| ▶ | 4¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 3¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 1 | ×0.2^3 = 0.0 |
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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 1 @ 5¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 2 | ×0.2^0 = 2.2 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 5¢ | 1 (1 yours) | ×0.2^4 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
|  | 1¢ | 100,450 | ×0.2^8 = 0.3 |
| | | **Σ** | **2.5** |

`yours 0.0 / Σ 2.5 = 0.1%`  
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
|  | 2¢ | 66,000 | ×0.2^5 = 21.1 |
| | | **Σ** | **22.8** |

`yours 0.0 / Σ 22.8 = 0.0%`  
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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 1 @ 4¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 2 | ×0.2^0 = 1.7 |
|  | 5¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 4¢ | 1 (1 yours) | ×0.2^3 = 0.0 |
|  | 2¢ | 66,000 | ×0.2^5 = 21.1 |
| | | **Σ** | **22.9** |

`yours 0.0 / Σ 22.9 = 0.0%`  
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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,312 resting) | ~54.4% | ~$40.79 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (631,210 resting) | ~26.8% | ~$20.11 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,070 resting) | ~24.9% | ~$18.69 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (277,223 resting) | ~10.4% | ~$7.81 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,723 resting) | ~27.7% | ~$6.92 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (35,637 resting) | ~10.7% | ~$2.67 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (73,654 resting) | ~36.3% | ~$1.51 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (281,778 resting) | ~1.9% | ~$1.46 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,401 resting) | ~1.9% | ~$1.44 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (374,132 resting) | ~22.6% | ~$1.41 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (59,168 resting) | ~20.9% | ~$1.31 |
| `ewc-usgub-mi-2026-11-03-dem` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (55,622 resting) | ~27.5% | ~$1.15 |

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
| 2026-08-16 11:10 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:03 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:59 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:47 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:38 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:22 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:18 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:56 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:33 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:28 AM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
