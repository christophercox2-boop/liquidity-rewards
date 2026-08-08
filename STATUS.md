# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-08 4:53 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$140.30/day estimated (ceiling, not promise — details below)

**Earned:** $1,712.09 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-06: **$52.21** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-05: **$31.46** · 2026-08-04: **$53.94** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — SELL at the best price, ~$41.11/day for 200 contracts. Runners-up: `ewc-usse-oh-2026-11-03-dem` (~$20.59/day), `ewc-usgub-ca-2026-11-03-xavbec` (~$14.73/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$140.30/day (~$5.85/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `opdc-mcconnell-resign-2026-11-02` | BUY | 12.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (35,655 resting ≥ 2,000 ✓) ≈ $12.50/day |
| `scc-senate-gop-2026-11-03-49` | BUY | 27.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (50,592 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 12.0¢ | 39 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (80,595 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `pvwc-housepopw-2026-11-03-dem` | SELL | 73.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~99.3% of ask side (4,248 resting ≥ 2,000 ✓) ≈ $6.20/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 49.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~99.3% of bid side (80,742 resting ≥ 5,000 ✓) ≈ $4.14/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 25.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~98.9% of bid side (100,606 resting ≥ 5,000 ✓) ≈ $3.81/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 43.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~98.5% of bid side (80,569 resting ≥ 5,000 ✓) ≈ $4.11/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~95.2% of ask side (48,663 resting ≥ 5,000 ✓) ≈ $3.97/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 9.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~95.2% of bid side (5,584 resting ≥ 5,000 ✓) ≈ $3.97/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 60.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~85.2% of ask side (63,032 resting ≥ 5,000 ✓) ≈ $3.55/day (pool ÷ 12 markets) |
| `pandc-anydis-2027-12-31` | SELL | 30.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~83.5% of ask side (11,152 resting ≥ 10,000 ✓) ≈ $10.44/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~79.2% of bid side (50,423 resting ≥ 5,000 ✓) ≈ $3.05/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~74.1% of bid side (80,592 resting ≥ 5,000 ✓) ≈ $3.09/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 29.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~71.4% of ask side (113,453 resting ≥ 5,000 ✓) ≈ $2.75/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~70.9% of bid side (200,559 resting ≥ 5,000 ✓) ≈ $2.73/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 27 | 0 | $100.00 | ✅ scoring — ~67.7% of ask side (113,542 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 35.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (62,557 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~57.1% of ask side (117,800 resting ≥ 5,000 ✓) ≈ $2.20/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 33.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~55.5% of bid side (200,468 resting ≥ 5,000 ✓) ≈ $2.31/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 57.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~55.5% of bid side (80,501 resting ≥ 5,000 ✓) ≈ $2.31/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | BUY | 16.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~52.4% of bid side (5,494 resting ≥ 5,000 ✓) ≈ $13.09/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 63.0¢ | 51 | 0 | $100.00 | ✅ scoring — ~52.3% of ask side (11,861 resting ≥ 5,000 ✓) ≈ $2.18/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 46.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~50.8% of ask side (48,220 resting ≥ 5,000 ✓) ≈ $2.12/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~33.3% of bid side (50,480 resting ≥ 5,000 ✓) ≈ $1.39/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~33.3% of bid side (50,480 resting ≥ 5,000 ✓) ≈ $1.39/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 13.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~33.0% of ask side (2,356 resting ≥ 2,000 ✓) ≈ $4.13/day |
| `scc-senate-gop-2026-11-03-51` | SELL | 26.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~32.1% of ask side (113,528 resting ≥ 5,000 ✓) ≈ $1.23/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 11.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~28.5% of ask side (113,532 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~28.4% of bid side (200,559 resting ≥ 5,000 ✓) ≈ $1.09/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 28.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~25.0% of ask side (113,521 resting ≥ 5,000 ✓) ≈ $0.96/day (pool ÷ 13 markets) |
| …and 57 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 100 @ 12¢ → $12.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 100 (100 yours) | ×0.1^0 = 100.0 |
|  | 10¢ | 0 | ×0.1^2 = 0.0 |
|  | 6¢ | 30 | ×0.1^6 = 0.0 |
|  | 5¢ | 99 | ×0.1^7 = 0.0 |
|  | 3¢ | 100 | ×0.1^9 = 0.0 |
|  | 1¢ | 35,326 | ×0.1^11 = 0.0 |
| | | **Σ** | **100.0** |

`yours 100.0 / Σ 100.0 = 100.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 100.0% = $12.50/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 17 @ 27¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 17 (17 yours) | ×0.2^0 = 17.0 |
|  | 20¢ | 10 | ×0.2^7 = 0.0 |
|  | 19¢ | 0 | ×0.2^8 = 0.0 |
|  | 17¢ | 156 | ×0.2^10 = 0.0 |
|  | 2¢ | 50,209 | ×0.2^25 = 0.0 |
| | | **Σ** | **17.0** |

`yours 17.0 / Σ 17.0 = 100.0%`  
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 39 @ 12¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 39 (39 yours) | ×0.2^0 = 38.9 |
|  | 1¢ | 80,557 | ×0.2^11 = 0.0 |
| | | **Σ** | **38.9** |

`yours 38.9 / Σ 38.9 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
10. `scc-hrep-rep-2026-11-03-gte225` ← this one
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>pvwc-housepopw-2026-11-03-dem</code> SELL 11 @ 73¢ → $6.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 73¢ | 11 (11 yours) | ×0.1^0 = 11.0 |
|  | 75¢ | 3 | ×0.1^2 = 0.0 |
|  | 76¢ | 52 | ×0.1^3 = 0.1 |
|  | 83¢ | 30 | ×0.1^10 = 0.0 |
|  | 88¢ | 1,370 | ×0.1^15 = 0.0 |
|  | 89¢ | 124 | ×0.1^16 = 0.0 |
|  | 92¢ | 129 | ×0.1^19 = 0.0 |
|  | 99¢ | 2,530 | ×0.1^26 = 0.0 |
| | | **Σ** | **11.1** |

`yours 11.0 / Σ 11.1 = 99.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.3% = $6.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem` ← this one
2. `pvwc-housepopw-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 20 @ 49¢ → $4.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 20 (20 yours) | ×0.2^0 = 20.1 |
|  | 47¢ | 1 | ×0.2^2 = 0.0 |
|  | 36¢ | 100 | ×0.2^13 = 0.0 |
|  | 35¢ | 80 | ×0.2^14 = 0.0 |
|  | 11¢ | 151 | ×0.2^38 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^47 = 0.0 |
| | | **Σ** | **20.2** |

`yours 20.0 / Σ 20.2 = 99.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.3% = $4.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 1 @ 25¢ → $3.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 23¢ | 0 | ×0.2^2 = 0.0 |
|  | 22¢ | 0 | ×0.2^3 = 0.0 |
|  | 16¢ | 380 | ×0.2^9 = 0.0 |
|  | 2¢ | 100,000 | ×0.2^23 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.9% = $3.81/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 1 @ 43¢ → $4.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 38¢ | 15 | ×0.2^5 = 0.0 |
|  | 35¢ | 3 | ×0.2^8 = 0.0 |
|  | 19¢ | 100 | ×0.2^24 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^41 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 98.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 98.5% = $4.11/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 20 @ 48¢ → $3.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 59¢ | 5 | ×0.2^11 = 0.0 |
|  | 60¢ | 100 | ×0.2^12 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> BUY 20 @ 9¢ → $3.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 1¢ | 5,563 | ×0.2^8 = 0.0 |
| | | **Σ** | **21.0** |

`yours 20.0 / Σ 21.0 = 95.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 95.2% = $3.97/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 10 @ 60¢ → $3.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 62¢ | 42 | ×0.2^2 = 1.7 |
|  | 63¢ | 5 | ×0.2^3 = 0.0 |
|  | 65¢ | 50 | ×0.2^5 = 0.0 |
|  | 71¢ | 200 | ×0.2^11 = 0.0 |
|  | 90¢ | 1 | ×0.2^30 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^38 = 0.0 |
| | | **Σ** | **11.7** |

`yours 10.0 / Σ 11.7 = 85.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 85.2% = $3.55/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 10 @ 30¢ → $10.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 11 (10 yours) | ×0.25^0 = 11.0 |
|  | 34¢ | 250 | ×0.25^4 = 1.0 |
|  | 50¢ | 19 | ×0.25^20 = 0.0 |
|  | 99¢ | 10,872 | ×0.25^69 = 0.0 |
| | | **Σ** | **12.0** |

`yours 10.0 / Σ 12.0 = 83.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 83.5% = $10.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 18¢ → $3.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **12.6** |

`yours 10.0 / Σ 12.6 = 79.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 79.2% = $3.05/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 75¢ → $3.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 41 (31 yours) | ×0.2^0 = 41.0 |
|  | 72¢ | 101 | ×0.2^3 = 0.8 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
| | | **Σ** | **41.8** |

`yours 31.0 / Σ 41.8 = 74.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 74.1% = $3.09/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 29¢ → $2.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 7 (5 yours) | ×0.2^0 = 7.0 |
|  | 34¢ | 0 | ×0.2^5 = 0.0 |
|  | 50¢ | 13 | ×0.2^21 = 0.0 |
|  | 63¢ | 0 | ×0.2^34 = 0.0 |
|  | 76¢ | 0 | ×0.2^47 = 0.0 |
|  | 96¢ | 25 | ×0.2^67 = 0.0 |
|  | 97¢ | 58,828 | ×0.2^68 = 0.0 |
| | | **Σ** | **7.0** |

`yours 5.0 / Σ 7.0 = 71.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 71.4% = $2.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5 @ 19¢ → $2.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 7 (5 yours) | ×0.2^0 = 7.0 |
|  | 16¢ | 6 | ×0.2^3 = 0.0 |
|  | 5¢ | 115 | ×0.2^14 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^18 = 0.0 |
| | | **Σ** | **7.0** |

`yours 5.0 / Σ 7.0 = 70.9%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 27 @ 22¢ → $2.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 40 (27 yours) | ×0.2^0 = 40.3 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 81¢ | 0 | ×0.2^59 = 0.0 |
|  | 83¢ | 0 | ×0.2^61 = 0.0 |
|  | 88¢ | 0 | ×0.2^66 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^75 = 0.0 |
| | | **Σ** | **40.3** |

`yours 27.3 / Σ 40.3 = 67.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.7% = $2.60/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 35¢ → $2.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 59¢ | 0 | ×0.2^24 = 0.0 |
|  | 64¢ | 0 | ×0.2^29 = 0.0 |
|  | 98¢ | 60,317 | ×0.2^63 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 10 @ 33¢ → $2.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 18 (10 yours) | ×0.2^0 = 18.0 |
|  | 1¢ | 200,450 | ×0.2^32 = 0.0 |
| | | **Σ** | **18.0** |

`yours 10.0 / Σ 18.0 = 55.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 55.5% = $2.31/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 57¢ → $2.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 18 (10 yours) | ×0.2^0 = 18.0 |
|  | 54¢ | 2 | ×0.2^3 = 0.0 |
|  | 51¢ | 20 | ×0.2^6 = 0.0 |
|  | 48¢ | 11 | ×0.2^9 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^55 = 0.0 |
| | | **Σ** | **18.0** |

`yours 10.0 / Σ 18.0 = 55.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 55.5% = $2.31/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 51 @ 63¢ → $2.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 63¢ | 97 (51 yours) | ×0.2^0 = 97.5 |
|  | 90¢ | 1 | ×0.2^27 = 0.0 |
|  | 95¢ | 100 | ×0.2^32 = 0.0 |
|  | 99¢ | 11,663 | ×0.2^36 = 0.0 |
| | | **Σ** | **97.5** |

`yours 51.0 / Σ 97.5 = 52.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 52.3% = $2.18/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 10 @ 46¢ → $2.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 12 (10 yours) | ×0.2^0 = 12.0 |
|  | 47¢ | 20 | ×0.2^1 = 4.0 |
|  | 49¢ | 462 | ×0.2^3 = 3.7 |
|  | 52¢ | 1 | ×0.2^6 = 0.0 |
|  | 55¢ | 0 | ×0.2^9 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^52 = 0.0 |
| | | **Σ** | **19.7** |

`yours 10.0 / Σ 19.7 = 50.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 50.8% = $2.12/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 82¢ → $1.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 30 (10 yours) | ×0.2^0 = 30.0 |
|  | 72¢ | 0 | ×0.2^10 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^80 = 0.0 |
| | | **Σ** | **30.0** |

`yours 10.0 / Σ 30.0 = 33.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 33.3% = $1.39/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 82¢ → $1.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 30 (10 yours) | ×0.2^0 = 30.0 |
|  | 72¢ | 0 | ×0.2^10 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^80 = 0.0 |
| | | **Σ** | **30.0** |

`yours 10.0 / Σ 30.0 = 33.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 33.3% = $1.39/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 25 @ 13¢ → $4.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 75 (25 yours) | ×0.1^0 = 75.0 |
|  | 15¢ | 70 | ×0.1^2 = 0.7 |
|  | 18¢ | 30 | ×0.1^5 = 0.0 |
|  | 35¢ | 101 | ×0.1^22 = 0.0 |
|  | 46¢ | 99 | ×0.1^33 = 0.0 |
|  | 88¢ | 0 | ×0.1^75 = 0.0 |
|  | 99¢ | 1,982 | ×0.1^86 = 0.0 |
| | | **Σ** | **75.7** |

`yours 25.0 / Σ 75.7 = 33.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 33.0% = $4.13/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 5 @ 26¢ → $1.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 16 (5 yours) | ×0.2^0 = 15.6 |
|  | 31¢ | 10 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^24 = 0.0 |
|  | 59¢ | 0 | ×0.2^33 = 0.0 |
|  | 67¢ | 0 | ×0.2^41 = 0.0 |
|  | 68¢ | 0 | ×0.2^42 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^71 = 0.0 |
| | | **Σ** | **15.6** |

`yours 5.0 / Σ 15.6 = 32.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.1% = $1.23/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 2 @ 19¢ → $1.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 7 (2 yours) | ×0.2^0 = 7.0 |
|  | 16¢ | 6 | ×0.2^3 = 0.0 |
|  | 5¢ | 115 | ×0.2^14 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^18 = 0.0 |
| | | **Σ** | **7.0** |

`yours 2.0 / Σ 7.0 = 28.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.4% = $1.09/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 2 @ 28¢ → $0.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 6 (2 yours) | ×0.2^0 = 6.0 |
|  | 29¢ | 10 | ×0.2^1 = 2.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 73¢ | 0 | ×0.2^45 = 0.0 |
|  | 74¢ | 0 | ×0.2^46 = 0.0 |
|  | 75¢ | 0 | ×0.2^47 = 0.0 |
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
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (219,993 resting) | ~54.8% | ~$41.11 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (103,846 resting) | ~82.4% | ~$20.59 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (325,597 resting) | ~19.6% | ~$14.73 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (78,027 resting) | ~41.8% | ~$10.44 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (193,463 resting) | ~13.2% | ~$9.91 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (32,451 resting) | ~33.7% | ~$8.41 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,814 resting) | ~30.2% | ~$7.56 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (64,047 resting) | ~8.3% | ~$6.20 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (63,807 resting) | ~21.4% | ~$5.36 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (172,701 resting) | ~5.8% | ~$4.32 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (72,894 resting) | ~3.4% | ~$2.51 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $100.00 ÷ 3 | 0.20 | 5,000 | BUY side (237,289 resting) | ~12.4% | ~$2.06 |

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
| 2026-08-08 4:53 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 3:47 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 3:02 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 1:50 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 12:56 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 11:49 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 10:52 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 10:01 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 9:15 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-08 7:47 AM ET | ✅ ok | 1702 | $1712.09 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
