# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-02 1:26 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$24.90/day estimated (ceiling, not promise — details below)

**Earned:** $1,463.12 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-31: **$67.96** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-30: **$20.48** · 2026-07-29: **$53.59** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — SELL at the best price, ~$14.37/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$10.51/day), `ewc-usse-me-2026-11-03-rep` (~$6.87/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$24.90/day (~$1.04/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-47` | BUY | 6.0¢ | 32 | 0 | $100.00 | ✅ scoring — ~78.7% of bid side (25,569 resting ≥ 5,000 ✓) ≈ $3.03/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 43.0¢ | 34 | 0 | $25.00 | ✅ scoring — ~75.5% of bid side (6,819 resting ≥ 2,000 ✓) ≈ $0.94/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 25.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~41.3% of ask side (11,972 resting ≥ 5,000 ✓) ≈ $1.59/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~40.4% of ask side (11,909 resting ≥ 5,000 ✓) ≈ $1.55/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~30.4% of ask side (12,222 resting ≥ 5,000 ✓) ≈ $1.17/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 30.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~29.3% of ask side (12,375 resting ≥ 5,000 ✓) ≈ $1.13/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 18.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~25.2% of ask side (11,951 resting ≥ 5,000 ✓) ≈ $0.97/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~24.8% of ask side (12,031 resting ≥ 5,000 ✓) ≈ $0.96/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~21.3% of bid side (12,139 resting ≥ 5,000 ✓) ≈ $0.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~21.2% of ask side (11,949 resting ≥ 5,000 ✓) ≈ $0.82/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 11.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~20.9% of bid side (5,628 resting ≥ 5,000 ✓) ≈ $0.87/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~20.4% of ask side (11,884 resting ≥ 5,000 ✓) ≈ $0.78/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~19.3% of bid side (25,932 resting ≥ 5,000 ✓) ≈ $0.74/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~19.3% of bid side (5,719 resting ≥ 5,000 ✓) ≈ $0.74/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 64.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~16.0% of ask side (6,188 resting ≥ 5,000 ✓) ≈ $0.67/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 19.0¢ | 50 | 2 | $100.00 | ✅ scoring — ~14.1% of bid side (5,529 resting ≥ 5,000 ✓) ≈ $0.54/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 30.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~14.0% of ask side (12,090 resting ≥ 5,000 ✓) ≈ $0.54/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~13.3% of ask side (5,377 resting ≥ 5,000 ✓) ≈ $0.56/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 3.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~11.5% of bid side (8,879 resting ≥ 5,000 ✓) ≈ $0.44/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 11.0¢ | 35 | 0 | $100.00 | ✅ scoring — ~10.9% of bid side (5,960 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 5.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~8.9% of bid side (5,800 resting ≥ 5,000 ✓) ≈ $0.37/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | SELL | 16.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~8.8% of ask side (5,364 resting ≥ 5,000 ✓) ≈ $2.19/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~8.6% of bid side (11,967 resting ≥ 5,000 ✓) ≈ $0.33/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 5.0¢ | 590 | 0 | $100.00 | ✅ scoring — ~6.5% of bid side (9,316 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~6.0% of bid side (8,494 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 2.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~4.4% of bid side (11,450 resting ≥ 5,000 ✓) ≈ $0.19/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 20.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~4.1% of ask side (8,442 resting ≥ 5,000 ✓) ≈ $0.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 1.0¢ | 5,000 | 5 | $100.00 | ✅ scoring — ~4.0% of bid side (25,569 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 30.0¢ | 25 | 1 | $100.00 | ✅ scoring — ~3.8% of ask side (12,068 resting ≥ 5,000 ✓) ≈ $0.14/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 22.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~2.7% of ask side (8,338 resting ≥ 5,000 ✓) ≈ $0.11/day (pool ÷ 12 markets) |
| …and 36 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 32 @ 6¢ → $3.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 32 (32 yours) | ×0.2^0 = 31.7 |
|  | 5¢ | 2 | ×0.2^1 = 0.4 |
|  | 1¢ | 25,535 | ×0.2^5 = 8.2 |
| | | **Σ** | **40.3** |

`yours 31.7 / Σ 40.3 = 78.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 78.7% = $3.03/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 34 @ 43¢ → $0.94/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 45 (34 yours) | ×0.1^0 = 45.0 |
|  | 39¢ | 24 | ×0.1^4 = 0.0 |
|  | 9¢ | 500 | ×0.1^34 = 0.0 |
|  | 8¢ | 451 | ×0.1^35 = 0.0 |
|  | 2¢ | 375 | ×0.1^41 = 0.0 |
|  | 1¢ | 5,424 | ×0.1^42 = 0.0 |
| | | **Σ** | **45.0** |

`yours 34.0 / Σ 45.0 = 75.5%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 75.5% = $0.94/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 50 @ 25¢ → $1.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 121 (50 yours) | ×0.2^0 = 121.1 |
|  | 50¢ | 100 | ×0.2^25 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^73 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^74 = 0.0 |
| | | **Σ** | **121.1** |

`yours 50.0 / Σ 121.1 = 41.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 41.3% = $1.59/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 18 @ 15¢ → $1.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 45 (18 yours) | ×0.2^0 = 45.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $1.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 132 (40 yours) | ×0.2^0 = 131.7 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **131.7** |

`yours 40.0 / Σ 131.7 = 30.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.4% = $1.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 30¢ → $1.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 124 (43 yours) | ×0.2^0 = 124.0 |
|  | 31¢ | 114 | ×0.2^1 = 22.8 |
|  | 38¢ | 128 | ×0.2^8 = 0.0 |
|  | 43¢ | 37 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^20 = 0.0 |
|  | 98¢ | 1,871 | ×0.2^68 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^69 = 0.0 |
| | | **Σ** | **146.8** |

`yours 43.0 / Σ 146.8 = 29.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.3% = $1.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 18¢ → $0.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 119 (30 yours) | ×0.2^0 = 119.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^81 = 0.0 |
| | | **Σ** | **119.0** |

`yours 30.0 / Σ 119.0 = 25.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.2% = $0.97/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $0.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 161 (40 yours) | ×0.2^0 = 161.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **161.0** |

`yours 40.0 / Σ 161.0 = 24.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 24.8% = $0.96/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 16¢ → $0.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 94 (20 yours) | ×0.2^0 = 94.2 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^82 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^83 = 0.0 |
| | | **Σ** | **94.2** |

`yours 20.0 / Σ 94.2 = 21.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 21.2% = $0.82/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 100 @ 11¢ → $0.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 478 (100 yours) | ×0.2^0 = 478.0 |
|  | 1¢ | 5,150 | ×0.2^10 = 0.0 |
| | | **Σ** | **478.0** |

`yours 100.0 / Σ 478.0 = 20.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 20.9% = $0.87/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 10¢ → $0.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 49 (10 yours) | ×0.2^0 = 49.0 |
|  | 16¢ | 3 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5,000 @ 1¢ → $0.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 25,932 (5,000 yours) | ×0.2^0 = 25,931.9 |
| | | **Σ** | **25,931.9** |

`yours 5,000.0 / Σ 25,931.9 = 19.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.3% = $0.74/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 100 @ 20¢ → $0.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 519 (100 yours) | ×0.2^0 = 519.0 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **519.0** |

`yours 100.0 / Σ 519.0 = 19.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.3% = $0.74/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 30 @ 64¢ → $0.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 64¢ | 187 (30 yours) | ×0.2^0 = 187.0 |
|  | 67¢ | 50 | ×0.2^3 = 0.4 |
|  | 77¢ | 1,893 | ×0.2^13 = 0.0 |
|  | 79¢ | 1,865 | ×0.2^15 = 0.0 |
|  | 90¢ | 1 | ×0.2^26 = 0.0 |
|  | 92¢ | 1 | ×0.2^28 = 0.0 |
|  | 99¢ | 2,191 | ×0.2^35 = 0.0 |
| | | **Σ** | **187.4** |

`yours 30.0 / Σ 187.4 = 16.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.0% = $0.67/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 50 @ 19¢ → $0.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 12 | ×0.2^0 = 12.0 |
|  | 20¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 19¢ | 50 (50 yours) | ×0.2^2 = 2.0 |
|  | 9¢ | 4 | ×0.2^12 = 0.0 |
|  | 1¢ | 5,462 | ×0.2^20 = 0.0 |
| | | **Σ** | **14.2** |

`yours 2.0 / Σ 14.2 = 14.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.1% = $0.54/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 30¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 29¢ | 1 | ×0.2^0 = 0.9 |
| ▶ | 30¢ | 67 (10 yours) | ×0.2^1 = 13.4 |
|  | 35¢ | 5 | ×0.2^6 = 0.0 |
|  | 40¢ | 105 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^21 = 0.0 |
|  | 98¢ | 1,811 | ×0.2^69 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^70 = 0.0 |
| | | **Σ** | **14.3** |

`yours 2.0 / Σ 14.3 = 14.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.0% = $0.54/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 50 @ 10¢ → $0.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 375 (50 yours) | ×0.2^0 = 374.7 |
|  | 50¢ | 25 | ×0.2^40 = 0.0 |
|  | 99¢ | 4,977 | ×0.2^89 = 0.0 |
| | | **Σ** | **374.7** |

`yours 50.0 / Σ 374.7 = 13.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 13.3% = $0.56/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1,000 @ 3¢ → $0.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,679 (1,000 yours) | ×0.2^0 = 8,679.0 |
| | | **Σ** | **8,679.0** |

`yours 1,000.0 / Σ 8,679.0 = 11.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.5% = $0.44/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 35 @ 11¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 322 (35 yours) | ×0.2^0 = 322.0 |
|  | 4¢ | 173 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,465 | ×0.2^10 = 0.0 |
| | | **Σ** | **322.0** |

`yours 35.0 / Σ 322.0 = 10.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 10.9% = $0.42/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 500 @ 5¢ → $0.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 5,600 (500 yours) | ×0.2^0 = 5,600.0 |
| | | **Σ** | **5,600.0** |

`yours 500.0 / Σ 5,600.0 = 8.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 8.9% = $0.37/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 16¢ → $2.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1,140 (100 yours) | ×0.2^0 = 1,139.8 |
|  | 32¢ | 192 | ×0.2^16 = 0.0 |
|  | 49¢ | 100 | ×0.2^33 = 0.0 |
|  | 99¢ | 3,932 | ×0.2^83 = 0.0 |
| | | **Σ** | **1,139.8** |

`yours 100.0 / Σ 1,139.8 = 8.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 8.8% = $2.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 11,664 (1,000 yours) | ×0.2^0 = 11,664.0 |
| | | **Σ** | **11,664.0** |

`yours 1,000.0 / Σ 11,664.0 = 8.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.6% = $0.33/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 590 @ 5¢ → $0.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 9,116 (590 yours) | ×0.2^0 = 9,116.0 |
| | | **Σ** | **9,116.0** |

`yours 590.0 / Σ 9,116.0 = 6.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.5% = $0.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,294 (500 yours) | ×0.2^0 = 8,294.0 |
| | | **Σ** | **8,294.0** |

`yours 500.0 / Σ 8,294.0 = 6.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.0% = $0.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> BUY 500 @ 2¢ → $0.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 11,250 (500 yours) | ×0.2^0 = 11,250.0 |
| | | **Σ** | **11,250.0** |

`yours 500.0 / Σ 11,250.0 = 4.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.4% = $0.19/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 50 @ 20¢ → $0.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 1,210 (50 yours) | ×0.2^0 = 1,209.5 |
|  | 50¢ | 25 | ×0.2^30 = 0.0 |
|  | 99¢ | 7,208 | ×0.2^79 = 0.0 |
| | | **Σ** | **1,209.5** |

`yours 50.0 / Σ 1,209.5 = 4.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.1% = $0.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 5,000 @ 1¢ → $0.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 32 | ×0.2^0 = 31.7 |
|  | 5¢ | 2 | ×0.2^1 = 0.4 |
| ▶ | 1¢ | 25,535 (5,000 yours) | ×0.2^5 = 8.2 |
| | | **Σ** | **40.3** |

`yours 1.6 / Σ 40.3 = 4.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 4.0% = $0.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 25 @ 30¢ → $0.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 29¢ | 128 | ×0.2^0 = 128.0 |
| ▶ | 30¢ | 25 (25 yours) | ×0.2^1 = 5.0 |
|  | 50¢ | 100 | ×0.2^21 = 0.0 |
|  | 98¢ | 1,814 | ×0.2^69 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^70 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 22¢ → $0.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 67 | ×0.2^0 = 67.0 |
| ▶ | 22¢ | 29 (10 yours) | ×0.2^1 = 5.8 |
|  | 99¢ | 8,242 | ×0.2^78 = 0.0 |
| | | **Σ** | **72.8** |

`yours 2.0 / Σ 72.8 = 2.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 2.7% = $0.11/day`  

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
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (87,295 resting) | ~19.2% | ~$14.37 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,415 resting) | ~14.0% | ~$10.51 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (182,698 resting) | ~9.2% | ~$6.87 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,500 resting) | ~22.0% | ~$5.51 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (75,217 resting) | ~9.8% | ~$2.45 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (113,509 resting) | ~2.7% | ~$1.99 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (343,576 resting) | ~1.8% | ~$1.35 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,874 resting) | ~81.2% | ~$1.23 |
| `cranc-uspres28-12-31-2026-rahema` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,573 resting) | ~66.9% | ~$1.01 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (78,440 resting) | ~4.0% | ~$1.01 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (89,606 resting) | ~1.3% | ~$0.97 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (94,159 resting) | ~1.2% | ~$0.91 |

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
| 2026-08-02 1:26 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 12:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 11:30 AM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 10:01 AM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:37 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-02 5:24 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-02 2:48 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 11:57 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 9:53 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 8:15 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
