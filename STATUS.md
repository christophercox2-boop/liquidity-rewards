# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-07 5:03 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$51.70/day estimated (ceiling, not promise — details below)

**Earned:** $1,659.88 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-05: **$31.46** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-04: **$53.94** · 2026-08-03: **$44.81** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — BUY at the best price, ~$23.23/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-08-31` (~$17.44/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$10.59/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$51.70/day (~$2.15/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 65.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (62,975 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (48,663 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 8.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~94.7% of bid side (35,473 resting ≥ 2,000 ✓) ≈ $11.84/day |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 27 | 0 | $100.00 | ✅ scoring — ~67.7% of ask side (112,762 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~67.4% of bid side (80,496 resting ≥ 5,000 ✓) ≈ $2.81/day (pool ÷ 12 markets) |
| `dccc-measles-us-2026-12-31-gt3000` | BUY | 77.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~66.7% of bid side (10,325 resting ≥ 10,000 ✓) ≈ $2.78/day (pool ÷ 6 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~62.2% of ask side (113,527 resting ≥ 5,000 ✓) ≈ $2.39/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 15.0¢ | 26 | 0 | $100.00 | ✅ scoring — ~61.9% of bid side (10,567 resting ≥ 5,000 ✓) ≈ $2.38/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~29.3% of bid side (80,495 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~29.3% of bid side (80,495 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 18.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~28.1% of bid side (200,335 resting ≥ 5,000 ✓) ≈ $1.08/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 19.0¢ | 126 | 0 | $100.00 | ✅ scoring — ~27.1% of ask side (5,628 resting ≥ 5,000 ✓) ≈ $6.77/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~23.5% of ask side (117,850 resting ≥ 5,000 ✓) ≈ $0.90/day (pool ÷ 13 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 40.0¢ | 2 | 0 | $50.00 | ✅ scoring — ~22.2% of bid side (11,001 resting ≥ 10,000 ✓) ≈ $0.93/day (pool ÷ 6 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 7.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~21.6% of bid side (80,757 resting ≥ 5,000 ✓) ≈ $0.83/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~17.3% of ask side (113,728 resting ≥ 5,000 ✓) ≈ $0.66/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 99.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~15.2% of bid side (263,364 resting ≥ 2,000 ✓) ≈ $0.19/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~13.4% of bid side (32,816 resting ≥ 5,000 ✓) ≈ $0.52/day (pool ÷ 13 markets) |
| `dccc-cyclo-us-2026-08-31-gt8000` | BUY | 95.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~13.3% of bid side (11,025 resting ≥ 10,000 ✓) ≈ $0.56/day (pool ÷ 6 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 13.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~8.8% of bid side (30,634 resting ≥ 5,000 ✓) ≈ $0.34/day (pool ÷ 13 markets) |
| `pandc-anydis-2027-12-31` | BUY | 10.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~7.9% of bid side (10,425 resting ≥ 10,000 ✓) ≈ $0.99/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~5.9% of ask side (100,093 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-butl` | BUY | 1.0¢ | 1,000 | 0 | $500.00 | ✅ scoring — ~5.5% of bid side (18,218 resting ≥ 2,500 ✓) ≈ $0.19/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~4.0% of bid side (49,864 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-lou` | BUY | 4.0¢ | 50 | 0 | $500.00 | ✅ scoring — ~3.5% of bid side (5,373 resting ≥ 2,500 ✓) ≈ $0.12/day (pool ÷ 73 markets) |
| `tec-cbb-champ-2027-04-05-w-duke` | BUY | 16.0¢ | 5 | 0 | $500.00 | ✅ scoring — ~2.9% of bid side (6,997 resting ≥ 2,500 ✓) ≈ $0.10/day (pool ÷ 73 markets) |
| `tec-cbb-champ-2027-04-05-w-mst` | BUY | 7.0¢ | 5 | 0 | $500.00 | ✅ scoring — ~2.3% of bid side (24,600 resting ≥ 2,500 ✓) ≈ $0.08/day (pool ÷ 73 markets) |
| `apdc-alito-2026-12-31` | BUY | 18.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~2.3% of bid side (5,486 resting ≥ 5,000 ✓) ≈ $0.57/day (pool ÷ 2 markets) |
| `stsc-bab-el-mandeb-clsd-2026-12-31` | SELL | 21.0¢ | 10 | 0 | $75.00 | ✅ scoring — ~2.0% of ask side (2,500 resting ≥ 2,000 ✓) ≈ $0.37/day (pool ÷ 2 markets) |
| `tec-cbb-champ-2027-04-05-w-butl` | SELL | 11.0¢ | 2 | 0 | $500.00 | ✅ scoring — ~1.8% of ask side (344,004 resting ≥ 2,500 ✓) ≈ $0.06/day (pool ÷ 73 markets) |
| …and 19 more | | | | | | |

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 10 @ 8¢ → $11.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 7¢ | 2 | ×0.1^1 = 0.2 |
|  | 6¢ | 35 | ×0.1^2 = 0.4 |
|  | 3¢ | 100 | ×0.1^5 = 0.0 |
|  | 1¢ | 35,326 | ×0.1^7 = 0.0 |
| | | **Σ** | **10.6** |

`yours 10.0 / Σ 10.6 = 94.7%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 94.7% = $11.84/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 75¢ → $2.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 46 (31 yours) | ×0.2^0 = 46.0 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
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
<details><summary><code>dccc-measles-us-2026-12-31-gt3000</code> BUY 10 @ 77¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 15 (10 yours) | ×0.25^0 = 15.0 |
|  | 50¢ | 110 | ×0.25^27 = 0.0 |
|  | 1¢ | 10,200 | ×0.25^76 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.7%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000` ← this one
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 10 @ 29¢ → $2.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 16 (10 yours) | ×0.2^0 = 16.0 |
|  | 31¢ | 1 | ×0.2^2 = 0.0 |
|  | 32¢ | 5 | ×0.2^3 = 0.0 |
|  | 50¢ | 100 | ×0.2^21 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^68 = 0.0 |
| | | **Σ** | **16.1** |

`yours 10.0 / Σ 16.1 = 62.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 62.2% = $2.39/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 26 @ 15¢ → $2.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 42 (26 yours) | ×0.2^0 = 42.0 |
|  | 7¢ | 3 | ×0.2^8 = 0.0 |
|  | 6¢ | 10,249 | ×0.2^9 = 0.0 |
| | | **Σ** | **42.0** |

`yours 26.0 / Σ 42.0 = 61.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 61.9% = $2.38/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $1.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 34 (10 yours) | ×0.2^0 = 34.0 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **34.1** |

`yours 10.0 / Σ 34.1 = 29.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 29.3% = $1.22/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $1.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 34 (10 yours) | ×0.2^0 = 34.0 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **34.1** |

`yours 10.0 / Σ 34.1 = 29.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 29.3% = $1.22/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5 @ 18¢ → $1.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 18 (5 yours) | ×0.2^0 = 18.1 |
|  | 16¢ | 1 | ×0.2^2 = 0.0 |
|  | 15¢ | 6 | ×0.2^3 = 0.0 |
|  | 3¢ | 110 | ×0.2^15 = 0.0 |
|  | 1¢ | 200,200 | ×0.2^17 = 0.0 |
| | | **Σ** | **18.2** |

`yours 5.1 / Σ 18.2 = 28.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.1% = $1.08/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 126 @ 19¢ → $6.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 465 (126 yours) | ×0.2^0 = 465.5 |
|  | 24¢ | 24 | ×0.2^5 = 0.0 |
|  | 25¢ | 609 | ×0.2^6 = 0.0 |
|  | 40¢ | 100 | ×0.2^21 = 0.0 |
|  | 99¢ | 4,429 | ×0.2^80 = 0.0 |
| | | **Σ** | **465.5** |

`yours 126.0 / Σ 465.5 = 27.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 27.1% = $6.77/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $0.90/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 85 (20 yours) | ×0.2^0 = 85.1 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **85.1** |

`yours 20.0 / Σ 85.1 = 23.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 23.5% = $0.90/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt4500</code> BUY 2 @ 40¢ → $0.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 9 (2 yours) | ×0.25^0 = 9.0 |
|  | 12¢ | 132 | ×0.25^28 = 0.0 |
|  | 1¢ | 10,860 | ×0.25^39 = 0.0 |
| | | **Σ** | **9.0** |

`yours 2.0 / Σ 9.0 = 22.2%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 22.2% = $0.93/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500` ← this one
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 100 @ 7¢ → $0.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 457 (100 yours) | ×0.2^0 = 457.0 |
|  | 1¢ | 80,300 | ×0.2^6 = 5.1 |
| | | **Σ** | **462.1** |

`yours 100.0 / Σ 462.1 = 21.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 21.6% = $0.83/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 8¢ → $0.66/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 16 (10 yours) | ×0.2^0 = 16.0 |
|  | 9¢ | 209 | ×0.2^1 = 41.8 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^89 = 0.0 |
| | | **Σ** | **57.8** |

`yours 10.0 / Σ 57.8 = 17.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.3% = $0.66/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 40 @ 99¢ → $0.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 264 (40 yours) | ×0.1^0 = 263.6 |
|  | 89¢ | 100 | ×0.1^10 = 0.0 |
|  | 76¢ | 1,000 | ×0.1^23 = 0.0 |
|  | 19¢ | 2,000 | ×0.1^80 = 0.0 |
| | | **Σ** | **263.6** |

`yours 40.0 / Σ 263.6 = 15.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 15.2% = $0.19/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5` ← this one
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 2,516 (500 yours) | ×0.2^0 = 2,516.0 |
|  | 1¢ | 30,300 | ×0.2^2 = 1,212.0 |
| | | **Σ** | **3,728.0** |

`yours 500.0 / Σ 3,728.0 = 13.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 13.4% = $0.52/day`  

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
<details><summary><code>dccc-cyclo-us-2026-08-31-gt8000</code> BUY 10 @ 95¢ → $0.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 75 (10 yours) | ×0.25^0 = 75.0 |
|  | 1¢ | 10,950 | ×0.25^94 = 0.0 |
| | | **Σ** | **75.0** |

`yours 10.0 / Σ 75.0 = 13.3%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 13.3% = $0.56/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-cyclo-us-2026-08-31-gt10000`
2. `dccc-cyclo-us-2026-08-31-gt5000`
3. `dccc-cyclo-us-2026-08-31-gt6000`
4. `dccc-cyclo-us-2026-08-31-gt7000`
5. `dccc-cyclo-us-2026-08-31-gt8000` ← this one
6. `dccc-cyclo-us-2026-08-31-gt9000`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 7 @ 13¢ → $0.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 79 (7 yours) | ×0.2^0 = 79.0 |
|  | 10¢ | 110 | ×0.2^3 = 0.9 |
|  | 2¢ | 30,220 | ×0.2^11 = 0.0 |
| | | **Σ** | **79.9** |

`yours 7.0 / Σ 79.9 = 8.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.8% = $0.34/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> BUY 10 @ 10¢ → $0.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 120 (10 yours) | ×0.25^0 = 120.0 |
|  | 8¢ | 101 | ×0.25^2 = 6.3 |
|  | 2¢ | 4 | ×0.25^8 = 0.0 |
|  | 1¢ | 10,200 | ×0.25^9 = 0.0 |
| | | **Σ** | **126.3** |

`yours 10.0 / Σ 126.3 = 7.9%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 7.9% = $0.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 20 @ 4¢ → $0.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 5¢ | 1,538 | ×0.2^1 = 307.7 |
|  | 6¢ | 23 | ×0.2^2 = 0.9 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^93 = 0.0 |
| | | **Σ** | **338.6** |

`yours 20.0 / Σ 338.6 = 5.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.9% = $0.23/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-butl</code> BUY 1,000 @ 1¢ → $0.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 18,218 (1,000 yours) | ×0.35^0 = 18,218.0 |
| | | **Σ** | **18,218.0** |

`yours 1,000.0 / Σ 18,218.0 = 5.5%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 5.5% = $0.19/day`  

<details><summary>÷ 73 markets in this race (40 known) — tap to list</summary>

1. `tec-cbb-champ-2027-04-05-w-ala`
2. `tec-cbb-champ-2027-04-05-w-ark`
3. `tec-cbb-champ-2027-04-05-w-arz`
4. `tec-cbb-champ-2027-04-05-w-aubrn`
5. `tec-cbb-champ-2027-04-05-w-bayl`
6. `tec-cbb-champ-2027-04-05-w-boise`
7. `tec-cbb-champ-2027-04-05-w-boscol`
8. `tec-cbb-champ-2027-04-05-w-butl` ← this one
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
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 2,000 @ 1¢ → $0.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 49,864 (2,000 yours) | ×0.2^0 = 49,864.0 |
| | | **Σ** | **49,864.0** |

`yours 2,000.0 / Σ 49,864.0 = 4.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 4.0% = $0.15/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-lou</code> BUY 50 @ 4¢ → $0.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 836 (50 yours) | ×0.35^0 = 835.8 |
|  | 3¢ | 1,666 | ×0.35^1 = 583.1 |
| | | **Σ** | **1,418.8** |

`yours 50.0 / Σ 1,418.8 = 3.5%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 3.5% = $0.12/day`  

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
26. `tec-cbb-champ-2027-04-05-w-lou` ← this one
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
<details><summary><code>tec-cbb-champ-2027-04-05-w-duke</code> BUY 5 @ 16¢ → $0.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 155 (5 yours) | ×0.35^0 = 155.0 |
|  | 12¢ | 607 | ×0.35^4 = 9.1 |
|  | 10¢ | 3,359 | ×0.35^6 = 6.2 |
| | | **Σ** | **170.3** |

`yours 5.0 / Σ 170.3 = 2.9%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 2.9% = $0.10/day`  

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
15. `tec-cbb-champ-2027-04-05-w-duke` ← this one
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
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>tec-cbb-champ-2027-04-05-w-mst</code> BUY 5 @ 7¢ → $0.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 110 (5 yours) | ×0.35^0 = 110.0 |
|  | 4¢ | 1,500 | ×0.35^3 = 64.3 |
|  | 2¢ | 50 | ×0.35^5 = 0.3 |
|  | 1¢ | 22,940 | ×0.35^6 = 42.2 |
| | | **Σ** | **216.7** |

`yours 5.0 / Σ 216.7 = 2.3%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 2.3% = $0.08/day`  

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
36. `tec-cbb-champ-2027-04-05-w-mst` ← this one
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 50 @ 18¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 2,200 (50 yours) | ×0.2^0 = 2,199.7 |
|  | 14¢ | 100 | ×0.2^4 = 0.2 |
|  | 12¢ | 6 | ×0.2^6 = 0.0 |
|  | 10¢ | 18 | ×0.2^8 = 0.0 |
|  | 9¢ | 30 | ×0.2^9 = 0.0 |
|  | 1¢ | 3,132 | ×0.2^17 = 0.0 |
| | | **Σ** | **2,199.9** |

`yours 50.0 / Σ 2,199.9 = 2.3%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 2.3% = $0.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>stsc-bab-el-mandeb-clsd-2026-12-31</code> SELL 10 @ 21¢ → $0.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 504 (10 yours) | ×0.25^0 = 504.4 |
|  | 24¢ | 1 | ×0.25^3 = 0.0 |
|  | 30¢ | 103 | ×0.25^9 = 0.0 |
|  | 45¢ | 20 | ×0.25^24 = 0.0 |
|  | 79¢ | 1 | ×0.25^58 = 0.0 |
|  | 97¢ | 25 | ×0.25^76 = 0.0 |
|  | 99¢ | 1,846 | ×0.25^78 = 0.0 |
| | | **Σ** | **504.5** |

`yours 10.0 / Σ 504.5 = 2.0%`  
`$75 ÷ 2 ÷ 2 = $18.75 × 2.0% = $0.37/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `stsc-bab-el-mandeb-clsd-2026-08-31`
2. `stsc-bab-el-mandeb-clsd-2026-12-31` ← this one

</details>

</details>
<details><summary><code>tec-cbb-champ-2027-04-05-w-butl</code> SELL 2 @ 11¢ → $0.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 81 (2 yours) | ×0.35^0 = 81.2 |
|  | 14¢ | 13 | ×0.35^3 = 0.6 |
|  | 15¢ | 187 | ×0.35^4 = 2.8 |
|  | 19¢ | 45 | ×0.35^8 = 0.0 |
|  | 20¢ | 342,178 | ×0.35^9 = 27.0 |
| | | **Σ** | **111.6** |

`yours 2.0 / Σ 111.6 = 1.8%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 1.8% = $0.06/day`  

<details><summary>÷ 73 markets in this race (40 known) — tap to list</summary>

1. `tec-cbb-champ-2027-04-05-w-ala`
2. `tec-cbb-champ-2027-04-05-w-ark`
3. `tec-cbb-champ-2027-04-05-w-arz`
4. `tec-cbb-champ-2027-04-05-w-aubrn`
5. `tec-cbb-champ-2027-04-05-w-bayl`
6. `tec-cbb-champ-2027-04-05-w-boise`
7. `tec-cbb-champ-2027-04-05-w-boscol`
8. `tec-cbb-champ-2027-04-05-w-butl` ← this one
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
40. `tec-cbb-champ-2027-04-05-w-nebr`

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
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (47,219 resting) | ~92.9% | ~$23.23 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (80,178 resting) | ~69.8% | ~$17.44 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,901 resting) | ~42.4% | ~$10.59 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (52,531 resting) | ~37.0% | ~$9.25 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,604 resting) | ~25.5% | ~$6.37 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (188,720 resting) | ~5.2% | ~$3.93 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (90,298 resting) | ~3.6% | ~$2.73 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,212 resting) | ~3.5% | ~$2.65 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (69,186 resting) | ~3.2% | ~$2.41 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (88,498 resting) | ~3.1% | ~$2.29 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (191,745 resting) | ~2.2% | ~$1.69 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (191,396 resting) | ~2.0% | ~$1.48 |

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
| 2026-08-07 5:03 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 4:03 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 3:20 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 2:19 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 2:06 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 1:11 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 12:11 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 11:12 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 9:42 AM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 8:48 AM ET | ✅ ok | 1676 | $1659.88 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
