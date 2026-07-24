# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ❌ Last check FAILED — 2026-07-24 2:42 AM ET

```
RuntimeError: https://api.prod.polymarketexchange.com/v1/incentives/earnings -> HTTP 401: {"message":"Unauthorized"}
https://api.polymarket.us/v1/incentives/earnings -> HTTP 500: {"code":2, "message":"The server was unable to process your request.", "details":[]}
probe https://api.prod.polymarketexchange.com/v1/incentives (no auth) -> HTTP 503
probe https://api.polymarket.us/v1/incentives (no auth) -> HTTP 401
```

The data below is from the last successful run. See the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml) for logs.

## 📌 Summary

**Earning right now:** couldn't be estimated this run — see details below

**Earned:** $606.98 lifetime ($155.84 paid). Last three recorded days — 2026-07-23: **$133.19** · 2026-07-22: **$82.95** · 2026-07-21: **$91.44** _(Polymarket reports ~1–2 days behind)_


---

# The details (how the numbers above are computed)

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-23 | ~$136.30 | $133.19 | 98% |
| 2026-07-22 | ~$110.63 | $82.95 | 75% |
| 2026-07-21 | ~$87.94 | $91.44 | 104% |

Biggest gaps on 2026-07-23: `scc-hrep-rep-2026-11-03-gte210` (est ~$2.21 → got $0.00), `scc-senate-gop-2026-11-03-55` (est ~$2.14 → got $0.00), `opdc-trump-resig-2027-12-31` (est ~$2.12 → got $0.00)

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $449.93 |
| Skipped | $1.21 |
| **Total earned** | **$606.98** |

257 reward rows · 21 days with rewards · 79 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-23 | $133.19 | `████████████████████` |
| 2026-07-22 | $82.95 | `████████████` |
| 2026-07-21 | $91.44 | `██████████████` |
| 2026-07-20 | $106.54 | `████████████████` |
| 2026-07-19 | $35.81 | `█████` |
| 2026-07-18 | $44.41 | `███████` |
| 2026-07-17 | $14.71 | `██` |
| 2026-07-16 | $17.02 | `███` |
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `██` |
| 2026-07-13 | $10.03 | `██` |
| 2026-07-12 | $39.90 | `██████` |
| 2026-07-11 | $2.11 | `█` |
| 2026-07-10 | $2.16 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $606.98 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $56.41 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $43.94 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $36.49 |
| `apdc-jerpowgov-2026-12-31` | $26.93 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $26.68 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $23.68 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $21.84 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $21.56 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $19.23 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $18.02 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $17.30 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $16.88 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.58 |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | $14.80 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-24 2:42 AM ET | ❌ error | 257 | $606.98 |
| 2026-07-23 11:48 PM ET | ✅ ok | 257 | $606.98 |
| 2026-07-23 9:18 PM ET | ✅ ok | 257 | $606.98 |
| 2026-07-23 9:06 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 9:02 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:55 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:53 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:49 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:13 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:11 PM ET | ✅ ok | 211 | $390.84 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
