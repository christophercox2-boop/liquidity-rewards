"""Probe -> earn -> sell: the heart of 2.0.

Built to the owner's brief (REBUILD.md), on the two seats families
first, under one risk number, with every 1.0 lesson encoded:

* **One risk number.** The buying power allocated to 2.0 ($100 for the
  seats test). `used` = the worst-case loss of the whole book, with
  negative-risk netting inside each seats family (v2/risk.py — the
  Senate's exact rungs are mutually exclusive, so shorts across them
  mostly share one collateral); every placement must fit its MARGINAL
  risk in the headroom. No per-market caps, ladders or graduated
  budgets.
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
from dataclasses import dataclass, field, replace

from .books import BookCache
from .fillmodel import FillModel, family_of
from .intents import BUY_LONG, BUY_SHORT, SELL_LONG, SELL_SHORT, capital_at_risk
from .orders import OrderDesk
from .programs import daily_side_pool, slug_event_date
from .risk import (
    Leg, family_risk, leg_for_inventory, leg_for_order, marginal_risk,
    parse_rung,
)
from .scoring import estimate_join
from .silver import SilverFairs
from .terms import TermsStore

BOOK_MAX_AGE = 120.0

# calibration-probe bins over predicted p(fill in a day) — the reliability
# page uses finer bins, but for aiming probes five coarse ones suffice
PROBE_BINS = ((0.0, 0.05), (0.05, 0.15), (0.15, 0.35), (0.35, 0.65), (0.65, 1.01))


@dataclass
class EngineConfig:
    whitelist_prefixes: tuple[str, ...] = ("scc-senate-gop-2026-11-03-",
                                           "scc-hrep-rep-2026-11-03-")
    ceiling_usd: float = 300.0       # the one risk number (owner raised the
                                     # $100 seats-test ceiling to $300,
                                     # 2026-08-19 morning). The exchange's own
                                     # funding check stays the hard backstop:
                                     # orders it can't fund self-cancel and
                                     # show up as silent cancels.
    max_actions_per_cycle: int = 10  # rate-limit manners (owner raised 4 -> 10
                                     # alongside the $300 ceiling, 2026-08-19)
    # Size is chosen to MAXIMISE EV, not by a flat cap (owner, 2026-08-19:
    # "at some point, increasing size has no marginal earnings benefit on
    # only marginal fill cost, correct?" — correct: our share saturates at
    # the whole side pool while fill risk stays linear, so EV has a single
    # peak). max_order_usd is now only a concentration backstop — no one
    # order may risk more than max_order_frac of the ceiling.
    # A quarter of the ceiling: concentration backstop, not the sizing rule.
    # (Was a flat 40 for a few hours this morning; EV sizing supersedes it.)
    max_order_usd: float = 75.0
    # The peak sits at q* proportional to 1/sqrt(fill_cost), and fill_cost is
    # still the cautious 2c seed until real fills grade it. Until a family has
    # this many graded fills, take only this fraction of the EV-optimal size.
    size_safety: float = 0.5
    size_proven_marks: int = 10
    # An order that is EARNING was never touched before 2026-08-19, so the
    # size it was born with was the size it died with — new sizing rules
    # only ever reached new placements, and with every market-side occupied
    # that meant they never bit at all. The optimal size moves with the
    # book, so an earning order is now resized when the optimum has moved
    # materially and the gain clears churn.
    resize_ratio: float = 1.5
    resize_min_gain_day: float = 0.02
    # Depth ahead of our price is evidence in its own right: a taker must
    # consume it before reaching us. Size is justified when the model and
    # market agree (a fill would not cost much) OR when this many Target
    # Sizes of wall sit in front (a fill is unlikely in the first place) —
    # owner, 2026-08-19. Both routes still face the EV bar and the band
    # rails; neither can bid above the band or ask below it.
    shield_size_x: float = 2.0
    scout_qty: float = 1.0           # low-confidence probe size
    min_ev_day: float = 0.005        # don't rest for under half a cent/day of EV
    tight_band: float = 0.06         # model & market within this = high confidence
    tight_ratio: float = 3.0         # ...and within this RATIO: at a 5c tail,
                                     # "model 0.5c vs market 5c" is six cents of
                                     # width but a 10x disagreement — scouts only
                                     # (caught live 2026-08-19: sized tail bids)
    fair_margin: float = 0.01        # one cent beyond the band is still "at fair"
    horizon_s: float = 86400.0       # the day the EV is computed over
    mark_after_s: float = 3600.0     # grade each fill against the mid this much later
    forecasts_keep: int = 400
    # EXP-1's information budget: boundary-disagreement setups are diluted
    # by construction, so pure EV would never try them and the window
    # question would never get answered. A scout there may pay up to this
    # much expected value per day, with at most this many open at once.
    exp1_max_cost_day: float = 0.02
    exp1_max_open: int = 6
    # Calibration probes: the odds model only learns the bins we visit, and
    # pure EV keeps every order at near-zero fill odds (owner, 2026-08-19:
    # "we won't get a full picture of the odds if we just stick on the safe
    # side"). One-share orders aimed at the least-evidenced fill-odds bin,
    # each allowed to cost at most probe_max_cost_day of EV — bounded tuition.
    probe_max_open: int = 6
    probe_max_cost_day: float = 0.05
    # During a deploy rollover two 2.0 instances briefly coexist; each saw
    # the other's fresh orders as foreign automation and they evicted each
    # other's book in a loop (2026-08-19). A foreign order must be at least
    # this old before eviction touches it — twins never overlap this long.
    evict_grace_s: float = 600.0
    # Rotation: free the worst resting order when an unaffordable candidate
    # beats it by this factor (and by a real absolute margin) — capital
    # sits where EV says, not where it happened to land first.
    rotate_factor: float = 2.0
    rotate_min_gain_day: float = 0.02
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
    purpose: str     # earn / scout / sell / close / exp1
    # live evaluation, recomputed every cycle against the fresh book —
    # what the order is worth NOW, not what was predicted at placement
    live_est: float | None = None    # $/day earning at current book
    live_ev: float | None = None     # EV/day of leaving it where it is
    live_yield: float | None = None  # live_ev per dollar at risk
    live_parts: dict | None = None   # the EV's components, for /order —
                                     # share, ticks, p_fill, fill_cost,
                                     # scoring_frac, side_pool, band


def _order_age_s(o: dict, now: float) -> float | None:
    """Age of an exchange order from its createTime; None if unparseable."""
    raw = str(o.get("created") or "")
    if not raw:
        return None
    try:
        ts = dt.datetime.fromisoformat(raw.replace("Z", "+00:00")).timestamp()
        return max(now - ts, 0.0)
    except ValueError:
        return None


@dataclass
class Summary:
    mode: str
    used: float = 0.0
    headroom: float = 0.0
    actions: list = field(default_factory=list)


class Engine:
    def __init__(self, desk: OrderDesk, config: EngineConfig | None = None,
                 alert=None, clock=None, fill_model: FillModel | None = None):
        self.desk = desk
        self.cfg = config or EngineConfig()
        self.alert = alert or (lambda title, msg: None)
        self._clock = clock or time.time
        self.model = fill_model or FillModel()
        self.forecasts: dict[str, dict] = {}       # order id -> prediction + outcome
        self.pending_marks: list[dict] = []        # fills awaiting their 1h grade
        self.last_cands: list[dict] = []           # the engine's latest reasoning
        self.last_cands_rejected: list[dict] = []  # ...and what it turned down
        self.orders: dict[str, OwnOrder] = {}      # our resting orders by id
        self.inventory: dict[str, dict] = {}       # slug -> {qty, cost} (net of side)
        self.positions_seen: dict[str, float] = {} # last cycle's net per market
        self.family_sweep_done = False             # the one-time 1.0 handover
        self.sweep_count = 0
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

    def _family_legs(self, skip_order_id: str | None = None
                     ) -> tuple[dict[str, list[Leg]], float]:
        """The whole book as risk legs grouped by family, plus the
        per-order fallback total for anything that isn't a seats rung."""
        fams: dict[str, list[Leg]] = {}
        flat = 0.0
        for oid, o in self.orders.items():
            if oid == skip_order_id:
                continue
            fr = parse_rung(o.market)
            leg = (leg_for_order(fr[1], o.intent, o.price, o.qty)
                   if fr is not None else None)
            if fr is not None and leg is not None:
                fams.setdefault(fr[0], []).append(leg)
            elif fr is None:
                flat += capital_at_risk(o.intent, o.price, o.qty)
        for slug, inv in self.inventory.items():
            fr = parse_rung(slug)
            leg = (leg_for_inventory(fr[1], inv.get("qty", 0.0),
                                     inv.get("cost", 0.0))
                   if fr is not None else None)
            if fr is not None and leg is not None:
                fams.setdefault(fr[0], []).append(leg)
            elif fr is None:
                flat += max(inv.get("cost", 0.0), 0.0)
        return fams, flat

    def used_capital(self) -> float:
        """Worst-case dollars the whole book can lose — negative-risk
        netting inside each seats family (owner, 2026-08-19), families
        summed because their seat counts are separate unknowns."""
        fams, flat = self._family_legs()
        return round(sum(family_risk(legs) for legs in fams.values()) + flat, 2)

    def risk_by_family(self) -> dict[str, float]:
        """The worst case per family, for the page."""
        fams, flat = self._family_legs()
        out = {fam: round(family_risk(legs), 2) for fam, legs in fams.items()}
        if flat:
            out["other"] = round(flat, 2)
        return out

    def _candidate_leg(self, slug: str, side: str, price: float,
                       qty: float) -> Leg | None:
        """The leg a would-be order adds, with the intent the desk would
        actually use: an ask sells held stock (no new risk) when there is
        enough of it, otherwise it opens a short."""
        fr = parse_rung(slug)
        if fr is None:
            return None
        net = (self.inventory.get(slug) or {}).get("qty", 0.0)
        if side == "SELL":
            intent = SELL_LONG if net >= qty else BUY_SHORT
        else:
            intent = BUY_LONG
        return leg_for_order(fr[1], intent, price, qty)

    def marginal_cost(self, slug: str, side: str, price: float,
                      qty: float) -> float:
        """What one more order adds to the worst case — the honest cost of
        a candidate. An ask on an exact-count rung already dominated by a
        bigger short elsewhere in the family adds nothing; a short on a
        nested House rung in a red-wave book adds its full collateral."""
        fr = parse_rung(slug)
        if fr is None:
            cost_ps = price if side == "BUY" else 1.0 - price
            return round(cost_ps * qty, 2)
        leg = self._candidate_leg(slug, side, price, qty)
        fams, _ = self._family_legs()
        return round(marginal_risk(fams.get(fr[0], []), leg), 2)

    def order_marginal(self, rec: "OwnOrder") -> float:
        """What one RESTING order contributes to the worst case — the
        capital freed if it were cancelled. The denominator live yields
        divide by."""
        fr = parse_rung(rec.market)
        if fr is None:
            return round(capital_at_risk(rec.intent, rec.price, rec.qty), 2)
        fams, _ = self._family_legs(skip_order_id=rec.id)
        leg = (leg_for_order(fr[1], rec.intent, rec.price, rec.qty)
               if fr is not None else None)
        return round(marginal_risk(fams.get(fr[0], []), leg), 2)

    def _probe_candidate(self, books: BookCache, terms: TermsStore,
                         silver: SilverFairs, now: float,
                         busy: set | None = None) -> dict | None:
        """One 1-share order aimed at the fill-odds bin with the least
        evidence on record. Same rails as everything else — the band, the
        never-cross check, the whitelist at the desk — only the EV bar is
        relaxed to -probe_max_cost_day: the price of a labeled data point
        the calibration page can grade. `busy` is the set of (market, side)
        slots real candidates want this cycle: a probe must never squat on
        a side that size is waiting to use (it once blocked a rotation)."""
        busy = busy or set()
        counts = [0] * len(PROBE_BINS)
        for fc in self.forecasts.values():
            p = fc.get("p_fill")
            if p is None:
                continue
            for i, (a, z) in enumerate(PROBE_BINS):
                if a <= p < z:
                    counts[i] += 1
                    break
        emptiness = sorted(range(len(PROBE_BINS)), key=lambda i: counts[i])
        have = {(o.market, o.side) for o in self.orders.values()}
        best: dict | None = None
        best_rank = None
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
            lo, hi, _src = b
            side_pool = daily_side_pool(prog, slug)
            for side in ("BUY", "SELL"):
                if ((slug, side) in have or (slug, side) in busy
                        or not self._cooldown_ok(slug, side, now)):
                    continue
                levels = book.side(side)
                if not levels:
                    continue
                touch = levels[0][0]
                sign = 1.0 if side == "BUY" else -1.0
                other = book.side("SELL" if side == "BUY" else "BUY")
                fair_ref = lo if side == "BUY" else hi
                for i, px in enumerate([touch + sign * book.tick, touch,
                                        touch - sign * book.tick,
                                        touch - 2 * sign * book.tick]):
                    px = round(px, 3)
                    if not (0.001 <= px <= 0.999):
                        continue
                    if i == 0 and other and (px >= other[0][0] - 1e-9 if side == "BUY"
                                             else px <= other[0][0] + 1e-9):
                        continue
                    if side == "BUY" and px > hi + self.cfg.fair_margin:
                        continue
                    if side == "SELL" and px < lo - self.cfg.fair_margin:
                        continue
                    j = estimate_join(side, list(levels), book.tick, prog.df,
                                      prog.target, px, self.cfg.scout_qty)
                    if not j.qualifies:
                        continue
                    p_f = self.model.p_fill(slug, side, j.ticks, self.cfg.horizon_s)
                    f_cost = self.model.fill_cost(slug, side, px, fair_ref)
                    earn = (j.share * side_pool * self.model.scoring_fraction(slug)
                            if j.in_window else 0.0)
                    ev = earn - p_f * f_cost * self.cfg.scout_qty
                    if ev < -self.cfg.probe_max_cost_day:
                        continue
                    bin_i = next(k for k, (a, z) in enumerate(PROBE_BINS)
                                 if a <= p_f < z)
                    rank = (emptiness.index(bin_i), -ev)
                    if best_rank is None or rank < best_rank:
                        best_rank = rank
                        best = {"market": slug, "side": side, "price": px,
                                "qty": self.cfg.scout_qty,
                                "est_day": round(earn, 4),
                                "exp_earn": round(earn, 4),
                                "p_fill": round(p_f, 4),
                                "fill_cost": round(f_cost, 4),
                                "ev": round(ev, 4),
                                "cost": self.marginal_cost(
                                    slug, side, px, self.cfg.scout_qty),
                                "ticks": j.ticks, "purpose": "probe"}
        return best

    def band_tight(self, lo: float, hi: float) -> bool:
        """Agreement means close in cents AND close proportionally, at both
        ends of the price range. Absolute width alone lets a tail pass —
        model 0.5c vs market 5c is under six cents of width but a tenfold
        disagreement, and sizing there is exactly what scouts are for."""
        return ((hi - lo) <= self.cfg.tight_band
                and hi <= self.cfg.tight_ratio * max(lo, 0.01)
                and (1.0 - lo) <= self.cfg.tight_ratio * max(1.0 - hi, 0.01))

    def _best_size(self, slug, side, px, levels, book, prog, side_pool,
                   fair_ref, shield, max_usd):
        """The EV-maximising size for this order, and its numbers.

        Earnings are concave in size — our share is q.d/(W + q.d), which
        saturates at the whole side pool — while fill risk is linear in
        size. So EV rises, peaks, and falls, and past the peak every extra
        share costs more in expected fill than it earns (owner, 2026-08-19).

        Searched numerically against the real scoring function rather than
        solved in closed form: our own size moves the Target Size window
        boundary, so the analytic optimum is only locally right and can
        recommend a size that scores nothing.

        Returns (qty, estimate, p_fill, fill_cost, ev) for the best size,
        or None when no size scores.
        """
        cost_ps = px if side == "BUY" else 1.0 - px
        if cost_ps <= 0:
            return None
        ceiling_qty = max_usd / cost_ps
        sf = self.model.scoring_fraction(slug)
        f_cost = self.model.fill_cost(slug, side, px, fair_ref)
        sizes, q = [], float(self.cfg.scout_qty)
        while q < ceiling_qty:
            sizes.append(q)
            q *= 1.5
        sizes.append(ceiling_qty)
        best = None
        for q in sizes:
            q = round(q, 2)
            if q < self.cfg.scout_qty:
                continue
            j = estimate_join(side, list(levels), book.tick, prog.df,
                              prog.target, px, q)
            if not (j.qualifies and j.in_window):
                continue
            p_f = self.model.p_fill(slug, side, j.ticks, self.cfg.horizon_s,
                                    shield=shield, target=prog.target)
            ev = j.share * side_pool * sf - p_f * f_cost * q
            if best is None or ev > best[4]:
                best = (q, j, p_f, f_cost, ev)
        if best is None:
            return None
        # Until real fills have graded the cost side, take only a fraction
        # of the peak: q* scales as 1/sqrt(fill_cost), so an optimistic
        # cost seed overstates the right size.
        proven = (self.model.marks_n.get(family_of(slug), 0)
                  >= self.cfg.size_proven_marks)
        if not proven and best[0] > self.cfg.scout_qty:
            q = max(round(best[0] * self.cfg.size_safety, 2), self.cfg.scout_qty)
            j = estimate_join(side, list(levels), book.tick, prog.df,
                              prog.target, px, q)
            if j.qualifies and j.in_window:
                p_f = self.model.p_fill(slug, side, j.ticks, self.cfg.horizon_s,
                                        shield=shield, target=prog.target)
                best = (q, j, p_f, best[3],
                        j.share * side_pool * sf - p_f * best[3] * q)
        return best

    @staticmethod
    def _shield(book, side: str, price: float, own_qty: float = 0.0) -> float:
        """Contracts a taker must consume before reaching our price:
        everything resting at a better price than ours, plus whatever
        already sits at our own level (queue priority ahead of a new
        order). For a bid, "better" is higher; for an ask, lower."""
        total = 0.0
        for px, qty in book.side(side):
            if (px > price + 1e-9) if side == "BUY" else (px < price - 1e-9):
                total += qty
            elif abs(px - price) < 1e-9:
                total += max(qty - own_qty, 0.0)
        return total

    @staticmethod
    def _book_less_own(book, rec: "OwnOrder"):
        """The book as it would look without this resting order: its own
        size subtracted from its price level (level dropped if nothing
        else rests there). Books are fetched after placement, so they
        carry our size; any re-scoring must not count it twice."""
        levels = []
        for p, q in book.side(rec.side):
            if abs(p - rec.price) < 1e-9:
                q -= rec.qty
                if q <= 1e-9:
                    continue
            levels.append((p, q))
        if rec.side == "BUY":
            return replace(book, bids=tuple(levels))
        return replace(book, asks=tuple(levels))

    def _cooldown_ok(self, slug: str, side: str, now: float) -> bool:
        return now - self.last_action.get(f"{slug}|{side}", 0.0) >= self.cfg.action_cooldown_s

    def _mark_action(self, slug: str, side: str, now: float) -> None:
        self.last_action[f"{slug}|{side}"] = now

    # ------------------------------------------------------------- fair bands

    def band(self, slug: str, book, silver: SilverFairs):
        """(lo, hi, source): the envelope of the model's OWN uncertainty
        interval and the market's mid. The interval is the spread across
        Silver's Classic/Deluxe/Lite simulated seat histograms (both
        chambers), widened by the swing-correlation fallback when the
        official run is stale — see silver.fair_range. Tight envelope =
        the flavors agree AND the market agrees = confidence. Anything
        else scouts."""
        rng = silver.fair_range(slug)
        mid = None
        if book and book.bids and book.asks:
            mid = (book.bids[0][0] + book.asks[0][0]) / 2
        vals = ([rng[0], rng[1]] if rng is not None else []) + \
               ([mid] if mid is not None else [])
        if not vals:
            return None
        lo, hi = min(vals), max(vals)
        if rng is None or mid is None:   # one voice is never confident
            lo, hi = max(lo - 0.10, 0.001), min(hi + 0.10, 0.999)
        src = ("model+market" if rng is not None and mid is not None
               else "model" if rng is not None else "market")
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
                self._close_forecast(oid, "silent_cancel", now)
                self._log(event="silent_cancel", market=rec.market, side=rec.side,
                          price=rec.price, qty=rec.qty, id=oid)
            del self.orders[oid]
        self.positions_seen = {m: v[0] for m, v in positions.items()}

    def _record_forecast(self, c: dict, order_id: str, now: float) -> None:
        """Every placement is a prediction on the record: p(fill), expected
        earnings, expected fill cost. Outcomes land on the same row, which
        is what makes calibration possible."""
        self.forecasts[order_id] = {
            "id": order_id,
            "ts": round(now, 1), "market": c["market"], "side": c["side"],
            "price": c["price"], "qty": c["qty"], "ticks": c.get("ticks"),
            "p_fill": c.get("p_fill"), "exp_earn": c.get("exp_earn"),
            "fill_cost": c.get("fill_cost"), "ev": c.get("ev"),
            "purpose": c.get("purpose"),
        }
        while len(self.forecasts) > self.cfg.forecasts_keep:
            closed = next((k for k, v in self.forecasts.items() if v.get("how")), None)
            del self.forecasts[closed or next(iter(self.forecasts))]

    def _close_forecast(self, order_id: str, how: str, now: float,
                        filled_qty: float = 0.0) -> None:
        f = self.forecasts.get(order_id)
        if f is None:
            return
        f["how"] = how
        f["end_ts"] = round(now, 1)
        f["rested_s"] = round(now - f["ts"], 1)
        if filled_qty:
            f["filled_qty"] = filled_qty

    def _on_fill(self, rec: OwnOrder, qty: float, now: float) -> None:
        """Book the fill into OUR OWN ledger. The account's positions are
        shared with 1.0 (which holds seats inventory of its own), so the
        engine's inventory is built strictly from its own fills — adopting
        account positions wholesale once put $34 of 1.0's stock inside
        2.0's ceiling and would have had the seller acting on positions
        nobody gave it."""
        inv = self.inventory.setdefault(rec.market, {"qty": 0.0, "cost": 0.0})
        if rec.intent == BUY_LONG:
            inv["qty"] += qty
            inv["cost"] += qty * rec.price
        elif rec.intent == SELL_LONG:
            share = qty / max(inv["qty"], qty)
            inv["cost"] -= inv["cost"] * share
            inv["qty"] -= qty
        elif rec.intent == BUY_SHORT:
            inv["qty"] -= qty
            inv["cost"] += qty * (1.0 - rec.price)
        elif rec.intent == SELL_SHORT:
            share = qty / max(-inv["qty"], qty)
            inv["cost"] -= inv["cost"] * share
            inv["qty"] += qty
        if abs(inv["qty"]) < 0.01:
            del self.inventory[rec.market]
        self._close_forecast(rec.id, "fill", now, filled_qty=qty)
        self.pending_marks.append({"id": rec.id, "market": rec.market,
                                   "side": rec.side, "price": rec.price,
                                   "ts": now})
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
        """The engine's reasoning for one market: a ladder of candidate
        prices per side — improve the touch, join it, or stand one or two
        ticks back — each scored as expected value over the horizon:

            EV/day = earn_rate x scoring_fraction
                     - p(fill within the day) x cost_of_that_fill x qty

        (owner's directive 2026-08-19). Earning pulls toward the touch,
        fill risk pushes away; the calibrated model arbitrates and the
        best EV wins. Fair-band rails stay as hard limits on top."""
        lo, hi, src = band
        tight = self.band_tight(lo, hi)
        side_pool = daily_side_pool(prog, slug)
        out = []
        for side in ("BUY", "SELL"):
            levels = book.side(side)
            if not levels:
                continue
            best = levels[0][0]
            sign = 1.0 if side == "BUY" else -1.0
            prices = [best + sign * book.tick, best,
                      best - sign * book.tick, best - 2 * sign * book.tick]
            other = book.side("SELL" if side == "BUY" else "BUY")
            fair_ref = lo if side == "BUY" else hi   # concede against the worse edge
            for i, px in enumerate(prices):
                px = round(px, 3)
                if not (0.001 <= px <= 0.999):
                    continue
                if i == 0 and other and (px >= other[0][0] - 1e-9 if side == "BUY"
                                         else px <= other[0][0] + 1e-9):
                    continue          # improving must never cross
                # fair rails: never bid above the band, never ask below it
                if side == "BUY" and px > hi + self.cfg.fair_margin:
                    continue
                if side == "SELL" and px < lo - self.cfg.fair_margin:
                    continue
                cost_ps = px if side == "BUY" else 1.0 - px
                # two independent routes to size: the model and market agree
                # on VALUE (a fill would not cost much), or a wall of resting
                # contracts sits in front of us (a fill is unlikely at all).
                # Either way the EV bar and the band rails still apply.
                shield = self._shield(book, side, px)
                walled = (prog.target
                          and shield >= self.cfg.shield_size_x * prog.target)
                confident = tight or walled
                if confident:
                    # size to the EV peak, not to a flat dollar cap
                    got = self._best_size(slug, side, px, levels, book, prog,
                                          side_pool, fair_ref, shield,
                                          self.cfg.max_order_usd)
                    if got is None:
                        continue
                    qty, j, p_f, f_cost, ev = got
                else:
                    qty = self.cfg.scout_qty
                    j = estimate_join(side, list(levels), book.tick, prog.df,
                                      prog.target, px, qty)
                    if not (j.qualifies and j.in_window):
                        continue
                    p_f = self.model.p_fill(slug, side, j.ticks,
                                            self.cfg.horizon_s, shield=shield,
                                            target=prog.target)
                    f_cost = self.model.fill_cost(slug, side, px, fair_ref)
                    ev = (j.share * side_pool * self.model.scoring_fraction(slug)
                          - p_f * f_cost * qty)
                earn = j.share * side_pool * self.model.scoring_fraction(slug)
                # the cost that gates the ceiling and ranks candidates is
                # MARGINAL family risk — an ask already dominated by a
                # bigger short on an exclusive sibling rung is nearly free
                cost = self.marginal_cost(slug, side, px, qty)
                cand = {"market": slug, "side": side, "price": px, "qty": qty,
                        "est_day": round(j.share * side_pool, 4),
                        "exp_earn": round(earn, 4), "p_fill": round(p_f, 4),
                        "fill_cost": round(f_cost, 4), "ev": round(ev, 4),
                        "cost": cost, "yield": ev / max(cost, 0.05),
                        "ticks": j.ticks,
                        "shield": round(shield, 1),
                        "purpose": "earn" if confident else "scout",
                        "exp1_gap": j.in_window and not j.in_window_queue,
                        "pred_level": round(j.share * side_pool, 4),
                        "pred_queue": round(j.share_if_queue * side_pool, 4),
                        "band": (round(lo, 3), round(hi, 3), src)}
                if ev >= self.cfg.min_ev_day:
                    out.append(cand)
                elif cand["exp1_gap"]:
                    # retry at scout size: the information trade
                    j1 = estimate_join(side, list(levels), book.tick, prog.df,
                                       prog.target, px, self.cfg.scout_qty)
                    earn1 = j1.share * side_pool * self.model.scoring_fraction(slug)
                    ev1 = earn1 - p_f * f_cost * self.cfg.scout_qty
                    if (j1.qualifies and j1.in_window
                            and ev1 >= -self.cfg.exp1_max_cost_day):
                        out.append({**cand, "qty": self.cfg.scout_qty,
                                    "exp_earn": round(earn1, 4),
                                    "ev": round(ev1, 4),
                                    "cost": self.marginal_cost(
                                        slug, side, px, self.cfg.scout_qty),
                                    "yield": ev1,
                                    "pred_level": round(j1.share * side_pool, 4),
                                    "pred_queue": round(j1.share_if_queue * side_pool, 4),
                                    "purpose": "exp1"})
                    else:
                        self.last_cands_rejected.append(cand)
                else:
                    self.last_cands_rejected.append(cand)
        return out

    # ------------------------------------------------------------------- act

    def cycle(self, now: float, open_orders: list[dict],
              positions: dict[str, tuple], books: BookCache, terms: TermsStore,
              silver: SilverFairs, switch_on: bool) -> dict:
        self.last_cands_rejected = []
        self.reconcile(open_orders, positions, now)
        self._grade_pending_marks(books, now)

        # The owner-approved handover sweep (2026-08-18, "clear them out"):
        # 1.0's resting orders in the seats families are cancelled so the
        # families become fully 2.0's. OPENING orders only — exits
        # (SELL_LONG asks unwinding held stock, SELL_SHORT bids closing
        # shorts) stay and finish their job, per the standing rule that
        # 1.0 may still reduce what it already holds. Runs once, a few
        # cancels per cycle for the rate limiter, works with the switch
        # off (cancelling only reduces exposure), then never again.
        # (2026-08-20, the 3.0 floor:) the sweep now also requires the
        # switch argument, which main forces False while 3.0 has the floor
        # — under the interlock 2.0 must touch nothing, and 3.0's adopted
        # seats orders must never read as "1.0 leftovers" to clear.
        if not self.family_sweep_done and switch_on:
            foreign = [o for o in open_orders
                       if self.whitelisted(o.get("market", ""))
                       and o["id"] not in self.orders
                       and o.get("intent") in (BUY_LONG, BUY_SHORT)]
            for o in foreign[:8]:
                r = self.desk.cancel(o["id"], o["market"])
                if r.ok:
                    self.sweep_count += 1
                    self._log(event="handover_cancel", market=o["market"],
                              side=o.get("side"), price=o.get("price"),
                              qty=o.get("size"), id=o["id"])
            if not foreign:
                self.family_sweep_done = True
                self.alert("Seats handover done",
                           f"cleared {self.sweep_count} 1.0 orders from the seats "
                           f"families; exit orders were left to finish")

        s = Summary(mode="on" if switch_on else "observing")
        s.used = self.used_capital()
        s.headroom = round(self.cfg.ceiling_usd - s.used, 2)
        if not switch_on:
            return self._summary(s)

        actions_left = self.cfg.max_actions_per_cycle

        # exclusivity, continuously: automation that slips back into our
        # families is removed; an owner hand-placed order is left alone
        # and only recorded
        if self.family_sweep_done:
            for o in open_orders:
                if actions_left <= 0:
                    break
                if (not self.whitelisted(o.get("market", ""))
                        or o["id"] in self.orders
                        or o.get("intent") not in (BUY_LONG, BUY_SHORT)):
                    continue
                if o.get("manual"):
                    self._log(event="foreign_manual_order", market=o["market"],
                              id=o["id"])
                    continue
                age = _order_age_s(o, now)
                if age is None or age < self.cfg.evict_grace_s:
                    # a fresh foreign order is probably our rollover twin's —
                    # the mutual-eviction loop of 2026-08-19 must not repeat
                    continue
                r = self.desk.cancel(o["id"], o["market"])
                if r.ok:
                    self._log(event="evict", market=o["market"], id=o["id"],
                              age_s=round(age))
                    actions_left -= 1

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
                    self._close_forecast(rec.id, "pulled", now)
                    self._log(event="exit", market=rec.market, why=why, id=rec.id)
                    del self.orders[rec.id]
                    actions_left -= 1

        # 1b) orphaned exits: a sell/close order must be backed by our own
        # inventory — if the ledger holds nothing there (sold elsewhere, or
        # the ledger migration dropped inherited stock), pull the order.
        for rec in list(self.orders.values()):
            if actions_left <= 0:
                break
            if rec.purpose not in ("sell", "close"):
                continue
            if not self.inventory.get(rec.market):
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    self._close_forecast(rec.id, "pulled", now)
                    self._log(event="orphan_exit_pulled", market=rec.market,
                              side=rec.side, price=rec.price, qty=rec.qty)
                    del self.orders[rec.id]
                    actions_left -= 1

        # 2) maintenance: every order is re-evaluated against the live book
        # (that's what /orders shows), and one out of the window or outside
        # its band moves
        for rec in list(self.orders.values()):
            if rec.purpose in ("sell", "close"):
                # exits are the seller's to manage, never repriced here —
                # but waiting stock EARNS while it rests (owner, 2026-08-20:
                # "how much the stock that is being sold is earning per
                # day?"), so they get the same live reading as everything
                # else. No fill-cost side: an exit's fill is the goal.
                book = books.fresh(rec.market, BOOK_MAX_AGE, now)
                prog = terms.get(rec.market)
                if book is None or prog is None:
                    continue
                unbooked = self._book_less_own(book, rec)
                here = estimate_join(rec.side, list(unbooked.side(rec.side)),
                                     book.tick, prog.df, prog.target,
                                     rec.price, rec.qty)
                earning_here = here.qualifies and here.in_window
                side_pool = daily_side_pool(prog, rec.market)
                sc_frac = self.model.scoring_fraction(rec.market)
                rec.live_est = round(here.share * side_pool
                                     if earning_here else 0.0, 4)
                rec.live_ev = round((rec.live_est or 0.0) * sc_frac, 4)
                rec.live_parts = {
                    "share": round(here.share, 4), "ticks": here.ticks,
                    "in_window": here.in_window, "qualifies": here.qualifies,
                    "scoring_frac": round(sc_frac, 3),
                    "side_pool": round(side_pool, 4), "exit": True,
                }
                continue
            book = books.fresh(rec.market, BOOK_MAX_AGE, now)
            prog = terms.get(rec.market)
            if book is None or prog is None:
                continue
            b = self.band(rec.market, book, silver)
            if b is None:
                continue
            # score against the book WITHOUT this order — the fetched book
            # already contains it, and estimate_join adds its size back as
            # the join; leaving it in counted the order twice and roughly
            # halved its share (/orders read $7.84/d while the estimator
            # said $12.27/d for the same books, 2026-08-19)
            unbooked = self._book_less_own(book, rec)
            here = estimate_join(rec.side, list(unbooked.side(rec.side)),
                                 book.tick, prog.df, prog.target,
                                 rec.price, rec.qty)
            earning_here = here.qualifies and here.in_window
            self.model.observe_scoring(rec.market, earning_here)
            # live evaluation: what this order earns and risks RIGHT NOW
            side_pool = daily_side_pool(prog, rec.market)
            live_est = here.share * side_pool if earning_here else 0.0
            lo, hi, _src = b
            fair_ref = lo if rec.side == "BUY" else hi
            shield = self._shield(unbooked, rec.side, rec.price)
            p_f = self.model.p_fill(rec.market, rec.side, here.ticks,
                                    self.cfg.horizon_s, shield=shield,
                                    target=prog.target)
            f_cost = self.model.fill_cost(rec.market, rec.side, rec.price, fair_ref)
            sc_frac = self.model.scoring_fraction(rec.market)
            rec.live_est = round(live_est, 4)
            rec.live_ev = round(live_est * sc_frac - p_f * f_cost * rec.qty, 4)
            # every component, so /order can show the working, not just the sum
            rec.live_parts = {
                "share": round(here.share, 4), "ticks": here.ticks,
                "in_window": here.in_window, "qualifies": here.qualifies,
                "p_fill": round(p_f, 4), "fill_cost": round(f_cost, 4),
                "shield": round(shield, 1), "target": prog.target,
                "scoring_frac": round(sc_frac, 3),
                "side_pool": round(side_pool, 4),
                "band": [round(lo, 3), round(hi, 3), _src],
            }
            risk = self.order_marginal(rec)
            rec.live_yield = round(rec.live_ev / max(risk, 0.05), 4)
            if actions_left <= 0 or not self._cooldown_ok(rec.market, rec.side, now):
                continue
            # reprice candidates ask "where would this size rest best?" —
            # also a question about the book without the order that would move
            cands = [c for c in self._candidates(rec.market, unbooked, prog, b, now)
                     if c["side"] == rec.side]
            best = max(cands, key=lambda c: c["yield"], default=None)
            lo, hi, _src = b
            guard_broken = (rec.price > hi + self.cfg.fair_margin
                            if rec.side == "BUY"
                            else rec.price < lo - self.cfg.fair_margin)
            # size belongs only where model and market agree; an earn-sized
            # order whose band no longer qualifies gets pulled the same way
            # (a scout may replace it next cycle)
            walled_now = (prog.target
                          and shield >= self.cfg.shield_size_x * prog.target)
            detightened = (rec.purpose == "earn"
                           and rec.qty > self.cfg.scout_qty
                           and not self.band_tight(lo, hi)
                           and not walled_now)
            if guard_broken or detightened:
                r = self.desk.cancel(rec.id, rec.market)
                if r.ok:
                    self._close_forecast(rec.id, "pulled", now)
                    self._log(event="pull", market=rec.market, side=rec.side,
                              why=("fair band moved" if guard_broken
                                   else "no longer tight and the wall is gone"
                                        " — size withdrawn"),
                              price=rec.price)
                    del self.orders[rec.id]
                    self._mark_action(rec.market, rec.side, now)
                    actions_left -= 1
                continue
            if rec.purpose == "probe":
                continue   # a probe must REST where it was aimed — moving it
                           # to the EV-optimal spot destroys the data point
            if not earning_here and best is not None and abs(
                    best["price"] - rec.price) > 1e-9:
                r = self.desk.reprice(
                    {"id": rec.id, "market": rec.market, "side": rec.side,
                     "price": rec.price, "size": rec.qty, "intent": rec.intent},
                    best["price"], new_qty=best["qty"])
                if r.ok:
                    if r.two_orders:
                        self.alert("Two orders resting",
                                   f"{rec.market} {rec.side}: replacement "
                                   f"{r.order_id} rests, original didn't cancel")
                    self._close_forecast(rec.id, "repriced", now)
                    del self.orders[rec.id]
                    self.orders[r.order_id] = OwnOrder(
                        id=r.order_id, market=rec.market, side=rec.side,
                        price=best["price"], qty=best["qty"], intent=rec.intent,
                        placed_ts=now, purpose=best.get("purpose", rec.purpose))
                    self._record_forecast(best, r.order_id, now)
                    self._register_exp1(best, now)
                    self._log(event="reprice", market=rec.market, side=rec.side,
                              frm=rec.price, to=best["price"])
                    self._mark_action(rec.market, rec.side, now)
                    actions_left -= 1
            elif (earning_here and best is not None
                  and rec.purpose in ("earn", "scout")
                  and abs(best["price"] - rec.price) < 1e-9
                  and best["qty"] > 0):
                # same price, different size: the EV optimum moves with the
                # book, and an order sitting at its birth size is leaving
                # money (or risk) on the table
                moved = (best["qty"] >= rec.qty * self.cfg.resize_ratio
                         or best["qty"] <= rec.qty / self.cfg.resize_ratio)
                gain = (best.get("ev") or 0.0) - (rec.live_ev or 0.0)
                fits = best["cost"] <= self.cfg.ceiling_usd - self.used_capital()
                if moved and gain >= self.cfg.resize_min_gain_day and fits:
                    r = self.desk.reprice(
                        {"id": rec.id, "market": rec.market, "side": rec.side,
                         "price": rec.price, "size": rec.qty,
                         "intent": rec.intent},
                        rec.price, new_qty=best["qty"])
                    if r.ok:
                        if r.two_orders:
                            self.alert("Two orders resting",
                                       f"{rec.market} {rec.side}: replacement "
                                       f"{r.order_id} rests, original didn't cancel")
                        self._close_forecast(rec.id, "resized", now)
                        del self.orders[rec.id]
                        self.orders[r.order_id] = OwnOrder(
                            id=r.order_id, market=rec.market, side=rec.side,
                            price=rec.price, qty=best["qty"], intent=rec.intent,
                            placed_ts=now,
                            purpose=best.get("purpose", rec.purpose))
                        self._record_forecast(best, r.order_id, now)
                        self._log(event="resize", market=rec.market,
                                  side=rec.side, price=rec.price,
                                  frm=rec.qty, to=best["qty"],
                                  gain=round(gain, 3))
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
            # NOTHING RESTS IN A MARKET THAT PAYS NOTHING — not even an exit.
            # Step 1 above pulls every order out of a dead-program market, so
            # a seller that keeps re-listing there just fights it: when the
            # seats programs vanished on 2026-08-20 this pair looped
            # place->cancel every six minutes across nine markets for two
            # hours (~85 order calls per half hour, feeding the rate limits)
            # and the owner watched fresh orders keep appearing: "This is
            # still going on." The position stays, visible, and is the
            # owner's to unwind — his call, same day: "You can remove the
            # unwinding positions as well. I'll replace those if necessary."
            prog_here = terms.get(slug)
            if prog_here is None or not prog_here.is_live() or not prog_here.pool:
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
        self.last_cands = cands[:40]
        self.last_cands_rejected = sorted(self.last_cands_rejected,
                                          key=lambda c: -c["ev"])[:12]
        placed_keys: set[tuple[str, str]] = set()
        for c in cands:
            if actions_left <= 0:
                break
            if (c["market"], c["side"]) in placed_keys:
                continue              # one order per side per market per cycle
            if (c["purpose"] == "exp1"
                    and sum(1 for o in self.orders.values()
                            if o.purpose == "exp1") >= self.cfg.exp1_max_open):
                continue              # the information budget is bounded too
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
                self._record_forecast(c, r.order_id, now)
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

        # 4b) calibration probes — after the earners, inside leftover actions:
        # the odds model only learns the bins we visit
        if actions_left > 0:
            probes_open = sum(1 for o in self.orders.values()
                              if o.purpose == "probe")
            if probes_open < self.cfg.probe_max_open:
                busy = {(c["market"], c["side"]) for c in cands} | placed_keys
                c = self._probe_candidate(books, terms, silver, now, busy)
                if (c is not None
                        and (c["market"], c["side"]) not in placed_keys
                        and c["cost"] <= self.cfg.ceiling_usd - self.used_capital()):
                    net = (self.inventory.get(c["market"]) or {}).get("qty", 0.0)
                    r = self.desk.place_resting(c["market"], c["side"],
                                                c["price"], c["qty"],
                                                net_position=net)
                    if r.ok:
                        self.orders[r.order_id] = OwnOrder(
                            id=r.order_id, market=c["market"], side=c["side"],
                            price=c["price"], qty=c["qty"], intent=r.intent,
                            placed_ts=now, purpose="probe")
                        self._record_forecast(c, r.order_id, now)
                        self._log(event="place", **{k: c[k] for k in
                                  ("market", "side", "price", "qty",
                                   "est_day", "purpose")})
                        s.actions.append(f"probe {c['market']} {c['side']} "
                                         f"{c['qty']:g} @ {c['price'] * 100:g}c")
                        self._mark_action(c["market"], c["side"], now)
                        placed_keys.add((c["market"], c["side"]))
                        actions_left -= 1

        # 5) rotation — the answer to "opps has good ideas, is anything
        # cycling out?": when the best idea we could not afford beats the
        # worst thing we hold decisively, free the worst. The better one
        # places next cycle with the freed capital. One per cycle, and only
        # decisive wins move — queue position is capital too.
        if actions_left > 0:
            headroom = self.cfg.ceiling_usd - self.used_capital()
            unafford = [c for c in cands
                        if (c["market"], c["side"]) not in placed_keys
                        and c["purpose"] != "exp1" and c["cost"] > headroom]
            resting = [r for r in self.orders.values()
                       if r.purpose in ("earn", "scout")
                       and r.live_yield is not None
                       and self._cooldown_ok(r.market, r.side, now)]
            if unafford and resting:
                best_c = max(unafford, key=lambda c: c["yield"])
                worst = min(resting, key=lambda r: r.live_yield)
                decisive = (best_c["yield"] > worst.live_yield * self.cfg.rotate_factor
                            and best_c["ev"] > (worst.live_ev or 0)
                            + self.cfg.rotate_min_gain_day)
                if decisive:
                    r = self.desk.cancel(worst.id, worst.market)
                    if r.ok:
                        self._close_forecast(worst.id, "rotated_out", now)
                        self._log(event="rotate_out", market=worst.market,
                                  side=worst.side, price=worst.price,
                                  live_ev=worst.live_ev,
                                  for_market=best_c["market"],
                                  for_ev=best_c["ev"])
                        del self.orders[worst.id]
                        self._mark_action(worst.market, worst.side, now)
                        actions_left -= 1

        s.used = self.used_capital()
        s.headroom = round(self.cfg.ceiling_usd - s.used, 2)
        return self._summary(s)

    def _grade_pending_marks(self, books: BookCache, now: float) -> None:
        """About an hour after each fill, mark it against the touch mid —
        the observation that keeps fill_cost honest. A mark that can't be
        taken (no fresh book) waits; one stale beyond use is dropped."""
        for m in list(self.pending_marks):
            if now - m["ts"] < self.cfg.mark_after_s:
                continue
            book = books.fresh(m["market"], BOOK_MAX_AGE, now)
            if book is None or not (book.bids and book.asks):
                if now - m["ts"] > 6 * self.cfg.mark_after_s:
                    self.pending_marks.remove(m)
                continue
            mid = (book.bids[0][0] + book.asks[0][0]) / 2
            adverse = self.model.observe_fill_mark(m["market"], m["side"],
                                                   m["price"], mid)
            f = self.forecasts.get(m["id"])
            if f is not None:
                f["adverse"] = round(adverse, 4)
            self._log(event="fill_marked", market=m["market"],
                      adverse=round(adverse, 4))
            self.pending_marks.remove(m)

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
            "risk_families": self.risk_by_family(),
            "orders": [{"id": o.id, "market": o.market, "side": o.side,
                        "price": o.price, "qty": o.qty, "purpose": o.purpose,
                        "live_est": o.live_est, "live_ev": o.live_ev,
                        "live_yield": o.live_yield, "live_parts": o.live_parts,
                        "placed_ts": o.placed_ts}
                       for o in self.orders.values()],
            "inventory": self.inventory,
            "silent_cancels": self.silent_cancels,
            "exp1_open": len(self.exp1),
            "sweep": {"done": self.family_sweep_done, "cancelled": self.sweep_count},
            "cands": self.last_cands[:20],
            "rejected": self.last_cands_rejected,
            "actions": s.actions,
        }

    # ------------------------------------------------------------ persistence

    def to_dict(self) -> dict:
        return {
            "orders": {oid: vars(o) for oid, o in self.orders.items()},
            "inventory": self.inventory,
            "positions_seen": self.positions_seen,
            "ledger_v": 2,
            "silent_cancels": self.silent_cancels,
            "family_sweep_done": self.family_sweep_done,
            "sweep_count": self.sweep_count,
            "exp1": self.exp1, "log": self.log[-self.cfg.log_keep:],
            "last_action": self.last_action,
            "fillmodel": self.model.to_dict(),
            "forecasts": self.forecasts,
            "pending_marks": self.pending_marks,
        }

    def restore(self, d: dict) -> None:
        self.log = list(d.get("log") or [])   # first: migrations below log too
        for oid, v in (d.get("orders") or {}).items():
            self.orders[oid] = OwnOrder(**{k: x for k, x in v.items()
                                           if k in OwnOrder.__dataclass_fields__})
        if d.get("ledger_v") == 2:
            self.inventory = dict(d.get("inventory") or {})
        else:
            # Migration, once: state written before 2026-08-18 evening had
            # adopted the ACCOUNT's positions (1.0's stock) as engine
            # inventory, and the seller acted on it — four orders against
            # positions nobody gave 2.0, inside its ceiling. The ledger
            # starts clean; the orphan rule in cycle() pulls any resting
            # sell/close orders left over from that inventory.
            self.inventory = {}
            if d.get("inventory"):
                self._log(event="ledger_reset",
                          dropped=sorted(d["inventory"].keys()))
        self.positions_seen = dict(d.get("positions_seen") or {})
        self.silent_cancels = d.get("silent_cancels") or 0
        self.family_sweep_done = bool(d.get("family_sweep_done"))
        self.sweep_count = d.get("sweep_count") or 0
        self.exp1 = list(d.get("exp1") or [])
        self.last_action = dict(d.get("last_action") or {})
        if d.get("fillmodel"):
            self.model = FillModel.from_dict(d["fillmodel"])
        self.forecasts = dict(d.get("forecasts") or {})
        self.pending_marks = list(d.get("pending_marks") or [])
