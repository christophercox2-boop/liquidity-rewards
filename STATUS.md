# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-01 9:53 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$32.91/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `cranc-uspres28-12-31-2026-jdvan` — BUY at the best price, ~$1.49/day for 200 contracts. Runners-up: `cranc-uspres28-12-31-2026-erikir` (~$1.46/day), `cranc-uspres28-12-31-2026-hunbid` (~$1.46/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$32.91/day (~$1.37/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-48` | BUY | 11.0¢ | 64 | 0 | $100.00 | ✅ scoring — ~99.9% of bid side (5,105 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 32.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~91.5% of ask side (12,210 resting ≥ 5,000 ✓) ≈ $3.52/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~68.4% of ask side (12,072 resting ≥ 5,000 ✓) ≈ $2.63/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 32.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~68.3% of ask side (12,024 resting ≥ 5,000 ✓) ≈ $2.63/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 6.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~62.5% of ask side (11,871 resting ≥ 5,000 ✓) ≈ $2.40/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~53.8% of ask side (12,005 resting ≥ 5,000 ✓) ≈ $2.07/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-tedcru` | SELL | 21.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~53.6% of ask side (5,897 resting ≥ 5,000 ✓) ≈ $0.81/day (pool ÷ 33 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 40.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~40.3% of ask side (9,202 resting ≥ 5,000 ✓) ≈ $1.68/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 15.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~37.7% of ask side (11,962 resting ≥ 5,000 ✓) ≈ $1.45/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~37.0% of ask side (11,862 resting ≥ 5,000 ✓) ≈ $1.42/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~31.8% of ask side (12,055 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 5.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~31.6% of ask side (12,024 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~31.1% of ask side (12,072 resting ≥ 5,000 ✓) ≈ $1.20/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~29.8% of ask side (12,379 resting ≥ 5,000 ✓) ≈ $1.15/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 22.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~23.3% of bid side (5,643 resting ≥ 5,000 ✓) ≈ $0.89/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 15.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~18.1% of ask side (12,102 resting ≥ 5,000 ✓) ≈ $0.70/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 16.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~17.2% of ask side (11,913 resting ≥ 5,000 ✓) ≈ $0.66/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 90.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~14.9% of bid side (5,526 resting ≥ 5,000 ✓) ≈ $0.62/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | SELL | 76.0¢ | 49 | 0 | $100.00 | ✅ scoring — ~9.2% of ask side (5,929 resting ≥ 5,000 ✓) ≈ $0.39/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~8.4% of bid side (12,103 resting ≥ 5,000 ✓) ≈ $0.32/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 24.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~8.3% of ask side (8,353 resting ≥ 5,000 ✓) ≈ $0.35/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 78.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~7.1% of bid side (5,534 resting ≥ 5,000 ✓) ≈ $0.30/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~6.2% of bid side (8,301 resting ≥ 5,000 ✓) ≈ $0.24/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 74.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~5.9% of bid side (5,428 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | BUY | 2.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~5.2% of bid side (19,442 resting ≥ 5,000 ✓) ≈ $0.20/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 42.0¢ | 53 | 2 | $100.00 | ✅ scoring — ~4.3% of ask side (9,202 resting ≥ 5,000 ✓) ≈ $0.18/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | BUY | 3.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~2.6% of bid side (25,218 resting ≥ 5,000 ✓) ≈ $0.10/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 20.0¢ | 11 | 1 | $100.00 | ✅ scoring — ~2.1% of bid side (5,591 resting ≥ 5,000 ✓) ≈ $0.09/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 20.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~1.9% of bid side (5,591 resting ≥ 5,000 ✓) ≈ $0.08/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 8.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~1.0% of ask side (11,973 resting ≥ 5,000 ✓) ≈ $0.04/day (pool ÷ 13 markets) |
| …and 26 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 64 @ 11¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 64 (64 yours) | ×0.2^0 = 63.8 |
|  | 6¢ | 104 | ×0.2^5 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 43 @ 32¢ → $3.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 47 (43 yours) | ×0.2^0 = 47.0 |
|  | 38¢ | 128 | ×0.2^6 = 0.0 |
|  | 46¢ | 37 | ×0.2^14 = 0.0 |
|  | 50¢ | 100 | ×0.2^18 = 0.0 |
|  | 98¢ | 1,897 | ×0.2^66 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^67 = 0.0 |
| | | **Σ** | **47.0** |

`yours 43.0 / Σ 47.0 = 91.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 91.5% = $3.52/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 22 @ 20¢ → $2.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 32 (22 yours) | ×0.2^0 = 32.0 |
|  | 24¢ | 100 | ×0.2^4 = 0.2 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,839 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **32.2** |

`yours 22.0 / Σ 32.2 = 68.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.4% = $2.63/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 10 @ 32¢ → $2.63/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 31¢ | 1 | ×0.2^0 = 0.9 |
| ▶ | 32¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 35¢ | 5 | ×0.2^4 = 0.0 |
|  | 40¢ | 105 | ×0.2^9 = 0.0 |
|  | 50¢ | 100 | ×0.2^19 = 0.0 |
|  | 98¢ | 1,802 | ×0.2^67 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^68 = 0.0 |
| | | **Σ** | **2.9** |

`yours 2.0 / Σ 2.9 = 68.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 68.3% = $2.63/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 10 @ 6¢ → $2.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 16 (10 yours) | ×0.2^0 = 16.0 |
|  | 13¢ | 19 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 98¢ | 1,735 | ×0.2^92 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^93 = 0.0 |
| | | **Σ** | **16.0** |

`yours 10.0 / Σ 16.0 = 62.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 62.5% = $2.40/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 50 @ 15¢ → $2.07/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 81 (50 yours) | ×0.2^0 = 81.0 |
|  | 16¢ | 60 | ×0.2^1 = 12.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **93.0** |

`yours 50.0 / Σ 93.0 = 53.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 53.8% = $2.07/day`  

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
<details><summary><code>cranc-uspres28-12-31-2026-tedcru</code> SELL 0 @ 21¢ → $0.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (0 yours) | ×0.2^0 = 0.7 |
|  | 24¢ | 2 | ×0.2^3 = 0.0 |
|  | 28¢ | 918 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^29 = 0.0 |
|  | 77¢ | 2 | ×0.2^56 = 0.0 |
|  | 78¢ | 2 | ×0.2^57 = 0.0 |
|  | 99¢ | 4,947 | ×0.2^78 = 0.0 |
| | | **Σ** | **0.7** |

`yours 0.4 / Σ 0.7 = 53.6%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 53.6% = $0.81/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 20 @ 40¢ → $1.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 40¢ | 44 (20 yours) | ×0.2^0 = 44.0 |
|  | 42¢ | 140 | ×0.2^2 = 5.6 |
|  | 52¢ | 1 | ×0.2^12 = 0.0 |
|  | 54¢ | 11 | ×0.2^14 = 0.0 |
|  | 69¢ | 100 | ×0.2^29 = 0.0 |
|  | 99¢ | 8,906 | ×0.2^59 = 0.0 |
| | | **Σ** | **49.6** |

`yours 20.0 / Σ 49.6 = 40.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 40.3% = $1.68/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 40 @ 15¢ → $1.45/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 106 (40 yours) | ×0.2^0 = 106.0 |
|  | 18¢ | 4 | ×0.2^3 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,751 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **106.0** |

`yours 40.0 / Σ 106.0 = 37.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.7% = $1.45/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 10 @ 10¢ → $1.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 27 (10 yours) | ×0.2^0 = 27.0 |
|  | 16¢ | 3 | ×0.2^6 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,731 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **27.0** |

`yours 10.0 / Σ 27.0 = 37.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.0% = $1.42/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 50 @ 21¢ → $1.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 157 (50 yours) | ×0.2^0 = 157.0 |
|  | 26¢ | 20 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,777 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **157.0** |

`yours 50.0 / Σ 157.0 = 31.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.8% = $1.22/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 50 @ 5¢ → $1.22/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 158 (50 yours) | ×0.2^0 = 158.2 |
|  | 50¢ | 100 | ×0.2^45 = 0.0 |
|  | 98¢ | 1,765 | ×0.2^93 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^94 = 0.0 |
| | | **Σ** | **158.2** |

`yours 50.0 / Σ 158.2 = 31.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.6% = $1.22/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 10 @ 20¢ → $1.20/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 32 (10 yours) | ×0.2^0 = 32.0 |
|  | 24¢ | 100 | ×0.2^4 = 0.2 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 98¢ | 1,839 | ×0.2^78 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^79 = 0.0 |
| | | **Σ** | **32.2** |

`yours 10.0 / Σ 32.2 = 31.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.1% = $1.20/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 10¢ → $1.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 137 (50 yours) | ×0.2^0 = 137.2 |
|  | 11¢ | 152 | ×0.2^1 = 30.4 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **167.6** |

`yours 50.0 / Σ 167.6 = 29.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.8% = $1.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 100 @ 22¢ → $0.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 430 (100 yours) | ×0.2^0 = 430.0 |
|  | 1¢ | 5,213 | ×0.2^21 = 0.0 |
| | | **Σ** | **430.0** |

`yours 100.0 / Σ 430.0 = 23.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 23.3% = $0.89/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 16¢ → $0.66/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 58 (10 yours) | ×0.2^0 = 58.2 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^82 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^83 = 0.0 |
| | | **Σ** | **58.2** |

`yours 10.0 / Σ 58.2 = 17.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.2% = $0.66/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 10 @ 90¢ → $0.62/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 67 (10 yours) | ×0.2^0 = 67.1 |
|  | 1¢ | 5,459 | ×0.2^89 = 0.0 |
| | | **Σ** | **67.1** |

`yours 10.0 / Σ 67.1 = 14.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 14.9% = $0.62/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> SELL 49 @ 76¢ → $0.39/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 76¢ | 530 (49 yours) | ×0.2^0 = 530.0 |
|  | 98¢ | 127 | ×0.2^22 = 0.0 |
|  | 99¢ | 5,272 | ×0.2^23 = 0.0 |
| | | **Σ** | **530.0** |

`yours 49.0 / Σ 530.0 = 9.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 9.2% = $0.39/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> BUY 1,000 @ 2¢ → $0.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 11,901 (1,000 yours) | ×0.2^0 = 11,901.0 |
| | | **Σ** | **11,901.0** |

`yours 1,000.0 / Σ 11,901.0 = 8.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 8.4% = $0.32/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 24¢ → $0.35/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 23¢ | 22 | ×0.2^0 = 22.0 |
| ▶ | 24¢ | 10 (10 yours) | ×0.2^1 = 2.0 |
|  | 94¢ | 24 | ×0.2^71 = 0.0 |
|  | 99¢ | 8,297 | ×0.2^76 = 0.0 |
| | | **Σ** | **24.0** |

`yours 2.0 / Σ 24.0 = 8.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 8.3% = $0.35/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 30 @ 78¢ → $0.30/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 422 (30 yours) | ×0.2^0 = 421.9 |
|  | 1¢ | 5,112 | ×0.2^77 = 0.0 |
| | | **Σ** | **421.9** |

`yours 30.0 / Σ 421.9 = 7.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.1% = $0.30/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 8,101 (500 yours) | ×0.2^0 = 8,101.0 |
| | | **Σ** | **8,101.0** |

`yours 500.0 / Σ 8,101.0 = 6.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 6.2% = $0.24/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 40 @ 74¢ → $0.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 674 (40 yours) | ×0.2^0 = 674.0 |
|  | 1¢ | 4,754 | ×0.2^73 = 0.0 |
| | | **Σ** | **674.0** |

`yours 40.0 / Σ 674.0 = 5.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.9% = $0.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> BUY 1,000 @ 2¢ → $0.20/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 19,242 (1,000 yours) | ×0.2^0 = 19,242.0 |
| | | **Σ** | **19,242.0** |

`yours 1,000.0 / Σ 19,242.0 = 5.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.2% = $0.20/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 53 @ 42¢ → $0.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 40¢ | 44 | ×0.2^0 = 44.0 |
| ▶ | 42¢ | 140 (53 yours) | ×0.2^2 = 5.6 |
|  | 52¢ | 1 | ×0.2^12 = 0.0 |
|  | 54¢ | 11 | ×0.2^14 = 0.0 |
|  | 69¢ | 100 | ×0.2^29 = 0.0 |
|  | 99¢ | 8,906 | ×0.2^59 = 0.0 |
| | | **Σ** | **49.6** |

`yours 2.1 / Σ 49.6 = 4.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.3% = $0.18/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> BUY 40 @ 3¢ → $0.10/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 537 (40 yours) | ×0.2^0 = 537.0 |
|  | 1¢ | 24,681 | ×0.2^2 = 987.2 |
| | | **Σ** | **1,524.2** |

`yours 40.0 / Σ 1,524.2 = 2.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 2.6% = $0.10/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 11 @ 20¢ → $0.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 100 | ×0.2^0 = 99.7 |
| ▶ | 20¢ | 21 (11 yours) | ×0.2^1 = 4.2 |
|  | 1¢ | 5,470 | ×0.2^20 = 0.0 |
| | | **Σ** | **103.9** |

`yours 2.2 / Σ 103.9 = 2.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 2.1% = $0.09/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 10 @ 20¢ → $0.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 21¢ | 100 | ×0.2^0 = 99.7 |
| ▶ | 20¢ | 21 (10 yours) | ×0.2^1 = 4.2 |
|  | 1¢ | 5,470 | ×0.2^20 = 0.0 |
| | | **Σ** | **103.9** |

`yours 2.0 / Σ 103.9 = 1.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 1.9% = $0.08/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 1 @ 8¢ → $0.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 99 (1 yours) | ×0.2^0 = 99.3 |
|  | 50¢ | 100 | ×0.2^42 = 0.0 |
|  | 98¢ | 1,773 | ×0.2^90 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^91 = 0.0 |
| | | **Σ** | **99.3** |

`yours 1.0 / Σ 99.3 = 1.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.0% = $0.04/day`  

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
| `cranc-uspres28-12-31-2026-jdvan` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (75,739 resting) | ~98.5% | ~$1.49 |
| `cranc-uspres28-12-31-2026-erikir` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,443 resting) | ~96.2% | ~$1.46 |
| `cranc-uspres28-12-31-2026-hunbid` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,623 resting) | ~96.2% | ~$1.46 |
| `cranc-uspres28-12-31-2026-elomus` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (12,108 resting) | ~76.6% | ~$1.16 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (6,226 resting) | ~69.0% | ~$1.04 |
| `cranc-uspres28-12-31-2026-kamhar` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (9,120 resting) | ~66.4% | ~$1.01 |
| `cranc-uspres28-12-31-2026-tuccar` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,406 resting) | ~66.4% | ~$1.01 |
| `cranc-uspres28-12-31-2026-gavnew` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (83,460 resting) | ~64.0% | ~$0.97 |
| `cranc-uspres28-12-31-2026-margre` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (8,774 resting) | ~57.3% | ~$0.87 |
| `cranc-uspres28-12-31-2026-bersan` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (5,564 resting) | ~35.7% | ~$0.54 |
| `cranc-uspres28-12-31-2026-aleoca` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (50,884 resting) | ~31.9% | ~$0.48 |
| `cranc-uspres28-12-31-2026-steban` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,866 resting) | ~23.7% | ~$0.36 |

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
| 2026-08-01 9:53 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 8:15 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 7:23 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 7:14 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 6:13 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 5:12 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 3:38 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 1:34 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 1:25 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 12:24 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
