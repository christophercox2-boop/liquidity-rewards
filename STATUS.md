# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-18 13:29 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📍 Right now — your resting orders

### Estimated earning rate: ~$440.45/day (~$18.35/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, and each pool splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 6.0¢ | 191 | 0 | $250.00 | ✅ scoring — ~54.3% of ask side (50,603 resting ≥ 10,000 ✓) ≈ $67.83/day |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 51.0¢ | 355 | 0 | $250.00 | ✅ scoring — ~49.1% of ask side (11,393 resting ≥ 10,000 ✓) ≈ $61.38/day |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 51.0¢ | 355 | 0 | $250.00 | ✅ scoring — ~49.1% of ask side (11,000 resting ≥ 10,000 ✓) ≈ $61.38/day |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 51.0¢ | 355 | 0 | $250.00 | ✅ scoring — ~49.1% of ask side (50,999 resting ≥ 10,000 ✓) ≈ $61.38/day |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 51.0¢ | 355 | 0 | $250.00 | ✅ scoring — ~49.1% of ask side (11,000 resting ≥ 10,000 ✓) ≈ $61.38/day |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~39.6% of bid side (25,275 resting ≥ 10,000 ✓) ≈ $49.46/day |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 13.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~22.8% of bid side (11,390 resting ≥ 10,000 ✓) ≈ $28.49/day |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~15.7% of bid side (63,834 resting ≥ 10,000 ✓) ≈ $19.58/day |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 10.0¢ | 199 | 0 | $250.00 | ✅ scoring — ~12.3% of ask side (92,765 resting ≥ 10,000 ✓) ≈ $15.38/day |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 90.0¢ | 199 | 0 | $250.00 | ✅ scoring — ~3.6% of bid side (44,147 resting ≥ 10,000 ✓) ≈ $4.46/day |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 11.0¢ | 201 | 0 | $250.00 | ✅ scoring — ~3.5% of ask side (96,934 resting ≥ 10,000 ✓) ≈ $4.37/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 90.0¢ | 199 | 0 | $250.00 | ✅ scoring — ~3.4% of bid side (26,114 resting ≥ 10,000 ✓) ≈ $4.20/day |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 3.0¢ | 29 | 0 | $250.00 | ✅ scoring — ~0.9% of ask side (80,883 resting ≥ 10,000 ✓) ≈ $1.16/day |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `vmc-ussep-misen-2026-08-04-els10-15` | $250.00 | 0.30 | 10,000 | SELL side (17,600 resting) | ~88.9% | ~$111.11 |
| `vmc-ussep-misen-2026-08-04-ste0-5` | $250.00 | 0.30 | 10,000 | BUY side (11,150 resting) | ~77.7% | ~$97.09 |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | $250.00 | 0.30 | 10,000 | BUY side (13,750 resting) | ~67.3% | ~$84.18 |
| `vmc-ussep-misen-2026-08-04-els5-10` | $250.00 | 0.30 | 10,000 | SELL side (11,050 resting) | ~61.5% | ~$76.92 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $250.00 | 0.30 | 10,000 | SELL side (10,888 resting) | ~61.5% | ~$76.92 |
| `vmc-ussep-misen-2026-08-04-ste05-10` | $250.00 | 0.30 | 10,000 | SELL side (11,054 resting) | ~60.8% | ~$75.99 |
| `paccc-usho-midterms-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | SELL side (621,246 resting) | ~55.1% | ~$68.84 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $250.00 | 0.30 | 10,000 | SELL side (11,000 resting) | ~29.5% | ~$36.87 |
| `paccc-usse-midterms-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | BUY side (497,334 resting) | ~28.2% | ~$35.25 |
| `enwc-usgubp-mn-2026-08-11-rep-kenqua` | $250.00 | 0.30 | 10,000 | SELL side (95,623 resting) | ~21.4% | ~$26.70 |
| `paccc-usse-midterms-2026-11-03-rep` | $250.00 | 0.30 | 10,000 | BUY side (524,094 resting) | ~15.5% | ~$19.33 |
| `enwc-usgubp-mn-2026-08-11-rep-lisdem` | $250.00 | 0.30 | 10,000 | BUY side (46,511 resting) | ~12.6% | ~$15.78 |

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
| 2026-07-18 13:29:37 | ✅ ok | 83 | $97.93 |
| 2026-07-18 12:19:42 | ✅ ok | 83 | $97.93 |
| 2026-07-18 11:26:27 | ✅ ok | 83 | $97.93 |
| 2026-07-18 09:49:19 | ✅ ok | 83 | $97.93 |
| 2026-07-18 08:13:34 | ✅ ok | 83 | $97.93 |
| 2026-07-18 06:22:35 | ✅ ok | 83 | $97.93 |
| 2026-07-18 04:07:22 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:40:46 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:37:44 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:32:09 | ✅ ok | 83 | $97.93 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
