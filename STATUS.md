# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-18 22:10 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$68.30/day estimated (ceiling, not promise — details below)

**Earned:** $97.93 lifetime ($78.17 paid). Last three recorded days — 2026-07-16: **$17.02** · 2026-07-15: **$1.53** · 2026-07-14: **$13.16** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `paccc-usse-midterms-2026-11-03-rep` — BUY at the best price, ~$35.44/day for 200 contracts. Runners-up: `paccc-usse-midterms-2026-11-03-dem` (~$33.58/day), `enwc-ussep-mn-2026-08-11-dem-angcra` (~$5.66/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$68.30/day (~$2.85/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 8.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~85.7% of ask side (10,706 resting ≥ 10,000 ✓) ≈ $21.42/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 28.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~83.6% of ask side (50,416 resting ≥ 10,000 ✓) ≈ $20.91/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 6.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~49.7% of bid side (20,244 resting ≥ 10,000 ✓) ≈ $12.43/day (pool ÷ 5 markets) |
| `cranc-uspres28-12-31-2026-marrub` | SELL | 40.0¢ | 20 | 0 | $250.00 | ✅ scoring — ~44.5% of ask side (78,383 resting ≥ 10,000 ✓) ≈ $1.69/day (pool ÷ 33 markets) |
| `stsc-hormuz-normal-aug31` | BUY | 12.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~31.0% of bid side (20,970 resting ≥ 10,000 ✓) ≈ $0.76/day (pool ÷ 3 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 1.0¢ | 10,000 | 5 | $250.00 | ✅ scoring — ~24.2% of bid side (20,244 resting ≥ 10,000 ✓) ≈ $6.04/day (pool ÷ 5 markets) |
| `enwc-usgubp-mich-2026-08-04-rep-perjoh` | BUY | 9.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~4.3% of bid side (32,118 resting ≥ 10,000 ✓) ≈ $1.80/day (pool ÷ 3 markets) |
| `cranc-uspres28-12-31-2026-dontru` | SELL | 35.0¢ | 20 | 1 | $250.00 | ✅ scoring — ~3.4% of ask side (75,740 resting ≥ 10,000 ✓) ≈ $0.13/day (pool ÷ 33 markets) |
| `enwc-usgubp-mich-2026-08-04-rep-perjoh` | SELL | 40.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~2.5% of ask side (43,513 resting ≥ 10,000 ✓) ≈ $1.06/day (pool ÷ 3 markets) |
| `pic-congress-trump-2026-12-31` | SELL | 8.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~1.1% of ask side (143,920 resting ≥ 10,000 ✓) ≈ $1.44/day |
| `paccc-usho-midterms-2026-11-03-rep` | SELL | 17.9¢ | 115 | 0 | $250.00 | ✅ scoring — ~0.9% of ask side (722,118 resting ≥ 10,000 ✓) ≈ $0.56/day (pool ÷ 2 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | BUY | 40.0¢ | 20 | 3 | $250.00 | ✅ scoring — ~0.7% of bid side (20,334 resting ≥ 10,000 ✓) ≈ $0.03/day (pool ÷ 33 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | SELL | 51.0¢ | 20 | 3 | $250.00 | ✅ scoring — ~0.1% of ask side (50,921 resting ≥ 10,000 ✓) ≈ $0.02/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 14.0¢ | 100 | 7 | $250.00 | ✅ scoring — ~0.1% of ask side (10,706 resting ≥ 10,000 ✓) ≈ $0.02/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | SELL | 51.0¢ | 100 | 44 | $250.00 | ✅ scoring — ~0.0% of ask side (50,852 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 19.0¢ | 100 | 3 | $250.00 | ❌ side has 725 of 10,000 Target Size — side not qualifying |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usse-midterms-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (622,546 resting) | ~56.7% | ~$35.44 |
| `paccc-usse-midterms-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (429,889 resting) | ~53.7% | ~$33.58 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (64,381 resting) | ~9.1% | ~$5.66 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (48,899 resting) | ~8.4% | ~$5.23 |
| `cranc-uspres28-12-31-2026-hunbid` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (26,147 resting) | ~89.1% | ~$3.38 |
| `cranc-uspres28-12-31-2026-andyan` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (21,651 resting) | ~88.5% | ~$3.35 |
| `cranc-uspres28-12-31-2026-markel` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (75,601 resting) | ~84.4% | ~$3.20 |
| `cranc-uspres28-12-31-2026-rahema` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (32,677 resting) | ~83.1% | ~$3.15 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (51,542 resting) | ~4.8% | ~$3.03 |
| `cranc-uspres28-12-31-2026-betoro` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (35,652 resting) | ~78.2% | ~$2.96 |
| `cranc-uspres28-12-31-2026-erikir` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (18,730 resting) | ~77.0% | ~$2.92 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (80,333 resting) | ~4.4% | ~$2.76 |

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
| 2026-07-18 22:10:04 | ✅ ok | 83 | $97.93 |
| 2026-07-18 21:08:25 | ✅ ok | 83 | $97.93 |
| 2026-07-18 19:35:32 | ✅ ok | 83 | $97.93 |
| 2026-07-18 18:10:35 | ✅ ok | 83 | $97.93 |
| 2026-07-18 17:17:57 | ✅ ok | 83 | $97.93 |
| 2026-07-18 16:38:47 | ✅ ok | 83 | $97.93 |
| 2026-07-18 16:13:22 | ✅ ok | 83 | $97.93 |
| 2026-07-18 15:18:09 | ✅ ok | 83 | $97.93 |
| 2026-07-18 14:47:54 | ✅ ok | 83 | $97.93 |
| 2026-07-18 14:44:56 | ✅ ok | 83 | $97.93 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
