# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 6:11 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$68.29/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mi-2026-08-04-dem-abdels` — BUY at the best price, ~$11.88/day for 200 contracts. Runners-up: `enwc-ussep-me-2026-07-27-dem-trojac` (~$11.35/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$8.70/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$68.29/day (~$2.85/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 5.0¢ | 10 | 0 | $250.00 | ✅ scoring — ~82.7% of ask side (11,577 resting ≥ 10,000 ✓) ≈ $51.70/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 5.0¢ | 93 | 0 | $250.00 | ✅ scoring — ~22.2% of ask side (11,265 resting ≥ 10,000 ✓) ≈ $4.62/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 48.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~11.4% of ask side (15,515 resting ≥ 10,000 ✓) ≈ $1.42/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 49.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~9.2% of ask side (15,978 resting ≥ 10,000 ✓) ≈ $1.15/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 48.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~9.2% of ask side (16,133 resting ≥ 10,000 ✓) ≈ $1.15/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 49.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~7.3% of ask side (16,931 resting ≥ 10,000 ✓) ≈ $0.91/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 21.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~4.4% of ask side (22,130 resting ≥ 10,000 ✓) ≈ $2.78/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 60.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~4.3% of bid side (10,806 resting ≥ 10,000 ✓) ≈ $2.67/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 87.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~2.4% of bid side (38,565 resting ≥ 10,000 ✓) ≈ $1.51/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 11.0¢ | 100 | 6 | $250.00 | ✅ scoring — ~0.6% of ask side (11,577 resting ≥ 10,000 ✓) ≈ $0.38/day (pool ÷ 2 markets) |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-nh-2026-09-08-dem-karman</code> SELL 10 @ 5¢ → $51.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 12 (10 yours) | ×0.3^0 = 12.0 |
|  | 11¢ | 100 | ×0.3^6 = 0.1 |
|  | 13¢ | 250 | ×0.3^8 = 0.0 |
|  | 99¢ | 11,215 | ×0.3^94 = 0.0 |
| | | **Σ** | **12.1** |

`yours 10.0 / Σ 12.1 = 82.7%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 82.7% = $51.70/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap`
2. `enwc-ussep-nh-2026-09-08-dem-karman` ← this one

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> SELL 93 @ 5¢ → $4.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 418 (93 yours) | ×0.3^0 = 418.0 |
|  | 7¢ | 12 | ×0.3^2 = 1.1 |
|  | 30¢ | 250 | ×0.3^25 = 0.0 |
|  | 99¢ | 10,585 | ×0.3^94 = 0.0 |
| | | **Σ** | **419.1** |

`yours 93.0 / Σ 419.1 = 22.2%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 22.2% = $4.62/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 100 @ 48¢ → $1.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 881 (100 yours) | ×0.3^0 = 881.0 |
|  | 99¢ | 14,634 | ×0.3^51 = 0.0 |
| | | **Σ** | **881.0** |

`yours 100.0 / Σ 881.0 = 11.4%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 11.4% = $1.42/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 100 @ 49¢ → $1.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 906 (100 yours) | ×0.3^0 = 906.0 |
|  | 50¢ | 588 | ×0.3^1 = 176.4 |
|  | 99¢ | 14,484 | ×0.3^50 = 0.0 |
| | | **Σ** | **1,082.4** |

`yours 100.0 / Σ 1,082.4 = 9.2%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 9.2% = $1.15/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 100 @ 48¢ → $1.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 909 (100 yours) | ×0.3^0 = 909.0 |
|  | 49¢ | 590 | ×0.3^1 = 177.0 |
|  | 99¢ | 14,634 | ×0.3^51 = 0.0 |
| | | **Σ** | **1,086.0** |

`yours 100.0 / Σ 1,086.0 = 9.2%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 9.2% = $1.15/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 100 @ 49¢ → $0.91/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 920 (100 yours) | ×0.3^0 = 920.0 |
|  | 50¢ | 1,527 | ×0.3^1 = 458.1 |
|  | 99¢ | 14,484 | ×0.3^50 = 0.0 |
| | | **Σ** | **1,378.1** |

`yours 100.0 / Σ 1,378.1 = 7.3%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 7.3% = $0.91/day`  

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
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 100 @ 21¢ → $2.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 150 (100 yours) | ×0.3^0 = 150.0 |
|  | 22¢ | 1,010 | ×0.3^1 = 303.0 |
|  | 23¢ | 19,969 | ×0.3^2 = 1,797.2 |
| | | **Σ** | **2,250.2** |

`yours 100.0 / Σ 2,250.2 = 4.4%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 4.4% = $2.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun`
2. `enwc-ussep-nh-2026-09-01-rep-scobro` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-chrpap</code> BUY 100 @ 60¢ → $2.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 61¢ | 622 | ×0.3^0 = 622.0 |
| ▶ | 60¢ | 264 (100 yours) | ×0.3^1 = 79.2 |
|  | 1¢ | 9,920 | ×0.3^60 = 0.0 |
| | | **Σ** | **701.2** |

`yours 30.0 / Σ 701.2 = 4.3%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 4.3% = $2.67/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap` ← this one
2. `enwc-ussep-nh-2026-09-08-dem-karman`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-johsun</code> BUY 100 @ 87¢ → $1.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 714 (100 yours) | ×0.3^0 = 714.0 |
|  | 86¢ | 147 | ×0.3^1 = 44.1 |
|  | 85¢ | 37,604 | ×0.3^2 = 3,384.4 |
| | | **Σ** | **4,142.5** |

`yours 100.0 / Σ 4,142.5 = 2.4%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 2.4% = $1.51/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun` ← this one
2. `enwc-ussep-nh-2026-09-01-rep-scobro`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-karman</code> SELL 100 @ 11¢ → $0.38/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 12 | ×0.3^0 = 12.0 |
| ▶ | 11¢ | 100 (100 yours) | ×0.3^6 = 0.1 |
|  | 13¢ | 250 | ×0.3^8 = 0.0 |
|  | 99¢ | 11,215 | ×0.3^94 = 0.0 |
| | | **Σ** | **12.1** |

`yours 0.1 / Σ 12.1 = 0.6%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.6% = $0.38/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap`
2. `enwc-ussep-nh-2026-09-08-dem-karman` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (11,689 resting) | ~28.5% | ~$11.88 |
| `enwc-ussep-me-2026-07-27-dem-trojac` | $250.00 ÷ 9 | 0.30 | 10,000 | BUY side (15,068 resting) | ~81.7% | ~$11.35 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (27,854 resting) | ~13.9% | ~$8.70 |
| `ewc-usgub-ga-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (58,494 resting) | ~11.6% | ~$7.24 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $250.00 ÷ 9 | 0.30 | 10,000 | SELL side (31,784 resting) | ~41.4% | ~$5.75 |
| `ewc-usgub-mi-2026-11-03-rep` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (58,580 resting) | ~10.8% | ~$4.49 |
| `ewc-usgub-ia-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (64,300 resting) | ~5.3% | ~$3.28 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (57,132 resting) | ~5.1% | ~$3.16 |
| `ewc-usgub-ia-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (70,639 resting) | ~4.4% | ~$2.77 |
| `enwc-ussep-me-2026-07-27-dem-shebel` | $250.00 ÷ 9 | 0.30 | 10,000 | SELL side (12,113 resting) | ~17.2% | ~$2.38 |
| `ewc-usgub-ga-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (84,102 resting) | ~3.7% | ~$2.29 |
| `ewc-usgub-ks-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (82,073 resting) | ~3.5% | ~$2.18 |

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
| 2026-07-19 6:11 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 6:10 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 5:10 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 3:36 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 3:22 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 2:47 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 2:16 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:57 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:53 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:27 PM ET | ✅ ok | 102 | $112.64 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
