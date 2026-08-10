# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-09 9:05 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$132.49/day estimated (ceiling, not promise — details below)

**Earned:** $1,787.15 lifetime ($1,771.01 paid). Last three recorded days — 2026-08-08: **$14.73** · 2026-08-07: **$60.33** · 2026-08-06: **$52.21** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — SELL at the best price, ~$36.43/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$31.80/day), `apdc-jerpowgov-2026-08-31` (~$15.97/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$132.49/day (~$5.52/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `pandc-anydis-2027-12-31` | BUY | 21.0¢ | 1 | 0 | $50.00 | ✅ scoring — ~99.0% of bid side (11,102 resting ≥ 10,000 ✓) ≈ $12.38/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 19.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.0% of bid side (85,729 resting ≥ 5,000 ✓) ≈ $4.13/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-51` | BUY | 19.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~98.0% of bid side (200,322 resting ≥ 5,000 ✓) ≈ $3.77/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~96.5% of bid side (50,558 resting ≥ 5,000 ✓) ≈ $3.71/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~88.2% of bid side (10,712 resting ≥ 5,000 ✓) ≈ $3.39/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 13.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~70.0% of bid side (51,110 resting ≥ 5,000 ✓) ≈ $2.69/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 15.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~67.7% of ask side (113,533 resting ≥ 5,000 ✓) ≈ $2.61/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-49` | SELL | 29.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (113,476 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (113,496 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `apdc-jerpowgov-2026-12-31` | SELL | 27.0¢ | 31 | 0 | $100.00 | ✅ scoring — ~64.6% of ask side (8,912 resting ≥ 5,000 ✓) ≈ $16.15/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 77.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~61.6% of bid side (80,583 resting ≥ 5,000 ✓) ≈ $2.57/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | SELL | 20.0¢ | 23 | 0 | $100.00 | ✅ scoring — ~56.3% of ask side (99,475 resting ≥ 5,000 ✓) ≈ $2.16/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 4.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~54.1% of ask side (117,802 resting ≥ 5,000 ✓) ≈ $2.08/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-50` | BUY | 18.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~48.2% of bid side (100,779 resting ≥ 5,000 ✓) ≈ $1.85/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte200` | SELL | 67.0¢ | 40 | 0 | $100.00 | ✅ scoring — ~48.1% of ask side (48,698 resting ≥ 5,000 ✓) ≈ $2.00/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-50` | SELL | 24.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~47.2% of ask side (98,576 resting ≥ 5,000 ✓) ≈ $1.81/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 18.0¢ | 7 | 0 | $100.00 | ✅ scoring — ~46.5% of bid side (50,368 resting ≥ 5,000 ✓) ≈ $1.79/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-gte57` | BUY | 6.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~42.6% of bid side (27,846 resting ≥ 5,000 ✓) ≈ $1.64/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 14.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~39.4% of bid side (5,843 resting ≥ 2,000 ✓) ≈ $4.93/day |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 50.0¢ | 25 | 0 | $100.00 | ✅ scoring — ~37.3% of bid side (80,525 resting ≥ 5,000 ✓) ≈ $1.55/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 49.0¢ | 115 | 1 | $100.00 | ✅ scoring — ~34.3% of bid side (80,525 resting ≥ 5,000 ✓) ≈ $1.43/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte205` | SELL | 48.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~31.7% of ask side (62,889 resting ≥ 5,000 ✓) ≈ $1.32/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte225` | SELL | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~30.2% of ask side (62,859 resting ≥ 5,000 ✓) ≈ $1.26/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 78.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~30.0% of bid side (50,380 resting ≥ 5,000 ✓) ≈ $1.25/day (pool ÷ 12 markets) |
| `pic-congress-trump-2026-12-31` | BUY | 9.0¢ | 30 | 0 | $25.00 | ✅ scoring — ~28.7% of bid side (6,928 resting ≥ 2,000 ✓) ≈ $3.59/day |
| `pandc-anydis-2027-12-31` | SELL | 25.0¢ | 10 | 0 | $50.00 | ✅ scoring — ~27.8% of ask side (10,855 resting ≥ 10,000 ✓) ≈ $3.47/day (pool ÷ 2 markets) |
| `apdc-jerpowgov-2026-12-31` | BUY | 26.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~27.8% of bid side (5,564 resting ≥ 5,000 ✓) ≈ $6.94/day (pool ÷ 2 markets) |
| `apdc-alito-2026-12-31` | BUY | 8.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~26.1% of bid side (5,315 resting ≥ 5,000 ✓) ≈ $6.53/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 75.0¢ | 21 | 2 | $100.00 | ✅ scoring — ~25.9% of bid side (80,583 resting ≥ 5,000 ✓) ≈ $1.08/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 17.0¢ | 20 | 1 | $100.00 | ✅ scoring — ~24.8% of bid side (50,368 resting ≥ 5,000 ✓) ≈ $0.95/day (pool ÷ 13 markets) |
| …and 54 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>pandc-anydis-2027-12-31</code> BUY 1 @ 21¢ → $12.38/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 1 (1 yours) | ×0.25^0 = 1.0 |
|  | 16¢ | 10 | ×0.25^5 = 0.0 |
|  | 8¢ | 101 | ×0.25^13 = 0.0 |
|  | 2¢ | 4 | ×0.25^19 = 0.0 |
|  | 1¢ | 10,986 | ×0.25^20 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.0%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 99.0% = $12.38/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte220</code> BUY 1 @ 19¢ → $4.13/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 8¢ | 100 | ×0.2^11 = 0.0 |
|  | 7¢ | 81 | ×0.2^12 = 0.0 |
|  | 3¢ | 5,247 | ×0.2^16 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 99.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 99.0% = $4.13/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-51</code> BUY 2 @ 19¢ → $3.77/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 2 (2 yours) | ×0.2^0 = 2.0 |
|  | 16¢ | 5 | ×0.2^3 = 0.0 |
|  | 5¢ | 115 | ×0.2^14 = 0.0 |
|  | 1¢ | 200,200 | ×0.2^18 = 0.0 |
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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 5 @ 9¢ → $3.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 5 (5 yours) | ×0.2^0 = 5.0 |
|  | 1¢ | 50,553 | ×0.2^8 = 0.1 |
| | | **Σ** | **5.2** |

`yours 5.0 / Σ 5.2 = 96.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 96.5% = $3.71/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> BUY 1 @ 13¢ → $3.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 7¢ | 3 | ×0.2^6 = 0.0 |
|  | 6¢ | 10,457 | ×0.2^7 = 0.1 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 88.2% = $3.39/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 20 @ 13¢ → $2.69/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 11¢ | 45 | ×0.2^2 = 1.8 |
|  | 10¢ | 845 | ×0.2^3 = 6.8 |
|  | 2¢ | 50,000 | ×0.2^11 = 0.0 |
| | | **Σ** | **28.6** |

`yours 20.0 / Σ 28.6 = 70.0%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 70.0% = $2.69/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 21 @ 15¢ → $2.61/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 31 (21 yours) | ×0.2^0 = 31.0 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^82 = 0.0 |
| | | **Σ** | **31.0** |

`yours 21.0 / Σ 31.0 = 67.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.7% = $2.61/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-49</code> SELL 20 @ 29¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 29¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 50¢ | 13 | ×0.2^21 = 0.0 |
|  | 96¢ | 25 | ×0.2^67 = 0.0 |
|  | 97¢ | 58,828 | ×0.2^68 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 20 @ 16¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 30 (20 yours) | ×0.2^0 = 30.0 |
|  | 26¢ | 0 | ×0.2^10 = 0.0 |
|  | 50¢ | 64 | ×0.2^34 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^81 = 0.0 |
| | | **Σ** | **30.0** |

`yours 20.0 / Σ 30.0 = 66.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 66.7% = $2.56/day`  

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
<details><summary><code>apdc-jerpowgov-2026-12-31</code> SELL 31 @ 27¢ → $16.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 27¢ | 48 (31 yours) | ×0.2^0 = 48.0 |
|  | 32¢ | 6 | ×0.2^5 = 0.0 |
|  | 34¢ | 30 | ×0.2^7 = 0.0 |
|  | 35¢ | 12 | ×0.2^8 = 0.0 |
|  | 42¢ | 100 | ×0.2^15 = 0.0 |
|  | 99¢ | 8,716 | ×0.2^72 = 0.0 |
| | | **Σ** | **48.0** |

`yours 31.0 / Σ 48.0 = 64.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 64.6% = $16.15/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> SELL 23 @ 20¢ → $2.16/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 34 (23 yours) | ×0.2^0 = 34.0 |
|  | 22¢ | 6 | ×0.2^2 = 0.2 |
|  | 23¢ | 829 | ×0.2^3 = 6.6 |
|  | 47¢ | 99 | ×0.2^27 = 0.0 |
|  | 50¢ | 99 | ×0.2^30 = 0.0 |
|  | 97¢ | 43,828 | ×0.2^77 = 0.0 |
| | | **Σ** | **40.9** |

`yours 23.0 / Σ 40.9 = 56.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 56.3% = $2.16/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> BUY 10 @ 18¢ → $1.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 16¢ | 200 | ×0.2^2 = 8.0 |
|  | 15¢ | 344 | ×0.2^3 = 2.8 |
|  | 2¢ | 100,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **20.8** |

`yours 10.0 / Σ 20.8 = 48.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 48.2% = $1.85/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte200</code> SELL 40 @ 67¢ → $2.00/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 67¢ | 76 (40 yours) | ×0.2^0 = 76.0 |
|  | 70¢ | 897 | ×0.2^3 = 7.2 |
|  | 90¢ | 1 | ×0.2^23 = 0.0 |
|  | 98¢ | 45,499 | ×0.2^31 = 0.0 |
| | | **Σ** | **83.2** |

`yours 40.0 / Σ 83.2 = 48.1%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 48.1% = $2.00/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-50</code> SELL 25 @ 24¢ → $1.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 52 (25 yours) | ×0.2^0 = 52.0 |
|  | 25¢ | 5 | ×0.2^1 = 1.0 |
|  | 28¢ | 4 | ×0.2^4 = 0.0 |
|  | 29¢ | 10 | ×0.2^5 = 0.0 |
|  | 50¢ | 100 | ×0.2^26 = 0.0 |
|  | 97¢ | 43,826 | ×0.2^73 = 0.0 |
| | | **Σ** | **53.0** |

`yours 25.0 / Σ 53.0 = 47.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.2% = $1.81/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 7 @ 18¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 7 (7 yours) | ×0.2^0 = 7.5 |
|  | 17¢ | 30 | ×0.2^1 = 6.0 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **16.1** |

`yours 7.5 / Σ 16.1 = 46.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 46.5% = $1.79/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 20 @ 14¢ → $4.93/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 14¢ | 42 (20 yours) | ×0.1^0 = 42.3 |
|  | 13¢ | 84 | ×0.1^1 = 8.4 |
|  | 9¢ | 67 | ×0.1^5 = 0.0 |
|  | 5¢ | 99 | ×0.1^9 = 0.0 |
|  | 3¢ | 100 | ×0.1^11 = 0.0 |
|  | 1¢ | 5,450 | ×0.1^13 = 0.0 |
| | | **Σ** | **50.7** |

`yours 20.0 / Σ 50.7 = 39.4%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 39.4% = $4.93/day`  

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 25 @ 50¢ → $1.55/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 50¢ | 30 (25 yours) | ×0.2^0 = 30.0 |
|  | 49¢ | 185 | ×0.2^1 = 37.0 |
|  | 24¢ | 170 | ×0.2^26 = 0.0 |
|  | 2¢ | 79,940 | ×0.2^48 = 0.0 |
| | | **Σ** | **67.0** |

`yours 25.0 / Σ 67.0 = 37.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 37.3% = $1.55/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 115 @ 49¢ → $1.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 50¢ | 30 | ×0.2^0 = 30.0 |
| ▶ | 49¢ | 185 (115 yours) | ×0.2^1 = 37.0 |
|  | 24¢ | 170 | ×0.2^26 = 0.0 |
|  | 2¢ | 79,940 | ×0.2^48 = 0.0 |
| | | **Σ** | **67.0** |

`yours 23.0 / Σ 67.0 = 34.3%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 34.3% = $1.43/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte205</code> SELL 20 @ 48¢ → $1.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 48¢ | 63 (20 yours) | ×0.2^0 = 63.0 |
|  | 51¢ | 1 | ×0.2^3 = 0.0 |
|  | 61¢ | 100 | ×0.2^13 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^50 = 0.0 |
| | | **Σ** | **63.0** |

`yours 20.0 / Σ 63.0 = 31.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 31.7% = $1.32/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte225</code> SELL 10 @ 12¢ → $1.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 31 (10 yours) | ×0.2^0 = 31.0 |
|  | 14¢ | 52 | ×0.2^2 = 2.1 |
|  | 20¢ | 1 | ×0.2^8 = 0.0 |
|  | 50¢ | 50 | ×0.2^38 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^86 = 0.0 |
| | | **Σ** | **33.1** |

`yours 10.0 / Σ 33.1 = 30.2%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 30.2% = $1.26/day`  

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 30 @ 78¢ → $1.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 78¢ | 80 (30 yours) | ×0.2^0 = 80.0 |
|  | 77¢ | 100 | ×0.2^1 = 20.0 |
|  | 2¢ | 50,000 | ×0.2^76 = 0.0 |
| | | **Σ** | **100.0** |

`yours 30.0 / Σ 100.0 = 30.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 30.0% = $1.25/day`  

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
<details><summary><code>pic-congress-trump-2026-12-31</code> BUY 30 @ 9¢ → $3.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 99 (30 yours) | ×0.1^0 = 99.0 |
|  | 7¢ | 280 | ×0.1^2 = 2.8 |
|  | 6¢ | 2,792 | ×0.1^3 = 2.8 |
| | | **Σ** | **104.6** |

`yours 30.0 / Σ 104.6 = 28.7%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 28.7% = $3.59/day`  

</details>
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 10 @ 25¢ → $3.47/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 36 (10 yours) | ×0.25^0 = 36.0 |
|  | 34¢ | 99 | ×0.25^9 = 0.0 |
|  | 50¢ | 19 | ×0.25^25 = 0.0 |
|  | 99¢ | 10,701 | ×0.25^74 = 0.0 |
| | | **Σ** | **36.0** |

`yours 10.0 / Σ 36.0 = 27.8%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 27.8% = $3.47/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>apdc-jerpowgov-2026-12-31</code> BUY 30 @ 26¢ → $6.94/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 96 (30 yours) | ×0.2^0 = 96.5 |
|  | 25¢ | 56 | ×0.2^1 = 11.1 |
|  | 24¢ | 12 | ×0.2^2 = 0.5 |
|  | 12¢ | 100 | ×0.2^14 = 0.0 |
|  | 2¢ | 100 | ×0.2^24 = 0.0 |
|  | 1¢ | 5,200 | ×0.2^25 = 0.0 |
| | | **Σ** | **108.1** |

`yours 30.0 / Σ 108.1 = 27.8%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 27.8% = $6.94/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-jerpowgov-2026-08-31`
2. `apdc-jerpowgov-2026-12-31` ← this one

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 30 @ 8¢ → $6.53/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 115 (30 yours) | ×0.2^0 = 114.7 |
|  | 1¢ | 5,200 | ×0.2^7 = 0.1 |
| | | **Σ** | **114.8** |

`yours 30.0 / Σ 114.8 = 26.1%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 26.1% = $6.53/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

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
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 20 @ 17¢ → $0.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 18¢ | 7 | ×0.2^0 = 7.5 |
| ▶ | 17¢ | 30 (20 yours) | ×0.2^1 = 6.0 |
|  | 16¢ | 64 | ×0.2^2 = 2.6 |
|  | 14¢ | 42 | ×0.2^4 = 0.1 |
|  | 2¢ | 50,000 | ×0.2^16 = 0.0 |
| | | **Σ** | **16.1** |

`yours 4.0 / Σ 16.1 = 24.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 24.8% = $0.95/day`  

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

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-08 | ~$111.62 | $14.73 | 13% |
| 2026-08-07 | ~$116.96 | $60.33 | 52% |
| 2026-08-06 | ~$60.78 | $52.21 | 86% |

Biggest gaps on 2026-08-08: `opdc-mcconnell-resign-2026-11-02` (est ~$9.47 → got $0.00), `pandc-anydis-2027-12-31` (est ~$5.82 → got $0.00), `scc-hrep-rep-2026-11-03-gte200` (est ~$5.15 → got $0.00)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (219,983 resting) | ~48.6% | ~$36.43 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (61,593 resting) | ~42.4% | ~$31.80 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,681 resting) | ~63.9% | ~$15.97 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,937 resting) | ~62.1% | ~$15.52 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,601 resting) | ~60.0% | ~$14.99 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (39,606 resting) | ~28.7% | ~$7.17 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,038 resting) | ~6.7% | ~$5.05 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (189,211 resting) | ~4.8% | ~$3.60 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (86,860 resting) | ~12.4% | ~$3.11 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (52,221 resting) | ~40.4% | ~$2.52 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (84,985 resting) | ~3.3% | ~$2.48 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (45,894 resting) | ~9.9% | ~$2.48 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,771.01 |
| Pending | $14.73 |
| Skipped | $1.41 |
| **Total earned** | **$1,787.15** |

1751 reward rows · 37 days with rewards · 377 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-08 | $14.73 | `██` |
| 2026-08-07 | $60.33 | `████████` |
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

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $323.83 | `████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $86.00 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `apdc-jerpowgov-2026-12-31` | $56.12 |
| `opdc-mcconnell-resign-2026-11-02` | $52.92 |
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
| 2026-08-09 9:05 PM ET | ✅ ok | 1751 | $1787.15 |
| 2026-08-09 9:03 PM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 7:51 PM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 6:53 PM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 5:51 PM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 4:55 PM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 4:48 PM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 4:22 PM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 3:51 PM ET | ✅ ok | 1749 | $1772.42 |
| 2026-08-09 3:20 PM ET | ✅ ok | 1749 | $1772.42 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
