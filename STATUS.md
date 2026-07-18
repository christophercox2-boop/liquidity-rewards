# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-18 04:07 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📍 Right now — your resting orders

### Estimated earning rate: ~$134.38/day (~$5.60/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, and each pool splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 25.0¢ | 10 | 0 | $250.00 | ✅ scoring — ~29.4% of ask side (60,780 resting ≥ 10,000 ✓) ≈ $36.76/day |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 25.0¢ | 10 | 0 | $250.00 | ✅ scoring — ~29.4% of ask side (60,780 resting ≥ 10,000 ✓) ≈ $36.76/day |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 90.0¢ | 129 | 0 | $250.00 | ✅ scoring — ~8.2% of bid side (41,050 resting ≥ 10,000 ✓) ≈ $10.27/day |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 11.0¢ | 130 | 0 | $250.00 | ✅ scoring — ~8.1% of ask side (93,570 resting ≥ 10,000 ✓) ≈ $10.15/day |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 10.0¢ | 129 | 0 | $250.00 | ✅ scoring — ~8.1% of ask side (94,533 resting ≥ 10,000 ✓) ≈ $10.12/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 90.0¢ | 129 | 0 | $250.00 | ✅ scoring — ~5.2% of bid side (55,718 resting ≥ 10,000 ✓) ≈ $6.44/day |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 34.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~4.9% of bid side (10,423 resting ≥ 10,000 ✓) ≈ $6.11/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | SELL | 91.0¢ | 70 | 0 | $250.00 | ✅ scoring — ~4.8% of ask side (11,470 resting ≥ 10,000 ✓) ≈ $5.97/day |
| `ewc-usgub-ca-2026-11-03-xavbec` | BUY | 93.0¢ | 125 | 0 | $250.00 | ✅ scoring — ~3.0% of bid side (89,454 resting ≥ 10,000 ✓) ≈ $3.78/day |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | SELL | 30.0¢ | 50 | 1 | $250.00 | ✅ scoring — ~2.8% of ask side (51,132 resting ≥ 10,000 ✓) ≈ $3.48/day |
| `ewc-usgub-ca-2026-11-03-stehil` | SELL | 7.0¢ | 125 | 1 | $250.00 | ✅ scoring — ~2.2% of ask side (185,036 resting ≥ 10,000 ✓) ≈ $2.70/day |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 3.0¢ | 29 | 0 | $250.00 | ✅ scoring — ~0.9% of ask side (81,556 resting ≥ 10,000 ✓) ≈ $1.09/day |
| `apdc-jerpowgov-2026-12-31` | BUY | 2.0¢ | 2,500 | 5 | $250.00 | ✅ scoring — ~0.6% of bid side (16,050 resting ≥ 10,000 ✓) ≈ $0.72/day |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | SELL | 45.0¢ | 50 | 4 | $250.00 | ✅ scoring — ~0.0% of ask side (52,566 resting ≥ 10,000 ✓) ≈ $0.02/day |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 99.0¢ | 10,000 | 74 | $250.00 | ✅ scoring — ~0.0% of ask side (60,780 resting ≥ 10,000 ✓) ≈ $0.00/day |
| `pvwc-housepopw-2026-11-03-dem` | BUY | 85.0¢ | 136 | 0 | — | ❌ no active reward program on this market |
| `pvwc-housepopw-2026-11-03-rep` | SELL | 23.0¢ | 149 | 1 | — | ❌ no active reward program on this market |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $250.00 | 0.30 | 10,000 | SELL side (11,127 resting) | ~97.1% | ~$121.36 |
| `vmc-ussep-misen-2026-08-04-ste0-5` | $250.00 | 0.30 | 10,000 | BUY side (11,140 resting) | ~75.4% | ~$94.26 |
| `paccc-usho-midterms-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | SELL side (626,858 resting) | ~25.3% | ~$31.64 |
| `vmc-ussep-misen-2026-08-04-els15-20` | $250.00 | 0.30 | 10,000 | SELL side (50,653 resting) | ~23.5% | ~$29.34 |
| `vmc-ussep-misen-2026-08-04-els5-10` | $250.00 | 0.30 | 10,000 | SELL side (50,659 resting) | ~23.3% | ~$29.14 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $250.00 | 0.30 | 10,000 | SELL side (50,659 resting) | ~23.3% | ~$29.14 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $250.00 | 0.30 | 10,000 | SELL side (50,659 resting) | ~23.3% | ~$29.14 |
| `vmc-ussep-misen-2026-08-04-ste05-10` | $250.00 | 0.30 | 10,000 | SELL side (50,660 resting) | ~23.3% | ~$29.10 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $250.00 | 0.30 | 10,000 | SELL side (50,661 resting) | ~23.3% | ~$29.07 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $250.00 | 0.30 | 10,000 | SELL side (50,661 resting) | ~23.3% | ~$29.07 |
| `paccc-usse-midterms-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | BUY side (402,665 resting) | ~12.3% | ~$15.43 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $250.00 | 0.30 | 10,000 | SELL side (51,649 resting) | ~10.8% | ~$13.53 |

## Totals

| | Amount |
|---|---:|
| Paid | $78.17 |
| Pending | $18.55 |
| Skipped | $1.21 |
| **Total earned** | **$97.93** |

83 reward rows · 14 days with rewards · 32 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
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
| 2026-07-01 | $3.41 | `██` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $97.93 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.17 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.56 |
| `paccc-usse-midterms-2026-11-03-rep` | $5.29 |
| `enwc-ussep-me-2026-07-27-dem-jargol` | $4.80 |
| `paccc-usho-midterms-2026-11-03-dem` | $4.07 |
| `apdc-jerpowgov-2026-12-31` | $3.75 |
| `pic-congress-trump-2026-12-31` | $3.60 |
| `ewc-usgub-ca-2026-11-03-stehil` | $3.24 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $3.13 |
| `apdc-alito-2026-12-31` | $2.49 |
| `enwc-ussep-me-2026-07-27-dem-trojac` | $2.28 |
| `enwc-ussep-me-2026-07-27-dem-shebel` | $1.20 |
| `paccc-usse-midterms-2026-11-03-dem` | $1.08 |
| `ewc-usse-oh-2026-11-03-rep` | $0.90 |
| `paccc-usho-midterms-2026-11-03-rep` | $0.85 |

## Recent checks

| Checked (UTC) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-18 04:07:22 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:40:46 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:37:44 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:32:09 | ✅ ok | 83 | $97.93 |
| 2026-07-18 00:12:37 | ✅ ok | 72 | $80.91 |
| 2026-07-18 00:01:41 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:49:54 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:34:53 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:11:26 | ✅ ok | 72 | $80.91 |
| 2026-07-17 22:08:52 | ✅ ok | 72 | $80.91 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
