# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 11:18 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$239.83/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$11.64/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$11.25/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$10.27/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$239.83/day (~$9.99/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,449 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 90.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (27,302 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 17.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~99.5% of ask side (71,619 resting ≥ 2,000 ✓) ≈ $6.22/day (pool ÷ 2 markets) |
| `dccc-measles-us-2026-12-31-gt3000` | BUY | 82.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~99.0% of bid side (10,270 resting ≥ 10,000 ✓) ≈ $4.13/day (pool ÷ 6 markets) |
| `usgubewc-usgub-ny-2026-11-03-dem` | BUY | 89.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~98.8% of bid side (502,675 resting ≥ 2,000 ✓) ≈ $6.17/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-rep` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~93.0% of ask side (65,518 resting ≥ 2,000 ✓) ≈ $5.81/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.3% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.47/day (pool ÷ 13 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 3.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~89.1% of ask side (66,096 resting ≥ 2,000 ✓) ≈ $5.57/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~84.8% of bid side (140,540 resting ≥ 5,000 ✓) ≈ $3.26/day (pool ÷ 13 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (510,250 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | SELL | 3.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~76.9% of ask side (130,777 resting ≥ 2,000 ✓) ≈ $4.81/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~75.5% of ask side (208,341 resting ≥ 2,000 ✓) ≈ $4.72/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~75.5% of ask side (130,778 resting ≥ 2,000 ✓) ≈ $4.72/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~74.1% of ask side (208,342 resting ≥ 2,000 ✓) ≈ $4.63/day (pool ÷ 2 markets) |
| `ussewc-usse-ks-2026-11-03-dem` | BUY | 28.0¢ | 16 | 0 | $25.00 | ✅ scoring — ~69.6% of bid side (3,049 resting ≥ 2,000 ✓) ≈ $4.35/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | SELL | 9.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~69.0% of ask side (7,233 resting ≥ 2,000 ✓) ≈ $2.87/day (pool ÷ 3 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~65.6% of ask side (72,205 resting ≥ 2,000 ✓) ≈ $4.10/day (pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-dem` | SELL | 8.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~58.1% of ask side (272,680 resting ≥ 2,000 ✓) ≈ $3.63/day (pool ÷ 2 markets) |
| `ussewc-usse-co-2026-11-03-rep` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~58.1% of ask side (59,199 resting ≥ 2,000 ✓) ≈ $3.63/day (pool ÷ 2 markets) |
| `ussewc-usse-fl-2026-11-03-rep` | BUY | 87.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~51.5% of bid side (510,335 resting ≥ 2,000 ✓) ≈ $3.22/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~48.8% of bid side (510,282 resting ≥ 2,000 ✓) ≈ $3.05/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~48.8% of bid side (500,282 resting ≥ 2,000 ✓) ≈ $3.05/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | BUY | 11.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~48.7% of bid side (11,097 resting ≥ 2,000 ✓) ≈ $3.04/day (pool ÷ 2 markets) |
| `usgubewc-usgub-pa-2026-11-03-rep` | BUY | 1.0¢ | 1,600 | 0 | $25.00 | ✅ scoring — ~48.5% of bid side (3,300 resting ≥ 2,000 ✓) ≈ $3.03/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~45.9% of bid side (10,890 resting ≥ 2,000 ✓) ≈ $2.87/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-rep` | SELL | 9.0¢ | 40 | 1 | $25.00 | ✅ scoring — ~45.5% of ask side (199,452 resting ≥ 2,000 ✓) ≈ $2.84/day (pool ÷ 2 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 42.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~42.9% of bid side (11,108 resting ≥ 10,000 ✓) ≈ $1.79/day (pool ÷ 6 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~42.1% of bid side (2,045 resting ≥ 2,000 ✓) ≈ $2.63/day (pool ÷ 2 markets) |
| `usgubewc-usgub-sd-2026-11-03-rep` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~41.7% of bid side (2,031 resting ≥ 2,000 ✓) ≈ $2.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~41.2% of bid side (610,297 resting ≥ 2,000 ✓) ≈ $2.58/day (pool ÷ 2 markets) |
| …and 380 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 18 @ 12¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 18 (18 yours) | ×0.2^0 = 18.0 |
|  | 1¢ | 300,431 | ×0.2^11 = 0.0 |
| | | **Σ** | **18.0** |

`yours 18.0 / Σ 18.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.84/day`  

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
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> SELL 1 @ 90¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 96¢ | 400 | ×0.1^6 = 0.0 |
|  | 99¢ | 26,901 | ×0.1^9 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 10 @ 17¢ → $6.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 20¢ | 50 | ×0.1^3 = 0.1 |
|  | 98¢ | 65,250 | ×0.1^81 = 0.0 |
| | | **Σ** | **10.1** |

`yours 10.0 / Σ 10.1 = 99.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.5% = $6.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>dccc-measles-us-2026-12-31-gt3000</code> BUY 20 @ 82¢ → $4.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 20 (20 yours) | ×0.25^0 = 20.0 |
|  | 78¢ | 50 | ×0.25^4 = 0.2 |
|  | 1¢ | 10,200 | ×0.25^81 = 0.0 |
| | | **Σ** | **20.2** |

`yours 20.0 / Σ 20.2 = 99.0%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 99.0% = $4.13/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000` ← this one
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-dem</code> BUY 10 @ 89¢ → $6.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 86¢ | 100 | ×0.1^3 = 0.1 |
|  | 85¢ | 50 | ×0.1^4 = 0.0 |
|  | 84¢ | 2,000 | ×0.1^5 = 0.0 |
| | | **Σ** | **10.1** |

`yours 10.0 / Σ 10.1 = 98.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.8% = $6.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ny-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> SELL 40 @ 5¢ → $5.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 43 (40 yours) | ×0.1^0 = 43.0 |
|  | 98¢ | 65,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **43.0** |

`yours 40.0 / Σ 43.0 = 93.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.0% = $5.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem`
2. `usgubewc-usgub-me-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 8 @ 9¢ → $3.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 8 (8 yours) | ×0.2^0 = 7.8 |
|  | 1¢ | 300,556 | ×0.2^8 = 0.8 |
| | | **Σ** | **8.6** |

`yours 7.8 / Σ 8.6 = 90.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 90.3% = $3.47/day`  

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 3¢ → $5.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 42 (40 yours) | ×0.1^0 = 42.0 |
|  | 4¢ | 29 | ×0.1^1 = 2.9 |
|  | 9¢ | 50 | ×0.1^6 = 0.0 |
|  | 98¢ | 65,750 | ×0.1^95 = 0.0 |
| | | **Σ** | **44.9** |

`yours 40.0 / Σ 44.9 = 89.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.1% = $5.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 10 @ 8¢ → $3.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 1¢ | 140,530 | ×0.2^7 = 1.8 |
| | | **Σ** | **11.8** |

`yours 10.0 / Σ 11.8 = 84.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 84.8% = $3.26/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> SELL 40 @ 3¢ → $4.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 52 (40 yours) | ×0.1^0 = 52.0 |
|  | 98¢ | 130,500 | ×0.1^95 = 0.0 |
| | | **Σ** | **52.0** |

`yours 40.0 / Σ 52.0 = 76.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 76.9% = $4.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> SELL 40 @ 4¢ → $4.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 53 (40 yours) | ×0.1^0 = 53.0 |
|  | 98¢ | 208,063 | ×0.1^94 = 0.0 |
| | | **Σ** | **53.0** |

`yours 40.0 / Σ 53.0 = 75.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.5% = $4.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $4.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 53 (40 yours) | ×0.1^0 = 53.0 |
|  | 98¢ | 130,500 | ×0.1^94 = 0.0 |
| | | **Σ** | **53.0** |

`yours 40.0 / Σ 53.0 = 75.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.5% = $4.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> SELL 40 @ 5¢ → $4.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 54 (40 yours) | ×0.1^0 = 54.0 |
|  | 98¢ | 208,063 | ×0.1^93 = 0.0 |
| | | **Σ** | **54.0** |

`yours 40.0 / Σ 54.0 = 74.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 74.1% = $4.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ks-2026-11-03-dem</code> BUY 16 @ 28¢ → $4.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 18 (16 yours) | ×0.1^0 = 18.0 |
|  | 27¢ | 50 | ×0.1^1 = 5.0 |
|  | 12¢ | 531 | ×0.1^16 = 0.0 |
|  | 7¢ | 250 | ×0.1^21 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^27 = 0.0 |
| | | **Σ** | **23.0** |

`yours 16.0 / Σ 23.0 = 69.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 69.6% = $4.35/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem` ← this one
2. `ussewc-usse-ks-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> SELL 40 @ 9¢ → $2.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 58 (40 yours) | ×0.1^0 = 58.0 |
|  | 13¢ | 50 | ×0.1^4 = 0.0 |
|  | 99¢ | 7,125 | ×0.1^90 = 0.0 |
| | | **Σ** | **58.0** |

`yours 40.0 / Σ 58.0 = 69.0%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 69.0% = $2.87/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 40 @ 10¢ → $4.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 61 (40 yours) | ×0.1^0 = 61.0 |
|  | 98¢ | 65,250 | ×0.1^88 = 0.0 |
| | | **Σ** | **61.0** |

`yours 40.0 / Σ 61.0 = 65.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 65.6% = $4.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-dem</code> SELL 50 @ 8¢ → $3.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 86 (50 yours) | ×0.1^0 = 86.0 |
|  | 98¢ | 265,567 | ×0.1^90 = 0.0 |
| | | **Σ** | **86.0** |

`yours 50.0 / Σ 86.0 = 58.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.1% = $3.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem` ← this one
2. `ussewc-usse-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-co-2026-11-03-rep</code> SELL 50 @ 7¢ → $3.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 86 (50 yours) | ×0.1^0 = 86.0 |
|  | 98¢ | 58,888 | ×0.1^91 = 0.0 |
| | | **Σ** | **86.0** |

`yours 50.0 / Σ 86.0 = 58.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.1% = $3.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem`
2. `ussewc-usse-co-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-fl-2026-11-03-rep</code> BUY 30 @ 87¢ → $3.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 58 (30 yours) | ×0.1^0 = 58.0 |
|  | 86¢ | 2 | ×0.1^1 = 0.2 |
|  | 76¢ | 50 | ×0.1^11 = 0.0 |
|  | 40¢ | 25 | ×0.1^47 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **58.2** |

`yours 30.0 / Σ 58.2 = 51.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 51.5% = $3.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem`
2. `ussewc-usse-fl-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> BUY 40 @ 95¢ → $3.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 82 (40 yours) | ×0.1^0 = 82.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **82.0** |

`yours 40.0 / Σ 82.0 = 48.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 48.8% = $3.05/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-dem</code> BUY 40 @ 95¢ → $3.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 82 (40 yours) | ×0.1^0 = 82.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **82.0** |

`yours 40.0 / Σ 82.0 = 48.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 48.8% = $3.05/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem` ← this one
2. `usgubewc-usgub-me-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> BUY 40 @ 11¢ → $3.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 67 (40 yours) | ×0.1^0 = 67.0 |
|  | 10¢ | 121 | ×0.1^1 = 12.1 |
|  | 9¢ | 309 | ×0.1^2 = 3.1 |
|  | 4¢ | 400 | ×0.1^7 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^10 = 0.0 |
| | | **Σ** | **82.2** |

`yours 40.0 / Σ 82.2 = 48.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 48.7% = $3.04/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-pa-2026-11-03-rep</code> BUY 1,600 @ 1¢ → $3.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,300 (1,600 yours) | ×0.1^0 = 3,300.0 |
| | | **Σ** | **3,300.0** |

`yours 1,600.0 / Σ 3,300.0 = 48.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 48.5% = $3.03/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem`
2. `usgubewc-usgub-pa-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $2.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 10,890 (5,000 yours) | ×0.1^0 = 10,890.0 |
| | | **Σ** | **10,890.0** |

`yours 5,000.0 / Σ 10,890.0 = 45.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 45.9% = $2.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-rep</code> SELL 40 @ 9¢ → $2.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 4 | ×0.1^0 = 4.0 |
| ▶ | 9¢ | 48 (40 yours) | ×0.1^1 = 4.8 |
|  | 98¢ | 199,175 | ×0.1^90 = 0.0 |
| | | **Σ** | **8.8** |

`yours 4.0 / Σ 8.8 = 45.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 45.5% = $2.84/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem`
2. `usgubewc-usgub-ct-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>dccc-measles-us-2026-12-31-gt4500</code> BUY 10 @ 42¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 17 (10 yours) | ×0.25^0 = 17.0 |
|  | 40¢ | 101 | ×0.25^2 = 6.3 |
|  | 38¢ | 4 | ×0.25^4 = 0.0 |
|  | 15¢ | 110 | ×0.25^27 = 0.0 |
|  | 1¢ | 10,876 | ×0.25^41 = 0.0 |
| | | **Σ** | **23.3** |

`yours 10.0 / Σ 23.3 = 42.9%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 42.9% = $1.79/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500` ← this one
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 40 @ 95¢ → $2.63/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 95 (40 yours) | ×0.1^0 = 95.0 |
|  | 1¢ | 1,950 | ×0.1^94 = 0.0 |
| | | **Σ** | **95.0** |

`yours 40.0 / Σ 95.0 = 42.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 42.1% = $2.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-sd-2026-11-03-rep</code> BUY 40 @ 95¢ → $2.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 96 (40 yours) | ×0.1^0 = 96.0 |
|  | 1¢ | 1,935 | ×0.1^94 = 0.0 |
| | | **Σ** | **96.0** |

`yours 40.0 / Σ 96.0 = 41.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 41.7% = $2.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sd-2026-11-03-dem`
2. `usgubewc-usgub-sd-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-co-2026-11-03-dem</code> BUY 40 @ 95¢ → $2.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 97 (40 yours) | ×0.1^0 = 97.0 |
|  | 2¢ | 600,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **97.0** |

`yours 40.0 / Σ 97.0 = 41.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 41.2% = $2.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem` ← this one
2. `usgubewc-usgub-co-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (29,200 resting) | ~46.6% | ~$11.64 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (64,325 resting) | ~15.0% | ~$11.25 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,325 resting) | ~41.1% | ~$10.27 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (82,829 resting) | ~9.3% | ~$7.01 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,037,661 resting) | ~7.7% | ~$5.78 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,082,892 resting) | ~6.3% | ~$4.75 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (292,835 resting) | ~6.1% | ~$4.59 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,434 resting) | ~14.5% | ~$3.62 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (818,725 resting) | ~4.7% | ~$3.53 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,655 resting) | ~4.6% | ~$3.45 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (688,803 resting) | ~3.3% | ~$2.46 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,045,780 resting) | ~3.2% | ~$2.37 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $964.28 |
| Skipped | $1.41 |
| **Total earned** | **$2,853.72** |

2087 reward rows · 40 days with rewards · 480 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-11 ⚠️ multi-day pending bucket | $406.66 | `███████████████` |
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
| 2026-07-30 | $20.67 | `█` |
| 2026-07-29 | $53.60 | `██` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $1,390.40 | `███████████████████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $107.37 |
| `apdc-alito-2026-12-31` | $106.43 |
| `opdc-mcconnell-resign-2026-11-02` | $70.72 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `pandc-anydis-2027-12-31` | $39.99 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.02 |
| `scc-hrep-rep-2026-11-03-gte200` | $38.44 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-13 11:18 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 9:52 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 8:02 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 7:51 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:31 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 4:46 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 2:50 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 1:11 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-12 11:02 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-12 9:32 PM ET | ✅ ok | 2087 | $2853.72 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
