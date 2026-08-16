# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-15 11:04 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$513.47/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usse-oh-2026-11-03-dem` — BUY at the best price, ~$22.31/day for 200 contracts. Runners-up: `ewc-usgub-wi-2026-11-03-dem` (~$5.03/day), `ewc-usgub-nv-2026-11-03-rep` (~$4.36/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$513.47/day (~$21.39/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (92,067 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 90.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (20,304 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-rep` | SELL | 90.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,476 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 20.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,773 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,509 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-pa-2026-11-03-rep` | BUY | 11.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 18.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.8% of ask side (91,760 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 19.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~99.8% of bid side (20,707 resting ≥ 20,000 ✓) ≈ $8.32/day (program pool ÷ 60 markets) |
| `enwc-uspres-nom-dem-2028-aleocc` | BUY | 26.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~99.8% of bid side (31,628 resting ≥ 20,000 ✓) ≈ $8.31/day (program pool ÷ 60 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | BUY | 4.0¢ | 200 | 0 | $25.00 | ✅ scoring — ~98.9% of bid side (2,400 resting ≥ 2,000 ✓) ≈ $6.18/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-dem` | SELL | 92.0¢ | 23 | 0 | $25.00 | ✅ scoring — ~98.3% of ask side (5,159 resting ≥ 2,000 ✓) ≈ $6.15/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 13.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~97.1% of bid side (300,406 resting ≥ 5,000 ✓) ≈ $3.74/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-kamhar` | BUY | 29.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~96.1% of bid side (30,198 resting ≥ 20,000 ✓) ≈ $8.01/day (program pool ÷ 60 markets) |
| `enwc-uspres-nom-dem-2028-stasmi` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~93.7% of bid side (20,519 resting ≥ 20,000 ✓) ≈ $7.81/day (program pool ÷ 60 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~93.0% of ask side (130,768 resting ≥ 2,000 ✓) ≈ $5.81/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-rep` | SELL | 9.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~91.7% of ask side (195,998 resting ≥ 2,000 ✓) ≈ $5.73/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 41.0¢ | 5 | 2 | $100.00 | ✅ scoring — ~90.9% of ask side (82,277 resting ≥ 5,000 ✓) ≈ $3.79/day (pool ÷ 12 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 7.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,753 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-rep` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,781 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | SELL | 10.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~89.1% of ask side (265,913 resting ≥ 2,000 ✓) ≈ $5.57/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 10.0¢ | 24 | 1 | $1,000.00 | ✅ scoring — ~88.7% of bid side (20,481 resting ≥ 20,000 ✓) ≈ $7.39/day (program pool ÷ 60 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~87.7% of ask side (2,026 resting ≥ 2,000 ✓) ≈ $5.48/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | SELL | 22.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~87.3% of ask side (65,501 resting ≥ 20,000 ✓) ≈ $7.27/day (program pool ÷ 60 markets) |
| `ewc-usp-2028-11-07-rokha` | BUY | 16.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~86.9% of bid side (40,461 resting ≥ 20,000 ✓) ≈ $7.24/day (program pool ÷ 60 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 9.0¢ | 75 | 0 | $25.00 | ✅ scoring — ~85.2% of ask side (208,376 resting ≥ 2,000 ✓) ≈ $5.33/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 10.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (65,499 resting ≥ 2,000 ✓) ≈ $5.21/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~83.1% of ask side (7,218 resting ≥ 2,000 ✓) ≈ $5.19/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 10.0¢ | 60 | 1 | $1,000.00 | ✅ scoring — ~82.9% of bid side (20,515 resting ≥ 20,000 ✓) ≈ $6.91/day (program pool ÷ 60 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 18.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~82.6% of bid side (20,513 resting ≥ 20,000 ✓) ≈ $6.89/day (program pool ÷ 60 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 10.0¢ | 60 | 1 | $1,000.00 | ✅ scoring — ~80.6% of bid side (20,518 resting ≥ 20,000 ✓) ≈ $6.71/day (program pool ÷ 60 markets) |
| …and 2625 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 8¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 80,716 | ×0.2^89 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> SELL 50 @ 90¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 98¢ | 50 | ×0.1^8 = 0.0 |
|  | 99¢ | 20,204 | ×0.1^9 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-rep</code> SELL 15 @ 90¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 15 (15 yours) | ×0.1^0 = 15.0 |
|  | 98¢ | 1,319 | ×0.1^8 = 0.0 |
|  | 99¢ | 1,142 | ×0.1^9 = 0.0 |
| | | **Σ** | **15.0** |

`yours 15.0 / Σ 15.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem`
2. `ussewc-usse-ms-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 5 @ 20¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 28¢ | 5 | ×0.2^8 = 0.0 |
|  | 50¢ | 90 | ×0.2^30 = 0.0 |
|  | 97¢ | 80,472 | ×0.2^77 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 30 @ 2¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 30 (30 yours) | ×0.1^0 = 30.0 |
|  | 5¢ | 4 | ×0.1^3 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^96 = 0.0 |
| | | **Σ** | **30.0** |

`yours 30.0 / Σ 30.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-pa-2026-11-03-rep</code> BUY 1 @ 11¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 6¢ | 50 | ×0.1^5 = 0.0 |
|  | 1¢ | 1,949 | ×0.1^10 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem`
2. `usgubewc-usgub-pa-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 1 @ 18¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 24¢ | 25 | ×0.2^6 = 0.0 |
|  | 50¢ | 74 | ×0.2^32 = 0.0 |
|  | 97¢ | 80,459 | ×0.2^79 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 1 @ 19¢ → $8.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 15¢ | 1 | ×0.2^4 = 0.0 |
|  | 14¢ | 1 | ×0.2^5 = 0.0 |
|  | 13¢ | 1 | ×0.2^6 = 0.0 |
|  | 8¢ | 1 | ×0.2^11 = 0.0 |
|  | 4¢ | 1 | ×0.2^15 = 0.0 |
|  | 3¢ | 500 | ×0.2^16 = 0.0 |
|  | 1¢ | 20,201 | ×0.2^18 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 99.8% = $8.32/day`  

<details><summary>÷ 60 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-aleocc</code> BUY 1 @ 26¢ → $8.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 22¢ | 1 | ×0.2^4 = 0.0 |
|  | 21¢ | 1 | ×0.2^5 = 0.0 |
|  | 19¢ | 25 | ×0.2^7 = 0.0 |
|  | 18¢ | 52 | ×0.2^8 = 0.0 |
|  | 14¢ | 100 | ×0.2^12 = 0.0 |
|  | 13¢ | 21,250 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 99.8% = $8.31/day`  

<details><summary>÷ 60 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> BUY 200 @ 4¢ → $6.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 200 (200 yours) | ×0.1^0 = 200.0 |
|  | 1¢ | 2,200 | ×0.1^3 = 2.2 |
| | | **Σ** | **202.2** |

`yours 200.0 / Σ 202.2 = 98.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.9% = $6.18/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-dem</code> SELL 23 @ 92¢ → $6.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 23 (23 yours) | ×0.1^0 = 23.0 |
|  | 94¢ | 39 | ×0.1^2 = 0.4 |
|  | 99¢ | 5,097 | ×0.1^7 = 0.0 |
| | | **Σ** | **23.4** |

`yours 23.0 / Σ 23.4 = 98.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.3% = $6.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-mn-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 7 @ 13¢ → $3.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 7 (7 yours) | ×0.2^0 = 6.8 |
|  | 10¢ | 25 | ×0.2^3 = 0.2 |
|  | 1¢ | 300,374 | ×0.2^12 = 0.0 |
| | | **Σ** | **7.0** |

`yours 6.8 / Σ 7.0 = 97.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 97.1% = $3.74/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-kamhar</code> BUY 1 @ 29¢ → $8.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 27¢ | 1 | ×0.2^2 = 0.0 |
|  | 24¢ | 2 | ×0.2^5 = 0.0 |
|  | 23¢ | 1 | ×0.2^6 = 0.0 |
|  | 14¢ | 5 | ×0.2^15 = 0.0 |
|  | 10¢ | 29 | ×0.2^19 = 0.0 |
|  | 2¢ | 750 | ×0.2^27 = 0.0 |
|  | 1¢ | 29,409 | ×0.2^28 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 96.1%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 96.1% = $8.01/day`  

<details><summary>÷ 60 markets in this race (17 known) — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar` ← this one
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-stasmi</code> BUY 60 @ 10¢ → $7.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 64 (60 yours) | ×0.2^0 = 63.8 |
|  | 9¢ | 1 | ×0.2^1 = 0.2 |
|  | 6¢ | 1 | ×0.2^4 = 0.0 |
|  | 3¢ | 1 | ×0.2^7 = 0.0 |
|  | 2¢ | 1 | ×0.2^8 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^9 = 0.0 |
| | | **Σ** | **64.0** |

`yours 60.0 / Σ 64.0 = 93.7%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 93.7% = $7.81/day`  

<details><summary>÷ 60 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $5.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 43 (40 yours) | ×0.1^0 = 43.0 |
|  | 98¢ | 130,500 | ×0.1^94 = 0.0 |
| | | **Σ** | **43.0** |

`yours 40.0 / Σ 43.0 = 93.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.0% = $5.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-rep</code> SELL 11 @ 9¢ → $5.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 12 (11 yours) | ×0.1^0 = 12.0 |
|  | 15¢ | 1 | ×0.1^6 = 0.0 |
|  | 18¢ | 10 | ×0.1^9 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^89 = 0.0 |
| | | **Σ** | **12.0** |

`yours 11.0 / Σ 12.0 = 91.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 91.7% = $5.73/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem`
2. `usgubewc-usgub-mn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 5 @ 41¢ → $3.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 39¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 41¢ | 5 (5 yours) | ×0.2^2 = 0.2 |
|  | 52¢ | 0 | ×0.2^13 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^59 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.2 / Σ 0.2 = 90.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 90.9% = $3.79/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210` ← this one
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 25 @ 7¢ → $5.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 28 (25 yours) | ×0.1^0 = 28.0 |
|  | 98¢ | 130,500 | ×0.1^91 = 0.0 |
| | | **Σ** | **28.0** |

`yours 25.0 / Σ 28.0 = 89.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.3% = $5.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-co-2026-11-03-rep</code> SELL 50 @ 7¢ → $5.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 56 (50 yours) | ×0.1^0 = 56.0 |
|  | 98¢ | 130,500 | ×0.1^91 = 0.0 |
| | | **Σ** | **56.0** |

`yours 50.0 / Σ 56.0 = 89.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.3% = $5.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem`
2. `usgubewc-usgub-co-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> SELL 50 @ 10¢ → $5.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 11¢ | 61 | ×0.1^1 = 6.1 |
|  | 14¢ | 10 | ×0.1^4 = 0.0 |
|  | 98¢ | 265,567 | ×0.1^88 = 0.0 |
| | | **Σ** | **56.1** |

`yours 50.0 / Σ 56.1 = 89.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.1% = $5.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 24 @ 10¢ → $7.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 0.6 |
| ▶ | 10¢ | 24 (24 yours) | ×0.2^1 = 4.8 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
|  | 8¢ | 2 | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^6 = 0.0 |
|  | 4¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^10 = 0.0 |
| | | **Σ** | **5.4** |

`yours 4.8 / Σ 5.4 = 88.7%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 88.7% = $7.39/day`  

<details><summary>÷ 60 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> SELL 50 @ 7¢ → $5.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 57 (50 yours) | ×0.1^0 = 57.0 |
|  | 99¢ | 1,969 | ×0.1^92 = 0.0 |
| | | **Σ** | **57.0** |

`yours 50.0 / Σ 57.0 = 87.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 87.7% = $5.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> SELL 1 @ 22¢ → $7.27/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 25¢ | 1 | ×0.2^3 = 0.0 |
|  | 29¢ | 1 | ×0.2^7 = 0.0 |
|  | 30¢ | 53,877 | ×0.2^8 = 0.1 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 87.3%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 87.3% = $7.27/day`  

<details><summary>÷ 60 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-rokha</code> BUY 1 @ 16¢ → $7.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 14¢ | 1 | ×0.2^2 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 10¢ | 2 | ×0.2^6 = 0.0 |
|  | 8¢ | 1 | ×0.2^8 = 0.0 |
|  | 7¢ | 2 | ×0.2^9 = 0.0 |
|  | 3¢ | 2 | ×0.2^13 = 0.0 |
|  | 1¢ | 40,451 | ×0.2^15 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 86.9%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 86.9% = $7.24/day`  

<details><summary>÷ 60 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 75 @ 9¢ → $5.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 88 (75 yours) | ×0.1^0 = 88.0 |
|  | 98¢ | 208,063 | ×0.1^89 = 0.0 |
| | | **Σ** | **88.0** |

`yours 75.0 / Σ 88.0 = 85.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 85.2% = $5.33/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 20 @ 10¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 24 (20 yours) | ×0.1^0 = 24.0 |
|  | 98¢ | 65,250 | ×0.1^88 = 0.0 |
| | | **Σ** | **24.0** |

`yours 20.0 / Σ 24.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 96¢ → $5.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 98¢ | 106 | ×0.1^2 = 1.1 |
|  | 99¢ | 7,072 | ×0.1^3 = 7.1 |
| | | **Σ** | **48.1** |

`yours 40.0 / Σ 48.1 = 83.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.1% = $5.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 60 @ 10¢ → $6.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 2 | ×0.2^0 = 2.5 |
| ▶ | 10¢ | 60 (60 yours) | ×0.2^1 = 12.0 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^10 = 0.0 |
| | | **Σ** | **14.5** |

`yours 12.0 / Σ 14.5 = 82.9%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 82.9% = $6.91/day`  

<details><summary>÷ 60 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 18¢ → $6.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.2^0 = 1.2 |
|  | 10¢ | 60 | ×0.2^8 = 0.0 |
|  | 6¢ | 1 | ×0.2^12 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^17 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 82.6%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 82.6% = $6.89/day`  

<details><summary>÷ 60 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 60 @ 10¢ → $6.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 2 | ×0.2^0 = 2.5 |
| ▶ | 10¢ | 62 (60 yours) | ×0.2^1 = 12.4 |
|  | 6¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^10 = 0.0 |
| | | **Σ** | **14.9** |

`yours 12.0 / Σ 14.9 = 80.6%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 80.6% = $6.71/day`  

<details><summary>÷ 60 markets in this race (27 known) — tap to list</summary>

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (551,156 resting) | ~89.2% | ~$22.31 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (294,041 resting) | ~80.4% | ~$5.03 |
| `ewc-usgub-nv-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (3,012 resting) | ~69.7% | ~$4.36 |
| `ewc-usse-mi-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (551,355 resting) | ~69.5% | ~$4.34 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (263,886 resting) | ~56.3% | ~$3.52 |
| `ewc-usgub-mi-2026-11-03-rep` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (4,993 resting) | ~59.7% | ~$2.49 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (11,808 resting) | ~2.7% | ~$2.03 |
| `ewc-usse-nh-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (2,622 resting) | ~31.4% | ~$1.97 |
| `ewc-usmayor-losang-2026-11-03-karbas` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (204,998 resting) | ~30.2% | ~$1.89 |
| `ewc-usmayor-losang-2026-11-03-nitram` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (204,948 resting) | ~28.6% | ~$1.79 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (3,184 resting) | ~39.7% | ~$1.65 |
| `ewc-usse-nc-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (16,071 resting) | ~4.7% | ~$1.16 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $1,678.09 |
| Skipped | $1.41 |
| **Total earned** | **$3,567.53** |

2562 reward rows · 43 days with rewards · 550 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-14 | $274.59 | `██████████` |
| 2026-08-13 | $223.24 | `████████` |
| 2026-08-12 | $213.04 | `████████` |
| 2026-08-11 | $409.60 | `███████████████` |
| 2026-08-10 | $557.62 | `████████████████████` |
| 2026-08-09 | $62.24 | `██` |
| 2026-08-08 | $54.78 | `██` |
| 2026-08-07 | $60.33 | `██` |
| 2026-08-06 | $52.21 | `██` |
| 2026-08-05 | $31.46 | `█` |
| 2026-08-04 | $53.94 | `██` |
| 2026-08-03 | $44.81 | `██` |
| 2026-08-02 | $14.05 | `█` |
| 2026-08-01 | $52.30 | `██` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $2,104.21 | `████████████████████` |
| 2026-07 | $1,463.32 | `██████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $172.95 |
| `apdc-alito-2026-12-31` | $115.00 |
| `opdc-mcconnell-resign-2026-11-02` | $79.41 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $63.61 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $55.91 |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | $51.17 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.44 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.51 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.04 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `scc-senate-gop-2026-11-03-49` | $32.00 |
| `scc-senate-gop-2026-11-03-52` | $31.83 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-15 11:04 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-15 10:54 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-15 10:51 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-15 10:42 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-15 10:35 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-15 10:29 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-15 10:14 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-15 10:09 PM ET | ✅ ok | 2490 | $3508.28 |
| 2026-08-15 10:07 PM ET | ✅ ok | 2383 | $3325.26 |
| 2026-08-15 10:00 PM ET | ✅ ok | 2381 | $3292.94 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
