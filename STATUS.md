# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 2:47 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$4.69/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$9.29/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$9.26/day), `enwc-ussep-mn-2026-08-11-dem-angcra` (~$5.39/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$4.69/day (~$0.20/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 6.0¢ | 98 | 0 | $250.00 | ✅ scoring — ~22.5% of ask side (11,279 resting ≥ 10,000 ✓) ≈ $4.69/day (pool ÷ 6 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 25.0¢ | 100 | 3 | $250.00 | ❌ outside Target Size window (order 3 ticks from best; window ends 2) |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> SELL 98 @ 6¢ → $4.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 431 (98 yours) | ×0.3^0 = 431.0 |
|  | 7¢ | 13 | ×0.3^1 = 3.9 |
|  | 30¢ | 250 | ×0.3^24 = 0.0 |
|  | 99¢ | 10,585 | ×0.3^93 = 0.0 |
| | | **Σ** | **434.9** |

`yours 98.0 / Σ 434.9 = 22.5%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 22.5% = $4.69/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 100 @ 25¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 22¢ | 477 | ×0.3^0 = 477.0 |
|  | 24¢ | 29,008 | ×0.3^2 = 2,610.7 |
| | | **Σ** | **3,087.7** |

`you 3t from best, window ends 2t → score 0`  

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (27,645 resting) | ~14.9% | ~$9.29 |
| `ewc-usgub-ga-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (58,572 resting) | ~14.8% | ~$9.26 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (59,565 resting) | ~8.6% | ~$5.39 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (97,279 resting) | ~6.9% | ~$4.32 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $250.00 ÷ 9 | 0.30 | 10,000 | SELL side (35,950 resting) | ~31.0% | ~$4.30 |
| `ewc-usgub-ga-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (64,448 resting) | ~5.8% | ~$3.62 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (57,371 resting) | ~5.2% | ~$3.27 |
| `ewc-usgub-mi-2026-11-03-rep` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (58,948 resting) | ~7.5% | ~$3.13 |
| `enwc-ussep-me-2026-07-27-dem-trojac` | $250.00 ÷ 9 | 0.30 | 10,000 | BUY side (15,360 resting) | ~19.5% | ~$2.71 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (30,432 resting) | ~6.1% | ~$2.56 |
| `ewc-usgub-ia-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (72,254 resting) | ~4.0% | ~$2.49 |
| `ewc-usgub-ks-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (81,685 resting) | ~3.8% | ~$2.36 |

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
| 2026-07-19 2:47 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 2:16 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:57 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:53 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:27 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 12:14 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 11:18 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:50 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:43 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:09 AM ET | ✅ ok | 102 | $112.64 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
