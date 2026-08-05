# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-05 2:45 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$40.93/day estimated (ceiling, not promise — details below)

**Earned:** $1,574.28 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-03: **$44.81** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-02: **$14.05** · 2026-08-01: **$52.30** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — SELL at the best price, ~$16.07/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$14.44/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$12.69/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$40.93/day (~$1.71/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (200,602 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 21.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~97.9% of bid side (50,316 resting ≥ 5,000 ✓) ≈ $3.77/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 61.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~97.3% of ask side (62,946 resting ≥ 5,000 ✓) ≈ $4.05/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 28 | 0 | $100.00 | ✅ scoring — ~70.0% of ask side (112,763 resting ≥ 5,000 ✓) ≈ $2.69/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 78.0¢ | 6 | 0 | $100.00 | ✅ scoring — ~66.3% of bid side (80,460 resting ≥ 5,000 ✓) ≈ $2.76/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 87.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~33.1% of bid side (50,592 resting ≥ 5,000 ✓) ≈ $1.38/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | SELL | 19.0¢ | 126 | 0 | $100.00 | ✅ scoring — ~28.8% of ask side (6,319 resting ≥ 5,000 ✓) ≈ $7.20/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 48.0¢ | 11 | 0 | $100.00 | ✅ scoring — ~23.8% of bid side (80,508 resting ≥ 5,000 ✓) ≈ $0.99/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~23.8% of bid side (80,335 resting ≥ 5,000 ✓) ≈ $0.99/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~19.9% of bid side (4,549 resting ≥ 2,500 ✓) ≈ $0.68/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 15.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~18.0% of ask side (62,880 resting ≥ 5,000 ✓) ≈ $0.75/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 38.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~17.3% of ask side (62,842 resting ≥ 5,000 ✓) ≈ $0.72/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | BUY | 18.0¢ | 150 | 0 | $100.00 | ✅ scoring — ~16.4% of bid side (5,501 resting ≥ 5,000 ✓) ≈ $4.10/day (pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | BUY | 18.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~10.9% of bid side (5,501 resting ≥ 5,000 ✓) ≈ $2.73/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 8.0¢ | 44 | 0 | $100.00 | ✅ scoring — ~9.2% of bid side (11,170 resting ≥ 5,000 ✓) ≈ $0.36/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~9.0% of bid side (80,621 resting ≥ 5,000 ✓) ≈ $0.38/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 5.0¢ | 133 | 0 | $100.00 | ✅ scoring — ~8.2% of bid side (51,830 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~8.0% of ask side (117,787 resting ≥ 5,000 ✓) ≈ $0.31/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 4 | $100.00 | ✅ scoring — ~7.1% of bid side (25,567 resting ≥ 5,000 ✓) ≈ $0.27/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 1 | $100.00 | ✅ scoring — ~6.2% of bid side (51,830 resting ≥ 5,000 ✓) ≈ $0.24/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 6.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~5.9% of ask side (113,623 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~5.8% of ask side (62,992 resting ≥ 5,000 ✓) ≈ $0.24/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~4.7% of ask side (48,046 resting ≥ 5,000 ✓) ≈ $0.20/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 5.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~3.5% of bid side (25,567 resting ≥ 5,000 ✓) ≈ $0.14/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~3.0% of ask side (58,935 resting ≥ 5,000 ✓) ≈ $0.12/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 14.0¢ | 12 | 0 | $100.00 | ✅ scoring — ~2.7% of bid side (87,936 resting ≥ 5,000 ✓) ≈ $0.11/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 18.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~2.6% of ask side (113,685 resting ≥ 5,000 ✓) ≈ $0.10/day (pool ÷ 13 markets) |
| `ewc-usse-oh-2026-11-03-rep` | BUY | 48.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~2.1% of bid side (58,620 resting ≥ 5,000 ✓) ≈ $0.52/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 35.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~2.0% of bid side (81,686 resting ≥ 5,000 ✓) ≈ $0.08/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 89.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~1.4% of ask side (54,770 resting ≥ 5,000 ✓) ≈ $0.06/day (pool ÷ 12 markets) |
| …and 16 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 15 @ 18¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 5¢ | 50 | ×0.2^13 = 0.0 |
|  | 1¢ | 200,538 | ×0.2^17 = 0.0 |
| | | **Σ** | **15.0** |

`yours 15.0 / Σ 15.0 = 100.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 21¢ → $3.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 19¢ | 5 | ×0.2^2 = 0.2 |
|  | 14¢ | 42 | ×0.2^7 = 0.0 |
|  | 7¢ | 58 | ×0.2^14 = 0.0 |
|  | 2¢ | 50,000 | ×0.2^19 = 0.0 |
| | | **Σ** | **10.2** |

`yours 10.0 / Σ 10.2 = 97.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 97.9% = $3.77/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 40 @ 61¢ → $4.05/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 61¢ | 41 (40 yours) | ×0.2^0 = 41.0 |
|  | 63¢ | 3 | ×0.2^2 = 0.1 |
|  | 65¢ | 1 | ×0.2^4 = 0.0 |
|  | 71¢ | 200 | ×0.2^10 = 0.0 |
|  | 90¢ | 1 | ×0.2^29 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^37 = 0.0 |
| | | **Σ** | **41.1** |

`yours 40.0 / Σ 41.1 = 97.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 97.3% = $4.05/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 28 @ 22¢ → $2.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 40 (28 yours) | ×0.2^0 = 40.1 |
|  | 24¢ | 1 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 97¢ | 58,044 | ×0.2^75 = 0.0 |
| | | **Σ** | **40.2** |

`yours 28.1 / Σ 40.2 = 70.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 70.0% = $2.69/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 6 @ 78¢ → $2.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 9 (6 yours) | ×0.2^0 = 9.0 |
|  | 76¢ | 1 | ×0.2^2 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^76 = 0.0 |
| | | **Σ** | **9.1** |

`yours 6.0 / Σ 9.1 = 66.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.3% = $2.76/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 87¢ → $1.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 30 (10 yours) | ×0.2^0 = 30.0 |
|  | 84¢ | 5 | ×0.2^3 = 0.0 |
|  | 83¢ | 107 | ×0.2^4 = 0.2 |
|  | 2¢ | 50,250 | ×0.2^85 = 0.0 |
| | | **Σ** | **30.2** |

`yours 10.0 / Σ 30.2 = 33.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 33.1% = $1.38/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 126 @ 19¢ → $7.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 438 (126 yours) | ×0.2^0 = 438.2 |
|  | 21¢ | 1 | ×0.2^2 = 0.1 |
|  | 25¢ | 579 | ×0.2^6 = 0.0 |
|  | 49¢ | 100 | ×0.2^30 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^80 = 0.0 |
| | | **Σ** | **438.3** |

`yours 126.2 / Σ 438.3 = 28.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 28.8% = $7.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 11 @ 48¢ → $0.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 46 (11 yours) | ×0.2^0 = 46.0 |
|  | 46¢ | 2 | ×0.2^2 = 0.1 |
|  | 45¢ | 10 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^46 = 0.0 |
| | | **Σ** | **46.2** |

`yours 11.0 / Σ 46.2 = 23.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 23.8% = $0.99/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 30 @ 85¢ → $0.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 126 (30 yours) | ×0.2^0 = 126.0 |
|  | 83¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 80,008 | ×0.2^83 = 0.0 |
| | | **Σ** | **126.1** |

`yours 30.0 / Σ 126.1 = 23.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 23.8% = $0.99/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 250 | ×0.35^0 = 250.0 |
| ▶ | 1¢ | 4,299 (1,000 yours) | ×0.35^1 = 1,504.6 |
| | | **Σ** | **1,754.6** |

`yours 350.0 / Σ 1,754.6 = 19.9%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 19.9% = $0.68/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 10 @ 15¢ → $0.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 31 (10 yours) | ×0.2^0 = 31.0 |
|  | 16¢ | 122 | ×0.2^1 = 24.4 |
|  | 17¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 25 | ×0.2^35 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^83 = 0.0 |
| | | **Σ** | **55.4** |

`yours 10.0 / Σ 55.4 = 18.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.0% = $0.75/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 7 @ 38¢ → $0.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 39 (7 yours) | ×0.2^0 = 39.1 |
|  | 40¢ | 2 | ×0.2^2 = 0.1 |
|  | 52¢ | 1 | ×0.2^14 = 0.0 |
|  | 69¢ | 100 | ×0.2^31 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^60 = 0.0 |
| | | **Σ** | **39.2** |

`yours 6.8 / Σ 39.2 = 17.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 17.3% = $0.72/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 150 @ 18¢ → $4.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 894 (150 yours) | ×0.2^0 = 894.4 |
|  | 17¢ | 100 | ×0.2^1 = 20.0 |
|  | 16¢ | 6 | ×0.2^2 = 0.3 |
|  | 15¢ | 30 | ×0.2^3 = 0.2 |
|  | 11¢ | 1,215 | ×0.2^7 = 0.0 |
|  | 1¢ | 3,255 | ×0.2^17 = 0.0 |
| | | **Σ** | **914.9** |

`yours 150.0 / Σ 914.9 = 16.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 16.4% = $4.10/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 100 @ 18¢ → $2.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 894 (100 yours) | ×0.2^0 = 894.4 |
|  | 17¢ | 100 | ×0.2^1 = 20.0 |
|  | 16¢ | 6 | ×0.2^2 = 0.3 |
|  | 15¢ | 30 | ×0.2^3 = 0.2 |
|  | 11¢ | 1,215 | ×0.2^7 = 0.0 |
|  | 1¢ | 3,255 | ×0.2^17 = 0.0 |
| | | **Σ** | **914.9** |

`yours 100.0 / Σ 914.9 = 10.9%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 10.9% = $2.73/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 44 @ 8¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 66 (44 yours) | ×0.2^0 = 66.0 |
|  | 6¢ | 10,266 | ×0.2^2 = 410.6 |
| | | **Σ** | **476.6** |

`yours 44.0 / Σ 476.6 = 9.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.2% = $0.36/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 10 @ 10¢ → $0.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 110 (10 yours) | ×0.2^0 = 110.0 |
|  | 8¢ | 12 | ×0.2^2 = 0.5 |
|  | 1¢ | 80,498 | ×0.2^9 = 0.0 |
| | | **Σ** | **110.5** |

`yours 10.0 / Σ 110.5 = 9.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 9.0% = $0.38/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 133 @ 5¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1,117 (133 yours) | ×0.2^0 = 1,117.0 |
|  | 4¢ | 500 | ×0.2^1 = 100.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **1,618.2** |

`yours 133.0 / Σ 1,618.2 = 8.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.2% = $0.32/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 1 @ 4¢ → $0.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 11 (1 yours) | ×0.2^0 = 10.5 |
|  | 5¢ | 10 | ×0.2^1 = 2.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **12.6** |

`yours 1.0 / Σ 12.6 = 8.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.0% = $0.31/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 68 | ×0.2^0 = 68.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 422 | ×0.2^3 = 3.4 |
| ▶ | 1¢ | 25,044 (5,000 yours) | ×0.2^4 = 40.1 |
| | | **Σ** | **112.8** |

`yours 8.0 / Σ 112.8 = 7.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.1% = $0.27/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $0.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 1,117 | ×0.2^0 = 1,117.0 |
| ▶ | 4¢ | 500 (500 yours) | ×0.2^1 = 100.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **1,618.2** |

`yours 100.0 / Σ 1,618.2 = 6.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.2% = $0.24/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 1 @ 6¢ → $0.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 16 (1 yours) | ×0.2^0 = 16.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 9¢ | 100 | ×0.2^3 = 0.8 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 16¢ | 3 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^91 = 0.0 |
| | | **Σ** | **16.8** |

`yours 1.0 / Σ 16.8 = 5.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.9% = $0.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 10 @ 48¢ → $0.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 47¢ | 30 | ×0.2^0 = 30.0 |
| ▶ | 48¢ | 21 (10 yours) | ×0.2^1 = 4.2 |
|  | 49¢ | 2 | ×0.2^2 = 0.1 |
|  | 52¢ | 133 | ×0.2^5 = 0.0 |
|  | 82¢ | 105 | ×0.2^35 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^51 = 0.0 |
| | | **Σ** | **34.3** |

`yours 2.0 / Σ 34.3 = 5.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.8% = $0.24/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 15 @ 7¢ → $0.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 319 (15 yours) | ×0.2^0 = 319.0 |
|  | 9¢ | 1 | ×0.2^2 = 0.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^91 = 0.0 |
| | | **Σ** | **319.1** |

`yours 15.0 / Σ 319.1 = 4.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.7% = $0.20/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 4 @ 5¢ → $0.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 68 (4 yours) | ×0.2^0 = 68.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 422 | ×0.2^3 = 3.4 |
|  | 1¢ | 25,044 | ×0.2^4 = 40.1 |
| | | **Σ** | **112.8** |

`yours 4.0 / Σ 112.8 = 3.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.5% = $0.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 50 @ 8¢ → $0.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1,666 (50 yours) | ×0.2^0 = 1,666.0 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 45,967 | ×0.2^89 = 0.0 |
| | | **Σ** | **1,666.0** |

`yours 50.0 / Σ 1,666.0 = 3.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.0% = $0.12/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 12 @ 14¢ → $0.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 441 (12 yours) | ×0.2^0 = 441.1 |
|  | 12¢ | 13 | ×0.2^2 = 0.5 |
|  | 8¢ | 100 | ×0.2^6 = 0.0 |
|  | 7¢ | 81 | ×0.2^7 = 0.0 |
|  | 6¢ | 100 | ×0.2^8 = 0.0 |
|  | 3¢ | 5,000 | ×0.2^11 = 0.0 |
| | | **Σ** | **441.7** |

`yours 12.0 / Σ 441.7 = 2.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 2.7% = $0.11/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 10 @ 18¢ → $0.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 15 | ×0.2^0 = 15.0 |
|  | 17¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 18¢ | 11 (10 yours) | ×0.2^2 = 0.4 |
|  | 20¢ | 15 | ×0.2^4 = 0.0 |
|  | 31¢ | 111 | ×0.2^15 = 0.0 |
|  | 40¢ | 30 | ×0.2^24 = 0.0 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^81 = 0.0 |
| | | **Σ** | **15.7** |

`yours 0.4 / Σ 15.7 = 2.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 2.6% = $0.10/day`  

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
<details><summary><code>ewc-usse-oh-2026-11-03-rep</code> BUY 50 @ 48¢ → $0.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 2,340 (50 yours) | ×0.2^0 = 2,340.0 |
|  | 46¢ | 1,060 | ×0.2^2 = 42.4 |
|  | 38¢ | 15,000 | ×0.2^10 = 0.0 |
| | | **Σ** | **2,382.4** |

`yours 50.0 / Σ 2,382.4 = 2.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 2.1% = $0.52/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-oh-2026-11-03-dem`
2. `ewc-usse-oh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 30 @ 35¢ → $0.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 1,483 (30 yours) | ×0.2^0 = 1,483.3 |
|  | 33¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 80,000 | ×0.2^33 = 0.0 |
| | | **Σ** | **1,483.4** |

`yours 30.0 / Σ 1,483.4 = 2.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 2.0% = $0.08/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 100 @ 89¢ → $0.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 7,118 (100 yours) | ×0.2^0 = 7,118.0 |
| | | **Σ** | **7,118.0** |

`yours 100.0 / Σ 7,118.0 = 1.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.4% = $0.06/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-02 | ~$25.55 | $14.05 | 55% |
| 2026-08-01 | ~$46.23 | $52.30 | 113% |
| 2026-07-31 | ~$64.95 | $67.96 | 105% |

Biggest gaps on 2026-08-02: `scc-senate-gop-2026-11-03-47` (est ~$2.48 → got $0.81), `scc-senate-gop-2026-11-03-51` (est ~$2.03 → got $0.48), `scc-senate-gop-2026-11-03-53` (est ~$1.30 → got $0.13)

_2026-08-03 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (85,287 resting) | ~64.3% | ~$16.07 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (65,982 resting) | ~19.3% | ~$14.44 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,637 resting) | ~50.8% | ~$12.69 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,989 resting) | ~44.3% | ~$11.09 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,066 resting) | ~39.2% | ~$9.80 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (323,668 resting) | ~12.1% | ~$9.10 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (181,614 resting) | ~6.6% | ~$4.96 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (73,027 resting) | ~6.0% | ~$4.49 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (87,037 resting) | ~5.6% | ~$4.21 |
| `ewc-usse-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (90,186 resting) | ~3.8% | ~$2.87 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (236,660 resting) | ~3.3% | ~$2.45 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (81,819 resting) | ~2.5% | ~$1.89 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,514.21 |
| Pending | $58.86 |
| Skipped | $1.21 |
| **Total earned** | **$1,574.28** |

1611 reward rows · 32 days with rewards · 362 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-03 ⚠️ multi-day pending bucket | $44.81 | `████` |
| 2026-08-02 | $14.05 | `█` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $111.16 | `██` |
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `apdc-jerpowgov-2026-12-31` | $42.68 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-alito-2026-12-31` | $37.56 |
| `opdc-mcconnell-resign-2026-11-02` | $35.08 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-05 2:45 AM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-04 11:39 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-04 10:37 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-04 10:16 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-04 9:14 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-04 9:08 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-04 9:03 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 9:02 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 8:17 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 6:31 PM ET | ✅ ok | 1573 | $1529.47 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
