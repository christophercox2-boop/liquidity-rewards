# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-05 9:26 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$35.24/day estimated (ceiling, not promise — details below)

**Earned:** $1,628.42 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-04: **$53.94** · 2026-08-03: **$44.81** · 2026-08-02: **$14.05** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-angcra` — SELL at the best price, ~$22.83/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$14.91/day), `ewc-usse-tx-2026-11-03-rep` (~$12.69/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$35.24/day (~$1.47/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (200,498 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 14.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (35,607 resting ≥ 2,000 ✓) ≈ $12.50/day |
| `scc-senate-gop-2026-11-03-53` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~90.9% of ask side (113,452 resting ≥ 5,000 ✓) ≈ $3.50/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 20.0¢ | 80 | 0 | $100.00 | ✅ scoring — ~62.0% of bid side (80,279 resting ≥ 5,000 ✓) ≈ $2.58/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 86.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~58.7% of bid side (50,468 resting ≥ 5,000 ✓) ≈ $2.45/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~32.9% of ask side (100,586 resting ≥ 5,000 ✓) ≈ $1.27/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 28 | 0 | $100.00 | ✅ scoring — ~31.9% of ask side (112,810 resting ≥ 5,000 ✓) ≈ $1.23/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 19.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~30.7% of bid side (102,697 resting ≥ 5,000 ✓) ≈ $1.18/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~29.6% of ask side (48,686 resting ≥ 5,000 ✓) ≈ $1.23/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~25.6% of bid side (80,500 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~25.6% of bid side (80,500 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~22.5% of bid side (3,974 resting ≥ 2,500 ✓) ≈ $0.77/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 15.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~12.4% of ask side (49,703 resting ≥ 5,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 88.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~10.7% of ask side (62,719 resting ≥ 5,000 ✓) ≈ $0.45/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~9.1% of bid side (80,608 resting ≥ 5,000 ✓) ≈ $0.38/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 99.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~7.7% of bid side (110,261 resting ≥ 2,000 ✓) ≈ $0.10/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 35.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~5.2% of bid side (80,781 resting ≥ 5,000 ✓) ≈ $0.22/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 6.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~5.1% of ask side (113,625 resting ≥ 5,000 ✓) ≈ $0.19/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~4.1% of ask side (48,089 resting ≥ 5,000 ✓) ≈ $0.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 5.0¢ | 133 | 0 | $100.00 | ✅ scoring — ~4.0% of bid side (53,154 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-mst` | BUY | 7.0¢ | 5 | 0 | $500.00 | ✅ scoring — ~1.8% of bid side (103,468 resting ≥ 2,500 ✓) ≈ $0.06/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~1.7% of ask side (117,835 resting ≥ 5,000 ✓) ≈ $0.07/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 30.0¢ | 42 | 2 | $100.00 | ✅ scoring — ~1.5% of ask side (98,797 resting ≥ 5,000 ✓) ≈ $0.06/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 15.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~1.0% of bid side (50,628 resting ≥ 5,000 ✓) ≈ $0.04/day (pool ÷ 13 markets) |
| `ewc-usse-oh-2026-11-03-rep` | BUY | 48.0¢ | 32 | 0 | $100.00 | ✅ scoring — ~0.6% of bid side (65,956 resting ≥ 5,000 ✓) ≈ $0.14/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 48.0¢ | 11 | 3 | $100.00 | ✅ scoring — ~0.2% of bid side (80,500 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 45 | 0 | $100.00 | ✅ scoring — ~0.1% of bid side (49,678 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 13 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 1.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~0.0% of ask side (282,443 resting ≥ 2,000 ✓) ≈ $0.00/day (pool ÷ 6 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 86.0¢ | 6 | 0 | $100.00 | ✅ scoring — ~0.0% of ask side (21,667 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 99.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~0.0% of ask side (42,124 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 12 markets) |
| …and 5 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 15 @ 18¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 6¢ | 2 | ×0.2^12 = 0.0 |
|  | 5¢ | 50 | ×0.2^13 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^17 = 0.0 |
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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 20 @ 14¢ → $12.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 20 (20 yours) | ×0.1^0 = 20.0 |
|  | 11¢ | 1 | ×0.1^3 = 0.0 |
|  | 6¢ | 30 | ×0.1^8 = 0.0 |
|  | 4¢ | 6 | ×0.1^10 = 0.0 |
|  | 1¢ | 35,550 | ×0.1^13 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 100.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 100.0% = $12.50/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 10 @ 20¢ → $3.50/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 11 (10 yours) | ×0.2^0 = 11.0 |
|  | 50¢ | 39 | ×0.2^30 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^77 = 0.0 |
| | | **Σ** | **11.0** |

`yours 10.0 / Σ 11.0 = 90.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 90.9% = $3.50/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 80 @ 20¢ → $2.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 129 (80 yours) | ×0.2^0 = 129.0 |
|  | 6¢ | 10 | ×0.2^14 = 0.0 |
|  | 2¢ | 79,940 | ×0.2^18 = 0.0 |
| | | **Σ** | **129.0** |

`yours 80.0 / Σ 129.0 = 62.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 62.0% = $2.58/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 86¢ → $2.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 86¢ | 17 (10 yours) | ×0.2^0 = 17.0 |
|  | 84¢ | 1 | ×0.2^2 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^84 = 0.0 |
| | | **Σ** | **17.0** |

`yours 10.0 / Σ 17.0 = 58.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 58.7% = $2.45/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 20¢ → $1.27/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 14 (10 yours) | ×0.2^0 = 14.0 |
|  | 22¢ | 20 | ×0.2^2 = 0.8 |
|  | 23¢ | 1,946 | ×0.2^3 = 15.6 |
|  | 47¢ | 99 | ×0.2^27 = 0.0 |
|  | 50¢ | 99 | ×0.2^30 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^77 = 0.0 |
| | | **Σ** | **30.4** |

`yours 10.0 / Σ 30.4 = 32.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.9% = $1.27/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 28 @ 22¢ → $1.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 88 (28 yours) | ×0.2^0 = 88.1 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 97¢ | 58,044 | ×0.2^75 = 0.0 |
| | | **Σ** | **88.1** |

`yours 28.1 / Σ 88.1 = 31.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.9% = $1.23/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 20 @ 19¢ → $1.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 54 (20 yours) | ×0.2^0 = 54.0 |
|  | 16¢ | 1,116 | ×0.2^3 = 8.9 |
|  | 15¢ | 1,327 | ×0.2^4 = 2.1 |
|  | 2¢ | 100,000 | ×0.2^17 = 0.0 |
| | | **Σ** | **65.1** |

`yours 20.0 / Σ 65.1 = 30.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.7% = $1.18/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 8 @ 48¢ → $1.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 27 (8 yours) | ×0.2^0 = 27.0 |
|  | 82¢ | 5 | ×0.2^34 = 0.0 |
|  | 83¢ | 954 | ×0.2^35 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **27.0** |

`yours 8.0 / Σ 27.0 = 29.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 29.6% = $1.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $1.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 39 (10 yours) | ×0.2^0 = 39.0 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **39.1** |

`yours 10.0 / Σ 39.1 = 25.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 25.6% = $1.07/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $1.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 39 (10 yours) | ×0.2^0 = 39.0 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **39.1** |

`yours 10.0 / Σ 39.1 = 25.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 25.6% = $1.07/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 250 | ×0.35^0 = 250.0 |
| ▶ | 1¢ | 3,724 (1,000 yours) | ×0.35^1 = 1,303.4 |
| | | **Σ** | **1,553.4** |

`yours 350.0 / Σ 1,553.4 = 22.5%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 22.5% = $0.77/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 10 @ 15¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 46 (10 yours) | ×0.2^0 = 46.0 |
|  | 16¢ | 173 | ×0.2^1 = 34.6 |
|  | 50¢ | 25 | ×0.2^35 = 0.0 |
|  | 97¢ | 1,759 | ×0.2^82 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^83 = 0.0 |
| | | **Σ** | **80.6** |

`yours 10.0 / Σ 80.6 = 12.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 12.4% = $0.52/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 10 @ 88¢ → $0.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 93 (10 yours) | ×0.2^0 = 93.0 |
|  | 93¢ | 137 | ×0.2^5 = 0.0 |
|  | 98¢ | 60,376 | ×0.2^10 = 0.0 |
| | | **Σ** | **93.1** |

`yours 10.0 / Σ 93.1 = 10.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 10.7% = $0.45/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 10 @ 10¢ → $0.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 110 (10 yours) | ×0.2^0 = 110.0 |
|  | 1¢ | 80,498 | ×0.2^9 = 0.0 |
| | | **Σ** | **110.0** |

`yours 10.0 / Σ 110.0 = 9.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 9.1% = $0.38/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 20 @ 99¢ → $0.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 261 (20 yours) | ×0.1^0 = 261.4 |
|  | 18¢ | 3,000 | ×0.1^81 = 0.0 |
| | | **Σ** | **261.4** |

`yours 20.0 / Σ 261.4 = 7.7%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 7.7% = $0.10/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5` ← this one
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 30 @ 35¢ → $0.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 581 (30 yours) | ×0.2^0 = 581.3 |
|  | 2¢ | 80,000 | ×0.2^33 = 0.0 |
| | | **Σ** | **581.3** |

`yours 30.0 / Σ 581.3 = 5.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.2% = $0.22/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 1 @ 6¢ → $0.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 19 (1 yours) | ×0.2^0 = 19.0 |
|  | 9¢ | 100 | ×0.2^3 = 0.8 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 16¢ | 3 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^91 = 0.0 |
| | | **Σ** | **19.8** |

`yours 1.0 / Σ 19.8 = 5.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.1% = $0.19/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 15 @ 7¢ → $0.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 363 (15 yours) | ×0.2^0 = 363.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^91 = 0.0 |
| | | **Σ** | **363.0** |

`yours 15.0 / Σ 363.0 = 4.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.1% = $0.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 133 @ 5¢ → $0.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 2,949 (133 yours) | ×0.2^0 = 2,949.0 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **3,348.8** |

`yours 133.0 / Σ 3,348.8 = 4.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 4.0% = $0.15/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-mst</code> BUY 5 @ 7¢ → $0.06/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 68 (5 yours) | ×0.35^0 = 68.0 |
|  | 4¢ | 500 | ×0.35^3 = 21.4 |
|  | 1¢ | 102,900 | ×0.35^6 = 189.2 |
| | | **Σ** | **278.5** |

`yours 5.0 / Σ 278.5 = 1.8%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 1.8% = $0.06/day`  

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
36. `tec-cbb-champ-2027-04-05-w-mst` ← this one
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 1 @ 4¢ → $0.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 56 (1 yours) | ×0.2^0 = 56.0 |
|  | 5¢ | 14 | ×0.2^1 = 2.8 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **58.8** |

`yours 1.0 / Σ 58.8 = 1.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.7% = $0.07/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 42 @ 30¢ → $0.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 28¢ | 113 | ×0.2^0 = 113.0 |
| ▶ | 30¢ | 42 (42 yours) | ×0.2^2 = 1.7 |
|  | 45¢ | 137 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 97¢ | 43,826 | ×0.2^69 = 0.0 |
| | | **Σ** | **114.7** |

`yours 1.7 / Σ 114.7 = 1.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.5% = $0.06/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 10 @ 15¢ → $0.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 159 | ×0.2^0 = 159.0 |
| ▶ | 15¢ | 157 (10 yours) | ×0.2^1 = 31.5 |
|  | 14¢ | 112 | ×0.2^2 = 4.5 |
|  | 2¢ | 50,000 | ×0.2^14 = 0.0 |
| | | **Σ** | **194.9** |

`yours 2.0 / Σ 194.9 = 1.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.0% = $0.04/day`  

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
<details><summary><code>ewc-usse-oh-2026-11-03-rep</code> BUY 32 @ 48¢ → $0.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 4,549 (32 yours) | ×0.2^0 = 4,549.0 |
|  | 47¢ | 5,587 | ×0.2^1 = 1,117.4 |
| | | **Σ** | **5,666.4** |

`yours 32.0 / Σ 5,666.4 = 0.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 0.6% = $0.14/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-oh-2026-11-03-dem`
2. `ewc-usse-oh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 11 @ 48¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 51¢ | 39 | ×0.2^0 = 39.0 |
| ▶ | 48¢ | 11 (11 yours) | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **39.1** |

`yours 0.1 / Σ 39.1 = 0.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.2% = $0.01/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 45 @ 3¢ → $0.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 39,478 (45 yours) | ×0.2^0 = 39,478.0 |
| | | **Σ** | **39,478.0** |

`yours 45.0 / Σ 39,478.0 = 0.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.1% = $0.00/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-sarrod</code> SELL 100 @ 1¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 281,443 (100 yours) | ×0.1^0 = 281,443.0 |
| | | **Σ** | **281,443.0** |

`yours 100.0 / Σ 281,443.0 = 0.0%`  
`$25 ÷ 6 ÷ 2 = $2.08 × 0.0% = $0.00/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 6 @ 86¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 86¢ | 19,453 (6 yours) | ×0.2^0 = 19,453.0 |
| | | **Σ** | **19,453.0** |

`yours 6.0 / Σ 19,453.0 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 1 @ 99¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 42,124 (1 yours) | ×0.2^0 = 42,123.7 |
| | | **Σ** | **42,123.7** |

`yours 1.0 / Σ 42,123.7 = 0.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 0.0% = $0.00/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-04 | ~$58.23 | $53.94 | 93% |
| 2026-08-03 | ~$56.69 | $44.81 | 79% |
| 2026-08-02 | ~$25.55 | $14.05 | 55% |

Biggest gaps on 2026-08-04: `scc-senate-gop-2026-11-03-53` (est ~$2.46 → got $0.70), `scc-hrep-rep-2026-11-03-gte210` (est ~$1.72 → got $0.30), `scc-senate-gop-2026-11-03-52` (est ~$1.77 → got $0.36)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,505 resting) | ~91.3% | ~$22.83 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (10,509 resting) | ~59.7% | ~$14.91 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (276,285 resting) | ~16.9% | ~$12.69 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,997 resting) | ~43.6% | ~$10.90 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,522 resting) | ~39.3% | ~$9.82 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (66,557 resting) | ~6.3% | ~$4.74 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (185,718 resting) | ~5.9% | ~$4.44 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (104,267 resting) | ~4.3% | ~$3.26 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (232,393 resting) | ~18.6% | ~$3.11 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (79,527 resting) | ~3.5% | ~$2.64 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (68,284 resting) | ~3.4% | ~$2.58 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (134,731 resting) | ~40.2% | ~$2.51 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,514.21 |
| Pending | $113.00 |
| Skipped | $1.21 |
| **Total earned** | **$1,628.42** |

1648 reward rows · 33 days with rewards · 362 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-04 | $53.94 | `█████` |
| 2026-08-03 | $44.81 | `████` |
| 2026-08-02 | $14.05 | `█` |
| 2026-08-01 | $52.30 | `█████` |
| 2026-07-31 | $67.96 | `██████` |
| 2026-07-30 | $20.67 | `██` |
| 2026-07-29 | $53.60 | `█████` |
| 2026-07-28 | $79.65 | `███████` |
| 2026-07-27 | $125.34 | `███████████` |
| 2026-07-26 | $153.80 | `██████████████` |
| 2026-07-25 | $125.69 | `███████████` |
| 2026-07-24 | $135.19 | `████████████` |
| 2026-07-23 | $227.63 | `████████████████████` |
| 2026-07-22 | $82.95 | `███████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $165.10 | `██` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `apdc-alito-2026-12-31` | $61.51 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `apdc-jerpowgov-2026-12-31` | $42.68 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `opdc-mcconnell-resign-2026-11-02` | $39.45 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
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
| 2026-08-05 9:26 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:22 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:14 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:06 PM ET | ✅ ok | 1640 | $1624.44 |
| 2026-08-05 9:04 PM ET | ✅ ok | 1613 | $1574.48 |
| 2026-08-05 8:52 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-05 8:13 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-05 6:29 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-05 4:40 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-05 2:56 PM ET | ✅ ok | 1611 | $1574.28 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
