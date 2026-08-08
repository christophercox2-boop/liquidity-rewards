# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-08 7:47 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$112.88/day estimated (ceiling, not promise — details below)

**Earned:** $1,712.09 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-06: **$52.21** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-05: **$31.46** · 2026-08-04: **$53.94** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-rep` — SELL at the best price, ~$14.69/day for 200 contracts. Runners-up: `ewc-usgub-ca-2026-11-03-stehil` (~$14.39/day), `ewc-usgub-oh-2026-11-03-dem` (~$9.16/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$112.88/day (~$4.70/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-49` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~99.3% of ask side (113,602 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 25.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~98.9% of bid side (100,684 resting ≥ 5,000 ✓) ≈ $3.81/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~97.5% of bid side (80,581 resting ≥ 5,000 ✓) ≈ $4.06/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~96.5% of bid side (8,012 resting ≥ 5,000 ✓) ≈ $3.71/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 10.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~96.3% of ask side (113,631 resting ≥ 5,000 ✓) ≈ $3.71/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~95.2% of ask side (48,664 resting ≥ 5,000 ✓) ≈ $3.97/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 50.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~90.9% of ask side (11,889 resting ≥ 5,000 ✓) ≈ $3.79/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 12.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~85.3% of bid side (10,690 resting ≥ 5,000 ✓) ≈ $3.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 21.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~85.1% of bid side (50,566 resting ≥ 5,000 ✓) ≈ $3.27/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 84.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~83.3% of ask side (62,628 resting ≥ 5,000 ✓) ≈ $3.47/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (5,544 resting ≥ 2,000 ✓) ≈ $10.41/day |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~75.6% of bid side (50,426 resting ≥ 5,000 ✓) ≈ $2.91/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 5.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~68.7% of ask side (113,728 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 63.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~67.6% of ask side (62,982 resting ≥ 5,000 ✓) ≈ $2.82/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (117,795 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 12.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (80,510 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 33.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.1% of bid side (200,476 resting ≥ 5,000 ✓) ≈ $2.75/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 36.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~61.2% of ask side (48,463 resting ≥ 5,000 ✓) ≈ $2.55/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 63.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~59.9% of ask side (11,801 resting ≥ 5,000 ✓) ≈ $2.50/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 19.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~53.3% of ask side (99,219 resting ≥ 5,000 ✓) ≈ $2.05/day (pool ÷ 13 markets) |
| `dccc-measles-us-2026-12-31-gt3000` | BUY | 78.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~52.6% of bid side (10,452 resting ≥ 10,000 ✓) ≈ $2.19/day (pool ÷ 6 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 12.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~43.8% of ask side (113,529 resting ≥ 5,000 ✓) ≈ $1.69/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~41.2% of ask side (48,210 resting ≥ 5,000 ✓) ≈ $1.72/day (pool ÷ 12 markets) |
| `lawec-cryptoleg-2026-12-31` | SELL | 25.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~37.0% of ask side (31,110 resting ≥ 2,000 ✓) ≈ $2.31/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 13.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~36.3% of ask side (62,983 resting ≥ 5,000 ✓) ≈ $1.51/day (pool ÷ 12 markets) |
| `pvwc-housepopw-2026-11-03-dem` | BUY | 71.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~33.7% of bid side (2,499 resting ≥ 2,000 ✓) ≈ $2.11/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 80.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~32.1% of bid side (50,553 resting ≥ 5,000 ✓) ≈ $1.34/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 5 | 4 | $100.00 | ✅ scoring — ~29.0% of bid side (200,576 resting ≥ 5,000 ✓) ≈ $1.11/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 65.0¢ | 50 | 2 | $100.00 | ✅ scoring — ~27.0% of ask side (62,982 resting ≥ 5,000 ✓) ≈ $1.13/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~25.5% of ask side (62,634 resting ≥ 5,000 ✓) ≈ $1.06/day (pool ÷ 12 markets) |
| …and 55 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 24¢ → $3.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 27¢ | 9 | ×0.2^3 = 0.1 |
|  | 50¢ | 175 | ×0.2^26 = 0.0 |
|  | 76¢ | 0 | ×0.2^52 = 0.0 |
|  | 97¢ | 58,828 | ×0.2^73 = 0.0 |
| | | **Σ** | **10.1** |

`yours 10.0 / Σ 10.1 = 99.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.3% = $3.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 1 @ 25¢ → $3.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 23¢ | 0 | ×0.2^2 = 0.0 |
|  | 22¢ | 0 | ×0.2^3 = 0.0 |
|  | 16¢ | 458 | ×0.2^9 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 75¢ → $4.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 31 (31 yours) | ×0.2^0 = 31.0 |
|  | 72¢ | 100 | ×0.2^3 = 0.8 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 10 @ 8¢ → $3.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 5¢ | 10 | ×0.2^3 = 0.1 |
|  | 2¢ | 2,766 | ×0.2^6 = 0.2 |
|  | 1¢ | 5,225 | ×0.2^7 = 0.1 |
| | | **Σ** | **10.4** |

`yours 10.0 / Σ 10.4 = 96.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 96.5% = $3.71/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 1 @ 10¢ → $3.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 13¢ | 1 | ×0.2^3 = 0.0 |
|  | 22¢ | 27 | ×0.2^12 = 0.0 |
|  | 26¢ | 100 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 88¢ | 0 | ×0.2^78 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^87 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 96.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 96.3% = $3.71/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 20 @ 50¢ → $3.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 22 (20 yours) | ×0.2^0 = 22.0 |
|  | 52¢ | 0 | ×0.2^2 = 0.0 |
|  | 53¢ | 0 | ×0.2^3 = 0.0 |
|  | 54¢ | 0 | ×0.2^4 = 0.0 |
|  | 84¢ | 50 | ×0.2^34 = 0.0 |
|  | 99¢ | 11,817 | ×0.2^49 = 0.0 |
| | | **Σ** | **22.0** |

`yours 20.0 / Σ 22.0 = 90.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 90.9% = $3.79/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 4 @ 12¢ → $3.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 4 (4 yours) | ×0.2^0 = 4.0 |
|  | 9¢ | 1 | ×0.2^3 = 0.0 |
|  | 7¢ | 3 | ×0.2^5 = 0.0 |
|  | 6¢ | 10,457 | ×0.2^6 = 0.7 |
| | | **Σ** | **4.7** |

`yours 4.0 / Σ 4.7 = 85.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 85.3% = $3.28/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 17 @ 21¢ → $3.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 18 (17 yours) | ×0.2^0 = 18.1 |
|  | 20¢ | 10 | ×0.2^1 = 2.0 |
|  | 19¢ | 0 | ×0.2^2 = 0.0 |
|  | 9¢ | 129 | ×0.2^12 = 0.0 |
|  | 2¢ | 50,209 | ×0.2^19 = 0.0 |
| | | **Σ** | **20.1** |

`yours 17.1 / Σ 20.1 = 85.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 85.1% = $3.27/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 20 @ 84¢ → $3.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 24 (20 yours) | ×0.2^0 = 24.0 |
|  | 98¢ | 60,376 | ×0.2^14 = 0.0 |
| | | **Σ** | **24.0** |

`yours 20.0 / Σ 24.0 = 83.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 83.3% = $3.47/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 10 @ 13¢ → $10.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 12 (10 yours) | ×0.1^0 = 12.0 |
|  | 17¢ | 51 | ×0.1^4 = 0.0 |
|  | 26¢ | 192 | ×0.1^13 = 0.0 |
|  | 46¢ | 99 | ×0.1^33 = 0.0 |
|  | 88¢ | 0 | ×0.1^75 = 0.0 |
|  | 99¢ | 5,190 | ×0.1^86 = 0.0 |
| | | **Σ** | **12.0** |

`yours 10.0 / Σ 12.0 = 83.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 83.3% = $10.41/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 18¢ → $2.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 17¢ | 3 | ×0.2^1 = 0.6 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **13.2** |

`yours 10.0 / Σ 13.2 = 75.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 75.6% = $2.91/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 1 @ 5¢ → $2.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 15 | ×0.2^3 = 0.1 |
|  | 9¢ | 209 | ×0.2^4 = 0.3 |
|  | 10¢ | 1 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^92 = 0.0 |
| | | **Σ** | **1.5** |

`yours 1.0 / Σ 1.5 = 68.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.7% = $2.64/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 5 @ 63¢ → $2.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 63¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 64¢ | 2 | ×0.2^1 = 0.4 |
|  | 65¢ | 50 | ×0.2^2 = 2.0 |
|  | 71¢ | 200 | ×0.2^8 = 0.0 |
|  | 90¢ | 1 | ×0.2^27 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^35 = 0.0 |
| | | **Σ** | **7.4** |

`yours 5.0 / Σ 7.4 = 67.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 67.6% = $2.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 40 @ 12¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 60 (40 yours) | ×0.2^0 = 60.0 |
|  | 1¢ | 80,450 | ×0.2^11 = 0.0 |
| | | **Σ** | **60.0** |

`yours 40.0 / Σ 60.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 10 @ 33¢ → $2.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 31¢ | 1 | ×0.2^2 = 0.0 |
|  | 30¢ | 10 | ×0.2^3 = 0.1 |
|  | 1¢ | 200,450 | ×0.2^32 = 0.0 |
| | | **Σ** | **15.1** |

`yours 10.0 / Σ 15.1 = 66.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.1% = $2.75/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 36¢ → $2.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 36¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 37¢ | 1 | ×0.2^1 = 0.2 |
|  | 38¢ | 10 | ×0.2^2 = 0.4 |
|  | 39¢ | 718 | ×0.2^3 = 5.7 |
|  | 59¢ | 0 | ×0.2^23 = 0.0 |
|  | 64¢ | 0 | ×0.2^28 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^62 = 0.0 |
| | | **Σ** | **16.3** |

`yours 10.0 / Σ 16.3 = 61.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 61.2% = $2.55/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 3 @ 63¢ → $2.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 63¢ | 5 (3 yours) | ×0.2^0 = 5.0 |
|  | 79¢ | 20 | ×0.2^16 = 0.0 |
|  | 94¢ | 1 | ×0.2^31 = 0.0 |
|  | 95¢ | 100 | ×0.2^32 = 0.0 |
|  | 99¢ | 11,675 | ×0.2^36 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 3 @ 19¢ → $2.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 3 (3 yours) | ×0.2^0 = 3.0 |
|  | 20¢ | 7 | ×0.2^1 = 1.4 |
|  | 23¢ | 768 | ×0.2^4 = 1.2 |
|  | 38¢ | 0 | ×0.2^19 = 0.0 |
|  | 50¢ | 39 | ×0.2^31 = 0.0 |
|  | 60¢ | 0 | ×0.2^41 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^78 = 0.0 |
| | | **Σ** | **5.6** |

`yours 3.0 / Σ 5.6 = 53.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.3% = $2.05/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt3000</code> BUY 10 @ 78¢ → $2.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 77¢ | 23 | ×0.25^1 = 5.8 |
|  | 75¢ | 209 | ×0.25^3 = 3.3 |
|  | 50¢ | 10 | ×0.25^28 = 0.0 |
|  | 1¢ | 10,200 | ×0.25^77 = 0.0 |
| | | **Σ** | **19.0** |

`yours 10.0 / Σ 19.0 = 52.6%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 52.6% = $2.19/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000` ← this one
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 10 @ 12¢ → $1.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 2 | ×0.2^0 = 1.5 |
| ▶ | 12¢ | 15 (10 yours) | ×0.2^1 = 3.0 |
|  | 14¢ | 1 | ×0.2^3 = 0.0 |
|  | 15¢ | 10 | ×0.2^4 = 0.0 |
|  | 50¢ | 100 | ×0.2^39 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^86 = 0.0 |
| | | **Σ** | **4.6** |

`yours 2.0 / Σ 4.6 = 43.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.8% = $1.69/day`  

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
<details><summary><code>lawec-cryptoleg-2026-12-31</code> SELL 10 @ 25¢ → $2.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 27 (10 yours) | ×0.1^0 = 27.0 |
|  | 28¢ | 1 | ×0.1^3 = 0.0 |
|  | 35¢ | 6 | ×0.1^10 = 0.0 |
|  | 52¢ | 5,764 | ×0.1^27 = 0.0 |
| | | **Σ** | **27.0** |

`yours 10.0 / Σ 27.0 = 37.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 37.0% = $2.31/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-cryptoleg-2026-08-10`
2. `lawec-cryptoleg-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 30 @ 13¢ → $1.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 45 (30 yours) | ×0.2^0 = 45.0 |
|  | 14¢ | 188 | ×0.2^1 = 37.6 |
|  | 20¢ | 1 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^37 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^85 = 0.0 |
| | | **Σ** | **82.6** |

`yours 30.0 / Σ 82.6 = 36.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 36.3% = $1.51/day`  

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
<details><summary><code>pvwc-housepopw-2026-11-03-dem</code> BUY 11 @ 71¢ → $2.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 71¢ | 24 (11 yours) | ×0.1^0 = 24.0 |
|  | 70¢ | 86 | ×0.1^1 = 8.6 |
|  | 64¢ | 30 | ×0.1^7 = 0.0 |
|  | 45¢ | 200 | ×0.1^26 = 0.0 |
|  | 5¢ | 1,100 | ×0.1^66 = 0.0 |
|  | 1¢ | 1,059 | ×0.1^70 = 0.0 |
| | | **Σ** | **32.6** |

`yours 11.0 / Σ 32.6 = 33.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 33.7% = $2.11/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem` ← this one
2. `pvwc-housepopw-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 80¢ → $1.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 14 (10 yours) | ×0.2^0 = 14.0 |
|  | 79¢ | 85 | ×0.2^1 = 17.0 |
|  | 78¢ | 4 | ×0.2^2 = 0.2 |
|  | 72¢ | 0 | ×0.2^8 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^78 = 0.0 |
| | | **Σ** | **31.2** |

`yours 10.0 / Σ 31.2 = 32.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 32.1% = $1.34/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5 @ 19¢ → $1.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 19¢ | 5 (5 yours) | ×0.2^4 = 0.0 |
|  | 18¢ | 30 | ×0.2^5 = 0.0 |
|  | 3¢ | 110 | ×0.2^20 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^22 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 29.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.0% = $1.11/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 65¢ → $1.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 63¢ | 5 | ×0.2^0 = 5.0 |
|  | 64¢ | 2 | ×0.2^1 = 0.4 |
| ▶ | 65¢ | 50 (50 yours) | ×0.2^2 = 2.0 |
|  | 71¢ | 200 | ×0.2^8 = 0.0 |
|  | 90¢ | 1 | ×0.2^27 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^35 = 0.0 |
| | | **Σ** | **7.4** |

`yours 2.0 / Σ 7.4 = 27.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 27.0% = $1.13/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 20 @ 7¢ → $1.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 78 (20 yours) | ×0.2^0 = 78.3 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 98¢ | 60,305 | ×0.2^91 = 0.0 |
| | | **Σ** | **78.3** |

`yours 20.0 / Σ 78.3 = 25.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 25.5% = $1.06/day`  

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
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,895 resting) | ~19.6% | ~$14.69 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (211,008 resting) | ~19.2% | ~$14.39 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (60,101 resting) | ~12.2% | ~$9.16 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,856 resting) | ~32.6% | ~$8.16 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,596 resting) | ~25.7% | ~$6.43 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (614,104 resting) | ~7.0% | ~$5.24 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (50,921 resting) | ~19.8% | ~$4.95 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (40,100 resting) | ~17.4% | ~$4.34 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (323,619 resting) | ~3.3% | ~$2.47 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (89,021 resting) | ~3.2% | ~$2.43 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (190,734 resting) | ~3.2% | ~$2.40 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (281,516 resting) | ~2.7% | ~$2.01 |

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
| 2026-08-08 7:47 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 6:54 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 5:57 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 5:04 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 4:03 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 3:26 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 3:24 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 3:18 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 1:59 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 12:31 AM ET | ✅ ok | 1702 | $1712.09 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
