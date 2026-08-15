# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-15 2:27 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$1,254.36/day estimated (ceiling, not promise — details below)

**Earned:** $3,292.94 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-13: **$223.24** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-12: **$213.04** · 2026-08-11: **$409.60** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-08-31` — SELL at the best price, ~$4.04/day for 200 contracts. Runners-up: `ewc-usgub-nv-2026-11-03-rep` (~$2.62/day), `ewc-usmayor-losang-2026-11-03-karbas` (~$2.29/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$1,254.36/day (~$52.26/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-49` | SELL | 24.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,734 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 15.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (198,015 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 41.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (82,402 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 20.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,823 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-markel` | SELL | 25.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~98.8% of ask side (44,252 resting ≥ 20,000 ✓) ≈ $29.05/day (pool ÷ 17 markets) |
| `usgubewc-usgub-mn-2026-11-03-rep` | SELL | 9.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~91.7% of ask side (196,098 resting ≥ 2,000 ✓) ≈ $5.73/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 16.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~90.9% of bid side (90,203 resting ≥ 20,000 ✓) ≈ $26.74/day (pool ÷ 17 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | SELL | 96.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~90.8% of ask side (3,587 resting ≥ 2,000 ✓) ≈ $5.67/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-gleyou` | BUY | 6.0¢ | 2,000 | 0 | $1,000.00 | ✅ scoring — ~90.6% of bid side (37,641 resting ≥ 20,000 ✓) ≈ $16.78/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 19.0¢ | 22 | 0 | $1,000.00 | ✅ scoring — ~90.6% of bid side (41,413 resting ≥ 20,000 ✓) ≈ $26.65/day (pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-thomas` | BUY | 15.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~90.1% of bid side (40,476 resting ≥ 20,000 ✓) ≈ $16.68/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jamtal` | BUY | 11.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~89.6% of bid side (40,478 resting ≥ 20,000 ✓) ≈ $16.59/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 10.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~88.8% of bid side (70,025 resting ≥ 20,000 ✓) ≈ $16.44/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-kamhar` | BUY | 14.0¢ | 5 | 1 | $1,000.00 | ✅ scoring — ~88.6% of bid side (40,735 resting ≥ 20,000 ✓) ≈ $26.04/day (pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 10.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~88.4% of bid side (70,453 resting ≥ 20,000 ✓) ≈ $16.36/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | SELL | 25.0¢ | 51 | 0 | $1,000.00 | ✅ scoring — ~86.6% of ask side (44,128 resting ≥ 20,000 ✓) ≈ $25.46/day (pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-marrub` | SELL | 44.0¢ | 50 | 0 | $1,000.00 | ✅ scoring — ~85.5% of ask side (53,905 resting ≥ 20,000 ✓) ≈ $30.54/day (pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-stasmi` | BUY | 9.0¢ | 3 | 0 | $1,000.00 | ✅ scoring — ~85.2% of bid side (70,454 resting ≥ 20,000 ✓) ≈ $15.78/day (pool ÷ 27 markets) |
| `ussewc-usse-tn-2026-11-03-dem` | SELL | 9.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~84.7% of ask side (527,395 resting ≥ 2,000 ✓) ≈ $5.30/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-dem` | SELL | 12.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (203,574 resting ≥ 2,000 ✓) ≈ $5.21/day (pool ÷ 2 markets) |
| `usgubewc-usgub-vt-2026-11-03-dem` | SELL | 15.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (330,178 resting ≥ 2,000 ✓) ≈ $5.21/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-micoba` | BUY | 9.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~83.1% of bid side (70,453 resting ≥ 20,000 ✓) ≈ $15.39/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rokha` | BUY | 9.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~83.1% of bid side (70,453 resting ≥ 20,000 ✓) ≈ $15.39/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 25.0¢ | 53 | 0 | $1,000.00 | ✅ scoring — ~82.8% of ask side (43,361 resting ≥ 20,000 ✓) ≈ $24.37/day (pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 9.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~82.8% of bid side (74,453 resting ≥ 20,000 ✓) ≈ $15.33/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rondes` | BUY | 8.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~73.8% of bid side (40,453 resting ≥ 20,000 ✓) ≈ $13.67/day (pool ÷ 27 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~71.1% of ask side (5,351 resting ≥ 2,000 ✓) ≈ $4.44/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-rep` | SELL | 90.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~68.2% of ask side (2,477 resting ≥ 2,000 ✓) ≈ $4.26/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-dem` | SELL | 92.0¢ | 23 | 0 | $25.00 | ✅ scoring — ~67.6% of ask side (5,131 resting ≥ 2,000 ✓) ≈ $4.23/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | SELL | 92.0¢ | 27 | 0 | $25.00 | ✅ scoring — ~67.5% of ask side (2,514 resting ≥ 2,000 ✓) ≈ $4.22/day (pool ÷ 2 markets) |
| …and 2992 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 25 @ 24¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 50¢ | 49 | ×0.2^26 = 0.0 |
|  | 97¢ | 80,459 | ×0.2^73 = 0.0 |
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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 10 @ 15¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 22¢ | 30 | ×0.1^7 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^82 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 5 @ 41¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 41¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 52¢ | 125 | ×0.2^11 = 0.0 |
|  | 59¢ | 0 | ×0.2^18 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^57 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 5 @ 20¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 28¢ | 5 | ×0.2^8 = 0.0 |
|  | 50¢ | 140 | ×0.2^30 = 0.0 |
|  | 76¢ | 0 | ×0.2^56 = 0.0 |
|  | 78¢ | 0 | ×0.2^58 = 0.0 |
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
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> SELL 1 @ 25¢ → $29.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 34¢ | 24,051 | ×0.2^9 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.8%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 98.8% = $29.05/day`  

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
<details><summary><code>usgubewc-usgub-mn-2026-11-03-rep</code> SELL 11 @ 9¢ → $5.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 12 (11 yours) | ×0.1^0 = 12.0 |
|  | 14¢ | 10 | ×0.1^5 = 0.0 |
|  | 15¢ | 101 | ×0.1^6 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^89 = 0.0 |
| | | **Σ** | **12.0** |

`yours 11.0 / Σ 12.0 = 91.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 91.7% = $5.73/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem`
2. `usgubewc-usgub-mn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 2 @ 16¢ → $26.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 2 (2 yours) | ×0.2^0 = 2.2 |
|  | 1¢ | 90,201 | ×0.2^15 = 0.0 |
| | | **Σ** | **2.2** |

`yours 2.0 / Σ 2.2 = 90.9%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 90.9% = $26.74/day`  

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
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> SELL 35 @ 96¢ → $5.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 35 (35 yours) | ×0.1^0 = 35.0 |
|  | 99¢ | 3,552 | ×0.1^3 = 3.6 |
| | | **Σ** | **38.6** |

`yours 35.0 / Σ 38.6 = 90.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.8% = $5.67/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-gleyou</code> BUY 2,000 @ 6¢ → $16.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 2,167 (2,000 yours) | ×0.2^0 = 2,166.7 |
|  | 2¢ | 25,000 | ×0.2^4 = 40.0 |
| | | **Σ** | **2,206.7** |

`yours 2,000.0 / Σ 2,206.7 = 90.6%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 90.6% = $16.78/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 22 @ 19¢ → $26.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 24 (22 yours) | ×0.2^0 = 24.2 |
|  | 15¢ | 34 | ×0.2^4 = 0.1 |
|  | 11¢ | 100 | ×0.2^8 = 0.0 |
|  | 10¢ | 21,000 | ×0.2^9 = 0.0 |
| | | **Σ** | **24.3** |

`yours 22.0 / Σ 24.3 = 90.6%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 90.6% = $26.65/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-thomas</code> BUY 2 @ 15¢ → $16.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 2 (2 yours) | ×0.2^0 = 2.2 |
|  | 1¢ | 40,474 | ×0.2^14 = 0.0 |
| | | **Σ** | **2.2** |

`yours 2.0 / Σ 2.2 = 90.1%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 90.1% = $16.68/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jamtal</code> BUY 2 @ 11¢ → $16.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 2 (2 yours) | ×0.2^0 = 2.2 |
|  | 1¢ | 40,476 | ×0.2^10 = 0.0 |
| | | **Σ** | **2.3** |

`yours 2.0 / Σ 2.3 = 89.6%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 89.6% = $16.59/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 2 @ 10¢ → $16.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 2 (2 yours) | ×0.2^0 = 2.2 |
|  | 1¢ | 70,023 | ×0.2^9 = 0.0 |
| | | **Σ** | **2.3** |

`yours 2.0 / Σ 2.3 = 88.8%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 88.8% = $16.44/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-kamhar</code> BUY 5 @ 14¢ → $26.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 15¢ | 0 | ×0.2^0 = 0.1 |
| ▶ | 14¢ | 5 (5 yours) | ×0.2^1 = 1.0 |
|  | 10¢ | 29 | ×0.2^5 = 0.0 |
|  | 2¢ | 500 | ×0.2^13 = 0.0 |
|  | 1¢ | 40,201 | ×0.2^14 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.6%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 88.6% = $26.04/day`  

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
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 2 @ 10¢ → $16.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 2 (2 yours) | ×0.2^0 = 2.2 |
|  | 1¢ | 70,451 | ×0.2^9 = 0.0 |
| | | **Σ** | **2.3** |

`yours 2.0 / Σ 2.3 = 88.4%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 88.4% = $16.36/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> SELL 51 @ 25¢ → $25.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 51 (51 yours) | ×0.2^0 = 51.0 |
|  | 28¢ | 33 | ×0.2^3 = 0.3 |
|  | 30¢ | 23,878 | ×0.2^5 = 7.6 |
| | | **Σ** | **58.9** |

`yours 51.0 / Σ 58.9 = 86.6%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 86.6% = $25.46/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-marrub</code> SELL 50 @ 44¢ → $30.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 44¢ | 56 (50 yours) | ×0.2^0 = 56.0 |
|  | 45¢ | 12 | ×0.2^1 = 2.4 |
|  | 51¢ | 1,000 | ×0.2^7 = 0.0 |
|  | 52¢ | 21,021 | ×0.2^8 = 0.1 |
| | | **Σ** | **58.5** |

`yours 50.0 / Σ 58.5 = 85.5%`  
`$1,000 ÷ 14 ÷ 2 = $35.71 × 85.5% = $30.54/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub` ← this one
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-stasmi</code> BUY 3 @ 9¢ → $15.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 3 (3 yours) | ×0.2^0 = 3.3 |
|  | 1¢ | 70,451 | ×0.2^8 = 0.2 |
| | | **Σ** | **3.5** |

`yours 3.0 / Σ 3.5 = 85.2%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 85.2% = $15.78/day`  

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
22. `ewc-usp-2028-11-07-stasmi` ← this one
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-dem</code> SELL 50 @ 9¢ → $5.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 59 (50 yours) | ×0.1^0 = 59.0 |
|  | 98¢ | 132,784 | ×0.1^89 = 0.0 |
| | | **Σ** | **59.0** |

`yours 50.0 / Σ 59.0 = 84.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 84.7% = $5.30/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem` ← this one
2. `ussewc-usse-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-dem</code> SELL 20 @ 12¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 24 (20 yours) | ×0.1^0 = 24.0 |
|  | 98¢ | 203,325 | ×0.1^86 = 0.0 |
| | | **Σ** | **24.0** |

`yours 20.0 / Σ 24.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem` ← this one
2. `ussewc-usse-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-vt-2026-11-03-dem</code> SELL 5 @ 15¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 6 (5 yours) | ×0.1^0 = 6.0 |
|  | 98¢ | 132,784 | ×0.1^83 = 0.0 |
| | | **Σ** | **6.0** |

`yours 5.0 / Σ 6.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-vt-2026-11-03-dem` ← this one
2. `usgubewc-usgub-vt-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-micoba</code> BUY 2 @ 9¢ → $15.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2 (2 yours) | ×0.2^0 = 2.2 |
|  | 1¢ | 70,451 | ×0.2^8 = 0.2 |
| | | **Σ** | **2.4** |

`yours 2.0 / Σ 2.4 = 83.1%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 83.1% = $15.39/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rokha</code> BUY 2 @ 9¢ → $15.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2 (2 yours) | ×0.2^0 = 2.2 |
|  | 1¢ | 70,451 | ×0.2^8 = 0.2 |
| | | **Σ** | **2.4** |

`yours 2.0 / Σ 2.4 = 83.1%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 83.1% = $15.39/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> SELL 53 @ 25¢ → $24.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 53 (53 yours) | ×0.2^0 = 53.0 |
|  | 30¢ | 34,286 | ×0.2^5 = 11.0 |
| | | **Σ** | **64.0** |

`yours 53.0 / Σ 64.0 = 82.8%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 82.8% = $24.37/day`  

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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 2 @ 9¢ → $15.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2 (2 yours) | ×0.2^0 = 2.2 |
|  | 1¢ | 74,451 | ×0.2^8 = 0.2 |
| | | **Σ** | **2.4** |

`yours 2.0 / Σ 2.4 = 82.8%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 82.8% = $15.33/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 2 @ 8¢ → $13.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (2 yours) | ×0.2^0 = 2.5 |
|  | 1¢ | 40,451 | ×0.2^7 = 0.5 |
| | | **Σ** | **3.0** |

`yours 2.2 / Σ 3.0 = 73.8%`  
`$1,000 ÷ 27 ÷ 2 = $18.52 × 73.8% = $13.67/day`  

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
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 96¢ → $4.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 98¢ | 106 | ×0.1^2 = 1.1 |
|  | 99¢ | 5,195 | ×0.1^3 = 5.2 |
| | | **Σ** | **56.3** |

`yours 40.0 / Σ 56.3 = 71.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.1% = $4.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-rep</code> SELL 15 @ 90¢ → $4.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 22 (15 yours) | ×0.1^0 = 22.0 |
|  | 98¢ | 1,319 | ×0.1^8 = 0.0 |
|  | 99¢ | 1,136 | ×0.1^9 = 0.0 |
| | | **Σ** | **22.0** |

`yours 15.0 / Σ 22.0 = 68.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 68.2% = $4.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem`
2. `ussewc-usse-ms-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-dem</code> SELL 23 @ 92¢ → $4.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 34 (23 yours) | ×0.1^0 = 34.0 |
|  | 99¢ | 5,097 | ×0.1^7 = 0.0 |
| | | **Σ** | **34.0** |

`yours 23.0 / Σ 34.0 = 67.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 67.6% = $4.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-mn-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> SELL 27 @ 92¢ → $4.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 40 (27 yours) | ×0.1^0 = 40.0 |
|  | 99¢ | 2,474 | ×0.1^7 = 0.0 |
| | | **Σ** | **40.0** |

`yours 27.0 / Σ 40.0 = 67.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 67.5% = $4.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,428 resting) | ~16.2% | ~$4.04 |
| `ewc-usgub-nv-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (80,989 resting) | ~42.0% | ~$2.62 |
| `ewc-usmayor-losang-2026-11-03-karbas` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (204,399 resting) | ~36.6% | ~$2.29 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (690,826 resting) | ~8.2% | ~$2.05 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (92,471 resting) | ~23.5% | ~$1.47 |
| `ewc-usmayor-losang-2026-11-03-nitram` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (205,199 resting) | ~22.3% | ~$1.40 |
| `ewc-usse-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (79,814 resting) | ~16.9% | ~$1.06 |
| `ewc-usse-nh-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (61,723 resting) | ~16.3% | ~$1.02 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (61,258 resting) | ~1.1% | ~$0.83 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (64,979 resting) | ~12.4% | ~$0.78 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $300.00 ÷ 3 | 0.20 | 10,000 | SELL side (48,955 resting) | ~1.5% | ~$0.77 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,240,235 resting) | ~12.2% | ~$0.76 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $1,403.50 |
| Skipped | $1.41 |
| **Total earned** | **$3,292.94** |

2381 reward rows · 42 days with rewards · 489 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-13 ⚠️ multi-day pending bucket | $223.24 | `████████` |
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
| 2026-07-31 | $67.96 | `██` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $1,829.62 | `████████████████████` |
| 2026-07 | $1,463.32 | `████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $141.45 |
| `apdc-alito-2026-12-31` | $114.18 |
| `opdc-mcconnell-resign-2026-11-02` | $78.63 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $52.60 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $43.44 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.00 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.04 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `scc-senate-gop-2026-11-03-49` | $31.97 |
| `scc-senate-gop-2026-11-03-52` | $30.11 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-15 2:27 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 2:11 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 1:10 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 12:45 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 12:10 PM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 11:09 AM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 10:09 AM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 9:46 AM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 9:02 AM ET | ✅ ok | 2381 | $3292.94 |
| 2026-08-15 8:16 AM ET | ✅ ok | 2381 | $3292.94 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
