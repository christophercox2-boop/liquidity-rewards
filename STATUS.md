# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-20 9:25 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$96.46/day estimated (ceiling, not promise — details below)

**Earned:** $192.86 lifetime ($155.84 paid). Last three recorded days — 2026-07-19: **$35.81** · 2026-07-18: **$44.41** · 2026-07-17: **$14.71** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — SELL at the best price, ~$17.30/day for 200 contracts. Runners-up: `enwc-ussep-mi-2026-08-04-dem-abdels` (~$8.54/day), `ewc-usgub-oh-2026-11-03-dem` (~$8.10/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$96.46/day (~$4.02/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 24.0¢ | 300 | 0 | $250.00 | ✅ scoring — ~99.9% of bid side (10,360 resting ≥ 10,000 ✓) ≈ $20.81/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | SELL | 27.0¢ | 20 | 0 | $250.00 | ✅ scoring — ~76.9% of ask side (11,527 resting ≥ 10,000 ✓) ≈ $16.03/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~47.8% of bid side (20,909 resting ≥ 10,000 ✓) ≈ $5.98/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~47.8% of bid side (20,909 resting ≥ 10,000 ✓) ≈ $5.98/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 1.0¢ | 10,000 | 2 | $250.00 | ✅ scoring — ~47.1% of bid side (20,483 resting ≥ 10,000 ✓) ≈ $9.80/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~30.1% of bid side (33,252 resting ≥ 10,000 ✓) ≈ $3.76/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~23.6% of bid side (42,284 resting ≥ 10,000 ✓) ≈ $2.96/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | SELL | 28.0¢ | 20 | 1 | $250.00 | ✅ scoring — ~23.1% of ask side (11,527 resting ≥ 10,000 ✓) ≈ $4.81/day (pool ÷ 6 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | BUY | 1.0¢ | 10,000 | 5 | $250.00 | ✅ scoring — ~21.2% of bid side (31,802 resting ≥ 10,000 ✓) ≈ $13.26/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 4.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~8.7% of ask side (13,251 resting ≥ 10,000 ✓) ≈ $1.81/day (pool ÷ 6 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | BUY | 2.0¢ | 1,000 | 4 | $250.00 | ✅ scoring — ~7.1% of bid side (31,802 resting ≥ 10,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 12.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~5.0% of ask side (12,694 resting ≥ 10,000 ✓) ≈ $3.15/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 9.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~3.7% of ask side (33,061 resting ≥ 10,000 ✓) ≈ $2.33/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 3.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~2.6% of bid side (20,483 resting ≥ 10,000 ✓) ≈ $0.54/day (pool ÷ 6 markets) |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | SELL | 18.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~1.0% of ask side (76,369 resting ≥ 10,000 ✓) ≈ $0.63/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 65.0¢ | 10 | 1 | $250.00 | ✅ scoring — ~0.6% of bid side (10,666 resting ≥ 10,000 ✓) ≈ $0.13/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 34.0¢ | 10 | 2 | $250.00 | ✅ scoring — ~0.3% of ask side (11,443 resting ≥ 10,000 ✓) ≈ $0.04/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 30.0¢ | 10 | 3 | $250.00 | ✅ scoring — ~0.1% of ask side (11,443 resting ≥ 10,000 ✓) ≈ $0.01/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-08-dem-karman` | BUY | 1.0¢ | 7,000 | 9 | $250.00 | ✅ scoring — ~0.0% of bid side (18,097 resting ≥ 10,000 ✓) ≈ $0.02/day (pool ÷ 2 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 30.0¢ | 10 | 5 | $250.00 | ✅ scoring — ~0.0% of ask side (11,664 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 35.0¢ | 10 | 5 | $250.00 | ✅ scoring — ~0.0% of ask side (11,943 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | BUY | 20.0¢ | 101 | 11 | $250.00 | ✅ scoring — ~0.0% of bid side (11,011 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 1.0¢ | 10,000 | 23 | $250.00 | ✅ scoring — ~0.0% of bid side (10,360 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 1.0¢ | 10,000 | 65 | $250.00 | ✅ scoring — ~0.0% of bid side (10,666 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | SELL | 99.0¢ | 10,000 | 72 | $250.00 | ✅ scoring — ~0.0% of ask side (11,527 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | SELL | 99.0¢ | 10,000 | 94 | $250.00 | ✅ scoring — ~0.0% of ask side (11,935 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 6 markets) |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 300 @ 24¢ → $20.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 300 (300 yours) | ×0.3^0 = 300.0 |
|  | 22¢ | 4 | ×0.3^2 = 0.4 |
|  | 12¢ | 15 | ×0.3^12 = 0.0 |
|  | 6¢ | 41 | ×0.3^18 = 0.0 |
|  | 1¢ | 10,000 | ×0.3^23 = 0.0 |
| | | **Σ** | **300.4** |

`yours 300.0 / Σ 300.4 = 99.9%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 99.9% = $20.81/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> SELL 20 @ 27¢ → $16.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 20 (20 yours) | ×0.3^0 = 20.0 |
|  | 28¢ | 20 | ×0.3^1 = 6.0 |
|  | 43¢ | 101 | ×0.3^16 = 0.0 |
|  | 44¢ | 385 | ×0.3^17 = 0.0 |
|  | 99¢ | 11,001 | ×0.3^72 = 0.0 |
| | | **Σ** | **26.0** |

`yours 20.0 / Σ 26.0 = 76.9%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 76.9% = $16.03/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> BUY 10,000 @ 1¢ → $5.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 20,909 (10,000 yours) | ×0.3^0 = 20,909.0 |
| | | **Σ** | **20,909.0** |

`yours 10,000.0 / Σ 20,909.0 = 47.8%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 47.8% = $5.98/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> BUY 10,000 @ 1¢ → $5.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 20,909 (10,000 yours) | ×0.3^0 = 20,909.0 |
| | | **Σ** | **20,909.0** |

`yours 10,000.0 / Σ 20,909.0 = 47.8%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 47.8% = $5.98/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> BUY 10,000 @ 1¢ → $9.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 63 | ×0.3^0 = 63.0 |
|  | 2¢ | 55 | ×0.3^1 = 16.5 |
| ▶ | 1¢ | 20,365 (10,000 yours) | ×0.3^2 = 1,832.8 |
| | | **Σ** | **1,912.3** |

`yours 900.0 / Σ 1,912.3 = 47.1%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 47.1% = $9.80/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> BUY 10,000 @ 1¢ → $3.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 33,252 (10,000 yours) | ×0.3^0 = 33,252.0 |
| | | **Σ** | **33,252.0** |

`yours 10,000.0 / Σ 33,252.0 = 30.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 30.1% = $3.76/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10` ← this one
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 10,000 @ 1¢ → $2.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 42,284 (10,000 yours) | ×0.3^0 = 42,284.0 |
| | | **Σ** | **42,284.0** |

`yours 10,000.0 / Σ 42,284.0 = 23.6%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 23.6% = $2.96/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> SELL 20 @ 28¢ → $4.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 27¢ | 20 | ×0.3^0 = 20.0 |
| ▶ | 28¢ | 20 (20 yours) | ×0.3^1 = 6.0 |
|  | 43¢ | 101 | ×0.3^16 = 0.0 |
|  | 44¢ | 385 | ×0.3^17 = 0.0 |
|  | 99¢ | 11,001 | ×0.3^72 = 0.0 |
| | | **Σ** | **26.0** |

`yours 6.0 / Σ 26.0 = 23.1%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 23.1% = $4.81/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> BUY 10,000 @ 1¢ → $13.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 25 | ×0.3^0 = 25.0 |
|  | 5¢ | 8 | ×0.3^1 = 2.4 |
|  | 3¢ | 64 | ×0.3^3 = 1.7 |
|  | 2¢ | 1,480 | ×0.3^4 = 12.0 |
| ▶ | 1¢ | 30,225 (10,000 yours) | ×0.3^5 = 73.4 |
| | | **Σ** | **114.6** |

`yours 24.3 / Σ 114.6 = 21.2%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 21.2% = $13.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun`
2. `enwc-ussep-nh-2026-09-01-rep-scobro` ← this one

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-sarrod</code> SELL 100 @ 4¢ → $1.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1,150 (100 yours) | ×0.3^0 = 1,150.0 |
|  | 9¢ | 101 | ×0.3^5 = 0.2 |
|  | 18¢ | 250 | ×0.3^14 = 0.0 |
|  | 99¢ | 11,750 | ×0.3^95 = 0.0 |
| | | **Σ** | **1,150.2** |

`yours 100.0 / Σ 1,150.2 = 8.7%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 8.7% = $1.81/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> BUY 1,000 @ 2¢ → $4.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 25 | ×0.3^0 = 25.0 |
|  | 5¢ | 8 | ×0.3^1 = 2.4 |
|  | 3¢ | 64 | ×0.3^3 = 1.7 |
| ▶ | 2¢ | 1,480 (1,000 yours) | ×0.3^4 = 12.0 |
|  | 1¢ | 30,225 | ×0.3^5 = 73.4 |
| | | **Σ** | **114.6** |

`yours 8.1 / Σ 114.6 = 7.1%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 7.1% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun`
2. `enwc-ussep-nh-2026-09-01-rep-scobro` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-karman</code> SELL 100 @ 12¢ → $3.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 200 | ×0.3^0 = 200.0 |
| ▶ | 12¢ | 1,243 (100 yours) | ×0.3^1 = 372.9 |
|  | 13¢ | 250 | ×0.3^2 = 22.5 |
|  | 99¢ | 11,001 | ×0.3^88 = 0.0 |
| | | **Σ** | **595.4** |

`yours 30.0 / Σ 595.4 = 5.0%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 5.0% = $3.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap`
2. `enwc-ussep-nh-2026-09-08-dem-karman` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 100 @ 9¢ → $2.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 755 (100 yours) | ×0.3^0 = 755.0 |
|  | 10¢ | 55 | ×0.3^1 = 16.5 |
|  | 11¢ | 21,224 | ×0.3^2 = 1,910.2 |
| | | **Σ** | **2,681.7** |

`yours 100.0 / Σ 2,681.7 = 3.7%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 3.7% = $2.33/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun`
2. `enwc-ussep-nh-2026-09-01-rep-scobro` ← this one

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> BUY 50 @ 3¢ → $0.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 63 (50 yours) | ×0.3^0 = 63.0 |
|  | 2¢ | 55 | ×0.3^1 = 16.5 |
|  | 1¢ | 20,365 | ×0.3^2 = 1,832.8 |
| | | **Σ** | **1,912.3** |

`yours 50.0 / Σ 1,912.3 = 2.6%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 2.6% = $0.54/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-ok-2026-06-16-rep-gendru</code> SELL 50 @ 18¢ → $0.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1,455 (50 yours) | ×0.3^0 = 1,455.0 |
|  | 19¢ | 60 | ×0.3^1 = 18.0 |
|  | 20¢ | 39,000 | ×0.3^2 = 3,510.0 |
| | | **Σ** | **4,983.0** |

`yours 50.0 / Σ 4,983.0 = 1.0%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 1.0% = $0.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-usgubp-ok-2026-06-16-rep-gendru` ← this one
2. `enwc-usgubp-ok-2026-06-16-rep-mikmaz`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-frahon</code> BUY 10 @ 65¢ → $0.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 66¢ | 400 | ×0.3^0 = 400.0 |
| ▶ | 65¢ | 196 (10 yours) | ×0.3^1 = 58.8 |
|  | 64¢ | 69 | ×0.3^2 = 6.2 |
|  | 57¢ | 1 | ×0.3^9 = 0.0 |
|  | 1¢ | 10,000 | ×0.3^65 = 0.0 |
| | | **Σ** | **465.0** |

`yours 3.0 / Σ 465.0 = 0.6%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 0.6% = $0.13/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon` ← this one
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 10 @ 34¢ → $0.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 32¢ | 278 | ×0.3^0 = 278.0 |
|  | 33¢ | 101 | ×0.3^1 = 30.3 |
| ▶ | 34¢ | 10 (10 yours) | ×0.3^2 = 0.9 |
|  | 45¢ | 25 | ×0.3^13 = 0.0 |
|  | 99¢ | 11,029 | ×0.3^67 = 0.0 |
| | | **Σ** | **309.2** |

`yours 0.9 / Σ 309.2 = 0.3%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.3% = $0.04/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 10 @ 30¢ → $0.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 27¢ | 278 | ×0.3^0 = 278.0 |
|  | 28¢ | 101 | ×0.3^1 = 30.3 |
| ▶ | 30¢ | 10 (10 yours) | ×0.3^3 = 0.3 |
|  | 45¢ | 25 | ×0.3^18 = 0.0 |
|  | 99¢ | 11,029 | ×0.3^72 = 0.0 |
| | | **Σ** | **308.6** |

`yours 0.3 / Σ 308.6 = 0.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.1% = $0.01/day`  

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
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-karman</code> BUY 7,000 @ 1¢ → $0.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 440 | ×0.3^0 = 440.0 |
|  | 4¢ | 182 | ×0.3^6 = 0.1 |
| ▶ | 1¢ | 17,475 (7,000 yours) | ×0.3^9 = 0.3 |
| | | **Σ** | **440.5** |

`yours 0.1 / Σ 440.5 = 0.0%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.0% = $0.02/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap`
2. `enwc-ussep-nh-2026-09-08-dem-karman` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 10 @ 30¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 25¢ | 278 | ×0.3^0 = 278.0 |
|  | 26¢ | 400 | ×0.3^1 = 120.0 |
|  | 28¢ | 101 | ×0.3^3 = 2.7 |
| ▶ | 30¢ | 10 (10 yours) | ×0.3^5 = 0.0 |
|  | 45¢ | 25 | ×0.3^20 = 0.0 |
|  | 99¢ | 10,850 | ×0.3^74 = 0.0 |
| | | **Σ** | **400.8** |

`yours 0.0 / Σ 400.8 = 0.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.0% = $0.00/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 10 @ 35¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 30¢ | 278 | ×0.3^0 = 278.0 |
|  | 31¢ | 500 | ×0.3^1 = 150.0 |
|  | 33¢ | 101 | ×0.3^3 = 2.7 |
| ▶ | 35¢ | 10 (10 yours) | ×0.3^5 = 0.0 |
|  | 45¢ | 25 | ×0.3^15 = 0.0 |
|  | 99¢ | 11,029 | ×0.3^69 = 0.0 |
| | | **Σ** | **430.8** |

`yours 0.0 / Σ 430.8 = 0.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.0% = $0.00/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> BUY 101 @ 20¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 31¢ | 3 | ×0.3^0 = 3.0 |
|  | 30¢ | 4 | ×0.3^1 = 1.2 |
|  | 27¢ | 4 | ×0.3^4 = 0.0 |
|  | 26¢ | 11 | ×0.3^5 = 0.0 |
|  | 25¢ | 4 | ×0.3^6 = 0.0 |
|  | 24¢ | 28 | ×0.3^7 = 0.0 |
| ▶ | 20¢ | 101 (101 yours) | ×0.3^11 = 0.0 |
|  | 15¢ | 25 | ×0.3^16 = 0.0 |
|  | 1¢ | 10,831 | ×0.3^30 = 0.0 |
| | | **Σ** | **4.3** |

`yours 0.0 / Σ 4.3 = 0.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 10,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 24¢ | 300 | ×0.3^0 = 300.0 |
|  | 22¢ | 4 | ×0.3^2 = 0.4 |
|  | 12¢ | 15 | ×0.3^12 = 0.0 |
|  | 6¢ | 41 | ×0.3^18 = 0.0 |
| ▶ | 1¢ | 10,000 (10,000 yours) | ×0.3^23 = 0.0 |
| | | **Σ** | **300.4** |

`yours 0.0 / Σ 300.4 = 0.0%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 0.0% = $0.00/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-frahon</code> BUY 10,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 66¢ | 400 | ×0.3^0 = 400.0 |
|  | 65¢ | 196 | ×0.3^1 = 58.8 |
|  | 64¢ | 69 | ×0.3^2 = 6.2 |
|  | 57¢ | 1 | ×0.3^9 = 0.0 |
| ▶ | 1¢ | 10,000 (10,000 yours) | ×0.3^65 = 0.0 |
| | | **Σ** | **465.0** |

`yours 0.0 / Σ 465.0 = 0.0%`  
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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> SELL 10,000 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 27¢ | 20 | ×0.3^0 = 20.0 |
|  | 28¢ | 20 | ×0.3^1 = 6.0 |
|  | 43¢ | 101 | ×0.3^16 = 0.0 |
|  | 44¢ | 385 | ×0.3^17 = 0.0 |
| ▶ | 99¢ | 11,001 (10,000 yours) | ×0.3^72 = 0.0 |
| | | **Σ** | **26.0** |

`yours 0.0 / Σ 26.0 = 0.0%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 0.0% = $0.00/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-joebre</code> SELL 10,000 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 808 | ×0.3^0 = 808.0 |
|  | 10¢ | 101 | ×0.3^5 = 0.2 |
|  | 20¢ | 25 | ×0.3^15 = 0.0 |
| ▶ | 99¢ | 11,001 (10,000 yours) | ×0.3^94 = 0.0 |
| | | **Σ** | **808.2** |

`yours 0.0 / Σ 808.2 = 0.0%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 0.0% = $0.00/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre` ← this one
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-19 | ~$36.97 | $35.81 | 97% |

Biggest gaps on 2026-07-19: `enwc-ussep-nh-2026-09-08-dem-karman` (est ~$12.54 → got $8.70), `enwc-ussep-nh-2026-09-01-rep-scobro` (est ~$6.05 → got $2.35), `enwc-usgubp-wi-2026-08-11-dem-sarrod` (est ~$3.33 → got $0.07)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (12,666 resting) | ~27.7% | ~$17.30 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (11,451 resting) | ~20.5% | ~$8.54 |
| `ewc-usgub-oh-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (88,201 resting) | ~13.0% | ~$8.10 |
| `ewc-usgub-ia-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (99,679 resting) | ~10.4% | ~$6.52 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (11,643 resting) | ~9.6% | ~$5.97 |
| `ewc-usgub-ia-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (84,137 resting) | ~8.9% | ~$5.57 |
| `ewc-usgub-ks-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (161,522 resting) | ~5.2% | ~$3.24 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (39,510 resting) | ~4.9% | ~$3.05 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (39,548 resting) | ~4.5% | ~$2.83 |
| `enwc-usgubp-fl-2026-08-18-rep-jaycol` | $250.00 ÷ 3 | 0.30 | 10,000 | SELL side (326,707 resting) | ~6.6% | ~$2.74 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (51,429 resting) | ~4.2% | ~$2.63 |
| `ewc-usgub-ga-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (106,775 resting) | ~4.0% | ~$2.49 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $35.81 |
| Skipped | $1.21 |
| **Total earned** | **$192.86** |

149 reward rows · 17 days with rewards · 54 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-19 | $35.81 | `████████████████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $192.86 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.30 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.56 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $16.23 |
| `apdc-jerpowgov-2026-12-31` | $12.15 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $10.62 |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | $10.16 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $6.56 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $6.31 |
| `paccc-usse-midterms-2026-11-03-rep` | $6.29 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $5.62 |
| `enwc-ussep-me-2026-07-27-dem-jargol` | $4.80 |
| `ewc-usgub-ca-2026-11-03-stehil` | $4.70 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $4.09 |
| `paccc-usho-midterms-2026-11-03-dem` | $4.09 |
| `pic-congress-trump-2026-12-31` | $4.08 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-20 9:25 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-20 8:14 PM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 8:06 PM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 7:18 PM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 6:15 PM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 4:43 PM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 2:23 PM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 11:54 AM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 11:35 AM ET | ✅ ok | 130 | $157.05 |
| 2026-07-20 11:23 AM ET | ✅ ok | 130 | $157.05 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
