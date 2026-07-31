# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-31 6:00 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$41.09/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$53.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-dem` — BUY at the best price, ~$16.55/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$10.63/day), `enwc-ussep-mn-2026-08-11-dem-angcra` (~$7.52/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$41.09/day (~$1.71/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-lte45` | SELL | 7.0¢ | 70 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (11,965 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 85.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~64.9% of bid side (5,527 resting ≥ 5,000 ✓) ≈ $2.71/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 55.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~63.5% of bid side (5,499 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 25.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~62.5% of ask side (127,664 resting ≥ 2,000 ✓) ≈ $0.78/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | SELL | 3.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~62.4% of ask side (104,384 resting ≥ 2,000 ✓) ≈ $0.78/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 80.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~61.7% of bid side (5,500 resting ≥ 5,000 ✓) ≈ $2.57/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 7.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~58.8% of ask side (11,965 resting ≥ 5,000 ✓) ≈ $2.26/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 89.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~58.1% of bid side (5,511 resting ≥ 5,000 ✓) ≈ $2.42/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~57.1% of ask side (8,763 resting ≥ 5,000 ✓) ≈ $2.38/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 10.0¢ | 46 | 0 | $100.00 | ✅ scoring — ~55.4% of ask side (12,027 resting ≥ 5,000 ✓) ≈ $2.13/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 8.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~55.1% of ask side (11,941 resting ≥ 5,000 ✓) ≈ $2.12/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 78.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~53.8% of bid side (5,518 resting ≥ 5,000 ✓) ≈ $2.24/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 19.0¢ | 47 | 1 | $100.00 | ✅ scoring — ~43.1% of bid side (5,301 resting ≥ 5,000 ✓) ≈ $1.66/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~32.2% of ask side (12,126 resting ≥ 5,000 ✓) ≈ $1.24/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 41.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~26.8% of bid side (5,637 resting ≥ 5,000 ✓) ≈ $1.12/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~25.8% of ask side (11,955 resting ≥ 5,000 ✓) ≈ $0.99/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 25.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~23.8% of ask side (12,060 resting ≥ 5,000 ✓) ≈ $0.92/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 25.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~16.7% of ask side (12,060 resting ≥ 5,000 ✓) ≈ $0.64/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~16.3% of bid side (26,294 resting ≥ 5,000 ✓) ≈ $0.63/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~16.2% of bid side (26,325 resting ≥ 5,000 ✓) ≈ $0.68/day (pool ÷ 12 markets) |
| `mlaec-swepm-2026-09-13-magand` | BUY | 68.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~15.3% of bid side (6,568 resting ≥ 2,000 ✓) ≈ $0.38/day (pool ÷ 5 markets) |
| `ewc-ref-fl-tax-2026-11-03-pass` | BUY | 56.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~13.1% of bid side (4,370 resting ≥ 2,000 ✓) ≈ $1.64/day |
| `scc-senate-gop-2026-11-03-52` | BUY | 18.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~12.3% of bid side (5,612 resting ≥ 5,000 ✓) ≈ $0.47/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 5,000 | 2 | $100.00 | ✅ scoring — ~11.6% of bid side (25,904 resting ≥ 5,000 ✓) ≈ $0.45/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 1.0¢ | 5,000 | 2 | $100.00 | ✅ scoring — ~10.1% of bid side (26,566 resting ≥ 5,000 ✓) ≈ $0.39/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 5.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~9.4% of bid side (25,485 resting ≥ 5,000 ✓) ≈ $0.36/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 4.0¢ | 45 | 0 | $100.00 | ✅ scoring — ~9.1% of bid side (25,561 resting ≥ 5,000 ✓) ≈ $0.35/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~8.8% of bid side (5,768 resting ≥ 5,000 ✓) ≈ $0.34/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 16.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~8.1% of ask side (128,015 resting ≥ 2,000 ✓) ≈ $0.10/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 16.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~8.1% of ask side (128,015 resting ≥ 2,000 ✓) ≈ $0.10/day (pool ÷ 10 markets) |
| …and 140 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 70 @ 7¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 105 (70 yours) | ×0.2^0 = 105.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **105.0** |

`yours 70.0 / Σ 105.0 = 66.7%`  
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 50 @ 85¢ → $2.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 77 (50 yours) | ×0.2^0 = 77.0 |
|  | 69¢ | 128 | ×0.2^16 = 0.0 |
|  | 1¢ | 5,322 | ×0.2^84 = 0.0 |
| | | **Σ** | **77.0** |

`yours 50.0 / Σ 77.0 = 64.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 64.9% = $2.71/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> BUY 31 @ 55¢ → $2.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 55¢ | 49 (31 yours) | ×0.2^0 = 49.2 |
|  | 1¢ | 5,450 | ×0.2^54 = 0.0 |
| | | **Σ** | **49.2** |

`yours 31.2 / Σ 49.2 = 63.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 63.5% = $2.64/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 10 @ 25¢ → $0.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 16 (10 yours) | ×0.1^0 = 16.0 |
|  | 29¢ | 6 | ×0.1^4 = 0.0 |
|  | 30¢ | 18 | ×0.1^5 = 0.0 |
|  | 45¢ | 25 | ×0.1^20 = 0.0 |
|  | 98¢ | 127,099 | ×0.1^73 = 0.0 |
| | | **Σ** | **16.0** |

`yours 10.0 / Σ 16.0 = 62.5%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 62.5% = $0.78/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> SELL 10 @ 3¢ → $0.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 16 (10 yours) | ×0.1^0 = 16.0 |
|  | 7¢ | 24 | ×0.1^4 = 0.0 |
|  | 8¢ | 1,665 | ×0.1^5 = 0.0 |
|  | 15¢ | 55 | ×0.1^12 = 0.0 |
|  | 45¢ | 25 | ×0.1^42 = 0.0 |
|  | 98¢ | 102,099 | ×0.1^95 = 0.0 |
| | | **Σ** | **16.0** |

`yours 10.0 / Σ 16.0 = 62.4%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 62.4% = $0.78/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10` ← this one
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 50 @ 80¢ → $2.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 81 (50 yours) | ×0.2^0 = 81.0 |
|  | 1¢ | 5,419 | ×0.2^79 = 0.0 |
| | | **Σ** | **81.0** |

`yours 50.0 / Σ 81.0 = 61.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 61.7% = $2.57/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 50 @ 7¢ → $2.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 85 (50 yours) | ×0.2^0 = 85.0 |
|  | 35¢ | 15 | ×0.2^28 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,764 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **85.0** |

`yours 50.0 / Σ 85.0 = 58.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 58.8% = $2.26/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 50 @ 89¢ → $2.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 86 (50 yours) | ×0.2^0 = 86.0 |
|  | 1¢ | 5,425 | ×0.2^88 = 0.0 |
| | | **Σ** | **86.0** |

`yours 50.0 / Σ 86.0 = 58.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 58.1% = $2.42/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 20 @ 16¢ → $2.38/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 35 (20 yours) | ×0.2^0 = 35.0 |
|  | 21¢ | 44 | ×0.2^5 = 0.0 |
|  | 50¢ | 25 | ×0.2^34 = 0.0 |
|  | 99¢ | 8,659 | ×0.2^83 = 0.0 |
| | | **Σ** | **35.0** |

`yours 20.0 / Σ 35.0 = 57.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 57.1% = $2.38/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 46 @ 10¢ → $2.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 83 (46 yours) | ×0.2^0 = 83.0 |
|  | 20¢ | 50 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,793 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **83.0** |

`yours 46.0 / Σ 83.0 = 55.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.4% = $2.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 5 @ 8¢ → $2.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 9 (5 yours) | ×0.2^0 = 9.1 |
|  | 40¢ | 29 | ×0.2^32 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,802 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^91 = 0.0 |
| | | **Σ** | **9.1** |

`yours 5.0 / Σ 9.1 = 55.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.1% = $2.12/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 50 @ 78¢ → $2.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 93 (50 yours) | ×0.2^0 = 93.0 |
|  | 1¢ | 5,425 | ×0.2^77 = 0.0 |
| | | **Σ** | **93.0** |

`yours 50.0 / Σ 93.0 = 53.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 53.8% = $2.24/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 47 @ 19¢ → $1.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 7 | ×0.2^0 = 7.0 |
| ▶ | 19¢ | 74 (47 yours) | ×0.2^1 = 14.8 |
|  | 5¢ | 20 | ×0.2^15 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **21.8** |

`yours 9.4 / Σ 21.8 = 43.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.1% = $1.66/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 50 @ 6¢ → $1.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 142 (50 yours) | ×0.2^0 = 142.0 |
|  | 7¢ | 66 | ×0.2^1 = 13.2 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,798 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **155.2** |

`yours 50.0 / Σ 155.2 = 32.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.2% = $1.24/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 50 @ 41¢ → $1.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 41¢ | 187 (50 yours) | ×0.2^0 = 186.6 |
|  | 1¢ | 5,450 | ×0.2^40 = 0.0 |
| | | **Σ** | **186.6** |

`yours 50.0 / Σ 186.6 = 26.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 26.8% = $1.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 15 @ 21¢ → $0.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 58 (15 yours) | ×0.2^0 = 58.1 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **58.1** |

`yours 15.0 / Σ 58.1 = 25.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.8% = $0.99/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 25¢ → $0.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 42 (10 yours) | ×0.2^0 = 42.0 |
|  | 39¢ | 1 | ×0.2^14 = 0.0 |
|  | 40¢ | 105 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^25 = 0.0 |
|  | 98¢ | 1,811 | ×0.2^73 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^74 = 0.0 |
| | | **Σ** | **42.0** |

`yours 10.0 / Σ 42.0 = 23.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 23.8% = $0.92/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 7 @ 25¢ → $0.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 42 (7 yours) | ×0.2^0 = 42.0 |
|  | 39¢ | 1 | ×0.2^14 = 0.0 |
|  | 40¢ | 105 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^25 = 0.0 |
|  | 98¢ | 1,811 | ×0.2^73 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^74 = 0.0 |
| | | **Σ** | **42.0** |

`yours 7.0 / Σ 42.0 = 16.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.7% = $0.64/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 5,000 @ 1¢ → $0.63/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1,092 | ×0.2^0 = 1,092.0 |
| ▶ | 1¢ | 25,202 (5,000 yours) | ×0.2^1 = 5,040.4 |
| | | **Σ** | **6,132.4** |

`yours 1,000.0 / Σ 6,132.4 = 16.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.3% = $0.63/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 5,000 @ 1¢ → $0.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1,125 | ×0.2^0 = 1,125.0 |
| ▶ | 1¢ | 25,200 (5,000 yours) | ×0.2^1 = 5,040.0 |
| | | **Σ** | **6,165.0** |

`yours 1,000.0 / Σ 6,165.0 = 16.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.2% = $0.68/day`  

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
<details><summary><code>mlaec-swepm-2026-09-13-magand</code> BUY 3 @ 68¢ → $0.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 68¢ | 17 (3 yours) | ×0.1^0 = 17.0 |
|  | 66¢ | 250 | ×0.1^2 = 2.5 |
|  | 63¢ | 6,000 | ×0.1^5 = 0.1 |
| | | **Σ** | **19.6** |

`yours 3.0 / Σ 19.6 = 15.3%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 15.3% = $0.38/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `mlaec-swepm-2026-09-13-ebbbus`
2. `mlaec-swepm-2026-09-13-jimake`
3. `mlaec-swepm-2026-09-13-magand` ← this one
4. `mlaec-swepm-2026-09-13-noodad`
5. `mlaec-swepm-2026-09-13-ulfkri`

</details>

</details>
<details><summary><code>ewc-ref-fl-tax-2026-11-03-pass</code> BUY 5 @ 56¢ → $1.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 56¢ | 38 (5 yours) | ×0.1^0 = 38.0 |
|  | 55¢ | 2 | ×0.1^1 = 0.2 |
|  | 54¢ | 2 | ×0.1^2 = 0.0 |
|  | 27¢ | 18 | ×0.1^29 = 0.0 |
|  | 5¢ | 4,110 | ×0.1^51 = 0.0 |
| | | **Σ** | **38.2** |

`yours 5.0 / Σ 38.2 = 13.1%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 13.1% = $1.64/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 9 @ 18¢ → $0.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 73 (9 yours) | ×0.2^0 = 73.3 |
|  | 5¢ | 60 | ×0.2^13 = 0.0 |
|  | 1¢ | 5,479 | ×0.2^17 = 0.0 |
| | | **Σ** | **73.3** |

`yours 9.0 / Σ 73.3 = 12.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 12.3% = $0.47/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 5,000 @ 1¢ → $0.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 714 | ×0.2^0 = 714.0 |
| ▶ | 1¢ | 25,190 (5,000 yours) | ×0.2^2 = 1,007.6 |
| | | **Σ** | **1,721.6** |

`yours 200.0 / Σ 1,721.6 = 11.6%`  
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
9. `scc-senate-gop-2026-11-03-54`
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56` ← this one
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 5,000 @ 1¢ → $0.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 866 | ×0.2^0 = 866.0 |
|  | 2¢ | 500 | ×0.2^1 = 100.0 |
| ▶ | 1¢ | 25,200 (5,000 yours) | ×0.2^2 = 1,008.0 |
| | | **Σ** | **1,974.0** |

`yours 200.0 / Σ 1,974.0 = 10.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 10.1% = $0.39/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 25 @ 5¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 226 (25 yours) | ×0.2^0 = 226.0 |
|  | 1¢ | 25,259 | ×0.2^4 = 40.4 |
| | | **Σ** | **266.4** |

`yours 25.0 / Σ 266.4 = 9.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.4% = $0.36/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 45 @ 4¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 295 (45 yours) | ×0.2^0 = 295.1 |
|  | 1¢ | 25,266 | ×0.2^3 = 202.1 |
| | | **Σ** | **497.2** |

`yours 45.1 / Σ 497.2 = 9.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.1% = $0.35/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 50 @ 20¢ → $0.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 568 (50 yours) | ×0.2^0 = 568.2 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **568.3** |

`yours 50.0 / Σ 568.3 = 8.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.8% = $0.34/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 1 @ 16¢ → $0.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 12 (1 yours) | ×0.1^0 = 12.4 |
|  | 19¢ | 1 | ×0.1^3 = 0.0 |
|  | 22¢ | 6 | ×0.1^6 = 0.0 |
|  | 24¢ | 17 | ×0.1^8 = 0.0 |
|  | 39¢ | 107 | ×0.1^23 = 0.0 |
|  | 40¢ | 31 | ×0.1^24 = 0.0 |
|  | 45¢ | 25 | ×0.1^29 = 0.0 |
|  | 98¢ | 127,315 | ×0.1^82 = 0.0 |
| | | **Σ** | **12.4** |

`yours 1.0 / Σ 12.4 = 8.1%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 8.1% = $0.10/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10` ← this one
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 1 @ 16¢ → $0.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 12 (1 yours) | ×0.1^0 = 12.4 |
|  | 19¢ | 1 | ×0.1^3 = 0.0 |
|  | 22¢ | 6 | ×0.1^6 = 0.0 |
|  | 24¢ | 17 | ×0.1^8 = 0.0 |
|  | 39¢ | 107 | ×0.1^23 = 0.0 |
|  | 40¢ | 31 | ×0.1^24 = 0.0 |
|  | 45¢ | 25 | ×0.1^29 = 0.0 |
|  | 98¢ | 127,315 | ×0.1^82 = 0.0 |
| | | **Σ** | **12.4** |

`yours 1.0 / Σ 12.4 = 8.1%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 8.1% = $0.10/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10` ← this one
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-28 | ~$148.78 | $79.65 | 54% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |
| 2026-07-26 | ~$159.09 | $153.80 | 97% |

Biggest gaps on 2026-07-28: `enwc-ussep-mi-2026-08-04-dem-abdels` (est ~$18.10 → got $9.25), `lawec-saveact-2026-12-31` (est ~$9.15 → got $1.86), `apdc-jerpowgov-2026-12-31` (est ~$3.09 → got $0.00)

_2026-07-29 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,386 resting) | ~22.1% | ~$16.55 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (86,018 resting) | ~42.5% | ~$10.63 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (68,703 resting) | ~30.1% | ~$7.52 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (72,941 resting) | ~9.6% | ~$7.16 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (83,711 resting) | ~26.5% | ~$6.64 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (77,043 resting) | ~6.6% | ~$4.97 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (88,118 resting) | ~6.4% | ~$4.81 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (322,154 resting) | ~6.8% | ~$3.41 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (300,758 resting) | ~3.9% | ~$2.91 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (13,434 resting) | ~5.7% | ~$2.86 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (78,223 resting) | ~3.8% | ~$2.85 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (178,476 resting) | ~3.7% | ~$2.77 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,240.74 |
| Pending | $132.73 |
| Skipped | $1.21 |
| **Total earned** | **$1,374.68** |

1406 reward rows · 27 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-29 ⚠️ multi-day pending bucket | $53.59 | `█████` |
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
| 2026-07-31 6:00 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 3:18 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 11:55 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 10:12 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:57 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:52 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:36 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:14 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 8:17 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 7:45 PM ET | ✅ ok | 1267 | $1321.41 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
