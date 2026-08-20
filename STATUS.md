# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 11:41 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$148.84/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `dipcc-us-iran-contnts-2026--irnfnd` — BUY at the best price, ~$6.24/day for 200 contracts. Runners-up: `dipcc-us-iran-contnts-2026--dilut` (~$6.22/day), `dipcc-us-iran-contnts-2026--enrcaplte5` (~$6.22/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$148.84/day (~$6.20/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `aachc-cfb-wins-2026-11-28-usc-7pt5wins` | SELL | 61.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~97.7% of the ask side — holding the estimate until I know how many markets share this pool |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 86 | 0 | $200.00 | ✅ scoring — ~97.7% of ask side (44,789 resting ≥ 20,000 ✓) ≈ $6.98/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~93.6% of bid side (50,355 resting ≥ 20,000 ✓) ≈ $3.47/day (event pool ÷ 27 markets) |
| `aachc-cfb-wins-2026-11-28-uk-5pt5wins` | BUY | 43.0¢ | 2 | 0 | $25.00 | ⏳ scoring ~88.3% of the bid side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-uk-6pt5wins` | SELL | 22.0¢ | 10 | 0 | $25.00 | ⏳ scoring ~86.8% of the ask side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-txtech-10pt5wins` | BUY | 65.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~84.5% of the bid side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-aubrn-4pt5wins` | SELL | 77.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~84.5% of ask side (384,472 resting ≥ 5,000 ✓) ≈ $2.11/day (event pool ÷ 5 markets) |
| `aachc-cfb-wins-2026-11-28-ga-8pt5wins` | SELL | 72.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~82.2% of the ask side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-mich-8pt5wins` | BUY | 47.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~81.1% of the bid side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-miss-6pt5wins` | SELL | 71.0¢ | 0 | 1 | $25.00 | ⏳ scoring ~79.7% of the ask side — holding the estimate until I know how many markets share this pool |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 120 | 0 | $200.00 | ✅ scoring — ~77.1% of bid side (20,574 resting ≥ 20,000 ✓) ≈ $2.86/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 7.0¢ | 83 | 0 | $200.00 | ✅ scoring — ~75.7% of bid side (36,178 resting ≥ 20,000 ✓) ≈ $2.80/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | SELL | 16.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~74.3% of ask side (38,742 resting ≥ 20,000 ✓) ≈ $4.37/day (event pool ÷ 17 markets) |
| `aachc-cfb-wins-2026-11-28-clmsn-5pt5wins` | BUY | 79.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~71.9% of the bid side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-ohiost-11pt5wins` | SELL | 15.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~69.2% of the ask side — holding the estimate until I know how many markets share this pool |
| `ewc-usp-2028-11-07-kamhar` | SELL | 5.0¢ | 286 | 0 | $200.00 | ✅ scoring — ~65.7% of ask side (67,299 resting ≥ 20,000 ✓) ≈ $2.44/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-tulgab` | BUY | 5.0¢ | 135 | 1 | $200.00 | ✅ scoring — ~62.6% of bid side (30,166 resting ≥ 20,000 ✓) ≈ $2.32/day (event pool ÷ 27 markets) |
| `aachc-cfb-wins-2026-11-28-boscol-2pt5wins` | BUY | 85.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~62.4% of the bid side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-ga-9pt5wins` | BUY | 74.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~62.3% of the bid side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-frest-4pt5wins` | BUY | 86.0¢ | 0 | 1 | $25.00 | ⏳ scoring ~61.6% of the bid side — holding the estimate until I know how many markets share this pool |
| `aqc-nfl-2027-01-10-playoffq-sea` | BUY | 71.0¢ | 0 | 0 | $300.00 | ⏳ scoring ~61.3% of the bid side — holding the estimate until I know how many markets share this pool |
| `ewc-usp-2028-11-07-rondes` | BUY | 8.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~58.8% of bid side (51,189 resting ≥ 20,000 ✓) ≈ $2.18/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-jbpri` | SELL | 9.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~58.1% of ask side (71,361 resting ≥ 20,000 ✓) ≈ $2.15/day (event pool ÷ 27 markets) |
| `aachc-cfb-wins-2026-11-28-mia-9pt5wins` | SELL | 71.0¢ | 0 | 2 | $25.00 | ⏳ scoring ~58.0% of the ask side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-pennst-8pt5wins` | BUY | 61.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~57.7% of the bid side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-ncst-7pt5wins` | BUY | 43.0¢ | 0 | 2 | $25.00 | ⏳ scoring ~56.2% of the bid side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-ucf-7pt5wins` | BUY | 18.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~55.5% of the bid side — holding the estimate until I know how many markets share this pool |
| `aachc-cfb-wins-2026-11-28-minnst-7pt5wins` | SELL | 25.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~54.4% of the ask side — holding the estimate until I know how many markets share this pool |
| `ewc-usp-2028-11-07-wesmoo` | BUY | 5.0¢ | 45 | 1 | $200.00 | ✅ scoring — ~51.0% of bid side (20,492 resting ≥ 20,000 ✓) ≈ $1.89/day (event pool ÷ 27 markets) |
| `aachc-cfb-wins-2026-11-28-iowa-7pt5wins` | BUY | 56.0¢ | 0 | 0 | $25.00 | ⏳ scoring ~50.5% of the bid side — holding the estimate until I know how many markets share this pool |
| …and 1586 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>aachc-cfb-wins-2026-11-28-usc-7pt5wins</code> SELL 0 @ 61¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 61¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 71¢ | 2 | ×0.5^10 = 0.0 |
|  | 84¢ | 50 | ×0.5^23 = 0.0 |
|  | 89¢ | 21,633 | ×0.5^28 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 97.7%`  

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 86 @ 4¢ → $6.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 88 (86 yours) | ×0.2^0 = 88.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 3 | ×0.2^8 = 0.0 |
|  | 13¢ | 4 | ×0.2^9 = 0.0 |
|  | 14¢ | 55 | ×0.2^10 = 0.0 |
|  | 15¢ | 40,995 | ×0.2^11 = 0.0 |
| | | **Σ** | **88.0** |

`yours 86.0 / Σ 88.0 = 97.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 97.7% = $6.98/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes` ← this one
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab`
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> BUY 135 @ 8¢ → $3.47/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 144 (135 yours) | ×0.2^0 = 143.5 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 1 | ×0.2^4 = 0.0 |
|  | 2¢ | 112 | ×0.2^6 = 0.0 |
|  | 1¢ | 50,097 | ×0.2^7 = 0.6 |
| | | **Σ** | **144.2** |

`yours 135.0 / Σ 144.2 = 93.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 93.6% = $3.47/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-uk-5pt5wins</code> BUY 2 @ 43¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 2 (2 yours) | ×0.5^0 = 2.3 |
|  | 41¢ | 0 | ×0.5^2 = 0.0 |
|  | 21¢ | 50 | ×0.5^22 = 0.0 |
|  | 16¢ | 16,000 | ×0.5^27 = 0.0 |
| | | **Σ** | **2.3** |

`yours 2.0 / Σ 2.3 = 88.3%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-uk-6pt5wins</code> SELL 10 @ 22¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 11 (10 yours) | ×0.5^0 = 10.5 |
|  | 35¢ | 56 | ×0.5^13 = 0.0 |
|  | 36¢ | 16,050 | ×0.5^14 = 1.0 |
| | | **Σ** | **11.5** |

`yours 10.0 / Σ 11.5 = 86.8%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-txtech-10pt5wins</code> BUY 0 @ 65¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 65¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 52¢ | 150 | ×0.5^13 = 0.0 |
|  | 27¢ | 50 | ×0.5^38 = 0.0 |
|  | 2¢ | 13 | ×0.5^63 = 0.0 |
|  | 1¢ | 5,336 | ×0.5^64 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 84.5%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-aubrn-4pt5wins</code> SELL 0 @ 77¢ → $2.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 77¢ | 0 (0 yours) | ×0.5^0 = 0.5 |
|  | 99¢ | 384,472 | ×0.5^22 = 0.1 |
| | | **Σ** | **0.6** |

`yours 0.5 / Σ 0.6 = 84.5%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 84.5% = $2.11/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-aubrn-4pt5wins` ← this one
2. `aachc-cfb-wins-2026-11-28-aubrn-5pt5wins`
3. `aachc-cfb-wins-2026-11-28-aubrn-6pt5wins`
4. `aachc-cfb-wins-2026-11-28-aubrn-7pt5wins`
5. `aachc-cfb-wins-2026-11-28-aubrn-8pt5wins`

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-ga-8pt5wins</code> SELL 0 @ 72¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 72¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 98¢ | 50 | ×0.5^26 = 0.0 |
|  | 99¢ | 213,249 | ×0.5^27 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 82.2%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-mich-8pt5wins</code> BUY 0 @ 47¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 47¢ | 0 (0 yours) | ×0.5^0 = 0.2 |
|  | 36¢ | 75 | ×0.5^11 = 0.0 |
|  | 33¢ | 100 | ×0.5^14 = 0.0 |
|  | 32¢ | 103 | ×0.5^15 = 0.0 |
|  | 31¢ | 50 | ×0.5^16 = 0.0 |
|  | 7¢ | 34 | ×0.5^40 = 0.0 |
|  | 2¢ | 15 | ×0.5^45 = 0.0 |
|  | 1¢ | 5,217 | ×0.5^46 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.2 / Σ 0.2 = 81.1%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-miss-6pt5wins</code> SELL 0 @ 71¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 70¢ | 0 | ×0.5^0 = 0.0 |
| ▶ | 71¢ | 0 (0 yours) | ×0.5^1 = 0.1 |
|  | 92¢ | 22,786 | ×0.5^22 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 79.7%`  

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 120 @ 5¢ → $2.86/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 122 (120 yours) | ×0.2^0 = 122.0 |
|  | 4¢ | 4 | ×0.2^1 = 0.8 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 20,443 | ×0.2^4 = 32.7 |
| | | **Σ** | **155.6** |

`yours 120.0 / Σ 155.6 = 77.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 77.1% = $2.86/day`  

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
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 83 @ 7¢ → $2.80/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 95 (83 yours) | ×0.2^0 = 95.4 |
|  | 6¢ | 27 | ×0.2^1 = 5.4 |
|  | 5¢ | 31 | ×0.2^2 = 1.2 |
|  | 3¢ | 250 | ×0.2^4 = 0.4 |
|  | 2¢ | 22,500 | ×0.2^5 = 7.2 |
| | | **Σ** | **109.7** |

`yours 83.0 / Σ 109.7 = 75.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 75.7% = $2.80/day`  

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
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> SELL 1 @ 16¢ → $4.37/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 17¢ | 1 | ×0.2^1 = 0.2 |
|  | 18¢ | 2 | ×0.2^2 = 0.1 |
|  | 20¢ | 2 | ×0.2^4 = 0.0 |
|  | 21¢ | 21 | ×0.2^5 = 0.0 |
|  | 24¢ | 22,165 | ×0.2^8 = 0.1 |
| | | **Σ** | **1.3** |

`yours 1.0 / Σ 1.3 = 74.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 74.3% = $4.37/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-clmsn-5pt5wins</code> BUY 0 @ 79¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 0 (0 yours) | ×0.5^0 = 0.5 |
|  | 71¢ | 50 | ×0.5^8 = 0.2 |
|  | 68¢ | 0 | ×0.5^11 = 0.0 |
|  | 2¢ | 52 | ×0.5^77 = 0.0 |
|  | 1¢ | 5,397 | ×0.5^78 = 0.0 |
| | | **Σ** | **0.7** |

`yours 0.5 / Σ 0.7 = 71.9%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-ohiost-11pt5wins</code> SELL 0 @ 15¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 26¢ | 50 | ×0.5^11 = 0.0 |
|  | 52¢ | 100 | ×0.5^37 = 0.0 |
|  | 98¢ | 50 | ×0.5^83 = 0.0 |
|  | 99¢ | 5,300 | ×0.5^84 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 69.2%`  

</details>
<details><summary><code>ewc-usp-2028-11-07-kamhar</code> SELL 286 @ 5¢ → $2.44/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 435 (286 yours) | ×0.2^0 = 435.0 |
|  | 14¢ | 172 | ×0.2^9 = 0.0 |
|  | 19¢ | 31,724 | ×0.2^14 = 0.0 |
| | | **Σ** | **435.0** |

`yours 286.0 / Σ 435.0 = 65.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 65.7% = $2.44/day`  

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
14. `ewc-usp-2028-11-07-kamhar` ← this one
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
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> BUY 135 @ 5¢ → $2.32/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 1 | ×0.2^0 = 1.0 |
| ▶ | 5¢ | 159 (135 yours) | ×0.2^1 = 31.8 |
|  | 4¢ | 18 | ×0.2^2 = 0.7 |
|  | 2¢ | 13 | ×0.2^4 = 0.0 |
|  | 1¢ | 29,975 | ×0.2^5 = 9.6 |
| | | **Σ** | **43.1** |

`yours 27.0 / Σ 43.1 = 62.6%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 62.6% = $2.32/day`  

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
25. `ewc-usp-2028-11-07-tulgab` ← this one
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-boscol-2pt5wins</code> BUY 0 @ 85¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 84¢ | 0 | ×0.5^1 = 0.0 |
|  | 83¢ | 0 | ×0.5^2 = 0.0 |
|  | 79¢ | 0 | ×0.5^6 = 0.0 |
|  | 57¢ | 78 | ×0.5^28 = 0.0 |
|  | 56¢ | 16,000 | ×0.5^29 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.1 / Σ 0.2 = 62.4%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-ga-9pt5wins</code> BUY 0 @ 74¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 63¢ | 62 | ×0.5^11 = 0.0 |
|  | 52¢ | 151 | ×0.5^22 = 0.0 |
|  | 50¢ | 200 | ×0.5^24 = 0.0 |
|  | 7¢ | 52 | ×0.5^67 = 0.0 |
|  | 1¢ | 5,036 | ×0.5^73 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 62.3%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-frest-4pt5wins</code> BUY 0 @ 86¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 87¢ | 0 | ×0.5^0 = 0.0 |
| ▶ | 86¢ | 0 (0 yours) | ×0.5^1 = 0.1 |
|  | 84¢ | 0 | ×0.5^3 = 0.0 |
|  | 73¢ | 151 | ×0.5^14 = 0.0 |
|  | 69¢ | 46 | ×0.5^18 = 0.0 |
|  | 68¢ | 16,000 | ×0.5^19 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.1 / Σ 0.2 = 61.6%`  

</details>
<details><summary><code>aqc-nfl-2027-01-10-playoffq-sea</code> BUY 0 @ 71¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 71¢ | 0 (0 yours) | ×0.3^0 = 0.5 |
|  | 66¢ | 130 | ×0.3^5 = 0.3 |
|  | 3¢ | 56 | ×0.3^68 = 0.0 |
|  | 2¢ | 50,000 | ×0.3^69 = 0.0 |
| | | **Σ** | **0.8** |

`yours 0.5 / Σ 0.8 = 61.3%`  

</details>
<details><summary><code>ewc-usp-2028-11-07-rondes</code> BUY 1 @ 8¢ → $2.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 4¢ | 4 | ×0.2^4 = 0.0 |
|  | 2¢ | 1 | ×0.2^6 = 0.0 |
|  | 1¢ | 51,182 | ×0.2^7 = 0.7 |
| | | **Σ** | **1.7** |

`yours 1.0 / Σ 1.7 = 58.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 58.8% = $2.18/day`  

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
21. `ewc-usp-2028-11-07-rondes` ← this one
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jbpri</code> SELL 1 @ 9¢ → $2.15/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 9¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 10¢ | 3 | ×0.2^1 = 0.6 |
|  | 11¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 2 | ×0.2^3 = 0.0 |
|  | 13¢ | 40 | ×0.2^4 = 0.1 |
|  | 15¢ | 14 | ×0.2^6 = 0.0 |
|  | 22¢ | 51,050 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.7** |

`yours 1.0 / Σ 1.7 = 58.1%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 58.1% = $2.15/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-mia-9pt5wins</code> SELL 0 @ 71¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 69¢ | 0 | ×0.5^0 = 0.0 |
| ▶ | 71¢ | 0 (0 yours) | ×0.5^2 = 0.1 |
|  | 88¢ | 37,030 | ×0.5^19 = 0.1 |
| | | **Σ** | **0.2** |

`yours 0.1 / Σ 0.2 = 58.0%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-pennst-8pt5wins</code> BUY 0 @ 61¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 61¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 50¢ | 150 | ×0.5^11 = 0.1 |
|  | 40¢ | 50 | ×0.5^21 = 0.0 |
|  | 2¢ | 47 | ×0.5^59 = 0.0 |
|  | 1¢ | 5,302 | ×0.5^60 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.1 / Σ 0.2 = 57.7%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-ncst-7pt5wins</code> BUY 0 @ 43¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 45¢ | 0 | ×0.5^0 = 0.1 |
|  | 44¢ | 0 | ×0.5^1 = 0.0 |
| ▶ | 43¢ | 0 (0 yours) | ×0.5^2 = 0.1 |
|  | 42¢ | 0 | ×0.5^3 = 0.0 |
|  | 39¢ | 0 | ×0.5^6 = 0.0 |
|  | 34¢ | 50 | ×0.5^11 = 0.0 |
|  | 2¢ | 5,400 | ×0.5^43 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.1 / Σ 0.2 = 56.2%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-ucf-7pt5wins</code> BUY 0 @ 18¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 2¢ | 5,250 | ×0.5^16 = 0.1 |
| | | **Σ** | **0.2** |

`yours 0.1 / Σ 0.2 = 55.5%`  

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-minnst-7pt5wins</code> SELL 0 @ 25¢ → $0</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 25¢ | 0 (0 yours) | ×0.5^0 = 0.5 |
|  | 29¢ | 7 | ×0.5^4 = 0.4 |
|  | 45¢ | 50 | ×0.5^20 = 0.0 |
|  | 50¢ | 45 | ×0.5^25 = 0.0 |
|  | 51¢ | 16,021 | ×0.5^26 = 0.0 |
| | | **Σ** | **0.9** |

`yours 0.5 / Σ 0.9 = 54.4%`  

</details>
<details><summary><code>ewc-usp-2028-11-07-wesmoo</code> BUY 45 @ 5¢ → $1.89/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 2 | ×0.2^0 = 2.1 |
| ▶ | 5¢ | 45 (45 yours) | ×0.2^1 = 9.0 |
|  | 2¢ | 1 | ×0.2^4 = 0.0 |
|  | 1¢ | 20,444 | ×0.2^5 = 6.5 |
| | | **Σ** | **17.7** |

`yours 9.0 / Σ 17.7 = 51.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 51.0% = $1.89/day`  

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
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo` ← this one

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-iowa-7pt5wins</code> BUY 0 @ 56¢ → $0</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 56¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 45¢ | 200 | ×0.5^11 = 0.1 |
|  | 37¢ | 102 | ×0.5^19 = 0.0 |
|  | 36¢ | 50 | ×0.5^20 = 0.0 |
|  | 2¢ | 13 | ×0.5^54 = 0.0 |
|  | 1¢ | 5,135 | ×0.5^55 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.1 / Σ 0.2 = 50.5%`  

</details>

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `dipcc-us-iran-contnts-2026--irnfnd` | $75.00 ÷ 6 | 0.25 | 2,000 | BUY side (2,200 resting) | ~99.9% | ~$6.24 |
| `dipcc-us-iran-contnts-2026--dilut` | $75.00 ÷ 6 | 0.25 | 2,000 | BUY side (2,312 resting) | ~99.5% | ~$6.22 |
| `dipcc-us-iran-contnts-2026--enrcaplte5` | $75.00 ÷ 6 | 0.25 | 2,000 | SELL side (9,793 resting) | ~99.5% | ~$6.22 |
| `dipcc-us-iran-contnts-2026--enrmor` | $75.00 ÷ 6 | 0.25 | 2,000 | SELL side (9,351 resting) | ~89.7% | ~$5.61 |
| `dipcc-us-iran-contnts-2026--urnsur` | $75.00 ÷ 6 | 0.25 | 2,000 | BUY side (3,760 resting) | ~56.6% | ~$3.54 |
| `dipcc-us-iran-contnts-2026--enrcap` | $75.00 ÷ 6 | 0.25 | 2,000 | SELL side (2,673 resting) | ~27.8% | ~$1.74 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (6,108 resting) | ~4.1% | ~$1.03 |

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
| 2026-08-20 11:41 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 10:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 9:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 8:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 7:30 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 6:13 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 4:57 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 3:54 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 2:53 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 1:52 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
