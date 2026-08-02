# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-02 7:37 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$21.77/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$7.60/day for 200 contracts. Runners-up: `cranc-uspres28-12-31-2026-kamhar` (~$1.49/day), `cranc-uspres28-12-31-2026-jdvan` (~$1.48/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$21.77/day (~$0.91/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-50` | SELL | 30.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~57.3% of ask side (12,212 resting ≥ 5,000 ✓) ≈ $2.21/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 34.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~55.6% of bid side (5,512 resting ≥ 5,000 ✓) ≈ $2.31/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 64.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~42.0% of ask side (6,072 resting ≥ 5,000 ✓) ≈ $1.75/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 18.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~41.7% of ask side (11,904 resting ≥ 5,000 ✓) ≈ $1.60/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~40.4% of ask side (11,909 resting ≥ 5,000 ✓) ≈ $1.55/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 19.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~40.3% of bid side (5,541 resting ≥ 5,000 ✓) ≈ $1.55/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~32.7% of ask side (11,916 resting ≥ 5,000 ✓) ≈ $1.26/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 11.0¢ | 35 | 0 | $100.00 | ✅ scoring — ~28.0% of bid side (5,340 resting ≥ 5,000 ✓) ≈ $1.08/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 16.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~21.8% of ask side (5,410 resting ≥ 5,000 ✓) ≈ $5.45/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 6.0¢ | 32 | 0 | $100.00 | ✅ scoring — ~15.4% of bid side (25,735 resting ≥ 5,000 ✓) ≈ $0.59/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 85.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~13.3% of bid side (5,548 resting ≥ 5,000 ✓) ≈ $0.55/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 4.0¢ | 66 | 0 | $100.00 | ✅ scoring — ~7.7% of bid side (25,958 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~6.0% of bid side (8,494 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 3 | $100.00 | ✅ scoring — ~4.7% of bid side (25,958 resting ≥ 5,000 ✓) ≈ $0.18/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 19.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~3.9% of bid side (5,900 resting ≥ 2,000 ✓) ≈ $0.49/day |
| `scc-hrep-rep-2026-11-03-gte205` | BUY | 48.0¢ | 12 | 0 | $100.00 | ✅ scoring — ~3.3% of bid side (5,827 resting ≥ 5,000 ✓) ≈ $0.14/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~3.2% of bid side (32,001 resting ≥ 5,000 ✓) ≈ $0.12/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 11 | 1 | $100.00 | ✅ scoring — ~1.9% of bid side (5,634 resting ≥ 5,000 ✓) ≈ $0.08/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 43.0¢ | 34 | 0 | $25.00 | ✅ scoring — ~1.8% of bid side (7,754 resting ≥ 2,000 ✓) ≈ $0.02/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~1.7% of bid side (5,634 resting ≥ 5,000 ✓) ≈ $0.07/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~1.4% of ask side (11,944 resting ≥ 5,000 ✓) ≈ $0.05/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 45.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~1.3% of ask side (12,198 resting ≥ 5,000 ✓) ≈ $0.05/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 52.0¢ | 40 | 1 | $100.00 | ✅ scoring — ~1.1% of ask side (8,222 resting ≥ 5,000 ✓) ≈ $0.05/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 1.0¢ | 5,000 | 5 | $100.00 | ✅ scoring — ~0.8% of bid side (25,735 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 67.0¢ | 50 | 3 | $100.00 | ✅ scoring — ~0.6% of ask side (6,072 resting ≥ 5,000 ✓) ≈ $0.02/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 45 | 0 | $100.00 | ✅ scoring — ~0.5% of bid side (8,494 resting ≥ 5,000 ✓) ≈ $0.02/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-tedcru` | SELL | 21.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~0.4% of ask side (5,529 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 33 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 5.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~0.1% of bid side (9,456 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | SELL | 89.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~0.1% of ask side (8,391 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 20.0¢ | 11 | 3 | $100.00 | ✅ scoring — ~0.0% of bid side (5,485 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| …and 17 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 30¢ → $2.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 30¢ | 75 (43 yours) | ×0.2^0 = 75.0 |
|  | 38¢ | 128 | ×0.2^8 = 0.0 |
|  | 44¢ | 37 | ×0.2^14 = 0.0 |
|  | 50¢ | 100 | ×0.2^20 = 0.0 |
|  | 98¢ | 1,871 | ×0.2^68 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^69 = 0.0 |
| | | **Σ** | **75.0** |

`yours 43.0 / Σ 75.0 = 57.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 57.3% = $2.21/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 20 @ 34¢ → $2.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 34 (20 yours) | ×0.2^0 = 34.0 |
|  | 33¢ | 10 | ×0.2^1 = 2.0 |
|  | 1¢ | 5,468 | ×0.2^33 = 0.0 |
| | | **Σ** | **36.0** |

`yours 20.0 / Σ 36.0 = 55.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 55.6% = $2.31/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 30 @ 64¢ → $1.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 64¢ | 71 (30 yours) | ×0.2^0 = 71.0 |
|  | 67¢ | 50 | ×0.2^3 = 0.4 |
|  | 77¢ | 1,893 | ×0.2^13 = 0.0 |
|  | 79¢ | 1,865 | ×0.2^15 = 0.0 |
|  | 80¢ | 190 | ×0.2^16 = 0.0 |
|  | 90¢ | 1 | ×0.2^26 = 0.0 |
|  | 93¢ | 1 | ×0.2^29 = 0.0 |
|  | 99¢ | 2,001 | ×0.2^35 = 0.0 |
| | | **Σ** | **71.4** |

`yours 30.0 / Σ 71.4 = 42.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 42.0% = $1.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 18¢ → $1.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 72 (30 yours) | ×0.2^0 = 72.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^81 = 0.0 |
| | | **Σ** | **72.0** |

`yours 30.0 / Σ 72.0 = 41.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 41.7% = $1.60/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 18 @ 15¢ → $1.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 45 (18 yours) | ×0.2^0 = 45.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **45.3** |

`yours 18.3 / Σ 45.3 = 40.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.4% = $1.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 50 @ 19¢ → $1.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 124 (50 yours) | ×0.2^0 = 124.0 |
|  | 8¢ | 4 | ×0.2^11 = 0.0 |
|  | 1¢ | 5,413 | ×0.2^18 = 0.0 |
| | | **Σ** | **124.0** |

`yours 50.0 / Σ 124.0 = 40.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.3% = $1.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 16¢ → $1.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 61 (20 yours) | ×0.2^0 = 61.2 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^82 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^83 = 0.0 |
| | | **Σ** | **61.2** |

`yours 20.0 / Σ 61.2 = 32.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.7% = $1.26/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 35 @ 11¢ → $1.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 125 (35 yours) | ×0.2^0 = 125.0 |
|  | 4¢ | 173 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,042 | ×0.2^10 = 0.0 |
| | | **Σ** | **125.0** |

`yours 35.0 / Σ 125.0 = 28.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.0% = $1.08/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 16¢ → $5.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 459 (100 yours) | ×0.2^0 = 459.1 |
|  | 33¢ | 192 | ×0.2^17 = 0.0 |
|  | 42¢ | 10 | ×0.2^26 = 0.0 |
|  | 49¢ | 100 | ×0.2^33 = 0.0 |
|  | 50¢ | 10 | ×0.2^34 = 0.0 |
|  | 57¢ | 10 | ×0.2^41 = 0.0 |
|  | 82¢ | 2 | ×0.2^66 = 0.0 |
|  | 83¢ | 2 | ×0.2^67 = 0.0 |
|  | 99¢ | 4,625 | ×0.2^83 = 0.0 |
| | | **Σ** | **459.1** |

`yours 100.0 / Σ 459.1 = 21.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 21.8% = $5.45/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 32 @ 6¢ → $0.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 198 (32 yours) | ×0.2^0 = 197.7 |
|  | 3¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 25,535 | ×0.2^5 = 8.2 |
| | | **Σ** | **205.9** |

`yours 31.7 / Σ 205.9 = 15.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 15.4% = $0.59/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 85¢ → $0.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 75 (10 yours) | ×0.2^0 = 75.3 |
|  | 1¢ | 5,473 | ×0.2^84 = 0.0 |
| | | **Σ** | **75.3** |

`yours 10.0 / Σ 75.3 = 13.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 13.3% = $0.55/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 66 @ 4¢ → $0.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 654 (66 yours) | ×0.2^0 = 653.9 |
|  | 1¢ | 25,304 | ×0.2^3 = 202.4 |
| | | **Σ** | **856.4** |

`yours 65.9 / Σ 856.4 = 7.7%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,294 (500 yours) | ×0.2^0 = 8,294.0 |
| | | **Σ** | **8,294.0** |

`yours 500.0 / Σ 8,294.0 = 6.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.0% = $0.23/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 654 | ×0.2^0 = 653.9 |
| ▶ | 1¢ | 25,304 (5,000 yours) | ×0.2^3 = 202.4 |
| | | **Σ** | **856.4** |

`yours 40.0 / Σ 856.4 = 4.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 4.7% = $0.18/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 15 @ 19¢ → $0.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 386 (15 yours) | ×0.1^0 = 386.4 |
|  | 18¢ | 2 | ×0.1^1 = 0.2 |
|  | 17¢ | 2 | ×0.1^2 = 0.0 |
|  | 10¢ | 5 | ×0.1^9 = 0.0 |
|  | 4¢ | 17 | ×0.1^15 = 0.0 |
|  | 3¢ | 188 | ×0.1^16 = 0.0 |
|  | 1¢ | 5,300 | ×0.1^18 = 0.0 |
| | | **Σ** | **386.6** |

`yours 15.0 / Σ 386.6 = 3.9%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 3.9% = $0.49/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> BUY 12 @ 48¢ → $0.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 365 (12 yours) | ×0.2^0 = 364.5 |
|  | 1¢ | 5,462 | ×0.2^47 = 0.0 |
| | | **Σ** | **364.5** |

`yours 12.0 / Σ 364.5 = 3.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.3% = $0.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 31,691 (1,000 yours) | ×0.2^0 = 31,691.0 |
| | | **Σ** | **31,691.0** |

`yours 1,000.0 / Σ 31,691.0 = 3.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.2% = $0.12/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 11 @ 75¢ → $0.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 76¢ | 113 | ×0.2^0 = 113.0 |
| ▶ | 75¢ | 21 (11 yours) | ×0.2^1 = 4.2 |
|  | 49¢ | 120 | ×0.2^27 = 0.0 |
|  | 1¢ | 5,380 | ×0.2^75 = 0.0 |
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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 34 @ 43¢ → $0.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 1,855 (34 yours) | ×0.1^0 = 1,855.0 |
|  | 37¢ | 6 | ×0.1^6 = 0.0 |
|  | 35¢ | 18 | ×0.1^8 = 0.0 |
|  | 7¢ | 499 | ×0.1^36 = 0.0 |
| | | **Σ** | **1,855.0** |

`yours 34.0 / Σ 1,855.0 = 1.8%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 1.8% = $0.02/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20` ← this one
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 75¢ → $0.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 76¢ | 113 | ×0.2^0 = 113.0 |
| ▶ | 75¢ | 21 (10 yours) | ×0.2^1 = 4.2 |
|  | 49¢ | 120 | ×0.2^27 = 0.0 |
|  | 1¢ | 5,380 | ×0.2^75 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 1 @ 8¢ → $0.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 70 (1 yours) | ×0.2^0 = 70.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,773 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^91 = 0.0 |
| | | **Σ** | **70.0** |

`yours 1.0 / Σ 70.0 = 1.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.4% = $0.05/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 10 @ 45¢ → $0.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 44¢ | 135 | ×0.2^0 = 135.0 |
| ▶ | 45¢ | 97 (10 yours) | ×0.2^1 = 19.4 |
|  | 50¢ | 100 | ×0.2^6 = 0.0 |
|  | 98¢ | 1,865 | ×0.2^54 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^55 = 0.0 |
| | | **Σ** | **154.4** |

`yours 2.0 / Σ 154.4 = 1.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.3% = $0.05/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 40 @ 52¢ → $0.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 51¢ | 717 | ×0.2^0 = 717.0 |
| ▶ | 52¢ | 40 (40 yours) | ×0.2^1 = 8.0 |
|  | 55¢ | 100 | ×0.2^4 = 0.2 |
|  | 99¢ | 7,365 | ×0.2^48 = 0.0 |
| | | **Σ** | **725.2** |

`yours 8.0 / Σ 725.2 = 1.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.1% = $0.05/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 5,000 @ 1¢ → $0.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 198 | ×0.2^0 = 197.7 |
|  | 3¢ | 2 | ×0.2^3 = 0.0 |
| ▶ | 1¢ | 25,535 (5,000 yours) | ×0.2^5 = 8.2 |
| | | **Σ** | **205.9** |

`yours 1.6 / Σ 205.9 = 0.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.8% = $0.03/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 67¢ → $0.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 64¢ | 71 | ×0.2^0 = 71.0 |
| ▶ | 67¢ | 50 (50 yours) | ×0.2^3 = 0.4 |
|  | 77¢ | 1,893 | ×0.2^13 = 0.0 |
|  | 79¢ | 1,865 | ×0.2^15 = 0.0 |
|  | 80¢ | 190 | ×0.2^16 = 0.0 |
|  | 90¢ | 1 | ×0.2^26 = 0.0 |
|  | 93¢ | 1 | ×0.2^29 = 0.0 |
|  | 99¢ | 2,001 | ×0.2^35 = 0.0 |
| | | **Σ** | **71.4** |

`yours 0.4 / Σ 71.4 = 0.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.6% = $0.02/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 45 @ 3¢ → $0.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,294 (45 yours) | ×0.2^0 = 8,294.0 |
| | | **Σ** | **8,294.0** |

`yours 45.0 / Σ 8,294.0 = 0.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.5% = $0.02/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-tedcru</code> SELL 0 @ 21¢ → $0.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 103 (0 yours) | ×0.2^0 = 103.0 |
|  | 24¢ | 2 | ×0.2^3 = 0.0 |
|  | 28¢ | 862 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^29 = 0.0 |
|  | 77¢ | 2 | ×0.2^56 = 0.0 |
|  | 78¢ | 2 | ×0.2^57 = 0.0 |
|  | 99¢ | 4,533 | ×0.2^78 = 0.0 |
| | | **Σ** | **103.0** |

`yours 0.4 / Σ 103.0 = 0.4%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 0.4% = $0.01/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru`
7. `cranc-uspres28-12-31-2026-dontrujr`
8. `cranc-uspres28-12-31-2026-dwajoh`
9. `cranc-uspres28-12-31-2026-elomus`
10. `cranc-uspres28-12-31-2026-erikir`
11. `cranc-uspres28-12-31-2026-gavnew`
12. `cranc-uspres28-12-31-2026-hilcli`
13. `cranc-uspres28-12-31-2026-hunbid`
14. `cranc-uspres28-12-31-2026-jdvan`
15. `cranc-uspres28-12-31-2026-jonoss`
16. `cranc-uspres28-12-31-2026-jossha`
17. `cranc-uspres28-12-31-2026-kamhar`
18. `cranc-uspres28-12-31-2026-krinoe`
19. `cranc-uspres28-12-31-2026-margre`
20. `cranc-uspres28-12-31-2026-markel`
21. `cranc-uspres28-12-31-2026-marrub`
22. `cranc-uspres28-12-31-2026-micoba`
23. `cranc-uspres28-12-31-2026-nikhal`
24. `cranc-uspres28-12-31-2026-oprwin`
25. `cranc-uspres28-12-31-2026-petbut`
26. `cranc-uspres28-12-31-2026-rahema`
27. `cranc-uspres28-12-31-2026-robken`
28. `cranc-uspres28-12-31-2026-steban`
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru` ← this one
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 10 @ 5¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 9,256 (10 yours) | ×0.2^0 = 9,256.0 |
| | | **Σ** | **9,256.0** |

`yours 10.0 / Σ 9,256.0 = 0.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.1% = $0.00/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> SELL 1 @ 89¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 629 (1 yours) | ×0.2^0 = 629.0 |
|  | 90¢ | 3,994 | ×0.2^1 = 798.8 |
|  | 99¢ | 3,768 | ×0.2^10 = 0.0 |
| | | **Σ** | **1,427.8** |

`yours 1.0 / Σ 1,427.8 = 0.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.1% = $0.00/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 11 @ 20¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 334 | ×0.2^0 = 333.6 |
| ▶ | 20¢ | 21 (11 yours) | ×0.2^3 = 0.2 |
|  | 1¢ | 5,130 | ×0.2^22 = 0.0 |
| | | **Σ** | **333.8** |

`yours 0.1 / Σ 333.8 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-29 | ~$65.42 | $53.59 | 82% |
| 2026-07-28 | ~$148.78 | $79.65 | 54% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |

Biggest gaps on 2026-07-29: `apdc-petehegseth-2026-12-31` (est ~$12.90 → got $1.16), `scc-senate-gop-2026-11-03-51` (est ~$3.25 → got $0.00), `scc-senate-gop-2026-11-03-54` (est ~$2.11 → got $0.02)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,484 resting) | ~30.4% | ~$7.60 |
| `cranc-uspres28-12-31-2026-kamhar` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (10,455 resting) | ~98.3% | ~$1.49 |
| `cranc-uspres28-12-31-2026-jdvan` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (29,797 resting) | ~98.0% | ~$1.48 |
| `cranc-uspres28-12-31-2026-hunbid` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,641 resting) | ~86.6% | ~$1.31 |
| `cranc-uspres28-12-31-2026-gavnew` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (81,772 resting) | ~75.2% | ~$1.14 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,657 resting) | ~64.0% | ~$0.97 |
| `cranc-uspres28-12-31-2026-erikir` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,528 resting) | ~63.6% | ~$0.96 |
| `cranc-uspres28-12-31-2026-rahema` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,520 resting) | ~59.3% | ~$0.90 |
| `cranc-uspres28-12-31-2026-betoro` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,706 resting) | ~58.5% | ~$0.89 |
| `cranc-uspres28-12-31-2026-stesmi` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (9,136 resting) | ~58.5% | ~$0.89 |
| `cranc-uspres28-12-31-2026-corboo` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,529 resting) | ~58.5% | ~$0.89 |
| `cranc-uspres28-12-31-2026-robken` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,231 resting) | ~54.8% | ~$0.83 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,373.47 |
| Skipped | $1.21 |
| **Total earned** | **$1,374.68** |

1406 reward rows · 27 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
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
| 2026-07-17 | $14.71 | `█` |
| 2026-07-16 | $17.02 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,374.68 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.26 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.82 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.47 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.25 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.73 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.96 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-02 7:37 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-02 5:24 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-02 2:48 AM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 11:57 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 9:53 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 8:15 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 7:23 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 7:14 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 6:13 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 5:12 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
