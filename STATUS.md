# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-16 4:37 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$522.27/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-sc-2026-08-11-rep-darnor` — SELL at the best price, ~$3.99/day for 200 contracts. Runners-up: `ewc-usgub-nv-2026-11-03-rep` (~$2.99/day), `ewc-usse-nh-2026-11-03-rep` (~$2.22/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$522.27/day (~$21.76/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ushrp-fl19-2026-08-18-olahaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 7 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (92,067 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `usgubewc-usgub-me-2026-11-03-rep` | BUY | 30.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (30,362 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 90.0¢ | 28 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (20,332 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 20.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,798 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `ussewc-usse-fl-2026-11-03-dem` | BUY | 18.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (51,037 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-rep` | SELL | 89.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,727 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-or-2026-11-03-rep` | BUY | 18.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,280 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,509 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 15.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.9% of bid side (2,024 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-dem` | BUY | 8.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.9% of bid side (10,202 resting ≥ 2,000 ✓) ≈ $6.24/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 13.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~97.1% of bid side (300,406 resting ≥ 5,000 ✓) ≈ $3.74/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-rokha` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~96.4% of bid side (20,514 resting ≥ 20,000 ✓) ≈ $8.03/day (program pool ÷ 60 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 46.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~95.1% of bid side (50,333 resting ≥ 5,000 ✓) ≈ $3.66/day (pool ÷ 13 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~93.0% of ask side (130,768 resting ≥ 2,000 ✓) ≈ $5.81/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~90.8% of bid side (20,519 resting ≥ 20,000 ✓) ≈ $7.57/day (program pool ÷ 60 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | BUY | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.2% of bid side (2,458 resting ≥ 2,000 ✓) ≈ $5.64/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jamtal` | BUY | 18.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~89.4% of bid side (20,065 resting ≥ 20,000 ✓) ≈ $7.45/day (program pool ÷ 60 markets) |
| `usgubewc-usgub-co-2026-11-03-rep` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,781 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 7.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,753 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | SELL | 10.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~89.1% of ask side (265,913 resting ≥ 2,000 ✓) ≈ $5.57/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 18.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~88.5% of bid side (20,515 resting ≥ 20,000 ✓) ≈ $7.38/day (program pool ÷ 60 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 10.0¢ | 24 | 0 | $1,000.00 | ✅ scoring — ~88.4% of bid side (80,480 resting ≥ 20,000 ✓) ≈ $7.37/day (program pool ÷ 60 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~87.7% of ask side (2,026 resting ≥ 2,000 ✓) ≈ $5.48/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | SELL | 22.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~87.3% of ask side (65,501 resting ≥ 20,000 ✓) ≈ $7.27/day (program pool ÷ 60 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~86.4% of ask side (5,341 resting ≥ 2,000 ✓) ≈ $5.40/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-rokha` | BUY | 16.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~86.2% of bid side (20,463 resting ≥ 20,000 ✓) ≈ $7.18/day (program pool ÷ 60 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 9.0¢ | 75 | 0 | $25.00 | ✅ scoring — ~85.2% of ask side (208,376 resting ≥ 2,000 ✓) ≈ $5.33/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 14.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~84.6% of bid side (105,484 resting ≥ 5,000 ✓) ≈ $3.25/day (pool ÷ 13 markets) |
| `usgubewc-usgub-tn-2026-11-03-dem` | SELL | 10.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~83.8% of ask side (2,094 resting ≥ 2,000 ✓) ≈ $5.24/day (pool ÷ 2 markets) |
| …and 2765 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
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
<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> BUY 1 @ 30¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 22¢ | 1 | ×0.1^8 = 0.0 |
|  | 10¢ | 60 | ×0.1^20 = 0.0 |
|  | 1¢ | 30,300 | ×0.1^29 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem`
2. `usgubewc-usgub-me-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> SELL 28 @ 90¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 28 (28 yours) | ×0.1^0 = 27.9 |
|  | 99¢ | 20,304 | ×0.1^9 = 0.0 |
| | | **Σ** | **27.9** |

`yours 27.9 / Σ 27.9 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 5 @ 20¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 28¢ | 5 | ×0.2^8 = 0.0 |
|  | 50¢ | 115 | ×0.2^30 = 0.0 |
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
<details><summary><code>ussewc-usse-fl-2026-11-03-dem</code> BUY 1 @ 18¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 12¢ | 1 | ×0.1^6 = 0.0 |
|  | 10¢ | 310 | ×0.1^8 = 0.0 |
|  | 6¢ | 325 | ×0.1^12 = 0.0 |
|  | 5¢ | 100 | ×0.1^13 = 0.0 |
|  | 2¢ | 50,000 | ×0.1^16 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem` ← this one
2. `ussewc-usse-fl-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-rep</code> SELL 1 @ 89¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 94¢ | 1 | ×0.1^5 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^8 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem`
2. `ussewc-usse-ms-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-or-2026-11-03-rep</code> BUY 1 @ 18¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 14¢ | 1 | ×0.1^4 = 0.0 |
|  | 10¢ | 1 | ×0.1^8 = 0.0 |
|  | 9¢ | 1 | ×0.1^9 = 0.0 |
|  | 3¢ | 109 | ×0.1^15 = 0.0 |
|  | 1¢ | 2,167 | ×0.1^17 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-or-2026-11-03-dem`
2. `usgubewc-usgub-or-2026-11-03-rep` ← this one

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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 1 @ 15¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 11¢ | 5 | ×0.1^4 = 0.0 |
|  | 9¢ | 27 | ×0.1^6 = 0.0 |
|  | 5¢ | 30 | ×0.1^10 = 0.0 |
|  | 1¢ | 1,961 | ×0.1^14 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.9% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-dem</code> BUY 1 @ 8¢ → $6.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 2¢ | 1 | ×0.1^6 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^7 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.9% = $6.24/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem` ← this one
2. `ussewc-usse-tn-2026-11-03-rep`

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
<details><summary><code>enwc-uspres-nom-dem-2028-rokha</code> BUY 60 @ 10¢ → $8.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 62 (60 yours) | ×0.2^0 = 62.2 |
|  | 4¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^9 = 0.0 |
| | | **Σ** | **62.2** |

`yours 60.0 / Σ 62.2 = 96.4%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 96.4% = $8.03/day`  

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
15. `enwc-uspres-nom-dem-2028-rokha` ← this one
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 1 @ 46¢ → $3.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 45¢ | 0 | ×0.2^1 = 0.0 |
|  | 40¢ | 0 | ×0.2^6 = 0.0 |
|  | 25¢ | 1 | ×0.2^21 = 0.0 |
|  | 21¢ | 1 | ×0.2^25 = 0.0 |
|  | 19¢ | 25 | ×0.2^27 = 0.0 |
|  | 2¢ | 50,105 | ×0.2^44 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 95.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 95.1% = $3.66/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 60 @ 10¢ → $7.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 66 (60 yours) | ×0.2^0 = 66.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^9 = 0.0 |
| | | **Σ** | **66.1** |

`yours 60.0 / Σ 66.1 = 90.8%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 90.8% = $7.57/day`  

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
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> BUY 1 @ 7¢ → $5.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 6¢ | 1 | ×0.1^1 = 0.1 |
|  | 3¢ | 58 | ×0.1^4 = 0.0 |
|  | 1¢ | 2,398 | ×0.1^6 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.2% = $5.64/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jamtal</code> BUY 1 @ 18¢ → $7.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 15¢ | 1 | ×0.2^3 = 0.0 |
|  | 13¢ | 2 | ×0.2^5 = 0.0 |
|  | 12¢ | 2 | ×0.2^6 = 0.0 |
|  | 11¢ | 1 | ×0.2^7 = 0.0 |
|  | 10¢ | 60 | ×0.2^8 = 0.0 |
|  | 6¢ | 2 | ×0.2^12 = 0.0 |
|  | 5¢ | 1 | ×0.2^13 = 0.0 |
|  | 4¢ | 2 | ×0.2^14 = 0.0 |
|  | 3¢ | 1 | ×0.2^15 = 0.0 |
| | … | +1 levels | 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 89.4%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 89.4% = $7.45/day`  

<details><summary>÷ 60 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 18¢ → $7.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 15¢ | 1 | ×0.2^3 = 0.0 |
|  | 14¢ | 1 | ×0.2^4 = 0.0 |
|  | 10¢ | 60 | ×0.2^8 = 0.0 |
|  | 6¢ | 1 | ×0.2^12 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^17 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.5%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 88.5% = $7.38/day`  

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 24 @ 10¢ → $7.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 27 (24 yours) | ×0.2^0 = 26.7 |
|  | 9¢ | 2 | ×0.2^1 = 0.4 |
|  | 1¢ | 80,451 | ×0.2^9 = 0.0 |
| | | **Σ** | **27.1** |

`yours 24.0 / Σ 27.1 = 88.4%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 88.4% = $7.37/day`  

<details><summary>÷ 60 markets in this race (27 known) — tap to list</summary>

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
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 96¢ → $5.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 98¢ | 108 | ×0.1^2 = 1.1 |
|  | 99¢ | 5,193 | ×0.1^3 = 5.2 |
| | | **Σ** | **46.3** |

`yours 40.0 / Σ 46.3 = 86.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 86.4% = $5.40/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-rokha</code> BUY 1 @ 16¢ → $7.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 14¢ | 1 | ×0.2^2 = 0.0 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 10¢ | 2 | ×0.2^6 = 0.0 |
|  | 8¢ | 1 | ×0.2^8 = 0.0 |
|  | 7¢ | 2 | ×0.2^9 = 0.0 |
|  | 6¢ | 1 | ×0.2^10 = 0.0 |
|  | 5¢ | 1 | ×0.2^11 = 0.0 |
|  | 3¢ | 2 | ×0.2^13 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^15 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 86.2%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 86.2% = $7.18/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 1 @ 14¢ → $3.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 11¢ | 2 | ×0.2^3 = 0.0 |
|  | 10¢ | 60 | ×0.2^4 = 0.1 |
|  | 1¢ | 105,420 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 84.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 84.6% = $3.25/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47` ← this one
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
<details><summary><code>usgubewc-usgub-tn-2026-11-03-dem</code> SELL 50 @ 10¢ → $5.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 58 (50 yours) | ×0.1^0 = 58.0 |
|  | 12¢ | 165 | ×0.1^2 = 1.7 |
|  | 99¢ | 1,871 | ×0.1^89 = 0.0 |
| | | **Σ** | **59.6** |

`yours 50.0 / Σ 59.6 = 83.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.8% = $5.24/day`  

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
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (263,844 resting) | ~63.9% | ~$3.99 |
| `ewc-usgub-nv-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (70,609 resting) | ~47.9% | ~$2.99 |
| `ewc-usse-nh-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (48,214 resting) | ~35.5% | ~$2.22 |
| `ewc-usmayor-losang-2026-11-03-karbas` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (204,914 resting) | ~33.2% | ~$2.08 |
| `ewc-usmayor-losang-2026-11-03-nitram` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (205,040 resting) | ~26.3% | ~$1.64 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (72,152 resting) | ~23.7% | ~$1.48 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (73,193 resting) | ~30.6% | ~$1.27 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (51,397 resting) | ~15.6% | ~$0.98 |
| `ewc-usse-mi-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (629,696 resting) | ~14.5% | ~$0.91 |
| `ewc-usgub-wi-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (1,240,222 resting) | ~13.9% | ~$0.87 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (61,695 resting) | ~1.1% | ~$0.81 |
| `ewc-usgub-mi-2026-11-03-dem` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (55,118 resting) | ~19.0% | ~$0.79 |

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
| 2026-08-16 4:37 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 3:36 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 2:35 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 1:35 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 1:26 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 1:17 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 1:12 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 1:09 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 1:04 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 12:51 AM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
