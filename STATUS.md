# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-02 5:12 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$17.45/day estimated (ceiling, not promise — details below)

**Earned:** $1,463.12 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-31: **$67.96** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-30: **$20.48** · 2026-07-29: **$53.59** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$22.54/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$22.29/day), `ewc-usgub-oh-2026-11-03-dem` (~$13.81/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$17.45/day (~$0.73/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 43.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.9% of bid side (6,650 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~40.4% of ask side (12,109 resting ≥ 5,000 ✓) ≈ $1.55/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 30.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~34.7% of ask side (12,461 resting ≥ 5,000 ✓) ≈ $1.33/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~29.9% of ask side (12,424 resting ≥ 5,000 ✓) ≈ $1.15/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~28.6% of bid side (5,550 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~26.5% of ask side (12,221 resting ≥ 5,000 ✓) ≈ $1.02/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 18.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~26.3% of ask side (12,146 resting ≥ 5,000 ✓) ≈ $1.01/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 25.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~22.2% of ask side (12,180 resting ≥ 5,000 ✓) ≈ $0.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~22.1% of ask side (12,216 resting ≥ 5,000 ✓) ≈ $0.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~20.4% of ask side (12,084 resting ≥ 5,000 ✓) ≈ $0.78/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~19.9% of bid side (12,303 resting ≥ 5,000 ✓) ≈ $0.77/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~19.6% of bid side (25,468 resting ≥ 5,000 ✓) ≈ $0.76/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 16.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~8.8% of ask side (5,502 resting ≥ 5,000 ✓) ≈ $2.20/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 15.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~7.7% of ask side (12,203 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 3.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~7.1% of bid side (14,325 resting ≥ 5,000 ✓) ≈ $0.27/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~5.2% of bid side (19,548 resting ≥ 5,000 ✓) ≈ $0.20/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 22.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~4.9% of ask side (5,519 resting ≥ 5,000 ✓) ≈ $0.20/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 2.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~4.3% of bid side (11,950 resting ≥ 5,000 ✓) ≈ $0.18/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 6.0¢ | 32 | 1 | $100.00 | ✅ scoring — ~4.2% of bid side (5,713 resting ≥ 5,000 ✓) ≈ $0.16/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 5.0¢ | 590 | 0 | $100.00 | ✅ scoring — ~4.0% of bid side (14,832 resting ≥ 5,000 ✓) ≈ $0.16/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~3.7% of bid side (13,885 resting ≥ 5,000 ✓) ≈ $0.14/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~3.5% of ask side (6,380 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 30.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~3.4% of ask side (12,319 resting ≥ 5,000 ✓) ≈ $0.13/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 11 | 1 | $100.00 | ✅ scoring — ~1.9% of bid side (5,613 resting ≥ 5,000 ✓) ≈ $0.08/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~1.7% of bid side (5,613 resting ≥ 5,000 ✓) ≈ $0.07/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 20.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~1.5% of ask side (5,562 resting ≥ 5,000 ✓) ≈ $0.06/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 67.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~1.3% of ask side (9,311 resting ≥ 5,000 ✓) ≈ $0.05/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~1.2% of ask side (12,159 resting ≥ 5,000 ✓) ≈ $0.05/day (pool ÷ 13 markets) |
| `ewc-usse-tx-2026-11-03-dem` | BUY | 47.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~0.8% of bid side (385,332 resting ≥ 10,000 ✓) ≈ $0.58/day (pool ÷ 2 markets) |
| `cranc-uspres28-12-31-2026-tedcru` | SELL | 21.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~0.4% of ask side (5,526 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 33 markets) |
| …and 27 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 1 @ 43¢ → $1.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 40¢ | 1 | ×0.1^3 = 0.0 |
|  | 38¢ | 17 | ×0.1^5 = 0.0 |
|  | 37¢ | 6 | ×0.1^6 = 0.0 |
|  | 11¢ | 1 | ×0.1^32 = 0.0 |
|  | 9¢ | 750 | ×0.1^34 = 0.0 |
|  | 8¢ | 450 | ×0.1^35 = 0.0 |
|  | 1¢ | 5,424 | ×0.1^42 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 99.9% = $1.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 18 @ 15¢ → $1.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 45 (18 yours) | ×0.2^0 = 45.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **45.3** |

`yours 18.3 / Σ 45.3 = 40.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.4% = $1.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 30¢ → $1.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 124 (43 yours) | ×0.2^0 = 124.0 |
|  | 38¢ | 128 | ×0.2^8 = 0.0 |
|  | 43¢ | 37 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^20 = 0.0 |
|  | 98¢ | 1,871 | ×0.2^68 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^69 = 0.0 |
| | | **Σ** | **124.0** |

`yours 43.0 / Σ 124.0 = 34.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.7% = $1.33/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $1.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 134 (40 yours) | ×0.2^0 = 133.7 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **133.7** |

`yours 40.0 / Σ 133.7 = 29.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.9% = $1.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 100 @ 20¢ → $1.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 350 (100 yours) | ×0.2^0 = 350.0 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **350.0** |

`yours 100.0 / Σ 350.0 = 28.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.6% = $1.10/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 151 (40 yours) | ×0.2^0 = 151.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **151.0** |

`yours 40.0 / Σ 151.0 = 26.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.5% = $1.02/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 18¢ → $1.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 114 (30 yours) | ×0.2^0 = 114.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^81 = 0.0 |
| | | **Σ** | **114.0** |

`yours 30.0 / Σ 114.0 = 26.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.3% = $1.01/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 50 @ 25¢ → $0.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 24¢ | 32 | ×0.2^0 = 32.1 |
| ▶ | 25¢ | 65 (50 yours) | ×0.2^1 = 13.0 |
|  | 50¢ | 100 | ×0.2^26 = 0.0 |
|  | 98¢ | 1,782 | ×0.2^74 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^75 = 0.0 |
| | | **Σ** | **45.1** |

`yours 10.0 / Σ 45.1 = 22.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 22.2% = $0.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 16¢ → $0.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 73 (20 yours) | ×0.2^0 = 73.0 |
|  | 17¢ | 88 | ×0.2^1 = 17.6 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^82 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^83 = 0.0 |
| | | **Σ** | **90.6** |

`yours 20.0 / Σ 90.6 = 22.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 22.1% = $0.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 10¢ → $0.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 49 (10 yours) | ×0.2^0 = 49.0 |
|  | 16¢ | 3 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **49.0** |

`yours 10.0 / Σ 49.0 = 20.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.4% = $0.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $0.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 2,113 (500 yours) | ×0.2^0 = 2,113.0 |
|  | 2¢ | 9,990 | ×0.2^2 = 399.6 |
| | | **Σ** | **2,512.6** |

`yours 500.0 / Σ 2,512.6 = 19.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.9% = $0.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5,000 @ 1¢ → $0.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 25,468 (5,000 yours) | ×0.2^0 = 25,467.9 |
| | | **Σ** | **25,467.9** |

`yours 5,000.0 / Σ 25,467.9 = 19.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.6% = $0.76/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 16¢ → $2.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1,138 (100 yours) | ×0.2^0 = 1,137.8 |
|  | 32¢ | 192 | ×0.2^16 = 0.0 |
|  | 41¢ | 10 | ×0.2^25 = 0.0 |
|  | 49¢ | 110 | ×0.2^33 = 0.0 |
|  | 56¢ | 10 | ×0.2^40 = 0.0 |
|  | 99¢ | 4,042 | ×0.2^83 = 0.0 |
| | | **Σ** | **1,137.8** |

`yours 100.0 / Σ 1,137.8 = 8.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 8.8% = $2.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 10 @ 15¢ → $0.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 130 (10 yours) | ×0.2^0 = 130.0 |
|  | 29¢ | 2 | ×0.2^14 = 0.0 |
|  | 35¢ | 2 | ×0.2^20 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,768 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **130.0** |

`yours 10.0 / Σ 130.0 = 7.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.7% = $0.30/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1,000 @ 3¢ → $0.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 14,125 (1,000 yours) | ×0.2^0 = 14,125.0 |
| | | **Σ** | **14,125.0** |

`yours 1,000.0 / Σ 14,125.0 = 7.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.1% = $0.27/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 19,245 (1,000 yours) | ×0.2^0 = 19,245.0 |
| | | **Σ** | **19,245.0** |

`yours 1,000.0 / Σ 19,245.0 = 5.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.2% = $0.20/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 22¢ → $0.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 39 | ×0.2^0 = 39.0 |
| ▶ | 22¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 94¢ | 31 | ×0.2^73 = 0.0 |
|  | 99¢ | 5,439 | ×0.2^78 = 0.0 |
| | | **Σ** | **41.0** |

`yours 2.0 / Σ 41.0 = 4.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.9% = $0.20/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> BUY 500 @ 2¢ → $0.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 11,750 (500 yours) | ×0.2^0 = 11,750.0 |
| | | **Σ** | **11,750.0** |

`yours 500.0 / Σ 11,750.0 = 4.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.3% = $0.18/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 32 @ 6¢ → $0.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 144 | ×0.2^0 = 144.0 |
| ▶ | 6¢ | 32 (32 yours) | ×0.2^1 = 6.3 |
|  | 5¢ | 2 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,535 | ×0.2^6 = 0.4 |
| | | **Σ** | **150.8** |

`yours 6.3 / Σ 150.8 = 4.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 4.2% = $0.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 590 @ 5¢ → $0.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 14,632 (590 yours) | ×0.2^0 = 14,632.0 |
| | | **Σ** | **14,632.0** |

`yours 590.0 / Σ 14,632.0 = 4.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 4.0% = $0.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 13,685 (500 yours) | ×0.2^0 = 13,685.0 |
| | | **Σ** | **13,685.0** |

`yours 500.0 / Σ 13,685.0 = 3.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.7% = $0.14/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 50 @ 10¢ → $0.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1,420 (50 yours) | ×0.2^0 = 1,419.7 |
|  | 50¢ | 25 | ×0.2^40 = 0.0 |
|  | 99¢ | 4,935 | ×0.2^89 = 0.0 |
| | | **Σ** | **1,419.7** |

`yours 50.0 / Σ 1,419.7 = 3.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.5% = $0.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 30¢ → $0.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 28¢ | 1 | ×0.2^0 = 0.9 |
|  | 29¢ | 49 | ×0.2^1 = 9.8 |
| ▶ | 30¢ | 25 (10 yours) | ×0.2^2 = 1.0 |
|  | 35¢ | 5 | ×0.2^7 = 0.0 |
|  | 40¢ | 105 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 98¢ | 1,833 | ×0.2^70 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^71 = 0.0 |
| | | **Σ** | **11.7** |

`yours 0.4 / Σ 11.7 = 3.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.4% = $0.13/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 11 @ 75¢ → $0.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 76¢ | 113 | ×0.2^0 = 113.0 |
| ▶ | 75¢ | 21 (11 yours) | ×0.2^1 = 4.2 |
|  | 49¢ | 120 | ×0.2^27 = 0.0 |
|  | 1¢ | 5,359 | ×0.2^75 = 0.0 |
| | | **Σ** | **117.2** |

`yours 2.2 / Σ 117.2 = 1.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.9% = $0.08/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 75¢ → $0.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 76¢ | 113 | ×0.2^0 = 113.0 |
| ▶ | 75¢ | 21 (10 yours) | ×0.2^1 = 4.2 |
|  | 49¢ | 120 | ×0.2^27 = 0.0 |
|  | 1¢ | 5,359 | ×0.2^75 = 0.0 |
| | | **Σ** | **117.2** |

`yours 2.0 / Σ 117.2 = 1.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.7% = $0.07/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 50 @ 20¢ → $0.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 3,336 (50 yours) | ×0.2^0 = 3,336.5 |
|  | 50¢ | 25 | ×0.2^30 = 0.0 |
|  | 99¢ | 2,201 | ×0.2^79 = 0.0 |
| | | **Σ** | **3,336.5** |

`yours 50.0 / Σ 3,336.5 = 1.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.5% = $0.06/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 67¢ → $0.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 3,952 (50 yours) | ×0.2^0 = 3,952.0 |
|  | 77¢ | 1,100 | ×0.2^10 = 0.0 |
| | | **Σ** | **3,952.0** |

`yours 50.0 / Σ 3,952.0 = 1.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.3% = $0.05/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 1 @ 8¢ → $0.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 85 (1 yours) | ×0.2^0 = 85.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,773 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **85.0** |

`yours 1.0 / Σ 85.0 = 1.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.2% = $0.05/day`  

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
<details><summary><code>ewc-usse-tx-2026-11-03-dem</code> BUY 50 @ 47¢ → $0.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 4,412 (50 yours) | ×0.2^0 = 4,412.0 |
|  | 46¢ | 10,069 | ×0.2^1 = 2,013.8 |
| | | **Σ** | **6,425.8** |

`yours 50.0 / Σ 6,425.8 = 0.8%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 0.8% = $0.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-tx-2026-11-03-dem` ← this one
2. `ewc-usse-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-tedcru</code> SELL 0 @ 21¢ → $0.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 103 (0 yours) | ×0.2^0 = 103.0 |
|  | 24¢ | 2 | ×0.2^3 = 0.0 |
|  | 28¢ | 862 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^29 = 0.0 |
|  | 99¢ | 4,534 | ×0.2^78 = 0.0 |
| | | **Σ** | **103.0** |

`yours 0.4 / Σ 103.0 = 0.4%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 0.4% = $0.01/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-30 | ~$43.67 | $20.48 | 47% |
| 2026-07-29 | ~$65.42 | $53.59 | 82% |
| 2026-07-28 | ~$148.78 | $79.65 | 54% |

Biggest gaps on 2026-07-30: `nocc-attgen-todblanche-2026-08-07` (est ~$3.65 → got $0.00), `scc-senate-gop-2026-11-03-51` (est ~$3.41 → got $1.26), `gsc-usfedgvmt-by-2026-10-01` (est ~$1.67 → got $0.00)

_2026-07-31 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,520 resting) | ~90.2% | ~$22.54 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (82,603 resting) | ~29.7% | ~$22.29 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (74,068 resting) | ~18.4% | ~$13.81 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (339,009 resting) | ~7.2% | ~$5.42 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (181,999 resting) | ~5.7% | ~$4.30 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (85,670 resting) | ~4.5% | ~$3.39 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (205,216 resting) | ~3.7% | ~$2.74 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (113,506 resting) | ~2.7% | ~$1.99 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,206 resting) | ~5.7% | ~$1.43 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (6,180 resting) | ~81.2% | ~$1.23 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (78,630 resting) | ~4.1% | ~$1.03 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (93,596 resting) | ~1.3% | ~$0.96 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,373.47 |
| Pending | $88.44 |
| Skipped | $1.21 |
| **Total earned** | **$1,463.12** |

1490 reward rows · 29 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-31 ⚠️ multi-day pending bucket | $67.96 | `██████` |
| 2026-07-30 | $20.48 | `██` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.59 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.35 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.73 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.96 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-02 5:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 3:38 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 1:26 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 12:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 11:30 AM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 10:01 AM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:37 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-02 5:24 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-02 2:48 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 11:57 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
