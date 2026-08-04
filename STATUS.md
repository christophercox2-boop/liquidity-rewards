# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-04 6:01 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$77.22/day estimated (ceiling, not promise — details below)

**Earned:** $1,529.47 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-02: **$14.05** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-01: **$52.30** · 2026-07-31: **$67.96** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$24.82/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-12-31` (~$16.61/day), `ewc-usgub-ca-2026-11-03-xavbec` (~$13.22/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$77.22/day (~$3.22/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (12,049 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 67.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~99.7% of ask side (12,332 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 12.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~98.4% of bid side (5,603 resting ≥ 5,000 ✓) ≈ $3.79/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 26.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~96.5% of ask side (12,199 resting ≥ 5,000 ✓) ≈ $3.71/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 14.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~96.1% of bid side (5,478 resting ≥ 5,000 ✓) ≈ $3.70/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 24.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~91.8% of bid side (5,558 resting ≥ 5,000 ✓) ≈ $3.53/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 21.0¢ | 80 | 0 | $100.00 | ✅ scoring — ~84.8% of ask side (10,103 resting ≥ 5,000 ✓) ≈ $21.20/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 9.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~80.8% of ask side (11,819 resting ≥ 5,000 ✓) ≈ $3.11/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 7.0¢ | 400 | 0 | $100.00 | ✅ scoring — ~68.4% of bid side (5,987 resting ≥ 5,000 ✓) ≈ $2.85/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 41 | 0 | $100.00 | ✅ scoring — ~67.2% of ask side (12,147 resting ≥ 5,000 ✓) ≈ $2.59/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~65.1% of ask side (12,066 resting ≥ 5,000 ✓) ≈ $2.50/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 97.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~60.6% of ask side (11,108 resting ≥ 5,000 ✓) ≈ $2.53/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 79.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~46.5% of bid side (5,522 resting ≥ 5,000 ✓) ≈ $1.94/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~42.5% of ask side (12,165 resting ≥ 5,000 ✓) ≈ $1.64/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 5.0¢ | 590 | 0 | $100.00 | ✅ scoring — ~42.3% of bid side (85,500 resting ≥ 5,000 ✓) ≈ $1.63/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~41.0% of ask side (12,312 resting ≥ 5,000 ✓) ≈ $1.58/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 7.0¢ | 3 | 1 | $100.00 | ✅ scoring — ~33.4% of bid side (5,726 resting ≥ 5,000 ✓) ≈ $1.28/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 20.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~29.6% of ask side (5,878 resting ≥ 5,000 ✓) ≈ $1.23/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 1 | $100.00 | ✅ scoring — ~28.5% of ask side (12,292 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~20.2% of bid side (5,357 resting ≥ 5,000 ✓) ≈ $0.84/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~19.6% of bid side (4,258 resting ≥ 2,500 ✓) ≈ $0.67/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 9.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~17.8% of ask side (12,292 resting ≥ 5,000 ✓) ≈ $0.68/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 88.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~13.2% of ask side (5,500 resting ≥ 5,000 ✓) ≈ $0.55/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 2.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~12.2% of bid side (7,509 resting ≥ 5,000 ✓) ≈ $0.51/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 5.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~11.9% of bid side (85,621 resting ≥ 5,000 ✓) ≈ $0.46/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 30 | 3 | $100.00 | ✅ scoring — ~11.7% of ask side (12,102 resting ≥ 5,000 ✓) ≈ $0.49/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 9.0¢ | 75 | 0 | $100.00 | ✅ scoring — ~11.6% of ask side (11,950 resting ≥ 5,000 ✓) ≈ $0.45/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~10.8% of bid side (85,500 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 58.0¢ | 12 | 0 | $100.00 | ✅ scoring — ~10.1% of ask side (5,022 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 8.0¢ | 75 | 0 | $100.00 | ✅ scoring — ~9.1% of ask side (12,228 resting ≥ 5,000 ✓) ≈ $0.35/day (pool ÷ 13 markets) |
| …and 55 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 3 @ 15¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 3 (3 yours) | ×0.2^0 = 3.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,745 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **3.3** |

`yours 3.3 / Σ 3.3 = 100.0%`  
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 67¢ → $4.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 69¢ | 3 | ×0.2^2 = 0.1 |
|  | 72¢ | 1 | ×0.2^5 = 0.0 |
|  | 83¢ | 164 | ×0.2^16 = 0.0 |
|  | 90¢ | 1 | ×0.2^23 = 0.0 |
|  | 99¢ | 12,113 | ×0.2^32 = 0.0 |
| | | **Σ** | **50.1** |

`yours 50.0 / Σ 50.1 = 99.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.7% = $4.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 5 @ 12¢ → $3.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 8¢ | 50 | ×0.2^4 = 0.1 |
|  | 1¢ | 5,548 | ×0.2^11 = 0.0 |
| | | **Σ** | **5.1** |

`yours 5.0 / Σ 5.1 = 98.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.4% = $3.79/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 26¢ → $3.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 27¢ | 1 | ×0.2^1 = 0.2 |
|  | 43¢ | 100 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^24 = 0.0 |
|  | 98¢ | 1,792 | ×0.2^72 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^73 = 0.0 |
| | | **Σ** | **5.2** |

`yours 5.0 / Σ 5.2 = 96.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 96.5% = $3.71/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 15 @ 14¢ → $3.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 13¢ | 1 | ×0.2^1 = 0.2 |
|  | 12¢ | 10 | ×0.2^2 = 0.4 |
|  | 6¢ | 32 | ×0.2^8 = 0.0 |
|  | 1¢ | 5,420 | ×0.2^13 = 0.0 |
| | | **Σ** | **15.6** |

`yours 15.0 / Σ 15.6 = 96.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 96.1% = $3.70/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 80 @ 21¢ → $21.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 80 (80 yours) | ×0.2^0 = 80.2 |
|  | 22¢ | 70 | ×0.2^1 = 14.0 |
|  | 23¢ | 1 | ×0.2^2 = 0.1 |
|  | 25¢ | 192 | ×0.2^4 = 0.3 |
|  | 48¢ | 105 | ×0.2^27 = 0.0 |
|  | 99¢ | 9,655 | ×0.2^78 = 0.0 |
| | | **Σ** | **94.5** |

`yours 80.2 / Σ 94.5 = 84.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 84.8% = $21.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 9¢ → $3.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 30 (30 yours) | ×0.2^0 = 30.0 |
|  | 11¢ | 101 | ×0.2^2 = 4.0 |
|  | 12¢ | 387 | ×0.2^3 = 3.1 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **37.1** |

`yours 30.0 / Σ 37.1 = 80.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 80.8% = $3.11/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 400 @ 7¢ → $2.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 584 (400 yours) | ×0.2^0 = 584.0 |
|  | 5¢ | 20 | ×0.2^2 = 0.8 |
|  | 1¢ | 5,383 | ×0.2^6 = 0.3 |
| | | **Σ** | **585.1** |

`yours 400.0 / Σ 585.1 = 68.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 68.4% = $2.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 41 @ 22¢ → $2.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 61 (41 yours) | ×0.2^0 = 61.2 |
|  | 24¢ | 1 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 98¢ | 1,784 | ×0.2^76 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^77 = 0.0 |
| | | **Σ** | **61.2** |

`yours 41.2 / Σ 61.2 = 67.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.2% = $2.59/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 15 @ 18¢ → $2.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 23 (15 yours) | ×0.2^0 = 23.0 |
|  | 20¢ | 1 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,741 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^81 = 0.0 |
| | | **Σ** | **23.1** |

`yours 15.0 / Σ 23.1 = 65.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 65.1% = $2.50/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 5,000 @ 97¢ → $2.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 8,250 (5,000 yours) | ×0.2^0 = 8,250.0 |
| | | **Σ** | **8,250.0** |

`yours 5,000.0 / Σ 8,250.0 = 60.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 60.6% = $2.53/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 20 @ 79¢ → $1.94/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 36 (20 yours) | ×0.2^0 = 36.0 |
|  | 78¢ | 35 | ×0.2^1 = 7.0 |
|  | 77¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,450 | ×0.2^78 = 0.0 |
| | | **Σ** | **43.1** |

`yours 20.0 / Σ 43.1 = 46.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 46.5% = $1.94/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 94 (40 yours) | ×0.2^0 = 94.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **94.0** |

`yours 40.0 / Σ 94.0 = 42.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 42.5% = $1.64/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 590 @ 5¢ → $1.63/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1,258 (590 yours) | ×0.2^0 = 1,258.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 1¢ | 84,209 | ×0.2^4 = 134.7 |
| | | **Σ** | **1,394.1** |

`yours 590.0 / Σ 1,394.1 = 42.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 42.3% = $1.63/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 50 @ 10¢ → $1.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 102 (50 yours) | ×0.2^0 = 102.0 |
|  | 11¢ | 100 | ×0.2^1 = 20.0 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,808 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **122.0** |

`yours 50.0 / Σ 122.0 = 41.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 41.0% = $1.58/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 3 @ 7¢ → $1.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 1 | ×0.2^0 = 1.1 |
| ▶ | 7¢ | 3 (3 yours) | ×0.2^1 = 0.6 |
|  | 2¢ | 232 | ×0.2^6 = 0.0 |
|  | 1¢ | 5,490 | ×0.2^7 = 0.1 |
| | | **Σ** | **1.7** |

`yours 0.6 / Σ 1.7 = 33.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.4% = $1.28/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 30 @ 20¢ → $1.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 101 (30 yours) | ×0.2^0 = 101.2 |
|  | 22¢ | 1 | ×0.2^2 = 0.1 |
|  | 99¢ | 5,776 | ×0.2^79 = 0.0 |
| | | **Σ** | **101.2** |

`yours 30.0 / Σ 101.2 = 29.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 29.6% = $1.23/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $1.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 20 | ×0.2^0 = 19.8 |
| ▶ | 10¢ | 41 (40 yours) | ×0.2^1 = 8.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 30¢ | 112 | ×0.2^21 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,817 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **28.1** |

`yours 8.0 / Σ 28.1 = 28.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.5% = $1.10/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 30 @ 85¢ → $0.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 148 (30 yours) | ×0.2^0 = 148.2 |
|  | 83¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,208 | ×0.2^84 = 0.0 |
| | | **Σ** | **148.3** |

`yours 30.0 / Σ 148.3 = 20.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 20.2% = $0.84/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 459 | ×0.35^0 = 459.0 |
| ▶ | 1¢ | 3,799 (1,000 yours) | ×0.35^1 = 1,329.6 |
| | | **Σ** | **1,788.6** |

`yours 350.0 / Σ 1,788.6 = 19.6%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 19.6% = $0.67/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 5 @ 9¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 20 (5 yours) | ×0.2^0 = 19.8 |
|  | 10¢ | 41 | ×0.2^1 = 8.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 30¢ | 112 | ×0.2^21 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,817 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **28.1** |

`yours 5.0 / Σ 28.1 = 17.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.8% = $0.68/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 10 @ 88¢ → $0.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 76 (10 yours) | ×0.2^0 = 75.6 |
|  | 90¢ | 10 | ×0.2^2 = 0.4 |
|  | 99¢ | 5,415 | ×0.2^11 = 0.0 |
| | | **Σ** | **76.0** |

`yours 10.0 / Σ 76.0 = 13.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 13.2% = $0.55/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> BUY 500 @ 2¢ → $0.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 3,230 (500 yours) | ×0.2^0 = 3,230.0 |
|  | 1¢ | 4,279 | ×0.2^1 = 855.8 |
| | | **Σ** | **4,085.8** |

`yours 500.0 / Σ 4,085.8 = 12.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 12.2% = $0.51/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 50 @ 5¢ → $0.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 281 (50 yours) | ×0.2^0 = 281.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 1¢ | 85,306 | ×0.2^4 = 136.5 |
| | | **Σ** | **418.8** |

`yours 50.0 / Σ 418.8 = 11.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.9% = $0.46/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 30 @ 47¢ → $0.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 44¢ | 2 | ×0.2^0 = 1.8 |
|  | 46¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 47¢ | 30 (30 yours) | ×0.2^3 = 0.2 |
|  | 52¢ | 1 | ×0.2^8 = 0.0 |
|  | 69¢ | 100 | ×0.2^25 = 0.0 |
|  | 99¢ | 11,968 | ×0.2^55 = 0.0 |
| | | **Σ** | **2.1** |

`yours 0.2 / Σ 2.1 = 11.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.7% = $0.49/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 75 @ 9¢ → $0.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 644 (75 yours) | ×0.2^0 = 644.0 |
|  | 10¢ | 1 | ×0.2^1 = 0.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 16¢ | 3 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **644.2** |

`yours 75.0 / Σ 644.2 = 11.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.6% = $0.45/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 1,242 (500 yours) | ×0.2^0 = 1,242.0 |
|  | 1¢ | 84,258 | ×0.2^2 = 3,370.3 |
| | | **Σ** | **4,612.3** |

`yours 500.0 / Σ 4,612.3 = 10.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 10.8% = $0.42/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 12 @ 58¢ → $0.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 119 (12 yours) | ×0.2^0 = 119.3 |
|  | 60¢ | 2 | ×0.2^2 = 0.1 |
|  | 81¢ | 107 | ×0.2^23 = 0.0 |
|  | 99¢ | 4,793 | ×0.2^41 = 0.0 |
| | | **Σ** | **119.4** |

`yours 12.0 / Σ 119.4 = 10.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 10.1% = $0.42/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 75 @ 8¢ → $0.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 826 (75 yours) | ×0.2^0 = 826.0 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 14¢ | 100 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **826.1** |

`yours 75.0 / Σ 826.1 = 9.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.1% = $0.35/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-01 | ~$46.23 | $52.30 | 113% |
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |

Biggest gaps on 2026-08-01: `scc-hrep-rep-2026-11-03-gte215` (est ~$2.09 → got $1.51), `scc-senate-gop-2026-11-03-52` (est ~$3.15 → got $2.78), `cranc-uspres28-12-31-2026-tedcru` (est ~$0.71 → got $0.35)

_2026-08-02 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,338 resting) | ~99.3% | ~$24.82 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,591 resting) | ~66.4% | ~$16.61 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (322,356 resting) | ~17.6% | ~$13.22 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,294 resting) | ~51.0% | ~$12.74 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (77,995 resting) | ~14.0% | ~$10.53 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,833 resting) | ~24.6% | ~$6.16 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,500 resting) | ~20.9% | ~$5.23 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (237,342 resting) | ~5.9% | ~$4.43 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (124,055 resting) | ~2.4% | ~$1.77 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (108,095 resting) | ~1.9% | ~$1.44 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (191,928 resting) | ~1.8% | ~$1.35 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (79,627 resting) | ~18.9% | ~$1.18 |

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
| 2026-08-02 ⚠️ multi-day pending bucket | $14.05 | `█` |
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
| 2026-08-04 6:01 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 2:43 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 11:42 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 10:10 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:31 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:24 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:12 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:10 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:07 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 9:02 PM ET | ✅ ok | 1532 | $1515.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
