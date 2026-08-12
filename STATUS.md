# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-12 6:06 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$188.90/day estimated (ceiling, not promise — details below)

**Earned:** $2,447.06 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-10: **$557.62** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-09: **$62.24** · 2026-08-08: **$54.78** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — BUY at the best price, ~$21.10/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$17.41/day), `ewc-usgub-ga-2026-11-03-dem` (~$14.65/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$188.90/day (~$7.87/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 35.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (400,471 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,549 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 12.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~95.7% of bid side (200,595 resting ≥ 5,000 ✓) ≈ $3.68/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.8% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.49/day (pool ÷ 13 markets) |
| `usgubewc-usgub-ct-2026-11-03-rep` | SELL | 9.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (207,002 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (273,394 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (203,556 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (510,500 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 95.0¢ | 60 | 0 | $25.00 | ✅ scoring — ~70.6% of bid side (510,535 resting ≥ 2,000 ✓) ≈ $4.41/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 93.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (500,475 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | SELL | 3.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~58.8% of ask side (130,793 resting ≥ 2,000 ✓) ≈ $3.68/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~58.0% of ask side (208,607 resting ≥ 2,000 ✓) ≈ $3.62/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~58.0% of ask side (130,994 resting ≥ 2,000 ✓) ≈ $3.62/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~58.0% of bid side (500,469 resting ≥ 2,000 ✓) ≈ $3.62/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~57.8% of ask side (65,764 resting ≥ 2,000 ✓) ≈ $3.61/day (pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-dem` | SELL | 8.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~57.5% of ask side (273,681 resting ≥ 2,000 ✓) ≈ $3.59/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~56.3% of ask side (208,609 resting ≥ 2,000 ✓) ≈ $3.52/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~54.1% of bid side (3,700 resting ≥ 2,000 ✓) ≈ $3.38/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 1,290 | 0 | $25.00 | ✅ scoring — ~51.6% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $3.23/day (pool ÷ 2 markets) |
| `ussewc-usse-ks-2026-11-03-dem` | SELL | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~50.0% of ask side (138,276 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 7.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~47.7% of bid side (90,540 resting ≥ 5,000 ✓) ≈ $1.84/day (pool ÷ 13 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~39.6% of bid side (12,642 resting ≥ 2,000 ✓) ≈ $2.47/day (pool ÷ 2 markets) |
| `pntcbk-nba-kawleo-2026-10-23-tor` | BUY | 70.0¢ | 10 | 0 | $500.00 | ✅ scoring — ~34.8% of bid side (48,188 resting ≥ 2,500 ✓) ≈ $2.90/day (pool ÷ 30 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~32.8% of bid side (2,072 resting ≥ 2,000 ✓) ≈ $2.05/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 22.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~31.8% of ask side (91,884 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | BUY | 77.0¢ | 66 | 0 | $25.00 | ✅ scoring — ~30.6% of bid side (100,912 resting ≥ 2,000 ✓) ≈ $1.91/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 15.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~29.8% of bid side (10,409 resting ≥ 2,000 ✓) ≈ $1.86/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | SELL | 30.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~27.5% of ask side (11,052 resting ≥ 10,000 ✓) ≈ $3.44/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~27.0% of bid side (610,598 resting ≥ 2,000 ✓) ≈ $1.69/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~26.0% of bid side (510,604 resting ≥ 2,000 ✓) ≈ $1.62/day (pool ÷ 2 markets) |
| …and 380 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 21 @ 35¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 21 (21 yours) | ×0.2^0 = 21.0 |
|  | 2¢ | 400,250 | ×0.2^33 = 0.0 |
| | | **Σ** | **21.0** |

`yours 21.0 / Σ 21.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 40 @ 12¢ → $3.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 10¢ | 45 | ×0.2^2 = 1.8 |
|  | 1¢ | 200,510 | ×0.2^11 = 0.0 |
| | | **Σ** | **41.8** |

`yours 40.0 / Σ 41.8 = 95.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 95.7% = $3.68/day`  

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
<details><summary><code>usgubewc-usgub-ct-2026-11-03-rep</code> SELL 40 @ 9¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 98¢ | 199,175 | ×0.1^89 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem`
2. `usgubewc-usgub-ct-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> SELL 40 @ 10¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 98¢ | 265,567 | ×0.1^88 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 40 @ 10¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 98¢ | 195,750 | ×0.1^88 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 500,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 60 @ 95¢ → $4.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 85 (60 yours) | ×0.1^0 = 85.0 |
|  | 2¢ | 500,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **85.0** |

`yours 60.0 / Σ 85.0 = 70.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.6% = $4.41/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 50 @ 93¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 75 (50 yours) | ×0.1^0 = 75.0 |
|  | 2¢ | 500,200 | ×0.1^91 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> SELL 40 @ 3¢ → $3.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 68 (40 yours) | ×0.1^0 = 68.0 |
|  | 98¢ | 130,500 | ×0.1^95 = 0.0 |
| | | **Σ** | **68.0** |

`yours 40.0 / Σ 68.0 = 58.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.8% = $3.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> SELL 40 @ 4¢ → $3.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 69 (40 yours) | ×0.1^0 = 69.0 |
|  | 98¢ | 208,313 | ×0.1^94 = 0.0 |
| | | **Σ** | **69.0** |

`yours 40.0 / Σ 69.0 = 58.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.0% = $3.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $3.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 69 (40 yours) | ×0.1^0 = 69.0 |
|  | 98¢ | 130,700 | ×0.1^94 = 0.0 |
| | | **Σ** | **69.0** |

`yours 40.0 / Σ 69.0 = 58.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.0% = $3.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-dem</code> BUY 40 @ 95¢ → $3.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 69 (40 yours) | ×0.1^0 = 69.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **69.0** |

`yours 40.0 / Σ 69.0 = 58.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.0% = $3.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem` ← this one
2. `usgubewc-usgub-me-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 4¢ → $3.61/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 69 (40 yours) | ×0.1^0 = 69.0 |
|  | 7¢ | 170 | ×0.1^3 = 0.2 |
|  | 9¢ | 50 | ×0.1^5 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^94 = 0.0 |
| | | **Σ** | **69.2** |

`yours 40.0 / Σ 69.2 = 57.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.8% = $3.61/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-dem</code> SELL 50 @ 8¢ → $3.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 87 (50 yours) | ×0.1^0 = 87.0 |
|  | 98¢ | 265,817 | ×0.1^90 = 0.0 |
| | | **Σ** | **87.0** |

`yours 50.0 / Σ 87.0 = 57.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.5% = $3.59/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem` ← this one
2. `ussewc-usse-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> SELL 40 @ 5¢ → $3.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 71 (40 yours) | ×0.1^0 = 71.0 |
|  | 98¢ | 208,313 | ×0.1^93 = 0.0 |
| | | **Σ** | **71.0** |

`yours 40.0 / Σ 71.0 = 56.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 56.3% = $3.52/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $3.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,700 (2,000 yours) | ×0.1^0 = 3,700.0 |
| | | **Σ** | **3,700.0** |

`yours 2,000.0 / Σ 3,700.0 = 54.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 54.1% = $3.38/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 1,290 @ 1¢ → $3.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,500 (1,290 yours) | ×0.1^0 = 2,500.0 |
| | | **Σ** | **2,500.0** |

`yours 1,290.0 / Σ 2,500.0 = 51.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 51.6% = $3.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ks-2026-11-03-dem</code> SELL 10 @ 13¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 20 (10 yours) | ×0.1^0 = 20.0 |
|  | 98¢ | 130,500 | ×0.1^85 = 0.0 |
| | | **Σ** | **20.0** |

`yours 10.0 / Σ 20.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem` ← this one
2. `ussewc-usse-ks-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 10 @ 7¢ → $1.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 12 (10 yours) | ×0.2^0 = 12.0 |
|  | 5¢ | 79 | ×0.2^2 = 3.2 |
|  | 1¢ | 90,449 | ×0.2^6 = 5.8 |
| | | **Σ** | **20.9** |

`yours 10.0 / Σ 20.9 = 47.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.7% = $1.84/day`  

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
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $2.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,642 (5,000 yours) | ×0.1^0 = 12,642.0 |
| | | **Σ** | **12,642.0** |

`yours 5,000.0 / Σ 12,642.0 = 39.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 39.6% = $2.47/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>pntcbk-nba-kawleo-2026-10-23-tor</code> BUY 10 @ 70¢ → $2.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 70¢ | 10 (10 yours) | ×0.35^0 = 10.0 |
|  | 69¢ | 26 | ×0.35^1 = 9.1 |
|  | 68¢ | 29 | ×0.35^2 = 3.6 |
|  | 67¢ | 64 | ×0.35^3 = 2.7 |
|  | 66¢ | 151 | ×0.35^4 = 2.3 |
|  | 65¢ | 208 | ×0.35^5 = 1.1 |
|  | 59¢ | 150 | ×0.35^11 = 0.0 |
|  | 39¢ | 100 | ×0.35^31 = 0.0 |
|  | 2¢ | 2,250 | ×0.35^68 = 0.0 |
| | | **Σ** | **28.8** |

`yours 10.0 / Σ 28.8 = 34.8%`  
`$500 ÷ 30 ÷ 2 = $8.33 × 34.8% = $2.90/day`  

<details><summary>÷ 30 markets in this race — tap to list</summary>

1. `pntcbk-nba-kawleo-2026-10-23-atl`
2. `pntcbk-nba-kawleo-2026-10-23-bkn`
3. `pntcbk-nba-kawleo-2026-10-23-bos`
4. `pntcbk-nba-kawleo-2026-10-23-cha`
5. `pntcbk-nba-kawleo-2026-10-23-chi`
6. `pntcbk-nba-kawleo-2026-10-23-cle`
7. `pntcbk-nba-kawleo-2026-10-23-dal`
8. `pntcbk-nba-kawleo-2026-10-23-den`
9. `pntcbk-nba-kawleo-2026-10-23-det`
10. `pntcbk-nba-kawleo-2026-10-23-gsw`
11. `pntcbk-nba-kawleo-2026-10-23-hou`
12. `pntcbk-nba-kawleo-2026-10-23-ind`
13. `pntcbk-nba-kawleo-2026-10-23-lac`
14. `pntcbk-nba-kawleo-2026-10-23-lal`
15. `pntcbk-nba-kawleo-2026-10-23-mem`
16. `pntcbk-nba-kawleo-2026-10-23-mia`
17. `pntcbk-nba-kawleo-2026-10-23-mil`
18. `pntcbk-nba-kawleo-2026-10-23-min`
19. `pntcbk-nba-kawleo-2026-10-23-nop`
20. `pntcbk-nba-kawleo-2026-10-23-nyk`
21. `pntcbk-nba-kawleo-2026-10-23-okc`
22. `pntcbk-nba-kawleo-2026-10-23-orl`
23. `pntcbk-nba-kawleo-2026-10-23-phi`
24. `pntcbk-nba-kawleo-2026-10-23-pho`
25. `pntcbk-nba-kawleo-2026-10-23-por`
26. `pntcbk-nba-kawleo-2026-10-23-sac`
27. `pntcbk-nba-kawleo-2026-10-23-sas`
28. `pntcbk-nba-kawleo-2026-10-23-tor` ← this one
29. `pntcbk-nba-kawleo-2026-10-23-uta`
30. `pntcbk-nba-kawleo-2026-10-23-was`

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 40 @ 95¢ → $2.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 122 (40 yours) | ×0.1^0 = 122.0 |
|  | 1¢ | 1,950 | ×0.1^94 = 0.0 |
| | | **Σ** | **122.0** |

`yours 40.0 / Σ 122.0 = 32.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 32.8% = $2.05/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 22¢ → $1.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 31 (10 yours) | ×0.2^0 = 31.0 |
|  | 25¢ | 58 | ×0.2^3 = 0.5 |
|  | 29¢ | 0 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 71¢ | 0 | ×0.2^49 = 0.0 |
|  | 97¢ | 80,494 | ×0.2^75 = 0.0 |
| | | **Σ** | **31.5** |

`yours 10.0 / Σ 31.5 = 31.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.8% = $1.22/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> BUY 66 @ 77¢ → $1.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 216 (66 yours) | ×0.1^0 = 216.3 |
|  | 74¢ | 110 | ×0.1^3 = 0.1 |
|  | 71¢ | 372 | ×0.1^6 = 0.0 |
|  | 66¢ | 150 | ×0.1^11 = 0.0 |
|  | 65¢ | 59 | ×0.1^12 = 0.0 |
|  | 42¢ | 5 | ×0.1^35 = 0.0 |
|  | 1¢ | 100,000 | ×0.1^76 = 0.0 |
| | | **Σ** | **216.4** |

`yours 66.3 / Σ 216.4 = 30.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 30.6% = $1.91/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-darnor` ← this one
2. `enwc-ussep-sc-2026-08-11-rep-ralnor`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 11 @ 15¢ → $1.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 36 (11 yours) | ×0.1^0 = 35.6 |
|  | 10¢ | 173 | ×0.1^5 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^14 = 0.0 |
| | | **Σ** | **35.6** |

`yours 10.6 / Σ 35.6 = 29.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 29.8% = $1.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 20 @ 30¢ → $3.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 72 (20 yours) | ×0.25^0 = 71.9 |
|  | 34¢ | 99 | ×0.25^4 = 0.4 |
|  | 50¢ | 25 | ×0.25^20 = 0.0 |
|  | 99¢ | 10,856 | ×0.25^69 = 0.0 |
| | | **Σ** | **72.3** |

`yours 19.9 / Σ 72.3 = 27.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 27.5% = $3.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-co-2026-11-03-dem</code> BUY 40 @ 95¢ → $1.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 148 (40 yours) | ×0.1^0 = 148.0 |
|  | 2¢ | 600,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **148.0** |

`yours 40.0 / Σ 148.0 = 27.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.0% = $1.69/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem` ← this one
2. `usgubewc-usgub-co-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 40 @ 95¢ → $1.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 154 (40 yours) | ×0.1^0 = 154.0 |
|  | 2¢ | 500,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **154.0** |

`yours 40.0 / Σ 154.0 = 26.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.0% = $1.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (10,466 resting) | ~84.4% | ~$21.10 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (36,475 resting) | ~69.6% | ~$17.41 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (61,174 resting) | ~19.5% | ~$14.65 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (60,240 resting) | ~17.3% | ~$12.99 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (687,611 resting) | ~12.4% | ~$9.33 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (801,971 resting) | ~11.7% | ~$8.74 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (36,312 resting) | ~29.0% | ~$7.26 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (10,050 resting) | ~27.1% | ~$6.77 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,039,008 resting) | ~5.6% | ~$4.18 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,636 resting) | ~4.4% | ~$3.33 |
| `ewc-usgub-ia-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (81,436 resting) | ~44.2% | ~$2.76 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (140,284 resting) | ~8.4% | ~$2.09 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $557.62 |
| Skipped | $1.41 |
| **Total earned** | **$2,447.06** |

1952 reward rows · 39 days with rewards · 478 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-10 ⚠️ multi-day pending bucket | $557.62 | `████████████████████` |
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
| 2026-07-28 | $79.65 | `███` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $983.74 | `█████████████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $101.55 |
| `apdc-jerpowgov-2026-12-31` | $87.26 |
| `opdc-mcconnell-resign-2026-11-02` | $65.07 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.99 |
| `scc-hrep-rep-2026-11-03-gte200` | $36.36 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `pandc-anydis-2027-12-31` | $31.51 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-12 6:06 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 5:06 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 5:01 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 3:30 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 2:48 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 2:10 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 1:16 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:49 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:39 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:12 PM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
