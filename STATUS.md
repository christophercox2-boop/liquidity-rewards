# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-10 9:48 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$333.89/day estimated (ceiling, not promise — details below)

**Earned:** $1,827.20 lifetime ($1,771.01 paid). Last three recorded days — 2026-08-08: **$54.78** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-07: **$60.33** · 2026-08-06: **$52.21** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — SELL at the best price, ~$22.32/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$19.62/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$16.08/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$333.89/day (~$13.91/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ussewc-usse-fl-2026-11-03-rep` | BUY | 77.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,290 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 71.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (80,200 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 55.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (80,765 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 19.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.0% of bid side (85,729 resting ≥ 5,000 ✓) ≈ $4.13/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~98.0% of bid side (80,560 resting ≥ 5,000 ✓) ≈ $4.08/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~97.1% of bid side (50,558 resting ≥ 5,000 ✓) ≈ $3.73/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 12.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~93.5% of bid side (5,785 resting ≥ 2,000 ✓) ≈ $11.68/day |
| `scc-senate-gop-2026-11-03-53` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~88.2% of bid side (10,687 resting ≥ 5,000 ✓) ≈ $3.39/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 16.0¢ | 34 | 0 | $25.00 | ✅ scoring — ~82.3% of ask side (4,306 resting ≥ 2,000 ✓) ≈ $10.29/day |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 31.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 43.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | SELL | 45.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-rep` | BUY | 83.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,390 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | SELL | 35.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-wv-2026-11-03-dem` | SELL | 33.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 78.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,340 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ri-2026-11-03-dem` | BUY | 87.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,390 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 37.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-nj-2026-11-03-dem` | BUY | 89.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,390 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-dem` | SELL | 41.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,365 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 36.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,405 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-fl-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-mt-2026-11-03-setbod` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $2.98/day (pool ÷ 3 markets) |
| `ussewc-usse-va-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 13.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~70.0% of bid side (51,110 resting ≥ 5,000 ✓) ≈ $2.69/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 42.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~67.7% of ask side (62,857 resting ≥ 5,000 ✓) ≈ $2.82/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 15.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~67.6% of ask side (113,514 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 13 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 98.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (2,310 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| …and 194 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ussewc-usse-fl-2026-11-03-rep</code> BUY 40 @ 77¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 50¢ | 50 | ×0.1^27 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^76 = 0.0 |
| | | **Σ** | **40.0** |

`yours 40.0 / Σ 40.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem`
2. `ussewc-usse-fl-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 10 @ 71¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 71¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 64¢ | 0 | ×0.2^7 = 0.0 |
|  | 3¢ | 49 | ×0.2^68 = 0.0 |
|  | 2¢ | 79,941 | ×0.2^69 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 10 @ 10¢ → $4.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 3¢ | 100 | ×0.2^7 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^8 = 0.2 |
| | | **Σ** | **10.2** |

`yours 10.0 / Σ 10.2 = 98.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 98.0% = $4.08/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 5 @ 9¢ → $3.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 1¢ | 50,553 | ×0.2^8 = 0.1 |
| | | **Σ** | **5.1** |

`yours 5.0 / Σ 5.1 = 97.1%`  
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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 20 @ 12¢ → $11.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 20 (20 yours) | ×0.1^0 = 20.0 |
|  | 11¢ | 6 | ×0.1^1 = 0.6 |
|  | 10¢ | 80 | ×0.1^2 = 0.8 |
|  | 6¢ | 30 | ×0.1^6 = 0.0 |
|  | 5¢ | 99 | ×0.1^7 = 0.0 |
|  | 3¢ | 100 | ×0.1^9 = 0.0 |
|  | 1¢ | 5,450 | ×0.1^11 = 0.0 |
| | | **Σ** | **21.4** |

`yours 20.0 / Σ 21.4 = 93.5%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 93.5% = $11.68/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 34 @ 16¢ → $10.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 34 (34 yours) | ×0.1^0 = 34.0 |
|  | 17¢ | 73 | ×0.1^1 = 7.3 |
|  | 22¢ | 56 | ×0.1^6 = 0.0 |
|  | 23¢ | 30 | ×0.1^7 = 0.0 |
|  | 24¢ | 99 | ×0.1^8 = 0.0 |
|  | 35¢ | 101 | ×0.1^19 = 0.0 |
|  | 99¢ | 3,913 | ×0.1^83 = 0.0 |
| | | **Σ** | **41.3** |

`yours 34.0 / Σ 41.3 = 82.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 82.3% = $10.29/day`  

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 40 @ 31¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 31¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 32¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^68 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 40 @ 43¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 44¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^56 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> SELL 40 @ 45¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 46¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^54 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-rep</code> BUY 40 @ 83¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 83¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 82¢ | 100 | ×0.1^1 = 10.0 |
|  | 50¢ | 50 | ×0.1^33 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^82 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem`
2. `ussewc-usse-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> SELL 40 @ 35¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 36¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^64 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wv-2026-11-03-dem</code> SELL 40 @ 33¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 34¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^66 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wv-2026-11-03-dem` ← this one
2. `ussewc-usse-wv-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 40 @ 78¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 77¢ | 100 | ×0.1^1 = 10.0 |
|  | 1¢ | 2,200 | ×0.1^77 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ri-2026-11-03-dem</code> BUY 40 @ 87¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 86¢ | 100 | ×0.1^1 = 10.0 |
|  | 50¢ | 50 | ×0.1^37 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^86 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ri-2026-11-03-dem` ← this one
2. `ussewc-usse-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 37¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 38¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^62 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nj-2026-11-03-dem</code> BUY 40 @ 89¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 88¢ | 100 | ×0.1^1 = 10.0 |
|  | 49¢ | 50 | ×0.1^40 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^88 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nj-2026-11-03-dem` ← this one
2. `ussewc-usse-nj-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-dem</code> SELL 40 @ 41¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 41¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 42¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^58 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem` ← this one
2. `ussewc-usse-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 36¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 36¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 37¢ | 100 | ×0.1^1 = 10.0 |
|  | 51¢ | 40 | ×0.1^15 = 0.0 |
|  | 99¢ | 2,225 | ×0.1^63 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-fl-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem` ← this one
2. `ussewc-usse-fl-2026-11-03-rep`

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
<details><summary><code>ussewc-usse-ar-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem`
2. `ussewc-usse-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem` ← this one
2. `ussewc-usse-va-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 20 @ 13¢ → $2.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 11¢ | 45 | ×0.2^2 = 1.8 |
|  | 10¢ | 845 | ×0.2^3 = 6.8 |
|  | 2¢ | 50,000 | ×0.2^11 = 0.0 |
| | | **Σ** | **28.6** |

`yours 20.0 / Σ 28.6 = 70.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 70.0% = $2.69/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 21 @ 42¢ → $2.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 31 (21 yours) | ×0.2^0 = 31.0 |
|  | 50¢ | 100 | ×0.2^8 = 0.0 |
|  | 52¢ | 1 | ×0.2^10 = 0.0 |
|  | 64¢ | 0 | ×0.2^22 = 0.0 |
|  | 72¢ | 0 | ×0.2^30 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^56 = 0.0 |
| | | **Σ** | **31.0** |

`yours 21.0 / Σ 31.0 = 67.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 67.7% = $2.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 8 @ 15¢ → $2.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 12 (8 yours) | ×0.2^0 = 12.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^82 = 0.0 |
| | | **Σ** | **12.3** |

`yours 8.3 / Σ 12.3 = 67.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.6% = $2.60/day`  

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
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 40 @ 98¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 98¢ | 60 (40 yours) | ×0.1^0 = 60.0 |
|  | 50¢ | 50 | ×0.1^48 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^97 = 0.0 |
| | | **Σ** | **60.0** |

`yours 40.0 / Σ 60.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

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
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (249,260 resting) | ~29.8% | ~$22.32 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (60,885 resting) | ~26.2% | ~$19.62 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,778 resting) | ~64.3% | ~$16.08 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,693 resting) | ~61.5% | ~$15.38 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,851 resting) | ~58.8% | ~$14.70 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (45,734 resting) | ~57.3% | ~$14.32 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (375,786 resting) | ~18.9% | ~$14.21 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,213 resting) | ~6.3% | ~$4.74 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (84,674 resting) | ~13.0% | ~$3.25 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (63,398 resting) | ~43.6% | ~$2.73 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (87,042 resting) | ~3.2% | ~$2.41 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (191,281 resting) | ~2.9% | ~$2.21 |

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
| 2026-08-10 9:48 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 8:02 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 6:38 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 4:53 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 2:44 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:58 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:28 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:24 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:19 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:17 AM ET | ✅ ok | 1783 | $1827.20 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
