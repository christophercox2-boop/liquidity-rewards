# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 5:07 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$108.68/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — BUY at the best price, ~$20.24/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$11.76/day), `ewc-usgub-ga-2026-11-03-dem` (~$11.15/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$108.68/day (~$4.53/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `dccc-measles-us-2026-12-31-gt3500` | BUY | 72.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~100.0% of bid side (11,204 resting ≥ 10,000 ✓) ≈ $4.17/day (pool ÷ 6 markets) |
| `pandc-anydis-2027-12-31` | SELL | 25.0¢ | 18 | 0 | $50.00 | ✅ scoring — ~100.0% of ask side (11,001 resting ≥ 10,000 ✓) ≈ $12.50/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,449 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.3% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.47/day (pool ÷ 13 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~89.3% of bid side (5,600 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~88.6% of bid side (100,430 resting ≥ 5,000 ✓) ≈ $3.41/day (pool ÷ 13 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~62.7% of ask side (9,927 resting ≥ 2,000 ✓) ≈ $3.92/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.5% of ask side (130,790 resting ≥ 2,000 ✓) ≈ $3.85/day (pool ÷ 2 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 42.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~61.2% of bid side (11,105 resting ≥ 10,000 ✓) ≈ $2.55/day (pool ÷ 6 markets) |
| `vsc-usgubp-fl-fshbck-atl-30pct` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~60.3% of bid side (8,291 resting ≥ 5,000 ✓) ≈ $3.02/day (pool ÷ 10 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 3.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~58.8% of ask side (65,543 resting ≥ 2,000 ✓) ≈ $3.68/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 16.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~51.5% of bid side (200,682 resting ≥ 5,000 ✓) ≈ $1.98/day (pool ÷ 13 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 56.0¢ | 50 | 1 | $25.00 | ✅ scoring — ~50.0% of bid side (12,104 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-dem` | BUY | 90.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~49.9% of bid side (512,720 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~47.1% of ask side (16,032 resting ≥ 2,000 ✓) ≈ $2.94/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~40.7% of ask side (8,348 resting ≥ 2,000 ✓) ≈ $2.54/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 4,971 | 0 | $25.00 | ✅ scoring — ~30.0% of bid side (16,571 resting ≥ 2,000 ✓) ≈ $1.87/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 97.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~22.7% of ask side (8,337 resting ≥ 2,000 ✓) ≈ $1.42/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 15.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~17.5% of bid side (10,261 resting ≥ 2,000 ✓) ≈ $1.09/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~16.3% of bid side (500,445 resting ≥ 2,000 ✓) ≈ $1.02/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | SELL | 97.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~16.0% of ask side (7,714 resting ≥ 2,000 ✓) ≈ $1.00/day (pool ÷ 2 markets) |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | BUY | 3.0¢ | 2,000 | 6 | $250.00 | ✅ scoring — ~11.6% of bid side (20,147 resting ≥ 5,000 ✓) ≈ $14.46/day |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 2 | 2 | $100.00 | ✅ scoring — ~11.0% of bid side (50,570 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 74.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~10.7% of bid side (500,819 resting ≥ 5,000 ✓) ≈ $0.45/day (pool ÷ 12 markets) |
| `ussewc-usse-wv-2026-11-03-dem` | BUY | 1.0¢ | 1,400 | 0 | $25.00 | ✅ scoring — ~10.7% of bid side (13,100 resting ≥ 2,000 ✓) ≈ $0.67/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | BUY | 11.0¢ | 40 | 2 | $25.00 | ✅ scoring — ~8.9% of bid side (10,584 resting ≥ 2,000 ✓) ≈ $0.56/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~8.9% of ask side (7,698 resting ≥ 2,000 ✓) ≈ $0.56/day (pool ÷ 2 markets) |
| `pntcbk-wnba-white-2027-06-30-roywhi` | BUY | 3.0¢ | 1,500 | 1 | $250.00 | ✅ scoring — ~7.8% of bid side (21,114 resting ≥ 5,000 ✓) ≈ $9.75/day |
| `usgubewc-usgub-il-2026-11-03-dem` | SELL | 97.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~7.7% of ask side (8,286 resting ≥ 2,000 ✓) ≈ $0.48/day (pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | SELL | 10.0¢ | 92 | 0 | $100.00 | ✅ scoring — ~7.7% of ask side (11,228 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 2 markets) |
| …and 168 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>dccc-measles-us-2026-12-31-gt3500</code> BUY 10 @ 72¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 72¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 46¢ | 204 | ×0.25^26 = 0.0 |
|  | 38¢ | 1 | ×0.25^34 = 0.0 |
|  | 1¢ | 10,989 | ×0.25^71 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500` ← this one
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 18 @ 25¢ → $12.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 18 (18 yours) | ×0.25^0 = 18.2 |
|  | 33¢ | 100 | ×0.25^8 = 0.0 |
|  | 50¢ | 25 | ×0.25^25 = 0.0 |
|  | 99¢ | 10,857 | ×0.25^74 = 0.0 |
| | | **Σ** | **18.2** |

`yours 18.2 / Σ 18.2 = 100.0%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 100.0% = $12.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
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
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $5.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,600 (5,000 yours) | ×0.1^0 = 5,600.0 |
| | | **Σ** | **5,600.0** |

`yours 5,000.0 / Σ 5,600.0 = 89.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.3% = $5.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 10 @ 8¢ → $3.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 1¢ | 100,420 | ×0.2^7 = 1.3 |
| | | **Σ** | **11.3** |

`yours 10.0 / Σ 11.3 = 88.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.6% = $3.41/day`  

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
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> SELL 40 @ 96¢ → $3.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 97¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 9,837 | ×0.1^3 = 9.8 |
| | | **Σ** | **63.8** |

`yours 40.0 / Σ 63.8 = 62.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 62.7% = $3.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 98¢ | 130,500 | ×0.1^94 = 0.0 |
| | | **Σ** | **65.0** |

`yours 40.0 / Σ 65.0 = 61.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.5% = $3.85/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>dccc-measles-us-2026-12-31-gt4500</code> BUY 10 @ 42¢ → $2.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 40¢ | 101 | ×0.25^2 = 6.3 |
|  | 38¢ | 4 | ×0.25^4 = 0.0 |
|  | 19¢ | 110 | ×0.25^23 = 0.0 |
|  | 1¢ | 10,880 | ×0.25^41 = 0.0 |
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
<details><summary><code>vsc-usgubp-fl-fshbck-atl-30pct</code> BUY 5,000 @ 1¢ → $3.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 8,291 (5,000 yours) | ×0.2^0 = 8,291.0 |
| | | **Σ** | **8,291.0** |

`yours 5,000.0 / Σ 8,291.0 = 60.3%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 60.3% = $3.02/day`  

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 3¢ → $3.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 68 (40 yours) | ×0.1^0 = 68.0 |
|  | 98¢ | 65,250 | ×0.1^95 = 0.0 |
| | | **Σ** | **68.0** |

`yours 40.0 / Σ 68.0 = 58.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.8% = $3.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 40 @ 16¢ → $1.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 15¢ | 188 | ×0.2^1 = 37.7 |
|  | 10¢ | 45 | ×0.2^6 = 0.0 |
|  | 1¢ | 200,409 | ×0.2^15 = 0.0 |
| | | **Σ** | **77.7** |

`yours 40.0 / Σ 77.7 = 51.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 51.5% = $1.98/day`  

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 50 @ 56¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 57¢ | 4 | ×0.1^0 = 4.0 |
| ▶ | 56¢ | 50 (50 yours) | ×0.1^1 = 5.0 |
|  | 55¢ | 100 | ×0.1^2 = 1.0 |
|  | 1¢ | 11,950 | ×0.1^56 = 0.0 |
| | | **Σ** | **10.0** |

`yours 5.0 / Σ 10.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-dem</code> BUY 10 @ 90¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 20 (10 yours) | ×0.1^0 = 20.0 |
|  | 86¢ | 200 | ×0.1^4 = 0.0 |
|  | 84¢ | 2,000 | ×0.1^6 = 0.0 |
| | | **Σ** | **20.0** |

`yours 10.0 / Σ 20.0 = 49.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.9% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ny-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $2.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 97¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 15,927 | ×0.1^3 = 15.9 |
| | | **Σ** | **84.9** |

`yours 40.0 / Σ 84.9 = 47.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 47.1% = $2.94/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-dem</code> SELL 40 @ 96¢ → $2.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 99¢ | 8,258 | ×0.1^3 = 8.3 |
| | | **Σ** | **98.3** |

`yours 40.0 / Σ 98.3 = 40.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 40.7% = $2.54/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem` ← this one
2. `ussewc-usse-or-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> BUY 4,971 @ 1¢ → $1.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 16,571 (4,971 yours) | ×0.1^0 = 16,571.0 |
| | | **Σ** | **16,571.0** |

`yours 4,971.0 / Σ 16,571.0 = 30.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 30.0% = $1.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 97¢ → $1.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 98¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 8,207 | ×0.1^2 = 82.1 |
| | | **Σ** | **176.1** |

`yours 40.0 / Σ 176.1 = 22.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 22.7% = $1.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 11 @ 15¢ → $1.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 61 (11 yours) | ×0.1^0 = 60.6 |
|  | 1¢ | 10,200 | ×0.1^14 = 0.0 |
| | | **Σ** | **60.6** |

`yours 10.6 / Σ 60.6 = 17.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 17.5% = $1.09/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 95¢ → $1.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 245 (40 yours) | ×0.1^0 = 245.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **245.0** |

`yours 40.0 / Σ 245.0 = 16.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 16.3% = $1.02/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> SELL 35 @ 97¢ → $1.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 135 (35 yours) | ×0.1^0 = 134.9 |
|  | 98¢ | 87 | ×0.1^1 = 8.7 |
|  | 99¢ | 7,492 | ×0.1^2 = 74.9 |
| | | **Σ** | **218.5** |

`yours 34.9 / Σ 218.5 = 16.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 16.0% = $1.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>pntcbk-wnba-freedom-2027-06-30-enekan</code> BUY 2,000 @ 3¢ → $14.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 2,246 | ×0.9^0 = 2,246.1 |
|  | 8¢ | 50 | ×0.9^1 = 45.0 |
|  | 7¢ | 621 | ×0.9^2 = 503.0 |
|  | 4¢ | 30 | ×0.9^5 = 17.7 |
| ▶ | 3¢ | 12,000 (2,000 yours) | ×0.9^6 = 6,377.3 |
| | | **Σ** | **9,189.1** |

`yours 1,062.9 / Σ 9,189.1 = 11.6%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 11.6% = $14.46/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 2 @ 15¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 15¢ | 18 (2 yours) | ×0.2^2 = 0.7 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 17 @ 74¢ → $0.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 50 (17 yours) | ×0.2^0 = 50.4 |
|  | 73¢ | 561 | ×0.2^1 = 112.2 |
|  | 1¢ | 500,208 | ×0.2^73 = 0.0 |
| | | **Σ** | **162.6** |

`yours 17.4 / Σ 162.6 = 10.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 10.7% = $0.45/day`  

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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> BUY 40 @ 11¢ → $0.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 4 | ×0.1^0 = 4.0 |
| ▶ | 11¢ | 40 (40 yours) | ×0.1^2 = 0.4 |
|  | 10¢ | 41 | ×0.1^3 = 0.0 |
|  | 9¢ | 299 | ×0.1^4 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^12 = 0.0 |
| | | **Σ** | **4.5** |

`yours 0.4 / Σ 4.5 = 8.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 8.9% = $0.56/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-co-2026-11-03-dem</code> SELL 40 @ 96¢ → $0.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 440 (40 yours) | ×0.1^0 = 440.0 |
|  | 99¢ | 7,258 | ×0.1^3 = 7.3 |
| | | **Σ** | **447.3** |

`yours 40.0 / Σ 447.3 = 8.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 8.9% = $0.56/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem` ← this one
2. `usgubewc-usgub-co-2026-11-03-rep`

</details>

</details>
<details><summary><code>pntcbk-wnba-white-2027-06-30-roywhi</code> BUY 1,500 @ 3¢ → $9.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 81 | ×0.9^0 = 81.2 |
| ▶ | 3¢ | 3,833 (1,500 yours) | ×0.9^1 = 3,450.0 |
|  | 2¢ | 17,000 | ×0.9^2 = 13,770.0 |
| | | **Σ** | **17,301.1** |

`yours 1,350.0 / Σ 17,301.1 = 7.8%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 7.8% = $9.75/day`  

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-dem</code> SELL 40 @ 97¢ → $0.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 440 (40 yours) | ×0.1^0 = 440.0 |
|  | 99¢ | 7,846 | ×0.1^2 = 78.5 |
| | | **Σ** | **518.5** |

`yours 40.0 / Σ 518.5 = 7.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 7.7% = $0.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem` ← this one
2. `usgubewc-usgub-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> SELL 92 @ 10¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1,029 (92 yours) | ×0.2^0 = 1,029.1 |
|  | 11¢ | 803 | ×0.2^1 = 160.5 |
|  | 13¢ | 747 | ×0.2^3 = 6.0 |
|  | 14¢ | 790 | ×0.2^4 = 1.3 |
|  | 16¢ | 1,949 | ×0.2^6 = 0.1 |
| | | **Σ** | **1,197.0** |

`yours 92.1 / Σ 1,197.0 = 7.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 7.7% = $1.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (48,360 resting) | ~27.0% | ~$20.24 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (49,490 resting) | ~15.7% | ~$11.76 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (67,499 resting) | ~14.9% | ~$11.15 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,783 resting) | ~39.0% | ~$9.75 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (283,103 resting) | ~10.8% | ~$8.11 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (29,882 resting) | ~29.6% | ~$7.40 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (140,565 resting) | ~9.3% | ~$6.94 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (135,677 resting) | ~6.2% | ~$4.66 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (685,381 resting) | ~5.4% | ~$4.01 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (288,563 resting) | ~5.2% | ~$3.89 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (10,743 resting) | ~7.8% | ~$3.88 |
| `ewc-usse-nc-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (30,969 resting) | ~15.4% | ~$3.84 |

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
| 2026-08-13 5:07 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 3:29 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 2:11 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 1:16 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 12:12 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 11:18 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 9:52 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 8:02 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 7:51 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:31 AM ET | ✅ ok | 2087 | $2853.72 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
