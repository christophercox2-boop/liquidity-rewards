# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-16 11:15 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$142.00/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-rep` — BUY at the best price, ~$40.54/day for 200 contracts. Runners-up: `ewc-usse-tx-2026-11-03-dem` (~$20.11/day), `ewc-usgub-ga-2026-11-03-dem` (~$18.69/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$142.00/day (~$5.92/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ewc-usp-2028-11-07-rokha` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~100.0% of bid side (30,000 resting ≥ 20,000 ✓) ≈ $13.89/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-kamhar` | SELL | 17.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~99.8% of ask side (85,796 resting ≥ 20,000 ✓) ≈ $13.87/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 13.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~99.2% of bid side (30,000 resting ≥ 20,000 ✓) ≈ $13.77/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 11.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~94.4% of bid side (180,493 resting ≥ 20,000 ✓) ≈ $13.12/day (program pool ÷ 36 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 9.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~81.3% of bid side (70,454 resting ≥ 20,000 ✓) ≈ $11.29/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-gavnew` | BUY | 14.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~77.9% of bid side (95,819 resting ≥ 20,000 ✓) ≈ $10.82/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-markel` | BUY | 9.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~72.0% of bid side (74,000 resting ≥ 20,000 ✓) ≈ $9.99/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-dontru` | BUY | 9.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~45.7% of bid side (59,665 resting ≥ 20,000 ✓) ≈ $6.35/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 8.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~33.8% of bid side (74,000 resting ≥ 20,000 ✓) ≈ $4.70/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 7.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~33.8% of bid side (30,000 resting ≥ 20,000 ✓) ≈ $4.69/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jonste` | SELL | 13.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~33.0% of ask side (68,347 resting ≥ 20,000 ✓) ≈ $4.59/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 1.0¢ | 10,000 | 6 | $1,000.00 | ✅ scoring — ~21.6% of bid side (30,000 resting ≥ 20,000 ✓) ≈ $3.00/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 1.0¢ | 9,546 | 6 | $1,000.00 | ✅ scoring — ~20.6% of bid side (30,000 resting ≥ 20,000 ✓) ≈ $2.86/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-markel` | BUY | 8.0¢ | 1 | 1 | $1,000.00 | ✅ scoring — ~14.4% of bid side (74,000 resting ≥ 20,000 ✓) ≈ $2.00/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-thomas` | BUY | 1.0¢ | 10,000 | 3 | $1,000.00 | ✅ scoring — ~13.5% of bid side (74,001 resting ≥ 20,000 ✓) ≈ $1.87/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-thomas` | BUY | 1.0¢ | 9,549 | 3 | $1,000.00 | ✅ scoring — ~12.9% of bid side (74,001 resting ≥ 20,000 ✓) ≈ $1.79/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-jossha` | BUY | 7.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~12.3% of bid side (104,454 resting ≥ 20,000 ✓) ≈ $1.71/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 7.0¢ | 1 | 3 | $1,000.00 | ✅ scoring — ~11.1% of bid side (104,454 resting ≥ 20,000 ✓) ≈ $1.55/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~9.7% of bid side (26,530 resting ≥ 20,000 ✓) ≈ $1.35/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 9.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~6.1% of bid side (70,001 resting ≥ 20,000 ✓) ≈ $0.85/day (program pool ÷ 36 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 1.0¢ | 10,000 | 7 | $1,000.00 | ✅ scoring — ~4.3% of bid side (74,000 resting ≥ 20,000 ✓) ≈ $0.60/day (program pool ÷ 36 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 7.0¢ | 1 | 2 | $100.00 | ✅ scoring — ~4.2% of bid side (340,443 resting ≥ 5,000 ✓) ≈ $0.16/day (pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 1.0¢ | 9,546 | 7 | $1,000.00 | ✅ scoring — ~4.1% of bid side (74,000 resting ≥ 20,000 ✓) ≈ $0.57/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-markel` | BUY | 7.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~3.8% of bid side (176,454 resting ≥ 20,000 ✓) ≈ $0.53/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 7.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~3.8% of bid side (176,454 resting ≥ 20,000 ✓) ≈ $0.53/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 9.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~3.8% of bid side (180,493 resting ≥ 20,000 ✓) ≈ $0.52/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 7.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~3.3% of bid side (70,454 resting ≥ 20,000 ✓) ≈ $0.45/day (program pool ÷ 36 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 16.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~2.9% of ask side (70,183 resting ≥ 20,000 ✓) ≈ $0.40/day (program pool ÷ 36 markets) |
| …and 144 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ewc-usp-2028-11-07-rokha</code> BUY 1 @ 15¢ → $13.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 6¢ | 1 | ×0.2^9 = 0.0 |
|  | 4¢ | 1 | ×0.2^11 = 0.0 |
|  | 2¢ | 1 | ×0.2^13 = 0.0 |
|  | 1¢ | 29,996 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 100.0% = $13.89/day`  

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
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha` ← this one
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 1 @ 13¢ → $13.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 7¢ | 1 | ×0.2^6 = 0.0 |
|  | 3¢ | 1,250 | ×0.2^10 = 0.0 |
|  | 1¢ | 28,747 | ×0.2^12 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.2%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 99.2% = $13.77/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 11¢ → $13.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
|  | 6¢ | 1 | ×0.2^5 = 0.0 |
|  | 2¢ | 30 | ×0.2^9 = 0.0 |
|  | 1¢ | 180,460 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 94.4%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 94.4% = $13.12/day`  

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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $5.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> BUY 1 @ 9¢ → $11.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 3¢ | 2 | ×0.2^6 = 0.0 |
|  | 1¢ | 70,450 | ×0.2^8 = 0.2 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 81.3%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 81.3% = $11.29/day`  

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
<details><summary><code>ewc-usp-2028-11-07-gavnew</code> BUY 1 @ 14¢ → $10.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 14¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 10¢ | 1 | ×0.2^6 = 0.0 |
|  | 8¢ | 1 | ×0.2^8 = 0.0 |
|  | 6¢ | 9,366 | ×0.2^10 = 0.0 |
|  | 5¢ | 16,000 | ×0.2^11 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 77.9%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 77.9% = $10.82/day`  

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
<details><summary><code>ewc-usp-2028-11-07-markel</code> BUY 1 @ 9¢ → $9.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 1 | ×0.2^1 = 0.2 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
|  | 1¢ | 73,997 | ×0.2^8 = 0.2 |
| | | **Σ** | **1.4** |

`yours 1.0 / Σ 1.4 = 72.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 72.0% = $9.99/day`  

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
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-dontru</code> BUY 1 @ 9¢ → $6.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 5¢ | 250 | ×0.2^4 = 0.4 |
|  | 3¢ | 9,666 | ×0.2^6 = 0.6 |
|  | 1¢ | 49,747 | ×0.2^8 = 0.1 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 45.7%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 45.7% = $6.35/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 1 @ 8¢ → $4.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 5¢ | 1 | ×0.2^3 = 0.0 |
|  | 2¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 73,996 | ×0.2^7 = 0.9 |
| | | **Σ** | **3.0** |

`yours 1.0 / Σ 3.0 = 33.8%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 33.8% = $4.70/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 1 @ 7¢ → $4.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 5¢ | 1 | ×0.2^2 = 0.0 |
|  | 3¢ | 2 | ×0.2^4 = 0.0 |
|  | 1¢ | 29,996 | ×0.2^6 = 1.9 |
| | | **Σ** | **3.0** |

`yours 1.0 / Σ 3.0 = 33.8%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 33.8% = $4.69/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonste</code> SELL 1 @ 13¢ → $4.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 3 (1 yours) | ×0.2^0 = 3.0 |
|  | 17¢ | 1 | ×0.2^4 = 0.0 |
|  | 21¢ | 30 | ×0.2^8 = 0.0 |
|  | 22¢ | 49,542 | ×0.2^9 = 0.0 |
| | | **Σ** | **3.0** |

`yours 1.0 / Σ 3.0 = 33.0%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 33.0% = $4.59/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 10,000 @ 1¢ → $3.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 1 | ×0.2^0 = 1.0 |
|  | 5¢ | 1 | ×0.2^2 = 0.0 |
|  | 3¢ | 2 | ×0.2^4 = 0.0 |
| ▶ | 1¢ | 29,996 (10,000 yours) | ×0.2^6 = 1.9 |
| | | **Σ** | **3.0** |

`yours 0.6 / Σ 3.0 = 21.6%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 21.6% = $3.00/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 9,546 @ 1¢ → $2.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 1 | ×0.2^0 = 1.0 |
|  | 5¢ | 1 | ×0.2^2 = 0.0 |
|  | 3¢ | 2 | ×0.2^4 = 0.0 |
| ▶ | 1¢ | 29,996 (9,546 yours) | ×0.2^6 = 1.9 |
| | | **Σ** | **3.0** |

`yours 0.6 / Σ 3.0 = 20.6%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 20.6% = $2.86/day`  

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
<details><summary><code>ewc-usp-2028-11-07-markel</code> BUY 1 @ 8¢ → $2.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 8¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
|  | 1¢ | 73,997 | ×0.2^8 = 0.2 |
| | | **Σ** | **1.4** |

`yours 0.2 / Σ 1.4 = 14.4%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 14.4% = $2.00/day`  

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
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-thomas</code> BUY 10,000 @ 1¢ → $1.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 1 | ×0.2^0 = 1.0 |
|  | 2¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 1¢ | 73,999 (10,000 yours) | ×0.2^3 = 592.0 |
| | | **Σ** | **593.0** |

`yours 80.0 / Σ 593.0 = 13.5%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 13.5% = $1.87/day`  

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
<details><summary><code>ewc-usp-2028-11-07-thomas</code> BUY 9,549 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 1 | ×0.2^0 = 1.0 |
|  | 2¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 1¢ | 73,999 (9,549 yours) | ×0.2^3 = 592.0 |
| | | **Σ** | **593.0** |

`yours 76.4 / Σ 593.0 = 12.9%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 12.9% = $1.79/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> BUY 1 @ 7¢ → $1.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 1 | ×0.2^5 = 0.0 |
|  | 2¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 104,450 | ×0.2^8 = 0.3 |
| | | **Σ** | **0.3** |

`yours 0.0 / Σ 0.3 = 12.3%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 12.3% = $1.71/day`  

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 1 @ 7¢ → $1.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 4¢ | 1 | ×0.2^6 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 1 @ 9¢ → $0.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 0.6 |
| ▶ | 9¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 6¢ | 1 | ×0.2^5 = 0.0 |
|  | 1¢ | 69,997 | ×0.2^10 = 0.0 |
| | | **Σ** | **0.7** |

`yours 0.0 / Σ 0.7 = 6.1%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 6.1% = $0.85/day`  

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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 10,000 @ 1¢ → $0.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 2 | ×0.2^0 = 2.0 |
|  | 5¢ | 1 | ×0.2^3 = 0.0 |
|  | 2¢ | 1 | ×0.2^6 = 0.0 |
| ▶ | 1¢ | 73,996 (10,000 yours) | ×0.2^7 = 0.9 |
| | | **Σ** | **3.0** |

`yours 0.1 / Σ 3.0 = 4.3%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 4.3% = $0.60/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

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
| | | **Σ** | **1.0** |

`yours 0.0 / Σ 1.0 = 4.2%`  
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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 9,546 @ 1¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 2 | ×0.2^0 = 2.0 |
|  | 5¢ | 1 | ×0.2^3 = 0.0 |
|  | 2¢ | 1 | ×0.2^6 = 0.0 |
| ▶ | 1¢ | 73,996 (9,546 yours) | ×0.2^7 = 0.9 |
| | | **Σ** | **3.0** |

`yours 0.1 / Σ 3.0 = 4.1%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 4.1% = $0.57/day`  

<details><summary>÷ 36 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 1 @ 7¢ → $0.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (1 yours) | ×0.2^0 = 1.7 |
|  | 5¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^3 = 0.0 |
|  | 2¢ | 76,000 | ×0.2^5 = 24.3 |
| | | **Σ** | **26.1** |

`yours 1.0 / Σ 26.1 = 3.8%`  
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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 9¢ → $0.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 9¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 6¢ | 1 | ×0.2^5 = 0.0 |
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
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> BUY 1 @ 7¢ → $0.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 7¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 3¢ | 2 | ×0.2^6 = 0.0 |
|  | 1¢ | 70,450 | ×0.2^8 = 0.2 |
| | | **Σ** | **1.2** |

`yours 0.0 / Σ 1.2 = 3.3%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 3.3% = $0.45/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 1 @ 16¢ → $0.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 17¢ | 1 | ×0.2^1 = 0.2 |
|  | 18¢ | 1 | ×0.2^2 = 0.0 |
|  | 19¢ | 30 | ×0.2^3 = 0.2 |
|  | 20¢ | 20,970 | ×0.2^4 = 33.6 |
| | | **Σ** | **35.0** |

`yours 1.0 / Σ 35.0 = 2.9%`  
`$1,000 ÷ 36 ÷ 2 = $13.89 × 2.9% = $0.40/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,316 resting) | ~54.1% | ~$40.54 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (631,210 resting) | ~26.8% | ~$20.11 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,070 resting) | ~24.9% | ~$18.69 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (277,294 resting) | ~10.4% | ~$7.80 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,720 resting) | ~27.8% | ~$6.95 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (97,747 resting) | ~60.8% | ~$3.80 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (35,637 resting) | ~10.7% | ~$2.67 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (23,532 resting) | ~4.0% | ~$2.00 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (279,640 resting) | ~2.1% | ~$1.58 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (73,654 resting) | ~36.3% | ~$1.51 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (887,337 resting) | ~2.0% | ~$1.49 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,401 resting) | ~1.9% | ~$1.44 |

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
| 2026-08-16 11:15 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:10 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:03 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:59 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:47 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:38 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:22 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:18 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:56 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 9:33 AM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
