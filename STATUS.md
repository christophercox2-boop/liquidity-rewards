# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-20 8:29 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$170.31/day estimated (ceiling, not promise — details below)

**Earned:** $157.05 lifetime ($78.17 paid). Last three recorded days — 2026-07-18: **$44.41** · 2026-07-17: **$14.71** · 2026-07-16: **$17.02** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — SELL at the best price, ~$30.24/day for 200 contracts. Runners-up: `ewc-usgub-ks-2026-11-03-rep` (~$12.59/day), `enwc-usgubp-sd-2026-06-02-rep-tobdoe` (~$10.72/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$170.31/day (~$7.10/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-nh-2026-09-08-dem-karman` | BUY | 8.0¢ | 44 | 0 | $250.00 | ✅ scoring — ~89.5% of bid side (23,669 resting ≥ 10,000 ✓) ≈ $55.93/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 89.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~43.3% of bid side (11,123 resting ≥ 10,000 ✓) ≈ $27.05/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 8.0¢ | 30 | 0 | $250.00 | ✅ scoring — ~37.0% of ask side (11,999 resting ≥ 10,000 ✓) ≈ $23.15/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 1.0¢ | 10,000 | 5 | $250.00 | ✅ scoring — ~30.9% of bid side (20,649 resting ≥ 10,000 ✓) ≈ $6.43/day (pool ÷ 6 markets) |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 12.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~29.9% of ask side (10,797 resting ≥ 10,000 ✓) ≈ $18.70/day (pool ÷ 2 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 48.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~17.2% of ask side (13,604 resting ≥ 10,000 ✓) ≈ $2.16/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 22.0¢ | 30 | 1 | $250.00 | ✅ scoring — ~15.0% of bid side (11,054 resting ≥ 10,000 ✓) ≈ $3.12/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 46.0¢ | 60 | 0 | $250.00 | ✅ scoring — ~14.8% of ask side (11,161 resting ≥ 10,000 ✓) ≈ $1.86/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 48.0¢ | 60 | 0 | $250.00 | ✅ scoring — ~14.6% of ask side (11,000 resting ≥ 10,000 ✓) ≈ $1.83/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 91.0¢ | 30 | 0 | $250.00 | ✅ scoring — ~12.5% of bid side (11,002 resting ≥ 10,000 ✓) ≈ $7.79/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | SELL | 28.0¢ | 10 | 1 | $250.00 | ✅ scoring — ~11.3% of ask side (11,049 resting ≥ 10,000 ✓) ≈ $2.35/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 47.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~9.6% of ask side (11,000 resting ≥ 10,000 ✓) ≈ $1.19/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 47.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~8.1% of ask side (11,184 resting ≥ 10,000 ✓) ≈ $1.02/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | SELL | 47.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~8.1% of ask side (11,184 resting ≥ 10,000 ✓) ≈ $1.02/day (pool ÷ 10 markets) |
| `enwc-ussep-mi-2026-08-04-dem-halste` | BUY | 33.0¢ | 200 | 0 | $250.00 | ✅ scoring — ~7.9% of bid side (77,192 resting ≥ 10,000 ✓) ≈ $3.30/day (pool ÷ 3 markets) |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | SELL | 99.0¢ | 10,000 | 7 | $250.00 | ✅ scoring — ~6.0% of ask side (30,586 resting ≥ 10,000 ✓) ≈ $3.75/day (pool ÷ 2 markets) |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | BUY | 16.0¢ | 200 | 1 | $250.00 | ✅ scoring — ~5.6% of bid side (26,682 resting ≥ 10,000 ✓) ≈ $3.52/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-08-dem-karman` | BUY | 1.0¢ | 10,000 | 7 | $250.00 | ✅ scoring — ~4.4% of bid side (23,669 resting ≥ 10,000 ✓) ≈ $2.78/day (pool ÷ 2 markets) |
| `ewc-usgub-ga-2026-11-03-dem` | BUY | 59.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~3.5% of bid side (91,334 resting ≥ 10,000 ✓) ≈ $2.20/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | SELL | 75.0¢ | 20 | 0 | $250.00 | ✅ scoring — ~2.3% of ask side (10,861 resting ≥ 10,000 ✓) ≈ $0.48/day (pool ÷ 6 markets) |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | BUY | 9.0¢ | 200 | 0 | $250.00 | ✅ scoring — ~0.9% of bid side (22,983 resting ≥ 10,000 ✓) ≈ $0.55/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | SELL | 96.0¢ | 5 | 4 | $250.00 | ✅ scoring — ~0.1% of ask side (30,586 resting ≥ 10,000 ✓) ≈ $0.07/day (pool ÷ 2 markets) |
| `ewc-usgub-ca-2026-11-03-xavbec` | BUY | 93.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~0.1% of bid side (110,684 resting ≥ 10,000 ✓) ≈ $0.06/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | SELL | 99.0¢ | 10,000 | 24 | $250.00 | ✅ scoring — ~0.0% of ask side (10,861 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 99.0¢ | 2,500 | 51 | $250.00 | ✅ scoring — ~0.0% of ask side (13,604 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 1.0¢ | 10,000 | 90 | $250.00 | ✅ scoring — ~0.0% of bid side (11,002 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 99.0¢ | 10,000 | 91 | $250.00 | ✅ scoring — ~0.0% of ask side (11,999 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 2 markets) |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-nh-2026-09-08-dem-karman</code> BUY 44 @ 8¢ → $55.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 44 (44 yours) | ×0.3^0 = 44.0 |
|  | 1¢ | 23,625 | ×0.3^7 = 5.2 |
| | | **Σ** | **49.2** |

`yours 44.0 / Σ 49.2 = 89.5%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 89.5% = $55.93/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap`
2. `enwc-ussep-nh-2026-09-08-dem-karman` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-chrpap</code> BUY 100 @ 89¢ → $27.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 90¢ | 18 | ×0.3^0 = 18.0 |
| ▶ | 89¢ | 100 (100 yours) | ×0.3^1 = 30.0 |
|  | 87¢ | 775 | ×0.3^3 = 20.9 |
|  | 84¢ | 525 | ×0.3^6 = 0.4 |
|  | 1¢ | 9,705 | ×0.3^89 = 0.0 |
| | | **Σ** | **69.3** |

`yours 30.0 / Σ 69.3 = 43.3%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 43.3% = $27.05/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap` ← this one
2. `enwc-ussep-nh-2026-09-08-dem-karman`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 30 @ 8¢ → $23.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 81 (30 yours) | ×0.3^0 = 81.0 |
|  | 55¢ | 87 | ×0.3^47 = 0.0 |
|  | 98¢ | 830 | ×0.3^90 = 0.0 |
|  | 99¢ | 11,001 | ×0.3^91 = 0.0 |
| | | **Σ** | **81.0** |

`yours 30.0 / Σ 81.0 = 37.0%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 37.0% = $23.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun`
2. `enwc-ussep-nh-2026-09-01-rep-scobro` ← this one

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> BUY 10,000 @ 1¢ → $6.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 5 | ×0.3^0 = 5.0 |
|  | 5¢ | 78 | ×0.3^1 = 23.4 |
|  | 2¢ | 55 | ×0.3^4 = 0.4 |
| ▶ | 1¢ | 20,511 (10,000 yours) | ×0.3^5 = 49.8 |
| | | **Σ** | **78.7** |

`yours 24.3 / Σ 78.7 = 30.9%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 30.9% = $6.43/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-karman</code> SELL 100 @ 12¢ → $18.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 100 (100 yours) | ×0.3^0 = 100.0 |
|  | 13¢ | 774 | ×0.3^1 = 232.2 |
|  | 15¢ | 76 | ×0.3^3 = 2.1 |
|  | 99¢ | 9,847 | ×0.3^87 = 0.0 |
| | | **Σ** | **334.3** |

`yours 100.0 / Σ 334.3 = 29.9%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 29.9% = $18.70/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap`
2. `enwc-ussep-nh-2026-09-08-dem-karman` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> SELL 100 @ 48¢ → $2.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 580 (100 yours) | ×0.3^0 = 580.0 |
|  | 54¢ | 34 | ×0.3^6 = 0.0 |
|  | 55¢ | 87 | ×0.3^7 = 0.0 |
|  | 99¢ | 12,903 | ×0.3^51 = 0.0 |
| | | **Σ** | **580.0** |

`yours 100.0 / Σ 580.0 = 17.2%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 17.2% = $2.16/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 30 @ 22¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 15 | ×0.3^0 = 15.0 |
| ▶ | 22¢ | 89 (30 yours) | ×0.3^1 = 26.7 |
|  | 20¢ | 682 | ×0.3^3 = 18.4 |
|  | 6¢ | 41 | ×0.3^17 = 0.0 |
|  | 1¢ | 10,227 | ×0.3^22 = 0.0 |
| | | **Σ** | **60.1** |

`yours 9.0 / Σ 60.1 = 15.0%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 15.0% = $3.12/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 60 @ 46¢ → $1.86/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 344 (60 yours) | ×0.3^0 = 344.0 |
|  | 47¢ | 201 | ×0.3^1 = 60.3 |
|  | 55¢ | 87 | ×0.3^9 = 0.0 |
|  | 99¢ | 10,529 | ×0.3^53 = 0.0 |
| | | **Σ** | **404.3** |

`yours 60.0 / Σ 404.3 = 14.8%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 14.8% = $1.86/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20` ← this one
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 60 @ 48¢ → $1.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 344 (60 yours) | ×0.3^0 = 344.0 |
|  | 49¢ | 219 | ×0.3^1 = 65.7 |
|  | 55¢ | 87 | ×0.3^7 = 0.0 |
|  | 99¢ | 10,350 | ×0.3^51 = 0.0 |
| | | **Σ** | **409.7** |

`yours 60.0 / Σ 409.7 = 14.6%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 14.6% = $1.83/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20` ← this one
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-johsun</code> BUY 30 @ 91¢ → $7.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 236 (30 yours) | ×0.3^0 = 235.8 |
|  | 88¢ | 141 | ×0.3^3 = 3.8 |
|  | 86¢ | 525 | ×0.3^5 = 1.3 |
|  | 1¢ | 10,100 | ×0.3^90 = 0.0 |
| | | **Σ** | **240.8** |

`yours 30.0 / Σ 240.8 = 12.5%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 12.5% = $7.79/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun` ← this one
2. `enwc-ussep-nh-2026-09-01-rep-scobro`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> SELL 10 @ 28¢ → $2.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 27¢ | 15 | ×0.3^0 = 15.0 |
| ▶ | 28¢ | 10 (10 yours) | ×0.3^1 = 3.0 |
|  | 30¢ | 111 | ×0.3^3 = 3.0 |
|  | 31¢ | 690 | ×0.3^4 = 5.6 |
|  | 44¢ | 250 | ×0.3^17 = 0.0 |
|  | 55¢ | 59 | ×0.3^28 = 0.0 |
|  | 99¢ | 9,914 | ×0.3^72 = 0.0 |
| | | **Σ** | **26.6** |

`yours 3.0 / Σ 26.6 = 11.3%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 11.3% = $2.35/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 100 @ 47¢ → $1.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 46¢ | 284 | ×0.3^0 = 284.0 |
| ▶ | 47¢ | 100 (100 yours) | ×0.3^1 = 30.0 |
|  | 55¢ | 87 | ×0.3^9 = 0.0 |
|  | 99¢ | 10,529 | ×0.3^53 = 0.0 |
| | | **Σ** | **314.0** |

`yours 30.0 / Σ 314.0 = 9.6%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 9.6% = $1.19/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 100 @ 47¢ → $1.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 46¢ | 284 | ×0.3^0 = 284.0 |
| ▶ | 47¢ | 284 (100 yours) | ×0.3^1 = 85.2 |
|  | 55¢ | 87 | ×0.3^9 = 0.0 |
|  | 99¢ | 10,529 | ×0.3^53 = 0.0 |
| | | **Σ** | **369.2** |

`yours 30.0 / Σ 369.2 = 8.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 8.1% = $1.02/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20` ← this one
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> SELL 100 @ 47¢ → $1.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 46¢ | 284 | ×0.3^0 = 284.0 |
| ▶ | 47¢ | 284 (100 yours) | ×0.3^1 = 85.2 |
|  | 55¢ | 87 | ×0.3^9 = 0.0 |
|  | 99¢ | 10,529 | ×0.3^53 = 0.0 |
| | | **Σ** | **369.2** |

`yours 30.0 / Σ 369.2 = 8.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 8.1% = $1.02/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15` ← this one
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>enwc-ussep-mi-2026-08-04-dem-halste</code> BUY 200 @ 33¢ → $3.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 726 (200 yours) | ×0.3^0 = 726.0 |
|  | 31¢ | 50 | ×0.3^2 = 4.5 |
|  | 30¢ | 66,333 | ×0.3^3 = 1,791.0 |
| | | **Σ** | **2,521.5** |

`yours 200.0 / Σ 2,521.5 = 7.9%`  
`$250 ÷ 3 ÷ 2 = $41.67 × 7.9% = $3.30/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `enwc-ussep-mi-2026-08-04-dem-abdels`
2. `enwc-ussep-mi-2026-08-04-dem-halste` ← this one
3. `enwc-ussep-mi-2026-08-04-dem-malmcm`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-chrpap</code> SELL 10,000 @ 99¢ → $3.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 18 | ×0.3^0 = 18.0 |
|  | 93¢ | 39 | ×0.3^1 = 11.7 |
|  | 96¢ | 5 | ×0.3^4 = 0.0 |
|  | 98¢ | 9 | ×0.3^6 = 0.0 |
| ▶ | 99¢ | 30,515 (10,000 yours) | ×0.3^7 = 6.7 |
| | | **Σ** | **36.4** |

`yours 2.2 / Σ 36.4 = 6.0%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 6.0% = $3.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap` ← this one
2. `enwc-ussep-nh-2026-09-08-dem-karman`

</details>

</details>
<details><summary><code>enwc-usgubp-ok-2026-06-16-rep-gendru</code> BUY 200 @ 16¢ → $3.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 1,000 | ×0.3^0 = 1,000.0 |
| ▶ | 16¢ | 200 (200 yours) | ×0.3^1 = 60.0 |
|  | 13¢ | 482 | ×0.3^4 = 3.9 |
|  | 1¢ | 25,000 | ×0.3^16 = 0.0 |
| | | **Σ** | **1,063.9** |

`yours 60.0 / Σ 1,063.9 = 5.6%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 5.6% = $3.52/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-usgubp-ok-2026-06-16-rep-gendru` ← this one
2. `enwc-usgubp-ok-2026-06-16-rep-mikmaz`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-karman</code> BUY 10,000 @ 1¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 44 | ×0.3^0 = 44.0 |
| ▶ | 1¢ | 23,625 (10,000 yours) | ×0.3^7 = 5.2 |
| | | **Σ** | **49.2** |

`yours 2.2 / Σ 49.2 = 4.4%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 4.4% = $2.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap`
2. `enwc-ussep-nh-2026-09-08-dem-karman` ← this one

</details>

</details>
<details><summary><code>ewc-usgub-ga-2026-11-03-dem</code> BUY 100 @ 59¢ → $2.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 59¢ | 1,510 (100 yours) | ×0.3^0 = 1,510.0 |
|  | 58¢ | 4,449 | ×0.3^1 = 1,334.7 |
|  | 42¢ | 15,000 | ×0.3^17 = 0.0 |
| | | **Σ** | **2,844.7** |

`yours 100.0 / Σ 2,844.7 = 3.5%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 3.5% = $2.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usgub-ga-2026-11-03-dem` ← this one
2. `ewc-usgub-ga-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-frahon</code> SELL 20 @ 75¢ → $0.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 860 (20 yours) | ×0.3^0 = 860.0 |
|  | 99¢ | 10,001 | ×0.3^24 = 0.0 |
| | | **Σ** | **860.0** |

`yours 20.0 / Σ 860.0 = 2.3%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 2.3% = $0.48/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon` ← this one
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-ussep-mn-2026-08-11-dem-angcra</code> BUY 200 @ 9¢ → $0.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 22,733 (200 yours) | ×0.3^0 = 22,733.0 |
| | | **Σ** | **22,733.0** |

`yours 200.0 / Σ 22,733.0 = 0.9%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.9% = $0.55/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-mn-2026-08-11-dem-angcra` ← this one
2. `enwc-ussep-mn-2026-08-11-dem-pegfla`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-chrpap</code> SELL 5 @ 96¢ → $0.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 18 | ×0.3^0 = 18.0 |
|  | 93¢ | 39 | ×0.3^1 = 11.7 |
| ▶ | 96¢ | 5 (5 yours) | ×0.3^4 = 0.0 |
|  | 98¢ | 9 | ×0.3^6 = 0.0 |
|  | 99¢ | 30,515 | ×0.3^7 = 6.7 |
| | | **Σ** | **36.4** |

`yours 0.0 / Σ 36.4 = 0.1%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.1% = $0.07/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap` ← this one
2. `enwc-ussep-nh-2026-09-08-dem-karman`

</details>

</details>
<details><summary><code>ewc-usgub-ca-2026-11-03-xavbec</code> BUY 100 @ 93¢ → $0.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 110,340 (100 yours) | ×0.3^0 = 110,340.3 |
| | | **Σ** | **110,340.3** |

`yours 100.0 / Σ 110,340.3 = 0.1%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.1% = $0.06/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usgub-ca-2026-11-03-stehil`
2. `ewc-usgub-ca-2026-11-03-xavbec` ← this one

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-frahon</code> SELL 10,000 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 75¢ | 860 | ×0.3^0 = 860.0 |
| ▶ | 99¢ | 10,001 (10,000 yours) | ×0.3^24 = 0.0 |
| | | **Σ** | **860.0** |

`yours 0.0 / Σ 860.0 = 0.0%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 0.0% = $0.00/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon` ← this one
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> SELL 2,500 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 48¢ | 580 | ×0.3^0 = 580.0 |
|  | 54¢ | 34 | ×0.3^6 = 0.0 |
|  | 55¢ | 87 | ×0.3^7 = 0.0 |
| ▶ | 99¢ | 12,903 (2,500 yours) | ×0.3^51 = 0.0 |
| | | **Σ** | **580.0** |

`yours 0.0 / Σ 580.0 = 0.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-johsun</code> BUY 10,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 91¢ | 236 | ×0.3^0 = 235.8 |
|  | 88¢ | 141 | ×0.3^3 = 3.8 |
|  | 86¢ | 525 | ×0.3^5 = 1.3 |
| ▶ | 1¢ | 10,100 (10,000 yours) | ×0.3^90 = 0.0 |
| | | **Σ** | **240.8** |

`yours 0.0 / Σ 240.8 = 0.0%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.0% = $0.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun` ← this one
2. `enwc-ussep-nh-2026-09-01-rep-scobro`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 10,000 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 81 | ×0.3^0 = 81.0 |
|  | 55¢ | 87 | ×0.3^47 = 0.0 |
|  | 98¢ | 830 | ×0.3^90 = 0.0 |
| ▶ | 99¢ | 11,001 (10,000 yours) | ×0.3^91 = 0.0 |
| | | **Σ** | **81.0** |

`yours 0.0 / Σ 81.0 = 0.0%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.0% = $0.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun`
2. `enwc-ussep-nh-2026-09-01-rep-scobro` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (11,688 resting) | ~48.4% | ~$30.24 |
| `ewc-usgub-ks-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (77,411 resting) | ~20.2% | ~$12.59 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (26,922 resting) | ~17.2% | ~$10.72 |
| `ewc-usgub-mi-2026-11-03-rep` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (56,920 resting) | ~15.6% | ~$6.49 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (29,597 resting) | ~7.4% | ~$4.61 |
| `ewc-usgub-ia-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (74,633 resting) | ~7.2% | ~$4.51 |
| `ewc-usgub-ks-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (73,122 resting) | ~6.6% | ~$4.10 |
| `ewc-usgub-mi-2026-11-03-dem` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (96,260 resting) | ~8.6% | ~$3.59 |
| `ewc-usse-ne-2026-11-03-rep` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (96,315 resting) | ~5.6% | ~$2.33 |
| `ewc-usgub-ia-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (101,048 resting) | ~3.5% | ~$2.17 |
| `ewc-usgub-oh-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (130,194 resting) | ~2.7% | ~$1.69 |
| `ewc-usgub-nv-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (106,294 resting) | ~2.7% | ~$1.67 |

## Totals

| | Amount |
|---|---:|
| Paid | $78.17 |
| Pending | $77.67 |
| Skipped | $1.21 |
| **Total earned** | **$157.05** |

130 reward rows · 16 days with rewards · 52 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-18 | $44.41 | `████████████████████` |
| 2026-07-17 | $14.71 | `███████` |
| 2026-07-16 | $17.02 | `████████` |
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `██████` |
| 2026-07-13 | $10.03 | `█████` |
| 2026-07-12 | $39.90 | `██████████████████` |
| 2026-07-11 | $2.11 | `█` |
| 2026-07-10 | $2.16 | `█` |
| 2026-07-09 | $4.72 | `██` |
| 2026-07-08 | $2.68 | `█` |
| 2026-07-07 | $0.14 | `█` |
| 2026-07-06 | $0.58 | `█` |
| 2026-07-05 | $0.47 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $157.05 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.30 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.56 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $16.16 |
| `paccc-usse-midterms-2026-11-03-rep` | $6.29 |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | $5.87 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $5.62 |
| `apdc-jerpowgov-2026-12-31` | $5.29 |
| `enwc-ussep-me-2026-07-27-dem-jargol` | $4.80 |
| `ewc-usgub-ca-2026-11-03-stehil` | $4.70 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $4.21 |
| `pic-congress-trump-2026-12-31` | $4.08 |
| `paccc-usho-midterms-2026-11-03-dem` | $4.07 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $3.42 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $3.25 |
| `apdc-alito-2026-12-31` | $3.07 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-20 8:29 AM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 7:16 AM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 7:14 AM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 3:33 AM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 12:08 AM ET | ✅ ok | 130 | $157.05 |
| 2026-07-19 10:33 PM ET | ✅ ok | 130 | $157.05 |
| 2026-07-19 8:40 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 8:21 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 8:15 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 7:14 PM ET | ✅ ok | 102 | $112.64 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
