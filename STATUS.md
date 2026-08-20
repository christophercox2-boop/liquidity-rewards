# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 12:49 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$514.09/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `paccc-usho-midterms-2026-11-03-rep` — BUY at the best price, ~$27.21/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$13.56/day), `ewc-usgub-ga-2026-11-03-dem` (~$11.40/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$514.09/day (~$21.42/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 93.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,257 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-ks-2026-11-03-rep` | BUY | 77.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,767 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `aachc-cfb-wins-2026-11-28-bayl-4pt5wins` | BUY | 87.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (6,440 resting ≥ 5,000 ✓) ≈ $2.50/day (event pool ÷ 5 markets) |
| `usgubewc-usgub-al-2026-11-03-dem` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (134,096 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-dem` | SELL | 6.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (268,901 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 21.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,894 resting ≥ 5,000 ✓) ≈ $3.84/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-nh-2026-11-03-rep` | BUY | 82.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (5,498 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | SELL | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.8% of ask side (69,139 resting ≥ 2,000 ✓) ≈ $6.24/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nh-2026-11-03-rep` | SELL | 84.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.7% of ask side (5,504 resting ≥ 2,000 ✓) ≈ $6.23/day (event pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 89.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.7% of ask side (2,098 resting ≥ 2,000 ✓) ≈ $6.23/day (event pool ÷ 2 markets) |
| `ussewc-usse-ks-2026-11-03-rep` | SELL | 84.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.6% of ask side (2,321 resting ≥ 2,000 ✓) ≈ $6.22/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-sc-2026-11-03-dem` | SELL | 11.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~98.2% of ask side (196,351 resting ≥ 2,000 ✓) ≈ $6.14/day (event pool ÷ 2 markets) |
| `ussewc-usse-ks-2026-11-03-dem` | SELL | 25.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~98.0% of ask side (130,899 resting ≥ 2,000 ✓) ≈ $6.13/day (event pool ÷ 2 markets) |
| `aachc-cfb-wins-2026-11-28-uk-5pt5wins` | BUY | 43.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~97.7% of bid side (18,780 resting ≥ 5,000 ✓) ≈ $2.44/day (event pool ÷ 5 markets) |
| `usgubewc-usgub-sd-2026-11-03-dem` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~97.6% of ask side (2,098 resting ≥ 2,000 ✓) ≈ $6.10/day (event pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 5,000 | 1 | $25.00 | ✅ scoring — ~96.0% of bid side (5,202 resting ≥ 2,000 ✓) ≈ $6.00/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-or-2026-11-03-dem` | SELL | 91.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~95.0% of ask side (2,200 resting ≥ 2,000 ✓) ≈ $5.94/day (event pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 8.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~94.7% of ask side (66,195 resting ≥ 2,000 ✓) ≈ $5.92/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 86 | 1 | $200.00 | ✅ scoring — ~92.4% of ask side (44,792 resting ≥ 20,000 ✓) ≈ $6.60/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 9.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~89.9% of ask side (130,827 resting ≥ 2,000 ✓) ≈ $5.62/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~89.0% of bid side (50,362 resting ≥ 20,000 ✓) ≈ $3.30/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-ny-2026-11-03-rep` | SELL | 9.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~88.6% of ask side (77,715 resting ≥ 2,000 ✓) ≈ $5.54/day (event pool ÷ 2 markets) |
| `ussewc-usse-de-2026-11-03-rep` | BUY | 1.0¢ | 1,798 | 1 | $25.00 | ✅ scoring — ~87.8% of bid side (2,004 resting ≥ 2,000 ✓) ≈ $5.48/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 15.0¢ | 146 | 0 | $100.00 | ✅ scoring — ~86.4% of bid side (805,769 resting ≥ 5,000 ✓) ≈ $3.60/day (event pool ÷ 12 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~86.1% of bid side (2,009 resting ≥ 2,000 ✓) ≈ $3.59/day (event pool ÷ 3 markets) |
| `ussewc-usse-ma-2026-11-03-rep` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~82.1% of ask side (65,637 resting ≥ 2,000 ✓) ≈ $5.13/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 88.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~82.0% of ask side (64,913 resting ≥ 2,000 ✓) ≈ $5.12/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 120 | 0 | $200.00 | ✅ scoring — ~77.6% of bid side (20,573 resting ≥ 20,000 ✓) ≈ $2.87/day (event pool ÷ 27 markets) |
| `ussewc-usse-il-2026-11-03-rep` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~76.0% of ask side (330,240 resting ≥ 2,000 ✓) ≈ $4.75/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | BUY | 10.0¢ | 112 | 0 | $200.00 | ✅ scoring — ~75.5% of bid side (133,212 resting ≥ 20,000 ✓) ≈ $4.44/day (event pool ÷ 17 markets) |
| …and 3211 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 3 @ 93¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 84¢ | 50 | ×0.1^9 = 0.0 |
|  | 10¢ | 4 | ×0.1^83 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ks-2026-11-03-rep</code> BUY 5 @ 77¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 5 (5 yours) | ×0.1^0 = 5.0 |
|  | 71¢ | 75 | ×0.1^6 = 0.0 |
|  | 70¢ | 325 | ×0.1^7 = 0.0 |
|  | 66¢ | 112 | ×0.1^11 = 0.0 |
|  | 65¢ | 50 | ×0.1^12 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^75 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem`
2. `ussewc-usse-ks-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-bayl-4pt5wins</code> BUY 0 @ 87¢ → $2.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 62¢ | 200 | ×0.5^25 = 0.0 |
|  | 61¢ | 50 | ×0.5^26 = 0.0 |
|  | 4¢ | 53 | ×0.5^83 = 0.0 |
|  | 1¢ | 6,137 | ×0.5^86 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 100.0%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 100.0% = $2.50/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-bayl-4pt5wins` ← this one
2. `aachc-cfb-wins-2026-11-28-bayl-5pt5wins`
3. `aachc-cfb-wins-2026-11-28-bayl-6pt5wins`
4. `aachc-cfb-wins-2026-11-28-bayl-7pt5wins`
5. `aachc-cfb-wins-2026-11-28-bayl-8pt5wins`

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-dem</code> SELL 1 @ 5¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 9¢ | 1 | ×0.1^4 = 0.0 |
|  | 12¢ | 1 | ×0.1^7 = 0.0 |
|  | 13¢ | 1 | ×0.1^8 = 0.0 |
|  | 14¢ | 3 | ×0.1^9 = 0.0 |
|  | 15¢ | 0 | ×0.1^10 = 0.0 |
|  | 16¢ | 140 | ×0.1^11 = 0.0 |
|  | 21¢ | 406 | ×0.1^16 = 0.0 |
|  | 22¢ | 500 | ×0.1^17 = 0.0 |
|  | 98¢ | 132,818 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem` ← this one
2. `usgubewc-usgub-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-dem</code> SELL 1 @ 6¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 1 | ×0.1^4 = 0.0 |
|  | 14¢ | 52 | ×0.1^8 = 0.0 |
|  | 17¢ | 55 | ×0.1^11 = 0.0 |
|  | 18¢ | 1,000 | ×0.1^12 = 0.0 |
|  | 36¢ | 0 | ×0.1^30 = 0.0 |
|  | 40¢ | 2,000 | ×0.1^34 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem` ← this one
2. `ussewc-usse-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 1 @ 21¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 29¢ | 150 | ×0.2^8 = 0.0 |
|  | 67¢ | 51 | ×0.2^46 = 0.0 |
|  | 68¢ | 1 | ×0.2^47 = 0.0 |
|  | 69¢ | 1 | ×0.2^48 = 0.0 |
|  | 70¢ | 1 | ×0.2^49 = 0.0 |
|  | 71¢ | 1 | ×0.2^50 = 0.0 |
|  | 72¢ | 1 | ×0.2^51 = 0.0 |
|  | 73¢ | 1 | ×0.2^52 = 0.0 |
|  | 74¢ | 1 | ×0.2^53 = 0.0 |
| | … | +23 levels | 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.84/day`  

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
<details><summary><code>usgubewc-usgub-nh-2026-11-03-rep</code> BUY 1 @ 82¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 77¢ | 47 | ×0.1^5 = 0.0 |
|  | 64¢ | 150 | ×0.1^18 = 0.0 |
|  | 50¢ | 100 | ×0.1^32 = 0.0 |
|  | 1¢ | 5,200 | ×0.1^81 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nh-2026-11-03-dem`
2. `usgubewc-usgub-nh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> SELL 1 @ 8¢ → $6.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 12¢ | 2 | ×0.1^4 = 0.0 |
|  | 13¢ | 159 | ×0.1^5 = 0.0 |
|  | 21¢ | 1 | ×0.1^13 = 0.0 |
|  | 42¢ | 1 | ×0.1^34 = 0.0 |
|  | 48¢ | 3,000 | ×0.1^40 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.8% = $6.24/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nh-2026-11-03-rep</code> SELL 1 @ 84¢ → $6.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 88¢ | 28 | ×0.1^4 = 0.0 |
|  | 90¢ | 150 | ×0.1^6 = 0.0 |
|  | 97¢ | 100 | ×0.1^13 = 0.0 |
|  | 99¢ | 5,225 | ×0.1^15 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.7% = $6.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nh-2026-11-03-dem`
2. `usgubewc-usgub-nh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 1 @ 89¢ → $6.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 92¢ | 3 | ×0.1^3 = 0.0 |
|  | 96¢ | 1 | ×0.1^7 = 0.0 |
|  | 98¢ | 65 | ×0.1^9 = 0.0 |
|  | 99¢ | 2,028 | ×0.1^10 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.7% = $6.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ks-2026-11-03-rep</code> SELL 1 @ 84¢ → $6.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 87¢ | 1 | ×0.1^3 = 0.0 |
|  | 89¢ | 325 | ×0.1^5 = 0.0 |
|  | 92¢ | 1 | ×0.1^8 = 0.0 |
|  | 97¢ | 50 | ×0.1^13 = 0.0 |
|  | 99¢ | 1,943 | ×0.1^15 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.6% = $6.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem`
2. `ussewc-usse-ks-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-sc-2026-11-03-dem</code> SELL 1 @ 11¢ → $6.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 15¢ | 162 | ×0.1^4 = 0.0 |
|  | 16¢ | 211 | ×0.1^5 = 0.0 |
|  | 17¢ | 1 | ×0.1^6 = 0.0 |
|  | 32¢ | 1 | ×0.1^21 = 0.0 |
|  | 55¢ | 0 | ×0.1^44 = 0.0 |
|  | 61¢ | 0 | ×0.1^50 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^87 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.2% = $6.14/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sc-2026-11-03-dem` ← this one
2. `usgubewc-usgub-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ks-2026-11-03-dem</code> SELL 1 @ 25¢ → $6.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 27¢ | 2 | ×0.1^2 = 0.0 |
|  | 35¢ | 171 | ×0.1^10 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^73 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.0% = $6.13/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem` ← this one
2. `ussewc-usse-ks-2026-11-03-rep`

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-uk-5pt5wins</code> BUY 2 @ 43¢ → $2.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 2 (2 yours) | ×0.5^0 = 2.0 |
|  | 41¢ | 0 | ×0.5^2 = 0.0 |
|  | 22¢ | 2,472 | ×0.5^21 = 0.0 |
|  | 21¢ | 50 | ×0.5^22 = 0.0 |
|  | 17¢ | 42 | ×0.5^26 = 0.0 |
|  | 16¢ | 16,000 | ×0.5^27 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 97.7%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 97.7% = $2.44/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-uk-2pt5wins`
2. `aachc-cfb-wins-2026-11-28-uk-3pt5wins`
3. `aachc-cfb-wins-2026-11-28-uk-4pt5wins`
4. `aachc-cfb-wins-2026-11-28-uk-5pt5wins` ← this one
5. `aachc-cfb-wins-2026-11-28-uk-6pt5wins`

</details>

</details>
<details><summary><code>usgubewc-usgub-sd-2026-11-03-dem</code> SELL 1 @ 5¢ → $6.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 7¢ | 1 | ×0.1^2 = 0.0 |
|  | 9¢ | 150 | ×0.1^4 = 0.0 |
|  | 13¢ | 325 | ×0.1^8 = 0.0 |
|  | 99¢ | 1,621 | ×0.1^94 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 97.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 97.6% = $6.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sd-2026-11-03-dem` ← this one
2. `usgubewc-usgub-sd-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 5,000 @ 1¢ → $6.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.1^1 = 520.1 |
| | | **Σ** | **521.1** |

`yours 500.0 / Σ 521.1 = 96.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 96.0% = $6.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-or-2026-11-03-dem</code> SELL 1 @ 91¢ → $5.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 95¢ | 524 | ×0.1^4 = 0.1 |
|  | 99¢ | 1,675 | ×0.1^8 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 95.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 95.0% = $5.94/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-or-2026-11-03-dem` ← this one
2. `usgubewc-usgub-or-2026-11-03-rep`

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 86 @ 4¢ → $6.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 4¢ | 88 (86 yours) | ×0.2^1 = 17.6 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 6 | ×0.2^10 = 0.0 |
|  | 14¢ | 55 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **18.6** |

`yours 17.2 / Σ 18.6 = 92.4%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 92.4% = $6.60/day`  

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
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 1 @ 9¢ → $5.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 10¢ | 1 | ×0.1^1 = 0.1 |
|  | 11¢ | 1 | ×0.1^2 = 0.0 |
|  | 12¢ | 1 | ×0.1^3 = 0.0 |
|  | 14¢ | 90 | ×0.1^5 = 0.0 |
|  | 43¢ | 1 | ×0.1^34 = 0.0 |
|  | 51¢ | 3 | ×0.1^42 = 0.0 |
|  | 64¢ | 1 | ×0.1^55 = 0.0 |
|  | 98¢ | 130,503 | ×0.1^89 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 89.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.9% = $5.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 151 (135 yours) | ×0.2^0 = 151.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **151.7** |

`yours 135.0 / Σ 151.7 = 89.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 89.0% = $3.30/day`  

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
<details><summary><code>usgubewc-usgub-ny-2026-11-03-rep</code> SELL 1 @ 9¢ → $5.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 13¢ | 1,189 | ×0.1^4 = 0.1 |
|  | 14¢ | 1,000 | ×0.1^5 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 88.6% = $5.54/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem`
2. `usgubewc-usgub-ny-2026-11-03-rep` ← this one

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
<details><summary><code>ussewc-usse-ma-2026-11-03-rep</code> SELL 1 @ 5¢ → $5.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 6¢ | 2 | ×0.1^1 = 0.2 |
|  | 8¢ | 2 | ×0.1^3 = 0.0 |
|  | 9¢ | 153 | ×0.1^4 = 0.0 |
|  | 75¢ | 1 | ×0.1^70 = 0.0 |
|  | 98¢ | 65,253 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 82.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 82.1% = $5.13/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem`
2. `ussewc-usse-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 1 @ 88¢ → $5.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 89¢ | 2 | ×0.1^1 = 0.2 |
|  | 90¢ | 2 | ×0.1^2 = 0.0 |
|  | 97¢ | 4,978 | ×0.1^9 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 82.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 82.0% = $5.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

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
<details><summary><code>ussewc-usse-il-2026-11-03-rep</code> SELL 1 @ 5¢ → $4.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 6¢ | 3 | ×0.1^1 = 0.3 |
|  | 7¢ | 1 | ×0.1^2 = 0.0 |
|  | 8¢ | 1 | ×0.1^3 = 0.0 |
|  | 9¢ | 53 | ×0.1^4 = 0.0 |
|  | 29¢ | 1 | ×0.1^24 = 0.0 |
|  | 44¢ | 1 | ×0.1^39 = 0.0 |
|  | 48¢ | 1 | ×0.1^43 = 0.0 |
|  | 60¢ | 1 | ×0.1^55 = 0.0 |
|  | 98¢ | 132,789 | ×0.1^93 = 0.0 |
| | | **Σ** | **1.3** |

`yours 1.0 / Σ 1.3 = 76.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 76.0% = $4.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem`
2. `ussewc-usse-il-2026-11-03-rep` ← this one

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (822,139 resting) | ~36.3% | ~$27.21 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (91,105 resting) | ~54.2% | ~$13.56 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (76,849 resting) | ~15.2% | ~$11.40 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (912,725 resting) | ~7.7% | ~$5.77 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (918,481 resting) | ~7.2% | ~$5.41 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (26,431 resting) | ~6.3% | ~$4.70 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (676,737 resting) | ~4.2% | ~$3.18 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (630,063 resting) | ~9.2% | ~$2.31 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (541,417 resting) | ~2.7% | ~$2.01 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (75,265 resting) | ~29.5% | ~$1.84 |
| `ewc-usse-ne-2026-11-03-danosb` | $25.00 ÷ 3 | 0.10 | 2,000 | BUY side (83,494 resting) | ~42.5% | ~$1.77 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (82,928 resting) | ~6.8% | ~$1.70 |

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
| 2026-08-20 12:49 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 11:48 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 10:48 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 9:33 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 8:33 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 7:01 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 3:37 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 2:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 11:59 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 10:58 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
