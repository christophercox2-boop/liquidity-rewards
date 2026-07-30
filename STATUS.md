# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-30 2:50 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$16.56/day estimated (ceiling, not promise — details below)

**Earned:** $1,321.41 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$0.32** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `cranc-uspres28-12-31-2026-tuccar` — SELL at the best price, ~$1.51/day for 200 contracts. Runners-up: `cranc-uspres28-12-31-2026-andyan` (~$1.51/day), `cranc-uspres28-12-31-2026-petbut` (~$1.51/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$16.56/day (~$0.69/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~99.4% of bid side (5,530 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 7.0¢ | 7 | 1 | $100.00 | ✅ scoring — ~99.3% of ask side (12,088 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 22.0¢ | 18 | 1 | $100.00 | ✅ scoring — ~97.7% of ask side (11,225 resting ≥ 5,000 ✓) ≈ $3.76/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 1.0¢ | 5,000 | 3 | $100.00 | ✅ scoring — ~77.2% of bid side (5,279 resting ≥ 5,000 ✓) ≈ $2.97/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 6.0¢ | 30 | 1 | $100.00 | ✅ scoring — ~14.7% of bid side (25,641 resting ≥ 5,000 ✓) ≈ $0.57/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 7.0¢ | 49 | 2 | $100.00 | ✅ scoring — ~14.5% of bid side (5,372 resting ≥ 5,000 ✓) ≈ $0.56/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 1.0¢ | 5,000 | 3 | $100.00 | ✅ scoring — ~14.4% of bid side (25,608 resting ≥ 5,000 ✓) ≈ $0.55/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 5.0¢ | 196 | 0 | $100.00 | ✅ scoring — ~8.2% of bid side (14,121 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 6.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~3.2% of ask side (11,636 resting ≥ 5,000 ✓) ≈ $0.12/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 1.0¢ | 5,000 | 6 | $100.00 | ✅ scoring — ~0.8% of bid side (25,641 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 42.0¢ | 50 | 4 | $100.00 | ✅ scoring — ~0.4% of ask side (12,081 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 48.0¢ | 50 | 4 | $100.00 | ✅ scoring — ~0.3% of ask side (12,081 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 20.0¢ | 1 | 2 | $100.00 | ✅ scoring — ~0.2% of ask side (12,118 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 1.0¢ | 5,000 | 8 | $100.00 | ✅ scoring — ~0.1% of bid side (5,372 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 9.0¢ | 3 | 3 | $100.00 | ✅ scoring — ~0.1% of ask side (11,636 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 11.0¢ | 3 | 5 | $100.00 | ✅ scoring — ~0.1% of ask side (12,088 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 10.0¢ | 20 | 6 | $100.00 | ✅ scoring — ~0.1% of bid side (5,530 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 15.0¢ | 5 | 4 | $100.00 | ✅ scoring — ~0.0% of bid side (5,615 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 4.0¢ | 4 | 1 | $100.00 | ✅ scoring — ~0.0% of bid side (13,901 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 15.0¢ | 5 | 5 | $100.00 | ✅ scoring — ~0.0% of bid side (5,342 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 25.0¢ | 5 | 7 | $100.00 | ✅ scoring — ~0.0% of ask side (12,118 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 13.0¢ | 5 | 7 | $100.00 | ✅ scoring — ~0.0% of ask side (11,636 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 5.0¢ | 50 | 11 | $100.00 | ✅ scoring — ~0.0% of bid side (5,530 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 16.0¢ | 5 | 10 | $100.00 | ✅ scoring — ~0.0% of ask side (12,088 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 10.0¢ | 10 | 9 | $100.00 | ✅ scoring — ~0.0% of bid side (5,615 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 10.0¢ | 10 | 10 | $100.00 | ✅ scoring — ~0.0% of bid side (5,342 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 1.0¢ | 5,000 | 15 | $100.00 | ✅ scoring — ~0.0% of bid side (5,530 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 17.0¢ | 100 | 11 | $100.00 | ✅ scoring — ~0.0% of ask side (11,636 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 19.0¢ | 50 | 13 | $100.00 | ✅ scoring — ~0.0% of ask side (12,088 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 30.0¢ | 10 | 12 | $100.00 | ✅ scoring — ~0.0% of ask side (12,118 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| …and 11 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 10 @ 15¢ → $3.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 15¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 10¢ | 20 | ×0.2^6 = 0.0 |
|  | 5¢ | 50 | ×0.2^11 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^15 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 99.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.4% = $3.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 7 @ 7¢ → $3.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 7¢ | 7 (7 yours) | ×0.2^1 = 1.5 |
|  | 11¢ | 3 | ×0.2^5 = 0.0 |
|  | 16¢ | 5 | ×0.2^10 = 0.0 |
|  | 19¢ | 50 | ×0.2^13 = 0.0 |
|  | 20¢ | 100 | ×0.2^14 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,822 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **1.5** |

`yours 1.5 / Σ 1.5 = 99.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.3% = $3.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 18 @ 22¢ → $3.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 22¢ | 18 (18 yours) | ×0.2^1 = 3.5 |
|  | 23¢ | 1 | ×0.2^2 = 0.0 |
|  | 26¢ | 100 | ×0.2^5 = 0.0 |
|  | 37¢ | 5 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **3.6** |

`yours 3.5 / Σ 3.6 = 97.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 97.7% = $3.76/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 5,000 @ 1¢ → $2.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 0 | ×0.2^0 = 0.0 |
|  | 3¢ | 50 | ×0.2^1 = 10.0 |
| ▶ | 1¢ | 5,229 (5,000 yours) | ×0.2^3 = 41.8 |
| | | **Σ** | **51.8** |

`yours 40.0 / Σ 51.8 = 77.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 77.2% = $2.97/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 49 @ 7¢ → $0.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
|  | 8¢ | 58 | ×0.2^1 = 11.6 |
| ▶ | 7¢ | 49 (49 yours) | ×0.2^2 = 2.0 |
|  | 1¢ | 5,265 | ×0.2^8 = 0.0 |
| | | **Σ** | **13.6** |

`yours 2.0 / Σ 13.6 = 14.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.5% = $0.56/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 5,000 @ 1¢ → $0.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 0 | ×0.2^0 = 0.0 |
|  | 3¢ | 383 | ×0.2^1 = 76.6 |
| ▶ | 1¢ | 25,225 (5,000 yours) | ×0.2^3 = 201.8 |
| | | **Σ** | **278.4** |

`yours 40.0 / Σ 278.4 = 14.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.4% = $0.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 196 @ 5¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 2,109 (196 yours) | ×0.2^0 = 2,109.0 |
|  | 3¢ | 6,833 | ×0.2^2 = 273.3 |
| | | **Σ** | **2,382.3** |

`yours 196.0 / Σ 2,382.3 = 8.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.2% = $0.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 50 @ 42¢ → $0.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 38¢ | 0 | ×0.2^0 = 0.0 |
|  | 39¢ | 111 | ×0.2^1 = 22.2 |
| ▶ | 42¢ | 50 (50 yours) | ×0.2^4 = 0.1 |
|  | 50¢ | 100 | ×0.2^12 = 0.0 |
|  | 98¢ | 1,819 | ×0.2^60 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^61 = 0.0 |
| | | **Σ** | **22.3** |

`yours 0.1 / Σ 22.3 = 0.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.4% = $0.01/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 48¢ → $0.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 44¢ | 0 | ×0.2^0 = 0.0 |
|  | 45¢ | 118 | ×0.2^1 = 23.6 |
| ▶ | 48¢ | 50 (50 yours) | ×0.2^4 = 0.1 |
|  | 50¢ | 100 | ×0.2^6 = 0.0 |
|  | 98¢ | 1,812 | ×0.2^54 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^55 = 0.0 |
| | | **Σ** | **23.7** |

`yours 0.1 / Σ 23.7 = 0.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.3% = $0.01/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 5,000 @ 1¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.0 |
|  | 8¢ | 58 | ×0.2^1 = 11.6 |
|  | 7¢ | 49 | ×0.2^2 = 2.0 |
| ▶ | 1¢ | 5,265 (5,000 yours) | ×0.2^8 = 0.0 |
| | | **Σ** | **13.6** |

`yours 0.0 / Σ 13.6 = 0.1%`  
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
|  | 6¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 7 | ×0.2^1 = 1.5 |
| ▶ | 11¢ | 3 (3 yours) | ×0.2^5 = 0.0 |
|  | 16¢ | 5 | ×0.2^10 = 0.0 |
|  | 19¢ | 50 | ×0.2^13 = 0.0 |
|  | 20¢ | 100 | ×0.2^14 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,822 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **1.5** |

`yours 0.0 / Σ 1.5 = 0.1%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 20 @ 10¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
|  | 15¢ | 10 | ×0.2^1 = 2.0 |
| ▶ | 10¢ | 20 (20 yours) | ×0.2^6 = 0.0 |
|  | 5¢ | 50 | ×0.2^11 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^15 = 0.0 |
| | | **Σ** | **2.0** |

`yours 0.0 / Σ 2.0 = 0.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.1% = $0.00/day`  

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
|  | 19¢ | 0 | ×0.2^0 = 0.0 |
|  | 18¢ | 105 | ×0.2^1 = 21.0 |
| ▶ | 15¢ | 5 (5 yours) | ×0.2^4 = 0.0 |
|  | 10¢ | 10 | ×0.2^9 = 0.0 |
|  | 5¢ | 20 | ×0.2^14 = 0.0 |
|  | 1¢ | 5,475 | ×0.2^18 = 0.0 |
| | | **Σ** | **21.0** |

`yours 0.0 / Σ 21.0 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 4 @ 4¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 1,865 | ×0.2^0 = 1,865.2 |
| ▶ | 4¢ | 4 (4 yours) | ×0.2^1 = 0.7 |
|  | 3¢ | 6,833 | ×0.2^2 = 273.3 |
| | | **Σ** | **2,139.2** |

`yours 0.7 / Σ 2,139.2 = 0.0%`  
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
|  | 20¢ | 2 | ×0.2^0 = 2.0 |
|  | 19¢ | 50 | ×0.2^1 = 10.0 |
| ▶ | 15¢ | 5 (5 yours) | ×0.2^5 = 0.0 |
|  | 10¢ | 10 | ×0.2^10 = 0.0 |
|  | 5¢ | 50 | ×0.2^15 = 0.0 |
|  | 1¢ | 5,225 | ×0.2^19 = 0.0 |
| | | **Σ** | **12.0** |

`yours 0.0 / Σ 12.0 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 50 @ 5¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
|  | 15¢ | 10 | ×0.2^1 = 2.0 |
|  | 10¢ | 20 | ×0.2^6 = 0.0 |
| ▶ | 5¢ | 50 (50 yours) | ×0.2^11 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^15 = 0.0 |
| | | **Σ** | **2.0** |

`yours 0.0 / Σ 2.0 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 5 @ 16¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 7 | ×0.2^1 = 1.5 |
|  | 11¢ | 3 | ×0.2^5 = 0.0 |
| ▶ | 16¢ | 5 (5 yours) | ×0.2^10 = 0.0 |
|  | 19¢ | 50 | ×0.2^13 = 0.0 |
|  | 20¢ | 100 | ×0.2^14 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,822 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **1.5** |

`yours 0.0 / Σ 1.5 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 10¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 0 | ×0.2^0 = 0.0 |
|  | 18¢ | 105 | ×0.2^1 = 21.0 |
|  | 15¢ | 5 | ×0.2^4 = 0.0 |
| ▶ | 10¢ | 10 (10 yours) | ×0.2^9 = 0.0 |
|  | 5¢ | 20 | ×0.2^14 = 0.0 |
|  | 1¢ | 5,475 | ×0.2^18 = 0.0 |
| | | **Σ** | **21.0** |

`yours 0.0 / Σ 21.0 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 10 @ 10¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 2 | ×0.2^0 = 2.0 |
|  | 19¢ | 50 | ×0.2^1 = 10.0 |
|  | 15¢ | 5 | ×0.2^5 = 0.0 |
| ▶ | 10¢ | 10 (10 yours) | ×0.2^10 = 0.0 |
|  | 5¢ | 50 | ×0.2^15 = 0.0 |
|  | 1¢ | 5,225 | ×0.2^19 = 0.0 |
| | | **Σ** | **12.0** |

`yours 0.0 / Σ 12.0 = 0.0%`  
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
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
|  | 15¢ | 10 | ×0.2^1 = 2.0 |
|  | 10¢ | 20 | ×0.2^6 = 0.0 |
|  | 5¢ | 50 | ×0.2^11 = 0.0 |
| ▶ | 1¢ | 5,450 (5,000 yours) | ×0.2^15 = 0.0 |
| | | **Σ** | **2.0** |

`yours 0.0 / Σ 2.0 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 100 @ 17¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 31 | ×0.2^0 = 31.2 |
|  | 9¢ | 3 | ×0.2^3 = 0.0 |
|  | 13¢ | 5 | ×0.2^7 = 0.0 |
| ▶ | 17¢ | 467 (100 yours) | ×0.2^11 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 50 @ 19¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 7 | ×0.2^1 = 1.5 |
|  | 11¢ | 3 | ×0.2^5 = 0.0 |
|  | 16¢ | 5 | ×0.2^10 = 0.0 |
| ▶ | 19¢ | 50 (50 yours) | ×0.2^13 = 0.0 |
|  | 20¢ | 100 | ×0.2^14 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,822 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **1.5** |

`yours 0.0 / Σ 1.5 = 0.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 10 @ 30¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 0 | ×0.2^0 = 0.0 |
|  | 19¢ | 112 | ×0.2^1 = 22.4 |
|  | 20¢ | 1 | ×0.2^2 = 0.0 |
|  | 25¢ | 5 | ×0.2^7 = 0.0 |
| ▶ | 30¢ | 10 (10 yours) | ×0.2^12 = 0.0 |
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
| `cranc-uspres28-12-31-2026-petbut` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,460 resting) | ~99.5% | ~$1.51 |
| `cranc-uspres28-12-31-2026-aleoca` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,499 resting) | ~99.2% | ~$1.50 |
| `cranc-uspres28-12-31-2026-margre` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (30,344 resting) | ~99.1% | ~$1.50 |
| `cranc-uspres28-12-31-2026-dontru` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,479 resting) | ~99.0% | ~$1.50 |
| `cranc-uspres28-12-31-2026-markel` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,344 resting) | ~98.5% | ~$1.49 |
| `cranc-uspres28-12-31-2026-robken` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (40,468 resting) | ~98.4% | ~$1.49 |
| `cranc-uspres28-12-31-2026-marrub` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (20,339 resting) | ~98.3% | ~$1.49 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,508 resting) | ~98.0% | ~$1.49 |
| `cranc-uspres28-12-31-2026-hunbid` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,504 resting) | ~97.7% | ~$1.48 |
| `cranc-uspres28-12-31-2026-rahema` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,357 resting) | ~97.6% | ~$1.48 |

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
| 2026-07-30 2:50 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 12:52 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 10:36 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 8:06 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 5:45 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:45 AM ET | ❌ error | 1267 | $1321.41 |
| 2026-07-29 11:34 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:36 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:19 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:18 PM ET | ✅ ok | 1267 | $1321.41 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
