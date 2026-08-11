# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-11 11:05 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$0.00/day estimated (ceiling, not promise — details below)

**Earned:** $1,889.44 lifetime ($1,771.01 paid). Last three recorded days — 2026-08-09: **$62.24** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-08: **$54.78** · 2026-08-07: **$60.33** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `paccc-usse-midterms-2026-11-03-dem` — BUY at the best price, ~$18.92/day for 200 contracts. Runners-up: `paccc-usho-midterms-2026-11-03-rep` (~$16.43/day), `apdc-jerpowgov-2026-12-31` (~$13.07/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$0.00/day (~$0.00/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 90.0¢ | 50 | 0 | $100.00 | ❌ side has 172 of 5,000 Target Size — side not qualifying |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 83.0¢ | 5 | 0 | $100.00 | ❌ side has 90 of 5,000 Target Size — side not qualifying |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 50 @ 90¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 99¢ | 122 | ×0.2^9 = 0.0 |

`side 172 < target 5,000 → side pays nobody`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 5 @ 83¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 83¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 80¢ | 78 | ×0.2^3 = 0.6 |
|  | 49¢ | 7 | ×0.2^34 = 0.0 |

`side 90 < target 5,000 → side pays nobody`  

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-08 | ~$111.62 | $54.78 | 49% |
| 2026-08-07 | ~$116.96 | $60.33 | 52% |
| 2026-08-06 | ~$60.78 | $52.21 | 86% |

Biggest gaps on 2026-08-08: `opdc-mcconnell-resign-2026-11-02` (est ~$9.47 → got $3.79), `scc-hrep-rep-2026-11-03-gte210` (est ~$5.11 → got $0.11), `scc-hrep-rep-2026-11-03-gte185` (est ~$4.26 → got $0.16)

_2026-08-09 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (280,698 resting) | ~25.2% | ~$18.92 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (364,979 resting) | ~21.9% | ~$16.43 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,598 resting) | ~52.3% | ~$13.07 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (35,089 resting) | ~16.3% | ~$12.20 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (25,279 resting) | ~44.4% | ~$11.11 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (25,260 resting) | ~44.4% | ~$11.11 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (42,561 resting) | ~14.8% | ~$11.08 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (49,823 resting) | ~10.6% | ~$7.95 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,974 resting) | ~27.7% | ~$6.93 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (55,562 resting) | ~6.0% | ~$4.52 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (44,510 resting) | ~4.3% | ~$3.25 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (59,128 resting) | ~4.3% | ~$3.20 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,771.01 |
| Pending | $117.02 |
| Skipped | $1.41 |
| **Total earned** | **$1,889.44** |

1818 reward rows · 38 days with rewards · 378 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-09 ⚠️ multi-day pending bucket | $62.24 | `██████████` |
| 2026-08-08 | $54.78 | `█████████` |
| 2026-08-07 | $60.33 | `██████████` |
| 2026-08-06 | $52.21 | `████████` |
| 2026-08-05 | $31.46 | `█████` |
| 2026-08-04 | $53.94 | `█████████` |
| 2026-08-03 | $44.81 | `███████` |
| 2026-08-02 | $14.05 | `██` |
| 2026-08-01 | $52.30 | `████████` |
| 2026-07-31 | $67.96 | `███████████` |
| 2026-07-30 | $20.67 | `███` |
| 2026-07-29 | $53.60 | `█████████` |
| 2026-07-28 | $79.65 | `█████████████` |
| 2026-07-27 | $125.34 | `████████████████████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $426.12 | `██████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $92.91 |
| `apdc-jerpowgov-2026-12-31` | $78.79 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `opdc-mcconnell-resign-2026-11-02` | $56.96 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.95 |
| `scc-hrep-rep-2026-11-03-gte200` | $36.01 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-11 11:05 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 10:35 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 10:30 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 10:27 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 9:47 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 8:02 AM ET | ❌ error | 1818 | $1889.44 |
| 2026-08-11 8:00 AM ET | ❌ error | 1818 | $1889.44 |
| 2026-08-11 7:53 AM ET | ❌ error | 1818 | $1889.44 |
| 2026-08-11 7:10 AM ET | ❌ error | 1818 | $1889.44 |
| 2026-08-11 7:08 AM ET | ❌ error | 1818 | $1889.44 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
