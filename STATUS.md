# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 02:06 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$65.71/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — SELL at the best price, ~$37.99/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-angcra` (~$22.92/day), `enwc-usgubp-sd-2026-06-02-rep-tobdoe` (~$9.81/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$65.71/day (~$2.74/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 10.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~71.5% of ask side (10,782 resting ≥ 10,000 ✓) ≈ $17.88/day (pool ÷ 5 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | SELL | 94.0¢ | 500 | 1 | $250.00 | ✅ scoring — ~47.5% of ask side (36,139 resting ≥ 10,000 ✓) ≈ $1.80/day (pool ÷ 33 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 51.0¢ | 250 | 0 | $250.00 | ✅ scoring — ~38.5% of ask side (11,250 resting ≥ 10,000 ✓) ≈ $4.81/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 51.0¢ | 250 | 0 | $250.00 | ✅ scoring — ~38.5% of ask side (11,250 resting ≥ 10,000 ✓) ≈ $4.81/day (pool ÷ 10 markets) |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | BUY | 68.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~23.4% of bid side (28,959 resting ≥ 10,000 ✓) ≈ $9.75/day (pool ÷ 3 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 9.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~19.7% of ask side (56,844 resting ≥ 10,000 ✓) ≈ $12.32/day (pool ÷ 2 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | BUY | 45.0¢ | 20 | 1 | $250.00 | ✅ scoring — ~19.4% of bid side (10,156 resting ≥ 10,000 ✓) ≈ $0.73/day (pool ÷ 33 markets) |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | SELL | 70.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~13.3% of ask side (42,068 resting ≥ 10,000 ✓) ≈ $5.53/day (pool ÷ 3 markets) |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 90.0¢ | 64 | 1 | $250.00 | ✅ scoring — ~6.7% of bid side (35,651 resting ≥ 10,000 ✓) ≈ $4.19/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 86.0¢ | 65 | 2 | $250.00 | ✅ scoring — ~4.4% of bid side (10,947 resting ≥ 10,000 ✓) ≈ $2.77/day (pool ÷ 2 markets) |
| `enwc-ussep-mi-2026-08-04-dem-halste` | BUY | 33.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~2.7% of bid side (31,339 resting ≥ 10,000 ✓) ≈ $1.13/day (pool ÷ 3 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 1.0¢ | 10,000 | 32 | $250.00 | ✅ scoring — ~0.0% of bid side (10,082 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 3 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | BUY | 1.0¢ | 10,000 | 45 | $250.00 | ✅ scoring — ~0.0% of bid side (10,156 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 33 markets) |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 1.0¢ | 10,000 | 87 | $250.00 | ✅ scoring — ~0.0% of bid side (10,947 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 99.0¢ | 10,000 | 89 | $250.00 | ✅ scoring — ~0.0% of ask side (10,782 resting ≥ 10,000 ✓) ≈ $0.00/day (pool ÷ 5 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 51.0¢ | 100 | 0 | $250.00 | ❌ side has 5,561 of 10,000 Target Size — side not qualifying |
| `enwc-ussep-mi-2026-08-04-dem-halste` | SELL | 35.0¢ | 100 | 0 | $250.00 | ❌ side has 9,940 of 10,000 Target Size — side not qualifying |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 13.0¢ | 100 | 0 | $250.00 | ❌ side has 5,660 of 10,000 Target Size — side not qualifying |
| `opdc-trump-resig-2026-12-31` | SELL | 20.0¢ | 100 | 0 | — | ❌ no active reward program on this market |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 51.0¢ | 100 | 0 | $250.00 | ❌ side has 5,561 of 10,000 Target Size — side not qualifying |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 99.0¢ | 5,000 | 86 | $250.00 | ❌ side has 5,660 of 10,000 Target Size — side not qualifying |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 99.0¢ | 2,000 | 90 | $250.00 | ❌ outside Target Size window (order 90 ticks from best; window ends 4) |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 1.0¢ | 10,000 | 90 | $250.00 | ❌ outside Target Size window (order 90 ticks from best; window ends 4) |

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (29,734 resting) | ~60.8% | ~$37.99 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (38,445 resting) | ~36.7% | ~$22.92 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (11,971 resting) | ~15.7% | ~$9.81 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (26,168 resting) | ~14.6% | ~$9.14 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (68,785 resting) | ~7.1% | ~$4.43 |
| `cranc-uspres28-12-31-2026-jonoss` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,240 resting) | ~92.6% | ~$3.51 |
| `cranc-uspres28-12-31-2026-krinoe` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,780 resting) | ~90.9% | ~$3.44 |
| `cranc-uspres28-12-31-2026-bersan` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,776 resting) | ~88.9% | ~$3.37 |
| `cranc-uspres28-12-31-2026-elomus` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (12,776 resting) | ~88.9% | ~$3.37 |
| `cranc-uspres28-12-31-2026-hunbid` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,240 resting) | ~88.9% | ~$3.37 |
| `cranc-uspres28-12-31-2026-margre` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,240 resting) | ~88.9% | ~$3.37 |
| `cranc-uspres28-12-31-2026-gavnew` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (31,698 resting) | ~76.0% | ~$2.88 |

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
| 2026-07-19 02:06:16 | ✅ ok | 102 | $112.64 |
| 2026-07-19 00:12:38 | ✅ ok | 83 | $97.93 |
| 2026-07-18 23:14:00 | ✅ ok | 83 | $97.93 |
| 2026-07-18 22:10:04 | ✅ ok | 83 | $97.93 |
| 2026-07-18 21:08:25 | ✅ ok | 83 | $97.93 |
| 2026-07-18 19:35:32 | ✅ ok | 83 | $97.93 |
| 2026-07-18 18:10:35 | ✅ ok | 83 | $97.93 |
| 2026-07-18 17:17:57 | ✅ ok | 83 | $97.93 |
| 2026-07-18 16:38:47 | ✅ ok | 83 | $97.93 |
| 2026-07-18 16:13:22 | ✅ ok | 83 | $97.93 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
