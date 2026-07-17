# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-17 21:11 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📍 Right now — your resting orders

Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. "Share" is your estimated cut of that side's score this second. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `apdc-jerpowgov-2026-12-31` | BUY | 2.0¢ | 2,500 | 1 | $250.00 | ✅ scoring — ~18.6% of bid side |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 89.0¢ | 77 | 0 | $250.00 | ✅ scoring — ~4.8% of bid side |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 5.0¢ | 20 | 1 | $250.00 | ❌ outside Target Size window (order 1 ticks from best; window ends 0) |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 5.0¢ | 9 | 1 | $250.00 | ❌ outside Target Size window (order 1 ticks from best; window ends 0) |

## 💡 Suggested markets — active pools you're not in

Ranked by the estimated share of a side's score a **200-contract order at the best price** would capture today, using each market's real book, Discount Factor, and Target Size. Higher = less competition for the pool.

| Market | Reward pool | Discount | Target Size | Best entry | Est. share |
|---|---:|---:|---:|---|---:|
| `atc-lmx-asl-caz-2026-07-17-asl` | $2,400.00 | 0.35 | 10,000 | SELL side | ~3.1% |
| `atc-lmx-ju-pue-2026-07-17-draw` | $2,400.00 | 0.35 | 10,000 | BUY side | ~2.1% |
| `atc-lmx-pum-pac-2026-07-18-pum` | $2,400.00 | 0.35 | 10,000 | SELL side | ~1.7% |
| `atc-lmx-leo-atl-2026-07-17-leo` | $2,400.00 | 0.35 | 10,000 | BUY side | ~1.4% |
| `atc-lmx-caz-pue-2026-07-21-caz` | $2,400.00 | 0.35 | 10,000 | SELL side | ~1.4% |
| `atc-lmx-caz-pue-2026-07-21-draw` | $2,400.00 | 0.35 | 10,000 | BUY side | ~1.4% |
| `atc-lmx-gua-tol-2026-07-18-draw` | $2,400.00 | 0.35 | 10,000 | BUY side | ~1.3% |
| `atc-lmx-cmf-san-2026-07-18-draw` | $2,400.00 | 0.35 | 10,000 | BUY side | ~1.3% |
| `atc-lmx-gua-tol-2026-07-18-gua` | $2,400.00 | 0.35 | 10,000 | BUY side | ~1.3% |
| `atc-lmx-cmf-san-2026-07-18-san` | $2,400.00 | 0.35 | 10,000 | SELL side | ~1.3% |
| `atc-lmx-que-ame-2026-07-18-ame` | $2,400.00 | 0.35 | 10,000 | SELL side | ~1.2% |
| `atc-lmx-que-ame-2026-07-18-draw` | $2,400.00 | 0.35 | 10,000 | SELL side | ~1.2% |

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
| 2026-07-17 21:11:09 | ✅ ok | 72 | $80.91 |
| 2026-07-17 21:09:18 | ✅ ok | 72 | $80.91 |
| 2026-07-17 20:36:53 | ✅ ok | 72 | $80.91 |
| 2026-07-17 20:34:20 | ✅ ok | 72 | $80.91 |
| 2026-07-17 19:51:06 | ✅ ok | 72 | $80.91 |
| 2026-07-17 19:48:51 | ✅ ok | 72 | $80.91 |
| 2026-07-17 19:46:02 | ✅ ok | 72 | $80.91 |
| 2026-07-17 19:43:28 | ✅ ok | 72 | $80.91 |
| 2026-07-17 19:35:58 | ✅ ok | 72 | $80.91 |
| 2026-07-17 18:17:44 | ✅ ok | 72 | $80.91 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
