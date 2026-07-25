# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-25 10:21 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$81.82/day estimated (ceiling, not promise — details below)

**Earned:** $701.42 lifetime ($155.84 paid). Last three recorded days — 2026-07-23: **$227.63** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-22: **$82.95** · 2026-07-21: **$91.44** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$7.05/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$4.62/day), `ewc-usgub-ga-2026-11-03-rep` (~$3.46/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$81.82/day (~$3.41/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~90.9% of bid side (2,200 resting ≥ 2,000 ✓) ≈ $3.79/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~79.2% of bid side (2,525 resting ≥ 2,000 ✓) ≈ $3.30/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~79.2% of bid side (2,525 resting ≥ 2,000 ✓) ≈ $3.30/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~75.5% of bid side (2,649 resting ≥ 2,000 ✓) ≈ $3.15/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~74.0% of bid side (2,703 resting ≥ 2,000 ✓) ≈ $3.08/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | BUY | 2.0¢ | 2,001 | 0 | $100.00 | ✅ scoring — ~63.0% of bid side (34,254 resting ≥ 2,000 ✓) ≈ $3.15/day (pool ÷ 10 markets) |
| `iarc-group-2026-12-31-tuccar` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~60.3% of bid side (3,317 resting ≥ 2,000 ✓) ≈ $3.01/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | BUY | 25.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~55.6% of bid side (7,684 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 2.0¢ | 2,001 | 0 | $100.00 | ✅ scoring — ~54.3% of bid side (9,760 resting ≥ 2,000 ✓) ≈ $2.72/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 16.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~53.7% of bid side (200,549 resting ≥ 2,000 ✓) ≈ $2.07/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 2.0¢ | 400 | 0 | $100.00 | ✅ scoring — ~53.6% of ask side (3,573 resting ≥ 2,000 ✓) ≈ $2.23/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 5.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~51.1% of ask side (39,508 resting ≥ 2,000 ✓) ≈ $2.55/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 34.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~50.9% of ask side (99,589 resting ≥ 2,000 ✓) ≈ $2.55/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 12.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~44.7% of bid side (200,649 resting ≥ 2,000 ✓) ≈ $1.72/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~44.5% of bid side (4,496 resting ≥ 2,000 ✓) ≈ $1.85/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 16.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~40.8% of bid side (200,667 resting ≥ 2,000 ✓) ≈ $1.57/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 93.0¢ | 78 | 0 | $100.00 | ✅ scoring — ~31.8% of ask side (3,179 resting ≥ 2,000 ✓) ≈ $1.32/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | SELL | 14.0¢ | 11 | 0 | $100.00 | ✅ scoring — ~29.0% of ask side (40,029 resting ≥ 2,000 ✓) ≈ $1.45/day (pool ÷ 10 markets) |
| `pvwc-housepopw-2026-11-03-dem` | SELL | 94.0¢ | 77 | 1 | $100.00 | ✅ scoring — ~25.8% of ask side (4,515 resting ≥ 2,000 ✓) ≈ $6.44/day (pool ÷ 2 markets) |
| `pvwc-housepopw-2026-11-03-dem` | SELL | 94.0¢ | 77 | 1 | $100.00 | ✅ scoring — ~25.8% of ask side (4,515 resting ≥ 2,000 ✓) ≈ $6.44/day (pool ÷ 2 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~21.6% of ask side (4,169 resting ≥ 2,000 ✓) ≈ $0.90/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 34.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~21.4% of bid side (10,837 resting ≥ 2,000 ✓) ≈ $10.68/day |
| `scc-senate-gop-2026-11-03-48` | SELL | 25.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~20.4% of ask side (89,306 resting ≥ 2,000 ✓) ≈ $0.78/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 8.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~17.7% of bid side (50,571 resting ≥ 2,000 ✓) ≈ $0.68/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 34.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~15.3% of ask side (99,589 resting ≥ 2,000 ✓) ≈ $0.76/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~14.4% of bid side (13,879 resting ≥ 2,000 ✓) ≈ $0.55/day (pool ÷ 13 markets) |
| `stsc-bab-el-mandeb-clsd-2026-07-31` | BUY | 6.0¢ | 500 | 0 | $250.00 | ✅ scoring — ~9.4% of bid side (6,553 resting ≥ 2,000 ✓) ≈ $3.92/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 49.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~7.7% of ask side (89,291 resting ≥ 2,000 ✓) ≈ $0.29/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 48.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~6.8% of ask side (112,104 resting ≥ 2,000 ✓) ≈ $0.26/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 16.0¢ | 61 | 0 | $100.00 | ✅ scoring — ~6.2% of ask side (2,501 resting ≥ 2,000 ✓) ≈ $1.04/day (pool ÷ 3 markets) |
| …and 54 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> BUY 2,000 @ 1¢ → $3.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,200 (2,000 yours) | ×0.5^0 = 2,200.0 |
| | | **Σ** | **2,200.0** |

`yours 2,000.0 / Σ 2,200.0 = 90.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 90.9% = $3.79/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-wiltim</code> BUY 2,000 @ 1¢ → $3.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,525 (2,000 yours) | ×0.5^0 = 2,525.0 |
| | | **Σ** | **2,525.0** |

`yours 2,000.0 / Σ 2,525.0 = 79.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 79.2% = $3.30/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-paudan</code> BUY 2,000 @ 1¢ → $3.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,525 (2,000 yours) | ×0.5^0 = 2,525.0 |
| | | **Σ** | **2,525.0** |

`yours 2,000.0 / Σ 2,525.0 = 79.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 79.2% = $3.30/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> BUY 2,000 @ 1¢ → $3.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,649 (2,000 yours) | ×0.5^0 = 2,649.0 |
| | | **Σ** | **2,649.0** |

`yours 2,000.0 / Σ 2,649.0 = 75.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 75.5% = $3.15/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-andbau</code> BUY 2,000 @ 1¢ → $3.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,703 (2,000 yours) | ×0.5^0 = 2,703.0 |
| | | **Σ** | **2,703.0** |

`yours 2,000.0 / Σ 2,703.0 = 74.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 74.0% = $3.08/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> BUY 2,001 @ 2¢ → $3.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 3,177 (2,001 yours) | ×0.5^0 = 3,177.0 |
| | | **Σ** | **3,177.0** |

`yours 2,001.0 / Σ 3,177.0 = 63.0%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 63.0% = $3.15/day`  

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
<details><summary><code>iarc-group-2026-12-31-tuccar</code> BUY 2,000 @ 1¢ → $3.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,317 (2,000 yours) | ×0.5^0 = 3,317.0 |
| | | **Σ** | **3,317.0** |

`yours 2,000.0 / Σ 3,317.0 = 60.3%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 60.3% = $3.01/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> BUY 50 @ 25¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 50 (50 yours) | ×0.5^0 = 50.0 |
|  | 24¢ | 80 | ×0.5^1 = 40.0 |
|  | 12¢ | 28 | ×0.5^13 = 0.0 |
|  | 2¢ | 2,001 | ×0.5^23 = 0.0 |
| | | **Σ** | **90.0** |

`yours 50.0 / Σ 90.0 = 55.6%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 55.6% = $2.78/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 2,001 @ 2¢ → $2.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 3,683 (2,001 yours) | ×0.5^0 = 3,683.0 |
| | | **Σ** | **3,683.0** |

`yours 2,001.0 / Σ 3,683.0 = 54.3%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 54.3% = $2.72/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 200 @ 16¢ → $2.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 24 | ×0.5^0 = 24.0 |
| ▶ | 16¢ | 300 (200 yours) | ×0.5^1 = 150.0 |
|  | 3¢ | 200,000 | ×0.5^14 = 12.2 |
| | | **Σ** | **186.2** |

`yours 100.0 / Σ 186.2 = 53.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.7% = $2.07/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 400 @ 2¢ → $2.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 746 (400 yours) | ×0.5^0 = 746.0 |
|  | 50¢ | 25 | ×0.5^48 = 0.0 |
|  | 55¢ | 44 | ×0.5^53 = 0.0 |
|  | 99¢ | 2,758 | ×0.5^97 = 0.0 |
| | | **Σ** | **746.0** |

`yours 400.0 / Σ 746.0 = 53.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 53.6% = $2.23/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 5¢ → $2.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 2 (1 yours) | ×0.5^0 = 1.5 |
|  | 11¢ | 28 | ×0.5^6 = 0.4 |
|  | 43¢ | 2,000 | ×0.5^38 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 51.1%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 51.1% = $2.55/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 30 @ 34¢ → $2.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 58 (30 yours) | ×0.5^0 = 58.0 |
|  | 40¢ | 56 | ×0.5^6 = 0.9 |
|  | 45¢ | 25 | ×0.5^11 = 0.0 |
|  | 55¢ | 44 | ×0.5^21 = 0.0 |
|  | 98¢ | 98,906 | ×0.5^64 = 0.0 |
| | | **Σ** | **58.9** |

`yours 30.0 / Σ 58.9 = 50.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 50.9% = $2.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 200 @ 12¢ → $1.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 24 | ×0.5^0 = 24.0 |
| ▶ | 12¢ | 300 (200 yours) | ×0.5^1 = 150.0 |
|  | 6¢ | 100 | ×0.5^7 = 0.8 |
|  | 1¢ | 200,225 | ×0.5^12 = 48.9 |
| | | **Σ** | **223.7** |

`yours 100.0 / Σ 223.7 = 44.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 44.7% = $1.72/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-nanmac</code> BUY 2,000 @ 1¢ → $1.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,496 (2,000 yours) | ×0.5^0 = 4,496.0 |
| | | **Σ** | **4,496.0** |

`yours 2,000.0 / Σ 4,496.0 = 44.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 44.5% = $1.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 200 @ 16¢ → $1.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 24 | ×0.5^0 = 24.0 |
| ▶ | 16¢ | 418 (200 yours) | ×0.5^1 = 209.0 |
|  | 3¢ | 200,000 | ×0.5^14 = 12.2 |
| | | **Σ** | **245.2** |

`yours 100.0 / Σ 245.2 = 40.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.8% = $1.57/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 78 @ 93¢ → $1.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 116 (78 yours) | ×0.5^0 = 115.8 |
|  | 97¢ | 2,063 | ×0.5^4 = 129.0 |
| | | **Σ** | **244.7** |

`yours 77.8 / Σ 244.7 = 31.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 31.8% = $1.32/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> SELL 11 @ 14¢ → $1.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 37 (11 yours) | ×0.5^0 = 37.0 |
|  | 20¢ | 29 | ×0.5^6 = 0.5 |
|  | 24¢ | 441 | ×0.5^10 = 0.4 |
|  | 43¢ | 2,000 | ×0.5^29 = 0.0 |
| | | **Σ** | **37.9** |

`yours 11.0 / Σ 37.9 = 29.0%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 29.0% = $1.45/day`  

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
<details><summary><code>pvwc-housepopw-2026-11-03-dem</code> SELL 77 @ 94¢ → $6.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 93¢ | 1 | ×0.5^0 = 1.0 |
| ▶ | 94¢ | 154 (77 yours) | ×0.5^1 = 76.9 |
|  | 97¢ | 69 | ×0.5^4 = 4.3 |
|  | 99¢ | 4,291 | ×0.5^6 = 67.0 |
| | | **Σ** | **149.3** |

`yours 38.5 / Σ 149.3 = 25.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 25.8% = $6.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem` ← this one
2. `pvwc-housepopw-2026-11-03-rep`

</details>

</details>
<details><summary><code>pvwc-housepopw-2026-11-03-dem</code> SELL 77 @ 94¢ → $6.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 93¢ | 1 | ×0.5^0 = 1.0 |
| ▶ | 94¢ | 154 (77 yours) | ×0.5^1 = 76.9 |
|  | 97¢ | 69 | ×0.5^4 = 4.3 |
|  | 99¢ | 4,291 | ×0.5^6 = 67.0 |
| | | **Σ** | **149.3** |

`yours 38.5 / Σ 149.3 = 25.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 25.8% = $6.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem` ← this one
2. `pvwc-housepopw-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 100 @ 20¢ → $0.90/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 464 (100 yours) | ×0.5^0 = 464.0 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 55¢ | 44 | ×0.5^35 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 250 | ×0.5^54 = 0.0 |
|  | 99¢ | 3,181 | ×0.5^79 = 0.0 |
| | | **Σ** | **464.0** |

`yours 100.0 / Σ 464.0 = 21.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 21.6% = $0.90/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 100 @ 34¢ → $10.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 36¢ | 42 | ×0.5^0 = 42.0 |
|  | 35¢ | 100 | ×0.5^1 = 50.0 |
| ▶ | 34¢ | 100 (100 yours) | ×0.5^2 = 25.0 |
|  | 27¢ | 29 | ×0.5^9 = 0.1 |
|  | 19¢ | 363 | ×0.5^17 = 0.0 |
|  | 2¢ | 10,000 | ×0.5^34 = 0.0 |
| | | **Σ** | **117.0** |

`yours 25.0 / Σ 117.0 = 21.4%`  
`$100 ÷ 1 ÷ 2 = $50.00 × 21.4% = $10.68/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 100 @ 25¢ → $0.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 472 (100 yours) | ×0.5^0 = 472.0 |
|  | 28¢ | 147 | ×0.5^3 = 18.4 |
|  | 50¢ | 100 | ×0.5^25 = 0.0 |
|  | 97¢ | 38,892 | ×0.5^72 = 0.0 |
| | | **Σ** | **490.4** |

`yours 100.0 / Σ 490.4 = 20.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.4% = $0.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 200 @ 8¢ → $0.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 24 | ×0.5^0 = 24.0 |
| ▶ | 8¢ | 300 (200 yours) | ×0.5^1 = 150.0 |
|  | 2¢ | 50,000 | ×0.5^7 = 390.6 |
| | | **Σ** | **564.6** |

`yours 100.0 / Σ 564.6 = 17.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.7% = $0.68/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 9 @ 34¢ → $0.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 58 (9 yours) | ×0.5^0 = 58.0 |
|  | 40¢ | 56 | ×0.5^6 = 0.9 |
|  | 45¢ | 25 | ×0.5^11 = 0.0 |
|  | 55¢ | 44 | ×0.5^21 = 0.0 |
|  | 98¢ | 98,906 | ×0.5^64 = 0.0 |
| | | **Σ** | **58.9** |

`yours 9.0 / Σ 58.9 = 15.3%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 15.3% = $0.76/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 2,000 @ 1¢ → $0.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 13,879 (2,000 yours) | ×0.5^0 = 13,879.0 |
| | | **Σ** | **13,879.0** |

`yours 2,000.0 / Σ 13,879.0 = 14.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.4% = $0.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 100 @ 49¢ → $0.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 48¢ | 577 | ×0.5^0 = 577.0 |
| ▶ | 49¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 50¢ | 100 | ×0.5^2 = 25.0 |
|  | 97¢ | 38,855 | ×0.5^49 = 0.0 |
| | | **Σ** | **652.0** |

`yours 50.0 / Σ 652.0 = 7.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.7% = $0.29/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 100 @ 48¢ → $0.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 47¢ | 677 | ×0.5^0 = 677.0 |
| ▶ | 48¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 50¢ | 100 | ×0.5^3 = 12.5 |
|  | 97¢ | 100,026 | ×0.5^50 = 0.0 |
| | | **Σ** | **739.5** |

`yours 50.0 / Σ 739.5 = 6.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.8% = $0.26/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 61 @ 16¢ → $1.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 977 (61 yours) | ×0.5^0 = 976.8 |
|  | 26¢ | 587 | ×0.5^10 = 0.6 |
|  | 50¢ | 250 | ×0.5^34 = 0.0 |
|  | 80¢ | 5 | ×0.5^64 = 0.0 |
|  | 81¢ | 5 | ×0.5^65 = 0.0 |
|  | 82¢ | 5 | ×0.5^66 = 0.0 |
|  | 99¢ | 672 | ×0.5^83 = 0.0 |
| | | **Σ** | **977.4** |

`yours 60.8 / Σ 977.4 = 6.2%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 6.2% = $1.04/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-alito-2026-07-31`
2. `apdc-alito-2026-08-31`
3. `apdc-alito-2026-12-31` ← this one

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
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (31,562 resting) | ~28.2% | ~$7.05 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (32,218 resting) | ~18.5% | ~$4.62 |
| `ewc-usgub-ga-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (56,897 resting) | ~13.8% | ~$3.46 |
| `ewc-usgub-ks-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (105,772 resting) | ~11.4% | ~$2.84 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (2,668 resting) | ~10.7% | ~$2.68 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $100.00 ÷ 3 | 0.50 | 2,000 | SELL side (96,719 resting) | ~15.6% | ~$2.61 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (77,549 resting) | ~7.4% | ~$1.85 |
| `ewc-usgub-ks-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (155,353 resting) | ~6.1% | ~$1.52 |
| `apdc-jerpowgov-2026-07-31` | $100.00 ÷ 3 | 0.50 | 2,000 | BUY side (2,220 resting) | ~8.3% | ~$1.38 |
| `ewc-usgub-ga-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (46,976 resting) | ~5.5% | ~$1.37 |
| `ewc-usgub-ia-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (102,792 resting) | ~4.8% | ~$1.19 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $100.00 ÷ 3 | 0.50 | 2,000 | BUY side (126,370 resting) | ~5.4% | ~$0.90 |

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
| 2026-07-25 10:21 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 10:05 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 9:58 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 9:41 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 8:11 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 6:46 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 5:14 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 2:31 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-24 11:43 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-24 10:00 PM ET | ✅ ok | 282 | $701.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
