# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-07 9:26 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$113.72/day estimated (ceiling, not promise — details below)

**Earned:** $1,712.09 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-06: **$52.21** · 2026-08-05: **$31.46** · 2026-08-04: **$53.94** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-08-31` — SELL at the best price, ~$17.27/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$10.46/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$6.43/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$113.72/day (~$4.74/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `dccc-measles-us-2026-12-31-gt3000` | BUY | 77.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~100.0% of bid side (10,220 resting ≥ 10,000 ✓) ≈ $4.17/day (pool ÷ 6 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 26.0¢ | 80 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (80,620 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 15.0¢ | 26 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (10,503 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 65.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (62,975 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 14.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~99.8% of bid side (35,477 resting ≥ 2,000 ✓) ≈ $12.48/day |
| `scc-senate-gop-2026-11-03-51` | BUY | 18.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~99.2% of bid side (200,551 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~95.2% of ask side (48,664 resting ≥ 5,000 ✓) ≈ $3.97/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 27.0¢ | 22 | 0 | $25.00 | ✅ scoring — ~78.0% of ask side (4,097 resting ≥ 2,000 ✓) ≈ $9.75/day |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~75.6% of bid side (50,426 resting ≥ 5,000 ✓) ≈ $2.91/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 84.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~74.5% of ask side (62,648 resting ≥ 5,000 ✓) ≈ $3.10/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~68.8% of ask side (113,516 resting ≥ 5,000 ✓) ≈ $2.65/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 37.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~68.1% of bid side (80,473 resting ≥ 5,000 ✓) ≈ $2.84/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 27 | 0 | $100.00 | ✅ scoring — ~67.7% of ask side (112,762 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.5% of ask side (113,521 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.5% of bid side (80,466 resting ≥ 5,000 ✓) ≈ $2.77/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~64.6% of bid side (80,498 resting ≥ 5,000 ✓) ≈ $2.69/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~63.2% of bid side (5,664 resting ≥ 5,000 ✓) ≈ $2.43/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 69.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~60.6% of ask side (18,247 resting ≥ 5,000 ✓) ≈ $2.53/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 82.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~54.1% of ask side (11,715 resting ≥ 5,000 ✓) ≈ $2.25/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 21.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~51.9% of bid side (200,232 resting ≥ 5,000 ✓) ≈ $2.16/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~51.6% of bid side (51,380 resting ≥ 5,000 ✓) ≈ $1.99/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~49.6% of bid side (80,483 resting ≥ 5,000 ✓) ≈ $2.07/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~49.6% of bid side (80,483 resting ≥ 5,000 ✓) ≈ $2.07/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 50.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~40.8% of ask side (48,048 resting ≥ 5,000 ✓) ≈ $1.70/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~39.6% of bid side (11,150 resting ≥ 5,000 ✓) ≈ $1.52/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | SELL | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~37.8% of ask side (6,552 resting ≥ 5,000 ✓) ≈ $1.58/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~36.7% of ask side (48,547 resting ≥ 5,000 ✓) ≈ $1.53/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 34.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~35.4% of ask side (98,620 resting ≥ 5,000 ✓) ≈ $1.36/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 52.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~32.3% of bid side (50,549 resting ≥ 5,000 ✓) ≈ $1.34/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 13.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~29.6% of ask side (62,968 resting ≥ 5,000 ✓) ≈ $1.23/day (pool ÷ 12 markets) |
| …and 44 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>dccc-measles-us-2026-12-31-gt3000</code> BUY 10 @ 77¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 50¢ | 10 | ×0.25^27 = 0.0 |
|  | 1¢ | 10,200 | ×0.25^76 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000` ← this one
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 80 @ 26¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 80 (80 yours) | ×0.2^0 = 80.0 |
|  | 10¢ | 150 | ×0.2^16 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^24 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 26 @ 15¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 26 (26 yours) | ×0.2^0 = 26.0 |
|  | 7¢ | 3 | ×0.2^8 = 0.0 |
|  | 6¢ | 10,249 | ×0.2^9 = 0.0 |
| | | **Σ** | **26.0** |

`yours 26.0 / Σ 26.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 20 @ 14¢ → $12.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 20 (20 yours) | ×0.1^0 = 20.0 |
|  | 12¢ | 1 | ×0.1^2 = 0.0 |
|  | 11¢ | 30 | ×0.1^3 = 0.0 |
|  | 3¢ | 100 | ×0.1^11 = 0.0 |
|  | 1¢ | 35,326 | ×0.1^13 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 99.8%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 99.8% = $12.48/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5 @ 18¢ → $3.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 5 (5 yours) | ×0.2^0 = 5.1 |
|  | 15¢ | 5 | ×0.2^3 = 0.0 |
|  | 3¢ | 110 | ×0.2^15 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^17 = 0.0 |
| | | **Σ** | **5.2** |

`yours 5.1 / Σ 5.2 = 99.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.2% = $3.82/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 22 @ 27¢ → $9.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 22 (22 yours) | ×0.1^0 = 22.1 |
|  | 28¢ | 5 | ×0.1^1 = 0.5 |
|  | 29¢ | 572 | ×0.1^2 = 5.7 |
|  | 39¢ | 414 | ×0.1^12 = 0.0 |
|  | 46¢ | 99 | ×0.1^19 = 0.0 |
|  | 99¢ | 2,985 | ×0.1^72 = 0.0 |
| | | **Σ** | **28.3** |

`yours 22.1 / Σ 28.3 = 78.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 78.0% = $9.75/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 18 @ 84¢ → $3.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 24 (18 yours) | ×0.2^0 = 24.0 |
|  | 87¢ | 20 | ×0.2^3 = 0.2 |
|  | 98¢ | 60,376 | ×0.2^14 = 0.0 |
| | | **Σ** | **24.2** |

`yours 18.0 / Σ 24.2 = 74.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 74.5% = $3.10/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 10 @ 12¢ → $2.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 15 (10 yours) | ×0.2^0 = 14.5 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^85 = 0.0 |
| | | **Σ** | **14.5** |

`yours 10.0 / Σ 14.5 = 68.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.8% = $2.65/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 15 @ 37¢ → $2.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 22 (15 yours) | ×0.2^0 = 22.0 |
|  | 35¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^35 = 0.0 |
| | | **Σ** | **22.0** |

`yours 15.0 / Σ 22.0 = 68.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 68.1% = $2.84/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 10 @ 29¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 31¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^21 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^68 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.5% = $2.56/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 10 @ 12¢ → $2.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 80,450 | ×0.2^11 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.5% = $2.77/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 75¢ → $2.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 48 (31 yours) | ×0.2^0 = 48.0 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
| | | **Σ** | **48.0** |

`yours 31.0 / Σ 48.0 = 64.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 64.6% = $2.69/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 10 @ 8¢ → $2.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 16 (10 yours) | ×0.2^0 = 15.7 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 232 | ×0.2^6 = 0.0 |
|  | 1¢ | 5,415 | ×0.2^7 = 0.1 |
| | | **Σ** | **15.8** |

`yours 10.0 / Σ 15.8 = 63.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 63.2% = $2.43/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 20 @ 69¢ → $2.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 69¢ | 33 (20 yours) | ×0.2^0 = 33.0 |
|  | 99¢ | 18,214 | ×0.2^30 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 20 @ 82¢ → $2.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 37 (20 yours) | ×0.2^0 = 37.0 |
|  | 99¢ | 11,678 | ×0.2^17 = 0.0 |
| | | **Σ** | **37.0** |

`yours 20.0 / Σ 37.0 = 54.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 54.1% = $2.25/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 10 @ 21¢ → $2.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 16 (10 yours) | ×0.2^0 = 16.0 |
|  | 20¢ | 16 | ×0.2^1 = 3.3 |
|  | 1¢ | 200,200 | ×0.2^20 = 0.0 |
| | | **Σ** | **19.3** |

`yours 10.0 / Σ 19.3 = 51.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 51.9% = $2.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 12¢ → $1.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 9¢ | 1,170 | ×0.2^3 = 9.4 |
|  | 2¢ | 50,000 | ×0.2^10 = 0.0 |
| | | **Σ** | **19.4** |

`yours 10.0 / Σ 19.4 = 51.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 51.6% = $1.99/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $2.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 20 (10 yours) | ×0.2^0 = 20.0 |
|  | 49¢ | 2 | ×0.2^2 = 0.1 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **20.2** |

`yours 10.0 / Σ 20.2 = 49.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.6% = $2.07/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $2.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 20 (10 yours) | ×0.2^0 = 20.0 |
|  | 49¢ | 2 | ×0.2^2 = 0.1 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **20.2** |

`yours 10.0 / Σ 20.2 = 49.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.6% = $2.07/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 50¢ → $1.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 51¢ | 12 | ×0.2^1 = 2.4 |
|  | 52¢ | 302 | ×0.2^2 = 12.1 |
|  | 98¢ | 45,499 | ×0.2^48 = 0.0 |
| | | **Σ** | **24.5** |

`yours 10.0 / Σ 24.5 = 40.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 40.8% = $1.70/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $1.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 850 (500 yours) | ×0.2^0 = 850.0 |
|  | 1¢ | 10,300 | ×0.2^2 = 412.0 |
| | | **Σ** | **1,262.0** |

`yours 500.0 / Σ 1,262.0 = 39.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 39.6% = $1.52/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> SELL 10 @ 82¢ → $1.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 85¢ | 1,424 | ×0.2^3 = 11.4 |
|  | 87¢ | 123 | ×0.2^5 = 0.0 |
|  | 99¢ | 4,989 | ×0.2^17 = 0.0 |
| | | **Σ** | **26.4** |

`yours 10.0 / Σ 26.4 = 37.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 37.8% = $1.58/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 20 @ 47¢ → $1.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 48¢ | 9 | ×0.2^1 = 1.8 |
|  | 49¢ | 791 | ×0.2^2 = 31.7 |
|  | 52¢ | 1 | ×0.2^5 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^51 = 0.0 |
| | | **Σ** | **54.5** |

`yours 20.0 / Σ 54.5 = 36.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 36.7% = $1.53/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 34¢ → $1.36/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 14 (10 yours) | ×0.2^0 = 14.0 |
|  | 35¢ | 71 | ×0.2^1 = 14.2 |
|  | 37¢ | 2 | ×0.2^3 = 0.0 |
|  | 38¢ | 25 | ×0.2^4 = 0.0 |
|  | 50¢ | 100 | ×0.2^16 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^63 = 0.0 |
| | | **Σ** | **28.3** |

`yours 10.0 / Σ 28.3 = 35.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 35.4% = $1.36/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 52¢ → $1.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 52¢ | 14 (10 yours) | ×0.2^0 = 14.0 |
|  | 51¢ | 85 | ×0.2^1 = 17.0 |
|  | 2¢ | 50,250 | ×0.2^50 = 0.0 |
| | | **Σ** | **31.0** |

`yours 10.0 / Σ 31.0 = 32.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 32.3% = $1.34/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 20 @ 13¢ → $1.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 14¢ | 188 | ×0.2^1 = 37.6 |
|  | 20¢ | 1 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^37 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^85 = 0.0 |
| | | **Σ** | **67.6** |

`yours 20.0 / Σ 67.6 = 29.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 29.6% = $1.23/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-06 | ~$60.78 | $52.21 | 86% |
| 2026-08-05 | ~$33.74 | $31.46 | 93% |
| 2026-08-04 | ~$67.52 | $53.94 | 80% |

Biggest gaps on 2026-08-06: `scc-senate-gop-2026-11-03-52` (est ~$1.89 → got $0.00), `opdc-mcconnell-resign-2026-11-02` (est ~$8.92 → got $8.07), `scc-hrep-rep-2026-11-03-gte195` (est ~$3.20 → got $2.38)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (80,178 resting) | ~69.1% | ~$17.27 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,909 resting) | ~41.8% | ~$10.46 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,596 resting) | ~25.7% | ~$6.43 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,799 resting) | ~25.1% | ~$6.27 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,067 resting) | ~6.6% | ~$4.95 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (188,263 resting) | ~3.4% | ~$2.54 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (87,916 resting) | ~3.4% | ~$2.51 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (51,280 resting) | ~8.4% | ~$2.10 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (191,957 resting) | ~2.8% | ~$2.10 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (184,926 resting) | ~2.7% | ~$2.05 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (336,662 resting) | ~2.3% | ~$1.74 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,273 resting) | ~5.1% | ~$1.28 |

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
| 2026-08-06 | $52.21 | `███████` |
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
| 2026-08-07 9:26 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-07 9:17 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-07 9:03 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 7:51 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 6:57 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 5:58 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 5:03 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 4:03 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 3:20 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 2:19 PM ET | ✅ ok | 1676 | $1659.88 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
