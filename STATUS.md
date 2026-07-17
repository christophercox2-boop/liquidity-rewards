# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-17 21:29 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📍 Right now — your resting orders

### Estimated earning rate: ~$126.90/day (~$5.29/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, and each pool splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-nh-2026-09-01-rep-johsun` | SELL | 92.0¢ | 70 | 0 | $250.00 | ✅ scoring — ~89.9% of ask side ≈ $112.38/day |
| `apdc-jerpowgov-2026-12-31` | BUY | 2.0¢ | 2,500 | 4 | $250.00 | ✅ scoring — ~6.3% of bid side ≈ $7.90/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 89.0¢ | 77 | 0 | $250.00 | ✅ scoring — ~5.3% of bid side ≈ $6.61/day |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 5.0¢ | 20 | 1 | $250.00 | ❌ outside Target Size window (order 1 tick from best; window ends 0) |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 5.0¢ | 9 | 1 | $250.00 | ❌ outside Target Size window (order 1 tick from best; window ends 0) |

## 💡 Suggested political markets

_No political markets with reachable pools found this run._

## Totals

| | Amount |
|---|---:|
| Paid | $78.17 |
| Pending | $1.53 |
| Skipped | $1.21 |
| **Total earned** | **$80.91** |

72 reward rows · 13 days with rewards · 29 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
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
| 2026-07 | $80.91 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-ussep-me-2026-07-27-dem-dankle` | $41.23 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.56 |
| `paccc-usse-midterms-2026-11-03-rep` | $5.20 |
| `enwc-ussep-me-2026-07-27-dem-jargol` | $4.80 |
| `paccc-usho-midterms-2026-11-03-dem` | $4.06 |
| `enwc-ussep-me-2026-07-27-dem-trojac` | $2.28 |
| `enwc-ussep-me-2026-07-27-dem-shebel` | $1.20 |
| `paccc-usse-midterms-2026-11-03-dem` | $1.08 |
| `paccc-usho-midterms-2026-11-03-rep` | $0.85 |
| `ewc-usse-oh-2026-11-03-rep` | $0.64 |
| `ewc-usse-tx-2026-11-03-dem` | $0.58 |
| `ewc-usse-me-2026-11-03-dem` | $0.44 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $0.38 |
| `ewc-usgub-az-2026-11-03-dem` | $0.30 |
| `ewc-usse-ak-2026-11-03-dem` | $0.24 |

## Recent checks

| Checked (UTC) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-17 21:29:53 | ✅ ok | 72 | $80.91 |
| 2026-07-17 21:26:26 | ✅ ok | 72 | $80.91 |
| 2026-07-17 21:11:09 | ✅ ok | 72 | $80.91 |
| 2026-07-17 21:09:18 | ✅ ok | 72 | $80.91 |
| 2026-07-17 20:36:53 | ✅ ok | 72 | $80.91 |
| 2026-07-17 20:34:20 | ✅ ok | 72 | $80.91 |
| 2026-07-17 19:51:06 | ✅ ok | 72 | $80.91 |
| 2026-07-17 19:48:51 | ✅ ok | 72 | $80.91 |
| 2026-07-17 19:46:02 | ✅ ok | 72 | $80.91 |
| 2026-07-17 19:43:28 | ✅ ok | 72 | $80.91 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
