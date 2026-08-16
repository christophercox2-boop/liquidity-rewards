# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-16 8:14 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/liquidity-rewards/actions/workflows/liquidity-rewards.yml).

> ⚠️ **2028-slate pool scope is UNRESOLVED — estimates shown CONSERVATIVELY (program-wide, ~$8.33/side/day).** The exchange's program sheet says 'Daily (per event)' ($1,000 per event, ~4x more), but Aug-14 actuals fit program-wide almost exactly. If the docs are right, the gap means bait-anchored touches are collecting pools this tracker credits to us. Both readings are logged (family_day.csv); the Aug-15 payout — predictions 4x apart — decides.

## 📌 Summary

**Earning right now:** ~$364.65/day estimated (ceiling, not promise — details below)

**Earned:** $3,567.53 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-14: **$274.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-13: **$223.24** · 2026-08-12: **$213.04** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-sc-2026-08-11-rep-darnor` — SELL at the best price, ~$6.10/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-08-31` (~$4.06/day), `ewc-usse-oh-2026-11-03-dem` (~$3.48/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$364.65/day (~$15.19/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ussewc-usse-ky-2026-11-03-rep` | SELL | 85.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,509 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 40.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,417 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 90.0¢ | 28 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (20,332 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-pa-2026-11-03-dem` | BUY | 59.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,503 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 41.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (82,377 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 9.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (5,354 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-rep` | BUY | 60.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (30,364 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-fl-2026-11-03-dem` | BUY | 15.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.9% of bid side (50,462 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-or-2026-11-03-rep` | BUY | 20.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.0% of bid side (2,406 resting ≥ 2,000 ✓) ≈ $6.19/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~98.8% of bid side (2,025 resting ≥ 2,000 ✓) ≈ $1.76/day (pool ÷ 7 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 13.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~97.1% of bid side (300,506 resting ≥ 5,000 ✓) ≈ $3.74/day (pool ÷ 13 markets) |
| `ussewc-usse-fl-2026-11-03-dem` | SELL | 21.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~92.6% of ask side (133,036 resting ≥ 2,000 ✓) ≈ $5.79/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 10.0¢ | 60 | 1 | $1,000.00 | ✅ scoring — ~88.4% of bid side (20,540 resting ≥ 20,000 ✓) ≈ $7.37/day (program pool ÷ 60 markets) |
| `ewc-usp-2028-11-07-andbes` | BUY | 10.0¢ | 24 | 0 | $1,000.00 | ✅ scoring — ~88.4% of bid side (80,580 resting ≥ 20,000 ✓) ≈ $7.37/day (program pool ÷ 60 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~87.7% of ask side (2,126 resting ≥ 2,000 ✓) ≈ $5.48/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | BUY | 11.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~86.9% of bid side (110,562 resting ≥ 20,000 ✓) ≈ $7.24/day (program pool ÷ 60 markets) |
| `ewc-usp-2028-11-07-stasmi` | BUY | 10.0¢ | 60 | 0 | $1,000.00 | ✅ scoring — ~85.2% of bid side (20,526 resting ≥ 20,000 ✓) ≈ $7.10/day (program pool ÷ 60 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 9.0¢ | 75 | 0 | $25.00 | ✅ scoring — ~82.4% of ask side (208,479 resting ≥ 2,000 ✓) ≈ $5.15/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~77.7% of ask side (7,758 resting ≥ 2,000 ✓) ≈ $4.85/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 7.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~73.9% of bid side (90,502 resting ≥ 5,000 ✓) ≈ $2.84/day (pool ÷ 13 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | SELL | 10.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~73.9% of ask side (266,029 resting ≥ 2,000 ✓) ≈ $4.62/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-rep` | SELL | 88.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~73.4% of ask side (2,184 resting ≥ 2,000 ✓) ≈ $4.59/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jamtal` | BUY | 18.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~71.9% of bid side (20,090 resting ≥ 20,000 ✓) ≈ $5.99/day (program pool ÷ 60 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 18.0¢ | 1 | 0 | $1,000.00 | ✅ scoring — ~71.6% of bid side (20,578 resting ≥ 20,000 ✓) ≈ $5.97/day (program pool ÷ 60 markets) |
| `ussewc-usse-co-2026-11-03-rep` | BUY | 10.0¢ | 60 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,601 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (92,092 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 14.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~63.9% of bid side (105,645 resting ≥ 5,000 ✓) ≈ $2.46/day (pool ÷ 13 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 42.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~58.6% of bid side (11,087 resting ≥ 10,000 ✓) ≈ $2.44/day (pool ÷ 6 markets) |
| `ewc-usp-2028-11-07-jossha` | BUY | 9.0¢ | 2 | 0 | $1,000.00 | ✅ scoring — ~56.7% of bid side (114,558 resting ≥ 20,000 ✓) ≈ $4.72/day (program pool ÷ 60 markets) |
| `ussewc-usse-tn-2026-11-03-dem` | BUY | 8.0¢ | 75 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (10,374 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| …and 2814 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ussewc-usse-ky-2026-11-03-rep</code> SELL 1 @ 85¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 95¢ | 33 | ×0.1^10 = 0.0 |
|  | 96¢ | 250 | ×0.1^11 = 0.0 |
|  | 97¢ | 2,000 | ×0.1^12 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem`
2. `ussewc-usse-ky-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 1 @ 40¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 32¢ | 1 | ×0.1^8 = 0.0 |
|  | 21¢ | 1 | ×0.1^19 = 0.0 |
|  | 17¢ | 1 | ×0.1^23 = 0.0 |
|  | 14¢ | 17 | ×0.1^26 = 0.0 |
|  | 11¢ | 1 | ×0.1^29 = 0.0 |
|  | 1¢ | 2,395 | ×0.1^39 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-pa-2026-11-03-dem</code> BUY 1 @ 59¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 59¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 53¢ | 1 | ×0.1^6 = 0.0 |
|  | 49¢ | 101 | ×0.1^10 = 0.0 |
|  | 7¢ | 1 | ×0.1^52 = 0.0 |
|  | 1¢ | 2,399 | ×0.1^58 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem` ← this one
2. `usgubewc-usgub-pa-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 5 @ 41¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 41¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 50¢ | 100 | ×0.2^9 = 0.0 |
|  | 60¢ | 0 | ×0.2^19 = 0.0 |
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
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> BUY 1 @ 9¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 3¢ | 1 | ×0.1^6 = 0.0 |
|  | 2¢ | 81 | ×0.1^7 = 0.0 |
|  | 1¢ | 5,271 | ×0.1^8 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> BUY 1 @ 60¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 56¢ | 1 | ×0.1^4 = 0.0 |
|  | 48¢ | 1 | ×0.1^12 = 0.0 |
|  | 32¢ | 1 | ×0.1^28 = 0.0 |
|  | 10¢ | 60 | ×0.1^50 = 0.0 |
|  | 1¢ | 30,300 | ×0.1^59 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem`
2. `usgubewc-usgub-me-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-fl-2026-11-03-dem</code> BUY 1 @ 15¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 11¢ | 1 | ×0.1^4 = 0.0 |
|  | 10¢ | 60 | ×0.1^5 = 0.0 |
|  | 5¢ | 100 | ×0.1^10 = 0.0 |
|  | 2¢ | 50,000 | ×0.1^13 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.9% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem` ← this one
2. `ussewc-usse-fl-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-or-2026-11-03-rep</code> BUY 1 @ 20¢ → $6.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 18¢ | 1 | ×0.1^2 = 0.0 |
|  | 14¢ | 1 | ×0.1^6 = 0.0 |
|  | 11¢ | 1 | ×0.1^9 = 0.0 |
|  | 10¢ | 120 | ×0.1^10 = 0.0 |
|  | 5¢ | 115 | ×0.1^15 = 0.0 |
|  | 1¢ | 2,167 | ×0.1^19 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.0% = $6.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-or-2026-11-03-dem`
2. `usgubewc-usgub-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> BUY 2,000 @ 1¢ → $1.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,025 (2,000 yours) | ×0.1^0 = 2,025.0 |
| | | **Σ** | **2,025.0** |

`yours 2,000.0 / Σ 2,025.0 = 98.8%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 98.8% = $1.76/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 7 @ 13¢ → $3.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 7 (7 yours) | ×0.2^0 = 6.8 |
|  | 10¢ | 25 | ×0.2^3 = 0.2 |
|  | 1¢ | 300,474 | ×0.2^12 = 0.0 |
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
<details><summary><code>ussewc-usse-fl-2026-11-03-dem</code> SELL 25 @ 21¢ → $5.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 27 (25 yours) | ×0.1^0 = 27.0 |
|  | 98¢ | 132,784 | ×0.1^77 = 0.0 |
| | | **Σ** | **27.0** |

`yours 25.0 / Σ 27.0 = 92.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 92.6% = $5.79/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem` ← this one
2. `ussewc-usse-fl-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 60 @ 10¢ → $7.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 1 | ×0.2^0 = 1.4 |
| ▶ | 10¢ | 61 (60 yours) | ×0.2^1 = 12.2 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 20,476 | ×0.2^10 = 0.0 |
| | | **Σ** | **13.6** |

`yours 12.0 / Σ 13.6 = 88.4%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 88.4% = $7.37/day`  

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
<details><summary><code>ewc-usp-2028-11-07-andbes</code> BUY 24 @ 10¢ → $7.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 27 (24 yours) | ×0.2^0 = 26.7 |
|  | 9¢ | 2 | ×0.2^1 = 0.4 |
|  | 1¢ | 80,551 | ×0.2^9 = 0.0 |
| | | **Σ** | **27.2** |

`yours 24.0 / Σ 27.2 = 88.4%`  
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
|  | 51¢ | 100 | ×0.1^44 = 0.0 |
|  | 99¢ | 1,969 | ×0.1^92 = 0.0 |
| | | **Σ** | **57.0** |

`yours 50.0 / Σ 57.0 = 87.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 87.7% = $5.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> BUY 1 @ 11¢ → $7.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 30 | ×0.2^9 = 0.0 |
|  | 1¢ | 110,530 | ×0.2^10 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 86.9%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 86.9% = $7.24/day`  

<details><summary>÷ 60 markets in this race (17 known) — tap to list</summary>

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
<details><summary><code>ewc-usp-2028-11-07-stasmi</code> BUY 60 @ 10¢ → $7.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 70 (60 yours) | ×0.2^0 = 70.4 |
|  | 7¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 1 | ×0.2^6 = 0.0 |
|  | 2¢ | 3 | ×0.2^8 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^9 = 0.0 |
| | | **Σ** | **70.4** |

`yours 60.0 / Σ 70.4 = 85.2%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 85.2% = $7.10/day`  

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
22. `ewc-usp-2028-11-07-stasmi` ← this one
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 75 @ 9¢ → $5.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 91 (75 yours) | ×0.1^0 = 91.0 |
|  | 51¢ | 100 | ×0.1^42 = 0.0 |
|  | 98¢ | 208,063 | ×0.1^89 = 0.0 |
| | | **Σ** | **91.0** |

`yours 75.0 / Σ 91.0 = 82.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 82.4% = $5.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 96¢ → $4.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 98¢ | 421 | ×0.1^2 = 4.2 |
|  | 99¢ | 7,297 | ×0.1^3 = 7.3 |
| | | **Σ** | **51.5** |

`yours 40.0 / Σ 51.5 = 77.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 77.7% = $4.85/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 25 @ 7¢ → $2.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 27 (25 yours) | ×0.2^0 = 27.0 |
|  | 5¢ | 26 | ×0.2^2 = 1.0 |
|  | 1¢ | 90,449 | ×0.2^6 = 5.8 |
| | | **Σ** | **33.8** |

`yours 25.0 / Σ 33.8 = 73.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 73.9% = $2.84/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53` ← this one
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> SELL 50 @ 10¢ → $4.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 11¢ | 177 | ×0.1^1 = 17.7 |
|  | 14¢ | 10 | ×0.1^4 = 0.0 |
|  | 98¢ | 265,567 | ×0.1^88 = 0.0 |
| | | **Σ** | **67.7** |

`yours 50.0 / Σ 67.7 = 73.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 73.9% = $4.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-rep</code> SELL 3 @ 88¢ → $4.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 4 (3 yours) | ×0.1^0 = 3.8 |
|  | 96¢ | 1 | ×0.1^8 = 0.0 |
|  | 98¢ | 2,000 | ×0.1^10 = 0.0 |
| | | **Σ** | **3.8** |

`yours 2.8 / Σ 3.8 = 73.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 73.4% = $4.59/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem`
2. `ussewc-usse-ok-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jamtal</code> BUY 1 @ 18¢ → $5.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 17¢ | 1 | ×0.2^1 = 0.2 |
|  | 16¢ | 1 | ×0.2^2 = 0.0 |
|  | 13¢ | 2 | ×0.2^5 = 0.0 |
|  | 12¢ | 2 | ×0.2^6 = 0.0 |
|  | 10¢ | 60 | ×0.2^8 = 0.0 |
|  | 6¢ | 2 | ×0.2^12 = 0.0 |
|  | 5¢ | 1 | ×0.2^13 = 0.0 |
|  | 4¢ | 2 | ×0.2^14 = 0.0 |
|  | 3¢ | 1 | ×0.2^15 = 0.0 |
| | … | +1 levels | 0.0 |
| | | **Σ** | **1.4** |

`yours 1.0 / Σ 1.4 = 71.9%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 71.9% = $5.99/day`  

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
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 18¢ → $5.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 17¢ | 1 | ×0.2^1 = 0.2 |
|  | 16¢ | 1 | ×0.2^2 = 0.0 |
|  | 15¢ | 2 | ×0.2^3 = 0.0 |
|  | 13¢ | 1 | ×0.2^5 = 0.0 |
|  | 10¢ | 120 | ×0.2^8 = 0.0 |
|  | 6¢ | 1 | ×0.2^12 = 0.0 |
|  | 1¢ | 20,451 | ×0.2^17 = 0.0 |
| | | **Σ** | **1.4** |

`yours 1.0 / Σ 1.4 = 71.6%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 71.6% = $5.97/day`  

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
<details><summary><code>ussewc-usse-co-2026-11-03-rep</code> BUY 60 @ 10¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 84 (60 yours) | ×0.1^0 = 84.0 |
|  | 7¢ | 1 | ×0.1^3 = 0.0 |
|  | 6¢ | 17 | ×0.1^4 = 0.0 |
|  | 1¢ | 2,499 | ×0.1^9 = 0.0 |
| | | **Σ** | **84.0** |

`yours 60.0 / Σ 84.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem`
2. `ussewc-usse-co-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 8¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 75 (50 yours) | ×0.2^0 = 75.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 80,716 | ×0.2^89 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 1 @ 14¢ → $2.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 1 (1 yours) | ×0.2^0 = 1.1 |
|  | 13¢ | 1 | ×0.2^1 = 0.2 |
|  | 11¢ | 3 | ×0.2^3 = 0.0 |
|  | 10¢ | 120 | ×0.2^4 = 0.2 |
|  | 1¢ | 105,520 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.6** |

`yours 1.0 / Σ 1.6 = 63.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 63.9% = $2.46/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt4500</code> BUY 10 @ 42¢ → $2.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 17 (10 yours) | ×0.25^0 = 17.0 |
|  | 40¢ | 1 | ×0.25^2 = 0.1 |
|  | 31¢ | 101 | ×0.25^11 = 0.0 |
|  | 1¢ | 10,968 | ×0.25^41 = 0.0 |
| | | **Σ** | **17.1** |

`yours 10.0 / Σ 17.1 = 58.6%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 58.6% = $2.44/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500` ← this one
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jossha</code> BUY 2 @ 9¢ → $4.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 3 (2 yours) | ×0.2^0 = 3.3 |
|  | 4¢ | 2 | ×0.2^5 = 0.0 |
|  | 3¢ | 1 | ×0.2^6 = 0.0 |
|  | 2¢ | 1 | ×0.2^7 = 0.0 |
|  | 1¢ | 114,551 | ×0.2^8 = 0.3 |
| | | **Σ** | **3.6** |

`yours 2.0 / Σ 3.6 = 56.7%`  
`$1,000 ÷ 60 ÷ 2 = $8.33 × 56.7% = $4.72/day`  

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
<details><summary><code>ussewc-usse-tn-2026-11-03-dem</code> BUY 75 @ 8¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 150 (75 yours) | ×0.1^0 = 150.0 |
|  | 3¢ | 23 | ×0.1^5 = 0.0 |
|  | 2¢ | 1 | ×0.1^6 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^7 = 0.0 |
| | | **Σ** | **150.0** |

`yours 75.0 / Σ 150.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem` ← this one
2. `ussewc-usse-tn-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (263,736 resting) | ~97.6% | ~$6.10 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,519 resting) | ~16.3% | ~$4.06 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (555,842 resting) | ~13.9% | ~$3.48 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (27,772 resting) | ~44.8% | ~$2.80 |
| `ewc-usse-nh-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (2,706 resting) | ~27.9% | ~$1.75 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (13,508 resting) | ~2.2% | ~$1.65 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (14,462 resting) | ~2.2% | ~$1.65 |
| `ewc-usmayor-losang-2026-11-03-nitram` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (205,219 resting) | ~20.9% | ~$1.30 |
| `ewc-usgub-mi-2026-11-03-mikdug` | $25.00 ÷ 3 | 0.10 | 2,000 | SELL side (3,336 resting) | ~30.5% | ~$1.27 |
| `ewc-usmayor-losang-2026-11-03-karbas` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (205,159 resting) | ~20.1% | ~$1.26 |
| `ewc-usse-mi-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (552,881 resting) | ~19.7% | ~$1.23 |
| `ewc-usse-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (2,027 resting) | ~15.6% | ~$0.98 |

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
| 2026-08-16 8:14 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:09 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 8:03 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 7:52 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 7:47 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 7:36 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 7:25 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 6:38 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 5:37 AM ET | ✅ ok | 2562 | $3567.53 |
| 2026-08-16 4:37 AM ET | ✅ ok | 2562 | $3567.53 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
