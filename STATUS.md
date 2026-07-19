# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-19 3:36 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$6.98/day estimated (ceiling, not promise — details below)

**Earned:** $112.64 lifetime ($78.17 paid). Last three recorded days — 2026-07-17: **$14.71** · 2026-07-16: **$17.02** · 2026-07-15: **$1.53** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — SELL at the best price, ~$5.32/day for 200 contracts. Runners-up: `enwc-usgubp-sd-2026-06-02-rep-larrho` (~$4.33/day), `enwc-usgubp-sd-2026-06-02-rep-tobdoe` (~$3.35/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$6.98/day (~$0.29/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | SELL | 6.0¢ | 98 | 0 | $250.00 | ✅ scoring — ~22.5% of ask side (11,280 resting ≥ 10,000 ✓) ≈ $4.68/day (pool ÷ 6 markets) |
| `cranc-uspres28-12-31-2026-dontru` | SELL | 45.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~9.2% of ask side (12,921 resting ≥ 10,000 ✓) ≈ $0.35/day (pool ÷ 33 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 22.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~3.1% of ask side (30,875 resting ≥ 10,000 ✓) ≈ $1.95/day (pool ÷ 2 markets) |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-manbar</code> SELL 98 @ 6¢ → $4.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 432 (98 yours) | ×0.3^0 = 432.0 |
|  | 7¢ | 13 | ×0.3^1 = 3.9 |
|  | 30¢ | 250 | ×0.3^24 = 0.0 |
|  | 99¢ | 10,585 | ×0.3^93 = 0.0 |
| | | **Σ** | **435.9** |

`yours 98.0 / Σ 435.9 = 22.5%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 22.5% = $4.68/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar` ← this one
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-dontru</code> SELL 100 @ 45¢ → $0.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 1,091 (100 yours) | ×0.3^0 = 1,091.0 |
|  | 49¢ | 100 | ×0.3^4 = 0.8 |
|  | 99¢ | 11,730 | ×0.3^54 = 0.0 |
| | | **Σ** | **1,091.8** |

`yours 100.0 / Σ 1,091.8 = 9.2%`  
`$250 ÷ 33 ÷ 2 = $3.79 × 9.2% = $0.35/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru` ← this one
7. `cranc-uspres28-12-31-2026-dontrujr`
8. `cranc-uspres28-12-31-2026-dwajoh`
9. `cranc-uspres28-12-31-2026-elomus`
10. `cranc-uspres28-12-31-2026-erikir`
11. `cranc-uspres28-12-31-2026-gavnew`
12. `cranc-uspres28-12-31-2026-hilcli`
13. `cranc-uspres28-12-31-2026-hunbid`
14. `cranc-uspres28-12-31-2026-jdvan`
15. `cranc-uspres28-12-31-2026-jonoss`
16. `cranc-uspres28-12-31-2026-jossha`
17. `cranc-uspres28-12-31-2026-kamhar`
18. `cranc-uspres28-12-31-2026-krinoe`
19. `cranc-uspres28-12-31-2026-margre`
20. `cranc-uspres28-12-31-2026-markel`
21. `cranc-uspres28-12-31-2026-marrub`
22. `cranc-uspres28-12-31-2026-micoba`
23. `cranc-uspres28-12-31-2026-nikhal`
24. `cranc-uspres28-12-31-2026-oprwin`
25. `cranc-uspres28-12-31-2026-petbut`
26. `cranc-uspres28-12-31-2026-rahema`
27. `cranc-uspres28-12-31-2026-robken`
28. `cranc-uspres28-12-31-2026-steban`
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 100 @ 22¢ → $1.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 577 (100 yours) | ×0.3^0 = 577.0 |
|  | 24¢ | 29,262 | ×0.3^2 = 2,633.6 |
| | | **Σ** | **3,210.6** |

`yours 100.0 / Σ 3,210.6 = 3.1%`  
`$250 ÷ 2 ÷ 2 = $62.50 × 3.1% = $1.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun`
2. `enwc-ussep-nh-2026-09-01-rep-scobro` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (60,812 resting) | ~8.5% | ~$5.32 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (72,025 resting) | ~6.9% | ~$4.33 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (31,226 resting) | ~5.4% | ~$3.35 |
| `cranc-uspres28-12-31-2026-jonoss` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (18,322 resting) | ~74.9% | ~$2.84 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (27,027 resting) | ~6.4% | ~$2.65 |
| `cranc-uspres28-12-31-2026-markel` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (18,687 resting) | ~69.4% | ~$2.63 |
| `cranc-uspres28-12-31-2026-jdvan` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (11,000 resting) | ~65.0% | ~$2.46 |
| `cranc-uspres28-12-31-2026-rahema` | $250.00 ÷ 33 | 0.30 | 10,000 | SELL side (11,088 resting) | ~58.5% | ~$2.22 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (78,771 resting) | ~2.1% | ~$1.33 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (59,029 resting) | ~3.2% | ~$1.32 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (28,441 resting) | ~1.8% | ~$1.15 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (11,822 resting) | ~1.7% | ~$1.07 |

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
| 2026-07-19 3:36 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 3:22 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 2:47 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 2:16 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:57 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:53 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 1:27 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 12:14 PM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 11:18 AM ET | ✅ ok | 102 | $112.64 |
| 2026-07-19 10:50 AM ET | ✅ ok | 102 | $112.64 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
