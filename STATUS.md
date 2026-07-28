# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-27 8:11 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$116.67/day estimated (ceiling, not promise — details below)

**Earned:** $962.30 lifetime ($155.84 paid). Last three recorded days — 2026-07-25: **$125.69** ⚠️ pending bucket — covers every day since then, still growing · 2026-07-24: **$135.19** · 2026-07-23: **$227.63** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-ussep-mi-2026-08-04-dem-abdels` — SELL at the best price, ~$46.07/day for 200 contracts. Runners-up: `enwc-ussep-mi-2026-08-04-dem-halste` (~$23.35/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$17.47/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$116.67/day (~$4.86/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `cranc-uspres28-12-31-2026-marrub` | SELL | 9.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (27,460 resting ≥ 5,000 ✓) ≈ $1.52/day (pool ÷ 33 markets) |
| `vmc-ussep-misen-2026-08-04-els10-15` | SELL | 22.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (61,649 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | SELL | 5.0¢ | 127 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (6,327 resting ≥ 2,000 ✓) ≈ $1.04/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | BUY | 26.0¢ | 9 | 0 | $25.00 | ✅ scoring — ~99.9% of bid side (10,334 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 2.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (43,405 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els0-5` | SELL | 27.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (99,573 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 29.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~96.5% of ask side (2,274 resting ≥ 2,000 ✓) ≈ $1.21/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~95.4% of bid side (60,677 resting ≥ 5,000 ✓) ≈ $3.67/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 13.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~83.3% of bid side (207,068 resting ≥ 5,000 ✓) ≈ $3.20/day (pool ÷ 13 markets) |
| `iarc-group-2026-12-31-joebid` | BUY | 4.0¢ | 200 | 1 | $25.00 | ✅ scoring — ~78.3% of bid side (35,677 resting ≥ 2,000 ✓) ≈ $0.98/day (pool ÷ 10 markets) |
| `cranc-uspres28-12-31-2026-krinoe` | BUY | 6.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~75.3% of bid side (10,698 resting ≥ 5,000 ✓) ≈ $1.14/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 9.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~74.0% of bid side (50,309 resting ≥ 5,000 ✓) ≈ $2.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 9.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~73.9% of bid side (100,309 resting ≥ 5,000 ✓) ≈ $2.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 9.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~73.9% of bid side (120,309 resting ≥ 5,000 ✓) ≈ $2.84/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-stesmi` | BUY | 8.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~72.5% of bid side (20,662 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 33 markets) |
| `mlaec-isrpol-pm-2026-10-27-yailap` | BUY | 4.0¢ | 100 | 1 | $25.00 | ✅ scoring — ~70.2% of bid side (22,549 resting ≥ 2,000 ✓) ≈ $0.88/day (pool ÷ 10 markets) |
| `iarc-group-2026-12-31-tuccar` | BUY | 4.0¢ | 100 | 1 | $25.00 | ✅ scoring — ~70.2% of bid side (22,563 resting ≥ 2,000 ✓) ≈ $0.88/day (pool ÷ 10 markets) |
| `mlaec-isrpol-pm-2026-10-27-ayesha` | BUY | 4.0¢ | 100 | 1 | $25.00 | ✅ scoring — ~70.2% of bid side (22,580 resting ≥ 2,000 ✓) ≈ $0.88/day (pool ÷ 10 markets) |
| `cranc-uspres28-12-31-2026-dontru` | BUY | 8.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~66.3% of bid side (120,713 resting ≥ 5,000 ✓) ≈ $1.00/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 8.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~66.3% of bid side (70,304 resting ≥ 5,000 ✓) ≈ $2.55/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-erikir` | BUY | 8.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~64.4% of bid side (17,110 resting ≥ 5,000 ✓) ≈ $0.98/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-markel` | BUY | 7.0¢ | 200 | 1 | $100.00 | ✅ scoring — ~58.0% of bid side (70,710 resting ≥ 5,000 ✓) ≈ $0.88/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-elomus` | BUY | 7.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~56.6% of bid side (40,611 resting ≥ 5,000 ✓) ≈ $0.86/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 8.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~56.2% of bid side (220,309 resting ≥ 5,000 ✓) ≈ $2.16/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-robken` | BUY | 9.0¢ | 100 | 2 | $100.00 | ✅ scoring — ~46.2% of bid side (70,364 resting ≥ 5,000 ✓) ≈ $0.70/day (pool ÷ 33 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 18.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~39.2% of ask side (3,755 resting ≥ 2,000 ✓) ≈ $4.90/day |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 18.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~39.2% of ask side (3,755 resting ≥ 2,000 ✓) ≈ $4.90/day |
| `cranc-uspres28-12-31-2026-dontrujr` | BUY | 7.0¢ | 200 | 2 | $100.00 | ✅ scoring — ~39.0% of bid side (17,971 resting ≥ 5,000 ✓) ≈ $0.59/day (pool ÷ 33 markets) |
| `ewc-pres-fra-2027-04-11-davlis` | BUY | 5.0¢ | 500 | 0 | $25.00 | ✅ scoring — ~36.0% of bid side (84,157 resting ≥ 2,000 ✓) ≈ $0.41/day (pool ÷ 11 markets) |
| `ewc-pres-fra-2027-04-11-bruret` | BUY | 5.0¢ | 200 | 1 | $25.00 | ✅ scoring — ~35.4% of bid side (26,170 resting ≥ 2,000 ✓) ≈ $0.40/day (pool ÷ 11 markets) |
| …and 215 more | | | | | | |

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
|  | 66¢ | 875 | ×0.2^57 = 0.0 |
|  | 67¢ | 810 | ×0.2^58 = 0.0 |
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
|  | 28¢ | 6 | ×0.1^6 = 0.0 |
|  | 30¢ | 30 | ×0.1^8 = 0.0 |
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
|  | 23¢ | 100 | ×0.1^18 = 0.0 |
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
|  | 32¢ | 28 | ×0.1^5 = 0.0 |
|  | 33¢ | 6 | ×0.1^6 = 0.0 |
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
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 11 @ 29¢ → $1.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 11 (11 yours) | ×0.1^0 = 11.0 |
|  | 30¢ | 4 | ×0.1^1 = 0.4 |
|  | 35¢ | 6 | ×0.1^6 = 0.0 |
|  | 36¢ | 28 | ×0.1^7 = 0.0 |
|  | 39¢ | 100 | ×0.1^10 = 0.0 |
|  | 99¢ | 2,125 | ×0.1^70 = 0.0 |
| | | **Σ** | **11.4** |

`yours 11.0 / Σ 11.4 = 96.5%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 96.5% = $1.21/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 100 @ 9¢ → $3.67/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 100 (100 yours) | ×0.2^0 = 100.0 |
|  | 7¢ | 100 | ×0.2^2 = 4.0 |
|  | 5¢ | 2 | ×0.2^4 = 0.0 |
|  | 2¢ | 60,250 | ×0.2^7 = 0.8 |
| | | **Σ** | **104.8** |

`yours 100.0 / Σ 104.8 = 95.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 95.4% = $3.67/day`  

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
|  | 7¢ | 12 | ×0.2^0 = 12.0 |
| ▶ | 6¢ | 200 (200 yours) | ×0.2^1 = 40.0 |
|  | 5¢ | 11 | ×0.2^2 = 0.4 |
|  | 1¢ | 10,475 | ×0.2^6 = 0.7 |
| | | **Σ** | **53.1** |

`yours 40.0 / Σ 53.1 = 75.3%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 75.3% = $1.14/day`  

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
|  | 1¢ | 50,200 | ×0.2^9 = 0.0 |
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
|  | 1¢ | 100,200 | ×0.2^9 = 0.1 |
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
|  | 1¢ | 120,200 | ×0.2^9 = 0.1 |
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
|  | 1¢ | 22,461 | ×0.1^4 = 2.2 |
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
|  | 1¢ | 22,475 | ×0.1^4 = 2.2 |
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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 100 @ 8¢ → $2.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 8¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 70,200 | ×0.2^9 = 0.0 |
| | | **Σ** | **6.0** |

`yours 4.0 / Σ 6.0 = 66.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.3% = $2.55/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-markel</code> BUY 200 @ 7¢ → $0.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 28 | ×0.2^0 = 28.0 |
| ▶ | 7¢ | 200 (200 yours) | ×0.2^1 = 40.0 |
|  | 5¢ | 2 | ×0.2^3 = 0.0 |
|  | 3¢ | 5 | ×0.2^5 = 0.0 |
|  | 2¢ | 250 | ×0.2^6 = 0.0 |
|  | 1¢ | 70,225 | ×0.2^7 = 0.9 |
| | | **Σ** | **68.9** |

`yours 40.0 / Σ 68.9 = 58.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 58.0% = $0.88/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 100 @ 8¢ → $2.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.2^0 = 2.0 |
|  | 9¢ | 5 | ×0.2^1 = 1.0 |
| ▶ | 8¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 220,200 | ×0.2^9 = 0.1 |
| | | **Σ** | **7.1** |

`yours 4.0 / Σ 7.1 = 56.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 56.2% = $2.16/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-robken</code> BUY 100 @ 9¢ → $0.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 11¢ | 3 | ×0.2^0 = 3.0 |
|  | 10¢ | 5 | ×0.2^1 = 1.0 |
| ▶ | 9¢ | 116 (100 yours) | ×0.2^2 = 4.6 |
|  | 6¢ | 6 | ×0.2^5 = 0.0 |
|  | 5¢ | 2 | ×0.2^6 = 0.0 |
|  | 1¢ | 70,232 | ×0.2^10 = 0.0 |
| | | **Σ** | **8.6** |

`yours 4.0 / Σ 8.6 = 46.2%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 46.2% = $0.70/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 10 @ 18¢ → $4.90/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 22 (10 yours) | ×0.1^0 = 21.5 |
|  | 19¢ | 40 | ×0.1^1 = 4.0 |
|  | 37¢ | 87 | ×0.1^19 = 0.0 |
|  | 51¢ | 61 | ×0.1^33 = 0.0 |
|  | 55¢ | 30 | ×0.1^37 = 0.0 |
|  | 58¢ | 50 | ×0.1^40 = 0.0 |
|  | 92¢ | 1,112 | ×0.1^74 = 0.0 |
|  | 96¢ | 22 | ×0.1^78 = 0.0 |
|  | 99¢ | 2,331 | ×0.1^81 = 0.0 |
| | | **Σ** | **25.5** |

`yours 10.0 / Σ 25.5 = 39.2%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 39.2% = $4.90/day`  

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 10 @ 18¢ → $4.90/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 22 (10 yours) | ×0.1^0 = 21.5 |
|  | 19¢ | 40 | ×0.1^1 = 4.0 |
|  | 37¢ | 87 | ×0.1^19 = 0.0 |
|  | 51¢ | 61 | ×0.1^33 = 0.0 |
|  | 55¢ | 30 | ×0.1^37 = 0.0 |
|  | 58¢ | 50 | ×0.1^40 = 0.0 |
|  | 92¢ | 1,112 | ×0.1^74 = 0.0 |
|  | 96¢ | 22 | ×0.1^78 = 0.0 |
|  | 99¢ | 2,331 | ×0.1^81 = 0.0 |
| | | **Σ** | **25.5** |

`yours 10.0 / Σ 25.5 = 39.2%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 39.2% = $4.90/day`  

</details>
<details><summary><code>cranc-uspres28-12-31-2026-dontrujr</code> BUY 200 @ 7¢ → $0.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 11 | ×0.2^0 = 11.0 |
|  | 8¢ | 2 | ×0.2^1 = 0.4 |
| ▶ | 7¢ | 200 (200 yours) | ×0.2^2 = 8.0 |
|  | 5¢ | 2 | ×0.2^4 = 0.0 |
|  | 3¢ | 17,556 | ×0.2^6 = 1.1 |
| | | **Σ** | **20.5** |

`yours 8.0 / Σ 20.5 = 39.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 39.0% = $0.59/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru`
7. `cranc-uspres28-12-31-2026-dontrujr` ← this one
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
<details><summary><code>ewc-pres-fra-2027-04-11-davlis</code> BUY 500 @ 5¢ → $0.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 828 (500 yours) | ×0.1^0 = 828.0 |
|  | 4¢ | 5,625 | ×0.1^1 = 562.5 |
| | | **Σ** | **1,390.5** |

`yours 500.0 / Σ 1,390.5 = 36.0%`  
`$25 ÷ 11 ÷ 2 = $1.14 × 36.0% = $0.41/day`  

<details><summary>÷ 11 markets in this race — tap to list</summary>

1. `ewc-pres-fra-2027-04-11-bruret`
2. `ewc-pres-fra-2027-04-11-davlis` ← this one
3. `ewc-pres-fra-2027-04-11-domvil`
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
<details><summary><code>ewc-pres-fra-2027-04-11-bruret</code> BUY 200 @ 5¢ → $0.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 31 | ×0.1^0 = 31.0 |
| ▶ | 5¢ | 202 (200 yours) | ×0.1^1 = 20.2 |
|  | 4¢ | 500 | ×0.1^2 = 5.0 |
|  | 2¢ | 160 | ×0.1^4 = 0.0 |
|  | 1¢ | 25,277 | ×0.1^5 = 0.3 |
| | | **Σ** | **56.5** |

`yours 20.0 / Σ 56.5 = 35.4%`  
`$25 ÷ 11 ÷ 2 = $1.14 × 35.4% = $0.40/day`  

<details><summary>÷ 11 markets in this race — tap to list</summary>

1. `ewc-pres-fra-2027-04-11-bruret` ← this one
2. `ewc-pres-fra-2027-04-11-davlis`
3. `ewc-pres-fra-2027-04-11-domvil`
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
| `enwc-ussep-mi-2026-08-04-dem-abdels` | $300.00 ÷ 3 | 0.20 | 10,000 | SELL side (77,263 resting) | ~92.1% | ~$46.07 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (150,057 resting) | ~46.7% | ~$23.35 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (60,088 resting) | ~69.9% | ~$17.47 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (92,310 resting) | ~65.7% | ~$16.42 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (25,236 resting) | ~90.9% | ~$15.15 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (66,605 resting) | ~35.3% | ~$8.83 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (77,889 resting) | ~11.6% | ~$8.69 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (121,002 resting) | ~9.2% | ~$6.92 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (150,537 resting) | ~6.8% | ~$5.14 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (99,369 resting) | ~5.0% | ~$3.75 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (78,106 resting) | ~3.6% | ~$2.67 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (78,883 resting) | ~3.4% | ~$2.58 |

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
| 2026-07-27 8:11 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 7:54 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 7:36 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 6:30 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:47 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:32 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:13 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 4:06 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 3:59 PM ET | ✅ ok | 567 | $962.30 |
| 2026-07-27 3:51 PM ET | ✅ ok | 567 | $962.30 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
