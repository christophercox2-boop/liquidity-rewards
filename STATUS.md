# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 1:16 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$122.17/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$12.70/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$11.37/day), `ewc-usgub-ga-2026-11-03-dem` (~$10.70/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$122.17/day (~$5.09/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `apdc-jerpowgov-2026-12-31` | BUY | 20.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (5,501 resting ≥ 5,000 ✓) ≈ $24.99/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,549 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~91.0% of ask side (9,325 resting ≥ 5,000 ✓) ≈ $22.75/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.3% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.47/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~84.7% of bid side (140,539 resting ≥ 5,000 ✓) ≈ $3.26/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 14.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~64.0% of ask side (91,829 resting ≥ 5,000 ✓) ≈ $2.46/day (pool ÷ 13 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 42.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~61.2% of bid side (11,101 resting ≥ 10,000 ✓) ≈ $2.55/day (pool ÷ 6 markets) |
| `ussewc-usse-ks-2026-11-03-dem` | BUY | 30.0¢ | 16 | 1 | $25.00 | ✅ scoring — ~43.9% of bid side (3,053 resting ≥ 2,000 ✓) ≈ $2.74/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 1,300 | 0 | $25.00 | ✅ scoring — ~43.3% of bid side (3,000 resting ≥ 2,000 ✓) ≈ $2.71/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~36.6% of bid side (13,678 resting ≥ 2,000 ✓) ≈ $2.28/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 4,971 | 0 | $25.00 | ✅ scoring — ~29.8% of bid side (16,671 resting ≥ 2,000 ✓) ≈ $1.86/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | SELL | 25.0¢ | 19 | 0 | $50.00 | ✅ scoring — ~28.8% of ask side (11,048 resting ≥ 10,000 ✓) ≈ $3.60/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-dem` | BUY | 89.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~28.4% of bid side (512,799 resting ≥ 2,000 ✓) ≈ $1.77/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 90.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~16.7% of ask side (27,361 resting ≥ 2,000 ✓) ≈ $1.04/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 44.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~16.3% of ask side (82,370 resting ≥ 5,000 ✓) ≈ $0.68/day (pool ÷ 12 markets) |
| `pntcbk-wnba-white-2027-06-30-roywhi` | BUY | 3.0¢ | 1,500 | 1 | $250.00 | ✅ scoring — ~13.2% of bid side (42,114 resting ≥ 5,000 ✓) ≈ $16.54/day |
| `usgubewc-usgub-pa-2026-11-03-rep` | BUY | 1.0¢ | 1,600 | 0 | $25.00 | ✅ scoring — ~12.0% of bid side (13,300 resting ≥ 2,000 ✓) ≈ $0.75/day (pool ÷ 2 markets) |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | BUY | 3.0¢ | 2,000 | 6 | $250.00 | ✅ scoring — ~11.6% of bid side (20,151 resting ≥ 5,000 ✓) ≈ $14.45/day |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 2 | 2 | $100.00 | ✅ scoring — ~10.7% of bid side (50,570 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 13 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~10.4% of bid side (500,784 resting ≥ 2,000 ✓) ≈ $0.65/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~8.3% of ask side (20,127 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 97.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~8.1% of ask side (24,703 resting ≥ 2,000 ✓) ≈ $0.51/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | SELL | 97.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~6.9% of ask side (14,184 resting ≥ 2,000 ✓) ≈ $0.43/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 74.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~6.8% of bid side (500,766 resting ≥ 5,000 ✓) ≈ $0.28/day (pool ÷ 12 markets) |
| `ussewc-usse-or-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~6.8% of ask side (22,545 resting ≥ 2,000 ✓) ≈ $0.42/day (pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | BUY | 2.0¢ | 500 | 0 | $25.00 | ✅ scoring — ~6.8% of bid side (7,600 resting ≥ 2,000 ✓) ≈ $0.42/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | BUY | 11.0¢ | 40 | 1 | $25.00 | ✅ scoring — ~6.2% of bid side (10,670 resting ≥ 2,000 ✓) ≈ $0.38/day (pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | SELL | 10.0¢ | 92 | 0 | $100.00 | ✅ scoring — ~5.9% of ask side (12,606 resting ≥ 5,000 ✓) ≈ $1.49/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 3.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~5.7% of bid side (8,290 resting ≥ 5,000 ✓) ≈ $0.22/day (pool ÷ 13 markets) |
| `ussewc-usse-ks-2026-11-03-rep` | BUY | 77.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~5.2% of bid side (510,739 resting ≥ 2,000 ✓) ≈ $0.32/day (pool ÷ 2 markets) |
| …and 170 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 20 @ 20¢ → $24.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 19¢ | 0 | ×0.2^1 = 0.0 |
|  | 14¢ | 6 | ×0.2^6 = 0.0 |
|  | 12¢ | 116 | ×0.2^8 = 0.0 |
|  | 2¢ | 100 | ×0.2^18 = 0.0 |
|  | 1¢ | 5,258 | ×0.2^19 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 100.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 100.0% = $24.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 18 @ 12¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 18 (18 yours) | ×0.2^0 = 18.0 |
|  | 1¢ | 300,531 | ×0.2^11 = 0.0 |
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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 24¢ → $22.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 26¢ | 23 | ×0.2^2 = 0.9 |
|  | 29¢ | 208 | ×0.2^5 = 0.1 |
|  | 35¢ | 38 | ×0.2^11 = 0.0 |
|  | 42¢ | 50 | ×0.2^18 = 0.0 |
|  | 79¢ | 0 | ×0.2^55 = 0.0 |
|  | 99¢ | 8,996 | ×0.2^75 = 0.0 |
| | | **Σ** | **11.0** |

`yours 10.0 / Σ 11.0 = 91.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 91.0% = $22.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 10 @ 8¢ → $3.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 2¢ | 109 | ×0.2^6 = 0.0 |
|  | 1¢ | 140,420 | ×0.2^7 = 1.8 |
| | | **Σ** | **11.8** |

`yours 10.0 / Σ 11.8 = 84.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 84.7% = $3.26/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 14¢ → $2.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 15¢ | 14 | ×0.2^1 = 2.8 |
|  | 28¢ | 50 | ×0.2^14 = 0.0 |
|  | 50¢ | 100 | ×0.2^36 = 0.0 |
|  | 97¢ | 80,459 | ×0.2^83 = 0.0 |
| | | **Σ** | **7.8** |

`yours 5.0 / Σ 7.8 = 64.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.0% = $2.46/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt4500</code> BUY 10 @ 42¢ → $2.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 40¢ | 101 | ×0.25^2 = 6.3 |
|  | 38¢ | 4 | ×0.25^4 = 0.0 |
|  | 19¢ | 110 | ×0.25^23 = 0.0 |
|  | 1¢ | 10,876 | ×0.25^41 = 0.0 |
| | | **Σ** | **16.3** |

`yours 10.0 / Σ 16.3 = 61.2%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 61.2% = $2.55/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500` ← this one
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>ussewc-usse-ks-2026-11-03-dem</code> BUY 16 @ 30¢ → $2.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 31¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 30¢ | 16 (16 yours) | ×0.1^1 = 1.6 |
|  | 29¢ | 4 | ×0.1^2 = 0.0 |
|  | 27¢ | 50 | ×0.1^4 = 0.0 |
|  | 12¢ | 531 | ×0.1^19 = 0.0 |
|  | 7¢ | 250 | ×0.1^24 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^30 = 0.0 |
| | | **Σ** | **3.6** |

`yours 1.6 / Σ 3.6 = 43.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 43.9% = $2.74/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem` ← this one
2. `ussewc-usse-ks-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 1,300 @ 1¢ → $2.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,000 (1,300 yours) | ×0.1^0 = 3,000.0 |
| | | **Σ** | **3,000.0** |

`yours 1,300.0 / Σ 3,000.0 = 43.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 43.3% = $2.71/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $2.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 13,678 (5,000 yours) | ×0.1^0 = 13,678.0 |
| | | **Σ** | **13,678.0** |

`yours 5,000.0 / Σ 13,678.0 = 36.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 36.6% = $2.28/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> BUY 4,971 @ 1¢ → $1.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 16,671 (4,971 yours) | ×0.1^0 = 16,671.0 |
| | | **Σ** | **16,671.0** |

`yours 4,971.0 / Σ 16,671.0 = 29.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 29.8% = $1.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 19 @ 25¢ → $3.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 66 (19 yours) | ×0.25^0 = 66.0 |
|  | 34¢ | 149 | ×0.25^9 = 0.0 |
|  | 50¢ | 25 | ×0.25^25 = 0.0 |
|  | 99¢ | 10,807 | ×0.25^74 = 0.0 |
| | | **Σ** | **66.0** |

`yours 19.0 / Σ 66.0 = 28.8%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 28.8% = $3.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-dem</code> BUY 10 @ 89¢ → $1.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 35 (10 yours) | ×0.1^0 = 35.0 |
|  | 86¢ | 214 | ×0.1^3 = 0.2 |
|  | 85¢ | 50 | ×0.1^4 = 0.0 |
|  | 84¢ | 2,000 | ×0.1^5 = 0.0 |
| | | **Σ** | **35.2** |

`yours 10.0 / Σ 35.2 = 28.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.4% = $1.77/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ny-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> SELL 1 @ 90¢ → $1.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 6 (1 yours) | ×0.1^0 = 6.0 |
|  | 99¢ | 27,355 | ×0.1^9 = 0.0 |
| | | **Σ** | **6.0** |

`yours 1.0 / Σ 6.0 = 16.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 16.7% = $1.04/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 8 @ 44¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 44¢ | 49 (8 yours) | ×0.2^0 = 49.0 |
|  | 71¢ | 50 | ×0.2^27 = 0.0 |
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
<details><summary><code>pntcbk-wnba-white-2027-06-30-roywhi</code> BUY 1,500 @ 3¢ → $16.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 1,081 | ×0.9^0 = 1,081.2 |
| ▶ | 3¢ | 3,833 (1,500 yours) | ×0.9^1 = 3,450.0 |
|  | 2¢ | 7,000 | ×0.9^2 = 5,670.0 |
| | | **Σ** | **10,201.1** |

`yours 1,350.0 / Σ 10,201.1 = 13.2%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 13.2% = $16.54/day`  

</details>
<details><summary><code>usgubewc-usgub-pa-2026-11-03-rep</code> BUY 1,600 @ 1¢ → $0.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 13,300 (1,600 yours) | ×0.1^0 = 13,300.0 |
| | | **Σ** | **13,300.0** |

`yours 1,600.0 / Σ 13,300.0 = 12.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 12.0% = $0.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem`
2. `usgubewc-usgub-pa-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>pntcbk-wnba-freedom-2027-06-30-enekan</code> BUY 2,000 @ 3¢ → $14.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 2,250 | ×0.9^0 = 2,250.1 |
|  | 8¢ | 50 | ×0.9^1 = 45.0 |
|  | 7¢ | 621 | ×0.9^2 = 503.0 |
|  | 4¢ | 30 | ×0.9^5 = 17.7 |
| ▶ | 3¢ | 12,000 (2,000 yours) | ×0.9^6 = 6,377.3 |
| | | **Σ** | **9,193.1** |

`yours 1,062.9 / Σ 9,193.1 = 11.6%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 11.6% = $14.45/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 2 @ 15¢ → $0.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 15¢ | 18 (2 yours) | ×0.2^2 = 0.7 |
|  | 2¢ | 50,250 | ×0.2^15 = 0.0 |
| | | **Σ** | **0.8** |

`yours 0.1 / Σ 0.8 = 10.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 10.7% = $0.41/day`  

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
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 95¢ → $0.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 384 (40 yours) | ×0.1^0 = 384.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **384.0** |

`yours 40.0 / Σ 384.0 = 10.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 10.4% = $0.65/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> SELL 40 @ 96¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 240 (40 yours) | ×0.1^0 = 240.0 |
|  | 97¢ | 1,373 | ×0.1^1 = 137.3 |
|  | 98¢ | 10,654 | ×0.1^2 = 106.5 |
| | | **Σ** | **483.9** |

`yours 40.0 / Σ 483.9 = 8.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 8.3% = $0.52/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 97¢ → $0.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 240 (40 yours) | ×0.1^0 = 240.0 |
|  | 98¢ | 105 | ×0.1^1 = 10.5 |
|  | 99¢ | 24,358 | ×0.1^2 = 243.6 |
| | | **Σ** | **494.1** |

`yours 40.0 / Σ 494.1 = 8.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 8.1% = $0.51/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> SELL 35 @ 97¢ → $0.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 235 (35 yours) | ×0.1^0 = 234.9 |
|  | 98¢ | 1,472 | ×0.1^1 = 147.2 |
|  | 99¢ | 12,477 | ×0.1^2 = 124.8 |
| | | **Σ** | **506.8** |

`yours 34.9 / Σ 506.8 = 6.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 6.9% = $0.43/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 18 @ 74¢ → $0.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 184 (18 yours) | ×0.2^0 = 183.6 |
|  | 73¢ | 374 | ×0.2^1 = 74.8 |
|  | 1¢ | 500,208 | ×0.2^73 = 0.0 |
| | | **Σ** | **258.4** |

`yours 17.6 / Σ 258.4 = 6.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 6.8% = $0.28/day`  

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
<details><summary><code>ussewc-usse-or-2026-11-03-dem</code> SELL 40 @ 96¢ → $0.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 440 (40 yours) | ×0.1^0 = 440.0 |
|  | 98¢ | 14,887 | ×0.1^2 = 148.9 |
| | | **Σ** | **588.9** |

`yours 40.0 / Σ 588.9 = 6.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 6.8% = $0.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem` ← this one
2. `ussewc-usse-or-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> BUY 500 @ 2¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 7,400 (500 yours) | ×0.1^0 = 7,400.0 |
| | | **Σ** | **7,400.0** |

`yours 500.0 / Σ 7,400.0 = 6.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 6.8% = $0.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> BUY 40 @ 11¢ → $0.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 60 | ×0.1^0 = 60.0 |
| ▶ | 11¢ | 40 (40 yours) | ×0.1^1 = 4.0 |
|  | 10¢ | 71 | ×0.1^2 = 0.7 |
|  | 9¢ | 299 | ×0.1^3 = 0.3 |
|  | 1¢ | 10,200 | ×0.1^11 = 0.0 |
| | | **Σ** | **65.0** |

`yours 4.0 / Σ 65.0 = 6.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 6.2% = $0.38/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> SELL 92 @ 10¢ → $1.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1,137 (92 yours) | ×0.2^0 = 1,137.1 |
|  | 11¢ | 2,023 | ×0.2^1 = 404.6 |
|  | 13¢ | 747 | ×0.2^3 = 6.0 |
|  | 14¢ | 790 | ×0.2^4 = 1.3 |
|  | 16¢ | 1,949 | ×0.2^6 = 0.1 |
| | | **Σ** | **1,549.1** |

`yours 92.1 / Σ 1,549.1 = 5.9%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 5.9% = $1.49/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 100 @ 3¢ → $0.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 733 (100 yours) | ×0.2^0 = 733.0 |
|  | 2¢ | 5,167 | ×0.2^1 = 1,033.4 |
| | | **Σ** | **1,766.4** |

`yours 100.0 / Σ 1,766.4 = 5.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.7% = $0.22/day`  

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
<details><summary><code>ussewc-usse-ks-2026-11-03-rep</code> BUY 20 @ 77¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 388 (20 yours) | ×0.1^0 = 388.0 |
|  | 73¢ | 151 | ×0.1^4 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^75 = 0.0 |
| | | **Σ** | **388.0** |

`yours 20.0 / Σ 388.0 = 5.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 5.2% = $0.32/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem`
2. `ussewc-usse-ks-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (29,013 resting) | ~50.8% | ~$12.70 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (64,525 resting) | ~15.2% | ~$11.37 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (83,388 resting) | ~14.3% | ~$10.70 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,029 resting) | ~27.2% | ~$6.80 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (282,169 resting) | ~6.3% | ~$4.73 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (396,283 resting) | ~6.1% | ~$4.57 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (294,591 resting) | ~5.6% | ~$4.23 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (10,615 resting) | ~8.2% | ~$4.09 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (164,008 resting) | ~5.3% | ~$3.97 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,564 resting) | ~14.4% | ~$3.61 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (688,579 resting) | ~3.8% | ~$2.86 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (646,209 resting) | ~3.6% | ~$2.71 |

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
| 2026-08-13 1:16 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 12:12 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 11:18 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 9:52 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 8:02 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 7:51 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:31 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 4:46 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 2:50 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 1:11 AM ET | ✅ ok | 2087 | $2853.72 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
