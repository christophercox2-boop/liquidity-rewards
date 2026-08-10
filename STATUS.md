# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-10 12:28 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$381.33/day estimated (ceiling, not promise — details below)

**Earned:** $1,827.20 lifetime ($1,771.01 paid). Last three recorded days — 2026-08-08: **$54.78** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-07: **$60.33** · 2026-08-06: **$52.21** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — SELL at the best price, ~$41.24/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$32.56/day), `apdc-jerpowgov-2026-08-31` (~$15.67/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$381.33/day (~$15.89/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,000 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,000 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (200,548 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (113,586 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 19.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.0% of bid side (85,729 resting ≥ 5,000 ✓) ≈ $4.13/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 21.0¢ | 6 | 0 | $25.00 | ✅ scoring — ~98.4% of ask side (4,220 resting ≥ 2,000 ✓) ≈ $12.31/day |
| `ussewc-usse-mt-2026-11-03-rep` | BUY | 54.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~97.6% of bid side (4,190 resting ≥ 2,000 ✓) ≈ $4.07/day (pool ÷ 3 markets) |
| `ussewc-usse-nm-2026-11-03-dem` | BUY | 51.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~96.4% of bid side (2,190 resting ≥ 2,000 ✓) ≈ $6.02/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $5.95/day (pool ÷ 2 markets) |
| `ussewc-usse-mt-2026-11-03-setbod` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $3.97/day (pool ÷ 3 markets) |
| `ussewc-usse-sd-2026-11-03-briben` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (2,100 resting ≥ 2,000 ✓) ≈ $5.95/day (pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~94.1% of ask side (2,125 resting ≥ 2,000 ✓) ≈ $5.88/day (pool ÷ 2 markets) |
| `ussewc-usse-nj-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~94.1% of ask side (2,125 resting ≥ 2,000 ✓) ≈ $5.88/day (pool ÷ 2 markets) |
| `ussewc-usse-co-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~94.1% of ask side (2,125 resting ≥ 2,000 ✓) ≈ $5.88/day (pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~94.1% of ask side (2,125 resting ≥ 2,000 ✓) ≈ $5.88/day (pool ÷ 2 markets) |
| `ussewc-usse-fl-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~94.1% of ask side (2,125 resting ≥ 2,000 ✓) ≈ $5.88/day (pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~94.1% of ask side (2,125 resting ≥ 2,000 ✓) ≈ $5.88/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~94.1% of ask side (2,125 resting ≥ 2,000 ✓) ≈ $5.88/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~94.1% of ask side (2,125 resting ≥ 2,000 ✓) ≈ $5.88/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~94.1% of ask side (2,125 resting ≥ 2,000 ✓) ≈ $5.88/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~88.2% of bid side (10,712 resting ≥ 5,000 ✓) ≈ $3.39/day (pool ÷ 13 markets) |
| `ussewc-usse-ar-2026-11-03-rep` | BUY | 51.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~87.0% of bid side (2,190 resting ≥ 2,000 ✓) ≈ $5.43/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | BUY | 51.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~87.0% of bid side (2,190 resting ≥ 2,000 ✓) ≈ $5.43/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 46.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (2,175 resting ≥ 2,000 ✓) ≈ $5.21/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-rep` | BUY | 53.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~82.7% of bid side (4,240 resting ≥ 2,000 ✓) ≈ $5.17/day (pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-dem` | SELL | 44.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,165 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | BUY | 62.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,140 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-dem` | BUY | 53.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,140 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~80.0% of ask side (117,890 resting ≥ 5,000 ✓) ≈ $3.08/day (pool ÷ 13 markets) |
| `ussewc-usse-nj-2026-11-03-dem` | BUY | 55.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,190 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| …and 194 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem`
2. `ussewc-usse-ms-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 2 @ 19¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 2 (2 yours) | ×0.2^0 = 2.0 |
|  | 5¢ | 115 | ×0.2^14 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^18 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 20 @ 16¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 23¢ | 100 | ×0.2^7 = 0.0 |
|  | 26¢ | 0 | ×0.2^10 = 0.0 |
|  | 50¢ | 64 | ×0.2^34 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^81 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 1 @ 19¢ → $4.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 100 | ×0.2^11 = 0.0 |
|  | 7¢ | 81 | ×0.2^12 = 0.0 |
|  | 3¢ | 5,247 | ×0.2^16 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.0% = $4.13/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 6 @ 21¢ → $12.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 6 (6 yours) | ×0.1^0 = 6.4 |
|  | 23¢ | 10 | ×0.1^2 = 0.1 |
|  | 26¢ | 94 | ×0.1^5 = 0.0 |
|  | 29¢ | 18 | ×0.1^8 = 0.0 |
|  | 32¢ | 30 | ×0.1^11 = 0.0 |
|  | 34¢ | 99 | ×0.1^13 = 0.0 |
|  | 35¢ | 101 | ×0.1^14 = 0.0 |
|  | 99¢ | 3,862 | ×0.1^78 = 0.0 |
| | | **Σ** | **6.5** |

`yours 6.4 / Σ 6.5 = 98.4%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 98.4% = $12.31/day`  

</details>
<details><summary><code>ussewc-usse-mt-2026-11-03-rep</code> BUY 40 @ 54¢ → $4.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 54¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 52¢ | 100 | ×0.1^2 = 1.0 |
|  | 48¢ | 50 | ×0.1^6 = 0.0 |
|  | 1¢ | 4,000 | ×0.1^53 = 0.0 |
| | | **Σ** | **41.0** |

`yours 40.0 / Σ 41.0 = 97.6%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 97.6% = $4.07/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `ussewc-usse-mt-2026-11-03-dem`
2. `ussewc-usse-mt-2026-11-03-rep` ← this one
3. `ussewc-usse-mt-2026-11-03-setbod`

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-dem</code> BUY 40 @ 51¢ → $6.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 49¢ | 150 | ×0.1^2 = 1.5 |
|  | 1¢ | 2,000 | ×0.1^50 = 0.0 |
| | | **Σ** | **41.5** |

`yours 40.0 / Σ 41.5 = 96.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 96.4% = $6.02/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem` ← this one
2. `ussewc-usse-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $5.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (2,000 yours) | ×0.1^0 = 2,100.0 |
| | | **Σ** | **2,100.0** |

`yours 2,000.0 / Σ 2,100.0 = 95.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 95.2% = $5.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-mt-2026-11-03-setbod</code> BUY 2,000 @ 1¢ → $3.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (2,000 yours) | ×0.1^0 = 2,100.0 |
| | | **Σ** | **2,100.0** |

`yours 2,000.0 / Σ 2,100.0 = 95.2%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 95.2% = $3.97/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `ussewc-usse-mt-2026-11-03-dem`
2. `ussewc-usse-mt-2026-11-03-rep`
3. `ussewc-usse-mt-2026-11-03-setbod` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sd-2026-11-03-briben</code> BUY 2,000 @ 1¢ → $5.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,100 (2,000 yours) | ×0.1^0 = 2,100.0 |
| | | **Σ** | **2,100.0** |

`yours 2,000.0 / Σ 2,100.0 = 95.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 95.2% = $5.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sd-2026-11-03-briben` ← this one
2. `ussewc-usse-sd-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $5.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,125 (2,000 yours) | ×0.1^0 = 2,125.0 |
| | | **Σ** | **2,125.0** |

`yours 2,000.0 / Σ 2,125.0 = 94.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.1% = $5.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem`
2. `ussewc-usse-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nj-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $5.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,125 (2,000 yours) | ×0.1^0 = 2,125.0 |
| | | **Σ** | **2,125.0** |

`yours 2,000.0 / Σ 2,125.0 = 94.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.1% = $5.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nj-2026-11-03-dem` ← this one
2. `ussewc-usse-nj-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-co-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $5.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,125 (2,000 yours) | ×0.1^0 = 2,125.0 |
| | | **Σ** | **2,125.0** |

`yours 2,000.0 / Σ 2,125.0 = 94.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.1% = $5.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem` ← this one
2. `ussewc-usse-co-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $5.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,125 (2,000 yours) | ×0.1^0 = 2,125.0 |
| | | **Σ** | **2,125.0** |

`yours 2,000.0 / Σ 2,125.0 = 94.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.1% = $5.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem`
2. `ussewc-usse-la-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-fl-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $5.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,125 (2,000 yours) | ×0.1^0 = 2,125.0 |
| | | **Σ** | **2,125.0** |

`yours 2,000.0 / Σ 2,125.0 = 94.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.1% = $5.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem`
2. `ussewc-usse-fl-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $5.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,125 (2,000 yours) | ×0.1^0 = 2,125.0 |
| | | **Σ** | **2,125.0** |

`yours 2,000.0 / Σ 2,125.0 = 94.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.1% = $5.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $5.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,125 (2,000 yours) | ×0.1^0 = 2,125.0 |
| | | **Σ** | **2,125.0** |

`yours 2,000.0 / Σ 2,125.0 = 94.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.1% = $5.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $5.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,125 (2,000 yours) | ×0.1^0 = 2,125.0 |
| | | **Σ** | **2,125.0** |

`yours 2,000.0 / Σ 2,125.0 = 94.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.1% = $5.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem` ← this one
2. `ussewc-usse-or-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $5.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,125 (2,000 yours) | ×0.1^0 = 2,125.0 |
| | | **Σ** | **2,125.0** |

`yours 2,000.0 / Σ 2,125.0 = 94.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.1% = $5.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 1 @ 13¢ → $3.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 3 | ×0.2^6 = 0.0 |
|  | 6¢ | 10,457 | ×0.2^7 = 0.1 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.2% = $3.39/day`  

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
<details><summary><code>ussewc-usse-ar-2026-11-03-rep</code> BUY 40 @ 51¢ → $5.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 50¢ | 50 | ×0.1^1 = 5.0 |
|  | 49¢ | 100 | ×0.1^2 = 1.0 |
|  | 1¢ | 2,000 | ×0.1^50 = 0.0 |
| | | **Σ** | **46.0** |

`yours 40.0 / Σ 46.0 = 87.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 87.0% = $5.43/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem`
2. `ussewc-usse-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> BUY 40 @ 51¢ → $5.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 50¢ | 50 | ×0.1^1 = 5.0 |
|  | 49¢ | 100 | ×0.1^2 = 1.0 |
|  | 1¢ | 2,000 | ×0.1^50 = 0.0 |
| | | **Σ** | **46.0** |

`yours 40.0 / Σ 46.0 = 87.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 87.0% = $5.43/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 50 @ 46¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 47¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,025 | ×0.1^53 = 0.0 |
| | | **Σ** | **60.0** |

`yours 50.0 / Σ 60.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-rep</code> BUY 50 @ 53¢ → $5.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 53¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 52¢ | 100 | ×0.1^1 = 10.0 |
|  | 51¢ | 40 | ×0.1^2 = 0.4 |
|  | 50¢ | 50 | ×0.1^3 = 0.1 |
|  | 1¢ | 4,000 | ×0.1^52 = 0.0 |
| | | **Σ** | **60.5** |

`yours 50.0 / Σ 60.5 = 82.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 82.7% = $5.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem`
2. `ussewc-usse-ms-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-dem</code> SELL 40 @ 44¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 44¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 45¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,025 | ×0.1^55 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem` ← this one
2. `ussewc-usse-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> BUY 40 @ 62¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 62¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 61¢ | 100 | ×0.1^1 = 10.0 |
|  | 1¢ | 2,000 | ×0.1^61 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-dem</code> BUY 40 @ 53¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 53¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 52¢ | 100 | ×0.1^1 = 10.0 |
|  | 1¢ | 2,000 | ×0.1^52 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem` ← this one
2. `ussewc-usse-or-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $3.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 25 (20 yours) | ×0.2^0 = 25.0 |
|  | 22¢ | 100 | ×0.2^18 = 0.0 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **25.0** |

`yours 20.0 / Σ 25.0 = 80.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 80.0% = $3.08/day`  

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
<details><summary><code>ussewc-usse-nj-2026-11-03-dem</code> BUY 40 @ 55¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 55¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 54¢ | 100 | ×0.1^1 = 10.0 |
|  | 49¢ | 50 | ×0.1^6 = 0.0 |
|  | 1¢ | 2,000 | ×0.1^54 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nj-2026-11-03-dem` ← this one
2. `ussewc-usse-nj-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-07 | ~$116.96 | $60.33 | 52% |
| 2026-08-06 | ~$60.78 | $52.21 | 86% |
| 2026-08-05 | ~$33.74 | $31.46 | 93% |

Biggest gaps on 2026-08-07: `opdc-mcconnell-resign-2026-11-02` (est ~$17.07 → got $5.10), `scc-hrep-rep-2026-11-03-gte205` (est ~$4.14 → got $0.00), `scc-hrep-rep-2026-11-03-gte195` (est ~$5.07 → got $0.94)

_2026-08-08 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (219,998 resting) | ~55.0% | ~$41.24 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (61,582 resting) | ~43.4% | ~$32.56 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,687 resting) | ~62.7% | ~$15.67 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (78,023 resting) | ~61.4% | ~$15.35 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,603 resting) | ~60.0% | ~$15.01 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,693 resting) | ~33.1% | ~$8.28 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (39,542 resting) | ~33.0% | ~$8.24 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,072 resting) | ~6.7% | ~$5.04 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (189,092 resting) | ~5.0% | ~$3.77 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (86,897 resting) | ~12.4% | ~$3.10 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (276,853 resting) | ~3.4% | ~$2.56 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (67,393 resting) | ~40.3% | ~$2.52 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,771.01 |
| Pending | $54.78 |
| Skipped | $1.41 |
| **Total earned** | **$1,827.20** |

1783 reward rows · 37 days with rewards · 377 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-08 ⚠️ multi-day pending bucket | $54.78 | `███████` |
| 2026-08-07 | $60.33 | `████████` |
| 2026-08-06 | $52.21 | `███████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $363.88 | `█████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $86.00 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `opdc-mcconnell-resign-2026-11-02` | $56.71 |
| `apdc-jerpowgov-2026-12-31` | $56.12 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.92 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `scc-hrep-rep-2026-11-03-gte200` | $32.74 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-10 12:28 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:24 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:19 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:17 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:07 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:04 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:03 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:02 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:01 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-09 11:59 PM ET | ✅ ok | 1783 | $1827.20 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
