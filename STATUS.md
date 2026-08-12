# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-12 2:46 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$170.32/day estimated (ceiling, not promise — details below)

**Earned:** $2,447.06 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-10: **$557.62** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-09: **$62.24** · 2026-08-08: **$54.78** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$17.49/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$17.18/day), `ewc-usgub-ca-2026-11-03-stehil` (~$13.30/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$170.32/day (~$7.10/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 24.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,548 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~87.4% of ask side (5,318 resting ≥ 5,000 ✓) ≈ $21.84/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 7.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~80.3% of bid side (90,618 resting ≥ 5,000 ✓) ≈ $3.09/day (pool ÷ 13 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~78.9% of ask side (65,805 resting ≥ 2,000 ✓) ≈ $4.93/day (pool ÷ 2 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 11.0¢ | 24 | 0 | $25.00 | ✅ scoring — ~70.5% of ask side (9,181 resting ≥ 2,000 ✓) ≈ $8.81/day |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~68.5% of bid side (50,371 resting ≥ 5,000 ✓) ≈ $2.63/day (pool ÷ 13 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~62.3% of bid side (3,210 resting ≥ 2,000 ✓) ≈ $3.89/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.5% of ask side (8,805 resting ≥ 2,000 ✓) ≈ $3.85/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~54.1% of bid side (3,700 resting ≥ 2,000 ✓) ≈ $3.38/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 14.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~53.8% of bid side (200,832 resting ≥ 5,000 ✓) ≈ $2.07/day (pool ÷ 13 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 44.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~53.1% of ask side (204,071 resting ≥ 2,000 ✓) ≈ $3.32/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~52.6% of bid side (3,800 resting ≥ 2,000 ✓) ≈ $3.29/day (pool ÷ 2 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 9.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~52.3% of bid side (20,706 resting ≥ 2,000 ✓) ≈ $6.54/day |
| `usgubewc-usgub-me-2026-11-03-dem` | BUY | 90.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~50.4% of bid side (500,683 resting ≥ 2,000 ✓) ≈ $3.15/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 90.0¢ | 40 | 1 | $25.00 | ✅ scoring — ~50.0% of bid side (500,244 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 93.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~46.4% of bid side (500,351 resting ≥ 2,000 ✓) ≈ $2.90/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~45.5% of bid side (5,344 resting ≥ 5,000 ✓) ≈ $11.36/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~44.4% of bid side (510,340 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 90.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~43.0% of bid side (510,585 resting ≥ 2,000 ✓) ≈ $2.69/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 8.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~38.5% of bid side (400,649 resting ≥ 5,000 ✓) ≈ $1.60/day (pool ÷ 12 markets) |
| `ussewc-usse-de-2026-11-03-rep` | SELL | 6.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~33.9% of ask side (138,945 resting ≥ 2,000 ✓) ≈ $2.12/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 40.0¢ | 58 | 0 | $100.00 | ✅ scoring — ~32.6% of ask side (83,104 resting ≥ 5,000 ✓) ≈ $1.36/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 15.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~32.6% of bid side (300,595 resting ≥ 5,000 ✓) ≈ $1.26/day (pool ÷ 13 markets) |
| `pandc-anydis-2027-12-31` | BUY | 14.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~32.5% of bid side (10,397 resting ≥ 10,000 ✓) ≈ $4.07/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 1 | $25.00 | ✅ scoring — ~32.3% of bid side (2,600 resting ≥ 2,000 ✓) ≈ $2.02/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 13.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~28.8% of ask side (69,235 resting ≥ 5,000 ✓) ≈ $1.20/day (pool ÷ 12 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~28.6% of ask side (273,849 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 37.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~28.0% of bid side (400,347 resting ≥ 5,000 ✓) ≈ $1.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 34.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~26.1% of ask side (82,433 resting ≥ 5,000 ✓) ≈ $1.09/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 13.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~25.3% of bid side (100,617 resting ≥ 5,000 ✓) ≈ $0.97/day (pool ÷ 13 markets) |
| …and 431 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 17 @ 24¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 17 (17 yours) | ×0.2^0 = 17.0 |
|  | 1¢ | 300,531 | ×0.2^23 = 0.0 |
| | | **Σ** | **17.0** |

`yours 17.0 / Σ 17.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 24¢ → $21.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 25¢ | 7 | ×0.2^1 = 1.4 |
|  | 28¢ | 1 | ×0.2^4 = 0.0 |
|  | 29¢ | 134 | ×0.2^5 = 0.0 |
|  | 32¢ | 23 | ×0.2^8 = 0.0 |
|  | 42¢ | 66 | ×0.2^18 = 0.0 |
|  | 99¢ | 5,078 | ×0.2^75 = 0.0 |
| | | **Σ** | **11.4** |

`yours 10.0 / Σ 11.4 = 87.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 87.4% = $21.84/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 40 @ 7¢ → $3.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 43 (40 yours) | ×0.2^0 = 43.0 |
|  | 5¢ | 26 | ×0.2^2 = 1.0 |
|  | 1¢ | 90,549 | ×0.2^6 = 5.8 |
| | | **Σ** | **49.8** |

`yours 40.0 / Σ 49.8 = 80.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 80.3% = $3.09/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53` ← this one
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 4¢ → $4.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 6¢ | 50 | ×0.1^2 = 0.5 |
|  | 7¢ | 170 | ×0.1^3 = 0.2 |
|  | 9¢ | 85 | ×0.1^5 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^94 = 0.0 |
| | | **Σ** | **50.7** |

`yours 40.0 / Σ 50.7 = 78.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 78.9% = $4.93/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 24 @ 11¢ → $8.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 34 (24 yours) | ×0.1^0 = 33.9 |
|  | 17¢ | 62 | ×0.1^6 = 0.0 |
|  | 18¢ | 348 | ×0.1^7 = 0.0 |
|  | 19¢ | 5 | ×0.1^8 = 0.0 |
|  | 33¢ | 300 | ×0.1^22 = 0.0 |
|  | 35¢ | 151 | ×0.1^24 = 0.0 |
|  | 99¢ | 8,281 | ×0.1^88 = 0.0 |
| | | **Σ** | **33.9** |

`yours 23.9 / Σ 33.9 = 70.5%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 70.5% = $8.81/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 100 @ 18¢ → $2.63/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 146 (100 yours) | ×0.2^0 = 146.0 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **146.0** |

`yours 100.0 / Σ 146.0 = 68.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.5% = $2.63/day`  

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
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $3.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,210 (2,000 yours) | ×0.1^0 = 3,210.0 |
| | | **Σ** | **3,210.0** |

`yours 2,000.0 / Σ 3,210.0 = 62.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 62.3% = $3.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> SELL 40 @ 10¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 14¢ | 138 | ×0.1^4 = 0.0 |
|  | 15¢ | 40 | ×0.1^5 = 0.0 |
|  | 16¢ | 40 | ×0.1^6 = 0.0 |
|  | 99¢ | 8,522 | ×0.1^89 = 0.0 |
| | | **Σ** | **65.0** |

`yours 40.0 / Σ 65.0 = 61.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.5% = $3.85/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $3.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,700 (2,000 yours) | ×0.1^0 = 3,700.0 |
| | | **Σ** | **3,700.0** |

`yours 2,000.0 / Σ 3,700.0 = 54.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 54.1% = $3.38/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 20 @ 14¢ → $2.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 37 (20 yours) | ×0.2^0 = 37.0 |
|  | 10¢ | 45 | ×0.2^4 = 0.1 |
|  | 9¢ | 341 | ×0.2^5 = 0.1 |
|  | 1¢ | 200,409 | ×0.2^13 = 0.0 |
| | | **Σ** | **37.2** |

`yours 20.0 / Σ 37.2 = 53.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.8% = $2.07/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 40 @ 44¢ → $3.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 44¢ | 75 (40 yours) | ×0.1^0 = 75.0 |
|  | 45¢ | 4 | ×0.1^1 = 0.4 |
|  | 50¢ | 40 | ×0.1^6 = 0.0 |
|  | 51¢ | 100 | ×0.1^7 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^54 = 0.0 |
| | | **Σ** | **75.4** |

`yours 40.0 / Σ 75.4 = 53.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 53.1% = $3.32/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $3.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,800 (2,000 yours) | ×0.1^0 = 3,800.0 |
| | | **Σ** | **3,800.0** |

`yours 2,000.0 / Σ 3,800.0 = 52.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 52.6% = $3.29/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 40 @ 9¢ → $6.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 76 (40 yours) | ×0.1^0 = 76.4 |
|  | 5¢ | 99 | ×0.1^4 = 0.0 |
|  | 3¢ | 80 | ×0.1^6 = 0.0 |
|  | 2¢ | 10,250 | ×0.1^7 = 0.0 |
| | | **Σ** | **76.4** |

`yours 40.0 / Σ 76.4 = 52.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 52.3% = $6.54/day`  

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-dem</code> BUY 40 @ 90¢ → $3.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 89¢ | 393 | ×0.1^1 = 39.3 |
|  | 86¢ | 50 | ×0.1^4 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^88 = 0.0 |
| | | **Σ** | **79.3** |

`yours 40.0 / Σ 79.3 = 50.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.4% = $3.15/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem` ← this one
2. `usgubewc-usgub-me-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 90¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 91¢ | 4 | ×0.1^0 = 4.0 |
| ▶ | 90¢ | 40 (40 yours) | ×0.1^1 = 4.0 |
|  | 2¢ | 500,000 | ×0.1^89 = 0.0 |
| | | **Σ** | **8.0** |

`yours 4.0 / Σ 8.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 93¢ → $2.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 86 (40 yours) | ×0.1^0 = 86.0 |
|  | 91¢ | 25 | ×0.1^2 = 0.3 |
|  | 51¢ | 40 | ×0.1^42 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **86.2** |

`yours 40.0 / Σ 86.2 = 46.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 46.4% = $2.90/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 10 @ 20¢ → $11.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 22 (10 yours) | ×0.2^0 = 22.0 |
|  | 16¢ | 1 | ×0.2^4 = 0.0 |
|  | 14¢ | 3 | ×0.2^6 = 0.0 |
|  | 13¢ | 3 | ×0.2^7 = 0.0 |
|  | 12¢ | 100 | ×0.2^8 = 0.0 |
|  | 2¢ | 16 | ×0.2^18 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **22.0** |

`yours 10.0 / Σ 22.0 = 45.5%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 45.5% = $11.36/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 40 @ 95¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 91¢ | 50 | ×0.1^4 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **90.0** |

`yours 40.0 / Σ 90.0 = 44.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.4% = $2.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 40 @ 90¢ → $2.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 88¢ | 295 | ×0.1^2 = 3.0 |
|  | 2¢ | 500,000 | ×0.1^88 = 0.0 |
| | | **Σ** | **93.0** |

`yours 40.0 / Σ 93.0 = 43.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 43.0% = $2.69/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 40 @ 8¢ → $1.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 48 (40 yours) | ×0.2^0 = 48.0 |
|  | 7¢ | 151 | ×0.2^1 = 30.3 |
|  | 2¢ | 400,250 | ×0.2^6 = 25.6 |
| | | **Σ** | **103.9** |

`yours 40.0 / Σ 103.9 = 38.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 38.5% = $1.60/day`  

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
<details><summary><code>ussewc-usse-de-2026-11-03-rep</code> SELL 40 @ 6¢ → $2.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 118 (40 yours) | ×0.1^0 = 118.0 |
|  | 98¢ | 130,700 | ×0.1^92 = 0.0 |
| | | **Σ** | **118.0** |

`yours 40.0 / Σ 118.0 = 33.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 33.9% = $2.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-de-2026-11-03-dem`
2. `ussewc-usse-de-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 58 @ 40¢ → $1.36/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 174 (58 yours) | ×0.2^0 = 173.6 |
|  | 43¢ | 360 | ×0.2^3 = 2.9 |
|  | 44¢ | 0 | ×0.2^4 = 0.0 |
|  | 63¢ | 299 | ×0.2^23 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^58 = 0.0 |
| | | **Σ** | **176.5** |

`yours 57.6 / Σ 176.5 = 32.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 32.6% = $1.36/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 8 @ 15¢ → $1.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 24 (8 yours) | ×0.2^0 = 23.8 |
|  | 9¢ | 5 | ×0.2^6 = 0.0 |
|  | 1¢ | 300,566 | ×0.2^14 = 0.0 |
| | | **Σ** | **23.8** |

`yours 7.8 / Σ 23.8 = 32.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.6% = $1.26/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> BUY 20 @ 14¢ → $4.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 50 (20 yours) | ×0.25^0 = 50.0 |
|  | 13¢ | 46 | ×0.25^1 = 11.5 |
|  | 1¢ | 10,301 | ×0.25^13 = 0.0 |
| | | **Σ** | **61.5** |

`yours 20.0 / Σ 61.5 = 32.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 32.5% = $4.07/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $2.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 400 | ×0.1^0 = 400.0 |
| ▶ | 1¢ | 2,200 (2,000 yours) | ×0.1^1 = 220.0 |
| | | **Σ** | **620.0** |

`yours 200.0 / Σ 620.0 = 32.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 32.3% = $2.02/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 40 @ 13¢ → $1.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 139 (40 yours) | ×0.2^0 = 139.0 |
|  | 19¢ | 780 | ×0.2^6 = 0.0 |
|  | 22¢ | 20 | ×0.2^9 = 0.0 |
|  | 25¢ | 1,000 | ×0.2^12 = 0.0 |
|  | 50¢ | 25 | ×0.2^37 = 0.0 |
|  | 98¢ | 65,046 | ×0.2^85 = 0.0 |
| | | **Σ** | **139.0** |

`yours 40.0 / Σ 139.0 = 28.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 28.8% = $1.20/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230` ← this one
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> SELL 40 @ 10¢ → $1.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 140 (40 yours) | ×0.1^0 = 140.0 |
|  | 51¢ | 40 | ×0.1^41 = 0.0 |
|  | 98¢ | 265,567 | ×0.1^88 = 0.0 |
| | | **Σ** | **140.0** |

`yours 40.0 / Σ 140.0 = 28.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.6% = $1.79/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> BUY 40 @ 37¢ → $1.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 142 (40 yours) | ×0.2^0 = 142.0 |
|  | 36¢ | 5 | ×0.2^1 = 1.0 |
|  | 34¢ | 0 | ×0.2^3 = 0.0 |
|  | 2¢ | 400,000 | ×0.2^35 = 0.0 |
| | | **Σ** | **143.0** |

`yours 40.0 / Σ 143.0 = 28.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 28.0% = $1.17/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205` ← this one
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 40 @ 34¢ → $1.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 153 (40 yours) | ×0.2^0 = 153.0 |
|  | 45¢ | 9 | ×0.2^11 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^64 = 0.0 |
| | | **Σ** | **153.0** |

`yours 40.0 / Σ 153.0 = 26.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 26.1% = $1.09/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 22 @ 13¢ → $0.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 87 (22 yours) | ×0.2^0 = 87.0 |
|  | 1¢ | 100,530 | ×0.2^12 = 0.0 |
| | | **Σ** | **87.0** |

`yours 22.0 / Σ 87.0 = 25.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.3% = $0.97/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,634 resting) | ~70.0% | ~$17.49 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (61,212 resting) | ~22.9% | ~$17.18 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (270,298 resting) | ~17.7% | ~$13.30 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (71,780 resting) | ~16.3% | ~$12.19 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,066,376 resting) | ~14.3% | ~$10.73 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,555 resting) | ~40.8% | ~$10.19 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,125 resting) | ~27.5% | ~$6.87 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (859,842 resting) | ~6.1% | ~$4.56 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (144,014 resting) | ~4.6% | ~$3.46 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (126,164 resting) | ~13.5% | ~$3.36 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (262,175 resting) | ~3.5% | ~$2.61 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (617,378 resting) | ~9.3% | ~$2.33 |

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
| 2026-08-12 2:46 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 1:09 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:17 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:31 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:24 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:10 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:03 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 10:48 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 10:35 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 10:28 PM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
