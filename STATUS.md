# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-11 7:21 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$151.61/day estimated (ceiling, not promise — details below)

**Earned:** $1,889.44 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-09: **$62.24** · 2026-08-08: **$54.78** · 2026-08-07: **$60.33** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-xavbec` — BUY at the best price, ~$22.73/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-angcra` (~$21.35/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$17.99/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$151.61/day (~$6.32/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 22.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~99.9% of bid side (305,320 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 38.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~99.0% of bid side (305,460 resting ≥ 5,000 ✓) ≈ $4.13/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~98.7% of bid side (55,501 resting ≥ 5,000 ✓) ≈ $3.80/day (pool ÷ 13 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | BUY | 66.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~95.2% of bid side (312,804 resting ≥ 2,000 ✓) ≈ $5.95/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 67.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~94.8% of bid side (512,278 resting ≥ 2,000 ✓) ≈ $5.93/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 25.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~83.3% of bid side (405,220 resting ≥ 5,000 ✓) ≈ $3.47/day (pool ÷ 12 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | SELL | 6.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (67,280 resting ≥ 2,000 ✓) ≈ $5.21/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 20.0¢ | 5 | 3 | $100.00 | ✅ scoring — ~74.6% of bid side (810,553 resting ≥ 5,000 ✓) ≈ $3.11/day (pool ÷ 12 markets) |
| `ussewc-usse-or-2026-11-03-rep` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~74.0% of ask side (132,479 resting ≥ 2,000 ✓) ≈ $4.62/day (pool ÷ 2 markets) |
| `usgubewc-usgub-tn-2026-11-03-rep` | BUY | 96.0¢ | 60 | 0 | $25.00 | ✅ scoring — ~58.3% of bid side (2,486 resting ≥ 2,000 ✓) ≈ $3.64/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 13.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~53.7% of bid side (105,561 resting ≥ 5,000 ✓) ≈ $2.06/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 29.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~52.6% of ask side (69,337 resting ≥ 5,000 ✓) ≈ $2.19/day (pool ÷ 12 markets) |
| `usgubewc-usgub-or-2026-11-03-rep` | SELL | 12.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~50.0% of ask side (77,247 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `usgubewc-usgub-nh-2026-11-03-rep` | BUY | 78.0¢ | 40 | 1 | $25.00 | ✅ scoring — ~50.0% of bid side (12,294 resting ≥ 2,000 ✓) ≈ $3.12/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 7.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~44.9% of ask side (142,451 resting ≥ 2,000 ✓) ≈ $2.81/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | BUY | 13.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~40.8% of bid side (10,350 resting ≥ 10,000 ✓) ≈ $5.10/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~39.4% of bid side (5,078 resting ≥ 2,000 ✓) ≈ $2.46/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 98.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~38.5% of bid side (2,354 resting ≥ 2,000 ✓) ≈ $2.40/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~37.0% of bid side (55,268 resting ≥ 5,000 ✓) ≈ $1.42/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 17.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~33.3% of bid side (22,579 resting ≥ 2,000 ✓) ≈ $4.17/day |
| `scc-senate-gop-2026-11-03-52` | BUY | 15.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~32.6% of bid side (305,585 resting ≥ 5,000 ✓) ≈ $1.26/day (pool ÷ 13 markets) |
| `ussewc-usse-ky-2026-11-03-rep` | BUY | 90.0¢ | 80 | 0 | $25.00 | ✅ scoring — ~30.8% of bid side (512,535 resting ≥ 2,000 ✓) ≈ $1.92/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 92.0¢ | 60 | 1 | $25.00 | ✅ scoring — ~28.6% of bid side (502,275 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 2 markets) |
| `ussewc-usse-de-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~26.5% of bid side (502,432 resting ≥ 2,000 ✓) ≈ $1.66/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 25.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~26.3% of ask side (79,033 resting ≥ 5,000 ✓) ≈ $1.01/day (pool ÷ 13 markets) |
| `usgubewc-usgub-ma-2026-11-03-dem` | BUY | 94.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~26.3% of bid side (2,352 resting ≥ 2,000 ✓) ≈ $1.64/day (pool ÷ 2 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~26.2% of bid side (502,440 resting ≥ 2,000 ✓) ≈ $1.64/day (pool ÷ 2 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 19.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~23.8% of ask side (13,048 resting ≥ 2,000 ✓) ≈ $2.98/day |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 62.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~23.7% of bid side (405,838 resting ≥ 5,000 ✓) ≈ $0.99/day (pool ÷ 12 markets) |
| `pandc-anydis-2027-12-31` | SELL | 25.0¢ | 14 | 0 | $50.00 | ✅ scoring — ~22.9% of ask side (12,684 resting ≥ 10,000 ✓) ≈ $2.87/day (pool ÷ 2 markets) |
| …and 1074 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 17 @ 22¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 17 (17 yours) | ×0.2^0 = 17.4 |
|  | 19¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 305,300 | ×0.2^21 = 0.0 |
| | | **Σ** | **17.4** |

`yours 17.4 / Σ 17.4 = 99.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.9% = $3.84/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 38¢ → $4.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 39¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 38¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 2¢ | 300,250 | ×0.2^37 = 0.0 |
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
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> BUY 10 @ 66¢ → $5.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 66¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 65¢ | 5 | ×0.1^1 = 0.5 |
|  | 55¢ | 89 | ×0.1^11 = 0.0 |
|  | 54¢ | 500 | ×0.1^12 = 0.0 |
|  | 2¢ | 300,000 | ×0.1^64 = 0.0 |
| | | **Σ** | **10.5** |

`yours 10.0 / Σ 10.5 = 95.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 95.2% = $5.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 25 @ 67¢ → $5.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 25 (25 yours) | ×0.1^0 = 25.0 |
|  | 66¢ | 10 | ×0.1^1 = 1.0 |
|  | 65¢ | 37 | ×0.1^2 = 0.4 |
|  | 61¢ | 6 | ×0.1^6 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^65 = 0.0 |
| | | **Σ** | **26.4** |

`yours 25.0 / Σ 26.4 = 94.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.8% = $5.93/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 10 @ 25¢ → $3.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 24¢ | 10 | ×0.2^1 = 2.0 |
|  | 2¢ | 400,000 | ×0.2^23 = 0.0 |
| | | **Σ** | **12.0** |

`yours 10.0 / Σ 12.0 = 83.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 83.3% = $3.47/day`  

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
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> SELL 50 @ 6¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 60 (50 yours) | ×0.1^0 = 60.0 |
|  | 10¢ | 60 | ×0.1^4 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^92 = 0.0 |
| | | **Σ** | **60.0** |

`yours 50.0 / Σ 60.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 5 @ 20¢ → $3.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 0 | ×0.2^0 = 0.0 |
|  | 22¢ | 0 | ×0.2^1 = 0.0 |
| ▶ | 20¢ | 5 (5 yours) | ×0.2^3 = 0.0 |
|  | 19¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 5,247 | ×0.2^21 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.0 / Σ 0.1 = 74.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 74.6% = $3.11/day`  

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
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> SELL 40 @ 5¢ → $4.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 54 (40 yours) | ×0.1^0 = 54.0 |
|  | 8¢ | 63 | ×0.1^3 = 0.1 |
|  | 98¢ | 130,500 | ×0.1^93 = 0.0 |
| | | **Σ** | **54.1** |

`yours 40.0 / Σ 54.1 = 74.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 74.0% = $4.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-tn-2026-11-03-rep</code> BUY 60 @ 96¢ → $3.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 87 (60 yours) | ×0.1^0 = 87.0 |
|  | 95¢ | 159 | ×0.1^1 = 15.9 |
|  | 89¢ | 40 | ×0.1^7 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^95 = 0.0 |
| | | **Σ** | **102.9** |

`yours 60.0 / Σ 102.9 = 58.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 58.3% = $3.64/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-tn-2026-11-03-dem`
2. `usgubewc-usgub-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 22 @ 13¢ → $2.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 41 (22 yours) | ×0.2^0 = 41.0 |
|  | 1¢ | 105,520 | ×0.2^12 = 0.0 |
| | | **Σ** | **41.0** |

`yours 22.0 / Σ 41.0 = 53.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.7% = $2.06/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 10 @ 29¢ → $2.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 30¢ | 45 | ×0.2^1 = 9.0 |
|  | 47¢ | 100 | ×0.2^18 = 0.0 |
|  | 98¢ | 65,046 | ×0.2^69 = 0.0 |
| | | **Σ** | **19.0** |

`yours 10.0 / Σ 19.0 = 52.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 52.6% = $2.19/day`  

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
<details><summary><code>usgubewc-usgub-or-2026-11-03-rep</code> SELL 40 @ 12¢ → $3.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 80 (40 yours) | ×0.1^0 = 80.0 |
|  | 26¢ | 40 | ×0.1^14 = 0.0 |
|  | 51¢ | 40 | ×0.1^39 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^86 = 0.0 |
| | | **Σ** | **80.0** |

`yours 40.0 / Σ 80.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-or-2026-11-03-dem`
2. `usgubewc-usgub-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-nh-2026-11-03-rep</code> BUY 40 @ 78¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 79¢ | 4 | ×0.1^0 = 4.0 |
| ▶ | 78¢ | 40 (40 yours) | ×0.1^1 = 4.0 |
|  | 75¢ | 10 | ×0.1^4 = 0.0 |
|  | 65¢ | 40 | ×0.1^14 = 0.0 |
|  | 1¢ | 12,200 | ×0.1^78 = 0.0 |
| | | **Σ** | **8.0** |

`yours 4.0 / Σ 8.0 = 50.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 50.0% = $3.12/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-nh-2026-11-03-dem`
2. `usgubewc-usgub-nh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 40 @ 7¢ → $2.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 89 (40 yours) | ×0.1^0 = 89.0 |
|  | 98¢ | 130,500 | ×0.1^91 = 0.0 |
| | | **Σ** | **89.0** |

`yours 40.0 / Σ 89.0 = 44.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 44.9% = $2.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> BUY 20 @ 13¢ → $5.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 49 (20 yours) | ×0.25^0 = 49.0 |
|  | 1¢ | 10,301 | ×0.25^12 = 0.0 |
| | | **Σ** | **49.0** |

`yours 20.0 / Σ 49.0 = 40.8%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 40.8% = $5.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $2.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,078 (2,000 yours) | ×0.1^0 = 5,078.0 |
| | | **Σ** | **5,078.0** |

`yours 2,000.0 / Σ 5,078.0 = 39.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 39.4% = $2.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ar-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 40 @ 98¢ → $2.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 98¢ | 104 (40 yours) | ×0.1^0 = 104.0 |
|  | 50¢ | 50 | ×0.1^48 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^97 = 0.0 |
| | | **Σ** | **104.0** |

`yours 40.0 / Σ 104.0 = 38.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 38.5% = $2.40/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 18¢ → $1.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 23 (10 yours) | ×0.2^0 = 23.0 |
|  | 17¢ | 20 | ×0.2^1 = 4.0 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **27.0** |

`yours 10.0 / Σ 27.0 = 37.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.0% = $1.42/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 5 @ 17¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 15 (5 yours) | ×0.1^0 = 15.0 |
|  | 7¢ | 4 | ×0.1^10 = 0.0 |
|  | 6¢ | 11 | ×0.1^11 = 0.0 |
|  | 5¢ | 99 | ×0.1^12 = 0.0 |
|  | 2¢ | 10,250 | ×0.1^15 = 0.0 |
| | | **Σ** | **15.0** |

`yours 5.0 / Σ 15.0 = 33.3%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 33.3% = $4.17/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 8 @ 15¢ → $1.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 24 (8 yours) | ×0.2^0 = 23.8 |
|  | 9¢ | 5 | ×0.2^6 = 0.0 |
|  | 1¢ | 305,556 | ×0.2^14 = 0.0 |
| | | **Σ** | **23.8** |

`yours 7.8 / Σ 23.8 = 32.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.6% = $1.26/day`  

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
<details><summary><code>ussewc-usse-ky-2026-11-03-rep</code> BUY 80 @ 90¢ → $1.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 260 (80 yours) | ×0.1^0 = 260.0 |
|  | 84¢ | 75 | ×0.1^6 = 0.0 |
|  | 2¢ | 500,000 | ×0.1^88 = 0.0 |
| | | **Σ** | **260.0** |

`yours 80.0 / Σ 260.0 = 30.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 30.8% = $1.92/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem`
2. `ussewc-usse-ky-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 60 @ 92¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 93¢ | 15 | ×0.1^0 = 15.0 |
| ▶ | 92¢ | 60 (60 yours) | ×0.1^1 = 6.0 |
|  | 2¢ | 500,000 | ×0.1^91 = 0.0 |
| | | **Σ** | **21.0** |

`yours 6.0 / Σ 21.0 = 28.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.6% = $1.79/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-de-2026-11-03-dem</code> BUY 40 @ 95¢ → $1.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 150 (40 yours) | ×0.1^0 = 150.0 |
|  | 93¢ | 82 | ×0.1^2 = 0.8 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **150.8** |

`yours 40.0 / Σ 150.8 = 26.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.5% = $1.66/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-de-2026-11-03-dem` ← this one
2. `ussewc-usse-de-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 5 @ 25¢ → $1.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 13 (5 yours) | ×0.2^0 = 12.9 |
|  | 27¢ | 100 | ×0.2^2 = 4.0 |
|  | 28¢ | 265 | ×0.2^3 = 2.1 |
|  | 50¢ | 100 | ×0.2^25 = 0.0 |
|  | 97¢ | 65,717 | ×0.2^72 = 0.0 |
| | | **Σ** | **19.0** |

`yours 5.0 / Σ 19.0 = 26.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.3% = $1.01/day`  

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
<details><summary><code>usgubewc-usgub-ma-2026-11-03-dem</code> BUY 40 @ 94¢ → $1.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 152 (40 yours) | ×0.1^0 = 152.0 |
|  | 1¢ | 2,200 | ×0.1^93 = 0.0 |
| | | **Σ** | **152.0** |

`yours 40.0 / Σ 152.0 = 26.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.3% = $1.64/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ma-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ma-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> BUY 40 @ 95¢ → $1.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 152 (40 yours) | ×0.1^0 = 152.0 |
|  | 93¢ | 88 | ×0.1^2 = 0.9 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **152.9** |

`yours 40.0 / Σ 152.9 = 26.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.2% = $1.64/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 5 @ 19¢ → $2.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 21 (5 yours) | ×0.1^0 = 21.0 |
|  | 28¢ | 32 | ×0.1^9 = 0.0 |
|  | 33¢ | 693 | ×0.1^14 = 0.0 |
|  | 35¢ | 101 | ×0.1^16 = 0.0 |
|  | 99¢ | 12,201 | ×0.1^80 = 0.0 |
| | | **Σ** | **21.0** |

`yours 5.0 / Σ 21.0 = 23.8%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 23.8% = $2.98/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 5 @ 62¢ → $0.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 62¢ | 21 (5 yours) | ×0.2^0 = 21.0 |
|  | 59¢ | 10 | ×0.2^3 = 0.1 |
|  | 57¢ | 109 | ×0.2^5 = 0.0 |
|  | 53¢ | 108 | ×0.2^9 = 0.0 |
|  | 50¢ | 25 | ×0.2^12 = 0.0 |
|  | 49¢ | 115 | ×0.2^13 = 0.0 |
|  | 2¢ | 400,250 | ×0.2^60 = 0.0 |
| | | **Σ** | **21.1** |

`yours 5.0 / Σ 21.1 = 23.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 23.7% = $0.99/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 14 @ 25¢ → $2.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 61 (14 yours) | ×0.25^0 = 61.0 |
|  | 30¢ | 5 | ×0.25^5 = 0.0 |
|  | 34¢ | 99 | ×0.25^9 = 0.0 |
|  | 50¢ | 25 | ×0.25^25 = 0.0 |
|  | 99¢ | 12,493 | ×0.25^74 = 0.0 |
| | | **Σ** | **61.0** |

`yours 14.0 / Σ 61.0 = 22.9%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 22.9% = $2.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-09 | ~$114.65 | $62.24 | 54% |

Biggest gaps on 2026-08-09: `opdc-mcconnell-resign-2026-11-02` (est ~$8.35 → got $0.25), `scc-hrep-rep-2026-11-03-gte185` (est ~$4.25 → got $0.05), `scc-senate-gop-2026-11-03-48` (est ~$3.91 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,052,211 resting) | ~30.3% | ~$22.73 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (300,823 resting) | ~85.4% | ~$21.35 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (300,274 resting) | ~71.9% | ~$17.99 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (25,900 resting) | ~31.6% | ~$7.90 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (25,917 resting) | ~31.5% | ~$7.87 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (313,099 resting) | ~9.9% | ~$7.45 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (52,773 resting) | ~9.8% | ~$7.34 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (850,528 resting) | ~8.5% | ~$6.41 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,876 resting) | ~21.0% | ~$5.26 |
| `paccc-usho-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (885,341 resting) | ~5.9% | ~$4.41 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (59,779 resting) | ~5.7% | ~$4.27 |
| `paccc-usse-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,007,043 resting) | ~5.4% | ~$4.07 |

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
| 2026-08-11 7:21 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 7:20 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 7:08 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 7:06 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 6:08 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 6:04 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 5:55 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 5:51 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 5:49 PM ET | ✅ ok | 1818 | $1889.44 |
| 2026-08-11 5:07 PM ET | ✅ ok | 1818 | $1889.44 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
