# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-07 2:19 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$135.08/day estimated (ceiling, not promise — details below)

**Earned:** $1,659.88 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-05: **$31.46** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-04: **$53.94** · 2026-08-03: **$44.81** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — BUY at the best price, ~$23.79/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$10.92/day), `enwc-ussep-mn-2026-08-11-dem-angcra` (~$9.95/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$135.08/day (~$5.63/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 25.0¢ | 80 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (80,620 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 65.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (62,975 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (48,663 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 15.0¢ | 26 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (10,651 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~98.7% of bid side (200,570 resting ≥ 5,000 ✓) ≈ $3.80/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 8.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~89.0% of bid side (35,535 resting ≥ 2,000 ✓) ≈ $11.13/day |
| `pvwc-housepopw-2026-11-03-dem` | BUY | 68.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~88.7% of bid side (12,044 resting ≥ 2,000 ✓) ≈ $5.54/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 85.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~75.0% of ask side (62,628 resting ≥ 5,000 ✓) ≈ $3.12/day (pool ÷ 12 markets) |
| `dccc-measles-us-2026-12-31-gt3000` | BUY | 76.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~69.0% of bid side (10,339 resting ≥ 10,000 ✓) ≈ $2.87/day (pool ÷ 6 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 27 | 0 | $100.00 | ✅ scoring — ~67.7% of ask side (112,762 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 74.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~67.4% of bid side (80,496 resting ≥ 5,000 ✓) ≈ $2.81/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 22.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (113,471 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 40.0¢ | 2 | 0 | $50.00 | ✅ scoring — ~66.7% of bid side (10,978 resting ≥ 10,000 ✓) ≈ $2.78/day (pool ÷ 6 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 37.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (80,468 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 66.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.2% of bid side (80,168 resting ≥ 5,000 ✓) ≈ $2.76/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 38.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.2% of ask side (62,751 resting ≥ 5,000 ✓) ≈ $2.76/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 80.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.2% of bid side (50,477 resting ≥ 5,000 ✓) ≈ $2.76/day (pool ÷ 12 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 24.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~65.7% of bid side (5,438 resting ≥ 5,000 ✓) ≈ $16.41/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~62.3% of ask side (113,522 resting ≥ 5,000 ✓) ≈ $2.40/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | SELL | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~61.2% of ask side (12,017 resting ≥ 5,000 ✓) ≈ $2.55/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~61.2% of bid side (5,663 resting ≥ 5,000 ✓) ≈ $2.35/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 10.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~57.4% of ask side (3,697 resting ≥ 2,000 ✓) ≈ $7.18/day |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 69.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~52.3% of ask side (11,824 resting ≥ 5,000 ✓) ≈ $2.18/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 75.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~51.3% of ask side (11,723 resting ≥ 5,000 ✓) ≈ $2.14/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~43.9% of ask side (100,455 resting ≥ 5,000 ✓) ≈ $1.69/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~43.4% of ask side (62,852 resting ≥ 5,000 ✓) ≈ $1.81/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 13.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~42.9% of ask side (62,863 resting ≥ 5,000 ✓) ≈ $1.79/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 28.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~41.7% of ask side (113,581 resting ≥ 5,000 ✓) ≈ $1.60/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 17.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~38.3% of bid side (50,426 resting ≥ 5,000 ✓) ≈ $1.47/day (pool ÷ 13 markets) |
| `dccc-measles-us-2026-12-31-gt3500` | BUY | 48.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~36.8% of bid side (10,458 resting ≥ 10,000 ✓) ≈ $1.53/day (pool ÷ 6 markets) |
| …and 56 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 80 @ 25¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 80 (80 yours) | ×0.2^0 = 80.0 |
|  | 3¢ | 150 | ×0.2^22 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^23 = 0.0 |
| | | **Σ** | **80.0** |

`yours 80.0 / Σ 80.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 65¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 71¢ | 200 | ×0.2^6 = 0.0 |
|  | 90¢ | 1 | ×0.2^25 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^33 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 20 @ 48¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 51¢ | 1 | ×0.2^3 = 0.0 |
|  | 59¢ | 5 | ×0.2^11 = 0.0 |
|  | 60¢ | 100 | ×0.2^12 = 0.0 |
|  | 83¢ | 812 | ×0.2^35 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 26 @ 15¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 26 (26 yours) | ×0.2^0 = 26.0 |
|  | 9¢ | 100 | ×0.2^6 = 0.0 |
|  | 7¢ | 3 | ×0.2^8 = 0.0 |
|  | 6¢ | 10,249 | ×0.2^9 = 0.0 |
| | | **Σ** | **26.0** |

`yours 26.0 / Σ 26.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.84/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 15 @ 18¢ → $3.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 15¢ | 24 | ×0.2^3 = 0.2 |
|  | 1¢ | 200,531 | ×0.2^17 = 0.0 |
| | | **Σ** | **15.2** |

`yours 15.0 / Σ 15.2 = 98.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.7% = $3.80/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 15 @ 8¢ → $11.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 15 (15 yours) | ×0.1^0 = 15.0 |
|  | 7¢ | 18 | ×0.1^1 = 1.8 |
|  | 5¢ | 41 | ×0.1^3 = 0.0 |
|  | 4¢ | 30 | ×0.1^4 = 0.0 |
|  | 3¢ | 100 | ×0.1^5 = 0.0 |
|  | 2¢ | 5 | ×0.1^6 = 0.0 |
|  | 1¢ | 35,326 | ×0.1^7 = 0.0 |
| | | **Σ** | **16.8** |

`yours 15.0 / Σ 16.8 = 89.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 89.0% = $11.13/day`  

</details>
<details><summary><code>pvwc-housepopw-2026-11-03-dem</code> BUY 10 @ 68¢ → $5.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 68¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 67¢ | 13 | ×0.1^1 = 1.3 |
|  | 60¢ | 1,221 | ×0.1^8 = 0.0 |
|  | 5¢ | 600 | ×0.1^63 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^67 = 0.0 |
| | | **Σ** | **11.3** |

`yours 10.0 / Σ 11.3 = 88.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 88.7% = $5.54/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem` ← this one
2. `pvwc-housepopw-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 18 @ 85¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 24 (18 yours) | ×0.2^0 = 24.0 |
|  | 98¢ | 60,376 | ×0.2^13 = 0.0 |
| | | **Σ** | **24.0** |

`yours 18.0 / Σ 24.0 = 75.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 75.0% = $3.12/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt3000</code> BUY 20 @ 76¢ → $2.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 76¢ | 29 (20 yours) | ×0.25^0 = 29.0 |
|  | 50¢ | 110 | ×0.25^26 = 0.0 |
|  | 1¢ | 10,200 | ×0.25^75 = 0.0 |
| | | **Σ** | **29.0** |

`yours 20.0 / Σ 29.0 = 69.0%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 69.0% = $2.87/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000` ← this one
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 27 @ 22¢ → $2.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 40 (27 yours) | ×0.2^0 = 40.3 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 97¢ | 58,044 | ×0.2^75 = 0.0 |
| | | **Σ** | **40.3** |

`yours 27.3 / Σ 40.3 = 67.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.7% = $2.60/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 74¢ → $2.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 46 (31 yours) | ×0.2^0 = 46.0 |
|  | 2¢ | 80,250 | ×0.2^72 = 0.0 |
| | | **Σ** | **46.0** |

`yours 31.0 / Σ 46.0 = 67.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 67.4% = $2.81/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 20 @ 22¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 50¢ | 39 | ×0.2^28 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^75 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt4500</code> BUY 2 @ 40¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 3 (2 yours) | ×0.25^0 = 3.0 |
|  | 12¢ | 132 | ×0.25^28 = 0.0 |
|  | 1¢ | 10,843 | ×0.25^39 = 0.0 |
| | | **Σ** | **3.0** |

`yours 2.0 / Σ 3.0 = 66.7%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500` ← this one
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 10 @ 37¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 21¢ | 3 | ×0.2^16 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^35 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 10 @ 66¢ → $2.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 66¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 63¢ | 12 | ×0.2^3 = 0.1 |
|  | 2¢ | 79,941 | ×0.2^64 = 0.0 |
| | | **Σ** | **15.1** |

`yours 10.0 / Σ 15.1 = 66.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.2% = $2.76/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 38¢ → $2.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 41¢ | 12 | ×0.2^3 = 0.1 |
|  | 98¢ | 60,499 | ×0.2^60 = 0.0 |
| | | **Σ** | **15.1** |

`yours 10.0 / Σ 15.1 = 66.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.2% = $2.76/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 80¢ → $2.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 77¢ | 12 | ×0.2^3 = 0.1 |
|  | 2¢ | 50,250 | ×0.2^78 = 0.0 |
| | | **Σ** | **15.1** |

`yours 10.0 / Σ 15.1 = 66.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.2% = $2.76/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 25 @ 24¢ → $16.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 38 (25 yours) | ×0.2^0 = 38.1 |
|  | 12¢ | 100 | ×0.2^12 = 0.0 |
|  | 2¢ | 100 | ×0.2^22 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^23 = 0.0 |
| | | **Σ** | **38.1** |

`yours 25.0 / Σ 38.1 = 65.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 65.7% = $16.41/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 10 @ 29¢ → $2.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 16 (10 yours) | ×0.2^0 = 16.0 |
|  | 31¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^21 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^68 = 0.0 |
| | | **Σ** | **16.0** |

`yours 10.0 / Σ 16.0 = 62.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 62.3% = $2.40/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> SELL 10 @ 82¢ → $2.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 84¢ | 7 | ×0.2^2 = 0.3 |
|  | 85¢ | 132 | ×0.2^3 = 1.1 |
|  | 93¢ | 123 | ×0.2^11 = 0.0 |
|  | 99¢ | 11,740 | ×0.2^17 = 0.0 |
| | | **Σ** | **16.3** |

`yours 10.0 / Σ 16.3 = 61.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 61.2% = $2.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 10 @ 8¢ → $2.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 16 (10 yours) | ×0.2^0 = 16.2 |
|  | 2¢ | 232 | ×0.2^6 = 0.0 |
|  | 1¢ | 5,415 | ×0.2^7 = 0.1 |
| | | **Σ** | **16.3** |

`yours 10.0 / Σ 16.3 = 61.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 61.2% = $2.35/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 10 @ 10¢ → $7.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 11¢ | 6 | ×0.1^1 = 0.6 |
|  | 12¢ | 682 | ×0.1^2 = 6.8 |
|  | 28¢ | 5 | ×0.1^18 = 0.0 |
|  | 85¢ | 10 | ×0.1^75 = 0.0 |
|  | 99¢ | 2,985 | ×0.1^89 = 0.0 |
| | | **Σ** | **17.4** |

`yours 10.0 / Σ 17.4 = 57.4%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 57.4% = $7.18/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 10 @ 69¢ → $2.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 69¢ | 19 (10 yours) | ×0.2^0 = 19.0 |
|  | 72¢ | 13 | ×0.2^3 = 0.1 |
|  | 99¢ | 11,792 | ×0.2^30 = 0.0 |
| | | **Σ** | **19.1** |

`yours 10.0 / Σ 19.1 = 52.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 52.3% = $2.18/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 20 @ 75¢ → $2.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 39 (20 yours) | ×0.2^0 = 39.0 |
|  | 99¢ | 11,684 | ×0.2^24 = 0.0 |
| | | **Σ** | **39.0** |

`yours 20.0 / Σ 39.0 = 51.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 51.3% = $2.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 20¢ → $1.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 31 (20 yours) | ×0.2^0 = 31.0 |
|  | 23¢ | 1,818 | ×0.2^3 = 14.5 |
|  | 47¢ | 99 | ×0.2^27 = 0.0 |
|  | 50¢ | 99 | ×0.2^30 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^77 = 0.0 |
| | | **Σ** | **45.5** |

`yours 20.0 / Σ 45.5 = 43.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.9% = $1.69/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 20 @ 48¢ → $1.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 26 (20 yours) | ×0.2^0 = 26.0 |
|  | 49¢ | 100 | ×0.2^1 = 20.1 |
|  | 52¢ | 1 | ×0.2^4 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **46.1** |

`yours 20.0 / Σ 46.1 = 43.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 43.4% = $1.81/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 20 @ 13¢ → $1.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 14¢ | 83 | ×0.2^1 = 16.6 |
|  | 20¢ | 1 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^37 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^85 = 0.0 |
| | | **Σ** | **46.6** |

`yours 20.0 / Σ 46.6 = 42.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 42.9% = $1.79/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 20 @ 28¢ → $1.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 48 (20 yours) | ×0.2^0 = 48.0 |
|  | 50¢ | 125 | ×0.2^22 = 0.0 |
|  | 97¢ | 58,828 | ×0.2^69 = 0.0 |
| | | **Σ** | **48.0** |

`yours 20.0 / Σ 48.0 = 41.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 41.7% = $1.60/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 17¢ → $1.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 13 (10 yours) | ×0.2^0 = 13.0 |
|  | 16¢ | 64 | ×0.2^1 = 12.8 |
|  | 14¢ | 42 | ×0.2^3 = 0.3 |
|  | 2¢ | 50,000 | ×0.2^15 = 0.0 |
| | | **Σ** | **26.1** |

`yours 10.0 / Σ 26.1 = 38.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.3% = $1.47/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt3500</code> BUY 20 @ 48¢ → $1.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 20 (20 yours) | ×0.25^0 = 20.0 |
|  | 47¢ | 138 | ×0.25^1 = 34.4 |
|  | 40¢ | 100 | ×0.25^8 = 0.0 |
|  | 1¢ | 10,200 | ×0.25^47 = 0.0 |
| | | **Σ** | **54.4** |

`yours 20.0 / Σ 54.4 = 36.8%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 36.8% = $1.53/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500` ← this one
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-04 | ~$67.52 | $53.94 | 80% |
| 2026-08-03 | ~$65.16 | $44.81 | 69% |
| 2026-08-02 | ~$31.04 | $14.05 | 45% |

Biggest gaps on 2026-08-04: `scc-senate-gop-2026-11-03-47` (est ~$4.95 → got $2.83), `scc-senate-gop-2026-11-03-51` (est ~$2.27 → got $0.33), `scc-senate-gop-2026-11-03-52` (est ~$2.25 → got $0.36)

_2026-08-05 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (49,501 resting) | ~95.2% | ~$23.79 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,887 resting) | ~43.7% | ~$10.92 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (70,467 resting) | ~39.8% | ~$9.95 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,604 resting) | ~25.5% | ~$6.37 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (102,623 resting) | ~4.4% | ~$3.29 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (87,968 resting) | ~3.3% | ~$2.49 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (189,222 resting) | ~3.1% | ~$2.35 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (69,608 resting) | ~3.0% | ~$2.26 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (192,665 resting) | ~2.6% | ~$1.94 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (93,198 resting) | ~1.9% | ~$1.44 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (86,326 resting) | ~5.4% | ~$1.35 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (72,601 resting) | ~1.4% | ~$1.04 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,627.01 |
| Pending | $31.46 |
| Skipped | $1.41 |
| **Total earned** | **$1,659.88** |

1676 reward rows · 34 days with rewards · 362 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-05 ⚠️ multi-day pending bucket | $31.46 | `███` |
| 2026-08-04 | $53.94 | `█████` |
| 2026-08-03 | $44.81 | `████` |
| 2026-08-02 | $14.05 | `█` |
| 2026-08-01 | $52.30 | `█████` |
| 2026-07-31 | $67.96 | `██████` |
| 2026-07-30 | $20.67 | `██` |
| 2026-07-29 | $53.60 | `█████` |
| 2026-07-28 | $79.65 | `███████` |
| 2026-07-27 | $125.34 | `███████████` |
| 2026-07-26 | $153.80 | `██████████████` |
| 2026-07-25 | $125.69 | `███████████` |
| 2026-07-24 | $135.19 | `████████████` |
| 2026-07-23 | $227.63 | `████████████████████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $196.56 | `███` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $66.95 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `apdc-jerpowgov-2026-12-31` | $42.68 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `opdc-mcconnell-resign-2026-11-02` | $39.75 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.92 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.83 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-07 2:19 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 2:06 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 1:11 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 12:11 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 11:12 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 9:42 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 8:48 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 8:23 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 8:03 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 8:01 AM ET | ✅ ok | 1676 | $1659.88 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
