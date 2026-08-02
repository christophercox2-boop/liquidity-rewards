# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-01 11:57 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$60.20/day estimated (ceiling, not promise — details below)

**Earned:** $1,374.68 lifetime ($1,373.47 paid). Last three recorded days — 2026-07-29: **$53.59** · 2026-07-28: **$79.65** · 2026-07-27: **$125.34** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-oh-2026-11-03-rep` — SELL at the best price, ~$11.09/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$10.75/day), `apdc-jerpowgov-2026-12-31` (~$7.79/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$60.20/day (~$2.51/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `scc-senate-gop-2026-11-03-48` | BUY | 11.0¢ | 64 | 0 | $100.00 | ✅ scoring — ~99.9% of bid side (5,106 resting ≥ 5,000 ✓) ≈ $3.84/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 32.0¢ | 43 | 0 | $100.00 | ✅ scoring — ~91.5% of ask side (12,210 resting ≥ 5,000 ✓) ≈ $3.52/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 38.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~81.7% of ask side (5,488 resting ≥ 5,000 ✓) ≈ $3.40/day (pool ÷ 12 markets) |
| `apdc-trumpadmin-2026-scobes` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~78.4% of bid side (2,550 resting ≥ 2,000 ✓) ≈ $0.58/day (pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~68.4% of ask side (12,072 resting ≥ 5,000 ✓) ≈ $2.63/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 32.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~68.3% of ask side (12,024 resting ≥ 5,000 ✓) ≈ $2.63/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 85.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~64.3% of bid side (5,500 resting ≥ 5,000 ✓) ≈ $2.68/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 15.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~61.7% of ask side (11,945 resting ≥ 5,000 ✓) ≈ $2.37/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 10.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~60.6% of ask side (11,962 resting ≥ 5,000 ✓) ≈ $2.33/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 15.0¢ | 60 | 0 | $100.00 | ✅ scoring — ~60.0% of bid side (5,546 resting ≥ 5,000 ✓) ≈ $2.31/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 23.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~52.5% of ask side (6,821 resting ≥ 5,000 ✓) ≈ $2.19/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte235` | SELL | 9.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~51.0% of ask side (5,440 resting ≥ 5,000 ✓) ≈ $2.13/day (pool ÷ 12 markets) |
| `cranc-uspres28-12-31-2026-tedcru` | SELL | 21.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~40.0% of ask side (5,920 resting ≥ 5,000 ✓) ≈ $0.61/day (pool ÷ 33 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 90.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~39.3% of bid side (5,586 resting ≥ 5,000 ✓) ≈ $1.64/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~37.0% of ask side (11,862 resting ≥ 5,000 ✓) ≈ $1.42/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 10.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~37.0% of ask side (12,225 resting ≥ 5,000 ✓) ≈ $1.42/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 5.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~31.6% of ask side (12,024 resting ≥ 5,000 ✓) ≈ $1.22/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 20.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~31.1% of ask side (12,072 resting ≥ 5,000 ✓) ≈ $1.20/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 21.0¢ | 45 | 0 | $100.00 | ✅ scoring — ~29.2% of ask side (12,053 resting ≥ 5,000 ✓) ≈ $1.12/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 25.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~28.4% of ask side (7,802 resting ≥ 5,000 ✓) ≈ $1.18/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 59.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~24.2% of ask side (7,777 resting ≥ 5,000 ✓) ≈ $1.01/day (pool ÷ 12 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 19.0¢ | 15 | 0 | $25.00 | ✅ scoring — ~23.0% of bid side (5,703 resting ≥ 2,000 ✓) ≈ $2.87/day |
| `scc-senate-gop-2026-11-03-49` | BUY | 22.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~22.5% of bid side (5,644 resting ≥ 5,000 ✓) ≈ $0.87/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | SELL | 15.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~20.5% of ask side (12,023 resting ≥ 5,000 ✓) ≈ $0.79/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | BUY | 65.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~18.4% of bid side (5,581 resting ≥ 5,000 ✓) ≈ $0.77/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 9.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~17.9% of ask side (5,474 resting ≥ 5,000 ✓) ≈ $0.75/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 16.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~17.8% of ask side (11,911 resting ≥ 5,000 ✓) ≈ $0.68/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 16.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~17.0% of ask side (5,522 resting ≥ 5,000 ✓) ≈ $4.26/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 6.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~15.6% of ask side (11,147 resting ≥ 5,000 ✓) ≈ $0.65/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | SELL | 98.0¢ | 5,000 | 0 | $100.00 | ✅ scoring — ~12.3% of ask side (70,904 resting ≥ 5,000 ✓) ≈ $0.51/day (pool ÷ 12 markets) |
| …and 67 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 64 @ 11¢ → $3.84/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 11¢ | 64 (64 yours) | ×0.2^0 = 63.8 |
|  | 6¢ | 105 | ×0.2^5 = 0.0 |
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 20 @ 38¢ → $3.40/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 38¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 39¢ | 22 | ×0.2^1 = 4.4 |
|  | 42¢ | 53 | ×0.2^4 = 0.1 |
|  | 52¢ | 1 | ×0.2^14 = 0.0 |
|  | 53¢ | 11 | ×0.2^15 = 0.0 |
|  | 69¢ | 100 | ×0.2^31 = 0.0 |
|  | 99¢ | 5,281 | ×0.2^61 = 0.0 |
| | | **Σ** | **24.5** |

`yours 20.0 / Σ 24.5 = 81.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 81.7% = $3.40/day`  

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
<details><summary><code>apdc-trumpadmin-2026-scobes</code> BUY 2,000 @ 1¢ → $0.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,550 (2,000 yours) | ×0.1^0 = 2,550.0 |
| | | **Σ** | **2,550.0** |

`yours 2,000.0 / Σ 2,550.0 = 78.4%`  
`$25 ÷ 17 ÷ 2 = $0.74 × 78.4% = $0.58/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `apdc-trumpadmin-2026-brorol`
2. `apdc-trumpadmin-2026-howlut`
3. `apdc-trumpadmin-2026-johrat`
4. `apdc-trumpadmin-2026-karlea`
5. `apdc-trumpadmin-2026-kaspat`
6. `apdc-trumpadmin-2026-linmcm`
7. `apdc-trumpadmin-2026-marrub`
8. `apdc-trumpadmin-2026-petheg`
9. `apdc-trumpadmin-2026-robken`
10. `apdc-trumpadmin-2026-rodsco`
11. `apdc-trumpadmin-2026-rusvou`
12. `apdc-trumpadmin-2026-scobes` ← this one
13. `apdc-trumpadmin-2026-steche`
14. `apdc-trumpadmin-2026-stemil`
15. `apdc-trumpadmin-2026-stewit`
16. `apdc-trumpadmin-2026-suswil`
17. `apdc-trumpadmin-2026-tomhom`

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 85¢ → $2.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 82¢ | 70 | ×0.2^3 = 0.6 |
|  | 1¢ | 5,415 | ×0.2^84 = 0.0 |
| | | **Σ** | **15.6** |

`yours 10.0 / Σ 15.6 = 64.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 64.3% = $2.68/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 50 @ 15¢ → $2.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 81 (50 yours) | ×0.2^0 = 81.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **81.0** |

`yours 50.0 / Σ 81.0 = 61.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 61.7% = $2.37/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 40 @ 10¢ → $2.33/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 66 (40 yours) | ×0.2^0 = 66.0 |
|  | 15¢ | 15 | ×0.2^5 = 0.0 |
|  | 18¢ | 4 | ×0.2^8 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,776 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **66.0** |

`yours 40.0 / Σ 66.0 = 60.6%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 60.6% = $2.33/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 60 @ 15¢ → $2.31/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 100 (60 yours) | ×0.2^0 = 100.0 |
|  | 1¢ | 5,446 | ×0.2^14 = 0.0 |
| | | **Σ** | **100.0** |

`yours 60.0 / Σ 100.0 = 60.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 60.0% = $2.31/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 10 @ 23¢ → $2.19/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 23¢ | 19 (10 yours) | ×0.2^0 = 19.0 |
|  | 25¢ | 1 | ×0.2^2 = 0.0 |
|  | 99¢ | 6,801 | ×0.2^76 = 0.0 |
| | | **Σ** | **19.0** |

`yours 10.0 / Σ 19.0 = 52.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 52.5% = $2.19/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte235</code> SELL 30 @ 9¢ → $2.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 49 (30 yours) | ×0.2^0 = 49.0 |
|  | 10¢ | 49 | ×0.2^1 = 9.8 |
|  | 16¢ | 15 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^41 = 0.0 |
|  | 94¢ | 21 | ×0.2^85 = 0.0 |
|  | 99¢ | 5,281 | ×0.2^90 = 0.0 |
| | | **Σ** | **58.8** |

`yours 30.0 / Σ 58.8 = 51.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 51.0% = $2.13/day`  

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
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235` ← this one

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-tedcru</code> SELL 0 @ 21¢ → $0.61/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (0 yours) | ×0.2^0 = 0.7 |
|  | 23¢ | 1 | ×0.2^2 = 0.0 |
|  | 24¢ | 28 | ×0.2^3 = 0.2 |
|  | 28¢ | 914 | ×0.2^7 = 0.0 |
|  | 50¢ | 25 | ×0.2^29 = 0.0 |
|  | 77¢ | 2 | ×0.2^56 = 0.0 |
|  | 78¢ | 2 | ×0.2^57 = 0.0 |
|  | 99¢ | 4,947 | ×0.2^78 = 0.0 |
| | | **Σ** | **1.0** |

`yours 0.4 / Σ 1.0 = 40.0%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 40.0% = $0.61/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 50 @ 90¢ → $1.64/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 90¢ | 127 (50 yours) | ×0.2^0 = 127.1 |
|  | 1¢ | 5,459 | ×0.2^89 = 0.0 |
| | | **Σ** | **127.1** |

`yours 50.0 / Σ 127.1 = 39.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 39.3% = $1.64/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 50 @ 10¢ → $1.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 135 (50 yours) | ×0.2^0 = 135.2 |
|  | 30¢ | 112 | ×0.2^20 = 0.0 |
|  | 40¢ | 30 | ×0.2^30 = 0.0 |
|  | 50¢ | 100 | ×0.2^40 = 0.0 |
|  | 98¢ | 1,847 | ×0.2^88 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^89 = 0.0 |
| | | **Σ** | **135.2** |

`yours 50.0 / Σ 135.2 = 37.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 37.0% = $1.42/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 45 @ 21¢ → $1.12/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 155 (45 yours) | ×0.2^0 = 155.4 |
|  | 26¢ | 20 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^29 = 0.0 |
|  | 98¢ | 1,777 | ×0.2^77 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^78 = 0.0 |
| | | **Σ** | **155.4** |

`yours 45.4 / Σ 155.4 = 29.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 29.2% = $1.12/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 20 @ 25¢ → $1.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 69 (20 yours) | ×0.2^0 = 69.0 |
|  | 30¢ | 4,633 | ×0.2^5 = 1.5 |
|  | 34¢ | 1,074 | ×0.2^9 = 0.0 |
| | | **Σ** | **70.5** |

`yours 20.0 / Σ 70.5 = 28.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 28.4% = $1.18/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 30 @ 59¢ → $1.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 59¢ | 79 (30 yours) | ×0.2^0 = 79.0 |
|  | 62¢ | 5,594 | ×0.2^3 = 44.7 |
| | | **Σ** | **123.7** |

`yours 30.0 / Σ 123.7 = 24.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 24.2% = $1.01/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 15 @ 19¢ → $2.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 65 (15 yours) | ×0.1^0 = 65.0 |
|  | 18¢ | 2 | ×0.1^1 = 0.2 |
|  | 17¢ | 2 | ×0.1^2 = 0.0 |
|  | 10¢ | 5 | ×0.1^9 = 0.0 |
|  | 4¢ | 17 | ×0.1^15 = 0.0 |
|  | 3¢ | 188 | ×0.1^16 = 0.0 |
|  | 1¢ | 5,424 | ×0.1^18 = 0.0 |
| | | **Σ** | **65.2** |

`yours 15.0 / Σ 65.2 = 23.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 23.0% = $2.87/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 100 @ 22¢ → $0.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 444 (100 yours) | ×0.2^0 = 444.0 |
|  | 1¢ | 5,200 | ×0.2^21 = 0.0 |
| | | **Σ** | **444.0** |

`yours 100.0 / Σ 444.0 = 22.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 22.5% = $0.87/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> SELL 25 @ 15¢ → $0.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 122 (25 yours) | ×0.2^0 = 122.0 |
|  | 29¢ | 2 | ×0.2^14 = 0.0 |
|  | 35¢ | 2 | ×0.2^20 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 1,796 | ×0.2^83 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^84 = 0.0 |
| | | **Σ** | **122.0** |

`yours 25.0 / Σ 122.0 = 20.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 20.5% = $0.79/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> BUY 30 @ 65¢ → $0.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 163 (30 yours) | ×0.2^0 = 162.8 |
|  | 1¢ | 5,418 | ×0.2^64 = 0.0 |
| | | **Σ** | **162.8** |

`yours 30.0 / Σ 162.8 = 18.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 18.4% = $0.77/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 30 @ 9¢ → $0.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 167 (30 yours) | ×0.2^0 = 167.5 |
|  | 20¢ | 1 | ×0.2^11 = 0.0 |
|  | 50¢ | 25 | ×0.2^41 = 0.0 |
|  | 99¢ | 5,281 | ×0.2^90 = 0.0 |
| | | **Σ** | **167.5** |

`yours 30.0 / Σ 167.5 = 17.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 17.9% = $0.75/day`  

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
10. `scc-hrep-rep-2026-11-03-gte225` ← this one
11. `scc-hrep-rep-2026-11-03-gte230`
12. `scc-hrep-rep-2026-11-03-gte235`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 10 @ 16¢ → $0.68/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 56 (10 yours) | ×0.2^0 = 56.2 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,754 | ×0.2^82 = 0.0 |
|  | 99¢ | 10,001 | ×0.2^83 = 0.0 |
| | | **Σ** | **56.2** |

`yours 10.0 / Σ 56.2 = 17.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 17.8% = $0.68/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 100 @ 16¢ → $4.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 587 (100 yours) | ×0.2^0 = 587.4 |
|  | 34¢ | 192 | ×0.2^18 = 0.0 |
|  | 42¢ | 10 | ×0.2^26 = 0.0 |
|  | 49¢ | 100 | ×0.2^33 = 0.0 |
|  | 50¢ | 10 | ×0.2^34 = 0.0 |
|  | 57¢ | 10 | ×0.2^41 = 0.0 |
|  | 82¢ | 2 | ×0.2^66 = 0.0 |
|  | 83¢ | 2 | ×0.2^67 = 0.0 |
|  | 99¢ | 4,609 | ×0.2^83 = 0.0 |
| | | **Σ** | **587.4** |

`yours 100.0 / Σ 587.4 = 17.0%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 17.0% = $4.26/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 30 @ 6¢ → $0.65/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 192 (30 yours) | ×0.2^0 = 191.8 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 50¢ | 25 | ×0.2^44 = 0.0 |
|  | 99¢ | 10,929 | ×0.2^93 = 0.0 |
| | | **Σ** | **191.8** |

`yours 30.0 / Σ 191.8 = 15.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 15.6% = $0.65/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> SELL 5,000 @ 98¢ → $0.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 98¢ | 40,494 (5,000 yours) | ×0.2^0 = 40,494.0 |
| | | **Σ** | **40,494.0** |

`yours 5,000.0 / Σ 40,494.0 = 12.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 12.3% = $0.51/day`  

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
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (90,410 resting) | ~14.8% | ~$11.09 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,226 resting) | ~14.3% | ~$10.75 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,468 resting) | ~31.2% | ~$7.79 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (182,764 resting) | ~4.1% | ~$3.10 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (115,297 resting) | ~2.1% | ~$1.61 |
| `cranc-uspres28-12-31-2026-hunbid` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (5,627 resting) | ~96.1% | ~$1.46 |
| `cranc-uspres28-12-31-2026-jdvan` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (75,807 resting) | ~80.0% | ~$1.21 |
| `cranc-uspres28-12-31-2026-kamhar` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (6,108 resting) | ~79.0% | ~$1.20 |
| `cranc-uspres28-12-31-2026-jonoss` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (6,226 resting) | ~69.0% | ~$1.04 |
| `cranc-uspres28-12-31-2026-gavnew` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (83,460 resting) | ~64.0% | ~$0.97 |
| `cranc-uspres28-12-31-2026-margre` | $100.00 ÷ 33 | 0.20 | 5,000 | SELL side (6,982 resting) | ~63.6% | ~$0.96 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (303,200 resting) | ~1.2% | ~$0.88 |

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
| 2026-08-01 11:57 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 9:53 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 8:15 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 7:23 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 7:14 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 6:13 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 5:12 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 3:38 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 1:34 PM ET | ✅ ok | 1406 | $1374.68 |
| 2026-08-01 1:25 PM ET | ✅ ok | 1406 | $1374.68 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
