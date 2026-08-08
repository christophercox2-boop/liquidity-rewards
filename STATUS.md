# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-08 7:48 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$132.20/day estimated (ceiling, not promise — details below)

**Earned:** $1,712.09 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-06: **$52.21** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-05: **$31.46** · 2026-08-04: **$53.94** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-xavbec` — BUY at the best price, ~$35.71/day for 200 contracts. Runners-up: `ewc-usse-oh-2026-11-03-dem` (~$21.18/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$13.02/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$132.20/day (~$5.51/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-49` | BUY | 29.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (50,610 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 12.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (35,655 resting ≥ 2,000 ✓) ≈ $12.50/day |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 43.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (80,554 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `pandc-anydis-2027-12-31` | BUY | 15.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~99.5% of bid side (11,610 resting ≥ 10,000 ✓) ≈ $12.43/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~97.6% of bid side (200,553 resting ≥ 5,000 ✓) ≈ $3.75/day (pool ÷ 13 markets) |
| `pandc-anydis-2027-12-31` | SELL | 30.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~96.3% of ask side (10,829 resting ≥ 10,000 ✓) ≈ $12.03/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~95.2% of ask side (48,664 resting ≥ 5,000 ✓) ≈ $3.97/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 25.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~92.6% of bid side (100,616 resting ≥ 5,000 ✓) ≈ $3.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 9.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~90.7% of bid side (5,594 resting ≥ 5,000 ✓) ≈ $3.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 46.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~84.3% of ask side (48,210 resting ≥ 5,000 ✓) ≈ $3.51/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 52.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~84.0% of ask side (16,276 resting ≥ 5,000 ✓) ≈ $3.50/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 22.0¢ | 7 | 3 | $100.00 | ✅ scoring — ~82.4% of bid side (85,488 resting ≥ 5,000 ✓) ≈ $3.43/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~75.3% of bid side (80,592 resting ≥ 5,000 ✓) ≈ $3.14/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 26.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~70.9% of ask side (113,510 resting ≥ 5,000 ✓) ≈ $2.73/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 27 | 3 | $100.00 | ✅ scoring — ~70.8% of ask side (113,539 resting ≥ 5,000 ✓) ≈ $2.72/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (50,465 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 59.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~66.4% of ask side (48,074 resting ≥ 5,000 ✓) ≈ $2.77/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 17.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~60.4% of bid side (50,433 resting ≥ 5,000 ✓) ≈ $2.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~57.1% of ask side (117,800 resting ≥ 5,000 ✓) ≈ $2.20/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 16.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~52.4% of bid side (5,494 resting ≥ 5,000 ✓) ≈ $13.09/day (pool ÷ 2 markets) |
| `lawec-cryptoleg-2026-12-31` | SELL | 43.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~47.7% of ask side (31,248 resting ≥ 2,000 ✓) ≈ $2.98/day (pool ÷ 2 markets) |
| `lawec-cryptoleg-2026-12-31` | BUY | 24.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~35.3% of bid side (26,959 resting ≥ 2,000 ✓) ≈ $2.21/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 11.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~28.5% of ask side (113,532 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 21.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~27.5% of ask side (100,249 resting ≥ 5,000 ✓) ≈ $1.06/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 13.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~27.2% of ask side (2,426 resting ≥ 2,000 ✓) ≈ $3.40/day |
| `scc-senate-gop-2026-11-03-50` | SELL | 28.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~25.0% of ask side (113,521 resting ≥ 5,000 ✓) ≈ $0.96/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 28.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~25.0% of ask side (113,521 resting ≥ 5,000 ✓) ≈ $0.96/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 29.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~25.0% of ask side (113,521 resting ≥ 5,000 ✓) ≈ $0.96/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~24.9% of bid side (3,924 resting ≥ 2,500 ✓) ≈ $0.85/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~24.3% of bid side (80,592 resting ≥ 5,000 ✓) ≈ $1.01/day (pool ÷ 12 markets) |
| …and 40 more | | | | | | |

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 100 @ 12¢ → $12.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 100 (100 yours) | ×0.1^0 = 100.0 |
|  | 6¢ | 30 | ×0.1^6 = 0.0 |
|  | 5¢ | 99 | ×0.1^7 = 0.0 |
|  | 3¢ | 100 | ×0.1^9 = 0.0 |
|  | 1¢ | 35,326 | ×0.1^11 = 0.0 |
| | | **Σ** | **100.0** |

`yours 100.0 / Σ 100.0 = 100.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 100.0% = $12.50/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> BUY 10 @ 15¢ → $12.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 10¢ | 10 | ×0.25^5 = 0.0 |
|  | 8¢ | 726 | ×0.25^7 = 0.0 |
|  | 2¢ | 4 | ×0.25^13 = 0.0 |
|  | 1¢ | 10,860 | ×0.25^14 = 0.0 |
| | | **Σ** | **10.1** |

`yours 10.0 / Σ 10.1 = 99.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 99.5% = $12.43/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

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
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 10 @ 30¢ → $12.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 34¢ | 99 | ×0.25^4 = 0.4 |
|  | 50¢ | 19 | ×0.25^20 = 0.0 |
|  | 99¢ | 10,701 | ×0.25^69 = 0.0 |
| | | **Σ** | **10.4** |

`yours 10.0 / Σ 10.4 = 96.3%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 96.3% = $12.03/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 10 @ 46¢ → $3.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 11 (10 yours) | ×0.2^0 = 11.0 |
|  | 48¢ | 1 | ×0.2^2 = 0.0 |
|  | 49¢ | 10 | ×0.2^3 = 0.1 |
|  | 50¢ | 462 | ×0.2^4 = 0.7 |
|  | 52¢ | 1 | ×0.2^6 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^52 = 0.0 |
| | | **Σ** | **11.9** |

`yours 10.0 / Σ 11.9 = 84.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 84.3% = $3.51/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 5 @ 52¢ → $3.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 52¢ | 6 (5 yours) | ×0.2^0 = 6.2 |
|  | 60¢ | 30 | ×0.2^8 = 0.0 |
|  | 82¢ | 175 | ×0.2^30 = 0.0 |
|  | 99¢ | 16,065 | ×0.2^47 = 0.0 |
| | | **Σ** | **6.3** |

`yours 5.2 / Σ 6.3 = 84.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 84.0% = $3.50/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 75¢ → $3.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 41 (31 yours) | ×0.2^0 = 41.0 |
|  | 71¢ | 101 | ×0.2^4 = 0.2 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
| | | **Σ** | **41.2** |

`yours 31.0 / Σ 41.2 = 75.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 75.3% = $3.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 27 @ 22¢ → $2.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 22¢ | 37 (27 yours) | ×0.2^3 = 0.3 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 81¢ | 0 | ×0.2^62 = 0.0 |
|  | 83¢ | 0 | ×0.2^64 = 0.0 |
|  | 84¢ | 0 | ×0.2^65 = 0.0 |
|  | 85¢ | 0 | ×0.2^66 = 0.0 |
|  | 86¢ | 0 | ×0.2^67 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^78 = 0.0 |
| | | **Σ** | **0.3** |

`yours 0.2 / Σ 0.3 = 70.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 70.8% = $2.72/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 82¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 72¢ | 0 | ×0.2^10 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^80 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 7 @ 59¢ → $2.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 59¢ | 7 (7 yours) | ×0.2^0 = 7.0 |
|  | 60¢ | 10 | ×0.2^1 = 2.0 |
|  | 61¢ | 30 | ×0.2^2 = 1.2 |
|  | 62¢ | 42 | ×0.2^3 = 0.3 |
|  | 63¢ | 5 | ×0.2^4 = 0.0 |
|  | 65¢ | 50 | ×0.2^6 = 0.0 |
|  | 70¢ | 205 | ×0.2^11 = 0.0 |
|  | 90¢ | 1 | ×0.2^31 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^39 = 0.0 |
| | | **Σ** | **10.5** |

`yours 7.0 / Σ 10.5 = 66.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.4% = $2.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 20 @ 17¢ → $2.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 16¢ | 64 | ×0.2^1 = 12.8 |
|  | 14¢ | 42 | ×0.2^3 = 0.3 |
|  | 2¢ | 50,000 | ×0.2^15 = 0.0 |
| | | **Σ** | **33.1** |

`yours 20.0 / Σ 33.1 = 60.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 60.4% = $2.32/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 21 @ 16¢ → $13.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 25 (21 yours) | ×0.2^0 = 24.9 |
|  | 14¢ | 100 | ×0.2^2 = 4.0 |
|  | 13¢ | 1,372 | ×0.2^3 = 11.0 |
|  | 1¢ | 3,998 | ×0.2^15 = 0.0 |
| | | **Σ** | **39.8** |

`yours 20.9 / Σ 39.8 = 52.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 52.4% = $13.09/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>lawec-cryptoleg-2026-12-31</code> SELL 10 @ 43¢ → $2.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 14 (10 yours) | ×0.1^0 = 14.0 |
|  | 44¢ | 69 | ×0.1^1 = 6.9 |
|  | 47¢ | 29 | ×0.1^4 = 0.0 |
|  | 52¢ | 5,823 | ×0.1^9 = 0.0 |
| | | **Σ** | **20.9** |

`yours 10.0 / Σ 20.9 = 47.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 47.7% = $2.98/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-cryptoleg-2026-08-10`
2. `lawec-cryptoleg-2026-12-31` ← this one

</details>

</details>
<details><summary><code>lawec-cryptoleg-2026-12-31</code> BUY 10 @ 24¢ → $2.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 23 (10 yours) | ×0.1^0 = 23.1 |
|  | 23¢ | 46 | ×0.1^1 = 4.5 |
|  | 22¢ | 64 | ×0.1^2 = 0.6 |
|  | 17¢ | 3 | ×0.1^7 = 0.0 |
|  | 13¢ | 875 | ×0.1^11 = 0.0 |
|  | 12¢ | 250 | ×0.1^12 = 0.0 |
|  | 11¢ | 250 | ×0.1^13 = 0.0 |
|  | 10¢ | 3 | ×0.1^14 = 0.0 |
|  | 7¢ | 5 | ×0.1^17 = 0.0 |
|  | 5¢ | 241 | ×0.1^19 = 0.0 |
| | … | +1 levels | 0.0 |
| | | **Σ** | **28.3** |

`yours 10.0 / Σ 28.3 = 35.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 35.3% = $2.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-cryptoleg-2026-08-10`
2. `lawec-cryptoleg-2026-12-31` ← this one

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 25 @ 13¢ → $3.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 75 (25 yours) | ×0.1^0 = 75.0 |
|  | 14¢ | 170 | ×0.1^1 = 17.0 |
|  | 35¢ | 101 | ×0.1^22 = 0.0 |
|  | 46¢ | 99 | ×0.1^33 = 0.0 |
|  | 99¢ | 1,982 | ×0.1^86 = 0.0 |
| | | **Σ** | **92.0** |

`yours 25.0 / Σ 92.0 = 27.2%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 27.2% = $3.40/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 2 @ 28¢ → $0.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 6 (2 yours) | ×0.2^0 = 6.0 |
|  | 29¢ | 10 | ×0.2^1 = 2.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^69 = 0.0 |
| | | **Σ** | **8.0** |

`yours 2.0 / Σ 8.0 = 25.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.0% = $0.96/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 2 @ 28¢ → $0.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 6 (2 yours) | ×0.2^0 = 6.0 |
|  | 29¢ | 10 | ×0.2^1 = 2.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^69 = 0.0 |
| | | **Σ** | **8.0** |

`yours 2.0 / Σ 8.0 = 25.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.0% = $0.96/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 10 @ 29¢ → $0.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 28¢ | 6 | ×0.2^0 = 6.0 |
| ▶ | 29¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^69 = 0.0 |
| | | **Σ** | **8.0** |

`yours 2.0 / Σ 8.0 = 25.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.0% = $0.96/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 50 | ×0.35^0 = 50.0 |
| ▶ | 1¢ | 3,874 (1,000 yours) | ×0.35^1 = 1,355.9 |
| | | **Σ** | **1,405.9** |

`yours 350.0 / Σ 1,405.9 = 24.9%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 24.9% = $0.85/day`  

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
40. `tec-cbb-champ-2027-04-05-w-nebr` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 75¢ → $1.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 41 (10 yours) | ×0.2^0 = 41.0 |
|  | 71¢ | 101 | ×0.2^4 = 0.2 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
| | | **Σ** | **41.2** |

`yours 10.0 / Σ 41.2 = 24.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 24.3% = $1.01/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-05 | ~$33.74 | $31.46 | 93% |
| 2026-08-04 | ~$67.52 | $53.94 | 80% |
| 2026-08-03 | ~$65.16 | $44.81 | 69% |

Biggest gaps on 2026-08-05: `opdc-mcconnell-resign-2026-11-02` (est ~$1.91 → got $0.30), `scc-senate-gop-2026-11-03-51` (est ~$2.87 → got $2.08), `ewc-usgub-ca-2026-11-03-stehil` (est ~$0.75 → got $0.00)

_2026-08-06 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (325,100 resting) | ~47.6% | ~$35.71 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (110,837 resting) | ~84.7% | ~$21.18 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (43,233 resting) | ~52.1% | ~$13.02 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (154,113 resting) | ~17.0% | ~$12.77 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,400 resting) | ~41.8% | ~$10.44 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,427 resting) | ~38.5% | ~$9.61 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (48,717 resting) | ~9.1% | ~$6.85 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (179,915 resting) | ~8.6% | ~$6.45 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (81,500 resting) | ~18.8% | ~$4.70 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (172,695 resting) | ~5.8% | ~$4.33 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (73,393 resting) | ~3.1% | ~$2.32 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $100.00 ÷ 3 | 0.20 | 5,000 | BUY side (237,247 resting) | ~12.5% | ~$2.08 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,627.01 |
| Pending | $83.67 |
| Skipped | $1.41 |
| **Total earned** | **$1,712.09** |

1702 reward rows · 35 days with rewards · 363 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-06 ⚠️ multi-day pending bucket | $52.21 | `███████` |
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
| 2026-07-24 | $135.19 | `██████████████████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $248.77 | `███` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $74.36 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `opdc-mcconnell-resign-2026-11-02` | $47.82 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `apdc-jerpowgov-2026-12-31` | $42.68 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.92 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.02 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `scc-hrep-rep-2026-11-03-gte200` | $25.65 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-08 7:48 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 6:50 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 5:49 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 4:53 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 3:47 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 3:02 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 1:50 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 12:56 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 11:49 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 10:52 AM ET | ✅ ok | 1702 | $1712.09 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
