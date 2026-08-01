# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-01 12:06 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$45.38/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$8.70/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$8.52/day), `apdc-jerpowgov-2026-08-31` (~$7.96/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$45.38/day (~$1.89/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ewc-pres-arg-2027-10-24-javmil` | BUY | 67.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,501 resting ≥ 2,000 ✓) ≈ $1.14/day (pool ÷ 11 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 10.0¢ | 66 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (5,370 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~99.2% of ask side (11,967 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 34.0¢ | 34 | 0 | $25.00 | ✅ scoring — ~97.2% of bid side (6,634 resting ≥ 2,000 ✓) ≈ $1.21/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 32.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~88.2% of ask side (12,253 resting ≥ 5,000 ✓) ≈ $3.39/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 6.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~69.4% of ask side (11,951 resting ≥ 5,000 ✓) ≈ $2.67/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~68.4% of ask side (12,072 resting ≥ 5,000 ✓) ≈ $2.63/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 90.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (5,502 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~62.5% of bid side (5,499 resting ≥ 5,000 ✓) ≈ $2.40/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~58.8% of ask side (11,842 resting ≥ 5,000 ✓) ≈ $2.26/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-tedcru` | SELL | 21.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~55.6% of ask side (5,505 resting ≥ 5,000 ✓) ≈ $0.84/day (pool ÷ 33 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 65.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~50.0% of bid side (5,519 resting ≥ 5,000 ✓) ≈ $2.08/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 22.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~49.5% of bid side (5,601 resting ≥ 5,000 ✓) ≈ $2.06/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 22.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~49.5% of bid side (5,601 resting ≥ 5,000 ✓) ≈ $2.06/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 11.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~47.6% of ask side (11,928 resting ≥ 5,000 ✓) ≈ $1.83/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~31.1% of ask side (12,072 resting ≥ 5,000 ✓) ≈ $1.20/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 36.0¢ | 50 | 3 | $100.00 | ✅ scoring — ~30.3% of ask side (12,096 resting ≥ 5,000 ✓) ≈ $1.16/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~27.7% of ask side (11,951 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~20.5% of bid side (5,033 resting ≥ 5,000 ✓) ≈ $0.79/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 21.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~16.7% of bid side (5,444 resting ≥ 5,000 ✓) ≈ $0.69/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | BUY | 17.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~16.3% of bid side (5,613 resting ≥ 5,000 ✓) ≈ $2.72/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~14.7% of bid side (12,623 resting ≥ 5,000 ✓) ≈ $0.57/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 2.0¢ | 250 | 0 | $100.00 | ✅ scoring — ~14.6% of bid side (5,500 resting ≥ 5,000 ✓) ≈ $0.61/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 74.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~8.3% of bid side (5,630 resting ≥ 5,000 ✓) ≈ $0.35/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 76.0¢ | 49 | 0 | $100.00 | ✅ scoring — ~6.9% of ask side (5,781 resting ≥ 5,000 ✓) ≈ $0.29/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 34.0¢ | 43 | 2 | $100.00 | ✅ scoring — ~3.5% of ask side (12,253 resting ≥ 5,000 ✓) ≈ $0.14/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 69.0¢ | 33 | 0 | $100.00 | ✅ scoring — ~3.4% of ask side (9,375 resting ≥ 5,000 ✓) ≈ $0.14/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~3.3% of bid side (5,414 resting ≥ 5,000 ✓) ≈ $0.13/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~3.2% of ask side (11,905 resting ≥ 5,000 ✓) ≈ $0.12/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 62.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~2.2% of ask side (6,752 resting ≥ 5,000 ✓) ≈ $0.09/day (pool ÷ 12 markets) |
| …and 115 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ewc-pres-arg-2027-10-24-javmil</code> BUY 1 @ 67¢ → $1.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 1 (1 yours) | ×0.1^0 = 1.3 |
|  | 62¢ | 1 | ×0.1^5 = 0.0 |
|  | 59¢ | 1 | ×0.1^8 = 0.0 |
|  | 56¢ | 4 | ×0.1^11 = 0.0 |
|  | 1¢ | 2,493 | ×0.1^66 = 0.0 |
| | | **Σ** | **1.3** |

`yours 1.3 / Σ 1.3 = 100.0%`  
`$25 ÷ 11 ÷ 2 = $1.14 × 100.0% = $1.14/day`  

<details><summary>÷ 11 markets in this race — tap to list</summary>

1. `ewc-pres-arg-2027-10-24-axekic`
2. `ewc-pres-arg-2027-10-24-dangeb`
3. `ewc-pres-arg-2027-10-24-estbul`
4. `ewc-pres-arg-2027-10-24-facman`
5. `ewc-pres-arg-2027-10-24-javmil` ← this one
6. `ewc-pres-arg-2027-10-24-juagra`
7. `ewc-pres-arg-2027-10-24-juasch`
8. `ewc-pres-arg-2027-10-24-maumac`
9. `ewc-pres-arg-2027-10-24-myrbre`
10. `ewc-pres-arg-2027-10-24-sermas`
11. `ewc-pres-arg-2027-10-24-vicvil`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 66 @ 10¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 66 (66 yours) | ×0.2^0 = 65.9 |
|  | 1¢ | 5,304 | ×0.2^9 = 0.0 |
| | | **Σ** | **65.9** |

`yours 65.9 / Σ 65.9 = 100.0%`  
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
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57` ← this one
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 2 @ 6¢ → $3.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 2 (2 yours) | ×0.2^0 = 2.0 |
|  | 10¢ | 10 | ×0.2^4 = 0.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 16¢ | 100 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,735 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 99.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.2% = $3.82/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55` ← this one
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 34 @ 34¢ → $1.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 35 (34 yours) | ×0.1^0 = 35.3 |
|  | 13¢ | 6 | ×0.1^21 = 0.0 |
|  | 10¢ | 18 | ×0.1^24 = 0.0 |
|  | 8¢ | 700 | ×0.1^26 = 0.0 |
|  | 7¢ | 499 | ×0.1^27 = 0.0 |
|  | 2¢ | 375 | ×0.1^32 = 0.0 |
|  | 1¢ | 5,001 | ×0.1^33 = 0.0 |
| | | **Σ** | **35.3** |

`yours 34.3 / Σ 35.3 = 97.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 97.2% = $1.21/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20` ← this one
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 32¢ → $3.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 47 (43 yours) | ×0.2^0 = 47.0 |
|  | 34¢ | 43 | ×0.2^2 = 1.7 |
|  | 38¢ | 128 | ×0.2^6 = 0.0 |
|  | 49¢ | 37 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^18 = 0.0 |
|  | 98¢ | 1,897 | ×0.2^66 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^67 = 0.0 |
| | | **Σ** | **48.7** |

`yours 43.0 / Σ 48.7 = 88.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.2% = $3.39/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 1 @ 6¢ → $2.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 11 | ×0.2^2 = 0.4 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 16¢ | 3 | ×0.2^10 = 0.0 |
|  | 19¢ | 100 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,734 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **1.4** |

`yours 1.0 / Σ 1.4 = 69.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 69.4% = $2.67/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 22 @ 20¢ → $2.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 32 (22 yours) | ×0.2^0 = 32.0 |
|  | 24¢ | 100 | ×0.2^4 = 0.2 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,839 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **32.2** |

`yours 22.0 / Σ 32.2 = 68.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.4% = $2.63/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 4 @ 90¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 6 (4 yours) | ×0.2^0 = 6.0 |
|  | 1¢ | 5,496 | ×0.2^89 = 0.0 |
| | | **Σ** | **6.0** |

`yours 4.0 / Σ 6.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185` ← this one
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 10 @ 29¢ → $2.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 16 (10 yours) | ×0.2^0 = 16.0 |
|  | 1¢ | 5,483 | ×0.2^28 = 0.0 |
| | | **Σ** | **16.0** |

`yours 10.0 / Σ 16.0 = 62.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 62.5% = $2.40/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 10 @ 8¢ → $2.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 17 (10 yours) | ×0.2^0 = 17.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,724 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^91 = 0.0 |
| | | **Σ** | **17.0** |

`yours 10.0 / Σ 17.0 = 58.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 58.8% = $2.26/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45` ← this one

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-tedcru</code> SELL 0 @ 21¢ → $0.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (0 yours) | ×0.2^0 = 0.7 |
|  | 28¢ | 56 | ×0.2^7 = 0.0 |
|  | 29¢ | 470 | ×0.2^8 = 0.0 |
|  | 50¢ | 25 | ×0.2^29 = 0.0 |
|  | 77¢ | 2 | ×0.2^56 = 0.0 |
|  | 78¢ | 2 | ×0.2^57 = 0.0 |
|  | 99¢ | 4,949 | ×0.2^78 = 0.0 |
| | | **Σ** | **0.7** |

`yours 0.4 / Σ 0.7 = 55.6%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 55.6% = $0.84/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru`
7. `cranc-uspres28-12-31-2026-dontrujr`
8. `cranc-uspres28-12-31-2026-dwajoh`
9. `cranc-uspres28-12-31-2026-elomus`
10. `cranc-uspres28-12-31-2026-erikir`
11. `cranc-uspres28-12-31-2026-gavnew`
12. `cranc-uspres28-12-31-2026-hilcli`
13. `cranc-uspres28-12-31-2026-hunbid`
14. `cranc-uspres28-12-31-2026-jdvan`
15. `cranc-uspres28-12-31-2026-jonoss`
16. `cranc-uspres28-12-31-2026-jossha`
17. `cranc-uspres28-12-31-2026-kamhar`
18. `cranc-uspres28-12-31-2026-krinoe`
19. `cranc-uspres28-12-31-2026-margre`
20. `cranc-uspres28-12-31-2026-markel`
21. `cranc-uspres28-12-31-2026-marrub`
22. `cranc-uspres28-12-31-2026-micoba`
23. `cranc-uspres28-12-31-2026-nikhal`
24. `cranc-uspres28-12-31-2026-oprwin`
25. `cranc-uspres28-12-31-2026-petbut`
26. `cranc-uspres28-12-31-2026-rahema`
27. `cranc-uspres28-12-31-2026-robken`
28. `cranc-uspres28-12-31-2026-steban`
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru` ← this one
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 30 @ 65¢ → $2.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 60 (30 yours) | ×0.2^0 = 60.0 |
|  | 1¢ | 5,459 | ×0.2^64 = 0.0 |
| | | **Σ** | **60.0** |

`yours 30.0 / Σ 60.0 = 50.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 50.0% = $2.08/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200` ← this one
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 10 @ 22¢ → $2.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 20 (10 yours) | ×0.2^0 = 20.0 |
|  | 19¢ | 5 | ×0.2^3 = 0.0 |
|  | 18¢ | 101 | ×0.2^4 = 0.2 |
|  | 17¢ | 50 | ×0.2^5 = 0.0 |
|  | 1¢ | 5,425 | ×0.2^21 = 0.0 |
| | | **Σ** | **20.2** |

`yours 10.0 / Σ 20.2 = 49.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.5% = $2.06/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215` ← this one
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 10 @ 22¢ → $2.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 20 (10 yours) | ×0.2^0 = 20.0 |
|  | 19¢ | 5 | ×0.2^3 = 0.0 |
|  | 18¢ | 101 | ×0.2^4 = 0.2 |
|  | 17¢ | 50 | ×0.2^5 = 0.0 |
|  | 1¢ | 5,425 | ×0.2^21 = 0.0 |
| | | **Σ** | **20.2** |

`yours 10.0 / Σ 20.2 = 49.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.5% = $2.06/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215` ← this one
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 11¢ → $1.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 42 (20 yours) | ×0.2^0 = 42.0 |
|  | 16¢ | 15 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^39 = 0.0 |
|  | 98¢ | 1,770 | ×0.2^87 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^88 = 0.0 |
| | | **Σ** | **42.0** |

`yours 20.0 / Σ 42.0 = 47.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.6% = $1.83/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 10 @ 20¢ → $1.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 32 (10 yours) | ×0.2^0 = 32.0 |
|  | 24¢ | 100 | ×0.2^4 = 0.2 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,839 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **32.2** |

`yours 10.0 / Σ 32.2 = 31.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.1% = $1.20/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 50 @ 36¢ → $1.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 33¢ | 1 | ×0.2^0 = 0.9 |
| ▶ | 36¢ | 50 (50 yours) | ×0.2^3 = 0.4 |
|  | 40¢ | 105 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^17 = 0.0 |
|  | 98¢ | 1,839 | ×0.2^65 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^66 = 0.0 |
| | | **Σ** | **1.3** |

`yours 0.4 / Σ 1.3 = 30.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.3% = $1.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 8¢ → $1.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 8¢ | 11 (10 yours) | ×0.2^2 = 0.4 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 16¢ | 3 | ×0.2^10 = 0.0 |
|  | 19¢ | 100 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,734 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **1.4** |

`yours 0.4 / Σ 1.4 = 27.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.7% = $1.07/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 1,000 @ 2¢ → $0.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 4,831 (1,000 yours) | ×0.2^0 = 4,831.0 |
|  | 1¢ | 202 | ×0.2^1 = 40.4 |
| | | **Σ** | **4,871.4** |

`yours 1,000.0 / Σ 4,871.4 = 20.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.5% = $0.79/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 50 @ 21¢ → $0.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 22¢ | 50 | ×0.2^0 = 50.0 |
| ▶ | 21¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 10¢ | 39 | ×0.2^12 = 0.0 |
|  | 6¢ | 100 | ×0.2^16 = 0.0 |
|  | 1¢ | 5,205 | ×0.2^21 = 0.0 |
| | | **Σ** | **60.0** |

`yours 10.0 / Σ 60.0 = 16.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.7% = $0.69/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220` ← this one
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 100 @ 17¢ → $2.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 413 (100 yours) | ×0.2^0 = 412.8 |
|  | 15¢ | 5,000 | ×0.2^2 = 200.0 |
| | | **Σ** | **612.8** |

`yours 100.0 / Σ 612.8 = 16.3%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 16.3% = $2.72/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-alito-2026-07-31`
2. `apdc-alito-2026-08-31`
3. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 3,013 (500 yours) | ×0.2^0 = 3,013.0 |
|  | 1¢ | 9,610 | ×0.2^2 = 384.4 |
| | | **Σ** | **3,397.4** |

`yours 500.0 / Σ 3,397.4 = 14.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.7% = $0.57/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46` ← this one
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> BUY 250 @ 2¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 765 (250 yours) | ×0.2^0 = 765.0 |
|  | 1¢ | 4,735 | ×0.2^1 = 947.0 |
| | | **Σ** | **1,712.0** |

`yours 250.0 / Σ 1,712.0 = 14.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 14.6% = $0.61/day`  

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
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230` ← this one
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 40 @ 74¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 478 (40 yours) | ×0.2^0 = 478.3 |
|  | 72¢ | 83 | ×0.2^2 = 3.3 |
|  | 1¢ | 5,069 | ×0.2^73 = 0.0 |
| | | **Σ** | **481.6** |

`yours 40.0 / Σ 481.6 = 8.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 8.3% = $0.35/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195` ← this one
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 49 @ 76¢ → $0.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 76¢ | 711 (49 yours) | ×0.2^0 = 711.0 |
|  | 80¢ | 50 | ×0.2^4 = 0.1 |
|  | 98¢ | 127 | ×0.2^22 = 0.0 |
|  | 99¢ | 4,893 | ×0.2^23 = 0.0 |
| | | **Σ** | **711.1** |

`yours 49.0 / Σ 711.1 = 6.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 6.9% = $0.29/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195` ← this one
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 34¢ → $0.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 32¢ | 47 | ×0.2^0 = 47.0 |
| ▶ | 34¢ | 43 (43 yours) | ×0.2^2 = 1.7 |
|  | 38¢ | 128 | ×0.2^6 = 0.0 |
|  | 49¢ | 37 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^18 = 0.0 |
|  | 98¢ | 1,897 | ×0.2^66 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^67 = 0.0 |
| | | **Σ** | **48.7** |

`yours 1.7 / Σ 48.7 = 3.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.5% = $0.14/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 33 @ 69¢ → $0.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 69¢ | 984 (33 yours) | ×0.2^0 = 984.2 |
|  | 74¢ | 85 | ×0.2^5 = 0.0 |
|  | 77¢ | 1,100 | ×0.2^8 = 0.0 |
|  | 79¢ | 1,865 | ×0.2^10 = 0.0 |
|  | 87¢ | 168 | ×0.2^18 = 0.0 |
|  | 90¢ | 1 | ×0.2^21 = 0.0 |
|  | 99¢ | 5,172 | ×0.2^30 = 0.0 |
| | | **Σ** | **984.3** |

`yours 33.0 / Σ 984.3 = 3.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.4% = $0.14/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200` ← this one
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 50 @ 20¢ → $0.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 1,536 (50 yours) | ×0.2^0 = 1,536.0 |
|  | 1¢ | 3,878 | ×0.2^19 = 0.0 |
| | | **Σ** | **1,536.0** |

`yours 50.0 / Σ 1,536.0 = 3.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.3% = $0.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 1 @ 8¢ → $0.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 31 (1 yours) | ×0.2^0 = 30.8 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,773 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^91 = 0.0 |
| | | **Σ** | **30.8** |

`yours 1.0 / Σ 30.8 = 3.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.2% = $0.12/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46` ← this one
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 30 @ 62¢ → $0.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 62¢ | 1,368 (30 yours) | ×0.2^0 = 1,367.7 |
|  | 83¢ | 103 | ×0.2^21 = 0.0 |
|  | 99¢ | 5,281 | ×0.2^37 = 0.0 |
| | | **Σ** | **1,367.7** |

`yours 30.0 / Σ 1,367.7 = 2.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 2.2% = $0.09/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205` ← this one
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-29 | ~$65.42 | $53.59 | 82% |
| 2026-07-28 | ~$148.78 | $79.65 | 54% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |

Biggest gaps on 2026-07-29: `apdc-petehegseth-2026-12-31` (est ~$12.90 → got $1.16), `scc-senate-gop-2026-11-03-51` (est ~$3.25 → got $0.00), `scc-senate-gop-2026-11-03-54` (est ~$2.11 → got $0.02)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (8,652 resting) | ~52.2% | ~$8.70 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (89,030 resting) | ~11.4% | ~$8.52 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (8,732 resting) | ~47.8% | ~$7.96 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (72,540 resting) | ~9.6% | ~$7.24 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (73,153 resting) | ~8.4% | ~$6.28 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (95,540 resting) | ~4.8% | ~$3.57 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (146,580 resting) | ~2.8% | ~$2.14 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (75,316 resting) | ~8.2% | ~$2.05 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (382,274 resting) | ~2.6% | ~$1.98 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (186,063 resting) | ~2.1% | ~$1.61 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,493 resting) | ~94.8% | ~$1.44 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (208,217 resting) | ~1.8% | ~$1.37 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,373.47 |
| Skipped | $1.21 |
| **Total earned** | **$1,374.68** |

1406 reward rows · 27 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-29 | $53.59 | `█████` |
| 2026-07-28 | $79.65 | `███████` |
| 2026-07-27 | $125.34 | `███████████` |
| 2026-07-26 | $153.80 | `██████████████` |
| 2026-07-25 | $125.69 | `███████████` |
| 2026-07-24 | $135.19 | `████████████` |
| 2026-07-23 | $227.63 | `████████████████████` |
| 2026-07-22 | $82.95 | `███████` |
| 2026-07-21 | $91.44 | `████████` |
| 2026-07-20 | $106.54 | `█████████` |
| 2026-07-19 | $35.81 | `███` |
| 2026-07-18 | $44.41 | `████` |
| 2026-07-17 | $14.71 | `█` |
| 2026-07-16 | $17.02 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,374.68 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.26 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.82 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.47 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.25 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.73 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.96 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-01 12:06 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 11:30 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 10:00 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 9:23 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 9:19 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 7:36 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 6:43 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 5:25 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 2:43 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 11:55 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
