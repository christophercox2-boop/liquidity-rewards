# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-16 12:59 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$266.95/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-rep` — BUY at the best price, ~$19.95/day for 200 contracts. Runners-up: `ewc-usse-tx-2026-11-03-dem` (~$17.74/day), `ewc-usgub-ga-2026-11-03-dem` (~$15.33/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$266.95/day (~$11.12/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ushrp-fl19-2026-08-18-olahaw` | SELL | 12.0¢ | 76 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (3,757 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 26.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,959 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `usgubewc-usgub-ri-2026-11-03-kenblo` | BUY | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.4% of bid side (6,201 resting ≥ 2,000 ✓) ≈ $4.14/day (pool ÷ 3 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~90.9% of bid side (30,063 resting ≥ 20,000 ✓) ≈ $9.67/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-gleyou` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~90.9% of bid side (30,063 resting ≥ 20,000 ✓) ≈ $9.67/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~90.8% of bid side (70,517 resting ≥ 20,000 ✓) ≈ $9.66/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-dontru` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~90.8% of bid side (30,063 resting ≥ 20,000 ✓) ≈ $9.66/day (program pool ÷ 47 markets) |
| `usgubewc-usgub-ri-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $3.73/day (pool ÷ 3 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $3.73/day (pool ÷ 3 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~89.3% of bid side (27,507 resting ≥ 20,000 ✓) ≈ $9.50/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 14.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~89.2% of bid side (30,011 resting ≥ 20,000 ✓) ≈ $9.49/day (program pool ÷ 47 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | BUY | 1.0¢ | 1,798 | 1 | $25.00 | ✅ scoring — ~89.1% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.57/day (pool ÷ 2 markets) |
| `ussewc-usse-co-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~87.8% of bid side (2,004 resting ≥ 2,000 ✓) ≈ $5.49/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~71.7% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $4.48/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 10.0¢ | 60 | 2 | $1,000.00 | ✅ scoring — ~60.4% of bid side (30,061 resting ≥ 20,000 ✓) ≈ $6.43/day (program pool ÷ 47 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~47.2% of bid side (3,799 resting ≥ 2,000 ✓) ≈ $2.95/day (pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~47.2% of bid side (3,799 resting ≥ 2,000 ✓) ≈ $2.95/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~47.2% of bid side (30,014 resting ≥ 20,000 ✓) ≈ $5.02/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~47.2% of bid side (30,014 resting ≥ 20,000 ✓) ≈ $5.02/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-dwajoh` | BUY | 10.0¢ | 5 | 0 | $1,000.00 | ✅ scoring — ~45.0% of bid side (30,015 resting ≥ 20,000 ✓) ≈ $4.79/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-dwajoh` | BUY | 10.0¢ | 5 | 0 | $1,000.00 | ✅ scoring — ~45.0% of bid side (30,015 resting ≥ 20,000 ✓) ≈ $4.79/day (program pool ÷ 47 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 12.0¢ | 157 | 0 | $25.00 | ✅ scoring — ~42.4% of ask side (133,175 resting ≥ 2,000 ✓) ≈ $2.65/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 12.0¢ | 157 | 0 | $25.00 | ✅ scoring — ~42.4% of ask side (133,175 resting ≥ 2,000 ✓) ≈ $2.65/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 12.0¢ | 1 | 1 | $1,000.00 | ✅ scoring — ~41.6% of bid side (70,477 resting ≥ 20,000 ✓) ≈ $4.43/day (program pool ÷ 47 markets) |
| …and 328 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> SELL 76 @ 12¢ → $1.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 76 (76 yours) | ×0.1^0 = 76.0 |
|  | 99¢ | 3,681 | ×0.1^87 = 0.0 |
| | | **Σ** | **76.0** |

`yours 76.0 / Σ 76.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 1 @ 26¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 51¢ | 1 | ×0.2^25 = 0.0 |
|  | 54¢ | 1 | ×0.2^28 = 0.0 |
|  | 66¢ | 213 | ×0.2^40 = 0.0 |
|  | 67¢ | 51 | ×0.2^41 = 0.0 |
|  | 68¢ | 1 | ×0.2^42 = 0.0 |
|  | 69¢ | 1 | ×0.2^43 = 0.0 |
|  | 70¢ | 1 | ×0.2^44 = 0.0 |
|  | 71¢ | 1 | ×0.2^45 = 0.0 |
|  | 72¢ | 1 | ×0.2^46 = 0.0 |
| | … | +25 levels | 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>usgubewc-usgub-ri-2026-11-03-kenblo</code> BUY 1 @ 7¢ → $4.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 1¢ | 6,200 | ×0.1^6 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.4%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 99.4% = $4.14/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo` ← this one
3. `usgubewc-usgub-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 60 @ 10¢ → $9.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 66 (60 yours) | ×0.2^0 = 66.0 |
|  | 3¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 29,996 | ×0.2^9 = 0.0 |
| | | **Σ** | **66.0** |

`yours 60.0 / Σ 66.0 = 90.9%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 90.9% = $9.67/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-gleyou</code> BUY 60 @ 10¢ → $9.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 66 (60 yours) | ×0.2^0 = 66.0 |
|  | 6¢ | 1 | ×0.2^4 = 0.0 |
|  | 1¢ | 29,996 | ×0.2^9 = 0.0 |
| | | **Σ** | **66.0** |

`yours 60.0 / Σ 66.0 = 90.9%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 90.9% = $9.67/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 60 @ 10¢ → $9.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 66 (60 yours) | ×0.2^0 = 66.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 1¢ | 70,450 | ×0.2^9 = 0.0 |
| | | **Σ** | **66.0** |

`yours 60.0 / Σ 66.0 = 90.8%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 90.8% = $9.66/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-dontru</code> BUY 60 @ 10¢ → $9.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 66 (60 yours) | ×0.2^0 = 66.0 |
|  | 5¢ | 250 | ×0.2^5 = 0.1 |
|  | 1¢ | 29,747 | ×0.2^9 = 0.0 |
| | | **Σ** | **66.1** |

`yours 60.0 / Σ 66.1 = 90.8%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 90.8% = $9.66/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru` ← this one
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
<details><summary><code>usgubewc-usgub-ri-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $3.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 89.5% = $3.73/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $5.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $3.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 89.5% = $3.73/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $5.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $5.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $5.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 1 @ 15¢ → $9.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 7¢ | 2 | ×0.2^8 = 0.0 |
|  | 5¢ | 6 | ×0.2^10 = 0.0 |
|  | 3¢ | 1 | ×0.2^12 = 0.0 |
|  | 1¢ | 27,497 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 89.3%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 89.3% = $9.50/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 1 @ 14¢ → $9.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 9¢ | 1 | ×0.2^5 = 0.0 |
|  | 8¢ | 6 | ×0.2^6 = 0.0 |
|  | 7¢ | 1 | ×0.2^7 = 0.0 |
|  | 6¢ | 5 | ×0.2^8 = 0.0 |
|  | 3¢ | 1,250 | ×0.2^11 = 0.0 |
|  | 1¢ | 28,747 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 89.2%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 89.2% = $9.49/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> BUY 1,798 @ 1¢ → $5.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 1¢ | 1,998 (1,798 yours) | ×0.1^1 = 199.8 |
| | | **Σ** | **201.8** |

`yours 179.8 / Σ 201.8 = 89.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.1% = $5.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-co-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 5 | ×0.1^0 = 5.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **204.9** |

`yours 179.9 / Σ 204.9 = 87.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 87.8% = $5.49/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem`
2. `ussewc-usse-co-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $4.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 2,499 (1,799 yours) | ×0.1^1 = 249.9 |
| | | **Σ** | **250.9** |

`yours 179.9 / Σ 250.9 = 71.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.7% = $4.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 60 @ 10¢ → $6.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 1 | ×0.2^0 = 1.0 |
|  | 11¢ | 3 | ×0.2^1 = 0.6 |
| ▶ | 10¢ | 60 (60 yours) | ×0.2^2 = 2.4 |
|  | 1¢ | 29,997 | ×0.2^11 = 0.0 |
| | | **Σ** | **4.0** |

`yours 2.4 / Σ 4.0 = 60.4%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 60.4% = $6.43/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $2.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 3,798 (1,799 yours) | ×0.1^1 = 379.8 |
| | | **Σ** | **380.8** |

`yours 179.9 / Σ 380.8 = 47.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 47.2% = $2.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $2.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 3,798 (1,799 yours) | ×0.1^1 = 379.8 |
| | | **Σ** | **380.8** |

`yours 179.9 / Σ 380.8 = 47.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 47.2% = $2.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 1 @ 15¢ → $5.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 2 (1 yours) | ×0.2^0 = 2.1 |
|  | 10¢ | 1 | ×0.2^5 = 0.0 |
|  | 8¢ | 1 | ×0.2^7 = 0.0 |
|  | 7¢ | 2 | ×0.2^8 = 0.0 |
|  | 6¢ | 6 | ×0.2^9 = 0.0 |
|  | 5¢ | 5 | ×0.2^10 = 0.0 |
|  | 1¢ | 29,997 | ×0.2^14 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 47.2%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 47.2% = $5.02/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 1 @ 15¢ → $5.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 2 (1 yours) | ×0.2^0 = 2.1 |
|  | 10¢ | 1 | ×0.2^5 = 0.0 |
|  | 8¢ | 1 | ×0.2^7 = 0.0 |
|  | 7¢ | 2 | ×0.2^8 = 0.0 |
|  | 6¢ | 6 | ×0.2^9 = 0.0 |
|  | 5¢ | 5 | ×0.2^10 = 0.0 |
|  | 1¢ | 29,997 | ×0.2^14 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 47.2%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 47.2% = $5.02/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-dwajoh</code> BUY 5 @ 10¢ → $4.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 11 (5 yours) | ×0.2^0 = 11.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 5 | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 2¢ | 1 | ×0.2^8 = 0.0 |
|  | 1¢ | 29,996 | ×0.2^9 = 0.0 |
| | | **Σ** | **11.1** |

`yours 5.0 / Σ 11.1 = 45.0%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 45.0% = $4.79/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-dwajoh</code> BUY 5 @ 10¢ → $4.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 11 (5 yours) | ×0.2^0 = 11.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 5 | ×0.2^3 = 0.0 |
|  | 5¢ | 1 | ×0.2^5 = 0.0 |
|  | 2¢ | 1 | ×0.2^8 = 0.0 |
|  | 1¢ | 29,996 | ×0.2^9 = 0.0 |
| | | **Σ** | **11.1** |

`yours 5.0 / Σ 11.1 = 45.0%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 45.0% = $4.79/day`  

<details><summary>÷ 47 markets in this race (27 known) — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh` ← this one
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
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 157 @ 12¢ → $2.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 370 (157 yours) | ×0.1^0 = 370.0 |
|  | 97¢ | 2,080 | ×0.1^85 = 0.0 |
| | | **Σ** | **370.0** |

`yours 157.0 / Σ 370.0 = 42.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 42.4% = $2.65/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 157 @ 12¢ → $2.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 370 (157 yours) | ×0.1^0 = 370.0 |
|  | 97¢ | 2,080 | ×0.1^85 = 0.0 |
| | | **Σ** | **370.0** |

`yours 157.0 / Σ 370.0 = 42.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 42.4% = $2.65/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 12¢ → $4.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 0 | ×0.2^0 = 0.1 |
| ▶ | 12¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 15 | ×0.2^3 = 0.1 |
|  | 1¢ | 70,460 | ×0.2^12 = 0.0 |
| | | **Σ** | **0.5** |

`yours 0.2 / Σ 0.5 = 41.6%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 41.6% = $4.43/day`  

<details><summary>÷ 47 markets in this race (17 known) — tap to list</summary>

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (72,171 resting) | ~26.6% | ~$19.95 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (617,264 resting) | ~23.7% | ~$17.74 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,622 resting) | ~20.4% | ~$15.33 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,704 resting) | ~28.4% | ~$7.11 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (278,222 resting) | ~7.5% | ~$5.59 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (277,972 resting) | ~3.1% | ~$2.29 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,878 resting) | ~8.6% | ~$2.15 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (90,710 resting) | ~31.3% | ~$1.95 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (21,514 resting) | ~3.0% | ~$1.48 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (359,941 resting) | ~22.1% | ~$1.38 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (88,193 resting) | ~30.6% | ~$1.27 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (150,695 resting) | ~1.5% | ~$1.16 |

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
| 2026-08-14 ⚠️ multi-day pending bucket | $274.59 | `██████████` |
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
| 2026-08-16 12:59 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 12:08 PM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:58 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:55 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:51 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:41 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:29 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:26 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:15 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:10 AM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
