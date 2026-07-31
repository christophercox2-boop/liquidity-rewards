# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-30 9:14 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$58.68/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$9.80/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$7.46/day), `ewc-usse-tx-2026-11-03-rep` (~$7.44/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$58.68/day (~$2.45/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 30.0¢ | 300 | 0 | $100.00 | ✅ scoring — ~94.3% of bid side (5,518 resting ≥ 5,000 ✓) ≈ $3.93/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 38.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~83.3% of bid side (5,502 resting ≥ 5,000 ✓) ≈ $3.47/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 8.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~68.7% of ask side (11,940 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | BUY | 15.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~67.9% of bid side (10,274 resting ≥ 2,000 ✓) ≈ $0.85/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (8,651 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 25.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~65.2% of ask side (127,660 resting ≥ 2,000 ✓) ≈ $0.82/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | SELL | 3.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~62.4% of ask side (104,384 resting ≥ 2,000 ✓) ≈ $0.78/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 78.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~61.7% of bid side (5,758 resting ≥ 5,000 ✓) ≈ $2.57/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 89.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~58.1% of bid side (5,511 resting ≥ 5,000 ✓) ≈ $2.42/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~58.1% of ask side (11,933 resting ≥ 5,000 ✓) ≈ $2.23/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 30.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~56.2% of ask side (7,540 resting ≥ 5,000 ✓) ≈ $2.34/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 15.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~54.9% of ask side (5,707 resting ≥ 5,000 ✓) ≈ $2.29/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~54.9% of ask side (12,036 resting ≥ 5,000 ✓) ≈ $2.11/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 80.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~53.8% of bid side (5,781 resting ≥ 5,000 ✓) ≈ $2.24/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 50.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~52.6% of ask side (6,149 resting ≥ 5,000 ✓) ≈ $2.19/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 55.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~50.5% of bid side (5,603 resting ≥ 5,000 ✓) ≈ $2.10/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 30.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~48.1% of bid side (5,554 resting ≥ 5,000 ✓) ≈ $1.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 7.0¢ | 70 | 0 | $100.00 | ✅ scoring — ~47.3% of ask side (12,008 resting ≥ 5,000 ✓) ≈ $1.82/day (pool ÷ 13 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 4.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~46.0% of bid side (25,622 resting ≥ 2,000 ✓) ≈ $0.96/day (pool ÷ 6 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 50.0¢ | 13 | 0 | $100.00 | ✅ scoring — ~44.8% of ask side (6,174 resting ≥ 5,000 ✓) ≈ $1.87/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | BUY | 14.0¢ | 9 | 1 | $25.00 | ✅ scoring — ~30.9% of bid side (30,794 resting ≥ 2,000 ✓) ≈ $0.39/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 11.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~30.3% of bid side (5,835 resting ≥ 5,000 ✓) ≈ $1.26/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 19.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~27.0% of bid side (5,297 resting ≥ 5,000 ✓) ≈ $1.04/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 75.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~27.0% of bid side (5,294 resting ≥ 5,000 ✓) ≈ $1.13/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 32.0¢ | 42 | 0 | $100.00 | ✅ scoring — ~23.8% of ask side (12,165 resting ≥ 5,000 ✓) ≈ $0.92/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 70.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~19.1% of ask side (5,599 resting ≥ 5,000 ✓) ≈ $0.80/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~19.1% of bid side (26,213 resting ≥ 5,000 ✓) ≈ $0.73/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~19.1% of bid side (26,225 resting ≥ 5,000 ✓) ≈ $0.79/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 94.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~18.9% of ask side (42,867 resting ≥ 5,000 ✓) ≈ $0.79/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 14.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~18.9% of ask side (11,130 resting ≥ 5,000 ✓) ≈ $0.73/day (pool ÷ 13 markets) |
| …and 51 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 300 @ 30¢ → $3.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 318 (300 yours) | ×0.2^0 = 318.0 |
|  | 1¢ | 5,200 | ×0.2^29 = 0.0 |
| | | **Σ** | **318.0** |

`yours 300.0 / Σ 318.0 = 94.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 94.3% = $3.93/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 50 @ 38¢ → $3.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 39¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 38¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 1¢ | 5,450 | ×0.2^38 = 0.0 |
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
|  | 6¢ | 13 | ×0.1^9 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 100 @ 20¢ → $2.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 150 (100 yours) | ×0.2^0 = 150.0 |
|  | 50¢ | 25 | ×0.2^30 = 0.0 |
|  | 99¢ | 8,476 | ×0.2^79 = 0.0 |
| | | **Σ** | **150.0** |

`yours 100.0 / Σ 150.0 = 66.7%`  
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
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230` ← this one
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 15 @ 25¢ → $0.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 23 (15 yours) | ×0.1^0 = 23.0 |
|  | 29¢ | 6 | ×0.1^4 = 0.0 |
|  | 30¢ | 7 | ×0.1^5 = 0.0 |
|  | 45¢ | 25 | ×0.1^20 = 0.0 |
|  | 98¢ | 127,099 | ×0.1^73 = 0.0 |
| | | **Σ** | **23.0** |

`yours 15.0 / Σ 23.0 = 65.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 65.2% = $0.82/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 50 @ 78¢ → $2.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 81 (50 yours) | ×0.2^0 = 81.0 |
|  | 1¢ | 5,677 | ×0.2^77 = 0.0 |
| | | **Σ** | **81.0** |

`yours 50.0 / Σ 81.0 = 61.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 61.7% = $2.57/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 18 @ 21¢ → $2.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 31 (18 yours) | ×0.2^0 = 31.0 |
|  | 37¢ | 5 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **31.0** |

`yours 18.0 / Σ 31.0 = 58.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 58.1% = $2.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 50 @ 30¢ → $2.34/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 89 (50 yours) | ×0.2^0 = 89.0 |
|  | 50¢ | 25 | ×0.2^20 = 0.0 |
|  | 99¢ | 7,426 | ×0.2^69 = 0.0 |
| | | **Σ** | **89.0** |

`yours 50.0 / Σ 89.0 = 56.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 56.2% = $2.34/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 15¢ → $2.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 91 (50 yours) | ×0.2^0 = 91.0 |
|  | 49¢ | 15 | ×0.2^34 = 0.0 |
|  | 50¢ | 25 | ×0.2^35 = 0.0 |
|  | 99¢ | 5,576 | ×0.2^84 = 0.0 |
| | | **Σ** | **91.0** |

`yours 50.0 / Σ 91.0 = 54.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 54.9% = $2.29/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 50 @ 10¢ → $2.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 91 (50 yours) | ×0.2^0 = 91.0 |
|  | 20¢ | 50 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,794 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **91.0** |

`yours 50.0 / Σ 91.0 = 54.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 54.9% = $2.11/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 50 @ 50¢ → $2.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 95 (50 yours) | ×0.2^0 = 95.0 |
|  | 99¢ | 6,054 | ×0.2^49 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 50 @ 30¢ → $1.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 104 (50 yours) | ×0.2^0 = 104.0 |
|  | 1¢ | 5,450 | ×0.2^29 = 0.0 |
| | | **Σ** | **104.0** |

`yours 50.0 / Σ 104.0 = 48.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.1% = $1.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 70 @ 7¢ → $1.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 148 (70 yours) | ×0.2^0 = 148.1 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,759 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **148.1** |

`yours 70.0 / Σ 148.1 = 47.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.3% = $1.82/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 13 @ 50¢ → $1.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 29 (13 yours) | ×0.2^0 = 29.0 |
|  | 99¢ | 6,145 | ×0.2^49 = 0.0 |
| | | **Σ** | **29.0** |

`yours 13.0 / Σ 29.0 = 44.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 44.8% = $1.87/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> BUY 9 @ 14¢ → $0.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 15¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 14¢ | 9 (9 yours) | ×0.1^1 = 0.9 |
|  | 13¢ | 1 | ×0.1^2 = 0.0 |
|  | 10¢ | 19 | ×0.1^5 = 0.0 |
|  | 9¢ | 6 | ×0.1^6 = 0.0 |
|  | 4¢ | 7 | ×0.1^11 = 0.0 |
|  | 3¢ | 750 | ×0.1^12 = 0.0 |
|  | 1¢ | 30,000 | ×0.1^14 = 0.0 |
| | | **Σ** | **2.9** |

`yours 0.9 / Σ 2.9 = 30.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 30.9% = $0.39/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 50 @ 11¢ → $1.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 165 (50 yours) | ×0.2^0 = 165.0 |
|  | 1¢ | 5,670 | ×0.2^10 = 0.0 |
| | | **Σ** | **165.0** |

`yours 50.0 / Σ 165.0 = 30.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 30.3% = $1.26/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 50 @ 19¢ → $1.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 27 | ×0.2^0 = 27.0 |
| ▶ | 19¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 5¢ | 20 | ×0.2^15 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **37.0** |

`yours 10.0 / Σ 37.0 = 27.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.0% = $1.04/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 75¢ → $1.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 37 (10 yours) | ×0.2^0 = 37.0 |
|  | 69¢ | 53 | ×0.2^6 = 0.0 |
|  | 1¢ | 5,204 | ×0.2^74 = 0.0 |
| | | **Σ** | **37.0** |

`yours 10.0 / Σ 37.0 = 27.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 27.0% = $1.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 42 @ 32¢ → $0.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 156 (42 yours) | ×0.2^0 = 156.0 |
|  | 33¢ | 101 | ×0.2^1 = 20.2 |
|  | 50¢ | 100 | ×0.2^18 = 0.0 |
|  | 98¢ | 1,807 | ×0.2^66 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^67 = 0.0 |
| | | **Σ** | **176.2** |

`yours 42.0 / Σ 176.2 = 23.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 23.8% = $0.92/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 30 @ 70¢ → $0.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 70¢ | 157 (30 yours) | ×0.2^0 = 156.8 |
|  | 99¢ | 5,442 | ×0.2^29 = 0.0 |
| | | **Σ** | **156.8** |

`yours 30.0 / Σ 156.8 = 19.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.1% = $0.80/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 5,000 @ 1¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 26,213 (5,000 yours) | ×0.2^0 = 26,213.0 |
| | | **Σ** | **26,213.0** |

`yours 5,000.0 / Σ 26,213.0 = 19.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.1% = $0.73/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 5,000 @ 1¢ → $0.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 26,225 (5,000 yours) | ×0.2^0 = 26,225.0 |
| | | **Σ** | **26,225.0** |

`yours 5,000.0 / Σ 26,225.0 = 19.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.1% = $0.79/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 30 @ 94¢ → $0.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 144 (30 yours) | ×0.2^0 = 144.0 |
|  | 98¢ | 729 | ×0.2^4 = 1.2 |
|  | 99¢ | 41,994 | ×0.2^5 = 13.4 |
| | | **Σ** | **158.6** |

`yours 30.0 / Σ 158.6 = 18.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.9% = $0.79/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 10 @ 14¢ → $0.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 14¢ | 28 (10 yours) | ×0.2^2 = 1.1 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^86 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^87 = 0.0 |
| | | **Σ** | **2.1** |

`yours 0.4 / Σ 2.1 = 18.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.9% = $0.73/day`  

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
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (86,018 resting) | ~39.2% | ~$9.80 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (73,430 resting) | ~10.0% | ~$7.46 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (297,525 resting) | ~9.9% | ~$7.44 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (57,780 resting) | ~26.5% | ~$6.62 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (83,711 resting) | ~25.9% | ~$6.47 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (231,750 resting) | ~8.2% | ~$6.16 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (121,168 resting) | ~4.8% | ~$3.61 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,362 resting) | ~4.0% | ~$2.98 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (178,472 resting) | ~3.7% | ~$2.77 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (74,506 resting) | ~9.9% | ~$2.48 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,187 resting) | ~9.4% | ~$2.34 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (77,636 resting) | ~2.9% | ~$2.21 |

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
| 2026-07-30 9:14 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-30 8:17 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 7:45 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 6:29 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 4:37 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:56 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:50 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 12:52 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 10:36 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 8:06 AM ET | ✅ ok | 1267 | $1321.41 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
