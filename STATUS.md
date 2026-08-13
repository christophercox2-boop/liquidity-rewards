# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 12:12 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$124.48/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$14.23/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$11.49/day), `ewc-usgub-ga-2026-11-03-rep` (~$11.25/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$124.48/day (~$5.19/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,549 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 90.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (27,302 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-dem` | BUY | 89.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~97.8% of bid side (502,775 resting ≥ 2,000 ✓) ≈ $6.11/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.3% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.47/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~84.8% of bid side (140,540 resting ≥ 5,000 ✓) ≈ $3.26/day (pool ÷ 13 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~75.5% of ask side (130,778 resting ≥ 2,000 ✓) ≈ $4.72/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 16.0¢ | 20 | 2 | $100.00 | ✅ scoring — ~74.9% of bid side (5,520 resting ≥ 5,000 ✓) ≈ $18.74/day (pool ÷ 2 markets) |
| `ussewc-usse-ks-2026-11-03-dem` | BUY | 28.0¢ | 16 | 0 | $25.00 | ✅ scoring — ~69.6% of bid side (3,049 resting ≥ 2,000 ✓) ≈ $4.35/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~64.3% of ask side (8,285 resting ≥ 2,000 ✓) ≈ $4.02/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~55.3% of ask side (7,374 resting ≥ 2,000 ✓) ≈ $3.46/day (pool ÷ 2 markets) |
| `mlaec-isrpol-pm-2026-10-27-bennet` | BUY | 31.0¢ | 50 | 3 | $25.00 | ✅ scoring — ~50.0% of bid side (51,481 resting ≥ 2,000 ✓) ≈ $0.62/day (pool ÷ 10 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~45.9% of bid side (10,890 resting ≥ 2,000 ✓) ≈ $2.87/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 24.0¢ | 10 | 4 | $100.00 | ✅ scoring — ~43.0% of ask side (8,694 resting ≥ 5,000 ✓) ≈ $10.76/day (pool ÷ 2 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 42.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~42.9% of bid side (11,108 resting ≥ 10,000 ✓) ≈ $1.79/day (pool ÷ 6 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~39.1% of ask side (8,535 resting ≥ 2,000 ✓) ≈ $2.44/day (pool ÷ 2 markets) |
| `usgubewc-usgub-sd-2026-11-03-dem` | BUY | 1.0¢ | 1,660 | 1 | $25.00 | ✅ scoring — ~37.2% of bid side (3,020 resting ≥ 2,000 ✓) ≈ $2.33/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | BUY | 89.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~35.7% of bid side (310,728 resting ≥ 2,000 ✓) ≈ $2.23/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl25-2026-08-18-dem-olilar` | SELL | 13.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~32.3% of ask side (6,274 resting ≥ 2,000 ✓) ≈ $2.02/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 4,971 | 0 | $25.00 | ✅ scoring — ~29.8% of bid side (16,671 resting ≥ 2,000 ✓) ≈ $1.86/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | BUY | 11.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~26.0% of bid side (11,087 resting ≥ 2,000 ✓) ≈ $1.62/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 44.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~19.0% of ask side (82,483 resting ≥ 5,000 ✓) ≈ $0.79/day (pool ÷ 12 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 1,300 | 0 | $25.00 | ✅ scoring — ~15.2% of bid side (8,554 resting ≥ 2,000 ✓) ≈ $0.95/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 74.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~13.6% of bid side (500,637 resting ≥ 5,000 ✓) ≈ $0.57/day (pool ÷ 12 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~12.7% of bid side (500,514 resting ≥ 2,000 ✓) ≈ $0.80/day (pool ÷ 2 markets) |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | BUY | 3.0¢ | 2,000 | 6 | $250.00 | ✅ scoring — ~11.6% of bid side (20,145 resting ≥ 5,000 ✓) ≈ $14.46/day |
| `usgubewc-usgub-ne-2026-11-03-dem` | BUY | 12.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~10.8% of bid side (11,365 resting ≥ 2,000 ✓) ≈ $0.68/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 2 | 2 | $100.00 | ✅ scoring — ~10.7% of bid side (50,570 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 13 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 97.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~10.1% of ask side (20,487 resting ≥ 2,000 ✓) ≈ $0.63/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 14.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~8.9% of ask side (91,841 resting ≥ 5,000 ✓) ≈ $0.34/day (pool ÷ 13 markets) |
| `ussewc-usse-ks-2026-11-03-rep` | BUY | 77.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~8.7% of bid side (510,582 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 2 markets) |
| …and 171 more | | | | | | |

**Tap an order for its book window and the math:**

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
<details><summary><code>usgubewc-usgub-ny-2026-11-03-dem</code> BUY 10 @ 89¢ → $6.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 86¢ | 200 | ×0.1^3 = 0.2 |
|  | 85¢ | 50 | ×0.1^4 = 0.0 |
|  | 84¢ | 2,000 | ×0.1^5 = 0.0 |
| | | **Σ** | **10.2** |

`yours 10.0 / Σ 10.2 = 97.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 97.8% = $6.11/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ny-2026-11-03-rep`

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 20 @ 16¢ → $18.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 16¢ | 20 (20 yours) | ×0.2^2 = 0.8 |
|  | 15¢ | 30 | ×0.2^3 = 0.2 |
|  | 14¢ | 6 | ×0.2^4 = 0.0 |
|  | 13¢ | 1 | ×0.2^5 = 0.0 |
|  | 12¢ | 118 | ×0.2^6 = 0.0 |
|  | 2¢ | 100 | ×0.2^16 = 0.0 |
|  | 1¢ | 5,246 | ×0.2^17 = 0.0 |
| | | **Σ** | **1.1** |

`yours 0.8 / Σ 1.1 = 74.9%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 74.9% = $18.74/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

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
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $4.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 97¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 8,195 | ×0.1^3 = 8.2 |
| | | **Σ** | **62.2** |

`yours 40.0 / Σ 62.2 = 64.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 64.3% = $4.02/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-dem</code> SELL 40 @ 96¢ → $3.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 99¢ | 7,309 | ×0.1^3 = 7.3 |
| | | **Σ** | **72.3** |

`yours 40.0 / Σ 72.3 = 55.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 55.3% = $3.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem` ← this one
2. `ussewc-usse-or-2026-11-03-rep`

</details>

</details>
<details><summary><code>mlaec-isrpol-pm-2026-10-27-bennet</code> BUY 50 @ 31¢ → $0.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 34¢ | 0 | ×0.1^0 = 0.0 |
| ▶ | 31¢ | 80 (50 yours) | ×0.1^3 = 0.1 |
|  | 28¢ | 21 | ×0.1^6 = 0.0 |
|  | 27¢ | 110 | ×0.1^7 = 0.0 |
|  | 22¢ | 170 | ×0.1^12 = 0.0 |
|  | 18¢ | 150 | ×0.1^16 = 0.0 |
|  | 12¢ | 250 | ×0.1^22 = 0.0 |
|  | 5¢ | 500 | ×0.1^29 = 0.0 |
|  | 1¢ | 50,200 | ×0.1^33 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 50.0%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 50.0% = $0.62/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `mlaec-isrpol-pm-2026-10-27-avilie`
2. `mlaec-isrpol-pm-2026-10-27-ayesha`
3. `mlaec-isrpol-pm-2026-10-27-bengan`
4. `mlaec-isrpol-pm-2026-10-27-bennet` ← this one
5. `mlaec-isrpol-pm-2026-10-27-gadeiz`
6. `mlaec-isrpol-pm-2026-10-27-gidsaa`
7. `mlaec-isrpol-pm-2026-10-27-itaben`
8. `mlaec-isrpol-pm-2026-10-27-nafben`
9. `mlaec-isrpol-pm-2026-10-27-yailap`
10. `mlaec-isrpol-pm-2026-10-27-yoahen`

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 24¢ → $10.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 24¢ | 10 (10 yours) | ×0.2^4 = 0.0 |
|  | 25¢ | 30 | ×0.2^5 = 0.0 |
|  | 26¢ | 23 | ×0.2^6 = 0.0 |
|  | 29¢ | 208 | ×0.2^9 = 0.0 |
|  | 35¢ | 38 | ×0.2^15 = 0.0 |
|  | 42¢ | 50 | ×0.2^22 = 0.0 |
|  | 99¢ | 8,335 | ×0.2^79 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 43.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 43.0% = $10.76/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

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
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> SELL 40 @ 96¢ → $2.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 97¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 8,405 | ×0.1^3 = 8.4 |
| | | **Σ** | **102.4** |

`yours 40.0 / Σ 102.4 = 39.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 39.1% = $2.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-sd-2026-11-03-dem</code> BUY 1,660 @ 1¢ → $2.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 160 | ×0.1^0 = 160.0 |
| ▶ | 1¢ | 2,860 (1,660 yours) | ×0.1^1 = 286.0 |
| | | **Σ** | **446.0** |

`yours 166.0 / Σ 446.0 = 37.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 37.2% = $2.33/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sd-2026-11-03-dem` ← this one
2. `usgubewc-usgub-sd-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> BUY 10 @ 89¢ → $2.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 28 (10 yours) | ×0.1^0 = 28.0 |
|  | 54¢ | 500 | ×0.1^35 = 0.0 |
|  | 2¢ | 300,000 | ×0.1^87 = 0.0 |
| | | **Σ** | **28.0** |

`yours 10.0 / Σ 28.0 = 35.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 35.7% = $2.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-ushrp-fl25-2026-08-18-dem-olilar</code> SELL 5 @ 13¢ → $2.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 15 (5 yours) | ×0.1^0 = 15.0 |
|  | 15¢ | 50 | ×0.1^2 = 0.5 |
|  | 49¢ | 100 | ×0.1^36 = 0.0 |
|  | 99¢ | 6,109 | ×0.1^86 = 0.0 |
| | | **Σ** | **15.5** |

`yours 5.0 / Σ 15.5 = 32.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 32.3% = $2.02/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl25-2026-08-18-dem-jarmos`
2. `enwc-ushrp-fl25-2026-08-18-dem-olilar` ← this one

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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> BUY 40 @ 11¢ → $1.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 147 (40 yours) | ×0.1^0 = 147.0 |
|  | 10¢ | 41 | ×0.1^1 = 4.1 |
|  | 9¢ | 299 | ×0.1^2 = 3.0 |
|  | 4¢ | 400 | ×0.1^7 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^10 = 0.0 |
| | | **Σ** | **154.1** |

`yours 40.0 / Σ 154.1 = 26.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.0% = $1.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 8 @ 44¢ → $0.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 44¢ | 42 (8 yours) | ×0.2^0 = 42.0 |
|  | 71¢ | 169 | ×0.2^27 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^54 = 0.0 |
| | | **Σ** | **42.0** |

`yours 8.0 / Σ 42.0 = 19.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.0% = $0.79/day`  

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
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 1,300 @ 1¢ → $0.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 8,554 (1,300 yours) | ×0.1^0 = 8,554.0 |
| | | **Σ** | **8,554.0** |

`yours 1,300.0 / Σ 8,554.0 = 15.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 15.2% = $0.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 18 @ 74¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 55 (18 yours) | ×0.2^0 = 54.5 |
|  | 73¢ | 374 | ×0.2^1 = 74.8 |
|  | 1¢ | 500,208 | ×0.2^73 = 0.0 |
| | | **Σ** | **129.3** |

`yours 17.6 / Σ 129.3 = 13.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 13.6% = $0.57/day`  

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
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 95¢ → $0.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 314 (40 yours) | ×0.1^0 = 314.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **314.0** |

`yours 40.0 / Σ 314.0 = 12.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 12.7% = $0.80/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>pntcbk-wnba-freedom-2027-06-30-enekan</code> BUY 2,000 @ 3¢ → $14.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 2,244 | ×0.9^0 = 2,244.1 |
|  | 8¢ | 50 | ×0.9^1 = 45.0 |
|  | 7¢ | 621 | ×0.9^2 = 503.0 |
|  | 4¢ | 30 | ×0.9^5 = 17.7 |
| ▶ | 3¢ | 12,000 (2,000 yours) | ×0.9^6 = 6,377.3 |
| | | **Σ** | **9,187.1** |

`yours 1,062.9 / Σ 9,187.1 = 11.6%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 11.6% = $14.46/day`  

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> BUY 10 @ 12¢ → $0.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 92 (10 yours) | ×0.1^0 = 92.0 |
|  | 9¢ | 400 | ×0.1^3 = 0.4 |
|  | 1¢ | 10,873 | ×0.1^11 = 0.0 |
| | | **Σ** | **92.4** |

`yours 10.0 / Σ 92.4 = 10.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 10.8% = $0.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

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
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 97¢ → $0.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 98¢ | 1,426 | ×0.1^1 = 142.6 |
|  | 99¢ | 18,996 | ×0.1^2 = 190.0 |
| | | **Σ** | **397.6** |

`yours 40.0 / Σ 397.6 = 10.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 10.1% = $0.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 14¢ → $0.34/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 56 (5 yours) | ×0.2^0 = 56.0 |
|  | 50¢ | 125 | ×0.2^36 = 0.0 |
|  | 97¢ | 80,459 | ×0.2^83 = 0.0 |
| | | **Σ** | **56.0** |

`yours 5.0 / Σ 56.0 = 8.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.9% = $0.34/day`  

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
<details><summary><code>ussewc-usse-ks-2026-11-03-rep</code> BUY 20 @ 77¢ → $0.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 231 (20 yours) | ×0.1^0 = 231.0 |
|  | 73¢ | 151 | ×0.1^4 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^75 = 0.0 |
| | | **Σ** | **231.0** |

`yours 20.0 / Σ 231.0 = 8.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 8.7% = $0.54/day`  

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
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (83,230 resting) | ~19.0% | ~$14.23 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (29,211 resting) | ~45.9% | ~$11.49 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (64,595 resting) | ~15.0% | ~$11.25 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (389,252 resting) | ~9.1% | ~$6.82 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,037,104 resting) | ~8.9% | ~$6.64 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (292,176 resting) | ~8.3% | ~$6.26 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,204 resting) | ~24.6% | ~$6.14 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (168,767 resting) | ~6.8% | ~$5.11 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,082,852 resting) | ~6.5% | ~$4.85 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,550 resting) | ~14.5% | ~$3.63 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (817,757 resting) | ~4.8% | ~$3.57 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,640 resting) | ~4.6% | ~$3.45 |

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
| 2026-08-13 12:12 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 11:18 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 9:52 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 8:02 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 7:51 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:31 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 4:46 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 2:50 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 1:11 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-12 11:02 PM ET | ✅ ok | 2087 | $2853.72 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
