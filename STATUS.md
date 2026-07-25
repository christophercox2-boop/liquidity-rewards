# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-25 1:18 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$78.79/day estimated (ceiling, not promise — details below)

**Earned:** $701.42 lifetime ($155.84 paid). Last three recorded days — 2026-07-23: **$227.63** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-22: **$82.95** · 2026-07-21: **$91.44** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — BUY at the best price, ~$7.58/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$2.99/day), `ewc-usgub-wi-2026-11-03-dem` (~$2.85/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$78.79/day (~$3.28/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 2.0¢ | 2,001 | 0 | $100.00 | ✅ scoring — ~85.0% of bid side (8,407 resting ≥ 2,000 ✓) ≈ $4.25/day (pool ÷ 10 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 34.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~68.5% of bid side (10,847 resting ≥ 2,000 ✓) ≈ $34.23/day |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 5.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~65.8% of ask side (39,524 resting ≥ 2,000 ✓) ≈ $3.29/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 2.0¢ | 400 | 0 | $100.00 | ✅ scoring — ~59.8% of ask side (4,238 resting ≥ 2,000 ✓) ≈ $2.49/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~48.5% of bid side (4,125 resting ≥ 2,000 ✓) ≈ $2.02/day (pool ÷ 12 markets) |
| `iarc-group-2026-12-31-tuccar` | BUY | 1.0¢ | 2,000 | 2 | $100.00 | ✅ scoring — ~48.2% of bid side (3,171 resting ≥ 2,000 ✓) ≈ $2.41/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~44.4% of bid side (4,500 resting ≥ 2,000 ✓) ≈ $1.85/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 34.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~41.5% of ask side (99,559 resting ≥ 2,000 ✓) ≈ $2.08/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~38.6% of bid side (5,181 resting ≥ 2,000 ✓) ≈ $1.61/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~36.0% of bid side (5,549 resting ≥ 2,000 ✓) ≈ $1.50/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 93.0¢ | 78 | 1 | $100.00 | ✅ scoring — ~35.8% of ask side (3,184 resting ≥ 2,000 ✓) ≈ $1.49/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 25.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~25.1% of ask side (91,430 resting ≥ 2,000 ✓) ≈ $0.96/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 20.0¢ | 86 | 0 | $100.00 | ✅ scoring — ~23.6% of ask side (6,144 resting ≥ 2,000 ✓) ≈ $0.98/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~19.3% of bid side (10,362 resting ≥ 2,000 ✓) ≈ $0.80/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 12.0¢ | 200 | 0 | $100.00 | ✅ scoring — ~19.1% of bid side (202,419 resting ≥ 2,000 ✓) ≈ $0.74/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 18.0¢ | 200 | 0 | $100.00 | ✅ scoring — ~17.2% of bid side (201,358 resting ≥ 2,000 ✓) ≈ $0.66/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~13.4% of bid side (14,950 resting ≥ 2,000 ✓) ≈ $0.51/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 34.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~12.5% of ask side (99,559 resting ≥ 2,000 ✓) ≈ $0.62/day (pool ÷ 10 markets) |
| `enwc-usgubp-fl-2026-08-18-rep-jaycol` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~12.3% of bid side (16,211 resting ≥ 2,000 ✓) ≈ $2.06/day (pool ÷ 3 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | BUY | 2.0¢ | 2,001 | 5 | $100.00 | ✅ scoring — ~10.8% of bid side (9,501 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 10 markets) |
| `stsc-bab-el-mandeb-clsd-2026-07-31` | BUY | 6.0¢ | 500 | 0 | $250.00 | ✅ scoring — ~9.4% of bid side (6,553 resting ≥ 2,000 ✓) ≈ $3.92/day (pool ÷ 3 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | BUY | 1.0¢ | 2,000 | 7 | $100.00 | ✅ scoring — ~5.0% of bid side (5,710 resting ≥ 2,000 ✓) ≈ $0.21/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 5 | $100.00 | ✅ scoring — ~3.9% of ask side (3,184 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 5 | $100.00 | ✅ scoring — ~3.9% of ask side (3,184 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 5 | $100.00 | ✅ scoring — ~3.9% of ask side (3,184 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 5 | $100.00 | ✅ scoring — ~3.9% of ask side (3,184 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 5 | $100.00 | ✅ scoring — ~3.9% of ask side (3,184 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 5 | $100.00 | ✅ scoring — ~3.9% of ask side (3,184 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 5 | $100.00 | ✅ scoring — ~3.9% of ask side (3,184 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 5 | $100.00 | ✅ scoring — ~3.9% of ask side (3,184 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 12 markets) |
| …and 67 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 2,001 @ 2¢ → $4.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 2,355 (2,001 yours) | ×0.5^0 = 2,355.0 |
| | | **Σ** | **2,355.0** |

`yours 2,001.0 / Σ 2,355.0 = 85.0%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 85.0% = $4.25/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 100 @ 34¢ → $34.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 35¢ | 23 | ×0.5^0 = 23.0 |
| ▶ | 34¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 27¢ | 9 | ×0.5^8 = 0.0 |
|  | 19¢ | 515 | ×0.5^16 = 0.0 |
|  | 2¢ | 10,000 | ×0.5^33 = 0.0 |
| | | **Σ** | **73.0** |

`yours 50.0 / Σ 73.0 = 68.5%`  
`$100 ÷ 1 ÷ 2 = $50.00 × 68.5% = $34.23/day`  

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 5¢ → $3.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 2 (1 yours) | ×0.5^0 = 1.5 |
|  | 43¢ | 2,000 | ×0.5^38 = 0.0 |
| | | **Σ** | **1.5** |

`yours 1.0 / Σ 1.5 = 65.8%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 65.8% = $3.29/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 400 @ 2¢ → $2.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 669 (400 yours) | ×0.5^0 = 669.0 |
|  | 50¢ | 25 | ×0.5^48 = 0.0 |
|  | 55¢ | 44 | ×0.5^53 = 0.0 |
|  | 99¢ | 3,500 | ×0.5^97 = 0.0 |
| | | **Σ** | **669.0** |

`yours 400.0 / Σ 669.0 = 59.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 59.8% = $2.49/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-wiltim</code> BUY 2,000 @ 1¢ → $2.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,125 (2,000 yours) | ×0.5^0 = 4,125.0 |
| | | **Σ** | **4,125.0** |

`yours 2,000.0 / Σ 4,125.0 = 48.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 48.5% = $2.02/day`  

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
<details><summary><code>iarc-group-2026-12-31-tuccar</code> BUY 2,000 @ 1¢ → $2.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 3 | ×0.5^0 = 3.0 |
|  | 2¢ | 968 | ×0.5^1 = 484.0 |
| ▶ | 1¢ | 2,200 (2,000 yours) | ×0.5^2 = 550.0 |
| | | **Σ** | **1,037.0** |

`yours 500.0 / Σ 1,037.0 = 48.2%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 48.2% = $2.41/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> BUY 2,000 @ 1¢ → $1.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,500 (2,000 yours) | ×0.5^0 = 4,500.0 |
| | | **Σ** | **4,500.0** |

`yours 2,000.0 / Σ 4,500.0 = 44.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 44.4% = $1.85/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 30 @ 34¢ → $2.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 72 (30 yours) | ×0.5^0 = 72.0 |
|  | 42¢ | 56 | ×0.5^8 = 0.2 |
|  | 45¢ | 25 | ×0.5^11 = 0.0 |
|  | 98¢ | 98,906 | ×0.5^64 = 0.0 |
| | | **Σ** | **72.2** |

`yours 30.0 / Σ 72.2 = 41.5%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 41.5% = $2.08/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-paudan</code> BUY 2,000 @ 1¢ → $1.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,181 (2,000 yours) | ×0.5^0 = 5,181.0 |
| | | **Σ** | **5,181.0** |

`yours 2,000.0 / Σ 5,181.0 = 38.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 38.6% = $1.61/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-andbau</code> BUY 2,000 @ 1¢ → $1.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,549 (2,000 yours) | ×0.5^0 = 5,549.0 |
| | | **Σ** | **5,549.0** |

`yours 2,000.0 / Σ 5,549.0 = 36.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 36.0% = $1.50/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 78 @ 93¢ → $1.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 4 | ×0.5^0 = 4.0 |
| ▶ | 93¢ | 78 (78 yours) | ×0.5^1 = 38.9 |
|  | 97¢ | 2,102 | ×0.5^5 = 65.7 |
| | | **Σ** | **108.6** |

`yours 38.9 / Σ 108.6 = 35.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 35.8% = $1.49/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 100 @ 25¢ → $0.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 399 (100 yours) | ×0.5^0 = 399.0 |
|  | 50¢ | 100 | ×0.5^25 = 0.0 |
|  | 55¢ | 44 | ×0.5^30 = 0.0 |
|  | 97¢ | 38,892 | ×0.5^72 = 0.0 |
| | | **Σ** | **399.0** |

`yours 100.0 / Σ 399.0 = 25.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.1% = $0.96/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 86 @ 20¢ → $0.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 364 (86 yours) | ×0.5^0 = 363.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 55¢ | 44 | ×0.5^35 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
|  | 99¢ | 5,481 | ×0.5^79 = 0.0 |
| | | **Σ** | **363.7** |

`yours 85.7 / Σ 363.7 = 23.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 23.6% = $0.98/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor` ← this one
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-nanmac</code> BUY 2,000 @ 1¢ → $0.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 10,362 (2,000 yours) | ×0.5^0 = 10,362.0 |
| | | **Σ** | **10,362.0** |

`yours 2,000.0 / Σ 10,362.0 = 19.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.3% = $0.80/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 200 @ 12¢ → $0.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1,012 (200 yours) | ×0.5^0 = 1,012.0 |
|  | 7¢ | 944 | ×0.5^5 = 29.5 |
|  | 6¢ | 263 | ×0.5^6 = 4.1 |
| | | **Σ** | **1,045.6** |

`yours 200.0 / Σ 1,045.6 = 19.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.1% = $0.74/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 200 @ 18¢ → $0.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1,158 (200 yours) | ×0.5^0 = 1,158.0 |
|  | 3¢ | 200,000 | ×0.5^15 = 6.1 |
| | | **Σ** | **1,164.1** |

`yours 200.0 / Σ 1,164.1 = 17.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.2% = $0.66/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 2,000 @ 1¢ → $0.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 14,950 (2,000 yours) | ×0.5^0 = 14,950.0 |
| | | **Σ** | **14,950.0** |

`yours 2,000.0 / Σ 14,950.0 = 13.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 13.4% = $0.51/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 9 @ 34¢ → $0.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 72 (9 yours) | ×0.5^0 = 72.0 |
|  | 42¢ | 56 | ×0.5^8 = 0.2 |
|  | 45¢ | 25 | ×0.5^11 = 0.0 |
|  | 98¢ | 98,906 | ×0.5^64 = 0.0 |
| | | **Σ** | **72.2** |

`yours 9.0 / Σ 72.2 = 12.5%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 12.5% = $0.62/day`  

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
<details><summary><code>enwc-usgubp-fl-2026-08-18-rep-jaycol</code> BUY 2,000 @ 1¢ → $2.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 16,211 (2,000 yours) | ×0.5^0 = 16,211.0 |
| | | **Σ** | **16,211.0** |

`yours 2,000.0 / Σ 16,211.0 = 12.3%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 12.3% = $2.06/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `enwc-usgubp-fl-2026-08-18-rep-byrdon`
2. `enwc-usgubp-fl-2026-08-18-rep-jamfis`
3. `enwc-usgubp-fl-2026-08-18-rep-jaycol` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> BUY 2,001 @ 2¢ → $0.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 269 | ×0.5^0 = 269.0 |
|  | 5¢ | 892 | ×0.5^2 = 223.0 |
| ▶ | 2¢ | 2,840 (2,001 yours) | ×0.5^5 = 88.8 |
| | | **Σ** | **580.8** |

`yours 62.5 / Σ 580.8 = 10.8%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 10.8% = $0.54/day`  

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
<details><summary><code>stsc-bab-el-mandeb-clsd-2026-07-31</code> BUY 500 @ 6¢ → $3.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 5,320 (500 yours) | ×0.5^0 = 5,320.3 |
| | | **Σ** | **5,320.3** |

`yours 500.0 / Σ 5,320.3 = 9.4%`  
`$250 ÷ 3 ÷ 2 = $41.67 × 9.4% = $3.92/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `stsc-bab-el-mandeb-clsd-2026-07-31` ← this one
2. `stsc-bab-el-mandeb-clsd-2026-08-31`
3. `stsc-bab-el-mandeb-clsd-2026-12-31`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> BUY 2,000 @ 1¢ → $0.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 124 | ×0.5^0 = 124.0 |
|  | 7¢ | 55 | ×0.5^1 = 27.5 |
|  | 5¢ | 892 | ×0.5^3 = 111.5 |
|  | 4¢ | 164 | ×0.5^4 = 10.2 |
|  | 3¢ | 164 | ×0.5^5 = 5.1 |
| ▶ | 1¢ | 4,311 (2,000 yours) | ×0.5^7 = 33.7 |
| | | **Σ** | **312.1** |

`yours 15.6 / Σ 312.1 = 5.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.0% = $0.21/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 4 | ×0.5^0 = 4.0 |
|  | 93¢ | 78 | ×0.5^1 = 38.9 |
| ▶ | 97¢ | 2,102 (136 yours) | ×0.5^5 = 65.7 |
| | | **Σ** | **108.6** |

`yours 4.2 / Σ 108.6 = 3.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.9% = $0.16/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 4 | ×0.5^0 = 4.0 |
|  | 93¢ | 78 | ×0.5^1 = 38.9 |
| ▶ | 97¢ | 2,102 (136 yours) | ×0.5^5 = 65.7 |
| | | **Σ** | **108.6** |

`yours 4.2 / Σ 108.6 = 3.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.9% = $0.16/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 4 | ×0.5^0 = 4.0 |
|  | 93¢ | 78 | ×0.5^1 = 38.9 |
| ▶ | 97¢ | 2,102 (136 yours) | ×0.5^5 = 65.7 |
| | | **Σ** | **108.6** |

`yours 4.2 / Σ 108.6 = 3.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.9% = $0.16/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 4 | ×0.5^0 = 4.0 |
|  | 93¢ | 78 | ×0.5^1 = 38.9 |
| ▶ | 97¢ | 2,102 (136 yours) | ×0.5^5 = 65.7 |
| | | **Σ** | **108.6** |

`yours 4.2 / Σ 108.6 = 3.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.9% = $0.16/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 4 | ×0.5^0 = 4.0 |
|  | 93¢ | 78 | ×0.5^1 = 38.9 |
| ▶ | 97¢ | 2,102 (136 yours) | ×0.5^5 = 65.7 |
| | | **Σ** | **108.6** |

`yours 4.2 / Σ 108.6 = 3.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.9% = $0.16/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 4 | ×0.5^0 = 4.0 |
|  | 93¢ | 78 | ×0.5^1 = 38.9 |
| ▶ | 97¢ | 2,102 (136 yours) | ×0.5^5 = 65.7 |
| | | **Σ** | **108.6** |

`yours 4.2 / Σ 108.6 = 3.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.9% = $0.16/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 4 | ×0.5^0 = 4.0 |
|  | 93¢ | 78 | ×0.5^1 = 38.9 |
| ▶ | 97¢ | 2,102 (136 yours) | ×0.5^5 = 65.7 |
| | | **Σ** | **108.6** |

`yours 4.2 / Σ 108.6 = 3.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.9% = $0.16/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 92¢ | 4 | ×0.5^0 = 4.0 |
|  | 93¢ | 78 | ×0.5^1 = 38.9 |
| ▶ | 97¢ | 2,102 (136 yours) | ×0.5^5 = 65.7 |
| | | **Σ** | **108.6** |

`yours 4.2 / Σ 108.6 = 3.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.9% = $0.16/day`  

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
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (14,326 resting) | ~30.3% | ~$7.58 |
| `ewc-usgub-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (87,844 resting) | ~12.0% | ~$2.99 |
| `ewc-usgub-wi-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (121,377 resting) | ~11.4% | ~$2.85 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (67,118 resting) | ~9.6% | ~$2.41 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (33,068 resting) | ~9.5% | ~$2.37 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (63,643 resting) | ~9.1% | ~$2.28 |
| `ewc-usgub-ks-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (164,930 resting) | ~8.6% | ~$2.15 |
| `ewc-usse-ia-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (170,094 resting) | ~8.4% | ~$2.09 |
| `ewc-usgub-ks-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (167,786 resting) | ~7.8% | ~$1.96 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (98,521 resting) | ~7.4% | ~$1.84 |
| `ewc-usgub-az-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (130,255 resting) | ~7.3% | ~$1.81 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $100.00 ÷ 3 | 0.50 | 2,000 | SELL side (128,321 resting) | ~9.1% | ~$1.52 |

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
| 2026-07-25 1:18 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 12:57 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 12:46 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 12:12 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 12:11 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 11:46 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 11:36 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 11:31 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 10:21 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 10:05 AM ET | ✅ ok | 282 | $701.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
