# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ❌ Last check FAILED — 2026-07-22 4:34 PM ET

```
RuntimeError: https://api.prod.polymarketexchange.com/v1/incentives/earnings -> HTTP 401: {"message":"Unauthorized"}
https://api.polymarket.us/v1/incentives/earnings -> HTTP 500: {"code":2, "message":"The server was unable to process your request.", "details":[]}
probe https://api.prod.polymarketexchange.com/v1/incentives (no auth) -> HTTP 503
probe https://api.polymarket.us/v1/incentives (no auth) -> HTTP 401
```

The data below is from the last successful run. See the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml) for logs.

## 📌 Summary

**Earning right now:** couldn't be estimated this run — see details below

**Earned:** $299.40 lifetime ($155.84 paid). Last three recorded days — 2026-07-20: **$106.54** · 2026-07-19: **$35.81** · 2026-07-18: **$44.41** _(Polymarket reports ~1–2 days behind)_


---

# The details (how the numbers above are computed)

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-20 | ~$125.00 | $106.54 | 85% |
| 2026-07-19 | ~$36.97 | $35.81 | 97% |

Biggest gaps on 2026-07-20: `enwc-usgubp-wi-2026-08-11-dem-davcro` (est ~$21.74 → got $16.08), `enwc-ussep-nh-2026-09-01-rep-scobro` (est ~$11.93 → got $8.30), `enwc-usgubp-ok-2026-06-16-rep-gendru` (est ~$4.33 → got $2.14)

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
| 2026-07-22 4:34 PM ET | ❌ error | 186 | $299.40 |
| 2026-07-22 2:36 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 12:51 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 10:28 AM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 8:07 AM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 5:41 AM ET | ✅ ok | 186 | $299.40 |
| 2026-07-22 2:44 AM ET | ✅ ok | 186 | $299.40 |
| 2026-07-21 11:51 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-21 9:16 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-21 9:06 PM ET | ✅ ok | 149 | $192.86 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
