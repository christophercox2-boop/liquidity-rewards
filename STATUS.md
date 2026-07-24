# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-23 11:48 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$156.42/day estimated (ceiling, not promise — details below)

**Earned:** $606.98 lifetime ($155.84 paid). Last three recorded days — 2026-07-23: **$133.19** · 2026-07-22: **$82.95** · 2026-07-21: **$91.44** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-sd-2026-06-02-rep-tobdoe` — SELL at the best price, ~$4.96/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$3.72/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$3.41/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$156.42/day (~$6.52/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~87.9% of bid side (2,275 resting ≥ 2,000 ✓) ≈ $5.49/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~86.8% of bid side (2,303 resting ≥ 2,000 ✓) ≈ $6.51/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 5,000 | 1 | $150.00 | ✅ scoring — ~72.2% of bid side (6,075 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 49.0¢ | 100 | 1 | $150.00 | ✅ scoring — ~66.7% of bid side (2,750 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 38.0¢ | 50 | 0 | $150.00 | ✅ scoring — ~66.7% of bid side (2,538 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 75.0¢ | 10 | 0 | $150.00 | ✅ scoring — ~66.4% of ask side (2,899 resting ≥ 2,000 ✓) ≈ $4.15/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 10.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~66.3% of ask side (12,228 resting ≥ 2,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 1.0¢ | 5,000 | 1 | $150.00 | ✅ scoring — ~57.2% of bid side (6,986 resting ≥ 2,000 ✓) ≈ $3.30/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 1 | $150.00 | ✅ scoring — ~54.7% of bid side (7,179 resting ≥ 2,000 ✓) ≈ $3.16/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 1.0¢ | 5,000 | 1 | $150.00 | ✅ scoring — ~54.7% of bid side (7,179 resting ≥ 2,000 ✓) ≈ $3.16/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 1.0¢ | 10,000 | 2 | $150.00 | ✅ scoring — ~53.4% of bid side (15,530 resting ≥ 2,000 ✓) ≈ $3.34/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 10.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~51.7% of ask side (12,304 resting ≥ 2,000 ✓) ≈ $2.99/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 10.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~51.5% of ask side (12,305 resting ≥ 2,000 ✓) ≈ $2.97/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-alawil` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~49.4% of bid side (4,047 resting ≥ 2,000 ✓) ≈ $3.09/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 6.0¢ | 500 | 3 | $150.00 | ✅ scoring — ~48.7% of bid side (3,238 resting ≥ 2,000 ✓) ≈ $3.04/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~48.0% of bid side (4,166 resting ≥ 2,000 ✓) ≈ $3.00/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-pameve` | BUY | 2.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~46.6% of bid side (4,315 resting ≥ 2,000 ✓) ≈ $2.91/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~42.0% of bid side (4,764 resting ≥ 2,000 ✓) ≈ $2.62/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~41.7% of bid side (4,794 resting ≥ 2,000 ✓) ≈ $2.61/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | BUY | 1.0¢ | 2,000 | 1 | $150.00 | ✅ scoring — ~39.6% of bid side (3,888 resting ≥ 2,000 ✓) ≈ $2.97/day (pool ÷ 10 markets) |
| `stsc-bab-el-mandeb-clsd-2026-12-31` | BUY | 40.0¢ | 40 | 1 | $250.00 | ✅ scoring — ~39.5% of bid side (3,366 resting ≥ 2,000 ✓) ≈ $16.46/day (pool ÷ 3 markets) |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~39.3% of bid side (5,083 resting ≥ 2,000 ✓) ≈ $2.46/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 1.0¢ | 2,000 | 4 | $150.00 | ✅ scoring — ~38.1% of bid side (5,103 resting ≥ 2,000 ✓) ≈ $2.86/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-tregow` | SELL | 2.0¢ | 600 | 0 | $150.00 | ✅ scoring — ~34.0% of ask side (3,437 resting ≥ 2,000 ✓) ≈ $2.12/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 2.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~33.9% of bid side (6,131 resting ≥ 2,000 ✓) ≈ $1.95/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 1.0¢ | 2,000 | 1 | $150.00 | ✅ scoring — ~32.6% of bid side (4,179 resting ≥ 2,000 ✓) ≈ $1.88/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 60.0¢ | 100 | 1 | $150.00 | ✅ scoring — ~27.9% of bid side (2,709 resting ≥ 2,000 ✓) ≈ $1.74/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 60.0¢ | 100 | 1 | $150.00 | ✅ scoring — ~27.5% of bid side (2,813 resting ≥ 2,000 ✓) ≈ $1.72/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 5.0¢ | 400 | 0 | $150.00 | ✅ scoring — ~26.0% of ask side (3,004 resting ≥ 2,000 ✓) ≈ $1.63/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~22.9% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $1.43/day (pool ÷ 12 markets) |
| …and 146 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-sc-2026-08-11-rep-wiltim</code> BUY 2,000 @ 1¢ → $5.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,275 (2,000 yours) | ×0.5^0 = 2,275.0 |
| | | **Σ** | **2,275.0** |

`yours 2,000.0 / Σ 2,275.0 = 87.9%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 87.9% = $5.49/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> BUY 2,000 @ 1¢ → $6.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,303 (2,000 yours) | ×0.5^0 = 2,303.0 |
| | | **Σ** | **2,303.0** |

`yours 2,000.0 / Σ 2,303.0 = 86.8%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 86.8% = $6.51/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 5,000 @ 1¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 850 | ×0.5^0 = 850.0 |
| ▶ | 1¢ | 5,225 (5,000 yours) | ×0.5^1 = 2,612.5 |
| | | **Σ** | **3,462.5** |

`yours 2,500.0 / Σ 3,462.5 = 72.2%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 72.2% = $4.17/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 100 @ 49¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 50¢ | 25 | ×0.5^0 = 25.0 |
| ▶ | 49¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 1¢ | 2,625 | ×0.5^49 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190` ← this one
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 50 @ 38¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 75 (50 yours) | ×0.5^0 = 75.0 |
|  | 1¢ | 2,463 | ×0.5^37 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210` ← this one
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 10 @ 75¢ → $4.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 15 (10 yours) | ×0.5^0 = 15.0 |
|  | 89¢ | 996 | ×0.5^14 = 0.1 |
|  | 99¢ | 1,888 | ×0.5^24 = 0.0 |
| | | **Σ** | **15.1** |

`yours 10.0 / Σ 15.1 = 66.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 66.4% = $4.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 100 @ 10¢ → $3.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 150 (100 yours) | ×0.5^0 = 150.0 |
|  | 19¢ | 477 | ×0.5^9 = 0.9 |
|  | 45¢ | 500 | ×0.5^35 = 0.0 |
|  | 50¢ | 100 | ×0.5^40 = 0.0 |
|  | 98¢ | 1,000 | ×0.5^88 = 0.0 |
| | | **Σ** | **150.9** |

`yours 100.0 / Σ 150.9 = 66.3%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 66.3% = $3.82/day`  

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
10. `scc-senate-gop-2026-11-03-55` ← this one
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 5,000 @ 1¢ → $3.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1,761 | ×0.5^0 = 1,761.0 |
| ▶ | 1¢ | 5,225 (5,000 yours) | ×0.5^1 = 2,612.5 |
| | | **Σ** | **4,373.5** |

`yours 2,500.0 / Σ 4,373.5 = 57.2%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 57.2% = $3.30/day`  

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
10. `scc-senate-gop-2026-11-03-55` ← this one
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $3.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1,954 | ×0.5^0 = 1,954.0 |
| ▶ | 1¢ | 5,225 (5,000 yours) | ×0.5^1 = 2,612.5 |
| | | **Σ** | **4,566.5** |

`yours 2,500.0 / Σ 4,566.5 = 54.7%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 54.7% = $3.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 5,000 @ 1¢ → $3.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1,954 | ×0.5^0 = 1,954.0 |
| ▶ | 1¢ | 5,225 (5,000 yours) | ×0.5^1 = 2,612.5 |
| | | **Σ** | **4,566.5** |

`yours 2,500.0 / Σ 4,566.5 = 54.7%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 54.7% = $3.16/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47` ← this one
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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> BUY 10,000 @ 1¢ → $3.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1,060 | ×0.5^0 = 1,060.0 |
| ▶ | 1¢ | 14,470 (10,000 yours) | ×0.5^2 = 3,617.5 |
| | | **Σ** | **4,677.5** |

`yours 2,500.0 / Σ 4,677.5 = 53.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 53.4% = $3.34/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 100 @ 10¢ → $2.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 193 (100 yours) | ×0.5^0 = 193.0 |
|  | 21¢ | 510 | ×0.5^11 = 0.2 |
|  | 45¢ | 500 | ×0.5^35 = 0.0 |
|  | 50¢ | 100 | ×0.5^40 = 0.0 |
|  | 98¢ | 1,000 | ×0.5^88 = 0.0 |
| | | **Σ** | **193.2** |

`yours 100.0 / Σ 193.2 = 51.7%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 51.7% = $2.99/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 100 @ 10¢ → $2.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 194 (100 yours) | ×0.5^0 = 194.0 |
|  | 21¢ | 510 | ×0.5^11 = 0.2 |
|  | 45¢ | 500 | ×0.5^35 = 0.0 |
|  | 50¢ | 100 | ×0.5^40 = 0.0 |
|  | 98¢ | 1,000 | ×0.5^88 = 0.0 |
| | | **Σ** | **194.2** |

`yours 100.0 / Σ 194.2 = 51.5%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 51.5% = $2.97/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-alawil</code> BUY 2,000 @ 1¢ → $3.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,047 (2,000 yours) | ×0.5^0 = 4,047.0 |
| | | **Σ** | **4,047.0** |

`yours 2,000.0 / Σ 4,047.0 = 49.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 49.4% = $3.09/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 500 @ 6¢ → $3.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 25 | ×0.5^0 = 25.0 |
| ▶ | 6¢ | 750 (500 yours) | ×0.5^3 = 93.8 |
|  | 1¢ | 2,463 | ×0.5^8 = 9.6 |
| | | **Σ** | **128.4** |

`yours 62.5 / Σ 128.4 = 48.7%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 48.7% = $3.04/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220` ← this one
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-paudan</code> BUY 2,000 @ 1¢ → $3.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,166 (2,000 yours) | ×0.5^0 = 4,166.0 |
| | | **Σ** | **4,166.0** |

`yours 2,000.0 / Σ 4,166.0 = 48.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 48.0% = $3.00/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-pameve</code> BUY 2,000 @ 2¢ → $2.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 4,290 (2,000 yours) | ×0.5^0 = 4,290.0 |
| | | **Σ** | **4,290.0** |

`yours 2,000.0 / Σ 4,290.0 = 46.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 46.6% = $2.91/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> BUY 2,000 @ 1¢ → $2.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,764 (2,000 yours) | ×0.5^0 = 4,764.0 |
| | | **Σ** | **4,764.0** |

`yours 2,000.0 / Σ 4,764.0 = 42.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 42.0% = $2.62/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> BUY 2,000 @ 1¢ → $2.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,794 (2,000 yours) | ×0.5^0 = 4,794.0 |
| | | **Σ** | **4,794.0** |

`yours 2,000.0 / Σ 4,794.0 = 41.7%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 41.7% = $2.61/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
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
12. `scc-hrep-rep-2026-11-03-gte235` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> BUY 2,000 @ 1¢ → $2.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1,168 | ×0.5^0 = 1,168.0 |
| ▶ | 1¢ | 2,720 (2,000 yours) | ×0.5^1 = 1,360.0 |
| | | **Σ** | **2,528.0** |

`yours 1,000.0 / Σ 2,528.0 = 39.6%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 39.6% = $2.97/day`  

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
<details><summary><code>stsc-bab-el-mandeb-clsd-2026-12-31</code> BUY 40 @ 40¢ → $16.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 41¢ | 18 | ×0.5^0 = 18.0 |
| ▶ | 40¢ | 65 (40 yours) | ×0.5^1 = 32.6 |
|  | 18¢ | 3,000 | ×0.5^23 = 0.0 |
| | | **Σ** | **50.6** |

`yours 20.0 / Σ 50.6 = 39.5%`  
`$250 ÷ 3 ÷ 2 = $41.67 × 39.5% = $16.46/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `stsc-bab-el-mandeb-clsd-2026-07-31`
2. `stsc-bab-el-mandeb-clsd-2026-08-31`
3. `stsc-bab-el-mandeb-clsd-2026-12-31` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-andbau</code> BUY 2,000 @ 1¢ → $2.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,083 (2,000 yours) | ×0.5^0 = 5,083.0 |
| | | **Σ** | **5,083.0** |

`yours 2,000.0 / Σ 5,083.0 = 39.3%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 39.3% = $2.46/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 2,000 @ 1¢ → $2.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 5 | ×0.5^0 = 5.0 |
|  | 2¢ | 73 | ×0.5^3 = 9.1 |
| ▶ | 1¢ | 5,025 (2,000 yours) | ×0.5^4 = 314.1 |
| | | **Σ** | **328.2** |

`yours 125.0 / Σ 328.2 = 38.1%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 38.1% = $2.86/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-tregow</code> SELL 600 @ 2¢ → $2.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 1,753 (600 yours) | ×0.5^0 = 1,752.5 |
|  | 7¢ | 408 | ×0.5^5 = 12.8 |
| | | **Σ** | **1,765.3** |

`yours 600.0 / Σ 1,765.3 = 34.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 34.0% = $2.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 2,000 @ 2¢ → $1.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 5,906 (2,000 yours) | ×0.5^0 = 5,906.0 |
| | | **Σ** | **5,906.0** |

`yours 2,000.0 / Σ 5,906.0 = 33.9%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 33.9% = $1.95/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53` ← this one
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 2,000 @ 1¢ → $1.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1,954 | ×0.5^0 = 1,954.0 |
| ▶ | 1¢ | 2,225 (2,000 yours) | ×0.5^1 = 1,112.5 |
| | | **Σ** | **3,066.5** |

`yours 1,000.0 / Σ 3,066.5 = 32.6%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 32.6% = $1.88/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 100 @ 60¢ → $1.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 61¢ | 25 | ×0.5^0 = 25.0 |
| ▶ | 60¢ | 309 (100 yours) | ×0.5^1 = 154.5 |
|  | 1¢ | 2,375 | ×0.5^60 = 0.0 |
| | | **Σ** | **179.5** |

`yours 50.0 / Σ 179.5 = 27.9%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 27.9% = $1.74/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 100 @ 60¢ → $1.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 61¢ | 25 | ×0.5^0 = 25.0 |
| ▶ | 60¢ | 313 (100 yours) | ×0.5^1 = 156.5 |
|  | 1¢ | 2,475 | ×0.5^60 = 0.0 |
| | | **Σ** | **181.5** |

`yours 50.0 / Σ 181.5 = 27.5%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 27.5% = $1.72/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185` ← this one
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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 400 @ 5¢ → $1.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1,343 (400 yours) | ×0.5^0 = 1,343.0 |
|  | 6¢ | 386 | ×0.5^1 = 193.0 |
|  | 22¢ | 250 | ×0.5^17 = 0.0 |
|  | 50¢ | 25 | ×0.5^45 = 0.0 |
| | | **Σ** | **1,536.0** |

`yours 400.0 / Σ 1,536.0 = 26.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 26.0% = $1.63/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 100 @ 49¢ → $1.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 436 (100 yours) | ×0.5^0 = 436.0 |
|  | 1¢ | 2,064 | ×0.5^48 = 0.0 |
| | | **Σ** | **436.0** |

`yours 100.0 / Σ 436.0 = 22.9%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 22.9% = $1.43/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195` ← this one
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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-23 | ~$136.30 | $133.19 | 98% |
| 2026-07-22 | ~$110.63 | $82.95 | 75% |
| 2026-07-21 | ~$87.94 | $91.44 | 104% |

Biggest gaps on 2026-07-23: `scc-hrep-rep-2026-11-03-gte210` (est ~$2.21 → got $0.00), `scc-senate-gop-2026-11-03-55` (est ~$2.14 → got $0.00), `opdc-trump-resig-2027-12-31` (est ~$2.12 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (30,707 resting) | ~13.2% | ~$4.96 |
| `ewc-usgub-ga-2026-11-03-dem` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (82,723 resting) | ~9.9% | ~$3.72 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (62,618 resting) | ~9.1% | ~$3.41 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $150.00 ÷ 3 | 0.50 | 2,000 | BUY side (12,630 resting) | ~12.7% | ~$3.18 |
| `ewc-usgub-ia-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (180,611 resting) | ~7.7% | ~$2.87 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (79,039 resting) | ~6.9% | ~$2.60 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $150.00 ÷ 3 | 0.50 | 2,000 | SELL side (20,794 resting) | ~9.8% | ~$2.44 |
| `ewc-usgub-ks-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (258,878 resting) | ~6.3% | ~$2.35 |
| `ewc-usgub-ga-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (86,183 resting) | ~6.0% | ~$2.26 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (39,623 resting) | ~5.3% | ~$1.98 |
| `ewc-usgub-ks-2026-11-03-dem` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (193,793 resting) | ~4.9% | ~$1.85 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (75,047 resting) | ~4.7% | ~$1.78 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $449.93 |
| Skipped | $1.21 |
| **Total earned** | **$606.98** |

257 reward rows · 21 days with rewards · 79 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-23 | $133.19 | `████████████████████` |
| 2026-07-22 | $82.95 | `████████████` |
| 2026-07-21 | $91.44 | `██████████████` |
| 2026-07-20 | $106.54 | `████████████████` |
| 2026-07-19 | $35.81 | `█████` |
| 2026-07-18 | $44.41 | `███████` |
| 2026-07-17 | $14.71 | `██` |
| 2026-07-16 | $17.02 | `███` |
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `██` |
| 2026-07-13 | $10.03 | `██` |
| 2026-07-12 | $39.90 | `██████` |
| 2026-07-11 | $2.11 | `█` |
| 2026-07-10 | $2.16 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $606.98 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $56.41 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $43.94 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $36.49 |
| `apdc-jerpowgov-2026-12-31` | $26.93 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $26.68 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $23.68 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $21.84 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $21.56 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $19.23 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $18.02 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $17.30 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $16.88 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.58 |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | $14.80 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-23 11:48 PM ET | ✅ ok | 257 | $606.98 |
| 2026-07-23 9:18 PM ET | ✅ ok | 257 | $606.98 |
| 2026-07-23 9:06 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 9:02 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:55 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:53 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:49 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:13 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:11 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 7:14 PM ET | ✅ ok | 211 | $390.84 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
