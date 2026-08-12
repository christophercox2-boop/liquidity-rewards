# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-12 8:37 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$146.67/day estimated (ceiling, not promise — details below)

**Earned:** $2,447.06 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-10: **$557.62** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-09: **$62.24** · 2026-08-08: **$54.78** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$14.86/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$13.96/day), `ewc-usgub-ga-2026-11-03-dem` (~$12.35/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$146.67/day (~$6.11/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 24.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,548 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 53.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~99.1% of bid side (500,259 resting ≥ 2,000 ✓) ≈ $6.19/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~98.7% of bid side (50,580 resting ≥ 5,000 ✓) ≈ $3.80/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~86.2% of bid side (50,341 resting ≥ 5,000 ✓) ≈ $3.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 7.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~80.3% of bid side (90,618 resting ≥ 5,000 ✓) ≈ $3.09/day (pool ÷ 13 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (208,313 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 93.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (510,250 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (610,250 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.4% of ask side (65,770 resting ≥ 2,000 ✓) ≈ $3.84/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~60.9% of ask side (9,837 resting ≥ 2,000 ✓) ≈ $3.80/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~55.6% of bid side (3,600 resting ≥ 2,000 ✓) ≈ $3.47/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 13.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~48.9% of bid side (100,575 resting ≥ 5,000 ✓) ≈ $1.88/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 14.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~48.6% of bid side (200,836 resting ≥ 5,000 ✓) ≈ $1.87/day (pool ÷ 13 markets) |
| `lawec-cryptoleg-2026-12-31` | SELL | 38.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~47.6% of ask side (47,302 resting ≥ 2,000 ✓) ≈ $5.95/day |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 93.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~46.5% of bid side (500,286 resting ≥ 2,000 ✓) ≈ $2.91/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | BUY | 15.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~45.5% of bid side (10,354 resting ≥ 10,000 ✓) ≈ $5.68/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-rep` | SELL | 6.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~45.2% of ask side (65,999 resting ≥ 2,000 ✓) ≈ $2.83/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~39.1% of bid side (5,115 resting ≥ 2,000 ✓) ≈ $2.44/day (pool ÷ 2 markets) |
| `usgubewc-usgub-sd-2026-11-03-dem` | BUY | 1.0¢ | 1,660 | 1 | $25.00 | ✅ scoring — ~32.2% of bid side (2,640 resting ≥ 2,000 ✓) ≈ $2.01/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 16.0¢ | 40 | 1 | $100.00 | ✅ scoring — ~32.0% of bid side (400,658 resting ≥ 5,000 ✓) ≈ $1.33/day (pool ÷ 12 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 27.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~31.7% of ask side (18,652 resting ≥ 5,000 ✓) ≈ $7.92/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 1,290 | 0 | $25.00 | ✅ scoring — ~31.3% of bid side (4,125 resting ≥ 2,000 ✓) ≈ $1.95/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 15.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~27.9% of bid side (300,599 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 26.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~27.7% of bid side (15,458 resting ≥ 5,000 ✓) ≈ $6.93/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | SELL | 22.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~26.0% of ask side (10,322 resting ≥ 10,000 ✓) ≈ $3.25/day (pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | SELL | 11.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~24.0% of ask side (10,907 resting ≥ 5,000 ✓) ≈ $6.01/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | SELL | 4.0¢ | 85 | 0 | $25.00 | ✅ scoring — ~21.4% of ask side (136,485 resting ≥ 2,000 ✓) ≈ $1.34/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-dem` | BUY | 1.0¢ | 1,200 | 1 | $25.00 | ✅ scoring — ~20.3% of bid side (2,300 resting ≥ 2,000 ✓) ≈ $1.27/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 43.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~19.5% of ask side (82,489 resting ≥ 5,000 ✓) ≈ $0.81/day (pool ÷ 12 markets) |
| `ussewc-usse-mt-2026-11-03-rep` | BUY | 86.0¢ | 40 | 1 | $25.00 | ✅ scoring — ~19.1% of bid side (510,499 resting ≥ 2,000 ✓) ≈ $0.80/day (pool ÷ 3 markets) |
| …and 414 more | | | | | | |

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
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 50 @ 53¢ → $6.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 53¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 52¢ | 4 | ×0.1^1 = 0.4 |
|  | 51¢ | 5 | ×0.1^2 = 0.1 |
|  | 2¢ | 500,000 | ×0.1^51 = 0.0 |
| | | **Σ** | **50.5** |

`yours 50.0 / Σ 50.5 = 99.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.1% = $6.19/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 10 @ 18¢ → $3.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 15¢ | 16 | ×0.2^3 = 0.1 |
|  | 2¢ | 50,250 | ×0.2^16 = 0.0 |
| | | **Σ** | **10.1** |

`yours 10.0 / Σ 10.1 = 98.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.7% = $3.80/day`  

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
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> SELL 40 @ 4¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 98¢ | 208,063 | ×0.1^94 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

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
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> BUY 40 @ 95¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 2¢ | 600,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

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
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $3.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 97¢ | 60 | ×0.1^1 = 6.0 |
|  | 99¢ | 9,727 | ×0.1^3 = 9.7 |
| | | **Σ** | **65.7** |

`yours 40.0 / Σ 65.7 = 60.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.9% = $3.80/day`  

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
|  | 1¢ | 100,530 | ×0.2^12 = 0.0 |
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
<details><summary><code>lawec-cryptoleg-2026-12-31</code> SELL 10 @ 38¢ → $5.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 21 (10 yours) | ×0.1^0 = 21.0 |
|  | 46¢ | 2 | ×0.1^8 = 0.0 |
|  | 99¢ | 47,279 | ×0.1^61 = 0.0 |
| | | **Σ** | **21.0** |

`yours 10.0 / Σ 21.0 = 47.6%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 47.6% = $5.95/day`  

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 93¢ → $2.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 86 (40 yours) | ×0.1^0 = 86.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **86.0** |

`yours 40.0 / Σ 86.0 = 46.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 46.5% = $2.91/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> BUY 20 @ 15¢ → $5.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 41 (20 yours) | ×0.25^0 = 41.0 |
|  | 14¢ | 12 | ×0.25^1 = 3.0 |
|  | 1¢ | 10,301 | ×0.25^14 = 0.0 |
| | | **Σ** | **44.0** |

`yours 20.0 / Σ 44.0 = 45.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 45.5% = $5.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> SELL 40 @ 6¢ → $2.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 7¢ | 484 | ×0.1^1 = 48.4 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **88.4** |

`yours 40.0 / Σ 88.4 = 45.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 45.2% = $2.83/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem`
2. `usgubewc-usgub-me-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $2.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,115 (2,000 yours) | ×0.1^0 = 5,115.0 |
| | | **Σ** | **5,115.0** |

`yours 2,000.0 / Σ 5,115.0 = 39.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 39.1% = $2.44/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-sd-2026-11-03-dem</code> BUY 1,660 @ 1¢ → $2.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 280 | ×0.1^0 = 280.0 |
| ▶ | 1¢ | 2,360 (1,660 yours) | ×0.1^1 = 236.0 |
| | | **Σ** | **516.0** |

`yours 166.0 / Σ 516.0 = 32.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 32.2% = $2.01/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sd-2026-11-03-dem` ← this one
2. `usgubewc-usgub-sd-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 40 @ 16¢ → $1.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 17 | ×0.2^0 = 17.0 |
| ▶ | 16¢ | 40 (40 yours) | ×0.2^1 = 8.0 |
|  | 7¢ | 151 | ×0.2^10 = 0.0 |
|  | 2¢ | 400,250 | ×0.2^15 = 0.0 |
| | | **Σ** | **25.0** |

`yours 8.0 / Σ 25.0 = 32.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 32.0% = $1.33/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 27¢ → $7.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 20 (10 yours) | ×0.2^0 = 20.0 |
|  | 28¢ | 31 | ×0.2^1 = 6.2 |
|  | 29¢ | 134 | ×0.2^2 = 5.3 |
|  | 31¢ | 23 | ×0.2^4 = 0.0 |
|  | 42¢ | 66 | ×0.2^15 = 0.0 |
|  | 99¢ | 18,378 | ×0.2^72 = 0.0 |
| | | **Σ** | **31.6** |

`yours 10.0 / Σ 31.6 = 31.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 31.7% = $7.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 1,290 @ 1¢ → $1.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,125 (1,290 yours) | ×0.1^0 = 4,125.0 |
| | | **Σ** | **4,125.0** |

`yours 1,290.0 / Σ 4,125.0 = 31.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 31.3% = $1.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 40 @ 26¢ → $6.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 144 (40 yours) | ×0.2^0 = 144.0 |
|  | 24¢ | 7 | ×0.2^2 = 0.3 |
|  | 16¢ | 1 | ×0.2^10 = 0.0 |
|  | 14¢ | 3 | ×0.2^12 = 0.0 |
|  | 13¢ | 3 | ×0.2^13 = 0.0 |
|  | 12¢ | 100 | ×0.2^14 = 0.0 |
|  | 1¢ | 15,200 | ×0.2^25 = 0.0 |
| | | **Σ** | **144.3** |

`yours 40.0 / Σ 144.3 = 27.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 27.7% = $6.93/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 20 @ 22¢ → $3.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 77 (20 yours) | ×0.25^0 = 77.0 |
|  | 34¢ | 148 | ×0.25^12 = 0.0 |
|  | 50¢ | 25 | ×0.25^28 = 0.0 |
|  | 99¢ | 10,072 | ×0.25^77 = 0.0 |
| | | **Σ** | **77.0** |

`yours 20.0 / Σ 77.0 = 26.0%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 26.0% = $3.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> SELL 50 @ 11¢ → $6.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 104 (50 yours) | ×0.2^0 = 104.0 |
|  | 12¢ | 250 | ×0.2^1 = 50.0 |
|  | 13¢ | 993 | ×0.2^2 = 39.7 |
|  | 14¢ | 1,726 | ×0.2^3 = 13.8 |
|  | 16¢ | 1,949 | ×0.2^5 = 0.6 |
| | | **Σ** | **208.2** |

`yours 50.0 / Σ 208.2 = 24.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 24.0% = $6.01/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

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
<details><summary><code>usgubewc-usgub-wy-2026-11-03-dem</code> BUY 1,200 @ 1¢ → $1.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 400 | ×0.1^0 = 400.0 |
| ▶ | 1¢ | 1,900 (1,200 yours) | ×0.1^1 = 190.0 |
| | | **Σ** | **590.0** |

`yours 120.0 / Σ 590.0 = 20.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 20.3% = $1.27/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem` ← this one
2. `usgubewc-usgub-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 8 @ 43¢ → $0.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 40 (8 yours) | ×0.2^0 = 39.8 |
|  | 44¢ | 0 | ×0.2^1 = 0.0 |
|  | 79¢ | 178 | ×0.2^36 = 0.0 |
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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,345 resting) | ~59.4% | ~$14.86 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (36,701 resting) | ~55.8% | ~$13.96 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (62,385 resting) | ~16.5% | ~$12.35 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (369,487 resting) | ~15.7% | ~$11.77 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,066,538 resting) | ~12.8% | ~$9.61 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (71,989 resting) | ~12.6% | ~$9.49 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (10,225 resting) | ~30.0% | ~$7.49 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (876,760 resting) | ~9.7% | ~$7.26 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (649,927 resting) | ~6.2% | ~$4.64 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (275,467 resting) | ~4.3% | ~$3.22 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,037,288 resting) | ~3.2% | ~$2.37 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (148,095 resting) | ~3.1% | ~$2.33 |

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
| 2026-08-12 8:37 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:36 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:21 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 8:02 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 7:57 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:57 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:45 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:34 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:32 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:29 AM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
