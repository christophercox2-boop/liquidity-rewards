# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-30 4:37 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$23.85/day estimated (ceiling, not promise — details below)

**Earned:** $1,321.41 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$0.32** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — SELL at the best price, ~$10.96/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-angcra` (~$8.61/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$7.55/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$23.85/day (~$0.99/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | SELL | 22.0¢ | 18 | 1 | $100.00 | ✅ scoring — ~84.4% of ask side (12,025 resting ≥ 5,000 ✓) ≈ $3.25/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 10.0¢ | 49 | 2 | $100.00 | ✅ scoring — ~82.7% of bid side (5,316 resting ≥ 5,000 ✓) ≈ $3.18/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 7.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~68.2% of ask side (11,987 resting ≥ 5,000 ✓) ≈ $2.62/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 18.0¢ | 40 | 1 | $100.00 | ✅ scoring — ~55.5% of ask side (12,016 resting ≥ 5,000 ✓) ≈ $2.14/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~47.5% of ask side (12,094 resting ≥ 5,000 ✓) ≈ $1.83/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 14.0¢ | 45 | 0 | $100.00 | ✅ scoring — ~43.1% of ask side (12,312 resting ≥ 5,000 ✓) ≈ $1.66/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 7.0¢ | 53 | 0 | $100.00 | ✅ scoring — ~36.3% of ask side (12,133 resting ≥ 5,000 ✓) ≈ $1.39/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 41.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~34.2% of ask side (12,066 resting ≥ 5,000 ✓) ≈ $1.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 10.0¢ | 30 | 1 | $100.00 | ✅ scoring — ~23.1% of bid side (5,575 resting ≥ 5,000 ✓) ≈ $0.89/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 6.0¢ | 98 | 0 | $100.00 | ✅ scoring — ~22.1% of bid side (5,882 resting ≥ 5,000 ✓) ≈ $0.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~18.7% of bid side (26,687 resting ≥ 5,000 ✓) ≈ $0.72/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 5.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~18.2% of ask side (11,977 resting ≥ 5,000 ✓) ≈ $0.70/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~12.6% of bid side (39,827 resting ≥ 5,000 ✓) ≈ $0.48/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 4.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~10.7% of bid side (25,266 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 19.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~9.7% of bid side (5,310 resting ≥ 5,000 ✓) ≈ $0.37/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 87.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~5.9% of ask side (5,693 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 12 markets) |
| `ewc-usse-mi-2026-11-03-rep` | BUY | 29.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~4.3% of bid side (67,169 resting ≥ 2,000 ✓) ≈ $0.27/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~3.0% of bid side (5,619 resting ≥ 5,000 ✓) ≈ $0.12/day (pool ÷ 13 markets) |
| `enwc-ussep-mi-2026-08-04-dem-halste` | SELL | 8.0¢ | 100 | 0 | $300.00 | ✅ scoring — ~2.8% of ask side (148,008 resting ≥ 10,000 ✓) ≈ $1.39/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 5 | $100.00 | ✅ scoring — ~0.4% of bid side (5,882 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 6.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~0.2% of bid side (6,965 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 1.0¢ | 5,000 | 5 | $100.00 | ✅ scoring — ~0.1% of bid side (6,965 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 1.0¢ | 5,000 | 11 | $100.00 | ✅ scoring — ~0.0% of bid side (5,316 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 11.0¢ | 3 | 4 | $100.00 | ✅ scoring — ~0.0% of ask side (12,133 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 20.0¢ | 2 | 6 | $100.00 | ✅ scoring — ~0.0% of ask side (12,094 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 1.0¢ | 5,000 | 10 | $100.00 | ✅ scoring — ~0.0% of bid side (5,575 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 10.0¢ | 20 | 7 | $100.00 | ✅ scoring — ~0.0% of bid side (5,619 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 15.0¢ | 5 | 5 | $100.00 | ✅ scoring — ~0.0% of bid side (5,703 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 10.0¢ | 10 | 9 | $100.00 | ✅ scoring — ~0.0% of bid side (5,310 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 5,000 | 12 | $100.00 | ✅ scoring — ~0.0% of bid side (5,566 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| …and 15 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 18 @ 22¢ → $3.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 22¢ | 21 (18 yours) | ×0.2^1 = 4.1 |
|  | 24¢ | 1 | ×0.2^3 = 0.0 |
|  | 26¢ | 100 | ×0.2^5 = 0.0 |
|  | 37¢ | 5 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,797 | ×0.2^77 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 49 @ 10¢ → $3.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 0 | ×0.2^0 = 0.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
| ▶ | 10¢ | 49 (49 yours) | ×0.2^2 = 2.0 |
|  | 1¢ | 5,265 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.4** |

`yours 2.0 / Σ 2.4 = 82.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 82.7% = $3.18/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 15 @ 7¢ → $2.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 22 (15 yours) | ×0.2^0 = 22.0 |
|  | 40¢ | 29 | ×0.2^33 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,835 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **22.0** |

`yours 15.0 / Σ 22.0 = 68.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.2% = $2.62/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 40 @ 18¢ → $2.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 18¢ | 52 (40 yours) | ×0.2^1 = 10.4 |
|  | 19¢ | 100 | ×0.2^2 = 4.0 |
|  | 50¢ | 100 | ×0.2^33 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^81 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^82 = 0.0 |
| | | **Σ** | **14.4** |

`yours 8.0 / Σ 14.4 = 55.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.5% = $2.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 10 @ 15¢ → $1.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 15¢ | 21 (10 yours) | ×0.2^1 = 4.2 |
|  | 20¢ | 2 | ×0.2^6 = 0.0 |
|  | 22¢ | 100 | ×0.2^8 = 0.0 |
|  | 25¢ | 5 | ×0.2^11 = 0.0 |
|  | 30¢ | 5 | ×0.2^16 = 0.0 |
|  | 34¢ | 40 | ×0.2^20 = 0.0 |
|  | 50¢ | 100 | ×0.2^36 = 0.0 |
|  | 98¢ | 1,820 | ×0.2^84 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^85 = 0.0 |
| | | **Σ** | **4.2** |

`yours 2.0 / Σ 4.2 = 47.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.5% = $1.83/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 45 @ 14¢ → $1.66/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 92 (45 yours) | ×0.2^0 = 92.3 |
|  | 15¢ | 60 | ×0.2^1 = 12.0 |
|  | 22¢ | 93 | ×0.2^8 = 0.0 |
|  | 33¢ | 125 | ×0.2^19 = 0.0 |
|  | 35¢ | 15 | ×0.2^21 = 0.0 |
|  | 50¢ | 100 | ×0.2^36 = 0.0 |
|  | 98¢ | 1,826 | ×0.2^84 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^85 = 0.0 |
| | | **Σ** | **104.3** |

`yours 45.0 / Σ 104.3 = 43.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.1% = $1.66/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 53 @ 7¢ → $1.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 131 (53 yours) | ×0.2^0 = 130.6 |
|  | 8¢ | 84 | ×0.2^1 = 16.8 |
|  | 11¢ | 3 | ×0.2^4 = 0.0 |
|  | 16¢ | 5 | ×0.2^9 = 0.0 |
|  | 19¢ | 50 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **147.4** |

`yours 53.4 / Σ 147.4 = 36.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 36.3% = $1.39/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 50 @ 41¢ → $1.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 41¢ | 146 (50 yours) | ×0.2^0 = 146.0 |
|  | 50¢ | 100 | ×0.2^9 = 0.0 |
|  | 98¢ | 1,819 | ×0.2^57 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^58 = 0.0 |
| | | **Σ** | **146.0** |

`yours 50.0 / Σ 146.0 = 34.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.2% = $1.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 30 @ 10¢ → $0.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 10¢ | 130 (30 yours) | ×0.2^1 = 26.0 |
|  | 1¢ | 5,445 | ×0.2^10 = 0.0 |
| | | **Σ** | **26.0** |

`yours 6.0 / Σ 26.0 = 23.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 23.1% = $0.89/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 98 @ 6¢ → $0.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 432 (98 yours) | ×0.2^0 = 431.8 |
|  | 4¢ | 250 | ×0.2^2 = 10.0 |
|  | 1¢ | 5,200 | ×0.2^5 = 1.7 |
| | | **Σ** | **443.5** |

`yours 97.8 / Σ 443.5 = 22.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 22.1% = $0.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 5,000 @ 1¢ → $0.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 26,687 (5,000 yours) | ×0.2^0 = 26,687.0 |
| | | **Σ** | **26,687.0** |

`yours 5,000.0 / Σ 26,687.0 = 18.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.7% = $0.72/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 10 @ 5¢ → $0.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 55 (10 yours) | ×0.2^0 = 55.0 |
|  | 14¢ | 19 | ×0.2^9 = 0.0 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 98¢ | 1,802 | ×0.2^93 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^94 = 0.0 |
| | | **Σ** | **55.0** |

`yours 10.0 / Σ 55.0 = 18.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.2% = $0.70/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 5,000 @ 1¢ → $0.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 39,827 (5,000 yours) | ×0.2^0 = 39,827.0 |
| | | **Σ** | **39,827.0** |

`yours 5,000.0 / Σ 39,827.0 = 12.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 12.6% = $0.48/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 50 @ 4¢ → $0.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 260 (50 yours) | ×0.2^0 = 260.0 |
|  | 3¢ | 6 | ×0.2^1 = 1.2 |
|  | 2¢ | 251 | ×0.2^2 = 10.0 |
|  | 1¢ | 24,749 | ×0.2^3 = 198.0 |
| | | **Σ** | **469.2** |

`yours 50.0 / Σ 469.2 = 10.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 10.7% = $0.41/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5 @ 19¢ → $0.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 50 (5 yours) | ×0.2^0 = 50.4 |
|  | 17¢ | 29 | ×0.2^2 = 1.2 |
|  | 10¢ | 10 | ×0.2^9 = 0.0 |
|  | 5¢ | 20 | ×0.2^14 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^18 = 0.0 |
| | | **Σ** | **51.6** |

`yours 5.0 / Σ 51.6 = 9.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.7% = $0.37/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 87¢ → $0.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 850 (50 yours) | ×0.2^0 = 850.1 |
|  | 99¢ | 4,843 | ×0.2^12 = 0.0 |
| | | **Σ** | **850.1** |

`yours 50.0 / Σ 850.1 = 5.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.9% = $0.25/day`  

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
<details><summary><code>ewc-usse-mi-2026-11-03-rep</code> BUY 100 @ 29¢ → $0.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 1,261 (100 yours) | ×0.1^0 = 1,261.0 |
|  | 28¢ | 10,662 | ×0.1^1 = 1,066.2 |
| | | **Σ** | **2,327.2** |

`yours 100.0 / Σ 2,327.2 = 4.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 4.3% = $0.27/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-mi-2026-11-03-dem`
2. `ewc-usse-mi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 10 @ 15¢ → $0.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 0 | ×0.2^0 = 0.0 |
|  | 16¢ | 64 | ×0.2^1 = 12.7 |
| ▶ | 15¢ | 10 (10 yours) | ×0.2^2 = 0.4 |
|  | 10¢ | 20 | ×0.2^7 = 0.0 |
|  | 5¢ | 50 | ×0.2^12 = 0.0 |
|  | 1¢ | 5,475 | ×0.2^16 = 0.0 |
| | | **Σ** | **13.1** |

`yours 0.4 / Σ 13.1 = 3.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.0% = $0.12/day`  

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
<details><summary><code>enwc-ussep-mi-2026-08-04-dem-halste</code> SELL 100 @ 8¢ → $1.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 3,521 (100 yours) | ×0.2^0 = 3,521.0 |
|  | 10¢ | 26 | ×0.2^2 = 1.0 |
|  | 11¢ | 3,063 | ×0.2^3 = 24.5 |
|  | 12¢ | 38,000 | ×0.2^4 = 60.8 |
| | | **Σ** | **3,607.3** |

`yours 100.0 / Σ 3,607.3 = 2.8%`  
`$300 ÷ 3 ÷ 2 = $50.00 × 2.8% = $1.39/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `enwc-ussep-mi-2026-08-04-dem-abdels`
2. `enwc-ussep-mi-2026-08-04-dem-halste` ← this one
3. `enwc-ussep-mi-2026-08-04-dem-malmcm`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 432 | ×0.2^0 = 431.8 |
|  | 4¢ | 250 | ×0.2^2 = 10.0 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^5 = 1.7 |
| | | **Σ** | **443.5** |

`yours 1.6 / Σ 443.5 = 0.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.4% = $0.01/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 4 @ 6¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1,515 (4 yours) | ×0.2^0 = 1,514.5 |
|  | 4¢ | 250 | ×0.2^2 = 10.0 |
|  | 1¢ | 5,200 | ×0.2^5 = 1.7 |
| | | **Σ** | **1,526.2** |

`yours 3.5 / Σ 1,526.2 = 0.2%`  
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
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 1,515 | ×0.2^0 = 1,514.5 |
|  | 4¢ | 250 | ×0.2^2 = 10.0 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^5 = 1.7 |
| | | **Σ** | **1,526.2** |

`yours 1.6 / Σ 1,526.2 = 0.1%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 0 | ×0.2^0 = 0.0 |
|  | 11¢ | 2 | ×0.2^1 = 0.4 |
|  | 10¢ | 49 | ×0.2^2 = 2.0 |
| ▶ | 1¢ | 5,265 (5,000 yours) | ×0.2^11 = 0.0 |
| | | **Σ** | **2.4** |

`yours 0.0 / Σ 2.4 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 3 @ 11¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 131 | ×0.2^0 = 130.6 |
|  | 8¢ | 84 | ×0.2^1 = 16.8 |
| ▶ | 11¢ | 3 (3 yours) | ×0.2^4 = 0.0 |
|  | 16¢ | 5 | ×0.2^9 = 0.0 |
|  | 19¢ | 50 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **147.4** |

`yours 0.0 / Σ 147.4 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 2 @ 20¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 0 | ×0.2^0 = 0.0 |
|  | 15¢ | 21 | ×0.2^1 = 4.2 |
| ▶ | 20¢ | 2 (2 yours) | ×0.2^6 = 0.0 |
|  | 22¢ | 100 | ×0.2^8 = 0.0 |
|  | 25¢ | 5 | ×0.2^11 = 0.0 |
|  | 30¢ | 5 | ×0.2^16 = 0.0 |
|  | 34¢ | 40 | ×0.2^20 = 0.0 |
|  | 50¢ | 100 | ×0.2^36 = 0.0 |
|  | 98¢ | 1,820 | ×0.2^84 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^85 = 0.0 |
| | | **Σ** | **4.2** |

`yours 0.0 / Σ 4.2 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 0 | ×0.2^0 = 0.0 |
|  | 10¢ | 130 | ×0.2^1 = 26.0 |
| ▶ | 1¢ | 5,445 (5,000 yours) | ×0.2^10 = 0.0 |
| | | **Σ** | **26.0** |

`yours 0.0 / Σ 26.0 = 0.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 20 @ 10¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 0 | ×0.2^0 = 0.0 |
|  | 16¢ | 64 | ×0.2^1 = 12.7 |
|  | 15¢ | 10 | ×0.2^2 = 0.4 |
| ▶ | 10¢ | 20 (20 yours) | ×0.2^7 = 0.0 |
|  | 5¢ | 50 | ×0.2^12 = 0.0 |
|  | 1¢ | 5,475 | ×0.2^16 = 0.0 |
| | | **Σ** | **13.1** |

`yours 0.0 / Σ 13.1 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5 @ 15¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 382 | ×0.2^0 = 382.0 |
|  | 18¢ | 56 | ×0.2^2 = 2.2 |
| ▶ | 15¢ | 5 (5 yours) | ×0.2^5 = 0.0 |
|  | 10¢ | 10 | ×0.2^10 = 0.0 |
|  | 5¢ | 50 | ×0.2^15 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **384.2** |

`yours 0.0 / Σ 384.2 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 10¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 50 | ×0.2^0 = 50.4 |
|  | 17¢ | 29 | ×0.2^2 = 1.2 |
| ▶ | 10¢ | 10 (10 yours) | ×0.2^9 = 0.0 |
|  | 5¢ | 20 | ×0.2^14 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^18 = 0.0 |
| | | **Σ** | **51.6** |

`yours 0.0 / Σ 51.6 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 264 | ×0.2^0 = 264.0 |
|  | 11¢ | 45 | ×0.2^2 = 1.8 |
|  | 5¢ | 7 | ×0.2^8 = 0.0 |
|  | 4¢ | 50 | ×0.2^9 = 0.0 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^12 = 0.0 |
| | | **Σ** | **265.8** |

`yours 0.0 / Σ 265.8 = 0.0%`  
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
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (252,956 resting) | ~14.6% | ~$10.96 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,544 resting) | ~34.4% | ~$8.61 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (44,671 resting) | ~30.2% | ~$7.55 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (72,937 resting) | ~9.6% | ~$7.17 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (375,284 resting) | ~9.4% | ~$7.07 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (83,763 resting) | ~26.0% | ~$6.50 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (191,071 resting) | ~7.4% | ~$5.53 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (81,327 resting) | ~5.0% | ~$3.75 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,500 resting) | ~11.8% | ~$2.94 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (178,589 resting) | ~3.5% | ~$2.66 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $300.00 ÷ 3 | 0.20 | 10,000 | SELL side (54,132 resting) | ~4.9% | ~$2.44 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (88,805 resting) | ~2.6% | ~$1.96 |

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
| 2026-07-30 4:37 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:56 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:50 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 12:52 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 10:36 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 8:06 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 5:45 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:45 AM ET | ❌ error | 1267 | $1321.41 |
| 2026-07-29 11:34 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:36 PM ET | ✅ ok | 1267 | $1321.41 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
