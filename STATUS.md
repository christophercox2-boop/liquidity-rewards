# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-22 6:18 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$21.34/day estimated (ceiling, not promise — details below)

**Earned:** $299.40 lifetime ($155.84 paid). Last three recorded days — 2026-07-20: **$106.54** · 2026-07-19: **$35.81** · 2026-07-18: **$44.41** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — BUY at the best price, ~$39.39/day for 200 contracts. Runners-up: `enwc-ussep-mi-2026-08-04-dem-halste` (~$26.28/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$21.99/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$21.34/day (~$0.89/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~49.3% of bid side (20,275 resting ≥ 10,000 ✓) ≈ $10.28/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~29.5% of bid side (33,866 resting ≥ 10,000 ✓) ≈ $6.15/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 8.0¢ | 200 | 0 | $250.00 | ✅ scoring — ~12.4% of bid side (54,943 resting ≥ 10,000 ✓) ≈ $2.58/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 73.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~9.2% of bid side (25,180 resting ≥ 10,000 ✓) ≈ $1.92/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 5.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~2.0% of bid side (33,027 resting ≥ 10,000 ✓) ≈ $0.41/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | BUY | 1.0¢ | 10,000 | 5 | $250.00 | ❌ outside Target Size window (order 5 ticks from best; window ends 2) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 1.0¢ | 10,000 | 7 | $250.00 | ❌ outside Target Size window (order 7 ticks from best; window ends 3) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 1.0¢ | 10,000 | 72 | $250.00 | ❌ outside Target Size window (order 72 ticks from best; window ends 3) |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-joebre</code> BUY 10,000 @ 1¢ → $10.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 20,275 (10,000 yours) | ×0.3^0 = 20,275.0 |
| | | **Σ** | **20,275.0** |

`yours 10,000.0 / Σ 20,275.0 = 49.3%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 49.3% = $10.28/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre` ← this one
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-kelroy</code> BUY 10,000 @ 1¢ → $6.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 33,866 (10,000 yours) | ×0.3^0 = 33,866.0 |
| | | **Σ** | **33,866.0** |

`yours 10,000.0 / Σ 33,866.0 = 29.5%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 29.5% = $6.15/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy` ← this one
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 200 @ 8¢ → $2.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 377 (200 yours) | ×0.3^0 = 377.0 |
|  | 6¢ | 525 | ×0.3^2 = 47.2 |
|  | 5¢ | 44,041 | ×0.3^3 = 1,189.1 |
| | | **Σ** | **1,613.4** |

`yours 200.0 / Σ 1,613.4 = 12.4%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 12.4% = $2.58/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-frahon</code> BUY 50 @ 73¢ → $1.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 73¢ | 100 (50 yours) | ×0.3^0 = 100.0 |
|  | 71¢ | 688 | ×0.3^2 = 61.9 |
|  | 70¢ | 14,142 | ×0.3^3 = 381.8 |
| | | **Σ** | **543.8** |

`yours 50.0 / Σ 543.8 = 9.2%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 9.2% = $1.92/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon` ← this one
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> BUY 100 @ 5¢ → $0.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 200 | ×0.3^0 = 200.0 |
| ▶ | 5¢ | 747 (100 yours) | ×0.3^1 = 224.1 |
|  | 4¢ | 12,080 | ×0.3^2 = 1,087.2 |
| | | **Σ** | **1,511.3** |

`yours 30.0 / Σ 1,511.3 = 2.0%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 2.0% = $0.41/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> BUY 10,000 @ 1¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 200 | ×0.3^0 = 200.0 |
|  | 5¢ | 747 | ×0.3^1 = 224.1 |
|  | 4¢ | 12,080 | ×0.3^2 = 1,087.2 |
| | | **Σ** | **1,511.3** |

`you 5t from best, window ends 2t → score 0`  

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 10,000 @ 1¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 377 | ×0.3^0 = 377.0 |
|  | 6¢ | 525 | ×0.3^2 = 47.2 |
|  | 5¢ | 44,041 | ×0.3^3 = 1,189.1 |
| | | **Σ** | **1,613.4** |

`you 7t from best, window ends 3t → score 0`  

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-frahon</code> BUY 10,000 @ 1¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 73¢ | 100 | ×0.3^0 = 100.0 |
|  | 71¢ | 688 | ×0.3^2 = 61.9 |
|  | 70¢ | 14,142 | ×0.3^3 = 381.8 |
| | | **Σ** | **543.8** |

`you 72t from best, window ends 3t → score 0`  

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-20 | ~$125.00 | $106.54 | 85% |
| 2026-07-19 | ~$36.97 | $35.81 | 97% |

Biggest gaps on 2026-07-20: `enwc-usgubp-wi-2026-08-11-dem-davcro` (est ~$21.74 → got $16.08), `enwc-ussep-nh-2026-09-01-rep-scobro` (est ~$11.93 → got $8.30), `enwc-usgubp-ok-2026-06-16-rep-gendru` (est ~$4.33 → got $2.14)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (34,689 resting) | ~63.0% | ~$39.39 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $250.00 ÷ 3 | 0.30 | 10,000 | SELL side (34,890 resting) | ~63.1% | ~$26.28 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (34,071 resting) | ~35.2% | ~$21.99 |
| `ewc-usgub-mi-2026-11-03-rep` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (41,282 resting) | ~46.7% | ~$19.44 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (83,028 resting) | ~23.6% | ~$14.75 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (21,273 resting) | ~19.7% | ~$12.28 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (171,125 resting) | ~28.5% | ~$11.87 |
| `ewc-usgub-ks-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (161,689 resting) | ~18.8% | ~$11.75 |
| `ewc-usgub-ga-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (78,461 resting) | ~12.3% | ~$7.68 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (83,667 resting) | ~8.5% | ~$5.31 |
| `ewc-usgub-ga-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (77,952 resting) | ~6.9% | ~$4.29 |
| `ewc-usgub-ks-2026-11-03-rep` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (171,405 resting) | ~6.2% | ~$3.89 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $142.35 |
| Skipped | $1.21 |
| **Total earned** | **$299.40** |

186 reward rows · 18 days with rewards · 69 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-20 | $106.54 | `████████████████████` |
| 2026-07-19 | $35.81 | `███████` |
| 2026-07-18 | $44.41 | `████████` |
| 2026-07-17 | $14.71 | `███` |
| 2026-07-16 | $17.02 | `███` |
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `██` |
| 2026-07-13 | $10.03 | `██` |
| 2026-07-12 | $39.90 | `███████` |
| 2026-07-11 | $2.11 | `█` |
| 2026-07-10 | $2.16 | `█` |
| 2026-07-09 | $4.72 | `█` |
| 2026-07-08 | $2.68 | `█` |
| 2026-07-07 | $0.14 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $299.40 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.30 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $39.46 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $21.33 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $17.96 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.56 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $16.08 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $14.86 |
| `apdc-jerpowgov-2026-12-31` | $14.76 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $13.59 |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | $13.18 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $7.79 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $6.57 |
| `paccc-usse-midterms-2026-11-03-rep` | $6.29 |
| `enwc-ussep-me-2026-07-27-dem-jargol` | $4.80 |
| `ewc-usgub-ca-2026-11-03-stehil` | $4.70 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-22 6:18 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 4:34 PM ET | ❌ error | 186 | $299.40 |
| 2026-07-22 2:36 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 12:51 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 10:28 AM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 8:07 AM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 5:41 AM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 2:44 AM ET | ✅ ok | 186 | $299.40 |
| 2026-07-21 11:51 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-21 9:16 PM ET | ✅ ok | 186 | $299.40 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
