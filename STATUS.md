# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-23 2:42 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$92.83/day estimated (ceiling, not promise — details below)

**Earned:** $390.84 lifetime ($155.84 paid). Last three recorded days — 2026-07-21: **$91.44** · 2026-07-20: **$106.54** · 2026-07-19: **$35.81** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — SELL at the best price, ~$42.31/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-12-31` (~$29.38/day), `enwc-ussep-mn-2026-08-11-dem-angcra` (~$28.60/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$92.83/day (~$3.87/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 7.0¢ | 400 | 0 | $250.00 | ✅ scoring — ~55.6% of ask side (12,643 resting ≥ 10,000 ✓) ≈ $5.80/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | SELL | 5.0¢ | 157 | 0 | $250.00 | ✅ scoring — ~55.3% of ask side (12,014 resting ≥ 10,000 ✓) ≈ $6.91/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~49.9% of bid side (20,025 resting ≥ 10,000 ✓) ≈ $5.20/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | BUY | 2.0¢ | 2,500 | 0 | $250.00 | ✅ scoring — ~36.5% of bid side (15,764 resting ≥ 10,000 ✓) ≈ $4.56/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | BUY | 3.0¢ | 1,000 | 0 | $250.00 | ✅ scoring — ~35.6% of bid side (21,033 resting ≥ 10,000 ✓) ≈ $4.45/day (pool ÷ 10 markets) |
| `apdc-alito-2026-12-31` | BUY | 20.0¢ | 80 | 0 | $250.00 | ✅ scoring — ~33.0% of bid side (58,299 resting ≥ 10,000 ✓) ≈ $13.77/day (pool ÷ 3 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | BUY | 1.0¢ | 10,000 | 2 | $250.00 | ✅ scoring — ~32.0% of bid side (21,033 resting ≥ 10,000 ✓) ≈ $4.00/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 20.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~25.5% of ask side (14,089 resting ≥ 10,000 ✓) ≈ $3.18/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-tregow` | SELL | 29.0¢ | 300 | 0 | $250.00 | ✅ scoring — ~24.2% of ask side (12,453 resting ≥ 10,000 ✓) ≈ $2.52/day (pool ÷ 12 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 10.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~24.1% of bid side (46,893 resting ≥ 10,000 ✓) ≈ $5.02/day (pool ÷ 6 markets) |
| `enwc-ussep-sc-2026-08-11-rep-tregow` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~24.1% of bid side (41,501 resting ≥ 10,000 ✓) ≈ $2.51/day (pool ÷ 12 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~23.5% of bid side (42,537 resting ≥ 10,000 ✓) ≈ $4.90/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 2.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~23.4% of ask side (41,454 resting ≥ 10,000 ✓) ≈ $4.88/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~20.9% of bid side (47,789 resting ≥ 10,000 ✓) ≈ $2.62/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~20.7% of bid side (48,236 resting ≥ 10,000 ✓) ≈ $4.32/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 9.0¢ | 200 | 0 | $250.00 | ✅ scoring — ~15.6% of bid side (46,026 resting ≥ 10,000 ✓) ≈ $3.25/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 20.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~14.5% of bid side (10,747 resting ≥ 10,000 ✓) ≈ $1.82/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 14.0¢ | 10 | 0 | $250.00 | ✅ scoring — ~14.3% of ask side (11,055 resting ≥ 10,000 ✓) ≈ $1.79/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | SELL | 11.0¢ | 171 | 0 | $250.00 | ✅ scoring — ~12.6% of ask side (45,245 resting ≥ 10,000 ✓) ≈ $2.63/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | BUY | 30.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~12.3% of bid side (10,907 resting ≥ 10,000 ✓) ≈ $1.54/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | BUY | 21.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~10.8% of bid side (10,985 resting ≥ 10,000 ✓) ≈ $1.35/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 23.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~8.1% of bid side (11,043 resting ≥ 10,000 ✓) ≈ $1.01/day (pool ÷ 10 markets) |
| `apdc-alito-2026-12-31` | SELL | 26.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~5.4% of ask side (12,287 resting ≥ 10,000 ✓) ≈ $2.25/day (pool ÷ 3 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 73.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~4.1% of bid side (25,278 resting ≥ 10,000 ✓) ≈ $0.84/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 73.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~4.1% of bid side (25,278 resting ≥ 10,000 ✓) ≈ $0.84/day (pool ÷ 6 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | BUY | 1.0¢ | 10,000 | 5 | $250.00 | ✅ scoring — ~2.7% of bid side (21,541 resting ≥ 10,000 ✓) ≈ $0.28/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 20.0¢ | 10 | 0 | $250.00 | ✅ scoring — ~1.5% of bid side (10,747 resting ≥ 10,000 ✓) ≈ $0.18/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 18.0¢ | 100 | 4 | $250.00 | ✅ scoring — ~1.2% of ask side (11,055 resting ≥ 10,000 ✓) ≈ $0.15/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | BUY | 8.0¢ | 290 | 3 | $250.00 | ✅ scoring — ~1.0% of bid side (11,851 resting ≥ 10,000 ✓) ≈ $0.13/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | BUY | 1.0¢ | 205 | 1 | $250.00 | ✅ scoring — ~0.9% of bid side (15,764 resting ≥ 10,000 ✓) ≈ $0.11/day (pool ÷ 10 markets) |
| …and 16 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 400 @ 7¢ → $5.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 719 (400 yours) | ×0.3^0 = 719.0 |
|  | 22¢ | 250 | ×0.3^15 = 0.0 |
|  | 50¢ | 25 | ×0.3^43 = 0.0 |
|  | 99¢ | 11,649 | ×0.3^92 = 0.0 |
| | | **Σ** | **719.0** |

`yours 400.0 / Σ 719.0 = 55.6%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 55.6% = $5.80/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn` ← this one
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> SELL 157 @ 5¢ → $6.91/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 284 (157 yours) | ×0.3^0 = 284.0 |
|  | 11¢ | 6 | ×0.3^6 = 0.0 |
|  | 17¢ | 29 | ×0.3^12 = 0.0 |
|  | 19¢ | 125 | ×0.3^14 = 0.0 |
|  | 24¢ | 250 | ×0.3^19 = 0.0 |
|  | 26¢ | 101 | ×0.3^21 = 0.0 |
|  | 45¢ | 25 | ×0.3^40 = 0.0 |
|  | 99¢ | 11,194 | ×0.3^94 = 0.0 |
| | | **Σ** | **284.0** |

`yours 157.0 / Σ 284.0 = 55.3%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 55.3% = $6.91/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> BUY 10,000 @ 1¢ → $5.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 20,025 (10,000 yours) | ×0.3^0 = 20,025.0 |
| | | **Σ** | **20,025.0** |

`yours 10,000.0 / Σ 20,025.0 = 49.9%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 49.9% = $5.20/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn` ← this one
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> BUY 2,500 @ 2¢ → $4.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 3,034 (2,500 yours) | ×0.3^0 = 3,034.0 |
|  | 1¢ | 12,730 | ×0.3^1 = 3,819.0 |
| | | **Σ** | **6,853.0** |

`yours 2,500.0 / Σ 6,853.0 = 36.5%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 36.5% = $4.56/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> BUY 1,000 @ 3¢ → $4.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 1,000 (1,000 yours) | ×0.3^0 = 1,000.0 |
|  | 2¢ | 33 | ×0.3^1 = 9.9 |
|  | 1¢ | 20,000 | ×0.3^2 = 1,800.0 |
| | | **Σ** | **2,809.9** |

`yours 1,000.0 / Σ 2,809.9 = 35.6%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 35.6% = $4.45/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 80 @ 20¢ → $13.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 80 (80 yours) | ×0.3^0 = 80.0 |
|  | 19¢ | 28 | ×0.3^1 = 8.4 |
|  | 17¢ | 61 | ×0.3^3 = 1.6 |
|  | 16¢ | 2,000 | ×0.3^4 = 16.2 |
|  | 15¢ | 55,930 | ×0.3^5 = 135.9 |
| | | **Σ** | **242.2** |

`yours 80.0 / Σ 242.2 = 33.0%`  
`$250 ÷ 3 ÷ 2 = $41.67 × 33.0% = $13.77/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-alito-2026-07-31`
2. `apdc-alito-2026-08-31`
3. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> BUY 10,000 @ 1¢ → $4.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1,000 | ×0.3^0 = 1,000.0 |
|  | 2¢ | 33 | ×0.3^1 = 9.9 |
| ▶ | 1¢ | 20,000 (10,000 yours) | ×0.3^2 = 1,800.0 |
| | | **Σ** | **2,809.9** |

`yours 900.0 / Σ 2,809.9 = 32.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 32.0% = $4.00/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 100 @ 20¢ → $3.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 148 (100 yours) | ×0.3^0 = 148.0 |
|  | 21¢ | 815 | ×0.3^1 = 244.5 |
|  | 26¢ | 6 | ×0.3^6 = 0.0 |
|  | 28¢ | 28 | ×0.3^8 = 0.0 |
|  | 45¢ | 25 | ×0.3^25 = 0.0 |
|  | 99¢ | 13,067 | ×0.3^79 = 0.0 |
| | | **Σ** | **392.5** |

`yours 100.0 / Σ 392.5 = 25.5%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 25.5% = $3.18/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-tregow</code> SELL 300 @ 29¢ → $2.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 1,240 (300 yours) | ×0.3^0 = 1,240.0 |
|  | 50¢ | 25 | ×0.3^21 = 0.0 |
|  | 72¢ | 1 | ×0.3^43 = 0.0 |
|  | 99¢ | 11,187 | ×0.3^70 = 0.0 |
| | | **Σ** | **1,240.0** |

`yours 300.0 / Σ 1,240.0 = 24.2%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 24.2% = $2.52/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow` ← this one
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> BUY 100 @ 10¢ → $5.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 5 | ×0.3^0 = 5.0 |
| ▶ | 10¢ | 100 (100 yours) | ×0.3^1 = 30.0 |
|  | 6¢ | 36,788 | ×0.3^5 = 89.4 |
| | | **Σ** | **124.4** |

`yours 30.0 / Σ 124.4 = 24.1%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 24.1% = $5.02/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-tregow</code> BUY 10,000 @ 1¢ → $2.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 41,501 (10,000 yours) | ×0.3^0 = 41,501.0 |
| | | **Σ** | **41,501.0** |

`yours 10,000.0 / Σ 41,501.0 = 24.1%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 24.1% = $2.51/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow` ← this one
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-kelroy</code> BUY 10,000 @ 1¢ → $4.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 42,537 (10,000 yours) | ×0.3^0 = 42,537.0 |
| | | **Σ** | **42,537.0** |

`yours 10,000.0 / Σ 42,537.0 = 23.5%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 23.5% = $4.90/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy` ← this one
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-sarrod</code> SELL 100 @ 2¢ → $4.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 103 (100 yours) | ×0.3^0 = 103.0 |
|  | 6¢ | 40,000 | ×0.3^4 = 324.0 |
| | | **Σ** | **427.0** |

`yours 100.0 / Σ 427.0 = 23.4%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 23.4% = $4.88/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> BUY 10,000 @ 1¢ → $2.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 47,789 (10,000 yours) | ×0.3^0 = 47,789.0 |
| | | **Σ** | **47,789.0** |

`yours 10,000.0 / Σ 47,789.0 = 20.9%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 20.9% = $2.62/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-joebre</code> BUY 10,000 @ 1¢ → $4.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 48,236 (10,000 yours) | ×0.3^0 = 48,236.0 |
| | | **Σ** | **48,236.0** |

`yours 10,000.0 / Σ 48,236.0 = 20.7%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 20.7% = $4.32/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre` ← this one
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 200 @ 9¢ → $3.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 319 (200 yours) | ×0.3^0 = 319.0 |
|  | 6¢ | 35,666 | ×0.3^3 = 963.0 |
| | | **Σ** | **1,282.0** |

`yours 200.0 / Σ 1,282.0 = 15.6%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 15.6% = $3.25/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 100 @ 20¢ → $1.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 688 (100 yours) | ×0.3^0 = 688.0 |
|  | 14¢ | 6 | ×0.3^6 = 0.0 |
|  | 12¢ | 28 | ×0.3^8 = 0.0 |
|  | 1¢ | 10,025 | ×0.3^19 = 0.0 |
| | | **Σ** | **688.0** |

`yours 100.0 / Σ 688.0 = 14.5%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 14.5% = $1.82/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 10 @ 14¢ → $1.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 66 (10 yours) | ×0.3^0 = 66.0 |
|  | 16¢ | 15 | ×0.3^2 = 1.3 |
|  | 17¢ | 56 | ×0.3^3 = 1.5 |
|  | 18¢ | 100 | ×0.3^4 = 0.8 |
|  | 21¢ | 529 | ×0.3^7 = 0.1 |
|  | 36¢ | 101 | ×0.3^22 = 0.0 |
|  | 40¢ | 16 | ×0.3^26 = 0.0 |
|  | 45¢ | 25 | ×0.3^31 = 0.0 |
|  | 99¢ | 10,147 | ×0.3^85 = 0.0 |
| | | **Σ** | **69.8** |

`yours 10.0 / Σ 69.8 = 14.3%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 14.3% = $1.79/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> SELL 171 @ 11¢ → $2.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 171 (171 yours) | ×0.3^0 = 171.0 |
|  | 14¢ | 43,824 | ×0.3^3 = 1,183.2 |
| | | **Σ** | **1,354.2** |

`yours 171.0 / Σ 1,354.2 = 12.6%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 12.6% = $2.63/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> BUY 100 @ 30¢ → $1.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 813 (100 yours) | ×0.3^0 = 813.0 |
|  | 24¢ | 6 | ×0.3^6 = 0.0 |
|  | 22¢ | 28 | ×0.3^8 = 0.0 |
|  | 1¢ | 10,060 | ×0.3^29 = 0.0 |
| | | **Σ** | **813.0** |

`yours 100.0 / Σ 813.0 = 12.3%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 12.3% = $1.54/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> BUY 100 @ 21¢ → $1.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 926 (100 yours) | ×0.3^0 = 926.0 |
|  | 15¢ | 6 | ×0.3^6 = 0.0 |
|  | 13¢ | 28 | ×0.3^8 = 0.0 |
|  | 1¢ | 10,025 | ×0.3^20 = 0.0 |
| | | **Σ** | **926.0** |

`yours 100.0 / Σ 926.0 = 10.8%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 10.8% = $1.35/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 100 @ 23¢ → $1.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 24¢ | 92 | ×0.3^0 = 92.0 |
| ▶ | 23¢ | 926 (100 yours) | ×0.3^1 = 277.8 |
|  | 5¢ | 25 | ×0.3^19 = 0.0 |
|  | 1¢ | 10,000 | ×0.3^23 = 0.0 |
| | | **Σ** | **369.8** |

`yours 30.0 / Σ 369.8 = 8.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 8.1% = $1.01/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 26¢ → $2.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 25¢ | 249 | ×0.3^0 = 249.0 |
| ▶ | 26¢ | 1,020 (100 yours) | ×0.3^1 = 305.9 |
|  | 33¢ | 28 | ×0.3^8 = 0.0 |
|  | 51¢ | 250 | ×0.3^26 = 0.0 |
|  | 99¢ | 10,740 | ×0.3^74 = 0.0 |
| | | **Σ** | **554.9** |

`yours 30.0 / Σ 554.9 = 5.4%`  
`$250 ÷ 3 ÷ 2 = $41.67 × 5.4% = $2.25/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-alito-2026-07-31`
2. `apdc-alito-2026-08-31`
3. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-frahon</code> BUY 50 @ 73¢ → $0.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 73¢ | 573 (50 yours) | ×0.3^0 = 573.0 |
|  | 70¢ | 24,455 | ×0.3^3 = 660.3 |
| | | **Σ** | **1,233.3** |

`yours 50.0 / Σ 1,233.3 = 4.1%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 4.1% = $0.84/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon` ← this one
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-frahon</code> BUY 50 @ 73¢ → $0.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 73¢ | 573 (50 yours) | ×0.3^0 = 573.0 |
|  | 70¢ | 24,455 | ×0.3^3 = 660.3 |
| | | **Σ** | **1,233.3** |

`yours 50.0 / Σ 1,233.3 = 4.1%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 4.1% = $0.84/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon` ← this one
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> BUY 10,000 @ 1¢ → $0.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 541 | ×0.3^0 = 541.0 |
|  | 5¢ | 1,000 | ×0.3^1 = 300.0 |
| ▶ | 1¢ | 20,000 (10,000 yours) | ×0.3^5 = 48.6 |
| | | **Σ** | **889.6** |

`yours 24.3 / Σ 889.6 = 2.7%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 2.7% = $0.28/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor` ← this one
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 10 @ 20¢ → $0.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 688 (10 yours) | ×0.3^0 = 688.0 |
|  | 14¢ | 6 | ×0.3^6 = 0.0 |
|  | 12¢ | 28 | ×0.3^8 = 0.0 |
|  | 1¢ | 10,025 | ×0.3^19 = 0.0 |
| | | **Σ** | **688.0** |

`yours 10.0 / Σ 688.0 = 1.5%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 1.5% = $0.18/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 100 @ 18¢ → $0.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 66 | ×0.3^0 = 66.0 |
|  | 16¢ | 15 | ×0.3^2 = 1.3 |
|  | 17¢ | 56 | ×0.3^3 = 1.5 |
| ▶ | 18¢ | 100 (100 yours) | ×0.3^4 = 0.8 |
|  | 21¢ | 529 | ×0.3^7 = 0.1 |
|  | 36¢ | 101 | ×0.3^22 = 0.0 |
|  | 40¢ | 16 | ×0.3^26 = 0.0 |
|  | 45¢ | 25 | ×0.3^31 = 0.0 |
|  | 99¢ | 10,147 | ×0.3^85 = 0.0 |
| | | **Σ** | **69.8** |

`yours 0.8 / Σ 69.8 = 1.2%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 1.2% = $0.15/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> BUY 290 @ 8¢ → $0.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 723 | ×0.3^0 = 723.0 |
|  | 9¢ | 87 | ×0.3^2 = 7.8 |
| ▶ | 8¢ | 766 (290 yours) | ×0.3^3 = 20.7 |
|  | 1¢ | 10,275 | ×0.3^10 = 0.1 |
| | | **Σ** | **751.6** |

`yours 7.8 / Σ 751.6 = 1.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 1.0% = $0.13/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> BUY 205 @ 1¢ → $0.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 3,034 | ×0.3^0 = 3,034.0 |
| ▶ | 1¢ | 12,730 (205 yours) | ×0.3^1 = 3,819.0 |
| | | **Σ** | **6,853.0** |

`yours 61.5 / Σ 6,853.0 = 0.9%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.9% = $0.11/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-21 | ~$87.94 | $91.44 | 104% |
| 2026-07-20 | ~$125.00 | $106.54 | 85% |
| 2026-07-19 | ~$36.97 | $35.81 | 97% |

Biggest gaps on 2026-07-21: `apdc-alito-2026-08-31` (est ~$2.10 → got $0.00), `enwc-ussep-sc-2026-08-11-rep-darnor` (est ~$2.07 → got $0.00), `enwc-ushrp-mo01-2026-08-04-dem-corbus` (est ~$1.84 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (10,724 resting) | ~67.7% | ~$42.31 |
| `apdc-jerpowgov-2026-12-31` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (11,100 resting) | ~70.5% | ~$29.38 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (11,217 resting) | ~45.8% | ~$28.60 |
| `ewc-usgub-ks-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (165,065 resting) | ~32.5% | ~$20.32 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (44,481 resting) | ~30.0% | ~$12.50 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (64,147 resting) | ~12.7% | ~$7.96 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (94,386 resting) | ~7.9% | ~$4.95 |
| `apdc-jerpowgov-2026-07-31` | $250.00 ÷ 3 | 0.30 | 10,000 | SELL side (18,874 resting) | ~8.8% | ~$3.68 |
| `ewc-usgub-ga-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (121,920 resting) | ~5.5% | ~$3.44 |
| `ewc-usgub-ks-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (247,783 resting) | ~5.3% | ~$3.31 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (58,824 resting) | ~4.9% | ~$3.09 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (66,227 resting) | ~4.0% | ~$2.53 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $233.79 |
| Skipped | $1.21 |
| **Total earned** | **$390.84** |

211 reward rows · 19 days with rewards · 71 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-21 | $91.44 | `█████████████████` |
| 2026-07-20 | $106.54 | `████████████████████` |
| 2026-07-19 | $35.81 | `███████` |
| 2026-07-18 | $44.41 | `████████` |
| 2026-07-17 | $14.71 | `███` |
| 2026-07-16 | $17.02 | `███` |
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `██` |
| 2026-07-13 | $10.03 | `██` |
| 2026-07-12 | $39.90 | `███████` |
| 2026-07-11 | $2.11 | `█` |
| 2026-07-10 | $2.16 | `█` |
| 2026-07-09 | $4.72 | `█` |
| 2026-07-08 | $2.68 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $390.84 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-ussep-nh-2026-09-08-dem-karman` | $43.94 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $41.68 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $29.71 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $18.83 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $18.02 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $17.30 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.58 |
| `apdc-jerpowgov-2026-12-31` | $14.76 |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | $13.18 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $12.14 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $8.81 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $7.85 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $7.79 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $7.13 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-23 2:42 AM ET | ✅ ok | 211 | $390.84 |
| 2026-07-22 11:48 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-22 10:01 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-22 9:30 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-22 9:16 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-22 9:10 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-22 9:09 PM ET | ✅ ok | 201 | $361.69 |
| 2026-07-22 9:02 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 8:15 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 7:18 PM ET | ✅ ok | 186 | $299.40 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
