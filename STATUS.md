# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-11 1:59 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$547.05/day estimated (ceiling, not promise — details below)

**Earned:** $1,889.44 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-09: **$62.24** · 2026-08-08: **$54.78** · 2026-08-07: **$60.33** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-xavbec` — BUY at the best price, ~$50.38/day for 200 contracts. Runners-up: `paccc-usse-midterms-2026-11-03-rep` (~$34.45/day), `paccc-usse-midterms-2026-11-03-dem` (~$19.48/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$547.05/day (~$22.79/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `pandc-anydis-2027-12-31` | BUY | 13.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~100.0% of bid side (10,311 resting ≥ 10,000 ✓) ≈ $12.50/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (8,866 resting ≥ 5,000 ✓) ≈ $25.00/day (pool ÷ 2 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 10.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~99.9% of bid side (2,594 resting ≥ 2,000 ✓) ≈ $12.49/day |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 38.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~99.0% of bid side (5,500 resting ≥ 5,000 ✓) ≈ $4.13/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~98.7% of bid side (5,326 resting ≥ 5,000 ✓) ≈ $3.80/day (pool ÷ 13 markets) |
| `usgubewc-usgub-ma-2026-11-03-rep` | SELL | 10.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~98.1% of ask side (2,282 resting ≥ 2,000 ✓) ≈ $6.13/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 12.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~96.0% of ask side (2,327 resting ≥ 2,000 ✓) ≈ $6.00/day (pool ÷ 2 markets) |
| `ussewc-usse-la-2026-11-03-dem` | SELL | 33.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,375 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | SELL | 14.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,391 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ar-2026-11-03-dem` | SELL | 40.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,422 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | SELL | 14.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,395 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-rep` | SELL | 20.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of ask side (2,404 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-pa-2026-11-03-rep` | SELL | 16.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~79.9% of ask side (2,429 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-rep` | SELL | 12.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~79.7% of ask side (2,422 resting ≥ 2,000 ✓) ≈ $4.98/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ri-2026-11-03-rep` | SELL | 22.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~76.9% of ask side (2,400 resting ≥ 2,000 ✓) ≈ $3.21/day (pool ÷ 3 markets) |
| `usgubewc-usgub-tn-2026-11-03-dem` | SELL | 12.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~74.6% of ask side (2,416 resting ≥ 2,000 ✓) ≈ $4.66/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~74.1% of ask side (2,700 resting ≥ 2,000 ✓) ≈ $4.63/day (pool ÷ 2 markets) |
| `enwc-ushrp-fl25-2026-08-18-dem-jarmos` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~72.4% of ask side (2,764 resting ≥ 2,000 ✓) ≈ $4.52/day (pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-rep` | BUY | 86.0¢ | 75 | 0 | $25.00 | ✅ scoring — ~72.1% of bid side (2,304 resting ≥ 2,000 ✓) ≈ $4.51/day (pool ÷ 2 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | SELL | 20.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~71.8% of ask side (2,462 resting ≥ 2,000 ✓) ≈ $4.49/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of ask side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `usgubewc-usgub-md-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of ask side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `usgubewc-usgub-mn-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of ask side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `usgubewc-usgub-sd-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of ask side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of ask side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of ask side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of ask side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `usgubewc-usgub-il-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `usgubewc-usgub-hi-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| …and 361 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>pandc-anydis-2027-12-31</code> BUY 10 @ 13¢ → $12.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 1¢ | 10,301 | ×0.25^12 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 100.0% = $12.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 18¢ → $25.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 25¢ | 140 | ×0.2^7 = 0.0 |
|  | 34¢ | 23 | ×0.2^16 = 0.0 |
|  | 99¢ | 8,692 | ×0.2^81 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 100.0% = $25.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 10 @ 10¢ → $12.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 7¢ | 6 | ×0.1^3 = 0.0 |
|  | 6¢ | 29 | ×0.1^4 = 0.0 |
|  | 5¢ | 99 | ×0.1^5 = 0.0 |
|  | 1¢ | 2,450 | ×0.1^9 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.9%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 99.9% = $12.49/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 38¢ → $4.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 39¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 38¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 1¢ | 5,490 | ×0.2^38 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 99.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.0% = $4.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 10 @ 18¢ → $3.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 15¢ | 16 | ×0.2^3 = 0.1 |
|  | 1¢ | 5,300 | ×0.2^17 = 0.0 |
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
<details><summary><code>usgubewc-usgub-ma-2026-11-03-rep</code> SELL 35 @ 10¢ → $6.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 35 (35 yours) | ×0.1^0 = 35.2 |
|  | 11¢ | 7 | ×0.1^1 = 0.7 |
|  | 51¢ | 40 | ×0.1^41 = 0.0 |
|  | 99¢ | 2,200 | ×0.1^89 = 0.0 |
| | | **Σ** | **35.9** |

`yours 35.2 / Σ 35.9 = 98.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 98.1% = $6.13/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem`
2. `usgubewc-usgub-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 40 @ 12¢ → $6.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 13¢ | 9 | ×0.1^1 = 0.9 |
|  | 14¢ | 78 | ×0.1^2 = 0.8 |
|  | 99¢ | 2,200 | ×0.1^87 = 0.0 |
| | | **Σ** | **41.7** |

`yours 40.0 / Σ 41.7 = 96.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 96.0% = $6.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-la-2026-11-03-dem</code> SELL 40 @ 33¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 34¢ | 100 | ×0.1^1 = 10.0 |
|  | 94¢ | 35 | ×0.1^61 = 0.0 |
|  | 99¢ | 2,200 | ×0.1^66 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-la-2026-11-03-dem` ← this one
2. `ussewc-usse-la-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> SELL 40 @ 14¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 15¢ | 100 | ×0.1^1 = 10.0 |
|  | 19¢ | 11 | ×0.1^5 = 0.0 |
|  | 51¢ | 40 | ×0.1^37 = 0.0 |
|  | 99¢ | 2,200 | ×0.1^85 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ar-2026-11-03-dem</code> SELL 40 @ 40¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 41¢ | 100 | ×0.1^1 = 10.0 |
|  | 45¢ | 57 | ×0.1^5 = 0.0 |
|  | 99¢ | 2,225 | ×0.1^59 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem` ← this one
2. `ussewc-usse-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> SELL 40 @ 14¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 15¢ | 100 | ×0.1^1 = 10.0 |
|  | 17¢ | 15 | ×0.1^3 = 0.0 |
|  | 51¢ | 40 | ×0.1^37 = 0.0 |
|  | 99¢ | 2,200 | ×0.1^85 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-rep</code> SELL 40 @ 20¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 21¢ | 100 | ×0.1^1 = 10.0 |
|  | 23¢ | 24 | ×0.1^3 = 0.0 |
|  | 51¢ | 40 | ×0.1^31 = 0.0 |
|  | 99¢ | 2,200 | ×0.1^79 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem`
2. `usgubewc-usgub-ny-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-pa-2026-11-03-rep</code> SELL 40 @ 16¢ → $5.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 17¢ | 100 | ×0.1^1 = 10.0 |
|  | 19¢ | 49 | ×0.1^3 = 0.0 |
|  | 51¢ | 40 | ×0.1^35 = 0.0 |
|  | 99¢ | 2,200 | ×0.1^83 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 79.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 79.9% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-pa-2026-11-03-dem`
2. `usgubewc-usgub-pa-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-rep</code> SELL 40 @ 12¢ → $4.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 13¢ | 100 | ×0.1^1 = 10.0 |
|  | 14¢ | 17 | ×0.1^2 = 0.2 |
|  | 51¢ | 40 | ×0.1^39 = 0.0 |
|  | 99¢ | 2,225 | ×0.1^87 = 0.0 |
| | | **Σ** | **50.2** |

`yours 40.0 / Σ 50.2 = 79.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 79.7% = $4.98/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem`
2. `usgubewc-usgub-md-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ri-2026-11-03-rep</code> SELL 40 @ 22¢ → $3.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 23¢ | 120 | ×0.1^1 = 12.0 |
|  | 51¢ | 40 | ×0.1^29 = 0.0 |
|  | 99¢ | 2,200 | ×0.1^77 = 0.0 |
| | | **Σ** | **52.0** |

`yours 40.0 / Σ 52.0 = 76.9%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 76.9% = $3.21/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ri-2026-11-03-dem`
2. `usgubewc-usgub-ri-2026-11-03-kenblo`
3. `usgubewc-usgub-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-dem</code> SELL 40 @ 12¢ → $4.66/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 13¢ | 136 | ×0.1^1 = 13.6 |
|  | 51¢ | 40 | ×0.1^39 = 0.0 |
|  | 99¢ | 2,200 | ×0.1^87 = 0.0 |
| | | **Σ** | **53.6** |

`yours 40.0 / Σ 53.6 = 74.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 74.6% = $4.66/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-tn-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $4.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,700 (2,000 yours) | ×0.1^0 = 2,700.0 |
| | | **Σ** | **2,700.0** |

`yours 2,000.0 / Σ 2,700.0 = 74.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 74.1% = $4.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-ushrp-fl25-2026-08-18-dem-jarmos</code> SELL 2,000 @ 99¢ → $4.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,764 (2,000 yours) | ×0.1^0 = 2,764.0 |
| | | **Σ** | **2,764.0** |

`yours 2,000.0 / Σ 2,764.0 = 72.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 72.4% = $4.52/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl25-2026-08-18-dem-jarmos` ← this one
2. `enwc-ushrp-fl25-2026-08-18-dem-olilar`

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-rep</code> BUY 75 @ 86¢ → $4.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 86¢ | 104 (75 yours) | ×0.1^0 = 104.0 |
|  | 1¢ | 2,200 | ×0.1^85 = 0.0 |
| | | **Σ** | **104.0** |

`yours 75.0 / Σ 104.0 = 72.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 72.1% = $4.51/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem`
2. `ussewc-usse-ky-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> SELL 40 @ 20¢ → $4.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 21¢ | 157 | ×0.1^1 = 15.7 |
|  | 51¢ | 40 | ×0.1^31 = 0.0 |
|  | 99¢ | 2,225 | ×0.1^79 = 0.0 |
| | | **Σ** | **55.7** |

`yours 40.0 / Σ 55.7 = 71.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.8% = $4.49/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-md-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $4.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-md-2026-11-03-dem` ← this one
2. `usgubewc-usgub-md-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-mn-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $4.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-mn-2026-11-03-dem` ← this one
2. `usgubewc-usgub-mn-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-sd-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-sd-2026-11-03-dem`
2. `usgubewc-usgub-sd-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $4.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ny-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-nm-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $4.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nm-2026-11-03-dem` ← this one
2. `usgubewc-usgub-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-co-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $4.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem` ← this one
2. `usgubewc-usgub-co-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-il-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-il-2026-11-03-dem`
2. `usgubewc-usgub-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-hi-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-hi-2026-11-03-dem`
2. `usgubewc-usgub-hi-2026-11-03-rep` ← this one

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

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-09 | ~$126.83 | $62.24 | 49% |
| 2026-08-08 | ~$111.62 | $54.78 | 49% |
| 2026-08-07 | ~$116.96 | $60.33 | 52% |

Biggest gaps on 2026-08-09: `opdc-mcconnell-resign-2026-11-02` (est ~$9.67 → got $0.25), `scc-hrep-rep-2026-11-03-gte185` (est ~$4.73 → got $0.05), `scc-hrep-rep-2026-11-03-gte210` (est ~$5.21 → got $0.54)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (21,712 resting) | ~67.2% | ~$50.38 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,019,414 resting) | ~45.9% | ~$34.45 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (728,092 resting) | ~26.0% | ~$19.48 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (7,850 resting) | ~71.9% | ~$17.98 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (48,512 resting) | ~10.0% | ~$7.50 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (127,266 resting) | ~7.6% | ~$5.73 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (18,979 resting) | ~6.8% | ~$5.09 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,275 resting) | ~19.8% | ~$4.96 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (843,828 resting) | ~6.0% | ~$4.48 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (885,309 resting) | ~5.9% | ~$4.46 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,987 resting) | ~11.7% | ~$2.93 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (52,713 resting) | ~3.6% | ~$2.71 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Skipped | $1.41 |
| **Total earned** | **$1,889.44** |

1818 reward rows · 38 days with rewards · 378 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-09 | $62.24 | `██████████` |
| 2026-08-08 | $54.78 | `█████████` |
| 2026-08-07 | $60.33 | `██████████` |
| 2026-08-06 | $52.21 | `████████` |
| 2026-08-05 | $31.46 | `█████` |
| 2026-08-04 | $53.94 | `█████████` |
| 2026-08-03 | $44.81 | `███████` |
| 2026-08-02 | $14.05 | `██` |
| 2026-08-01 | $52.30 | `████████` |
| 2026-07-31 | $67.96 | `███████████` |
| 2026-07-30 | $20.67 | `███` |
| 2026-07-29 | $53.60 | `█████████` |
| 2026-07-28 | $79.65 | `█████████████` |
| 2026-07-27 | $125.34 | `████████████████████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $426.12 | `██████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $92.91 |
| `apdc-jerpowgov-2026-12-31` | $78.79 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `opdc-mcconnell-resign-2026-11-02` | $56.96 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.95 |
| `scc-hrep-rep-2026-11-03-gte200` | $36.01 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-11 1:59 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 1:16 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 12:13 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 11:18 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 11:17 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 11:12 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 11:05 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 10:35 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 10:30 AM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 10:27 AM ET | ✅ ok | 1818 | $1889.44 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
