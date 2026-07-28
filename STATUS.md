# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-27 8:14 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$125.97/day estimated (ceiling, not promise — details below)

**Earned:** $962.30 lifetime ($155.84 paid). Last three recorded days — 2026-07-25: **$125.69** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-24: **$135.19** · 2026-07-23: **$227.63** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mi-2026-08-04-dem-abdels` — SELL at the best price, ~$42.55/day for 200 contracts. Runners-up: `enwc-ussep-mi-2026-08-04-dem-halste` (~$20.88/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$17.47/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$125.97/day (~$5.25/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `cranc-uspres28-12-31-2026-marrub` | SELL | 9.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (27,460 resting ≥ 5,000 ✓) ≈ $1.52/day (pool ÷ 33 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 22.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (61,749 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 5.0¢ | 127 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (6,227 resting ≥ 2,000 ✓) ≈ $1.04/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 26.0¢ | 9 | 0 | $25.00 | ✅ scoring — ~99.9% of bid side (10,334 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 2.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (43,505 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 27.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (99,573 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `tec-pga-rockclas-2026-08-02-r2l-andnov` | BUY | 1.0¢ | 2,125 | 0 | $10,000.00 | ✅ scoring — ~99.9% of bid side (14,625 resting ≥ 10,000 ✓) ≈ $2.01/day (pool ÷ 146 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-r2l-harhal` | BUY | 1.0¢ | 2,125 | 0 | $10,000.00 | ✅ scoring — ~99.7% of bid side (10,708 resting ≥ 10,000 ✓) ≈ $2.01/day (pool ÷ 146 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-r3l-wilmou` | BUY | 1.0¢ | 871 | 0 | $10,000.00 | ✅ scoring — ~99.7% of bid side (27,108 resting ≥ 10,000 ✓) ≈ $9.46/day (pool ÷ 31 markets) (pre-tournament pool over 17d) |
| `tec-pga-rockclas-2026-08-02-r2l-jessve` | BUY | 1.0¢ | 2,125 | 0 | $10,000.00 | ✅ scoring — ~99.7% of bid side (11,708 resting ≥ 10,000 ✓) ≈ $2.01/day (pool ÷ 146 markets) (pre-tournament pool over 17d) |
| `scc-senate-gop-2026-11-03-50` | BUY | 13.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~83.3% of bid side (207,068 resting ≥ 5,000 ✓) ≈ $3.20/day (pool ÷ 13 markets) |
| `iarc-group-2026-12-31-joebid` | BUY | 4.0¢ | 200 | 1 | $25.00 | ✅ scoring — ~78.3% of bid side (35,677 resting ≥ 2,000 ✓) ≈ $0.98/day (pool ÷ 10 markets) |
| `cranc-uspres28-12-31-2026-krinoe` | BUY | 6.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~74.9% of bid side (30,672 resting ≥ 5,000 ✓) ≈ $1.14/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 9.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~74.0% of bid side (50,334 resting ≥ 5,000 ✓) ≈ $2.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 9.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~73.9% of bid side (100,334 resting ≥ 5,000 ✓) ≈ $2.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 9.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~73.9% of bid side (120,359 resting ≥ 5,000 ✓) ≈ $2.84/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-stesmi` | BUY | 8.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~72.5% of bid side (20,662 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 33 markets) |
| `mlaec-isrpol-pm-2026-10-27-yailap` | BUY | 4.0¢ | 100 | 1 | $25.00 | ✅ scoring — ~70.2% of bid side (22,549 resting ≥ 2,000 ✓) ≈ $0.88/day (pool ÷ 10 markets) |
| `iarc-group-2026-12-31-tuccar` | BUY | 4.0¢ | 100 | 1 | $25.00 | ✅ scoring — ~70.2% of bid side (22,587 resting ≥ 2,000 ✓) ≈ $0.88/day (pool ÷ 10 markets) |
| `mlaec-isrpol-pm-2026-10-27-ayesha` | BUY | 4.0¢ | 100 | 1 | $25.00 | ✅ scoring — ~70.2% of bid side (22,605 resting ≥ 2,000 ✓) ≈ $0.88/day (pool ÷ 10 markets) |
| `cranc-uspres28-12-31-2026-dontru` | BUY | 8.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~66.3% of bid side (120,713 resting ≥ 5,000 ✓) ≈ $1.00/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 8.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~65.4% of bid side (220,329 resting ≥ 5,000 ✓) ≈ $2.52/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-erikir` | BUY | 8.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~64.4% of bid side (17,110 resting ≥ 5,000 ✓) ≈ $0.98/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 8.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~64.3% of bid side (30,559 resting ≥ 5,000 ✓) ≈ $2.47/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 8.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~64.3% of bid side (30,559 resting ≥ 5,000 ✓) ≈ $2.47/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 8.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~64.3% of bid side (30,584 resting ≥ 5,000 ✓) ≈ $2.47/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-markel` | BUY | 7.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~63.6% of bid side (70,679 resting ≥ 5,000 ✓) ≈ $0.96/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 8.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~56.8% of bid side (70,309 resting ≥ 5,000 ✓) ≈ $2.19/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-elomus` | BUY | 7.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~56.6% of bid side (40,611 resting ≥ 5,000 ✓) ≈ $0.86/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 8.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~49.8% of bid side (70,589 resting ≥ 5,000 ✓) ≈ $1.91/day (pool ÷ 13 markets) |
| …and 218 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>cranc-uspres28-12-31-2026-marrub</code> SELL 31 @ 9¢ → $1.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 31 (31 yours) | ×0.2^0 = 30.6 |
|  | 20¢ | 3 | ×0.2^11 = 0.0 |
|  | 22¢ | 60 | ×0.2^13 = 0.0 |
|  | 30¢ | 2 | ×0.2^21 = 0.0 |
|  | 42¢ | 50 | ×0.2^33 = 0.0 |
|  | 49¢ | 50 | ×0.2^40 = 0.0 |
|  | 50¢ | 50 | ×0.2^41 = 0.0 |
|  | 57¢ | 26 | ×0.2^48 = 0.0 |
|  | 65¢ | 875 | ×0.2^56 = 0.0 |
|  | 66¢ | 810 | ×0.2^57 = 0.0 |
| | … | +1 levels | 0.0 |
| | | **Σ** | **30.7** |

`yours 30.6 / Σ 30.7 = 100.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 100.0% = $1.52/day`  

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
21. `cranc-uspres28-12-31-2026-marrub` ← this one
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
<details><summary><code>vmc-ussep-misen-2026-08-04-els10-15</code> SELL 30 @ 22¢ → $1.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 30 (30 yours) | ×0.1^0 = 30.0 |
|  | 28¢ | 34 | ×0.1^6 = 0.0 |
|  | 29¢ | 100 | ×0.1^7 = 0.0 |
|  | 30¢ | 2 | ×0.1^8 = 0.0 |
|  | 45¢ | 25 | ×0.1^23 = 0.0 |
|  | 97¢ | 5 | ×0.1^75 = 0.0 |
|  | 98¢ | 61,053 | ×0.1^76 = 0.0 |
| | | **Σ** | **30.0** |

`yours 30.0 / Σ 30.0 = 100.0%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 100.0% = $1.25/day`  

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
<details><summary><code>enwc-ussep-sc-2026-08-11-rep-marlyn</code> SELL 127 @ 5¢ → $1.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 127 (127 yours) | ×0.1^0 = 127.3 |
|  | 10¢ | 75 | ×0.1^5 = 0.0 |
|  | 20¢ | 3 | ×0.1^15 = 0.0 |
|  | 30¢ | 4 | ×0.1^25 = 0.0 |
|  | 40¢ | 1 | ×0.1^35 = 0.0 |
|  | 50¢ | 25 | ×0.1^45 = 0.0 |
|  | 99¢ | 5,992 | ×0.1^94 = 0.0 |
| | | **Σ** | **127.4** |

`yours 127.3 / Σ 127.4 = 100.0%`  
`$25 ÷ 12 ÷ 2 = $1.04 × 100.0% = $1.04/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> BUY 9 @ 26¢ → $1.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 9 (9 yours) | ×0.1^0 = 8.7 |
|  | 23¢ | 6 | ×0.1^3 = 0.0 |
|  | 21¢ | 28 | ×0.1^5 = 0.0 |
|  | 5¢ | 2 | ×0.1^21 = 0.0 |
|  | 3¢ | 10,250 | ×0.1^23 = 0.0 |
| | | **Σ** | **8.7** |

`yours 8.7 / Σ 8.7 = 99.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 99.9% = $1.25/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 2¢ → $1.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 6¢ | 6 | ×0.1^4 = 0.0 |
|  | 7¢ | 28 | ×0.1^5 = 0.0 |
|  | 16¢ | 100 | ×0.1^14 = 0.0 |
|  | 20¢ | 3 | ×0.1^18 = 0.0 |
|  | 30¢ | 2 | ×0.1^28 = 0.0 |
|  | 43¢ | 3,387 | ×0.1^41 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 99.9% = $1.25/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-els0-5</code> SELL 2 @ 27¢ → $1.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 2 (2 yours) | ×0.1^0 = 2.3 |
|  | 30¢ | 2 | ×0.1^3 = 0.0 |
|  | 31¢ | 4 | ×0.1^4 = 0.0 |
|  | 33¢ | 34 | ×0.1^6 = 0.0 |
|  | 39¢ | 100 | ×0.1^12 = 0.0 |
|  | 45¢ | 25 | ×0.1^18 = 0.0 |
|  | 98¢ | 98,906 | ×0.1^71 = 0.0 |
| | | **Σ** | **2.3** |

`yours 2.3 / Σ 2.3 = 99.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 99.9% = $1.25/day`  

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
<details><summary><code>tec-pga-rockclas-2026-08-02-r2l-andnov</code> BUY 2,125 @ 1¢ → $2.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,125 (2,125 yours) | ×0.35^0 = 2,125.0 |
|  | 0.2¢ | 12,500 | ×0.35^8 = 2.8 |
| | | **Σ** | **2,127.8** |

`yours 2,125.0 / Σ 2,127.8 = 99.9%`  
`$10,000 ÷ 17d ÷ 146 ÷ 2 = $2.01 × 99.9% = $2.01/day`  

<details><summary>÷ 146 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r2l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r2l-adasch`
3. `tec-pga-rockclas-2026-08-02-r2l-adasve`
4. `tec-pga-rockclas-2026-08-02-r2l-adrcha`
5. `tec-pga-rockclas-2026-08-02-r2l-adrsad`
6. `tec-pga-rockclas-2026-08-02-r2l-aewa`
7. `tec-pga-rockclas-2026-08-02-r2l-aksbha`
8. `tec-pga-rockclas-2026-08-02-r2l-aldpot`
9. `tec-pga-rockclas-2026-08-02-r2l-aletos`
10. `tec-pga-rockclas-2026-08-02-r2l-andnov` ← this one
11. `tec-pga-rockclas-2026-08-02-r2l-andput`
12. `tec-pga-rockclas-2026-08-02-r2l-auseck`
13. `tec-pga-rockclas-2026-08-02-r2l-aussmo`
14. `tec-pga-rockclas-2026-08-02-r2l-beahos`
15. `tec-pga-rockclas-2026-08-02-r2l-bengri`
16. `tec-pga-rockclas-2026-08-02-r2l-benjam`
17. `tec-pga-rockclas-2026-08-02-r2l-benkoh`
18. `tec-pga-rockclas-2026-08-02-r2l-bilhor`
19. `tec-pga-rockclas-2026-08-02-r2l-bradal`
20. `tec-pga-rockclas-2026-08-02-r2l-brasne`
21. `tec-pga-rockclas-2026-08-02-r2l-bretod`
22. `tec-pga-rockclas-2026-08-02-r2l-bricam`
23. `tec-pga-rockclas-2026-08-02-r2l-brigar`
24. `tec-pga-rockclas-2026-08-02-r2l-brokoe`
25. `tec-pga-rockclas-2026-08-02-r2l-camdav`
26. `tec-pga-rockclas-2026-08-02-r2l-camyou`
27. `tec-pga-rockclas-2026-08-02-r2l-chabla`
28. `tec-pga-rockclas-2026-08-02-r2l-chaphi`
29. `tec-pga-rockclas-2026-08-02-r2l-charam`
30. `tec-pga-rockclas-2026-08-02-r2l-chrbez`
31. `tec-pga-rockclas-2026-08-02-r2l-chrgot`
32. `tec-pga-rockclas-2026-08-02-r2l-chrkir`
33. `tec-pga-rockclas-2026-08-02-r2l-chrlam`
34. `tec-pga-rockclas-2026-08-02-r2l-corcon`
35. `tec-pga-rockclas-2026-08-02-r2l-danaza`
36. `tec-pga-rockclas-2026-08-02-r2l-danwal`
37. `tec-pga-rockclas-2026-08-02-r2l-davcha`
38. `tec-pga-rockclas-2026-08-02-r2l-davlip`
39. `tec-pga-rockclas-2026-08-02-r2l-davril`
40. `tec-pga-rockclas-2026-08-02-r2l-davtho`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-r2l-harhal</code> BUY 2,125 @ 1¢ → $2.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,125 (2,125 yours) | ×0.35^0 = 2,125.0 |
|  | 0.3¢ | 8,333 | ×0.35^7 = 5.4 |
| | | **Σ** | **2,130.4** |

`yours 2,125.0 / Σ 2,130.4 = 99.7%`  
`$10,000 ÷ 17d ÷ 146 ÷ 2 = $2.01 × 99.7% = $2.01/day`  

<details><summary>÷ 146 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r2l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r2l-adasch`
3. `tec-pga-rockclas-2026-08-02-r2l-adasve`
4. `tec-pga-rockclas-2026-08-02-r2l-adrcha`
5. `tec-pga-rockclas-2026-08-02-r2l-adrsad`
6. `tec-pga-rockclas-2026-08-02-r2l-aewa`
7. `tec-pga-rockclas-2026-08-02-r2l-aksbha`
8. `tec-pga-rockclas-2026-08-02-r2l-aldpot`
9. `tec-pga-rockclas-2026-08-02-r2l-aletos`
10. `tec-pga-rockclas-2026-08-02-r2l-andnov`
11. `tec-pga-rockclas-2026-08-02-r2l-andput`
12. `tec-pga-rockclas-2026-08-02-r2l-auseck`
13. `tec-pga-rockclas-2026-08-02-r2l-aussmo`
14. `tec-pga-rockclas-2026-08-02-r2l-beahos`
15. `tec-pga-rockclas-2026-08-02-r2l-bengri`
16. `tec-pga-rockclas-2026-08-02-r2l-benjam`
17. `tec-pga-rockclas-2026-08-02-r2l-benkoh`
18. `tec-pga-rockclas-2026-08-02-r2l-bilhor`
19. `tec-pga-rockclas-2026-08-02-r2l-bradal`
20. `tec-pga-rockclas-2026-08-02-r2l-brasne`
21. `tec-pga-rockclas-2026-08-02-r2l-bretod`
22. `tec-pga-rockclas-2026-08-02-r2l-bricam`
23. `tec-pga-rockclas-2026-08-02-r2l-brigar`
24. `tec-pga-rockclas-2026-08-02-r2l-brokoe`
25. `tec-pga-rockclas-2026-08-02-r2l-camdav`
26. `tec-pga-rockclas-2026-08-02-r2l-camyou`
27. `tec-pga-rockclas-2026-08-02-r2l-chabla`
28. `tec-pga-rockclas-2026-08-02-r2l-chaphi`
29. `tec-pga-rockclas-2026-08-02-r2l-charam`
30. `tec-pga-rockclas-2026-08-02-r2l-chrbez`
31. `tec-pga-rockclas-2026-08-02-r2l-chrgot`
32. `tec-pga-rockclas-2026-08-02-r2l-chrkir`
33. `tec-pga-rockclas-2026-08-02-r2l-chrlam`
34. `tec-pga-rockclas-2026-08-02-r2l-corcon`
35. `tec-pga-rockclas-2026-08-02-r2l-danaza`
36. `tec-pga-rockclas-2026-08-02-r2l-danwal`
37. `tec-pga-rockclas-2026-08-02-r2l-davcha`
38. `tec-pga-rockclas-2026-08-02-r2l-davlip`
39. `tec-pga-rockclas-2026-08-02-r2l-davril`
40. `tec-pga-rockclas-2026-08-02-r2l-davtho`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-r3l-wilmou</code> BUY 871 @ 1¢ → $9.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 871 (871 yours) | ×0.35^0 = 871.0 |
|  | 0.2¢ | 1,237 | ×0.35^8 = 0.3 |
|  | 0.1¢ | 25,000 | ×0.35^9 = 2.0 |
| | | **Σ** | **873.2** |

`yours 871.0 / Σ 873.2 = 99.7%`  
`$10,000 ÷ 17d ÷ 31 ÷ 2 = $9.49 × 99.7% = $9.46/day`  

<details><summary>÷ 31 markets in this race — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r3l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r3l-adrsad`
3. `tec-pga-rockclas-2026-08-02-r3l-auseck`
4. `tec-pga-rockclas-2026-08-02-r3l-aussmo`
5. `tec-pga-rockclas-2026-08-02-r3l-bretod`
6. `tec-pga-rockclas-2026-08-02-r3l-bricam`
7. `tec-pga-rockclas-2026-08-02-r3l-chaphi`
8. `tec-pga-rockclas-2026-08-02-r3l-charam`
9. `tec-pga-rockclas-2026-08-02-r3l-chrkir`
10. `tec-pga-rockclas-2026-08-02-r3l-garhig`
11. `tec-pga-rockclas-2026-08-02-r3l-joedah`
12. `tec-pga-rockclas-2026-08-02-r3l-johpar`
13. `tec-pga-rockclas-2026-08-02-r3l-johvan`
14. `tec-pga-rockclas-2026-08-02-r3l-karvil`
15. `tec-pga-rockclas-2026-08-02-r3l-keinak`
16. `tec-pga-rockclas-2026-08-02-r3l-kevroy`
17. `tec-pga-rockclas-2026-08-02-r3l-kriven`
18. `tec-pga-rockclas-2026-08-02-r3l-leehod`
19. `tec-pga-rockclas-2026-08-02-r3l-lucglo`
20. `tec-pga-rockclas-2026-08-02-r3l-matpav`
21. `tec-pga-rockclas-2026-08-02-r3l-matsch`
22. `tec-pga-rockclas-2026-08-02-r3l-nicech`
23. `tec-pga-rockclas-2026-08-02-r3l-patfis`
24. `tec-pga-rockclas-2026-08-02-r3l-petmal`
25. `tec-pga-rockclas-2026-08-02-r3l-richoe`
26. `tec-pga-rockclas-2026-08-02-r3l-thoole`
27. `tec-pga-rockclas-2026-08-02-r3l-vinwha`
28. `tec-pga-rockclas-2026-08-02-r3l-wiljen`
29. `tec-pga-rockclas-2026-08-02-r3l-wilmou` ← this one
30. `tec-pga-rockclas-2026-08-02-r3l-zacbau`
31. `tec-pga-rockclas-2026-08-02-r3l-zacbla`

</details>

</details>
<details><summary><code>tec-pga-rockclas-2026-08-02-r2l-jessve</code> BUY 2,125 @ 1¢ → $2.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,125 (2,125 yours) | ×0.35^0 = 2,125.0 |
|  | 0.3¢ | 9,333 | ×0.35^7 = 6.0 |
| | | **Σ** | **2,131.0** |

`yours 2,125.0 / Σ 2,131.0 = 99.7%`  
`$10,000 ÷ 17d ÷ 146 ÷ 2 = $2.01 × 99.7% = $2.01/day`  

<details><summary>÷ 146 markets in this race (40 known) — tap to list</summary>

1. `tec-pga-rockclas-2026-08-02-r2l-aarwis`
2. `tec-pga-rockclas-2026-08-02-r2l-adasch`
3. `tec-pga-rockclas-2026-08-02-r2l-adasve`
4. `tec-pga-rockclas-2026-08-02-r2l-adrcha`
5. `tec-pga-rockclas-2026-08-02-r2l-adrsad`
6. `tec-pga-rockclas-2026-08-02-r2l-aewa`
7. `tec-pga-rockclas-2026-08-02-r2l-aksbha`
8. `tec-pga-rockclas-2026-08-02-r2l-aldpot`
9. `tec-pga-rockclas-2026-08-02-r2l-aletos`
10. `tec-pga-rockclas-2026-08-02-r2l-andnov`
11. `tec-pga-rockclas-2026-08-02-r2l-andput`
12. `tec-pga-rockclas-2026-08-02-r2l-auseck`
13. `tec-pga-rockclas-2026-08-02-r2l-aussmo`
14. `tec-pga-rockclas-2026-08-02-r2l-beahos`
15. `tec-pga-rockclas-2026-08-02-r2l-bengri`
16. `tec-pga-rockclas-2026-08-02-r2l-benjam`
17. `tec-pga-rockclas-2026-08-02-r2l-benkoh`
18. `tec-pga-rockclas-2026-08-02-r2l-bilhor`
19. `tec-pga-rockclas-2026-08-02-r2l-bradal`
20. `tec-pga-rockclas-2026-08-02-r2l-brasne`
21. `tec-pga-rockclas-2026-08-02-r2l-bretod`
22. `tec-pga-rockclas-2026-08-02-r2l-bricam`
23. `tec-pga-rockclas-2026-08-02-r2l-brigar`
24. `tec-pga-rockclas-2026-08-02-r2l-brokoe`
25. `tec-pga-rockclas-2026-08-02-r2l-camdav`
26. `tec-pga-rockclas-2026-08-02-r2l-camyou`
27. `tec-pga-rockclas-2026-08-02-r2l-chabla`
28. `tec-pga-rockclas-2026-08-02-r2l-chaphi`
29. `tec-pga-rockclas-2026-08-02-r2l-charam`
30. `tec-pga-rockclas-2026-08-02-r2l-chrbez`
31. `tec-pga-rockclas-2026-08-02-r2l-chrgot`
32. `tec-pga-rockclas-2026-08-02-r2l-chrkir`
33. `tec-pga-rockclas-2026-08-02-r2l-chrlam`
34. `tec-pga-rockclas-2026-08-02-r2l-corcon`
35. `tec-pga-rockclas-2026-08-02-r2l-danaza`
36. `tec-pga-rockclas-2026-08-02-r2l-danwal`
37. `tec-pga-rockclas-2026-08-02-r2l-davcha`
38. `tec-pga-rockclas-2026-08-02-r2l-davlip`
39. `tec-pga-rockclas-2026-08-02-r2l-davril`
40. `tec-pga-rockclas-2026-08-02-r2l-davtho`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 100 @ 13¢ → $3.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 100 (100 yours) | ×0.2^0 = 100.0 |
|  | 12¢ | 100 | ×0.2^1 = 20.0 |
|  | 5¢ | 2 | ×0.2^8 = 0.0 |
|  | 3¢ | 206,666 | ×0.2^10 = 0.0 |
| | | **Σ** | **120.0** |

`yours 100.0 / Σ 120.0 = 83.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 83.3% = $3.20/day`  

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
<details><summary><code>iarc-group-2026-12-31-joebid</code> BUY 200 @ 4¢ → $0.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 4¢ | 200 (200 yours) | ×0.1^1 = 20.0 |
|  | 1¢ | 35,475 | ×0.1^4 = 3.5 |
| | | **Σ** | **25.5** |

`yours 20.0 / Σ 25.5 = 78.3%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 78.3% = $0.98/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-krinoe</code> BUY 200 @ 6¢ → $1.14/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 11 | ×0.2^0 = 11.0 |
| ▶ | 6¢ | 200 (200 yours) | ×0.2^1 = 40.0 |
|  | 5¢ | 11 | ×0.2^2 = 0.4 |
|  | 1¢ | 30,450 | ×0.2^6 = 1.9 |
| | | **Σ** | **53.4** |

`yours 40.0 / Σ 53.4 = 74.9%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 74.9% = $1.14/day`  

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
18. `cranc-uspres28-12-31-2026-krinoe` ← this one
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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 100 @ 9¢ → $2.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 7 | ×0.2^0 = 7.0 |
| ▶ | 9¢ | 100 (100 yours) | ×0.2^1 = 20.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 50,225 | ×0.2^9 = 0.0 |
| | | **Σ** | **27.0** |

`yours 20.0 / Σ 27.0 = 74.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 74.0% = $2.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 100 @ 9¢ → $2.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 7 | ×0.2^0 = 7.0 |
| ▶ | 9¢ | 100 (100 yours) | ×0.2^1 = 20.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 100,225 | ×0.2^9 = 0.1 |
| | | **Σ** | **27.1** |

`yours 20.0 / Σ 27.1 = 73.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 73.9% = $2.84/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 100 @ 9¢ → $2.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 7 | ×0.2^0 = 7.0 |
| ▶ | 9¢ | 100 (100 yours) | ×0.2^1 = 20.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 120,250 | ×0.2^9 = 0.1 |
| | | **Σ** | **27.1** |

`yours 20.0 / Σ 27.1 = 73.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 73.9% = $2.84/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-stesmi</code> BUY 200 @ 8¢ → $1.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 8 | ×0.2^0 = 8.0 |
| ▶ | 8¢ | 202 (200 yours) | ×0.2^1 = 40.4 |
|  | 5¢ | 252 | ×0.2^4 = 0.4 |
|  | 4¢ | 20,000 | ×0.2^5 = 6.4 |
| | | **Σ** | **55.2** |

`yours 40.0 / Σ 55.2 = 72.5%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 72.5% = $1.10/day`  

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
27. `cranc-uspres28-12-31-2026-robken`
28. `cranc-uspres28-12-31-2026-steban`
29. `cranc-uspres28-12-31-2026-stesmi` ← this one
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>mlaec-isrpol-pm-2026-10-27-yailap</code> BUY 100 @ 4¢ → $0.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 4¢ | 100 (100 yours) | ×0.1^1 = 10.0 |
|  | 1¢ | 22,447 | ×0.1^4 = 2.2 |
| | | **Σ** | **14.2** |

`yours 10.0 / Σ 14.2 = 70.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 70.2% = $0.88/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `mlaec-isrpol-pm-2026-10-27-avilie`
2. `mlaec-isrpol-pm-2026-10-27-ayesha`
3. `mlaec-isrpol-pm-2026-10-27-bengan`
4. `mlaec-isrpol-pm-2026-10-27-bennet`
5. `mlaec-isrpol-pm-2026-10-27-gadeiz`
6. `mlaec-isrpol-pm-2026-10-27-gidsaa`
7. `mlaec-isrpol-pm-2026-10-27-itaben`
8. `mlaec-isrpol-pm-2026-10-27-nafben`
9. `mlaec-isrpol-pm-2026-10-27-yailap` ← this one
10. `mlaec-isrpol-pm-2026-10-27-yoahen`

</details>

</details>
<details><summary><code>iarc-group-2026-12-31-tuccar</code> BUY 100 @ 4¢ → $0.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 4¢ | 100 (100 yours) | ×0.1^1 = 10.0 |
|  | 1¢ | 22,485 | ×0.1^4 = 2.2 |
| | | **Σ** | **14.2** |

`yours 10.0 / Σ 14.2 = 70.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 70.2% = $0.88/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `iarc-group-2026-12-31-antfau`
2. `iarc-group-2026-12-31-baroba`
3. `iarc-group-2026-12-31-bilcli`
4. `iarc-group-2026-12-31-canowe`
5. `iarc-group-2026-12-31-gavnew`
6. `iarc-group-2026-12-31-hilcli`
7. `iarc-group-2026-12-31-joebid`
8. `iarc-group-2026-12-31-johbre`
9. `iarc-group-2026-12-31-tomhom`
10. `iarc-group-2026-12-31-tuccar` ← this one

</details>

</details>
<details><summary><code>mlaec-isrpol-pm-2026-10-27-ayesha</code> BUY 100 @ 4¢ → $0.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 4¢ | 100 (100 yours) | ×0.1^1 = 10.0 |
|  | 2¢ | 3 | ×0.1^3 = 0.0 |
|  | 1¢ | 22,500 | ×0.1^4 = 2.3 |
| | | **Σ** | **14.3** |

`yours 10.0 / Σ 14.3 = 70.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 70.2% = $0.88/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `mlaec-isrpol-pm-2026-10-27-avilie`
2. `mlaec-isrpol-pm-2026-10-27-ayesha` ← this one
3. `mlaec-isrpol-pm-2026-10-27-bengan`
4. `mlaec-isrpol-pm-2026-10-27-bennet`
5. `mlaec-isrpol-pm-2026-10-27-gadeiz`
6. `mlaec-isrpol-pm-2026-10-27-gidsaa`
7. `mlaec-isrpol-pm-2026-10-27-itaben`
8. `mlaec-isrpol-pm-2026-10-27-nafben`
9. `mlaec-isrpol-pm-2026-10-27-yailap`
10. `mlaec-isrpol-pm-2026-10-27-yoahen`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-dontru</code> BUY 200 @ 8¢ → $1.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 20 | ×0.2^0 = 20.0 |
| ▶ | 8¢ | 200 (200 yours) | ×0.2^1 = 40.0 |
|  | 5¢ | 2 | ×0.2^4 = 0.0 |
|  | 1¢ | 120,491 | ×0.2^8 = 0.3 |
| | | **Σ** | **60.3** |

`yours 40.0 / Σ 60.3 = 66.3%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 66.3% = $1.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 100 @ 8¢ → $2.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 8¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 220,225 | ×0.2^9 = 0.1 |
| | | **Σ** | **6.1** |

`yours 4.0 / Σ 6.1 = 65.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 65.4% = $2.52/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-erikir</code> BUY 100 @ 8¢ → $0.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 8¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 3¢ | 16,806 | ×0.2^7 = 0.2 |
| | | **Σ** | **6.2** |

`yours 4.0 / Σ 6.2 = 64.4%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 64.4% = $0.98/day`  

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
10. `cranc-uspres28-12-31-2026-erikir` ← this one
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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 100 @ 8¢ → $2.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 8¢ | 105 (100 yours) | ×0.2^2 = 4.2 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 30,450 | ×0.2^9 = 0.0 |
| | | **Σ** | **6.2** |

`yours 4.0 / Σ 6.2 = 64.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.3% = $2.47/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 100 @ 8¢ → $2.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 8¢ | 105 (100 yours) | ×0.2^2 = 4.2 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 30,450 | ×0.2^9 = 0.0 |
| | | **Σ** | **6.2** |

`yours 4.0 / Σ 6.2 = 64.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.3% = $2.47/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 100 @ 8¢ → $2.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 8¢ | 105 (100 yours) | ×0.2^2 = 4.2 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 30,475 | ×0.2^9 = 0.0 |
| | | **Σ** | **6.2** |

`yours 4.0 / Σ 6.2 = 64.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 64.3% = $2.47/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-markel</code> BUY 200 @ 7¢ → $0.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 22 | ×0.2^0 = 22.0 |
| ▶ | 7¢ | 200 (200 yours) | ×0.2^1 = 40.0 |
|  | 5¢ | 2 | ×0.2^3 = 0.0 |
|  | 3¢ | 5 | ×0.2^5 = 0.0 |
|  | 2¢ | 250 | ×0.2^6 = 0.0 |
|  | 1¢ | 70,200 | ×0.2^7 = 0.9 |
| | | **Σ** | **62.9** |

`yours 40.0 / Σ 62.9 = 63.6%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 63.6% = $0.96/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 100 @ 8¢ → $2.19/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.2^0 = 2.0 |
|  | 9¢ | 5 | ×0.2^1 = 1.0 |
| ▶ | 8¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 70,200 | ×0.2^9 = 0.0 |
| | | **Σ** | **7.0** |

`yours 4.0 / Σ 7.0 = 56.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 56.8% = $2.19/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-elomus</code> BUY 100 @ 7¢ → $0.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 14 | ×0.2^0 = 14.0 |
| ▶ | 7¢ | 100 (100 yours) | ×0.2^1 = 20.0 |
|  | 6¢ | 20 | ×0.2^2 = 0.8 |
|  | 5¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 40,475 | ×0.2^7 = 0.5 |
| | | **Σ** | **35.3** |

`yours 20.0 / Σ 35.3 = 56.6%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 56.6% = $0.86/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 100 @ 8¢ → $1.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.2^0 = 2.0 |
|  | 9¢ | 10 | ×0.2^1 = 2.0 |
| ▶ | 8¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 70,475 | ×0.2^9 = 0.0 |
| | | **Σ** | **8.0** |

`yours 4.0 / Σ 8.0 = 49.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 49.8% = $1.91/day`  

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
| 2026-07-24 | ~$133.49 | $135.19 | 101% |
| 2026-07-23 | ~$136.30 | $227.63 | 167% |
| 2026-07-22 | ~$110.63 | $82.95 | 75% |

Biggest gaps on 2026-07-24: `opdc-mcconnell-resign-2026-11-02` (est ~$25.83 → got $12.25), `pvwc-housepopw-2026-11-03-dem` (est ~$7.47 → got $2.62), `pvwc-housepopw-2026-11-03-rep` (est ~$12.57 → got $10.29)

_2026-07-25 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $300.00 ÷ 3 | 0.20 | 10,000 | SELL side (77,381 resting) | ~85.1% | ~$42.55 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (150,310 resting) | ~41.8% | ~$20.88 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (60,088 resting) | ~69.9% | ~$17.47 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (92,310 resting) | ~65.7% | ~$16.42 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (25,236 resting) | ~90.9% | ~$15.15 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (146,198 resting) | ~15.4% | ~$11.54 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (66,605 resting) | ~35.3% | ~$8.83 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (78,027 resting) | ~11.6% | ~$8.69 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (150,553 resting) | ~6.8% | ~$5.14 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (99,369 resting) | ~5.0% | ~$3.75 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (34,466 resting) | ~11.6% | ~$2.91 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (78,156 resting) | ~3.5% | ~$2.63 |

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
| 2026-07-27 8:14 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 8:11 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 7:54 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 7:36 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 6:30 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:47 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:32 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:13 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:06 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 3:59 PM ET | ✅ ok | 567 | $962.30 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
