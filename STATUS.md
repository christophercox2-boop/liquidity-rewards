# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-26 5:15 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$201.28/day estimated (ceiling, not promise — details below)

**Earned:** $836.61 lifetime ($155.84 paid). Last three recorded days — 2026-07-24: **$135.19** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-23: **$227.63** · 2026-07-22: **$82.95** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$13.24/day for 200 contracts. Runners-up: `enwc-usgubp-sd-2026-06-02-rep-tobdoe` (~$7.43/day), `paccc-usse-midterms-2026-11-03-rep` (~$6.38/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$201.28/day (~$8.39/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 50.0¢ | 11 | 0 | $100.00 | ✅ scoring — ~99.0% of ask side (7,603 resting ≥ 2,000 ✓) ≈ $4.95/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-paudan` | BUY | 1.0¢ | 8,155 | 0 | $100.00 | ✅ scoring — ~84.2% of bid side (9,680 resting ≥ 2,000 ✓) ≈ $3.51/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-wiltim` | BUY | 1.0¢ | 8,155 | 0 | $100.00 | ✅ scoring — ~84.2% of bid side (9,680 resting ≥ 2,000 ✓) ≈ $3.51/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 27.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~78.5% of ask side (99,516 resting ≥ 2,000 ✓) ≈ $3.92/day (pool ÷ 10 markets) |
| `nphc-attgen-hardhi` | BUY | 1.0¢ | 8,155 | 0 | $100.00 | ✅ scoring — ~73.4% of bid side (11,105 resting ≥ 2,000 ✓) ≈ $2.29/day (pool ÷ 16 markets) |
| `enwc-ussep-sc-2026-08-11-rep-nanmac` | BUY | 1.0¢ | 8,155 | 0 | $100.00 | ✅ scoring — ~72.9% of bid side (11,180 resting ≥ 2,000 ✓) ≈ $3.04/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | BUY | 1.0¢ | 8,155 | 4 | $100.00 | ✅ scoring — ~69.9% of bid side (8,529 resting ≥ 2,000 ✓) ≈ $2.91/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 15.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~67.9% of ask side (63,735 resting ≥ 2,000 ✓) ≈ $3.39/day (pool ÷ 10 markets) |
| `nphc-attgen-rondes` | BUY | 1.0¢ | 8,155 | 0 | $100.00 | ✅ scoring — ~67.4% of bid side (12,105 resting ≥ 2,000 ✓) ≈ $2.11/day (pool ÷ 16 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 10.0¢ | 53 | 0 | $100.00 | ✅ scoring — ~66.9% of ask side (106,066 resting ≥ 2,000 ✓) ≈ $2.57/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-rusfry` | BUY | 1.0¢ | 8,155 | 1 | $100.00 | ✅ scoring — ~66.7% of bid side (11,438 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 50.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (2,456 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 50.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `apdc-trumpadmin-2026-petheg` | BUY | 26.0¢ | 314 | 2 | $100.00 | ✅ scoring — ~63.7% of bid side (80,592 resting ≥ 2,000 ✓) ≈ $1.87/day (pool ÷ 17 markets) |
| `enwc-ussep-sc-2026-08-11-rep-pameve` | BUY | 1.0¢ | 8,155 | 1 | $100.00 | ✅ scoring — ~63.4% of bid side (12,255 resting ≥ 2,000 ✓) ≈ $2.64/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 50.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~62.5% of bid side (2,500 resting ≥ 2,000 ✓) ≈ $2.60/day (pool ÷ 12 markets) |
| `pintc-meet-trump-2026-12-31-vlaput` | BUY | 21.0¢ | 388 | 3 | $100.00 | ✅ scoring — ~56.4% of bid side (50,628 resting ≥ 2,000 ✓) ≈ $2.17/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-alawil` | BUY | 1.0¢ | 8,155 | 0 | $100.00 | ✅ scoring — ~53.4% of bid side (15,265 resting ≥ 2,000 ✓) ≈ $2.23/day (pool ÷ 12 markets) |
| `enwc-ussep-sc-2026-08-11-rep-andbau` | BUY | 1.0¢ | 8,155 | 0 | $100.00 | ✅ scoring — ~53.4% of bid side (15,265 resting ≥ 2,000 ✓) ≈ $2.23/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 2.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~53.3% of ask side (42,007 resting ≥ 2,000 ✓) ≈ $2.67/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-joewil` | SELL | 20.0¢ | 214 | 1 | $100.00 | ✅ scoring — ~48.7% of ask side (6,499 resting ≥ 2,000 ✓) ≈ $2.03/day (pool ÷ 12 markets) |
| `apdc-trumpadmin-2026-johrat` | BUY | 21.0¢ | 388 | 3 | $100.00 | ✅ scoring — ~43.0% of bid side (50,706 resting ≥ 2,000 ✓) ≈ $1.26/day (pool ÷ 17 markets) |
| `enwc-ussep-sc-2026-08-11-rep-tregow` | BUY | 1.0¢ | 8,155 | 0 | $100.00 | ✅ scoring — ~35.4% of bid side (23,018 resting ≥ 2,000 ✓) ≈ $1.48/day (pool ÷ 12 markets) |
| `apdc-trumpadmin-2026-rodsco` | BUY | 20.0¢ | 408 | 3 | $100.00 | ✅ scoring — ~35.3% of bid side (52,235 resting ≥ 2,000 ✓) ≈ $1.04/day (pool ÷ 17 markets) |
| `cranc-uspres28-12-31-2026-betoro` | BUY | 6.0¢ | 1,359 | 1 | $100.00 | ✅ scoring — ~29.0% of bid side (26,373 resting ≥ 2,000 ✓) ≈ $0.44/day (pool ÷ 33 markets) |
| `pintc-meet-trump-2026-12-31-leoxiv` | BUY | 2.0¢ | 4,077 | 1 | $100.00 | ✅ scoring — ~28.9% of bid side (64,289 resting ≥ 2,000 ✓) ≈ $1.11/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-hilcli` | BUY | 2.0¢ | 4,078 | 1 | $100.00 | ✅ scoring — ~28.7% of bid side (55,332 resting ≥ 2,000 ✓) ≈ $0.44/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-dontru` | BUY | 8.0¢ | 1,019 | 1 | $100.00 | ✅ scoring — ~28.7% of bid side (103,741 resting ≥ 2,000 ✓) ≈ $0.43/day (pool ÷ 33 markets) |
| `pintc-meet-trump-2026-12-31-kimjon` | BUY | 3.0¢ | 2,718 | 3 | $100.00 | ✅ scoring — ~28.6% of bid side (19,620 resting ≥ 2,000 ✓) ≈ $1.10/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-markel` | BUY | 2.0¢ | 4,078 | 1 | $100.00 | ✅ scoring — ~28.4% of bid side (64,534 resting ≥ 2,000 ✓) ≈ $0.43/day (pool ÷ 33 markets) |
| …and 149 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 11 @ 50¢ → $4.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 11 (11 yours) | ×0.5^0 = 11.0 |
|  | 58¢ | 28 | ×0.5^8 = 0.1 |
|  | 99¢ | 7,564 | ×0.5^49 = 0.0 |
| | | **Σ** | **11.1** |

`yours 11.0 / Σ 11.1 = 99.0%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 99.0% = $4.95/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-paudan</code> BUY 8,155 @ 1¢ → $3.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 9,680 (8,155 yours) | ×0.5^0 = 9,680.0 |
| | | **Σ** | **9,680.0** |

`yours 8,155.0 / Σ 9,680.0 = 84.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 84.2% = $3.51/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-wiltim</code> BUY 8,155 @ 1¢ → $3.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 9,680 (8,155 yours) | ×0.5^0 = 9,680.0 |
| | | **Σ** | **9,680.0** |

`yours 8,155.0 / Σ 9,680.0 = 84.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 84.2% = $3.51/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 20 @ 27¢ → $3.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 20 (20 yours) | ×0.5^0 = 20.0 |
|  | 28¢ | 9 | ×0.5^1 = 4.5 |
|  | 32¢ | 28 | ×0.5^5 = 0.9 |
|  | 35¢ | 28 | ×0.5^8 = 0.1 |
|  | 45¢ | 25 | ×0.5^18 = 0.0 |
|  | 98¢ | 98,906 | ×0.5^71 = 0.0 |
| | | **Σ** | **25.5** |

`yours 20.0 / Σ 25.5 = 78.5%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 78.5% = $3.92/day`  

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
<details><summary><code>nphc-attgen-hardhi</code> BUY 8,155 @ 1¢ → $2.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,105 (8,155 yours) | ×0.5^0 = 11,105.0 |
| | | **Σ** | **11,105.0** |

`yours 8,155.0 / Σ 11,105.0 = 73.4%`  
`$100 ÷ 16 ÷ 2 = $3.12 × 73.4% = $2.29/day`  

<details><summary>÷ 16 markets in this race — tap to list</summary>

1. `nphc-attgen-ailcan`
2. `nphc-attgen-alihab`
3. `nphc-attgen-andbai`
4. `nphc-attgen-ashmoo`
5. `nphc-attgen-edmar`
6. `nphc-attgen-hardhi` ← this one
7. `nphc-attgen-jeapir`
8. `nphc-attgen-jefjen`
9. `nphc-attgen-kenpax`
10. `nphc-attgen-leezel`
11. `nphc-attgen-matgae`
12. `nphc-attgen-matwhi`
13. `nphc-attgen-robgiu`
14. `nphc-attgen-rondes`
15. `nphc-attgen-tedcru`
16. `nphc-attgen-todbla`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-nanmac</code> BUY 8,155 @ 1¢ → $3.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,180 (8,155 yours) | ×0.5^0 = 11,180.0 |
| | | **Σ** | **11,180.0** |

`yours 8,155.0 / Σ 11,180.0 = 72.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 72.9% = $3.04/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> BUY 8,155 @ 1¢ → $2.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 66 | ×0.5^0 = 66.0 |
|  | 4¢ | 308 | ×0.5^1 = 154.0 |
| ▶ | 1¢ | 8,155 (8,155 yours) | ×0.5^4 = 509.7 |
| | | **Σ** | **729.7** |

`yours 509.7 / Σ 729.7 = 69.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 69.9% = $2.91/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 20 @ 15¢ → $3.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 29 (20 yours) | ×0.5^0 = 29.0 |
|  | 21¢ | 29 | ×0.5^6 = 0.5 |
|  | 45¢ | 25 | ×0.5^30 = 0.0 |
|  | 97¢ | 56 | ×0.5^82 = 0.0 |
|  | 98¢ | 63,096 | ×0.5^83 = 0.0 |
| | | **Σ** | **29.4** |

`yours 20.0 / Σ 29.4 = 67.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 67.9% = $3.39/day`  

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
<details><summary><code>nphc-attgen-rondes</code> BUY 8,155 @ 1¢ → $2.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,105 (8,155 yours) | ×0.5^0 = 12,105.0 |
| | | **Σ** | **12,105.0** |

`yours 8,155.0 / Σ 12,105.0 = 67.4%`  
`$100 ÷ 16 ÷ 2 = $3.12 × 67.4% = $2.11/day`  

<details><summary>÷ 16 markets in this race — tap to list</summary>

1. `nphc-attgen-ailcan`
2. `nphc-attgen-alihab`
3. `nphc-attgen-andbai`
4. `nphc-attgen-ashmoo`
5. `nphc-attgen-edmar`
6. `nphc-attgen-hardhi`
7. `nphc-attgen-jeapir`
8. `nphc-attgen-jefjen`
9. `nphc-attgen-kenpax`
10. `nphc-attgen-leezel`
11. `nphc-attgen-matgae`
12. `nphc-attgen-matwhi`
13. `nphc-attgen-robgiu`
14. `nphc-attgen-rondes` ← this one
15. `nphc-attgen-tedcru`
16. `nphc-attgen-todbla`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 53 @ 10¢ → $2.57/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 79 (53 yours) | ×0.5^0 = 78.6 |
|  | 50¢ | 100 | ×0.5^40 = 0.0 |
|  | 97¢ | 53,892 | ×0.5^87 = 0.0 |
| | | **Σ** | **78.6** |

`yours 52.6 / Σ 78.6 = 66.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.9% = $2.57/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-rusfry</code> BUY 8,155 @ 1¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 783 | ×0.5^0 = 783.3 |
| ▶ | 1¢ | 10,655 (8,155 yours) | ×0.5^1 = 5,327.5 |
| | | **Σ** | **6,110.8** |

`yours 4,077.5 / Σ 6,110.8 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 20 @ 50¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 30 (20 yours) | ×0.5^0 = 30.0 |
|  | 2¢ | 250 | ×0.5^48 = 0.0 |
|  | 1¢ | 2,176 | ×0.5^49 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 50¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 15 (10 yours) | ×0.5^0 = 15.0 |
|  | 1¢ | 2,485 | ×0.5^49 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>apdc-trumpadmin-2026-petheg</code> BUY 314 @ 26¢ → $1.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 28¢ | 40 | ×0.5^0 = 40.0 |
| ▶ | 26¢ | 314 (314 yours) | ×0.5^2 = 78.4 |
|  | 25¢ | 38 | ×0.5^3 = 4.8 |
|  | 2¢ | 80,000 | ×0.5^26 = 0.0 |
| | | **Σ** | **123.2** |

`yours 78.4 / Σ 123.2 = 63.7%`  
`$100 ÷ 17 ÷ 2 = $2.94 × 63.7% = $1.87/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `apdc-trumpadmin-2026-brorol`
2. `apdc-trumpadmin-2026-howlut`
3. `apdc-trumpadmin-2026-johrat`
4. `apdc-trumpadmin-2026-karlea`
5. `apdc-trumpadmin-2026-kaspat`
6. `apdc-trumpadmin-2026-linmcm`
7. `apdc-trumpadmin-2026-marrub`
8. `apdc-trumpadmin-2026-petheg` ← this one
9. `apdc-trumpadmin-2026-robken`
10. `apdc-trumpadmin-2026-rodsco`
11. `apdc-trumpadmin-2026-rusvou`
12. `apdc-trumpadmin-2026-scobes`
13. `apdc-trumpadmin-2026-steche`
14. `apdc-trumpadmin-2026-stemil`
15. `apdc-trumpadmin-2026-stewit`
16. `apdc-trumpadmin-2026-suswil`
17. `apdc-trumpadmin-2026-tomhom`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-pameve</code> BUY 8,155 @ 1¢ → $2.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 600 | ×0.5^0 = 600.0 |
| ▶ | 1¢ | 11,655 (8,155 yours) | ×0.5^1 = 5,827.5 |
| | | **Σ** | **6,427.5** |

`yours 4,077.5 / Σ 6,427.5 = 63.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 63.4% = $2.64/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve` ← this one
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor`
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 20 @ 50¢ → $2.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 32 (20 yours) | ×0.5^0 = 32.0 |
|  | 1¢ | 2,468 | ×0.5^49 = 0.0 |
| | | **Σ** | **32.0** |

`yours 20.0 / Σ 32.0 = 62.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 62.5% = $2.60/day`  

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
<details><summary><code>pintc-meet-trump-2026-12-31-vlaput</code> BUY 388 @ 21¢ → $2.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 24¢ | 35 | ×0.5^0 = 35.0 |
|  | 23¢ | 5 | ×0.5^1 = 2.5 |
| ▶ | 21¢ | 388 (388 yours) | ×0.5^3 = 48.5 |
|  | 1¢ | 50,200 | ×0.5^23 = 0.0 |
| | | **Σ** | **86.0** |

`yours 48.5 / Σ 86.0 = 56.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 56.4% = $2.17/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon`
6. `pintc-meet-trump-2026-12-31-kimkar`
7. `pintc-meet-trump-2026-12-31-leoxiv`
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput` ← this one
11. `pintc-meet-trump-2026-12-31-volzel`
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-alawil</code> BUY 8,155 @ 1¢ → $2.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 15,265 (8,155 yours) | ×0.5^0 = 15,265.0 |
| | | **Σ** | **15,265.0** |

`yours 8,155.0 / Σ 15,265.0 = 53.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 53.4% = $2.23/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-andbau</code> BUY 8,155 @ 1¢ → $2.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 15,265 (8,155 yours) | ×0.5^0 = 15,265.0 |
| | | **Σ** | **15,265.0** |

`yours 8,155.0 / Σ 15,265.0 = 53.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 53.4% = $2.23/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 2¢ → $2.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 1 (1 yours) | ×0.5^0 = 1.0 |
|  | 7¢ | 28 | ×0.5^5 = 0.9 |
|  | 43¢ | 2,000 | ×0.5^41 = 0.0 |
| | | **Σ** | **1.9** |

`yours 1.0 / Σ 1.9 = 53.3%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 53.3% = $2.67/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-joewil</code> SELL 214 @ 20¢ → $2.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 19¢ | 100 | ×0.5^0 = 100.0 |
| ▶ | 20¢ | 214 (214 yours) | ×0.5^1 = 107.0 |
|  | 22¢ | 100 | ×0.5^3 = 12.5 |
|  | 50¢ | 25 | ×0.5^31 = 0.0 |
|  | 99¢ | 6,060 | ×0.5^80 = 0.0 |
| | | **Σ** | **219.5** |

`yours 107.0 / Σ 219.5 = 48.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 48.7% = $2.03/day`  

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
<details><summary><code>apdc-trumpadmin-2026-johrat</code> BUY 388 @ 21¢ → $1.26/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 24¢ | 47 | ×0.5^0 = 47.0 |
|  | 23¢ | 28 | ×0.5^1 = 14.0 |
|  | 22¢ | 9 | ×0.5^2 = 2.2 |
| ▶ | 21¢ | 397 (388 yours) | ×0.5^3 = 49.7 |
|  | 4¢ | 25 | ×0.5^20 = 0.0 |
|  | 2¢ | 50,000 | ×0.5^22 = 0.0 |
| | | **Σ** | **112.9** |

`yours 48.5 / Σ 112.9 = 43.0%`  
`$100 ÷ 17 ÷ 2 = $2.94 × 43.0% = $1.26/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `apdc-trumpadmin-2026-brorol`
2. `apdc-trumpadmin-2026-howlut`
3. `apdc-trumpadmin-2026-johrat` ← this one
4. `apdc-trumpadmin-2026-karlea`
5. `apdc-trumpadmin-2026-kaspat`
6. `apdc-trumpadmin-2026-linmcm`
7. `apdc-trumpadmin-2026-marrub`
8. `apdc-trumpadmin-2026-petheg`
9. `apdc-trumpadmin-2026-robken`
10. `apdc-trumpadmin-2026-rodsco`
11. `apdc-trumpadmin-2026-rusvou`
12. `apdc-trumpadmin-2026-scobes`
13. `apdc-trumpadmin-2026-steche`
14. `apdc-trumpadmin-2026-stemil`
15. `apdc-trumpadmin-2026-stewit`
16. `apdc-trumpadmin-2026-suswil`
17. `apdc-trumpadmin-2026-tomhom`

</details>

</details>
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-tregow</code> BUY 8,155 @ 1¢ → $1.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 23,018 (8,155 yours) | ×0.5^0 = 23,018.0 |
| | | **Σ** | **23,018.0** |

`yours 8,155.0 / Σ 23,018.0 = 35.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 35.4% = $1.48/day`  

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
<details><summary><code>apdc-trumpadmin-2026-rodsco</code> BUY 408 @ 20¢ → $1.04/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 21 | ×0.5^0 = 21.0 |
|  | 22¢ | 1 | ×0.5^1 = 0.5 |
| ▶ | 20¢ | 837 (408 yours) | ×0.5^3 = 104.6 |
|  | 17¢ | 1,176 | ×0.5^6 = 18.4 |
| | | **Σ** | **144.5** |

`yours 51.0 / Σ 144.5 = 35.3%`  
`$100 ÷ 17 ÷ 2 = $2.94 × 35.3% = $1.04/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `apdc-trumpadmin-2026-brorol`
2. `apdc-trumpadmin-2026-howlut`
3. `apdc-trumpadmin-2026-johrat`
4. `apdc-trumpadmin-2026-karlea`
5. `apdc-trumpadmin-2026-kaspat`
6. `apdc-trumpadmin-2026-linmcm`
7. `apdc-trumpadmin-2026-marrub`
8. `apdc-trumpadmin-2026-petheg`
9. `apdc-trumpadmin-2026-robken`
10. `apdc-trumpadmin-2026-rodsco` ← this one
11. `apdc-trumpadmin-2026-rusvou`
12. `apdc-trumpadmin-2026-scobes`
13. `apdc-trumpadmin-2026-steche`
14. `apdc-trumpadmin-2026-stemil`
15. `apdc-trumpadmin-2026-stewit`
16. `apdc-trumpadmin-2026-suswil`
17. `apdc-trumpadmin-2026-tomhom`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-betoro</code> BUY 1,359 @ 6¢ → $0.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 1 | ×0.5^0 = 1.0 |
| ▶ | 6¢ | 4,692 (1,359 yours) | ×0.5^1 = 2,346.1 |
| | | **Σ** | **2,347.1** |

`yours 679.6 / Σ 2,347.1 = 29.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 29.0% = $0.44/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro` ← this one
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
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>pintc-meet-trump-2026-12-31-leoxiv</code> BUY 4,077 @ 2¢ → $1.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 12 | ×0.5^0 = 12.0 |
| ▶ | 2¢ | 14,077 (4,077 yours) | ×0.5^1 = 7,038.5 |
| | | **Σ** | **7,050.5** |

`yours 2,038.5 / Σ 7,050.5 = 28.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.9% = $1.11/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon`
6. `pintc-meet-trump-2026-12-31-kimkar`
7. `pintc-meet-trump-2026-12-31-leoxiv` ← this one
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput`
11. `pintc-meet-trump-2026-12-31-volzel`
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-hilcli</code> BUY 4,078 @ 2¢ → $0.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 54 | ×0.5^0 = 54.0 |
| ▶ | 2¢ | 14,078 (4,078 yours) | ×0.5^1 = 7,038.8 |
| | | **Σ** | **7,092.8** |

`yours 2,038.8 / Σ 7,092.8 = 28.7%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 28.7% = $0.44/day`  

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
12. `cranc-uspres28-12-31-2026-hilcli` ← this one
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
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-dontru</code> BUY 1,019 @ 8¢ → $0.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 13 | ×0.5^0 = 13.0 |
| ▶ | 8¢ | 3,528 (1,019 yours) | ×0.5^1 = 1,764.2 |
| | | **Σ** | **1,777.2** |

`yours 509.7 / Σ 1,777.2 = 28.7%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 28.7% = $0.43/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru` ← this one
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
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>pintc-meet-trump-2026-12-31-kimjon</code> BUY 2,718 @ 3¢ → $1.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 14 | ×0.5^0 = 14.0 |
| ▶ | 3¢ | 9,406 (2,718 yours) | ×0.5^3 = 1,175.8 |
| | | **Σ** | **1,189.8** |

`yours 339.8 / Σ 1,189.8 = 28.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.6% = $1.10/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon` ← this one
6. `pintc-meet-trump-2026-12-31-kimkar`
7. `pintc-meet-trump-2026-12-31-leoxiv`
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput`
11. `pintc-meet-trump-2026-12-31-volzel`
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-markel</code> BUY 4,078 @ 2¢ → $0.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 7 | ×0.5^0 = 6.6 |
| ▶ | 2¢ | 14,328 (4,078 yours) | ×0.5^1 = 7,163.8 |
| | | **Σ** | **7,170.4** |

`yours 2,038.8 / Σ 7,170.4 = 28.4%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 28.4% = $0.43/day`  

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
20. `cranc-uspres28-12-31-2026-markel` ← this one
21. `cranc-uspres28-12-31-2026-marrub`
22. `cranc-uspres28-12-31-2026-micoba`
23. `cranc-uspres28-12-31-2026-nikhal`
24. `cranc-uspres28-12-31-2026-oprwin`
25. `cranc-uspres28-12-31-2026-petbut`
26. `cranc-uspres28-12-31-2026-rahema`
27. `cranc-uspres28-12-31-2026-robken`
28. `cranc-uspres28-12-31-2026-steban`
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-23 | ~$136.30 | $227.63 | 167% |
| 2026-07-22 | ~$110.63 | $82.95 | 75% |
| 2026-07-21 | ~$87.94 | $91.44 | 104% |

Biggest gaps on 2026-07-23: `opdc-trump-resig-2027-12-31` (est ~$2.12 → got $0.00), `scc-senate-gop-2026-11-03-55` (est ~$2.14 → got $0.44), `stsc-hormuz-normal-aug31` (est ~$1.67 → got $0.01)

_2026-07-24 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.50 | 2,000 | SELL side (15,260 resting) | ~79.5% | ~$13.24 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (67,709 resting) | ~29.7% | ~$7.43 |
| `paccc-usse-midterms-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (616,054 resting) | ~25.5% | ~$6.38 |
| `dipcc-us-iran-contnts-2026--enrcaplte5` | $250.00 ÷ 6 | 0.50 | 2,000 | SELL side (2,869 resting) | ~26.5% | ~$5.52 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (32,391 resting) | ~18.6% | ~$4.66 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (2,558 resting) | ~16.7% | ~$4.19 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $100.00 ÷ 3 | 0.50 | 2,000 | BUY side (130,743 resting) | ~23.2% | ~$3.86 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (98,081 resting) | ~12.2% | ~$3.04 |
| `ewc-usgub-ks-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (99,241 resting) | ~11.9% | ~$2.96 |
| `ewc-usgub-wi-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (108,119 resting) | ~7.7% | ~$1.93 |
| `dipcc-us-iran-contnts-2026--irnfnd` | $250.00 ÷ 6 | 0.50 | 2,000 | SELL side (6,837 resting) | ~8.6% | ~$1.78 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (94,168 resting) | ~6.3% | ~$1.57 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $679.56 |
| Skipped | $1.21 |
| **Total earned** | **$836.61** |

351 reward rows · 22 days with rewards · 126 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-24 ⚠️ multi-day pending bucket | $135.19 | `████████████` |
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
| 2026-07-12 | $39.90 | `████` |
| 2026-07-11 | $2.11 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $836.61 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $57.16 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $43.94 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $37.11 |
| `apdc-jerpowgov-2026-12-31` | $37.00 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $33.15 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.61 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $26.86 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $21.69 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $21.65 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $21.29 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $21.19 |
| `vmc-ussep-misen-2026-08-04-stegte20` | $20.20 |
| `vmc-ussep-misen-2026-08-04-ste05-10` | $19.47 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-26 5:15 PM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 4:54 PM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 3:39 PM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 1:27 PM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 11:33 AM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 10:02 AM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 7:39 AM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 5:53 AM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 5:27 AM ET | ✅ ok | 351 | $836.61 |
| 2026-07-26 3:07 AM ET | ✅ ok | 351 | $836.61 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
