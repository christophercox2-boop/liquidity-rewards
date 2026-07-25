# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-25 3:48 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$118.18/day estimated (ceiling, not promise — details below)

**Earned:** $701.42 lifetime ($155.84 paid). Last three recorded days — 2026-07-23: **$227.63** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-22: **$82.95** · 2026-07-21: **$91.44** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — SELL at the best price, ~$8.94/day for 200 contracts. Runners-up: `ewc-usgub-ks-2026-11-03-dem` (~$2.46/day), `ewc-usgub-oh-2026-11-03-rep` (~$2.44/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$118.18/day (~$4.92/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $8.33/day (pool ÷ 6 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | BUY | 1.0¢ | 1,986 | 0 | $100.00 | ✅ scoring — ~90.6% of bid side (2,192 resting ≥ 2,000 ✓) ≈ $3.78/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-tregow` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~88.9% of bid side (2,250 resting ≥ 2,000 ✓) ≈ $3.70/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~80.0% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $3.33/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~74.7% of bid side (2,678 resting ≥ 2,000 ✓) ≈ $3.11/day (pool ÷ 12 markets) |
| `iarc-group-2026-12-31-tuccar` | BUY | 1.0¢ | 2,000 | 2 | $100.00 | ✅ scoring — ~71.7% of bid side (2,486 resting ≥ 2,000 ✓) ≈ $3.59/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 5.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~48.8% of ask side (39,514 resting ≥ 2,000 ✓) ≈ $2.44/day (pool ÷ 10 markets) |
| `mlaec-swepm-2026-09-13-magand` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~46.6% of bid side (4,290 resting ≥ 2,000 ✓) ≈ $4.66/day (pool ÷ 5 markets) |
| `cranc-uspres28-12-31-2026-robken` | BUY | 11.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~44.7% of bid side (70,380 resting ≥ 2,000 ✓) ≈ $0.68/day (pool ÷ 33 markets) |
| `mowc-nato-us-12-31-2026` | SELL | 10.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~43.5% of ask side (42,485 resting ≥ 2,000 ✓) ≈ $10.87/day (pool ÷ 2 markets) |
| `nphc-attgen-jefjen` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~43.2% of bid side (4,628 resting ≥ 2,000 ✓) ≈ $1.35/day (pool ÷ 16 markets) |
| `nphc-attgen-matwhi` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~40.4% of bid side (4,950 resting ≥ 2,000 ✓) ≈ $1.26/day (pool ÷ 16 markets) |
| `mlaec-swepm-2026-09-13-noodad` | BUY | 1.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~38.8% of bid side (2,576 resting ≥ 2,000 ✓) ≈ $3.88/day (pool ÷ 5 markets) |
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~34.1% of bid side (5,867 resting ≥ 2,000 ✓) ≈ $1.42/day (pool ÷ 12 markets) |
| `mlaec-swepm-2026-09-13-jimake` | BUY | 1.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~33.7% of bid side (2,966 resting ≥ 2,000 ✓) ≈ $3.37/day (pool ÷ 5 markets) |
| `lawec-saveact-2026-12-31` | BUY | 12.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~32.6% of bid side (38,105 resting ≥ 2,000 ✓) ≈ $8.15/day (pool ÷ 2 markets) |
| `mlaec-swepm-2026-09-13-ulfkri` | BUY | 1.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~32.4% of bid side (3,086 resting ≥ 2,000 ✓) ≈ $3.24/day (pool ÷ 5 markets) |
| `enwc-usgubp-fl-2026-08-18-rep-jaycol` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~30.7% of bid side (6,509 resting ≥ 2,000 ✓) ≈ $5.12/day (pool ÷ 3 markets) |
| `enwc-ussep-sc-2026-08-11-rep-alawil` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~29.6% of bid side (6,762 resting ≥ 2,000 ✓) ≈ $1.23/day (pool ÷ 12 markets) |
| `ewc-pres-fra-2027-04-11-frahol` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~28.3% of bid side (29,214 resting ≥ 2,000 ✓) ≈ $1.29/day (pool ÷ 11 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~23.8% of bid side (8,395 resting ≥ 2,000 ✓) ≈ $1.99/day (pool ÷ 6 markets) |
| `pintc-meet-trump-2026-12-31-kimjon` | BUY | 6.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~23.1% of bid side (10,331 resting ≥ 2,000 ✓) ≈ $0.89/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~21.7% of bid side (9,235 resting ≥ 2,000 ✓) ≈ $0.90/day (pool ÷ 12 markets) |
| `cranc-uspres28-12-31-2026-bersan` | BUY | 7.0¢ | 200 | 0 | $100.00 | ✅ scoring — ~19.2% of bid side (23,488 resting ≥ 2,000 ✓) ≈ $0.29/day (pool ÷ 33 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 93.0¢ | 78 | 0 | $100.00 | ✅ scoring — ~19.1% of ask side (2,969 resting ≥ 2,000 ✓) ≈ $0.80/day (pool ÷ 12 markets) |
| `nphc-attgen-rondes` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~18.6% of bid side (2,895 resting ≥ 2,000 ✓) ≈ $0.58/day (pool ÷ 16 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 25.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~17.8% of ask side (91,548 resting ≥ 2,000 ✓) ≈ $0.69/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-zohmam` | BUY | 8.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~17.5% of bid side (32,566 resting ≥ 2,000 ✓) ≈ $0.26/day (pool ÷ 33 markets) |
| `nphc-attgen-kenpax` | BUY | 1.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~16.9% of bid side (2,950 resting ≥ 2,000 ✓) ≈ $0.53/day (pool ÷ 16 markets) |
| …and 139 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-sarrod</code> BUY 2,000 @ 1¢ → $8.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.5^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$100 ÷ 6 ÷ 2 = $8.33 × 100.0% = $8.33/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> BUY 2,000 @ 1¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.5^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> BUY 1,986 @ 1¢ → $3.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,192 (1,986 yours) | ×0.5^0 = 2,191.5 |
| | | **Σ** | **2,191.5** |

`yours 1,985.5 / Σ 2,191.5 = 90.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 90.6% = $3.78/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil` ← this one
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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-tregow</code> BUY 2,000 @ 1¢ → $3.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,250 (2,000 yours) | ×0.5^0 = 2,250.0 |
| | | **Σ** | **2,250.0** |

`yours 2,000.0 / Σ 2,250.0 = 88.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 88.9% = $3.70/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-paudan</code> BUY 2,000 @ 1¢ → $3.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,500 (2,000 yours) | ×0.5^0 = 2,500.0 |
| | | **Σ** | **2,500.0** |

`yours 2,000.0 / Σ 2,500.0 = 80.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 80.0% = $3.33/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan` ← this one
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-andbau</code> BUY 2,000 @ 1¢ → $3.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,678 (2,000 yours) | ×0.5^0 = 2,678.0 |
| | | **Σ** | **2,678.0** |

`yours 2,000.0 / Σ 2,678.0 = 74.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 74.7% = $3.11/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau` ← this one
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
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
<details><summary><code>iarc-group-2026-12-31-tuccar</code> BUY 2,000 @ 1¢ → $3.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 8 | ×0.5^0 = 8.0 |
|  | 2¢ | 278 | ×0.5^1 = 139.0 |
| ▶ | 1¢ | 2,200 (2,000 yours) | ×0.5^2 = 550.0 |
| | | **Σ** | **697.0** |

`yours 500.0 / Σ 697.0 = 71.7%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 71.7% = $3.59/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `iarc-group-2026-12-31-antfau`
2. `iarc-group-2026-12-31-baroba`
3. `iarc-group-2026-12-31-bilcli`
4. `iarc-group-2026-12-31-canowe`
5. `iarc-group-2026-12-31-gavnew`
6. `iarc-group-2026-12-31-hilcli`
7. `iarc-group-2026-12-31-joebid`
8. `iarc-group-2026-12-31-johbre`
9. `iarc-group-2026-12-31-tomhom`
10. `iarc-group-2026-12-31-tuccar` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 5¢ → $2.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 2 (1 yours) | ×0.5^0 = 1.5 |
|  | 11¢ | 34 | ×0.5^6 = 0.5 |
|  | 43¢ | 2,000 | ×0.5^38 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 48.8%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 48.8% = $2.44/day`  

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
<details><summary><code>mlaec-swepm-2026-09-13-magand</code> BUY 2,000 @ 1¢ → $4.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,290 (2,000 yours) | ×0.5^0 = 4,290.0 |
| | | **Σ** | **4,290.0** |

`yours 2,000.0 / Σ 4,290.0 = 46.6%`  
`$100 ÷ 5 ÷ 2 = $10.00 × 46.6% = $4.66/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `mlaec-swepm-2026-09-13-ebbbus`
2. `mlaec-swepm-2026-09-13-jimake`
3. `mlaec-swepm-2026-09-13-magand` ← this one
4. `mlaec-swepm-2026-09-13-noodad`
5. `mlaec-swepm-2026-09-13-ulfkri`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-robken</code> BUY 100 @ 11¢ → $0.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 151 (100 yours) | ×0.5^0 = 151.0 |
|  | 9¢ | 16 | ×0.5^2 = 4.0 |
|  | 6¢ | 6 | ×0.5^5 = 0.2 |
|  | 1¢ | 70,207 | ×0.5^10 = 68.6 |
| | | **Σ** | **223.7** |

`yours 100.0 / Σ 223.7 = 44.7%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 44.7% = $0.68/day`  

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
15. `cranc-uspres28-12-31-2026-jonoss`
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
27. `cranc-uspres28-12-31-2026-robken` ← this one
28. `cranc-uspres28-12-31-2026-steban`
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>mowc-nato-us-12-31-2026</code> SELL 100 @ 10¢ → $10.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 100 (100 yours) | ×0.5^0 = 100.2 |
|  | 11¢ | 227 | ×0.5^1 = 113.5 |
|  | 20¢ | 68 | ×0.5^10 = 0.1 |
|  | 21¢ | 33,234 | ×0.5^11 = 16.2 |
| | | **Σ** | **230.0** |

`yours 100.0 / Σ 230.0 = 43.5%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 43.5% = $10.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `mowc-nato-us-07-31-2026`
2. `mowc-nato-us-12-31-2026` ← this one

</details>

</details>
<details><summary><code>nphc-attgen-jefjen</code> BUY 2,000 @ 1¢ → $1.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,628 (2,000 yours) | ×0.5^0 = 4,628.0 |
| | | **Σ** | **4,628.0** |

`yours 2,000.0 / Σ 4,628.0 = 43.2%`  
`$100 ÷ 16 ÷ 2 = $3.12 × 43.2% = $1.35/day`  

<details><summary>÷ 16 markets in this race — tap to list</summary>

1. `nphc-attgen-ailcan`
2. `nphc-attgen-alihab`
3. `nphc-attgen-andbai`
4. `nphc-attgen-ashmoo`
5. `nphc-attgen-edmar`
6. `nphc-attgen-hardhi`
7. `nphc-attgen-jeapir`
8. `nphc-attgen-jefjen` ← this one
9. `nphc-attgen-kenpax`
10. `nphc-attgen-leezel`
11. `nphc-attgen-matgae`
12. `nphc-attgen-matwhi`
13. `nphc-attgen-robgiu`
14. `nphc-attgen-rondes`
15. `nphc-attgen-tedcru`
16. `nphc-attgen-todbla`

</details>

</details>
<details><summary><code>nphc-attgen-matwhi</code> BUY 2,000 @ 1¢ → $1.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,950 (2,000 yours) | ×0.5^0 = 4,950.0 |
| | | **Σ** | **4,950.0** |

`yours 2,000.0 / Σ 4,950.0 = 40.4%`  
`$100 ÷ 16 ÷ 2 = $3.12 × 40.4% = $1.26/day`  

<details><summary>÷ 16 markets in this race — tap to list</summary>

1. `nphc-attgen-ailcan`
2. `nphc-attgen-alihab`
3. `nphc-attgen-andbai`
4. `nphc-attgen-ashmoo`
5. `nphc-attgen-edmar`
6. `nphc-attgen-hardhi`
7. `nphc-attgen-jeapir`
8. `nphc-attgen-jefjen`
9. `nphc-attgen-kenpax`
10. `nphc-attgen-leezel`
11. `nphc-attgen-matgae`
12. `nphc-attgen-matwhi` ← this one
13. `nphc-attgen-robgiu`
14. `nphc-attgen-rondes`
15. `nphc-attgen-tedcru`
16. `nphc-attgen-todbla`

</details>

</details>
<details><summary><code>mlaec-swepm-2026-09-13-noodad</code> BUY 1,000 @ 1¢ → $3.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,576 (1,000 yours) | ×0.5^0 = 2,576.0 |
| | | **Σ** | **2,576.0** |

`yours 1,000.0 / Σ 2,576.0 = 38.8%`  
`$100 ÷ 5 ÷ 2 = $10.00 × 38.8% = $3.88/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `mlaec-swepm-2026-09-13-ebbbus`
2. `mlaec-swepm-2026-09-13-jimake`
3. `mlaec-swepm-2026-09-13-magand`
4. `mlaec-swepm-2026-09-13-noodad` ← this one
5. `mlaec-swepm-2026-09-13-ulfkri`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-wiltim</code> BUY 2,000 @ 1¢ → $1.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,867 (2,000 yours) | ×0.5^0 = 5,867.0 |
| | | **Σ** | **5,867.0** |

`yours 2,000.0 / Σ 5,867.0 = 34.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 34.1% = $1.42/day`  

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
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim` ← this one

</details>

</details>
<details><summary><code>mlaec-swepm-2026-09-13-jimake</code> BUY 1,000 @ 1¢ → $3.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,966 (1,000 yours) | ×0.5^0 = 2,966.0 |
| | | **Σ** | **2,966.0** |

`yours 1,000.0 / Σ 2,966.0 = 33.7%`  
`$100 ÷ 5 ÷ 2 = $10.00 × 33.7% = $3.37/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `mlaec-swepm-2026-09-13-ebbbus`
2. `mlaec-swepm-2026-09-13-jimake` ← this one
3. `mlaec-swepm-2026-09-13-magand`
4. `mlaec-swepm-2026-09-13-noodad`
5. `mlaec-swepm-2026-09-13-ulfkri`

</details>

</details>
<details><summary><code>lawec-saveact-2026-12-31</code> BUY 100 @ 12¢ → $8.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 246 (100 yours) | ×0.5^0 = 246.0 |
|  | 10¢ | 10 | ×0.5^2 = 2.5 |
|  | 9¢ | 29 | ×0.5^3 = 3.6 |
|  | 8¢ | 831 | ×0.5^4 = 51.9 |
|  | 3¢ | 1,442 | ×0.5^9 = 2.8 |
| | | **Σ** | **306.9** |

`yours 100.0 / Σ 306.9 = 32.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 32.6% = $8.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-saveact-2026-08-31`
2. `lawec-saveact-2026-12-31` ← this one

</details>

</details>
<details><summary><code>mlaec-swepm-2026-09-13-ulfkri</code> BUY 1,000 @ 1¢ → $3.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,086 (1,000 yours) | ×0.5^0 = 3,086.0 |
| | | **Σ** | **3,086.0** |

`yours 1,000.0 / Σ 3,086.0 = 32.4%`  
`$100 ÷ 5 ÷ 2 = $10.00 × 32.4% = $3.24/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `mlaec-swepm-2026-09-13-ebbbus`
2. `mlaec-swepm-2026-09-13-jimake`
3. `mlaec-swepm-2026-09-13-magand`
4. `mlaec-swepm-2026-09-13-noodad`
5. `mlaec-swepm-2026-09-13-ulfkri` ← this one

</details>

</details>
<details><summary><code>enwc-usgubp-fl-2026-08-18-rep-jaycol</code> BUY 2,000 @ 1¢ → $5.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 6,509 (2,000 yours) | ×0.5^0 = 6,509.0 |
| | | **Σ** | **6,509.0** |

`yours 2,000.0 / Σ 6,509.0 = 30.7%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 30.7% = $5.12/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `enwc-usgubp-fl-2026-08-18-rep-byrdon`
2. `enwc-usgubp-fl-2026-08-18-rep-jamfis`
3. `enwc-usgubp-fl-2026-08-18-rep-jaycol` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-alawil</code> BUY 2,000 @ 1¢ → $1.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 6,762 (2,000 yours) | ×0.5^0 = 6,762.0 |
| | | **Σ** | **6,762.0** |

`yours 2,000.0 / Σ 6,762.0 = 29.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 29.6% = $1.23/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil` ← this one
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
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
<details><summary><code>ewc-pres-fra-2027-04-11-frahol</code> BUY 1,000 @ 2¢ → $1.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 3,534 (1,000 yours) | ×0.5^0 = 3,534.0 |
| | | **Σ** | **3,534.0** |

`yours 1,000.0 / Σ 3,534.0 = 28.3%`  
`$100 ÷ 11 ÷ 2 = $4.55 × 28.3% = $1.29/day`  

<details><summary>÷ 11 markets in this race — tap to list</summary>

1. `ewc-pres-fra-2027-04-11-bruret`
2. `ewc-pres-fra-2027-04-11-davlis`
3. `ewc-pres-fra-2027-04-11-domvil`
4. `ewc-pres-fra-2027-04-11-edophi`
5. `ewc-pres-fra-2027-04-11-frahol` ← this one
6. `ewc-pres-fra-2027-04-11-gabatt`
7. `ewc-pres-fra-2027-04-11-jeamel`
8. `ewc-pres-fra-2027-04-11-jorbar`
9. `ewc-pres-fra-2027-04-11-marlep`
10. `ewc-pres-fra-2027-04-11-rapglu`
11. `ewc-pres-fra-2027-04-11-sarkna`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 2,000 @ 1¢ → $1.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 8,395 (2,000 yours) | ×0.5^0 = 8,395.0 |
| | | **Σ** | **8,395.0** |

`yours 2,000.0 / Σ 8,395.0 = 23.8%`  
`$100 ÷ 6 ÷ 2 = $8.33 × 23.8% = $1.99/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>pintc-meet-trump-2026-12-31-kimjon</code> BUY 100 @ 6¢ → $0.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 114 (100 yours) | ×0.5^0 = 114.0 |
|  | 1¢ | 10,217 | ×0.5^5 = 319.3 |
| | | **Σ** | **433.3** |

`yours 100.0 / Σ 433.3 = 23.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 23.1% = $0.89/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon` ← this one
6. `pintc-meet-trump-2026-12-31-kimkar`
7. `pintc-meet-trump-2026-12-31-leoxiv`
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput`
11. `pintc-meet-trump-2026-12-31-volzel`
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-nanmac</code> BUY 2,000 @ 1¢ → $0.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 9,235 (2,000 yours) | ×0.5^0 = 9,235.0 |
| | | **Σ** | **9,235.0** |

`yours 2,000.0 / Σ 9,235.0 = 21.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 21.7% = $0.90/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac` ← this one
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-bersan</code> BUY 200 @ 7¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 640 (200 yours) | ×0.5^0 = 640.0 |
|  | 5¢ | 145 | ×0.5^2 = 36.2 |
|  | 3¢ | 202 | ×0.5^4 = 12.6 |
|  | 1¢ | 22,501 | ×0.5^6 = 351.6 |
| | | **Σ** | **1,040.5** |

`yours 200.0 / Σ 1,040.5 = 19.2%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 19.2% = $0.29/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan` ← this one
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
15. `cranc-uspres28-12-31-2026-jonoss`
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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 78 @ 93¢ → $0.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 341 (78 yours) | ×0.5^0 = 340.8 |
|  | 97¢ | 542 | ×0.5^4 = 33.9 |
|  | 99¢ | 2,086 | ×0.5^6 = 32.6 |
| | | **Σ** | **407.3** |

`yours 77.8 / Σ 407.3 = 19.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.1% = $0.80/day`  

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
<details><summary><code>nphc-attgen-rondes</code> BUY 500 @ 3¢ → $0.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 2,695 (500 yours) | ×0.5^0 = 2,695.0 |
| | | **Σ** | **2,695.0** |

`yours 500.0 / Σ 2,695.0 = 18.6%`  
`$100 ÷ 16 ÷ 2 = $3.12 × 18.6% = $0.58/day`  

<details><summary>÷ 16 markets in this race — tap to list</summary>

1. `nphc-attgen-ailcan`
2. `nphc-attgen-alihab`
3. `nphc-attgen-andbai`
4. `nphc-attgen-ashmoo`
5. `nphc-attgen-edmar`
6. `nphc-attgen-hardhi`
7. `nphc-attgen-jeapir`
8. `nphc-attgen-jefjen`
9. `nphc-attgen-kenpax`
10. `nphc-attgen-leezel`
11. `nphc-attgen-matgae`
12. `nphc-attgen-matwhi`
13. `nphc-attgen-robgiu`
14. `nphc-attgen-rondes` ← this one
15. `nphc-attgen-tedcru`
16. `nphc-attgen-todbla`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 100 @ 25¢ → $0.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 561 (100 yours) | ×0.5^0 = 561.0 |
|  | 50¢ | 100 | ×0.5^25 = 0.0 |
|  | 97¢ | 38,892 | ×0.5^72 = 0.0 |
| | | **Σ** | **561.0** |

`yours 100.0 / Σ 561.0 = 17.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.8% = $0.69/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-zohmam</code> BUY 100 @ 8¢ → $0.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 196 (100 yours) | ×0.5^0 = 196.0 |
|  | 7¢ | 250 | ×0.5^1 = 125.0 |
|  | 1¢ | 32,120 | ×0.5^7 = 250.9 |
| | | **Σ** | **571.9** |

`yours 100.0 / Σ 571.9 = 17.5%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 17.5% = $0.26/day`  

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
15. `cranc-uspres28-12-31-2026-jonoss`
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
33. `cranc-uspres28-12-31-2026-zohmam` ← this one

</details>

</details>
<details><summary><code>nphc-attgen-kenpax</code> BUY 500 @ 1¢ → $0.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,950 (500 yours) | ×0.5^0 = 2,950.0 |
| | | **Σ** | **2,950.0** |

`yours 500.0 / Σ 2,950.0 = 16.9%`  
`$100 ÷ 16 ÷ 2 = $3.12 × 16.9% = $0.53/day`  

<details><summary>÷ 16 markets in this race — tap to list</summary>

1. `nphc-attgen-ailcan`
2. `nphc-attgen-alihab`
3. `nphc-attgen-andbai`
4. `nphc-attgen-ashmoo`
5. `nphc-attgen-edmar`
6. `nphc-attgen-hardhi`
7. `nphc-attgen-jeapir`
8. `nphc-attgen-jefjen`
9. `nphc-attgen-kenpax` ← this one
10. `nphc-attgen-leezel`
11. `nphc-attgen-matgae`
12. `nphc-attgen-matwhi`
13. `nphc-attgen-robgiu`
14. `nphc-attgen-rondes`
15. `nphc-attgen-tedcru`
16. `nphc-attgen-todbla`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-22 | ~$110.63 | $82.95 | 75% |
| 2026-07-21 | ~$87.94 | $91.44 | 104% |
| 2026-07-20 | ~$125.00 | $106.54 | 85% |

Biggest gaps on 2026-07-22: `apdc-alito-2026-12-31` (est ~$6.62 → got $0.00), `vmc-ussep-misen-2026-08-04-els0-5` (est ~$6.70 → got $1.57), `stsc-bab-el-mandeb-clsd-2026-12-31` (est ~$2.85 → got $0.00)

_2026-07-23 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (64,807 resting) | ~35.8% | ~$8.94 |
| `ewc-usgub-ks-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (107,118 resting) | ~9.8% | ~$2.46 |
| `ewc-usgub-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (47,708 resting) | ~9.8% | ~$2.44 |
| `ewc-usgub-wi-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (67,105 resting) | ~9.1% | ~$2.27 |
| `ewc-usgub-ia-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (47,248 resting) | ~9.0% | ~$2.25 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (27,282 resting) | ~9.0% | ~$2.24 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (33,537 resting) | ~8.4% | ~$2.10 |
| `ewc-usse-ia-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (170,459 resting) | ~7.2% | ~$1.81 |
| `ewc-usgub-az-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (71,560 resting) | ~6.9% | ~$1.72 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (74,665 resting) | ~5.1% | ~$1.26 |
| `ewc-usgub-az-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (64,570 resting) | ~4.9% | ~$1.23 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $100.00 ÷ 3 | 0.50 | 2,000 | BUY side (164,130 resting) | ~6.7% | ~$1.11 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $544.37 |
| Skipped | $1.21 |
| **Total earned** | **$701.42** |

282 reward rows · 21 days with rewards · 103 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-23 ⚠️ multi-day pending bucket | $227.63 | `████████████████████` |
| 2026-07-22 | $82.95 | `███████` |
| 2026-07-21 | $91.44 | `████████` |
| 2026-07-20 | $106.54 | `█████████` |
| 2026-07-19 | $35.81 | `███` |
| 2026-07-18 | $44.41 | `████` |
| 2026-07-17 | $14.71 | `█` |
| 2026-07-16 | $17.02 | `█` |
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `█` |
| 2026-07-13 | $10.03 | `█` |
| 2026-07-12 | $39.90 | `████` |
| 2026-07-11 | $2.11 | `█` |
| 2026-07-10 | $2.16 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $701.42 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $57.09 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $43.94 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $36.97 |
| `apdc-jerpowgov-2026-12-31` | $35.01 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $31.28 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.61 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $24.38 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $21.69 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $19.67 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $19.58 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $18.02 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $17.71 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $17.30 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-25 3:48 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 3:38 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 3:35 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 2:59 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 2:48 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 2:12 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 2:06 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 1:47 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 1:18 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 12:57 PM ET | ✅ ok | 282 | $701.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
