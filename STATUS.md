# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-03 9:07 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$38.88/day estimated (ceiling, not promise — details below)

**Earned:** $1,515.42 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-01: **$52.30** · 2026-07-31: **$67.96** · 2026-07-30: **$20.48** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — SELL at the best price, ~$16.50/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$16.22/day), `ewc-usgub-oh-2026-11-03-dem` (~$9.25/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$38.88/day (~$1.62/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-47` | BUY | 14.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~99.3% of bid side (5,470 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~98.8% of ask side (12,054 resting ≥ 5,000 ✓) ≈ $3.80/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 24.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~91.8% of bid side (5,558 resting ≥ 5,000 ✓) ≈ $3.53/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 67.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~89.1% of ask side (12,425 resting ≥ 5,000 ✓) ≈ $3.71/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 30.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~88.8% of bid side (5,557 resting ≥ 5,000 ✓) ≈ $3.41/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 9.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~34.9% of ask side (12,274 resting ≥ 5,000 ✓) ≈ $1.34/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~29.6% of ask side (12,456 resting ≥ 5,000 ✓) ≈ $1.14/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 7.0¢ | 3 | 1 | $100.00 | ✅ scoring — ~29.2% of bid side (25,570 resting ≥ 5,000 ✓) ≈ $1.12/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 41 | 0 | $100.00 | ✅ scoring — ~26.7% of ask side (12,239 resting ≥ 5,000 ✓) ≈ $1.03/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~26.6% of ask side (12,306 resting ≥ 5,000 ✓) ≈ $1.02/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 27.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~26.4% of ask side (12,243 resting ≥ 5,000 ✓) ≈ $1.02/day (pool ÷ 13 markets) |
| `pintc-meet-trump-2026-12-31-kimjon` | BUY | 23.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~24.8% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $0.24/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 17.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~18.8% of bid side (12,374 resting ≥ 5,000 ✓) ≈ $4.69/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~13.5% of bid side (5,534 resting ≥ 5,000 ✓) ≈ $0.56/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 58.0¢ | 12 | 0 | $100.00 | ✅ scoring — ~12.8% of ask side (9,876 resting ≥ 5,000 ✓) ≈ $0.54/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 31.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~12.5% of bid side (5,528 resting ≥ 5,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 70.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~11.9% of bid side (5,536 resting ≥ 5,000 ✓) ≈ $0.50/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-ind` | SELL | 2.0¢ | 32 | 0 | $500.00 | ✅ scoring — ~9.3% of ask side (153,789 resting ≥ 2,500 ✓) ≈ $0.32/day (pool ÷ 73 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~7.8% of bid side (10,968 resting ≥ 2,500 ✓) ≈ $0.27/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~7.0% of ask side (9,132 resting ≥ 5,000 ✓) ≈ $0.29/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 18.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~6.9% of ask side (11,938 resting ≥ 2,000 ✓) ≈ $0.86/day |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 1 | $100.00 | ✅ scoring — ~6.0% of bid side (51,844 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 15.0¢ | 20 | 1 | $25.00 | ✅ scoring — ~5.0% of bid side (13,137 resting ≥ 2,000 ✓) ≈ $0.62/day |
| `scc-senate-gop-2026-11-03-52` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~4.7% of bid side (105,728 resting ≥ 5,000 ✓) ≈ $0.18/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 7 | $100.00 | ✅ scoring — ~3.2% of bid side (25,570 resting ≥ 5,000 ✓) ≈ $0.12/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~2.9% of bid side (174,136 resting ≥ 5,000 ✓) ≈ $0.11/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 3.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~2.9% of bid side (35,212 resting ≥ 5,000 ✓) ≈ $0.11/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | SELL | 84.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~2.7% of ask side (5,899 resting ≥ 5,000 ✓) ≈ $0.11/day (pool ÷ 12 markets) |
| `ewc-usse-oh-2026-11-03-rep` | BUY | 48.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~2.7% of bid side (82,542 resting ≥ 5,000 ✓) ≈ $0.68/day (pool ÷ 2 markets) |
| `ewc-usse-tx-2026-11-03-dem` | BUY | 47.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~2.6% of bid side (379,964 resting ≥ 10,000 ✓) ≈ $1.96/day (pool ÷ 2 markets) |
| …and 49 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 15 @ 14¢ → $3.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 12¢ | 3 | ×0.2^2 = 0.1 |
|  | 6¢ | 32 | ×0.2^8 = 0.0 |
|  | 1¢ | 5,420 | ×0.2^13 = 0.0 |
| | | **Σ** | **15.1** |

`yours 15.0 / Σ 15.1 = 99.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.3% = $3.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 3 @ 15¢ → $3.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 3 (3 yours) | ×0.2^0 = 3.3 |
|  | 18¢ | 5 | ×0.2^3 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,745 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **3.3** |

`yours 3.3 / Σ 3.3 = 98.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.8% = $3.80/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 24¢ → $3.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 2 | ×0.2^3 = 0.0 |
|  | 20¢ | 46 | ×0.2^4 = 0.1 |
|  | 1¢ | 5,509 | ×0.2^23 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 91.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 91.8% = $3.53/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 67¢ → $3.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 56 (50 yours) | ×0.2^0 = 56.0 |
|  | 69¢ | 3 | ×0.2^2 = 0.1 |
|  | 77¢ | 1 | ×0.2^10 = 0.0 |
|  | 83¢ | 164 | ×0.2^16 = 0.0 |
|  | 90¢ | 1 | ×0.2^23 = 0.0 |
|  | 99¢ | 12,200 | ×0.2^32 = 0.0 |
| | | **Σ** | **56.1** |

`yours 50.0 / Σ 56.1 = 89.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 89.1% = $3.71/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 5 @ 30¢ → $3.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 28¢ | 3 | ×0.2^2 = 0.1 |
|  | 27¢ | 64 | ×0.2^3 = 0.5 |
|  | 20¢ | 30 | ×0.2^10 = 0.0 |
|  | 14¢ | 72 | ×0.2^16 = 0.0 |
|  | 1¢ | 5,383 | ×0.2^29 = 0.0 |
| | | **Σ** | **5.6** |

`yours 5.0 / Σ 5.6 = 88.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.8% = $3.41/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 10 @ 9¢ → $1.34/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 17 (10 yours) | ×0.2^0 = 17.0 |
|  | 11¢ | 125 | ×0.2^2 = 5.0 |
|  | 12¢ | 831 | ×0.2^3 = 6.6 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **28.7** |

`yours 10.0 / Σ 28.7 = 34.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.9% = $1.34/day`  

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
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $1.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 127 (40 yours) | ×0.2^0 = 127.2 |
|  | 11¢ | 39 | ×0.2^1 = 7.8 |
|  | 12¢ | 0 | ×0.2^2 = 0.0 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **135.0** |

`yours 40.0 / Σ 135.0 = 29.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.6% = $1.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 3 @ 7¢ → $1.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 1 | ×0.2^0 = 1.1 |
| ▶ | 7¢ | 3 (3 yours) | ×0.2^1 = 0.6 |
|  | 2¢ | 232 | ×0.2^6 = 0.0 |
|  | 1¢ | 25,334 | ×0.2^7 = 0.3 |
| | | **Σ** | **2.0** |

`yours 0.6 / Σ 2.0 = 29.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.2% = $1.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 41 @ 22¢ → $1.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 154 (41 yours) | ×0.2^0 = 154.2 |
|  | 24¢ | 0 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 98¢ | 1,784 | ×0.2^76 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^77 = 0.0 |
| | | **Σ** | **154.2** |

`yours 41.2 / Σ 154.2 = 26.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.7% = $1.03/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 129 (40 yours) | ×0.2^0 = 129.0 |
|  | 7¢ | 107 | ×0.2^1 = 21.4 |
|  | 8¢ | 0 | ×0.2^2 = 0.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **150.4** |

`yours 40.0 / Σ 150.4 = 26.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.6% = $1.02/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 27¢ → $1.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 19 (5 yours) | ×0.2^0 = 18.9 |
|  | 29¢ | 0 | ×0.2^2 = 0.0 |
|  | 43¢ | 100 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^23 = 0.0 |
|  | 98¢ | 1,823 | ×0.2^71 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^72 = 0.0 |
| | | **Σ** | **18.9** |

`yours 5.0 / Σ 18.9 = 26.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.4% = $1.02/day`  

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
<details><summary><code>pintc-meet-trump-2026-12-31-kimjon</code> BUY 2 @ 23¢ → $0.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 23¢ | 8 (2 yours) | ×0.1^0 = 8.0 |
|  | 21¢ | 6 | ×0.1^2 = 0.1 |
|  | 20¢ | 2 | ×0.1^3 = 0.0 |
|  | 5¢ | 100 | ×0.1^18 = 0.0 |
|  | 1¢ | 2,384 | ×0.1^22 = 0.0 |
| | | **Σ** | **8.1** |

`yours 2.0 / Σ 8.1 = 24.8%`  
`$25 ÷ 13 ÷ 2 = $0.96 × 24.8% = $0.24/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon` ← this one
6. `pintc-meet-trump-2026-12-31-kimkar`
7. `pintc-meet-trump-2026-12-31-leoxiv`
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput`
11. `pintc-meet-trump-2026-12-31-volzel`
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 100 @ 17¢ → $4.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 343 (100 yours) | ×0.2^0 = 343.0 |
|  | 15¢ | 4,501 | ×0.2^2 = 180.0 |
|  | 13¢ | 6,115 | ×0.2^4 = 9.8 |
| | | **Σ** | **532.8** |

`yours 100.0 / Σ 532.8 = 18.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 18.8% = $4.69/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 82¢ → $0.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 74 (10 yours) | ×0.2^0 = 74.2 |
|  | 80¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,459 | ×0.2^81 = 0.0 |
| | | **Σ** | **74.2** |

`yours 10.0 / Σ 74.2 = 13.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 13.5% = $0.56/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 12 @ 58¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 93 (12 yours) | ×0.2^0 = 93.0 |
|  | 60¢ | 6 | ×0.2^2 = 0.3 |
|  | 62¢ | 107 | ×0.2^4 = 0.2 |
|  | 81¢ | 107 | ×0.2^23 = 0.0 |
|  | 99¢ | 9,562 | ×0.2^41 = 0.0 |
| | | **Σ** | **93.4** |

`yours 12.0 / Σ 93.4 = 12.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 12.8% = $0.54/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> BUY 15 @ 31¢ → $0.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 31¢ | 120 (15 yours) | ×0.2^0 = 119.5 |
|  | 29¢ | 3 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,405 | ×0.2^30 = 0.0 |
| | | **Σ** | **119.7** |

`yours 15.0 / Σ 119.7 = 12.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 12.5% = $0.52/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 50 @ 70¢ → $0.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 71¢ | 74 | ×0.2^0 = 74.0 |
| ▶ | 70¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 69¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,410 | ×0.2^70 = 0.0 |
| | | **Σ** | **84.1** |

`yours 10.0 / Σ 84.1 = 11.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.9% = $0.50/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-ind</code> SELL 32 @ 2¢ → $0.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 62 (32 yours) | ×0.35^0 = 62.0 |
|  | 4¢ | 14 | ×0.35^2 = 1.7 |
|  | 7¢ | 46 | ×0.35^5 = 0.2 |
|  | 8¢ | 151,584 | ×0.35^6 = 278.7 |
| | | **Σ** | **342.6** |

`yours 32.0 / Σ 342.6 = 9.3%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 9.3% = $0.32/day`  

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
22. `tec-cbb-champ-2027-04-05-w-ind` ← this one
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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 981 | ×0.35^0 = 981.0 |
| ▶ | 1¢ | 9,987 (1,000 yours) | ×0.35^1 = 3,495.4 |
| | | **Σ** | **4,476.4** |

`yours 350.0 / Σ 4,476.4 = 7.8%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 7.8% = $0.27/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 15 @ 7¢ → $0.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 213 (15 yours) | ×0.2^0 = 213.0 |
|  | 9¢ | 2 | ×0.2^2 = 0.1 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 99¢ | 8,891 | ×0.2^92 = 0.0 |
| | | **Σ** | **213.1** |

`yours 15.0 / Σ 213.1 = 7.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.0% = $0.29/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 10 @ 18¢ → $0.86/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 31 (10 yours) | ×0.1^0 = 31.0 |
|  | 20¢ | 11,351 | ×0.1^2 = 113.5 |
| | | **Σ** | **144.5** |

`yours 10.0 / Σ 144.5 = 6.9%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 6.9% = $0.86/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $0.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 1,161 | ×0.2^0 = 1,161.0 |
| ▶ | 4¢ | 500 (500 yours) | ×0.2^1 = 100.0 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **1,661.0** |

`yours 100.0 / Σ 1,661.0 = 6.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.0% = $0.23/day`  

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
11. `scc-senate-gop-2026-11-03-56` ← this one
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 20 @ 15¢ → $0.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 38 | ×0.1^0 = 38.2 |
| ▶ | 15¢ | 20 (20 yours) | ×0.1^1 = 2.0 |
|  | 14¢ | 7 | ×0.1^2 = 0.1 |
|  | 8¢ | 5 | ×0.1^8 = 0.0 |
|  | 4¢ | 10 | ×0.1^12 = 0.0 |
|  | 2¢ | 7 | ×0.1^14 = 0.0 |
|  | 1¢ | 13,050 | ×0.1^15 = 0.0 |
| | | **Σ** | **40.3** |

`yours 2.0 / Σ 40.3 = 5.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 5.0% = $0.62/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 5,000 @ 1¢ → $0.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 105,728 (5,000 yours) | ×0.2^0 = 105,728.0 |
| | | **Σ** | **105,728.0** |

`yours 5,000.0 / Σ 105,728.0 = 4.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 4.7% = $0.18/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 1 | ×0.2^0 = 1.1 |
|  | 7¢ | 3 | ×0.2^1 = 0.6 |
|  | 2¢ | 232 | ×0.2^6 = 0.0 |
| ▶ | 1¢ | 25,334 (5,000 yours) | ×0.2^7 = 0.3 |
| | | **Σ** | **2.0** |

`yours 0.1 / Σ 2.0 = 3.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.2% = $0.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5,000 @ 1¢ → $0.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 174,136 (5,000 yours) | ×0.2^0 = 174,136.5 |
| | | **Σ** | **174,136.5** |

`yours 5,000.0 / Σ 174,136.5 = 2.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 2.9% = $0.11/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1,000 @ 3¢ → $0.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 35,012 (1,000 yours) | ×0.2^0 = 35,012.0 |
| | | **Σ** | **35,012.0** |

`yours 1,000.0 / Σ 35,012.0 = 2.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 2.9% = $0.11/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> SELL 1 @ 84¢ → $0.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 27 (1 yours) | ×0.2^0 = 27.0 |
|  | 85¢ | 44 | ×0.2^1 = 8.8 |
|  | 86¢ | 19 | ×0.2^2 = 0.8 |
|  | 99¢ | 5,809 | ×0.2^15 = 0.0 |
| | | **Σ** | **36.6** |

`yours 1.0 / Σ 36.6 = 2.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 2.7% = $0.11/day`  

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
<details><summary><code>ewc-usse-oh-2026-11-03-rep</code> BUY 50 @ 48¢ → $0.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 1,411 (50 yours) | ×0.2^0 = 1,411.0 |
|  | 46¢ | 10,872 | ×0.2^2 = 434.9 |
| | | **Σ** | **1,845.9** |

`yours 50.0 / Σ 1,845.9 = 2.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 2.7% = $0.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-oh-2026-11-03-dem`
2. `ewc-usse-oh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usse-tx-2026-11-03-dem</code> BUY 50 @ 47¢ → $1.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 555 (50 yours) | ×0.2^0 = 555.0 |
|  | 46¢ | 6,360 | ×0.2^1 = 1,272.0 |
|  | 45¢ | 2,228 | ×0.2^2 = 89.1 |
|  | 35¢ | 15,000 | ×0.2^12 = 0.0 |
| | | **Σ** | **1,916.1** |

`yours 50.0 / Σ 1,916.1 = 2.6%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 2.6% = $1.96/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-tx-2026-11-03-dem` ← this one
2. `ewc-usse-tx-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-01 | ~$46.23 | $52.30 | 113% |
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |

Biggest gaps on 2026-08-01: `scc-hrep-rep-2026-11-03-gte215` (est ~$2.09 → got $1.51), `scc-senate-gop-2026-11-03-52` (est ~$3.15 → got $2.78), `cranc-uspres28-12-31-2026-tedcru` (est ~$0.71 → got $0.35)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (26,613 resting) | ~66.0% | ~$16.50 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,628 resting) | ~64.9% | ~$16.22 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (80,607 resting) | ~12.3% | ~$9.25 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (322,517 resting) | ~12.2% | ~$9.13 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (130,811 resting) | ~9.0% | ~$6.74 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,897 resting) | ~21.6% | ~$5.40 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (187,905 resting) | ~2.4% | ~$1.79 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (85,488 resting) | ~2.2% | ~$1.65 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (123,824 resting) | ~2.1% | ~$1.57 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (88,057 resting) | ~6.2% | ~$1.55 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (137,278 resting) | ~1.4% | ~$1.06 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $300.00 ÷ 3 | 0.20 | 10,000 | SELL side (9,915 resting) | ~2.0% | ~$0.99 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,514.21 |
| Skipped | $1.21 |
| **Total earned** | **$1,515.42** |

1532 reward rows · 30 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-01 | $52.30 | `█████` |
| 2026-07-31 | $67.96 | `██████` |
| 2026-07-30 | $20.48 | `██` |
| 2026-07-29 | $53.59 | `█████` |
| 2026-07-28 | $79.65 | `███████` |
| 2026-07-27 | $125.34 | `███████████` |
| 2026-07-26 | $153.80 | `██████████████` |
| 2026-07-25 | $125.69 | `███████████` |
| 2026-07-24 | $135.19 | `████████████` |
| 2026-07-23 | $227.63 | `████████████████████` |
| 2026-07-22 | $82.95 | `███████` |
| 2026-07-21 | $91.44 | `████████` |
| 2026-07-20 | $106.54 | `█████████` |
| 2026-07-19 | $35.81 | `███` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $52.30 | `█` |
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.60 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.96 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-03 9:07 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 9:02 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:17 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 6:29 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 4:40 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 3:00 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 1:22 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 11:20 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:30 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:15 AM ET | ✅ ok | 1532 | $1515.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
