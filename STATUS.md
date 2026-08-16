# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-16 11:55 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$238.54/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-rep` — BUY at the best price, ~$27.74/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$18.44/day), `ewc-usse-tx-2026-11-03-dem` (~$17.75/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$238.54/day (~$9.94/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ewc-usp-2028-11-07-elomus` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~100.0% of bid side (27,506 resting ≥ 20,000 ✓) ≈ $10.20/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~100.0% of bid side (30,057 resting ≥ 20,000 ✓) ≈ $10.20/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~99.9% of bid side (70,511 resting ≥ 20,000 ✓) ≈ $10.20/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-dontru` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~99.8% of bid side (30,157 resting ≥ 20,000 ✓) ≈ $10.18/day (program pool ÷ 49 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 14.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~98.4% of bid side (70,567 resting ≥ 20,000 ✓) ≈ $10.04/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 15.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~96.1% of bid side (30,007 resting ≥ 20,000 ✓) ≈ $9.81/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 10.0¢ | 60 | 1 | $1,000.00 | ✅ scoring — ~95.2% of bid side (40,083 resting ≥ 20,000 ✓) ≈ $9.72/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-markel` | BUY | 14.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~92.4% of bid side (30,006 resting ≥ 20,000 ✓) ≈ $9.43/day (program pool ÷ 49 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | SELL | 11.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~92.0% of ask side (70,789 resting ≥ 20,000 ✓) ≈ $9.39/day (program pool ÷ 49 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.5% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~89.1% of bid side (2,001 resting ≥ 2,000 ✓) ≈ $3.71/day (pool ÷ 3 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | BUY | 1.0¢ | 1,798 | 1 | $25.00 | ✅ scoring — ~89.1% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $5.57/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~87.0% of bid side (2,006 resting ≥ 2,000 ✓) ≈ $5.43/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-kamhar` | SELL | 20.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~83.2% of ask side (85,766 resting ≥ 20,000 ✓) ≈ $8.49/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-gleyou` | BUY | 10.0¢ | 60 | 2 | $1,000.00 | ✅ scoring — ~70.6% of bid side (40,158 resting ≥ 20,000 ✓) ≈ $7.20/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-jossha` | BUY | 9.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~59.3% of bid side (101,463 resting ≥ 20,000 ✓) ≈ $6.05/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 9.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~58.8% of bid side (74,030 resting ≥ 20,000 ✓) ≈ $6.00/day (program pool ÷ 49 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | SELL | 19.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~52.9% of ask side (65,827 resting ≥ 20,000 ✓) ≈ $5.40/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 14.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~50.0% of bid side (30,111 resting ≥ 20,000 ✓) ≈ $5.10/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 14.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~50.0% of bid side (30,111 resting ≥ 20,000 ✓) ≈ $5.10/day (program pool ÷ 49 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~46.0% of bid side (3,899 resting ≥ 2,000 ✓) ≈ $2.88/day (pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | BUY | 1.0¢ | 1,799 | 1 | $25.00 | ✅ scoring — ~46.0% of bid side (3,899 resting ≥ 2,000 ✓) ≈ $2.88/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 10.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~45.5% of bid side (76,486 resting ≥ 20,000 ✓) ≈ $4.65/day (program pool ÷ 49 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 9.0¢ | 5 | 1 | $1,000.00 | ✅ scoring — ~45.5% of bid side (76,486 resting ≥ 20,000 ✓) ≈ $4.65/day (program pool ÷ 49 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 12.0¢ | 157 | 0 | $25.00 | ✅ scoring — ~42.4% of ask side (133,165 resting ≥ 2,000 ✓) ≈ $2.65/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 12.0¢ | 157 | 0 | $25.00 | ✅ scoring — ~42.4% of ask side (133,165 resting ≥ 2,000 ✓) ≈ $2.65/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~36.2% of bid side (300,443 resting ≥ 5,000 ✓) ≈ $1.39/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~36.2% of bid side (300,443 resting ≥ 5,000 ✓) ≈ $1.39/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | BUY | 9.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~34.5% of bid side (180,460 resting ≥ 20,000 ✓) ≈ $3.52/day (program pool ÷ 49 markets) |
| `ewc-usp-2028-11-07-dwajoh` | BUY | 8.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~32.5% of bid side (72,007 resting ≥ 20,000 ✓) ≈ $3.31/day (program pool ÷ 49 markets) |
| …and 231 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 1 @ 15¢ → $10.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 1 | ×0.2^7 = 0.0 |
|  | 7¢ | 1 | ×0.2^8 = 0.0 |
|  | 6¢ | 1 | ×0.2^9 = 0.0 |
|  | 4¢ | 5 | ×0.2^11 = 0.0 |
|  | 1¢ | 27,497 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 100.0% = $10.20/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 60 @ 10¢ → $10.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 60 (60 yours) | ×0.2^0 = 60.0 |
|  | 3¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 29,996 | ×0.2^9 = 0.0 |
| | | **Σ** | **60.0** |

`yours 60.0 / Σ 60.0 = 100.0%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 100.0% = $10.20/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 60 @ 10¢ → $10.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 60 (60 yours) | ×0.2^0 = 60.0 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 1¢ | 70,450 | ×0.2^9 = 0.0 |
| | | **Σ** | **60.0** |

`yours 60.0 / Σ 60.0 = 99.9%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 99.9% = $10.20/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-dontru</code> BUY 60 @ 10¢ → $10.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 60 (60 yours) | ×0.2^0 = 60.0 |
|  | 9¢ | 0 | ×0.2^1 = 0.0 |
|  | 5¢ | 250 | ×0.2^5 = 0.1 |
|  | 1¢ | 29,847 | ×0.2^9 = 0.0 |
| | | **Σ** | **60.1** |

`yours 60.0 / Σ 60.1 = 99.8%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 99.8% = $10.18/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 14¢ → $10.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 11¢ | 1 | ×0.2^3 = 0.0 |
|  | 10¢ | 5 | ×0.2^4 = 0.0 |
|  | 1¢ | 70,560 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.4%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 98.4% = $10.04/day`  

<details><summary>÷ 49 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 1 @ 15¢ → $9.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 13¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 1 | ×0.2^5 = 0.0 |
|  | 8¢ | 1 | ×0.2^7 = 0.0 |
|  | 7¢ | 1 | ×0.2^8 = 0.0 |
|  | 5¢ | 5 | ×0.2^10 = 0.0 |
|  | 1¢ | 29,997 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 96.1%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 96.1% = $9.81/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 60 @ 10¢ → $9.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 0.6 |
| ▶ | 10¢ | 60 (60 yours) | ×0.2^1 = 12.0 |
|  | 1¢ | 40,022 | ×0.2^10 = 0.0 |
| | | **Σ** | **12.6** |

`yours 12.0 / Σ 12.6 = 95.2%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 95.2% = $9.72/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-markel</code> BUY 1 @ 14¢ → $9.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 12¢ | 2 | ×0.2^2 = 0.1 |
|  | 9¢ | 5 | ×0.2^5 = 0.0 |
|  | 5¢ | 1 | ×0.2^9 = 0.0 |
|  | 1¢ | 29,997 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 92.4%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 92.4% = $9.43/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> SELL 1 @ 11¢ → $9.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 14¢ | 11 | ×0.2^3 = 0.1 |
|  | 22¢ | 30 | ×0.2^11 = 0.0 |
|  | 24¢ | 22,240 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 92.0%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 92.0% = $9.39/day`  

<details><summary>÷ 49 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>usgubewc-usgub-ri-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $3.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **201.9** |

`yours 179.9 / Σ 201.9 = 89.1%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 89.1% = $3.71/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep`

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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $5.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 7 | ×0.1^0 = 7.0 |
| ▶ | 1¢ | 1,999 (1,799 yours) | ×0.1^1 = 199.9 |
| | | **Σ** | **206.9** |

`yours 179.9 / Σ 206.9 = 87.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 87.0% = $5.43/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-kamhar</code> SELL 1 @ 20¢ → $8.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 1 | ×0.2^1 = 0.2 |
|  | 25¢ | 1 | ×0.2^5 = 0.0 |
|  | 26¢ | 1 | ×0.2^6 = 0.0 |
|  | 27¢ | 1 | ×0.2^7 = 0.0 |
|  | 31¢ | 50,967 | ×0.2^11 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 83.2%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 83.2% = $8.49/day`  

<details><summary>÷ 49 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-gleyou</code> BUY 60 @ 10¢ → $7.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 10¢ | 60 (60 yours) | ×0.2^2 = 2.4 |
|  | 6¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 40,096 | ×0.2^11 = 0.0 |
| | | **Σ** | **3.4** |

`yours 2.4 / Σ 3.4 = 70.6%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 70.6% = $7.20/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-jossha</code> BUY 1 @ 9¢ → $6.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 6¢ | 6 | ×0.2^3 = 0.0 |
|  | 4¢ | 1,005 | ×0.2^5 = 0.3 |
|  | 1¢ | 100,450 | ×0.2^8 = 0.3 |
| | | **Σ** | **1.7** |

`yours 1.0 / Σ 1.7 = 59.3%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 59.3% = $6.05/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 1 @ 9¢ → $6.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 2 | ×0.2^1 = 0.4 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 6¢ | 5 | ×0.2^3 = 0.0 |
|  | 1¢ | 74,021 | ×0.2^8 = 0.2 |
| | | **Σ** | **1.7** |

`yours 1.0 / Σ 1.7 = 58.8%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 58.8% = $6.00/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> SELL 1 @ 19¢ → $5.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 2 (1 yours) | ×0.2^0 = 1.9 |
|  | 27¢ | 2 | ×0.2^8 = 0.0 |
|  | 29¢ | 1 | ×0.2^10 = 0.0 |
|  | 31¢ | 30 | ×0.2^12 = 0.0 |
|  | 32¢ | 31,000 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.9** |

`yours 1.0 / Σ 1.9 = 52.9%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 52.9% = $5.40/day`  

<details><summary>÷ 49 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 1 @ 14¢ → $5.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 7¢ | 6 | ×0.2^7 = 0.0 |
|  | 6¢ | 5 | ×0.2^8 = 0.0 |
|  | 3¢ | 1,250 | ×0.2^11 = 0.0 |
|  | 1¢ | 28,847 | ×0.2^13 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 50.0%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 50.0% = $5.10/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 1 @ 14¢ → $5.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 7¢ | 6 | ×0.2^7 = 0.0 |
|  | 6¢ | 5 | ×0.2^8 = 0.0 |
|  | 3¢ | 1,250 | ×0.2^11 = 0.0 |
|  | 1¢ | 28,847 | ×0.2^13 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 50.0%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 50.0% = $5.10/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $2.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 3,898 (1,799 yours) | ×0.1^1 = 389.8 |
| | | **Σ** | **390.8** |

`yours 179.9 / Σ 390.8 = 46.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 46.0% = $2.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> BUY 1,799 @ 1¢ → $2.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 1¢ | 3,898 (1,799 yours) | ×0.1^1 = 389.8 |
| | | **Σ** | **390.8** |

`yours 179.9 / Σ 390.8 = 46.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 46.0% = $2.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 1 @ 10¢ → $4.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 5 | ×0.2^1 = 1.0 |
|  | 3¢ | 30 | ×0.2^7 = 0.0 |
|  | 2¢ | 76,250 | ×0.2^8 = 0.2 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 45.5%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 45.5% = $4.65/day`  

<details><summary>÷ 49 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 5 @ 9¢ → $4.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 9¢ | 5 (5 yours) | ×0.2^1 = 1.0 |
|  | 3¢ | 30 | ×0.2^7 = 0.0 |
|  | 2¢ | 76,250 | ×0.2^8 = 0.2 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 45.5%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 45.5% = $4.65/day`  

<details><summary>÷ 49 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 157 @ 12¢ → $2.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 370 (157 yours) | ×0.1^0 = 370.0 |
|  | 97¢ | 2,070 | ×0.1^85 = 0.0 |
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
|  | 97¢ | 2,070 | ×0.1^85 = 0.0 |
| | | **Σ** | **370.0** |

`yours 157.0 / Σ 370.0 = 42.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 42.4% = $2.65/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 1 @ 13¢ → $1.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 12¢ | 1 | ×0.2^1 = 0.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 65 | ×0.2^3 = 0.5 |
|  | 1¢ | 300,374 | ×0.2^12 = 0.0 |
| | | **Σ** | **2.8** |

`yours 1.0 / Σ 2.8 = 36.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 36.2% = $1.39/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 1 @ 13¢ → $1.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 12¢ | 1 | ×0.2^1 = 0.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 65 | ×0.2^3 = 0.5 |
|  | 1¢ | 300,374 | ×0.2^12 = 0.0 |
| | | **Σ** | **2.8** |

`yours 1.0 / Σ 2.8 = 36.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 36.2% = $1.39/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> BUY 1 @ 9¢ → $3.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2 (1 yours) | ×0.2^0 = 2.3 |
|  | 7¢ | 2 | ×0.2^2 = 0.1 |
|  | 6¢ | 1 | ×0.2^3 = 0.0 |
|  | 5¢ | 5 | ×0.2^4 = 0.0 |
|  | 1¢ | 180,450 | ×0.2^8 = 0.5 |
| | | **Σ** | **2.9** |

`yours 1.0 / Σ 2.9 = 34.5%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 34.5% = $3.52/day`  

<details><summary>÷ 49 markets in this race (14 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-dwajoh</code> BUY 1 @ 8¢ → $3.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 5 | ×0.2^1 = 1.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 5¢ | 2 | ×0.2^3 = 0.0 |
|  | 2¢ | 2,002 | ×0.2^6 = 0.1 |
|  | 1¢ | 69,996 | ×0.2^7 = 0.9 |
| | | **Σ** | **3.1** |

`yours 1.0 / Σ 3.1 = 32.5%`  
`$1,000 ÷ 49 ÷ 2 = $10.20 × 32.5% = $3.31/day`  

<details><summary>÷ 49 markets in this race (27 known) — tap to list</summary>

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,323 resting) | ~37.0% | ~$27.74 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,333 resting) | ~24.6% | ~$18.44 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (617,179 resting) | ~23.7% | ~$17.75 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (277,459 resting) | ~10.2% | ~$7.65 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,722 resting) | ~27.7% | ~$6.93 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (35,824 resting) | ~10.7% | ~$2.67 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (75,468 resting) | ~26.2% | ~$1.64 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (58,654 resting) | ~36.3% | ~$1.51 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (21,533 resting) | ~3.0% | ~$1.48 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (280,414 resting) | ~1.9% | ~$1.46 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (65,427 resting) | ~22.8% | ~$1.42 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (59,401 resting) | ~1.6% | ~$1.20 |

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
| 2026-08-16 11:55 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:51 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:41 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:29 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:26 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:15 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:10 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 11:03 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:59 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 10:47 AM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
