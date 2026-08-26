"""3.0 entry point.

    python -m v3.main          # run the loop
    python -m v3.main --once   # one cycle against the live exchange, print, exit

One process, one loop, a list of families. Politics is the first and the
priority; adding a family is one config function and one line in
FAMILIES — exactly how the owner expanded 2.0.

Placing needs BOTH the master switch and the family's own switch ON.
Everything starts OFF; until the owner arms a family it only discovers,
scores, and shows what it would do. Master OFF stops every family with
one tap.

Env: POLYMARKET_KEY_ID / POLYMARKET_SECRET_KEY (required),
GITHUB_TOKEN (state survives redeploys; optional),
NTFY_TOPIC / NTFY_SERVER (alerts; optional),
V3_STATE_PATH (default ./v3_state.json), V3_PORT (default 8092).
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import threading
import time
from pathlib import Path

from . import basketball, football, politics
from .alerts import Alerts
from .api import ApiError, Client, GATEWAY
from .books import BookCache
from .family import Family
from .floor import Floor
from .names import Names
from .orders import OrderDesk
from .estimator import Estimator
from .silver import SilverFairs
from .state import StateStore
from .switch import MasterSwitch
from .ws import Stream

try:
    from zoneinfo import ZoneInfo
    ET_STATUS = ZoneInfo("America/New_York")
except Exception:  # noqa: BLE001
    import datetime as _dtz
    ET_STATUS = _dtz.timezone(_dtz.timedelta(hours=-4), "ET")

POLL_S = 60.0
NURSE_TICK_S = 5.0
ERROR_BACKOFF_CAP_S = 600.0
FLATTEN_CANCELS_PER_CYCLE = 45


def flatten_active() -> bool:
    """Owner, 2026-08-20 evening: "cancel all of my open orders except for
    the ones that are exiting a position that I'm already in... I need to
    have no risk of spending any money." And once flat: "increase the
    budget to 100 and follow the same strategy that was already existing
    in V1 and V2 for politics markets, looking at the orders that were the
    most successful."

    While the marker file ships with the build (v3/FLATTEN), the monitor
    runs the flatten: phase one cancels every opening order on the account
    and keeps every exit; once a pass finds nothing left to cancel, phase
    two lets the armed families rebuild under their (now $100 politics)
    ceilings, history-guided, while the pass keeps guarding against any
    opening order 3.0 does not own. Removing the marker (a redeploy) ends
    the mode entirely. V3_FLATTEN=0/1 overrides for tests."""
    env = os.environ.get("V3_FLATTEN")
    if env is not None:
        return env == "1"
    return os.path.exists(os.path.join(os.path.dirname(__file__), "FLATTEN"))


def is_exit_order(order: dict, positions: dict) -> bool:
    """An order whose FILL reduces a position we already hold: an ask
    while long, or a bid while short. Book side from the INTENT (the
    exchange's side field is not trustworthy for shorts — 1.0's lesson).
    Same classification the owner approved in the dead-programs sweep."""
    from .intents import REST_SIDE
    side = REST_SIDE.get(str(order.get("intent") or ""))
    if side is None:
        return False
    net = (positions.get(order.get("market")) or (0.0, 0.0))[0]
    return (side == "SELL" and net > 0.005) or (side == "BUY" and net < -0.005)

# name -> (config fn, discover fn). Adding a family = adding a line.
# Politics first — it gets the capital, the book budget, and the page.
FAMILIES = {
    "politics": (politics.config, politics.discover),
    "cfb": (football.cfb, football.cfb_discover),
    "nfl": (football.nfl, football.nfl_discover),
    "nba": (basketball.nba, basketball.nba_discover),
}


def load_history() -> dict[str, float]:
    """Average $/day each market has ACTUALLY paid us, from the committed
    ground truth (data/rewards.csv on main). This is the "most successful
    orders" record the rebuild replicates. Empty on any failure — history
    guides, it never blocks."""
    tok = os.environ.get("GITHUB_TOKEN", "")
    if not tok:
        return {}, {}, {}
    import csv
    import io
    from collections import defaultdict

    import requests
    repo = os.environ.get("GITHUB_REPOSITORY", "wfco223/Liquidity-rewards")
    try:
        r = requests.get(
            f"https://api.github.com/repos/{repo}/contents/data/rewards.csv",
            headers={"Authorization": f"Bearer {tok}",
                     "Accept": "application/vnd.github.raw+json"},
            timeout=30)
        if r.status_code >= 400:
            return {}, {}, {}
        paid: dict = defaultdict(float)
        days: dict = defaultdict(set)
        day_totals: dict = defaultdict(float)
        r_paid: dict = defaultdict(float)
        r_days: dict = defaultdict(set)
        import datetime as _dt
        cutoff = (_dt.date.today()
                  - _dt.timedelta(days=7)).isoformat()
        for row in csv.DictReader(io.StringIO(r.text)):
            v = float(row.get("reward_usd") or 0)
            if v <= 0:
                continue
            mkt = row.get("market") or ""
            paid[mkt] += v
            days[mkt].add(row.get("date"))
            day_totals[row.get("date") or "?"] += v
            if (row.get("date") or "") >= cutoff:
                r_paid[mkt] += v
                r_days[mkt].add(row.get("date"))
        recent = {mkt: (round(r_paid[mkt] / max(len(r_days[mkt]), 1), 4),
                        len(r_days[mkt])) for mkt in r_paid}
        return ({mkt: round(paid[mkt] / max(len(days[mkt]), 1), 4)
                 for mkt in paid},
                {d: round(v, 2) for d, v in day_totals.items()},
                recent)
    except Exception:  # noqa: BLE001
        return {}, {}, {}


FILLS_CSV_HEADER_V1 = ("ts,family,market,side,qty,px,purpose,est_day,"
                       "rested_h,fair,band_lo,band_hi,conf,touch_bid,"
                       "touch_ask,conc,pos_after,why\n")
FILLS_CSV_HEADER = ("ts,family,market,side,qty,px,purpose,est_day,"
                    "rested_h,fair,band_lo,band_hi,conf,touch_bid,"
                    "touch_ask,conc,pos_after,why,oid\n")


def fills_csv_append(existing: str | None, rows: list) -> tuple[str, int]:
    """Append-only fills archive (owner, 2026-08-22: 'bound it much
    higher — write to GitHub'). `rows` are (ts, family, journal-row)
    tuples; returns (new file text, rows added). Fills from the same
    cycle share a timestamp, so dedup is by the whole line, not ts."""
    def s(x):
        if x is None:
            return ""
        return f"{x:g}" if isinstance(x, (int, float)) else str(x)
    text = existing if existing else FILLS_CSV_HEADER
    if text.startswith(FILLS_CSV_HEADER_V1):
        # oid became the final column on 2026-08-23; upgrade the header
        # in place so the file keeps one shape. Older rows simply lack
        # the trailing field.
        text = FILLS_CSV_HEADER + text[len(FILLS_CSV_HEADER_V1):]
    tail = set(text.rstrip().split("\n")[-400:])
    last = 0.0
    body = text.rstrip().rsplit("\n", 1)[-1]
    try:
        last = float(body.split(",", 1)[0])
    except Exception:
        last = 0.0
    added = 0
    for ts, fam, r in sorted(rows, key=lambda x: x[0]):
        if ts < last - 0.05:
            continue
        band = r.get("band") or [None, None]
        why = str(r.get("why") or "").replace(",", ";").replace("\n", " ")[:80]
        line = ",".join([
            f"{ts:.1f}", fam, s(r.get("market")), s(r.get("side")),
            s(r.get("qty")), s(r.get("px")), s(r.get("purpose")),
            s(r.get("est_day")), s(r.get("rested_h")), s(r.get("fair")),
            s(band[0]), s(band[1]), s(r.get("conf")),
            s(r.get("touch_bid")), s(r.get("touch_ask")),
            s(r.get("conc")), s(r.get("pos_after")), why,
            s(r.get("oid"))])
        if line in tail:
            continue
        text += line + "\n"
        tail.add(line)
        added += 1
    return text, added


TRADES_CSV_HEADER = ("ts,iso,type,market,side,intent,price,shares,"
                     "order_id,role,realized_pnl,placed_iso,rested_h,"
                     "commission,maker_bps,manual,order_state,"
                     "cancel_reason,reject_reason,amount_usd,detail\n")


def _first_num(d: dict, keys) -> float | None:
    """The first of `keys` present in `d` that reads as a number.

    Written for the settlement and account-transfer rows, where the
    feed's own name for the money is not yet known to us — try the
    plausible ones in order rather than guessing one and recording
    a blank forever."""
    for k in keys:
        if k in d:
            v = _act_num(d.get(k))
            if v is not None:
                return v
        inner = d.get(k)
        if isinstance(inner, dict):        # {"amount": {"value": "3.00"}}
            v = _act_num(inner.get("value") or inner.get("amount"))
            if v is not None:
                return v
    return None


def _shape_of(d: dict, limit: int = 10) -> str:
    """The payload's field names, for a shape we could not read a
    number out of. The owner's standing rule (2026-08-23): when a
    number cannot be checked, go find the source — so record what
    the source actually offered instead of a silent blank."""
    if not isinstance(d, dict):
        return ""
    return "keys=" + "|".join(sorted(d.keys())[:limit])


def _act_num(x):
    """Protobuf money/qty shapes: plain, {'value': '1.5'}, or string."""
    if x is None:
        return None
    if isinstance(x, dict):
        x = x.get("value")
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _iso_to_ts(s: str) -> float:
    import datetime as _d
    s = (s or "").strip()
    if not s:
        return 0.0
    try:
        return _d.datetime.fromisoformat(
            s.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return 0.0


def parse_activities(rows: list) -> list[dict]:
    """Activity rows -> OUR executions, one per row.

    The feed returns BOTH sides of every trade: ours and the
    counterparty's. Treating that as a self-cross once dropped 1,623 of
    1,623 real fills (1.0, the hard way). OUR side is the one whose
    order carries a real intent — the API redacts the counterparty's to
    ORDER_INTENT_UNDEFINED."""
    out = []
    for a in rows or []:
        atype = str(a.get("type") or a.get("activityType") or "")
        t = a.get("trade") or {}
        pr = a.get("positionResolution") or {}
        if t:
            ours = None
            role = ""
            for key, name in (("passiveExecution", "passive"),
                              ("aggressorExecution", "aggressor")):
                ex = t.get(key) or {}
                o = ex.get("order") or {}
                it = str(o.get("intent") or "")
                if o.get("id") and it and not it.endswith("UNDEFINED"):
                    ours, role = ex, name
                    break
            if ours is None:
                continue                      # entirely the other side
            o = ours.get("order") or {}
            shares = _act_num(ours.get("lastShares"))
            if not shares or shares <= 0:
                continue                      # a placement, not a fill
            px = (_act_num(ours.get("lastPx"))
                  or _act_num(o.get("avgPx")) or _act_num(o.get("price")))
            intent = str(o.get("intent") or "")
            # Two of the four intents rest on the OPPOSITE side from
            # their name (BUY_SHORT is an ASK, SELL_SHORT is a BID) —
            # v3/intents.py is the single place that mapping lives.
            # Reading the name naively inverted the side on every
            # short and made the journal look like it had missed
            # fills it had actually recorded.
            from .intents import REST_SIDE
            side = REST_SIDE.get(intent, "")
            ts_s = str(ours.get("transactTime") or t.get("updateTime")
                       or t.get("createTime") or "")
            # the exchange carries far more than we were reading (the
            # 2026-08-23 shape probe): when the order was PLACED, why
            # it was cancelled, and the commissions actually charged.
            placed_s = str(o.get("createTime") or o.get("insertTime") or "")
            placed = _iso_to_ts(placed_s)
            ex_ts = _iso_to_ts(ts_s)
            out.append({
                "ts": ex_ts, "iso": ts_s,
                "type": atype or "TRADE",
                "market": str(t.get("marketSlug") or ""),
                "side": side, "intent": intent,
                "price": px, "shares": shares,
                "order_id": str(o.get("id") or ""), "role": role,
                "realized_pnl": _act_num(t.get("realizedPnl")),
                "placed_iso": placed_s,
                "placed_ts": placed or None,
                # the exact resting period, from the exchange itself —
                # no ledger needed, and it covers history too
                "rested_h": (round((ex_ts - placed) / 3600.0, 3)
                             if placed and ex_ts > placed else None),
                "commission": _act_num(
                    ours.get("commissionNotionalCollected")),
                "maker_bps": _act_num(o.get("makerCommissionsBasisPoints")),
                "manual": (1 if o.get("manualOrderIndicator") else 0),
                "order_state": str(o.get("state") or ""),
                "cancel_reason": str(ours.get("unsolicitedCancelReason")
                                     or ""),
                "reject_reason": str(ours.get("orderRejectReason") or "")})
        elif pr:
            ts_s = str(pr.get("updateTime") or pr.get("createTime") or "")
            after = pr.get("afterPosition") or {}
            before = pr.get("beforePosition") or {}
            # a settlement is a PAYMENT — the shares we held stop being
            # shares and become cash. We were recording that it happened
            # and not how much (2026-08-24, owner: "tell me what these
            # other payments I'm getting are"). Take the first amount
            # field the feed actually carries.
            amt = _first_num(pr, ("payout", "payoutNotional", "notional",
                                  "settlementNotional", "amount",
                                  "cashAmount", "proceeds"))
            held = _act_num(before.get("quantity"))
            out.append({
                "ts": _iso_to_ts(ts_s), "iso": ts_s,
                "type": atype or "POSITION_RESOLUTION",
                "market": str(pr.get("marketSlug") or ""),
                "side": "", "intent": "",
                "price": _first_num(pr, ("settlementPrice", "price",
                                         "resolutionPrice")),
                "shares": _act_num(after.get("quantity")),
                "order_id": "", "role": "",
                "realized_pnl": _act_num(pr.get("realizedPnl")),
                "amount_usd": amt,
                "detail": _shape_of(pr) if amt is None else
                          (f"held={held:g}" if held else "")})
        else:
            # Deposits, withdrawals, transfers and any shape we have
            # not seen. These carry their fields in a sub-object named
            # after the activity, not at the top level, so reading
            # updateTime/createTime off the root produced rows with no
            # date and no amount at all — four of them, all blank.
            # Find the payload, take its time and its amount, and if
            # the amount is not where we expect, write down the shape
            # so the next fetch answers the question instead of
            # repeating it.
            body = None
            for k, v in a.items():
                if isinstance(v, dict) and k not in ("trade",
                                                     "positionResolution"):
                    body = v
                    break
            src = body if isinstance(body, dict) else a
            ts_s = str(src.get("updateTime") or src.get("createTime")
                       or a.get("updateTime") or a.get("createTime") or "")
            amt = _first_num(src, ("amount", "notional", "amountUsd",
                                   "cashAmount", "value", "quantity",
                                   "usdAmount", "netAmount"))
            out.append({"ts": _iso_to_ts(ts_s), "iso": ts_s,
                        "type": atype or "UNKNOWN", "market": "",
                        "side": "", "intent": "", "price": None,
                        "shares": None, "order_id": "", "role": "",
                        "realized_pnl": None,
                        "amount_usd": amt,
                        "detail": _shape_of(src) if amt is None else ""})
    return out


def trades_csv_append(existing: str | None, rows: list) -> tuple[str, int]:
    """Append-only transaction record. Deduplicated on the whole line,
    so re-fetching overlapping pages adds nothing."""
    def s(x):
        if x is None:
            return ""
        return f"{x:g}" if isinstance(x, (int, float)) else str(x)
    text = existing if existing else TRADES_CSV_HEADER
    seen = set(text.rstrip().split("\n"))
    added = 0
    for r in sorted(rows, key=lambda x: x.get("ts") or 0.0):
        line = ",".join([
            f"{r.get('ts') or 0:.1f}", s(r.get("iso")), s(r.get("type")),
            s(r.get("market")), s(r.get("side")), s(r.get("intent")),
            s(r.get("price")), s(r.get("shares")), s(r.get("order_id")),
            s(r.get("role")), s(r.get("realized_pnl")),
            s(r.get("placed_iso")), s(r.get("rested_h")),
            s(r.get("commission")), s(r.get("maker_bps")),
            s(r.get("manual")), s(r.get("order_state")),
            s(r.get("cancel_reason")), s(r.get("reject_reason")),
            s(r.get("amount_usd")), s(r.get("detail"))])
        if line in seen:
            continue
        text += line + "\n"
        seen.add(line)
        added += 1
    return text, added


ESTIMATES_CSV_HEADER = ("day,family,est_usd,unmeasured_min,recorded_at,"
                        "paid_usd,paid_at,error_pct\n")


MARKET_EST_CSV_HEADER = ("day,market,family,est_day_usd,orders,"
                         "recorded_at,paid_usd,paid_at,error_pct,"
                         "share,pool_day,live_h,realized_share,levels\n")


def market_est_append(existing: str | None, today: str, rows: list,
                      paid_by_market_day: dict, now_iso: str,
                      keep_rows: int = 6000) -> tuple[str, int]:
    """The per-MARKET estimate ledger.

    The family ledger (estimates_csv_append) records one number a day
    per family, which is enough to see that politics is wrong and not
    enough to see WHERE. Across Aug 20-22 politics estimated $255-366
    a day and paid $76-101, while college football estimated $47.66
    and paid $54.33 — but with only family totals written down, no
    market and no race can be graded against its own prediction, so
    the cause stays a guess. This file makes it arithmetic.

    Same discipline as the family ledger: a past day's estimate is
    FROZEN the first time it is written. Only paid_usd, paid_at and
    error_pct fill in afterwards.

    `rows` are (day, market, family, est_day, orders, share, pool_day,
    live_h) tuples. The last three are the estimator's own time-weighted
    measurement of our share and the pool it competed for. Once the
    money lands, realized_share = paid / (pool_day * live_h / 24), and
    share vs realized_share is the estimator's bias measured directly,
    with no model in between (owner, 2026-08-24: the sampler runs 4,320
    times a day, so a persistent error is a bias, and averaging more
    samples cannot remove a bias).
    `paid_by_market_day` maps "day|market" -> paid, which is exactly
    the shape the monitor already keeps in self.rewards_seen.
    """
    text = existing if existing else MARKET_EST_CSV_HEADER
    kept: dict = {}
    order: list = []
    for line in text.strip().split("\n")[1:]:
        parts = line.split(",")
        if len(parts) < 9:
            continue
        parts += [""] * (14 - len(parts))      # rows written before the
        key = (parts[0], parts[1])             # share/depth columns existed
        if key not in kept:
            order.append(key)
        kept[key] = parts
    changed = 0
    for day, market, family, est, orders, share, pool_day, live_h, levels \
            in rows:
        key = (day, market)
        prior = kept.get(key)
        if prior and day != today:      # frozen: a prediction you can
            est_s = prior[3]            # revise after the fact is
            ord_s = prior[4]            # worth nothing
            rec_s = prior[5]
            share_s = prior[9] if len(prior) > 9 else ""
            pool_s = prior[10] if len(prior) > 10 else ""
            live_s = prior[11] if len(prior) > 11 else ""
            lv_s = prior[13] if len(prior) > 13 else ""
        else:
            est_s = f"{est:.4f}"
            ord_s = str(int(orders))
            rec_s = prior[5] if prior else now_iso
            share_s = f"{share:.6f}" if share else ""
            pool_s = f"{pool_day:.6f}" if pool_day else ""
            live_s = f"{live_h:.3f}" if live_h else ""
            lv_s = str(int(levels)) if levels else ""
        paid = paid_by_market_day.get(f"{day}|{market}")
        paid_s = f"{paid:.4f}" if paid is not None else ""
        paid_at = (prior[7] if prior and prior[6] else
                   (now_iso if paid is not None else ""))
        err = ""
        if paid is not None:
            try:
                e = float(est_s)
                if e > 0:
                    err = f"{(paid - e) / e * 100:+.1f}"
            except ValueError:
                pass
        realized = ""
        if paid is not None:
            try:
                offered = float(pool_s) * float(live_s) / 24.0
                if offered > 0:
                    realized = f"{paid / offered:.6f}"
            except (ValueError, ZeroDivisionError):
                pass
        row = [day, market, family, est_s, ord_s, rec_s, paid_s,
               paid_at, err, share_s, pool_s, live_s, realized, lv_s]
        if kept.get(key) != row:
            changed += 1
        if key not in kept:
            order.append(key)
        kept[key] = row
    # newest days first when trimming — the old ones are already graded
    order.sort(key=lambda k: k[0], reverse=True)
    order = order[:keep_rows]
    body = "\n".join(",".join(kept[k]) for k in order)
    return MARKET_EST_CSV_HEADER + body + "\n", changed


def estimates_csv_append(existing: str | None, today: str,
                         rows: list, paid_by_day: dict,
                         now_iso: str,
                         paid_by_fam: dict | None = None,
                         ) -> tuple[str, int]:
    """The estimate ledger (owner, 2026-08-23: "All the estimates
    should stay written down somewhere until the actual numbers come
    in").

    A past day's estimate is FROZEN the first time it is written — it
    is a prediction, and a prediction you can revise after the fact is
    worthless. Only the paid column fills in later. Today's row keeps
    updating because the day is still accruing.

    `rows` are (day, family, est_usd, unmeasured_min) tuples.
    `paid_by_day` maps day -> total paid for the whole account, and
    `paid_by_fam` maps (day, family) -> that family's own share.

    Grade a family against ITS OWN money (2026-08-24). Before this the
    whole account's total was written into every family row, so the
    politics estimate was measured against politics + football + NBA
    together, and nfl's $0.00 estimate was scored against the entire
    day. Both the paid column and error_pct were nonsense per family.
    The day total is still the fallback for a family the breakdown
    cannot classify, so a row never goes blank.
    """
    text = existing if existing else ESTIMATES_CSV_HEADER
    kept: dict = {}
    order: list = []
    for line in text.strip().split("\n")[1:]:
        parts = line.split(",")
        if len(parts) < 8:
            continue
        key = (parts[0], parts[1])
        if key not in kept:
            order.append(key)
        kept[key] = parts
    changed = 0
    for day, family, est, unmeas in rows:
        key = (day, family)
        prior = kept.get(key)
        if prior and day != today:
            est_s, unmeas_s, rec_s = prior[2], prior[3], prior[4]
        else:                       # today, or never recorded before
            est_s = f"{est:.2f}"
            unmeas_s = f"{unmeas:.1f}"
            rec_s = prior[4] if prior else now_iso
        paid = (paid_by_fam or {}).get((day, family))
        if paid is None and not paid_by_fam:
            paid = paid_by_day.get(day)
        paid_s = f"{paid:.2f}" if paid is not None else ""
        paid_at = (prior[6] if prior and prior[5] else
                   (now_iso if paid is not None else ""))
        err = ""
        if paid is not None:
            try:
                e = float(est_s)
                if e > 0:
                    err = f"{(paid - e) / e * 100:+.1f}"
            except ValueError:
                pass
        row = [day, family, est_s, unmeas_s, rec_s, paid_s, paid_at, err]
        if prior != row:
            changed += 1
        if key not in kept:
            order.append(key)
        kept[key] = row
    out = ESTIMATES_CSV_HEADER
    for key in sorted(order, key=lambda k: (k[0], k[1])):
        out += ",".join(kept[key]) + "\n"
    return out, changed


def card_is_open(card: dict) -> bool:
    """A lot is open only while the exchange still shows a position —
    a lot the pairing thinks is open on a FLAT market was closed by a
    correction or an untracked fill (the Florida card, 2026-08-22) and
    counts as closed."""
    if card.get("stray_close"):
        return False
    oq = (card.get("open_qty") if card.get("open_qty") is not None
          else card.get("qty", 0.0))
    if oq <= 0.005:
        return False
    if (card.get("pos_now") is not None
            and abs(card["pos_now"]) < 0.005):
        return False
    return True


def card_net(card: dict) -> float:
    """The card's bottom line, same math the page shows: realized plus
    rewards earned resting, plus (for open lots) the conservative mark
    and what the resting exit has earned."""
    earned = 0.0
    if card.get("est_day") and card.get("rested_h") is not None:
        earned = card["est_day"] * card["rested_h"] / 24.0
    is_open = card_is_open(card)
    net = (card.get("realized") or 0.0) + earned
    if is_open:
        oq = (card.get("open_qty") if card.get("open_qty") is not None
              else card.get("qty", 0.0))
        if card.get("side") == "BUY" and card.get("now_bid") is not None:
            net += (card["now_bid"] - card["px"]) * oq
        if card.get("side") == "SELL" and card.get("now_ask") is not None:
            net += (card["px"] - card["now_ask"]) * oq
        net += card.get("exit_earned") or 0.0
    return net


def card_visible(card: dict, now: float) -> bool:
    """Owner's retention (2026-08-22): closed cards show for 3 days
    after their last close; open cards show until they turn profitable
    (then the journal keeps tracking them silently)."""
    if card_is_open(card):
        return card_net(card) <= 0.005
    last = card.get("last_ts", card.get("ts", 0.0))
    return now - last <= 3 * 86400.0


def pair_fills(fills: list) -> list:
    """Match closes to entries, oldest lot first, per market: a buy pairs
    with the sells that unload it, a short sale with the buys that cover
    it (owner, 2026-08-21: "each should have a matching buy and sell or
    sell short and buy back"). Returns one card per entry lot carrying
    its closes and realized money, plus stray closes of stock the journal
    never saw bought."""
    out: list[dict] = []
    by_mkt: dict[str, list] = {}
    for r in sorted(fills, key=lambda x: x.get("ts", 0.0)):
        by_mkt.setdefault(r.get("market", "?"), []).append(r)
    for evs in by_mkt.values():
        longs: list[dict] = []
        shorts: list[dict] = []
        for r in evs:
            qty = float(r.get("qty") or 0.0)
            opp = shorts if r["side"] == "BUY" else longs
            while qty > 0.005 and opp:
                lot = opp[0]
                take = min(qty, lot["open_qty"])
                pl = ((lot["px"] - r["px"]) if r["side"] == "BUY"
                      else (r["px"] - lot["px"])) * take
                lot["closes"].append({
                    "ts": r["ts"], "px": r["px"], "qty": round(take, 2),
                    "pl": round(pl, 4)})
                lot["realized"] = round(lot["realized"] + pl, 4)
                lot["open_qty"] = round(lot["open_qty"] - take, 2)
                lot["last_ts"] = r["ts"]
                if lot["open_qty"] <= 0.005:
                    opp.pop(0)
                qty = round(qty - take, 2)
            if qty > 0.005:
                lot = dict(r)
                lot["open_qty"] = qty
                lot["closes"] = []
                lot["realized"] = 0.0
                lot["last_ts"] = r["ts"]
                if r.get("purpose") == "sell":
                    # an exit with no purchase to match: it closed stock
                    # bought before the journal — not a new position
                    lot["stray_close"] = True
                    lot["open_qty"] = 0.0
                else:
                    (longs if r["side"] == "BUY" else shorts).append(lot)
                out.append(lot)
    return out


def build_hash() -> str:
    h = hashlib.sha256()
    for p in sorted(Path(__file__).parent.glob("*.py")):
        h.update(p.read_bytes())
    return h.hexdigest()[:8]


class CacheRouter:
    """The stream writes here; frames route to the family that owns the
    market (politics is the fallback). One socket, every family fed."""

    def __init__(self, families: dict):
        self.families = families

    def put(self, slug: str, book) -> None:
        for key in ("cfb", "nfl", "nba"):
            fam = self.families.get(key)
            if fam is not None and slug in fam.universe:
                fam.cache.put(slug, book)
                return
        pol = self.families.get("politics")
        if pol is not None:
            pol.cache.put(slug, book)


def touch_snapshot(fam: Family, now: float, cap: int = 400) -> dict:
    """Best bid/ask + side totals + age per market the family is in —
    published so the book is readable without the dashboard."""
    out = {}
    slugs = sorted(fam.active_markets() | set(fam.inventory))[:cap]
    for s in slugs:
        b = fam.cache.any_age(s)
        if b is None or now - b.fetched_at > 600:
            continue
        out[s] = [round(b.bids[0][0] * 100, 1) if b.bids else None,
                  round(b.asks[0][0] * 100, 1) if b.asks else None,
                  round(sum(q for _, q in b.bids)),
                  round(sum(q for _, q in b.asks)),
                  int(now - b.fetched_at)]
    return out


class Monitor:
    def __init__(self):
        self.client = Client()
        self.alerts = Alerts()
        self.names = Names()
        self.store = StateStore(os.environ.get("V3_STATE_PATH", "v3_state.json"))
        self.build = build_hash()
        self.boot_ts = time.time()
        self.errors: list[str] = []
        self.audit: list[dict] = []
        self.last_state: dict = {}
        self.boots: list[float] = []
        self.master = MasterSwitch(alert=self.alerts.notify,
                                   name="3.0 master switch", scope="all of 3.0")
        # The floor handshake (v3/floor.py): master ON asks 1.0 and 2.0 to
        # halt their automation; nothing here touches an order until both
        # have acknowledged. _floor_ok is refreshed every cycle and read by
        # every desk's switch closure.
        self.floor = Floor()
        self._floor_ok = False
        self.flatten = flatten_active()
        self.flatten_done = False          # phase two reached (persisted)
        self.flat_stats = {"cancelled": 0, "failed": 0}
        self.last_flat: dict | None = None
        self._history_at = 0.0
        # the boot readout: what the first cycle is doing right now, so a
        # restart shows a progress bar instead of a scary red "stale"
        self.boot_stage = {"stage": "starting", "pct": 2, "ts": time.time()}
        self.payload_json: bytes | None = None    # frozen /data.json body
        # per-market fair values SET BY THE OWNER from the orders page —
        # his number beats the model everywhere fair is used (owner,
        # 2026-08-23: "Give me an option to set fair market for the
        # 2028 markets because you're off")
        self.owner_fairs: dict[str, float] = {}
        self.backfilled = False        # one-shot journal recovery
        self.evidence_seeded = False   # one-shot evidence seed
        self._first_cycle_done = False
        self.silver = SilverFairs(client=self.client)
        self.samplers: dict[str, Estimator] = {}
        self.actuals_by_day: dict[str, float] = {}
        self.actuals_by_fam: dict[str, float] = {}   # "day|family" -> usd
        self.rewards_seen: dict[str, float] = {}
        self.rw_last: dict | None = None      # latest payout-check result
        self._rw_at = 0.0
        self._lock = threading.Lock()
        self.families: dict[str, Family] = {}
        self.switches: dict[str, MasterSwitch] = {}
        for key, (cfg_fn, discover) in FAMILIES.items():
            cfg = cfg_fn()
            sw = MasterSwitch(alert=self.alerts.notify,
                              name=f"{cfg.name} switch", scope=cfg.name)
            cache = BookCache()
            fam = Family(None, cache, discover, config=cfg,
                         alert=self.alerts.notify, names=self.names)
            desk = OrderDesk(
                client=self.client,
                whitelist=fam.knows,
                switch_on=lambda s=sw: (self.master.on and s.on
                                        and self._floor_ok),
                fresh_book=lambda slug, c=cache: c.fresh(slug, 120.0, time.time()),
                log=self._audit,
            )
            fam.desk = desk
            fam.fairs = self._fair_for
            # every family's fill model learns from its own book feed
            cache.on_put = (lambda slug, book, f=fam:
                            f.fillmodel.observe_touch(
                                slug,
                                book.bids[0][0] if book.bids else None,
                                book.asks[0][0] if book.asks else None,
                                book.tick, book.fetched_at))
            self.families[key] = fam
            self.switches[key] = sw
            self.samplers[key] = Estimator()
        # The book stream: politics markets subscribe first (its cache is
        # the one the stream writes); a dead stream degrades to REST
        # polling through the cache's own age interlock.
        pol = self.families.get("politics")
        self.stream = (Stream(CacheRouter(self.families), self._ws_slugs,
                              self.client.key_id, self.client.secret_key)
                       if pol is not None else None)
        self._restore()
        self.boots = [b for b in self.boots if time.time() - b < 86400]
        self.boots.append(time.time())
        # A deploy replaces the container and its floor files with it. If the
        # master came back ON, the request must be back on disk before 1.0's
        # first automation pass, not a poll later.
        self.floor.write_want(self.master.on or self.flatten)

    def _ws_slugs(self) -> list[str]:
        """The owner's slot order (2026-08-21): every politics market
        he is in seats first — that is the priority — then football
        markets holding orders, then idle candidates rotate through the
        leftover slots. Promising candidates (a measured rate or a
        planned estimate) hold stable seats or rotate often; cold ones
        get a thin rotation lane."""
        from .ws import SUB_CAP
        out: list[str] = []
        seen: set[str] = set()

        def take(slugs, room=None):
            for s in slugs:
                if room is not None and len(out) >= room:
                    break
                if s not in seen:
                    seen.add(s)
                    out.append(s)

        for key in ("politics", "cfb", "nfl", "nba"):
            fam = self.families.get(key)
            if fam is not None:
                take(sorted(fam.active_markets() | set(fam.inventory)),
                     room=SUB_CAP)
        cands: list[tuple[float, str]] = []
        for key in ("politics", "cfb", "nfl", "nba"):
            fam = self.families.get(key)
            if fam is None:
                continue
            est = self.samplers.get(key)
            rates = est.market_rates if est is not None else {}
            for s, sb in fam.scoreboard.items():
                if s in seen:
                    continue
                promise = max(rates.get(s) or 0.0,
                              (sb.get("est") or 0.0) if sb.get("plans")
                              else 0.0)
                cands.append((promise, s))
        cands.sort(key=lambda t: (-t[0], t[1]))
        warm = [s for p, s in cands if p > 0.0]
        cold = [s for p, s in cands if p <= 0.0]
        room = max(SUB_CAP - len(out), 0)
        take(warm[:room // 2], room=SUB_CAP)     # stable seats for the best
        warm_rest = warm[room // 2:]

        def rotate(pool, n, window):
            if not pool or n <= 0:
                return []
            n = min(n, len(pool))
            off = (window * n) % len(pool)
            return (pool + pool)[off:off + n]

        window = int(time.time() // 900)         # a fresh mix every 15 min
        room = max(SUB_CAP - len(out), 0)
        take(rotate(warm_rest, (room * 3) // 4, window), room=SUB_CAP)
        room = max(SUB_CAP - len(out), 0)
        take(rotate(cold, room, window), room=SUB_CAP)
        return out[:SUB_CAP]

    def _sampler_loop(self) -> None:
        """The independent clock (REBUILD.md's lesson): earnings are
        sampled every 20s by this thread, never by anything that just
        placed an order. Nothing here can touch an order."""
        while True:
            time.sleep(20.0)
            now = time.time()
            with self._lock:
                for key, fam in self.families.items():
                    try:
                        orders = [{"market": o.market, "side": o.side,
                                   "price": o.price, "size": o.qty}
                                  for o in fam.orders.values()]
                        self.samplers[key].sample(
                            now, orders, fam.cache, fam.terms,
                            side_pool=lambda s, p, f=fam: f._side_pool(s, p))
                    except Exception:  # noqa: BLE001 — measuring never breaks
                        pass

    def _audit(self, row: dict) -> None:
        self.audit.append(row)
        del self.audit[:-200]

    def _note(self, msg: str) -> None:
        self.errors.append(f"{time.strftime('%m-%d %H:%M:%S')} {msg}")
        del self.errors[:-40]
        print(f"v3: {msg}", flush=True)

    # -- persistence --------------------------------------------------------

    def _restore(self) -> None:
        saved = self.store.load_best()
        if not saved:
            self._note(f"booted build {self.build}; fresh state — "
                       "every switch is off")
            return
        if saved.get("master_switch"):
            self.master.restore(saved["master_switch"])
        if saved.get("names"):
            self.names.restore(saved["names"])
        for key, fam in self.families.items():
            if saved.get(f"fam_{key}"):
                fam.restore(saved[f"fam_{key}"])
            if saved.get(f"sw_{key}"):
                self.switches[key].restore(saved[f"sw_{key}"])
            if saved.get(f"est_{key}"):
                self.samplers[key] = Estimator.from_dict(saved[f"est_{key}"])
            if saved.get(f"evi_{key}"):
                fam.evidence.restore(saved[f"evi_{key}"])
        self.errors = list(saved.get("errors") or [])
        self.boots = list(saved.get("boots") or [])
        self.audit = list(saved.get("audit") or [])
        self.flatten_done = bool(saved.get("flatten_done"))
        self.flat_stats = dict(saved.get("flat_stats")
                               or {"cancelled": 0, "failed": 0})
        self.rewards_seen = dict(saved.get("rewards_seen") or {})
        self.actuals_by_day = dict(saved.get("actuals_by_day") or {})
        self.actuals_by_fam = dict(saved.get("actuals_by_fam") or {})
        self.owner_fairs = {k: float(v) for k, v in
                            (saved.get("owner_fairs") or {}).items()}
        self.backfilled = bool(saved.get("backfilled_600"))
        self.evidence_seeded = bool(saved.get("evidence_seeded"))
        self.silver.changes = list(saved.get("silver_log") or [])
        self.rw_last = saved.get("rewards_last")
        age = time.time() - (saved.get("saved_at") or 0)
        armed = [k for k, sw in self.switches.items() if sw.on and self.master.on]
        self._note(f"booted build {self.build}; restored state {age:.0f}s old"
                   + (f"; ARMED: {', '.join(armed)}" if armed else ""))
        # READ-ONLY book comparison (owner approved 2026-08-25): log
        # what each endpoint sees for a few of our markets. No fetch
        # path changes; the lines land in the notes for the next check.
        try:
            slugs = []
            for fam in self.families.values():
                for o in fam.orders.values():
                    if o.market not in slugs:
                        slugs.append(o.market)
                    if len(slugs) >= 4:
                        break
                if len(slugs) >= 4:
                    break
            for line in (self.client.compare_book_sources(slugs)
                         if slugs else []):
                self._note("book compare: " + line)
        except Exception as e:  # noqa: BLE001 — never blocks a boot
            self._note(f"book compare failed: {type(e).__name__}: {e}")
        if armed and saved.get("build") != self.build:
            self.alerts.notify("3.0: new build with a switch ON",
                               f"build {self.build} booted; may place orders "
                               f"({', '.join(armed)})")

    def _grades(self) -> list[dict]:
        """Per-day estimate vs what the exchange actually paid. The
        estimate is 3.0's own sampler from the day it took over; the
        actuals are the whole account's postings (during the transition
        the older versions' books pay into the same number — labelled so
        on the page)."""
        est_by_day: dict[str, dict] = {}
        for key, est in self.samplers.items():
            for h in est.history:
                row = est_by_day.setdefault(h["day"], {"est": 0.0, "stale_s": 0.0})
                row["est"] += h.get("earned") or 0.0
                row["stale_s"] += h.get("stale_s") or 0.0
            if est.day:
                row = est_by_day.setdefault(est.day, {"est": 0.0, "stale_s": 0.0})
                row["est"] += est.earned
                row["stale_s"] += est.stale_s
        days = sorted(set(est_by_day) | set(self.actuals_by_day))[-14:]
        return [{"day": d,
                 "est": round(est_by_day.get(d, {}).get("est", 0.0), 2)
                 if d in est_by_day else None,
                 "actual": self.actuals_by_day.get(d),
                 "unmeasured_min": round(
                     est_by_day.get(d, {}).get("stale_s", 0.0) / 60.0, 1)}
                for d in days]

    def _paid_total(self) -> dict | None:
        """All-time posted rewards: EVERY day in rewards.csv, not just
        the rows the grades page lists (owner, 2026-08-22: "way more
        than 12 posted days — just look at rewards.csv")."""
        if not self.actuals_by_day:
            return None
        return {"usd": round(sum(self.actuals_by_day.values()), 2),
                "days": len(self.actuals_by_day),
                "since": min(self.actuals_by_day)}

    def _state(self, now: float, summaries: dict) -> dict:
        st = {
            "saved_at": now, "build": self.build, "boot_ts": self.boot_ts,
            "boots": self.boots[-20:], "errors": self.errors,
            "audit": self.audit[-60:],
            "master_switch": self.master.to_dict(),
            "flatten_done": self.flatten_done,
            "flat_stats": self.flat_stats,
            "rewards_seen": self.rewards_seen,
            "actuals_by_day": self.actuals_by_day,
            "actuals_by_fam": self.actuals_by_fam,
            "owner_fairs": dict(self.owner_fairs),
            "backfilled_600": bool(self.backfilled),
            "evidence_seeded": bool(self.evidence_seeded),
            "names": self.names.to_dict(),
            "summaries": summaries,
            "floor": self.floor.status(now),
            "ws": dict(self.stream.status) if self.stream else {},
            "lite_study": self._lite_study(),

            "silver_log": self.silver.changes[-120:],
            "rewards_last": self.rw_last,
            "silver": {
                "priced": sum(1 for s in self.families["politics"].universe
                              if self.families["politics"].enterable(s)
                              and self.silver.model_fair(s) is not None),
                "unpriced": sum(1 for s in self.families["politics"].universe
                                if self.families["politics"].enterable(s)
                                and self.silver.model_fair(s) is None),
                "senate_races": len(self.silver.races),
                "gov_races": len(self.silver.gov_races),
                "tables_age_min": (round((now - self.silver.fetched_at) / 60)
                                   if self.silver.fetched_at else None),
                "tables_changed_h": (round(
                    (now - self.silver.changed_at) / 3600, 1)
                    if getattr(self.silver, "changed_at", 0) else None),
                "gov_changed_h": (round(
                    (now - self.silver.gov_changed_at) / 3600, 1)
                    if getattr(self.silver, "gov_changed_at", 0) else None),
                "note": getattr(self.silver, "note", ""),
                "ak_gov": dict(self.silver.gov_races.get("ak") or {}),
                "official_source": self.silver.official_source,
                "official_age_h": (round(
                    self.silver.official_run_age_s(now) / 3600, 1)
                    if self.silver.official_meta else None),
                "meta": dict(self.silver.official_meta or {}),
            },
            "grades": self._grades(),
            "paid_total": self._paid_total(),
            "flatten": ({"active": self.flatten,
                         "done": self.flatten_done, **(self.last_flat or {})}
                        if self.flatten else {"active": False}),
            "alerts_log": self.alerts.log[-30:],
        }
        for key, fam in self.families.items():
            st[f"fam_{key}"] = fam.to_dict()
            st[f"est_{key}"] = self.samplers[key].to_dict()
            st[f"evi_{key}"] = fam.evidence.to_dict()
            st[f"sw_{key}"] = self.switches[key].to_dict()
            st[f"touches_{key}"] = touch_snapshot(fam, now)
        return st

    # -- owner controls -----------------------------------------------------

    def switch_tap(self, op: str, which: str = "master") -> dict:
        """A tap on /v3/switch. Persisted IMMEDIATELY, local and remote —
        a restart between a flip and the next save must not undo it."""
        sw = self.switches.get(which, self.master)
        s = sw.op(op)
        self.floor.write_want(self.master.on or self.flatten)
        st = dict(self.last_state) if self.last_state else {}
        st["master_switch"] = self.master.to_dict()
        for key in self.families:
            st[f"sw_{key}"] = self.switches[key].to_dict()
        st["saved_at"] = time.time()
        self.last_state = st
        self.freeze_payload()      # a switch flip shows immediately
        self.store.save_local(st)
        self.store.save_remote(st)
        return s

    def _fair_for(self, slug: str) -> float | None:
        """One fair per market: the OWNER'S number when he has set one,
        else the model's. Every consumer of fair — the past-fair caps,
        exit guards, EV edge, watch cards — sees the same value."""
        own = self.owner_fairs.get(slug)
        if own is not None:
            return own
        return self.silver.model_fair(slug)

    def set_owner_fair(self, market: str, fair: float | None) -> dict:
        """Owner control from the orders page. fair in DOLLARS
        (0.001-0.999); None clears back to the model."""
        if not any(fam.knows(market) for fam in self.families.values()):
            return {"ok": False,
                    "note": "no family knows this market — check the slug"}
        if fair is None:
            had = self.owner_fairs.pop(market, None)
            note = ("owner fair cleared — the model prices it again"
                    if had is not None else "no owner fair was set")
        else:
            if not (0.001 <= fair <= 0.999):
                return {"ok": False, "note": "fair must be 0.1c to 99.9c"}
            self.owner_fairs[market] = round(float(fair), 4)
            note = f"owner fair set: {fair * 100:g}c — beats the model"
        # the resting book in this market is now suspect: re-check it
        # first on the next sweep instead of waiting its turn
        for fam in self.families.values():
            if fam.knows(market):
                fam.priority.add(market)
        self._audit({"op": "owner_fair", "market": market,
                     "fair": fair, "ts": time.time()})
        self._note(f"{note} ({market})")
        # persisted IMMEDIATELY, like a switch flip — a restart between
        # the tap and the next save must not undo it
        st = dict(self.last_state) if self.last_state else {}
        st["owner_fairs"] = dict(self.owner_fairs)
        st["saved_at"] = time.time()
        self.last_state = st
        self.freeze_payload()
        self.store.save_local(st)
        self.store.save_remote(st)
        return {"ok": True, "note": note}

    def owner_place(self, market: str, side: str, price: float,
                    qty: float) -> dict:
        """The owner's own hand: bypasses switches, keeps every other
        rail, and the automation never touches the result."""
        from .family import FamilyOrder
        for fam in self.families.values():
            if not fam.knows(market):
                continue
            net = 0.0
            try:
                net = (self.client.positions_net().get(market) or (0.0,))[0]
            except Exception:  # noqa: BLE001
                pass
            r = fam.desk.place_resting(market, side, price, qty,
                                       net_position=net, initiator="owner",
                                       verify=True)
            if r.ok and r.order_id:
                fam.orders[r.order_id] = FamilyOrder(
                    id=r.order_id, market=market, side=side, price=price,
                    qty=qty, intent=r.intent, placed_ts=time.time(),
                    purpose="manual", why="placed by the owner")
            return {"ok": r.ok, "note": r.note, "order_id": r.order_id}
        return {"ok": False,
                "note": "no family knows this market — check the slug"}

    def order_op(self, op: str, order_id: str, price: float | None = None,
                 pin: bool = False, qty: float | None = None) -> dict:
        """Owner move/cancel/resize on one of OUR orders, from the
        orders page or the live card. initiator='owner' bypasses the
        switches but no other rail. pin=True (the live card's hand ops)
        marks an engine order hand-set: the engine hands off until the
        release rule or the nurse ends the pin; the hold's baseline is
        measured on the first read AFTER the change (a new price or
        size earns differently than the old one did). Manual orders
        stay manual — already stronger than any pin. An oversized SELL
        is safe by construction: the desk verifies the replacement
        rests at full size and leaves the original untouched if the
        exchange trims it."""
        for fam in self.families.values():
            rec = fam.orders.get(order_id)
            if rec is None:
                continue
            if op == "cancel":
                r = fam.desk.cancel(order_id, rec.market, initiator="owner")
                if r.ok:
                    del fam.orders[order_id]
                return {"ok": r.ok, "note": r.note}
            if op == "move" and (price is not None or qty is not None):
                new_px = float(price) if price is not None else rec.price
                new_q = round(float(qty), 2) if qty is not None else rec.qty
                r = fam.desk.reprice(
                    {"id": rec.id, "market": rec.market, "side": rec.side,
                     "price": rec.price, "size": rec.qty, "intent": rec.intent},
                    new_px, new_q if qty is not None else None,
                    initiator="owner")
                if r.ok:
                    del fam.orders[order_id]
                    from .family import FamilyOrder
                    now = time.time()
                    pinning = pin and rec.purpose != "manual"
                    fam.orders[r.order_id] = FamilyOrder(
                        id=r.order_id, market=rec.market, side=rec.side,
                        price=new_px, qty=new_q, intent=rec.intent,
                        placed_ts=now, purpose=rec.purpose,
                        why=("hand-set from the live card — the engine "
                             "holds off" if pinning
                             else "moved by the owner"),
                        pinned=pinning, pin_ts=now if pinning else 0.0,
                        pin_est=-1.0 if pinning else 0.0)
                    if pinning:
                        fam._log(event="hand_set", market=rec.market,
                                 side=rec.side, price=new_px, qty=new_q,
                                 note="the owner changed this order from "
                                      "the live card — the engine holds "
                                      "off until the book turns against it")
                return {"ok": r.ok, "note": r.note}
            return {"ok": False, "note": f"unknown op {op}"}
        return {"ok": False, "note": "not one of 3.0's orders"}

    def close_position(self, market: str) -> dict:
        """The live card's close-out button: sell the open shares at the
        current best bid, never worse — the same carved shape as the
        taker dump, fired by the owner's own tap. Engine exits are
        cancelled first so shares are never offered twice; his own
        hand-placed asks are untouchable, so their shares stay theirs.
        The part the displayed bid can take is journaled as sold; any
        rest stays resting AT the bid as the owner's own order."""
        from .family import FamilyOrder
        from .intents import SELL_LONG
        now = time.time()
        for fam in self.families.values():
            inv = fam.inventory.get(market)
            if inv is None:
                continue
            qty = round(inv.get("qty") or 0.0, 2)
            if qty <= -0.01:
                return {"ok": False,
                        "note": "this position is short — closing it means "
                                "BUYING at the ask, which nothing may cross "
                                "for; rest a bid instead"}
            if qty < 0.01:
                return {"ok": False, "note": "no open position here"}
            try:
                book = self.client.book(market, fetched_at=now)
                fam.cache.put(market, book)
            except Exception as e:  # noqa: BLE001 — fail closed, plainly
                return {"ok": False,
                        "note": f"could not read a fresh book: {e}"}
            if not book.bids:
                return {"ok": False,
                        "note": "no bid resting to sell to right now"}
            bid_px, bid_sz = book.bids[0]
            manual_cover = sum(
                o.qty for o in fam.orders.values()
                if o.market == market and o.side == "SELL"
                and o.purpose == "manual")
            sellable = round(qty - manual_cover, 2)
            if sellable < 0.01:
                return {"ok": False,
                        "note": "your own resting asks already cover this "
                                "position — cancel one first if you want "
                                "these shares sold here"}
            # engine exits (hand-set ones included — this tap supersedes
            # the earlier hand move) come off first
            for o in [o for o in fam.orders.values()
                      if o.market == market and o.purpose == "sell"
                      and o.side == "SELL"]:
                rr = fam.desk.cancel(o.id, o.market, initiator="owner")
                if rr.ok:
                    fam.orders.pop(o.id, None)
                    fam.evidence.order_gone(o.market, o.id)
            r = fam.desk.place_resting(
                market, "SELL", bid_px, sellable, net_position=qty,
                intent=SELL_LONG, initiator="owner", taker=True,
                verify=False)
            if not r.ok:
                return {"ok": False, "note": r.note}
            # journal what the displayed bid can take NOW (the dump's
            # own convention); the rest is the owner's resting ask and
            # the normal fill watch journals it when it sells
            took = round(min(sellable, bid_sz), 2)
            if took >= 0.01:
                inv["qty"] = round(inv.get("qty", 0.0) - took, 4)
                inv["cost"] = round(inv.get("cost", 0.0) - took * bid_px, 4)
                left = round(inv["qty"], 2)
                if abs(inv["qty"]) < 0.005:
                    fam.inventory.pop(market, None)
                    fam.inv_since.pop(market, None)
                fam._journal_fill(FamilyOrder(
                    id=r.order_id or f"close{int(now)}",
                    market=market, side="SELL", price=bid_px, qty=took,
                    intent=SELL_LONG, placed_ts=now, purpose="sell",
                    why="closed out by the owner from the live card — "
                        "sold into the bid"), took, now, left)
            rest = round(sellable - took, 2)
            if rest >= 0.01 and r.order_id:
                fam.orders[r.order_id] = FamilyOrder(
                    id=r.order_id, market=market, side="SELL",
                    price=bid_px, qty=rest, intent=SELL_LONG,
                    placed_ts=now, purpose="manual",
                    why="the rest of the owner's close-out — resting at "
                        "the bid until it sells")
            fam._log(event="close_out", market=market, price=bid_px,
                     qty=sellable,
                     note=(f"owner closed out — {took:g} sold into the bid"
                           + (f", {rest:g} resting at "
                              f"{bid_px * 100:g}c" if rest >= 0.01 else "")))
            note = f"sold {took:g} at {bid_px * 100:g}c"
            if rest >= 0.01:
                note += (f"; the bid could not take the other {rest:g} — "
                         f"they rest at {bid_px * 100:g}c as your own ask")
            if manual_cover > 0.01:
                note += (f" (your own resting ask for {manual_cover:g} "
                         "was left alone)")
            return {"ok": True, "note": note}
        return {"ok": False, "note": "no position on record for this market"}

    def live_view(self, slug: str) -> dict:
        """One tick of the live card: the book read STRAIGHT from the
        exchange this second — never the stored copy — with our orders
        and the position joined. The fresh read also lands in the cache,
        so the estimates sharpen while the owner watches."""
        fam = None
        for f in self.families.values():
            if slug in f.inventory or any(
                    o.market == slug for o in list(f.orders.values())):
                fam = f
                break
        if fam is None:
            for f in self.families.values():
                if f.knows(slug):
                    fam = f
                    break
        if fam is None:
            return {"ok": False, "note": "no family knows this market"}
        now = time.time()
        book = self.client.book(slug, fetched_at=now)
        fam.cache.put(slug, book)
        # the earnings math, recomputed on THIS second's book (owner,
        # 2026-08-26: "make it so that the earnings math is shown so I
        # get a sense of how much it's earning"): share of the side's
        # score x the side's daily pool, the exchange's own arithmetic
        from .scoring import estimate_join
        prog, prog_why = fam._prog_row(slug)
        side_pool = (fam._side_pool(slug, prog)
                     if prog is not None else None)
        ours = []
        for o in list(fam.orders.values()):
            if o.market != slug:
                continue
            row = {"id": o.id, "side": o.side, "price": o.price,
                   "qty": o.qty, "purpose": o.purpose,
                   "est": o.live_est, "pinned": bool(o.pinned),
                   "share": None, "qualifies": None}
            if prog is not None:
                lv = [(p, q - o.qty if abs(p - o.price) < 1e-9 else q)
                      for p, q in book.side(o.side)]
                lv = [(p, q) for p, q in lv if q > 1e-9]
                j = estimate_join(o.side, lv, book.tick, float(prog.df),
                                  float(prog.target), o.price, o.qty)
                row["share"] = round(j.share, 4)
                row["qualifies"] = bool(j.qualifies and j.in_window)
                if side_pool is not None:
                    row["est"] = round(j.share * side_pool
                                       if row["qualifies"] else 0.0, 4)
            ours.append(row)
        inv = fam.inventory.get(slug)
        # deliberately NO timestamp in the payload: the stream sends only
        # when something CHANGED, so a still book costs the phone nothing
        return {"ok": True, "market": slug,
                "name": self.names.label(slug),
                "tick": book.tick,
                "pool_day": (round(side_pool, 2)
                             if side_pool is not None else None),
                "prog_note": (prog_why if prog is None
                              else ("" if side_pool is not None
                                    else "pool share unconfirmed — no "
                                         "dollar figure until it is")),
                "bids": [[p, q] for p, q in book.bids[:10]],
                "asks": [[p, q] for p, q in book.asks[:10]],
                "ours": ours,
                "position": ({"qty": round(inv.get("qty", 0), 2),
                              "cost": round(inv.get("cost", 0), 2)}
                             if inv else None)}

    def _kick_tracker(self) -> None:
        """Ask 1.0 (same container) to refresh rewards.csv on GitHub so
        the committed record is current when the push lands. The file
        keeps exactly one writer."""
        pw = os.environ.get("DASH_PASSWORD", "")
        if not pw:
            return
        try:
            import requests
            requests.post(
                f"http://127.0.0.1:{os.environ.get('PORT', '8080')}/track_now",
                json={}, headers={"X-Dash-Key": pw, "X-Reprice": "1"},
                timeout=5)
        except Exception:  # noqa: BLE001 — best effort
            pass

    # -- the repo files 1.0 used to write (ported; single-writer gated) --

    def _gh_file(self, path: str):
        """(text, sha) of a repo file on main, or (None, None)."""
        tok = os.environ.get("GITHUB_TOKEN", "")
        if not tok:
            return None, None
        import requests
        repo = os.environ.get("GITHUB_REPOSITORY", "wfco223/Liquidity-rewards")
        r = requests.get(
            f"https://api.github.com/repos/{repo}/contents/{path}",
            headers={"Authorization": f"Bearer {tok}",
                     "Accept": "application/vnd.github+json"}, timeout=30)
        if r.status_code >= 400:
            return None, None
        j = r.json()
        import base64
        return base64.b64decode(j.get("content") or "").decode(), j.get("sha")

    def _gh_put(self, path: str, text: str, sha, message: str) -> bool:
        tok = os.environ.get("GITHUB_TOKEN", "")
        if not tok:
            return False
        import base64
        import requests
        repo = os.environ.get("GITHUB_REPOSITORY", "wfco223/Liquidity-rewards")
        body = {"message": message,
                "content": base64.b64encode(text.encode()).decode()}
        if sha:
            body["sha"] = sha
        r = requests.put(
            f"https://api.github.com/repos/{repo}/contents/{path}",
            headers={"Authorization": f"Bearer {tok}",
                     "Accept": "application/vnd.github+json"},
            json=body, timeout=30)
        return r.status_code < 300

    def compose_rewards_csv(self, rows: list[dict], existing: str | None) -> str:
        """The exact 1.0 file shape, with history the API no longer serves
        preserved from the existing file."""
        header = "date,market,program_type,reward_usd,status"
        fetched_min = min((r["date"] for r in rows), default="9999")
        keep = []
        for line in (existing or "").splitlines():
            if not line or line.startswith("date,"):
                continue
            if line.split(",", 1)[0] < fetched_min:
                keep.append(line)
        fresh = [f"{r['date']},{r['market']},{r['program_type']},"
                 f"{r['reward_usd']:g},{r['status']}" for r in rows]
        return "\n".join([header] + keep + fresh) + "\n"

    def compose_status_md(self, now: float) -> str:
        import datetime as _dt2
        ts = _dt2.datetime.fromtimestamp(now, _dt2.timezone.utc)
        et = ts.astimezone(ET_STATUS)
        lines = [f"# Liquidity rewards — 3.0",
                 f"",
                 f"✅ Updated {et.strftime('%b %d, %I:%M %p ET')} — the app "
                 f"writes this file every hour.", ""]
        total_rate = 0.0
        total_today = 0.0
        for key, fam in self.families.items():
            est = self.samplers[key]
            s = (self.last_state.get("summaries") or {}).get(key) or {}
            total_today += est.earned
            rate = est.rate
            total_rate += rate
            lines.append(
                f"- **{fam.cfg.name}**: about ${rate:,.2f}/day resting "
                f"(${est.earned:,.2f} accrued today), "
                f"{len(fam.orders)} orders, "
                f"${fam.family_spent():,.2f} of "
                f"${fam.cfg.capital_usd:,.0f} at risk"
                + (f" — includes holdings worth "
                   f"${fam.holdings_value():,.2f} at liquidation"
                   if fam.cfg.holdings_in_ceiling else "") + ".")
        lines += ["",
                  f"**Whole book: ~${total_rate:,.2f}/day; "
                  f"${total_today:,.2f} accrued today.**", "",
                  "Every number is arithmetic on the exchange's own reward "
                  "terms — no fudge factors. The pages have the detail: "
                  "orders (with plain-English verdicts), the model's moves, "
                  "and grades (estimate vs. what actually paid).", ""]
        return "\n".join(lines)

    def publish_trades(self, now: float, deep: bool = False) -> dict:
        """The definitive transaction record: the exchange's own
        activity history, published to data/trades.csv (owner,
        2026-08-23: "get the transaction history so we can have a
        definitive record of what is happening"). Deep at boot, a few
        pages hourly after — the file is append-only and deduplicated,
        so overlap costs nothing."""
        try:
            raw = self.client.activities(pages=25 if deep else 3)
        except Exception as e:  # noqa: BLE001 — never breaks the loop
            self._note(f"trades history: {e}")
            return {"ok": False, "note": str(e)[:120]}
        rows = parse_activities(raw)
        # One-time shape probe: if the exchange's order object already
        # carries a creation time, resting periods come free for
        # history too — no ledger needed for the past. Written once so
        # it can be read rather than guessed at.
        if raw and not getattr(self, "_act_shape_noted", False):
            self._act_shape_noted = True
            try:
                for a in raw:
                    t = (a.get("trade") or {})
                    ex = (t.get("passiveExecution")
                          or t.get("aggressorExecution") or {})
                    o = ex.get("order") or {}
                    if o:
                        self._note("activity order fields: "
                                   + ",".join(sorted(o.keys()))
                                   + " | execution fields: "
                                   + ",".join(sorted(ex.keys())))
                        break
            except Exception:  # noqa: BLE001
                pass
        kinds = {}
        for r in rows:
            kinds[r["type"]] = kinds.get(r["type"], 0) + 1
        try:
            existing, sha = self._gh_file("data/trades.csv")
            text, added = trades_csv_append(existing, rows)
            if added:
                self._gh_put("data/trades.csv", text, sha,
                             f"trade history: +{added} rows [skip ci]")
        except Exception as e:  # noqa: BLE001
            self._note(f"trades publish: {e}")
            return {"ok": False, "note": str(e)[:120]}
        self._note(f"trade history: {len(raw)} activities, {len(rows)} ours, "
                   f"+{added} new rows; kinds={kinds}")
        return {"ok": True, "activities": len(raw), "parsed": len(rows),
                "added": added, "kinds": kinds}

    def backfill_journal(self, days: float = 3.0,
                         dry_run: bool = True) -> dict:
        """Walk the exchange's transaction record against the fills
        journal and add rows for executions the journal never recorded
        (owner, 2026-08-23).

        Matching is by ORDER ID — the exchange's own handle, exact even
        when two orders rest at one price (owner: "keep track of the
        order id in the future so we can match it up"). Journal rows
        written before order ids were recorded carry none, so their
        shares stay available as a per-market/side/price CREDIT that
        each unmatched execution consumes before claiming a shortfall;
        that keeps the transition conservative — it can under-recover,
        never double-count. Recovered rows carry the order id, so the
        next run matches them exactly. Inventory is never touched: the
        exchange's position feed stays the sole authority."""
        from collections import defaultdict
        try:
            raw = self.client.activities(pages=25)
        except Exception as e:  # noqa: BLE001
            return {"ok": False, "note": f"history fetch: {str(e)[:120]}"}
        cutoff = time.time() - days * 86400.0
        ex: dict = defaultdict(lambda: {"shares": 0.0, "ts": 0.0,
                                        "market": "", "side": "", "px": 0.0,
                                        "placed_ts": None})
        for r in parse_activities(raw):
            if r["type"] != "ACTIVITY_TYPE_TRADE":
                continue
            if not (r["market"] and r["side"] and r["price"]
                    and r["shares"] and r["order_id"]):
                continue
            if (r["ts"] or 0) < cutoff:
                continue
            g = ex[r["order_id"]]
            g["shares"] += r["shares"]
            g["ts"] = max(g["ts"], r["ts"])
            g["market"], g["side"] = r["market"], r["side"]
            g["px"] = round(r["price"], 4)
            if r.get("placed_ts"):
                g["placed_ts"] = r["placed_ts"]
        jr_oid: dict = defaultdict(float)
        legacy: dict = defaultdict(float)
        owner_of: dict = {}
        for tag, fam in self.families.items():
            for row in fam.fills:
                if (row.get("ts") or 0) < cutoff:
                    continue
                owner_of[row.get("market")] = tag
                qty = row.get("qty") or 0.0
                oid = row.get("oid")
                if oid:
                    jr_oid[oid] += qty
                else:
                    legacy[(row.get("market"), row.get("side"),
                            round(row.get("px") or 0, 4))] += qty
        added, skipped, rows_out = 0, 0, []
        for oid, g in sorted(ex.items(), key=lambda kv: kv[1]["ts"]):
            short = g["shares"] - jr_oid.get(oid, 0.0)
            if oid not in jr_oid:
                k = (g["market"], g["side"], g["px"])
                take = min(short, legacy.get(k, 0.0))
                if take > 0:
                    legacy[k] -= take
                    short -= take
            if round(short, 4) <= 0.005:
                continue
            tag = owner_of.get(g["market"])
            if tag is None:
                for t2, fam in self.families.items():
                    if fam.knows(g["market"]):
                        tag = t2
                        break
            if tag is None:
                skipped += 1
                continue
            rows_out.append({"family": tag, "market": g["market"],
                             "side": g["side"], "px": g["px"],
                             "qty": short, "ts": g["ts"], "oid": oid,
                             "placed_ts": g.get("placed_ts")})
            added += 1
        fed_odds = [0]
        if not dry_run:
            for r in rows_out:
                fam = self.families[r["family"]]
                fam.fills.append({
                    "ts": round(r["ts"], 1), "market": r["market"],
                    "side": r["side"], "qty": round(r["qty"], 2),
                    "px": r["px"], "oid": r["oid"], "purpose": "backfill",
                    "why": "recovered from the exchange\u2019s transaction "
                           "history \u2014 this fill was never journaled",
                    "est_day": None, "rested_h": None, "fair": None,
                    "band": None, "conf": None, "touch_bid": None,
                    "touch_ask": None, "conc": None,
                    "pos_after": None,
                    # exact resting period when we still know when the
                    # order went on the book (owner, 2026-08-23)
                    "rested_h": (round((r["ts"] - placed) / 3600.0, 2)
                                 if (placed := (r.get("placed_ts")
                                     or fam.placed_at.get(r["oid"])))
                                 and r["ts"] > placed else None)})
                # a recovered fill is real evidence about where this
                # market trades, so it corrects the band the engine
                # prices against (owner approved, 2026-08-23). Its own
                # timestamp carries it: evidence decays on a 36h half
                # life, so an older recovery lands lighter. NOT fed to
                # the fill-odds model — that needs the order's PLACED
                # time, which the exchange record does not carry, and
                # inventing one would poison the odds with fiction.
                fam.evidence.fill(r["market"], r["side"], r["px"],
                                  ts=r["ts"])
                # and the fill-odds model, but ONLY with a real resting
                # period measured from our own placement ledger. No
                # ledger entry means no observation — a guessed resting
                # time would poison the odds that price every order.
                # the exchange's own createTime first — it covers
                # history, which our ledger cannot; the ledger backs it
                placed = r.get("placed_ts") or fam.placed_at.get(r["oid"])
                if placed and r["ts"] > placed:
                    fam.fillmodel.observe_fill_age(r["market"],
                                                   r["ts"] - placed)
                    fed_odds[0] += 1
                fam.fills.sort(key=lambda x: x.get("ts") or 0.0)
            self._note(f"journal backfill: +{added} rows from the exchange "
                       f"record ({days:g} days, matched by order id)")
            self.freeze_payload()
        return {"ok": True, "dry_run": dry_run, "added": added,
                "skipped_unknown_market": skipped, "days": days,
                "shares": round(sum(r["qty"] for r in rows_out), 2),
                "odds_fed": fed_odds[0],
                "sample": [f"{r['market'][:34]} {r['side']} "
                           f"{r['qty']:g}@{r['px']*100:g}c"
                           for r in rows_out[:8]]}

    def _depth_of(self, family: str, market: str) -> int:
        """How many price levels the last book for this market carried.

        There is no cache on the Monitor — each family owns its own, and
        writing self.cache here threw on every publish, so the whole
        per-market ledger stopped being written from the moment the
        depth column was added ("'Monitor' object has no attribute
        'cache'", every hour, swallowed by the ledger's own try/except).
        The share measurement itself was never lost: the estimator banks
        it in state. Only the CSV rows went missing."""
        fam = self.families.get(family)
        cache = getattr(fam, "cache", None) if fam is not None else None
        if cache is None:
            return 0
        return int(getattr(cache, "depth_seen", {}).get(market, 0) or 0)

    def _family_of(self, market: str) -> str:
        """Which family a rewarded market belongs to. The families'
        own universes are the authority — a market can only earn where
        the engine quotes it. Falls back to the prefixes for a market
        that has since left a universe (a settled game, a closed race),
        which is most of the football rows by the time they pay."""
        for key, fam in self.families.items():
            if market in fam.universe:
                return key
        low = market.lower()
        if low.startswith(("tec-nba-", "aqc-nba-", "ftsc-nba-", "fptc-nba-")):
            return "nba"
        if "nfl" in low:
            return "nfl"
        if "cfb" in low or "ncaaf" in low:
            return "cfb"
        return "politics"

    def _feed_check(self, now: float) -> None:
        """The approved live-feed test (owner, 2026-08-25, log-only):
        for a few markets whose cached book was last written by the
        STREAM, fetch the same book fresh over REST and log both side
        by side. If the stream-written picture is consistently thinner,
        the feed is overwriting whole books with partial updates — the
        prime suspect for the inflated share estimates. Changes
        nothing; three extra fetches an hour."""
        done = 0
        for key, fam in self.families.items():
            if done >= 3:
                break
            for slug, w in list(fam.cache.last_writer.items()):
                if done >= 3:
                    break
                if w != "ws":
                    continue
                cached = fam.cache.any_age(slug)
                if cached is None or now - cached.fetched_at > 90:
                    continue
                try:
                    fresh = self.client.book(slug, fetched_at=now)
                except Exception as e:  # noqa: BLE001
                    self._note(f"feed check: {slug[:40]} REST err "
                               f"{str(e)[:50]}")
                    done += 1
                    continue
                def _shape(b):
                    bb = b.bids[0][0] * 100 if b.bids else 0
                    ba = b.asks[0][0] * 100 if b.asks else 0
                    return (f"{len(b.bids)}+{len(b.asks)} lvls "
                            f"{bb:.0f}c/{ba:.0f}c")
                self._note(
                    f"feed check: {slug[:40]}  stream-cache("
                    f"{now - cached.fetched_at:.0f}s old)={_shape(cached)}"
                    f"  fresh-REST={_shape(fresh)}")
                done += 1

    def publish_files(self, now: float) -> None:
        """Hourly, and only while 1.0 is retired (one writer per file)."""
        if os.environ.get("V1_ENABLED", "0") != "0":
            return
        if now - getattr(self, "_pub_at", 0.0) < 3600.0:
            return
        self._pub_at = now
        try:
            self._feed_check(now)
        except Exception as e:  # noqa: BLE001 — a diagnostic, never a blocker
            self._note(f"feed check failed: {type(e).__name__}: {e}")
        try:
            # FILL-MODEL CALIBRATION, out loud (owner, 2026-08-25: the
            # expected-risk budget leans on these odds, so they are
            # graded hourly): the model's own expected fills per day
            # across the resting book, beside actual fills in the last
            # 24h. Drift past ~2x is the tripwire to raise with the
            # owner.
            for key, fam in self.families.items():
                exp_day = sum(o.live_pf for o in fam.orders.values()
                              if o.live_pf is not None
                              and o.purpose != "manual")
                actual = sum(1 for f in fam.fills
                             if (f.get("ts") or 0) > now - 86400)
                if exp_day or actual:
                    self._note(
                        f"fill calibration {key}: model expects "
                        f"{exp_day:.1f} fills/day resting; actual last "
                        f"24h: {actual}"
                        + ("  <-- DRIFTING" if exp_day > 0 and
                           (actual > 2 * exp_day + 2
                            or exp_day > 2 * actual + 2) else ""))
                    self._note(
                        f"risk {key}: expected ${fam.family_spent():.2f}"
                        f"/{fam.cfg.capital_usd:.0f}  gross "
                        f"${fam.family_gross():.2f}/{fam.gross_cap():.0f}")
        except Exception as e:  # noqa: BLE001
            self._note(f"fill calibration failed: {type(e).__name__}: {e}")
        try:      # the estimate ledger: every day's prediction, kept
                  # until the exchange settles it (owner, 2026-08-23)
            from .estimator import et_day
            rows = []
            for key, est in self.samplers.items():
                for h in est.history:
                    rows.append((h["day"], key, h.get("earned") or 0.0,
                                 (h.get("stale_s") or 0.0) / 60.0))
                if est.day:
                    rows.append((est.day, key, est.earned,
                                 est.stale_s / 60.0))
            if rows:
                existing, sha = self._gh_file("data/estimates.csv")
                text, n = estimates_csv_append(
                    existing, et_day(now), rows, self.actuals_by_day,
                    time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
                    paid_by_fam={tuple(k.split("|", 1)): v for k, v
                                 in self.actuals_by_fam.items()})
                if n:
                    self._gh_put("data/estimates.csv", text, sha,
                                 f"estimates: {n} rows [skip ci]")
        except Exception as e:  # noqa: BLE001
            self._note(f"estimates ledger: {e}")
        try:      # ...and the same thing per MARKET, so a race can be
                  # graded against its own prediction (2026-08-24)
            from .estimator import et_day
            day = et_day(now)
            per: dict = {}
            for key, fam in self.families.items():
                for o in fam.orders.values():
                    if o.purpose == "manual":   # not our prediction
                        continue
                    a = per.setdefault((day, o.market, key),
                                       {"est": 0.0, "n": 0})
                    a["est"] += o.live_est or 0.0
                    a["n"] += 1
            cal = {}
            for key in self.families:
                est = self.samplers.get(key)
                if est is not None:
                    cal.update(est.calibration())
            mrows = [(d, m, f, a["est"], a["n"],
                      (cal.get(m) or {}).get("share", 0.0),
                      (cal.get(m) or {}).get("pool_day", 0.0),
                      (cal.get(m) or {}).get("live_h", 0.0),
                      self._depth_of(f, m))
                     for (d, m, f), a in per.items()]
            if mrows:
                existing, sha = self._gh_file("data/market_est.csv")
                text, n = market_est_append(
                    existing, day, mrows, self.rewards_seen,
                    time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)))
                if n:
                    self._gh_put("data/market_est.csv", text, sha,
                                 f"market estimates: {n} rows [skip ci]")
        except Exception as e:  # noqa: BLE001
            self._note(f"market estimate ledger: {e}")
        try:
            self.publish_trades(now, deep=not getattr(self, "_trades_deep",
                                                      False))
            self._trades_deep = True
        except Exception as e:  # noqa: BLE001
            self._note(f"trades: {e}")
        # one-shot recovery of fills the journal never recorded (owner,
        # 2026-08-23: "Do it"). Runs once, then the flag is persisted;
        # the fills page keeps a button for later runs. Additive and
        # idempotent, so a repeat would be harmless anyway.
        if not self.evidence_seeded:
            # the 554 rows recovered before evidence feeding existed
            n = 0
            try:
                for fam in self.families.values():
                    for row in fam.fills:
                        if row.get("purpose") != "backfill":
                            continue
                        if not (row.get("market") and row.get("side")
                                and row.get("px")):
                            continue
                        fam.evidence.fill(row["market"], row["side"],
                                          row["px"], ts=row.get("ts"))
                        n += 1
                self.evidence_seeded = True
                self._note(f"evidence seeded from {n} recovered fills")
            except Exception as e:  # noqa: BLE001
                self._note(f"evidence seed: {e}")
        if not self.backfilled:
            try:
                r = self.backfill_journal(days=3.0, dry_run=False)
                if r.get("ok"):
                    self.backfilled = True
            except Exception as e:  # noqa: BLE001
                self._note(f"backfill: {e}")
        try:
            import datetime as _dt3
            start = (_dt3.datetime.now(_dt3.timezone.utc)
                     - _dt3.timedelta(days=40)).strftime("%Y-%m-%d")
            rows = self.client.earnings(start)
            existing, sha = self._gh_file("data/rewards.csv")
            text = self.compose_rewards_csv(rows, existing)
            if text != existing:
                self._gh_put("data/rewards.csv", text, sha,
                             "Update rewards.csv [skip ci]")
        except Exception as e:  # noqa: BLE001
            self._note(f"rewards.csv publish: {e}")
        try:
            frows = [(r.get("ts", 0.0), tag, r)
                     for tag, fam in self.families.items()
                     for r in fam.fills]
            if frows:
                existing, sha = self._gh_file("data/fills.csv")
                text, added = fills_csv_append(existing, frows)
                if added:
                    self._gh_put("data/fills.csv", text, sha,
                                 f"fills archive: +{added} rows [skip ci]")
        except Exception as e:  # noqa: BLE001
            self._note(f"fills.csv publish: {e}")
        try:
            for path, text in (("data/silver_gov_races.csv",
                                getattr(self.silver, "gov_raw", "")),
                               ("data/silver_senate_races.csv",
                                getattr(self.silver, "senate_raw", ""))):
                if not text:
                    continue
                existing, sha = self._gh_file(path)
                if existing is not None and existing != text:
                    self._gh_put(path, text, sha,
                                 "Silver model refresh [skip ci]")
            existing, sha = self._gh_file("STATUS.md")
            text = self.compose_status_md(now)
            if text != existing:
                self._gh_put("STATUS.md", text, sha,
                             "Update STATUS.md [skip ci]")
        except Exception as e:  # noqa: BLE001
            self._note(f"STATUS.md publish: {e}")

    def refresh_rewards(self) -> dict:
        """Owner's button: pull the exchange's posted payouts now, show
        what is new since the last look, and fold the day totals into the
        grades page. Reads only — rewards.csv on GitHub stays 1.0's file
        to write."""
        import datetime as _dt
        start = (_dt.datetime.now(_dt.timezone.utc)
                 - _dt.timedelta(days=6)).strftime("%Y-%m-%d")
        rows = self.client.earnings(start)
        first = not self.rewards_seen
        # The exchange splits one market-day into SEVERAL rows (a SKIPPED
        # row and a PAID row of different amounts), and each call returns
        # a different set of ancient strays outside the asked window. So:
        # AGGREGATE per market-day before diffing, remember everything
        # ever seen (never date-pruned, size-capped instead), and only
        # SHOW news from the last few days — older strays are absorbed
        # silently (owner, 2026-08-21: "still off").
        agg: dict[str, dict] = {}
        for r in rows:
            key = f"{r['date']}|{r['market']}"
            a = agg.setdefault(key, {"date": r["date"], "market": r["market"],
                                     "usd": 0.0, "paid": 0.0, "status": set()})
            a["usd"] += r["reward_usd"]
            a["status"].add(r["status"])
            if r["status"] != "SKIPPED":
                a["paid"] += r["reward_usd"]
        seen = self.rewards_seen
        fresh = []
        totals: dict[str, float] = {}
        for key, a in agg.items():
            totals[a["date"]] = totals.get(a["date"], 0.0) + a["paid"]
            if abs(seen.get(key, -1.0) - round(a["usd"], 2)) > 0.005:
                fresh.append(a)
            seen[key] = round(a["usd"], 2)
        if len(seen) > 12000:
            for k in sorted(seen)[:len(seen) - 12000]:
                del seen[k]
        self.rewards_seen = seen
        for d, v in totals.items():
            self.actuals_by_day[d] = round(v, 2)
        for key, a in agg.items():           # ...and per family, so the
            fam = self._family_of(a["market"])   # ledger grades each
            if not fam:                          # one on its own money
                continue
            fk = f"{a['date']}|{fam}"
            self.actuals_by_fam[fk] = round(
                self.actuals_by_fam.get(fk, 0.0) + a["paid"], 2)
        if len(self.actuals_by_fam) > 4000:
            for k in sorted(self.actuals_by_fam)[:len(self.actuals_by_fam) - 4000]:
                del self.actuals_by_fam[k]
        # the baseline must survive a deploy between now and the next save
        # — local AND remote, immediately (a rebuild replaces the disk)
        if self.last_state:
            self.last_state["rewards_seen"] = self.rewards_seen
            self.last_state["actuals_by_day"] = self.actuals_by_day
            self.store.save_local(self.last_state)
            self.store.save_remote(self.last_state)
        days = {d: round(v, 2) for d, v in sorted(totals.items())}
        if first:
            # the FIRST check has nothing to compare against — every row
            # would read "new". Record the baseline and say so plainly.
            latest = max(totals) if totals else "?"
            self._note(f"rewards baseline: {len(rows)} rows through {latest}")
            return {"ok": True, "new_rows": [], "new_count": 0, "days": days,
                    "note": (f"First check: I recorded a baseline of "
                             f"{len(rows):,} rows through {latest}. From "
                             f"now on this button shows only what is new.")}
        if len(fresh) > max(400, 0.5 * len(rows)):
            # more than half the window "changed" means the baseline was
            # lost (a deploy race), not that thousands of rows posted at
            # once. Re-record it and say so, instead of spamming old rows.
            latest = max(totals) if totals else "?"
            self._note(f"rewards baseline re-recorded ({len(fresh)} rows)")
            return {"ok": True, "new_rows": [], "new_count": 0, "days": days,
                    "note": (f"The baseline was lost in a restart, so I "
                             f"re-recorded it ({len(rows):,} rows through "
                             f"{latest}). Press again later — only true "
                             f"news will show.")}
        if len(fresh) > max(400, 0.5 * len(agg)):
            # more than half the window "changed" means the memory was
            # lost or its format moved — re-record it, never spam old rows
            latest = max(totals) if totals else "?"
            self._note(f"rewards baseline re-recorded ({len(fresh)} rows)")
            return {"ok": True, "new_rows": [], "new_count": 0, "days": days,
                    "note": (f"I re-recorded the baseline "
                             f"({len(agg):,} market-days through {latest}). "
                             f"From here only true news shows.")}
        show_from = (_dt.datetime.now(_dt.timezone.utc)
                     - _dt.timedelta(days=4)).strftime("%Y-%m-%d")
        shown = [a for a in fresh if a["date"] >= show_from]
        shown.sort(key=lambda a: (a["date"], a["usd"]), reverse=True)
        out_rows = [{"day": a["date"], "market": a["market"],
                     "name": self.names.label(a["market"]),
                     "usd": round(a["usd"], 2),
                     "status": "/".join(sorted(a["status"]))}
                    for a in shown[:40]]
        self._note(f"rewards check: {len(shown)} new market-days shown, "
                   f"{len(fresh) - len(shown)} old strays absorbed")
        return {"ok": True, "new_rows": out_rows, "new_count": len(shown),
                "days": days}

    def _lite_study(self) -> dict:
        """Declared-anchor scoring study (owner, 2026-08-21): what each
        of our markets would pay if scoring anchors on the exchange's
        DECLARED best bid/ask instead of the raw touch. Read-only."""
        if self.stream is None:
            return {"note": "no stream"}
        declared = dict(getattr(self.stream, "declared", {}) or {})
        if not declared:
            return {"note": "no lite frames yet"}
        rows: list[dict] = []
        n_cov = n_div = 0
        tot_cur = tot_alt = 0.0
        for tag, fam in self.families.items():
            for slug in {o.market for o in fam.orders.values()}:
                d = declared.get(slug)
                if not d:
                    continue
                r = fam.lite_recalc(slug, d[0], d[1])
                if r is None:
                    continue
                n_cov += 1
                div = ((r["bb"] is not None and r["raw_bid"] is not None
                        and abs(r["bb"] - r["raw_bid"]) > 0.005)
                       or (r["ba"] is not None and r["raw_ask"] is not None
                           and abs(r["ba"] - r["raw_ask"]) > 0.005))
                r["diverges"] = div
                r["family"] = tag
                n_div += 1 if div else 0
                tot_cur += r["est_cur"]
                tot_alt += r["est_alt"]
                rows.append(r)
        rows.sort(key=lambda x: -abs(x["est_alt"] - x["est_cur"]))
        return {"covered": n_cov, "divergent": n_div,
                "est_current_total": round(tot_cur, 2),
                "est_declared_total": round(tot_alt, 2),
                "rows": rows[:60]}

    def fills_view(self) -> dict:
        """Every purchase as a round trip, newest activity first, joined
        with where the market stands now — one report per entry lot,
        updated as its closes land."""
        rows = []
        hidden_open = 0
        hidden_recon = 0
        for tag, fam in self.families.items():
            for card in pair_fills(fam.fills):
                card["family"] = tag
                card["name"] = self.names.label(card["market"])
                b = fam.cache.any_age(card["market"])
                card["now_bid"] = (b.bids[0][0]
                                   if b is not None and b.bids else None)
                card["now_ask"] = (b.asks[0][0]
                                   if b is not None and b.asks else None)
                inv = fam.inventory.get(card["market"])
                card["pos_now"] = (round(inv.get("qty", 0.0), 2)
                                   if inv else 0.0)
                exits = [o for o in fam.orders.values()
                         if o.market == card["market"]
                         and o.purpose == "sell"]
                card["exit_resting"] = bool(exits)
                now = time.time()
                card["exit_rate"] = round(sum((o.live_est or 0.0)
                                              for o in exits), 4)
                card["exit_earned"] = round(sum(
                    (o.live_est or 0.0) * (now - o.placed_ts) / 86400.0
                    for o in exits if o.placed_ts > 0), 4)
                card["net"] = round(card_net(card), 4)
                # Cards the journal never saw closed: the position is
                # flat but the closes are missing, so there is no price
                # and no P&L to show. The owner, 2026-08-23:
                # "essentially useless to me for now" — counted, not
                # listed. The exchange's own record of them lives in
                # data/trades.csv.
                if ((card.get("open_qty") or 0) > 0.005
                        and not card.get("stray_close")
                        and card.get("pos_now") is not None
                        and abs(card["pos_now"]) < 0.005):
                    hidden_recon += 1
                    continue
                if not card_visible(card, now):
                    if card_is_open(card):
                        hidden_open += 1   # open AND profitable — off
                                           # the list, still counted
                    continue
                rows.append(card)
        # Cap each group SEPARATELY. A single rows[:150] after an
        # open-first sort let 150 open cards eat the whole budget and
        # the closed tab came up empty however many real round trips
        # existed (owner, 2026-08-23: "I'm not seeing any").
        def recent(x):
            return -x.get("last_ts", x["ts"])
        is_open = (lambda x: (x.get("open_qty", 0) > 0.005
                              and not x.get("stray_close")))
        opens = sorted([r for r in rows if is_open(r)], key=recent)[:120]
        closes = sorted([r for r in rows if not is_open(r)],
                        key=recent)[:120]
        return {"ok": True, "fills": opens + closes,
                "open_total": sum(1 for r in rows if is_open(r)),
                "closed_total": sum(1 for r in rows if not is_open(r)),
                "open_hidden": hidden_open,
                "hidden_reconciled": hidden_recon,
                "pending": self._pending_fills()}

    def _pending_fills(self) -> list[dict]:
        """Vanished orders waiting for the position feed or the trade
        history to confirm — shown gray in the closed cards (owner,
        2026-08-23: "include the card in the closed section colored
        gray and note it is waiting for position to close out")."""
        from .family import GONE_GRACE_S
        out = []
        for tag, fam in self.families.items():
            for oid, gp in list(fam.gone_pending.items()):
                rec = gp["rec"]
                out.append({"market": rec.market, "family": tag,
                            "name": self.names.label(rec.market),
                            "side": rec.side, "qty": rec.qty,
                            "px": rec.price,
                            "ts": gp["until"] - GONE_GRACE_S})
        out.sort(key=lambda r: -r["ts"])
        return out

    def book_view(self, slug: str) -> dict:
        """The raw shape of one market's book, with our own orders
        marked — the owner looks at the truth himself."""
        for fam in self.families.values():
            b = fam.cache.any_age(slug)
            if b is None:
                continue
            ours = [{"side": o.side, "price": o.price, "qty": o.qty,
                     "purpose": o.purpose, "est": o.live_est,
                     "verdict": o.verdict}
                    for o in fam.orders.values() if o.market == slug]
            inv = fam.inventory.get(slug)
            return {"ok": True, "market": slug,
                    "name": self.names.label(slug),
                    "age_s": round(time.time() - b.fetched_at, 1),
                    "tick": b.tick,
                    "bids": [[p, q] for p, q in b.bids[:12]],
                    "asks": [[p, q] for p, q in b.asks[:12]],
                    "ours": ours,
                    "fair": (self.silver.model_fair(slug)
                             if hasattr(self, "silver") else None),
                    "band": fam._band(slug, b.bids, b.asks, b.tick),
                    "conf": round(fam.evidence.confidence(slug), 3),
                    "position": ({"qty": round(inv.get("qty", 0), 2),
                                  "cost": round(inv.get("cost", 0), 2)}
                                 if inv else None),
                    "ladder": fam.ladder_view(slug)}
        return {"ok": False, "note": "no book cached for this market yet"}

    def public_state(self) -> dict:
        st = dict(self.last_state) if self.last_state else {"saved_at": 0}
        st["switch_view"] = {
            "master": self.master.state(),
            **{k: self.switches[k].state() for k in self.families}}
        st["floor"] = self.floor.status()
        return st

    # what the phone pages actually read. The old payload shipped the
    # whole state minus fam_* — 1.85 MB a refresh — and worse, the web
    # thread serialized LIVE dicts while the cycle thread mutated them:
    # "dictionary changed size during iteration" dropped the socket and
    # every page read "unreachable" while the app was healthy
    # (2026-08-22 night). The payload is now frozen to bytes at the end
    # of each cycle, on the cycle's own thread, under the cycle's lock.
    PHONE_KEYS = ("owner_fairs",
                  "saved_at", "build", "boot_ts", "errors", "audit",
                  "master_switch", "flatten", "flat_stats", "summaries",
                  "silver", "silver_log", "grades", "paid_total", "ws",
                  "alerts_log", "rewards_last", "floor")

    def build_phone_payload(self) -> dict:
        st = self.public_state()
        d = {k: st[k] for k in self.PHONE_KEYS if k in st}
        for k in st:
            if k.startswith("est_") or k.startswith("sw_") \
                    or k == "switch_view":
                d[k] = st[k]
        labels: dict[str, str] = {}
        slugs: set[str] = set()
        for key, s in (st.get("summaries") or {}).items():
            for o in s.get("orders") or []:
                slugs.add(o.get("market") or "")
            for b in s.get("best_idle") or []:
                slugs.add(b.get("market") or "")
            for t in s.get("triage_feed") or []:
                slugs.add(t.get("market") or "")
            slugs.update((s.get("inventory") or {}).keys())
            fam = self.families.get(key)
            if fam is not None:
                d[f"fam_log_{key}"] = [dict(r) for r in fam.log[-80:]]
                for row in d[f"fam_log_{key}"]:
                    mkt = row.get("market")
                    if mkt:
                        slugs.add(mkt)
        for s in slugs:
            if s:
                labels[s] = self.names.label(s)
        d["labels"] = labels
        d["now"] = time.time()
        d["boot"] = dict(self.boot_stage or {})
        return d

    def freeze_payload(self) -> None:
        try:
            self.payload_json = json.dumps(
                self.build_phone_payload()).encode()
        except Exception as e:  # noqa: BLE001 — a stale payload beats none
            self._note(f"payload freeze: {e}")

    # -- one poll -----------------------------------------------------------

    def _flatten_pass(self, orders: list[dict], positions: dict) -> dict:
        """Cancel opening orders, a batch per cycle for the rate limiter;
        exits are never touched. Runs only once 1.0/2.0 have stood down.
        In phase two (flatten_done) it turns guard: orders the 3.0
        families own are exempt — they are the rebuild."""
        desk = self.families["politics"].desk
        owned = {oid for fam in self.families.values() for oid in fam.orders}
        done = kept = remaining = 0
        if self.flatten_done:
            # Phase two was a janitor: cancel any open order the families
            # did not own. Since 2026-08-22 an unknown order IS THE
            # OWNER'S OWN ("Don't let it cancel orders I set by hand") —
            # this guard cancelled 964 orders, his hand-placed ones
            # included, racing adoption every cycle. It now only reports.
            kept = sum(1 for o in orders if is_exit_order(o, positions))
            return {"active": True, "phase": "rebuild",
                    "kept_exits": kept, "remaining": 0,
                    "cancelled_now": 0,
                    "cancelled_total": self.flat_stats["cancelled"],
                    "failed_total": self.flat_stats["failed"]}
        for o in orders:
            if not (o.get("id") and o.get("market")):
                continue
            if is_exit_order(o, positions):
                kept += 1
                continue
            if self.flatten_done and o["id"] in owned:
                continue
            if done >= FLATTEN_CANCELS_PER_CYCLE:
                remaining += 1
                continue
            r = desk.cancel(o["id"], o["market"], initiator="flatten")
            if r.ok:
                done += 1
                self.flat_stats["cancelled"] += 1
                for fam in self.families.values():
                    fam.orders.pop(o["id"], None)
            else:
                self.flat_stats["failed"] += 1
            time.sleep(0.2)
        if not self.flatten_done and done == 0 and remaining == 0:
            self.flatten_done = True
            self.alerts.notify(
                "Flat — no spending risk left",
                f"kept {kept} exit orders, cancelled "
                f"{self.flat_stats['cancelled']} opening orders. The $100 "
                f"politics rebuild starts now, guided by what paid best.")
        return {"active": True, "phase": ("rebuild" if self.flatten_done
                                          else "cancelling"),
                "kept_exits": kept, "remaining": remaining,
                "cancelled_now": done,
                "cancelled_total": self.flat_stats["cancelled"],
                "failed_total": self.flat_stats["failed"]}

    def cycle(self, now: float | None = None) -> dict:
        now = now or time.time()
        with self._lock:
            return self._cycle_locked(now)

    def _stage(self, stage: str, pct: int) -> None:
        if not self._first_cycle_done:
            self.boot_stage = {"stage": stage, "pct": pct,
                               "ts": round(time.time(), 1)}

    def _cycle_locked(self, now: float) -> dict:
        self._stage("checking the floor and switches", 5)
        self.flatten = flatten_active()
        self.floor.write_want(self.master.on or self.flatten)
        self._floor_ok = self.floor.acked(now)
        self._stage("fetching the account's resting orders", 10)
        orders = self.client.open_orders()
        self._stage("fetching positions", 18)
        positions = self.client.positions_net()
        self.last_flat = None
        if self.flatten and self._floor_ok:
            self.last_flat = self._flatten_pass(orders, positions)
        trades_by_oid: dict[str, float] = {}
        if any(fam.gone_pending for fam in self.families.values()):
            # vanished orders waiting for confirmation: ask the
            # exchange's own trade history by ORDER ID — the definitive
            # source (owner, 2026-08-23: "is there no way to see
            # transaction history and backfill?" — there is)
            try:
                for a in self.client.recent_trades(limit=50):
                    t = a.get("trade") or {}
                    for exk in ("passiveExecution", "aggressorExecution"):
                        ex = t.get(exk) or {}
                        o = ex.get("order") or {}
                        it = str(o.get("intent") or "")
                        if o.get("id") and it and not it.endswith("UNDEFINED"):
                            try:
                                sh = float(ex.get("lastShares") or 0)
                            except (TypeError, ValueError):
                                sh = 0.0
                            if sh > 0:
                                oid = str(o["id"])
                                trades_by_oid[oid] = (
                                    trades_by_oid.get(oid, 0.0) + sh)
            except Exception as e:  # noqa: BLE001 — history is a bonus
                self._note(f"trade history: {e}")
        try:
            self.silver.refresh(now)     # TTL-gated inside
        except Exception as e:  # noqa: BLE001 — the model never kills the loop
            self._note(f"silver: {e}")
        # the payout watcher (ported from 2.0, owner-approved): every five
        # minutes, diff the exchange's posted rewards and push the phone
        # the moment something new lands
        if now - self._rw_at > 300.0:
            self._rw_at = now
            try:
                res = self.refresh_rewards()
                if res.get("new_count"):
                    self.rw_last = res
                    days = sorted((res.get("days") or {}).items())[-2:]
                    line = ", ".join(f"{d[5:]} ${v:,.2f}" for d, v in days)
                    self.alerts.notify(
                        "Rewards posted",
                        f"{res['new_count']} new rows at the exchange; "
                        f"latest day totals: {line}")
                    self._kick_tracker()
            except Exception as e:  # noqa: BLE001 — watching never breaks
                self._note(f"rewards watch: {e}")
        self.publish_files(now)
        if now - self._history_at > 6 * 3600.0:
            self._history_at = now
            hist, day_totals, recent = load_history()
            if hist:
                for fam in self.families.values():
                    fam.history = hist
                    fam.recent_paid = recent
            if day_totals:
                self.actuals_by_day = day_totals
        summaries = {}
        fam_pct = {"politics": 25, "cfb": 78, "nfl": 88, "nba": 92}
        for key, fam in self.families.items():
            self._stage(f"{fam.cfg.name}: discovering, reading terms, "
                        f"scoring books", fam_pct.get(key, 94))
            if fam.cfg.proven_usd > 0:
                # graduation takes STABILITY and HIGH EARNINGS (owner,
                # 2026-08-22): paid on 3+ of the last 7 days, averaging
                # at least the bar — no reaching back to the old era
                fam.proven = {
                    mkt for mkt, (avg, nd)
                    in getattr(fam, "recent_paid", {}).items()
                    if avg >= fam.cfg.graduate_paid_usd
                    and nd >= fam.cfg.graduate_days}
            on = self.master.on and self.switches[key].on and self._floor_ok
            foreign = {oid for k2, f2 in self.families.items() if k2 != key
                       for oid in f2.orders}
            try:
                exits_only = self.flatten and not self.flatten_done
                summaries[key] = fam.cycle(now, orders, positions,
                                           self.client, on,
                                           foreign_ids=foreign,
                                           exits_only=exits_only,
                                           trades=trades_by_oid)
                summaries[key]["name"] = fam.cfg.name
                est = self.samplers[key]
                summaries[key]["earned_today"] = round(est.earned, 2)
                summaries[key]["est_rate"] = round(est.rate, 2)
                summaries[key]["unmeasured_min"] = round(est.stale_s / 60.0, 1)
                if (self.master.on and self.switches[key].on
                        and not self._floor_ok):
                    summaries[key]["mode"] = "waiting for the floor"
            except ApiError as e:
                self._note(f"{key}: {e}")
                summaries[key] = {"name": fam.cfg.name, "error": str(e)[:120]}
        self._stage("first save", 98)
        st = self._state(now, summaries)
        self.last_state = st
        self.freeze_payload()
        self.store.save_local(st)
        self.store.maybe_save_remote(st)
        if not self._first_cycle_done:
            self._first_cycle_done = True
            self.boot_stage = {"stage": "running", "pct": 100,
                               "ts": round(time.time(), 1)}
        return st

    def run(self) -> int:
        from .web import WebServer
        web = WebServer(self)
        web.start()
        if self.stream is not None:
            self.stream.start()
        threading.Thread(target=self._sampler_loop, daemon=True,
                         name="sampler").start()
        self._note(f"serving on :{web.port}")
        backoff = 5.0
        while True:
            t0 = time.time()
            try:
                self.cycle()
                backoff = 5.0
            except Exception as e:  # noqa: BLE001 — the loop survives anything
                self._note(f"cycle failed: {type(e).__name__}: {e}")
                time.sleep(backoff)
                backoff = min(backoff * 2, ERROR_BACKOFF_CAP_S)
            # The sleep between cycles is broken into nurse ticks
            # (owner, 2026-08-25): freshly placed orders are watched
            # every few seconds for jumpers and rushing touches, on
            # THIS thread, so no cancel can race the cycle. With no
            # young orders to watch, nurse() returns immediately and
            # this is an ordinary sleep.
            rem = max(POLL_S - (time.time() - t0), 5.0)
            end_t = time.time() + rem
            while True:
                left = end_t - time.time()
                if left <= 0:
                    break
                time.sleep(min(NURSE_TICK_S, left))
                try:
                    for fam in self.families.values():
                        fam.nurse(time.time(), self.client)
                except Exception as e:  # noqa: BLE001 — never kill the loop
                    self._note(f"nurse: {type(e).__name__}: {e}")


def main() -> int:
    m = Monitor()
    if "--once" in sys.argv:
        st = m.cycle()
        import json
        print(json.dumps({k: v for k, v in st.items()
                          if k in ("summaries", "errors", "build")}, indent=1)[:4000])
        return 0
    return m.run()


if __name__ == "__main__":
    sys.exit(main())
