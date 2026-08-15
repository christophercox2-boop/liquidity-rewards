# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-14 8:12 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$1,001.07/day estimated (ceiling, not promise — details below)

**Earned:** $3,069.69 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-12: **$213.04** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-11: **$409.59** · 2026-08-10: **$557.62** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-nv-2026-11-03-rep` — BUY at the best price, ~$6.05/day for 200 contracts. Runners-up: `ewc-usmayor-losang-2026-11-03-karbas` (~$2.94/day), `ewc-usse-nc-2026-11-03-dem` (~$2.41/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$1,001.07/day (~$41.71/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-uspres-nom-dem-2028-aleocc` | BUY | 30.0¢ | 5 | 0 | $1,000.00 | ✅ scoring — ~100.0% of bid side (31,889 resting ≥ 20,000 ✓) ≈ $29.41/day (pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 28.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,849 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (92,092 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 28.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,759 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `ussewc-usse-ks-2026-11-03-dem` | BUY | 27.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,513 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-rep` | SELL | 90.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,481 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 38.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (400,231 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `usgubewc-usgub-mn-2026-11-03-dem` | SELL | 92.0¢ | 23 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (5,120 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,509 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 10.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~99.4% of bid side (301,399 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 42.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~99.4% of bid side (11,101 resting ≥ 10,000 ✓) ≈ $4.14/day (pool ÷ 6 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 17.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~98.4% of bid side (50,572 resting ≥ 5,000 ✓) ≈ $3.78/day (pool ÷ 13 markets) |
| `ussewc-usse-co-2026-11-03-dem` | BUY | 92.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (500,388 resting ≥ 2,000 ✓) ≈ $5.95/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~93.0% of ask side (130,768 resting ≥ 2,000 ✓) ≈ $5.81/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-rep` | SELL | 9.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~91.7% of ask side (196,023 resting ≥ 2,000 ✓) ≈ $5.73/day (pool ÷ 2 markets) |
| `ewc-usp-party-2028-11-07-dem` | BUY | 63.0¢ | 20 | 0 | $1,000.00 | ✅ scoring — ~91.0% of bid side (20,000 resting ≥ 20,000 ✓) ≈ $227.51/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 7.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,753 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-rep` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,781 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~86.5% of ask side (5,341 resting ≥ 2,000 ✓) ≈ $5.40/day (pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | SELL | 8.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~86.2% of ask side (70,569 resting ≥ 2,000 ✓) ≈ $5.39/day (pool ÷ 2 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 9.0¢ | 75 | 0 | $25.00 | ✅ scoring — ~84.3% of ask side (208,377 resting ≥ 2,000 ✓) ≈ $5.27/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 90.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~82.4% of ask side (20,357 resting ≥ 2,000 ✓) ≈ $5.15/day (pool ÷ 2 markets) |
| `ewc-usp-party-2028-11-07-dem` | SELL | 64.0¢ | 114 | 0 | $1,000.00 | ✅ scoring — ~82.1% of ask side (20,001 resting ≥ 20,000 ✓) ≈ $205.15/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | SELL | 10.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~75.2% of ask side (131,080 resting ≥ 2,000 ✓) ≈ $4.70/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-dem` | SELL | 16.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~71.4% of ask side (134,005 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 23.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~69.7% of bid side (5,528 resting ≥ 5,000 ✓) ≈ $17.41/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-dem` | BUY | 3.0¢ | 200 | 0 | $25.00 | ✅ scoring — ~67.5% of bid side (9,824 resting ≥ 2,000 ✓) ≈ $4.22/day (pool ÷ 2 markets) |
| `ussewc-usse-nj-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (3,000 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nh-2026-11-03-rep` | BUY | 85.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~65.8% of bid side (2,118 resting ≥ 2,000 ✓) ≈ $4.11/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tn-2026-11-03-dem` | SELL | 10.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~62.0% of ask side (2,113 resting ≥ 2,000 ✓) ≈ $3.88/day (pool ÷ 2 markets) |
| …and 4556 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-uspres-nom-dem-2028-aleocc</code> BUY 5 @ 30¢ → $29.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 5 (5 yours) | ×0.2^0 = 5.3 |
|  | 3¢ | 108 | ×0.2^27 = 0.0 |
|  | 1¢ | 31,776 | ×0.2^29 = 0.0 |
| | | **Σ** | **5.3** |

`yours 5.3 / Σ 5.3 = 100.0%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 100.0% = $29.41/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 5 @ 28¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 49¢ | 25 | ×0.2^21 = 0.0 |
|  | 50¢ | 90 | ×0.2^22 = 0.0 |
|  | 56¢ | 56 | ×0.2^28 = 0.0 |
|  | 97¢ | 80,472 | ×0.2^69 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 8¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 20¢ | 25 | ×0.2^12 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 25 @ 28¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 38¢ | 25 | ×0.2^10 = 0.0 |
|  | 50¢ | 49 | ×0.2^22 = 0.0 |
|  | 97¢ | 80,459 | ×0.2^69 = 0.0 |
| | | **Σ** | **25.0** |

`yours 25.0 / Σ 25.0 = 100.0%`  
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
<details><summary><code>ussewc-usse-ks-2026-11-03-dem</code> BUY 50 @ 27¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 20¢ | 94 | ×0.1^7 = 0.0 |
|  | 19¢ | 250 | ×0.1^8 = 0.0 |
|  | 13¢ | 386 | ×0.1^14 = 0.0 |
|  | 3¢ | 25 | ×0.1^24 = 0.0 |
|  | 1¢ | 1,708 | ×0.1^26 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem` ← this one
2. `ussewc-usse-ks-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-rep</code> SELL 15 @ 90¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 15 (15 yours) | ×0.1^0 = 15.0 |
|  | 98¢ | 1,322 | ×0.1^8 = 0.0 |
|  | 99¢ | 1,144 | ×0.1^9 = 0.0 |
| | | **Σ** | **15.0** |

`yours 15.0 / Σ 15.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem`
2. `ussewc-usse-ms-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> BUY 4 @ 38¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 4 (4 yours) | ×0.2^0 = 4.0 |
|  | 34¢ | 0 | ×0.2^4 = 0.0 |
|  | 27¢ | 25 | ×0.2^11 = 0.0 |
|  | 3¢ | 2 | ×0.2^35 = 0.0 |
|  | 2¢ | 400,000 | ×0.2^36 = 0.0 |
| | | **Σ** | **4.0** |

`yours 4.0 / Σ 4.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205` ← this one
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-dem</code> SELL 23 @ 92¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 23 (23 yours) | ×0.1^0 = 23.0 |
|  | 99¢ | 5,097 | ×0.1^7 = 0.0 |
| | | **Σ** | **23.0** |

`yours 23.0 / Σ 23.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-mn-2026-11-03-rep`

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 25 @ 10¢ → $3.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 1¢ | 301,374 | ×0.2^9 = 0.2 |
| | | **Σ** | **25.2** |

`yours 25.0 / Σ 25.2 = 99.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.4% = $3.82/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt4500</code> BUY 10 @ 42¢ → $4.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 40¢ | 1 | ×0.25^2 = 0.1 |
|  | 31¢ | 126 | ×0.25^11 = 0.0 |
|  | 1¢ | 10,964 | ×0.25^41 = 0.0 |
| | | **Σ** | **10.1** |

`yours 10.0 / Σ 10.1 = 99.4%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 99.4% = $4.14/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500` ← this one
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 1 @ 17¢ → $3.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 12¢ | 21 | ×0.2^5 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^15 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.4% = $3.78/day`  

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
<details><summary><code>ussewc-usse-co-2026-11-03-dem</code> BUY 50 @ 92¢ → $5.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 91¢ | 25 | ×0.1^1 = 2.5 |
|  | 86¢ | 41 | ×0.1^6 = 0.0 |
|  | 51¢ | 72 | ×0.1^41 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^90 = 0.0 |
| | | **Σ** | **52.5** |

`yours 50.0 / Σ 52.5 = 95.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 95.2% = $5.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem` ← this one
2. `ussewc-usse-co-2026-11-03-rep`

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
|  | 14¢ | 10 | ×0.1^5 = 0.0 |
|  | 15¢ | 26 | ×0.1^6 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^89 = 0.0 |
| | | **Σ** | **12.0** |

`yours 11.0 / Σ 12.0 = 91.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 91.7% = $5.73/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem`
2. `usgubewc-usgub-mn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-party-2028-11-07-dem</code> BUY 20 @ 63¢ → $227.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 63¢ | 22 (20 yours) | ×0.2^0 = 22.2 |
|  | 48¢ | 34 | ×0.2^15 = 0.0 |
|  | 44¢ | 25 | ×0.2^19 = 0.0 |
|  | 39¢ | 100 | ×0.2^24 = 0.0 |
|  | 1¢ | 19,819 | ×0.2^62 = 0.0 |
| | | **Σ** | **22.2** |

`yours 20.2 / Σ 22.2 = 91.0%`  
`$1,000 ÷ 2 ÷ 2 = $250.00 × 91.0% = $227.51/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usp-party-2028-11-07-dem` ← this one
2. `ewc-usp-party-2028-11-07-rep`

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
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 96¢ → $5.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 98¢ | 107 | ×0.1^2 = 1.1 |
|  | 99¢ | 5,194 | ×0.1^3 = 5.2 |
| | | **Σ** | **46.3** |

`yours 40.0 / Σ 46.3 = 86.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 86.5% = $5.40/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> SELL 50 @ 8¢ → $5.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 58 (50 yours) | ×0.1^0 = 58.0 |
|  | 32¢ | 5,036 | ×0.1^24 = 0.0 |
| | | **Σ** | **58.0** |

`yours 50.0 / Σ 58.0 = 86.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 86.2% = $5.39/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 75 @ 9¢ → $5.27/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 89 (75 yours) | ×0.1^0 = 89.0 |
|  | 98¢ | 208,063 | ×0.1^89 = 0.0 |
| | | **Σ** | **89.0** |

`yours 75.0 / Σ 89.0 = 84.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 84.3% = $5.27/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> SELL 50 @ 90¢ → $5.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 91¢ | 107 | ×0.1^1 = 10.7 |
|  | 99¢ | 20,200 | ×0.1^9 = 0.0 |
| | | **Σ** | **60.7** |

`yours 50.0 / Σ 60.7 = 82.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 82.4% = $5.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-party-2028-11-07-dem</code> SELL 114 @ 64¢ → $205.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 64¢ | 139 (114 yours) | ×0.2^0 = 139.4 |
|  | 76¢ | 25 | ×0.2^12 = 0.0 |
|  | 99¢ | 19,836 | ×0.2^35 = 0.0 |
| | | **Σ** | **139.4** |

`yours 114.4 / Σ 139.4 = 82.1%`  
`$1,000 ÷ 2 ÷ 2 = $250.00 × 82.1% = $205.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usp-party-2028-11-07-dem` ← this one
2. `ewc-usp-party-2028-11-07-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> SELL 25 @ 10¢ → $4.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 30 (25 yours) | ×0.1^0 = 30.0 |
|  | 12¢ | 325 | ×0.1^2 = 3.3 |
|  | 98¢ | 130,500 | ×0.1^88 = 0.0 |
| | | **Σ** | **33.2** |

`yours 25.0 / Σ 33.2 = 75.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.2% = $4.70/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-dem</code> SELL 50 @ 16¢ → $4.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 17¢ | 198 | ×0.1^1 = 19.8 |
|  | 18¢ | 23 | ×0.1^2 = 0.2 |
|  | 21¢ | 37 | ×0.1^5 = 0.0 |
|  | 22¢ | 564 | ×0.1^6 = 0.0 |
|  | 23¢ | 57 | ×0.1^7 = 0.0 |
|  | 25¢ | 33 | ×0.1^9 = 0.0 |
|  | 98¢ | 132,818 | ×0.1^82 = 0.0 |
| | | **Σ** | **70.0** |

`yours 50.0 / Σ 70.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem` ← this one
2. `usgubewc-usgub-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 25 @ 23¢ → $17.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 23¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 21¢ | 272 | ×0.2^2 = 10.9 |
|  | 18¢ | 25 | ×0.2^5 = 0.0 |
|  | 17¢ | 6 | ×0.2^6 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^22 = 0.0 |
| | | **Σ** | **35.9** |

`yours 25.0 / Σ 35.9 = 69.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 69.7% = $17.41/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-dem</code> BUY 200 @ 3¢ → $4.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 200 (200 yours) | ×0.1^0 = 200.0 |
|  | 1¢ | 9,624 | ×0.1^2 = 96.2 |
| | | **Σ** | **296.2** |

`yours 200.0 / Σ 296.2 = 67.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 67.5% = $4.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem` ← this one
2. `ussewc-usse-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-nj-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,000 (2,000 yours) | ×0.1^0 = 3,000.0 |
| | | **Σ** | **3,000.0** |

`yours 2,000.0 / Σ 3,000.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nj-2026-11-03-dem`
2. `ussewc-usse-nj-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nh-2026-11-03-rep</code> BUY 25 @ 85¢ → $4.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 25 (25 yours) | ×0.1^0 = 25.0 |
|  | 84¢ | 130 | ×0.1^1 = 13.0 |
|  | 81¢ | 40 | ×0.1^4 = 0.0 |
|  | 77¢ | 37 | ×0.1^8 = 0.0 |
|  | 64¢ | 25 | ×0.1^21 = 0.0 |
|  | 1¢ | 1,861 | ×0.1^84 = 0.0 |
| | | **Σ** | **38.0** |

`yours 25.0 / Σ 38.0 = 65.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 65.8% = $4.11/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nh-2026-11-03-dem`
2. `usgubewc-usgub-nh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-dem</code> SELL 50 @ 10¢ → $3.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 79 (50 yours) | ×0.1^0 = 79.0 |
|  | 12¢ | 163 | ×0.1^2 = 1.6 |
|  | 99¢ | 1,871 | ×0.1^89 = 0.0 |
| | | **Σ** | **80.6** |

`yours 50.0 / Σ 80.6 = 62.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 62.0% = $3.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tn-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-nv-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (70,760 resting) | ~96.8% | ~$6.05 |
| `ewc-usmayor-losang-2026-11-03-karbas` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (204,591 resting) | ~47.0% | ~$2.94 |
| `ewc-usse-nc-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (54,309 resting) | ~9.6% | ~$2.41 |
| `ewc-usmayor-losang-2026-11-03-nitram` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (205,254 resting) | ~21.0% | ~$1.32 |
| `ewc-usgub-wi-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (351,606 resting) | ~16.7% | ~$1.05 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (79,721 resting) | ~16.0% | ~$1.00 |
| `ewc-usse-mi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (637,284 resting) | ~15.6% | ~$0.98 |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (565,093 resting) | ~13.6% | ~$0.85 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,735 resting) | ~1.0% | ~$0.77 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (17,561 resting) | ~1.5% | ~$0.74 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $300.00 ÷ 3 | 0.20 | 10,000 | SELL side (49,667 resting) | ~1.5% | ~$0.73 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (96,362 resting) | ~0.9% | ~$0.69 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $1,180.25 |
| Skipped | $1.41 |
| **Total earned** | **$3,069.69** |

2234 reward rows · 41 days with rewards · 486 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-12 ⚠️ multi-day pending bucket | $213.04 | `████████` |
| 2026-08-11 | $409.59 | `███████████████` |
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
| 2026-07-31 | $67.96 | `██` |
| 2026-07-30 | $20.67 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $1,606.37 | `████████████████████` |
| 2026-07 | $1,463.32 | `██████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $127.10 |
| `apdc-alito-2026-12-31` | $111.76 |
| `opdc-mcconnell-resign-2026-11-02` | $77.87 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $47.80 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $40.44 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.03 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `scc-senate-gop-2026-11-03-49` | $28.51 |
| `scc-senate-gop-2026-11-03-48` | $27.99 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-14 8:12 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 8:11 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 7:45 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 7:41 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 7:14 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 6:52 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 6:43 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 6:42 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 6:37 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 6:34 PM ET | ✅ ok | 2234 | $3069.69 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
