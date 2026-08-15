# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-15 7:22 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$1,256.81/day estimated (ceiling, not promise — details below)

**Earned:** $3,292.94 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-13: **$223.24** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-12: **$213.04** · 2026-08-11: **$409.60** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usse-oh-2026-11-03-dem` — BUY at the best price, ~$9.45/day for 200 contracts. Runners-up: `ewc-usgub-wi-2026-11-03-dem` (~$6.13/day), `ewc-usgub-nv-2026-11-03-rep` (~$4.36/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$1,256.81/day (~$52.37/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (92,067 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 24.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,759 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `ussewc-usse-nj-2026-11-03-dem` | BUY | 93.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,225 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | BUY | 87.0¢ | 39 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (300,819 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 15.0¢ | 15 | 0 | $1,000.00 | ✅ scoring — ~100.0% of ask side (54,985 resting ≥ 20,000 ✓) ≈ $29.41/day (pool ÷ 17 markets) |
| `ussewc-usse-ms-2026-11-03-rep` | SELL | 90.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,385 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 20.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,879 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,509 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-kamhar` | SELL | 14.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~100.0% of ask side (62,462 resting ≥ 20,000 ✓) ≈ $18.51/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 16.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~98.9% of bid side (20,602 resting ≥ 20,000 ✓) ≈ $18.31/day (pool ÷ 27 markets) |
| `usgubewc-usgub-mn-2026-11-03-dem` | SELL | 92.0¢ | 23 | 0 | $25.00 | ✅ scoring — ~98.2% of ask side (5,161 resting ≥ 2,000 ✓) ≈ $6.14/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~93.0% of ask side (130,768 resting ≥ 2,000 ✓) ≈ $5.81/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-rep` | SELL | 9.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~91.7% of ask side (196,098 resting ≥ 2,000 ✓) ≈ $5.73/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 41.0¢ | 5 | 2 | $100.00 | ✅ scoring — ~90.9% of ask side (82,377 resting ≥ 5,000 ✓) ≈ $3.79/day (pool ÷ 12 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 18.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~90.9% of bid side (20,554 resting ≥ 20,000 ✓) ≈ $16.83/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-dwajoh` | BUY | 13.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~89.8% of bid side (20,482 resting ≥ 20,000 ✓) ≈ $16.62/day (pool ÷ 27 markets) |
| `usgubewc-usgub-co-2026-11-03-rep` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,781 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `ussewc-usse-fl-2026-11-03-dem` | SELL | 22.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (133,037 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 7.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,753 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-stasmi` | BUY | 10.0¢ | 3 | 0 | $1,000.00 | ✅ scoring — ~88.8% of bid side (60,459 resting ≥ 20,000 ✓) ≈ $16.44/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | SELL | 22.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~88.3% of ask side (60,493 resting ≥ 20,000 ✓) ≈ $25.96/day (pool ÷ 17 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~86.5% of ask side (5,338 resting ≥ 2,000 ✓) ≈ $5.41/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rokha` | BUY | 16.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~86.2% of bid side (20,461 resting ≥ 20,000 ✓) ≈ $15.96/day (pool ÷ 27 markets) |
| `usgubewc-usgub-vt-2026-11-03-dem` | SELL | 15.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (330,178 resting ≥ 2,000 ✓) ≈ $5.21/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-markel` | BUY | 14.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~82.8% of bid side (20,615 resting ≥ 20,000 ✓) ≈ $15.33/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jossha` | BUY | 9.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~79.4% of bid side (114,456 resting ≥ 20,000 ✓) ≈ $14.70/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 10.0¢ | 24 | 0 | $1,000.00 | ✅ scoring — ~78.8% of bid side (80,483 resting ≥ 20,000 ✓) ≈ $14.58/day (pool ÷ 27 markets) |
| `usgubewc-usgub-al-2026-11-03-dem` | SELL | 14.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~78.1% of ask side (133,762 resting ≥ 2,000 ✓) ≈ $4.88/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 7.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~73.9% of bid side (90,502 resting ≥ 5,000 ✓) ≈ $2.84/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 25.0¢ | 5 | 0 | $1,000.00 | ✅ scoring — ~73.2% of bid side (31,632 resting ≥ 20,000 ✓) ≈ $21.52/day (pool ÷ 17 markets) |
| …and 2626 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 8¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 80,716 | ×0.2^89 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 25 @ 24¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 50¢ | 74 | ×0.2^26 = 0.0 |
|  | 97¢ | 80,459 | ×0.2^73 = 0.0 |
| | | **Σ** | **25.0** |

`yours 25.0 / Σ 25.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>ussewc-usse-nj-2026-11-03-dem</code> BUY 25 @ 93¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 25 (25 yours) | ×0.1^0 = 25.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **25.0** |

`yours 25.0 / Σ 25.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nj-2026-11-03-dem` ← this one
2. `ussewc-usse-nj-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> BUY 39 @ 87¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 39 (39 yours) | ×0.1^0 = 39.0 |
|  | 80¢ | 50 | ×0.1^7 = 0.0 |
|  | 79¢ | 30 | ×0.1^8 = 0.0 |
|  | 54¢ | 500 | ×0.1^33 = 0.0 |
|  | 2¢ | 300,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **39.0** |

`yours 39.0 / Σ 39.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 15 @ 15¢ → $29.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 24¢ | 1 | ×0.2^9 = 0.0 |
|  | 25¢ | 14 | ×0.2^10 = 0.0 |
|  | 30¢ | 46,429 | ×0.2^15 = 0.0 |
| | | **Σ** | **15.0** |

`yours 15.0 / Σ 15.0 = 100.0%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 100.0% = $29.41/day`  

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
<details><summary><code>ussewc-usse-ms-2026-11-03-rep</code> SELL 15 @ 90¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 15 (15 yours) | ×0.1^0 = 15.0 |
|  | 98¢ | 1,226 | ×0.1^8 = 0.0 |
|  | 99¢ | 1,144 | ×0.1^9 = 0.0 |
| | | **Σ** | **15.0** |

`yours 15.0 / Σ 15.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem`
2. `ussewc-usse-ms-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 5 @ 20¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 28¢ | 5 | ×0.2^8 = 0.0 |
|  | 50¢ | 140 | ×0.2^30 = 0.0 |
|  | 56¢ | 56 | ×0.2^36 = 0.0 |
|  | 97¢ | 80,472 | ×0.2^77 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 30 @ 2¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 30 (30 yours) | ×0.1^0 = 30.0 |
|  | 5¢ | 4 | ×0.1^3 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^96 = 0.0 |
| | | **Σ** | **30.0** |

`yours 30.0 / Σ 30.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-kamhar</code> SELL 1 @ 14¢ → $18.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 2 | ×0.2^7 = 0.0 |
|  | 25¢ | 21,455 | ×0.2^11 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 100.0% = $18.51/day`  

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
14. `ewc-usp-2028-11-07-kamhar` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 1 @ 16¢ → $18.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 12¢ | 2 | ×0.2^4 = 0.0 |
|  | 10¢ | 121 | ×0.2^6 = 0.0 |
|  | 3¢ | 1 | ×0.2^13 = 0.0 |
|  | 2¢ | 1 | ×0.2^14 = 0.0 |
|  | 1¢ | 20,476 | ×0.2^15 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.9%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 98.9% = $18.31/day`  

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
<details><summary><code>usgubewc-usgub-mn-2026-11-03-dem</code> SELL 23 @ 92¢ → $6.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 23 (23 yours) | ×0.1^0 = 23.0 |
|  | 94¢ | 41 | ×0.1^2 = 0.4 |
|  | 99¢ | 5,097 | ×0.1^7 = 0.0 |
| | | **Σ** | **23.4** |

`yours 23.0 / Σ 23.4 = 98.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.2% = $6.14/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-mn-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $5.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 43 (40 yours) | ×0.1^0 = 43.0 |
|  | 98¢ | 130,500 | ×0.1^94 = 0.0 |
| | | **Σ** | **43.0** |

`yours 40.0 / Σ 43.0 = 93.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.0% = $5.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-rep</code> SELL 11 @ 9¢ → $5.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 12 (11 yours) | ×0.1^0 = 12.0 |
|  | 14¢ | 10 | ×0.1^5 = 0.0 |
|  | 15¢ | 101 | ×0.1^6 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^89 = 0.0 |
| | | **Σ** | **12.0** |

`yours 11.0 / Σ 12.0 = 91.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 91.7% = $5.73/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem`
2. `usgubewc-usgub-mn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 5 @ 41¢ → $3.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 39¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 41¢ | 5 (5 yours) | ×0.2^2 = 0.2 |
|  | 52¢ | 100 | ×0.2^13 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^59 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.2 / Σ 0.2 = 90.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 90.9% = $3.79/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210` ← this one
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 18¢ → $16.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 11¢ | 1 | ×0.2^7 = 0.0 |
|  | 6¢ | 1 | ×0.2^12 = 0.0 |
|  | 1¢ | 20,551 | ×0.2^17 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.9%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 90.9% = $16.83/day`  

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
<details><summary><code>ewc-usp-2028-11-07-dwajoh</code> BUY 1 @ 13¢ → $16.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 9¢ | 2 | ×0.2^4 = 0.0 |
|  | 8¢ | 2 | ×0.2^5 = 0.0 |
|  | 2¢ | 1 | ×0.2^11 = 0.0 |
|  | 1¢ | 20,476 | ×0.2^12 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 89.8%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 89.8% = $16.62/day`  

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
<details><summary><code>usgubewc-usgub-co-2026-11-03-rep</code> SELL 50 @ 7¢ → $5.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 56 (50 yours) | ×0.1^0 = 56.0 |
|  | 98¢ | 130,500 | ×0.1^91 = 0.0 |
| | | **Σ** | **56.0** |

`yours 50.0 / Σ 56.0 = 89.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.3% = $5.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem`
2. `usgubewc-usgub-co-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-fl-2026-11-03-dem</code> SELL 25 @ 22¢ → $5.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 28 (25 yours) | ×0.1^0 = 28.0 |
|  | 98¢ | 132,784 | ×0.1^76 = 0.0 |
| | | **Σ** | **28.0** |

`yours 25.0 / Σ 28.0 = 89.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.3% = $5.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem` ← this one
2. `ussewc-usse-fl-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 25 @ 7¢ → $5.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 28 (25 yours) | ×0.1^0 = 28.0 |
|  | 98¢ | 130,500 | ×0.1^91 = 0.0 |
| | | **Σ** | **28.0** |

`yours 25.0 / Σ 28.0 = 89.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.3% = $5.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-stasmi</code> BUY 3 @ 10¢ → $16.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 3 (3 yours) | ×0.2^0 = 3.3 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 1 | ×0.2^6 = 0.0 |
|  | 2¢ | 3 | ×0.2^8 = 0.0 |
|  | 1¢ | 60,451 | ×0.2^9 = 0.0 |
| | | **Σ** | **3.4** |

`yours 3.0 / Σ 3.4 = 88.8%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 88.8% = $16.44/day`  

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
22. `ewc-usp-2028-11-07-stasmi` ← this one
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> SELL 1 @ 22¢ → $25.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 25¢ | 1 | ×0.2^3 = 0.0 |
|  | 29¢ | 1 | ×0.2^7 = 0.0 |
|  | 30¢ | 48,877 | ×0.2^8 = 0.1 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.3%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 88.3% = $25.96/day`  

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
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 96¢ → $5.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 98¢ | 105 | ×0.1^2 = 1.1 |
|  | 99¢ | 5,193 | ×0.1^3 = 5.2 |
| | | **Σ** | **46.2** |

`yours 40.0 / Σ 46.2 = 86.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 86.5% = $5.41/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rokha</code> BUY 1 @ 16¢ → $15.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 14¢ | 1 | ×0.2^2 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 10¢ | 2 | ×0.2^6 = 0.0 |
|  | 8¢ | 1 | ×0.2^8 = 0.0 |
|  | 7¢ | 2 | ×0.2^9 = 0.0 |
|  | 3¢ | 2 | ×0.2^13 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^15 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 86.2%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 86.2% = $15.96/day`  

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
<details><summary><code>usgubewc-usgub-vt-2026-11-03-dem</code> SELL 5 @ 15¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 6 (5 yours) | ×0.1^0 = 6.0 |
|  | 98¢ | 132,784 | ×0.1^83 = 0.0 |
| | | **Σ** | **6.0** |

`yours 5.0 / Σ 6.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-vt-2026-11-03-dem` ← this one
2. `usgubewc-usgub-vt-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-markel</code> BUY 1 @ 14¢ → $15.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 10¢ | 61 | ×0.2^4 = 0.1 |
|  | 7¢ | 1 | ×0.2^7 = 0.0 |
|  | 2¢ | 1 | ×0.2^12 = 0.0 |
|  | 1¢ | 20,551 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 82.8%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 82.8% = $15.33/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> BUY 2 @ 9¢ → $14.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2 (2 yours) | ×0.2^0 = 2.2 |
|  | 5¢ | 1 | ×0.2^4 = 0.0 |
|  | 3¢ | 1 | ×0.2^6 = 0.0 |
|  | 2¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 114,451 | ×0.2^8 = 0.3 |
| | | **Σ** | **2.5** |

`yours 2.0 / Σ 2.5 = 79.4%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 79.4% = $14.70/day`  

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 24 @ 10¢ → $14.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 30 (24 yours) | ×0.2^0 = 30.0 |
|  | 9¢ | 2 | ×0.2^1 = 0.4 |
|  | 1¢ | 80,451 | ×0.2^9 = 0.0 |
| | | **Σ** | **30.5** |

`yours 24.0 / Σ 30.5 = 78.8%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 78.8% = $14.58/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

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
<details><summary><code>usgubewc-usgub-al-2026-11-03-dem</code> SELL 50 @ 14¢ → $4.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 64 (50 yours) | ×0.1^0 = 64.0 |
|  | 22¢ | 602 | ×0.1^8 = 0.0 |
|  | 25¢ | 53 | ×0.1^11 = 0.0 |
|  | 98¢ | 132,818 | ×0.1^84 = 0.0 |
| | | **Σ** | **64.0** |

`yours 50.0 / Σ 64.0 = 78.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 78.1% = $4.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem` ← this one
2. `usgubewc-usgub-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 25 @ 7¢ → $2.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 27 (25 yours) | ×0.2^0 = 27.0 |
|  | 5¢ | 26 | ×0.2^2 = 1.0 |
|  | 1¢ | 90,449 | ×0.2^6 = 5.8 |
| | | **Σ** | **33.8** |

`yours 25.0 / Σ 33.8 = 73.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 73.9% = $2.84/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53` ← this one
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 5 @ 25¢ → $21.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 7 (5 yours) | ×0.2^0 = 7.5 |
|  | 15¢ | 34 | ×0.2^10 = 0.0 |
|  | 11¢ | 100 | ×0.2^14 = 0.0 |
|  | 10¢ | 21,250 | ×0.2^15 = 0.0 |
| | | **Σ** | **7.5** |

`yours 5.5 / Σ 7.5 = 73.2%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 73.2% = $21.52/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (557,062 resting) | ~37.8% | ~$9.45 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (289,378 resting) | ~98.1% | ~$6.13 |
| `ewc-usgub-nv-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (3,012 resting) | ~69.7% | ~$4.36 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (263,706 resting) | ~65.8% | ~$4.11 |
| `ewc-usgub-mi-2026-11-03-rep` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (5,014 resting) | ~60.1% | ~$2.50 |
| `ewc-usse-mi-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (552,457 resting) | ~34.6% | ~$2.16 |
| `ewc-usmayor-losang-2026-11-03-karbas` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (205,069 resting) | ~28.9% | ~$1.80 |
| `ewc-usmayor-losang-2026-11-03-nitram` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (204,977 resting) | ~28.6% | ~$1.79 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (3,184 resting) | ~39.7% | ~$1.65 |
| `ewc-usse-nc-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (16,072 resting) | ~5.2% | ~$1.31 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (15,717 resting) | ~1.7% | ~$1.30 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (5,662 resting) | ~15.2% | ~$0.95 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $1,403.50 |
| Skipped | $1.41 |
| **Total earned** | **$3,292.94** |

2381 reward rows · 42 days with rewards · 489 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-13 ⚠️ multi-day pending bucket | $223.24 | `████████` |
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
| 2026-07-31 | $67.96 | `██` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $1,829.62 | `████████████████████` |
| 2026-07 | $1,463.32 | `████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $141.45 |
| `apdc-alito-2026-12-31` | $114.18 |
| `opdc-mcconnell-resign-2026-11-02` | $78.63 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $52.60 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $43.44 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.00 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.04 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `scc-senate-gop-2026-11-03-49` | $31.97 |
| `scc-senate-gop-2026-11-03-52` | $30.11 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-15 7:22 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 6:30 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 6:26 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 6:19 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 5:19 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 5:06 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 5:03 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 4:43 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 4:43 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 4:16 PM ET | ✅ ok | 2381 | $3292.94 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
