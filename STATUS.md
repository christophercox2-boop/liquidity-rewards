# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-12 2:48 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$153.13/day estimated (ceiling, not promise — details below)

**Earned:** $2,447.06 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-10: **$557.62** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-09: **$62.24** · 2026-08-08: **$54.78** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-xavbec` — BUY at the best price, ~$24.90/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$12.99/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$12.29/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$153.13/day (~$6.38/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 11.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (300,550 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.8% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.49/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 11.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~81.6% of bid side (200,595 resting ≥ 5,000 ✓) ≈ $3.14/day (pool ÷ 13 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (510,450 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~76.9% of bid side (6,500 resting ≥ 2,000 ✓) ≈ $4.81/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~75.5% of ask side (208,541 resting ≥ 2,000 ✓) ≈ $4.72/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-rep` | BUY | 9.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~63.2% of bid side (15,683 resting ≥ 2,000 ✓) ≈ $3.95/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~57.8% of ask side (65,714 resting ≥ 2,000 ✓) ≈ $3.61/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 1,290 | 0 | $25.00 | ✅ scoring — ~51.6% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $3.23/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (500,480 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~49.6% of ask side (24,707 resting ≥ 2,000 ✓) ≈ $3.10/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~33.7% of bid side (5,940 resting ≥ 2,000 ✓) ≈ $2.10/day (pool ÷ 2 markets) |
| `pntcbk-wnba-white-2027-06-30-roywhi` | BUY | 1.0¢ | 10,000 | 1 | $250.00 | ✅ scoring — ~32.5% of bid side (30,812 resting ≥ 5,000 ✓) ≈ $40.57/day |
| `ussewc-usse-ok-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~30.1% of bid side (16,600 resting ≥ 2,000 ✓) ≈ $1.88/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-rep` | BUY | 11.0¢ | 40 | 1 | $25.00 | ✅ scoring — ~28.6% of bid side (11,050 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 95.0¢ | 60 | 0 | $25.00 | ✅ scoring — ~27.9% of bid side (510,665 resting ≥ 2,000 ✓) ≈ $1.74/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | SELL | 30.0¢ | 20 | 1 | $50.00 | ✅ scoring — ~27.5% of ask side (11,052 resting ≥ 10,000 ✓) ≈ $3.44/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 93.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~24.2% of bid side (500,607 resting ≥ 2,000 ✓) ≈ $1.51/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl25-2026-08-18-dem-olilar` | SELL | 13.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~22.7% of ask side (8,804 resting ≥ 2,000 ✓) ≈ $1.42/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | SELL | 3.0¢ | 85 | 0 | $25.00 | ✅ scoring — ~20.8% of ask side (136,422 resting ≥ 2,000 ✓) ≈ $1.30/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 72.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~18.8% of bid side (500,404 resting ≥ 5,000 ✓) ≈ $0.78/day (pool ÷ 12 markets) |
| `ussewc-usse-ky-2026-11-03-rep` | BUY | 94.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~18.0% of bid side (510,672 resting ≥ 2,000 ✓) ≈ $1.13/day (pool ÷ 2 markets) |
| `usgubewc-usgub-vt-2026-11-03-dem` | SELL | 12.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~15.9% of ask side (339,105 resting ≥ 2,000 ✓) ≈ $0.99/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 35.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~15.8% of bid side (400,583 resting ≥ 5,000 ✓) ≈ $0.66/day (pool ÷ 12 markets) |
| `ussewc-usse-va-2026-11-03-rep` | BUY | 1.0¢ | 5,000 | 1 | $25.00 | ✅ scoring — ~14.3% of bid side (17,180 resting ≥ 2,000 ✓) ≈ $0.89/day (pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | SELL | 5.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~13.9% of ask side (66,085 resting ≥ 2,000 ✓) ≈ $0.87/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~13.3% of bid side (510,751 resting ≥ 2,000 ✓) ≈ $0.83/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~12.1% of bid side (16,571 resting ≥ 2,000 ✓) ≈ $0.75/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~12.1% of bid side (16,571 resting ≥ 2,000 ✓) ≈ $0.75/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-dem` | BUY | 95.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~11.7% of bid side (610,878 resting ≥ 2,000 ✓) ≈ $0.73/day (pool ÷ 2 markets) |
| …and 385 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 18 @ 11¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 18 (18 yours) | ×0.2^0 = 18.4 |
|  | 1¢ | 300,531 | ×0.2^10 = 0.0 |
| | | **Σ** | **18.4** |

`yours 18.4 / Σ 18.4 = 99.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.8% = $3.84/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 40 @ 11¢ → $3.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 10¢ | 45 | ×0.2^1 = 9.0 |
|  | 1¢ | 200,510 | ×0.2^10 = 0.0 |
| | | **Σ** | **49.0** |

`yours 40.0 / Σ 49.0 = 81.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 81.6% = $3.14/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $4.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 6,500 (5,000 yours) | ×0.1^0 = 6,500.0 |
| | | **Σ** | **6,500.0** |

`yours 5,000.0 / Σ 6,500.0 = 76.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 76.9% = $4.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> SELL 40 @ 4¢ → $4.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 53 (40 yours) | ×0.1^0 = 53.0 |
|  | 98¢ | 208,263 | ×0.1^94 = 0.0 |
| | | **Σ** | **53.0** |

`yours 40.0 / Σ 53.0 = 75.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.5% = $4.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-rep</code> BUY 40 @ 9¢ → $3.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 60 (40 yours) | ×0.1^0 = 60.0 |
|  | 7¢ | 323 | ×0.1^2 = 3.2 |
|  | 6¢ | 100 | ×0.1^3 = 0.1 |
|  | 1¢ | 15,200 | ×0.1^8 = 0.0 |
| | | **Σ** | **63.3** |

`yours 40.0 / Σ 63.3 = 63.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.2% = $3.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem`
2. `usgubewc-usgub-mn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 4¢ → $3.61/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 69 (40 yours) | ×0.1^0 = 69.0 |
|  | 7¢ | 170 | ×0.1^3 = 0.2 |
|  | 98¢ | 65,250 | ×0.1^94 = 0.0 |
| | | **Σ** | **69.2** |

`yours 40.0 / Σ 69.2 = 57.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.8% = $3.61/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 1,290 @ 1¢ → $3.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,500 (1,290 yours) | ×0.1^0 = 2,500.0 |
| | | **Σ** | **2,500.0** |

`yours 1,290.0 / Σ 2,500.0 = 51.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 51.6% = $3.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-dem</code> BUY 40 @ 95¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 80 (40 yours) | ×0.1^0 = 80.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **80.0** |

`yours 40.0 / Σ 80.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem` ← this one
2. `usgubewc-usgub-me-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $3.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 97¢ | 60 | ×0.1^1 = 6.0 |
|  | 99¢ | 24,597 | ×0.1^3 = 24.6 |
| | | **Σ** | **80.6** |

`yours 40.0 / Σ 80.6 = 49.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.6% = $3.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $2.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,940 (2,000 yours) | ×0.1^0 = 5,940.0 |
| | | **Σ** | **5,940.0** |

`yours 2,000.0 / Σ 5,940.0 = 33.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 33.7% = $2.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>pntcbk-wnba-white-2027-06-30-roywhi</code> BUY 10,000 @ 1¢ → $40.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 12 | ×0.9^0 = 12.0 |
| ▶ | 1¢ | 30,800 (10,000 yours) | ×0.9^1 = 27,720.0 |
| | | **Σ** | **27,732.0** |

`yours 9,000.0 / Σ 27,732.0 = 32.5%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 32.5% = $40.57/day`  

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $1.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 16,600 (5,000 yours) | ×0.1^0 = 16,600.0 |
| | | **Σ** | **16,600.0** |

`yours 5,000.0 / Σ 16,600.0 = 30.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 30.1% = $1.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-rep</code> BUY 40 @ 11¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 10 | ×0.1^0 = 10.0 |
| ▶ | 11¢ | 40 (40 yours) | ×0.1^1 = 4.0 |
|  | 5¢ | 700 | ×0.1^7 = 0.0 |
|  | 1¢ | 10,300 | ×0.1^11 = 0.0 |
| | | **Σ** | **14.0** |

`yours 4.0 / Σ 14.0 = 28.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.6% = $1.79/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem`
2. `usgubewc-usgub-ny-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 60 @ 95¢ → $1.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 215 (60 yours) | ×0.1^0 = 215.0 |
|  | 2¢ | 500,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **215.0** |

`yours 60.0 / Σ 215.0 = 27.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.9% = $1.74/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 20 @ 30¢ → $3.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 29¢ | 0 | ×0.25^0 = 0.0 |
| ▶ | 30¢ | 72 (20 yours) | ×0.25^1 = 18.0 |
|  | 34¢ | 99 | ×0.25^5 = 0.1 |
|  | 50¢ | 25 | ×0.25^21 = 0.0 |
|  | 99¢ | 10,856 | ×0.25^70 = 0.0 |
| | | **Σ** | **18.1** |

`yours 5.0 / Σ 18.1 = 27.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 27.5% = $3.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 50 @ 93¢ → $1.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 207 (50 yours) | ×0.1^0 = 207.0 |
|  | 2¢ | 500,200 | ×0.1^91 = 0.0 |
| | | **Σ** | **207.0** |

`yours 50.0 / Σ 207.0 = 24.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 24.2% = $1.51/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-ushrp-fl25-2026-08-18-dem-olilar</code> SELL 5 @ 13¢ → $1.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 22 (5 yours) | ×0.1^0 = 22.0 |
|  | 19¢ | 50 | ×0.1^6 = 0.0 |
|  | 49¢ | 100 | ×0.1^36 = 0.0 |
|  | 99¢ | 8,632 | ×0.1^86 = 0.0 |
| | | **Σ** | **22.0** |

`yours 5.0 / Σ 22.0 = 22.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 22.7% = $1.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl25-2026-08-18-dem-jarmos`
2. `enwc-ushrp-fl25-2026-08-18-dem-olilar` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> SELL 85 @ 3¢ → $1.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 408 (85 yours) | ×0.1^0 = 408.0 |
|  | 6¢ | 289 | ×0.1^3 = 0.3 |
|  | 50¢ | 5,000 | ×0.1^47 = 0.0 |
| | | **Σ** | **408.3** |

`yours 85.0 / Σ 408.3 = 20.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 20.8% = $1.30/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 18 @ 72¢ → $0.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 72¢ | 94 (18 yours) | ×0.2^0 = 93.5 |
|  | 2¢ | 102 | ×0.2^70 = 0.0 |
|  | 1¢ | 500,208 | ×0.2^71 = 0.0 |
| | | **Σ** | **93.5** |

`yours 17.6 / Σ 93.5 = 18.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.8% = $0.78/day`  

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
<details><summary><code>ussewc-usse-ky-2026-11-03-rep</code> BUY 40 @ 94¢ → $1.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 222 (40 yours) | ×0.1^0 = 222.0 |
|  | 2¢ | 500,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **222.0** |

`yours 40.0 / Σ 222.0 = 18.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 18.0% = $1.13/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem`
2. `ussewc-usse-ky-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-vt-2026-11-03-dem</code> SELL 20 @ 12¢ → $0.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 126 (20 yours) | ×0.1^0 = 126.0 |
|  | 98¢ | 132,984 | ×0.1^86 = 0.0 |
| | | **Σ** | **126.0** |

`yours 20.0 / Σ 126.0 = 15.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 15.9% = $0.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-vt-2026-11-03-dem` ← this one
2. `usgubewc-usgub-vt-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 21 @ 35¢ → $0.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 133 (21 yours) | ×0.2^0 = 133.0 |
|  | 2¢ | 400,250 | ×0.2^33 = 0.0 |
| | | **Σ** | **133.0** |

`yours 21.0 / Σ 133.0 = 15.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 15.8% = $0.66/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210` ← this one
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> BUY 5,000 @ 1¢ → $0.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1,980 | ×0.1^0 = 1,980.0 |
| ▶ | 1¢ | 15,200 (5,000 yours) | ×0.1^1 = 1,520.0 |
| | | **Σ** | **3,500.0** |

`yours 500.0 / Σ 3,500.0 = 14.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 14.3% = $0.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> SELL 50 @ 5¢ → $0.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 360 (50 yours) | ×0.1^0 = 360.0 |
|  | 98¢ | 65,500 | ×0.1^93 = 0.0 |
| | | **Σ** | **360.0** |

`yours 50.0 / Σ 360.0 = 13.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 13.9% = $0.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 40 @ 95¢ → $0.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 301 (40 yours) | ×0.1^0 = 301.0 |
|  | 2¢ | 500,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **301.0** |

`yours 40.0 / Σ 301.0 = 13.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 13.3% = $0.83/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $0.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 16,571 (2,000 yours) | ×0.1^0 = 16,571.0 |
| | | **Σ** | **16,571.0** |

`yours 2,000.0 / Σ 16,571.0 = 12.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 12.1% = $0.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $0.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 16,571 (2,000 yours) | ×0.1^0 = 16,571.0 |
| | | **Σ** | **16,571.0** |

`yours 2,000.0 / Σ 16,571.0 = 12.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 12.1% = $0.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-dem</code> BUY 50 @ 95¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 428 (50 yours) | ×0.1^0 = 428.0 |
|  | 2¢ | 600,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **428.0** |

`yours 50.0 / Σ 428.0 = 11.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 11.7% = $0.73/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem` ← this one
2. `ussewc-usse-va-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,046,573 resting) | ~33.2% | ~$24.90 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (66,455 resting) | ~17.3% | ~$12.99 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,676 resting) | ~49.1% | ~$12.29 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,606 resting) | ~37.8% | ~$9.44 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (68,875 resting) | ~12.3% | ~$9.19 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (687,944 resting) | ~12.0% | ~$9.02 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (801,524 resting) | ~11.4% | ~$8.57 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (867,355 resting) | ~11.1% | ~$8.30 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (10,282 resting) | ~20.6% | ~$5.15 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,051,502 resting) | ~6.7% | ~$5.02 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,855 resting) | ~4.1% | ~$3.04 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (315,355 resting) | ~3.5% | ~$2.60 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $557.62 |
| Skipped | $1.41 |
| **Total earned** | **$2,447.06** |

1952 reward rows · 39 days with rewards · 478 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-10 ⚠️ multi-day pending bucket | $557.62 | `████████████████████` |
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
| 2026-07-28 | $79.65 | `███` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $983.74 | `█████████████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $101.55 |
| `apdc-jerpowgov-2026-12-31` | $87.26 |
| `opdc-mcconnell-resign-2026-11-02` | $65.07 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.99 |
| `scc-hrep-rep-2026-11-03-gte200` | $36.36 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `pandc-anydis-2027-12-31` | $31.51 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-12 2:48 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 2:10 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 1:16 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:49 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:39 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:12 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 11:55 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 11:17 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 10:41 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 10:39 AM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
