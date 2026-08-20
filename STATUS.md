# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 1:52 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$479.43/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `paccc-usho-midterms-2026-11-03-rep` — BUY at the best price, ~$32.73/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$14.67/day), `ewc-usgub-ga-2026-11-03-dem` (~$11.50/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$479.43/day (~$19.98/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ussewc-usse-ks-2026-11-03-dem` | SELL | 25.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (130,899 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 21.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.8% of ask side (92,009 resting ≥ 5,000 ✓) ≈ $3.84/day (event pool ÷ 13 markets) |
| `ussewc-usse-or-2026-11-03-rep` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.5% of ask side (130,801 resting ≥ 2,000 ✓) ≈ $6.22/day (event pool ÷ 2 markets) |
| `aachc-cfb-wins-2026-11-28-ala-6pt5wins` | BUY | 91.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~99.3% of bid side (5,782 resting ≥ 5,000 ✓) ≈ $2.48/day (event pool ÷ 5 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.0% of ask side (69,031 resting ≥ 2,000 ✓) ≈ $6.19/day (event pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 5,000 | 1 | $25.00 | ✅ scoring — ~97.8% of bid side (5,101 resting ≥ 2,000 ✓) ≈ $6.12/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 86 | 0 | $200.00 | ✅ scoring — ~97.7% of ask side (44,789 resting ≥ 20,000 ✓) ≈ $6.98/day (event pool ÷ 14 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 89.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~97.7% of ask side (2,101 resting ≥ 2,000 ✓) ≈ $6.10/day (event pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~94.7% of ask side (66,195 resting ≥ 2,000 ✓) ≈ $5.92/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tn-2026-11-03-rep` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~93.6% of bid side (2,210 resting ≥ 2,000 ✓) ≈ $5.85/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-sc-2026-11-03-dem` | SELL | 9.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.9% of ask side (196,141 resting ≥ 2,000 ✓) ≈ $5.68/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.1% of ask side (70,634 resting ≥ 2,000 ✓) ≈ $5.63/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~89.8% of bid side (50,361 resting ≥ 20,000 ✓) ≈ $3.33/day (event pool ÷ 27 markets) |
| `ussewc-usse-de-2026-11-03-rep` | BUY | 1.0¢ | 1,798 | 1 | $25.00 | ✅ scoring — ~87.8% of bid side (2,004 resting ≥ 2,000 ✓) ≈ $5.48/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 15.0¢ | 146 | 0 | $100.00 | ✅ scoring — ~86.4% of bid side (805,769 resting ≥ 5,000 ✓) ≈ $3.60/day (event pool ÷ 12 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~86.1% of bid side (2,009 resting ≥ 2,000 ✓) ≈ $3.59/day (event pool ÷ 3 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | BUY | 1.0¢ | 1,700 | 0 | $25.00 | ✅ scoring — ~85.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.31/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-sd-2026-11-03-dem` | BUY | 1.0¢ | 1,700 | 1 | $25.00 | ✅ scoring — ~84.2% of bid side (2,002 resting ≥ 2,000 ✓) ≈ $5.26/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 120 | 0 | $200.00 | ✅ scoring — ~77.6% of bid side (20,573 resting ≥ 20,000 ✓) ≈ $2.87/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 10.0¢ | 112 | 0 | $200.00 | ✅ scoring — ~75.5% of bid side (133,212 resting ≥ 20,000 ✓) ≈ $4.44/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ma-2026-11-03-rep` | BUY | 1.0¢ | 1,666 | 1 | $25.00 | ✅ scoring — ~72.6% of bid side (2,269 resting ≥ 2,000 ✓) ≈ $4.53/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 68 | 0 | $200.00 | ✅ scoring — ~71.1% of bid side (96,881 resting ≥ 20,000 ✓) ≈ $4.18/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-markel` | SELL | 11.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~66.7% of ask side (23,832 resting ≥ 20,000 ✓) ≈ $3.92/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-tn-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~66.2% of bid side (2,071 resting ≥ 2,000 ✓) ≈ $4.14/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-kamhar` | SELL | 5.0¢ | 286 | 0 | $200.00 | ✅ scoring — ~61.9% of ask side (67,326 resting ≥ 20,000 ✓) ≈ $2.29/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 93.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~60.0% of bid side (500,259 resting ≥ 2,000 ✓) ≈ $3.75/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 12.0¢ | 42 | 0 | $200.00 | ✅ scoring — ~60.0% of ask side (38,939 resting ≥ 20,000 ✓) ≈ $3.53/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 5.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~57.4% of ask side (65,541 resting ≥ 2,000 ✓) ≈ $3.59/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 5.0¢ | 79 | 0 | $100.00 | ✅ scoring — ~57.2% of ask side (77,535 resting ≥ 5,000 ✓) ≈ $2.20/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 7.0¢ | 24 | 0 | $25.00 | ✅ scoring — ~56.9% of ask side (65,569 resting ≥ 2,000 ✓) ≈ $3.55/day (event pool ÷ 2 markets) |
| …and 3230 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ussewc-usse-ks-2026-11-03-dem</code> SELL 1 @ 25¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 32¢ | 1 | ×0.1^7 = 0.0 |
|  | 34¢ | 1 | ×0.1^9 = 0.0 |
|  | 35¢ | 171 | ×0.1^10 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^73 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem` ← this one
2. `ussewc-usse-ks-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 1 @ 21¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 28¢ | 115 | ×0.2^7 = 0.0 |
|  | 29¢ | 150 | ×0.2^8 = 0.0 |
|  | 67¢ | 51 | ×0.2^46 = 0.0 |
|  | 68¢ | 1 | ×0.2^47 = 0.0 |
|  | 69¢ | 1 | ×0.2^48 = 0.0 |
|  | 70¢ | 1 | ×0.2^49 = 0.0 |
|  | 71¢ | 1 | ×0.2^50 = 0.0 |
|  | 72¢ | 1 | ×0.2^51 = 0.0 |
|  | 73¢ | 1 | ×0.2^52 = 0.0 |
| | … | +24 levels | 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.8% = $3.84/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49` ← this one
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
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> SELL 1 @ 5¢ → $6.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 9¢ | 50 | ×0.1^4 = 0.0 |
|  | 45¢ | 25 | ×0.1^40 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.5% = $6.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-ala-6pt5wins</code> BUY 0 @ 91¢ → $2.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 0 (0 yours) | ×0.5^0 = 0.5 |
|  | 73¢ | 884 | ×0.5^18 = 0.0 |
|  | 72¢ | 50 | ×0.5^19 = 0.0 |
|  | 7¢ | 52 | ×0.5^84 = 0.0 |
|  | 1¢ | 4,796 | ×0.5^90 = 0.0 |
| | | **Σ** | **0.5** |

`yours 0.5 / Σ 0.5 = 99.3%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 99.3% = $2.48/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-ala-10pt5wins`
2. `aachc-cfb-wins-2026-11-28-ala-6pt5wins` ← this one
3. `aachc-cfb-wins-2026-11-28-ala-7pt5wins`
4. `aachc-cfb-wins-2026-11-28-ala-8pt5wins`
5. `aachc-cfb-wins-2026-11-28-ala-9pt5wins`

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> SELL 1 @ 7¢ → $6.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 9¢ | 1 | ×0.1^2 = 0.0 |
|  | 12¢ | 2 | ×0.1^5 = 0.0 |
|  | 13¢ | 50 | ×0.1^6 = 0.0 |
|  | 21¢ | 1 | ×0.1^14 = 0.0 |
|  | 42¢ | 1 | ×0.1^35 = 0.0 |
|  | 48¢ | 3,000 | ×0.1^41 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.0% = $6.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 5,000 @ 1¢ → $6.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 5,100 (5,000 yours) | ×0.1^1 = 510.0 |
| | | **Σ** | **511.0** |

`yours 500.0 / Σ 511.0 = 97.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 97.8% = $6.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 86 @ 4¢ → $6.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 88 (86 yours) | ×0.2^0 = 88.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 3 | ×0.2^8 = 0.0 |
|  | 13¢ | 4 | ×0.2^9 = 0.0 |
|  | 14¢ | 55 | ×0.2^10 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^11 = 0.0 |
| | | **Σ** | **88.0** |

`yours 86.0 / Σ 88.0 = 97.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 97.7% = $6.98/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 1 @ 89¢ → $6.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 91¢ | 2 | ×0.1^2 = 0.0 |
|  | 92¢ | 4 | ×0.1^3 = 0.0 |
|  | 94¢ | 1 | ×0.1^5 = 0.0 |
|  | 98¢ | 65 | ×0.1^9 = 0.0 |
|  | 99¢ | 2,028 | ×0.1^10 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 97.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 97.7% = $6.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 8¢ → $5.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 9¢ | 1 | ×0.1^1 = 0.1 |
|  | 10¢ | 1 | ×0.1^2 = 0.0 |
|  | 11¢ | 2 | ×0.1^3 = 0.0 |
|  | 13¢ | 2 | ×0.1^5 = 0.0 |
|  | 14¢ | 2 | ×0.1^6 = 0.0 |
|  | 15¢ | 160 | ×0.1^7 = 0.0 |
|  | 18¢ | 50 | ×0.1^10 = 0.0 |
|  | 45¢ | 500 | ×0.1^37 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^90 = 0.0 |
| | | **Σ** | **2.1** |

`yours 2.0 / Σ 2.1 = 94.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.7% = $5.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-rep</code> BUY 3 @ 94¢ → $5.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 91¢ | 204 | ×0.1^3 = 0.2 |
|  | 83¢ | 3 | ×0.1^11 = 0.0 |
|  | 32¢ | 1 | ×0.1^62 = 0.0 |
|  | 10¢ | 5 | ×0.1^84 = 0.0 |
|  | 1¢ | 1,994 | ×0.1^93 = 0.0 |
| | | **Σ** | **3.2** |

`yours 3.0 / Σ 3.2 = 93.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.6% = $5.85/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem`
2. `usgubewc-usgub-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-sc-2026-11-03-dem</code> SELL 1 @ 9¢ → $5.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 1 | ×0.1^1 = 0.1 |
|  | 15¢ | 162 | ×0.1^6 = 0.0 |
|  | 17¢ | 1 | ×0.1^8 = 0.0 |
|  | 32¢ | 1 | ×0.1^23 = 0.0 |
|  | 55¢ | 0 | ×0.1^46 = 0.0 |
|  | 61¢ | 0 | ×0.1^52 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^89 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.9% = $5.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sc-2026-11-03-dem` ← this one
2. `usgubewc-usgub-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> SELL 1 @ 8¢ → $5.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 9¢ | 1 | ×0.1^1 = 0.1 |
|  | 10¢ | 1 | ×0.1^2 = 0.0 |
|  | 12¢ | 1 | ×0.1^4 = 0.0 |
|  | 15¢ | 2 | ×0.1^7 = 0.0 |
|  | 17¢ | 153 | ×0.1^9 = 0.0 |
|  | 32¢ | 5,000 | ×0.1^24 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.1% = $5.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 150 (135 yours) | ×0.2^0 = 149.6 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **150.3** |

`yours 135.0 / Σ 150.3 = 89.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 89.8% = $3.33/day`  

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
<details><summary><code>ussewc-usse-de-2026-11-03-rep</code> BUY 1,798 @ 1¢ → $5.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 5 | ×0.1^0 = 5.0 |
| ▶ | 1¢ | 1,999 (1,798 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **204.9** |

`yours 179.8 / Σ 204.9 = 87.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 87.8% = $5.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-de-2026-11-03-dem`
2. `ussewc-usse-de-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 146 @ 15¢ → $3.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 169 (146 yours) | ×0.2^0 = 169.0 |
|  | 2¢ | 5,400 | ×0.2^13 = 0.0 |
| | | **Σ** | **169.0** |

`yours 146.0 / Σ 169.0 = 86.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 86.4% = $3.60/day`  

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
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $3.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 9 | ×0.1^0 = 9.0 |
| ▶ | 1¢ | 2,000 (1,799 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **209.0** |

`yours 179.9 / Σ 209.0 = 86.1%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 86.1% = $3.59/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> BUY 1,700 @ 1¢ → $5.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (1,700 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 1,700.0 / Σ 2,000.0 = 85.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 85.0% = $5.31/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-sd-2026-11-03-dem</code> BUY 1,700 @ 1¢ → $5.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 1¢ | 2,000 (1,700 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **202.0** |

`yours 170.0 / Σ 202.0 = 84.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 84.2% = $5.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sd-2026-11-03-dem` ← this one
2. `usgubewc-usgub-sd-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 120 @ 5¢ → $2.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 121 (120 yours) | ×0.2^0 = 121.0 |
|  | 4¢ | 4 | ×0.2^1 = 0.8 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 20,443 | ×0.2^4 = 32.7 |
| | | **Σ** | **154.6** |

`yours 120.0 / Σ 154.6 = 77.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 77.6% = $2.87/day`  

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
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram` ← this one
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> BUY 112 @ 10¢ → $4.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 145 (112 yours) | ×0.2^0 = 145.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 6¢ | 255 | ×0.2^4 = 0.4 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 4¢ | 46,360 | ×0.2^6 = 3.0 |
| | | **Σ** | **148.4** |

`yours 112.0 / Σ 148.4 = 75.5%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 75.5% = $4.44/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha` ← this one
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
<details><summary><code>usgubewc-usgub-ma-2026-11-03-rep</code> BUY 1,666 @ 1¢ → $4.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 3 | ×0.1^0 = 3.0 |
| ▶ | 1¢ | 2,266 (1,666 yours) | ×0.1^1 = 226.6 |
| | | **Σ** | **229.6** |

`yours 166.6 / Σ 229.6 = 72.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 72.6% = $4.53/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem`
2. `usgubewc-usgub-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 68 @ 12¢ → $4.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 95 (68 yours) | ×0.2^0 = 95.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 8¢ | 6 | ×0.2^4 = 0.0 |
|  | 7¢ | 30 | ×0.2^5 = 0.0 |
|  | 6¢ | 112 | ×0.2^6 = 0.0 |
|  | 5¢ | 10,000 | ×0.2^7 = 0.1 |
|  | 4¢ | 13 | ×0.2^8 = 0.0 |
|  | 3¢ | 171 | ×0.2^9 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **95.6** |

`yours 68.0 / Σ 95.6 = 71.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 71.1% = $4.18/day`  

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
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut` ← this one
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> SELL 20 @ 11¢ → $3.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 16¢ | 1 | ×0.2^5 = 0.0 |
|  | 19¢ | 31 | ×0.2^8 = 0.0 |
|  | 20¢ | 1 | ×0.2^9 = 0.0 |
|  | 24¢ | 50 | ×0.2^13 = 0.0 |
|  | 25¢ | 10 | ×0.2^14 = 0.0 |
|  | 26¢ | 50 | ×0.2^15 = 0.0 |
|  | 45¢ | 50 | ×0.2^34 = 0.0 |
|  | 99¢ | 23,609 | ×0.2^88 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 66.7% = $3.92/day`  

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
11. `enwc-uspres-nom-dem-2028-markel` ← this one
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $4.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 72 | ×0.1^0 = 72.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **271.9** |

`yours 179.9 / Σ 271.9 = 66.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.2% = $4.14/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-kamhar</code> SELL 286 @ 5¢ → $2.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 462 (286 yours) | ×0.2^0 = 462.0 |
|  | 14¢ | 172 | ×0.2^9 = 0.0 |
|  | 19¢ | 31,724 | ×0.2^14 = 0.0 |
| | | **Σ** | **462.0** |

`yours 286.0 / Σ 462.0 = 61.9%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 61.9% = $2.29/day`  

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
14. `ewc-usp-2028-11-07-kamhar` ← this one
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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 3 @ 93¢ → $3.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 5 (3 yours) | ×0.1^0 = 5.0 |
|  | 84¢ | 50 | ×0.1^9 = 0.0 |
|  | 10¢ | 4 | ×0.1^83 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **5.0** |

`yours 3.0 / Σ 5.0 = 60.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.0% = $3.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> SELL 42 @ 12¢ → $3.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 70 (42 yours) | ×0.2^0 = 70.0 |
|  | 16¢ | 13 | ×0.2^4 = 0.0 |
|  | 17¢ | 62 | ×0.2^5 = 0.0 |
|  | 19¢ | 4 | ×0.2^7 = 0.0 |
|  | 26¢ | 21,040 | ×0.2^14 = 0.0 |
| | | **Σ** | **70.0** |

`yours 42.0 / Σ 70.0 = 60.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 60.0% = $3.53/day`  

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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 3 @ 5¢ → $3.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 5 (3 yours) | ×0.1^0 = 5.0 |
|  | 6¢ | 2 | ×0.1^1 = 0.2 |
|  | 7¢ | 2 | ×0.1^2 = 0.0 |
|  | 9¢ | 52 | ×0.1^4 = 0.0 |
|  | 24¢ | 1 | ×0.1^19 = 0.0 |
|  | 28¢ | 1 | ×0.1^23 = 0.0 |
|  | 98¢ | 65,253 | ×0.1^93 = 0.0 |
| | | **Σ** | **5.2** |

`yours 3.0 / Σ 5.2 = 57.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.4% = $3.59/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 79 @ 5¢ → $2.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 79 (79 yours) | ×0.2^0 = 79.0 |
|  | 6¢ | 295 | ×0.2^1 = 59.0 |
|  | 15¢ | 100 | ×0.2^10 = 0.0 |
|  | 22¢ | 50 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^92 = 0.0 |
| | | **Σ** | **138.0** |

`yours 79.0 / Σ 138.0 = 57.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 57.2% = $2.20/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46` ← this one
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 24 @ 7¢ → $3.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 42 (24 yours) | ×0.1^0 = 42.0 |
|  | 8¢ | 2 | ×0.1^1 = 0.2 |
|  | 16¢ | 50 | ×0.1^9 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^91 = 0.0 |
| | | **Σ** | **42.2** |

`yours 24.0 / Σ 42.2 = 56.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 56.9% = $3.55/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (821,996 resting) | ~43.6% | ~$32.73 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (90,110 resting) | ~58.7% | ~$14.67 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (76,837 resting) | ~15.3% | ~$11.50 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (912,900 resting) | ~5.5% | ~$4.12 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (922,976 resting) | ~5.4% | ~$4.02 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (26,950 resting) | ~5.3% | ~$4.00 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (675,847 resting) | ~4.2% | ~$3.18 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (627,873 resting) | ~11.8% | ~$2.95 |
| `ewc-usse-ne-2026-11-03-danosb` | $25.00 ÷ 3 | 0.10 | 2,000 | BUY side (83,806 resting) | ~49.4% | ~$2.06 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (541,447 resting) | ~2.7% | ~$2.00 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (75,121 resting) | ~29.0% | ~$1.82 |
| `ewc-usse-nc-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (68,834 resting) | ~6.9% | ~$1.72 |

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
| 2026-08-20 1:52 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:49 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 11:48 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 10:48 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 9:33 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 8:33 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 7:01 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 3:37 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 2:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 11:59 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
