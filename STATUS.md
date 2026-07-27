# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-27 6:30 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$38.67/day estimated (ceiling, not promise — details below)

**Earned:** $962.30 lifetime ($155.84 paid). Last three recorded days — 2026-07-25: **$125.69** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-24: **$135.19** · 2026-07-23: **$227.63** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mn-2026-08-11-dem-pegfla` — BUY at the best price, ~$10.22/day for 200 contracts. Runners-up: `enwc-usgubp-sd-2026-06-02-rep-tobdoe` (~$9.35/day), `enwc-usgubp-ok-2026-06-16-rep-gendru` (~$8.84/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$38.67/day (~$1.61/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 2.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.4% of ask side (43,471 resting ≥ 2,000 ✓) ≈ $4.97/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 5.0¢ | 127 | 0 | $100.00 | ✅ scoring — ~98.7% of ask side (6,289 resting ≥ 2,000 ✓) ≈ $4.11/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 22.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~87.3% of ask side (61,772 resting ≥ 2,000 ✓) ≈ $4.37/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 16.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~69.9% of ask side (218,128 resting ≥ 2,000 ✓) ≈ $2.69/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 27.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~52.7% of ask side (99,591 resting ≥ 2,000 ✓) ≈ $2.64/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 13.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~30.2% of bid side (200,570 resting ≥ 2,000 ✓) ≈ $1.16/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 26.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~14.0% of bid side (10,353 resting ≥ 2,000 ✓) ≈ $0.70/day (pool ÷ 10 markets) |
| `tec-pga-rockclas-2026-08-02-r3l-nicdun` | BUY | 0.2¢ | 308 | 0 | $10,000.00 | ✅ scoring — ~7.9% of bid side (10,608 resting ≥ 10,000 ✓) ≈ $0.93/day (pool ÷ 25 markets) (pre-tournament pool over 17d) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 22.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~6.7% of bid side (10,878 resting ≥ 2,000 ✓) ≈ $3.35/day |
| `tec-pga-rockclas-2026-08-02-w-eriroo` | BUY | 0.2¢ | 500 | 0 | $10,000.00 | ✅ scoring — ~6.5% of bid side (18,487 resting ≥ 10,000 ✓) ≈ $0.42/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-bradal` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~5.9% of bid side (17,071 resting ≥ 10,000 ✓) ≈ $0.38/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-matkuc` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~5.8% of bid side (17,352 resting ≥ 10,000 ✓) ≈ $0.38/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-ryaruf` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~5.6% of bid side (17,932 resting ≥ 10,000 ✓) ≈ $0.36/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-adasch` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~5.5% of bid side (18,034 resting ≥ 10,000 ✓) ≈ $0.36/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-danwal` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~5.4% of bid side (18,380 resting ≥ 10,000 ✓) ≈ $0.36/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-adasve` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~5.4% of bid side (18,532 resting ≥ 10,000 ✓) ≈ $0.35/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-brasne` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~5.3% of bid side (18,789 resting ≥ 10,000 ✓) ≈ $0.35/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-kenhir` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~5.3% of bid side (18,884 resting ≥ 10,000 ✓) ≈ $0.35/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-petmal` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~5.2% of bid side (19,138 resting ≥ 10,000 ✓) ≈ $0.34/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-patkiz` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~5.2% of bid side (19,180 resting ≥ 10,000 ✓) ≈ $0.34/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-andput` | BUY | 0.2¢ | 500 | 0 | $10,000.00 | ✅ scoring — ~5.1% of bid side (22,597 resting ≥ 10,000 ✓) ≈ $0.33/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-patrod` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~4.5% of bid side (22,162 resting ≥ 10,000 ✓) ≈ $0.29/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-ponnyh` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~4.5% of bid side (22,411 resting ≥ 10,000 ✓) ≈ $0.29/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-w-takkan` | BUY | 0.1¢ | 1,000 | 0 | $10,000.00 | ✅ scoring — ~4.4% of bid side (22,483 resting ≥ 10,000 ✓) ≈ $0.29/day (pool ÷ 45 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-r3l-jefkan` | BUY | 0.2¢ | 287 | 0 | $10,000.00 | ✅ scoring — ~4.4% of bid side (13,062 resting ≥ 10,000 ✓) ≈ $0.09/day (pool ÷ 146 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-r3l-tonfin` | BUY | 0.2¢ | 500 | 0 | $10,000.00 | ✅ scoring — ~4.3% of bid side (17,012 resting ≥ 10,000 ✓) ≈ $0.50/day (pool ÷ 25 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-r3l-lucglo` | BUY | 0.2¢ | 500 | 0 | $10,000.00 | ✅ scoring — ~4.3% of bid side (17,012 resting ≥ 10,000 ✓) ≈ $0.09/day (pool ÷ 146 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-r3l-johpar` | BUY | 0.2¢ | 500 | 0 | $10,000.00 | ✅ scoring — ~4.3% of bid side (26,992 resting ≥ 10,000 ✓) ≈ $0.09/day (pool ÷ 146 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-r3l-kevroy` | BUY | 0.2¢ | 500 | 0 | $10,000.00 | ✅ scoring — ~4.3% of bid side (16,992 resting ≥ 10,000 ✓) ≈ $0.09/day (pool ÷ 146 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-r3l-kriven` | BUY | 0.2¢ | 500 | 0 | $10,000.00 | ✅ scoring — ~4.3% of bid side (16,997 resting ≥ 10,000 ✓) ≈ $0.09/day (pool ÷ 146 markets) (pre-tournament pool over 17d) |
| …and 52 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 2¢ → $4.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 1 (1 yours) | ×0.5^0 = 1.0 |
|  | 16¢ | 100 | ×0.5^14 = 0.0 |
|  | 20¢ | 3 | ×0.5^18 = 0.0 |
|  | 30¢ | 2 | ×0.5^28 = 0.0 |
|  | 43¢ | 3,387 | ×0.5^41 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.4%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 99.4% = $4.97/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 127 @ 5¢ → $4.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 127 (127 yours) | ×0.5^0 = 127.3 |
|  | 10¢ | 52 | ×0.5^5 = 1.6 |
|  | 20¢ | 3 | ×0.5^15 = 0.0 |
|  | 23¢ | 100 | ×0.5^18 = 0.0 |
|  | 30¢ | 4 | ×0.5^25 = 0.0 |
|  | 40¢ | 1 | ×0.5^35 = 0.0 |
|  | 50¢ | 25 | ×0.5^45 = 0.0 |
|  | 99¢ | 5,977 | ×0.5^94 = 0.0 |
| | | **Σ** | **129.0** |

`yours 127.3 / Σ 129.0 = 98.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 98.7% = $4.11/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> SELL 30 @ 22¢ → $4.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 30 (30 yours) | ×0.5^0 = 30.0 |
|  | 26¢ | 57 | ×0.5^4 = 3.6 |
|  | 29¢ | 100 | ×0.5^7 = 0.8 |
|  | 30¢ | 2 | ×0.5^8 = 0.0 |
|  | 45¢ | 25 | ×0.5^23 = 0.0 |
|  | 97¢ | 5 | ×0.5^75 = 0.0 |
|  | 98¢ | 61,053 | ×0.5^76 = 0.0 |
| | | **Σ** | **34.4** |

`yours 30.0 / Σ 34.4 = 87.3%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 87.3% = $4.37/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 100 @ 16¢ → $2.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 15¢ | 21 | ×0.5^0 = 21.0 |
| ▶ | 16¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 19¢ | 5 | ×0.5^4 = 0.3 |
|  | 20¢ | 1 | ×0.5^5 = 0.0 |
|  | 24¢ | 100 | ×0.5^9 = 0.2 |
|  | 28¢ | 100 | ×0.5^13 = 0.0 |
|  | 30¢ | 4 | ×0.5^15 = 0.0 |
|  | 50¢ | 100 | ×0.5^35 = 0.0 |
|  | 98¢ | 131,484 | ×0.5^83 = 0.0 |
| | | **Σ** | **71.6** |

`yours 50.0 / Σ 71.6 = 69.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 69.9% = $2.69/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 2 @ 27¢ → $2.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 2 (2 yours) | ×0.5^0 = 2.3 |
|  | 30¢ | 2 | ×0.5^3 = 0.2 |
|  | 32¢ | 56 | ×0.5^5 = 1.8 |
|  | 39¢ | 100 | ×0.5^12 = 0.0 |
|  | 45¢ | 25 | ×0.5^18 = 0.0 |
|  | 98¢ | 98,906 | ×0.5^71 = 0.0 |
| | | **Σ** | **4.3** |

`yours 2.3 / Σ 4.3 = 52.7%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 52.7% = $2.64/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 100 @ 13¢ → $1.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 18 | ×0.5^0 = 18.0 |
| ▶ | 13¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 5¢ | 2 | ×0.5^9 = 0.0 |
|  | 3¢ | 200,250 | ×0.5^11 = 97.8 |
| | | **Σ** | **165.8** |

`yours 50.0 / Σ 165.8 = 30.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 30.2% = $1.16/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 9 @ 26¢ → $0.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 62 (9 yours) | ×0.5^0 = 62.4 |
|  | 9¢ | 25 | ×0.5^17 = 0.0 |
|  | 5¢ | 2 | ×0.5^21 = 0.0 |
|  | 3¢ | 10,250 | ×0.5^23 = 0.0 |
| | | **Σ** | **62.4** |

`yours 8.7 / Σ 62.4 = 14.0%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 14.0% = $0.70/day`  

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
<details><summary><code>tec-pga-rockclas-2026-08-02-r3l-nicdun</code> BUY 308 @ 0.2¢ → $0.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.2¢ | 308 (308 yours) | ×0.35^0 = 308.0 |
|  | 0.1¢ | 10,300 | ×0.35^1 = 3,605.0 |
| | | **Σ** | **3,913.0** |

`yours 308.0 / Σ 3,913.0 = 7.9%`  
`$10,000 ÷ 17d ÷ 25 ÷ 2 = $11.76 × 7.9% = $0.93/day`  

<details><summary>÷ 25 markets in this race — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r3l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r3l-adrsad`
3. `tec-pga-rockclas-2026-08-02-r3l-bretod`
4. `tec-pga-rockclas-2026-08-02-r3l-camdav`
5. `tec-pga-rockclas-2026-08-02-r3l-charam`
6. `tec-pga-rockclas-2026-08-02-r3l-chrkir`
7. `tec-pga-rockclas-2026-08-02-r3l-haoli`
8. `tec-pga-rockclas-2026-08-02-r3l-jefkan`
9. `tec-pga-rockclas-2026-08-02-r3l-johpar`
10. `tec-pga-rockclas-2026-08-02-r3l-johvan`
11. `tec-pga-rockclas-2026-08-02-r3l-keinak`
12. `tec-pga-rockclas-2026-08-02-r3l-kevroy`
13. `tec-pga-rockclas-2026-08-02-r3l-kriven`
14. `tec-pga-rockclas-2026-08-02-r3l-leehod`
15. `tec-pga-rockclas-2026-08-02-r3l-lucglo`
16. `tec-pga-rockclas-2026-08-02-r3l-machug`
17. `tec-pga-rockclas-2026-08-02-r3l-marhub`
18. `tec-pga-rockclas-2026-08-02-r3l-matsch`
19. `tec-pga-rockclas-2026-08-02-r3l-nicdun` ← this one
20. `tec-pga-rockclas-2026-08-02-r3l-sudyel`
21. `tec-pga-rockclas-2026-08-02-r3l-tonfin`
22. `tec-pga-rockclas-2026-08-02-r3l-vinwha`
23. `tec-pga-rockclas-2026-08-02-r3l-websim`
24. `tec-pga-rockclas-2026-08-02-r3l-wiljen`
25. `tec-pga-rockclas-2026-08-02-r3l-zacbau`

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 10 @ 22¢ → $3.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 34 | ×0.5^0 = 34.0 |
| ▶ | 22¢ | 50 (10 yours) | ×0.5^1 = 25.0 |
|  | 21¢ | 35 | ×0.5^2 = 8.7 |
|  | 20¢ | 48 | ×0.5^3 = 6.0 |
|  | 17¢ | 54 | ×0.5^6 = 0.8 |
|  | 12¢ | 64 | ×0.5^11 = 0.0 |
|  | 5¢ | 2 | ×0.5^18 = 0.0 |
|  | 4¢ | 239 | ×0.5^19 = 0.0 |
|  | 2¢ | 10,152 | ×0.5^21 = 0.0 |
| | | **Σ** | **74.6** |

`yours 5.0 / Σ 74.6 = 6.7%`  
`$100 ÷ 1 ÷ 2 = $50.00 × 6.7% = $3.35/day`  

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-eriroo</code> BUY 500 @ 0.2¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.2¢ | 1,969 (500 yours) | ×0.35^0 = 1,969.0 |
|  | 0.1¢ | 16,518 | ×0.35^1 = 5,781.2 |
| | | **Σ** | **7,750.2** |

`yours 500.0 / Σ 7,750.2 = 6.5%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 6.5% = $0.42/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo` ← this one
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-bradal</code> BUY 1,000 @ 0.1¢ → $0.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 17,071 (1,000 yours) | ×0.35^0 = 17,071.0 |
| | | **Σ** | **17,071.0** |

`yours 1,000.0 / Σ 17,071.0 = 5.9%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.9% = $0.38/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal` ← this one
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-matkuc</code> BUY 1,000 @ 0.1¢ → $0.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 17,352 (1,000 yours) | ×0.35^0 = 17,351.8 |
| | | **Σ** | **17,351.8** |

`yours 1,000.0 / Σ 17,351.8 = 5.8%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.8% = $0.38/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc` ← this one
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-ryaruf</code> BUY 1,000 @ 0.1¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 17,932 (1,000 yours) | ×0.35^0 = 17,932.5 |
| | | **Σ** | **17,932.5** |

`yours 1,000.0 / Σ 17,932.5 = 5.6%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.6% = $0.36/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf` ← this one
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-adasch</code> BUY 1,000 @ 0.1¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 18,034 (1,000 yours) | ×0.35^0 = 18,034.2 |
| | | **Σ** | **18,034.2** |

`yours 1,000.0 / Σ 18,034.2 = 5.5%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.5% = $0.36/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch` ← this one
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-danwal</code> BUY 1,000 @ 0.1¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 18,380 (1,000 yours) | ×0.35^0 = 18,380.0 |
| | | **Σ** | **18,380.0** |

`yours 1,000.0 / Σ 18,380.0 = 5.4%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.4% = $0.36/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal` ← this one
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-adasve</code> BUY 1,000 @ 0.1¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 18,532 (1,000 yours) | ×0.35^0 = 18,531.8 |
| | | **Σ** | **18,531.8** |

`yours 1,000.0 / Σ 18,531.8 = 5.4%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.4% = $0.35/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve` ← this one
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-brasne</code> BUY 1,000 @ 0.1¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 18,789 (1,000 yours) | ×0.35^0 = 18,789.2 |
| | | **Σ** | **18,789.2** |

`yours 1,000.0 / Σ 18,789.2 = 5.3%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.3% = $0.35/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne` ← this one
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-kenhir</code> BUY 1,000 @ 0.1¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 18,884 (1,000 yours) | ×0.35^0 = 18,883.8 |
| | | **Σ** | **18,883.8** |

`yours 1,000.0 / Σ 18,883.8 = 5.3%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.3% = $0.35/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir` ← this one
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-petmal</code> BUY 1,000 @ 0.1¢ → $0.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 19,138 (1,000 yours) | ×0.35^0 = 19,137.7 |
| | | **Σ** | **19,137.7** |

`yours 1,000.0 / Σ 19,137.7 = 5.2%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.2% = $0.34/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal` ← this one
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-patkiz</code> BUY 1,000 @ 0.1¢ → $0.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 19,180 (1,000 yours) | ×0.35^0 = 19,180.3 |
| | | **Σ** | **19,180.3** |

`yours 1,000.0 / Σ 19,180.3 = 5.2%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.2% = $0.34/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz` ← this one
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-andput</code> BUY 500 @ 0.2¢ → $0.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.2¢ | 2,974 (500 yours) | ×0.35^0 = 2,974.0 |
|  | 0.1¢ | 19,623 | ×0.35^1 = 6,868.2 |
| | | **Σ** | **9,842.2** |

`yours 500.0 / Σ 9,842.2 = 5.1%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 5.1% = $0.33/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput` ← this one
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-patrod</code> BUY 1,000 @ 0.1¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 22,162 (1,000 yours) | ×0.35^0 = 22,161.6 |
| | | **Σ** | **22,161.6** |

`yours 1,000.0 / Σ 22,161.6 = 4.5%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 4.5% = $0.29/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod` ← this one
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-ponnyh</code> BUY 1,000 @ 0.1¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 22,411 (1,000 yours) | ×0.35^0 = 22,411.5 |
| | | **Σ** | **22,411.5** |

`yours 1,000.0 / Σ 22,411.5 = 4.5%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 4.5% = $0.29/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh` ← this one
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-w-takkan</code> BUY 1,000 @ 0.1¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.1¢ | 22,483 (1,000 yours) | ×0.35^0 = 22,483.1 |
| | | **Σ** | **22,483.1** |

`yours 1,000.0 / Σ 22,483.1 = 4.4%`  
`$10,000 ÷ 17d ÷ 45 ÷ 2 = $6.54 × 4.4% = $0.29/day`  

<details><summary>÷ 45 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-w-aarwis`
2. `tec-pga-rockclas-2026-08-02-w-adasch`
3. `tec-pga-rockclas-2026-08-02-w-adasve`
4. `tec-pga-rockclas-2026-08-02-w-adrsad`
5. `tec-pga-rockclas-2026-08-02-w-aletos`
6. `tec-pga-rockclas-2026-08-02-w-andput`
7. `tec-pga-rockclas-2026-08-02-w-auseck`
8. `tec-pga-rockclas-2026-08-02-w-bradal`
9. `tec-pga-rockclas-2026-08-02-w-brasne`
10. `tec-pga-rockclas-2026-08-02-w-bretod`
11. `tec-pga-rockclas-2026-08-02-w-bricam`
12. `tec-pga-rockclas-2026-08-02-w-brigar`
13. `tec-pga-rockclas-2026-08-02-w-charam`
14. `tec-pga-rockclas-2026-08-02-w-chrlam`
15. `tec-pga-rockclas-2026-08-02-w-danwal`
16. `tec-pga-rockclas-2026-08-02-w-davcha`
17. `tec-pga-rockclas-2026-08-02-w-davlip`
18. `tec-pga-rockclas-2026-08-02-w-davril`
19. `tec-pga-rockclas-2026-08-02-w-eriroo`
20. `tec-pga-rockclas-2026-08-02-w-garhig`
21. `tec-pga-rockclas-2026-08-02-w-gorsar`
22. `tec-pga-rockclas-2026-08-02-w-haoli`
23. `tec-pga-rockclas-2026-08-02-w-jefkan`
24. `tec-pga-rockclas-2026-08-02-w-joehig`
25. `tec-pga-rockclas-2026-08-02-w-joehoo`
26. `tec-pga-rockclas-2026-08-02-w-johvan`
27. `tec-pga-rockclas-2026-08-02-w-kenhir`
28. `tec-pga-rockclas-2026-08-02-w-kevstr`
29. `tec-pga-rockclas-2026-08-02-w-lukcla`
30. `tec-pga-rockclas-2026-08-02-w-marroz`
31. `tec-pga-rockclas-2026-08-02-w-matkuc`
32. `tec-pga-rockclas-2026-08-02-w-matpav`
33. `tec-pga-rockclas-2026-08-02-w-nicdun`
34. `tec-pga-rockclas-2026-08-02-w-patkiz`
35. `tec-pga-rockclas-2026-08-02-w-patrod`
36. `tec-pga-rockclas-2026-08-02-w-petmal`
37. `tec-pga-rockclas-2026-08-02-w-ponnyh`
38. `tec-pga-rockclas-2026-08-02-w-ryaruf`
39. `tec-pga-rockclas-2026-08-02-w-stemaz`
40. `tec-pga-rockclas-2026-08-02-w-takkan` ← this one

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-r3l-jefkan</code> BUY 287 @ 0.2¢ → $0.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.2¢ | 3,037 (287 yours) | ×0.35^0 = 3,037.0 |
|  | 0.1¢ | 10,025 | ×0.35^1 = 3,508.8 |
| | | **Σ** | **6,545.8** |

`yours 287.0 / Σ 6,545.8 = 4.4%`  
`$10,000 ÷ 17d ÷ 146 ÷ 2 = $2.01 × 4.4% = $0.09/day`  

<details><summary>÷ 146 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r3l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r3l-adasch`
3. `tec-pga-rockclas-2026-08-02-r3l-adasve`
4. `tec-pga-rockclas-2026-08-02-r3l-adrcha`
5. `tec-pga-rockclas-2026-08-02-r3l-adrsad`
6. `tec-pga-rockclas-2026-08-02-r3l-aewa`
7. `tec-pga-rockclas-2026-08-02-r3l-aksbha`
8. `tec-pga-rockclas-2026-08-02-r3l-aldpot`
9. `tec-pga-rockclas-2026-08-02-r3l-aletos`
10. `tec-pga-rockclas-2026-08-02-r3l-andnov`
11. `tec-pga-rockclas-2026-08-02-r3l-andput`
12. `tec-pga-rockclas-2026-08-02-r3l-auseck`
13. `tec-pga-rockclas-2026-08-02-r3l-aussmo`
14. `tec-pga-rockclas-2026-08-02-r3l-beahos`
15. `tec-pga-rockclas-2026-08-02-r3l-bengri`
16. `tec-pga-rockclas-2026-08-02-r3l-benjam`
17. `tec-pga-rockclas-2026-08-02-r3l-benkoh`
18. `tec-pga-rockclas-2026-08-02-r3l-bilhor`
19. `tec-pga-rockclas-2026-08-02-r3l-bradal`
20. `tec-pga-rockclas-2026-08-02-r3l-brasne`
21. `tec-pga-rockclas-2026-08-02-r3l-bretod`
22. `tec-pga-rockclas-2026-08-02-r3l-bricam`
23. `tec-pga-rockclas-2026-08-02-r3l-brigar`
24. `tec-pga-rockclas-2026-08-02-r3l-brokoe`
25. `tec-pga-rockclas-2026-08-02-r3l-camdav`
26. `tec-pga-rockclas-2026-08-02-r3l-camyou`
27. `tec-pga-rockclas-2026-08-02-r3l-chabla`
28. `tec-pga-rockclas-2026-08-02-r3l-chaphi`
29. `tec-pga-rockclas-2026-08-02-r3l-charam`
30. `tec-pga-rockclas-2026-08-02-r3l-chrbez`
31. `tec-pga-rockclas-2026-08-02-r3l-chrgot`
32. `tec-pga-rockclas-2026-08-02-r3l-chrkir`
33. `tec-pga-rockclas-2026-08-02-r3l-chrlam`
34. `tec-pga-rockclas-2026-08-02-r3l-corcon`
35. `tec-pga-rockclas-2026-08-02-r3l-danaza`
36. `tec-pga-rockclas-2026-08-02-r3l-danwal`
37. `tec-pga-rockclas-2026-08-02-r3l-davcha`
38. `tec-pga-rockclas-2026-08-02-r3l-davlip`
39. `tec-pga-rockclas-2026-08-02-r3l-davril`
40. `tec-pga-rockclas-2026-08-02-r3l-davtho`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-r3l-tonfin</code> BUY 500 @ 0.2¢ → $0.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.2¢ | 11,737 (500 yours) | ×0.35^0 = 11,737.0 |
| | | **Σ** | **11,737.0** |

`yours 500.0 / Σ 11,737.0 = 4.3%`  
`$10,000 ÷ 17d ÷ 25 ÷ 2 = $11.76 × 4.3% = $0.50/day`  

<details><summary>÷ 25 markets in this race — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r3l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r3l-adrsad`
3. `tec-pga-rockclas-2026-08-02-r3l-bretod`
4. `tec-pga-rockclas-2026-08-02-r3l-camdav`
5. `tec-pga-rockclas-2026-08-02-r3l-charam`
6. `tec-pga-rockclas-2026-08-02-r3l-chrkir`
7. `tec-pga-rockclas-2026-08-02-r3l-haoli`
8. `tec-pga-rockclas-2026-08-02-r3l-jefkan`
9. `tec-pga-rockclas-2026-08-02-r3l-johpar`
10. `tec-pga-rockclas-2026-08-02-r3l-johvan`
11. `tec-pga-rockclas-2026-08-02-r3l-keinak`
12. `tec-pga-rockclas-2026-08-02-r3l-kevroy`
13. `tec-pga-rockclas-2026-08-02-r3l-kriven`
14. `tec-pga-rockclas-2026-08-02-r3l-leehod`
15. `tec-pga-rockclas-2026-08-02-r3l-lucglo`
16. `tec-pga-rockclas-2026-08-02-r3l-machug`
17. `tec-pga-rockclas-2026-08-02-r3l-marhub`
18. `tec-pga-rockclas-2026-08-02-r3l-matsch`
19. `tec-pga-rockclas-2026-08-02-r3l-nicdun`
20. `tec-pga-rockclas-2026-08-02-r3l-sudyel`
21. `tec-pga-rockclas-2026-08-02-r3l-tonfin` ← this one
22. `tec-pga-rockclas-2026-08-02-r3l-vinwha`
23. `tec-pga-rockclas-2026-08-02-r3l-websim`
24. `tec-pga-rockclas-2026-08-02-r3l-wiljen`
25. `tec-pga-rockclas-2026-08-02-r3l-zacbau`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-r3l-lucglo</code> BUY 500 @ 0.2¢ → $0.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.2¢ | 11,737 (500 yours) | ×0.35^0 = 11,737.0 |
| | | **Σ** | **11,737.0** |

`yours 500.0 / Σ 11,737.0 = 4.3%`  
`$10,000 ÷ 17d ÷ 146 ÷ 2 = $2.01 × 4.3% = $0.09/day`  

<details><summary>÷ 146 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r3l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r3l-adasch`
3. `tec-pga-rockclas-2026-08-02-r3l-adasve`
4. `tec-pga-rockclas-2026-08-02-r3l-adrcha`
5. `tec-pga-rockclas-2026-08-02-r3l-adrsad`
6. `tec-pga-rockclas-2026-08-02-r3l-aewa`
7. `tec-pga-rockclas-2026-08-02-r3l-aksbha`
8. `tec-pga-rockclas-2026-08-02-r3l-aldpot`
9. `tec-pga-rockclas-2026-08-02-r3l-aletos`
10. `tec-pga-rockclas-2026-08-02-r3l-andnov`
11. `tec-pga-rockclas-2026-08-02-r3l-andput`
12. `tec-pga-rockclas-2026-08-02-r3l-auseck`
13. `tec-pga-rockclas-2026-08-02-r3l-aussmo`
14. `tec-pga-rockclas-2026-08-02-r3l-beahos`
15. `tec-pga-rockclas-2026-08-02-r3l-bengri`
16. `tec-pga-rockclas-2026-08-02-r3l-benjam`
17. `tec-pga-rockclas-2026-08-02-r3l-benkoh`
18. `tec-pga-rockclas-2026-08-02-r3l-bilhor`
19. `tec-pga-rockclas-2026-08-02-r3l-bradal`
20. `tec-pga-rockclas-2026-08-02-r3l-brasne`
21. `tec-pga-rockclas-2026-08-02-r3l-bretod`
22. `tec-pga-rockclas-2026-08-02-r3l-bricam`
23. `tec-pga-rockclas-2026-08-02-r3l-brigar`
24. `tec-pga-rockclas-2026-08-02-r3l-brokoe`
25. `tec-pga-rockclas-2026-08-02-r3l-camdav`
26. `tec-pga-rockclas-2026-08-02-r3l-camyou`
27. `tec-pga-rockclas-2026-08-02-r3l-chabla`
28. `tec-pga-rockclas-2026-08-02-r3l-chaphi`
29. `tec-pga-rockclas-2026-08-02-r3l-charam`
30. `tec-pga-rockclas-2026-08-02-r3l-chrbez`
31. `tec-pga-rockclas-2026-08-02-r3l-chrgot`
32. `tec-pga-rockclas-2026-08-02-r3l-chrkir`
33. `tec-pga-rockclas-2026-08-02-r3l-chrlam`
34. `tec-pga-rockclas-2026-08-02-r3l-corcon`
35. `tec-pga-rockclas-2026-08-02-r3l-danaza`
36. `tec-pga-rockclas-2026-08-02-r3l-danwal`
37. `tec-pga-rockclas-2026-08-02-r3l-davcha`
38. `tec-pga-rockclas-2026-08-02-r3l-davlip`
39. `tec-pga-rockclas-2026-08-02-r3l-davril`
40. `tec-pga-rockclas-2026-08-02-r3l-davtho`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-r3l-johpar</code> BUY 500 @ 0.2¢ → $0.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.2¢ | 11,742 (500 yours) | ×0.35^0 = 11,742.0 |
| | | **Σ** | **11,742.0** |

`yours 500.0 / Σ 11,742.0 = 4.3%`  
`$10,000 ÷ 17d ÷ 146 ÷ 2 = $2.01 × 4.3% = $0.09/day`  

<details><summary>÷ 146 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r3l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r3l-adasch`
3. `tec-pga-rockclas-2026-08-02-r3l-adasve`
4. `tec-pga-rockclas-2026-08-02-r3l-adrcha`
5. `tec-pga-rockclas-2026-08-02-r3l-adrsad`
6. `tec-pga-rockclas-2026-08-02-r3l-aewa`
7. `tec-pga-rockclas-2026-08-02-r3l-aksbha`
8. `tec-pga-rockclas-2026-08-02-r3l-aldpot`
9. `tec-pga-rockclas-2026-08-02-r3l-aletos`
10. `tec-pga-rockclas-2026-08-02-r3l-andnov`
11. `tec-pga-rockclas-2026-08-02-r3l-andput`
12. `tec-pga-rockclas-2026-08-02-r3l-auseck`
13. `tec-pga-rockclas-2026-08-02-r3l-aussmo`
14. `tec-pga-rockclas-2026-08-02-r3l-beahos`
15. `tec-pga-rockclas-2026-08-02-r3l-bengri`
16. `tec-pga-rockclas-2026-08-02-r3l-benjam`
17. `tec-pga-rockclas-2026-08-02-r3l-benkoh`
18. `tec-pga-rockclas-2026-08-02-r3l-bilhor`
19. `tec-pga-rockclas-2026-08-02-r3l-bradal`
20. `tec-pga-rockclas-2026-08-02-r3l-brasne`
21. `tec-pga-rockclas-2026-08-02-r3l-bretod`
22. `tec-pga-rockclas-2026-08-02-r3l-bricam`
23. `tec-pga-rockclas-2026-08-02-r3l-brigar`
24. `tec-pga-rockclas-2026-08-02-r3l-brokoe`
25. `tec-pga-rockclas-2026-08-02-r3l-camdav`
26. `tec-pga-rockclas-2026-08-02-r3l-camyou`
27. `tec-pga-rockclas-2026-08-02-r3l-chabla`
28. `tec-pga-rockclas-2026-08-02-r3l-chaphi`
29. `tec-pga-rockclas-2026-08-02-r3l-charam`
30. `tec-pga-rockclas-2026-08-02-r3l-chrbez`
31. `tec-pga-rockclas-2026-08-02-r3l-chrgot`
32. `tec-pga-rockclas-2026-08-02-r3l-chrkir`
33. `tec-pga-rockclas-2026-08-02-r3l-chrlam`
34. `tec-pga-rockclas-2026-08-02-r3l-corcon`
35. `tec-pga-rockclas-2026-08-02-r3l-danaza`
36. `tec-pga-rockclas-2026-08-02-r3l-danwal`
37. `tec-pga-rockclas-2026-08-02-r3l-davcha`
38. `tec-pga-rockclas-2026-08-02-r3l-davlip`
39. `tec-pga-rockclas-2026-08-02-r3l-davril`
40. `tec-pga-rockclas-2026-08-02-r3l-davtho`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-r3l-kevroy</code> BUY 500 @ 0.2¢ → $0.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.2¢ | 11,742 (500 yours) | ×0.35^0 = 11,742.0 |
| | | **Σ** | **11,742.0** |

`yours 500.0 / Σ 11,742.0 = 4.3%`  
`$10,000 ÷ 17d ÷ 146 ÷ 2 = $2.01 × 4.3% = $0.09/day`  

<details><summary>÷ 146 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r3l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r3l-adasch`
3. `tec-pga-rockclas-2026-08-02-r3l-adasve`
4. `tec-pga-rockclas-2026-08-02-r3l-adrcha`
5. `tec-pga-rockclas-2026-08-02-r3l-adrsad`
6. `tec-pga-rockclas-2026-08-02-r3l-aewa`
7. `tec-pga-rockclas-2026-08-02-r3l-aksbha`
8. `tec-pga-rockclas-2026-08-02-r3l-aldpot`
9. `tec-pga-rockclas-2026-08-02-r3l-aletos`
10. `tec-pga-rockclas-2026-08-02-r3l-andnov`
11. `tec-pga-rockclas-2026-08-02-r3l-andput`
12. `tec-pga-rockclas-2026-08-02-r3l-auseck`
13. `tec-pga-rockclas-2026-08-02-r3l-aussmo`
14. `tec-pga-rockclas-2026-08-02-r3l-beahos`
15. `tec-pga-rockclas-2026-08-02-r3l-bengri`
16. `tec-pga-rockclas-2026-08-02-r3l-benjam`
17. `tec-pga-rockclas-2026-08-02-r3l-benkoh`
18. `tec-pga-rockclas-2026-08-02-r3l-bilhor`
19. `tec-pga-rockclas-2026-08-02-r3l-bradal`
20. `tec-pga-rockclas-2026-08-02-r3l-brasne`
21. `tec-pga-rockclas-2026-08-02-r3l-bretod`
22. `tec-pga-rockclas-2026-08-02-r3l-bricam`
23. `tec-pga-rockclas-2026-08-02-r3l-brigar`
24. `tec-pga-rockclas-2026-08-02-r3l-brokoe`
25. `tec-pga-rockclas-2026-08-02-r3l-camdav`
26. `tec-pga-rockclas-2026-08-02-r3l-camyou`
27. `tec-pga-rockclas-2026-08-02-r3l-chabla`
28. `tec-pga-rockclas-2026-08-02-r3l-chaphi`
29. `tec-pga-rockclas-2026-08-02-r3l-charam`
30. `tec-pga-rockclas-2026-08-02-r3l-chrbez`
31. `tec-pga-rockclas-2026-08-02-r3l-chrgot`
32. `tec-pga-rockclas-2026-08-02-r3l-chrkir`
33. `tec-pga-rockclas-2026-08-02-r3l-chrlam`
34. `tec-pga-rockclas-2026-08-02-r3l-corcon`
35. `tec-pga-rockclas-2026-08-02-r3l-danaza`
36. `tec-pga-rockclas-2026-08-02-r3l-danwal`
37. `tec-pga-rockclas-2026-08-02-r3l-davcha`
38. `tec-pga-rockclas-2026-08-02-r3l-davlip`
39. `tec-pga-rockclas-2026-08-02-r3l-davril`
40. `tec-pga-rockclas-2026-08-02-r3l-davtho`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-r3l-kriven</code> BUY 500 @ 0.2¢ → $0.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 0.2¢ | 11,747 (500 yours) | ×0.35^0 = 11,747.0 |
| | | **Σ** | **11,747.0** |

`yours 500.0 / Σ 11,747.0 = 4.3%`  
`$10,000 ÷ 17d ÷ 146 ÷ 2 = $2.01 × 4.3% = $0.09/day`  

<details><summary>÷ 146 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r3l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r3l-adasch`
3. `tec-pga-rockclas-2026-08-02-r3l-adasve`
4. `tec-pga-rockclas-2026-08-02-r3l-adrcha`
5. `tec-pga-rockclas-2026-08-02-r3l-adrsad`
6. `tec-pga-rockclas-2026-08-02-r3l-aewa`
7. `tec-pga-rockclas-2026-08-02-r3l-aksbha`
8. `tec-pga-rockclas-2026-08-02-r3l-aldpot`
9. `tec-pga-rockclas-2026-08-02-r3l-aletos`
10. `tec-pga-rockclas-2026-08-02-r3l-andnov`
11. `tec-pga-rockclas-2026-08-02-r3l-andput`
12. `tec-pga-rockclas-2026-08-02-r3l-auseck`
13. `tec-pga-rockclas-2026-08-02-r3l-aussmo`
14. `tec-pga-rockclas-2026-08-02-r3l-beahos`
15. `tec-pga-rockclas-2026-08-02-r3l-bengri`
16. `tec-pga-rockclas-2026-08-02-r3l-benjam`
17. `tec-pga-rockclas-2026-08-02-r3l-benkoh`
18. `tec-pga-rockclas-2026-08-02-r3l-bilhor`
19. `tec-pga-rockclas-2026-08-02-r3l-bradal`
20. `tec-pga-rockclas-2026-08-02-r3l-brasne`
21. `tec-pga-rockclas-2026-08-02-r3l-bretod`
22. `tec-pga-rockclas-2026-08-02-r3l-bricam`
23. `tec-pga-rockclas-2026-08-02-r3l-brigar`
24. `tec-pga-rockclas-2026-08-02-r3l-brokoe`
25. `tec-pga-rockclas-2026-08-02-r3l-camdav`
26. `tec-pga-rockclas-2026-08-02-r3l-camyou`
27. `tec-pga-rockclas-2026-08-02-r3l-chabla`
28. `tec-pga-rockclas-2026-08-02-r3l-chaphi`
29. `tec-pga-rockclas-2026-08-02-r3l-charam`
30. `tec-pga-rockclas-2026-08-02-r3l-chrbez`
31. `tec-pga-rockclas-2026-08-02-r3l-chrgot`
32. `tec-pga-rockclas-2026-08-02-r3l-chrkir`
33. `tec-pga-rockclas-2026-08-02-r3l-chrlam`
34. `tec-pga-rockclas-2026-08-02-r3l-corcon`
35. `tec-pga-rockclas-2026-08-02-r3l-danaza`
36. `tec-pga-rockclas-2026-08-02-r3l-danwal`
37. `tec-pga-rockclas-2026-08-02-r3l-davcha`
38. `tec-pga-rockclas-2026-08-02-r3l-davlip`
39. `tec-pga-rockclas-2026-08-02-r3l-davril`
40. `tec-pga-rockclas-2026-08-02-r3l-davtho`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-24 | ~$133.49 | $135.19 | 101% |
| 2026-07-23 | ~$136.30 | $227.63 | 167% |
| 2026-07-22 | ~$110.63 | $82.95 | 75% |

Biggest gaps on 2026-07-24: `opdc-mcconnell-resign-2026-11-02` (est ~$25.83 → got $12.25), `pvwc-housepopw-2026-11-03-dem` (est ~$7.47 → got $2.62), `pvwc-housepopw-2026-11-03-rep` (est ~$12.57 → got $10.29)

_2026-07-25 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (52,088 resting) | ~40.9% | ~$10.22 |
| `enwc-usgubp-sd-2026-06-02-rep-tobdoe` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (26,515 resting) | ~37.4% | ~$9.35 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (84,422 resting) | ~35.4% | ~$8.84 |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $100.00 ÷ 3 | 0.50 | 2,000 | SELL side (71,358 resting) | ~40.2% | ~$6.70 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (95,029 resting) | ~22.7% | ~$5.67 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (45,299 resting) | ~16.9% | ~$4.24 |
| `paccc-usho-midterms-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (317,052 resting) | ~12.8% | ~$3.19 |
| `enwc-usgubp-sd-2026-06-02-rep-larrho` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (27,695 resting) | ~12.6% | ~$3.16 |
| `ewc-usgub-ks-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (99,318 resting) | ~10.0% | ~$2.51 |
| `ewc-usgub-ks-2026-11-03-dem` | $100.00 ÷ 2 | 0.50 | 2,000 | SELL side (221,557 resting) | ~9.0% | ~$2.26 |
| `ewc-usgub-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.50 | 2,000 | BUY side (80,847 resting) | ~7.0% | ~$1.76 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $100.00 ÷ 3 | 0.50 | 2,000 | BUY side (150,315 resting) | ~8.4% | ~$1.41 |

## Totals

| | Amount |
|---|---:|
| Paid | $155.84 |
| Pending | $805.25 |
| Skipped | $1.21 |
| **Total earned** | **$962.30** |

567 reward rows · 23 days with rewards · 258 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-25 ⚠️ multi-day pending bucket | $125.69 | `███████████` |
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
| 2026-07-12 | $39.90 | `████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $962.30 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $57.61 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.10 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $37.74 |
| `apdc-jerpowgov-2026-12-31` | $37.66 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `opdc-mcconnell-resign-2026-11-02` | $29.79 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.65 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $27.08 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $25.71 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.50 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $23.10 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $21.90 |
| `vmc-ussep-misen-2026-08-04-ste05-10` | $21.89 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-27 6:30 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:47 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:32 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:13 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:06 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 3:59 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 3:51 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 2:51 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 2:23 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 2:08 PM ET | ✅ ok | 567 | $962.30 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
