# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-04 8:17 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$42.54/day estimated (ceiling, not promise — details below)

**Earned:** $1,529.47 lifetime ($1,514.21 paid). Last three recorded days — 2026-08-02: **$14.05** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-01: **$52.30** · 2026-07-31: **$67.96** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-xavbec` — BUY at the best price, ~$24.20/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$16.31/day), `enwc-ussep-mn-2026-08-11-dem-angcra` (~$7.22/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$42.54/day (~$1.77/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `ewc-pres-arg-2027-10-24-javmil` | SELL | 65.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~99.6% of ask side (2,657 resting ≥ 2,000 ✓) ≈ $1.13/day (pool ÷ 11 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 20.0¢ | 14 | 0 | $100.00 | ✅ scoring — ~98.3% of bid side (50,493 resting ≥ 5,000 ✓) ≈ $3.78/day (pool ÷ 13 markets) |
| `apdc-alito-2026-12-31` | SELL | 20.0¢ | 125 | 0 | $100.00 | ✅ scoring — ~89.2% of ask side (6,605 resting ≥ 5,000 ✓) ≈ $22.29/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 24.0¢ | 6 | 0 | $100.00 | ✅ scoring — ~87.4% of bid side (50,533 resting ≥ 5,000 ✓) ≈ $3.36/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 22.0¢ | 28 | 0 | $100.00 | ✅ scoring — ~47.5% of ask side (112,784 resting ≥ 5,000 ✓) ≈ $1.83/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-51` | SELL | 18.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~33.2% of ask side (112,810 resting ≥ 5,000 ✓) ≈ $1.28/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 85.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~27.2% of bid side (80,318 resting ≥ 5,000 ✓) ≈ $1.13/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~26.9% of ask side (117,941 resting ≥ 5,000 ✓) ≈ $1.04/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-nebr` | BUY | 1.0¢ | 1,000 | 1 | $500.00 | ✅ scoring — ~18.9% of bid side (4,643 resting ≥ 2,500 ✓) ≈ $0.65/day (pool ÷ 73 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~14.3% of ask side (62,983 resting ≥ 5,000 ✓) ≈ $0.60/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | SELL | 15.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~12.4% of ask side (62,947 resting ≥ 5,000 ✓) ≈ $0.52/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 14.0¢ | 12 | 0 | $100.00 | ✅ scoring — ~12.0% of bid side (87,834 resting ≥ 5,000 ✓) ≈ $0.50/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 18.0¢ | 10 | 1 | $100.00 | ✅ scoring — ~11.5% of ask side (98,685 resting ≥ 5,000 ✓) ≈ $0.44/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 61.0¢ | 10 | 2 | $100.00 | ✅ scoring — ~11.2% of ask side (47,920 resting ≥ 5,000 ✓) ≈ $0.47/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 8.0¢ | 44 | 0 | $100.00 | ✅ scoring — ~9.2% of bid side (11,170 resting ≥ 5,000 ✓) ≈ $0.36/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | BUY | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~7.8% of bid side (80,763 resting ≥ 5,000 ✓) ≈ $0.33/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 5.0¢ | 133 | 0 | $100.00 | ✅ scoring — ~7.3% of bid side (52,025 resting ≥ 5,000 ✓) ≈ $0.28/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-54` | SELL | 6.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~5.9% of ask side (113,623 resting ≥ 5,000 ✓) ≈ $0.23/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 47.0¢ | 30 | 3 | $100.00 | ✅ scoring — ~5.9% of ask side (62,836 resting ≥ 5,000 ✓) ≈ $0.25/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-56` | BUY | 4.0¢ | 500 | 1 | $100.00 | ✅ scoring — ~5.5% of bid side (52,025 resting ≥ 5,000 ✓) ≈ $0.21/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 10.0¢ | 25 | 0 | $25.00 | ✅ scoring — ~5.1% of ask side (4,474 resting ≥ 2,000 ✓) ≈ $0.64/day |
| `scc-hrep-rep-2026-11-03-gte230` | SELL | 7.0¢ | 15 | 0 | $100.00 | ✅ scoring — ~4.1% of ask side (48,090 resting ≥ 5,000 ✓) ≈ $0.17/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 5.0¢ | 4 | 0 | $100.00 | ✅ scoring — ~3.0% of bid side (15,421 resting ≥ 5,000 ✓) ≈ $0.12/day (pool ÷ 13 markets) |
| `ewc-usse-oh-2026-11-03-rep` | BUY | 48.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~1.7% of bid side (46,122 resting ≥ 5,000 ✓) ≈ $0.41/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 2.0¢ | 200 | 3 | $100.00 | ✅ scoring — ~1.2% of bid side (15,421 resting ≥ 5,000 ✓) ≈ $0.05/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 20.0¢ | 15 | 3 | $100.00 | ✅ scoring — ~0.7% of ask side (98,685 resting ≥ 5,000 ✓) ≈ $0.03/day (pool ÷ 13 markets) |
| `ewc-usse-tx-2026-11-03-dem` | BUY | 47.0¢ | 50 | 0 | $300.00 | ✅ scoring — ~0.5% of bid side (381,687 resting ≥ 10,000 ✓) ≈ $0.39/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-46` | BUY | 3.0¢ | 500 | 0 | $100.00 | ✅ scoring — ~0.5% of bid side (119,531 resting ≥ 5,000 ✓) ≈ $0.02/day (pool ÷ 13 markets) |
| `tec-cbb-champ-2027-04-05-w-mst` | BUY | 7.0¢ | 5 | 0 | $500.00 | ✅ scoring — ~0.4% of bid side (28,468 resting ≥ 2,500 ✓) ≈ $0.01/day (pool ÷ 73 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 40.0¢ | 42 | 3 | $100.00 | ✅ scoring — ~0.3% of ask side (98,796 resting ≥ 5,000 ✓) ≈ $0.01/day (pool ÷ 13 markets) |
| …and 16 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>ewc-pres-arg-2027-10-24-javmil</code> SELL 0 @ 65¢ → $1.13/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 0 (0 yours) | ×0.1^0 = 0.1 |
|  | 72¢ | 1,931 | ×0.1^7 = 0.0 |
|  | 80¢ | 1 | ×0.1^15 = 0.0 |
|  | 85¢ | 25 | ×0.1^20 = 0.0 |
|  | 99¢ | 700 | ×0.1^34 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 99.6%`  
`$25 ÷ 11 ÷ 2 = $1.14 × 99.6% = $1.13/day`  

<details><summary>÷ 11 markets in this race — tap to list</summary>

1. `ewc-pres-arg-2027-10-24-axekic`
2. `ewc-pres-arg-2027-10-24-dangeb`
3. `ewc-pres-arg-2027-10-24-estbul`
4. `ewc-pres-arg-2027-10-24-facman`
5. `ewc-pres-arg-2027-10-24-javmil` ← this one
6. `ewc-pres-arg-2027-10-24-juagra`
7. `ewc-pres-arg-2027-10-24-juasch`
8. `ewc-pres-arg-2027-10-24-maumac`
9. `ewc-pres-arg-2027-10-24-myrbre`
10. `ewc-pres-arg-2027-10-24-sermas`
11. `ewc-pres-arg-2027-10-24-vicvil`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 14 @ 20¢ → $3.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 14 (14 yours) | ×0.2^0 = 13.8 |
|  | 18¢ | 6 | ×0.2^2 = 0.2 |
|  | 16¢ | 10 | ×0.2^4 = 0.0 |
|  | 14¢ | 42 | ×0.2^6 = 0.0 |
|  | 12¢ | 163 | ×0.2^8 = 0.0 |
|  | 3¢ | 58 | ×0.2^17 = 0.0 |
|  | 2¢ | 50,000 | ×0.2^18 = 0.0 |
| | | **Σ** | **14.0** |

`yours 13.8 / Σ 14.0 = 98.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 98.3% = $3.78/day`  

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
<details><summary><code>apdc-alito-2026-12-31</code> SELL 125 @ 20¢ → $22.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 137 (125 yours) | ×0.2^0 = 137.0 |
|  | 22¢ | 71 | ×0.2^2 = 2.9 |
|  | 25¢ | 1,091 | ×0.2^5 = 0.3 |
|  | 48¢ | 105 | ×0.2^28 = 0.0 |
|  | 99¢ | 5,200 | ×0.2^79 = 0.0 |
| | | **Σ** | **140.2** |

`yours 125.0 / Σ 140.2 = 89.2%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 89.2% = $22.29/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 6 @ 24¢ → $3.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 6 (6 yours) | ×0.2^0 = 6.0 |
|  | 23¢ | 1 | ×0.2^1 = 0.2 |
|  | 22¢ | 17 | ×0.2^2 = 0.7 |
|  | 2¢ | 50,209 | ×0.2^22 = 0.0 |
| | | **Σ** | **6.9** |

`yours 6.0 / Σ 6.9 = 87.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 87.4% = $3.36/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 28 @ 22¢ → $1.83/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 59 (28 yours) | ×0.2^0 = 59.1 |
|  | 24¢ | 3 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^28 = 0.0 |
|  | 97¢ | 58,044 | ×0.2^75 = 0.0 |
| | | **Σ** | **59.3** |

`yours 28.1 / Σ 59.3 = 47.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.5% = $1.83/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> SELL 15 @ 18¢ → $1.28/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 45 (15 yours) | ×0.2^0 = 45.0 |
|  | 20¢ | 3 | ×0.2^2 = 0.1 |
|  | 50¢ | 100 | ×0.2^32 = 0.0 |
|  | 97¢ | 58,083 | ×0.2^79 = 0.0 |
| | | **Σ** | **45.1** |

`yours 15.0 / Σ 45.1 = 33.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 33.2% = $1.28/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 30 @ 85¢ → $1.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 110 (30 yours) | ×0.2^0 = 110.2 |
|  | 83¢ | 0 | ×0.2^2 = 0.0 |
|  | 2¢ | 80,008 | ×0.2^83 = 0.0 |
| | | **Σ** | **110.2** |

`yours 30.0 / Σ 110.2 = 27.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 27.2% = $1.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 1 @ 4¢ → $1.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 5¢ | 11 | ×0.2^1 = 2.2 |
|  | 7¢ | 64 | ×0.2^3 = 0.5 |
|  | 19¢ | 100 | ×0.2^15 = 0.0 |
|  | 50¢ | 100 | ×0.2^46 = 0.0 |
|  | 97¢ | 60,967 | ×0.2^93 = 0.0 |
| | | **Σ** | **3.7** |

`yours 1.0 / Σ 3.7 = 26.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 26.9% = $1.04/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-nebr</code> BUY 1,000 @ 1¢ → $0.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 344 | ×0.35^0 = 344.0 |
| ▶ | 1¢ | 4,299 (1,000 yours) | ×0.35^1 = 1,504.6 |
| | | **Σ** | **1,848.6** |

`yours 350.0 / Σ 1,848.6 = 18.9%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 18.9% = $0.65/day`  

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
40. `tec-cbb-champ-2027-04-05-w-nebr` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 10 @ 48¢ → $0.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 70 (10 yours) | ×0.2^0 = 70.0 |
|  | 50¢ | 0 | ×0.2^2 = 0.0 |
|  | 54¢ | 107 | ×0.2^6 = 0.0 |
|  | 82¢ | 105 | ×0.2^34 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **70.0** |

`yours 10.0 / Σ 70.0 = 14.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 14.3% = $0.60/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> SELL 10 @ 15¢ → $0.52/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 45 (10 yours) | ×0.2^0 = 45.0 |
|  | 16¢ | 177 | ×0.2^1 = 35.4 |
|  | 17¢ | 0 | ×0.2^2 = 0.0 |
|  | 50¢ | 25 | ×0.2^35 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^83 = 0.0 |
| | | **Σ** | **80.4** |

`yours 10.0 / Σ 80.4 = 12.4%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 12.4% = $0.52/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 12 @ 14¢ → $0.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 100 (12 yours) | ×0.2^0 = 99.6 |
|  | 12¢ | 6 | ×0.2^2 = 0.2 |
|  | 8¢ | 100 | ×0.2^6 = 0.0 |
|  | 7¢ | 81 | ×0.2^7 = 0.0 |
|  | 6¢ | 100 | ×0.2^8 = 0.0 |
|  | 3¢ | 5,247 | ×0.2^11 = 0.0 |
| | | **Σ** | **99.8** |

`yours 12.0 / Σ 99.8 = 12.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 12.0% = $0.50/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 10 @ 18¢ → $0.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 15 | ×0.2^0 = 15.0 |
| ▶ | 18¢ | 11 (10 yours) | ×0.2^1 = 2.2 |
|  | 19¢ | 1 | ×0.2^2 = 0.0 |
|  | 20¢ | 15 | ×0.2^3 = 0.1 |
|  | 31¢ | 111 | ×0.2^14 = 0.0 |
|  | 40¢ | 30 | ×0.2^23 = 0.0 |
|  | 50¢ | 100 | ×0.2^33 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^80 = 0.0 |
| | | **Σ** | **17.4** |

`yours 2.0 / Σ 17.4 = 11.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 11.5% = $0.44/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 10 @ 61¢ → $0.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 59¢ | 3 | ×0.2^0 = 3.0 |
| ▶ | 61¢ | 14 (10 yours) | ×0.2^2 = 0.6 |
|  | 66¢ | 1 | ×0.2^7 = 0.0 |
|  | 71¢ | 200 | ×0.2^12 = 0.0 |
|  | 90¢ | 1 | ×0.2^31 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^39 = 0.0 |
| | | **Σ** | **3.6** |

`yours 0.4 / Σ 3.6 = 11.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 11.2% = $0.47/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 44 @ 8¢ → $0.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 66 (44 yours) | ×0.2^0 = 66.0 |
|  | 6¢ | 10,266 | ×0.2^2 = 410.6 |
| | | **Σ** | **476.6** |

`yours 44.0 / Σ 476.6 = 9.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 9.2% = $0.36/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> BUY 10 @ 10¢ → $0.33/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 128 (10 yours) | ×0.2^0 = 128.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.1 |
|  | 1¢ | 80,633 | ×0.2^9 = 0.0 |
| | | **Σ** | **128.1** |

`yours 10.0 / Σ 128.1 = 7.8%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 7.8% = $0.33/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 133 @ 5¢ → $0.28/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 1,312 (133 yours) | ×0.2^0 = 1,312.0 |
|  | 4¢ | 500 | ×0.2^1 = 100.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **1,813.2** |

`yours 133.0 / Σ 1,813.2 = 7.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 7.3% = $0.28/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-54</code> SELL 1 @ 6¢ → $0.23/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 6¢ | 16 (1 yours) | ×0.2^0 = 16.0 |
|  | 8¢ | 1 | ×0.2^2 = 0.0 |
|  | 9¢ | 100 | ×0.2^3 = 0.8 |
|  | 10¢ | 1 | ×0.2^4 = 0.0 |
|  | 16¢ | 3 | ×0.2^10 = 0.0 |
|  | 50¢ | 100 | ×0.2^44 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^91 = 0.0 |
| | | **Σ** | **16.8** |

`yours 1.0 / Σ 16.8 = 5.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.9% = $0.23/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 30 @ 47¢ → $0.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 44¢ | 4 | ×0.2^0 = 3.8 |
|  | 46¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 47¢ | 30 (30 yours) | ×0.2^3 = 0.2 |
|  | 52¢ | 1 | ×0.2^8 = 0.0 |
|  | 69¢ | 100 | ×0.2^25 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^54 = 0.0 |
| | | **Σ** | **4.1** |

`yours 0.2 / Σ 4.1 = 5.9%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 5.9% = $0.25/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-56</code> BUY 500 @ 4¢ → $0.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 1,312 | ×0.2^0 = 1,312.0 |
| ▶ | 4¢ | 500 (500 yours) | ×0.2^1 = 100.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 49,980 | ×0.2^3 = 399.8 |
| | | **Σ** | **1,813.2** |

`yours 100.0 / Σ 1,813.2 = 5.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 5.5% = $0.21/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 25 @ 10¢ → $0.64/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 488 (25 yours) | ×0.1^0 = 487.8 |
|  | 12¢ | 1 | ×0.1^2 = 0.0 |
|  | 15¢ | 98 | ×0.1^5 = 0.0 |
|  | 19¢ | 2,517 | ×0.1^9 = 0.0 |
| | | **Σ** | **487.8** |

`yours 25.0 / Σ 487.8 = 5.1%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 5.1% = $0.64/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte230</code> SELL 15 @ 7¢ → $0.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 364 (15 yours) | ×0.2^0 = 364.0 |
|  | 9¢ | 0 | ×0.2^2 = 0.0 |
|  | 10¢ | 1 | ×0.2^3 = 0.0 |
|  | 50¢ | 25 | ×0.2^43 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^91 = 0.0 |
| | | **Σ** | **364.0** |

`yours 15.0 / Σ 364.0 = 4.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 4.1% = $0.17/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 4 @ 5¢ → $0.12/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 48 (4 yours) | ×0.2^0 = 48.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
|  | 2¢ | 10,466 | ×0.2^3 = 83.7 |
| | | **Σ** | **133.1** |

`yours 4.0 / Σ 133.1 = 3.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 3.0% = $0.12/day`  

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
<details><summary><code>ewc-usse-oh-2026-11-03-rep</code> BUY 50 @ 48¢ → $0.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 2,902 (50 yours) | ×0.2^0 = 2,902.0 |
|  | 46¢ | 3,020 | ×0.2^2 = 120.8 |
| | | **Σ** | **3,022.8** |

`yours 50.0 / Σ 3,022.8 = 1.7%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 1.7% = $0.41/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-oh-2026-11-03-dem`
2. `ewc-usse-oh-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-gte57</code> BUY 200 @ 2¢ → $0.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 48 | ×0.2^0 = 48.0 |
|  | 3¢ | 33 | ×0.2^2 = 1.3 |
| ▶ | 2¢ | 10,466 (200 yours) | ×0.2^3 = 83.7 |
| | | **Σ** | **133.1** |

`yours 1.6 / Σ 133.1 = 1.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 1.2% = $0.05/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 15 @ 20¢ → $0.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 15 | ×0.2^0 = 15.0 |
|  | 18¢ | 11 | ×0.2^1 = 2.2 |
|  | 19¢ | 1 | ×0.2^2 = 0.0 |
| ▶ | 20¢ | 15 (15 yours) | ×0.2^3 = 0.1 |
|  | 31¢ | 111 | ×0.2^14 = 0.0 |
|  | 40¢ | 30 | ×0.2^23 = 0.0 |
|  | 50¢ | 100 | ×0.2^33 = 0.0 |
|  | 97¢ | 43,824 | ×0.2^80 = 0.0 |
| | | **Σ** | **17.4** |

`yours 0.1 / Σ 17.4 = 0.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.7% = $0.03/day`  

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
<details><summary><code>ewc-usse-tx-2026-11-03-dem</code> BUY 50 @ 47¢ → $0.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 9,235 (50 yours) | ×0.2^0 = 9,235.0 |
|  | 46¢ | 2,196 | ×0.2^1 = 439.2 |
| | | **Σ** | **9,674.2** |

`yours 50.0 / Σ 9,674.2 = 0.5%`  
`$300 ÷ 2 ÷ 2 = $75.00 × 0.5% = $0.39/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ewc-usse-tx-2026-11-03-dem` ← this one
2. `ewc-usse-tx-2026-11-03-rep`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> BUY 500 @ 3¢ → $0.02/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 109,331 (500 yours) | ×0.2^0 = 109,331.0 |
| | | **Σ** | **109,331.0** |

`yours 500.0 / Σ 109,331.0 = 0.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.5% = $0.02/day`  

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
<details><summary><code>tec-cbb-champ-2027-04-05-w-mst</code> BUY 5 @ 7¢ → $0.01/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 60 (5 yours) | ×0.35^0 = 60.0 |
|  | 5¢ | 20 | ×0.35^2 = 2.4 |
|  | 4¢ | 25,508 | ×0.35^3 = 1,093.7 |
| | | **Σ** | **1,156.1** |

`yours 5.0 / Σ 1,156.1 = 0.4%`  
`$500 ÷ 73 ÷ 2 = $3.42 × 0.4% = $0.01/day`  

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
36. `tec-cbb-champ-2027-04-05-w-mst` ← this one
37. `tec-cbb-champ-2027-04-05-w-ncar`
38. `tec-cbb-champ-2027-04-05-w-ncst`
39. `tec-cbb-champ-2027-04-05-w-nd`
40. `tec-cbb-champ-2027-04-05-w-nebr`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 42 @ 40¢ → $0.01/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 37¢ | 92 | ×0.2^0 = 91.8 |
|  | 38¢ | 36 | ×0.2^1 = 7.2 |
|  | 39¢ | 18 | ×0.2^2 = 0.7 |
| ▶ | 40¢ | 42 (42 yours) | ×0.2^3 = 0.3 |
|  | 49¢ | 104 | ×0.2^12 = 0.0 |
|  | 50¢ | 100 | ×0.2^13 = 0.0 |
|  | 97¢ | 43,826 | ×0.2^60 = 0.0 |
| | | **Σ** | **100.0** |

`yours 0.3 / Σ 100.0 = 0.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 0.3% = $0.01/day`  

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

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-01 | ~$46.23 | $52.30 | 113% |
| 2026-07-31 | ~$64.95 | $67.96 | 105% |
| 2026-07-30 | ~$43.67 | $20.48 | 47% |

Biggest gaps on 2026-08-01: `scc-hrep-rep-2026-11-03-gte215` (est ~$2.09 → got $1.51), `scc-senate-gop-2026-11-03-52` (est ~$3.15 → got $2.78), `cranc-uspres28-12-31-2026-tedcru` (est ~$0.71 → got $0.35)

_2026-08-02 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (320,724 resting) | ~32.3% | ~$24.20 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,617 resting) | ~65.2% | ~$16.31 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (87,168 resting) | ~28.9% | ~$7.22 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (46,645 resting) | ~8.3% | ~$6.25 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (76,913 resting) | ~20.1% | ~$5.02 |
| `ewc-usse-me-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (184,155 resting) | ~5.6% | ~$4.22 |
| `apdc-jerpowgov-2026-12-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,501 resting) | ~10.7% | ~$2.69 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (236,778 resting) | ~3.2% | ~$2.40 |
| `ewc-usse-tx-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (189,121 resting) | ~2.3% | ~$1.75 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (92,855 resting) | ~2.2% | ~$1.63 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (55,746 resting) | ~2.0% | ~$1.48 |
| `cranc-uspres28-12-31-2026-jdvan` | $100.00 ÷ 33 | 0.20 | 5,000 | BUY side (75,824 resting) | ~85.9% | ~$1.30 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,514.21 |
| Pending | $14.05 |
| Skipped | $1.21 |
| **Total earned** | **$1,529.47** |

1573 reward rows · 31 days with rewards · 353 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-02 ⚠️ multi-day pending bucket | $14.05 | `█` |
| 2026-08-01 | $52.30 | `█████` |
| 2026-07-31 | $67.96 | `██████` |
| 2026-07-30 | $20.48 | `██` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $66.35 | `█` |
| 2026-07 | $1,463.12 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.35 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.33 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.85 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `opdc-mcconnell-resign-2026-11-02` | $35.05 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $28.80 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.67 |
| `apdc-alito-2026-12-31` | $23.38 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-04 8:17 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 6:31 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 4:46 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 2:57 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 1:06 PM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 10:45 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 8:21 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 6:01 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-04 2:43 AM ET | ✅ ok | 1573 | $1529.47 |
| 2026-08-03 11:42 PM ET | ✅ ok | 1573 | $1529.47 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
