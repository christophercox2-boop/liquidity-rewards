# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-13 7:29 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$105.46/day estimated (ceiling, not promise — details below)

**Earned:** $2,853.72 lifetime ($1,888.03 paid). Last three recorded days — 2026-08-11: **$406.66** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-10: **$557.62** · 2026-08-09: **$62.24** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — BUY at the best price, ~$13.38/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-dem` (~$10.86/day), `ewc-usgub-ga-2026-11-03-rep` (~$10.17/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$105.46/day (~$4.39/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `apdc-jerpowgov-2026-12-31` | SELL | 24.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~91.6% of ask side (9,075 resting ≥ 5,000 ✓) ≈ $22.89/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~90.8% of bid side (300,564 resting ≥ 5,000 ✓) ≈ $3.49/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 12.0¢ | 18 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (300,458 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | BUY | 8.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~59.5% of bid side (140,435 resting ≥ 5,000 ✓) ≈ $2.29/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 22.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~50.0% of bid side (200,694 resting ≥ 5,000 ✓) ≈ $1.92/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 22.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~49.8% of bid side (5,571 resting ≥ 5,000 ✓) ≈ $12.45/day (pool ÷ 2 markets) |
| `tec-cbb-champ-2027-04-05-w-wisc` | BUY | 1.0¢ | 5,000 | 0 | $500.00 | ✅ scoring — ~47.2% of bid side (10,594 resting ≥ 2,500 ✓) ≈ $1.62/day (pool ÷ 73 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | BUY | 11.0¢ | 40 | 1 | $25.00 | ✅ scoring — ~45.9% of bid side (10,584 resting ≥ 2,000 ✓) ≈ $2.87/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ar-2026-11-03-rep` | SELL | 96.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~35.1% of ask side (13,009 resting ≥ 2,000 ✓) ≈ $2.20/day (pool ÷ 2 markets) |
| `usgubewc-usgub-wy-2026-11-03-rep` | BUY | 83.0¢ | 50 | 1 | $25.00 | ✅ scoring — ~30.3% of bid side (12,176 resting ≥ 2,000 ✓) ≈ $1.89/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ny-2026-11-03-dem` | BUY | 90.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~28.6% of bid side (512,735 resting ≥ 2,000 ✓) ≈ $1.78/day (pool ÷ 2 markets) |
| `tec-cbb-champ-2027-04-05-w-stmry` | BUY | 1.0¢ | 5,000 | 0 | $500.00 | ✅ scoring — ~27.9% of bid side (17,901 resting ≥ 2,500 ✓) ≈ $0.96/day (pool ÷ 73 markets) |
| `pandc-anydis-2027-12-31` | SELL | 25.0¢ | 18 | 0 | $50.00 | ✅ scoring — ~27.9% of ask side (11,048 resting ≥ 10,000 ✓) ≈ $3.48/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-dem` | BUY | 1.0¢ | 5,000 | 0 | $25.00 | ✅ scoring — ~26.9% of bid side (18,602 resting ≥ 2,000 ✓) ≈ $1.68/day (pool ÷ 2 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 8.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~26.8% of bid side (20,744 resting ≥ 2,000 ✓) ≈ $3.35/day |
| `ussewc-usse-nm-2026-11-03-rep` | BUY | 1.0¢ | 4,971 | 0 | $25.00 | ✅ scoring — ~18.1% of bid side (27,507 resting ≥ 2,000 ✓) ≈ $1.13/day (pool ÷ 2 markets) |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | BUY | 3.0¢ | 2,000 | 6 | $250.00 | ✅ scoring — ~14.4% of bid side (13,507 resting ≥ 5,000 ✓) ≈ $17.99/day |
| `vsc-usgubp-fl-fshbck-atl-30pct` | BUY | 1.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~13.9% of bid side (36,025 resting ≥ 5,000 ✓) ≈ $0.69/day (pool ÷ 10 markets) |
| `usgubewc-usgub-id-2026-11-03-rep` | SELL | 97.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~13.3% of ask side (22,647 resting ≥ 2,000 ✓) ≈ $0.83/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 4.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~12.1% of ask side (131,055 resting ≥ 2,000 ✓) ≈ $0.76/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 2 | 2 | $100.00 | ✅ scoring — ~11.0% of bid side (50,580 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 44.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~10.9% of ask side (82,344 resting ≥ 5,000 ✓) ≈ $0.45/day (pool ÷ 12 markets) |
| `ussewc-usse-or-2026-11-03-rep` | BUY | 1.0¢ | 1,300 | 0 | $25.00 | ✅ scoring — ~10.0% of bid side (12,950 resting ≥ 2,000 ✓) ≈ $0.63/day (pool ÷ 2 markets) |
| `ussewc-usse-ma-2026-11-03-rep` | BUY | 1.0¢ | 1,237 | 0 | $25.00 | ✅ scoring — ~9.6% of bid side (12,937 resting ≥ 2,000 ✓) ≈ $0.60/day (pool ÷ 2 markets) |
| `ussewc-usse-il-2026-11-03-dem` | BUY | 95.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~8.4% of bid side (500,678 resting ≥ 2,000 ✓) ≈ $0.52/day (pool ÷ 2 markets) |
| `pntcbk-wnba-white-2027-06-30-roywhi` | BUY | 3.0¢ | 1,500 | 1 | $250.00 | ✅ scoring — ~7.8% of bid side (21,151 resting ≥ 5,000 ✓) ≈ $9.73/day |
| `usgubewc-usgub-ct-2026-11-03-dem` | SELL | 96.0¢ | 35 | 0 | $25.00 | ✅ scoring — ~7.7% of ask side (18,627 resting ≥ 2,000 ✓) ≈ $0.48/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 3.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~7.2% of ask side (66,030 resting ≥ 2,000 ✓) ≈ $0.45/day (pool ÷ 2 markets) |
| `ussewc-usse-wv-2026-11-03-dem` | BUY | 1.0¢ | 1,400 | 0 | $25.00 | ✅ scoring — ~6.5% of bid side (21,615 resting ≥ 2,000 ✓) ≈ $0.40/day (pool ÷ 2 markets) |
| `usgubewc-usgub-ct-2026-11-03-dem` | BUY | 95.0¢ | 5 | 0 | $25.00 | ✅ scoring — ~5.8% of bid side (510,288 resting ≥ 2,000 ✓) ≈ $0.36/day (pool ÷ 2 markets) |
| …and 167 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 10 @ 24¢ → $22.89/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 26¢ | 23 | ×0.2^2 = 0.9 |
|  | 32¢ | 168 | ×0.2^8 = 0.0 |
|  | 38¢ | 80 | ×0.2^14 = 0.0 |
|  | 99¢ | 8,794 | ×0.2^75 = 0.0 |
| | | **Σ** | **10.9** |

`yours 10.0 / Σ 10.9 = 91.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 91.6% = $22.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 8 @ 9¢ → $3.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 8 (8 yours) | ×0.2^0 = 7.8 |
|  | 1¢ | 300,556 | ×0.2^8 = 0.8 |
| | | **Σ** | **8.5** |

`yours 7.8 / Σ 8.5 = 90.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 90.8% = $3.49/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 18 @ 12¢ → $2.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 27 (18 yours) | ×0.2^0 = 27.0 |
|  | 1¢ | 300,431 | ×0.2^11 = 0.0 |
| | | **Σ** | **27.0** |

`yours 18.0 / Σ 27.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> BUY 10 @ 8¢ → $2.29/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 1¢ | 140,420 | ×0.2^7 = 1.8 |
| | | **Σ** | **16.8** |

`yours 10.0 / Σ 16.8 = 59.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 59.5% = $2.29/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 40 @ 22¢ → $1.92/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 40 (40 yours) | ×0.2^0 = 40.0 |
|  | 21¢ | 200 | ×0.2^1 = 40.0 |
|  | 10¢ | 45 | ×0.2^12 = 0.0 |
|  | 1¢ | 200,409 | ×0.2^21 = 0.0 |
| | | **Σ** | **80.0** |

`yours 40.0 / Σ 80.0 = 50.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 50.0% = $1.92/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 20 @ 22¢ → $12.45/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 4 | ×0.2^0 = 4.0 |
| ▶ | 22¢ | 20 (20 yours) | ×0.2^1 = 4.0 |
|  | 20¢ | 1 | ×0.2^3 = 0.0 |
|  | 18¢ | 66 | ×0.2^5 = 0.0 |
|  | 14¢ | 6 | ×0.2^9 = 0.0 |
|  | 2¢ | 100 | ×0.2^21 = 0.0 |
|  | 1¢ | 5,374 | ×0.2^22 = 0.0 |
| | | **Σ** | **8.0** |

`yours 4.0 / Σ 8.0 = 49.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 49.8% = $12.45/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>tec-cbb-champ-2027-04-05-w-wisc</code> BUY 5,000 @ 1¢ → $1.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 10,594 (5,000 yours) | ×0.35^0 = 10,594.2 |
| | | **Σ** | **10,594.2** |

`yours 5,000.0 / Σ 10,594.2 = 47.2%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 47.2% = $1.62/day`  

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
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> BUY 40 @ 11¢ → $2.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 4 | ×0.1^0 = 4.0 |
| ▶ | 11¢ | 40 (40 yours) | ×0.1^1 = 4.0 |
|  | 10¢ | 41 | ×0.1^2 = 0.4 |
|  | 9¢ | 299 | ×0.1^3 = 0.3 |
|  | 1¢ | 10,200 | ×0.1^11 = 0.0 |
| | | **Σ** | **8.7** |

`yours 4.0 / Σ 8.7 = 45.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 45.9% = $2.87/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ar-2026-11-03-rep</code> SELL 40 @ 96¢ → $2.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 97 (40 yours) | ×0.1^0 = 97.0 |
|  | 97¢ | 40 | ×0.1^1 = 4.0 |
|  | 99¢ | 12,872 | ×0.1^3 = 12.9 |
| | | **Σ** | **113.9** |

`yours 40.0 / Σ 113.9 = 35.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 35.1% = $2.20/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ar-2026-11-03-dem`
2. `usgubewc-usgub-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-wy-2026-11-03-rep</code> BUY 50 @ 83¢ → $1.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 84¢ | 10 | ×0.1^0 = 10.0 |
| ▶ | 83¢ | 50 (50 yours) | ×0.1^1 = 5.0 |
|  | 82¢ | 150 | ×0.1^2 = 1.5 |
|  | 8¢ | 16 | ×0.1^76 = 0.0 |
|  | 1¢ | 11,950 | ×0.1^83 = 0.0 |
| | | **Σ** | **16.5** |

`yours 5.0 / Σ 16.5 = 30.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 30.3% = $1.89/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-wy-2026-11-03-dem`
2. `usgubewc-usgub-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>usgubewc-usgub-ny-2026-11-03-dem</code> BUY 10 @ 90¢ → $1.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 35 (10 yours) | ×0.1^0 = 35.0 |
|  | 86¢ | 200 | ×0.1^4 = 0.0 |
|  | 84¢ | 2,000 | ×0.1^6 = 0.0 |
| | | **Σ** | **35.0** |

`yours 10.0 / Σ 35.0 = 28.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 28.6% = $1.78/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ny-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ny-2026-11-03-rep`

</details>

</details>
<details><summary><code>tec-cbb-champ-2027-04-05-w-stmry</code> BUY 5,000 @ 1¢ → $0.96/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 17,901 (5,000 yours) | ×0.35^0 = 17,901.0 |
| | | **Σ** | **17,901.0** |

`yours 5,000.0 / Σ 17,901.0 = 27.9%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 27.9% = $0.96/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 18 @ 25¢ → $3.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 65 (18 yours) | ×0.25^0 = 65.2 |
|  | 33¢ | 100 | ×0.25^8 = 0.0 |
|  | 50¢ | 25 | ×0.25^25 = 0.0 |
|  | 99¢ | 10,857 | ×0.25^74 = 0.0 |
| | | **Σ** | **65.2** |

`yours 18.2 / Σ 65.2 = 27.9%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 27.9% = $3.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-dem</code> BUY 5,000 @ 1¢ → $1.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 18,602 (5,000 yours) | ×0.1^0 = 18,602.0 |
| | | **Σ** | **18,602.0** |

`yours 5,000.0 / Σ 18,602.0 = 26.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 26.9% = $1.68/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem` ← this one
2. `ussewc-usse-wy-2026-11-03-rep`

</details>

</details>
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 10 @ 8¢ → $3.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 36 (10 yours) | ×0.1^0 = 35.8 |
|  | 6¢ | 153 | ×0.1^2 = 1.5 |
|  | 3¢ | 80 | ×0.1^5 = 0.0 |
|  | 2¢ | 10,250 | ×0.1^6 = 0.0 |
| | | **Σ** | **37.3** |

`yours 10.0 / Σ 37.3 = 26.8%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 26.8% = $3.35/day`  

</details>
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> BUY 4,971 @ 1¢ → $1.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 27,507 (4,971 yours) | ×0.1^0 = 27,507.0 |
| | | **Σ** | **27,507.0** |

`yours 4,971.0 / Σ 27,507.0 = 18.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 18.1% = $1.13/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>pntcbk-wnba-freedom-2027-06-30-enekan</code> BUY 2,000 @ 3¢ → $17.99/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 376 | ×0.9^0 = 376.0 |
|  | 8¢ | 50 | ×0.9^1 = 45.0 |
|  | 7¢ | 51 | ×0.9^2 = 41.3 |
|  | 6¢ | 30 | ×0.9^3 = 21.9 |
|  | 5¢ | 800 | ×0.9^4 = 524.9 |
| ▶ | 3¢ | 12,000 (2,000 yours) | ×0.9^6 = 6,377.3 |
| | | **Σ** | **7,386.4** |

`yours 1,062.9 / Σ 7,386.4 = 14.4%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 14.4% = $17.99/day`  

</details>
<details><summary><code>vsc-usgubp-fl-fshbck-atl-30pct</code> BUY 5,000 @ 1¢ → $0.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 36,025 (5,000 yours) | ×0.2^0 = 36,025.0 |
| | | **Σ** | **36,025.0** |

`yours 5,000.0 / Σ 36,025.0 = 13.9%`  
`$100 ÷ 10 ÷ 2 = $5.00 × 13.9% = $0.69/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vsc-usgubp-fl-fshbck-atl-11pct`
2. `vsc-usgubp-fl-fshbck-atl-13pct`
3. `vsc-usgubp-fl-fshbck-atl-15pct`
4. `vsc-usgubp-fl-fshbck-atl-17pct`
5. `vsc-usgubp-fl-fshbck-atl-19pct`
6. `vsc-usgubp-fl-fshbck-atl-21pct`
7. `vsc-usgubp-fl-fshbck-atl-30pct` ← this one
8. `vsc-usgubp-fl-fshbck-atl-5pct`
9. `vsc-usgubp-fl-fshbck-atl-7pct`
10. `vsc-usgubp-fl-fshbck-atl-9pct`

</details>

</details>
<details><summary><code>usgubewc-usgub-id-2026-11-03-rep</code> SELL 40 @ 97¢ → $0.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 97¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 98¢ | 105 | ×0.1^1 = 10.5 |
|  | 99¢ | 22,477 | ×0.1^2 = 224.8 |
| | | **Σ** | **300.3** |

`yours 40.0 / Σ 300.3 = 13.3%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 13.3% = $0.83/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-id-2026-11-03-dem`
2. `usgubewc-usgub-id-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 4¢ → $0.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 330 (40 yours) | ×0.1^0 = 330.0 |
|  | 98¢ | 130,500 | ×0.1^94 = 0.0 |
| | | **Σ** | **330.0** |

`yours 40.0 / Σ 330.0 = 12.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 12.1% = $0.76/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 2 @ 15¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 15¢ | 18 (2 yours) | ×0.2^2 = 0.7 |
|  | 7¢ | 112 | ×0.2^10 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^15 = 0.0 |
| | | **Σ** | **0.7** |

`yours 0.1 / Σ 0.7 = 11.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.0% = $0.42/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 8 @ 44¢ → $0.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 44¢ | 73 (8 yours) | ×0.2^0 = 73.0 |
|  | 98¢ | 80,046 | ×0.2^54 = 0.0 |
| | | **Σ** | **73.0** |

`yours 8.0 / Σ 73.0 = 10.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 10.9% = $0.45/day`  

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
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> BUY 1,300 @ 1¢ → $0.63/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,950 (1,300 yours) | ×0.1^0 = 12,950.0 |
| | | **Σ** | **12,950.0** |

`yours 1,300.0 / Σ 12,950.0 = 10.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 10.0% = $0.63/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ma-2026-11-03-rep</code> BUY 1,237 @ 1¢ → $0.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 12,937 (1,237 yours) | ×0.1^0 = 12,937.0 |
| | | **Σ** | **12,937.0** |

`yours 1,237.0 / Σ 12,937.0 = 9.6%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 9.6% = $0.60/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ma-2026-11-03-dem`
2. `ussewc-usse-ma-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-il-2026-11-03-dem</code> BUY 40 @ 95¢ → $0.52/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 478 (40 yours) | ×0.1^0 = 478.0 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **478.0** |

`yours 40.0 / Σ 478.0 = 8.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 8.4% = $0.52/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-il-2026-11-03-dem` ← this one
2. `ussewc-usse-il-2026-11-03-rep`

</details>

</details>
<details><summary><code>pntcbk-wnba-white-2027-06-30-roywhi</code> BUY 1,500 @ 3¢ → $9.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 118 | ×0.9^0 = 118.2 |
| ▶ | 3¢ | 3,833 (1,500 yours) | ×0.9^1 = 3,450.0 |
|  | 2¢ | 17,000 | ×0.9^2 = 13,770.0 |
| | | **Σ** | **17,338.1** |

`yours 1,350.0 / Σ 17,338.1 = 7.8%`  
`$250 ÷ 1 ÷ 2 = $125.00 × 7.8% = $9.73/day`  

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> SELL 35 @ 96¢ → $0.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 96¢ | 435 (35 yours) | ×0.1^0 = 435.0 |
|  | 99¢ | 18,192 | ×0.1^3 = 18.2 |
| | | **Σ** | **453.2** |

`yours 35.0 / Σ 453.2 = 7.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 7.7% = $0.48/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 3¢ → $0.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 555 (40 yours) | ×0.1^0 = 555.0 |
|  | 98¢ | 65,250 | ×0.1^95 = 0.0 |
| | | **Σ** | **555.0** |

`yours 40.0 / Σ 555.0 = 7.2%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 7.2% = $0.45/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wv-2026-11-03-dem</code> BUY 1,400 @ 1¢ → $0.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 21,615 (1,400 yours) | ×0.1^0 = 21,615.0 |
| | | **Σ** | **21,615.0** |

`yours 1,400.0 / Σ 21,615.0 = 6.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 6.5% = $0.40/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wv-2026-11-03-dem` ← this one
2. `ussewc-usse-wv-2026-11-03-rep`

</details>

</details>
<details><summary><code>usgubewc-usgub-ct-2026-11-03-dem</code> BUY 5 @ 95¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 88 (5 yours) | ×0.1^0 = 88.1 |
|  | 2¢ | 500,000 | ×0.1^93 = 0.0 |
| | | **Σ** | **88.1** |

`yours 5.1 / Σ 88.1 = 5.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 5.8% = $0.36/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `usgubewc-usgub-ct-2026-11-03-dem` ← this one
2. `usgubewc-usgub-ct-2026-11-03-rep`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (48,571 resting) | ~17.8% | ~$13.38 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (63,611 resting) | ~14.5% | ~$10.86 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (64,635 resting) | ~13.6% | ~$10.17 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (27,025 resting) | ~28.3% | ~$7.07 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (27,723 resting) | ~24.7% | ~$6.18 |
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (539,546 resting) | ~7.5% | ~$5.64 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (293,833 resting) | ~7.3% | ~$5.44 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (687,908 resting) | ~4.4% | ~$3.29 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (644,986 resting) | ~4.1% | ~$3.10 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (136,996 resting) | ~11.7% | ~$2.93 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,044,942 resting) | ~3.4% | ~$2.55 |
| `enwc-usgubp-fl-2026-08-18-rep-jamfis` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (18,617 resting) | ~4.9% | ~$2.43 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,888.03 |
| Pending | $964.28 |
| Skipped | $1.41 |
| **Total earned** | **$2,853.72** |

2087 reward rows · 40 days with rewards · 480 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-11 ⚠️ multi-day pending bucket | $406.66 | `███████████████` |
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
| 2026-07-29 | $53.60 | `██` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $1,390.40 | `███████████████████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $107.37 |
| `apdc-alito-2026-12-31` | $106.43 |
| `opdc-mcconnell-resign-2026-11-02` | $70.72 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `pandc-anydis-2027-12-31` | $39.99 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.02 |
| `scc-hrep-rep-2026-11-03-gte200` | $38.44 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-13 7:29 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 7:06 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:34 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 6:06 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 5:16 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 5:07 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 3:29 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 2:11 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 1:16 PM ET | ✅ ok | 2087 | $2853.72 |
| 2026-08-13 12:12 PM ET | ✅ ok | 2087 | $2853.72 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
