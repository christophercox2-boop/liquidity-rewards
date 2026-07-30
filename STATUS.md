# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-30 7:45 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$16.68/day estimated (ceiling, not promise — details below)

**Earned:** $1,321.41 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$0.32** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — BUY at the best price, ~$7.17/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$6.41/day), `ewc-usse-tx-2026-11-03-rep` (~$5.18/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$16.68/day (~$0.69/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-47` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~91.8% of bid side (5,445 resting ≥ 5,000 ✓) ≈ $3.53/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 22.0¢ | 18 | 1 | $100.00 | ✅ scoring — ~84.4% of ask side (12,024 resting ≥ 5,000 ✓) ≈ $3.25/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 14.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~49.9% of ask side (11,907 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 10.0¢ | 5 | 2 | $100.00 | ✅ scoring — ~41.2% of ask side (12,038 resting ≥ 5,000 ✓) ≈ $1.59/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 30.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~29.0% of bid side (5,519 resting ≥ 5,000 ✓) ≈ $1.11/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 6.0¢ | 98 | 1 | $100.00 | ✅ scoring — ~20.1% of bid side (5,686 resting ≥ 5,000 ✓) ≈ $0.77/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 1.0¢ | 5,000 | 2 | $100.00 | ✅ scoring — ~19.8% of bid side (25,200 resting ≥ 5,000 ✓) ≈ $0.76/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~19.0% of bid side (26,380 resting ≥ 5,000 ✓) ≈ $0.73/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~18.9% of bid side (26,463 resting ≥ 5,000 ✓) ≈ $0.73/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~18.9% of bid side (26,475 resting ≥ 5,000 ✓) ≈ $0.73/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~18.9% of bid side (26,479 resting ≥ 5,000 ✓) ≈ $0.73/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 87.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~7.3% of ask side (5,549 resting ≥ 5,000 ✓) ≈ $0.31/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 33.0¢ | 42 | 1 | $100.00 | ✅ scoring — ~6.1% of ask side (12,138 resting ≥ 5,000 ✓) ≈ $0.24/day (pool ÷ 13 markets) |
| `ewc-usse-mi-2026-11-03-rep` | BUY | 29.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~3.5% of bid side (73,076 resting ≥ 2,000 ✓) ≈ $0.22/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~1.6% of bid side (5,886 resting ≥ 5,000 ✓) ≈ $0.06/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 6 | $100.00 | ✅ scoring — ~0.3% of bid side (5,686 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 6.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~0.0% of bid side (19,295 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 11.0¢ | 3 | 4 | $100.00 | ✅ scoring — ~0.0% of ask side (11,971 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 15.0¢ | 5 | 5 | $100.00 | ✅ scoring — ~0.0% of bid side (5,403 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 5.0¢ | 20 | 5 | $100.00 | ✅ scoring — ~0.0% of bid side (5,886 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 1.0¢ | 5,000 | 9 | $100.00 | ✅ scoring — ~0.0% of bid side (5,886 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 16.0¢ | 5 | 9 | $100.00 | ✅ scoring — ~0.0% of ask side (11,971 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 10.0¢ | 10 | 10 | $100.00 | ✅ scoring — ~0.0% of bid side (5,403 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 19.0¢ | 50 | 12 | $100.00 | ✅ scoring — ~0.0% of ask side (11,971 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 5.0¢ | 50 | 15 | $100.00 | ✅ scoring — ~0.0% of bid side (5,403 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 1.0¢ | 5,000 | 19 | $100.00 | ✅ scoring — ~0.0% of bid side (5,403 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 1.0¢ | 5,000 | 30 | $100.00 | ✅ scoring — ~0.0% of bid side (5,519 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 48.0¢ | 50 | 39 | $100.00 | ✅ scoring — ~0.0% of ask side (11,265 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 1.0¢ | 5,000 | 5 | $100.00 | ❌ outside Target Size window (order 5 ticks from best; window ends 0) |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 5,000 @ 1¢ → $3.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 1¢ | 5,445 (5,000 yours) | ×0.2^1 = 1,089.0 |
| | | **Σ** | **1,089.0** |

`yours 1,000.0 / Σ 1,089.0 = 91.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 91.8% = $3.53/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 18 @ 22¢ → $3.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 22¢ | 21 (18 yours) | ×0.2^1 = 4.1 |
|  | 24¢ | 1 | ×0.2^3 = 0.0 |
|  | 26¢ | 100 | ×0.2^5 = 0.0 |
|  | 37¢ | 5 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **4.2** |

`yours 3.5 / Σ 4.2 = 84.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 84.4% = $3.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 10 @ 14¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 14¢ | 20 (10 yours) | ×0.2^1 = 4.0 |
|  | 50¢ | 100 | ×0.2^37 = 0.0 |
|  | 98¢ | 1,786 | ×0.2^85 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^86 = 0.0 |
| | | **Σ** | **4.0** |

`yours 2.0 / Σ 4.0 = 49.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 49.9% = $1.92/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 5 @ 10¢ → $1.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 0 | ×0.2^0 = 0.0 |
|  | 9¢ | 1 | ×0.2^1 = 0.3 |
| ▶ | 10¢ | 5 (5 yours) | ×0.2^2 = 0.2 |
|  | 15¢ | 100 | ×0.2^7 = 0.0 |
|  | 40¢ | 29 | ×0.2^32 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,802 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^91 = 0.0 |
| | | **Σ** | **0.5** |

`yours 0.2 / Σ 0.5 = 41.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 41.2% = $1.59/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 20 @ 30¢ → $1.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 31¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 30¢ | 69 (20 yours) | ×0.2^1 = 13.8 |
|  | 1¢ | 5,450 | ×0.2^30 = 0.0 |
| | | **Σ** | **13.8** |

`yours 4.0 / Σ 13.8 = 29.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.0% = $1.11/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 98 @ 6¢ → $0.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 6¢ | 486 (98 yours) | ×0.2^1 = 97.2 |
|  | 1¢ | 5,200 | ×0.2^6 = 0.3 |
| | | **Σ** | **97.5** |

`yours 19.6 / Σ 97.5 = 20.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.1% = $0.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 5,000 @ 1¢ → $0.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 0 | ×0.2^0 = 0.0 |
|  | 2¢ | 4 | ×0.2^1 = 0.8 |
| ▶ | 1¢ | 25,196 (5,000 yours) | ×0.2^2 = 1,007.8 |
| | | **Σ** | **1,008.7** |

`yours 200.0 / Σ 1,008.7 = 19.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.8% = $0.76/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 5,000 @ 1¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 1¢ | 26,380 (5,000 yours) | ×0.2^1 = 5,276.0 |
| | | **Σ** | **5,276.0** |

`yours 1,000.0 / Σ 5,276.0 = 19.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.0% = $0.73/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 5,000 @ 1¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 1¢ | 26,463 (5,000 yours) | ×0.2^1 = 5,292.6 |
| | | **Σ** | **5,292.6** |

`yours 1,000.0 / Σ 5,292.6 = 18.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.9% = $0.73/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 5,000 @ 1¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 1¢ | 26,475 (5,000 yours) | ×0.2^1 = 5,295.0 |
| | | **Σ** | **5,295.0** |

`yours 1,000.0 / Σ 5,295.0 = 18.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.9% = $0.73/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 5,000 @ 1¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 1¢ | 26,479 (5,000 yours) | ×0.2^1 = 5,295.8 |
| | | **Σ** | **5,295.8** |

`yours 1,000.0 / Σ 5,295.8 = 18.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.9% = $0.73/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 87¢ → $0.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 682 (50 yours) | ×0.2^0 = 682.1 |
|  | 99¢ | 4,867 | ×0.2^12 = 0.0 |
| | | **Σ** | **682.1** |

`yours 50.0 / Σ 682.1 = 7.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.3% = $0.31/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 42 @ 33¢ → $0.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 32¢ | 114 | ×0.2^0 = 114.0 |
| ▶ | 33¢ | 116 (42 yours) | ×0.2^1 = 23.2 |
|  | 50¢ | 100 | ×0.2^18 = 0.0 |
|  | 98¢ | 1,807 | ×0.2^66 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^67 = 0.0 |
| | | **Σ** | **137.2** |

`yours 8.4 / Σ 137.2 = 6.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.1% = $0.24/day`  

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
<details><summary><code>ewc-usse-mi-2026-11-03-rep</code> BUY 100 @ 29¢ → $0.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 2,862 (100 yours) | ×0.1^0 = 2,862.0 |
| | | **Σ** | **2,862.0** |

`yours 100.0 / Σ 2,862.0 = 3.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 3.5% = $0.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-mi-2026-11-03-dem`
2. `ewc-usse-mi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 10¢ → $0.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 604 (10 yours) | ×0.2^0 = 604.0 |
|  | 8¢ | 62 | ×0.2^2 = 2.5 |
|  | 5¢ | 20 | ×0.2^5 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^9 = 0.0 |
| | | **Σ** | **606.5** |

`yours 10.0 / Σ 606.5 = 1.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.6% = $0.06/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 0 | ×0.2^0 = 0.0 |
|  | 6¢ | 486 | ×0.2^1 = 97.2 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^6 = 0.3 |
| | | **Σ** | **97.5** |

`yours 0.3 / Σ 97.5 = 0.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.3% = $0.01/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 4 @ 6¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 13,970 (4 yours) | ×0.2^0 = 13,969.5 |
| | | **Σ** | **13,969.5** |

`yours 3.5 / Σ 13,969.5 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 3 @ 11¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 53 | ×0.2^0 = 53.1 |
| ▶ | 11¢ | 3 (3 yours) | ×0.2^4 = 0.0 |
|  | 16¢ | 5 | ×0.2^9 = 0.0 |
|  | 19¢ | 50 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **53.1** |

`yours 0.0 / Σ 53.1 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5 @ 15¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 51 | ×0.2^0 = 51.0 |
|  | 18¢ | 28 | ×0.2^2 = 1.1 |
| ▶ | 15¢ | 5 (5 yours) | ×0.2^5 = 0.0 |
|  | 10¢ | 10 | ×0.2^10 = 0.0 |
|  | 5¢ | 50 | ×0.2^15 = 0.0 |
|  | 1¢ | 5,259 | ×0.2^19 = 0.0 |
| | | **Σ** | **52.1** |

`yours 0.0 / Σ 52.1 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 20 @ 5¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 604 | ×0.2^0 = 604.0 |
|  | 8¢ | 62 | ×0.2^2 = 2.5 |
| ▶ | 5¢ | 20 (20 yours) | ×0.2^5 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^9 = 0.0 |
| | | **Σ** | **606.5** |

`yours 0.0 / Σ 606.5 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 604 | ×0.2^0 = 604.0 |
|  | 8¢ | 62 | ×0.2^2 = 2.5 |
|  | 5¢ | 20 | ×0.2^5 = 0.0 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^9 = 0.0 |
| | | **Σ** | **606.5** |

`yours 0.0 / Σ 606.5 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 5 @ 16¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 53 | ×0.2^0 = 53.1 |
|  | 11¢ | 3 | ×0.2^4 = 0.0 |
| ▶ | 16¢ | 5 (5 yours) | ×0.2^9 = 0.0 |
|  | 19¢ | 50 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **53.1** |

`yours 0.0 / Σ 53.1 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 10 @ 10¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 51 | ×0.2^0 = 51.0 |
|  | 18¢ | 28 | ×0.2^2 = 1.1 |
|  | 15¢ | 5 | ×0.2^5 = 0.0 |
| ▶ | 10¢ | 10 (10 yours) | ×0.2^10 = 0.0 |
|  | 5¢ | 50 | ×0.2^15 = 0.0 |
|  | 1¢ | 5,259 | ×0.2^19 = 0.0 |
| | | **Σ** | **52.1** |

`yours 0.0 / Σ 52.1 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 50 @ 19¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 53 | ×0.2^0 = 53.1 |
|  | 11¢ | 3 | ×0.2^4 = 0.0 |
|  | 16¢ | 5 | ×0.2^9 = 0.0 |
| ▶ | 19¢ | 50 (50 yours) | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **53.1** |

`yours 0.0 / Σ 53.1 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 50 @ 5¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 51 | ×0.2^0 = 51.0 |
|  | 18¢ | 28 | ×0.2^2 = 1.1 |
|  | 15¢ | 5 | ×0.2^5 = 0.0 |
|  | 10¢ | 10 | ×0.2^10 = 0.0 |
| ▶ | 5¢ | 50 (50 yours) | ×0.2^15 = 0.0 |
|  | 1¢ | 5,259 | ×0.2^19 = 0.0 |
| | | **Σ** | **52.1** |

`yours 0.0 / Σ 52.1 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 51 | ×0.2^0 = 51.0 |
|  | 18¢ | 28 | ×0.2^2 = 1.1 |
|  | 15¢ | 5 | ×0.2^5 = 0.0 |
|  | 10¢ | 10 | ×0.2^10 = 0.0 |
|  | 5¢ | 50 | ×0.2^15 = 0.0 |
| ▶ | 1¢ | 5,259 (5,000 yours) | ×0.2^19 = 0.0 |
| | | **Σ** | **52.1** |

`yours 0.0 / Σ 52.1 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 31¢ | 0 | ×0.2^0 = 0.0 |
|  | 30¢ | 69 | ×0.2^1 = 13.8 |
| ▶ | 1¢ | 5,450 (5,000 yours) | ×0.2^30 = 0.0 |
| | | **Σ** | **13.8** |

`yours 0.0 / Σ 13.8 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 48¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
|  | 10¢ | 0 | ×0.2^1 = 0.0 |
|  | 30¢ | 112 | ×0.2^21 = 0.0 |
|  | 32¢ | 2 | ×0.2^23 = 0.0 |
| ▶ | 48¢ | 50 (50 yours) | ×0.2^39 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^90 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 5,000 @ 1¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 13,970 | ×0.2^0 = 13,969.5 |
| | | **Σ** | **13,969.5** |

`you 5t from best, window ends 0t → score 0`  

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-29 | ~$65.42 | $0.32 | 0% |
| 2026-07-28 | ~$148.78 | $79.65 | 54% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |

Biggest gaps on 2026-07-29: `apdc-petehegseth-2026-12-31` (est ~$12.90 → got $0.00), `scc-senate-gop-2026-11-03-51` (est ~$3.25 → got $0.00), `scc-senate-gop-2026-11-03-55` (est ~$2.26 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (72,937 resting) | ~9.6% | ~$7.17 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (75,412 resting) | ~8.5% | ~$6.41 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (313,140 resting) | ~6.9% | ~$5.18 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,360 resting) | ~4.0% | ~$2.98 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (178,705 resting) | ~3.5% | ~$2.66 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (123,021 resting) | ~3.4% | ~$2.54 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (112,938 resting) | ~2.1% | ~$1.58 |
| `ewc-usse-ak-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (72,784 resting) | ~20.9% | ~$1.30 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (89,076 resting) | ~1.6% | ~$1.22 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (86,455 resting) | ~4.6% | ~$1.15 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (65,092 resting) | ~15.7% | ~$0.98 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (388,555 resting) | ~1.3% | ~$0.95 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,240.74 |
| Pending | $79.46 |
| Skipped | $1.21 |
| **Total earned** | **$1,321.41** |

1267 reward rows · 27 days with rewards · 352 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-29 | $0.32 | `█` |
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
| 2026-07-18 | $44.41 | `████` |
| 2026-07-17 | $14.71 | `█` |
| 2026-07-16 | $17.02 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,321.41 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.23 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.22 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.75 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.47 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.70 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.21 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.64 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `vmc-ussep-misen-2026-08-04-els15-20` | $22.78 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-30 7:45 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 6:29 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 4:37 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:56 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:50 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 12:52 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 10:36 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 8:06 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 5:45 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:45 AM ET | ❌ error | 1267 | $1321.41 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
