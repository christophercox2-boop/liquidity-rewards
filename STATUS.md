# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-01 7:23 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$30.65/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `cranc-uspres28-12-31-2026-hunbid` — SELL at the best price, ~$1.44/day for 200 contracts. Runners-up: `cranc-uspres28-12-31-2026-petbut` (~$1.39/day), `cranc-uspres28-12-31-2026-jdvan` (~$1.26/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$30.65/day (~$1.28/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-48` | BUY | 11.0¢ | 64 | 0 | $100.00 | ✅ scoring — ~99.9% of bid side (5,127 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-elsgte20` | BUY | 34.0¢ | 34 | 0 | $25.00 | ✅ scoring — ~97.2% of bid side (6,634 resting ≥ 2,000 ✓) ≈ $1.21/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 32.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~70.5% of ask side (12,224 resting ≥ 5,000 ✓) ≈ $2.71/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (11,939 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~49.8% of ask side (12,084 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-tedcru` | SELL | 21.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~47.4% of ask side (5,518 resting ≥ 5,000 ✓) ≈ $0.72/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~45.5% of ask side (11,857 resting ≥ 5,000 ✓) ≈ $1.75/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~45.5% of ask side (11,877 resting ≥ 5,000 ✓) ≈ $1.75/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 15.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~43.9% of ask side (11,947 resting ≥ 5,000 ✓) ≈ $1.69/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 32.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~40.1% of ask side (12,062 resting ≥ 5,000 ✓) ≈ $1.54/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 7.0¢ | 60 | 0 | $25.00 | ✅ scoring — ~34.3% of ask side (119,487 resting ≥ 2,000 ✓) ≈ $0.43/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~34.0% of ask side (12,237 resting ≥ 5,000 ✓) ≈ $1.31/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 5.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~27.6% of ask side (12,130 resting ≥ 5,000 ✓) ≈ $1.06/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~26.7% of ask side (12,239 resting ≥ 5,000 ✓) ≈ $1.03/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 40.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~25.8% of ask side (5,584 resting ≥ 5,000 ✓) ≈ $1.07/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~22.6% of ask side (12,084 resting ≥ 5,000 ✓) ≈ $0.87/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 16.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~20.8% of ask side (11,903 resting ≥ 5,000 ✓) ≈ $0.80/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 7.0¢ | 33 | 0 | $25.00 | ✅ scoring — ~18.9% of ask side (119,487 resting ≥ 2,000 ✓) ≈ $0.24/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 15.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~18.1% of ask side (12,102 resting ≥ 5,000 ✓) ≈ $0.70/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 2.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~17.1% of ask side (220,534 resting ≥ 2,000 ✓) ≈ $0.21/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 90.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~15.6% of bid side (5,503 resting ≥ 5,000 ✓) ≈ $0.65/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~8.5% of bid side (11,949 resting ≥ 5,000 ✓) ≈ $0.33/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 74.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~8.2% of bid side (5,656 resting ≥ 5,000 ✓) ≈ $0.34/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 76.0¢ | 49 | 0 | $100.00 | ✅ scoring — ~7.9% of ask side (6,027 resting ≥ 5,000 ✓) ≈ $0.33/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 78.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~6.9% of bid side (5,547 resting ≥ 5,000 ✓) ≈ $0.29/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 24.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~6.8% of ask side (5,329 resting ≥ 5,000 ✓) ≈ $0.28/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~6.0% of bid side (8,494 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 2.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~5.6% of ask side (214,626 resting ≥ 2,000 ✓) ≈ $0.07/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | BUY | 2.0¢ | 250 | 0 | $100.00 | ✅ scoring — ~3.7% of bid side (22,900 resting ≥ 5,000 ✓) ≈ $0.15/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~3.4% of bid side (29,626 resting ≥ 5,000 ✓) ≈ $0.13/day (pool ÷ 13 markets) |
| …and 26 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 64 @ 11¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 64 (64 yours) | ×0.2^0 = 63.8 |
|  | 6¢ | 126 | ×0.2^5 = 0.0 |
|  | 4¢ | 173 | ×0.2^7 = 0.0 |
|  | 1¢ | 4,764 | ×0.2^10 = 0.0 |
| | | **Σ** | **63.8** |

`yours 63.8 / Σ 63.8 = 99.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 99.9% = $3.84/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-elsgte20</code> BUY 34 @ 34¢ → $1.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 35 (34 yours) | ×0.1^0 = 35.3 |
|  | 13¢ | 6 | ×0.1^21 = 0.0 |
|  | 10¢ | 18 | ×0.1^24 = 0.0 |
|  | 8¢ | 700 | ×0.1^26 = 0.0 |
|  | 7¢ | 499 | ×0.1^27 = 0.0 |
|  | 2¢ | 375 | ×0.1^32 = 0.0 |
|  | 1¢ | 5,001 | ×0.1^33 = 0.0 |
| | | **Σ** | **35.3** |

`yours 34.3 / Σ 35.3 = 97.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 97.2% = $1.21/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 32¢ → $2.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 61 (43 yours) | ×0.2^0 = 61.0 |
|  | 38¢ | 128 | ×0.2^6 = 0.0 |
|  | 47¢ | 37 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^18 = 0.0 |
|  | 98¢ | 1,897 | ×0.2^66 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^67 = 0.0 |
| | | **Σ** | **61.0** |

`yours 43.0 / Σ 61.0 = 70.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 70.5% = $2.71/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 50 @ 15¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 75 (50 yours) | ×0.2^0 = 75.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 22 @ 20¢ → $1.92/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 44 (22 yours) | ×0.2^0 = 44.0 |
|  | 24¢ | 100 | ×0.2^4 = 0.2 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,839 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **44.2** |

`yours 22.0 / Σ 44.2 = 49.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 49.8% = $1.92/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-tedcru</code> SELL 0 @ 21¢ → $0.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (0 yours) | ×0.2^0 = 0.7 |
|  | 24¢ | 15 | ×0.2^3 = 0.1 |
|  | 28¢ | 56 | ×0.2^7 = 0.0 |
|  | 29¢ | 470 | ×0.2^8 = 0.0 |
|  | 50¢ | 25 | ×0.2^29 = 0.0 |
|  | 77¢ | 2 | ×0.2^56 = 0.0 |
|  | 78¢ | 2 | ×0.2^57 = 0.0 |
|  | 99¢ | 4,947 | ×0.2^78 = 0.0 |
| | | **Σ** | **0.8** |

`yours 0.4 / Σ 0.8 = 47.4%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 47.4% = $0.72/day`  

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
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru` ← this one
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 10¢ → $1.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 22 (10 yours) | ×0.2^0 = 22.0 |
|  | 16¢ | 3 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **22.0** |

`yours 10.0 / Σ 22.0 = 45.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 45.5% = $1.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 10 @ 6¢ → $1.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 22 (10 yours) | ×0.2^0 = 22.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,735 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **22.0** |

`yours 10.0 / Σ 22.0 = 45.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 45.5% = $1.75/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 40 @ 15¢ → $1.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 91 (40 yours) | ×0.2^0 = 91.0 |
|  | 18¢ | 4 | ×0.2^3 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,751 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **91.0** |

`yours 40.0 / Σ 91.0 = 43.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.9% = $1.69/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 32¢ → $1.54/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 25 (10 yours) | ×0.2^0 = 24.9 |
|  | 35¢ | 5 | ×0.2^3 = 0.0 |
|  | 40¢ | 105 | ×0.2^8 = 0.0 |
|  | 50¢ | 100 | ×0.2^18 = 0.0 |
|  | 98¢ | 1,826 | ×0.2^66 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^67 = 0.0 |
| | | **Σ** | **25.0** |

`yours 10.0 / Σ 25.0 = 40.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.1% = $1.54/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 60 @ 7¢ → $0.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 158 (60 yours) | ×0.1^0 = 158.0 |
|  | 9¢ | 47 | ×0.1^2 = 0.5 |
|  | 10¢ | 16,556 | ×0.1^3 = 16.6 |
| | | **Σ** | **175.0** |

`yours 60.0 / Σ 175.0 = 34.3%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 34.3% = $0.43/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 10¢ → $1.31/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 147 (50 yours) | ×0.2^0 = 147.2 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **147.2** |

`yours 50.0 / Σ 147.2 = 34.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 34.0% = $1.31/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 50 @ 5¢ → $1.06/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 160 (50 yours) | ×0.2^0 = 160.2 |
|  | 6¢ | 104 | ×0.2^1 = 20.8 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 98¢ | 1,765 | ×0.2^93 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^94 = 0.0 |
| | | **Σ** | **181.0** |

`yours 50.0 / Σ 181.0 = 27.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.6% = $1.06/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 50 @ 21¢ → $1.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 149 (50 yours) | ×0.2^0 = 149.0 |
|  | 22¢ | 192 | ×0.2^1 = 38.4 |
|  | 27¢ | 20 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,777 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **187.4** |

`yours 50.0 / Σ 187.4 = 26.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.7% = $1.03/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 20 @ 40¢ → $1.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 39¢ | 5 | ×0.2^0 = 5.0 |
| ▶ | 40¢ | 47 (20 yours) | ×0.2^1 = 9.4 |
|  | 42¢ | 139 | ×0.2^3 = 1.1 |
|  | 52¢ | 1 | ×0.2^13 = 0.0 |
|  | 55¢ | 11 | ×0.2^16 = 0.0 |
|  | 69¢ | 100 | ×0.2^30 = 0.0 |
|  | 99¢ | 5,281 | ×0.2^60 = 0.0 |
| | | **Σ** | **15.5** |

`yours 4.0 / Σ 15.5 = 25.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 25.8% = $1.07/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 10 @ 20¢ → $0.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 44 (10 yours) | ×0.2^0 = 44.0 |
|  | 24¢ | 100 | ×0.2^4 = 0.2 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,839 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **44.2** |

`yours 10.0 / Σ 44.2 = 22.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 22.6% = $0.87/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 16¢ → $0.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 48 (10 yours) | ×0.2^0 = 48.2 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^82 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^83 = 0.0 |
| | | **Σ** | **48.2** |

`yours 10.0 / Σ 48.2 = 20.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.8% = $0.80/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 33 @ 7¢ → $0.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 158 (33 yours) | ×0.1^0 = 158.0 |
|  | 9¢ | 47 | ×0.1^2 = 0.5 |
|  | 10¢ | 16,556 | ×0.1^3 = 16.6 |
| | | **Σ** | **175.0** |

`yours 33.0 / Σ 175.0 = 18.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 18.9% = $0.24/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 25 @ 15¢ → $0.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 122 (25 yours) | ×0.2^0 = 122.0 |
|  | 16¢ | 79 | ×0.2^1 = 15.8 |
|  | 29¢ | 2 | ×0.2^14 = 0.0 |
|  | 35¢ | 2 | ×0.2^20 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **137.8** |

`yours 25.0 / Σ 137.8 = 18.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.1% = $0.70/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 50 @ 2¢ → $0.21/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 124 (50 yours) | ×0.1^0 = 124.0 |
|  | 3¢ | 25 | ×0.1^1 = 2.5 |
|  | 4¢ | 16,632 | ×0.1^2 = 166.3 |
| | | **Σ** | **292.8** |

`yours 50.0 / Σ 292.8 = 17.1%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 17.1% = $0.21/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 90¢ → $0.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 64 (10 yours) | ×0.2^0 = 64.1 |
|  | 1¢ | 5,439 | ×0.2^89 = 0.0 |
| | | **Σ** | **64.1** |

`yours 10.0 / Σ 64.1 = 15.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 15.6% = $0.65/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 1,000 @ 2¢ → $0.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 11,747 (1,000 yours) | ×0.2^0 = 11,747.0 |
| | | **Σ** | **11,747.0** |

`yours 1,000.0 / Σ 11,747.0 = 8.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.5% = $0.33/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 40 @ 74¢ → $0.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 468 (40 yours) | ×0.2^0 = 468.3 |
|  | 73¢ | 83 | ×0.2^1 = 16.6 |
|  | 1¢ | 5,105 | ×0.2^73 = 0.0 |
| | | **Σ** | **484.9** |

`yours 40.0 / Σ 484.9 = 8.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 8.2% = $0.34/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 49 @ 76¢ → $0.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 76¢ | 618 (49 yours) | ×0.2^0 = 618.0 |
|  | 98¢ | 127 | ×0.2^22 = 0.0 |
|  | 99¢ | 5,282 | ×0.2^23 = 0.0 |
| | | **Σ** | **618.0** |

`yours 49.0 / Σ 618.0 = 7.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.9% = $0.33/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 30 @ 78¢ → $0.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 435 (30 yours) | ×0.2^0 = 435.0 |
|  | 1¢ | 5,112 | ×0.2^77 = 0.0 |
| | | **Σ** | **435.0** |

`yours 30.0 / Σ 435.0 = 6.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 6.9% = $0.29/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 24¢ → $0.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 25 | ×0.2^0 = 25.0 |
| ▶ | 24¢ | 23 (10 yours) | ×0.2^1 = 4.6 |
|  | 99¢ | 5,281 | ×0.2^76 = 0.0 |
| | | **Σ** | **29.6** |

`yours 2.0 / Σ 29.6 = 6.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 6.8% = $0.28/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215` ← this one
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.23/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,294 (500 yours) | ×0.2^0 = 8,294.0 |
| | | **Σ** | **8,294.0** |

`yours 500.0 / Σ 8,294.0 = 6.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.0% = $0.23/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 100 @ 2¢ → $0.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 789 (100 yours) | ×0.1^0 = 789.0 |
|  | 3¢ | 10,051 | ×0.1^1 = 1,005.1 |
| | | **Σ** | **1,794.1** |

`yours 100.0 / Σ 1,794.1 = 5.6%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 5.6% = $0.07/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> BUY 250 @ 2¢ → $0.15/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 2,700 (250 yours) | ×0.2^0 = 2,700.0 |
|  | 1¢ | 20,200 | ×0.2^1 = 4,040.0 |
| | | **Σ** | **6,740.0** |

`yours 250.0 / Σ 6,740.0 = 3.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 3.7% = $0.15/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230` ← this one
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 29,426 (1,000 yours) | ×0.2^0 = 29,426.0 |
| | | **Σ** | **29,426.0** |

`yours 1,000.0 / Σ 29,426.0 = 3.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.4% = $0.13/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-29 | ~$65.42 | $53.59 | 82% |
| 2026-07-28 | ~$148.78 | $79.65 | 54% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |

Biggest gaps on 2026-07-29: `apdc-petehegseth-2026-12-31` (est ~$12.90 → got $1.16), `scc-senate-gop-2026-11-03-51` (est ~$3.25 → got $0.00), `scc-senate-gop-2026-11-03-54` (est ~$2.11 → got $0.02)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `cranc-uspres28-12-31-2026-hunbid` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,625 resting) | ~95.2% | ~$1.44 |
| `cranc-uspres28-12-31-2026-petbut` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (9,067 resting) | ~92.1% | ~$1.39 |
| `cranc-uspres28-12-31-2026-jdvan` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (29,777 resting) | ~83.2% | ~$1.26 |
| `cranc-uspres28-12-31-2026-erikir` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,511 resting) | ~70.9% | ~$1.07 |
| `cranc-uspres28-12-31-2026-elomus` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (12,641 resting) | ~68.7% | ~$1.04 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (6,228 resting) | ~68.5% | ~$1.04 |
| `cranc-uspres28-12-31-2026-kamhar` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (9,132 resting) | ~67.8% | ~$1.03 |
| `cranc-uspres28-12-31-2026-gavnew` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (83,481 resting) | ~60.0% | ~$0.91 |
| `cranc-uspres28-12-31-2026-tuccar` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (9,059 resting) | ~57.2% | ~$0.87 |
| `cranc-uspres28-12-31-2026-margre` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (8,756 resting) | ~55.5% | ~$0.84 |
| `cranc-uspres28-12-31-2026-aleoca` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,884 resting) | ~31.9% | ~$0.48 |
| `cranc-uspres28-12-31-2026-bersan` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (5,776 resting) | ~25.9% | ~$0.39 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,373.47 |
| Skipped | $1.21 |
| **Total earned** | **$1,374.68** |

1406 reward rows · 27 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-29 | $53.59 | `█████` |
| 2026-07-28 | $79.65 | `███████` |
| 2026-07-27 | $125.34 | `███████████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,374.68 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.26 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.82 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.47 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.25 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.73 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.96 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-01 7:23 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 7:14 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 6:13 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 5:12 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 3:38 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 1:34 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 1:25 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 12:24 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 12:17 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 12:06 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
