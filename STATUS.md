# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-18 06:22 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📍 Right now — your resting orders

### Estimated earning rate: ~$180.15/day (~$7.51/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, and each pool splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 21.0¢ | 10 | 0 | $250.00 | ✅ scoring — ~93.9% of ask side (50,836 resting ≥ 10,000 ✓) ≈ $117.39/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | SELL | 91.0¢ | 70 | 0 | $250.00 | ✅ scoring — ~19.0% of ask side (10,370 resting ≥ 10,000 ✓) ≈ $23.69/day |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 10.0¢ | 129 | 0 | $250.00 | ✅ scoring — ~8.7% of ask side (90,637 resting ≥ 10,000 ✓) ≈ $10.83/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 90.0¢ | 129 | 0 | $250.00 | ✅ scoring — ~8.4% of bid side (11,630 resting ≥ 10,000 ✓) ≈ $10.55/day |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 25.0¢ | 60 | 4 | $250.00 | ✅ scoring — ~4.6% of ask side (50,836 resting ≥ 10,000 ✓) ≈ $5.71/day |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 11.0¢ | 130 | 0 | $250.00 | ✅ scoring — ~2.4% of ask side (94,638 resting ≥ 10,000 ✓) ≈ $2.96/day |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 90.0¢ | 129 | 0 | $250.00 | ✅ scoring — ~2.2% of bid side (47,077 resting ≥ 10,000 ✓) ≈ $2.79/day |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 3.0¢ | 29 | 0 | $250.00 | ✅ scoring — ~0.9% of ask side (80,883 resting ≥ 10,000 ✓) ≈ $1.16/day |
| `ewc-usgub-ca-2026-11-03-xavbec` | BUY | 93.0¢ | 125 | 0 | $250.00 | ✅ scoring — ~0.8% of bid side (95,607 resting ≥ 10,000 ✓) ≈ $1.05/day |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 25.0¢ | 10 | 4 | $250.00 | ✅ scoring — ~0.8% of ask side (50,836 resting ≥ 10,000 ✓) ≈ $0.95/day |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 25.0¢ | 10 | 4 | $250.00 | ✅ scoring — ~0.8% of ask side (50,836 resting ≥ 10,000 ✓) ≈ $0.95/day |
| `ewc-usgub-ca-2026-11-03-stehil` | SELL | 7.0¢ | 125 | 1 | $250.00 | ✅ scoring — ~0.7% of ask side (156,588 resting ≥ 10,000 ✓) ≈ $0.85/day |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 35.0¢ | 100 | 2 | $250.00 | ✅ scoring — ~0.6% of bid side (11,793 resting ≥ 10,000 ✓) ≈ $0.71/day |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | SELL | 30.0¢ | 50 | 3 | $250.00 | ✅ scoring — ~0.3% of ask side (50,902 resting ≥ 10,000 ✓) ≈ $0.34/day |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 34.0¢ | 100 | 3 | $250.00 | ✅ scoring — ~0.2% of bid side (11,793 resting ≥ 10,000 ✓) ≈ $0.21/day |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 10.0¢ | 10 | 0 | — | ❌ no active reward program on this market |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 90.0¢ | 10 | 32 | — | ❌ no active reward program on this market |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `vmc-ussep-misen-2026-08-04-els15-20` | $250.00 | 0.30 | 10,000 | SELL side (50,251 resting) | ~44.4% | ~$55.56 |
| `vmc-ussep-misen-2026-08-04-els5-10` | $250.00 | 0.30 | 10,000 | SELL side (50,251 resting) | ~44.4% | ~$55.56 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $250.00 | 0.30 | 10,000 | SELL side (50,251 resting) | ~44.4% | ~$55.56 |
| `paccc-usse-midterms-2026-11-03-rep` | $250.00 | 0.30 | 10,000 | BUY side (588,119 resting) | ~40.7% | ~$50.85 |
| `vmc-ussep-misen-2026-08-04-ste05-10` | $250.00 | 0.30 | 10,000 | SELL side (50,650 resting) | ~35.1% | ~$43.88 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $250.00 | 0.30 | 10,000 | SELL side (50,651 resting) | ~35.1% | ~$43.86 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $250.00 | 0.30 | 10,000 | SELL side (51,383 resting) | ~27.3% | ~$34.12 |
| `vmc-ussep-misen-2026-08-04-els10-15` | $250.00 | 0.30 | 10,000 | SELL side (50,645 resting) | ~23.7% | ~$29.62 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $250.00 | 0.30 | 10,000 | SELL side (50,647 resting) | ~23.6% | ~$29.55 |
| `paccc-usse-midterms-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | BUY side (512,198 resting) | ~21.0% | ~$26.27 |
| `ewc-usgub-ks-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | SELL side (124,235 resting) | ~11.5% | ~$14.42 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 | 0.30 | 10,000 | SELL side (49,183 resting) | ~5.2% | ~$6.46 |

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
| 2026-07-18 06:22:35 | ✅ ok | 83 | $97.93 |
| 2026-07-18 04:07:22 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:40:46 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:37:44 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:32:09 | ✅ ok | 83 | $97.93 |
| 2026-07-18 00:12:37 | ✅ ok | 72 | $80.91 |
| 2026-07-18 00:01:41 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:49:54 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:34:53 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:11:26 | ✅ ok | 72 | $80.91 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
