# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-14 2:22 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$877.18/day estimated (ceiling, not promise — details below)

**Earned:** $3,069.69 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-12: **$213.04** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-11: **$409.59** · 2026-08-10: **$557.62** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$16.16/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$12.69/day), `ewc-usgub-ga-2026-11-03-rep` (~$11.59/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$877.18/day (~$36.55/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ewc-usp-2028-11-07-aleocc` | SELL | 39.0¢ | 33 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (10,220 resting ≥ 10,000 ✓) ≈ $5.56/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rahema` | SELL | 43.0¢ | 33 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (10,646 resting ≥ 10,000 ✓) ≈ $5.56/day (pool ÷ 27 markets) |
| `ussewc-usse-sc-2026-11-03-dem` | SELL | 10.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (196,015 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-rep-2028-vivram` | SELL | 33.0¢ | 33 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (10,195 resting ≥ 10,000 ✓) ≈ $10.71/day (pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-jamtal` | SELL | 25.0¢ | 33 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (12,635 resting ≥ 10,000 ✓) ≈ $8.82/day (pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (92,167 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 15.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~100.0% of bid side (50,425 resting ≥ 5,000 ✓) ≈ $3.85/day (pool ÷ 13 markets) |
| `enwc-uspres-nom-dem-2028-markel` | SELL | 43.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (12,643 resting ≥ 10,000 ✓) ≈ $8.82/day (pool ÷ 17 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 2.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (65,659 resting ≥ 2,000 ✓) ≈ $6.25/day (pool ÷ 2 markets) |
| `ewc-usp-party-2028-11-07-dem` | BUY | 65.0¢ | 9 | 0 | $300.00 | ✅ scoring — ~100.0% of bid side (10,487 resting ≥ 10,000 ✓) ≈ $74.98/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-jonoss` | SELL | 27.0¢ | 33 | 0 | $300.00 | ✅ scoring — ~99.6% of ask side (12,600 resting ≥ 10,000 ✓) ≈ $5.53/day (pool ÷ 27 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | BUY | 5.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~99.5% of bid side (2,450 resting ≥ 2,000 ✓) ≈ $6.22/day (pool ÷ 2 markets) |
| `usgubewc-usgub-fl-2026-11-03-rep` | SELL | 80.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~94.9% of ask side (10,603 resting ≥ 2,000 ✓) ≈ $5.93/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | SELL | 96.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~93.6% of ask side (2,426 resting ≥ 2,000 ✓) ≈ $5.85/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~93.0% of ask side (130,868 resting ≥ 2,000 ✓) ≈ $5.81/day (pool ÷ 2 markets) |
| `enwc-uspres-nom-dem-2028-aleocc` | SELL | 39.0¢ | 26 | 0 | $300.00 | ✅ scoring — ~92.8% of ask side (12,536 resting ≥ 10,000 ✓) ≈ $8.19/day (pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-aleocc` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.3% of bid side (11,200 resting ≥ 10,000 ✓) ≈ $4.96/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-rahema` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.3% of bid side (11,200 resting ≥ 10,000 ✓) ≈ $4.96/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-vivram` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.3% of bid side (11,200 resting ≥ 10,000 ✓) ≈ $9.57/day (pool ÷ 14 markets) |
| `usgubewc-usgub-ok-2026-11-03-dem` | SELL | 7.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~89.3% of ask side (130,853 resting ≥ 2,000 ✓) ≈ $5.58/day (pool ÷ 2 markets) |
| `ewc-usp-2028-11-07-tuccar` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-dontrujr` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-ranpau` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $9.55/day (pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-stasmi` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $7.86/day (pool ÷ 17 markets) |
| `enwc-uspres-nom-rep-2028-margre` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $9.55/day (pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-dwajoh` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $7.86/day (pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-micoba` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-elomus` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $9.55/day (pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-thomas` | BUY | 1.0¢ | 10,000 | 0 | $300.00 | ✅ scoring — ~89.1% of bid side (11,225 resting ≥ 10,000 ✓) ≈ $4.95/day (pool ÷ 27 markets) |
| …and 4569 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ewc-usp-2028-11-07-aleocc</code> SELL 33 @ 39¢ → $5.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 39¢ | 33 (33 yours) | ×0.2^0 = 33.0 |
|  | 99¢ | 10,187 | ×0.2^60 = 0.0 |
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
<details><summary><code>ewc-usp-2028-11-07-rahema</code> SELL 33 @ 43¢ → $5.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 33 (33 yours) | ×0.2^0 = 33.0 |
|  | 99¢ | 10,613 | ×0.2^56 = 0.0 |
| | | **Σ** | **33.0** |

`yours 33.0 / Σ 33.0 = 100.0%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 100.0% = $5.56/day`  

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
19. `ewc-usp-2028-11-07-rahema` ← this one
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
<details><summary><code>ussewc-usse-sc-2026-11-03-dem</code> SELL 40 @ 10¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 98¢ | 195,750 | ×0.1^88 = 0.0 |
| | | **Σ** | **40.0** |

`yours 40.0 / Σ 40.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem` ← this one
2. `ussewc-usse-sc-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-vivram</code> SELL 33 @ 33¢ → $10.71/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 33¢ | 33 (33 yours) | ×0.2^0 = 33.0 |
|  | 99¢ | 10,162 | ×0.2^66 = 0.0 |
| | | **Σ** | **33.0** |

`yours 33.0 / Σ 33.0 = 100.0%`  
`$300 ÷ 14 ÷ 2 = $10.71 × 100.0% = $10.71/day`  

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
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram` ← this one

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jamtal</code> SELL 33 @ 25¢ → $8.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 33 (33 yours) | ×0.2^0 = 33.0 |
|  | 39¢ | 142 | ×0.2^14 = 0.0 |
|  | 99¢ | 12,460 | ×0.2^74 = 0.0 |
| | | **Σ** | **33.0** |

`yours 33.0 / Σ 33.0 = 100.0%`  
`$300 ÷ 17 ÷ 2 = $8.82 × 100.0% = $8.82/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal` ← this one
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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 8¢ → $3.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 50 (50 yours) | ×0.2^0 = 50.0 |
|  | 20¢ | 100 | ×0.2^12 = 0.0 |
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
|  | 51¢ | 150 | ×0.2^8 = 0.0 |
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
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 30 @ 2¢ → $6.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 30 (30 yours) | ×0.1^0 = 30.0 |
|  | 5¢ | 4 | ×0.1^3 = 0.0 |
|  | 9¢ | 150 | ×0.1^7 = 0.0 |
|  | 98¢ | 65,250 | ×0.1^96 = 0.0 |
| | | **Σ** | **30.0** |

`yours 30.0 / Σ 30.0 = 100.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 100.0% = $6.25/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ewc-usp-party-2028-11-07-dem</code> BUY 9 @ 65¢ → $74.98/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 9 (9 yours) | ×0.2^0 = 9.0 |
|  | 64¢ | 0 | ×0.2^1 = 0.0 |
|  | 44¢ | 178 | ×0.2^21 = 0.0 |
|  | 40¢ | 100 | ×0.2^25 = 0.0 |
|  | 1¢ | 10,200 | ×0.2^64 = 0.0 |
| | | **Σ** | **9.0** |

`yours 9.0 / Σ 9.0 = 100.0%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 100.0% = $74.98/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usp-party-2028-11-07-dem` ← this one
2. `ewc-usp-party-2028-11-07-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jonoss</code> SELL 33 @ 27¢ → $5.53/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 33 (33 yours) | ×0.2^0 = 33.0 |
|  | 31¢ | 90 | ×0.2^4 = 0.1 |
|  | 99¢ | 12,477 | ×0.2^72 = 0.0 |
| | | **Σ** | **33.1** |

`yours 33.0 / Σ 33.1 = 99.6%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 99.6% = $5.53/day`  

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
12. `ewc-usp-2028-11-07-jonoss` ← this one
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
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> BUY 50 @ 5¢ → $6.22/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 1¢ | 2,400 | ×0.1^4 = 0.2 |
| | | **Σ** | **50.2** |

`yours 50.0 / Σ 50.2 = 99.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 99.5% = $6.22/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-fl-2026-11-03-rep</code> SELL 50 @ 80¢ → $5.93/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 80¢ | 50 (50 yours) | ×0.1^0 = 50.0 |
|  | 81¢ | 19 | ×0.1^1 = 1.9 |
|  | 82¢ | 81 | ×0.1^2 = 0.8 |
|  | 86¢ | 178 | ×0.1^6 = 0.0 |
|  | 93¢ | 50 | ×0.1^13 = 0.0 |
|  | 98¢ | 10,000 | ×0.1^18 = 0.0 |
| | | **Σ** | **52.7** |

`yours 50.0 / Σ 52.7 = 94.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 94.9% = $5.93/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-fl-2026-11-03-dem`
2. `usgubewc-usgub-fl-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> SELL 35 @ 96¢ → $5.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 35 (35 yours) | ×0.1^0 = 35.0 |
|  | 99¢ | 2,391 | ×0.1^3 = 2.4 |
| | | **Σ** | **37.4** |

`yours 35.0 / Σ 37.4 = 93.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.6% = $5.85/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $5.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 43 (40 yours) | ×0.1^0 = 43.0 |
|  | 9¢ | 100 | ×0.1^5 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^94 = 0.0 |
| | | **Σ** | **43.0** |

`yours 40.0 / Σ 43.0 = 93.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 93.0% = $5.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-aleocc</code> SELL 26 @ 39¢ → $8.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 39¢ | 26 (26 yours) | ×0.2^0 = 26.0 |
|  | 41¢ | 50 | ×0.2^2 = 2.0 |
|  | 99¢ | 12,460 | ×0.2^60 = 0.0 |
| | | **Σ** | **28.0** |

`yours 26.0 / Σ 28.0 = 92.8%`  
`$300 ÷ 17 ÷ 2 = $8.82 × 92.8% = $8.19/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc` ← this one
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
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-aleocc</code> BUY 10,000 @ 1¢ → $4.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,200 (10,000 yours) | ×0.2^0 = 11,200.0 |
| | | **Σ** | **11,200.0** |

`yours 10,000.0 / Σ 11,200.0 = 89.3%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.3% = $4.96/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rahema</code> BUY 10,000 @ 1¢ → $4.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,200 (10,000 yours) | ×0.2^0 = 11,200.0 |
| | | **Σ** | **11,200.0** |

`yours 10,000.0 / Σ 11,200.0 = 89.3%`  
`$300 ÷ 27 ÷ 2 = $5.56 × 89.3% = $4.96/day`  

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
19. `ewc-usp-2028-11-07-rahema` ← this one
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
<details><summary><code>enwc-uspres-nom-rep-2028-vivram</code> BUY 10,000 @ 1¢ → $9.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,200 (10,000 yours) | ×0.2^0 = 11,200.0 |
| | | **Σ** | **11,200.0** |

`yours 10,000.0 / Σ 11,200.0 = 89.3%`  
`$300 ÷ 14 ÷ 2 = $10.71 × 89.3% = $9.57/day`  

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
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ok-2026-11-03-dem</code> SELL 25 @ 7¢ → $5.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 28 (25 yours) | ×0.1^0 = 28.0 |
|  | 12¢ | 100 | ×0.1^5 = 0.0 |
|  | 98¢ | 130,500 | ×0.1^91 = 0.0 |
| | | **Σ** | **28.0** |

`yours 25.0 / Σ 28.0 = 89.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 89.3% = $5.58/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ok-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tuccar</code> BUY 10,000 @ 1¢ → $4.95/day</summary>

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
24. `ewc-usp-2028-11-07-tuccar` ← this one
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
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
<details><summary><code>enwc-uspres-nom-dem-2028-dwajoh</code> BUY 10,000 @ 1¢ → $7.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 11,225 (10,000 yours) | ×0.2^0 = 11,225.0 |
| | | **Σ** | **11,225.0** |

`yours 10,000.0 / Σ 11,225.0 = 89.1%`  
`$300 ÷ 17 ÷ 2 = $8.82 × 89.1% = $7.86/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh` ← this one
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
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,865 resting) | ~64.7% | ~$16.16 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (86,020 resting) | ~16.9% | ~$12.69 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (83,445 resting) | ~15.4% | ~$11.59 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (29,037 resting) | ~20.1% | ~$5.02 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (7,363 resting) | ~16.4% | ~$4.10 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (144,369 resting) | ~12.3% | ~$3.08 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (88,307 resting) | ~46.0% | ~$2.87 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (944,367 resting) | ~3.0% | ~$2.28 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (634,274 resting) | ~8.8% | ~$2.20 |
| `ewc-usse-ia-2026-11-03-dem` | $25.00 ÷ 2 | 0.10 | 2,000 | SELL side (83,499 resting) | ~28.9% | ~$1.81 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (681,830 resting) | ~2.4% | ~$1.80 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (280,941 resting) | ~2.3% | ~$1.75 |

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
| 2026-08-14 2:22 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 2:20 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 2:15 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 2:09 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 1:15 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 12:08 PM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 11:42 AM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 11:40 AM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 11:38 AM ET | ✅ ok | 2234 | $3069.69 |
| 2026-08-14 11:10 AM ET | ✅ ok | 2234 | $3069.69 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
