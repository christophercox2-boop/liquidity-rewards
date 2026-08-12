# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-12 5:06 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$230.64/day estimated (ceiling, not promise — details below)

**Earned:** $2,447.06 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-10: **$557.62** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-09: **$62.24** · 2026-08-08: **$54.78** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$15.75/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$14.64/day), `ewc-usgub-ga-2026-11-03-rep` (~$12.99/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$230.64/day (~$9.61/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-49` | SELL | 14.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (91,765 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,549 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 15.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~99.0% of ask side (74,007 resting ≥ 2,000 ✓) ≈ $6.19/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.8% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.49/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 11.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~81.6% of bid side (200,595 resting ≥ 5,000 ✓) ≈ $3.14/day (pool ÷ 13 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (203,859 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~75.5% of ask side (130,978 resting ≥ 2,000 ✓) ≈ $4.72/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 35.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~72.4% of bid side (400,479 resting ≥ 5,000 ✓) ≈ $3.02/day (pool ÷ 12 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 95.0¢ | 60 | 0 | $25.00 | ✅ scoring — ~70.6% of bid side (510,535 resting ≥ 2,000 ✓) ≈ $4.41/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 93.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (500,475 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.5% of bid side (510,515 resting ≥ 2,000 ✓) ≈ $3.85/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | SELL | 3.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~58.8% of ask side (130,793 resting ≥ 2,000 ✓) ≈ $3.68/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 25.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~58.8% of ask side (92,177 resting ≥ 5,000 ✓) ≈ $2.26/day (pool ÷ 13 markets) |
| `ussewc-usse-ar-2026-11-03-dem` | SELL | 8.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~58.1% of ask side (273,944 resting ≥ 2,000 ✓) ≈ $3.63/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~58.0% of ask side (208,607 resting ≥ 2,000 ✓) ≈ $3.62/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~57.8% of ask side (65,714 resting ≥ 2,000 ✓) ≈ $3.61/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~56.3% of ask side (130,796 resting ≥ 2,000 ✓) ≈ $3.52/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~56.3% of ask side (208,609 resting ≥ 2,000 ✓) ≈ $3.52/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~54.1% of bid side (500,474 resting ≥ 2,000 ✓) ≈ $3.38/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tx-2026-11-03-dem` | BUY | 15.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~51.4% of bid side (10,474 resting ≥ 2,000 ✓) ≈ $3.21/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-rep` | BUY | 9.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~42.9% of bid side (15,713 resting ≥ 2,000 ✓) ≈ $2.68/day (pool ÷ 2 markets) |
| `usgubewc-usgub-sc-2026-11-03-rep` | BUY | 92.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~37.0% of bid side (510,308 resting ≥ 2,000 ✓) ≈ $2.31/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-rep` | SELL | 9.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~35.7% of ask side (207,528 resting ≥ 2,000 ✓) ≈ $2.23/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~35.0% of bid side (14,291 resting ≥ 2,000 ✓) ≈ $2.19/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~31.7% of bid side (15,750 resting ≥ 2,000 ✓) ≈ $1.98/day (pool ÷ 2 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | BUY | 77.0¢ | 66 | 0 | $25.00 | ✅ scoring — ~30.5% of bid side (100,912 resting ≥ 2,000 ✓) ≈ $1.91/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | SELL | 30.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~27.5% of ask side (11,152 resting ≥ 10,000 ✓) ≈ $3.44/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~26.8% of bid side (610,599 resting ≥ 2,000 ✓) ≈ $1.68/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~26.7% of bid side (510,600 resting ≥ 2,000 ✓) ≈ $1.67/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~26.0% of bid side (2,104 resting ≥ 2,000 ✓) ≈ $1.62/day (pool ÷ 2 markets) |
| …and 388 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 14¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 50¢ | 100 | ×0.2^36 = 0.0 |
|  | 97¢ | 80,459 | ×0.2^83 = 0.0 |
| | | **Σ** | **5.0** |

`yours 5.0 / Σ 5.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 40 @ 15¢ → $6.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 16¢ | 4 | ×0.1^1 = 0.4 |
|  | 26¢ | 658 | ×0.1^11 = 0.0 |
|  | 54¢ | 17 | ×0.1^39 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^83 = 0.0 |
| | | **Σ** | **40.4** |

`yours 40.0 / Σ 40.4 = 99.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.0% = $6.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 40 @ 11¢ → $3.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 10¢ | 45 | ×0.2^1 = 9.0 |
|  | 1¢ | 200,510 | ×0.2^10 = 0.0 |
| | | **Σ** | **49.0** |

`yours 40.0 / Σ 49.0 = 81.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 81.6% = $3.14/day`  

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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 40 @ 10¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 24¢ | 50 | ×0.1^14 = 0.0 |
|  | 98¢ | 195,750 | ×0.1^88 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $4.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 53 (40 yours) | ×0.1^0 = 53.0 |
|  | 98¢ | 130,700 | ×0.1^94 = 0.0 |
| | | **Σ** | **53.0** |

`yours 40.0 / Σ 53.0 = 75.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.5% = $4.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 21 @ 35¢ → $3.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 29 (21 yours) | ×0.2^0 = 29.0 |
|  | 2¢ | 400,250 | ×0.2^33 = 0.0 |
| | | **Σ** | **29.0** |

`yours 21.0 / Σ 29.0 = 72.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 72.4% = $3.02/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 95¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 2¢ | 500,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **65.0** |

`yours 40.0 / Σ 65.0 = 61.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.5% = $3.85/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 25¢ → $2.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 26¢ | 21 | ×0.2^1 = 4.2 |
|  | 28¢ | 351 | ×0.2^3 = 2.8 |
|  | 29¢ | 0 | ×0.2^4 = 0.0 |
|  | 50¢ | 100 | ×0.2^25 = 0.0 |
|  | 97¢ | 80,494 | ×0.2^72 = 0.0 |
| | | **Σ** | **17.0** |

`yours 10.0 / Σ 17.0 = 58.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 58.8% = $2.26/day`  

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
<details><summary><code>ussewc-usse-ar-2026-11-03-dem</code> SELL 50 @ 8¢ → $3.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 86 (50 yours) | ×0.1^0 = 86.0 |
|  | 98¢ | 265,817 | ×0.1^90 = 0.0 |
| | | **Σ** | **86.0** |

`yours 50.0 / Σ 86.0 = 58.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.1% = $3.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem` ← this one
2. `ussewc-usse-ar-2026-11-03-rep`

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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 4¢ → $3.61/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 69 (40 yours) | ×0.1^0 = 69.0 |
|  | 7¢ | 170 | ×0.1^3 = 0.2 |
|  | 98¢ | 65,250 | ×0.1^94 = 0.0 |
| | | **Σ** | **69.2** |

`yours 40.0 / Σ 69.2 = 57.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.8% = $3.61/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 40 @ 5¢ → $3.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 71 (40 yours) | ×0.1^0 = 71.0 |
|  | 98¢ | 130,500 | ×0.1^93 = 0.0 |
| | | **Σ** | **71.0** |

`yours 40.0 / Σ 71.0 = 56.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 56.3% = $3.52/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-me-2026-11-03-dem</code> BUY 40 @ 95¢ → $3.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 74 (40 yours) | ×0.1^0 = 74.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **74.0** |

`yours 40.0 / Σ 74.0 = 54.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 54.1% = $3.38/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem` ← this one
2. `usgubewc-usgub-me-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-tx-2026-11-03-dem</code> BUY 11 @ 15¢ → $3.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 21 (11 yours) | ×0.1^0 = 20.6 |
|  | 11¢ | 30 | ×0.1^4 = 0.0 |
|  | 10¢ | 173 | ×0.1^5 = 0.0 |
|  | 2¢ | 50 | ×0.1^13 = 0.0 |
|  | 1¢ | 10,200 | ×0.1^14 = 0.0 |
| | | **Σ** | **20.6** |

`yours 10.6 / Σ 20.6 = 51.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 51.4% = $3.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tx-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-rep</code> BUY 40 @ 9¢ → $2.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 7¢ | 323 | ×0.1^2 = 3.2 |
|  | 6¢ | 100 | ×0.1^3 = 0.1 |
|  | 1¢ | 15,200 | ×0.1^8 = 0.0 |
| | | **Σ** | **93.3** |

`yours 40.0 / Σ 93.3 = 42.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 42.9% = $2.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem`
2. `usgubewc-usgub-mn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-sc-2026-11-03-rep</code> BUY 40 @ 92¢ → $2.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 108 (40 yours) | ×0.1^0 = 108.0 |
|  | 2¢ | 500,000 | ×0.1^90 = 0.0 |
| | | **Σ** | **108.0** |

`yours 40.0 / Σ 108.0 = 37.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 37.0% = $2.31/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sc-2026-11-03-dem`
2. `usgubewc-usgub-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-rep</code> SELL 40 @ 9¢ → $2.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 10¢ | 222 | ×0.1^1 = 22.2 |
|  | 98¢ | 199,175 | ×0.1^89 = 0.0 |
| | | **Σ** | **112.2** |

`yours 40.0 / Σ 112.2 = 35.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 35.7% = $2.23/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem`
2. `usgubewc-usgub-ct-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $2.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 14,291 (5,000 yours) | ×0.1^0 = 14,291.0 |
| | | **Σ** | **14,291.0** |

`yours 5,000.0 / Σ 14,291.0 = 35.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 35.0% = $2.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $1.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 15,750 (5,000 yours) | ×0.1^0 = 15,750.0 |
| | | **Σ** | **15,750.0** |

`yours 5,000.0 / Σ 15,750.0 = 31.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 31.7% = $1.98/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> BUY 66 @ 77¢ → $1.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 216 (66 yours) | ×0.1^0 = 216.3 |
|  | 75¢ | 110 | ×0.1^2 = 1.1 |
|  | 71¢ | 372 | ×0.1^6 = 0.0 |
|  | 66¢ | 150 | ×0.1^11 = 0.0 |
|  | 65¢ | 59 | ×0.1^12 = 0.0 |
|  | 42¢ | 5 | ×0.1^35 = 0.0 |
|  | 1¢ | 100,000 | ×0.1^76 = 0.0 |
| | | **Σ** | **217.4** |

`yours 66.3 / Σ 217.4 = 30.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 30.5% = $1.91/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-darnor` ← this one
2. `enwc-ussep-sc-2026-08-11-rep-ralnor`

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 20 @ 30¢ → $3.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 72 (20 yours) | ×0.25^0 = 71.9 |
|  | 34¢ | 99 | ×0.25^4 = 0.4 |
|  | 50¢ | 25 | ×0.25^20 = 0.0 |
|  | 99¢ | 10,956 | ×0.25^69 = 0.0 |
| | | **Σ** | **72.3** |

`yours 19.9 / Σ 72.3 = 27.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 27.5% = $3.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-co-2026-11-03-dem</code> BUY 40 @ 95¢ → $1.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 149 (40 yours) | ×0.1^0 = 149.0 |
|  | 2¢ | 600,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **149.0** |

`yours 40.0 / Σ 149.0 = 26.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.8% = $1.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem` ← this one
2. `usgubewc-usgub-co-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> BUY 40 @ 95¢ → $1.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 150 (40 yours) | ×0.1^0 = 150.0 |
|  | 2¢ | 500,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **150.0** |

`yours 40.0 / Σ 150.0 = 26.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.7% = $1.67/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 40 @ 95¢ → $1.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 154 (40 yours) | ×0.1^0 = 154.0 |
|  | 1¢ | 1,950 | ×0.1^94 = 0.0 |
| | | **Σ** | **154.0** |

`yours 40.0 / Σ 154.0 = 26.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.0% = $1.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,481 resting) | ~63.0% | ~$15.75 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (64,113 resting) | ~19.5% | ~$14.64 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (63,725 resting) | ~17.3% | ~$12.99 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (687,736 resting) | ~11.8% | ~$8.85 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (801,948 resting) | ~11.7% | ~$8.74 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (36,313 resting) | ~29.0% | ~$7.25 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (10,105 resting) | ~26.9% | ~$6.72 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,039,620 resting) | ~4.8% | ~$3.56 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,690 resting) | ~4.3% | ~$3.25 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (91,183 resting) | ~3.9% | ~$2.94 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (160,476 resting) | ~8.4% | ~$2.10 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (623,237 resting) | ~6.2% | ~$1.56 |

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
| 2026-08-12 5:06 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 5:01 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 3:30 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 2:48 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 2:10 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 1:16 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:49 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:39 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:12 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 11:55 AM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
