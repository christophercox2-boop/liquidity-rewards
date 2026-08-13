# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 2:11 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$144.52/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usse-tx-2026-11-03-rep` — SELL at the best price, ~$14.51/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$14.41/day), `ewc-usgub-ga-2026-11-03-dem` (~$13.97/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$144.52/day (~$6.02/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-49` | SELL | 14.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,839 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 20.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (5,501 resting ≥ 5,000 ✓) ≈ $24.99/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,549 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 42.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~99.2% of bid side (11,101 resting ≥ 10,000 ✓) ≈ $4.13/day (pool ÷ 6 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 12.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~95.7% of bid side (200,494 resting ≥ 5,000 ✓) ≈ $3.68/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~91.1% of ask side (12,276 resting ≥ 5,000 ✓) ≈ $22.78/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.8% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.49/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~88.6% of bid side (100,430 resting ≥ 5,000 ✓) ≈ $3.41/day (pool ÷ 13 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 4,971 | 0 | $25.00 | ✅ scoring — ~74.5% of bid side (6,671 resting ≥ 2,000 ✓) ≈ $4.66/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~63.9% of ask side (8,680 resting ≥ 2,000 ✓) ≈ $3.99/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~63.7% of ask side (8,890 resting ≥ 2,000 ✓) ≈ $3.98/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~60.6% of bid side (500,316 resting ≥ 2,000 ✓) ≈ $3.79/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 1.0¢ | 1,750 | 1 | $25.00 | ✅ scoring — ~49.3% of bid side (2,110 resting ≥ 2,000 ✓) ≈ $3.08/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~42.1% of ask side (130,820 resting ≥ 2,000 ✓) ≈ $2.63/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~36.6% of bid side (13,678 resting ≥ 2,000 ✓) ≈ $2.28/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 15.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~29.8% of bid side (10,286 resting ≥ 2,000 ✓) ≈ $1.86/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 3.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~28.6% of ask side (65,665 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-dem` | BUY | 90.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~28.6% of bid side (512,785 resting ≥ 2,000 ✓) ≈ $1.78/day (pool ÷ 2 markets) |
| `ussewc-usse-ri-2026-11-03-rep` | BUY | 1.0¢ | 1,400 | 1 | $25.00 | ✅ scoring — ~22.6% of bid side (2,060 resting ≥ 2,000 ✓) ≈ $1.41/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 1,300 | 0 | $25.00 | ✅ scoring — ~21.0% of bid side (6,196 resting ≥ 2,000 ✓) ≈ $1.31/day (pool ÷ 2 markets) |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | BUY | 3.0¢ | 2,000 | 6 | $250.00 | ✅ scoring — ~18.8% of bid side (9,574 resting ≥ 5,000 ✓) ≈ $23.52/day |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 90.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~16.7% of ask side (27,302 resting ≥ 2,000 ✓) ≈ $1.04/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | BUY | 89.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~16.1% of bid side (310,762 resting ≥ 2,000 ✓) ≈ $1.01/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~15.9% of ask side (11,559 resting ≥ 2,000 ✓) ≈ $0.99/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 97.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~13.2% of ask side (22,944 resting ≥ 2,000 ✓) ≈ $0.82/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 74.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~12.6% of bid side (500,348 resting ≥ 5,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `usgubewc-usgub-vt-2026-11-03-rep` | SELL | 94.0¢ | 233 | 0 | $25.00 | ✅ scoring — ~11.0% of ask side (19,633 resting ≥ 2,000 ✓) ≈ $0.69/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 2 | 2 | $100.00 | ✅ scoring — ~10.7% of bid side (50,570 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 10.0¢ | 92 | 0 | $100.00 | ✅ scoring — ~8.8% of ask side (11,174 resting ≥ 5,000 ✓) ≈ $2.20/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~8.4% of ask side (21,147 resting ≥ 2,000 ✓) ≈ $0.53/day (pool ÷ 2 markets) |
| …and 170 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 4 @ 14¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 4 (4 yours) | ×0.2^0 = 4.0 |
|  | 28¢ | 50 | ×0.2^14 = 0.0 |
|  | 50¢ | 125 | ×0.2^36 = 0.0 |
|  | 97¢ | 80,459 | ×0.2^83 = 0.0 |
| | | **Σ** | **4.0** |

`yours 4.0 / Σ 4.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt4500</code> BUY 10 @ 42¢ → $4.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 40¢ | 1 | ×0.25^2 = 0.1 |
|  | 38¢ | 4 | ×0.25^4 = 0.0 |
|  | 19¢ | 110 | ×0.25^23 = 0.0 |
|  | 1¢ | 10,976 | ×0.25^41 = 0.0 |
| | | **Σ** | **10.1** |

`yours 10.0 / Σ 10.1 = 99.2%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 99.2% = $4.13/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500` ← this one
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 40 @ 12¢ → $3.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 10¢ | 45 | ×0.2^2 = 1.8 |
|  | 1¢ | 200,409 | ×0.2^11 = 0.0 |
| | | **Σ** | **41.8** |

`yours 40.0 / Σ 41.8 = 95.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 95.7% = $3.68/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 24¢ → $22.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 26¢ | 23 | ×0.2^2 = 0.9 |
|  | 29¢ | 170 | ×0.2^5 = 0.1 |
|  | 35¢ | 38 | ×0.2^11 = 0.0 |
|  | 42¢ | 50 | ×0.2^18 = 0.0 |
|  | 79¢ | 0 | ×0.2^55 = 0.0 |
|  | 99¢ | 11,985 | ×0.2^75 = 0.0 |
| | | **Σ** | **11.0** |

`yours 10.0 / Σ 11.0 = 91.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 91.1% = $22.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

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
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> BUY 4,971 @ 1¢ → $4.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 6,671 (4,971 yours) | ×0.1^0 = 6,671.0 |
| | | **Σ** | **6,671.0** |

`yours 4,971.0 / Σ 6,671.0 = 74.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 74.5% = $4.66/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $3.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 97¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 8,590 | ×0.1^3 = 8.6 |
| | | **Σ** | **62.6** |

`yours 40.0 / Σ 62.6 = 63.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.9% = $3.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> SELL 40 @ 96¢ → $3.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 97¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 8,800 | ×0.1^3 = 8.8 |
| | | **Σ** | **62.8** |

`yours 40.0 / Σ 62.8 = 63.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.7% = $3.98/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 95¢ → $3.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 66 (40 yours) | ×0.1^0 = 66.0 |
|  | 91¢ | 50 | ×0.1^4 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **66.0** |

`yours 40.0 / Σ 66.0 = 60.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.6% = $3.79/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 1,750 @ 1¢ → $3.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 160 | ×0.1^0 = 160.0 |
| ▶ | 1¢ | 1,950 (1,750 yours) | ×0.1^1 = 195.0 |
| | | **Σ** | **355.0** |

`yours 175.0 / Σ 355.0 = 49.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.3% = $3.08/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $2.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 95 (40 yours) | ×0.1^0 = 95.0 |
|  | 98¢ | 130,500 | ×0.1^94 = 0.0 |
| | | **Σ** | **95.0** |

`yours 40.0 / Σ 95.0 = 42.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 42.1% = $2.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 11 @ 15¢ → $1.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 36 (11 yours) | ×0.1^0 = 35.6 |
|  | 2¢ | 50 | ×0.1^13 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^14 = 0.0 |
| | | **Σ** | **35.6** |

`yours 10.6 / Σ 35.6 = 29.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 29.8% = $1.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 3¢ → $1.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 140 (40 yours) | ×0.1^0 = 140.0 |
|  | 9¢ | 50 | ×0.1^6 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^95 = 0.0 |
| | | **Σ** | **140.0** |

`yours 40.0 / Σ 140.0 = 28.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.6% = $1.79/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-dem</code> BUY 10 @ 90¢ → $1.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 35 (10 yours) | ×0.1^0 = 35.0 |
|  | 86¢ | 200 | ×0.1^4 = 0.0 |
|  | 85¢ | 50 | ×0.1^5 = 0.0 |
|  | 84¢ | 2,000 | ×0.1^6 = 0.0 |
| | | **Σ** | **35.0** |

`yours 10.0 / Σ 35.0 = 28.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.6% = $1.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ny-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ri-2026-11-03-rep</code> BUY 1,400 @ 1¢ → $1.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 460 | ×0.1^0 = 460.0 |
| ▶ | 1¢ | 1,600 (1,400 yours) | ×0.1^1 = 160.0 |
| | | **Σ** | **620.0** |

`yours 140.0 / Σ 620.0 = 22.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 22.6% = $1.41/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ri-2026-11-03-dem`
2. `ussewc-usse-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 1,300 @ 1¢ → $1.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 6,196 (1,300 yours) | ×0.1^0 = 6,196.0 |
| | | **Σ** | **6,196.0** |

`yours 1,300.0 / Σ 6,196.0 = 21.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 21.0% = $1.31/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>pntcbk-wnba-freedom-2027-06-30-enekan</code> BUY 2,000 @ 3¢ → $23.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 2,244 | ×0.9^0 = 2,244.1 |
|  | 8¢ | 50 | ×0.9^1 = 45.0 |
|  | 7¢ | 50 | ×0.9^2 = 40.5 |
|  | 4¢ | 30 | ×0.9^5 = 17.7 |
| ▶ | 3¢ | 2,000 (2,000 yours) | ×0.9^6 = 1,062.9 |
|  | 1¢ | 5,200 | ×0.9^8 = 2,238.4 |
| | | **Σ** | **5,648.7** |

`yours 1,062.9 / Σ 5,648.7 = 18.8%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 18.8% = $23.52/day`  

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> SELL 1 @ 90¢ → $1.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 6 (1 yours) | ×0.1^0 = 6.0 |
|  | 99¢ | 27,296 | ×0.1^9 = 0.0 |
| | | **Σ** | **6.0** |

`yours 1.0 / Σ 6.0 = 16.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 16.7% = $1.04/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> BUY 10 @ 89¢ → $1.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 62 (10 yours) | ×0.1^0 = 62.0 |
|  | 54¢ | 500 | ×0.1^35 = 0.0 |
|  | 2¢ | 300,000 | ×0.1^87 = 0.0 |
| | | **Σ** | **62.0** |

`yours 10.0 / Σ 62.0 = 16.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 16.1% = $1.01/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-co-2026-11-03-dem</code> SELL 40 @ 96¢ → $0.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 240 (40 yours) | ×0.1^0 = 240.0 |
|  | 99¢ | 11,319 | ×0.1^3 = 11.3 |
| | | **Σ** | **251.3** |

`yours 40.0 / Σ 251.3 = 15.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 15.9% = $0.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem` ← this one
2. `usgubewc-usgub-co-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 97¢ → $0.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 98¢ | 105 | ×0.1^1 = 10.5 |
|  | 99¢ | 22,774 | ×0.1^2 = 227.7 |
| | | **Σ** | **303.2** |

`yours 40.0 / Σ 303.2 = 13.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 13.2% = $0.82/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 18 @ 74¢ → $0.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 140 (18 yours) | ×0.2^0 = 139.6 |
|  | 1¢ | 500,208 | ×0.2^73 = 0.0 |
| | | **Σ** | **139.6** |

`yours 17.6 / Σ 139.6 = 12.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 12.6% = $0.52/day`  

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
<details><summary><code>usgubewc-usgub-vt-2026-11-03-rep</code> SELL 233 @ 94¢ → $0.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 2,109 (233 yours) | ×0.1^0 = 2,109.4 |
| | | **Σ** | **2,109.4** |

`yours 232.8 / Σ 2,109.4 = 11.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 11.0% = $0.69/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-vt-2026-11-03-dem`
2. `usgubewc-usgub-vt-2026-11-03-rep` ← this one

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 92 @ 10¢ → $2.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 865 (92 yours) | ×0.2^0 = 865.1 |
|  | 11¢ | 863 | ×0.2^1 = 172.5 |
|  | 13¢ | 747 | ×0.2^3 = 6.0 |
|  | 14¢ | 790 | ×0.2^4 = 1.3 |
|  | 16¢ | 1,949 | ×0.2^6 = 0.1 |
| | | **Σ** | **1,045.0** |

`yours 92.1 / Σ 1,045.0 = 8.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 8.8% = $2.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-dem</code> SELL 40 @ 96¢ → $0.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 440 (40 yours) | ×0.1^0 = 440.0 |
|  | 97¢ | 156 | ×0.1^1 = 15.6 |
|  | 99¢ | 20,551 | ×0.1^3 = 20.6 |
| | | **Σ** | **476.2** |

`yours 40.0 / Σ 476.2 = 8.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 8.4% = $0.53/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem` ← this one
2. `ussewc-usse-or-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (160,634 resting) | ~19.3% | ~$14.51 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,837 resting) | ~57.7% | ~$14.41 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (83,276 resting) | ~18.6% | ~$13.97 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (64,484 resting) | ~15.4% | ~$11.53 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,406 resting) | ~27.1% | ~$6.78 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (287,614 resting) | ~8.4% | ~$6.34 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (395,965 resting) | ~6.7% | ~$5.03 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,725 resting) | ~17.7% | ~$4.42 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (957,798 resting) | ~5.8% | ~$4.37 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (685,386 resting) | ~5.6% | ~$4.19 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (10,593 resting) | ~8.2% | ~$4.12 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (105,085 resting) | ~14.5% | ~$3.63 |

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
| 2026-08-13 2:11 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 1:16 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 12:12 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 11:18 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 9:52 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 8:02 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 7:51 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:31 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 4:46 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 2:50 AM ET | ✅ ok | 2087 | $2853.72 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
