# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-14 12:03 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$463.44/day estimated (ceiling, not promise — details below)

**Earned:** $3,069.69 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-12: **$213.04** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-11: **$409.59** · 2026-08-10: **$557.62** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-rep` — SELL at the best price, ~$17.77/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$12.09/day), `ewc-usgub-oh-2026-11-03-dem` (~$6.97/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$463.44/day (~$19.31/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 95.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,047 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ks-2026-11-03-dem` | SELL | 20.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (130,829 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 36.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~98.0% of bid side (400,672 resting ≥ 5,000 ✓) ≈ $4.08/day (pool ÷ 12 markets) |
| `dccc-measles-us-2026-12-31-gt3500` | BUY | 76.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~92.6% of bid side (11,100 resting ≥ 10,000 ✓) ≈ $3.86/day (pool ÷ 6 markets) |
| `ewc-usp-party-2028-11-07-dem` | SELL | 80.0¢ | 100 | 0 | $300.00 | ✅ scoring — ~90.9% of ask side (10,088 resting ≥ 10,000 ✓) ≈ $68.18/day (pool ÷ 2 markets) |
| `ewc-usp-party-2028-11-07-rep` | SELL | 65.0¢ | 200 | 0 | $300.00 | ✅ scoring — ~87.0% of ask side (10,211 resting ≥ 10,000 ✓) ≈ $65.22/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~84.8% of bid side (340,566 resting ≥ 5,000 ✓) ≈ $3.26/day (pool ÷ 13 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | SELL | 9.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (2,285 resting ≥ 2,000 ✓) ≈ $5.21/day (pool ÷ 2 markets) |
| `ewc-usp-party-2028-11-07-dem` | BUY | 20.0¢ | 100 | 0 | $300.00 | ✅ scoring — ~80.0% of bid side (10,350 resting ≥ 10,000 ✓) ≈ $60.00/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 32.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~77.2% of ask side (91,836 resting ≥ 5,000 ✓) ≈ $2.97/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 16.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~76.2% of ask side (79,341 resting ≥ 5,000 ✓) ≈ $2.93/day (pool ÷ 13 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~75.5% of ask side (130,778 resting ≥ 2,000 ✓) ≈ $4.72/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 10.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~75.1% of bid side (302,475 resting ≥ 5,000 ✓) ≈ $2.89/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 7.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~73.9% of bid side (90,502 resting ≥ 5,000 ✓) ≈ $2.84/day (pool ÷ 13 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 10.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~71.4% of ask side (137,174 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | SELL | 30.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~71.4% of ask side (6,744 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~67.9% of ask side (77,331 resting ≥ 5,000 ✓) ≈ $2.61/day (pool ÷ 13 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 25.0¢ | 21 | 0 | $25.00 | ✅ scoring — ~67.7% of bid side (10,382 resting ≥ 2,000 ✓) ≈ $4.23/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-dem` | SELL | 12.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~66.7% of ask side (210,094 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `dccc-measles-us-2026-12-31-gt3000` | BUY | 79.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~66.4% of bid side (11,000 resting ≥ 10,000 ✓) ≈ $2.77/day (pool ÷ 6 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~60.8% of bid side (8,226 resting ≥ 2,000 ✓) ≈ $3.80/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-rep` | BUY | 86.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~60.0% of bid side (10,357 resting ≥ 2,000 ✓) ≈ $3.75/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~59.7% of ask side (65,542 resting ≥ 2,000 ✓) ≈ $3.73/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 20.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~56.4% of bid side (5,353 resting ≥ 5,000 ✓) ≈ $14.10/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 54.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~52.9% of ask side (82,536 resting ≥ 5,000 ✓) ≈ $2.20/day (pool ÷ 12 markets) |
| `usgubewc-usgub-fl-2026-11-03-dem` | SELL | 17.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~52.1% of ask side (272,248 resting ≥ 2,000 ✓) ≈ $3.26/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 10.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~50.0% of ask side (72,026 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 90.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (510,250 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-rep` | BUY | 85.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~50.0% of bid side (511,261 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-rep` | SELL | 10.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~47.8% of ask side (203,351 resting ≥ 2,000 ✓) ≈ $2.99/day (pool ÷ 2 markets) |
| …and 505 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 50 @ 95¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 8¢ | 47 | ×0.1^87 = 0.0 |
|  | 1¢ | 1,950 | ×0.1^94 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ks-2026-11-03-dem</code> SELL 20 @ 20¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 20 (20 yours) | ×0.1^0 = 20.0 |
|  | 73¢ | 84 | ×0.1^53 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^78 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem` ← this one
2. `ussewc-usse-ks-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 1 @ 36¢ → $4.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 36¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 28¢ | 21 | ×0.2^8 = 0.0 |
|  | 25¢ | 0 | ×0.2^11 = 0.0 |
|  | 22¢ | 0 | ×0.2^14 = 0.0 |
|  | 19¢ | 0 | ×0.2^17 = 0.0 |
|  | 16¢ | 0 | ×0.2^20 = 0.0 |
|  | 2¢ | 400,450 | ×0.2^34 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 98.0% = $4.08/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt3500</code> BUY 10 @ 76¢ → $3.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 76¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 72¢ | 204 | ×0.25^4 = 0.8 |
|  | 38¢ | 1 | ×0.25^38 = 0.0 |
|  | 1¢ | 10,885 | ×0.25^75 = 0.0 |
| | | **Σ** | **10.8** |

`yours 10.0 / Σ 10.8 = 92.6%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 92.6% = $3.86/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000`
2. `dccc-measles-us-2026-12-31-gt3500` ← this one
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>ewc-usp-party-2028-11-07-dem</code> SELL 100 @ 80¢ → $68.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 110 (100 yours) | ×0.2^0 = 110.0 |
|  | 99¢ | 9,978 | ×0.2^19 = 0.0 |
| | | **Σ** | **110.0** |

`yours 100.0 / Σ 110.0 = 90.9%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 90.9% = $68.18/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usp-party-2028-11-07-dem` ← this one
2. `ewc-usp-party-2028-11-07-rep`

</details>

</details>
<details><summary><code>ewc-usp-party-2028-11-07-rep</code> SELL 200 @ 65¢ → $65.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 210 (200 yours) | ×0.2^0 = 210.0 |
|  | 66¢ | 100 | ×0.2^1 = 20.0 |
|  | 99¢ | 9,901 | ×0.2^34 = 0.0 |
| | | **Σ** | **230.0** |

`yours 200.0 / Σ 230.0 = 87.0%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 87.0% = $65.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usp-party-2028-11-07-dem`
2. `ewc-usp-party-2028-11-07-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 5 @ 9¢ → $3.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 3¢ | 124 | ×0.2^6 = 0.0 |
|  | 1¢ | 340,437 | ×0.2^8 = 0.9 |
| | | **Σ** | **5.9** |

`yours 5.0 / Σ 5.9 = 84.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 84.8% = $3.26/day`  

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> SELL 50 @ 9¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 10¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,135 | ×0.1^90 = 0.0 |
| | | **Σ** | **60.0** |

`yours 50.0 / Σ 60.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-party-2028-11-07-dem</code> BUY 100 @ 20¢ → $60.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 125 (100 yours) | ×0.2^0 = 125.0 |
|  | 1¢ | 10,225 | ×0.2^19 = 0.0 |
| | | **Σ** | **125.0** |

`yours 100.0 / Σ 125.0 = 80.0%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 80.0% = $60.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usp-party-2028-11-07-dem` ← this one
2. `ewc-usp-party-2028-11-07-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 25 @ 32¢ → $2.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 33¢ | 37 | ×0.2^1 = 7.4 |
|  | 48¢ | 11 | ×0.2^16 = 0.0 |
|  | 50¢ | 90 | ×0.2^18 = 0.0 |
|  | 97¢ | 80,472 | ×0.2^65 = 0.0 |
| | | **Σ** | **32.4** |

`yours 25.0 / Σ 32.4 = 77.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 77.2% = $2.97/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 25 @ 16¢ → $2.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 19¢ | 647 | ×0.2^3 = 5.2 |
|  | 20¢ | 1,651 | ×0.2^4 = 2.6 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 83¢ | 0 | ×0.2^67 = 0.0 |
|  | 97¢ | 65,717 | ×0.2^81 = 0.0 |
| | | **Σ** | **32.8** |

`yours 25.0 / Σ 32.8 = 76.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 76.2% = $2.93/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 25 @ 10¢ → $2.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 7¢ | 1,019 | ×0.2^3 = 8.2 |
|  | 1¢ | 301,431 | ×0.2^9 = 0.2 |
| | | **Σ** | **33.3** |

`yours 25.0 / Σ 33.3 = 75.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 75.1% = $2.89/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 25 @ 7¢ → $2.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 27 (25 yours) | ×0.2^0 = 27.0 |
|  | 5¢ | 26 | ×0.2^2 = 1.0 |
|  | 1¢ | 90,449 | ×0.2^6 = 5.8 |
| | | **Σ** | **33.8** |

`yours 25.0 / Σ 33.8 = 73.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 73.9% = $2.84/day`  

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
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 25 @ 10¢ → $4.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 35 (25 yours) | ×0.1^0 = 35.0 |
|  | 41¢ | 6 | ×0.1^31 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^88 = 0.0 |
| | | **Σ** | **35.0** |

`yours 25.0 / Σ 35.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> SELL 25 @ 30¢ → $4.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 35 (25 yours) | ×0.1^0 = 35.0 |
|  | 36¢ | 49 | ×0.1^6 = 0.0 |
|  | 42¢ | 27 | ×0.1^12 = 0.0 |
|  | 99¢ | 6,633 | ×0.1^69 = 0.0 |
| | | **Σ** | **35.0** |

`yours 25.0 / Σ 35.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 25 @ 4¢ → $2.61/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 6¢ | 295 | ×0.2^2 = 11.8 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^93 = 0.0 |
| | | **Σ** | **36.8** |

`yours 25.0 / Σ 36.8 = 67.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.9% = $2.61/day`  

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
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 21 @ 25¢ → $4.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 31 (21 yours) | ×0.1^0 = 31.0 |
|  | 11¢ | 151 | ×0.1^14 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^24 = 0.0 |
| | | **Σ** | **31.0** |

`yours 21.0 / Σ 31.0 = 67.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 67.7% = $4.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-dem</code> SELL 20 @ 12¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 30 (20 yours) | ×0.1^0 = 30.0 |
|  | 20¢ | 100 | ×0.1^8 = 0.0 |
|  | 94¢ | 6 | ×0.1^82 = 0.0 |
|  | 98¢ | 203,325 | ×0.1^86 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem` ← this one
2. `ussewc-usse-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>dccc-measles-us-2026-12-31-gt3000</code> BUY 10 @ 79¢ → $2.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 77¢ | 81 | ×0.25^2 = 5.1 |
|  | 1¢ | 10,909 | ×0.25^78 = 0.0 |
| | | **Σ** | **15.1** |

`yours 10.0 / Σ 15.1 = 66.4%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 66.4% = $2.77/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000` ← this one
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $3.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 8,226 (5,000 yours) | ×0.1^0 = 8,226.0 |
| | | **Σ** | **8,226.0** |

`yours 5,000.0 / Σ 8,226.0 = 60.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.8% = $3.80/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-rep</code> BUY 15 @ 86¢ → $3.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 86¢ | 25 (15 yours) | ×0.1^0 = 25.0 |
|  | 74¢ | 100 | ×0.1^12 = 0.0 |
|  | 10¢ | 32 | ×0.1^76 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^85 = 0.0 |
| | | **Σ** | **25.0** |

`yours 15.0 / Σ 25.0 = 60.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.0% = $3.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem`
2. `usgubewc-usgub-tx-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 2¢ → $3.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 67 (40 yours) | ×0.1^0 = 67.0 |
|  | 98¢ | 65,250 | ×0.1^96 = 0.0 |
| | | **Σ** | **67.0** |

`yours 40.0 / Σ 67.0 = 59.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 59.7% = $3.73/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 25 @ 20¢ → $14.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 40 (25 yours) | ×0.2^0 = 40.0 |
|  | 18¢ | 107 | ×0.2^2 = 4.3 |
|  | 17¢ | 6 | ×0.2^3 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **44.3** |

`yours 25.0 / Σ 44.3 = 56.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 56.4% = $14.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 25 @ 54¢ → $2.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 54¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 55¢ | 111 | ×0.2^1 = 22.2 |
|  | 58¢ | 29 | ×0.2^4 = 0.0 |
|  | 59¢ | 100 | ×0.2^5 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^44 = 0.0 |
| | | **Σ** | **47.3** |

`yours 25.0 / Σ 47.3 = 52.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 52.9% = $2.20/day`  

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
<details><summary><code>usgubewc-usgub-fl-2026-11-03-dem</code> SELL 25 @ 17¢ → $3.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 48 (25 yours) | ×0.1^0 = 48.0 |
|  | 98¢ | 265,567 | ×0.1^81 = 0.0 |
| | | **Σ** | **48.0** |

`yours 25.0 / Σ 48.0 = 52.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 52.1% = $3.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-fl-2026-11-03-dem` ← this one
2. `usgubewc-usgub-fl-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 20 @ 10¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 30 (20 yours) | ×0.1^0 = 30.0 |
|  | 11¢ | 100 | ×0.1^1 = 10.0 |
|  | 38¢ | 13 | ×0.1^28 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^88 = 0.0 |
| | | **Σ** | **40.0** |

`yours 20.0 / Σ 40.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 25 @ 90¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 50 (25 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 500,000 | ×0.1^88 = 0.0 |
| | | **Σ** | **50.0** |

`yours 25.0 / Σ 50.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-rep</code> BUY 10 @ 85¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 20 (10 yours) | ×0.1^0 = 20.0 |
|  | 77¢ | 1,029 | ×0.1^8 = 0.0 |
|  | 70¢ | 12 | ×0.1^15 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^83 = 0.0 |
| | | **Σ** | **20.0** |

`yours 10.0 / Σ 20.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem`
2. `ussewc-usse-ms-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-rep</code> SELL 50 @ 10¢ → $2.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 100 (50 yours) | ×0.1^0 = 100.0 |
|  | 11¢ | 10 | ×0.1^1 = 1.0 |
|  | 12¢ | 358 | ×0.1^2 = 3.6 |
|  | 37¢ | 500 | ×0.1^27 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^88 = 0.0 |
| | | **Σ** | **104.6** |

`yours 50.0 / Σ 104.6 = 47.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 47.8% = $2.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem`
2. `usgubewc-usgub-mn-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-11 | ~$75.57 | $409.59 | 542% |

_2026-08-12 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (73,893 resting) | ~23.7% | ~$17.77 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (60,491 resting) | ~16.1% | ~$12.09 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (273,109 resting) | ~9.3% | ~$6.97 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (503,764 resting) | ~7.5% | ~$5.66 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,497 resting) | ~17.0% | ~$4.25 |
| `ewc-usse-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (71,290 resting) | ~53.9% | ~$3.37 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (133,350 resting) | ~12.5% | ~$3.12 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,035,237 resting) | ~3.2% | ~$2.38 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (680,346 resting) | ~2.8% | ~$2.10 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (635,041 resting) | ~8.3% | ~$2.08 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (281,872 resting) | ~1.7% | ~$1.24 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (66,288 resting) | ~19.8% | ~$1.24 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $1,180.25 |
| Skipped | $1.41 |
| **Total earned** | **$3,069.69** |

2234 reward rows · 41 days with rewards · 486 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-12 ⚠️ multi-day pending bucket | $213.04 | `████████` |
| 2026-08-11 | $409.59 | `███████████████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $1,606.37 | `████████████████████` |
| 2026-07 | $1,463.32 | `██████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $127.10 |
| `apdc-alito-2026-12-31` | $111.76 |
| `opdc-mcconnell-resign-2026-11-02` | $77.87 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $47.80 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $40.44 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.03 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `scc-senate-gop-2026-11-03-49` | $28.51 |
| `scc-senate-gop-2026-11-03-48` | $27.99 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-14 12:03 AM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-13 11:51 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-13 9:50 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-13 9:42 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-13 9:29 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-13 9:15 PM ET | ✅ ok | 2233 | $3069.20 |
| 2026-08-13 9:13 PM ET | ✅ ok | 2135 | $2961.97 |
| 2026-08-13 9:09 PM ET | ✅ ok | 2091 | $2881.72 |
| 2026-08-13 8:54 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 8:53 PM ET | ✅ ok | 2087 | $2853.72 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
