# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-04 2:43 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$72.82/day estimated (ceiling, not promise — details below)

**Earned:** $1,529.47 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-02: **$14.05** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-01: **$52.30** · 2026-07-31: **$67.96** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$24.82/day for 200 contracts. Runners-up: `ewc-usgub-ca-2026-11-03-xavbec` (~$24.67/day), `apdc-jerpowgov-2026-12-31` (~$17.20/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$72.82/day (~$3.03/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 67.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~99.7% of ask side (12,332 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 88.0¢ | 34 | 0 | $100.00 | ✅ scoring — ~98.8% of ask side (12,126 resting ≥ 5,000 ✓) ≈ $4.12/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 12.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~98.4% of bid side (5,603 resting ≥ 5,000 ✓) ≈ $3.79/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 26.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~96.5% of ask side (12,199 resting ≥ 5,000 ✓) ≈ $3.71/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 24.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~88.2% of bid side (5,482 resting ≥ 5,000 ✓) ≈ $3.39/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 21.0¢ | 80 | 0 | $100.00 | ✅ scoring — ~85.0% of ask side (10,336 resting ≥ 5,000 ✓) ≈ $21.26/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~76.7% of ask side (12,050 resting ≥ 5,000 ✓) ≈ $2.95/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 58.0¢ | 12 | 0 | $100.00 | ✅ scoring — ~73.2% of ask side (7,080 resting ≥ 5,000 ✓) ≈ $3.05/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 14.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~69.4% of bid side (5,484 resting ≥ 5,000 ✓) ≈ $2.67/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~68.0% of ask side (12,065 resting ≥ 5,000 ✓) ≈ $2.62/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 41 | 0 | $100.00 | ✅ scoring — ~67.2% of ask side (12,147 resting ≥ 5,000 ✓) ≈ $2.59/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 86.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~66.6% of bid side (5,481 resting ≥ 5,000 ✓) ≈ $2.77/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 9.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~53.9% of ask side (12,278 resting ≥ 5,000 ✓) ≈ $2.07/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 79.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~43.4% of bid side (5,525 resting ≥ 5,000 ✓) ≈ $1.81/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~42.5% of ask side (12,165 resting ≥ 5,000 ✓) ≈ $1.64/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~41.3% of ask side (12,311 resting ≥ 5,000 ✓) ≈ $1.59/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~20.9% of bid side (4,085 resting ≥ 2,500 ✓) ≈ $0.72/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~20.0% of bid side (5,359 resting ≥ 5,000 ✓) ≈ $0.83/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~14.8% of bid side (5,558 resting ≥ 5,000 ✓) ≈ $0.62/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 30 | 3 | $100.00 | ✅ scoring — ~11.7% of ask side (12,102 resting ≥ 5,000 ✓) ≈ $0.49/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 1 | $100.00 | ✅ scoring — ~11.5% of ask side (12,409 resting ≥ 5,000 ✓) ≈ $0.44/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 7.0¢ | 400 | 0 | $100.00 | ✅ scoring — ~10.1% of bid side (9,161 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 18.0¢ | 35 | 0 | $100.00 | ✅ scoring — ~10.1% of bid side (5,551 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 20.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~9.9% of ask side (5,474 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 7.0¢ | 3 | 1 | $100.00 | ✅ scoring — ~9.7% of bid side (25,474 resting ≥ 5,000 ✓) ≈ $0.37/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~8.4% of ask side (5,939 resting ≥ 5,000 ✓) ≈ $0.35/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 9.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~7.2% of ask side (12,409 resting ≥ 5,000 ✓) ≈ $0.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 9.0¢ | 75 | 0 | $100.00 | ✅ scoring — ~6.9% of ask side (12,389 resting ≥ 5,000 ✓) ≈ $0.27/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 9.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~5.8% of ask side (5,515 resting ≥ 5,000 ✓) ≈ $0.24/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 8.0¢ | 75 | 0 | $100.00 | ✅ scoring — ~5.1% of ask side (12,864 resting ≥ 5,000 ✓) ≈ $0.20/day (pool ÷ 13 markets) |
| …and 58 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 67¢ → $4.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 69¢ | 3 | ×0.2^2 = 0.1 |
|  | 74¢ | 1 | ×0.2^7 = 0.0 |
|  | 83¢ | 164 | ×0.2^16 = 0.0 |
|  | 90¢ | 1 | ×0.2^23 = 0.0 |
|  | 99¢ | 12,113 | ×0.2^32 = 0.0 |
| | | **Σ** | **50.1** |

`yours 50.0 / Σ 50.1 = 99.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.7% = $4.16/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 34 @ 88¢ → $4.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 34 (34 yours) | ×0.2^0 = 34.0 |
|  | 90¢ | 10 | ×0.2^2 = 0.4 |
|  | 99¢ | 12,082 | ×0.2^11 = 0.0 |
| | | **Σ** | **34.4** |

`yours 34.0 / Σ 34.4 = 98.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 98.8% = $4.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 5 @ 12¢ → $3.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 8¢ | 50 | ×0.2^4 = 0.1 |
|  | 1¢ | 5,548 | ×0.2^11 = 0.0 |
| | | **Σ** | **5.1** |

`yours 5.0 / Σ 5.1 = 98.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.4% = $3.79/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 26¢ → $3.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 27¢ | 1 | ×0.2^1 = 0.2 |
|  | 43¢ | 100 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^24 = 0.0 |
|  | 98¢ | 1,792 | ×0.2^72 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^73 = 0.0 |
| | | **Σ** | **5.2** |

`yours 5.0 / Σ 5.2 = 96.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 96.5% = $3.71/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 24¢ → $3.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 3 | ×0.2^3 = 0.0 |
|  | 20¢ | 69 | ×0.2^4 = 0.1 |
|  | 1¢ | 5,409 | ×0.2^23 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.2% = $3.39/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 80 @ 21¢ → $21.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 80 (80 yours) | ×0.2^0 = 80.2 |
|  | 22¢ | 70 | ×0.2^1 = 14.0 |
|  | 25¢ | 34 | ×0.2^4 = 0.1 |
|  | 26¢ | 192 | ×0.2^5 = 0.1 |
|  | 46¢ | 200 | ×0.2^25 = 0.0 |
|  | 48¢ | 105 | ×0.2^27 = 0.0 |
|  | 99¢ | 9,655 | ×0.2^78 = 0.0 |
| | | **Σ** | **94.3** |

`yours 80.2 / Σ 94.3 = 85.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 85.0% = $21.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 3 @ 15¢ → $2.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 4 (3 yours) | ×0.2^0 = 4.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,745 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **4.3** |

`yours 3.3 / Σ 4.3 = 76.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 76.7% = $2.95/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 12 @ 58¢ → $3.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 12 (12 yours) | ×0.2^0 = 12.0 |
|  | 60¢ | 110 | ×0.2^2 = 4.4 |
|  | 81¢ | 107 | ×0.2^23 = 0.0 |
|  | 99¢ | 6,851 | ×0.2^41 = 0.0 |
| | | **Σ** | **16.4** |

`yours 12.0 / Σ 16.4 = 73.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 73.2% = $3.05/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 15 @ 14¢ → $2.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 21 (15 yours) | ×0.2^0 = 21.0 |
|  | 13¢ | 1 | ×0.2^1 = 0.2 |
|  | 12¢ | 10 | ×0.2^2 = 0.4 |
|  | 6¢ | 32 | ×0.2^8 = 0.0 |
|  | 1¢ | 5,420 | ×0.2^13 = 0.0 |
| | | **Σ** | **21.6** |

`yours 15.0 / Σ 21.6 = 69.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 69.4% = $2.67/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 15 @ 18¢ → $2.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 22 (15 yours) | ×0.2^0 = 22.0 |
|  | 20¢ | 1 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,741 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^81 = 0.0 |
| | | **Σ** | **22.1** |

`yours 15.0 / Σ 22.1 = 68.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.0% = $2.62/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 41 @ 22¢ → $2.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 61 (41 yours) | ×0.2^0 = 61.2 |
|  | 24¢ | 1 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 98¢ | 1,784 | ×0.2^76 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^77 = 0.0 |
| | | **Σ** | **61.2** |

`yours 41.2 / Σ 61.2 = 67.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.2% = $2.59/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 20 @ 86¢ → $2.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 86¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 84¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^85 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.6% = $2.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 9¢ → $2.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 45 (30 yours) | ×0.2^0 = 45.0 |
|  | 11¢ | 101 | ×0.2^2 = 4.0 |
|  | 12¢ | 831 | ×0.2^3 = 6.6 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **55.7** |

`yours 30.0 / Σ 55.7 = 53.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.9% = $2.07/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 20 @ 79¢ → $1.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 39 (20 yours) | ×0.2^0 = 39.0 |
|  | 78¢ | 35 | ×0.2^1 = 7.0 |
|  | 77¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,450 | ×0.2^78 = 0.0 |
| | | **Σ** | **46.1** |

`yours 20.0 / Σ 46.1 = 43.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 43.4% = $1.81/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 94 (40 yours) | ×0.2^0 = 94.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **94.0** |

`yours 40.0 / Σ 94.0 = 42.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 42.5% = $1.64/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 50 @ 10¢ → $1.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 101 (50 yours) | ×0.2^0 = 101.0 |
|  | 11¢ | 100 | ×0.2^1 = 20.0 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,808 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **121.0** |

`yours 50.0 / Σ 121.0 = 41.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 41.3% = $1.59/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 376 | ×0.35^0 = 376.0 |
| ▶ | 1¢ | 3,709 (1,000 yours) | ×0.35^1 = 1,298.1 |
| | | **Σ** | **1,674.1** |

`yours 350.0 / Σ 1,674.1 = 20.9%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 20.9% = $0.72/day`  

<details><summary>÷ 73 markets in this race (40 known) — tap to list</summary>

1. `tec-cbb-champ-2027-04-05-w-ala`
2. `tec-cbb-champ-2027-04-05-w-ark`
3. `tec-cbb-champ-2027-04-05-w-arz`
4. `tec-cbb-champ-2027-04-05-w-aubrn`
5. `tec-cbb-champ-2027-04-05-w-bayl`
6. `tec-cbb-champ-2027-04-05-w-boise`
7. `tec-cbb-champ-2027-04-05-w-boscol`
8. `tec-cbb-champ-2027-04-05-w-butl`
9. `tec-cbb-champ-2027-04-05-w-byu`
10. `tec-cbb-champ-2027-04-05-w-cin`
11. `tec-cbb-champ-2027-04-05-w-clmsn`
12. `tec-cbb-champ-2027-04-05-w-colst`
13. `tec-cbb-champ-2027-04-05-w-creigh`
14. `tec-cbb-champ-2027-04-05-w-day`
15. `tec-cbb-champ-2027-04-05-w-duke`
16. `tec-cbb-champ-2027-04-05-w-fl`
17. `tec-cbb-champ-2027-04-05-w-flst`
18. `tec-cbb-champ-2027-04-05-w-george`
19. `tec-cbb-champ-2027-04-05-w-gnzg`
20. `tec-cbb-champ-2027-04-05-w-hou`
21. `tec-cbb-champ-2027-04-05-w-ill`
22. `tec-cbb-champ-2027-04-05-w-ind`
23. `tec-cbb-champ-2027-04-05-w-iowa`
24. `tec-cbb-champ-2027-04-05-w-iowast`
25. `tec-cbb-champ-2027-04-05-w-kan`
26. `tec-cbb-champ-2027-04-05-w-lou`
27. `tec-cbb-champ-2027-04-05-w-loych`
28. `tec-cbb-champ-2027-04-05-w-lsutig`
29. `tec-cbb-champ-2027-04-05-w-marq`
30. `tec-cbb-champ-2027-04-05-w-mia`
31. `tec-cbb-champ-2027-04-05-w-mich`
32. `tec-cbb-champ-2027-04-05-w-miss`
33. `tec-cbb-champ-2027-04-05-w-missr`
34. `tec-cbb-champ-2027-04-05-w-mphs`
35. `tec-cbb-champ-2027-04-05-w-mspst`
36. `tec-cbb-champ-2027-04-05-w-mst`
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 30 @ 85¢ → $0.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 150 (30 yours) | ×0.2^0 = 150.2 |
|  | 83¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,208 | ×0.2^84 = 0.0 |
| | | **Σ** | **150.3** |

`yours 30.0 / Σ 150.3 = 20.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 20.0% = $0.83/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 82¢ → $0.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 68 (10 yours) | ×0.2^0 = 67.7 |
|  | 80¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,489 | ×0.2^81 = 0.0 |
| | | **Σ** | **67.7** |

`yours 10.0 / Σ 67.7 = 14.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 14.8% = $0.62/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 30 @ 47¢ → $0.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 44¢ | 2 | ×0.2^0 = 1.8 |
|  | 46¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 47¢ | 30 (30 yours) | ×0.2^3 = 0.2 |
|  | 52¢ | 1 | ×0.2^8 = 0.0 |
|  | 69¢ | 100 | ×0.2^25 = 0.0 |
|  | 99¢ | 11,968 | ×0.2^55 = 0.0 |
| | | **Σ** | **2.1** |

`yours 0.2 / Σ 2.1 = 11.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.7% = $0.49/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $0.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 62 | ×0.2^0 = 61.6 |
| ▶ | 10¢ | 41 (40 yours) | ×0.2^1 = 8.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 30¢ | 112 | ×0.2^21 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,892 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **69.8** |

`yours 8.0 / Σ 69.8 = 11.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.5% = $0.44/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 400 @ 7¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 3,941 (400 yours) | ×0.2^0 = 3,941.0 |
|  | 5¢ | 20 | ×0.2^2 = 0.8 |
|  | 1¢ | 5,200 | ×0.2^6 = 0.3 |
| | | **Σ** | **3,942.1** |

`yours 400.0 / Σ 3,942.1 = 10.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 10.1% = $0.42/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 35 @ 18¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 345 (35 yours) | ×0.2^0 = 345.0 |
|  | 16¢ | 6 | ×0.2^2 = 0.3 |
|  | 1¢ | 5,200 | ×0.2^17 = 0.0 |
| | | **Σ** | **345.3** |

`yours 35.0 / Σ 345.3 = 10.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 10.1% = $0.42/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 30 @ 20¢ → $0.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 304 (30 yours) | ×0.2^0 = 304.0 |
|  | 22¢ | 1 | ×0.2^2 = 0.1 |
|  | 99¢ | 5,169 | ×0.2^79 = 0.0 |
| | | **Σ** | **304.1** |

`yours 30.0 / Σ 304.1 = 9.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 9.9% = $0.41/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 3 @ 7¢ → $0.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 5 | ×0.2^0 = 5.1 |
| ▶ | 7¢ | 3 (3 yours) | ×0.2^1 = 0.6 |
|  | 2¢ | 232 | ×0.2^6 = 0.0 |
|  | 1¢ | 25,234 | ×0.2^7 = 0.3 |
| | | **Σ** | **6.0** |

`yours 0.6 / Σ 6.0 = 9.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.7% = $0.37/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 10 @ 10¢ → $0.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 118 (10 yours) | ×0.2^0 = 118.3 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 14¢ | 100 | ×0.2^4 = 0.2 |
|  | 20¢ | 1 | ×0.2^10 = 0.0 |
|  | 50¢ | 25 | ×0.2^40 = 0.0 |
|  | 99¢ | 5,694 | ×0.2^89 = 0.0 |
| | | **Σ** | **118.5** |

`yours 10.0 / Σ 118.5 = 8.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 8.4% = $0.35/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 5 @ 9¢ → $0.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 62 (5 yours) | ×0.2^0 = 61.6 |
|  | 10¢ | 41 | ×0.2^1 = 8.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 30¢ | 112 | ×0.2^21 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,892 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **69.8** |

`yours 5.0 / Σ 69.8 = 7.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.2% = $0.28/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 75 @ 9¢ → $0.27/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1,083 (75 yours) | ×0.2^0 = 1,083.0 |
|  | 10¢ | 1 | ×0.2^1 = 0.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 16¢ | 3 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **1,083.2** |

`yours 75.0 / Σ 1,083.2 = 6.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.9% = $0.27/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 9¢ → $0.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 162 | ×0.2^0 = 162.0 |
| ▶ | 9¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 15¢ | 15 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^42 = 0.0 |
|  | 99¢ | 5,261 | ×0.2^91 = 0.0 |
| | | **Σ** | **172.1** |

`yours 10.0 / Σ 172.1 = 5.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.8% = $0.24/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 75 @ 8¢ → $0.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1,462 (75 yours) | ×0.2^0 = 1,462.0 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 14¢ | 100 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **1,462.1** |

`yours 75.0 / Σ 1,462.1 = 5.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.1% = $0.20/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-01 | ~$46.23 | $52.30 | 113% |
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |

Biggest gaps on 2026-08-01: `scc-hrep-rep-2026-11-03-gte215` (est ~$2.09 → got $1.51), `scc-senate-gop-2026-11-03-52` (est ~$3.15 → got $2.78), `cranc-uspres28-12-31-2026-tedcru` (est ~$0.71 → got $0.35)

_2026-08-02 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,525 resting) | ~99.3% | ~$24.82 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (322,334 resting) | ~32.9% | ~$24.67 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (7,714 resting) | ~68.8% | ~$17.20 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,294 resting) | ~51.0% | ~$12.74 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,500 resting) | ~28.2% | ~$7.05 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (83,330 resting) | ~7.6% | ~$5.73 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,803 resting) | ~19.1% | ~$4.76 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (237,353 resting) | ~5.9% | ~$4.42 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (123,105 resting) | ~2.3% | ~$1.73 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (190,772 resting) | ~2.1% | ~$1.58 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (107,748 resting) | ~2.1% | ~$1.58 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (104,898 resting) | ~1.3% | ~$0.95 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,514.21 |
| Pending | $14.05 |
| Skipped | $1.21 |
| **Total earned** | **$1,529.47** |

1573 reward rows · 31 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-02 ⚠️ multi-day pending bucket | $14.05 | `█` |
| 2026-08-01 | $52.30 | `█████` |
| 2026-07-31 | $67.96 | `██████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $66.35 | `█` |
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $35.05 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `apdc-alito-2026-12-31` | $23.38 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-04 2:43 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 11:42 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 10:10 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:31 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:24 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:12 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:10 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:07 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 9:02 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:17 PM ET | ✅ ok | 1532 | $1515.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
