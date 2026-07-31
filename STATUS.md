# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-31 5:11 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$22.25/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-dem` — BUY at the best price, ~$18.59/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-12-31` (~$8.75/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$6.68/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$22.25/day (~$0.93/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-48` | BUY | 9.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~71.9% of bid side (5,348 resting ≥ 5,000 ✓) ≈ $2.76/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 15.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~44.9% of ask side (12,282 resting ≥ 5,000 ✓) ≈ $1.73/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 8.0¢ | 98 | 1 | $100.00 | ✅ scoring — ~28.1% of bid side (5,348 resting ≥ 5,000 ✓) ≈ $1.08/day (pool ÷ 13 markets) |
| `opdc-trump-resig-2026-12-31` | SELL | 7.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~26.1% of ask side (7,346 resting ≥ 2,000 ✓) ≈ $1.63/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 13.0¢ | 30 | 2 | $100.00 | ✅ scoring — ~19.9% of ask side (11,931 resting ≥ 5,000 ✓) ≈ $0.77/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 8.0¢ | 46 | 0 | $100.00 | ✅ scoring — ~19.5% of bid side (5,465 resting ≥ 5,000 ✓) ≈ $0.75/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 8.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~18.0% of ask side (119,340 resting ≥ 2,000 ✓) ≈ $0.23/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | SELL | 3.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~12.6% of ask side (119,312 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 10 markets) |
| `aec-itfme-ronhoh-olitar-2026-08-01` | SELL | 10.0¢ | 5 | 0 | $150.00 | ✅ scoring — ~11.4% of ask side (8,811 resting ≥ 8,000 ✓) ≈ $8.58/day |
| `scc-senate-gop-2026-11-03-46` | BUY | 1.0¢ | 5,000 | 2 | $100.00 | ✅ scoring — ~10.6% of bid side (26,080 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 17.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~10.1% of bid side (7,267 resting ≥ 5,000 ✓) ≈ $1.69/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 9.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~7.9% of bid side (5,872 resting ≥ 5,000 ✓) ≈ $0.31/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | SELL | 2.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~5.4% of ask side (11,640 resting ≥ 2,000 ✓) ≈ $0.07/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 95.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~4.4% of bid side (5,189 resting ≥ 2,000 ✓) ≈ $0.28/day (pool ÷ 2 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 28.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~2.7% of ask side (105,077 resting ≥ 2,000 ✓) ≈ $0.03/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 5,000 | 4 | $100.00 | ✅ scoring — ~2.3% of bid side (25,864 resting ≥ 5,000 ✓) ≈ $0.09/day (pool ÷ 13 markets) |
| `ewc-usse-tx-2026-11-03-dem` | BUY | 47.0¢ | 100 | 0 | $300.00 | ✅ scoring — ~1.5% of bid side (388,732 resting ≥ 10,000 ✓) ≈ $1.15/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 1.0¢ | 5,000 | 4 | $100.00 | ✅ scoring — ~1.1% of bid side (25,816 resting ≥ 5,000 ✓) ≈ $0.04/day (pool ÷ 13 markets) |
| `aec-itfwo-arigee-mararg-2026-08-01` | BUY | 83.0¢ | 5 | 1 | $150.00 | ✅ scoring — ~0.7% of bid side (8,856 resting ≥ 8,000 ✓) ≈ $0.49/day |
| `scc-senate-gop-2026-11-03-48` | SELL | 15.0¢ | 10 | 4 | $100.00 | ✅ scoring — ~0.3% of ask side (11,931 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 34.0¢ | 25 | 4 | $25.00 | ✅ scoring — ~0.2% of ask side (102,927 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 7 | $100.00 | ✅ scoring — ~0.0% of bid side (5,465 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 1.0¢ | 5,000 | 8 | $100.00 | ✅ scoring — ~0.0% of bid side (5,348 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 1.0¢ | 5,000 | 8 | $100.00 | ✅ scoring — ~0.0% of bid side (5,872 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 99.0¢ | 176 | 7 | $100.00 | ✅ scoring — ~0.0% of ask side (6,212 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 99.0¢ | 176 | 7 | $100.00 | ✅ scoring — ~0.0% of ask side (6,212 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 99.0¢ | 176 | 7 | $100.00 | ✅ scoring — ~0.0% of ask side (6,212 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 99.0¢ | 176 | 7 | $100.00 | ✅ scoring — ~0.0% of ask side (6,212 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 99.0¢ | 176 | 7 | $100.00 | ✅ scoring — ~0.0% of ask side (6,212 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 99.0¢ | 176 | 7 | $100.00 | ✅ scoring — ~0.0% of ask side (6,212 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| …and 193 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 50 @ 9¢ → $2.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 8¢ | 98 | ×0.2^1 = 19.6 |
|  | 1¢ | 5,200 | ×0.2^8 = 0.0 |
| | | **Σ** | **69.6** |

`yours 50.0 / Σ 69.6 = 71.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 71.9% = $2.76/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 100 @ 15¢ → $1.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 197 (100 yours) | ×0.2^0 = 197.0 |
|  | 16¢ | 128 | ×0.2^1 = 25.6 |
|  | 40¢ | 29 | ×0.2^25 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,827 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **222.6** |

`yours 100.0 / Σ 222.6 = 44.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 44.9% = $1.73/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 98 @ 8¢ → $1.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 50 | ×0.2^0 = 50.0 |
| ▶ | 8¢ | 98 (98 yours) | ×0.2^1 = 19.6 |
|  | 1¢ | 5,200 | ×0.2^8 = 0.0 |
| | | **Σ** | **69.6** |

`yours 19.6 / Σ 69.6 = 28.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.1% = $1.08/day`  

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
<details><summary><code>opdc-trump-resig-2026-12-31</code> SELL 0 @ 7¢ → $1.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 0 (0 yours) | ×0.1^0 = 0.1 |
|  | 9¢ | 10 | ×0.1^2 = 0.1 |
|  | 11¢ | 2,966 | ×0.1^4 = 0.3 |
| | | **Σ** | **0.5** |

`yours 0.1 / Σ 0.5 = 26.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.1% = $1.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `opdc-trump-resig-2026-12-31` ← this one
2. `opdc-trump-resig-2027-12-31`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 30 @ 13¢ → $0.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 4 | ×0.2^0 = 4.0 |
|  | 12¢ | 2 | ×0.2^1 = 0.4 |
| ▶ | 13¢ | 40 (30 yours) | ×0.2^2 = 1.6 |
|  | 15¢ | 10 | ×0.2^4 = 0.0 |
|  | 16¢ | 15 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^39 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^87 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^88 = 0.0 |
| | | **Σ** | **6.0** |

`yours 1.2 / Σ 6.0 = 19.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.9% = $0.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 46 @ 8¢ → $0.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 236 (46 yours) | ×0.2^0 = 235.9 |
|  | 1¢ | 5,229 | ×0.2^7 = 0.1 |
| | | **Σ** | **236.0** |

`yours 45.9 / Σ 236.0 = 19.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.5% = $0.75/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 40 @ 8¢ → $0.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 55 (40 yours) | ×0.1^0 = 55.0 |
|  | 9¢ | 18 | ×0.1^1 = 1.8 |
|  | 10¢ | 16,529 | ×0.1^2 = 165.3 |
| | | **Σ** | **222.1** |

`yours 40.0 / Σ 222.1 = 18.0%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 18.0% = $0.23/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> SELL 30 @ 3¢ → $0.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 69 (30 yours) | ×0.1^0 = 69.0 |
|  | 4¢ | 31 | ×0.1^1 = 3.1 |
|  | 5¢ | 16,533 | ×0.1^2 = 165.3 |
| | | **Σ** | **237.4** |

`yours 30.0 / Σ 237.4 = 12.6%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 12.6% = $0.16/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10` ← this one
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>aec-itfme-ronhoh-olitar-2026-08-01</code> SELL 5 @ 10¢ → $8.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 33 (5 yours) | ×0.3^0 = 33.0 |
|  | 11¢ | 32 | ×0.3^1 = 9.6 |
|  | 12¢ | 12 | ×0.3^2 = 1.1 |
|  | 98¢ | 10 | ×0.3^88 = 0.0 |
|  | 99¢ | 8,724 | ×0.3^89 = 0.0 |
| | | **Σ** | **43.7** |

`yours 5.0 / Σ 43.7 = 11.4%`  
`$150 ÷ 1 ÷ 2 = $75.00 × 11.4% = $8.58/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 5,000 @ 1¢ → $0.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 880 | ×0.2^0 = 880.0 |
| ▶ | 1¢ | 25,200 (5,000 yours) | ×0.2^2 = 1,008.0 |
| | | **Σ** | **1,888.0** |

`yours 200.0 / Σ 1,888.0 = 10.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 10.6% = $0.41/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 100 @ 17¢ → $1.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 734 (100 yours) | ×0.2^0 = 733.8 |
|  | 15¢ | 6,333 | ×0.2^2 = 253.3 |
| | | **Σ** | **987.2** |

`yours 100.0 / Σ 987.2 = 10.1%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 10.1% = $1.69/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-alito-2026-07-31`
2. `apdc-alito-2026-08-31`
3. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 50 @ 9¢ → $0.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 630 (50 yours) | ×0.2^0 = 630.0 |
|  | 1¢ | 5,242 | ×0.2^8 = 0.0 |
| | | **Σ** | **630.0** |

`yours 50.0 / Σ 630.0 = 7.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.9% = $0.31/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> SELL 50 @ 2¢ → $0.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 823 (50 yours) | ×0.1^0 = 823.0 |
|  | 3¢ | 60 | ×0.1^1 = 6.0 |
|  | 4¢ | 10,000 | ×0.1^2 = 100.0 |
| | | **Σ** | **929.0** |

`yours 50.0 / Σ 929.0 = 5.4%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 5.4% = $0.07/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15` ← this one
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-johsun</code> BUY 50 @ 95¢ → $0.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 930 (50 yours) | ×0.1^0 = 930.3 |
|  | 94¢ | 2,000 | ×0.1^1 = 200.0 |
| | | **Σ** | **1,130.3** |

`yours 50.0 / Σ 1,130.3 = 4.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 4.4% = $0.28/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun` ← this one
2. `enwc-ussep-nh-2026-09-01-rep-scobro`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 50 @ 28¢ → $0.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 1,854 (50 yours) | ×0.1^0 = 1,853.9 |
|  | 29¢ | 2 | ×0.1^1 = 0.2 |
|  | 33¢ | 240 | ×0.1^5 = 0.0 |
| | | **Σ** | **1,854.1** |

`yours 50.0 / Σ 1,854.1 = 2.7%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 2.7% = $0.03/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5` ← this one
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 5,000 @ 1¢ → $0.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 268 | ×0.2^0 = 268.0 |
|  | 4¢ | 231 | ×0.2^1 = 46.2 |
| ▶ | 1¢ | 25,365 (5,000 yours) | ×0.2^4 = 40.6 |
| | | **Σ** | **354.8** |

`yours 8.0 / Σ 354.8 = 2.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 2.3% = $0.09/day`  

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
<details><summary><code>ewc-usse-tx-2026-11-03-dem</code> BUY 100 @ 47¢ → $1.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 5,388 (100 yours) | ×0.2^0 = 5,388.0 |
|  | 46¢ | 5,803 | ×0.2^1 = 1,160.6 |
| | | **Σ** | **6,548.6** |

`yours 100.0 / Σ 6,548.6 = 1.5%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 1.5% = $1.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-tx-2026-11-03-dem` ← this one
2. `ewc-usse-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 5,000 @ 1¢ → $0.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 656 | ×0.2^0 = 656.0 |
| ▶ | 1¢ | 25,160 (5,000 yours) | ×0.2^4 = 40.3 |
| | | **Σ** | **696.3** |

`yours 8.0 / Σ 696.3 = 1.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.1% = $0.04/day`  

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
<details><summary><code>aec-itfwo-arigee-mararg-2026-08-01</code> BUY 5 @ 83¢ → $0.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 84¢ | 2 | ×0.3^0 = 2.0 |
| ▶ | 83¢ | 9 (5 yours) | ×0.3^1 = 2.6 |
|  | 82¢ | 2,476 | ×0.3^2 = 222.8 |
|  | 78¢ | 5 | ×0.3^6 = 0.0 |
|  | 2¢ | 34 | ×0.3^82 = 0.0 |
|  | 1¢ | 6,331 | ×0.3^83 = 0.0 |
| | | **Σ** | **227.4** |

`yours 1.5 / Σ 227.4 = 0.7%`  
`$150 ÷ 1 ÷ 2 = $75.00 × 0.7% = $0.49/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 15¢ → $0.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 4 | ×0.2^0 = 4.0 |
|  | 12¢ | 2 | ×0.2^1 = 0.4 |
|  | 13¢ | 40 | ×0.2^2 = 1.6 |
| ▶ | 15¢ | 10 (10 yours) | ×0.2^4 = 0.0 |
|  | 16¢ | 15 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^39 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^87 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^88 = 0.0 |
| | | **Σ** | **6.0** |

`yours 0.0 / Σ 6.0 = 0.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.3% = $0.01/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 25 @ 34¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 30¢ | 1 | ×0.1^0 = 1.0 |
|  | 33¢ | 1 | ×0.1^3 = 0.0 |
| ▶ | 34¢ | 25 (25 yours) | ×0.1^4 = 0.0 |
|  | 37¢ | 6 | ×0.1^7 = 0.0 |
|  | 38¢ | 20 | ×0.1^8 = 0.0 |
|  | 42¢ | 18 | ×0.1^12 = 0.0 |
|  | 45¢ | 25 | ×0.1^15 = 0.0 |
|  | 98¢ | 102,331 | ×0.1^68 = 0.0 |
| | | **Σ** | **1.0** |

`yours 0.0 / Σ 1.0 = 0.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 0.2% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 236 | ×0.2^0 = 235.9 |
| ▶ | 1¢ | 5,229 (5,000 yours) | ×0.2^7 = 0.1 |
| | | **Σ** | **236.0** |

`yours 0.1 / Σ 236.0 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 50 | ×0.2^0 = 50.0 |
|  | 8¢ | 98 | ×0.2^1 = 19.6 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^8 = 0.0 |
| | | **Σ** | **69.6** |

`yours 0.0 / Σ 69.6 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 630 | ×0.2^0 = 630.0 |
| ▶ | 1¢ | 5,242 (5,000 yours) | ×0.2^8 = 0.0 |
| | | **Σ** | **630.0** |

`yours 0.0 / Σ 630.0 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 176 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 201 | ×0.2^0 = 201.4 |
| ▶ | 99¢ | 6,010 (176 yours) | ×0.2^7 = 0.1 |
| | | **Σ** | **201.4** |

`yours 0.0 / Σ 201.4 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190` ← this one
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 176 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 201 | ×0.2^0 = 201.4 |
| ▶ | 99¢ | 6,010 (176 yours) | ×0.2^7 = 0.1 |
| | | **Σ** | **201.4** |

`yours 0.0 / Σ 201.4 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190` ← this one
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 176 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 201 | ×0.2^0 = 201.4 |
| ▶ | 99¢ | 6,010 (176 yours) | ×0.2^7 = 0.1 |
| | | **Σ** | **201.4** |

`yours 0.0 / Σ 201.4 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190` ← this one
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 176 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 201 | ×0.2^0 = 201.4 |
| ▶ | 99¢ | 6,010 (176 yours) | ×0.2^7 = 0.1 |
| | | **Σ** | **201.4** |

`yours 0.0 / Σ 201.4 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190` ← this one
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 176 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 201 | ×0.2^0 = 201.4 |
| ▶ | 99¢ | 6,010 (176 yours) | ×0.2^7 = 0.1 |
| | | **Σ** | **201.4** |

`yours 0.0 / Σ 201.4 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190` ← this one
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 176 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 201 | ×0.2^0 = 201.4 |
| ▶ | 99¢ | 6,010 (176 yours) | ×0.2^7 = 0.1 |
| | | **Σ** | **201.4** |

`yours 0.0 / Σ 201.4 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190` ← this one
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
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (81,865 resting) | ~24.8% | ~$18.59 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (8,448 resting) | ~52.5% | ~$8.75 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (83,706 resting) | ~26.7% | ~$6.68 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (69,828 resting) | ~26.1% | ~$6.53 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (68,002 resting) | ~25.8% | ~$6.46 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (121,620 resting) | ~7.0% | ~$5.23 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (33,548 resting) | ~9.6% | ~$4.80 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (74,522 resting) | ~5.6% | ~$4.21 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (74,810 resting) | ~5.0% | ~$3.79 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (108,983 resting) | ~4.8% | ~$3.63 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,062 resting) | ~8.4% | ~$2.10 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (44,923 resting) | ~8.2% | ~$2.04 |

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
| 2026-07-31 5:11 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 5:07 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 4:37 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 2:47 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 1:40 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 12:59 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 10:41 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 8:20 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 8:11 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 6:00 AM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
