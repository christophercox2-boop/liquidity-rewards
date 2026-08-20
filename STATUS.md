# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 8:31 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$288.83/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — SELL at the best price, ~$13.59/day for 200 contracts. Runners-up: `ewc-usgub-ca-2026-11-03-xavbec` (~$6.61/day), `ewc-usgub-ga-2026-11-03-dem` (~$5.67/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$288.83/day (~$12.03/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-49` | SELL | 21.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.8% of ask side (92,007 resting ≥ 5,000 ✓) ≈ $3.84/day (event pool ÷ 13 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 86 | 0 | $200.00 | ✅ scoring — ~97.7% of ask side (44,791 resting ≥ 20,000 ✓) ≈ $6.98/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~93.6% of bid side (50,355 resting ≥ 20,000 ✓) ≈ $3.47/day (event pool ÷ 27 markets) |
| `aachc-cfb-wins-2026-11-28-boscol-2pt5wins` | BUY | 85.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~89.2% of bid side (17,296 resting ≥ 5,000 ✓) ≈ $3.72/day (event pool ÷ 3 markets) |
| `aachc-cfb-wins-2026-11-28-lou-8pt5wins` | SELL | 37.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~88.4% of ask side (16,472 resting ≥ 5,000 ✓) ≈ $2.21/day (event pool ÷ 5 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 15.0¢ | 146 | 0 | $100.00 | ✅ scoring — ~86.4% of bid side (805,769 resting ≥ 5,000 ✓) ≈ $3.60/day (event pool ÷ 12 markets) |
| `fptc-nfl-qbfpou-2027-01-10-danjon` | BUY | 38.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~81.4% of bid side (8,251 resting ≥ 7,500 ✓) ≈ $4.52/day (event pool ÷ 9 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 120 | 0 | $200.00 | ✅ scoring — ~77.1% of bid side (20,574 resting ≥ 20,000 ✓) ≈ $2.86/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 12.0¢ | 68 | 0 | $200.00 | ✅ scoring — ~69.6% of bid side (96,883 resting ≥ 20,000 ✓) ≈ $4.10/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-kamhar` | SELL | 5.0¢ | 286 | 0 | $200.00 | ✅ scoring — ~65.7% of ask side (67,299 resting ≥ 20,000 ✓) ≈ $2.44/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rokha` | BUY | 6.0¢ | 22 | 1 | $200.00 | ✅ scoring — ~65.7% of bid side (20,067 resting ≥ 20,000 ✓) ≈ $2.43/day (event pool ÷ 27 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 14.0¢ | 130 | 0 | $100.00 | ✅ scoring — ~62.6% of bid side (307,172 resting ≥ 5,000 ✓) ≈ $2.41/day (event pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 12.0¢ | 42 | 0 | $200.00 | ✅ scoring — ~60.0% of ask side (38,939 resting ≥ 20,000 ✓) ≈ $3.53/day (event pool ÷ 17 markets) |
| `aachc-cfb-wins-2026-11-28-iowa-8pt5wins` | BUY | 32.0¢ | 1 | 6 | $25.00 | ✅ scoring — ~59.8% of bid side (5,509 resting ≥ 5,000 ✓) ≈ $1.50/day (event pool ÷ 5 markets) |
| `ewc-usp-2028-11-07-jamtal` | BUY | 6.0¢ | 100 | 1 | $200.00 | ✅ scoring — ~59.1% of bid side (160,139 resting ≥ 20,000 ✓) ≈ $2.19/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-tulgab` | BUY | 1.0¢ | 19,238 | 2 | $200.00 | ✅ scoring — ~58.2% of bid side (29,919 resting ≥ 20,000 ✓) ≈ $4.16/day (event pool ÷ 14 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 5.0¢ | 79 | 0 | $100.00 | ✅ scoring — ~57.2% of ask side (77,535 resting ≥ 5,000 ✓) ≈ $2.20/day (event pool ÷ 13 markets) |
| `aachc-cfb-wins-2026-11-28-uk-6pt5wins` | SELL | 22.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~57.1% of ask side (32,342 resting ≥ 5,000 ✓) ≈ $1.43/day (event pool ÷ 5 markets) |
| `enwc-uspres-nom-dem-2028-dwajoh` | BUY | 1.0¢ | 19,311 | 2 | $200.00 | ✅ scoring — ~56.6% of bid side (29,921 resting ≥ 20,000 ✓) ≈ $3.33/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 7.0¢ | 83 | 0 | $200.00 | ✅ scoring — ~54.7% of bid side (36,220 resting ≥ 20,000 ✓) ≈ $2.03/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-markel` | SELL | 11.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~50.3% of ask side (22,004 resting ≥ 20,000 ✓) ≈ $2.96/day (event pool ÷ 17 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 37.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~48.8% of bid side (400,626 resting ≥ 5,000 ✓) ≈ $2.03/day (event pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 37.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~48.8% of bid side (400,626 resting ≥ 5,000 ✓) ≈ $2.03/day (event pool ÷ 12 markets) |
| `ewc-usp-2028-11-07-wesmoo` | BUY | 1.0¢ | 9,871 | 1 | $200.00 | ✅ scoring — ~47.9% of bid side (20,477 resting ≥ 20,000 ✓) ≈ $1.78/day (event pool ÷ 27 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~45.0% of bid side (24,378 resting ≥ 5,000 ✓) ≈ $11.25/day (event pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 91.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~44.0% of ask side (101,516 resting ≥ 5,000 ✓) ≈ $1.83/day (event pool ÷ 12 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 1.0¢ | 9,996 | 3 | $200.00 | ✅ scoring — ~43.3% of bid side (20,495 resting ≥ 20,000 ✓) ≈ $1.60/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-gleyou` | BUY | 1.0¢ | 9,814 | 3 | $200.00 | ✅ scoring — ~42.4% of bid side (20,469 resting ≥ 20,000 ✓) ≈ $1.57/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 19,263 | 3 | $200.00 | ✅ scoring — ~42.3% of bid side (29,939 resting ≥ 20,000 ✓) ≈ $3.02/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 19,336 | 3 | $200.00 | ✅ scoring — ~41.8% of bid side (29,943 resting ≥ 20,000 ✓) ≈ $2.98/day (event pool ÷ 14 markets) |
| …and 1632 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 1 @ 21¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 28¢ | 115 | ×0.2^7 = 0.0 |
|  | 29¢ | 148 | ×0.2^8 = 0.0 |
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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 86 @ 4¢ → $6.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 88 (86 yours) | ×0.2^0 = 88.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 3 | ×0.2^8 = 0.0 |
|  | 13¢ | 6 | ×0.2^9 = 0.0 |
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
<details><summary><code>aachc-cfb-wins-2026-11-28-boscol-2pt5wins</code> BUY 0 @ 85¢ → $3.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 1 (0 yours) | ×0.5^0 = 0.6 |
|  | 84¢ | 0 | ×0.5^1 = 0.0 |
|  | 83¢ | 0 | ×0.5^2 = 0.0 |
|  | 79¢ | 0 | ×0.5^6 = 0.0 |
|  | 63¢ | 993 | ×0.5^22 = 0.0 |
|  | 57¢ | 52 | ×0.5^28 = 0.0 |
|  | 56¢ | 16,000 | ×0.5^29 = 0.0 |
| | | **Σ** | **0.6** |

`yours 0.5 / Σ 0.6 = 89.2%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 89.2% = $3.72/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-boscol-2pt5wins` ← this one
2. `aachc-cfb-wins-2026-11-28-boscol-4pt5wins`
3. `aachc-cfb-wins-2026-11-28-boscol-5pt5wins`

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-lou-8pt5wins</code> SELL 0 @ 37¢ → $2.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 0 (0 yours) | ×0.5^0 = 0.2 |
|  | 39¢ | 0 | ×0.5^2 = 0.0 |
|  | 56¢ | 150 | ×0.5^19 = 0.0 |
|  | 60¢ | 98 | ×0.5^23 = 0.0 |
|  | 61¢ | 16,021 | ×0.5^24 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.2 / Σ 0.2 = 88.4%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 88.4% = $2.21/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-lou-10pt5wins`
2. `aachc-cfb-wins-2026-11-28-lou-6pt5wins`
3. `aachc-cfb-wins-2026-11-28-lou-7pt5wins`
4. `aachc-cfb-wins-2026-11-28-lou-8pt5wins` ← this one
5. `aachc-cfb-wins-2026-11-28-lou-9pt5wins`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 146 @ 15¢ → $3.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 169 (146 yours) | ×0.2^0 = 169.0 |
|  | 3¢ | 50 | ×0.2^12 = 0.0 |
|  | 2¢ | 5,350 | ×0.2^13 = 0.0 |
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
<details><summary><code>fptc-nfl-qbfpou-2027-01-10-danjon</code> BUY 0 @ 38¢ → $4.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 0 (0 yours) | ×0.4^0 = 0.2 |
|  | 35¢ | 1 | ×0.4^3 = 0.0 |
|  | 24¢ | 150 | ×0.4^14 = 0.0 |
|  | 1¢ | 8,100 | ×0.4^37 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.2 / Σ 0.2 = 81.4%`  
`$100 ÷ 9 ÷ 2 = $5.56 × 81.4% = $4.52/day`  

<details><summary>÷ 9 markets in this race — tap to list</summary>

1. `fptc-nfl-qbfpou-2027-01-10-calewil`
2. `fptc-nfl-qbfpou-2027-01-10-camwar`
3. `fptc-nfl-qbfpou-2027-01-10-danjon` ← this one
4. `fptc-nfl-qbfpou-2027-01-10-gensmi`
5. `fptc-nfl-qbfpou-2027-01-10-jargof`
6. `fptc-nfl-qbfpou-2027-01-10-jaydan`
7. `fptc-nfl-qbfpou-2027-01-10-jusher`
8. `fptc-nfl-qbfpou-2027-01-10-matsta`
9. `fptc-nfl-qbfpou-2027-01-10-tylsho`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 120 @ 5¢ → $2.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 122 (120 yours) | ×0.2^0 = 122.0 |
|  | 4¢ | 4 | ×0.2^1 = 0.8 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 20,443 | ×0.2^4 = 32.7 |
| | | **Σ** | **155.6** |

`yours 120.0 / Σ 155.6 = 77.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 77.1% = $2.86/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 68 @ 12¢ → $4.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 97 (68 yours) | ×0.2^0 = 97.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 8¢ | 6 | ×0.2^4 = 0.0 |
|  | 7¢ | 30 | ×0.2^5 = 0.0 |
|  | 6¢ | 125 | ×0.2^6 = 0.0 |
|  | 5¢ | 10,000 | ×0.2^7 = 0.1 |
|  | 3¢ | 171 | ×0.2^9 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^10 = 0.0 |
| | | **Σ** | **97.6** |

`yours 68.0 / Σ 97.6 = 69.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 69.6% = $4.10/day`  

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
<details><summary><code>ewc-usp-2028-11-07-kamhar</code> SELL 286 @ 5¢ → $2.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 435 (286 yours) | ×0.2^0 = 435.0 |
|  | 14¢ | 172 | ×0.2^9 = 0.0 |
|  | 19¢ | 31,724 | ×0.2^14 = 0.0 |
| | | **Σ** | **435.0** |

`yours 286.0 / Σ 435.0 = 65.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 65.7% = $2.44/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rokha</code> BUY 22 @ 6¢ → $2.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 6¢ | 22 (22 yours) | ×0.2^1 = 4.4 |
|  | 4¢ | 2 | ×0.2^3 = 0.0 |
|  | 3¢ | 5 | ×0.2^4 = 0.0 |
|  | 2¢ | 3 | ×0.2^5 = 0.0 |
|  | 1¢ | 20,034 | ×0.2^6 = 1.3 |
| | | **Σ** | **6.7** |

`yours 4.4 / Σ 6.7 = 65.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 65.7% = $2.43/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 130 @ 14¢ → $2.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 197 (130 yours) | ×0.2^0 = 196.8 |
|  | 10¢ | 6,544 | ×0.2^4 = 10.5 |
| | | **Σ** | **207.2** |

`yours 129.8 / Σ 207.2 = 62.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 62.6% = $2.41/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-iowa-8pt5wins</code> BUY 1 @ 32¢ → $1.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 38¢ | 0 | ×0.5^0 = 0.0 |
| ▶ | 32¢ | 1 (1 yours) | ×0.5^6 = 0.0 |
|  | 30¢ | 0 | ×0.5^8 = 0.0 |
|  | 15¢ | 3,333 | ×0.5^23 = 0.0 |
|  | 14¢ | 151 | ×0.5^24 = 0.0 |
|  | 6¢ | 1 | ×0.5^32 = 0.0 |
|  | 2¢ | 13 | ×0.5^36 = 0.0 |
|  | 1¢ | 2,010 | ×0.5^37 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 59.8%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 59.8% = $1.50/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-iowa-5pt5wins`
2. `aachc-cfb-wins-2026-11-28-iowa-6pt5wins`
3. `aachc-cfb-wins-2026-11-28-iowa-7pt5wins`
4. `aachc-cfb-wins-2026-11-28-iowa-8pt5wins` ← this one
5. `aachc-cfb-wins-2026-11-28-iowa-9pt5wins`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jamtal</code> BUY 100 @ 6¢ → $2.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 3 | ×0.2^0 = 3.5 |
| ▶ | 6¢ | 100 (100 yours) | ×0.2^1 = 20.0 |
|  | 4¢ | 15 | ×0.2^3 = 0.1 |
|  | 1¢ | 160,021 | ×0.2^6 = 10.2 |
| | | **Σ** | **33.9** |

`yours 20.0 / Σ 33.9 = 59.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 59.1% = $2.19/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal` ← this one
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
<details><summary><code>enwc-uspres-nom-rep-2028-tulgab</code> BUY 19,238 @ 1¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 131 | ×0.2^0 = 131.3 |
| ▶ | 1¢ | 29,788 (19,238 yours) | ×0.2^2 = 1,191.5 |
| | | **Σ** | **1,322.9** |

`yours 769.5 / Σ 1,322.9 = 58.2%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 58.2% = $4.16/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-uk-6pt5wins</code> SELL 10 @ 22¢ → $1.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 17 (10 yours) | ×0.5^0 = 16.5 |
|  | 35¢ | 53 | ×0.5^13 = 0.0 |
|  | 36¢ | 16,050 | ×0.5^14 = 1.0 |
| | | **Σ** | **17.5** |

`yours 10.0 / Σ 17.5 = 57.1%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 57.1% = $1.43/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-uk-2pt5wins`
2. `aachc-cfb-wins-2026-11-28-uk-3pt5wins`
3. `aachc-cfb-wins-2026-11-28-uk-4pt5wins`
4. `aachc-cfb-wins-2026-11-28-uk-5pt5wins`
5. `aachc-cfb-wins-2026-11-28-uk-6pt5wins` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-dwajoh</code> BUY 19,311 @ 1¢ → $3.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 133 | ×0.2^0 = 133.3 |
|  | 2¢ | 250 | ×0.2^1 = 50.0 |
| ▶ | 1¢ | 29,538 (19,311 yours) | ×0.2^2 = 1,181.5 |
| | | **Σ** | **1,364.9** |

`yours 772.4 / Σ 1,364.9 = 56.6%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 56.6% = $3.33/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 83 @ 7¢ → $2.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 137 (83 yours) | ×0.2^0 = 137.4 |
|  | 6¢ | 27 | ×0.2^1 = 5.4 |
|  | 5¢ | 31 | ×0.2^2 = 1.2 |
|  | 3¢ | 250 | ×0.2^4 = 0.4 |
|  | 2¢ | 22,500 | ×0.2^5 = 7.2 |
| | | **Σ** | **151.7** |

`yours 83.0 / Σ 151.7 = 54.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 54.7% = $2.03/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> SELL 20 @ 11¢ → $2.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 40 (20 yours) | ×0.2^0 = 39.8 |
|  | 16¢ | 1 | ×0.2^5 = 0.0 |
|  | 19¢ | 31 | ×0.2^8 = 0.0 |
|  | 20¢ | 1 | ×0.2^9 = 0.0 |
|  | 24¢ | 50 | ×0.2^13 = 0.0 |
|  | 25¢ | 10 | ×0.2^14 = 0.0 |
|  | 26¢ | 50 | ×0.2^15 = 0.0 |
|  | 45¢ | 50 | ×0.2^34 = 0.0 |
|  | 99¢ | 21,771 | ×0.2^88 = 0.0 |
| | | **Σ** | **39.8** |

`yours 20.0 / Σ 39.8 = 50.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 50.3% = $2.96/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 1 @ 37¢ → $2.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 15¢ | 173 | ×0.2^22 = 0.0 |
|  | 2¢ | 400,250 | ×0.2^35 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 48.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 48.8% = $2.03/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 1 @ 37¢ → $2.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 15¢ | 173 | ×0.2^22 = 0.0 |
|  | 2¢ | 400,250 | ×0.2^35 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 48.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 48.8% = $2.03/day`  

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
<details><summary><code>ewc-usp-2028-11-07-wesmoo</code> BUY 9,871 @ 1¢ → $1.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 28 | ×0.2^0 = 28.0 |
| ▶ | 1¢ | 20,449 (9,871 yours) | ×0.2^1 = 4,089.8 |
| | | **Σ** | **4,117.8** |

`yours 1,974.2 / Σ 4,117.8 = 47.9%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 47.9% = $1.78/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $11.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,166 (1,000 yours) | ×0.2^0 = 2,165.9 |
|  | 7¢ | 1,390 | ×0.2^2 = 55.6 |
|  | 5¢ | 501 | ×0.2^4 = 0.8 |
|  | 3¢ | 97 | ×0.2^6 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^7 = 0.3 |
| | | **Σ** | **2,222.6** |

`yours 1,000.0 / Σ 2,222.6 = 45.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 45.0% = $11.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 1 @ 91¢ → $1.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 98¢ | 99,315 | ×0.2^7 = 1.3 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 44.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 44.0% = $1.83/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180` ← this one
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 9,996 @ 1¢ → $1.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 21 | ×0.2^0 = 21.0 |
|  | 2¢ | 3 | ×0.2^2 = 0.1 |
| ▶ | 1¢ | 20,471 (9,996 yours) | ×0.2^3 = 163.8 |
| | | **Σ** | **184.9** |

`yours 80.0 / Σ 184.9 = 43.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 43.3% = $1.60/day`  

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
<details><summary><code>ewc-usp-2028-11-07-gleyou</code> BUY 9,814 @ 1¢ → $1.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 18 | ×0.2^0 = 18.0 |
|  | 3¢ | 5 | ×0.2^1 = 1.0 |
|  | 2¢ | 82 | ×0.2^2 = 3.3 |
| ▶ | 1¢ | 20,364 (9,814 yours) | ×0.2^3 = 162.9 |
| | | **Σ** | **185.2** |

`yours 78.5 / Σ 185.2 = 42.4%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 42.4% = $1.57/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou` ← this one
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
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 19,263 @ 1¢ → $3.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 126 | ×0.2^0 = 125.8 |
| ▶ | 1¢ | 29,813 (19,263 yours) | ×0.2^3 = 238.5 |
| | | **Σ** | **364.3** |

`yours 154.1 / Σ 364.3 = 42.3%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 42.3% = $3.02/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre` ← this one
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
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 19,336 @ 1¢ → $2.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 132 | ×0.2^0 = 131.8 |
| ▶ | 1¢ | 29,811 (19,336 yours) | ×0.2^3 = 238.5 |
| | | **Σ** | **370.2** |

`yours 154.7 / Σ 370.2 = 41.8%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 41.8% = $2.98/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus` ← this one
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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (91,137 resting) | ~54.3% | ~$13.59 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (24,978 resting) | ~8.8% | ~$6.61 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,469 resting) | ~7.6% | ~$5.67 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (929,326 resting) | ~5.2% | ~$3.90 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (82,068 resting) | ~7.0% | ~$1.75 |
| `ewc-usse-ne-2026-11-03-danosb` | $25.00 ÷ 3 | 0.10 | 2,000 | BUY side (83,511 resting) | ~40.2% | ~$1.67 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (630,756 resting) | ~6.5% | ~$1.63 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (39,953 resting) | ~6.4% | ~$1.61 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,240,507 resting) | ~24.9% | ~$1.56 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (75,300 resting) | ~21.5% | ~$1.35 |
| `ewc-usse-nc-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (76,324 resting) | ~4.5% | ~$1.13 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (6,489 resting) | ~4.2% | ~$1.05 |

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
| 2026-08-20 8:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 7:30 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 6:13 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 4:57 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 3:54 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 2:53 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 1:52 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:49 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 11:48 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 10:48 PM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
