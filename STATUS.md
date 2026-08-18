# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-18 7:32 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$163.60/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `enwc-usgubp-ok-2026-06-16-rep-gendru` — BUY at the best price, ~$23.67/day for 200 contracts. Runners-up: `enwc-usgubp-ok-2026-06-16-rep-mikmaz` (~$9.55/day), `ewc-usgub-oh-2026-11-03-dem` (~$1.95/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$163.60/day (~$6.82/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `enwc-ushrp-fl19-2026-08-18-madcaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimobe` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimobe` | SELL | 70.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (2,001 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-catlau` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-chrcol` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | BUY | 1.0¢ | 2,000 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.79/day (event pool ÷ 7 markets) |
| `enwc-ushrp-fl19-2026-08-18-johstr` | BUY | 1.0¢ | 1,994 | 0 | $25.00 | ✅ scoring — ~99.7% of bid side (2,000 resting ≥ 2,000 ✓) ≈ $1.78/day (event pool ÷ 7 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~96.8% of bid side (35,913 resting ≥ 20,000 ✓) ≈ $3.58/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | SELL | 9.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~91.5% of ask side (38,992 resting ≥ 20,000 ✓) ≈ $5.38/day (event pool ÷ 17 markets) |
| `scc-senate-gop-2026-11-03-48` | BUY | 15.0¢ | 1 | 1 | $100.00 | ✅ scoring — ~90.8% of bid side (55,508 resting ≥ 5,000 ✓) ≈ $3.49/day (event pool ÷ 13 markets) |
| `ewc-usp-2028-11-07-elomus` | BUY | 8.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~82.3% of bid side (54,000 resting ≥ 20,000 ✓) ≈ $3.05/day (event pool ÷ 27 markets) |
| `enwc-ushrp-fl19-2026-08-18-jimsch` | SELL | 95.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~72.3% of ask side (3,839 resting ≥ 2,000 ✓) ≈ $1.29/day (event pool ÷ 7 markets) |
| `enwc-uspres-nom-dem-2028-jbpri` | BUY | 9.0¢ | 19 | 0 | $200.00 | ✅ scoring — ~69.8% of bid side (141,525 resting ≥ 20,000 ✓) ≈ $4.11/day (event pool ÷ 17 markets) |
| `erac-usgubp-ak-adv-2026-08-18-despay` | BUY | 1.0¢ | 9,890 | 1 | $500.00 | ✅ scoring — ~67.6% of bid side (12,638 resting ≥ 10,000 ✓) ≈ $8.90/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-micoba` | BUY | 1.0¢ | 9,973 | 3 | $200.00 | ✅ scoring — ~48.6% of bid side (20,000 resting ≥ 20,000 ✓) ≈ $1.80/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-micoba` | BUY | 1.0¢ | 9,546 | 3 | $200.00 | ✅ scoring — ~46.5% of bid side (20,000 resting ≥ 20,000 ✓) ≈ $1.72/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jossha` | SELL | 9.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~45.6% of ask side (60,593 resting ≥ 20,000 ✓) ≈ $1.69/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 12.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~43.1% of bid side (50,219 resting ≥ 20,000 ✓) ≈ $1.60/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 12.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~43.1% of bid side (50,219 resting ≥ 20,000 ✓) ≈ $1.60/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-stasmi` | BUY | 4.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~43.0% of bid side (22,136 resting ≥ 20,000 ✓) ≈ $1.59/day (event pool ÷ 27 markets) |
| `apdc-alito-2026-12-31` | BUY | 9.0¢ | 1,000 | 0 | $100.00 | ✅ scoring — ~41.6% of bid side (23,208 resting ≥ 5,000 ✓) ≈ $10.40/day (event pool ÷ 2 markets) |
| `erac-usgubp-ak-adv-2026-08-18-shehug` | BUY | 1.0¢ | 8,774 | 0 | $500.00 | ✅ scoring — ~41.3% of bid side (21,242 resting ≥ 10,000 ✓) ≈ $5.43/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-mathei` | BUY | 1.0¢ | 9,899 | 0 | $500.00 | ✅ scoring — ~41.2% of bid side (24,055 resting ≥ 10,000 ✓) ≈ $5.41/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-tretay` | BUY | 26.0¢ | 20 | 0 | $500.00 | ✅ scoring — ~41.0% of bid side (16,549 resting ≥ 10,000 ✓) ≈ $5.39/day (event pool ÷ 19 markets) |
| `erac-usgubp-ak-adv-2026-08-18-edndev` | BUY | 1.0¢ | 9,899 | 0 | $500.00 | ✅ scoring — ~38.7% of bid side (25,571 resting ≥ 10,000 ✓) ≈ $5.09/day (event pool ÷ 19 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 8.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~33.8% of bid side (64,056 resting ≥ 20,000 ✓) ≈ $1.25/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 8.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~33.8% of bid side (64,056 resting ≥ 20,000 ✓) ≈ $1.25/day (event pool ÷ 27 markets) |
| `enwc-ushrp-fl19-2026-08-18-olahaw` | SELL | 7.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~33.3% of ask side (3,758 resting ≥ 2,000 ✓) ≈ $0.60/day (event pool ÷ 7 markets) |
| `scc-senate-gop-2026-11-03-52` | BUY | 8.0¢ | 1 | 1 | $100.00 | ✅ scoring — ~31.5% of bid side (325,747 resting ≥ 5,000 ✓) ≈ $1.21/day (event pool ÷ 13 markets) |
| …and 2052 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>enwc-ushrp-fl19-2026-08-18-madcaw</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw` ← this one
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimobe</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe` ← this one
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimobe</code> SELL 1 @ 70¢ → $1.79/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 70¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 99¢ | 2,000 | ×0.1^29 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe` ← this one
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-catlau</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau` ← this one
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw` ← this one

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-chrcol</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol` ← this one
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimsch</code> BUY 2,000 @ 1¢ → $1.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (2,000 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 2,000.0 / Σ 2,000.0 = 100.0%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 100.0% = $1.79/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch` ← this one
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-johstr</code> BUY 1,994 @ 1¢ → $1.78/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 2,000 (1,994 yours) | ×0.1^0 = 2,000.0 |
| | | **Σ** | **2,000.0** |

`yours 1,994.0 / Σ 2,000.0 = 99.7%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 99.7% = $1.78/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr` ← this one
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 135 @ 8¢ → $3.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 136 (135 yours) | ×0.2^0 = 136.0 |
|  | 6¢ | 27 | ×0.2^2 = 1.1 |
|  | 5¢ | 31 | ×0.2^3 = 0.2 |
|  | 3¢ | 3,583 | ×0.2^5 = 1.1 |
|  | 2¢ | 12,500 | ×0.2^6 = 0.8 |
|  | 1¢ | 19,636 | ×0.2^7 = 0.3 |
| | | **Σ** | **139.5** |

`yours 135.0 / Σ 139.5 = 96.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 96.8% = $3.58/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut` ← this one
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> SELL 1 @ 9¢ → $5.38/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 13¢ | 14 | ×0.2^4 = 0.0 |
|  | 14¢ | 222 | ×0.2^5 = 0.1 |
|  | 24¢ | 22,240 | ×0.2^15 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 91.5%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 91.5% = $5.38/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut` ← this one
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-48</code> BUY 1 @ 15¢ → $3.49/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 16¢ | 0 | ×0.2^0 = 0.0 |
| ▶ | 15¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 11¢ | 1 | ×0.2^5 = 0.0 |
|  | 5¢ | 1 | ×0.2^11 = 0.0 |
|  | 4¢ | 5,200 | ×0.2^12 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.2 / Σ 0.2 = 90.8%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 90.8% = $3.49/day`  

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
<details><summary><code>ewc-usp-2028-11-07-elomus</code> BUY 3 @ 8¢ → $3.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 3 (3 yours) | ×0.2^0 = 3.2 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 2 | ×0.2^6 = 0.0 |
|  | 1¢ | 53,994 | ×0.2^7 = 0.7 |
| | | **Σ** | **3.9** |

`yours 3.2 / Σ 3.9 = 82.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 82.3% = $3.05/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus` ← this one
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-jimsch</code> SELL 1 @ 95¢ → $1.29/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 99¢ | 3,838 | ×0.1^4 = 0.4 |
| | | **Σ** | **1.4** |

`yours 1.0 / Σ 1.4 = 72.3%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 72.3% = $1.29/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch` ← this one
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-jbpri</code> BUY 19 @ 9¢ → $4.11/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 20 (19 yours) | ×0.2^0 = 20.4 |
|  | 8¢ | 35 | ×0.2^1 = 7.0 |
|  | 4¢ | 110 | ×0.2^5 = 0.0 |
|  | 1¢ | 141,360 | ×0.2^8 = 0.4 |
| | | **Σ** | **27.8** |

`yours 19.4 / Σ 27.8 = 69.8%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 69.8% = $4.11/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri` ← this one
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha`
10. `enwc-uspres-nom-dem-2028-kamhar`
11. `enwc-uspres-nom-dem-2028-markel`
12. `enwc-uspres-nom-dem-2028-micoba`
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-despay</code> BUY 9,890 @ 1¢ → $8.90/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 2¢ | 498 | ×0.2^0 = 497.5 |
| ▶ | 1¢ | 12,140 (9,890 yours) | ×0.2^1 = 2,428.1 |
| | | **Σ** | **2,925.6** |

`yours 1,978.1 / Σ 2,925.6 = 67.6%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 67.6% = $8.90/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro`
7. `erac-usgubp-ak-adv-2026-08-18-despay` ← this one
8. `erac-usgubp-ak-adv-2026-08-18-edndev`
9. `erac-usgubp-ak-adv-2026-08-18-grebre`
10. `erac-usgubp-ak-adv-2026-08-18-hankro`
11. `erac-usgubp-ak-adv-2026-08-18-jesfai`
12. `erac-usgubp-ak-adv-2026-08-18-jonkre`
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg`
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei`
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-micoba</code> BUY 9,973 @ 1¢ → $1.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 4 | ×0.2^0 = 4.0 |
|  | 3¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 1¢ | 19,995 (9,973 yours) | ×0.2^3 = 160.0 |
| | | **Σ** | **164.2** |

`yours 79.8 / Σ 164.2 = 48.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 48.6% = $1.80/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba` ← this one
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-micoba</code> BUY 9,546 @ 1¢ → $1.72/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 4¢ | 4 | ×0.2^0 = 4.0 |
|  | 3¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 1¢ | 19,995 (9,546 yours) | ×0.2^3 = 160.0 |
| | | **Σ** | **164.2** |

`yours 76.4 / Σ 164.2 = 46.5%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 46.5% = $1.72/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba` ← this one
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jossha</code> SELL 3 @ 9¢ → $1.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 4 (3 yours) | ×0.2^0 = 4.0 |
|  | 13¢ | 5 | ×0.2^4 = 0.0 |
|  | 15¢ | 40,163 | ×0.2^6 = 2.6 |
| | | **Σ** | **6.6** |

`yours 3.0 / Σ 6.6 = 45.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 45.6% = $1.69/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha` ← this one
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 12¢ → $1.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 11¢ | 1 | ×0.2^1 = 0.2 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 9¢ | 5 | ×0.2^3 = 0.0 |
|  | 2¢ | 112 | ×0.2^10 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 43.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 43.1% = $1.60/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri` ← this one
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 1 @ 12¢ → $1.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 11¢ | 1 | ×0.2^1 = 0.2 |
|  | 10¢ | 2 | ×0.2^2 = 0.1 |
|  | 9¢ | 5 | ×0.2^3 = 0.0 |
|  | 2¢ | 112 | ×0.2^10 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^11 = 0.0 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 43.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 43.1% = $1.60/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri` ← this one
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-stasmi</code> BUY 135 @ 4¢ → $1.59/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 138 (135 yours) | ×0.2^0 = 138.0 |
|  | 1¢ | 21,998 | ×0.2^3 = 176.0 |
| | | **Σ** | **314.0** |

`yours 135.0 / Σ 314.0 = 43.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 43.0% = $1.59/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi` ← this one
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>apdc-alito-2026-12-31</code> BUY 1,000 @ 9¢ → $10.40/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 2,402 (1,000 yours) | ×0.2^0 = 2,402.0 |
|  | 5¢ | 501 | ×0.2^4 = 0.8 |
|  | 3¢ | 80 | ×0.2^6 = 0.0 |
|  | 2¢ | 20,000 | ×0.2^7 = 0.3 |
| | | **Σ** | **2,403.1** |

`yours 1,000.0 / Σ 2,403.1 = 41.6%`  
`$100 ÷ 2 ÷ 2 = $25.00 × 41.6% = $10.40/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `apdc-alito-2026-08-31`
2. `apdc-alito-2026-12-31` ← this one

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-shehug</code> BUY 8,774 @ 1¢ → $5.43/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 21,242 (8,774 yours) | ×0.2^0 = 21,242.2 |
| | | **Σ** | **21,242.2** |

`yours 8,774.0 / Σ 21,242.2 = 41.3%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 41.3% = $5.43/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro`
7. `erac-usgubp-ak-adv-2026-08-18-despay`
8. `erac-usgubp-ak-adv-2026-08-18-edndev`
9. `erac-usgubp-ak-adv-2026-08-18-grebre`
10. `erac-usgubp-ak-adv-2026-08-18-hankro`
11. `erac-usgubp-ak-adv-2026-08-18-jesfai`
12. `erac-usgubp-ak-adv-2026-08-18-jonkre`
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg`
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei`
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug` ← this one
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-mathei</code> BUY 9,899 @ 1¢ → $5.41/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 24,055 (9,899 yours) | ×0.2^0 = 24,054.9 |
| | | **Σ** | **24,054.9** |

`yours 9,899.1 / Σ 24,054.9 = 41.2%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 41.2% = $5.41/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro`
7. `erac-usgubp-ak-adv-2026-08-18-despay`
8. `erac-usgubp-ak-adv-2026-08-18-edndev`
9. `erac-usgubp-ak-adv-2026-08-18-grebre`
10. `erac-usgubp-ak-adv-2026-08-18-hankro`
11. `erac-usgubp-ak-adv-2026-08-18-jesfai`
12. `erac-usgubp-ak-adv-2026-08-18-jonkre`
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg`
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei` ← this one
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-tretay</code> BUY 20 @ 26¢ → $5.39/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 49 (20 yours) | ×0.2^0 = 48.8 |
|  | 4¢ | 6,250 | ×0.2^22 = 0.0 |
|  | 3¢ | 250 | ×0.2^23 = 0.0 |
|  | 1¢ | 10,000 | ×0.2^25 = 0.0 |
| | | **Σ** | **48.8** |

`yours 20.0 / Σ 48.8 = 41.0%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 41.0% = $5.39/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro`
7. `erac-usgubp-ak-adv-2026-08-18-despay`
8. `erac-usgubp-ak-adv-2026-08-18-edndev`
9. `erac-usgubp-ak-adv-2026-08-18-grebre`
10. `erac-usgubp-ak-adv-2026-08-18-hankro`
11. `erac-usgubp-ak-adv-2026-08-18-jesfai`
12. `erac-usgubp-ak-adv-2026-08-18-jonkre`
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg`
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei`
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay` ← this one

</details>

</details>
<details><summary><code>erac-usgubp-ak-adv-2026-08-18-edndev</code> BUY 9,899 @ 1¢ → $5.09/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 25,571 (9,899 yours) | ×0.2^0 = 25,570.9 |
| | | **Σ** | **25,570.9** |

`yours 9,899.1 / Σ 25,570.9 = 38.7%`  
`$500 ÷ 19 ÷ 2 = $13.16 × 38.7% = $5.09/day`  

<details><summary>÷ 19 markets in this race — tap to list</summary>

1. `erac-usgubp-ak-adv-2026-08-18-adacru`
2. `erac-usgubp-ak-adv-2026-08-18-berwil`
3. `erac-usgubp-ak-adv-2026-08-18-bilwal`
4. `erac-usgubp-ak-adv-2026-08-18-bruwal`
5. `erac-usgubp-ak-adv-2026-08-18-clibis`
6. `erac-usgubp-ak-adv-2026-08-18-davbro`
7. `erac-usgubp-ak-adv-2026-08-18-despay`
8. `erac-usgubp-ak-adv-2026-08-18-edndev` ← this one
9. `erac-usgubp-ak-adv-2026-08-18-grebre`
10. `erac-usgubp-ak-adv-2026-08-18-hankro`
11. `erac-usgubp-ak-adv-2026-08-18-jesfai`
12. `erac-usgubp-ak-adv-2026-08-18-jonkre`
13. `erac-usgubp-ak-adv-2026-08-18-lesmcg`
14. `erac-usgubp-ak-adv-2026-08-18-matcla`
15. `erac-usgubp-ak-adv-2026-08-18-mathei`
16. `erac-usgubp-ak-adv-2026-08-18-nandah`
17. `erac-usgubp-ak-adv-2026-08-18-shehug`
18. `erac-usgubp-ak-adv-2026-08-18-tombeg`
19. `erac-usgubp-ak-adv-2026-08-18-tretay`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 1 @ 8¢ → $1.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (1 yours) | ×0.2^0 = 2.1 |
|  | 5¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 3¢ | 1 | ×0.2^5 = 0.0 |
|  | 2¢ | 30 | ×0.2^6 = 0.0 |
|  | 1¢ | 64,021 | ×0.2^7 = 0.8 |
| | | **Σ** | **3.0** |

`yours 1.0 / Σ 3.0 = 33.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 33.8% = $1.25/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram` ← this one
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 1 @ 8¢ → $1.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 2 (1 yours) | ×0.2^0 = 2.1 |
|  | 5¢ | 1 | ×0.2^3 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 3¢ | 1 | ×0.2^5 = 0.0 |
|  | 2¢ | 30 | ×0.2^6 = 0.0 |
|  | 1¢ | 64,021 | ×0.2^7 = 0.8 |
| | | **Σ** | **3.0** |

`yours 1.0 / Σ 3.0 = 33.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 33.8% = $1.25/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal`
10. `ewc-usp-2028-11-07-jbpri`
11. `ewc-usp-2028-11-07-jdvan`
12. `ewc-usp-2028-11-07-jonoss`
13. `ewc-usp-2028-11-07-jossha`
14. `ewc-usp-2028-11-07-kamhar`
15. `ewc-usp-2028-11-07-markel`
16. `ewc-usp-2028-11-07-marrub`
17. `ewc-usp-2028-11-07-micoba`
18. `ewc-usp-2028-11-07-petbut`
19. `ewc-usp-2028-11-07-rahema`
20. `ewc-usp-2028-11-07-rokha`
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram` ← this one
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>enwc-ushrp-fl19-2026-08-18-olahaw</code> SELL 1 @ 7¢ → $0.60/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 3 (1 yours) | ×0.1^0 = 3.0 |
|  | 12¢ | 74 | ×0.1^5 = 0.0 |
|  | 99¢ | 3,681 | ×0.1^92 = 0.0 |
| | | **Σ** | **3.0** |

`yours 1.0 / Σ 3.0 = 33.3%`  
`$25 ÷ 7 ÷ 2 = $1.79 × 33.3% = $0.60/day`  

<details><summary>÷ 7 markets in this race — tap to list</summary>

1. `enwc-ushrp-fl19-2026-08-18-catlau`
2. `enwc-ushrp-fl19-2026-08-18-chrcol`
3. `enwc-ushrp-fl19-2026-08-18-jimobe`
4. `enwc-ushrp-fl19-2026-08-18-jimsch`
5. `enwc-ushrp-fl19-2026-08-18-johstr`
6. `enwc-ushrp-fl19-2026-08-18-madcaw`
7. `enwc-ushrp-fl19-2026-08-18-olahaw` ← this one

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-52</code> BUY 1 @ 8¢ → $1.21/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 0 | ×0.2^0 = 0.1 |
| ▶ | 8¢ | 1 (1 yours) | ×0.2^1 = 0.2 |
|  | 7¢ | 1 | ×0.2^2 = 0.0 |
|  | 5¢ | 1 | ×0.2^4 = 0.0 |
|  | 4¢ | 4 | ×0.2^5 = 0.0 |
|  | 3¢ | 2 | ×0.2^6 = 0.0 |
|  | 2¢ | 25,187 | ×0.2^7 = 0.3 |
| | | **Σ** | **0.6** |

`yours 0.2 / Σ 0.6 = 31.5%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 31.5% = $1.21/day`  

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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (26,927 resting) | ~94.7% | ~$23.67 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (60,049 resting) | ~38.2% | ~$9.55 |
| `ewc-usgub-oh-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (289,700 resting) | ~2.6% | ~$1.95 |
| `ewc-usse-oh-2026-11-03-rep` | $100.00 ÷ 2 | 0.20 | 5,000 | BUY side (632,544 resting) | ~6.2% | ~$1.56 |
| `ewc-usgub-oh-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (295,872 resting) | ~2.0% | ~$1.47 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,926 resting) | ~5.4% | ~$1.35 |
| `ewc-usgub-ks-2026-11-03-rep` | $25.00 ÷ 2 | 0.10 | 2,000 | BUY side (90,483 resting) | ~19.4% | ~$1.21 |
| `ewc-usgub-ga-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (84,254 resting) | ~1.6% | ~$1.16 |
| `ewc-usgub-ca-2026-11-03-stehil` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (76,498 resting) | ~1.5% | ~$1.13 |
| `ewc-usgub-ga-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | SELL side (94,775 resting) | ~1.4% | ~$1.02 |
| `enwc-usgubp-fl-2026-08-18-rep-byrdon` | $500.00 ÷ 3 | 0.20 | 10,000 | BUY side (670,644 resting) | ~1.2% | ~$1.01 |
| `ewc-usse-nc-2026-11-03-dem` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (55,034 resting) | ~3.3% | ~$0.82 |

## Totals

| | Amount |
|---|---:|
| Paid | $4,919.08 |
| Pending | $197.10 |
| Skipped | $1.41 |
| **Total earned** | **$5,117.59** |

2859 reward rows · 45 days with rewards · 559 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
| 2026-08-16 ⚠️ multi-day pending bucket | $197.03 | `███` |
| 2026-08-15 | $1,352.63 | `████████████████████` |
| 2026-08-14 | $274.92 | `████` |
| 2026-08-13 | $223.24 | `███` |
| 2026-08-12 | $213.04 | `███` |
| 2026-08-11 | $409.60 | `██████` |
| 2026-08-10 | $557.62 | `████████` |
| 2026-08-09 | $62.24 | `█` |
| 2026-08-08 | $54.83 | `█` |
| 2026-08-07 | $60.34 | `█` |
| 2026-08-06 | $52.22 | `█` |
| 2026-08-05 | $31.46 | `█` |
| 2026-08-04 | $53.94 | `█` |
| 2026-08-03 | $44.81 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-08 | $3,654.27 | `████████████████████` |
| 2026-07 | $1,463.32 | `████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `apdc-jerpowgov-2026-12-31` | $178.70 |
| `apdc-alito-2026-12-31` | $115.00 |
| `ewc-usp-party-2028-11-07-rep` | $100.01 |
| `ewc-usp-party-2028-11-07-dem` | $79.48 |
| `opdc-mcconnell-resign-2026-11-02` | $79.41 |
| `pntcbk-wnba-freedom-2027-06-30-enekan` | $66.06 |
| `pntcbk-wnba-white-2027-06-30-roywhi` | $63.61 |
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $62.45 |
| `pandc-anydis-2027-12-31` | $62.40 |
| `enwc-uspres-nom-rep-2028-rondes` | $48.49 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.60 |
| `enwc-uspres-nom-dem-2028-stasmi` | $44.12 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `scc-hrep-rep-2026-11-03-gte200` | $41.51 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $39.04 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-08-18 7:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 6:22 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 5:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 4:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 3:39 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 2:53 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 1:52 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-18 12:52 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-17 8:50 PM ET | ✅ ok | 2700 | $4920.49 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
