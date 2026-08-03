# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-03 11:20 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$71.55/day estimated (ceiling, not promise — details below)

**Earned:** $1,515.42 lifetime ($1,373.47 paid). Last three recorded days — 2026-08-01: **$52.30** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-31: **$67.96** · 2026-07-30: **$20.48** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$19.16/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$16.75/day), `ewc-usgub-oh-2026-11-03-dem` (~$13.83/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$71.55/day (~$2.98/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-47` | BUY | 14.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~99.5% of bid side (5,471 resting ≥ 5,000 ✓) ≈ $3.83/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 24.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~91.7% of bid side (5,468 resting ≥ 5,000 ✓) ≈ $3.53/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 47 | 0 | $100.00 | ✅ scoring — ~88.9% of ask side (12,315 resting ≥ 5,000 ✓) ≈ $3.42/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 16.0¢ | 28 | 0 | $100.00 | ✅ scoring — ~77.8% of bid side (5,614 resting ≥ 5,000 ✓) ≈ $2.99/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 27.0¢ | 11 | 0 | $100.00 | ✅ scoring — ~68.7% of ask side (12,243 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 9.0¢ | 47 | 0 | $100.00 | ✅ scoring — ~65.3% of ask side (12,327 resting ≥ 5,000 ✓) ≈ $2.51/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~63.5% of ask side (12,353 resting ≥ 5,000 ✓) ≈ $2.44/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 19.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~60.6% of ask side (12,282 resting ≥ 5,000 ✓) ≈ $2.33/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 7.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~60.4% of bid side (25,570 resting ≥ 5,000 ✓) ≈ $2.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 21.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~59.2% of bid side (5,561 resting ≥ 5,000 ✓) ≈ $2.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~50.0% of ask side (12,116 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~45.7% of bid side (11,354 resting ≥ 5,000 ✓) ≈ $1.76/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~42.2% of ask side (12,208 resting ≥ 5,000 ✓) ≈ $1.62/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 25.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~41.7% of ask side (9,788 resting ≥ 5,000 ✓) ≈ $10.41/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 10.0¢ | 33 | 0 | $100.00 | ✅ scoring — ~39.8% of ask side (12,340 resting ≥ 5,000 ✓) ≈ $1.53/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 17.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~27.8% of bid side (5,611 resting ≥ 5,000 ✓) ≈ $6.95/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~21.5% of ask side (12,066 resting ≥ 5,000 ✓) ≈ $0.83/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $5,000.00 | ✅ scoring — ~20.3% of bid side (4,852 resting ≥ 2,500 ✓) ≈ $6.95/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 3.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~12.2% of bid side (8,379 resting ≥ 5,000 ✓) ≈ $0.47/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 10.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~11.8% of ask side (12,134 resting ≥ 5,000 ✓) ≈ $0.49/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 5.0¢ | 590 | 0 | $100.00 | ✅ scoring — ~11.7% of bid side (5,239 resting ≥ 5,000 ✓) ≈ $0.45/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-ind` | SELL | 2.0¢ | 32 | 0 | $5,000.00 | ✅ scoring — ~10.3% of ask side (5,283 resting ≥ 2,500 ✓) ≈ $3.52/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~8.6% of bid side (11,864 resting ≥ 5,000 ✓) ≈ $0.33/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~8.3% of bid side (59,926 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 6 | $100.00 | ✅ scoring — ~6.6% of bid side (25,570 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~6.4% of bid side (7,994 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 6.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~6.2% of bid side (12,599 resting ≥ 5,000 ✓) ≈ $0.26/day (pool ÷ 12 markets) |
| `ewc-usse-oh-2026-11-03-rep` | BUY | 48.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~6.0% of bid side (78,833 resting ≥ 5,000 ✓) ≈ $1.49/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 47.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~5.5% of bid side (5,552 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 80.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~4.8% of ask side (11,653 resting ≥ 5,000 ✓) ≈ $0.20/day (pool ÷ 12 markets) |
| …and 69 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 15 @ 14¢ → $3.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 12¢ | 2 | ×0.2^2 = 0.1 |
|  | 6¢ | 32 | ×0.2^8 = 0.0 |
|  | 5¢ | 2 | ×0.2^9 = 0.0 |
|  | 1¢ | 5,420 | ×0.2^13 = 0.0 |
| | | **Σ** | **15.1** |

`yours 15.0 / Σ 15.1 = 99.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.5% = $3.83/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 24¢ → $3.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 2 | ×0.2^3 = 0.0 |
|  | 20¢ | 46 | ×0.2^4 = 0.1 |
|  | 18¢ | 10 | ×0.2^6 = 0.0 |
|  | 1¢ | 5,409 | ×0.2^23 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 91.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 91.7% = $3.53/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 47 @ 22¢ → $3.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 47 (47 yours) | ×0.2^0 = 46.7 |
|  | 24¢ | 146 | ×0.2^2 = 5.9 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 98¢ | 1,821 | ×0.2^76 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^77 = 0.0 |
| | | **Σ** | **52.6** |

`yours 46.7 / Σ 52.6 = 88.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.9% = $3.42/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 28 @ 16¢ → $2.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 28 (28 yours) | ×0.2^0 = 28.0 |
|  | 15¢ | 40 | ×0.2^1 = 8.0 |
|  | 1¢ | 5,546 | ×0.2^15 = 0.0 |
| | | **Σ** | **36.0** |

`yours 28.0 / Σ 36.0 = 77.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 77.8% = $2.99/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 11 @ 27¢ → $2.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 16 (11 yours) | ×0.2^0 = 15.9 |
|  | 30¢ | 10 | ×0.2^3 = 0.1 |
|  | 43¢ | 93 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^23 = 0.0 |
|  | 98¢ | 1,823 | ×0.2^71 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^72 = 0.0 |
| | | **Σ** | **16.0** |

`yours 11.0 / Σ 16.0 = 68.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.7% = $2.64/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 47 @ 9¢ → $2.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 68 (47 yours) | ×0.2^0 = 68.0 |
|  | 11¢ | 100 | ×0.2^2 = 4.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,858 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **72.0** |

`yours 47.0 / Σ 72.0 = 65.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 65.3% = $2.51/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $2.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 63 (40 yours) | ×0.2^0 = 63.0 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **63.0** |

`yours 40.0 / Σ 63.0 = 63.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 63.5% = $2.44/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 19¢ → $2.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 71 (43 yours) | ×0.2^0 = 71.0 |
|  | 38¢ | 37 | ×0.2^19 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 98¢ | 1,873 | ×0.2^79 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^80 = 0.0 |
| | | **Σ** | **71.0** |

`yours 43.0 / Σ 71.0 = 60.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 60.6% = $2.33/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 3 @ 7¢ → $2.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 3 (3 yours) | ×0.2^0 = 2.9 |
|  | 6¢ | 1 | ×0.2^1 = 0.2 |
|  | 2¢ | 232 | ×0.2^5 = 0.1 |
|  | 1¢ | 25,334 | ×0.2^6 = 1.6 |
| | | **Σ** | **4.8** |

`yours 2.9 / Σ 4.8 = 60.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 60.4% = $2.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 21¢ → $2.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.3 |
|  | 20¢ | 4 | ×0.2^1 = 0.9 |
|  | 1¢ | 5,555 | ×0.2^20 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.3 / Σ 2.1 = 59.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 59.2% = $2.28/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 21 @ 8¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 42 (21 yours) | ×0.2^0 = 42.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,773 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **42.0** |

`yours 21.0 / Σ 42.0 = 50.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 50.0% = $1.92/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $1.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 674 (500 yours) | ×0.2^0 = 674.0 |
|  | 2¢ | 10,480 | ×0.2^2 = 419.2 |
| | | **Σ** | **1,093.2** |

`yours 500.0 / Σ 1,093.2 = 45.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 45.7% = $1.76/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 84 (40 yours) | ×0.2^0 = 84.0 |
|  | 7¢ | 54 | ×0.2^1 = 10.8 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **94.8** |

`yours 40.0 / Σ 94.8 = 42.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 42.2% = $1.62/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 25¢ → $10.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 240 (100 yours) | ×0.2^0 = 240.0 |
|  | 30¢ | 192 | ×0.2^5 = 0.1 |
|  | 46¢ | 200 | ×0.2^21 = 0.0 |
|  | 49¢ | 100 | ×0.2^24 = 0.0 |
|  | 99¢ | 9,056 | ×0.2^74 = 0.0 |
| | | **Σ** | **240.1** |

`yours 100.0 / Σ 240.1 = 41.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 41.7% = $10.41/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 33 @ 10¢ → $1.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 63 (33 yours) | ×0.2^0 = 63.0 |
|  | 11¢ | 100 | ×0.2^1 = 20.0 |
|  | 15¢ | 30 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,846 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **83.0** |

`yours 33.0 / Σ 83.0 = 39.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 39.8% = $1.53/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 100 @ 17¢ → $6.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 200 (100 yours) | ×0.2^0 = 200.0 |
|  | 15¢ | 3,996 | ×0.2^2 = 159.8 |
|  | 11¢ | 1,215 | ×0.2^6 = 0.1 |
| | | **Σ** | **359.9** |

`yours 100.0 / Σ 359.9 = 27.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 27.8% = $6.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 3 @ 15¢ → $0.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 15 (3 yours) | ×0.2^0 = 15.3 |
|  | 18¢ | 5 | ×0.2^3 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,745 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **15.3** |

`yours 3.3 / Σ 15.3 = 21.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 21.5% = $0.83/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $6.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 653 | ×0.9^0 = 653.2 |
| ▶ | 1¢ | 4,199 (1,000 yours) | ×0.9^1 = 3,779.1 |
| | | **Σ** | **4,432.3** |

`yours 900.0 / Σ 4,432.3 = 20.3%`  
`$5,000 ÷ 73 ÷ 2 = $34.25 × 20.3% = $6.95/day`  

<details><summary>÷ 73 markets in this race (40 known) — tap to list</summary>

1. `tec-cbb-champ-2027-04-05-w-ala`
2. `tec-cbb-champ-2027-04-05-w-ark`
3. `tec-cbb-champ-2027-04-05-w-arz`
4. `tec-cbb-champ-2027-04-05-w-aubrn`
5. `tec-cbb-champ-2027-04-05-w-bayl`
6. `tec-cbb-champ-2027-04-05-w-boise`
7. `tec-cbb-champ-2027-04-05-w-boscol`
8. `tec-cbb-champ-2027-04-05-w-butl`
9. `tec-cbb-champ-2027-04-05-w-byu`
10. `tec-cbb-champ-2027-04-05-w-cin`
11. `tec-cbb-champ-2027-04-05-w-clmsn`
12. `tec-cbb-champ-2027-04-05-w-colst`
13. `tec-cbb-champ-2027-04-05-w-creigh`
14. `tec-cbb-champ-2027-04-05-w-day`
15. `tec-cbb-champ-2027-04-05-w-duke`
16. `tec-cbb-champ-2027-04-05-w-fl`
17. `tec-cbb-champ-2027-04-05-w-flst`
18. `tec-cbb-champ-2027-04-05-w-george`
19. `tec-cbb-champ-2027-04-05-w-gnzg`
20. `tec-cbb-champ-2027-04-05-w-hou`
21. `tec-cbb-champ-2027-04-05-w-ill`
22. `tec-cbb-champ-2027-04-05-w-ind`
23. `tec-cbb-champ-2027-04-05-w-iowa`
24. `tec-cbb-champ-2027-04-05-w-iowast`
25. `tec-cbb-champ-2027-04-05-w-kan`
26. `tec-cbb-champ-2027-04-05-w-lou`
27. `tec-cbb-champ-2027-04-05-w-loych`
28. `tec-cbb-champ-2027-04-05-w-lsutig`
29. `tec-cbb-champ-2027-04-05-w-marq`
30. `tec-cbb-champ-2027-04-05-w-mia`
31. `tec-cbb-champ-2027-04-05-w-mich`
32. `tec-cbb-champ-2027-04-05-w-miss`
33. `tec-cbb-champ-2027-04-05-w-missr`
34. `tec-cbb-champ-2027-04-05-w-mphs`
35. `tec-cbb-champ-2027-04-05-w-mspst`
36. `tec-cbb-champ-2027-04-05-w-mst`
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1,000 @ 3¢ → $0.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,179 (1,000 yours) | ×0.2^0 = 8,179.0 |
| | | **Σ** | **8,179.0** |

`yours 1,000.0 / Σ 8,179.0 = 12.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 12.2% = $0.47/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 3 @ 10¢ → $0.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 25 (3 yours) | ×0.2^0 = 25.3 |
|  | 14¢ | 100 | ×0.2^4 = 0.2 |
|  | 20¢ | 1 | ×0.2^10 = 0.0 |
|  | 50¢ | 25 | ×0.2^40 = 0.0 |
|  | 99¢ | 11,983 | ×0.2^89 = 0.0 |
| | | **Σ** | **25.4** |

`yours 3.0 / Σ 25.4 = 11.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.8% = $0.49/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 590 @ 5¢ → $0.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 5,039 (590 yours) | ×0.2^0 = 5,039.0 |
| | | **Σ** | **5,039.0** |

`yours 590.0 / Σ 5,039.0 = 11.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.7% = $0.45/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-ind</code> SELL 32 @ 2¢ → $3.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 52 (32 yours) | ×0.9^0 = 52.0 |
|  | 15¢ | 862 | ×0.9^13 = 219.0 |
|  | 16¢ | 1 | ×0.9^14 = 0.1 |
|  | 20¢ | 21 | ×0.9^18 = 3.2 |
|  | 25¢ | 400 | ×0.9^23 = 35.5 |
|  | 50¢ | 200 | ×0.9^48 = 1.3 |
|  | 97¢ | 48 | ×0.9^95 = 0.0 |
|  | 98¢ | 1,000 | ×0.9^96 = 0.0 |
| | | **Σ** | **311.0** |

`yours 32.0 / Σ 311.0 = 10.3%`  
`$5,000 ÷ 73 ÷ 2 = $34.25 × 10.3% = $3.52/day`  

<details><summary>÷ 73 markets in this race (40 known) — tap to list</summary>

1. `tec-cbb-champ-2027-04-05-w-ala`
2. `tec-cbb-champ-2027-04-05-w-ark`
3. `tec-cbb-champ-2027-04-05-w-arz`
4. `tec-cbb-champ-2027-04-05-w-aubrn`
5. `tec-cbb-champ-2027-04-05-w-bayl`
6. `tec-cbb-champ-2027-04-05-w-boise`
7. `tec-cbb-champ-2027-04-05-w-boscol`
8. `tec-cbb-champ-2027-04-05-w-butl`
9. `tec-cbb-champ-2027-04-05-w-byu`
10. `tec-cbb-champ-2027-04-05-w-cin`
11. `tec-cbb-champ-2027-04-05-w-clmsn`
12. `tec-cbb-champ-2027-04-05-w-colst`
13. `tec-cbb-champ-2027-04-05-w-creigh`
14. `tec-cbb-champ-2027-04-05-w-day`
15. `tec-cbb-champ-2027-04-05-w-duke`
16. `tec-cbb-champ-2027-04-05-w-fl`
17. `tec-cbb-champ-2027-04-05-w-flst`
18. `tec-cbb-champ-2027-04-05-w-george`
19. `tec-cbb-champ-2027-04-05-w-gnzg`
20. `tec-cbb-champ-2027-04-05-w-hou`
21. `tec-cbb-champ-2027-04-05-w-ill`
22. `tec-cbb-champ-2027-04-05-w-ind` ← this one
23. `tec-cbb-champ-2027-04-05-w-iowa`
24. `tec-cbb-champ-2027-04-05-w-iowast`
25. `tec-cbb-champ-2027-04-05-w-kan`
26. `tec-cbb-champ-2027-04-05-w-lou`
27. `tec-cbb-champ-2027-04-05-w-loych`
28. `tec-cbb-champ-2027-04-05-w-lsutig`
29. `tec-cbb-champ-2027-04-05-w-marq`
30. `tec-cbb-champ-2027-04-05-w-mia`
31. `tec-cbb-champ-2027-04-05-w-mich`
32. `tec-cbb-champ-2027-04-05-w-miss`
33. `tec-cbb-champ-2027-04-05-w-missr`
34. `tec-cbb-champ-2027-04-05-w-mphs`
35. `tec-cbb-champ-2027-04-05-w-mspst`
36. `tec-cbb-champ-2027-04-05-w-mst`
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 11,664 (1,000 yours) | ×0.2^0 = 11,664.0 |
| | | **Σ** | **11,664.0** |

`yours 1,000.0 / Σ 11,664.0 = 8.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.6% = $0.33/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5,000 @ 1¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 59,926 (5,000 yours) | ×0.2^0 = 59,926.0 |
| | | **Σ** | **59,926.0** |

`yours 5,000.0 / Σ 59,926.0 = 8.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.3% = $0.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 3 | ×0.2^0 = 2.9 |
|  | 6¢ | 1 | ×0.2^1 = 0.2 |
|  | 2¢ | 232 | ×0.2^5 = 0.1 |
| ▶ | 1¢ | 25,334 (5,000 yours) | ×0.2^6 = 1.6 |
| | | **Σ** | **4.8** |

`yours 0.3 / Σ 4.8 = 6.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.6% = $0.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 7,794 (500 yours) | ×0.2^0 = 7,794.0 |
| | | **Σ** | **7,794.0** |

`yours 500.0 / Σ 7,794.0 = 6.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.4% = $0.25/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 30 @ 6¢ → $0.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 465 (30 yours) | ×0.2^0 = 465.0 |
|  | 5¢ | 5 | ×0.2^1 = 1.0 |
|  | 2¢ | 11,929 | ×0.2^4 = 19.1 |
| | | **Σ** | **485.1** |

`yours 30.0 / Σ 485.1 = 6.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 6.2% = $0.26/day`  

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
<details><summary><code>ewc-usse-oh-2026-11-03-rep</code> BUY 50 @ 48¢ → $1.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 515 (50 yours) | ×0.2^0 = 515.0 |
|  | 47¢ | 6 | ×0.2^1 = 1.2 |
|  | 46¢ | 8,072 | ×0.2^2 = 322.9 |
| | | **Σ** | **839.1** |

`yours 50.0 / Σ 839.1 = 6.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 6.0% = $1.49/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-oh-2026-11-03-dem`
2. `ewc-usse-oh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 47¢ → $0.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 48¢ | 30 | ×0.2^0 = 30.0 |
| ▶ | 47¢ | 31 (10 yours) | ×0.2^1 = 6.2 |
|  | 43¢ | 10 | ×0.2^5 = 0.0 |
|  | 39¢ | 100 | ×0.2^9 = 0.0 |
|  | 1¢ | 5,381 | ×0.2^47 = 0.0 |
| | | **Σ** | **36.2** |

`yours 2.0 / Σ 36.2 = 5.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.5% = $0.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 10 @ 80¢ → $0.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 172 (10 yours) | ×0.2^0 = 172.0 |
|  | 82¢ | 94 | ×0.2^2 = 3.8 |
|  | 83¢ | 4,143 | ×0.2^3 = 33.1 |
|  | 94¢ | 43 | ×0.2^14 = 0.0 |
|  | 99¢ | 7,201 | ×0.2^19 = 0.0 |
| | | **Σ** | **208.9** |

`yours 10.0 / Σ 208.9 = 4.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.8% = $0.20/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |
| 2026-07-29 | ~$65.42 | $53.59 | 82% |

Biggest gaps on 2026-07-31: `scc-senate-gop-2026-11-03-48` (est ~$3.79 → got $2.51), `scc-senate-gop-2026-11-03-50` (est ~$3.29 → got $2.17), `apdc-alito-2026-12-31` (est ~$1.38 → got $0.45)

_2026-08-01 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,373 resting) | ~76.6% | ~$19.16 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (26,606 resting) | ~67.0% | ~$16.75 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (77,939 resting) | ~18.4% | ~$13.83 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (79,237 resting) | ~48.0% | ~$11.99 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (316,893 resting) | ~11.9% | ~$8.96 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (181,491 resting) | ~8.7% | ~$6.51 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (84,195 resting) | ~7.3% | ~$5.49 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (88,695 resting) | ~6.0% | ~$4.46 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (99,629 resting) | ~3.0% | ~$2.25 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (100,191 resting) | ~2.5% | ~$1.87 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (114,871 resting) | ~2.2% | ~$1.69 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (197,391 resting) | ~1.9% | ~$1.43 |

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
| 2026-08-01 ⚠️ multi-day pending bucket | $52.30 | `█████` |
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
| 2026-08-03 11:20 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:30 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:15 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:13 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 7:48 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 3:51 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 12:00 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-02 9:06 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-02 8:15 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:59 PM ET | ✅ ok | 1490 | $1463.12 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
