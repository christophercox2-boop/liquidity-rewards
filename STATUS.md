# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-12 1:16 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$303.40/day estimated (ceiling, not promise — details below)

**Earned:** $2,447.06 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-10: **$557.62** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-09: **$62.24** · 2026-08-08: **$54.78** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-xavbec` — BUY at the best price, ~$19.14/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$15.32/day), `ewc-usgub-ga-2026-11-03-dem` (~$14.96/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$303.40/day (~$12.64/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 72.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (500,361 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 35.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (400,471 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 38.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (82,374 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 14.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (77,379 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 11.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (300,550 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 20.0¢ | 32 | 0 | $100.00 | ✅ scoring — ~99.2% of ask side (91,972 resting ≥ 5,000 ✓) ≈ $3.81/day (pool ÷ 13 markets) |
| `pandc-anydis-2027-12-31` | SELL | 30.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~98.1% of ask side (10,951 resting ≥ 10,000 ✓) ≈ $12.26/day (pool ÷ 2 markets) |
| `pntcbk-wnba-white-2027-06-30-roywhi` | BUY | 1.0¢ | 5,000 | 0 | $250.00 | ✅ scoring — ~94.3% of bid side (5,300 resting ≥ 5,000 ✓) ≈ $117.92/day |
| `usgubewc-usgub-me-2026-11-03-rep` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~93.0% of ask side (65,518 resting ≥ 2,000 ✓) ≈ $5.81/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.8% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.49/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 11.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~81.6% of bid side (200,595 resting ≥ 5,000 ✓) ≈ $3.14/day (pool ÷ 13 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (510,450 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~75.5% of ask side (208,541 resting ≥ 2,000 ✓) ≈ $4.72/day (pool ÷ 2 markets) |
| `ussewc-usse-wv-2026-11-03-dem` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~75.5% of ask side (130,978 resting ≥ 2,000 ✓) ≈ $4.72/day (pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | SELL | 5.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~66.7% of ask side (65,800 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `usgubewc-usgub-vt-2026-11-03-dem` | SELL | 12.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~66.7% of ask side (338,999 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-rep` | BUY | 9.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~63.2% of bid side (15,683 resting ≥ 2,000 ✓) ≈ $3.95/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~58.7% of ask side (65,713 resting ≥ 2,000 ✓) ≈ $3.67/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~51.9% of bid side (500,477 resting ≥ 2,000 ✓) ≈ $3.25/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~50.6% of ask side (23,154 resting ≥ 2,000 ✓) ≈ $3.16/day (pool ÷ 2 markets) |
| `ussewc-usse-de-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~47.0% of ask side (9,316 resting ≥ 2,000 ✓) ≈ $2.94/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 92.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~44.4% of bid side (500,290 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-rep` | BUY | 94.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~44.0% of bid side (510,541 resting ≥ 2,000 ✓) ≈ $2.75/day (pool ÷ 2 markets) |
| `ussewc-usse-ri-2026-11-03-dem` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~40.4% of ask side (9,002 resting ≥ 2,000 ✓) ≈ $2.53/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~40.2% of bid side (12,435 resting ≥ 2,000 ✓) ≈ $2.51/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 27.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~33.9% of bid side (10,669 resting ≥ 5,000 ✓) ≈ $8.48/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~31.1% of bid side (16,100 resting ≥ 2,000 ✓) ≈ $1.94/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 95.0¢ | 60 | 0 | $25.00 | ✅ scoring — ~27.9% of bid side (510,665 resting ≥ 2,000 ✓) ≈ $1.74/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~27.0% of bid side (500,548 resting ≥ 2,000 ✓) ≈ $1.69/day (pool ÷ 2 markets) |
| `ussewc-usse-de-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~25.8% of bid side (510,605 resting ≥ 2,000 ✓) ≈ $1.61/day (pool ÷ 2 markets) |
| …and 388 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 18 @ 72¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 72¢ | 18 (18 yours) | ×0.2^0 = 17.6 |
|  | 2¢ | 135 | ×0.2^70 = 0.0 |
|  | 1¢ | 500,208 | ×0.2^71 = 0.0 |
| | | **Σ** | **17.6** |

`yours 17.6 / Σ 17.6 = 100.0%`  
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 2 @ 38¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 2 (2 yours) | ×0.2^0 = 2.0 |
|  | 57¢ | 100 | ×0.2^19 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^60 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 100.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 14¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 22¢ | 356 | ×0.2^8 = 0.0 |
|  | 50¢ | 100 | ×0.2^36 = 0.0 |
|  | 97¢ | 65,717 | ×0.2^83 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 18 @ 11¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 18 (18 yours) | ×0.2^0 = 18.4 |
|  | 1¢ | 300,531 | ×0.2^10 = 0.0 |
| | | **Σ** | **18.4** |

`yours 18.4 / Σ 18.4 = 99.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.8% = $3.84/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 32 @ 20¢ → $3.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 32 (32 yours) | ×0.2^0 = 31.9 |
|  | 24¢ | 167 | ×0.2^4 = 0.3 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 97¢ | 80,472 | ×0.2^77 = 0.0 |
| | | **Σ** | **32.2** |

`yours 31.9 / Σ 32.2 = 99.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.2% = $3.81/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 20 @ 30¢ → $12.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 20 (20 yours) | ×0.25^0 = 19.9 |
|  | 34¢ | 99 | ×0.25^4 = 0.4 |
|  | 50¢ | 25 | ×0.25^20 = 0.0 |
|  | 99¢ | 10,807 | ×0.25^69 = 0.0 |
| | | **Σ** | **20.3** |

`yours 19.9 / Σ 20.3 = 98.1%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 98.1% = $12.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>pntcbk-wnba-white-2027-06-30-roywhi</code> BUY 5,000 @ 1¢ → $117.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,300 (5,000 yours) | ×0.9^0 = 5,300.0 |
| | | **Σ** | **5,300.0** |

`yours 5,000.0 / Σ 5,300.0 = 94.3%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 94.3% = $117.92/day`  

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> SELL 40 @ 5¢ → $5.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 43 (40 yours) | ×0.1^0 = 43.0 |
|  | 98¢ | 65,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **43.0** |

`yours 40.0 / Σ 43.0 = 93.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.0% = $5.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem`
2. `usgubewc-usgub-me-2026-11-03-rep` ← this one

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> SELL 40 @ 4¢ → $4.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 53 (40 yours) | ×0.1^0 = 53.0 |
|  | 98¢ | 208,263 | ×0.1^94 = 0.0 |
| | | **Σ** | **53.0** |

`yours 40.0 / Σ 53.0 = 75.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.5% = $4.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wv-2026-11-03-dem</code> SELL 40 @ 5¢ → $4.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 53 (40 yours) | ×0.1^0 = 53.0 |
|  | 98¢ | 130,700 | ×0.1^93 = 0.0 |
| | | **Σ** | **53.0** |

`yours 40.0 / Σ 53.0 = 75.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 75.5% = $4.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wv-2026-11-03-dem` ← this one
2. `ussewc-usse-wv-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> SELL 50 @ 5¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 75 (50 yours) | ×0.1^0 = 75.0 |
|  | 98¢ | 65,500 | ×0.1^93 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-vt-2026-11-03-dem</code> SELL 20 @ 12¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 30 (20 yours) | ×0.1^0 = 30.0 |
|  | 98¢ | 132,984 | ×0.1^86 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-vt-2026-11-03-dem` ← this one
2. `usgubewc-usgub-vt-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-rep</code> BUY 40 @ 9¢ → $3.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 60 (40 yours) | ×0.1^0 = 60.0 |
|  | 7¢ | 323 | ×0.1^2 = 3.2 |
|  | 6¢ | 100 | ×0.1^3 = 0.1 |
|  | 1¢ | 15,200 | ×0.1^8 = 0.0 |
| | | **Σ** | **63.3** |

`yours 40.0 / Σ 63.3 = 63.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.2% = $3.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem`
2. `usgubewc-usgub-mn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 4¢ → $3.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 68 (40 yours) | ×0.1^0 = 68.0 |
|  | 7¢ | 170 | ×0.1^3 = 0.2 |
|  | 98¢ | 65,250 | ×0.1^94 = 0.0 |
| | | **Σ** | **68.2** |

`yours 40.0 / Σ 68.2 = 58.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.7% = $3.67/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-dem</code> BUY 40 @ 95¢ → $3.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 77 (40 yours) | ×0.1^0 = 77.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **77.0** |

`yours 40.0 / Σ 77.0 = 51.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 51.9% = $3.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem` ← this one
2. `usgubewc-usgub-me-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $3.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 97¢ | 60 | ×0.1^1 = 6.0 |
|  | 99¢ | 23,044 | ×0.1^3 = 23.0 |
| | | **Σ** | **79.0** |

`yours 40.0 / Σ 79.0 = 50.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.6% = $3.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-de-2026-11-03-dem</code> SELL 40 @ 96¢ → $2.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 97¢ | 105 | ×0.1^1 = 10.5 |
|  | 98¢ | 52 | ×0.1^2 = 0.5 |
|  | 99¢ | 9,094 | ×0.1^3 = 9.1 |
| | | **Σ** | **85.1** |

`yours 40.0 / Σ 85.1 = 47.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 47.0% = $2.94/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-de-2026-11-03-dem` ← this one
2. `ussewc-usse-de-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 40 @ 92¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 2¢ | 500,000 | ×0.1^90 = 0.0 |
| | | **Σ** | **90.0** |

`yours 40.0 / Σ 90.0 = 44.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.4% = $2.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-rep</code> BUY 40 @ 94¢ → $2.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 91 (40 yours) | ×0.1^0 = 91.0 |
|  | 2¢ | 500,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **91.0** |

`yours 40.0 / Σ 91.0 = 44.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.0% = $2.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem`
2. `ussewc-usse-ky-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ri-2026-11-03-dem</code> SELL 40 @ 96¢ → $2.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 99¢ | 8,912 | ×0.1^3 = 8.9 |
| | | **Σ** | **98.9** |

`yours 40.0 / Σ 98.9 = 40.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 40.4% = $2.53/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ri-2026-11-03-dem` ← this one
2. `ussewc-usse-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $2.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,435 (5,000 yours) | ×0.1^0 = 12,435.0 |
| | | **Σ** | **12,435.0** |

`yours 5,000.0 / Σ 12,435.0 = 40.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 40.2% = $2.51/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 30 @ 27¢ → $8.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 49 (30 yours) | ×0.2^0 = 49.3 |
|  | 26¢ | 189 | ×0.2^1 = 37.8 |
|  | 24¢ | 7 | ×0.2^3 = 0.1 |
|  | 16¢ | 1 | ×0.2^11 = 0.0 |
|  | 14¢ | 3 | ×0.2^13 = 0.0 |
|  | 13¢ | 3 | ×0.2^14 = 0.0 |
|  | 12¢ | 116 | ×0.2^15 = 0.0 |
|  | 2¢ | 100 | ×0.2^25 = 0.0 |
|  | 1¢ | 10,200 | ×0.2^26 = 0.0 |
| | | **Σ** | **87.1** |

`yours 29.6 / Σ 87.1 = 33.9%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 33.9% = $8.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $1.94/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 16,100 (5,000 yours) | ×0.1^0 = 16,100.0 |
| | | **Σ** | **16,100.0** |

`yours 5,000.0 / Σ 16,100.0 = 31.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 31.1% = $1.94/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 60 @ 95¢ → $1.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 215 (60 yours) | ×0.1^0 = 215.0 |
|  | 2¢ | 500,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **215.0** |

`yours 60.0 / Σ 215.0 = 27.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.9% = $1.74/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 95¢ → $1.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 148 (40 yours) | ×0.1^0 = 148.0 |
|  | 2¢ | 500,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **148.0** |

`yours 40.0 / Σ 148.0 = 27.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.0% = $1.69/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-de-2026-11-03-dem</code> BUY 40 @ 95¢ → $1.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 155 (40 yours) | ×0.1^0 = 155.0 |
|  | 2¢ | 500,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **155.0** |

`yours 40.0 / Σ 155.0 = 25.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 25.8% = $1.61/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-de-2026-11-03-dem` ← this one
2. `ussewc-usse-de-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,050,512 resting) | ~25.5% | ~$19.14 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,548 resting) | ~61.3% | ~$15.32 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (69,188 resting) | ~19.9% | ~$14.96 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (66,295 resting) | ~17.9% | ~$13.42 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (687,861 resting) | ~12.2% | ~$9.15 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (726,000 resting) | ~9.4% | ~$7.03 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,622 resting) | ~26.5% | ~$6.63 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (10,281 resting) | ~20.6% | ~$5.15 |
| `ewc-usgub-ia-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (75,990 resting) | ~63.3% | ~$3.96 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (869,192 resting) | ~4.8% | ~$3.60 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (284,624 resting) | ~4.2% | ~$3.18 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (318,963 resting) | ~2.9% | ~$2.15 |

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
| 2026-08-12 1:16 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:49 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:39 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:12 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 11:55 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 11:17 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 10:41 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 10:39 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 9:52 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:45 AM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
