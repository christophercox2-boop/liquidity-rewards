# Polymarket US — Liquidity Rewards

## ✅ Last successful check: 2026-08-20 10:40 AM ET

Written by **the live monitor**, every hour. **If the timestamp above is more than ~2 hours old, something is broken.** Open /map. If that page will not load at all, the monitor is down and needs a restart from DigitalOcean.

> ⚠️ **Nothing is watching the watcher.** The 4-hourly Actions run used to stamp a ❌ here if the monitor died. No job in this repo has reached a runner since 2026-08-16 03:34 UTC — Actions minutes or the spending limit, fixable only at [billing](https://github.com/settings/billing). Until then a dead monitor looks like a timestamp that quietly stops moving, and no email arrives. The timestamp above is the check.

> ✅ **2028-slate pool scope: SETTLED — the pool is per EVENT.** The Aug-15 payout decided it. Predicted program-wide vs per-event vs what actually paid: nominees $108 / $400 / **$684**, winners $140 / $310 / **$412**, the party pair $4 / $130 / **$148**. Program-wide was out by up to 34x; per-event lands within 1.1–1.7x and errs low. Estimates from 2026-08-17 use per event, so slate figures here are ~4x higher than in earlier runs — that is the fix, not a windfall.

## 📌 Summary

**Earning right now:** ~$364.94/day estimated (ceiling, not promise — details below)

**Earned:** $5,117.59 lifetime ($4,919.08 paid). Last three recorded days — 2026-08-16: **$197.03** ⚠️ pending bucket — covers every day since then, still growing · 2026-08-15: **$1,352.63** · 2026-08-14: **$274.92** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `dipcc-us-iran-contnts-2026--dilut` — BUY at the best price, ~$6.22/day for 200 contracts. Runners-up: `dipcc-us-iran-contnts-2026--enrcaplte5` (~$6.22/day), `dipcc-us-iran-contnts-2026--irnfnd` (~$6.17/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$364.94/day (~$15.21/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `aqc-nfl-2027-01-10-playoffq-gb` | SELL | 51.0¢ | 0 | 0 | $300.00 | ✅ scoring — ~100.0% of ask side (32,997 resting ≥ 15,000 ✓) ≈ $18.75/day (event pool ÷ 8 markets) |
| `enwc-uspres-nom-rep-2028-rondes` | SELL | 4.0¢ | 86 | 0 | $200.00 | ✅ scoring — ~97.7% of ask side (44,791 resting ≥ 20,000 ✓) ≈ $6.98/day (event pool ÷ 14 markets) |
| `ewc-usp-2028-11-07-jbpri` | BUY | 8.0¢ | 135 | 0 | $200.00 | ✅ scoring — ~93.6% of bid side (50,355 resting ≥ 20,000 ✓) ≈ $3.47/day (event pool ÷ 27 markets) |
| `ftsc-nfl-temostfp-w1-2026-09-14-brobow` | SELL | 12.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~92.8% of ask side (65,334 resting ≥ 7,500 ✓) ≈ $5.80/day (event pool ÷ 8 markets) |
| `ewc-usp-2028-11-07-tulgab` | SELL | 7.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~88.0% of ask side (50,860 resting ≥ 20,000 ✓) ≈ $3.26/day (event pool ÷ 27 markets) |
| `fptc-nfl-rbfpou-2027-01-10-kyrwil` | SELL | 51.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~85.2% of ask side (16,486 resting ≥ 7,500 ✓) ≈ $2.03/day (event pool ÷ 21 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | BUY | 15.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~81.4% of bid side (96,739 resting ≥ 20,000 ✓) ≈ $4.79/day (event pool ÷ 17 markets) |
| `aqc-nfl-2027-01-10-playoffq-bal` | BUY | 79.0¢ | 0 | 0 | $300.00 | ✅ scoring — ~80.0% of bid side (250,125 resting ≥ 15,000 ✓) ≈ $15.00/day (event pool ÷ 8 markets) |
| `ewc-usp-2028-11-07-petbut` | BUY | 7.0¢ | 83 | 0 | $200.00 | ✅ scoring — ~76.4% of bid side (36,177 resting ≥ 20,000 ✓) ≈ $2.83/day (event pool ÷ 27 markets) |
| `aachc-cfb-wins-2026-11-28-ind-11pt5wins` | BUY | 34.0¢ | 1 | 5 | $25.00 | ✅ scoring — ~75.4% of bid side (5,528 resting ≥ 5,000 ✓) ≈ $2.36/day (event pool ÷ 4 markets) |
| `ewc-usp-2028-11-07-vivram` | BUY | 5.0¢ | 120 | 0 | $200.00 | ✅ scoring — ~72.3% of bid side (20,584 resting ≥ 20,000 ✓) ≈ $2.68/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-kamhar` | SELL | 5.0¢ | 286 | 0 | $200.00 | ✅ scoring — ~65.7% of ask side (67,299 resting ≥ 20,000 ✓) ≈ $2.44/day (event pool ÷ 27 markets) |
| `aachc-cfb-wins-2026-11-28-boscol-2pt5wins` | BUY | 85.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~62.3% of bid side (17,295 resting ≥ 5,000 ✓) ≈ $1.95/day (event pool ÷ 4 markets) |
| `aachc-cfb-wins-2026-11-28-sdst-5pt5wins` | SELL | 74.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~61.5% of ask side (16,518 resting ≥ 5,000 ✓) ≈ $2.56/day (event pool ÷ 3 markets) |
| `aachc-cfb-wins-2026-11-28-uk-6pt5wins` | SELL | 22.0¢ | 10 | 0 | $25.00 | ✅ scoring — ~60.6% of ask side (32,341 resting ≥ 5,000 ✓) ≈ $1.51/day (event pool ÷ 5 markets) |
| `aachc-cfb-wins-2026-11-28-arz-9pt5wins` | SELL | 20.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~57.3% of ask side (16,520 resting ≥ 5,000 ✓) ≈ $1.43/day (event pool ÷ 5 markets) |
| `aachc-cfb-wins-2026-11-28-txtech-9pt5wins` | SELL | 74.0¢ | 0 | 0 | $25.00 | ✅ scoring — ~55.7% of ask side (41,927 resting ≥ 5,000 ✓) ≈ $1.74/day (event pool ÷ 4 markets) |
| `ewc-usp-2028-11-07-jamtal` | BUY | 6.0¢ | 100 | 2 | $200.00 | ✅ scoring — ~50.7% of bid side (160,139 resting ≥ 20,000 ✓) ≈ $1.88/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-dem-2028-jossha` | SELL | 8.0¢ | 38 | 0 | $200.00 | ✅ scoring — ~50.1% of ask side (53,664 resting ≥ 20,000 ✓) ≈ $2.95/day (event pool ÷ 17 markets) |
| `aachc-cfb-wins-2026-11-28-missr-5pt5wins` | SELL | 70.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~49.7% of ask side (5,502 resting ≥ 5,000 ✓) ≈ $3.11/day (event pool ÷ 2 markets) |
| `fptc-nfl-rbfpou-2027-01-10-bhatut` | SELL | 49.0¢ | 0 | 0 | $100.00 | ✅ scoring — ~49.5% of ask side (16,486 resting ≥ 7,500 ✓) ≈ $1.18/day (event pool ÷ 21 markets) |
| `aachc-cfb-wins-2026-11-28-uk-5pt5wins` | BUY | 43.0¢ | 2 | 0 | $25.00 | ✅ scoring — ~47.1% of bid side (18,583 resting ≥ 5,000 ✓) ≈ $1.18/day (event pool ÷ 5 markets) |
| `enwc-uspres-nom-dem-2028-andbes` | SELL | 12.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~46.9% of ask side (38,877 resting ≥ 20,000 ✓) ≈ $2.76/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-micoba` | BUY | 1.0¢ | 9,253 | 2 | $200.00 | ✅ scoring — ~46.0% of bid side (20,029 resting ≥ 20,000 ✓) ≈ $2.71/day (event pool ÷ 17 markets) |
| `enwc-uspres-nom-dem-2028-petbut` | SELL | 16.0¢ | 1 | 0 | $200.00 | ✅ scoring — ~43.3% of ask side (38,729 resting ≥ 20,000 ✓) ≈ $2.55/day (event pool ÷ 17 markets) |
| `ewc-usp-2028-11-07-rokha` | BUY | 1.0¢ | 9,546 | 0 | $200.00 | ✅ scoring — ~43.2% of bid side (22,072 resting ≥ 20,000 ✓) ≈ $1.60/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-thomas` | SELL | 3.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~42.8% of ask side (71,552 resting ≥ 20,000 ✓) ≈ $1.59/day (event pool ÷ 27 markets) |
| `ewc-usp-2028-11-07-elomus` | SELL | 5.0¢ | 3 | 0 | $200.00 | ✅ scoring — ~42.8% of ask side (56,689 resting ≥ 20,000 ✓) ≈ $1.58/day (event pool ÷ 27 markets) |
| `enwc-uspres-nom-rep-2028-tulgab` | BUY | 1.0¢ | 19,238 | 2 | $200.00 | ✅ scoring — ~42.7% of bid side (41,919 resting ≥ 20,000 ✓) ≈ $3.05/day (event pool ÷ 14 markets) |
| `enwc-uspres-nom-dem-2028-dwajoh` | BUY | 1.0¢ | 19,311 | 2 | $200.00 | ✅ scoring — ~41.9% of bid side (41,921 resting ≥ 20,000 ✓) ≈ $2.46/day (event pool ÷ 17 markets) |
| …and 1452 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>aqc-nfl-2027-01-10-playoffq-gb</code> SELL 0 @ 51¢ → $18.75/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 0 (0 yours) | ×0.3^0 = 0.1 |
|  | 85¢ | 675 | ×0.3^34 = 0.0 |
|  | 89¢ | 50 | ×0.3^38 = 0.0 |
|  | 90¢ | 16,000 | ×0.3^39 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 100.0%`  
`$300 ÷ 8 ÷ 2 = $18.75 × 100.0% = $18.75/day`  

<details><summary>÷ 8 markets in this race — tap to list</summary>

1. `aqc-nfl-2027-01-10-playoffq-bal`
2. `aqc-nfl-2027-01-10-playoffq-cin`
3. `aqc-nfl-2027-01-10-playoffq-cle`
4. `aqc-nfl-2027-01-10-playoffq-dal`
5. `aqc-nfl-2027-01-10-playoffq-gb` ← this one
6. `aqc-nfl-2027-01-10-playoffq-sea`
7. `aqc-nfl-2027-01-10-playoffq-sf`
8. `aqc-nfl-2027-01-10-playoffq-was`

</details>

</details>
<details><summary><code>enwc-uspres-nom-rep-2028-rondes</code> SELL 86 @ 4¢ → $6.98/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 4¢ | 88 (86 yours) | ×0.2^0 = 88.0 |
|  | 6¢ | 1 | ×0.2^2 = 0.0 |
|  | 12¢ | 3 | ×0.2^8 = 0.0 |
|  | 13¢ | 6 | ×0.2^9 = 0.0 |
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
<details><summary><code>ftsc-nfl-temostfp-w1-2026-09-14-brobow</code> SELL 0 @ 12¢ → $5.80/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 0 (0 yours) | ×0.4^0 = 0.1 |
|  | 24¢ | 50 | ×0.4^12 = 0.0 |
|  | 28¢ | 16,000 | ×0.4^16 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 92.8%`  
`$100 ÷ 8 ÷ 2 = $6.25 × 92.8% = $5.80/day`  

<details><summary>÷ 8 markets in this race — tap to list</summary>

1. `ftsc-nfl-temostfp-w1-2026-09-14-brobow` ← this one
2. `ftsc-nfl-temostfp-w1-2026-09-14-dalgoe`
3. `ftsc-nfl-temostfp-w1-2026-09-14-dalkin`
4. `ftsc-nfl-temostfp-w1-2026-09-14-davnjo`
5. `ftsc-nfl-temostfp-w1-2026-09-14-harfan`
6. `ftsc-nfl-temostfp-w1-2026-09-14-jakfer`
7. `ftsc-nfl-temostfp-w1-2026-09-14-thoc`
8. `ftsc-nfl-temostfp-w1-2026-09-14-tremcb`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-tulgab</code> SELL 1 @ 7¢ → $3.26/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 9¢ | 3 | ×0.2^2 = 0.1 |
|  | 10¢ | 2 | ×0.2^3 = 0.0 |
|  | 13¢ | 1 | ×0.2^6 = 0.0 |
|  | 20¢ | 287 | ×0.2^13 = 0.0 |
|  | 21¢ | 50 | ×0.2^14 = 0.0 |
|  | 25¢ | 30,266 | ×0.2^18 = 0.0 |
| | | **Σ** | **1.1** |

`yours 1.0 / Σ 1.1 = 88.0%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 88.0% = $3.26/day`  

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
<details><summary><code>fptc-nfl-rbfpou-2027-01-10-kyrwil</code> SELL 0 @ 51¢ → $2.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 51¢ | 0 (0 yours) | ×0.4^0 = 0.2 |
|  | 54¢ | 1 | ×0.4^3 = 0.0 |
|  | 66¢ | 50 | ×0.4^15 = 0.0 |
|  | 75¢ | 16,210 | ×0.4^24 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.2 / Σ 0.2 = 85.2%`  
`$100 ÷ 21 ÷ 2 = $2.38 × 85.2% = $2.03/day`  

<details><summary>÷ 21 markets in this race — tap to list</summary>

1. `fptc-nfl-rbfpou-2027-01-10-aarjon`
2. `fptc-nfl-rbfpou-2027-01-10-ashjea`
3. `fptc-nfl-rbfpou-2027-01-10-bhatut`
4. `fptc-nfl-rbfpou-2027-01-10-bucirv`
5. `fptc-nfl-rbfpou-2027-01-10-camska`
6. `fptc-nfl-rbfpou-2027-01-10-chrmcc`
7. `fptc-nfl-rbfpou-2027-01-10-chuhub`
8. `fptc-nfl-rbfpou-2027-01-10-davmon`
9. `fptc-nfl-rbfpou-2027-01-10-jadpri`
10. `fptc-nfl-rbfpou-2027-01-10-jamcoo`
11. `fptc-nfl-rbfpou-2027-01-10-jaywar`
12. `fptc-nfl-rbfpou-2027-01-10-jdob`
13. `fptc-nfl-rbfpou-2027-01-10-kenwal`
14. `fptc-nfl-rbfpou-2027-01-10-kyrwil` ← this one
15. `fptc-nfl-rbfpou-2027-01-10-omaham`
16. `fptc-nfl-rbfpou-2027-01-10-racwhi`
17. `fptc-nfl-rbfpou-2027-01-10-rhaste`
18. `fptc-nfl-rbfpou-2027-01-10-rjhar`
19. `fptc-nfl-rbfpou-2027-01-10-tylall`
20. `fptc-nfl-rbfpou-2027-01-10-tyrtra`
21. `fptc-nfl-rbfpou-2027-01-10-woomar`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> BUY 1 @ 15¢ → $4.79/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 15¢ | 1 (1 yours) | ×0.2^0 = 1.0 |
|  | 14¢ | 1 | ×0.2^1 = 0.2 |
|  | 12¢ | 3 | ×0.2^3 = 0.0 |
|  | 11¢ | 2 | ×0.2^4 = 0.0 |
|  | 10¢ | 2 | ×0.2^5 = 0.0 |
|  | 8¢ | 6 | ×0.2^7 = 0.0 |
|  | 6¢ | 125 | ×0.2^9 = 0.0 |
|  | 5¢ | 10,000 | ×0.2^10 = 0.0 |
|  | 2¢ | 66,250 | ×0.2^13 = 0.0 |
| | | **Σ** | **1.2** |

`yours 1.0 / Σ 1.2 = 81.4%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 81.4% = $4.79/day`  

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
<details><summary><code>aqc-nfl-2027-01-10-playoffq-bal</code> BUY 0 @ 79¢ → $15.00/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 79¢ | 0 (0 yours) | ×0.3^0 = 0.2 |
|  | 59¢ | 1,047 | ×0.3^20 = 0.0 |
|  | 58¢ | 48 | ×0.3^21 = 0.0 |
|  | 57¢ | 17,944 | ×0.3^22 = 0.0 |
| | | **Σ** | **0.3** |

`yours 0.2 / Σ 0.3 = 80.0%`  
`$300 ÷ 8 ÷ 2 = $18.75 × 80.0% = $15.00/day`  

<details><summary>÷ 8 markets in this race — tap to list</summary>

1. `aqc-nfl-2027-01-10-playoffq-bal` ← this one
2. `aqc-nfl-2027-01-10-playoffq-cin`
3. `aqc-nfl-2027-01-10-playoffq-cle`
4. `aqc-nfl-2027-01-10-playoffq-dal`
5. `aqc-nfl-2027-01-10-playoffq-gb`
6. `aqc-nfl-2027-01-10-playoffq-sea`
7. `aqc-nfl-2027-01-10-playoffq-sf`
8. `aqc-nfl-2027-01-10-playoffq-was`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-petbut</code> BUY 83 @ 7¢ → $2.83/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 94 (83 yours) | ×0.2^0 = 94.4 |
|  | 6¢ | 27 | ×0.2^1 = 5.4 |
|  | 5¢ | 31 | ×0.2^2 = 1.2 |
|  | 3¢ | 250 | ×0.2^4 = 0.4 |
|  | 2¢ | 22,500 | ×0.2^5 = 7.2 |
| | | **Σ** | **108.7** |

`yours 83.0 / Σ 108.7 = 76.4%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 76.4% = $2.83/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-ind-11pt5wins</code> BUY 1 @ 34¢ → $2.36/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 39¢ | 0 | ×0.5^0 = 0.0 |
| ▶ | 34¢ | 1 (1 yours) | ×0.5^5 = 0.0 |
|  | 33¢ | 0 | ×0.5^6 = 0.0 |
|  | 31¢ | 0 | ×0.5^8 = 0.0 |
|  | 3¢ | 5,200 | ×0.5^36 = 0.0 |
| | | **Σ** | **0.0** |

`yours 0.0 / Σ 0.0 = 75.4%`  
`$25 ÷ 4 ÷ 2 = $3.12 × 75.4% = $2.36/day`  

<details><summary>÷ 4 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-ind-11pt5wins` ← this one
2. `aachc-cfb-wins-2026-11-28-ind-7pt5wins`
3. `aachc-cfb-wins-2026-11-28-ind-8pt5wins`
4. `aachc-cfb-wins-2026-11-28-ind-9pt5wins`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-vivram</code> BUY 120 @ 5¢ → $2.68/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 132 (120 yours) | ×0.2^0 = 132.4 |
|  | 4¢ | 4 | ×0.2^1 = 0.8 |
|  | 3¢ | 3 | ×0.2^2 = 0.1 |
|  | 2¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 20,443 | ×0.2^4 = 32.7 |
| | | **Σ** | **166.0** |

`yours 120.0 / Σ 166.0 = 72.3%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 72.3% = $2.68/day`  

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
<details><summary><code>aachc-cfb-wins-2026-11-28-boscol-2pt5wins</code> BUY 0 @ 85¢ → $1.95/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 85¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 84¢ | 0 | ×0.5^1 = 0.0 |
|  | 83¢ | 0 | ×0.5^2 = 0.0 |
|  | 79¢ | 0 | ×0.5^6 = 0.0 |
|  | 63¢ | 993 | ×0.5^22 = 0.0 |
|  | 57¢ | 52 | ×0.5^28 = 0.0 |
|  | 56¢ | 16,000 | ×0.5^29 = 0.0 |
| | | **Σ** | **0.2** |

`yours 0.1 / Σ 0.2 = 62.3%`  
`$25 ÷ 4 ÷ 2 = $3.12 × 62.3% = $1.95/day`  

<details><summary>÷ 4 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-boscol-2pt5wins` ← this one
2. `aachc-cfb-wins-2026-11-28-boscol-3pt5wins`
3. `aachc-cfb-wins-2026-11-28-boscol-4pt5wins`
4. `aachc-cfb-wins-2026-11-28-boscol-5pt5wins`

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-sdst-5pt5wins</code> SELL 0 @ 74¢ → $2.56/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 91¢ | 50 | ×0.5^17 = 0.0 |
|  | 93¢ | 16,221 | ×0.5^19 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 61.5%`  
`$25 ÷ 3 ÷ 2 = $4.17 × 61.5% = $2.56/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-sdst-5pt5wins` ← this one
2. `aachc-cfb-wins-2026-11-28-sdst-8pt5wins`
3. `aachc-cfb-wins-2026-11-28-sdst-9pt5wins`

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-uk-6pt5wins</code> SELL 10 @ 22¢ → $1.51/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 22¢ | 16 (10 yours) | ×0.5^0 = 15.5 |
|  | 35¢ | 53 | ×0.5^13 = 0.0 |
|  | 36¢ | 16,050 | ×0.5^14 = 1.0 |
| | | **Σ** | **16.5** |

`yours 10.0 / Σ 16.5 = 60.6%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 60.6% = $1.51/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-uk-2pt5wins`
2. `aachc-cfb-wins-2026-11-28-uk-3pt5wins`
3. `aachc-cfb-wins-2026-11-28-uk-4pt5wins`
4. `aachc-cfb-wins-2026-11-28-uk-5pt5wins`
5. `aachc-cfb-wins-2026-11-28-uk-6pt5wins` ← this one

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-arz-9pt5wins</code> SELL 0 @ 20¢ → $1.43/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 20¢ | 1 (0 yours) | ×0.5^0 = 0.6 |
|  | 31¢ | 50 | ×0.5^11 = 0.0 |
|  | 36¢ | 16,221 | ×0.5^16 = 0.2 |
| | | **Σ** | **0.9** |

`yours 0.5 / Σ 0.9 = 57.3%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 57.3% = $1.43/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-arz-5pt5wins`
2. `aachc-cfb-wins-2026-11-28-arz-6pt5wins`
3. `aachc-cfb-wins-2026-11-28-arz-7pt5wins`
4. `aachc-cfb-wins-2026-11-28-arz-8pt5wins`
5. `aachc-cfb-wins-2026-11-28-arz-9pt5wins` ← this one

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-txtech-9pt5wins</code> SELL 0 @ 74¢ → $1.74/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 0 (0 yours) | ×0.5^0 = 0.1 |
|  | 93¢ | 50 | ×0.5^19 = 0.0 |
|  | 94¢ | 41,676 | ×0.5^20 = 0.0 |
| | | **Σ** | **0.1** |

`yours 0.1 / Σ 0.1 = 55.7%`  
`$25 ÷ 4 ÷ 2 = $3.12 × 55.7% = $1.74/day`  

<details><summary>÷ 4 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-txtech-10pt5wins`
2. `aachc-cfb-wins-2026-11-28-txtech-11pt5wins`
3. `aachc-cfb-wins-2026-11-28-txtech-8pt5wins`
4. `aachc-cfb-wins-2026-11-28-txtech-9pt5wins` ← this one

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-jamtal</code> BUY 100 @ 6¢ → $1.88/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 2 | ×0.2^0 = 1.6 |
|  | 7¢ | 1 | ×0.2^1 = 0.2 |
| ▶ | 6¢ | 100 (100 yours) | ×0.2^2 = 4.0 |
|  | 4¢ | 15 | ×0.2^4 = 0.0 |
|  | 1¢ | 160,021 | ×0.2^7 = 2.0 |
| | | **Σ** | **7.9** |

`yours 4.0 / Σ 7.9 = 50.7%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 50.7% = $1.88/day`  

<details><summary>÷ 27 markets in this race — tap to list</summary>

1. `ewc-usp-2028-11-07-aleocc`
2. `ewc-usp-2028-11-07-andbes`
3. `ewc-usp-2028-11-07-dontru`
4. `ewc-usp-2028-11-07-dontrujr`
5. `ewc-usp-2028-11-07-dwajoh`
6. `ewc-usp-2028-11-07-elomus`
7. `ewc-usp-2028-11-07-gavnew`
8. `ewc-usp-2028-11-07-gleyou`
9. `ewc-usp-2028-11-07-jamtal` ← this one
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
<details><summary><code>enwc-uspres-nom-dem-2028-jossha</code> SELL 38 @ 8¢ → $2.95/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 8¢ | 64 (38 yours) | ×0.2^0 = 64.0 |
|  | 11¢ | 5 | ×0.2^3 = 0.0 |
|  | 13¢ | 37,032 | ×0.2^5 = 11.9 |
| | | **Σ** | **75.9** |

`yours 38.0 / Σ 75.9 = 50.1%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 50.1% = $2.95/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh`
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
7. `enwc-uspres-nom-dem-2028-jonoss`
8. `enwc-uspres-nom-dem-2028-jonste`
9. `enwc-uspres-nom-dem-2028-jossha` ← this one
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
<details><summary><code>aachc-cfb-wins-2026-11-28-missr-5pt5wins</code> SELL 1 @ 70¢ → $3.11/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 70¢ | 2 (1 yours) | ×0.5^0 = 2.0 |
|  | 87¢ | 51 | ×0.5^17 = 0.0 |
|  | 88¢ | 0 | ×0.5^18 = 0.0 |
|  | 99¢ | 5,449 | ×0.5^29 = 0.0 |
| | | **Σ** | **2.0** |

`yours 1.0 / Σ 2.0 = 49.7%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 49.7% = $3.11/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-missr-5pt5wins` ← this one
2. `aachc-cfb-wins-2026-11-28-missr-7pt5wins`

</details>

</details>
<details><summary><code>fptc-nfl-rbfpou-2027-01-10-bhatut</code> SELL 0 @ 49¢ → $1.18/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 49¢ | 0 (0 yours) | ×0.4^0 = 0.2 |
|  | 50¢ | 1 | ×0.4^1 = 0.2 |
|  | 63¢ | 50 | ×0.4^14 = 0.0 |
|  | 75¢ | 16,210 | ×0.4^26 = 0.0 |
| | | **Σ** | **0.4** |

`yours 0.2 / Σ 0.4 = 49.5%`  
`$100 ÷ 21 ÷ 2 = $2.38 × 49.5% = $1.18/day`  

<details><summary>÷ 21 markets in this race — tap to list</summary>

1. `fptc-nfl-rbfpou-2027-01-10-aarjon`
2. `fptc-nfl-rbfpou-2027-01-10-ashjea`
3. `fptc-nfl-rbfpou-2027-01-10-bhatut` ← this one
4. `fptc-nfl-rbfpou-2027-01-10-bucirv`
5. `fptc-nfl-rbfpou-2027-01-10-camska`
6. `fptc-nfl-rbfpou-2027-01-10-chrmcc`
7. `fptc-nfl-rbfpou-2027-01-10-chuhub`
8. `fptc-nfl-rbfpou-2027-01-10-davmon`
9. `fptc-nfl-rbfpou-2027-01-10-jadpri`
10. `fptc-nfl-rbfpou-2027-01-10-jamcoo`
11. `fptc-nfl-rbfpou-2027-01-10-jaywar`
12. `fptc-nfl-rbfpou-2027-01-10-jdob`
13. `fptc-nfl-rbfpou-2027-01-10-kenwal`
14. `fptc-nfl-rbfpou-2027-01-10-kyrwil`
15. `fptc-nfl-rbfpou-2027-01-10-omaham`
16. `fptc-nfl-rbfpou-2027-01-10-racwhi`
17. `fptc-nfl-rbfpou-2027-01-10-rhaste`
18. `fptc-nfl-rbfpou-2027-01-10-rjhar`
19. `fptc-nfl-rbfpou-2027-01-10-tylall`
20. `fptc-nfl-rbfpou-2027-01-10-tyrtra`
21. `fptc-nfl-rbfpou-2027-01-10-woomar`

</details>

</details>
<details><summary><code>aachc-cfb-wins-2026-11-28-uk-5pt5wins</code> BUY 2 @ 43¢ → $1.18/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 43¢ | 4 (2 yours) | ×0.5^0 = 4.2 |
|  | 41¢ | 0 | ×0.5^2 = 0.0 |
|  | 22¢ | 2,272 | ×0.5^21 = 0.0 |
|  | 21¢ | 50 | ×0.5^22 = 0.0 |
|  | 17¢ | 42 | ×0.5^26 = 0.0 |
|  | 16¢ | 16,000 | ×0.5^27 = 0.0 |
| | | **Σ** | **4.2** |

`yours 2.0 / Σ 4.2 = 47.1%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 47.1% = $1.18/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `aachc-cfb-wins-2026-11-28-uk-2pt5wins`
2. `aachc-cfb-wins-2026-11-28-uk-3pt5wins`
3. `aachc-cfb-wins-2026-11-28-uk-4pt5wins`
4. `aachc-cfb-wins-2026-11-28-uk-5pt5wins` ← this one
5. `aachc-cfb-wins-2026-11-28-uk-6pt5wins`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-andbes</code> SELL 1 @ 12¢ → $2.76/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 14¢ | 2 | ×0.2^2 = 0.1 |
|  | 15¢ | 1 | ×0.2^3 = 0.0 |
|  | 16¢ | 16 | ×0.2^4 = 0.0 |
|  | 17¢ | 62 | ×0.2^5 = 0.0 |
|  | 19¢ | 4 | ×0.2^7 = 0.0 |
|  | 26¢ | 21,040 | ×0.2^14 = 0.0 |
| | | **Σ** | **2.1** |

`yours 1.0 / Σ 2.1 = 46.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 46.9% = $2.76/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes` ← this one
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
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-micoba</code> BUY 9,253 @ 1¢ → $2.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 3 | ×0.2^0 = 3.0 |
|  | 2¢ | 3 | ×0.2^1 = 0.6 |
| ▶ | 1¢ | 20,023 (9,253 yours) | ×0.2^2 = 800.9 |
| | | **Σ** | **804.5** |

`yours 370.1 / Σ 804.5 = 46.0%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 46.0% = $2.71/day`  

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
12. `enwc-uspres-nom-dem-2028-micoba` ← this one
13. `enwc-uspres-nom-dem-2028-petbut`
14. `enwc-uspres-nom-dem-2028-rahema`
15. `enwc-uspres-nom-dem-2028-rokha`
16. `enwc-uspres-nom-dem-2028-stasmi`
17. `enwc-uspres-nom-dem-2028-wesmoo`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-petbut</code> SELL 1 @ 16¢ → $2.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 16¢ | 2 (1 yours) | ×0.2^0 = 2.0 |
|  | 17¢ | 1 | ×0.2^1 = 0.2 |
|  | 18¢ | 1 | ×0.2^2 = 0.0 |
|  | 20¢ | 2 | ×0.2^4 = 0.0 |
|  | 21¢ | 24 | ×0.2^5 = 0.0 |
|  | 24¢ | 22,165 | ×0.2^8 = 0.1 |
| | | **Σ** | **2.3** |

`yours 1.0 / Σ 2.3 = 43.3%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 43.3% = $2.55/day`  

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
<details><summary><code>ewc-usp-2028-11-07-rokha</code> BUY 9,546 @ 1¢ → $1.60/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 1¢ | 22,072 (9,546 yours) | ×0.2^0 = 22,072.0 |
| | | **Σ** | **22,072.0** |

`yours 9,546.0 / Σ 22,072.0 = 43.2%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 43.2% = $1.60/day`  

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
20. `ewc-usp-2028-11-07-rokha` ← this one
21. `ewc-usp-2028-11-07-rondes`
22. `ewc-usp-2028-11-07-stasmi`
23. `ewc-usp-2028-11-07-thomas`
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-thomas</code> SELL 3 @ 3¢ → $1.59/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 7 (3 yours) | ×0.2^0 = 7.0 |
|  | 7¢ | 1 | ×0.2^4 = 0.0 |
|  | 8¢ | 17 | ×0.2^5 = 0.0 |
|  | 20¢ | 206 | ×0.2^17 = 0.0 |
|  | 21¢ | 51,071 | ×0.2^18 = 0.0 |
| | | **Σ** | **7.0** |

`yours 3.0 / Σ 7.0 = 42.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 42.8% = $1.59/day`  

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
23. `ewc-usp-2028-11-07-thomas` ← this one
24. `ewc-usp-2028-11-07-tuccar`
25. `ewc-usp-2028-11-07-tulgab`
26. `ewc-usp-2028-11-07-vivram`
27. `ewc-usp-2028-11-07-wesmoo`

</details>

</details>
<details><summary><code>ewc-usp-2028-11-07-elomus</code> SELL 3 @ 5¢ → $1.58/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 5¢ | 7 (3 yours) | ×0.2^0 = 7.0 |
|  | 8¢ | 1 | ×0.2^3 = 0.0 |
|  | 10¢ | 1 | ×0.2^5 = 0.0 |
|  | 11¢ | 100 | ×0.2^6 = 0.0 |
|  | 12¢ | 3 | ×0.2^7 = 0.0 |
|  | 14¢ | 2 | ×0.2^9 = 0.0 |
|  | 16¢ | 4 | ×0.2^11 = 0.0 |
|  | 17¢ | 275 | ×0.2^12 = 0.0 |
|  | 20¢ | 31,021 | ×0.2^15 = 0.0 |
| | | **Σ** | **7.0** |

`yours 3.0 / Σ 7.0 = 42.8%`  
`$200 ÷ 27 ÷ 2 = $3.70 × 42.8% = $1.58/day`  

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
<details><summary><code>enwc-uspres-nom-rep-2028-tulgab</code> BUY 19,238 @ 1¢ → $3.05/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 131 | ×0.2^0 = 131.3 |
| ▶ | 1¢ | 41,788 (19,238 yours) | ×0.2^2 = 1,671.5 |
| | | **Σ** | **1,802.9** |

`yours 769.5 / Σ 1,802.9 = 42.7%`  
`$200 ÷ 14 ÷ 2 = $7.14 × 42.7% = $3.05/day`  

<details><summary>÷ 14 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-rep-2028-dontru`
2. `enwc-uspres-nom-rep-2028-dontrujr`
3. `enwc-uspres-nom-rep-2028-elomus`
4. `enwc-uspres-nom-rep-2028-gleyou`
5. `enwc-uspres-nom-rep-2028-jdvan`
6. `enwc-uspres-nom-rep-2028-margre`
7. `enwc-uspres-nom-rep-2028-marrub`
8. `enwc-uspres-nom-rep-2028-ranpau`
9. `enwc-uspres-nom-rep-2028-rondes`
10. `enwc-uspres-nom-rep-2028-tedcru`
11. `enwc-uspres-nom-rep-2028-thomas`
12. `enwc-uspres-nom-rep-2028-tuccar`
13. `enwc-uspres-nom-rep-2028-tulgab` ← this one
14. `enwc-uspres-nom-rep-2028-vivram`

</details>

</details>
<details><summary><code>enwc-uspres-nom-dem-2028-dwajoh</code> BUY 19,311 @ 1¢ → $2.46/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 3¢ | 133 | ×0.2^0 = 133.3 |
|  | 2¢ | 250 | ×0.2^1 = 50.0 |
| ▶ | 1¢ | 41,538 (19,311 yours) | ×0.2^2 = 1,661.5 |
| | | **Σ** | **1,844.9** |

`yours 772.4 / Σ 1,844.9 = 41.9%`  
`$200 ÷ 17 ÷ 2 = $5.88 × 41.9% = $2.46/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `enwc-uspres-nom-dem-2028-aleocc`
2. `enwc-uspres-nom-dem-2028-andbes`
3. `enwc-uspres-nom-dem-2028-dwajoh` ← this one
4. `enwc-uspres-nom-dem-2028-gavnew`
5. `enwc-uspres-nom-dem-2028-jamtal`
6. `enwc-uspres-nom-dem-2028-jbpri`
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

## 📊 Estimate vs. actual — where the gap is

_Collecting estimate history (started 2026-07-18). This comparison fills in once Polymarket posts results for a day with estimate coverage — about two days._

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `dipcc-us-iran-contnts-2026--dilut` | $75.00 ÷ 6 | 0.25 | 2,000 | BUY side (2,494 resting) | ~99.5% | ~$6.22 |
| `dipcc-us-iran-contnts-2026--enrcaplte5` | $75.00 ÷ 6 | 0.25 | 2,000 | SELL side (9,793 resting) | ~99.5% | ~$6.22 |
| `dipcc-us-iran-contnts-2026--irnfnd` | $75.00 ÷ 6 | 0.25 | 2,000 | BUY side (4,906 resting) | ~98.7% | ~$6.17 |
| `dipcc-us-iran-contnts-2026--enrmor` | $75.00 ÷ 6 | 0.25 | 2,000 | SELL side (9,414 resting) | ~69.9% | ~$4.37 |
| `dipcc-us-iran-contnts-2026--urnsur` | $75.00 ÷ 6 | 0.25 | 2,000 | BUY side (3,914 resting) | ~56.1% | ~$3.50 |
| `dipcc-us-iran-contnts-2026--enrcap` | $75.00 ÷ 6 | 0.25 | 2,000 | BUY side (2,500 resting) | ~22.2% | ~$1.39 |
| `apdc-jerpowgov-2026-08-31` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (5,718 resting) | ~4.5% | ~$1.12 |

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
| 2026-08-20 10:40 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 9:32 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 8:31 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 7:30 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 6:13 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 4:57 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 3:54 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 2:53 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 1:52 AM ET | ✅ ok | 2859 | $5117.59 |
| 2026-08-20 12:49 AM ET | ✅ ok | 2859 | $5117.59 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
