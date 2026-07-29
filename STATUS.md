# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-29 7:17 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$52.94/day estimated (ceiling, not promise — details below)

**Earned:** $1,241.95 lifetime ($1,240.74 paid). Last three recorded days — 2026-07-28: **$0.51** · 2026-07-27: **$125.34** · 2026-07-26: **$153.80** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `apdc-jerpowgov-2026-12-31` — SELL at the best price, ~$16.16/day for 200 contracts. Runners-up: `ewc-usgub-oh-2026-11-03-dem` (~$15.03/day), `ewc-usgub-ga-2026-11-03-dem` (~$10.35/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$52.94/day (~$2.21/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `apdc-petehegseth-2026-12-31` | BUY | 16.0¢ | 9 | 0 | $100.00 | ✅ scoring — ~99.9% of bid side (80,551 resting ≥ 5,000 ✓) ≈ $16.65/day (pool ÷ 3 markets) |
| `ewc-pres-bra-2026-10-04-roncai` | SELL | 18.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (6,146 resting ≥ 2,000 ✓) ≈ $1.78/day (pool ÷ 7 markets) |
| `apdc-trumpadmin-2026-robken` | BUY | 45.0¢ | 11 | 0 | $25.00 | ✅ scoring — ~94.5% of bid side (50,702 resting ≥ 2,000 ✓) ≈ $0.69/day (pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 19.0¢ | 30 | 1 | $100.00 | ✅ scoring — ~84.3% of ask side (75,189 resting ≥ 5,000 ✓) ≈ $3.24/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 23.0¢ | 22 | 0 | $100.00 | ✅ scoring — ~70.2% of ask side (240,577 resting ≥ 5,000 ✓) ≈ $2.70/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | SELL | 19.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~66.6% of ask side (61,983 resting ≥ 2,000 ✓) ≈ $0.83/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste0-5` | BUY | 13.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~56.1% of bid side (10,810 resting ≥ 2,000 ✓) ≈ $0.70/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 82.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~53.8% of bid side (5,547 resting ≥ 5,000 ✓) ≈ $2.24/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 15.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~52.7% of ask side (141,703 resting ≥ 5,000 ✓) ≈ $2.03/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 19.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~51.2% of ask side (144,150 resting ≥ 5,000 ✓) ≈ $1.97/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-56` | SELL | 13.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~50.4% of ask side (141,696 resting ≥ 5,000 ✓) ≈ $1.94/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | BUY | 7.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~48.9% of bid side (3,285 resting ≥ 2,000 ✓) ≈ $0.61/day (pool ÷ 10 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 84.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~47.2% of bid side (5,560 resting ≥ 5,000 ✓) ≈ $1.97/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 15.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~46.9% of ask side (103,489 resting ≥ 5,000 ✓) ≈ $1.80/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-47` | SELL | 20.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~44.8% of ask side (108,558 resting ≥ 5,000 ✓) ≈ $1.72/day (pool ÷ 13 markets) |
| `vmc-ussep-misen-2026-08-04-stegte20` | SELL | 2.0¢ | 100 | 0 | $25.00 | ✅ scoring — ~44.4% of ask side (64,321 resting ≥ 2,000 ✓) ≈ $0.56/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 19.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~41.0% of ask side (103,556 resting ≥ 5,000 ✓) ≈ $1.58/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 20.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~38.5% of ask side (142,435 resting ≥ 5,000 ✓) ≈ $1.48/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 60.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~22.8% of ask side (5,501 resting ≥ 5,000 ✓) ≈ $0.95/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 72.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~20.8% of bid side (5,542 resting ≥ 5,000 ✓) ≈ $0.87/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 15.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~20.8% of ask side (5,233 resting ≥ 5,000 ✓) ≈ $0.87/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 17.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~18.3% of bid side (200,563 resting ≥ 5,000 ✓) ≈ $0.71/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 6.0¢ | 100 | 0 | $100.00 | ✅ scoring — ~18.1% of bid side (56,304 resting ≥ 5,000 ✓) ≈ $0.70/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 34.0¢ | 12 | 0 | $100.00 | ✅ scoring — ~17.6% of bid side (5,641 resting ≥ 5,000 ✓) ≈ $0.73/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 17.0¢ | 50 | 1 | $100.00 | ✅ scoring — ~16.1% of ask side (128,036 resting ≥ 5,000 ✓) ≈ $0.62/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | BUY | 7.0¢ | 100 | 1 | $100.00 | ✅ scoring — ~11.5% of bid side (5,617 resting ≥ 5,000 ✓) ≈ $0.48/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 84.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~9.4% of bid side (5,560 resting ≥ 5,000 ✓) ≈ $0.39/day (pool ÷ 12 markets) |
| `vmc-ussep-misen-2026-08-04-ste05-10` | SELL | 15.0¢ | 10 | 2 | $25.00 | ✅ scoring — ~9.1% of ask side (40,132 resting ≥ 2,000 ✓) ≈ $0.11/day (pool ÷ 10 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 14.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~9.0% of bid side (200,565 resting ≥ 5,000 ✓) ≈ $0.35/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte215` | SELL | 25.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~6.2% of ask side (7,810 resting ≥ 5,000 ✓) ≈ $0.26/day (pool ÷ 12 markets) |
| …and 167 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>apdc-petehegseth-2026-12-31</code> BUY 9 @ 16¢ → $16.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 9 (9 yours) | ×0.2^0 = 9.0 |
|  | 12¢ | 6 | ×0.2^4 = 0.0 |
|  | 8¢ | 83 | ×0.2^8 = 0.0 |
|  | 6¢ | 3 | ×0.2^10 = 0.0 |
|  | 1¢ | 80,450 | ×0.2^15 = 0.0 |
| | | **Σ** | **9.0** |

`yours 9.0 / Σ 9.0 = 99.9%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 99.9% = $16.65/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-petehegseth-2026-07-31`
2. `apdc-petehegseth-2026-08-31`
3. `apdc-petehegseth-2026-12-31` ← this one

</details>

</details>
<details><summary><code>ewc-pres-bra-2026-10-04-roncai</code> SELL 20 @ 18¢ → $1.78/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 20 (20 yours) | ×0.1^0 = 20.0 |
|  | 20¢ | 3 | ×0.1^2 = 0.0 |
|  | 30¢ | 2 | ×0.1^12 = 0.0 |
|  | 98¢ | 200 | ×0.1^80 = 0.0 |
|  | 99¢ | 5,921 | ×0.1^81 = 0.0 |
| | | **Σ** | **20.0** |

`yours 20.0 / Σ 20.0 = 99.9%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 99.9% = $1.78/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `ewc-pres-bra-2026-10-04-camsan`
2. `ewc-pres-bra-2026-10-04-ferhad`
3. `ewc-pres-bra-2026-10-04-flabol`
4. `ewc-pres-bra-2026-10-04-luisil`
5. `ewc-pres-bra-2026-10-04-rensan`
6. `ewc-pres-bra-2026-10-04-romzem`
7. `ewc-pres-bra-2026-10-04-roncai` ← this one

</details>

</details>
<details><summary><code>apdc-trumpadmin-2026-robken</code> BUY 11 @ 45¢ → $0.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 45¢ | 11 (11 yours) | ×0.1^0 = 11.0 |
|  | 43¢ | 64 | ×0.1^2 = 0.6 |
|  | 22¢ | 47 | ×0.1^23 = 0.0 |
|  | 20¢ | 2 | ×0.1^25 = 0.0 |
|  | 14¢ | 46 | ×0.1^31 = 0.0 |
|  | 7¢ | 46 | ×0.1^38 = 0.0 |
|  | 5¢ | 2 | ×0.1^40 = 0.0 |
|  | 2¢ | 50,250 | ×0.1^43 = 0.0 |
| | | **Σ** | **11.6** |

`yours 11.0 / Σ 11.6 = 94.5%`  
`$25 ÷ 17 ÷ 2 = $0.74 × 94.5% = $0.69/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `apdc-trumpadmin-2026-brorol`
2. `apdc-trumpadmin-2026-howlut`
3. `apdc-trumpadmin-2026-johrat`
4. `apdc-trumpadmin-2026-karlea`
5. `apdc-trumpadmin-2026-kaspat`
6. `apdc-trumpadmin-2026-linmcm`
7. `apdc-trumpadmin-2026-marrub`
8. `apdc-trumpadmin-2026-petheg`
9. `apdc-trumpadmin-2026-robken` ← this one
10. `apdc-trumpadmin-2026-rodsco`
11. `apdc-trumpadmin-2026-rusvou`
12. `apdc-trumpadmin-2026-scobes`
13. `apdc-trumpadmin-2026-steche`
14. `apdc-trumpadmin-2026-stemil`
15. `apdc-trumpadmin-2026-stewit`
16. `apdc-trumpadmin-2026-suswil`
17. `apdc-trumpadmin-2026-tomhom`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 30 @ 19¢ → $3.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 19¢ | 30 (30 yours) | ×0.2^1 = 6.0 |
|  | 20¢ | 3 | ×0.2^2 = 0.1 |
|  | 30¢ | 4 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 97¢ | 25,555 | ×0.2^79 = 0.0 |
| | | **Σ** | **7.1** |

`yours 6.0 / Σ 7.1 = 84.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 84.3% = $3.24/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 22 @ 23¢ → $2.70/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 23¢ | 31 (22 yours) | ×0.2^0 = 31.0 |
|  | 26¢ | 42 | ×0.2^3 = 0.3 |
|  | 30¢ | 4 | ×0.2^7 = 0.0 |
|  | 50¢ | 100 | ×0.2^27 = 0.0 |
|  | 98¢ | 1,763 | ×0.2^75 = 0.0 |
|  | 99¢ | 238,637 | ×0.2^76 = 0.0 |
| | | **Σ** | **31.3** |

`yours 22.0 / Σ 31.3 = 70.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 70.2% = $2.70/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> SELL 30 @ 19¢ → $0.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 45 (30 yours) | ×0.1^0 = 45.0 |
|  | 21¢ | 2 | ×0.1^2 = 0.0 |
|  | 24¢ | 6 | ×0.1^5 = 0.0 |
|  | 27¢ | 18 | ×0.1^8 = 0.0 |
|  | 45¢ | 231 | ×0.1^26 = 0.0 |
|  | 85¢ | 32 | ×0.1^66 = 0.0 |
|  | 98¢ | 61,149 | ×0.1^79 = 0.0 |
| | | **Σ** | **45.0** |

`yours 30.0 / Σ 45.0 = 66.6%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 66.6% = $0.83/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste0-5</code> BUY 10 @ 13¢ → $0.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 17 (10 yours) | ×0.1^0 = 17.0 |
|  | 12¢ | 7 | ×0.1^1 = 0.7 |
|  | 11¢ | 6 | ×0.1^2 = 0.1 |
|  | 10¢ | 61 | ×0.1^3 = 0.1 |
|  | 5¢ | 20 | ×0.1^8 = 0.0 |
|  | 1¢ | 10,699 | ×0.1^12 = 0.0 |
| | | **Σ** | **17.8** |

`yours 10.0 / Σ 17.8 = 56.1%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 56.1% = $0.70/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 50 @ 82¢ → $2.24/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 93 (50 yours) | ×0.2^0 = 93.0 |
|  | 10¢ | 2 | ×0.2^72 = 0.0 |
|  | 5¢ | 2 | ×0.2^77 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^81 = 0.0 |
| | | **Σ** | **93.0** |

`yours 50.0 / Σ 93.0 = 53.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 53.8% = $2.24/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 50 @ 15¢ → $2.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 91 (50 yours) | ×0.2^0 = 91.0 |
|  | 16¢ | 19 | ×0.2^1 = 3.8 |
|  | 20¢ | 3 | ×0.2^5 = 0.0 |
|  | 30¢ | 4 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 98¢ | 131,484 | ×0.2^83 = 0.0 |
| | | **Σ** | **94.8** |

`yours 50.0 / Σ 94.8 = 52.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 52.7% = $2.03/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 30 @ 19¢ → $1.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 58 (30 yours) | ×0.2^0 = 58.0 |
|  | 20¢ | 3 | ×0.2^1 = 0.6 |
|  | 30¢ | 4 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 98¢ | 131,484 | ×0.2^79 = 0.0 |
| | | **Σ** | **58.6** |

`yours 30.0 / Σ 58.6 = 51.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 51.2% = $1.97/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> SELL 50 @ 13¢ → $1.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 98 (50 yours) | ×0.2^0 = 98.0 |
|  | 14¢ | 6 | ×0.2^1 = 1.2 |
|  | 20¢ | 3 | ×0.2^7 = 0.0 |
|  | 30¢ | 4 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^37 = 0.0 |
|  | 98¢ | 131,484 | ×0.2^85 = 0.0 |
| | | **Σ** | **99.2** |

`yours 50.0 / Σ 99.2 = 50.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 50.4% = $1.94/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> BUY 2 @ 7¢ → $0.61/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 4 (2 yours) | ×0.1^0 = 4.0 |
|  | 5¢ | 8 | ×0.1^2 = 0.1 |
|  | 4¢ | 4 | ×0.1^3 = 0.0 |
|  | 2¢ | 19 | ×0.1^5 = 0.0 |
|  | 1¢ | 3,250 | ×0.1^6 = 0.0 |
| | | **Σ** | **4.1** |

`yours 2.0 / Σ 4.1 = 48.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 48.9% = $0.61/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10` ← this one
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 50 @ 84¢ → $1.97/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 106 (50 yours) | ×0.2^0 = 106.0 |
|  | 10¢ | 2 | ×0.2^74 = 0.0 |
|  | 5¢ | 2 | ×0.2^79 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^83 = 0.0 |
| | | **Σ** | **106.0** |

`yours 50.0 / Σ 106.0 = 47.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 47.2% = $1.97/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 30 @ 15¢ → $1.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 63 (30 yours) | ×0.2^0 = 63.0 |
|  | 16¢ | 5 | ×0.2^1 = 1.0 |
|  | 20¢ | 3 | ×0.2^5 = 0.0 |
|  | 30¢ | 4 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 97¢ | 53,855 | ×0.2^82 = 0.0 |
| | | **Σ** | **64.0** |

`yours 30.0 / Σ 64.0 = 46.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 46.9% = $1.80/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 30 @ 20¢ → $1.72/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 67 (30 yours) | ×0.2^0 = 67.0 |
|  | 30¢ | 4 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 97¢ | 53,892 | ×0.2^77 = 0.0 |
| | | **Σ** | **67.0** |

`yours 30.0 / Σ 67.0 = 44.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 44.8% = $1.72/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-stegte20</code> SELL 100 @ 2¢ → $0.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 225 (100 yours) | ×0.1^0 = 225.0 |
|  | 8¢ | 1 | ×0.1^6 = 0.0 |
|  | 12¢ | 6 | ×0.1^10 = 0.0 |
|  | 13¢ | 18 | ×0.1^11 = 0.0 |
|  | 20¢ | 3 | ×0.1^18 = 0.0 |
|  | 30¢ | 2 | ×0.1^28 = 0.0 |
|  | 45¢ | 25 | ×0.1^43 = 0.0 |
|  | 98¢ | 61,041 | ×0.1^96 = 0.0 |
| | | **Σ** | **225.0** |

`yours 100.0 / Σ 225.0 = 44.4%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 44.4% = $0.56/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 20 @ 19¢ → $1.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 48 (20 yours) | ×0.2^0 = 48.0 |
|  | 21¢ | 18 | ×0.2^2 = 0.7 |
|  | 30¢ | 2 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 97¢ | 53,892 | ×0.2^78 = 0.0 |
| | | **Σ** | **48.7** |

`yours 20.0 / Σ 48.7 = 41.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 41.0% = $1.58/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 20 @ 20¢ → $1.48/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 52 (20 yours) | ×0.2^0 = 52.0 |
|  | 30¢ | 4 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^30 = 0.0 |
|  | 97¢ | 92,783 | ×0.2^77 = 0.0 |
| | | **Σ** | **52.0** |

`yours 20.0 / Σ 52.0 = 38.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 38.5% = $1.48/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 4 @ 60¢ → $0.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 60¢ | 19 (4 yours) | ×0.2^0 = 19.5 |
|  | 62¢ | 2 | ×0.2^2 = 0.1 |
|  | 69¢ | 40 | ×0.2^9 = 0.0 |
|  | 99¢ | 5,440 | ×0.2^39 = 0.0 |
| | | **Σ** | **19.5** |

`yours 4.5 / Σ 19.5 = 22.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 22.8% = $0.95/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte185</code> BUY 50 @ 72¢ → $0.87/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 73¢ | 38 | ×0.2^0 = 38.0 |
| ▶ | 72¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 10¢ | 2 | ×0.2^63 = 0.0 |
|  | 5¢ | 2 | ×0.2^68 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^72 = 0.0 |
| | | **Σ** | **48.0** |

`yours 10.0 / Σ 48.0 = 20.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 20.8% = $0.87/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 50 @ 15¢ → $0.87/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 14¢ | 32 | ×0.2^0 = 32.0 |
| ▶ | 15¢ | 80 (50 yours) | ×0.2^1 = 16.0 |
|  | 20¢ | 7 | ×0.2^6 = 0.0 |
|  | 21¢ | 2 | ×0.2^7 = 0.0 |
|  | 22¢ | 1 | ×0.2^8 = 0.0 |
|  | 23¢ | 1 | ×0.2^9 = 0.0 |
|  | 30¢ | 4 | ×0.2^16 = 0.0 |
|  | 50¢ | 25 | ×0.2^36 = 0.0 |
|  | 99¢ | 5,081 | ×0.2^85 = 0.0 |
| | | **Σ** | **48.0** |

`yours 10.0 / Σ 48.0 = 20.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 20.8% = $0.87/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 20 @ 17¢ → $0.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 109 (20 yours) | ×0.2^0 = 109.0 |
|  | 15¢ | 2 | ×0.2^2 = 0.1 |
|  | 5¢ | 2 | ×0.2^12 = 0.0 |
|  | 3¢ | 200,250 | ×0.2^14 = 0.0 |
| | | **Σ** | **109.1** |

`yours 20.0 / Σ 109.1 = 18.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.3% = $0.71/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 100 @ 6¢ → $0.70/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 438 (100 yours) | ×0.2^0 = 438.0 |
|  | 5¢ | 12 | ×0.2^1 = 2.4 |
|  | 4¢ | 625 | ×0.2^2 = 25.0 |
|  | 2¢ | 55,000 | ×0.2^4 = 88.0 |
| | | **Σ** | **553.4** |

`yours 100.0 / Σ 553.4 = 18.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 18.1% = $0.70/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 12 @ 34¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 34¢ | 66 (12 yours) | ×0.2^0 = 65.5 |
|  | 25¢ | 100 | ×0.2^9 = 0.0 |
|  | 10¢ | 2 | ×0.2^24 = 0.0 |
|  | 5¢ | 2 | ×0.2^29 = 0.0 |
|  | 1¢ | 5,471 | ×0.2^33 = 0.0 |
| | | **Σ** | **65.5** |

`yours 11.5 / Σ 65.5 = 17.6%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 17.6% = $0.73/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 50 @ 17¢ → $0.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 52 | ×0.2^0 = 52.0 |
| ▶ | 17¢ | 50 (50 yours) | ×0.2^1 = 10.0 |
|  | 18¢ | 5 | ×0.2^2 = 0.2 |
|  | 19¢ | 3 | ×0.2^3 = 0.0 |
|  | 20¢ | 3 | ×0.2^4 = 0.0 |
|  | 30¢ | 4 | ×0.2^14 = 0.0 |
|  | 50¢ | 100 | ×0.2^34 = 0.0 |
|  | 98¢ | 1,000 | ×0.2^82 = 0.0 |
|  | 99¢ | 126,819 | ×0.2^83 = 0.0 |
| | | **Σ** | **62.2** |

`yours 10.0 / Σ 62.2 = 16.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 16.1% = $0.62/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> BUY 100 @ 7¢ → $0.48/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 150 | ×0.2^0 = 150.0 |
| ▶ | 7¢ | 100 (100 yours) | ×0.2^1 = 20.0 |
|  | 6¢ | 100 | ×0.2^2 = 4.0 |
|  | 5¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 5,265 | ×0.2^7 = 0.1 |
| | | **Σ** | **174.1** |

`yours 20.0 / Σ 174.1 = 11.5%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.5% = $0.48/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 10 @ 84¢ → $0.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 84¢ | 106 (10 yours) | ×0.2^0 = 106.0 |
|  | 10¢ | 2 | ×0.2^74 = 0.0 |
|  | 5¢ | 2 | ×0.2^79 = 0.0 |
|  | 1¢ | 5,450 | ×0.2^83 = 0.0 |
| | | **Σ** | **106.0** |

`yours 10.0 / Σ 106.0 = 9.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 9.4% = $0.39/day`  

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
<details><summary><code>vmc-ussep-misen-2026-08-04-ste05-10</code> SELL 10 @ 15¢ → $0.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 13¢ | 1 | ×0.1^0 = 1.0 |
| ▶ | 15¢ | 10 (10 yours) | ×0.1^2 = 0.1 |
|  | 17¢ | 0 | ×0.1^4 = 0.0 |
|  | 20¢ | 3 | ×0.1^7 = 0.0 |
|  | 21¢ | 6 | ×0.1^8 = 0.0 |
|  | 23¢ | 17 | ×0.1^10 = 0.0 |
|  | 30¢ | 2 | ×0.1^17 = 0.0 |
|  | 37¢ | 6 | ×0.1^24 = 0.0 |
|  | 39¢ | 609 | ×0.1^26 = 0.0 |
|  | 41¢ | 2,000 | ×0.1^28 = 0.0 |
| | | **Σ** | **1.1** |

`yours 0.1 / Σ 1.1 = 9.1%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 9.1% = $0.11/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10` ← this one
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 10 @ 14¢ → $0.35/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 111 (10 yours) | ×0.2^0 = 111.0 |
|  | 10¢ | 2 | ×0.2^4 = 0.0 |
|  | 5¢ | 2 | ×0.2^9 = 0.0 |
|  | 1¢ | 200,450 | ×0.2^13 = 0.0 |
| | | **Σ** | **111.0** |

`yours 10.0 / Σ 111.0 = 9.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.0% = $0.35/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte215</code> SELL 1 @ 25¢ → $0.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 16 (1 yours) | ×0.2^0 = 16.0 |
|  | 27¢ | 4 | ×0.2^2 = 0.2 |
|  | 28¢ | 11 | ×0.2^3 = 0.1 |
|  | 30¢ | 1 | ×0.2^5 = 0.0 |
|  | 32¢ | 3 | ×0.2^7 = 0.0 |
|  | 33¢ | 3 | ×0.2^8 = 0.0 |
|  | 99¢ | 7,772 | ×0.2^74 = 0.0 |
| | | **Σ** | **16.2** |

`yours 1.0 / Σ 16.2 = 6.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 6.2% = $0.26/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-28 | ~$148.78 | $0.51 | 0% |
| 2026-07-27 | ~$145.69 | $125.34 | 86% |
| 2026-07-26 | ~$159.09 | $153.80 | 97% |

Biggest gaps on 2026-07-28: `enwc-ussep-mi-2026-08-04-dem-abdels` (est ~$18.10 → got $0.00), `lawec-saveact-2026-12-31` (est ~$9.15 → got $0.00), `stsc-bab-el-mandeb-clsd-2026-12-31` (est ~$5.96 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (25,288 resting) | ~96.9% | ~$16.16 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (82,238 resting) | ~20.0% | ~$15.03 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (88,729 resting) | ~13.8% | ~$10.35 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (103,864 resting) | ~5.6% | ~$4.21 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (76,619 resting) | ~66.8% | ~$4.17 |
| `ewc-usse-tx-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (274,897 resting) | ~5.3% | ~$3.97 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (173,281 resting) | ~4.7% | ~$3.56 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (275,446 resting) | ~4.4% | ~$3.29 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (103,045 resting) | ~2.8% | ~$2.09 |
| `apdc-jerpowgov-2026-07-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (5,765 resting) | ~11.3% | ~$1.89 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (198,820 resting) | ~2.4% | ~$1.80 |
| `ewc-usse-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (65,935 resting) | ~2.2% | ~$1.62 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,240.74 |
| Skipped | $1.21 |
| **Total earned** | **$1,241.95** |

1063 reward rows · 26 days with rewards · 329 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-07-28 | $0.51 | `█` |
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
| 2026-07-15 | $1.53 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,241.95 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.23 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.16 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.66 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $34.20 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.45 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.40 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $28.21 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.15 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.61 |
| `vmc-ussep-misen-2026-08-04-els15-20` | $22.78 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-29 7:17 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 6:15 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 5:14 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 3:47 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 2:16 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 1:22 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 12:42 PM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 11:22 AM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 8:23 AM ET | ✅ ok | 1063 | $1241.95 |
| 2026-07-29 6:00 AM ET | ✅ ok | 1063 | $1241.95 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
