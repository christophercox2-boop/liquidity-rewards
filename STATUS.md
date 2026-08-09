# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-09 12:02 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$109.63/day estimated (ceiling, not promise — details below)

**Earned:** $1,772.42 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-07: **$60.33** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-06: **$52.21** · 2026-08-05: **$31.46** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — SELL at the best price, ~$36.43/day for 200 contracts. Runners-up: `ewc-usgub-ca-2026-11-03-xavbec` (~$17.69/day), `apdc-jerpowgov-2026-08-31` (~$15.92/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$109.63/day (~$4.57/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 54.0¢ | 23 | 0 | $100.00 | ✅ scoring — ~100.0% of ask side (62,953 resting ≥ 5,000 ✓) ≈ $4.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~98.0% of bid side (200,553 resting ≥ 5,000 ✓) ≈ $3.77/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~96.0% of bid side (50,558 resting ≥ 5,000 ✓) ≈ $3.69/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 22.0¢ | 7 | 2 | $100.00 | ✅ scoring — ~90.3% of bid side (85,736 resting ≥ 5,000 ✓) ≈ $3.76/day (pool ÷ 12 markets) |
| `tec-cbb-champ-2027-04-05-w-uconn` | BUY | 14.0¢ | 2 | 0 | $500.00 | ✅ scoring — ~88.4% of bid side (8,789 resting ≥ 2,500 ✓) ≈ $3.03/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~86.9% of bid side (10,504 resting ≥ 5,000 ✓) ≈ $3.34/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 46.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~85.2% of ask side (48,199 resting ≥ 5,000 ✓) ≈ $3.55/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 49.0¢ | 115 | 0 | $100.00 | ✅ scoring — ~82.0% of bid side (80,684 resting ≥ 5,000 ✓) ≈ $3.42/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 15.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~67.7% of ask side (113,533 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 24.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~63.4% of bid side (5,447 resting ≥ 5,000 ✓) ≈ $15.86/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 77.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~61.6% of bid side (80,583 resting ≥ 5,000 ✓) ≈ $2.57/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 23 | 0 | $100.00 | ✅ scoring — ~56.6% of ask side (99,469 resting ≥ 5,000 ✓) ≈ $2.18/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 8.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~55.2% of ask side (113,529 resting ≥ 5,000 ✓) ≈ $2.12/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~54.1% of ask side (117,802 resting ≥ 5,000 ✓) ≈ $2.08/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~51.3% of ask side (62,870 resting ≥ 5,000 ✓) ≈ $2.14/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 66.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~48.5% of ask side (7,364 resting ≥ 5,000 ✓) ≈ $2.02/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 43.0¢ | 11 | 0 | $100.00 | ✅ scoring — ~45.8% of bid side (80,474 resting ≥ 5,000 ✓) ≈ $1.91/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 12.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~45.5% of bid side (35,614 resting ≥ 2,000 ✓) ≈ $5.68/day |
| `scc-senate-gop-2026-11-03-49` | SELL | 44.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~43.5% of ask side (98,520 resting ≥ 5,000 ✓) ≈ $1.67/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 6.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~42.6% of bid side (27,846 resting ≥ 5,000 ✓) ≈ $1.64/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 16.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~40.0% of bid side (50,615 resting ≥ 5,000 ✓) ≈ $1.54/day (pool ÷ 13 markets) |
| `pandc-anydis-2027-12-31` | BUY | 15.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~38.5% of bid side (11,117 resting ≥ 10,000 ✓) ≈ $4.81/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 52.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~33.3% of bid side (80,465 resting ≥ 5,000 ✓) ≈ $1.39/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 25.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~32.1% of ask side (113,543 resting ≥ 5,000 ✓) ≈ $1.24/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 75.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~32.1% of bid side (50,338 resting ≥ 5,000 ✓) ≈ $1.34/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~26.8% of bid side (50,375 resting ≥ 5,000 ✓) ≈ $1.03/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 21 | 2 | $100.00 | ✅ scoring — ~25.9% of bid side (80,583 resting ≥ 5,000 ✓) ≈ $1.08/day (pool ÷ 12 markets) |
| `apdc-alito-2026-12-31` | BUY | 5.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~24.8% of bid side (27,731 resting ≥ 5,000 ✓) ≈ $6.20/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 9.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~22.1% of ask side (113,529 resting ≥ 5,000 ✓) ≈ $0.85/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 28.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~21.7% of ask side (113,566 resting ≥ 5,000 ✓) ≈ $0.84/day (pool ÷ 13 markets) |
| …and 44 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 23 @ 54¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 54¢ | 23 (23 yours) | ×0.2^0 = 23.0 |
|  | 70¢ | 205 | ×0.2^16 = 0.0 |
|  | 90¢ | 1 | ×0.2^36 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^44 = 0.0 |
| | | **Σ** | **23.0** |

`yours 23.0 / Σ 23.0 = 100.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 100.0% = $4.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 2 @ 19¢ → $3.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 2 (2 yours) | ×0.2^0 = 2.0 |
|  | 16¢ | 5 | ×0.2^3 = 0.0 |
|  | 5¢ | 115 | ×0.2^14 = 0.0 |
|  | 1¢ | 200,431 | ×0.2^18 = 0.0 |
| | | **Σ** | **2.0** |

`yours 2.0 / Σ 2.0 = 98.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.0% = $3.77/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 5 @ 9¢ → $3.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 5 (5 yours) | ×0.2^0 = 5.1 |
|  | 1¢ | 50,553 | ×0.2^8 = 0.1 |
| | | **Σ** | **5.2** |

`yours 5.0 / Σ 5.2 = 96.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 96.0% = $3.69/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 7 @ 22¢ → $3.76/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 24¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 22¢ | 7 (7 yours) | ×0.2^2 = 0.3 |
|  | 17¢ | 0 | ×0.2^7 = 0.0 |
|  | 8¢ | 100 | ×0.2^16 = 0.0 |
|  | 7¢ | 81 | ×0.2^17 = 0.0 |
|  | 3¢ | 5,247 | ×0.2^21 = 0.0 |
| | | **Σ** | **0.3** |

`yours 0.3 / Σ 0.3 = 90.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 90.3% = $3.76/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205`
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220` ← this one
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>tec-cbb-champ-2027-04-05-w-uconn</code> BUY 2 @ 14¢ → $3.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 2 (2 yours) | ×0.35^0 = 2.0 |
|  | 6¢ | 1,083 | ×0.35^8 = 0.2 |
|  | 3¢ | 979 | ×0.35^11 = 0.0 |
|  | 2¢ | 3,000 | ×0.35^12 = 0.0 |
| | | **Σ** | **2.3** |

`yours 2.0 / Σ 2.3 = 88.4%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 88.4% = $3.03/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 1 @ 13¢ → $3.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 3 | ×0.2^6 = 0.0 |
|  | 6¢ | 10,249 | ×0.2^7 = 0.1 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 86.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 86.9% = $3.34/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 10 @ 46¢ → $3.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 46¢ | 11 (10 yours) | ×0.2^0 = 11.0 |
|  | 50¢ | 462 | ×0.2^4 = 0.7 |
|  | 52¢ | 1 | ×0.2^6 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^52 = 0.0 |
| | | **Σ** | **11.7** |

`yours 10.0 / Σ 11.7 = 85.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 85.2% = $3.55/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 115 @ 49¢ → $3.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 140 (115 yours) | ×0.2^0 = 140.3 |
|  | 14¢ | 154 | ×0.2^35 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^47 = 0.0 |
| | | **Σ** | **140.3** |

`yours 115.0 / Σ 140.3 = 82.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 82.0% = $3.42/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 21 @ 15¢ → $2.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 31 (21 yours) | ×0.2^0 = 31.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 81¢ | 0 | ×0.2^66 = 0.0 |
|  | 82¢ | 0 | ×0.2^67 = 0.0 |
|  | 83¢ | 0 | ×0.2^68 = 0.0 |
|  | 84¢ | 0 | ×0.2^69 = 0.0 |
|  | 85¢ | 0 | ×0.2^70 = 0.0 |
|  | 86¢ | 0 | ×0.2^71 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^82 = 0.0 |
| | | **Σ** | **31.0** |

`yours 21.0 / Σ 31.0 = 67.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.7% = $2.60/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 30 @ 24¢ → $15.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 47 (30 yours) | ×0.2^0 = 47.3 |
|  | 12¢ | 100 | ×0.2^12 = 0.0 |
|  | 2¢ | 100 | ×0.2^22 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^23 = 0.0 |
| | | **Σ** | **47.3** |

`yours 30.0 / Σ 47.3 = 63.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 63.4% = $15.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 2 @ 77¢ → $2.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 2 (2 yours) | ×0.2^0 = 2.0 |
|  | 75¢ | 31 | ×0.2^2 = 1.2 |
|  | 71¢ | 100 | ×0.2^6 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^75 = 0.0 |
| | | **Σ** | **3.2** |

`yours 2.0 / Σ 3.2 = 61.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 61.6% = $2.57/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 23 @ 20¢ → $2.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 34 (23 yours) | ×0.2^0 = 34.0 |
|  | 23¢ | 829 | ×0.2^3 = 6.6 |
|  | 47¢ | 99 | ×0.2^27 = 0.0 |
|  | 50¢ | 99 | ×0.2^30 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^77 = 0.0 |
| | | **Σ** | **40.6** |

`yours 23.0 / Σ 40.6 = 56.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 56.6% = $2.18/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 5 @ 8¢ → $2.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 7 (5 yours) | ×0.2^0 = 7.0 |
|  | 9¢ | 10 | ×0.2^1 = 2.0 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 11¢ | 5 | ×0.2^3 = 0.0 |
|  | 15¢ | 5 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^89 = 0.0 |
| | | **Σ** | **9.1** |

`yours 5.0 / Σ 9.1 = 55.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 55.2% = $2.12/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 20 @ 4¢ → $2.08/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 37 (20 yours) | ×0.2^0 = 37.0 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **37.0** |

`yours 20.0 / Σ 37.0 = 54.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 54.1% = $2.08/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 20 @ 48¢ → $2.14/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 39 (20 yours) | ×0.2^0 = 39.0 |
|  | 51¢ | 1 | ×0.2^3 = 0.0 |
|  | 60¢ | 5 | ×0.2^12 = 0.0 |
|  | 61¢ | 100 | ×0.2^13 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **39.0** |

`yours 20.0 / Σ 39.0 = 51.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 51.3% = $2.14/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `scc-hrep-rep-2026-11-03-gte180`
2. `scc-hrep-rep-2026-11-03-gte185`
3. `scc-hrep-rep-2026-11-03-gte190`
4. `scc-hrep-rep-2026-11-03-gte195`
5. `scc-hrep-rep-2026-11-03-gte200`
6. `scc-hrep-rep-2026-11-03-gte205` ← this one
7. `scc-hrep-rep-2026-11-03-gte210`
8. `scc-hrep-rep-2026-11-03-gte215`
9. `scc-hrep-rep-2026-11-03-gte220`
10. `scc-hrep-rep-2026-11-03-gte225`
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 10 @ 66¢ → $2.02/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 66¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 67¢ | 28 | ×0.2^1 = 5.6 |
|  | 75¢ | 187 | ×0.2^9 = 0.0 |
|  | 99¢ | 7,134 | ×0.2^33 = 0.0 |
| | | **Σ** | **20.6** |

`yours 10.0 / Σ 20.6 = 48.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 48.5% = $2.02/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 11 @ 43¢ → $1.91/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 24 (11 yours) | ×0.2^0 = 24.0 |
|  | 2¢ | 80,250 | ×0.2^41 = 0.0 |
| | | **Σ** | **24.0** |

`yours 11.0 / Σ 24.0 = 45.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 45.8% = $1.91/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 30 @ 12¢ → $5.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 66 (30 yours) | ×0.1^0 = 66.0 |
|  | 6¢ | 22 | ×0.1^6 = 0.0 |
|  | 5¢ | 99 | ×0.1^7 = 0.0 |
|  | 3¢ | 100 | ×0.1^9 = 0.0 |
|  | 1¢ | 35,326 | ×0.1^11 = 0.0 |
| | | **Σ** | **66.0** |

`yours 30.0 / Σ 66.0 = 45.5%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 45.5% = $5.68/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 44¢ → $1.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 44¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 45¢ | 64 | ×0.2^1 = 12.8 |
|  | 47¢ | 25 | ×0.2^3 = 0.2 |
|  | 50¢ | 13 | ×0.2^6 = 0.0 |
|  | 66¢ | 0 | ×0.2^22 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^53 = 0.0 |
| | | **Σ** | **23.0** |

`yours 10.0 / Σ 23.0 = 43.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 43.5% = $1.67/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 10 @ 6¢ → $1.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 11 (10 yours) | ×0.2^0 = 11.0 |
|  | 2¢ | 2,766 | ×0.2^4 = 4.4 |
|  | 1¢ | 25,069 | ×0.2^5 = 8.0 |
| | | **Σ** | **23.4** |

`yours 10.0 / Σ 23.4 = 42.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 42.6% = $1.64/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 16¢ → $1.54/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 25 (10 yours) | ×0.2^0 = 25.0 |
|  | 12¢ | 0 | ×0.2^4 = 0.0 |
|  | 11¢ | 45 | ×0.2^5 = 0.0 |
|  | 2¢ | 50,209 | ×0.2^14 = 0.0 |
| | | **Σ** | **25.0** |

`yours 10.0 / Σ 25.0 = 40.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 40.0% = $1.54/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> BUY 10 @ 15¢ → $4.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 26 (10 yours) | ×0.25^0 = 26.0 |
|  | 8¢ | 101 | ×0.25^7 = 0.0 |
|  | 2¢ | 4 | ×0.25^13 = 0.0 |
|  | 1¢ | 10,986 | ×0.25^14 = 0.0 |
| | | **Σ** | **26.0** |

`yours 10.0 / Σ 26.0 = 38.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 38.5% = $4.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 5 @ 52¢ → $1.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 52¢ | 15 (5 yours) | ×0.2^0 = 15.0 |
|  | 2¢ | 80,250 | ×0.2^50 = 0.0 |
| | | **Σ** | **15.0** |

`yours 5.0 / Σ 15.0 = 33.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 33.3% = $1.39/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 5 @ 25¢ → $1.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 16 (5 yours) | ×0.2^0 = 15.6 |
|  | 50¢ | 125 | ×0.2^25 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^72 = 0.0 |
| | | **Σ** | **15.6** |

`yours 5.0 / Σ 15.6 = 32.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.1% = $1.24/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 5 @ 75¢ → $1.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 74¢ | 33 | ×0.2^1 = 6.6 |
|  | 73¢ | 100 | ×0.2^2 = 4.0 |
|  | 69¢ | 0 | ×0.2^6 = 0.0 |
|  | 67¢ | 0 | ×0.2^8 = 0.0 |
|  | 64¢ | 0 | ×0.2^11 = 0.0 |
|  | 63¢ | 0 | ×0.2^12 = 0.0 |
|  | 62¢ | 0 | ×0.2^13 = 0.0 |
|  | 61¢ | 0 | ×0.2^14 = 0.0 |
|  | 60¢ | 0 | ×0.2^15 = 0.0 |
| | … | +2 levels | 0.0 |
| | | **Σ** | **15.6** |

`yours 5.0 / Σ 15.6 = 32.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 32.1% = $1.34/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 7 @ 18¢ → $1.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 20 (7 yours) | ×0.2^0 = 20.5 |
|  | 17¢ | 24 | ×0.2^1 = 4.8 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **27.9** |

`yours 7.5 / Σ 27.9 = 26.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.8% = $1.03/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 21 @ 75¢ → $1.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 77¢ | 2 | ×0.2^0 = 2.0 |
| ▶ | 75¢ | 31 (21 yours) | ×0.2^2 = 1.2 |
|  | 71¢ | 100 | ×0.2^6 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^75 = 0.0 |
| | | **Σ** | **3.2** |

`yours 0.8 / Σ 3.2 = 25.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 25.9% = $1.08/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> BUY 20 @ 5¢ → $6.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 2¢ | 2,549 | ×0.2^3 = 20.4 |
|  | 1¢ | 25,162 | ×0.2^4 = 40.3 |
| | | **Σ** | **80.6** |

`yours 20.0 / Σ 80.6 = 24.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 24.8% = $6.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 10 @ 9¢ → $0.85/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 7 | ×0.2^0 = 7.0 |
| ▶ | 9¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 11¢ | 5 | ×0.2^3 = 0.0 |
|  | 15¢ | 5 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^89 = 0.0 |
| | | **Σ** | **9.1** |

`yours 2.0 / Σ 9.1 = 22.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 22.1% = $0.85/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 5 @ 28¢ → $0.84/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 21 (5 yours) | ×0.2^0 = 21.0 |
|  | 29¢ | 10 | ×0.2^1 = 2.0 |
|  | 34¢ | 30 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^69 = 0.0 |
| | | **Σ** | **23.0** |

`yours 5.0 / Σ 23.0 = 21.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 21.7% = $0.84/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-06 | ~$60.78 | $52.21 | 86% |
| 2026-08-05 | ~$33.74 | $31.46 | 93% |
| 2026-08-04 | ~$67.52 | $53.94 | 80% |

Biggest gaps on 2026-08-06: `scc-senate-gop-2026-11-03-52` (est ~$1.89 → got $0.00), `opdc-mcconnell-resign-2026-11-02` (est ~$8.92 → got $8.07), `scc-hrep-rep-2026-11-03-gte195` (est ~$3.20 → got $2.38)

_2026-08-07 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (219,983 resting) | ~48.6% | ~$36.43 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (326,556 resting) | ~23.6% | ~$17.69 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,506 resting) | ~63.7% | ~$15.92 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (66,867 resting) | ~60.8% | ~$15.20 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,377 resting) | ~56.3% | ~$14.08 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,640 resting) | ~52.5% | ~$13.12 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (5,481 resting) | ~51.2% | ~$12.81 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (215,009 resting) | ~12.9% | ~$9.67 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (83,011 resting) | ~30.7% | ~$7.69 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,228 resting) | ~7.2% | ~$5.41 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (189,184 resting) | ~4.9% | ~$3.64 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (68,004 resting) | ~41.5% | ~$2.59 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,627.01 |
| Pending | $144.00 |
| Skipped | $1.41 |
| **Total earned** | **$1,772.42** |

1749 reward rows · 36 days with rewards · 377 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-07 ⚠️ multi-day pending bucket | $60.33 | `████████` |
| 2026-08-06 | $52.21 | `███████` |
| 2026-08-05 | $31.46 | `████` |
| 2026-08-04 | $53.94 | `███████` |
| 2026-08-03 | $44.81 | `██████` |
| 2026-08-02 | $14.05 | `██` |
| 2026-08-01 | $52.30 | `███████` |
| 2026-07-31 | $67.96 | `█████████` |
| 2026-07-30 | $20.67 | `███` |
| 2026-07-29 | $53.60 | `███████` |
| 2026-07-28 | $79.65 | `██████████` |
| 2026-07-27 | $125.34 | `████████████████` |
| 2026-07-26 | $153.80 | `████████████████████` |
| 2026-07-25 | $125.69 | `████████████████` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $309.10 | `████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $77.48 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `opdc-mcconnell-resign-2026-11-02` | $52.92 |
| `apdc-jerpowgov-2026-12-31` | $49.91 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.92 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `scc-hrep-rep-2026-11-03-gte200` | $29.77 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.19 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-09 12:02 PM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 11:52 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 11:50 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 11:05 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 10:55 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 10:34 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 10:02 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 9:18 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 7:48 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 6:55 AM ET | ✅ ok | 1749 | $1772.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
