# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-17 12:50 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$181.92/day estimated (ceiling, not promise — details below)

**Earned:** $4,920.49 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** · 2026-08-13: **$223.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-rep` — SELL at the best price, ~$8.70/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$3.69/day), `ewc-usgub-oh-2026-11-03-dem` (~$2.65/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$181.92/day (~$7.58/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ushrp-fl19-2026-08-18-olahaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~98.8% of bid side (2,025 resting ≥ 2,000 ✓) ≈ $1.76/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-chrcol` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimobe` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $1.70/day (event pool ÷ 7 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 14.0¢ | 0 | 0 | $200.00 | ✅ scoring — ~87.8% of bid side (24,531 resting ≥ 20,000 ✓) ≈ $3.25/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-kamhar` | BUY | 13.0¢ | 284 | 0 | $200.00 | ✅ scoring — ~71.9% of bid side (79,203 resting ≥ 20,000 ✓) ≈ $2.66/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | SELL | 16.0¢ | 15 | 0 | $200.00 | ✅ scoring — ~68.2% of ask side (69,752 resting ≥ 20,000 ✓) ≈ $4.01/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-thomas` | BUY | 7.0¢ | 250 | 0 | $200.00 | ✅ scoring — ~68.1% of bid side (63,139 resting ≥ 20,000 ✓) ≈ $2.52/day (event pool ÷ 27 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~64.1% of bid side (200,605 resting ≥ 5,000 ✓) ≈ $2.46/day (event pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-jonoss` | BUY | 19.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~62.3% of bid side (74,481 resting ≥ 20,000 ✓) ≈ $2.31/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-stasmi` | SELL | 4.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~52.1% of ask side (43,956 resting ≥ 20,000 ✓) ≈ $3.06/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-jonste` | SELL | 7.0¢ | 48 | 0 | $200.00 | ✅ scoring — ~51.6% of ask side (52,982 resting ≥ 20,000 ✓) ≈ $3.04/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 20.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~49.8% of ask side (92,858 resting ≥ 5,000 ✓) ≈ $1.92/day (event pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~49.7% of bid side (400,576 resting ≥ 5,000 ✓) ≈ $2.07/day (event pool ÷ 12 markets) |
| `enwc-uspres-nom-dem-2028-micoba` | SELL | 9.0¢ | 45 | 0 | $200.00 | ✅ scoring — ~49.4% of ask side (43,498 resting ≥ 20,000 ✓) ≈ $2.91/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 12.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~49.0% of bid side (100,529 resting ≥ 5,000 ✓) ≈ $1.88/day (event pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 12.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~49.0% of bid side (100,529 resting ≥ 5,000 ✓) ≈ $1.88/day (event pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-aleocc` | BUY | 18.0¢ | 200 | 0 | $200.00 | ✅ scoring — ~48.1% of bid side (174,456 resting ≥ 20,000 ✓) ≈ $1.78/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 15.0¢ | 200 | 0 | $200.00 | ✅ scoring — ~46.6% of bid side (89,842 resting ≥ 20,000 ✓) ≈ $2.74/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 14.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~46.3% of bid side (300,552 resting ≥ 5,000 ✓) ≈ $1.78/day (event pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-rokha` | SELL | 4.0¢ | 25 | 0 | $200.00 | ✅ scoring — ~43.9% of ask side (38,745 resting ≥ 20,000 ✓) ≈ $2.58/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 5.0¢ | 25 | 0 | $200.00 | ✅ scoring — ~43.1% of ask side (43,348 resting ≥ 20,000 ✓) ≈ $2.54/day (event pool ÷ 17 markets) |
| `ussewc-usse-la-2026-11-03-rep` | SELL | 93.0¢ | 9 | 0 | $25.00 | ✅ scoring — ~42.8% of ask side (11,462 resting ≥ 2,000 ✓) ≈ $2.67/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-tulgab` | BUY | 1.0¢ | 19,400 | 2 | $200.00 | ✅ scoring — ~42.0% of bid side (41,161 resting ≥ 20,000 ✓) ≈ $3.00/day (event pool ÷ 14 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 3.0¢ | 157 | 0 | $25.00 | ✅ scoring — ~40.8% of ask side (131,156 resting ≥ 2,000 ✓) ≈ $2.55/day (event pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~39.4% of bid side (24,310 resting ≥ 5,000 ✓) ≈ $9.86/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-wesmoo` | SELL | 5.0¢ | 25 | 0 | $200.00 | ✅ scoring — ~39.1% of ask side (43,307 resting ≥ 20,000 ✓) ≈ $2.30/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 13.0¢ | 4 | 1 | $100.00 | ✅ scoring — ~37.0% of bid side (300,552 resting ≥ 5,000 ✓) ≈ $1.42/day (event pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-markel` | SELL | 13.0¢ | 16 | 0 | $200.00 | ✅ scoring — ~33.8% of ask side (61,797 resting ≥ 20,000 ✓) ≈ $1.25/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 88.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~33.3% of bid side (510,251 resting ≥ 2,000 ✓) ≈ $2.08/day (event pool ÷ 2 markets) |
| …and 867 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> BUY 2,000 @ 1¢ → $1.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,025 (2,000 yours) | ×0.1^0 = 2,025.0 |
| | | **Σ** | **2,025.0** |

`yours 2,000.0 / Σ 2,025.0 = 98.8%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 98.8% = $1.76/day`  

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
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 0 @ 14¢ → $3.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 0 (0 yours) | ×0.2^0 = 0.1 |
|  | 11¢ | 1 | ×0.2^3 = 0.0 |
|  | 7¢ | 1 | ×0.2^7 = 0.0 |
|  | 6¢ | 1 | ×0.2^8 = 0.0 |
|  | 5¢ | 1 | ×0.2^9 = 0.0 |
|  | 4¢ | 1 | ×0.2^10 = 0.0 |
|  | 3¢ | 2 | ×0.2^11 = 0.0 |
|  | 2¢ | 2 | ×0.2^12 = 0.0 |
|  | 1¢ | 24,522 | ×0.2^13 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 87.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 87.8% = $3.25/day`  

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
<details><summary><code>ewc-usp-2028-11-07-kamhar</code> BUY 284 @ 13¢ → $2.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 395 (284 yours) | ×0.2^0 = 395.0 |
|  | 3¢ | 78,583 | ×0.2^10 = 0.0 |
| | | **Σ** | **395.0** |

`yours 284.0 / Σ 395.0 = 71.9%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 71.9% = $2.66/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> SELL 15 @ 16¢ → $4.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 22 (15 yours) | ×0.2^0 = 22.0 |
|  | 28¢ | 2 | ×0.2^12 = 0.0 |
|  | 32¢ | 50,932 | ×0.2^16 = 0.0 |
| | | **Σ** | **22.0** |

`yours 15.0 / Σ 22.0 = 68.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 68.2% = $4.01/day`  

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
<details><summary><code>ewc-usp-2028-11-07-thomas</code> BUY 250 @ 7¢ → $2.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 360 (250 yours) | ×0.2^0 = 360.0 |
|  | 2¢ | 22,000 | ×0.2^5 = 7.0 |
| | | **Σ** | **367.0** |

`yours 250.0 / Σ 367.0 = 68.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 68.1% = $2.52/day`  

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
23. `ewc-usp-2028-11-07-thomas` ← this one
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 13¢ → $2.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 10¢ | 70 | ×0.2^3 = 0.6 |
|  | 3¢ | 25 | ×0.2^10 = 0.0 |
|  | 1¢ | 200,509 | ×0.2^12 = 0.0 |
| | | **Σ** | **1.6** |

`yours 1.0 / Σ 1.6 = 64.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.1% = $2.46/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jonoss</code> BUY 1 @ 19¢ → $2.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 18¢ | 1 | ×0.2^1 = 0.2 |
|  | 16¢ | 30 | ×0.2^3 = 0.2 |
|  | 15¢ | 104 | ×0.2^4 = 0.2 |
|  | 13¢ | 1 | ×0.2^6 = 0.0 |
|  | 12¢ | 1 | ×0.2^7 = 0.0 |
|  | 11¢ | 11 | ×0.2^8 = 0.0 |
|  | 9¢ | 2,777 | ×0.2^10 = 0.0 |
|  | 8¢ | 5 | ×0.2^11 = 0.0 |
|  | 2¢ | 1,000 | ×0.2^17 = 0.0 |
| | … | +1 levels | 0.0 |
| | | **Σ** | **1.6** |

`yours 1.0 / Σ 1.6 = 62.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 62.3% = $2.31/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-stasmi</code> SELL 50 @ 4¢ → $3.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 96 (50 yours) | ×0.2^0 = 96.0 |
|  | 12¢ | 2 | ×0.2^8 = 0.0 |
|  | 15¢ | 4 | ×0.2^11 = 0.0 |
|  | 16¢ | 2 | ×0.2^12 = 0.0 |
|  | 17¢ | 30 | ×0.2^13 = 0.0 |
|  | 18¢ | 21 | ×0.2^14 = 0.0 |
|  | 19¢ | 40,992 | ×0.2^15 = 0.0 |
| | | **Σ** | **96.0** |

`yours 50.0 / Σ 96.0 = 52.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 52.1% = $3.06/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonste</code> SELL 48 @ 7¢ → $3.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 93 (48 yours) | ×0.2^0 = 93.0 |
|  | 13¢ | 4 | ×0.2^6 = 0.0 |
|  | 14¢ | 105 | ×0.2^7 = 0.0 |
|  | 20¢ | 46 | ×0.2^13 = 0.0 |
|  | 21¢ | 400 | ×0.2^14 = 0.0 |
|  | 22¢ | 49,542 | ×0.2^15 = 0.0 |
| | | **Σ** | **93.0** |

`yours 48.0 / Σ 93.0 = 51.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 51.6% = $3.04/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste` ← this one
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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 1 @ 20¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 26¢ | 121 | ×0.2^6 = 0.0 |
|  | 27¢ | 25 | ×0.2^7 = 0.0 |
|  | 29¢ | 0 | ×0.2^9 = 0.0 |
|  | 31¢ | 18 | ×0.2^11 = 0.0 |
|  | 35¢ | 1 | ×0.2^15 = 0.0 |
|  | 41¢ | 1 | ×0.2^21 = 0.0 |
|  | 50¢ | 18 | ×0.2^30 = 0.0 |
|  | 96¢ | 1,000 | ×0.2^76 = 0.0 |
|  | 97¢ | 80,472 | ×0.2^77 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 49.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 49.8% = $1.92/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50` ← this one
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 1 @ 13¢ → $2.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 10¢ | 125 | ×0.2^3 = 1.0 |
|  | 2¢ | 400,250 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 49.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.7% = $2.07/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-micoba</code> SELL 45 @ 9¢ → $2.91/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 91 (45 yours) | ×0.2^0 = 91.0 |
|  | 14¢ | 31 | ×0.2^5 = 0.0 |
|  | 15¢ | 1 | ×0.2^6 = 0.0 |
|  | 17¢ | 40,200 | ×0.2^8 = 0.1 |
| | | **Σ** | **91.1** |

`yours 45.0 / Σ 91.1 = 49.4%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 49.4% = $2.91/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 1 @ 12¢ → $1.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^8 = 0.0 |
|  | 3¢ | 5 | ×0.2^9 = 0.0 |
|  | 1¢ | 100,520 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 49.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 49.0% = $1.88/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47` ← this one
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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 1 @ 12¢ → $1.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^8 = 0.0 |
|  | 3¢ | 5 | ×0.2^9 = 0.0 |
|  | 1¢ | 100,520 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 49.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 49.0% = $1.88/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-aleocc</code> BUY 200 @ 18¢ → $1.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 414 (200 yours) | ×0.2^0 = 414.1 |
|  | 17¢ | 1 | ×0.2^1 = 0.2 |
|  | 14¢ | 714 | ×0.2^4 = 1.1 |
|  | 9¢ | 2,777 | ×0.2^9 = 0.0 |
|  | 1¢ | 170,550 | ×0.2^17 = 0.0 |
| | | **Σ** | **415.4** |

`yours 200.0 / Σ 415.4 = 48.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 48.1% = $1.78/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc` ← this one
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
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 200 @ 15¢ → $2.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 215 (200 yours) | ×0.2^0 = 215.2 |
|  | 14¢ | 1 | ×0.2^1 = 0.2 |
|  | 13¢ | 5,076 | ×0.2^2 = 203.0 |
|  | 10¢ | 34,250 | ×0.2^5 = 11.0 |
| | | **Σ** | **429.4** |

`yours 200.0 / Σ 429.4 = 46.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 46.6% = $2.74/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 1 @ 14¢ → $1.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 13¢ | 5 | ×0.2^1 = 1.0 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 11¢ | 1 | ×0.2^3 = 0.0 |
|  | 10¢ | 70 | ×0.2^4 = 0.1 |
|  | 1¢ | 300,474 | ×0.2^13 = 0.0 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 46.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 46.3% = $1.78/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51` ← this one
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-rokha</code> SELL 25 @ 4¢ → $2.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 57 (25 yours) | ×0.2^0 = 57.0 |
|  | 10¢ | 2 | ×0.2^6 = 0.0 |
|  | 15¢ | 0 | ×0.2^11 = 0.0 |
|  | 16¢ | 20,910 | ×0.2^12 = 0.0 |
| | | **Σ** | **57.0** |

`yours 25.0 / Σ 57.0 = 43.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 43.9% = $2.58/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 25 @ 5¢ → $2.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 58 (25 yours) | ×0.2^0 = 58.0 |
|  | 13¢ | 4 | ×0.2^8 = 0.0 |
|  | 15¢ | 9 | ×0.2^10 = 0.0 |
|  | 19¢ | 2 | ×0.2^14 = 0.0 |
|  | 20¢ | 25,501 | ×0.2^15 = 0.0 |
| | | **Σ** | **58.0** |

`yours 25.0 / Σ 58.0 = 43.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 43.1% = $2.54/day`  

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
<details><summary><code>ussewc-usse-la-2026-11-03-rep</code> SELL 9 @ 93¢ → $2.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 19 (9 yours) | ×0.1^0 = 19.0 |
|  | 94¢ | 18 | ×0.1^1 = 1.8 |
|  | 95¢ | 5 | ×0.1^2 = 0.1 |
|  | 97¢ | 2,000 | ×0.1^4 = 0.2 |
| | | **Σ** | **21.1** |

`yours 9.0 / Σ 21.1 = 42.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 42.8% = $2.67/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem`
2. `ussewc-usse-la-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-tulgab</code> BUY 19,400 @ 1¢ → $3.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 211 | ×0.2^0 = 211.0 |
| ▶ | 1¢ | 40,950 (19,400 yours) | ×0.2^2 = 1,638.0 |
| | | **Σ** | **1,849.0** |

`yours 776.0 / Σ 1,849.0 = 42.0%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 42.0% = $3.00/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
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
13. `enwc-uspres-nom-rep-2028-tulgab` ← this one
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 157 @ 3¢ → $2.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 385 (157 yours) | ×0.1^0 = 385.0 |
|  | 7¢ | 46 | ×0.1^4 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^95 = 0.0 |
| | | **Σ** | **385.0** |

`yours 157.0 / Σ 385.0 = 40.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 40.8% = $2.55/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

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
<details><summary><code>enwc-uspres-nom-dem-2028-wesmoo</code> SELL 25 @ 5¢ → $2.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 63 (25 yours) | ×0.2^0 = 63.0 |
|  | 7¢ | 16 | ×0.2^2 = 0.7 |
|  | 12¢ | 25,453 | ×0.2^7 = 0.3 |
| | | **Σ** | **64.0** |

`yours 25.0 / Σ 64.0 = 39.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 39.1% = $2.30/day`  

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
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 4 @ 13¢ → $1.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 13¢ | 5 (4 yours) | ×0.2^1 = 1.0 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 11¢ | 1 | ×0.2^3 = 0.0 |
|  | 10¢ | 70 | ×0.2^4 = 0.1 |
|  | 1¢ | 300,474 | ×0.2^13 = 0.0 |
| | | **Σ** | **2.2** |

`yours 0.8 / Σ 2.2 = 37.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.0% = $1.42/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51` ← this one
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-markel</code> SELL 16 @ 13¢ → $1.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 34 (16 yours) | ×0.2^0 = 34.0 |
|  | 15¢ | 1 | ×0.2^2 = 0.1 |
|  | 17¢ | 30 | ×0.2^4 = 0.0 |
|  | 18¢ | 41,456 | ×0.2^5 = 13.3 |
| | | **Σ** | **47.4** |

`yours 16.0 / Σ 47.4 = 33.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 33.8% = $1.25/day`  

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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 3 @ 88¢ → $2.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 9 (3 yours) | ×0.1^0 = 9.0 |
|  | 75¢ | 25 | ×0.1^13 = 0.0 |
|  | 44¢ | 1 | ×0.1^44 = 0.0 |
|  | 38¢ | 11 | ×0.1^50 = 0.0 |
|  | 29¢ | 1 | ×0.1^59 = 0.0 |
|  | 10¢ | 4 | ×0.1^78 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^86 = 0.0 |
| | | **Σ** | **9.0** |

`yours 3.0 / Σ 9.0 = 33.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 33.3% = $2.08/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (20,548 resting) | ~11.6% | ~$8.70 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,736 resting) | ~14.8% | ~$3.69 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (288,308 resting) | ~3.5% | ~$2.65 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (36,823 resting) | ~9.5% | ~$2.38 |
| `ewc-usse-mi-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (642,391 resting) | ~37.2% | ~$2.33 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (85,652 resting) | ~36.0% | ~$2.25 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (629,776 resting) | ~6.6% | ~$1.65 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,229 resting) | ~6.1% | ~$1.53 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (133,213 resting) | ~1.7% | ~$1.29 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $500.00 ÷ 3 | 0.20 | 10,000 | BUY side (13,535 resting) | ~1.5% | ~$1.21 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (69,404 resting) | ~1.6% | ~$1.20 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $500.00 ÷ 3 | 0.20 | 10,000 | BUY side (674,268 resting) | ~1.4% | ~$1.14 |

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
| 2026-08-17 12:50 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 12:39 PM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 9:17 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 8:51 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 8:43 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 8:06 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 7:50 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 7:04 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 6:54 AM ET | ✅ ok | 2700 | $4920.49 |
| 2026-08-17 6:38 AM ET | ✅ ok | 2700 | $4920.49 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
