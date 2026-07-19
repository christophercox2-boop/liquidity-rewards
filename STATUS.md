# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 1:53 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$6.72/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mi-2026-08-04-dem-abdels` — BUY at the best price, ~$8.98/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$8.56/day), `enwc-ussep-mn-2026-08-11-dem-angcra` (~$5.25/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$6.72/day (~$0.28/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `cranc-uspres28-12-31-2026-jdvan` | SELL | 15.0¢ | 13 | 1 | $250.00 | ✅ scoring — ~30.1% of ask side (26,139 resting ≥ 10,000 ✓) ≈ $1.14/day (pool ÷ 33 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 6.0¢ | 98 | 0 | $250.00 | ✅ scoring — ~22.6% of ask side (11,277 resting ≥ 10,000 ✓) ≈ $4.72/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 51.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~3.5% of ask side (11,975 resting ≥ 10,000 ✓) ≈ $0.43/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 51.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~3.5% of ask side (11,975 resting ≥ 10,000 ✓) ≈ $0.43/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 25.0¢ | 100 | 3 | $250.00 | ❌ outside Target Size window (order 3 ticks from best; window ends 2) |

**Tap an order for its book window and the math:**

<details><summary><code>cranc-uspres28-12-31-2026-jdvan</code> SELL 13 @ 15¢ → $1.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 9 | ×0.3^0 = 9.0 |
| ▶ | 15¢ | 13 (13 yours) | ×0.3^1 = 3.9 |
|  | 19¢ | 48 | ×0.3^5 = 0.1 |
|  | 21¢ | 125 | ×0.3^7 = 0.0 |
|  | 50¢ | 90 | ×0.3^36 = 0.0 |
|  | 55¢ | 116 | ×0.3^41 = 0.0 |
|  | 58¢ | 739 | ×0.3^44 = 0.0 |
|  | 99¢ | 24,999 | ×0.3^85 = 0.0 |
| | | **Σ** | **13.1** |

`yours 3.9 / Σ 13.1 = 30.1%`  
`$250 ÷ 33 ÷ 2 = $3.79 × 30.1% = $1.14/day`  

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> SELL 98 @ 6¢ → $4.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 429 (98 yours) | ×0.3^0 = 429.0 |
|  | 7¢ | 13 | ×0.3^1 = 3.9 |
|  | 30¢ | 250 | ×0.3^24 = 0.0 |
|  | 99¢ | 10,585 | ×0.3^93 = 0.0 |
| | | **Σ** | **432.9** |

`yours 98.0 / Σ 432.9 = 22.6%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 22.6% = $4.72/day`  

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 100 @ 51¢ → $0.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 50¢ | 661 | ×0.3^0 = 661.0 |
| ▶ | 51¢ | 692 (100 yours) | ×0.3^1 = 207.6 |
|  | 99¢ | 10,622 | ×0.3^49 = 0.0 |
| | | **Σ** | **868.6** |

`yours 30.0 / Σ 868.6 = 3.5%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 3.5% = $0.43/day`  

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 100 @ 51¢ → $0.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 50¢ | 661 | ×0.3^0 = 661.0 |
| ▶ | 51¢ | 692 (100 yours) | ×0.3^1 = 207.6 |
|  | 99¢ | 10,622 | ×0.3^49 = 0.0 |
| | | **Σ** | **868.6** |

`yours 30.0 / Σ 868.6 = 3.5%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 3.5% = $0.43/day`  

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 100 @ 25¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 22¢ | 477 | ×0.3^0 = 477.0 |
|  | 24¢ | 29,857 | ×0.3^2 = 2,687.1 |
| | | **Σ** | **3,164.1** |

`you 3t from best, window ends 2t → score 0`  

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (23,438 resting) | ~21.5% | ~$8.98 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (27,472 resting) | ~13.7% | ~$8.56 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (61,033 resting) | ~8.4% | ~$5.25 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (38,564 resting) | ~9.6% | ~$3.98 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (58,076 resting) | ~5.1% | ~$3.21 |
| `cranc-uspres28-12-31-2026-jonoss` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,322 resting) | ~74.9% | ~$2.84 |
| `cranc-uspres28-12-31-2026-markel` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,687 resting) | ~69.4% | ~$2.63 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (68,438 resting) | ~3.7% | ~$2.32 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (98,956 resting) | ~2.2% | ~$1.36 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (28,747 resting) | ~1.8% | ~$1.14 |
| `cranc-uspres28-12-31-2026-gavnew` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (25,673 resting) | ~23.9% | ~$0.90 |
| `cranc-uspres28-12-31-2026-bersan` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (10,999 resting) | ~16.7% | ~$0.63 |

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
| 2026-07-19 1:53 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:27 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 12:14 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 11:18 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:50 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:43 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:09 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:56 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:47 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:34 AM ET | ✅ ok | 102 | $112.64 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
