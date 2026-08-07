# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-07 6:57 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$101.12/day estimated (ceiling, not promise — details below)

**Earned:** $1,659.88 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-05: **$31.46** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-04: **$53.94** · 2026-08-03: **$44.81** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — SELL at the best price, ~$17.41/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-08-31` (~$17.03/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$11.04/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$101.12/day (~$4.21/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 27 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (112,749 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 50.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (4,956 resting ≥ 2,000 ✓) ≈ $12.50/day |
| `dccc-measles-us-2026-12-31-gt3000` | BUY | 77.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~100.0% of bid side (10,320 resting ≥ 10,000 ✓) ≈ $4.17/day (pool ÷ 6 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 65.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (62,975 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (48,562 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 50.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~99.8% of ask side (62,746 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~99.6% of ask side (113,520 resting ≥ 5,000 ✓) ≈ $3.83/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~91.2% of bid side (80,484 resting ≥ 5,000 ✓) ≈ $3.80/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 46.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~90.0% of ask side (98,961 resting ≥ 5,000 ✓) ≈ $3.46/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 82.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~80.0% of ask side (8,450 resting ≥ 5,000 ✓) ≈ $3.33/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 87.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~73.7% of ask side (47,657 resting ≥ 5,000 ✓) ≈ $3.07/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 37.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~70.6% of bid side (80,473 resting ≥ 5,000 ✓) ≈ $2.94/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 8.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~65.3% of bid side (35,471 resting ≥ 2,000 ✓) ≈ $8.17/day |
| `scc-senate-gop-2026-11-03-53` | BUY | 15.0¢ | 26 | 0 | $100.00 | ✅ scoring — ~61.9% of bid side (10,494 resting ≥ 5,000 ✓) ≈ $2.38/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 93.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~61.2% of ask side (42,164 resting ≥ 5,000 ✓) ≈ $2.55/day (pool ÷ 12 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 24.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~46.4% of bid side (5,343 resting ≥ 5,000 ✓) ≈ $11.61/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~39.9% of ask side (100,401 resting ≥ 5,000 ✓) ≈ $1.54/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~39.0% of bid side (50,329 resting ≥ 5,000 ✓) ≈ $1.50/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~37.7% of ask side (117,818 resting ≥ 5,000 ✓) ≈ $1.45/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 6.0¢ | 80 | 0 | $100.00 | ✅ scoring — ~35.6% of bid side (85,228 resting ≥ 5,000 ✓) ≈ $1.48/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~29.3% of bid side (80,495 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~29.3% of bid side (80,495 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 18.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~28.1% of bid side (200,451 resting ≥ 5,000 ✓) ≈ $1.08/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~27.7% of bid side (50,994 resting ≥ 5,000 ✓) ≈ $1.06/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 19.0¢ | 126 | 0 | $100.00 | ✅ scoring — ~27.1% of ask side (6,245 resting ≥ 5,000 ✓) ≈ $6.77/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 7.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~21.6% of bid side (80,657 resting ≥ 5,000 ✓) ≈ $0.83/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~21.4% of bid side (4,036 resting ≥ 2,500 ✓) ≈ $0.73/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~19.3% of ask side (113,722 resting ≥ 5,000 ✓) ≈ $0.74/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 99.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~15.2% of bid side (263,364 resting ≥ 2,000 ✓) ≈ $0.19/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~13.4% of bid side (32,716 resting ≥ 5,000 ✓) ≈ $0.52/day (pool ÷ 13 markets) |
| …and 35 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 27 @ 22¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 27 (27 yours) | ×0.2^0 = 27.3 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 97¢ | 58,044 | ×0.2^75 = 0.0 |
| | | **Σ** | **27.3** |

`yours 27.3 / Σ 27.3 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 10 @ 50¢ → $12.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 85¢ | 9 | ×0.1^35 = 0.0 |
|  | 99¢ | 4,937 | ×0.1^49 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 100.0% = $12.50/day`  

</details>
<details><summary><code>dccc-measles-us-2026-12-31-gt3000</code> BUY 10 @ 77¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 50¢ | 110 | ×0.25^27 = 0.0 |
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
|  | 82¢ | 5 | ×0.2^34 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 20 @ 50¢ → $4.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 52¢ | 1 | ×0.2^2 = 0.0 |
|  | 53¢ | 1 | ×0.2^3 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^48 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 99.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.8% = $4.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 10 @ 29¢ → $3.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 32¢ | 5 | ×0.2^3 = 0.0 |
|  | 50¢ | 100 | ×0.2^21 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^68 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.6% = $3.83/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 75¢ → $3.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 34 (31 yours) | ×0.2^0 = 34.0 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
| | | **Σ** | **34.0** |

`yours 31.0 / Σ 34.0 = 91.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 91.2% = $3.80/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 46¢ → $3.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 48¢ | 2 | ×0.2^2 = 0.1 |
|  | 49¢ | 25 | ×0.2^3 = 0.2 |
|  | 50¢ | 516 | ×0.2^4 = 0.8 |
|  | 97¢ | 43,828 | ×0.2^51 = 0.0 |
| | | **Σ** | **11.1** |

`yours 10.0 / Σ 11.1 = 90.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 90.0% = $3.46/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 20 @ 82¢ → $3.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 25 (20 yours) | ×0.2^0 = 25.0 |
|  | 99¢ | 8,425 | ×0.2^17 = 0.0 |
| | | **Σ** | **25.0** |

`yours 20.0 / Σ 25.0 = 80.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 80.0% = $3.33/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 20 @ 87¢ → $3.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 27 (20 yours) | ×0.2^0 = 27.0 |
|  | 90¢ | 18 | ×0.2^3 = 0.1 |
|  | 98¢ | 45,499 | ×0.2^11 = 0.0 |
| | | **Σ** | **27.1** |

`yours 20.0 / Σ 27.1 = 73.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 73.7% = $3.07/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 15 @ 37¢ → $2.94/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 21 (15 yours) | ×0.2^0 = 21.0 |
|  | 36¢ | 1 | ×0.2^1 = 0.2 |
|  | 35¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^35 = 0.0 |
| | | **Σ** | **21.2** |

`yours 15.0 / Σ 21.2 = 70.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 70.6% = $2.94/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 10 @ 8¢ → $8.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 15 (10 yours) | ×0.1^0 = 15.0 |
|  | 6¢ | 30 | ×0.1^2 = 0.3 |
|  | 3¢ | 100 | ×0.1^5 = 0.0 |
|  | 1¢ | 35,326 | ×0.1^7 = 0.0 |
| | | **Σ** | **15.3** |

`yours 10.0 / Σ 15.3 = 65.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 65.3% = $8.17/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 20 @ 93¢ → $2.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 99¢ | 42,134 | ×0.2^6 = 2.7 |
| | | **Σ** | **32.7** |

`yours 20.0 / Σ 32.7 = 61.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 61.2% = $2.55/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 20 @ 24¢ → $11.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 43 (20 yours) | ×0.2^0 = 43.1 |
|  | 2¢ | 100 | ×0.2^22 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^23 = 0.0 |
| | | **Σ** | **43.1** |

`yours 20.0 / Σ 43.1 = 46.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 46.4% = $11.61/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 20¢ → $1.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 21¢ | 2 | ×0.2^1 = 0.4 |
|  | 22¢ | 12 | ×0.2^2 = 0.5 |
|  | 23¢ | 1,771 | ×0.2^3 = 14.2 |
|  | 47¢ | 99 | ×0.2^27 = 0.0 |
|  | 50¢ | 99 | ×0.2^30 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^77 = 0.0 |
| | | **Σ** | **25.0** |

`yours 10.0 / Σ 25.0 = 39.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 39.9% = $1.54/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 18¢ → $1.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 23 (10 yours) | ×0.2^0 = 23.0 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **25.6** |

`yours 10.0 / Σ 25.6 = 39.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 39.0% = $1.50/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $1.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 53 (20 yours) | ×0.2^0 = 53.1 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **53.1** |

`yours 20.0 / Σ 53.1 = 37.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.7% = $1.45/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 80 @ 6¢ → $1.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 89 (80 yours) | ×0.2^0 = 89.0 |
|  | 2¢ | 84,939 | ×0.2^4 = 135.9 |
| | | **Σ** | **224.9** |

`yours 80.0 / Σ 224.9 = 35.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 35.6% = $1.48/day`  

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
|  | 16¢ | 2 | ×0.2^2 = 0.1 |
|  | 1¢ | 200,431 | ×0.2^17 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 12¢ → $1.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 30 (10 yours) | ×0.2^0 = 30.0 |
|  | 9¢ | 764 | ×0.2^3 = 6.1 |
|  | 2¢ | 50,000 | ×0.2^10 = 0.0 |
| | | **Σ** | **36.1** |

`yours 10.0 / Σ 36.1 = 27.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.7% = $1.06/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 126 @ 19¢ → $6.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 465 (126 yours) | ×0.2^0 = 465.5 |
|  | 25¢ | 579 | ×0.2^6 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^80 = 0.0 |
| | | **Σ** | **465.5** |

`yours 126.0 / Σ 465.5 = 27.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 27.1% = $6.77/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 100 @ 7¢ → $0.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 457 (100 yours) | ×0.2^0 = 457.0 |
|  | 1¢ | 80,200 | ×0.2^6 = 5.1 |
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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 338 | ×0.35^0 = 337.5 |
| ▶ | 1¢ | 3,699 (1,000 yours) | ×0.35^1 = 1,294.6 |
| | | **Σ** | **1,632.1** |

`yours 350.0 / Σ 1,632.1 = 21.4%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 21.4% = $0.73/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 8¢ → $0.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 9¢ | 209 | ×0.2^1 = 41.8 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^89 = 0.0 |
| | | **Σ** | **51.8** |

`yours 10.0 / Σ 51.8 = 19.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.3% = $0.74/day`  

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
|  | 1¢ | 30,200 | ×0.2^2 = 1,208.0 |
| | | **Σ** | **3,724.0** |

`yours 500.0 / Σ 3,724.0 = 13.4%`  
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
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (82,256 resting) | ~69.6% | ~$17.41 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (80,083 resting) | ~68.1% | ~$17.03 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (49,905 resting) | ~44.2% | ~$11.04 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,904 resting) | ~42.3% | ~$10.57 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,122 resting) | ~25.5% | ~$6.37 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (66,350 resting) | ~7.4% | ~$5.52 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (68,126 resting) | ~5.4% | ~$4.04 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (189,096 resting) | ~4.6% | ~$3.42 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (113,614 resting) | ~4.2% | ~$3.16 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (87,849 resting) | ~3.4% | ~$2.57 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (184,733 resting) | ~2.8% | ~$2.11 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (190,335 resting) | ~2.6% | ~$1.92 |

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
| 2026-08-07 6:57 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 5:58 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 5:03 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 4:03 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 3:20 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 2:19 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 2:06 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 1:11 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 12:11 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 11:12 AM ET | ✅ ok | 1676 | $1659.88 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
