# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-18 13:53 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📍 Right now — your resting orders

### Estimated earning rate: ~$350.35/day (~$14.60/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event (so it's divided across the event's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `cranc-uspres28-12-31-2026-dontru` | SELL | 35.0¢ | 20 | 0 | $250.00 | ✅ scoring — ~95.8% of ask side (50,928 resting ≥ 10,000 ✓) ≈ $119.79/day |
| `cranc-uspres28-12-31-2026-marrub` | SELL | 40.0¢ | 20 | 0 | $250.00 | ✅ scoring — ~80.5% of ask side (78,681 resting ≥ 10,000 ✓) ≈ $100.61/day |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 51.0¢ | 355 | 0 | $250.00 | ✅ scoring — ~58.7% of ask side (10,607 resting ≥ 10,000 ✓) ≈ $7.33/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 51.0¢ | 355 | 0 | $250.00 | ✅ scoring — ~49.1% of ask side (50,999 resting ≥ 10,000 ✓) ≈ $6.14/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 51.0¢ | 355 | 0 | $250.00 | ✅ scoring — ~49.1% of ask side (11,000 resting ≥ 10,000 ✓) ≈ $6.14/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 51.0¢ | 355 | 0 | $250.00 | ✅ scoring — ~49.1% of ask side (11,393 resting ≥ 10,000 ✓) ≈ $6.14/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 13.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~47.0% of bid side (11,164 resting ≥ 10,000 ✓) ≈ $11.75/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 6.0¢ | 191 | 0 | $250.00 | ✅ scoring — ~45.4% of ask side (50,831 resting ≥ 10,000 ✓) ≈ $11.36/day (pool ÷ 5 markets) |
| `stsc-hormuz-normal-aug31` | BUY | 12.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~31.0% of bid side (20,970 resting ≥ 10,000 ✓) ≈ $2.28/day |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~19.1% of bid side (52,381 resting ≥ 10,000 ✓) ≈ $4.77/day (pool ÷ 5 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | SELL | 45.0¢ | 20 | 0 | $250.00 | ✅ scoring — ~16.4% of ask side (27,361 resting ≥ 10,000 ✓) ≈ $20.44/day |
| `lawec-saveact-2026-12-31` | BUY | 20.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~16.0% of bid side (37,754 resting ≥ 10,000 ✓) ≈ $20.05/day |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~14.0% of bid side (71,241 resting ≥ 10,000 ✓) ≈ $3.51/day (pool ÷ 5 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 10.0¢ | 199 | 0 | $250.00 | ✅ scoring — ~12.3% of ask side (92,765 resting ≥ 10,000 ✓) ≈ $15.38/day |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 90.0¢ | 199 | 0 | $250.00 | ✅ scoring — ~3.6% of bid side (44,081 resting ≥ 10,000 ✓) ≈ $4.55/day |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 11.0¢ | 201 | 0 | $250.00 | ✅ scoring — ~3.5% of ask side (96,934 resting ≥ 10,000 ✓) ≈ $4.37/day |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 90.0¢ | 199 | 0 | $250.00 | ✅ scoring — ~2.5% of bid side (33,822 resting ≥ 10,000 ✓) ≈ $3.10/day |
| `pic-congress-trump-2026-12-31` | SELL | 8.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~1.2% of ask side (143,608 resting ≥ 10,000 ✓) ≈ $1.50/day |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 3.0¢ | 29 | 0 | $250.00 | ✅ scoring — ~0.9% of ask side (80,883 resting ≥ 10,000 ✓) ≈ $1.16/day |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usse-midterms-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (497,300 resting) | ~32.8% | ~$20.52 |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | $250.00 ÷ 5 | 0.30 | 10,000 | BUY side (13,750 resting) | ~67.3% | ~$16.84 |
| `vmc-ussep-misen-2026-08-04-els10-15` | $250.00 ÷ 10 | 0.30 | 10,000 | SELL side (17,600 resting) | ~88.9% | ~$11.11 |
| `vmc-ussep-misen-2026-08-04-ste0-5` | $250.00 ÷ 10 | 0.30 | 10,000 | BUY side (11,150 resting) | ~77.7% | ~$9.71 |
| `paccc-usse-midterms-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (524,094 resting) | ~15.5% | ~$9.66 |
| `enwc-usgubp-mn-2026-08-11-rep-kenqua` | $250.00 ÷ 3 | 0.30 | 10,000 | SELL side (95,864 resting) | ~19.8% | ~$8.26 |
| `vmc-ussep-misen-2026-08-04-ste05-10` | $250.00 ÷ 10 | 0.30 | 10,000 | SELL side (11,054 resting) | ~60.8% | ~$7.60 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $250.00 ÷ 10 | 0.30 | 10,000 | SELL side (10,892 resting) | ~60.8% | ~$7.60 |
| `ewc-usgub-ks-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (123,242 resting) | ~10.6% | ~$6.61 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (50,611 resting) | ~9.2% | ~$5.72 |
| `vmc-ussep-misen-2026-08-04-els5-10` | $250.00 ÷ 10 | 0.30 | 10,000 | SELL side (11,050 resting) | ~43.0% | ~$5.38 |
| `enwc-usgubp-mn-2026-08-11-rep-lisdem` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (46,511 resting) | ~12.6% | ~$5.26 |

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
| 2026-07-18 13:53:35 | ✅ ok | 83 | $97.93 |
| 2026-07-18 13:34:58 | ✅ ok | 83 | $97.93 |
| 2026-07-18 13:29:37 | ✅ ok | 83 | $97.93 |
| 2026-07-18 12:19:42 | ✅ ok | 83 | $97.93 |
| 2026-07-18 11:26:27 | ✅ ok | 83 | $97.93 |
| 2026-07-18 09:49:19 | ✅ ok | 83 | $97.93 |
| 2026-07-18 08:13:34 | ✅ ok | 83 | $97.93 |
| 2026-07-18 06:22:35 | ✅ ok | 83 | $97.93 |
| 2026-07-18 04:07:22 | ✅ ok | 83 | $97.93 |
| 2026-07-18 03:40:46 | ✅ ok | 83 | $97.93 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
