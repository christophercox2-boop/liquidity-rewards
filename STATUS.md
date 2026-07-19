# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 1:27 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$6.49/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$8.14/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-angcra` (~$5.01/day), `enwc-usgubp-sd-2026-06-02-rep-tobdoe` (~$3.07/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$6.49/day (~$0.27/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 6.0¢ | 98 | 0 | $250.00 | ✅ scoring — ~22.5% of ask side (11,055 resting ≥ 10,000 ✓) ≈ $4.69/day (pool ÷ 6 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | SELL | 15.0¢ | 13 | 1 | $250.00 | ✅ scoring — ~20.6% of ask side (26,526 resting ≥ 10,000 ✓) ≈ $0.78/day (pool ÷ 33 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 51.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~4.1% of ask side (11,545 resting ≥ 10,000 ✓) ≈ $0.51/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 51.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~4.1% of ask side (11,545 resting ≥ 10,000 ✓) ≈ $0.51/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 25.0¢ | 100 | 3 | $250.00 | ❌ outside Target Size window (order 3 ticks from best; window ends 2) |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> SELL 98 @ 6¢ → $4.69/day</summary>

| | Asks | Resting |
|---|---:|---:|
| ▶ | 6¢ | 431 (98 yours) |
|  | 7¢ | 14 |
|  | 14¢ | 25 |
|  | 99¢ | 10,585 |

`0.3^0 × 98 = 98.0`  
`98.0 / 435.2 = 22.5%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 22.5% = $4.69/day`  

</details>
<details><summary><code>cranc-uspres28-12-31-2026-jdvan</code> SELL 13 @ 15¢ → $0.78/day</summary>

| | Asks | Resting |
|---|---:|---:|
|  | 14¢ | 15 |
| ▶ | 15¢ | 13 (13 yours) |
|  | 19¢ | 48 |
|  | 21¢ | 125 |
|  | 50¢ | 90 |
|  | 55¢ | 116 |
|  | 58¢ | 620 |
|  | 99¢ | 25,499 |

`0.3^1 × 13 = 3.9`  
`3.9 / 19.1 = 20.6%`  
`$250 ÷ 33 ÷ 2 = $3.79 × 20.6% = $0.78/day`  

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 100 @ 51¢ → $0.51/day</summary>

| | Asks | Resting |
|---|---:|---:|
|  | 50¢ | 660 |
| ▶ | 51¢ | 263 (100 yours) |
|  | 99¢ | 10,622 |

`0.3^1 × 100 = 30.0`  
`30.0 / 738.9 = 4.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 4.1% = $0.51/day`  

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 100 @ 51¢ → $0.51/day</summary>

| | Asks | Resting |
|---|---:|---:|
|  | 50¢ | 660 |
| ▶ | 51¢ | 263 (100 yours) |
|  | 99¢ | 10,622 |

`0.3^1 × 100 = 30.0`  
`30.0 / 738.9 = 4.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 4.1% = $0.51/day`  

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 100 @ 25¢ → $0</summary>

| | Asks | Resting |
|---|---:|---:|
|  | 22¢ | 477 |
|  | 24¢ | 30,754 |

`you 3t from best, window ends 2t → score 0`  

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (27,561 resting) | ~13.0% | ~$8.14 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (36,793 resting) | ~8.0% | ~$5.01 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (60,052 resting) | ~4.9% | ~$3.07 |
| `cranc-uspres28-12-31-2026-jonoss` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,820 resting) | ~75.5% | ~$2.86 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (31,156 resting) | ~4.4% | ~$2.78 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (27,678 resting) | ~6.5% | ~$2.70 |
| `cranc-uspres28-12-31-2026-markel` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (18,186 resting) | ~69.7% | ~$2.64 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (79,204 resting) | ~6.0% | ~$2.51 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (78,214 resting) | ~2.5% | ~$1.56 |
| `cranc-uspres28-12-31-2026-gavnew` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (27,051 resting) | ~23.8% | ~$0.90 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (53,125 resting) | ~1.0% | ~$0.64 |
| `cranc-uspres28-12-31-2026-marrub` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (28,147 resting) | ~16.3% | ~$0.62 |

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
| 2026-07-19 1:27 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 12:14 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 11:18 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:50 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:43 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:09 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:56 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:47 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:34 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:10 AM ET | ✅ ok | 102 | $112.64 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
