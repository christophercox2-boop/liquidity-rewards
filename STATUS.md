# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-12 9:52 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$155.72/day estimated (ceiling, not promise — details below)

**Earned:** $2,447.06 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-10: **$557.62** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-09: **$62.24** · 2026-08-08: **$54.78** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$16.78/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$15.95/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$15.71/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$155.72/day (~$6.49/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 24.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,548 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 16.0¢ | 40 | 1 | $100.00 | ✅ scoring — ~99.8% of bid side (400,642 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 74.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~95.8% of bid side (510,424 resting ≥ 2,000 ✓) ≈ $5.99/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~86.2% of bid side (50,341 resting ≥ 5,000 ✓) ≈ $3.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 7.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~80.3% of bid side (90,618 resting ≥ 5,000 ✓) ≈ $3.09/day (pool ÷ 13 markets) |
| `usgubewc-usgub-me-2026-11-03-rep` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~65.4% of ask side (65,727 resting ≥ 2,000 ✓) ≈ $4.08/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.4% of ask side (65,795 resting ≥ 2,000 ✓) ≈ $3.84/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.0% of ask side (9,647 resting ≥ 2,000 ✓) ≈ $3.81/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~55.6% of bid side (3,600 resting ≥ 2,000 ✓) ≈ $3.47/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 13.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~48.9% of bid side (100,565 resting ≥ 5,000 ✓) ≈ $1.88/day (pool ÷ 13 markets) |
| `pandc-anydis-2027-12-31` | BUY | 15.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~48.8% of bid side (10,342 resting ≥ 10,000 ✓) ≈ $6.10/day (pool ÷ 2 markets) |
| `lawec-cryptoleg-2026-12-31` | SELL | 38.0¢ | 10 | 1 | $25.00 | ✅ scoring — ~47.4% of ask side (47,123 resting ≥ 2,000 ✓) ≈ $5.92/day |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 22.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~46.5% of ask side (68,428 resting ≥ 5,000 ✓) ≈ $1.94/day (pool ÷ 12 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~43.4% of bid side (510,496 resting ≥ 2,000 ✓) ≈ $2.72/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 20.0¢ | 40 | 1 | $100.00 | ✅ scoring — ~41.6% of ask side (82,367 resting ≥ 5,000 ✓) ≈ $1.74/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~39.4% of ask side (138,362 resting ≥ 5,000 ✓) ≈ $1.64/day (pool ÷ 12 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 27.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~39.1% of ask side (18,622 resting ≥ 5,000 ✓) ≈ $9.77/day (pool ÷ 2 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | BUY | 27.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~38.5% of bid side (610,566 resting ≥ 2,000 ✓) ≈ $2.40/day (pool ÷ 2 markets) |
| `ussewc-usse-de-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~36.0% of bid side (510,611 resting ≥ 2,000 ✓) ≈ $2.25/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~34.6% of bid side (5,775 resting ≥ 2,000 ✓) ≈ $2.16/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 1,290 | 0 | $25.00 | ✅ scoring — ~29.5% of bid side (4,368 resting ≥ 2,000 ✓) ≈ $1.85/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~28.6% of bid side (2,090 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 15.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~27.9% of bid side (300,589 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 18.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~24.9% of bid side (50,586 resting ≥ 5,000 ✓) ≈ $0.96/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~24.8% of ask side (77,874 resting ≥ 5,000 ✓) ≈ $0.95/day (pool ÷ 13 markets) |
| `ussewc-usse-ar-2026-11-03-rep` | BUY | 93.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~22.2% of bid side (511,189 resting ≥ 2,000 ✓) ≈ $1.39/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | SELL | 4.0¢ | 85 | 0 | $25.00 | ✅ scoring — ~21.4% of ask side (136,485 resting ≥ 2,000 ✓) ≈ $1.34/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 43.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~19.5% of ask side (82,545 resting ≥ 5,000 ✓) ≈ $0.81/day (pool ÷ 12 markets) |
| `ussewc-usse-mt-2026-11-03-rep` | BUY | 86.0¢ | 40 | 1 | $25.00 | ✅ scoring — ~19.1% of bid side (510,499 resting ≥ 2,000 ✓) ≈ $0.80/day (pool ÷ 3 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~18.5% of ask side (82,476 resting ≥ 5,000 ✓) ≈ $0.77/day (pool ÷ 12 markets) |
| …and 428 more | | | | | | |

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 40 @ 16¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 16¢ | 40 (40 yours) | ×0.2^1 = 8.0 |
|  | 7¢ | 151 | ×0.2^10 = 0.0 |
|  | 2¢ | 400,250 | ×0.2^15 = 0.0 |
| | | **Σ** | **8.0** |

`yours 8.0 / Σ 8.0 = 99.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.8% = $4.16/day`  

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
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 50 @ 74¢ → $5.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 73¢ | 20 | ×0.1^1 = 2.0 |
|  | 72¢ | 4 | ×0.1^2 = 0.0 |
|  | 71¢ | 150 | ×0.1^3 = 0.2 |
|  | 2¢ | 500,000 | ×0.1^72 = 0.0 |
| | | **Σ** | **52.2** |

`yours 50.0 / Σ 52.2 = 95.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 95.8% = $5.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 100 @ 18¢ → $3.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 116 (100 yours) | ×0.2^0 = 116.0 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **116.0** |

`yours 100.0 / Σ 116.0 = 86.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 86.2% = $3.32/day`  

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
<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> SELL 40 @ 5¢ → $4.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 6¢ | 212 | ×0.1^1 = 21.2 |
|  | 98¢ | 65,250 | ×0.1^93 = 0.0 |
| | | **Σ** | **61.2** |

`yours 40.0 / Σ 61.2 = 65.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 65.4% = $4.08/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem`
2. `usgubewc-usgub-me-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 4¢ → $3.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 7¢ | 170 | ×0.1^3 = 0.2 |
|  | 9¢ | 85 | ×0.1^5 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^94 = 0.0 |
| | | **Σ** | **65.2** |

`yours 40.0 / Σ 65.2 = 61.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.4% = $3.84/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $3.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 97¢ | 60 | ×0.1^1 = 6.0 |
|  | 99¢ | 9,537 | ×0.1^3 = 9.5 |
| | | **Σ** | **65.5** |

`yours 40.0 / Σ 65.5 = 61.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.0% = $3.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $3.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,600 (2,000 yours) | ×0.1^0 = 3,600.0 |
| | | **Σ** | **3,600.0** |

`yours 2,000.0 / Σ 3,600.0 = 55.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 55.6% = $3.47/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 22 @ 13¢ → $1.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 45 (22 yours) | ×0.2^0 = 45.0 |
|  | 1¢ | 100,520 | ×0.2^12 = 0.0 |
| | | **Σ** | **45.0** |

`yours 22.0 / Σ 45.0 = 48.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.9% = $1.88/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> BUY 20 @ 15¢ → $6.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 41 (20 yours) | ×0.25^0 = 41.0 |
|  | 1¢ | 10,301 | ×0.25^14 = 0.0 |
| | | **Σ** | **41.0** |

`yours 20.0 / Σ 41.0 = 48.8%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 48.8% = $6.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>lawec-cryptoleg-2026-12-31</code> SELL 10 @ 38¢ → $5.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 37¢ | 0 | ×0.1^0 = 0.0 |
| ▶ | 38¢ | 21 (10 yours) | ×0.1^1 = 2.1 |
|  | 46¢ | 2 | ×0.1^9 = 0.0 |
|  | 99¢ | 47,100 | ×0.1^62 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 47.4%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 47.4% = $5.92/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 15 @ 22¢ → $1.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 25 (15 yours) | ×0.2^0 = 25.0 |
|  | 25¢ | 907 | ×0.2^3 = 7.3 |
|  | 27¢ | 0 | ×0.2^5 = 0.0 |
|  | 28¢ | 200 | ×0.2^6 = 0.0 |
|  | 29¢ | 0 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^28 = 0.0 |
|  | 98¢ | 65,046 | ×0.2^76 = 0.0 |
| | | **Σ** | **32.2** |

`yours 15.0 / Σ 32.2 = 46.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 46.5% = $1.94/day`  

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 95¢ → $2.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 93¢ | 206 | ×0.1^2 = 2.1 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **92.1** |

`yours 40.0 / Σ 92.1 = 43.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 43.4% = $2.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 40 @ 20¢ → $1.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 20¢ | 96 (40 yours) | ×0.2^1 = 19.2 |
|  | 81¢ | 0 | ×0.2^62 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^79 = 0.0 |
| | | **Σ** | **19.2** |

`yours 8.0 / Σ 19.2 = 41.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 41.6% = $1.74/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 10 @ 10¢ → $1.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 11¢ | 10 | ×0.2^1 = 2.0 |
|  | 12¢ | 15 | ×0.2^2 = 0.6 |
|  | 13¢ | 1,362 | ×0.2^3 = 10.9 |
|  | 14¢ | 1,195 | ×0.2^4 = 1.9 |
|  | 17¢ | 150 | ×0.2^7 = 0.0 |
|  | 18¢ | 0 | ×0.2^8 = 0.0 |
|  | 39¢ | 3,329 | ×0.2^29 = 0.0 |
| | | **Σ** | **25.4** |

`yours 10.0 / Σ 25.4 = 39.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 39.4% = $1.64/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 27¢ → $9.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 20 (10 yours) | ×0.2^0 = 20.0 |
|  | 28¢ | 1 | ×0.2^1 = 0.2 |
|  | 29¢ | 134 | ×0.2^2 = 5.3 |
|  | 31¢ | 23 | ×0.2^4 = 0.0 |
|  | 42¢ | 66 | ×0.2^15 = 0.0 |
|  | 99¢ | 18,378 | ×0.2^72 = 0.0 |
| | | **Σ** | **25.6** |

`yours 10.0 / Σ 25.6 = 39.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 39.1% = $9.77/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> BUY 10 @ 27¢ → $2.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 25 (10 yours) | ×0.1^0 = 25.0 |
|  | 25¢ | 100 | ×0.1^2 = 1.0 |
|  | 22¢ | 291 | ×0.1^5 = 0.0 |
|  | 16¢ | 150 | ×0.1^11 = 0.0 |
|  | 6¢ | 50,000 | ×0.1^21 = 0.0 |
| | | **Σ** | **26.0** |

`yours 10.0 / Σ 26.0 = 38.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 38.5% = $2.40/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-darnor`
2. `enwc-ussep-sc-2026-08-11-rep-ralnor` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-de-2026-11-03-dem</code> BUY 40 @ 95¢ → $2.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 111 (40 yours) | ×0.1^0 = 111.0 |
|  | 2¢ | 500,300 | ×0.1^93 = 0.0 |
| | | **Σ** | **111.0** |

`yours 40.0 / Σ 111.0 = 36.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 36.0% = $2.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-de-2026-11-03-dem` ← this one
2. `ussewc-usse-de-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $2.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,775 (2,000 yours) | ×0.1^0 = 5,775.0 |
| | | **Σ** | **5,775.0** |

`yours 2,000.0 / Σ 5,775.0 = 34.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 34.6% = $2.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 1,290 @ 1¢ → $1.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,368 (1,290 yours) | ×0.1^0 = 4,368.0 |
| | | **Σ** | **4,368.0** |

`yours 1,290.0 / Σ 4,368.0 = 29.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 29.5% = $1.85/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 40 @ 95¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 140 (40 yours) | ×0.1^0 = 140.0 |
|  | 1¢ | 1,950 | ×0.1^94 = 0.0 |
| | | **Σ** | **140.0** |

`yours 40.0 / Σ 140.0 = 28.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.6% = $1.79/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 8 @ 15¢ → $1.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 28 (8 yours) | ×0.2^0 = 27.8 |
|  | 9¢ | 5 | ×0.2^6 = 0.0 |
|  | 1¢ | 300,556 | ×0.2^14 = 0.0 |
| | | **Σ** | **27.8** |

`yours 7.8 / Σ 27.8 = 27.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.9% = $1.07/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 10 @ 18¢ → $0.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 6 | ×0.2^0 = 6.0 |
| ▶ | 18¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 15¢ | 16 | ×0.2^4 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^17 = 0.0 |
| | | **Σ** | **8.0** |

`yours 2.0 / Σ 8.0 = 24.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 24.9% = $0.96/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $0.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 68 (20 yours) | ×0.2^0 = 68.0 |
|  | 6¢ | 295 | ×0.2^2 = 11.8 |
|  | 8¢ | 500 | ×0.2^4 = 0.8 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^93 = 0.0 |
| | | **Σ** | **80.6** |

`yours 20.0 / Σ 80.6 = 24.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 24.8% = $0.95/day`  

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
<details><summary><code>ussewc-usse-ar-2026-11-03-rep</code> BUY 40 @ 93¢ → $1.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 92¢ | 899 | ×0.1^1 = 89.9 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **179.9** |

`yours 40.0 / Σ 179.9 = 22.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 22.2% = $1.39/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem`
2. `ussewc-usse-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> SELL 85 @ 4¢ → $1.34/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 393 (85 yours) | ×0.1^0 = 393.0 |
|  | 6¢ | 367 | ×0.1^2 = 3.7 |
|  | 50¢ | 5,000 | ×0.1^46 = 0.0 |
| | | **Σ** | **396.7** |

`yours 85.0 / Σ 396.7 = 21.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 21.4% = $1.34/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 8 @ 43¢ → $0.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 40 (8 yours) | ×0.2^0 = 39.8 |
|  | 44¢ | 0 | ×0.2^1 = 0.0 |
|  | 79¢ | 234 | ×0.2^36 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^55 = 0.0 |
| | | **Σ** | **39.8** |

`yours 7.8 / Σ 39.8 = 19.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.5% = $0.81/day`  

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
<details><summary><code>ussewc-usse-mt-2026-11-03-rep</code> BUY 40 @ 86¢ → $0.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 87¢ | 14 | ×0.1^0 = 14.0 |
| ▶ | 86¢ | 69 (40 yours) | ×0.1^1 = 6.9 |
|  | 76¢ | 10 | ×0.1^11 = 0.0 |
|  | 74¢ | 206 | ×0.1^13 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^85 = 0.0 |
| | | **Σ** | **20.9** |

`yours 4.0 / Σ 20.9 = 19.1%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 19.1% = $0.80/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `ussewc-usse-mt-2026-11-03-dem`
2. `ussewc-usse-mt-2026-11-03-rep` ← this one
3. `ussewc-usse-mt-2026-11-03-setbod`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 10 @ 29¢ → $0.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 54 (10 yours) | ×0.2^0 = 54.0 |
|  | 47¢ | 150 | ×0.2^18 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^69 = 0.0 |
| | | **Σ** | **54.0** |

`yours 10.0 / Σ 54.0 = 18.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.5% = $0.77/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (66,469 resting) | ~22.4% | ~$16.78 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,092 resting) | ~63.8% | ~$15.95 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,426 resting) | ~62.8% | ~$15.71 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (65,864 resting) | ~13.8% | ~$10.32 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (9,992 resting) | ~22.6% | ~$5.65 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (880,817 resting) | ~6.5% | ~$4.89 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (282,050 resting) | ~5.9% | ~$4.46 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (728,180 resting) | ~4.3% | ~$3.21 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (137,092 resting) | ~8.0% | ~$2.00 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (68,295 resting) | ~29.5% | ~$1.84 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (627,629 resting) | ~6.8% | ~$1.71 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (52,086 resting) | ~2.2% | ~$1.65 |

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
| 2026-08-12 9:52 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:45 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:37 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:36 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:21 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:02 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 7:57 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:57 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:45 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:34 AM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
