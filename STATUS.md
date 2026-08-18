# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-18 12:34 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$329.97/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$15.68/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$13.43/day), `ewc-usgub-ga-2026-11-03-dem` (~$6.25/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$329.97/day (~$13.75/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-ok-2026-11-03-rep` | BUY | 82.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (600,365 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | BUY | 76.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (601,383 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-pa-2026-11-03-dem` | BUY | 74.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (7,228 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | BUY | 67.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,355 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 68.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,352 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 69.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,362 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `erac-usgubp-ak-adv-2026-08-18-tretay` | BUY | 26.0¢ | 20 | 0 | $500.00 | ✅ scoring — ~100.0% of bid side (16,538 resting ≥ 10,000 ✓) ≈ $13.16/day (event pool ÷ 19 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 14.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~99.4% of bid side (17,126 resting ≥ 2,000 ✓) ≈ $6.21/day (event pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 47.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~98.5% of ask side (130,877 resting ≥ 2,000 ✓) ≈ $6.16/day (event pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-dem` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~98.4% of bid side (600,269 resting ≥ 2,000 ✓) ≈ $6.15/day (event pool ÷ 2 markets) |
| `erac-usgubp-ak-adv-2026-08-18-despay` | BUY | 1.0¢ | 9,890 | 1 | $500.00 | ✅ scoring — ~95.8% of bid side (10,177 resting ≥ 10,000 ✓) ≈ $12.60/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~95.5% of bid side (42,555 resting ≥ 20,000 ✓) ≈ $3.54/day (event pool ÷ 27 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 85.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~94.8% of ask side (2,061 resting ≥ 2,000 ✓) ≈ $5.92/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-gavnew` | SELL | 14.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~94.1% of ask side (55,953 resting ≥ 20,000 ✓) ≈ $3.49/day (event pool ÷ 27 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~93.9% of bid side (2,029 resting ≥ 2,000 ✓) ≈ $5.87/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 8.0¢ | 45 | 0 | $200.00 | ✅ scoring — ~91.0% of bid side (20,044 resting ≥ 20,000 ✓) ≈ $3.37/day (event pool ÷ 27 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~90.9% of ask side (66,186 resting ≥ 2,000 ✓) ≈ $5.68/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,001 resting ≥ 2,000 ✓) ≈ $5.59/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,001 resting ≥ 2,000 ✓) ≈ $3.73/day (event pool ÷ 3 markets) |
| `ussewc-usse-co-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 0 | $25.00 | ✅ scoring — ~85.7% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $5.35/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-stasmi` | SELL | 4.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~83.3% of ask side (44,216 resting ≥ 20,000 ✓) ≈ $4.90/day (event pool ÷ 17 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (196,042 resting ≥ 2,000 ✓) ≈ $5.20/day (event pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | SELL | 4.0¢ | 75 | 1 | $25.00 | ✅ scoring — ~78.9% of ask side (2,261 resting ≥ 2,000 ✓) ≈ $1.41/day (event pool ÷ 7 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 95.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~76.9% of bid side (2,155 resting ≥ 2,000 ✓) ≈ $4.81/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | BUY | 94.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~71.6% of bid side (301,263 resting ≥ 2,000 ✓) ≈ $4.48/day (event pool ÷ 2 markets) |
| `vsc-usgubp-fl-fshbck-atl-5pct` | BUY | 92.0¢ | 30 | 0 | $500.00 | ✅ scoring — ~68.2% of bid side (60,841 resting ≥ 10,000 ✓) ≈ $17.04/day (event pool ÷ 10 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 11.0¢ | 45 | 0 | $200.00 | ✅ scoring — ~62.5% of bid side (83,703 resting ≥ 20,000 ✓) ≈ $4.46/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-aleocc` | BUY | 21.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~62.4% of bid side (76,007 resting ≥ 20,000 ✓) ≈ $3.67/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 87.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~60.0% of ask side (27,351 resting ≥ 2,000 ✓) ≈ $3.75/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | SELL | 26.0¢ | 4 | 0 | $200.00 | ✅ scoring — ~53.8% of ask side (71,751 resting ≥ 20,000 ✓) ≈ $3.16/day (event pool ÷ 17 markets) |
| …and 2014 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> BUY 3 @ 82¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 64¢ | 150 | ×0.1^18 = 0.0 |
|  | 63¢ | 4 | ×0.1^19 = 0.0 |
|  | 56¢ | 1 | ×0.1^26 = 0.0 |
|  | 35¢ | 1 | ×0.1^47 = 0.0 |
|  | 13¢ | 1 | ×0.1^69 = 0.0 |
|  | 10¢ | 5 | ×0.1^72 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^80 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem`
2. `usgubewc-usgub-ok-2026-11-03-rep` ← this one

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
|  | 2¢ | 601,000 | ×0.1^74 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-pa-2026-11-03-dem</code> BUY 3 @ 74¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 56¢ | 221 | ×0.1^18 = 0.0 |
|  | 55¢ | 4 | ×0.1^19 = 0.0 |
|  | 50¢ | 100 | ×0.1^24 = 0.0 |
|  | 2¢ | 100 | ×0.1^72 = 0.0 |
|  | 1¢ | 6,800 | ×0.1^73 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem` ← this one
2. `usgubewc-usgub-pa-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> BUY 3 @ 67¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 49¢ | 150 | ×0.1^18 = 0.0 |
|  | 39¢ | 1 | ×0.1^28 = 0.0 |
|  | 36¢ | 1 | ×0.1^31 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^65 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 3 @ 68¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 68¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 50¢ | 145 | ×0.1^18 = 0.0 |
|  | 12¢ | 4 | ×0.1^56 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^66 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 3 @ 69¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 69¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 52¢ | 4 | ×0.1^17 = 0.0 |
|  | 50¢ | 150 | ×0.1^19 = 0.0 |
|  | 22¢ | 1 | ×0.1^47 = 0.0 |
|  | 10¢ | 4 | ×0.1^59 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^67 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-tretay</code> BUY 20 @ 26¢ → $13.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 4¢ | 6,268 | ×0.2^22 = 0.0 |
|  | 3¢ | 250 | ×0.2^23 = 0.0 |
|  | 1¢ | 10,000 | ×0.2^25 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 100.0%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 100.0% = $13.16/day`  

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
15. `erac-usgubp-ak-adv-2026-08-18-mathei`
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 3 @ 14¢ → $6.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 3 (3 yours) | ×0.1^0 = 3.4 |
|  | 12¢ | 2 | ×0.1^2 = 0.0 |
|  | 10¢ | 16 | ×0.1^4 = 0.0 |
|  | 7¢ | 8 | ×0.1^7 = 0.0 |
|  | 2¢ | 15,000 | ×0.1^12 = 0.0 |
| | | **Σ** | **3.4** |

`yours 3.4 / Σ 3.4 = 99.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.4% = $6.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 1 @ 47¢ → $6.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 51¢ | 150 | ×0.1^4 = 0.0 |
|  | 92¢ | 1 | ×0.1^45 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^51 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.5% = $6.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-dem</code> BUY 3 @ 94¢ → $6.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 91¢ | 50 | ×0.1^3 = 0.1 |
|  | 60¢ | 4 | ×0.1^34 = 0.0 |
|  | 59¢ | 1 | ×0.1^35 = 0.0 |
|  | 53¢ | 1 | ×0.1^41 = 0.0 |
|  | 50¢ | 10 | ×0.1^44 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 98.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.4% = $6.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem` ← this one
2. `ussewc-usse-va-2026-11-03-rep`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-despay</code> BUY 9,890 @ 1¢ → $12.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 37 | ×0.2^0 = 37.0 |
| ▶ | 1¢ | 10,140 (9,890 yours) | ×0.2^1 = 2,028.1 |
| | | **Σ** | **2,065.1** |

`yours 1,978.1 / Σ 2,065.1 = 95.8%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 95.8% = $12.60/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro`
7. `erac-usgubp-ak-adv-2026-08-18-despay` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 135 @ 8¢ → $3.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 136 (135 yours) | ×0.2^0 = 136.0 |
|  | 6¢ | 27 | ×0.2^2 = 1.1 |
|  | 5¢ | 31 | ×0.2^3 = 0.2 |
|  | 3¢ | 10,250 | ×0.2^5 = 3.3 |
|  | 2¢ | 12,500 | ×0.2^6 = 0.8 |
| | | **Σ** | **141.4** |

`yours 135.0 / Σ 141.4 = 95.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 95.5% = $3.54/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 2 @ 85¢ → $5.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 86¢ | 1 | ×0.1^1 = 0.1 |
|  | 87¢ | 1 | ×0.1^2 = 0.0 |
|  | 91¢ | 1 | ×0.1^6 = 0.0 |
|  | 94¢ | 1 | ×0.1^9 = 0.0 |
|  | 97¢ | 1 | ×0.1^12 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-gavnew</code> SELL 1 @ 14¢ → $3.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 17¢ | 1 | ×0.2^3 = 0.0 |
|  | 22¢ | 21,155 | ×0.2^8 = 0.1 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 94.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 94.1% = $3.49/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew` ← this one
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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 10 @ 12¢ → $5.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 11¢ | 5 | ×0.1^1 = 0.5 |
|  | 10¢ | 15 | ×0.1^2 = 0.2 |
|  | 1¢ | 1,999 | ×0.1^11 = 0.0 |
| | | **Σ** | **10.7** |

`yours 10.0 / Σ 10.7 = 93.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.9% = $5.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 45 @ 8¢ → $3.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 49 (45 yours) | ×0.2^0 = 49.2 |
|  | 2¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 19,994 | ×0.2^7 = 0.3 |
| | | **Σ** | **49.5** |

`yours 45.0 / Σ 49.5 = 91.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 91.0% = $3.37/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus` ← this one
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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 2,000 (1,799 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **201.0** |

`yours 179.9 / Σ 201.0 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.59/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $3.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 2,000 (1,799 yours) | ×0.1^1 = 200.0 |
| | | **Σ** | **201.0** |

`yours 179.9 / Σ 201.0 = 89.5%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 89.5% = $3.73/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-co-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (1,799 yours) | ×0.1^0 = 2,099.7 |
| | | **Σ** | **2,099.7** |

`yours 1,799.0 / Σ 2,099.7 = 85.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 85.7% = $5.35/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem`
2. `ussewc-usse-co-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-stasmi</code> SELL 50 @ 4¢ → $4.90/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 60 (50 yours) | ×0.2^0 = 60.0 |
|  | 10¢ | 30 | ×0.2^6 = 0.0 |
|  | 11¢ | 55 | ×0.2^7 = 0.0 |
|  | 12¢ | 270 | ×0.2^8 = 0.0 |
|  | 15¢ | 4 | ×0.2^11 = 0.0 |
|  | 16¢ | 4 | ×0.2^12 = 0.0 |
|  | 19¢ | 40,992 | ×0.2^15 = 0.0 |
| | | **Σ** | **60.0** |

`yours 50.0 / Σ 60.0 = 83.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 83.3% = $4.90/day`  

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
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi` ← this one
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 10 @ 13¢ → $5.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 12 (10 yours) | ×0.1^0 = 12.0 |
|  | 15¢ | 1 | ×0.1^2 = 0.0 |
|  | 25¢ | 50 | ×0.1^12 = 0.0 |
|  | 35¢ | 3 | ×0.1^22 = 0.0 |
|  | 40¢ | 1 | ×0.1^27 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^85 = 0.0 |
| | | **Σ** | **12.0** |

`yours 10.0 / Σ 12.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> SELL 75 @ 4¢ → $1.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 4¢ | 75 (75 yours) | ×0.1^1 = 7.5 |
|  | 99¢ | 2,184 | ×0.1^96 = 0.0 |
| | | **Σ** | **9.5** |

`yours 7.5 / Σ 9.5 = 78.9%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 78.9% = $1.41/day`  

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 5 @ 95¢ → $4.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 5 (5 yours) | ×0.1^0 = 5.0 |
|  | 93¢ | 150 | ×0.1^2 = 1.5 |
|  | 17¢ | 1 | ×0.1^78 = 0.0 |
|  | 1¢ | 1,999 | ×0.1^94 = 0.0 |
| | | **Σ** | **6.5** |

`yours 5.0 / Σ 6.5 = 76.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 76.9% = $4.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> BUY 3 @ 94¢ → $4.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 92¢ | 80 | ×0.1^2 = 0.8 |
|  | 91¢ | 385 | ×0.1^3 = 0.4 |
|  | 90¢ | 45 | ×0.1^4 = 0.0 |
|  | 84¢ | 50 | ×0.1^10 = 0.0 |
|  | 54¢ | 500 | ×0.1^40 = 0.0 |
|  | 2¢ | 300,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **4.2** |

`yours 3.0 / Σ 4.2 = 71.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.6% = $4.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>vsc-usgubp-fl-fshbck-atl-5pct</code> BUY 30 @ 92¢ → $17.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 44 (30 yours) | ×0.2^0 = 44.0 |
|  | 86¢ | 30 | ×0.2^6 = 0.0 |
|  | 85¢ | 294 | ×0.2^7 = 0.0 |
|  | 82¢ | 62 | ×0.2^10 = 0.0 |
|  | 80¢ | 161 | ×0.2^12 = 0.0 |
|  | 2¢ | 50,000 | ×0.2^90 = 0.0 |
| | | **Σ** | **44.0** |

`yours 30.0 / Σ 44.0 = 68.2%`  
`$500 ÷ 10 ÷ 2 = $25.00 × 68.2% = $17.04/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 45 @ 11¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 72 (45 yours) | ×0.2^0 = 72.0 |
|  | 2¢ | 12,972 | ×0.2^9 = 0.0 |
|  | 1¢ | 70,659 | ×0.2^10 = 0.0 |
| | | **Σ** | **72.0** |

`yours 45.0 / Σ 72.0 = 62.5%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 62.5% = $4.46/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-aleocc</code> BUY 20 @ 21¢ → $3.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 18¢ | 612 | ×0.2^3 = 4.9 |
|  | 17¢ | 3,822 | ×0.2^4 = 6.1 |
|  | 13¢ | 21,250 | ×0.2^8 = 0.1 |
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
|  | 92¢ | 8 | ×0.1^5 = 0.0 |
|  | 97¢ | 5,348 | ×0.1^10 = 0.0 |
| | | **Σ** | **5.0** |

`yours 3.0 / Σ 5.0 = 60.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.0% = $3.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> SELL 4 @ 26¢ → $3.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 4 (4 yours) | ×0.2^0 = 4.0 |
|  | 30¢ | 30 | ×0.2^4 = 0.0 |
|  | 31¢ | 54 | ×0.2^5 = 0.0 |
|  | 32¢ | 52,741 | ×0.2^6 = 3.4 |
| | | **Σ** | **7.4** |

`yours 4.0 / Σ 7.4 = 53.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 53.8% = $3.16/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,996 resting) | ~62.7% | ~$15.68 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (44,882 resting) | ~53.7% | ~$13.43 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (79,901 resting) | ~8.3% | ~$6.25 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (74,853 resting) | ~92.5% | ~$5.78 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (71,526 resting) | ~5.0% | ~$3.73 |
| `ewc-usgub-ia-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (84,676 resting) | ~58.0% | ~$3.63 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (295,317 resting) | ~3.5% | ~$2.64 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (287,305 resting) | ~2.6% | ~$1.97 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (631,946 resting) | ~6.7% | ~$1.66 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,756 resting) | ~1.7% | ~$1.24 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (65,688 resting) | ~4.7% | ~$1.18 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,244,744 resting) | ~18.0% | ~$1.13 |

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
| 2026-08-18 12:34 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 11:57 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 10:56 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 7:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:22 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 5:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 4:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 3:39 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
