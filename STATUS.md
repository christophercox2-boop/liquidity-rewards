# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 8:28 PM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$89.98/day estimated (ceiling, not promise — details below)

**Earned:** $5,595.00 lifetime ($5,593.52 paid). Last three recorded days — 2026-08-19: **$0.60** · 2026-08-18: **$181.52** · 2026-08-17: **$295.29** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$21.30/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$11.50/day), `ewc-usgub-ca-2026-11-03-xavbec` (~$8.60/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$89.98/day (~$3.75/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 91.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (63,344 resting ≥ 2,000 ✓) ≈ $6.25/day (event pool ÷ 2 markets) |
| `opdc-delrod-venpres-2027-06-30` | BUY | 14.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~97.5% of bid side (32,400 resting ≥ 2,000 ✓) ≈ $6.09/day (event pool ÷ 2 markets) |
| `opdc-delrod-venpres-2027-06-30` | SELL | 30.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~95.2% of ask side (10,108 resting ≥ 2,000 ✓) ≈ $5.95/day (event pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~93.7% of ask side (65,661 resting ≥ 2,000 ✓) ≈ $5.86/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~87.5% of bid side (52,704 resting ≥ 20,000 ✓) ≈ $3.24/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 9.0¢ | 20 | 2 | $200.00 | ✅ scoring — ~75.3% of bid side (95,723 resting ≥ 20,000 ✓) ≈ $4.43/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~72.1% of ask side (54,635 resting ≥ 20,000 ✓) ≈ $2.67/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 37 | 1 | $200.00 | ✅ scoring — ~70.3% of ask side (47,003 resting ≥ 20,000 ✓) ≈ $5.02/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-ok-2026-11-03-rep` | BUY | 90.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (600,450 resting ≥ 2,000 ✓) ≈ $4.17/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 7.0¢ | 100 | 2 | $200.00 | ✅ scoring — ~49.7% of bid side (93,590 resting ≥ 20,000 ✓) ≈ $1.84/day (event pool ÷ 27 markets) |
| `ussewc-usse-ar-2026-11-03-dem` | SELL | 12.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~47.0% of ask side (268,961 resting ≥ 2,000 ✓) ≈ $2.94/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~42.0% of bid side (87,484 resting ≥ 20,000 ✓) ≈ $1.56/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-thomas` | BUY | 1.0¢ | 19,311 | 3 | $200.00 | ✅ scoring — ~40.5% of bid side (42,304 resting ≥ 20,000 ✓) ≈ $2.89/day (event pool ÷ 14 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | SELL | 95.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~26.3% of ask side (4,560 resting ≥ 2,000 ✓) ≈ $1.64/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 9.0¢ | 50 | 1 | $200.00 | ✅ scoring — ~26.0% of bid side (103,318 resting ≥ 20,000 ✓) ≈ $0.96/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 19,263 | 3 | $200.00 | ✅ scoring — ~25.6% of bid side (44,362 resting ≥ 20,000 ✓) ≈ $1.83/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 19,336 | 3 | $200.00 | ✅ scoring — ~25.4% of bid side (44,366 resting ≥ 20,000 ✓) ≈ $1.82/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 6.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~24.0% of ask side (54,635 resting ≥ 20,000 ✓) ≈ $0.89/day (event pool ÷ 27 markets) |
| `ussewc-usse-ma-2026-11-03-rep` | SELL | 6.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~23.9% of ask side (65,635 resting ≥ 2,000 ✓) ≈ $1.50/day (event pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-jdvan` | BUY | 50.0¢ | 70 | 1 | $200.00 | ✅ scoring — ~22.2% of bid side (75,958 resting ≥ 20,000 ✓) ≈ $1.58/day (event pool ÷ 14 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | SELL | 2.0¢ | 85 | 0 | $25.00 | ✅ scoring — ~19.0% of ask side (308,861 resting ≥ 2,000 ✓) ≈ $1.19/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-markel` | BUY | 6.0¢ | 100 | 2 | $200.00 | ✅ scoring — ~16.0% of bid side (103,145 resting ≥ 20,000 ✓) ≈ $0.59/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,693 | 0 | $25.00 | ✅ scoring — ~14.1% of bid side (11,999 resting ≥ 2,000 ✓) ≈ $0.88/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 9.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~12.4% of bid side (93,590 resting ≥ 20,000 ✓) ≈ $0.46/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 90.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~11.0% of bid side (500,960 resting ≥ 2,000 ✓) ≈ $0.69/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-tuccar` | BUY | 4.0¢ | 200 | 1 | $200.00 | ✅ scoring — ~10.7% of bid side (78,331 resting ≥ 20,000 ✓) ≈ $0.40/day (event pool ÷ 27 markets) |
| `usgubewc-usgub-ok-2026-11-03-rep` | SELL | 94.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~10.4% of ask side (16,330 resting ≥ 2,000 ✓) ≈ $0.65/day (event pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 1.0¢ | 19,484 | 4 | $200.00 | ✅ scoring — ~9.7% of bid side (87,484 resting ≥ 20,000 ✓) ≈ $0.36/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 3.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~9.5% of ask side (47,003 resting ≥ 20,000 ✓) ≈ $0.68/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 5 | 1 | $200.00 | ✅ scoring — ~9.5% of ask side (47,003 resting ≥ 20,000 ✓) ≈ $0.68/day (event pool ÷ 14 markets) |
| …and 374 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 10 @ 91¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 97¢ | 5,194 | ×0.1^6 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.9% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>opdc-delrod-venpres-2027-06-30</code> BUY 0 @ 14¢ → $6.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 0 (0 yours) | ×0.1^0 = 0.0 |
|  | 8¢ | 250 | ×0.1^6 = 0.0 |
|  | 6¢ | 150 | ×0.1^8 = 0.0 |
|  | 4¢ | 30,000 | ×0.1^10 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 97.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 97.5% = $6.09/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `opdc-delrod-venpres-2026-12-31`
2. `opdc-delrod-venpres-2027-06-30` ← this one

</details>

</details>
<details><summary><code>opdc-delrod-venpres-2027-06-30</code> SELL 0 @ 30¢ → $5.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 0 (0 yours) | ×0.1^0 = 0.0 |
|  | 34¢ | 5 | ×0.1^4 = 0.0 |
|  | 38¢ | 675 | ×0.1^8 = 0.0 |
|  | 40¢ | 842 | ×0.1^10 = 0.0 |
|  | 41¢ | 781 | ×0.1^11 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 95.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 95.2% = $5.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `opdc-delrod-venpres-2026-12-31`
2. `opdc-delrod-venpres-2027-06-30` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 30 @ 2¢ → $5.86/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 32 (30 yours) | ×0.1^0 = 32.0 |
|  | 5¢ | 4 | ×0.1^3 = 0.0 |
|  | 9¢ | 150 | ×0.1^7 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^96 = 0.0 |
| | | **Σ** | **32.0** |

`yours 30.0 / Σ 32.0 = 93.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.7% = $5.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 144 (135 yours) | ×0.2^0 = 143.5 |
|  | 7¢ | 50 | ×0.2^1 = 10.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 52,397 | ×0.2^7 = 0.7 |
| | | **Σ** | **154.2** |

`yours 135.0 / Σ 154.2 = 87.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 87.5% = $3.24/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 20 @ 9¢ → $4.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 0 | ×0.2^0 = 0.2 |
| ▶ | 9¢ | 21 (20 yours) | ×0.2^2 = 0.8 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 64 | ×0.2^6 = 0.0 |
|  | 4¢ | 226 | ×0.2^7 = 0.0 |
|  | 3¢ | 110 | ×0.2^8 = 0.0 |
|  | 2¢ | 72,500 | ×0.2^9 = 0.0 |
| | | **Σ** | **1.1** |

`yours 0.8 / Σ 1.1 = 75.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 75.3% = $4.43/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 3 @ 6¢ → $2.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 4 (3 yours) | ×0.2^0 = 4.0 |
|  | 7¢ | 0 | ×0.2^1 = 0.1 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 1 | ×0.2^6 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 14¢ | 473 | ×0.2^8 = 0.0 |
|  | 15¢ | 26,415 | ×0.2^9 = 0.0 |
| | | **Σ** | **4.2** |

`yours 3.0 / Σ 4.2 = 72.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 72.1% = $2.67/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 37 @ 4¢ → $5.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 4¢ | 47 (37 yours) | ×0.2^1 = 9.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **10.5** |

`yours 7.4 / Σ 10.5 = 70.3%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 70.3% = $5.02/day`  

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
<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> BUY 0 @ 90¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 0 (0 yours) | ×0.1^0 = 0.0 |
|  | 86¢ | 50 | ×0.1^4 = 0.0 |
|  | 2¢ | 600,200 | ×0.1^88 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem`
2. `usgubewc-usgub-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 100 @ 7¢ → $1.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 4 | ×0.2^0 = 3.8 |
| ▶ | 7¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 2 | ×0.2^5 = 0.0 |
|  | 2¢ | 20,001 | ×0.2^7 = 0.3 |
| | | **Σ** | **8.1** |

`yours 4.0 / Σ 8.1 = 49.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 49.7% = $1.84/day`  

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
21. `ewc-usp-2028-11-07-rondes` ← this one
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-dem</code> SELL 1 @ 12¢ → $2.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 14¢ | 112 | ×0.1^2 = 1.1 |
|  | 17¢ | 55 | ×0.1^5 = 0.0 |
|  | 18¢ | 1,000 | ×0.1^6 = 0.0 |
|  | 36¢ | 0 | ×0.1^24 = 0.0 |
|  | 40¢ | 2,000 | ×0.1^28 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 47.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 47.0% = $2.94/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem` ← this one
2. `ussewc-usse-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $1.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 178 (135 yours) | ×0.2^0 = 177.9 |
|  | 4¢ | 18 | ×0.2^1 = 3.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
|  | 1¢ | 87,275 | ×0.2^4 = 139.6 |
| | | **Σ** | **321.3** |

`yours 135.0 / Σ 321.3 = 42.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 42.0% = $1.56/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-thomas</code> BUY 19,311 @ 1¢ → $2.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 2 | ×0.2^0 = 2.0 |
|  | 3¢ | 213 | ×0.2^1 = 42.6 |
| ▶ | 1¢ | 42,089 (19,311 yours) | ×0.2^3 = 336.7 |
| | | **Σ** | **381.3** |

`yours 154.5 / Σ 381.3 = 40.5%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 40.5% = $2.89/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> SELL 10 @ 95¢ → $1.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 28 (10 yours) | ×0.1^0 = 28.0 |
|  | 96¢ | 53 | ×0.1^1 = 5.3 |
|  | 97¢ | 438 | ×0.1^2 = 4.4 |
|  | 99¢ | 4,041 | ×0.1^4 = 0.4 |
| | | **Σ** | **38.1** |

`yours 10.0 / Σ 38.1 = 26.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.3% = $1.64/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 50 @ 9¢ → $0.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 28 | ×0.2^0 = 28.3 |
| ▶ | 9¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 5 | ×0.2^5 = 0.0 |
|  | 2¢ | 111 | ×0.2^8 = 0.0 |
|  | 1¢ | 103,122 | ×0.2^9 = 0.1 |
| | | **Σ** | **38.4** |

`yours 10.0 / Σ 38.4 = 26.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 26.0% = $0.96/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 19,263 @ 1¢ → $1.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 249 | ×0.2^0 = 249.0 |
| ▶ | 1¢ | 44,113 (19,263 yours) | ×0.2^3 = 352.9 |
| | | **Σ** | **601.9** |

`yours 154.1 / Σ 601.9 = 25.6%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 25.6% = $1.83/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 19,336 @ 1¢ → $1.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 255 | ×0.2^0 = 255.0 |
| ▶ | 1¢ | 44,111 (19,336 yours) | ×0.2^3 = 352.9 |
| | | **Σ** | **607.9** |

`yours 154.7 / Σ 607.9 = 25.4%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 25.4% = $1.82/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 1 @ 6¢ → $0.89/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 4 (1 yours) | ×0.2^0 = 4.0 |
|  | 7¢ | 0 | ×0.2^1 = 0.1 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 1 | ×0.2^6 = 0.0 |
|  | 13¢ | 1 | ×0.2^7 = 0.0 |
|  | 14¢ | 473 | ×0.2^8 = 0.0 |
|  | 15¢ | 26,415 | ×0.2^9 = 0.0 |
| | | **Σ** | **4.2** |

`yours 1.0 / Σ 4.2 = 24.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 24.0% = $0.89/day`  

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
<details><summary><code>ussewc-usse-ma-2026-11-03-rep</code> SELL 0 @ 6¢ → $1.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 0 (0 yours) | ×0.1^0 = 0.1 |
|  | 9¢ | 159 | ×0.1^3 = 0.2 |
|  | 32¢ | 1 | ×0.1^26 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.1 / Σ 0.2 = 23.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 23.9% = $1.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem`
2. `ussewc-usse-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-jdvan</code> BUY 70 @ 50¢ → $1.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 51¢ | 12 | ×0.2^0 = 12.4 |
| ▶ | 50¢ | 249 (70 yours) | ×0.2^1 = 49.8 |
|  | 48¢ | 120 | ×0.2^3 = 1.0 |
|  | 43¢ | 581 | ×0.2^8 = 0.0 |
|  | 32¢ | 108 | ×0.2^19 = 0.0 |
|  | 31¢ | 50 | ×0.2^20 = 0.0 |
|  | 5¢ | 100 | ×0.2^46 = 0.0 |
|  | 3¢ | 2,238 | ×0.2^48 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^49 = 0.0 |
| | | **Σ** | **63.1** |

`yours 14.0 / Σ 63.1 = 22.2%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 22.2% = $1.58/day`  

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
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> SELL 85 @ 2¢ → $1.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 448 (85 yours) | ×0.1^0 = 448.0 |
|  | 6¢ | 150 | ×0.1^4 = 0.0 |
|  | 49¢ | 5,000 | ×0.1^47 = 0.0 |
| | | **Σ** | **448.0** |

`yours 85.0 / Σ 448.0 = 19.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 19.0% = $1.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-markel</code> BUY 100 @ 6¢ → $0.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 17 | ×0.2^0 = 17.0 |
| ▶ | 6¢ | 170 (100 yours) | ×0.2^2 = 6.8 |
|  | 3¢ | 14 | ×0.2^5 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^6 = 1.3 |
| | | **Σ** | **25.1** |

`yours 4.0 / Σ 25.1 = 16.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 16.0% = $0.59/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> BUY 1,693 @ 1¢ → $0.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,999 (1,693 yours) | ×0.1^0 = 11,999.0 |
| | | **Σ** | **11,999.0** |

`yours 1,693.0 / Σ 11,999.0 = 14.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 14.1% = $0.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 1 @ 9¢ → $0.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 4 (1 yours) | ×0.2^0 = 3.8 |
|  | 7¢ | 100 | ×0.2^2 = 4.0 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 2 | ×0.2^5 = 0.0 |
|  | 2¢ | 20,001 | ×0.2^7 = 0.3 |
| | | **Σ** | **8.1** |

`yours 1.0 / Σ 8.1 = 12.4%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 12.4% = $0.46/day`  

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
21. `ewc-usp-2028-11-07-rondes` ← this one
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 1 @ 90¢ → $0.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 88¢ | 708 | ×0.1^2 = 7.1 |
|  | 75¢ | 50 | ×0.1^15 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^88 = 0.0 |
| | | **Σ** | **9.1** |

`yours 1.0 / Σ 9.1 = 11.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 11.0% = $0.69/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tuccar</code> BUY 200 @ 4¢ → $0.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 6 | ×0.2^0 = 6.0 |
| ▶ | 4¢ | 201 (200 yours) | ×0.2^1 = 40.2 |
|  | 2¢ | 41,095 | ×0.2^3 = 328.8 |
| | | **Σ** | **375.0** |

`yours 40.0 / Σ 375.0 = 10.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 10.7% = $0.40/day`  

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
<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> SELL 0 @ 94¢ → $0.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 0 (0 yours) | ×0.1^0 = 0.0 |
|  | 98¢ | 105 | ×0.1^4 = 0.0 |
|  | 99¢ | 16,225 | ×0.1^5 = 0.2 |
| | | **Σ** | **0.2** |

`yours 0.0 / Σ 0.2 = 10.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 10.4% = $0.65/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem`
2. `usgubewc-usgub-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 19,484 @ 1¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 178 | ×0.2^0 = 177.9 |
|  | 4¢ | 18 | ×0.2^1 = 3.6 |
|  | 2¢ | 13 | ×0.2^3 = 0.1 |
| ▶ | 1¢ | 87,275 (19,484 yours) | ×0.2^4 = 139.6 |
| | | **Σ** | **321.3** |

`yours 31.2 / Σ 321.3 = 9.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 9.7% = $0.36/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 1 @ 3¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 4¢ | 47 | ×0.2^1 = 9.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **10.5** |

`yours 1.0 / Σ 10.5 = 9.5%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 9.5% = $0.68/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 5 @ 4¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 4¢ | 47 (5 yours) | ×0.2^1 = 9.4 |
|  | 5¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 12¢ | 3 | ×0.2^9 = 0.0 |
|  | 13¢ | 5 | ×0.2^10 = 0.0 |
|  | 14¢ | 5 | ×0.2^11 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^12 = 0.0 |
| | | **Σ** | **10.5** |

`yours 1.0 / Σ 10.5 = 9.5%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 9.5% = $0.68/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-19 | ~$57.34 | $0.60 | 1% |

Biggest gaps on 2026-08-19: `ussewc-usse-il-2026-11-03-dem` (est ~$5.65 → got $0.00), `ussewc-usse-ok-2026-11-03-rep` (est ~$5.42 → got $0.00), `usgubewc-usgub-ma-2026-11-03-dem` (est ~$5.35 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (71,391 resting) | ~28.4% | ~$21.30 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (152,001 resting) | ~15.3% | ~$11.50 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (26,750 resting) | ~11.5% | ~$8.60 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,564 resting) | ~18.4% | ~$4.59 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (922,752 resting) | ~4.6% | ~$3.48 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (81,266 resting) | ~4.3% | ~$3.19 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (391,482 resting) | ~4.0% | ~$2.97 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (638,622 resting) | ~10.1% | ~$2.54 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (69,003 resting) | ~9.3% | ~$2.33 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (692,150 resting) | ~2.3% | ~$1.76 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (150,032 resting) | ~2.1% | ~$1.59 |
| `cranc-uspres28-12-31-2026-dwajoh` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (47,975 resting) | ~100.0% | ~$1.51 |

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
| 2026-08-20 8:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 7:28 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 6:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 5:27 PM ET | ✅ ok | 3188 | $5595.00 |
| 2026-08-20 4:10 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:42 PM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 11:41 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 10:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 9:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 8:31 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
