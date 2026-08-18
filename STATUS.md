# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-18 12:52 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$184.33/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$11.01/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$2.39/day), `apdc-jerpowgov-2026-08-31` (~$2.05/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$184.33/day (~$7.68/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ushrp-fl19-2026-08-18-jimsch` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-chrcol` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-madcaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimobe` | SELL | 70.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,001 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimobe` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-catlau` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 15.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (805,598 resting ≥ 5,000 ✓) ≈ $4.17/day (event pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 15.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (50,318 resting ≥ 5,000 ✓) ≈ $3.84/day (event pool ÷ 13 markets) |
| `enwc-ushrp-fl19-2026-08-18-johstr` | BUY | 1.0¢ | 1,994 | 0 | $25.00 | ✅ scoring — ~99.7% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.78/day (event pool ÷ 7 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~96.0% of bid side (52,246 resting ≥ 20,000 ✓) ≈ $3.55/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-dwajoh` | BUY | 10.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~95.9% of bid side (67,942 resting ≥ 20,000 ✓) ≈ $3.55/day (event pool ÷ 27 markets) |
| `erac-usgubp-ak-adv-2026-08-18-davbro` | BUY | 59.0¢ | 20 | 0 | $500.00 | ✅ scoring — ~76.6% of bid side (10,276 resting ≥ 10,000 ✓) ≈ $10.08/day (event pool ÷ 19 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | SELL | 95.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~72.3% of ask side (3,839 resting ≥ 2,000 ✓) ≈ $1.29/day (event pool ÷ 7 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 5.0¢ | 25 | 0 | $200.00 | ✅ scoring — ~71.4% of ask side (43,495 resting ≥ 20,000 ✓) ≈ $4.20/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 7.0¢ | 27 | 0 | $25.00 | ✅ scoring — ~69.2% of ask side (73,349 resting ≥ 2,000 ✓) ≈ $4.33/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 9.0¢ | 91 | 1 | $200.00 | ✅ scoring — ~65.8% of bid side (141,650 resting ≥ 20,000 ✓) ≈ $3.87/day (event pool ÷ 17 markets) |
| `erac-usgubp-ak-adv-2026-08-18-edndev` | BUY | 1.0¢ | 10,000 | 0 | $500.00 | ✅ scoring — ~65.4% of bid side (15,289 resting ≥ 10,000 ✓) ≈ $8.61/day (event pool ÷ 19 markets) |
| `enwc-uspres-nom-dem-2028-micoba` | BUY | 8.0¢ | 132 | 0 | $200.00 | ✅ scoring — ~55.7% of bid side (100,711 resting ≥ 20,000 ✓) ≈ $3.28/day (event pool ÷ 17 markets) |
| `erac-usgubp-ak-adv-2026-08-18-jonkre` | BUY | 82.0¢ | 10 | 0 | $500.00 | ✅ scoring — ~47.2% of bid side (10,986 resting ≥ 10,000 ✓) ≈ $6.21/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-jonkre` | BUY | 82.0¢ | 10 | 0 | $500.00 | ✅ scoring — ~47.2% of bid side (10,986 resting ≥ 10,000 ✓) ≈ $6.21/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 10.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~47.1% of bid side (130,957 resting ≥ 20,000 ✓) ≈ $1.75/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 10.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~47.1% of bid side (130,957 resting ≥ 20,000 ✓) ≈ $1.75/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 9.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~43.4% of ask side (61,240 resting ≥ 20,000 ✓) ≈ $1.61/day (event pool ÷ 27 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~41.6% of bid side (23,158 resting ≥ 5,000 ✓) ≈ $10.40/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-stasmi` | BUY | 1.0¢ | 9,549 | 3 | $200.00 | ✅ scoring — ~38.6% of bid side (22,020 resting ≥ 20,000 ✓) ≈ $1.43/day (event pool ÷ 27 markets) |
| `erac-usgubp-ak-adv-2026-08-18-mathei` | BUY | 1.0¢ | 10,000 | 0 | $500.00 | ✅ scoring — ~36.8% of bid side (27,208 resting ≥ 10,000 ✓) ≈ $4.84/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-jonoss` | BUY | 15.0¢ | 100 | 0 | $200.00 | ✅ scoring — ~34.5% of bid side (73,128 resting ≥ 20,000 ✓) ≈ $1.28/day (event pool ÷ 27 markets) |
| `vsc-usgubp-fl-fshbck-atl-9pct` | BUY | 63.0¢ | 6 | 0 | $500.00 | ✅ scoring — ~31.6% of bid side (10,502 resting ≥ 10,000 ✓) ≈ $7.89/day (event pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~31.1% of bid side (400,602 resting ≥ 5,000 ✓) ≈ $1.30/day (event pool ÷ 12 markets) |
| …and 1898 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimsch</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch` ← this one
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw` ← this one

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-chrcol</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol` ← this one
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-madcaw</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw` ← this one
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimobe</code> SELL 1 @ 70¢ → $1.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 70¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 99¢ | 2,000 | ×0.1^29 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe` ← this one
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimobe</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe` ← this one
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-catlau</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau` ← this one
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 1 @ 15¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 2¢ | 5,397 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220` ← this one
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 1 @ 15¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 11¢ | 1 | ×0.2^4 = 0.0 |
|  | 5¢ | 11 | ×0.2^10 = 0.0 |
|  | 3¢ | 105 | ×0.2^12 = 0.0 |
|  | 2¢ | 50,000 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.8% = $3.84/day`  

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
<details><summary><code>enwc-ushrp-fl19-2026-08-18-johstr</code> BUY 1,994 @ 1¢ → $1.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (1,994 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 1,994.0 / Σ 2,000.0 = 99.7%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 99.7% = $1.78/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr` ← this one
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 135 @ 8¢ → $3.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 136 (135 yours) | ×0.2^0 = 136.0 |
|  | 6¢ | 27 | ×0.2^2 = 1.1 |
|  | 5¢ | 31 | ×0.2^3 = 0.2 |
|  | 3¢ | 4,916 | ×0.2^5 = 1.6 |
|  | 2¢ | 27,500 | ×0.2^6 = 1.8 |
| | | **Σ** | **140.7** |

`yours 135.0 / Σ 140.7 = 96.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 96.0% = $3.55/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut` ← this one
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-dwajoh</code> BUY 3 @ 10¢ → $3.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 3 (3 yours) | ×0.2^0 = 3.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 5 | ×0.2^3 = 0.0 |
|  | 2¢ | 7,112 | ×0.2^8 = 0.0 |
|  | 1¢ | 60,821 | ×0.2^9 = 0.0 |
| | | **Σ** | **3.1** |

`yours 3.0 / Σ 3.1 = 95.9%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 95.9% = $3.55/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh` ← this one
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-davbro</code> BUY 20 @ 59¢ → $10.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 59¢ | 26 (20 yours) | ×0.2^0 = 25.6 |
|  | 51¢ | 250 | ×0.2^8 = 0.0 |
|  | 1¢ | 10,000 | ×0.2^58 = 0.0 |
| | | **Σ** | **25.6** |

`yours 19.6 / Σ 25.6 = 76.6%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 76.6% = $10.08/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro` ← this one
7. `erac-usgubp-ak-adv-2026-08-18-despay`
8. `erac-usgubp-ak-adv-2026-08-18-edndev`
9. `erac-usgubp-ak-adv-2026-08-18-grebre`
10. `erac-usgubp-ak-adv-2026-08-18-hankro`
11. `erac-usgubp-ak-adv-2026-08-18-jesfai`
12. `erac-usgubp-ak-adv-2026-08-18-jonkre`
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg`
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei`
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimsch</code> SELL 1 @ 95¢ → $1.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 99¢ | 3,838 | ×0.1^4 = 0.4 |
| | | **Σ** | **1.4** |

`yours 1.0 / Σ 1.4 = 72.3%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 72.3% = $1.29/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch` ← this one
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 25 @ 5¢ → $4.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 35 (25 yours) | ×0.2^0 = 35.0 |
|  | 13¢ | 130 | ×0.2^8 = 0.0 |
|  | 15¢ | 9 | ×0.2^10 = 0.0 |
|  | 18¢ | 3 | ×0.2^13 = 0.0 |
|  | 19¢ | 3 | ×0.2^14 = 0.0 |
|  | 20¢ | 25,516 | ×0.2^15 = 0.0 |
| | | **Σ** | **35.0** |

`yours 25.0 / Σ 35.0 = 71.4%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 71.4% = $4.20/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal` ← this one
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 27 @ 7¢ → $4.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 39 (27 yours) | ×0.1^0 = 39.0 |
|  | 16¢ | 50 | ×0.1^9 = 0.0 |
|  | 98¢ | 65,450 | ×0.1^91 = 0.0 |
| | | **Σ** | **39.0** |

`yours 27.0 / Σ 39.0 = 69.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 69.2% = $4.33/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> BUY 91 @ 9¢ → $3.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 4 | ×0.2^0 = 4.0 |
| ▶ | 9¢ | 111 (91 yours) | ×0.2^1 = 22.2 |
|  | 8¢ | 35 | ×0.2^2 = 1.4 |
|  | 4¢ | 110 | ×0.2^6 = 0.0 |
|  | 1¢ | 141,390 | ×0.2^9 = 0.1 |
| | | **Σ** | **27.7** |

`yours 18.2 / Σ 27.7 = 65.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 65.8% = $3.87/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri` ← this one
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-edndev</code> BUY 10,000 @ 1¢ → $8.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 15,289 (10,000 yours) | ×0.2^0 = 15,289.2 |
| | | **Σ** | **15,289.2** |

`yours 10,000.0 / Σ 15,289.2 = 65.4%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 65.4% = $8.61/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro`
7. `erac-usgubp-ak-adv-2026-08-18-despay`
8. `erac-usgubp-ak-adv-2026-08-18-edndev` ← this one
9. `erac-usgubp-ak-adv-2026-08-18-grebre`
10. `erac-usgubp-ak-adv-2026-08-18-hankro`
11. `erac-usgubp-ak-adv-2026-08-18-jesfai`
12. `erac-usgubp-ak-adv-2026-08-18-jonkre`
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg`
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei`
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-micoba</code> BUY 132 @ 8¢ → $3.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 236 (132 yours) | ×0.2^0 = 235.6 |
|  | 1¢ | 100,475 | ×0.2^7 = 1.3 |
| | | **Σ** | **236.9** |

`yours 132.0 / Σ 236.9 = 55.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 55.7% = $3.28/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba` ← this one
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-jonkre</code> BUY 10 @ 82¢ → $6.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 21 (10 yours) | ×0.2^0 = 21.0 |
|  | 81¢ | 1 | ×0.2^1 = 0.2 |
|  | 62¢ | 403 | ×0.2^20 = 0.0 |
|  | 61¢ | 250 | ×0.2^21 = 0.0 |
|  | 60¢ | 151 | ×0.2^22 = 0.0 |
|  | 44¢ | 0 | ×0.2^38 = 0.0 |
|  | 1¢ | 10,160 | ×0.2^81 = 0.0 |
| | | **Σ** | **21.2** |

`yours 10.0 / Σ 21.2 = 47.2%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 47.2% = $6.21/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro`
7. `erac-usgubp-ak-adv-2026-08-18-despay`
8. `erac-usgubp-ak-adv-2026-08-18-edndev`
9. `erac-usgubp-ak-adv-2026-08-18-grebre`
10. `erac-usgubp-ak-adv-2026-08-18-hankro`
11. `erac-usgubp-ak-adv-2026-08-18-jesfai`
12. `erac-usgubp-ak-adv-2026-08-18-jonkre` ← this one
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg`
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei`
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-jonkre</code> BUY 10 @ 82¢ → $6.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 21 (10 yours) | ×0.2^0 = 21.0 |
|  | 81¢ | 1 | ×0.2^1 = 0.2 |
|  | 62¢ | 403 | ×0.2^20 = 0.0 |
|  | 61¢ | 250 | ×0.2^21 = 0.0 |
|  | 60¢ | 151 | ×0.2^22 = 0.0 |
|  | 44¢ | 0 | ×0.2^38 = 0.0 |
|  | 1¢ | 10,160 | ×0.2^81 = 0.0 |
| | | **Σ** | **21.2** |

`yours 10.0 / Σ 21.2 = 47.2%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 47.2% = $6.21/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro`
7. `erac-usgubp-ak-adv-2026-08-18-despay`
8. `erac-usgubp-ak-adv-2026-08-18-edndev`
9. `erac-usgubp-ak-adv-2026-08-18-grebre`
10. `erac-usgubp-ak-adv-2026-08-18-hankro`
11. `erac-usgubp-ak-adv-2026-08-18-jesfai`
12. `erac-usgubp-ak-adv-2026-08-18-jonkre` ← this one
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg`
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei`
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 1 @ 10¢ → $1.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 20 | ×0.2^5 = 0.0 |
|  | 2¢ | 111 | ×0.2^8 = 0.0 |
|  | 1¢ | 130,822 | ×0.2^9 = 0.1 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 47.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 47.1% = $1.75/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema` ← this one
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 1 @ 10¢ → $1.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 20 | ×0.2^5 = 0.0 |
|  | 2¢ | 111 | ×0.2^8 = 0.0 |
|  | 1¢ | 130,822 | ×0.2^9 = 0.1 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 47.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 47.1% = $1.75/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema` ← this one
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 3 @ 9¢ → $1.61/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 4 (3 yours) | ×0.2^0 = 4.0 |
|  | 10¢ | 1 | ×0.2^1 = 0.2 |
|  | 12¢ | 1 | ×0.2^3 = 0.0 |
|  | 13¢ | 61 | ×0.2^4 = 0.1 |
|  | 15¢ | 40,737 | ×0.2^6 = 2.6 |
| | | **Σ** | **6.9** |

`yours 3.0 / Σ 6.9 = 43.4%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 43.4% = $1.61/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha` ← this one
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $10.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,402 (1,000 yours) | ×0.2^0 = 2,402.0 |
|  | 5¢ | 501 | ×0.2^4 = 0.8 |
|  | 3¢ | 30 | ×0.2^6 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^7 = 0.3 |
| | | **Σ** | **2,403.1** |

`yours 1,000.0 / Σ 2,403.1 = 41.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 41.6% = $10.40/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-stasmi</code> BUY 9,549 @ 1¢ → $1.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 22 | ×0.2^0 = 22.1 |
| ▶ | 1¢ | 21,998 (9,549 yours) | ×0.2^3 = 176.0 |
| | | **Σ** | **198.1** |

`yours 76.4 / Σ 198.1 = 38.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 38.6% = $1.43/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi` ← this one
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-mathei</code> BUY 10,000 @ 1¢ → $4.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 27,208 (10,000 yours) | ×0.2^0 = 27,208.0 |
| | | **Σ** | **27,208.0** |

`yours 10,000.0 / Σ 27,208.0 = 36.8%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 36.8% = $4.84/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro`
7. `erac-usgubp-ak-adv-2026-08-18-despay`
8. `erac-usgubp-ak-adv-2026-08-18-edndev`
9. `erac-usgubp-ak-adv-2026-08-18-grebre`
10. `erac-usgubp-ak-adv-2026-08-18-hankro`
11. `erac-usgubp-ak-adv-2026-08-18-jesfai`
12. `erac-usgubp-ak-adv-2026-08-18-jonkre`
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg`
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei` ← this one
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jonoss</code> BUY 100 @ 15¢ → $1.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 288 (100 yours) | ×0.2^0 = 287.7 |
|  | 13¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 1 | ×0.2^3 = 0.0 |
|  | 11¢ | 1,283 | ×0.2^4 = 2.1 |
|  | 8¢ | 5 | ×0.2^7 = 0.0 |
|  | 2¢ | 1,000 | ×0.2^13 = 0.0 |
|  | 1¢ | 70,550 | ×0.2^14 = 0.0 |
| | | **Σ** | **289.8** |

`yours 100.0 / Σ 289.8 = 34.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 34.5% = $1.28/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss` ← this one
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>vsc-usgubp-fl-fshbck-atl-9pct</code> BUY 6 @ 63¢ → $7.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 63¢ | 17 (6 yours) | ×0.2^0 = 17.0 |
|  | 61¢ | 50 | ×0.2^2 = 2.0 |
|  | 1¢ | 10,435 | ×0.2^62 = 0.0 |
| | | **Σ** | **19.0** |

`yours 6.0 / Σ 19.0 = 31.6%`  
`$500 ÷ 10 ÷ 2 = $25.00 × 31.6% = $7.89/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vsc-usgubp-fl-fshbck-atl-11pct`
2. `vsc-usgubp-fl-fshbck-atl-13pct`
3. `vsc-usgubp-fl-fshbck-atl-15pct`
4. `vsc-usgubp-fl-fshbck-atl-17pct`
5. `vsc-usgubp-fl-fshbck-atl-19pct`
6. `vsc-usgubp-fl-fshbck-atl-21pct`
7. `vsc-usgubp-fl-fshbck-atl-30pct`
8. `vsc-usgubp-fl-fshbck-atl-5pct`
9. `vsc-usgubp-fl-fshbck-atl-7pct`
10. `vsc-usgubp-fl-fshbck-atl-9pct` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 1 @ 13¢ → $1.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 10¢ | 150 | ×0.2^3 = 1.2 |
|  | 2¢ | 400,250 | ×0.2^11 = 0.0 |
| | | **Σ** | **3.2** |

`yours 1.0 / Σ 3.2 = 31.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 31.1% = $1.30/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215` ← this one
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,673 resting) | ~44.0% | ~$11.01 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (36,820 resting) | ~9.6% | ~$2.39 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (10,323 resting) | ~8.2% | ~$2.05 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (290,718 resting) | ~2.3% | ~$1.72 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (634,101 resting) | ~6.7% | ~$1.66 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (75,406 resting) | ~6.1% | ~$1.52 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $500.00 ÷ 3 | 0.20 | 10,000 | BUY side (10,779 resting) | ~1.8% | ~$1.52 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (91,306 resting) | ~19.1% | ~$1.19 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,903 resting) | ~1.6% | ~$1.18 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (76,118 resting) | ~1.5% | ~$1.16 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (164,411 resting) | ~16.5% | ~$1.03 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (96,160 resting) | ~1.3% | ~$0.99 |

## Totals

| | Amount |
|---|---:|
| Paid | $4,919.08 |
| Pending | $197.10 |
| Skipped | $1.41 |
| **Total earned** | **$5,117.59** |

2859 reward rows · 45 days with rewards · 559 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-16 ⚠️ multi-day pending bucket | $197.03 | `███` |
| 2026-08-15 | $1,352.63 | `████████████████████` |
| 2026-08-14 | $274.92 | `████` |
| 2026-08-13 | $223.24 | `███` |
| 2026-08-12 | $213.04 | `███` |
| 2026-08-11 | $409.60 | `██████` |
| 2026-08-10 | $557.62 | `████████` |
| 2026-08-09 | $62.24 | `█` |
| 2026-08-08 | $54.83 | `█` |
| 2026-08-07 | $60.34 | `█` |
| 2026-08-06 | $52.22 | `█` |
| 2026-08-05 | $31.46 | `█` |
| 2026-08-04 | $53.94 | `█` |
| 2026-08-03 | $44.81 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $3,654.27 | `████████████████████` |
| 2026-07 | $1,463.32 | `████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $178.70 |
| `apdc-alito-2026-12-31` | $115.00 |
| `ewc-usp-party-2028-11-07-rep` | $100.01 |
| `ewc-usp-party-2028-11-07-dem` | $79.48 |
| `opdc-mcconnell-resign-2026-11-02` | $79.41 |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | $66.06 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $63.61 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $62.40 |
| `enwc-uspres-nom-rep-2028-rondes` | $48.49 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.60 |
| `enwc-uspres-nom-dem-2028-stasmi` | $44.12 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.51 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.04 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-18 12:52 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-17 8:50 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 7:50 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 6:49 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 5:49 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 4:48 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 3:48 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 2:47 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 1:33 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 12:50 PM ET | ✅ ok | 2700 | $4920.49 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
