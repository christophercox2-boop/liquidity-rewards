# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-30 10:36 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$0.00/day estimated (ceiling, not promise — details below)

**Earned:** $1,321.41 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$0.32** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$15.87/day for 200 contracts. Runners-up: `cranc-uspres28-12-31-2026-andyan` (~$1.51/day), `cranc-uspres28-12-31-2026-micoba` (~$1.51/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$0.00/day (~$0.00/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `cranc-uspres28-12-31-2026-kamhar` | SELL | 27.0¢ | 2 | 4 | $100.00 | ✅ scoring — ~0.0% of ask side (5,709 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 33 markets) |
| `apdc-petehegseth-2026-12-31` | BUY | 14.0¢ | 1 | 1 | $100.00 | ❌ side has 783 of 5,000 Target Size — side not qualifying |

**Tap an order for its book window and the math:**

<details><summary><code>cranc-uspres28-12-31-2026-kamhar</code> SELL 2 @ 27¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 0 | ×0.2^0 = 0.0 |
|  | 24¢ | 6 | ×0.2^1 = 1.2 |
|  | 25¢ | 1,009 | ×0.2^2 = 40.4 |
| ▶ | 27¢ | 2 (2 yours) | ×0.2^4 = 0.0 |
|  | 28¢ | 2 | ×0.2^5 = 0.0 |
|  | 45¢ | 192 | ×0.2^22 = 0.0 |
|  | 99¢ | 4,498 | ×0.2^76 = 0.0 |
| | | **Σ** | **41.6** |

`yours 0.0 / Σ 41.6 = 0.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 0.0% = $0.00/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru`
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
17. `cranc-uspres28-12-31-2026-kamhar` ← this one
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
<details><summary><code>apdc-petehegseth-2026-12-31</code> BUY 1 @ 14¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 15¢ | 3 | ×0.2^0 = 3.0 |
| ▶ | 14¢ | 241 (1 yours) | ×0.2^1 = 48.1 |
|  | 12¢ | 6 | ×0.2^3 = 0.0 |
|  | 1¢ | 533 | ×0.2^14 = 0.0 |

`side 783 < target 5,000 → side pays nobody`  

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-29 | ~$65.42 | $0.32 | 0% |
| 2026-07-28 | ~$148.78 | $79.65 | 54% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |

Biggest gaps on 2026-07-29: `apdc-petehegseth-2026-12-31` (est ~$12.90 → got $0.00), `scc-senate-gop-2026-11-03-51` (est ~$3.25 → got $0.00), `scc-senate-gop-2026-11-03-55` (est ~$2.26 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (8,556 resting) | ~95.2% | ~$15.87 |
| `cranc-uspres28-12-31-2026-andyan` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (10,458 resting) | ~99.9% | ~$1.51 |
| `cranc-uspres28-12-31-2026-micoba` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,113 resting) | ~99.6% | ~$1.51 |
| `cranc-uspres28-12-31-2026-jdvan` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,592 resting) | ~99.2% | ~$1.50 |
| `cranc-uspres28-12-31-2026-hunbid` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (30,218 resting) | ~98.9% | ~$1.50 |
| `cranc-uspres28-12-31-2026-rahema` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,410 resting) | ~98.4% | ~$1.49 |
| `cranc-uspres28-12-31-2026-marrub` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (6,751 resting) | ~97.1% | ~$1.47 |
| `cranc-uspres28-12-31-2026-gavnew` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (81,561 resting) | ~94.2% | ~$1.43 |
| `cranc-uspres28-12-31-2026-elomus` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,511 resting) | ~93.8% | ~$1.42 |
| `cranc-uspres28-12-31-2026-krinoe` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,466 resting) | ~91.8% | ~$1.39 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,951 resting) | ~90.9% | ~$1.38 |
| `cranc-uspres28-12-31-2026-dontrujr` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (6,750 resting) | ~89.6% | ~$1.36 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,240.74 |
| Pending | $79.46 |
| Skipped | $1.21 |
| **Total earned** | **$1,321.41** |

1267 reward rows · 27 days with rewards · 352 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-29 | $0.32 | `█` |
| 2026-07-28 | $79.65 | `███████` |
| 2026-07-27 | $125.34 | `███████████` |
| 2026-07-26 | $153.80 | `██████████████` |
| 2026-07-25 | $125.69 | `███████████` |
| 2026-07-24 | $135.19 | `████████████` |
| 2026-07-23 | $227.63 | `████████████████████` |
| 2026-07-22 | $82.95 | `███████` |
| 2026-07-21 | $91.44 | `████████` |
| 2026-07-20 | $106.54 | `█████████` |
| 2026-07-19 | $35.81 | `███` |
| 2026-07-18 | $44.41 | `████` |
| 2026-07-17 | $14.71 | `█` |
| 2026-07-16 | $17.02 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,321.41 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.23 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.22 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.75 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.47 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.70 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.21 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.64 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `vmc-ussep-misen-2026-08-04-els15-20` | $22.78 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-30 10:36 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 8:06 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 5:45 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:45 AM ET | ❌ error | 1267 | $1321.41 |
| 2026-07-29 11:34 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:36 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:19 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:18 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:09 PM ET | ✅ ok | 1256 | $1321.25 |
| 2026-07-29 9:06 PM ET | ✅ ok | 1230 | $1290.27 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
