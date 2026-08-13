# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 3:29 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$103.79/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$14.90/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$11.43/day), `ewc-usgub-ga-2026-11-03-dem` (~$10.88/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$103.79/day (~$4.32/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vsc-usgubp-fl-fshbck-atl-30pct` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (5,000 resting ≥ 5,000 ✓) ≈ $5.00/day (pool ÷ 10 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 20.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (5,501 resting ≥ 5,000 ✓) ≈ $24.99/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,449 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 53.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~99.2% of bid side (12,206 resting ≥ 2,000 ✓) ≈ $6.20/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.3% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.47/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~84.8% of bid side (140,430 resting ≥ 5,000 ✓) ≈ $3.26/day (pool ÷ 13 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~74.1% of ask side (130,779 resting ≥ 2,000 ✓) ≈ $4.63/day (pool ÷ 2 markets) |
| `dccc-measles-us-2026-12-31-gt4500` | BUY | 42.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~61.2% of bid side (11,201 resting ≥ 10,000 ✓) ≈ $2.55/day (pool ÷ 6 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 3.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~58.8% of ask side (65,543 resting ≥ 2,000 ✓) ≈ $3.68/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 14.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~51.5% of bid side (200,682 resting ≥ 5,000 ✓) ≈ $1.98/day (pool ÷ 13 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | BUY | 11.0¢ | 40 | 1 | $25.00 | ✅ scoring — ~45.9% of bid side (10,584 resting ≥ 2,000 ✓) ≈ $2.87/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~36.6% of bid side (13,678 resting ≥ 2,000 ✓) ≈ $2.28/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-dem` | BUY | 90.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~28.6% of bid side (512,735 resting ≥ 2,000 ✓) ≈ $1.78/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | SELL | 25.0¢ | 18 | 0 | $50.00 | ✅ scoring — ~27.9% of ask side (11,048 resting ≥ 10,000 ✓) ≈ $3.48/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 4,971 | 0 | $25.00 | ✅ scoring — ~18.1% of bid side (27,507 resting ≥ 2,000 ✓) ≈ $1.13/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 90.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~16.7% of ask side (27,193 resting ≥ 2,000 ✓) ≈ $1.04/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~14.0% of bid side (500,486 resting ≥ 2,000 ✓) ≈ $0.87/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 74.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~13.9% of bid side (500,632 resting ≥ 5,000 ✓) ≈ $0.58/day (pool ÷ 12 markets) |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | BUY | 3.0¢ | 2,000 | 6 | $250.00 | ✅ scoring — ~11.6% of bid side (20,150 resting ≥ 5,000 ✓) ≈ $14.45/day |
| `ussewc-usse-wv-2026-11-03-dem` | BUY | 1.0¢ | 1,400 | 0 | $25.00 | ✅ scoring — ~10.7% of bid side (13,100 resting ≥ 2,000 ✓) ≈ $0.67/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 2 | 2 | $100.00 | ✅ scoring — ~10.7% of bid side (50,570 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 13 markets) |
| `pntcbk-wnba-white-2027-06-30-roywhi` | BUY | 3.0¢ | 1,500 | 1 | $250.00 | ✅ scoring — ~7.8% of bid side (21,113 resting ≥ 5,000 ✓) ≈ $9.75/day |
| `ussewc-usse-or-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~5.7% of ask side (33,510 resting ≥ 2,000 ✓) ≈ $0.36/day (pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | SELL | 10.0¢ | 92 | 0 | $100.00 | ✅ scoring — ~5.7% of ask side (12,669 resting ≥ 5,000 ✓) ≈ $1.43/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 3.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~5.7% of bid side (8,290 resting ≥ 5,000 ✓) ≈ $0.22/day (pool ÷ 13 markets) |
| `ussewc-usse-ks-2026-11-03-rep` | BUY | 77.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~5.2% of bid side (510,687 resting ≥ 2,000 ✓) ≈ $0.32/day (pool ÷ 2 markets) |
| `dccc-measles-us-2026-12-31-gt3500` | BUY | 72.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~4.7% of bid side (11,100 resting ≥ 10,000 ✓) ≈ $0.19/day (pool ÷ 6 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 15.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~2.7% of bid side (10,821 resting ≥ 2,000 ✓) ≈ $0.17/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~2.3% of ask side (19,812 resting ≥ 2,000 ✓) ≈ $0.15/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~2.3% of ask side (91,816 resting ≥ 5,000 ✓) ≈ $0.09/day (pool ÷ 13 markets) |
| …and 171 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vsc-usgubp-fl-fshbck-atl-30pct</code> BUY 5,000 @ 1¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,000 (5,000 yours) | ×0.2^0 = 5,000.0 |
| | | **Σ** | **5,000.0** |

`yours 5,000.0 / Σ 5,000.0 = 100.0%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 100.0% = $5.00/day`  

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 50 @ 53¢ → $6.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 53¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 52¢ | 4 | ×0.1^1 = 0.4 |
|  | 49¢ | 150 | ×0.1^4 = 0.0 |
|  | 4¢ | 52 | ×0.1^49 = 0.0 |
|  | 1¢ | 11,950 | ×0.1^52 = 0.0 |
| | | **Σ** | **50.4** |

`yours 50.0 / Σ 50.4 = 99.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.2% = $6.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

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
|  | 1¢ | 140,420 | ×0.2^7 = 1.8 |
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
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $4.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 54 (40 yours) | ×0.1^0 = 54.0 |
|  | 98¢ | 130,500 | ×0.1^94 = 0.0 |
| | | **Σ** | **54.0** |

`yours 40.0 / Σ 54.0 = 74.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 74.1% = $4.63/day`  

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
|  | 1¢ | 10,976 | ×0.25^41 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 40 @ 14¢ → $1.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 13¢ | 188 | ×0.2^1 = 37.7 |
|  | 10¢ | 45 | ×0.2^4 = 0.1 |
|  | 1¢ | 200,409 | ×0.2^13 = 0.0 |
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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> BUY 40 @ 11¢ → $2.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 4 | ×0.1^0 = 4.0 |
| ▶ | 11¢ | 40 (40 yours) | ×0.1^1 = 4.0 |
|  | 10¢ | 41 | ×0.1^2 = 0.4 |
|  | 9¢ | 299 | ×0.1^3 = 0.3 |
|  | 1¢ | 10,200 | ×0.1^11 = 0.0 |
| | | **Σ** | **8.7** |

`yours 4.0 / Σ 8.7 = 45.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 45.9% = $2.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> SELL 1 @ 90¢ → $1.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 6 (1 yours) | ×0.1^0 = 6.0 |
|  | 99¢ | 27,187 | ×0.1^9 = 0.0 |
| | | **Σ** | **6.0** |

`yours 1.0 / Σ 6.0 = 16.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 16.7% = $1.04/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 95¢ → $0.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 286 (40 yours) | ×0.1^0 = 286.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **286.0** |

`yours 40.0 / Σ 286.0 = 14.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 14.0% = $0.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 17 @ 74¢ → $0.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 50 (17 yours) | ×0.2^0 = 50.4 |
|  | 73¢ | 374 | ×0.2^1 = 74.8 |
|  | 1¢ | 500,208 | ×0.2^73 = 0.0 |
| | | **Σ** | **125.2** |

`yours 17.4 / Σ 125.2 = 13.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 13.9% = $0.58/day`  

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
<details><summary><code>pntcbk-wnba-freedom-2027-06-30-enekan</code> BUY 2,000 @ 3¢ → $14.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 2,249 | ×0.9^0 = 2,249.1 |
|  | 8¢ | 50 | ×0.9^1 = 45.0 |
|  | 7¢ | 621 | ×0.9^2 = 503.0 |
|  | 4¢ | 30 | ×0.9^5 = 17.7 |
| ▶ | 3¢ | 12,000 (2,000 yours) | ×0.9^6 = 6,377.3 |
| | | **Σ** | **9,192.1** |

`yours 1,062.9 / Σ 9,192.1 = 11.6%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 11.6% = $14.45/day`  

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
<details><summary><code>pntcbk-wnba-white-2027-06-30-roywhi</code> BUY 1,500 @ 3¢ → $9.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 80 | ×0.9^0 = 80.2 |
| ▶ | 3¢ | 3,833 (1,500 yours) | ×0.9^1 = 3,450.0 |
|  | 2¢ | 17,000 | ×0.9^2 = 13,770.0 |
| | | **Σ** | **17,300.1** |

`yours 1,350.0 / Σ 17,300.1 = 7.8%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 7.8% = $9.75/day`  

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-dem</code> SELL 40 @ 96¢ → $0.36/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 440 (40 yours) | ×0.1^0 = 440.0 |
|  | 98¢ | 25,858 | ×0.1^2 = 258.6 |
| | | **Σ** | **698.6** |

`yours 40.0 / Σ 698.6 = 5.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 5.7% = $0.36/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem` ← this one
2. `ussewc-usse-or-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> SELL 92 @ 10¢ → $1.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1,196 (92 yours) | ×0.2^0 = 1,196.1 |
|  | 11¢ | 2,027 | ×0.2^1 = 405.4 |
|  | 13¢ | 747 | ×0.2^3 = 6.0 |
|  | 14¢ | 790 | ×0.2^4 = 1.3 |
|  | 16¢ | 1,949 | ×0.2^6 = 0.1 |
| | | **Σ** | **1,608.9** |

`yours 92.1 / Σ 1,608.9 = 5.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 5.7% = $1.43/day`  

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
| ▶ | 77¢ | 386 (20 yours) | ×0.1^0 = 386.0 |
|  | 73¢ | 101 | ×0.1^4 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^75 = 0.0 |
| | | **Σ** | **386.0** |

`yours 20.0 / Σ 386.0 = 5.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 5.2% = $0.32/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem`
2. `ussewc-usse-ks-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>dccc-measles-us-2026-12-31-gt3500</code> BUY 10 @ 72¢ → $0.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 72¢ | 214 (10 yours) | ×0.25^0 = 214.1 |
|  | 38¢ | 1 | ×0.25^34 = 0.0 |
|  | 1¢ | 10,885 | ×0.25^71 = 0.0 |
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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 11 @ 15¢ → $0.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 392 (11 yours) | ×0.1^0 = 391.6 |
|  | 10¢ | 179 | ×0.1^5 = 0.0 |
|  | 2¢ | 50 | ×0.1^13 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^14 = 0.0 |
| | | **Σ** | **391.6** |

`yours 10.6 / Σ 391.6 = 2.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 2.7% = $0.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $0.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 1,690 (40 yours) | ×0.1^0 = 1,690.0 |
|  | 97¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 18,082 | ×0.1^3 = 18.1 |
| | | **Σ** | **1,712.1** |

`yours 40.0 / Σ 1,712.1 = 2.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 2.3% = $0.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 0 @ 20¢ → $0.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 21 (0 yours) | ×0.2^0 = 21.5 |
|  | 29¢ | 0 | ×0.2^9 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 71¢ | 0 | ×0.2^51 = 0.0 |
|  | 97¢ | 80,494 | ×0.2^77 = 0.0 |
| | | **Σ** | **21.5** |

`yours 0.5 / Σ 21.5 = 2.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 2.3% = $0.09/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,880 resting) | ~59.6% | ~$14.90 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (64,394 resting) | ~15.2% | ~$11.43 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (68,224 resting) | ~14.5% | ~$10.88 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (956,820 resting) | ~9.5% | ~$7.12 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (134,301 resting) | ~8.3% | ~$6.24 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,728 resting) | ~24.6% | ~$6.14 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (293,655 resting) | ~7.8% | ~$5.85 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (395,518 resting) | ~7.7% | ~$5.80 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (282,809 resting) | ~7.3% | ~$5.44 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (10,496 resting) | ~8.3% | ~$4.15 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,458 resting) | ~14.5% | ~$3.63 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (646,778 resting) | ~4.3% | ~$3.21 |

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
| 2026-08-13 3:29 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 2:11 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 1:16 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 12:12 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 11:18 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 9:52 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 8:02 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 7:51 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:31 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 4:46 AM ET | ✅ ok | 2087 | $2853.72 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
