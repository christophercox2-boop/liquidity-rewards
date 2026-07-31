# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-31 3:18 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$62.18/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$53.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-dem` — BUY at the best price, ~$18.51/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$10.63/day), `enwc-ussep-mn-2026-08-11-dem-angcra` (~$7.76/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$62.18/day (~$2.59/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 85.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (5,500 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `ewc-pres-arg-2027-10-24-javmil` | BUY | 58.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~96.2% of bid side (2,499 resting ≥ 2,000 ✓) ≈ $1.09/day (pool ÷ 11 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | SELL | 3.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~90.7% of ask side (104,533 resting ≥ 2,000 ✓) ≈ $1.13/day (pool ÷ 10 markets) |
| `ewc-ref-fl-tax-2026-11-03-pass` | BUY | 56.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~69.3% of bid side (4,339 resting ≥ 2,000 ✓) ≈ $8.66/day |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 55.0¢ | 42 | 0 | $100.00 | ✅ scoring — ~68.9% of bid side (5,511 resting ≥ 5,000 ✓) ≈ $2.87/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 7.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (11,955 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 80.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (5,525 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 89.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (5,500 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 7.0¢ | 70 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (11,965 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 78.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (5,500 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 10.0¢ | 46 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (12,008 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 25.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~62.5% of ask side (127,664 resting ≥ 2,000 ✓) ≈ $0.78/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~56.1% of ask side (12,048 resting ≥ 5,000 ✓) ≈ $2.16/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 5.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~55.3% of bid side (25,302 resting ≥ 5,000 ✓) ≈ $2.13/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 8.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~55.1% of ask side (11,941 resting ≥ 5,000 ✓) ≈ $2.12/day (pool ÷ 13 markets) |
| `mlaec-swepm-2026-09-13-magand` | BUY | 68.0¢ | 3 | 0 | $25.00 | ✅ scoring — ~54.0% of bid side (6,554 resting ≥ 2,000 ✓) ≈ $1.35/day (pool ÷ 5 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 18.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~51.9% of bid side (5,556 resting ≥ 5,000 ✓) ≈ $2.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 5.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~37.6% of bid side (25,285 resting ≥ 5,000 ✓) ≈ $1.45/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 41.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~33.2% of bid side (5,601 resting ≥ 5,000 ✓) ≈ $1.38/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 9.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~33.0% of bid side (5,582 resting ≥ 5,000 ✓) ≈ $1.38/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 19.0¢ | 47 | 1 | $100.00 | ✅ scoring — ~32.9% of bid side (5,512 resting ≥ 5,000 ✓) ≈ $1.26/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~27.2% of ask side (11,952 resting ≥ 5,000 ✓) ≈ $1.05/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | BUY | 15.0¢ | 7 | 0 | $25.00 | ✅ scoring — ~26.9% of bid side (10,295 resting ≥ 2,000 ✓) ≈ $0.34/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 12.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~26.3% of ask side (11,874 resting ≥ 5,000 ✓) ≈ $1.01/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~18.4% of bid side (25,590 resting ≥ 5,000 ✓) ≈ $0.77/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~18.3% of bid side (25,637 resting ≥ 5,000 ✓) ≈ $0.70/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 4.0¢ | 45 | 0 | $100.00 | ✅ scoring — ~18.2% of bid side (25,311 resting ≥ 5,000 ✓) ≈ $0.70/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 5,000 | 2 | $100.00 | ✅ scoring — ~18.2% of bid side (25,452 resting ≥ 5,000 ✓) ≈ $0.70/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 1.0¢ | 5,000 | 3 | $100.00 | ✅ scoring — ~16.2% of bid side (25,311 resting ≥ 5,000 ✓) ≈ $0.62/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~15.8% of bid side (26,502 resting ≥ 5,000 ✓) ≈ $0.61/day (pool ÷ 13 markets) |
| …and 140 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 50 @ 85¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 69¢ | 128 | ×0.2^16 = 0.0 |
|  | 1¢ | 5,322 | ×0.2^84 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>ewc-pres-arg-2027-10-24-javmil</code> BUY 1 @ 58¢ → $1.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 56¢ | 4 | ×0.1^2 = 0.0 |
|  | 1¢ | 2,494 | ×0.1^57 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 96.2%`  
`$25 ÷ 11 ÷ 2 = $1.14 × 96.2% = $1.09/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> SELL 10 @ 3¢ → $1.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 11 (10 yours) | ×0.1^0 = 11.0 |
|  | 6¢ | 4 | ×0.1^3 = 0.0 |
|  | 7¢ | 72 | ×0.1^4 = 0.0 |
|  | 8¢ | 1,665 | ×0.1^5 = 0.0 |
|  | 15¢ | 55 | ×0.1^12 = 0.0 |
|  | 23¢ | 102 | ×0.1^20 = 0.0 |
|  | 45¢ | 25 | ×0.1^42 = 0.0 |
|  | 98¢ | 102,099 | ×0.1^95 = 0.0 |
| | | **Σ** | **11.0** |

`yours 10.0 / Σ 11.0 = 90.7%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 90.7% = $1.13/day`  

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
<details><summary><code>ewc-ref-fl-tax-2026-11-03-pass</code> BUY 5 @ 56¢ → $8.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 56¢ | 7 (5 yours) | ×0.1^0 = 7.0 |
|  | 55¢ | 2 | ×0.1^1 = 0.2 |
|  | 54¢ | 2 | ×0.1^2 = 0.0 |
|  | 27¢ | 18 | ×0.1^29 = 0.0 |
|  | 5¢ | 4,110 | ×0.1^51 = 0.0 |
| | | **Σ** | **7.2** |

`yours 5.0 / Σ 7.2 = 69.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 69.3% = $8.66/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> BUY 42 @ 55¢ → $2.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 55¢ | 61 (42 yours) | ×0.2^0 = 61.0 |
|  | 1¢ | 5,450 | ×0.2^54 = 0.0 |
| | | **Σ** | **61.0** |

`yours 42.0 / Σ 61.0 = 68.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 68.9% = $2.87/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 50 @ 7¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 75 (50 yours) | ×0.2^0 = 75.0 |
|  | 35¢ | 15 | ×0.2^28 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,764 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
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
11. `scc-senate-gop-2026-11-03-56` ← this one
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 50 @ 80¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 75 (50 yours) | ×0.2^0 = 75.0 |
|  | 1¢ | 5,450 | ×0.2^79 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 50 @ 89¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 75 (50 yours) | ×0.2^0 = 75.0 |
|  | 1¢ | 5,425 | ×0.2^88 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 50 @ 78¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 75 (50 yours) | ×0.2^0 = 75.0 |
|  | 1¢ | 5,425 | ×0.2^77 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 46 @ 10¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 69 (46 yours) | ×0.2^0 = 69.0 |
|  | 20¢ | 50 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,788 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **69.0** |

`yours 46.0 / Σ 69.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 10 @ 25¢ → $0.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 16 (10 yours) | ×0.1^0 = 16.0 |
|  | 29¢ | 6 | ×0.1^4 = 0.0 |
|  | 33¢ | 18 | ×0.1^8 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 50 @ 6¢ → $2.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 79 (50 yours) | ×0.2^0 = 79.0 |
|  | 7¢ | 51 | ×0.2^1 = 10.2 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,798 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **89.2** |

`yours 50.0 / Σ 89.2 = 56.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 56.1% = $2.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 50 @ 5¢ → $2.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 1¢ | 25,252 | ×0.2^4 = 40.4 |
| | | **Σ** | **90.4** |

`yours 50.0 / Σ 90.4 = 55.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.3% = $2.13/day`  

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
<details><summary><code>mlaec-swepm-2026-09-13-magand</code> BUY 3 @ 68¢ → $1.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 68¢ | 3 (3 yours) | ×0.1^0 = 3.0 |
|  | 66¢ | 250 | ×0.1^2 = 2.5 |
|  | 63¢ | 6,000 | ×0.1^5 = 0.1 |
| | | **Σ** | **5.6** |

`yours 3.0 / Σ 5.6 = 54.0%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 54.0% = $1.35/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `mlaec-swepm-2026-09-13-ebbbus`
2. `mlaec-swepm-2026-09-13-jimake`
3. `mlaec-swepm-2026-09-13-magand` ← this one
4. `mlaec-swepm-2026-09-13-noodad`
5. `mlaec-swepm-2026-09-13-ulfkri`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 9 @ 18¢ → $2.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 17 (9 yours) | ×0.2^0 = 17.3 |
|  | 5¢ | 60 | ×0.2^13 = 0.0 |
|  | 1¢ | 5,479 | ×0.2^17 = 0.0 |
| | | **Σ** | **17.3** |

`yours 9.0 / Σ 17.3 = 51.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 51.9% = $2.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 25 @ 5¢ → $1.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 26 (25 yours) | ×0.2^0 = 26.0 |
|  | 1¢ | 25,259 | ×0.2^4 = 40.4 |
| | | **Σ** | **66.4** |

`yours 25.0 / Σ 66.4 = 37.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.6% = $1.45/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 50 @ 41¢ → $1.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 41¢ | 151 (50 yours) | ×0.2^0 = 150.6 |
|  | 1¢ | 5,450 | ×0.2^40 = 0.0 |
| | | **Σ** | **150.6** |

`yours 50.0 / Σ 150.6 = 33.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 33.2% = $1.38/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 10 @ 9¢ → $1.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 29 (10 yours) | ×0.2^0 = 29.4 |
|  | 6¢ | 103 | ×0.2^3 = 0.8 |
|  | 1¢ | 5,450 | ×0.2^8 = 0.0 |
| | | **Σ** | **30.3** |

`yours 10.0 / Σ 30.3 = 33.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 33.0% = $1.38/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 47 @ 19¢ → $1.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 15 | ×0.2^0 = 15.0 |
| ▶ | 19¢ | 68 (47 yours) | ×0.2^1 = 13.6 |
|  | 5¢ | 20 | ×0.2^15 = 0.0 |
|  | 1¢ | 5,409 | ×0.2^19 = 0.0 |
| | | **Σ** | **28.6** |

`yours 9.4 / Σ 28.6 = 32.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.9% = $1.26/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 15 @ 21¢ → $1.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 55 (15 yours) | ×0.2^0 = 55.1 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **55.1** |

`yours 15.0 / Σ 55.1 = 27.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.2% = $1.05/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> BUY 7 @ 15¢ → $0.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 26 (7 yours) | ×0.1^0 = 26.0 |
|  | 11¢ | 6 | ×0.1^4 = 0.0 |
|  | 9¢ | 18 | ×0.1^6 = 0.0 |
|  | 8¢ | 13 | ×0.1^7 = 0.0 |
|  | 1¢ | 10,232 | ×0.1^14 = 0.0 |
| | | **Σ** | **26.0** |

`yours 7.0 / Σ 26.0 = 26.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 26.9% = $0.34/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 10 @ 12¢ → $1.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 12¢ | 13 (10 yours) | ×0.2^2 = 0.5 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **1.5** |

`yours 0.4 / Σ 1.5 = 26.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.3% = $1.01/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 5,000 @ 1¢ → $0.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 390 | ×0.2^0 = 390.0 |
| ▶ | 1¢ | 25,200 (5,000 yours) | ×0.2^1 = 5,040.0 |
| | | **Σ** | **5,430.0** |

`yours 1,000.0 / Σ 5,430.0 = 18.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.4% = $0.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 5,000 @ 1¢ → $0.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 435 | ×0.2^0 = 435.0 |
| ▶ | 1¢ | 25,202 (5,000 yours) | ×0.2^1 = 5,040.4 |
| | | **Σ** | **5,475.4** |

`yours 1,000.0 / Σ 5,475.4 = 18.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.3% = $0.70/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 45 @ 4¢ → $0.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 45 (45 yours) | ×0.2^0 = 45.1 |
|  | 1¢ | 25,266 | ×0.2^3 = 202.1 |
| | | **Σ** | **247.2** |

`yours 45.1 / Σ 247.2 = 18.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.2% = $0.70/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 5,000 @ 1¢ → $0.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 87 | ×0.2^0 = 87.0 |
| ▶ | 1¢ | 25,365 (5,000 yours) | ×0.2^2 = 1,014.6 |
| | | **Σ** | **1,101.6** |

`yours 200.0 / Σ 1,101.6 = 18.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.2% = $0.70/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 5,000 @ 1¢ → $0.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 45 | ×0.2^0 = 45.1 |
| ▶ | 1¢ | 25,266 (5,000 yours) | ×0.2^3 = 202.1 |
| | | **Σ** | **247.2** |

`yours 40.0 / Σ 247.2 = 16.2%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 5,000 @ 1¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1,302 | ×0.2^0 = 1,302.0 |
| ▶ | 1¢ | 25,200 (5,000 yours) | ×0.2^1 = 5,040.0 |
| | | **Σ** | **6,342.0** |

`yours 1,000.0 / Σ 6,342.0 = 15.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 15.8% = $0.61/day`  

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
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (51,789 resting) | ~24.7% | ~$18.51 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (86,018 resting) | ~42.5% | ~$10.63 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (71,682 resting) | ~31.0% | ~$7.76 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (83,711 resting) | ~26.5% | ~$6.64 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (11,839 resting) | ~10.5% | ~$5.25 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (43,810 resting) | ~5.9% | ~$4.46 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $300.00 ÷ 3 | 0.20 | 10,000 | SELL side (34,528 resting) | ~7.9% | ~$3.96 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (43,943 resting) | ~13.6% | ~$3.40 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (268,463 resting) | ~4.2% | ~$3.12 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (162,618 resting) | ~4.1% | ~$3.05 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (8,546 resting) | ~10.5% | ~$2.63 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,004 resting) | ~3.1% | ~$2.35 |

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
| 2026-07-31 3:18 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 11:55 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 10:12 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:57 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:52 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:36 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:14 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 8:17 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 7:45 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 6:29 PM ET | ✅ ok | 1267 | $1321.41 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
