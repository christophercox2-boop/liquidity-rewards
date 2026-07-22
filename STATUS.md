# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-21 8:10 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$53.23/day estimated (ceiling, not promise — details below)

**Earned:** $192.86 lifetime ($155.84 paid). Last three recorded days — 2026-07-19: **$35.81** · 2026-07-18: **$44.41** · 2026-07-17: **$14.71** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — BUY at the best price, ~$17.90/day for 200 contracts. Runners-up: `enwc-ussep-mi-2026-08-04-dem-abdels` (~$3.25/day), `enwc-ussep-mn-2026-08-11-dem-angcra` (~$2.40/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$53.23/day (~$2.22/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 19.0¢ | 500 | 0 | $250.00 | ✅ scoring — ~99.6% of bid side (10,561 resting ≥ 10,000 ✓) ≈ $12.45/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | BUY | 8.0¢ | 500 | 0 | $250.00 | ✅ scoring — ~74.2% of bid side (30,728 resting ≥ 10,000 ✓) ≈ $9.28/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~32.5% of bid side (30,789 resting ≥ 10,000 ✓) ≈ $4.06/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | SELL | 15.0¢ | 171 | 0 | $250.00 | ✅ scoring — ~27.5% of ask side (27,099 resting ≥ 10,000 ✓) ≈ $5.73/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 1.0¢ | 200 | 0 | $250.00 | ✅ scoring — ~24.9% of ask side (23,898 resting ≥ 10,000 ✓) ≈ $5.19/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 10.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~17.9% of ask side (13,322 resting ≥ 10,000 ✓) ≈ $2.23/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 12.0¢ | 150 | 0 | $250.00 | ✅ scoring — ~16.3% of bid side (37,109 resting ≥ 10,000 ✓) ≈ $3.40/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~13.4% of bid side (74,906 resting ≥ 10,000 ✓) ≈ $2.78/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~12.0% of bid side (83,003 resting ≥ 10,000 ✓) ≈ $2.51/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 19.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~12.0% of ask side (12,211 resting ≥ 10,000 ✓) ≈ $1.51/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 18.0¢ | 50 | 2 | $250.00 | ✅ scoring — ~5.9% of bid side (10,880 resting ≥ 10,000 ✓) ≈ $0.74/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 40.0¢ | 200 | 3 | $250.00 | ✅ scoring — ~4.0% of ask side (11,014 resting ≥ 10,000 ✓) ≈ $0.50/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 8.0¢ | 200 | 0 | $250.00 | ✅ scoring — ~3.3% of bid side (63,399 resting ≥ 10,000 ✓) ≈ $0.69/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 72.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~2.3% of bid side (29,470 resting ≥ 10,000 ✓) ≈ $0.48/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | SELL | 5.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~1.4% of ask side (33,366 resting ≥ 10,000 ✓) ≈ $0.29/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | SELL | 5.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~1.1% of ask side (26,667 resting ≥ 10,000 ✓) ≈ $0.24/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 16.0¢ | 100 | 4 | $250.00 | ✅ scoring — ~1.1% of bid side (10,880 resting ≥ 10,000 ✓) ≈ $0.13/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 16.0¢ | 100 | 4 | $250.00 | ✅ scoring — ~1.1% of bid side (10,880 resting ≥ 10,000 ✓) ≈ $0.13/day (pool ÷ 10 markets) |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | SELL | 18.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~0.7% of ask side (96,095 resting ≥ 10,000 ✓) ≈ $0.45/day (pool ÷ 2 markets) |
| `ewc-usgub-wi-2026-11-03-rep` | BUY | 39.0¢ | 200 | 0 | $250.00 | ✅ scoring — ~0.6% of bid side (123,477 resting ≥ 10,000 ✓) ≈ $0.35/day (pool ÷ 2 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | BUY | 1.0¢ | 10,000 | 7 | $250.00 | ✅ scoring — ~0.3% of bid side (30,728 resting ≥ 10,000 ✓) ≈ $0.04/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | BUY | 1.0¢ | 10,000 | 6 | $250.00 | ✅ scoring — ~0.1% of bid side (30,187 resting ≥ 10,000 ✓) ≈ $0.05/day (pool ÷ 2 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | BUY | 1.0¢ | 10,000 | 16 | $250.00 | ✅ scoring — ~0.0% of bid side (10,941 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 1.0¢ | 10,000 | 19 | $250.00 | ✅ scoring — ~0.0% of bid side (10,880 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 1.0¢ | 10,000 | 18 | $250.00 | ✅ scoring — ~0.0% of bid side (10,561 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 99.0¢ | 10,000 | 80 | $250.00 | ✅ scoring — ~0.0% of ask side (12,211 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 42.0¢ | 100 | 0 | $250.00 | ❌ side has 761 of 10,000 Target Size — side not qualifying |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 1.0¢ | 10,000 | 7 | $250.00 | ❌ outside Target Size window (order 7 ticks from best; window ends 2) |
| `enwc-ussep-nh-2026-09-08-dem-karman` | BUY | 1.0¢ | 7,000 | 9 | $250.00 | ❌ outside Target Size window (order 9 ticks from best; window ends 3) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 1.0¢ | 10,000 | 11 | $250.00 | ❌ outside Target Size window (order 11 ticks from best; window ends 3) |
| …and 3 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 500 @ 19¢ → $12.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 502 (500 yours) | ×0.3^0 = 502.0 |
|  | 15¢ | 6 | ×0.3^4 = 0.0 |
|  | 11¢ | 28 | ×0.3^8 = 0.0 |
|  | 5¢ | 25 | ×0.3^14 = 0.0 |
|  | 1¢ | 10,000 | ×0.3^18 = 0.0 |
| | | **Σ** | **502.1** |

`yours 500.0 / Σ 502.1 = 99.6%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 99.6% = $12.45/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> BUY 500 @ 8¢ → $9.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 667 (500 yours) | ×0.3^0 = 667.0 |
|  | 2¢ | 34 | ×0.3^6 = 0.0 |
|  | 1¢ | 30,027 | ×0.3^7 = 6.6 |
| | | **Σ** | **673.6** |

`yours 500.0 / Σ 673.6 = 74.2%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 74.2% = $9.28/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 10,000 @ 1¢ → $4.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 30,789 (10,000 yours) | ×0.3^0 = 30,789.0 |
| | | **Σ** | **30,789.0** |

`yours 10,000.0 / Σ 30,789.0 = 32.5%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 32.5% = $4.06/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> SELL 171 @ 15¢ → $5.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 171 (171 yours) | ×0.3^0 = 171.3 |
|  | 16¢ | 111 | ×0.3^1 = 33.3 |
|  | 18¢ | 15,487 | ×0.3^3 = 418.1 |
| | | **Σ** | **622.8** |

`yours 171.3 / Σ 622.8 = 27.5%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 27.5% = $5.73/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-sarrod</code> SELL 200 @ 1¢ → $5.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 203 (200 yours) | ×0.3^0 = 203.0 |
|  | 4¢ | 22,214 | ×0.3^3 = 599.8 |
| | | **Σ** | **802.8** |

`yours 200.0 / Σ 802.8 = 24.9%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 24.9% = $5.19/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 100 @ 10¢ → $2.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 121 | ×0.3^0 = 121.0 |
| ▶ | 10¢ | 139 (100 yours) | ×0.3^1 = 41.7 |
|  | 13¢ | 76 | ×0.3^4 = 0.6 |
|  | 14¢ | 1,861 | ×0.3^5 = 4.5 |
|  | 21¢ | 250 | ×0.3^12 = 0.0 |
|  | 45¢ | 25 | ×0.3^36 = 0.0 |
|  | 99¢ | 10,850 | ×0.3^90 = 0.0 |
| | | **Σ** | **167.8** |

`yours 30.0 / Σ 167.8 = 17.9%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 17.9% = $2.23/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 150 @ 12¢ → $3.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 150 (150 yours) | ×0.3^0 = 150.0 |
|  | 10¢ | 693 | ×0.3^2 = 62.4 |
|  | 9¢ | 26,225 | ×0.3^3 = 708.1 |
| | | **Σ** | **920.4** |

`yours 150.0 / Σ 920.4 = 16.3%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 16.3% = $3.40/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-kelroy</code> BUY 10,000 @ 1¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 74,906 (10,000 yours) | ×0.3^0 = 74,906.0 |
| | | **Σ** | **74,906.0** |

`yours 10,000.0 / Σ 74,906.0 = 13.4%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 13.4% = $2.78/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy` ← this one
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-joebre</code> BUY 10,000 @ 1¢ → $2.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 83,003 (10,000 yours) | ×0.3^0 = 83,003.0 |
| | | **Σ** | **83,003.0** |

`yours 10,000.0 / Σ 83,003.0 = 12.0%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 12.0% = $2.51/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre` ← this one
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 100 @ 19¢ → $1.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 652 (100 yours) | ×0.3^0 = 652.0 |
|  | 20¢ | 422 | ×0.3^1 = 126.6 |
|  | 21¢ | 577 | ×0.3^2 = 51.9 |
|  | 25¢ | 6 | ×0.3^6 = 0.0 |
|  | 27¢ | 28 | ×0.3^8 = 0.0 |
|  | 45¢ | 25 | ×0.3^26 = 0.0 |
|  | 99¢ | 10,501 | ×0.3^80 = 0.0 |
| | | **Σ** | **830.5** |

`yours 100.0 / Σ 830.5 = 12.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 12.0% = $1.51/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 50 @ 18¢ → $0.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 55 | ×0.3^0 = 55.0 |
|  | 19¢ | 50 | ×0.3^1 = 15.0 |
| ▶ | 18¢ | 50 (50 yours) | ×0.3^2 = 4.5 |
|  | 16¢ | 200 | ×0.3^4 = 1.6 |
|  | 2¢ | 500 | ×0.3^18 = 0.0 |
|  | 1¢ | 10,025 | ×0.3^19 = 0.0 |
| | | **Σ** | **76.1** |

`yours 4.5 / Σ 76.1 = 5.9%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 5.9% = $0.74/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> SELL 200 @ 40¢ → $0.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 37¢ | 123 | ×0.3^0 = 123.0 |
|  | 38¢ | 25 | ×0.3^1 = 7.5 |
| ▶ | 40¢ | 200 (200 yours) | ×0.3^3 = 5.4 |
|  | 42¢ | 101 | ×0.3^5 = 0.2 |
|  | 45¢ | 25 | ×0.3^8 = 0.0 |
|  | 99¢ | 10,540 | ×0.3^62 = 0.0 |
| | | **Σ** | **136.1** |

`yours 5.4 / Σ 136.1 = 4.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 4.0% = $0.50/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> BUY 200 @ 8¢ → $0.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1,047 (200 yours) | ×0.3^0 = 1,047.0 |
|  | 7¢ | 1,179 | ×0.3^1 = 353.7 |
|  | 6¢ | 51,119 | ×0.3^2 = 4,600.7 |
| | | **Σ** | **6,001.4** |

`yours 200.0 / Σ 6,001.4 = 3.3%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 3.3% = $0.69/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-frahon</code> BUY 50 @ 72¢ → $0.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 72¢ | 132 (50 yours) | ×0.3^0 = 132.0 |
|  | 71¢ | 1,499 | ×0.3^1 = 449.7 |
|  | 70¢ | 17,589 | ×0.3^2 = 1,583.0 |
| | | **Σ** | **2,164.7** |

`yours 50.0 / Σ 2,164.7 = 2.3%`  
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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-joebre</code> SELL 100 @ 5¢ → $0.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 495 | ×0.3^0 = 495.0 |
| ▶ | 5¢ | 100 (100 yours) | ×0.3^1 = 30.0 |
|  | 6¢ | 18,520 | ×0.3^2 = 1,666.8 |
| | | **Σ** | **2,191.8** |

`yours 30.0 / Σ 2,191.8 = 1.4%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 1.4% = $0.29/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre` ← this one
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-kelroy</code> SELL 100 @ 5¢ → $0.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 580 | ×0.3^0 = 580.0 |
| ▶ | 5¢ | 100 (100 yours) | ×0.3^1 = 30.0 |
|  | 6¢ | 22,236 | ×0.3^2 = 2,001.2 |
| | | **Σ** | **2,611.2** |

`yours 30.0 / Σ 2,611.2 = 1.1%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 1.1% = $0.24/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy` ← this one
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 100 @ 16¢ → $0.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 55 | ×0.3^0 = 55.0 |
|  | 19¢ | 50 | ×0.3^1 = 15.0 |
|  | 18¢ | 50 | ×0.3^2 = 4.5 |
| ▶ | 16¢ | 200 (100 yours) | ×0.3^4 = 1.6 |
|  | 2¢ | 500 | ×0.3^18 = 0.0 |
|  | 1¢ | 10,025 | ×0.3^19 = 0.0 |
| | | **Σ** | **76.1** |

`yours 0.8 / Σ 76.1 = 1.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 1.1% = $0.13/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 100 @ 16¢ → $0.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 55 | ×0.3^0 = 55.0 |
|  | 19¢ | 50 | ×0.3^1 = 15.0 |
|  | 18¢ | 50 | ×0.3^2 = 4.5 |
| ▶ | 16¢ | 200 (100 yours) | ×0.3^4 = 1.6 |
|  | 2¢ | 500 | ×0.3^18 = 0.0 |
|  | 1¢ | 10,025 | ×0.3^19 = 0.0 |
| | | **Σ** | **76.1** |

`yours 0.8 / Σ 76.1 = 1.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 1.1% = $0.13/day`  

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
<details><summary><code>enwc-usgubp-ok-2026-06-16-rep-gendru</code> SELL 50 @ 18¢ → $0.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1,349 (50 yours) | ×0.3^0 = 1,349.0 |
|  | 19¢ | 1,110 | ×0.3^1 = 333.0 |
|  | 20¢ | 57,839 | ×0.3^2 = 5,205.5 |
| | | **Σ** | **6,887.5** |

`yours 50.0 / Σ 6,887.5 = 0.7%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.7% = $0.45/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-usgubp-ok-2026-06-16-rep-gendru` ← this one
2. `enwc-usgubp-ok-2026-06-16-rep-mikmaz`

</details>

</details>
<details><summary><code>ewc-usgub-wi-2026-11-03-rep</code> BUY 200 @ 39¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 39¢ | 35,711 (200 yours) | ×0.3^0 = 35,711.0 |
| | | **Σ** | **35,711.0** |

`yours 200.0 / Σ 35,711.0 = 0.6%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.6% = $0.35/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usgub-wi-2026-11-03-dem`
2. `ewc-usgub-wi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> BUY 10,000 @ 1¢ → $0.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 667 | ×0.3^0 = 667.0 |
|  | 2¢ | 34 | ×0.3^6 = 0.0 |
| ▶ | 1¢ | 30,027 (10,000 yours) | ×0.3^7 = 6.6 |
| | | **Σ** | **673.6** |

`yours 2.2 / Σ 673.6 = 0.3%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.3% = $0.04/day`  

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
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> BUY 10,000 @ 1¢ → $0.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 9,537 | ×0.3^0 = 9,537.0 |
|  | 6¢ | 416 | ×0.3^1 = 124.8 |
|  | 2¢ | 9 | ×0.3^5 = 0.0 |
| ▶ | 1¢ | 20,225 (10,000 yours) | ×0.3^6 = 14.7 |
| | | **Σ** | **9,676.6** |

`yours 7.3 / Σ 9,676.6 = 0.1%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.1% = $0.05/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun`
2. `enwc-ussep-nh-2026-09-01-rep-scobro` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> BUY 10,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 132 | ×0.3^0 = 132.0 |
|  | 11¢ | 6 | ×0.3^6 = 0.0 |
|  | 8¢ | 28 | ×0.3^9 = 0.0 |
|  | 2¢ | 750 | ×0.3^15 = 0.0 |
| ▶ | 1¢ | 10,025 (10,000 yours) | ×0.3^16 = 0.0 |
| | | **Σ** | **132.0** |

`yours 0.0 / Σ 132.0 = 0.0%`  
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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 10,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 55 | ×0.3^0 = 55.0 |
|  | 19¢ | 50 | ×0.3^1 = 15.0 |
|  | 18¢ | 50 | ×0.3^2 = 4.5 |
|  | 16¢ | 200 | ×0.3^4 = 1.6 |
|  | 2¢ | 500 | ×0.3^18 = 0.0 |
| ▶ | 1¢ | 10,025 (10,000 yours) | ×0.3^19 = 0.0 |
| | | **Σ** | **76.1** |

`yours 0.0 / Σ 76.1 = 0.0%`  
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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 10,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 502 | ×0.3^0 = 502.0 |
|  | 15¢ | 6 | ×0.3^4 = 0.0 |
|  | 11¢ | 28 | ×0.3^8 = 0.0 |
|  | 5¢ | 25 | ×0.3^14 = 0.0 |
| ▶ | 1¢ | 10,000 (10,000 yours) | ×0.3^18 = 0.0 |
| | | **Σ** | **502.1** |

`yours 0.0 / Σ 502.1 = 0.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.0% = $0.00/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 10,000 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 652 | ×0.3^0 = 652.0 |
|  | 20¢ | 422 | ×0.3^1 = 126.6 |
|  | 21¢ | 577 | ×0.3^2 = 51.9 |
|  | 25¢ | 6 | ×0.3^6 = 0.0 |
|  | 27¢ | 28 | ×0.3^8 = 0.0 |
|  | 45¢ | 25 | ×0.3^26 = 0.0 |
| ▶ | 99¢ | 10,501 (10,000 yours) | ×0.3^80 = 0.0 |
| | | **Σ** | **830.5** |

`yours 0.0 / Σ 830.5 = 0.0%`  
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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 100 @ 42¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 100 (100 yours) | ×0.3^0 = 100.0 |
|  | 43¢ | 101 | ×0.3^1 = 30.3 |
|  | 45¢ | 25 | ×0.3^3 = 0.7 |
|  | 49¢ | 6 | ×0.3^7 = 0.0 |
|  | 51¢ | 28 | ×0.3^9 = 0.0 |
|  | 99¢ | 501 | ×0.3^57 = 0.0 |

`side 761 < target 10,000 → side pays nobody`  

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> BUY 10,000 @ 1¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 1,047 | ×0.3^0 = 1,047.0 |
|  | 7¢ | 1,179 | ×0.3^1 = 353.7 |
|  | 6¢ | 51,119 | ×0.3^2 = 4,600.7 |
| | | **Σ** | **6,001.4** |

`you 7t from best, window ends 2t → score 0`  

</details>
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-karman</code> BUY 7,000 @ 1¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 9,552 | ×0.3^0 = 9,552.0 |
|  | 7¢ | 942 | ×0.3^3 = 25.4 |
| | | **Σ** | **9,577.4** |

`you 9t from best, window ends 3t → score 0`  

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 10,000 @ 1¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 150 | ×0.3^0 = 150.0 |
|  | 10¢ | 693 | ×0.3^2 = 62.4 |
|  | 9¢ | 26,225 | ×0.3^3 = 708.1 |
| | | **Σ** | **920.4** |

`you 11t from best, window ends 3t → score 0`  

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
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (11,377 resting) | ~28.6% | ~$17.90 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (13,116 resting) | ~7.8% | ~$3.25 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (53,122 resting) | ~3.8% | ~$2.40 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (41,652 resting) | ~5.5% | ~$2.30 |
| `ewc-usgub-mi-2026-11-03-rep` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (73,121 resting) | ~4.3% | ~$1.80 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (33,600 resting) | ~2.9% | ~$1.78 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (110,719 resting) | ~2.2% | ~$1.36 |
| `ewc-usgub-ga-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (77,981 resting) | ~1.9% | ~$1.20 |
| `ewc-usse-ne-2026-11-03-rep` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (75,838 resting) | ~2.8% | ~$1.18 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (83,323 resting) | ~1.2% | ~$0.76 |
| `ewc-usgub-az-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (192,165 resting) | ~1.2% | ~$0.72 |
| `ewc-usgub-ga-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (83,664 resting) | ~1.1% | ~$0.70 |

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
| 2026-07-21 8:10 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 7:14 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 6:14 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 4:38 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 2:43 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 12:47 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 10:27 AM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 8:02 AM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 5:43 AM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 2:43 AM ET | ✅ ok | 149 | $192.86 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
