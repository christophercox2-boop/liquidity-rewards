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

import math
import datetime as dt
import time
from dataclasses import dataclass, field
from zoneinfo import ZoneInfo

from . import risk
from .books import BookCache
from .evidence import Evidence
from .fillmodel import FillModel
from .intents import BUY_LONG, BUY_SHORT, SELL_LONG, SELL_SHORT, capital_at_risk
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
    # Restrict NEW entries to slugs containing any of these tokens (None =
    # the whole universe). Exits, adopted orders, and dead handling are
    # never scoped — only where fresh money goes.
    enter_tokens: tuple[str, ...] | None = None
    max_actions_per_cycle: int = 6
    books_per_cycle: int = 16
    scan_reserve: int = 6
    book_stale_s: float = 150.0         # refresh an active market's book this often
    read_age_s: float = 480.0           # oldest book maintenance will read
    verify_resting: bool = False        # next cycle's reconcile checks by id anyway
    rescan_s: float = 4 * 3600.0        # full REFETCH cadence per market
    # Re-SCORING a market whose book is already fresh in the cache (the
    # stream keeps ~100 live) costs no API call at all — so it happens
    # every replan_s, keeps the triage feed genuinely live, and catches a
    # spread opening minutes after it appears instead of hours
    # (owner, 2026-08-21: "I don't see anything moving").
    replan_s: float = 0.0               # 0 = off
    replans_per_cycle: int = 40
    # The prober (owner, 2026-08-21: "there are markets we can earn in
    # that need probing for information. Unless you have all the
    # information you need, go out and get some"): a market whose pool
    # could clear the bar but whose evidence confidence is still low gets
    # a one-share scout behind the touch. Its job is the information —
    # what fills it, what ignores it — and it earns a trickle meanwhile.
    probe_usd: float = 0.0            # concurrent probe collateral (0 = off)
    probe_qty: float = 1.0
    # whole-share quoting: the owner is testing whether fractional-share
    # orders are even picked up by the rewards program (2026-08-21)
    whole_shares: bool = False
    probe_ttl_s: float = 45 * 60.0    # rotate: 45 quiet minutes IS the datum
    probe_cooldown_s: float = 6 * 3600.0
    probe_conf: float = 0.5           # below this confidence, information pays
    probes_per_cycle: int = 1
    # Owner, 2026-08-21: "it's okay to get filled at reasonable prices."
    # When the touch sits at least join_edge_ticks INSIDE what the market
    # is worth (the Silver+evidence blend), joining it needs no quiet-book
    # proof — a fill there is a purchase at better than value, not a loss.
    # And the courtesy share cap lifts continuously with that same edge,
    # from share_hi up to share_max at four-plus ticks of edge. No edge
    # information (no model, no evidence) = the timid defaults stand.
    join_edge_ticks: float | None = None
    share_max: float = 0.10           # == share_hi means no lift
    # Growth investing (owner, 2026-08-21: "take the 75 cents per day as
    # a GOAL and if it's not doable at first, invest in the markets where
    # growth after building confidence is possible"). A market that can't
    # clear the goal at today's confidence, but WOULD at full confidence
    # (touch unlocked, full share cap, evidence-width bounds), gets a
    # starter position from its own budget. Its resting and its fills are
    # the evidence that grows the confidence that clears the goal.
    grow_usd: float = 0.0             # 0 = growth investing off
    grow_floor: float = 0.10          # a growth order must still earn this
    grow_pull_s: float = 1800.0       # under its floor this long -> out
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
    # Graduation (owner, 2026-08-21, the v1 pattern): a market whose
    # orders have MEASURED real accrual today moves off the search
    # ceiling onto the proven pool's own cap, so the search money keeps
    # hunting new candidates. Membership is recomputed from the sampler
    # every cycle — a market that stops accruing falls back in.
    graduate_paid_usd: float = 0.25   # measured $ accrued today to graduate
    proven_usd: float = 0.0           # 0 = graduation off
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
    live_ev: float | None = None
    live_share: float | None = None
    weak_since: float = 0.0   # measuring under the bar since (0 = fine)
    rest_noted: float = 0.0   # last time quiet resting was logged as evidence
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
        self.fairs = None      # callable(slug) -> model fair prob | None
        self.evidence = Evidence(clock=clock)
        self.fillmodel = FillModel()
        self.pending_marks: list[dict] = []   # fills awaiting their 1h grade
        self.proven: set[str] = set()         # graduated markets (main feeds it)
        self.inv_since: dict[str, float] = {}  # market -> first-fill ts
        self._exit_rate_ps = 0.0               # $/share/day our exits earn
        self.triage_feed: list[dict] = []     # the sweep's recent verdicts
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

    def enterable(self, slug: str) -> bool:
        toks = self.cfg.enter_tokens
        return toks is None or any(t in slug for t in toks)

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
        """The search ceiling's number: worst case of the UNGRADUATED
        book, negative risk netted per race group (v3/risk.py). Graduated
        markets sit outside it, under proven_spent's own cap."""
        return risk.book_risk(risk.order_legs(
            o for o in self.orders.values() if o.market not in self.proven))

    def proven_spent(self) -> float:
        return risk.book_risk(risk.order_legs(
            o for o in self.orders.values() if o.market in self.proven))

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
            # markets whose terms were NEVER read come first — a restart
            # must not send the rotation back to the top of the alphabet
            # while whole families (the Aug-20 seat-count arrivals) sit
            # unread at the bottom of it
            slugs = sorted(self.universe,
                           key=lambda s: (s in self.terms.current
                                          or s in self.known_dead, s))
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
        changes = self.terms.refresh(raw, sizes, now=now)
        # the store only keeps LIVE programs; a slug we asked about that
        # ends up without one was read-and-programless — dead ground until
        # a later read finds a program (the seat-count families read empty
        # on 2026-08-21 but were shown as "not read yet" forever)
        for slug in batch:
            if slug in self.terms.current:
                self.known_dead.discard(slug)
            else:
                self.known_dead.add(slug)
        for ch in changes:
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
                   own: FamilyOrder | None = None, bar: float | None = None,
                   full_confidence: bool = False,
                   cross_px: float | None = None) -> dict | None:
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
            if self.cfg.whole_shares:
                qty = float(math.ceil(qty))
            best = None
            r_lo, r_hi = self._price_bounds(
                slug, levels if side == "BUY" else other,
                other if side == "BUY" else levels, tick)
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
                k_r = round(abs(((levels[0][0]) if levels else px) - px) / tick)
                r_ctr = None
                if r_lo is not None and r_hi is not None:
                    r_ctr = (r_lo + r_hi) / 2.0
                else:
                    r_ctr = r_hi if r_hi is not None else r_lo
                conc_r = 0.0
                if r_ctr is not None:
                    past = (px - r_ctr) if side == "BUY" else (r_ctr - px)
                    conc_r = max(past / tick, 0.0)
                pf_r = self.fillmodel.p_fill(slug, side, k_r, target=target,
                                             bait=conc_r)
                fc_r = self.fillmodel.fill_cost(slug, side, px, r_ctr,
                                                exit_rate_ps=self._exit_rate_ps)
                ev = (est * self.fillmodel.scoring_fraction(slug)
                      - pf_r * fc_r * qty)
                if best is None or ev > best["ev"]:
                    best = {"side": side, "px": px, "qty": qty,
                            "share": round(j.share, 4), "est": round(est, 4),
                            "ev": round(ev, 4), "p_fill": round(pf_r, 4),
                            "fill_cost": round(fc_r, 4),
                            "cost": round(cost, 2), "revive": True,
                            "why": (f"the {side_name} side holds "
                                    f"{side_total:,.0f} of {target:,.0f} Target"
                                    f" Size and pays NOBODY — this order "
                                    f"revives it and takes ~"
                                    f"{j.share * 100:.0f}% of the side")}
            if best is not None and best["ev"] >= self.cfg.min_est_day:
                return best
            return None

        # -- the side qualifies: join or step back, never in front --
        touch = levels[0][0]
        # Every price level is an option (owner, 2026-08-21): the EV math
        # walks the whole in-window ladder and picks the best spot.
        # Joining an occupied level is safer than the distance alone
        # says — fills are first-come-first-served, so the shares already
        # resting there absorb takers before ours. That protection is
        # priced into the fill odds (the queue shield), not a rule.
        # One fair price per market, everything through EV (owner,
        # 2026-08-21): the band — Silver prior pulled by fills, quiet
        # rests, and sized touch anchors — gives a single fair estimate.
        # There is no hard wrong-side rule. Resting past fair pays the
        # concession inside fill_cost and raises the assumed fill speed
        # (bait); if the reward still clears the bar, it is +EV and
        # allowed — on either side, both, or neither.
        b_lo, b_hi = self._price_bounds(
            slug, levels if side == "BUY" else other,
            other if side == "BUY" else levels, tick)
        # heat (recent fills through our orders) is not a gate — the
        # owner, 2026-08-21: "Fine to try and place again with a small
        # size to see if the taker has moved on." It raises the assumed
        # fill odds everywhere in this market and shrinks the retry size
        # at the front; both fade as the fills age out.
        h = self.evidence.heat(slug)
        value_ctr = None
        if b_lo is not None and b_hi is not None:
            value_ctr = (b_lo + b_hi) / 2.0
        elif b_hi is not None:
            value_ctr = b_hi
        elif b_lo is not None:
            value_ctr = b_lo
        # Edge must come from INDEPENDENT information. The market's own
        # touches feed the band, so without a model or real fills the
        # band's center is just the spread's midpoint — and the touch must
        # not certify itself. The model counts in full; without it, edge
        # scales with fill-built confidence, continuously.
        if full_confidence:
            independence = 1.0
        elif self.fairs is not None and self.fairs(slug) is not None:
            independence = 1.0
        else:
            independence = self.evidence.confidence(slug)

        def edge_ticks(px: float) -> float:
            """How far inside independent value a fill at px is, in ticks."""
            if value_ctr is None or independence <= 0.0:
                return 0.0
            e = (value_ctr - px) if side == "BUY" else (px - value_ctr)
            return max(e / tick, 0.0) * independence

        rungs = tuple(range(0, 16))
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
        if other:
            # In FRONT of the touch is an option too (owner, 2026-08-21:
            # in a wide spread, a small order closer to the midpoint can
            # capture far more of the score, and a fill there may be a
            # bargain against fair value, not a cost). Post-only bounds
            # it one tick inside the other side's touch; the EV math
            # prices the rest — no queue ahead, bait-fast fill odds, and
            # the fill cost credits a fill below fair.
            for kf in (1, 2, 3, 5, 8, 12, 18, 25, 35, 50):
                px = round(touch + kf * sign * tick, 3)
                if not (0.001 <= px <= 0.999):
                    continue
                if (px - (other[0][0] - sign * tick)) * sign > 1e-9:
                    continue
                if px not in cands:
                    cands.append(px)
        elif self.cfg.allow_improve and not other:
            # College's launch quirk, kept on the owner's word: a book
            # with NO opposing quote at all has no value anchor, so the
            # in-front rungs stay short and size is clamped to probe
            # money (in the qty grid).
            for k in (1, 5, 10):
                px = round(touch + k * sign * tick, 3)
                if not (0.001 <= px <= 0.999):
                    continue
                if (px - (touch + sign * 10 * tick)) * sign > 1e-9:
                    continue
                if px not in cands:
                    cands.append(px)
            budget = min(budget, 0.05)
        # Every candidate is priced by the owner's EV formula
        # (2026-08-19): what it earns while resting, minus what a fill
        # would probably cost.
        #     EV/day = est x scoring_fraction - p(fill) x fill_cost x size
        # Fill odds are learned per distance bucket from every touch move;
        # fill cost is the calibrated adverse markdown plus anything
        # conceded past value; depth ahead of the price shields the odds.
        if cross_px is not None:
            # our own opposite-side order rests at cross_px: stay a full
            # tick clear so the pair can never cross (post-only would
            # bounce the second placement)
            cands = [px for px in cands
                     if (px - (cross_px - sign * tick)) * sign <= 1e-9]
        sf = self.fillmodel.scoring_fraction(slug)
        exit_rate_ps = self._exit_rate_ps
        grid = (tuple(q for q in QTY_GRID if q >= 1.0)
                if self.cfg.whole_shares else QTY_GRID)
        pick, solo = None, None
        for px in cands:
            cost_ps = px if side == "BUY" else 1.0 - px
            in_front = (px - touch) * sign > 1e-9
            k_px = 0 if in_front else round(abs(touch - px) / tick)
            shield = sum(q for p2, q in levels
                         if (p2 - px) * sign > 1e-9)
            queue = sum(q for p2, q in levels if abs(p2 - px) <= 1e-9)
            if (own is not None and own.side == side
                    and abs(own.price - px) <= 1e-9):
                queue = max(queue - own.qty, 0.0)
            shield += queue
            conc = 0.0
            if value_ctr is not None:
                past = (px - value_ctr) if side == "BUY" else (value_ctr - px)
                conc = max(past / tick, 0.0)
            if in_front and independence < 1.0:
                # with no independent sense of fair value, ticks in
                # front of the touch are assumed to be a gift to takers;
                # a model or fill-built confidence waives that in
                # proportion (owner, 2026-08-21: a 35c bid on a 50c-fair
                # market is a bargain for US, however far in front)
                conc = max(conc, (abs(px - touch) / tick)
                           * (1.0 - independence))
            pf = self.fillmodel.p_fill(slug, side, k_px, shield=shield,
                                       target=target, bait=conc + h)
            fcost = self.fillmodel.fill_cost(slug, side, px, value_ctr,
                                             exit_rate_ps=exit_rate_ps)
            for qty in grid:
                if (h >= 0.5 and qty > grid[0]
                        and (in_front or k_px == 0)):
                    break     # a fill just happened here: minimum size
                if qty * cost_ps > budget + 1e-9:
                    break
                j = estimate_join(side, levels, tick, df, target, px, qty)
                if not (j.qualifies and j.in_window):
                    break
                est = j.share * side_pool
                ev = est * sf - pf * fcost * qty
                k = k_px
                kf = round(abs(px - touch) / tick)
                row = {"side": side, "px": px, "qty": qty,
                       "share": round(j.share, 4), "est": round(est, 4),
                       "ev": round(ev, 4), "p_fill": round(pf, 4),
                       "fill_cost": round(fcost, 4),
                       "cost": round(qty * cost_ps, 2),
                       "why": (f"at the touch — a fill here is "
                               f"{edge_ticks(px):.0f} ticks inside value "
                               f"({'Silver + evidence' if independence >= 1.0 else f'evidence band only, confidence {independence:.0%}'})"
                               if k == 0 and not in_front
                               and edge_ticks(px) >= 1 else
                               "joins the touch — the book has been quiet"
                               if k == 0 and not in_front else
                               f"{kf} tick{'s' if kf != 1 else ''} in front "
                               f"of the touch — closer to the midpoint, "
                               f"~{j.share * 100:.1f}% of the {side_name} side"
                               if in_front else
                               f"{k} tick{'s' if k != 1 else ''} behind the "
                               f"touch, ~{j.share * 100:.1f}% of the "
                               f"{side_name} side")}
                lift = 1.0 if full_confidence else min(edge_ticks(px) / 4.0, 1.0)
                eff_cap = (self.cfg.share_hi
                           + (max(self.cfg.share_max, self.cfg.share_hi)
                              - self.cfg.share_hi) * lift)
                if j.share > eff_cap:
                    # louder than the (edge-lifted) courtesy band:
                    # acceptable only as a minimum-size solo in front of a
                    # wall (college)
                    if in_front and qty == grid[0]:
                        if solo is None or ev > solo["ev"] + 1e-9:
                            solo = {**row, "solo": True}
                    break
                if pick is None or ev > pick["ev"] + 1e-9:
                    pick = row
        the_bar = self.cfg.min_est_day if bar is None else bar
        if pick is not None and pick["ev"] >= the_bar:
            return pick
        if solo is not None and solo["ev"] >= the_bar:
            return solo
        return None

    def _band(self, slug: str, bids, asks, tick: float) -> dict | None:
        """The evidence band for a market: Silver as prior when it prices
        it, real touches (levels holding at least 5 shares — smaller is
        bait, 1.0's rule) as anchors, WEIGHTED BY THEIR SIZE — a
        million-share wall testifies harder than a token quote."""
        fair = self.fairs(slug) if self.fairs is not None else None
        bt = next(((p, q) for p, q in (bids or ()) if q >= 5.0), (None, None))
        at = next(((p, q) for p, q in (asks or ()) if q >= 5.0), (None, None))
        return self.evidence.band(slug, prior_fair=fair,
                                  touches=(bt[0], at[0]),
                                  touch_sizes=(bt[1], at[1]))

    def _price_bounds(self, slug: str, bids, asks,
                      tick: float) -> tuple[float | None, float | None]:
        """(lo, hi) price bounds in DOLLARS for resting, or Nones.

        No thresholds (owner, 2026-08-21: "I don't want hard and fast
        rules. I want confidence values that learned over time"). The
        bound is a continuous blend: it sits ON the Silver model when the
        evidence has earned nothing, and slides toward the evidence
        band's edge exactly as far as the evidence's confidence — built
        by real fills, amplified by a tight band, decayed by time — has
        earned. One fresh fill moves it some; a run of fills moves it
        most of the way; a quiet week slides it back toward the model.
        With no model the band stands alone; with neither, no bound."""
        band = self._band(slug, bids, asks, tick)
        fair = self.fairs(slug) if self.fairs is not None else None
        lo = band["lo"] / 100.0 if band else None
        hi = band["hi"] / 100.0 if band else None
        if fair is None:
            return lo, hi
        if band is None:
            return fair, fair
        c = self.evidence.confidence(slug, band)
        return (fair + c * (lo - fair), fair + c * (hi - fair))

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

        def plan_pair(bar=None):
            a = self._plan_side(slug, book, "BUY", prog, side_pool,
                                budget, bar=bar)
            b = self._plan_side(slug, book, "SELL", prog, side_pool,
                                budget, bar=bar)
            if a and b and a["px"] >= b["px"] - 1e-9:
                if a["ev"] >= b["ev"]:
                    b = self._plan_side(slug, book, "SELL", prog, side_pool,
                                        budget, bar=bar, cross_px=a["px"])
                else:
                    a = self._plan_side(slug, book, "BUY", prog, side_pool,
                                        budget, bar=bar, cross_px=b["px"])
            return [p for p in (a, b) if p]

        out = plan_pair()
        grow: list[dict] = []
        potential = 0.0
        if not out and self.cfg.grow_usd > 0:
            for side in ("BUY", "SELL"):
                fp = self._plan_side(slug, book, side, prog, side_pool,
                                     budget, full_confidence=True)
                if fp:
                    potential = max(potential, fp["ev"])
            if potential >= self.cfg.min_est_day:
                for gp in plan_pair(bar=self.cfg.grow_floor):
                    gp["grow"] = True
                    gp["why"] = (
                        f"under the {self.cfg.min_est_day * 100:.0f}c "
                        f"goal today (${gp['ev']:.2f}/day) but worth "
                        f"${potential:.2f} at full confidence — "
                        f"investing to build the evidence")
                    grow.append(gp)
        if not out:
            why = ("nothing here clears the bar: both sides either pay "
                   f"under {self.cfg.min_est_day * 100:.0f}c/day, are louder "
                   "than the courtesy band, or don't qualify")
        return out, why, grow, round(potential, 4)

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
            self.evidence.order_gone(rec.market, oid, now=now)
            del self.orders[oid]
        for m in tracked:
            if m in positions:
                self.positions_seen[m] = positions[m][0]
        for m in list(self.positions_seen):
            if (m not in self.inventory
                    and m not in {o.market for o in self.orders.values()}):
                self.positions_seen.pop(m, None)

    def _on_fill(self, rec: FamilyOrder, filled: float, now: float) -> None:
        if rec.market not in self.inventory:
            self.inv_since[rec.market] = now
        inv = self.inventory.setdefault(rec.market, {"qty": 0.0, "cost": 0.0})
        if rec.side == "BUY":
            inv["qty"] += filled
            inv["cost"] += filled * rec.price
        else:
            inv["qty"] -= filled
            inv["cost"] -= filled * rec.price
        if abs(inv["qty"]) < 0.005:
            self.inventory.pop(rec.market, None)
            since = self.inv_since.pop(rec.market, None)
            if since is not None and now > since:
                self.fillmodel.observe_offload(rec.market,
                                               (now - since) / 86400.0)
        self.evidence.fill(rec.market, rec.side, rec.price, ts=now)
        self.fillmodel.observe_fill_age(rec.market, now - rec.placed_ts)
        self.pending_marks.append({"market": rec.market, "side": rec.side,
                                   "price": rec.price, "due": now + 3600.0})
        del self.pending_marks[:-60]
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
            if rec.purpose in ("sell", "manual"):
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
        stock = sum(abs(v.get("qty") or 0.0) for v in self.inventory.values())
        stock_rate = sum(o.live_est or 0.0 for o in self.orders.values()
                         if o.purpose == "sell")
        self._exit_rate_ps = (stock_rate / stock) if stock > 0.01 else 0.0
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
            return self._finish(summary, now)
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
            return self._finish(summary, now)
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
            return self._finish(summary, now)

        # grade fills that have had their hour: the adverse move a fill
        # actually cost is the calibration everything else leans on
        for mk in list(self.pending_marks):
            if now < mk["due"]:
                continue
            book_m = self.cache.fresh(mk["market"], self.cfg.read_age_s, now)
            if book_m is None:
                if now > mk["due"] + 4 * 3600.0:
                    self.pending_marks.remove(mk)   # too stale to grade honestly
                continue
            if book_m.bids and book_m.asks:
                mid = (book_m.bids[0][0] + book_m.asks[0][0]) / 2.0
                adverse = self.fillmodel.observe_fill_mark(
                    mk["market"], mk["side"], mk["price"], mid)
                self._log(event="fill_graded", market=mk["market"],
                          why=f"cost {adverse * 100:.1f}c/share vs the "
                              f"mid an hour on")
            self.pending_marks.remove(mk)

        # 0) zombies from a failed cancel: retry until they die
        for rec in list(self.orders.values()):
            if rec.why == "cancel failed during a move — retrying":
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    self._log(event="zombie_cancelled", market=rec.market,
                              id=rec.id)
                    del self.orders[rec.id]

        # 1) leave dead or near-resolution markets ENTIRELY (exits included)
        for rec in list(self.orders.values()):
            if actions <= 0:
                break
            days = slug_days_out(rec.market, now)
            near = days is not None and days < self.cfg.min_days_out
            dead = self._dead_here(rec.market)
            out_of_scope = (rec.purpose != "sell"
                            and not self.enterable(rec.market))
            if dead or ((near or out_of_scope) and rec.purpose != "sell"):
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    why = ("program pays nothing" if dead
                           else "outside the families you chose"
                           if out_of_scope else "resolves soon")
                    self._log(event="exit", market=rec.market, why=why, id=rec.id)
                    del self.orders[rec.id]
                    actions -= 1

        # 2) maintenance: reprice or pull against fresh books
        actions = self._maintain(now, actions)

        # 3) the ceiling is enforced, not just checked at the door: over
        # it (reprices once grew orders past it), the worst value per
        # dollar goes first until the book fits
        actions = self._trim(now, actions)

        # 4) the seller next — getting the owner OUT always outranks new
        # risk (starving it behind entries left shorts uncovered, 23:53Z)
        actions = self._sell(now, actions)

        # 5) probes: buy information where it is missing
        actions = self._probe(now, positions, actions)

        # 6) new entries, best scoreboard candidates first
        actions = self._enter(now, positions, actions)

        # 7) growth: seed the markets whose goal needs confidence first
        self._grow(now, positions, actions)
        return self._finish(summary, now)

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
            self.fillmodel.observe_order_age(rec.market, now - rec.placed_ts,
                                             60.0)
            if rec.purpose not in ("sell", "probe"):
                ticks_now = (round(abs(lv[0][0] - rec.price) / book.tick)
                             if lv else 0)
                shield_now = sum(q for p2, q in lv
                                 if (p2 - rec.price)
                                 * (1.0 if rec.side == "BUY" else -1.0) > 1e-9)
                shield_now += max(sum(q for p2, q in lv
                                      if abs(p2 - rec.price) <= 1e-9)
                                  - rec.qty, 0.0)
                pf_now = self.fillmodel.p_fill(rec.market, rec.side, ticks_now,
                                               shield=shield_now,
                                               target=float(prog.target))
                fc_now = self.fillmodel.fill_cost(rec.market, rec.side,
                                                  rec.price, None)
                rec.live_ev = round(
                    rec.live_est * self.fillmodel.scoring_fraction(rec.market)
                    - pf_now * fc_now * rec.qty, 4)
                self.fillmodel.observe_scoring(rec.market,
                                               j.qualifies and j.in_window)
                self.fillmodel.observe_approach(rec.market, rec.side,
                                                ticks_now, 60.0,
                                                rec.live_est or 0.0)
            if rec.purpose != "sell" and now - rec.rest_noted > 1800.0:
                rec.rest_noted = now
                self.evidence.rest_mark(rec.market, rec.id, rec.side,
                                        rec.price, rec.placed_ts, now=now)
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
            if (self.cfg.whole_shares
                    and rec.purpose not in ("sell", "manual")
                    and abs(rec.qty - round(rec.qty)) > 1e-9):
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    self.orders.pop(rec.id, None)
                    self.evidence.order_gone(rec.market, rec.id)
                    self._log(event="whole_shares_cull", market=rec.market,
                              price=rec.price, qty=rec.qty,
                              note="fractional size retired — politics "
                                   "quotes whole shares now")
                    actions -= 1
                continue
            if rec.purpose in ("sell", "probe", "manual"):
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
                                   self.cfg.per_market_usd / 2.0, own=rec,
                                   bar=(self.cfg.grow_floor
                                        if rec.purpose == "grow" else None))
            drifted = ((rec.live_share or 0.0) > self.cfg.drift_share
                       and rec.purpose not in ("revive", "solo"))
            gain = (best["est"] if best else 0.0) - (rec.live_est or 0.0)
            measured = rec.live_ev if rec.live_ev is not None else rec.live_est
            floor_here = (self.cfg.grow_floor if rec.purpose == "grow"
                          else self.cfg.min_est_day)
            below = measured is not None and measured < floor_here
            if below and not rec.weak_since:
                rec.weak_since = now
            elif not below:
                rec.weak_since = 0.0
            window_here = (self.cfg.grow_pull_s if rec.purpose == "grow"
                           else self.cfg.weak_pull_s)
            weak = (window_here > 0 and rec.weak_since
                    and now - rec.weak_since > window_here
                    and (best is None
                         or best.get("ev", best["est"]) < floor_here))
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
                         or abs(best["qty"] - rec.qty) > 1e-9)
                    # a reprice that GROWS the order answers to the same
                    # ceiling as a new entry (the $121.99-of-$100 lesson)
                    and (self.family_spent()
                         - capital_at_risk(rec.intent, rec.price, rec.qty)
                         + capital_at_risk(rec.intent, best["px"], best["qty"])
                         <= self.cfg.capital_usd + 1e-9)):
                r = self.desk.reprice(
                    {"id": rec.id, "market": rec.market, "side": rec.side,
                     "price": rec.price, "size": rec.qty, "intent": rec.intent},
                    best["px"], new_qty=best["qty"])
                if r.ok:
                    self._log(event="reprice", market=rec.market, side=rec.side,
                              frm=rec.price, to=best["px"], qty=best["qty"])
                    if r.two_orders:
                        # the original REFUSED to cancel and still rests.
                        # It stays tracked — its collateral is real, the
                        # ceiling must see it — and the cancel is retried
                        # every cycle until it dies (owner, 2026-08-21: no
                        # ghosts left behind after a move).
                        rec.why = "cancel failed during a move — retrying"
                        self.alert(f"{self.cfg.tag}: two orders resting",
                                   f"{self._label(rec.market)}: the original "
                                   f"would not cancel during a move; holding "
                                   f"both and retrying the cancel")
                    else:
                        del self.orders[rec.id]
                    new_purpose = ("revive" if best.get("revive")
                                   else "solo" if best.get("solo")
                                   else "grow" if (rec.purpose == "grow"
                                   and best.get("ev", best["est"])
                                   < self.cfg.min_est_day)
                                   else "earn")
                    self.orders[r.order_id] = FamilyOrder(
                        id=r.order_id, market=rec.market, side=rec.side,
                        price=best["px"], qty=best["qty"], intent=rec.intent,
                        placed_ts=now, purpose=new_purpose,
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
            if not self.enterable(slug):
                continue
            days = slug_days_out(slug, now)
            if days is not None and days < self.cfg.min_days_out:
                continue
            for plan in sb["plans"]:
                if actions <= 0:
                    break
                if plan.get("ev", plan["est"]) < self.cfg.min_est_day:
                    continue    # under the bar (old plans lack ev: use est)
                if (slug, plan["side"]) in have:
                    continue
                if not self._cooldown_ok(slug, plan["side"], now):
                    continue
                if self.market_spent(slug) + plan["cost"] \
                        > self.cfg.per_market_usd + 1e-9 \
                        and not plan.get("revive"):
                    continue
                guess = BUY_LONG if plan["side"] == "BUY" else BUY_SHORT
                if slug in self.proven and self.cfg.proven_usd > 0:
                    pool_orders = [o for o in self.orders.values()
                                   if o.market in self.proven]
                    if self.proven_spent() + risk.marginal(
                            pool_orders, slug, guess,
                            plan["px"], plan["qty"]) \
                            > self.cfg.proven_usd + 1e-9:
                        continue      # the proven pool has its own cap
                else:
                    search_orders = [o for o in self.orders.values()
                                     if o.market not in self.proven]
                    if self.family_spent() + risk.marginal(
                            search_orders, slug, guess,
                            plan["px"], plan["qty"]) \
                            > self.cfg.capital_usd + 1e-9:
                        continue      # the search ceiling — it binds
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

    def _trim(self, now: float, actions: int) -> int:
        while actions > 0:
            spent = self.family_spent()
            if spent <= self.cfg.capital_usd + 1e-9:
                break
            cands = [o for o in self.orders.values() if o.purpose != "sell"]
            if not cands:
                break
            def value_per_dollar(o):
                est = (o.live_est if o.live_est is not None else o.est_day) or 0.0
                return est / max(capital_at_risk(o.intent, o.price, o.qty), 0.01)
            worst = min(cands, key=value_per_dollar)
            r = self.desk.cancel(worst.id, worst.market)
            if not r.ok:
                break
            freed = capital_at_risk(worst.intent, worst.price, worst.qty)
            self._log(event="trim", market=worst.market, side=worst.side,
                      why=(f"${spent:.2f} on the book is over the "
                           f"${self.cfg.capital_usd:.0f} ceiling — freeing "
                           f"${freed:.2f} from the lowest earner"))
            del self.orders[worst.id]
            actions -= 1
        return actions

    def _grow(self, now: float, positions: dict, actions: int) -> int:
        if self.cfg.grow_usd <= 0 or actions <= 0:
            return actions
        spent = sum(capital_at_risk(o.intent, o.price, o.qty)
                    for o in self.orders.values() if o.purpose == "grow")
        have = {(o.market, o.side) for o in self.orders.values()
                if o.purpose != "sell"}
        ranked = sorted(((s, sb) for s, sb in self.scoreboard.items()
                         if sb.get("grow")),
                        key=lambda kv: -(kv[1].get("potential") or 0.0))
        for slug, sb in ranked:
            if actions <= 0 or spent >= self.cfg.grow_usd - 1e-9:
                break
            if slug not in self.universe or self._dead_here(slug) \
                    or not self.enterable(slug):
                continue
            days = slug_days_out(slug, now)
            if days is not None and days < self.cfg.min_days_out:
                continue
            for plan in sb["grow"]:
                if actions <= 0 or spent + plan["cost"] > self.cfg.grow_usd + 1e-9:
                    break
                if (slug, plan["side"]) in have:
                    continue
                if not self._cooldown_ok(slug, plan["side"], now):
                    continue
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
                        placed_ts=now, purpose="grow", why=plan["why"],
                        est_day=plan["est"], share=plan["share"])
                    self._log(event="grow", market=slug, side=plan["side"],
                              price=plan["px"], qty=plan["qty"],
                              why=plan["why"][:80])
                    self._mark(slug, plan["side"], now)
                    spent += plan["cost"]
                    actions -= 1
        return actions

    def _maybe_move_exit(self, slug: str, side: str, mine: list, book,
                         inv: dict, now: float) -> None:
        """A single resting exit in a clearly worse slot moves to the
        better one. Cancel-first on purpose: placing the replacement
        before cancelling would briefly offer MORE than the position
        holds, and that extra could fill. Ladders of several exits are
        left alone — moving them wholesale would churn the adopted
        book."""
        if len(mine) != 1:
            return
        rec = mine[0]
        qty = inv.get("qty") or 0.0
        if not self._cooldown_ok(slug, side, now):
            return
        if side == "SELL":
            break_even = min(max(inv.get("cost", 0.0) / qty, 0.001), 0.989)
            lo = max(break_even + book.tick,
                     (book.bids[0][0] + book.tick) if book.bids else 0.002)
            hi = max((book.asks[0][0] if book.asks
                      else break_even + book.tick), lo)
        else:
            received = min(max(-inv.get("cost", 0.0) / -qty, 0.002), 0.999)
            hi = min(received - book.tick,
                     (book.asks[0][0] - book.tick) if book.asks
                     else received - book.tick)
            lo = min((book.bids[0][0] if book.bids else hi), hi)
        best = self._best_exit_px(slug, side, book, lo, hi, rec.qty)
        if best is None or abs(best - rec.price) < book.tick / 2:
            return
        prog, _w = self._prog_row(slug)
        side_pool = self._side_pool(slug, prog) if prog is not None else None
        if prog is None or side_pool is None:
            return
        levels = [(p, q) for p, q in book.side(side) if q > 1e-9]
        j = estimate_join(side, levels, book.tick, float(prog.df),
                          float(prog.target), best, rec.qty)
        best_est = (j.share * side_pool
                    if j.qualifies and j.in_window else 0.0)
        cur_est = rec.live_est or 0.0
        if best_est < cur_est * 1.5 + 0.05:
            return                      # not clearly better — stay put
        r = self.desk.cancel(rec.id, rec.market)
        if r.ok:
            self.orders.pop(rec.id, None)
            self.evidence.order_gone(rec.market, rec.id)
            self._log(event="exit_moved", market=slug, price=rec.price,
                      qty=rec.qty,
                      note=f"a slot at {best:.2f} earns more — moving")

    def _best_exit_px(self, slug: str, side: str, book, lo: float,
                      hi: float, qty: float) -> float:
        """The exit slot that EARNS the most among prices that still
        profit (owner, 2026-08-21: the MN example — don't pile onto a
        crowded touch next to a wall when an open slot a few cents
        lower earns more, and a fill there is still profit plus buying
        power back). Tie goes to the price nearer the other side, which
        fills sooner."""
        lo, hi = round(lo, 3), round(hi, 3)
        if hi < lo:
            return hi
        prog, _w = self._prog_row(slug)
        side_pool = self._side_pool(slug, prog) if prog is not None else None
        if prog is None:
            return hi if side == "SELL" else lo
        levels = [(p, q) for p, q in book.side(side) if q > 1e-9]
        n = int(round((hi - lo) / book.tick)) + 1
        step = max(1, n // 24)            # sample big ranges, walk small
        cands = [round(lo + i * book.tick, 3) for i in range(0, n, step)]
        if cands[-1] != hi:
            cands.append(hi)
        best_px, best_key = None, None
        for px in cands:
            j = estimate_join(side, levels, book.tick, float(prog.df),
                              float(prog.target), px, qty)
            est = (j.share * side_pool
                   if side_pool is not None and j.qualifies and j.in_window
                   else 0.0)
            # nearer the other side breaks ties: it fills sooner, and an
            # exit fill is profit plus buying power back
            near = -px if side == "SELL" else px
            key = (round(est, 4), near)
            if best_key is None or key > best_key:
                best_px, best_key = px, key
        return best_px if best_px is not None else (hi if side == "SELL" else lo)

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
                mine = [o for o in self.orders.values()
                        if o.market == slug and o.purpose == "sell"
                        and o.side == "SELL"]
                self._maybe_move_exit(slug, "SELL", mine, book, inv, now)
                covered = sum(o.qty for o in self.orders.values()
                              if o.market == slug and o.purpose == "sell"
                              and o.side == "SELL")
                rest = qty - covered
                if rest < 0.01 or not self._cooldown_ok(slug, "SELL", now):
                    continue
                break_even = min(max(inv.get("cost", 0.0) / qty, 0.001), 0.989)
                ask_touch = (book.asks[0][0] if book.asks
                             else break_even + book.tick)
                lo = max(break_even + book.tick,
                         (book.bids[0][0] + book.tick) if book.bids
                         else 0.002)
                px = self._best_exit_px(slug, "SELL", book, lo,
                                        max(ask_touch, lo), rest)
                px = min(max(px, 0.002), 0.999)
                side, intent, rest_qty = "SELL", SELL_LONG, rest
                why = "selling filled stock — it earns while it waits"
            else:
                # a SHORT: buy it back at the bid touch, never above
                # break-even — the bid earns rewards while it exits and
                # adds no collateral (owner, 2026-08-20: "try and exit
                # positions in a way that earns liquidity reward")
                mine = [o for o in self.orders.values()
                        if o.market == slug and o.purpose == "sell"
                        and o.side == "BUY"]
                self._maybe_move_exit(slug, "BUY", mine, book, inv, now)
                covered = sum(o.qty for o in self.orders.values()
                              if o.market == slug and o.purpose == "sell"
                              and o.side == "BUY")
                rest = -qty - covered
                if rest < 0.01 or not self._cooldown_ok(slug, "BUY", now):
                    continue
                received = min(max(-inv.get("cost", 0.0) / -qty, 0.002), 0.999)
                bid_touch = (book.bids[0][0] if book.bids
                             else received - book.tick)
                hi = min(received - book.tick,
                         (book.asks[0][0] - book.tick) if book.asks
                         else received - book.tick)
                px = self._best_exit_px(slug, "BUY", book,
                                        min(bid_touch, hi), hi, rest)
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

    def _probe(self, now: float, positions: dict, actions: int) -> int:
        if self.cfg.probe_usd <= 0 or actions <= 0:
            return actions
        spent = sum(capital_at_risk(o.intent, o.price, o.qty)
                    for o in self.orders.values() if o.purpose == "probe")
        placed = 0
        for slug, sb in sorted(self.scoreboard.items(),
                               key=lambda kv: -(kv[1].get("pool_day") or 0.0)):
            if actions <= 0 or placed >= self.cfg.probes_per_cycle:
                break
            if spent >= self.cfg.probe_usd - 1e-9:
                break
            if not self.enterable(slug) or self._dead_here(slug):
                continue
            prog, _w = self._prog_row(slug)
            if prog is None:
                continue
            side_pool = self._side_pool(slug, prog)
            if side_pool is None or side_pool < self.cfg.min_est_day:
                continue      # even owning the side couldn't pay the bar
            if sb.get("plans"):
                continue      # the planner can already act — no probe needed
            band = self.evidence.band(
                slug, prior_fair=self.fairs(slug) if self.fairs else None)
            if self.evidence.confidence(slug, band) >= self.cfg.probe_conf:
                continue      # we already know enough here
            if now - self.last_action.get(f"{slug}|probe", 0.0) \
                    < self.cfg.probe_cooldown_s:
                continue
            if any(o.market == slug and o.purpose == "probe"
                   for o in self.orders.values()):
                continue
            book = self.cache.fresh(slug, BOOK_MAX_AGE, now)
            if book is None or not book.bids:
                continue
            # aim the scout at the least-observed fill-odds bucket
            # (owner, 2026-08-19: "we won't get a full picture of the odds
            # if we just stick on the safe side")
            from .fillmodel import DIST_BUCKETS, family_of
            fam_k = family_of(slug)
            def bucket_hours(b):
                cell = self.fillmodel.obs.get(
                    self.fillmodel._key(fam_k, "BUY", b))
                return (cell or [0.0])[0]
            k_probe = min(DIST_BUCKETS, key=bucket_hours)
            px = round(book.bids[0][0] - k_probe * book.tick, 3)
            _lo, hi = self._price_bounds(slug, book.bids, book.asks, book.tick)
            if hi is not None:
                px = min(px, round(hi, 3))
            if not (0.001 <= px <= 0.6):
                continue      # 1.0's rule: probes buy cheap or not at all
            r = self.desk.place_resting(slug, "BUY", px, self.cfg.probe_qty,
                                        net_position=(positions.get(slug)
                                                      or (0.0,))[0],
                                        verify=self.cfg.verify_resting)
            if r.ok and r.order_id:
                self.orders[r.order_id] = FamilyOrder(
                    id=r.order_id, market=slug, side="BUY", price=px,
                    qty=self.cfg.probe_qty, intent=r.intent, placed_ts=now,
                    purpose="probe",
                    why=("a scout — this market's pool could pay, but I "
                         "don't know enough yet; what happens to this "
                         "share IS the information"))
                self._log(event="probe", market=slug, price=px)
                self.last_action[f"{slug}|probe"] = now
                spent += capital_at_risk(r.intent, px, self.cfg.probe_qty)
                placed += 1
                actions -= 1
        # rotation: a scout that sat its full watch has reported in
        for rec in list(self.orders.values()):
            if rec.purpose != "probe":
                continue
            if now - rec.placed_ts >= self.cfg.probe_ttl_s:
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    self.evidence.rest_mark(rec.market, rec.id, rec.side,
                                            rec.price, rec.placed_ts, now=now)
                    self.evidence.order_gone(rec.market, rec.id, now=now)
                    self._log(event="probe_done", market=rec.market,
                              why="sat its watch untouched — noted")
                    del self.orders[rec.id]
        return actions

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
                and self.enterable(s)
                and now - (self.scoreboard.get(s) or {}).get("ts", 0.0)
                > self.cfg.rescan_s]

        def triage(s: str) -> float:
            """Rapid triage (owner, 2026-08-21): mispriced markets and big
            spreads first, using whatever is already known — the model's
            distance from the last seen touch, the spread's width, the
            payout record. A market never seen at all scores a flat
            curiosity bonus so first looks keep happening."""
            score = min(self.history.get(s, 0.0), 5.0)
            b2 = self.cache.any_age(s)
            if b2 is None:
                return score + 1.0
            bb2 = b2.bids[0][0] if b2.bids else None
            ba2 = b2.asks[0][0] if b2.asks else None
            if bb2 is not None and ba2 is not None:
                score += min((ba2 - bb2) * 100.0 / 2.0, 10.0)   # spread, cents
                fair2 = self.fairs(s) if self.fairs is not None else None
                if fair2 is not None:
                    mid2 = (bb2 + ba2) / 2.0
                    score += min(abs(mid2 - fair2) * 100.0, 20.0)  # mispricing
            return score

        idle.sort(key=lambda s: (-triage(s),
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
            plans, why, grow, potential = self.plan_market(book, slug)
            prog2, _ = self._prog_row(slug)
            sp2 = self._side_pool(slug, prog2) if prog2 else None
            conf2 = self.evidence.confidence(slug)
            self.scoreboard[slug] = {
                "ts": now, "plans": plans, "why": why,
                "grow": grow, "potential": potential,
                "est": round(sum(p["est"] for p in plans), 4),
                "pool_day": round(sp2, 4) if sp2 is not None else None,
                "conf": conf2}
            # the sweep's verdict, for the live triage feed on the page
            spread_c = (round((book.asks[0][0] - book.bids[0][0]) * 100, 1)
                        if book.bids and book.asks else None)
            best_ev = (max(p.get("ev", p["est"]) for p in plans)
                       if plans else (potential if grow else 0.0))
            self.triage_feed.append({
                "ts": round(now, 1), "market": slug,
                "in": bool(plans or grow),
                "ev": round(best_ev, 2), "spread": spread_c,
                "pool": round(sp2, 2) if sp2 is not None else None,
                "conf": round(conf2, 2),
                "why": (plans[0]["why"][:60] if plans
                        else grow[0]["why"][:60] if grow
                        else (why or "")[:60])})
            del self.triage_feed[:-40]
            done += 1
        # the free pass: re-plan from cached books, no fetches spent
        if self.cfg.replan_s > 0:
            fresh_idle = [s for s in self.universe
                          if s not in self.active_markets()
                          and self.enterable(s)
                          and not self._dead_here(s)
                          and now - (self.scoreboard.get(s) or {}).get("ts", 0.0)
                          > self.cfg.replan_s
                          and self.cache.fresh(s, BOOK_MAX_AGE, now) is not None]
            fresh_idle.sort(key=lambda s: (self.scoreboard.get(s) or {}).get("ts", 0.0))
            for slug in fresh_idle[:self.cfg.replans_per_cycle]:
                prog3, _w3 = self._prog_row(slug)
                if prog3 is None:
                    continue
                book3 = self.cache.fresh(slug, BOOK_MAX_AGE, now)
                plans, why, grow, potential = self.plan_market(book3, slug)
                sp3 = self._side_pool(slug, prog3)
                conf3 = self.evidence.confidence(slug)
                self.scoreboard[slug] = {
                    "ts": now, "plans": plans, "why": why,
                    "grow": grow, "potential": potential,
                    "est": round(sum(p["est"] for p in plans), 4),
                    "pool_day": round(sp3, 4) if sp3 is not None else None,
                    "conf": conf3}
                spread3 = (round((book3.asks[0][0] - book3.bids[0][0]) * 100, 1)
                           if book3.bids and book3.asks else None)
                best3 = (max(p.get("ev", p["est"]) for p in plans)
                         if plans else (potential if grow else 0.0))
                self.triage_feed.append({
                    "ts": round(now, 1), "market": slug,
                    "in": bool(plans or grow),
                    "ev": round(best3, 2), "spread": spread3,
                    "pool": round(sp3, 2) if sp3 is not None else None,
                    "conf": round(conf3, 2),
                    "why": (plans[0]["why"][:60] if plans
                            else grow[0]["why"][:60] if grow
                            else (why or "")[:60])})
                del self.triage_feed[:-40]
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

    def _finish(self, summary: dict, now: float) -> dict:
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
        # the triage sweep's progress: how much of the eligible board —
        # in scope, carrying a live program — has a current score
        elig = [s for s in self.universe
                if self.enterable(s) and s in self.terms.current
                and not self._dead_here(s)]
        done = sum(1 for s in elig
                   if now - (self.scoreboard.get(s) or {}).get("ts", 0.0)
                   <= self.cfg.rescan_s)
        summary["triage"] = {"total": len(elig), "done": done,
                             "per_cycle": max(self.cfg.scan_reserve, 1)}
        summary["triage_feed"] = self.triage_feed[-16:]
        top = sorted(((s, sb) for s, sb in self.scoreboard.items()
                      if sb.get("plans")),
                     key=lambda kv: -(kv[1].get("est") or 0.0))[:12]
        summary["best_idle"] = [
            {"market": s, "name": self._label(s), "est": sb.get("est"),
             "hist": self.history.get(s), "conf": sb.get("conf"),
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
            "inv_since": self.inv_since,
            "fillmodel": self.fillmodel.to_dict(),
            "pending_marks": self.pending_marks[-60:],
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
        self.inv_since = dict(d.get("inv_since") or {})
        if d.get("fillmodel"):
            self.fillmodel = FillModel.from_dict(d["fillmodel"])
        self.pending_marks = list(d.get("pending_marks") or [])
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
