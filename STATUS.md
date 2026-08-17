# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-17 7:50 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$300.28/day estimated (ceiling, not promise — details below)

**Earned:** $4,920.49 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** · 2026-08-13: **$223.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$8.21/day for 200 contracts. Runners-up: `enwc-usgubp-fl-2026-08-18-rep-jaycol` (~$3.47/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$2.31/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$300.28/day (~$12.51/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `erac-usgubp-ak-adv-2026-08-18-lesmcg` | SELL | 50.0¢ | 100 | 0 | $500.00 | ✅ scoring — ~100.0% of ask side (10,561 resting ≥ 10,000 ✓) ≈ $13.16/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-grebre` | SELL | 50.0¢ | 100 | 0 | $500.00 | ✅ scoring — ~100.0% of ask side (10,292 resting ≥ 10,000 ✓) ≈ $13.16/day (event pool ÷ 19 markets) |
| `vsc-usgubp-fl-fshbck-atl-5pct` | BUY | 96.0¢ | 1 | 0 | $500.00 | ✅ scoring — ~100.0% of bid side (10,428 resting ≥ 10,000 ✓) ≈ $25.00/day (event pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 15.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (805,598 resting ≥ 5,000 ✓) ≈ $4.17/day (event pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 15.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (55,508 resting ≥ 5,000 ✓) ≈ $3.84/day (event pool ÷ 13 markets) |
| `erac-usgubp-ak-adv-2026-08-18-bruwal` | SELL | 14.0¢ | 15 | 0 | $500.00 | ✅ scoring — ~99.5% of ask side (18,527 resting ≥ 10,000 ✓) ≈ $13.09/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 11.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~99.2% of bid side (54,533 resting ≥ 20,000 ✓) ≈ $3.68/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-wesmoo` | BUY | 7.0¢ | 85 | 0 | $200.00 | ✅ scoring — ~96.7% of bid side (30,183 resting ≥ 20,000 ✓) ≈ $3.58/day (event pool ÷ 27 markets) |
| `enwc-ushrp-fl19-2026-08-18-chrcol` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimobe` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-johstr` | BUY | 1.0¢ | 1,994 | 0 | $25.00 | ✅ scoring — ~95.0% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `vsc-usgubp-fl-fshbck-atl-13pct` | BUY | 33.0¢ | 10 | 0 | $500.00 | ✅ scoring — ~90.9% of bid side (10,369 resting ≥ 10,000 ✓) ≈ $22.73/day (event pool ÷ 10 markets) |
| `vsc-usgubp-fl-fshbck-atl-21pct` | SELL | 11.0¢ | 4 | 0 | $500.00 | ✅ scoring — ~89.6% of ask side (24,439 resting ≥ 10,000 ✓) ≈ $22.40/day (event pool ÷ 10 markets) |
| `vsc-usgubp-fl-fshbck-atl-11pct` | BUY | 48.0¢ | 60 | 0 | $500.00 | ✅ scoring — ~84.1% of bid side (10,604 resting ≥ 10,000 ✓) ≈ $21.02/day (event pool ÷ 10 markets) |
| `erac-usgubp-ak-adv-2026-08-18-despay` | BUY | 1.0¢ | 10,000 | 0 | $500.00 | ✅ scoring — ~80.6% of bid side (12,400 resting ≥ 10,000 ✓) ≈ $10.61/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-edndev` | BUY | 1.0¢ | 10,000 | 0 | $500.00 | ✅ scoring — ~80.6% of bid side (12,400 resting ≥ 10,000 ✓) ≈ $10.61/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-jonkre` | BUY | 82.0¢ | 10 | 0 | $500.00 | ✅ scoring — ~70.4% of bid side (10,826 resting ≥ 10,000 ✓) ≈ $9.27/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 13.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~68.3% of bid side (50,120 resting ≥ 20,000 ✓) ≈ $2.53/day (event pool ÷ 27 markets) |
| `enwc-ushrp-fl19-2026-08-18-madcaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~66.1% of bid side (3,025 resting ≥ 2,000 ✓) ≈ $1.18/day (event pool ÷ 7 markets) |
| `erac-usgubp-ak-adv-2026-08-18-davbro` | BUY | 59.0¢ | 20 | 0 | $500.00 | ✅ scoring — ~62.4% of bid side (15,282 resting ≥ 10,000 ✓) ≈ $8.21/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-hankro` | SELL | 4.0¢ | 60 | 0 | $500.00 | ✅ scoring — ~54.5% of ask side (10,040 resting ≥ 10,000 ✓) ≈ $7.18/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-hankro` | SELL | 4.0¢ | 50 | 0 | $500.00 | ✅ scoring — ~45.5% of ask side (10,040 resting ≥ 10,000 ✓) ≈ $5.98/day (event pool ÷ 19 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~43.6% of bid side (23,098 resting ≥ 5,000 ✓) ≈ $10.90/day (event pool ÷ 2 markets) |
| `erac-usgubp-ak-adv-2026-08-18-mathei` | BUY | 1.0¢ | 10,000 | 0 | $500.00 | ✅ scoring — ~38.5% of bid side (25,994 resting ≥ 10,000 ✓) ≈ $5.06/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-adacru` | SELL | 12.0¢ | 15 | 0 | $500.00 | ✅ scoring — ~34.8% of ask side (22,088 resting ≥ 10,000 ✓) ≈ $4.58/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-berwil` | BUY | 91.0¢ | 3 | 0 | $500.00 | ✅ scoring — ~33.3% of bid side (10,715 resting ≥ 10,000 ✓) ≈ $4.39/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-berwil` | BUY | 91.0¢ | 3 | 0 | $500.00 | ✅ scoring — ~33.3% of bid side (10,715 resting ≥ 10,000 ✓) ≈ $4.39/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-berwil` | BUY | 91.0¢ | 3 | 0 | $500.00 | ✅ scoring — ~33.3% of bid side (10,715 resting ≥ 10,000 ✓) ≈ $4.39/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-shehug` | BUY | 1.0¢ | 8,774 | 0 | $500.00 | ✅ scoring — ~31.8% of bid side (27,564 resting ≥ 10,000 ✓) ≈ $4.19/day (event pool ÷ 19 markets) |
| …and 1984 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>erac-usgubp-ak-adv-2026-08-18-lesmcg</code> SELL 100 @ 50¢ → $13.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 100 (100 yours) | ×0.2^0 = 100.0 |
|  | 99¢ | 10,461 | ×0.2^49 = 0.0 |
| | | **Σ** | **100.0** |

`yours 100.0 / Σ 100.0 = 100.0%`  
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
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg` ← this one
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei`
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-grebre</code> SELL 100 @ 50¢ → $13.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 100 (100 yours) | ×0.2^0 = 100.0 |
|  | 99¢ | 10,192 | ×0.2^49 = 0.0 |
| | | **Σ** | **100.0** |

`yours 100.0 / Σ 100.0 = 100.0%`  
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
9. `erac-usgubp-ak-adv-2026-08-18-grebre` ← this one
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
<details><summary><code>vsc-usgubp-fl-fshbck-atl-5pct</code> BUY 1 @ 96¢ → $25.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 1 (1 yours) | ×0.2^0 = 0.8 |
|  | 80¢ | 161 | ×0.2^16 = 0.0 |
|  | 77¢ | 16 | ×0.2^19 = 0.0 |
|  | 1¢ | 10,250 | ×0.2^95 = 0.0 |
| | | **Σ** | **0.8** |

`yours 0.8 / Σ 0.8 = 100.0%`  
`$500 ÷ 10 ÷ 2 = $25.00 × 100.0% = $25.00/day`  

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
|  | 5¢ | 1 | ×0.2^10 = 0.0 |
|  | 4¢ | 5,200 | ×0.2^11 = 0.0 |
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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-bruwal</code> SELL 15 @ 14¢ → $13.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 19¢ | 1 | ×0.2^5 = 0.0 |
|  | 20¢ | 969 | ×0.2^6 = 0.1 |
|  | 21¢ | 774 | ×0.2^7 = 0.0 |
|  | 29¢ | 0 | ×0.2^15 = 0.0 |
|  | 99¢ | 16,769 | ×0.2^85 = 0.0 |
| | | **Σ** | **15.1** |

`yours 15.0 / Σ 15.1 = 99.5%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 99.5% = $13.09/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal` ← this one
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
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 1 @ 11¢ → $3.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 1 | ×0.2^4 = 0.0 |
|  | 6¢ | 1 | ×0.2^5 = 0.0 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 4¢ | 2 | ×0.2^7 = 0.0 |
|  | 3¢ | 3 | ×0.2^8 = 0.0 |
|  | 2¢ | 2 | ×0.2^9 = 0.0 |
|  | 1¢ | 54,522 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.2%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 99.2% = $3.68/day`  

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
<details><summary><code>ewc-usp-2028-11-07-wesmoo</code> BUY 85 @ 7¢ → $3.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 86 (85 yours) | ×0.2^0 = 86.0 |
|  | 1¢ | 30,097 | ×0.2^6 = 1.9 |
| | | **Σ** | **87.9** |

`yours 85.0 / Σ 87.9 = 96.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 96.7% = $3.58/day`  

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
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo` ← this one

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-chrcol</code> BUY 2,000 @ 1¢ → $1.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (2,000 yours) | ×0.1^0 = 2,100.0 |
| | | **Σ** | **2,100.0** |

`yours 2,000.0 / Σ 2,100.0 = 95.2%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 95.2% = $1.70/day`  

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
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimobe</code> BUY 2,000 @ 1¢ → $1.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (2,000 yours) | ×0.1^0 = 2,100.0 |
| | | **Σ** | **2,100.0** |

`yours 2,000.0 / Σ 2,100.0 = 95.2%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 95.2% = $1.70/day`  

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
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimsch</code> BUY 2,000 @ 1¢ → $1.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (2,000 yours) | ×0.1^0 = 2,100.0 |
| | | **Σ** | **2,100.0** |

`yours 2,000.0 / Σ 2,100.0 = 95.2%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 95.2% = $1.70/day`  

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
<details><summary><code>enwc-ushrp-fl19-2026-08-18-johstr</code> BUY 1,994 @ 1¢ → $1.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (1,994 yours) | ×0.1^0 = 2,100.0 |
| | | **Σ** | **2,100.0** |

`yours 1,994.0 / Σ 2,100.0 = 95.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 95.0% = $1.70/day`  

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
<details><summary><code>vsc-usgubp-fl-fshbck-atl-13pct</code> BUY 10 @ 33¢ → $22.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 11 (10 yours) | ×0.2^0 = 11.0 |
|  | 25¢ | 50 | ×0.2^8 = 0.0 |
|  | 24¢ | 17 | ×0.2^9 = 0.0 |
|  | 17¢ | 50 | ×0.2^16 = 0.0 |
|  | 12¢ | 30 | ×0.2^21 = 0.0 |
|  | 1¢ | 10,211 | ×0.2^32 = 0.0 |
| | | **Σ** | **11.0** |

`yours 10.0 / Σ 11.0 = 90.9%`  
`$500 ÷ 10 ÷ 2 = $25.00 × 90.9% = $22.73/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vsc-usgubp-fl-fshbck-atl-11pct`
2. `vsc-usgubp-fl-fshbck-atl-13pct` ← this one
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
<details><summary><code>vsc-usgubp-fl-fshbck-atl-21pct</code> SELL 4 @ 11¢ → $22.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 4 (4 yours) | ×0.2^0 = 4.0 |
|  | 14¢ | 56 | ×0.2^3 = 0.4 |
|  | 15¢ | 1 | ×0.2^4 = 0.0 |
|  | 16¢ | 30 | ×0.2^5 = 0.0 |
|  | 49¢ | 25 | ×0.2^38 = 0.0 |
|  | 55¢ | 27 | ×0.2^44 = 0.0 |
|  | 99¢ | 24,296 | ×0.2^88 = 0.0 |
| | | **Σ** | **4.4** |

`yours 4.0 / Σ 4.4 = 89.6%`  
`$500 ÷ 10 ÷ 2 = $25.00 × 89.6% = $22.40/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vsc-usgubp-fl-fshbck-atl-11pct`
2. `vsc-usgubp-fl-fshbck-atl-13pct`
3. `vsc-usgubp-fl-fshbck-atl-15pct`
4. `vsc-usgubp-fl-fshbck-atl-17pct`
5. `vsc-usgubp-fl-fshbck-atl-19pct`
6. `vsc-usgubp-fl-fshbck-atl-21pct` ← this one
7. `vsc-usgubp-fl-fshbck-atl-30pct`
8. `vsc-usgubp-fl-fshbck-atl-5pct`
9. `vsc-usgubp-fl-fshbck-atl-7pct`
10. `vsc-usgubp-fl-fshbck-atl-9pct`

</details>

</details>
<details><summary><code>vsc-usgubp-fl-fshbck-atl-11pct</code> BUY 60 @ 48¢ → $21.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 65 (60 yours) | ×0.2^0 = 65.0 |
|  | 46¢ | 159 | ×0.2^2 = 6.4 |
|  | 40¢ | 50 | ×0.2^8 = 0.0 |
|  | 39¢ | 30 | ×0.2^9 = 0.0 |
|  | 36¢ | 50 | ×0.2^12 = 0.0 |
|  | 1¢ | 10,250 | ×0.2^47 = 0.0 |
| | | **Σ** | **71.4** |

`yours 60.0 / Σ 71.4 = 84.1%`  
`$500 ÷ 10 ÷ 2 = $25.00 × 84.1% = $21.02/day`  

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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-despay</code> BUY 10,000 @ 1¢ → $10.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,400 (10,000 yours) | ×0.2^0 = 12,400.0 |
| | | **Σ** | **12,400.0** |

`yours 10,000.0 / Σ 12,400.0 = 80.6%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 80.6% = $10.61/day`  

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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-edndev</code> BUY 10,000 @ 1¢ → $10.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,400 (10,000 yours) | ×0.2^0 = 12,400.0 |
| | | **Σ** | **12,400.0** |

`yours 10,000.0 / Σ 12,400.0 = 80.6%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 80.6% = $10.61/day`  

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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-jonkre</code> BUY 10 @ 82¢ → $9.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 14 (10 yours) | ×0.2^0 = 14.0 |
|  | 81¢ | 1 | ×0.2^1 = 0.2 |
|  | 61¢ | 659 | ×0.2^21 = 0.0 |
|  | 60¢ | 200 | ×0.2^22 = 0.0 |
|  | 44¢ | 0 | ×0.2^38 = 0.0 |
|  | 1¢ | 9,952 | ×0.2^81 = 0.0 |
| | | **Σ** | **14.2** |

`yours 10.0 / Σ 14.2 = 70.4%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 70.4% = $9.27/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 13¢ → $2.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 12¢ | 2 | ×0.2^1 = 0.4 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 2 | ×0.2^3 = 0.0 |
|  | 9¢ | 5 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^11 = 0.0 |
|  | 1¢ | 49,997 | ×0.2^12 = 0.0 |
| | | **Σ** | **1.5** |

`yours 1.0 / Σ 1.5 = 68.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 68.3% = $2.53/day`  

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
<details><summary><code>enwc-ushrp-fl19-2026-08-18-madcaw</code> BUY 2,000 @ 1¢ → $1.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,025 (2,000 yours) | ×0.1^0 = 3,025.0 |
| | | **Σ** | **3,025.0** |

`yours 2,000.0 / Σ 3,025.0 = 66.1%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 66.1% = $1.18/day`  

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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-davbro</code> BUY 20 @ 59¢ → $8.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 59¢ | 32 (20 yours) | ×0.2^0 = 32.0 |
|  | 51¢ | 250 | ×0.2^8 = 0.0 |
|  | 5¢ | 5,000 | ×0.2^54 = 0.0 |
|  | 1¢ | 10,000 | ×0.2^58 = 0.0 |
| | | **Σ** | **32.1** |

`yours 20.0 / Σ 32.1 = 62.4%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 62.4% = $8.21/day`  

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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-hankro</code> SELL 60 @ 4¢ → $7.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 110 (60 yours) | ×0.2^0 = 110.0 |
|  | 99¢ | 9,930 | ×0.2^95 = 0.0 |
| | | **Σ** | **110.0** |

`yours 60.0 / Σ 110.0 = 54.5%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 54.5% = $7.18/day`  

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
10. `erac-usgubp-ak-adv-2026-08-18-hankro` ← this one
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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-hankro</code> SELL 50 @ 4¢ → $5.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 110 (50 yours) | ×0.2^0 = 110.0 |
|  | 99¢ | 9,930 | ×0.2^95 = 0.0 |
| | | **Σ** | **110.0** |

`yours 50.0 / Σ 110.0 = 45.5%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 45.5% = $5.98/day`  

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
10. `erac-usgubp-ak-adv-2026-08-18-hankro` ← this one
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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $10.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,292 (1,000 yours) | ×0.2^0 = 2,291.9 |
|  | 5¢ | 501 | ×0.2^4 = 0.8 |
|  | 3¢ | 80 | ×0.2^6 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^7 = 0.3 |
| | | **Σ** | **2,293.0** |

`yours 1,000.0 / Σ 2,293.0 = 43.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 43.6% = $10.90/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-mathei</code> BUY 10,000 @ 1¢ → $5.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 25,994 (10,000 yours) | ×0.2^0 = 25,993.8 |
| | | **Σ** | **25,993.8** |

`yours 10,000.0 / Σ 25,993.8 = 38.5%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 38.5% = $5.06/day`  

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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-adacru</code> SELL 15 @ 12¢ → $4.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 21 (15 yours) | ×0.2^0 = 21.0 |
|  | 13¢ | 17 | ×0.2^1 = 3.3 |
|  | 14¢ | 30 | ×0.2^2 = 1.2 |
|  | 15¢ | 2,201 | ×0.2^3 = 17.6 |
|  | 98¢ | 10 | ×0.2^86 = 0.0 |
|  | 99¢ | 19,809 | ×0.2^87 = 0.0 |
| | | **Σ** | **43.1** |

`yours 15.0 / Σ 43.1 = 34.8%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 34.8% = $4.58/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru` ← this one
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
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-berwil</code> BUY 3 @ 91¢ → $4.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 9 (3 yours) | ×0.2^0 = 9.0 |
|  | 60¢ | 9 | ×0.2^31 = 0.0 |
|  | 55¢ | 454 | ×0.2^36 = 0.0 |
|  | 54¢ | 250 | ×0.2^37 = 0.0 |
|  | 53¢ | 88 | ×0.2^38 = 0.0 |
|  | 1¢ | 9,905 | ×0.2^90 = 0.0 |
| | | **Σ** | **9.0** |

`yours 3.0 / Σ 9.0 = 33.3%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 33.3% = $4.39/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil` ← this one
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
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-berwil</code> BUY 3 @ 91¢ → $4.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 9 (3 yours) | ×0.2^0 = 9.0 |
|  | 60¢ | 9 | ×0.2^31 = 0.0 |
|  | 55¢ | 454 | ×0.2^36 = 0.0 |
|  | 54¢ | 250 | ×0.2^37 = 0.0 |
|  | 53¢ | 88 | ×0.2^38 = 0.0 |
|  | 1¢ | 9,905 | ×0.2^90 = 0.0 |
| | | **Σ** | **9.0** |

`yours 3.0 / Σ 9.0 = 33.3%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 33.3% = $4.39/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil` ← this one
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
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-berwil</code> BUY 3 @ 91¢ → $4.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 9 (3 yours) | ×0.2^0 = 9.0 |
|  | 60¢ | 9 | ×0.2^31 = 0.0 |
|  | 55¢ | 454 | ×0.2^36 = 0.0 |
|  | 54¢ | 250 | ×0.2^37 = 0.0 |
|  | 53¢ | 88 | ×0.2^38 = 0.0 |
|  | 1¢ | 9,905 | ×0.2^90 = 0.0 |
| | | **Σ** | **9.0** |

`yours 3.0 / Σ 9.0 = 33.3%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 33.3% = $4.39/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil` ← this one
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
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-shehug</code> BUY 8,774 @ 1¢ → $4.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 27,564 (8,774 yours) | ×0.2^0 = 27,564.0 |
| | | **Σ** | **27,564.0** |

`yours 8,774.0 / Σ 27,564.0 = 31.8%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 31.8% = $4.19/day`  

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
17. `erac-usgubp-ak-adv-2026-08-18-shehug` ← this one
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,400 resting) | ~32.8% | ~$8.21 |
| `enwc-usgubp-fl-2026-08-18-rep-jaycol` | $500.00 ÷ 3 | 0.20 | 10,000 | SELL side (154,903 resting) | ~4.2% | ~$3.47 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (36,882 resting) | ~9.3% | ~$2.31 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (634,388 resting) | ~6.9% | ~$1.73 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (290,905 resting) | ~2.2% | ~$1.66 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,855 resting) | ~5.4% | ~$1.36 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (85,506 resting) | ~1.7% | ~$1.28 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,250,031 resting) | ~19.9% | ~$1.25 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (158,075 resting) | ~19.8% | ~$1.24 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $500.00 ÷ 3 | 0.20 | 10,000 | BUY side (672,363 resting) | ~1.4% | ~$1.20 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (75,918 resting) | ~1.6% | ~$1.18 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (97,131 resting) | ~1.4% | ~$1.03 |

## Totals

| | Amount |
|---|---:|
| Paid | $4,919.08 |
| Skipped | $1.41 |
| **Total earned** | **$4,920.49** |

2700 reward rows · 44 days with rewards · 552 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-15 | $1,352.63 | `████████████████████` |
| 2026-08-14 | $274.92 | `████` |
| 2026-08-13 | $223.24 | `███` |
| 2026-08-12 | $213.04 | `███` |
| 2026-08-11 | $409.60 | `██████` |
| 2026-08-10 | $557.62 | `████████` |
| 2026-08-09 | $62.24 | `█` |
| 2026-08-08 | $54.78 | `█` |
| 2026-08-07 | $60.33 | `█` |
| 2026-08-06 | $52.21 | `█` |
| 2026-08-05 | $31.46 | `█` |
| 2026-08-04 | $53.94 | `█` |
| 2026-08-03 | $44.81 | `█` |
| 2026-08-02 | $14.05 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $3,457.17 | `████████████████████` |
| 2026-07 | $1,463.32 | `████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $176.70 |
| `apdc-alito-2026-12-31` | $115.00 |
| `ewc-usp-party-2028-11-07-rep` | $83.48 |
| `opdc-mcconnell-resign-2026-11-02` | $79.41 |
| `ewc-usp-party-2028-11-07-dem` | $69.70 |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | $66.06 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $63.61 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $60.43 |
| `enwc-uspres-nom-rep-2028-rondes` | $45.09 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.58 |
| `enwc-uspres-nom-dem-2028-stasmi` | $42.80 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.51 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.04 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-17 7:50 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 6:49 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 5:49 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 4:48 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 3:48 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 2:47 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 1:33 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 12:50 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 12:39 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 9:17 AM ET | ✅ ok | 2700 | $4920.49 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
