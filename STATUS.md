# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-02 7:59 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$20.27/day estimated (ceiling, not promise — details below)

**Earned:** $1,463.12 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-31: **$67.96** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-30: **$20.48** · 2026-07-29: **$53.59** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$24.51/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-rep` (~$22.00/day), `ewc-usgub-oh-2026-11-03-dem` (~$13.81/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$20.27/day (~$0.84/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-52` | BUY | 21.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~76.7% of bid side (5,384 resting ≥ 5,000 ✓) ≈ $2.95/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~40.3% of ask side (12,110 resting ≥ 5,000 ✓) ≈ $1.55/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 38.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~36.4% of bid side (5,614 resting ≥ 5,000 ✓) ≈ $1.52/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 25.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~35.5% of ask side (12,165 resting ≥ 5,000 ✓) ≈ $1.37/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 30.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~33.6% of ask side (12,469 resting ≥ 5,000 ✓) ≈ $1.29/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~30.3% of ask side (12,424 resting ≥ 5,000 ✓) ≈ $1.17/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~28.6% of bid side (5,556 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~28.1% of ask side (12,127 resting ≥ 5,000 ✓) ≈ $1.08/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~26.1% of ask side (12,225 resting ≥ 5,000 ✓) ≈ $1.00/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~21.7% of ask side (11,463 resting ≥ 5,000 ✓) ≈ $0.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~21.3% of bid side (12,189 resting ≥ 5,000 ✓) ≈ $0.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~20.8% of ask side (12,084 resting ≥ 5,000 ✓) ≈ $0.80/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 1 | $100.00 | ✅ scoring — ~17.2% of bid side (26,013 resting ≥ 5,000 ✓) ≈ $0.66/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 3.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~11.5% of bid side (8,879 resting ≥ 5,000 ✓) ≈ $0.44/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~8.4% of bid side (12,165 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 15.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~7.7% of ask side (12,204 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~7.0% of bid side (71,718 resting ≥ 5,000 ✓) ≈ $0.27/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 5.0¢ | 590 | 0 | $100.00 | ✅ scoring — ~6.4% of bid side (9,395 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~5.9% of bid side (8,604 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 22.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~4.7% of ask side (8,710 resting ≥ 5,000 ✓) ≈ $0.19/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 6.0¢ | 32 | 1 | $100.00 | ✅ scoring — ~4.2% of bid side (5,733 resting ≥ 5,000 ✓) ≈ $0.16/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~3.5% of ask side (6,434 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 30.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~3.4% of ask side (12,319 resting ≥ 5,000 ✓) ≈ $0.13/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 11 | 1 | $100.00 | ✅ scoring — ~1.9% of bid side (5,862 resting ≥ 5,000 ✓) ≈ $0.08/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~1.7% of bid side (5,862 resting ≥ 5,000 ✓) ≈ $0.07/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 2.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~1.7% of bid side (29,875 resting ≥ 5,000 ✓) ≈ $0.07/day (pool ÷ 12 markets) |
| `ewc-usse-tx-2026-11-03-dem` | BUY | 47.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~1.7% of bid side (382,680 resting ≥ 10,000 ✓) ≈ $1.26/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 20.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~1.5% of ask side (5,568 resting ≥ 5,000 ✓) ≈ $0.06/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~1.2% of ask side (12,162 resting ≥ 5,000 ✓) ≈ $0.04/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 18.0¢ | 30 | 3 | $100.00 | ✅ scoring — ~0.8% of ask side (12,125 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 13 markets) |
| …and 28 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 50 @ 21¢ → $2.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 65 (50 yours) | ×0.2^0 = 65.0 |
|  | 19¢ | 5 | ×0.2^2 = 0.2 |
|  | 11¢ | 4 | ×0.2^10 = 0.0 |
|  | 9¢ | 4 | ×0.2^12 = 0.0 |
|  | 1¢ | 5,305 | ×0.2^20 = 0.0 |
| | | **Σ** | **65.2** |

`yours 50.0 / Σ 65.2 = 76.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 76.7% = $2.95/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 18 @ 15¢ → $1.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 45 (18 yours) | ×0.2^0 = 45.3 |
|  | 17¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **45.3** |

`yours 18.3 / Σ 45.3 = 40.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.3% = $1.55/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 100 @ 38¢ → $1.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 39¢ | 35 | ×0.2^0 = 35.0 |
| ▶ | 38¢ | 100 (100 yours) | ×0.2^1 = 20.0 |
|  | 1¢ | 5,479 | ×0.2^38 = 0.0 |
| | | **Σ** | **55.0** |

`yours 20.0 / Σ 55.0 = 36.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 36.4% = $1.52/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 50 @ 25¢ → $1.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 24¢ | 15 | ×0.2^0 = 15.1 |
| ▶ | 25¢ | 65 (50 yours) | ×0.2^1 = 13.0 |
|  | 26¢ | 1 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^26 = 0.0 |
|  | 98¢ | 1,782 | ×0.2^74 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^75 = 0.0 |
| | | **Σ** | **28.2** |

`yours 10.0 / Σ 28.2 = 35.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 35.5% = $1.37/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 30¢ → $1.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 128 (43 yours) | ×0.2^0 = 128.0 |
|  | 32¢ | 3 | ×0.2^2 = 0.1 |
|  | 38¢ | 128 | ×0.2^8 = 0.0 |
|  | 43¢ | 37 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^20 = 0.0 |
|  | 98¢ | 1,871 | ×0.2^68 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^69 = 0.0 |
| | | **Σ** | **128.1** |

`yours 43.0 / Σ 128.1 = 33.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.6% = $1.29/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $1.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 132 (40 yours) | ×0.2^0 = 131.7 |
|  | 12¢ | 2 | ×0.2^2 = 0.1 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **131.8** |

`yours 40.0 / Σ 131.8 = 30.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.3% = $1.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 16¢ → $1.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 71 (20 yours) | ×0.2^0 = 71.0 |
|  | 18¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^82 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^83 = 0.0 |
| | | **Σ** | **71.0** |

`yours 20.0 / Σ 71.0 = 28.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.1% = $1.08/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 10 @ 24¢ → $0.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 40 (10 yours) | ×0.2^0 = 40.0 |
|  | 25¢ | 26 | ×0.2^1 = 5.2 |
|  | 26¢ | 1 | ×0.2^2 = 0.1 |
|  | 27¢ | 94 | ×0.2^3 = 0.8 |
|  | 50¢ | 100 | ×0.2^26 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^74 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^75 = 0.0 |
| | | **Σ** | **46.0** |

`yours 10.0 / Σ 46.0 = 21.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 21.7% = $0.84/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $0.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1,949 (500 yours) | ×0.2^0 = 1,949.0 |
|  | 2¢ | 10,040 | ×0.2^2 = 401.6 |
| | | **Σ** | **2,350.6** |

`yours 500.0 / Σ 2,350.6 = 21.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 21.3% = $0.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 10¢ → $0.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 48 (10 yours) | ×0.2^0 = 48.0 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 16¢ | 3 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **48.0** |

`yours 10.0 / Σ 48.0 = 20.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.8% = $0.80/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.66/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 766 | ×0.2^0 = 766.0 |
| ▶ | 1¢ | 25,247 (5,000 yours) | ×0.2^1 = 5,049.4 |
| | | **Σ** | **5,815.4** |

`yours 1,000.0 / Σ 5,815.4 = 17.2%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1,000 @ 3¢ → $0.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,679 (1,000 yours) | ×0.2^0 = 8,679.0 |
| | | **Σ** | **8,679.0** |

`yours 1,000.0 / Σ 8,679.0 = 11.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.5% = $0.44/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 11,862 (1,000 yours) | ×0.2^0 = 11,862.0 |
| | | **Σ** | **11,862.0** |

`yours 1,000.0 / Σ 11,862.0 = 8.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.4% = $0.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 10 @ 15¢ → $0.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 130 (10 yours) | ×0.2^0 = 130.0 |
|  | 17¢ | 1 | ×0.2^2 = 0.0 |
|  | 29¢ | 2 | ×0.2^14 = 0.0 |
|  | 35¢ | 2 | ×0.2^20 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,768 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **130.0** |

`yours 10.0 / Σ 130.0 = 7.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.7% = $0.30/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5,000 @ 1¢ → $0.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 71,718 (5,000 yours) | ×0.2^0 = 71,717.9 |
| | | **Σ** | **71,717.9** |

`yours 5,000.0 / Σ 71,717.9 = 7.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.0% = $0.27/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 590 @ 5¢ → $0.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 9,195 (590 yours) | ×0.2^0 = 9,195.0 |
| | | **Σ** | **9,195.0** |

`yours 590.0 / Σ 9,195.0 = 6.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.4% = $0.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,404 (500 yours) | ×0.2^0 = 8,404.0 |
| | | **Σ** | **8,404.0** |

`yours 500.0 / Σ 8,404.0 = 5.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.9% = $0.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 22¢ → $0.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 41 | ×0.2^0 = 41.0 |
| ▶ | 22¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 94¢ | 33 | ×0.2^73 = 0.0 |
|  | 99¢ | 8,626 | ×0.2^78 = 0.0 |
| | | **Σ** | **43.0** |

`yours 2.0 / Σ 43.0 = 4.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.7% = $0.19/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 32 @ 6¢ → $0.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 144 | ×0.2^0 = 144.0 |
| ▶ | 6¢ | 32 (32 yours) | ×0.2^1 = 6.3 |
|  | 5¢ | 22 | ×0.2^2 = 0.9 |
|  | 1¢ | 5,535 | ×0.2^6 = 0.4 |
| | | **Σ** | **151.6** |

`yours 6.3 / Σ 151.6 = 4.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 4.2% = $0.16/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 50 @ 10¢ → $0.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 1,436 (50 yours) | ×0.2^0 = 1,435.7 |
|  | 50¢ | 25 | ×0.2^40 = 0.0 |
|  | 99¢ | 4,973 | ×0.2^89 = 0.0 |
| | | **Σ** | **1,435.7** |

`yours 50.0 / Σ 1,435.7 = 3.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.5% = $0.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 30¢ → $0.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 28¢ | 1 | ×0.2^0 = 0.9 |
|  | 29¢ | 50 | ×0.2^1 = 10.0 |
| ▶ | 30¢ | 24 (10 yours) | ×0.2^2 = 1.0 |
|  | 35¢ | 5 | ×0.2^7 = 0.0 |
|  | 40¢ | 105 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 98¢ | 1,833 | ×0.2^70 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^71 = 0.0 |
| | | **Σ** | **11.9** |

`yours 0.4 / Σ 11.9 = 3.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.4% = $0.13/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 11 @ 75¢ → $0.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 76¢ | 113 | ×0.2^0 = 113.0 |
| ▶ | 75¢ | 21 (11 yours) | ×0.2^1 = 4.2 |
|  | 49¢ | 120 | ×0.2^27 = 0.0 |
|  | 1¢ | 5,608 | ×0.2^75 = 0.0 |
| | | **Σ** | **117.2** |

`yours 2.2 / Σ 117.2 = 1.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.9% = $0.08/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 75¢ → $0.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 76¢ | 113 | ×0.2^0 = 113.0 |
| ▶ | 75¢ | 21 (10 yours) | ×0.2^1 = 4.2 |
|  | 49¢ | 120 | ×0.2^27 = 0.0 |
|  | 1¢ | 5,608 | ×0.2^75 = 0.0 |
| | | **Σ** | **117.2** |

`yours 2.0 / Σ 117.2 = 1.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.7% = $0.07/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> BUY 500 @ 2¢ → $0.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 29,675 (500 yours) | ×0.2^0 = 29,675.0 |
| | | **Σ** | **29,675.0** |

`yours 500.0 / Σ 29,675.0 = 1.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.7% = $0.07/day`  

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
<details><summary><code>ewc-usse-tx-2026-11-03-dem</code> BUY 50 @ 47¢ → $1.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 758 (50 yours) | ×0.2^0 = 758.0 |
|  | 46¢ | 11,069 | ×0.2^1 = 2,213.8 |
| | | **Σ** | **2,971.8** |

`yours 50.0 / Σ 2,971.8 = 1.7%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 1.7% = $1.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-tx-2026-11-03-dem` ← this one
2. `ewc-usse-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 50 @ 20¢ → $0.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 3,342 (50 yours) | ×0.2^0 = 3,342.5 |
|  | 50¢ | 25 | ×0.2^30 = 0.0 |
|  | 99¢ | 2,201 | ×0.2^79 = 0.0 |
| | | **Σ** | **3,342.5** |

`yours 50.0 / Σ 3,342.5 = 1.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.5% = $0.06/day`  

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
10. `scc-hrep-rep-2026-11-03-gte225` ← this one
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 1 @ 8¢ → $0.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 86 (1 yours) | ×0.2^0 = 86.0 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,773 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **86.1** |

`yours 1.0 / Σ 86.1 = 1.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.2% = $0.04/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 18¢ → $0.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 15¢ | 30 | ×0.2^0 = 30.0 |
|  | 17¢ | 2 | ×0.2^2 = 0.1 |
| ▶ | 18¢ | 34 (30 yours) | ×0.2^3 = 0.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,758 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **30.4** |

`yours 0.2 / Σ 30.4 = 0.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.8% = $0.03/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-30 | ~$43.67 | $20.48 | 47% |
| 2026-07-29 | ~$65.42 | $53.59 | 82% |
| 2026-07-28 | ~$148.78 | $79.65 | 54% |

Biggest gaps on 2026-07-30: `nocc-attgen-todblanche-2026-08-07` (est ~$3.65 → got $0.00), `scc-senate-gop-2026-11-03-51` (est ~$3.41 → got $1.26), `gsc-usfedgvmt-by-2026-10-01` (est ~$1.67 → got $0.00)

_2026-07-31 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,582 resting) | ~98.0% | ~$24.51 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,832 resting) | ~29.3% | ~$22.00 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (74,093 resting) | ~18.4% | ~$13.81 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (338,663 resting) | ~8.6% | ~$6.46 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (181,416 resting) | ~7.2% | ~$5.43 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (83,823 resting) | ~5.5% | ~$4.11 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (206,055 resting) | ~4.2% | ~$3.19 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (98,812 resting) | ~3.4% | ~$2.53 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (113,625 resting) | ~2.6% | ~$1.96 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (80,828 resting) | ~2.1% | ~$1.57 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,208 resting) | ~5.7% | ~$1.43 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (6,288 resting) | ~81.2% | ~$1.23 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,373.47 |
| Pending | $88.44 |
| Skipped | $1.21 |
| **Total earned** | **$1,463.12** |

1490 reward rows · 29 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-31 ⚠️ multi-day pending bucket | $67.96 | `██████` |
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
| 2026-07-18 | $44.41 | `████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.59 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.35 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.73 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.96 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-02 7:59 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:15 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 6:13 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 5:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 3:38 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 1:26 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 12:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 11:30 AM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 10:01 AM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:37 AM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
