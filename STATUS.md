# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-17 5:49 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$195.43/day estimated (ceiling, not promise — details below)

**Earned:** $4,920.49 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** · 2026-08-13: **$223.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$8.18/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$2.65/day), `ewc-usgub-oh-2026-11-03-dem` (~$2.01/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$195.43/day (~$8.14/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vsc-usgubp-fl-fshbck-atl-5pct` | BUY | 96.0¢ | 8 | 0 | $500.00 | ✅ scoring — ~100.0% of bid side (10,185 resting ≥ 10,000 ✓) ≈ $25.00/day (event pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 15.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (805,598 resting ≥ 5,000 ✓) ≈ $4.17/day (event pool ÷ 12 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 11.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~99.2% of bid side (54,530 resting ≥ 20,000 ✓) ≈ $3.68/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-wesmoo` | BUY | 7.0¢ | 85 | 0 | $200.00 | ✅ scoring — ~96.5% of bid side (30,183 resting ≥ 20,000 ✓) ≈ $3.57/day (event pool ÷ 27 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimobe` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-chrcol` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-johstr` | BUY | 1.0¢ | 1,994 | 0 | $25.00 | ✅ scoring — ~95.0% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `enwc-uspres-nom-dem-2028-micoba` | BUY | 8.0¢ | 132 | 0 | $200.00 | ✅ scoring — ~55.3% of bid side (90,688 resting ≥ 20,000 ✓) ≈ $3.25/day (event pool ÷ 17 markets) |
| `erac-usgubp-ak-adv-2026-08-18-davbro` | BUY | 1.0¢ | 10,000 | 1 | $500.00 | ✅ scoring — ~44.4% of bid side (12,500 resting ≥ 10,000 ✓) ≈ $5.85/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-markel` | SELL | 13.0¢ | 16 | 0 | $200.00 | ✅ scoring — ~42.8% of ask side (61,982 resting ≥ 20,000 ✓) ≈ $1.59/day (event pool ÷ 27 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~39.4% of bid side (24,310 resting ≥ 5,000 ✓) ≈ $9.86/day (event pool ÷ 2 markets) |
| `erac-usgubp-ak-adv-2026-08-18-edndev` | BUY | 1.0¢ | 10,000 | 0 | $500.00 | ✅ scoring — ~33.8% of bid side (29,552 resting ≥ 10,000 ✓) ≈ $4.45/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 9.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~30.3% of bid side (20,161 resting ≥ 20,000 ✓) ≈ $1.12/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 84.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~28.4% of bid side (512,183 resting ≥ 2,000 ✓) ≈ $1.77/day (event pool ÷ 2 markets) |
| `erac-usgubp-ak-adv-2026-08-18-mathei` | BUY | 1.0¢ | 10,000 | 0 | $500.00 | ✅ scoring — ~28.0% of bid side (35,764 resting ≥ 10,000 ✓) ≈ $3.68/day (event pool ÷ 19 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 85.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~27.9% of ask side (10,984 resting ≥ 2,000 ✓) ≈ $1.74/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~27.7% of bid side (400,604 resting ≥ 5,000 ✓) ≈ $1.15/day (event pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~27.7% of bid side (400,604 resting ≥ 5,000 ✓) ≈ $1.15/day (event pool ÷ 12 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | BUY | 6.0¢ | 7 | 0 | $25.00 | ✅ scoring — ~27.4% of bid side (12,261 resting ≥ 2,000 ✓) ≈ $1.71/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | BUY | 6.0¢ | 7 | 0 | $25.00 | ✅ scoring — ~27.4% of bid side (12,261 resting ≥ 2,000 ✓) ≈ $1.71/day (event pool ÷ 2 markets) |
| `erac-usgubp-ak-adv-2026-08-18-berwil` | BUY | 91.0¢ | 3 | 0 | $500.00 | ✅ scoring — ~26.8% of bid side (10,467 resting ≥ 10,000 ✓) ≈ $3.52/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-berwil` | BUY | 91.0¢ | 3 | 0 | $500.00 | ✅ scoring — ~26.8% of bid side (10,467 resting ≥ 10,000 ✓) ≈ $3.52/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 9.0¢ | 34 | 0 | $200.00 | ✅ scoring — ~23.8% of bid side (30,165 resting ≥ 20,000 ✓) ≈ $0.88/day (event pool ÷ 27 markets) |
| `enwc-ushrp-fl19-2026-08-18-madcaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~23.2% of bid side (8,620 resting ≥ 2,000 ✓) ≈ $0.41/day (event pool ÷ 7 markets) |
| `ewc-usp-2028-11-07-stasmi` | BUY | 1.0¢ | 9,549 | 2 | $200.00 | ✅ scoring — ~17.7% of bid side (53,977 resting ≥ 20,000 ✓) ≈ $0.65/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-dontrujr` | SELL | 5.0¢ | 149 | 0 | $200.00 | ✅ scoring — ~17.0% of ask side (46,196 resting ≥ 20,000 ✓) ≈ $1.22/day (event pool ÷ 14 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 15.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~15.4% of ask side (225,049 resting ≥ 2,000 ✓) ≈ $0.96/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rokha` | BUY | 1.0¢ | 9,546 | 1 | $200.00 | ✅ scoring — ~15.3% of bid side (52,521 resting ≥ 20,000 ✓) ≈ $0.57/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-rokha` | SELL | 4.0¢ | 25 | 0 | $200.00 | ✅ scoring — ~14.8% of ask side (38,898 resting ≥ 20,000 ✓) ≈ $0.87/day (event pool ÷ 17 markets) |
| …and 2000 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vsc-usgubp-fl-fshbck-atl-5pct</code> BUY 8 @ 96¢ → $25.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 8 (8 yours) | ×0.2^0 = 7.8 |
|  | 80¢ | 161 | ×0.2^16 = 0.0 |
|  | 77¢ | 16 | ×0.2^19 = 0.0 |
|  | 1¢ | 10,000 | ×0.2^95 = 0.0 |
| | | **Σ** | **7.8** |

`yours 7.8 / Σ 7.8 = 100.0%`  
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
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 1 @ 11¢ → $3.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 1 | ×0.2^4 = 0.0 |
|  | 6¢ | 1 | ×0.2^5 = 0.0 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 4¢ | 1 | ×0.2^7 = 0.0 |
|  | 3¢ | 2 | ×0.2^8 = 0.0 |
|  | 2¢ | 1 | ×0.2^9 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-wesmoo</code> BUY 85 @ 7¢ → $3.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 86 (85 yours) | ×0.2^0 = 86.1 |
|  | 1¢ | 30,097 | ×0.2^6 = 1.9 |
| | | **Σ** | **88.1** |

`yours 85.0 / Σ 88.1 = 96.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 96.5% = $3.57/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-micoba</code> BUY 132 @ 8¢ → $3.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 238 (132 yours) | ×0.2^0 = 237.6 |
|  | 1¢ | 90,450 | ×0.2^7 = 1.2 |
| | | **Σ** | **238.7** |

`yours 132.0 / Σ 238.7 = 55.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 55.3% = $3.25/day`  

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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-davbro</code> BUY 10,000 @ 1¢ → $5.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 2,500 | ×0.2^0 = 2,500.0 |
| ▶ | 1¢ | 10,000 (10,000 yours) | ×0.2^1 = 2,000.0 |
| | | **Σ** | **4,500.0** |

`yours 2,000.0 / Σ 4,500.0 = 44.4%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 44.4% = $5.85/day`  

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
<details><summary><code>ewc-usp-2028-11-07-markel</code> SELL 16 @ 13¢ → $1.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 24 (16 yours) | ×0.2^0 = 24.0 |
|  | 15¢ | 1 | ×0.2^2 = 0.1 |
|  | 18¢ | 41,656 | ×0.2^5 = 13.3 |
| | | **Σ** | **37.4** |

`yours 16.0 / Σ 37.4 = 42.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 42.8% = $1.59/day`  

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
15. `ewc-usp-2028-11-07-markel` ← this one
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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $9.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,292 (1,000 yours) | ×0.2^0 = 2,291.9 |
|  | 8¢ | 1,212 | ×0.2^1 = 242.4 |
|  | 5¢ | 501 | ×0.2^4 = 0.8 |
|  | 3¢ | 80 | ×0.2^6 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^7 = 0.3 |
| | | **Σ** | **2,535.4** |

`yours 1,000.0 / Σ 2,535.4 = 39.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 39.4% = $9.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-edndev</code> BUY 10,000 @ 1¢ → $4.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 29,552 (10,000 yours) | ×0.2^0 = 29,552.0 |
| | | **Σ** | **29,552.0** |

`yours 10,000.0 / Σ 29,552.0 = 33.8%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 33.8% = $4.45/day`  

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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 50 @ 9¢ → $1.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 165 (50 yours) | ×0.2^0 = 165.0 |
|  | 1¢ | 19,996 | ×0.2^8 = 0.1 |
| | | **Σ** | **165.1** |

`yours 50.0 / Σ 165.1 = 30.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 30.3% = $1.12/day`  

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 2 @ 84¢ → $1.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 7 (2 yours) | ×0.1^0 = 7.0 |
|  | 82¢ | 5 | ×0.1^2 = 0.1 |
|  | 74¢ | 152 | ×0.1^10 = 0.0 |
|  | 65¢ | 14 | ×0.1^19 = 0.0 |
|  | 60¢ | 1 | ×0.1^24 = 0.0 |
|  | 10¢ | 5 | ×0.1^74 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^82 = 0.0 |
| | | **Σ** | **7.1** |

`yours 2.0 / Σ 7.1 = 28.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.4% = $1.77/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-mathei</code> BUY 10,000 @ 1¢ → $3.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 35,764 (10,000 yours) | ×0.2^0 = 35,764.0 |
| | | **Σ** | **35,764.0** |

`yours 10,000.0 / Σ 35,764.0 = 28.0%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 28.0% = $3.68/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 2 @ 85¢ → $1.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 7 (2 yours) | ×0.1^0 = 7.0 |
|  | 86¢ | 1 | ×0.1^1 = 0.1 |
|  | 87¢ | 1 | ×0.1^2 = 0.0 |
|  | 88¢ | 55 | ×0.1^3 = 0.1 |
|  | 99¢ | 10,920 | ×0.1^14 = 0.0 |
| | | **Σ** | **7.2** |

`yours 2.0 / Σ 7.2 = 27.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.9% = $1.74/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 1 @ 13¢ → $1.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 12¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 150 | ×0.2^3 = 1.2 |
|  | 2¢ | 400,250 | ×0.2^11 = 0.0 |
| | | **Σ** | **3.6** |

`yours 1.0 / Σ 3.6 = 27.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 27.7% = $1.15/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 1 @ 13¢ → $1.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 12¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 150 | ×0.2^3 = 1.2 |
|  | 2¢ | 400,250 | ×0.2^11 = 0.0 |
| | | **Σ** | **3.6** |

`yours 1.0 / Σ 3.6 = 27.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 27.7% = $1.15/day`  

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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> BUY 7 @ 6¢ → $1.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 24 (7 yours) | ×0.1^0 = 24.0 |
|  | 5¢ | 1 | ×0.1^1 = 0.1 |
|  | 4¢ | 135 | ×0.1^2 = 1.4 |
|  | 2¢ | 2 | ×0.1^4 = 0.0 |
|  | 1¢ | 12,099 | ×0.1^5 = 0.1 |
| | | **Σ** | **25.6** |

`yours 7.0 / Σ 25.6 = 27.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.4% = $1.71/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> BUY 7 @ 6¢ → $1.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 24 (7 yours) | ×0.1^0 = 24.0 |
|  | 5¢ | 1 | ×0.1^1 = 0.1 |
|  | 4¢ | 135 | ×0.1^2 = 1.4 |
|  | 2¢ | 2 | ×0.1^4 = 0.0 |
|  | 1¢ | 12,099 | ×0.1^5 = 0.1 |
| | | **Σ** | **25.6** |

`yours 7.0 / Σ 25.6 = 27.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.4% = $1.71/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-berwil</code> BUY 3 @ 91¢ → $3.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 11 (3 yours) | ×0.2^0 = 11.2 |
|  | 60¢ | 1 | ×0.2^31 = 0.0 |
|  | 54¢ | 462 | ×0.2^37 = 0.0 |
|  | 53¢ | 88 | ×0.2^38 = 0.0 |
|  | 1¢ | 9,905 | ×0.2^90 = 0.0 |
| | | **Σ** | **11.2** |

`yours 3.0 / Σ 11.2 = 26.8%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 26.8% = $3.52/day`  

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
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-berwil</code> BUY 3 @ 91¢ → $3.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 11 (3 yours) | ×0.2^0 = 11.2 |
|  | 60¢ | 1 | ×0.2^31 = 0.0 |
|  | 54¢ | 462 | ×0.2^37 = 0.0 |
|  | 53¢ | 88 | ×0.2^38 = 0.0 |
|  | 1¢ | 9,905 | ×0.2^90 = 0.0 |
| | | **Σ** | **11.2** |

`yours 3.0 / Σ 11.2 = 26.8%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 26.8% = $3.52/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 34 @ 9¢ → $0.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 143 (34 yours) | ×0.2^0 = 142.6 |
|  | 5¢ | 25 | ×0.2^4 = 0.0 |
|  | 1¢ | 29,997 | ×0.2^8 = 0.1 |
| | | **Σ** | **142.7** |

`yours 34.0 / Σ 142.7 = 23.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 23.8% = $0.88/day`  

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
25. `ewc-usp-2028-11-07-tulgab` ← this one
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-madcaw</code> BUY 2,000 @ 1¢ → $0.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 8,620 (2,000 yours) | ×0.1^0 = 8,620.0 |
| | | **Σ** | **8,620.0** |

`yours 2,000.0 / Σ 8,620.0 = 23.2%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 23.2% = $0.41/day`  

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
<details><summary><code>ewc-usp-2028-11-07-stasmi</code> BUY 9,549 @ 1¢ → $0.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.3 |
|  | 2¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 1¢ | 53,975 (9,549 yours) | ×0.2^2 = 2,159.0 |
| | | **Σ** | **2,160.5** |

`yours 382.0 / Σ 2,160.5 = 17.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 17.7% = $0.65/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-dontrujr</code> SELL 149 @ 5¢ → $1.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 527 (149 yours) | ×0.2^0 = 527.0 |
|  | 6¢ | 10 | ×0.2^1 = 2.0 |
|  | 7¢ | 74 | ×0.2^2 = 2.9 |
|  | 8¢ | 42,771 | ×0.2^3 = 342.2 |
| | | **Σ** | **874.1** |

`yours 149.0 / Σ 874.1 = 17.0%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 17.0% = $1.22/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr` ← this one
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 2 @ 15¢ → $0.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 13 (2 yours) | ×0.1^0 = 13.0 |
|  | 25¢ | 50 | ×0.1^10 = 0.0 |
|  | 35¢ | 89 | ×0.1^20 = 0.0 |
|  | 40¢ | 1 | ×0.1^25 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^83 = 0.0 |
| | | **Σ** | **13.0** |

`yours 2.0 / Σ 13.0 = 15.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 15.4% = $0.96/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rokha</code> BUY 9,546 @ 1¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 2,500 | ×0.2^0 = 2,500.0 |
| ▶ | 1¢ | 50,021 (9,546 yours) | ×0.2^1 = 10,004.2 |
| | | **Σ** | **12,504.2** |

`yours 1,909.2 / Σ 12,504.2 = 15.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 15.3% = $0.57/day`  

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
20. `ewc-usp-2028-11-07-rokha` ← this one
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-rokha</code> SELL 25 @ 4¢ → $0.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 169 (25 yours) | ×0.2^0 = 169.0 |
|  | 10¢ | 2 | ×0.2^6 = 0.0 |
|  | 15¢ | 0 | ×0.2^11 = 0.0 |
|  | 16¢ | 20,910 | ×0.2^12 = 0.0 |
| | | **Σ** | **169.0** |

`yours 25.0 / Σ 169.0 = 14.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 14.8% = $0.87/day`  

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
15. `enwc-uspres-nom-dem-2028-rokha` ← this one
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
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,232 resting) | ~32.7% | ~$8.18 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (35,809 resting) | ~10.6% | ~$2.65 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (289,326 resting) | ~2.7% | ~$2.01 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (629,811 resting) | ~7.2% | ~$1.79 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (90,616 resting) | ~25.9% | ~$1.62 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (156,700 resting) | ~24.4% | ~$1.52 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,894 resting) | ~5.4% | ~$1.35 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,970 resting) | ~1.7% | ~$1.31 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (75,654 resting) | ~1.6% | ~$1.20 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $500.00 ÷ 3 | 0.20 | 10,000 | BUY side (673,947 resting) | ~1.4% | ~$1.17 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (166,626 resting) | ~4.3% | ~$1.09 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (96,849 resting) | ~1.4% | ~$1.03 |

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
| 2026-08-17 5:49 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 4:48 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 3:48 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 2:47 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 1:33 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 12:50 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 12:39 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 9:17 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 8:51 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 8:43 AM ET | ✅ ok | 2700 | $4920.49 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
