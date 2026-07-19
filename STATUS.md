# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 7:14 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$47.00/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-me-2026-07-27-dem-trojac` — BUY at the best price, ~$9.86/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$8.72/day), `enwc-ussep-me-2026-07-27-dem-nirsha` (~$7.24/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$47.00/day (~$1.96/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-nh-2026-09-08-dem-karman` | SELL | 11.0¢ | 68 | 0 | $250.00 | ✅ scoring — ~60.4% of ask side (10,588 resting ≥ 10,000 ✓) ≈ $37.72/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 5.0¢ | 93 | 0 | $250.00 | ✅ scoring — ~22.4% of ask side (11,250 resting ≥ 10,000 ✓) ≈ $4.67/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 48.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~10.8% of ask side (15,587 resting ≥ 10,000 ✓) ≈ $1.35/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 49.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~3.9% of ask side (15,469 resting ≥ 10,000 ✓) ≈ $0.49/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 48.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~3.4% of ask side (16,008 resting ≥ 10,000 ✓) ≈ $0.43/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 49.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~2.9% of ask side (16,445 resting ≥ 10,000 ✓) ≈ $0.36/day (pool ÷ 10 markets) |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | BUY | 87.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~2.2% of bid side (40,266 resting ≥ 10,000 ✓) ≈ $1.35/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 21.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~0.6% of ask side (39,851 resting ≥ 10,000 ✓) ≈ $0.40/day (pool ÷ 2 markets) |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | BUY | 60.0¢ | 100 | 3 | $250.00 | ✅ scoring — ~0.4% of bid side (12,193 resting ≥ 10,000 ✓) ≈ $0.22/day (pool ÷ 2 markets) |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-nh-2026-09-08-dem-karman</code> SELL 68 @ 11¢ → $37.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 68 (68 yours) | ×0.3^0 = 67.5 |
|  | 13¢ | 493 | ×0.3^2 = 44.4 |
|  | 55¢ | 87 | ×0.3^44 = 0.0 |
|  | 99¢ | 9,940 | ×0.3^88 = 0.0 |
| | | **Σ** | **111.9** |

`yours 67.5 / Σ 111.9 = 60.4%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 60.4% = $37.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap`
2. `enwc-ussep-nh-2026-09-08-dem-karman` ← this one

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> SELL 93 @ 5¢ → $4.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 415 (93 yours) | ×0.3^0 = 415.0 |
|  | 30¢ | 250 | ×0.3^25 = 0.0 |
|  | 99¢ | 10,585 | ×0.3^94 = 0.0 |
| | | **Σ** | **415.0** |

`yours 93.0 / Σ 415.0 = 22.4%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 22.4% = $4.67/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 100 @ 48¢ → $1.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 925 (100 yours) | ×0.3^0 = 925.0 |
|  | 56¢ | 28 | ×0.3^8 = 0.0 |
|  | 99¢ | 14,634 | ×0.3^51 = 0.0 |
| | | **Σ** | **925.0** |

`yours 100.0 / Σ 925.0 = 10.8%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 10.8% = $1.35/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 100 @ 49¢ → $0.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 48¢ | 735 | ×0.3^0 = 735.0 |
| ▶ | 49¢ | 100 (100 yours) | ×0.3^1 = 30.0 |
|  | 99¢ | 14,634 | ×0.3^51 = 0.0 |
| | | **Σ** | **765.0** |

`yours 30.0 / Σ 765.0 = 3.9%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 3.9% = $0.49/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 100 @ 48¢ → $0.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 47¢ | 663 | ×0.3^0 = 663.0 |
| ▶ | 48¢ | 711 (100 yours) | ×0.3^1 = 213.3 |
|  | 99¢ | 14,634 | ×0.3^52 = 0.0 |
| | | **Σ** | **876.3** |

`yours 30.0 / Σ 876.3 = 3.4%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 3.4% = $0.43/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 100 @ 49¢ → $0.36/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 48¢ | 696 | ×0.3^0 = 696.0 |
| ▶ | 49¢ | 1,115 (100 yours) | ×0.3^1 = 334.5 |
|  | 99¢ | 14,634 | ×0.3^51 = 0.0 |
| | | **Σ** | **1,030.5** |

`yours 30.0 / Σ 1,030.5 = 2.9%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 2.9% = $0.36/day`  

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
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-johsun</code> BUY 100 @ 87¢ → $1.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 1,078 (100 yours) | ×0.3^0 = 1,078.0 |
|  | 86¢ | 147 | ×0.3^1 = 44.1 |
|  | 85¢ | 38,941 | ×0.3^2 = 3,504.7 |
| | | **Σ** | **4,626.8** |

`yours 100.0 / Σ 4,626.8 = 2.2%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 2.2% = $1.35/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun` ← this one
2. `enwc-ussep-nh-2026-09-01-rep-scobro`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 100 @ 21¢ → $0.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 1,259 | ×0.3^0 = 1,259.0 |
| ▶ | 21¢ | 266 (100 yours) | ×0.3^1 = 79.8 |
|  | 22¢ | 37,825 | ×0.3^2 = 3,404.2 |
| | | **Σ** | **4,743.1** |

`yours 30.0 / Σ 4,743.1 = 0.6%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.6% = $0.40/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun`
2. `enwc-ussep-nh-2026-09-01-rep-scobro` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-08-dem-chrpap</code> BUY 100 @ 60¢ → $0.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 63¢ | 513 | ×0.3^0 = 513.0 |
|  | 62¢ | 767 | ×0.3^1 = 230.1 |
| ▶ | 60¢ | 263 (100 yours) | ×0.3^3 = 7.1 |
|  | 1¢ | 10,650 | ×0.3^62 = 0.0 |
| | | **Σ** | **750.2** |

`yours 2.7 / Σ 750.2 = 0.4%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 0.4% = $0.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-08-dem-chrpap` ← this one
2. `enwc-ussep-nh-2026-09-08-dem-karman`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-me-2026-07-27-dem-trojac` | $250.00 ÷ 9 | 0.30 | 10,000 | BUY side (15,032 resting) | ~71.0% | ~$9.86 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (27,839 resting) | ~14.0% | ~$8.72 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $250.00 ÷ 9 | 0.30 | 10,000 | SELL side (46,113 resting) | ~52.2% | ~$7.24 |
| `ewc-usgub-ga-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (58,494 resting) | ~11.6% | ~$7.24 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (20,478 resting) | ~8.4% | ~$3.50 |
| `ewc-usgub-ia-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (64,967 resting) | ~5.5% | ~$3.44 |
| `ewc-usgub-mi-2026-11-03-rep` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (59,273 resting) | ~7.8% | ~$3.25 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (56,901 resting) | ~5.1% | ~$3.19 |
| `ewc-usgub-ks-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (80,814 resting) | ~4.7% | ~$2.92 |
| `enwc-ussep-me-2026-07-27-dem-shebel` | $250.00 ÷ 9 | 0.30 | 10,000 | SELL side (11,482 resting) | ~20.4% | ~$2.83 |
| `ewc-usgub-ga-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (83,576 resting) | ~4.0% | ~$2.53 |
| `ewc-usgub-ia-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (71,247 resting) | ~3.8% | ~$2.39 |

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
| 2026-07-19 7:14 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 6:11 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 6:10 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 5:10 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 3:36 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 3:22 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 2:47 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 2:16 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:57 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:53 PM ET | ✅ ok | 102 | $112.64 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
