"""The engine. One class; every market category is a config of it.

3.0's merge of the two 2.0 engines, built to the owner's 2026-08-20
instruction: "Simplicity of v2 and personality of v1. A new version that
prioritizes politics but can be expanded in the way I expanded V2."

* A family's UNIVERSE comes from a pluggable `discover` function
  (politics: the events feed, names and event divisor included) or, for
  prefix families, whatever discover function wraps their sweep. The
  family fetches its own reward terms for that universe — no survey
  dependency, no shared mutable state with any other version.
* Resting style is config: `behind` (every new family — owner's rule)
  or `join_quiet` (politics, the owner's known ground: join the touch
  only when the book has been sitting still; step back when it is busy).
  Nothing in 3.0 ever prices IN FRONT of the touch.
* Qualifying a dead side is just another candidate (`revive=True`,
  known ground only): estimate_join already prices what happens when our
  size is what carries the side over Target Size. The owner accepted
  over-target exposure explicitly ("I'm fine with the qualifier bringing
  sides of the markets over their target size, I just need a list of
  where I'm exposed") — the exposure list is the blocks page.
* One risk number binds: `capital_usd`, the family's total collateral
  ceiling. The per-market cap exists but the family line is the one the
  owner watches.
* A market whose program died is LEFT ENTIRELY — every order cancelled,
  exits included, seller stood down (owner: "I don't want to be in
  markets if there are no rewards" / "You can remove the unwinding
  positions as well").
* No estimate until the divisor is confirmed: only markets that arrived
  through discovery (which knows their event) ever show a dollar figure.
  The 2026-08-20 lesson — a guessed divisor turned $1.50/day into
  $23.30/day on a phone screen — does not repeat.
* Every skip and every plan carries a plain-English `why`. The engine is
  read-only until its own switch is armed; while observing it still
  discovers, scores and shows exactly what it would do, so the owner can
  judge it against the running 1.0 before any money moves.

All money-touching calls go through the OrderDesk rails: post-only, price
bounds, whitelist, verify-by-id, never /modify.
"""

from __future__ import annotations

import datetime as dt
import time
from dataclasses import dataclass, field
from zoneinfo import ZoneInfo

from .books import BookCache
from .intents import BUY_LONG, SELL_LONG, SELL_SHORT, capital_at_risk
from .orders import OrderDesk
from .scoring import estimate_join
from .terms import TermsStore

ET = ZoneInfo("America/New_York")

BOOK_MAX_AGE = 120.0

# size grid the planner walks (contracts); fractional sizes are live rails
QTY_GRID = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0,
            50.0, 100.0, 200.0, 500.0)


@dataclass
class FamilyConfig:
    name: str = "Family"
    tag: str = "FAM"
    # Known ground = a category the owner reads fluently (politics). It
    # unlocks join_quiet resting and reviving dead sides. Everything the
    # owner is NOT familiar with stays behind the touch and never revives
    # (owner, 2026-08-20: "don't auto set... in families where I'm not
    # familiar" and "place them behind the touch because of the df").
    known_ground: bool = False
    rest_style: str = "behind"          # "behind" | "join_quiet"
    revive: bool = False                # may qualify a below-target side
    vol_quiet: float = 0.15             # book EWMA below this = quiet enough to join
    # THE risk number: total collateral this family may hold at once.
    capital_usd: float = 25.0
    per_market_usd: float = 1.00        # both sides combined
    revive_max_usd: float = 5.0         # a revival order's own collateral cap
    share_hi: float = 0.10              # courtesy ceiling when others carry the side
    # optional weekly no-resting window (game days), ET (weekday, hour);
    # None = the family rests every day (politics)
    rest_from: tuple[int, int] | None = None
    rest_until: tuple[int, int] | None = None
    season_start: tuple[int, int, int] | None = None
    min_days_out: int = 3               # nothing resolving this week
    max_actions_per_cycle: int = 6
    books_per_cycle: int = 16
    scan_reserve: int = 6
    book_stale_s: float = 150.0         # refresh an active market's book this often
    read_age_s: float = 480.0           # oldest book maintenance will read
    verify_resting: bool = False        # next cycle's reconcile checks by id anyway
    rescan_s: float = 4 * 3600.0
    # College only: may price IN FRONT of a junk touch (wall-only books).
    # The owner kept college's launch behavior ("I wouldn't change anything
    # for now"); every other family leaves this off.
    allow_improve: bool = False
    # Take over resting orders already on the account in this family's
    # markets (the 1.0/2.0 handover). Owner-placed manual orders are never
    # claimed.
    adopt: bool = True
    terms_slice: int = 120              # universe terms slugs per full-refresh pass
    cooldown_s: float = 3600.0
    min_est_day: float = 0.02
    # Cycle-out rule (owner, 2026-08-20: "be very picky... and if
    # something's not working cycle out of it"): an order measured under
    # min_est_day for this long, with no plan at this market that clears
    # the bar either, is pulled so the capital can go to the next best
    # market. 0 disables.
    weak_pull_s: float = 0.0
    reprice_gain_day: float = 0.06
    drift_share: float = 0.15
    terms_active_s: float = 600.0       # live terms for markets we're in
    terms_full_s: float = 3600.0        # the whole universe's terms
    discover_s: float = 6 * 3600.0
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
    purpose: str         # earn / revive / sell
    why: str = ""        # plain-English placement reason, shown on pages
    est_day: float = 0.0
    share: float = 0.0
    live_est: float | None = None
    live_share: float | None = None
    weak_since: float = 0.0   # measuring under the bar since (0 = fine)
    verdict: str = ""    # plain-English live state, refreshed each cycle


def resting_ok(now: float, cfg: FamilyConfig) -> bool:
    """Inside the family's resting window? No window means every hour is a
    resting hour. Before season_start there are no game days."""
    if cfg.rest_from is None or cfg.rest_until is None:
        return True
    t = dt.datetime.fromtimestamp(now, ET)
    if cfg.season_start is not None and t.date() < dt.date(*cfg.season_start):
        return True
    m = t.weekday() * 24 + t.hour
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


def _et_day(now: float) -> str:
    return dt.datetime.fromtimestamp(now, ET).date().isoformat()


class Family:
    """One market category: its universe, terms, books, orders, and money.

    `discover(client) -> dict[slug, {"event_n": int, "name": str, ...}]`
    is injected; everything the family knows starts there. The desk's
    whitelist should be wired to `knows()` so no order can leave the
    family's own ground.
    """

    def __init__(self, desk: OrderDesk, cache: BookCache, discover,
                 config: FamilyConfig | None = None, alert=None,
                 names=None, clock=None):
        self.desk = desk
        self.cache = cache
        self.discover = discover
        self.cfg = config or FamilyConfig()
        self.alert = alert or (lambda title, msg: None)
        self.names = names
        self._clock = clock or time.time
        self.terms = TermsStore()
        self.universe: dict[str, dict] = {}       # slug -> {event_n, ...}
        self.orders: dict[str, FamilyOrder] = {}
        self.history: dict[str, float] = {}       # slug -> avg $/day actually PAID
        self.inventory: dict[str, dict] = {}      # slug -> {qty, cost}
        self.positions_seen: dict[str, float] = {}
        self.scoreboard: dict[str, dict] = {}     # slug -> {ts, plans, why...}
        self.last_action: dict[str, float] = {}   # "slug|side" -> ts
        self.known_dead: set[str] = set()          # program read as gone
        self.last_discover = 0.0
        self.last_terms_active = 0.0
        self.last_terms_full = 0.0
        self._terms_rotor = 0
        self.earned_today = 0.0
        self.earned_day = ""
        self.earned_history: list[list] = []      # [day, $] rolling
        self._last_accrual = 0.0
        self.silent_cancels = 0
        self.log: list[dict] = []

    # ------------------------------------------------------------- helpers

    def _label(self, slug: str) -> str:
        return self.names.label(slug) if self.names is not None else slug

    def _log(self, **row) -> None:
        row.setdefault("ts", round(self._clock(), 1))
        self.log.append(row)
        del self.log[:-self.cfg.log_keep]

    def knows(self, slug: str) -> bool:
        """This family's ground: discovered markets, plus anything we
        already hold orders or stock in (so exits always stay legal)."""
        return (slug in self.universe or slug in self.inventory
                or any(o.market == slug for o in self.orders.values()))

    def _cooldown_ok(self, slug: str, side: str, now: float) -> bool:
        return now - self.last_action.get(f"{slug}|{side}", 0.0) >= self.cfg.cooldown_s

    def _mark(self, slug: str, side: str, now: float) -> None:
        self.last_action[f"{slug}|{side}"] = now

    def market_spent(self, slug: str) -> float:
        return sum(capital_at_risk(o.intent, o.price, o.qty)
                   for o in self.orders.values()
                   if o.market == slug and o.purpose != "sell")

    def family_spent(self) -> float:
        """The one risk number: collateral across every resting order."""
        return sum(capital_at_risk(o.intent, o.price, o.qty)
                   for o in self.orders.values() if o.purpose != "sell")

    def active_markets(self) -> set[str]:
        return {o.market for o in self.orders.values() if o.purpose != "sell"}

    def _dead_here(self, slug: str) -> bool:
        """Program known dead: read as paying nothing, or read as GONE
        (absent from the incentives response — the store drops the record,
        so gone markets are remembered here). A market never successfully
        read is NOT dead — no data is no verdict."""
        prog = self.terms.get(slug)
        if prog is None:
            return slug in self.known_dead
        return not prog.is_live() or not prog.pool

    def _prog_row(self, slug: str):
        """The program to score against, or (None, why-not)."""
        prog = self.terms.get(slug)
        if prog is None:
            return None, "no reward terms read yet"
        if not prog.is_live() or not prog.pool:
            return None, "program pays nothing"
        if not prog.df or not prog.target:
            return None, "terms incomplete (no df or Target Size)"
        return prog, ""

    def _side_pool(self, slug: str, prog) -> float | None:
        """$/day one side competes for — or None when the event divisor is
        unconfirmed (then NOTHING shows a dollar figure; owner: "don't
        estimate until you have a grasp of everything you need to know")."""
        u = self.universe.get(slug) or {}
        n = u.get("event_n")
        if not n:
            return None
        return (prog.pool or 0.0) / max(int(n), 1) / 2.0

    # ------------------------------------------------------------ discovery

    def refresh_universe(self, client, now: float) -> None:
        if now - self.last_discover < self.cfg.discover_s and self.universe:
            return
        self.last_discover = now
        try:
            found = self.discover(client) or {}
        except Exception as e:  # noqa: BLE001 — keep the old universe
            self._log(event="discover_error", error=str(e)[:80])
            return
        fresh = set(found) - set(self.universe)
        self.universe = found
        if self.names is not None:
            for slug, row in found.items():
                if row.get("name"):
                    self.names.learn(slug, {"title": row["name"]})
        if fresh:
            self._log(event="discovered", n=len(found), new=len(fresh))

    def refresh_terms(self, client, now: float) -> None:
        """Two cadences: markets we're in (fast), the whole universe in a
        rotating slice (slow). Every requested slug is force-present in
        the raw map so 'absent from the incentives response' reads as
        program-gone — first reading acts (owner: "Don't hold the dead
        market scan"). A failed fetch changes nothing (data safety)."""
        batch: list[str] = []
        if now - self.last_terms_active >= self.cfg.terms_active_s:
            self.last_terms_active = now
            batch += sorted(self.active_markets() | set(self.inventory))
        if now - self.last_terms_full >= self.cfg.terms_full_s and self.universe:
            slugs = sorted(self.universe)
            take = self.cfg.terms_slice
            lo = self._terms_rotor % max(len(slugs), 1)
            batch += (slugs[lo:lo + take] + slugs[:max(0, lo + take - len(slugs))])
            self._terms_rotor = (lo + take) % max(len(slugs), 1)
            if self._terms_rotor < take:
                self.last_terms_full = now   # a full lap is done
        batch = list(dict.fromkeys(batch))
        if not batch:
            return
        try:
            raw = client.programs(batch)
        except Exception as e:  # noqa: BLE001 — aged terms beat no terms
            self._log(event="terms_error", error=str(e)[:80])
            return
        for slug in batch:
            raw.setdefault(slug, {})
        sizes = {s: int((self.universe.get(s) or {}).get("event_n") or 0) or 1
                 for s in batch}
        for ch in self.terms.refresh(raw, sizes, now=now):
            if ch.field == "program_gone":
                self.known_dead.add(ch.slug)
            elif ch.field == "program_new":
                self.known_dead.discard(ch.slug)
            if ch.field in ("pool", "program_gone", "program_new"):
                self._log(event="terms_change", market=ch.slug, field=ch.field,
                          old=str(ch.old), new=str(ch.new))
                self.alert(f"{self.cfg.tag}: reward pool change",
                           f"{self._label(ch.slug)}: {ch.field} "
                           f"{ch.old} -> {ch.new}")

    # ------------------------------------------------------------- planning

    def _plan_side(self, slug: str, book, side: str, prog,
                   side_pool: float | None, budget: float,
                   own: FamilyOrder | None = None) -> dict | None:
        """The best resting order for one side, or None. Every plan and
        every refusal is phone-readable."""
        df, target = float(prog.df), float(prog.target)
        levels = list(book.side(side))
        if own is not None:
            levels = [(p, q - own.qty if abs(p - own.price) < 1e-9 else q)
                      for p, q in levels]
            levels = [(p, q) for p, q in levels if q > 1e-9]
        side_name = "bid" if side == "BUY" else "ask"
        sign = 1.0 if side == "BUY" else -1.0
        tick = book.tick
        other = book.side("SELL" if side == "BUY" else "BUY")
        side_total = sum(q for _, q in levels)

        if side_pool is None:
            return None     # divisor unconfirmed: no estimate, no order

        # -- a side below Target Size pays nobody: skip it, or revive it --
        if side_total < target:
            if not (self.cfg.revive and self.cfg.known_ground):
                return None
            gap = target - side_total
            if not levels and not other:
                return None                       # empty book, no anchor
            anchor = (levels[0][0] if levels
                      else other[0][0] - sign * 5 * tick)
            qty = round(gap * 1.02 + 1.0, 2)
            best = None
            for k in (0, 1, 2, 3):
                px = round(anchor - k * sign * tick, 3)
                if not (0.001 <= px <= 0.999):
                    continue
                if other and (px >= other[0][0] - 1e-9 if side == "BUY"
                              else px <= other[0][0] + 1e-9):
                    continue
                cost = qty * (px if side == "BUY" else 1.0 - px)
                # a revival is bigger than an earn order by nature — its own
                # cap applies, not the per-market split; the family ceiling
                # still binds at placement
                if cost > self.cfg.revive_max_usd + 1e-9:
                    continue
                j = estimate_join(side, levels, tick, df, target, px, qty)
                if not (j.qualifies and j.in_window):
                    continue
                est = j.share * side_pool
                if best is None or est > best["est"]:
                    best = {"side": side, "px": px, "qty": qty,
                            "share": round(j.share, 4), "est": round(est, 4),
                            "cost": round(cost, 2), "revive": True,
                            "why": (f"the {side_name} side holds "
                                    f"{side_total:,.0f} of {target:,.0f} Target"
                                    f" Size and pays NOBODY — this order "
                                    f"revives it and takes ~"
                                    f"{j.share * 100:.0f}% of the side")}
            if best is not None and best["est"] >= self.cfg.min_est_day:
                return best
            return None

        # -- the side qualifies: join or step back, never in front --
        touch = levels[0][0]
        # Joining the touch needs EVIDENCE of quiet: a volatility reading
        # exists only after repeated fetches, so a first entry always goes
        # behind the touch and only a market we are already watching can
        # graduate to the touch. Known ground only.
        join_ok = False
        if self.cfg.rest_style == "join_quiet":
            v = self.cache.volatility_of(slug)
            join_ok = v is not None and v <= self.cfg.vol_quiet
        rungs = ((0,) if join_ok else ()) + (1, 2, 3, 6, 10, 15)
        cands = []
        for k in rungs:
            px = round(touch - k * sign * tick, 3)
            if not (0.001 <= px <= 0.999):
                continue
            if other and (px >= other[0][0] - 1e-9 if side == "BUY"
                          else px <= other[0][0] + 1e-9):
                continue
            if px not in cands:
                cands.append(px)
        if self.cfg.allow_improve:
            # College's launch quirk, kept on the owner's word: in a book
            # whose touch is a junk wall far from any opposing quote, a
            # small order may price in front of it. The improve rungs stay
            # 5 ticks clear of the other side's touch; with no opposing
            # quote at all there is no value anchor, so the rungs stay
            # short and size is clamped to probe money (in the qty grid).
            if other:
                cap_improve = other[0][0] - sign * 5 * tick
                improve = (1, 5, 10, 15, 20)
            else:
                cap_improve = touch + sign * 10 * tick
                improve = (1, 5, 10)
                budget = min(budget, 0.05)
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
        pick, solo = None, None
        for px in cands:
            cost_ps = px if side == "BUY" else 1.0 - px
            for qty in QTY_GRID:
                if qty * cost_ps > budget + 1e-9:
                    break
                j = estimate_join(side, levels, tick, df, target, px, qty)
                if not (j.qualifies and j.in_window):
                    break
                est = j.share * side_pool
                k = round(abs(touch - px) / tick)
                in_front = (px - touch) * sign > 1e-9
                row = {"side": side, "px": px, "qty": qty,
                       "share": round(j.share, 4), "est": round(est, 4),
                       "cost": round(qty * cost_ps, 2),
                       "why": ("joins the touch — the book has been quiet"
                               if k == 0 and not in_front else
                               f"{k} tick{'s' if k != 1 else ''} in front of "
                               f"a junk wall — nothing real to stand behind"
                               if in_front else
                               f"{k} tick{'s' if k != 1 else ''} behind the "
                               f"touch, ~{j.share * 100:.1f}% of the "
                               f"{side_name} side")}
                if j.share > self.cfg.share_hi:
                    # louder than the courtesy band: acceptable only as a
                    # minimum-size solo in front of a wall (college)
                    if in_front and qty == QTY_GRID[0]:
                        if solo is None or est > solo["est"] + 1e-9:
                            solo = {**row, "solo": True}
                    break
                if pick is None or est > pick["est"] + 1e-9:
                    pick = row
        if pick is not None and pick["est"] >= self.cfg.min_est_day:
            return pick
        if solo is not None and solo["est"] >= self.cfg.min_est_day:
            return solo
        return None

    def plan_market(self, book, slug: str) -> tuple[list[dict], str]:
        """Both sides' best entries, within the caps. Returns (plans, why)
        — why explains an empty answer in the owner's language."""
        prog, why = self._prog_row(slug)
        if prog is None:
            return [], why
        side_pool = self._side_pool(slug, prog)
        if side_pool is None:
            return [], ("still confirming how many markets share this "
                        "pool — no estimate until I know")
        budget = self.cfg.per_market_usd / 2.0
        out = []
        for side in ("BUY", "SELL"):
            p = self._plan_side(slug, book, side, prog, side_pool, budget)
            if p:
                out.append(p)
        if not out:
            why = ("nothing here clears the bar: both sides either pay "
                   f"under {self.cfg.min_est_day * 100:.0f}c/day, are louder "
                   "than the courtesy band, or don't qualify")
        return out, why

    # -------------------------------------------------------------- reconcile

    def reconcile(self, open_orders: list[dict], positions: dict, now: float) -> None:
        """Adopt reality. Fills come from position deltas, never from mere
        disappearance. Scoped to markets THIS family placed in — the
        account is shared with 1.0 and 2.0, and their fills are not ours."""
        open_by_id = {o["id"]: o for o in open_orders}
        tracked = (set(self.positions_seen) | set(self.inventory)
                   | {o.market for o in self.orders.values()})
        deltas = {m: (positions.get(m) or (0.0, 0.0))[0]
                  - self.positions_seen.get(m, 0.0)
                  for m in tracked}
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
        for m in tracked:
            if m in positions:
                self.positions_seen[m] = positions[m][0]
        for m in list(self.positions_seen):
            if (m not in self.inventory
                    and m not in {o.market for o in self.orders.values()}):
                self.positions_seen.pop(m, None)

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
        self.alert(f"{self.cfg.tag} order filled",
                   f"{self._label(rec.market)}: {rec.side} {filled:g} @ "
                   f"{rec.price * 100:g}c — fills are usually losses here; "
                   f"the exit seller takes over")

    # ---------------------------------------------------------------- adoption

    def adoptable(self, open_orders: list[dict], foreign_ids=()) -> list[dict]:
        """Resting account orders this family would take over: in its
        universe, not already claimed (by it or a sibling family), and
        never the owner's own manual orders."""
        out = []
        for o in open_orders:
            if o["id"] in self.orders or o["id"] in foreign_ids:
                continue
            if o.get("manual"):
                continue
            if o["market"] not in self.universe:
                continue
            if not o.get("size") or not o.get("price"):
                continue
            out.append(o)
        return out

    def _adopt(self, adoptable: list[dict], positions: dict, now: float) -> None:
        """The 1.0/2.0 handover: claim their resting orders as our own and
        take their long stock onto the exit seller's book. Runs only once
        the floor is ours (cycle gates it), so nothing else is still
        maintaining these orders when we start."""
        for o in adoptable:
            net0 = (positions.get(o["market"]) or (0.0, 0.0))[0]
            purpose = ("sell" if o["intent"] in (SELL_LONG, SELL_SHORT)
                       or (o["side"] == "SELL" and net0 > 0.005)
                       or (o["side"] == "BUY" and net0 < -0.005)
                       else "earn")

            self.orders[o["id"]] = FamilyOrder(
                id=o["id"], market=o["market"], side=o["side"],
                price=o["price"], qty=o["size"], intent=o["intent"],
                placed_ts=now, purpose=purpose,
                why="adopted from the earlier versions")
            self.positions_seen.setdefault(
                o["market"], (positions.get(o["market"]) or (0.0,))[0])
            # a cooldown from the moment of adoption: the inherited book is
            # already earning, so it converges to 3.0's shape at the usual
            # measured pace instead of being rearranged in a burst
            self._mark(o["market"], o["side"], now)
        if adoptable:
            self._log(event="adopted", n=len(adoptable))
            self.alert(f"{self.cfg.tag}: took over the resting book",
                       f"{len(adoptable)} orders adopted from the earlier "
                       f"versions — maintained under 3.0's rules from here")

    def _seed_inventory(self, positions: dict) -> None:
        """Positions on our ground the seller does not know yet — long
        stock OR shorts — join its book. Runs every armed cycle so a
        position found after the adoption still gets its exit."""
        for m, pv in positions.items():
            net, cost = ((list(pv) + [0.0, 0.0])[:2]
                         if isinstance(pv, (tuple, list)) else (float(pv), 0.0))
            if m in self.universe and abs(net) > 0.005 and m not in self.inventory:
                self.inventory[m] = {"qty": net, "cost": cost}
                self.positions_seen[m] = net

    # ------------------------------------------------------------------ cycle

    def _reclassify_exits(self, positions: dict) -> None:
        """An adopted order whose FILL reduces the position it sits on is
        an EXIT whatever its intent says — a bid covering a short, an ask
        while long. Mislabelling them "earn" once let maintenance reprice
        and pull the owner's exits (2026-08-20 23:12Z) and counted their
        collateral against the rebuild ceiling. Idempotent, every cycle."""
        for rec in self.orders.values():
            if rec.purpose == "sell":
                continue
            net = (positions.get(rec.market) or (0.0, 0.0))[0]
            if ((rec.side == "SELL" and net > 0.005)
                    or (rec.side == "BUY" and net < -0.005)):
                rec.purpose = "sell"
                rec.why = "an exit — its fill reduces the position it sits on"

    def cycle(self, now: float, open_orders: list[dict], positions: dict,
              client, switch_on: bool, foreign_ids=(),
              exits_only: bool = False) -> dict:
        self.reconcile(open_orders, positions, now)
        self._reclassify_exits(positions)
        self.refresh_universe(client, now)
        self.refresh_terms(client, now)
        refreshed = self._refresh_books(client, now)
        self._read_live(now)
        self._accrue(now)
        pending = (self.adoptable(open_orders, foreign_ids)
                   if self.cfg.adopt else [])
        summary = {"mode": "on" if switch_on else "observing",
                   "markets": len(self.universe),
                   "active": len(self.active_markets()),
                   "resting_ok": resting_ok(now, self.cfg),
                   "refreshed": refreshed,
                   "would_adopt": len(pending)}
        if not switch_on:
            return self._finish(summary)
        if pending:
            self._adopt(pending, positions, now)
            summary["would_adopt"] = 0
            summary["active"] = len(self.active_markets())
        if self.cfg.adopt:
            self._seed_inventory(positions)
        if exits_only:
            # the flatten's first phase: the monitor is cancelling every
            # opening order; this family only keeps stock exiting — asks
            # that cost nothing to place and earn while they wait
            summary["mode"] = "flatten — exits only"
            self._sell(now, self.cfg.max_actions_per_cycle)
            return self._finish(summary)
        actions = self.cfg.max_actions_per_cycle

        # game window: pull everything that isn't an exit
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

        # 1) leave dead or near-resolution markets ENTIRELY (exits included)
        for rec in list(self.orders.values()):
            if actions <= 0:
                break
            days = slug_days_out(rec.market, now)
            near = days is not None and days < self.cfg.min_days_out
            dead = self._dead_here(rec.market)
            if dead or (near and rec.purpose != "sell"):
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    why = "program pays nothing" if dead else "resolves soon"
                    self._log(event="exit", market=rec.market, why=why, id=rec.id)
                    del self.orders[rec.id]
                    actions -= 1

        # 2) maintenance: reprice or pull against fresh books
        actions = self._maintain(now, actions)

        # 3) the seller first — getting the owner OUT always outranks new
        # risk (starving it behind entries left shorts uncovered, 23:53Z)
        actions = self._sell(now, actions)

        # 4) new entries, best scoreboard candidates first
        self._enter(now, positions, actions)
        return self._finish(summary)

    def _read_live(self, now: float) -> None:
        """Refresh every order's live share/est and verdict — the reading
        happens whether or not the switch is on (the observing mode's
        whole point)."""
        for rec in self.orders.values():
            book = self.cache.fresh(rec.market, self.cfg.read_age_s, now)
            prog, why = self._prog_row(rec.market)
            if book is None:
                rec.verdict = "no fresh book — can't read this one right now"
                continue
            if prog is None:
                rec.live_est, rec.live_share = 0.0, 0.0
                rec.verdict = why
                continue
            side_pool = self._side_pool(rec.market, prog)
            lv = [(p, q - rec.qty if abs(p - rec.price) < 1e-9 else q)
                  for p, q in book.side(rec.side)]
            lv = [(p, q) for p, q in lv if q > 1e-9]
            j = estimate_join(rec.side, lv, book.tick, float(prog.df),
                              float(prog.target), rec.price, rec.qty)
            rec.live_share = round(j.share, 4)
            if side_pool is None:
                rec.live_est = None
                rec.verdict = ("scoring ~"
                               f"{j.share * 100:.1f}% of its side — holding "
                               "the estimate until the pool divisor is known")
                continue
            rec.live_est = round(j.share * side_pool
                                 if j.qualifies and j.in_window else 0.0, 4)
            if not j.qualifies:
                rec.verdict = ("its side is below Target Size — the whole "
                               "side pays nobody right now")
            elif not j.in_window:
                rec.verdict = "outside the Target Size window — earning $0"
            else:
                rec.verdict = (f"earning ~${rec.live_est:.2f}/day — "
                               f"{j.share * 100:.1f}% of its side")

    def _maintain(self, now: float, actions: int) -> int:
        for rec in list(self.orders.values()):
            if actions <= 0:
                break
            if rec.purpose == "sell":
                continue
            book = self.cache.fresh(rec.market, self.cfg.read_age_s, now)
            prog, _why = self._prog_row(rec.market)
            if book is None or prog is None:
                continue
            side_pool = self._side_pool(rec.market, prog)
            if side_pool is None:
                continue
            if not self._cooldown_ok(rec.market, rec.side, now):
                continue
            best = self._plan_side(rec.market, book, rec.side, prog,
                                   side_pool,
                                   self.cfg.per_market_usd / 2.0, own=rec)
            drifted = ((rec.live_share or 0.0) > self.cfg.drift_share
                       and rec.purpose not in ("revive", "solo"))
            gain = (best["est"] if best else 0.0) - (rec.live_est or 0.0)
            below = (rec.live_est is not None
                     and rec.live_est < self.cfg.min_est_day)
            if below and not rec.weak_since:
                rec.weak_since = now
            elif not below:
                rec.weak_since = 0.0
            weak = (self.cfg.weak_pull_s > 0 and rec.weak_since
                    and now - rec.weak_since > self.cfg.weak_pull_s
                    and (best is None
                         or best["est"] < self.cfg.min_est_day))
            if (best is None and (rec.live_est or 0.0) <= 0.0) or weak:
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    why = (f"under {self.cfg.min_est_day * 100:.0f}c/day for "
                           f"{(now - rec.weak_since) / 3600:.1f}h — cycling "
                           f"out to the next best market" if weak else
                           "earning nothing and no better spot")
                    self._log(event="pull", market=rec.market, side=rec.side,
                              why=why)
                    del self.orders[rec.id]
                    self._mark(rec.market, rec.side, now)
                    actions -= 1
            elif (best is not None
                    and (drifted or gain >= self.cfg.reprice_gain_day)
                    and (abs(best["px"] - rec.price) > 1e-9
                         or abs(best["qty"] - rec.qty) > 1e-9)):
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
                        purpose=("revive" if best.get("revive")
                                 else "solo" if best.get("solo") else "earn"),
                        why=best["why"], est_day=best["est"], share=best["share"])
                    self._mark(rec.market, rec.side, now)
                    actions -= 1
        return actions

    def _enter(self, now: float, positions: dict, actions: int) -> int:
        have = {(o.market, o.side) for o in self.orders.values()
                if o.purpose != "sell"}
        # proven ground first (owner, 2026-08-20: "looking at the orders
        # that were the most successful and trying to replicate those") —
        # a market's record of actually PAYING us counts alongside what
        # the book says it should pay now
        ranked = sorted(((s, sb) for s, sb in self.scoreboard.items()
                         if sb.get("plans")),
                        key=lambda kv: -(sum(p["est"] for p in kv[1]["plans"])
                                         + min(self.history.get(kv[0], 0.0),
                                               5.0)))
        for slug, sb in ranked:
            if actions <= 0:
                break
            if slug not in self.universe or self._dead_here(slug):
                continue
            days = slug_days_out(slug, now)
            if days is not None and days < self.cfg.min_days_out:
                continue
            for plan in sb["plans"]:
                if actions <= 0:
                    break
                if plan["est"] < self.cfg.min_est_day:
                    continue    # a plan scored under an older, looser config
                if (slug, plan["side"]) in have:
                    continue
                if not self._cooldown_ok(slug, plan["side"], now):
                    continue
                if self.market_spent(slug) + plan["cost"] \
                        > self.cfg.per_market_usd + 1e-9 \
                        and not plan.get("revive"):
                    continue
                if self.family_spent() + plan["cost"] \
                        > self.cfg.capital_usd + 1e-9:
                    continue          # THE ceiling — one number, it binds
                book = self.cache.fresh(slug, BOOK_MAX_AGE, now)
                if book is None:
                    continue
                net = (positions.get(slug) or (0.0,))[0]
                r = self.desk.place_resting(slug, plan["side"], plan["px"],
                                            plan["qty"], net_position=net,
                                            verify=self.cfg.verify_resting)
                if r.ok and r.order_id:
                    self.positions_seen.setdefault(slug, net)
                    self.orders[r.order_id] = FamilyOrder(
                        id=r.order_id, market=slug, side=plan["side"],
                        price=plan["px"], qty=plan["qty"], intent=r.intent,
                        placed_ts=now,
                        purpose=("revive" if plan.get("revive")
                                 else "solo" if plan.get("solo") else "earn"),
                        why=plan["why"], est_day=plan["est"],
                        share=plan["share"])
                    self._log(event="place", market=slug, side=plan["side"],
                              price=plan["px"], qty=plan["qty"],
                              est=plan["est"], why=plan["why"][:90])
                    self._mark(slug, plan["side"], now)
                    actions -= 1
                else:
                    self._log(event="refused", market=slug, side=plan["side"],
                              note=r.note[:90])
                    self._mark(slug, plan["side"], now)
        return actions

    def _sell(self, now: float, actions: int) -> int:
        for slug, inv in list(self.inventory.items()):
            if actions <= 0:
                break
            qty = inv.get("qty") or 0.0
            if abs(qty) < 0.01:
                continue
            if self._dead_here(slug):
                continue      # out means out — no resting anything there
            book = self.cache.fresh(slug, BOOK_MAX_AGE, now)
            if book is None:
                continue
            if qty >= 0.01:
                # long stock: an ask at break-even or better
                covered = sum(o.qty for o in self.orders.values()
                              if o.market == slug and o.purpose == "sell"
                              and o.side == "SELL")
                rest = qty - covered
                if rest < 0.01 or not self._cooldown_ok(slug, "SELL", now):
                    continue
                break_even = min(max(inv.get("cost", 0.0) / qty, 0.001), 0.989)
                ask_touch = (book.asks[0][0] if book.asks
                             else break_even + book.tick)
                px = round(max(break_even + book.tick, ask_touch), 3)
                side, intent, rest_qty = "SELL", SELL_LONG, rest
                why = "selling filled stock — it earns while it waits"
            else:
                # a SHORT: buy it back at the bid touch, never above
                # break-even — the bid earns rewards while it exits and
                # adds no collateral (owner, 2026-08-20: "try and exit
                # positions in a way that earns liquidity reward")
                covered = sum(o.qty for o in self.orders.values()
                              if o.market == slug and o.purpose == "sell"
                              and o.side == "BUY")
                rest = -qty - covered
                if rest < 0.01 or not self._cooldown_ok(slug, "BUY", now):
                    continue
                received = min(max(-inv.get("cost", 0.0) / -qty, 0.002), 0.999)
                bid_touch = (book.bids[0][0] if book.bids
                             else received - book.tick)
                px = round(min(received - book.tick, bid_touch), 3)
                px = min(max(px, 0.001), 0.999)
                side, intent, rest_qty = "BUY", SELL_SHORT, rest
                why = ("buying back the short at or under what it sold "
                       "for — the bid earns while it waits")
            r = self.desk.place_resting(slug, side, px, rest_qty,
                                        net_position=qty, intent=intent)
            if r.ok and r.order_id:
                self.orders[r.order_id] = FamilyOrder(
                    id=r.order_id, market=slug, side=side, price=px,
                    qty=rest_qty, intent=intent, placed_ts=now,
                    purpose="sell", why=why)
                self._log(event="sell_rested", market=slug, price=px,
                          qty=rest_qty, side=side)
                self._mark(slug, side, now)
                actions -= 1
        return actions

    # --------------------------------------------------------------- books

    def _refresh_books(self, client, now: float) -> int:
        """Active markets by staleness first; the candidate scan keeps its
        reserved slice so discovery can never starve (the 2026-08-20 CFB
        lesson)."""
        budget = self.cfg.books_per_cycle
        scan_reserve = min(self.cfg.scan_reserve, budget)
        done = 0
        active = sorted(self.active_markets() | set(self.inventory),
                        key=lambda s: self.cache.age(s, now), reverse=True)
        for slug in active:
            if done >= budget - scan_reserve:
                break
            if self.cache.age(slug, now) > self.cfg.book_stale_s:
                try:
                    self.cache.put(slug, client.book(slug, fetched_at=now))
                except Exception as e:  # noqa: BLE001
                    self._log(event="book_error", market=slug, error=str(e)[:60])
                done += 1
        idle = [s for s in self.universe if s not in self.active_markets()
                and now - (self.scoreboard.get(s) or {}).get("ts", 0.0)
                > self.cfg.rescan_s]
        idle.sort(key=lambda s: (-min(self.history.get(s, 0.0), 5.0),
                                 (self.scoreboard.get(s) or {}).get("ts", 0.0)))
        for slug in idle:
            if done >= budget:
                break
            days = slug_days_out(slug, now)
            if days is not None and days < self.cfg.min_days_out:
                self.scoreboard[slug] = {"ts": now, "plans": [],
                                         "why": "resolves soon — not worth entering"}
                continue
            if self._dead_here(slug):
                self.scoreboard[slug] = {"ts": now, "plans": [],
                                         "why": "program pays nothing"}
                continue
            prog, no_prog_why = self._prog_row(slug)
            if prog is None:
                # no terms yet: no book fetch spent; retry in ~15 minutes
                # rather than a full rescan interval, because the terms
                # rotor may confirm a pool for it within the hour
                self.scoreboard[slug] = {
                    "ts": now - self.cfg.rescan_s + 900.0, "plans": [],
                    "why": no_prog_why}
                continue
            try:
                book = client.book(slug, fetched_at=now)
                self.cache.put(slug, book)
            except Exception as e:  # noqa: BLE001
                self.scoreboard[slug] = {"ts": now, "plans": [],
                                         "why": f"book fetch failed: {str(e)[:50]}"}
                done += 1
                continue
            plans, why = self.plan_market(book, slug)
            self.scoreboard[slug] = {"ts": now, "plans": plans, "why": why,
                                     "est": round(sum(p["est"] for p in plans), 4)}
            done += 1
        for gone in set(self.scoreboard) - set(self.universe):
            del self.scoreboard[gone]
        return done

    # ------------------------------------------------------------- estimate

    def _accrue(self, now: float) -> None:
        """ONE earned-today number: the live rate integrated over time,
        accruing only while enough of our order books are fresh (no
        quorum, no accrual — a blind stretch adds nothing rather than a
        guess; owner: "If you miss a few seconds that is fine")."""
        day = _et_day(now)
        if self.earned_day and day != self.earned_day:
            self.earned_history.append([self.earned_day,
                                        round(self.earned_today, 2)])
            del self.earned_history[:-14]
            self.earned_today = 0.0
        self.earned_day = day
        dt_s = now - self._last_accrual if self._last_accrual else 0.0
        self._last_accrual = now
        if not (0.0 < dt_s <= 600.0):
            return
        mkts = {o.market for o in self.orders.values()
                if o.live_est is not None}
        if not mkts:
            return
        if self.cache.coverage(mkts, self.cfg.read_age_s, now) < 0.6:
            return
        rate = sum(o.live_est or 0.0 for o in self.orders.values())
        self.earned_today += rate * dt_s / 86400.0

    # --------------------------------------------------------------- finish

    def _finish(self, summary: dict) -> dict:
        summary["orders"] = [vars(o) for o in self.orders.values()]
        ests = [o.live_est if o.live_est is not None else o.est_day
                for o in self.orders.values() if o.purpose != "sell"]
        summary["est_day"] = round(sum(ests), 2)
        summary["stock_day"] = round(sum(o.live_est or 0.0
                                         for o in self.orders.values()
                                         if o.purpose == "sell"), 2)
        summary["spent"] = round(self.family_spent(), 2)
        summary["capital_usd"] = self.cfg.capital_usd
        summary["earned_today"] = round(self.earned_today, 2)
        summary["inventory"] = {k: dict(v) for k, v in self.inventory.items()}
        summary["scanned"] = sum(1 for sb in self.scoreboard.values()
                                 if "plans" in sb)
        top = sorted(((s, sb) for s, sb in self.scoreboard.items()
                      if sb.get("plans")),
                     key=lambda kv: -(kv[1].get("est") or 0.0))[:12]
        summary["best_idle"] = [
            {"market": s, "name": self._label(s), "est": sb.get("est"),
             "hist": self.history.get(s),
             "plans": sb["plans"]} for s, sb in top]
        return summary

    # ------------------------------------------------------------ persistence

    def _cfg_sig(self) -> str:
        c = self.cfg
        return "|".join(str(x) for x in (
            c.per_market_usd, c.min_est_day, c.share_hi, c.rest_style,
            c.allow_improve, c.revive, c.revive_max_usd, c.vol_quiet))

    def to_dict(self) -> dict:
        return {
            "cfg_sig": self._cfg_sig(),
            "orders": {oid: vars(o) for oid, o in self.orders.items()},
            "inventory": self.inventory,
            "positions_seen": self.positions_seen,
            "silent_cancels": self.silent_cancels,
            "last_action": self.last_action,
            "known_dead": sorted(self.known_dead),
            "scoreboard": self.scoreboard,
            "universe": self.universe,
            "terms": self.terms.to_dict(),
            "earned_today": round(self.earned_today, 4),
            "earned_day": self.earned_day,
            "earned_history": self.earned_history,
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
        self.known_dead = set(d.get("known_dead") or ())
        if d.get("cfg_sig") == self._cfg_sig():
            self.scoreboard = dict(d.get("scoreboard") or {})
        else:
            # the plans were scored under different knobs — the 2026-08-20
            # 23:53Z lesson: stale $1-era crumbs placed under a $20 config.
            # Rescan everything under the config actually running.
            self.scoreboard = {}
        self.universe = dict(d.get("universe") or {})
        if d.get("terms"):
            self.terms = TermsStore.from_dict(d["terms"])
        self.earned_today = float(d.get("earned_today") or 0.0)
        self.earned_day = str(d.get("earned_day") or "")
        self.earned_history = list(d.get("earned_history") or [])
        self.log = list(d.get("log") or [])
