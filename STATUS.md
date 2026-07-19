# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 11:18 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$7.62/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — BUY at the best price, ~$12.05/day for 200 contracts. Runners-up: `enwc-usgubp-sd-2026-06-02-rep-tobdoe` (~$11.43/day), `enwc-ussep-mi-2026-08-04-dem-abdels` (~$11.21/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$7.62/day (~$0.32/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 6.0¢ | 98 | 0 | $250.00 | ✅ scoring — ~22.8% of ask side (11,048 resting ≥ 10,000 ✓) ≈ $5.70/day (pool ÷ 5 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | SELL | 15.0¢ | 13 | 1 | $250.00 | ✅ scoring — ~20.6% of ask side (25,406 resting ≥ 10,000 ✓) ≈ $0.78/day (pool ÷ 33 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 51.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~3.8% of ask side (11,691 resting ≥ 10,000 ✓) ≈ $0.48/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 51.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~3.8% of ask side (11,706 resting ≥ 10,000 ✓) ≈ $0.48/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 25.0¢ | 100 | 5 | $250.00 | ✅ scoring — ~0.3% of ask side (23,580 resting ≥ 10,000 ✓) ≈ $0.17/day (pool ÷ 2 markets) |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> SELL 98 @ 6¢ → $5.70/day</summary>

| | Asks | Resting |
|---|---:|---:|
| ▶ | 6¢ | 426 (98 yours) |
|  | 7¢ | 12 |
|  | 14¢ | 25 |
|  | 99¢ | 10,585 |

`0.3^0 × 98 = 98.0`  
`98.0 / 429.6 = 22.8%`  
`$250 ÷ 5 ÷ 2 = $25.00 × 22.8% = $5.70/day`  

</details>
<details><summary><code>cranc-uspres28-12-31-2026-jdvan</code> SELL 13 @ 15¢ → $0.78/day</summary>

| | Asks | Resting |
|---|---:|---:|
|  | 14¢ | 15 |
| ▶ | 15¢ | 13 (13 yours) |
|  | 19¢ | 48 |
|  | 21¢ | 125 |
|  | 50¢ | 90 |
|  | 56¢ | 116 |
|  | 99¢ | 24,999 |

`0.3^1 × 13 = 3.9`  
`3.9 / 19.1 = 20.6%`  
`$250 ÷ 33 ÷ 2 = $3.79 × 20.6% = $0.78/day`  

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 100 @ 51¢ → $0.48/day</summary>

| | Asks | Resting |
|---|---:|---:|
|  | 50¢ | 659 |
| ▶ | 51¢ | 410 (100 yours) |
|  | 99¢ | 10,622 |

`0.3^1 × 100 = 30.0`  
`30.0 / 782.0 = 3.8%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 3.8% = $0.48/day`  

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 100 @ 51¢ → $0.48/day</summary>

| | Asks | Resting |
|---|---:|---:|
|  | 50¢ | 659 |
| ▶ | 51¢ | 425 (100 yours) |
|  | 99¢ | 10,622 |

`0.3^1 × 100 = 30.0`  
`30.0 / 786.5 = 3.8%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 3.8% = $0.48/day`  

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 100 @ 25¢ → $0.17/day</summary>

| | Asks | Resting |
|---|---:|---:|
|  | 20¢ | 50 |
|  | 22¢ | 407 |
| ▶ | 25¢ | 122 (100 yours) |
|  | 93¢ | 23,000 |

`0.3^5 × 100 = 0.2`  
`0.2 / 86.9 = 0.3%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.3% = $0.17/day`  

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (35,337 resting) | ~19.3% | ~$12.05 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (26,950 resting) | ~18.3% | ~$11.43 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (20,733 resting) | ~26.9% | ~$11.21 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (27,485 resting) | ~13.5% | ~$8.46 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (28,526 resting) | ~8.1% | ~$5.04 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (23,076 resting) | ~5.9% | ~$3.67 |
| `cranc-uspres28-12-31-2026-kamhar` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,021 resting) | ~91.7% | ~$3.47 |
| `cranc-uspres28-12-31-2026-krinoe` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (21,632 resting) | ~79.4% | ~$3.01 |
| `cranc-uspres28-12-31-2026-andyan` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (21,276 resting) | ~77.5% | ~$2.94 |
| `cranc-uspres28-12-31-2026-hunbid` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,040 resting) | ~75.5% | ~$2.86 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (75,006 resting) | ~6.2% | ~$2.57 |
| `cranc-uspres28-12-31-2026-gavnew` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (29,356 resting) | ~51.7% | ~$1.96 |

## Totals

| | Amount |
|---|---:|
| Paid | $78.17 |
| Pending | $33.26 |
| Skipped | $1.21 |
| **Total earned** | **$112.64** |

102 reward rows · 15 days with rewards · 44 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-17 | $14.71 | `███████` |
| 2026-07-16 | $17.02 | `█████████` |
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `███████` |
| 2026-07-13 | $10.03 | `█████` |
| 2026-07-12 | $39.90 | `████████████████████` |
| 2026-07-11 | $2.11 | `█` |
| 2026-07-10 | $2.16 | `█` |
| 2026-07-09 | $4.72 | `██` |
| 2026-07-08 | $2.68 | `█` |
| 2026-07-07 | $0.14 | `█` |
| 2026-07-06 | $0.58 | `█` |
| 2026-07-05 | $0.47 | `█` |
| 2026-07-02 | $0.02 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $112.64 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.20 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.56 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $5.31 |
| `paccc-usse-midterms-2026-11-03-rep` | $5.29 |
| `apdc-jerpowgov-2026-12-31` | $5.25 |
| `enwc-ussep-me-2026-07-27-dem-jargol` | $4.80 |
| `ewc-usgub-ca-2026-11-03-stehil` | $4.49 |
| `paccc-usho-midterms-2026-11-03-dem` | $4.07 |
| `pic-congress-trump-2026-12-31` | $3.77 |
| `apdc-alito-2026-12-31` | $3.07 |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | $3.03 |
| `enwc-ussep-me-2026-07-27-dem-trojac` | $2.28 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $2.16 |
| `enwc-ussep-me-2026-07-27-dem-shebel` | $1.20 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $1.18 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-19 11:18 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:50 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:43 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:09 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:56 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:47 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:34 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:10 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 8:08 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 6:46 AM ET | ✅ ok | 102 | $112.64 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
