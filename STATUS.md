# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-05 9:54 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$49.57/day estimated (ceiling, not promise — details below)

**Earned:** $1,628.42 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-04: **$53.94** · 2026-08-03: **$44.81** · 2026-08-02: **$14.05** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — BUY at the best price, ~$22.72/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-12-31` (~$22.13/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$10.76/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$49.57/day (~$2.07/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | BUY | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (200,610 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 14.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (35,607 resting ≥ 2,000 ✓) ≈ $12.50/day |
| `scc-senate-gop-2026-11-03-53` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~62.5% of ask side (113,457 resting ≥ 5,000 ✓) ≈ $2.40/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 20.0¢ | 80 | 0 | $100.00 | ✅ scoring — ~62.0% of bid side (80,429 resting ≥ 5,000 ✓) ≈ $2.58/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 86.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~58.7% of bid side (50,468 resting ≥ 5,000 ✓) ≈ $2.45/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | SELL | 83.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~39.1% of ask side (7,481 resting ≥ 5,000 ✓) ≈ $1.63/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~29.6% of ask side (48,682 resting ≥ 5,000 ✓) ≈ $1.23/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 28 | 0 | $100.00 | ✅ scoring — ~25.8% of ask side (112,831 resting ≥ 5,000 ✓) ≈ $0.99/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~25.3% of ask side (100,598 resting ≥ 5,000 ✓) ≈ $0.97/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~22.5% of bid side (3,974 resting ≥ 2,500 ✓) ≈ $0.77/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~18.8% of bid side (80,514 resting ≥ 5,000 ✓) ≈ $0.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 51.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~18.8% of bid side (80,514 resting ≥ 5,000 ✓) ≈ $0.78/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 19.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~15.9% of bid side (102,717 resting ≥ 5,000 ✓) ≈ $0.61/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 15.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~13.3% of ask side (49,697 resting ≥ 5,000 ✓) ≈ $0.55/day (pool ÷ 12 markets) |
| `ewc-usgub-ca-2026-11-03-stehil` | BUY | 4.0¢ | 500 | 0 | $300.00 | ✅ scoring — ~12.2% of bid side (104,746 resting ≥ 10,000 ✓) ≈ $9.18/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 88.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~10.7% of ask side (62,706 resting ≥ 5,000 ✓) ≈ $0.45/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | SELL | 19.0¢ | 126 | 0 | $100.00 | ✅ scoring — ~9.7% of ask side (7,174 resting ≥ 5,000 ✓) ≈ $2.43/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~9.1% of bid side (80,608 resting ≥ 5,000 ✓) ≈ $0.38/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 6.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~7.8% of ask side (113,618 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 99.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~7.7% of bid side (110,261 resting ≥ 2,000 ✓) ≈ $0.10/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 8.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~7.3% of ask side (100,973 resting ≥ 5,000 ✓) ≈ $0.28/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~6.7% of ask side (48,101 resting ≥ 5,000 ✓) ≈ $0.28/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | BUY | 18.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~6.5% of bid side (7,294 resting ≥ 5,000 ✓) ≈ $1.62/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 6.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~6.4% of ask side (100,288 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 4 | $100.00 | ✅ scoring — ~6.1% of bid side (25,554 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 35.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~5.2% of bid side (80,781 resting ≥ 5,000 ✓) ≈ $0.22/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 5.0¢ | 133 | 0 | $100.00 | ✅ scoring — ~4.0% of bid side (53,131 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-mst` | BUY | 7.0¢ | 5 | 0 | $500.00 | ✅ scoring — ~1.8% of bid side (103,468 resting ≥ 2,500 ✓) ≈ $0.06/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~1.6% of ask side (117,839 resting ≥ 5,000 ✓) ≈ $0.06/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 30.0¢ | 42 | 2 | $100.00 | ✅ scoring — ~1.5% of ask side (98,739 resting ≥ 5,000 ✓) ≈ $0.06/day (pool ÷ 13 markets) |
| …and 19 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 15 @ 18¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 15 (15 yours) | ×0.2^0 = 15.0 |
|  | 6¢ | 2 | ×0.2^12 = 0.0 |
|  | 5¢ | 50 | ×0.2^13 = 0.0 |
|  | 3¢ | 111 | ×0.2^15 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 10 @ 20¢ → $2.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 16 (10 yours) | ×0.2^0 = 16.0 |
|  | 50¢ | 39 | ×0.2^30 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^77 = 0.0 |
| | | **Σ** | **16.0** |

`yours 10.0 / Σ 16.0 = 62.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 62.5% = $2.40/day`  

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
|  | 10¢ | 150 | ×0.2^10 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> SELL 3 @ 83¢ → $1.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 83¢ | 3 (3 yours) | ×0.2^0 = 3.0 |
|  | 84¢ | 4 | ×0.2^1 = 0.8 |
|  | 85¢ | 92 | ×0.2^2 = 3.7 |
|  | 87¢ | 138 | ×0.2^4 = 0.2 |
|  | 99¢ | 7,244 | ×0.2^16 = 0.0 |
| | | **Σ** | **7.7** |

`yours 3.0 / Σ 7.7 = 39.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 39.1% = $1.63/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 8 @ 48¢ → $1.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 27 (8 yours) | ×0.2^0 = 27.0 |
|  | 82¢ | 5 | ×0.2^34 = 0.0 |
|  | 83¢ | 950 | ×0.2^35 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 28 @ 22¢ → $0.99/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 109 (28 yours) | ×0.2^0 = 109.1 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 97¢ | 58,044 | ×0.2^75 = 0.0 |
| | | **Σ** | **109.1** |

`yours 28.1 / Σ 109.1 = 25.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.8% = $0.99/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 20¢ → $0.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 23 (10 yours) | ×0.2^0 = 23.0 |
|  | 22¢ | 23 | ×0.2^2 = 0.9 |
|  | 23¢ | 1,946 | ×0.2^3 = 15.6 |
|  | 47¢ | 99 | ×0.2^27 = 0.0 |
|  | 50¢ | 99 | ×0.2^30 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^77 = 0.0 |
| | | **Σ** | **39.5** |

`yours 10.0 / Σ 39.5 = 25.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 25.3% = $0.97/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $0.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 53 (10 yours) | ×0.2^0 = 53.0 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **53.1** |

`yours 10.0 / Σ 53.1 = 18.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.8% = $0.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 10 @ 51¢ → $0.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 53 (10 yours) | ×0.2^0 = 53.0 |
|  | 48¢ | 11 | ×0.2^3 = 0.1 |
|  | 2¢ | 80,250 | ×0.2^49 = 0.0 |
| | | **Σ** | **53.1** |

`yours 10.0 / Σ 53.1 = 18.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.8% = $0.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 20 @ 19¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 115 (20 yours) | ×0.2^0 = 115.0 |
|  | 16¢ | 1,075 | ×0.2^3 = 8.6 |
|  | 15¢ | 1,327 | ×0.2^4 = 2.1 |
|  | 2¢ | 100,000 | ×0.2^17 = 0.0 |
| | | **Σ** | **125.7** |

`yours 20.0 / Σ 125.7 = 15.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 15.9% = $0.61/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 10 @ 15¢ → $0.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 41 (10 yours) | ×0.2^0 = 41.0 |
|  | 16¢ | 172 | ×0.2^1 = 34.4 |
|  | 50¢ | 25 | ×0.2^35 = 0.0 |
|  | 97¢ | 1,759 | ×0.2^82 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^83 = 0.0 |
| | | **Σ** | **75.4** |

`yours 10.0 / Σ 75.4 = 13.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 13.3% = $0.55/day`  

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
<details><summary><code>ewc-usgub-ca-2026-11-03-stehil</code> BUY 500 @ 4¢ → $9.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1,878 (500 yours) | ×0.2^0 = 1,878.0 |
|  | 3¢ | 11,030 | ×0.2^1 = 2,206.0 |
| | | **Σ** | **4,084.0** |

`yours 500.0 / Σ 4,084.0 = 12.2%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 12.2% = $9.18/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usgub-ca-2026-11-03-stehil` ← this one
2. `ewc-usgub-ca-2026-11-03-xavbec`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 10 @ 88¢ → $0.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 93 (10 yours) | ×0.2^0 = 93.0 |
|  | 93¢ | 124 | ×0.2^5 = 0.0 |
|  | 98¢ | 60,376 | ×0.2^10 = 0.0 |
| | | **Σ** | **93.0** |

`yours 10.0 / Σ 93.0 = 10.7%`  
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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 126 @ 19¢ → $2.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 1,295 (126 yours) | ×0.2^0 = 1,295.0 |
|  | 25¢ | 579 | ×0.2^6 = 0.0 |
|  | 49¢ | 100 | ×0.2^30 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^80 = 0.0 |
| | | **Σ** | **1,295.0** |

`yours 126.0 / Σ 1,295.0 = 9.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 9.7% = $2.43/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 1 @ 6¢ → $0.30/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 12 (1 yours) | ×0.2^0 = 12.0 |
|  | 9¢ | 100 | ×0.2^3 = 0.8 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 16¢ | 3 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^91 = 0.0 |
| | | **Σ** | **12.8** |

`yours 1.0 / Σ 12.8 = 7.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.8% = $0.30/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 40 @ 8¢ → $0.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 65 (40 yours) | ×0.2^0 = 65.0 |
|  | 9¢ | 2,406 | ×0.2^1 = 481.2 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^89 = 0.0 |
| | | **Σ** | **546.2** |

`yours 40.0 / Σ 546.2 = 7.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.3% = $0.28/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 25 @ 7¢ → $0.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 375 (25 yours) | ×0.2^0 = 375.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^91 = 0.0 |
| | | **Σ** | **375.0** |

`yours 25.0 / Σ 375.0 = 6.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 6.7% = $0.28/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 50 @ 18¢ → $1.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 749 (50 yours) | ×0.2^0 = 749.0 |
|  | 17¢ | 100 | ×0.2^1 = 20.0 |
|  | 15¢ | 30 | ×0.2^3 = 0.2 |
|  | 11¢ | 1,215 | ×0.2^7 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^17 = 0.0 |
| | | **Σ** | **769.3** |

`yours 50.0 / Σ 769.3 = 6.5%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 6.5% = $1.62/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 25 @ 6¢ → $0.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 38 (25 yours) | ×0.2^0 = 38.0 |
|  | 7¢ | 1,748 | ×0.2^1 = 349.6 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^91 = 0.0 |
| | | **Σ** | **387.6** |

`yours 25.0 / Σ 387.6 = 6.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.4% = $0.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 88 | ×0.2^0 = 88.0 |
|  | 2¢ | 422 | ×0.2^3 = 3.4 |
| ▶ | 1¢ | 25,044 (5,000 yours) | ×0.2^4 = 40.1 |
| | | **Σ** | **131.4** |

`yours 8.0 / Σ 131.4 = 6.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.1% = $0.23/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 133 @ 5¢ → $0.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 2,951 (133 yours) | ×0.2^0 = 2,951.0 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **3,350.8** |

`yours 133.0 / Σ 3,350.8 = 4.0%`  
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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 1 @ 4¢ → $0.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 60 (1 yours) | ×0.2^0 = 60.0 |
|  | 5¢ | 14 | ×0.2^1 = 2.8 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **62.8** |

`yours 1.0 / Σ 62.8 = 1.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.6% = $0.06/day`  

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
|  | 45¢ | 79 | ×0.2^17 = 0.0 |
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
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (6,504 resting) | ~90.9% | ~$22.72 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (8,294 resting) | ~88.5% | ~$22.13 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,004 resting) | ~43.0% | ~$10.76 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (308,285 resting) | ~13.9% | ~$10.43 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,523 resting) | ~39.3% | ~$9.82 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (172,873 resting) | ~12.9% | ~$9.65 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (28,543 resting) | ~25.4% | ~$6.35 |
| `ewc-usgub-ks-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (136,415 resting) | ~44.1% | ~$2.76 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (68,556 resting) | ~3.4% | ~$2.52 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (103,541 resting) | ~3.2% | ~$2.42 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (86,606 resting) | ~2.1% | ~$1.61 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (386,582 resting) | ~2.0% | ~$1.52 |

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
| 2026-08-05 9:54 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:26 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:22 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:14 PM ET | ✅ ok | 1648 | $1628.42 |
| 2026-08-05 9:06 PM ET | ✅ ok | 1640 | $1624.44 |
| 2026-08-05 9:04 PM ET | ✅ ok | 1613 | $1574.48 |
| 2026-08-05 8:52 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-05 8:13 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-05 6:29 PM ET | ✅ ok | 1611 | $1574.28 |
| 2026-08-05 4:40 PM ET | ✅ ok | 1611 | $1574.28 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
