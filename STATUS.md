# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-18 1:58 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$298.85/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$17.67/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$11.42/day), `ewc-usgub-ga-2026-11-03-dem` (~$10.64/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$298.85/day (~$12.45/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ussewc-usse-wy-2026-11-03-rep` | BUY | 88.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,266 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 76.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,383 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 86.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,153 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-rep` | BUY | 76.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,365 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-pa-2026-11-03-dem` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (7,157 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ma-2026-11-03-dem` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,365 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `vsc-usgubp-fl-fshbck-atl-11pct` | BUY | 43.0¢ | 9 | 0 | $500.00 | ✅ scoring — ~98.9% of bid side (31,104 resting ≥ 10,000 ✓) ≈ $24.72/day (event pool ÷ 10 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 6.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~98.7% of ask side (30,801 resting ≥ 20,000 ✓) ≈ $7.05/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-jonoss` | SELL | 18.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~97.6% of ask side (58,864 resting ≥ 20,000 ✓) ≈ $3.62/day (event pool ÷ 27 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 85.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~94.8% of ask side (2,058 resting ≥ 2,000 ✓) ≈ $5.92/day (event pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~90.9% of ask side (66,186 resting ≥ 2,000 ✓) ≈ $5.68/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 4.0¢ | 61 | 0 | $200.00 | ✅ scoring — ~85.9% of ask side (34,084 resting ≥ 20,000 ✓) ≈ $5.05/day (event pool ÷ 17 markets) |
| `vsc-usgubp-fl-fshbck-atl-5pct` | BUY | 88.0¢ | 30 | 0 | $500.00 | ✅ scoring — ~84.6% of bid side (50,814 resting ≥ 10,000 ✓) ≈ $21.15/day (event pool ÷ 10 markets) |
| `enwc-uspres-nom-dem-2028-micoba` | SELL | 4.0¢ | 42 | 0 | $200.00 | ✅ scoring — ~84.1% of ask side (30,464 resting ≥ 20,000 ✓) ≈ $4.95/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-al-2026-11-03-dem` | SELL | 7.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (134,028 resting ≥ 2,000 ✓) ≈ $5.21/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~78.3% of bid side (2,029 resting ≥ 2,000 ✓) ≈ $4.89/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~76.6% of bid side (2,035 resting ≥ 2,000 ✓) ≈ $3.19/day (event pool ÷ 3 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~67.4% of bid side (500,352 resting ≥ 2,000 ✓) ≈ $4.21/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | SELL | 24.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~66.3% of ask side (57,969 resting ≥ 20,000 ✓) ≈ $3.90/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~62.9% of ask side (130,788 resting ≥ 2,000 ✓) ≈ $3.93/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-aleocc` | BUY | 21.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~62.4% of bid side (71,007 resting ≥ 20,000 ✓) ≈ $3.67/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 87.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~60.0% of ask side (27,343 resting ≥ 2,000 ✓) ≈ $3.75/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 8.0¢ | 1 | 1 | $100.00 | ✅ scoring — ~57.8% of bid side (305,763 resting ≥ 5,000 ✓) ≈ $2.22/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~57.1% of ask side (208,350 resting ≥ 2,000 ✓) ≈ $3.57/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 20.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~56.0% of bid side (77,372 resting ≥ 20,000 ✓) ≈ $3.30/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~55.7% of ask side (65,538 resting ≥ 2,000 ✓) ≈ $3.48/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 9.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~49.8% of ask side (46,917 resting ≥ 20,000 ✓) ≈ $1.84/day (event pool ÷ 27 markets) |
| `ussewc-usse-tn-2026-11-03-dem` | SELL | 5.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~43.8% of ask side (527,397 resting ≥ 2,000 ✓) ≈ $2.74/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 12.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~43.1% of bid side (30,219 resting ≥ 20,000 ✓) ≈ $1.60/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 12.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~43.1% of bid side (30,219 resting ≥ 20,000 ✓) ≈ $1.60/day (event pool ÷ 27 markets) |
| …and 1347 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> BUY 3 @ 88¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 50¢ | 61 | ×0.1^38 = 0.0 |
|  | 39¢ | 1 | ×0.1^49 = 0.0 |
|  | 36¢ | 1 | ×0.1^52 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^86 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> BUY 3 @ 76¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 76¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 58¢ | 150 | ×0.1^18 = 0.0 |
|  | 57¢ | 1 | ×0.1^19 = 0.0 |
|  | 46¢ | 4 | ×0.1^30 = 0.0 |
|  | 40¢ | 25 | ×0.1^36 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^74 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 3 @ 86¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 86¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 68¢ | 150 | ×0.1^18 = 0.0 |
|  | 17¢ | 1 | ×0.1^69 = 0.0 |
|  | 1¢ | 1,999 | ×0.1^85 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> BUY 3 @ 76¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 76¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 57¢ | 154 | ×0.1^19 = 0.0 |
|  | 56¢ | 1 | ×0.1^20 = 0.0 |
|  | 35¢ | 1 | ×0.1^41 = 0.0 |
|  | 13¢ | 1 | ×0.1^63 = 0.0 |
|  | 10¢ | 5 | ×0.1^66 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^74 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem`
2. `usgubewc-usgub-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-pa-2026-11-03-dem</code> BUY 3 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 77¢ | 150 | ×0.1^17 = 0.0 |
|  | 55¢ | 4 | ×0.1^39 = 0.0 |
|  | 50¢ | 100 | ×0.1^44 = 0.0 |
|  | 2¢ | 100 | ×0.1^92 = 0.0 |
|  | 1¢ | 6,800 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem` ← this one
2. `usgubewc-usgub-pa-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ma-2026-11-03-dem</code> BUY 3 @ 94¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 79¢ | 150 | ×0.1^15 = 0.0 |
|  | 60¢ | 4 | ×0.1^34 = 0.0 |
|  | 59¢ | 1 | ×0.1^35 = 0.0 |
|  | 43¢ | 1 | ×0.1^51 = 0.0 |
|  | 31¢ | 1 | ×0.1^63 = 0.0 |
|  | 10¢ | 5 | ×0.1^84 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>vsc-usgubp-fl-fshbck-atl-11pct</code> BUY 9 @ 43¢ → $24.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 9 (9 yours) | ×0.2^0 = 8.7 |
|  | 39¢ | 50 | ×0.2^4 = 0.1 |
|  | 38¢ | 21 | ×0.2^5 = 0.0 |
|  | 37¢ | 30 | ×0.2^6 = 0.0 |
|  | 36¢ | 744 | ×0.2^7 = 0.0 |
|  | 2¢ | 30,000 | ×0.2^41 = 0.0 |
| | | **Σ** | **8.8** |

`yours 8.7 / Σ 8.8 = 98.9%`  
`$500 ÷ 10 ÷ 2 = $25.00 × 98.9% = $24.72/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vsc-usgubp-fl-fshbck-atl-11pct` ← this one
2. `vsc-usgubp-fl-fshbck-atl-13pct`
3. `vsc-usgubp-fl-fshbck-atl-15pct`
4. `vsc-usgubp-fl-fshbck-atl-17pct`
5. `vsc-usgubp-fl-fshbck-atl-19pct`
6. `vsc-usgubp-fl-fshbck-atl-21pct`
7. `vsc-usgubp-fl-fshbck-atl-30pct`
8. `vsc-usgubp-fl-fshbck-atl-5pct`
9. `vsc-usgubp-fl-fshbck-atl-7pct`
10. `vsc-usgubp-fl-fshbck-atl-9pct`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 1 @ 6¢ → $7.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 15¢ | 26,392 | ×0.2^9 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 98.7% = $7.05/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes` ← this one
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jonoss</code> SELL 1 @ 18¢ → $3.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 3 | ×0.2^3 = 0.0 |
|  | 28¢ | 30 | ×0.2^10 = 0.0 |
|  | 29¢ | 101 | ×0.2^11 = 0.0 |
|  | 30¢ | 38,479 | ×0.2^12 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 97.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 97.6% = $3.62/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 2 @ 85¢ → $5.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 86¢ | 1 | ×0.1^1 = 0.1 |
|  | 87¢ | 1 | ×0.1^2 = 0.0 |
|  | 98¢ | 55 | ×0.1^13 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^14 = 0.0 |
| | | **Σ** | **2.1** |

`yours 2.0 / Σ 2.1 = 94.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.8% = $5.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 7¢ → $5.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 8¢ | 2 | ×0.1^1 = 0.2 |
|  | 15¢ | 157 | ×0.1^8 = 0.0 |
|  | 18¢ | 50 | ×0.1^11 = 0.0 |
|  | 45¢ | 500 | ×0.1^38 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^91 = 0.0 |
| | | **Σ** | **2.2** |

`yours 2.0 / Σ 2.2 = 90.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.9% = $5.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> SELL 61 @ 4¢ → $5.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 71 (61 yours) | ×0.2^0 = 71.0 |
|  | 16¢ | 219 | ×0.2^12 = 0.0 |
|  | 19¢ | 4 | ×0.2^15 = 0.0 |
|  | 26¢ | 16,040 | ×0.2^22 = 0.0 |
|  | 30¢ | 15,000 | ×0.2^26 = 0.0 |
| | | **Σ** | **71.0** |

`yours 61.0 / Σ 71.0 = 85.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 85.9% = $5.05/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes` ← this one
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
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
<details><summary><code>vsc-usgubp-fl-fshbck-atl-5pct</code> BUY 30 @ 88¢ → $21.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 33 (30 yours) | ×0.2^0 = 33.0 |
|  | 85¢ | 308 | ×0.2^3 = 2.5 |
|  | 82¢ | 62 | ×0.2^6 = 0.0 |
|  | 80¢ | 161 | ×0.2^8 = 0.0 |
|  | 2¢ | 50,000 | ×0.2^86 = 0.0 |
| | | **Σ** | **35.5** |

`yours 30.0 / Σ 35.5 = 84.6%`  
`$500 ÷ 10 ÷ 2 = $25.00 × 84.6% = $21.15/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vsc-usgubp-fl-fshbck-atl-11pct`
2. `vsc-usgubp-fl-fshbck-atl-13pct`
3. `vsc-usgubp-fl-fshbck-atl-15pct`
4. `vsc-usgubp-fl-fshbck-atl-17pct`
5. `vsc-usgubp-fl-fshbck-atl-19pct`
6. `vsc-usgubp-fl-fshbck-atl-21pct`
7. `vsc-usgubp-fl-fshbck-atl-30pct`
8. `vsc-usgubp-fl-fshbck-atl-5pct` ← this one
9. `vsc-usgubp-fl-fshbck-atl-7pct`
10. `vsc-usgubp-fl-fshbck-atl-9pct`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-micoba</code> SELL 42 @ 4¢ → $4.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 50 (42 yours) | ×0.2^0 = 50.5 |
|  | 9¢ | 53 | ×0.2^5 = 0.0 |
|  | 14¢ | 37 | ×0.2^10 = 0.0 |
|  | 15¢ | 1 | ×0.2^11 = 0.0 |
|  | 16¢ | 4 | ×0.2^12 = 0.0 |
|  | 17¢ | 26,417 | ×0.2^13 = 0.0 |
| | | **Σ** | **50.5** |

`yours 42.5 / Σ 50.5 = 84.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 84.1% = $4.95/day`  

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
<details><summary><code>usgubewc-usgub-al-2026-11-03-dem</code> SELL 10 @ 7¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 12 (10 yours) | ×0.1^0 = 12.0 |
|  | 15¢ | 0 | ×0.1^8 = 0.0 |
|  | 16¢ | 50 | ×0.1^9 = 0.0 |
|  | 21¢ | 335 | ×0.1^14 = 0.0 |
|  | 22¢ | 500 | ×0.1^15 = 0.0 |
|  | 25¢ | 20 | ×0.1^18 = 0.0 |
|  | 27¢ | 68 | ×0.1^20 = 0.0 |
|  | 98¢ | 132,818 | ×0.1^91 = 0.0 |
| | | **Σ** | **12.0** |

`yours 10.0 / Σ 12.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem` ← this one
2. `usgubewc-usgub-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $4.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 30 | ×0.1^0 = 30.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **229.9** |

`yours 179.9 / Σ 229.9 = 78.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 78.3% = $4.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $3.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 35 | ×0.1^0 = 35.0 |
| ▶ | 1¢ | 2,000 (1,799 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **235.0** |

`yours 179.9 / Σ 235.0 = 76.6%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 76.6% = $3.19/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 3 @ 94¢ → $4.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 92¢ | 145 | ×0.1^2 = 1.5 |
|  | 12¢ | 4 | ×0.1^82 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **4.5** |

`yours 3.0 / Σ 4.5 = 67.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 67.4% = $4.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> SELL 1 @ 24¢ → $3.90/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 25¢ | 1 | ×0.2^1 = 0.2 |
|  | 26¢ | 4 | ×0.2^2 = 0.2 |
|  | 28¢ | 30 | ×0.2^4 = 0.0 |
|  | 31¢ | 54 | ×0.2^7 = 0.0 |
|  | 32¢ | 38,957 | ×0.2^8 = 0.1 |
| | | **Σ** | **1.5** |

`yours 1.0 / Σ 1.5 = 66.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 66.3% = $3.90/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss` ← this one
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
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> SELL 1 @ 6¢ → $3.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 8¢ | 59 | ×0.1^2 = 0.6 |
|  | 21¢ | 1 | ×0.1^15 = 0.0 |
|  | 26¢ | 1 | ×0.1^20 = 0.0 |
|  | 68¢ | 1 | ×0.1^62 = 0.0 |
|  | 96¢ | 0 | ×0.1^90 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^92 = 0.0 |
| | | **Σ** | **1.6** |

`yours 1.0 / Σ 1.6 = 62.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 62.9% = $3.93/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-aleocc</code> BUY 20 @ 21¢ → $3.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 18¢ | 612 | ×0.2^3 = 4.9 |
|  | 17¢ | 3,822 | ×0.2^4 = 6.1 |
|  | 13¢ | 16,250 | ×0.2^8 = 0.0 |
| | | **Σ** | **32.1** |

`yours 20.0 / Σ 32.1 = 62.4%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 62.4% = $3.67/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc` ← this one
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
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 3 @ 87¢ → $3.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 5 (3 yours) | ×0.1^0 = 5.0 |
|  | 97¢ | 5,348 | ×0.1^10 = 0.0 |
| | | **Σ** | **5.0** |

`yours 3.0 / Σ 5.0 = 60.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.0% = $3.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 8¢ → $2.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 8¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 6¢ | 2 | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^4 = 0.0 |
|  | 4¢ | 5 | ×0.2^5 = 0.0 |
|  | 3¢ | 2 | ×0.2^6 = 0.0 |
|  | 2¢ | 5,200 | ×0.2^7 = 0.1 |
| | | **Σ** | **0.3** |

`yours 0.2 / Σ 0.3 = 57.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 57.8% = $2.22/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52` ← this one
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 2 @ 7¢ → $3.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 3 (2 yours) | ×0.1^0 = 3.0 |
|  | 9¢ | 50 | ×0.1^2 = 0.5 |
|  | 93¢ | 9 | ×0.1^86 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^91 = 0.0 |
| | | **Σ** | **3.5** |

`yours 2.0 / Σ 3.5 = 57.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.1% = $3.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 1 @ 20¢ → $3.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 17¢ | 62 | ×0.2^3 = 0.5 |
|  | 15¢ | 697 | ×0.2^5 = 0.2 |
|  | 13¢ | 4,999 | ×0.2^7 = 0.1 |
|  | 10¢ | 21,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.8** |

`yours 1.0 / Σ 1.8 = 56.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 56.0% = $3.30/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss` ← this one
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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 2 @ 7¢ → $3.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 3 (2 yours) | ×0.1^0 = 3.0 |
|  | 9¢ | 59 | ×0.1^2 = 0.6 |
|  | 28¢ | 1 | ×0.1^21 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^91 = 0.0 |
| | | **Σ** | **3.6** |

`yours 2.0 / Σ 3.6 = 55.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 55.7% = $3.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 3 @ 9¢ → $1.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 4 (3 yours) | ×0.2^0 = 4.0 |
|  | 10¢ | 1 | ×0.2^1 = 0.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 13¢ | 61 | ×0.2^4 = 0.1 |
|  | 15¢ | 26,429 | ×0.2^6 = 1.7 |
| | | **Σ** | **6.0** |

`yours 3.0 / Σ 6.0 = 49.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 49.8% = $1.84/day`  

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
<details><summary><code>ussewc-usse-tn-2026-11-03-dem</code> SELL 2 @ 5¢ → $2.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 4 (2 yours) | ×0.1^0 = 4.0 |
|  | 7¢ | 57 | ×0.1^2 = 0.6 |
|  | 98¢ | 132,784 | ×0.1^93 = 0.0 |
| | | **Σ** | **4.6** |

`yours 2.0 / Σ 4.6 = 43.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 43.8% = $2.74/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem` ← this one
2. `ussewc-usse-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 12¢ → $1.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 11¢ | 1 | ×0.2^1 = 0.2 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 9¢ | 5 | ×0.2^3 = 0.0 |
|  | 2¢ | 112 | ×0.2^10 = 0.0 |
|  | 1¢ | 30,097 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 43.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 43.1% = $1.60/day`  

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
10. `ewc-usp-2028-11-07-jbpri` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 12¢ → $1.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 11¢ | 1 | ×0.2^1 = 0.2 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 9¢ | 5 | ×0.2^3 = 0.0 |
|  | 2¢ | 112 | ×0.2^10 = 0.0 |
|  | 1¢ | 30,097 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 43.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 43.1% = $1.60/day`  

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
10. `ewc-usp-2028-11-07-jbpri` ← this one
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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,821 resting) | ~70.7% | ~$17.67 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (273,833 resting) | ~15.2% | ~$11.42 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (79,900 resting) | ~14.2% | ~$10.64 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (72,001 resting) | ~34.9% | ~$8.73 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (71,051 resting) | ~4.2% | ~$3.19 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (74,696 resting) | ~49.3% | ~$3.08 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,078 resting) | ~3.9% | ~$2.95 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (632,633 resting) | ~9.0% | ~$2.25 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (64,473 resting) | ~8.2% | ~$2.05 |
| `ewc-usse-ak-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (376,348 resting) | ~22.5% | ~$1.40 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,244,653 resting) | ~20.6% | ~$1.29 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,401 resting) | ~1.7% | ~$1.24 |

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
| 2026-08-18 1:58 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 1:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 12:44 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 12:34 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 11:57 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 10:56 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 7:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:22 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
