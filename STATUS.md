# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-24 3:50 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$77.66/day estimated (ceiling, not promise — details below)

**Earned:** $606.98 lifetime ($155.84 paid). Last three recorded days — 2026-07-23: **$133.19** · 2026-07-22: **$82.95** · 2026-07-21: **$91.44** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ga-2026-11-03-dem` — SELL at the best price, ~$24.59/day for 200 contracts. Runners-up: `enwc-ussep-mi-2026-08-04-dem-halste` (~$4.36/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$3.56/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$77.66/day (~$3.24/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~79.2% of bid side (2,525 resting ≥ 2,000 ✓) ≈ $4.95/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~79.2% of bid side (2,525 resting ≥ 2,000 ✓) ≈ $4.95/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~79.2% of bid side (2,525 resting ≥ 2,000 ✓) ≈ $4.95/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~75.5% of bid side (2,649 resting ≥ 2,000 ✓) ≈ $4.72/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~74.0% of bid side (2,703 resting ≥ 2,000 ✓) ≈ $4.62/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-alawil` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~60.6% of bid side (3,303 resting ≥ 2,000 ✓) ≈ $3.78/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 2.0¢ | 400 | 0 | $150.00 | ✅ scoring — ~51.6% of ask side (2,529 resting ≥ 2,000 ✓) ≈ $3.23/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 49.0¢ | 20 | 0 | $150.00 | ✅ scoring — ~29.9% of bid side (2,780 resting ≥ 2,000 ✓) ≈ $1.87/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 25.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~17.0% of ask side (4,048 resting ≥ 2,000 ✓) ≈ $1.06/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~16.0% of bid side (12,475 resting ≥ 2,000 ✓) ≈ $0.92/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~16.0% of bid side (12,475 resting ≥ 2,000 ✓) ≈ $0.92/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 32.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~13.2% of ask side (11,064 resting ≥ 2,000 ✓) ≈ $9.86/day |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 32.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~13.2% of ask side (11,064 resting ≥ 2,000 ✓) ≈ $9.86/day |
| `pvwc-housepopw-2026-11-03-rep` | SELL | 17.0¢ | 64 | 0 | $150.00 | ✅ scoring — ~9.9% of ask side (6,054 resting ≥ 2,000 ✓) ≈ $3.72/day (pool ÷ 2 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.6% of ask side (2,320 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.6% of ask side (2,320 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.6% of ask side (2,320 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.6% of ask side (2,320 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.6% of ask side (2,320 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.6% of ask side (2,320 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.6% of ask side (2,320 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.6% of ask side (2,320 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | SELL | 97.0¢ | 136 | 0 | $150.00 | ✅ scoring — ~8.6% of ask side (2,320 resting ≥ 2,000 ✓) ≈ $0.54/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~6.4% of ask side (117,041 resting ≥ 2,000 ✓) ≈ $0.37/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~6.4% of ask side (165,554 resting ≥ 2,000 ✓) ≈ $0.37/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~6.3% of ask side (230,212 resting ≥ 2,000 ✓) ≈ $0.37/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 48.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~6.2% of ask side (112,834 resting ≥ 2,000 ✓) ≈ $0.36/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 49.0¢ | 100 | 0 | $150.00 | ✅ scoring — ~6.2% of ask side (115,937 resting ≥ 2,000 ✓) ≈ $0.36/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 1.0¢ | 2,000 | 0 | $150.00 | ✅ scoring — ~6.2% of bid side (32,475 resting ≥ 2,000 ✓) ≈ $0.36/day (pool ÷ 13 markets) |
| …and 50 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> BUY 2,000 @ 1¢ → $6.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.5^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-nanmac</code> BUY 2,000 @ 1¢ → $4.95/day</summary>

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
6. `enwc-ussep-sc-2026-08-11-rep-nanmac` ← this one
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-wiltim</code> BUY 2,000 @ 1¢ → $4.95/day</summary>

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
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> BUY 2,000 @ 1¢ → $4.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,649 (2,000 yours) | ×0.5^0 = 2,649.0 |
| | | **Σ** | **2,649.0** |

`yours 2,000.0 / Σ 2,649.0 = 75.5%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 75.5% = $4.72/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-andbau</code> BUY 2,000 @ 1¢ → $4.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,703 (2,000 yours) | ×0.5^0 = 2,703.0 |
| | | **Σ** | **2,703.0** |

`yours 2,000.0 / Σ 2,703.0 = 74.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 74.0% = $4.62/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-alawil</code> BUY 2,000 @ 1¢ → $3.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 3,303 (2,000 yours) | ×0.5^0 = 3,303.0 |
| | | **Σ** | **3,303.0** |

`yours 2,000.0 / Σ 3,303.0 = 60.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 60.6% = $3.78/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 400 @ 2¢ → $3.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 775 (400 yours) | ×0.5^0 = 775.0 |
|  | 50¢ | 25 | ×0.5^48 = 0.0 |
|  | 99¢ | 1,729 | ×0.5^97 = 0.0 |
| | | **Σ** | **775.0** |

`yours 400.0 / Σ 775.0 = 51.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 51.6% = $3.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 20 @ 49¢ → $1.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 67 (20 yours) | ×0.5^0 = 67.0 |
|  | 1¢ | 2,713 | ×0.5^48 = 0.0 |
| | | **Σ** | **67.0** |

`yours 20.0 / Σ 67.0 = 29.9%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 29.9% = $1.87/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 100 @ 25¢ → $1.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 587 (100 yours) | ×0.5^0 = 587.0 |
|  | 50¢ | 25 | ×0.5^25 = 0.0 |
|  | 71¢ | 205 | ×0.5^46 = 0.0 |
|  | 74¢ | 250 | ×0.5^49 = 0.0 |
|  | 99¢ | 2,981 | ×0.5^74 = 0.0 |
| | | **Σ** | **587.0** |

`yours 100.0 / Σ 587.0 = 17.0%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 17.0% = $1.06/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 2,000 @ 1¢ → $0.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,475 (2,000 yours) | ×0.5^0 = 12,475.0 |
| | | **Σ** | **12,475.0** |

`yours 2,000.0 / Σ 12,475.0 = 16.0%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 16.0% = $0.92/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 2,000 @ 1¢ → $0.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,475 (2,000 yours) | ×0.5^0 = 12,475.0 |
| | | **Σ** | **12,475.0** |

`yours 2,000.0 / Σ 12,475.0 = 16.0%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 16.0% = $0.92/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 100 @ 32¢ → $9.86/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 748 (100 yours) | ×0.5^0 = 748.0 |
|  | 36¢ | 174 | ×0.5^4 = 10.9 |
|  | 38¢ | 15 | ×0.5^6 = 0.2 |
|  | 40¢ | 27 | ×0.5^8 = 0.1 |
|  | 45¢ | 10,000 | ×0.5^13 = 1.2 |
| | | **Σ** | **760.4** |

`yours 100.0 / Σ 760.4 = 13.2%`  
`$150 ÷ 1 ÷ 2 = $75.00 × 13.2% = $9.86/day`  

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 100 @ 32¢ → $9.86/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 748 (100 yours) | ×0.5^0 = 748.0 |
|  | 36¢ | 174 | ×0.5^4 = 10.9 |
|  | 38¢ | 15 | ×0.5^6 = 0.2 |
|  | 40¢ | 27 | ×0.5^8 = 0.1 |
|  | 45¢ | 10,000 | ×0.5^13 = 1.2 |
| | | **Σ** | **760.4** |

`yours 100.0 / Σ 760.4 = 13.2%`  
`$150 ÷ 1 ÷ 2 = $75.00 × 13.2% = $9.86/day`  

</details>
<details><summary><code>pvwc-housepopw-2026-11-03-rep</code> SELL 64 @ 17¢ → $3.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 533 (64 yours) | ×0.5^0 = 533.2 |
|  | 19¢ | 452 | ×0.5^2 = 113.0 |
|  | 36¢ | 69 | ×0.5^19 = 0.0 |
|  | 99¢ | 5,000 | ×0.5^82 = 0.0 |
| | | **Σ** | **646.2** |

`yours 64.2 / Σ 646.2 = 9.9%`  
`$150 ÷ 2 ÷ 2 = $37.50 × 9.9% = $3.72/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pvwc-housepopw-2026-11-03-dem`
2. `pvwc-housepopw-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,320 (136 yours) | ×0.5^0 = 1,320.5 |
|  | 99¢ | 1,000 | ×0.5^2 = 250.0 |
| | | **Σ** | **1,570.5** |

`yours 135.6 / Σ 1,570.5 = 8.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.6% = $0.54/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,320 (136 yours) | ×0.5^0 = 1,320.5 |
|  | 99¢ | 1,000 | ×0.5^2 = 250.0 |
| | | **Σ** | **1,570.5** |

`yours 135.6 / Σ 1,570.5 = 8.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.6% = $0.54/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,320 (136 yours) | ×0.5^0 = 1,320.5 |
|  | 99¢ | 1,000 | ×0.5^2 = 250.0 |
| | | **Σ** | **1,570.5** |

`yours 135.6 / Σ 1,570.5 = 8.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.6% = $0.54/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,320 (136 yours) | ×0.5^0 = 1,320.5 |
|  | 99¢ | 1,000 | ×0.5^2 = 250.0 |
| | | **Σ** | **1,570.5** |

`yours 135.6 / Σ 1,570.5 = 8.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.6% = $0.54/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,320 (136 yours) | ×0.5^0 = 1,320.5 |
|  | 99¢ | 1,000 | ×0.5^2 = 250.0 |
| | | **Σ** | **1,570.5** |

`yours 135.6 / Σ 1,570.5 = 8.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.6% = $0.54/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,320 (136 yours) | ×0.5^0 = 1,320.5 |
|  | 99¢ | 1,000 | ×0.5^2 = 250.0 |
| | | **Σ** | **1,570.5** |

`yours 135.6 / Σ 1,570.5 = 8.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.6% = $0.54/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,320 (136 yours) | ×0.5^0 = 1,320.5 |
|  | 99¢ | 1,000 | ×0.5^2 = 250.0 |
| | | **Σ** | **1,570.5** |

`yours 135.6 / Σ 1,570.5 = 8.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.6% = $0.54/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,320 (136 yours) | ×0.5^0 = 1,320.5 |
|  | 99¢ | 1,000 | ×0.5^2 = 250.0 |
| | | **Σ** | **1,570.5** |

`yours 135.6 / Σ 1,570.5 = 8.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.6% = $0.54/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-darnor</code> SELL 136 @ 97¢ → $0.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 1,320 (136 yours) | ×0.5^0 = 1,320.5 |
|  | 99¢ | 1,000 | ×0.5^2 = 250.0 |
| | | **Σ** | **1,570.5** |

`yours 135.6 / Σ 1,570.5 = 8.6%`  
`$150 ÷ 12 ÷ 2 = $6.25 × 8.6% = $0.54/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 100 @ 49¢ → $0.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,556 (100 yours) | ×0.5^0 = 1,556.0 |
|  | 98¢ | 115,484 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,556.0** |

`yours 100.0 / Σ 1,556.0 = 6.4%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 6.4% = $0.37/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 100 @ 49¢ → $0.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,574 (100 yours) | ×0.5^0 = 1,574.0 |
|  | 98¢ | 153,979 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,574.0** |

`yours 100.0 / Σ 1,574.0 = 6.4%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 6.4% = $0.37/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 100 @ 49¢ → $0.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,575 (100 yours) | ×0.5^0 = 1,575.0 |
|  | 99¢ | 228,637 | ×0.5^50 = 0.0 |
| | | **Σ** | **1,575.0** |

`yours 100.0 / Σ 1,575.0 = 6.3%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 6.3% = $0.37/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 100 @ 48¢ → $0.36/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 1,544 (100 yours) | ×0.5^0 = 1,544.0 |
|  | 50¢ | 263 | ×0.5^2 = 65.8 |
|  | 97¢ | 100,026 | ×0.5^49 = 0.0 |
| | | **Σ** | **1,609.8** |

`yours 100.0 / Σ 1,609.8 = 6.2%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 6.2% = $0.36/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 100 @ 49¢ → $0.36/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 1,618 (100 yours) | ×0.5^0 = 1,618.0 |
|  | 99¢ | 114,319 | ×0.5^50 = 0.0 |
| | | **Σ** | **1,618.0** |

`yours 100.0 / Σ 1,618.0 = 6.2%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 6.2% = $0.36/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 2,000 @ 1¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 32,475 (2,000 yours) | ×0.5^0 = 32,475.0 |
| | | **Σ** | **32,475.0** |

`yours 2,000.0 / Σ 32,475.0 = 6.2%`  
`$150 ÷ 13 ÷ 2 = $5.77 × 6.2% = $0.36/day`  

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
| `ewc-usgub-ga-2026-11-03-dem` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (2,605 resting) | ~65.6% | ~$24.59 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $150.00 ÷ 3 | 0.50 | 2,000 | BUY side (2,502 resting) | ~17.4% | ~$4.36 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (27,475 resting) | ~9.5% | ~$3.56 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (19,019 resting) | ~9.4% | ~$3.51 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (7,805 resting) | ~8.6% | ~$3.23 |
| `ewc-usgub-ks-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (126,127 resting) | ~7.9% | ~$2.96 |
| `ewc-usgub-ga-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | SELL side (5,796 resting) | ~7.7% | ~$2.90 |
| `ewc-usgub-mi-2026-11-03-dem` | $150.00 ÷ 3 | 0.50 | 2,000 | BUY side (41,505 resting) | ~10.4% | ~$2.60 |
| `ewc-usgub-ia-2026-11-03-rep` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (109,146 resting) | ~6.5% | ~$2.45 |
| `ewc-usgub-ks-2026-11-03-dem` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (96,115 resting) | ~5.7% | ~$2.13 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (3,345 resting) | ~5.6% | ~$2.12 |
| `ewc-usgub-ia-2026-11-03-dem` | $150.00 ÷ 2 | 0.50 | 2,000 | BUY side (47,762 resting) | ~4.4% | ~$1.66 |

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
| 2026-07-24 3:50 PM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 1:55 PM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 11:47 AM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 10:16 AM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 9:26 AM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 7:57 AM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 5:38 AM ET | ✅ ok | 257 | $606.98 |
| 2026-07-24 2:42 AM ET | ❌ error | 257 | $606.98 |
| 2026-07-23 11:48 PM ET | ✅ ok | 257 | $606.98 |
| 2026-07-23 9:18 PM ET | ✅ ok | 257 | $606.98 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
