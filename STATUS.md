# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 10:09 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$16.29/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mi-2026-08-04-dem-abdels` — BUY at the best price, ~$19.87/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$16.82/day), `enwc-usgubp-sd-2026-06-02-rep-tobdoe` (~$12.56/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$16.29/day (~$0.68/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `cranc-uspres28-12-31-2026-jdvan` | SELL | 15.0¢ | 13 | 0 | $250.00 | ✅ scoring — ~97.1% of ask side (26,823 resting ≥ 10,000 ✓) ≈ $3.68/day (pool ÷ 33 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 6.0¢ | 98 | 0 | $250.00 | ✅ scoring — ~25.4% of ask side (11,000 resting ≥ 10,000 ✓) ≈ $6.34/day (pool ÷ 5 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 51.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~10.7% of ask side (10,972 resting ≥ 10,000 ✓) ≈ $1.34/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 51.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~9.1% of ask side (11,134 resting ≥ 10,000 ✓) ≈ $1.14/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 25.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~6.1% of ask side (24,218 resting ≥ 10,000 ✓) ≈ $3.79/day (pool ÷ 2 markets) |

**Tap any order below to see the math behind its number:**

<details><summary><code>cranc-uspres28-12-31-2026-jdvan</code> SELL 13 @ 15.0¢ — ✅ scoring — ~97.1% of ask side (26,823 resting ≥ 10,000 ✓) ≈</summary>

- Your order: SELL 13 @ 15.0¢. Best ask: 15.0¢ (tick = 1¢) → you are 0 ticks from best.
- Target Size check: ask side holds 26,823 resting ≥ 10,000 required ✓
- Window walk: from best outward until 10,000 contracts accumulate — ends 84 ticks out. Levels: 15.0¢×13 · 19.0¢×48 · 50.0¢×90 · 58.0¢×114 · 95.0¢×875 · 96.0¢×684 · …1 more levels
- Your score = DiscountFactor^ticks × size = 0.3^0 × 13 = 13.1
- Whole ask-side score = Σ (level size × 0.3^ticks) over the window = 13.5
- Your share = 13.1 / 13.5 = 97.1% of the ask side
- Pool: $250.00/day ÷ 33 markets in this race ÷ 2 sides = $3.79/day for this side
- Estimate = 97.1% × $3.79 = $3.68/day

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> SELL 98 @ 6.0¢ — ✅ scoring — ~25.4% of ask side (11,000 resting ≥ 10,000 ✓) ≈</summary>

- Your order: SELL 98 @ 6.0¢. Best ask: 6.0¢ (tick = 1¢) → you are 0 ticks from best.
- Target Size check: ask side holds 11,000 resting ≥ 10,000 required ✓
- Window walk: from best outward until 10,000 contracts accumulate — ends 93 ticks out. Levels: 6.0¢×385 · 7.0¢×5 · 14.0¢×25 · 99.0¢×10,585
- Your score = DiscountFactor^ticks × size = 0.3^0 × 98 = 98.0
- Whole ask-side score = Σ (level size × 0.3^ticks) over the window = 386.5
- Your share = 98.0 / 386.5 = 25.4% of the ask side
- Pool: $250.00/day ÷ 5 markets in this race ÷ 2 sides = $25.00/day for this side
- Estimate = 25.4% × $25.00 = $6.34/day

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 100 @ 51.0¢ — ✅ scoring — ~10.7% of ask side (10,972 resting ≥ 10,000 ✓) ≈</summary>

- Your order: SELL 100 @ 51.0¢. Best ask: 50.0¢ (tick = 1¢) → you are 1 tick from best.
- Target Size check: ask side holds 10,972 resting ≥ 10,000 required ✓
- Window walk: from best outward until 10,000 contracts accumulate — ends 49 ticks out. Levels: 50.0¢×250 · 51.0¢×100 · 99.0¢×10,622
- Your score = DiscountFactor^ticks × size = 0.3^1 × 100 = 30.0
- Whole ask-side score = Σ (level size × 0.3^ticks) over the window = 280.0
- Your share = 30.0 / 280.0 = 10.7% of the ask side
- Pool: $250.00/day ÷ 10 markets in this race ÷ 2 sides = $12.50/day for this side
- Estimate = 10.7% × $12.50 = $1.34/day

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 100 @ 51.0¢ — ✅ scoring — ~9.1% of ask side (11,134 resting ≥ 10,000 ✓) ≈ </summary>

- Your order: SELL 100 @ 51.0¢. Best ask: 50.0¢ (tick = 1¢) → you are 1 tick from best.
- Target Size check: ask side holds 11,134 resting ≥ 10,000 required ✓
- Window walk: from best outward until 10,000 contracts accumulate — ends 49 ticks out. Levels: 50.0¢×250 · 51.0¢×262 · 99.0¢×10,622
- Your score = DiscountFactor^ticks × size = 0.3^1 × 100 = 30.0
- Whole ask-side score = Σ (level size × 0.3^ticks) over the window = 328.6
- Your share = 30.0 / 328.6 = 9.1% of the ask side
- Pool: $250.00/day ÷ 10 markets in this race ÷ 2 sides = $12.50/day for this side
- Estimate = 9.1% × $12.50 = $1.14/day

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 100 @ 25.0¢ — ✅ scoring — ~6.1% of ask side (24,218 resting ≥ 10,000 ✓) ≈ </summary>

- Your order: SELL 100 @ 25.0¢. Best ask: 24.0¢ (tick = 1¢) → you are 1 tick from best.
- Target Size check: ask side holds 24,218 resting ≥ 10,000 required ✓
- Window walk: from best outward until 10,000 contracts accumulate — ends 69 ticks out. Levels: 24.0¢×400 · 25.0¢×317 · 93.0¢×23,500
- Your score = DiscountFactor^ticks × size = 0.3^1 × 100 = 30.0
- Whole ask-side score = Σ (level size × 0.3^ticks) over the window = 495.1
- Your share = 30.0 / 495.1 = 6.1% of the ask side
- Pool: $250.00/day ÷ 2 markets in this race ÷ 2 sides = $62.50/day for this side
- Estimate = 6.1% × $62.50 = $3.79/day

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (20,434 resting) | ~47.7% | ~$19.87 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (26,630 resting) | ~26.9% | ~$16.82 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (26,782 resting) | ~20.1% | ~$12.56 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (35,420 resting) | ~17.9% | ~$11.16 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (11,000 resting) | ~9.5% | ~$5.96 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (26,385 resting) | ~5.9% | ~$3.66 |
| `cranc-uspres28-12-31-2026-kamhar` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (17,014 resting) | ~94.8% | ~$3.59 |
| `cranc-uspres28-12-31-2026-krinoe` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (21,600 resting) | ~90.9% | ~$3.44 |
| `cranc-uspres28-12-31-2026-andyan` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (21,240 resting) | ~90.1% | ~$3.41 |
| `cranc-uspres28-12-31-2026-hunbid` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (21,000 resting) | ~88.9% | ~$3.37 |
| `cranc-uspres28-12-31-2026-gavnew` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (25,464 resting) | ~73.8% | ~$2.79 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (72,326 resting) | ~6.6% | ~$2.75 |

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

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-19 10:09 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:56 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:47 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:34 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 9:10 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 8:08 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 6:46 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 5:20 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 2:45 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-18 11:59 PM ET | ✅ ok | 102 | $112.64 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
