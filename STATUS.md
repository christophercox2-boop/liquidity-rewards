# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-14 2:58 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$778.18/day estimated (ceiling, not promise — details below)

**Earned:** $3,069.69 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-12: **$213.04** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-11: **$409.59** · 2026-08-10: **$557.62** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$16.16/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$11.66/day), `ewc-usgub-ga-2026-11-03-dem` (~$5.98/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$778.18/day (~$32.42/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (92,067 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-rahema` | SELL | 25.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (12,590 resting ≥ 10,000 ✓) ≈ $8.82/day (pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-jdvan` | SELL | 64.0¢ | 25 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (11,610 resting ≥ 10,000 ✓) ≈ $10.71/day (pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-marrub` | SELL | 50.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (11,888 resting ≥ 10,000 ✓) ≈ $10.71/day (pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-aleocc` | SELL | 29.0¢ | 33 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (10,320 resting ≥ 10,000 ✓) ≈ $5.56/day (pool ÷ 27 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 15.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (50,425 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-markel` | SELL | 43.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (12,593 resting ≥ 10,000 ✓) ≈ $8.82/day (pool ÷ 17 markets) |
| `ewc-usp-party-2028-11-07-rep` | BUY | 40.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~99.8% of bid side (10,586 resting ≥ 10,000 ✓) ≈ $74.84/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-gavnew` | SELL | 47.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~99.7% of ask side (10,780 resting ≥ 10,000 ✓) ≈ $8.80/day (pool ÷ 17 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~93.0% of ask side (130,768 resting ≥ 2,000 ✓) ≈ $5.81/day (pool ÷ 2 markets) |
| `usgubewc-usgub-co-2026-11-03-rep` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,781 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 7.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,753 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-rep` | SELL | 7.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (330,228 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-stasmi` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-micoba` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-thomas` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-gleyou` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-ranpau` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $9.55/day (pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-dwajoh` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jonste` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $7.86/day (pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $9.55/day (pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-stasmi` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $7.86/day (pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $9.55/day (pool ÷ 14 markets) |
| `enwc-uspres-nom-rep-2028-thomas` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $9.55/day (pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~88.5% of bid side (11,300 resting ≥ 10,000 ✓) ≈ $4.92/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-gavnew` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~88.5% of bid side (11,300 resting ≥ 10,000 ✓) ≈ $4.92/day (pool ÷ 27 markets) |
| …and 4568 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 8¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 80,716 | ×0.2^89 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 100.0% = $3.85/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-rahema</code> SELL 50 @ 25¢ → $8.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 51¢ | 100 | ×0.2^26 = 0.0 |
|  | 99¢ | 12,440 | ×0.2^74 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$300 ÷ 17 ÷ 2 = $8.82 × 100.0% = $8.82/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema` ← this one
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-jdvan</code> SELL 25 @ 64¢ → $10.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 64¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 99¢ | 11,585 | ×0.2^35 = 0.0 |
| | | **Σ** | **25.0** |

`yours 25.0 / Σ 25.0 = 100.0%`  
`$300 ÷ 14 ÷ 2 = $10.71 × 100.0% = $10.71/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan` ← this one
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-marrub</code> SELL 50 @ 50¢ → $10.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 60¢ | 100 | ×0.2^10 = 0.0 |
|  | 99¢ | 11,738 | ×0.2^49 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$300 ÷ 14 ÷ 2 = $10.71 × 100.0% = $10.71/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub` ← this one
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-aleocc</code> SELL 33 @ 29¢ → $5.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 33 (33 yours) | ×0.2^0 = 33.0 |
|  | 38¢ | 100 | ×0.2^9 = 0.0 |
|  | 99¢ | 10,187 | ×0.2^70 = 0.0 |
| | | **Σ** | **33.0** |

`yours 33.0 / Σ 33.0 = 100.0%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 100.0% = $5.56/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc` ← this one
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 25 @ 15¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 25 (25 yours) | ×0.2^0 = 25.0 |
|  | 9¢ | 0 | ×0.2^6 = 0.0 |
|  | 2¢ | 50,200 | ×0.2^13 = 0.0 |
| | | **Σ** | **25.0** |

`yours 25.0 / Σ 25.0 = 100.0%`  
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
<details><summary><code>enwc-uspres-nom-dem-2028-markel</code> SELL 50 @ 43¢ → $8.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 51¢ | 100 | ×0.2^8 = 0.0 |
|  | 99¢ | 12,443 | ×0.2^56 = 0.0 |
| | | **Σ** | **50.0** |

`yours 50.0 / Σ 50.0 = 100.0%`  
`$300 ÷ 17 ÷ 2 = $8.82 × 100.0% = $8.82/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel` ← this one
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-party-2028-11-07-rep</code> BUY 50 @ 40¢ → $74.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 35¢ | 336 | ×0.2^5 = 0.1 |
|  | 1¢ | 10,200 | ×0.2^39 = 0.0 |
| | | **Σ** | **50.1** |

`yours 50.0 / Σ 50.1 = 99.8%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 99.8% = $74.84/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usp-party-2028-11-07-dem`
2. `ewc-usp-party-2028-11-07-rep` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-gavnew</code> SELL 50 @ 47¢ → $8.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 51¢ | 100 | ×0.2^4 = 0.2 |
|  | 99¢ | 10,630 | ×0.2^52 = 0.0 |
| | | **Σ** | **50.2** |

`yours 50.0 / Σ 50.2 = 99.7%`  
`$300 ÷ 17 ÷ 2 = $8.82 × 99.7% = $8.80/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew` ← this one
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $5.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 43 (40 yours) | ×0.1^0 = 43.0 |
|  | 98¢ | 130,500 | ×0.1^94 = 0.0 |
| | | **Σ** | **43.0** |

`yours 40.0 / Σ 43.0 = 93.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.0% = $5.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-co-2026-11-03-rep</code> SELL 50 @ 7¢ → $5.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 56 (50 yours) | ×0.1^0 = 56.0 |
|  | 98¢ | 130,500 | ×0.1^91 = 0.0 |
| | | **Σ** | **56.0** |

`yours 50.0 / Σ 56.0 = 89.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.3% = $5.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-co-2026-11-03-dem`
2. `usgubewc-usgub-co-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 25 @ 7¢ → $5.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 28 (25 yours) | ×0.1^0 = 28.0 |
|  | 98¢ | 130,500 | ×0.1^91 = 0.0 |
| | | **Σ** | **28.0** |

`yours 25.0 / Σ 28.0 = 89.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.3% = $5.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-rep</code> SELL 50 @ 7¢ → $5.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 56 (50 yours) | ×0.1^0 = 56.0 |
|  | 98¢ | 132,784 | ×0.1^91 = 0.0 |
| | | **Σ** | **56.0** |

`yours 50.0 / Σ 56.0 = 89.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.3% = $5.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem`
2. `ussewc-usse-il-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-stasmi</code> BUY 10,000 @ 1¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.1% = $4.95/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi` ← this one
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-micoba</code> BUY 10,000 @ 1¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.1% = $4.95/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba` ← this one
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-thomas</code> BUY 10,000 @ 1¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.1% = $4.95/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas` ← this one
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-gleyou</code> BUY 10,000 @ 1¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.1% = $4.95/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou` ← this one
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-ranpau</code> BUY 10,000 @ 1¢ → $9.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 14 ÷ 2 = $10.71 × 89.1% = $9.55/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau` ← this one
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-dwajoh</code> BUY 10,000 @ 1¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.1% = $4.95/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh` ← this one
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jonste</code> BUY 10,000 @ 1¢ → $7.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 17 ÷ 2 = $8.82 × 89.1% = $7.86/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste` ← this one
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 10,000 @ 1¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.1% = $4.95/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram` ← this one
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-dontrujr</code> BUY 10,000 @ 1¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.1% = $4.95/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr` ← this one
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 10,000 @ 1¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.1% = $4.95/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri` ← this one
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-margre</code> BUY 10,000 @ 1¢ → $9.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 14 ÷ 2 = $10.71 × 89.1% = $9.55/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre` ← this one
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-stasmi</code> BUY 10,000 @ 1¢ → $7.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 17 ÷ 2 = $8.82 × 89.1% = $7.86/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi` ← this one
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 10,000 @ 1¢ → $4.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.1% = $4.95/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus` ← this one
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-elomus</code> BUY 10,000 @ 1¢ → $9.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 14 ÷ 2 = $10.71 × 89.1% = $9.55/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus` ← this one
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-thomas</code> BUY 10,000 @ 1¢ → $9.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 14 ÷ 2 = $10.71 × 89.1% = $9.55/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas` ← this one
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 10,000 @ 1¢ → $4.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,300 (10,000 yours) | ×0.2^0 = 11,300.0 |
| | | **Σ** | **11,300.0** |

`yours 10,000.0 / Σ 11,300.0 = 88.5%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 88.5% = $4.92/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut` ← this one
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-gavnew</code> BUY 10,000 @ 1¢ → $4.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,300 (10,000 yours) | ×0.2^0 = 11,300.0 |
| | | **Σ** | **11,300.0** |

`yours 10,000.0 / Σ 11,300.0 = 88.5%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 88.5% = $4.92/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew` ← this one
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,677 resting) | ~64.7% | ~$16.16 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (57,765 resting) | ~15.6% | ~$11.66 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (70,757 resting) | ~8.0% | ~$5.98 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (29,044 resting) | ~20.0% | ~$4.99 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (6,742 resting) | ~16.4% | ~$4.11 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (634,137 resting) | ~8.5% | ~$2.13 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (928,008 resting) | ~2.7% | ~$2.06 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (680,791 resting) | ~2.7% | ~$2.04 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (278,902 resting) | ~2.7% | ~$2.04 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (316,382 resting) | ~2.0% | ~$1.47 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (295,272 resting) | ~1.6% | ~$1.23 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (137,937 resting) | ~4.1% | ~$1.03 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $1,180.25 |
| Skipped | $1.41 |
| **Total earned** | **$3,069.69** |

2234 reward rows · 41 days with rewards · 486 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-12 ⚠️ multi-day pending bucket | $213.04 | `████████` |
| 2026-08-11 | $409.59 | `███████████████` |
| 2026-08-10 | $557.62 | `████████████████████` |
| 2026-08-09 | $62.24 | `██` |
| 2026-08-08 | $54.78 | `██` |
| 2026-08-07 | $60.33 | `██` |
| 2026-08-06 | $52.21 | `██` |
| 2026-08-05 | $31.46 | `█` |
| 2026-08-04 | $53.94 | `██` |
| 2026-08-03 | $44.81 | `██` |
| 2026-08-02 | $14.05 | `█` |
| 2026-08-01 | $52.30 | `██` |
| 2026-07-31 | $67.96 | `██` |
| 2026-07-30 | $20.67 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $1,606.37 | `████████████████████` |
| 2026-07 | $1,463.32 | `██████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $127.10 |
| `apdc-alito-2026-12-31` | $111.76 |
| `opdc-mcconnell-resign-2026-11-02` | $77.87 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $47.80 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $40.44 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.03 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `scc-senate-gop-2026-11-03-49` | $28.51 |
| `scc-senate-gop-2026-11-03-48` | $27.99 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-14 2:58 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 2:45 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 2:22 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 2:20 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 2:15 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 2:09 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 1:15 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 12:08 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 11:42 AM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 11:40 AM ET | ✅ ok | 2234 | $3069.69 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
