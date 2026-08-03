# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-03 7:48 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$68.36/day estimated (ceiling, not promise — details below)

**Earned:** $1,515.42 lifetime ($1,373.47 paid). Last three recorded days — 2026-08-01: **$52.30** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-31: **$67.96** · 2026-07-30: **$20.48** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — SELL at the best price, ~$24.20/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$19.15/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$16.37/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$68.36/day (~$2.85/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `pintc-meet-trump-2026-12-31-kimjon` | BUY | 20.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~99.5% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $0.96/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 24.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~91.7% of bid side (5,784 resting ≥ 5,000 ✓) ≈ $3.53/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 27.0¢ | 11 | 0 | $100.00 | ✅ scoring — ~68.6% of ask side (12,226 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 81.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~64.0% of bid side (5,663 resting ≥ 5,000 ✓) ≈ $2.67/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~63.5% of ask side (12,353 resting ≥ 5,000 ✓) ≈ $2.44/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 21.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~59.2% of bid side (5,565 resting ≥ 5,000 ✓) ≈ $2.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~50.0% of ask side (12,116 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-ind` | SELL | 2.0¢ | 32 | 0 | $500.00 | ✅ scoring — ~49.1% of ask side (5,297 resting ≥ 2,500 ✓) ≈ $1.68/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~45.7% of bid side (11,359 resting ≥ 5,000 ✓) ≈ $1.76/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~45.2% of bid side (5,473 resting ≥ 5,000 ✓) ≈ $1.88/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | SELL | 25.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~41.6% of ask side (9,789 resting ≥ 5,000 ✓) ≈ $10.41/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~39.5% of ask side (12,110 resting ≥ 5,000 ✓) ≈ $1.52/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 9.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~37.9% of ask side (12,391 resting ≥ 5,000 ✓) ≈ $1.46/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 16.0¢ | 28 | 0 | $100.00 | ✅ scoring — ~36.4% of bid side (5,563 resting ≥ 5,000 ✓) ≈ $1.40/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 17.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~35.7% of bid side (5,618 resting ≥ 5,000 ✓) ≈ $8.92/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~30.2% of bid side (5,532 resting ≥ 5,000 ✓) ≈ $1.16/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~28.4% of ask side (12,211 resting ≥ 5,000 ✓) ≈ $1.09/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 10.0¢ | 33 | 0 | $100.00 | ✅ scoring — ~28.0% of ask side (12,379 resting ≥ 5,000 ✓) ≈ $1.08/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 29.0¢ | 11 | 0 | $100.00 | ✅ scoring — ~27.2% of ask side (7,285 resting ≥ 5,000 ✓) ≈ $6.79/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 19.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~26.9% of ask side (12,410 resting ≥ 5,000 ✓) ≈ $1.03/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 55.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~26.2% of ask side (5,529 resting ≥ 5,000 ✓) ≈ $1.09/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 12 | 0 | $100.00 | ✅ scoring — ~24.0% of ask side (7,160 resting ≥ 5,000 ✓) ≈ $1.00/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 84.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~17.7% of bid side (5,247 resting ≥ 5,000 ✓) ≈ $0.74/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~17.7% of bid side (4,452 resting ≥ 2,500 ✓) ≈ $0.60/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 20.0¢ | 30 | 2 | $100.00 | ✅ scoring — ~16.2% of bid side (5,323 resting ≥ 5,000 ✓) ≈ $0.62/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 6.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~12.2% of bid side (12,609 resting ≥ 5,000 ✓) ≈ $0.51/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~11.0% of ask side (12,172 resting ≥ 5,000 ✓) ≈ $0.46/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-gnzg` | SELL | 7.0¢ | 2 | 0 | $500.00 | ✅ scoring — ~8.2% of ask side (2,782 resting ≥ 2,500 ✓) ≈ $0.28/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 5 | $100.00 | ✅ scoring — ~8.1% of bid side (25,583 resting ≥ 5,000 ✓) ≈ $0.31/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~7.7% of ask side (12,253 resting ≥ 5,000 ✓) ≈ $0.29/day (pool ÷ 13 markets) |
| …and 71 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>pintc-meet-trump-2026-12-31-kimjon</code> BUY 2 @ 20¢ → $0.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 2 (2 yours) | ×0.1^0 = 2.0 |
|  | 18¢ | 1 | ×0.1^2 = 0.0 |
|  | 5¢ | 100 | ×0.1^15 = 0.0 |
|  | 3¢ | 1 | ×0.1^17 = 0.0 |
|  | 1¢ | 2,396 | ×0.1^19 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 99.5%`  
`$25 ÷ 13 ÷ 2 = $0.96 × 99.5% = $0.96/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 24¢ → $3.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 2 | ×0.2^3 = 0.0 |
|  | 20¢ | 46 | ×0.2^4 = 0.1 |
|  | 18¢ | 10 | ×0.2^6 = 0.0 |
|  | 14¢ | 7 | ×0.2^10 = 0.0 |
|  | 10¢ | 100 | ×0.2^14 = 0.0 |
|  | 1¢ | 5,618 | ×0.2^23 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 91.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 91.7% = $3.53/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 11 @ 27¢ → $2.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 16 (11 yours) | ×0.2^0 = 15.9 |
|  | 29¢ | 1 | ×0.2^2 = 0.0 |
|  | 30¢ | 10 | ×0.2^3 = 0.1 |
|  | 34¢ | 35 | ×0.2^7 = 0.0 |
|  | 35¢ | 5 | ×0.2^8 = 0.0 |
|  | 43¢ | 100 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^23 = 0.0 |
|  | 98¢ | 1,758 | ×0.2^71 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^72 = 0.0 |
| | | **Σ** | **16.0** |

`yours 11.0 / Σ 16.0 = 68.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.6% = $2.64/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 10 @ 81¢ → $2.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 81¢ | 12 (10 yours) | ×0.2^0 = 12.0 |
|  | 79¢ | 0 | ×0.2^2 = 0.0 |
|  | 78¢ | 451 | ×0.2^3 = 3.6 |
|  | 1¢ | 5,200 | ×0.2^80 = 0.0 |
| | | **Σ** | **15.6** |

`yours 10.0 / Σ 15.6 = 64.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 64.0% = $2.67/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $2.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 63 (40 yours) | ×0.2^0 = 63.0 |
|  | 12¢ | 0 | ×0.2^2 = 0.0 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **63.0** |

`yours 40.0 / Σ 63.0 = 63.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 63.5% = $2.44/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 21¢ → $2.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.2^0 = 1.3 |
|  | 20¢ | 4 | ×0.2^1 = 0.9 |
|  | 9¢ | 4 | ×0.2^12 = 0.0 |
|  | 1¢ | 5,555 | ×0.2^20 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.3 / Σ 2.1 = 59.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 59.2% = $2.28/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 21 @ 8¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 42 (21 yours) | ×0.2^0 = 42.0 |
|  | 10¢ | 0 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,773 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **42.0** |

`yours 21.0 / Σ 42.0 = 50.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 50.0% = $1.92/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-ind</code> SELL 32 @ 2¢ → $1.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 65 (32 yours) | ×0.35^0 = 65.0 |
|  | 4¢ | 1 | ×0.35^2 = 0.1 |
|  | 15¢ | 862 | ×0.35^13 = 0.0 |
|  | 16¢ | 1 | ×0.35^14 = 0.0 |
|  | 20¢ | 21 | ×0.35^18 = 0.0 |
|  | 25¢ | 400 | ×0.35^23 = 0.0 |
|  | 50¢ | 200 | ×0.35^48 = 0.0 |
|  | 97¢ | 48 | ×0.35^95 = 0.0 |
|  | 98¢ | 1,000 | ×0.35^96 = 0.0 |
| | | **Σ** | **65.1** |

`yours 32.0 / Σ 65.1 = 49.1%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 49.1% = $1.68/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $1.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 674 (500 yours) | ×0.2^0 = 674.0 |
|  | 2¢ | 10,485 | ×0.2^2 = 419.4 |
| | | **Σ** | **1,093.4** |

`yours 500.0 / Σ 1,093.4 = 45.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 45.7% = $1.76/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 82¢ → $1.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 22 (10 yours) | ×0.2^0 = 22.0 |
|  | 81¢ | 1 | ×0.2^1 = 0.1 |
|  | 80¢ | 0 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^81 = 0.0 |
| | | **Σ** | **22.1** |

`yours 10.0 / Σ 22.1 = 45.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 45.2% = $1.88/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 25¢ → $10.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 240 (100 yours) | ×0.2^0 = 240.0 |
|  | 27¢ | 1 | ×0.2^2 = 0.1 |
|  | 30¢ | 192 | ×0.2^5 = 0.1 |
|  | 46¢ | 200 | ×0.2^21 = 0.0 |
|  | 49¢ | 100 | ×0.2^24 = 0.0 |
|  | 99¢ | 9,056 | ×0.2^74 = 0.0 |
| | | **Σ** | **240.1** |

`yours 100.0 / Σ 240.1 = 41.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 41.6% = $10.41/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 18 @ 15¢ → $1.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 46 (18 yours) | ×0.2^0 = 46.3 |
|  | 17¢ | 0 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **46.3** |

`yours 18.3 / Σ 46.3 = 39.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 39.5% = $1.52/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 50 @ 9¢ → $1.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 128 (50 yours) | ×0.2^0 = 128.0 |
|  | 11¢ | 100 | ×0.2^2 = 4.0 |
|  | 29¢ | 2 | ×0.2^20 = 0.0 |
|  | 35¢ | 2 | ×0.2^26 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,858 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **132.0** |

`yours 50.0 / Σ 132.0 = 37.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.9% = $1.46/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 28 @ 16¢ → $1.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 69 (28 yours) | ×0.2^0 = 69.0 |
|  | 15¢ | 40 | ×0.2^1 = 8.0 |
|  | 14¢ | 1 | ×0.2^2 = 0.0 |
|  | 7¢ | 7 | ×0.2^9 = 0.0 |
|  | 1¢ | 5,446 | ×0.2^15 = 0.0 |
| | | **Σ** | **77.0** |

`yours 28.0 / Σ 77.0 = 36.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 36.4% = $1.40/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 100 @ 17¢ → $8.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 100 (100 yours) | ×0.2^0 = 100.0 |
|  | 16¢ | 100 | ×0.2^1 = 20.0 |
|  | 15¢ | 4,003 | ×0.2^2 = 160.1 |
|  | 11¢ | 1,215 | ×0.2^6 = 0.1 |
| | | **Σ** | **280.2** |

`yours 100.0 / Σ 280.2 = 35.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 35.7% = $8.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 100 @ 20¢ → $1.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 331 (100 yours) | ×0.2^0 = 331.5 |
|  | 18¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **331.5** |

`yours 100.0 / Σ 331.5 = 30.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.2% = $1.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 141 (40 yours) | ×0.2^0 = 141.0 |
|  | 8¢ | 0 | ×0.2^2 = 0.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **141.0** |

`yours 40.0 / Σ 141.0 = 28.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.4% = $1.09/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 33 @ 10¢ → $1.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 98 (33 yours) | ×0.2^0 = 98.0 |
|  | 11¢ | 100 | ×0.2^1 = 20.0 |
|  | 12¢ | 0 | ×0.2^2 = 0.0 |
|  | 15¢ | 30 | ×0.2^5 = 0.0 |
|  | 18¢ | 4 | ×0.2^8 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,846 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **118.0** |

`yours 33.0 / Σ 118.0 = 28.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.0% = $1.08/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 11 @ 29¢ → $6.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 39 (11 yours) | ×0.2^0 = 39.0 |
|  | 31¢ | 22 | ×0.2^2 = 0.9 |
|  | 34¢ | 1,906 | ×0.2^5 = 0.6 |
|  | 35¢ | 1 | ×0.2^6 = 0.0 |
|  | 36¢ | 3 | ×0.2^7 = 0.0 |
|  | 53¢ | 114 | ×0.2^24 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^70 = 0.0 |
| | | **Σ** | **40.5** |

`yours 11.0 / Σ 40.5 = 27.2%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 27.2% = $6.79/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 19¢ → $1.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 160 (43 yours) | ×0.2^0 = 160.0 |
|  | 21¢ | 0 | ×0.2^2 = 0.0 |
|  | 27¢ | 39 | ×0.2^8 = 0.0 |
|  | 38¢ | 37 | ×0.2^19 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 98¢ | 1,873 | ×0.2^79 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^80 = 0.0 |
| | | **Σ** | **160.0** |

`yours 43.0 / Σ 160.0 = 26.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.9% = $1.03/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 10 @ 55¢ → $1.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 55¢ | 38 (10 yours) | ×0.2^0 = 38.0 |
|  | 57¢ | 3 | ×0.2^2 = 0.1 |
|  | 60¢ | 20 | ×0.2^5 = 0.0 |
|  | 67¢ | 50 | ×0.2^12 = 0.0 |
|  | 83¢ | 1 | ×0.2^28 = 0.0 |
|  | 89¢ | 139 | ×0.2^34 = 0.0 |
|  | 90¢ | 1 | ×0.2^35 = 0.0 |
|  | 92¢ | 1 | ×0.2^37 = 0.0 |
|  | 99¢ | 5,275 | ×0.2^44 = 0.0 |
| | | **Σ** | **38.1** |

`yours 10.0 / Σ 38.1 = 26.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 26.2% = $1.09/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 12 @ 48¢ → $1.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 50 (12 yours) | ×0.2^0 = 50.0 |
|  | 50¢ | 0 | ×0.2^2 = 0.0 |
|  | 67¢ | 107 | ×0.2^19 = 0.0 |
|  | 81¢ | 107 | ×0.2^33 = 0.0 |
|  | 99¢ | 6,896 | ×0.2^51 = 0.0 |
| | | **Σ** | **50.0** |

`yours 12.0 / Σ 50.0 = 24.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 24.0% = $1.00/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 20 @ 84¢ → $0.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 85¢ | 19 | ×0.2^0 = 18.6 |
| ▶ | 84¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 83¢ | 0 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,208 | ×0.2^84 = 0.0 |
| | | **Σ** | **22.6** |

`yours 4.0 / Σ 22.6 = 17.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 17.7% = $0.74/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 653 | ×0.35^0 = 653.2 |
| ▶ | 1¢ | 3,799 (1,000 yours) | ×0.35^1 = 1,329.6 |
| | | **Σ** | **1,982.8** |

`yours 350.0 / Σ 1,982.8 = 17.7%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 17.7% = $0.60/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 30 @ 20¢ → $0.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 22¢ | 6 | ×0.2^0 = 6.0 |
|  | 21¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 20¢ | 30 (30 yours) | ×0.2^2 = 1.2 |
|  | 15¢ | 13 | ×0.2^7 = 0.0 |
|  | 14¢ | 72 | ×0.2^8 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^21 = 0.0 |
| | | **Σ** | **7.4** |

`yours 1.2 / Σ 7.4 = 16.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.2% = $0.62/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 30 @ 6¢ → $0.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 225 (30 yours) | ×0.2^0 = 225.0 |
|  | 5¢ | 5 | ×0.2^1 = 1.0 |
|  | 4¢ | 2 | ×0.2^2 = 0.1 |
|  | 2¢ | 12,176 | ×0.2^4 = 19.5 |
| | | **Σ** | **245.6** |

`yours 30.0 / Σ 245.6 = 12.2%`  
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
9. `scc-hrep-rep-2026-11-03-gte220` ← this one
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 15 @ 7¢ → $0.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 136 (15 yours) | ×0.2^0 = 136.0 |
|  | 9¢ | 0 | ×0.2^2 = 0.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 99¢ | 12,010 | ×0.2^92 = 0.0 |
| | | **Σ** | **136.0** |

`yours 15.0 / Σ 136.0 = 11.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.0% = $0.46/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-gnzg</code> SELL 2 @ 7¢ → $0.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 24 (2 yours) | ×0.35^0 = 24.2 |
|  | 9¢ | 1 | ×0.35^2 = 0.1 |
|  | 14¢ | 4 | ×0.35^7 = 0.0 |
|  | 23¢ | 86 | ×0.35^16 = 0.0 |
|  | 24¢ | 1,223 | ×0.35^17 = 0.0 |
|  | 50¢ | 200 | ×0.35^43 = 0.0 |
|  | 97¢ | 43 | ×0.35^90 = 0.0 |
|  | 98¢ | 1,000 | ×0.35^91 = 0.0 |
| | | **Σ** | **24.3** |

`yours 2.0 / Σ 24.3 = 8.2%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 8.2% = $0.28/day`  

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
19. `tec-cbb-champ-2027-04-05-w-gnzg` ← this one
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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 11 | ×0.2^0 = 11.1 |
|  | 4¢ | 2 | ×0.2^2 = 0.1 |
|  | 2¢ | 232 | ×0.2^4 = 0.4 |
| ▶ | 1¢ | 25,337 (5,000 yours) | ×0.2^5 = 8.1 |
| | | **Σ** | **19.7** |

`yours 1.6 / Σ 19.7 = 8.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.1% = $0.31/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 10 @ 24¢ → $0.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 130 (10 yours) | ×0.2^0 = 130.4 |
|  | 26¢ | 0 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^26 = 0.0 |
|  | 98¢ | 1,821 | ×0.2^74 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^75 = 0.0 |
| | | **Σ** | **130.4** |

`yours 10.0 / Σ 130.4 = 7.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.7% = $0.29/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |
| 2026-07-29 | ~$65.42 | $53.59 | 82% |

Biggest gaps on 2026-07-31: `scc-senate-gop-2026-11-03-48` (est ~$3.79 → got $2.51), `scc-senate-gop-2026-11-03-50` (est ~$3.29 → got $2.17), `apdc-alito-2026-12-31` (est ~$1.38 → got $0.45)

_2026-08-01 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (80,418 resting) | ~32.3% | ~$24.20 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,374 resting) | ~76.6% | ~$19.15 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (26,613 resting) | ~65.5% | ~$16.37 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (74,162 resting) | ~19.0% | ~$14.24 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (79,368 resting) | ~43.9% | ~$10.96 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (194,847 resting) | ~9.5% | ~$7.14 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (83,797 resting) | ~8.7% | ~$6.52 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (180,221 resting) | ~8.2% | ~$6.18 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (308,179 resting) | ~7.0% | ~$5.28 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (92,946 resting) | ~5.6% | ~$4.21 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (96,533 resting) | ~5.6% | ~$4.19 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (112,828 resting) | ~3.3% | ~$2.48 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,373.47 |
| Pending | $140.74 |
| Skipped | $1.21 |
| **Total earned** | **$1,515.42** |

1532 reward rows · 30 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-01 ⚠️ multi-day pending bucket | $52.30 | `█████` |
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
| 2026-08-03 7:48 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 3:51 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 12:00 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-02 9:06 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-02 8:15 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:59 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:15 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 6:13 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 5:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 3:38 PM ET | ✅ ok | 1490 | $1463.12 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
