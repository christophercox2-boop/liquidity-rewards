"""The evidence model — 1.0's prober rebuilt to run on free evidence.

1.0 paid for evidence: it rested small scouts and read what happened to
them. 3.0's book IS the scout fleet — every resting order is already an
experiment, and the market's own prints are free. The judgment engine is
1.0's, kept because it was tuned on real money (live/monitor.py
_bayes_fair): a grid posterior over 1..99c, every event a soft one-sided
observation through a logistic likelihood about two ticks wide:

    our bid FILLED at p     -> a seller accepted p  -> fair likely <= p
    our ask FILLED at p     -> a buyer paid p       -> fair likely >= p
    our order RESTED quietly-> weak opposite evidence (0.35x — absence
                               of a taker in thin flow proves little)
    de-baited real touches  -> gentle anchors (someone risks size there)

Improvements over 1.0:

* Where the Silver model prices the market, its fair is the PRIOR (a
  logistic bump, ~4 ticks wide) instead of a flat grid — polling and
  order-flow evidence pull the same posterior instead of living on
  separate pages.
* The band feeds the planner directly: bids must stay under the band's
  high edge, asks above its low edge (the wrong-side rule, now driven
  by evidence AND model together), and a market whose fills-per-day
  heat is high loses its join-the-touch privilege — scouts getting
  eaten was exactly 1.0's signal to step back.
* No budget, no journal page, no scout rotation to babysit. Events in,
  bands out, capped memory.
"""

from __future__ import annotations

import math
import time

EVENT_KEEP = 60            # events remembered per market
HALF_LIFE_S = 36 * 3600.0  # evidence half-life
LOGISTIC_SCALE = 2.0       # ticks (cents) — 1.0's likelihood width
PRIOR_SCALE = 4.0          # Silver prior width, cents
REST_WEIGHT = 0.35         # 1.0's quiet-resting discount
SNATCH_WEIGHT = 2.5        # a faster-than-its-context fill shouts
REST_LOG_CAP = 6.0         # log2(1+hours) caps here (~2.6 days saturates)
ANCHOR_BASE = 0.5          # a touch level's floor weight
ANCHOR_CAP = 2.5           # ...and its ceiling, however big the wall
HEAT_WINDOW_S = 24 * 3600.0


def _logistic(x: float) -> float:
    if x < -30:
        return 0.0
    if x > 30:
        return 1.0
    return 1.0 / (1.0 + math.exp(-x))


class Evidence:
    """Per-market event log and posterior bands."""

    def __init__(self, clock=None):
        self._clock = clock or time.time
        self.events: dict[str, list[list]] = {}   # slug -> [ts, kind, px_cents]

    # -- observations --------------------------------------------------------

    def _note(self, slug: str, kind: str, px: float, ts: float | None) -> None:
        ts = ts if ts is not None else self._clock()
        rows = self.events.setdefault(slug, [])
        rows.append([round(ts, 1), kind, round(px * 100.0, 2)])
        del rows[:-EVENT_KEEP]

    def fill(self, slug: str, side: str, px: float, ts: float | None = None,
             weight: float = 1.0) -> None:
        """One of OUR orders traded. side is the BOOK side it rested on.

        `weight` carries the SPEED verdict (owner, 2026-08-25: "Getting
        filled quickly tells us that we're over the fair price. Getting
        filled after a while tells us we're in the range."). A fill
        faster than the 25th percentile of its context — spread width x
        how far past the touch we rested, quantiles measured from our
        own 368 exchange-stamped fills — arrives at SNATCH_WEIGHT, so a
        burn pushes the band away from the burn price hard instead of
        counting like ordinary flow. The direction was always right
        here (a bid filling says fair <= px); the WEIGHT is what was
        blind to speed."""
        ts = ts if ts is not None else self._clock()
        rows = self.events.setdefault(slug, [])
        rows.append([round(ts, 1),
                     "fill_buy" if side == "BUY" else "fill_sell",
                     round(px * 100.0, 2), round(float(weight), 2)])
        del rows[:-EVENT_KEEP]

    def rested(self, slug: str, side: str, px: float, ts: float | None = None) -> None:
        """Back-compat shim: a single legacy quiet observation."""
        self._note(slug, "rest_buy" if side == "BUY" else "rest_sell", px, ts)

    def rest_mark(self, slug: str, order_id: str, side: str, px: float,
                  started: float, now: float | None = None) -> None:
        """ONE term per resting order, however long it lives (owner,
        2026-08-21: the information keeps coming, but a week says more
        than an hour, not 168x more). The term's weight grows with the
        LOG of the order's quiet time: an hour ~1 unit, a day ~4.6, a
        week ~7.4 — capped so no single order dominates. Re-marking the
        same order UPDATES its one record instead of stacking votes."""
        now = now if now is not None else self._clock()
        rows = self.events.setdefault(slug, [])
        key = f"restrec:{order_id}"
        for r in rows:
            if len(r) >= 5 and r[3] == key:
                r[0] = round(now, 1)          # freshness for decay
                r[4] = round(started, 1)
                r[1] = "restrec_buy" if side == "BUY" else "restrec_sell"
                r[2] = round(px * 100.0, 2)
                return
        rows.append([round(now, 1),
                     "restrec_buy" if side == "BUY" else "restrec_sell",
                     round(px * 100.0, 2), key, round(started, 1)])
        del rows[:-EVENT_KEEP]

    def order_gone(self, slug: str, order_id: str,
                   now: float | None = None) -> None:
        """The order ended: freeze its quiet record; it decays from here."""
        now = now if now is not None else self._clock()
        key = f"restrec:{order_id}"
        for r in self.events.get(slug, ()):
            if len(r) >= 5 and r[3] == key:
                r[0] = round(now, 1)
                r[3] = f"restdone:{order_id}"

    # -- the read ------------------------------------------------------------

    def _iter(self, slug: str):
        for r in self.events.get(slug, ()):
            yield r[0], r[1], r[2]

    def heat(self, slug: str, now: float | None = None) -> float:
        """Age-weighted fills through our orders in the last day — how hot
        the ground is, as a CONTINUOUS quantity: a fill an hour ago counts
        nearly 1.0, one from last night counts a fraction, and the number
        decays back toward zero on its own. No cliffs."""
        now = now if now is not None else self._clock()
        return round(sum(0.5 ** ((now - ts) / HALF_LIFE_S)
                         for ts, kind, _ in self._iter(slug)
                         if kind.startswith("fill")
                         and now - ts < HEAT_WINDOW_S), 3)

    def fills_effective(self, slug: str, now: float | None = None) -> float:
        """Age-weighted count of ALL our fills here — the evidence mass
        confidence grows from and decays with."""
        now = now if now is not None else self._clock()
        return sum(0.5 ** ((now - ts) / HALF_LIFE_S)
                   for ts, kind, _ in self._iter(slug)
                   if kind.startswith("fill"))

    def confidence(self, slug: str, band: dict | None = None,
                   now: float | None = None) -> float:
        """How much the evidence has EARNED the right to move prices off
        the model, 0..1 and continuous — 1.0's graduated idea ("one real
        trade is enough when the band is very tight, two when it's merely
        tight") as a curve instead of thresholds. Real trades build it,
        time decays it, a tight band amplifies it, a sloppy band damps
        it. Nothing about it is a rule; it is a weight."""
        f = self.fills_effective(slug, now)
        base = f / (f + 1.2)
        if band and band.get("hi") is not None and band.get("lo") is not None:
            width = band["hi"] - band["lo"]
            base *= min(max(1.3 - width / 30.0, 0.3), 1.0)
        return round(min(base, 1.0), 4)

    @staticmethod
    def _rest_weight(quiet_s: float) -> float:
        import math as _m
        hours = max(quiet_s, 0.0) / 3600.0
        return REST_WEIGHT * min(_m.log2(1.0 + hours), REST_LOG_CAP)

    @staticmethod
    def _anchor_weight(size: float | None) -> float:
        """A standing level's testimony grows with the money behind it:
        five shares is the floor, a million-share wall caps at 2.5 —
        the owner's 2026-08-21 point that the market's own resting
        depth is evidence just like ours, weighted by its size."""
        import math as _m
        if size is None or size < 5.0:
            return ANCHOR_BASE
        return min(ANCHOR_BASE + 0.5 * _m.log10(size / 5.0), ANCHOR_CAP)

    def band(self, slug: str, prior_fair: float | None = None,
             touches: tuple[float | None, float | None] = (None, None),
             touch_sizes: tuple[float | None, float | None] = (None, None),
             now: float | None = None) -> dict | None:
        """Posterior {lo, med, hi (cents), n, fills} or None without
        evidence AND prior. lo/hi are the 10-90% credible interval."""
        now = now if now is not None else self._clock()
        rows = self.events.get(slug, ())
        terms = []
        for r in rows:
            ts, kind, pxc = r[0], r[1], r[2]
            age_w = 0.5 ** ((now - ts) / HALF_LIFE_S)
            if kind in ("fill_buy", "fill_sell"):
                w = 1.0                    # legacy rows carry no weight
                if len(r) >= 4 and isinstance(r[3], (int, float)):
                    w = float(r[3])
                # fill_buy: seller accepted px -> fair <= px; fill_sell
                # the mirror — the speed weight scales how loudly
                terms.append(("le" if kind == "fill_buy" else "ge",
                              pxc, w * age_w))
            elif kind in ("rest_buy", "rest_sell"):   # legacy single marks
                terms.append(("ge" if kind == "rest_buy" else "le",
                              pxc, REST_WEIGHT * age_w))
            elif kind.startswith("restrec"):
                quiet = ts - (r[4] if len(r) >= 5 else ts)
                w = self._rest_weight(quiet) * age_w
                terms.append(("ge" if kind.endswith("buy") else "le", pxc, w))
        bb, ba = touches
        sb, sa = touch_sizes
        if bb is not None:
            terms.append(("ge", bb * 100.0, self._anchor_weight(sb)))
        if ba is not None:
            terms.append(("le", ba * 100.0, self._anchor_weight(sa)))
        if not terms and prior_fair is None:
            return None
        post = []
        for c in range(1, 100):
            lp = 0.0
            if prior_fair is not None:
                d = (c - prior_fair * 100.0) / PRIOR_SCALE
                lp += -abs(d) - math.log(1 + math.exp(-2 * abs(d)))  # logistic bump
            for op, pxc, w in terms:
                d = (pxc - c) / LOGISTIC_SCALE
                p = _logistic(d) if op == "le" else 1.0 - _logistic(d)
                lp += w * math.log(max(p, 1e-9))
            post.append(lp)
        m = max(post)
        ps = [math.exp(x - m) for x in post]
        tot = sum(ps)
        cum, lo, med, hi = 0.0, None, None, None
        for i, p in enumerate(ps):
            cum += p / tot
            c = i + 1
            if lo is None and cum >= 0.10:
                lo = c
            if med is None and cum >= 0.50:
                med = c
            if hi is None and cum >= 0.90:
                hi = c
        fills = sum(1 for r in rows if r[1].startswith("fill"))
        return {"lo": lo, "med": med, "hi": hi,
                "n": len(rows), "fills": fills}

    # -- persistence ---------------------------------------------------------

    def to_dict(self) -> dict:
        return {"events": {s: rows[-EVENT_KEEP:]
                           for s, rows in self.events.items() if rows}}

    def restore(self, d: dict) -> None:
        for s, rows in (d.get("events") or {}).items():
            # legacy per-half-hour rest votes are dropped: the new one-
            # record-per-order form rebuilds within hours and cannot
            # stack (owner, 2026-08-21). Fills and rest-records survive.
            self.events[s] = [list(r) for r in rows
                              if not str(r[1]).startswith("rest_")
                              ][-EVENT_KEEP:]
