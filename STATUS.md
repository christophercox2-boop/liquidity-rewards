# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-29 9:06 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$88.31/day estimated (ceiling, not promise — details below)

**Earned:** $1,290.27 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-28: **$48.83** · 2026-07-27: **$125.34** · 2026-07-26: **$153.80** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$16.16/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$14.85/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$13.56/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$88.31/day (~$3.68/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 85.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (5,543 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 90.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (5,292 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 16.0¢ | 7 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (2,748 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `ewc-pres-bra-2026-10-04-roncai` | SELL | 18.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (6,146 resting ≥ 2,000 ✓) ≈ $1.78/day (pool ÷ 7 markets) |
| `apdc-petehegseth-2026-12-31` | BUY | 16.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~98.6% of bid side (80,543 resting ≥ 5,000 ✓) ≈ $16.44/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 22.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~88.0% of ask side (240,507 resting ≥ 5,000 ✓) ≈ $3.38/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~81.9% of ask side (8,966 resting ≥ 5,000 ✓) ≈ $3.41/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 17.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~79.2% of ask side (125,496 resting ≥ 5,000 ✓) ≈ $3.05/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 15.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~78.3% of ask side (126,664 resting ≥ 5,000 ✓) ≈ $3.01/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 58.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~77.5% of ask side (5,134 resting ≥ 5,000 ✓) ≈ $3.23/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 19.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~66.6% of ask side (61,951 resting ≥ 2,000 ✓) ≈ $0.83/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 18.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~61.1% of ask side (90,207 resting ≥ 5,000 ✓) ≈ $2.35/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 85.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~60.2% of bid side (5,545 resting ≥ 5,000 ✓) ≈ $2.51/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 11.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~57.5% of ask side (106,014 resting ≥ 5,000 ✓) ≈ $2.21/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 62.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~54.9% of bid side (5,591 resting ≥ 5,000 ✓) ≈ $2.29/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 18.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~54.4% of ask side (8,501 resting ≥ 5,000 ✓) ≈ $2.27/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 13.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~53.1% of ask side (144,191 resting ≥ 5,000 ✓) ≈ $2.04/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 88.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~52.6% of bid side (5,549 resting ≥ 5,000 ✓) ≈ $2.19/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 19.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~49.2% of ask side (217,862 resting ≥ 5,000 ✓) ≈ $1.89/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 19.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~47.2% of ask side (141,655 resting ≥ 5,000 ✓) ≈ $1.81/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 20.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~44.8% of ask side (108,558 resting ≥ 5,000 ✓) ≈ $1.72/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 2.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~44.4% of ask side (64,321 resting ≥ 2,000 ✓) ≈ $0.56/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 17.0¢ | 60 | 0 | $100.00 | ✅ scoring — ~39.7% of bid side (200,605 resting ≥ 5,000 ✓) ≈ $1.53/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 20.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~38.5% of ask side (142,435 resting ≥ 5,000 ✓) ≈ $1.48/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 15.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~38.5% of ask side (8,579 resting ≥ 5,000 ✓) ≈ $1.60/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | BUY | 14.0¢ | 100 | 1 | $25.00 | ✅ scoring — ~37.0% of bid side (5,386 resting ≥ 2,000 ✓) ≈ $0.46/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~33.3% of bid side (200,602 resting ≥ 5,000 ✓) ≈ $1.28/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 18.0¢ | 11 | 0 | $100.00 | ✅ scoring — ~33.2% of ask side (7,881 resting ≥ 5,000 ✓) ≈ $1.38/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 25.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~32.2% of ask side (8,355 resting ≥ 5,000 ✓) ≈ $1.34/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 19.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~31.6% of ask side (180,119 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 13 markets) |
| …and 251 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 50 @ 85¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 67¢ | 38 | ×0.2^18 = 0.0 |
|  | 47¢ | 1 | ×0.2^38 = 0.0 |
|  | 10¢ | 2 | ×0.2^75 = 0.0 |
|  | 5¢ | 2 | ×0.2^80 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^84 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 50 @ 90¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 76¢ | 38 | ×0.2^14 = 0.0 |
|  | 10¢ | 2 | ×0.2^80 = 0.0 |
|  | 5¢ | 2 | ×0.2^85 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^89 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 7 @ 16¢ → $1.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 7 (7 yours) | ×0.1^0 = 7.0 |
|  | 18¢ | 1 | ×0.1^2 = 0.0 |
|  | 22¢ | 6 | ×0.1^6 = 0.0 |
|  | 23¢ | 18 | ×0.1^7 = 0.0 |
|  | 31¢ | 5 | ×0.1^15 = 0.0 |
|  | 37¢ | 135 | ×0.1^21 = 0.0 |
|  | 42¢ | 1 | ×0.1^26 = 0.0 |
|  | 58¢ | 5 | ×0.1^42 = 0.0 |
|  | 99¢ | 2,570 | ×0.1^83 = 0.0 |
| | | **Σ** | **7.0** |

`yours 7.0 / Σ 7.0 = 99.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 99.9% = $1.25/day`  

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
<details><summary><code>ewc-pres-bra-2026-10-04-roncai</code> SELL 20 @ 18¢ → $1.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 20 (20 yours) | ×0.1^0 = 20.0 |
|  | 20¢ | 3 | ×0.1^2 = 0.0 |
|  | 30¢ | 2 | ×0.1^12 = 0.0 |
|  | 98¢ | 200 | ×0.1^80 = 0.0 |
|  | 99¢ | 5,921 | ×0.1^81 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 99.9%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 99.9% = $1.78/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `ewc-pres-bra-2026-10-04-camsan`
2. `ewc-pres-bra-2026-10-04-ferhad`
3. `ewc-pres-bra-2026-10-04-flabol`
4. `ewc-pres-bra-2026-10-04-luisil`
5. `ewc-pres-bra-2026-10-04-rensan`
6. `ewc-pres-bra-2026-10-04-romzem`
7. `ewc-pres-bra-2026-10-04-roncai` ← this one

</details>

</details>
<details><summary><code>apdc-petehegseth-2026-12-31</code> BUY 1 @ 16¢ → $16.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 0.7 |
|  | 12¢ | 6 | ×0.2^4 = 0.0 |
|  | 9¢ | 3 | ×0.2^7 = 0.0 |
|  | 8¢ | 83 | ×0.2^8 = 0.0 |
|  | 1¢ | 80,450 | ×0.2^15 = 0.0 |
| | | **Σ** | **0.7** |

`yours 0.7 / Σ 0.7 = 98.6%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 98.6% = $16.44/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-petehegseth-2026-07-31`
2. `apdc-petehegseth-2026-08-31`
3. `apdc-petehegseth-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 22 @ 22¢ → $3.38/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 25 (22 yours) | ×0.2^0 = 25.0 |
|  | 30¢ | 4 | ×0.2^8 = 0.0 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 98¢ | 1,741 | ×0.2^76 = 0.0 |
|  | 99¢ | 238,637 | ×0.2^77 = 0.0 |
| | | **Σ** | **25.0** |

`yours 22.0 / Σ 25.0 = 88.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.0% = $3.38/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 10¢ → $3.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 61 (50 yours) | ×0.2^0 = 61.0 |
|  | 14¢ | 15 | ×0.2^4 = 0.0 |
|  | 15¢ | 20 | ×0.2^5 = 0.0 |
|  | 19¢ | 50 | ×0.2^9 = 0.0 |
|  | 20¢ | 3 | ×0.2^10 = 0.0 |
|  | 23¢ | 1 | ×0.2^13 = 0.0 |
|  | 30¢ | 4 | ×0.2^20 = 0.0 |
|  | 48¢ | 35 | ×0.2^38 = 0.0 |
|  | 50¢ | 16 | ×0.2^40 = 0.0 |
|  | 99¢ | 8,761 | ×0.2^89 = 0.0 |
| | | **Σ** | **61.0** |

`yours 50.0 / Σ 61.0 = 81.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 81.9% = $3.41/day`  

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
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 17¢ → $3.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 62 (50 yours) | ×0.2^0 = 62.0 |
|  | 18¢ | 5 | ×0.2^1 = 1.0 |
|  | 19¢ | 3 | ×0.2^2 = 0.1 |
|  | 20¢ | 3 | ×0.2^3 = 0.0 |
|  | 30¢ | 4 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^33 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^81 = 0.0 |
|  | 99¢ | 124,319 | ×0.2^82 = 0.0 |
| | | **Σ** | **63.1** |

`yours 50.0 / Σ 63.1 = 79.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 79.2% = $3.05/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 50 @ 15¢ → $3.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 15¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 16¢ | 19 | ×0.2^2 = 0.8 |
|  | 20¢ | 3 | ×0.2^6 = 0.0 |
|  | 30¢ | 4 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^36 = 0.0 |
|  | 98¢ | 116,484 | ×0.2^84 = 0.0 |
| | | **Σ** | **12.8** |

`yours 10.0 / Σ 12.8 = 78.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 78.3% = $3.01/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 40 @ 58¢ → $3.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 50 (40 yours) | ×0.2^0 = 50.0 |
|  | 59¢ | 8 | ×0.2^1 = 1.6 |
|  | 99¢ | 5,076 | ×0.2^41 = 0.0 |
| | | **Σ** | **51.6** |

`yours 40.0 / Σ 51.6 = 77.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 77.5% = $3.23/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 30 @ 19¢ → $0.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 45 (30 yours) | ×0.1^0 = 45.0 |
|  | 21¢ | 2 | ×0.1^2 = 0.0 |
|  | 25¢ | 6 | ×0.1^6 = 0.0 |
|  | 26¢ | 18 | ×0.1^7 = 0.0 |
|  | 45¢ | 231 | ×0.1^26 = 0.0 |
|  | 98¢ | 61,149 | ×0.1^79 = 0.0 |
| | | **Σ** | **45.0** |

`yours 30.0 / Σ 45.0 = 66.6%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 66.6% = $0.83/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5` ← this one
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 30 @ 18¢ → $2.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 49 (30 yours) | ×0.2^0 = 49.0 |
|  | 20¢ | 3 | ×0.2^2 = 0.1 |
|  | 30¢ | 4 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 97¢ | 40,555 | ×0.2^79 = 0.0 |
| | | **Σ** | **49.1** |

`yours 30.0 / Σ 49.1 = 61.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 61.1% = $2.35/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 50 @ 85¢ → $2.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 81 (50 yours) | ×0.2^0 = 81.0 |
|  | 84¢ | 10 | ×0.2^1 = 2.0 |
|  | 10¢ | 2 | ×0.2^75 = 0.0 |
|  | 5¢ | 2 | ×0.2^80 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^84 = 0.0 |
| | | **Σ** | **83.0** |

`yours 50.0 / Σ 83.0 = 60.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 60.2% = $2.51/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 50 @ 11¢ → $2.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 87 (50 yours) | ×0.2^0 = 87.0 |
|  | 15¢ | 1 | ×0.2^4 = 0.0 |
|  | 16¢ | 5 | ×0.2^5 = 0.0 |
|  | 20¢ | 3 | ×0.2^9 = 0.0 |
|  | 30¢ | 4 | ×0.2^19 = 0.0 |
|  | 50¢ | 100 | ×0.2^39 = 0.0 |
|  | 97¢ | 53,855 | ×0.2^86 = 0.0 |
| | | **Σ** | **87.0** |

`yours 50.0 / Σ 87.0 = 57.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 57.5% = $2.21/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 50 @ 62¢ → $2.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 62¢ | 91 (50 yours) | ×0.2^0 = 91.0 |
|  | 10¢ | 2 | ×0.2^52 = 0.0 |
|  | 5¢ | 2 | ×0.2^57 = 0.0 |
|  | 1¢ | 5,496 | ×0.2^61 = 0.0 |
| | | **Σ** | **91.0** |

`yours 50.0 / Σ 91.0 = 54.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 54.9% = $2.29/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 50 @ 18¢ → $2.27/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 91 (50 yours) | ×0.2^0 = 91.0 |
|  | 20¢ | 23 | ×0.2^2 = 0.9 |
|  | 21¢ | 4 | ×0.2^3 = 0.0 |
|  | 22¢ | 1 | ×0.2^4 = 0.0 |
|  | 23¢ | 3 | ×0.2^5 = 0.0 |
|  | 30¢ | 4 | ×0.2^12 = 0.0 |
|  | 50¢ | 25 | ×0.2^32 = 0.0 |
|  | 99¢ | 8,350 | ×0.2^81 = 0.0 |
| | | **Σ** | **92.0** |

`yours 50.0 / Σ 92.0 = 54.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 54.4% = $2.27/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 50 @ 13¢ → $2.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 93 (50 yours) | ×0.2^0 = 93.0 |
|  | 14¢ | 6 | ×0.2^1 = 1.2 |
|  | 20¢ | 3 | ×0.2^7 = 0.0 |
|  | 30¢ | 4 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^37 = 0.0 |
|  | 98¢ | 131,484 | ×0.2^85 = 0.0 |
| | | **Σ** | **94.2** |

`yours 50.0 / Σ 94.2 = 53.1%`  
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
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56` ← this one
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 50 @ 88¢ → $2.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 95 (50 yours) | ×0.2^0 = 95.0 |
|  | 10¢ | 2 | ×0.2^78 = 0.0 |
|  | 5¢ | 2 | ×0.2^83 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^87 = 0.0 |
| | | **Σ** | **95.0** |

`yours 50.0 / Σ 95.0 = 52.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 52.6% = $2.19/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 30 @ 19¢ → $1.89/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 61 (30 yours) | ×0.2^0 = 61.0 |
|  | 30¢ | 4 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 98¢ | 131,484 | ×0.2^79 = 0.0 |
| | | **Σ** | **61.0** |

`yours 30.0 / Σ 61.0 = 49.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 49.2% = $1.89/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 30 @ 19¢ → $1.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 63 (30 yours) | ×0.2^0 = 63.0 |
|  | 20¢ | 3 | ×0.2^1 = 0.6 |
|  | 30¢ | 4 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 98¢ | 131,484 | ×0.2^79 = 0.0 |
| | | **Σ** | **63.6** |

`yours 30.0 / Σ 63.6 = 47.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.2% = $1.81/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 30 @ 20¢ → $1.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 67 (30 yours) | ×0.2^0 = 67.0 |
|  | 30¢ | 4 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 97¢ | 53,892 | ×0.2^77 = 0.0 |
| | | **Σ** | **67.0** |

`yours 30.0 / Σ 67.0 = 44.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 44.8% = $1.72/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 100 @ 2¢ → $0.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 225 (100 yours) | ×0.1^0 = 225.0 |
|  | 8¢ | 1 | ×0.1^6 = 0.0 |
|  | 12¢ | 6 | ×0.1^10 = 0.0 |
|  | 13¢ | 18 | ×0.1^11 = 0.0 |
|  | 20¢ | 3 | ×0.1^18 = 0.0 |
|  | 30¢ | 2 | ×0.1^28 = 0.0 |
|  | 45¢ | 25 | ×0.1^43 = 0.0 |
|  | 98¢ | 61,041 | ×0.1^96 = 0.0 |
| | | **Σ** | **225.0** |

`yours 100.0 / Σ 225.0 = 44.4%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 44.4% = $0.56/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 60 @ 17¢ → $1.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 151 (60 yours) | ×0.2^0 = 151.0 |
|  | 15¢ | 2 | ×0.2^2 = 0.1 |
|  | 5¢ | 2 | ×0.2^12 = 0.0 |
|  | 3¢ | 200,250 | ×0.2^14 = 0.0 |
| | | **Σ** | **151.1** |

`yours 60.0 / Σ 151.1 = 39.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 39.7% = $1.53/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 20 @ 20¢ → $1.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 52 (20 yours) | ×0.2^0 = 52.0 |
|  | 30¢ | 4 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 97¢ | 92,783 | ×0.2^77 = 0.0 |
| | | **Σ** | **52.0** |

`yours 20.0 / Σ 52.0 = 38.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.5% = $1.48/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 50 @ 15¢ → $1.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 16 | ×0.2^0 = 16.0 |
| ▶ | 15¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 20¢ | 7 | ×0.2^6 = 0.0 |
|  | 21¢ | 2 | ×0.2^7 = 0.0 |
|  | 22¢ | 1 | ×0.2^8 = 0.0 |
|  | 23¢ | 1 | ×0.2^9 = 0.0 |
|  | 30¢ | 4 | ×0.2^16 = 0.0 |
|  | 50¢ | 25 | ×0.2^36 = 0.0 |
|  | 99¢ | 8,473 | ×0.2^85 = 0.0 |
| | | **Σ** | **26.0** |

`yours 10.0 / Σ 26.0 = 38.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 38.5% = $1.60/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> BUY 100 @ 14¢ → $0.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 15¢ | 17 | ×0.1^0 = 17.0 |
| ▶ | 14¢ | 100 (100 yours) | ×0.1^1 = 10.0 |
|  | 7¢ | 18 | ×0.1^8 = 0.0 |
|  | 5¢ | 1 | ×0.1^10 = 0.0 |
|  | 1¢ | 5,250 | ×0.1^14 = 0.0 |
| | | **Σ** | **27.0** |

`yours 10.0 / Σ 27.0 = 37.0%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 37.0% = $0.46/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 50 @ 20¢ → $1.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 150 (50 yours) | ×0.2^0 = 150.0 |
|  | 5¢ | 2 | ×0.2^15 = 0.0 |
|  | 3¢ | 200,250 | ×0.2^17 = 0.0 |
| | | **Σ** | **150.0** |

`yours 50.0 / Σ 150.0 = 33.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.3% = $1.28/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 11 @ 18¢ → $1.38/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 33 (11 yours) | ×0.2^0 = 33.0 |
|  | 20¢ | 3 | ×0.2^2 = 0.1 |
|  | 23¢ | 2 | ×0.2^5 = 0.0 |
|  | 30¢ | 4 | ×0.2^12 = 0.0 |
|  | 50¢ | 25 | ×0.2^32 = 0.0 |
|  | 99¢ | 7,814 | ×0.2^81 = 0.0 |
| | | **Σ** | **33.1** |

`yours 11.0 / Σ 33.1 = 33.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 33.2% = $1.38/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 25¢ → $1.34/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 31 (10 yours) | ×0.2^0 = 31.0 |
|  | 28¢ | 2 | ×0.2^3 = 0.0 |
|  | 30¢ | 1 | ×0.2^5 = 0.0 |
|  | 32¢ | 3 | ×0.2^7 = 0.0 |
|  | 33¢ | 3 | ×0.2^8 = 0.0 |
|  | 99¢ | 8,315 | ×0.2^74 = 0.0 |
| | | **Σ** | **31.0** |

`yours 10.0 / Σ 31.0 = 32.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 32.2% = $1.34/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 10 @ 19¢ → $1.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 31 (10 yours) | ×0.2^0 = 31.0 |
|  | 20¢ | 3 | ×0.2^1 = 0.6 |
|  | 22¢ | 1 | ×0.2^3 = 0.0 |
|  | 30¢ | 4 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 98¢ | 169,979 | ×0.2^79 = 0.0 |
| | | **Σ** | **31.6** |

`yours 10.0 / Σ 31.6 = 31.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.6% = $1.22/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-28 | ~$148.78 | $48.83 | 33% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |
| 2026-07-26 | ~$159.09 | $153.80 | 97% |

Biggest gaps on 2026-07-28: `enwc-ussep-mi-2026-08-04-dem-abdels` (est ~$18.10 → got $9.25), `lawec-saveact-2026-12-31` (est ~$9.15 → got $1.86), `stsc-bab-el-mandeb-clsd-2026-12-31` (est ~$5.96 → got $0.20)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (25,288 resting) | ~96.9% | ~$16.16 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,250 resting) | ~19.8% | ~$14.85 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (91,704 resting) | ~54.2% | ~$13.56 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (88,729 resting) | ~13.8% | ~$10.35 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (98,136 resting) | ~26.3% | ~$6.57 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (53,999 resting) | ~24.3% | ~$6.08 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (103,864 resting) | ~5.6% | ~$4.21 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (282,641 resting) | ~4.2% | ~$3.17 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (175,913 resting) | ~4.0% | ~$3.03 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (8,230 resting) | ~9.9% | ~$2.48 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (102,924 resting) | ~2.8% | ~$2.11 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (87,505 resting) | ~2.7% | ~$2.05 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,240.74 |
| Pending | $48.32 |
| Skipped | $1.21 |
| **Total earned** | **$1,290.27** |

1230 reward rows · 26 days with rewards · 337 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-28 | $48.83 | `████` |
| 2026-07-27 | $125.34 | `███████████` |
| 2026-07-26 | $153.80 | `██████████████` |
| 2026-07-25 | $125.69 | `███████████` |
| 2026-07-24 | $135.19 | `████████████` |
| 2026-07-23 | $227.63 | `████████████████████` |
| 2026-07-22 | $82.95 | `███████` |
| 2026-07-21 | $91.44 | `████████` |
| 2026-07-20 | $106.54 | `█████████` |
| 2026-07-19 | $35.81 | `███` |
| 2026-07-18 | $44.41 | `████` |
| 2026-07-17 | $14.71 | `█` |
| 2026-07-16 | $17.02 | `█` |
| 2026-07-15 | $1.53 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,290.27 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.23 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.22 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.75 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.47 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.45 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.21 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.15 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `vmc-ussep-misen-2026-08-04-els15-20` | $22.78 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-29 9:06 PM ET | ✅ ok | 1230 | $1290.27 |
| 2026-07-29 8:14 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 7:17 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 6:15 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 5:14 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 3:47 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 2:16 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 1:22 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 12:42 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 11:22 AM ET | ✅ ok | 1063 | $1241.95 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
