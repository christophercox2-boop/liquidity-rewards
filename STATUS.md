# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-02 9:06 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$44.09/day estimated (ceiling, not promise — details below)

**Earned:** $1,515.42 lifetime ($1,373.47 paid). Last three recorded days — 2026-08-01: **$52.30** · 2026-07-31: **$67.96** · 2026-07-30: **$20.48** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — SELL at the best price, ~$18.69/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$14.93/day), `enwc-ussep-mn-2026-08-11-dem-angcra` (~$14.66/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$44.09/day (~$1.84/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 80.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (5,268 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 21.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~99.6% of bid side (5,619 resting ≥ 5,000 ✓) ≈ $3.83/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 39.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~74.1% of bid side (5,614 resting ≥ 5,000 ✓) ≈ $3.09/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~40.7% of ask side (7,439 resting ≥ 5,000 ✓) ≈ $1.70/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~40.4% of ask side (12,109 resting ≥ 5,000 ✓) ≈ $1.55/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 30.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~33.6% of ask side (12,465 resting ≥ 5,000 ✓) ≈ $1.29/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 15.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~31.6% of ask side (12,158 resting ≥ 5,000 ✓) ≈ $1.21/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~29.7% of ask side (12,425 resting ≥ 5,000 ✓) ≈ $1.14/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~28.6% of bid side (5,556 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~27.8% of ask side (12,127 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~26.8% of ask side (12,219 resting ≥ 5,000 ✓) ≈ $1.03/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 31.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~22.3% of bid side (5,540 resting ≥ 5,000 ✓) ≈ $0.93/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~20.8% of ask side (12,101 resting ≥ 5,000 ✓) ≈ $0.80/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~19.9% of bid side (12,351 resting ≥ 5,000 ✓) ≈ $0.77/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~19.7% of ask side (7,607 resting ≥ 5,000 ✓) ≈ $4.93/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~19.6% of bid side (25,468 resting ≥ 5,000 ✓) ≈ $0.76/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~19.6% of ask side (12,086 resting ≥ 5,000 ✓) ≈ $0.75/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~17.5% of ask side (12,194 resting ≥ 5,000 ✓) ≈ $0.67/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 2.0¢ | 2,000 | 0 | $100.00 | ✅ scoring — ~15.7% of bid side (12,910 resting ≥ 5,000 ✓) ≈ $0.66/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 19.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~15.7% of ask side (6,862 resting ≥ 5,000 ✓) ≈ $0.65/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 3.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~11.5% of bid side (8,879 resting ≥ 5,000 ✓) ≈ $0.44/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 25.0¢ | 50 | 2 | $100.00 | ✅ scoring — ~10.8% of ask side (11,385 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 15.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~10.6% of bid side (6,153 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~10.3% of bid side (5,364 resting ≥ 5,000 ✓) ≈ $2.57/day (pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | SELL | 16.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~8.9% of ask side (6,810 resting ≥ 5,000 ✓) ≈ $2.24/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 85.0¢ | 79 | 1 | $100.00 | ✅ scoring — ~8.9% of ask side (7,347 resting ≥ 5,000 ✓) ≈ $0.37/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~8.4% of bid side (12,163 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 45.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~7.7% of ask side (7,341 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~7.7% of ask side (12,252 resting ≥ 5,000 ✓) ≈ $0.29/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 84.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~7.5% of bid side (5,510 resting ≥ 5,000 ✓) ≈ $0.31/day (pool ÷ 12 markets) |
| …and 36 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 30 @ 80¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 30 (30 yours) | ×0.2^0 = 30.0 |
|  | 61¢ | 89 | ×0.2^19 = 0.0 |
|  | 1¢ | 5,149 | ×0.2^79 = 0.0 |
| | | **Σ** | **30.0** |

`yours 30.0 / Σ 30.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180` ← this one
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 50 @ 21¢ → $3.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 19¢ | 5 | ×0.2^2 = 0.2 |
|  | 11¢ | 4 | ×0.2^10 = 0.0 |
|  | 9¢ | 4 | ×0.2^12 = 0.0 |
|  | 1¢ | 5,555 | ×0.2^20 = 0.0 |
| | | **Σ** | **50.2** |

`yours 50.0 / Σ 50.2 = 99.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.6% = $3.83/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52` ← this one
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 100 @ 39¢ → $3.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 39¢ | 135 (100 yours) | ×0.2^0 = 135.0 |
|  | 1¢ | 5,479 | ×0.2^38 = 0.0 |
| | | **Σ** | **135.0** |

`yours 100.0 / Σ 135.0 = 74.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 74.1% = $3.09/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200` ← this one
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 50 @ 8¢ → $1.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 119 (50 yours) | ×0.2^0 = 119.0 |
|  | 10¢ | 94 | ×0.2^2 = 3.7 |
|  | 50¢ | 25 | ×0.2^42 = 0.0 |
|  | 99¢ | 7,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **122.7** |

`yours 50.0 / Σ 122.7 = 40.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 40.7% = $1.70/day`  

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
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230` ← this one
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 18 @ 15¢ → $1.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 45 (18 yours) | ×0.2^0 = 45.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **45.3** |

`yours 18.3 / Σ 45.3 = 40.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.4% = $1.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 30¢ → $1.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 128 (43 yours) | ×0.2^0 = 128.0 |
|  | 38¢ | 128 | ×0.2^8 = 0.0 |
|  | 40¢ | 37 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^20 = 0.0 |
|  | 98¢ | 1,871 | ×0.2^68 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^69 = 0.0 |
| | | **Σ** | **128.0** |

`yours 43.0 / Σ 128.0 = 33.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.6% = $1.29/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 15¢ → $1.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 95 (30 yours) | ×0.2^0 = 95.0 |
|  | 18¢ | 4 | ×0.2^3 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,758 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **95.0** |

`yours 30.0 / Σ 95.0 = 31.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.6% = $1.21/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
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
13. `scc-senate-gop-2026-11-03-lte45` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $1.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 135 (40 yours) | ×0.2^0 = 134.7 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **134.7** |

`yours 40.0 / Σ 134.7 = 29.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.7% = $1.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 100 @ 20¢ → $1.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 350 (100 yours) | ×0.2^0 = 350.0 |
|  | 18¢ | 6 | ×0.2^2 = 0.2 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **350.2** |

`yours 100.0 / Σ 350.2 = 28.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.6% = $1.10/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 16¢ → $1.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 72 (20 yours) | ×0.2^0 = 72.0 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^82 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^83 = 0.0 |
| | | **Σ** | **72.0** |

`yours 20.0 / Σ 72.0 = 27.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.8% = $1.07/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 149 (40 yours) | ×0.2^0 = 149.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **149.0** |

`yours 40.0 / Σ 149.0 = 26.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.8% = $1.03/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55` ← this one
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> BUY 30 @ 31¢ → $0.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 31¢ | 135 (30 yours) | ×0.2^0 = 134.5 |
|  | 1¢ | 5,405 | ×0.2^30 = 0.0 |
| | | **Σ** | **134.5** |

`yours 30.0 / Σ 134.5 = 22.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 22.3% = $0.93/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 10 @ 12¢ → $0.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 48 (10 yours) | ×0.2^0 = 48.0 |
|  | 29¢ | 2 | ×0.2^17 = 0.0 |
|  | 35¢ | 2 | ×0.2^23 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 98¢ | 1,748 | ×0.2^86 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^87 = 0.0 |
| | | **Σ** | **48.0** |

`yours 10.0 / Σ 48.0 = 20.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.8% = $0.80/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57` ← this one
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $0.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 2,111 (500 yours) | ×0.2^0 = 2,111.0 |
|  | 2¢ | 10,040 | ×0.2^2 = 401.6 |
| | | **Σ** | **2,512.6** |

`yours 500.0 / Σ 2,512.6 = 19.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.9% = $0.77/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56` ← this one
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 1 @ 13¢ → $4.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 5 (1 yours) | ×0.2^0 = 5.0 |
|  | 16¢ | 9 | ×0.2^3 = 0.1 |
|  | 27¢ | 206 | ×0.2^14 = 0.0 |
|  | 34¢ | 2,183 | ×0.2^21 = 0.0 |
|  | 35¢ | 1 | ×0.2^22 = 0.0 |
|  | 36¢ | 3 | ×0.2^23 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^86 = 0.0 |
| | | **Σ** | **5.1** |

`yours 1.0 / Σ 5.1 = 19.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 19.7% = $4.93/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5,000 @ 1¢ → $0.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 25,468 (5,000 yours) | ×0.2^0 = 25,467.9 |
| | | **Σ** | **25,467.9** |

`yours 5,000.0 / Σ 25,467.9 = 19.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.6% = $0.76/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 10¢ → $0.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 51 (10 yours) | ×0.2^0 = 51.0 |
|  | 16¢ | 3 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **51.0** |

`yours 10.0 / Σ 51.0 = 19.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.6% = $0.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 21 @ 8¢ → $0.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 120 (21 yours) | ×0.2^0 = 120.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,773 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **120.0** |

`yours 21.0 / Σ 120.0 = 17.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.5% = $0.67/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46` ← this one
2. `scc-senate-gop-2026-11-03-47`
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 2,000 @ 2¢ → $0.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 12,705 (2,000 yours) | ×0.2^0 = 12,705.0 |
| | | **Σ** | **12,705.0** |

`yours 2,000.0 / Σ 12,705.0 = 15.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 15.7% = $0.66/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220` ← this one
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 50 @ 19¢ → $0.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 141 (50 yours) | ×0.2^0 = 141.0 |
|  | 20¢ | 888 | ×0.2^1 = 177.5 |
|  | 50¢ | 25 | ×0.2^31 = 0.0 |
|  | 99¢ | 5,809 | ×0.2^80 = 0.0 |
| | | **Σ** | **318.5** |

`yours 50.0 / Σ 318.5 = 15.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 15.7% = $0.65/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1,000 @ 3¢ → $0.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,679 (1,000 yours) | ×0.2^0 = 8,679.0 |
| | | **Σ** | **8,679.0** |

`yours 1,000.0 / Σ 8,679.0 = 11.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.5% = $0.44/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 50 @ 25¢ → $0.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 15 | ×0.2^0 = 15.1 |
|  | 24¢ | 4 | ×0.2^1 = 0.8 |
| ▶ | 25¢ | 65 (50 yours) | ×0.2^2 = 2.6 |
|  | 50¢ | 100 | ×0.2^27 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^75 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^76 = 0.0 |
| | | **Σ** | **18.5** |

`yours 2.0 / Σ 18.5 = 10.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 10.8% = $0.42/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 500 @ 15¢ → $2.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 4,730 (500 yours) | ×0.2^0 = 4,730.0 |
|  | 13¢ | 8 | ×0.2^2 = 0.3 |
|  | 11¢ | 1,215 | ×0.2^4 = 1.9 |
| | | **Σ** | **4,732.3** |

`yours 500.0 / Σ 4,732.3 = 10.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 10.6% = $2.64/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 10 @ 12¢ → $2.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 97 (10 yours) | ×0.2^0 = 97.0 |
|  | 10¢ | 10 | ×0.2^2 = 0.4 |
|  | 5¢ | 57 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^11 = 0.0 |
| | | **Σ** | **97.4** |

`yours 10.0 / Σ 97.4 = 10.3%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 10.3% = $2.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 16¢ → $2.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1,118 (100 yours) | ×0.2^0 = 1,117.8 |
|  | 31¢ | 192 | ×0.2^15 = 0.0 |
|  | 41¢ | 200 | ×0.2^25 = 0.0 |
|  | 49¢ | 100 | ×0.2^33 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^83 = 0.0 |
| | | **Σ** | **1,117.8** |

`yours 100.0 / Σ 1,117.8 = 8.9%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 8.9% = $2.24/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 79 @ 85¢ → $0.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 84¢ | 161 | ×0.2^0 = 161.0 |
| ▶ | 85¢ | 79 (79 yours) | ×0.2^1 = 15.8 |
|  | 86¢ | 7 | ×0.2^2 = 0.3 |
|  | 91¢ | 64 | ×0.2^7 = 0.0 |
|  | 97¢ | 162 | ×0.2^13 = 0.0 |
|  | 99¢ | 6,874 | ×0.2^15 = 0.0 |
| | | **Σ** | **177.1** |

`yours 15.8 / Σ 177.1 = 8.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 8.9% = $0.37/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195` ← this one
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 11,860 (1,000 yours) | ×0.2^0 = 11,860.0 |
| | | **Σ** | **11,860.0** |

`yours 1,000.0 / Σ 11,860.0 = 8.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.4% = $0.32/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55` ← this one
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 3 @ 45¢ → $0.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 39 (3 yours) | ×0.2^0 = 39.0 |
|  | 50¢ | 51 | ×0.2^5 = 0.0 |
|  | 55¢ | 100 | ×0.2^10 = 0.0 |
|  | 69¢ | 107 | ×0.2^24 = 0.0 |
|  | 81¢ | 107 | ×0.2^36 = 0.0 |
|  | 99¢ | 6,937 | ×0.2^54 = 0.0 |
| | | **Σ** | **39.0** |

`yours 3.0 / Σ 39.0 = 7.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.7% = $0.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 10 @ 24¢ → $0.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 130 (10 yours) | ×0.2^0 = 130.4 |
|  | 50¢ | 100 | ×0.2^26 = 0.0 |
|  | 98¢ | 1,821 | ×0.2^74 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^75 = 0.0 |
| | | **Σ** | **130.4** |

`yours 10.0 / Σ 130.4 = 7.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.7% = $0.29/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52` ← this one
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 10 @ 84¢ → $0.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 133 (10 yours) | ×0.2^0 = 133.4 |
|  | 83¢ | 1 | ×0.2^1 = 0.2 |
|  | 78¢ | 243 | ×0.2^6 = 0.0 |
|  | 1¢ | 5,133 | ×0.2^83 = 0.0 |
| | | **Σ** | **133.6** |

`yours 10.0 / Σ 133.6 = 7.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.5% = $0.31/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190` ← this one
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-01 | ~$46.23 | $52.30 | 113% |
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |

Biggest gaps on 2026-08-01: `scc-hrep-rep-2026-11-03-gte215` (est ~$2.09 → got $1.51), `scc-senate-gop-2026-11-03-52` (est ~$3.15 → got $2.78), `cranc-uspres28-12-31-2026-tedcru` (est ~$0.71 → got $0.35)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (83,956 resting) | ~24.9% | ~$18.69 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,666 resting) | ~59.7% | ~$14.93 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (85,406 resting) | ~58.6% | ~$14.66 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,176 resting) | ~52.9% | ~$13.23 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (74,399 resting) | ~14.3% | ~$10.74 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (338,888 resting) | ~7.7% | ~$5.79 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (200,306 resting) | ~6.5% | ~$4.89 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (181,756 resting) | ~6.5% | ~$4.85 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (83,713 resting) | ~5.7% | ~$4.24 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (37,114 resting) | ~12.1% | ~$3.02 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $300.00 ÷ 3 | 0.20 | 10,000 | SELL side (18,435 resting) | ~4.8% | ~$2.40 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (115,186 resting) | ~2.2% | ~$1.63 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,373.47 |
| Pending | $140.74 |
| Skipped | $1.21 |
| **Total earned** | **$1,515.42** |

1532 reward rows · 30 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-01 | $52.30 | `█████` |
| 2026-07-31 | $67.96 | `██████` |
| 2026-07-30 | $20.48 | `██` |
| 2026-07-29 | $53.59 | `█████` |
| 2026-07-28 | $79.65 | `███████` |
| 2026-07-27 | $125.34 | `███████████` |
| 2026-07-26 | $153.80 | `██████████████` |
| 2026-07-25 | $125.69 | `███████████` |
| 2026-07-24 | $135.19 | `████████████` |
| 2026-07-23 | $227.63 | `████████████████████` |
| 2026-07-22 | $82.95 | `███████` |
| 2026-07-21 | $91.44 | `████████` |
| 2026-07-20 | $106.54 | `█████████` |
| 2026-07-19 | $35.81 | `███` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $52.30 | `█` |
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.60 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.96 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-02 9:06 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-02 8:15 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:59 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:15 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 6:13 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 5:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 3:38 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 1:26 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 12:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 11:30 AM ET | ✅ ok | 1490 | $1463.12 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
