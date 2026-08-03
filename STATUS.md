# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-03 6:29 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$43.40/day estimated (ceiling, not promise — details below)

**Earned:** $1,515.42 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-01: **$52.30** · 2026-07-31: **$67.96** · 2026-07-30: **$20.48** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-xavbec` — SELL at the best price, ~$21.35/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$9.59/day), `ewc-usgub-ca-2026-11-03-stehil` (~$8.17/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$43.40/day (~$1.81/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-49` | BUY | 24.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~91.8% of bid side (5,558 resting ≥ 5,000 ✓) ≈ $3.53/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~76.7% of ask side (12,050 resting ≥ 5,000 ✓) ≈ $2.95/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 14.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~66.3% of bid side (11,000 resting ≥ 5,000 ✓) ≈ $2.55/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~64.4% of ask side (12,354 resting ≥ 5,000 ✓) ≈ $2.48/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~38.4% of ask side (13,802 resting ≥ 5,000 ✓) ≈ $1.60/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | BUY | 17.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~35.7% of bid side (11,100 resting ≥ 5,000 ✓) ≈ $8.92/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 41 | 0 | $100.00 | ✅ scoring — ~34.5% of ask side (12,207 resting ≥ 5,000 ✓) ≈ $1.33/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 57.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~31.8% of ask side (6,078 resting ≥ 5,000 ✓) ≈ $1.32/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 7.0¢ | 3 | 1 | $100.00 | ✅ scoring — ~29.2% of bid side (25,570 resting ≥ 5,000 ✓) ≈ $1.12/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~28.2% of ask side (12,289 resting ≥ 5,000 ✓) ≈ $1.08/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 45.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~27.9% of ask side (11,711 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 27.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~26.3% of ask side (12,245 resting ≥ 5,000 ✓) ≈ $1.01/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 25.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~26.0% of ask side (17,998 resting ≥ 5,000 ✓) ≈ $6.50/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~19.1% of bid side (26,126 resting ≥ 5,000 ✓) ≈ $0.74/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 26.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~17.7% of bid side (11,001 resting ≥ 5,000 ✓) ≈ $0.68/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~16.8% of ask side (12,225 resting ≥ 5,000 ✓) ≈ $0.64/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~12.8% of bid side (11,000 resting ≥ 5,000 ✓) ≈ $0.53/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 1 | $100.00 | ✅ scoring — ~12.5% of bid side (11,344 resting ≥ 5,000 ✓) ≈ $0.48/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 3.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~11.5% of bid side (8,879 resting ≥ 5,000 ✓) ≈ $0.44/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-ind` | SELL | 2.0¢ | 32 | 0 | $500.00 | ✅ scoring — ~9.3% of ask side (153,790 resting ≥ 2,500 ✓) ≈ $0.32/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~8.3% of bid side (60,076 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~8.2% of bid side (12,364 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 5.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~7.9% of bid side (25,948 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~6.9% of ask side (6,619 resting ≥ 5,000 ✓) ≈ $0.29/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 5.0¢ | 590 | 0 | $100.00 | ✅ scoring — ~6.4% of bid side (9,444 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 57.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~6.4% of ask side (6,078 resting ≥ 5,000 ✓) ≈ $0.26/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~6.0% of bid side (8,494 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~4.8% of bid side (19,188 resting ≥ 2,500 ✓) ≈ $0.16/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 9.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~4.7% of ask side (15,598 resting ≥ 5,000 ✓) ≈ $0.20/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 7 | $100.00 | ✅ scoring — ~3.2% of bid side (25,570 resting ≥ 5,000 ✓) ≈ $0.12/day (pool ÷ 13 markets) |
| …and 41 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 24¢ → $3.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 2 | ×0.2^3 = 0.0 |
|  | 20¢ | 46 | ×0.2^4 = 0.1 |
|  | 1¢ | 5,509 | ×0.2^23 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 91.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 91.8% = $3.53/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 15 @ 14¢ → $2.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 22 (15 yours) | ×0.2^0 = 22.0 |
|  | 13¢ | 1 | ×0.2^1 = 0.2 |
|  | 12¢ | 10 | ×0.2^2 = 0.4 |
|  | 6¢ | 32 | ×0.2^8 = 0.0 |
|  | 1¢ | 10,935 | ×0.2^13 = 0.0 |
| | | **Σ** | **22.6** |

`yours 15.0 / Σ 22.6 = 66.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.3% = $2.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $2.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 62 (40 yours) | ×0.2^0 = 62.0 |
|  | 12¢ | 2 | ×0.2^2 = 0.1 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **62.1** |

`yours 40.0 / Σ 62.1 = 64.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.4% = $2.48/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 30 @ 47¢ → $1.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 78 (30 yours) | ×0.2^0 = 78.0 |
|  | 49¢ | 5 | ×0.2^2 = 0.2 |
|  | 52¢ | 1 | ×0.2^5 = 0.0 |
|  | 69¢ | 100 | ×0.2^22 = 0.0 |
|  | 99¢ | 13,618 | ×0.2^52 = 0.0 |
| | | **Σ** | **78.2** |

`yours 30.0 / Σ 78.2 = 38.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 38.4% = $1.60/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 100 @ 17¢ → $8.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 100 (100 yours) | ×0.2^0 = 100.0 |
|  | 16¢ | 100 | ×0.2^1 = 20.0 |
|  | 15¢ | 4,003 | ×0.2^2 = 160.1 |
|  | 11¢ | 1,215 | ×0.2^6 = 0.1 |
| | | **Σ** | **280.2** |

`yours 100.0 / Σ 280.2 = 35.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 35.7% = $8.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 41 @ 22¢ → $1.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 119 (41 yours) | ×0.2^0 = 119.2 |
|  | 24¢ | 3 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 98¢ | 1,784 | ×0.2^76 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^77 = 0.0 |
| | | **Σ** | **119.3** |

`yours 41.2 / Σ 119.3 = 34.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.5% = $1.33/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 15 @ 57¢ → $1.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 47 (15 yours) | ×0.2^0 = 47.0 |
|  | 59¢ | 5 | ×0.2^2 = 0.2 |
|  | 67¢ | 50 | ×0.2^10 = 0.0 |
|  | 77¢ | 1 | ×0.2^20 = 0.0 |
|  | 83¢ | 164 | ×0.2^26 = 0.0 |
|  | 90¢ | 1 | ×0.2^33 = 0.0 |
|  | 99¢ | 5,809 | ×0.2^42 = 0.0 |
| | | **Σ** | **47.2** |

`yours 15.0 / Σ 47.2 = 31.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 31.8% = $1.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 3 @ 7¢ → $1.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 1 | ×0.2^0 = 1.1 |
| ▶ | 7¢ | 3 (3 yours) | ×0.2^1 = 0.6 |
|  | 2¢ | 232 | ×0.2^6 = 0.0 |
|  | 1¢ | 25,334 | ×0.2^7 = 0.3 |
| | | **Σ** | **2.0** |

`yours 0.6 / Σ 2.0 = 29.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.2% = $1.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 123 (40 yours) | ×0.2^0 = 123.0 |
|  | 7¢ | 94 | ×0.2^1 = 18.8 |
|  | 8¢ | 2 | ×0.2^2 = 0.1 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **141.9** |

`yours 40.0 / Σ 141.9 = 28.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.2% = $1.08/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 50 @ 45¢ → $1.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 179 (50 yours) | ×0.2^0 = 179.0 |
|  | 47¢ | 2 | ×0.2^2 = 0.1 |
|  | 49¢ | 229 | ×0.2^4 = 0.4 |
|  | 50¢ | 100 | ×0.2^5 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^53 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^54 = 0.0 |
| | | **Σ** | **179.5** |

`yours 50.0 / Σ 179.5 = 27.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.9% = $1.07/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 27¢ → $1.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 19 (5 yours) | ×0.2^0 = 18.9 |
|  | 29¢ | 2 | ×0.2^2 = 0.1 |
|  | 43¢ | 100 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^23 = 0.0 |
|  | 98¢ | 1,823 | ×0.2^71 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^72 = 0.0 |
| | | **Σ** | **19.0** |

`yours 5.0 / Σ 19.0 = 26.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.3% = $1.01/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 25¢ → $6.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 173 (100 yours) | ×0.2^0 = 173.0 |
|  | 27¢ | 5,286 | ×0.2^2 = 211.4 |
| | | **Σ** | **384.4** |

`yours 100.0 / Σ 384.4 = 26.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 26.0% = $6.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 5,000 @ 1¢ → $0.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 26,126 (5,000 yours) | ×0.2^0 = 26,126.0 |
| | | **Σ** | **26,126.0** |

`yours 5,000.0 / Σ 26,126.0 = 19.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.1% = $0.74/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 15 @ 26¢ → $0.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 84 (15 yours) | ×0.2^0 = 84.4 |
|  | 24¢ | 4 | ×0.2^2 = 0.2 |
|  | 20¢ | 30 | ×0.2^6 = 0.0 |
|  | 14¢ | 72 | ×0.2^12 = 0.0 |
|  | 7¢ | 190 | ×0.2^19 = 0.0 |
|  | 1¢ | 10,620 | ×0.2^25 = 0.0 |
| | | **Σ** | **84.6** |

`yours 15.0 / Σ 84.6 = 17.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.7% = $0.68/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 8¢ → $0.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 103 (20 yours) | ×0.2^0 = 103.1 |
|  | 9¢ | 81 | ×0.2^1 = 16.2 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,739 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **119.4** |

`yours 20.0 / Σ 119.4 = 16.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.8% = $0.64/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 82¢ → $0.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 78 (10 yours) | ×0.2^0 = 78.2 |
|  | 80¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 10,921 | ×0.2^81 = 0.0 |
| | | **Σ** | **78.2** |

`yours 10.0 / Σ 78.2 = 12.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 12.8% = $0.53/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $0.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 621 | ×0.2^0 = 621.0 |
| ▶ | 4¢ | 500 (500 yours) | ×0.2^1 = 100.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 9,990 | ×0.2^3 = 79.9 |
| | | **Σ** | **802.3** |

`yours 100.0 / Σ 802.3 = 12.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 12.5% = $0.48/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-ind</code> SELL 32 @ 2¢ → $0.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 63 (32 yours) | ×0.35^0 = 63.0 |
|  | 4¢ | 14 | ×0.35^2 = 1.7 |
|  | 7¢ | 46 | ×0.35^5 = 0.2 |
|  | 8¢ | 151,584 | ×0.35^6 = 278.7 |
| | | **Σ** | **343.6** |

`yours 32.0 / Σ 343.6 = 9.3%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 9.3% = $0.32/day`  

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
22. `tec-cbb-champ-2027-04-05-w-ind` ← this one
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
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5,000 @ 1¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 60,076 (5,000 yours) | ×0.2^0 = 60,075.5 |
| | | **Σ** | **60,075.5** |

`yours 5,000.0 / Σ 60,075.5 = 8.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.3% = $0.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 12,164 (1,000 yours) | ×0.2^0 = 12,164.0 |
| | | **Σ** | **12,164.0** |

`yours 1,000.0 / Σ 12,164.0 = 8.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.2% = $0.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 50 @ 5¢ → $0.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 591 (50 yours) | ×0.2^0 = 591.0 |
|  | 3¢ | 87 | ×0.2^2 = 3.5 |
|  | 1¢ | 25,270 | ×0.2^4 = 40.4 |
| | | **Σ** | **634.9** |

`yours 50.0 / Σ 634.9 = 7.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.9% = $0.30/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 15 @ 7¢ → $0.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 218 (15 yours) | ×0.2^0 = 218.0 |
|  | 9¢ | 2 | ×0.2^2 = 0.1 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 99¢ | 6,373 | ×0.2^92 = 0.0 |
| | | **Σ** | **218.1** |

`yours 15.0 / Σ 218.1 = 6.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 6.9% = $0.29/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 590 @ 5¢ → $0.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 9,244 (590 yours) | ×0.2^0 = 9,244.0 |
| | | **Σ** | **9,244.0** |

`yours 590.0 / Σ 9,244.0 = 6.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.4% = $0.25/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 3 @ 57¢ → $0.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 47 (3 yours) | ×0.2^0 = 47.0 |
|  | 59¢ | 5 | ×0.2^2 = 0.2 |
|  | 67¢ | 50 | ×0.2^10 = 0.0 |
|  | 77¢ | 1 | ×0.2^20 = 0.0 |
|  | 83¢ | 164 | ×0.2^26 = 0.0 |
|  | 90¢ | 1 | ×0.2^33 = 0.0 |
|  | 99¢ | 5,809 | ×0.2^42 = 0.0 |
| | | **Σ** | **47.2** |

`yours 3.0 / Σ 47.2 = 6.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 6.4% = $0.26/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 980 | ×0.35^0 = 980.0 |
| ▶ | 1¢ | 18,208 (1,000 yours) | ×0.35^1 = 6,372.8 |
| | | **Σ** | **7,352.8** |

`yours 350.0 / Σ 7,352.8 = 4.8%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 4.8% = $0.16/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 9¢ → $0.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 195 | ×0.2^0 = 195.0 |
| ▶ | 9¢ | 84 (50 yours) | ×0.2^1 = 16.8 |
|  | 10¢ | 5 | ×0.2^2 = 0.2 |
|  | 15¢ | 15 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^42 = 0.0 |
|  | 99¢ | 15,274 | ×0.2^91 = 0.0 |
| | | **Σ** | **212.0** |

`yours 10.0 / Σ 212.0 = 4.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.7% = $0.20/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 1 | ×0.2^0 = 1.1 |
|  | 7¢ | 3 | ×0.2^1 = 0.6 |
|  | 2¢ | 232 | ×0.2^6 = 0.0 |
| ▶ | 1¢ | 25,334 (5,000 yours) | ×0.2^7 = 0.3 |
| | | **Σ** | **2.0** |

`yours 0.1 / Σ 2.0 = 3.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.2% = $0.12/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-01 | ~$46.23 | $52.30 | 113% |
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |

Biggest gaps on 2026-08-01: `scc-hrep-rep-2026-11-03-gte215` (est ~$2.09 → got $1.51), `scc-senate-gop-2026-11-03-52` (est ~$3.15 → got $2.78), `cranc-uspres28-12-31-2026-tedcru` (est ~$0.71 → got $0.35)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,934 resting) | ~28.5% | ~$21.35 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (78,520 resting) | ~12.8% | ~$9.59 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (91,982 resting) | ~10.9% | ~$8.17 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (188,101 resting) | ~4.2% | ~$3.12 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (83,727 resting) | ~2.8% | ~$2.10 |
| `ewc-usse-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (89,169 resting) | ~33.3% | ~$2.08 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (202,154 resting) | ~2.7% | ~$2.06 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (122,362 resting) | ~2.4% | ~$1.82 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (66,314 resting) | ~23.5% | ~$1.47 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (133,451 resting) | ~1.9% | ~$1.46 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (109,018 resting) | ~1.3% | ~$0.94 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (79,390 resting) | ~14.9% | ~$0.93 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,514.21 |
| Skipped | $1.21 |
| **Total earned** | **$1,515.42** |

1532 reward rows · 30 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
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
| 2026-07-19 | $35.81 | `███` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $52.30 | `█` |
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.60 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.96 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-03 6:29 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 4:40 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 3:00 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 1:22 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 11:20 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:30 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:15 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:13 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 7:48 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 3:51 AM ET | ✅ ok | 1532 | $1515.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
