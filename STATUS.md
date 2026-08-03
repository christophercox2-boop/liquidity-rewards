# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-03 3:51 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$72.65/day estimated (ceiling, not promise — details below)

**Earned:** $1,515.42 lifetime ($1,373.47 paid). Last three recorded days — 2026-08-01: **$52.30** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-31: **$67.96** · 2026-07-30: **$20.48** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — SELL at the best price, ~$22.95/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$19.15/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$16.37/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$72.65/day (~$3.03/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-52` | BUY | 21.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~99.9% of bid side (5,596 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 57.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~93.7% of ask side (6,238 resting ≥ 5,000 ✓) ≈ $3.91/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | SELL | 16.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~81.3% of ask side (9,677 resting ≥ 5,000 ✓) ≈ $20.32/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~70.3% of ask side (12,134 resting ≥ 5,000 ✓) ≈ $2.93/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 9.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~70.2% of ask side (18,250 resting ≥ 5,000 ✓) ≈ $2.92/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~66.6% of bid side (5,458 resting ≥ 5,000 ✓) ≈ $2.77/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~63.5% of ask side (12,353 resting ≥ 5,000 ✓) ≈ $2.44/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 12.0¢ | 33 | 0 | $100.00 | ✅ scoring — ~63.2% of ask side (12,161 resting ≥ 5,000 ✓) ≈ $2.43/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~60.4% of ask side (12,094 resting ≥ 5,000 ✓) ≈ $2.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 20.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~58.8% of bid side (5,522 resting ≥ 5,000 ✓) ≈ $2.26/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~50.0% of ask side (12,116 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 12.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~46.3% of ask side (12,178 resting ≥ 5,000 ✓) ≈ $1.78/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~33.2% of bid side (11,297 resting ≥ 5,000 ✓) ≈ $1.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 60 | 1 | $100.00 | ✅ scoring — ~32.4% of bid side (5,563 resting ≥ 5,000 ✓) ≈ $1.25/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 84.0¢ | 79 | 0 | $100.00 | ✅ scoring — ~32.1% of ask side (12,854 resting ≥ 5,000 ✓) ≈ $1.34/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~31.5% of ask side (12,178 resting ≥ 5,000 ✓) ≈ $1.21/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~30.3% of ask side (12,065 resting ≥ 5,000 ✓) ≈ $1.17/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~28.6% of bid side (5,550 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 45.0¢ | 13 | 0 | $100.00 | ✅ scoring — ~26.5% of ask side (8,367 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 81.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~25.9% of bid side (6,018 resting ≥ 5,000 ✓) ≈ $1.08/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 84.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~19.4% of bid side (5,491 resting ≥ 5,000 ✓) ≈ $0.81/day (pool ÷ 12 markets) |
| `pintc-meet-trump-2026-12-31-kimjon` | BUY | 20.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~18.1% of bid side (2,261 resting ≥ 2,000 ✓) ≈ $0.17/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 15.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~16.9% of ask side (12,260 resting ≥ 5,000 ✓) ≈ $0.65/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~15.4% of bid side (4,739 resting ≥ 2,500 ✓) ≈ $0.53/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 3.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~12.2% of bid side (8,379 resting ≥ 5,000 ✓) ≈ $0.47/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 6.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~12.2% of bid side (12,631 resting ≥ 5,000 ✓) ≈ $0.51/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 18.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~11.8% of bid side (5,522 resting ≥ 5,000 ✓) ≈ $0.45/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 15.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~10.9% of bid side (6,019 resting ≥ 5,000 ✓) ≈ $2.72/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 5.0¢ | 590 | 0 | $100.00 | ✅ scoring — ~10.7% of bid side (5,727 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 80.0¢ | 51 | 2 | $100.00 | ✅ scoring — ~10.6% of bid side (5,520 resting ≥ 5,000 ✓) ≈ $0.44/day (pool ÷ 12 markets) |
| …and 69 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 25 @ 21¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 18¢ | 4 | ×0.2^3 = 0.0 |
|  | 13¢ | 7 | ×0.2^8 = 0.0 |
|  | 9¢ | 4 | ×0.2^12 = 0.0 |
|  | 1¢ | 5,555 | ×0.2^20 = 0.0 |
| | | **Σ** | **25.0** |

`yours 25.0 / Σ 25.0 = 99.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.9% = $3.84/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 3 @ 57¢ → $3.91/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 3 (3 yours) | ×0.2^0 = 3.0 |
|  | 59¢ | 1 | ×0.2^2 = 0.0 |
|  | 60¢ | 20 | ×0.2^3 = 0.2 |
|  | 67¢ | 50 | ×0.2^10 = 0.0 |
|  | 77¢ | 1,905 | ×0.2^20 = 0.0 |
|  | 79¢ | 1,865 | ×0.2^22 = 0.0 |
|  | 80¢ | 190 | ×0.2^23 = 0.0 |
|  | 85¢ | 1 | ×0.2^28 = 0.0 |
|  | 90¢ | 1 | ×0.2^33 = 0.0 |
|  | 92¢ | 1 | ×0.2^35 = 0.0 |
| | … | +1 levels | 0.0 |
| | | **Σ** | **3.2** |

`yours 3.0 / Σ 3.2 = 93.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 93.7% = $3.91/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 16¢ → $20.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 123 (100 yours) | ×0.2^0 = 123.0 |
|  | 18¢ | 1 | ×0.2^2 = 0.0 |
|  | 30¢ | 192 | ×0.2^14 = 0.0 |
|  | 41¢ | 200 | ×0.2^25 = 0.0 |
|  | 49¢ | 100 | ×0.2^33 = 0.0 |
|  | 99¢ | 9,061 | ×0.2^83 = 0.0 |
| | | **Σ** | **123.0** |

`yours 100.0 / Σ 123.0 = 81.3%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 81.3% = $20.32/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 50 @ 8¢ → $2.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 71 (50 yours) | ×0.2^0 = 71.0 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 50¢ | 25 | ×0.2^42 = 0.0 |
|  | 99¢ | 12,036 | ×0.2^91 = 0.0 |
| | | **Σ** | **71.1** |

`yours 50.0 / Σ 71.1 = 70.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 70.3% = $2.93/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 9¢ → $2.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 71 (50 yours) | ×0.2^0 = 71.0 |
|  | 10¢ | 1 | ×0.2^1 = 0.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 15¢ | 15 | ×0.2^6 = 0.0 |
|  | 50¢ | 25 | ×0.2^41 = 0.0 |
|  | 99¢ | 18,137 | ×0.2^90 = 0.0 |
| | | **Σ** | **71.2** |

`yours 50.0 / Σ 71.2 = 70.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 70.2% = $2.92/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 10¢ → $2.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 63 (40 yours) | ×0.2^0 = 63.0 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **63.0** |

`yours 40.0 / Σ 63.0 = 63.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 63.5% = $2.44/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 33 @ 12¢ → $2.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 52 (33 yours) | ×0.2^0 = 52.0 |
|  | 15¢ | 30 | ×0.2^3 = 0.2 |
|  | 18¢ | 4 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 98¢ | 1,774 | ×0.2^86 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^87 = 0.0 |
| | | **Σ** | **52.2** |

`yours 33.0 / Σ 52.2 = 63.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 63.2% = $2.43/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 18 @ 15¢ → $2.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 30 (18 yours) | ×0.2^0 = 30.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **30.3** |

`yours 18.3 / Σ 30.3 = 60.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 60.4% = $2.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 21 @ 8¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 42 (21 yours) | ×0.2^0 = 42.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,773 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^91 = 0.0 |
| | | **Σ** | **42.0** |

`yours 21.0 / Σ 42.0 = 50.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 50.0% = $1.92/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 50 @ 12¢ → $1.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 108 (50 yours) | ×0.2^0 = 108.0 |
|  | 29¢ | 2 | ×0.2^17 = 0.0 |
|  | 35¢ | 2 | ×0.2^23 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 98¢ | 1,765 | ×0.2^86 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^87 = 0.0 |
| | | **Σ** | **108.0** |

`yours 50.0 / Σ 108.0 = 46.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 46.3% = $1.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $1.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1,107 (500 yours) | ×0.2^0 = 1,107.0 |
|  | 2¢ | 9,990 | ×0.2^2 = 399.6 |
| | | **Σ** | **1,506.6** |

`yours 500.0 / Σ 1,506.6 = 33.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.2% = $1.28/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 60 @ 15¢ → $1.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 17 | ×0.2^0 = 17.0 |
| ▶ | 15¢ | 100 (60 yours) | ×0.2^1 = 20.0 |
|  | 1¢ | 5,446 | ×0.2^15 = 0.0 |
| | | **Σ** | **37.0** |

`yours 12.0 / Σ 37.0 = 32.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.4% = $1.25/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 79 @ 84¢ → $1.34/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 246 (79 yours) | ×0.2^0 = 246.0 |
|  | 86¢ | 7 | ×0.2^2 = 0.3 |
|  | 94¢ | 205 | ×0.2^10 = 0.0 |
|  | 99¢ | 12,396 | ×0.2^15 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $1.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 127 (40 yours) | ×0.2^0 = 127.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **127.0** |

`yours 40.0 / Σ 127.0 = 31.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.5% = $1.21/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 10¢ → $1.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 33 (10 yours) | ×0.2^0 = 33.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **33.0** |

`yours 10.0 / Σ 33.0 = 30.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.3% = $1.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 100 @ 20¢ → $1.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 350 (100 yours) | ×0.2^0 = 350.0 |
|  | 1¢ | 5,200 | ×0.2^19 = 0.0 |
| | | **Σ** | **350.0** |

`yours 100.0 / Σ 350.0 = 28.6%`  
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
|  | 68¢ | 107 | ×0.2^23 = 0.0 |
|  | 81¢ | 107 | ×0.2^36 = 0.0 |
|  | 99¢ | 8,102 | ×0.2^54 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 10 @ 81¢ → $1.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 81¢ | 33 (10 yours) | ×0.2^0 = 33.0 |
|  | 79¢ | 1 | ×0.2^2 = 0.1 |
|  | 78¢ | 697 | ×0.2^3 = 5.6 |
|  | 75¢ | 83 | ×0.2^6 = 0.0 |
|  | 74¢ | 4 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^80 = 0.0 |
| | | **Σ** | **38.6** |

`yours 10.0 / Σ 38.6 = 25.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 25.9% = $1.08/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 20 @ 84¢ → $0.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 85¢ | 16 | ×0.2^0 = 16.0 |
| ▶ | 84¢ | 23 (20 yours) | ×0.2^1 = 4.6 |
|  | 83¢ | 1 | ×0.2^2 = 0.0 |
|  | 78¢ | 243 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,208 | ×0.2^84 = 0.0 |
| | | **Σ** | **20.7** |

`yours 4.0 / Σ 20.7 = 19.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.4% = $0.81/day`  

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
<details><summary><code>pintc-meet-trump-2026-12-31-kimjon</code> BUY 2 @ 20¢ → $0.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 11 (2 yours) | ×0.1^0 = 11.0 |
|  | 18¢ | 6 | ×0.1^2 = 0.1 |
|  | 5¢ | 100 | ×0.1^15 = 0.0 |
|  | 3¢ | 1 | ×0.1^17 = 0.0 |
|  | 1¢ | 2,143 | ×0.1^19 = 0.0 |
| | | **Σ** | **11.1** |

`yours 2.0 / Σ 11.1 = 18.1%`  
`$25 ÷ 13 ÷ 2 = $0.96 × 18.1% = $0.17/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon` ← this one
6. `pintc-meet-trump-2026-12-31-kimkar`
7. `pintc-meet-trump-2026-12-31-leoxiv`
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput`
11. `pintc-meet-trump-2026-12-31-volzel`
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 25 @ 15¢ → $0.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 148 (25 yours) | ×0.2^0 = 148.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,811 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **148.0** |

`yours 25.0 / Σ 148.0 = 16.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.9% = $0.65/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 940 | ×0.35^0 = 940.0 |
| ▶ | 1¢ | 3,799 (1,000 yours) | ×0.35^1 = 1,329.6 |
| | | **Σ** | **2,269.6** |

`yours 350.0 / Σ 2,269.6 = 15.4%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 15.4% = $0.53/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 1,000 @ 3¢ → $0.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,179 (1,000 yours) | ×0.2^0 = 8,179.0 |
| | | **Σ** | **8,179.0** |

`yours 1,000.0 / Σ 8,179.0 = 12.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 12.2% = $0.47/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 30 @ 6¢ → $0.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 225 (30 yours) | ×0.2^0 = 225.0 |
|  | 4¢ | 25 | ×0.2^2 = 1.0 |
|  | 3¢ | 5 | ×0.2^3 = 0.0 |
|  | 2¢ | 12,176 | ×0.2^4 = 19.5 |
| | | **Σ** | **245.5** |

`yours 30.0 / Σ 245.5 = 12.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 12.2% = $0.51/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 18¢ → $0.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 3 | ×0.2^0 = 3.0 |
| ▶ | 18¢ | 10 (10 yours) | ×0.2^2 = 0.4 |
|  | 10¢ | 100 | ×0.2^10 = 0.0 |
|  | 1¢ | 5,409 | ×0.2^19 = 0.0 |
| | | **Σ** | **3.4** |

`yours 0.4 / Σ 3.4 = 11.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.8% = $0.45/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 500 @ 15¢ → $2.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 4,596 (500 yours) | ×0.2^0 = 4,595.9 |
|  | 13¢ | 8 | ×0.2^2 = 0.3 |
|  | 11¢ | 1,215 | ×0.2^4 = 1.9 |
| | | **Σ** | **4,598.2** |

`yours 500.0 / Σ 4,598.2 = 10.9%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 10.9% = $2.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 590 @ 5¢ → $0.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 5,527 (590 yours) | ×0.2^0 = 5,527.0 |
| | | **Σ** | **5,527.0** |

`yours 590.0 / Σ 5,527.0 = 10.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 10.7% = $0.41/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 51 @ 80¢ → $0.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 82¢ | 17 | ×0.2^0 = 17.0 |
|  | 81¢ | 1 | ×0.2^1 = 0.1 |
| ▶ | 80¢ | 52 (51 yours) | ×0.2^2 = 2.1 |
|  | 1¢ | 5,450 | ×0.2^81 = 0.0 |
| | | **Σ** | **19.2** |

`yours 2.0 / Σ 19.2 = 10.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 10.6% = $0.44/day`  

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
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,673 resting) | ~30.6% | ~$22.95 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,374 resting) | ~76.6% | ~$19.15 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (26,613 resting) | ~65.5% | ~$16.37 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (70,160 resting) | ~59.0% | ~$14.75 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (74,182 resting) | ~19.0% | ~$14.24 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (181,506 resting) | ~8.6% | ~$6.47 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (84,184 resting) | ~7.4% | ~$5.58 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (198,699 resting) | ~6.8% | ~$5.07 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (96,533 resting) | ~5.6% | ~$4.19 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (96,461 resting) | ~4.7% | ~$3.51 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (112,828 resting) | ~3.3% | ~$2.48 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (80,513 resting) | ~24.4% | ~$1.52 |

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
| 2026-08-03 3:51 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-03 12:00 AM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-02 9:06 PM ET | ✅ ok | 1532 | $1515.42 |
| 2026-08-02 8:15 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:59 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 7:15 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 6:13 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 5:12 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 3:38 PM ET | ✅ ok | 1490 | $1463.12 |
| 2026-08-02 1:26 PM ET | ✅ ok | 1490 | $1463.12 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
