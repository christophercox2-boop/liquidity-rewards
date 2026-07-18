# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-18 03:32 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📍 Right now — your resting orders

### Estimated earning rate: ~$110.28/day (~$4.60/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, and each pool splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 25.0¢ | 10 | 0 | $250.00 | ✅ scoring — ~55.6% of ask side (10,764 resting ≥ 10,000 ✓) ≈ $69.44/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | SELL | 91.0¢ | 70 | 0 | $250.00 | ✅ scoring — ~13.2% of ask side (11,612 resting ≥ 10,000 ✓) ≈ $16.47/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 90.0¢ | 129 | 0 | $250.00 | ✅ scoring — ~6.9% of bid side (55,679 resting ≥ 10,000 ✓) ≈ $8.65/day |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 34.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~5.5% of bid side (11,326 resting ≥ 10,000 ✓) ≈ $6.85/day |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | SELL | 30.0¢ | 50 | 1 | $250.00 | ✅ scoring — ~3.2% of ask side (11,252 resting ≥ 10,000 ✓) ≈ $3.96/day |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | SELL | 45.0¢ | 50 | 1 | $250.00 | ✅ scoring — ~2.3% of ask side (10,981 resting ≥ 10,000 ✓) ≈ $2.91/day |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 3.0¢ | 29 | 0 | $250.00 | ✅ scoring — ~0.9% of ask side (31,561 resting ≥ 10,000 ✓) ≈ $1.09/day |
| `apdc-jerpowgov-2026-12-31` | BUY | 2.0¢ | 2,500 | 5 | $250.00 | ✅ scoring — ~0.7% of bid side (15,326 resting ≥ 10,000 ✓) ≈ $0.90/day |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 99.0¢ | 10,000 | 74 | $250.00 | ✅ scoring — ~0.0% of ask side (10,764 resting ≥ 10,000 ✓) ≈ $0.00/day |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $250.00 | 0.30 | 10,000 | SELL side (11,127 resting) | ~97.1% | ~$121.36 |
| `vmc-ussep-misen-2026-08-04-ste0-5` | $250.00 | 0.30 | 10,000 | BUY side (11,141 resting) | ~75.1% | ~$93.91 |
| `paccc-usho-midterms-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | SELL side (627,398 resting) | ~68.6% | ~$85.79 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $250.00 | 0.30 | 10,000 | SELL side (11,365 resting) | ~24.5% | ~$30.67 |
| `vmc-ussep-misen-2026-08-04-ste05-10` | $250.00 | 0.30 | 10,000 | SELL side (11,367 resting) | ~24.5% | ~$30.60 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $250.00 | 0.30 | 10,000 | SELL side (11,393 resting) | ~23.7% | ~$29.66 |
| `vmc-ussep-misen-2026-08-04-els15-20` | $250.00 | 0.30 | 10,000 | SELL side (11,394 resting) | ~23.7% | ~$29.62 |
| `vmc-ussep-misen-2026-08-04-els5-10` | $250.00 | 0.30 | 10,000 | SELL side (11,394 resting) | ~23.7% | ~$29.62 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $250.00 | 0.30 | 10,000 | SELL side (11,394 resting) | ~23.7% | ~$29.62 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $250.00 | 0.30 | 10,000 | SELL side (11,394 resting) | ~23.7% | ~$29.62 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $250.00 | 0.30 | 10,000 | SELL side (11,531 resting) | ~17.7% | ~$22.10 |
| `paccc-usse-midterms-2026-11-03-dem` | $250.00 | 0.30 | 10,000 | BUY side (373,327 resting) | ~11.7% | ~$14.68 |

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
| 2026-07-18 03:32:09 | ✅ ok | 83 | $97.93 |
| 2026-07-18 00:12:37 | ✅ ok | 72 | $80.91 |
| 2026-07-18 00:01:41 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:49:54 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:34:53 | ✅ ok | 72 | $80.91 |
| 2026-07-17 23:11:26 | ✅ ok | 72 | $80.91 |
| 2026-07-17 22:08:52 | ✅ ok | 72 | $80.91 |
| 2026-07-17 21:42:22 | ✅ ok | 72 | $80.91 |
| 2026-07-17 21:39:48 | ✅ ok | 72 | $80.91 |
| 2026-07-17 21:35:48 | ✅ ok | 72 | $80.91 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
