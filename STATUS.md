# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-06 6:02 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$53.79/day estimated (ceiling, not promise — details below)

**Earned:** $1,628.42 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-04: **$53.94** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-03: **$44.81** · 2026-08-02: **$14.05** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — SELL at the best price, ~$21.93/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-12-31` (~$20.01/day), `ewc-usse-tx-2026-11-03-rep` (~$11.92/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$53.79/day (~$2.24/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 37.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (62,841 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 65.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~92.6% of ask side (62,955 resting ≥ 5,000 ✓) ≈ $3.86/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~91.3% of ask side (117,796 resting ≥ 5,000 ✓) ≈ $3.51/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 19.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.6% of ask side (113,458 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 20.0¢ | 80 | 0 | $100.00 | ✅ scoring — ~62.0% of bid side (80,429 resting ≥ 5,000 ✓) ≈ $2.58/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 13.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~57.1% of ask side (62,870 resting ≥ 5,000 ✓) ≈ $2.38/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 14.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~55.6% of bid side (35,627 resting ≥ 2,000 ✓) ≈ $6.94/day |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 27 | 0 | $100.00 | ✅ scoring — ~46.8% of ask side (112,780 resting ≥ 5,000 ✓) ≈ $1.80/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 15.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~46.3% of bid side (85,944 resting ≥ 5,000 ✓) ≈ $1.93/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~38.5% of bid side (200,634 resting ≥ 5,000 ✓) ≈ $1.48/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~33.4% of ask side (100,575 resting ≥ 5,000 ✓) ≈ $1.29/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 85.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~29.9% of bid side (80,275 resting ≥ 5,000 ✓) ≈ $1.24/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | SELL | 19.0¢ | 126 | 0 | $100.00 | ✅ scoring — ~27.8% of ask side (6,332 resting ≥ 5,000 ✓) ≈ $6.95/day (pool ÷ 2 markets) |
| `ewc-usse-mi-2026-11-03-dem` | BUY | 61.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~27.0% of bid side (210,754 resting ≥ 2,000 ✓) ≈ $1.68/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 87.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~24.8% of ask side (62,590 resting ≥ 5,000 ✓) ≈ $1.03/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 86.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~22.3% of bid side (50,469 resting ≥ 5,000 ✓) ≈ $0.93/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~20.2% of bid side (4,474 resting ≥ 2,500 ✓) ≈ $0.69/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 19.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~20.1% of bid side (100,746 resting ≥ 5,000 ✓) ≈ $0.77/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~19.0% of ask side (48,718 resting ≥ 5,000 ✓) ≈ $0.79/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~18.8% of bid side (80,514 resting ≥ 5,000 ✓) ≈ $0.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~18.8% of bid side (80,514 resting ≥ 5,000 ✓) ≈ $0.78/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~17.3% of bid side (25,810 resting ≥ 5,000 ✓) ≈ $0.67/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 99.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~13.3% of bid side (110,301 resting ≥ 2,000 ✓) ≈ $0.17/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 5.0¢ | 133 | 0 | $100.00 | ✅ scoring — ~11.0% of bid side (50,993 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 6.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~7.8% of ask side (113,618 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 8.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~6.9% of ask side (101,211 resting ≥ 5,000 ✓) ≈ $0.26/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 99.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~6.6% of bid side (110,301 resting ≥ 2,000 ✓) ≈ $0.08/day (pool ÷ 10 markets) |
| `apdc-alito-2026-12-31` | BUY | 18.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~6.5% of bid side (7,294 resting ≥ 5,000 ✓) ≈ $1.62/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 6.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~6.1% of ask side (100,412 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~5.9% of ask side (48,150 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 12 markets) |
| …and 22 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 40 @ 37¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 52¢ | 1 | ×0.2^15 = 0.0 |
|  | 69¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^61 = 0.0 |
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
7. `scc-hrep-rep-2026-11-03-gte210` ← this one
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 65¢ → $3.86/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 54 (50 yours) | ×0.2^0 = 54.0 |
|  | 71¢ | 200 | ×0.2^6 = 0.0 |
|  | 90¢ | 1 | ×0.2^25 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^33 = 0.0 |
| | | **Σ** | **54.0** |

`yours 50.0 / Σ 54.0 = 92.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 92.6% = $3.86/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 21 @ 4¢ → $3.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 21 (21 yours) | ×0.2^0 = 21.0 |
|  | 5¢ | 10 | ×0.2^1 = 2.0 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **23.0** |

`yours 21.0 / Σ 23.0 = 91.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 91.3% = $3.51/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 10 @ 19¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 22¢ | 2 | ×0.2^3 = 0.0 |
|  | 50¢ | 39 | ×0.2^31 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^78 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.6% = $2.56/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 80 @ 20¢ → $2.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 129 (80 yours) | ×0.2^0 = 129.0 |
|  | 10¢ | 150 | ×0.2^10 = 0.0 |
|  | 6¢ | 10 | ×0.2^14 = 0.0 |
|  | 2¢ | 79,940 | ×0.2^18 = 0.0 |
| | | **Σ** | **129.0** |

`yours 80.0 / Σ 129.0 = 62.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 62.0% = $2.58/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 30 @ 13¢ → $2.38/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 36 (30 yours) | ×0.2^0 = 36.0 |
|  | 14¢ | 83 | ×0.2^1 = 16.6 |
|  | 20¢ | 1 | ×0.2^7 = 0.0 |
|  | 50¢ | 50 | ×0.2^37 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^85 = 0.0 |
| | | **Σ** | **52.6** |

`yours 30.0 / Σ 52.6 = 57.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 57.1% = $2.38/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 20 @ 14¢ → $6.94/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 36 (20 yours) | ×0.1^0 = 36.0 |
|  | 7¢ | 5 | ×0.1^7 = 0.0 |
|  | 6¢ | 30 | ×0.1^8 = 0.0 |
|  | 4¢ | 6 | ×0.1^10 = 0.0 |
|  | 1¢ | 35,550 | ×0.1^13 = 0.0 |
| | | **Σ** | **36.0** |

`yours 20.0 / Σ 36.0 = 55.6%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 55.6% = $6.94/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 27 @ 22¢ → $1.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 58 (27 yours) | ×0.2^0 = 58.3 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 97¢ | 58,044 | ×0.2^75 = 0.0 |
| | | **Σ** | **58.3** |

`yours 27.3 / Σ 58.3 = 46.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 46.8% = $1.80/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 100 @ 15¢ → $1.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 216 (100 yours) | ×0.2^0 = 216.0 |
|  | 8¢ | 100 | ×0.2^7 = 0.0 |
|  | 7¢ | 81 | ×0.2^8 = 0.0 |
|  | 6¢ | 100 | ×0.2^9 = 0.0 |
|  | 3¢ | 5,247 | ×0.2^12 = 0.0 |
| | | **Σ** | **216.0** |

`yours 100.0 / Σ 216.0 = 46.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 46.3% = $1.93/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 15 @ 18¢ → $1.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 39 (15 yours) | ×0.2^0 = 39.0 |
|  | 6¢ | 2 | ×0.2^12 = 0.0 |
|  | 5¢ | 50 | ×0.2^13 = 0.0 |
|  | 4¢ | 112 | ×0.2^14 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^17 = 0.0 |
| | | **Σ** | **39.0** |

`yours 15.0 / Σ 39.0 = 38.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.5% = $1.48/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 20¢ → $1.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 14 (10 yours) | ×0.2^0 = 14.0 |
|  | 22¢ | 9 | ×0.2^2 = 0.4 |
|  | 23¢ | 1,946 | ×0.2^3 = 15.6 |
|  | 47¢ | 99 | ×0.2^27 = 0.0 |
|  | 50¢ | 99 | ×0.2^30 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^77 = 0.0 |
| | | **Σ** | **29.9** |

`yours 10.0 / Σ 29.9 = 33.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.4% = $1.29/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 20 @ 85¢ → $1.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 67 (20 yours) | ×0.2^0 = 67.0 |
|  | 2¢ | 80,008 | ×0.2^83 = 0.0 |
| | | **Σ** | **67.0** |

`yours 20.0 / Σ 67.0 = 29.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 29.9% = $1.24/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 126 @ 19¢ → $6.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 453 (126 yours) | ×0.2^0 = 453.0 |
|  | 25¢ | 579 | ×0.2^6 = 0.0 |
|  | 49¢ | 100 | ×0.2^30 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^80 = 0.0 |
| | | **Σ** | **453.0** |

`yours 126.0 / Σ 453.0 = 27.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 27.8% = $6.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ewc-usse-mi-2026-11-03-dem</code> BUY 5 @ 61¢ → $1.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 61¢ | 6 (5 yours) | ×0.1^0 = 6.0 |
|  | 59¢ | 780 | ×0.1^2 = 7.8 |
|  | 58¢ | 4,748 | ×0.1^3 = 4.7 |
| | | **Σ** | **18.5** |

`yours 5.0 / Σ 18.5 = 27.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.0% = $1.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-mi-2026-11-03-dem` ← this one
2. `ewc-usse-mi-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 25 @ 87¢ → $1.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 101 (25 yours) | ×0.2^0 = 101.0 |
|  | 98¢ | 60,376 | ×0.2^11 = 0.0 |
| | | **Σ** | **101.0** |

`yours 25.0 / Σ 101.0 = 24.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 24.8% = $1.03/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 2 @ 86¢ → $0.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 86¢ | 9 (2 yours) | ×0.2^0 = 9.0 |
|  | 83¢ | 10 | ×0.2^3 = 0.1 |
|  | 2¢ | 50,250 | ×0.2^84 = 0.0 |
| | | **Σ** | **9.1** |

`yours 2.0 / Σ 9.1 = 22.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 22.3% = $0.93/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 250 | ×0.35^0 = 250.0 |
| ▶ | 1¢ | 4,224 (1,000 yours) | ×0.35^1 = 1,478.4 |
| | | **Σ** | **1,728.4** |

`yours 350.0 / Σ 1,728.4 = 20.2%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 20.2% = $0.69/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 20 @ 19¢ → $0.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 96 (20 yours) | ×0.2^0 = 96.0 |
|  | 16¢ | 450 | ×0.2^3 = 3.6 |
|  | 2¢ | 100,000 | ×0.2^17 = 0.0 |
| | | **Σ** | **99.6** |

`yours 20.0 / Σ 99.6 = 20.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.1% = $0.77/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 20 @ 48¢ → $0.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 106 (20 yours) | ×0.2^0 = 105.5 |
|  | 83¢ | 912 | ×0.2^35 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **105.5** |

`yours 20.0 / Σ 105.5 = 19.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.0% = $0.79/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $0.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 53 (10 yours) | ×0.2^0 = 53.0 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **53.1** |

`yours 10.0 / Σ 53.1 = 18.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.8% = $0.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $0.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 53 (10 yours) | ×0.2^0 = 53.0 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **53.1** |

`yours 10.0 / Σ 53.1 = 18.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.8% = $0.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 766 | ×0.2^0 = 766.0 |
| ▶ | 1¢ | 25,044 (5,000 yours) | ×0.2^1 = 5,008.8 |
| | | **Σ** | **5,774.8** |

`yours 1,000.0 / Σ 5,774.8 = 17.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.3% = $0.67/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 40 @ 99¢ → $0.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 301 (40 yours) | ×0.1^0 = 301.4 |
|  | 18¢ | 3,000 | ×0.1^81 = 0.0 |
| | | **Σ** | **301.4** |

`yours 40.0 / Σ 301.4 = 13.3%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 13.3% = $0.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 133 @ 5¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 813 (133 yours) | ×0.2^0 = 813.0 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **1,212.8** |

`yours 133.0 / Σ 1,212.8 = 11.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.0% = $0.42/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 1 @ 6¢ → $0.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 12 (1 yours) | ×0.2^0 = 12.0 |
|  | 9¢ | 100 | ×0.2^3 = 0.8 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 16¢ | 3 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^91 = 0.0 |
| | | **Σ** | **12.8** |

`yours 1.0 / Σ 12.8 = 7.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.8% = $0.30/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 40 @ 8¢ → $0.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 50 (40 yours) | ×0.2^0 = 50.0 |
|  | 9¢ | 2,659 | ×0.2^1 = 531.8 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^89 = 0.0 |
| | | **Σ** | **581.8** |

`yours 40.0 / Σ 581.8 = 6.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.9% = $0.26/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 20 @ 99¢ → $0.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 301 (20 yours) | ×0.1^0 = 301.4 |
|  | 18¢ | 3,000 | ×0.1^81 = 0.0 |
| | | **Σ** | **301.4** |

`yours 20.0 / Σ 301.4 = 6.6%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 6.6% = $0.08/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 50 @ 18¢ → $1.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 749 (50 yours) | ×0.2^0 = 749.0 |
|  | 17¢ | 100 | ×0.2^1 = 20.0 |
|  | 15¢ | 30 | ×0.2^3 = 0.2 |
|  | 11¢ | 1,215 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^17 = 0.0 |
| | | **Σ** | **769.3** |

`yours 50.0 / Σ 769.3 = 6.5%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 6.5% = $1.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 25 @ 6¢ → $0.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 38 (25 yours) | ×0.2^0 = 38.0 |
|  | 7¢ | 1,872 | ×0.2^1 = 374.4 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^91 = 0.0 |
| | | **Σ** | **412.4** |

`yours 25.0 / Σ 412.4 = 6.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.1% = $0.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 25 @ 7¢ → $0.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 424 (25 yours) | ×0.2^0 = 424.3 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^91 = 0.0 |
| | | **Σ** | **424.3** |

`yours 25.0 / Σ 424.3 = 5.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.9% = $0.25/day`  

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

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-03 | ~$56.69 | $44.81 | 79% |
| 2026-08-02 | ~$25.55 | $14.05 | 55% |
| 2026-08-01 | ~$46.23 | $52.30 | 113% |

Biggest gaps on 2026-08-03: `scc-senate-gop-2026-11-03-47` (est ~$5.15 → got $1.15), `scc-senate-gop-2026-11-03-49` (est ~$4.73 → got $2.54), `apdc-alito-2026-12-31` (est ~$15.91 → got $14.18)

_2026-08-04 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (58,146 resting) | ~87.7% | ~$21.93 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,500 resting) | ~80.0% | ~$20.01 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (252,137 resting) | ~15.9% | ~$11.92 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,116 resting) | ~34.5% | ~$8.63 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (61,197 resting) | ~9.3% | ~$6.95 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (376,523 resting) | ~6.6% | ~$4.95 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,522 resting) | ~19.7% | ~$4.93 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (64,406 resting) | ~3.7% | ~$2.78 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (85,628 resting) | ~3.5% | ~$2.59 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (188,033 resting) | ~3.2% | ~$2.37 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (48,257 resting) | ~8.2% | ~$2.05 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (104,722 resting) | ~2.7% | ~$2.03 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,514.21 |
| Pending | $113.00 |
| Skipped | $1.21 |
| **Total earned** | **$1,628.42** |

1648 reward rows · 33 days with rewards · 362 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-04 ⚠️ multi-day pending bucket | $53.94 | `█████` |
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
| 2026-07-22 | $82.95 | `███████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $165.10 | `██` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `apdc-alito-2026-12-31` | $61.51 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `apdc-jerpowgov-2026-12-31` | $42.68 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `opdc-mcconnell-resign-2026-11-02` | $39.45 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-06 6:02 AM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-06 3:06 AM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 11:44 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:54 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:26 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:22 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:14 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:06 PM ET | ✅ ok | 1640 | $1624.44 |
| 2026-08-05 9:04 PM ET | ✅ ok | 1613 | $1574.48 |
| 2026-08-05 8:52 PM ET | ✅ ok | 1611 | $1574.28 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
