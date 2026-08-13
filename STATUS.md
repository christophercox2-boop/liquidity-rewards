# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 7:43 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$140.69/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — BUY at the best price, ~$13.36/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$10.86/day), `apdc-jerpowgov-2026-08-31` (~$9.04/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$140.69/day (~$5.86/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-48` | BUY | 14.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (50,410 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 13.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (100,435 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 86.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~99.2% of bid side (12,185 resting ≥ 2,000 ✓) ≈ $6.20/day (pool ÷ 2 markets) |
| `dccc-measles-us-2026-12-31-gt3500` | BUY | 76.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~96.1% of bid side (10,850 resting ≥ 10,000 ✓) ≈ $4.00/day (pool ÷ 6 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~91.6% of ask side (5,400 resting ≥ 5,000 ✓) ≈ $22.89/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | SELL | 4.0¢ | 85 | 0 | $25.00 | ✅ scoring — ~82.6% of ask side (137,153 resting ≥ 2,000 ✓) ≈ $5.16/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 12.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~75.5% of ask side (203,113 resting ≥ 2,000 ✓) ≈ $4.72/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-rep` | BUY | 17.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (15,443 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 17.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~70.4% of bid side (10,656 resting ≥ 2,000 ✓) ≈ $4.40/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-dem` | BUY | 87.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~68.2% of bid side (590,249 resting ≥ 2,000 ✓) ≈ $4.26/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 83.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~58.8% of bid side (10,242 resting ≥ 2,000 ✓) ≈ $3.68/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | SELL | 18.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~52.6% of ask side (7,318 resting ≥ 2,000 ✓) ≈ $3.29/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | SELL | 88.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~51.3% of ask side (7,391 resting ≥ 2,000 ✓) ≈ $3.21/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-dem` | BUY | 90.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~44.4% of bid side (512,745 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~37.8% of ask side (12,977 resting ≥ 2,000 ✓) ≈ $2.36/day (pool ÷ 2 markets) |
| `tec-cbb-champ-2027-04-05-w-wisc` | BUY | 1.0¢ | 5,000 | 0 | $500.00 | ✅ scoring — ~37.7% of bid side (13,245 resting ≥ 2,500 ✓) ≈ $1.29/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 6.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~34.4% of ask side (77,504 resting ≥ 5,000 ✓) ≈ $1.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~30.9% of bid side (300,490 resting ≥ 5,000 ✓) ≈ $1.19/day (pool ÷ 13 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 4,971 | 0 | $25.00 | ✅ scoring — ~29.8% of bid side (16,671 resting ≥ 2,000 ✓) ≈ $1.86/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~29.8% of bid side (300,721 resting ≥ 5,000 ✓) ≈ $1.15/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-stmry` | BUY | 1.0¢ | 5,000 | 0 | $500.00 | ✅ scoring — ~27.9% of bid side (17,901 resting ≥ 2,500 ✓) ≈ $0.96/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~27.8% of ask side (91,881 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 13 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~26.6% of bid side (18,786 resting ≥ 2,000 ✓) ≈ $1.66/day (pool ÷ 2 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 8.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~22.5% of bid side (20,726 resting ≥ 2,000 ✓) ≈ $2.81/day |
| `usgubewc-usgub-ma-2026-11-03-dem` | BUY | 97.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~20.8% of bid side (2,102 resting ≥ 2,000 ✓) ≈ $1.30/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 16.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~19.3% of ask side (79,360 resting ≥ 5,000 ✓) ≈ $0.74/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 2.0¢ | 14 | 0 | $100.00 | ✅ scoring — ~18.7% of ask side (78,013 resting ≥ 5,000 ✓) ≈ $0.72/day (pool ÷ 13 markets) |
| `usgubewc-usgub-mn-2026-11-03-rep` | SELL | 18.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~15.4% of ask side (204,728 resting ≥ 2,000 ✓) ≈ $0.96/day (pool ÷ 2 markets) |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | BUY | 3.0¢ | 2,000 | 6 | $250.00 | ✅ scoring — ~14.4% of bid side (13,507 resting ≥ 5,000 ✓) ≈ $17.99/day |
| `usgubewc-usgub-ma-2026-11-03-rep` | SELL | 9.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~13.3% of ask side (7,741 resting ≥ 2,000 ✓) ≈ $0.83/day (pool ÷ 2 markets) |
| …and 195 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 14¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 9¢ | 0 | ×0.2^5 = 0.0 |
|  | 2¢ | 50,200 | ×0.2^12 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 10 @ 13¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 8¢ | 5 | ×0.2^5 = 0.0 |
|  | 1¢ | 100,420 | ×0.2^12 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 50 @ 86¢ → $6.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 86¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 85¢ | 4 | ×0.1^1 = 0.4 |
|  | 82¢ | 150 | ×0.1^4 = 0.0 |
|  | 8¢ | 31 | ×0.1^78 = 0.0 |
|  | 1¢ | 11,950 | ×0.1^85 = 0.0 |
| | | **Σ** | **50.4** |

`yours 50.0 / Σ 50.4 = 99.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.2% = $6.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>dccc-measles-us-2026-12-31-gt3500</code> BUY 10 @ 76¢ → $4.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 76¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 72¢ | 104 | ×0.25^4 = 0.4 |
|  | 38¢ | 1 | ×0.25^38 = 0.0 |
|  | 1¢ | 10,735 | ×0.25^75 = 0.0 |
| | | **Σ** | **10.4** |

`yours 10.0 / Σ 10.4 = 96.1%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 96.1% = $4.00/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500` ← this one
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 24¢ → $22.89/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 26¢ | 23 | ×0.2^2 = 0.9 |
|  | 32¢ | 68 | ×0.2^8 = 0.0 |
|  | 38¢ | 80 | ×0.2^14 = 0.0 |
|  | 99¢ | 5,219 | ×0.2^75 = 0.0 |
| | | **Σ** | **10.9** |

`yours 10.0 / Σ 10.9 = 91.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 91.6% = $22.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> SELL 85 @ 4¢ → $5.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 92 (85 yours) | ×0.1^0 = 92.0 |
|  | 6¢ | 1,091 | ×0.1^2 = 10.9 |
|  | 49¢ | 245 | ×0.1^45 = 0.0 |
|  | 50¢ | 5,000 | ×0.1^46 = 0.0 |
| | | **Σ** | **102.9** |

`yours 85.0 / Σ 102.9 = 82.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 82.6% = $5.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 40 @ 12¢ → $4.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 53 (40 yours) | ×0.1^0 = 53.0 |
|  | 19¢ | 12 | ×0.1^7 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^86 = 0.0 |
| | | **Σ** | **53.0** |

`yours 40.0 / Σ 53.0 = 75.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.5% = $4.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-rep</code> BUY 10 @ 17¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 14 (10 yours) | ×0.1^0 = 14.0 |
|  | 11¢ | 0 | ×0.1^6 = 0.0 |
|  | 7¢ | 30 | ×0.1^10 = 0.0 |
|  | 6¢ | 100 | ×0.1^11 = 0.0 |
|  | 1¢ | 15,299 | ×0.1^16 = 0.0 |
| | | **Σ** | **14.0** |

`yours 10.0 / Σ 14.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem`
2. `usgubewc-usgub-mn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 11 @ 17¢ → $4.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 11 (11 yours) | ×0.1^0 = 10.6 |
|  | 15¢ | 445 | ×0.1^2 = 4.5 |
|  | 1¢ | 10,200 | ×0.1^16 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.6 / Σ 15.0 = 70.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.4% = $4.40/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-dem</code> BUY 15 @ 87¢ → $4.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 22 (15 yours) | ×0.1^0 = 22.0 |
|  | 8¢ | 27 | ×0.1^79 = 0.0 |
|  | 2¢ | 580,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **22.0** |

`yours 15.0 / Σ 22.0 = 68.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 68.2% = $4.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-mn-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 10 @ 83¢ → $3.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 83¢ | 17 (10 yours) | ×0.1^0 = 17.0 |
|  | 10¢ | 25 | ×0.1^73 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^82 = 0.0 |
| | | **Σ** | **17.0** |

`yours 10.0 / Σ 17.0 = 58.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.8% = $3.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> SELL 10 @ 18¢ → $3.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 19 (10 yours) | ×0.1^0 = 19.0 |
|  | 99¢ | 7,299 | ×0.1^81 = 0.0 |
| | | **Σ** | **19.0** |

`yours 10.0 / Σ 19.0 = 52.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 52.6% = $3.29/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> SELL 10 @ 88¢ → $3.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 17 (10 yours) | ×0.1^0 = 17.0 |
|  | 89¢ | 25 | ×0.1^1 = 2.5 |
|  | 98¢ | 50 | ×0.1^10 = 0.0 |
|  | 99¢ | 7,299 | ×0.1^11 = 0.0 |
| | | **Σ** | **19.5** |

`yours 10.0 / Σ 19.5 = 51.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 51.3% = $3.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-dem</code> BUY 20 @ 90¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 45 (20 yours) | ×0.1^0 = 45.0 |
|  | 86¢ | 200 | ×0.1^4 = 0.0 |
|  | 84¢ | 2,000 | ×0.1^6 = 0.0 |
| | | **Σ** | **45.0** |

`yours 20.0 / Σ 45.0 = 44.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.4% = $2.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ny-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $2.36/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 89 (40 yours) | ×0.1^0 = 89.0 |
|  | 97¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 12,848 | ×0.1^3 = 12.8 |
| | | **Σ** | **105.8** |

`yours 40.0 / Σ 105.8 = 37.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 37.8% = $2.36/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>tec-cbb-champ-2027-04-05-w-wisc</code> BUY 5,000 @ 1¢ → $1.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 13,245 (5,000 yours) | ×0.35^0 = 13,245.2 |
| | | **Σ** | **13,245.2** |

`yours 5,000.0 / Σ 13,245.2 = 37.7%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 37.7% = $1.29/day`  

<details><summary>÷ 73 markets in this race (40 known) — tap to list</summary>

1. `tec-cbb-champ-2027-04-05-w-ala`
2. `tec-cbb-champ-2027-04-05-w-ark`
3. `tec-cbb-champ-2027-04-05-w-arz`
4. `tec-cbb-champ-2027-04-05-w-aubrn`
5. `tec-cbb-champ-2027-04-05-w-bayl`
6. `tec-cbb-champ-2027-04-05-w-boise`
7. `tec-cbb-champ-2027-04-05-w-boscol`
8. `tec-cbb-champ-2027-04-05-w-butl`
9. `tec-cbb-champ-2027-04-05-w-byu`
10. `tec-cbb-champ-2027-04-05-w-cin`
11. `tec-cbb-champ-2027-04-05-w-clmsn`
12. `tec-cbb-champ-2027-04-05-w-colst`
13. `tec-cbb-champ-2027-04-05-w-creigh`
14. `tec-cbb-champ-2027-04-05-w-day`
15. `tec-cbb-champ-2027-04-05-w-duke`
16. `tec-cbb-champ-2027-04-05-w-fl`
17. `tec-cbb-champ-2027-04-05-w-flst`
18. `tec-cbb-champ-2027-04-05-w-george`
19. `tec-cbb-champ-2027-04-05-w-gnzg`
20. `tec-cbb-champ-2027-04-05-w-hou`
21. `tec-cbb-champ-2027-04-05-w-ill`
22. `tec-cbb-champ-2027-04-05-w-ind`
23. `tec-cbb-champ-2027-04-05-w-iowa`
24. `tec-cbb-champ-2027-04-05-w-iowast`
25. `tec-cbb-champ-2027-04-05-w-kan`
26. `tec-cbb-champ-2027-04-05-w-lou`
27. `tec-cbb-champ-2027-04-05-w-loych`
28. `tec-cbb-champ-2027-04-05-w-lsutig`
29. `tec-cbb-champ-2027-04-05-w-marq`
30. `tec-cbb-champ-2027-04-05-w-mia`
31. `tec-cbb-champ-2027-04-05-w-mich`
32. `tec-cbb-champ-2027-04-05-w-miss`
33. `tec-cbb-champ-2027-04-05-w-missr`
34. `tec-cbb-champ-2027-04-05-w-mphs`
35. `tec-cbb-champ-2027-04-05-w-mspst`
36. `tec-cbb-champ-2027-04-05-w-mst`
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 6¢ → $1.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 8¢ | 476 | ×0.2^2 = 19.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 97¢ | 65,717 | ×0.2^91 = 0.0 |
| | | **Σ** | **29.0** |

`yours 10.0 / Σ 29.0 = 34.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.4% = $1.32/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54` ← this one
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 18 @ 12¢ → $1.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 59 (18 yours) | ×0.2^0 = 59.4 |
|  | 1¢ | 300,431 | ×0.2^11 = 0.0 |
| | | **Σ** | **59.4** |

`yours 18.4 / Σ 59.4 = 30.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.9% = $1.19/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 18 @ 9¢ → $1.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 59 (18 yours) | ×0.2^0 = 58.8 |
|  | 1¢ | 300,662 | ×0.2^8 = 0.8 |
| | | **Σ** | **59.5** |

`yours 17.8 / Σ 59.5 = 29.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.8% = $1.15/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-stmry</code> BUY 5,000 @ 1¢ → $0.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 17,901 (5,000 yours) | ×0.35^0 = 17,901.0 |
| | | **Σ** | **17,901.0** |

`yours 5,000.0 / Σ 17,901.0 = 27.9%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 27.9% = $0.96/day`  

<details><summary>÷ 73 markets in this race (40 known) — tap to list</summary>

1. `tec-cbb-champ-2027-04-05-w-ala`
2. `tec-cbb-champ-2027-04-05-w-ark`
3. `tec-cbb-champ-2027-04-05-w-arz`
4. `tec-cbb-champ-2027-04-05-w-aubrn`
5. `tec-cbb-champ-2027-04-05-w-bayl`
6. `tec-cbb-champ-2027-04-05-w-boise`
7. `tec-cbb-champ-2027-04-05-w-boscol`
8. `tec-cbb-champ-2027-04-05-w-butl`
9. `tec-cbb-champ-2027-04-05-w-byu`
10. `tec-cbb-champ-2027-04-05-w-cin`
11. `tec-cbb-champ-2027-04-05-w-clmsn`
12. `tec-cbb-champ-2027-04-05-w-colst`
13. `tec-cbb-champ-2027-04-05-w-creigh`
14. `tec-cbb-champ-2027-04-05-w-day`
15. `tec-cbb-champ-2027-04-05-w-duke`
16. `tec-cbb-champ-2027-04-05-w-fl`
17. `tec-cbb-champ-2027-04-05-w-flst`
18. `tec-cbb-champ-2027-04-05-w-george`
19. `tec-cbb-champ-2027-04-05-w-gnzg`
20. `tec-cbb-champ-2027-04-05-w-hou`
21. `tec-cbb-champ-2027-04-05-w-ill`
22. `tec-cbb-champ-2027-04-05-w-ind`
23. `tec-cbb-champ-2027-04-05-w-iowa`
24. `tec-cbb-champ-2027-04-05-w-iowast`
25. `tec-cbb-champ-2027-04-05-w-kan`
26. `tec-cbb-champ-2027-04-05-w-lou`
27. `tec-cbb-champ-2027-04-05-w-loych`
28. `tec-cbb-champ-2027-04-05-w-lsutig`
29. `tec-cbb-champ-2027-04-05-w-marq`
30. `tec-cbb-champ-2027-04-05-w-mia`
31. `tec-cbb-champ-2027-04-05-w-mich`
32. `tec-cbb-champ-2027-04-05-w-miss`
33. `tec-cbb-champ-2027-04-05-w-missr`
34. `tec-cbb-champ-2027-04-05-w-mphs`
35. `tec-cbb-champ-2027-04-05-w-mspst`
36. `tec-cbb-champ-2027-04-05-w-mst`
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 20¢ → $1.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 36 (10 yours) | ×0.2^0 = 36.0 |
|  | 27¢ | 50 | ×0.2^7 = 0.0 |
|  | 29¢ | 0 | ×0.2^9 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 97¢ | 80,494 | ×0.2^77 = 0.0 |
| | | **Σ** | **36.0** |

`yours 10.0 / Σ 36.0 = 27.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.8% = $1.07/day`  

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
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $1.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 18,786 (5,000 yours) | ×0.1^0 = 18,786.0 |
| | | **Σ** | **18,786.0** |

`yours 5,000.0 / Σ 18,786.0 = 26.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.6% = $1.66/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 10 @ 8¢ → $2.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 43 (10 yours) | ×0.1^0 = 43.0 |
|  | 6¢ | 153 | ×0.1^2 = 1.5 |
|  | 3¢ | 80 | ×0.1^5 = 0.0 |
|  | 2¢ | 10,250 | ×0.1^6 = 0.0 |
| | | **Σ** | **44.5** |

`yours 10.0 / Σ 44.5 = 22.5%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 22.5% = $2.81/day`  

</details>
<details><summary><code>usgubewc-usgub-ma-2026-11-03-dem</code> BUY 40 @ 97¢ → $1.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 192 (40 yours) | ×0.1^0 = 191.9 |
|  | 1¢ | 1,910 | ×0.1^96 = 0.0 |
| | | **Σ** | **191.9** |

`yours 40.0 / Σ 191.9 = 20.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 20.8% = $1.30/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 10 @ 16¢ → $0.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 44 (10 yours) | ×0.2^0 = 44.0 |
|  | 19¢ | 647 | ×0.2^3 = 5.2 |
|  | 20¢ | 1,651 | ×0.2^4 = 2.6 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 83¢ | 0 | ×0.2^67 = 0.0 |
|  | 97¢ | 65,717 | ×0.2^81 = 0.0 |
| | | **Σ** | **51.8** |

`yours 10.0 / Σ 51.8 = 19.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.3% = $0.74/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 14 @ 2¢ → $0.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 52 (14 yours) | ×0.2^0 = 51.7 |
|  | 4¢ | 530 | ×0.2^2 = 21.2 |
|  | 6¢ | 413 | ×0.2^4 = 0.7 |
|  | 50¢ | 100 | ×0.2^48 = 0.0 |
|  | 97¢ | 65,717 | ×0.2^95 = 0.0 |
| | | **Σ** | **73.6** |

`yours 13.7 / Σ 73.6 = 18.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.7% = $0.72/day`  

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
10. `scc-senate-gop-2026-11-03-55` ← this one
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-rep</code> SELL 20 @ 18¢ → $0.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 130 (20 yours) | ×0.1^0 = 130.0 |
|  | 26¢ | 30 | ×0.1^8 = 0.0 |
|  | 27¢ | 1,020 | ×0.1^9 = 0.0 |
|  | 37¢ | 500 | ×0.1^19 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^80 = 0.0 |
| | | **Σ** | **130.0** |

`yours 20.0 / Σ 130.0 = 15.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 15.4% = $0.96/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem`
2. `usgubewc-usgub-mn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>pntcbk-wnba-freedom-2027-06-30-enekan</code> BUY 2,000 @ 3¢ → $17.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 376 | ×0.9^0 = 376.0 |
|  | 8¢ | 50 | ×0.9^1 = 45.0 |
|  | 7¢ | 51 | ×0.9^2 = 41.3 |
|  | 6¢ | 30 | ×0.9^3 = 21.9 |
|  | 5¢ | 800 | ×0.9^4 = 524.9 |
| ▶ | 3¢ | 12,000 (2,000 yours) | ×0.9^6 = 6,377.3 |
| | | **Σ** | **7,386.4** |

`yours 1,062.9 / Σ 7,386.4 = 14.4%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 14.4% = $17.99/day`  

</details>
<details><summary><code>usgubewc-usgub-ma-2026-11-03-rep</code> SELL 50 @ 9¢ → $0.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 375 (50 yours) | ×0.1^0 = 375.0 |
|  | 16¢ | 68 | ×0.1^7 = 0.0 |
|  | 99¢ | 7,298 | ×0.1^90 = 0.0 |
| | | **Σ** | **375.0** |

`yours 50.0 / Σ 375.0 = 13.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 13.3% = $0.83/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem`
2. `usgubewc-usgub-ma-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (48,796 resting) | ~17.8% | ~$13.36 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (63,611 resting) | ~14.5% | ~$10.86 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (6,497 resting) | ~36.1% | ~$9.04 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,001 resting) | ~28.3% | ~$7.08 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,266 resting) | ~24.7% | ~$6.17 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (65,658 resting) | ~8.0% | ~$6.01 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (539,526 resting) | ~7.5% | ~$5.65 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (293,836 resting) | ~7.3% | ~$5.44 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (136,016 resting) | ~13.3% | ~$3.31 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (644,986 resting) | ~4.1% | ~$3.10 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (688,145 resting) | ~4.0% | ~$3.01 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (18,569 resting) | ~4.9% | ~$2.45 |

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
| 2026-08-13 7:43 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 7:29 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 7:06 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:34 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:06 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 5:16 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 5:07 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 3:29 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 2:11 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 1:16 PM ET | ✅ ok | 2087 | $2853.72 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
