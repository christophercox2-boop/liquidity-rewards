# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 4:10 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$145.12/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$59.61/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$15.47/day), `ewc-usgub-ca-2026-11-03-xavbec` (~$13.87/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$145.12/day (~$6.05/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 57.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,211 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 52.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,205 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 14.0¢ | 16 | 0 | $200.00 | ✅ scoring — ~99.1% of bid side (93,033 resting ≥ 20,000 ✓) ≈ $5.83/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~94.0% of ask side (57,251 resting ≥ 20,000 ✓) ≈ $3.48/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-tulgab` | SELL | 7.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~94.0% of ask side (50,829 resting ≥ 20,000 ✓) ≈ $3.48/day (event pool ÷ 27 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~93.7% of ask side (65,511 resting ≥ 2,000 ✓) ≈ $5.86/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~93.6% of bid side (50,355 resting ≥ 20,000 ✓) ≈ $3.47/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 91.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~91.4% of bid side (500,485 resting ≥ 2,000 ✓) ≈ $5.71/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 37 | 0 | $200.00 | ✅ scoring — ~86.8% of ask side (44,648 resting ≥ 20,000 ✓) ≈ $6.20/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | BUY | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~66.2% of bid side (2,001 resting ≥ 2,000 ✓) ≈ $4.14/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | SELL | 5.0¢ | 32 | 0 | $200.00 | ✅ scoring — ~62.7% of ask side (48,294 resting ≥ 20,000 ✓) ≈ $3.69/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 7.0¢ | 83 | 0 | $200.00 | ✅ scoring — ~58.4% of bid side (64,510 resting ≥ 20,000 ✓) ≈ $2.16/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-ct-2026-11-03-rep` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~49.7% of ask side (199,489 resting ≥ 2,000 ✓) ≈ $3.11/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 119 | 0 | $200.00 | ✅ scoring — ~49.0% of bid side (75,573 resting ≥ 20,000 ✓) ≈ $1.82/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 1 | $200.00 | ✅ scoring — ~44.6% of bid side (85,165 resting ≥ 20,000 ✓) ≈ $1.65/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-thomas` | SELL | 3.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~42.8% of ask side (71,502 resting ≥ 20,000 ✓) ≈ $1.59/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-tulgab` | BUY | 1.0¢ | 19,238 | 2 | $200.00 | ✅ scoring — ~42.7% of bid side (41,919 resting ≥ 20,000 ✓) ≈ $3.05/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-elomus` | SELL | 5.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~41.7% of ask side (51,539 resting ≥ 20,000 ✓) ≈ $1.54/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 9.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~41.1% of bid side (20,490 resting ≥ 20,000 ✓) ≈ $1.52/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jonste` | SELL | 7.0¢ | 35 | 0 | $200.00 | ✅ scoring — ~40.2% of ask side (53,476 resting ≥ 20,000 ✓) ≈ $2.37/day (event pool ÷ 17 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~38.4% of bid side (24,800 resting ≥ 5,000 ✓) ≈ $9.59/day (event pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | SELL | 2.0¢ | 85 | 0 | $25.00 | ✅ scoring — ~37.0% of ask side (308,493 resting ≥ 2,000 ✓) ≈ $2.31/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-tuccar` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~36.3% of ask side (55,827 resting ≥ 20,000 ✓) ≈ $1.35/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 5.0¢ | 10 | 0 | $200.00 | ✅ scoring — ~33.3% of ask side (58,290 resting ≥ 20,000 ✓) ≈ $1.96/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | SELL | 21.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~32.7% of ask side (49,356 resting ≥ 20,000 ✓) ≈ $1.92/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 12.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~29.8% of ask side (38,771 resting ≥ 20,000 ✓) ≈ $1.75/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-jbpri` | SELL | 9.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~28.5% of ask side (71,426 resting ≥ 20,000 ✓) ≈ $1.05/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-wesmoo` | SELL | 5.0¢ | 26 | 0 | $200.00 | ✅ scoring — ~26.8% of ask side (48,319 resting ≥ 20,000 ✓) ≈ $1.58/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-wesmoo` | SELL | 5.0¢ | 25 | 0 | $200.00 | ✅ scoring — ~25.8% of ask side (48,319 resting ≥ 20,000 ✓) ≈ $1.52/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | SELL | 8.0¢ | 6 | 0 | $200.00 | ✅ scoring — ~25.0% of ask side (54,482 resting ≥ 20,000 ✓) ≈ $1.47/day (event pool ÷ 17 markets) |
| …and 1773 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 1 @ 57¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 21¢ | 10 | ×0.1^36 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^55 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 1 @ 52¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 52¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 40¢ | 1 | ×0.1^12 = 0.0 |
|  | 21¢ | 3 | ×0.1^31 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^50 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 16 @ 14¢ → $5.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 16 (16 yours) | ×0.2^0 = 16.3 |
|  | 12¢ | 3 | ×0.2^2 = 0.1 |
|  | 11¢ | 2 | ×0.2^3 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 8¢ | 6 | ×0.2^6 = 0.0 |
|  | 7¢ | 30 | ×0.2^7 = 0.0 |
|  | 6¢ | 112 | ×0.2^8 = 0.0 |
|  | 5¢ | 13 | ×0.2^9 = 0.0 |
|  | 4¢ | 6,250 | ×0.2^10 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^12 = 0.0 |
| | | **Σ** | **16.4** |

`yours 16.3 / Σ 16.4 = 99.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 99.1% = $5.83/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 1 @ 6¢ → $3.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 1 | ×0.2^6 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 14¢ | 458 | ×0.2^8 = 0.0 |
|  | 15¢ | 36,415 | ×0.2^9 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 94.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 94.0% = $3.48/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> SELL 1 @ 7¢ → $3.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 10¢ | 8 | ×0.2^3 = 0.1 |
|  | 13¢ | 1 | ×0.2^6 = 0.0 |
|  | 20¢ | 287 | ×0.2^13 = 0.0 |
|  | 25¢ | 30,266 | ×0.2^18 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 94.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 94.0% = $3.48/day`  

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 30 @ 2¢ → $5.86/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 32 (30 yours) | ×0.1^0 = 32.0 |
|  | 5¢ | 4 | ×0.1^3 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^96 = 0.0 |
| | | **Σ** | **32.0** |

`yours 30.0 / Σ 32.0 = 93.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.7% = $5.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 144 (135 yours) | ×0.2^0 = 143.5 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **144.2** |

`yours 135.0 / Σ 144.2 = 93.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 93.6% = $3.47/day`  

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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 3 @ 91¢ → $5.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 88¢ | 282 | ×0.1^3 = 0.3 |
|  | 2¢ | 500,000 | ×0.1^89 = 0.0 |
| | | **Σ** | **3.3** |

`yours 3.0 / Σ 3.3 = 91.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 91.4% = $5.71/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 37 @ 4¢ → $6.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 42 (37 yours) | ×0.2^0 = 42.0 |
|  | 5¢ | 3 | ×0.2^1 = 0.6 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 3 | ×0.2^8 = 0.0 |
|  | 13¢ | 6 | ×0.2^9 = 0.0 |
|  | 14¢ | 5 | ×0.2^10 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^11 = 0.0 |
| | | **Σ** | **42.6** |

`yours 37.0 / Σ 42.6 = 86.8%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 86.8% = $6.20/day`  

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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> BUY 1 @ 5¢ → $4.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 4¢ | 1 | ×0.1^1 = 0.1 |
|  | 2¢ | 233 | ×0.1^3 = 0.2 |
|  | 1¢ | 1,766 | ×0.1^4 = 0.2 |
| | | **Σ** | **1.5** |

`yours 1.0 / Σ 1.5 = 66.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.2% = $4.14/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> SELL 32 @ 5¢ → $3.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 51 (32 yours) | ×0.2^0 = 51.0 |
|  | 15¢ | 30,493 | ×0.2^10 = 0.0 |
| | | **Σ** | **51.0** |

`yours 32.0 / Σ 51.0 = 62.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 62.7% = $3.69/day`  

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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 83 @ 7¢ → $2.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 95 (83 yours) | ×0.2^0 = 95.4 |
|  | 6¢ | 27 | ×0.2^1 = 5.4 |
|  | 5¢ | 31 | ×0.2^2 = 1.2 |
|  | 3¢ | 18,582 | ×0.2^4 = 29.7 |
|  | 2¢ | 32,500 | ×0.2^5 = 10.4 |
| | | **Σ** | **142.2** |

`yours 83.0 / Σ 142.2 = 58.4%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 58.4% = $2.16/day`  

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
<details><summary><code>usgubewc-usgub-ct-2026-11-03-rep</code> SELL 1 @ 7¢ → $3.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 9¢ | 1 | ×0.1^2 = 0.0 |
|  | 12¢ | 86 | ×0.1^5 = 0.0 |
|  | 98¢ | 199,175 | ×0.1^91 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 49.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.7% = $3.11/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem`
2. `usgubewc-usgub-ct-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 119 @ 5¢ → $1.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 121 (119 yours) | ×0.2^0 = 121.0 |
|  | 4¢ | 4 | ×0.2^1 = 0.8 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 75,443 | ×0.2^4 = 120.7 |
| | | **Σ** | **242.6** |

`yours 119.0 / Σ 242.6 = 49.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 49.0% = $1.82/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 5¢ | 158 (135 yours) | ×0.2^1 = 31.6 |
|  | 4¢ | 18 | ×0.2^2 = 0.7 |
|  | 2¢ | 13 | ×0.2^4 = 0.0 |
|  | 1¢ | 84,975 | ×0.2^5 = 27.2 |
| | | **Σ** | **60.5** |

`yours 27.0 / Σ 60.5 = 44.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 44.6% = $1.65/day`  

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
<details><summary><code>ewc-usp-2028-11-07-thomas</code> SELL 3 @ 3¢ → $1.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 7 (3 yours) | ×0.2^0 = 7.0 |
|  | 7¢ | 1 | ×0.2^4 = 0.0 |
|  | 8¢ | 17 | ×0.2^5 = 0.0 |
|  | 20¢ | 206 | ×0.2^17 = 0.0 |
|  | 21¢ | 51,021 | ×0.2^18 = 0.0 |
| | | **Σ** | **7.0** |

`yours 3.0 / Σ 7.0 = 42.8%`  
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
<details><summary><code>enwc-uspres-nom-rep-2028-tulgab</code> BUY 19,238 @ 1¢ → $3.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 131 | ×0.2^0 = 131.3 |
| ▶ | 1¢ | 41,788 (19,238 yours) | ×0.2^2 = 1,671.5 |
| | | **Σ** | **1,802.9** |

`yours 769.5 / Σ 1,802.9 = 42.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 42.7% = $3.05/day`  

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
<details><summary><code>ewc-usp-2028-11-07-elomus</code> SELL 3 @ 5¢ → $1.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 7 (3 yours) | ×0.2^0 = 7.0 |
|  | 6¢ | 1 | ×0.2^1 = 0.2 |
|  | 10¢ | 2 | ×0.2^5 = 0.0 |
|  | 12¢ | 3 | ×0.2^7 = 0.0 |
|  | 14¢ | 1 | ×0.2^9 = 0.0 |
|  | 16¢ | 4 | ×0.2^11 = 0.0 |
|  | 17¢ | 275 | ×0.2^12 = 0.0 |
|  | 20¢ | 31,021 | ×0.2^15 = 0.0 |
| | | **Σ** | **7.2** |

`yours 3.0 / Σ 7.2 = 41.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 41.7% = $1.54/day`  

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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 50 @ 9¢ → $1.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 122 (50 yours) | ×0.2^0 = 121.5 |
|  | 1¢ | 20,368 | ×0.2^8 = 0.1 |
| | | **Σ** | **121.6** |

`yours 50.0 / Σ 121.6 = 41.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 41.1% = $1.52/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonste</code> SELL 35 @ 7¢ → $2.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 87 (35 yours) | ×0.2^0 = 87.0 |
|  | 13¢ | 4 | ×0.2^6 = 0.0 |
|  | 14¢ | 7 | ×0.2^7 = 0.0 |
|  | 19¢ | 4 | ×0.2^12 = 0.0 |
|  | 21¢ | 95 | ×0.2^14 = 0.0 |
|  | 22¢ | 50,529 | ×0.2^15 = 0.0 |
| | | **Σ** | **87.0** |

`yours 35.0 / Σ 87.0 = 40.2%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 40.2% = $2.37/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $9.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,530 (1,000 yours) | ×0.2^0 = 2,529.8 |
|  | 8¢ | 100 | ×0.2^1 = 20.0 |
|  | 7¢ | 1,390 | ×0.2^2 = 55.6 |
|  | 5¢ | 501 | ×0.2^4 = 0.8 |
|  | 3¢ | 80 | ×0.2^6 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^7 = 0.3 |
| | | **Σ** | **2,606.5** |

`yours 1,000.0 / Σ 2,606.5 = 38.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 38.4% = $9.59/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> SELL 85 @ 2¢ → $2.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 230 (85 yours) | ×0.1^0 = 230.0 |
|  | 49¢ | 5,000 | ×0.1^47 = 0.0 |
| | | **Σ** | **230.0** |

`yours 85.0 / Σ 230.0 = 37.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 37.0% = $2.31/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tuccar</code> SELL 3 @ 6¢ → $1.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 8 (3 yours) | ×0.2^0 = 8.1 |
|  | 7¢ | 1 | ×0.2^1 = 0.2 |
|  | 14¢ | 1 | ×0.2^8 = 0.0 |
|  | 26¢ | 21,262 | ×0.2^20 = 0.0 |
| | | **Σ** | **8.3** |

`yours 3.0 / Σ 8.3 = 36.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 36.3% = $1.35/day`  

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
24. `ewc-usp-2028-11-07-tuccar` ← this one
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 10 @ 5¢ → $1.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 30 (10 yours) | ×0.2^0 = 30.0 |
|  | 13¢ | 4 | ×0.2^8 = 0.0 |
|  | 18¢ | 3 | ×0.2^13 = 0.0 |
|  | 19¢ | 3 | ×0.2^14 = 0.0 |
|  | 20¢ | 40,501 | ×0.2^15 = 0.0 |
| | | **Σ** | **30.0** |

`yours 10.0 / Σ 30.0 = 33.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 33.3% = $1.96/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> SELL 3 @ 21¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 7 (3 yours) | ×0.2^0 = 7.0 |
|  | 23¢ | 1 | ×0.2^2 = 0.0 |
|  | 24¢ | 265 | ×0.2^3 = 2.1 |
|  | 30¢ | 46,331 | ×0.2^9 = 0.0 |
| | | **Σ** | **9.2** |

`yours 3.0 / Σ 9.2 = 32.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 32.7% = $1.92/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> SELL 3 @ 12¢ → $1.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 10 (3 yours) | ×0.2^0 = 10.0 |
|  | 14¢ | 1 | ×0.2^2 = 0.0 |
|  | 16¢ | 16 | ×0.2^4 = 0.0 |
|  | 19¢ | 4 | ×0.2^7 = 0.0 |
|  | 26¢ | 20,990 | ×0.2^14 = 0.0 |
| | | **Σ** | **10.1** |

`yours 3.0 / Σ 10.1 = 29.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 29.8% = $1.75/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> SELL 1 @ 9¢ → $1.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 3 (1 yours) | ×0.2^0 = 3.0 |
|  | 10¢ | 1 | ×0.2^1 = 0.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 3 | ×0.2^3 = 0.0 |
|  | 13¢ | 154 | ×0.2^4 = 0.2 |
|  | 15¢ | 14 | ×0.2^6 = 0.0 |
|  | 22¢ | 51,000 | ×0.2^13 = 0.0 |
| | | **Σ** | **3.5** |

`yours 1.0 / Σ 3.5 = 28.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 28.5% = $1.05/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-wesmoo</code> SELL 26 @ 5¢ → $1.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 96 (26 yours) | ×0.2^0 = 96.0 |
|  | 7¢ | 16 | ×0.2^2 = 0.7 |
|  | 11¢ | 4 | ×0.2^6 = 0.0 |
|  | 12¢ | 30,453 | ×0.2^7 = 0.4 |
| | | **Σ** | **97.0** |

`yours 26.0 / Σ 97.0 = 26.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 26.8% = $1.58/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-wesmoo</code> SELL 25 @ 5¢ → $1.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 96 (25 yours) | ×0.2^0 = 96.0 |
|  | 7¢ | 16 | ×0.2^2 = 0.7 |
|  | 11¢ | 4 | ×0.2^6 = 0.0 |
|  | 12¢ | 30,453 | ×0.2^7 = 0.4 |
| | | **Σ** | **97.0** |

`yours 25.0 / Σ 97.0 = 25.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 25.8% = $1.52/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> SELL 6 @ 8¢ → $1.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 13 (6 yours) | ×0.2^0 = 13.4 |
|  | 11¢ | 5 | ×0.2^3 = 0.0 |
|  | 13¢ | 37,951 | ×0.2^5 = 12.1 |
| | | **Σ** | **25.6** |

`yours 6.4 / Σ 25.6 = 25.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 25.0% = $1.47/day`  

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
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (68,905 resting) | ~79.5% | ~$59.61 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (147,066 resting) | ~20.6% | ~$15.47 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (25,748 resting) | ~18.5% | ~$13.87 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (923,050 resting) | ~16.6% | ~$12.49 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (682,879 resting) | ~7.2% | ~$5.38 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (73,943 resting) | ~70.1% | ~$4.38 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (627,494 resting) | ~16.8% | ~$4.21 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (47,301 resting) | ~15.6% | ~$3.89 |
| `ewc-usse-nc-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (60,037 resting) | ~14.8% | ~$3.69 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,708 resting) | ~3.2% | ~$2.42 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (34,599 resting) | ~9.5% | ~$2.38 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (80,733 resting) | ~9.0% | ~$2.26 |

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
| 2026-08-20 4:10 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:42 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 11:41 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 10:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 9:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 8:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 7:30 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 6:13 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 4:57 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 3:54 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
