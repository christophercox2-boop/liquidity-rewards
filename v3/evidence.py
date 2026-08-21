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

    def fill(self, slug: str, side: str, px: float, ts: float | None = None) -> None:
        """One of OUR orders traded. side is the BOOK side it rested on."""
        self._note(slug, "fill_buy" if side == "BUY" else "fill_sell", px, ts)

    def rested(self, slug: str, side: str, px: float, ts: float | None = None) -> None:
        """One of our orders sat through a full maintenance read untouched."""
        self._note(slug, "rest_buy" if side == "BUY" else "rest_sell", px, ts)

    # -- the read ------------------------------------------------------------

    def heat(self, slug: str, now: float | None = None) -> int:
        """Fills through our orders in the last day — how hot the ground is."""
        now = now if now is not None else self._clock()
        return sum(1 for ts, kind, _ in self.events.get(slug, ())
                   if kind.startswith("fill") and now - ts < HEAT_WINDOW_S)

    def band(self, slug: str, prior_fair: float | None = None,
             touches: tuple[float | None, float | None] = (None, None),
             now: float | None = None) -> dict | None:
        """Posterior {lo, med, hi (cents), n, fills} or None without
        evidence AND prior. lo/hi are the 10-90% credible interval."""
        now = now if now is not None else self._clock()
        rows = self.events.get(slug, ())
        terms = []
        for ts, kind, pxc in rows:
            age_w = 0.5 ** ((now - ts) / HALF_LIFE_S)
            if kind == "fill_buy":     # seller accepted px -> fair <= px
                terms.append(("le", pxc, 1.0 * age_w))
            elif kind == "fill_sell":  # buyer paid px -> fair >= px
                terms.append(("ge", pxc, 1.0 * age_w))
            elif kind == "rest_buy":   # nobody sold to us -> weakly fair >= px
                terms.append(("ge", pxc, REST_WEIGHT * age_w))
            elif kind == "rest_sell":
                terms.append(("le", pxc, REST_WEIGHT * age_w))
        bb, ba = touches
        if bb is not None:
            terms.append(("ge", bb * 100.0, 0.5))   # real money bids there
        if ba is not None:
            terms.append(("le", ba * 100.0, 0.5))
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
        fills = sum(1 for _, k, _2 in rows if k.startswith("fill"))
        return {"lo": lo, "med": med, "hi": hi,
                "n": len(rows), "fills": fills}

    # -- persistence ---------------------------------------------------------

    def to_dict(self) -> dict:
        return {"events": {s: rows[-EVENT_KEEP:]
                           for s, rows in self.events.items() if rows}}

    def restore(self, d: dict) -> None:
        for s, rows in (d.get("events") or {}).items():
            self.events[s] = [list(r) for r in rows][-EVENT_KEEP:]
