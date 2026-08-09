# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-08 9:12 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$140.43/day estimated (ceiling, not promise — details below)

**Earned:** $1,772.42 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-07: **$60.33** · 2026-08-06: **$52.21** · 2026-08-05: **$31.46** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usse-oh-2026-11-03-dem` — BUY at the best price, ~$21.18/day for 200 contracts. Runners-up: `ewc-usgub-ca-2026-11-03-xavbec` (~$18.05/day), `ewc-usgub-ca-2026-11-03-stehil` (~$11.85/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$140.43/day (~$5.85/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-49` | BUY | 29.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (50,610 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 43.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (80,554 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `pandc-anydis-2027-12-31` | BUY | 15.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~99.9% of bid side (10,975 resting ≥ 10,000 ✓) ≈ $12.49/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 49.0¢ | 115 | 0 | $100.00 | ✅ scoring — ~99.9% of bid side (80,656 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `lawec-cryptoleg-2026-12-31` | BUY | 27.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~99.7% of bid side (26,960 resting ≥ 2,000 ✓) ≈ $6.23/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 53.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~99.4% of bid side (80,318 resting ≥ 5,000 ✓) ≈ $4.14/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~97.6% of bid side (200,553 resting ≥ 5,000 ✓) ≈ $3.75/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~95.2% of ask side (48,664 resting ≥ 5,000 ✓) ≈ $3.97/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 25.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~92.6% of bid side (100,616 resting ≥ 5,000 ✓) ≈ $3.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 9.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~90.7% of bid side (5,594 resting ≥ 5,000 ✓) ≈ $3.78/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~86.7% of bid side (10,799 resting ≥ 5,000 ✓) ≈ $3.33/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 46.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~85.2% of ask side (48,199 resting ≥ 5,000 ✓) ≈ $3.55/day (pool ÷ 12 markets) |
| `pandc-anydis-2027-12-31` | SELL | 30.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~83.5% of ask side (10,981 resting ≥ 10,000 ✓) ≈ $10.44/day (pool ÷ 2 markets) |
| `lawec-cryptoleg-2026-12-31` | SELL | 39.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (31,119 resting ≥ 2,000 ✓) ≈ $5.21/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 22.0¢ | 7 | 3 | $100.00 | ✅ scoring — ~82.4% of bid side (85,488 resting ≥ 5,000 ✓) ≈ $3.43/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 65.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~75.7% of bid side (50,540 resting ≥ 5,000 ✓) ≈ $3.15/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 59.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~74.9% of ask side (63,044 resting ≥ 5,000 ✓) ≈ $3.12/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 12.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~73.5% of bid side (35,684 resting ≥ 2,000 ✓) ≈ $9.19/day |
| `scc-senate-gop-2026-11-03-51` | SELL | 26.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~70.9% of ask side (113,510 resting ≥ 5,000 ✓) ≈ $2.73/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~67.3% of bid side (80,599 resting ≥ 5,000 ✓) ≈ $2.81/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~57.1% of ask side (117,800 resting ≥ 5,000 ✓) ≈ $2.20/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 13.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~55.3% of ask side (2,408 resting ≥ 2,000 ✓) ≈ $6.92/day |
| `scc-senate-gop-2026-11-03-48` | BUY | 17.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~53.9% of bid side (50,437 resting ≥ 5,000 ✓) ≈ $2.07/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 73.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~47.8% of ask side (62,673 resting ≥ 5,000 ✓) ≈ $1.99/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~39.9% of bid side (80,482 resting ≥ 5,000 ✓) ≈ $1.66/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~39.9% of bid side (80,482 resting ≥ 5,000 ✓) ≈ $1.66/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~32.1% of bid side (80,599 resting ≥ 5,000 ✓) ≈ $1.34/day (pool ÷ 12 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 24.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~28.8% of bid side (5,504 resting ≥ 5,000 ✓) ≈ $7.21/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 11.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~28.5% of ask side (113,532 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 21.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~27.5% of ask side (100,249 resting ≥ 5,000 ✓) ≈ $1.06/day (pool ÷ 13 markets) |
| …and 48 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 0 @ 29¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 0 (0 yours) | ×0.2^0 = 0.0 |
|  | 16¢ | 0 | ×0.2^13 = 0.0 |
|  | 12¢ | 0 | ×0.2^17 = 0.0 |
|  | 11¢ | 45 | ×0.2^18 = 0.0 |
|  | 3¢ | 156 | ×0.2^26 = 0.0 |
|  | 2¢ | 50,209 | ×0.2^27 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 100.0%`  
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 1 @ 43¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 37¢ | 3 | ×0.2^6 = 0.0 |
|  | 18¢ | 100 | ×0.2^25 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^41 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> BUY 10 @ 15¢ → $12.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 8¢ | 101 | ×0.25^7 = 0.0 |
|  | 2¢ | 4 | ×0.25^13 = 0.0 |
|  | 1¢ | 10,860 | ×0.25^14 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.9%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 99.9% = $12.49/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 115 @ 49¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 115 (115 yours) | ×0.2^0 = 115.1 |
|  | 11¢ | 151 | ×0.2^38 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^47 = 0.0 |
| | | **Σ** | **115.1** |

`yours 115.0 / Σ 115.1 = 99.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.9% = $4.16/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195` ← this one
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
<details><summary><code>lawec-cryptoleg-2026-12-31</code> BUY 10 @ 27¢ → $6.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 24¢ | 23 | ×0.1^3 = 0.0 |
|  | 23¢ | 46 | ×0.1^4 = 0.0 |
|  | 22¢ | 65 | ×0.1^5 = 0.0 |
|  | 17¢ | 3 | ×0.1^10 = 0.0 |
|  | 13¢ | 875 | ×0.1^14 = 0.0 |
|  | 12¢ | 250 | ×0.1^15 = 0.0 |
|  | 11¢ | 250 | ×0.1^16 = 0.0 |
|  | 10¢ | 3 | ×0.1^17 = 0.0 |
|  | 7¢ | 5 | ×0.1^20 = 0.0 |
| | … | +2 levels | 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.7% = $6.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-cryptoleg-2026-08-10`
2. `lawec-cryptoleg-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 10 @ 53¢ → $4.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 53¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 49¢ | 7 | ×0.2^4 = 0.0 |
|  | 48¢ | 152 | ×0.2^5 = 0.0 |
|  | 2¢ | 79,949 | ×0.2^51 = 0.0 |
| | | **Σ** | **10.1** |

`yours 10.0 / Σ 10.1 = 99.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.4% = $4.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 2 @ 19¢ → $3.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 2 (2 yours) | ×0.2^0 = 2.0 |
|  | 16¢ | 5 | ×0.2^3 = 0.0 |
|  | 5¢ | 115 | ×0.2^14 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^18 = 0.0 |
| | | **Σ** | **2.1** |

`yours 2.0 / Σ 2.1 = 97.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 97.6% = $3.75/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 20 @ 48¢ → $3.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 51¢ | 1 | ×0.2^3 = 0.0 |
|  | 60¢ | 5 | ×0.2^12 = 0.0 |
|  | 61¢ | 100 | ×0.2^13 = 0.0 |
|  | 83¢ | 812 | ×0.2^35 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **21.0** |

`yours 20.0 / Σ 21.0 = 95.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 95.2% = $3.97/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 1 @ 25¢ → $3.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 22¢ | 10 | ×0.2^3 = 0.1 |
|  | 16¢ | 380 | ×0.2^9 = 0.0 |
|  | 2¢ | 100,000 | ×0.2^23 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 92.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 92.6% = $3.56/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> BUY 20 @ 9¢ → $3.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 8¢ | 10 | ×0.2^1 = 2.0 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,563 | ×0.2^8 = 0.0 |
| | | **Σ** | **22.1** |

`yours 20.0 / Σ 22.1 = 90.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 90.7% = $3.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 1 @ 13¢ → $3.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 3 | ×0.2^6 = 0.0 |
|  | 6¢ | 10,457 | ×0.2^7 = 0.1 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 86.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 86.7% = $3.33/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 10 @ 46¢ → $3.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 11 (10 yours) | ×0.2^0 = 11.0 |
|  | 50¢ | 462 | ×0.2^4 = 0.7 |
|  | 52¢ | 1 | ×0.2^6 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^52 = 0.0 |
| | | **Σ** | **11.7** |

`yours 10.0 / Σ 11.7 = 85.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 85.2% = $3.55/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 10 @ 30¢ → $10.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 11 (10 yours) | ×0.25^0 = 11.0 |
|  | 34¢ | 250 | ×0.25^4 = 1.0 |
|  | 50¢ | 19 | ×0.25^20 = 0.0 |
|  | 99¢ | 10,701 | ×0.25^69 = 0.0 |
| | | **Σ** | **12.0** |

`yours 10.0 / Σ 12.0 = 83.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 83.5% = $10.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>lawec-cryptoleg-2026-12-31</code> SELL 5 @ 39¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 39¢ | 6 (5 yours) | ×0.1^0 = 6.0 |
|  | 47¢ | 29 | ×0.1^8 = 0.0 |
|  | 52¢ | 5,772 | ×0.1^13 = 0.0 |
| | | **Σ** | **6.0** |

`yours 5.0 / Σ 6.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-cryptoleg-2026-08-10`
2. `lawec-cryptoleg-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 7 @ 22¢ → $3.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 25¢ | 0 | ×0.2^0 = 0.0 |
|  | 24¢ | 0 | ×0.2^1 = 0.0 |
| ▶ | 22¢ | 7 (7 yours) | ×0.2^3 = 0.1 |
|  | 17¢ | 0 | ×0.2^8 = 0.0 |
|  | 8¢ | 100 | ×0.2^17 = 0.0 |
|  | 7¢ | 81 | ×0.2^18 = 0.0 |
|  | 3¢ | 5,000 | ×0.2^22 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 82.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 82.4% = $3.43/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220` ← this one
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 65¢ → $3.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 63¢ | 80 | ×0.2^2 = 3.2 |
|  | 60¢ | 0 | ×0.2^5 = 0.0 |
|  | 57¢ | 0 | ×0.2^8 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^63 = 0.0 |
| | | **Σ** | **13.2** |

`yours 10.0 / Σ 13.2 = 75.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 75.7% = $3.15/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180` ← this one
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 7 @ 59¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 59¢ | 7 (7 yours) | ×0.2^0 = 7.0 |
|  | 60¢ | 10 | ×0.2^1 = 2.0 |
|  | 62¢ | 42 | ×0.2^3 = 0.3 |
|  | 63¢ | 5 | ×0.2^4 = 0.0 |
|  | 65¢ | 50 | ×0.2^6 = 0.0 |
|  | 70¢ | 205 | ×0.2^11 = 0.0 |
|  | 90¢ | 1 | ×0.2^31 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^39 = 0.0 |
| | | **Σ** | **9.3** |

`yours 7.0 / Σ 9.3 = 74.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 74.9% = $3.12/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 100 @ 12¢ → $9.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 136 (100 yours) | ×0.1^0 = 136.0 |
|  | 6¢ | 22 | ×0.1^6 = 0.0 |
|  | 5¢ | 99 | ×0.1^7 = 0.0 |
|  | 3¢ | 100 | ×0.1^9 = 0.0 |
|  | 1¢ | 35,326 | ×0.1^11 = 0.0 |
| | | **Σ** | **136.0** |

`yours 100.0 / Σ 136.0 = 73.5%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 73.5% = $9.19/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 5 @ 26¢ → $2.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 7 (5 yours) | ×0.2^0 = 7.0 |
|  | 50¢ | 100 | ×0.2^24 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^71 = 0.0 |
| | | **Σ** | **7.1** |

`yours 5.0 / Σ 7.1 = 70.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 70.9% = $2.73/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 21 @ 75¢ → $2.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 31 (21 yours) | ×0.2^0 = 31.0 |
|  | 71¢ | 118 | ×0.2^4 = 0.2 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
| | | **Σ** | **31.2** |

`yours 21.0 / Σ 31.2 = 67.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 67.3% = $2.81/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185` ← this one
3. `scc-hrep-rep-2026-11-03-gte190`
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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $2.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 35 (20 yours) | ×0.2^0 = 35.0 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **35.0** |

`yours 20.0 / Σ 35.0 = 57.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 57.1% = $2.20/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 25 @ 13¢ → $6.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 25 (25 yours) | ×0.1^0 = 25.0 |
|  | 14¢ | 202 | ×0.1^1 = 20.2 |
|  | 35¢ | 101 | ×0.1^22 = 0.0 |
|  | 46¢ | 99 | ×0.1^33 = 0.0 |
|  | 99¢ | 1,982 | ×0.1^86 = 0.0 |
| | | **Σ** | **45.2** |

`yours 25.0 / Σ 45.2 = 55.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 55.3% = $6.92/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 20 @ 17¢ → $2.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 24 (20 yours) | ×0.2^0 = 24.0 |
|  | 16¢ | 64 | ×0.2^1 = 12.8 |
|  | 14¢ | 42 | ×0.2^3 = 0.3 |
|  | 2¢ | 50,000 | ×0.2^15 = 0.0 |
| | | **Σ** | **37.1** |

`yours 20.0 / Σ 37.1 = 53.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.9% = $2.07/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 1 @ 73¢ → $1.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 73¢ | 2 (1 yours) | ×0.2^0 = 2.1 |
|  | 98¢ | 60,318 | ×0.2^25 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 47.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 47.8% = $1.99/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180` ← this one
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $1.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 52¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 51¢ | 20 (10 yours) | ×0.2^1 = 4.0 |
|  | 48¢ | 11 | ×0.2^4 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^50 = 0.0 |
| | | **Σ** | **5.0** |

`yours 2.0 / Σ 5.0 = 39.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 39.9% = $1.66/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $1.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 52¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 51¢ | 20 (10 yours) | ×0.2^1 = 4.0 |
|  | 48¢ | 11 | ×0.2^4 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^50 = 0.0 |
| | | **Σ** | **5.0** |

`yours 2.0 / Σ 5.0 = 39.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 39.9% = $1.66/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 75¢ → $1.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 31 (10 yours) | ×0.2^0 = 31.0 |
|  | 71¢ | 118 | ×0.2^4 = 0.2 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
| | | **Σ** | **31.2** |

`yours 10.0 / Σ 31.2 = 32.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 32.1% = $1.34/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185` ← this one
3. `scc-hrep-rep-2026-11-03-gte190`
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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 30 @ 24¢ → $7.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 104 (30 yours) | ×0.2^0 = 104.0 |
|  | 12¢ | 100 | ×0.2^12 = 0.0 |
|  | 2¢ | 100 | ×0.2^22 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^23 = 0.0 |
| | | **Σ** | **104.0** |

`yours 30.0 / Σ 104.0 = 28.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 28.8% = $7.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 5 @ 11¢ → $1.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 16 (5 yours) | ×0.2^0 = 15.5 |
|  | 12¢ | 10 | ×0.2^1 = 2.0 |
|  | 15¢ | 5 | ×0.2^4 = 0.0 |
|  | 50¢ | 100 | ×0.2^39 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^86 = 0.0 |
| | | **Σ** | **17.5** |

`yours 5.0 / Σ 17.5 = 28.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.5% = $1.10/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 30 @ 21¢ → $1.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 45 (30 yours) | ×0.2^0 = 45.0 |
|  | 23¢ | 1,598 | ×0.2^2 = 63.9 |
|  | 47¢ | 99 | ×0.2^26 = 0.0 |
|  | 50¢ | 99 | ×0.2^29 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^76 = 0.0 |
| | | **Σ** | **108.9** |

`yours 30.0 / Σ 108.9 = 27.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.5% = $1.06/day`  

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

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-07 | ~$116.96 | $60.33 | 52% |
| 2026-08-06 | ~$60.78 | $52.21 | 86% |
| 2026-08-05 | ~$33.74 | $31.46 | 93% |

Biggest gaps on 2026-08-07: `opdc-mcconnell-resign-2026-11-02` (est ~$17.07 → got $5.10), `scc-hrep-rep-2026-11-03-gte205` (est ~$4.14 → got $0.00), `scc-hrep-rep-2026-11-03-gte195` (est ~$5.07 → got $0.94)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (110,837 resting) | ~84.7% | ~$21.18 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (325,441 resting) | ~24.1% | ~$18.05 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (221,245 resting) | ~15.8% | ~$11.85 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,395 resting) | ~42.2% | ~$10.55 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (75,894 resting) | ~32.7% | ~$8.17 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (44,516 resting) | ~30.0% | ~$7.49 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (48,717 resting) | ~9.1% | ~$6.85 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (79,950 resting) | ~22.6% | ~$5.65 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (172,317 resting) | ~6.5% | ~$4.86 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (87,529 resting) | ~18.0% | ~$4.49 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (56,176 resting) | ~63.0% | ~$3.94 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (71,784 resting) | ~3.8% | ~$2.83 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,627.01 |
| Pending | $144.00 |
| Skipped | $1.41 |
| **Total earned** | **$1,772.42** |

1749 reward rows · 36 days with rewards · 377 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-07 | $60.33 | `████████` |
| 2026-08-06 | $52.21 | `███████` |
| 2026-08-05 | $31.46 | `████` |
| 2026-08-04 | $53.94 | `███████` |
| 2026-08-03 | $44.81 | `██████` |
| 2026-08-02 | $14.05 | `██` |
| 2026-08-01 | $52.30 | `███████` |
| 2026-07-31 | $67.96 | `█████████` |
| 2026-07-30 | $20.67 | `███` |
| 2026-07-29 | $53.60 | `███████` |
| 2026-07-28 | $79.65 | `██████████` |
| 2026-07-27 | $125.34 | `████████████████` |
| 2026-07-26 | $153.80 | `████████████████████` |
| 2026-07-25 | $125.69 | `████████████████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $309.10 | `████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $77.48 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `opdc-mcconnell-resign-2026-11-02` | $52.92 |
| `apdc-jerpowgov-2026-12-31` | $49.91 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.92 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `scc-hrep-rep-2026-11-03-gte200` | $29.77 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.19 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-08 9:12 PM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-08 9:06 PM ET | ✅ ok | 1704 | $1722.44 |
| 2026-08-08 7:48 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 6:50 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 5:49 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 4:53 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 3:47 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 3:02 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 1:50 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 12:56 PM ET | ✅ ok | 1702 | $1712.09 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
