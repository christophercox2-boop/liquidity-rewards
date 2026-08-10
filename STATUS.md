# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-10 8:02 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$286.45/day estimated (ceiling, not promise — details below)

**Earned:** $1,827.20 lifetime ($1,771.01 paid). Last three recorded days — 2026-08-08: **$54.78** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-07: **$60.33** · 2026-08-06: **$52.21** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — SELL at the best price, ~$24.58/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$19.13/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$17.03/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$286.45/day (~$11.94/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 55.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (80,765 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 19.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.0% of bid side (85,729 resting ≥ 5,000 ✓) ≈ $4.13/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 20.0¢ | 16 | 0 | $25.00 | ✅ scoring — ~94.8% of ask side (4,305 resting ≥ 2,000 ✓) ≈ $11.85/day |
| `scc-senate-gop-2026-11-03-53` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~88.2% of bid side (10,712 resting ≥ 5,000 ✓) ≈ $3.39/day (pool ÷ 13 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 74.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,340 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-wv-2026-11-03-dem` | SELL | 39.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 45.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 89.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,390 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-nj-2026-11-03-dem` | BUY | 77.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,390 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | SELL | 41.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-rep` | BUY | 77.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,390 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 41.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ri-2026-11-03-dem` | BUY | 79.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,390 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 69.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~76.9% of bid side (80,195 resting ≥ 5,000 ✓) ≈ $3.21/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 63.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~76.9% of bid side (80,468 resting ≥ 5,000 ✓) ≈ $3.20/day (pool ÷ 12 markets) |
| `ussewc-usse-va-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-mt-2026-11-03-setbod` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $2.98/day (pool ÷ 3 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~68.1% of ask side (2,935 resting ≥ 2,000 ✓) ≈ $4.26/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | BUY | 77.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (2,260 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 82.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (50,501 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~64.5% of ask side (113,497 resting ≥ 5,000 ✓) ≈ $2.48/day (pool ÷ 13 markets) |
| `ussewc-usse-al-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~63.7% of ask side (3,138 resting ≥ 2,000 ✓) ≈ $3.98/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 77.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~61.6% of bid side (80,583 resting ≥ 5,000 ✓) ≈ $2.57/day (pool ÷ 12 markets) |
| `ussewc-usse-nm-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~58.9% of ask side (3,393 resting ≥ 2,000 ✓) ≈ $3.68/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~56.0% of bid side (3,569 resting ≥ 2,000 ✓) ≈ $3.50/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~56.0% of bid side (3,570 resting ≥ 2,000 ✓) ≈ $3.50/day (pool ÷ 2 markets) |
| `pic-congress-trump-2026-12-31` | BUY | 9.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~54.8% of bid side (7,013 resting ≥ 2,000 ✓) ≈ $6.85/day |
| …and 191 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 10 @ 55¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 55¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 50¢ | 30 | ×0.2^5 = 0.0 |
|  | 49¢ | 165 | ×0.2^6 = 0.0 |
|  | 24¢ | 170 | ×0.2^31 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^53 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.8% = $4.16/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 16 @ 20¢ → $11.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 16 (16 yours) | ×0.1^0 = 16.4 |
|  | 21¢ | 6 | ×0.1^1 = 0.6 |
|  | 22¢ | 18 | ×0.1^2 = 0.2 |
|  | 23¢ | 110 | ×0.1^3 = 0.1 |
|  | 24¢ | 149 | ×0.1^4 = 0.0 |
|  | 35¢ | 101 | ×0.1^15 = 0.0 |
|  | 99¢ | 3,905 | ×0.1^79 = 0.0 |
| | | **Σ** | **17.3** |

`yours 16.4 / Σ 17.3 = 94.8%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 94.8% = $11.85/day`  

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
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 40 @ 74¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 73¢ | 100 | ×0.1^1 = 10.0 |
|  | 1¢ | 2,200 | ×0.1^73 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wv-2026-11-03-dem</code> SELL 40 @ 39¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 39¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 40¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^60 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wv-2026-11-03-dem` ← this one
2. `ussewc-usse-wv-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 45¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 46¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^54 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 40 @ 89¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 88¢ | 100 | ×0.1^1 = 10.0 |
|  | 50¢ | 50 | ×0.1^39 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^88 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nj-2026-11-03-dem</code> BUY 40 @ 77¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 76¢ | 100 | ×0.1^1 = 10.0 |
|  | 49¢ | 50 | ×0.1^28 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^76 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nj-2026-11-03-dem` ← this one
2. `ussewc-usse-nj-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> SELL 40 @ 41¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 41¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 42¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^58 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-rep</code> BUY 40 @ 77¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 76¢ | 100 | ×0.1^1 = 10.0 |
|  | 50¢ | 50 | ×0.1^27 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^76 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem`
2. `ussewc-usse-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 40 @ 41¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 41¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 42¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^58 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ri-2026-11-03-dem</code> BUY 40 @ 79¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 78¢ | 100 | ×0.1^1 = 10.0 |
|  | 50¢ | 50 | ×0.1^29 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^78 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ri-2026-11-03-dem` ← this one
2. `ussewc-usse-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 10 @ 69¢ → $3.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 69¢ | 13 (10 yours) | ×0.2^0 = 13.0 |
|  | 64¢ | 0 | ×0.2^5 = 0.0 |
|  | 3¢ | 49 | ×0.2^66 = 0.0 |
|  | 2¢ | 79,933 | ×0.2^67 = 0.0 |
| | | **Σ** | **13.0** |

`yours 10.0 / Σ 13.0 = 76.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 76.9% = $3.21/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 63¢ → $3.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 63¢ | 13 (10 yours) | ×0.2^0 = 13.0 |
|  | 59¢ | 5 | ×0.2^4 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^61 = 0.0 |
| | | **Σ** | **13.0** |

`yours 10.0 / Σ 13.0 = 76.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 76.9% = $3.20/day`  

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-mt-2026-11-03-setbod</code> BUY 2,000 @ 1¢ → $2.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 71.4% = $2.98/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `ussewc-usse-mt-2026-11-03-dem`
2. `ussewc-usse-mt-2026-11-03-rep`
3. `ussewc-usse-mt-2026-11-03-setbod` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,935 (2,000 yours) | ×0.1^0 = 2,935.0 |
| | | **Σ** | **2,935.0** |

`yours 2,000.0 / Σ 2,935.0 = 68.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 68.1% = $4.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> BUY 40 @ 77¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 60 (40 yours) | ×0.1^0 = 60.0 |
|  | 1¢ | 2,200 | ×0.1^76 = 0.0 |
| | | **Σ** | **60.0** |

`yours 40.0 / Σ 60.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 30 @ 82¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 45 (30 yours) | ×0.2^0 = 45.0 |
|  | 76¢ | 6 | ×0.2^6 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^80 = 0.0 |
| | | **Σ** | **45.0** |

`yours 30.0 / Σ 45.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 20 @ 16¢ → $2.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 31 (20 yours) | ×0.2^0 = 31.0 |
|  | 26¢ | 0 | ×0.2^10 = 0.0 |
|  | 50¢ | 64 | ×0.2^34 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^81 = 0.0 |
| | | **Σ** | **31.0** |

`yours 20.0 / Σ 31.0 = 64.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.5% = $2.48/day`  

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
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $3.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 3,138 (2,000 yours) | ×0.1^0 = 3,138.0 |
| | | **Σ** | **3,138.0** |

`yours 2,000.0 / Σ 3,138.0 = 63.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.7% = $3.98/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 2 @ 77¢ → $2.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 2 (2 yours) | ×0.2^0 = 2.0 |
|  | 75¢ | 31 | ×0.2^2 = 1.2 |
|  | 71¢ | 100 | ×0.2^6 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^75 = 0.0 |
| | | **Σ** | **3.2** |

`yours 2.0 / Σ 3.2 = 61.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 61.6% = $2.57/day`  

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
<details><summary><code>ussewc-usse-nm-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $3.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 3,393 (2,000 yours) | ×0.1^0 = 3,393.0 |
| | | **Σ** | **3,393.0** |

`yours 2,000.0 / Σ 3,393.0 = 58.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.9% = $3.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem` ← this one
2. `ussewc-usse-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $3.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,569 (2,000 yours) | ×0.1^0 = 3,569.0 |
| | | **Σ** | **3,569.0** |

`yours 2,000.0 / Σ 3,569.0 = 56.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 56.0% = $3.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $3.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,570 (2,000 yours) | ×0.1^0 = 3,570.0 |
| | | **Σ** | **3,570.0** |

`yours 2,000.0 / Σ 3,570.0 = 56.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 56.0% = $3.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>pic-congress-trump-2026-12-31</code> BUY 30 @ 9¢ → $6.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 51 (30 yours) | ×0.1^0 = 50.8 |
|  | 7¢ | 80 | ×0.1^2 = 0.8 |
|  | 6¢ | 3,126 | ×0.1^3 = 3.1 |
| | | **Σ** | **54.7** |

`yours 30.0 / Σ 54.7 = 54.8%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 54.8% = $6.85/day`  

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
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (249,198 resting) | ~32.8% | ~$24.58 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (64,146 resting) | ~25.5% | ~$19.13 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,954 resting) | ~68.1% | ~$17.03 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,692 resting) | ~61.7% | ~$15.43 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,582 resting) | ~59.3% | ~$14.82 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (374,027 resting) | ~16.6% | ~$12.45 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (45,873 resting) | ~45.9% | ~$11.48 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (63,638 resting) | ~9.7% | ~$7.27 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,236 resting) | ~23.6% | ~$5.89 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (87,184 resting) | ~12.0% | ~$3.00 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (67,537 resting) | ~40.3% | ~$2.52 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (87,974 resting) | ~3.2% | ~$2.41 |

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
| 2026-08-10 8:02 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 6:38 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 4:53 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 2:44 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:58 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:28 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:24 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:19 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:17 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:07 AM ET | ✅ ok | 1783 | $1827.20 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
