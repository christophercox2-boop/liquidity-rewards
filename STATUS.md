# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-25 5:11 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$34.20/day estimated (ceiling, not promise — details below)

**Earned:** $701.42 lifetime ($155.84 paid). Last three recorded days — 2026-07-23: **$227.63** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-22: **$82.95** · 2026-07-21: **$91.44** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — SELL at the best price, ~$10.10/day for 200 contracts. Runners-up: `ewc-usgub-ia-2026-11-03-rep` (~$3.11/day), `ewc-usgub-ks-2026-11-03-dem` (~$2.25/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$34.20/day (~$1.42/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | BUY | 1.0¢ | 1,986 | 0 | $100.00 | ✅ scoring — ~90.6% of bid side (2,192 resting ≥ 2,000 ✓) ≈ $3.78/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~80.0% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $3.33/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~80.0% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $3.33/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~80.0% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $3.33/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~74.7% of bid side (2,678 resting ≥ 2,000 ✓) ≈ $3.11/day (pool ÷ 12 markets) |
| `iarc-group-2026-12-31-tuccar` | BUY | 1.0¢ | 2,000 | 2 | $100.00 | ✅ scoring — ~71.7% of bid side (2,486 resting ≥ 2,000 ✓) ≈ $3.59/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 5.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~57.5% of ask side (39,508 resting ≥ 2,000 ✓) ≈ $2.88/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 17.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~47.3% of ask side (63,816 resting ≥ 2,000 ✓) ≈ $2.37/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 10.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~42.6% of ask side (103,722 resting ≥ 2,000 ✓) ≈ $1.64/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 20.0¢ | 86 | 0 | $100.00 | ✅ scoring — ~16.8% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.70/day (pool ÷ 12 markets) |
| `ewc-usgub-ca-2026-11-03-stehil` | SELL | 6.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~7.3% of ask side (240,202 resting ≥ 2,000 ✓) ≈ $1.83/day (pool ÷ 2 markets) |
| `ewc-ref-ca-blntax-2026-11-03-pass` | BUY | 38.0¢ | 22 | 3 | $100.00 | ✅ scoring — ~0.2% of bid side (51,608 resting ≥ 2,000 ✓) ≈ $0.11/day |
| `ewc-ref-ca-blntax-2026-11-03-pass` | SELL | 44.0¢ | 16 | 1 | $100.00 | ✅ scoring — ~0.1% of ask side (82,683 resting ≥ 2,000 ✓) ≈ $0.04/day |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 99.0¢ | 132 | 79 | $100.00 | ✅ scoring — ~0.0% of ask side (3,747 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | SELL | 2.0¢ | 14 | 0 | $100.00 | ❌ side has 1,840 of 2,000 Target Size — side not qualifying |
| …and 5 more | | | | | | |

**Tap an order for its book window and the math:**

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 5¢ → $2.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 2 (1 yours) | ×0.5^0 = 1.5 |
|  | 12¢ | 28 | ×0.5^7 = 0.2 |
|  | 43¢ | 2,000 | ×0.5^38 = 0.0 |
| | | **Σ** | **1.7** |

`yours 1.0 / Σ 1.7 = 57.5%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 57.5% = $2.88/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 20 @ 17¢ → $2.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 42 (20 yours) | ×0.5^0 = 42.0 |
|  | 24¢ | 29 | ×0.5^7 = 0.2 |
|  | 40¢ | 16 | ×0.5^23 = 0.0 |
|  | 45¢ | 25 | ×0.5^28 = 0.0 |
|  | 97¢ | 56 | ×0.5^80 = 0.0 |
|  | 98¢ | 63,149 | ×0.5^81 = 0.0 |
| | | **Σ** | **42.2** |

`yours 20.0 / Σ 42.2 = 47.3%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 47.3% = $2.37/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 100 @ 10¢ → $1.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 235 (100 yours) | ×0.5^0 = 235.0 |
|  | 50¢ | 100 | ×0.5^40 = 0.0 |
|  | 97¢ | 53,892 | ×0.5^87 = 0.0 |
| | | **Σ** | **235.0** |

`yours 100.0 / Σ 235.0 = 42.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 42.6% = $1.64/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 86 @ 20¢ → $0.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 511 (86 yours) | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
|  | 99¢ | 2,981 | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 85.7 / Σ 510.7 = 16.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.8% = $0.70/day`  

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
<details><summary><code>ewc-usgub-ca-2026-11-03-stehil</code> SELL 20 @ 6¢ → $1.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 20 (20 yours) | ×0.5^0 = 19.8 |
|  | 9¢ | 2,000 | ×0.5^3 = 250.0 |
| | | **Σ** | **269.8** |

`yours 19.8 / Σ 269.8 = 7.3%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 7.3% = $1.83/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usgub-ca-2026-11-03-stehil` ← this one
2. `ewc-usgub-ca-2026-11-03-xavbec`

</details>

</details>
<details><summary><code>ewc-ref-ca-blntax-2026-11-03-pass</code> BUY 22 @ 38¢ → $0.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 41¢ | 450 | ×0.5^0 = 450.0 |
|  | 39¢ | 115 | ×0.5^2 = 28.8 |
| ▶ | 38¢ | 57 (22 yours) | ×0.5^3 = 7.1 |
|  | 35¢ | 45,786 | ×0.5^6 = 715.4 |
| | | **Σ** | **1,201.2** |

`yours 2.7 / Σ 1,201.2 = 0.2%`  
`$100 ÷ 1 ÷ 2 = $50.00 × 0.2% = $0.11/day`  

</details>
<details><summary><code>ewc-ref-ca-blntax-2026-11-03-pass</code> SELL 16 @ 44¢ → $0.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 43¢ | 70 | ×0.5^0 = 70.0 |
| ▶ | 44¢ | 45 (16 yours) | ×0.5^1 = 22.5 |
|  | 45¢ | 43,742 | ×0.5^2 = 10,935.5 |
| | | **Σ** | **11,028.0** |

`yours 8.0 / Σ 11,028.0 = 0.1%`  
`$100 ÷ 1 ÷ 2 = $50.00 × 0.1% = $0.04/day`  

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 132 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 511 | ×0.5^0 = 510.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
| ▶ | 99¢ | 2,981 (132 yours) | ×0.5^79 = 0.0 |
| | | **Σ** | **510.7** |

`yours 0.0 / Σ 510.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> SELL 14 @ 2¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 14 (14 yours) | ×0.5^0 = 14.5 |
|  | 29¢ | 500 | ×0.5^27 = 0.0 |
|  | 31¢ | 100 | ×0.5^29 = 0.0 |
|  | 32¢ | 100 | ×0.5^30 = 0.0 |
|  | 48¢ | 100 | ×0.5^46 = 0.0 |
|  | 50¢ | 25 | ×0.5^48 = 0.0 |
|  | 99¢ | 1,000 | ×0.5^97 = 0.0 |

`side 1,840 < target 2,000 → side pays nobody`  

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
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (54,746 resting) | ~40.4% | ~$10.10 |
| `ewc-usgub-ia-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (45,849 resting) | ~12.4% | ~$3.11 |
| `ewc-usgub-ks-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (107,313 resting) | ~9.0% | ~$2.25 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (27,272 resting) | ~9.0% | ~$2.24 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (48,869 resting) | ~8.7% | ~$2.17 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (33,540 resting) | ~8.4% | ~$2.10 |
| `ewc-usgub-wi-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (50,390 resting) | ~8.4% | ~$2.09 |
| `ewc-usgub-ga-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (42,905 resting) | ~8.2% | ~$2.05 |
| `ewc-usgub-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (73,414 resting) | ~7.4% | ~$1.85 |
| `ewc-usse-ia-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (158,433 resting) | ~7.1% | ~$1.76 |
| `ewc-usgub-az-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (86,652 resting) | ~6.7% | ~$1.68 |
| `ewc-usgub-az-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (63,586 resting) | ~6.5% | ~$1.62 |

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
| 2026-07-25 5:11 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 4:14 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 4:08 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 4:03 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 3:51 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 3:48 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 3:38 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 3:35 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 2:59 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 2:48 PM ET | ✅ ok | 282 | $701.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
