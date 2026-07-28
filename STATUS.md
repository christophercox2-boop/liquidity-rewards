# Polymarket US — Liquidity Rewards

[![Track liquidity rewards](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml/badge.svg)](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml)

## ✅ Last successful check: 2026-07-28 6:28 PM ET

This runs automatically every hour. **If the timestamp above is more than ~2 hours old, something is broken** — check the [Actions tab](https://github.com/wfco223/Liquidity-rewards/actions/workflows/liquidity-rewards.yml).

## 📌 Summary

**Earning right now:** ~$123.22/day estimated (ceiling, not promise — details below)

**Earned:** $1,116.10 lifetime ($1,114.89 paid). Last three recorded days — 2026-07-26: **$153.80** · 2026-07-25: **$125.69** · 2026-07-24: **$135.19** _(Polymarket reports ~1–2 days behind)_

**What else to join:** `paccc-usho-midterms-2026-11-03-dem` — BUY at the best price, ~$70.09/day for 200 contracts. Runners-up: `paccc-usse-midterms-2026-11-03-rep` (~$25.90/day), `enwc-ussep-mn-2026-08-11-dem-pegfla` (~$20.96/day)

---

# The details (how the numbers above are computed)

## 📍 Right now — your resting orders

### Estimated earning rate: ~$123.22/day (~$5.13/hour)

Rough estimate — assumes the books, pools, and your orders stay as they are, both sides keep qualifying, each pool covers its whole event/race (so it's divided across that race's open markets), and splits evenly between bid and ask. Scored with the official formula: `DiscountFactor ^ (ticks from best price) × size`, counting only orders inside the Target Size window. Earning orders first.

| Market | Side | Price | Size | Ticks off best | Reward pool | Earning? |
|---|---|---:|---:|---:|---:|---|
| `vmc-ussep-misen-2026-08-04-els5-10` | BUY | 26.0¢ | 47 | 0 | $25.00 | ✅ scoring — ~100.0% of bid side (2,524 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-ste15-20` | SELL | 2.0¢ | 1 | 0 | $25.00 | ✅ scoring — ~100.0% of ask side (43,495 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `vmc-ussep-misen-2026-08-04-els5-10` | SELL | 39.0¢ | 21 | 0 | $25.00 | ✅ scoring — ~99.9% of ask side (2,098 resting ≥ 2,000 ✓) ≈ $1.25/day (pool ÷ 10 markets) |
| `apdc-trumpadmin-2026-howlut` | BUY | 39.0¢ | 31 | 0 | $25.00 | ✅ scoring — ~96.9% of bid side (50,693 resting ≥ 2,000 ✓) ≈ $0.71/day (pool ÷ 17 markets) |
| `apdc-andburpm-2026-12-31` | SELL | 32.0¢ | 17 | 0 | $25.00 | ✅ scoring — ~93.0% of ask side (5,370 resting ≥ 2,000 ✓) ≈ $11.62/day |
| `iarc-group-2026-12-31-bilcli` | BUY | 4.0¢ | 625 | 1 | $25.00 | ✅ scoring — ~59.2% of bid side (41,078 resting ≥ 2,000 ✓) ≈ $0.74/day (pool ÷ 10 markets) |
| `pintc-meet-trump-2026-12-31-zohmam` | BUY | 7.0¢ | 178 | 0 | $25.00 | ✅ scoring — ~59.1% of bid side (50,600 resting ≥ 2,000 ✓) ≈ $0.57/day (pool ÷ 13 markets) |
| `iarc-group-2026-12-31-joebid` | BUY | 4.0¢ | 625 | 1 | $25.00 | ✅ scoring — ~58.4% of bid side (16,093 resting ≥ 2,000 ✓) ≈ $0.73/day (pool ÷ 10 markets) |
| `pintc-meet-trump-2026-12-31-kanwes` | BUY | 9.0¢ | 277 | 1 | $25.00 | ✅ scoring — ~57.9% of bid side (10,687 resting ≥ 2,000 ✓) ≈ $0.56/day (pool ÷ 13 markets) |
| `pintc-meet-trump-2026-12-31-kimkar` | BUY | 9.0¢ | 277 | 1 | $25.00 | ✅ scoring — ~57.9% of bid side (10,688 resting ≥ 2,000 ✓) ≈ $0.56/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-53` | SELL | 19.0¢ | 31 | 2 | $100.00 | ✅ scoring — ~52.9% of ask side (141,636 resting ≥ 5,000 ✓) ≈ $2.03/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-lte45` | SELL | 12.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~47.3% of ask side (103,449 resting ≥ 5,000 ✓) ≈ $1.82/day (pool ÷ 13 markets) |
| `scc-senate-gop-2026-11-03-55` | SELL | 12.0¢ | 50 | 0 | $100.00 | ✅ scoring — ~46.1% of ask side (141,770 resting ≥ 5,000 ✓) ≈ $1.77/day (pool ÷ 13 markets) |
| `pintc-meet-trump-2026-12-31-volzel` | BUY | 62.0¢ | 19 | 0 | $25.00 | ✅ scoring — ~45.8% of bid side (52,984 resting ≥ 2,000 ✓) ≈ $0.44/day (pool ÷ 13 markets) |
| `cranc-uspres28-12-31-2026-krinoe` | BUY | 10.0¢ | 250 | 2 | $100.00 | ✅ scoring — ~43.2% of bid side (10,642 resting ≥ 5,000 ✓) ≈ $0.65/day (pool ÷ 33 markets) |
| `iarc-group-2026-12-31-tomhom` | BUY | 4.0¢ | 625 | 1 | $25.00 | ✅ scoring — ~40.9% of bid side (47,321 resting ≥ 2,000 ✓) ≈ $0.51/day (pool ÷ 10 markets) |
| `cranc-uspres28-12-31-2026-micoba` | BUY | 4.0¢ | 625 | 1 | $100.00 | ✅ scoring — ~38.4% of bid side (82,534 resting ≥ 5,000 ✓) ≈ $0.58/day (pool ÷ 33 markets) |
| `opdc-delrod-venpres-2026-12-31` | BUY | 17.0¢ | 147 | 0 | $25.00 | ✅ scoring — ~37.9% of bid side (50,590 resting ≥ 2,000 ✓) ≈ $2.37/day (pool ÷ 2 markets) |
| `cranc-uspres28-12-31-2026-hilcli` | BUY | 5.0¢ | 500 | 1 | $100.00 | ✅ scoring — ~37.4% of bid side (61,849 resting ≥ 5,000 ✓) ≈ $0.57/day (pool ÷ 33 markets) |
| `apdc-petehegseth-2026-08-31` | BUY | 4.0¢ | 625 | 1 | $100.00 | ✅ scoring — ~36.9% of bid side (51,263 resting ≥ 5,000 ✓) ≈ $6.16/day (pool ÷ 3 markets) |
| `cranc-uspres28-12-31-2026-kamhar` | SELL | 18.0¢ | 42 | 0 | $100.00 | ✅ scoring — ~36.1% of ask side (10,436 resting ≥ 5,000 ✓) ≈ $0.55/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-margre` | BUY | 10.0¢ | 250 | 0 | $100.00 | ✅ scoring — ~32.7% of bid side (51,034 resting ≥ 5,000 ✓) ≈ $0.50/day (pool ÷ 33 markets) |
| `scc-senate-gop-2026-11-03-46` | SELL | 13.0¢ | 10 | 0 | $100.00 | ✅ scoring — ~32.2% of ask side (92,689 resting ≥ 5,000 ✓) ≈ $1.24/day (pool ÷ 13 markets) |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | SELL | 74.0¢ | 84 | 0 | $300.00 | ✅ scoring — ~29.8% of ask side (80,447 resting ≥ 10,000 ✓) ≈ $14.91/day (pool ÷ 3 markets) |
| `apdc-andburpm-2026-12-31` | BUY | 3.0¢ | 1,248 | 0 | $25.00 | ✅ scoring — ~28.5% of bid side (5,947 resting ≥ 2,000 ✓) ≈ $3.57/day |
| `scc-senate-gop-2026-11-03-47` | SELL | 19.0¢ | 5 | 0 | $100.00 | ✅ scoring — ~28.4% of ask side (108,511 resting ≥ 5,000 ✓) ≈ $1.09/day (pool ÷ 13 markets) |
| `mlaec-swepm-2026-09-13-magand` | SELL | 95.0¢ | 192 | 0 | $25.00 | ✅ scoring — ~27.8% of ask side (5,642 resting ≥ 2,000 ✓) ≈ $0.69/day (pool ÷ 5 markets) |
| `cranc-uspres28-12-31-2026-jdvan` | BUY | 8.0¢ | 312 | 1 | $100.00 | ✅ scoring — ~27.6% of bid side (51,097 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 33 markets) |
| `cranc-uspres28-12-31-2026-elomus` | BUY | 7.0¢ | 357 | 1 | $100.00 | ✅ scoring — ~27.5% of bid side (20,966 resting ≥ 5,000 ✓) ≈ $0.42/day (pool ÷ 33 markets) |
| `enwc-ussep-mi-2026-08-04-dem-abdels` | SELL | 74.0¢ | 77 | 0 | $300.00 | ✅ scoring — ~27.3% of ask side (80,447 resting ≥ 10,000 ✓) ≈ $13.67/day (pool ÷ 3 markets) |
| …and 181 more | | | | | | |

**Tap an order for its book window and the math:**

<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> BUY 47 @ 26¢ → $1.25/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 26¢ | 47 (47 yours) | ×0.1^0 = 47.0 |
|  | 20¢ | 24 | ×0.1^6 = 0.0 |
|  | 18¢ | 51 | ×0.1^8 = 0.0 |
|  | 5¢ | 2 | ×0.1^21 = 0.0 |
|  | 1¢ | 2,400 | ×0.1^25 = 0.0 |
| | | **Σ** | **47.0** |

`yours 47.0 / Σ 47.0 = 100.0%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 100.0% = $1.25/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10` ← this one
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-ste15-20</code> SELL 1 @ 2¢ → $1.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 2¢ | 1 (1 yours) | ×0.1^0 = 1.0 |
|  | 8¢ | 6 | ×0.1^6 = 0.0 |
|  | 9¢ | 18 | ×0.1^7 = 0.0 |
|  | 16¢ | 100 | ×0.1^14 = 0.0 |
|  | 20¢ | 3 | ×0.1^18 = 0.0 |
|  | 30¢ | 2 | ×0.1^28 = 0.0 |
|  | 43¢ | 3,387 | ×0.1^41 = 0.0 |
| | | **Σ** | **1.0** |

`yours 1.0 / Σ 1.0 = 100.0%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 100.0% = $1.25/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10`
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20` ← this one
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>vmc-ussep-misen-2026-08-04-els5-10</code> SELL 21 @ 39¢ → $1.25/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 39¢ | 21 (21 yours) | ×0.1^0 = 21.0 |
|  | 42¢ | 6 | ×0.1^3 = 0.0 |
|  | 43¢ | 74 | ×0.1^4 = 0.0 |
|  | 45¢ | 18 | ×0.1^6 = 0.0 |
|  | 99¢ | 1,979 | ×0.1^60 = 0.0 |
| | | **Σ** | **21.0** |

`yours 21.0 / Σ 21.0 = 99.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 99.9% = $1.25/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `vmc-ussep-misen-2026-08-04-els0-5`
2. `vmc-ussep-misen-2026-08-04-els10-15`
3. `vmc-ussep-misen-2026-08-04-els15-20`
4. `vmc-ussep-misen-2026-08-04-els5-10` ← this one
5. `vmc-ussep-misen-2026-08-04-elsgte20`
6. `vmc-ussep-misen-2026-08-04-ste0-5`
7. `vmc-ussep-misen-2026-08-04-ste05-10`
8. `vmc-ussep-misen-2026-08-04-ste10-15`
9. `vmc-ussep-misen-2026-08-04-ste15-20`
10. `vmc-ussep-misen-2026-08-04-stegte20`

</details>

</details>
<details><summary><code>apdc-trumpadmin-2026-howlut</code> BUY 31 @ 39¢ → $0.71/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 39¢ | 31 (31 yours) | ×0.1^0 = 31.0 |
|  | 37¢ | 100 | ×0.1^2 = 1.0 |
|  | 35¢ | 10 | ×0.1^4 = 0.0 |
|  | 5¢ | 227 | ×0.1^34 = 0.0 |
|  | 2¢ | 50,000 | ×0.1^37 = 0.0 |
| | | **Σ** | **32.0** |

`yours 31.0 / Σ 32.0 = 96.9%`  
`$25 ÷ 17 ÷ 2 = $0.74 × 96.9% = $0.71/day`  

<details><summary>÷ 17 markets in this race — tap to list</summary>

1. `apdc-trumpadmin-2026-brorol`
2. `apdc-trumpadmin-2026-howlut` ← this one
3. `apdc-trumpadmin-2026-johrat`
4. `apdc-trumpadmin-2026-karlea`
5. `apdc-trumpadmin-2026-kaspat`
6. `apdc-trumpadmin-2026-linmcm`
7. `apdc-trumpadmin-2026-marrub`
8. `apdc-trumpadmin-2026-petheg`
9. `apdc-trumpadmin-2026-robken`
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
<details><summary><code>apdc-andburpm-2026-12-31</code> SELL 17 @ 32¢ → $11.62/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 32¢ | 17 (17 yours) | ×0.1^0 = 17.0 |
|  | 34¢ | 117 | ×0.1^2 = 1.2 |
|  | 35¢ | 120 | ×0.1^3 = 0.1 |
|  | 99¢ | 5,116 | ×0.1^67 = 0.0 |
| | | **Σ** | **18.3** |

`yours 17.0 / Σ 18.3 = 93.0%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 93.0% = $11.62/day`  

</details>
<details><summary><code>iarc-group-2026-12-31-bilcli</code> BUY 625 @ 4¢ → $0.74/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 3 | ×0.1^0 = 3.0 |
| ▶ | 4¢ | 875 (625 yours) | ×0.1^1 = 87.5 |
|  | 2¢ | 15,000 | ×0.1^3 = 15.0 |
| | | **Σ** | **105.5** |

`yours 62.5 / Σ 105.5 = 59.2%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 59.2% = $0.74/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `iarc-group-2026-12-31-antfau`
2. `iarc-group-2026-12-31-baroba`
3. `iarc-group-2026-12-31-bilcli` ← this one
4. `iarc-group-2026-12-31-canowe`
5. `iarc-group-2026-12-31-gavnew`
6. `iarc-group-2026-12-31-hilcli`
7. `iarc-group-2026-12-31-joebid`
8. `iarc-group-2026-12-31-johbre`
9. `iarc-group-2026-12-31-tomhom`
10. `iarc-group-2026-12-31-tuccar`

</details>

</details>
<details><summary><code>pintc-meet-trump-2026-12-31-zohmam</code> BUY 178 @ 7¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 7¢ | 300 (178 yours) | ×0.1^0 = 300.0 |
|  | 5¢ | 100 | ×0.1^2 = 1.0 |
|  | 1¢ | 50,200 | ×0.1^6 = 0.1 |
| | | **Σ** | **301.1** |

`yours 178.0 / Σ 301.1 = 59.1%`  
`$25 ÷ 13 ÷ 2 = $0.96 × 59.1% = $0.57/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon`
6. `pintc-meet-trump-2026-12-31-kimkar`
7. `pintc-meet-trump-2026-12-31-leoxiv`
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput`
11. `pintc-meet-trump-2026-12-31-volzel`
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam` ← this one

</details>

</details>
<details><summary><code>iarc-group-2026-12-31-joebid</code> BUY 625 @ 4¢ → $0.73/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 18 | ×0.1^0 = 18.0 |
| ▶ | 4¢ | 875 (625 yours) | ×0.1^1 = 87.5 |
|  | 1¢ | 15,200 | ×0.1^4 = 1.5 |
| | | **Σ** | **107.0** |

`yours 62.5 / Σ 107.0 = 58.4%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 58.4% = $0.73/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `iarc-group-2026-12-31-antfau`
2. `iarc-group-2026-12-31-baroba`
3. `iarc-group-2026-12-31-bilcli`
4. `iarc-group-2026-12-31-canowe`
5. `iarc-group-2026-12-31-gavnew`
6. `iarc-group-2026-12-31-hilcli`
7. `iarc-group-2026-12-31-joebid` ← this one
8. `iarc-group-2026-12-31-johbre`
9. `iarc-group-2026-12-31-tomhom`
10. `iarc-group-2026-12-31-tuccar`

</details>

</details>
<details><summary><code>pintc-meet-trump-2026-12-31-kanwes</code> BUY 277 @ 9¢ → $0.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 9¢ | 458 (277 yours) | ×0.1^1 = 45.8 |
|  | 5¢ | 2 | ×0.1^5 = 0.0 |
|  | 1¢ | 10,225 | ×0.1^9 = 0.0 |
| | | **Σ** | **47.8** |

`yours 27.7 / Σ 47.8 = 57.9%`  
`$25 ÷ 13 ÷ 2 = $0.96 × 57.9% = $0.56/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes` ← this one
5. `pintc-meet-trump-2026-12-31-kimjon`
6. `pintc-meet-trump-2026-12-31-kimkar`
7. `pintc-meet-trump-2026-12-31-leoxiv`
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput`
11. `pintc-meet-trump-2026-12-31-volzel`
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam`

</details>

</details>
<details><summary><code>pintc-meet-trump-2026-12-31-kimkar</code> BUY 277 @ 9¢ → $0.56/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 10¢ | 2 | ×0.1^0 = 2.0 |
| ▶ | 9¢ | 458 (277 yours) | ×0.1^1 = 45.8 |
|  | 7¢ | 1 | ×0.1^3 = 0.0 |
|  | 5¢ | 2 | ×0.1^5 = 0.0 |
|  | 1¢ | 10,225 | ×0.1^9 = 0.0 |
| | | **Σ** | **47.8** |

`yours 27.7 / Σ 47.8 = 57.9%`  
`$25 ÷ 13 ÷ 2 = $0.96 × 57.9% = $0.56/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon`
6. `pintc-meet-trump-2026-12-31-kimkar` ← this one
7. `pintc-meet-trump-2026-12-31-leoxiv`
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput`
11. `pintc-meet-trump-2026-12-31-volzel`
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-53</code> SELL 31 @ 19¢ → $2.03/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
|  | 17¢ | 1 | ×0.2^0 = 0.6 |
| ▶ | 19¢ | 43 (31 yours) | ×0.2^2 = 1.7 |
|  | 20¢ | 3 | ×0.2^3 = 0.0 |
|  | 30¢ | 4 | ×0.2^13 = 0.0 |
|  | 50¢ | 100 | ×0.2^33 = 0.0 |
|  | 98¢ | 131,484 | ×0.2^81 = 0.0 |
| | | **Σ** | **2.3** |

`yours 1.2 / Σ 2.3 = 52.9%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 52.9% = $2.03/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-lte45</code> SELL 10 @ 12¢ → $1.82/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 21 (10 yours) | ×0.2^0 = 21.0 |
|  | 13¢ | 1 | ×0.2^1 = 0.1 |
|  | 15¢ | 1 | ×0.2^3 = 0.0 |
|  | 16¢ | 5 | ×0.2^4 = 0.0 |
|  | 20¢ | 3 | ×0.2^8 = 0.0 |
|  | 30¢ | 4 | ×0.2^18 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 97¢ | 53,855 | ×0.2^85 = 0.0 |
| | | **Σ** | **21.1** |

`yours 10.0 / Σ 21.1 = 47.3%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 47.3% = $1.82/day`  

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
<details><summary><code>scc-senate-gop-2026-11-03-55</code> SELL 50 @ 12¢ → $1.77/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 12¢ | 96 (50 yours) | ×0.2^0 = 96.0 |
|  | 13¢ | 62 | ×0.2^1 = 12.4 |
|  | 18¢ | 19 | ×0.2^6 = 0.0 |
|  | 20¢ | 3 | ×0.2^8 = 0.0 |
|  | 30¢ | 4 | ×0.2^18 = 0.0 |
|  | 50¢ | 100 | ×0.2^38 = 0.0 |
|  | 98¢ | 131,484 | ×0.2^86 = 0.0 |
| | | **Σ** | **108.4** |

`yours 50.0 / Σ 108.4 = 46.1%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 46.1% = $1.77/day`  

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
<details><summary><code>pintc-meet-trump-2026-12-31-volzel</code> BUY 19 @ 62¢ → $0.44/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 62¢ | 35 (19 yours) | ×0.1^0 = 35.0 |
|  | 60¢ | 650 | ×0.1^2 = 6.5 |
|  | 52¢ | 85 | ×0.1^10 = 0.0 |
|  | 50¢ | 2,002 | ×0.1^12 = 0.0 |
| | | **Σ** | **41.5** |

`yours 19.0 / Σ 41.5 = 45.8%`  
`$25 ÷ 13 ÷ 2 = $0.96 × 45.8% = $0.44/day`  

<details><summary>÷ 13 markets in this race — tap to list</summary>

1. `pintc-meet-trump-2026-12-31-delrod`
2. `pintc-meet-trump-2026-12-31-elomus`
3. `pintc-meet-trump-2026-12-31-joerog`
4. `pintc-meet-trump-2026-12-31-kanwes`
5. `pintc-meet-trump-2026-12-31-kimjon`
6. `pintc-meet-trump-2026-12-31-kimkar`
7. `pintc-meet-trump-2026-12-31-leoxiv`
8. `pintc-meet-trump-2026-12-31-mojkha`
9. `pintc-meet-trump-2026-12-31-talswi`
10. `pintc-meet-trump-2026-12-31-vlaput`
11. `pintc-meet-trump-2026-12-31-volzel` ← this one
12. `pintc-meet-trump-2026-12-31-xijin`
13. `pintc-meet-trump-2026-12-31-zohmam`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-krinoe</code> BUY 250 @ 10¢ → $0.65/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 12¢ | 4 | ×0.2^0 = 4.2 |
|  | 11¢ | 12 | ×0.2^1 = 2.4 |
| ▶ | 10¢ | 415 (250 yours) | ×0.2^2 = 16.6 |
|  | 5¢ | 11 | ×0.2^7 = 0.0 |
|  | 1¢ | 10,200 | ×0.2^11 = 0.0 |
| | | **Σ** | **23.2** |

`yours 10.0 / Σ 23.2 = 43.2%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 43.2% = $0.65/day`  

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
18. `cranc-uspres28-12-31-2026-krinoe` ← this one
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
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>iarc-group-2026-12-31-tomhom</code> BUY 625 @ 4¢ → $0.51/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 3 | ×0.1^0 = 3.0 |
| ▶ | 4¢ | 875 (625 yours) | ×0.1^1 = 87.5 |
|  | 3¢ | 6,243 | ×0.1^2 = 62.4 |
| | | **Σ** | **152.9** |

`yours 62.5 / Σ 152.9 = 40.9%`  
`$25 ÷ 10 ÷ 2 = $1.25 × 40.9% = $0.51/day`  

<details><summary>÷ 10 markets in this race — tap to list</summary>

1. `iarc-group-2026-12-31-antfau`
2. `iarc-group-2026-12-31-baroba`
3. `iarc-group-2026-12-31-bilcli`
4. `iarc-group-2026-12-31-canowe`
5. `iarc-group-2026-12-31-gavnew`
6. `iarc-group-2026-12-31-hilcli`
7. `iarc-group-2026-12-31-joebid`
8. `iarc-group-2026-12-31-johbre`
9. `iarc-group-2026-12-31-tomhom` ← this one
10. `iarc-group-2026-12-31-tuccar`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-micoba</code> BUY 625 @ 4¢ → $0.58/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 70 | ×0.2^0 = 70.0 |
| ▶ | 4¢ | 625 (625 yours) | ×0.2^1 = 125.0 |
|  | 1¢ | 81,839 | ×0.2^4 = 130.9 |
| | | **Σ** | **325.9** |

`yours 125.0 / Σ 325.9 = 38.4%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 38.4% = $0.58/day`  

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
22. `cranc-uspres28-12-31-2026-micoba` ← this one
23. `cranc-uspres28-12-31-2026-nikhal`
24. `cranc-uspres28-12-31-2026-oprwin`
25. `cranc-uspres28-12-31-2026-petbut`
26. `cranc-uspres28-12-31-2026-rahema`
27. `cranc-uspres28-12-31-2026-robken`
28. `cranc-uspres28-12-31-2026-steban`
29. `cranc-uspres28-12-31-2026-stesmi`
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>opdc-delrod-venpres-2026-12-31</code> BUY 147 @ 17¢ → $2.37/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 17¢ | 388 (147 yours) | ×0.1^0 = 387.9 |
|  | 5¢ | 2 | ×0.1^12 = 0.0 |
|  | 1¢ | 50,200 | ×0.1^16 = 0.0 |
| | | **Σ** | **387.9** |

`yours 147.0 / Σ 387.9 = 37.9%`  
`$25 ÷ 2 ÷ 2 = $6.25 × 37.9% = $2.37/day`  

<details><summary>÷ 2 markets in this race — tap to list</summary>

1. `opdc-delrod-venpres-2026-12-31` ← this one
2. `opdc-delrod-venpres-2027-06-30`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-hilcli</code> BUY 500 @ 5¢ → $0.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 6¢ | 147 | ×0.2^0 = 147.3 |
| ▶ | 5¢ | 502 (500 yours) | ×0.2^1 = 100.4 |
|  | 1¢ | 61,200 | ×0.2^5 = 19.6 |
| | | **Σ** | **267.3** |

`yours 100.0 / Σ 267.3 = 37.4%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 37.4% = $0.57/day`  

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
12. `cranc-uspres28-12-31-2026-hilcli` ← this one
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
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>apdc-petehegseth-2026-08-31</code> BUY 625 @ 4¢ → $6.16/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 5¢ | 63 | ×0.2^0 = 63.1 |
| ▶ | 4¢ | 975 (625 yours) | ×0.2^1 = 195.0 |
|  | 1¢ | 50,225 | ×0.2^4 = 80.4 |
| | | **Σ** | **338.4** |

`yours 125.0 / Σ 338.4 = 36.9%`  
`$100 ÷ 3 ÷ 2 = $16.67 × 36.9% = $6.16/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `apdc-petehegseth-2026-07-31`
2. `apdc-petehegseth-2026-08-31` ← this one
3. `apdc-petehegseth-2026-12-31`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-kamhar</code> SELL 42 @ 18¢ → $0.55/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 18¢ | 117 (42 yours) | ×0.2^0 = 117.3 |
|  | 24¢ | 24 | ×0.2^6 = 0.0 |
|  | 25¢ | 81 | ×0.2^7 = 0.0 |
|  | 28¢ | 9,661 | ×0.2^10 = 0.0 |
| | | **Σ** | **117.3** |

`yours 42.3 / Σ 117.3 = 36.1%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 36.1% = $0.55/day`  

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
17. `cranc-uspres28-12-31-2026-kamhar` ← this one
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
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-margre</code> BUY 250 @ 10¢ → $0.50/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 10¢ | 747 (250 yours) | ×0.2^0 = 747.0 |
|  | 9¢ | 85 | ×0.2^1 = 17.1 |
|  | 5¢ | 2 | ×0.2^5 = 0.0 |
|  | 1¢ | 50,200 | ×0.2^9 = 0.0 |
| | | **Σ** | **764.1** |

`yours 250.0 / Σ 764.1 = 32.7%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 32.7% = $0.50/day`  

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
19. `cranc-uspres28-12-31-2026-margre` ← this one
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
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>scc-senate-gop-2026-11-03-46</code> SELL 10 @ 13¢ → $1.24/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 13¢ | 31 (10 yours) | ×0.2^0 = 31.0 |
|  | 15¢ | 1 | ×0.2^2 = 0.0 |
|  | 20¢ | 3 | ×0.2^7 = 0.0 |
|  | 30¢ | 4 | ×0.2^17 = 0.0 |
|  | 50¢ | 100 | ×0.2^37 = 0.0 |
|  | 97¢ | 40,555 | ×0.2^84 = 0.0 |
| | | **Σ** | **31.0** |

`yours 10.0 / Σ 31.0 = 32.2%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 32.2% = $1.24/day`  

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
<details><summary><code>enwc-ussep-mi-2026-08-04-dem-abdels</code> SELL 84 @ 74¢ → $14.91/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 279 (84 yours) | ×0.2^0 = 279.0 |
|  | 80¢ | 42,000 | ×0.2^6 = 2.7 |
| | | **Σ** | **281.7** |

`yours 84.0 / Σ 281.7 = 29.8%`  
`$300 ÷ 3 ÷ 2 = $50.00 × 29.8% = $14.91/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `enwc-ussep-mi-2026-08-04-dem-abdels` ← this one
2. `enwc-ussep-mi-2026-08-04-dem-halste`
3. `enwc-ussep-mi-2026-08-04-dem-malmcm`

</details>

</details>
<details><summary><code>apdc-andburpm-2026-12-31</code> BUY 1,248 @ 3¢ → $3.57/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
| ▶ | 3¢ | 4,372 (1,248 yours) | ×0.1^0 = 4,372.0 |
| | | **Σ** | **4,372.0** |

`yours 1,248.0 / Σ 4,372.0 = 28.5%`  
`$25 ÷ 1 ÷ 2 = $12.50 × 28.5% = $3.57/day`  

</details>
<details><summary><code>scc-senate-gop-2026-11-03-47</code> SELL 5 @ 19¢ → $1.09/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 19¢ | 17 (5 yours) | ×0.2^0 = 17.0 |
|  | 20¢ | 3 | ×0.2^1 = 0.6 |
|  | 30¢ | 4 | ×0.2^11 = 0.0 |
|  | 50¢ | 100 | ×0.2^31 = 0.0 |
|  | 97¢ | 53,892 | ×0.2^78 = 0.0 |
| | | **Σ** | **17.6** |

`yours 5.0 / Σ 17.6 = 28.4%`  
`$100 ÷ 13 ÷ 2 = $3.85 × 28.4% = $1.09/day`  

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
<details><summary><code>mlaec-swepm-2026-09-13-magand</code> SELL 192 @ 95¢ → $0.69/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 95¢ | 192 (192 yours) | ×0.1^0 = 192.3 |
|  | 96¢ | 5,000 | ×0.1^1 = 500.0 |
| | | **Σ** | **692.3** |

`yours 192.3 / Σ 692.3 = 27.8%`  
`$25 ÷ 5 ÷ 2 = $2.50 × 27.8% = $0.69/day`  

<details><summary>÷ 5 markets in this race — tap to list</summary>

1. `mlaec-swepm-2026-09-13-ebbbus`
2. `mlaec-swepm-2026-09-13-jimake`
3. `mlaec-swepm-2026-09-13-magand` ← this one
4. `mlaec-swepm-2026-09-13-noodad`
5. `mlaec-swepm-2026-09-13-ulfkri`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-jdvan</code> BUY 312 @ 8¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 9¢ | 121 | ×0.2^0 = 121.0 |
| ▶ | 8¢ | 523 (312 yours) | ×0.2^1 = 104.6 |
|  | 6¢ | 70 | ×0.2^3 = 0.6 |
|  | 5¢ | 73 | ×0.2^4 = 0.1 |
|  | 1¢ | 50,310 | ×0.2^8 = 0.1 |
| | | **Σ** | **226.4** |

`yours 62.4 / Σ 226.4 = 27.6%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 27.6% = $0.42/day`  

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
14. `cranc-uspres28-12-31-2026-jdvan` ← this one
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
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>cranc-uspres28-12-31-2026-elomus</code> BUY 357 @ 7¢ → $0.42/day</summary>

| | Bids | Resting | Score |
|---|---:|---:|---:|
|  | 8¢ | 137 | ×0.2^0 = 136.7 |
| ▶ | 7¢ | 607 (357 yours) | ×0.2^1 = 121.4 |
|  | 6¢ | 20 | ×0.2^2 = 0.8 |
|  | 5¢ | 2 | ×0.2^3 = 0.0 |
|  | 1¢ | 20,200 | ×0.2^7 = 0.3 |
| | | **Σ** | **259.2** |

`yours 71.4 / Σ 259.2 = 27.5%`  
`$100 ÷ 33 ÷ 2 = $1.52 × 27.5% = $0.42/day`  

<details><summary>÷ 33 markets in this race — tap to list</summary>

1. `cranc-uspres28-12-31-2026-aleoca`
2. `cranc-uspres28-12-31-2026-andyan`
3. `cranc-uspres28-12-31-2026-bersan`
4. `cranc-uspres28-12-31-2026-betoro`
5. `cranc-uspres28-12-31-2026-corboo`
6. `cranc-uspres28-12-31-2026-dontru`
7. `cranc-uspres28-12-31-2026-dontrujr`
8. `cranc-uspres28-12-31-2026-dwajoh`
9. `cranc-uspres28-12-31-2026-elomus` ← this one
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
30. `cranc-uspres28-12-31-2026-tedcru`
31. `cranc-uspres28-12-31-2026-tuccar`
32. `cranc-uspres28-12-31-2026-vivram`
33. `cranc-uspres28-12-31-2026-zohmam`

</details>

</details>
<details><summary><code>enwc-ussep-mi-2026-08-04-dem-abdels</code> SELL 77 @ 74¢ → $13.67/day</summary>

| | Asks | Resting | Score |
|---|---:|---:|---:|
| ▶ | 74¢ | 279 (77 yours) | ×0.2^0 = 279.0 |
|  | 80¢ | 42,000 | ×0.2^6 = 2.7 |
| | | **Σ** | **281.7** |

`yours 77.0 / Σ 281.7 = 27.3%`  
`$300 ÷ 3 ÷ 2 = $50.00 × 27.3% = $13.67/day`  

<details><summary>÷ 3 markets in this race — tap to list</summary>

1. `enwc-ussep-mi-2026-08-04-dem-abdels` ← this one
2. `enwc-ussep-mi-2026-08-04-dem-halste`
3. `enwc-ussep-mi-2026-08-04-dem-malmcm`

</details>

</details>

## 📊 Estimate vs. actual — where the gap is

Time-averaged estimate for each day (across that day's hourly snapshots) vs. what Polymarket actually recorded. Days run midnight-to-midnight Eastern, matching the reward day. Low capture = your position decayed between snapshots (competition joining the best price, prices moving away, fills).

| Day | Estimated | Recorded | Captured |
|---|---:|---:|---:|
| 2026-07-26 | ~$159.09 | $153.80 | 97% |
| 2026-07-25 | ~$123.00 | $125.69 | 102% |
| 2026-07-24 | ~$133.49 | $135.19 | 101% |

Biggest gaps on 2026-07-26: `pvwc-housepopw-2026-11-03-dem` (est ~$3.30 → got $0.37), `vmc-ussep-misen-2026-08-04-els0-5` (est ~$3.67 → got $1.39), `lawec-cryptoleg-2026-08-10` (est ~$3.57 → got $2.35)

## 💡 Suggested U.S. political markets — active pools you're not in

U.S. politics only. Ranked by what a **200-contract order at the best price** would earn today, using each market's real book, Discount Factor, and Target Size (same assumptions as the earning rate above).

| Market | Reward pool | Discount | Target Size | Best entry | Est. share | Est. $/day |
|---|---:|---:|---:|---|---:|---:|
| `paccc-usho-midterms-2026-11-03-dem` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (1,116,735 resting) | ~93.5% | ~$70.09 |
| `paccc-usse-midterms-2026-11-03-rep` | $300.00 ÷ 2 | 0.20 | 10,000 | BUY side (780,529 resting) | ~34.5% | ~$25.90 |
| `enwc-ussep-mn-2026-08-11-dem-pegfla` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (40,044 resting) | ~83.9% | ~$20.96 |
| `enwc-usgubp-ok-2026-06-16-rep-gendru` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (92,145 resting) | ~73.5% | ~$18.38 |
| `enwc-usgubp-ok-2026-06-16-rep-mikmaz` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (64,325 resting) | ~59.9% | ~$14.98 |
| `enwc-ussep-mn-2026-08-11-dem-angcra` | $100.00 ÷ 2 | 0.20 | 5,000 | SELL side (80,586 resting) | ~25.5% | ~$6.37 |
| `scc-hrep-rep-2026-11-03-gte225` | $100.00 ÷ 12 | 0.20 | 5,000 | SELL side (5,029 resting) | ~91.1% | ~$3.80 |
| `scc-hrep-rep-2026-11-03-gte210` | $100.00 ÷ 12 | 0.20 | 5,000 | SELL side (5,509 resting) | ~83.6% | ~$3.48 |
| `enwc-ussep-mi-2026-08-04-dem-halste` | $300.00 ÷ 3 | 0.20 | 10,000 | BUY side (124,698 resting) | ~3.9% | ~$1.93 |
| `scc-hrep-rep-2026-11-03-gte215` | $100.00 ÷ 12 | 0.20 | 5,000 | BUY side (25,650 resting) | ~35.6% | ~$1.48 |
| `ewc-usgub-mi-2026-11-03-rep` | $25.00 ÷ 3 | 0.10 | 2,000 | BUY side (58,976 resting) | ~28.2% | ~$1.18 |
| `apdc-jerpowgov-2026-07-31` | $100.00 ÷ 3 | 0.20 | 5,000 | SELL side (6,887 resting) | ~6.9% | ~$1.15 |

## Totals

| | Amount |
|---|---:|
| Paid | $1,114.89 |
| Skipped | $1.21 |
| **Total earned** | **$1,116.10** |

823 reward rows · 24 days with rewards · 302 markets · since 2026-03-21

## Last 14 days

| Date | Rewards | |
|---|---:|---|
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
| 2026-07-14 | $13.16 | `█` |
| 2026-07-13 | $10.03 | `█` |

## By month

| Month | Rewards | |
|---|---:|---|
| 2026-07 | $1,116.10 | `████████████████████` |

## Top markets (lifetime)

| Market | Rewards |
|---|---:|
| `enwc-usgubp-wi-2026-08-11-dem-davcro` | $58.43 |
| `enwc-ussep-nh-2026-09-08-dem-karman` | $44.16 |
| `enwc-ussep-me-2026-07-27-dem-dankle` | $42.31 |
| `enwc-usgubp-wi-2026-08-11-dem-sarrod` | $38.65 |
| `apdc-jerpowgov-2026-12-31` | $38.36 |
| `vmc-ussep-misen-2026-08-04-ste10-15` | $34.11 |
| `opdc-mcconnell-resign-2026-11-02` | $32.64 |
| `enwc-usgubp-wi-2026-08-11-dem-kelroy` | $27.70 |
| `vmc-ussep-misen-2026-08-04-elsgte20` | $27.29 |
| `enwc-usgubp-wi-2026-08-11-dem-joebre` | $27.10 |
| `enwc-ussep-sc-2026-08-11-rep-marlyn` | $25.79 |
| `vmc-ussep-misen-2026-08-04-els0-5` | $24.49 |
| `enwc-ussep-sc-2026-08-11-rep-darnor` | $23.61 |
| `enwc-usgubp-wi-2026-08-11-dem-manbar` | $22.58 |
| `vmc-ussep-misen-2026-08-04-ste15-20` | $22.32 |

## Recent checks

| Checked (ET) | Result | Rows | Total |
|---|---|---:|---:|
| 2026-07-28 6:28 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 5:50 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 4:52 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 4:48 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 4:37 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 4:32 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 4:15 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 4:05 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 2:50 PM ET | ✅ ok | 823 | $1116.10 |
| 2026-07-28 1:49 PM ET | ✅ ok | 823 | $1116.10 |

Full history: [`data/rewards.csv`](data/rewards.csv) · every check: [`data/checks.csv`](data/checks.csv)
