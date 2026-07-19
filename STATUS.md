# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 00:12 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$26.17/day estimated (ceiling, not promise — details below)

**Earned:** $97.93 lifetime ($78.17 paid). Last three recorded days — 2026-07-16: **$17.02** · 2026-07-15: **$1.53** · 2026-07-14: **$13.16** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — SELL at the best price, ~$5.66/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$5.23/day), `cranc-uspres28-12-31-2026-margre` (~$3.59/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$26.17/day (~$1.09/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 1.0¢ | 10,000 | 5 | $250.00 | ✅ scoring — ~79.0% of bid side (10,195 resting ≥ 10,000 ✓) ≈ $19.75/day (pool ÷ 5 markets) |
| `cranc-uspres28-12-31-2026-marrub` | SELL | 40.0¢ | 20 | 0 | $250.00 | ✅ scoring — ~44.5% of ask side (28,387 resting ≥ 10,000 ✓) ≈ $1.69/day (pool ÷ 33 markets) |
| `stsc-hormuz-normal-aug31` | BUY | 12.0¢ | 88 | 0 | $250.00 | ✅ scoring — ~41.6% of bid side (20,897 resting ≥ 10,000 ✓) ≈ $1.02/day (pool ÷ 3 markets) |
| `enwc-usgubp-mich-2026-08-04-rep-perjoh` | BUY | 9.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~8.4% of bid side (43,475 resting ≥ 10,000 ✓) ≈ $3.51/day (pool ÷ 3 markets) |
| `cranc-uspres28-12-31-2026-dontru` | SELL | 35.0¢ | 20 | 1 | $250.00 | ✅ scoring — ~3.4% of ask side (16,889 resting ≥ 10,000 ✓) ≈ $0.13/day (pool ÷ 33 markets) |
| `enwc-usgubp-mich-2026-08-04-rep-perjoh` | SELL | 40.0¢ | 100 | 3 | $250.00 | ✅ scoring — ~0.2% of ask side (50,934 resting ≥ 10,000 ✓) ≈ $0.08/day (pool ÷ 3 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | BUY | 40.0¢ | 20 | 9 | $250.00 | ✅ scoring — ~0.0% of bid side (22,716 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 33 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 19.0¢ | 100 | 40 | $250.00 | ✅ scoring — ~0.0% of bid side (10,400 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | SELL | 51.0¢ | 20 | 44 | $250.00 | ✅ scoring — ~0.0% of ask side (10,855 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 5 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | SELL | 51.0¢ | 100 | 44 | $250.00 | ✅ scoring — ~0.0% of ask side (11,306 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 5 markets) |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (64,381 resting) | ~9.1% | ~$5.66 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (48,660 resting) | ~8.4% | ~$5.23 |
| `cranc-uspres28-12-31-2026-margre` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (30,924 resting) | ~94.7% | ~$3.59 |
| `cranc-uspres28-12-31-2026-hunbid` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (26,142 resting) | ~91.2% | ~$3.45 |
| `cranc-uspres28-12-31-2026-andyan` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (21,648 resting) | ~89.7% | ~$3.40 |
| `cranc-uspres28-12-31-2026-markel` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,600 resting) | ~84.4% | ~$3.20 |
| `cranc-uspres28-12-31-2026-rahema` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (32,677 resting) | ~83.1% | ~$3.15 |
| `cranc-uspres28-12-31-2026-betoro` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (35,649 resting) | ~78.8% | ~$2.98 |
| `cranc-uspres28-12-31-2026-erikir` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (26,980 resting) | ~78.4% | ~$2.97 |
| `cranc-uspres28-12-31-2026-nikhal` | $250.00 ÷ 33 | 0.30 | 10,000 | BUY side (26,855 resting) | ~76.9% | ~$2.91 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (80,333 resting) | ~4.4% | ~$2.76 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (56,256 resting) | ~3.8% | ~$2.40 |

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
| 2026-07-19 00:12:38 | ✅ ok | 83 | $97.93 |
| 2026-07-18 23:14:00 | ✅ ok | 83 | $97.93 |
| 2026-07-18 22:10:04 | ✅ ok | 83 | $97.93 |
| 2026-07-18 21:08:25 | ✅ ok | 83 | $97.93 |
| 2026-07-18 19:35:32 | ✅ ok | 83 | $97.93 |
| 2026-07-18 18:10:35 | ✅ ok | 83 | $97.93 |
| 2026-07-18 17:17:57 | ✅ ok | 83 | $97.93 |
| 2026-07-18 16:38:47 | ✅ ok | 83 | $97.93 |
| 2026-07-18 16:13:22 | ✅ ok | 83 | $97.93 |
| 2026-07-18 15:18:09 | ✅ ok | 83 | $97.93 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
