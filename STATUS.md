# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-12 4:42 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$174.74/day estimated (ceiling, not promise — details below)

**Earned:** $2,447.06 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-10: **$557.62** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-09: **$62.24** · 2026-08-08: **$54.78** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$17.39/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$15.90/day), `ewc-usgub-ca-2026-11-03-stehil` (~$13.30/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$174.74/day (~$7.28/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-me-2026-11-03-rep` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,555 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 24.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,548 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 10.0¢ | 31 | 0 | $25.00 | ✅ scoring — ~97.3% of ask side (9,430 resting ≥ 2,000 ✓) ≈ $12.17/day |
| `apdc-jerpowgov-2026-12-31` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~87.4% of ask side (5,318 resting ≥ 5,000 ✓) ≈ $21.84/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 7.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~80.3% of bid side (90,618 resting ≥ 5,000 ✓) ≈ $3.09/day (pool ÷ 13 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 93.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (510,250 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~78.9% of ask side (65,805 resting ≥ 2,000 ✓) ≈ $4.93/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~67.1% of bid side (50,374 resting ≥ 5,000 ✓) ≈ $2.58/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 13.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~63.5% of bid side (400,664 resting ≥ 5,000 ✓) ≈ $2.64/day (pool ÷ 12 markets) |
| `usgubewc-usgub-me-2026-11-03-dem` | BUY | 92.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~55.1% of bid side (500,616 resting ≥ 2,000 ✓) ≈ $3.44/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~53.7% of bid side (12,307 resting ≥ 2,000 ✓) ≈ $2.24/day (pool ÷ 3 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~52.6% of bid side (3,800 resting ≥ 2,000 ✓) ≈ $3.29/day (pool ÷ 2 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 9.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~51.3% of bid side (20,711 resting ≥ 2,000 ✓) ≈ $6.41/day |
| `scc-senate-gop-2026-11-03-49` | BUY | 14.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~48.6% of bid side (200,836 resting ≥ 5,000 ✓) ≈ $1.87/day (pool ÷ 13 markets) |
| `usgubewc-usgub-sc-2026-11-03-rep` | BUY | 92.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~46.5% of bid side (510,286 resting ≥ 2,000 ✓) ≈ $2.91/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 93.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~46.4% of bid side (500,351 resting ≥ 2,000 ✓) ≈ $2.90/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 20.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~41.7% of ask side (82,500 resting ≥ 5,000 ✓) ≈ $1.74/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 40.0¢ | 58 | 0 | $100.00 | ✅ scoring — ~40.1% of ask side (82,724 resting ≥ 5,000 ✓) ≈ $1.67/day (pool ÷ 12 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~40.0% of bid side (5,348 resting ≥ 5,000 ✓) ≈ $10.00/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~32.8% of bid side (6,105 resting ≥ 2,000 ✓) ≈ $2.05/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~31.8% of bid side (6,286 resting ≥ 2,000 ✓) ≈ $1.99/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | BUY | 14.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~30.5% of bid side (10,401 resting ≥ 10,000 ✓) ≈ $3.82/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 9.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~28.4% of ask side (69,237 resting ≥ 5,000 ✓) ≈ $1.18/day (pool ÷ 12 markets) |
| `ussewc-usse-de-2026-11-03-rep` | SELL | 6.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~28.0% of ask side (138,991 resting ≥ 2,000 ✓) ≈ $1.75/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 15.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~27.9% of bid side (300,599 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 37.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~27.4% of bid side (400,350 resting ≥ 5,000 ✓) ≈ $1.14/day (pool ÷ 12 markets) |
| `usgubewc-usgub-hi-2026-11-03-dem` | SELL | 97.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~25.0% of ask side (12,039 resting ≥ 2,000 ✓) ≈ $1.56/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~24.7% of ask side (78,078 resting ≥ 5,000 ✓) ≈ $0.95/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 71.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~24.4% of bid side (500,351 resting ≥ 5,000 ✓) ≈ $1.02/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 13.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~24.2% of bid side (100,621 resting ≥ 5,000 ✓) ≈ $0.93/day (pool ÷ 13 markets) |
| …and 425 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> SELL 40 @ 10¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 51¢ | 40 | ×0.1^41 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^88 = 0.0 |
| | | **Σ** | **40.0** |

`yours 40.0 / Σ 40.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem`
2. `usgubewc-usgub-me-2026-11-03-rep` ← this one

</details>

</details>
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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 31 @ 10¢ → $12.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 31 (31 yours) | ×0.1^0 = 30.5 |
|  | 11¢ | 8 | ×0.1^1 = 0.8 |
|  | 13¢ | 30 | ×0.1^3 = 0.0 |
|  | 14¢ | 32 | ×0.1^4 = 0.0 |
|  | 16¢ | 6 | ×0.1^6 = 0.0 |
|  | 17¢ | 18 | ×0.1^7 = 0.0 |
|  | 18¢ | 348 | ×0.1^8 = 0.0 |
|  | 19¢ | 5 | ×0.1^9 = 0.0 |
|  | 33¢ | 300 | ×0.1^23 = 0.0 |
|  | 35¢ | 151 | ×0.1^25 = 0.0 |
| | … | +1 levels | 0.0 |
| | | **Σ** | **31.3** |

`yours 30.5 / Σ 31.3 = 97.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 97.3% = $12.17/day`  

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 24¢ → $21.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 25¢ | 7 | ×0.2^1 = 1.4 |
|  | 28¢ | 1 | ×0.2^4 = 0.0 |
|  | 29¢ | 134 | ×0.2^5 = 0.0 |
|  | 32¢ | 23 | ×0.2^8 = 0.0 |
|  | 42¢ | 66 | ×0.2^18 = 0.0 |
|  | 99¢ | 5,078 | ×0.2^75 = 0.0 |
| | | **Σ** | **11.4** |

`yours 10.0 / Σ 11.4 = 87.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 87.4% = $21.84/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

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
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> BUY 40 @ 93¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 4¢ → $4.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 6¢ | 50 | ×0.1^2 = 0.5 |
|  | 7¢ | 170 | ×0.1^3 = 0.2 |
|  | 9¢ | 85 | ×0.1^5 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^94 = 0.0 |
| | | **Σ** | **50.7** |

`yours 40.0 / Σ 50.7 = 78.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 78.9% = $4.93/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 100 @ 18¢ → $2.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 149 (100 yours) | ×0.2^0 = 149.0 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **149.0** |

`yours 100.0 / Σ 149.0 = 67.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.1% = $2.58/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 40 @ 13¢ → $2.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 63 (40 yours) | ×0.2^0 = 63.0 |
|  | 7¢ | 151 | ×0.2^6 = 0.0 |
|  | 2¢ | 400,250 | ×0.2^11 = 0.0 |
| | | **Σ** | **63.0** |

`yours 40.0 / Σ 63.0 = 63.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 63.5% = $2.64/day`  

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
<details><summary><code>usgubewc-usgub-me-2026-11-03-dem</code> BUY 40 @ 92¢ → $3.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 91¢ | 326 | ×0.1^1 = 32.6 |
|  | 86¢ | 50 | ×0.1^6 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^90 = 0.0 |
| | | **Σ** | **72.6** |

`yours 40.0 / Σ 72.6 = 55.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 55.1% = $3.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem` ← this one
2. `usgubewc-usgub-me-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-dem</code> BUY 40 @ 95¢ → $2.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 94¢ | 345 | ×0.1^1 = 34.5 |
|  | 1¢ | 11,922 | ×0.1^94 = 0.0 |
| | | **Σ** | **74.5** |

`yours 40.0 / Σ 74.5 = 53.7%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 53.7% = $2.24/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep`

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 40 @ 9¢ → $6.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 78 (40 yours) | ×0.1^0 = 78.0 |
|  | 6¢ | 24 | ×0.1^3 = 0.0 |
|  | 5¢ | 148 | ×0.1^4 = 0.0 |
|  | 3¢ | 11 | ×0.1^6 = 0.0 |
|  | 2¢ | 10,250 | ×0.1^7 = 0.0 |
| | | **Σ** | **78.0** |

`yours 40.0 / Σ 78.0 = 51.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 51.3% = $6.41/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 20 @ 14¢ → $1.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 41 (20 yours) | ×0.2^0 = 41.0 |
|  | 10¢ | 45 | ×0.2^4 = 0.1 |
|  | 9¢ | 341 | ×0.2^5 = 0.1 |
|  | 1¢ | 200,409 | ×0.2^13 = 0.0 |
| | | **Σ** | **41.2** |

`yours 20.0 / Σ 41.2 = 48.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.6% = $1.87/day`  

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
<details><summary><code>usgubewc-usgub-sc-2026-11-03-rep</code> BUY 40 @ 92¢ → $2.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 86 (40 yours) | ×0.1^0 = 86.0 |
|  | 2¢ | 500,000 | ×0.1^90 = 0.0 |
| | | **Σ** | **86.0** |

`yours 40.0 / Σ 86.0 = 46.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 46.5% = $2.91/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sc-2026-11-03-dem`
2. `usgubewc-usgub-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 93¢ → $2.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 86 (40 yours) | ×0.1^0 = 86.0 |
|  | 91¢ | 25 | ×0.1^2 = 0.3 |
|  | 51¢ | 40 | ×0.1^42 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **86.2** |

`yours 40.0 / Σ 86.2 = 46.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 46.4% = $2.90/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 40 @ 20¢ → $1.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 96 (40 yours) | ×0.2^0 = 96.0 |
|  | 25¢ | 84 | ×0.2^5 = 0.0 |
|  | 48¢ | 49 | ×0.2^28 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^78 = 0.0 |
| | | **Σ** | **96.0** |

`yours 40.0 / Σ 96.0 = 41.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 41.7% = $1.74/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 58 @ 40¢ → $1.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 144 (58 yours) | ×0.2^0 = 143.6 |
|  | 43¢ | 10 | ×0.2^3 = 0.1 |
|  | 44¢ | 0 | ×0.2^4 = 0.0 |
|  | 63¢ | 299 | ×0.2^23 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^58 = 0.0 |
| | | **Σ** | **143.7** |

`yours 57.6 / Σ 143.7 = 40.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 40.1% = $1.67/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 10 @ 20¢ → $10.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 25 (10 yours) | ×0.2^0 = 25.0 |
|  | 16¢ | 1 | ×0.2^4 = 0.0 |
|  | 14¢ | 3 | ×0.2^6 = 0.0 |
|  | 13¢ | 3 | ×0.2^7 = 0.0 |
|  | 12¢ | 100 | ×0.2^8 = 0.0 |
|  | 2¢ | 16 | ×0.2^18 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **25.0** |

`yours 10.0 / Σ 25.0 = 40.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 40.0% = $10.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $2.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 6,105 (2,000 yours) | ×0.1^0 = 6,105.0 |
| | | **Σ** | **6,105.0** |

`yours 2,000.0 / Σ 6,105.0 = 32.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 32.8% = $2.05/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $1.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 6,286 (2,000 yours) | ×0.1^0 = 6,286.0 |
| | | **Σ** | **6,286.0** |

`yours 2,000.0 / Σ 6,286.0 = 31.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 31.8% = $1.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> BUY 20 @ 14¢ → $3.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 54 (20 yours) | ×0.25^0 = 54.0 |
|  | 13¢ | 46 | ×0.25^1 = 11.5 |
|  | 1¢ | 10,301 | ×0.25^13 = 0.0 |
| | | **Σ** | **65.5** |

`yours 20.0 / Σ 65.5 = 30.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 30.5% = $3.82/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 40 @ 9¢ → $1.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 141 (40 yours) | ×0.2^0 = 141.0 |
|  | 19¢ | 780 | ×0.2^10 = 0.0 |
|  | 21¢ | 20 | ×0.2^12 = 0.0 |
|  | 25¢ | 1,000 | ×0.2^16 = 0.0 |
|  | 50¢ | 25 | ×0.2^41 = 0.0 |
|  | 98¢ | 65,046 | ×0.2^89 = 0.0 |
| | | **Σ** | **141.0** |

`yours 40.0 / Σ 141.0 = 28.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 28.4% = $1.18/day`  

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
<details><summary><code>ussewc-usse-de-2026-11-03-rep</code> SELL 40 @ 6¢ → $1.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 143 (40 yours) | ×0.1^0 = 143.0 |
|  | 98¢ | 130,500 | ×0.1^92 = 0.0 |
| | | **Σ** | **143.0** |

`yours 40.0 / Σ 143.0 = 28.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.0% = $1.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-de-2026-11-03-dem`
2. `ussewc-usse-de-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 8 @ 15¢ → $1.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 28 (8 yours) | ×0.2^0 = 27.8 |
|  | 9¢ | 5 | ×0.2^6 = 0.0 |
|  | 1¢ | 300,566 | ×0.2^14 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> BUY 40 @ 37¢ → $1.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 145 (40 yours) | ×0.2^0 = 145.0 |
|  | 36¢ | 5 | ×0.2^1 = 1.0 |
|  | 34¢ | 0 | ×0.2^3 = 0.0 |
|  | 2¢ | 400,000 | ×0.2^35 = 0.0 |
| | | **Σ** | **146.0** |

`yours 40.0 / Σ 146.0 = 27.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 27.4% = $1.14/day`  

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
<details><summary><code>usgubewc-usgub-hi-2026-11-03-dem</code> SELL 40 @ 97¢ → $1.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 99¢ | 11,999 | ×0.1^2 = 120.0 |
| | | **Σ** | **160.0** |

`yours 40.0 / Σ 160.0 = 25.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 25.0% = $1.56/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem` ← this one
2. `usgubewc-usgub-hi-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $0.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 60 (20 yours) | ×0.2^0 = 60.0 |
|  | 6¢ | 507 | ×0.2^2 = 20.3 |
|  | 8¢ | 500 | ×0.2^4 = 0.8 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^93 = 0.0 |
| | | **Σ** | **81.1** |

`yours 20.0 / Σ 81.1 = 24.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 24.7% = $0.95/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 10 @ 71¢ → $1.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 71¢ | 41 (10 yours) | ×0.2^0 = 41.0 |
|  | 2¢ | 102 | ×0.2^69 = 0.0 |
|  | 1¢ | 500,208 | ×0.2^70 = 0.0 |
| | | **Σ** | **41.0** |

`yours 10.0 / Σ 41.0 = 24.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 24.4% = $1.02/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 22 @ 13¢ → $0.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 91 (22 yours) | ×0.2^0 = 91.0 |
|  | 1¢ | 100,530 | ×0.2^12 = 0.0 |
| | | **Σ** | **91.0** |

`yours 22.0 / Σ 91.0 = 24.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 24.2% = $0.93/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,641 resting) | ~69.6% | ~$17.39 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,478 resting) | ~21.2% | ~$15.90 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (270,298 resting) | ~17.7% | ~$13.30 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,066,186 resting) | ~16.9% | ~$12.64 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (65,575 resting) | ~16.3% | ~$12.20 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,540 resting) | ~41.1% | ~$10.27 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,125 resting) | ~27.5% | ~$6.87 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (865,844 resting) | ~5.3% | ~$3.98 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (144,014 resting) | ~4.6% | ~$3.46 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (125,953 resting) | ~13.5% | ~$3.36 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (91,457 resting) | ~3.9% | ~$2.90 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (262,025 resting) | ~3.5% | ~$2.61 |

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
| 2026-08-12 4:42 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 2:46 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 1:09 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:17 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:31 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:24 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:10 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:03 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 10:48 PM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 10:35 PM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
