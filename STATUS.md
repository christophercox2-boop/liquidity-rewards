# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-30 9:57 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$92.95/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$10.64/day for 200 contracts. Runners-up: `ewc-usse-tx-2026-11-03-rep` (~$7.58/day), `ewc-usgub-ga-2026-11-03-dem` (~$7.16/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$92.95/day (~$3.87/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `gsc-usfedgvmt-by-2026-10-01` | SELL | 60.0¢ | 6 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,560 resting ≥ 2,000 ✓) ≈ $12.49/day |
| `nocc-attgen-todblanche-2026-08-07` | SELL | 20.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~87.6% of ask side (8,607 resting ≥ 2,000 ✓) ≈ $10.95/day |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 38.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~83.3% of bid side (5,500 resting ≥ 5,000 ✓) ≈ $3.47/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 28.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~74.1% of ask side (12,148 resting ≥ 5,000 ✓) ≈ $2.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 8.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~68.7% of ask side (11,940 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | BUY | 15.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~67.9% of bid side (10,292 resting ≥ 2,000 ✓) ≈ $0.85/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~66.6% of ask side (11,990 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 25.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~65.0% of ask side (127,678 resting ≥ 2,000 ✓) ≈ $0.81/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 15.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~62.5% of ask side (5,500 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | SELL | 3.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~62.4% of ask side (104,384 resting ≥ 2,000 ✓) ≈ $0.78/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 10.0¢ | 46 | 0 | $100.00 | ✅ scoring — ~62.1% of ask side (12,067 resting ≥ 5,000 ✓) ≈ $2.39/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~61.7% of ask side (9,905 resting ≥ 5,000 ✓) ≈ $2.57/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 30.0¢ | 47 | 0 | $100.00 | ✅ scoring — ~58.7% of bid side (5,566 resting ≥ 5,000 ✓) ≈ $2.26/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 89.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~58.1% of bid side (5,511 resting ≥ 5,000 ✓) ≈ $2.42/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 80.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~53.8% of bid side (5,781 resting ≥ 5,000 ✓) ≈ $2.24/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 78.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~53.8% of bid side (5,770 resting ≥ 5,000 ✓) ≈ $2.24/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~53.6% of ask side (11,968 resting ≥ 5,000 ✓) ≈ $2.06/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 50.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~52.6% of ask side (8,368 resting ≥ 5,000 ✓) ≈ $2.19/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 55.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~50.5% of bid side (5,603 resting ≥ 5,000 ✓) ≈ $2.10/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 7.0¢ | 70 | 0 | $100.00 | ✅ scoring — ~48.6% of ask side (12,052 resting ≥ 5,000 ✓) ≈ $1.87/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 16.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~47.6% of ask side (128,004 resting ≥ 2,000 ✓) ≈ $0.60/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 16.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~47.6% of ask side (128,004 resting ≥ 2,000 ✓) ≈ $0.60/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 4.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~46.0% of bid side (25,622 resting ≥ 2,000 ✓) ≈ $0.96/day (pool ÷ 6 markets) |
| `ewc-ref-fl-tax-2026-11-03-pass` | SELL | 58.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~42.1% of ask side (2,663 resting ≥ 2,000 ✓) ≈ $5.26/day |
| `scc-senate-gop-2026-11-03-54` | SELL | 14.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~40.3% of ask side (11,228 resting ≥ 5,000 ✓) ≈ $1.55/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~40.0% of ask side (12,053 resting ≥ 5,000 ✓) ≈ $1.54/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | BUY | 14.0¢ | 9 | 1 | $25.00 | ✅ scoring — ~39.0% of bid side (30,803 resting ≥ 2,000 ✓) ≈ $0.49/day (pool ÷ 10 markets) |
| `nocc-attgen-todblanche-2026-08-07` | BUY | 3.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~38.3% of bid side (2,322 resting ≥ 2,000 ✓) ≈ $4.78/day |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~32.7% of bid side (5,610 resting ≥ 5,000 ✓) ≈ $1.26/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~29.4% of ask side (11,947 resting ≥ 5,000 ✓) ≈ $1.13/day (pool ÷ 13 markets) |
| …and 70 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>gsc-usfedgvmt-by-2026-10-01</code> SELL 6 @ 60¢ → $12.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 6 (6 yours) | ×0.1^0 = 6.0 |
|  | 63¢ | 3 | ×0.1^3 = 0.0 |
|  | 74¢ | 57 | ×0.1^14 = 0.0 |
|  | 75¢ | 25 | ×0.1^15 = 0.0 |
|  | 99¢ | 2,469 | ×0.1^39 = 0.0 |
| | | **Σ** | **6.0** |

`yours 6.0 / Σ 6.0 = 100.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 100.0% = $12.49/day`  

</details>
<details><summary><code>nocc-attgen-todblanche-2026-08-07</code> SELL 10 @ 20¢ → $10.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 21¢ | 4 | ×0.1^1 = 0.4 |
|  | 22¢ | 102 | ×0.1^2 = 1.0 |
|  | 34¢ | 100 | ×0.1^14 = 0.0 |
|  | 42¢ | 100 | ×0.1^22 = 0.0 |
|  | 82¢ | 200 | ×0.1^62 = 0.0 |
|  | 94¢ | 200 | ×0.1^74 = 0.0 |
|  | 99¢ | 7,891 | ×0.1^79 = 0.0 |
| | | **Σ** | **11.4** |

`yours 10.0 / Σ 11.4 = 87.6%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 87.6% = $10.95/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 50 @ 38¢ → $3.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 39¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 38¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 1¢ | 5,448 | ×0.2^38 = 0.0 |
| | | **Σ** | **12.0** |

`yours 10.0 / Σ 12.0 = 83.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 83.3% = $3.47/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 28¢ → $2.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 63 (50 yours) | ×0.2^0 = 63.0 |
|  | 30¢ | 112 | ×0.2^2 = 4.5 |
|  | 32¢ | 2 | ×0.2^4 = 0.0 |
|  | 40¢ | 30 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 98¢ | 1,840 | ×0.2^70 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^71 = 0.0 |
| | | **Σ** | **67.5** |

`yours 50.0 / Σ 67.5 = 74.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 74.1% = $2.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 5 @ 8¢ → $2.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 7 (5 yours) | ×0.2^0 = 7.0 |
|  | 9¢ | 1 | ×0.2^1 = 0.3 |
|  | 40¢ | 29 | ×0.2^32 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,802 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^91 = 0.0 |
| | | **Σ** | **7.3** |

`yours 5.0 / Σ 7.3 = 68.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.7% = $2.64/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> BUY 15 @ 15¢ → $0.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 22 (15 yours) | ×0.1^0 = 22.0 |
|  | 14¢ | 1 | ×0.1^1 = 0.1 |
|  | 9¢ | 6 | ×0.1^6 = 0.0 |
|  | 7¢ | 31 | ×0.1^8 = 0.0 |
|  | 1¢ | 10,232 | ×0.1^14 = 0.0 |
| | | **Σ** | **22.1** |

`yours 15.0 / Σ 22.1 = 67.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 67.9% = $0.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 50 @ 10¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 75 (50 yours) | ×0.2^0 = 75.0 |
|  | 13¢ | 11 | ×0.2^3 = 0.1 |
|  | 35¢ | 15 | ×0.2^25 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,788 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **75.1** |

`yours 50.0 / Σ 75.1 = 66.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.6% = $2.56/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 15 @ 25¢ → $0.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 23 (15 yours) | ×0.1^0 = 23.0 |
|  | 27¢ | 6 | ×0.1^2 = 0.1 |
|  | 28¢ | 18 | ×0.1^3 = 0.0 |
|  | 30¢ | 7 | ×0.1^5 = 0.0 |
|  | 45¢ | 25 | ×0.1^20 = 0.0 |
|  | 98¢ | 127,099 | ×0.1^73 = 0.0 |
| | | **Σ** | **23.1** |

`yours 15.0 / Σ 23.1 = 65.0%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 65.0% = $0.81/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 15¢ → $2.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 80 (50 yours) | ×0.2^0 = 80.0 |
|  | 49¢ | 15 | ×0.2^34 = 0.0 |
|  | 50¢ | 25 | ×0.2^35 = 0.0 |
|  | 99¢ | 5,380 | ×0.2^84 = 0.0 |
| | | **Σ** | **80.0** |

`yours 50.0 / Σ 80.0 = 62.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 62.5% = $2.60/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> SELL 10 @ 3¢ → $0.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 16 (10 yours) | ×0.1^0 = 16.0 |
|  | 6¢ | 7 | ×0.1^3 = 0.0 |
|  | 7¢ | 17 | ×0.1^4 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 46 @ 10¢ → $2.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 74 (46 yours) | ×0.2^0 = 74.0 |
|  | 15¢ | 48 | ×0.2^5 = 0.0 |
|  | 20¢ | 50 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,794 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **74.0** |

`yours 46.0 / Σ 74.0 = 62.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 62.1% = $2.39/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 100 @ 20¢ → $2.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 162 (100 yours) | ×0.2^0 = 162.0 |
|  | 50¢ | 25 | ×0.2^30 = 0.0 |
|  | 99¢ | 9,718 | ×0.2^79 = 0.0 |
| | | **Σ** | **162.0** |

`yours 100.0 / Σ 162.0 = 61.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 61.7% = $2.57/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 47 @ 30¢ → $2.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 80 (47 yours) | ×0.2^0 = 80.0 |
|  | 21¢ | 8 | ×0.2^9 = 0.0 |
|  | 1¢ | 5,478 | ×0.2^29 = 0.0 |
| | | **Σ** | **80.0** |

`yours 47.0 / Σ 80.0 = 58.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 58.7% = $2.26/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 50 @ 80¢ → $2.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 93 (50 yours) | ×0.2^0 = 93.0 |
|  | 1¢ | 5,688 | ×0.2^79 = 0.0 |
| | | **Σ** | **93.0** |

`yours 50.0 / Σ 93.0 = 53.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 53.8% = $2.24/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 50 @ 78¢ → $2.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 93 (50 yours) | ×0.2^0 = 93.0 |
|  | 1¢ | 5,677 | ×0.2^77 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 15 @ 21¢ → $2.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 28 (15 yours) | ×0.2^0 = 28.0 |
|  | 24¢ | 1 | ×0.2^3 = 0.0 |
|  | 30¢ | 37 | ×0.2^9 = 0.0 |
|  | 37¢ | 5 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **28.0** |

`yours 15.0 / Σ 28.0 = 53.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.6% = $2.06/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 50 @ 50¢ → $2.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 95 (50 yours) | ×0.2^0 = 95.0 |
|  | 99¢ | 8,273 | ×0.2^49 = 0.0 |
| | | **Σ** | **95.0** |

`yours 50.0 / Σ 95.0 = 52.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 52.6% = $2.19/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> BUY 50 @ 55¢ → $2.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 55¢ | 99 (50 yours) | ×0.2^0 = 99.0 |
|  | 49¢ | 54 | ×0.2^6 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^54 = 0.0 |
| | | **Σ** | **99.0** |

`yours 50.0 / Σ 99.0 = 50.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 50.5% = $2.10/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 70 @ 7¢ → $1.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 144 (70 yours) | ×0.2^0 = 144.1 |
|  | 16¢ | 48 | ×0.2^9 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **144.1** |

`yours 70.0 / Σ 144.1 = 48.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.6% = $1.87/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 1 @ 16¢ → $0.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 17¢ | 1 | ×0.1^1 = 0.1 |
|  | 22¢ | 23 | ×0.1^6 = 0.0 |
|  | 39¢ | 107 | ×0.1^23 = 0.0 |
|  | 40¢ | 31 | ×0.1^24 = 0.0 |
|  | 45¢ | 25 | ×0.1^29 = 0.0 |
|  | 98¢ | 127,315 | ×0.1^82 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 47.6%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 47.6% = $0.60/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 1 @ 16¢ → $0.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 2 (1 yours) | ×0.1^0 = 2.0 |
|  | 17¢ | 1 | ×0.1^1 = 0.1 |
|  | 22¢ | 23 | ×0.1^6 = 0.0 |
|  | 39¢ | 107 | ×0.1^23 = 0.0 |
|  | 40¢ | 31 | ×0.1^24 = 0.0 |
|  | 45¢ | 25 | ×0.1^29 = 0.0 |
|  | 98¢ | 127,315 | ×0.1^82 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 47.6%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 47.6% = $0.60/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 50 @ 4¢ → $0.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 83 (50 yours) | ×0.1^0 = 83.0 |
|  | 3¢ | 2 | ×0.1^1 = 0.2 |
|  | 2¢ | 2 | ×0.1^2 = 0.0 |
|  | 1¢ | 25,535 | ×0.1^3 = 25.5 |
| | | **Σ** | **108.8** |

`yours 50.0 / Σ 108.8 = 46.0%`  
`$25 ÷ 6 ÷ 2 = $2.08 × 46.0% = $0.96/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>ewc-ref-fl-tax-2026-11-03-pass</code> SELL 5 @ 58¢ → $5.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 58¢ | 10 (5 yours) | ×0.1^0 = 10.0 |
|  | 59¢ | 1 | ×0.1^1 = 0.1 |
|  | 60¢ | 16 | ×0.1^2 = 0.2 |
|  | 61¢ | 1,611 | ×0.1^3 = 1.6 |
|  | 75¢ | 25 | ×0.1^17 = 0.0 |
|  | 99¢ | 1,000 | ×0.1^41 = 0.0 |
| | | **Σ** | **11.9** |

`yours 5.0 / Σ 11.9 = 42.1%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 42.1% = $5.26/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 14¢ → $1.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 124 (50 yours) | ×0.2^0 = 124.0 |
|  | 16¢ | 3 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^36 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^84 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^85 = 0.0 |
| | | **Σ** | **124.1** |

`yours 50.0 / Σ 124.1 = 40.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.3% = $1.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 50 @ 10¢ → $1.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 125 (50 yours) | ×0.2^0 = 125.0 |
|  | 13¢ | 19 | ×0.2^3 = 0.2 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,808 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **125.2** |

`yours 50.0 / Σ 125.2 = 40.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.0% = $1.54/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> BUY 9 @ 14¢ → $0.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 15¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 14¢ | 13 (9 yours) | ×0.1^1 = 1.3 |
|  | 13¢ | 1 | ×0.1^2 = 0.0 |
|  | 11¢ | 6 | ×0.1^4 = 0.0 |
|  | 9¢ | 6 | ×0.1^6 = 0.0 |
|  | 8¢ | 19 | ×0.1^7 = 0.0 |
|  | 4¢ | 7 | ×0.1^11 = 0.0 |
|  | 3¢ | 750 | ×0.1^12 = 0.0 |
|  | 1¢ | 30,000 | ×0.1^14 = 0.0 |
| | | **Σ** | **2.3** |

`yours 0.9 / Σ 2.3 = 39.0%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 39.0% = $0.49/day`  

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
<details><summary><code>nocc-attgen-todblanche-2026-08-07</code> BUY 50 @ 3¢ → $4.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 104 (50 yours) | ×0.1^0 = 104.0 |
|  | 2¢ | 50 | ×0.1^1 = 5.0 |
|  | 1¢ | 2,168 | ×0.1^2 = 21.7 |
| | | **Σ** | **130.7** |

`yours 50.0 / Σ 130.7 = 38.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 38.3% = $4.78/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 50 @ 20¢ → $1.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 153 (50 yours) | ×0.2^0 = 153.0 |
|  | 11¢ | 7 | ×0.2^9 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^19 = 0.0 |
| | | **Σ** | **153.0** |

`yours 50.0 / Σ 153.0 = 32.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.7% = $1.26/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 10 @ 12¢ → $1.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 34 (10 yours) | ×0.2^0 = 34.0 |
|  | 17¢ | 47 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 98¢ | 1,765 | ×0.2^86 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^87 = 0.0 |
| | | **Σ** | **34.0** |

`yours 10.0 / Σ 34.0 = 29.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.4% = $1.13/day`  

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
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (86,018 resting) | ~42.5% | ~$10.64 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (288,187 resting) | ~10.1% | ~$7.58 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (72,941 resting) | ~9.6% | ~$7.16 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (83,711 resting) | ~25.9% | ~$6.47 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (60,923 resting) | ~20.0% | ~$4.99 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (210,115 resting) | ~6.1% | ~$4.59 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,342 resting) | ~4.0% | ~$3.00 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (77,887 resting) | ~3.8% | ~$2.85 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (178,472 resting) | ~3.7% | ~$2.77 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (6,066 resting) | ~9.2% | ~$2.31 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (75,071 resting) | ~6.8% | ~$1.71 |
| `cranc-uspres28-12-31-2026-robken` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (40,505 resting) | ~99.5% | ~$1.51 |

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
| 2026-07-30 9:57 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:52 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:36 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 9:14 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 8:17 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 7:45 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 6:29 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 4:37 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:56 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:50 PM ET | ✅ ok | 1267 | $1321.41 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
