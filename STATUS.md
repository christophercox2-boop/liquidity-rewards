# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-03 11:42 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$92.83/day estimated (ceiling, not promise — details below)

**Earned:** $1,529.47 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-02: **$14.05** · 2026-08-01: **$52.30** · 2026-07-31: **$67.96** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$23.58/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$23.52/day), `ewc-usgub-ca-2026-11-03-xavbec` (~$20.08/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$92.83/day (~$3.87/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `apdc-alito-2026-12-31` | BUY | 21.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~99.3% of bid side (6,114 resting ≥ 5,000 ✓) ≈ $24.84/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 24.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~91.8% of bid side (5,558 resting ≥ 5,000 ✓) ≈ $3.53/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 67.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~89.1% of ask side (12,338 resting ≥ 5,000 ✓) ≈ $3.71/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | SELL | 22.0¢ | 84 | 0 | $100.00 | ✅ scoring — ~87.2% of ask side (10,212 resting ≥ 5,000 ✓) ≈ $21.80/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~76.0% of ask side (12,055 resting ≥ 5,000 ✓) ≈ $2.92/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 14.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~67.8% of bid side (5,479 resting ≥ 5,000 ✓) ≈ $2.61/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 9.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~55.9% of ask side (12,275 resting ≥ 5,000 ✓) ≈ $2.15/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 41 | 0 | $100.00 | ✅ scoring — ~52.0% of ask side (12,164 resting ≥ 5,000 ✓) ≈ $2.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~51.4% of ask side (12,072 resting ≥ 5,000 ✓) ≈ $1.98/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 15.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~47.0% of ask side (14,170 resting ≥ 2,000 ✓) ≈ $5.88/day |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 88.0¢ | 34 | 0 | $100.00 | ✅ scoring — ~47.0% of ask side (12,164 resting ≥ 5,000 ✓) ≈ $1.96/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 86.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~45.4% of bid side (5,495 resting ≥ 5,000 ✓) ≈ $1.89/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 79.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~43.4% of bid side (5,525 resting ≥ 5,000 ✓) ≈ $1.81/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~43.1% of ask side (12,305 resting ≥ 5,000 ✓) ≈ $1.66/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~38.5% of ask side (12,174 resting ≥ 5,000 ✓) ≈ $1.48/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 7.0¢ | 3 | 1 | $100.00 | ✅ scoring — ~29.2% of bid side (25,570 resting ≥ 5,000 ✓) ≈ $1.12/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 26.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~27.5% of ask side (12,212 resting ≥ 5,000 ✓) ≈ $1.06/day (pool ÷ 13 markets) |
| `pintc-meet-trump-2026-12-31-kimjon` | BUY | 23.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~24.8% of bid side (2,250 resting ≥ 2,000 ✓) ≈ $0.24/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 1 | $100.00 | ✅ scoring — ~23.8% of ask side (12,443 resting ≥ 5,000 ✓) ≈ $0.91/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~18.1% of bid side (5,375 resting ≥ 5,000 ✓) ≈ $0.75/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~17.4% of ask side (9,736 resting ≥ 5,000 ✓) ≈ $0.72/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 9.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~14.9% of ask side (12,443 resting ≥ 5,000 ✓) ≈ $0.57/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~13.5% of bid side (5,534 resting ≥ 5,000 ✓) ≈ $0.56/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 31.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~12.5% of bid side (5,528 resting ≥ 5,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 7.0¢ | 400 | 0 | $100.00 | ✅ scoring — ~9.8% of bid side (9,310 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-ind` | SELL | 2.0¢ | 32 | 0 | $500.00 | ✅ scoring — ~9.3% of ask side (153,791 resting ≥ 2,500 ✓) ≈ $0.32/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 18.0¢ | 35 | 0 | $100.00 | ✅ scoring — ~8.7% of bid side (5,606 resting ≥ 5,000 ✓) ≈ $0.36/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 12.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~8.0% of bid side (5,661 resting ≥ 5,000 ✓) ≈ $0.31/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~7.9% of ask side (5,510 resting ≥ 5,000 ✓) ≈ $0.33/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 5.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~7.7% of bid side (105,791 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 13 markets) |
| …and 60 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>apdc-alito-2026-12-31</code> BUY 100 @ 21¢ → $24.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 100 (100 yours) | ×0.2^0 = 100.0 |
|  | 19¢ | 5 | ×0.2^2 = 0.2 |
|  | 17¢ | 100 | ×0.2^4 = 0.2 |
|  | 15¢ | 4,494 | ×0.2^6 = 0.3 |
|  | 11¢ | 1,215 | ×0.2^10 = 0.0 |
| | | **Σ** | **100.7** |

`yours 100.0 / Σ 100.7 = 99.3%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 99.3% = $24.84/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

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
|  | 75¢ | 1 | ×0.2^8 = 0.0 |
|  | 83¢ | 164 | ×0.2^16 = 0.0 |
|  | 90¢ | 1 | ×0.2^23 = 0.0 |
|  | 99¢ | 12,113 | ×0.2^32 = 0.0 |
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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 84 @ 22¢ → $21.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 96 (84 yours) | ×0.2^0 = 96.2 |
|  | 24¢ | 1 | ×0.2^2 = 0.1 |
|  | 26¢ | 192 | ×0.2^4 = 0.3 |
|  | 46¢ | 200 | ×0.2^24 = 0.0 |
|  | 49¢ | 100 | ×0.2^27 = 0.0 |
|  | 99¢ | 9,623 | ×0.2^77 = 0.0 |
| | | **Σ** | **96.5** |

`yours 84.2 / Σ 96.5 = 87.2%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 87.2% = $21.80/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 3 @ 15¢ → $2.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 4 (3 yours) | ×0.2^0 = 4.3 |
|  | 18¢ | 5 | ×0.2^3 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,745 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **4.3** |

`yours 3.3 / Σ 4.3 = 76.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 76.0% = $2.92/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 15 @ 14¢ → $2.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 22 (15 yours) | ×0.2^0 = 22.0 |
|  | 12¢ | 3 | ×0.2^2 = 0.1 |
|  | 11¢ | 2 | ×0.2^3 = 0.0 |
|  | 6¢ | 32 | ×0.2^8 = 0.0 |
|  | 1¢ | 5,420 | ×0.2^13 = 0.0 |
| | | **Σ** | **22.1** |

`yours 15.0 / Σ 22.1 = 67.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.8% = $2.61/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 9¢ → $2.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 43 (30 yours) | ×0.2^0 = 43.0 |
|  | 11¢ | 100 | ×0.2^2 = 4.0 |
|  | 12¢ | 831 | ×0.2^3 = 6.6 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **53.7** |

`yours 30.0 / Σ 53.7 = 55.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.9% = $2.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 41 @ 22¢ → $2.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 79 (41 yours) | ×0.2^0 = 79.2 |
|  | 24¢ | 0 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 98¢ | 1,784 | ×0.2^76 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^77 = 0.0 |
| | | **Σ** | **79.2** |

`yours 41.2 / Σ 79.2 = 52.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 52.0% = $2.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 15 @ 18¢ → $1.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 29 (15 yours) | ×0.2^0 = 29.0 |
|  | 19¢ | 1 | ×0.2^1 = 0.2 |
|  | 20¢ | 0 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,741 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^81 = 0.0 |
| | | **Σ** | **29.2** |

`yours 15.0 / Σ 29.2 = 51.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 51.4% = $1.98/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 10 @ 15¢ → $5.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 21 (10 yours) | ×0.1^0 = 20.9 |
|  | 17¢ | 1 | ×0.1^2 = 0.0 |
|  | 20¢ | 13,568 | ×0.1^5 = 0.1 |
| | | **Σ** | **21.0** |

`yours 9.9 / Σ 21.0 = 47.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 47.0% = $5.88/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 34 @ 88¢ → $1.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 72 (34 yours) | ×0.2^0 = 72.0 |
|  | 90¢ | 10 | ×0.2^2 = 0.4 |
|  | 99¢ | 12,082 | ×0.2^11 = 0.0 |
| | | **Σ** | **72.4** |

`yours 34.0 / Σ 72.4 = 47.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 47.0% = $1.96/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 20 @ 86¢ → $1.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 86¢ | 44 (20 yours) | ×0.2^0 = 44.0 |
|  | 84¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^85 = 0.0 |
| | | **Σ** | **44.0** |

`yours 20.0 / Σ 44.0 = 45.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 45.4% = $1.89/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 20 @ 79¢ → $1.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 39 (20 yours) | ×0.2^0 = 39.0 |
|  | 78¢ | 35 | ×0.2^1 = 7.0 |
|  | 77¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,450 | ×0.2^78 = 0.0 |
| | | **Σ** | **46.1** |

`yours 20.0 / Σ 46.1 = 43.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 43.4% = $1.81/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 50 @ 10¢ → $1.66/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 96 (50 yours) | ×0.2^0 = 96.0 |
|  | 11¢ | 100 | ×0.2^1 = 20.0 |
|  | 12¢ | 0 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,808 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **116.0** |

`yours 50.0 / Σ 116.0 = 43.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.1% = $1.66/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 104 (40 yours) | ×0.2^0 = 104.0 |
|  | 8¢ | 0 | ×0.2^2 = 0.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **104.0** |

`yours 40.0 / Σ 104.0 = 38.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.5% = $1.48/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 26¢ → $1.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 18 (5 yours) | ×0.2^0 = 18.0 |
|  | 27¢ | 1 | ×0.2^1 = 0.2 |
|  | 28¢ | 0 | ×0.2^2 = 0.0 |
|  | 43¢ | 100 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^24 = 0.0 |
|  | 98¢ | 1,792 | ×0.2^72 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^73 = 0.0 |
| | | **Σ** | **18.2** |

`yours 5.0 / Σ 18.2 = 27.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.5% = $1.06/day`  

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
|  | 1¢ | 2,134 | ×0.1^22 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $0.91/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 15 | ×0.2^0 = 15.0 |
| ▶ | 10¢ | 93 (40 yours) | ×0.2^1 = 18.6 |
|  | 11¢ | 0 | ×0.2^2 = 0.0 |
|  | 30¢ | 112 | ×0.2^21 = 0.0 |
|  | 40¢ | 30 | ×0.2^31 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,892 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **33.7** |

`yours 8.0 / Σ 33.7 = 23.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 23.8% = $0.91/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 30 @ 85¢ → $0.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 166 (30 yours) | ×0.2^0 = 166.1 |
|  | 83¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,208 | ×0.2^84 = 0.0 |
| | | **Σ** | **166.2** |

`yours 30.0 / Σ 166.2 = 18.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.1% = $0.75/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 10 @ 10¢ → $0.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 57 (10 yours) | ×0.2^0 = 57.3 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 14¢ | 100 | ×0.2^4 = 0.2 |
|  | 20¢ | 1 | ×0.2^10 = 0.0 |
|  | 50¢ | 25 | ×0.2^40 = 0.0 |
|  | 99¢ | 9,552 | ×0.2^89 = 0.0 |
| | | **Σ** | **57.5** |

`yours 10.0 / Σ 57.5 = 17.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 17.4% = $0.72/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 5 @ 9¢ → $0.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 15 (5 yours) | ×0.2^0 = 15.0 |
|  | 10¢ | 93 | ×0.2^1 = 18.6 |
|  | 11¢ | 0 | ×0.2^2 = 0.0 |
|  | 30¢ | 112 | ×0.2^21 = 0.0 |
|  | 40¢ | 30 | ×0.2^31 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,892 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **33.7** |

`yours 5.0 / Σ 33.7 = 14.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.9% = $0.57/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 400 @ 7¢ → $0.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 4,090 (400 yours) | ×0.2^0 = 4,090.1 |
|  | 5¢ | 20 | ×0.2^2 = 0.8 |
|  | 1¢ | 5,200 | ×0.2^6 = 0.3 |
| | | **Σ** | **4,091.3** |

`yours 400.0 / Σ 4,091.3 = 9.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 9.8% = $0.41/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-ind</code> SELL 32 @ 2¢ → $0.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 64 (32 yours) | ×0.35^0 = 64.0 |
|  | 4¢ | 14 | ×0.35^2 = 1.7 |
|  | 7¢ | 46 | ×0.35^5 = 0.2 |
|  | 8¢ | 151,584 | ×0.35^6 = 278.7 |
| | | **Σ** | **344.6** |

`yours 32.0 / Σ 344.6 = 9.3%`  
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 35 @ 18¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 400 (35 yours) | ×0.2^0 = 400.0 |
|  | 16¢ | 6 | ×0.2^2 = 0.3 |
|  | 1¢ | 5,200 | ×0.2^17 = 0.0 |
| | | **Σ** | **400.3** |

`yours 35.0 / Σ 400.3 = 8.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 8.7% = $0.36/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 5 @ 12¢ → $0.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 62 (5 yours) | ×0.2^0 = 62.0 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 8¢ | 50 | ×0.2^4 = 0.1 |
|  | 1¢ | 5,548 | ×0.2^11 = 0.0 |
| | | **Σ** | **62.1** |

`yours 5.0 / Σ 62.1 = 8.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.0% = $0.31/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 15 @ 7¢ → $0.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 189 (15 yours) | ×0.2^0 = 189.0 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 99¢ | 5,294 | ×0.2^92 = 0.0 |
| | | **Σ** | **189.1** |

`yours 15.0 / Σ 189.1 = 7.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.9% = $0.33/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 50 @ 5¢ → $0.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 481 (50 yours) | ×0.2^0 = 481.0 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 1¢ | 105,306 | ×0.2^4 = 168.5 |
| | | **Σ** | **649.6** |

`yours 50.0 / Σ 649.6 = 7.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.7% = $0.30/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-02 | ~$25.55 | $14.05 | 55% |
| 2026-08-01 | ~$46.23 | $52.30 | 113% |
| 2026-07-31 | ~$64.95 | $67.96 | 105% |

Biggest gaps on 2026-08-02: `scc-senate-gop-2026-11-03-47` (est ~$2.48 → got $0.81), `scc-senate-gop-2026-11-03-51` (est ~$2.03 → got $0.48), `scc-senate-gop-2026-11-03-53` (est ~$1.30 → got $0.13)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,349 resting) | ~94.3% | ~$23.58 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (26,196 resting) | ~94.1% | ~$23.52 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (323,606 resting) | ~26.8% | ~$20.08 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,348 resting) | ~66.4% | ~$16.61 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (79,994 resting) | ~12.6% | ~$9.49 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,159 resting) | ~29.0% | ~$7.25 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,733 resting) | ~24.6% | ~$6.16 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (236,898 resting) | ~5.0% | ~$3.74 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (189,561 resting) | ~2.4% | ~$1.81 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (123,878 resting) | ~2.1% | ~$1.58 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (99,273 resting) | ~1.8% | ~$1.32 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (93,601 resting) | ~1.7% | ~$1.28 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,514.21 |
| Pending | $14.05 |
| Skipped | $1.21 |
| **Total earned** | **$1,529.47** |

1573 reward rows · 31 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-02 | $14.05 | `█` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $66.35 | `█` |
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $35.05 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `apdc-alito-2026-12-31` | $23.38 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-03 11:42 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 10:10 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:31 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:24 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:12 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:10 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:07 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 9:02 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 8:17 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 6:29 PM ET | ✅ ok | 1532 | $1515.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
