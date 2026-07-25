# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-25 12:11 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$111.59/day estimated (ceiling, not promise — details below)

**Earned:** $701.42 lifetime ($155.84 paid). Last three recorded days — 2026-07-23: **$227.63** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-22: **$82.95** · 2026-07-21: **$91.44** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$7.05/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$4.62/day), `ewc-usgub-ga-2026-11-03-rep` (~$3.45/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$111.59/day (~$4.65/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~80.0% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $3.33/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 16.0¢ | 200 | 2 | $100.00 | ✅ scoring — ~79.2% of bid side (200,657 resting ≥ 2,000 ✓) ≈ $3.05/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 34.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~75.4% of bid side (10,869 resting ≥ 2,000 ✓) ≈ $37.72/day |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~74.7% of bid side (2,678 resting ≥ 2,000 ✓) ≈ $3.11/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 24.0¢ | 70 | 0 | $100.00 | ✅ scoring — ~66.6% of ask side (63,843 resting ≥ 2,000 ✓) ≈ $3.33/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 5.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~65.8% of ask side (39,480 resting ≥ 2,000 ✓) ≈ $3.29/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | BUY | 25.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~55.6% of bid side (7,909 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 2.0¢ | 400 | 0 | $100.00 | ✅ scoring — ~53.6% of ask side (5,873 resting ≥ 2,000 ✓) ≈ $2.23/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | BUY | 2.0¢ | 2,001 | 0 | $100.00 | ✅ scoring — ~51.5% of bid side (34,938 resting ≥ 2,000 ✓) ≈ $2.57/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 34.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~51.3% of ask side (99,589 resting ≥ 2,000 ✓) ≈ $2.57/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~48.5% of bid side (4,125 resting ≥ 2,000 ✓) ≈ $2.02/day (pool ÷ 12 markets) |
| `iarc-group-2026-12-31-tuccar` | BUY | 1.0¢ | 2,000 | 2 | $100.00 | ✅ scoring — ~48.2% of bid side (3,173 resting ≥ 2,000 ✓) ≈ $2.41/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~44.4% of bid side (4,500 resting ≥ 2,000 ✓) ≈ $1.85/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 12.0¢ | 200 | 0 | $100.00 | ✅ scoring — ~33.7% of bid side (200,795 resting ≥ 2,000 ✓) ≈ $1.29/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 2.0¢ | 2,001 | 0 | $100.00 | ✅ scoring — ~28.0% of bid side (12,155 resting ≥ 2,000 ✓) ≈ $1.40/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 93.0¢ | 78 | 0 | $100.00 | ✅ scoring — ~27.6% of ask side (3,254 resting ≥ 2,000 ✓) ≈ $1.15/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | BUY | 1.0¢ | 2,000 | 3 | $100.00 | ✅ scoring — ~25.3% of bid side (3,328 resting ≥ 2,000 ✓) ≈ $1.05/day (pool ÷ 12 markets) |
| `ewc-ref-ca-blntax-2026-11-03-pass` | BUY | 37.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~25.1% of bid side (5,534 resting ≥ 2,000 ✓) ≈ $12.55/day |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~24.2% of bid side (8,250 resting ≥ 2,000 ✓) ≈ $1.01/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 20.0¢ | 86 | 0 | $100.00 | ✅ scoring — ~19.1% of ask side (6,230 resting ≥ 2,000 ✓) ≈ $0.79/day (pool ÷ 12 markets) |
| `pvwc-housepopw-2026-11-03-dem` | SELL | 94.0¢ | 77 | 0 | $100.00 | ✅ scoring — ~17.2% of ask side (4,767 resting ≥ 2,000 ✓) ≈ $4.29/day (pool ÷ 2 markets) |
| `pvwc-housepopw-2026-11-03-dem` | SELL | 94.0¢ | 77 | 0 | $100.00 | ✅ scoring — ~17.2% of ask side (4,767 resting ≥ 2,000 ✓) ≈ $4.29/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 25.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~16.0% of ask side (89,309 resting ≥ 2,000 ✓) ≈ $0.62/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 40.0¢ | 30 | 4 | $100.00 | ✅ scoring — ~15.7% of ask side (63,781 resting ≥ 2,000 ✓) ≈ $0.79/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 34.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~15.4% of ask side (99,589 resting ≥ 2,000 ✓) ≈ $0.77/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~12.6% of bid side (15,830 resting ≥ 2,000 ✓) ≈ $0.49/day (pool ÷ 13 markets) |
| `stsc-bab-el-mandeb-clsd-2026-07-31` | BUY | 6.0¢ | 500 | 0 | $250.00 | ✅ scoring — ~9.4% of bid side (6,553 resting ≥ 2,000 ✓) ≈ $3.92/day (pool ÷ 3 markets) |
| `apdc-alito-2026-12-31` | SELL | 16.0¢ | 61 | 0 | $100.00 | ✅ scoring — ~6.2% of ask side (2,079 resting ≥ 2,000 ✓) ≈ $1.04/day (pool ÷ 3 markets) |
| `ewc-ref-ca-blntax-2026-11-03-pass` | SELL | 44.0¢ | 20 | 6 | $100.00 | ✅ scoring — ~6.0% of ask side (63,458 resting ≥ 2,000 ✓) ≈ $2.99/day |
| `mowc-nato-us-12-31-2026` | BUY | 10.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~5.2% of bid side (103,883 resting ≥ 2,000 ✓) ≈ $1.30/day (pool ÷ 2 markets) |
| …and 51 more | | | | | | |

**Tap an order for its book window and the math:**

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 200 @ 16¢ → $3.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 7 | ×0.5^0 = 7.0 |
| ▶ | 16¢ | 200 (200 yours) | ×0.5^2 = 50.0 |
|  | 3¢ | 200,250 | ×0.5^15 = 6.1 |
| | | **Σ** | **63.1** |

`yours 50.0 / Σ 63.1 = 79.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 79.2% = $3.05/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 100 @ 34¢ → $37.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 35¢ | 16 | ×0.5^0 = 16.0 |
| ▶ | 34¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 28¢ | 29 | ×0.5^7 = 0.2 |
|  | 27¢ | 9 | ×0.5^8 = 0.0 |
|  | 19¢ | 515 | ×0.5^16 = 0.0 |
|  | 2¢ | 10,000 | ×0.5^33 = 0.0 |
| | | **Σ** | **66.3** |

`yours 50.0 / Σ 66.3 = 75.4%`  
`$100 ÷ 1 ÷ 2 = $50.00 × 75.4% = $37.72/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 70 @ 24¢ → $3.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 105 (70 yours) | ×0.5^0 = 105.0 |
|  | 32¢ | 29 | ×0.5^8 = 0.1 |
|  | 40¢ | 16 | ×0.5^16 = 0.0 |
|  | 45¢ | 25 | ×0.5^21 = 0.0 |
|  | 55¢ | 44 | ×0.5^31 = 0.0 |
|  | 98¢ | 63,125 | ×0.5^74 = 0.0 |
| | | **Σ** | **105.1** |

`yours 70.0 / Σ 105.1 = 66.6%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 66.6% = $3.33/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> BUY 50 @ 25¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 50 (50 yours) | ×0.5^0 = 50.0 |
|  | 24¢ | 80 | ×0.5^1 = 40.0 |
|  | 12¢ | 28 | ×0.5^13 = 0.0 |
|  | 2¢ | 2,251 | ×0.5^23 = 0.0 |
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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 400 @ 2¢ → $2.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 746 (400 yours) | ×0.5^0 = 746.0 |
|  | 50¢ | 25 | ×0.5^48 = 0.0 |
|  | 55¢ | 44 | ×0.5^53 = 0.0 |
|  | 99¢ | 5,058 | ×0.5^97 = 0.0 |
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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> BUY 2,001 @ 2¢ → $2.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 3,886 (2,001 yours) | ×0.5^0 = 3,886.0 |
| | | **Σ** | **3,886.0** |

`yours 2,001.0 / Σ 3,886.0 = 51.5%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 51.5% = $2.57/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 30 @ 34¢ → $2.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 58 (30 yours) | ×0.5^0 = 58.0 |
|  | 41¢ | 56 | ×0.5^7 = 0.4 |
|  | 45¢ | 25 | ×0.5^11 = 0.0 |
|  | 55¢ | 44 | ×0.5^21 = 0.0 |
|  | 98¢ | 98,906 | ×0.5^64 = 0.0 |
| | | **Σ** | **58.4** |

`yours 30.0 / Σ 58.4 = 51.3%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 51.3% = $2.57/day`  

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
|  | 2¢ | 970 | ×0.5^1 = 485.0 |
| ▶ | 1¢ | 2,200 (2,000 yours) | ×0.5^2 = 550.0 |
| | | **Σ** | **1,038.0** |

`yours 500.0 / Σ 1,038.0 = 48.2%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 200 @ 12¢ → $1.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 495 (200 yours) | ×0.5^0 = 495.0 |
|  | 6¢ | 100 | ×0.5^6 = 1.6 |
|  | 1¢ | 200,200 | ×0.5^11 = 97.8 |
| | | **Σ** | **594.3** |

`yours 200.0 / Σ 594.3 = 33.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.7% = $1.29/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 2,001 @ 2¢ → $1.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 7,155 (2,001 yours) | ×0.5^0 = 7,155.0 |
| | | **Σ** | **7,155.0** |

`yours 2,001.0 / Σ 7,155.0 = 28.0%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 28.0% = $1.40/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 78 @ 93¢ → $1.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 116 (78 yours) | ×0.5^0 = 115.8 |
|  | 94¢ | 75 | ×0.5^1 = 37.5 |
|  | 97¢ | 2,063 | ×0.5^4 = 129.0 |
| | | **Σ** | **282.2** |

`yours 77.8 / Σ 282.2 = 27.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 27.6% = $1.15/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> BUY 2,000 @ 1¢ → $1.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 186 | ×0.5^0 = 186.0 |
|  | 3¢ | 1,068 | ×0.5^1 = 534.0 |
|  | 2¢ | 74 | ×0.5^2 = 18.5 |
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.5^3 = 250.0 |
| | | **Σ** | **988.5** |

`yours 250.0 / Σ 988.5 = 25.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 25.3% = $1.05/day`  

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
<details><summary><code>ewc-ref-ca-blntax-2026-11-03-pass</code> BUY 30 @ 37¢ → $12.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 30 (30 yours) | ×0.5^0 = 30.0 |
|  | 36¢ | 54 | ×0.5^1 = 27.0 |
|  | 35¢ | 250 | ×0.5^2 = 62.5 |
|  | 2¢ | 5,000 | ×0.5^35 = 0.0 |
| | | **Σ** | **119.5** |

`yours 30.0 / Σ 119.5 = 25.1%`  
`$100 ÷ 1 ÷ 2 = $50.00 × 25.1% = $12.55/day`  

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-nanmac</code> BUY 2,000 @ 1¢ → $1.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 8,250 (2,000 yours) | ×0.5^0 = 8,250.0 |
| | | **Σ** | **8,250.0** |

`yours 2,000.0 / Σ 8,250.0 = 24.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 24.2% = $1.01/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 86 @ 20¢ → $0.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 450 (86 yours) | ×0.5^0 = 449.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 55¢ | 44 | ×0.5^35 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
|  | 99¢ | 5,481 | ×0.5^79 = 0.0 |
| | | **Σ** | **449.7** |

`yours 85.7 / Σ 449.7 = 19.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.1% = $0.79/day`  

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
<details><summary><code>pvwc-housepopw-2026-11-03-dem</code> SELL 77 @ 94¢ → $4.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 230 (77 yours) | ×0.5^0 = 229.9 |
|  | 95¢ | 149 | ×0.5^1 = 74.5 |
|  | 97¢ | 69 | ×0.5^3 = 8.6 |
|  | 99¢ | 4,319 | ×0.5^5 = 135.0 |
| | | **Σ** | **448.0** |

`yours 76.9 / Σ 448.0 = 17.2%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 17.2% = $4.29/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem` ← this one
2. `pvwc-housepopw-2026-11-03-rep`

</details>

</details>
<details><summary><code>pvwc-housepopw-2026-11-03-dem</code> SELL 77 @ 94¢ → $4.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 230 (77 yours) | ×0.5^0 = 229.9 |
|  | 95¢ | 149 | ×0.5^1 = 74.5 |
|  | 97¢ | 69 | ×0.5^3 = 8.6 |
|  | 99¢ | 4,319 | ×0.5^5 = 135.0 |
| | | **Σ** | **448.0** |

`yours 76.9 / Σ 448.0 = 17.2%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 17.2% = $4.29/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem` ← this one
2. `pvwc-housepopw-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 100 @ 25¢ → $0.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 472 (100 yours) | ×0.5^0 = 472.0 |
|  | 26¢ | 306 | ×0.5^1 = 153.0 |
|  | 50¢ | 100 | ×0.5^25 = 0.0 |
|  | 55¢ | 44 | ×0.5^30 = 0.0 |
|  | 97¢ | 38,892 | ×0.5^72 = 0.0 |
| | | **Σ** | **625.0** |

`yours 100.0 / Σ 625.0 = 16.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.0% = $0.62/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 30 @ 40¢ → $0.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 36¢ | 10 | ×0.5^0 = 10.0 |
| ▶ | 40¢ | 30 (30 yours) | ×0.5^4 = 1.9 |
|  | 45¢ | 25 | ×0.5^9 = 0.0 |
|  | 55¢ | 44 | ×0.5^19 = 0.0 |
|  | 98¢ | 63,172 | ×0.5^62 = 0.0 |
| | | **Σ** | **11.9** |

`yours 1.9 / Σ 11.9 = 15.7%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 15.7% = $0.79/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 9 @ 34¢ → $0.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 58 (9 yours) | ×0.5^0 = 58.0 |
|  | 41¢ | 56 | ×0.5^7 = 0.4 |
|  | 45¢ | 25 | ×0.5^11 = 0.0 |
|  | 55¢ | 44 | ×0.5^21 = 0.0 |
|  | 98¢ | 98,906 | ×0.5^64 = 0.0 |
| | | **Σ** | **58.4** |

`yours 9.0 / Σ 58.4 = 15.4%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 15.4% = $0.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 2,000 @ 1¢ → $0.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 15,830 (2,000 yours) | ×0.5^0 = 15,830.0 |
| | | **Σ** | **15,830.0** |

`yours 2,000.0 / Σ 15,830.0 = 12.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 12.6% = $0.49/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 61 @ 16¢ → $1.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 977 (61 yours) | ×0.5^0 = 976.8 |
|  | 26¢ | 587 | ×0.5^10 = 0.6 |
|  | 50¢ | 500 | ×0.5^34 = 0.0 |
| | | **Σ** | **977.4** |

`yours 60.8 / Σ 977.4 = 6.2%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 6.2% = $1.04/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-alito-2026-07-31`
2. `apdc-alito-2026-08-31`
3. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ewc-ref-ca-blntax-2026-11-03-pass</code> SELL 20 @ 44¢ → $2.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 38¢ | 4 | ×0.5^0 = 4.3 |
| ▶ | 44¢ | 49 (20 yours) | ×0.5^6 = 0.8 |
|  | 45¢ | 25 | ×0.5^7 = 0.2 |
|  | 55¢ | 44 | ×0.5^17 = 0.0 |
|  | 99¢ | 63,335 | ×0.5^61 = 0.0 |
| | | **Σ** | **5.2** |

`yours 0.3 / Σ 5.2 = 6.0%`  
`$100 ÷ 1 ÷ 2 = $50.00 × 6.0% = $2.99/day`  

</details>
<details><summary><code>mowc-nato-us-12-31-2026</code> BUY 100 @ 10¢ → $1.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 54 | ×0.5^0 = 54.0 |
| ▶ | 10¢ | 100 (100 yours) | ×0.5^2 = 25.0 |
|  | 5¢ | 51,529 | ×0.5^7 = 402.6 |
| | | **Σ** | **481.6** |

`yours 25.0 / Σ 481.6 = 5.2%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 5.2% = $1.30/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `mowc-nato-us-07-31-2026`
2. `mowc-nato-us-12-31-2026` ← this one

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
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (33,149 resting) | ~28.2% | ~$7.05 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (32,218 resting) | ~18.5% | ~$4.62 |
| `ewc-usgub-ga-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (71,874 resting) | ~13.8% | ~$3.45 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (42,470 resting) | ~13.1% | ~$3.26 |
| `ewc-usgub-ks-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (105,769 resting) | ~11.4% | ~$2.85 |
| `ewc-usse-ne-2026-11-03-danosb` | $100.00 ÷ 3 | 0.50 | 2,000 | BUY side (117,838 resting) | ~14.6% | ~$2.43 |
| `ewc-usgub-wi-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (86,520 resting) | ~8.6% | ~$2.15 |
| `ewc-usgub-ga-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (45,976 resting) | ~7.5% | ~$1.88 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $100.00 ÷ 3 | 0.50 | 2,000 | SELL side (97,259 resting) | ~11.0% | ~$1.83 |
| `ewc-usse-ak-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (133,586 resting) | ~5.2% | ~$1.30 |
| `ewc-usgub-ia-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (129,892 resting) | ~5.0% | ~$1.25 |
| `ewc-usgub-ks-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (156,274 resting) | ~4.8% | ~$1.20 |

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
| 2026-07-25 12:11 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 11:46 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 11:36 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 11:31 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 10:21 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 10:05 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 9:58 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 9:41 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 8:11 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 6:46 AM ET | ✅ ok | 282 | $701.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
