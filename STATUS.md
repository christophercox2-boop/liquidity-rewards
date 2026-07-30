# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-29 9:36 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$69.11/day estimated (ceiling, not promise — details below)

**Earned:** $1,321.41 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$0.32** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$16.14/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$13.56/day), `ewc-usgub-ga-2026-11-03-dem` (~$10.42/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$69.11/day (~$2.88/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `apdc-petehegseth-2026-12-31` | BUY | 16.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~97.7% of bid side (80,561 resting ≥ 5,000 ✓) ≈ $16.28/day (pool ÷ 3 markets) |
| `ewc-ref-fl-tax-2026-11-03-pass` | SELL | 46.0¢ | 4 | 0 | $25.00 | ✅ scoring — ~82.9% of ask side (12,744 resting ≥ 2,000 ✓) ≈ $10.36/day |
| `ewc-pres-bra-2026-10-04-roncai` | SELL | 18.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~73.9% of ask side (6,156 resting ≥ 2,000 ✓) ≈ $1.32/day (pool ÷ 7 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~70.4% of ask side (8,956 resting ≥ 5,000 ✓) ≈ $2.93/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 16.0¢ | 7 | 0 | $25.00 | ✅ scoring — ~58.2% of ask side (2,754 resting ≥ 2,000 ✓) ≈ $0.73/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 85.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~56.8% of bid side (5,550 resting ≥ 5,000 ✓) ≈ $2.37/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 17.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~56.7% of ask side (126,290 resting ≥ 5,000 ✓) ≈ $2.18/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 22.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~54.1% of ask side (240,514 resting ≥ 5,000 ✓) ≈ $2.08/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 13.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~53.1% of ask side (141,691 resting ≥ 5,000 ✓) ≈ $2.04/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 15.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~52.5% of ask side (141,688 resting ≥ 5,000 ✓) ≈ $2.02/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 11.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~48.1% of ask side (106,031 resting ≥ 5,000 ✓) ≈ $1.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 19.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~47.2% of ask side (141,655 resting ≥ 5,000 ✓) ≈ $1.81/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 2.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~42.9% of ask side (64,329 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 18.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~40.2% of ask side (8,569 resting ≥ 5,000 ✓) ≈ $1.67/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 19.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~34.5% of ask side (217,888 resting ≥ 5,000 ✓) ≈ $1.33/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~33.3% of bid side (200,602 resting ≥ 5,000 ✓) ≈ $1.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 18.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~31.5% of ask side (90,257 resting ≥ 5,000 ✓) ≈ $1.21/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 16.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~31.1% of ask side (126,295 resting ≥ 5,000 ✓) ≈ $1.19/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 75.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~29.1% of bid side (5,451 resting ≥ 5,000 ✓) ≈ $1.21/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 20.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~28.8% of ask side (108,595 resting ≥ 5,000 ✓) ≈ $1.11/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 18.0¢ | 11 | 0 | $100.00 | ✅ scoring — ~28.7% of ask side (7,407 resting ≥ 5,000 ✓) ≈ $1.20/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 20.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~28.6% of ask side (142,453 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 90.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~26.0% of bid side (5,646 resting ≥ 5,000 ✓) ≈ $1.09/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 15.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~25.4% of ask side (8,610 resting ≥ 5,000 ✓) ≈ $1.06/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 88.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~23.0% of bid side (5,671 resting ≥ 5,000 ✓) ≈ $0.96/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 19.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~21.6% of ask side (180,136 resting ≥ 5,000 ✓) ≈ $0.83/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 25.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~20.8% of ask side (8,372 resting ≥ 5,000 ✓) ≈ $0.87/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 19.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~18.4% of ask side (62,147 resting ≥ 2,000 ✓) ≈ $0.23/day (pool ÷ 10 markets) |
| `cranc-uspres28-12-31-2026-jonoss` | BUY | 14.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~17.7% of bid side (101,091 resting ≥ 5,000 ✓) ≈ $0.27/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 14.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~14.4% of ask side (103,954 resting ≥ 5,000 ✓) ≈ $0.56/day (pool ÷ 13 markets) |
| …and 258 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>apdc-petehegseth-2026-12-31</code> BUY 1 @ 16¢ → $16.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 0.7 |
|  | 12¢ | 6 | ×0.2^4 = 0.0 |
|  | 11¢ | 21 | ×0.2^5 = 0.0 |
|  | 8¢ | 83 | ×0.2^8 = 0.0 |
|  | 1¢ | 80,450 | ×0.2^15 = 0.0 |
| | | **Σ** | **0.7** |

`yours 0.7 / Σ 0.7 = 97.7%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 97.7% = $16.28/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-petehegseth-2026-07-31`
2. `apdc-petehegseth-2026-08-31`
3. `apdc-petehegseth-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ewc-ref-fl-tax-2026-11-03-pass</code> SELL 4 @ 46¢ → $10.36/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 4 (4 yours) | ×0.1^0 = 4.0 |
|  | 49¢ | 5 | ×0.1^3 = 0.0 |
|  | 50¢ | 8,220 | ×0.1^4 = 0.8 |
| | | **Σ** | **4.8** |

`yours 4.0 / Σ 4.8 = 82.9%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 82.9% = $10.36/day`  

</details>
<details><summary><code>ewc-pres-bra-2026-10-04-roncai</code> SELL 20 @ 18¢ → $1.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 27 (20 yours) | ×0.1^0 = 27.0 |
|  | 20¢ | 6 | ×0.1^2 = 0.1 |
|  | 30¢ | 2 | ×0.1^12 = 0.0 |
|  | 98¢ | 200 | ×0.1^80 = 0.0 |
|  | 99¢ | 5,921 | ×0.1^81 = 0.0 |
| | | **Σ** | **27.1** |

`yours 20.0 / Σ 27.1 = 73.9%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 73.9% = $1.32/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 10¢ → $2.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 71 (50 yours) | ×0.2^0 = 71.0 |
|  | 18¢ | 15 | ×0.2^8 = 0.0 |
|  | 19¢ | 50 | ×0.2^9 = 0.0 |
|  | 20¢ | 3 | ×0.2^10 = 0.0 |
|  | 23¢ | 1 | ×0.2^13 = 0.0 |
|  | 30¢ | 4 | ×0.2^20 = 0.0 |
|  | 48¢ | 35 | ×0.2^38 = 0.0 |
|  | 50¢ | 16 | ×0.2^40 = 0.0 |
|  | 99¢ | 8,761 | ×0.2^89 = 0.0 |
| | | **Σ** | **71.0** |

`yours 50.0 / Σ 71.0 = 70.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 70.4% = $2.93/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 7 @ 16¢ → $0.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 12 (7 yours) | ×0.1^0 = 12.0 |
|  | 18¢ | 2 | ×0.1^2 = 0.0 |
|  | 22¢ | 24 | ×0.1^6 = 0.0 |
|  | 31¢ | 5 | ×0.1^15 = 0.0 |
|  | 37¢ | 135 | ×0.1^21 = 0.0 |
|  | 42¢ | 1 | ×0.1^26 = 0.0 |
|  | 58¢ | 5 | ×0.1^42 = 0.0 |
|  | 99¢ | 2,570 | ×0.1^83 = 0.0 |
| | | **Σ** | **12.0** |

`yours 7.0 / Σ 12.0 = 58.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 58.2% = $0.73/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 50 @ 85¢ → $2.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 86 (50 yours) | ×0.2^0 = 86.0 |
|  | 84¢ | 10 | ×0.2^1 = 2.0 |
|  | 10¢ | 2 | ×0.2^75 = 0.0 |
|  | 5¢ | 2 | ×0.2^80 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^84 = 0.0 |
| | | **Σ** | **88.0** |

`yours 50.0 / Σ 88.0 = 56.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 56.8% = $2.37/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 17¢ → $2.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 87 (50 yours) | ×0.2^0 = 87.0 |
|  | 18¢ | 5 | ×0.2^1 = 1.0 |
|  | 19¢ | 3 | ×0.2^2 = 0.1 |
|  | 20¢ | 3 | ×0.2^3 = 0.0 |
|  | 30¢ | 4 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^33 = 0.0 |
|  | 98¢ | 1,769 | ×0.2^81 = 0.0 |
|  | 99¢ | 124,319 | ×0.2^82 = 0.0 |
| | | **Σ** | **88.1** |

`yours 50.0 / Σ 88.1 = 56.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 56.7% = $2.18/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 18 @ 22¢ → $2.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 33 (18 yours) | ×0.2^0 = 32.6 |
|  | 30¢ | 4 | ×0.2^8 = 0.0 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 98¢ | 1,741 | ×0.2^76 = 0.0 |
|  | 99¢ | 238,637 | ×0.2^77 = 0.0 |
| | | **Σ** | **32.7** |

`yours 17.6 / Σ 32.7 = 54.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 54.1% = $2.08/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 50 @ 15¢ → $2.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 95 (50 yours) | ×0.2^0 = 95.2 |
|  | 20¢ | 3 | ×0.2^5 = 0.0 |
|  | 30¢ | 4 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 131,484 | ×0.2^83 = 0.0 |
| | | **Σ** | **95.2** |

`yours 50.0 / Σ 95.2 = 52.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 52.5% = $2.02/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 50 @ 11¢ → $1.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 104 (50 yours) | ×0.2^0 = 104.0 |
|  | 15¢ | 1 | ×0.2^4 = 0.0 |
|  | 16¢ | 5 | ×0.2^5 = 0.0 |
|  | 20¢ | 3 | ×0.2^9 = 0.0 |
|  | 30¢ | 4 | ×0.2^19 = 0.0 |
|  | 50¢ | 100 | ×0.2^39 = 0.0 |
|  | 97¢ | 53,855 | ×0.2^86 = 0.0 |
| | | **Σ** | **104.0** |

`yours 50.0 / Σ 104.0 = 48.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.1% = $1.85/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 100 @ 2¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 233 (100 yours) | ×0.1^0 = 233.0 |
|  | 8¢ | 1 | ×0.1^6 = 0.0 |
|  | 12¢ | 6 | ×0.1^10 = 0.0 |
|  | 13¢ | 18 | ×0.1^11 = 0.0 |
|  | 20¢ | 3 | ×0.1^18 = 0.0 |
|  | 30¢ | 2 | ×0.1^28 = 0.0 |
|  | 45¢ | 25 | ×0.1^43 = 0.0 |
|  | 98¢ | 61,041 | ×0.1^96 = 0.0 |
| | | **Σ** | **233.0** |

`yours 100.0 / Σ 233.0 = 42.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 42.9% = $0.54/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 50 @ 18¢ → $1.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 122 (50 yours) | ×0.2^0 = 122.0 |
|  | 20¢ | 60 | ×0.2^2 = 2.4 |
|  | 21¢ | 4 | ×0.2^3 = 0.0 |
|  | 22¢ | 1 | ×0.2^4 = 0.0 |
|  | 23¢ | 3 | ×0.2^5 = 0.0 |
|  | 30¢ | 4 | ×0.2^12 = 0.0 |
|  | 50¢ | 25 | ×0.2^32 = 0.0 |
|  | 99¢ | 8,350 | ×0.2^81 = 0.0 |
| | | **Σ** | **124.4** |

`yours 50.0 / Σ 124.4 = 40.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 40.2% = $1.67/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 30 @ 19¢ → $1.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 87 (30 yours) | ×0.2^0 = 87.0 |
|  | 30¢ | 4 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 98¢ | 131,484 | ×0.2^79 = 0.0 |
| | | **Σ** | **87.0** |

`yours 30.0 / Σ 87.0 = 34.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.5% = $1.33/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 30 @ 18¢ → $1.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 95 (30 yours) | ×0.2^0 = 95.0 |
|  | 20¢ | 7 | ×0.2^2 = 0.3 |
|  | 30¢ | 4 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 97¢ | 40,555 | ×0.2^79 = 0.0 |
| | | **Σ** | **95.3** |

`yours 30.0 / Σ 95.3 = 31.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.5% = $1.21/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 50 @ 16¢ → $1.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 161 (50 yours) | ×0.2^0 = 161.0 |
|  | 20¢ | 3 | ×0.2^4 = 0.0 |
|  | 30¢ | 4 | ×0.2^14 = 0.0 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 97¢ | 115,026 | ×0.2^81 = 0.0 |
| | | **Σ** | **161.0** |

`yours 50.0 / Σ 161.0 = 31.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.1% = $1.19/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 50 @ 75¢ → $1.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 172 (50 yours) | ×0.2^0 = 172.0 |
|  | 69¢ | 53 | ×0.2^6 = 0.0 |
|  | 47¢ | 22 | ×0.2^28 = 0.0 |
|  | 10¢ | 2 | ×0.2^65 = 0.0 |
|  | 5¢ | 2 | ×0.2^70 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^74 = 0.0 |
| | | **Σ** | **172.0** |

`yours 50.0 / Σ 172.0 = 29.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 29.1% = $1.21/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 30 @ 20¢ → $1.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 104 (30 yours) | ×0.2^0 = 104.0 |
|  | 30¢ | 4 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 97¢ | 53,892 | ×0.2^77 = 0.0 |
| | | **Σ** | **104.0** |

`yours 30.0 / Σ 104.0 = 28.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.8% = $1.11/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 11 @ 18¢ → $1.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 38 (11 yours) | ×0.2^0 = 38.0 |
|  | 20¢ | 7 | ×0.2^2 = 0.3 |
|  | 23¢ | 2 | ×0.2^5 = 0.0 |
|  | 30¢ | 4 | ×0.2^12 = 0.0 |
|  | 50¢ | 25 | ×0.2^32 = 0.0 |
|  | 99¢ | 7,331 | ×0.2^81 = 0.0 |
| | | **Σ** | **38.3** |

`yours 11.0 / Σ 38.3 = 28.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 28.7% = $1.20/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 20 @ 20¢ → $1.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 70 (20 yours) | ×0.2^0 = 70.0 |
|  | 30¢ | 4 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 97¢ | 92,783 | ×0.2^77 = 0.0 |
| | | **Σ** | **70.0** |

`yours 20.0 / Σ 70.0 = 28.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.6% = $1.10/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 50 @ 90¢ → $1.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 192 (50 yours) | ×0.2^0 = 192.0 |
|  | 10¢ | 2 | ×0.2^80 = 0.0 |
|  | 5¢ | 2 | ×0.2^85 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^89 = 0.0 |
| | | **Σ** | **192.0** |

`yours 50.0 / Σ 192.0 = 26.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 26.0% = $1.09/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 50 @ 15¢ → $1.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 25 | ×0.2^0 = 25.0 |
| ▶ | 15¢ | 72 (50 yours) | ×0.2^1 = 14.4 |
|  | 20¢ | 7 | ×0.2^6 = 0.0 |
|  | 21¢ | 2 | ×0.2^7 = 0.0 |
|  | 22¢ | 1 | ×0.2^8 = 0.0 |
|  | 23¢ | 1 | ×0.2^9 = 0.0 |
|  | 30¢ | 4 | ×0.2^16 = 0.0 |
|  | 50¢ | 25 | ×0.2^36 = 0.0 |
|  | 99¢ | 8,473 | ×0.2^85 = 0.0 |
| | | **Σ** | **39.4** |

`yours 10.0 / Σ 39.4 = 25.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 25.4% = $1.06/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 50 @ 88¢ → $0.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 217 (50 yours) | ×0.2^0 = 217.0 |
|  | 10¢ | 2 | ×0.2^78 = 0.0 |
|  | 5¢ | 2 | ×0.2^83 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^87 = 0.0 |
| | | **Σ** | **217.0** |

`yours 50.0 / Σ 217.0 = 23.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 23.0% = $0.96/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 10 @ 19¢ → $0.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 45 (10 yours) | ×0.2^0 = 45.0 |
|  | 20¢ | 7 | ×0.2^1 = 1.4 |
|  | 30¢ | 4 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 98¢ | 169,979 | ×0.2^79 = 0.0 |
| | | **Σ** | **46.4** |

`yours 10.0 / Σ 46.4 = 21.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 21.6% = $0.83/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 25¢ → $0.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 48 (10 yours) | ×0.2^0 = 48.0 |
|  | 28¢ | 2 | ×0.2^3 = 0.0 |
|  | 30¢ | 1 | ×0.2^5 = 0.0 |
|  | 32¢ | 3 | ×0.2^7 = 0.0 |
|  | 33¢ | 3 | ×0.2^8 = 0.0 |
|  | 99¢ | 8,315 | ×0.2^74 = 0.0 |
| | | **Σ** | **48.0** |

`yours 10.0 / Σ 48.0 = 20.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 20.8% = $0.87/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 30 @ 19¢ → $0.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 163 (30 yours) | ×0.1^0 = 163.0 |
|  | 21¢ | 5 | ×0.1^2 = 0.1 |
|  | 25¢ | 6 | ×0.1^6 = 0.0 |
|  | 26¢ | 18 | ×0.1^7 = 0.0 |
|  | 45¢ | 231 | ×0.1^26 = 0.0 |
|  | 98¢ | 61,224 | ×0.1^79 = 0.0 |
| | | **Σ** | **163.1** |

`yours 30.0 / Σ 163.1 = 18.4%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 18.4% = $0.23/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-jonoss</code> BUY 17 @ 14¢ → $0.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 88 (17 yours) | ×0.2^0 = 88.0 |
|  | 12¢ | 100 | ×0.2^2 = 4.0 |
|  | 11¢ | 503 | ×0.2^3 = 4.0 |
|  | 8¢ | 198 | ×0.2^6 = 0.0 |
|  | 5¢ | 2 | ×0.2^9 = 0.0 |
|  | 1¢ | 100,200 | ×0.2^13 = 0.0 |
| | | **Σ** | **96.0** |

`yours 17.0 / Σ 96.0 = 17.7%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 17.7% = $0.27/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru`
7. `cranc-uspres28-12-31-2026-dontrujr`
8. `cranc-uspres28-12-31-2026-dwajoh`
9. `cranc-uspres28-12-31-2026-elomus`
10. `cranc-uspres28-12-31-2026-erikir`
11. `cranc-uspres28-12-31-2026-gavnew`
12. `cranc-uspres28-12-31-2026-hilcli`
13. `cranc-uspres28-12-31-2026-hunbid`
14. `cranc-uspres28-12-31-2026-jdvan`
15. `cranc-uspres28-12-31-2026-jonoss` ← this one
16. `cranc-uspres28-12-31-2026-jossha`
17. `cranc-uspres28-12-31-2026-kamhar`
18. `cranc-uspres28-12-31-2026-krinoe`
19. `cranc-uspres28-12-31-2026-margre`
20. `cranc-uspres28-12-31-2026-markel`
21. `cranc-uspres28-12-31-2026-marrub`
22. `cranc-uspres28-12-31-2026-micoba`
23. `cranc-uspres28-12-31-2026-nikhal`
24. `cranc-uspres28-12-31-2026-oprwin`
25. `cranc-uspres28-12-31-2026-petbut`
26. `cranc-uspres28-12-31-2026-rahema`
27. `cranc-uspres28-12-31-2026-robken`
28. `cranc-uspres28-12-31-2026-steban`
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 40 @ 14¢ → $0.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 235 (40 yours) | ×0.2^0 = 235.0 |
|  | 15¢ | 211 | ×0.2^1 = 42.2 |
|  | 21¢ | 18 | ×0.2^7 = 0.0 |
|  | 30¢ | 2 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^36 = 0.0 |
|  | 97¢ | 53,892 | ×0.2^83 = 0.0 |
| | | **Σ** | **277.2** |

`yours 40.0 / Σ 277.2 = 14.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.4% = $0.56/day`  

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

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-29 | ~$66.11 | $0.32 | 0% |
| 2026-07-28 | ~$148.78 | $79.65 | 54% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |

Biggest gaps on 2026-07-29: `apdc-petehegseth-2026-12-31` (est ~$13.48 → got $0.00), `scc-senate-gop-2026-11-03-51` (est ~$3.24 → got $0.00), `scc-senate-gop-2026-11-03-48` (est ~$2.35 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (25,289 resting) | ~96.8% | ~$16.14 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (91,704 resting) | ~54.2% | ~$13.56 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (88,679 resting) | ~13.9% | ~$10.42 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (86,369 resting) | ~13.6% | ~$10.23 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (98,770 resting) | ~19.4% | ~$4.85 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (103,864 resting) | ~5.6% | ~$4.21 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (46,880 resting) | ~16.0% | ~$4.01 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (175,034 resting) | ~4.5% | ~$3.36 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (282,568 resting) | ~4.3% | ~$3.20 |
| `apdc-jerpowgov-2026-07-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (5,765 resting) | ~11.3% | ~$1.89 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,484 resting) | ~5.7% | ~$1.42 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (195,041 resting) | ~1.9% | ~$1.40 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,240.74 |
| Pending | $79.46 |
| Skipped | $1.21 |
| **Total earned** | **$1,321.41** |

1267 reward rows · 27 days with rewards · 352 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-29 | $0.32 | `█` |
| 2026-07-28 | $79.65 | `███████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,321.41 | `████████████████████` |

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
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.70 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.21 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.64 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `vmc-ussep-misen-2026-08-04-els15-20` | $22.78 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-29 9:36 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:19 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:18 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:09 PM ET | ✅ ok | 1256 | $1321.25 |
| 2026-07-29 9:06 PM ET | ✅ ok | 1230 | $1290.27 |
| 2026-07-29 8:14 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 7:17 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 6:15 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 5:14 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 3:47 PM ET | ✅ ok | 1063 | $1241.95 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
