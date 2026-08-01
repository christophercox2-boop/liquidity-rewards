# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-01 11:30 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$62.60/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$8.70/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$8.52/day), `apdc-jerpowgov-2026-08-31` (~$7.96/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$62.60/day (~$2.61/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ewc-pres-arg-2027-10-24-javmil` | BUY | 67.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,501 resting ≥ 2,000 ✓) ≈ $1.14/day (pool ÷ 11 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~99.2% of ask side (11,132 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 34.0¢ | 34 | 0 | $25.00 | ✅ scoring — ~97.2% of bid side (6,643 resting ≥ 2,000 ✓) ≈ $1.21/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 32.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~88.2% of ask side (12,253 resting ≥ 5,000 ✓) ≈ $3.39/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 33.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~76.9% of bid side (5,643 resting ≥ 5,000 ✓) ≈ $3.21/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~70.4% of ask side (11,927 resting ≥ 5,000 ✓) ≈ $2.71/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 6.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~69.4% of ask side (11,951 resting ≥ 5,000 ✓) ≈ $2.67/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~68.4% of ask side (12,072 resting ≥ 5,000 ✓) ≈ $2.63/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 22.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~64.1% of bid side (5,556 resting ≥ 5,000 ✓) ≈ $2.47/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~62.5% of bid side (5,499 resting ≥ 5,000 ✓) ≈ $2.40/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~58.8% of ask side (11,842 resting ≥ 5,000 ✓) ≈ $2.26/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 90.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~58.1% of bid side (5,508 resting ≥ 5,000 ✓) ≈ $2.42/day (pool ÷ 12 markets) |
| `cranc-uspres28-12-31-2026-tedcru` | SELL | 21.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~55.6% of ask side (5,505 resting ≥ 5,000 ✓) ≈ $0.84/day (pool ÷ 33 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 7.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~51.5% of ask side (5,505 resting ≥ 5,000 ✓) ≈ $2.15/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 65.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~50.0% of bid side (5,519 resting ≥ 5,000 ✓) ≈ $2.08/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 22.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~49.4% of bid side (5,602 resting ≥ 5,000 ✓) ≈ $2.06/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 22.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~49.4% of bid side (5,602 resting ≥ 5,000 ✓) ≈ $2.06/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 11.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~46.8% of ask side (11,970 resting ≥ 5,000 ✓) ≈ $1.80/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 7.0¢ | 33 | 0 | $25.00 | ✅ scoring — ~45.5% of ask side (119,363 resting ≥ 2,000 ✓) ≈ $0.57/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 42.0¢ | 53 | 0 | $100.00 | ✅ scoring — ~43.1% of ask side (5,798 resting ≥ 5,000 ✓) ≈ $1.80/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~40.0% of bid side (5,500 resting ≥ 5,000 ✓) ≈ $1.54/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 10.0¢ | 66 | 1 | $100.00 | ✅ scoring — ~38.4% of bid side (5,674 resting ≥ 5,000 ✓) ≈ $1.48/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~37.0% of ask side (12,225 resting ≥ 5,000 ✓) ≈ $1.42/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 5.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~34.4% of ask side (12,011 resting ≥ 5,000 ✓) ≈ $1.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~31.1% of ask side (12,072 resting ≥ 5,000 ✓) ≈ $1.20/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 36.0¢ | 50 | 3 | $100.00 | ✅ scoring — ~30.3% of ask side (12,096 resting ≥ 5,000 ✓) ≈ $1.16/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~29.7% of bid side (7,531 resting ≥ 5,000 ✓) ≈ $1.24/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~29.1% of ask side (12,231 resting ≥ 5,000 ✓) ≈ $1.12/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~27.7% of ask side (11,951 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~26.4% of bid side (7,951 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 12 markets) |
| …and 149 more | | | | | | |

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 2 @ 6¢ → $3.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 2 (2 yours) | ×0.2^0 = 2.0 |
|  | 10¢ | 10 | ×0.2^4 = 0.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^92 = 0.0 |
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
|  | 29¢ | 9 | ×0.1^5 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 20 @ 33¢ → $3.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 32¢ | 30 | ×0.2^1 = 6.0 |
|  | 10¢ | 32 | ×0.2^23 = 0.0 |
|  | 5¢ | 106 | ×0.2^28 = 0.0 |
|  | 1¢ | 5,455 | ×0.2^32 = 0.0 |
| | | **Σ** | **26.0** |

`yours 20.0 / Σ 26.0 = 76.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 76.9% = $3.21/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 50 @ 15¢ → $2.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 71 (50 yours) | ×0.2^0 = 71.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,755 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **71.0** |

`yours 50.0 / Σ 71.0 = 70.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 70.4% = $2.71/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47` ← this one
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 100 @ 22¢ → $2.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 156 (100 yours) | ×0.2^0 = 156.0 |
|  | 1¢ | 5,400 | ×0.2^21 = 0.0 |
| | | **Σ** | **156.0** |

`yours 100.0 / Σ 156.0 = 64.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.1% = $2.47/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 50 @ 90¢ → $2.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 86 (50 yours) | ×0.2^0 = 86.0 |
|  | 1¢ | 5,422 | ×0.2^89 = 0.0 |
| | | **Σ** | **86.0** |

`yours 50.0 / Σ 86.0 = 58.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 58.1% = $2.42/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 7¢ → $2.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 97 (50 yours) | ×0.2^0 = 97.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 14¢ | 15 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 99¢ | 5,367 | ×0.2^92 = 0.0 |
| | | **Σ** | **97.0** |

`yours 50.0 / Σ 97.0 = 51.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 51.5% = $2.15/day`  

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
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235` ← this one

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
|  | 20¢ | 1 | ×0.2^2 = 0.0 |
|  | 19¢ | 5 | ×0.2^3 = 0.0 |
|  | 18¢ | 101 | ×0.2^4 = 0.2 |
|  | 17¢ | 50 | ×0.2^5 = 0.0 |
|  | 1¢ | 5,425 | ×0.2^21 = 0.0 |
| | | **Σ** | **20.3** |

`yours 10.0 / Σ 20.3 = 49.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.4% = $2.06/day`  

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
|  | 20¢ | 1 | ×0.2^2 = 0.0 |
|  | 19¢ | 5 | ×0.2^3 = 0.0 |
|  | 18¢ | 101 | ×0.2^4 = 0.2 |
|  | 17¢ | 50 | ×0.2^5 = 0.0 |
|  | 1¢ | 5,425 | ×0.2^21 = 0.0 |
| | | **Σ** | **20.3** |

`yours 10.0 / Σ 20.3 = 49.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.4% = $2.06/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 11¢ → $1.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 41 (20 yours) | ×0.2^0 = 41.0 |
|  | 13¢ | 43 | ×0.2^2 = 1.7 |
|  | 16¢ | 15 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^39 = 0.0 |
|  | 98¢ | 1,770 | ×0.2^87 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^88 = 0.0 |
| | | **Σ** | **42.7** |

`yours 20.0 / Σ 42.7 = 46.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 46.8% = $1.80/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 33 @ 7¢ → $0.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 56 (33 yours) | ×0.1^0 = 56.3 |
|  | 9¢ | 24 | ×0.1^2 = 0.2 |
|  | 10¢ | 16,556 | ×0.1^3 = 16.6 |
| | | **Σ** | **73.1** |

`yours 33.3 / Σ 73.1 = 45.5%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 45.5% = $0.57/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5` ← this one
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 53 @ 42¢ → $1.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 123 (53 yours) | ×0.2^0 = 123.0 |
|  | 52¢ | 1 | ×0.2^10 = 0.0 |
|  | 57¢ | 11 | ×0.2^15 = 0.0 |
|  | 69¢ | 100 | ×0.2^27 = 0.0 |
|  | 99¢ | 5,563 | ×0.2^57 = 0.0 |
| | | **Σ** | **123.0** |

`yours 53.0 / Σ 123.0 = 43.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 43.1% = $1.80/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 1,000 @ 2¢ → $1.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 1,747 (1,000 yours) | ×0.2^0 = 1,747.0 |
|  | 1¢ | 3,753 | ×0.2^1 = 750.6 |
| | | **Σ** | **2,497.6** |

`yours 1,000.0 / Σ 2,497.6 = 40.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.0% = $1.54/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 66 @ 10¢ → $1.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 21 | ×0.2^0 = 21.0 |
| ▶ | 10¢ | 66 (66 yours) | ×0.2^1 = 13.2 |
|  | 7¢ | 93 | ×0.2^4 = 0.1 |
|  | 1¢ | 5,494 | ×0.2^10 = 0.0 |
| | | **Σ** | **34.3** |

`yours 13.2 / Σ 34.3 = 38.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.4% = $1.48/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 10¢ → $1.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 135 (50 yours) | ×0.2^0 = 135.2 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **135.2** |

`yours 50.0 / Σ 135.2 = 37.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.0% = $1.42/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 50 @ 5¢ → $1.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 145 (50 yours) | ×0.2^0 = 145.2 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 98¢ | 1,765 | ×0.2^93 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^94 = 0.0 |
| | | **Σ** | **145.2** |

`yours 50.0 / Σ 145.2 = 34.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.4% = $1.32/day`  

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
11. `scc-senate-gop-2026-11-03-56` ← this one
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 5,000 @ 1¢ → $1.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 2,331 | ×0.2^0 = 2,331.0 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^1 = 1,040.0 |
| | | **Σ** | **3,371.0** |

`yours 1,000.0 / Σ 3,371.0 = 29.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 29.7% = $1.24/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 50 @ 21¢ → $1.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 136 (50 yours) | ×0.2^0 = 136.0 |
|  | 22¢ | 178 | ×0.2^1 = 35.6 |
|  | 28¢ | 20 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **171.6** |

`yours 50.0 / Σ 171.6 = 29.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.1% = $1.12/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> BUY 5,000 @ 1¢ → $1.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 2,751 | ×0.2^0 = 2,751.0 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^1 = 1,040.0 |
| | | **Σ** | **3,791.0** |

`yours 1,000.0 / Σ 3,791.0 = 26.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 26.4% = $1.10/day`  

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
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (89,032 resting) | ~11.4% | ~$8.52 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (8,736 resting) | ~47.8% | ~$7.96 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (70,808 resting) | ~24.2% | ~$6.06 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (73,093 resting) | ~7.6% | ~$5.71 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (17,070 resting) | ~9.0% | ~$4.51 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (95,533 resting) | ~4.8% | ~$3.57 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (146,613 resting) | ~2.8% | ~$2.13 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (75,313 resting) | ~8.2% | ~$2.06 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (78,368 resting) | ~2.6% | ~$1.97 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (385,655 resting) | ~2.5% | ~$1.85 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (186,038 resting) | ~2.1% | ~$1.60 |

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
| 2026-08-01 11:30 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 10:00 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 9:23 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 9:19 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 7:36 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 6:43 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 5:25 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 2:43 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 11:55 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 11:25 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
