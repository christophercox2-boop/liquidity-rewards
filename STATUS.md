# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-18 08:13 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📍 Right now — your resting orders

### Estimated earning rate: ~$29.83/day (~$1.24/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, and each pool splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 10.0¢ | 129 | 0 | $250.00 | ✅ scoring — ~8.6% of ask side (40,695 resting ≥ 10,000 ✓) ≈ $10.80/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 90.0¢ | 129 | 0 | $250.00 | ✅ scoring — ~8.3% of bid side (11,819 resting ≥ 10,000 ✓) ≈ $10.43/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | SELL | 91.0¢ | 70 | 0 | $250.00 | ✅ scoring — ~4.0% of ask side (12,425 resting ≥ 10,000 ✓) ≈ $5.00/day |
| `ewc-usgub-ca-2026-11-03-xavbec` | BUY | 93.0¢ | 125 | 0 | $250.00 | ✅ scoring — ~1.0% of bid side (86,163 resting ≥ 10,000 ✓) ≈ $1.27/day |
| `ewc-usgub-ca-2026-11-03-stehil` | SELL | 7.0¢ | 125 | 1 | $250.00 | ✅ scoring — ~0.9% of ask side (92,385 resting ≥ 10,000 ✓) ≈ $1.18/day |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 3.0¢ | 29 | 0 | $250.00 | ✅ scoring — ~0.9% of ask side (30,883 resting ≥ 10,000 ✓) ≈ $1.16/day |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 35.0¢ | 100 | 23 | $250.00 | ✅ scoring — ~0.0% of bid side (11,426 resting ≥ 10,000 ✓) ≈ $0.00/day |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 34.0¢ | 100 | 24 | $250.00 | ✅ scoring — ~0.0% of bid side (11,426 resting ≥ 10,000 ✓) ≈ $0.00/day |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 10.0¢ | 10 | 0 | — | ❌ no active reward program on this market |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 90.0¢ | 129 | 0 | $250.00 | ❌ side has 1,827 of 10,000 Target Size — side not qualifying |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 11.0¢ | 130 | 0 | $250.00 | ❌ side has 1,613 of 10,000 Target Size — side not qualifying |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 21.0¢ | 10 | 15 | $250.00 | ❌ side has 1,301 of 10,000 Target Size — side not qualifying |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 25.0¢ | 10 | 19 | $250.00 | ❌ side has 1,301 of 10,000 Target Size — side not qualifying |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 25.0¢ | 60 | 19 | $250.00 | ❌ side has 1,301 of 10,000 Target Size — side not qualifying |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 25.0¢ | 10 | 19 | $250.00 | ❌ side has 1,301 of 10,000 Target Size — side not qualifying |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | SELL | 30.0¢ | 50 | 24 | $250.00 | ❌ side has 1,049 of 10,000 Target Size — side not qualifying |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 90.0¢ | 10 | 32 | — | ❌ no active reward program on this market |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $250.00 | 0.30 | 10,000 | SELL side (11,226 resting) | ~97.6% | ~$121.95 |
| `vmc-ussep-misen-2026-08-04-ste0-5` | $250.00 | 0.30 | 10,000 | BUY side (21,100 resting) | ~88.7% | ~$110.91 |
| `paccc-usho-midterms-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | BUY side (741,539 resting) | ~35.3% | ~$44.14 |
| `paccc-usse-midterms-2026-11-03-rep` | $250.00 | 0.30 | 10,000 | BUY side (537,244 resting) | ~28.5% | ~$35.57 |
| `paccc-usse-midterms-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | BUY side (499,403 resting) | ~23.3% | ~$29.19 |
| `enwc-usgubp-mn-2026-08-11-rep-kenqua` | $250.00 | 0.30 | 10,000 | SELL side (43,851 resting) | ~17.4% | ~$21.77 |
| `ewc-usgub-ks-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | SELL side (124,401 resting) | ~10.5% | ~$13.16 |
| `enwc-usgubp-mn-2026-08-11-rep-miklin` | $250.00 | 0.30 | 10,000 | SELL side (51,929 resting) | ~9.4% | ~$11.72 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 | 0.30 | 10,000 | SELL side (48,950 resting) | ~8.2% | ~$10.28 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 | 0.30 | 10,000 | SELL side (22,401 resting) | ~8.2% | ~$10.20 |
| `enwc-usgubp-mn-2026-08-11-rep-lisdem` | $250.00 | 0.30 | 10,000 | BUY side (41,278 resting) | ~4.8% | ~$6.04 |
| `ewc-usgub-oh-2026-11-03-rep` | $250.00 | 0.30 | 10,000 | BUY side (221,071 resting) | ~4.5% | ~$5.65 |

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
| 2026-07-18 08:13:34 | ✅ ok | 83 | $97.93 |
| 2026-07-18 06:22:35 | ✅ ok | 83 | $97.93 |
| 2026-07-18 04:07:22 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:40:46 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:37:44 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:32:09 | ✅ ok | 83 | $97.93 |
| 2026-07-18 00:12:37 | ✅ ok | 72 | $80.91 |
| 2026-07-18 00:01:41 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:49:54 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:34:53 | ✅ ok | 72 | $80.91 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
