# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-04 6:31 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$49.88/day estimated (ceiling, not promise — details below)

**Earned:** $1,529.47 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-02: **$14.05** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-01: **$52.30** · 2026-07-31: **$67.96** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$16.85/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$14.18/day), `ewc-usgub-ca-2026-11-03-xavbec` (~$9.88/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$49.88/day (~$2.08/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 50.0¢ | 7 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (265,051 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 25.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~91.2% of bid side (55,422 resting ≥ 5,000 ✓) ≈ $3.51/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 20.0¢ | 125 | 0 | $100.00 | ✅ scoring — ~89.4% of ask side (8,991 resting ≥ 5,000 ✓) ≈ $22.35/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~84.4% of ask side (98,560 resting ≥ 5,000 ✓) ≈ $3.25/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 13.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~71.6% of bid side (50,367 resting ≥ 5,000 ✓) ≈ $2.75/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~57.4% of ask side (112,791 resting ≥ 5,000 ✓) ≈ $2.21/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 28 | 0 | $100.00 | ✅ scoring — ~47.5% of ask side (112,784 resting ≥ 5,000 ✓) ≈ $1.83/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 7.0¢ | 48 | 0 | $100.00 | ✅ scoring — ~31.0% of ask side (100,973 resting ≥ 5,000 ✓) ≈ $1.19/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 40.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~28.6% of bid side (85,260 resting ≥ 5,000 ✓) ≈ $1.19/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~27.2% of bid side (80,318 resting ≥ 5,000 ✓) ≈ $1.13/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 61.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~24.5% of ask side (62,744 resting ≥ 5,000 ✓) ≈ $1.02/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 12.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~23.6% of bid side (35,607 resting ≥ 2,000 ✓) ≈ $2.95/day |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~19.9% of bid side (4,549 resting ≥ 2,500 ✓) ≈ $0.68/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 15.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~16.4% of ask side (62,922 resting ≥ 5,000 ✓) ≈ $0.68/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~13.5% of ask side (62,882 resting ≥ 5,000 ✓) ≈ $0.56/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 61.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~11.8% of ask side (62,744 resting ≥ 5,000 ✓) ≈ $0.49/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 8.0¢ | 44 | 0 | $100.00 | ✅ scoring — ~9.7% of bid side (11,148 resting ≥ 5,000 ✓) ≈ $0.37/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~7.8% of bid side (80,628 resting ≥ 5,000 ✓) ≈ $0.33/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 5.0¢ | 133 | 0 | $100.00 | ✅ scoring — ~7.3% of bid side (52,025 resting ≥ 5,000 ✓) ≈ $0.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 1 | $100.00 | ✅ scoring — ~5.5% of bid side (52,025 resting ≥ 5,000 ✓) ≈ $0.21/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 20.0¢ | 15 | 2 | $100.00 | ✅ scoring — ~5.1% of ask side (98,560 resting ≥ 5,000 ✓) ≈ $0.19/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 30 | 3 | $100.00 | ✅ scoring — ~4.7% of ask side (62,738 resting ≥ 5,000 ✓) ≈ $0.20/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~4.1% of ask side (48,089 resting ≥ 5,000 ✓) ≈ $0.17/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-mst` | BUY | 7.0¢ | 5 | 0 | $500.00 | ✅ scoring — ~1.9% of bid side (103,138 resting ≥ 2,500 ✓) ≈ $0.07/day (pool ÷ 73 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 75.0¢ | 10 | 1 | $25.00 | ✅ scoring — ~1.7% of ask side (185,095 resting ≥ 2,000 ✓) ≈ $0.02/day (pool ÷ 10 markets) |
| `ewc-usse-oh-2026-11-03-rep` | BUY | 48.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~1.1% of bid side (46,550 resting ≥ 5,000 ✓) ≈ $0.28/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 2.0¢ | 200 | 0 | $100.00 | ✅ scoring — ~0.9% of bid side (27,814 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~0.8% of bid side (120,288 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 13 markets) |
| `ewc-usse-tx-2026-11-03-dem` | BUY | 47.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~0.8% of bid side (378,140 resting ≥ 10,000 ✓) ≈ $0.61/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~0.6% of bid side (91,295 resting ≥ 5,000 ✓) ≈ $0.02/day (pool ÷ 13 markets) |
| …and 20 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 7 @ 50¢ → $1.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 7 (7 yours) | ×0.1^0 = 7.1 |
|  | 53¢ | 1 | ×0.1^3 = 0.0 |
|  | 73¢ | 24 | ×0.1^23 = 0.0 |
|  | 74¢ | 30 | ×0.1^24 = 0.0 |
|  | 89¢ | 5 | ×0.1^39 = 0.0 |
|  | 97¢ | 104,984 | ×0.1^47 = 0.0 |
| | | **Σ** | **7.1** |

`yours 7.1 / Σ 7.1 = 100.0%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 100.0% = $1.25/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10` ← this one
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 25¢ → $3.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 22¢ | 12 | ×0.2^3 = 0.1 |
|  | 2¢ | 50,209 | ×0.2^23 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 91.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 91.2% = $3.51/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 125 @ 20¢ → $22.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 137 (125 yours) | ×0.2^0 = 137.0 |
|  | 22¢ | 71 | ×0.2^2 = 2.9 |
|  | 99¢ | 8,783 | ×0.2^79 = 0.0 |
| | | **Σ** | **139.9** |

`yours 125.0 / Σ 139.9 = 89.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 89.4% = $22.35/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 10 @ 18¢ → $3.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 11 (10 yours) | ×0.2^0 = 11.0 |
|  | 19¢ | 1 | ×0.2^1 = 0.2 |
|  | 20¢ | 16 | ×0.2^2 = 0.7 |
|  | 40¢ | 30 | ×0.2^22 = 0.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^79 = 0.0 |
| | | **Σ** | **11.9** |

`yours 10.0 / Σ 11.9 = 84.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 84.4% = $3.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 13¢ → $2.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 11¢ | 99 | ×0.2^2 = 4.0 |
|  | 3¢ | 58 | ×0.2^10 = 0.0 |
|  | 2¢ | 50,000 | ×0.2^11 = 0.0 |
| | | **Σ** | **14.0** |

`yours 10.0 / Σ 14.0 = 71.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 71.6% = $2.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 15 @ 18¢ → $2.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 26 (15 yours) | ×0.2^0 = 26.0 |
|  | 20¢ | 3 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 97¢ | 58,083 | ×0.2^79 = 0.0 |
| | | **Σ** | **26.1** |

`yours 15.0 / Σ 26.1 = 57.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 57.4% = $2.21/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 28 @ 22¢ → $1.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 59 (28 yours) | ×0.2^0 = 59.1 |
|  | 24¢ | 3 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 97¢ | 58,044 | ×0.2^75 = 0.0 |
| | | **Σ** | **59.3** |

`yours 28.1 / Σ 59.3 = 47.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.5% = $1.83/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 48 @ 7¢ → $1.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 58 (48 yours) | ×0.2^0 = 57.9 |
|  | 9¢ | 2,413 | ×0.2^2 = 96.5 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^90 = 0.0 |
| | | **Σ** | **154.4** |

`yours 47.9 / Σ 154.4 = 31.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.0% = $1.19/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 40¢ → $1.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 35 (10 yours) | ×0.2^0 = 35.0 |
|  | 38¢ | 0 | ×0.2^2 = 0.0 |
|  | 30¢ | 25 | ×0.2^10 = 0.0 |
|  | 2¢ | 80,000 | ×0.2^38 = 0.0 |
| | | **Σ** | **35.0** |

`yours 10.0 / Σ 35.0 = 28.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 28.6% = $1.19/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 30 @ 85¢ → $1.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 110 (30 yours) | ×0.2^0 = 110.2 |
|  | 83¢ | 0 | ×0.2^2 = 0.0 |
|  | 2¢ | 80,008 | ×0.2^83 = 0.0 |
| | | **Σ** | **110.2** |

`yours 30.0 / Σ 110.2 = 27.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 27.2% = $1.13/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 10 @ 61¢ → $1.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 61¢ | 41 (10 yours) | ×0.2^0 = 40.8 |
|  | 63¢ | 0 | ×0.2^2 = 0.0 |
|  | 66¢ | 1 | ×0.2^5 = 0.0 |
|  | 90¢ | 1 | ×0.2^29 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^37 = 0.0 |
| | | **Σ** | **40.8** |

`yours 10.0 / Σ 40.8 = 24.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 24.5% = $1.02/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 25 @ 12¢ → $2.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 106 (25 yours) | ×0.1^0 = 106.0 |
|  | 10¢ | 10 | ×0.1^2 = 0.1 |
|  | 4¢ | 6 | ×0.1^8 = 0.0 |
|  | 3¢ | 5 | ×0.1^9 = 0.0 |
|  | 2¢ | 30 | ×0.1^10 = 0.0 |
|  | 1¢ | 35,450 | ×0.1^11 = 0.0 |
| | | **Σ** | **106.1** |

`yours 25.0 / Σ 106.1 = 23.6%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 23.6% = $2.95/day`  

</details>
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 250 | ×0.35^0 = 250.0 |
| ▶ | 1¢ | 4,299 (1,000 yours) | ×0.35^1 = 1,504.6 |
| | | **Σ** | **1,754.6** |

`yours 350.0 / Σ 1,754.6 = 19.9%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 19.9% = $0.68/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 10 @ 15¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 27 (10 yours) | ×0.2^0 = 27.0 |
|  | 16¢ | 170 | ×0.2^1 = 34.0 |
|  | 17¢ | 0 | ×0.2^2 = 0.0 |
|  | 50¢ | 25 | ×0.2^35 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^83 = 0.0 |
| | | **Σ** | **61.0** |

`yours 10.0 / Σ 61.0 = 16.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.4% = $0.68/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 10 @ 48¢ → $0.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 74 (10 yours) | ×0.2^0 = 74.0 |
|  | 50¢ | 0 | ×0.2^2 = 0.0 |
|  | 54¢ | 107 | ×0.2^6 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **74.0** |

`yours 10.0 / Σ 74.0 = 13.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 13.5% = $0.56/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 5 @ 61¢ → $0.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 61¢ | 41 (5 yours) | ×0.2^0 = 40.8 |
|  | 63¢ | 0 | ×0.2^2 = 0.0 |
|  | 66¢ | 1 | ×0.2^5 = 0.0 |
|  | 90¢ | 1 | ×0.2^29 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^37 = 0.0 |
| | | **Σ** | **40.8** |

`yours 4.8 / Σ 40.8 = 11.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.8% = $0.49/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 44 @ 8¢ → $0.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 44 (44 yours) | ×0.2^0 = 44.0 |
|  | 6¢ | 10,266 | ×0.2^2 = 410.6 |
| | | **Σ** | **454.6** |

`yours 44.0 / Σ 454.6 = 9.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.7% = $0.37/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 10 @ 10¢ → $0.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 128 (10 yours) | ×0.2^0 = 128.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 80,498 | ×0.2^9 = 0.0 |
| | | **Σ** | **128.1** |

`yours 10.0 / Σ 128.1 = 7.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.8% = $0.33/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 133 @ 5¢ → $0.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1,312 (133 yours) | ×0.2^0 = 1,312.0 |
|  | 4¢ | 500 | ×0.2^1 = 100.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **1,813.2** |

`yours 133.0 / Σ 1,813.2 = 7.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.3% = $0.28/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $0.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 1,312 | ×0.2^0 = 1,312.0 |
| ▶ | 4¢ | 500 (500 yours) | ×0.2^1 = 100.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **1,813.2** |

`yours 100.0 / Σ 1,813.2 = 5.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.5% = $0.21/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 15 @ 20¢ → $0.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 11 | ×0.2^0 = 11.0 |
|  | 19¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 20¢ | 16 (15 yours) | ×0.2^2 = 0.7 |
|  | 40¢ | 30 | ×0.2^22 = 0.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^79 = 0.0 |
| | | **Σ** | **11.9** |

`yours 0.6 / Σ 11.9 = 5.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.1% = $0.19/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 30 @ 47¢ → $0.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 44¢ | 5 | ×0.2^0 = 4.8 |
|  | 46¢ | 2 | ×0.2^2 = 0.1 |
| ▶ | 47¢ | 30 (30 yours) | ×0.2^3 = 0.2 |
|  | 52¢ | 1 | ×0.2^8 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^54 = 0.0 |
| | | **Σ** | **5.1** |

`yours 0.2 / Σ 5.1 = 4.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.7% = $0.20/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 15 @ 7¢ → $0.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 363 (15 yours) | ×0.2^0 = 363.0 |
|  | 9¢ | 0 | ×0.2^2 = 0.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^91 = 0.0 |
| | | **Σ** | **363.0** |

`yours 15.0 / Σ 363.0 = 4.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.1% = $0.17/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-mst</code> BUY 5 @ 7¢ → $0.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 60 (5 yours) | ×0.35^0 = 60.0 |
|  | 5¢ | 20 | ×0.35^2 = 2.4 |
|  | 4¢ | 258 | ×0.35^3 = 11.1 |
|  | 1¢ | 102,800 | ×0.35^6 = 189.0 |
| | | **Σ** | **262.4** |

`yours 5.0 / Σ 262.4 = 1.9%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 1.9% = $0.07/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> SELL 10 @ 75¢ → $0.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 74¢ | 55 | ×0.1^0 = 55.0 |
| ▶ | 75¢ | 40 (10 yours) | ×0.1^1 = 4.0 |
|  | 99¢ | 185,000 | ×0.1^25 = 0.0 |
| | | **Σ** | **59.0** |

`yours 1.0 / Σ 59.0 = 1.7%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 1.7% = $0.02/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15` ← this one
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
<details><summary><code>ewc-usse-oh-2026-11-03-rep</code> BUY 50 @ 48¢ → $0.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 4,429 (50 yours) | ×0.2^0 = 4,429.0 |
|  | 46¢ | 1,921 | ×0.2^2 = 76.8 |
| | | **Σ** | **4,505.8** |

`yours 50.0 / Σ 4,505.8 = 1.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 1.1% = $0.28/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-oh-2026-11-03-dem`
2. `ewc-usse-oh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 200 @ 2¢ → $0.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 22,614 (200 yours) | ×0.2^0 = 22,614.0 |
| | | **Σ** | **22,614.0** |

`yours 200.0 / Σ 22,614.0 = 0.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.9% = $0.03/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 120,088 (1,000 yours) | ×0.2^0 = 120,088.0 |
| | | **Σ** | **120,088.0** |

`yours 1,000.0 / Σ 120,088.0 = 0.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.8% = $0.03/day`  

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
<details><summary><code>ewc-usse-tx-2026-11-03-dem</code> BUY 50 @ 47¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 5,734 (50 yours) | ×0.2^0 = 5,734.0 |
|  | 46¢ | 2,173 | ×0.2^1 = 434.6 |
|  | 45¢ | 2 | ×0.2^2 = 0.1 |
|  | 39¢ | 15,000 | ×0.2^8 = 0.0 |
| | | **Σ** | **6,168.7** |

`yours 50.0 / Σ 6,168.7 = 0.8%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 0.8% = $0.61/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-tx-2026-11-03-dem` ← this one
2. `ewc-usse-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 81,095 (500 yours) | ×0.2^0 = 81,095.0 |
| | | **Σ** | **81,095.0** |

`yours 500.0 / Σ 81,095.0 = 0.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.6% = $0.02/day`  

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

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-01 | ~$46.23 | $52.30 | 113% |
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |

Biggest gaps on 2026-08-01: `scc-hrep-rep-2026-11-03-gte215` (est ~$2.09 → got $1.51), `scc-senate-gop-2026-11-03-52` (est ~$3.15 → got $2.78), `cranc-uspres28-12-31-2026-tedcru` (est ~$0.71 → got $0.35)

_2026-08-02 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,567 resting) | ~67.4% | ~$16.85 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (46,105 resting) | ~18.9% | ~$14.18 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (66,651 resting) | ~13.2% | ~$9.88 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (180,370 resting) | ~7.1% | ~$5.32 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,897 resting) | ~20.4% | ~$5.10 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (88,170 resting) | ~10.8% | ~$2.69 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (236,678 resting) | ~3.2% | ~$2.40 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (91,857 resting) | ~2.4% | ~$1.83 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (189,191 resting) | ~2.3% | ~$1.74 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (54,931 resting) | ~2.3% | ~$1.70 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (98,751 resting) | ~1.7% | ~$1.30 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (63,391 resting) | ~4.6% | ~$1.15 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,514.21 |
| Pending | $14.05 |
| Skipped | $1.21 |
| **Total earned** | **$1,529.47** |

1573 reward rows · 31 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-02 ⚠️ multi-day pending bucket | $14.05 | `█` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $66.35 | `█` |
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $35.05 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `apdc-alito-2026-12-31` | $23.38 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-04 6:31 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 4:46 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 2:57 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 1:06 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 10:45 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 8:21 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 6:01 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 2:43 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 11:42 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 10:10 PM ET | ✅ ok | 1573 | $1529.47 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
