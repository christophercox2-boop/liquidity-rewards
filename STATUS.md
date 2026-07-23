# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-23 6:17 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$57.60/day estimated (ceiling, not promise — details below)

**Earned:** $390.84 lifetime ($155.84 paid). Last three recorded days — 2026-07-21: **$91.44** · 2026-07-20: **$106.54** · 2026-07-19: **$35.81** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — SELL at the best price, ~$4.62/day for 200 contracts. Runners-up: `enwc-usgubp-sd-2026-06-02-rep-larrho` (~$3.62/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$3.00/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$57.60/day (~$2.40/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 1.0¢ | 10,000 | 1 | $150.00 | ✅ scoring — ~96.6% of bid side (10,303 resting ≥ 2,000 ✓) ≈ $7.24/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | BUY | 1.0¢ | 10,000 | 0 | $150.00 | ✅ scoring — ~78.1% of bid side (12,803 resting ≥ 2,000 ✓) ≈ $5.86/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste10-15` | BUY | 1.0¢ | 9,990 | 1 | $150.00 | ✅ scoring — ~75.8% of bid side (12,956 resting ≥ 2,000 ✓) ≈ $5.68/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | BUY | 1.0¢ | 10,000 | 0 | $150.00 | ✅ scoring — ~73.9% of bid side (13,523 resting ≥ 2,000 ✓) ≈ $5.55/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | BUY | 1.0¢ | 10,000 | 1 | $150.00 | ✅ scoring — ~70.3% of bid side (13,379 resting ≥ 2,000 ✓) ≈ $5.27/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 1.0¢ | 10,000 | 4 | $150.00 | ✅ scoring — ~40.9% of bid side (14,097 resting ≥ 2,000 ✓) ≈ $3.07/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-tregow` | BUY | 1.0¢ | 10,000 | 0 | $150.00 | ✅ scoring — ~33.8% of bid side (29,551 resting ≥ 2,000 ✓) ≈ $2.11/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 89.0¢ | 189 | 0 | $150.00 | ✅ scoring — ~29.7% of ask side (3,109 resting ≥ 2,000 ✓) ≈ $1.86/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~28.7% of bid side (2,823 resting ≥ 2,000 ✓) ≈ $1.80/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~28.6% of bid side (2,825 resting ≥ 2,000 ✓) ≈ $1.79/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~28.0% of bid side (2,832 resting ≥ 2,000 ✓) ≈ $1.75/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | BUY | 20.0¢ | 200 | 3 | $150.00 | ✅ scoring — ~24.4% of bid side (10,753 resting ≥ 2,000 ✓) ≈ $1.52/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 38.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~17.9% of bid side (3,034 resting ≥ 2,000 ✓) ≈ $1.12/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-rusfry` | BUY | 6.0¢ | 400 | 0 | $150.00 | ✅ scoring — ~17.2% of bid side (12,990 resting ≥ 2,000 ✓) ≈ $1.07/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 40.0¢ | 9 | 0 | $150.00 | ✅ scoring — ~17.0% of ask side (11,981 resting ≥ 2,000 ✓) ≈ $1.28/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 4.0¢ | 500 | 1 | $150.00 | ✅ scoring — ~16.4% of bid side (14,097 resting ≥ 2,000 ✓) ≈ $1.23/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~16.0% of bid side (3,001 resting ≥ 2,000 ✓) ≈ $1.00/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | SELL | 19.0¢ | 75 | 0 | $150.00 | ✅ scoring — ~12.4% of ask side (4,089 resting ≥ 2,000 ✓) ≈ $3.09/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~8.2% of ask side (12,347 resting ≥ 2,000 ✓) ≈ $0.48/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~8.1% of ask side (12,370 resting ≥ 2,000 ✓) ≈ $0.47/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~7.8% of ask side (12,420 resting ≥ 2,000 ✓) ≈ $0.45/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~7.7% of ask side (12,433 resting ≥ 2,000 ✓) ≈ $0.44/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~6.6% of ask side (12,658 resting ≥ 2,000 ✓) ≈ $0.38/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~6.0% of ask side (12,803 resting ≥ 2,000 ✓) ≈ $0.35/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~5.9% of ask side (12,818 resting ≥ 2,000 ✓) ≈ $0.34/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~5.7% of ask side (12,898 resting ≥ 2,000 ✓) ≈ $0.33/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 40.0¢ | 10 | 0 | $150.00 | ✅ scoring — ~3.2% of ask side (2,610 resting ≥ 2,000 ✓) ≈ $0.24/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 3.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~3.1% of bid side (14,860 resting ≥ 2,000 ✓) ≈ $0.20/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 99.0¢ | 170 | 0 | $150.00 | ✅ scoring — ~2.0% of ask side (8,502 resting ≥ 2,000 ✓) ≈ $0.12/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | SELL | 99.0¢ | 170 | 0 | $150.00 | ✅ scoring — ~2.0% of ask side (8,502 resting ≥ 2,000 ✓) ≈ $0.12/day (pool ÷ 12 markets) |
| …and 100 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 10,000 @ 1¢ → $7.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 53 | ×0.5^0 = 53.0 |
| ▶ | 1¢ | 10,250 (10,000 yours) | ×0.5^1 = 5,125.0 |
| | | **Σ** | **5,178.0** |

`yours 5,000.0 / Σ 5,178.0 = 96.6%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 96.6% = $7.24/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> BUY 10,000 @ 1¢ → $5.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,803 (10,000 yours) | ×0.5^0 = 12,803.0 |
| | | **Σ** | **12,803.0** |

`yours 10,000.0 / Σ 12,803.0 = 78.1%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 78.1% = $5.86/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10` ← this one
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste10-15</code> BUY 9,990 @ 1¢ → $5.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 226 | ×0.5^0 = 226.0 |
| ▶ | 1¢ | 12,730 (9,990 yours) | ×0.5^1 = 6,365.0 |
| | | **Σ** | **6,591.0** |

`yours 4,995.0 / Σ 6,591.0 = 75.8%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 75.8% = $5.68/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> BUY 10,000 @ 1¢ → $5.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 13,523 (10,000 yours) | ×0.5^0 = 13,523.0 |
| | | **Σ** | **13,523.0** |

`yours 10,000.0 / Σ 13,523.0 = 73.9%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 73.9% = $5.55/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> BUY 10,000 @ 1¢ → $5.27/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 854 | ×0.5^0 = 854.0 |
| ▶ | 1¢ | 12,525 (10,000 yours) | ×0.5^1 = 6,262.5 |
| | | **Σ** | **7,116.5** |

`yours 5,000.0 / Σ 7,116.5 = 70.3%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 70.3% = $5.27/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 10,000 @ 1¢ → $3.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 74 | ×0.5^0 = 74.0 |
|  | 4¢ | 1,320 | ×0.5^1 = 660.0 |
| ▶ | 1¢ | 12,703 (10,000 yours) | ×0.5^4 = 793.9 |
| | | **Σ** | **1,527.9** |

`yours 625.0 / Σ 1,527.9 = 40.9%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 40.9% = $3.07/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-tregow</code> BUY 10,000 @ 1¢ → $2.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 29,551 (10,000 yours) | ×0.5^0 = 29,551.0 |
| | | **Σ** | **29,551.0** |

`yours 10,000.0 / Σ 29,551.0 = 33.8%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 33.8% = $2.11/day`  

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
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow` ← this one
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 189 @ 89¢ → $1.86/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 89¢ | 634 (189 yours) | ×0.5^0 = 634.2 |
|  | 99¢ | 2,475 | ×0.5^10 = 2.4 |
| | | **Σ** | **636.6** |

`yours 189.2 / Σ 636.6 = 29.7%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 29.7% = $1.86/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 100 @ 49¢ → $1.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 348 (100 yours) | ×0.5^0 = 348.0 |
|  | 1¢ | 2,475 | ×0.5^48 = 0.0 |
| | | **Σ** | **348.0** |

`yours 100.0 / Σ 348.0 = 28.7%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 28.7% = $1.80/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 100 @ 49¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 350 (100 yours) | ×0.5^0 = 350.0 |
|  | 1¢ | 2,475 | ×0.5^48 = 0.0 |
| | | **Σ** | **350.0** |

`yours 100.0 / Σ 350.0 = 28.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 28.6% = $1.79/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 100 @ 49¢ → $1.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 357 (100 yours) | ×0.5^0 = 357.0 |
|  | 1¢ | 2,475 | ×0.5^48 = 0.0 |
| | | **Σ** | **357.0** |

`yours 100.0 / Σ 357.0 = 28.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 28.0% = $1.75/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> BUY 200 @ 20¢ → $1.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 36 | ×0.5^0 = 36.0 |
| ▶ | 20¢ | 529 (200 yours) | ×0.5^3 = 66.1 |
|  | 15¢ | 133 | ×0.5^8 = 0.5 |
|  | 14¢ | 1 | ×0.5^9 = 0.0 |
|  | 1¢ | 10,054 | ×0.5^22 = 0.0 |
| | | **Σ** | **102.6** |

`yours 25.0 / Σ 102.6 = 24.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 24.4% = $1.52/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 100 @ 38¢ → $1.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 559 (100 yours) | ×0.5^0 = 559.0 |
|  | 1¢ | 2,475 | ×0.5^37 = 0.0 |
| | | **Σ** | **559.0** |

`yours 100.0 / Σ 559.0 = 17.9%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 17.9% = $1.12/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-rusfry</code> BUY 400 @ 6¢ → $1.07/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 1,668 (400 yours) | ×0.5^0 = 1,668.0 |
|  | 5¢ | 1,321 | ×0.5^1 = 660.5 |
| | | **Σ** | **2,328.5** |

`yours 400.0 / Σ 2,328.5 = 17.2%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 17.2% = $1.07/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 9 @ 40¢ → $1.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 22 (9 yours) | ×0.5^0 = 22.0 |
|  | 44¢ | 149 | ×0.5^4 = 9.3 |
|  | 45¢ | 68 | ×0.5^5 = 2.1 |
|  | 46¢ | 1,246 | ×0.5^6 = 19.5 |
|  | 99¢ | 10,496 | ×0.5^59 = 0.0 |
| | | **Σ** | **52.9** |

`yours 9.0 / Σ 52.9 = 17.0%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 17.0% = $1.28/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 500 @ 4¢ → $1.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 74 | ×0.5^0 = 74.0 |
| ▶ | 4¢ | 1,320 (500 yours) | ×0.5^1 = 660.0 |
|  | 1¢ | 12,703 | ×0.5^4 = 793.9 |
| | | **Σ** | **1,527.9** |

`yours 250.0 / Σ 1,527.9 = 16.4%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 16.4% = $1.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 100 @ 49¢ → $1.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 626 (100 yours) | ×0.5^0 = 626.0 |
|  | 1¢ | 2,375 | ×0.5^48 = 0.0 |
| | | **Σ** | **626.0** |

`yours 100.0 / Σ 626.0 = 16.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 16.0% = $1.00/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 75 @ 19¢ → $3.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 602 (75 yours) | ×0.5^0 = 602.0 |
|  | 26¢ | 587 | ×0.5^7 = 4.6 |
|  | 44¢ | 50 | ×0.5^25 = 0.0 |
|  | 50¢ | 250 | ×0.5^31 = 0.0 |
|  | 52¢ | 50 | ×0.5^33 = 0.0 |
|  | 59¢ | 50 | ×0.5^40 = 0.0 |
|  | 99¢ | 2,500 | ×0.5^80 = 0.0 |
| | | **Σ** | **606.6** |

`yours 75.0 / Σ 606.6 = 12.4%`  
`$150 ÷ 3 ÷ 2 = $25.00 × 12.4% = $3.09/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-alito-2026-07-31`
2. `apdc-alito-2026-08-31`
3. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 100 @ 49¢ → $0.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,083 (100 yours) | ×0.5^0 = 1,083.0 |
|  | 50¢ | 263 | ×0.5^1 = 131.5 |
|  | 98¢ | 1,000 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,214.5** |

`yours 100.0 / Σ 1,214.5 = 8.2%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 8.2% = $0.48/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 100 @ 49¢ → $0.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,103 (100 yours) | ×0.5^0 = 1,103.0 |
|  | 50¢ | 266 | ×0.5^1 = 133.0 |
|  | 98¢ | 1,000 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,236.0** |

`yours 100.0 / Σ 1,236.0 = 8.1%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 8.1% = $0.47/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 100 @ 49¢ → $0.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,153 (100 yours) | ×0.5^0 = 1,153.0 |
|  | 50¢ | 266 | ×0.5^1 = 133.0 |
|  | 98¢ | 1,000 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,286.0** |

`yours 100.0 / Σ 1,286.0 = 7.8%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 7.8% = $0.45/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 100 @ 49¢ → $0.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,169 (100 yours) | ×0.5^0 = 1,169.0 |
|  | 50¢ | 263 | ×0.5^1 = 131.5 |
|  | 98¢ | 1,000 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,300.5** |

`yours 100.0 / Σ 1,300.5 = 7.7%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 7.7% = $0.44/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 100 @ 49¢ → $0.38/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,391 (100 yours) | ×0.5^0 = 1,391.0 |
|  | 50¢ | 266 | ×0.5^1 = 133.0 |
|  | 98¢ | 1,000 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,524.0** |

`yours 100.0 / Σ 1,524.0 = 6.6%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 6.6% = $0.38/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 100 @ 49¢ → $0.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,536 (100 yours) | ×0.5^0 = 1,536.0 |
|  | 50¢ | 266 | ×0.5^1 = 133.0 |
|  | 98¢ | 1,000 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,669.0** |

`yours 100.0 / Σ 1,669.0 = 6.0%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 6.0% = $0.35/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 100 @ 49¢ → $0.34/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,551 (100 yours) | ×0.5^0 = 1,551.0 |
|  | 50¢ | 266 | ×0.5^1 = 133.0 |
|  | 98¢ | 1,000 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,684.0** |

`yours 100.0 / Σ 1,684.0 = 5.9%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 5.9% = $0.34/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 100 @ 49¢ → $0.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,634 (100 yours) | ×0.5^0 = 1,634.0 |
|  | 50¢ | 263 | ×0.5^1 = 131.5 |
|  | 98¢ | 1,000 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,765.5** |

`yours 100.0 / Σ 1,765.5 = 5.7%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 5.7% = $0.33/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 10 @ 40¢ → $0.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 38 (10 yours) | ×0.5^0 = 38.0 |
|  | 41¢ | 105 | ×0.5^1 = 52.5 |
|  | 42¢ | 91 | ×0.5^2 = 22.8 |
|  | 43¢ | 1,558 | ×0.5^3 = 194.8 |
|  | 45¢ | 68 | ×0.5^5 = 2.1 |
|  | 55¢ | 250 | ×0.5^15 = 0.0 |
| | | **Σ** | **310.1** |

`yours 10.0 / Σ 310.1 = 3.2%`  
`$150 ÷ 10 ÷ 2 = $7.50 × 3.2% = $0.24/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> BUY 100 @ 3¢ → $0.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 1,533 (100 yours) | ×0.5^0 = 1,533.0 |
|  | 2¢ | 3,302 | ×0.5^1 = 1,651.0 |
| | | **Σ** | **3,184.0** |

`yours 100.0 / Σ 3,184.0 = 3.1%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 3.1% = $0.20/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn` ← this one
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 170 @ 99¢ → $0.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 8,502 (170 yours) | ×0.5^0 = 8,501.5 |
| | | **Σ** | **8,501.5** |

`yours 170.0 / Σ 8,501.5 = 2.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 2.0% = $0.12/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> SELL 170 @ 99¢ → $0.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 8,502 (170 yours) | ×0.5^0 = 8,501.5 |
| | | **Σ** | **8,501.5** |

`yours 170.0 / Σ 8,501.5 = 2.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 2.0% = $0.12/day`  

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
| 2026-07-21 | ~$87.94 | $91.44 | 104% |
| 2026-07-20 | ~$125.00 | $106.54 | 85% |
| 2026-07-19 | ~$36.97 | $35.81 | 97% |

Biggest gaps on 2026-07-21: `apdc-alito-2026-08-31` (est ~$2.10 → got $0.00), `enwc-ussep-sc-2026-08-11-rep-darnor` (est ~$2.07 → got $0.00), `enwc-ushrp-mo01-2026-08-04-dem-corbus` (est ~$1.84 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (9,720 resting) | ~12.3% | ~$4.62 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (87,836 resting) | ~9.6% | ~$3.62 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (38,333 resting) | ~8.0% | ~$3.00 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (101,373 resting) | ~7.8% | ~$2.94 |
| `ewc-usgub-ga-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (103,693 resting) | ~7.7% | ~$2.90 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (79,237 resting) | ~7.1% | ~$2.66 |
| `ewc-usgub-ks-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (274,407 resting) | ~6.7% | ~$2.52 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $150.00 ÷ 3 | 0.50 | 2,000 | SELL side (21,595 resting) | ~9.8% | ~$2.44 |
| `ewc-usgub-ks-2026-11-03-dem` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (192,479 resting) | ~6.4% | ~$2.39 |
| `ewc-usgub-ia-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (136,414 resting) | ~5.4% | ~$2.04 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (47,368 resting) | ~4.4% | ~$1.65 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $150.00 ÷ 3 | 0.50 | 2,000 | BUY side (38,667 resting) | ~6.1% | ~$1.52 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $233.79 |
| Skipped | $1.21 |
| **Total earned** | **$390.84** |

211 reward rows · 19 days with rewards · 71 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-21 | $91.44 | `█████████████████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $390.84 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-ussep-nh-2026-09-08-dem-karman` | $43.94 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $41.68 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $29.71 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $18.83 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $18.02 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $17.30 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.58 |
| `apdc-jerpowgov-2026-12-31` | $14.76 |
| `enwc-ussep-nh-2026-09-01-rep-johsun` | $13.18 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $12.14 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $8.81 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $7.85 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $7.79 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $7.13 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-23 6:17 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 4:43 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 4:32 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 3:02 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 2:40 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 12:49 PM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 10:37 AM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 8:05 AM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 5:40 AM ET | ✅ ok | 211 | $390.84 |
| 2026-07-23 2:42 AM ET | ✅ ok | 211 | $390.84 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
