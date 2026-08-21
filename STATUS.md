# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 11:44 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$61.44/day estimated (ceiling, not promise — details below)

**Earned:** $5,595.00 lifetime ($5,593.52 paid). Last three recorded days — 2026-08-19: **$0.60** · 2026-08-18: **$181.52** · 2026-08-17: **$295.29** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$49.81/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$11.70/day), `ewc-usse-ga-2026-11-03-rep` (~$8.39/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$61.44/day (~$2.56/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 37 | 1 | $200.00 | ✅ scoring — ~64.2% of ask side (47,008 resting ≥ 20,000 ✓) ≈ $4.59/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 16.0¢ | 16 | 0 | $25.00 | ✅ scoring — ~47.4% of bid side (37,179 resting ≥ 2,000 ✓) ≈ $2.96/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-rep` | SELL | 3.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~46.3% of ask side (201,353 resting ≥ 2,000 ✓) ≈ $2.89/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 3 | $200.00 | ✅ scoring — ~44.2% of bid side (52,749 resting ≥ 20,000 ✓) ≈ $1.64/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~39.6% of bid side (87,584 resting ≥ 20,000 ✓) ≈ $1.47/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | SELL | 93.0¢ | 9 | 2 | $25.00 | ✅ scoring — ~34.6% of ask side (3,536 resting ≥ 2,000 ✓) ≈ $2.16/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 11.0¢ | 20 | 0 | $200.00 | ✅ scoring — ~34.4% of bid side (43,298 resting ≥ 20,000 ✓) ≈ $2.02/day (event pool ÷ 17 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | SELL | 95.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~27.8% of ask side (3,961 resting ≥ 2,000 ✓) ≈ $1.74/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 19,263 | 3 | $200.00 | ✅ scoring — ~26.3% of bid side (42,362 resting ≥ 20,000 ✓) ≈ $1.88/day (event pool ÷ 14 markets) |
| `ussewc-usse-id-2026-11-03-rep` | BUY | 95.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~25.0% of bid side (504,250 resting ≥ 2,000 ✓) ≈ $1.56/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-markel` | BUY | 13.0¢ | 10 | 0 | $200.00 | ✅ scoring — ~23.9% of bid side (99,878 resting ≥ 20,000 ✓) ≈ $1.41/day (event pool ÷ 17 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~23.8% of ask side (67,455 resting ≥ 2,000 ✓) ≈ $1.49/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-jdvan` | BUY | 50.0¢ | 70 | 2 | $200.00 | ✅ scoring — ~20.7% of bid side (75,398 resting ≥ 20,000 ✓) ≈ $1.48/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 86.0¢ | 0 | 2 | $25.00 | ✅ scoring — ~18.5% of bid side (502,153 resting ≥ 2,000 ✓) ≈ $1.16/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~16.5% of ask side (54,649 resting ≥ 20,000 ✓) ≈ $0.61/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 9.0¢ | 50 | 1 | $200.00 | ✅ scoring — ~14.7% of bid side (82,644 resting ≥ 20,000 ✓) ≈ $0.54/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 5.0¢ | 10 | 0 | $200.00 | ✅ scoring — ~13.3% of ask side (60,691 resting ≥ 20,000 ✓) ≈ $0.78/day (event pool ÷ 17 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | SELL | 2.0¢ | 85 | 0 | $25.00 | ✅ scoring — ~13.0% of ask side (310,768 resting ≥ 2,000 ✓) ≈ $0.81/day (event pool ÷ 2 markets) |
| `ewc-usgub-ca-2026-11-03-xavbec` | SELL | 95.0¢ | 200 | 0 | $300.00 | ✅ scoring — ~12.3% of ask side (26,829 resting ≥ 10,000 ✓) ≈ $9.25/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-thomas` | BUY | 1.0¢ | 19,311 | 3 | $200.00 | ✅ scoring — ~12.3% of bid side (152,276 resting ≥ 20,000 ✓) ≈ $0.88/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 19,336 | 3 | $200.00 | ✅ scoring — ~10.2% of bid side (152,542 resting ≥ 20,000 ✓) ≈ $0.73/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-tuccar` | BUY | 4.0¢ | 200 | 5 | $200.00 | ✅ scoring — ~10.0% of bid side (59,016 resting ≥ 20,000 ✓) ≈ $0.37/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 1.0¢ | 19,484 | 4 | $200.00 | ✅ scoring — ~9.1% of bid side (87,584 resting ≥ 20,000 ✓) ≈ $0.34/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-al-2026-11-03-dem` | BUY | 12.0¢ | 0 | 1 | $25.00 | ✅ scoring — ~9.1% of bid side (42,111 resting ≥ 2,000 ✓) ≈ $0.57/day (event pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-kenblo` | SELL | 5.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~9.1% of ask side (3,583 resting ≥ 2,000 ✓) ≈ $0.38/day (event pool ÷ 3 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 3.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~8.7% of ask side (47,008 resting ≥ 20,000 ✓) ≈ $0.62/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 5 | 1 | $200.00 | ✅ scoring — ~8.7% of ask side (47,008 resting ≥ 20,000 ✓) ≈ $0.62/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 5 | 1 | $200.00 | ✅ scoring — ~8.7% of ask side (47,008 resting ≥ 20,000 ✓) ≈ $0.62/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 4.0¢ | 50 | 0 | $200.00 | ✅ scoring — ~8.5% of bid side (42,362 resting ≥ 20,000 ✓) ≈ $0.61/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | BUY | 94.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~8.5% of bid side (302,613 resting ≥ 2,000 ✓) ≈ $0.53/day (event pool ÷ 2 markets) |
| …and 377 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 37 @ 4¢ → $4.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 4¢ | 52 (37 yours) | ×0.2^1 = 10.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **11.5** |

`yours 7.4 / Σ 11.5 = 64.2%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 64.2% = $4.59/day`  

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 16 @ 16¢ → $2.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 34 (16 yours) | ×0.1^0 = 34.2 |
|  | 10¢ | 10 | ×0.1^6 = 0.0 |
|  | 9¢ | 10 | ×0.1^7 = 0.0 |
|  | 6¢ | 125 | ×0.1^10 = 0.0 |
|  | 2¢ | 15,000 | ×0.1^14 = 0.0 |
| | | **Σ** | **34.2** |

`yours 16.2 / Σ 34.2 = 47.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 47.4% = $2.96/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-rep</code> SELL 1 @ 3¢ → $2.89/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 5¢ | 16 | ×0.1^2 = 0.2 |
|  | 6¢ | 1 | ×0.1^3 = 0.0 |
|  | 9¢ | 1 | ×0.1^6 = 0.0 |
|  | 10¢ | 50 | ×0.1^7 = 0.0 |
|  | 12¢ | 83 | ×0.1^9 = 0.0 |
|  | 98¢ | 199,175 | ×0.1^95 = 0.0 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 46.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 46.3% = $2.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem`
2. `usgubewc-usgub-ct-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $1.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 1.0 |
|  | 10¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 8¢ | 137 (135 yours) | ×0.2^3 = 1.1 |
|  | 7¢ | 100 | ×0.2^4 = 0.2 |
|  | 6¢ | 1 | ×0.2^5 = 0.0 |
|  | 2¢ | 112 | ×0.2^9 = 0.0 |
|  | 1¢ | 52,397 | ×0.2^10 = 0.0 |
| | | **Σ** | **2.4** |

`yours 1.1 / Σ 2.4 = 44.2%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 44.2% = $1.64/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 178 (135 yours) | ×0.2^0 = 177.8 |
|  | 4¢ | 118 | ×0.2^1 = 23.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
|  | 1¢ | 87,275 | ×0.2^4 = 139.6 |
| | | **Σ** | **341.2** |

`yours 135.0 / Σ 341.2 = 39.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 39.6% = $1.47/day`  

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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> SELL 9 @ 93¢ → $2.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 91¢ | 0 | ×0.1^0 = 0.0 |
| ▶ | 93¢ | 24 (9 yours) | ×0.1^2 = 0.2 |
|  | 99¢ | 3,512 | ×0.1^8 = 0.0 |
| | | **Σ** | **0.3** |

`yours 0.1 / Σ 0.3 = 34.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 34.6% = $2.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 20 @ 11¢ → $2.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 53 (20 yours) | ×0.2^0 = 53.3 |
|  | 10¢ | 20 | ×0.2^1 = 4.0 |
|  | 9¢ | 21 | ×0.2^2 = 0.8 |
|  | 8¢ | 2 | ×0.2^3 = 0.0 |
|  | 5¢ | 64 | ×0.2^6 = 0.0 |
|  | 4¢ | 226 | ×0.2^7 = 0.0 |
|  | 3¢ | 110 | ×0.2^8 = 0.0 |
|  | 1¢ | 42,801 | ×0.2^10 = 0.0 |
| | | **Σ** | **58.2** |

`yours 20.0 / Σ 58.2 = 34.4%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 34.4% = $2.02/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> SELL 10 @ 95¢ → $1.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 26 (10 yours) | ×0.1^0 = 26.0 |
|  | 96¢ | 52 | ×0.1^1 = 5.2 |
|  | 97¢ | 438 | ×0.1^2 = 4.4 |
|  | 99¢ | 3,445 | ×0.1^4 = 0.3 |
| | | **Σ** | **35.9** |

`yours 10.0 / Σ 35.9 = 27.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.8% = $1.74/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 19,263 @ 1¢ → $1.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 249 | ×0.2^0 = 249.0 |
| ▶ | 1¢ | 42,113 (19,263 yours) | ×0.2^3 = 336.9 |
| | | **Σ** | **585.9** |

`yours 154.1 / Σ 585.9 = 26.3%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 26.3% = $1.88/day`  

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
<details><summary><code>ussewc-usse-id-2026-11-03-rep</code> BUY 0 @ 95¢ → $1.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 0 (0 yours) | ×0.1^0 = 0.1 |
|  | 82¢ | 50 | ×0.1^13 = 0.0 |
|  | 50¢ | 2,200 | ×0.1^45 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 25.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 25.0% = $1.56/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-id-2026-11-03-rep` ← this one
2. `ussewc-usse-id-2026-11-03-todach`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> BUY 10 @ 13¢ → $1.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 38 (10 yours) | ×0.2^0 = 38.1 |
|  | 11¢ | 50 | ×0.2^2 = 2.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 9¢ | 986 | ×0.2^4 = 1.6 |
|  | 8¢ | 193 | ×0.2^5 = 0.1 |
|  | 7¢ | 110 | ×0.2^6 = 0.0 |
|  | 2¢ | 26,000 | ×0.2^11 = 0.0 |
| | | **Σ** | **41.8** |

`yours 10.0 / Σ 41.8 = 23.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 23.9% = $1.41/day`  

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 30 @ 2¢ → $1.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 126 (30 yours) | ×0.1^0 = 126.0 |
|  | 5¢ | 4 | ×0.1^3 = 0.0 |
|  | 9¢ | 50 | ×0.1^7 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^96 = 0.0 |
| | | **Σ** | **126.0** |

`yours 30.0 / Σ 126.0 = 23.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 23.8% = $1.49/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-jdvan</code> BUY 70 @ 50¢ → $1.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 52¢ | 0 | ×0.2^0 = 0.0 |
|  | 51¢ | 13 | ×0.2^1 = 2.5 |
| ▶ | 50¢ | 269 (70 yours) | ×0.2^2 = 10.8 |
|  | 48¢ | 120 | ×0.2^4 = 0.2 |
|  | 32¢ | 108 | ×0.2^20 = 0.0 |
|  | 31¢ | 50 | ×0.2^21 = 0.0 |
|  | 5¢ | 100 | ×0.2^47 = 0.0 |
|  | 3¢ | 2,238 | ×0.2^49 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^50 = 0.0 |
| | | **Σ** | **13.5** |

`yours 2.8 / Σ 13.5 = 20.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 20.7% = $1.48/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan` ← this one
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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 0 @ 86¢ → $1.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 88¢ | 0 | ×0.1^0 = 0.0 |
|  | 87¢ | 0 | ×0.1^1 = 0.0 |
| ▶ | 86¢ | 0 (0 yours) | ×0.1^2 = 0.0 |
|  | 85¢ | 0 | ×0.1^3 = 0.0 |
|  | 84¢ | 0 | ×0.1^4 = 0.0 |
|  | 75¢ | 152 | ×0.1^13 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^86 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 18.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 18.5% = $1.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 3 @ 6¢ → $0.61/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 18 (3 yours) | ×0.2^0 = 18.0 |
|  | 7¢ | 0 | ×0.2^1 = 0.1 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 1 | ×0.2^6 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 14¢ | 473 | ×0.2^8 = 0.0 |
|  | 15¢ | 26,415 | ×0.2^9 = 0.0 |
| | | **Σ** | **18.2** |

`yours 3.0 / Σ 18.2 = 16.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 16.5% = $0.61/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 50 @ 9¢ → $0.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 54 | ×0.2^0 = 54.0 |
| ▶ | 9¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 8¢ | 101 | ×0.2^2 = 4.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 5 | ×0.2^5 = 0.0 |
|  | 2¢ | 111 | ×0.2^8 = 0.0 |
|  | 1¢ | 82,322 | ×0.2^9 = 0.0 |
| | | **Σ** | **68.1** |

`yours 10.0 / Σ 68.1 = 14.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 14.7% = $0.54/day`  

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
19. `ewc-usp-2028-11-07-rahema` ← this one
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
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 10 @ 5¢ → $0.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 75 (10 yours) | ×0.2^0 = 75.0 |
|  | 6¢ | 1 | ×0.2^1 = 0.2 |
|  | 13¢ | 9 | ×0.2^8 = 0.0 |
|  | 19¢ | 3 | ×0.2^14 = 0.0 |
|  | 20¢ | 40,501 | ×0.2^15 = 0.0 |
| | | **Σ** | **75.2** |

`yours 10.0 / Σ 75.2 = 13.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 13.3% = $0.78/day`  

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
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> SELL 85 @ 2¢ → $0.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 655 (85 yours) | ×0.1^0 = 655.0 |
|  | 6¢ | 50 | ×0.1^4 = 0.0 |
|  | 49¢ | 5,000 | ×0.1^47 = 0.0 |
| | | **Σ** | **655.0** |

`yours 85.0 / Σ 655.0 = 13.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 13.0% = $0.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usgub-ca-2026-11-03-xavbec</code> SELL 200 @ 95¢ → $9.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 1,458 (200 yours) | ×0.2^0 = 1,457.8 |
|  | 97¢ | 40 | ×0.2^2 = 1.6 |
|  | 98¢ | 20,332 | ×0.2^3 = 162.7 |
| | | **Σ** | **1,622.1** |

`yours 200.0 / Σ 1,622.1 = 12.3%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 12.3% = $9.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usgub-ca-2026-11-03-stehil`
2. `ewc-usgub-ca-2026-11-03-xavbec` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-thomas</code> BUY 19,311 @ 1¢ → $0.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 2 | ×0.2^0 = 2.0 |
|  | 3¢ | 213 | ×0.2^1 = 42.6 |
| ▶ | 1¢ | 152,061 (19,311 yours) | ×0.2^3 = 1,216.5 |
| | | **Σ** | **1,261.1** |

`yours 154.5 / Σ 1,261.1 = 12.3%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 12.3% = $0.88/day`  

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
11. `enwc-uspres-nom-rep-2028-thomas` ← this one
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 19,336 @ 1¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 255 | ×0.2^0 = 255.0 |
|  | 3¢ | 200 | ×0.2^1 = 40.0 |
| ▶ | 1¢ | 152,087 (19,336 yours) | ×0.2^3 = 1,216.7 |
| | | **Σ** | **1,511.7** |

`yours 154.7 / Σ 1,511.7 = 10.2%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 10.2% = $0.73/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tuccar</code> BUY 200 @ 4¢ → $0.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
|  | 5¢ | 6 | ×0.2^4 = 0.0 |
| ▶ | 4¢ | 201 (200 yours) | ×0.2^5 = 0.1 |
|  | 2¢ | 42,580 | ×0.2^7 = 0.5 |
| | | **Σ** | **0.6** |

`yours 0.1 / Σ 0.6 = 10.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 10.0% = $0.37/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 19,484 @ 1¢ → $0.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 178 | ×0.2^0 = 177.8 |
|  | 4¢ | 118 | ×0.2^1 = 23.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
| ▶ | 1¢ | 87,275 (19,484 yours) | ×0.2^4 = 139.6 |
| | | **Σ** | **341.2** |

`yours 31.2 / Σ 341.2 = 9.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 9.1% = $0.34/day`  

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
<details><summary><code>usgubewc-usgub-al-2026-11-03-dem</code> BUY 0 @ 12¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 0 | ×0.1^0 = 0.1 |
| ▶ | 12¢ | 0 (0 yours) | ×0.1^1 = 0.0 |
|  | 1¢ | 42,111 | ×0.1^12 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 9.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 9.1% = $0.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem` ← this one
2. `usgubewc-usgub-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-kenblo</code> SELL 1 @ 5¢ → $0.38/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 11 (1 yours) | ×0.1^0 = 11.0 |
|  | 8¢ | 2 | ×0.1^3 = 0.0 |
|  | 10¢ | 1 | ×0.1^5 = 0.0 |
|  | 12¢ | 7 | ×0.1^7 = 0.0 |
|  | 15¢ | 50 | ×0.1^10 = 0.0 |
|  | 99¢ | 3,512 | ×0.1^94 = 0.0 |
| | | **Σ** | **11.0** |

`yours 1.0 / Σ 11.0 = 9.1%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 9.1% = $0.38/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo` ← this one
3. `usgubewc-usgub-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 1 @ 3¢ → $0.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 4¢ | 52 | ×0.2^1 = 10.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **11.5** |

`yours 1.0 / Σ 11.5 = 8.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 8.7% = $0.62/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 5 @ 4¢ → $0.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 4¢ | 52 (5 yours) | ×0.2^1 = 10.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **11.5** |

`yours 1.0 / Σ 11.5 = 8.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 8.7% = $0.62/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 5 @ 4¢ → $0.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 4¢ | 52 (5 yours) | ×0.2^1 = 10.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **11.5** |

`yours 1.0 / Σ 11.5 = 8.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 8.7% = $0.62/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 50 @ 4¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 249 (50 yours) | ×0.2^0 = 249.0 |
|  | 1¢ | 42,113 | ×0.2^3 = 336.9 |
| | | **Σ** | **585.9** |

`yours 50.0 / Σ 585.9 = 8.5%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 8.5% = $0.61/day`  

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
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> BUY 1 @ 94¢ → $0.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 12 (1 yours) | ×0.1^0 = 12.0 |
|  | 90¢ | 1 | ×0.1^4 = 0.0 |
|  | 86¢ | 25 | ×0.1^8 = 0.0 |
|  | 85¢ | 25 | ×0.1^9 = 0.0 |
|  | 84¢ | 50 | ×0.1^10 = 0.0 |
|  | 54¢ | 500 | ×0.1^40 = 0.0 |
|  | 2¢ | 300,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **12.0** |

`yours 1.0 / Σ 12.0 = 8.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 8.5% = $0.53/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-19 | ~$5.79 | $0.60 | 10% |

Biggest gaps on 2026-08-19: `ussewc-usse-de-2026-11-03-dem` (est ~$1.21 → got $0.00), `usgubewc-usgub-tn-2026-11-03-rep` (est ~$0.97 → got $0.00), `usgubewc-usgub-id-2026-11-03-rep` (est ~$0.73 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (70,871 resting) | ~66.4% | ~$49.81 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (151,941 resting) | ~15.6% | ~$11.70 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (71,685 resting) | ~11.2% | ~$8.39 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (920,650 resting) | ~5.7% | ~$4.31 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (391,549 resting) | ~3.9% | ~$2.92 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,475 resting) | ~10.4% | ~$2.60 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (68,944 resting) | ~9.3% | ~$2.32 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (637,755 resting) | ~7.9% | ~$1.97 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (692,138 resting) | ~2.4% | ~$1.76 |
| `ewc-usse-ak-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (375,146 resting) | ~21.9% | ~$1.37 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (84,518 resting) | ~18.0% | ~$1.12 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (155,662 resting) | ~1.3% | ~$1.00 |

## Totals

| | Amount |
|---|---:|
| Paid | $5,593.52 |
| Skipped | $1.48 |
| **Total earned** | **$5,595.00** |

3188 reward rows · 48 days with rewards · 586 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-19 | $0.60 | `█` |
| 2026-08-18 | $181.52 | `███` |
| 2026-08-17 | $295.29 | `████` |
| 2026-08-16 | $197.03 | `███` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $4,131.68 | `████████████████████` |
| 2026-07 | $1,463.32 | `███████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $190.39 |
| `apdc-alito-2026-12-31` | $120.07 |
| `ewc-usp-party-2028-11-07-rep` | $110.48 |
| `ewc-usp-party-2028-11-07-dem` | $102.28 |
| `opdc-mcconnell-resign-2026-11-02` | $79.42 |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | $66.06 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $63.61 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $62.40 |
| `enwc-uspres-nom-rep-2028-rondes` | $49.72 |
| `enwc-uspres-nom-dem-2028-stasmi` | $47.79 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.60 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.51 |
| `enwc-uspres-nom-dem-2028-jamtal` | $40.91 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-20 11:44 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 10:29 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 9:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 8:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 7:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 6:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 5:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 4:10 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:42 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 11:41 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
