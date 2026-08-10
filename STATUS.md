# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-10 6:38 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$318.25/day estimated (ceiling, not promise — details below)

**Earned:** $1,827.20 lifetime ($1,771.01 paid). Last three recorded days — 2026-08-08: **$54.78** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-07: **$60.33** · 2026-08-06: **$52.21** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — SELL at the best price, ~$24.58/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$17.00/day), `apdc-jerpowgov-2026-08-31` (~$15.67/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$318.25/day (~$13.26/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (62,850 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `pandc-anydis-2027-12-31` | SELL | 25.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~100.0% of ask side (10,829 resting ≥ 10,000 ✓) ≈ $12.50/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 42.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (62,827 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `pandc-anydis-2027-12-31` | BUY | 21.0¢ | 11 | 0 | $50.00 | ✅ scoring — ~99.9% of bid side (11,112 resting ≥ 10,000 ✓) ≈ $12.49/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 55.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (80,515 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 19.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.0% of bid side (85,729 resting ≥ 5,000 ✓) ≈ $4.13/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 67.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~96.1% of ask side (62,970 resting ≥ 5,000 ✓) ≈ $4.00/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 20.0¢ | 16 | 0 | $25.00 | ✅ scoring — ~94.7% of ask side (2,623 resting ≥ 2,000 ✓) ≈ $11.84/day |
| `scc-senate-gop-2026-11-03-53` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~88.2% of bid side (10,712 resting ≥ 5,000 ✓) ≈ $3.39/day (pool ÷ 13 markets) |
| `ussewc-usse-ri-2026-11-03-rep` | SELL | 11.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (2,375 resting ≥ 2,000 ✓) ≈ $5.21/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 20.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~83.3% of ask side (2,375 resting ≥ 2,000 ✓) ≈ $5.21/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 6.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~81.0% of bid side (5,657 resting ≥ 5,000 ✓) ≈ $3.12/day (pool ÷ 13 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | BUY | 92.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,340 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | BUY | 73.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,340 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-ri-2026-11-03-dem` | BUY | 71.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,390 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 72.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~79.4% of bid side (2,380 resting ≥ 2,000 ✓) ≈ $4.96/day (pool ÷ 2 markets) |
| `ussewc-usse-mt-2026-11-03-setbod` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $2.98/day (pool ÷ 3 markets) |
| `ussewc-usse-ri-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-ky-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-nj-2026-11-03-rep` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-sd-2026-11-03-briben` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-fl-2026-11-03-dem` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~71.4% of bid side (2,800 resting ≥ 2,000 ✓) ≈ $4.46/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `ussewc-usse-wv-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `ussewc-usse-tn-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `ussewc-usse-nm-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `usgubewc-usgub-al-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `ussewc-usse-co-2026-11-03-dem` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| …and 194 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 20 @ 48¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 60¢ | 5 | ×0.2^12 = 0.0 |
|  | 61¢ | 100 | ×0.2^13 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 10 @ 25¢ → $12.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 10 (10 yours) | ×0.25^0 = 10.0 |
|  | 34¢ | 99 | ×0.25^9 = 0.0 |
|  | 50¢ | 19 | ×0.25^25 = 0.0 |
|  | 99¢ | 10,701 | ×0.25^74 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 100.0% = $12.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 1 @ 42¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 50¢ | 100 | ×0.2^8 = 0.0 |
|  | 52¢ | 1 | ×0.2^10 = 0.0 |
|  | 64¢ | 0 | ×0.2^22 = 0.0 |
|  | 72¢ | 0 | ×0.2^30 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^56 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
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
<details><summary><code>pandc-anydis-2027-12-31</code> BUY 11 @ 21¢ → $12.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 11 (11 yours) | ×0.25^0 = 11.0 |
|  | 16¢ | 10 | ×0.25^5 = 0.0 |
|  | 8¢ | 101 | ×0.25^13 = 0.0 |
|  | 2¢ | 4 | ×0.25^19 = 0.0 |
|  | 1¢ | 10,986 | ×0.25^20 = 0.0 |
| | | **Σ** | **11.0** |

`yours 11.0 / Σ 11.0 = 99.9%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 99.9% = $12.49/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 10 @ 55¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 55¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 50¢ | 30 | ×0.2^5 = 0.0 |
|  | 49¢ | 165 | ×0.2^6 = 0.0 |
|  | 24¢ | 170 | ×0.2^31 = 0.0 |
|  | 2¢ | 79,940 | ×0.2^53 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.8% = $4.16/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 1 @ 19¢ → $4.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 100 | ×0.2^11 = 0.0 |
|  | 7¢ | 81 | ×0.2^12 = 0.0 |
|  | 3¢ | 5,247 | ×0.2^16 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.0% = $4.13/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 40 @ 67¢ → $4.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 70¢ | 205 | ×0.2^3 = 1.6 |
|  | 90¢ | 1 | ×0.2^23 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^31 = 0.0 |
| | | **Σ** | **41.6** |

`yours 40.0 / Σ 41.6 = 96.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 96.1% = $4.00/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 16 @ 20¢ → $11.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 16 (16 yours) | ×0.1^0 = 16.4 |
|  | 21¢ | 6 | ×0.1^1 = 0.6 |
|  | 22¢ | 18 | ×0.1^2 = 0.2 |
|  | 23¢ | 123 | ×0.1^3 = 0.1 |
|  | 24¢ | 159 | ×0.1^4 = 0.0 |
|  | 35¢ | 101 | ×0.1^15 = 0.0 |
|  | 99¢ | 2,200 | ×0.1^79 = 0.0 |
| | | **Σ** | **17.3** |

`yours 16.4 / Σ 17.3 = 94.7%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 94.7% = $11.84/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 1 @ 13¢ → $3.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 3 | ×0.2^6 = 0.0 |
|  | 6¢ | 10,457 | ×0.2^7 = 0.1 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.2% = $3.39/day`  

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
<details><summary><code>ussewc-usse-ri-2026-11-03-rep</code> SELL 50 @ 11¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 12¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^88 = 0.0 |
| | | **Σ** | **60.0** |

`yours 50.0 / Σ 60.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ri-2026-11-03-dem`
2. `ussewc-usse-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 50 @ 20¢ → $5.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 21¢ | 100 | ×0.1^1 = 10.0 |
|  | 99¢ | 2,225 | ×0.1^79 = 0.0 |
| | | **Σ** | **60.0** |

`yours 50.0 / Σ 60.0 = 83.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 83.3% = $5.21/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 10 @ 6¢ → $3.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 2¢ | 422 | ×0.2^4 = 0.7 |
|  | 1¢ | 5,225 | ×0.2^5 = 1.7 |
| | | **Σ** | **12.3** |

`yours 10.0 / Σ 12.3 = 81.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 81.0% = $3.12/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
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
12. `scc-senate-gop-2026-11-03-gte57` ← this one
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> BUY 40 @ 92¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 92¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 91¢ | 100 | ×0.1^1 = 10.0 |
|  | 1¢ | 2,200 | ×0.1^91 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> BUY 40 @ 73¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 73¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 72¢ | 100 | ×0.1^1 = 10.0 |
|  | 1¢ | 2,200 | ×0.1^72 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ri-2026-11-03-dem</code> BUY 40 @ 71¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 71¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 70¢ | 100 | ×0.1^1 = 10.0 |
|  | 50¢ | 50 | ×0.1^21 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^70 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ri-2026-11-03-dem` ← this one
2. `ussewc-usse-ri-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 40 @ 72¢ → $4.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 72¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 71¢ | 100 | ×0.1^1 = 10.0 |
|  | 70¢ | 40 | ×0.1^2 = 0.4 |
|  | 1¢ | 2,200 | ×0.1^71 = 0.0 |
| | | **Σ** | **50.4** |

`yours 40.0 / Σ 50.4 = 79.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 79.4% = $4.96/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-mt-2026-11-03-setbod</code> BUY 2,000 @ 1¢ → $2.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 71.4% = $2.98/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `ussewc-usse-mt-2026-11-03-dem`
2. `ussewc-usse-mt-2026-11-03-rep`
3. `ussewc-usse-mt-2026-11-03-setbod` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ri-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ri-2026-11-03-dem`
2. `ussewc-usse-ri-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ky-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ky-2026-11-03-dem` ← this one
2. `ussewc-usse-ky-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-nj-2026-11-03-rep</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nj-2026-11-03-dem`
2. `ussewc-usse-nj-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-sd-2026-11-03-briben</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sd-2026-11-03-briben` ← this one
2. `ussewc-usse-sd-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-fl-2026-11-03-dem</code> BUY 2,000 @ 1¢ → $4.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,800 (2,000 yours) | ×0.1^0 = 2,800.0 |
| | | **Σ** | **2,800.0** |

`yours 2,000.0 / Σ 2,800.0 = 71.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 71.4% = $4.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem` ← this one
2. `ussewc-usse-fl-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem`
2. `ussewc-usse-ms-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wv-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wv-2026-11-03-dem`
2. `ussewc-usse-wv-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem` ← this one
2. `ussewc-usse-nm-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-al-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-al-2026-11-03-dem`
2. `usgubewc-usgub-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem` ← this one
2. `ussewc-usse-va-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-co-2026-11-03-dem</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-co-2026-11-03-dem` ← this one
2. `ussewc-usse-co-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-07 | ~$116.96 | $60.33 | 52% |
| 2026-08-06 | ~$60.78 | $52.21 | 86% |
| 2026-08-05 | ~$33.74 | $31.46 | 93% |

Biggest gaps on 2026-08-07: `opdc-mcconnell-resign-2026-11-02` (est ~$17.07 → got $5.10), `scc-hrep-rep-2026-11-03-gte205` (est ~$4.14 → got $0.00), `scc-hrep-rep-2026-11-03-gte195` (est ~$5.07 → got $0.94)

_2026-08-08 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (249,198 resting) | ~32.8% | ~$24.58 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,410 resting) | ~68.0% | ~$17.00 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,687 resting) | ~62.7% | ~$15.67 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (65,146 resting) | ~20.3% | ~$15.22 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,580 resting) | ~59.6% | ~$14.91 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (60,074 resting) | ~11.5% | ~$8.64 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (42,580 resting) | ~29.0% | ~$7.24 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (87,151 resting) | ~12.0% | ~$3.01 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (46,804 resting) | ~10.5% | ~$2.64 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (67,320 resting) | ~40.3% | ~$2.52 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (191,245 resting) | ~3.0% | ~$2.22 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (88,974 resting) | ~2.8% | ~$2.08 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,771.01 |
| Pending | $54.78 |
| Skipped | $1.41 |
| **Total earned** | **$1,827.20** |

1783 reward rows · 37 days with rewards · 377 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-08 ⚠️ multi-day pending bucket | $54.78 | `███████` |
| 2026-08-07 | $60.33 | `████████` |
| 2026-08-06 | $52.21 | `███████` |
| 2026-08-05 | $31.46 | `████` |
| 2026-08-04 | $53.94 | `███████` |
| 2026-08-03 | $44.81 | `██████` |
| 2026-08-02 | $14.05 | `██` |
| 2026-08-01 | $52.30 | `███████` |
| 2026-07-31 | $67.96 | `█████████` |
| 2026-07-30 | $20.67 | `███` |
| 2026-07-29 | $53.60 | `███████` |
| 2026-07-28 | $79.65 | `██████████` |
| 2026-07-27 | $125.34 | `████████████████` |
| 2026-07-26 | $153.80 | `████████████████████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $363.88 | `█████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $86.00 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `opdc-mcconnell-resign-2026-11-02` | $56.71 |
| `apdc-jerpowgov-2026-12-31` | $56.12 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.92 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `scc-hrep-rep-2026-11-03-gte200` | $32.74 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-10 6:38 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 4:53 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 2:44 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:58 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:28 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:24 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:19 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:17 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:07 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:04 AM ET | ✅ ok | 1783 | $1827.20 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
