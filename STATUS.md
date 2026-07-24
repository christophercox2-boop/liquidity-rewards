# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-24 5:31 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$70.25/day estimated (ceiling, not promise — details below)

**Earned:** $606.98 lifetime ($155.84 paid). Last three recorded days — 2026-07-23: **$133.19** · 2026-07-22: **$82.95** · 2026-07-21: **$91.44** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$9.24/day for 200 contracts. Runners-up: `enwc-usgubp-sd-2026-06-02-rep-larrho` (~$4.96/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$3.52/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$70.25/day (~$2.93/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~79.2% of bid side (2,525 resting ≥ 2,000 ✓) ≈ $4.95/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 20.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~69.0% of ask side (6,513 resting ≥ 2,000 ✓) ≈ $4.31/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 2.0¢ | 400 | 0 | $150.00 | ✅ scoring — ~59.6% of ask side (4,196 resting ≥ 2,000 ✓) ≈ $3.73/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~45.8% of bid side (4,370 resting ≥ 2,000 ✓) ≈ $2.86/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-alawil` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~44.9% of bid side (4,459 resting ≥ 2,000 ✓) ≈ $2.80/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~44.9% of bid side (4,459 resting ≥ 2,000 ✓) ≈ $2.80/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~44.4% of bid side (4,500 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 49.0¢ | 20 | 0 | $150.00 | ✅ scoring — ~44.4% of bid side (2,758 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~38.2% of bid side (5,232 resting ≥ 2,000 ✓) ≈ $2.39/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~33.8% of bid side (5,925 resting ≥ 2,000 ✓) ≈ $2.11/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 22.0¢ | 20 | 1 | $150.00 | ✅ scoring — ~22.0% of ask side (2,287 resting ≥ 2,000 ✓) ≈ $16.52/day |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~13.4% of bid side (14,975 resting ≥ 2,000 ✓) ≈ $0.77/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~12.2% of bid side (16,387 resting ≥ 2,000 ✓) ≈ $0.70/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 24.0¢ | 42 | 3 | $150.00 | ✅ scoring — ~11.6% of ask side (2,287 resting ≥ 2,000 ✓) ≈ $8.68/day |
| `apdc-alito-2026-12-31` | SELL | 17.0¢ | 64 | 0 | $150.00 | ✅ scoring — ~8.8% of ask side (2,479 resting ≥ 2,000 ✓) ≈ $2.19/day (pool ÷ 3 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.4% of ask side (3,013 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.4% of ask side (3,013 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.4% of ask side (3,013 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.4% of ask side (3,013 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.4% of ask side (3,013 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.4% of ask side (3,013 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.4% of ask side (3,013 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.4% of ask side (3,013 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.4% of ask side (3,013 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~7.5% of ask side (118,146 resting ≥ 2,000 ✓) ≈ $0.43/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~7.4% of ask side (167,831 resting ≥ 2,000 ✓) ≈ $0.43/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~7.4% of ask side (232,489 resting ≥ 2,000 ✓) ≈ $0.43/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~7.4% of ask side (119,339 resting ≥ 2,000 ✓) ≈ $0.43/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~7.0% of ask side (196,360 resting ≥ 2,000 ✓) ≈ $0.40/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 48.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~6.5% of ask side (115,260 resting ≥ 2,000 ✓) ≈ $0.38/day (pool ÷ 13 markets) |
| …and 54 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-sc-2026-08-11-rep-paudan</code> BUY 2,000 @ 1¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,525 (2,000 yours) | ×0.5^0 = 2,525.0 |
| | | **Σ** | **2,525.0** |

`yours 2,000.0 / Σ 2,525.0 = 79.2%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 79.2% = $4.95/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan` ← this one
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 100 @ 20¢ → $4.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 145 (100 yours) | ×0.5^0 = 145.0 |
|  | 50¢ | 25 | ×0.5^30 = 0.0 |
|  | 71¢ | 205 | ×0.5^51 = 0.0 |
|  | 74¢ | 657 | ×0.5^54 = 0.0 |
|  | 99¢ | 5,481 | ×0.5^79 = 0.0 |
| | | **Σ** | **145.0** |

`yours 100.0 / Σ 145.0 = 69.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 69.0% = $4.31/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 400 @ 2¢ → $3.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 671 (400 yours) | ×0.5^0 = 671.0 |
|  | 50¢ | 25 | ×0.5^48 = 0.0 |
|  | 99¢ | 3,500 | ×0.5^97 = 0.0 |
| | | **Σ** | **671.0** |

`yours 400.0 / Σ 671.0 = 59.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 59.6% = $3.73/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> BUY 2,000 @ 1¢ → $2.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,370 (2,000 yours) | ×0.5^0 = 4,370.0 |
| | | **Σ** | **4,370.0** |

`yours 2,000.0 / Σ 4,370.0 = 45.8%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 45.8% = $2.86/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil` ← this one
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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-alawil</code> BUY 2,000 @ 1¢ → $2.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,459 (2,000 yours) | ×0.5^0 = 4,459.0 |
| | | **Σ** | **4,459.0** |

`yours 2,000.0 / Σ 4,459.0 = 44.9%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 44.9% = $2.80/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil` ← this one
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-andbau</code> BUY 2,000 @ 1¢ → $2.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,459 (2,000 yours) | ×0.5^0 = 4,459.0 |
| | | **Σ** | **4,459.0** |

`yours 2,000.0 / Σ 4,459.0 = 44.9%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 44.9% = $2.80/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau` ← this one
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> BUY 2,000 @ 1¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 4,500 (2,000 yours) | ×0.5^0 = 4,500.0 |
| | | **Σ** | **4,500.0** |

`yours 2,000.0 / Σ 4,500.0 = 44.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 44.4% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 20 @ 49¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 45 (20 yours) | ×0.5^0 = 45.0 |
|  | 1¢ | 2,713 | ×0.5^48 = 0.0 |
| | | **Σ** | **45.0** |

`yours 20.0 / Σ 45.0 = 44.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 44.4% = $2.78/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-nanmac</code> BUY 2,000 @ 1¢ → $2.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,232 (2,000 yours) | ×0.5^0 = 5,232.0 |
| | | **Σ** | **5,232.0** |

`yours 2,000.0 / Σ 5,232.0 = 38.2%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 38.2% = $2.39/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-wiltim</code> BUY 2,000 @ 1¢ → $2.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 5,925 (2,000 yours) | ×0.5^0 = 5,925.0 |
| | | **Σ** | **5,925.0** |

`yours 2,000.0 / Σ 5,925.0 = 33.8%`  
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
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim` ← this one

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 20 @ 22¢ → $16.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 17 | ×0.5^0 = 17.0 |
| ▶ | 22¢ | 36 (20 yours) | ×0.5^1 = 18.0 |
|  | 24¢ | 83 | ×0.5^3 = 10.4 |
|  | 32¢ | 58 | ×0.5^11 = 0.0 |
|  | 55¢ | 100 | ×0.5^34 = 0.0 |
|  | 99¢ | 1,993 | ×0.5^78 = 0.0 |
| | | **Σ** | **45.4** |

`yours 10.0 / Σ 45.4 = 22.0%`  
`$150 ÷ 1 ÷ 2 = $75.00 × 22.0% = $16.52/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 2,000 @ 1¢ → $0.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 14,975 (2,000 yours) | ×0.5^0 = 14,975.0 |
| | | **Σ** | **14,975.0** |

`yours 2,000.0 / Σ 14,975.0 = 13.4%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 13.4% = $0.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 2,000 @ 1¢ → $0.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 16,387 (2,000 yours) | ×0.5^0 = 16,387.0 |
| | | **Σ** | **16,387.0** |

`yours 2,000.0 / Σ 16,387.0 = 12.2%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 12.2% = $0.70/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 42 @ 24¢ → $8.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 17 | ×0.5^0 = 17.0 |
|  | 22¢ | 36 | ×0.5^1 = 18.0 |
| ▶ | 24¢ | 83 (42 yours) | ×0.5^3 = 10.4 |
|  | 32¢ | 58 | ×0.5^11 = 0.0 |
|  | 55¢ | 100 | ×0.5^34 = 0.0 |
|  | 99¢ | 1,993 | ×0.5^78 = 0.0 |
| | | **Σ** | **45.4** |

`yours 5.3 / Σ 45.4 = 11.6%`  
`$150 ÷ 1 ÷ 2 = $75.00 × 11.6% = $8.68/day`  

</details>
<details><summary><code>apdc-alito-2026-12-31</code> SELL 64 @ 17¢ → $2.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 727 (64 yours) | ×0.5^0 = 726.8 |
|  | 50¢ | 250 | ×0.5^33 = 0.0 |
|  | 80¢ | 5 | ×0.5^63 = 0.0 |
|  | 81¢ | 5 | ×0.5^64 = 0.0 |
|  | 82¢ | 5 | ×0.5^65 = 0.0 |
|  | 99¢ | 1,487 | ×0.5^82 = 0.0 |
| | | **Σ** | **726.8** |

`yours 63.8 / Σ 726.8 = 8.8%`  
`$150 ÷ 3 ÷ 2 = $25.00 × 8.8% = $2.19/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-alito-2026-07-31`
2. `apdc-alito-2026-08-31`
3. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,220 (136 yours) | ×0.5^0 = 1,220.5 |
|  | 98¢ | 793 | ×0.5^1 = 396.5 |
| | | **Σ** | **1,617.0** |

`yours 135.6 / Σ 1,617.0 = 8.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.4% = $0.52/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,220 (136 yours) | ×0.5^0 = 1,220.5 |
|  | 98¢ | 793 | ×0.5^1 = 396.5 |
| | | **Σ** | **1,617.0** |

`yours 135.6 / Σ 1,617.0 = 8.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.4% = $0.52/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,220 (136 yours) | ×0.5^0 = 1,220.5 |
|  | 98¢ | 793 | ×0.5^1 = 396.5 |
| | | **Σ** | **1,617.0** |

`yours 135.6 / Σ 1,617.0 = 8.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.4% = $0.52/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,220 (136 yours) | ×0.5^0 = 1,220.5 |
|  | 98¢ | 793 | ×0.5^1 = 396.5 |
| | | **Σ** | **1,617.0** |

`yours 135.6 / Σ 1,617.0 = 8.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.4% = $0.52/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,220 (136 yours) | ×0.5^0 = 1,220.5 |
|  | 98¢ | 793 | ×0.5^1 = 396.5 |
| | | **Σ** | **1,617.0** |

`yours 135.6 / Σ 1,617.0 = 8.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.4% = $0.52/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,220 (136 yours) | ×0.5^0 = 1,220.5 |
|  | 98¢ | 793 | ×0.5^1 = 396.5 |
| | | **Σ** | **1,617.0** |

`yours 135.6 / Σ 1,617.0 = 8.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.4% = $0.52/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,220 (136 yours) | ×0.5^0 = 1,220.5 |
|  | 98¢ | 793 | ×0.5^1 = 396.5 |
| | | **Σ** | **1,617.0** |

`yours 135.6 / Σ 1,617.0 = 8.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.4% = $0.52/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,220 (136 yours) | ×0.5^0 = 1,220.5 |
|  | 98¢ | 793 | ×0.5^1 = 396.5 |
| | | **Σ** | **1,617.0** |

`yours 135.6 / Σ 1,617.0 = 8.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.4% = $0.52/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,220 (136 yours) | ×0.5^0 = 1,220.5 |
|  | 98¢ | 793 | ×0.5^1 = 396.5 |
| | | **Σ** | **1,617.0** |

`yours 135.6 / Σ 1,617.0 = 8.4%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.4% = $0.52/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 100 @ 49¢ → $0.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,327 (100 yours) | ×0.5^0 = 1,327.0 |
|  | 99¢ | 116,819 | ×0.5^50 = 0.0 |
| | | **Σ** | **1,327.0** |

`yours 100.0 / Σ 1,327.0 = 7.5%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 7.5% = $0.43/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 100 @ 49¢ → $0.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,351 (100 yours) | ×0.5^0 = 1,351.0 |
|  | 98¢ | 153,979 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,351.0** |

`yours 100.0 / Σ 1,351.0 = 7.4%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 7.4% = $0.43/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 100 @ 49¢ → $0.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,352 (100 yours) | ×0.5^0 = 1,352.0 |
|  | 99¢ | 231,137 | ×0.5^50 = 0.0 |
| | | **Σ** | **1,352.0** |

`yours 100.0 / Σ 1,352.0 = 7.4%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 7.4% = $0.43/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 100 @ 49¢ → $0.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,354 (100 yours) | ×0.5^0 = 1,354.0 |
|  | 98¢ | 115,484 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,354.0** |

`yours 100.0 / Σ 1,354.0 = 7.4%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 7.4% = $0.43/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 100 @ 49¢ → $0.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,427 (100 yours) | ×0.5^0 = 1,427.0 |
|  | 98¢ | 115,484 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,427.0** |

`yours 100.0 / Σ 1,427.0 = 7.0%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 7.0% = $0.40/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 100 @ 48¢ → $0.38/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 1,470 (100 yours) | ×0.5^0 = 1,470.0 |
|  | 50¢ | 263 | ×0.5^2 = 65.8 |
|  | 97¢ | 100,026 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,535.8** |

`yours 100.0 / Σ 1,535.8 = 6.5%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 6.5% = $0.38/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-23 | ~$136.30 | $133.19 | 98% |
| 2026-07-22 | ~$110.63 | $82.95 | 75% |
| 2026-07-21 | ~$87.94 | $91.44 | 104% |

Biggest gaps on 2026-07-23: `scc-hrep-rep-2026-11-03-gte210` (est ~$2.21 → got $0.00), `scc-senate-gop-2026-11-03-55` (est ~$2.14 → got $0.00), `opdc-trump-resig-2027-12-31` (est ~$2.12 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ga-2026-11-03-dem` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (3,571 resting) | ~24.6% | ~$9.24 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (34,072 resting) | ~13.2% | ~$4.96 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (59,290 resting) | ~9.4% | ~$3.52 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (7,616 resting) | ~9.3% | ~$3.50 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $150.00 ÷ 3 | 0.50 | 2,000 | SELL side (2,755 resting) | ~14.0% | ~$3.50 |
| `ewc-usgub-ga-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (71,098 resting) | ~7.9% | ~$2.96 |
| `ewc-usgub-ks-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (118,694 resting) | ~6.5% | ~$2.43 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (8,902 resting) | ~5.6% | ~$2.10 |
| `ewc-usgub-ks-2026-11-03-dem` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (80,996 resting) | ~5.4% | ~$2.02 |
| `ewc-usgub-ia-2026-11-03-dem` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (51,473 resting) | ~4.7% | ~$1.78 |
| `ewc-usgub-mi-2026-11-03-dem` | $150.00 ÷ 3 | 0.50 | 2,000 | SELL side (6,976 resting) | ~5.9% | ~$1.48 |
| `ewc-usgub-ia-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (48,922 resting) | ~2.9% | ~$1.10 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $449.93 |
| Skipped | $1.21 |
| **Total earned** | **$606.98** |

257 reward rows · 21 days with rewards · 79 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-23 | $133.19 | `████████████████████` |
| 2026-07-22 | $82.95 | `████████████` |
| 2026-07-21 | $91.44 | `██████████████` |
| 2026-07-20 | $106.54 | `████████████████` |
| 2026-07-19 | $35.81 | `█████` |
| 2026-07-18 | $44.41 | `███████` |
| 2026-07-17 | $14.71 | `██` |
| 2026-07-16 | $17.02 | `███` |
| 2026-07-15 | $1.53 | `█` |
| 2026-07-14 | $13.16 | `██` |
| 2026-07-13 | $10.03 | `██` |
| 2026-07-12 | $39.90 | `██████` |
| 2026-07-11 | $2.11 | `█` |
| 2026-07-10 | $2.16 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $606.98 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $56.41 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $43.94 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $36.49 |
| `apdc-jerpowgov-2026-12-31` | $26.93 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $26.68 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $23.68 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $21.84 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $21.56 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $19.23 |
| `enwc-ussep-nh-2026-09-08-dem-chrpap` | $18.02 |
| `enwc-ussep-nh-2026-09-01-rep-scobro` | $17.30 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $16.88 |
| `enwc-ussep-me-2026-07-27-dem-nirsha` | $16.58 |
| `enwc-usgubp-wi-2026-08-11-dem-frahon` | $14.80 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-24 5:31 PM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 3:50 PM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 1:55 PM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 11:47 AM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 10:16 AM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 9:26 AM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 7:57 AM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 5:38 AM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 2:42 AM ET | ❌ error | 257 | $606.98 |
| 2026-07-23 11:48 PM ET | ✅ ok | 257 | $606.98 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
