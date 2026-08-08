# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-08 1:50 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$112.95/day estimated (ceiling, not promise — details below)

**Earned:** $1,712.09 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-06: **$52.21** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-05: **$31.46** · 2026-08-04: **$53.94** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — BUY at the best price, ~$10.75/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$9.21/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$7.64/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$112.95/day (~$4.71/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-50` | BUY | 25.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~98.9% of bid side (100,606 resting ≥ 5,000 ✓) ≈ $3.81/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~95.2% of ask side (48,664 resting ≥ 5,000 ✓) ≈ $3.97/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 60.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~85.2% of ask side (63,032 resting ≥ 5,000 ✓) ≈ $3.55/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 35.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~79.5% of ask side (48,076 resting ≥ 5,000 ✓) ≈ $3.31/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 49.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~79.3% of bid side (80,746 resting ≥ 5,000 ✓) ≈ $3.30/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~79.2% of bid side (50,423 resting ≥ 5,000 ✓) ≈ $3.05/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 63.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~74.3% of ask side (11,842 resting ≥ 5,000 ✓) ≈ $3.10/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 57.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~71.4% of bid side (80,495 resting ≥ 5,000 ✓) ≈ $2.97/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~71.3% of bid side (200,553 resting ≥ 5,000 ✓) ≈ $2.74/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 91.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~70.4% of ask side (12,173 resting ≥ 5,000 ✓) ≈ $2.93/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~69.2% of bid side (80,595 resting ≥ 5,000 ✓) ≈ $2.88/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (50,637 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 12.0¢ | 39 | 0 | $100.00 | ✅ scoring — ~66.0% of bid side (80,615 resting ≥ 5,000 ✓) ≈ $2.75/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~57.1% of ask side (117,800 resting ≥ 5,000 ✓) ≈ $2.20/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 10.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~55.3% of ask side (113,539 resting ≥ 5,000 ✓) ≈ $2.13/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 5.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~53.1% of ask side (113,731 resting ≥ 5,000 ✓) ≈ $2.04/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 16.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~52.4% of bid side (5,429 resting ≥ 5,000 ✓) ≈ $13.09/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 46.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~50.8% of ask side (48,220 resting ≥ 5,000 ✓) ≈ $2.12/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 26.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~47.1% of ask side (113,523 resting ≥ 5,000 ✓) ≈ $1.81/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 33.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~43.8% of bid side (200,476 resting ≥ 5,000 ✓) ≈ $1.83/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 19.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~43.7% of ask side (99,128 resting ≥ 5,000 ✓) ≈ $1.68/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~40.0% of bid side (50,475 resting ≥ 5,000 ✓) ≈ $1.67/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~40.0% of bid side (50,475 resting ≥ 5,000 ✓) ≈ $1.67/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 5.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~38.1% of bid side (25,414 resting ≥ 5,000 ✓) ≈ $1.47/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 11.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~36.9% of ask side (113,529 resting ≥ 5,000 ✓) ≈ $1.42/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 28.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~33.3% of ask side (113,519 resting ≥ 5,000 ✓) ≈ $1.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 28.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~33.3% of ask side (113,519 resting ≥ 5,000 ✓) ≈ $1.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 29.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~33.3% of ask side (113,519 resting ≥ 5,000 ✓) ≈ $1.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 29.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~33.3% of bid side (50,637 resting ≥ 5,000 ✓) ≈ $1.28/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 12.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~29.9% of bid side (35,756 resting ≥ 2,000 ✓) ≈ $3.74/day |
| …and 71 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 1 @ 25¢ → $3.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 23¢ | 0 | ×0.2^2 = 0.0 |
|  | 22¢ | 0 | ×0.2^3 = 0.0 |
|  | 16¢ | 380 | ×0.2^9 = 0.0 |
|  | 2¢ | 100,000 | ×0.2^23 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.9% = $3.81/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 20 @ 48¢ → $3.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 51¢ | 1 | ×0.2^3 = 0.0 |
|  | 59¢ | 5 | ×0.2^11 = 0.0 |
|  | 60¢ | 100 | ×0.2^12 = 0.0 |
|  | 83¢ | 812 | ×0.2^35 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **21.0** |

`yours 20.0 / Σ 21.0 = 95.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 95.2% = $3.97/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 10 @ 60¢ → $3.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 62¢ | 42 | ×0.2^2 = 1.7 |
|  | 63¢ | 5 | ×0.2^3 = 0.0 |
|  | 65¢ | 50 | ×0.2^5 = 0.0 |
|  | 71¢ | 200 | ×0.2^11 = 0.0 |
|  | 90¢ | 1 | ×0.2^30 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^38 = 0.0 |
| | | **Σ** | **11.7** |

`yours 10.0 / Σ 11.7 = 85.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 85.2% = $3.55/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 35¢ → $3.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 12 (10 yours) | ×0.2^0 = 12.0 |
|  | 37¢ | 1 | ×0.2^2 = 0.0 |
|  | 39¢ | 339 | ×0.2^4 = 0.5 |
|  | 59¢ | 0 | ×0.2^24 = 0.0 |
|  | 64¢ | 0 | ×0.2^29 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^63 = 0.0 |
| | | **Σ** | **12.6** |

`yours 10.0 / Σ 12.6 = 79.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 79.5% = $3.31/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 20 @ 49¢ → $3.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 25 (20 yours) | ×0.2^0 = 25.2 |
|  | 36¢ | 100 | ×0.2^13 = 0.0 |
|  | 35¢ | 80 | ×0.2^14 = 0.0 |
|  | 11¢ | 151 | ×0.2^38 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^47 = 0.0 |
| | | **Σ** | **25.2** |

`yours 20.0 / Σ 25.2 = 79.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 79.3% = $3.30/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 18¢ → $3.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **12.6** |

`yours 10.0 / Σ 12.6 = 79.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 79.2% = $3.05/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 10 @ 63¢ → $3.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 63¢ | 13 (10 yours) | ×0.2^0 = 13.5 |
|  | 72¢ | 30 | ×0.2^9 = 0.0 |
|  | 84¢ | 135 | ×0.2^21 = 0.0 |
|  | 94¢ | 1 | ×0.2^31 = 0.0 |
|  | 99¢ | 11,663 | ×0.2^36 = 0.0 |
| | | **Σ** | **13.5** |

`yours 10.0 / Σ 13.5 = 74.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 74.3% = $3.10/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 57¢ → $2.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 14 (10 yours) | ×0.2^0 = 14.0 |
|  | 51¢ | 20 | ×0.2^6 = 0.0 |
|  | 48¢ | 11 | ×0.2^9 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^55 = 0.0 |
| | | **Σ** | **14.0** |

`yours 10.0 / Σ 14.0 = 71.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 71.4% = $2.97/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5 @ 19¢ → $2.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 7 (5 yours) | ×0.2^0 = 7.0 |
|  | 5¢ | 115 | ×0.2^14 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^18 = 0.0 |
| | | **Σ** | **7.0** |

`yours 5.0 / Σ 7.0 = 71.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 71.3% = $2.74/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 20 @ 91¢ → $2.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 28 (20 yours) | ×0.2^0 = 28.0 |
|  | 94¢ | 48 | ×0.2^3 = 0.4 |
|  | 99¢ | 12,097 | ×0.2^8 = 0.0 |
| | | **Σ** | **28.4** |

`yours 20.0 / Σ 28.4 = 70.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 70.4% = $2.93/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 75¢ → $2.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 44 (31 yours) | ×0.2^0 = 44.0 |
|  | 72¢ | 101 | ×0.2^3 = 0.8 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
| | | **Σ** | **44.8** |

`yours 31.0 / Σ 44.8 = 69.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 69.2% = $2.88/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 29¢ → $2.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 22¢ | 30 | ×0.2^7 = 0.0 |
|  | 21¢ | 17 | ×0.2^8 = 0.0 |
|  | 20¢ | 10 | ×0.2^9 = 0.0 |
|  | 19¢ | 0 | ×0.2^10 = 0.0 |
|  | 16¢ | 156 | ×0.2^13 = 0.0 |
|  | 2¢ | 50,209 | ×0.2^27 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 39 @ 12¢ → $2.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 59 (39 yours) | ×0.2^0 = 58.9 |
|  | 1¢ | 80,557 | ×0.2^11 = 0.0 |
| | | **Σ** | **58.9** |

`yours 38.9 / Σ 58.9 = 66.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.0% = $2.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $2.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 35 (20 yours) | ×0.2^0 = 35.0 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **35.0** |

`yours 20.0 / Σ 35.0 = 57.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 57.1% = $2.20/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 5 @ 10¢ → $2.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 9 (5 yours) | ×0.2^0 = 9.0 |
|  | 13¢ | 1 | ×0.2^3 = 0.0 |
|  | 22¢ | 27 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 88¢ | 0 | ×0.2^78 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^87 = 0.0 |
| | | **Σ** | **9.0** |

`yours 5.0 / Σ 9.0 = 55.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.3% = $2.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 5 @ 5¢ → $2.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 9 (5 yours) | ×0.2^0 = 9.0 |
|  | 8¢ | 10 | ×0.2^3 = 0.1 |
|  | 9¢ | 209 | ×0.2^4 = 0.3 |
|  | 10¢ | 1 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^92 = 0.0 |
| | | **Σ** | **9.4** |

`yours 5.0 / Σ 9.4 = 53.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.1% = $2.04/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 21 @ 16¢ → $13.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 25 (21 yours) | ×0.2^0 = 24.9 |
|  | 14¢ | 100 | ×0.2^2 = 4.0 |
|  | 13¢ | 1,372 | ×0.2^3 = 11.0 |
|  | 1¢ | 3,933 | ×0.2^15 = 0.0 |
| | | **Σ** | **39.8** |

`yours 20.9 / Σ 39.8 = 52.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 52.4% = $13.09/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 10 @ 46¢ → $2.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 12 (10 yours) | ×0.2^0 = 12.0 |
|  | 47¢ | 20 | ×0.2^1 = 4.0 |
|  | 49¢ | 462 | ×0.2^3 = 3.7 |
|  | 52¢ | 1 | ×0.2^6 = 0.0 |
|  | 55¢ | 0 | ×0.2^9 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^52 = 0.0 |
| | | **Σ** | **19.7** |

`yours 10.0 / Σ 19.7 = 50.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 50.8% = $2.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 5 @ 26¢ → $1.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 11 (5 yours) | ×0.2^0 = 10.6 |
|  | 31¢ | 10 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^24 = 0.0 |
|  | 59¢ | 0 | ×0.2^33 = 0.0 |
|  | 67¢ | 0 | ×0.2^41 = 0.0 |
|  | 68¢ | 0 | ×0.2^42 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^71 = 0.0 |
| | | **Σ** | **10.6** |

`yours 5.0 / Σ 10.6 = 47.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.1% = $1.81/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 10 @ 33¢ → $1.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 22 (10 yours) | ×0.2^0 = 22.0 |
|  | 32¢ | 4 | ×0.2^1 = 0.8 |
|  | 1¢ | 200,450 | ×0.2^32 = 0.0 |
| | | **Σ** | **22.8** |

`yours 10.0 / Σ 22.8 = 43.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 43.8% = $1.83/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 5 @ 19¢ → $1.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 10 (5 yours) | ×0.2^0 = 10.0 |
|  | 21¢ | 2 | ×0.2^2 = 0.1 |
|  | 22¢ | 46 | ×0.2^3 = 0.4 |
|  | 23¢ | 629 | ×0.2^4 = 1.0 |
|  | 26¢ | 0 | ×0.2^7 = 0.0 |
|  | 38¢ | 0 | ×0.2^19 = 0.0 |
|  | 50¢ | 39 | ×0.2^31 = 0.0 |
|  | 60¢ | 0 | ×0.2^41 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^78 = 0.0 |
| | | **Σ** | **11.5** |

`yours 5.0 / Σ 11.5 = 43.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.7% = $1.68/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 82¢ → $1.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 25 (10 yours) | ×0.2^0 = 25.0 |
|  | 72¢ | 0 | ×0.2^10 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^80 = 0.0 |
| | | **Σ** | **25.0** |

`yours 10.0 / Σ 25.0 = 40.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 40.0% = $1.67/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 82¢ → $1.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 25 (10 yours) | ×0.2^0 = 25.0 |
|  | 72¢ | 0 | ×0.2^10 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^80 = 0.0 |
| | | **Σ** | **25.0** |

`yours 10.0 / Σ 25.0 = 40.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 40.0% = $1.67/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 25 @ 5¢ → $1.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 1¢ | 25,389 | ×0.2^4 = 40.6 |
| | | **Σ** | **65.6** |

`yours 25.0 / Σ 65.6 = 38.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.1% = $1.47/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 5 @ 11¢ → $1.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 12 (5 yours) | ×0.2^0 = 11.5 |
|  | 12¢ | 10 | ×0.2^1 = 2.0 |
|  | 14¢ | 1 | ×0.2^3 = 0.0 |
|  | 15¢ | 5 | ×0.2^4 = 0.0 |
|  | 50¢ | 100 | ×0.2^39 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^86 = 0.0 |
| | | **Σ** | **13.6** |

`yours 5.0 / Σ 13.6 = 36.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 36.9% = $1.42/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 2 @ 28¢ → $1.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 4 (2 yours) | ×0.2^0 = 4.0 |
|  | 29¢ | 10 | ×0.2^1 = 2.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 73¢ | 0 | ×0.2^45 = 0.0 |
|  | 74¢ | 0 | ×0.2^46 = 0.0 |
|  | 75¢ | 0 | ×0.2^47 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^69 = 0.0 |
| | | **Σ** | **6.0** |

`yours 2.0 / Σ 6.0 = 33.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.3% = $1.28/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 2 @ 28¢ → $1.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 4 (2 yours) | ×0.2^0 = 4.0 |
|  | 29¢ | 10 | ×0.2^1 = 2.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 73¢ | 0 | ×0.2^45 = 0.0 |
|  | 74¢ | 0 | ×0.2^46 = 0.0 |
|  | 75¢ | 0 | ×0.2^47 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^69 = 0.0 |
| | | **Σ** | **6.0** |

`yours 2.0 / Σ 6.0 = 33.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.3% = $1.28/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 10 @ 29¢ → $1.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 28¢ | 4 | ×0.2^0 = 4.0 |
| ▶ | 29¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 73¢ | 0 | ×0.2^45 = 0.0 |
|  | 74¢ | 0 | ×0.2^46 = 0.0 |
|  | 75¢ | 0 | ×0.2^47 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^69 = 0.0 |
| | | **Σ** | **6.0** |

`yours 2.0 / Σ 6.0 = 33.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.3% = $1.28/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5 @ 29¢ → $1.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 15 (5 yours) | ×0.2^0 = 15.0 |
|  | 22¢ | 30 | ×0.2^7 = 0.0 |
|  | 21¢ | 17 | ×0.2^8 = 0.0 |
|  | 20¢ | 10 | ×0.2^9 = 0.0 |
|  | 19¢ | 0 | ×0.2^10 = 0.0 |
|  | 16¢ | 156 | ×0.2^13 = 0.0 |
|  | 2¢ | 50,209 | ×0.2^27 = 0.0 |
| | | **Σ** | **15.0** |

`yours 5.0 / Σ 15.0 = 33.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.3% = $1.28/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 100 @ 12¢ → $3.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 334 (100 yours) | ×0.1^0 = 334.0 |
|  | 10¢ | 0 | ×0.1^2 = 0.0 |
|  | 5¢ | 99 | ×0.1^7 = 0.0 |
|  | 4¢ | 22 | ×0.1^8 = 0.0 |
|  | 3¢ | 100 | ×0.1^9 = 0.0 |
|  | 1¢ | 35,200 | ×0.1^11 = 0.0 |
| | | **Σ** | **334.0** |

`yours 100.0 / Σ 334.0 = 29.9%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 29.9% = $3.74/day`  

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-05 | ~$33.74 | $31.46 | 93% |
| 2026-08-04 | ~$67.52 | $53.94 | 80% |
| 2026-08-03 | ~$65.16 | $44.81 | 69% |

Biggest gaps on 2026-08-05: `opdc-mcconnell-resign-2026-11-02` (est ~$1.91 → got $0.30), `scc-senate-gop-2026-11-03-51` (est ~$2.87 → got $2.08), `ewc-usgub-ca-2026-11-03-stehil` (est ~$0.75 → got $0.00)

_2026-08-06 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (151,628 resting) | ~14.3% | ~$10.75 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,749 resting) | ~36.8% | ~$9.21 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (78,303 resting) | ~30.6% | ~$7.64 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (613,291 resting) | ~7.5% | ~$5.63 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (66,969 resting) | ~6.7% | ~$4.99 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (322,671 resting) | ~4.0% | ~$3.02 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (190,173 resting) | ~3.6% | ~$2.69 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (87,994 resting) | ~3.4% | ~$2.51 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (281,571 resting) | ~2.4% | ~$1.78 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (52,865 resting) | ~6.8% | ~$1.69 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (68,004 resting) | ~2.2% | ~$1.64 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (183,809 resting) | ~1.5% | ~$1.15 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,627.01 |
| Pending | $83.67 |
| Skipped | $1.41 |
| **Total earned** | **$1,712.09** |

1702 reward rows · 35 days with rewards · 363 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-06 ⚠️ multi-day pending bucket | $52.21 | `███████` |
| 2026-08-05 | $31.46 | `████` |
| 2026-08-04 | $53.94 | `███████` |
| 2026-08-03 | $44.81 | `██████` |
| 2026-08-02 | $14.05 | `██` |
| 2026-08-01 | $52.30 | `███████` |
| 2026-07-31 | $67.96 | `█████████` |
| 2026-07-30 | $20.67 | `███` |
| 2026-07-29 | $53.60 | `███████` |
| 2026-07-28 | $79.65 | `██████████` |
| 2026-07-27 | $125.34 | `████████████████` |
| 2026-07-26 | $153.80 | `████████████████████` |
| 2026-07-25 | $125.69 | `████████████████` |
| 2026-07-24 | $135.19 | `██████████████████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $248.77 | `███` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $74.36 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `opdc-mcconnell-resign-2026-11-02` | $47.82 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `apdc-jerpowgov-2026-12-31` | $42.68 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.92 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.02 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `scc-hrep-rep-2026-11-03-gte200` | $25.65 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-08 1:50 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 12:56 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 11:49 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 10:52 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 10:01 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 9:15 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 7:47 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 6:54 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 5:57 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 5:04 AM ET | ✅ ok | 1702 | $1712.09 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
