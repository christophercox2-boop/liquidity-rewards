# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-08 12:31 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$97.97/day estimated (ceiling, not promise — details below)

**Earned:** $1,712.09 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-06: **$52.21** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-05: **$31.46** · 2026-08-04: **$53.94** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$11.11/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$10.49/day), `paccc-usho-midterms-2026-11-03-rep` (~$7.98/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$97.97/day (~$4.08/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `lawec-cryptoleg-2026-12-31` | SELL | 25.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (30,490 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~99.3% of ask side (113,602 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~97.6% of bid side (8,001 resting ≥ 5,000 ✓) ≈ $3.75/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 10.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~97.1% of ask side (113,630 resting ≥ 5,000 ✓) ≈ $3.73/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~95.2% of ask side (48,664 resting ≥ 5,000 ✓) ≈ $3.97/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 34.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~95.1% of ask side (98,764 resting ≥ 5,000 ✓) ≈ $3.66/day (pool ÷ 13 markets) |
| `lawec-cryptoleg-2026-12-31` | BUY | 21.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~90.3% of bid side (29,457 resting ≥ 2,000 ✓) ≈ $5.64/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 31 | 1 | $100.00 | ✅ scoring — ~84.2% of bid side (80,582 resting ≥ 5,000 ✓) ≈ $3.51/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~73.5% of bid side (50,562 resting ≥ 5,000 ✓) ≈ $2.83/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 5.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~68.7% of ask side (113,728 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (117,795 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 50.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~66.6% of ask side (11,892 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~64.4% of ask side (113,517 resting ≥ 5,000 ✓) ≈ $2.48/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | SELL | 82.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~64.3% of ask side (7,162 resting ≥ 5,000 ✓) ≈ $2.68/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 19.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~63.2% of ask side (113,669 resting ≥ 5,000 ✓) ≈ $2.43/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 36.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~62.7% of ask side (48,453 resting ≥ 5,000 ✓) ≈ $2.61/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 63.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~59.8% of ask side (11,802 resting ≥ 5,000 ✓) ≈ $2.49/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 63.0¢ | 5 | 3 | $100.00 | ✅ scoring — ~57.8% of ask side (47,982 resting ≥ 5,000 ✓) ≈ $2.41/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 33.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~55.5% of bid side (200,484 resting ≥ 5,000 ✓) ≈ $2.31/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~46.0% of ask side (48,209 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 12.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~46.0% of bid side (80,537 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 5 | 4 | $100.00 | ✅ scoring — ~44.4% of bid side (200,315 resting ≥ 5,000 ✓) ≈ $1.71/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 84.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~44.4% of ask side (62,629 resting ≥ 5,000 ✓) ≈ $1.85/day (pool ÷ 12 markets) |
| `dccc-measles-us-2026-12-31-gt3000` | BUY | 78.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~37.7% of bid side (10,482 resting ≥ 10,000 ✓) ≈ $1.57/day (pool ÷ 6 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~37.6% of bid side (50,437 resting ≥ 5,000 ✓) ≈ $1.44/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 80.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~36.8% of bid side (50,553 resting ≥ 5,000 ✓) ≈ $1.53/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 13.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~36.3% of ask side (62,983 resting ≥ 5,000 ✓) ≈ $1.51/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 34.0¢ | 80 | 6 | $100.00 | ✅ scoring — ~33.9% of bid side (80,620 resting ≥ 5,000 ✓) ≈ $1.41/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 38.0¢ | 15 | 5 | $100.00 | ✅ scoring — ~32.4% of bid side (80,465 resting ≥ 5,000 ✓) ≈ $1.35/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~25.5% of ask side (62,634 resting ≥ 5,000 ✓) ≈ $1.06/day (pool ÷ 12 markets) |
| …and 50 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>lawec-cryptoleg-2026-12-31</code> SELL 10 @ 25¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 35¢ | 6 | ×0.1^10 = 0.0 |
|  | 46¢ | 7 | ×0.1^21 = 0.0 |
|  | 49¢ | 1,670 | ×0.1^24 = 0.0 |
|  | 52¢ | 3,485 | ×0.1^27 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-cryptoleg-2026-08-10`
2. `lawec-cryptoleg-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 24¢ → $3.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 27¢ | 9 | ×0.2^3 = 0.1 |
|  | 50¢ | 175 | ×0.2^26 = 0.0 |
|  | 76¢ | 0 | ×0.2^52 = 0.0 |
|  | 97¢ | 58,828 | ×0.2^73 = 0.0 |
| | | **Σ** | **10.1** |

`yours 10.0 / Σ 10.1 = 99.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.3% = $3.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 10 @ 8¢ → $3.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 2¢ | 2,766 | ×0.2^6 = 0.2 |
|  | 1¢ | 5,225 | ×0.2^7 = 0.1 |
| | | **Σ** | **10.2** |

`yours 10.0 / Σ 10.2 = 97.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 97.6% = $3.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 1 @ 10¢ → $3.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 22¢ | 27 | ×0.2^12 = 0.0 |
|  | 26¢ | 100 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 88¢ | 0 | ×0.2^78 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^87 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 97.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 97.1% = $3.73/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 20 @ 48¢ → $3.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 21 (20 yours) | ×0.2^0 = 21.0 |
|  | 51¢ | 1 | ×0.2^3 = 0.0 |
|  | 59¢ | 5 | ×0.2^11 = 0.0 |
|  | 60¢ | 100 | ×0.2^12 = 0.0 |
|  | 83¢ | 812 | ×0.2^35 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **21.0** |

`yours 20.0 / Σ 21.0 = 95.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 95.2% = $3.97/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 10 @ 34¢ → $3.66/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 36¢ | 1 | ×0.2^2 = 0.0 |
|  | 37¢ | 11 | ×0.2^3 = 0.1 |
|  | 38¢ | 239 | ×0.2^4 = 0.4 |
|  | 50¢ | 100 | ×0.2^16 = 0.0 |
|  | 59¢ | 0 | ×0.2^25 = 0.0 |
|  | 67¢ | 0 | ×0.2^33 = 0.0 |
|  | 68¢ | 0 | ×0.2^34 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^63 = 0.0 |
| | | **Σ** | **10.5** |

`yours 10.0 / Σ 10.5 = 95.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 95.1% = $3.66/day`  

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
<details><summary><code>lawec-cryptoleg-2026-12-31</code> BUY 0 @ 21¢ → $5.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 0 (0 yours) | ×0.1^0 = 0.4 |
|  | 19¢ | 1 | ×0.1^2 = 0.0 |
|  | 18¢ | 18 | ×0.1^3 = 0.0 |
|  | 17¢ | 129 | ×0.1^4 = 0.0 |
|  | 8¢ | 1,125 | ×0.1^13 = 0.0 |
|  | 7¢ | 784 | ×0.1^14 = 0.0 |
| | | **Σ** | **0.4** |

`yours 0.4 / Σ 0.4 = 90.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 90.3% = $5.64/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-cryptoleg-2026-08-10`
2. `lawec-cryptoleg-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 31 @ 75¢ → $3.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 76¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 75¢ | 31 (31 yours) | ×0.2^1 = 6.2 |
|  | 72¢ | 100 | ×0.2^4 = 0.2 |
|  | 2¢ | 80,250 | ×0.2^74 = 0.0 |
| | | **Σ** | **7.4** |

`yours 6.2 / Σ 7.4 = 84.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 84.2% = $3.51/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 20¢ → $2.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 11 (10 yours) | ×0.2^0 = 11.0 |
|  | 19¢ | 13 | ×0.2^1 = 2.6 |
|  | 9¢ | 129 | ×0.2^11 = 0.0 |
|  | 2¢ | 50,209 | ×0.2^18 = 0.0 |
| | | **Σ** | **13.6** |

`yours 10.0 / Σ 13.6 = 73.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 73.5% = $2.83/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 1 @ 5¢ → $2.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 15 | ×0.2^3 = 0.1 |
|  | 9¢ | 209 | ×0.2^4 = 0.3 |
|  | 10¢ | 1 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^92 = 0.0 |
| | | **Σ** | **1.5** |

`yours 1.0 / Σ 1.5 = 68.7%`  
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
9. `scc-senate-gop-2026-11-03-54` ← this one
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 20 @ 50¢ → $2.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 49¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 50¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 53¢ | 1 | ×0.2^4 = 0.0 |
|  | 54¢ | 0 | ×0.2^5 = 0.0 |
|  | 84¢ | 50 | ×0.2^35 = 0.0 |
|  | 99¢ | 11,819 | ×0.2^50 = 0.0 |
| | | **Σ** | **6.0** |

`yours 4.0 / Σ 6.0 = 66.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.6% = $2.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 10 @ 12¢ → $2.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 16 (10 yours) | ×0.2^0 = 15.5 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^85 = 0.0 |
| | | **Σ** | **15.5** |

`yours 10.0 / Σ 15.5 = 64.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.4% = $2.48/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> SELL 10 @ 82¢ → $2.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 84¢ | 1 | ×0.2^2 = 0.0 |
|  | 85¢ | 6 | ×0.2^3 = 0.0 |
|  | 87¢ | 1,422 | ×0.2^5 = 0.5 |
|  | 99¢ | 5,718 | ×0.2^17 = 0.0 |
| | | **Σ** | **15.5** |

`yours 10.0 / Σ 15.5 = 64.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 64.3% = $2.68/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 3 @ 19¢ → $2.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 3 (3 yours) | ×0.2^0 = 3.0 |
|  | 20¢ | 7 | ×0.2^1 = 1.4 |
|  | 23¢ | 218 | ×0.2^4 = 0.3 |
|  | 38¢ | 0 | ×0.2^19 = 0.0 |
|  | 50¢ | 39 | ×0.2^31 = 0.0 |
|  | 60¢ | 0 | ×0.2^41 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^78 = 0.0 |
| | | **Σ** | **4.7** |

`yours 3.0 / Σ 4.7 = 63.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 63.2% = $2.43/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 36¢ → $2.61/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 36¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 37¢ | 1 | ×0.2^1 = 0.2 |
|  | 39¢ | 718 | ×0.2^3 = 5.7 |
|  | 59¢ | 0 | ×0.2^23 = 0.0 |
|  | 64¢ | 0 | ×0.2^28 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^62 = 0.0 |
| | | **Σ** | **15.9** |

`yours 10.0 / Σ 15.9 = 62.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 62.7% = $2.61/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 3 @ 63¢ → $2.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 63¢ | 5 (3 yours) | ×0.2^0 = 5.0 |
|  | 66¢ | 1 | ×0.2^3 = 0.0 |
|  | 79¢ | 20 | ×0.2^16 = 0.0 |
|  | 95¢ | 100 | ×0.2^32 = 0.0 |
|  | 99¢ | 11,676 | ×0.2^36 = 0.0 |
| | | **Σ** | **5.0** |

`yours 3.0 / Σ 5.0 = 59.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 59.8% = $2.49/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 5 @ 63¢ → $2.41/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 60¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 63¢ | 5 (5 yours) | ×0.2^3 = 0.0 |
|  | 64¢ | 2 | ×0.2^4 = 0.0 |
|  | 65¢ | 50 | ×0.2^5 = 0.0 |
|  | 71¢ | 200 | ×0.2^11 = 0.0 |
|  | 90¢ | 1 | ×0.2^30 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^38 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 57.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 57.8% = $2.41/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 10 @ 33¢ → $2.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 18 (10 yours) | ×0.2^0 = 18.0 |
|  | 20¢ | 16 | ×0.2^13 = 0.0 |
|  | 1¢ | 200,450 | ×0.2^32 = 0.0 |
| | | **Σ** | **18.0** |

`yours 10.0 / Σ 18.0 = 55.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 55.5% = $2.31/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 20 @ 47¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 46¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 47¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 49¢ | 462 | ×0.2^3 = 3.7 |
|  | 52¢ | 1 | ×0.2^6 = 0.0 |
|  | 55¢ | 0 | ×0.2^9 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^52 = 0.0 |
| | | **Σ** | **8.7** |

`yours 4.0 / Σ 8.7 = 46.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 46.0% = $1.92/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 40 @ 12¢ → $1.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 87 (40 yours) | ×0.2^0 = 87.0 |
|  | 1¢ | 80,450 | ×0.2^11 = 0.0 |
| | | **Σ** | **87.0** |

`yours 40.0 / Σ 87.0 = 46.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 46.0% = $1.92/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 5 @ 19¢ → $1.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 19¢ | 5 (5 yours) | ×0.2^4 = 0.0 |
|  | 3¢ | 110 | ×0.2^20 = 0.0 |
|  | 1¢ | 200,200 | ×0.2^22 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 44.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 44.4% = $1.71/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 20 @ 84¢ → $1.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 83¢ | 5 | ×0.2^0 = 5.0 |
| ▶ | 84¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 98¢ | 60,376 | ×0.2^15 = 0.0 |
| | | **Σ** | **9.0** |

`yours 4.0 / Σ 9.0 = 44.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 44.4% = $1.85/day`  

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
<details><summary><code>dccc-measles-us-2026-12-31-gt3000</code> BUY 10 @ 78¢ → $1.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 77¢ | 53 | ×0.25^1 = 13.2 |
|  | 75¢ | 209 | ×0.25^3 = 3.3 |
|  | 50¢ | 10 | ×0.25^28 = 0.0 |
|  | 1¢ | 10,200 | ×0.25^77 = 0.0 |
| | | **Σ** | **26.5** |

`yours 10.0 / Σ 26.5 = 37.7%`  
`$50 ÷ 6 ÷ 2 = $4.17 × 37.7% = $1.57/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `dccc-measles-us-2026-12-31-gt3000` ← this one
2. `dccc-measles-us-2026-12-31-gt3500`
3. `dccc-measles-us-2026-12-31-gt4000`
4. `dccc-measles-us-2026-12-31-gt4500`
5. `dccc-measles-us-2026-12-31-gt5000`
6. `dccc-measles-us-2026-12-31-gt7500`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 18¢ → $1.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 24 (10 yours) | ×0.2^0 = 24.0 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **26.6** |

`yours 10.0 / Σ 26.6 = 37.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.6% = $1.44/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 80¢ → $1.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 79¢ | 85 | ×0.2^1 = 17.0 |
|  | 78¢ | 4 | ×0.2^2 = 0.2 |
|  | 76¢ | 4 | ×0.2^4 = 0.0 |
|  | 72¢ | 0 | ×0.2^8 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^78 = 0.0 |
| | | **Σ** | **27.2** |

`yours 10.0 / Σ 27.2 = 36.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 36.8% = $1.53/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 30 @ 13¢ → $1.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 45 (30 yours) | ×0.2^0 = 45.0 |
|  | 14¢ | 188 | ×0.2^1 = 37.6 |
|  | 20¢ | 1 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^37 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^85 = 0.0 |
| | | **Σ** | **82.6** |

`yours 30.0 / Σ 82.6 = 36.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 36.3% = $1.51/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 80 @ 34¢ → $1.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 40¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 34¢ | 80 (80 yours) | ×0.2^6 = 0.0 |
|  | 10¢ | 150 | ×0.2^30 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^38 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 33.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 33.9% = $1.41/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 15 @ 38¢ → $1.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 43¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 38¢ | 15 (15 yours) | ×0.2^5 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^41 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 32.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 32.4% = $1.35/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 20 @ 7¢ → $1.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 78 (20 yours) | ×0.2^0 = 78.3 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 98¢ | 60,305 | ×0.2^91 = 0.0 |
| | | **Σ** | **78.3** |

`yours 20.0 / Σ 78.3 = 25.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 25.5% = $1.06/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-05 | ~$33.74 | $31.46 | 93% |
| 2026-08-04 | ~$67.52 | $53.94 | 80% |
| 2026-08-03 | ~$65.16 | $44.81 | 69% |

Biggest gaps on 2026-08-05: `opdc-mcconnell-resign-2026-11-02` (est ~$1.91 → got $0.30), `scc-senate-gop-2026-11-03-51` (est ~$2.87 → got $2.08), `ewc-usgub-ca-2026-11-03-stehil` (est ~$0.75 → got $0.00)

_2026-08-06 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,384 resting) | ~44.4% | ~$11.11 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,628 resting) | ~42.0% | ~$10.49 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (613,373 resting) | ~10.6% | ~$7.98 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,601 resting) | ~25.6% | ~$6.39 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,303 resting) | ~6.5% | ~$4.87 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (44,524 resting) | ~13.7% | ~$3.42 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (156,362 resting) | ~3.8% | ~$2.88 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (141,904 resting) | ~3.6% | ~$2.70 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (88,021 resting) | ~3.4% | ~$2.51 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (277,809 resting) | ~3.3% | ~$2.49 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (67,846 resting) | ~2.2% | ~$1.67 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (60,774 resting) | ~1.4% | ~$1.06 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,627.01 |
| Pending | $83.67 |
| Skipped | $1.41 |
| **Total earned** | **$1,712.09** |

1702 reward rows · 35 days with rewards · 363 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-06 ⚠️ multi-day pending bucket | $52.21 | `███████` |
| 2026-08-05 | $31.46 | `████` |
| 2026-08-04 | $53.94 | `███████` |
| 2026-08-03 | $44.81 | `██████` |
| 2026-08-02 | $14.05 | `██` |
| 2026-08-01 | $52.30 | `███████` |
| 2026-07-31 | $67.96 | `█████████` |
| 2026-07-30 | $20.67 | `███` |
| 2026-07-29 | $53.60 | `███████` |
| 2026-07-28 | $79.65 | `██████████` |
| 2026-07-27 | $125.34 | `████████████████` |
| 2026-07-26 | $153.80 | `████████████████████` |
| 2026-07-25 | $125.69 | `████████████████` |
| 2026-07-24 | $135.19 | `██████████████████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $248.77 | `███` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $74.36 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `opdc-mcconnell-resign-2026-11-02` | $47.82 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `apdc-jerpowgov-2026-12-31` | $42.68 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.92 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.02 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `scc-hrep-rep-2026-11-03-gte200` | $25.65 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-08 12:31 AM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-07 10:24 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-07 9:26 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-07 9:17 PM ET | ✅ ok | 1702 | $1712.09 |
| 2026-08-07 9:03 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 7:51 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 6:57 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 5:58 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 5:03 PM ET | ✅ ok | 1676 | $1659.88 |
| 2026-08-07 4:03 PM ET | ✅ ok | 1676 | $1659.88 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
