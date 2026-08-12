# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-12 6:57 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$164.28/day estimated (ceiling, not promise — details below)

**Earned:** $2,447.06 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-10: **$557.62** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-09: **$62.24** · 2026-08-08: **$54.78** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$16.44/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$14.81/day), `ewc-usgub-ca-2026-11-03-stehil` (~$14.27/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$164.28/day (~$6.84/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `usgubewc-usgub-me-2026-11-03-rep` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,515 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 24.0¢ | 17 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (300,548 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 7.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~80.3% of bid side (90,618 resting ≥ 5,000 ✓) ≈ $3.09/day (pool ÷ 13 markets) |
| `usgubewc-usgub-nm-2026-11-03-dem` | BUY | 93.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (510,250 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `lawec-cryptoleg-2026-12-31` | SELL | 37.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~79.8% of ask side (48,035 resting ≥ 2,000 ✓) ≈ $9.98/day |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~67.1% of bid side (50,374 resting ≥ 5,000 ✓) ≈ $2.58/day (pool ÷ 13 markets) |
| `lawec-cryptoleg-2026-12-31` | BUY | 33.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~67.0% of bid side (36,633 resting ≥ 2,000 ✓) ≈ $8.37/day |
| `ussewc-usse-co-2026-11-03-dem` | BUY | 94.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.5% of bid side (510,265 resting ≥ 2,000 ✓) ≈ $3.85/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.4% of ask side (65,685 resting ≥ 2,000 ✓) ≈ $3.84/day (pool ÷ 2 markets) |
| `usgubewc-usgub-me-2026-11-03-dem` | BUY | 94.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~55.2% of bid side (500,564 resting ≥ 2,000 ✓) ≈ $3.45/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 23.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~49.3% of ask side (19,311 resting ≥ 5,000 ✓) ≈ $12.32/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 14.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~48.6% of bid side (200,836 resting ≥ 5,000 ✓) ≈ $1.87/day (pool ÷ 13 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 93.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~46.5% of bid side (500,286 resting ≥ 2,000 ✓) ≈ $2.91/day (pool ÷ 2 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~42.1% of bid side (20,704 resting ≥ 2,000 ✓) ≈ $5.26/day |
| `usgubewc-usgub-id-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~37.9% of bid side (5,280 resting ≥ 2,000 ✓) ≈ $2.37/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~36.3% of ask side (205,575 resting ≥ 2,000 ✓) ≈ $2.27/day (pool ÷ 2 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 15.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~36.0% of ask side (10,308 resting ≥ 2,000 ✓) ≈ $4.50/day |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 5.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~34.2% of ask side (130,857 resting ≥ 2,000 ✓) ≈ $2.14/day (pool ÷ 2 markets) |
| `usgubewc-usgub-sd-2026-11-03-dem` | BUY | 1.0¢ | 1,660 | 1 | $25.00 | ✅ scoring — ~32.2% of bid side (2,640 resting ≥ 2,000 ✓) ≈ $2.01/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 16.0¢ | 40 | 1 | $100.00 | ✅ scoring — ~32.0% of bid side (400,658 resting ≥ 5,000 ✓) ≈ $1.33/day (pool ÷ 12 markets) |
| `pandc-anydis-2027-12-31` | BUY | 14.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~30.5% of bid side (10,401 resting ≥ 10,000 ✓) ≈ $3.82/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 21.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~29.4% of bid side (15,356 resting ≥ 5,000 ✓) ≈ $7.35/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~29.2% of bid side (6,845 resting ≥ 2,000 ✓) ≈ $1.83/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 9.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~28.4% of ask side (69,237 resting ≥ 5,000 ✓) ≈ $1.18/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 15.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~27.9% of bid side (300,599 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 20.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~27.8% of ask side (82,464 resting ≥ 5,000 ✓) ≈ $1.16/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~27.5% of ask side (77,866 resting ≥ 5,000 ✓) ≈ $1.06/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 37.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~27.4% of bid side (400,380 resting ≥ 5,000 ✓) ≈ $1.14/day (pool ÷ 12 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 1,290 | 0 | $25.00 | ✅ scoring — ~27.0% of bid side (4,785 resting ≥ 2,000 ✓) ≈ $1.68/day (pool ÷ 2 markets) |
| `pandc-anydis-2027-12-31` | SELL | 22.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~25.4% of ask side (10,366 resting ≥ 10,000 ✓) ≈ $3.17/day (pool ÷ 2 markets) |
| …and 328 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>usgubewc-usgub-me-2026-11-03-rep</code> SELL 40 @ 10¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
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
<details><summary><code>lawec-cryptoleg-2026-12-31</code> SELL 40 @ 37¢ → $9.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 50 (40 yours) | ×0.1^0 = 50.0 |
|  | 38¢ | 1 | ×0.1^1 = 0.1 |
|  | 46¢ | 2 | ×0.1^9 = 0.0 |
|  | 48¢ | 30 | ×0.1^11 = 0.0 |
|  | 99¢ | 47,952 | ×0.1^62 = 0.0 |
| | | **Σ** | **50.1** |

`yours 40.0 / Σ 50.1 = 79.8%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 79.8% = $9.98/day`  

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
<details><summary><code>lawec-cryptoleg-2026-12-31</code> BUY 30 @ 33¢ → $8.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 40 (30 yours) | ×0.1^0 = 40.0 |
|  | 32¢ | 30 | ×0.1^1 = 3.0 |
|  | 31¢ | 181 | ×0.1^2 = 1.8 |
|  | 26¢ | 250 | ×0.1^7 = 0.0 |
|  | 25¢ | 12 | ×0.1^8 = 0.0 |
|  | 23¢ | 40 | ×0.1^10 = 0.0 |
|  | 10¢ | 875 | ×0.1^23 = 0.0 |
|  | 9¢ | 5 | ×0.1^24 = 0.0 |
|  | 1¢ | 35,200 | ×0.1^32 = 0.0 |
| | | **Σ** | **44.8** |

`yours 30.0 / Σ 44.8 = 67.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 67.0% = $8.37/day`  

</details>
<details><summary><code>ussewc-usse-co-2026-11-03-dem</code> BUY 40 @ 94¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 2¢ | 500,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **65.0** |

`yours 40.0 / Σ 65.0 = 61.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.5% = $3.85/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem` ← this one
2. `ussewc-usse-co-2026-11-03-rep`

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
<details><summary><code>usgubewc-usgub-me-2026-11-03-dem</code> BUY 40 @ 94¢ → $3.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 94¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 93¢ | 324 | ×0.1^1 = 32.4 |
|  | 2¢ | 500,000 | ×0.1^92 = 0.0 |
| | | **Σ** | **72.4** |

`yours 40.0 / Σ 72.4 = 55.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 55.2% = $3.45/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-me-2026-11-03-dem` ← this one
2. `usgubewc-usgub-me-2026-11-03-rep`

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 23¢ → $12.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 23¢ | 20 (10 yours) | ×0.2^0 = 20.0 |
|  | 25¢ | 7 | ×0.2^2 = 0.3 |
|  | 28¢ | 1 | ×0.2^5 = 0.0 |
|  | 29¢ | 134 | ×0.2^6 = 0.0 |
|  | 32¢ | 23 | ×0.2^9 = 0.0 |
|  | 42¢ | 66 | ×0.2^19 = 0.0 |
|  | 99¢ | 19,060 | ×0.2^76 = 0.0 |
| | | **Σ** | **20.3** |

`yours 10.0 / Σ 20.3 = 49.3%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 49.3% = $12.32/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 40 @ 10¢ → $5.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 95 (40 yours) | ×0.1^0 = 95.0 |
|  | 6¢ | 11 | ×0.1^4 = 0.0 |
|  | 5¢ | 148 | ×0.1^5 = 0.0 |
|  | 2¢ | 10,250 | ×0.1^8 = 0.0 |
| | | **Σ** | **95.0** |

`yours 40.0 / Σ 95.0 = 42.1%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 42.1% = $5.26/day`  

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $2.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,280 (2,000 yours) | ×0.1^0 = 5,280.0 |
| | | **Σ** | **5,280.0** |

`yours 2,000.0 / Σ 5,280.0 = 37.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 37.9% = $2.37/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem` ← this one
2. `usgubewc-usgub-id-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 40 @ 10¢ → $2.27/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 90 (40 yours) | ×0.1^0 = 90.0 |
|  | 11¢ | 170 | ×0.1^1 = 17.0 |
|  | 12¢ | 333 | ×0.1^2 = 3.3 |
|  | 98¢ | 195,750 | ×0.1^88 = 0.0 |
| | | **Σ** | **110.3** |

`yours 40.0 / Σ 110.3 = 36.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 36.3% = $2.27/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 40 @ 15¢ → $4.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 97 (40 yours) | ×0.1^0 = 97.0 |
|  | 16¢ | 134 | ×0.1^1 = 13.4 |
|  | 17¢ | 30 | ×0.1^2 = 0.3 |
|  | 18¢ | 348 | ×0.1^3 = 0.3 |
|  | 33¢ | 300 | ×0.1^18 = 0.0 |
|  | 35¢ | 151 | ×0.1^20 = 0.0 |
|  | 99¢ | 9,248 | ×0.1^84 = 0.0 |
| | | **Σ** | **111.0** |

`yours 40.0 / Σ 111.0 = 36.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 36.0% = $4.50/day`  

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 40 @ 5¢ → $2.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 117 (40 yours) | ×0.1^0 = 117.0 |
|  | 11¢ | 40 | ×0.1^6 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^93 = 0.0 |
| | | **Σ** | **117.0** |

`yours 40.0 / Σ 117.0 = 34.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 34.2% = $2.14/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 10 @ 21¢ → $7.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 34 (10 yours) | ×0.2^0 = 34.0 |
|  | 16¢ | 1 | ×0.2^5 = 0.0 |
|  | 14¢ | 3 | ×0.2^7 = 0.0 |
|  | 13¢ | 3 | ×0.2^8 = 0.0 |
|  | 12¢ | 100 | ×0.2^9 = 0.0 |
|  | 2¢ | 16 | ×0.2^19 = 0.0 |
|  | 1¢ | 15,200 | ×0.2^20 = 0.0 |
| | | **Σ** | **34.0** |

`yours 10.0 / Σ 34.0 = 29.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 29.4% = $7.35/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $1.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 6,845 (2,000 yours) | ×0.1^0 = 6,845.0 |
| | | **Σ** | **6,845.0** |

`yours 2,000.0 / Σ 6,845.0 = 29.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 29.2% = $1.83/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 40 @ 20¢ → $1.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 144 (40 yours) | ×0.2^0 = 144.0 |
|  | 48¢ | 49 | ×0.2^28 = 0.0 |
|  | 81¢ | 0 | ×0.2^61 = 0.0 |
|  | 98¢ | 80,046 | ×0.2^78 = 0.0 |
| | | **Σ** | **144.0** |

`yours 40.0 / Σ 144.0 = 27.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 27.8% = $1.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $1.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 60 (20 yours) | ×0.2^0 = 60.0 |
|  | 6¢ | 295 | ×0.2^2 = 11.8 |
|  | 8¢ | 500 | ×0.2^4 = 0.8 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 65,710 | ×0.2^93 = 0.0 |
| | | **Σ** | **72.6** |

`yours 20.0 / Σ 72.6 = 27.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.5% = $1.06/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> BUY 40 @ 37¢ → $1.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 37¢ | 145 (40 yours) | ×0.2^0 = 145.0 |
|  | 36¢ | 5 | ×0.2^1 = 1.0 |
|  | 34¢ | 0 | ×0.2^3 = 0.0 |
|  | 21¢ | 30 | ×0.2^16 = 0.0 |
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
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 1,290 @ 1¢ → $1.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,785 (1,290 yours) | ×0.1^0 = 4,785.0 |
| | | **Σ** | **4,785.0** |

`yours 1,290.0 / Σ 4,785.0 = 27.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 27.0% = $1.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 20 @ 22¢ → $3.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 77 (20 yours) | ×0.25^0 = 77.0 |
|  | 23¢ | 7 | ×0.25^1 = 1.8 |
|  | 34¢ | 185 | ×0.25^12 = 0.0 |
|  | 50¢ | 25 | ×0.25^28 = 0.0 |
|  | 99¢ | 10,072 | ×0.25^77 = 0.0 |
| | | **Σ** | **78.8** |

`yours 20.0 / Σ 78.8 = 25.4%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 25.4% = $3.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (77,531 resting) | ~21.9% | ~$16.44 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,503 resting) | ~59.3% | ~$14.81 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (369,264 resting) | ~19.0% | ~$14.27 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (65,575 resting) | ~16.3% | ~$12.20 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,066,422 resting) | ~13.8% | ~$10.39 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (37,456 resting) | ~33.9% | ~$8.46 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (10,407 resting) | ~30.0% | ~$7.49 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (649,427 resting) | ~7.5% | ~$5.59 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (863,416 resting) | ~5.3% | ~$3.97 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (91,431 resting) | ~3.9% | ~$2.91 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (145,195 resting) | ~10.6% | ~$2.66 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (277,064 resting) | ~3.5% | ~$2.60 |

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
| 2026-08-12 6:57 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:45 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:34 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:32 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 6:29 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 4:42 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 2:46 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 1:09 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-12 12:17 AM ET | ✅ ok | 1952 | $2447.06 |
| 2026-08-11 11:31 PM ET | ✅ ok | 1952 | $2447.06 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
