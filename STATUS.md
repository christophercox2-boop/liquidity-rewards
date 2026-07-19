# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 03:59 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$57.62/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$12.75/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$9.83/day), `enwc-usgubp-sd-2026-06-02-rep-tobdoe` (~$4.76/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$57.62/day (~$2.40/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `cranc-uspres28-12-31-2026-jdvan` | BUY | 1.0¢ | 9,987 | 1 | $250.00 | ✅ scoring — ~65.4% of bid side (15,222 resting ≥ 10,000 ✓) ≈ $2.48/day (pool ÷ 33 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~63.1% of bid side (15,850 resting ≥ 10,000 ✓) ≈ $26.29/day (pool ÷ 3 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | SELL | 94.0¢ | 500 | 1 | $250.00 | ✅ scoring — ~45.9% of ask side (36,152 resting ≥ 10,000 ✓) ≈ $1.74/day (pool ÷ 33 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 51.0¢ | 250 | 0 | $250.00 | ✅ scoring — ~38.5% of ask side (11,250 resting ≥ 10,000 ✓) ≈ $4.81/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 13.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~17.9% of ask side (10,596 resting ≥ 10,000 ✓) ≈ $11.16/day (pool ÷ 2 markets) |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | BUY | 68.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~6.6% of bid side (43,549 resting ≥ 10,000 ✓) ≈ $2.73/day (pool ÷ 3 markets) |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 90.0¢ | 64 | 1 | $250.00 | ✅ scoring — ~6.0% of bid side (37,823 resting ≥ 10,000 ✓) ≈ $3.77/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 86.0¢ | 65 | 2 | $250.00 | ✅ scoring — ~3.9% of bid side (10,483 resting ≥ 10,000 ✓) ≈ $2.45/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 9.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~1.6% of ask side (77,613 resting ≥ 10,000 ✓) ≈ $0.97/day (pool ÷ 2 markets) |
| `enwc-ussep-mi-2026-08-04-dem-halste` | BUY | 33.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~1.2% of bid side (72,426 resting ≥ 10,000 ✓) ≈ $0.51/day (pool ÷ 3 markets) |
| `enwc-ussep-mi-2026-08-04-dem-halste` | SELL | 35.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~1.2% of ask side (23,978 resting ≥ 10,000 ✓) ≈ $0.50/day (pool ÷ 3 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 10.0¢ | 98 | 3 | $250.00 | ✅ scoring — ~0.8% of ask side (10,923 resting ≥ 10,000 ✓) ≈ $0.21/day (pool ÷ 5 markets) |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 1.0¢ | 10,000 | 87 | $250.00 | ✅ scoring — ~0.0% of bid side (10,483 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 99.0¢ | 5,000 | 86 | $250.00 | ✅ scoring — ~0.0% of ask side (10,596 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 99.0¢ | 10,000 | 92 | $250.00 | ✅ scoring — ~0.0% of ask side (10,923 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 5 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 51.0¢ | 100 | 0 | $250.00 | ❌ side has 101 of 10,000 Target Size — side not qualifying |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 51.0¢ | 250 | 0 | $250.00 | ❌ side has 6,250 of 10,000 Target Size — side not qualifying |
| `opdc-trump-resig-2026-12-31` | SELL | 20.0¢ | 100 | 0 | — | ❌ no active reward program on this market |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 51.0¢ | 100 | 0 | $250.00 | ❌ side has 311 of 10,000 Target Size — side not qualifying |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | SELL | 70.0¢ | 100 | 1 | $250.00 | ❌ outside Target Size window (order 1 tick from best; window ends 0) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 99.0¢ | 2,000 | 90 | $250.00 | ❌ outside Target Size window (order 90 ticks from best; window ends 2) |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 1.0¢ | 10,000 | 90 | $250.00 | ❌ outside Target Size window (order 90 ticks from best; window ends 4) |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (26,861 resting) | ~20.4% | ~$12.75 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (10,176 resting) | ~15.7% | ~$9.83 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (63,971 resting) | ~7.6% | ~$4.76 |
| `cranc-uspres28-12-31-2026-jonoss` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,601 resting) | ~92.6% | ~$3.51 |
| `cranc-uspres28-12-31-2026-krinoe` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,780 resting) | ~90.9% | ~$3.44 |
| `cranc-uspres28-12-31-2026-andyan` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,779 resting) | ~90.1% | ~$3.41 |
| `cranc-uspres28-12-31-2026-bersan` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,776 resting) | ~88.9% | ~$3.37 |
| `cranc-uspres28-12-31-2026-betoro` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,776 resting) | ~88.9% | ~$3.37 |
| `cranc-uspres28-12-31-2026-dontrujr` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,776 resting) | ~88.9% | ~$3.37 |
| `cranc-uspres28-12-31-2026-dwajoh` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,776 resting) | ~88.9% | ~$3.37 |
| `cranc-uspres28-12-31-2026-elomus` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,776 resting) | ~88.9% | ~$3.37 |
| `cranc-uspres28-12-31-2026-jossha` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,776 resting) | ~88.9% | ~$3.37 |

## Totals

| | Amount |
|---|---:|
| Paid | $78.17 |
| Pending | $33.26 |
| Skipped | $1.21 |
| **Total earned** | **$112.64** |

102 reward rows · 15 days with rewards · 44 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-17 | $14.71 | `███████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $112.64 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.20 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.56 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $5.31 |
| `paccc-usse-midterms-2026-11-03-rep` | $5.29 |
| `apdc-jerpowgov-2026-12-31` | $5.25 |
| `enwc-ussep-me-2026-07-27-dem-jargol` | $4.80 |
| `ewc-usgub-ca-2026-11-03-stehil` | $4.49 |
| `paccc-usho-midterms-2026-11-03-dem` | $4.07 |
| `pic-congress-trump-2026-12-31` | $3.77 |
| `apdc-alito-2026-12-31` | $3.07 |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | $3.03 |
| `enwc-ussep-me-2026-07-27-dem-trojac` | $2.28 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $2.16 |
| `enwc-ussep-me-2026-07-27-dem-shebel` | $1.20 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $1.18 |

## Recent checks

| Checked (UTC) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-19 03:59:31 | ✅ ok | 102 | $112.64 |
| 2026-07-19 02:06:16 | ✅ ok | 102 | $112.64 |
| 2026-07-19 00:12:38 | ✅ ok | 83 | $97.93 |
| 2026-07-18 23:14:00 | ✅ ok | 83 | $97.93 |
| 2026-07-18 22:10:04 | ✅ ok | 83 | $97.93 |
| 2026-07-18 21:08:25 | ✅ ok | 83 | $97.93 |
| 2026-07-18 19:35:32 | ✅ ok | 83 | $97.93 |
| 2026-07-18 18:10:35 | ✅ ok | 83 | $97.93 |
| 2026-07-18 17:17:57 | ✅ ok | 83 | $97.93 |
| 2026-07-18 16:38:47 | ✅ ok | 83 | $97.93 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
