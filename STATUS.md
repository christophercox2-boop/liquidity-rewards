# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-03 12:00 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$81.67/day estimated (ceiling, not promise — details below)

**Earned:** $1,515.42 lifetime ($1,373.47 paid). Last three recorded days — 2026-08-01: **$52.30** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-31: **$67.96** · 2026-07-30: **$20.48** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — SELL at the best price, ~$23.48/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$14.91/day), `ewc-usgub-oh-2026-11-03-dem` (~$14.24/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$81.67/day (~$3.40/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `apdc-jerpowgov-2026-12-31` | SELL | 13.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (6,481 resting ≥ 5,000 ✓) ≈ $24.99/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 21.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~99.6% of bid side (5,619 resting ≥ 5,000 ✓) ≈ $3.83/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~66.6% of bid side (5,458 resting ≥ 5,000 ✓) ≈ $2.77/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 84.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~64.0% of bid side (5,484 resting ≥ 5,000 ✓) ≈ $2.67/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~61.6% of ask side (12,147 resting ≥ 5,000 ✓) ≈ $2.57/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 9.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~59.9% of ask side (6,186 resting ≥ 5,000 ✓) ≈ $2.50/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 20.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~58.8% of bid side (5,522 resting ≥ 5,000 ✓) ≈ $2.26/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 12.0¢ | 33 | 0 | $100.00 | ✅ scoring — ~49.0% of ask side (12,201 resting ≥ 5,000 ✓) ≈ $1.88/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 12.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~44.6% of ask side (12,166 resting ≥ 5,000 ✓) ≈ $1.72/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~42.8% of ask side (12,125 resting ≥ 5,000 ✓) ≈ $1.65/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~40.0% of ask side (12,488 resting ≥ 5,000 ✓) ≈ $1.54/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~38.6% of ask side (12,112 resting ≥ 5,000 ✓) ≈ $1.49/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 84.0¢ | 79 | 0 | $100.00 | ✅ scoring — ~32.1% of ask side (13,225 resting ≥ 5,000 ✓) ≈ $1.34/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~31.7% of bid side (11,414 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 80.0¢ | 51 | 0 | $100.00 | ✅ scoring — ~31.3% of bid side (5,614 resting ≥ 5,000 ✓) ≈ $1.30/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~30.3% of ask side (12,069 resting ≥ 5,000 ✓) ≈ $1.16/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 16.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~30.0% of ask side (6,028 resting ≥ 5,000 ✓) ≈ $7.49/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~28.6% of bid side (5,556 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 45.0¢ | 13 | 0 | $100.00 | ✅ scoring — ~26.5% of ask side (6,884 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~26.1% of ask side (12,225 resting ≥ 5,000 ✓) ≈ $1.00/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 81.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~20.6% of bid side (5,842 resting ≥ 5,000 ✓) ≈ $0.86/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~19.6% of ask side (6,069 resting ≥ 5,000 ✓) ≈ $0.81/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~18.8% of ask side (12,163 resting ≥ 5,000 ✓) ≈ $0.72/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~17.8% of ask side (6,260 resting ≥ 5,000 ✓) ≈ $0.74/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-ind` | BUY | 11.0¢ | 10 | 0 | $500.00 | ✅ scoring — ~17.6% of bid side (1,151,210 resting ≥ 2,500 ✓) ≈ $0.60/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~17.2% of bid side (26,014 resting ≥ 5,000 ✓) ≈ $0.66/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~16.4% of bid side (4,927 resting ≥ 2,500 ✓) ≈ $0.56/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 15.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~14.9% of ask side (12,357 resting ≥ 5,000 ✓) ≈ $0.57/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-ind` | BUY | 10.0¢ | 22 | 1 | $500.00 | ✅ scoring — ~13.6% of bid side (1,151,210 resting ≥ 2,500 ✓) ≈ $0.46/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 60 | 2 | $100.00 | ✅ scoring — ~12.3% of bid side (5,323 resting ≥ 5,000 ✓) ≈ $0.47/day (pool ÷ 13 markets) |
| …and 74 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 13¢ → $24.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 15¢ | 0 | ×0.2^2 = 0.0 |
|  | 34¢ | 1,167 | ×0.2^21 = 0.0 |
|  | 35¢ | 1 | ×0.2^22 = 0.0 |
|  | 36¢ | 3 | ×0.2^23 = 0.0 |
|  | 57¢ | 100 | ×0.2^44 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^86 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 100.0% = $24.99/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 50 @ 21¢ → $3.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 19¢ | 5 | ×0.2^2 = 0.2 |
|  | 15¢ | 4 | ×0.2^6 = 0.0 |
|  | 9¢ | 4 | ×0.2^12 = 0.0 |
|  | 1¢ | 5,555 | ×0.2^20 = 0.0 |
| | | **Σ** | **50.2** |

`yours 50.0 / Σ 50.2 = 99.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.6% = $3.83/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 30 @ 85¢ → $2.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 45 (30 yours) | ×0.2^0 = 45.0 |
|  | 83¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,412 | ×0.2^84 = 0.0 |
| | | **Σ** | **45.0** |

`yours 30.0 / Σ 45.0 = 66.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.6% = $2.77/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180` ← this one
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
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 20 @ 84¢ → $2.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 31 (20 yours) | ×0.2^0 = 31.0 |
|  | 83¢ | 1 | ×0.2^1 = 0.2 |
|  | 82¢ | 1 | ×0.2^2 = 0.0 |
|  | 78¢ | 243 | ×0.2^6 = 0.0 |
|  | 1¢ | 5,208 | ×0.2^83 = 0.0 |
| | | **Σ** | **31.3** |

`yours 20.0 / Σ 31.3 = 64.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 64.0% = $2.67/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 50 @ 8¢ → $2.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 81 (50 yours) | ×0.2^0 = 81.0 |
|  | 10¢ | 5 | ×0.2^2 = 0.2 |
|  | 50¢ | 25 | ×0.2^42 = 0.0 |
|  | 99¢ | 12,036 | ×0.2^91 = 0.0 |
| | | **Σ** | **81.2** |

`yours 50.0 / Σ 81.2 = 61.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 61.6% = $2.57/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 9¢ → $2.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 83 (50 yours) | ×0.2^0 = 83.0 |
|  | 10¢ | 2 | ×0.2^1 = 0.4 |
|  | 11¢ | 2 | ×0.2^2 = 0.1 |
|  | 15¢ | 15 | ×0.2^6 = 0.0 |
|  | 50¢ | 25 | ×0.2^41 = 0.0 |
|  | 99¢ | 6,059 | ×0.2^90 = 0.0 |
| | | **Σ** | **83.5** |

`yours 50.0 / Σ 83.5 = 59.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 59.9% = $2.50/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 2 @ 20¢ → $2.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 3 (2 yours) | ×0.2^0 = 3.0 |
|  | 18¢ | 10 | ×0.2^2 = 0.4 |
|  | 10¢ | 100 | ×0.2^10 = 0.0 |
|  | 1¢ | 5,409 | ×0.2^19 = 0.0 |
| | | **Σ** | **3.4** |

`yours 2.0 / Σ 3.4 = 58.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 58.8% = $2.26/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 33 @ 12¢ → $1.88/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 67 (33 yours) | ×0.2^0 = 67.0 |
|  | 14¢ | 1 | ×0.2^2 = 0.0 |
|  | 15¢ | 46 | ×0.2^3 = 0.4 |
|  | 18¢ | 4 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 98¢ | 1,782 | ×0.2^86 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^87 = 0.0 |
| | | **Σ** | **67.4** |

`yours 33.0 / Σ 67.4 = 49.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 49.0% = $1.88/day`  

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
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 50 @ 12¢ → $1.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 112 (50 yours) | ×0.2^0 = 112.0 |
|  | 14¢ | 1 | ×0.2^2 = 0.0 |
|  | 29¢ | 2 | ×0.2^17 = 0.0 |
|  | 35¢ | 2 | ×0.2^23 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 98¢ | 1,748 | ×0.2^86 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^87 = 0.0 |
| | | **Σ** | **112.0** |

`yours 50.0 / Σ 112.0 = 44.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 44.6% = $1.72/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 21 @ 8¢ → $1.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 49 (21 yours) | ×0.2^0 = 49.0 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,773 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **49.1** |

`yours 21.0 / Σ 49.1 = 42.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 42.8% = $1.65/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $1.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 76 (40 yours) | ×0.2^0 = 76.0 |
|  | 11¢ | 120 | ×0.2^1 = 24.0 |
|  | 12¢ | 2 | ×0.2^2 = 0.1 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **100.1** |

`yours 40.0 / Σ 100.1 = 40.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.0% = $1.54/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 18 @ 15¢ → $1.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 47 (18 yours) | ×0.2^0 = 47.3 |
|  | 17¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **47.3** |

`yours 18.3 / Σ 47.3 = 38.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.6% = $1.49/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 79 @ 84¢ → $1.34/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 246 (79 yours) | ×0.2^0 = 246.0 |
|  | 86¢ | 7 | ×0.2^2 = 0.3 |
|  | 94¢ | 205 | ×0.2^10 = 0.0 |
|  | 99¢ | 12,767 | ×0.2^15 = 0.0 |
| | | **Σ** | **246.3** |

`yours 79.0 / Σ 246.3 = 32.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 32.1% = $1.34/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $1.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1,174 (500 yours) | ×0.2^0 = 1,174.0 |
|  | 2¢ | 10,040 | ×0.2^2 = 401.6 |
| | | **Σ** | **1,575.6** |

`yours 500.0 / Σ 1,575.6 = 31.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.7% = $1.22/day`  

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
11. `scc-senate-gop-2026-11-03-56` ← this one
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 51 @ 80¢ → $1.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 163 (51 yours) | ×0.2^0 = 163.0 |
|  | 78¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,450 | ×0.2^79 = 0.0 |
| | | **Σ** | **163.1** |

`yours 51.0 / Σ 163.1 = 31.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 31.3% = $1.30/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185` ← this one
3. `scc-hrep-rep-2026-11-03-gte190`
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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 10¢ → $1.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 33 (10 yours) | ×0.2^0 = 33.0 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 16¢ | 3 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **33.0** |

`yours 10.0 / Σ 33.0 = 30.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.3% = $1.16/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `scc-senate-gop-2026-11-03-46`
2. `scc-senate-gop-2026-11-03-47`
3. `scc-senate-gop-2026-11-03-48`
4. `scc-senate-gop-2026-11-03-49`
5. `scc-senate-gop-2026-11-03-50`
6. `scc-senate-gop-2026-11-03-51`
7. `scc-senate-gop-2026-11-03-52`
8. `scc-senate-gop-2026-11-03-53`
9. `scc-senate-gop-2026-11-03-54` ← this one
10. `scc-senate-gop-2026-11-03-55`
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 16¢ → $7.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 334 (100 yours) | ×0.2^0 = 333.7 |
|  | 18¢ | 2 | ×0.2^2 = 0.1 |
|  | 30¢ | 192 | ×0.2^14 = 0.0 |
|  | 41¢ | 200 | ×0.2^25 = 0.0 |
|  | 49¢ | 100 | ×0.2^33 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^83 = 0.0 |
| | | **Σ** | **333.8** |

`yours 100.0 / Σ 333.8 = 30.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 30.0% = $7.49/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 100 @ 20¢ → $1.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 350 (100 yours) | ×0.2^0 = 350.0 |
|  | 18¢ | 6 | ×0.2^2 = 0.2 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **350.2** |

`yours 100.0 / Σ 350.2 = 28.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.6% = $1.10/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 13 @ 45¢ → $1.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 49 (13 yours) | ×0.2^0 = 49.0 |
|  | 47¢ | 2 | ×0.2^2 = 0.1 |
|  | 69¢ | 107 | ×0.2^24 = 0.0 |
|  | 81¢ | 107 | ×0.2^36 = 0.0 |
|  | 94¢ | 69 | ×0.2^49 = 0.0 |
|  | 99¢ | 6,550 | ×0.2^54 = 0.0 |
| | | **Σ** | **49.1** |

`yours 13.0 / Σ 49.1 = 26.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 26.5% = $1.10/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 153 (40 yours) | ×0.2^0 = 153.0 |
|  | 8¢ | 2 | ×0.2^2 = 0.1 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **153.1** |

`yours 40.0 / Σ 153.1 = 26.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.1% = $1.00/day`  

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
10. `scc-senate-gop-2026-11-03-55` ← this one
11. `scc-senate-gop-2026-11-03-56`
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 10 @ 81¢ → $0.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 81¢ | 47 (10 yours) | ×0.2^0 = 47.0 |
|  | 79¢ | 1 | ×0.2^2 = 0.1 |
|  | 78¢ | 174 | ×0.2^3 = 1.4 |
|  | 77¢ | 83 | ×0.2^4 = 0.1 |
|  | 75¢ | 83 | ×0.2^6 = 0.0 |
|  | 74¢ | 4 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^80 = 0.0 |
| | | **Σ** | **48.6** |

`yours 10.0 / Σ 48.6 = 20.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 20.6% = $0.86/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 30 @ 47¢ → $0.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 153 (30 yours) | ×0.2^0 = 153.2 |
|  | 49¢ | 6 | ×0.2^2 = 0.2 |
|  | 52¢ | 1 | ×0.2^5 = 0.0 |
|  | 69¢ | 100 | ×0.2^22 = 0.0 |
|  | 99¢ | 5,809 | ×0.2^52 = 0.0 |
| | | **Σ** | **153.4** |

`yours 30.0 / Σ 153.4 = 19.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.6% = $0.81/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 16¢ → $0.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 106 (20 yours) | ×0.2^0 = 106.2 |
|  | 18¢ | 2 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^82 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^83 = 0.0 |
| | | **Σ** | **106.3** |

`yours 20.0 / Σ 106.3 = 18.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.8% = $0.72/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 20¢ → $0.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 56 (10 yours) | ×0.2^0 = 56.0 |
|  | 22¢ | 1 | ×0.2^2 = 0.1 |
|  | 94¢ | 28 | ×0.2^74 = 0.0 |
|  | 99¢ | 6,175 | ×0.2^79 = 0.0 |
| | | **Σ** | **56.0** |

`yours 10.0 / Σ 56.0 = 17.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 17.8% = $0.74/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-ind</code> BUY 10 @ 11¢ → $0.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 16 (10 yours) | ×0.35^0 = 16.0 |
|  | 10¢ | 22 | ×0.35^1 = 7.7 |
|  | 9¢ | 11 | ×0.35^2 = 1.4 |
|  | 1¢ | 1,151,161 | ×0.35^10 = 31.8 |
| | | **Σ** | **56.8** |

`yours 10.0 / Σ 56.8 = 17.6%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 17.6% = $0.60/day`  

<details><summary>÷ 73 markets in this race (40 known) — tap to list</summary>

1. `tec-cbb-champ-2027-04-05-w-ala`
2. `tec-cbb-champ-2027-04-05-w-ark`
3. `tec-cbb-champ-2027-04-05-w-arz`
4. `tec-cbb-champ-2027-04-05-w-aubrn`
5. `tec-cbb-champ-2027-04-05-w-bayl`
6. `tec-cbb-champ-2027-04-05-w-boise`
7. `tec-cbb-champ-2027-04-05-w-boscol`
8. `tec-cbb-champ-2027-04-05-w-butl`
9. `tec-cbb-champ-2027-04-05-w-byu`
10. `tec-cbb-champ-2027-04-05-w-cin`
11. `tec-cbb-champ-2027-04-05-w-clmsn`
12. `tec-cbb-champ-2027-04-05-w-colst`
13. `tec-cbb-champ-2027-04-05-w-creigh`
14. `tec-cbb-champ-2027-04-05-w-day`
15. `tec-cbb-champ-2027-04-05-w-duke`
16. `tec-cbb-champ-2027-04-05-w-fl`
17. `tec-cbb-champ-2027-04-05-w-flst`
18. `tec-cbb-champ-2027-04-05-w-george`
19. `tec-cbb-champ-2027-04-05-w-gnzg`
20. `tec-cbb-champ-2027-04-05-w-hou`
21. `tec-cbb-champ-2027-04-05-w-ill`
22. `tec-cbb-champ-2027-04-05-w-ind` ← this one
23. `tec-cbb-champ-2027-04-05-w-iowa`
24. `tec-cbb-champ-2027-04-05-w-iowast`
25. `tec-cbb-champ-2027-04-05-w-kan`
26. `tec-cbb-champ-2027-04-05-w-lou`
27. `tec-cbb-champ-2027-04-05-w-loych`
28. `tec-cbb-champ-2027-04-05-w-lsutig`
29. `tec-cbb-champ-2027-04-05-w-marq`
30. `tec-cbb-champ-2027-04-05-w-mia`
31. `tec-cbb-champ-2027-04-05-w-mich`
32. `tec-cbb-champ-2027-04-05-w-miss`
33. `tec-cbb-champ-2027-04-05-w-missr`
34. `tec-cbb-champ-2027-04-05-w-mphs`
35. `tec-cbb-champ-2027-04-05-w-mspst`
36. `tec-cbb-champ-2027-04-05-w-mst`
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 766 | ×0.2^0 = 766.0 |
| ▶ | 1¢ | 25,248 (5,000 yours) | ×0.2^1 = 5,049.6 |
| | | **Σ** | **5,815.6** |

`yours 1,000.0 / Σ 5,815.6 = 17.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.2% = $0.66/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 628 | ×0.35^0 = 628.0 |
| ▶ | 1¢ | 4,299 (1,000 yours) | ×0.35^1 = 1,504.6 |
| | | **Σ** | **2,132.6** |

`yours 350.0 / Σ 2,132.6 = 16.4%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 16.4% = $0.56/day`  

<details><summary>÷ 73 markets in this race (40 known) — tap to list</summary>

1. `tec-cbb-champ-2027-04-05-w-ala`
2. `tec-cbb-champ-2027-04-05-w-ark`
3. `tec-cbb-champ-2027-04-05-w-arz`
4. `tec-cbb-champ-2027-04-05-w-aubrn`
5. `tec-cbb-champ-2027-04-05-w-bayl`
6. `tec-cbb-champ-2027-04-05-w-boise`
7. `tec-cbb-champ-2027-04-05-w-boscol`
8. `tec-cbb-champ-2027-04-05-w-butl`
9. `tec-cbb-champ-2027-04-05-w-byu`
10. `tec-cbb-champ-2027-04-05-w-cin`
11. `tec-cbb-champ-2027-04-05-w-clmsn`
12. `tec-cbb-champ-2027-04-05-w-colst`
13. `tec-cbb-champ-2027-04-05-w-creigh`
14. `tec-cbb-champ-2027-04-05-w-day`
15. `tec-cbb-champ-2027-04-05-w-duke`
16. `tec-cbb-champ-2027-04-05-w-fl`
17. `tec-cbb-champ-2027-04-05-w-flst`
18. `tec-cbb-champ-2027-04-05-w-george`
19. `tec-cbb-champ-2027-04-05-w-gnzg`
20. `tec-cbb-champ-2027-04-05-w-hou`
21. `tec-cbb-champ-2027-04-05-w-ill`
22. `tec-cbb-champ-2027-04-05-w-ind`
23. `tec-cbb-champ-2027-04-05-w-iowa`
24. `tec-cbb-champ-2027-04-05-w-iowast`
25. `tec-cbb-champ-2027-04-05-w-kan`
26. `tec-cbb-champ-2027-04-05-w-lou`
27. `tec-cbb-champ-2027-04-05-w-loych`
28. `tec-cbb-champ-2027-04-05-w-lsutig`
29. `tec-cbb-champ-2027-04-05-w-marq`
30. `tec-cbb-champ-2027-04-05-w-mia`
31. `tec-cbb-champ-2027-04-05-w-mich`
32. `tec-cbb-champ-2027-04-05-w-miss`
33. `tec-cbb-champ-2027-04-05-w-missr`
34. `tec-cbb-champ-2027-04-05-w-mphs`
35. `tec-cbb-champ-2027-04-05-w-mspst`
36. `tec-cbb-champ-2027-04-05-w-mst`
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 25 @ 15¢ → $0.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 148 (25 yours) | ×0.2^0 = 148.0 |
|  | 16¢ | 96 | ×0.2^1 = 19.2 |
|  | 17¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,811 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **167.2** |

`yours 25.0 / Σ 167.2 = 14.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 14.9% = $0.57/day`  

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
11. `scc-senate-gop-2026-11-03-56` ← this one
12. `scc-senate-gop-2026-11-03-gte57`
13. `scc-senate-gop-2026-11-03-lte45`

</details>

</details>
<details><summary><code>tec-cbb-champ-2027-04-05-w-ind</code> BUY 22 @ 10¢ → $0.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 16 | ×0.35^0 = 16.0 |
| ▶ | 10¢ | 22 (22 yours) | ×0.35^1 = 7.7 |
|  | 9¢ | 11 | ×0.35^2 = 1.4 |
|  | 1¢ | 1,151,161 | ×0.35^10 = 31.8 |
| | | **Σ** | **56.8** |

`yours 7.7 / Σ 56.8 = 13.6%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 13.6% = $0.46/day`  

<details><summary>÷ 73 markets in this race (40 known) — tap to list</summary>

1. `tec-cbb-champ-2027-04-05-w-ala`
2. `tec-cbb-champ-2027-04-05-w-ark`
3. `tec-cbb-champ-2027-04-05-w-arz`
4. `tec-cbb-champ-2027-04-05-w-aubrn`
5. `tec-cbb-champ-2027-04-05-w-bayl`
6. `tec-cbb-champ-2027-04-05-w-boise`
7. `tec-cbb-champ-2027-04-05-w-boscol`
8. `tec-cbb-champ-2027-04-05-w-butl`
9. `tec-cbb-champ-2027-04-05-w-byu`
10. `tec-cbb-champ-2027-04-05-w-cin`
11. `tec-cbb-champ-2027-04-05-w-clmsn`
12. `tec-cbb-champ-2027-04-05-w-colst`
13. `tec-cbb-champ-2027-04-05-w-creigh`
14. `tec-cbb-champ-2027-04-05-w-day`
15. `tec-cbb-champ-2027-04-05-w-duke`
16. `tec-cbb-champ-2027-04-05-w-fl`
17. `tec-cbb-champ-2027-04-05-w-flst`
18. `tec-cbb-champ-2027-04-05-w-george`
19. `tec-cbb-champ-2027-04-05-w-gnzg`
20. `tec-cbb-champ-2027-04-05-w-hou`
21. `tec-cbb-champ-2027-04-05-w-ill`
22. `tec-cbb-champ-2027-04-05-w-ind` ← this one
23. `tec-cbb-champ-2027-04-05-w-iowa`
24. `tec-cbb-champ-2027-04-05-w-iowast`
25. `tec-cbb-champ-2027-04-05-w-kan`
26. `tec-cbb-champ-2027-04-05-w-lou`
27. `tec-cbb-champ-2027-04-05-w-loych`
28. `tec-cbb-champ-2027-04-05-w-lsutig`
29. `tec-cbb-champ-2027-04-05-w-marq`
30. `tec-cbb-champ-2027-04-05-w-mia`
31. `tec-cbb-champ-2027-04-05-w-mich`
32. `tec-cbb-champ-2027-04-05-w-miss`
33. `tec-cbb-champ-2027-04-05-w-missr`
34. `tec-cbb-champ-2027-04-05-w-mphs`
35. `tec-cbb-champ-2027-04-05-w-mspst`
36. `tec-cbb-champ-2027-04-05-w-mst`
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 60 @ 15¢ → $0.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 14 | ×0.2^0 = 14.0 |
|  | 16¢ | 6 | ×0.2^1 = 1.2 |
| ▶ | 15¢ | 107 (60 yours) | ×0.2^2 = 4.3 |
|  | 1¢ | 5,196 | ×0.2^16 = 0.0 |
| | | **Σ** | **19.5** |

`yours 2.4 / Σ 19.5 = 12.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 12.3% = $0.47/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |
| 2026-07-29 | ~$65.42 | $53.59 | 82% |

Biggest gaps on 2026-07-31: `scc-senate-gop-2026-11-03-48` (est ~$3.79 → got $2.51), `scc-senate-gop-2026-11-03-50` (est ~$3.29 → got $2.17), `apdc-alito-2026-12-31` (est ~$1.38 → got $0.45)

_2026-08-01 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,769 resting) | ~31.3% | ~$23.48 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,837 resting) | ~59.7% | ~$14.91 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (74,165 resting) | ~19.0% | ~$14.24 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (26,797 resting) | ~56.3% | ~$14.07 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (86,325 resting) | ~42.3% | ~$10.58 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (198,693 resting) | ~9.1% | ~$6.84 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (84,204 resting) | ~7.5% | ~$5.64 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (181,449 resting) | ~7.2% | ~$5.42 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (97,153 resting) | ~5.4% | ~$4.05 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (37,442 resting) | ~12.0% | ~$3.00 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $300.00 ÷ 3 | 0.20 | 10,000 | SELL side (18,772 resting) | ~5.0% | ~$2.51 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (112,808 resting) | ~3.3% | ~$2.48 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,373.47 |
| Pending | $140.74 |
| Skipped | $1.21 |
| **Total earned** | **$1,515.42** |

1532 reward rows · 30 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-01 ⚠️ multi-day pending bucket | $52.30 | `█████` |
| 2026-07-31 | $67.96 | `██████` |
| 2026-07-30 | $20.48 | `██` |
| 2026-07-29 | $53.59 | `█████` |
| 2026-07-28 | $79.65 | `███████` |
| 2026-07-27 | $125.34 | `███████████` |
| 2026-07-26 | $153.80 | `██████████████` |
| 2026-07-25 | $125.69 | `███████████` |
| 2026-07-24 | $135.19 | `████████████` |
| 2026-07-23 | $227.63 | `████████████████████` |
| 2026-07-22 | $82.95 | `███████` |
| 2026-07-21 | $91.44 | `████████` |
| 2026-07-20 | $106.54 | `█████████` |
| 2026-07-19 | $35.81 | `███` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $52.30 | `█` |
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.60 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.96 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-03 12:00 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-02 9:06 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-02 8:15 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:59 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:15 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 6:13 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 5:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 3:38 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 1:26 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 12:12 PM ET | ✅ ok | 1490 | $1463.12 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
