# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-04 4:46 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$40.75/day estimated (ceiling, not promise — details below)

**Earned:** $1,529.47 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-02: **$14.05** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-01: **$52.30** · 2026-07-31: **$67.96** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-xavbec` — BUY at the best price, ~$23.68/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$15.13/day), `ewc-usgub-oh-2026-11-03-dem` (~$14.35/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$40.75/day (~$1.70/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-47` | BUY | 14.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~97.3% of bid side (5,477 resting ≥ 5,000 ✓) ≈ $3.74/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 20.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~93.5% of ask side (12,276 resting ≥ 5,000 ✓) ≈ $3.59/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 24.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~91.2% of bid side (5,522 resting ≥ 5,000 ✓) ≈ $3.51/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 8.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~67.9% of bid side (25,470 resting ≥ 5,000 ✓) ≈ $2.61/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~59.7% of ask side (12,070 resting ≥ 5,000 ✓) ≈ $2.30/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 28 | 0 | $100.00 | ✅ scoring — ~46.6% of ask side (12,145 resting ≥ 5,000 ✓) ≈ $1.79/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~37.9% of ask side (8,140 resting ≥ 5,000 ✓) ≈ $9.47/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~27.2% of bid side (80,318 resting ≥ 5,000 ✓) ≈ $1.13/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 7.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~25.8% of ask side (117,073 resting ≥ 5,000 ✓) ≈ $0.99/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 61.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~23.9% of ask side (62,945 resting ≥ 5,000 ✓) ≈ $1.00/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 25.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~23.2% of ask side (12,116 resting ≥ 5,000 ✓) ≈ $0.89/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~21.9% of bid side (4,009 resting ≥ 2,500 ✓) ≈ $0.75/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 8.0¢ | 44 | 0 | $100.00 | ✅ scoring — ~20.8% of bid side (21,148 resting ≥ 5,000 ✓) ≈ $0.80/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 13.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~18.6% of bid side (87,894 resting ≥ 5,000 ✓) ≈ $0.77/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 15.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~16.0% of ask side (62,929 resting ≥ 5,000 ✓) ≈ $0.67/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 61.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~11.5% of ask side (62,945 resting ≥ 5,000 ✓) ≈ $0.48/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 12 | 0 | $100.00 | ✅ scoring — ~11.3% of ask side (63,019 resting ≥ 5,000 ✓) ≈ $0.47/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~9.4% of ask side (63,019 resting ≥ 5,000 ✓) ≈ $0.39/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 2.0¢ | 5,000 | 2 | $100.00 | ✅ scoring — ~7.6% of bid side (55,721 resting ≥ 5,000 ✓) ≈ $0.29/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~7.2% of bid side (84,002 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 5.0¢ | 133 | 0 | $100.00 | ✅ scoring — ~7.2% of bid side (52,055 resting ≥ 5,000 ✓) ≈ $0.28/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 18.0¢ | 35 | 0 | $100.00 | ✅ scoring — ~7.0% of bid side (200,698 resting ≥ 5,000 ✓) ≈ $0.29/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | SELL | 21.0¢ | 80 | 1 | $100.00 | ✅ scoring — ~6.1% of ask side (8,140 resting ≥ 5,000 ✓) ≈ $1.52/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 30 | 3 | $100.00 | ✅ scoring — ~5.9% of ask side (62,837 resting ≥ 5,000 ✓) ≈ $0.24/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 1 | $100.00 | ✅ scoring — ~5.4% of bid side (52,055 resting ≥ 5,000 ✓) ≈ $0.21/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 20.0¢ | 16 | 0 | $100.00 | ✅ scoring — ~4.7% of ask side (48,034 resting ≥ 5,000 ✓) ≈ $0.20/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~3.8% of bid side (23,309 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~2.8% of ask side (48,270 resting ≥ 5,000 ✓) ≈ $0.11/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 7.0¢ | 400 | 3 | $100.00 | ✅ scoring — ~2.3% of bid side (84,002 resting ≥ 5,000 ✓) ≈ $0.10/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 5.0¢ | 590 | 3 | $100.00 | ✅ scoring — ~2.2% of bid side (21,148 resting ≥ 5,000 ✓) ≈ $0.09/day (pool ÷ 13 markets) |
| …and 44 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 15 @ 14¢ → $3.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 12¢ | 10 | ×0.2^2 = 0.4 |
|  | 6¢ | 32 | ×0.2^8 = 0.0 |
|  | 1¢ | 5,420 | ×0.2^13 = 0.0 |
| | | **Σ** | **15.4** |

`yours 15.0 / Σ 15.4 = 97.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 97.3% = $3.74/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 15 @ 20¢ → $3.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 16 (15 yours) | ×0.2^0 = 16.0 |
|  | 22¢ | 1 | ×0.2^2 = 0.1 |
|  | 31¢ | 111 | ×0.2^11 = 0.0 |
|  | 40¢ | 30 | ×0.2^20 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,817 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^79 = 0.0 |
| | | **Σ** | **16.1** |

`yours 15.0 / Σ 16.1 = 93.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 93.5% = $3.59/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 1 @ 24¢ → $3.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 21¢ | 12 | ×0.2^3 = 0.1 |
|  | 1¢ | 5,509 | ×0.2^23 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 91.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 91.2% = $3.51/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 3 @ 8¢ → $2.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 4 (3 yours) | ×0.2^0 = 4.1 |
|  | 2¢ | 232 | ×0.2^6 = 0.0 |
|  | 1¢ | 25,234 | ×0.2^7 = 0.3 |
| | | **Σ** | **4.4** |

`yours 3.0 / Σ 4.4 = 67.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.9% = $2.61/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 15 @ 18¢ → $2.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 25 (15 yours) | ×0.2^0 = 25.0 |
|  | 20¢ | 3 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 98¢ | 1,741 | ×0.2^80 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^81 = 0.0 |
| | | **Σ** | **25.1** |

`yours 15.0 / Σ 25.1 = 59.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 59.7% = $2.30/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 28 @ 22¢ → $1.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 60 (28 yours) | ×0.2^0 = 60.1 |
|  | 24¢ | 4 | ×0.2^2 = 0.2 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 98¢ | 1,780 | ×0.2^76 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^77 = 0.0 |
| | | **Σ** | **60.3** |

`yours 28.1 / Σ 60.3 = 46.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 46.6% = $1.79/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 20¢ → $9.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 145 (100 yours) | ×0.2^0 = 145.0 |
|  | 21¢ | 165 | ×0.2^1 = 33.0 |
|  | 22¢ | 2,148 | ×0.2^2 = 85.9 |
|  | 48¢ | 105 | ×0.2^28 = 0.0 |
|  | 99¢ | 5,576 | ×0.2^79 = 0.0 |
| | | **Σ** | **264.0** |

`yours 100.0 / Σ 264.0 = 37.9%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 37.9% = $9.47/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 30 @ 85¢ → $1.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 110 (30 yours) | ×0.2^0 = 110.2 |
|  | 83¢ | 0 | ×0.2^2 = 0.0 |
|  | 2¢ | 80,008 | ×0.2^83 = 0.0 |
| | | **Σ** | **110.2** |

`yours 30.0 / Σ 110.2 = 27.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 27.2% = $1.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 31 @ 7¢ → $0.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 120 (31 yours) | ×0.2^0 = 120.2 |
|  | 9¢ | 2 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^43 = 0.0 |
|  | 97¢ | 60,152 | ×0.2^90 = 0.0 |
| | | **Σ** | **120.3** |

`yours 31.0 / Σ 120.3 = 25.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.8% = $0.99/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 10 @ 61¢ → $1.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 61¢ | 42 (10 yours) | ×0.2^0 = 41.8 |
|  | 63¢ | 0 | ×0.2^2 = 0.0 |
|  | 67¢ | 1 | ×0.2^6 = 0.0 |
|  | 71¢ | 200 | ×0.2^10 = 0.0 |
|  | 90¢ | 1 | ×0.2^29 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^37 = 0.0 |
| | | **Σ** | **41.8** |

`yours 10.0 / Σ 41.8 = 23.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 23.9% = $1.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 8 @ 25¢ → $0.89/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 34 (8 yours) | ×0.2^0 = 33.9 |
|  | 27¢ | 3 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^25 = 0.0 |
|  | 98¢ | 1,778 | ×0.2^73 = 0.0 |
|  | 99¢ | 10,201 | ×0.2^74 = 0.0 |
| | | **Σ** | **34.0** |

`yours 7.9 / Σ 34.0 = 23.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 23.2% = $0.89/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 300 | ×0.35^0 = 300.0 |
| ▶ | 1¢ | 3,709 (1,000 yours) | ×0.35^1 = 1,298.1 |
| | | **Σ** | **1,598.1** |

`yours 350.0 / Σ 1,598.1 = 21.9%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 21.9% = $0.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 44 @ 8¢ → $0.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 44 (44 yours) | ×0.2^0 = 44.0 |
|  | 6¢ | 17 | ×0.2^2 = 0.7 |
|  | 5¢ | 20,839 | ×0.2^3 = 166.7 |
| | | **Σ** | **211.4** |

`yours 44.0 / Σ 211.4 = 20.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.8% = $0.80/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 30 @ 13¢ → $0.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 160 (30 yours) | ×0.2^0 = 160.4 |
|  | 12¢ | 5 | ×0.2^1 = 1.0 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 8¢ | 100 | ×0.2^5 = 0.0 |
|  | 7¢ | 81 | ×0.2^6 = 0.0 |
|  | 6¢ | 100 | ×0.2^7 = 0.0 |
|  | 3¢ | 5,247 | ×0.2^10 = 0.0 |
| | | **Σ** | **161.5** |

`yours 30.0 / Σ 161.5 = 18.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.6% = $0.77/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 10 @ 15¢ → $0.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 27 (10 yours) | ×0.2^0 = 27.0 |
|  | 16¢ | 177 | ×0.2^1 = 35.4 |
|  | 17¢ | 0 | ×0.2^2 = 0.0 |
|  | 50¢ | 25 | ×0.2^35 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^83 = 0.0 |
| | | **Σ** | **62.4** |

`yours 10.0 / Σ 62.4 = 16.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.0% = $0.67/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 5 @ 61¢ → $0.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 61¢ | 42 (5 yours) | ×0.2^0 = 41.8 |
|  | 63¢ | 0 | ×0.2^2 = 0.0 |
|  | 67¢ | 1 | ×0.2^6 = 0.0 |
|  | 71¢ | 200 | ×0.2^10 = 0.0 |
|  | 90¢ | 1 | ×0.2^29 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^37 = 0.0 |
| | | **Σ** | **41.8** |

`yours 4.8 / Σ 41.8 = 11.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.5% = $0.48/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 12 @ 48¢ → $0.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 106 (12 yours) | ×0.2^0 = 106.0 |
|  | 50¢ | 0 | ×0.2^2 = 0.0 |
|  | 55¢ | 107 | ×0.2^7 = 0.0 |
|  | 82¢ | 105 | ×0.2^34 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **106.0** |

`yours 12.0 / Σ 106.0 = 11.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.3% = $0.47/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 10 @ 48¢ → $0.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 106 (10 yours) | ×0.2^0 = 106.0 |
|  | 50¢ | 0 | ×0.2^2 = 0.0 |
|  | 55¢ | 107 | ×0.2^7 = 0.0 |
|  | 82¢ | 105 | ×0.2^34 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **106.0** |

`yours 10.0 / Σ 106.0 = 9.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 9.4% = $0.39/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 5,000 @ 2¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 413 | ×0.2^0 = 413.0 |
| ▶ | 2¢ | 55,108 (5,000 yours) | ×0.2^2 = 2,204.3 |
| | | **Σ** | **2,617.3** |

`yours 200.0 / Σ 2,617.3 = 7.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.6% = $0.29/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 10 @ 10¢ → $0.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 110 (10 yours) | ×0.2^0 = 110.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.1 |
|  | 7¢ | 3,507 | ×0.2^3 = 28.1 |
|  | 1¢ | 80,383 | ×0.2^9 = 0.0 |
| | | **Σ** | **138.1** |

`yours 10.0 / Σ 138.1 = 7.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.2% = $0.30/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 133 @ 5¢ → $0.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1,342 (133 yours) | ×0.2^0 = 1,342.0 |
|  | 4¢ | 500 | ×0.2^1 = 100.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **1,843.2** |

`yours 133.0 / Σ 1,843.2 = 7.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.2% = $0.28/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 35 @ 18¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 497 (35 yours) | ×0.2^0 = 496.9 |
|  | 16¢ | 1 | ×0.2^2 = 0.0 |
|  | 1¢ | 200,200 | ×0.2^17 = 0.0 |
| | | **Σ** | **496.9** |

`yours 35.0 / Σ 496.9 = 7.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.0% = $0.29/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 80 @ 21¢ → $1.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 145 | ×0.2^0 = 145.0 |
| ▶ | 21¢ | 165 (80 yours) | ×0.2^1 = 33.0 |
|  | 22¢ | 2,148 | ×0.2^2 = 85.9 |
|  | 48¢ | 105 | ×0.2^28 = 0.0 |
|  | 99¢ | 5,576 | ×0.2^79 = 0.0 |
| | | **Σ** | **264.0** |

`yours 16.0 / Σ 264.0 = 6.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 6.1% = $1.52/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 30 @ 47¢ → $0.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 44¢ | 4 | ×0.2^0 = 3.8 |
|  | 46¢ | 2 | ×0.2^2 = 0.1 |
| ▶ | 47¢ | 30 (30 yours) | ×0.2^3 = 0.2 |
|  | 52¢ | 1 | ×0.2^8 = 0.0 |
|  | 69¢ | 100 | ×0.2^25 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^54 = 0.0 |
| | | **Σ** | **4.1** |

`yours 0.2 / Σ 4.1 = 5.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.9% = $0.24/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $0.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 1,342 | ×0.2^0 = 1,342.0 |
| ▶ | 4¢ | 500 (500 yours) | ×0.2^1 = 100.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **1,843.2** |

`yours 100.0 / Σ 1,843.2 = 5.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.4% = $0.21/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 16 @ 20¢ → $0.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 334 (16 yours) | ×0.2^0 = 333.9 |
|  | 22¢ | 0 | ×0.2^2 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^78 = 0.0 |
| | | **Σ** | **333.9** |

`yours 15.7 / Σ 333.9 = 4.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.7% = $0.20/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 13,109 (500 yours) | ×0.2^0 = 13,109.0 |
| | | **Σ** | **13,109.0** |

`yours 500.0 / Σ 13,109.0 = 3.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.8% = $0.15/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 15 @ 7¢ → $0.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 544 (15 yours) | ×0.2^0 = 544.0 |
|  | 9¢ | 0 | ×0.2^2 = 0.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^91 = 0.0 |
| | | **Σ** | **544.0** |

`yours 15.0 / Σ 544.0 = 2.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 2.8% = $0.11/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 400 @ 7¢ → $0.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 110 | ×0.2^0 = 110.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.1 |
| ▶ | 7¢ | 3,507 (400 yours) | ×0.2^3 = 28.1 |
|  | 1¢ | 80,383 | ×0.2^9 = 0.0 |
| | | **Σ** | **138.1** |

`yours 3.2 / Σ 138.1 = 2.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 2.3% = $0.10/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 590 @ 5¢ → $0.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 44 | ×0.2^0 = 44.0 |
|  | 6¢ | 17 | ×0.2^2 = 0.7 |
| ▶ | 5¢ | 20,839 (590 yours) | ×0.2^3 = 166.7 |
| | | **Σ** | **211.4** |

`yours 4.7 / Σ 211.4 = 2.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 2.2% = $0.09/day`  

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
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (323,540 resting) | ~31.6% | ~$23.68 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (25,635 resting) | ~60.5% | ~$15.13 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (44,583 resting) | ~19.1% | ~$14.35 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (235,414 resting) | ~7.6% | ~$5.69 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (180,338 resting) | ~7.2% | ~$5.36 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,254 resting) | ~20.8% | ~$5.19 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (88,053 resting) | ~10.6% | ~$2.65 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (59,268 resting) | ~2.8% | ~$2.11 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (91,857 resting) | ~2.4% | ~$1.83 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (189,246 resting) | ~2.3% | ~$1.73 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (96,473 resting) | ~1.7% | ~$1.31 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (43,214 resting) | ~20.5% | ~$1.28 |

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
| 2026-08-04 4:46 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 2:57 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 1:06 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 10:45 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 8:21 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 6:01 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 2:43 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 11:42 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 10:10 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 9:31 PM ET | ✅ ok | 1573 | $1529.47 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
