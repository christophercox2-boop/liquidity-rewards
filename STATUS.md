# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 7:06 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$108.10/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — BUY at the best price, ~$13.40/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$13.01/day), `apdc-jerpowgov-2026-08-31` (~$8.41/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$108.10/day (~$4.50/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 42.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~99.4% of bid side (11,001 resting ≥ 10,000 ✓) ≈ $4.14/day (pool ÷ 6 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 78.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~99.2% of bid side (12,134 resting ≥ 2,000 ✓) ≈ $6.20/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.8% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.49/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~89.9% of ask side (8,334 resting ≥ 5,000 ✓) ≈ $22.48/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (300,458 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~59.5% of bid side (140,435 resting ≥ 5,000 ✓) ≈ $2.29/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 22.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~50.0% of bid side (200,694 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 22.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~49.8% of bid side (5,571 resting ≥ 5,000 ✓) ≈ $12.45/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~41.2% of ask side (130,822 resting ≥ 2,000 ✓) ≈ $2.58/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~34.1% of ask side (16,434 resting ≥ 2,000 ✓) ≈ $2.13/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-dem` | BUY | 90.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~28.6% of bid side (512,735 resting ≥ 2,000 ✓) ≈ $1.78/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~27.9% of bid side (17,932 resting ≥ 2,000 ✓) ≈ $1.74/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | SELL | 25.0¢ | 18 | 0 | $50.00 | ✅ scoring — ~27.9% of ask side (11,048 resting ≥ 10,000 ✓) ≈ $3.48/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 3.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~21.9% of ask side (65,658 resting ≥ 2,000 ✓) ≈ $1.37/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 4,971 | 0 | $25.00 | ✅ scoring — ~18.1% of bid side (27,507 resting ≥ 2,000 ✓) ≈ $1.13/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 44.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~16.3% of ask side (82,320 resting ≥ 5,000 ✓) ≈ $0.68/day (pool ÷ 12 markets) |
| `ussewc-usse-or-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~14.5% of ask side (12,053 resting ≥ 2,000 ✓) ≈ $0.90/day (pool ÷ 2 markets) |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | BUY | 3.0¢ | 2,000 | 6 | $250.00 | ✅ scoring — ~14.3% of bid side (13,565 resting ≥ 5,000 ✓) ≈ $17.85/day |
| `vsc-usgubp-fl-fshbck-atl-30pct` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~13.9% of bid side (36,025 resting ≥ 5,000 ✓) ≈ $0.69/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 74.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~13.5% of bid side (500,336 resting ≥ 5,000 ✓) ≈ $0.56/day (pool ÷ 12 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 97.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~13.4% of ask side (22,535 resting ≥ 2,000 ✓) ≈ $0.84/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 2 | 2 | $100.00 | ✅ scoring — ~11.0% of bid side (50,580 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 13 markets) |
| `ussewc-usse-wv-2026-11-03-dem` | BUY | 1.0¢ | 1,400 | 0 | $25.00 | ✅ scoring — ~10.7% of bid side (13,100 resting ≥ 2,000 ✓) ≈ $0.67/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | SELL | 96.0¢ | 40 | 2 | $25.00 | ✅ scoring — ~8.5% of ask side (7,883 resting ≥ 2,000 ✓) ≈ $0.53/day (pool ÷ 2 markets) |
| `pntcbk-wnba-white-2027-06-30-roywhi` | BUY | 3.0¢ | 1,500 | 1 | $250.00 | ✅ scoring — ~7.8% of bid side (21,151 resting ≥ 5,000 ✓) ≈ $9.73/day |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~6.0% of bid side (500,868 resting ≥ 2,000 ✓) ≈ $0.37/day (pool ÷ 2 markets) |
| `ussewc-usse-ks-2026-11-03-rep` | BUY | 77.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~5.7% of bid side (510,653 resting ≥ 2,000 ✓) ≈ $0.35/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | SELL | 96.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~5.4% of ask side (15,419 resting ≥ 2,000 ✓) ≈ $0.34/day (pool ÷ 2 markets) |
| `dccc-measles-us-2026-12-31-gt3500` | BUY | 72.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~4.7% of bid side (10,950 resting ≥ 10,000 ✓) ≈ $0.19/day (pool ÷ 6 markets) |
| `ussewc-usse-ma-2026-11-03-rep` | BUY | 1.0¢ | 1,237 | 0 | $25.00 | ✅ scoring — ~4.6% of bid side (26,704 resting ≥ 2,000 ✓) ≈ $0.29/day (pool ÷ 2 markets) |
| …and 168 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>dccc-measles-us-2026-12-31-gt4500</code> BUY 10 @ 42¢ → $4.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 40¢ | 1 | ×0.25^2 = 0.1 |
|  | 19¢ | 110 | ×0.25^23 = 0.0 |
|  | 1¢ | 10,880 | ×0.25^41 = 0.0 |
| | | **Σ** | **10.1** |

`yours 10.0 / Σ 10.1 = 99.4%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 99.4% = $4.14/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500` ← this one
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 50 @ 78¢ → $6.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 77¢ | 4 | ×0.1^1 = 0.4 |
|  | 74¢ | 100 | ×0.1^4 = 0.0 |
|  | 8¢ | 30 | ×0.1^70 = 0.0 |
|  | 1¢ | 11,950 | ×0.1^77 = 0.0 |
| | | **Σ** | **50.4** |

`yours 50.0 / Σ 50.4 = 99.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.2% = $6.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 8 @ 9¢ → $3.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 8 (8 yours) | ×0.2^0 = 7.8 |
|  | 1¢ | 300,556 | ×0.2^8 = 0.8 |
| | | **Σ** | **8.5** |

`yours 7.8 / Σ 8.5 = 90.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 90.8% = $3.49/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 24¢ → $22.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 25¢ | 1 | ×0.2^1 = 0.2 |
|  | 26¢ | 23 | ×0.2^2 = 0.9 |
|  | 32¢ | 168 | ×0.2^8 = 0.0 |
|  | 38¢ | 80 | ×0.2^14 = 0.0 |
|  | 99¢ | 8,052 | ×0.2^75 = 0.0 |
| | | **Σ** | **11.1** |

`yours 10.0 / Σ 11.1 = 89.9%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 89.9% = $22.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 18 @ 12¢ → $2.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 27 (18 yours) | ×0.2^0 = 27.0 |
|  | 1¢ | 300,431 | ×0.2^11 = 0.0 |
| | | **Σ** | **27.0** |

`yours 18.0 / Σ 27.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 10 @ 8¢ → $2.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 1¢ | 140,420 | ×0.2^7 = 1.8 |
| | | **Σ** | **16.8** |

`yours 10.0 / Σ 16.8 = 59.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 59.5% = $2.29/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 40 @ 22¢ → $1.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 21¢ | 200 | ×0.2^1 = 40.0 |
|  | 10¢ | 45 | ×0.2^12 = 0.0 |
|  | 1¢ | 200,409 | ×0.2^21 = 0.0 |
| | | **Σ** | **80.0** |

`yours 40.0 / Σ 80.0 = 50.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 50.0% = $1.92/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 20 @ 22¢ → $12.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 4 | ×0.2^0 = 4.0 |
| ▶ | 22¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 20¢ | 1 | ×0.2^3 = 0.0 |
|  | 18¢ | 66 | ×0.2^5 = 0.0 |
|  | 14¢ | 6 | ×0.2^9 = 0.0 |
|  | 2¢ | 100 | ×0.2^21 = 0.0 |
|  | 1¢ | 5,374 | ×0.2^22 = 0.0 |
| | | **Σ** | **8.0** |

`yours 4.0 / Σ 8.0 = 49.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 49.8% = $12.45/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $2.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 97 (40 yours) | ×0.1^0 = 97.0 |
|  | 98¢ | 130,500 | ×0.1^94 = 0.0 |
| | | **Σ** | **97.0** |

`yours 40.0 / Σ 97.0 = 41.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 41.2% = $2.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $2.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 97 (40 yours) | ×0.1^0 = 97.0 |
|  | 97¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 16,297 | ×0.1^3 = 16.3 |
| | | **Σ** | **117.3** |

`yours 40.0 / Σ 117.3 = 34.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 34.1% = $2.13/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-dem</code> BUY 10 @ 90¢ → $1.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 35 (10 yours) | ×0.1^0 = 35.0 |
|  | 86¢ | 200 | ×0.1^4 = 0.0 |
|  | 84¢ | 2,000 | ×0.1^6 = 0.0 |
| | | **Σ** | **35.0** |

`yours 10.0 / Σ 35.0 = 28.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.6% = $1.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ny-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $1.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 17,932 (5,000 yours) | ×0.1^0 = 17,932.0 |
| | | **Σ** | **17,932.0** |

`yours 5,000.0 / Σ 17,932.0 = 27.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.9% = $1.74/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 18 @ 25¢ → $3.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 65 (18 yours) | ×0.25^0 = 65.2 |
|  | 33¢ | 100 | ×0.25^8 = 0.0 |
|  | 50¢ | 25 | ×0.25^25 = 0.0 |
|  | 99¢ | 10,857 | ×0.25^74 = 0.0 |
| | | **Σ** | **65.2** |

`yours 18.2 / Σ 65.2 = 27.9%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 27.9% = $3.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 3¢ → $1.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 183 (40 yours) | ×0.1^0 = 183.0 |
|  | 98¢ | 65,250 | ×0.1^95 = 0.0 |
| | | **Σ** | **183.0** |

`yours 40.0 / Σ 183.0 = 21.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 21.9% = $1.37/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> BUY 4,971 @ 1¢ → $1.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 27,507 (4,971 yours) | ×0.1^0 = 27,507.0 |
| | | **Σ** | **27,507.0** |

`yours 4,971.0 / Σ 27,507.0 = 18.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 18.1% = $1.13/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 8 @ 44¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 44¢ | 49 (8 yours) | ×0.2^0 = 49.0 |
|  | 98¢ | 80,046 | ×0.2^54 = 0.0 |
| | | **Σ** | **49.0** |

`yours 8.0 / Σ 49.0 = 16.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.3% = $0.68/day`  

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
<details><summary><code>ussewc-usse-or-2026-11-03-dem</code> SELL 40 @ 96¢ → $0.90/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 160 (40 yours) | ×0.1^0 = 160.0 |
|  | 98¢ | 11,668 | ×0.1^2 = 116.7 |
| | | **Σ** | **276.7** |

`yours 40.0 / Σ 276.7 = 14.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 14.5% = $0.90/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem` ← this one
2. `ussewc-usse-or-2026-11-03-rep`

</details>

</details>
<details><summary><code>pntcbk-wnba-freedom-2027-06-30-enekan</code> BUY 2,000 @ 3¢ → $17.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 434 | ×0.9^0 = 434.0 |
|  | 8¢ | 50 | ×0.9^1 = 45.0 |
|  | 7¢ | 51 | ×0.9^2 = 41.3 |
|  | 6¢ | 30 | ×0.9^3 = 21.9 |
|  | 5¢ | 800 | ×0.9^4 = 524.9 |
| ▶ | 3¢ | 12,000 (2,000 yours) | ×0.9^6 = 6,377.3 |
| | | **Σ** | **7,444.4** |

`yours 1,062.9 / Σ 7,444.4 = 14.3%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 14.3% = $17.85/day`  

</details>
<details><summary><code>vsc-usgubp-fl-fshbck-atl-30pct</code> BUY 5,000 @ 1¢ → $0.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 36,025 (5,000 yours) | ×0.2^0 = 36,025.0 |
| | | **Σ** | **36,025.0** |

`yours 5,000.0 / Σ 36,025.0 = 13.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 13.9% = $0.69/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vsc-usgubp-fl-fshbck-atl-11pct`
2. `vsc-usgubp-fl-fshbck-atl-13pct`
3. `vsc-usgubp-fl-fshbck-atl-15pct`
4. `vsc-usgubp-fl-fshbck-atl-17pct`
5. `vsc-usgubp-fl-fshbck-atl-19pct`
6. `vsc-usgubp-fl-fshbck-atl-21pct`
7. `vsc-usgubp-fl-fshbck-atl-30pct` ← this one
8. `vsc-usgubp-fl-fshbck-atl-5pct`
9. `vsc-usgubp-fl-fshbck-atl-7pct`
10. `vsc-usgubp-fl-fshbck-atl-9pct`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 17 @ 74¢ → $0.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 128 (17 yours) | ×0.2^0 = 128.4 |
|  | 1¢ | 500,208 | ×0.2^73 = 0.0 |
| | | **Σ** | **128.4** |

`yours 17.4 / Σ 128.4 = 13.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 13.5% = $0.56/day`  

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
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 97¢ → $0.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 98¢ | 105 | ×0.1^1 = 10.5 |
|  | 99¢ | 22,365 | ×0.1^2 = 223.6 |
| | | **Σ** | **299.1** |

`yours 40.0 / Σ 299.1 = 13.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 13.4% = $0.84/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 2 @ 15¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 15¢ | 18 (2 yours) | ×0.2^2 = 0.7 |
|  | 7¢ | 112 | ×0.2^10 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^15 = 0.0 |
| | | **Σ** | **0.7** |

`yours 0.1 / Σ 0.7 = 11.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.0% = $0.42/day`  

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
<details><summary><code>ussewc-usse-wv-2026-11-03-dem</code> BUY 1,400 @ 1¢ → $0.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 13,100 (1,400 yours) | ×0.1^0 = 13,100.0 |
| | | **Σ** | **13,100.0** |

`yours 1,400.0 / Σ 13,100.0 = 10.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 10.7% = $0.67/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wv-2026-11-03-dem` ← this one
2. `ussewc-usse-wv-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> SELL 40 @ 96¢ → $0.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 94¢ | 4 | ×0.1^0 = 4.0 |
|  | 95¢ | 2 | ×0.1^1 = 0.2 |
| ▶ | 96¢ | 40 (40 yours) | ×0.1^2 = 0.4 |
|  | 97¢ | 40 | ×0.1^3 = 0.0 |
|  | 99¢ | 7,797 | ×0.1^5 = 0.1 |
| | | **Σ** | **4.7** |

`yours 0.4 / Σ 4.7 = 8.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 8.5% = $0.53/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>pntcbk-wnba-white-2027-06-30-roywhi</code> BUY 1,500 @ 3¢ → $9.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 118 | ×0.9^0 = 118.2 |
| ▶ | 3¢ | 3,833 (1,500 yours) | ×0.9^1 = 3,450.0 |
|  | 2¢ | 17,000 | ×0.9^2 = 13,770.0 |
| | | **Σ** | **17,338.1** |

`yours 1,350.0 / Σ 17,338.1 = 7.8%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 7.8% = $9.73/day`  

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 95¢ → $0.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 668 (40 yours) | ×0.1^0 = 668.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **668.0** |

`yours 40.0 / Σ 668.0 = 6.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 6.0% = $0.37/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ks-2026-11-03-rep</code> BUY 20 @ 77¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 353 (20 yours) | ×0.1^0 = 353.0 |
|  | 73¢ | 100 | ×0.1^4 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^75 = 0.0 |
| | | **Σ** | **353.0** |

`yours 20.0 / Σ 353.0 = 5.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 5.7% = $0.35/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem`
2. `ussewc-usse-ks-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> SELL 35 @ 96¢ → $0.34/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 635 (35 yours) | ×0.1^0 = 635.0 |
|  | 99¢ | 14,784 | ×0.1^3 = 14.8 |
| | | **Σ** | **649.8** |

`yours 35.0 / Σ 649.8 = 5.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 5.4% = $0.34/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>dccc-measles-us-2026-12-31-gt3500</code> BUY 10 @ 72¢ → $0.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 72¢ | 214 (10 yours) | ×0.25^0 = 214.1 |
|  | 38¢ | 1 | ×0.25^34 = 0.0 |
|  | 1¢ | 10,735 | ×0.25^71 = 0.0 |
| | | **Σ** | **214.1** |

`yours 10.0 / Σ 214.1 = 4.7%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 4.7% = $0.19/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500` ← this one
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>ussewc-usse-ma-2026-11-03-rep</code> BUY 1,237 @ 1¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 26,704 (1,237 yours) | ×0.1^0 = 26,704.0 |
| | | **Σ** | **26,704.0** |

`yours 1,237.0 / Σ 26,704.0 = 4.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 4.6% = $0.29/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem`
2. `ussewc-usse-ma-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (48,541 resting) | ~17.9% | ~$13.40 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,693 resting) | ~17.3% | ~$13.01 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,502 resting) | ~33.6% | ~$8.41 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,002 resting) | ~28.3% | ~$7.07 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,267 resting) | ~24.7% | ~$6.17 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (65,635 resting) | ~8.1% | ~$6.06 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (293,828 resting) | ~7.3% | ~$5.44 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (523,714 resting) | ~6.6% | ~$4.98 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (134,776 resting) | ~15.9% | ~$3.97 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (688,749 resting) | ~4.4% | ~$3.32 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (644,936 resting) | ~4.1% | ~$3.10 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (102,255 resting) | ~45.5% | ~$2.84 |

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
| 2026-08-13 7:06 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:34 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:06 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 5:16 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 5:07 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 3:29 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 2:11 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 1:16 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 12:12 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 11:18 AM ET | ✅ ok | 2087 | $2853.72 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
