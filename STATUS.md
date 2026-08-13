# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 1:11 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$215.73/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — SELL at the best price, ~$22.11/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$18.80/day), `ewc-usgub-ga-2026-11-03-dem` (~$13.21/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$215.73/day (~$8.99/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,440 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,549 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `usgubewc-usgub-me-2026-11-03-rep` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~93.0% of ask side (65,568 resting ≥ 2,000 ✓) ≈ $5.81/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.8% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.49/day (pool ÷ 13 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 92.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (500,250 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~75.8% of bid side (6,600 resting ≥ 2,000 ✓) ≈ $4.73/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | BUY | 94.0¢ | 29 | 0 | $25.00 | ✅ scoring — ~74.4% of bid side (310,739 resting ≥ 2,000 ✓) ≈ $4.65/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 12.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~59.9% of bid side (200,620 resting ≥ 5,000 ✓) ≈ $2.30/day (pool ÷ 13 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~58.8% of ask side (208,556 resting ≥ 2,000 ✓) ≈ $3.68/day (pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-dem` | SELL | 8.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~58.1% of ask side (272,197 resting ≥ 2,000 ✓) ≈ $3.63/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~57.8% of ask side (65,714 resting ≥ 2,000 ✓) ≈ $3.61/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~57.1% of ask side (208,558 resting ≥ 2,000 ✓) ≈ $3.57/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~57.1% of ask side (130,995 resting ≥ 2,000 ✓) ≈ $3.57/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~54.1% of bid side (3,700 resting ≥ 2,000 ✓) ≈ $3.38/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~53.0% of ask side (19,555 resting ≥ 2,000 ✓) ≈ $3.31/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~50.6% of bid side (500,479 resting ≥ 2,000 ✓) ≈ $3.16/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 34.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~50.1% of ask side (82,797 resting ≥ 5,000 ✓) ≈ $2.09/day (pool ÷ 12 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 1,300 | 0 | $25.00 | ✅ scoring — ~43.3% of bid side (3,000 resting ≥ 2,000 ✓) ≈ $2.71/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~38.9% of ask side (77,922 resting ≥ 5,000 ✓) ≈ $1.50/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 8.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~36.6% of bid side (400,587 resting ≥ 5,000 ✓) ≈ $1.53/day (pool ÷ 12 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~32.3% of ask side (8,543 resting ≥ 2,000 ✓) ≈ $2.02/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~30.7% of ask side (72,125 resting ≥ 2,000 ✓) ≈ $1.92/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~29.9% of bid side (16,700 resting ≥ 2,000 ✓) ≈ $1.87/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 4,971 | 0 | $25.00 | ✅ scoring — ~29.8% of bid side (16,671 resting ≥ 2,000 ✓) ≈ $1.86/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 26.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~29.0% of bid side (10,526 resting ≥ 5,000 ✓) ≈ $7.26/day (pool ÷ 2 markets) |
| `pntcbk-wnba-white-2027-06-30-roywhi` | BUY | 2.0¢ | 6,000 | 1 | $250.00 | ✅ scoring — ~26.6% of bid side (22,721 resting ≥ 5,000 ✓) ≈ $33.30/day |
| `mlaec-isrpol-pm-2026-10-27-bennet` | BUY | 31.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~26.6% of bid side (51,955 resting ≥ 2,000 ✓) ≈ $0.33/day (pool ÷ 10 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~26.3% of bid side (2,102 resting ≥ 2,000 ✓) ≈ $1.64/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nh-2026-11-03-rep` | BUY | 80.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~26.1% of bid side (11,080 resting ≥ 2,000 ✓) ≈ $1.63/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | SELL | 25.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~25.3% of ask side (10,290 resting ≥ 10,000 ✓) ≈ $3.16/day (pool ÷ 2 markets) |
| …and 397 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 95¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **40.0** |

`yours 40.0 / Σ 40.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> SELL 40 @ 5¢ → $5.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 43 (40 yours) | ×0.1^0 = 43.0 |
|  | 14¢ | 50 | ×0.1^9 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **43.0** |

`yours 40.0 / Σ 43.0 = 93.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.0% = $5.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem`
2. `usgubewc-usgub-me-2026-11-03-rep` ← this one

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
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 40 @ 92¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 500,000 | ×0.1^90 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $4.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 6,600 (5,000 yours) | ×0.1^0 = 6,600.0 |
| | | **Σ** | **6,600.0** |

`yours 5,000.0 / Σ 6,600.0 = 75.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.8% = $4.73/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> BUY 29 @ 94¢ → $4.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 39 (29 yours) | ×0.1^0 = 39.0 |
|  | 54¢ | 500 | ×0.1^40 = 0.0 |
|  | 2¢ | 300,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **39.0** |

`yours 29.0 / Σ 39.0 = 74.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 74.4% = $4.65/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 40 @ 12¢ → $2.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 65 (40 yours) | ×0.2^0 = 65.0 |
|  | 10¢ | 45 | ×0.2^2 = 1.8 |
|  | 1¢ | 200,510 | ×0.2^11 = 0.0 |
| | | **Σ** | **66.8** |

`yours 40.0 / Σ 66.8 = 59.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 59.9% = $2.30/day`  

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
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> SELL 40 @ 4¢ → $3.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 68 (40 yours) | ×0.1^0 = 68.0 |
|  | 98¢ | 208,263 | ×0.1^94 = 0.0 |
| | | **Σ** | **68.0** |

`yours 40.0 / Σ 68.0 = 58.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.8% = $3.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-dem</code> SELL 50 @ 8¢ → $3.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 86 (50 yours) | ×0.1^0 = 86.0 |
|  | 98¢ | 265,767 | ×0.1^90 = 0.0 |
| | | **Σ** | **86.0** |

`yours 50.0 / Σ 86.0 = 58.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.1% = $3.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem` ← this one
2. `ussewc-usse-ar-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> SELL 40 @ 5¢ → $3.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 70 (40 yours) | ×0.1^0 = 70.0 |
|  | 98¢ | 208,263 | ×0.1^93 = 0.0 |
| | | **Σ** | **70.0** |

`yours 40.0 / Σ 70.0 = 57.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.1% = $3.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $3.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 70 (40 yours) | ×0.1^0 = 70.0 |
|  | 98¢ | 130,700 | ×0.1^94 = 0.0 |
| | | **Σ** | **70.0** |

`yours 40.0 / Σ 70.0 = 57.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.1% = $3.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $3.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,700 (2,000 yours) | ×0.1^0 = 3,700.0 |
| | | **Σ** | **3,700.0** |

`yours 2,000.0 / Σ 3,700.0 = 54.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 54.1% = $3.38/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $3.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 97¢ | 60 | ×0.1^1 = 6.0 |
|  | 99¢ | 19,445 | ×0.1^3 = 19.4 |
| | | **Σ** | **75.4** |

`yours 40.0 / Σ 75.4 = 53.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 53.0% = $3.31/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-dem</code> BUY 40 @ 95¢ → $3.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 79 (40 yours) | ×0.1^0 = 79.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **79.0** |

`yours 40.0 / Σ 79.0 = 50.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.6% = $3.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem` ← this one
2. `usgubewc-usgub-me-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 30 @ 34¢ → $2.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 30 (30 yours) | ×0.2^0 = 30.0 |
|  | 35¢ | 135 | ×0.2^1 = 27.0 |
|  | 37¢ | 361 | ×0.2^3 = 2.9 |
|  | 98¢ | 80,046 | ×0.2^64 = 0.0 |
| | | **Σ** | **59.9** |

`yours 30.0 / Σ 59.9 = 50.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 50.1% = $2.09/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215` ← this one
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 50 @ 4¢ → $1.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 116 (50 yours) | ×0.2^0 = 116.0 |
|  | 6¢ | 295 | ×0.2^2 = 11.8 |
|  | 8¢ | 500 | ×0.2^4 = 0.8 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^93 = 0.0 |
| | | **Σ** | **128.6** |

`yours 50.0 / Σ 128.6 = 38.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.9% = $1.50/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 30 @ 8¢ → $1.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 36 (30 yours) | ×0.2^0 = 36.0 |
|  | 7¢ | 101 | ×0.2^1 = 20.3 |
|  | 2¢ | 400,250 | ×0.2^6 = 25.6 |
| | | **Σ** | **81.9** |

`yours 30.0 / Σ 81.9 = 36.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 36.6% = $1.53/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215` ← this one
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> SELL 40 @ 96¢ → $2.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 97¢ | 257 | ×0.1^1 = 25.7 |
|  | 99¢ | 8,196 | ×0.1^3 = 8.2 |
| | | **Σ** | **123.9** |

`yours 40.0 / Σ 123.9 = 32.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 32.3% = $2.02/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 40 @ 10¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 108 (40 yours) | ×0.1^0 = 108.0 |
|  | 11¢ | 224 | ×0.1^1 = 22.4 |
|  | 98¢ | 65,450 | ×0.1^88 = 0.0 |
| | | **Σ** | **130.4** |

`yours 40.0 / Σ 130.4 = 30.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 30.7% = $1.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $1.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 16,700 (5,000 yours) | ×0.1^0 = 16,700.0 |
| | | **Σ** | **16,700.0** |

`yours 5,000.0 / Σ 16,700.0 = 29.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 29.9% = $1.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 30 @ 26¢ → $7.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 103 (30 yours) | ×0.2^0 = 103.0 |
|  | 24¢ | 7 | ×0.2^2 = 0.3 |
|  | 12¢ | 116 | ×0.2^14 = 0.0 |
|  | 2¢ | 100 | ×0.2^24 = 0.0 |
|  | 1¢ | 10,200 | ×0.2^25 = 0.0 |
| | | **Σ** | **103.3** |

`yours 30.0 / Σ 103.3 = 29.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 29.0% = $7.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>pntcbk-wnba-white-2027-06-30-roywhi</code> BUY 6,000 @ 2¢ → $33.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 21 | ×0.9^0 = 21.0 |
| ▶ | 2¢ | 22,500 (6,000 yours) | ×0.9^1 = 20,250.0 |
| | | **Σ** | **20,271.0** |

`yours 5,400.0 / Σ 20,271.0 = 26.6%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 26.6% = $33.30/day`  

</details>
<details><summary><code>mlaec-isrpol-pm-2026-10-27-bennet</code> BUY 50 @ 31¢ → $0.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 31¢ | 188 (50 yours) | ×0.1^0 = 188.0 |
|  | 28¢ | 21 | ×0.1^3 = 0.0 |
|  | 27¢ | 646 | ×0.1^4 = 0.1 |
|  | 18¢ | 150 | ×0.1^13 = 0.0 |
|  | 12¢ | 250 | ×0.1^19 = 0.0 |
|  | 5¢ | 500 | ×0.1^26 = 0.0 |
|  | 1¢ | 50,200 | ×0.1^30 = 0.0 |
| | | **Σ** | **188.1** |

`yours 50.0 / Σ 188.1 = 26.6%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 26.6% = $0.33/day`  

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 40 @ 95¢ → $1.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 152 (40 yours) | ×0.1^0 = 152.0 |
|  | 1¢ | 1,950 | ×0.1^94 = 0.0 |
| | | **Σ** | **152.0** |

`yours 40.0 / Σ 152.0 = 26.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.3% = $1.64/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nh-2026-11-03-rep</code> BUY 30 @ 80¢ → $1.63/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 30 (30 yours) | ×0.1^0 = 30.0 |
|  | 79¢ | 850 | ×0.1^1 = 85.0 |
|  | 1¢ | 10,200 | ×0.1^79 = 0.0 |
| | | **Σ** | **115.0** |

`yours 30.0 / Σ 115.0 = 26.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.1% = $1.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nh-2026-11-03-dem`
2. `usgubewc-usgub-nh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 20 @ 25¢ → $3.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 79 (20 yours) | ×0.25^0 = 79.0 |
|  | 34¢ | 99 | ×0.25^9 = 0.0 |
|  | 50¢ | 25 | ×0.25^25 = 0.0 |
|  | 99¢ | 10,087 | ×0.25^74 = 0.0 |
| | | **Σ** | **79.0** |

`yours 20.0 / Σ 79.0 = 25.3%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 25.3% = $3.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (35,945 resting) | ~88.4% | ~$22.11 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (36,740 resting) | ~75.2% | ~$18.80 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (74,418 resting) | ~17.6% | ~$13.21 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (62,023 resting) | ~17.4% | ~$13.03 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (292,344 resting) | ~7.8% | ~$5.86 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (11,794 resting) | ~15.7% | ~$3.93 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,634 resting) | ~4.7% | ~$3.50 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,039,743 resting) | ~4.6% | ~$3.47 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (815,483 resting) | ~4.4% | ~$3.30 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (688,162 resting) | ~3.8% | ~$2.88 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,045,724 resting) | ~3.2% | ~$2.38 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,071,657 resting) | ~2.9% | ~$2.14 |

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
| 2026-08-13 1:11 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-12 11:02 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-12 9:32 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-12 8:05 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:01 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 7:05 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:06 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 5:06 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 5:01 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 3:30 PM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
