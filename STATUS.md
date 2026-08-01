# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-31 9:35 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$77.02/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$18.13/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$17.09/day), `apdc-jerpowgov-2026-12-31` (~$13.57/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$77.02/day (~$3.21/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-54` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~96.2% of bid side (5,200 resting ≥ 5,000 ✓) ≈ $3.70/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~95.9% of ask side (12,142 resting ≥ 5,000 ✓) ≈ $3.69/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 6.0¢ | 23 | 0 | $100.00 | ✅ scoring — ~92.9% of bid side (5,234 resting ≥ 5,000 ✓) ≈ $3.57/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 35.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~92.8% of ask side (8,770 resting ≥ 5,000 ✓) ≈ $3.87/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 32.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~92.2% of ask side (127,615 resting ≥ 2,000 ✓) ≈ $1.15/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 84.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~90.6% of ask side (9,147 resting ≥ 5,000 ✓) ≈ $3.77/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 36.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~78.1% of ask side (12,175 resting ≥ 5,000 ✓) ≈ $3.00/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 89.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~71.4% of bid side (5,499 resting ≥ 5,000 ✓) ≈ $2.98/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 30 | 1 | $100.00 | ✅ scoring — ~67.7% of ask side (8,511 resting ≥ 5,000 ✓) ≈ $2.82/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~65.6% of ask side (11,932 resting ≥ 5,000 ✓) ≈ $2.52/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 6.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~64.9% of ask side (11,944 resting ≥ 5,000 ✓) ≈ $2.50/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 85.0¢ | 60 | 0 | $100.00 | ✅ scoring — ~63.7% of bid side (5,501 resting ≥ 5,000 ✓) ≈ $2.65/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 79.0¢ | 48 | 0 | $100.00 | ✅ scoring — ~62.9% of bid side (5,584 resting ≥ 5,000 ✓) ≈ $2.62/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 7.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~61.7% of ask side (8,850 resting ≥ 5,000 ✓) ≈ $2.57/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 10.0¢ | 46 | 0 | $100.00 | ✅ scoring — ~61.2% of ask side (11,995 resting ≥ 5,000 ✓) ≈ $2.36/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 13.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~58.1% of ask side (11,947 resting ≥ 5,000 ✓) ≈ $2.23/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 37.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~58.0% of ask side (12,167 resting ≥ 5,000 ✓) ≈ $2.23/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~56.3% of ask side (12,135 resting ≥ 5,000 ✓) ≈ $2.17/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 13.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~53.9% of ask side (12,147 resting ≥ 5,000 ✓) ≈ $2.07/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 7.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~53.7% of ask side (11,195 resting ≥ 5,000 ✓) ≈ $2.07/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~49.0% of bid side (6,200 resting ≥ 5,000 ✓) ≈ $2.04/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 42.0¢ | 53 | 0 | $100.00 | ✅ scoring — ~47.3% of ask side (8,780 resting ≥ 5,000 ✓) ≈ $1.97/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~44.5% of ask side (12,029 resting ≥ 5,000 ✓) ≈ $1.71/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 11.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~37.9% of ask side (5,661 resting ≥ 5,000 ✓) ≈ $1.58/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 15.0¢ | 62 | 0 | $100.00 | ✅ scoring — ~34.3% of ask side (12,281 resting ≥ 5,000 ✓) ≈ $1.32/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 90.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~28.6% of bid side (5,499 resting ≥ 5,000 ✓) ≈ $1.19/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 9.0¢ | 49 | 0 | $100.00 | ✅ scoring — ~25.7% of bid side (5,550 resting ≥ 5,000 ✓) ≈ $0.99/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 62.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~22.1% of ask side (5,234 resting ≥ 5,000 ✓) ≈ $0.92/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 79.0¢ | 29 | 1 | $100.00 | ✅ scoring — ~16.5% of bid side (5,258 resting ≥ 5,000 ✓) ≈ $0.69/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | SELL | 91.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~15.7% of ask side (6,344 resting ≥ 5,000 ✓) ≈ $0.65/day (pool ÷ 12 markets) |
| …and 179 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 5,000 @ 1¢ → $3.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^0 = 5,200.0 |
| | | **Σ** | **5,200.0** |

`yours 5,000.0 / Σ 5,200.0 = 96.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 96.2% = $3.70/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 10¢ → $3.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 52 (50 yours) | ×0.2^0 = 52.1 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **52.1** |

`yours 50.0 / Σ 52.1 = 95.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 95.9% = $3.69/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 23 @ 6¢ → $3.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 23 (23 yours) | ×0.2^0 = 23.0 |
|  | 3¢ | 11 | ×0.2^3 = 0.1 |
|  | 1¢ | 5,200 | ×0.2^5 = 1.7 |
| | | **Σ** | **24.8** |

`yours 23.0 / Σ 24.8 = 92.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 92.9% = $3.57/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 20 @ 35¢ → $3.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 22 (20 yours) | ×0.2^0 = 21.5 |
|  | 40¢ | 94 | ×0.2^5 = 0.0 |
|  | 50¢ | 25 | ×0.2^15 = 0.0 |
|  | 99¢ | 8,630 | ×0.2^64 = 0.0 |
| | | **Σ** | **21.6** |

`yours 20.0 / Σ 21.6 = 92.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 92.8% = $3.87/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 10 @ 32¢ → $1.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 33¢ | 6 | ×0.1^1 = 0.6 |
|  | 34¢ | 25 | ×0.1^2 = 0.3 |
|  | 37¢ | 18 | ×0.1^5 = 0.0 |
|  | 38¢ | 20 | ×0.1^6 = 0.0 |
|  | 45¢ | 25 | ×0.1^13 = 0.0 |
|  | 98¢ | 127,011 | ×0.1^66 = 0.0 |
| | | **Σ** | **10.9** |

`yours 10.0 / Σ 10.9 = 92.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 92.2% = $1.15/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 100 @ 84¢ → $3.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 106 (100 yours) | ×0.2^0 = 106.2 |
|  | 86¢ | 104 | ×0.2^2 = 4.1 |
|  | 90¢ | 1 | ×0.2^6 = 0.0 |
|  | 93¢ | 133 | ×0.2^9 = 0.0 |
|  | 99¢ | 8,803 | ×0.2^15 = 0.0 |
| | | **Σ** | **110.4** |

`yours 100.0 / Σ 110.4 = 90.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 90.6% = $3.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 50 @ 36¢ → $3.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 36¢ | 52 (50 yours) | ×0.2^0 = 52.5 |
|  | 37¢ | 57 | ×0.2^1 = 11.4 |
|  | 40¢ | 105 | ×0.2^4 = 0.2 |
|  | 50¢ | 100 | ×0.2^14 = 0.0 |
|  | 98¢ | 1,860 | ×0.2^62 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^63 = 0.0 |
| | | **Σ** | **64.0** |

`yours 50.0 / Σ 64.0 = 78.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 78.1% = $3.00/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 50 @ 89¢ → $2.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 90¢ | 4 | ×0.2^0 = 4.0 |
| ▶ | 89¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 1¢ | 5,445 | ×0.2^89 = 0.0 |
| | | **Σ** | **14.0** |

`yours 10.0 / Σ 14.0 = 71.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 71.4% = $2.98/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 30 @ 7¢ → $2.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 2 | ×0.2^0 = 2.1 |
| ▶ | 7¢ | 34 (30 yours) | ×0.2^1 = 6.8 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 50¢ | 25 | ×0.2^44 = 0.0 |
|  | 99¢ | 8,449 | ×0.2^93 = 0.0 |
| | | **Σ** | **8.9** |

`yours 6.0 / Σ 8.9 = 67.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 67.7% = $2.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 50 @ 15¢ → $2.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 76 (50 yours) | ×0.2^0 = 76.2 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,755 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **76.2** |

`yours 50.0 / Σ 76.2 = 65.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 65.6% = $2.52/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 50 @ 6¢ → $2.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 77 (50 yours) | ×0.2^0 = 77.1 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,766 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **77.1** |

`yours 50.0 / Σ 77.1 = 64.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.9% = $2.50/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 60 @ 85¢ → $2.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 94 (60 yours) | ×0.2^0 = 94.2 |
|  | 1¢ | 5,407 | ×0.2^84 = 0.0 |
| | | **Σ** | **94.2** |

`yours 60.0 / Σ 94.2 = 63.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 63.7% = $2.65/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 48 @ 79¢ → $2.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 76 (48 yours) | ×0.2^0 = 76.3 |
|  | 70¢ | 83 | ×0.2^9 = 0.0 |
|  | 1¢ | 5,425 | ×0.2^78 = 0.0 |
| | | **Σ** | **76.3** |

`yours 48.0 / Σ 76.3 = 62.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 62.9% = $2.62/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 7¢ → $2.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 81 (50 yours) | ×0.2^0 = 81.1 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 14¢ | 15 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 99¢ | 8,728 | ×0.2^92 = 0.0 |
| | | **Σ** | **81.1** |

`yours 50.0 / Σ 81.1 = 61.7%`  
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
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 46 @ 10¢ → $2.36/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 75 (46 yours) | ×0.2^0 = 75.1 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,819 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **75.1** |

`yours 46.0 / Σ 75.1 = 61.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 61.2% = $2.36/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 30 @ 13¢ → $2.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 51 (30 yours) | ×0.2^0 = 51.1 |
|  | 15¢ | 10 | ×0.2^2 = 0.4 |
|  | 16¢ | 15 | ×0.2^3 = 0.1 |
|  | 50¢ | 100 | ×0.2^37 = 0.0 |
|  | 98¢ | 1,770 | ×0.2^85 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^86 = 0.0 |
| | | **Σ** | **51.7** |

`yours 30.0 / Σ 51.7 = 58.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 58.1% = $2.23/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 37¢ → $2.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 49 (43 yours) | ×0.2^0 = 48.6 |
|  | 38¢ | 128 | ×0.2^1 = 25.6 |
|  | 50¢ | 100 | ×0.2^13 = 0.0 |
|  | 53¢ | 37 | ×0.2^16 = 0.0 |
|  | 98¢ | 1,852 | ×0.2^61 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^62 = 0.0 |
| | | **Σ** | **74.2** |

`yours 43.0 / Σ 74.2 = 58.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 58.0% = $2.23/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 22 @ 20¢ → $2.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 38 (22 yours) | ×0.2^0 = 38.2 |
|  | 22¢ | 17 | ×0.2^2 = 0.7 |
|  | 24¢ | 100 | ×0.2^4 = 0.2 |
|  | 39¢ | 40 | ×0.2^19 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,839 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **39.1** |

`yours 22.0 / Σ 39.1 = 56.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 56.3% = $2.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 13¢ → $2.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 60 (40 yours) | ×0.2^0 = 60.4 |
|  | 14¢ | 65 | ×0.2^1 = 13.0 |
|  | 16¢ | 102 | ×0.2^3 = 0.8 |
|  | 50¢ | 100 | ×0.2^37 = 0.0 |
|  | 98¢ | 1,819 | ×0.2^85 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^86 = 0.0 |
| | | **Σ** | **74.2** |

`yours 40.0 / Σ 74.2 = 53.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.9% = $2.07/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 7¢ → $2.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 93 (50 yours) | ×0.2^0 = 93.1 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^92 = 0.0 |
| | | **Σ** | **93.1** |

`yours 50.0 / Σ 93.1 = 53.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.7% = $2.07/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> BUY 5,000 @ 1¢ → $2.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 1,000 | ×0.2^0 = 1,000.0 |
| ▶ | 1¢ | 5,200 (5,000 yours) | ×0.2^1 = 1,040.0 |
| | | **Σ** | **2,040.0** |

`yours 1,000.0 / Σ 2,040.0 = 49.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.0% = $2.04/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 53 @ 42¢ → $1.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 112 (53 yours) | ×0.2^0 = 112.0 |
|  | 52¢ | 1 | ×0.2^10 = 0.0 |
|  | 61¢ | 13 | ×0.2^19 = 0.0 |
|  | 69¢ | 100 | ×0.2^27 = 0.0 |
|  | 99¢ | 8,554 | ×0.2^57 = 0.0 |
| | | **Σ** | **112.0** |

`yours 53.0 / Σ 112.0 = 47.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 47.3% = $1.97/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 50 @ 21¢ → $1.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 112 (50 yours) | ×0.2^0 = 112.4 |
|  | 30¢ | 20 | ×0.2^9 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **112.4** |

`yours 50.0 / Σ 112.4 = 44.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 44.5% = $1.71/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 30 @ 11¢ → $1.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 79 (30 yours) | ×0.2^0 = 79.2 |
|  | 20¢ | 1 | ×0.2^9 = 0.0 |
|  | 50¢ | 25 | ×0.2^39 = 0.0 |
|  | 99¢ | 5,556 | ×0.2^88 = 0.0 |
| | | **Σ** | **79.2** |

`yours 30.0 / Σ 79.2 = 37.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 37.9% = $1.58/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 62 @ 15¢ → $1.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 160 (62 yours) | ×0.2^0 = 160.2 |
|  | 16¢ | 104 | ×0.2^1 = 20.8 |
|  | 20¢ | 30 | ×0.2^5 = 0.0 |
|  | 40¢ | 29 | ×0.2^25 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,857 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **181.0** |

`yours 62.0 / Σ 181.0 = 34.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.3% = $1.32/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 4 @ 90¢ → $1.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 4 (4 yours) | ×0.2^0 = 4.0 |
|  | 89¢ | 50 | ×0.2^1 = 10.0 |
|  | 1¢ | 5,445 | ×0.2^89 = 0.0 |
| | | **Σ** | **14.0** |

`yours 4.0 / Σ 14.0 = 28.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 28.6% = $1.19/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 49 @ 9¢ → $0.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 171 (49 yours) | ×0.2^0 = 171.1 |
|  | 8¢ | 98 | ×0.2^1 = 19.6 |
|  | 2¢ | 81 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^8 = 0.0 |
| | | **Σ** | **190.7** |

`yours 49.0 / Σ 190.7 = 25.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.7% = $0.99/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 30 @ 62¢ → $0.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 62¢ | 136 (30 yours) | ×0.2^0 = 135.7 |
|  | 83¢ | 103 | ×0.2^21 = 0.0 |
|  | 99¢ | 4,995 | ×0.2^37 = 0.0 |
| | | **Σ** | **135.7** |

`yours 30.0 / Σ 135.7 = 22.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 22.1% = $0.92/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 29 @ 79¢ → $0.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 80¢ | 29 | ×0.2^0 = 29.2 |
| ▶ | 79¢ | 29 (29 yours) | ×0.2^1 = 5.8 |
|  | 1¢ | 5,200 | ×0.2^79 = 0.0 |
| | | **Σ** | **35.0** |

`yours 5.8 / Σ 35.0 = 16.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.5% = $0.69/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> SELL 5 @ 91¢ → $0.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 16 (5 yours) | ×0.2^0 = 16.1 |
|  | 92¢ | 79 | ×0.2^1 = 15.8 |
|  | 99¢ | 6,249 | ×0.2^8 = 0.0 |
| | | **Σ** | **31.9** |

`yours 5.0 / Σ 31.9 = 15.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 15.7% = $0.65/day`  

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
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (79,757 resting) | ~72.5% | ~$18.13 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (90,753 resting) | ~22.8% | ~$17.09 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (8,605 resting) | ~81.4% | ~$13.57 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (5,005 resting) | ~80.3% | ~$13.39 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (83,538 resting) | ~26.7% | ~$6.67 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (73,365 resting) | ~7.9% | ~$5.96 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (52,463 resting) | ~15.1% | ~$3.78 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (143,808 resting) | ~4.9% | ~$3.69 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (73,992 resting) | ~10.9% | ~$2.72 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (95,240 resting) | ~3.6% | ~$2.68 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (77,070 resting) | ~3.3% | ~$2.46 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (206,617 resting) | ~2.1% | ~$1.61 |

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
| 2026-07-31 9:35 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 9:34 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 9:31 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 9:12 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 9:09 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 9:02 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 8:13 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 7:18 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 6:17 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-07-31 5:11 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
