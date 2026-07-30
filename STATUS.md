# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-30 2:56 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$14.78/day estimated (ceiling, not promise — details below)

**Earned:** $1,321.41 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$0.32** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `cranc-uspres28-12-31-2026-tuccar` — SELL at the best price, ~$1.51/day for 200 contracts. Runners-up: `cranc-uspres28-12-31-2026-andyan` (~$1.51/day), `cranc-uspres28-12-31-2026-petbut` (~$1.51/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$14.78/day (~$0.62/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-lte45` | SELL | 7.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~99.9% of ask side (11,266 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 20.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.8% of ask side (11,257 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 22.0¢ | 18 | 1 | $100.00 | ✅ scoring — ~98.8% of ask side (12,021 resting ≥ 5,000 ✓) ≈ $3.80/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 5,000 | 2 | $100.00 | ✅ scoring — ~19.8% of bid side (25,194 resting ≥ 5,000 ✓) ≈ $0.76/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 6.0¢ | 30 | 1 | $100.00 | ✅ scoring — ~14.7% of bid side (25,641 resting ≥ 5,000 ✓) ≈ $0.57/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~13.1% of bid side (5,371 resting ≥ 5,000 ✓) ≈ $0.51/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 7.0¢ | 49 | 3 | $100.00 | ✅ scoring — ~12.9% of bid side (5,372 resting ≥ 5,000 ✓) ≈ $0.50/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 87.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~7.1% of ask side (5,549 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 1.0¢ | 5,000 | 5 | $100.00 | ✅ scoring — ~3.9% of bid side (25,392 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 1.0¢ | 5,000 | 5 | $100.00 | ✅ scoring — ~3.9% of bid side (25,396 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 5.0¢ | 196 | 0 | $100.00 | ✅ scoring — ~3.2% of bid side (11,238 resting ≥ 5,000 ✓) ≈ $0.12/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 6.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~3.2% of ask side (11,636 resting ≥ 5,000 ✓) ≈ $0.12/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 6.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~1.2% of bid side (26,040 resting ≥ 5,000 ✓) ≈ $0.05/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 1.0¢ | 5,000 | 6 | $100.00 | ✅ scoring — ~0.8% of bid side (25,641 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 1.0¢ | 5,000 | 5 | $100.00 | ✅ scoring — ~0.5% of bid side (26,040 resting ≥ 5,000 ✓) ≈ $0.02/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 20.0¢ | 1 | 2 | $100.00 | ✅ scoring — ~0.2% of ask side (12,118 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 25.0¢ | 5 | 5 | $100.00 | ✅ scoring — ~0.2% of ask side (11,257 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 1.0¢ | 5,000 | 9 | $100.00 | ✅ scoring — ~0.1% of bid side (5,372 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 9.0¢ | 3 | 3 | $100.00 | ✅ scoring — ~0.1% of ask side (11,636 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 11.0¢ | 3 | 4 | $100.00 | ✅ scoring — ~0.1% of ask side (11,266 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 42.0¢ | 50 | 6 | $100.00 | ✅ scoring — ~0.0% of ask side (11,247 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 48.0¢ | 50 | 6 | $100.00 | ✅ scoring — ~0.0% of ask side (11,268 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 10.0¢ | 20 | 6 | $100.00 | ✅ scoring — ~0.0% of bid side (5,371 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 15.0¢ | 5 | 6 | $100.00 | ✅ scoring — ~0.0% of bid side (5,335 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-kamhar` | SELL | 27.0¢ | 2 | 6 | $100.00 | ✅ scoring — ~0.0% of ask side (5,101 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 15.0¢ | 5 | 5 | $100.00 | ✅ scoring — ~0.0% of bid side (5,618 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 25.0¢ | 5 | 7 | $100.00 | ✅ scoring — ~0.0% of ask side (12,118 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 13.0¢ | 5 | 7 | $100.00 | ✅ scoring — ~0.0% of ask side (11,636 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 30.0¢ | 10 | 10 | $100.00 | ✅ scoring — ~0.0% of ask side (11,257 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 16.0¢ | 5 | 9 | $100.00 | ✅ scoring — ~0.0% of ask side (11,266 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| …and 15 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 7 @ 7¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 7 (7 yours) | ×0.2^0 = 7.4 |
|  | 11¢ | 3 | ×0.2^4 = 0.0 |
|  | 16¢ | 5 | ×0.2^9 = 0.0 |
|  | 19¢ | 50 | ×0.2^12 = 0.0 |
|  | 20¢ | 100 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **7.4** |

`yours 7.4 / Σ 7.4 = 99.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.9% = $3.84/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 1 @ 20¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 24¢ | 0 | ×0.2^4 = 0.0 |
|  | 25¢ | 5 | ×0.2^5 = 0.0 |
|  | 30¢ | 10 | ×0.2^10 = 0.0 |
|  | 33¢ | 125 | ×0.2^13 = 0.0 |
|  | 35¢ | 15 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.8% = $3.84/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 18 @ 22¢ → $3.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 22¢ | 18 (18 yours) | ×0.2^1 = 3.5 |
|  | 26¢ | 100 | ×0.2^5 = 0.0 |
|  | 37¢ | 5 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,797 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **3.6** |

`yours 3.5 / Σ 3.6 = 98.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.8% = $3.80/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 5,000 @ 1¢ → $0.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 0 | ×0.2^0 = 0.0 |
|  | 2¢ | 4 | ×0.2^1 = 0.8 |
| ▶ | 1¢ | 25,190 (5,000 yours) | ×0.2^2 = 1,007.6 |
| | | **Σ** | **1,008.4** |

`yours 200.0 / Σ 1,008.4 = 19.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.8% = $0.76/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 30 @ 6¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 6¢ | 196 (30 yours) | ×0.2^1 = 39.2 |
|  | 1¢ | 25,445 | ×0.2^6 = 1.6 |
| | | **Σ** | **40.8** |

`yours 6.0 / Σ 40.8 = 14.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.7% = $0.57/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 10 @ 15¢ → $0.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 15¢ | 76 (10 yours) | ×0.2^1 = 15.2 |
|  | 10¢ | 20 | ×0.2^6 = 0.0 |
|  | 5¢ | 50 | ×0.2^11 = 0.0 |
|  | 1¢ | 5,225 | ×0.2^15 = 0.0 |
| | | **Σ** | **15.2** |

`yours 2.0 / Σ 15.2 = 13.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 13.1% = $0.51/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 49 @ 7¢ → $0.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 0 | ×0.2^0 = 0.0 |
|  | 9¢ | 2 | ×0.2^1 = 0.4 |
|  | 8¢ | 56 | ×0.2^2 = 2.2 |
| ▶ | 7¢ | 49 (49 yours) | ×0.2^3 = 0.4 |
|  | 1¢ | 5,265 | ×0.2^9 = 0.0 |
| | | **Σ** | **3.0** |

`yours 0.4 / Σ 3.0 = 12.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 12.9% = $0.50/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 87¢ → $0.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 706 (50 yours) | ×0.2^0 = 706.1 |
|  | 99¢ | 4,843 | ×0.2^12 = 0.0 |
| | | **Σ** | **706.1** |

`yours 50.0 / Σ 706.1 = 7.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.1% = $0.30/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 5,000 @ 1¢ → $0.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 0 | ×0.2^0 = 0.0 |
|  | 5¢ | 167 | ×0.2^1 = 33.4 |
| ▶ | 1¢ | 25,225 (5,000 yours) | ×0.2^5 = 8.1 |
| | | **Σ** | **41.5** |

`yours 1.6 / Σ 41.5 = 3.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.9% = $0.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 5,000 @ 1¢ → $0.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 0 | ×0.2^0 = 0.0 |
|  | 5¢ | 167 | ×0.2^1 = 33.4 |
| ▶ | 1¢ | 25,229 (5,000 yours) | ×0.2^5 = 8.1 |
| | | **Σ** | **41.5** |

`yours 1.6 / Σ 41.5 = 3.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.9% = $0.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 196 @ 5¢ → $0.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 6,058 (196 yours) | ×0.2^0 = 6,058.0 |
| | | **Σ** | **6,058.0** |

`yours 196.0 / Σ 6,058.0 = 3.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.2% = $0.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 1 @ 6¢ → $0.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 31 (1 yours) | ×0.2^0 = 31.2 |
|  | 9¢ | 3 | ×0.2^3 = 0.0 |
|  | 13¢ | 5 | ×0.2^7 = 0.0 |
|  | 17¢ | 467 | ×0.2^11 = 0.0 |
|  | 40¢ | 29 | ×0.2^34 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **31.2** |

`yours 1.0 / Σ 31.2 = 3.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.2% = $0.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 4 @ 6¢ → $0.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 170 (4 yours) | ×0.2^0 = 169.6 |
|  | 5¢ | 545 | ×0.2^1 = 109.0 |
|  | 4¢ | 125 | ×0.2^2 = 5.0 |
|  | 1¢ | 25,200 | ×0.2^5 = 8.1 |
| | | **Σ** | **291.6** |

`yours 3.5 / Σ 291.6 = 1.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.2% = $0.05/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 5,000 @ 1¢ → $0.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 0 | ×0.2^0 = 0.0 |
|  | 6¢ | 196 | ×0.2^1 = 39.2 |
| ▶ | 1¢ | 25,445 (5,000 yours) | ×0.2^6 = 1.6 |
| | | **Σ** | **40.8** |

`yours 0.3 / Σ 40.8 = 0.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.8% = $0.03/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 5,000 @ 1¢ → $0.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 170 | ×0.2^0 = 169.6 |
|  | 5¢ | 545 | ×0.2^1 = 109.0 |
|  | 4¢ | 125 | ×0.2^2 = 5.0 |
| ▶ | 1¢ | 25,200 (5,000 yours) | ×0.2^5 = 8.1 |
| | | **Σ** | **291.6** |

`yours 1.6 / Σ 291.6 = 0.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.5% = $0.02/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 1 @ 20¢ → $0.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 0 | ×0.2^0 = 0.0 |
|  | 19¢ | 112 | ×0.2^1 = 22.4 |
| ▶ | 20¢ | 1 (1 yours) | ×0.2^2 = 0.0 |
|  | 25¢ | 5 | ×0.2^7 = 0.0 |
|  | 30¢ | 10 | ×0.2^12 = 0.0 |
|  | 35¢ | 20 | ×0.2^17 = 0.0 |
|  | 40¢ | 40 | ×0.2^22 = 0.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,829 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^81 = 0.0 |
| | | **Σ** | **22.5** |

`yours 0.0 / Σ 22.5 = 0.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.2% = $0.01/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 5 @ 25¢ → $0.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 1 | ×0.2^0 = 1.0 |
|  | 24¢ | 0 | ×0.2^4 = 0.0 |
| ▶ | 25¢ | 5 (5 yours) | ×0.2^5 = 0.0 |
|  | 30¢ | 10 | ×0.2^10 = 0.0 |
|  | 33¢ | 125 | ×0.2^13 = 0.0 |
|  | 35¢ | 15 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **1.0** |

`yours 0.0 / Σ 1.0 = 0.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.2% = $0.01/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 0 | ×0.2^0 = 0.0 |
|  | 9¢ | 2 | ×0.2^1 = 0.4 |
|  | 8¢ | 56 | ×0.2^2 = 2.2 |
|  | 7¢ | 49 | ×0.2^3 = 0.4 |
| ▶ | 1¢ | 5,265 (5,000 yours) | ×0.2^9 = 0.0 |
| | | **Σ** | **3.0** |

`yours 0.0 / Σ 3.0 = 0.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.1% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 3 @ 9¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 31 | ×0.2^0 = 31.2 |
| ▶ | 9¢ | 3 (3 yours) | ×0.2^3 = 0.0 |
|  | 13¢ | 5 | ×0.2^7 = 0.0 |
|  | 17¢ | 467 | ×0.2^11 = 0.0 |
|  | 40¢ | 29 | ×0.2^34 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **31.2** |

`yours 0.0 / Σ 31.2 = 0.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.1% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 3 @ 11¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 7 | ×0.2^0 = 7.4 |
| ▶ | 11¢ | 3 (3 yours) | ×0.2^4 = 0.0 |
|  | 16¢ | 5 | ×0.2^9 = 0.0 |
|  | 19¢ | 50 | ×0.2^12 = 0.0 |
|  | 20¢ | 100 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **7.4** |

`yours 0.0 / Σ 7.4 = 0.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.1% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 50 @ 42¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 36¢ | 0 | ×0.2^0 = 0.0 |
|  | 37¢ | 96 | ×0.2^1 = 19.2 |
| ▶ | 42¢ | 50 (50 yours) | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^14 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^62 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^63 = 0.0 |
| | | **Σ** | **19.2** |

`yours 0.0 / Σ 19.2 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 48¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 42¢ | 0 | ×0.2^0 = 0.0 |
|  | 43¢ | 117 | ×0.2^1 = 23.4 |
| ▶ | 48¢ | 50 (50 yours) | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^8 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^56 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^57 = 0.0 |
| | | **Σ** | **23.4** |

`yours 0.0 / Σ 23.4 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 20 @ 10¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
|  | 15¢ | 76 | ×0.2^1 = 15.2 |
| ▶ | 10¢ | 20 (20 yours) | ×0.2^6 = 0.0 |
|  | 5¢ | 50 | ×0.2^11 = 0.0 |
|  | 1¢ | 5,225 | ×0.2^15 = 0.0 |
| | | **Σ** | **15.2** |

`yours 0.0 / Σ 15.2 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5 @ 15¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 0 | ×0.2^0 = 0.0 |
|  | 20¢ | 50 | ×0.2^1 = 10.0 |
| ▶ | 15¢ | 5 (5 yours) | ×0.2^6 = 0.0 |
|  | 10¢ | 10 | ×0.2^11 = 0.0 |
|  | 5¢ | 20 | ×0.2^16 = 0.0 |
|  | 1¢ | 5,250 | ×0.2^20 = 0.0 |
| | | **Σ** | **10.0** |

`yours 0.0 / Σ 10.0 = 0.0%`  
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
<details><summary><code>cranc-uspres28-12-31-2026-kamhar</code> SELL 2 @ 27¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 0 | ×0.2^0 = 0.0 |
|  | 22¢ | 3 | ×0.2^1 = 0.6 |
|  | 23¢ | 62 | ×0.2^2 = 2.5 |
|  | 24¢ | 69 | ×0.2^3 = 0.6 |
|  | 25¢ | 580 | ×0.2^4 = 0.9 |
| ▶ | 27¢ | 4 (2 yours) | ×0.2^6 = 0.0 |
|  | 45¢ | 192 | ×0.2^24 = 0.0 |
|  | 50¢ | 25 | ×0.2^29 = 0.0 |
|  | 99¢ | 4,166 | ×0.2^78 = 0.0 |
| | | **Σ** | **4.6** |

`yours 0.0 / Σ 4.6 = 0.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 0.0% = $0.00/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru`
7. `cranc-uspres28-12-31-2026-dontrujr`
8. `cranc-uspres28-12-31-2026-dwajoh`
9. `cranc-uspres28-12-31-2026-elomus`
10. `cranc-uspres28-12-31-2026-erikir`
11. `cranc-uspres28-12-31-2026-gavnew`
12. `cranc-uspres28-12-31-2026-hilcli`
13. `cranc-uspres28-12-31-2026-hunbid`
14. `cranc-uspres28-12-31-2026-jdvan`
15. `cranc-uspres28-12-31-2026-jonoss`
16. `cranc-uspres28-12-31-2026-jossha`
17. `cranc-uspres28-12-31-2026-kamhar` ← this one
18. `cranc-uspres28-12-31-2026-krinoe`
19. `cranc-uspres28-12-31-2026-margre`
20. `cranc-uspres28-12-31-2026-markel`
21. `cranc-uspres28-12-31-2026-marrub`
22. `cranc-uspres28-12-31-2026-micoba`
23. `cranc-uspres28-12-31-2026-nikhal`
24. `cranc-uspres28-12-31-2026-oprwin`
25. `cranc-uspres28-12-31-2026-petbut`
26. `cranc-uspres28-12-31-2026-rahema`
27. `cranc-uspres28-12-31-2026-robken`
28. `cranc-uspres28-12-31-2026-steban`
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5 @ 15¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 75 | ×0.2^0 = 75.0 |
|  | 18¢ | 28 | ×0.2^2 = 1.1 |
| ▶ | 15¢ | 5 (5 yours) | ×0.2^5 = 0.0 |
|  | 10¢ | 10 | ×0.2^10 = 0.0 |
|  | 5¢ | 50 | ×0.2^15 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^19 = 0.0 |
| | | **Σ** | **76.1** |

`yours 0.0 / Σ 76.1 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 5 @ 25¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 0 | ×0.2^0 = 0.0 |
|  | 19¢ | 112 | ×0.2^1 = 22.4 |
|  | 20¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 25¢ | 5 (5 yours) | ×0.2^7 = 0.0 |
|  | 30¢ | 10 | ×0.2^12 = 0.0 |
|  | 35¢ | 20 | ×0.2^17 = 0.0 |
|  | 40¢ | 40 | ×0.2^22 = 0.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,829 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^81 = 0.0 |
| | | **Σ** | **22.5** |

`yours 0.0 / Σ 22.5 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 5 @ 13¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 31 | ×0.2^0 = 31.2 |
|  | 9¢ | 3 | ×0.2^3 = 0.0 |
| ▶ | 13¢ | 5 (5 yours) | ×0.2^7 = 0.0 |
|  | 17¢ | 467 | ×0.2^11 = 0.0 |
|  | 40¢ | 29 | ×0.2^34 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **31.2** |

`yours 0.0 / Σ 31.2 = 0.0%`  
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
12. `scc-senate-gop-2026-11-03-gte57` ← this one
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 10 @ 30¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 1 | ×0.2^0 = 1.0 |
|  | 24¢ | 0 | ×0.2^4 = 0.0 |
|  | 25¢ | 5 | ×0.2^5 = 0.0 |
| ▶ | 30¢ | 10 (10 yours) | ×0.2^10 = 0.0 |
|  | 33¢ | 125 | ×0.2^13 = 0.0 |
|  | 35¢ | 15 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **1.0** |

`yours 0.0 / Σ 1.0 = 0.0%`  
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
11. `scc-senate-gop-2026-11-03-56` ← this one
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 5 @ 16¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 7 | ×0.2^0 = 7.4 |
|  | 11¢ | 3 | ×0.2^4 = 0.0 |
| ▶ | 16¢ | 5 (5 yours) | ×0.2^9 = 0.0 |
|  | 19¢ | 50 | ×0.2^12 = 0.0 |
|  | 20¢ | 100 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **7.4** |

`yours 0.0 / Σ 7.4 = 0.0%`  
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
| `cranc-uspres28-12-31-2026-tuccar` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,430 resting) | ~100.0% | ~$1.51 |
| `cranc-uspres28-12-31-2026-andyan` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (10,453 resting) | ~99.9% | ~$1.51 |
| `cranc-uspres28-12-31-2026-petbut` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,462 resting) | ~99.5% | ~$1.51 |
| `cranc-uspres28-12-31-2026-aleoca` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,499 resting) | ~99.2% | ~$1.50 |
| `cranc-uspres28-12-31-2026-margre` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (30,344 resting) | ~99.1% | ~$1.50 |
| `cranc-uspres28-12-31-2026-dontru` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,479 resting) | ~99.0% | ~$1.50 |
| `cranc-uspres28-12-31-2026-markel` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,505 resting) | ~98.8% | ~$1.50 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,500 resting) | ~98.8% | ~$1.50 |
| `cranc-uspres28-12-31-2026-marrub` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,500 resting) | ~98.6% | ~$1.49 |
| `cranc-uspres28-12-31-2026-robken` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (40,468 resting) | ~98.4% | ~$1.49 |
| `cranc-uspres28-12-31-2026-hunbid` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (30,284 resting) | ~98.4% | ~$1.49 |
| `cranc-uspres28-12-31-2026-gavnew` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (81,529 resting) | ~93.2% | ~$1.41 |

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
| 2026-07-30 2:56 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:50 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 12:52 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 10:36 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 8:06 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 5:45 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:45 AM ET | ❌ error | 1267 | $1321.41 |
| 2026-07-29 11:34 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:36 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:19 PM ET | ✅ ok | 1267 | $1321.41 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
