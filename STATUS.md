# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-25 11:31 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$71.51/day estimated (ceiling, not promise — details below)

**Earned:** $701.42 lifetime ($155.84 paid). Last three recorded days — 2026-07-23: **$227.63** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-22: **$82.95** · 2026-07-21: **$91.44** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ia-2026-11-03-rep` — BUY at the best price, ~$9.13/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$7.05/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$4.62/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$71.51/day (~$2.98/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~80.0% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $3.33/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~80.0% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $3.33/day (pool ÷ 12 markets) |
| `iarc-group-2026-12-31-tuccar` | BUY | 1.0¢ | 2,000 | 1 | $100.00 | ✅ scoring — ~61.4% of bid side (3,255 resting ≥ 2,000 ✓) ≈ $3.07/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 5.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~61.4% of ask side (39,508 resting ≥ 2,000 ✓) ≈ $3.07/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | BUY | 2.0¢ | 2,001 | 0 | $100.00 | ✅ scoring — ~61.0% of bid side (34,332 resting ≥ 2,000 ✓) ≈ $3.05/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 2.0¢ | 400 | 0 | $100.00 | ✅ scoring — ~53.6% of ask side (3,373 resting ≥ 2,000 ✓) ≈ $2.23/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 34.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~51.3% of ask side (99,589 resting ≥ 2,000 ✓) ≈ $2.57/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 49.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~50.0% of ask side (103,564 resting ≥ 2,000 ✓) ≈ $1.92/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | BUY | 1.0¢ | 2,000 | 2 | $100.00 | ✅ scoring — ~49.7% of bid side (2,887 resting ≥ 2,000 ✓) ≈ $2.07/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~45.3% of bid side (4,418 resting ≥ 2,000 ✓) ≈ $1.89/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~44.4% of bid side (4,500 resting ≥ 2,000 ✓) ≈ $1.85/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 12.0¢ | 200 | 0 | $100.00 | ✅ scoring — ~33.7% of bid side (200,795 resting ≥ 2,000 ✓) ≈ $1.29/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | BUY | 25.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~32.7% of bid side (7,972 resting ≥ 2,000 ✓) ≈ $1.63/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~28.3% of bid side (7,057 resting ≥ 2,000 ✓) ≈ $1.18/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 93.0¢ | 78 | 0 | $100.00 | ✅ scoring — ~27.6% of ask side (3,254 resting ≥ 2,000 ✓) ≈ $1.15/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 24.0¢ | 70 | 1 | $100.00 | ✅ scoring — ~25.9% of ask side (63,951 resting ≥ 2,000 ✓) ≈ $1.30/day (pool ÷ 10 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 34.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~24.3% of bid side (10,943 resting ≥ 2,000 ✓) ≈ $12.14/day |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 2.0¢ | 2,001 | 0 | $100.00 | ✅ scoring — ~23.9% of bid side (14,432 resting ≥ 2,000 ✓) ≈ $1.19/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~21.6% of ask side (3,744 resting ≥ 2,000 ✓) ≈ $0.90/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 25.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~21.2% of ask side (89,003 resting ≥ 2,000 ✓) ≈ $0.81/day (pool ÷ 13 markets) |
| `pvwc-housepopw-2026-11-03-dem` | SELL | 94.0¢ | 77 | 0 | $100.00 | ✅ scoring — ~20.6% of ask side (4,618 resting ≥ 2,000 ✓) ≈ $5.15/day (pool ÷ 2 markets) |
| `pvwc-housepopw-2026-11-03-dem` | SELL | 94.0¢ | 77 | 0 | $100.00 | ✅ scoring — ~20.6% of ask side (4,618 resting ≥ 2,000 ✓) ≈ $5.15/day (pool ÷ 2 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | SELL | 14.0¢ | 11 | 1 | $100.00 | ✅ scoring — ~16.4% of ask side (39,620 resting ≥ 2,000 ✓) ≈ $0.82/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~16.1% of bid side (12,450 resting ≥ 2,000 ✓) ≈ $0.62/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 34.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~15.4% of ask side (99,589 resting ≥ 2,000 ✓) ≈ $0.77/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 48.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~10.2% of ask side (111,654 resting ≥ 2,000 ✓) ≈ $0.39/day (pool ÷ 13 markets) |
| `stsc-bab-el-mandeb-clsd-2026-07-31` | BUY | 6.0¢ | 500 | 0 | $250.00 | ✅ scoring — ~9.4% of bid side (6,553 resting ≥ 2,000 ✓) ≈ $3.92/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 49.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~8.3% of ask side (126,048 resting ≥ 2,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 8.0¢ | 200 | 6 | $100.00 | ✅ scoring — ~7.9% of bid side (50,425 resting ≥ 2,000 ✓) ≈ $0.31/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 49.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~6.6% of ask side (75,932 resting ≥ 2,000 ✓) ≈ $0.25/day (pool ÷ 13 markets) |
| …and 54 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-sc-2026-08-11-rep-wiltim</code> BUY 2,000 @ 1¢ → $3.33/day</summary>

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
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-nanmac</code> BUY 2,000 @ 1¢ → $3.33/day</summary>

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
6. `enwc-ussep-sc-2026-08-11-rep-nanmac` ← this one
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>iarc-group-2026-12-31-tuccar</code> BUY 2,000 @ 1¢ → $3.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 3 | ×0.5^0 = 3.0 |
| ▶ | 1¢ | 3,252 (2,000 yours) | ×0.5^1 = 1,626.0 |
| | | **Σ** | **1,629.0** |

`yours 1,000.0 / Σ 1,629.0 = 61.4%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 61.4% = $3.07/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 5¢ → $3.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 2 (1 yours) | ×0.5^0 = 1.5 |
|  | 13¢ | 28 | ×0.5^8 = 0.1 |
|  | 43¢ | 2,000 | ×0.5^38 = 0.0 |
| | | **Σ** | **1.6** |

`yours 1.0 / Σ 1.6 = 61.4%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 61.4% = $3.07/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> BUY 2,001 @ 2¢ → $3.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 3,280 (2,001 yours) | ×0.5^0 = 3,280.0 |
| | | **Σ** | **3,280.0** |

`yours 2,001.0 / Σ 3,280.0 = 61.0%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 61.0% = $3.05/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 400 @ 2¢ → $2.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 746 (400 yours) | ×0.5^0 = 746.0 |
|  | 50¢ | 25 | ×0.5^48 = 0.0 |
|  | 55¢ | 44 | ×0.5^53 = 0.0 |
|  | 99¢ | 2,558 | ×0.5^97 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 100 @ 49¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 150 (100 yours) | ×0.5^0 = 150.0 |
|  | 50¢ | 100 | ×0.5^1 = 50.0 |
|  | 97¢ | 53,855 | ×0.5^48 = 0.0 |
| | | **Σ** | **200.0** |

`yours 100.0 / Σ 200.0 = 50.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 50.0% = $1.92/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> BUY 2,000 @ 1¢ → $2.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 124 | ×0.5^0 = 124.0 |
|  | 2¢ | 763 | ×0.5^1 = 381.5 |
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.5^2 = 500.0 |
| | | **Σ** | **1,005.5** |

`yours 500.0 / Σ 1,005.5 = 49.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.7% = $2.07/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-andbau</code> BUY 2,000 @ 1¢ → $1.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,418 (2,000 yours) | ×0.5^0 = 4,418.0 |
| | | **Σ** | **4,418.0** |

`yours 2,000.0 / Σ 4,418.0 = 45.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 45.3% = $1.89/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> BUY 50 @ 25¢ → $1.63/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 113 (50 yours) | ×0.5^0 = 113.0 |
|  | 24¢ | 80 | ×0.5^1 = 40.0 |
|  | 12¢ | 28 | ×0.5^13 = 0.0 |
|  | 2¢ | 2,251 | ×0.5^23 = 0.0 |
| | | **Σ** | **153.0** |

`yours 50.0 / Σ 153.0 = 32.7%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 32.7% = $1.63/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-paudan</code> BUY 2,000 @ 1¢ → $1.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 7,057 (2,000 yours) | ×0.5^0 = 7,057.0 |
| | | **Σ** | **7,057.0** |

`yours 2,000.0 / Σ 7,057.0 = 28.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 28.3% = $1.18/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 70 @ 24¢ → $1.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 100 | ×0.5^0 = 100.0 |
| ▶ | 24¢ | 70 (70 yours) | ×0.5^1 = 35.0 |
|  | 32¢ | 29 | ×0.5^9 = 0.1 |
|  | 40¢ | 16 | ×0.5^17 = 0.0 |
|  | 45¢ | 25 | ×0.5^22 = 0.0 |
|  | 55¢ | 44 | ×0.5^32 = 0.0 |
|  | 98¢ | 63,168 | ×0.5^75 = 0.0 |
| | | **Σ** | **135.1** |

`yours 35.0 / Σ 135.1 = 25.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 25.9% = $1.30/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 100 @ 34¢ → $12.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 36¢ | 28 | ×0.5^0 = 28.0 |
|  | 35¢ | 100 | ×0.5^1 = 50.0 |
| ▶ | 34¢ | 100 (100 yours) | ×0.5^2 = 25.0 |
|  | 19¢ | 515 | ×0.5^17 = 0.0 |
|  | 2¢ | 10,000 | ×0.5^34 = 0.0 |
| | | **Σ** | **103.0** |

`yours 25.0 / Σ 103.0 = 24.3%`  
`$100 ÷ 1 ÷ 2 = $50.00 × 24.3% = $12.14/day`  

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 2,001 @ 2¢ → $1.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 8,380 (2,001 yours) | ×0.5^0 = 8,380.0 |
| | | **Σ** | **8,380.0** |

`yours 2,001.0 / Σ 8,380.0 = 23.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 23.9% = $1.19/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 100 @ 20¢ → $0.90/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 464 (100 yours) | ×0.5^0 = 464.0 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 55¢ | 44 | ×0.5^35 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
|  | 99¢ | 2,981 | ×0.5^79 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 100 @ 25¢ → $0.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 472 (100 yours) | ×0.5^0 = 472.0 |
|  | 50¢ | 100 | ×0.5^25 = 0.0 |
|  | 55¢ | 44 | ×0.5^30 = 0.0 |
|  | 97¢ | 38,892 | ×0.5^72 = 0.0 |
| | | **Σ** | **472.0** |

`yours 100.0 / Σ 472.0 = 21.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 21.2% = $0.81/day`  

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
<details><summary><code>pvwc-housepopw-2026-11-03-dem</code> SELL 77 @ 94¢ → $5.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 230 (77 yours) | ×0.5^0 = 229.9 |
|  | 97¢ | 69 | ×0.5^3 = 8.6 |
|  | 99¢ | 4,319 | ×0.5^5 = 135.0 |
| | | **Σ** | **373.5** |

`yours 76.9 / Σ 373.5 = 20.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 20.6% = $5.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem` ← this one
2. `pvwc-housepopw-2026-11-03-rep`

</details>

</details>
<details><summary><code>pvwc-housepopw-2026-11-03-dem</code> SELL 77 @ 94¢ → $5.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 230 (77 yours) | ×0.5^0 = 229.9 |
|  | 97¢ | 69 | ×0.5^3 = 8.6 |
|  | 99¢ | 4,319 | ×0.5^5 = 135.0 |
| | | **Σ** | **373.5** |

`yours 76.9 / Σ 373.5 = 20.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 20.6% = $5.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem` ← this one
2. `pvwc-housepopw-2026-11-03-rep`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> SELL 11 @ 14¢ → $0.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 25 | ×0.5^0 = 25.0 |
| ▶ | 14¢ | 16 (11 yours) | ×0.5^1 = 8.0 |
|  | 20¢ | 57 | ×0.5^7 = 0.4 |
|  | 43¢ | 2,000 | ×0.5^30 = 0.0 |
| | | **Σ** | **33.4** |

`yours 5.5 / Σ 33.4 = 16.4%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 16.4% = $0.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 2,000 @ 1¢ → $0.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,450 (2,000 yours) | ×0.5^0 = 12,450.0 |
| | | **Σ** | **12,450.0** |

`yours 2,000.0 / Σ 12,450.0 = 16.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.1% = $0.62/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 100 @ 48¢ → $0.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 47¢ | 427 | ×0.5^0 = 427.0 |
| ▶ | 48¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 50¢ | 100 | ×0.5^3 = 12.5 |
|  | 97¢ | 100,026 | ×0.5^50 = 0.0 |
| | | **Σ** | **489.5** |

`yours 50.0 / Σ 489.5 = 10.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 10.2% = $0.39/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 100 @ 49¢ → $0.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 48¢ | 529 | ×0.5^0 = 529.0 |
| ▶ | 49¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 50¢ | 100 | ×0.5^2 = 25.0 |
|  | 98¢ | 1,000 | ×0.5^50 = 0.0 |
|  | 99¢ | 124,319 | ×0.5^51 = 0.0 |
| | | **Σ** | **604.0** |

`yours 50.0 / Σ 604.0 = 8.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.3% = $0.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 200 @ 8¢ → $0.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 23 | ×0.5^0 = 23.0 |
|  | 13¢ | 2 | ×0.5^1 = 1.0 |
| ▶ | 8¢ | 200 (200 yours) | ×0.5^6 = 3.1 |
|  | 2¢ | 50,000 | ×0.5^12 = 12.2 |
| | | **Σ** | **39.3** |

`yours 3.1 / Σ 39.3 = 7.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.9% = $0.31/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 100 @ 49¢ → $0.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 48¢ | 681 | ×0.5^0 = 681.0 |
| ▶ | 49¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 50¢ | 100 | ×0.5^2 = 25.0 |
|  | 97¢ | 25,555 | ×0.5^49 = 0.0 |
| | | **Σ** | **756.0** |

`yours 50.0 / Σ 756.0 = 6.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.6% = $0.25/day`  

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
| `ewc-usgub-ia-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (44,507 resting) | ~36.5% | ~$9.13 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (31,562 resting) | ~28.2% | ~$7.05 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (32,218 resting) | ~18.5% | ~$4.62 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (32,003 resting) | ~17.6% | ~$4.40 |
| `ewc-usgub-ks-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (105,773 resting) | ~11.4% | ~$2.85 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (2,671 resting) | ~10.7% | ~$2.67 |
| `ewc-usgub-ks-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (126,448 resting) | ~9.8% | ~$2.45 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $100.00 ÷ 3 | 0.50 | 2,000 | BUY side (137,201 resting) | ~14.2% | ~$2.37 |
| `ewc-usgub-ga-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (45,976 resting) | ~7.5% | ~$1.88 |
| `ewc-usgub-ga-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (109,476 resting) | ~6.7% | ~$1.67 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $100.00 ÷ 3 | 0.50 | 2,000 | SELL side (97,557 resting) | ~9.6% | ~$1.60 |
| `apdc-jerpowgov-2026-07-31` | $100.00 ÷ 3 | 0.50 | 2,000 | BUY side (2,060 resting) | ~8.8% | ~$1.47 |

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
| 2026-07-25 11:31 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 10:21 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 10:05 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 9:58 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 9:41 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 8:11 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 6:46 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 5:14 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 2:31 AM ET | ✅ ok | 282 | $701.42 |
| 2026-07-24 11:43 PM ET | ✅ ok | 282 | $701.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
