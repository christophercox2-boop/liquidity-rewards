"""Reward families beyond the seats: one engine, one config per family.

Born as the college-football module (owner, 2026-08-20: "Just make college
football for now") and generalized the same day when the owner approved NFL
futures with one correction: "I thought the idea was to place them behind
the touch because of the df... going forward with the new families you can
model that way." That correction is the `allow_improve` knob — college keeps
its original behavior (in wall-only books it may step in FRONT of the
qualifier wall, which is why some of its orders rest alone); every family
built after it sets allow_improve=False and only ever joins the touch or
rests behind it, so a side with no real competition is simply skipped.

Everything else is shared and per-family separate by construction: each
family gets its own MasterSwitch (off by default), its own OrderDesk
whitelisted to exactly its slug prefixes, its own BookCache and TermsStore,
its own $1/market budget and 5-10% share courtesy band, and its own weekly
resting window (game days belong to others). Resting orders do not consume
buying power (owner: "$1 per market, regardless of how many I'm in, ties up
exactly $1") — collateral numbers are the worst case if everything fills,
and the exchange's funding check self-cancels beyond what is funded.

Placement, per side of each market: only sides already holding Target Size
are entered (a fractional order can't qualify a side, and topping one up
gifts the pool to whoever quotes closer). The price ladder steps back from
the touch; size is the largest on a small grid keeping our share of the
side's score at or under share_hi within the per-market budget. Fills are
found from position deltas, never from disappearance; every fill pings the
phone and the exit seller re-offers at break-even or better. All
money-touching calls go through the desk rails: post-only, price bounds,
verify-by-id.
"""

from __future__ import annotations

import datetime as dt
import time
from dataclasses import dataclass, field
from zoneinfo import ZoneInfo

from .books import BookCache
from .intents import BUY_LONG, SELL_LONG, capital_at_risk
from .orders import OrderDesk
from .scoring import estimate_join
from .terms import TermsStore

ET = ZoneInfo("America/New_York")

PREFIX = "aachc-cfb-wins-"
BOOK_MAX_AGE = 120.0

# size grid the planner walks (contracts); fractional sizes are live rails
# (QTY_MIN = 0.01) and the whole point of a $1 market cap
QTY_GRID = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0)


@dataclass
class FamilyConfig:
    name: str = "College football"   # page label
    tag: str = "CFB"                 # alert prefix
    prefixes: tuple[str, ...] = (PREFIX,)
    # the weekly resting window, ET: resting allowed from rest_from until
    # rest_until (exclusive); the rest of the week the family is out and
    # only exit orders stay. (weekday, hour), Monday = 0.
    rest_from: tuple[int, int] = (6, 6)     # Sunday 06:00
    rest_until: tuple[int, int] = (3, 17)   # Thursday 17:00
    # the weekly window only means anything once the season is playing —
    # before this ET date every day is a resting day (owner, 2026-08-20:
    # "there aren't any games until next week")
    season_start: tuple[int, int, int] | None = None
    # may the planner price IN FRONT of the side's current touch? College
    # launched with this on (it is why some of its orders rest alone, in
    # front of a junk wall); the owner's 2026-08-20 correction makes every
    # newer family behind-the-touch only.
    allow_improve: bool = True
    per_market_usd: float = 1.00     # owner's cap, both sides combined
    share_hi: float = 0.10           # the not-drawing-attention ceiling
    # owner, 2026-08-20: "There should be no market limit." None = every
    # paying market the planner finds worth resting in; the real bounds are
    # the $1/market cap, the share band, and the placement/scan pacing.
    max_markets: int | None = None
    # Ramp speed (owner, 2026-08-20: "What can be done to let the cfb bot
    # go faster?"): six placements and ten book fetches a cycle, four of
    # them reserved for discovering new markets. The big saving that pays
    # for this is verify_resting=False below — the old per-placement
    # verification polled the account's open orders (3,300+ rows) up to
    # four times per order, which is where the HTTP 429s came from.
    max_actions_per_cycle: int = 6
    books_per_cycle: int = 10        # REST fetches: active first, then the scan
    scan_reserve: int = 4            # fetches the scan always keeps
    # New placements trust the exchange's accepted-response and skip the
    # verify poll; the NEXT cycle's reconcile checks every order by id
    # anyway, and a post-only rejection simply vanishes there as a silent
    # cancel and is retried later. Reprices keep full place-verify-cancel.
    verify_resting: bool = False
    rescan_s: float = 4 * 3600.0     # re-score an idle candidate this often
    # Live tuning, 2026-08-20 early hours: the first cfb deploy repriced a
    # dozen orders per pass chasing 1-tick touch wobbles for +$0.02/day
    # gains, and the box started catching HTTP 429s — each reprice is a
    # place-verify-cancel of several API calls. A move now has to be worth
    # ~30% of a typical order's est before it clears the bar, and each
    # market-side moves at most hourly.
    cooldown_s: float = 3600.0       # per market-side between our own moves
    min_est_day: float = 0.02        # don't rest for under 2c/day
    reprice_gain_day: float = 0.06   # a move must clear real churn
    drift_share: float = 0.15        # live share above this = too visible, replan
    min_days_out: int = 3            # nothing resolving this week
    terms_every_s: float = 600.0     # live terms refresh for active markets
    log_keep: int = 300


@dataclass
class FamilyOrder:
    id: str
    market: str
    side: str            # book side: BUY bid / SELL ask
    price: float
    qty: float
    intent: str
    placed_ts: float
    purpose: str         # earn / solo / sell
    est_day: float = 0.0
    share: float = 0.0
    live_est: float | None = None
    live_share: float | None = None


def resting_ok(now: float, cfg: FamilyConfig) -> bool:
    """Inside the family's weekly resting window? Game days belong to
    others (owner). The window runs rest_from -> rest_until in ET and may
    wrap the week boundary; before season_start there are no game days
    and every hour is a resting hour."""
    t = dt.datetime.fromtimestamp(now, ET)
    if cfg.season_start is not None and t.date() < dt.date(*cfg.season_start):
        return True
    m = t.weekday() * 24 + t.hour                    # hour-of-week, Mon 0
    a = cfg.rest_from[0] * 24 + cfg.rest_from[1]
    b = cfg.rest_until[0] * 24 + cfg.rest_until[1]
    if a <= b:
        return a <= m < b
    return m >= a or m < b


def slug_days_out(slug: str, now: float) -> int | None:
    parts = (slug or "").split("-")
    for i in range(len(parts) - 2):
        if (parts[i].isdigit() and len(parts[i]) == 4
                and parts[i + 1].isdigit() and parts[i + 2].isdigit()):
            try:
                when = dt.date(int(parts[i]), int(parts[i + 1]), int(parts[i + 2][:2]))
            except ValueError:
                return None
            return (when - dt.datetime.fromtimestamp(now, ET).date()).days
    return None


class Family:
    def __init__(self, desk: OrderDesk, cache: BookCache,
                 config: FamilyConfig | None = None, alert=None, clock=None):
        self.desk = desk
        self.cache = cache
        self.cfg = config or FamilyConfig()
        self.alert = alert or (lambda title, msg: None)
        self._clock = clock or time.time
        self.terms = TermsStore()
        self.orders: dict[str, FamilyOrder] = {}
        self.inventory: dict[str, dict] = {}      # slug -> {qty, cost}
        self.positions_seen: dict[str, float] = {}
        self.scoreboard: dict[str, dict] = {}     # slug -> {ts, est, plans}
        self.last_action: dict[str, float] = {}   # "slug|side" -> ts
        self.last_terms = 0.0
        self.silent_cancels = 0
        self.log: list[dict] = []

    # ------------------------------------------------------------- helpers

    def _log(self, **row) -> None:
        row.setdefault("ts", round(self._clock(), 1))
        self.log.append(row)
        del self.log[:-self.cfg.log_keep]

    def _cooldown_ok(self, slug: str, side: str, now: float) -> bool:
        return now - self.last_action.get(f"{slug}|{side}", 0.0) >= self.cfg.cooldown_s

    def _mark(self, slug: str, side: str, now: float) -> None:
        self.last_action[f"{slug}|{side}"] = now

    def market_spent(self, slug: str, skip_id: str | None = None) -> float:
        """Collateral this market already holds across our resting orders."""
        return sum(capital_at_risk(o.intent, o.price, o.qty)
                   for o in self.orders.values()
                   if o.market == slug and o.id != skip_id
                   and o.purpose != "sell")

    def active_markets(self) -> set[str]:
        return {o.market for o in self.orders.values() if o.purpose != "sell"}

    def engaged(self) -> bool:
        return bool(self.orders or self.inventory)

    # ------------------------------------------------------------ catalogue

    def catalogue(self, survey_terms: dict) -> dict[str, dict]:
        """The family's paying markets, from the survey's whole-exchange
        terms sweep — {slug: {pool,target,df,event_n,side_pool}}. The survey
        already refreshes these on its own cadence; this module never
        re-fetches the catalogue."""
        out = {}
        for slug, row in (survey_terms or {}).items():
            if not slug.startswith(self.cfg.prefixes) or not isinstance(row, dict):
                continue
            if not row.get("pool") or not row.get("target"):
                continue
            out[slug] = row
        return out

    # ------------------------------------------------------------- planning

    def _plan_side(self, book, side: str, df: float, target: float,
                   side_pool: float, budget: float,
                   own: FamilyOrder | None = None) -> dict | None:
        """The best resting order for one side of one book, or None.

        Walks a small price ladder back from the touch and, per price, the
        size grid; keeps share at or under share_hi against real
        competition, falls back to a minimum-size solo probe when the
        window is effectively empty. `own` excludes our current order from
        the book before scoring (the fetched book contains it)."""
        levels = list(book.side(side))
        if own is not None:
            levels = [(p, q - own.qty if abs(p - own.price) < 1e-9 else q)
                      for p, q in levels]
            levels = [(p, q) for p, q in levels if q > 1e-9]
        if sum(q for _, q in levels) < target:
            return None      # the side can't qualify; topping it up gifts others
        tick = book.tick
        sign = 1.0 if side == "BUY" else -1.0
        touch = levels[0][0]
        other = book.side("SELL" if side == "BUY" else "BUY")
        # stepping back from the touch is always allowed; stepping IN FRONT
        # of it is only for books whose touch is a junk wall far from any
        # opposing quote — df 0.5 means a wall one tick behind still scores
        # half, so share only appears several ticks in front of it. The
        # improve rungs stay 5 ticks clear of the other side's touch; with
        # no opposing quote at all there is no value anchor, so the rungs
        # stay short and the size is clamped to probe money.
        if not self.cfg.allow_improve:
            cap_improve, improve = touch, ()
        elif other:
            cap_improve = other[0][0] - sign * 5 * tick
            improve = (1, 5, 10, 15, 20)
        else:
            cap_improve = touch + sign * 10 * tick
            improve = (1, 5, 10)
            budget = min(budget, 0.05)
        cands = []
        for k in (0, 1, 2, 3, 6, 10, 15):
            px = round(touch - k * sign * tick, 3)
            if not (0.001 <= px <= 0.999):
                continue
            if other and (px >= other[0][0] - 1e-9 if side == "BUY"
                          else px <= other[0][0] + 1e-9):
                continue
            if px not in cands:
                cands.append(px)
        for k in improve:
            px = round(touch + k * sign * tick, 3)
            if not (0.001 <= px <= 0.999):
                continue
            if (px - cap_improve) * sign > 1e-9:
                continue
            if other and (px >= other[0][0] - 1e-9 if side == "BUY"
                          else px <= other[0][0] + 1e-9):
                continue
            if px not in cands:
                cands.append(px)
        polite, solo = None, None
        for px in cands:
            cost_ps = px if side == "BUY" else 1.0 - px
            for qty in QTY_GRID:
                if qty * cost_ps > budget + 1e-9:
                    break
                j = estimate_join(side, levels, tick, df, target, px, qty)
                if not (j.qualifies and j.in_window):
                    break    # bigger sizes at this price won't come back in
                est = j.share * side_pool
                row = {"side": side, "px": px, "qty": qty,
                       "share": round(j.share, 4), "est": round(est, 4),
                       "cost": round(qty * cost_ps, 2)}
                if j.share <= self.cfg.share_hi:
                    if polite is None or est > polite["est"] + 1e-9:
                        polite = row
                elif qty == QTY_GRID[0]:
                    # even the minimum size dominates the window — a solo
                    # probe; prefer the DEEPEST price that still earns
                    if solo is None or (est > 0 and px * sign < solo["px"] * sign):
                        solo = {**row, "solo": True}
                    break    # larger sizes are just more visible
                else:
                    break
        pick = polite if polite and polite["est"] >= self.cfg.min_est_day else None
        if pick is None and solo is not None and solo["est"] >= self.cfg.min_est_day:
            pick = solo
        return pick

    def plan_market(self, book, row: dict) -> list[dict]:
        """Both sides' best entries for one market, within the $1 cap."""
        df, target = float(row["df"]), float(row["target"])
        side_pool = float(row.get("side_pool")
                          or row["pool"] / max(row.get("event_n") or 1, 1) / 2.0)
        out = []
        budget = self.cfg.per_market_usd / 2.0
        for side in ("BUY", "SELL"):
            p = self._plan_side(book, side, df, target, side_pool, budget)
            if p:
                out.append(p)
        return out

    # -------------------------------------------------------------- reconcile

    def reconcile(self, open_orders: list[dict], positions: dict, now: float) -> None:
        """Adopt reality — fills come from position deltas, never from mere
        disappearance (the exchange silently cancels)."""
        open_by_id = {o["id"]: o for o in open_orders}
        deltas = {m: (positions.get(m) or (0.0, 0.0))[0]
                  - self.positions_seen.get(m, 0.0)
                  for m in set(positions) | set(self.positions_seen)
                  if m.startswith(self.cfg.prefixes)}
        for oid, rec in list(self.orders.items()):
            live = open_by_id.get(oid)
            if live is not None:
                if live["size"] < rec.qty - 1e-9:
                    filled = rec.qty - live["size"]
                    d = deltas.get(rec.market, 0.0)
                    deltas[rec.market] = d - (filled if rec.intent == BUY_LONG
                                              else -filled)
                    self._on_fill(rec, filled, now)
                    rec.qty = live["size"]
                continue
            delta = deltas.get(rec.market, 0.0)
            expected = rec.qty if rec.intent == BUY_LONG else -rec.qty
            if abs(delta) > 1e-9 and (delta > 0) == (expected > 0):
                filled = min(abs(delta), rec.qty)
                deltas[rec.market] = delta - (filled if delta > 0 else -filled)
                self._on_fill(rec, filled, now)
            else:
                self.silent_cancels += 1
                self._log(event="silent_cancel", market=rec.market,
                          side=rec.side, price=rec.price, qty=rec.qty, id=oid)
            del self.orders[oid]
        for m, v in positions.items():
            if m.startswith(self.cfg.prefixes):
                self.positions_seen[m] = v[0]

    def _on_fill(self, rec: FamilyOrder, filled: float, now: float) -> None:
        inv = self.inventory.setdefault(rec.market, {"qty": 0.0, "cost": 0.0})
        if rec.side == "BUY":
            inv["qty"] += filled
            inv["cost"] += filled * rec.price
        else:
            inv["qty"] -= filled
            inv["cost"] -= filled * rec.price
        if abs(inv["qty"]) < 0.005:
            self.inventory.pop(rec.market, None)
        self._log(event="fill", market=rec.market, side=rec.side,
                  price=rec.price, qty=round(filled, 2))
        self.alert(f"{self.cfg.tag} fill",
                   f"{rec.market} {rec.side} {filled:g} @ {rec.price * 100:g}c — "
                   f"fills are rare here by design; the exit seller takes over")

    # ------------------------------------------------------------------ cycle

    def cycle(self, now: float, open_orders: list[dict], positions: dict,
              client, survey_terms: dict, switch_on: bool) -> dict:
        self.reconcile(open_orders, positions, now)
        cat = self.catalogue(survey_terms)
        summary = {"mode": "on" if switch_on else "observing",
                   "markets": len(cat), "active": len(self.active_markets()),
                   "resting_ok": resting_ok(now, self.cfg)}
        if not switch_on:
            return self._finish(summary)
        actions = self.cfg.max_actions_per_cycle

        # live terms for markets we're in AND the scan's next picks, so a
        # pool cut is known before the first order goes in, not after
        # (owner, 2026-08-20: no placing in markets without rewards)
        soon = [s for s, sb in sorted(self.scoreboard.items(),
                                      key=lambda kv: -(kv[1].get("est") or 0))[:20]
                if sb.get("plans")]
        active = sorted(self.active_markets() | set(self.inventory) | set(soon))
        if active and now - self.last_terms > self.cfg.terms_every_s:
            self.last_terms = now
            try:
                raw = client.programs(active)
                self.terms.refresh(raw, {s: cat.get(s, {}).get("event_n") or 1
                                         for s in active}, now=now)
            except Exception as e:  # noqa: BLE001 — keep serving aged terms
                self._log(event="terms_error", error=str(e)[:80])

        # game window: pull everything that isn't an exit, place nothing
        if not resting_ok(now, self.cfg):
            summary["mode"] = "game window"
            for rec in list(self.orders.values()):
                if actions <= 0:
                    break
                if rec.purpose == "sell":
                    continue
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    self._log(event="window_pull", market=rec.market,
                              side=rec.side, price=rec.price)
                    del self.orders[rec.id]
                    actions -= 1
            return self._finish(summary)

        # 1) dead-program / near-resolution exits
        for rec in list(self.orders.values()):
            if actions <= 0:
                break
            if rec.purpose == "sell":
                continue
            prog = self.terms.get(rec.market)
            days = slug_days_out(rec.market, now)
            dead = (prog is not None
                    and (not prog.is_live() or not prog.pool))
            gone = rec.market not in cat and prog is None
            near = days is not None and days < self.cfg.min_days_out
            if dead or gone or near:
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    why = ("resolves soon" if near else "program pays nothing")
                    self._log(event="exit", market=rec.market, why=why, id=rec.id)
                    del self.orders[rec.id]
                    actions -= 1

        # 2) maintenance: re-evaluate resting orders against fresh books
        refreshed = self._refresh_books(client, cat, now)
        for rec in list(self.orders.values()):
            book = self.cache.fresh(rec.market, BOOK_MAX_AGE * 4, now)
            row = cat.get(rec.market)
            if book is None or row is None:
                continue
            if rec.purpose == "sell":
                # exits wait for their price, and they EARN while they wait
                # (owner, 2026-08-20) — read it, never reprice it here
                lv = [(p, q - rec.qty if abs(p - rec.price) < 1e-9 else q)
                      for p, q in book.side(rec.side)]
                lv = [(p, q) for p, q in lv if q > 1e-9]
                j = estimate_join(rec.side, lv, book.tick, float(row["df"]),
                                  float(row["target"]), rec.price, rec.qty)
                sp = float(row.get("side_pool") or 0.0)
                rec.live_share = round(j.share, 4)
                rec.live_est = round(j.share * sp
                                     if j.qualifies and j.in_window else 0.0, 4)
                continue
            levels = [(p, q - rec.qty if abs(p - rec.price) < 1e-9 else q)
                      for p, q in book.side(rec.side)]
            levels = [(p, q) for p, q in levels if q > 1e-9]
            j = estimate_join(rec.side, levels, book.tick, float(row["df"]),
                              float(row["target"]), rec.price, rec.qty)
            side_pool = float(row.get("side_pool") or 0.0)
            rec.live_share = round(j.share, 4)
            rec.live_est = round(j.share * side_pool
                                 if j.qualifies and j.in_window else 0.0, 4)
            if actions <= 0 or not self._cooldown_ok(rec.market, rec.side, now):
                continue
            best = self._plan_side(book, rec.side, float(row["df"]),
                                   float(row["target"]), side_pool,
                                   self.cfg.per_market_usd / 2.0, own=rec)
            drifted = (rec.live_share or 0.0) > self.cfg.drift_share \
                and rec.purpose != "solo"
            gain = (best["est"] if best else 0.0) - (rec.live_est or 0.0)
            if best is None and (rec.live_est or 0.0) <= 0.0:
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    self._log(event="pull", market=rec.market, side=rec.side,
                              why="earning nothing and no better spot")
                    del self.orders[rec.id]
                    self._mark(rec.market, rec.side, now)
                    actions -= 1
            elif best is not None and (drifted or gain >= self.cfg.reprice_gain_day) \
                    and (abs(best["px"] - rec.price) > 1e-9
                         or abs(best["qty"] - rec.qty) > 1e-9):
                r = self.desk.reprice(
                    {"id": rec.id, "market": rec.market, "side": rec.side,
                     "price": rec.price, "size": rec.qty, "intent": rec.intent},
                    best["px"], new_qty=best["qty"])
                if r.ok:
                    self._log(event="reprice", market=rec.market, side=rec.side,
                              frm=rec.price, to=best["px"], qty=best["qty"])
                    del self.orders[rec.id]
                    self.orders[r.order_id] = FamilyOrder(
                        id=r.order_id, market=rec.market, side=rec.side,
                        price=best["px"], qty=best["qty"], intent=rec.intent,
                        placed_ts=now,
                        purpose="solo" if best.get("solo") else "earn",
                        est_day=best["est"], share=best["share"])
                    self._mark(rec.market, rec.side, now)
                    actions -= 1

        # 3) new entries, best scoreboard candidates first
        have = {(o.market, o.side) for o in self.orders.values()
                if o.purpose != "sell"}
        ranked = sorted(((s, sb) for s, sb in self.scoreboard.items()
                         if sb.get("plans")),
                        key=lambda kv: -sum(p["est"] for p in kv[1]["plans"]))
        for slug, sb in ranked:
            if actions <= 0:
                break
            if slug not in cat:
                continue
            days = slug_days_out(slug, now)
            if days is not None and days < self.cfg.min_days_out:
                continue
            prog = self.terms.get(slug)
            if prog is not None and (not prog.is_live() or not prog.pool):
                self.scoreboard.pop(slug, None)   # known dead: never place
                continue
            fresh_new = slug in self.active_markets()
            if (self.cfg.max_markets is not None and not fresh_new
                    and len(self.active_markets()) >= self.cfg.max_markets):
                continue
            for plan in sb["plans"]:
                if actions <= 0:
                    break
                if (slug, plan["side"]) in have:
                    continue
                if not self._cooldown_ok(slug, plan["side"], now):
                    continue
                spent = self.market_spent(slug)
                if spent + plan["cost"] > self.cfg.per_market_usd + 1e-9:
                    continue
                book = self.cache.fresh(slug, BOOK_MAX_AGE, now)
                if book is None:
                    continue
                net = (positions.get(slug) or (0.0,))[0]
                r = self.desk.place_resting(slug, plan["side"], plan["px"],
                                            plan["qty"], net_position=net,
                                            verify=self.cfg.verify_resting)
                if r.ok and r.order_id:
                    self.orders[r.order_id] = FamilyOrder(
                        id=r.order_id, market=slug, side=plan["side"],
                        price=plan["px"], qty=plan["qty"], intent=r.intent,
                        placed_ts=now,
                        purpose="solo" if plan.get("solo") else "earn",
                        est_day=plan["est"], share=plan["share"])
                    self._log(event="place", market=slug, side=plan["side"],
                              price=plan["px"], qty=plan["qty"],
                              est=plan["est"], share=plan["share"])
                    self._mark(slug, plan["side"], now)
                    actions -= 1
                else:
                    self._log(event="refused", market=slug, side=plan["side"],
                              note=r.note[:90])
                    self._mark(slug, plan["side"], now)

        # 4) the seller: filled longs rest as exits at break-even or better
        for slug, inv in list(self.inventory.items()):
            if actions <= 0:
                break
            qty = inv.get("qty") or 0.0
            if qty < 0.01:
                continue
            # not in a market that pays nothing — see the same guard in
            # engine.py, where a seller re-listing against the dead-program
            # pull looped for two hours on 2026-08-20
            prog_here = self.terms.get(slug)
            if slug not in cat or (prog_here is not None
                                   and (not prog_here.is_live()
                                        or not prog_here.pool)):
                continue
            covered = sum(o.qty for o in self.orders.values()
                          if o.market == slug and o.purpose == "sell")
            rest = qty - covered
            book = self.cache.fresh(slug, BOOK_MAX_AGE, now)
            if rest < 0.01 or book is None \
                    or not self._cooldown_ok(slug, "SELL", now):
                continue
            break_even = min(max(inv.get("cost", 0.0) / qty, 0.001), 0.989)
            ask_touch = book.asks[0][0] if book.asks else break_even + book.tick
            px = round(max(break_even + book.tick, ask_touch), 3)
            r = self.desk.place_resting(slug, "SELL", px, rest,
                                        net_position=qty, intent=SELL_LONG)
            if r.ok:
                self.orders[r.order_id] = FamilyOrder(
                    id=r.order_id, market=slug, side="SELL", price=px,
                    qty=rest, intent=SELL_LONG, placed_ts=now, purpose="sell")
                self._log(event="sell_rested", market=slug, price=px, qty=rest)
                self._mark(slug, "SELL", now)
                actions -= 1

        summary["refreshed"] = refreshed
        return self._finish(summary)

    def _refresh_books(self, client, cat: dict, now: float) -> int:
        """Fetch a few books: active markets by staleness first, then the
        candidate scan rotation. All through this family's own cache.

        The scan keeps a reserved slice of the budget. Without it, the
        first night's 15 active markets ate all six fetches every cycle
        (every book is older than one 60s poll) and the family stopped
        discovering anything new — the owner found it "on but not doing
        anything" (2026-08-20 morning). Maintenance only needs a book
        fresher than 4x BOOK_MAX_AGE, so actives can wait 150s between
        refreshes and still stay well inside that."""
        budget = self.cfg.books_per_cycle
        scan_reserve = min(self.cfg.scan_reserve, budget)
        done = 0
        active = sorted(self.active_markets() | set(self.inventory),
                        key=lambda s: self.cache.age(s, now), reverse=True)
        for slug in active:
            if done >= budget - scan_reserve:
                break
            if self.cache.age(slug, now) > 150.0:
                try:
                    self.cache.put(slug, client.book(slug, fetched_at=now))
                    done += 1
                except Exception as e:  # noqa: BLE001
                    self._log(event="book_error", market=slug, error=str(e)[:60])
                    done += 1
        idle = [s for s in cat if s not in self.active_markets()
                and now - (self.scoreboard.get(s) or {}).get("ts", 0.0)
                > self.cfg.rescan_s]
        idle.sort(key=lambda s: (self.scoreboard.get(s) or {}).get("ts", 0.0))
        for slug in idle:
            if done >= budget:
                break
            days = slug_days_out(slug, now)
            if days is not None and days < self.cfg.min_days_out:
                self.scoreboard[slug] = {"ts": now, "plans": []}
                continue
            try:
                book = client.book(slug, fetched_at=now)
                self.cache.put(slug, book)
            except Exception as e:  # noqa: BLE001
                self.scoreboard[slug] = {"ts": now, "plans": [], "err": str(e)[:60]}
                done += 1
                continue
            plans = self.plan_market(book, cat[slug])
            self.scoreboard[slug] = {"ts": now, "plans": plans,
                                     "est": round(sum(p["est"] for p in plans), 4)}
            done += 1
        for gone in set(self.scoreboard) - set(cat):
            del self.scoreboard[gone]
        return done

    def _finish(self, summary: dict) -> dict:
        summary["orders"] = [vars(o) for o in self.orders.values()]
        summary["est_day"] = round(sum(o.live_est if o.live_est is not None
                                       else o.est_day
                                       for o in self.orders.values()
                                       if o.purpose != "sell"), 2)
        summary["stock_day"] = round(sum(o.live_est or 0.0
                                         for o in self.orders.values()
                                         if o.purpose == "sell"), 2)
        summary["spent"] = round(sum(capital_at_risk(o.intent, o.price, o.qty)
                                     for o in self.orders.values()
                                     if o.purpose != "sell"), 2)
        summary["inventory"] = {k: dict(v) for k, v in self.inventory.items()}
        top = sorted((sb for sb in self.scoreboard.values() if sb.get("plans")),
                     key=lambda sb: -(sb.get("est") or 0.0))
        summary["scanned"] = sum(1 for sb in self.scoreboard.values()
                                 if "plans" in sb)
        summary["best_idle"] = round(top[0]["est"], 3) if top else None
        return summary

    # ------------------------------------------------------------ persistence

    def to_dict(self) -> dict:
        return {
            "orders": {oid: vars(o) for oid, o in self.orders.items()},
            "inventory": self.inventory,
            "positions_seen": self.positions_seen,
            "silent_cancels": self.silent_cancels,
            "last_action": self.last_action,
            # the scan pipeline survives restarts — losing it silenced the
            # family for hours on 2026-08-20 (placements come FROM it)
            "scoreboard": self.scoreboard,
            "log": self.log[-self.cfg.log_keep:],
        }

    def restore(self, d: dict) -> None:
        for oid, v in (d.get("orders") or {}).items():
            self.orders[oid] = FamilyOrder(**{k: x for k, x in v.items()
                                           if k in FamilyOrder.__dataclass_fields__})
        self.inventory = dict(d.get("inventory") or {})
        self.positions_seen = dict(d.get("positions_seen") or {})
        self.silent_cancels = d.get("silent_cancels") or 0
        self.last_action = dict(d.get("last_action") or {})
        self.scoreboard = dict(d.get("scoreboard") or {})
        self.log = list(d.get("log") or [])


def college() -> FamilyConfig:
    """The launch family. Week 0 kicks off Saturday 2026-08-29; the weekly
    Thu-evening-to-Sun-morning pull starts with that week's Thursday."""
    return FamilyConfig(season_start=(2026, 8, 27))


def nfl() -> FamilyConfig:
    """NFL futures: awards and title races (tec-nfl), makes-the-playoffs
    (aqc-nfl), and the season stat futures (ftsc/fptc). Behind-the-touch
    only, per the owner's 2026-08-20 correction. Resting window Tuesday
    06:00 -> Thursday 17:00 ET: NFL plays Thursday/Sunday/Monday (and any
    day in preseason weekends), so the family is out from Thursday evening
    through Tuesday morning."""
    return FamilyConfig(
        name="NFL futures", tag="NFL",
        prefixes=("tec-nfl-", "aqc-nfl-", "ftsc-nfl-", "fptc-nfl-"),
        rest_from=(1, 6), rest_until=(3, 17),
        allow_improve=False,
        season_start=(2026, 8, 20),   # preseason games are already playing
    )
