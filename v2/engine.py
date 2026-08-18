"""Probe -> earn -> sell: the heart of 2.0.

Built to the owner's brief (REBUILD.md), on the two seats families
first, under one risk number, with every 1.0 lesson encoded:

* **One risk number.** The buying power allocated to 2.0 ($100 for the
  seats test). `used` = capital at risk of our resting opening orders
  plus what our inventory cost; every placement must fit in the
  headroom. No per-market caps, ladders or graduated budgets.
* **Confidence decides where, the ceiling decides how much — never
  both.** Confidence comes from agreement: the fair band is the ENVELOPE
  of the Silver model's rung value and the market's own mid. Where they
  agree tightly we size normally near the touch; where they disagree we
  send a 1-share scout — gathering evidence is the point, and the
  narrow-tailed independence model must never talk us into shorting a
  tail the market prices fat (correlated polling error is real).
* **Both sides considered**, queue-aware, on the generous level reading
  of the window rule (owner's call) — and every placement where the two
  readings disagree registers both predictions for EXP-1, small ones
  included, pooled for grading.
* **Fills are found from position deltas**, not from orders vanishing:
  the exchange silently cancels resting orders, so disappearance is
  never treated as a fill. A vanished order with no position change is
  recorded as a silent cancel (and counted — if the exchange's
  buying-power auto-cancel is what 1.0 kept seeing, this is where it
  shows up).
* **The seller always works.** Anything long is rested as a SELL_LONG
  ask at max(break-even + tick, the ask touch) so it earns while it
  waits; shorts are bought back below entry. Selling runs even when
  probing/earning has nothing to do.
* **Absolute-zero exit**: a market whose program closed or whose pool
  went to zero gets our orders pulled — arithmetic, not judgement.
  (Board-relative fade rules come with multi-family expansion; on two
  families inside one board there is no "board" to compare against.)
* Markets resolving today are excluded and flagged.

Everything money-touching goes through OrderDesk (the rails). With the
master switch OFF the engine only reconciles — it never places, moves
or cancels anything.
"""

from __future__ import annotations

import datetime as dt
import time
from dataclasses import dataclass, field

from .books import BookCache
from .intents import BUY_LONG, SELL_LONG, SELL_SHORT, capital_at_risk
from .orders import OrderDesk
from .programs import daily_side_pool, slug_event_date
from .scoring import estimate_join
from .silver import SilverFairs
from .terms import TermsStore

BOOK_MAX_AGE = 120.0


@dataclass
class EngineConfig:
    whitelist_prefixes: tuple[str, ...] = ("scc-senate-gop-2026-11-03-",
                                           "scc-hrep-rep-2026-11-03-")
    ceiling_usd: float = 100.0       # the one risk number (owner: $100 seats test)
    max_actions_per_cycle: int = 4   # rate-limit manners; the book moves slowly
    max_order_usd: float = 12.0      # one order's nominal cost, high confidence
    scout_qty: float = 1.0           # low-confidence probe size
    min_est_day: float = 0.02        # don't rest for less than 2c/day
    tight_band: float = 0.06         # model & market within this = high confidence
    fair_margin: float = 0.01        # one cent beyond the band is still "at fair"
    action_cooldown_s: float = 300.0 # per market+side: no churn, queue position is capital
    exp1_keep: int = 500
    log_keep: int = 300


@dataclass
class OwnOrder:
    id: str
    market: str
    side: str        # book side: BUY bid / SELL ask
    price: float
    qty: float
    intent: str
    placed_ts: float
    purpose: str     # earn / scout / sell / close


@dataclass
class Summary:
    mode: str
    used: float = 0.0
    headroom: float = 0.0
    actions: list = field(default_factory=list)


class Engine:
    def __init__(self, desk: OrderDesk, config: EngineConfig | None = None,
                 alert=None, clock=None):
        self.desk = desk
        self.cfg = config or EngineConfig()
        self.alert = alert or (lambda title, msg: None)
        self._clock = clock or time.time
        self.orders: dict[str, OwnOrder] = {}      # our resting orders by id
        self.inventory: dict[str, dict] = {}       # slug -> {qty, cost} (net of side)
        self.positions_seen: dict[str, float] = {} # last cycle's net per market
        self.silent_cancels = 0
        self.exp1: list[dict] = []
        self.log: list[dict] = []
        self.last_action: dict[str, float] = {}    # "slug|side" -> ts

    # ---------------------------------------------------------------- helpers

    def whitelisted(self, slug: str) -> bool:
        return slug.startswith(self.cfg.whitelist_prefixes)

    def _log(self, **row) -> None:
        row.setdefault("ts", round(self._clock(), 1))
        self.log.append(row)
        del self.log[:-self.cfg.log_keep]

    def used_capital(self) -> float:
        used = sum(capital_at_risk(o.intent, o.price, o.qty)
                   for o in self.orders.values())
        for inv in self.inventory.values():
            used += max(inv.get("cost", 0.0), 0.0)
        return round(used, 2)

    def _cooldown_ok(self, slug: str, side: str, now: float) -> bool:
        return now - self.last_action.get(f"{slug}|{side}", 0.0) >= self.cfg.action_cooldown_s

    def _mark_action(self, slug: str, side: str, now: float) -> None:
        self.last_action[f"{slug}|{side}"] = now

    # ------------------------------------------------------------- fair bands

    def band(self, slug: str, book, silver: SilverFairs):
        """(lo, hi, source): the envelope of the model's rung value and the
        market's own mid. Tight envelope = the two agree = confidence."""
        model = silver.fair(slug)
        mid = None
        if book and book.bids and book.asks:
            mid = (book.bids[0][0] + book.asks[0][0]) / 2
        vals = [v for v in (model, mid) if v is not None]
        if not vals:
            return None
        lo, hi = min(vals), max(vals)
        if len(vals) == 1:           # one voice is never confident
            lo, hi = max(lo - 0.10, 0.001), min(hi + 0.10, 0.999)
        src = ("model+market" if model is not None and mid is not None
               else "model" if model is not None else "market")
        return lo, hi, src

    # -------------------------------------------------------------- reconcile

    def reconcile(self, open_orders: list[dict], positions: dict[str, tuple],
                  now: float) -> None:
        """Adopt reality: which of our orders still rest, what filled.
        Fills come from position deltas — never from mere disappearance."""
        open_by_id = {o["id"]: o for o in open_orders}
        # unexplained position change per market, consumed as fills are matched
        deltas = {m: (positions.get(m) or (0.0, 0.0))[0]
                  - self.positions_seen.get(m, 0.0)
                  for m in set(positions) | set(self.positions_seen)}
        for oid, rec in list(self.orders.items()):
            live = open_by_id.get(oid)
            if live is not None:
                if live["size"] < rec.qty - 1e-9:   # partial fill trims leaves
                    rec.qty = live["size"]
                continue
            # vanished: filled, cancelled by us earlier, or silently removed
            delta = deltas.get(rec.market, 0.0)
            expected = rec.qty if rec.intent in (BUY_LONG, SELL_SHORT) else -rec.qty
            if abs(delta) > 1e-9 and (delta > 0) == (expected > 0):
                filled = min(abs(delta), rec.qty)
                deltas[rec.market] = delta - (filled if delta > 0 else -filled)
                self._on_fill(rec, filled, now)
            else:
                self.silent_cancels += 1
                self._log(event="silent_cancel", market=rec.market, side=rec.side,
                          price=rec.price, qty=rec.qty, id=oid)
            del self.orders[oid]
        self.positions_seen = {m: v[0] for m, v in positions.items()}
        # inventory follows the exchange's own numbers for our markets
        for slug, (net, cost) in positions.items():
            if self.whitelisted(slug):
                self.inventory[slug] = {"qty": net, "cost": cost}
        for slug in list(self.inventory):
            if slug not in positions:
                del self.inventory[slug]

    def _on_fill(self, rec: OwnOrder, qty: float, now: float) -> None:
        self._log(event="fill", market=rec.market, side=rec.side,
                  price=rec.price, qty=qty, purpose=rec.purpose)
        self.alert("Order filled",
                   f"{rec.market} {rec.side} {qty:g} @ {rec.price * 100:g}c "
                   f"({rec.purpose})")

    # ----------------------------------------------------------------- decide

    def _ends_today(self, slug: str, now: float) -> bool:
        d = slug_event_date(slug)
        return d is not None and d <= dt.datetime.fromtimestamp(
            now, tz=dt.timezone.utc).date()

    def _candidates(self, slug: str, book, prog, band, now: float) -> list[dict]:
        """Scored placement candidates for one market, both sides."""
        lo, hi, src = band
        tight = (hi - lo) <= self.cfg.tight_band
        side_pool = daily_side_pool(prog, slug)
        out = []
        for side in ("BUY", "SELL"):
            levels = book.side(side)
            if not levels:
                continue
            best = levels[0][0]
            # price candidates: join the touch, improve it by a tick
            cands = [best]
            imp = best + book.tick if side == "BUY" else best - book.tick
            other = book.side("SELL" if side == "BUY" else "BUY")
            crosses = other and (imp >= other[0][0] - 1e-9 if side == "BUY"
                                 else imp <= other[0][0] + 1e-9)
            if 0.001 <= imp <= 0.999 and not crosses:
                cands.append(imp)
            for px in cands:
                # fair guards: never bid above the band, never ask below it
                if side == "BUY" and px > hi + self.cfg.fair_margin:
                    continue
                if side == "SELL" and px < lo - self.cfg.fair_margin:
                    continue
                cost_ps = px if side == "BUY" else 1.0 - px
                usd = self.cfg.max_order_usd if tight else self.cfg.scout_qty * cost_ps
                qty = max(round(usd / cost_ps, 2), self.cfg.scout_qty)
                j = estimate_join(side, list(levels), book.tick, prog.df,
                                  prog.target, px, qty)
                if not (j.qualifies and j.in_window):
                    continue
                est = j.share * side_pool
                if est < self.cfg.min_est_day:
                    continue
                cost = cost_ps * qty
                out.append({"market": slug, "side": side, "price": px, "qty": qty,
                            "est_day": est, "cost": cost, "yield": est / cost,
                            "purpose": "earn" if tight else "scout",
                            "exp1_gap": j.in_window and not j.in_window_queue,
                            "pred_level": est,
                            "pred_queue": j.share_if_queue * side_pool,
                            "band": (round(lo, 3), round(hi, 3), src)})
        return out

    # ------------------------------------------------------------------- act

    def cycle(self, now: float, open_orders: list[dict],
              positions: dict[str, tuple], books: BookCache, terms: TermsStore,
              silver: SilverFairs, switch_on: bool) -> dict:
        self.reconcile(open_orders, positions, now)

        s = Summary(mode="on" if switch_on else "observing")
        s.used = self.used_capital()
        s.headroom = round(self.cfg.ceiling_usd - s.used, 2)
        if not switch_on:
            return self._summary(s)

        actions_left = self.cfg.max_actions_per_cycle

        # 1) absolute-zero exit + resolution day: pull our orders out
        for rec in list(self.orders.values()):
            prog = terms.get(rec.market)
            dead = prog is None or not prog.is_live() or not prog.pool
            if dead or self._ends_today(rec.market, now):
                if actions_left <= 0:
                    break
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    why = "resolves today" if not dead else "program pays nothing"
                    self._log(event="exit", market=rec.market, why=why, id=rec.id)
                    del self.orders[rec.id]
                    actions_left -= 1

        # 2) maintenance: an order out of the window or outside its band moves
        for rec in list(self.orders.values()):
            if actions_left <= 0:
                break
            if rec.purpose in ("sell", "close"):
                continue
            book = books.fresh(rec.market, BOOK_MAX_AGE, now)
            prog = terms.get(rec.market)
            if book is None or prog is None or not self._cooldown_ok(
                    rec.market, rec.side, now):
                continue
            b = self.band(rec.market, book, silver)
            if b is None:
                continue
            cands = [c for c in self._candidates(rec.market, book, prog, b, now)
                     if c["side"] == rec.side]
            here = estimate_join(rec.side, list(book.side(rec.side)), book.tick,
                                 prog.df, prog.target, rec.price, 0.01)
            earning_here = here.qualifies and here.in_window
            best = max(cands, key=lambda c: c["yield"], default=None)
            lo, hi, _src = b
            guard_broken = (rec.price > hi + self.cfg.fair_margin
                            if rec.side == "BUY"
                            else rec.price < lo - self.cfg.fair_margin)
            if guard_broken:
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    self._log(event="pull", market=rec.market, side=rec.side,
                              why="fair band moved", price=rec.price)
                    del self.orders[rec.id]
                    self._mark_action(rec.market, rec.side, now)
                    actions_left -= 1
                continue
            if not earning_here and best is not None and abs(
                    best["price"] - rec.price) > 1e-9:
                r = self.desk.reprice(
                    {"id": rec.id, "market": rec.market, "side": rec.side,
                     "price": rec.price, "size": rec.qty, "intent": rec.intent},
                    best["price"])
                if r.ok:
                    if r.two_orders:
                        self.alert("Two orders resting",
                                   f"{rec.market} {rec.side}: replacement "
                                   f"{r.order_id} rests, original didn't cancel")
                    del self.orders[rec.id]
                    self.orders[r.order_id] = OwnOrder(
                        id=r.order_id, market=rec.market, side=rec.side,
                        price=best["price"], qty=rec.qty, intent=rec.intent,
                        placed_ts=now, purpose=rec.purpose)
                    self._register_exp1(best, now)
                    self._log(event="reprice", market=rec.market, side=rec.side,
                              frm=rec.price, to=best["price"])
                    self._mark_action(rec.market, rec.side, now)
                    actions_left -= 1

        # 3) the seller: longs rest as asks at max(break-even + tick, the touch)
        for slug, inv in self.inventory.items():
            if actions_left <= 0:
                break
            qty = inv.get("qty") or 0.0
            book = books.fresh(slug, BOOK_MAX_AGE, now)
            if book is None or abs(qty) < 1.0:
                continue
            covered = sum(o.qty for o in self.orders.values()
                          if o.market == slug and o.purpose in ("sell", "close"))
            if qty > 0:
                rest = qty - covered
                if rest < 1.0 or not self._cooldown_ok(slug, "SELL", now):
                    continue
                break_even = min(max(inv.get("cost", 0.0) / qty, 0.001), 0.989)
                ask_touch = book.asks[0][0] if book.asks else break_even + book.tick
                px = round(max(break_even + book.tick, ask_touch), 3)
                r = self.desk.place_resting(slug, "SELL", px, rest,
                                            net_position=qty, intent=SELL_LONG)
                if r.ok:
                    self.orders[r.order_id] = OwnOrder(
                        id=r.order_id, market=slug, side="SELL", price=px,
                        qty=rest, intent=SELL_LONG, placed_ts=now, purpose="sell")
                    self._log(event="sell_listed", market=slug, price=px, qty=rest)
                    self._mark_action(slug, "SELL", now)
                    actions_left -= 1
            elif qty < 0:
                rest = -qty - covered
                if rest < 1.0 or not self._cooldown_ok(slug, "BUY", now):
                    continue
                # cost semantics for a short position are a best guess until
                # the read-only run confirms the payload; scouts are 1 share,
                # so a wrong guess costs a tick, not a book
                entry = min(max(1.0 - abs(inv.get("cost", 0.0) / qty), 0.011), 0.999)
                bid_touch = book.bids[0][0] if book.bids else entry - book.tick
                px = round(min(entry - book.tick, bid_touch), 3)
                if px < 0.001:
                    continue
                r = self.desk.place_resting(slug, "BUY", px, rest,
                                            net_position=qty, close_short=True,
                                            intent=SELL_SHORT)
                if r.ok:
                    self.orders[r.order_id] = OwnOrder(
                        id=r.order_id, market=slug, side="BUY", price=px,
                        qty=rest, intent=SELL_SHORT, placed_ts=now, purpose="close")
                    self._log(event="short_close_listed", market=slug,
                              price=px, qty=rest)
                    self._mark_action(slug, "BUY", now)
                    actions_left -= 1

        # 4) new placements: rank everything by income per dollar at risk
        cands: list[dict] = []
        for slug in terms.current:
            if not self.whitelisted(slug) or self._ends_today(slug, now):
                continue
            prog = terms.get(slug)
            if prog is None or not prog.is_live() or not prog.pool:
                continue
            book = books.fresh(slug, BOOK_MAX_AGE, now)
            if book is None:
                continue
            b = self.band(slug, book, silver)
            if b is None:
                continue
            have = {(o.market, o.side) for o in self.orders.values()}
            for c in self._candidates(slug, book, prog, b, now):
                if (slug, c["side"]) in have:
                    continue          # maintenance owns existing spots
                if not self._cooldown_ok(slug, c["side"], now):
                    continue
                cands.append(c)
        cands.sort(key=lambda c: -c["yield"])
        placed_keys: set[tuple[str, str]] = set()
        for c in cands:
            if actions_left <= 0:
                break
            if (c["market"], c["side"]) in placed_keys:
                continue              # one order per side per market per cycle
            headroom = self.cfg.ceiling_usd - self.used_capital()
            if c["cost"] > headroom:
                continue              # the ceiling decides how much — always
            net = (self.inventory.get(c["market"]) or {}).get("qty", 0.0)
            r = self.desk.place_resting(c["market"], c["side"], c["price"],
                                        c["qty"], net_position=net)
            if r.ok:
                self.orders[r.order_id] = OwnOrder(
                    id=r.order_id, market=c["market"], side=c["side"],
                    price=c["price"], qty=c["qty"], intent=r.intent,
                    placed_ts=now, purpose=c["purpose"])
                self._register_exp1(c, now)
                self._log(event="place", **{k: c[k] for k in
                          ("market", "side", "price", "qty", "est_day", "purpose")})
                s.actions.append(f"{c['purpose']} {c['market']} {c['side']} "
                                 f"{c['qty']:g} @ {c['price'] * 100:g}c")
                self._mark_action(c["market"], c["side"], now)
                placed_keys.add((c["market"], c["side"]))
                actions_left -= 1
            else:
                self._log(event="refused", market=c["market"], side=c["side"],
                          note=r.note)

        s.used = self.used_capital()
        s.headroom = round(self.cfg.ceiling_usd - s.used, 2)
        return self._summary(s)

    def _register_exp1(self, c: dict, now: float) -> None:
        """EXP-1: a placement where the level and queue readings disagree is
        automatically an experiment — both predictions recorded, small ones
        included (they pool)."""
        if not c.get("exp1_gap"):
            return
        self.exp1.append({
            "ts": round(now, 1), "market": c["market"], "side": c["side"],
            "price": c["price"], "qty": c["qty"],
            "pred_level_day": round(c["pred_level"], 4),
            "pred_queue_day": round(c["pred_queue"], 4),
        })
        del self.exp1[:-self.cfg.exp1_keep]

    def _summary(self, s: Summary) -> dict:
        return {
            "mode": s.mode, "used": s.used, "headroom": s.headroom,
            "ceiling": self.cfg.ceiling_usd,
            "orders": [{"id": o.id, "market": o.market, "side": o.side,
                        "price": o.price, "qty": o.qty, "purpose": o.purpose}
                       for o in self.orders.values()],
            "inventory": self.inventory,
            "silent_cancels": self.silent_cancels,
            "exp1_open": len(self.exp1),
            "actions": s.actions,
        }

    # ------------------------------------------------------------ persistence

    def to_dict(self) -> dict:
        return {
            "orders": {oid: vars(o) for oid, o in self.orders.items()},
            "inventory": self.inventory,
            "positions_seen": self.positions_seen,
            "silent_cancels": self.silent_cancels,
            "exp1": self.exp1, "log": self.log[-self.cfg.log_keep:],
            "last_action": self.last_action,
        }

    def restore(self, d: dict) -> None:
        for oid, v in (d.get("orders") or {}).items():
            self.orders[oid] = OwnOrder(**v)
        self.inventory = dict(d.get("inventory") or {})
        self.positions_seen = dict(d.get("positions_seen") or {})
        self.silent_cancels = d.get("silent_cancels") or 0
        self.exp1 = list(d.get("exp1") or [])
        self.log = list(d.get("log") or [])
        self.last_action = dict(d.get("last_action") or {})
