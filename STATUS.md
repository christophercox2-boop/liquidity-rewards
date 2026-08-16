# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-16 9:28 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$125.16/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — BUY at the best price, ~$15.04/day for 200 contracts. Runners-up: `ewc-usse-oh-2026-11-03-dem` (~$8.65/day), `ewc-usse-tx-2026-11-03-dem` (~$4.76/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$125.16/day (~$5.21/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-id-2026-11-03-rep` | BUY | 57.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,203 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 24.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (132,756 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-fl-2026-11-03-dem` | BUY | 23.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (50,302 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-rep` | SELL | 79.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,484 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-dem` | BUY | 17.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (5,302 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-or-2026-11-03-rep` | BUY | 28.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,502 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 59.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,303 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-rep` | BUY | 10.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,231 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-fl-2026-11-03-dem` | BUY | 28.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (10,281 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 55.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,204 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | BUY | 14.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~100.0% of bid side (70,591 resting ≥ 20,000 ✓) ≈ $29.41/day (pool ÷ 17 markets) |
| `usgubewc-usgub-ok-2026-11-03-rep` | BUY | 54.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.8% of bid side (600,204 resting ≥ 2,000 ✓) ≈ $6.24/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.2% of bid side (300,377 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `ussewc-usse-ar-2026-11-03-rep` | BUY | 57.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~90.9% of bid side (500,303 resting ≥ 2,000 ✓) ≈ $5.68/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 50.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (500,203 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-dem` | BUY | 45.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (600,204 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 50.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (500,203 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `usgubewc-usgub-sc-2026-11-03-rep` | BUY | 15.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (500,203 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-rep` | SELL | 93.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~45.5% of ask side (2,727 resting ≥ 2,000 ✓) ≈ $2.84/day (pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-rep` | BUY | 56.0¢ | 1 | 1 | $25.00 | ✅ scoring — ~9.1% of bid side (500,303 resting ≥ 2,000 ✓) ≈ $0.57/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-dem` | BUY | 18.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~5.9% of bid side (40,267 resting ≥ 2,000 ✓) ≈ $0.37/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jonoss` | BUY | 24.0¢ | 1 | 2 | $1,000.00 | ✅ scoring — ~3.4% of bid side (21,686 resting ≥ 20,000 ✓) ≈ $1.01/day (pool ÷ 17 markets) |
| `usgubewc-usgub-ma-2026-11-03-dem` | BUY | 3.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~3.0% of bid side (3,169 resting ≥ 2,000 ✓) ≈ $0.19/day (pool ÷ 2 markets) |
| `ussewc-usse-wv-2026-11-03-dem` | BUY | 2.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~0.2% of bid side (4,201 resting ≥ 2,000 ✓) ≈ $0.01/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 8.0¢ | 1 | 4 | $100.00 | ✅ scoring — ~0.2% of bid side (300,377 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 6.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~0.2% of bid side (415,450 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 12 markets) |
| `usgubewc-usgub-ok-2026-11-03-rep` | BUY | 51.0¢ | 1 | 3 | $25.00 | ✅ scoring — ~0.1% of bid side (600,204 resting ≥ 2,000 ✓) ≈ $0.01/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 54.0¢ | 1 | 1 | $25.00 | ✅ scoring — ~0.1% of bid side (500,604 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 47.0¢ | 1 | 3 | $25.00 | ✅ scoring — ~0.0% of bid side (500,203 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-sc-2026-11-03-rep` | BUY | 12.0¢ | 1 | 3 | $25.00 | ✅ scoring — ~0.0% of bid side (500,203 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 2 markets) |
| …and 53 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> BUY 1 @ 57¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 34¢ | 1 | ×0.1^23 = 0.0 |
|  | 16¢ | 1 | ×0.1^41 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^55 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 1 @ 24¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 92¢ | 30 | ×0.1^68 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^73 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-fl-2026-11-03-dem</code> BUY 1 @ 23¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 23¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 4¢ | 1 | ×0.1^19 = 0.0 |
|  | 2¢ | 50,000 | ×0.1^21 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem` ← this one
2. `ussewc-usse-fl-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-rep</code> SELL 1 @ 79¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 95¢ | 7 | ×0.1^16 = 0.0 |
|  | 96¢ | 276 | ×0.1^17 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^18 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem`
2. `ussewc-usse-ky-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-dem</code> BUY 1 @ 17¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 3¢ | 1 | ×0.1^14 = 0.0 |
|  | 1¢ | 5,300 | ×0.1^16 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem` ← this one
2. `ussewc-usse-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-or-2026-11-03-rep</code> BUY 1 @ 28¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 18¢ | 1 | ×0.1^10 = 0.0 |
|  | 2¢ | 115 | ×0.1^26 = 0.0 |
|  | 1¢ | 2,385 | ×0.1^27 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-or-2026-11-03-dem`
2. `usgubewc-usgub-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 1 @ 59¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 59¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 50¢ | 100 | ×0.1^9 = 0.0 |
|  | 49¢ | 1 | ×0.1^10 = 0.0 |
|  | 12¢ | 1 | ×0.1^47 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^57 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-rep</code> BUY 1 @ 10¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 2¢ | 30 | ×0.1^8 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^9 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem`
2. `usgubewc-usgub-ny-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-fl-2026-11-03-dem</code> BUY 1 @ 28¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 21¢ | 50 | ×0.1^7 = 0.0 |
|  | 20¢ | 30 | ×0.1^8 = 0.0 |
|  | 2¢ | 10,000 | ×0.1^26 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-fl-2026-11-03-dem` ← this one
2. `usgubewc-usgub-fl-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 1 @ 55¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 55¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 50¢ | 1 | ×0.1^5 = 0.0 |
|  | 37¢ | 2 | ×0.1^18 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^53 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> BUY 1 @ 14¢ → $29.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 3¢ | 30 | ×0.2^11 = 0.0 |
|  | 1¢ | 70,560 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 100.0% = $29.41/day`  

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
<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> BUY 1 @ 54¢ → $6.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 54¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 51¢ | 2 | ×0.1^3 = 0.0 |
|  | 38¢ | 1 | ×0.1^16 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^52 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.8% = $6.24/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem`
2. `usgubewc-usgub-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 1 @ 12¢ → $3.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 1 | ×0.2^4 = 0.0 |
|  | 4¢ | 1 | ×0.2^8 = 0.0 |
|  | 1¢ | 300,374 | ×0.2^11 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.2% = $3.82/day`  

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
<details><summary><code>ussewc-usse-ar-2026-11-03-rep</code> BUY 1 @ 57¢ → $5.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 56¢ | 1 | ×0.1^1 = 0.1 |
|  | 51¢ | 100 | ×0.1^6 = 0.0 |
|  | 50¢ | 1 | ×0.1^7 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^55 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 90.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.9% = $5.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem`
2. `ussewc-usse-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 1 @ 50¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 12¢ | 1 | ×0.1^38 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^48 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-co-2026-11-03-dem</code> BUY 1 @ 45¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 26¢ | 1 | ×0.1^19 = 0.0 |
|  | 10¢ | 1 | ×0.1^35 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^43 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem` ← this one
2. `usgubewc-usgub-co-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 1 @ 50¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 47¢ | 1 | ×0.1^3 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^48 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-sc-2026-11-03-rep</code> BUY 1 @ 15¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 12¢ | 1 | ×0.1^3 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^13 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sc-2026-11-03-dem`
2. `usgubewc-usgub-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-rep</code> SELL 1 @ 93¢ → $2.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 97¢ | 2,000 | ×0.1^4 = 0.2 |
| | | **Σ** | **2.2** |

`yours 1.0 / Σ 2.2 = 45.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 45.5% = $2.84/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem`
2. `ussewc-usse-ms-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-rep</code> BUY 1 @ 56¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 57¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 56¢ | 1 (1 yours) | ×0.1^1 = 0.1 |
|  | 51¢ | 100 | ×0.1^6 = 0.0 |
|  | 50¢ | 1 | ×0.1^7 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^55 = 0.0 |
| | | **Σ** | **1.1** |

`yours 0.1 / Σ 1.1 = 9.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 9.1% = $0.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem`
2. `ussewc-usse-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-dem</code> BUY 1 @ 18¢ → $0.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 17 (1 yours) | ×0.1^0 = 17.0 |
|  | 4¢ | 50 | ×0.1^14 = 0.0 |
|  | 1¢ | 40,200 | ×0.1^17 = 0.0 |
| | | **Σ** | **17.0** |

`yours 1.0 / Σ 17.0 = 5.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 5.9% = $0.37/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem` ← this one
2. `usgubewc-usgub-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jonoss</code> BUY 1 @ 24¢ → $1.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 26¢ | 1 | ×0.2^0 = 1.1 |
| ▶ | 24¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 15¢ | 34 | ×0.2^11 = 0.0 |
|  | 11¢ | 100 | ×0.2^15 = 0.0 |
|  | 10¢ | 21,250 | ×0.2^16 = 0.0 |
| | | **Σ** | **1.2** |

`yours 0.0 / Σ 1.2 = 3.4%`  
`$1,000 ÷ 17 ÷ 2 = $29.41 × 3.4% = $1.01/day`  

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
<details><summary><code>usgubewc-usgub-ma-2026-11-03-dem</code> BUY 1 @ 3¢ → $0.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 1¢ | 3,167 | ×0.1^2 = 31.7 |
| | | **Σ** | **33.7** |

`yours 1.0 / Σ 33.7 = 3.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 3.0% = $0.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wv-2026-11-03-dem</code> BUY 1 @ 2¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 1¢ | 4,200 | ×0.1^1 = 420.0 |
| | | **Σ** | **421.0** |

`yours 1.0 / Σ 421.0 = 0.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 0.2% = $0.01/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wv-2026-11-03-dem` ← this one
2. `ussewc-usse-wv-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 1 @ 8¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 8¢ | 1 (1 yours) | ×0.2^4 = 0.0 |
|  | 4¢ | 1 | ×0.2^8 = 0.0 |
|  | 1¢ | 300,374 | ×0.2^11 = 0.0 |
| | | **Σ** | **1.0** |

`yours 0.0 / Σ 1.0 = 0.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.2% = $0.01/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 1 @ 6¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 2¢ | 415,249 | ×0.2^4 = 664.4 |
| | | **Σ** | **665.4** |

`yours 1.0 / Σ 665.4 = 0.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.2% = $0.01/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225` ← this one
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-rep</code> BUY 1 @ 51¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 54¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 51¢ | 2 (1 yours) | ×0.1^3 = 0.0 |
|  | 38¢ | 1 | ×0.1^16 = 0.0 |
|  | 2¢ | 600,000 | ×0.1^52 = 0.0 |
| | | **Σ** | **1.0** |

`yours 0.0 / Σ 1.0 = 0.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 0.1% = $0.01/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem`
2. `usgubewc-usgub-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 1 @ 54¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 55¢ | 181 | ×0.1^0 = 181.0 |
| ▶ | 54¢ | 1 (1 yours) | ×0.1^1 = 0.1 |
|  | 49¢ | 222 | ×0.1^6 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^53 = 0.0 |
| | | **Σ** | **181.1** |

`yours 0.1 / Σ 181.1 = 0.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 0.1% = $0.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 1 @ 47¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 50¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 47¢ | 1 (1 yours) | ×0.1^3 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^48 = 0.0 |
| | | **Σ** | **2.0** |

`yours 0.0 / Σ 2.0 = 0.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 0.0% = $0.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-sc-2026-11-03-rep</code> BUY 1 @ 12¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 15¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 12¢ | 1 (1 yours) | ×0.1^3 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^13 = 0.0 |
| | | **Σ** | **2.0** |

`yours 0.0 / Σ 2.0 = 0.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 0.0% = $0.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sc-2026-11-03-dem`
2. `usgubewc-usgub-sc-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (201,184 resting) | ~20.1% | ~$15.04 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (595,436 resting) | ~34.6% | ~$8.65 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (553,610 resting) | ~6.3% | ~$4.76 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (11,014 resting) | ~69.2% | ~$4.32 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (71,747 resting) | ~5.0% | ~$3.74 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (610,048 resting) | ~4.2% | ~$3.16 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (74,086 resting) | ~3.5% | ~$2.64 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (11,515 resting) | ~8.5% | ~$2.12 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (555,104 resting) | ~7.0% | ~$1.75 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (3,184 resting) | ~39.7% | ~$1.65 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,401 resting) | ~1.9% | ~$1.44 |
| `ewc-usse-ak-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (302,077 resting) | ~22.1% | ~$1.38 |

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
| 2026-08-16 9:28 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:31 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:25 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:19 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:14 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:09 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:03 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 7:52 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 7:47 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 7:36 AM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
