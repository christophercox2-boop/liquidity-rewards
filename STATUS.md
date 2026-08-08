# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-08 12:56 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$114.73/day estimated (ceiling, not promise — details below)

**Earned:** $1,712.09 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-06: **$52.21** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-05: **$31.46** · 2026-08-04: **$53.94** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$9.15/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$8.06/day), `paccc-usho-midterms-2026-11-03-rep` (~$5.62/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$114.73/day (~$4.78/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 12.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (80,377 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 26.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~98.9% of ask side (113,608 resting ≥ 5,000 ✓) ≈ $3.81/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 25.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~98.9% of bid side (100,606 resting ≥ 5,000 ✓) ≈ $3.81/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 43.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~98.5% of bid side (80,469 resting ≥ 5,000 ✓) ≈ $4.11/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~97.5% of bid side (80,331 resting ≥ 5,000 ✓) ≈ $4.06/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~95.2% of ask side (48,664 resting ≥ 5,000 ✓) ≈ $3.97/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 35.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~92.7% of ask side (48,183 resting ≥ 5,000 ✓) ≈ $3.86/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 40.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~90.6% of ask side (49,603 resting ≥ 5,000 ✓) ≈ $3.77/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 10.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~82.8% of ask side (113,636 resting ≥ 5,000 ✓) ≈ $3.18/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 5.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~77.5% of ask side (113,733 resting ≥ 5,000 ✓) ≈ $2.98/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~70.8% of bid side (200,559 resting ≥ 5,000 ✓) ≈ $2.72/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 36.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~68.5% of bid side (80,750 resting ≥ 5,000 ✓) ≈ $2.85/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (50,465 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 62.0¢ | 42 | 0 | $100.00 | ✅ scoring — ~66.5% of ask side (48,516 resting ≥ 5,000 ✓) ≈ $2.77/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 63.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~59.9% of ask side (15,375 resting ≥ 5,000 ✓) ≈ $2.50/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~57.1% of ask side (117,800 resting ≥ 5,000 ✓) ≈ $2.20/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~52.6% of bid side (50,593 resting ≥ 5,000 ✓) ≈ $2.02/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 16.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~52.4% of bid side (5,429 resting ≥ 5,000 ✓) ≈ $13.09/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 33.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~49.3% of bid side (200,553 resting ≥ 5,000 ✓) ≈ $2.06/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~48.5% of bid side (50,439 resting ≥ 5,000 ✓) ≈ $1.86/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 19.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~47.8% of ask side (99,127 resting ≥ 5,000 ✓) ≈ $1.84/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~41.2% of ask side (48,210 resting ≥ 5,000 ✓) ≈ $1.72/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 11.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~36.9% of ask side (113,533 resting ≥ 5,000 ✓) ≈ $1.42/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 31.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~33.9% of ask side (98,670 resting ≥ 5,000 ✓) ≈ $1.30/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 12.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~29.9% of bid side (35,664 resting ≥ 2,000 ✓) ≈ $3.74/day |
| `apdc-jerpowgov-2026-12-31` | BUY | 24.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~28.8% of bid side (5,544 resting ≥ 5,000 ✓) ≈ $7.21/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 19.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~28.7% of ask side (99,127 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~28.3% of bid side (200,559 resting ≥ 5,000 ✓) ≈ $1.09/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 29.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~26.3% of bid side (50,593 resting ≥ 5,000 ✓) ≈ $1.01/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~24.2% of bid side (50,439 resting ≥ 5,000 ✓) ≈ $0.93/day (pool ÷ 13 markets) |
| …and 64 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 40 @ 12¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 2¢ | 30 | ×0.2^10 = 0.0 |
|  | 1¢ | 80,307 | ×0.2^11 = 0.0 |
| | | **Σ** | **40.0** |

`yours 40.0 / Σ 40.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 5 @ 26¢ → $3.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 31¢ | 10 | ×0.2^5 = 0.0 |
|  | 36¢ | 85 | ×0.2^10 = 0.0 |
|  | 37¢ | 6 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^24 = 0.0 |
|  | 59¢ | 0 | ×0.2^33 = 0.0 |
|  | 67¢ | 0 | ×0.2^41 = 0.0 |
|  | 68¢ | 0 | ×0.2^42 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^71 = 0.0 |
| | | **Σ** | **5.1** |

`yours 5.0 / Σ 5.1 = 98.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.9% = $3.81/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 1 @ 43¢ → $4.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 38¢ | 15 | ×0.2^5 = 0.0 |
|  | 32¢ | 3 | ×0.2^11 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^41 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 98.5% = $4.11/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 75¢ → $4.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 31 (31 yours) | ×0.2^0 = 31.0 |
|  | 72¢ | 100 | ×0.2^3 = 0.8 |
|  | 2¢ | 80,000 | ×0.2^73 = 0.0 |
| | | **Σ** | **31.8** |

`yours 31.0 / Σ 31.8 = 97.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 97.5% = $4.06/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 35¢ → $3.86/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 38¢ | 10 | ×0.2^3 = 0.1 |
|  | 39¢ | 439 | ×0.2^4 = 0.7 |
|  | 59¢ | 0 | ×0.2^24 = 0.0 |
|  | 64¢ | 0 | ×0.2^29 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^63 = 0.0 |
| | | **Σ** | **10.8** |

`yours 10.0 / Σ 10.8 = 92.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 92.7% = $3.86/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 10 @ 40¢ → $3.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 11 (10 yours) | ×0.2^0 = 11.0 |
|  | 43¢ | 5 | ×0.2^3 = 0.0 |
|  | 49¢ | 100 | ×0.2^9 = 0.0 |
|  | 50¢ | 25 | ×0.2^10 = 0.0 |
|  | 66¢ | 0 | ×0.2^26 = 0.0 |
|  | 71¢ | 0 | ×0.2^31 = 0.0 |
|  | 97¢ | 1,738 | ×0.2^57 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^58 = 0.0 |
| | | **Σ** | **11.0** |

`yours 10.0 / Σ 11.0 = 90.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 90.6% = $3.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 5 @ 10¢ → $3.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 6 (5 yours) | ×0.2^0 = 6.0 |
|  | 13¢ | 1 | ×0.2^3 = 0.0 |
|  | 22¢ | 27 | ×0.2^12 = 0.0 |
|  | 26¢ | 100 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 88¢ | 0 | ×0.2^78 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^87 = 0.0 |
| | | **Σ** | **6.0** |

`yours 5.0 / Σ 6.0 = 82.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 82.8% = $3.18/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 5 @ 5¢ → $2.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 6 (5 yours) | ×0.2^0 = 6.0 |
|  | 8¢ | 15 | ×0.2^3 = 0.1 |
|  | 9¢ | 209 | ×0.2^4 = 0.3 |
|  | 10¢ | 1 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^92 = 0.0 |
| | | **Σ** | **6.5** |

`yours 5.0 / Σ 6.5 = 77.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 77.5% = $2.98/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5 @ 19¢ → $2.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 7 (5 yours) | ×0.2^0 = 7.0 |
|  | 16¢ | 6 | ×0.2^3 = 0.0 |
|  | 5¢ | 115 | ×0.2^14 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^18 = 0.0 |
| | | **Σ** | **7.1** |

`yours 5.0 / Σ 7.1 = 70.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 70.8% = $2.72/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 100 @ 36¢ → $2.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 36¢ | 130 (100 yours) | ×0.2^0 = 130.0 |
|  | 35¢ | 80 | ×0.2^1 = 16.0 |
|  | 10¢ | 150 | ×0.2^26 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^34 = 0.0 |
| | | **Σ** | **146.0** |

`yours 100.0 / Σ 146.0 = 68.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 68.5% = $2.85/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 82¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 72¢ | 0 | ×0.2^10 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^80 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 42 @ 62¢ → $2.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 62¢ | 42 (42 yours) | ×0.2^0 = 42.0 |
|  | 63¢ | 5 | ×0.2^1 = 1.0 |
|  | 64¢ | 494 | ×0.2^2 = 19.8 |
|  | 65¢ | 50 | ×0.2^3 = 0.4 |
|  | 71¢ | 200 | ×0.2^9 = 0.0 |
|  | 90¢ | 1 | ×0.2^28 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^36 = 0.0 |
| | | **Σ** | **63.2** |

`yours 42.0 / Σ 63.2 = 66.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.5% = $2.77/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 3 @ 63¢ → $2.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 63¢ | 5 (3 yours) | ×0.2^0 = 5.0 |
|  | 94¢ | 1 | ×0.2^31 = 0.0 |
|  | 95¢ | 100 | ×0.2^32 = 0.0 |
|  | 99¢ | 15,269 | ×0.2^36 = 0.0 |
| | | **Σ** | **5.0** |

`yours 3.0 / Σ 5.0 = 59.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 59.9% = $2.50/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 29¢ → $2.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 17 (10 yours) | ×0.2^0 = 17.0 |
|  | 28¢ | 10 | ×0.2^1 = 2.0 |
|  | 26¢ | 1 | ×0.2^3 = 0.0 |
|  | 21¢ | 17 | ×0.2^8 = 0.0 |
|  | 20¢ | 10 | ×0.2^9 = 0.0 |
|  | 19¢ | 0 | ×0.2^10 = 0.0 |
|  | 9¢ | 129 | ×0.2^20 = 0.0 |
|  | 2¢ | 50,209 | ×0.2^27 = 0.0 |
| | | **Σ** | **19.0** |

`yours 10.0 / Σ 19.0 = 52.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 52.6% = $2.02/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 10 @ 33¢ → $2.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 16 (10 yours) | ×0.2^0 = 16.0 |
|  | 32¢ | 5 | ×0.2^1 = 1.0 |
|  | 31¢ | 82 | ×0.2^2 = 3.3 |
|  | 1¢ | 200,450 | ×0.2^32 = 0.0 |
| | | **Σ** | **20.3** |

`yours 10.0 / Σ 20.3 = 49.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.3% = $2.06/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 18¢ → $1.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 16 (10 yours) | ×0.2^0 = 16.0 |
|  | 17¢ | 10 | ×0.2^1 = 2.0 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **20.6** |

`yours 10.0 / Σ 20.6 = 48.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.5% = $1.86/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 5 @ 19¢ → $1.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 9 (5 yours) | ×0.2^0 = 9.0 |
|  | 21¢ | 2 | ×0.2^2 = 0.1 |
|  | 22¢ | 46 | ×0.2^3 = 0.4 |
|  | 23¢ | 629 | ×0.2^4 = 1.0 |
|  | 26¢ | 0 | ×0.2^7 = 0.0 |
|  | 38¢ | 0 | ×0.2^19 = 0.0 |
|  | 50¢ | 39 | ×0.2^31 = 0.0 |
|  | 60¢ | 0 | ×0.2^41 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^78 = 0.0 |
| | | **Σ** | **10.5** |

`yours 5.0 / Σ 10.5 = 47.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.8% = $1.84/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 20 @ 47¢ → $1.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 46¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 47¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 49¢ | 462 | ×0.2^3 = 3.7 |
|  | 52¢ | 1 | ×0.2^6 = 0.0 |
|  | 55¢ | 0 | ×0.2^9 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^52 = 0.0 |
| | | **Σ** | **9.7** |

`yours 4.0 / Σ 9.7 = 41.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 41.2% = $1.72/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 5 @ 11¢ → $1.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 11 (5 yours) | ×0.2^0 = 10.5 |
|  | 12¢ | 15 | ×0.2^1 = 3.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 31¢ → $1.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 31¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 33¢ | 244 | ×0.2^2 = 9.8 |
|  | 34¢ | 0 | ×0.2^3 = 0.0 |
|  | 50¢ | 13 | ×0.2^19 = 0.0 |
|  | 63¢ | 0 | ×0.2^32 = 0.0 |
|  | 76¢ | 0 | ×0.2^45 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^66 = 0.0 |
| | | **Σ** | **14.8** |

`yours 5.0 / Σ 14.8 = 33.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.9% = $1.30/day`  

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
|  | 3¢ | 130 | ×0.1^9 = 0.0 |
|  | 1¢ | 35,200 | ×0.1^11 = 0.0 |
| | | **Σ** | **334.0** |

`yours 100.0 / Σ 334.0 = 29.9%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 29.9% = $3.74/day`  

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 30 @ 24¢ → $7.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 104 (30 yours) | ×0.2^0 = 104.0 |
|  | 12¢ | 100 | ×0.2^12 = 0.0 |
|  | 2¢ | 100 | ×0.2^22 = 0.0 |
|  | 1¢ | 5,240 | ×0.2^23 = 0.0 |
| | | **Σ** | **104.0** |

`yours 30.0 / Σ 104.0 = 28.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 28.8% = $7.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 3 @ 19¢ → $1.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 9 (3 yours) | ×0.2^0 = 9.0 |
|  | 21¢ | 2 | ×0.2^2 = 0.1 |
|  | 22¢ | 46 | ×0.2^3 = 0.4 |
|  | 23¢ | 629 | ×0.2^4 = 1.0 |
|  | 26¢ | 0 | ×0.2^7 = 0.0 |
|  | 38¢ | 0 | ×0.2^19 = 0.0 |
|  | 50¢ | 39 | ×0.2^31 = 0.0 |
|  | 60¢ | 0 | ×0.2^41 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^78 = 0.0 |
| | | **Σ** | **10.5** |

`yours 3.0 / Σ 10.5 = 28.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.7% = $1.10/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 2 @ 19¢ → $1.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 7 (2 yours) | ×0.2^0 = 7.0 |
|  | 16¢ | 6 | ×0.2^3 = 0.0 |
|  | 5¢ | 115 | ×0.2^14 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^18 = 0.0 |
| | | **Σ** | **7.1** |

`yours 2.0 / Σ 7.1 = 28.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.3% = $1.09/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5 @ 29¢ → $1.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 17 (5 yours) | ×0.2^0 = 17.0 |
|  | 28¢ | 10 | ×0.2^1 = 2.0 |
|  | 26¢ | 1 | ×0.2^3 = 0.0 |
|  | 21¢ | 17 | ×0.2^8 = 0.0 |
|  | 20¢ | 10 | ×0.2^9 = 0.0 |
|  | 19¢ | 0 | ×0.2^10 = 0.0 |
|  | 9¢ | 129 | ×0.2^20 = 0.0 |
|  | 2¢ | 50,209 | ×0.2^27 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 5 @ 18¢ → $0.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 16 (5 yours) | ×0.2^0 = 16.0 |
|  | 17¢ | 10 | ×0.2^1 = 2.0 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **20.6** |

`yours 5.0 / Σ 20.6 = 24.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 24.2% = $0.93/day`  

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
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,838 resting) | ~36.6% | ~$9.15 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (78,339 resting) | ~32.3% | ~$8.06 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (613,258 resting) | ~7.5% | ~$5.62 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (81,990 resting) | ~6.7% | ~$5.00 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,500 resting) | ~16.9% | ~$4.22 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (322,878 resting) | ~3.9% | ~$2.90 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (190,159 resting) | ~3.6% | ~$2.70 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (72,936 resting) | ~3.4% | ~$2.51 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (52,328 resting) | ~8.3% | ~$2.07 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (281,517 resting) | ~2.4% | ~$1.78 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (67,994 resting) | ~2.2% | ~$1.64 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (219,951 resting) | ~2.0% | ~$1.48 |

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
| 2026-08-08 12:56 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 11:49 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 10:52 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 10:01 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 9:15 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 7:47 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 6:54 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 5:57 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 5:04 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 4:03 AM ET | ✅ ok | 1702 | $1712.09 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
