# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-28 7:12 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$53.17/day estimated (ceiling, not promise — details below)

**Earned:** $1,116.10 lifetime ($1,114.89 paid). Last three recorded days — 2026-07-26: **$153.80** · 2026-07-25: **$125.69** · 2026-07-24: **$135.19** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — SELL at the best price, ~$17.81/day for 200 contracts. Runners-up: `apdc-jerpowgov-2026-12-31` (~$14.95/day), `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$14.65/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$53.17/day (~$2.22/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 19.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~60.8% of ask side (61,772 resting ≥ 2,000 ✓) ≈ $0.76/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 21.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~54.2% of ask side (62,069 resting ≥ 2,000 ✓) ≈ $0.68/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 12.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~50.0% of ask side (126,340 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~47.3% of ask side (103,573 resting ≥ 5,000 ✓) ≈ $1.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~47.2% of bid side (50,583 resting ≥ 5,000 ✓) ≈ $1.81/day (pool ÷ 13 markets) |
| `apdc-kashpatel-2026-08-31` | SELL | 6.0¢ | 33 | 0 | $25.00 | ✅ scoring — ~44.3% of ask side (10,224 resting ≥ 2,000 ✓) ≈ $1.85/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 18.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~39.9% of bid side (200,584 resting ≥ 5,000 ✓) ≈ $1.54/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 20.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~35.7% of ask side (142,497 resting ≥ 5,000 ✓) ≈ $1.37/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 17.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~33.7% of bid side (200,612 resting ≥ 5,000 ✓) ≈ $1.30/day (pool ÷ 13 markets) |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | BUY | 74.0¢ | 20 | 0 | $300.00 | ✅ scoring — ~33.6% of bid side (143,054 resting ≥ 10,000 ✓) ≈ $16.78/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 16.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~31.6% of bid side (80,558 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 13.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~29.4% of ask side (90,308 resting ≥ 5,000 ✓) ≈ $1.13/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 13.0¢ | 30 | 1 | $100.00 | ✅ scoring — ~28.4% of ask side (103,573 resting ≥ 5,000 ✓) ≈ $1.09/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 16.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~27.0% of bid side (200,612 resting ≥ 5,000 ✓) ≈ $1.04/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 11.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~24.9% of bid side (30,559 resting ≥ 5,000 ✓) ≈ $0.96/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 20.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~22.7% of ask side (239,876 resting ≥ 5,000 ✓) ≈ $0.87/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 19.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~17.6% of ask side (108,625 resting ≥ 5,000 ✓) ≈ $0.68/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 2.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~16.7% of ask side (43,500 resting ≥ 2,000 ✓) ≈ $0.21/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 17.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~16.0% of bid side (200,584 resting ≥ 5,000 ✓) ≈ $0.61/day (pool ÷ 13 markets) |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | BUY | 81.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~13.0% of bid side (36,089 resting ≥ 5,000 ✓) ≈ $3.26/day (pool ÷ 2 markets) |
| `pvwc-housepopw-2026-11-03-dem` | SELL | 91.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~12.3% of ask side (4,330 resting ≥ 2,000 ✓) ≈ $0.77/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 14.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~11.8% of ask side (90,308 resting ≥ 5,000 ✓) ≈ $0.45/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~9.1% of ask side (239,876 resting ≥ 5,000 ✓) ≈ $0.35/day (pool ÷ 13 markets) |
| `enwc-ussep-mi-2026-08-04-dem-halste` | SELL | 29.0¢ | 100 | 0 | $300.00 | ✅ scoring — ~7.9% of ask side (129,148 resting ≥ 10,000 ✓) ≈ $3.95/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 16.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~6.3% of bid side (80,558 resting ≥ 5,000 ✓) ≈ $0.24/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 20.0¢ | 11 | 1 | $25.00 | ✅ scoring — ~6.1% of ask side (61,772 resting ≥ 2,000 ✓) ≈ $0.08/day (pool ÷ 10 markets) |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | SELL | 20.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~4.6% of ask side (49,327 resting ≥ 5,000 ✓) ≈ $1.16/day (pool ÷ 2 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 1.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~4.6% of ask side (5,426 resting ≥ 2,000 ✓) ≈ $0.10/day (pool ÷ 6 markets) |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | SELL | 82.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~4.4% of ask side (36,220 resting ≥ 5,000 ✓) ≈ $1.09/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 10.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~3.8% of bid side (50,583 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 13 markets) |
| …and 15 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> SELL 11 @ 19¢ → $0.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 17 (11 yours) | ×0.1^0 = 17.0 |
|  | 20¢ | 11 | ×0.1^1 = 1.1 |
|  | 25¢ | 6 | ×0.1^6 = 0.0 |
|  | 27¢ | 18 | ×0.1^8 = 0.0 |
|  | 29¢ | 100 | ×0.1^10 = 0.0 |
|  | 30¢ | 2 | ×0.1^11 = 0.0 |
|  | 45¢ | 25 | ×0.1^26 = 0.0 |
|  | 97¢ | 5 | ×0.1^78 = 0.0 |
|  | 98¢ | 61,088 | ×0.1^79 = 0.0 |
| | | **Σ** | **18.1** |

`yours 11.0 / Σ 18.1 = 60.8%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 60.8% = $0.76/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15` ← this one
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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 5 @ 21¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 9 (5 yours) | ×0.1^0 = 8.7 |
|  | 25¢ | 6 | ×0.1^4 = 0.0 |
|  | 26¢ | 18 | ×0.1^5 = 0.0 |
|  | 31¢ | 100 | ×0.1^10 = 0.0 |
|  | 45¢ | 231 | ×0.1^24 = 0.0 |
|  | 98¢ | 61,205 | ×0.1^77 = 0.0 |
| | | **Σ** | **8.7** |

`yours 4.7 / Σ 8.7 = 54.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 54.2% = $0.68/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5` ← this one
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 5 @ 12¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 10 (5 yours) | ×0.2^0 = 10.0 |
|  | 18¢ | 5 | ×0.2^6 = 0.0 |
|  | 19¢ | 100 | ×0.2^7 = 0.0 |
|  | 20¢ | 3 | ×0.2^8 = 0.0 |
|  | 23¢ | 3 | ×0.2^11 = 0.0 |
|  | 30¢ | 4 | ×0.2^18 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^86 = 0.0 |
|  | 99¢ | 124,319 | ×0.2^87 = 0.0 |
| | | **Σ** | **10.0** |

`yours 5.0 / Σ 10.0 = 50.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 50.0% = $1.92/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 10 @ 12¢ → $1.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 13¢ | 31 | ×0.2^1 = 6.1 |
|  | 15¢ | 1 | ×0.2^3 = 0.0 |
|  | 16¢ | 5 | ×0.2^4 = 0.0 |
|  | 20¢ | 103 | ×0.2^8 = 0.0 |
|  | 30¢ | 4 | ×0.2^18 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 97¢ | 53,855 | ×0.2^85 = 0.0 |
| | | **Σ** | **21.1** |

`yours 10.0 / Σ 21.1 = 47.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.3% = $1.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 50 @ 10¢ → $1.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 106 (50 yours) | ×0.2^0 = 106.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 50,475 | ×0.2^9 = 0.0 |
| | | **Σ** | **106.0** |

`yours 50.0 / Σ 106.0 = 47.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.2% = $1.81/day`  

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
<details><summary><code>apdc-kashpatel-2026-08-31</code> SELL 33 @ 6¢ → $1.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 73 (33 yours) | ×0.1^0 = 73.0 |
|  | 9¢ | 1,411 | ×0.1^3 = 1.4 |
|  | 11¢ | 8,645 | ×0.1^5 = 0.1 |
| | | **Σ** | **74.5** |

`yours 33.0 / Σ 74.5 = 44.3%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 44.3% = $1.85/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-kashpatel-2026-07-31`
2. `apdc-kashpatel-2026-08-31` ← this one
3. `apdc-kashpatel-2026-12-31`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 25 @ 18¢ → $1.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 52 (25 yours) | ×0.2^0 = 52.0 |
|  | 17¢ | 53 | ×0.2^1 = 10.6 |
|  | 10¢ | 2 | ×0.2^8 = 0.0 |
|  | 5¢ | 2 | ×0.2^13 = 0.0 |
|  | 1¢ | 200,475 | ×0.2^17 = 0.0 |
| | | **Σ** | **62.6** |

`yours 25.0 / Σ 62.6 = 39.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 39.9% = $1.54/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 5 @ 20¢ → $1.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 14 (5 yours) | ×0.2^0 = 14.0 |
|  | 26¢ | 100 | ×0.2^6 = 0.0 |
|  | 30¢ | 4 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 97¢ | 92,783 | ×0.2^77 = 0.0 |
| | | **Σ** | **14.0** |

`yours 5.0 / Σ 14.0 = 35.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 35.7% = $1.37/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 25 @ 17¢ → $1.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 54 (25 yours) | ×0.2^0 = 54.0 |
|  | 16¢ | 100 | ×0.2^1 = 20.0 |
|  | 15¢ | 2 | ×0.2^2 = 0.1 |
|  | 14¢ | 4 | ×0.2^3 = 0.0 |
|  | 5¢ | 2 | ×0.2^12 = 0.0 |
|  | 3¢ | 200,250 | ×0.2^14 = 0.0 |
| | | **Σ** | **74.1** |

`yours 25.0 / Σ 74.1 = 33.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.7% = $1.30/day`  

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
<details><summary><code>enwc-ussep-mi-2026-08-04-dem-abdels</code> BUY 20 @ 74¢ → $16.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 58 (20 yours) | ×0.2^0 = 58.0 |
|  | 71¢ | 184 | ×0.2^3 = 1.5 |
|  | 67¢ | 19 | ×0.2^7 = 0.0 |
|  | 66¢ | 42,000 | ×0.2^8 = 0.1 |
| | | **Σ** | **59.6** |

`yours 20.0 / Σ 59.6 = 33.6%`  
`$300 ÷ 3 ÷ 2 = $50.00 × 33.6% = $16.78/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `enwc-ussep-mi-2026-08-04-dem-abdels` ← this one
2. `enwc-ussep-mi-2026-08-04-dem-halste`
3. `enwc-ussep-mi-2026-08-04-dem-malmcm`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 25 @ 16¢ → $1.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 79 (25 yours) | ×0.2^0 = 79.1 |
|  | 10¢ | 2 | ×0.2^6 = 0.0 |
|  | 5¢ | 2 | ×0.2^11 = 0.0 |
|  | 1¢ | 80,475 | ×0.2^15 = 0.0 |
| | | **Σ** | **79.1** |

`yours 25.0 / Σ 79.1 = 31.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.6% = $1.22/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 10 @ 13¢ → $1.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 30 (10 yours) | ×0.2^0 = 30.0 |
|  | 14¢ | 20 | ×0.2^1 = 4.0 |
|  | 15¢ | 1 | ×0.2^2 = 0.0 |
|  | 19¢ | 100 | ×0.2^6 = 0.0 |
|  | 20¢ | 3 | ×0.2^7 = 0.0 |
|  | 30¢ | 4 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^37 = 0.0 |
|  | 97¢ | 40,555 | ×0.2^84 = 0.0 |
| | | **Σ** | **34.0** |

`yours 10.0 / Σ 34.0 = 29.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.4% = $1.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 13¢ → $1.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 15 | ×0.2^0 = 15.0 |
| ▶ | 13¢ | 31 (30 yours) | ×0.2^1 = 6.1 |
|  | 15¢ | 1 | ×0.2^3 = 0.0 |
|  | 16¢ | 5 | ×0.2^4 = 0.0 |
|  | 20¢ | 103 | ×0.2^8 = 0.0 |
|  | 30¢ | 4 | ×0.2^18 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 97¢ | 53,855 | ×0.2^85 = 0.0 |
| | | **Σ** | **21.1** |

`yours 6.0 / Σ 21.1 = 28.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.4% = $1.09/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 100 @ 16¢ → $1.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 54 | ×0.2^0 = 54.0 |
| ▶ | 16¢ | 100 (100 yours) | ×0.2^1 = 20.0 |
|  | 15¢ | 2 | ×0.2^2 = 0.1 |
|  | 14¢ | 4 | ×0.2^3 = 0.0 |
|  | 5¢ | 2 | ×0.2^12 = 0.0 |
|  | 3¢ | 200,250 | ×0.2^14 = 0.0 |
| | | **Σ** | **74.1** |

`yours 20.0 / Σ 74.1 = 27.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.0% = $1.04/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 20 @ 11¢ → $0.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 80 (20 yours) | ×0.2^0 = 80.0 |
|  | 10¢ | 2 | ×0.2^1 = 0.4 |
|  | 5¢ | 2 | ×0.2^6 = 0.0 |
|  | 1¢ | 30,475 | ×0.2^10 = 0.0 |
| | | **Σ** | **80.4** |

`yours 20.0 / Σ 80.4 = 24.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 24.9% = $0.96/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 5 @ 20¢ → $0.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 20 (5 yours) | ×0.2^0 = 20.0 |
|  | 21¢ | 10 | ×0.2^1 = 2.0 |
|  | 24¢ | 5 | ×0.2^4 = 0.0 |
|  | 26¢ | 100 | ×0.2^6 = 0.0 |
|  | 30¢ | 4 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^78 = 0.0 |
|  | 99¢ | 238,637 | ×0.2^79 = 0.0 |
| | | **Σ** | **22.0** |

`yours 5.0 / Σ 22.0 = 22.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 22.7% = $0.87/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 5 @ 19¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 26 (5 yours) | ×0.2^0 = 26.0 |
|  | 20¢ | 8 | ×0.2^1 = 1.6 |
|  | 22¢ | 100 | ×0.2^3 = 0.8 |
|  | 30¢ | 4 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 97¢ | 53,892 | ×0.2^78 = 0.0 |
| | | **Σ** | **28.4** |

`yours 5.0 / Σ 28.4 = 17.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.6% = $0.68/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 2¢ → $0.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 6 (1 yours) | ×0.1^0 = 6.0 |
|  | 8¢ | 6 | ×0.1^6 = 0.0 |
|  | 9¢ | 18 | ×0.1^7 = 0.0 |
|  | 16¢ | 100 | ×0.1^14 = 0.0 |
|  | 20¢ | 3 | ×0.1^18 = 0.0 |
|  | 30¢ | 2 | ×0.1^28 = 0.0 |
|  | 43¢ | 3,387 | ×0.1^41 = 0.0 |
| | | **Σ** | **6.0** |

`yours 1.0 / Σ 6.0 = 16.7%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 16.7% = $0.21/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20` ← this one
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 50 @ 17¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 52 | ×0.2^0 = 52.0 |
| ▶ | 17¢ | 53 (50 yours) | ×0.2^1 = 10.6 |
|  | 10¢ | 2 | ×0.2^8 = 0.0 |
|  | 5¢ | 2 | ×0.2^13 = 0.0 |
|  | 1¢ | 200,475 | ×0.2^17 = 0.0 |
| | | **Σ** | **62.6** |

`yours 10.0 / Σ 62.6 = 16.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.0% = $0.61/day`  

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
<details><summary><code>enwc-ussep-mn-2026-08-11-dem-pegfla</code> BUY 10 @ 81¢ → $3.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 81¢ | 76 (10 yours) | ×0.2^0 = 76.0 |
|  | 79¢ | 6 | ×0.2^2 = 0.2 |
|  | 74¢ | 36,005 | ×0.2^7 = 0.5 |
| | | **Σ** | **76.7** |

`yours 10.0 / Σ 76.7 = 13.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 13.0% = $3.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-mn-2026-08-11-dem-angcra`
2. `enwc-ussep-mn-2026-08-11-dem-pegfla` ← this one

</details>

</details>
<details><summary><code>pvwc-housepopw-2026-11-03-dem</code> SELL 10 @ 91¢ → $0.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 91¢ | 81 (10 yours) | ×0.1^0 = 81.0 |
|  | 95¢ | 1,649 | ×0.1^4 = 0.2 |
|  | 99¢ | 2,600 | ×0.1^8 = 0.0 |
| | | **Σ** | **81.2** |

`yours 10.0 / Σ 81.2 = 12.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 12.3% = $0.77/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem` ← this one
2. `pvwc-housepopw-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 14¢ → $0.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 30 | ×0.2^0 = 30.0 |
| ▶ | 14¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 15¢ | 1 | ×0.2^2 = 0.0 |
|  | 19¢ | 100 | ×0.2^6 = 0.0 |
|  | 20¢ | 3 | ×0.2^7 = 0.0 |
|  | 30¢ | 4 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^37 = 0.0 |
|  | 97¢ | 40,555 | ×0.2^84 = 0.0 |
| | | **Σ** | **34.0** |

`yours 4.0 / Σ 34.0 = 11.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.8% = $0.45/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 10 @ 21¢ → $0.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 20¢ | 20 | ×0.2^0 = 20.0 |
| ▶ | 21¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 24¢ | 5 | ×0.2^4 = 0.0 |
|  | 26¢ | 100 | ×0.2^6 = 0.0 |
|  | 30¢ | 4 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^78 = 0.0 |
|  | 99¢ | 238,637 | ×0.2^79 = 0.0 |
| | | **Σ** | **22.0** |

`yours 2.0 / Σ 22.0 = 9.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.1% = $0.35/day`  

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
<details><summary><code>enwc-ussep-mi-2026-08-04-dem-halste</code> SELL 100 @ 29¢ → $3.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 1,093 (100 yours) | ×0.2^0 = 1,093.0 |
|  | 30¢ | 607 | ×0.2^1 = 121.4 |
|  | 32¢ | 60 | ×0.2^3 = 0.5 |
|  | 33¢ | 32,000 | ×0.2^4 = 51.2 |
| | | **Σ** | **1,266.1** |

`yours 100.0 / Σ 1,266.1 = 7.9%`  
`$300 ÷ 3 ÷ 2 = $50.00 × 7.9% = $3.95/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `enwc-ussep-mi-2026-08-04-dem-abdels`
2. `enwc-ussep-mi-2026-08-04-dem-halste` ← this one
3. `enwc-ussep-mi-2026-08-04-dem-malmcm`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 5 @ 16¢ → $0.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 79 (5 yours) | ×0.2^0 = 79.1 |
|  | 10¢ | 2 | ×0.2^6 = 0.0 |
|  | 5¢ | 2 | ×0.2^11 = 0.0 |
|  | 1¢ | 80,475 | ×0.2^15 = 0.0 |
| | | **Σ** | **79.1** |

`yours 5.0 / Σ 79.1 = 6.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.3% = $0.24/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> SELL 11 @ 20¢ → $0.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 17 | ×0.1^0 = 17.0 |
| ▶ | 20¢ | 11 (11 yours) | ×0.1^1 = 1.1 |
|  | 25¢ | 6 | ×0.1^6 = 0.0 |
|  | 27¢ | 18 | ×0.1^8 = 0.0 |
|  | 29¢ | 100 | ×0.1^10 = 0.0 |
|  | 30¢ | 2 | ×0.1^11 = 0.0 |
|  | 45¢ | 25 | ×0.1^26 = 0.0 |
|  | 97¢ | 5 | ×0.1^78 = 0.0 |
|  | 98¢ | 61,088 | ×0.1^79 = 0.0 |
| | | **Σ** | **18.1** |

`yours 1.1 / Σ 18.1 = 6.1%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 6.1% = $0.08/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15` ← this one
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
<details><summary><code>enwc-ussep-mn-2026-08-11-dem-angcra</code> SELL 15 @ 20¢ → $1.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 321 (15 yours) | ×0.2^0 = 321.0 |
|  | 26¢ | 48,000 | ×0.2^6 = 3.1 |
| | | **Σ** | **324.1** |

`yours 15.0 / Σ 324.1 = 4.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 4.6% = $1.16/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-mn-2026-08-11-dem-angcra` ← this one
2. `enwc-ussep-mn-2026-08-11-dem-pegfla`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-sarrod</code> SELL 100 @ 1¢ → $0.10/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,169 (100 yours) | ×0.1^0 = 2,169.0 |
| | | **Σ** | **2,169.0** |

`yours 100.0 / Σ 2,169.0 = 4.6%`  
`$25 ÷ 6 ÷ 2 = $2.08 × 4.6% = $0.10/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-mn-2026-08-11-dem-pegfla</code> SELL 5 @ 82¢ → $1.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 113 (5 yours) | ×0.2^0 = 113.0 |
|  | 83¢ | 7 | ×0.2^1 = 1.4 |
|  | 89¢ | 35,000 | ×0.2^7 = 0.4 |
| | | **Σ** | **114.8** |

`yours 5.0 / Σ 114.8 = 4.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 4.4% = $1.09/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ussep-mn-2026-08-11-dem-angcra`
2. `enwc-ussep-mn-2026-08-11-dem-pegfla` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 4 @ 10¢ → $0.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 106 (4 yours) | ×0.2^0 = 106.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 50,475 | ×0.2^9 = 0.0 |
| | | **Σ** | **106.0** |

`yours 4.0 / Σ 106.0 = 3.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.8% = $0.15/day`  

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
| 2026-07-26 | ~$159.09 | $153.80 | 97% |
| 2026-07-25 | ~$123.00 | $125.69 | 102% |
| 2026-07-24 | ~$133.49 | $135.19 | 101% |

Biggest gaps on 2026-07-26: `pvwc-housepopw-2026-11-03-dem` (est ~$3.30 → got $0.37), `vmc-ussep-misen-2026-08-04-els0-5` (est ~$3.67 → got $1.39), `lawec-cryptoleg-2026-08-10` (est ~$3.57 → got $2.35)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (92,292 resting) | ~71.2% | ~$17.81 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (25,265 resting) | ~89.7% | ~$14.95 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (64,954 resting) | ~58.6% | ~$14.65 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (87,926 resting) | ~17.9% | ~$13.42 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (173,062 resting) | ~10.8% | ~$8.10 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (93,755 resting) | ~4.0% | ~$2.97 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (75,319 resting) | ~45.8% | ~$2.86 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (97,915 resting) | ~3.4% | ~$2.56 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (173,230 resting) | ~2.9% | ~$2.16 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (103,519 resting) | ~2.8% | ~$2.13 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (51,637 resting) | ~2.3% | ~$1.69 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (67,579 resting) | ~5.1% | ~$1.28 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,114.89 |
| Skipped | $1.21 |
| **Total earned** | **$1,116.10** |

823 reward rows · 24 days with rewards · 302 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
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
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `█` |
| 2026-07-13 | $10.03 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,116.10 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $58.43 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.16 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.65 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `opdc-mcconnell-resign-2026-11-02` | $32.64 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.70 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $27.29 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $25.79 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $24.49 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.61 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.58 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $22.32 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-28 7:12 AM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 6:54 AM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 5:59 AM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 2:45 AM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-27 11:42 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-27 9:13 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-27 8:17 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 8:14 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 8:11 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 7:54 PM ET | ✅ ok | 567 | $962.30 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
