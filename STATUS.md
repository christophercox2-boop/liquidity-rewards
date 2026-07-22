# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-22 2:44 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$104.47/day estimated (ceiling, not promise — details below)

**Earned:** $299.40 lifetime ($155.84 paid). Last three recorded days — 2026-07-20: **$106.54** · 2026-07-19: **$35.81** · 2026-07-18: **$44.41** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — BUY at the best price, ~$9.18/day for 200 contracts. Runners-up: `enwc-ussep-mn-2026-08-11-dem-angcra` (~$7.60/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$7.22/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$104.47/day (~$4.35/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ushrp-mo01-2026-08-04-dem-corbus` | BUY | 57.0¢ | 25 | 0 | $500.00 | ✅ scoring — ~100.0% of bid side (10,099 resting ≥ 10,000 ✓) ≈ $12.50/day (pool ÷ 2 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | BUY | 44.0¢ | 40 | 0 | $250.00 | ✅ scoring — ~100.0% of bid side (11,120 resting ≥ 10,000 ✓) ≈ $12.50/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 93.0¢ | 200 | 0 | $250.00 | ✅ scoring — ~81.2% of ask side (51,303 resting ≥ 10,000 ✓) ≈ $8.46/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | SELL | 6.0¢ | 207 | 0 | $250.00 | ✅ scoring — ~72.9% of ask side (11,623 resting ≥ 10,000 ✓) ≈ $9.11/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 10.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~66.7% of ask side (11,040 resting ≥ 10,000 ✓) ≈ $8.33/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | SELL | 9.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~48.6% of ask side (10,927 resting ≥ 10,000 ✓) ≈ $6.07/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 19.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~39.4% of ask side (11,442 resting ≥ 10,000 ✓) ≈ $4.93/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 17.0¢ | 100 | 1 | $250.00 | ✅ scoring — ~33.4% of ask side (10,998 resting ≥ 10,000 ✓) ≈ $4.18/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~30.5% of bid side (32,803 resting ≥ 10,000 ✓) ≈ $3.18/day (pool ÷ 12 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | BUY | 75.0¢ | 30 | 1 | $250.00 | ✅ scoring — ~27.3% of bid side (10,134 resting ≥ 10,000 ✓) ≈ $5.68/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~27.2% of bid side (36,755 resting ≥ 10,000 ✓) ≈ $5.67/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | BUY | 1.0¢ | 10,000 | 3 | $250.00 | ✅ scoring — ~19.9% of bid side (31,045 resting ≥ 10,000 ✓) ≈ $2.49/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-rusfry` | BUY | 1.0¢ | 10,000 | 5 | $250.00 | ✅ scoring — ~18.3% of bid side (30,360 resting ≥ 10,000 ✓) ≈ $1.90/day (pool ÷ 12 markets) |
| `apdc-alito-2026-08-31` | BUY | 18.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~17.2% of bid side (10,919 resting ≥ 10,000 ✓) ≈ $7.17/day (pool ÷ 3 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | BUY | 13.0¢ | 50 | 0 | $250.00 | ✅ scoring — ~15.3% of bid side (34,313 resting ≥ 10,000 ✓) ≈ $3.18/day (pool ÷ 6 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | BUY | 1.0¢ | 10,000 | 0 | $250.00 | ✅ scoring — ~10.1% of bid side (99,080 resting ≥ 10,000 ✓) ≈ $2.10/day (pool ÷ 6 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | BUY | 25.0¢ | 100 | 3 | $250.00 | ✅ scoring — ~8.4% of bid side (11,014 resting ≥ 10,000 ✓) ≈ $0.88/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | BUY | 27.0¢ | 40 | 0 | $250.00 | ✅ scoring — ~8.2% of bid side (10,784 resting ≥ 10,000 ✓) ≈ $1.02/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | SELL | 18.0¢ | 171 | 0 | $250.00 | ✅ scoring — ~5.4% of ask side (39,447 resting ≥ 10,000 ✓) ≈ $1.12/day (pool ÷ 6 markets) |
| `enwc-ussep-mi-2026-08-04-dem-halste` | BUY | 20.0¢ | 200 | 0 | $250.00 | ✅ scoring — ~4.7% of bid side (47,594 resting ≥ 10,000 ✓) ≈ $1.97/day (pool ÷ 3 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 99.0¢ | 10,000 | 6 | $250.00 | ✅ scoring — ~3.0% of ask side (51,303 resting ≥ 10,000 ✓) ≈ $0.31/day (pool ÷ 12 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 4.0¢ | 100 | 0 | $250.00 | ✅ scoring — ~2.5% of ask side (37,956 resting ≥ 10,000 ✓) ≈ $0.53/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 1.0¢ | 10,000 | 6 | $250.00 | ✅ scoring — ~2.3% of bid side (30,848 resting ≥ 10,000 ✓) ≈ $0.29/day (pool ÷ 10 markets) |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | SELL | 4.0¢ | 80 | 0 | $250.00 | ✅ scoring — ~2.0% of ask side (37,956 resting ≥ 10,000 ✓) ≈ $0.42/day (pool ÷ 6 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 25.0¢ | 5 | 0 | $250.00 | ✅ scoring — ~1.4% of bid side (10,989 resting ≥ 10,000 ✓) ≈ $0.18/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | BUY | 5.0¢ | 90 | 3 | $250.00 | ✅ scoring — ~0.6% of bid side (11,031 resting ≥ 10,000 ✓) ≈ $0.08/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 5.0¢ | 20 | 2 | $250.00 | ✅ scoring — ~0.6% of bid side (30,848 resting ≥ 10,000 ✓) ≈ $0.07/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | BUY | 1.0¢ | 10,000 | 7 | $250.00 | ✅ scoring — ~0.6% of bid side (11,031 resting ≥ 10,000 ✓) ≈ $0.07/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | SELL | 28.0¢ | 10 | 1 | $250.00 | ✅ scoring — ~0.5% of ask side (10,997 resting ≥ 10,000 ✓) ≈ $0.06/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | BUY | 23.0¢ | 5 | 2 | $250.00 | ✅ scoring — ~0.1% of bid side (10,989 resting ≥ 10,000 ✓) ≈ $0.02/day (pool ÷ 10 markets) |
| …and 18 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ushrp-mo01-2026-08-04-dem-corbus</code> BUY 25 @ 57¢ → $12.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 57¢ | 25 (25 yours) | ×0.3^0 = 25.0 |
|  | 17¢ | 25 | ×0.3^40 = 0.0 |
|  | 1¢ | 10,049 | ×0.3^56 = 0.0 |
| | | **Σ** | **25.0** |

`yours 25.0 / Σ 25.0 = 100.0%`  
`$500 ÷ 2 ÷ 2 = $12.50 × 100.0% = $12.50/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `enwc-ushrp-mo01-2026-08-04-dem-corbus` ← this one
2. `enwc-ushrp-mo01-2026-08-04-dem-wesbel`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> BUY 40 @ 44¢ → $12.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 44¢ | 40 (40 yours) | ×0.3^0 = 40.0 |
|  | 38¢ | 6 | ×0.3^6 = 0.0 |
|  | 36¢ | 28 | ×0.3^8 = 0.0 |
|  | 14¢ | 25 | ×0.3^30 = 0.0 |
|  | 1¢ | 11,021 | ×0.3^43 = 0.0 |
| | | **Σ** | **40.0** |

`yours 40.0 / Σ 40.0 = 100.0%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 100.0% = $12.50/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 200 @ 93¢ → $8.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 93¢ | 200 (200 yours) | ×0.3^0 = 200.0 |
|  | 95¢ | 102 | ×0.3^2 = 9.2 |
|  | 99¢ | 51,001 | ×0.3^6 = 37.2 |
| | | **Σ** | **246.4** |

`yours 200.0 / Σ 246.4 = 81.2%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 81.2% = $8.46/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor` ← this one
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> SELL 207 @ 6¢ → $9.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 284 (207 yours) | ×0.3^0 = 284.0 |
|  | 12¢ | 6 | ×0.3^6 = 0.0 |
|  | 15¢ | 29 | ×0.3^9 = 0.0 |
|  | 24¢ | 250 | ×0.3^18 = 0.0 |
|  | 45¢ | 25 | ×0.3^39 = 0.0 |
|  | 99¢ | 11,029 | ×0.3^93 = 0.0 |
| | | **Σ** | **284.0** |

`yours 207.0 / Σ 284.0 = 72.9%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 72.9% = $9.11/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15` ← this one
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 100 @ 10¢ → $8.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 150 (100 yours) | ×0.3^0 = 150.0 |
|  | 16¢ | 6 | ×0.3^6 = 0.0 |
|  | 18¢ | 28 | ×0.3^8 = 0.0 |
|  | 21¢ | 535 | ×0.3^11 = 0.0 |
|  | 45¢ | 25 | ×0.3^35 = 0.0 |
|  | 99¢ | 10,296 | ×0.3^89 = 0.0 |
| | | **Σ** | **150.0** |

`yours 100.0 / Σ 150.0 = 66.7%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 66.7% = $8.33/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20` ← this one
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> SELL 100 @ 9¢ → $6.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 201 (100 yours) | ×0.3^0 = 201.0 |
|  | 13¢ | 34 | ×0.3^4 = 0.3 |
|  | 14¢ | 1,861 | ×0.3^5 = 4.5 |
|  | 21¢ | 250 | ×0.3^12 = 0.0 |
|  | 45¢ | 25 | ×0.3^36 = 0.0 |
|  | 99¢ | 8,556 | ×0.3^90 = 0.0 |
| | | **Σ** | **205.8** |

`yours 100.0 / Σ 205.8 = 48.6%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 48.6% = $6.07/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 100 @ 19¢ → $4.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 100 (100 yours) | ×0.3^0 = 100.0 |
|  | 20¢ | 437 | ×0.3^1 = 131.1 |
|  | 21¢ | 250 | ×0.3^2 = 22.5 |
|  | 25¢ | 6 | ×0.3^6 = 0.0 |
|  | 27¢ | 28 | ×0.3^8 = 0.0 |
|  | 45¢ | 25 | ×0.3^26 = 0.0 |
|  | 99¢ | 10,596 | ×0.3^80 = 0.0 |
| | | **Σ** | **253.6** |

`yours 100.0 / Σ 253.6 = 39.4%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 39.4% = $4.93/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 100 @ 17¢ → $4.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 28 | ×0.3^0 = 28.0 |
| ▶ | 17¢ | 201 (100 yours) | ×0.3^1 = 60.3 |
|  | 20¢ | 6 | ×0.3^4 = 0.0 |
|  | 21¢ | 578 | ×0.3^5 = 1.4 |
|  | 45¢ | 25 | ×0.3^29 = 0.0 |
|  | 99¢ | 10,160 | ×0.3^83 = 0.0 |
| | | **Σ** | **89.8** |

`yours 30.0 / Σ 89.8 = 33.4%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 33.4% = $4.18/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> BUY 10,000 @ 1¢ → $3.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 32,803 (10,000 yours) | ×0.3^0 = 32,803.0 |
| | | **Σ** | **32,803.0** |

`yours 10,000.0 / Σ 32,803.0 = 30.5%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 30.5% = $3.18/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor` ← this one
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-frahon</code> BUY 30 @ 75¢ → $5.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 76¢ | 24 | ×0.3^0 = 24.0 |
| ▶ | 75¢ | 30 (30 yours) | ×0.3^1 = 9.0 |
|  | 69¢ | 55 | ×0.3^7 = 0.0 |
|  | 66¢ | 25 | ×0.3^10 = 0.0 |
|  | 1¢ | 10,000 | ×0.3^75 = 0.0 |
| | | **Σ** | **33.0** |

`yours 9.0 / Σ 33.0 = 27.3%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 27.3% = $5.68/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon` ← this one
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-kelroy</code> BUY 10,000 @ 1¢ → $5.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 36,755 (10,000 yours) | ×0.3^0 = 36,755.0 |
| | | **Σ** | **36,755.0** |

`yours 10,000.0 / Σ 36,755.0 = 27.2%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 27.2% = $5.67/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy` ← this one
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> BUY 10,000 @ 1¢ → $2.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 532 | ×0.3^0 = 531.8 |
|  | 2¢ | 33 | ×0.3^2 = 3.0 |
| ▶ | 1¢ | 30,480 (10,000 yours) | ×0.3^3 = 823.0 |
| | | **Σ** | **1,357.7** |

`yours 270.0 / Σ 1,357.7 = 19.9%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 19.9% = $2.49/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15` ← this one
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-rusfry</code> BUY 10,000 @ 1¢ → $1.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 54 | ×0.3^0 = 54.2 |
|  | 5¢ | 1 | ×0.3^1 = 0.3 |
|  | 4¢ | 55 | ×0.3^2 = 5.0 |
| ▶ | 1¢ | 30,250 (10,000 yours) | ×0.3^5 = 73.5 |
| | | **Σ** | **132.9** |

`yours 24.3 / Σ 132.9 = 18.3%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 18.3% = $1.90/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry` ← this one
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>apdc-alito-2026-08-31</code> BUY 50 @ 18¢ → $7.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 289 (50 yours) | ×0.3^0 = 289.0 |
|  | 17¢ | 5 | ×0.3^1 = 1.5 |
|  | 2¢ | 275 | ×0.3^16 = 0.0 |
|  | 1¢ | 10,350 | ×0.3^17 = 0.0 |
| | | **Σ** | **290.5** |

`yours 50.0 / Σ 290.5 = 17.2%`  
`$250 ÷ 3 ÷ 2 = $41.67 × 17.2% = $7.17/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-alito-2026-07-31`
2. `apdc-alito-2026-08-31` ← this one
3. `apdc-alito-2026-12-31`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> BUY 50 @ 13¢ → $3.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 50 (50 yours) | ×0.3^0 = 50.0 |
|  | 9¢ | 34,222 | ×0.3^4 = 277.2 |
| | | **Σ** | **327.2** |

`yours 50.0 / Σ 327.2 = 15.3%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 15.3% = $3.18/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-joebre</code> BUY 10,000 @ 1¢ → $2.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 99,080 (10,000 yours) | ×0.3^0 = 99,080.0 |
| | | **Σ** | **99,080.0** |

`yours 10,000.0 / Σ 99,080.0 = 10.1%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 10.1% = $2.10/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre` ← this one
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> BUY 100 @ 25¢ → $0.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 28¢ | 25 | ×0.3^0 = 25.0 |
|  | 27¢ | 14 | ×0.3^1 = 4.2 |
|  | 26¢ | 1 | ×0.3^2 = 0.1 |
| ▶ | 25¢ | 100 (100 yours) | ×0.3^3 = 2.7 |
|  | 1¢ | 10,874 | ×0.3^27 = 0.0 |
| | | **Σ** | **32.0** |

`yours 2.7 / Σ 32.0 = 8.4%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 8.4% = $0.88/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor` ← this one
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> BUY 40 @ 27¢ → $1.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 490 (40 yours) | ×0.3^0 = 490.0 |
|  | 21¢ | 6 | ×0.3^6 = 0.0 |
|  | 19¢ | 28 | ×0.3^8 = 0.0 |
|  | 8¢ | 200 | ×0.3^19 = 0.0 |
|  | 1¢ | 10,060 | ×0.3^26 = 0.0 |
| | | **Σ** | **490.0** |

`yours 40.0 / Σ 490.0 = 8.2%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 8.2% = $1.02/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10` ← this one
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-davcro</code> SELL 171 @ 18¢ → $1.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 696 (171 yours) | ×0.3^0 = 696.0 |
|  | 20¢ | 27,500 | ×0.3^2 = 2,475.0 |
| | | **Σ** | **3,171.0** |

`yours 171.0 / Σ 3,171.0 = 5.4%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 5.4% = $1.12/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro` ← this one
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod`

</details>

</details>
<details><summary><code>enwc-ussep-mi-2026-08-04-dem-halste</code> BUY 200 @ 20¢ → $1.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 800 (200 yours) | ×0.3^0 = 800.0 |
|  | 19¢ | 600 | ×0.3^1 = 180.0 |
|  | 18¢ | 36,111 | ×0.3^2 = 3,250.0 |
| | | **Σ** | **4,230.0** |

`yours 200.0 / Σ 4,230.0 = 4.7%`  
`$250 ÷ 3 ÷ 2 = $41.67 × 4.7% = $1.97/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `enwc-ussep-mi-2026-08-04-dem-abdels`
2. `enwc-ussep-mi-2026-08-04-dem-halste` ← this one
3. `enwc-ussep-mi-2026-08-04-dem-malmcm`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 10,000 @ 99¢ → $0.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 93¢ | 200 | ×0.3^0 = 200.0 |
|  | 95¢ | 102 | ×0.3^2 = 9.2 |
| ▶ | 99¢ | 51,001 (10,000 yours) | ×0.3^6 = 37.2 |
| | | **Σ** | **246.4** |

`yours 7.3 / Σ 246.4 = 3.0%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 3.0% = $0.31/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor` ← this one
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-sarrod</code> SELL 100 @ 4¢ → $0.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 705 (100 yours) | ×0.3^0 = 705.0 |
|  | 6¢ | 36,000 | ×0.3^2 = 3,240.0 |
| | | **Σ** | **3,945.0** |

`yours 100.0 / Σ 3,945.0 = 2.5%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 2.5% = $0.53/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 10,000 @ 1¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 289 | ×0.3^0 = 289.0 |
|  | 5¢ | 20 | ×0.3^2 = 1.8 |
|  | 2¢ | 34 | ×0.3^5 = 0.1 |
| ▶ | 1¢ | 30,505 (10,000 yours) | ×0.3^6 = 22.2 |
| | | **Σ** | **313.1** |

`yours 7.3 / Σ 313.1 = 2.3%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 2.3% = $0.29/day`  

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
<details><summary><code>enwc-usgubp-wi-2026-08-11-dem-sarrod</code> SELL 80 @ 4¢ → $0.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 705 (80 yours) | ×0.3^0 = 705.0 |
|  | 6¢ | 36,000 | ×0.3^2 = 3,240.0 |
| | | **Σ** | **3,945.0** |

`yours 80.0 / Σ 3,945.0 = 2.0%`  
`$250 ÷ 6 ÷ 2 = $20.83 × 2.0% = $0.42/day`  

<details><summary>÷ 6 markets in this race — tap to list</summary>

1. `enwc-usgubp-wi-2026-08-11-dem-davcro`
2. `enwc-usgubp-wi-2026-08-11-dem-frahon`
3. `enwc-usgubp-wi-2026-08-11-dem-joebre`
4. `enwc-usgubp-wi-2026-08-11-dem-kelroy`
5. `enwc-usgubp-wi-2026-08-11-dem-manbar`
6. `enwc-usgubp-wi-2026-08-11-dem-sarrod` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 5 @ 25¢ → $0.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 355 (5 yours) | ×0.3^0 = 355.0 |
|  | 23¢ | 5 | ×0.3^2 = 0.4 |
|  | 19¢ | 6 | ×0.3^6 = 0.0 |
|  | 18¢ | 70 | ×0.3^7 = 0.0 |
|  | 17¢ | 28 | ×0.3^8 = 0.0 |
|  | 2¢ | 500 | ×0.3^23 = 0.0 |
|  | 1¢ | 10,025 | ×0.3^24 = 0.0 |
| | | **Σ** | **355.5** |

`yours 5.0 / Σ 355.5 = 1.4%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 1.4% = $0.18/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> BUY 90 @ 5¢ → $0.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 382 | ×0.3^0 = 381.7 |
| ▶ | 5¢ | 90 (90 yours) | ×0.3^3 = 2.4 |
|  | 3¢ | 34 | ×0.3^5 = 0.1 |
|  | 2¢ | 500 | ×0.3^6 = 0.4 |
|  | 1¢ | 10,025 | ×0.3^7 = 2.2 |
| | | **Σ** | **386.7** |

`yours 2.4 / Σ 386.7 = 0.6%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.6% = $0.08/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20` ← this one
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 20 @ 5¢ → $0.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 289 | ×0.3^0 = 289.0 |
| ▶ | 5¢ | 20 (20 yours) | ×0.3^2 = 1.8 |
|  | 2¢ | 34 | ×0.3^5 = 0.1 |
|  | 1¢ | 30,505 | ×0.3^6 = 22.2 |
| | | **Σ** | **313.1** |

`yours 1.8 / Σ 313.1 = 0.6%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.6% = $0.07/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> BUY 10,000 @ 1¢ → $0.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 382 | ×0.3^0 = 381.7 |
|  | 5¢ | 90 | ×0.3^3 = 2.4 |
|  | 3¢ | 34 | ×0.3^5 = 0.1 |
|  | 2¢ | 500 | ×0.3^6 = 0.4 |
| ▶ | 1¢ | 10,025 (10,000 yours) | ×0.3^7 = 2.2 |
| | | **Σ** | **386.7** |

`yours 2.2 / Σ 386.7 = 0.6%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.6% = $0.07/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20` ← this one
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-nanmac</code> SELL 10 @ 28¢ → $0.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 27¢ | 563 | ×0.3^0 = 563.0 |
| ▶ | 28¢ | 10 (10 yours) | ×0.3^1 = 3.0 |
|  | 33¢ | 10 | ×0.3^6 = 0.0 |
|  | 38¢ | 130 | ×0.3^11 = 0.0 |
|  | 46¢ | 101 | ×0.3^19 = 0.0 |
|  | 50¢ | 25 | ×0.3^23 = 0.0 |
|  | 99¢ | 10,158 | ×0.3^72 = 0.0 |
| | | **Σ** | **566.0** |

`yours 3.0 / Σ 566.0 = 0.5%`  
`$250 ÷ 12 ÷ 2 = $10.42 × 0.5% = $0.06/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac` ← this one
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> BUY 5 @ 23¢ → $0.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 25¢ | 355 | ×0.3^0 = 355.0 |
| ▶ | 23¢ | 5 (5 yours) | ×0.3^2 = 0.4 |
|  | 19¢ | 6 | ×0.3^6 = 0.0 |
|  | 18¢ | 70 | ×0.3^7 = 0.0 |
|  | 17¢ | 28 | ×0.3^8 = 0.0 |
|  | 2¢ | 500 | ×0.3^23 = 0.0 |
|  | 1¢ | 10,025 | ×0.3^24 = 0.0 |
| | | **Σ** | **355.5** |

`yours 0.4 / Σ 355.5 = 0.1%`  
`$250 ÷ 10 ÷ 2 = $12.50 × 0.1% = $0.02/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-20 | ~$125.00 | $106.54 | 85% |
| 2026-07-19 | ~$36.97 | $35.81 | 97% |

Biggest gaps on 2026-07-20: `enwc-usgubp-wi-2026-08-11-dem-davcro` (est ~$21.74 → got $16.08), `enwc-ussep-nh-2026-09-01-rep-scobro` (est ~$11.93 → got $8.30), `enwc-usgubp-ok-2026-06-16-rep-gendru` (est ~$4.33 → got $2.14)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (10,916 resting) | ~22.0% | ~$9.18 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (12,470 resting) | ~12.2% | ~$7.60 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (51,329 resting) | ~11.5% | ~$7.22 |
| `ewc-usgub-ks-2026-11-03-dem` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (110,759 resting) | ~11.3% | ~$7.05 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (59,913 resting) | ~6.3% | ~$3.95 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $250.00 ÷ 2 | 0.30 | 10,000 | SELL side (62,041 resting) | ~5.8% | ~$3.64 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $250.00 ÷ 3 | 0.30 | 10,000 | SELL side (52,715 resting) | ~7.9% | ~$3.29 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (32,907 resting) | ~7.5% | ~$3.13 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $250.00 ÷ 3 | 0.30 | 10,000 | BUY side (31,049 resting) | ~7.5% | ~$3.12 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (68,727 resting) | ~4.9% | ~$3.08 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $250.00 ÷ 2 | 0.30 | 10,000 | BUY side (76,002 resting) | ~3.8% | ~$2.40 |
| `apdc-jerpowgov-2026-07-31` | $250.00 ÷ 3 | 0.30 | 10,000 | SELL side (22,552 resting) | ~4.5% | ~$1.88 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $142.35 |
| Skipped | $1.21 |
| **Total earned** | **$299.40** |

186 reward rows · 18 days with rewards · 69 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-20 | $106.54 | `████████████████████` |
| 2026-07-19 | $35.81 | `███████` |
| 2026-07-18 | $44.41 | `████████` |
| 2026-07-17 | $14.71 | `███` |
| 2026-07-16 | $17.02 | `███` |
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `██` |
| 2026-07-13 | $10.03 | `██` |
| 2026-07-12 | $39.90 | `███████` |
| 2026-07-11 | $2.11 | `█` |
| 2026-07-10 | $2.16 | `█` |
| 2026-07-09 | $4.72 | `█` |
| 2026-07-08 | $2.68 | `█` |
| 2026-07-07 | $0.14 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $299.40 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.30 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $39.46 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $21.33 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $17.96 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.56 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $16.08 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $14.86 |
| `apdc-jerpowgov-2026-12-31` | $14.76 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $13.59 |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | $13.18 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $7.79 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $6.57 |
| `paccc-usse-midterms-2026-11-03-rep` | $6.29 |
| `enwc-ussep-me-2026-07-27-dem-jargol` | $4.80 |
| `ewc-usgub-ca-2026-11-03-stehil` | $4.70 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-22 2:44 AM ET | ✅ ok | 186 | $299.40 |
| 2026-07-21 11:51 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-21 9:16 PM ET | ✅ ok | 186 | $299.40 |
| 2026-07-21 9:06 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 8:10 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 7:14 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 6:14 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 4:38 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 2:43 PM ET | ✅ ok | 149 | $192.86 |
| 2026-07-21 12:47 PM ET | ✅ ok | 149 | $192.86 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
