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
from dataclasses import asdict, dataclass, field
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
PAGE_LOSS_USD = 1.0    # only losses bigger than this reach the phone
PAGE_SETTLE_S = 20.0   # let the book settle before marking an open
GONE_GRACE_S = 300.0   # a vanished order waits this long for the lagging
                       # position feed before it counts as a silent cancel

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
    # Size the chosen join up to the per-market money even when the
    # fill-cost term prefers dust (owner, 2026-08-23, NBA: "increase
    # the amounts... they are so small that they aren't earning
    # anything" — stability comes from the wall's queue, not tiny size,
    # and "obviously we'll get filled occasionally" is accepted).
    wall_size_up: bool = False
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
    # holdings count against the family ceiling at liquidation value
    # (owner, 2026-08-21: cfb risk = orders + holdings, capped)
    holdings_in_ceiling: bool = False
    # graduated markets may carry more money than searchers
    proven_per_market_usd: float | None = None
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
    graduate_paid_usd: float = 0.25   # avg PAID $/day over recent paid days
    graduate_days: int = 3            # paid days needed in the last 7 (stability)
    dump_usd_day: float = 0.0         # taker-dump proceeds allowed per day (0 = off)
    avoid_tokens: tuple = ()
    # FROZEN ground: the engine does nothing here at all — places no
    # orders, rests no exits, reprices nothing, cancels nothing. Every
    # order in a frozen market is treated exactly like one the owner
    # placed by hand (owner, 2026-08-24: "Don't sell my gop governor
    # count race orders. In fact don't touch those"). Different from
    # avoid_tokens, which PULLS the engine's orders out; freezing
    # leaves the book exactly as it stands.
    freeze_tokens: tuple = ()          # slug fragments the owner told us to stay out of
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
        self.fills: list[dict] = []           # the purchase journal, one row per fill
        self.proven: set[str] = set()         # graduated markets (main feeds it)
        self.recent_paid: dict[str, tuple] = {}   # mkt -> (avg $/day, paid days), last 7d
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
        self.dump_today = 0.0                     # taker-dump proceeds today
        self.earned_history: list[list] = []      # [day, $] rolling
        self._last_accrual = 0.0
        self.silent_cancels = 0
        self.gone_pending: dict[str, dict] = {}   # vanished, feed pending
        # order id -> when WE placed it. The audit log keeps 60 rows, so
        # a fill recovered from the exchange later had no placement time
        # and its resting period was unknowable (owner, 2026-08-23:
        # "can't you match up the placement time with the execution
        # time to get an exact resting period?" — yes, with this).
        self.placed_at: dict[str, float] = {}
        self.priority: set = set()   # markets to re-check first
        self.pending_pages: list = []   # open fills awaiting a mark
        self.log: list[dict] = []

    # ------------------------------------------------------------- helpers

    def _label(self, slug: str) -> str:
        return self.names.label(slug) if self.names is not None else slug

    def _log(self, **row) -> None:
        row.setdefault("ts", round(self._clock(), 1))
        self.log.append(row)
        del self.log[:-self.cfg.log_keep]

    def _avoided(self, slug: str) -> bool:
        """Markets the owner told us to stay out of (2026-08-22: Alaska
        governor, special rules pending). Exits still manage held stock;
        nothing new rests, probes, revives, or dumps here."""
        return any(t in slug for t in self.cfg.avoid_tokens)

    def _frozen(self, slug: str) -> bool:
        """Hands off entirely (owner, 2026-08-24: "don't touch those").
        Unlike an avoided market, nothing is pulled: whatever rests
        here stays exactly as it is, and the engine adds nothing."""
        return any(t in slug for t in self.cfg.freeze_tokens)

    def enterable(self, slug: str) -> bool:
        if self._avoided(slug) or self._frozen(slug):
            return False
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

    def _market_budget(self, slug: str) -> float:
        """Proven ground earns a bigger allowance (owner, 2026-08-21)."""
        if slug in self.proven and self.cfg.proven_per_market_usd:
            return self.cfg.proven_per_market_usd
        return self.cfg.per_market_usd

    def family_spent(self) -> float:
        """The search ceiling's number: worst case of the UNGRADUATED
        book, negative risk netted per race group (v3/risk.py). Graduated
        markets sit outside it, under proven_spent's own cap."""
        spent = risk.book_risk(risk.order_legs(
            o for o in self.orders.values()
            if o.market not in self.proven and not self._owner_exit(o)))
        if self.cfg.holdings_in_ceiling:
            spent += self.holdings_value()
        return spent

    def _owner_exit(self, o) -> bool:
        """The owner's own order. It never counts against a ceiling.

        The family budget limits what the ENGINE puts at risk on its
        own initiative. The owner sizes his own book, and standing
        instruction is that the engine neither touches it nor is
        credited for it — so spending it against his cap is charging
        the engine for money it did not commit.

        Was reduce-side manual orders only, on the reasoning that
        those add no new risk. On 2026-08-24 the manual orders became
        VISIBLE for the first time (before that the exchange's MANUAL
        flag made them invisible to the whole engine), and the
        risk-opening ones alone measured $484.66 against a $250
        politics cap — 194% of the budget, spent entirely by the
        owner. The engine was locked out: 0 entry orders, $4.27 of
        stale exits, and the lowest earning rate on record beside the
        highest budget utilisation on record. The owner spotted the
        contradiction before I did.

        Owner, 2026-08-24, on excluding all of them: "That's good." """
        return o.purpose == "manual"

    def holdings_value(self) -> float:
        """What the stock would fetch if liquidated NOW: longs at the
        best bid, shorts at what closing them recovers (owner,
        2026-08-21 evening: this number counts against the family
        budget — 'no more than $50 of risk in cfb, orders + holdings').
        A market with no book values conservatively at cost."""
        total = 0.0
        for slug, inv in self.inventory.items():
            qty = inv.get("qty") or 0.0
            if abs(qty) < 0.005:
                continue
            book = self.cache.any_age(slug)
            if qty > 0:
                if book is not None and book.bids:
                    total += qty * book.bids[0][0]
                else:
                    total += max(inv.get("cost", 0.0), 0.0)
            else:
                if book is not None and book.asks:
                    total += -qty * (1.0 - book.asks[0][0])
                else:
                    total += max(-inv.get("cost", 0.0), 0.0)
        return total

    def proven_spent(self) -> float:
        return risk.book_risk(risk.order_legs(
            o for o in self.orders.values()
            if o.market in self.proven and not self._owner_exit(o)))

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
                   cross_px: float | None = None,
                   ladder: list | None = None) -> dict | None:
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
            fair_rv = self.fairs(slug) if self.fairs is not None else None
            for k in (0, 1, 2, 3):
                px = round(anchor - k * sign * tick, 3)
                if not (0.001 <= px <= 0.999):
                    continue
                if other and (px >= other[0][0] - 1e-9 if side == "BUY"
                              else px <= other[0][0] + 1e-9):
                    continue
                if fair_rv is not None and (
                        (side == "BUY" and px > fair_rv - tick + 1e-9)
                        or (side == "SELL"
                            and px < fair_rv + tick - 1e-9)):
                    continue    # the hard cap binds revives too, both
                                # sides (owner, 2026-08-23)
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
                      - pf_r * fc_r * qty
                      - cost * self._capital_charge_rate(slug))
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
            bar_here = self.cfg.min_est_day if bar is None else bar
            if best is not None and best["ev"] >= bar_here:
                return best
            return None

        if own is not None and own.side == side:
            # net OUR OWN resting order out of the book first — planning
            # against a touch that is just ourselves anchors on a ghost
            # (the Massachusetts primary lesson: our 13c bid kept
            # re-planning against itself)
            netted = []
            for p2, q2 in levels:
                if abs(p2 - own.price) < tick / 2:
                    q2 = q2 - own.qty
                if q2 > 1e-9:
                    netted.append((p2, q2))
            levels = tuple(netted)
            if not levels:
                return None
        # -- the side qualifies: join or step back, never in front --
        # Never plan against ourselves (the Massachusetts rule,
        # generalized on the owner's word 2026-08-21: "Aren't I just
        # bidding against myself?"). Every order WE have resting on this
        # side comes out of the book before the touch is read; the share
        # math below still uses the full book, because the program counts
        # our size like anyone else's.
        mine_orders = [o for o in self.orders.values()
                       if o.market == slug and o.side == side
                       and (own is None or o.id != own.id)]
        mine_at: dict[float, float] = {}
        for o in mine_orders:
            pk = round(o.price, 3)
            mine_at[pk] = mine_at.get(pk, 0.0) + o.qty
        others = []
        for p2, q2 in levels:
            q3 = q2 - mine_at.get(round(p2, 3), 0.0)
            if q3 > 1e-9:
                others.append((p2, q3))
        if not others:
            return None   # the only real orders on this side are ours
        touch = others[0][0]
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

        grid = (tuple(q for q in QTY_GRID if q >= 1.0)
                if self.cfg.whole_shares else QTY_GRID)
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
        # In front of the touch, walk ONLY to the score frontier
        # (owner, 2026-08-21: "if you can get 100% of the score at 8
        # cents, why go to 9" — the question is 27 vs 28 vs 29, not 27
        # vs 44). Each next rung must materially improve the minimum-
        # size score share, or the walk stops: deeper adds fill risk
        # and a worse price for nothing.
        if other:
            best_share = 0.0
            for kf in range(1, 51):
                px = round(touch + kf * sign * tick, 3)
                if not (0.001 <= px <= 0.999):
                    break
                if (px - (other[0][0] - sign * tick)) * sign > 1e-9:
                    break
                j = estimate_join(side, levels, tick, df, target, px,
                                  grid[0])
                s = j.share if (j.qualifies and j.in_window) else 0.0
                if best_share > 0 and s <= best_share * 1.01 + 1e-9:
                    break         # no marginal score out here — pointless
                if s > best_share:
                    best_share = s
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
        # THE HARD CAP (owner, 2026-08-23, both halves: "not paying so
        # much past value for underdogs. That includes selling the
        # favorites short"): on a MODELED market an earn quote never
        # rests past fair — a BUY stays at or under fair minus one
        # tick, a SELL at or over fair plus one tick, at any price.
        # No concession ladder, no earned-confidence override. The NY
        # governor short (sold 1 @ 91c against a 98.4c model, filled
        # in a minute) is what the SELL half prevents. Markets with no
        # model keep the ignorance premium and independence discount.
        fair_hard = self.fairs(slug) if self.fairs is not None else None
        if fair_hard is not None:
            if side == "BUY":
                cands = [px for px in cands
                         if px <= fair_hard - tick + 1e-9]
            else:
                cands = [px for px in cands
                         if px >= fair_hard + tick - 1e-9]
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
        r_day = self._exit_opportunity_rate()
        r_tie = self._capital_charge_rate(slug)
        d_off = self.fillmodel.expected_offload_days(slug)
        inv_net = (self.inventory.get(slug) or {}).get("qty", 0.0)

        def _minus(lv, price, q0):
            out = []
            for p3, q3 in lv:
                if abs(p3 - price) < tick / 2:
                    q3 = q3 - q0
                if q3 > 1e-9:
                    out.append((p3, q3))
            return out

        est0 = 0.0
        for o in mine_orders:
            j0 = estimate_join(side, _minus(levels, o.price, o.qty), tick,
                               df, target, o.price, o.qty)
            if j0.qualifies and j0.in_window:
                est0 += j0.share * side_pool
        contenders: list[dict] = []
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
            # the ignorance premium (owner approved 2026-08-21): when we
            # cannot price the market, a fill's cost includes the
            # EXPECTED overpay if true fair lies anywhere in the spread
            # — zero at the touch, quadratic as we advance, gone when a
            # model grounds the market or fills build confidence
            ign = 0.0
            if independence < 1.0 and other:
                spread_w = abs(other[0][0] - touch)
                if spread_w > tick / 2:
                    adv = (px - touch) if side == "BUY" else (touch - px)
                    if adv > 0:
                        ign = ((1.0 - independence) * adv * adv
                               / (2.0 * spread_w))
            pf = self.fillmodel.p_fill(slug, side, k_px, shield=shield,
                                       target=target, bait=conc + h)
            fcost = self.fillmodel.fill_cost(slug, side, px, value_ctr,
                                             exit_rate_ps=exit_rate_ps,
                                             ignorance=ign)
            for qty in grid:
                if (h >= 0.5 and qty > grid[0]
                        and (in_front or k_px == 0)):
                    break     # a fill just happened here: minimum size
                # a price past fair is a TARGET (owner, 2026-08-22:
                # "bigger size is fine so long as we can use some of the
                # spread to offset losses"): size shrinks with every tick
                # conceded — three or more ticks past value rests only
                # the minimum
                if conc >= 1.0 and qty > grid[0]:
                    if conc >= 3.0:
                        break
                    if qty > grid[0] * (8.0 if conc < 2.0 else 3.0):
                        break
                if qty * cost_ps > budget + 1e-9:
                    break
                j = estimate_join(side, levels, tick, df, target, px, qty)
                if not (j.qualifies and j.in_window):
                    break
                est = j.share * side_pool
                # marginal, not gross (owner, 2026-08-21): what this
                # order ADDS is its own score minus what it takes from
                # our other orders already resting on this side
                cann = 0.0
                if mine_orders:
                    cl = list(levels) + [(px, qty)]
                    est1 = 0.0
                    for o in mine_orders:
                        j1 = estimate_join(side, _minus(cl, o.price, o.qty),
                                           tick, df, target, o.price, o.qty)
                        if j1.qualifies and j1.in_window:
                            est1 += j1.share * side_pool
                    cann = max(est0 - est1, 0.0)
                # collateral tied while resting costs the marginal-cent
                # rate, scarcity-scaled. Freed capital counts ONLY in the
                # exit scorer — an earner gets NOTHING for freeing
                # capital (owner, 2026-08-22). Selling stock we already
                # hold still ties no new collateral; that is a fact, not
                # a credit.
                if side == "BUY":
                    tie = px * qty
                    if px >= 0.75:
                        # owner, 2026-08-23 ("Yes do both"): the
                        # expensive side is WANTED — a filled favorite
                        # resolves near $1 and always has an exit, so
                        # its locked-cash charge is halved and the EV
                        # ranking stops shying away from it
                        tie *= 0.5
                else:
                    sells = max(min(qty, inv_net), 0.0)
                    tie = (1.0 - px) * (qty - sells)
                ev = ((est - cann) * sf - pf * fcost * qty
                      - tie * r_tie)
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
                if ladder is not None:
                    ladder.append(dict(row))
                # No share cap (owner, 2026-08-21: "why would we cap the
                # total score we can claim? I don't agree with that. No
                # cap"). Size is bounded by the per-market money, the
                # family ceiling, the EV bar, and fill odds — nothing
                # else.
                contenders.append(row)
        the_bar = self.cfg.min_est_day if bar is None else bar
        live = [r for r in contenders if r["ev"] >= the_bar]
        if not live:
            return None
        best_ev = max(r["ev"] for r in live)
        # Near-tied EVs resolve to the most CONSERVATIVE spot — lowest
        # fill odds (owner, 2026-08-21: "the model is not precise
        # enough to make a big fuss over 1 cent of ev" — never take a
        # deeper price for the last penny).
        tol = max(0.01, 0.01 * best_ev)
        close = [r for r in live if r["ev"] >= best_ev - tol]
        pick = min(close, key=lambda r: (r["p_fill"], -r["ev"]))
        if self.cfg.wall_size_up:
            # same price level, biggest size the budget allows: the
            # modeled fill cost that shrank it is an accepted cost here
            same_px = [r for r in contenders
                       if abs(r["px"] - pick["px"]) < 1e-9
                       and r["est"] > 0.0]
            if same_px:
                pick = max(same_px, key=lambda r: r["qty"])
        return pick

    def lite_recalc(self, slug: str, bb: float | None,
                    ba: float | None) -> dict | None:
        """Our estimated $/day in this market IF scoring anchors on the
        exchange's DECLARED best bid/ask (the group-chat claim,
        2026-08-21) instead of the raw touch. Study only — changes no
        behavior."""
        book = self.cache.any_age(slug)
        prog, _w = self._prog_row(slug)
        if book is None or prog is None:
            return None
        sp = self._side_pool(slug, prog)
        if sp is None:
            return None
        df, target = float(prog.df), float(prog.target)
        out = {"market": slug, "bb": bb, "ba": ba,
               "raw_bid": book.bids[0][0] if book.bids else None,
               "raw_ask": book.asks[0][0] if book.asks else None,
               "est_alt": 0.0, "est_cur": 0.0}
        # levels the exchange's declared best SKIPPED — the filter that
        # produced the declared value must reject every one of these
        # (owner, 2026-08-21: "figure out how the best bid / ask are
        # calculated ... so that I could try and move them")
        if bb is not None:
            out["skip_b"] = [[p, round(q, 2)] for p, q in book.bids
                             if p > bb + 1e-9][:6]
        if ba is not None:
            out["skip_a"] = [[p, round(q, 2)] for p, q in book.asks
                             if p < ba - 1e-9][:6]
        # the window-closing play, priced: resting Target Size at the raw
        # touch closes the scoring window there — everyone deeper earns
        # zero (the docs' own example). What that costs per side:
        if book.bids:
            out["own_bid_usd"] = round(target * book.bids[0][0], 2)
        if book.asks:
            out["own_ask_usd"] = round(target * (1.0 - book.asks[0][0]), 2)
        out["pool_side"] = round(sp, 2)
        for side, anchor in (("BUY", bb), ("SELL", ba)):
            levels = list(book.side(side))
            total = sum(q for _, q in levels)
            mine = [(o.price, o.qty) for o in self.orders.values()
                    if o.market == slug and o.side == side]
            out["est_cur"] += sum((o.live_est or 0.0)
                                  for o in self.orders.values()
                                  if o.market == slug and o.side == side)
            if anchor is None or not mine or total < target:
                continue
            denom = sum(q * df ** round(abs(p - anchor) / book.tick)
                        for p, q in levels)
            ours = sum(q * df ** round(abs(p - anchor) / book.tick)
                       for p, q in mine)
            if denom > 1e-12:
                out["est_alt"] += min(ours / denom, 1.0) * sp
        out["est_alt"] = round(out["est_alt"], 4)
        out["est_cur"] = round(out["est_cur"], 4)
        return out

    def ladder_view(self, slug: str) -> dict:
        """Every price level the planner prices, with its numbers —
        the owner reads the whole ladder himself (2026-08-21: "allow me
        to click into any market to see even more detail on the numbers
        for listing at every price level")."""
        book = self.cache.any_age(slug)
        if book is None:
            return {"ok": False, "note": "no book cached yet"}
        prog, why = self._prog_row(slug)
        if prog is None:
            return {"ok": False, "note": why}
        sp = self._side_pool(slug, prog)
        headroom = self.cfg.capital_usd - self.family_spent()
        out = {"ok": True, "bar": self.cfg.min_est_day,
               "pool_day": round(sp, 2) if sp is not None else None,
               "note": ("pool divisor unconfirmed — dollar figures held at 0"
                        if sp is None else
                        f"family at its ceiling — new orders wait for "
                        f"${-headroom + 1:.0f} of space" if headroom < 1.0
                        else ""), "sides": {}}
        for side in ("BUY", "SELL"):
            rows: list[dict] = []
            try:
                pick = self._plan_side(slug, book, side, prog, sp or 0.0,
                                       self.cfg.per_market_usd / 2.0,
                                       ladder=rows)
            except Exception as e:  # noqa: BLE001 — the view never breaks
                out["sides"][side] = {"rows": [], "note": str(e)[:80]}
                continue
            best: dict[float, dict] = {}
            for r in rows:
                b = best.get(r["px"])
                if b is None or r["ev"] > b["ev"]:
                    best[r["px"]] = r
            ordered = sorted(best.values(), key=lambda r: -r["px"]
                             if side == "BUY" else r["px"])
            for r in ordered:
                r["picked"] = bool(pick and abs(pick["px"] - r["px"]) < 1e-9)
                r["clears_bar"] = r["ev"] >= self.cfg.min_est_day
            entry = {"rows": ordered[:24]}
            if not ordered:
                st = sum(q for _, q in book.side(side))
                if st < float(prog.target):
                    entry["note"] = (
                        f"the {'bid' if side == 'BUY' else 'ask'} side holds "
                        f"{st:,.0f} of {float(prog.target):,.0f} Target Size "
                        f"shares — the whole side pays nobody, so there is "
                        f"nothing to price")
            out["sides"][side] = entry
        return out

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
        budget = self._market_budget(slug) / 2.0

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

    def reconcile(self, open_orders: list[dict], positions: dict, now: float,
                  trades=None) -> None:
        """Adopt reality. Fills come from position deltas, never from mere
        disappearance. Scoped to markets THIS family placed in — the
        account is shared with 1.0 and 2.0, and their fills are not ours."""
        open_by_id = {o["id"]: o for o in open_orders}
        # remember when each live order was placed, before it can vanish
        for _oid, _rec in self.orders.items():
            if _rec.placed_ts:
                self.placed_at[_oid] = _rec.placed_ts
        if len(self.placed_at) > 6000:      # keep the newest, bounded
            for _k in sorted(self.placed_at, key=self.placed_at.get)[:2000]:
                self.placed_at.pop(_k, None)
        tracked = (set(self.positions_seen) | set(self.inventory)
                   | {o.market for o in self.orders.values()}
                   | {g["rec"].market for g in self.gone_pending.values()})
        deltas = {m: (positions.get(m) or (0.0, 0.0))[0]
                  - self.positions_seen.get(m, 0.0)
                  for m in tracked}
        # limbo first: orders that disappeared earlier waiting for the
        # lagging position feed to say fill or cancel
        for oid, gp in list(self.gone_pending.items()):
            rec = gp["rec"]
            if trades and oid in trades:
                # the exchange's own trade history names this order id:
                # the definitive confirmation — a post-only rest fills
                # at its own price, so the journal price is exact
                filled = min(float(trades[oid]), rec.qty)
                self._on_fill(rec, filled, now)
                del self.gone_pending[oid]
                continue
            d = deltas.get(rec.market, 0.0)
            expected = rec.qty if rec.intent == BUY_LONG else -rec.qty
            if abs(d) > 1e-9 and (d > 0) == (expected > 0):
                filled = min(abs(d), rec.qty)
                deltas[rec.market] = d - (filled if d > 0 else -filled)
                self._on_fill(rec, filled, now)
                del self.gone_pending[oid]
            elif now >= gp["until"]:
                self.silent_cancels += 1
                self._log(event="silent_cancel", market=rec.market,
                          side=rec.side, price=rec.price, qty=rec.qty,
                          id=oid)
                del self.gone_pending[oid]
        for oid, rec in list(self.orders.items()):
            live = open_by_id.get(oid)
            if live is not None:
                if live["size"] < rec.qty - 1e-9:
                    # a shrunken size is only a FILL if the position
                    # moved with it (the Louisiana phantom, 2026-08-21:
                    # cancelled revives were booked as 265-share shorts
                    # the exchange never saw, and the exit engine bid
                    # real money to cover them). No delta -> it is a
                    # size correction, not a fill.
                    shrink = rec.qty - live["size"]
                    d = deltas.get(rec.market, 0.0)
                    expected_sign = 1.0 if rec.intent == BUY_LONG else -1.0
                    if abs(d) > 1e-9 and (d > 0) == (expected_sign > 0):
                        filled = min(shrink, abs(d))
                        deltas[rec.market] = d - expected_sign * filled
                        self._on_fill(rec, filled, now)
                    else:
                        self._log(event="size_shrunk_no_fill",
                                  market=rec.market, side=rec.side,
                                  price=rec.price, qty=shrink, id=oid)
                    rec.qty = live["size"]
                continue
            delta = deltas.get(rec.market, 0.0)
            expected = rec.qty if rec.intent == BUY_LONG else -rec.qty
            if abs(delta) > 1e-9 and (delta > 0) == (expected > 0):
                filled = min(abs(delta), rec.qty)
                deltas[rec.market] = delta - (filled if delta > 0 else -filled)
                self._on_fill(rec, filled, now)
            elif trades and oid in trades:
                self._on_fill(rec, min(float(trades[oid]), rec.qty), now)
            else:
                # NOT ruled a silent cancel yet: the position feed LAGS
                # the order list, so a complete fill often shows the
                # order gone before the delta arrives — instant
                # classification threw those fills away and the cards
                # read "closed by reconciliation" (owner, 2026-08-23:
                # "literally every closed position... says closed by
                # reconciliation"). The record waits in limbo; a
                # matching delta books the fill, GONE_GRACE_S of
                # silence makes it a real silent cancel.
                self.gone_pending[oid] = {"rec": rec,
                                          "until": now + GONE_GRACE_S}
            self.evidence.order_gone(rec.market, oid, now=now)
            del self.orders[oid]
        for m in tracked:
            if m in positions:
                self.positions_seen[m] = positions[m][0]
                # the exchange's position feed is the truth: wherever it
                # explicitly reports this market, our inventory snaps to
                # it, purging any phantom the fill accounting invented
                feed_qty = positions[m][0]
                inv = self.inventory.get(m)
                have = (inv or {}).get("qty", 0.0)
                if abs(feed_qty - have) > 0.01:
                    if abs(feed_qty) < 0.005:
                        if inv is not None:
                            self.inventory.pop(m, None)
                            self.inv_since.pop(m, None)
                    else:
                        if abs(have) > 0.005:
                            per = (inv or {}).get("cost", 0.0) / have
                            cost = per * feed_qty
                        else:
                            cost = (positions[m][1]
                                    if len(positions[m]) > 1 else 0.0)
                        self.inventory[m] = {"qty": feed_qty,
                                             "cost": round(cost, 4)}
                    self._log(event="inventory_corrected", market=m,
                              qty=feed_qty,
                              note=f"book said {have:g}, exchange says "
                                   f"{feed_qty:g} — exchange wins")
        # The feed lists only markets actually held (a failed fetch
        # aborts the cycle upstream, so this snapshot is complete).
        # Book inventory in a market the feed does not mention is
        # phantom — the Louisiana lesson part two: the first fix only
        # snapped markets the feed NAMED, and a phantom market is
        # exactly the one it never names. Fresh fills get a grace
        # period; the next snapshot confirms them.
        for m in list(self.inventory):
            if m in positions:
                continue
            if now - self.inv_since.get(m, 0.0) < 180.0:
                continue
            gone_qty = self.inventory[m].get("qty", 0.0)
            self.inventory.pop(m, None)
            self.inv_since.pop(m, None)
            self._log(event="inventory_corrected", market=m, qty=0.0,
                      note=f"book said {gone_qty:g}, the exchange holds "
                           f"nothing — phantom purged")
        for m in list(self.positions_seen):
            if (m not in self.inventory
                    and m not in {o.market for o in self.orders.values()}):
                self.positions_seen.pop(m, None)

    def _on_fill(self, rec: FamilyOrder, filled: float, now: float) -> None:
        if rec.market not in self.inventory:
            self.inv_since[rec.market] = now
        inv = self.inventory.setdefault(rec.market, {"qty": 0.0, "cost": 0.0})
        q0, c0 = inv["qty"], inv["cost"]
        if rec.side == "BUY":
            inv["qty"] += filled
            inv["cost"] += filled * rec.price
        else:
            inv["qty"] -= filled
            inv["cost"] -= filled * rec.price
        qty_after = round(inv["qty"], 2)
        if abs(inv["qty"]) < 0.005:
            self.inventory.pop(rec.market, None)
            since = self.inv_since.pop(rec.market, None)
            if since is not None and now > since:
                self.fillmodel.observe_offload(rec.market,
                                               (now - since) / 86400.0)
        self._journal_fill(rec, filled, now, qty_after)
        self.evidence.fill(rec.market, rec.side, rec.price, ts=now)
        self.fillmodel.observe_fill_age(rec.market, now - rec.placed_ts)
        self.pending_marks.append({"market": rec.market, "side": rec.side,
                                   "price": rec.price, "due": now + 3600.0})
        del self.pending_marks[:-60]
        self._log(event="fill", market=rec.market, side=rec.side,
                  price=rec.price, qty=round(filled, 2))
        gain = self._closing_gain(rec.side, rec.price, filled, q0, c0)
        if gain is not None:
            # A CLOSE. Silent unless it realised more than a dollar of
            # loss (owner, 2026-08-24). Profit, break-even and small
            # losses all stay off the phone; the card still records it.
            if gain < -PAGE_LOSS_USD:
                self.alert(f"{self.cfg.tag} closed at a loss",
                           f"{self._label(rec.market)}: {rec.side} "
                           f"{filled:g} @ {rec.price * 100:g}c — "
                           f"${-gain:.2f} lost on the round trip")
            else:
                self._log(event="fill_no_page", market=rec.market,
                          note=f"closed {filled:g} at ${gain:+.2f} — "
                               f"under the ${PAGE_LOSS_USD:g} page bar")
        else:
            # An OPEN. The decision waits for the book to settle: right
            # after a fill the touch is the one our own trade just moved
            # (owner, 2026-08-24: "liquidation 20 seconds later").
            self.pending_pages.append(
                {"market": rec.market, "side": rec.side, "qty": filled,
                 "px": rec.price, "due": now + PAGE_SETTLE_S})
            del self.pending_pages[:-200]

    @staticmethod
    def _closing_gain(side: str, price: float, filled: float,
                      q0: float, c0: float) -> float | None:
        """Realized dollars when a fill only REDUCES the position it
        found: proceeds against the average cost of the shares closed.
        None when the fill opened, grew, or flipped a position — that
        is new risk, and new risk always pages."""
        if side == "SELL" and q0 > 0.005 and filled <= q0 + 0.005:
            return (price - c0 / q0) * filled
        if side == "BUY" and q0 < -0.005 and filled <= -q0 + 0.005:
            return (c0 / q0 - price) * filled
        return None

    def _page_opens_due(self, now: float) -> None:
        """Decide the held-back OPEN fills once the book has settled.
        Page only when the position is BOTH marked at more than a
        dollar of loss AND earning nothing (owner, 2026-08-24) — a
        paper loss that is collecting rewards is the business working,
        not news."""
        for p in list(self.pending_pages):
            if now < p["due"]:
                continue
            self.pending_pages.remove(p)
            slug = p["market"]
            inv = self.inventory.get(slug) or {}
            qty = inv.get("qty") or 0.0
            if abs(qty) < 0.005:
                continue                  # already gone; nothing to warn about
            book = self.cache.any_age(slug)
            if book is None:
                continue                  # no mark, no claim
            mark = (book.bids[0][0] if qty > 0 and book.bids
                    else book.asks[0][0] if qty < 0 and book.asks else None)
            if mark is None:
                continue
            pnl = qty * mark - (inv.get("cost") or 0.0)
            earning = any((o.live_est or 0.0) > 0.0
                          for o in self.orders.values() if o.market == slug)
            if pnl < -PAGE_LOSS_USD and not earning:
                self.alert(f"{self.cfg.tag} position under water, earning nothing",
                           f"{self._label(slug)}: {p['side']} {p['qty']:g} @ "
                           f"{p['px'] * 100:g}c — the {qty:g} now held marks "
                           f"${-pnl:.2f} down and nothing is earning here")
            else:
                self._log(event="fill_no_page", market=slug,
                          note=f"opened {p['qty']:g} — marks ${pnl:+.2f}"
                               f"{' and is earning' if earning else ''}; "
                               f"under the page bar")

    def _journal_fill(self, rec: FamilyOrder, filled: float, now: float,
                      qty_after: float) -> None:
        """One row per purchase, captured the moment it happens: what the
        order was doing, what value looked like right then (before this
        fill enters the evidence), and the position it left behind. The
        fills page reads these back to the owner."""
        try:
            book = self.cache.any_age(rec.market)
            fair = self.fairs(rec.market) if self.fairs is not None else None
            band = None
            if book is not None:
                try:
                    band = self._band(rec.market, book.bids, book.asks,
                                      book.tick)
                except Exception:  # noqa: BLE001
                    band = None
            ref = fair
            if ref is None and band and band.get("med") is not None:
                ref = band["med"] / 100.0
            conc = None
            if ref is not None:
                conc = round((rec.price - ref) if rec.side == "BUY"
                             else (ref - rec.price), 4)
            self.fills.append({
                "ts": round(now, 1), "market": rec.market, "side": rec.side,
                "qty": round(filled, 2), "px": rec.price,
                # the exchange's order id: the exact handle for matching
                # a journal row to the exchange's own transaction record
                # (owner, 2026-08-23: "keep track of the order id in the
                # future so we can match it up"). Price-bucket matching
                # was the only option before this and could not tell two
                # orders at one price apart.
                "oid": rec.id,
                "purpose": rec.purpose, "why": rec.why,
                "est_day": (rec.live_est if rec.live_est is not None
                            else rec.est_day),
                "rested_h": (round((now - rec.placed_ts) / 3600.0, 2)
                             if rec.placed_ts > 0 else None),
                "fair": fair,
                "band": ([band["lo"], band["hi"]] if band else None),
                "conf": round(self.evidence.confidence(rec.market), 3),
                "touch_bid": (book.bids[0][0]
                              if book is not None and book.bids else None),
                "touch_ask": (book.asks[0][0]
                              if book is not None and book.asks else None),
                "conc": conc, "pos_after": qty_after})
            # retention (owner, 2026-08-22): a row must outlive its card
            # — closed cards show for 3 days, open ones until profitable
            # — so keep a week of rows plus anything belonging to a
            # market we still hold, bounded at 600
            cutoff = now - 7 * 86400.0
            keep = [r2 for r2 in self.fills
                    if r2.get("ts", 0.0) >= cutoff
                    or abs((self.inventory.get(r2.get("market"))
                            or {}).get("qty", 0.0)) > 0.005]
            self.fills = keep[-600:]
        except Exception:  # noqa: BLE001 — the journal never breaks a fill
            pass

    # ---------------------------------------------------------------- adoption

    def adoptable(self, open_orders: list[dict], foreign_ids=()) -> list[dict]:
        """Every resting account order this family does not already
        track, in its universe.

        Orders the exchange flags MANUAL are RECORDED, not skipped
        (owner, 2026-08-24: "if I cancel an order and put a new one
        back the model won't sell more than is already there").
        Skipping them meant the owner's own exits never entered the
        book, so the cover math saw a bare position and rested a
        second exit on top of his — the flag that identifies his
        orders was the thing that hid them. Recording costs nothing:
        every adopted order becomes purpose="manual", which is never
        cancelled, moved or resized anywhere in the engine."""
        out = []
        for o in open_orders:
            if o["id"] in self.orders or o["id"] in foreign_ids:
                continue
            if o["market"] not in self.universe:
                continue
            if not o.get("size") or not o.get("price"):
                continue
            out.append(o)
        return out

    def _adopt(self, adoptable: list[dict], positions: dict, now: float) -> None:
        """An open order this engine did not place is the OWNER'S OWN
        (the 1.0/2.0 handover is finished — nothing else places orders).
        Record it so ceilings, exits, and dedupe can see it, mark it
        manual, and never cancel, move, or reprice it (owner, 2026-08-22:
        "Don't let it cancel orders I set by hand")."""
        for o in adoptable:
            self.orders[o["id"]] = FamilyOrder(
                id=o["id"], market=o["market"], side=o["side"],
                price=o["price"], qty=o["size"], intent=o["intent"],
                placed_ts=now, purpose="manual",
                why="the owner's own order — the engine leaves it alone")
            self.positions_seen.setdefault(
                o["market"], (positions.get(o["market"]) or (0.0,))[0])
            self._mark(o["market"], o["side"], now)
        if adoptable:
            self._log(event="owner_orders_seen", n=len(adoptable),
                      note="resting orders this engine did not place — "
                           "recorded hands-off, never cancelled")

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
              exits_only: bool = False, trades=None) -> dict:
        self.reconcile(open_orders, positions, now, trades=trades)
        self._page_opens_due(now)
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
            if rec.purpose == "manual" or self._frozen(rec.market):
                continue      # owner, 2026-08-22: never cancel the owner's
                              # own orders — no rule outranks the hand;
                              # 2026-08-24: nor anything in frozen ground
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
                ign_now = 0.0
                ind_now = (1.0 if self.fairs is not None
                           and self.fairs(rec.market) is not None
                           else self.evidence.confidence(rec.market))
                osd = book.side("SELL" if rec.side == "BUY" else "BUY")
                if ind_now < 1.0 and lv and osd:
                    spread_w = abs(osd[0][0] - lv[0][0])
                    if spread_w > book.tick / 2:
                        adv = ((rec.price - lv[0][0]) if rec.side == "BUY"
                               else (lv[0][0] - rec.price))
                        if adv > 0:
                            ign_now = ((1.0 - ind_now) * adv * adv
                                       / (2.0 * spread_w))
                fc_now = self.fillmodel.fill_cost(rec.market, rec.side,
                                                  rec.price, None,
                                                  ignorance=ign_now)
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
        # Markets the owner just repriced come FIRST. Setting a fair is
        # a statement that the resting book is wrong there, and with
        # 283 orders and 10 actions a cycle the sweep could take many
        # minutes to reach them — long enough for a non-compliant order
        # to fill (the jdvan buy at 57c against his 50c fair,
        # 2026-08-23). Same rails, same budget, different order.
        recs = sorted(self.orders.values(),
                      key=lambda r: 0 if r.market in self.priority else 1)
        for rec in recs:
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
            if rec.purpose == "manual" or self._frozen(rec.market):
                continue          # frozen ground: never repriced,
                                  # never pulled, never resized
            if self._avoided(rec.market):
                # out means OUT — earn orders, probes, AND the engine's
                # own exits leave (owner, 2026-08-22: the balance-of-power
                # markets are his to work by hand; an engine order resting
                # there kills his via the exchange's self-match guard).
                # Manual orders were already skipped above.
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    self._log(event="pull", market=rec.market,
                              side=rec.side,
                              why="owner: staying out of this market "
                                  "for now — it is his to work by hand")
                    del self.orders[rec.id]
                    actions -= 1
                continue
            if rec.purpose in ("sell", "probe"):
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
                                   self._market_budget(rec.market) / 2.0,
                                   own=rec,
                                   bar=(self.cfg.grow_floor
                                        if rec.purpose == "grow" else None))
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
            gmin = 1.0 if self.cfg.whole_shares else QTY_GRID[0]
            shrink_cap = None
            fair_m = self.fairs(rec.market) if self.fairs is not None else None
            if fair_m is not None:
                past_t = (((rec.price - fair_m) if rec.side == "BUY"
                           else (fair_m - rec.price)) / book.tick)
                if past_t >= 3.0:
                    shrink_cap = gmin
                elif past_t >= 2.0:
                    shrink_cap = gmin * 3.0
                elif past_t >= 1.0:
                    shrink_cap = gmin * 8.0
            shrink_needed = (shrink_cap is not None
                             and rec.qty > shrink_cap + 1e-9)
            if fair_m is not None and (
                    (rec.side == "BUY"
                     and rec.price > fair_m - book.tick + 1e-9)
                    or (rec.side == "SELL"
                        and rec.price < fair_m + book.tick - 1e-9)):
                # the hard cap binds the RESTING book too, both sides
                # (owner, 2026-08-23): a quote past fair moves back to
                # a compliant slot or leaves — regardless of earnings
                shrink_needed = True
            if (self.cfg.wall_size_up and best is not None
                    and best["qty"] > rec.qty * 2 + 1e-9):
                # the size-up binds the RESTING book too (owner,
                # 2026-08-23: "I don't see any increase in nba order
                # sizes" — the dust joins placed before the rule never
                # repriced, because bigger size shows worse model EV).
                # An undersized join is forced to the full-size slot
                # exactly like an oversized one is forced to shrink.
                shrink_needed = True
            if (best is not None and best.get("revive")
                    and rec.purpose != "grow"):
                # the order earns nothing only because its side is below
                # Target Size, and a revive within the caps can qualify
                # it — that is the fix, not a cancel (owner, 2026-08-21:
                # "we shouldn't cancel something on the basis that it
                # does not earn rewards if the fix is easy i.e.
                # qualifying the side")
                rec.weak_since = 0.0
                continue
            if (best is None and rec.purpose != "grow"
                    and (rec.live_est or 0.0) <= 0.0
                    and sum(q for _, q in book.side(rec.side))
                    < float(prog.target)
                    and self._plan_side(rec.market, book, rec.side, prog,
                                        side_pool,
                                        self._market_budget(rec.market) / 2.0,
                                        own=rec, bar=0.0) is not None):
                # same caveat, bar aside: the side CAN be qualified within
                # the caps, it just does not pay enough to act on yet —
                # the order stays; the revive places if its EV ever clears
                rec.weak_since = 0.0
                continue
            if ((best is None and ((rec.live_est or 0.0) <= 0.0
                                   or shrink_needed)) or weak):
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    why = (f"under {self.cfg.min_est_day * 100:.0f}c/day for "
                           f"{(now - rec.weak_since) / 3600:.1f}h — cycling "
                           f"out to the next best market" if weak else
                           "resting size past fair — a target; pulled "
                           "(owner, 2026-08-22)" if shrink_needed else
                           "earning nothing and no better spot")
                    self._log(event="pull", market=rec.market, side=rec.side,
                              why=why)
                    del self.orders[rec.id]
                    self._mark(rec.market, rec.side, now)
                    actions -= 1
            elif (best is not None
                    and (gain >= self.cfg.reprice_gain_day
                         or shrink_needed)
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
                        > self._market_budget(slug) + 1e-9 \
                        and not plan.get("revive"):
                    continue    # proven ground gets its bigger allowance
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
            cands = [o for o in self.orders.values()
                     if o.purpose not in ("sell", "manual")
                     and not self._frozen(o.market)]
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

    def _prune_excess_exits(self, slug: str, side: str, excess: float,
                            now: float) -> None:
        """Exits must never total more than the position they exit —
        an over-covered short flips long when everything fills (the
        Alabama six-covers-for-five-shares case, 2026-08-21). Pull the
        worst-earning excess, never manual orders."""
        cands = sorted((o for o in self.orders.values()
                        if o.market == slug and o.purpose == "sell"
                        and o.side == side),
                       key=lambda o: (o.live_est or 0.0))
        for rec in cands:
            if excess < 0.01:
                break
            if rec.qty > excess + 0.01:
                continue          # too big to pull whole — fallback below
            r = self.desk.cancel(rec.id, rec.market)
            if r.ok:
                excess -= rec.qty
                self.orders.pop(rec.id, None)
                self.evidence.order_gone(rec.market, rec.id)
                self._log(event="excess_exit_pruned", market=slug,
                          price=rec.price, qty=rec.qty,
                          note="exits exceeded the position")
        if excess >= 0.01:
            # every remaining cover is BIGGER than the excess (the tulgab
            # 500-vs-1 shape) — cancel the worst earner whole; the next
            # pass rests one sized to the real position. Cancel-first, so
            # nothing is ever over-offered (owner approved 2026-08-21).
            for rec in cands:
                if rec.id not in self.orders:
                    continue
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    self.orders.pop(rec.id, None)
                    self.evidence.order_gone(rec.market, rec.id)
                    self._log(event="excess_exit_pruned", market=slug,
                              price=rec.price, qty=rec.qty,
                              note="bigger than the position it covers — "
                                   "cancelled whole; the next pass rests "
                                   "one sized to the real position")
                break

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
            floor_px, _sb = self._exit_floor(slug, "SELL", break_even,
                                             book.tick, book=book, qty=qty)
            lo = max(floor_px,
                     (book.bids[0][0] + book.tick) if book.bids else 0.002)
            # 2026-08-22: the target IS the front of the profitable
            # range — join the ask touch unless it gives away against
            # the model
            fair_m2 = self.fairs(slug) if self.fairs is not None else None
            jp = (book.asks[0][0] if book.asks
                  else break_even + book.tick)
            if fair_m2 is not None and jp < fair_m2 - 3 * book.tick:
                jp = fair_m2 - book.tick
            hi = max(min(jp, 0.999), lo)
        else:
            received = min(max(-inv.get("cost", 0.0) / -qty, 0.002), 0.999)
            cap_px, _sb = self._exit_floor(slug, "BUY", received, book.tick,
                                           book=book, qty=-qty)
            hi = min(cap_px,
                     (book.asks[0][0] - book.tick) if book.asks
                     else cap_px)
            lo = min((book.bids[0][0] if book.bids else hi), hi)
        best = (hi if side == "SELL"
                else self._best_exit_px(slug, side, book, lo, hi, rec.qty))
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
        if side != "SELL" and best_est < cur_est * 1.5 + 0.05:
            return                      # covers: move only when clearly better
        # stock sells always come to the front (owner, 2026-08-22:
        # "sell more aggressively") — the cooldown throttles the churn
        r = self.desk.cancel(rec.id, rec.market)
        if r.ok:
            self.orders.pop(rec.id, None)
            self.evidence.order_gone(rec.market, rec.id)
            self._log(event="exit_moved", market=slug, price=rec.price,
                      qty=rec.qty,
                      note=f"a slot at {best:.2f} earns more — moving")

    def _exit_floor(self, slug: str, side: str, basis: float,
                    tick: float, book=None,
                    qty: float | None = None) -> tuple[float, float]:
        """(price limit, scoring basis) for an exit. Break-even bounds it
        by default. When the model prices the market and says holding to
        resolution loses MORE than closing near fair, the limit extends
        to fair (owner, 2026-08-21, the Massachusetts short). With no
        model, the EVIDENCE BAND's conservative edge does the same job —
        sell no lower than the band's top, cover no higher than its
        bottom (owner, 2026-08-22: stranded exits must be able to fill).
        And a position worth under 50 cents in total may walk away at
        the touch — the argument is smaller than the tick."""
        fair = self.fairs(slug) if self.fairs is not None else None
        if fair is None and book is not None:
            try:
                band = self._band(slug, book.bids, book.asks, book.tick)
            except Exception:  # noqa: BLE001
                band = None
            if band:
                edge = band.get("hi") if side == "SELL" else band.get("lo")
                if edge is not None:
                    fair = edge / 100.0
        dust = False
        if qty is not None and book is not None:
            if side == "SELL" and book.bids:
                dust = qty * book.bids[0][0] < 0.50
            elif side == "BUY" and book.asks:
                dust = qty * (1.0 - book.asks[0][0]) < 0.50
        if side == "SELL":
            if dust and book is not None and book.bids:
                fl = round(book.bids[0][0] + tick, 3)
                return fl, min(basis, fl)
            if fair is not None and fair < basis:
                fl = max(fair, 0.002)
                return fl, fl
            return basis + tick, basis
        if dust and book is not None and book.asks:
            cp = round(book.asks[0][0] - tick, 3)
            return cp, max(basis, cp)
        if fair is not None and fair > basis:
            cp = min(fair, 0.998)
            return cp, cp
        return basis - tick, basis

    def _capital_charge_rate(self, slug: str) -> float:
        """The rate a candidate pays for tying capital up. Opportunity
        cost only exists under scarcity (owner, 2026-08-22: "opportunity
        cost is not a factor here" — the ceiling has slack): the
        marginal-cent rate scaled by how full the relevant pool is."""
        r = self._exit_opportunity_rate()
        if slug in self.proven and self.cfg.proven_usd > 0:
            util = self.proven_spent() / self.cfg.proven_usd
        else:
            util = self.family_spent() / max(self.cfg.capital_usd, 1e-9)
        return r * min(max(util, 0.0), 1.0)

    def _exit_opportunity_rate(self) -> float:
        """$/day one freed cent could earn — the owner's definition
        (2026-08-21): "assume that we could use each cent gained from a
        sale about as effectively on average as our last marginal cent."
        Measured as the lower-quartile value-per-dollar among the
        deployed earn orders: the rate of the last money we chose to
        put to work, not the average of the best of it."""
        rates = []
        for o in self.orders.values():
            if o.purpose in ("sell", "manual", "probe"):
                continue
            risk = capital_at_risk(o.intent, o.price, o.qty)
            if risk > 0.005 and (o.live_est or 0.0) > 0:
                # cap what one order's claim may testify (owner,
                # 2026-08-22: "realistically we can do no better than
                # 2 dollars a day on one dollar worth of capital")
                rates.append(min((o.live_est or 0.0) / risk, 2.0))
        if not rates:
            return 0.0
        rates.sort()
        return rates[max(len(rates) // 4 - 1, 0)]

    def _exit_score(self, est: float, pf: float, qty: float, px: float,
                    basis: float, side: str, r_eff: float,
                    d_off: float) -> float:
        """$/day value of resting an exit at px: what it earns resting,
        plus fill odds times (the realized profit over basis AND the
        freed capital redeployed at the book's rate for the measured
        hold). The owner's exit math, 2026-08-21."""
        if side == "SELL":
            profit = max(px - basis, 0.0) * qty
            freed = px * qty
        else:
            profit = max(basis - px, 0.0) * qty
            freed = (1.0 - px) * qty
        return est + pf * (profit + freed * r_eff * d_off)

    def _best_exit_px(self, slug: str, side: str, book, lo: float,
                      hi: float, qty: float,
                      basis: float | None = None) -> float:
        """The exit slot with the best $/day VALUE: resting earnings
        plus the expected gain of actually exiting (profit + freed
        money redeployed). With slack in the ceiling this reduces to
        the best-earning slot; with the ceiling binding it concedes
        toward faster exits (owner, 2026-08-21: opportunity cost)."""
        lo, hi = round(lo, 3), round(hi, 3)
        if hi < lo:
            return hi
        prog, _w = self._prog_row(slug)
        side_pool = self._side_pool(slug, prog) if prog is not None else None
        if prog is None:
            return hi if side == "SELL" else lo
        levels = [(p, q) for p, q in book.side(side) if q > 1e-9]
        touch = levels[0][0] if levels else (hi if side == "SELL" else lo)
        r_eff = self._exit_opportunity_rate()
        d_off = self.fillmodel.expected_offload_days(slug)
        base = basis if basis is not None else (lo if side == "SELL" else hi)
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
            ticks = (max(round((px - touch) / book.tick), 0)
                     if side == "SELL"
                     else max(round((touch - px) / book.tick), 0))
            pf = self.fillmodel.p_fill(slug, side, ticks,
                                       target=float(prog.target))
            score = self._exit_score(est, pf, qty, px, base, side,
                                     r_eff, d_off)
            near = -px if side == "SELL" else px
            key = (round(score, 4), near)
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
            if self._avoided(slug) or self._frozen(slug):
                continue      # the owner works these by hand: the engine
                              # rests NO exits here (owner, 2026-08-22),
                              # and a FROZEN market is not even tidied
            book = self.cache.fresh(slug, BOOK_MAX_AGE, now)
            if book is None:
                continue
            if qty >= 0.01:
                # long stock: an ask at break-even or better
                mine = [o for o in self.orders.values()
                        if o.market == slug and o.purpose == "sell"
                        and o.side == "SELL"]
                self._maybe_move_exit(slug, "SELL", mine, book, inv, now)
                # the owner's own resting SELLs of this stock count as
                # cover too — the engine sizes around them and never
                # offers the same shares twice (owner, 2026-08-22)
                manual_cover = sum(
                    o.qty for o in self.orders.values()
                    if o.market == slug and o.purpose == "manual"
                    and o.side == "SELL")
                covered = manual_cover + sum(
                    o.qty for o in self.orders.values()
                    if o.market == slug and o.purpose == "sell"
                    and o.side == "SELL")
                rest = qty - covered
                if covered > qty + 0.01:
                    self._prune_excess_exits(slug, "SELL", covered - qty, now)
                # THE CARVED EXCEPTION (owner, 2026-08-22 "Carve it"):
                # the taker dump — a limit SELL of held stock priced AT
                # the bid, never worse. Tight spread only, never past the
                # bid's displayed size, never a giveaway against the
                # model, exits cancelled first, capped per day.
                if (self.cfg.dump_usd_day > 0 and actions > 0
                        and not self._avoided(slug)
                        and book.bids and book.asks
                        and self._cooldown_ok(slug, "SELL", now)
                        and self.dump_today
                        < self.cfg.dump_usd_day - 1e-9):
                    be_d = min(max(inv.get("cost", 0.0) / qty, 0.001),
                               0.989)
                    fair_d = (self.fairs(slug)
                              if self.fairs is not None else None)
                    bid_t, bid_sz = book.bids[0]
                    if (bid_t >= be_d + 2 * book.tick
                            and book.asks[0][0] - bid_t
                            <= 2 * book.tick + 1e-9
                            and (fair_d is None
                                 or bid_t >= fair_d - 3 * book.tick)):
                        dq = min(qty - manual_cover, bid_sz,
                                 (self.cfg.dump_usd_day
                                  - self.dump_today)
                                 / max(bid_t, 0.01))
                        if self.cfg.whole_shares:
                            dq = float(int(dq))
                        dq = round(dq, 2)
                        if dq >= (1.0 if self.cfg.whole_shares else 0.01):
                            for o2 in [o2 for o2 in self.orders.values()
                                       if o2.market == slug
                                       and o2.purpose == "sell"
                                       and o2.side == "SELL"]:
                                rr = self.desk.cancel(o2.id, o2.market)
                                if rr.ok:
                                    self.orders.pop(o2.id, None)
                                    self.evidence.order_gone(o2.market,
                                                             o2.id)
                            r2 = self.desk.place_resting(
                                slug, "SELL", bid_t, dq,
                                net_position=qty, intent=SELL_LONG,
                                taker=True, verify=False)
                            if r2.ok:
                                self.dump_today = round(
                                    self.dump_today + dq * bid_t, 2)
                                # the sale is journaled HERE, at the
                                # known price — dumps used to leave no
                                # record, so every one surfaced later
                                # as "closed by reconciliation, no
                                # price recorded" (owner, 2026-08-23).
                                # A rare partial fill rests at the bid
                                # and the exchange snapshot reconciles.
                                inv["qty"] -= dq
                                inv["cost"] -= dq * bid_t
                                left = round(inv["qty"], 2)
                                if abs(inv["qty"]) < 0.005:
                                    self.inventory.pop(slug, None)
                                    self.inv_since.pop(slug, None)
                                self._journal_fill(FamilyOrder(
                                    id=r2.order_id or f"dump{int(now)}",
                                    market=slug, side="SELL",
                                    price=bid_t, qty=dq,
                                    intent=SELL_LONG, placed_ts=now,
                                    purpose="sell",
                                    why="taker dump — sold into the "
                                        "bid (the carved exception)"),
                                    dq, now, left)
                                self._log(event="dump", market=slug,
                                          price=bid_t, qty=dq,
                                          note="sold into the bid — "
                                               "tight spread, above "
                                               "basis")
                                self._mark(slug, "SELL", now)
                                actions -= 1
                                continue
                if rest < 0.01:
                    continue
                if covered > 0.01 and not self._cooldown_ok(slug, "SELL",
                                                            now):
                    continue    # adjustments throttle; a bare position
                                # gets its exit NOW (owner, 2026-08-22:
                                # "no reason to wait")
                break_even = min(max(inv.get("cost", 0.0) / qty, 0.001), 0.989)
                floor_px, score_basis = self._exit_floor(
                    slug, "SELL", break_even, book.tick, book=book, qty=qty)
                ask_touch = (book.asks[0][0] if book.asks
                             else break_even + book.tick)
                lo = max(floor_px,
                         (book.bids[0][0] + book.tick) if book.bids
                         else 0.002)
                bound = max(ask_touch, floor_px) + 2 * book.tick
                stray = [o for o in mine if o.price > bound + 1e-9
                         and o.id in self.orders]
                if stray:
                    worst = max(stray, key=lambda o: o.price)
                    rr = self.desk.cancel(worst.id, worst.market)
                    if rr.ok:
                        self.orders.pop(worst.id, None)
                        self.evidence.order_gone(worst.market, worst.id)
                        self._log(event="stranded_exit_repriced",
                                  market=slug, price=worst.price,
                                  qty=worst.qty,
                                  note="past the touch and the allowed "
                                       "bound — re-resting where it can "
                                       "fill (owner, 2026-08-22)")
                        actions -= 1
                    continue
                # sell at the FRONT of the profitable range (owner,
                # 2026-08-22): join the ask touch — unless the touch is
                # a giveaway against the model, then rest just under fair
                fair_g = self.fairs(slug) if self.fairs is not None else None
                join_px = ask_touch
                if fair_g is not None and join_px < fair_g - 3 * book.tick:
                    join_px = fair_g - book.tick
                px = max(lo, min(join_px, 0.999))
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
                covered = sum(
                    o.qty for o in self.orders.values()
                    if o.market == slug and o.side == "BUY"
                    and o.purpose in ("sell", "manual"))
                rest = -qty - covered
                if covered > -qty + 0.01:
                    self._prune_excess_exits(slug, "BUY", covered + qty, now)
                if rest < 0.01:
                    continue
                if covered > 0.01 and not self._cooldown_ok(slug, "BUY",
                                                            now):
                    continue    # same rule for covers: bare shorts get
                                # their buy-back immediately
                received = min(max(-inv.get("cost", 0.0) / -qty, 0.002), 0.999)
                cap_px, score_basis = self._exit_floor(
                    slug, "BUY", received, book.tick, book=book, qty=-qty)
                bid_touch = (book.bids[0][0] if book.bids
                             else received - book.tick)
                hi = min(cap_px,
                         (book.asks[0][0] - book.tick) if book.asks
                         else cap_px)
                bound = min(bid_touch, cap_px) - 2 * book.tick
                stray = [o for o in mine if o.price < bound - 1e-9
                         and o.id in self.orders]
                if stray:
                    worst = min(stray, key=lambda o: o.price)
                    rr = self.desk.cancel(worst.id, worst.market)
                    if rr.ok:
                        self.orders.pop(worst.id, None)
                        self.evidence.order_gone(worst.market, worst.id)
                        self._log(event="stranded_exit_repriced",
                                  market=slug, price=worst.price,
                                  qty=worst.qty,
                                  note="past the touch and the allowed "
                                       "bound — re-resting where it can "
                                       "fill (owner, 2026-08-22)")
                        actions -= 1
                    continue
                px = self._best_exit_px(slug, "BUY", book,
                                        min(bid_touch, hi), hi, rest,
                                        basis=score_basis)
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
        # an "exit" with no position behind it is not an exit — a fill
        # would OPEN a position, not close one (the petbut shape; owner
        # approved 2026-08-21). Reduce-checking also catches covers left
        # on the wrong side after a phantom position was corrected.
        for rec in list(self.orders.values()):
            if actions <= 0:
                break
            if rec.purpose != "sell":
                continue
            if now - rec.placed_ts < 300.0:
                continue      # a fresh exit gets its feed cycle first
            pos = (self.inventory.get(rec.market) or {}).get("qty", 0.0)
            reduces = ((rec.side == "BUY" and pos < -0.005)
                       or (rec.side == "SELL" and pos > 0.005))
            if reduces:
                continue
            r = self.desk.cancel(rec.id, rec.market)
            if r.ok:
                self.orders.pop(rec.id, None)
                self.evidence.order_gone(rec.market, rec.id)
                self._log(event="orphan_exit_cancelled", market=rec.market,
                          price=rec.price, qty=rec.qty,
                          note="no position behind it — a fill would open "
                               "a new position, not close one")
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
            fair_pr = self.fairs(slug) if self.fairs is not None else None
            if fair_pr is not None:
                # scouts obey the hard cap too (owner, 2026-08-23)
                cap_pr = fair_pr - book.tick
                hi = cap_pr if hi is None else min(hi, cap_pr)
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
            top = (max(plans, key=lambda p: p.get("ev", p["est"]))
                   if plans else (grow[0] if grow else None))
            self.triage_feed.append({
                "ts": round(now, 1), "market": slug,
                "in": bool(plans or grow),
                "ev": round(best_ev, 2), "spread": spread_c,
                "pool": round(sp2, 2) if sp2 is not None else None,
                "conf": round(conf2, 2),
                "plan": (f"{'bid' if top['side'] == 'BUY' else 'ask'} "
                         f"{top['qty']:g} @ {top['px'] * 100:.0f}c"
                         if top else None),
                "book": {"b": [[p2, round(q2, 1)] for p2, q2 in book.bids[:6]],
                         "a": [[p2, round(q2, 1)] for p2, q2 in book.asks[:6]]},
                "picks": [{"s": p["side"], "px": p["px"], "q": p["qty"],
                           "ev": round(p.get("ev", p["est"]), 2)}
                          for p in plans[:2]],
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
                    "book": {"b": [[p2, round(q2, 1)]
                                   for p2, q2 in book3.bids[:6]],
                             "a": [[p2, round(q2, 1)]
                                   for p2, q2 in book3.asks[:6]]},
                    "picks": [{"s": p["side"], "px": p["px"], "q": p["qty"],
                               "ev": round(p.get("ev", p["est"]), 2)}
                              for p in plans[:2]],
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
            self.dump_today = 0.0
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
        if self.cfg.proven_usd > 0:
            summary["proven_spent"] = round(self.proven_spent(), 2)
            summary["proven_usd"] = self.cfg.proven_usd
            summary["proven_n"] = len(self.proven)
        summary["holdings_usd"] = round(self.holdings_value(), 2)
        summary["holdings_counted"] = bool(self.cfg.holdings_in_ceiling)
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
            "placed_at": self.placed_at,
            "pending_pages": self.pending_pages,
            "gone_pending": {oid: {"rec": asdict(g["rec"]),
                                   "until": g["until"]}
                             for oid, g in self.gone_pending.items()},
            "last_action": self.last_action,
            "known_dead": sorted(self.known_dead),
            "inv_since": self.inv_since,
            "fillmodel": self.fillmodel.to_dict(),
            "pending_marks": self.pending_marks[-60:],
            # 600 to match the in-memory retention trim: saving
            # only 200 silently discarded most of the journal on
            # every save, and threw away 300 of the 493 rows the
            # 2026-08-23 recovery had just rebuilt. data/fills.csv
            # and data/trades.csv remain the unbounded archives.
            "fills": self.fills[-600:],
            "scoreboard": self.scoreboard,
            "universe": self.universe,
            "terms": self.terms.to_dict(),
            "earned_today": round(self.earned_today, 4),
            "earned_day": self.earned_day,
            "dump_today": round(self.dump_today, 2),
            "earned_history": self.earned_history,
            "log": self.log[-self.cfg.log_keep:],
        }

    def restore(self, d: dict) -> None:
        for oid, v in (d.get("orders") or {}).items():
            rec = FamilyOrder(**{k: x for k, x in v.items()
                                 if k in FamilyOrder.__dataclass_fields__})
            if rec.why == "adopted from the earlier versions":
                # one-time migration (owner, 2026-08-22 "Don't let it
                # cancel orders I set by hand", then "Still getting
                # orders cancelled"): everything claimed by the old
                # adoption after the 1.0/2.0 retirement was the owner's
                # hand — relabel it untouchable.
                rec.purpose = "manual"
                rec.why = "the owner's own order — the engine leaves it alone"
            self.orders[oid] = rec
        self.inventory = dict(d.get("inventory") or {})
        self.positions_seen = dict(d.get("positions_seen") or {})
        self.silent_cancels = d.get("silent_cancels") or 0
        self.placed_at = {k: float(v) for k, v in
                          (d.get("placed_at") or {}).items()}
        self.pending_pages = list(d.get("pending_pages") or [])
        self.gone_pending = {}
        for oid, g in (d.get("gone_pending") or {}).items():
            try:
                self.gone_pending[oid] = {
                    "rec": FamilyOrder(**{k: x for k, x in g["rec"].items()
                                          if k in
                                          FamilyOrder.__dataclass_fields__}),
                    "until": float(g["until"])}
            except (KeyError, TypeError, ValueError):
                continue
        self.last_action = dict(d.get("last_action") or {})
        self.known_dead = set(d.get("known_dead") or ())
        self.inv_since = dict(d.get("inv_since") or {})
        if d.get("fillmodel"):
            self.fillmodel = FillModel.from_dict(d["fillmodel"])
        self.pending_marks = list(d.get("pending_marks") or [])
        self.fills = list(d.get("fills") or [])
        self.dump_today = float(d.get("dump_today") or 0.0)
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
