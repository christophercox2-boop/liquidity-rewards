# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-08-10 11:26 AM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$248.40/day estimated (ceiling, not promise — details below)

**Earned:** $1,827.20 lifetime ($1,771.01 paid). Last three recorded days — 2026-08-08: **$54.78** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-07: **$60.33** · 2026-08-06: **$52.21** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `ewc-usgub-ca-2026-11-03-stehil` — SELL at the best price, ~$24.87/day for 200 contracts. Runners-up: `ewc-usgub-ga-2026-11-03-rep` (~$18.89/day), `apdc-jerpowgov-2026-08-31` (~$15.11/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$248.40/day (~$10.35/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ussep-sc-2026-08-11-rep-ralnor` | SELL | 25.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,179 resting ≥ 2,000 ✓) ≈ $1.04/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte195` | BUY | 55.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~99.8% of bid side (80,765 resting ≥ 5,000 ✓) ≈ $4.16/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte220` | BUY | 19.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~99.0% of bid side (85,729 resting ≥ 5,000 ✓) ≈ $4.13/day (pool ÷ 12 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | BUY | 10.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~98.0% of bid side (80,560 resting ≥ 5,000 ✓) ≈ $4.08/day (pool ÷ 12 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 9.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~96.5% of bid side (50,558 resting ≥ 5,000 ✓) ≈ $3.71/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | BUY | 12.0¢ | 20 | 0 | $25.00 | ✅ scoring — ~93.5% of bid side (5,785 resting ≥ 2,000 ✓) ≈ $11.68/day |
| `scc-senate-gop-2026-11-03-53` | BUY | 13.0¢ | 1 | 0 | $100.00 | ✅ scoring — ~88.2% of bid side (10,712 resting ≥ 5,000 ✓) ≈ $3.39/day (pool ÷ 13 markets) |
| `opdc-mcconnell-resign-2026-11-02` | SELL | 16.0¢ | 34 | 0 | $25.00 | ✅ scoring — ~82.5% of ask side (4,331 resting ≥ 2,000 ✓) ≈ $10.32/day |
| `ussewc-usse-tn-2026-11-03-rep` | BUY | 82.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~80.0% of bid side (2,340 resting ≥ 2,000 ✓) ≈ $5.00/day (pool ÷ 2 markets) |
| `ussewc-usse-wy-2026-11-03-rep` | SELL | 99.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~70.8% of ask side (2,825 resting ≥ 2,000 ✓) ≈ $4.42/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte210` | SELL | 42.0¢ | 21 | 0 | $100.00 | ✅ scoring — ~67.7% of ask side (62,857 resting ≥ 5,000 ✓) ≈ $2.82/day (pool ÷ 12 markets) |
| `pandc-anydis-2027-12-31` | SELL | 24.0¢ | 20 | 0 | $50.00 | ✅ scoring — ~67.7% of ask side (10,856 resting ≥ 10,000 ✓) ≈ $8.46/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-49` | BUY | 13.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~67.7% of bid side (51,235 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-52` | SELL | 15.0¢ | 8 | 0 | $100.00 | ✅ scoring — ~67.5% of ask side (113,514 resting ≥ 5,000 ✓) ≈ $2.60/day (pool ÷ 13 markets) |
| `ussewc-usse-ar-2026-11-03-rep` | BUY | 88.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (2,310 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-rep` | BUY | 98.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (2,310 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `ussewc-usse-fl-2026-11-03-rep` | BUY | 77.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (2,310 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `ussewc-usse-ms-2026-11-03-dem` | SELL | 19.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~66.7% of ask side (2,300 resting ≥ 2,000 ✓) ≈ $4.17/day (pool ÷ 2 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 16.0¢ | 20 | 0 | $100.00 | ✅ scoring — ~66.7% of ask side (113,496 resting ≥ 5,000 ✓) ≈ $2.56/day (pool ÷ 13 markets) |
| `scc-hrep-rep-2026-11-03-gte190` | BUY | 71.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (80,181 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `ussewc-usse-mt-2026-11-03-rep` | BUY | 75.0¢ | 50 | 0 | $25.00 | ✅ scoring — ~66.7% of bid side (4,365 resting ≥ 2,000 ✓) ≈ $2.78/day (pool ÷ 3 markets) |
| `scc-hrep-rep-2026-11-03-gte180` | BUY | 82.0¢ | 30 | 0 | $100.00 | ✅ scoring — ~66.7% of bid side (50,501 resting ≥ 5,000 ✓) ≈ $2.78/day (pool ÷ 12 markets) |
| `ussewc-usse-nm-2026-11-03-rep` | SELL | 21.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~63.4% of ask side (2,518 resting ≥ 2,000 ✓) ≈ $3.97/day (pool ÷ 2 markets) |
| `ussewc-usse-wv-2026-11-03-dem` | SELL | 23.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~63.1% of ask side (2,522 resting ≥ 2,000 ✓) ≈ $3.95/day (pool ÷ 2 markets) |
| `ussewc-usse-va-2026-11-03-rep` | SELL | 25.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~63.0% of ask side (2,500 resting ≥ 2,000 ✓) ≈ $3.94/day (pool ÷ 2 markets) |
| `ussewc-usse-ok-2026-11-03-dem` | SELL | 28.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~62.5% of ask side (2,545 resting ≥ 2,000 ✓) ≈ $3.91/day (pool ÷ 2 markets) |
| `scc-hrep-rep-2026-11-03-gte185` | BUY | 77.0¢ | 2 | 0 | $100.00 | ✅ scoring — ~61.6% of bid side (80,583 resting ≥ 5,000 ✓) ≈ $2.57/day (pool ÷ 12 markets) |
| `ussewc-usse-sc-2026-11-03-rep` | BUY | 77.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.5% of bid side (2,265 resting ≥ 2,000 ✓) ≈ $3.85/day (pool ÷ 2 markets) |
| `ussewc-usse-al-2026-11-03-dem` | SELL | 35.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~61.0% of ask side (2,521 resting ≥ 2,000 ✓) ≈ $3.81/day (pool ÷ 2 markets) |
| `ussewc-usse-or-2026-11-03-rep` | SELL | 39.0¢ | 40 | 0 | $25.00 | ✅ scoring — ~60.1% of ask side (2,531 resting ≥ 2,000 ✓) ≈ $3.75/day (pool ÷ 2 markets) |
| …and 193 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ussep-sc-2026-08-11-rep-ralnor</code> SELL 10 @ 25¢ → $1.04/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 10 (10 yours) | ×0.1^0 = 10.0 |
|  | 29¢ | 20 | ×0.1^4 = 0.0 |
|  | 30¢ | 40 | ×0.1^5 = 0.0 |
|  | 35¢ | 100 | ×0.1^10 = 0.0 |
|  | 36¢ | 11 | ×0.1^11 = 0.0 |
|  | 38¢ | 4 | ×0.1^13 = 0.0 |
|  | 40¢ | 105 | ×0.1^15 = 0.0 |
|  | 43¢ | 6 | ×0.1^18 = 0.0 |
|  | 50¢ | 25 | ×0.1^25 = 0.0 |
|  | 99¢ | 1,858 | ×0.1^74 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 100.0%`  
`$25 ÷ 12 ÷ 2 = $1.04 × 100.0% = $1.04/day`  

<details><summary>÷ 12 markets in this race — tap to list</summary>

1. `enwc-ussep-sc-2026-08-11-rep-alawil`
2. `enwc-ussep-sc-2026-08-11-rep-andbau`
3. `enwc-ussep-sc-2026-08-11-rep-darnor`
4. `enwc-ussep-sc-2026-08-11-rep-joewil`
5. `enwc-ussep-sc-2026-08-11-rep-marlyn`
6. `enwc-ussep-sc-2026-08-11-rep-nanmac`
7. `enwc-ussep-sc-2026-08-11-rep-pameve`
8. `enwc-ussep-sc-2026-08-11-rep-paudan`
9. `enwc-ussep-sc-2026-08-11-rep-ralnor` ← this one
10. `enwc-ussep-sc-2026-08-11-rep-rusfry`
11. `enwc-ussep-sc-2026-08-11-rep-tregow`
12. `enwc-ussep-sc-2026-08-11-rep-wiltim`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte195</code> BUY 10 @ 55¢ → $4.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 55¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 50¢ | 30 | ×0.2^5 = 0.0 |
|  | 49¢ | 165 | ×0.2^6 = 0.0 |
|  | 24¢ | 170 | ×0.2^31 = 0.0 |
|  | 2¢ | 80,190 | ×0.2^53 = 0.0 |
| | | **Σ** | **10.0** |

`yours 10.0 / Σ 10.0 = 99.8%`  
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
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> BUY 10 @ 10¢ → $4.08/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 10 (10 yours) | ×0.2^0 = 10.0 |
|  | 3¢ | 100 | ×0.2^7 = 0.0 |
|  | 2¢ | 80,250 | ×0.2^8 = 0.2 |
| | | **Σ** | **10.2** |

`yours 10.0 / Σ 10.2 = 98.0%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 98.0% = $4.08/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> BUY 20 @ 12¢ → $11.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 20 (20 yours) | ×0.1^0 = 20.0 |
|  | 11¢ | 6 | ×0.1^1 = 0.6 |
|  | 10¢ | 80 | ×0.1^2 = 0.8 |
|  | 6¢ | 30 | ×0.1^6 = 0.0 |
|  | 5¢ | 99 | ×0.1^7 = 0.0 |
|  | 3¢ | 100 | ×0.1^9 = 0.0 |
|  | 1¢ | 5,450 | ×0.1^11 = 0.0 |
| | | **Σ** | **21.4** |

`yours 20.0 / Σ 21.4 = 93.5%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 93.5% = $11.68/day`  

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
<details><summary><code>opdc-mcconnell-resign-2026-11-02</code> SELL 34 @ 16¢ → $10.32/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 34 (34 yours) | ×0.1^0 = 34.0 |
|  | 17¢ | 72 | ×0.1^1 = 7.2 |
|  | 22¢ | 82 | ×0.1^6 = 0.0 |
|  | 23¢ | 30 | ×0.1^7 = 0.0 |
|  | 24¢ | 99 | ×0.1^8 = 0.0 |
|  | 35¢ | 101 | ×0.1^19 = 0.0 |
|  | 99¢ | 3,913 | ×0.1^83 = 0.0 |
| | | **Σ** | **41.2** |

`yours 34.0 / Σ 41.2 = 82.5%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 82.5% = $10.32/day`  

</details>
<details><summary><code>ussewc-usse-tn-2026-11-03-rep</code> BUY 40 @ 82¢ → $5.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 81¢ | 100 | ×0.1^1 = 10.0 |
|  | 1¢ | 2,200 | ×0.1^81 = 0.0 |
| | | **Σ** | **50.0** |

`yours 40.0 / Σ 50.0 = 80.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 80.0% = $5.00/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-tn-2026-11-03-dem`
2. `ussewc-usse-tn-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wy-2026-11-03-rep</code> SELL 2,000 @ 99¢ → $4.42/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 99¢ | 2,825 (2,000 yours) | ×0.1^0 = 2,825.0 |
| | | **Σ** | **2,825.0** |

`yours 2,000.0 / Σ 2,825.0 = 70.8%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 70.8% = $4.42/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wy-2026-11-03-dem`
2. `ussewc-usse-wy-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte210</code> SELL 21 @ 42¢ → $2.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 42¢ | 31 (21 yours) | ×0.2^0 = 31.0 |
|  | 50¢ | 100 | ×0.2^8 = 0.0 |
|  | 52¢ | 1 | ×0.2^10 = 0.0 |
|  | 64¢ | 0 | ×0.2^22 = 0.0 |
|  | 72¢ | 0 | ×0.2^30 = 0.0 |
|  | 98¢ | 60,499 | ×0.2^56 = 0.0 |
| | | **Σ** | **31.0** |

`yours 21.0 / Σ 31.0 = 67.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 67.7% = $2.82/day`  

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
<details><summary><code>pandc-anydis-2027-12-31</code> SELL 20 @ 24¢ → $8.46/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 24¢ | 27 (20 yours) | ×0.25^0 = 26.9 |
|  | 25¢ | 10 | ×0.25^1 = 2.5 |
|  | 34¢ | 99 | ×0.25^10 = 0.0 |
|  | 50¢ | 19 | ×0.25^26 = 0.0 |
|  | 99¢ | 10,701 | ×0.25^75 = 0.0 |
| | | **Σ** | **29.4** |

`yours 19.9 / Σ 29.4 = 67.7%`  
`$50 ÷ 2 ÷ 2 = $12.50 × 67.7% = $8.46/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `pandc-anydis-2026-12-31`
2. `pandc-anydis-2027-12-31` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-49</code> BUY 20 @ 13¢ → $2.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 20 (20 yours) | ×0.2^0 = 20.0 |
|  | 11¢ | 45 | ×0.2^2 = 1.8 |
|  | 10¢ | 970 | ×0.2^3 = 7.8 |
|  | 2¢ | 50,000 | ×0.2^11 = 0.0 |
| | | **Σ** | **29.6** |

`yours 20.0 / Σ 29.6 = 67.7%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.7% = $2.60/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-52</code> SELL 8 @ 15¢ → $2.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 12 (8 yours) | ×0.2^0 = 12.3 |
|  | 50¢ | 100 | ×0.2^35 = 0.0 |
|  | 97¢ | 58,824 | ×0.2^82 = 0.0 |
| | | **Σ** | **12.3** |

`yours 8.3 / Σ 12.3 = 67.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 67.5% = $2.60/day`  

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
<details><summary><code>ussewc-usse-ar-2026-11-03-rep</code> BUY 40 @ 88¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 88¢ | 60 (40 yours) | ×0.1^0 = 60.0 |
|  | 50¢ | 50 | ×0.1^38 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^87 = 0.0 |
| | | **Σ** | **60.0** |

`yours 40.0 / Σ 60.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ar-2026-11-03-dem`
2. `ussewc-usse-ar-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-rep</code> BUY 40 @ 98¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 98¢ | 60 (40 yours) | ×0.1^0 = 60.0 |
|  | 50¢ | 50 | ×0.1^48 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^97 = 0.0 |
| | | **Σ** | **60.0** |

`yours 40.0 / Σ 60.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem`
2. `ussewc-usse-al-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-fl-2026-11-03-rep</code> BUY 40 @ 77¢ → $4.17/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 60 (40 yours) | ×0.1^0 = 60.0 |
|  | 50¢ | 50 | ×0.1^27 = 0.0 |
|  | 1¢ | 2,200 | ×0.1^76 = 0.0 |
| | | **Σ** | **60.0** |

`yours 40.0 / Σ 60.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-fl-2026-11-03-dem`
2. `ussewc-usse-fl-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ms-2026-11-03-dem</code> SELL 50 @ 19¢ → $4.17/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 75 (50 yours) | ×0.1^0 = 75.0 |
|  | 99¢ | 2,225 | ×0.1^80 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 66.7% = $4.17/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ms-2026-11-03-dem` ← this one
2. `ussewc-usse-ms-2026-11-03-rep`

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
<details><summary><code>scc-hrep-rep-2026-11-03-gte190</code> BUY 10 @ 71¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 71¢ | 15 (10 yours) | ×0.2^0 = 15.0 |
|  | 64¢ | 0 | ×0.2^7 = 0.0 |
|  | 3¢ | 33 | ×0.2^68 = 0.0 |
|  | 2¢ | 79,933 | ×0.2^69 = 0.0 |
| | | **Σ** | **15.0** |

`yours 10.0 / Σ 15.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>ussewc-usse-mt-2026-11-03-rep</code> BUY 50 @ 75¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 75¢ | 75 (50 yours) | ×0.1^0 = 75.0 |
|  | 70¢ | 40 | ×0.1^5 = 0.0 |
|  | 48¢ | 50 | ×0.1^27 = 0.0 |
|  | 1¢ | 4,200 | ×0.1^74 = 0.0 |
| | | **Σ** | **75.0** |

`yours 50.0 / Σ 75.0 = 66.7%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `ussewc-usse-mt-2026-11-03-dem`
2. `ussewc-usse-mt-2026-11-03-rep` ← this one
3. `ussewc-usse-mt-2026-11-03-setbod`

</details>

</details>
<details><summary><code>scc-hrep-rep-2026-11-03-gte180</code> BUY 30 @ 82¢ → $2.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 82¢ | 45 (30 yours) | ×0.2^0 = 45.0 |
|  | 76¢ | 6 | ×0.2^6 = 0.0 |
|  | 2¢ | 50,250 | ×0.2^80 = 0.0 |
| | | **Σ** | **45.0** |

`yours 30.0 / Σ 45.0 = 66.7%`  
`$100 ÷ 12 ÷ 2 = $4.17 × 66.7% = $2.78/day`  

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
<details><summary><code>ussewc-usse-nm-2026-11-03-rep</code> SELL 40 @ 21¢ → $3.97/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 21¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 22¢ | 228 | ×0.1^1 = 22.8 |
|  | 23¢ | 25 | ×0.1^2 = 0.3 |
|  | 99¢ | 2,225 | ×0.1^78 = 0.0 |
| | | **Σ** | **63.1** |

`yours 40.0 / Σ 63.1 = 63.4%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.4% = $3.97/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-nm-2026-11-03-dem`
2. `ussewc-usse-nm-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-wv-2026-11-03-dem</code> SELL 40 @ 23¢ → $3.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 23¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 24¢ | 231 | ×0.1^1 = 23.1 |
|  | 25¢ | 26 | ×0.1^2 = 0.3 |
|  | 99¢ | 2,225 | ×0.1^76 = 0.0 |
| | | **Σ** | **63.4** |

`yours 40.0 / Σ 63.4 = 63.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.1% = $3.95/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-wv-2026-11-03-dem` ← this one
2. `ussewc-usse-wv-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-va-2026-11-03-rep</code> SELL 40 @ 25¢ → $3.94/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 26¢ | 235 | ×0.1^1 = 23.5 |
|  | 99¢ | 2,225 | ×0.1^74 = 0.0 |
| | | **Σ** | **63.5** |

`yours 40.0 / Σ 63.5 = 63.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 63.0% = $3.94/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-va-2026-11-03-dem`
2. `ussewc-usse-va-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-ok-2026-11-03-dem</code> SELL 40 @ 28¢ → $3.91/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 28¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 29¢ | 240 | ×0.1^1 = 24.0 |
|  | 51¢ | 40 | ×0.1^23 = 0.0 |
|  | 99¢ | 2,225 | ×0.1^71 = 0.0 |
| | | **Σ** | **64.0** |

`yours 40.0 / Σ 64.0 = 62.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 62.5% = $3.91/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-ok-2026-11-03-dem` ← this one
2. `ussewc-usse-ok-2026-11-03-rep`

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
<details><summary><code>ussewc-usse-sc-2026-11-03-rep</code> BUY 40 @ 77¢ → $3.85/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 65 (40 yours) | ×0.1^0 = 65.0 |
|  | 1¢ | 2,200 | ×0.1^76 = 0.0 |
| | | **Σ** | **65.0** |

`yours 40.0 / Σ 65.0 = 61.5%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.5% = $3.85/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-sc-2026-11-03-dem`
2. `ussewc-usse-sc-2026-11-03-rep` ← this one

</details>

</details>
<details><summary><code>ussewc-usse-al-2026-11-03-dem</code> SELL 40 @ 35¢ → $3.81/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 35¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 36¢ | 256 | ×0.1^1 = 25.6 |
|  | 99¢ | 2,225 | ×0.1^64 = 0.0 |
| | | **Σ** | **65.6** |

`yours 40.0 / Σ 65.6 = 61.0%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 61.0% = $3.81/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-al-2026-11-03-dem` ← this one
2. `ussewc-usse-al-2026-11-03-rep`

</details>

</details>
<details><summary><code>ussewc-usse-or-2026-11-03-rep</code> SELL 40 @ 39¢ → $3.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 39¢ | 40 (40 yours) | ×0.1^0 = 40.0 |
|  | 40¢ | 266 | ×0.1^1 = 26.6 |
|  | 99¢ | 2,225 | ×0.1^60 = 0.0 |
| | | **Σ** | **66.6** |

`yours 40.0 / Σ 66.6 = 60.1%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 60.1% = $3.75/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `ussewc-usse-or-2026-11-03-dem`
2. `ussewc-usse-or-2026-11-03-rep` ← this one

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-weighted estimate for each day (each hourly snapshot's rate counts for the time until the next one) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. The dashboard's Tracked column is the finer-grained official figure and can differ a little — it samples every 30 seconds. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-08-07 | ~$116.96 | $60.33 | 52% |
| 2026-08-06 | ~$60.78 | $52.21 | 86% |
| 2026-08-05 | ~$33.74 | $31.46 | 93% |

Biggest gaps on 2026-08-07: `opdc-mcconnell-resign-2026-11-02` (est ~$17.07 → got $5.10), `scc-hrep-rep-2026-11-03-gte205` (est ~$4.14 → got $0.00), `scc-hrep-rep-2026-11-03-gte195` (est ~$5.07 → got $0.94)

_2026-08-08 is excluded: since the program restructure, pending rewards accumulate under that one date (its total keeps growing day over day), so it can't be compared against a single day's estimate until it's finalized._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (249,191 resting) | ~33.2% | ~$24.87 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (60,977 resting) | ~25.2% | ~$18.89 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,699 resting) | ~60.4% | ~$15.11 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,610 resting) | ~58.8% | ~$14.69 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (45,734 resting) | ~57.3% | ~$14.32 |
| `ewc-usgub-ca-2026-11-03-xavbec` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (375,816 resting) | ~18.9% | ~$14.21 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (77,510 resting) | ~45.9% | ~$11.48 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (67,200 resting) | ~6.3% | ~$4.75 |
| `ewc-usse-oh-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (84,644 resting) | ~13.2% | ~$3.30 |
| `ewc-usgub-ia-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (63,307 resting) | ~47.5% | ~$2.97 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (86,788 resting) | ~3.2% | ~$2.41 |
| `ewc-usse-me-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (191,255 resting) | ~3.0% | ~$2.28 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,771.01 |
| Pending | $54.78 |
| Skipped | $1.41 |
| **Total earned** | **$1,827.20** |

1783 reward rows · 37 days with rewards · 377 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-08 ⚠️ multi-day pending bucket | $54.78 | `███████` |
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
| 2026-08 | $363.88 | `█████` |
| 2026-07 | $1,463.32 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-alito-2026-12-31` | $86.00 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `opdc-mcconnell-resign-2026-11-02` | $56.71 |
| `apdc-jerpowgov-2026-12-31` | $56.12 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.36 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.92 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.12 |
| `scc-hrep-rep-2026-11-03-gte200` | $32.74 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $29.75 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $29.31 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $28.66 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.77 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $25.76 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-10 11:26 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 10:59 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 10:58 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 10:53 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 9:48 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 8:02 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 6:38 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 4:53 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 2:44 AM ET | ✅ ok | 1783 | $1827.20 |
| 2026-08-10 12:58 AM ET | ✅ ok | 1783 | $1827.20 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
