# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 9:32 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$272.69/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usse-tx-2026-11-03-rep` — BUY at the best price, ~$9.22/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$9.18/day), `ewc-usgub-ca-2026-11-03-xavbec` (~$6.53/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$272.69/day (~$11.36/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 16.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~99.3% of bid side (96,739 resting ≥ 20,000 ✓) ≈ $5.84/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 86 | 0 | $200.00 | ✅ scoring — ~97.7% of ask side (44,791 resting ≥ 20,000 ✓) ≈ $6.98/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~93.0% of bid side (50,356 resting ≥ 20,000 ✓) ≈ $3.44/day (event pool ÷ 27 markets) |
| `aachc-cfb-wins-2026-11-28-mspst-3pt5wins` | BUY | 67.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~78.9% of bid side (17,300 resting ≥ 5,000 ✓) ≈ $3.29/day (event pool ÷ 3 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 7.0¢ | 83 | 0 | $200.00 | ✅ scoring — ~75.7% of bid side (36,178 resting ≥ 20,000 ✓) ≈ $2.80/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 120 | 0 | $200.00 | ✅ scoring — ~72.3% of bid side (20,584 resting ≥ 20,000 ✓) ≈ $2.68/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-kamhar` | SELL | 5.0¢ | 286 | 0 | $200.00 | ✅ scoring — ~65.7% of ask side (67,299 resting ≥ 20,000 ✓) ≈ $2.44/day (event pool ÷ 27 markets) |
| `aachc-cfb-wins-2026-11-28-uk-6pt5wins` | SELL | 22.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~60.5% of ask side (32,341 resting ≥ 5,000 ✓) ≈ $1.51/day (event pool ÷ 5 markets) |
| `enwc-uspres-nom-rep-2028-tulgab` | BUY | 1.0¢ | 19,238 | 2 | $200.00 | ✅ scoring — ~58.2% of bid side (29,919 resting ≥ 20,000 ✓) ≈ $4.16/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | SELL | 8.0¢ | 38 | 0 | $200.00 | ✅ scoring — ~57.7% of ask side (53,652 resting ≥ 20,000 ✓) ≈ $3.39/day (event pool ÷ 17 markets) |
| `aachc-cfb-wins-2026-11-28-ncst-9pt5wins` | SELL | 16.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~57.3% of ask side (40,476 resting ≥ 5,000 ✓) ≈ $1.79/day (event pool ÷ 4 markets) |
| `enwc-uspres-nom-dem-2028-dwajoh` | BUY | 1.0¢ | 19,311 | 2 | $200.00 | ✅ scoring — ~56.6% of bid side (29,921 resting ≥ 20,000 ✓) ≈ $3.33/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-jamtal` | BUY | 6.0¢ | 100 | 2 | $200.00 | ✅ scoring — ~52.1% of bid side (160,138 resting ≥ 20,000 ✓) ≈ $1.93/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rokha` | BUY | 6.0¢ | 22 | 1 | $200.00 | ✅ scoring — ~50.7% of bid side (20,064 resting ≥ 20,000 ✓) ≈ $1.88/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-wesmoo` | BUY | 1.0¢ | 9,871 | 2 | $200.00 | ✅ scoring — ~48.2% of bid side (20,447 resting ≥ 20,000 ✓) ≈ $1.79/day (event pool ÷ 27 markets) |
| `aqc-nfl-2027-01-10-playoffq-bal` | BUY | 77.0¢ | 0 | 2 | $300.00 | ✅ scoring — ~47.4% of bid side (249,956 resting ≥ 15,000 ✓) ≈ $7.89/day (event pool ÷ 9 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~45.0% of bid side (24,332 resting ≥ 5,000 ✓) ≈ $11.25/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 1.0¢ | 9,996 | 3 | $200.00 | ✅ scoring — ~43.3% of bid side (20,495 resting ≥ 20,000 ✓) ≈ $1.60/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-gleyou` | BUY | 1.0¢ | 9,814 | 3 | $200.00 | ✅ scoring — ~42.4% of bid side (20,469 resting ≥ 20,000 ✓) ≈ $1.57/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 9.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~41.8% of bid side (20,463 resting ≥ 20,000 ✓) ≈ $1.55/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 19,336 | 3 | $200.00 | ✅ scoring — ~41.8% of bid side (29,943 resting ≥ 20,000 ✓) ≈ $2.98/day (event pool ÷ 14 markets) |
| `aachc-cfb-wins-2026-11-28-boise-6pt5wins` | BUY | 81.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~40.3% of bid side (33,064 resting ≥ 5,000 ✓) ≈ $1.01/day (event pool ÷ 5 markets) |
| `enwc-uspres-nom-dem-2028-jonste` | SELL | 7.0¢ | 35 | 0 | $200.00 | ✅ scoring — ~40.2% of ask side (53,569 resting ≥ 20,000 ✓) ≈ $2.37/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-rokha` | SELL | 14.0¢ | 36 | 2 | $200.00 | ✅ scoring — ~40.0% of ask side (50,899 resting ≥ 20,000 ✓) ≈ $1.48/day (event pool ÷ 27 markets) |
| `fptc-nfl-rbfpou-2027-01-10-rjhar` | BUY | 48.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~39.5% of bid side (8,252 resting ≥ 7,500 ✓) ≈ $0.79/day (event pool ÷ 25 markets) |
| `aachc-cfb-wins-2026-11-28-miss-5pt5wins` | SELL | 78.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~38.6% of ask side (26,312 resting ≥ 5,000 ✓) ≈ $0.96/day (event pool ÷ 5 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 1 | $200.00 | ✅ scoring — ~35.1% of bid side (30,308 resting ≥ 20,000 ✓) ≈ $1.30/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 1 | $200.00 | ✅ scoring — ~35.1% of bid side (30,308 resting ≥ 20,000 ✓) ≈ $1.30/day (event pool ÷ 27 markets) |
| `aachc-cfb-wins-2026-11-28-txam-9pt5wins` | SELL | 40.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~34.8% of ask side (5,700 resting ≥ 5,000 ✓) ≈ $1.09/day (event pool ÷ 4 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 19,263 | 3 | $200.00 | ✅ scoring — ~34.7% of bid side (39,939 resting ≥ 20,000 ✓) ≈ $2.48/day (event pool ÷ 14 markets) |
| …and 1501 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 1 @ 16¢ → $5.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 12¢ | 4 | ×0.2^4 = 0.0 |
|  | 11¢ | 2 | ×0.2^5 = 0.0 |
|  | 10¢ | 2 | ×0.2^6 = 0.0 |
|  | 8¢ | 6 | ×0.2^8 = 0.0 |
|  | 6¢ | 125 | ×0.2^10 = 0.0 |
|  | 5¢ | 10,000 | ×0.2^11 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 99.3% = $5.84/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 144 (135 yours) | ×0.2^0 = 144.5 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **145.2** |

`yours 135.0 / Σ 145.2 = 93.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 93.0% = $3.44/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-mspst-3pt5wins</code> BUY 0 @ 67¢ → $3.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 0 (0 yours) | ×0.5^0 = 0.5 |
|  | 53¢ | 50 | ×0.5^14 = 0.0 |
|  | 51¢ | 49 | ×0.5^16 = 0.0 |
|  | 50¢ | 17,000 | ×0.5^17 = 0.1 |
| | | **Σ** | **0.6** |

`yours 0.5 / Σ 0.6 = 78.9%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 78.9% = $3.29/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-mspst-2pt5wins`
2. `aachc-cfb-wins-2026-11-28-mspst-3pt5wins` ← this one
3. `aachc-cfb-wins-2026-11-28-mspst-6pt5wins`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 83 @ 7¢ → $2.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 95 (83 yours) | ×0.2^0 = 95.4 |
|  | 6¢ | 27 | ×0.2^1 = 5.4 |
|  | 5¢ | 31 | ×0.2^2 = 1.2 |
|  | 3¢ | 250 | ×0.2^4 = 0.4 |
|  | 2¢ | 22,500 | ×0.2^5 = 7.2 |
| | | **Σ** | **109.7** |

`yours 83.0 / Σ 109.7 = 75.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 75.7% = $2.80/day`  

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
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 120 @ 5¢ → $2.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 132 (120 yours) | ×0.2^0 = 132.4 |
|  | 4¢ | 4 | ×0.2^1 = 0.8 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 20,443 | ×0.2^4 = 32.7 |
| | | **Σ** | **166.0** |

`yours 120.0 / Σ 166.0 = 72.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 72.3% = $2.68/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-uk-6pt5wins</code> SELL 10 @ 22¢ → $1.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 16 (10 yours) | ×0.5^0 = 15.5 |
|  | 35¢ | 53 | ×0.5^13 = 0.0 |
|  | 36¢ | 16,050 | ×0.5^14 = 1.0 |
| | | **Σ** | **16.5** |

`yours 10.0 / Σ 16.5 = 60.5%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 60.5% = $1.51/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-uk-2pt5wins`
2. `aachc-cfb-wins-2026-11-28-uk-3pt5wins`
3. `aachc-cfb-wins-2026-11-28-uk-4pt5wins`
4. `aachc-cfb-wins-2026-11-28-uk-5pt5wins`
5. `aachc-cfb-wins-2026-11-28-uk-6pt5wins` ← this one

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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> SELL 38 @ 8¢ → $3.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 54 (38 yours) | ×0.2^0 = 54.0 |
|  | 11¢ | 4 | ×0.2^3 = 0.0 |
|  | 13¢ | 37,032 | ×0.2^5 = 11.9 |
| | | **Σ** | **65.9** |

`yours 38.0 / Σ 65.9 = 57.7%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 57.7% = $3.39/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-ncst-9pt5wins</code> SELL 0 @ 16¢ → $1.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 0 (0 yours) | ×0.5^0 = 0.5 |
|  | 31¢ | 128 | ×0.5^15 = 0.0 |
|  | 32¢ | 24,126 | ×0.5^16 = 0.4 |
| | | **Σ** | **0.9** |

`yours 0.5 / Σ 0.9 = 57.3%`  
`$25 ÷ 4 ÷ 2 = $3.12 × 57.3% = $1.79/day`  

<details><summary>÷ 4 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-ncst-6pt5wins`
2. `aachc-cfb-wins-2026-11-28-ncst-7pt5wins`
3. `aachc-cfb-wins-2026-11-28-ncst-8pt5wins`
4. `aachc-cfb-wins-2026-11-28-ncst-9pt5wins` ← this one

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
<details><summary><code>ewc-usp-2028-11-07-jamtal</code> BUY 100 @ 6¢ → $1.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 2 | ×0.2^0 = 1.6 |
| ▶ | 6¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 4¢ | 15 | ×0.2^4 = 0.0 |
|  | 1¢ | 160,021 | ×0.2^7 = 2.0 |
| | | **Σ** | **7.7** |

`yours 4.0 / Σ 7.7 = 52.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 52.1% = $1.93/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rokha</code> BUY 22 @ 6¢ → $1.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 3 | ×0.2^0 = 3.0 |
| ▶ | 6¢ | 22 (22 yours) | ×0.2^1 = 4.4 |
|  | 4¢ | 2 | ×0.2^3 = 0.0 |
|  | 3¢ | 5 | ×0.2^4 = 0.0 |
|  | 2¢ | 3 | ×0.2^5 = 0.0 |
|  | 1¢ | 20,029 | ×0.2^6 = 1.3 |
| | | **Σ** | **8.7** |

`yours 4.4 / Σ 8.7 = 50.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 50.7% = $1.88/day`  

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
<details><summary><code>ewc-usp-2028-11-07-wesmoo</code> BUY 9,871 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
|  | 2¢ | 2 | ×0.2^1 = 0.4 |
| ▶ | 1¢ | 20,444 (9,871 yours) | ×0.2^2 = 817.8 |
| | | **Σ** | **819.2** |

`yours 394.8 / Σ 819.2 = 48.2%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 48.2% = $1.79/day`  

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
<details><summary><code>aqc-nfl-2027-01-10-playoffq-bal</code> BUY 0 @ 77¢ → $7.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 79¢ | 0 | ×0.3^0 = 0.1 |
| ▶ | 77¢ | 0 (0 yours) | ×0.3^2 = 0.0 |
|  | 58¢ | 48 | ×0.3^21 = 0.0 |
|  | 57¢ | 18,821 | ×0.3^22 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 47.4%`  
`$300 ÷ 9 ÷ 2 = $16.67 × 47.4% = $7.89/day`  

<details><summary>÷ 9 markets in this race — tap to list</summary>

1. `aqc-nfl-2027-01-10-playoffq-bal` ← this one
2. `aqc-nfl-2027-01-10-playoffq-buf`
3. `aqc-nfl-2027-01-10-playoffq-cin`
4. `aqc-nfl-2027-01-10-playoffq-cle`
5. `aqc-nfl-2027-01-10-playoffq-dal`
6. `aqc-nfl-2027-01-10-playoffq-gb`
7. `aqc-nfl-2027-01-10-playoffq-sea`
8. `aqc-nfl-2027-01-10-playoffq-sf`
9. `aqc-nfl-2027-01-10-playoffq-was`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $11.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,166 (1,000 yours) | ×0.2^0 = 2,165.9 |
|  | 7¢ | 1,390 | ×0.2^2 = 55.6 |
|  | 5¢ | 501 | ×0.2^4 = 0.8 |
|  | 3¢ | 50 | ×0.2^6 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^7 = 0.3 |
| | | **Σ** | **2,222.6** |

`yours 1,000.0 / Σ 2,222.6 = 45.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 45.0% = $11.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 50 @ 9¢ → $1.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 120 (50 yours) | ×0.2^0 = 119.5 |
|  | 1¢ | 20,343 | ×0.2^8 = 0.1 |
| | | **Σ** | **119.6** |

`yours 50.0 / Σ 119.6 = 41.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 41.8% = $1.55/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-boise-6pt5wins</code> BUY 0 @ 81¢ → $1.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 81¢ | 0 (0 yours) | ×0.5^0 = 0.2 |
|  | 68¢ | 27 | ×0.5^13 = 0.0 |
|  | 67¢ | 787 | ×0.5^14 = 0.0 |
|  | 65¢ | 16,050 | ×0.5^16 = 0.2 |
| | | **Σ** | **0.5** |

`yours 0.2 / Σ 0.5 = 40.3%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 40.3% = $1.01/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-boise-5pt5wins`
2. `aachc-cfb-wins-2026-11-28-boise-6pt5wins` ← this one
3. `aachc-cfb-wins-2026-11-28-boise-7pt5wins`
4. `aachc-cfb-wins-2026-11-28-boise-8pt5wins`
5. `aachc-cfb-wins-2026-11-28-boise-9pt5wins`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jonste</code> SELL 35 @ 7¢ → $2.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 87 (35 yours) | ×0.2^0 = 87.0 |
|  | 13¢ | 34 | ×0.2^6 = 0.0 |
|  | 14¢ | 10 | ×0.2^7 = 0.0 |
|  | 19¢ | 14 | ×0.2^12 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-rokha</code> SELL 36 @ 14¢ → $1.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 1 | ×0.2^0 = 1.0 |
|  | 13¢ | 5 | ×0.2^1 = 1.0 |
| ▶ | 14¢ | 40 (36 yours) | ×0.2^2 = 1.6 |
|  | 20¢ | 287 | ×0.2^8 = 0.0 |
|  | 21¢ | 50 | ×0.2^9 = 0.0 |
|  | 25¢ | 30,266 | ×0.2^13 = 0.0 |
| | | **Σ** | **3.6** |

`yours 1.4 / Σ 3.6 = 40.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 40.0% = $1.48/day`  

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
<details><summary><code>fptc-nfl-rbfpou-2027-01-10-rjhar</code> BUY 1 @ 48¢ → $0.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 3 (1 yours) | ×0.4^0 = 2.5 |
|  | 37¢ | 50 | ×0.4^11 = 0.0 |
|  | 1¢ | 8,199 | ×0.4^47 = 0.0 |
| | | **Σ** | **2.5** |

`yours 1.0 / Σ 2.5 = 39.5%`  
`$100 ÷ 25 ÷ 2 = $2.00 × 39.5% = $0.79/day`  

<details><summary>÷ 25 markets in this race — tap to list</summary>

1. `fptc-nfl-rbfpou-2027-01-10-aarjon`
2. `fptc-nfl-rbfpou-2027-01-10-ashjea`
3. `fptc-nfl-rbfpou-2027-01-10-bhatut`
4. `fptc-nfl-rbfpou-2027-01-10-bijrob`
5. `fptc-nfl-rbfpou-2027-01-10-blacor`
6. `fptc-nfl-rbfpou-2027-01-10-bucirv`
7. `fptc-nfl-rbfpou-2027-01-10-camska`
8. `fptc-nfl-rbfpou-2027-01-10-chrmcc`
9. `fptc-nfl-rbfpou-2027-01-10-chuhub`
10. `fptc-nfl-rbfpou-2027-01-10-davmon`
11. `fptc-nfl-rbfpou-2027-01-10-dswi`
12. `fptc-nfl-rbfpou-2027-01-10-dylsam`
13. `fptc-nfl-rbfpou-2027-01-10-jadpri`
14. `fptc-nfl-rbfpou-2027-01-10-jamcoo`
15. `fptc-nfl-rbfpou-2027-01-10-jaywar`
16. `fptc-nfl-rbfpou-2027-01-10-jdob`
17. `fptc-nfl-rbfpou-2027-01-10-kenwal`
18. `fptc-nfl-rbfpou-2027-01-10-kyrwil`
19. `fptc-nfl-rbfpou-2027-01-10-omaham`
20. `fptc-nfl-rbfpou-2027-01-10-racwhi`
21. `fptc-nfl-rbfpou-2027-01-10-rhaste`
22. `fptc-nfl-rbfpou-2027-01-10-rjhar` ← this one
23. `fptc-nfl-rbfpou-2027-01-10-tylall`
24. `fptc-nfl-rbfpou-2027-01-10-tyrtra`
25. `fptc-nfl-rbfpou-2027-01-10-woomar`

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-miss-5pt5wins</code> SELL 0 @ 78¢ → $0.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 0 (0 yours) | ×0.5^0 = 0.5 |
|  | 93¢ | 26,062 | ×0.5^15 = 0.8 |
| | | **Σ** | **1.3** |

`yours 0.5 / Σ 1.3 = 38.6%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 38.6% = $0.96/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-miss-5pt5wins` ← this one
2. `aachc-cfb-wins-2026-11-28-miss-6pt5wins`
3. `aachc-cfb-wins-2026-11-28-miss-7pt5wins`
4. `aachc-cfb-wins-2026-11-28-miss-8pt5wins`
5. `aachc-cfb-wins-2026-11-28-miss-9pt5wins`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 8 | ×0.2^0 = 7.7 |
| ▶ | 5¢ | 294 (135 yours) | ×0.2^1 = 58.8 |
|  | 4¢ | 18 | ×0.2^2 = 0.7 |
|  | 2¢ | 13 | ×0.2^4 = 0.0 |
|  | 1¢ | 29,975 | ×0.2^5 = 9.6 |
| | | **Σ** | **76.8** |

`yours 27.0 / Σ 76.8 = 35.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 35.1% = $1.30/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 8 | ×0.2^0 = 7.7 |
| ▶ | 5¢ | 294 (135 yours) | ×0.2^1 = 58.8 |
|  | 4¢ | 18 | ×0.2^2 = 0.7 |
|  | 2¢ | 13 | ×0.2^4 = 0.0 |
|  | 1¢ | 29,975 | ×0.2^5 = 9.6 |
| | | **Σ** | **76.8** |

`yours 27.0 / Σ 76.8 = 35.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 35.1% = $1.30/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-txam-9pt5wins</code> SELL 0 @ 40¢ → $1.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 0 (0 yours) | ×0.5^0 = 0.5 |
|  | 47¢ | 45 | ×0.5^7 = 0.4 |
|  | 50¢ | 599 | ×0.5^10 = 0.6 |
|  | 94¢ | 40 | ×0.5^54 = 0.0 |
|  | 98¢ | 13 | ×0.5^58 = 0.0 |
|  | 99¢ | 5,002 | ×0.5^59 = 0.0 |
| | | **Σ** | **1.4** |

`yours 0.5 / Σ 1.4 = 34.8%`  
`$25 ÷ 4 ÷ 2 = $3.12 × 34.8% = $1.09/day`  

<details><summary>÷ 4 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-txam-6pt5wins`
2. `aachc-cfb-wins-2026-11-28-txam-7pt5wins`
3. `aachc-cfb-wins-2026-11-28-txam-8pt5wins`
4. `aachc-cfb-wins-2026-11-28-txam-9pt5wins` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 19,263 @ 1¢ → $2.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 126 | ×0.2^0 = 125.8 |
| ▶ | 1¢ | 39,813 (19,263 yours) | ×0.2^3 = 318.5 |
| | | **Σ** | **444.3** |

`yours 154.1 / Σ 444.3 = 34.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 34.7% = $2.48/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (918,144 resting) | ~12.3% | ~$9.22 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (82,085 resting) | ~12.2% | ~$9.18 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (25,560 resting) | ~8.7% | ~$6.53 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (92,230 resting) | ~10.0% | ~$2.50 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (631,074 resting) | ~8.7% | ~$2.18 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (39,639 resting) | ~6.7% | ~$1.68 |
| `ewc-usse-ne-2026-11-03-danosb` | $25.00 ÷ 3 | 0.10 | 2,000 | BUY side (84,329 resting) | ~38.9% | ~$1.62 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,240,482 resting) | ~25.6% | ~$1.60 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (71,126 resting) | ~24.3% | ~$1.52 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (82,913 resting) | ~5.4% | ~$1.34 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (75,368 resting) | ~20.8% | ~$1.30 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (6,281 resting) | ~4.2% | ~$1.05 |

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
| 2026-08-20 9:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 8:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 7:30 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 6:13 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 4:57 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 3:54 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 2:53 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 1:52 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:49 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-19 11:48 PM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
