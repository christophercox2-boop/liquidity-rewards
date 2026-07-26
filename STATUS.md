# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-25 10:06 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$14.65/day estimated (ceiling, not promise — details below)

**Earned:** $836.61 lifetime ($155.84 paid). Last three recorded days — 2026-07-24: **$135.19** · 2026-07-23: **$227.63** · 2026-07-22: **$82.95** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — BUY at the best price, ~$11.99/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-angcra` (~$8.73/day), `ewc-usgub-ia-2026-11-03-rep` (~$4.85/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$14.65/day (~$0.61/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 20.0¢ | 86 | 0 | $100.00 | ✅ scoring — ~67.1% of ask side (2,312 resting ≥ 2,000 ✓) ≈ $2.80/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 10.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (103,681 resting ≥ 2,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 5.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~65.8% of ask side (39,524 resting ≥ 2,000 ✓) ≈ $3.29/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 17.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~64.9% of ask side (63,832 resting ≥ 2,000 ✓) ≈ $3.24/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | SELL | 30.0¢ | 300 | 1 | $100.00 | ✅ scoring — ~56.4% of ask side (2,500 resting ≥ 2,000 ✓) ≈ $2.35/day (pool ÷ 12 markets) |
| `enwc-usgubp-mn-2026-08-11-rep-kenqua` | BUY | 1.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~1.7% of bid side (5,874 resting ≥ 2,000 ✓) ≈ $0.28/day (pool ÷ 3 markets) |
| `ewc-usgub-ca-2026-11-03-stehil` | BUY | 5.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~0.5% of bid side (176,614 resting ≥ 2,000 ✓) ≈ $0.12/day (pool ÷ 2 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 1.0¢ | 400 | 0 | $100.00 | ❌ side has 1,715 of 2,000 Target Size — side not qualifying |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 86 @ 20¢ → $2.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 128 (86 yours) | ×0.5^0 = 127.7 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 55¢ | 44 | ×0.5^35 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 25 | ×0.5^54 = 0.0 |
|  | 99¢ | 1,885 | ×0.5^79 = 0.0 |
| | | **Σ** | **127.7** |

`yours 85.7 / Σ 127.7 = 67.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 67.1% = $2.80/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor` ← this one
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 100 @ 10¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 150 (100 yours) | ×0.5^0 = 150.0 |
|  | 50¢ | 100 | ×0.5^40 = 0.0 |
|  | 55¢ | 44 | ×0.5^45 = 0.0 |
|  | 97¢ | 53,892 | ×0.5^87 = 0.0 |
| | | **Σ** | **150.0** |

`yours 100.0 / Σ 150.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48` ← this one
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 5¢ → $3.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 2 (1 yours) | ×0.5^0 = 1.5 |
|  | 43¢ | 2,000 | ×0.5^38 = 0.0 |
| | | **Σ** | **1.5** |

`yours 1.0 / Σ 1.5 = 65.8%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 65.8% = $3.29/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 20 @ 17¢ → $3.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 29 (20 yours) | ×0.5^0 = 29.0 |
|  | 22¢ | 58 | ×0.5^5 = 1.8 |
|  | 40¢ | 16 | ×0.5^23 = 0.0 |
|  | 45¢ | 25 | ×0.5^28 = 0.0 |
|  | 97¢ | 56 | ×0.5^80 = 0.0 |
|  | 98¢ | 63,149 | ×0.5^81 = 0.0 |
| | | **Σ** | **30.8** |

`yours 20.0 / Σ 30.8 = 64.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 64.9% = $3.24/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> SELL 300 @ 30¢ → $2.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 29¢ | 14 | ×0.5^0 = 14.0 |
| ▶ | 30¢ | 504 (300 yours) | ×0.5^1 = 252.0 |
|  | 50¢ | 25 | ×0.5^21 = 0.0 |
|  | 55¢ | 44 | ×0.5^26 = 0.0 |
|  | 99¢ | 1,913 | ×0.5^70 = 0.0 |
| | | **Σ** | **266.0** |

`yours 150.0 / Σ 266.0 = 56.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 56.4% = $2.35/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil` ← this one
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>enwc-usgubp-mn-2026-08-11-rep-kenqua</code> BUY 100 @ 1¢ → $0.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,874 (100 yours) | ×0.5^0 = 5,874.0 |
| | | **Σ** | **5,874.0** |

`yours 100.0 / Σ 5,874.0 = 1.7%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 1.7% = $0.28/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `enwc-usgubp-mn-2026-08-11-rep-kenqua` ← this one
2. `enwc-usgubp-mn-2026-08-11-rep-lisdem`
3. `enwc-usgubp-mn-2026-08-11-rep-miklin`

</details>

</details>
<details><summary><code>ewc-usgub-ca-2026-11-03-stehil</code> BUY 100 @ 5¢ → $0.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 57 | ×0.5^0 = 57.0 |
| ▶ | 5¢ | 21,026 (100 yours) | ×0.5^1 = 10,513.0 |
| | | **Σ** | **10,570.0** |

`yours 50.0 / Σ 10,570.0 = 0.5%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 0.5% = $0.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usgub-ca-2026-11-03-stehil` ← this one
2. `ewc-usgub-ca-2026-11-03-xavbec`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 400 @ 1¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 646 (400 yours) | ×0.5^0 = 646.0 |
|  | 50¢ | 25 | ×0.5^49 = 0.0 |
|  | 55¢ | 44 | ×0.5^54 = 0.0 |
|  | 99¢ | 1,000 | ×0.5^98 = 0.0 |

`side 1,715 < target 2,000 → side pays nobody`  

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-24 | ~$133.49 | $135.19 | 101% |
| 2026-07-23 | ~$136.30 | $227.63 | 167% |
| 2026-07-22 | ~$110.63 | $82.95 | 75% |

Biggest gaps on 2026-07-24: `opdc-mcconnell-resign-2026-11-02` (est ~$25.83 → got $12.25), `pvwc-housepopw-2026-11-03-dem` (est ~$7.47 → got $2.62), `pvwc-housepopw-2026-11-03-rep` (est ~$12.57 → got $10.29)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (46,048 resting) | ~48.0% | ~$11.99 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (68,384 resting) | ~34.9% | ~$8.73 |
| `ewc-usgub-ia-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (122,596 resting) | ~19.4% | ~$4.85 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $100.00 ÷ 3 | 0.50 | 2,000 | SELL side (63,014 resting) | ~27.8% | ~$4.63 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (78,423 resting) | ~16.0% | ~$4.00 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (32,247 resting) | ~15.4% | ~$3.84 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (26,475 resting) | ~13.5% | ~$3.36 |
| `ewc-usgub-ks-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (157,644 resting) | ~9.8% | ~$2.45 |
| `ewc-usgub-ks-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (97,290 resting) | ~9.4% | ~$2.34 |
| `ewc-usse-ia-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (157,444 resting) | ~9.3% | ~$2.33 |
| `ewc-usgub-az-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (83,381 resting) | ~9.0% | ~$2.26 |
| `ewc-usgub-wi-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (64,174 resting) | ~8.3% | ~$2.09 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $679.56 |
| Skipped | $1.21 |
| **Total earned** | **$836.61** |

351 reward rows · 22 days with rewards · 126 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-24 | $135.19 | `████████████` |
| 2026-07-23 | $227.63 | `████████████████████` |
| 2026-07-22 | $82.95 | `███████` |
| 2026-07-21 | $91.44 | `████████` |
| 2026-07-20 | $106.54 | `█████████` |
| 2026-07-19 | $35.81 | `███` |
| 2026-07-18 | $44.41 | `████` |
| 2026-07-17 | $14.71 | `█` |
| 2026-07-16 | $17.02 | `█` |
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `█` |
| 2026-07-13 | $10.03 | `█` |
| 2026-07-12 | $39.90 | `████` |
| 2026-07-11 | $2.11 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $836.61 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $57.16 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $43.94 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $37.11 |
| `apdc-jerpowgov-2026-12-31` | $37.00 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $33.15 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.61 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $26.86 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $21.69 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $21.65 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $21.29 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $21.19 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $20.20 |
| `vmc-ussep-misen-2026-08-04-ste05-10` | $19.47 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-25 10:06 PM ET | ✅ ok | 351 | $836.61 |
| 2026-07-25 9:09 PM ET | ✅ ok | 351 | $836.61 |
| 2026-07-25 9:05 PM ET | ✅ ok | 288 | $708.72 |
| 2026-07-25 8:16 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 7:34 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 7:28 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 7:16 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 6:45 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 6:13 PM ET | ✅ ok | 282 | $701.42 |
| 2026-07-25 5:11 PM ET | ✅ ok | 282 | $701.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
