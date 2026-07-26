# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-26 5:27 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$65.10/day estimated (ceiling, not promise — details below)

**Earned:** $836.61 lifetime ($155.84 paid). Last three recorded days — 2026-07-24: **$135.19** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-23: **$227.63** · 2026-07-22: **$82.95** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — BUY at the best price, ~$15.10/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-angcra` (~$10.45/day), `ewc-usgub-ia-2026-11-03-rep` (~$5.55/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$65.10/day (~$2.71/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-48` | SELL | 10.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (103,587 resting ≥ 2,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 20.0¢ | 86 | 0 | $100.00 | ✅ scoring — ~99.6% of ask side (2,227 resting ≥ 2,000 ✓) ≈ $4.15/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~80.0% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $3.33/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | BUY | 1.0¢ | 2,000 | 3 | $100.00 | ✅ scoring — ~79.7% of bid side (2,501 resting ≥ 2,000 ✓) ≈ $3.32/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~79.7% of bid side (2,510 resting ≥ 2,000 ✓) ≈ $3.32/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-alawil` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~74.7% of bid side (2,678 resting ≥ 2,000 ✓) ≈ $3.11/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~74.7% of bid side (2,678 resting ≥ 2,000 ✓) ≈ $3.11/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-pameve` | BUY | 1.0¢ | 2,000 | 1 | $100.00 | ✅ scoring — ~66.7% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~42.4% of bid side (4,716 resting ≥ 2,000 ✓) ≈ $1.77/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-tregow` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~42.1% of bid side (4,750 resting ≥ 2,000 ✓) ≈ $1.75/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 5.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~41.6% of ask side (42,041 resting ≥ 2,000 ✓) ≈ $2.08/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~39.9% of bid side (5,010 resting ≥ 2,000 ✓) ≈ $1.66/day (pool ÷ 12 markets) |
| `cranc-uspres28-12-31-2026-dontru` | BUY | 10.0¢ | 200 | 0 | $100.00 | ✅ scoring — ~33.3% of bid side (120,546 resting ≥ 2,000 ✓) ≈ $0.50/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-robken` | BUY | 9.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~24.3% of bid side (70,343 resting ≥ 2,000 ✓) ≈ $0.37/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-betoro` | BUY | 6.0¢ | 1,000 | 2 | $100.00 | ✅ scoring — ~23.0% of bid side (25,544 resting ≥ 2,000 ✓) ≈ $0.35/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-stesmi` | BUY | 5.0¢ | 1,000 | 1 | $100.00 | ✅ scoring — ~19.1% of bid side (20,437 resting ≥ 2,000 ✓) ≈ $0.29/day (pool ÷ 33 markets) |
| `pintc-meet-trump-2026-12-31-leoxiv` | BUY | 2.0¢ | 2,000 | 1 | $100.00 | ✅ scoring — ~16.6% of bid side (62,212 resting ≥ 2,000 ✓) ≈ $0.64/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 17.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~16.6% of ask side (63,796 resting ≥ 2,000 ✓) ≈ $0.83/day (pool ÷ 10 markets) |
| `cranc-uspres28-12-31-2026-hilcli` | BUY | 2.0¢ | 2,000 | 1 | $100.00 | ✅ scoring — ~16.6% of bid side (53,236 resting ≥ 2,000 ✓) ≈ $0.25/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-krinoe` | BUY | 6.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~14.8% of bid side (30,615 resting ≥ 2,000 ✓) ≈ $0.22/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 4.0¢ | 1,000 | 1 | $100.00 | ✅ scoring — ~13.7% of bid side (27,158 resting ≥ 2,000 ✓) ≈ $0.53/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-erikir` | BUY | 3.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~10.7% of bid side (29,662 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-nikhal` | BUY | 3.0¢ | 2,000 | 1 | $100.00 | ✅ scoring — ~10.7% of bid side (29,926 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-dontrujr` | BUY | 3.0¢ | 2,000 | 2 | $100.00 | ✅ scoring — ~10.3% of bid side (30,510 resting ≥ 2,000 ✓) ≈ $0.16/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-steban` | BUY | 8.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~9.5% of bid side (65,460 resting ≥ 2,000 ✓) ≈ $0.14/day (pool ÷ 33 markets) |
| `pintc-meet-trump-2026-12-31-delrod` | BUY | 4.0¢ | 500 | 1 | $100.00 | ✅ scoring — ~9.0% of bid side (55,708 resting ≥ 2,000 ✓) ≈ $0.35/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~9.0% of bid side (55,450 resting ≥ 2,000 ✓) ≈ $0.35/day (pool ÷ 13 markets) |
| `mlaec-swepm-2026-09-13-magand` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~9.0% of bid side (22,200 resting ≥ 2,000 ✓) ≈ $0.90/day (pool ÷ 5 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 1.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~9.0% of bid side (22,200 resting ≥ 2,000 ✓) ≈ $0.38/day (pool ÷ 12 markets) |
| `vtc-hrep-to-2026-11-03-100-105m` | BUY | 2.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~8.9% of bid side (47,616 resting ≥ 2,000 ✓) ≈ $0.45/day (pool ÷ 10 markets) |
| …and 103 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 100 @ 10¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 100 (100 yours) | ×0.5^0 = 100.0 |
|  | 50¢ | 100 | ×0.5^40 = 0.0 |
|  | 97¢ | 53,892 | ×0.5^87 = 0.0 |
| | | **Σ** | **100.0** |

`yours 100.0 / Σ 100.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 86 @ 20¢ → $4.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 86 (86 yours) | ×0.5^0 = 85.7 |
|  | 22¢ | 1 | ×0.5^2 = 0.3 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
|  | 99¢ | 1,885 | ×0.5^79 = 0.0 |
| | | **Σ** | **86.0** |

`yours 85.7 / Σ 86.0 = 99.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.6% = $4.15/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> BUY 2,000 @ 1¢ → $3.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 1 | ×0.5^0 = 1.0 |
| ▶ | 1¢ | 2,500 (2,000 yours) | ×0.5^3 = 312.5 |
| | | **Σ** | **313.5** |

`yours 250.0 / Σ 313.5 = 79.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 79.7% = $3.32/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-paudan</code> BUY 2,000 @ 1¢ → $3.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,510 (2,000 yours) | ×0.5^0 = 2,510.0 |
| | | **Σ** | **2,510.0** |

`yours 2,000.0 / Σ 2,510.0 = 79.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 79.7% = $3.32/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-alawil</code> BUY 2,000 @ 1¢ → $3.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,678 (2,000 yours) | ×0.5^0 = 2,678.0 |
| | | **Σ** | **2,678.0** |

`yours 2,000.0 / Σ 2,678.0 = 74.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 74.7% = $3.11/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-pameve</code> BUY 2,000 @ 1¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 500 | ×0.5^0 = 500.0 |
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.5^1 = 1,000.0 |
| | | **Σ** | **1,500.0** |

`yours 1,000.0 / Σ 1,500.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve` ← this one
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> BUY 2,000 @ 1¢ → $1.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,716 (2,000 yours) | ×0.5^0 = 4,716.0 |
| | | **Σ** | **4,716.0** |

`yours 2,000.0 / Σ 4,716.0 = 42.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 42.4% = $1.77/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-tregow</code> BUY 2,000 @ 1¢ → $1.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,750 (2,000 yours) | ×0.5^0 = 4,750.0 |
| | | **Σ** | **4,750.0** |

`yours 2,000.0 / Σ 4,750.0 = 42.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 42.1% = $1.75/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 5¢ → $2.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.5^0 = 1.0 |
|  | 10¢ | 28 | ×0.5^5 = 0.9 |
|  | 11¢ | 34 | ×0.5^6 = 0.5 |
|  | 43¢ | 2,000 | ×0.5^38 = 0.0 |
| | | **Σ** | **2.4** |

`yours 1.0 / Σ 2.4 = 41.6%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 41.6% = $2.08/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-nanmac</code> BUY 2,000 @ 1¢ → $1.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,010 (2,000 yours) | ×0.5^0 = 5,010.0 |
| | | **Σ** | **5,010.0** |

`yours 2,000.0 / Σ 5,010.0 = 39.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 39.9% = $1.66/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-dontru</code> BUY 200 @ 10¢ → $0.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 362 (200 yours) | ×0.5^0 = 362.0 |
|  | 9¢ | 9 | ×0.5^1 = 4.5 |
|  | 1¢ | 120,175 | ×0.5^9 = 234.7 |
| | | **Σ** | **601.2** |

`yours 200.0 / Σ 601.2 = 33.3%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 33.3% = $0.50/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru` ← this one
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
<details><summary><code>cranc-uspres28-12-31-2026-robken</code> BUY 100 @ 9¢ → $0.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.5^0 = 1.0 |
|  | 10¢ | 3 | ×0.5^1 = 1.5 |
| ▶ | 9¢ | 126 (100 yours) | ×0.5^2 = 31.5 |
|  | 6¢ | 6 | ×0.5^5 = 0.2 |
|  | 1¢ | 70,207 | ×0.5^10 = 68.6 |
| | | **Σ** | **102.7** |

`yours 25.0 / Σ 102.7 = 24.3%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 24.3% = $0.37/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-betoro</code> BUY 1,000 @ 6¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 1 | ×0.5^0 = 1.0 |
| ▶ | 6¢ | 4,343 (1,000 yours) | ×0.5^2 = 1,085.8 |
| | | **Σ** | **1,086.8** |

`yours 250.0 / Σ 1,086.8 = 23.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 23.0% = $0.35/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro` ← this one
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
<details><summary><code>cranc-uspres28-12-31-2026-stesmi</code> BUY 1,000 @ 5¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 3 | ×0.5^0 = 3.0 |
| ▶ | 5¢ | 5,234 (1,000 yours) | ×0.5^1 = 2,617.0 |
| | | **Σ** | **2,620.0** |

`yours 500.0 / Σ 2,620.0 = 19.1%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 19.1% = $0.29/day`  

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
29. `cranc-uspres28-12-31-2026-stesmi` ← this one
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>pintc-meet-trump-2026-12-31-leoxiv</code> BUY 2,000 @ 2¢ → $0.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 12 | ×0.5^0 = 12.0 |
| ▶ | 2¢ | 12,000 (2,000 yours) | ×0.5^1 = 6,000.0 |
| | | **Σ** | **6,012.0** |

`yours 1,000.0 / Σ 6,012.0 = 16.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.6% = $0.64/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon`
6. `pintc-meet-trump-2026-12-31-kimkar`
7. `pintc-meet-trump-2026-12-31-leoxiv` ← this one
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput`
11. `pintc-meet-trump-2026-12-31-volzel`
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 20 @ 17¢ → $0.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 50 | ×0.5^0 = 50.0 |
| ▶ | 17¢ | 20 (20 yours) | ×0.5^1 = 10.0 |
|  | 23¢ | 6 | ×0.5^7 = 0.0 |
|  | 24¢ | 29 | ×0.5^8 = 0.1 |
|  | 45¢ | 25 | ×0.5^29 = 0.0 |
|  | 97¢ | 56 | ×0.5^81 = 0.0 |
|  | 98¢ | 63,110 | ×0.5^82 = 0.0 |
| | | **Σ** | **60.2** |

`yours 10.0 / Σ 60.2 = 16.6%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 16.6% = $0.83/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-hilcli</code> BUY 2,000 @ 2¢ → $0.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 36 | ×0.5^0 = 36.0 |
| ▶ | 2¢ | 12,000 (2,000 yours) | ×0.5^1 = 6,000.0 |
| | | **Σ** | **6,036.0** |

`yours 1,000.0 / Σ 6,036.0 = 16.6%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 16.6% = $0.25/day`  

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
12. `cranc-uspres28-12-31-2026-hilcli` ← this one
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
<details><summary><code>cranc-uspres28-12-31-2026-krinoe</code> BUY 200 @ 6¢ → $0.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 5 | ×0.5^0 = 5.0 |
| ▶ | 6¢ | 391 (200 yours) | ×0.5^1 = 195.5 |
|  | 5¢ | 19 | ×0.5^2 = 4.8 |
|  | 1¢ | 30,200 | ×0.5^6 = 471.9 |
| | | **Σ** | **677.1** |

`yours 100.0 / Σ 677.1 = 14.8%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 14.8% = $0.22/day`  

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
18. `cranc-uspres28-12-31-2026-krinoe` ← this one
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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 1,000 @ 4¢ → $0.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 333 | ×0.5^0 = 333.0 |
| ▶ | 4¢ | 6,625 (1,000 yours) | ×0.5^1 = 3,312.5 |
| | | **Σ** | **3,645.5** |

`yours 500.0 / Σ 3,645.5 = 13.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 13.7% = $0.53/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-erikir</code> BUY 2,000 @ 3¢ → $0.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 18,657 (2,000 yours) | ×0.5^0 = 18,657.0 |
| | | **Σ** | **18,657.0** |

`yours 2,000.0 / Σ 18,657.0 = 10.7%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 10.7% = $0.16/day`  

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
10. `cranc-uspres28-12-31-2026-erikir` ← this one
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
<details><summary><code>cranc-uspres28-12-31-2026-nikhal</code> BUY 2,000 @ 3¢ → $0.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 50 | ×0.5^0 = 50.0 |
| ▶ | 3¢ | 18,666 (2,000 yours) | ×0.5^1 = 9,333.0 |
| | | **Σ** | **9,383.0** |

`yours 1,000.0 / Σ 9,383.0 = 10.7%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 10.7% = $0.16/day`  

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
23. `cranc-uspres28-12-31-2026-nikhal` ← this one
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
<details><summary><code>cranc-uspres28-12-31-2026-dontrujr</code> BUY 2,000 @ 3¢ → $0.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 9 | ×0.5^0 = 9.0 |
| ▶ | 3¢ | 19,316 (2,000 yours) | ×0.5^2 = 4,829.0 |
| | | **Σ** | **4,838.0** |

`yours 500.0 / Σ 4,838.0 = 10.3%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 10.3% = $0.16/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru`
7. `cranc-uspres28-12-31-2026-dontrujr` ← this one
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
<details><summary><code>cranc-uspres28-12-31-2026-steban</code> BUY 500 @ 8¢ → $0.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 5,250 (500 yours) | ×0.5^0 = 5,250.0 |
| | | **Σ** | **5,250.0** |

`yours 500.0 / Σ 5,250.0 = 9.5%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 9.5% = $0.14/day`  

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
28. `cranc-uspres28-12-31-2026-steban` ← this one
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>pintc-meet-trump-2026-12-31-delrod</code> BUY 500 @ 4¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 16 | ×0.5^0 = 16.0 |
| ▶ | 4¢ | 5,500 (500 yours) | ×0.5^1 = 2,750.0 |
| | | **Σ** | **2,766.0** |

`yours 250.0 / Σ 2,766.0 = 9.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.0% = $0.35/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod` ← this one
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon`
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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 5,000 @ 1¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 55,450 (5,000 yours) | ×0.5^0 = 55,450.0 |
| | | **Σ** | **55,450.0** |

`yours 5,000.0 / Σ 55,450.0 = 9.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.0% = $0.35/day`  

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
<details><summary><code>mlaec-swepm-2026-09-13-magand</code> BUY 2,000 @ 1¢ → $0.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 22,200 (2,000 yours) | ×0.5^0 = 22,200.0 |
| | | **Σ** | **22,200.0** |

`yours 2,000.0 / Σ 22,200.0 = 9.0%`  
`$100 ÷ 5 ÷ 2 = $10.00 × 9.0% = $0.90/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `mlaec-swepm-2026-09-13-ebbbus`
2. `mlaec-swepm-2026-09-13-jimake`
3. `mlaec-swepm-2026-09-13-magand` ← this one
4. `mlaec-swepm-2026-09-13-noodad`
5. `mlaec-swepm-2026-09-13-ulfkri`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 2,000 @ 1¢ → $0.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 22,200 (2,000 yours) | ×0.5^0 = 22,200.0 |
| | | **Σ** | **22,200.0** |

`yours 2,000.0 / Σ 22,200.0 = 9.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 9.0% = $0.38/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180` ← this one
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>vtc-hrep-to-2026-11-03-100-105m</code> BUY 2,000 @ 2¢ → $0.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 22,416 (2,000 yours) | ×0.5^0 = 22,416.0 |
| | | **Σ** | **22,416.0** |

`yours 2,000.0 / Σ 22,416.0 = 8.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 8.9% = $0.45/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vtc-hrep-to-2026-11-03-100-105m` ← this one
2. `vtc-hrep-to-2026-11-03-105-110m`
3. `vtc-hrep-to-2026-11-03-110-115m`
4. `vtc-hrep-to-2026-11-03-115-120m`
5. `vtc-hrep-to-2026-11-03-120-125m`
6. `vtc-hrep-to-2026-11-03-125-130m`
7. `vtc-hrep-to-2026-11-03-90-95m`
8. `vtc-hrep-to-2026-11-03-95-100m`
9. `vtc-hrep-to-2026-11-03-gte130m`
10. `vtc-hrep-to-2026-11-03-lt90m`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-23 | ~$136.30 | $227.63 | 167% |
| 2026-07-22 | ~$110.63 | $82.95 | 75% |
| 2026-07-21 | ~$87.94 | $91.44 | 104% |

Biggest gaps on 2026-07-23: `opdc-trump-resig-2027-12-31` (est ~$2.12 → got $0.00), `scc-senate-gop-2026-11-03-55` (est ~$2.14 → got $0.44), `stsc-hormuz-normal-aug31` (est ~$1.67 → got $0.01)

_2026-07-24 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (12,054 resting) | ~60.4% | ~$15.10 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (49,358 resting) | ~41.8% | ~$10.45 |
| `ewc-usgub-ia-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (45,675 resting) | ~22.2% | ~$5.55 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (75,404 resting) | ~16.9% | ~$4.22 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (32,391 resting) | ~14.6% | ~$3.64 |
| `ewc-usgub-ks-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (108,008 resting) | ~12.6% | ~$3.14 |
| `ewc-usgub-ks-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (181,041 resting) | ~10.2% | ~$2.56 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (1,992 resting) | ~9.1% | ~$2.28 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (91,927 resting) | ~6.4% | ~$1.61 |
| `ewc-usgub-nv-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (52,944 resting) | ~6.4% | ~$1.60 |
| `ewc-usse-ia-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (159,032 resting) | ~5.8% | ~$1.46 |
| `ewc-usgub-mi-2026-11-03-rep` | $100.00 ÷ 3 | 0.50 | 2,000 | BUY side (67,951 resting) | ~8.6% | ~$1.43 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $679.56 |
| Skipped | $1.21 |
| **Total earned** | **$836.61** |

351 reward rows · 22 days with rewards · 126 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-24 ⚠️ multi-day pending bucket | $135.19 | `████████████` |
| 2026-07-23 | $227.63 | `████████████████████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $836.61 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $57.16 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $43.94 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $37.11 |
| `apdc-jerpowgov-2026-12-31` | $37.00 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $33.15 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.61 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $26.86 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $21.69 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $21.65 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $21.29 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $21.19 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $20.20 |
| `vmc-ussep-misen-2026-08-04-ste05-10` | $19.47 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-26 5:27 AM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 3:07 AM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 12:00 AM ET | ✅ ok | 351 | $836.61 |
| 2026-07-25 10:06 PM ET | ✅ ok | 351 | $836.61 |
| 2026-07-25 9:09 PM ET | ✅ ok | 351 | $836.61 |
| 2026-07-25 9:05 PM ET | ✅ ok | 288 | $708.72 |
| 2026-07-25 8:16 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 7:34 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 7:28 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 7:16 PM ET | ✅ ok | 282 | $701.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
