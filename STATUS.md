# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-09 10:55 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$102.95/day estimated (ceiling, not promise — details below)

**Earned:** $1,772.42 lifetime ($1,627.01 paid). Last three recorded days — 2026-08-07: **$60.33** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-06: **$52.21** · 2026-08-05: **$31.46** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — SELL at the best price, ~$24.52/day for 200 contracts. Runners-up: `ewc-usgub-ca-2026-11-03-xavbec` (~$17.68/day), `apdc-jerpowgov-2026-08-31` (~$15.97/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$102.95/day (~$4.29/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 54.0¢ | 3 | 0 | $100.00 | ✅ scoring — ~99.8% of ask side (63,052 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 49.0¢ | 115 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (80,659 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~98.0% of bid side (200,553 resting ≥ 5,000 ✓) ≈ $3.77/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~96.0% of bid side (50,558 resting ≥ 5,000 ✓) ≈ $3.69/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-uconn` | BUY | 14.0¢ | 2 | 0 | $500.00 | ✅ scoring — ~88.4% of bid side (8,784 resting ≥ 2,500 ✓) ≈ $3.03/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~86.9% of bid side (10,504 resting ≥ 5,000 ✓) ≈ $3.34/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 46.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~85.2% of ask side (48,199 resting ≥ 5,000 ✓) ≈ $3.55/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 15.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~67.7% of ask side (113,533 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~67.4% of bid side (80,581 resting ≥ 5,000 ✓) ≈ $2.81/day (pool ÷ 12 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 24.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~63.4% of bid side (5,347 resting ≥ 5,000 ✓) ≈ $15.86/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 73.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~58.1% of ask side (5,501 resting ≥ 5,000 ✓) ≈ $2.42/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~54.1% of ask side (117,802 resting ≥ 5,000 ✓) ≈ $2.08/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~51.3% of ask side (62,870 resting ≥ 5,000 ✓) ≈ $2.14/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 23 | 0 | $100.00 | ✅ scoring — ~49.1% of ask side (99,373 resting ≥ 5,000 ✓) ≈ $1.89/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 12.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~45.5% of bid side (35,614 resting ≥ 2,000 ✓) ≈ $5.68/day |
| `pandc-anydis-2027-12-31` | SELL | 25.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~43.5% of ask side (11,013 resting ≥ 10,000 ✓) ≈ $5.43/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 71.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~43.1% of bid side (50,298 resting ≥ 5,000 ✓) ≈ $1.80/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~42.3% of bid side (50,376 resting ≥ 5,000 ✓) ≈ $1.63/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 25.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~41.0% of bid side (85,752 resting ≥ 5,000 ✓) ≈ $1.71/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 28.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~38.5% of ask side (113,526 resting ≥ 5,000 ✓) ≈ $1.48/day (pool ÷ 13 markets) |
| `pandc-anydis-2027-12-31` | BUY | 15.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~38.5% of bid side (11,117 resting ≥ 10,000 ✓) ≈ $4.81/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 26.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~32.1% of ask side (113,543 resting ≥ 5,000 ✓) ≈ $1.24/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~32.1% of bid side (80,581 resting ≥ 5,000 ✓) ≈ $1.34/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 25.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~31.1% of bid side (100,701 resting ≥ 5,000 ✓) ≈ $1.20/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 52.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~26.3% of bid side (80,496 resting ≥ 5,000 ✓) ≈ $1.10/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 17.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~22.6% of bid side (50,376 resting ≥ 5,000 ✓) ≈ $0.87/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | SELL | 75.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~20.8% of ask side (9,139 resting ≥ 5,000 ✓) ≈ $0.87/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 11.0¢ | 5 | 1 | $100.00 | ✅ scoring — ~20.2% of ask side (113,533 resting ≥ 5,000 ✓) ≈ $0.78/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~17.0% of ask side (113,737 resting ≥ 5,000 ✓) ≈ $0.65/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 43.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~16.7% of bid side (80,556 resting ≥ 5,000 ✓) ≈ $0.69/day (pool ÷ 12 markets) |
| …and 51 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 3 @ 54¢ → $4.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 54¢ | 3 (3 yours) | ×0.2^0 = 3.0 |
|  | 59¢ | 12 | ×0.2^5 = 0.0 |
|  | 60¢ | 10 | ×0.2^6 = 0.0 |
|  | 62¢ | 42 | ×0.2^8 = 0.0 |
|  | 63¢ | 5 | ×0.2^9 = 0.0 |
|  | 65¢ | 50 | ×0.2^11 = 0.0 |
|  | 70¢ | 205 | ×0.2^16 = 0.0 |
|  | 90¢ | 1 | ×0.2^36 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^44 = 0.0 |
| | | **Σ** | **3.0** |

`yours 3.0 / Σ 3.0 = 99.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.8% = $4.16/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 115 @ 49¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 115 (115 yours) | ×0.2^0 = 115.3 |
|  | 14¢ | 154 | ×0.2^35 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^47 = 0.0 |
| | | **Σ** | **115.3** |

`yours 115.0 / Σ 115.3 = 99.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.8% = $4.16/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-uconn</code> BUY 2 @ 14¢ → $3.03/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 2 (2 yours) | ×0.35^0 = 2.0 |
|  | 6¢ | 1,083 | ×0.35^8 = 0.2 |
|  | 3¢ | 925 | ×0.35^11 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 21 @ 75¢ → $2.81/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 31 (21 yours) | ×0.2^0 = 31.0 |
|  | 71¢ | 100 | ×0.2^4 = 0.2 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
| | | **Σ** | **31.2** |

`yours 21.0 / Σ 31.2 = 67.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 67.4% = $2.81/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 30 @ 24¢ → $15.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 47 (30 yours) | ×0.2^0 = 47.3 |
|  | 12¢ | 100 | ×0.2^12 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^23 = 0.0 |
| | | **Σ** | **47.3** |

`yours 30.0 / Σ 47.3 = 63.4%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 63.4% = $15.86/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 10 @ 73¢ → $2.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 73¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 74¢ | 36 | ×0.2^1 = 7.2 |
|  | 82¢ | 333 | ×0.2^9 = 0.0 |
|  | 99¢ | 5,122 | ×0.2^26 = 0.0 |
| | | **Σ** | **17.2** |

`yours 10.0 / Σ 17.2 = 58.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 58.1% = $2.42/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 23 @ 20¢ → $1.89/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 41 (23 yours) | ×0.2^0 = 41.0 |
|  | 23¢ | 726 | ×0.2^3 = 5.8 |
|  | 47¢ | 99 | ×0.2^27 = 0.0 |
|  | 50¢ | 99 | ×0.2^30 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^77 = 0.0 |
| | | **Σ** | **46.8** |

`yours 23.0 / Σ 46.8 = 49.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 49.1% = $1.89/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 30 @ 12¢ → $5.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 66 (30 yours) | ×0.1^0 = 66.0 |
|  | 5¢ | 99 | ×0.1^7 = 0.0 |
|  | 4¢ | 22 | ×0.1^8 = 0.0 |
|  | 3¢ | 100 | ×0.1^9 = 0.0 |
|  | 1¢ | 35,326 | ×0.1^11 = 0.0 |
| | | **Σ** | **66.0** |

`yours 30.0 / Σ 66.0 = 45.5%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 45.5% = $5.68/day`  

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 10 @ 25¢ → $5.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 23 (10 yours) | ×0.25^0 = 23.0 |
|  | 34¢ | 99 | ×0.25^9 = 0.0 |
|  | 50¢ | 19 | ×0.25^25 = 0.0 |
|  | 99¢ | 10,872 | ×0.25^74 = 0.0 |
| | | **Σ** | **23.0** |

`yours 10.0 / Σ 23.0 = 43.5%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 43.5% = $5.43/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 5 @ 71¢ → $1.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 71¢ | 8 (5 yours) | ×0.2^0 = 8.0 |
|  | 69¢ | 90 | ×0.2^2 = 3.6 |
|  | 67¢ | 0 | ×0.2^4 = 0.0 |
|  | 64¢ | 0 | ×0.2^7 = 0.0 |
|  | 63¢ | 0 | ×0.2^8 = 0.0 |
|  | 62¢ | 0 | ×0.2^9 = 0.0 |
|  | 61¢ | 0 | ×0.2^10 = 0.0 |
|  | 60¢ | 0 | ×0.2^11 = 0.0 |
|  | 57¢ | 0 | ×0.2^14 = 0.0 |
|  | 2¢ | 50,000 | ×0.2^69 = 0.0 |
| | | **Σ** | **11.6** |

`yours 5.0 / Σ 11.6 = 43.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 43.1% = $1.80/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 7 @ 18¢ → $1.63/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 7 (7 yours) | ×0.2^0 = 7.5 |
|  | 17¢ | 38 | ×0.2^1 = 7.6 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **17.7** |

`yours 7.5 / Σ 17.7 = 42.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 42.3% = $1.63/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 7 @ 25¢ → $1.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 17 (7 yours) | ×0.2^0 = 17.0 |
|  | 24¢ | 0 | ×0.2^1 = 0.0 |
|  | 22¢ | 7 | ×0.2^3 = 0.1 |
|  | 17¢ | 0 | ×0.2^8 = 0.0 |
|  | 8¢ | 100 | ×0.2^17 = 0.0 |
|  | 7¢ | 81 | ×0.2^18 = 0.0 |
|  | 3¢ | 5,247 | ×0.2^22 = 0.0 |
| | | **Σ** | **17.1** |

`yours 7.0 / Σ 17.1 = 41.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 41.0% = $1.71/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 5 @ 28¢ → $1.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 11 (5 yours) | ×0.2^0 = 11.0 |
|  | 29¢ | 10 | ×0.2^1 = 2.0 |
|  | 50¢ | 100 | ×0.2^22 = 0.0 |
|  | 97¢ | 58,826 | ×0.2^69 = 0.0 |
| | | **Σ** | **13.0** |

`yours 5.0 / Σ 13.0 = 38.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.5% = $1.48/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 5 @ 26¢ → $1.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 16 (5 yours) | ×0.2^0 = 15.6 |
|  | 50¢ | 125 | ×0.2^24 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^71 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 75¢ → $1.34/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 31 (10 yours) | ×0.2^0 = 31.0 |
|  | 71¢ | 100 | ×0.2^4 = 0.2 |
|  | 2¢ | 80,250 | ×0.2^73 = 0.0 |
| | | **Σ** | **31.2** |

`yours 10.0 / Σ 31.2 = 32.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 32.1% = $1.34/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 5 @ 25¢ → $1.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 16 (5 yours) | ×0.2^0 = 16.0 |
|  | 22¢ | 10 | ×0.2^3 = 0.1 |
|  | 16¢ | 200 | ×0.2^9 = 0.0 |
|  | 2¢ | 100,250 | ×0.2^23 = 0.0 |
| | | **Σ** | **16.1** |

`yours 5.0 / Σ 16.1 = 31.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.1% = $1.20/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 5 @ 52¢ → $1.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 52¢ | 15 (5 yours) | ×0.2^0 = 15.0 |
|  | 51¢ | 20 | ×0.2^1 = 4.0 |
|  | 48¢ | 11 | ×0.2^4 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^50 = 0.0 |
| | | **Σ** | **19.0** |

`yours 5.0 / Σ 19.0 = 26.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 26.3% = $1.10/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 20 @ 17¢ → $0.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 7 | ×0.2^0 = 7.5 |
| ▶ | 17¢ | 38 (20 yours) | ×0.2^1 = 7.6 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **17.7** |

`yours 4.0 / Σ 17.7 = 22.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 22.6% = $0.87/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> SELL 10 @ 75¢ → $0.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 48 (10 yours) | ×0.2^0 = 48.0 |
|  | 95¢ | 100 | ×0.2^20 = 0.0 |
|  | 99¢ | 8,991 | ×0.2^24 = 0.0 |
| | | **Σ** | **48.0** |

`yours 10.0 / Σ 48.0 = 20.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 20.8% = $0.87/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 5 @ 11¢ → $0.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.2^0 = 1.5 |
| ▶ | 11¢ | 15 (5 yours) | ×0.2^1 = 3.0 |
|  | 12¢ | 10 | ×0.2^2 = 0.4 |
|  | 15¢ | 5 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^87 = 0.0 |
| | | **Σ** | **4.9** |

`yours 1.0 / Σ 4.9 = 20.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.2% = $0.78/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 8¢ → $0.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 9¢ | 219 | ×0.2^1 = 43.8 |
|  | 10¢ | 1 | ×0.2^2 = 0.0 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^89 = 0.0 |
| | | **Σ** | **58.8** |

`yours 10.0 / Σ 58.8 = 17.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.0% = $0.65/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 1 @ 43¢ → $0.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 6 (1 yours) | ×0.2^0 = 6.0 |
|  | 18¢ | 100 | ×0.2^25 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^41 = 0.0 |
| | | **Σ** | **6.0** |

`yours 1.0 / Σ 6.0 = 16.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 16.7% = $0.69/day`  

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
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (220,983 resting) | ~32.7% | ~$24.52 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (326,626 resting) | ~23.6% | ~$17.68 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,505 resting) | ~63.9% | ~$15.97 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,589 resting) | ~60.6% | ~$15.15 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (61,926 resting) | ~12.2% | ~$9.15 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,626 resting) | ~33.1% | ~$8.28 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (81,584 resting) | ~31.6% | ~$7.89 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (40,564 resting) | ~29.4% | ~$7.34 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,208 resting) | ~18.0% | ~$4.49 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (189,186 resting) | ~4.8% | ~$3.64 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (69,280 resting) | ~3.7% | ~$2.79 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (67,292 resting) | ~40.4% | ~$2.53 |

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
| 2026-08-09 10:55 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 10:34 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 10:02 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 9:18 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 7:48 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 6:55 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 5:59 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 5:05 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 3:26 AM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 2:01 AM ET | ✅ ok | 1749 | $1772.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
