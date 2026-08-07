# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-07 8:03 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$116.53/day estimated (ceiling, not promise — details below)

**Earned:** $1,659.88 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-05: **$31.46** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-04: **$53.94** · 2026-08-03: **$44.81** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-xavbec` — BUY at the best price, ~$15.32/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-angcra` (~$10.50/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$10.27/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$116.53/day (~$4.86/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 65.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (62,975 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (48,663 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 15.0¢ | 26 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (10,651 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~99.7% of bid side (200,547 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 7.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~96.9% of bid side (35,517 resting ≥ 2,000 ✓) ≈ $12.11/day |
| `lawec-cryptoleg-2026-12-31` | BUY | 25.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~77.2% of bid side (27,603 resting ≥ 2,000 ✓) ≈ $4.82/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 85.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~75.0% of ask side (62,628 resting ≥ 5,000 ✓) ≈ $3.12/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 27 | 0 | $100.00 | ✅ scoring — ~67.7% of ask side (112,762 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 22.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (113,471 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 40.0¢ | 2 | 0 | $50.00 | ✅ scoring — ~66.7% of bid side (10,978 resting ≥ 10,000 ✓) ≈ $2.78/day (pool ÷ 6 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 37.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (80,468 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 66.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.2% of bid side (80,169 resting ≥ 5,000 ✓) ≈ $2.76/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 69.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~60.6% of ask side (12,021 resting ≥ 5,000 ✓) ≈ $2.53/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 75.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~57.1% of ask side (11,719 resting ≥ 5,000 ✓) ≈ $2.38/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 38.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~54.3% of ask side (62,752 resting ≥ 5,000 ✓) ≈ $2.26/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~52.6% of ask side (113,524 resting ≥ 5,000 ✓) ≈ $2.02/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~44.9% of ask side (100,454 resting ≥ 5,000 ✓) ≈ $1.73/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 73.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~44.3% of bid side (80,520 resting ≥ 5,000 ✓) ≈ $1.85/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~43.4% of ask side (62,852 resting ≥ 5,000 ✓) ≈ $1.81/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 13.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~40.3% of ask side (62,891 resting ≥ 5,000 ✓) ≈ $1.68/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 28.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~40.0% of ask side (113,583 resting ≥ 5,000 ✓) ≈ $1.54/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 17.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~38.3% of bid side (50,426 resting ≥ 5,000 ✓) ≈ $1.47/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 10.0¢ | 12 | 0 | $25.00 | ✅ scoring — ~37.2% of ask side (4,035 resting ≥ 2,000 ✓) ≈ $4.66/day |
| `dccc-measles-us-2026-12-31-gt3500` | BUY | 48.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~36.8% of bid side (10,458 resting ≥ 10,000 ✓) ≈ $1.53/day (pool ÷ 6 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 11.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~35.2% of bid side (51,114 resting ≥ 5,000 ✓) ≈ $1.36/day (pool ÷ 13 markets) |
| `dccc-measles-us-2026-12-31-gt3000` | BUY | 72.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~33.3% of bid side (10,490 resting ≥ 10,000 ✓) ≈ $1.39/day (pool ÷ 6 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~33.2% of bid side (80,491 resting ≥ 5,000 ✓) ≈ $1.38/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~33.2% of bid side (80,491 resting ≥ 5,000 ✓) ≈ $1.38/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 10.0¢ | 30 | 1 | $100.00 | ✅ scoring — ~28.6% of bid side (80,495 resting ≥ 5,000 ✓) ≈ $1.19/day (pool ÷ 12 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 24.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~27.6% of bid side (5,419 resting ≥ 5,000 ✓) ≈ $6.90/day (pool ÷ 2 markets) |
| …and 58 more | | | | | | |

**Tap an order for its book window and the math:**

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 15 @ 18¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 16¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 200,531 | ×0.2^17 = 0.0 |
| | | **Σ** | **15.0** |

`yours 15.0 / Σ 15.0 = 99.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.7% = $3.84/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 15 @ 7¢ → $12.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 15 (15 yours) | ×0.1^0 = 15.0 |
|  | 5¢ | 41 | ×0.1^2 = 0.4 |
|  | 4¢ | 30 | ×0.1^3 = 0.0 |
|  | 3¢ | 100 | ×0.1^4 = 0.0 |
|  | 2¢ | 5 | ×0.1^5 = 0.0 |
|  | 1¢ | 35,326 | ×0.1^6 = 0.0 |
| | | **Σ** | **15.5** |

`yours 15.0 / Σ 15.5 = 96.9%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 96.9% = $12.11/day`  

</details>
<details><summary><code>lawec-cryptoleg-2026-12-31</code> BUY 3 @ 25¢ → $4.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 4 (3 yours) | ×0.1^0 = 4.4 |
|  | 20¢ | 4 | ×0.1^5 = 0.0 |
|  | 19¢ | 133 | ×0.1^6 = 0.0 |
|  | 6¢ | 1,125 | ×0.1^19 = 0.0 |
|  | 5¢ | 173 | ×0.1^20 = 0.0 |
|  | 2¢ | 964 | ×0.1^23 = 0.0 |
| | | **Σ** | **4.4** |

`yours 3.4 / Σ 4.4 = 77.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 77.2% = $4.82/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-cryptoleg-2026-08-10`
2. `lawec-cryptoleg-2026-12-31` ← this one

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
|  | 63¢ | 13 | ×0.2^3 = 0.1 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 20 @ 69¢ → $2.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 69¢ | 33 (20 yours) | ×0.2^0 = 33.0 |
|  | 99¢ | 11,988 | ×0.2^30 = 0.0 |
| | | **Σ** | **33.0** |

`yours 20.0 / Σ 33.0 = 60.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 60.6% = $2.53/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 20 @ 75¢ → $2.38/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 35 (20 yours) | ×0.2^0 = 35.0 |
|  | 99¢ | 11,684 | ×0.2^24 = 0.0 |
| | | **Σ** | **35.0** |

`yours 20.0 / Σ 35.0 = 57.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 57.1% = $2.38/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 38¢ → $2.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 16 (10 yours) | ×0.2^0 = 16.0 |
|  | 39¢ | 12 | ×0.2^1 = 2.4 |
|  | 98¢ | 60,499 | ×0.2^60 = 0.0 |
| | | **Σ** | **18.4** |

`yours 10.0 / Σ 18.4 = 54.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 54.3% = $2.26/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 10 @ 29¢ → $2.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 19 (10 yours) | ×0.2^0 = 19.0 |
|  | 50¢ | 100 | ×0.2^21 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^68 = 0.0 |
| | | **Σ** | **19.0** |

`yours 10.0 / Σ 19.0 = 52.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 52.6% = $2.02/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 20¢ → $1.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 23¢ | 1,818 | ×0.2^3 = 14.5 |
|  | 47¢ | 99 | ×0.2^27 = 0.0 |
|  | 50¢ | 99 | ×0.2^30 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^77 = 0.0 |
| | | **Σ** | **44.5** |

`yours 20.0 / Σ 44.5 = 44.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 44.9% = $1.73/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 73¢ → $1.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 73¢ | 70 (31 yours) | ×0.2^0 = 70.0 |
|  | 2¢ | 80,250 | ×0.2^71 = 0.0 |
| | | **Σ** | **70.0** |

`yours 31.0 / Σ 70.0 = 44.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 44.3% = $1.85/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 20 @ 13¢ → $1.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 33 (20 yours) | ×0.2^0 = 33.0 |
|  | 14¢ | 83 | ×0.2^1 = 16.6 |
|  | 20¢ | 1 | ×0.2^7 = 0.0 |
|  | 50¢ | 50 | ×0.2^37 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^85 = 0.0 |
| | | **Σ** | **49.6** |

`yours 20.0 / Σ 49.6 = 40.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 40.3% = $1.68/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 20 @ 28¢ → $1.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 50 (20 yours) | ×0.2^0 = 50.0 |
|  | 50¢ | 125 | ×0.2^22 = 0.0 |
|  | 97¢ | 58,828 | ×0.2^69 = 0.0 |
| | | **Σ** | **50.0** |

`yours 20.0 / Σ 50.0 = 40.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.0% = $1.54/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 12 @ 10¢ → $4.66/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 18 (12 yours) | ×0.1^0 = 18.0 |
|  | 11¢ | 45 | ×0.1^1 = 4.5 |
|  | 12¢ | 972 | ×0.1^2 = 9.7 |
|  | 28¢ | 5 | ×0.1^18 = 0.0 |
|  | 85¢ | 10 | ×0.1^75 = 0.0 |
|  | 99¢ | 2,985 | ×0.1^89 = 0.0 |
| | | **Σ** | **32.2** |

`yours 12.0 / Σ 32.2 = 37.2%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 37.2% = $4.66/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 20 @ 11¢ → $1.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 9¢ | 893 | ×0.2^2 = 35.7 |
|  | 2¢ | 50,000 | ×0.2^9 = 0.0 |
| | | **Σ** | **56.7** |

`yours 20.0 / Σ 56.7 = 35.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 35.2% = $1.36/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt3000</code> BUY 20 @ 72¢ → $1.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 72¢ | 20 (20 yours) | ×0.25^0 = 20.0 |
|  | 71¢ | 160 | ×0.25^1 = 40.0 |
|  | 50¢ | 110 | ×0.25^22 = 0.0 |
|  | 1¢ | 10,200 | ×0.25^71 = 0.0 |
| | | **Σ** | **60.0** |

`yours 20.0 / Σ 60.0 = 33.3%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 33.3% = $1.39/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000` ← this one
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $1.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 30 (10 yours) | ×0.2^0 = 30.0 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **30.1** |

`yours 10.0 / Σ 30.1 = 33.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 33.2% = $1.38/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $1.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 30 (10 yours) | ×0.2^0 = 30.0 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **30.1** |

`yours 10.0 / Σ 30.1 = 33.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 33.2% = $1.38/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 30 @ 10¢ → $1.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 15 | ×0.2^0 = 15.0 |
| ▶ | 10¢ | 30 (30 yours) | ×0.2^1 = 6.0 |
|  | 1¢ | 80,450 | ×0.2^10 = 0.0 |
| | | **Σ** | **21.0** |

`yours 6.0 / Σ 21.0 = 28.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 28.6% = $1.19/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 5 @ 24¢ → $6.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 18 (5 yours) | ×0.2^0 = 18.1 |
|  | 22¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 100 | ×0.2^12 = 0.0 |
|  | 2¢ | 100 | ×0.2^22 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^23 = 0.0 |
| | | **Σ** | **18.1** |

`yours 5.0 / Σ 18.1 = 27.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 27.6% = $6.90/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

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
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (458,228 resting) | ~20.4% | ~$15.32 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,679 resting) | ~42.0% | ~$10.50 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,104 resting) | ~41.1% | ~$10.27 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (60,072 resting) | ~10.3% | ~$7.71 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,604 resting) | ~25.5% | ~$6.37 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (86,582 resting) | ~5.3% | ~$3.97 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (189,962 resting) | ~3.8% | ~$2.82 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (88,982 resting) | ~3.2% | ~$2.41 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (299,292 resting) | ~2.3% | ~$1.70 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (190,979 resting) | ~2.1% | ~$1.56 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (86,332 resting) | ~5.4% | ~$1.36 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (87,591 resting) | ~1.5% | ~$1.11 |

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
| 2026-08-07 8:03 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 8:01 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 7:11 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 6:57 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 6:29 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 6:14 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 5:18 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 3:46 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 1:53 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 12:04 AM ET | ✅ ok | 1676 | $1659.88 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
