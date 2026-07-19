# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 5:10 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$6.67/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$9.70/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$8.71/day), `enwc-ussep-me-2026-07-27-dem-trojac` (~$5.81/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$6.67/day (~$0.28/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 6.0¢ | 98 | 0 | $250.00 | ✅ scoring — ~22.7% of ask side (11,275 resting ≥ 10,000 ✓) ≈ $4.72/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 50.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~4.1% of ask side (11,394 resting ≥ 10,000 ✓) ≈ $0.51/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 49.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~4.1% of ask side (11,597 resting ≥ 10,000 ✓) ≈ $0.51/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 50.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~4.0% of ask side (11,452 resting ≥ 10,000 ✓) ≈ $0.50/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 49.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~3.5% of ask side (11,968 resting ≥ 10,000 ✓) ≈ $0.43/day (pool ÷ 10 markets) |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> SELL 98 @ 6¢ → $4.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 429 (98 yours) | ×0.3^0 = 429.0 |
|  | 7¢ | 11 | ×0.3^1 = 3.3 |
|  | 30¢ | 250 | ×0.3^24 = 0.0 |
|  | 99¢ | 10,585 | ×0.3^93 = 0.0 |
| | | **Σ** | **432.3** |

`yours 98.0 / Σ 432.3 = 22.7%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 22.7% = $4.72/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 100 @ 50¢ → $0.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 49¢ | 658 | ×0.3^0 = 658.0 |
| ▶ | 50¢ | 264 (100 yours) | ×0.3^1 = 79.2 |
|  | 99¢ | 10,472 | ×0.3^50 = 0.0 |
| | | **Σ** | **737.2** |

`yours 30.0 / Σ 737.2 = 4.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 4.1% = $0.51/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 100 @ 49¢ → $0.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 48¢ | 640 | ×0.3^0 = 640.0 |
| ▶ | 49¢ | 335 (100 yours) | ×0.3^1 = 100.5 |
|  | 99¢ | 10,622 | ×0.3^51 = 0.0 |
| | | **Σ** | **740.5** |

`yours 30.0 / Σ 740.5 = 4.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 4.1% = $0.51/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20` ← this one
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 100 @ 50¢ → $0.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 49¢ | 662 | ×0.3^0 = 662.0 |
| ▶ | 50¢ | 318 (100 yours) | ×0.3^1 = 95.4 |
|  | 99¢ | 10,472 | ×0.3^50 = 0.0 |
| | | **Σ** | **757.4** |

`yours 30.0 / Σ 757.4 = 4.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 4.0% = $0.50/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20` ← this one
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 100 @ 49¢ → $0.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 48¢ | 657 | ×0.3^0 = 657.0 |
| ▶ | 49¢ | 689 (100 yours) | ×0.3^1 = 206.7 |
|  | 99¢ | 10,622 | ×0.3^51 = 0.0 |
| | | **Σ** | **863.7** |

`yours 30.0 / Σ 863.7 = 3.5%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 3.5% = $0.43/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20` ← this one
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (58,494 resting) | ~15.5% | ~$9.70 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (27,846 resting) | ~13.9% | ~$8.71 |
| `enwc-ussep-me-2026-07-27-dem-trojac` | $250.00 ÷ 9 | 0.30 | 10,000 | BUY side (15,420 resting) | ~41.8% | ~$5.81 |
| `ewc-usgub-ia-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (69,748 resting) | ~8.6% | ~$5.40 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (71,624 resting) | ~7.8% | ~$4.90 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $250.00 ÷ 9 | 0.30 | 10,000 | SELL side (36,908 resting) | ~33.2% | ~$4.61 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (56,911 resting) | ~5.1% | ~$3.18 |
| `ewc-usgub-mi-2026-11-03-rep` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (59,367 resting) | ~7.6% | ~$3.15 |
| `ewc-usgub-ks-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (81,506 resting) | ~3.9% | ~$2.44 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (68,413 resting) | ~3.7% | ~$2.30 |
| `enwc-ussep-me-2026-07-27-dem-shebel` | $250.00 ÷ 9 | 0.30 | 10,000 | SELL side (12,160 resting) | ~16.5% | ~$2.29 |
| `ewc-usgub-ga-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (84,576 resting) | ~3.4% | ~$2.10 |

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
| 2026-07-19 5:10 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 3:36 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 3:22 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 2:47 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 2:16 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:57 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:53 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:27 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 12:14 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 11:18 AM ET | ✅ ok | 102 | $112.64 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
