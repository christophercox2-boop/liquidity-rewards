# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-30 12:52 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$10.40/day estimated (ceiling, not promise — details below)

**Earned:** $1,321.41 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-29: **$0.32** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `cranc-uspres28-12-31-2026-dontru` — BUY at the best price, ~$1.52/day for 200 contracts. Runners-up: `cranc-uspres28-12-31-2026-petbut` (~$1.51/day), `cranc-uspres28-12-31-2026-andyan` (~$1.51/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$10.40/day (~$0.43/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-51` | SELL | 22.0¢ | 18 | 1 | $100.00 | ✅ scoring — ~98.8% of ask side (11,224 resting ≥ 5,000 ✓) ≈ $3.80/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 6.0¢ | 30 | 1 | $100.00 | ✅ scoring — ~78.5% of bid side (25,475 resting ≥ 5,000 ✓) ≈ $3.02/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 5.0¢ | 196 | 1 | $100.00 | ✅ scoring — ~31.3% of bid side (25,766 resting ≥ 5,000 ✓) ≈ $1.20/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 6.0¢ | 49 | 2 | $100.00 | ✅ scoring — ~27.4% of bid side (25,347 resting ≥ 5,000 ✓) ≈ $1.05/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 87.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~22.5% of ask side (8,928 resting ≥ 5,000 ✓) ≈ $0.94/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 1.0¢ | 5,000 | 6 | $100.00 | ✅ scoring — ~4.2% of bid side (25,475 resting ≥ 5,000 ✓) ≈ $0.16/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 17.0¢ | 100 | 4 | $100.00 | ✅ scoring — ~3.6% of ask side (11,418 resting ≥ 5,000 ✓) ≈ $0.14/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 1.0¢ | 5,000 | 5 | $100.00 | ✅ scoring — ~1.3% of bid side (25,766 resting ≥ 5,000 ✓) ≈ $0.05/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 1.0¢ | 5,000 | 7 | $100.00 | ✅ scoring — ~0.9% of bid side (25,347 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-kamhar` | SELL | 27.0¢ | 2 | 4 | $100.00 | ✅ scoring — ~0.0% of ask side (5,176 resting ≥ 5,000 ✓) ≈ $0.00/day (pool ÷ 33 markets) |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 18 @ 22¢ → $3.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 22¢ | 18 (18 yours) | ×0.2^1 = 3.5 |
|  | 26¢ | 100 | ×0.2^5 = 0.0 |
|  | 37¢ | 5 | ×0.2^16 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **3.6** |

`yours 3.5 / Σ 3.6 = 98.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.8% = $3.80/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 30 @ 6¢ → $3.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 6¢ | 30 (30 yours) | ×0.2^1 = 6.0 |
|  | 1¢ | 25,445 | ×0.2^6 = 1.6 |
| | | **Σ** | **7.6** |

`yours 6.0 / Σ 7.6 = 78.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 78.5% = $3.02/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 196 @ 5¢ → $1.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 5¢ | 586 (196 yours) | ×0.2^1 = 117.2 |
|  | 1¢ | 25,180 | ×0.2^5 = 8.1 |
| | | **Σ** | **125.3** |

`yours 39.2 / Σ 125.3 = 31.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.3% = $1.20/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 49 @ 6¢ → $1.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 5 | ×0.2^1 = 1.0 |
| ▶ | 6¢ | 146 (49 yours) | ×0.2^2 = 5.8 |
|  | 1¢ | 25,196 | ×0.2^7 = 0.3 |
| | | **Σ** | **7.2** |

`yours 2.0 / Σ 7.2 = 27.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 27.4% = $1.05/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 50 @ 87¢ → $0.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 87¢ | 220 (50 yours) | ×0.2^0 = 220.0 |
|  | 89¢ | 45 | ×0.2^2 = 1.8 |
|  | 99¢ | 8,663 | ×0.2^12 = 0.0 |
| | | **Σ** | **221.8** |

`yours 50.0 / Σ 221.8 = 22.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 22.5% = $0.94/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 5,000 @ 1¢ → $0.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 7¢ | 0 | ×0.2^0 = 0.0 |
|  | 6¢ | 30 | ×0.2^1 = 6.0 |
| ▶ | 1¢ | 25,445 (5,000 yours) | ×0.2^6 = 1.6 |
| | | **Σ** | **7.6** |

`yours 0.3 / Σ 7.6 = 4.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 4.2% = $0.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 100 @ 17¢ → $0.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 0 | ×0.2^0 = 0.0 |
|  | 14¢ | 20 | ×0.2^1 = 4.0 |
| ▶ | 17¢ | 268 (100 yours) | ×0.2^4 = 0.4 |
|  | 40¢ | 29 | ×0.2^27 = 0.0 |
|  | 50¢ | 100 | ×0.2^37 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^85 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^86 = 0.0 |
| | | **Σ** | **4.5** |

`yours 0.2 / Σ 4.5 = 3.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.6% = $0.14/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 5,000 @ 1¢ → $0.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 0 | ×0.2^0 = 0.0 |
|  | 5¢ | 586 | ×0.2^1 = 117.2 |
| ▶ | 1¢ | 25,180 (5,000 yours) | ×0.2^5 = 8.1 |
| | | **Σ** | **125.3** |

`yours 1.6 / Σ 125.3 = 1.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.3% = $0.05/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 5,000 @ 1¢ → $0.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 0 | ×0.2^0 = 0.0 |
|  | 7¢ | 5 | ×0.2^1 = 1.0 |
|  | 6¢ | 146 | ×0.2^2 = 5.8 |
| ▶ | 1¢ | 25,196 (5,000 yours) | ×0.2^7 = 0.3 |
| | | **Σ** | **7.2** |

`yours 0.1 / Σ 7.2 = 0.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.9% = $0.03/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-kamhar</code> SELL 2 @ 27¢ → $0.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 0 | ×0.2^0 = 0.0 |
|  | 24¢ | 13 | ×0.2^1 = 2.6 |
|  | 25¢ | 599 | ×0.2^2 = 24.0 |
| ▶ | 27¢ | 4 (2 yours) | ×0.2^4 = 0.0 |
|  | 45¢ | 192 | ×0.2^22 = 0.0 |
|  | 50¢ | 25 | ×0.2^27 = 0.0 |
|  | 99¢ | 4,343 | ×0.2^76 = 0.0 |
| | | **Σ** | **26.6** |

`yours 0.0 / Σ 26.6 = 0.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 0.0% = $0.00/day`  

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
17. `cranc-uspres28-12-31-2026-kamhar` ← this one
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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-29 | ~$65.42 | $0.32 | 0% |
| 2026-07-28 | ~$148.78 | $79.65 | 54% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |

Biggest gaps on 2026-07-29: `apdc-petehegseth-2026-12-31` (est ~$12.90 → got $0.00), `scc-senate-gop-2026-11-03-51` (est ~$3.25 → got $0.00), `scc-senate-gop-2026-11-03-55` (est ~$2.26 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `cranc-uspres28-12-31-2026-dontru` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,224 resting) | ~100.0% | ~$1.52 |
| `cranc-uspres28-12-31-2026-petbut` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,207 resting) | ~100.0% | ~$1.51 |
| `cranc-uspres28-12-31-2026-andyan` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (10,458 resting) | ~99.9% | ~$1.51 |
| `cranc-uspres28-12-31-2026-tuccar` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,512 resting) | ~99.9% | ~$1.51 |
| `cranc-uspres28-12-31-2026-micoba` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,626 resting) | ~99.9% | ~$1.51 |
| `cranc-uspres28-12-31-2026-aleoca` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,757 resting) | ~99.7% | ~$1.51 |
| `cranc-uspres28-12-31-2026-hunbid` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (30,218 resting) | ~98.9% | ~$1.50 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,500 resting) | ~98.8% | ~$1.50 |
| `cranc-uspres28-12-31-2026-margre` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (30,361 resting) | ~98.6% | ~$1.49 |
| `cranc-uspres28-12-31-2026-marrub` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,506 resting) | ~97.2% | ~$1.47 |
| `cranc-uspres28-12-31-2026-rahema` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,389 resting) | ~95.0% | ~$1.44 |
| `cranc-uspres28-12-31-2026-corboo` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,924 resting) | ~94.1% | ~$1.43 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,240.74 |
| Pending | $79.46 |
| Skipped | $1.21 |
| **Total earned** | **$1,321.41** |

1267 reward rows · 27 days with rewards · 352 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-29 | $0.32 | `█` |
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
| 2026-07 | $1,321.41 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.23 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.22 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.75 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.47 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.70 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.21 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.64 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `vmc-ussep-misen-2026-08-04-els15-20` | $22.78 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-30 12:52 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 10:36 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 8:06 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 5:45 AM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-30 2:45 AM ET | ❌ error | 1267 | $1321.41 |
| 2026-07-29 11:34 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:36 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:19 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:18 PM ET | ✅ ok | 1267 | $1321.41 |
| 2026-07-29 9:09 PM ET | ✅ ok | 1256 | $1321.25 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
