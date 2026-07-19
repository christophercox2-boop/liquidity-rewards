# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 13:34 UTC

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$25.34/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — BUY at the best price, ~$30.77/day for 200 contracts. Runners-up: `enwc-ussep-mi-2026-08-04-dem-abdels` (~$19.87/day), `paccc-usse-midterms-2026-11-03-rep` (~$14.46/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$25.34/day (~$1.06/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 65.0¢ | 50 | 1 | $250.00 | ✅ scoring — ~23.1% of ask side (23,631 resting ≥ 10,000 ✓) ≈ $14.42/day (pool ÷ 2 markets) |
| `paccc-usho-midterms-2026-11-03-dem` | BUY | 84.0¢ | 27 | 1 | $250.00 | ✅ scoring — ~11.3% of bid side (796,985 resting ≥ 10,000 ✓) ≈ $7.08/day (pool ÷ 2 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 51.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~10.7% of ask side (10,972 resting ≥ 10,000 ✓) ≈ $1.34/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 51.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~9.1% of ask side (11,134 resting ≥ 10,000 ✓) ≈ $1.14/day (pool ÷ 10 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | SELL | 25.0¢ | 13 | 1 | $250.00 | ✅ scoring — ~7.6% of ask side (29,319 resting ≥ 10,000 ✓) ≈ $0.29/day (pool ÷ 33 markets) |
| `enwc-ussep-me-2026-07-27-dem-trojac` | BUY | 93.0¢ | 30 | 0 | $250.00 | ✅ scoring — ~6.4% of bid side (15,293 resting ≥ 10,000 ✓) ≈ $0.89/day (pool ÷ 9 markets) |
| `ewc-usgub-ca-2026-11-03-xavbec` | BUY | 95.0¢ | 20 | 0 | $250.00 | ✅ scoring — ~0.3% of bid side (166,505 resting ≥ 10,000 ✓) ≈ $0.16/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 70.0¢ | 30 | 6 | $250.00 | ✅ scoring — ~0.0% of ask side (23,631 resting ≥ 10,000 ✓) ≈ $0.02/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 6.0¢ | 98 | 0 | $250.00 | ❌ side has 416 of 10,000 Target Size — side not qualifying |
| `paccc-usho-midterms-2026-11-03-dem` | SELL | 84.6¢ | 15 | 1 | $250.00 | ❌ outside Target Size window (order 1 tick from best; window ends 58) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | BUY | 9.0¢ | 100 | 3 | $250.00 | ❌ side has 525 of 10,000 Target Size — side not qualifying |

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (34,706 resting) | ~49.2% | ~$30.77 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (20,434 resting) | ~47.7% | ~$19.87 |
| `paccc-usse-midterms-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (767,114 resting) | ~23.1% | ~$14.46 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (26,378 resting) | ~21.5% | ~$13.43 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (26,782 resting) | ~20.1% | ~$12.56 |
| `ewc-usgub-mi-2026-11-03-rep` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (56,762 resting) | ~15.5% | ~$6.47 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (11,000 resting) | ~9.5% | ~$5.96 |
| `ewc-usgub-ks-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (68,548 resting) | ~8.5% | ~$5.28 |
| `ewc-usgub-ga-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (58,122 resting) | ~8.3% | ~$5.21 |
| `ewc-usgub-ga-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (63,100 resting) | ~6.2% | ~$3.84 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (26,385 resting) | ~5.9% | ~$3.66 |
| `ewc-usse-ia-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (64,826 resting) | ~5.7% | ~$3.57 |

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
| 2026-07-19 13:34:33 | ✅ ok | 102 | $112.64 |
| 2026-07-19 13:10:08 | ✅ ok | 102 | $112.64 |
| 2026-07-19 12:08:17 | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:46:58 | ✅ ok | 102 | $112.64 |
| 2026-07-19 09:20:41 | ✅ ok | 102 | $112.64 |
| 2026-07-19 06:45:08 | ✅ ok | 102 | $112.64 |
| 2026-07-19 03:59:31 | ✅ ok | 102 | $112.64 |
| 2026-07-19 02:06:16 | ✅ ok | 102 | $112.64 |
| 2026-07-19 00:12:38 | ✅ ok | 83 | $97.93 |
| 2026-07-18 23:14:00 | ✅ ok | 83 | $97.93 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
