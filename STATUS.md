# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-01 7:36 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$53.12/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-dem` — BUY at the best price, ~$16.95/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-12-31` (~$8.70/day), `apdc-jerpowgov-2026-08-31` (~$7.96/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$53.12/day (~$2.21/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 22.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~97.9% of bid side (5,288 resting ≥ 5,000 ✓) ≈ $4.08/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 34.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~97.2% of bid side (6,305 resting ≥ 2,000 ✓) ≈ $1.22/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~94.3% of ask side (11,970 resting ≥ 5,000 ✓) ≈ $3.63/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 42.0¢ | 53 | 0 | $100.00 | ✅ scoring — ~93.0% of ask side (5,732 resting ≥ 5,000 ✓) ≈ $3.87/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 36.0¢ | 50 | 2 | $100.00 | ✅ scoring — ~68.3% of ask side (12,073 resting ≥ 5,000 ✓) ≈ $2.63/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (11,870 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 27.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~66.7% of ask side (127,928 resting ≥ 2,000 ✓) ≈ $0.83/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~64.9% of ask side (11,933 resting ≥ 5,000 ✓) ≈ $2.50/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 32.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~57.5% of ask side (11,382 resting ≥ 5,000 ✓) ≈ $2.21/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 10.0¢ | 46 | 0 | $100.00 | ✅ scoring — ~56.1% of ask side (11,951 resting ≥ 5,000 ✓) ≈ $2.16/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~55.9% of bid side (5,950 resting ≥ 5,000 ✓) ≈ $2.33/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 7.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~55.6% of ask side (9,068 resting ≥ 5,000 ✓) ≈ $2.31/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 90.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~54.3% of bid side (5,538 resting ≥ 5,000 ✓) ≈ $2.26/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 77.0¢ | 49 | 0 | $100.00 | ✅ scoring — ~53.0% of ask side (5,322 resting ≥ 5,000 ✓) ≈ $2.21/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 7.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~50.1% of ask side (119,369 resting ≥ 2,000 ✓) ≈ $0.63/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 70.0¢ | 33 | 0 | $100.00 | ✅ scoring — ~49.8% of ask side (8,674 resting ≥ 5,000 ✓) ≈ $2.08/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~48.7% of ask side (12,125 resting ≥ 5,000 ✓) ≈ $1.87/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 22.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~46.5% of bid side (5,502 resting ≥ 5,000 ✓) ≈ $1.79/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 11.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~43.3% of ask side (11,971 resting ≥ 5,000 ✓) ≈ $1.66/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~40.2% of ask side (12,214 resting ≥ 5,000 ✓) ≈ $1.55/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~37.0% of bid side (5,517 resting ≥ 5,000 ✓) ≈ $1.42/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~22.1% of ask side (12,125 resting ≥ 5,000 ✓) ≈ $0.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 9.0¢ | 49 | 0 | $100.00 | ✅ scoring — ~18.6% of bid side (5,545 resting ≥ 5,000 ✓) ≈ $0.71/day (pool ÷ 13 markets) |
| `ewc-pres-arg-2027-10-24-javmil` | BUY | 62.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~17.9% of bid side (2,506 resting ≥ 2,000 ✓) ≈ $0.20/day (pool ÷ 11 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 62.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~16.6% of ask side (7,228 resting ≥ 5,000 ✓) ≈ $0.69/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | BUY | 17.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~16.0% of bid side (5,625 resting ≥ 5,000 ✓) ≈ $2.67/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 6.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~14.0% of ask side (11,977 resting ≥ 5,000 ✓) ≈ $0.54/day (pool ÷ 13 markets) |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | SELL | 6.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~10.6% of ask side (4,470 resting ≥ 2,000 ✓) ≈ $0.66/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 30 | 1 | $100.00 | ✅ scoring — ~5.6% of ask side (6,199 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 90.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~4.3% of bid side (5,538 resting ≥ 5,000 ✓) ≈ $0.18/day (pool ÷ 12 markets) |
| …and 156 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 10 @ 22¢ → $4.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 19¢ | 5 | ×0.2^3 = 0.0 |
|  | 18¢ | 101 | ×0.2^4 = 0.2 |
|  | 17¢ | 50 | ×0.2^5 = 0.0 |
|  | 1¢ | 5,122 | ×0.2^21 = 0.0 |
| | | **Σ** | **10.2** |

`yours 10.0 / Σ 10.2 = 97.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 97.9% = $4.08/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 35 @ 34¢ → $1.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 36 (35 yours) | ×0.1^0 = 36.0 |
|  | 13¢ | 6 | ×0.1^21 = 0.0 |
|  | 10¢ | 18 | ×0.1^24 = 0.0 |
|  | 8¢ | 869 | ×0.1^26 = 0.0 |
|  | 2¢ | 375 | ×0.1^32 = 0.0 |
|  | 1¢ | 5,001 | ×0.1^33 = 0.0 |
| | | **Σ** | **36.0** |

`yours 35.0 / Σ 36.0 = 97.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 97.2% = $1.22/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20` ← this one
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 50 @ 21¢ → $3.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 53 (50 yours) | ×0.2^0 = 53.0 |
|  | 28¢ | 20 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **53.0** |

`yours 50.0 / Σ 53.0 = 94.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 94.3% = $3.63/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 53 @ 42¢ → $3.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 57 (53 yours) | ×0.2^0 = 57.0 |
|  | 52¢ | 1 | ×0.2^10 = 0.0 |
|  | 58¢ | 11 | ×0.2^16 = 0.0 |
|  | 69¢ | 100 | ×0.2^27 = 0.0 |
|  | 99¢ | 5,563 | ×0.2^57 = 0.0 |
| | | **Σ** | **57.0** |

`yours 53.0 / Σ 57.0 = 93.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 93.0% = $3.87/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 50 @ 36¢ → $2.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 34¢ | 1 | ×0.2^0 = 0.9 |
| ▶ | 36¢ | 50 (50 yours) | ×0.2^2 = 2.0 |
|  | 40¢ | 105 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^16 = 0.0 |
|  | 98¢ | 1,816 | ×0.2^64 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^65 = 0.0 |
| | | **Σ** | **2.9** |

`yours 2.0 / Σ 2.9 = 68.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.3% = $2.63/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 10 @ 8¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^91 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> SELL 20 @ 27¢ → $0.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 30 (20 yours) | ×0.1^0 = 30.0 |
|  | 33¢ | 16 | ×0.1^6 = 0.0 |
|  | 35¢ | 18 | ×0.1^8 = 0.0 |
|  | 45¢ | 81 | ×0.1^18 = 0.0 |
|  | 98¢ | 127,283 | ×0.1^71 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 66.7% = $0.83/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15` ← this one
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 50 @ 15¢ → $2.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 77 (50 yours) | ×0.2^0 = 77.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,755 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **77.0** |

`yours 50.0 / Σ 77.0 = 64.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.9% = $2.50/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 32¢ → $2.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 73 (43 yours) | ×0.2^0 = 73.0 |
|  | 34¢ | 43 | ×0.2^2 = 1.7 |
|  | 38¢ | 128 | ×0.2^6 = 0.0 |
|  | 50¢ | 137 | ×0.2^18 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^66 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^67 = 0.0 |
| | | **Σ** | **74.7** |

`yours 43.0 / Σ 74.7 = 57.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 57.5% = $2.21/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 46 @ 10¢ → $2.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 82 (46 yours) | ×0.2^0 = 82.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,768 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **82.0** |

`yours 46.0 / Σ 82.0 = 56.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 56.1% = $2.16/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 5,000 @ 1¢ → $2.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 750 | ×0.2^0 = 750.0 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^1 = 1,040.0 |
| | | **Σ** | **1,790.0** |

`yours 1,000.0 / Σ 1,790.0 = 55.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 55.9% = $2.33/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 7¢ → $2.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 90 (50 yours) | ×0.2^0 = 90.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 15¢ | 15 | ×0.2^8 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 99¢ | 8,937 | ×0.2^92 = 0.0 |
| | | **Σ** | **90.0** |

`yours 50.0 / Σ 90.0 = 55.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 55.6% = $2.31/day`  

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
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 50 @ 90¢ → $2.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 92 (50 yours) | ×0.2^0 = 92.0 |
|  | 1¢ | 5,446 | ×0.2^89 = 0.0 |
| | | **Σ** | **92.0** |

`yours 50.0 / Σ 92.0 = 54.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 54.3% = $2.26/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 49 @ 77¢ → $2.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 92 (49 yours) | ×0.2^0 = 92.0 |
|  | 80¢ | 50 | ×0.2^3 = 0.4 |
|  | 98¢ | 127 | ×0.2^21 = 0.0 |
|  | 99¢ | 5,053 | ×0.2^22 = 0.0 |
| | | **Σ** | **92.4** |

`yours 49.0 / Σ 92.4 = 53.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 53.0% = $2.21/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 40 @ 7¢ → $0.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 63 (40 yours) | ×0.1^0 = 63.0 |
|  | 9¢ | 24 | ×0.1^2 = 0.2 |
|  | 10¢ | 16,556 | ×0.1^3 = 16.6 |
| | | **Σ** | **79.8** |

`yours 40.0 / Σ 79.8 = 50.1%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 50.1% = $0.63/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5` ← this one
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 33 @ 70¢ → $2.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 70¢ | 66 (33 yours) | ×0.2^0 = 66.0 |
|  | 74¢ | 100 | ×0.2^4 = 0.2 |
|  | 75¢ | 202 | ×0.2^5 = 0.1 |
|  | 77¢ | 1,100 | ×0.2^7 = 0.0 |
|  | 79¢ | 1,865 | ×0.2^9 = 0.0 |
|  | 87¢ | 168 | ×0.2^17 = 0.0 |
|  | 90¢ | 1 | ×0.2^20 = 0.0 |
|  | 99¢ | 5,172 | ×0.2^29 = 0.0 |
| | | **Σ** | **66.2** |

`yours 33.0 / Σ 66.2 = 49.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.8% = $2.08/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 22 @ 20¢ → $1.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 45 (22 yours) | ×0.2^0 = 45.0 |
|  | 24¢ | 100 | ×0.2^4 = 0.2 |
|  | 39¢ | 40 | ×0.2^19 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,839 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **45.2** |

`yours 22.0 / Σ 45.2 = 48.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.7% = $1.87/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 100 @ 22¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 22¢ | 205 (100 yours) | ×0.2^1 = 41.0 |
|  | 1¢ | 5,295 | ×0.2^22 = 0.0 |
| | | **Σ** | **43.0** |

`yours 20.0 / Σ 43.0 = 46.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 46.5% = $1.79/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 11¢ → $1.66/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 45 (20 yours) | ×0.2^0 = 45.0 |
|  | 13¢ | 30 | ×0.2^2 = 1.2 |
|  | 15¢ | 10 | ×0.2^4 = 0.0 |
|  | 16¢ | 15 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^39 = 0.0 |
|  | 98¢ | 1,770 | ×0.2^87 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^88 = 0.0 |
| | | **Σ** | **46.2** |

`yours 20.0 / Σ 46.2 = 43.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.3% = $1.66/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 10¢ → $1.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 124 (50 yours) | ×0.2^0 = 124.2 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **124.2** |

`yours 50.0 / Σ 124.2 = 40.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.2% = $1.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 10 @ 29¢ → $1.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 27 (10 yours) | ×0.2^0 = 27.0 |
|  | 1¢ | 5,490 | ×0.2^28 = 0.0 |
| | | **Σ** | **27.0** |

`yours 10.0 / Σ 27.0 = 37.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.0% = $1.42/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 10 @ 20¢ → $0.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 45 (10 yours) | ×0.2^0 = 45.0 |
|  | 24¢ | 100 | ×0.2^4 = 0.2 |
|  | 39¢ | 40 | ×0.2^19 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,839 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **45.2** |

`yours 10.0 / Σ 45.2 = 22.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 22.1% = $0.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 49 @ 9¢ → $0.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 264 (49 yours) | ×0.2^0 = 264.0 |
|  | 2¢ | 81 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^8 = 0.0 |
| | | **Σ** | **264.0** |

`yours 49.0 / Σ 264.0 = 18.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.6% = $0.71/day`  

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
<details><summary><code>ewc-pres-arg-2027-10-24-javmil</code> BUY 1 @ 62¢ → $0.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 62¢ | 7 (1 yours) | ×0.1^0 = 7.3 |
|  | 59¢ | 1 | ×0.1^3 = 0.0 |
|  | 56¢ | 4 | ×0.1^6 = 0.0 |
|  | 1¢ | 2,494 | ×0.1^61 = 0.0 |
| | | **Σ** | **7.3** |

`yours 1.3 / Σ 7.3 = 17.9%`  
`$25 ÷ 11 ÷ 2 = $1.14 × 17.9% = $0.20/day`  

<details><summary>÷ 11 markets in this race — tap to list</summary>

1. `ewc-pres-arg-2027-10-24-axekic`
2. `ewc-pres-arg-2027-10-24-dangeb`
3. `ewc-pres-arg-2027-10-24-estbul`
4. `ewc-pres-arg-2027-10-24-facman`
5. `ewc-pres-arg-2027-10-24-javmil` ← this one
6. `ewc-pres-arg-2027-10-24-juagra`
7. `ewc-pres-arg-2027-10-24-juasch`
8. `ewc-pres-arg-2027-10-24-maumac`
9. `ewc-pres-arg-2027-10-24-myrbre`
10. `ewc-pres-arg-2027-10-24-sermas`
11. `ewc-pres-arg-2027-10-24-vicvil`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 30 @ 62¢ → $0.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 62¢ | 181 (30 yours) | ×0.2^0 = 180.7 |
|  | 83¢ | 103 | ×0.2^21 = 0.0 |
|  | 99¢ | 6,944 | ×0.2^37 = 0.0 |
| | | **Σ** | **180.7** |

`yours 30.0 / Σ 180.7 = 16.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.6% = $0.69/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 100 @ 17¢ → $2.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 425 (100 yours) | ×0.2^0 = 424.8 |
|  | 15¢ | 5,000 | ×0.2^2 = 200.0 |
| | | **Σ** | **624.8** |

`yours 100.0 / Σ 624.8 = 16.0%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 16.0% = $2.67/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-alito-2026-07-31`
2. `apdc-alito-2026-08-31`
3. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 50 @ 6¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 61 | ×0.2^0 = 61.2 |
| ▶ | 6¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 98¢ | 1,765 | ×0.2^93 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^94 = 0.0 |
| | | **Σ** | **71.2** |

`yours 10.0 / Σ 71.2 = 14.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.0% = $0.54/day`  

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
<details><summary><code>enwc-ussep-nh-2026-09-01-rep-scobro</code> SELL 50 @ 6¢ → $0.66/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 440 (50 yours) | ×0.1^0 = 440.2 |
|  | 8¢ | 3,030 | ×0.1^2 = 30.3 |
| | | **Σ** | **470.5** |

`yours 50.0 / Σ 470.5 = 10.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 10.6% = $0.66/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-nh-2026-09-01-rep-johsun`
2. `enwc-ussep-nh-2026-09-01-rep-scobro` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 30 @ 7¢ → $0.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 101 | ×0.2^0 = 100.8 |
| ▶ | 7¢ | 30 (30 yours) | ×0.2^1 = 6.0 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 50¢ | 25 | ×0.2^44 = 0.0 |
|  | 99¢ | 6,042 | ×0.2^93 = 0.0 |
| | | **Σ** | **106.8** |

`yours 6.0 / Σ 106.8 = 5.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.6% = $0.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 4 @ 90¢ → $0.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 92 (4 yours) | ×0.2^0 = 92.0 |
|  | 1¢ | 5,446 | ×0.2^89 = 0.0 |
| | | **Σ** | **92.0** |

`yours 4.0 / Σ 92.0 = 4.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.3% = $0.18/day`  

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

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-29 | ~$65.42 | $53.59 | 82% |
| 2026-07-28 | ~$148.78 | $79.65 | 54% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |

Biggest gaps on 2026-07-29: `apdc-petehegseth-2026-12-31` (est ~$12.90 → got $1.16), `scc-senate-gop-2026-11-03-51` (est ~$3.25 → got $0.00), `scc-senate-gop-2026-11-03-54` (est ~$2.11 → got $0.02)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (90,760 resting) | ~22.6% | ~$16.95 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (8,562 resting) | ~52.2% | ~$8.70 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (8,749 resting) | ~47.8% | ~$7.96 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (63,115 resting) | ~23.9% | ~$5.96 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (73,880 resting) | ~6.6% | ~$4.95 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (74,247 resting) | ~16.6% | ~$4.15 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (147,711 resting) | ~5.0% | ~$3.78 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (10,135 resting) | ~14.9% | ~$3.72 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (94,505 resting) | ~4.9% | ~$3.69 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (20,948 resting) | ~6.3% | ~$3.15 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (78,391 resting) | ~2.7% | ~$2.02 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (207,406 resting) | ~2.2% | ~$1.65 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,373.47 |
| Skipped | $1.21 |
| **Total earned** | **$1,374.68** |

1406 reward rows · 27 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
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
| 2026-07-18 | $44.41 | `████` |
| 2026-07-17 | $14.71 | `█` |
| 2026-07-16 | $17.02 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,374.68 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.26 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.82 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.47 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.25 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.73 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.96 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-01 7:36 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 6:43 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 5:25 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 2:43 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 11:55 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 11:25 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 10:44 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 10:39 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 10:26 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 10:12 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
