# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-02 3:38 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$27.51/day estimated (ceiling, not promise — details below)

**Earned:** $1,463.12 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-31: **$67.96** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-30: **$20.48** · 2026-07-29: **$53.59** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$24.51/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$14.36/day), `ewc-usgub-oh-2026-11-03-dem` (~$13.03/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$27.51/day (~$1.15/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 43.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (7,024 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 19.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~76.9% of bid side (5,401 resting ≥ 5,000 ✓) ≈ $2.96/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~49.0% of ask side (12,102 resting ≥ 5,000 ✓) ≈ $1.88/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 30.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~34.4% of ask side (12,462 resting ≥ 5,000 ✓) ≈ $1.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~30.2% of ask side (12,070 resting ≥ 5,000 ✓) ≈ $1.16/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 18.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~30.0% of ask side (12,132 resting ≥ 5,000 ✓) ≈ $1.15/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~28.6% of bid side (5,550 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~26.5% of ask side (12,221 resting ≥ 5,000 ✓) ≈ $1.02/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~24.8% of ask side (12,554 resting ≥ 5,000 ✓) ≈ $0.95/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 25.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~22.1% of ask side (12,182 resting ≥ 5,000 ✓) ≈ $0.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~21.3% of bid side (12,139 resting ≥ 5,000 ✓) ≈ $0.82/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 16.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~20.3% of ask side (6,016 resting ≥ 5,000 ✓) ≈ $5.06/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~18.5% of ask side (12,248 resting ≥ 5,000 ✓) ≈ $0.71/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~17.5% of bid side (25,839 resting ≥ 5,000 ✓) ≈ $0.67/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 64.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~16.8% of ask side (6,455 resting ≥ 5,000 ✓) ≈ $0.70/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 85.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~15.3% of bid side (5,515 resting ≥ 5,000 ✓) ≈ $0.64/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~13.5% of ask side (6,206 resting ≥ 5,000 ✓) ≈ $0.56/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 3.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~12.2% of bid side (8,379 resting ≥ 5,000 ✓) ≈ $0.47/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 11.0¢ | 35 | 0 | $100.00 | ✅ scoring — ~10.6% of bid side (5,956 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 34.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~9.5% of bid side (5,540 resting ≥ 5,000 ✓) ≈ $0.40/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~8.4% of bid side (12,159 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~8.4% of bid side (59,377 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 15.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~7.7% of ask side (12,203 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~6.4% of bid side (7,994 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 5.0¢ | 590 | 0 | $100.00 | ✅ scoring — ~6.2% of bid side (9,779 resting ≥ 5,000 ✓) ≈ $0.24/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 22.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~4.6% of ask side (8,535 resting ≥ 5,000 ✓) ≈ $0.19/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 6.0¢ | 32 | 1 | $100.00 | ✅ scoring — ~4.2% of bid side (5,713 resting ≥ 5,000 ✓) ≈ $0.16/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 5.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~3.8% of bid side (13,425 resting ≥ 5,000 ✓) ≈ $0.16/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 30.0¢ | 25 | 1 | $100.00 | ✅ scoring — ~3.8% of ask side (12,268 resting ≥ 5,000 ✓) ≈ $0.14/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 30.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~3.4% of ask side (12,320 resting ≥ 5,000 ✓) ≈ $0.13/day (pool ÷ 13 markets) |
| …and 36 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 1 @ 43¢ → $1.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 37¢ | 23 | ×0.1^6 = 0.0 |
|  | 9¢ | 750 | ×0.1^34 = 0.0 |
|  | 8¢ | 451 | ×0.1^35 = 0.0 |
|  | 2¢ | 375 | ×0.1^41 = 0.0 |
|  | 1¢ | 5,424 | ×0.1^42 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 100.0% = $1.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 50 @ 19¢ → $2.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 3 | ×0.2^0 = 3.0 |
| ▶ | 19¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 11¢ | 4 | ×0.2^9 = 0.0 |
|  | 9¢ | 4 | ×0.2^11 = 0.0 |
|  | 1¢ | 5,339 | ×0.2^19 = 0.0 |
| | | **Σ** | **13.0** |

`yours 10.0 / Σ 13.0 = 76.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 76.9% = $2.96/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 18 @ 15¢ → $1.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 37 (18 yours) | ×0.2^0 = 37.3 |
|  | 17¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **37.3** |

`yours 18.3 / Σ 37.3 = 49.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 49.0% = $1.88/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 30¢ → $1.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 125 (43 yours) | ×0.2^0 = 125.0 |
|  | 38¢ | 128 | ×0.2^8 = 0.0 |
|  | 43¢ | 37 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^20 = 0.0 |
|  | 98¢ | 1,871 | ×0.2^68 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^69 = 0.0 |
| | | **Σ** | **125.0** |

`yours 43.0 / Σ 125.0 = 34.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.4% = $1.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 10¢ → $1.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 33 (10 yours) | ×0.2^0 = 33.0 |
|  | 12¢ | 2 | ×0.2^2 = 0.1 |
|  | 16¢ | 3 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **33.1** |

`yours 10.0 / Σ 33.1 = 30.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.2% = $1.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 18¢ → $1.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 100 (30 yours) | ×0.2^0 = 100.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^81 = 0.0 |
| | | **Σ** | **100.0** |

`yours 30.0 / Σ 100.0 = 30.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.0% = $1.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $0.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 136 (40 yours) | ×0.2^0 = 135.7 |
|  | 11¢ | 128 | ×0.2^1 = 25.6 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **161.3** |

`yours 40.0 / Σ 161.3 = 24.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 24.8% = $0.95/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 50 @ 25¢ → $0.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 24¢ | 32 | ×0.2^0 = 32.1 |
| ▶ | 25¢ | 65 (50 yours) | ×0.2^1 = 13.0 |
|  | 26¢ | 1 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^26 = 0.0 |
|  | 98¢ | 1,782 | ×0.2^74 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^75 = 0.0 |
| | | **Σ** | **45.2** |

`yours 10.0 / Σ 45.2 = 22.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 22.1% = $0.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $0.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1,949 (500 yours) | ×0.2^0 = 1,949.0 |
|  | 2¢ | 9,990 | ×0.2^2 = 399.6 |
| | | **Σ** | **2,348.6** |

`yours 500.0 / Σ 2,348.6 = 21.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 21.3% = $0.82/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 16¢ → $5.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 494 (100 yours) | ×0.2^0 = 493.8 |
|  | 32¢ | 192 | ×0.2^16 = 0.0 |
|  | 41¢ | 10 | ×0.2^25 = 0.0 |
|  | 49¢ | 110 | ×0.2^33 = 0.0 |
|  | 56¢ | 10 | ×0.2^40 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^83 = 0.0 |
| | | **Σ** | **493.8** |

`yours 100.0 / Σ 493.8 = 20.3%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 20.3% = $5.06/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 16¢ → $0.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 87 (20 yours) | ×0.2^0 = 87.2 |
|  | 17¢ | 106 | ×0.2^1 = 21.2 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^82 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^83 = 0.0 |
| | | **Σ** | **108.4** |

`yours 20.0 / Σ 108.4 = 18.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.5% = $0.71/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 692 | ×0.2^0 = 692.0 |
| ▶ | 1¢ | 25,147 (5,000 yours) | ×0.2^1 = 5,029.4 |
| | | **Σ** | **5,721.4** |

`yours 1,000.0 / Σ 5,721.4 = 17.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.5% = $0.67/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 30 @ 64¢ → $0.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 64¢ | 178 (30 yours) | ×0.2^0 = 178.0 |
|  | 67¢ | 50 | ×0.2^3 = 0.4 |
|  | 77¢ | 1,968 | ×0.2^13 = 0.0 |
|  | 79¢ | 1,865 | ×0.2^15 = 0.0 |
|  | 80¢ | 190 | ×0.2^16 = 0.0 |
|  | 90¢ | 2 | ×0.2^26 = 0.0 |
|  | 92¢ | 1 | ×0.2^28 = 0.0 |
|  | 99¢ | 2,201 | ×0.2^35 = 0.0 |
| | | **Σ** | **178.4** |

`yours 30.0 / Σ 178.4 = 16.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.8% = $0.70/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 85¢ → $0.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 65 (10 yours) | ×0.2^0 = 65.3 |
|  | 1¢ | 5,450 | ×0.2^84 = 0.0 |
| | | **Σ** | **65.3** |

`yours 10.0 / Σ 65.3 = 15.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 15.3% = $0.64/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180` ← this one
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
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 50 @ 10¢ → $0.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 372 (50 yours) | ×0.2^0 = 371.7 |
|  | 50¢ | 25 | ×0.2^40 = 0.0 |
|  | 99¢ | 5,809 | ×0.2^89 = 0.0 |
| | | **Σ** | **371.7** |

`yours 50.0 / Σ 371.7 = 13.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 13.5% = $0.56/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1,000 @ 3¢ → $0.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,179 (1,000 yours) | ×0.2^0 = 8,179.0 |
| | | **Σ** | **8,179.0** |

`yours 1,000.0 / Σ 8,179.0 = 12.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 12.2% = $0.47/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 35 @ 11¢ → $0.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 329 (35 yours) | ×0.2^0 = 329.0 |
|  | 4¢ | 173 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,454 | ×0.2^10 = 0.0 |
| | | **Σ** | **329.0** |

`yours 35.0 / Σ 329.0 = 10.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 10.6% = $0.41/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 20 @ 34¢ → $0.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 35¢ | 38 | ×0.2^0 = 38.0 |
| ▶ | 34¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 33¢ | 3 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,479 | ×0.2^34 = 0.0 |
| | | **Σ** | **42.1** |

`yours 4.0 / Σ 42.1 = 9.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 9.5% = $0.40/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 11,856 (1,000 yours) | ×0.2^0 = 11,856.0 |
| | | **Σ** | **11,856.0** |

`yours 1,000.0 / Σ 11,856.0 = 8.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.4% = $0.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5,000 @ 1¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 59,377 (5,000 yours) | ×0.2^0 = 59,376.9 |
| | | **Σ** | **59,376.9** |

`yours 5,000.0 / Σ 59,376.9 = 8.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.4% = $0.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 7,794 (500 yours) | ×0.2^0 = 7,794.0 |
| | | **Σ** | **7,794.0** |

`yours 500.0 / Σ 7,794.0 = 6.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.4% = $0.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 590 @ 5¢ → $0.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 9,579 (590 yours) | ×0.2^0 = 9,579.0 |
| | | **Σ** | **9,579.0** |

`yours 590.0 / Σ 9,579.0 = 6.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.2% = $0.24/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 22¢ → $0.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 41 | ×0.2^0 = 41.0 |
| ▶ | 22¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 23¢ | 1 | ×0.2^2 = 0.1 |
|  | 94¢ | 19 | ×0.2^73 = 0.0 |
|  | 99¢ | 8,464 | ×0.2^78 = 0.0 |
| | | **Σ** | **43.0** |

`yours 2.0 / Σ 43.0 = 4.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.6% = $0.19/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 500 @ 5¢ → $0.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 13,225 (500 yours) | ×0.2^0 = 13,225.0 |
| | | **Σ** | **13,225.0** |

`yours 500.0 / Σ 13,225.0 = 3.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.8% = $0.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 25 @ 30¢ → $0.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 29¢ | 128 | ×0.2^0 = 128.0 |
| ▶ | 30¢ | 25 (25 yours) | ×0.2^1 = 5.0 |
|  | 50¢ | 100 | ×0.2^21 = 0.0 |
|  | 98¢ | 1,814 | ×0.2^69 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^70 = 0.0 |
| | | **Σ** | **133.0** |

`yours 5.0 / Σ 133.0 = 3.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.8% = $0.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 30¢ → $0.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 28¢ | 1 | ×0.2^0 = 0.9 |
|  | 29¢ | 50 | ×0.2^1 = 10.0 |
| ▶ | 30¢ | 25 (10 yours) | ×0.2^2 = 1.0 |
|  | 35¢ | 5 | ×0.2^7 = 0.0 |
|  | 40¢ | 105 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 98¢ | 1,833 | ×0.2^70 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^71 = 0.0 |
| | | **Σ** | **11.9** |

`yours 0.4 / Σ 11.9 = 3.4%`  
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
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,148 resting) | ~98.0% | ~$24.51 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (87,523 resting) | ~19.2% | ~$14.36 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,140 resting) | ~17.4% | ~$13.03 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (91,826 resting) | ~8.7% | ~$6.52 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (344,561 resting) | ~5.7% | ~$4.25 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (183,875 resting) | ~5.3% | ~$3.95 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (75,219 resting) | ~8.0% | ~$2.01 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (113,508 resting) | ~2.7% | ~$1.99 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (78,645 resting) | ~4.0% | ~$1.01 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (93,373 resting) | ~1.3% | ~$0.97 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (89,981 resting) | ~1.3% | ~$0.95 |
| `cranc-uspres28-12-31-2026-stesmi` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (9,431 resting) | ~58.5% | ~$0.89 |

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
| 2026-08-02 3:38 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 1:26 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 12:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 11:30 AM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 10:01 AM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:37 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-02 5:24 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-02 2:48 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 11:57 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 9:53 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
