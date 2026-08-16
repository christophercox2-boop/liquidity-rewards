# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-16 11:41 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$242.08/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-rep` — BUY at the best price, ~$40.69/day for 200 contracts. Runners-up: `ewc-usse-tx-2026-11-03-dem` (~$23.27/day), `ewc-usgub-ga-2026-11-03-dem` (~$18.69/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$242.08/day (~$10.09/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ewc-usp-2028-11-07-rahema` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~100.0% of bid side (30,000 resting ≥ 20,000 ✓) ≈ $10.64/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~100.0% of bid side (30,058 resting ≥ 20,000 ✓) ≈ $10.64/day (program pool ÷ 47 markets) |
| `enwc-uspres-nom-dem-2028-kamhar` | SELL | 20.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~99.8% of ask side (85,764 resting ≥ 20,000 ✓) ≈ $10.62/day (program pool ÷ 47 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 58.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.8% of ask side (91,958 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-dontru` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~99.8% of bid side (30,058 resting ≥ 20,000 ✓) ≈ $10.61/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~99.6% of bid side (70,513 resting ≥ 20,000 ✓) ≈ $10.59/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~95.4% of bid side (27,506 resting ≥ 20,000 ✓) ≈ $10.15/day (program pool ÷ 47 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 14.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~94.0% of bid side (70,473 resting ≥ 20,000 ✓) ≈ $10.00/day (program pool ÷ 47 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | SELL | 11.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~92.0% of ask side (70,802 resting ≥ 20,000 ✓) ≈ $9.79/day (program pool ÷ 47 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $3.73/day (pool ÷ 3 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | BUY | 1.0¢ | 1,798 | 1 | $25.00 | ✅ scoring — ~89.1% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.57/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 10.0¢ | 60 | 1 | $1,000.00 | ✅ scoring — ~88.2% of bid side (30,060 resting ≥ 20,000 ✓) ≈ $9.38/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-tulgab` | SELL | 12.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~83.2% of ask side (86,827 resting ≥ 20,000 ✓) ≈ $8.85/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~80.6% of bid side (30,006 resting ≥ 20,000 ✓) ≈ $8.58/day (program pool ÷ 47 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 10.0¢ | 60 | 1 | $100.00 | ✅ scoring — ~79.6% of bid side (300,447 resting ≥ 5,000 ✓) ≈ $3.06/day (pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-markel` | BUY | 10.0¢ | 60 | 2 | $1,000.00 | ✅ scoring — ~70.4% of bid side (30,060 resting ≥ 20,000 ✓) ≈ $7.49/day (program pool ÷ 47 markets) |
| `ewc-usp-2028-11-07-gleyou` | BUY | 10.0¢ | 60 | 2 | $1,000.00 | ✅ scoring — ~66.7% of bid side (30,060 resting ≥ 20,000 ✓) ≈ $7.09/day (program pool ÷ 47 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | SELL | 19.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~52.9% of ask side (64,498 resting ≥ 20,000 ✓) ≈ $5.63/day (program pool ÷ 47 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 12.0¢ | 157 | 0 | $25.00 | ✅ scoring — ~50.0% of ask side (133,052 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 12.0¢ | 157 | 0 | $25.00 | ✅ scoring — ~50.0% of ask side (133,052 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~49.9% of bid side (3,599 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~49.9% of bid side (3,599 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-micoba` | SELL | 8.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~49.8% of ask side (59,500 resting ≥ 20,000 ✓) ≈ $5.30/day (program pool ÷ 47 markets) |
| `usgubewc-usgub-ct-2026-11-03-rep` | SELL | 12.0¢ | 84 | 0 | $25.00 | ✅ scoring — ~49.7% of ask side (201,610 resting ≥ 2,000 ✓) ≈ $3.11/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-rep` | SELL | 12.0¢ | 84 | 0 | $25.00 | ✅ scoring — ~49.7% of ask side (201,610 resting ≥ 2,000 ✓) ≈ $3.11/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 10.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~45.5% of bid side (76,486 resting ≥ 20,000 ✓) ≈ $4.85/day (program pool ÷ 47 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 9.0¢ | 5 | 1 | $1,000.00 | ✅ scoring — ~45.5% of bid side (76,486 resting ≥ 20,000 ✓) ≈ $4.85/day (program pool ÷ 47 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 9.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~35.1% of bid side (180,459 resting ≥ 20,000 ✓) ≈ $3.73/day (program pool ÷ 47 markets) |
| …and 216 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 1 @ 15¢ → $10.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 1 | ×0.2^6 = 0.0 |
|  | 2¢ | 1 | ×0.2^13 = 0.0 |
|  | 1¢ | 29,997 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 100.0% = $10.64/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 60 @ 10¢ → $10.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 60 (60 yours) | ×0.2^0 = 60.0 |
|  | 6¢ | 1 | ×0.2^4 = 0.0 |
|  | 3¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 29,996 | ×0.2^9 = 0.0 |
| | | **Σ** | **60.0** |

`yours 60.0 / Σ 60.0 = 100.0%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 100.0% = $10.64/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-kamhar</code> SELL 1 @ 20¢ → $10.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 25¢ | 2 | ×0.2^5 = 0.0 |
|  | 26¢ | 1 | ×0.2^6 = 0.0 |
|  | 27¢ | 1 | ×0.2^7 = 0.0 |
|  | 31¢ | 50,967 | ×0.2^11 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 99.8% = $10.62/day`  

<details><summary>÷ 47 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 1 @ 58¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 62¢ | 1 | ×0.2^4 = 0.0 |
|  | 66¢ | 213 | ×0.2^8 = 0.0 |
|  | 67¢ | 51 | ×0.2^9 = 0.0 |
|  | 68¢ | 1 | ×0.2^10 = 0.0 |
|  | 69¢ | 1 | ×0.2^11 = 0.0 |
|  | 70¢ | 1 | ×0.2^12 = 0.0 |
|  | 71¢ | 1 | ×0.2^13 = 0.0 |
|  | 72¢ | 1 | ×0.2^14 = 0.0 |
|  | 73¢ | 1 | ×0.2^15 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-dontru</code> BUY 60 @ 10¢ → $10.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 60 (60 yours) | ×0.2^0 = 60.0 |
|  | 9¢ | 0 | ×0.2^1 = 0.0 |
|  | 6¢ | 1 | ×0.2^4 = 0.0 |
|  | 5¢ | 250 | ×0.2^5 = 0.1 |
|  | 1¢ | 29,747 | ×0.2^9 = 0.0 |
| | | **Σ** | **60.1** |

`yours 60.0 / Σ 60.1 = 99.8%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 99.8% = $10.61/day`  

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 60 @ 10¢ → $10.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 60 (60 yours) | ×0.2^0 = 60.0 |
|  | 9¢ | 1 | ×0.2^1 = 0.2 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 70,450 | ×0.2^9 = 0.0 |
| | | **Σ** | **60.3** |

`yours 60.0 / Σ 60.3 = 99.6%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 99.6% = $10.59/day`  

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
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 1 @ 15¢ → $10.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 13¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 1 | ×0.2^3 = 0.0 |
|  | 8¢ | 1 | ×0.2^7 = 0.0 |
|  | 4¢ | 5 | ×0.2^11 = 0.0 |
|  | 1¢ | 27,497 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 95.4%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 95.4% = $10.15/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 14¢ → $10.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 11¢ | 1 | ×0.2^3 = 0.0 |
|  | 10¢ | 10 | ×0.2^4 = 0.0 |
|  | 1¢ | 70,460 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 94.0%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 94.0% = $10.00/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> SELL 1 @ 11¢ → $9.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 14¢ | 11 | ×0.2^3 = 0.1 |
|  | 22¢ | 30 | ×0.2^11 = 0.0 |
|  | 24¢ | 22,253 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 92.0%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 92.0% = $9.79/day`  

<details><summary>÷ 47 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> BUY 1,799 @ 1¢ → $5.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **200.9** |

`yours 179.9 / Σ 200.9 = 89.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.5% = $5.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 60 @ 10¢ → $9.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 2 | ×0.2^0 = 1.6 |
| ▶ | 10¢ | 60 (60 yours) | ×0.2^1 = 12.0 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 1¢ | 29,997 | ×0.2^10 = 0.0 |
| | | **Σ** | **13.6** |

`yours 12.0 / Σ 13.6 = 88.2%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 88.2% = $9.38/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> SELL 1 @ 12¢ → $8.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 13¢ | 1 | ×0.2^1 = 0.2 |
|  | 16¢ | 1 | ×0.2^4 = 0.0 |
|  | 20¢ | 287 | ×0.2^8 = 0.0 |
|  | 25¢ | 50,266 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 83.2%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 83.2% = $8.85/day`  

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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 1 @ 15¢ → $8.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 14¢ | 1 | ×0.2^1 = 0.2 |
|  | 13¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 6 | ×0.2^8 = 0.0 |
|  | 3¢ | 1,250 | ×0.2^12 = 0.0 |
|  | 1¢ | 28,747 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 80.6%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 80.6% = $8.58/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 60 @ 10¢ → $3.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 10¢ | 70 (60 yours) | ×0.2^1 = 14.0 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 1¢ | 300,374 | ×0.2^10 = 0.0 |
| | | **Σ** | **15.1** |

`yours 12.0 / Σ 15.1 = 79.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 79.6% = $3.06/day`  

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
<details><summary><code>ewc-usp-2028-11-07-markel</code> BUY 60 @ 10¢ → $7.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 10¢ | 60 (60 yours) | ×0.2^2 = 2.4 |
|  | 9¢ | 1 | ×0.2^3 = 0.0 |
|  | 3¢ | 1 | ×0.2^9 = 0.0 |
|  | 1¢ | 29,997 | ×0.2^11 = 0.0 |
| | | **Σ** | **3.4** |

`yours 2.4 / Σ 3.4 = 70.4%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 70.4% = $7.49/day`  

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
<details><summary><code>ewc-usp-2028-11-07-gleyou</code> BUY 60 @ 10¢ → $7.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 1 | ×0.2^0 = 1.0 |
|  | 11¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 10¢ | 60 (60 yours) | ×0.2^2 = 2.4 |
|  | 6¢ | 1 | ×0.2^6 = 0.0 |
|  | 4¢ | 1 | ×0.2^8 = 0.0 |
|  | 1¢ | 29,996 | ×0.2^11 = 0.0 |
| | | **Σ** | **3.6** |

`yours 2.4 / Σ 3.6 = 66.7%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 66.7% = $7.09/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> SELL 1 @ 19¢ → $5.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 2 (1 yours) | ×0.2^0 = 1.9 |
|  | 27¢ | 1 | ×0.2^8 = 0.0 |
|  | 29¢ | 1 | ×0.2^10 = 0.0 |
|  | 31¢ | 30 | ×0.2^12 = 0.0 |
|  | 32¢ | 29,672 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.9** |

`yours 1.0 / Σ 1.9 = 52.9%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 52.9% = $5.63/day`  

<details><summary>÷ 47 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 157 @ 12¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 314 (157 yours) | ×0.1^0 = 314.0 |
|  | 87¢ | 13 | ×0.1^75 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **314.0** |

`yours 157.0 / Σ 314.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 157 @ 12¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 314 (157 yours) | ×0.1^0 = 314.0 |
|  | 87¢ | 13 | ×0.1^75 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **314.0** |

`yours 157.0 / Σ 314.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 3,598 (1,799 yours) | ×0.1^1 = 359.8 |
| | | **Σ** | **360.8** |

`yours 179.9 / Σ 360.8 = 49.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.9% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 3,598 (1,799 yours) | ×0.1^1 = 359.8 |
| | | **Σ** | **360.8** |

`yours 179.9 / Σ 360.8 = 49.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.9% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-micoba</code> SELL 1 @ 8¢ → $5.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 14¢ | 106 | ×0.2^6 = 0.0 |
|  | 17¢ | 1 | ×0.2^9 = 0.0 |
|  | 19¢ | 1,344 | ×0.2^11 = 0.0 |
|  | 20¢ | 755 | ×0.2^12 = 0.0 |
|  | 25¢ | 21,021 | ×0.2^17 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 49.8%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 49.8% = $5.30/day`  

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
17. `ewc-usp-2028-11-07-micoba` ← this one
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
<details><summary><code>usgubewc-usgub-ct-2026-11-03-rep</code> SELL 84 @ 12¢ → $3.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 169 (84 yours) | ×0.1^0 = 169.0 |
|  | 92¢ | 41 | ×0.1^80 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **169.0** |

`yours 84.0 / Σ 169.0 = 49.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.7% = $3.11/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem`
2. `usgubewc-usgub-ct-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-rep</code> SELL 84 @ 12¢ → $3.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 169 (84 yours) | ×0.1^0 = 169.0 |
|  | 92¢ | 41 | ×0.1^80 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **169.0** |

`yours 84.0 / Σ 169.0 = 49.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.7% = $3.11/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem`
2. `usgubewc-usgub-ct-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 1 @ 10¢ → $4.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 5 | ×0.2^1 = 1.0 |
|  | 3¢ | 30 | ×0.2^7 = 0.0 |
|  | 2¢ | 76,250 | ×0.2^8 = 0.2 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 45.5%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 45.5% = $4.85/day`  

<details><summary>÷ 47 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 5 @ 9¢ → $4.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 9¢ | 5 (5 yours) | ×0.2^1 = 1.0 |
|  | 3¢ | 30 | ×0.2^7 = 0.0 |
|  | 2¢ | 76,250 | ×0.2^8 = 0.2 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 45.5%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 45.5% = $4.85/day`  

<details><summary>÷ 47 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 1 @ 9¢ → $3.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2 (1 yours) | ×0.2^0 = 2.3 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 5¢ | 5 | ×0.2^4 = 0.0 |
|  | 3¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **2.9** |

`yours 1.0 / Σ 2.9 = 35.1%`  
`$1,000 ÷ 47 ÷ 2 = $10.64 × 35.1% = $3.73/day`  

<details><summary>÷ 47 markets in this race (14 known) — tap to list</summary>

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

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,314 resting) | ~54.3% | ~$40.69 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (621,992 resting) | ~31.0% | ~$23.27 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,070 resting) | ~24.9% | ~$18.69 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,720 resting) | ~27.8% | ~$6.95 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (277,521 resting) | ~9.1% | ~$6.80 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (35,824 resting) | ~10.7% | ~$2.67 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (280,809 resting) | ~2.2% | ~$1.62 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (80,259 resting) | ~24.9% | ~$1.56 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (73,654 resting) | ~36.3% | ~$1.51 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (21,461 resting) | ~3.0% | ~$1.50 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,401 resting) | ~1.9% | ~$1.44 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (374,345 resting) | ~21.9% | ~$1.37 |

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
| 2026-08-16 11:41 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:29 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:26 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:15 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:10 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:03 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:59 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:47 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:38 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:22 AM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
