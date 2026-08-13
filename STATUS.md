# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 2:50 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$301.75/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$15.94/day for 200 contracts. Runners-up: `paccc-usse-midterms-2026-11-03-dem` (~$14.63/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$13.61/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$301.75/day (~$12.57/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-me-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (500,440 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-rep` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,565 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,549 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `ussewc-usse-ks-2026-11-03-dem` | BUY | 17.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~99.9% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 26.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~99.1% of bid side (5,500 resting ≥ 5,000 ✓) ≈ $24.77/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.8% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.49/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~84.7% of bid side (140,570 resting ≥ 5,000 ✓) ≈ $3.26/day (pool ÷ 13 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (510,250 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (208,538 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-il-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (610,250 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (510,450 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | SELL | 9.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (7,175 resting ≥ 2,000 ✓) ≈ $3.33/day (pool ÷ 3 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (610,450 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (510,500 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | SELL | 3.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (130,825 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (72,444 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (610,500 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~79.9% of ask side (208,588 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~79.9% of ask side (131,025 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~79.2% of bid side (2,050 resting ≥ 2,000 ✓) ≈ $4.95/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~75.8% of bid side (6,600 resting ≥ 2,000 ✓) ≈ $4.73/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | BUY | 94.0¢ | 29 | 0 | $25.00 | ✅ scoring — ~74.4% of bid side (310,739 resting ≥ 2,000 ✓) ≈ $4.65/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 95.0¢ | 60 | 0 | $25.00 | ✅ scoring — ~70.6% of bid side (510,535 resting ≥ 2,000 ✓) ≈ $4.41/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | BUY | 95.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (500,475 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `ussewc-usse-co-2026-11-03-rep` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~66.7% of ask side (59,388 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-dem` | SELL | 8.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~66.7% of ask side (272,919 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 93.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~66.2% of bid side (500,525 resting ≥ 2,000 ✓) ≈ $4.14/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~62.0% of ask side (8,578 resting ≥ 2,000 ✓) ≈ $3.88/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.4% of ask side (65,710 resting ≥ 2,000 ✓) ≈ $3.84/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 12.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~59.9% of bid side (200,620 resting ≥ 5,000 ✓) ≈ $2.30/day (pool ÷ 13 markets) |
| …and 393 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-me-2026-11-03-dem</code> BUY 40 @ 95¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **40.0** |

`yours 40.0 / Σ 40.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem` ← this one
2. `usgubewc-usgub-me-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> SELL 40 @ 5¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 14¢ | 50 | ×0.1^9 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **40.0** |

`yours 40.0 / Σ 40.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem`
2. `usgubewc-usgub-me-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 18 @ 12¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 18 (18 yours) | ×0.2^0 = 18.0 |
|  | 1¢ | 300,531 | ×0.2^11 = 0.0 |
| | | **Σ** | **18.0** |

`yours 18.0 / Σ 18.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.84/day`  

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
<details><summary><code>ussewc-usse-ks-2026-11-03-dem</code> BUY 10 @ 17¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 12¢ | 547 | ×0.1^5 = 0.0 |
|  | 7¢ | 250 | ×0.1^10 = 0.0 |
|  | 3¢ | 50 | ×0.1^14 = 0.0 |
|  | 1¢ | 1,643 | ×0.1^16 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.9% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem` ← this one
2. `ussewc-usse-ks-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 30 @ 26¢ → $24.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 30 (30 yours) | ×0.2^0 = 30.0 |
|  | 24¢ | 7 | ×0.2^2 = 0.3 |
|  | 12¢ | 116 | ×0.2^14 = 0.0 |
|  | 2¢ | 100 | ×0.2^24 = 0.0 |
|  | 1¢ | 5,247 | ×0.2^25 = 0.0 |
| | | **Σ** | **30.3** |

`yours 30.0 / Σ 30.3 = 99.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 99.1% = $24.77/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 8 @ 9¢ → $3.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 8 (8 yours) | ×0.2^0 = 7.8 |
|  | 1¢ | 300,556 | ×0.2^8 = 0.8 |
| | | **Σ** | **8.5** |

`yours 7.8 / Σ 8.5 = 90.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 90.8% = $3.49/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 10 @ 8¢ → $3.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 2¢ | 30 | ×0.2^6 = 0.0 |
|  | 1¢ | 140,530 | ×0.2^7 = 1.8 |
| | | **Σ** | **11.8** |

`yours 10.0 / Σ 11.8 = 84.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 84.7% = $3.26/day`  

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
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> SELL 40 @ 4¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 98¢ | 208,263 | ×0.1^94 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-dem</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 600,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem` ← this one
2. `usgubewc-usgub-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> SELL 40 @ 9¢ → $3.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 99¢ | 7,125 | ×0.1^90 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 80.0% = $3.33/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 600,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 84¢ | 50 | ×0.1^11 = 0.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> SELL 40 @ 3¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 9¢ | 50 | ×0.1^6 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^95 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 40 @ 10¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 16¢ | 50 | ×0.1^6 = 0.0 |
|  | 98¢ | 65,450 | ×0.1^88 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-co-2026-11-03-dem</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 91¢ | 50 | ×0.1^4 = 0.0 |
|  | 2¢ | 600,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem` ← this one
2. `usgubewc-usgub-co-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> SELL 40 @ 5¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 8¢ | 50 | ×0.1^3 = 0.1 |
|  | 98¢ | 208,263 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 79.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 79.9% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 7¢ | 50 | ×0.1^3 = 0.1 |
|  | 98¢ | 130,700 | ×0.1^94 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 79.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 79.9% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 40 @ 95¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 93¢ | 50 | ×0.1^2 = 0.5 |
|  | 1¢ | 1,950 | ×0.1^94 = 0.0 |
| | | **Σ** | **50.5** |

`yours 40.0 / Σ 50.5 = 79.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 79.2% = $4.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $4.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 6,600 (5,000 yours) | ×0.1^0 = 6,600.0 |
| | | **Σ** | **6,600.0** |

`yours 5,000.0 / Σ 6,600.0 = 75.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.8% = $4.73/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> BUY 29 @ 94¢ → $4.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 39 (29 yours) | ×0.1^0 = 39.0 |
|  | 54¢ | 500 | ×0.1^40 = 0.0 |
|  | 2¢ | 300,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **39.0** |

`yours 29.0 / Σ 39.0 = 74.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 74.4% = $4.65/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 60 @ 95¢ → $4.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 85 (60 yours) | ×0.1^0 = 85.0 |
|  | 88¢ | 50 | ×0.1^7 = 0.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **85.0** |

`yours 60.0 / Σ 85.0 = 70.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.6% = $4.41/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> BUY 50 @ 95¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 75 (50 yours) | ×0.1^0 = 75.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-co-2026-11-03-rep</code> SELL 50 @ 7¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 75 (50 yours) | ×0.1^0 = 75.0 |
|  | 98¢ | 59,088 | ×0.1^91 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem`
2. `ussewc-usse-co-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-dem</code> SELL 50 @ 8¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 75 (50 yours) | ×0.1^0 = 75.0 |
|  | 13¢ | 50 | ×0.1^5 = 0.0 |
|  | 98¢ | 265,767 | ×0.1^90 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem` ← this one
2. `ussewc-usse-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 50 @ 93¢ → $4.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 75 (50 yours) | ×0.1^0 = 75.0 |
|  | 91¢ | 50 | ×0.1^2 = 0.5 |
|  | 2¢ | 500,200 | ×0.1^91 = 0.0 |
| | | **Σ** | **75.5** |

`yours 50.0 / Σ 75.5 = 66.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.2% = $4.14/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $3.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 97¢ | 60 | ×0.1^1 = 6.0 |
|  | 99¢ | 8,468 | ×0.1^3 = 8.5 |
| | | **Σ** | **64.5** |

`yours 40.0 / Σ 64.5 = 62.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 62.0% = $3.88/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 4¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 7¢ | 170 | ×0.1^3 = 0.2 |
|  | 98¢ | 65,250 | ×0.1^94 = 0.0 |
| | | **Σ** | **65.2** |

`yours 40.0 / Σ 65.2 = 61.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.4% = $3.84/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 40 @ 12¢ → $2.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 65 (40 yours) | ×0.2^0 = 65.0 |
|  | 10¢ | 45 | ×0.2^2 = 1.8 |
|  | 1¢ | 200,510 | ×0.2^11 = 0.0 |
| | | **Σ** | **66.8** |

`yours 40.0 / Σ 66.8 = 59.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 59.9% = $2.30/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,752 resting) | ~63.8% | ~$15.94 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,033,967 resting) | ~19.5% | ~$14.63 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,112 resting) | ~54.4% | ~$13.61 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (79,701 resting) | ~15.7% | ~$11.78 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (63,723 resting) | ~15.3% | ~$11.45 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,707 resting) | ~32.9% | ~$8.22 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (284,263 resting) | ~10.6% | ~$7.93 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (281,651 resting) | ~6.7% | ~$5.02 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (683,176 resting) | ~6.0% | ~$4.50 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (809,544 resting) | ~5.9% | ~$4.40 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,085,363 resting) | ~3.6% | ~$2.68 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,045,358 resting) | ~3.4% | ~$2.52 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $964.28 |
| Skipped | $1.41 |
| **Total earned** | **$2,853.72** |

2087 reward rows · 40 days with rewards · 480 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-11 ⚠️ multi-day pending bucket | $406.66 | `███████████████` |
| 2026-08-10 | $557.62 | `████████████████████` |
| 2026-08-09 | $62.24 | `██` |
| 2026-08-08 | $54.78 | `██` |
| 2026-08-07 | $60.33 | `██` |
| 2026-08-06 | $52.21 | `██` |
| 2026-08-05 | $31.46 | `█` |
| 2026-08-04 | $53.94 | `██` |
| 2026-08-03 | $44.81 | `██` |
| 2026-08-02 | $14.05 | `█` |
| 2026-08-01 | $52.30 | `██` |
| 2026-07-31 | $67.96 | `██` |
| 2026-07-30 | $20.67 | `█` |
| 2026-07-29 | $53.60 | `██` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $1,390.40 | `███████████████████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $107.37 |
| `apdc-alito-2026-12-31` | $106.43 |
| `opdc-mcconnell-resign-2026-11-02` | $70.72 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `pandc-anydis-2027-12-31` | $39.99 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.02 |
| `scc-hrep-rep-2026-11-03-gte200` | $38.44 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-13 2:50 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 1:11 AM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-12 11:02 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-12 9:32 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-12 8:05 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:01 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 7:05 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:06 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 5:06 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 5:01 PM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
