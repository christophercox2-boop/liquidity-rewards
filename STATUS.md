# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-18 1:26 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$341.14/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$17.66/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$13.52/day), `ewc-usgub-oh-2026-11-03-rep` (~$12.38/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$341.14/day (~$14.21/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `erac-usgubp-ak-adv-2026-08-18-tretay` | BUY | 26.0¢ | 20 | 0 | $500.00 | ✅ scoring — ~100.0% of bid side (16,538 resting ≥ 10,000 ✓) ≈ $13.16/day (event pool ÷ 19 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | BUY | 83.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (700,253 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 14.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (17,109 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 94.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~99.9% of bid side (500,256 resting ≥ 2,000 ✓) ≈ $6.24/day (event pool ÷ 2 markets) |
| `vsc-usgubp-fl-fshbck-atl-17pct` | BUY | 20.0¢ | 10 | 0 | $500.00 | ✅ scoring — ~99.8% of bid side (10,979 resting ≥ 10,000 ✓) ≈ $24.94/day (event pool ÷ 10 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 12.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~99.7% of bid side (103,633 resting ≥ 20,000 ✓) ≈ $7.12/day (event pool ÷ 14 markets) |
| `vsc-usgubp-fl-fshbck-atl-5pct` | BUY | 92.0¢ | 30 | 0 | $500.00 | ✅ scoring — ~99.6% of bid side (60,911 resting ≥ 10,000 ✓) ≈ $24.90/day (event pool ÷ 10 markets) |
| `erac-usgubp-ak-adv-2026-08-18-mathei` | BUY | 1.0¢ | 9,899 | 0 | $500.00 | ✅ scoring — ~97.5% of bid side (10,149 resting ≥ 10,000 ✓) ≈ $12.83/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~97.5% of bid side (32,655 resting ≥ 20,000 ✓) ≈ $3.61/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~96.8% of bid side (20,134 resting ≥ 20,000 ✓) ≈ $3.58/day (event pool ÷ 27 markets) |
| `erac-usgubp-ak-adv-2026-08-18-despay` | BUY | 1.0¢ | 9,890 | 1 | $500.00 | ✅ scoring — ~95.8% of bid side (10,177 resting ≥ 10,000 ✓) ≈ $12.60/day (event pool ÷ 19 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 85.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~94.7% of ask side (2,060 resting ≥ 2,000 ✓) ≈ $5.92/day (event pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~93.9% of bid side (4,244 resting ≥ 2,000 ✓) ≈ $5.87/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-micoba` | SELL | 4.0¢ | 42 | 0 | $200.00 | ✅ scoring — ~84.1% of ask side (43,140 resting ≥ 20,000 ✓) ≈ $4.95/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-al-2026-11-03-dem` | SELL | 7.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (133,960 resting ≥ 2,000 ✓) ≈ $5.21/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-tn-2026-11-03-dem` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~80.3% of ask side (2,075 resting ≥ 2,000 ✓) ≈ $5.02/day (event pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | SELL | 4.0¢ | 75 | 1 | $25.00 | ✅ scoring — ~78.9% of ask side (2,261 resting ≥ 2,000 ✓) ≈ $1.41/day (event pool ÷ 7 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~76.6% of bid side (2,035 resting ≥ 2,000 ✓) ≈ $3.19/day (event pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 8.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~72.5% of bid side (15,650 resting ≥ 5,000 ✓) ≈ $2.79/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | SELL | 95.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~72.3% of ask side (2,500 resting ≥ 2,000 ✓) ≈ $4.52/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 4.0¢ | 61 | 0 | $200.00 | ✅ scoring — ~70.9% of ask side (38,953 resting ≥ 20,000 ✓) ≈ $4.17/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-aleocc` | BUY | 21.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~70.7% of bid side (68,655 resting ≥ 20,000 ✓) ≈ $4.16/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | BUY | 21.0¢ | 15 | 0 | $200.00 | ✅ scoring — ~70.7% of bid side (168,566 resting ≥ 20,000 ✓) ≈ $4.16/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | SELL | 6.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~70.2% of ask side (48,578 resting ≥ 20,000 ✓) ≈ $4.13/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-ma-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 0 | $25.00 | ✅ scoring — ~68.1% of bid side (2,643 resting ≥ 2,000 ✓) ≈ $4.25/day (event pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~62.3% of ask side (66,189 resting ≥ 2,000 ✓) ≈ $3.89/day (event pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 8.0¢ | 1 | 1 | $100.00 | ✅ scoring — ~60.6% of bid side (305,761 resting ≥ 5,000 ✓) ≈ $2.33/day (event pool ÷ 13 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 87.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~60.0% of ask side (27,343 resting ≥ 2,000 ✓) ≈ $3.75/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 9.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~58.8% of ask side (46,860 resting ≥ 20,000 ✓) ≈ $2.18/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-dontrujr` | SELL | 10.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~57.1% of ask side (71,769 resting ≥ 20,000 ✓) ≈ $2.12/day (event pool ÷ 27 markets) |
| …and 2004 more | | | | | | |

**Tap an order for its book window and the math:**

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
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> BUY 3 @ 83¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 83¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 75¢ | 50 | ×0.1^8 = 0.0 |
|  | 2¢ | 700,000 | ×0.1^81 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 3 @ 14¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 3 (3 yours) | ×0.1^0 = 3.4 |
|  | 10¢ | 1 | ×0.1^4 = 0.0 |
|  | 7¢ | 8 | ×0.1^7 = 0.0 |
|  | 2¢ | 15,000 | ×0.1^12 = 0.0 |
| | | **Σ** | **3.4** |

`yours 3.4 / Σ 3.4 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 5 @ 94¢ → $6.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 5 (5 yours) | ×0.1^0 = 5.0 |
|  | 90¢ | 50 | ×0.1^4 = 0.0 |
|  | 36¢ | 1 | ×0.1^58 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 99.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.9% = $6.24/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>vsc-usgubp-fl-fshbck-atl-17pct</code> BUY 10 @ 20¢ → $24.94/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 15¢ | 50 | ×0.2^5 = 0.0 |
|  | 14¢ | 55 | ×0.2^6 = 0.0 |
|  | 13¢ | 250 | ×0.2^7 = 0.0 |
|  | 9¢ | 414 | ×0.2^11 = 0.0 |
|  | 1¢ | 10,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.8%`  
`$500 ÷ 10 ÷ 2 = $25.00 × 99.8% = $24.94/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vsc-usgubp-fl-fshbck-atl-11pct`
2. `vsc-usgubp-fl-fshbck-atl-13pct`
3. `vsc-usgubp-fl-fshbck-atl-15pct`
4. `vsc-usgubp-fl-fshbck-atl-17pct` ← this one
5. `vsc-usgubp-fl-fshbck-atl-19pct`
6. `vsc-usgubp-fl-fshbck-atl-21pct`
7. `vsc-usgubp-fl-fshbck-atl-30pct`
8. `vsc-usgubp-fl-fshbck-atl-5pct`
9. `vsc-usgubp-fl-fshbck-atl-7pct`
10. `vsc-usgubp-fl-fshbck-atl-9pct`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 1 @ 12¢ → $7.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 5¢ | 1 | ×0.2^7 = 0.0 |
|  | 2¢ | 12,972 | ×0.2^10 = 0.0 |
|  | 1¢ | 90,659 | ×0.2^11 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 99.7% = $7.12/day`  

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
<details><summary><code>vsc-usgubp-fl-fshbck-atl-5pct</code> BUY 30 @ 92¢ → $24.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 30 (30 yours) | ×0.2^0 = 30.0 |
|  | 89¢ | 14 | ×0.2^3 = 0.1 |
|  | 85¢ | 294 | ×0.2^7 = 0.0 |
|  | 82¢ | 62 | ×0.2^10 = 0.0 |
|  | 80¢ | 161 | ×0.2^12 = 0.0 |
|  | 2¢ | 50,100 | ×0.2^90 = 0.0 |
| | | **Σ** | **30.1** |

`yours 30.0 / Σ 30.1 = 99.6%`  
`$500 ÷ 10 ÷ 2 = $25.00 × 99.6% = $24.90/day`  

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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-mathei</code> BUY 9,899 @ 1¢ → $12.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 10,149 (9,899 yours) | ×0.2^0 = 10,149.1 |
| | | **Σ** | **10,149.1** |

`yours 9,899.1 / Σ 10,149.1 = 97.5%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 97.5% = $12.83/day`  

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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 135 @ 8¢ → $3.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 136 (135 yours) | ×0.2^0 = 136.0 |
|  | 6¢ | 27 | ×0.2^2 = 1.1 |
|  | 5¢ | 31 | ×0.2^3 = 0.2 |
|  | 3¢ | 250 | ×0.2^5 = 0.1 |
|  | 2¢ | 12,500 | ×0.2^6 = 0.8 |
|  | 1¢ | 19,711 | ×0.2^7 = 0.3 |
| | | **Σ** | **138.5** |

`yours 135.0 / Σ 138.5 = 97.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 97.5% = $3.61/day`  

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
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 135 @ 8¢ → $3.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 139 (135 yours) | ×0.2^0 = 139.2 |
|  | 2¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 19,994 | ×0.2^7 = 0.3 |
| | | **Σ** | **139.5** |

`yours 135.0 / Σ 139.5 = 96.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 96.8% = $3.58/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 2 @ 85¢ → $5.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 86¢ | 1 | ×0.1^1 = 0.1 |
|  | 87¢ | 1 | ×0.1^2 = 0.0 |
|  | 88¢ | 1 | ×0.1^3 = 0.0 |
|  | 89¢ | 1 | ×0.1^4 = 0.0 |
|  | 98¢ | 55 | ×0.1^13 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^14 = 0.0 |
| | | **Σ** | **2.1** |

`yours 2.0 / Σ 2.1 = 94.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.7% = $5.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 2 @ 7¢ → $5.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 6¢ | 1 | ×0.1^1 = 0.1 |
|  | 3¢ | 243 | ×0.1^4 = 0.0 |
|  | 2¢ | 200 | ×0.1^5 = 0.0 |
|  | 1¢ | 3,798 | ×0.1^6 = 0.0 |
| | | **Σ** | **2.1** |

`yours 2.0 / Σ 2.1 = 93.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.9% = $5.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-micoba</code> SELL 42 @ 4¢ → $4.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 50 (42 yours) | ×0.2^0 = 50.5 |
|  | 9¢ | 53 | ×0.2^5 = 0.0 |
|  | 14¢ | 31 | ×0.2^10 = 0.0 |
|  | 15¢ | 1 | ×0.2^11 = 0.0 |
|  | 16¢ | 4 | ×0.2^12 = 0.0 |
|  | 17¢ | 40,200 | ×0.2^13 = 0.0 |
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
|  | 98¢ | 132,818 | ×0.1^91 = 0.0 |
| | | **Σ** | **12.0** |

`yours 10.0 / Σ 12.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem` ← this one
2. `usgubewc-usgub-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-dem</code> SELL 1 @ 5¢ → $5.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 7¢ | 24 | ×0.1^2 = 0.2 |
|  | 9¢ | 50 | ×0.1^4 = 0.0 |
|  | 58¢ | 1 | ×0.1^53 = 0.0 |
|  | 99¢ | 1,999 | ×0.1^94 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 80.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.3% = $5.02/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tn-2026-11-03-rep`

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1 @ 8¢ → $2.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 6¢ | 0 | ×0.2^2 = 0.0 |
|  | 4¢ | 3 | ×0.2^4 = 0.0 |
|  | 2¢ | 5,200 | ×0.2^6 = 0.3 |
| | | **Σ** | **1.4** |

`yours 1.0 / Σ 1.4 = 72.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 72.5% = $2.79/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54` ← this one
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> SELL 3 @ 95¢ → $4.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 98¢ | 1,000 | ×0.1^3 = 1.0 |
|  | 99¢ | 1,497 | ×0.1^4 = 0.1 |
| | | **Σ** | **4.1** |

`yours 3.0 / Σ 4.1 = 72.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 72.3% = $4.52/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> SELL 61 @ 4¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 86 (61 yours) | ×0.2^0 = 86.0 |
|  | 16¢ | 73 | ×0.2^12 = 0.0 |
|  | 19¢ | 4 | ×0.2^15 = 0.0 |
|  | 26¢ | 21,040 | ×0.2^22 = 0.0 |
| | | **Σ** | **86.0** |

`yours 61.0 / Σ 86.0 = 70.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 70.9% = $4.17/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-aleocc</code> BUY 20 @ 21¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 18¢ | 612 | ×0.2^3 = 4.9 |
|  | 17¢ | 1,470 | ×0.2^4 = 2.4 |
|  | 13¢ | 16,250 | ×0.2^8 = 0.0 |
|  | 1¢ | 50,303 | ×0.2^20 = 0.0 |
| | | **Σ** | **28.3** |

`yours 20.0 / Σ 28.3 = 70.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 70.7% = $4.16/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> BUY 15 @ 21¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 19¢ | 8 | ×0.2^2 = 0.3 |
|  | 18¢ | 21 | ×0.2^3 = 0.2 |
|  | 17¢ | 296 | ×0.2^4 = 0.5 |
|  | 16¢ | 16,110 | ×0.2^5 = 5.2 |
|  | 15¢ | 1,666 | ×0.2^6 = 0.1 |
|  | 2¢ | 250 | ×0.2^19 = 0.0 |
|  | 1¢ | 150,200 | ×0.2^20 = 0.0 |
| | | **Σ** | **21.2** |

`yours 15.0 / Σ 21.2 = 70.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 70.7% = $4.16/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew` ← this one
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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> SELL 1 @ 6¢ → $4.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 10¢ | 8 | ×0.2^4 = 0.0 |
|  | 13¢ | 32,097 | ×0.2^7 = 0.4 |
| | | **Σ** | **1.4** |

`yours 1.0 / Σ 1.4 = 70.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 70.2% = $4.13/day`  

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
<details><summary><code>usgubewc-usgub-ma-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $4.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,643 (1,799 yours) | ×0.1^0 = 2,643.0 |
| | | **Σ** | **2,643.0** |

`yours 1,799.0 / Σ 2,643.0 = 68.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 68.1% = $4.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem`
2. `usgubewc-usgub-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 2 @ 7¢ → $3.89/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 3 (2 yours) | ×0.1^0 = 3.0 |
|  | 8¢ | 2 | ×0.1^1 = 0.2 |
|  | 9¢ | 1 | ×0.1^2 = 0.0 |
|  | 13¢ | 1 | ×0.1^6 = 0.0 |
|  | 15¢ | 157 | ×0.1^8 = 0.0 |
|  | 18¢ | 50 | ×0.1^11 = 0.0 |
|  | 45¢ | 500 | ×0.1^38 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^91 = 0.0 |
| | | **Σ** | **3.2** |

`yours 2.0 / Σ 3.2 = 62.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 62.3% = $3.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 8¢ → $2.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 8¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 5¢ | 1 | ×0.2^4 = 0.0 |
|  | 4¢ | 5 | ×0.2^5 = 0.0 |
|  | 3¢ | 2 | ×0.2^6 = 0.0 |
|  | 2¢ | 5,200 | ×0.2^7 = 0.1 |
| | | **Σ** | **0.3** |

`yours 0.2 / Σ 0.3 = 60.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 60.6% = $2.33/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 3 @ 9¢ → $2.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 3 (3 yours) | ×0.2^0 = 3.0 |
|  | 10¢ | 2 | ×0.2^1 = 0.4 |
|  | 13¢ | 5 | ×0.2^4 = 0.0 |
|  | 15¢ | 26,429 | ×0.2^6 = 1.7 |
| | | **Σ** | **5.1** |

`yours 3.0 / Σ 5.1 = 58.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 58.8% = $2.18/day`  

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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> SELL 50 @ 10¢ → $2.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 73 (50 yours) | ×0.2^0 = 73.0 |
|  | 11¢ | 73 | ×0.2^1 = 14.5 |
|  | 20¢ | 300 | ×0.2^10 = 0.0 |
|  | 21¢ | 51,071 | ×0.2^11 = 0.0 |
| | | **Σ** | **87.5** |

`yours 50.0 / Σ 87.5 = 57.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 57.1% = $2.12/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr` ← this one
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
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,695 resting) | ~70.7% | ~$17.66 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (43,578 resting) | ~54.1% | ~$13.52 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (272,860 resting) | ~16.5% | ~$12.38 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (79,900 resting) | ~14.2% | ~$10.64 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (66,405 resting) | ~13.3% | ~$9.95 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (74,540 resting) | ~79.7% | ~$4.98 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (62,552 resting) | ~12.6% | ~$3.16 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (629,637 resting) | ~11.7% | ~$2.92 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,184 resting) | ~3.0% | ~$2.27 |
| `ewc-usse-nc-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (51,030 resting) | ~8.5% | ~$2.12 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (147,029 resting) | ~8.4% | ~$2.09 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,243,693 resting) | ~21.5% | ~$1.35 |

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
| 2026-08-18 1:26 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 12:44 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 12:34 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 11:57 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 10:56 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 8:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 7:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:22 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 5:40 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
