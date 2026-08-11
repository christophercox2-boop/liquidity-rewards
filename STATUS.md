# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ❌ Last check FAILED — 2026-08-11 6:25 AM ET

```
RuntimeError: https://api.prod.polymarketexchange.com/v1/incentives/earnings -> HTTP 401: {"message":"Unauthorized"}
https://api.polymarket.us/v1/incentives/earnings -> HTTP 500: {"code":2,"message":"The server was unable to process your request.","details":[]}
probe https://api.prod.polymarketexchange.com/v1/incentives (no auth) -> HTTP 503
probe https://api.polymarket.us/v1/incentives (no auth) -> HTTP 401
```

The data below is from the last successful run. See the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml) for logs.

## 📌 Summary

**Earning right now:** couldn't be estimated this run — see details below

**Earned:** $1,889.44 lifetime ($1,771.01 paid). Last three recorded days — 2026-08-09: **$62.24** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-08: **$54.78** · 2026-08-07: **$60.33** _(Polymarket reports ~1–2 days behind)_


---

# The details (how the numbers above are computed)

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-08 | ~$111.62 | $54.78 | 49% |
| 2026-08-07 | ~$116.96 | $60.33 | 52% |
| 2026-08-06 | ~$60.78 | $52.21 | 86% |

Biggest gaps on 2026-08-08: `opdc-mcconnell-resign-2026-11-02` (est ~$9.47 → got $3.79), `scc-hrep-rep-2026-11-03-gte210` (est ~$5.11 → got $0.11), `scc-hrep-rep-2026-11-03-gte185` (est ~$4.26 → got $0.16)

_2026-08-09 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## Totals

| | Amount |
|---|---:|
| Paid | $1,771.01 |
| Pending | $117.02 |
| Skipped | $1.41 |
| **Total earned** | **$1,889.44** |

1818 reward rows · 38 days with rewards · 378 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-09 ⚠️ multi-day pending bucket | $62.24 | `██████████` |
| 2026-08-08 | $54.78 | `█████████` |
| 2026-08-07 | $60.33 | `██████████` |
| 2026-08-06 | $52.21 | `████████` |
| 2026-08-05 | $31.46 | `█████` |
| 2026-08-04 | $53.94 | `█████████` |
| 2026-08-03 | $44.81 | `███████` |
| 2026-08-02 | $14.05 | `██` |
| 2026-08-01 | $52.30 | `████████` |
| 2026-07-31 | $67.96 | `███████████` |
| 2026-07-30 | $20.67 | `███` |
| 2026-07-29 | $53.60 | `█████████` |
| 2026-07-28 | $79.65 | `█████████████` |
| 2026-07-27 | $125.34 | `████████████████████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $426.12 | `██████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $92.91 |
| `apdc-jerpowgov-2026-12-31` | $78.79 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `opdc-mcconnell-resign-2026-11-02` | $56.96 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.95 |
| `scc-hrep-rep-2026-11-03-gte200` | $36.01 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-11 6:25 AM ET | ❌ error | 1818 | $1889.44 |
| 2026-08-11 6:14 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 5:16 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 3:41 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 2:07 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 12:43 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-10 11:18 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-10 11:17 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-10 11:14 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-10 11:13 PM ET | ✅ ok | 1818 | $1889.44 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
