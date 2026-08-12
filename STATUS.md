# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-12 12:17 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$273.93/day estimated (ceiling, not promise — details below)

**Earned:** $2,447.06 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-10: **$557.62** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-09: **$62.24** · 2026-08-08: **$54.78** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$16.30/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-08-31` (~$11.54/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$9.24/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$273.93/day (~$11.41/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 24.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,548 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 39.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~99.9% of bid side (300,460 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 24.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.0% of bid side (805,558 resting ≥ 5,000 ✓) ≈ $4.12/day (pool ÷ 12 markets) |
| `usgubewc-usgub-me-2026-11-03-rep` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~81.6% of ask side (65,564 resting ≥ 2,000 ✓) ≈ $5.10/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 7.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~80.3% of bid side (90,618 resting ≥ 5,000 ✓) ≈ $3.09/day (pool ÷ 13 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 98.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (502,300 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-or-2026-11-03-rep` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (73,378 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ne-2026-11-03-dem` | SELL | 11.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (273,620 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 71.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~76.9% of bid side (500,356 resting ≥ 5,000 ✓) ≈ $3.21/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~75.2% of bid side (50,358 resting ≥ 5,000 ✓) ≈ $2.89/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~73.7% of ask side (8,859 resting ≥ 2,000 ✓) ≈ $9.21/day |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 27.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~70.0% of bid side (400,480 resting ≥ 5,000 ✓) ≈ $2.92/day (pool ÷ 12 markets) |
| `usgubewc-usgub-vt-2026-11-03-dem` | SELL | 12.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~66.7% of ask side (337,880 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | SELL | 21.0¢ | 40 | 2 | $100.00 | ✅ scoring — ~66.1% of ask side (9,352 resting ≥ 5,000 ✓) ≈ $16.53/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 90.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~62.5% of bid side (511,012 resting ≥ 2,000 ✓) ≈ $3.91/day (pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | BUY | 13.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~61.6% of bid side (20,440 resting ≥ 5,000 ✓) ≈ $15.41/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.5% of ask side (8,133 resting ≥ 2,000 ✓) ≈ $2.56/day (pool ÷ 3 markets) |
| `usgubewc-usgub-nm-2026-11-03-rep` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.5% of ask side (73,095 resting ≥ 2,000 ✓) ≈ $3.85/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 8.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~60.0% of bid side (403,934 resting ≥ 5,000 ✓) ≈ $2.50/day (pool ÷ 12 markets) |
| `ussewc-usse-ks-2026-11-03-dem` | SELL | 21.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~57.2% of ask side (138,895 resting ≥ 2,000 ✓) ≈ $3.57/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~57.1% of ask side (208,333 resting ≥ 2,000 ✓) ≈ $3.57/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 62.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~54.7% of bid side (400,892 resting ≥ 5,000 ✓) ≈ $2.28/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 40.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~54.1% of ask side (82,527 resting ≥ 5,000 ✓) ≈ $2.25/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 14.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~53.9% of bid side (200,640 resting ≥ 5,000 ✓) ≈ $2.07/day (pool ÷ 13 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~52.6% of bid side (3,800 resting ≥ 2,000 ✓) ≈ $3.29/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~52.6% of bid side (3,800 resting ≥ 2,000 ✓) ≈ $3.29/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~52.5% of bid side (3,810 resting ≥ 2,000 ✓) ≈ $3.28/day (pool ÷ 2 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 9.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~51.3% of bid side (20,657 resting ≥ 2,000 ✓) ≈ $6.41/day |
| `usgubewc-usgub-ne-2026-11-03-rep` | BUY | 84.0¢ | 40 | 1 | $25.00 | ✅ scoring — ~50.0% of bid side (510,893 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 40.0¢ | 60 | 0 | $100.00 | ✅ scoring — ~49.1% of ask side (82,702 resting ≥ 5,000 ✓) ≈ $2.05/day (pool ÷ 12 markets) |
| …and 384 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 17 @ 24¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 17 (17 yours) | ×0.2^0 = 17.0 |
|  | 1¢ | 300,531 | ×0.2^23 = 0.0 |
| | | **Σ** | **17.0** |

`yours 17.0 / Σ 17.0 = 100.0%`  
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 39¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 39¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 2¢ | 300,250 | ×0.2^37 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.9% = $4.16/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 1 @ 24¢ → $4.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 22¢ | 0 | ×0.2^2 = 0.0 |
|  | 2¢ | 5,247 | ×0.2^22 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.0% = $4.12/day`  

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
<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> SELL 40 @ 10¢ → $5.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 49 (40 yours) | ×0.1^0 = 49.0 |
|  | 51¢ | 40 | ×0.1^41 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^88 = 0.0 |
| | | **Σ** | **49.0** |

`yours 40.0 / Σ 49.0 = 81.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 81.6% = $5.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem`
2. `usgubewc-usgub-me-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 40 @ 7¢ → $3.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 43 (40 yours) | ×0.2^0 = 43.0 |
|  | 5¢ | 26 | ×0.2^2 = 1.0 |
|  | 1¢ | 90,549 | ×0.2^6 = 5.8 |
| | | **Σ** | **49.8** |

`yours 40.0 / Σ 49.8 = 80.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 80.3% = $3.09/day`  

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
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 40 @ 98¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 98¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 50¢ | 50 | ×0.1^48 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^96 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-or-2026-11-03-rep</code> SELL 40 @ 10¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 26¢ | 335 | ×0.1^16 = 0.0 |
|  | 51¢ | 40 | ×0.1^41 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^88 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-or-2026-11-03-dem`
2. `usgubewc-usgub-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-dem</code> SELL 40 @ 11¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 20¢ | 10 | ×0.1^9 = 0.0 |
|  | 51¢ | 40 | ×0.1^40 = 0.0 |
|  | 98¢ | 265,817 | ×0.1^87 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ne-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 10 @ 71¢ → $3.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 71¢ | 13 (10 yours) | ×0.2^0 = 13.0 |
|  | 2¢ | 135 | ×0.2^69 = 0.0 |
|  | 1¢ | 500,208 | ×0.2^70 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 100 @ 18¢ → $2.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 133 (100 yours) | ×0.2^0 = 133.0 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **133.0** |

`yours 100.0 / Σ 133.0 = 75.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 75.2% = $2.89/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 40 @ 10¢ → $9.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 11¢ | 43 | ×0.1^1 = 4.3 |
|  | 17¢ | 32 | ×0.1^7 = 0.0 |
|  | 18¢ | 348 | ×0.1^8 = 0.0 |
|  | 19¢ | 5 | ×0.1^9 = 0.0 |
|  | 28¢ | 26 | ×0.1^18 = 0.0 |
|  | 33¢ | 300 | ×0.1^23 = 0.0 |
|  | 35¢ | 151 | ×0.1^25 = 0.0 |
|  | 99¢ | 7,904 | ×0.1^89 = 0.0 |
| | | **Σ** | **54.3** |

`yours 40.0 / Σ 54.3 = 73.7%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 73.7% = $9.21/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 21 @ 27¢ → $2.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 30 (21 yours) | ×0.2^0 = 30.0 |
|  | 2¢ | 400,250 | ×0.2^25 = 0.0 |
| | | **Σ** | **30.0** |

`yours 21.0 / Σ 30.0 = 70.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 70.0% = $2.92/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 40 @ 21¢ → $16.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 0 | ×0.2^0 = 0.1 |
| ▶ | 21¢ | 40 (40 yours) | ×0.2^2 = 1.6 |
|  | 23¢ | 469 | ×0.2^4 = 0.8 |
|  | 50¢ | 5 | ×0.2^31 = 0.0 |
|  | 99¢ | 8,838 | ×0.2^80 = 0.0 |
| | | **Σ** | **2.4** |

`yours 1.6 / Σ 2.4 = 66.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 66.1% = $16.53/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 90¢ → $3.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 89¢ | 181 | ×0.1^1 = 18.1 |
|  | 88¢ | 591 | ×0.1^2 = 5.9 |
|  | 2¢ | 500,000 | ×0.1^88 = 0.0 |
| | | **Σ** | **64.0** |

`yours 40.0 / Σ 64.0 = 62.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 62.5% = $3.91/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 20 @ 13¢ → $15.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 13¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 12¢ | 56 | ×0.2^2 = 2.2 |
|  | 11¢ | 20 | ×0.2^3 = 0.2 |
|  | 10¢ | 54 | ×0.2^4 = 0.1 |
|  | 9¢ | 20 | ×0.2^5 = 0.0 |
|  | 8¢ | 60 | ×0.2^6 = 0.0 |
|  | 6¢ | 10 | ×0.2^8 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^12 = 0.0 |
| | | **Σ** | **6.5** |

`yours 4.0 / Σ 6.5 = 61.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 61.6% = $15.41/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> SELL 40 @ 10¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 26¢ | 40 | ×0.1^16 = 0.0 |
|  | 51¢ | 40 | ×0.1^41 = 0.0 |
|  | 94¢ | 12 | ×0.1^84 = 0.0 |
|  | 99¢ | 7,976 | ×0.1^89 = 0.0 |
| | | **Σ** | **65.0** |

`yours 40.0 / Σ 65.0 = 61.5%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 61.5% = $2.56/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-rep</code> SELL 40 @ 10¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 37¢ | 12 | ×0.1^27 = 0.0 |
|  | 51¢ | 40 | ×0.1^41 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^88 = 0.0 |
| | | **Σ** | **65.0** |

`yours 40.0 / Σ 65.0 = 61.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.5% = $3.85/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem`
2. `usgubewc-usgub-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 40 @ 8¢ → $2.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 3¢ | 3,444 | ×0.2^5 = 1.1 |
|  | 2¢ | 400,250 | ×0.2^6 = 25.6 |
| | | **Σ** | **66.7** |

`yours 40.0 / Σ 66.7 = 60.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 60.0% = $2.50/day`  

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
<details><summary><code>ussewc-usse-ks-2026-11-03-dem</code> SELL 50 @ 21¢ → $3.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 80 (50 yours) | ×0.1^0 = 80.0 |
|  | 22¢ | 70 | ×0.1^1 = 7.0 |
|  | 24¢ | 472 | ×0.1^3 = 0.5 |
|  | 92¢ | 70 | ×0.1^71 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^77 = 0.0 |
| | | **Σ** | **87.5** |

`yours 50.0 / Σ 87.5 = 57.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.2% = $3.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ks-2026-11-03-dem` ← this one
2. `ussewc-usse-ks-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> SELL 40 @ 5¢ → $3.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 70 (40 yours) | ×0.1^0 = 70.0 |
|  | 98¢ | 208,063 | ×0.1^93 = 0.0 |
| | | **Σ** | **70.0** |

`yours 40.0 / Σ 70.0 = 57.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 57.1% = $3.57/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 5 @ 62¢ → $2.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 62¢ | 9 (5 yours) | ×0.2^0 = 9.0 |
|  | 59¢ | 10 | ×0.2^3 = 0.1 |
|  | 58¢ | 12 | ×0.2^4 = 0.0 |
|  | 57¢ | 109 | ×0.2^5 = 0.0 |
|  | 53¢ | 162 | ×0.2^9 = 0.0 |
|  | 50¢ | 25 | ×0.2^12 = 0.0 |
|  | 49¢ | 115 | ×0.2^13 = 0.0 |
|  | 2¢ | 400,250 | ×0.2^60 = 0.0 |
| | | **Σ** | **9.1** |

`yours 5.0 / Σ 9.1 = 54.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 54.7% = $2.28/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 20 @ 40¢ → $2.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 41¢ | 85 | ×0.2^1 = 17.0 |
|  | 50¢ | 0 | ×0.2^10 = 0.0 |
|  | 56¢ | 0 | ×0.2^16 = 0.0 |
|  | 57¢ | 0 | ×0.2^17 = 0.0 |
|  | 58¢ | 0 | ×0.2^18 = 0.0 |
|  | 59¢ | 150 | ×0.2^19 = 0.0 |
|  | 61¢ | 0 | ×0.2^21 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^58 = 0.0 |
| | | **Σ** | **37.0** |

`yours 20.0 / Σ 37.0 = 54.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 54.1% = $2.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 20 @ 14¢ → $2.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 37 (20 yours) | ×0.2^0 = 37.0 |
|  | 10¢ | 45 | ×0.2^4 = 0.1 |
|  | 9¢ | 149 | ×0.2^5 = 0.0 |
|  | 1¢ | 200,409 | ×0.2^13 = 0.0 |
| | | **Σ** | **37.1** |

`yours 20.0 / Σ 37.1 = 53.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.9% = $2.07/day`  

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
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $3.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,800 (2,000 yours) | ×0.1^0 = 3,800.0 |
| | | **Σ** | **3,800.0** |

`yours 2,000.0 / Σ 3,800.0 = 52.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 52.6% = $3.29/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $3.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,800 (2,000 yours) | ×0.1^0 = 3,800.0 |
| | | **Σ** | **3,800.0** |

`yours 2,000.0 / Σ 3,800.0 = 52.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 52.6% = $3.29/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $3.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,810 (2,000 yours) | ×0.1^0 = 3,810.0 |
| | | **Σ** | **3,810.0** |

`yours 2,000.0 / Σ 3,810.0 = 52.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 52.5% = $3.28/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 40 @ 9¢ → $6.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 78 (40 yours) | ×0.1^0 = 78.0 |
|  | 5¢ | 99 | ×0.1^4 = 0.0 |
|  | 3¢ | 30 | ×0.1^6 = 0.0 |
|  | 2¢ | 10,250 | ×0.1^7 = 0.0 |
| | | **Σ** | **78.0** |

`yours 40.0 / Σ 78.0 = 51.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 51.3% = $6.41/day`  

</details>
<details><summary><code>usgubewc-usgub-ne-2026-11-03-rep</code> BUY 40 @ 84¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 85¢ | 4 | ×0.1^0 = 4.0 |
| ▶ | 84¢ | 40 (40 yours) | ×0.1^1 = 4.0 |
|  | 80¢ | 313 | ×0.1^5 = 0.0 |
|  | 79¢ | 325 | ×0.1^6 = 0.0 |
|  | 59¢ | 11 | ×0.1^26 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^83 = 0.0 |
| | | **Σ** | **8.0** |

`yours 4.0 / Σ 8.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ne-2026-11-03-dem`
2. `usgubewc-usgub-ne-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 60 @ 40¢ → $2.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 122 (60 yours) | ×0.2^0 = 122.0 |
|  | 43¢ | 10 | ×0.2^3 = 0.1 |
|  | 44¢ | 0 | ×0.2^4 = 0.0 |
|  | 63¢ | 299 | ×0.2^23 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^58 = 0.0 |
| | | **Σ** | **122.1** |

`yours 60.0 / Σ 122.1 = 49.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.1% = $2.05/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (53,679 resting) | ~21.7% | ~$16.30 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,938 resting) | ~46.1% | ~$11.54 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,120 resting) | ~36.9% | ~$9.24 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (25,867 resting) | ~34.2% | ~$8.54 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (68,524 resting) | ~7.8% | ~$5.88 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (279,178 resting) | ~7.1% | ~$5.36 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (857,175 resting) | ~5.3% | ~$3.99 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (270,203 resting) | ~4.2% | ~$3.14 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (681,755 resting) | ~2.1% | ~$1.59 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (58,108 resting) | ~6.3% | ~$1.57 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (610,038 resting) | ~6.1% | ~$1.52 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (134,350 resting) | ~1.9% | ~$1.43 |

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
| 2026-08-12 12:17 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:31 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:24 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:10 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:03 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 10:48 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 10:35 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 10:28 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 10:23 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 10:17 PM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
