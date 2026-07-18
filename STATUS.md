# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-18 18:10 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$77.05/day estimated (ceiling, not promise — details below)

**Earned:** $97.93 lifetime ($78.17 paid). Last three recorded days — 2026-07-16: **$17.02** · 2026-07-15: **$1.53** · 2026-07-14: **$13.16** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — SELL at the best price, ~$23.86/day for 200 contracts. Runners-up: `paccc-usho-midterms-2026-11-03-dem` (~$22.13/day), `paccc-usse-midterms-2026-11-03-dem` (~$10.63/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$77.05/day (~$3.21/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 28.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~99.6% of ask side (50,851 resting ≥ 10,000 ✓) ≈ $24.90/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | SELL | 51.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~80.0% of ask side (60,757 resting ≥ 10,000 ✓) ≈ $20.00/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 6.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~49.7% of bid side (20,244 resting ≥ 10,000 ✓) ≈ $12.43/day (pool ÷ 5 markets) |
| `cranc-uspres28-12-31-2026-marrub` | SELL | 40.0¢ | 20 | 0 | $250.00 | ✅ scoring — ~44.5% of ask side (78,383 resting ≥ 10,000 ✓) ≈ $1.69/day (pool ÷ 33 markets) |
| `stsc-hormuz-normal-aug31` | BUY | 12.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~31.0% of bid side (20,970 resting ≥ 10,000 ✓) ≈ $0.76/day (pool ÷ 3 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | SELL | 45.0¢ | 20 | 0 | $250.00 | ✅ scoring — ~29.7% of ask side (26,318 resting ≥ 10,000 ✓) ≈ $1.13/day (pool ÷ 33 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 1.0¢ | 10,000 | 5 | $250.00 | ✅ scoring — ~24.2% of bid side (20,244 resting ≥ 10,000 ✓) ≈ $6.04/day (pool ÷ 5 markets) |
| `paccc-usse-midterms-2026-11-03-rep` | BUY | 56.6¢ | 100 | 0 | $250.00 | ✅ scoring — ~9.6% of bid side (576,519 resting ≥ 10,000 ✓) ≈ $6.00/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 19.0¢ | 100 | 2 | $250.00 | ✅ scoring — ~4.9% of bid side (10,625 resting ≥ 10,000 ✓) ≈ $1.22/day (pool ÷ 5 markets) |
| `cranc-uspres28-12-31-2026-dontru` | SELL | 35.0¢ | 20 | 1 | $250.00 | ✅ scoring — ~3.4% of ask side (75,740 resting ≥ 10,000 ✓) ≈ $0.13/day (pool ÷ 33 markets) |
| `pic-congress-trump-2026-12-31` | SELL | 8.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~1.3% of ask side (142,896 resting ≥ 10,000 ✓) ≈ $1.63/day |
| `paccc-usho-midterms-2026-11-03-rep` | SELL | 17.9¢ | 115 | 0 | $250.00 | ✅ scoring — ~1.0% of ask side (713,848 resting ≥ 10,000 ✓) ≈ $0.61/day (pool ÷ 2 markets) |
| `enwc-ussep-me-2026-07-27-dem-dankle` | SELL | 3.0¢ | 29 | 0 | $250.00 | ✅ scoring — ~0.9% of ask side (80,883 resting ≥ 10,000 ✓) ≈ $0.13/day (pool ÷ 9 markets) |
| `enwc-usgubp-mich-2026-08-04-rep-perjoh` | BUY | 9.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~0.5% of bid side (59,172 resting ≥ 10,000 ✓) ≈ $0.22/day (pool ÷ 3 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | SELL | 51.0¢ | 20 | 2 | $250.00 | ✅ scoring — ~0.4% of ask side (60,833 resting ≥ 10,000 ✓) ≈ $0.10/day (pool ÷ 5 markets) |
| `enwc-usgubp-mich-2026-08-04-rep-perjoh` | SELL | 40.0¢ | 100 | 3 | $250.00 | ✅ scoring — ~0.2% of ask side (54,013 resting ≥ 10,000 ✓) ≈ $0.07/day (pool ÷ 3 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 1.0¢ | 10,000 | 20 | $250.00 | ✅ scoring — ~0.0% of bid side (10,625 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | SELL | 99.0¢ | 10,000 | 48 | $250.00 | ✅ scoring — ~0.0% of ask side (60,757 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | SELL | 99.0¢ | 10,000 | 50 | $250.00 | ✅ scoring — ~0.0% of ask side (60,833 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 8.0¢ | 100 | 1 | $250.00 | ❌ side has 1,023 of 10,000 Target Size — side not qualifying |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 14.0¢ | 100 | 7 | $250.00 | ❌ side has 1,023 of 10,000 Target Size — side not qualifying |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (60,804 resting) | ~38.2% | ~$23.86 |
| `paccc-usho-midterms-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (733,165 resting) | ~35.4% | ~$22.13 |
| `paccc-usse-midterms-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (498,442 resting) | ~17.0% | ~$10.63 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (64,390 resting) | ~9.0% | ~$5.64 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (48,910 resting) | ~8.4% | ~$5.23 |
| `cranc-uspres28-12-31-2026-andyan` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (25,005 resting) | ~89.8% | ~$3.40 |
| `cranc-uspres28-12-31-2026-hunbid` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (23,654 resting) | ~86.3% | ~$3.27 |
| `cranc-uspres28-12-31-2026-rahema` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (32,827 resting) | ~83.3% | ~$3.16 |
| `cranc-uspres28-12-31-2026-corboo` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (25,862 resting) | ~83.3% | ~$3.15 |
| `cranc-uspres28-12-31-2026-betoro` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (18,744 resting) | ~77.1% | ~$2.92 |
| `cranc-uspres28-12-31-2026-erikir` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (18,730 resting) | ~77.0% | ~$2.92 |
| `cranc-uspres28-12-31-2026-markel` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (75,618 resting) | ~76.9% | ~$2.91 |

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
| 2026-07-18 18:10:35 | ✅ ok | 83 | $97.93 |
| 2026-07-18 17:17:57 | ✅ ok | 83 | $97.93 |
| 2026-07-18 16:38:47 | ✅ ok | 83 | $97.93 |
| 2026-07-18 16:13:22 | ✅ ok | 83 | $97.93 |
| 2026-07-18 15:18:09 | ✅ ok | 83 | $97.93 |
| 2026-07-18 14:47:54 | ✅ ok | 83 | $97.93 |
| 2026-07-18 14:44:56 | ✅ ok | 83 | $97.93 |
| 2026-07-18 14:41:45 | ✅ ok | 83 | $97.93 |
| 2026-07-18 14:33:27 | ✅ ok | 83 | $97.93 |
| 2026-07-18 14:30:19 | ✅ ok | 83 | $97.93 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
