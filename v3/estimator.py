"""ONE earned-today number.

1.0 kept three — the plain integration, the high-frequency one, and a
sparse fallback — and they disagreed because nobody decided which was
authoritative. Worse, the plain sampler was WOKEN by our own order
activity, so it sampled at exactly the moments our book looked best and
read high.

2.0's estimator:

* samples on its own clock. There is deliberately NO kick API on this
  class — nothing that places, moves or cancels orders can make it
  sample. Whoever schedules it calls sample() on a fixed or Poisson
  interval, full stop.
* integrates rate x elapsed into "earned today", with the elapsed time
  capped so a dead spell can't be billed at the last known rate.
* refuses to accrue when too few books are fresh — the stale seconds are
  banked and published instead, so a dead feed shows up as "X minutes
  unmeasured", never as invented earnings.
* reads terms from the ONE TermsStore. There is no second cache to go
  stale against.
* rolls the day at midnight Eastern (the exchange's reward day) and
  keeps each closed day so estimate-vs-paid is checkable per day.

NO correction factor. The number is the arithmetic on real inputs —
wrong output means a wrong input (owner's standing instruction).
"""

from __future__ import annotations

import datetime as dt

from .books import BookCache
from .scoring import Book, score_resting
from .terms import TermsStore

try:
    from zoneinfo import ZoneInfo
    ET = ZoneInfo("America/New_York")
except Exception:  # no tz database: fixed EDT offset, same fallback as 1.0
    ET = dt.timezone(dt.timedelta(hours=-4), "ET")

BOOK_MAX_AGE = 180.0   # a book older than this doesn't get scored
MAX_GAP_S = 300.0      # longest interval one sample may bill for
MIN_FRESH = 0.5        # book-freshness quorum below which nothing accrues
HISTORY_DAYS = 30


def et_day(now: float) -> str:
    return dt.datetime.fromtimestamp(now, tz=dt.timezone.utc).astimezone(ET).strftime("%Y-%m-%d")


def top_up_book(book: Book, own_orders) -> Book:
    """Guarantee our own resting size is present at its price level before
    scoring. Books and order snapshots are seconds apart; scoring a book
    that predates our order yields nonsense ("you 3 ticks from best"
    while we ARE the best). Ported from 1.0's self-consistency pass."""
    want: dict[tuple[str, float], float] = {}
    for o in own_orders:
        want[(o["side"], o["price"])] = want.get((o["side"], o["price"]), 0.0) + o["size"]
    if not want:
        return book
    sides = {"BUY": list(book.bids), "SELL": list(book.asks)}
    changed = False
    for (side, px), sz in want.items():
        levels = sides[side]
        have = sum(q for lp, q in levels if abs(lp - px) < 1e-9)
        if have < sz - 1e-9:
            levels[:] = [(lp, q) for lp, q in levels if abs(lp - px) >= 1e-9]
            levels.append((px, sz))
            changed = True
    if not changed:
        return book
    return Book(
        bids=tuple(sorted(sides["BUY"], key=lambda x: -x[0])),
        asks=tuple(sorted(sides["SELL"], key=lambda x: x[0])),
        tick=book.tick, fetched_at=book.fetched_at,
    )


class Estimator:
    def __init__(self):
        self.day: str | None = None
        self.earned = 0.0
        self.per_market: dict[str, float] = {}
        self.rate = 0.0                      # $/day from the latest sample
        self.market_rates: dict[str, float] = {}
        self.samples = 0
        self.covered_s = 0.0                 # seconds actually billed today
        self.stale_s = 0.0                   # seconds refused for staleness today
        self.last_ts: float | None = None
        self.history: list[dict] = []        # closed days

    # -- the one entry point -------------------------------------------------

    def sample(self, now: float, orders: list[dict], books: BookCache,
               terms: TermsStore, side_pool=None) -> dict:
        """Score the resting book and advance the integral. `orders` is the
        normalized open-order list; `side_pool(slug, prog)` supplies the
        divisor-confirmed daily side pool (None = hold the estimate, the
        3.0 integrity rule — a market with an unconfirmed divisor accrues
        nothing rather than a guess)."""
        day = et_day(now)
        if self.day is None:
            self.day = day
        elif day != self.day:
            self._close_day()
            self.day = day

        # elapsed time since the previous sample, billed at the PREVIOUS
        # rate (the rate that was actually in force over that interval)
        dt_s = 0.0
        if self.last_ts is not None:
            dt_s = min(max(now - self.last_ts, 0.0), MAX_GAP_S)
        self.last_ts = now

        by_market: dict[str, list[dict]] = {}
        for o in orders:
            if o.get("market"):
                by_market.setdefault(o["market"], []).append(o)

        considered = [m for m in by_market if terms.get(m) is not None]
        fresh = [m for m in considered
                 if books.fresh(m, BOOK_MAX_AGE, now) is not None]
        fresh_set = set(fresh)
        # Per-market accrual (owner, 2026-08-21 evening: "CFB still says
        # it's only earned 5 cents today" — the old all-or-nothing
        # freshness quorum threw away whole minutes when most of a big
        # family was unwatched, refusing to count even the markets it
        # COULD see). Each market with a fresh book bills its own rate;
        # only the unwatched ones bank stale time. covered/stale are
        # coverage-weighted seconds, so the phone still shows how much
        # of the family the meter actually sees.
        frac = (len(fresh) / len(considered)) if considered else 1.0
        if dt_s:
            for m, r in self.market_rates.items():
                if m in fresh_set:
                    self.earned += r * dt_s / 86400.0
                    self.per_market[m] = (self.per_market.get(m, 0.0)
                                          + r * dt_s / 86400.0)
            self.covered_s += dt_s * frac
            self.stale_s += dt_s * (1.0 - frac)

        rates: dict[str, float] = {}
        for m in fresh:
            prog = terms.get(m)
            if not prog.is_live():
                continue
            book = top_up_book(books.fresh(m, BOOK_MAX_AGE, now), by_market[m])
            pool = side_pool(m, prog) if side_pool is not None else None
            if pool is None:
                continue          # divisor unconfirmed: no number, not a guess
            for o in by_market[m]:
                s = score_resting(o["side"], o["price"], o["size"], book,
                                  df=prog.df, target=prog.target,
                                  daily_side_pool=pool)
                if s.est_day:
                    rates[m] = rates.get(m, 0.0) + s.est_day
        self.market_rates = rates
        self.rate = sum(rates.values())
        self.samples += 1
        return self.snapshot(now)

    # -- bookkeeping ------------------------------------------------------------

    def _close_day(self) -> None:
        self.history.append({
            "day": self.day, "earned": round(self.earned, 4),
            "samples": self.samples, "covered_s": round(self.covered_s, 1),
            "stale_s": round(self.stale_s, 1),
            "per_market": {m: round(v, 4) for m, v in sorted(
                self.per_market.items(), key=lambda kv: -kv[1])[:50]},
        })
        del self.history[:-HISTORY_DAYS]
        self.earned = 0.0
        self.per_market = {}
        self.samples = 0
        self.covered_s = 0.0
        self.stale_s = 0.0

    def snapshot(self, now: float) -> dict:
        return {
            "day": self.day, "earned": round(self.earned, 4),
            "rate": round(self.rate, 4),
            "market_rates": {m: round(v, 4) for m, v in self.market_rates.items()},
            "per_market": {m: round(v, 4) for m, v in self.per_market.items()},
            "samples": self.samples, "covered_s": round(self.covered_s, 1),
            "stale_s": round(self.stale_s, 1), "ts": now,
        }

    # -- persistence --------------------------------------------------------------

    def to_dict(self) -> dict:
        d = self.snapshot(self.last_ts or 0.0)
        d["history"] = self.history
        d["last_ts"] = self.last_ts
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Estimator":
        e = cls()
        e.day = d.get("day")
        e.earned = d.get("earned") or 0.0
        e.per_market = dict(d.get("per_market") or {})
        e.rate = d.get("rate") or 0.0
        e.market_rates = dict(d.get("market_rates") or {})
        e.samples = d.get("samples") or 0
        e.covered_s = d.get("covered_s") or 0.0
        e.stale_s = d.get("stale_s") or 0.0
        e.last_ts = d.get("last_ts")
        e.history = list(d.get("history") or [])
        return e
