# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-31 8:20 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$85.38/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$53.59** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-dem` — BUY at the best price, ~$18.73/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-angcra` (~$10.75/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$10.58/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$85.38/day (~$3.56/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 80.0¢ | 150 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (5,683 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 15.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (12,101 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~98.0% of ask side (12,093 resting ≥ 5,000 ✓) ≈ $3.77/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 6.0¢ | 55 | 0 | $100.00 | ✅ scoring — ~97.0% of bid side (5,321 resting ≥ 5,000 ✓) ≈ $3.73/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 10.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~96.8% of ask side (11,904 resting ≥ 5,000 ✓) ≈ $3.72/day (pool ÷ 13 markets) |
| `ewc-pres-arg-2027-10-24-javmil` | BUY | 58.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~96.2% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $1.09/day (pool ÷ 11 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 8.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~90.9% of ask side (5,165 resting ≥ 5,000 ✓) ≈ $3.79/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 15.0¢ | 9 | 0 | $25.00 | ✅ scoring — ~89.5% of ask side (127,963 resting ≥ 2,000 ✓) ≈ $1.12/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 10.0¢ | 46 | 0 | $100.00 | ✅ scoring — ~80.7% of ask side (12,001 resting ≥ 5,000 ✓) ≈ $3.10/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~80.6% of ask side (12,152 resting ≥ 5,000 ✓) ≈ $3.10/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 9.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~71.2% of ask side (7,666 resting ≥ 5,000 ✓) ≈ $2.97/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 22.0¢ | 44 | 0 | $100.00 | ✅ scoring — ~68.7% of bid side (5,493 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 7.0¢ | 70 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (11,965 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 14.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (8,684 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 58.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~65.2% of ask side (5,436 resting ≥ 5,000 ✓) ≈ $2.72/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 85.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~64.9% of bid side (5,527 resting ≥ 5,000 ✓) ≈ $2.71/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 55.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~63.5% of bid side (5,499 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 80.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~59.5% of bid side (5,534 resting ≥ 5,000 ✓) ≈ $2.48/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 7.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~58.8% of ask side (11,965 resting ≥ 5,000 ✓) ≈ $2.26/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 89.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~58.1% of bid side (5,511 resting ≥ 5,000 ✓) ≈ $2.42/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 43.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~57.5% of ask side (11,272 resting ≥ 5,000 ✓) ≈ $2.21/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 38.0¢ | 42 | 0 | $100.00 | ✅ scoring — ~55.7% of bid side (5,309 resting ≥ 5,000 ✓) ≈ $2.14/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 25.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~55.6% of ask side (12,073 resting ≥ 5,000 ✓) ≈ $2.14/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~55.6% of ask side (12,008 resting ≥ 5,000 ✓) ≈ $2.14/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~52.0% of ask side (8,615 resting ≥ 5,000 ✓) ≈ $2.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~45.5% of ask side (11,882 resting ≥ 5,000 ✓) ≈ $1.75/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 42 | 0 | $100.00 | ✅ scoring — ~42.4% of ask side (11,996 resting ≥ 5,000 ✓) ≈ $1.63/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~36.7% of bid side (13,613 resting ≥ 2,000 ✓) ≈ $0.46/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 18.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~30.7% of bid side (5,568 resting ≥ 5,000 ✓) ≈ $1.18/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 41.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~26.8% of bid side (5,637 resting ≥ 5,000 ✓) ≈ $1.12/day (pool ÷ 12 markets) |
| …and 149 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 150 @ 80¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 150 (150 yours) | ×0.2^0 = 150.0 |
|  | 52¢ | 83 | ×0.2^28 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^79 = 0.0 |
| | | **Σ** | **150.0** |

`yours 150.0 / Σ 150.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 100 @ 15¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 100 (100 yours) | ×0.2^0 = 100.0 |
|  | 21¢ | 44 | ×0.2^6 = 0.0 |
|  | 40¢ | 29 | ×0.2^25 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,827 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **100.0** |

`yours 100.0 / Σ 100.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 10¢ → $3.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 51 (50 yours) | ×0.2^0 = 51.0 |
|  | 16¢ | 3 | ×0.2^6 = 0.0 |
|  | 18¢ | 101 | ×0.2^8 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,837 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **51.0** |

`yours 50.0 / Σ 51.0 = 98.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.0% = $3.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 55 @ 6¢ → $3.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 55 (55 yours) | ×0.2^0 = 55.1 |
|  | 1¢ | 5,266 | ×0.2^5 = 1.7 |
| | | **Σ** | **56.8** |

`yours 55.1 / Σ 56.8 = 97.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 97.0% = $3.73/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 30 @ 10¢ → $3.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 31 (30 yours) | ×0.2^0 = 31.0 |
|  | 17¢ | 15 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,757 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **31.0** |

`yours 30.0 / Σ 31.0 = 96.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 96.8% = $3.72/day`  

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
<details><summary><code>ewc-pres-arg-2027-10-24-javmil</code> BUY 1 @ 58¢ → $1.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 56¢ | 4 | ×0.1^2 = 0.0 |
|  | 1¢ | 2,495 | ×0.1^57 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 100 @ 8¢ → $3.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 110 (100 yours) | ×0.2^0 = 110.0 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 25 | ×0.2^42 = 0.0 |
|  | 99¢ | 5,029 | ×0.2^91 = 0.0 |
| | | **Σ** | **110.0** |

`yours 100.0 / Σ 110.0 = 90.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 90.9% = $3.79/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 9 @ 15¢ → $1.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 9 (9 yours) | ×0.1^0 = 9.0 |
|  | 16¢ | 10 | ×0.1^1 = 1.0 |
|  | 17¢ | 1 | ×0.1^2 = 0.0 |
|  | 20¢ | 17 | ×0.1^5 = 0.0 |
|  | 21¢ | 13 | ×0.1^6 = 0.0 |
|  | 24¢ | 41 | ×0.1^9 = 0.0 |
|  | 40¢ | 31 | ×0.1^25 = 0.0 |
|  | 45¢ | 25 | ×0.1^30 = 0.0 |
|  | 98¢ | 127,315 | ×0.1^83 = 0.0 |
| | | **Σ** | **10.1** |

`yours 9.0 / Σ 10.1 = 89.5%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 89.5% = $1.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 46 @ 10¢ → $3.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 57 (46 yours) | ×0.2^0 = 57.0 |
|  | 20¢ | 50 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,793 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **57.0** |

`yours 46.0 / Σ 57.0 = 80.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 80.7% = $3.10/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 10¢ → $3.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 62 (50 yours) | ×0.2^0 = 62.0 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **62.0** |

`yours 50.0 / Σ 62.0 = 80.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 80.6% = $3.10/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 9¢ → $2.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 60 (50 yours) | ×0.2^0 = 60.0 |
|  | 10¢ | 51 | ×0.2^1 = 10.2 |
|  | 50¢ | 25 | ×0.2^41 = 0.0 |
|  | 99¢ | 7,530 | ×0.2^90 = 0.0 |
| | | **Σ** | **70.2** |

`yours 50.0 / Σ 70.2 = 71.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 71.2% = $2.97/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 44 @ 22¢ → $2.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 64 (44 yours) | ×0.2^0 = 64.0 |
|  | 5¢ | 20 | ×0.2^17 = 0.0 |
|  | 1¢ | 5,409 | ×0.2^21 = 0.0 |
| | | **Σ** | **64.0** |

`yours 44.0 / Σ 64.0 = 68.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.7% = $2.64/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 20 @ 14¢ → $2.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 50¢ | 25 | ×0.2^36 = 0.0 |
|  | 99¢ | 8,629 | ×0.2^85 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 30 @ 58¢ → $2.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 46 (30 yours) | ×0.2^0 = 46.0 |
|  | 99¢ | 5,390 | ×0.2^41 = 0.0 |
| | | **Σ** | **46.0** |

`yours 30.0 / Σ 46.0 = 65.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 65.2% = $2.72/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 50 @ 80¢ → $2.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 84 (50 yours) | ×0.2^0 = 84.0 |
|  | 1¢ | 5,450 | ×0.2^79 = 0.0 |
| | | **Σ** | **84.0** |

`yours 50.0 / Σ 84.0 = 59.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 59.5% = $2.48/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 50 @ 43¢ → $2.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 67 (50 yours) | ×0.2^0 = 67.0 |
|  | 44¢ | 100 | ×0.2^1 = 20.0 |
|  | 50¢ | 100 | ×0.2^7 = 0.0 |
|  | 54¢ | 2 | ×0.2^11 = 0.0 |
|  | 55¢ | 2 | ×0.2^12 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^55 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^56 = 0.0 |
| | | **Σ** | **87.0** |

`yours 50.0 / Σ 87.0 = 57.5%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 42 @ 38¢ → $2.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 68 (42 yours) | ×0.2^0 = 68.0 |
|  | 37¢ | 37 | ×0.2^1 = 7.4 |
|  | 34¢ | 2 | ×0.2^4 = 0.0 |
|  | 33¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^37 = 0.0 |
| | | **Σ** | **75.4** |

`yours 42.0 / Σ 75.4 = 55.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.7% = $2.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 40 @ 25¢ → $2.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 72 (40 yours) | ×0.2^0 = 72.0 |
|  | 38¢ | 1 | ×0.2^13 = 0.0 |
|  | 40¢ | 105 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^25 = 0.0 |
|  | 98¢ | 1,794 | ×0.2^73 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^74 = 0.0 |
| | | **Σ** | **72.0** |

`yours 40.0 / Σ 72.0 = 55.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.6% = $2.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 50 @ 6¢ → $2.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 90 (50 yours) | ×0.2^0 = 90.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,798 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **90.0** |

`yours 50.0 / Σ 90.0 = 55.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.6% = $2.14/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 18¢ → $2.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 19 (10 yours) | ×0.2^0 = 19.0 |
|  | 20¢ | 6 | ×0.2^2 = 0.2 |
|  | 50¢ | 50 | ×0.2^32 = 0.0 |
|  | 99¢ | 8,540 | ×0.2^81 = 0.0 |
| | | **Σ** | **19.2** |

`yours 10.0 / Σ 19.2 = 52.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 52.0% = $2.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 10 @ 10¢ → $1.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 22 (10 yours) | ×0.2^0 = 22.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **22.0** |

`yours 10.0 / Σ 22.0 = 45.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 45.5% = $1.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 42 @ 21¢ → $1.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 99 (42 yours) | ×0.2^0 = 99.2 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **99.2** |

`yours 42.0 / Σ 99.2 = 42.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 42.4% = $1.63/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 5,000 @ 1¢ → $0.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 13,613 (5,000 yours) | ×0.1^0 = 13,613.0 |
| | | **Σ** | **13,613.0** |

`yours 5,000.0 / Σ 13,613.0 = 36.7%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 36.7% = $0.46/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 9 @ 18¢ → $1.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 29 (9 yours) | ×0.2^0 = 29.3 |
|  | 5¢ | 60 | ×0.2^13 = 0.0 |
|  | 1¢ | 5,479 | ×0.2^17 = 0.0 |
| | | **Σ** | **29.3** |

`yours 9.0 / Σ 29.3 = 30.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.7% = $1.18/day`  

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
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (81,886 resting) | ~25.0% | ~$18.73 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (58,738 resting) | ~43.0% | ~$10.75 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (86,018 resting) | ~42.3% | ~$10.58 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (345,060 resting) | ~17.8% | ~$8.88 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (83,711 resting) | ~26.5% | ~$6.64 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (119,616 resting) | ~7.1% | ~$5.31 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (85,044 resting) | ~4.7% | ~$3.51 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (75,384 resting) | ~4.4% | ~$3.31 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (74,067 resting) | ~12.7% | ~$3.17 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (79,783 resting) | ~3.5% | ~$2.60 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (180,608 resting) | ~2.7% | ~$1.99 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (322,108 resting) | ~2.2% | ~$1.66 |

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
| 2026-07-31 8:20 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 8:11 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 6:00 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 3:18 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 11:55 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 10:12 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:57 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:52 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:36 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:14 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
