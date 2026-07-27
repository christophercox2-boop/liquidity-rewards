# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-27 3:51 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$73.28/day estimated (ceiling, not promise — details below)

**Earned:** $962.30 lifetime ($155.84 paid). Last three recorded days — 2026-07-25: **$125.69** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-24: **$135.19** · 2026-07-23: **$227.63** _(Polymarket reports ~1–2 days behind)_


---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$73.28/day (~$3.05/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-48` | SELL | 8.0¢ | 53 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (103,544 resting ≥ 2,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 5.0¢ | 127 | 0 | $100.00 | ✅ scoring — ~98.7% of ask side (6,246 resting ≥ 2,000 ✓) ≈ $4.11/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 22.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~97.0% of ask side (61,699 resting ≥ 2,000 ✓) ≈ $4.85/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~97.0% of ask side (217,956 resting ≥ 2,000 ✓) ≈ $3.73/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 17.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~89.1% of bid side (200,552 resting ≥ 2,000 ✓) ≈ $3.43/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 27.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~76.1% of ask side (99,478 resting ≥ 2,000 ✓) ≈ $3.81/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 2.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~76.0% of ask side (43,454 resting ≥ 2,000 ✓) ≈ $3.80/day (pool ÷ 10 markets) |
| `ewc-pres-fra-2027-04-11-edophi` | BUY | 16.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~57.6% of bid side (25,624 resting ≥ 2,000 ✓) ≈ $2.62/day (pool ÷ 11 markets) |
| `cranc-uspres28-12-31-2026-hunbid` | BUY | 13.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~53.1% of bid side (50,383 resting ≥ 2,000 ✓) ≈ $0.80/day (pool ÷ 33 markets) |
| `pintc-meet-put-zel-2026-12-31` | BUY | 8.0¢ | 200 | 2 | $100.00 | ✅ scoring — ~45.2% of bid side (27,846 resting ≥ 2,000 ✓) ≈ $7.54/day (pool ÷ 3 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 25.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~31.4% of bid side (10,653 resting ≥ 2,000 ✓) ≈ $15.70/day |
| `cranc-uspres28-12-31-2026-andyan` | BUY | 11.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~28.0% of bid side (50,452 resting ≥ 2,000 ✓) ≈ $0.42/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-robken` | BUY | 9.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~24.2% of bid side (70,339 resting ≥ 2,000 ✓) ≈ $0.37/day (pool ÷ 33 markets) |
| `lawec-cryptoleg-2026-08-10` | BUY | 5.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~23.2% of bid side (2,398 resting ≥ 2,000 ✓) ≈ $5.79/day (pool ÷ 2 markets) |
| `pintc-meet-put-zel-2026-09-30` | BUY | 7.0¢ | 156 | 2 | $100.00 | ✅ scoring — ~22.7% of bid side (30,620 resting ≥ 2,000 ✓) ≈ $3.78/day (pool ÷ 3 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 12.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~19.4% of bid side (207,223 resting ≥ 2,000 ✓) ≈ $0.75/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 27.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~19.1% of ask side (99,478 resting ≥ 2,000 ✓) ≈ $0.96/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 26.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~14.0% of bid side (10,362 resting ≥ 2,000 ✓) ≈ $0.70/day (pool ÷ 10 markets) |
| `cranc-uspres28-12-31-2026-elomus` | BUY | 6.0¢ | 200 | 2 | $100.00 | ✅ scoring — ~13.0% of bid side (40,736 resting ≥ 2,000 ✓) ≈ $0.20/day (pool ÷ 33 markets) |
| `vtc-hrep-to-2026-11-03-115-120m` | BUY | 17.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~12.2% of bid side (78,076 resting ≥ 2,000 ✓) ≈ $0.61/day (pool ÷ 10 markets) |
| `lawec-saveact-2026-12-31` | BUY | 15.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~6.4% of bid side (39,491 resting ≥ 2,000 ✓) ≈ $1.61/day (pool ÷ 2 markets) |
| `vtc-hrep-to-2026-11-03-90-95m` | BUY | 1.0¢ | 1,000 | 4 | $100.00 | ✅ scoring — ~4.2% of bid side (23,644 resting ≥ 2,000 ✓) ≈ $0.21/day (pool ÷ 10 markets) |
| `ewc-pres-fra-2027-04-11-domvil` | BUY | 5.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~4.2% of bid side (18,525 resting ≥ 2,000 ✓) ≈ $0.19/day (pool ÷ 11 markets) |
| `vtc-hrep-to-2026-11-03-lt90m` | BUY | 1.0¢ | 1,000 | 4 | $100.00 | ✅ scoring — ~4.1% of bid side (24,149 resting ≥ 2,000 ✓) ≈ $0.21/day (pool ÷ 10 markets) |
| `vtc-hrep-to-2026-11-03-110-115m` | BUY | 11.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~3.9% of bid side (78,462 resting ≥ 2,000 ✓) ≈ $0.20/day (pool ÷ 10 markets) |
| `opdc-trump-resig-2027-12-31` | BUY | 5.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~3.1% of bid side (97,265 resting ≥ 2,000 ✓) ≈ $0.77/day (pool ÷ 2 markets) |
| `vmc-ussep-misen-2026-08-04-els15-20` | SELL | 14.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~2.9% of ask side (39,610 resting ≥ 2,000 ✓) ≈ $0.15/day (pool ÷ 10 markets) |
| `mlaec-isrpol-pm-2026-10-27-nafben` | BUY | 1.0¢ | 1,000 | 9 | $100.00 | ✅ scoring — ~2.9% of bid side (31,781 resting ≥ 2,000 ✓) ≈ $0.14/day (pool ÷ 10 markets) |
| `iarc-group-2026-12-31-joebid` | BUY | 1.0¢ | 1,000 | 4 | $100.00 | ✅ scoring — ~2.7% of bid side (36,502 resting ≥ 2,000 ✓) ≈ $0.14/day (pool ÷ 10 markets) |
| `tec-cbb-champ-2027-04-05-w-vcu` | SELL | 2.0¢ | 10 | 0 | $500.00 | ✅ scoring — ~2.7% of ask side (414,016 resting ≥ 2,500 ✓) ≈ $0.09/day (pool ÷ 73 markets) |
| …and 11 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 53 @ 8¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 53 (53 yours) | ×0.5^0 = 52.6 |
|  | 20¢ | 2 | ×0.5^12 = 0.0 |
|  | 30¢ | 2 | ×0.5^22 = 0.0 |
|  | 50¢ | 100 | ×0.5^42 = 0.0 |
|  | 97¢ | 53,892 | ×0.5^89 = 0.0 |
| | | **Σ** | **52.6** |

`yours 52.6 / Σ 52.6 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 127 @ 5¢ → $4.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 127 (127 yours) | ×0.5^0 = 127.3 |
|  | 10¢ | 52 | ×0.5^5 = 1.6 |
|  | 20¢ | 2 | ×0.5^15 = 0.0 |
|  | 23¢ | 50 | ×0.5^18 = 0.0 |
|  | 30¢ | 4 | ×0.5^25 = 0.0 |
|  | 40¢ | 1 | ×0.5^35 = 0.0 |
|  | 50¢ | 25 | ×0.5^45 = 0.0 |
|  | 99¢ | 5,985 | ×0.5^94 = 0.0 |
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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> SELL 30 @ 22¢ → $4.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 30 (30 yours) | ×0.5^0 = 30.0 |
|  | 28¢ | 34 | ×0.5^6 = 0.5 |
|  | 29¢ | 50 | ×0.5^7 = 0.4 |
|  | 30¢ | 2 | ×0.5^8 = 0.0 |
|  | 45¢ | 25 | ×0.5^23 = 0.0 |
|  | 97¢ | 5 | ×0.5^75 = 0.0 |
|  | 98¢ | 61,053 | ×0.5^76 = 0.0 |
| | | **Σ** | **30.9** |

`yours 30.0 / Σ 30.9 = 97.0%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 97.0% = $4.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 100 @ 20¢ → $3.73/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 100 (100 yours) | ×0.5^0 = 100.0 |
|  | 24¢ | 50 | ×0.5^4 = 3.1 |
|  | 30¢ | 4 | ×0.5^10 = 0.0 |
|  | 33¢ | 5 | ×0.5^13 = 0.0 |
|  | 50¢ | 100 | ×0.5^30 = 0.0 |
|  | 98¢ | 131,484 | ×0.5^78 = 0.0 |
| | | **Σ** | **103.1** |

`yours 100.0 / Σ 103.1 = 97.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 97.0% = $3.73/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 100 @ 17¢ → $3.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 100 (100 yours) | ×0.5^0 = 100.0 |
|  | 5¢ | 2 | ×0.5^12 = 0.0 |
|  | 3¢ | 200,250 | ×0.5^14 = 12.2 |
| | | **Σ** | **112.2** |

`yours 100.0 / Σ 112.2 = 89.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 89.1% = $3.43/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 9 @ 27¢ → $3.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 11 (9 yours) | ×0.5^0 = 11.3 |
|  | 30¢ | 2 | ×0.5^3 = 0.2 |
|  | 33¢ | 6 | ×0.5^6 = 0.1 |
|  | 34¢ | 28 | ×0.5^7 = 0.2 |
|  | 45¢ | 25 | ×0.5^18 = 0.0 |
|  | 98¢ | 98,906 | ×0.5^71 = 0.0 |
| | | **Σ** | **11.8** |

`yours 9.0 / Σ 11.8 = 76.1%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 76.1% = $3.81/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 2¢ → $3.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 1 (1 yours) | ×0.5^0 = 1.0 |
|  | 8¢ | 6 | ×0.5^6 = 0.1 |
|  | 9¢ | 28 | ×0.5^7 = 0.2 |
|  | 16¢ | 50 | ×0.5^14 = 0.0 |
|  | 20¢ | 2 | ×0.5^18 = 0.0 |
|  | 30¢ | 2 | ×0.5^28 = 0.0 |
|  | 43¢ | 3,387 | ×0.5^41 = 0.0 |
| | | **Σ** | **1.3** |

`yours 1.0 / Σ 1.3 = 76.0%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 76.0% = $3.80/day`  

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
<details><summary><code>ewc-pres-fra-2027-04-11-edophi</code> BUY 100 @ 16¢ → $2.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 36 | ×0.5^0 = 36.0 |
| ▶ | 16¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 5¢ | 2 | ×0.5^12 = 0.0 |
|  | 2¢ | 25,286 | ×0.5^15 = 0.8 |
| | | **Σ** | **86.8** |

`yours 50.0 / Σ 86.8 = 57.6%`  
`$100 ÷ 11 ÷ 2 = $4.55 × 57.6% = $2.62/day`  

<details><summary>÷ 11 markets in this race — tap to list</summary>

1. `ewc-pres-fra-2027-04-11-bruret`
2. `ewc-pres-fra-2027-04-11-davlis`
3. `ewc-pres-fra-2027-04-11-domvil`
4. `ewc-pres-fra-2027-04-11-edophi` ← this one
5. `ewc-pres-fra-2027-04-11-frahol`
6. `ewc-pres-fra-2027-04-11-gabatt`
7. `ewc-pres-fra-2027-04-11-jeamel`
8. `ewc-pres-fra-2027-04-11-jorbar`
9. `ewc-pres-fra-2027-04-11-marlep`
10. `ewc-pres-fra-2027-04-11-rapglu`
11. `ewc-pres-fra-2027-04-11-sarkna`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-hunbid</code> BUY 100 @ 13¢ → $0.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 15¢ | 13 | ×0.5^0 = 13.0 |
|  | 14¢ | 12 | ×0.5^1 = 6.0 |
| ▶ | 13¢ | 100 (100 yours) | ×0.5^2 = 25.0 |
|  | 5¢ | 2 | ×0.5^10 = 0.0 |
|  | 1¢ | 50,256 | ×0.5^14 = 3.1 |
| | | **Σ** | **47.1** |

`yours 25.0 / Σ 47.1 = 53.1%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 53.1% = $0.80/day`  

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
13. `cranc-uspres28-12-31-2026-hunbid` ← this one
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
<details><summary><code>pintc-meet-put-zel-2026-12-31</code> BUY 200 @ 8¢ → $7.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.5^0 = 2.0 |
|  | 9¢ | 1 | ×0.5^1 = 0.5 |
| ▶ | 8¢ | 200 (200 yours) | ×0.5^2 = 50.0 |
|  | 5¢ | 2 | ×0.5^5 = 0.1 |
|  | 3¢ | 7,416 | ×0.5^7 = 57.9 |
| | | **Σ** | **110.5** |

`yours 50.0 / Σ 110.5 = 45.2%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 45.2% = $7.54/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `pintc-meet-put-zel-2026-07-31`
2. `pintc-meet-put-zel-2026-09-30`
3. `pintc-meet-put-zel-2026-12-31` ← this one

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 20 @ 25¢ → $15.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 46 (20 yours) | ×0.5^0 = 46.0 |
|  | 23¢ | 64 | ×0.5^2 = 16.0 |
|  | 20¢ | 48 | ×0.5^5 = 1.5 |
|  | 17¢ | 54 | ×0.5^8 = 0.2 |
|  | 5¢ | 2 | ×0.5^20 = 0.0 |
|  | 4¢ | 239 | ×0.5^21 = 0.0 |
|  | 2¢ | 10,000 | ×0.5^23 = 0.0 |
| | | **Σ** | **63.7** |

`yours 20.0 / Σ 63.7 = 31.4%`  
`$100 ÷ 1 ÷ 2 = $50.00 × 31.4% = $15.70/day`  

</details>
<details><summary><code>cranc-uspres28-12-31-2026-andyan</code> BUY 100 @ 11¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 21 | ×0.5^0 = 21.0 |
|  | 12¢ | 62 | ×0.5^1 = 31.1 |
| ▶ | 11¢ | 100 (100 yours) | ×0.5^2 = 25.0 |
|  | 5¢ | 2 | ×0.5^8 = 0.0 |
|  | 1¢ | 50,267 | ×0.5^12 = 12.3 |
| | | **Σ** | **89.4** |

`yours 25.0 / Σ 89.4 = 28.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 28.0% = $0.42/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan` ← this one
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
<details><summary><code>cranc-uspres28-12-31-2026-robken</code> BUY 100 @ 9¢ → $0.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 3 | ×0.5^0 = 3.0 |
|  | 10¢ | 5 | ×0.5^1 = 2.5 |
| ▶ | 9¢ | 116 (100 yours) | ×0.5^2 = 29.0 |
|  | 6¢ | 6 | ×0.5^5 = 0.2 |
|  | 5¢ | 2 | ×0.5^6 = 0.0 |
|  | 1¢ | 70,207 | ×0.5^10 = 68.6 |
| | | **Σ** | **103.3** |

`yours 25.0 / Σ 103.3 = 24.2%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 24.2% = $0.37/day`  

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
20. `cranc-uspres28-12-31-2026-markel`
21. `cranc-uspres28-12-31-2026-marrub`
22. `cranc-uspres28-12-31-2026-micoba`
23. `cranc-uspres28-12-31-2026-nikhal`
24. `cranc-uspres28-12-31-2026-oprwin`
25. `cranc-uspres28-12-31-2026-petbut`
26. `cranc-uspres28-12-31-2026-rahema`
27. `cranc-uspres28-12-31-2026-robken` ← this one
28. `cranc-uspres28-12-31-2026-steban`
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>lawec-cryptoleg-2026-08-10</code> BUY 100 @ 5¢ → $5.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 36 | ×0.5^0 = 36.0 |
| ▶ | 5¢ | 102 (100 yours) | ×0.5^1 = 51.0 |
|  | 2¢ | 2,060 | ×0.5^4 = 128.8 |
| | | **Σ** | **215.8** |

`yours 50.0 / Σ 215.8 = 23.2%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 23.2% = $5.79/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-cryptoleg-2026-08-10` ← this one
2. `lawec-cryptoleg-2026-12-31`

</details>

</details>
<details><summary><code>pintc-meet-put-zel-2026-09-30</code> BUY 156 @ 7¢ → $3.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 14 | ×0.5^0 = 14.0 |
| ▶ | 7¢ | 156 (156 yours) | ×0.5^2 = 39.0 |
|  | 5¢ | 2 | ×0.5^4 = 0.1 |
|  | 1¢ | 30,448 | ×0.5^8 = 118.9 |
| | | **Σ** | **172.1** |

`yours 39.0 / Σ 172.1 = 22.7%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 22.7% = $3.78/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `pintc-meet-put-zel-2026-07-31`
2. `pintc-meet-put-zel-2026-09-30` ← this one
3. `pintc-meet-put-zel-2026-12-31`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 100 @ 12¢ → $0.75/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 5 | ×0.5^0 = 5.0 |
| ▶ | 12¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 5¢ | 2 | ×0.5^8 = 0.0 |
|  | 3¢ | 206,916 | ×0.5^10 = 202.1 |
| | | **Σ** | **257.1** |

`yours 50.0 / Σ 257.1 = 19.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 19.4% = $0.75/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 2 @ 27¢ → $0.96/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 11 (2 yours) | ×0.5^0 = 11.3 |
|  | 30¢ | 2 | ×0.5^3 = 0.2 |
|  | 33¢ | 6 | ×0.5^6 = 0.1 |
|  | 34¢ | 28 | ×0.5^7 = 0.2 |
|  | 45¢ | 25 | ×0.5^18 = 0.0 |
|  | 98¢ | 98,906 | ×0.5^71 = 0.0 |
| | | **Σ** | **11.8** |

`yours 2.3 / Σ 11.8 = 19.1%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 19.1% = $0.96/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 9 @ 26¢ → $0.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 62 (9 yours) | ×0.5^0 = 62.4 |
|  | 20¢ | 6 | ×0.5^6 = 0.1 |
|  | 18¢ | 28 | ×0.5^8 = 0.1 |
|  | 5¢ | 2 | ×0.5^21 = 0.0 |
|  | 3¢ | 10,250 | ×0.5^23 = 0.0 |
| | | **Σ** | **62.6** |

`yours 8.7 / Σ 62.6 = 14.0%`  
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
<details><summary><code>cranc-uspres28-12-31-2026-elomus</code> BUY 200 @ 6¢ → $0.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 14 | ×0.5^0 = 14.0 |
| ▶ | 6¢ | 220 (200 yours) | ×0.5^2 = 55.0 |
|  | 5¢ | 2 | ×0.5^3 = 0.2 |
|  | 1¢ | 40,500 | ×0.5^7 = 316.4 |
| | | **Σ** | **385.7** |

`yours 50.0 / Σ 385.7 = 13.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 13.0% = $0.20/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru`
7. `cranc-uspres28-12-31-2026-dontrujr`
8. `cranc-uspres28-12-31-2026-dwajoh`
9. `cranc-uspres28-12-31-2026-elomus` ← this one
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
<details><summary><code>vtc-hrep-to-2026-11-03-115-120m</code> BUY 100 @ 17¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 200 | ×0.5^0 = 200.0 |
| ▶ | 17¢ | 100 (100 yours) | ×0.5^1 = 50.0 |
|  | 16¢ | 62 | ×0.5^2 = 15.6 |
|  | 15¢ | 28 | ×0.5^3 = 3.5 |
|  | 14¢ | 2,241 | ×0.5^4 = 140.1 |
| | | **Σ** | **409.2** |

`yours 50.0 / Σ 409.2 = 12.2%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 12.2% = $0.61/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vtc-hrep-to-2026-11-03-100-105m`
2. `vtc-hrep-to-2026-11-03-105-110m`
3. `vtc-hrep-to-2026-11-03-110-115m`
4. `vtc-hrep-to-2026-11-03-115-120m` ← this one
5. `vtc-hrep-to-2026-11-03-120-125m`
6. `vtc-hrep-to-2026-11-03-125-130m`
7. `vtc-hrep-to-2026-11-03-90-95m`
8. `vtc-hrep-to-2026-11-03-95-100m`
9. `vtc-hrep-to-2026-11-03-gte130m`
10. `vtc-hrep-to-2026-11-03-lt90m`

</details>

</details>
<details><summary><code>lawec-saveact-2026-12-31</code> BUY 100 @ 15¢ → $1.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 689 (100 yours) | ×0.5^0 = 689.3 |
|  | 14¢ | 1,731 | ×0.5^1 = 865.7 |
| | | **Σ** | **1,555.1** |

`yours 100.0 / Σ 1,555.1 = 6.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 6.4% = $1.61/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `lawec-saveact-2026-08-31`
2. `lawec-saveact-2026-12-31` ← this one

</details>

</details>
<details><summary><code>vtc-hrep-to-2026-11-03-90-95m</code> BUY 1,000 @ 1¢ → $0.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 2 | ×0.5^0 = 2.0 |
| ▶ | 1¢ | 23,642 (1,000 yours) | ×0.5^4 = 1,477.6 |
| | | **Σ** | **1,479.6** |

`yours 62.5 / Σ 1,479.6 = 4.2%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 4.2% = $0.21/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vtc-hrep-to-2026-11-03-100-105m`
2. `vtc-hrep-to-2026-11-03-105-110m`
3. `vtc-hrep-to-2026-11-03-110-115m`
4. `vtc-hrep-to-2026-11-03-115-120m`
5. `vtc-hrep-to-2026-11-03-120-125m`
6. `vtc-hrep-to-2026-11-03-125-130m`
7. `vtc-hrep-to-2026-11-03-90-95m` ← this one
8. `vtc-hrep-to-2026-11-03-95-100m`
9. `vtc-hrep-to-2026-11-03-gte130m`
10. `vtc-hrep-to-2026-11-03-lt90m`

</details>

</details>
<details><summary><code>ewc-pres-fra-2027-04-11-domvil</code> BUY 200 @ 5¢ → $0.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 7 | ×0.5^0 = 7.0 |
| ▶ | 5¢ | 202 (200 yours) | ×0.5^1 = 101.0 |
|  | 3¢ | 18,116 | ×0.5^3 = 2,264.5 |
| | | **Σ** | **2,372.5** |

`yours 100.0 / Σ 2,372.5 = 4.2%`  
`$100 ÷ 11 ÷ 2 = $4.55 × 4.2% = $0.19/day`  

<details><summary>÷ 11 markets in this race — tap to list</summary>

1. `ewc-pres-fra-2027-04-11-bruret`
2. `ewc-pres-fra-2027-04-11-davlis`
3. `ewc-pres-fra-2027-04-11-domvil` ← this one
4. `ewc-pres-fra-2027-04-11-edophi`
5. `ewc-pres-fra-2027-04-11-frahol`
6. `ewc-pres-fra-2027-04-11-gabatt`
7. `ewc-pres-fra-2027-04-11-jeamel`
8. `ewc-pres-fra-2027-04-11-jorbar`
9. `ewc-pres-fra-2027-04-11-marlep`
10. `ewc-pres-fra-2027-04-11-rapglu`
11. `ewc-pres-fra-2027-04-11-sarkna`

</details>

</details>
<details><summary><code>vtc-hrep-to-2026-11-03-lt90m</code> BUY 1,000 @ 1¢ → $0.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 2 | ×0.5^0 = 2.0 |
| ▶ | 1¢ | 24,147 (1,000 yours) | ×0.5^4 = 1,509.2 |
| | | **Σ** | **1,511.2** |

`yours 62.5 / Σ 1,511.2 = 4.1%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 4.1% = $0.21/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vtc-hrep-to-2026-11-03-100-105m`
2. `vtc-hrep-to-2026-11-03-105-110m`
3. `vtc-hrep-to-2026-11-03-110-115m`
4. `vtc-hrep-to-2026-11-03-115-120m`
5. `vtc-hrep-to-2026-11-03-120-125m`
6. `vtc-hrep-to-2026-11-03-125-130m`
7. `vtc-hrep-to-2026-11-03-90-95m`
8. `vtc-hrep-to-2026-11-03-95-100m`
9. `vtc-hrep-to-2026-11-03-gte130m`
10. `vtc-hrep-to-2026-11-03-lt90m` ← this one

</details>

</details>
<details><summary><code>vtc-hrep-to-2026-11-03-110-115m</code> BUY 100 @ 11¢ → $0.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 36 | ×0.5^0 = 36.0 |
|  | 12¢ | 28 | ×0.5^1 = 14.0 |
| ▶ | 11¢ | 2,355 (100 yours) | ×0.5^2 = 588.8 |
| | | **Σ** | **638.8** |

`yours 25.0 / Σ 638.8 = 3.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 3.9% = $0.20/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vtc-hrep-to-2026-11-03-100-105m`
2. `vtc-hrep-to-2026-11-03-105-110m`
3. `vtc-hrep-to-2026-11-03-110-115m` ← this one
4. `vtc-hrep-to-2026-11-03-115-120m`
5. `vtc-hrep-to-2026-11-03-120-125m`
6. `vtc-hrep-to-2026-11-03-125-130m`
7. `vtc-hrep-to-2026-11-03-90-95m`
8. `vtc-hrep-to-2026-11-03-95-100m`
9. `vtc-hrep-to-2026-11-03-gte130m`
10. `vtc-hrep-to-2026-11-03-lt90m`

</details>

</details>
<details><summary><code>opdc-trump-resig-2027-12-31</code> BUY 100 @ 5¢ → $0.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 30 | ×0.5^0 = 30.0 |
|  | 6¢ | 17 | ×0.5^1 = 8.5 |
| ▶ | 5¢ | 102 (100 yours) | ×0.5^2 = 25.5 |
|  | 3¢ | 11,916 | ×0.5^4 = 744.8 |
| | | **Σ** | **808.8** |

`yours 25.0 / Σ 808.8 = 3.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 3.1% = $0.77/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `opdc-trump-resig-2026-12-31`
2. `opdc-trump-resig-2027-12-31` ← this one

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els15-20</code> SELL 20 @ 14¢ → $0.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 515 (20 yours) | ×0.5^0 = 515.0 |
|  | 15¢ | 344 | ×0.5^1 = 172.0 |
|  | 20¢ | 8 | ×0.5^6 = 0.1 |
|  | 22¢ | 29 | ×0.5^8 = 0.1 |
|  | 30¢ | 2 | ×0.5^16 = 0.0 |
|  | 40¢ | 16 | ×0.5^26 = 0.0 |
|  | 45¢ | 25 | ×0.5^31 = 0.0 |
|  | 98¢ | 38,172 | ×0.5^84 = 0.0 |
| | | **Σ** | **687.2** |

`yours 20.0 / Σ 687.2 = 2.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 2.9% = $0.15/day`  

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
<details><summary><code>mlaec-isrpol-pm-2026-10-27-nafben</code> BUY 1,000 @ 1¢ → $0.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 5 | ×0.5^0 = 5.0 |
|  | 5¢ | 2 | ×0.5^5 = 0.1 |
|  | 3¢ | 100 | ×0.5^7 = 0.8 |
| ▶ | 1¢ | 31,674 (1,000 yours) | ×0.5^9 = 61.9 |
| | | **Σ** | **67.7** |

`yours 2.0 / Σ 67.7 = 2.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 2.9% = $0.14/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `mlaec-isrpol-pm-2026-10-27-avilie`
2. `mlaec-isrpol-pm-2026-10-27-ayesha`
3. `mlaec-isrpol-pm-2026-10-27-bengan`
4. `mlaec-isrpol-pm-2026-10-27-bennet`
5. `mlaec-isrpol-pm-2026-10-27-gadeiz`
6. `mlaec-isrpol-pm-2026-10-27-gidsaa`
7. `mlaec-isrpol-pm-2026-10-27-itaben`
8. `mlaec-isrpol-pm-2026-10-27-nafben` ← this one
9. `mlaec-isrpol-pm-2026-10-27-yailap`
10. `mlaec-isrpol-pm-2026-10-27-yoahen`

</details>

</details>
<details><summary><code>iarc-group-2026-12-31-joebid</code> BUY 1,000 @ 1¢ → $0.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 2 | ×0.5^0 = 2.0 |
| ▶ | 1¢ | 36,500 (1,000 yours) | ×0.5^4 = 2,281.2 |
| | | **Σ** | **2,283.2** |

`yours 62.5 / Σ 2,283.2 = 2.7%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 2.7% = $0.14/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `iarc-group-2026-12-31-antfau`
2. `iarc-group-2026-12-31-baroba`
3. `iarc-group-2026-12-31-bilcli`
4. `iarc-group-2026-12-31-canowe`
5. `iarc-group-2026-12-31-gavnew`
6. `iarc-group-2026-12-31-hilcli`
7. `iarc-group-2026-12-31-joebid` ← this one
8. `iarc-group-2026-12-31-johbre`
9. `iarc-group-2026-12-31-tomhom`
10. `iarc-group-2026-12-31-tuccar`

</details>

</details>
<details><summary><code>tec-cbb-champ-2027-04-05-w-vcu</code> SELL 10 @ 2¢ → $0.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 110 (10 yours) | ×0.35^0 = 110.0 |
|  | 7¢ | 49,270 | ×0.35^5 = 258.8 |
| | | **Σ** | **368.8** |

`yours 10.0 / Σ 368.8 = 2.7%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 2.7% = $0.09/day`  

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
40. `tec-cbb-champ-2027-04-05-w-nebr`

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
| 2026-07-27 3:51 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 2:51 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 2:23 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 2:08 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 1:58 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 1:49 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 1:27 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 1:13 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 11:59 AM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 11:52 AM ET | ✅ ok | 567 | $962.30 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
