# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-04 10:45 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$93.01/day estimated (ceiling, not promise — details below)

**Earned:** $1,529.47 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-02: **$14.05** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-01: **$52.30** · 2026-07-31: **$67.96** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-mikmaz` — BUY at the best price, ~$24.82/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$15.23/day), `apdc-jerpowgov-2026-12-31` (~$14.59/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$93.01/day (~$3.88/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (12,049 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 24.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~99.3% of bid side (5,451 resting ≥ 5,000 ✓) ≈ $3.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 14.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~96.1% of bid side (5,478 resting ≥ 5,000 ✓) ≈ $3.70/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 65.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~80.3% of ask side (12,315 resting ≥ 5,000 ✓) ≈ $3.35/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 41 | 0 | $100.00 | ✅ scoring — ~77.4% of ask side (12,139 resting ≥ 5,000 ✓) ≈ $2.98/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~76.2% of ask side (10,019 resting ≥ 5,000 ✓) ≈ $19.06/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 9.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~73.7% of ask side (12,263 resting ≥ 5,000 ✓) ≈ $2.84/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | BUY | 18.0¢ | 150 | 0 | $100.00 | ✅ scoring — ~64.0% of bid side (12,042 resting ≥ 5,000 ✓) ≈ $16.01/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 25.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~61.0% of ask side (12,143 resting ≥ 5,000 ✓) ≈ $2.34/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~55.5% of ask side (12,070 resting ≥ 5,000 ✓) ≈ $2.13/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~54.8% of ask side (12,144 resting ≥ 5,000 ✓) ≈ $2.11/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 14.0¢ | 8 | 0 | $25.00 | ✅ scoring — ~50.9% of bid side (40,403 resting ≥ 2,000 ✓) ≈ $6.36/day |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 79.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~49.9% of bid side (5,519 resting ≥ 5,000 ✓) ≈ $2.08/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 5.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~41.1% of ask side (11,306 resting ≥ 5,000 ✓) ≈ $1.71/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 9.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~38.6% of ask side (12,335 resting ≥ 5,000 ✓) ≈ $1.48/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 50.0¢ | 12 | 0 | $100.00 | ✅ scoring — ~37.4% of ask side (7,449 resting ≥ 5,000 ✓) ≈ $1.56/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~34.4% of ask side (12,388 resting ≥ 5,000 ✓) ≈ $1.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 7.0¢ | 3 | 1 | $100.00 | ✅ scoring — ~29.2% of bid side (25,570 resting ≥ 5,000 ✓) ≈ $1.12/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 83.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~28.6% of bid side (5,480 resting ≥ 5,000 ✓) ≈ $1.19/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 20.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~26.3% of ask side (7,728 resting ≥ 5,000 ✓) ≈ $1.09/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~20.2% of ask side (12,350 resting ≥ 5,000 ✓) ≈ $0.84/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~19.8% of bid side (5,360 resting ≥ 5,000 ✓) ≈ $0.83/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 7.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~19.7% of ask side (12,274 resting ≥ 5,000 ✓) ≈ $0.76/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~18.6% of bid side (4,674 resting ≥ 2,500 ✓) ≈ $0.64/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 82.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~18.1% of bid side (5,617 resting ≥ 5,000 ✓) ≈ $0.75/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 27.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~16.6% of bid side (5,552 resting ≥ 5,000 ✓) ≈ $0.64/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 21.0¢ | 80 | 1 | $100.00 | ✅ scoring — ~12.2% of ask side (10,019 resting ≥ 5,000 ✓) ≈ $3.06/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 26.0¢ | 25 | 1 | $100.00 | ✅ scoring — ~11.9% of ask side (12,281 resting ≥ 5,000 ✓) ≈ $0.46/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 30 | 3 | $100.00 | ✅ scoring — ~11.7% of ask side (12,002 resting ≥ 5,000 ✓) ≈ $0.49/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 7.0¢ | 400 | 0 | $100.00 | ✅ scoring — ~11.2% of bid side (8,986 resting ≥ 5,000 ✓) ≈ $0.47/day (pool ÷ 12 markets) |
| …and 68 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 3 @ 15¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 3 (3 yours) | ×0.2^0 = 3.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,745 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^84 = 0.0 |
| | | **Σ** | **3.3** |

`yours 3.3 / Σ 3.3 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 25 @ 24¢ → $3.82/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 22¢ | 5 | ×0.2^2 = 0.2 |
|  | 12¢ | 163 | ×0.2^12 = 0.0 |
|  | 1¢ | 5,258 | ×0.2^23 = 0.0 |
| | | **Σ** | **25.2** |

`yours 25.0 / Σ 25.2 = 99.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.3% = $3.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 15 @ 14¢ → $3.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 13¢ | 1 | ×0.2^1 = 0.2 |
|  | 12¢ | 10 | ×0.2^2 = 0.4 |
|  | 6¢ | 32 | ×0.2^8 = 0.0 |
|  | 1¢ | 5,420 | ×0.2^13 = 0.0 |
| | | **Σ** | **15.6** |

`yours 15.0 / Σ 15.6 = 96.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 96.1% = $3.70/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 25 @ 65¢ → $3.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 29 (25 yours) | ×0.2^0 = 29.0 |
|  | 67¢ | 53 | ×0.2^2 = 2.1 |
|  | 70¢ | 1 | ×0.2^5 = 0.0 |
|  | 83¢ | 164 | ×0.2^18 = 0.0 |
|  | 90¢ | 1 | ×0.2^25 = 0.0 |
|  | 99¢ | 12,067 | ×0.2^34 = 0.0 |
| | | **Σ** | **31.1** |

`yours 25.0 / Σ 31.1 = 80.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 80.3% = $3.35/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 41 @ 22¢ → $2.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 53 (41 yours) | ×0.2^0 = 53.2 |
|  | 24¢ | 1 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 98¢ | 1,784 | ×0.2^76 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^77 = 0.0 |
| | | **Σ** | **53.2** |

`yours 41.2 / Σ 53.2 = 77.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 77.4% = $2.98/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 20¢ → $19.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 112 (100 yours) | ×0.2^0 = 112.0 |
|  | 21¢ | 80 | ×0.2^1 = 16.0 |
|  | 22¢ | 71 | ×0.2^2 = 2.9 |
|  | 24¢ | 192 | ×0.2^4 = 0.3 |
|  | 99¢ | 9,564 | ×0.2^79 = 0.0 |
| | | **Σ** | **131.2** |

`yours 100.0 / Σ 131.2 = 76.2%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 76.2% = $19.06/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 9¢ → $2.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 30 (30 yours) | ×0.2^0 = 30.0 |
|  | 11¢ | 101 | ×0.2^2 = 4.0 |
|  | 12¢ | 831 | ×0.2^3 = 6.6 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **40.7** |

`yours 30.0 / Σ 40.7 = 73.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 73.7% = $2.84/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 150 @ 18¢ → $16.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 150 (150 yours) | ×0.2^0 = 150.0 |
|  | 17¢ | 1 | ×0.2^1 = 0.2 |
|  | 16¢ | 6 | ×0.2^2 = 0.3 |
|  | 15¢ | 10,470 | ×0.2^3 = 83.8 |
| | | **Σ** | **234.2** |

`yours 150.0 / Σ 234.2 = 64.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 64.0% = $16.01/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 8 @ 25¢ → $2.34/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 13 (8 yours) | ×0.2^0 = 12.9 |
|  | 27¢ | 1 | ×0.2^2 = 0.1 |
|  | 39¢ | 50 | ×0.2^14 = 0.0 |
|  | 50¢ | 100 | ×0.2^25 = 0.0 |
|  | 98¢ | 1,778 | ×0.2^73 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^74 = 0.0 |
| | | **Σ** | **12.9** |

`yours 7.9 / Σ 12.9 = 61.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 61.0% = $2.34/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 15 @ 18¢ → $2.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 27 (15 yours) | ×0.2^0 = 27.0 |
|  | 20¢ | 1 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,741 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^81 = 0.0 |
| | | **Σ** | **27.1** |

`yours 15.0 / Σ 27.1 = 55.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.5% = $2.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 40 @ 6¢ → $2.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 73 (40 yours) | ×0.2^0 = 73.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,750 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^93 = 0.0 |
| | | **Σ** | **73.0** |

`yours 40.0 / Σ 73.0 = 54.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 54.8% = $2.11/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 8 @ 14¢ → $6.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 8 (8 yours) | ×0.1^0 = 7.7 |
|  | 13¢ | 74 | ×0.1^1 = 7.4 |
|  | 8¢ | 1 | ×0.1^6 = 0.0 |
|  | 6¢ | 5 | ×0.1^8 = 0.0 |
|  | 4¢ | 6 | ×0.1^10 = 0.0 |
|  | 2¢ | 7 | ×0.1^12 = 0.0 |
|  | 1¢ | 40,302 | ×0.1^13 = 0.0 |
| | | **Σ** | **15.1** |

`yours 7.7 / Σ 15.1 = 50.9%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 50.9% = $6.36/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 20 @ 79¢ → $2.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 33 (20 yours) | ×0.2^0 = 33.0 |
|  | 78¢ | 35 | ×0.2^1 = 7.0 |
|  | 77¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,450 | ×0.2^78 = 0.0 |
| | | **Σ** | **40.1** |

`yours 20.0 / Σ 40.1 = 49.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 49.9% = $2.08/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 50 @ 5¢ → $1.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 120 (50 yours) | ×0.2^0 = 120.3 |
|  | 7¢ | 16 | ×0.2^2 = 0.6 |
|  | 8¢ | 100 | ×0.2^3 = 0.8 |
|  | 10¢ | 1 | ×0.2^5 = 0.0 |
|  | 50¢ | 25 | ×0.2^45 = 0.0 |
|  | 99¢ | 11,044 | ×0.2^94 = 0.0 |
| | | **Σ** | **121.7** |

`yours 50.0 / Σ 121.7 = 41.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 41.1% = $1.71/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 40 @ 9¢ → $1.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 103 (40 yours) | ×0.2^0 = 103.4 |
|  | 10¢ | 1 | ×0.2^1 = 0.2 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 30¢ | 112 | ×0.2^21 = 0.0 |
|  | 50¢ | 100 | ×0.2^41 = 0.0 |
|  | 98¢ | 1,817 | ×0.2^89 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^90 = 0.0 |
| | | **Σ** | **103.6** |

`yours 40.0 / Σ 103.6 = 38.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.6% = $1.48/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 12 @ 50¢ → $1.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 32 (12 yours) | ×0.2^0 = 32.0 |
|  | 52¢ | 2 | ×0.2^2 = 0.1 |
|  | 57¢ | 107 | ×0.2^7 = 0.0 |
|  | 81¢ | 107 | ×0.2^31 = 0.0 |
|  | 99¢ | 7,201 | ×0.2^49 = 0.0 |
| | | **Σ** | **32.1** |

`yours 12.0 / Σ 32.1 = 37.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 37.4% = $1.56/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 50 @ 10¢ → $1.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 112 (50 yours) | ×0.2^0 = 112.0 |
|  | 11¢ | 166 | ×0.2^1 = 33.2 |
|  | 12¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,808 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^89 = 0.0 |
| | | **Σ** | **145.2** |

`yours 50.0 / Σ 145.2 = 34.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.4% = $1.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 3 @ 7¢ → $1.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 1 | ×0.2^0 = 1.1 |
| ▶ | 7¢ | 3 (3 yours) | ×0.2^1 = 0.6 |
|  | 2¢ | 232 | ×0.2^6 = 0.0 |
|  | 1¢ | 25,334 | ×0.2^7 = 0.3 |
| | | **Σ** | **2.0** |

`yours 0.6 / Σ 2.0 = 29.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.2% = $1.12/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 20 @ 83¢ → $1.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 83¢ | 70 (20 yours) | ×0.2^0 = 70.0 |
|  | 81¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 5,209 | ×0.2^81 = 0.0 |
| | | **Σ** | **70.0** |

`yours 20.0 / Σ 70.0 = 28.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 28.6% = $1.19/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 30 @ 20¢ → $1.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 114 (30 yours) | ×0.2^0 = 114.2 |
|  | 22¢ | 1 | ×0.2^2 = 0.1 |
|  | 99¢ | 7,613 | ×0.2^79 = 0.0 |
| | | **Σ** | **114.2** |

`yours 30.0 / Σ 114.2 = 26.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 26.3% = $1.09/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 30 @ 85¢ → $0.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 148 (30 yours) | ×0.2^0 = 148.0 |
|  | 87¢ | 8 | ×0.2^2 = 0.3 |
|  | 89¢ | 73 | ×0.2^4 = 0.1 |
|  | 99¢ | 12,121 | ×0.2^14 = 0.0 |
| | | **Σ** | **148.4** |

`yours 30.0 / Σ 148.4 = 20.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 20.2% = $0.84/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 30 @ 85¢ → $0.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 151 (30 yours) | ×0.2^0 = 151.2 |
|  | 83¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 5,208 | ×0.2^84 = 0.0 |
| | | **Σ** | **151.3** |

`yours 30.0 / Σ 151.3 = 19.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 19.8% = $0.83/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 31 @ 7¢ → $0.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 157 (31 yours) | ×0.2^0 = 157.2 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 98¢ | 1,815 | ×0.2^91 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^92 = 0.0 |
| | | **Σ** | **157.3** |

`yours 31.0 / Σ 157.3 = 19.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.7% = $0.76/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 375 | ×0.35^0 = 375.0 |
| ▶ | 1¢ | 4,299 (1,000 yours) | ×0.35^1 = 1,504.6 |
| | | **Σ** | **1,879.6** |

`yours 350.0 / Σ 1,879.6 = 18.6%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 18.6% = $0.64/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 30 @ 82¢ → $0.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 166 (30 yours) | ×0.2^0 = 165.6 |
|  | 80¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 5,450 | ×0.2^81 = 0.0 |
| | | **Σ** | **165.6** |

`yours 30.0 / Σ 165.6 = 18.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.1% = $0.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 5 @ 27¢ → $0.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 30 (5 yours) | ×0.2^0 = 30.0 |
|  | 25¢ | 4 | ×0.2^2 = 0.2 |
|  | 24¢ | 1 | ×0.2^3 = 0.0 |
|  | 18¢ | 7 | ×0.2^9 = 0.0 |
|  | 8¢ | 101 | ×0.2^19 = 0.0 |
|  | 1¢ | 5,409 | ×0.2^26 = 0.0 |
| | | **Σ** | **30.2** |

`yours 5.0 / Σ 30.2 = 16.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.6% = $0.64/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 80 @ 21¢ → $3.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 112 | ×0.2^0 = 112.0 |
| ▶ | 21¢ | 80 (80 yours) | ×0.2^1 = 16.0 |
|  | 22¢ | 71 | ×0.2^2 = 2.9 |
|  | 24¢ | 192 | ×0.2^4 = 0.3 |
|  | 99¢ | 9,564 | ×0.2^79 = 0.0 |
| | | **Σ** | **131.2** |

`yours 16.0 / Σ 131.2 = 12.2%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 12.2% = $3.06/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 25 @ 26¢ → $0.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 25¢ | 37 | ×0.2^0 = 37.0 |
| ▶ | 26¢ | 25 (25 yours) | ×0.2^1 = 5.0 |
|  | 27¢ | 1 | ×0.2^2 = 0.1 |
|  | 47¢ | 99 | ×0.2^22 = 0.0 |
|  | 50¢ | 99 | ×0.2^25 = 0.0 |
|  | 98¢ | 1,819 | ×0.2^73 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^74 = 0.0 |
| | | **Σ** | **42.1** |

`yours 5.0 / Σ 42.1 = 11.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.9% = $0.46/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 30 @ 47¢ → $0.49/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 44¢ | 2 | ×0.2^0 = 1.8 |
|  | 46¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 47¢ | 30 (30 yours) | ×0.2^3 = 0.2 |
|  | 52¢ | 1 | ×0.2^8 = 0.0 |
|  | 99¢ | 11,968 | ×0.2^55 = 0.0 |
| | | **Σ** | **2.1** |

`yours 0.2 / Σ 2.1 = 11.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.7% = $0.49/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 400 @ 7¢ → $0.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 3,583 (400 yours) | ×0.2^0 = 3,583.0 |
|  | 5¢ | 20 | ×0.2^2 = 0.8 |
|  | 1¢ | 5,383 | ×0.2^6 = 0.3 |
| | | **Σ** | **3,584.1** |

`yours 400.0 / Σ 3,584.1 = 11.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.2% = $0.47/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-01 | ~$46.23 | $52.30 | 113% |
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |

Biggest gaps on 2026-08-01: `scc-hrep-rep-2026-11-03-gte215` (est ~$2.09 → got $1.51), `scc-senate-gop-2026-11-03-52` (est ~$3.15 → got $2.78), `cranc-uspres28-12-31-2026-tedcru` (est ~$0.71 → got $0.35)

_2026-08-02 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (25,548 resting) | ~99.3% | ~$24.82 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,761 resting) | ~60.9% | ~$15.23 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,591 resting) | ~58.4% | ~$14.59 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,279 resting) | ~51.0% | ~$12.74 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (50,639 resting) | ~7.1% | ~$5.31 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (239,469 resting) | ~7.0% | ~$5.28 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (323,031 resting) | ~4.6% | ~$3.46 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (87,369 resting) | ~7.8% | ~$1.95 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (85,320 resting) | ~2.6% | ~$1.91 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (176,057 resting) | ~1.9% | ~$1.46 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (64,397 resting) | ~18.9% | ~$1.18 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (72,507 resting) | ~1.4% | ~$1.02 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,514.21 |
| Pending | $14.05 |
| Skipped | $1.21 |
| **Total earned** | **$1,529.47** |

1573 reward rows · 31 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-02 ⚠️ multi-day pending bucket | $14.05 | `█` |
| 2026-08-01 | $52.30 | `█████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $66.35 | `█` |
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $35.05 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `apdc-alito-2026-12-31` | $23.38 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-04 10:45 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 8:21 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 6:01 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 2:43 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 11:42 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 10:10 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:31 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:24 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:12 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:10 PM ET | ✅ ok | 1573 | $1529.47 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
