"""The book feed: one age-stamped cache, two writers, rationed reads.

Ported from 1.0's best subsystem (REBUILD.md: worth studying before
replacing). The design:

* One cache, every entry stamped with fetch time. Nothing in the system
  acts on a book without checking its age — consumers pick their own
  tolerance and fail closed.
* Writer 1 is the WebSocket stream (capped at 200 markets by the
  exchange; markets we hold orders in subscribe first). Every frame goes
  through the same normalizer as REST so the two produce identical books.
* Writer 2 is the REST rotation, budgeted per poll to respect the rate
  limiter. The interlock that makes the fallback automatic: books
  younger than WS_FRESH_S don't need REST — while the stream is healthy
  it keeps its markets under that, so REST fetches almost nothing; when
  the stream dies, ages cross the line and polling resumes by itself,
  with no state change anywhere.
* Refresh priority is staleness x churn: a book that changed on recent
  refreshes ages ~4x faster than one that sat still, so the fixed budget
  concentrates where scores actually move.
"""

from __future__ import annotations

import time

from .scoring import Book

WS_FRESH_S = 15.0        # younger than this = the stream is covering it
DEFAULT_BUDGET = 28      # REST fetches per rotation pass (rate-limit budget)
PRIORITY_RESERVE = 6     # rotation slots the priority set can never starve


class BookCache:
    def __init__(self):
        self.depth_seen: dict[str, int] = {}   # slug -> levels last seen
        self.last_writer: dict[str, str] = {}  # slug -> "ws" | "rest"
        # write counters per writer since last read-and-reset — the
        # hourly stream-health line reports them (owner, 2026-08-26)
        self.writes: dict[str, int] = {"ws": 0, "rest": 0}
        self.depth_hist: dict[int, int] = {}   # levels -> how often
        self._books: dict[str, Book] = {}
        # optional observer: called as on_put(slug, book) after every
        # write, from EITHER writer (REST rotation or the stream thread).
        # The fill model learns its hazards from exactly this feed.
        self.on_put = None
        # EWMA of "top 3 levels changed since last refresh", 0..1
        self._volatility: dict[str, float] = {}

    # -- reads -------------------------------------------------------------

    def fresh(self, slug: str, max_age: float, now: float | None = None) -> Book | None:
        """The book, or None if it is older than the caller tolerates.
        Every consumer must come through here — no raw dict access."""
        b = self._books.get(slug)
        if b is None:
            return None
        if (now or time.time()) - b.fetched_at > max_age:
            return None
        return b

    def any_age(self, slug: str) -> Book | None:
        """Last known book regardless of age — display only, never action."""
        return self._books.get(slug)

    def age(self, slug: str, now: float | None = None) -> float:
        b = self._books.get(slug)
        return (now or time.time()) - b.fetched_at if b else float("inf")

    def coverage(self, slugs, max_age: float, now: float | None = None) -> float:
        """Fraction of `slugs` with a fresh-enough book — the estimator's
        accrual quorum."""
        slugs = list(slugs)
        if not slugs:
            return 1.0
        now = now or time.time()
        ok = sum(1 for s in slugs if self.fresh(s, max_age, now) is not None)
        return ok / len(slugs)

    # -- writes ------------------------------------------------------------

    def put(self, slug: str, book: Book, writer: str = "rest") -> None:
        """Store a freshly normalized book (either writer). Learns how
        lively the book is from whether its top 3 levels moved, and how
        DEEP the book we were handed actually is.

        Depth is recorded because we could not previously say how much
        of a book we were even seeing: 370 stored snapshots capped at
        4-5 levels a side. It is not the cause of the share
        overestimate — measured 2026-08-24, a ladder seen 3 deep scores
        37.5% against 36.8% seen 20 deep — but a number we cannot state
        is a number we cannot rule in or out, and this one cost a day
        of theorising."""
        n = max(len(book.bids), len(book.asks))
        self.depth_seen[slug] = n
        self.writes[writer] = self.writes.get(writer, 0) + 1
        self.last_writer[slug] = writer   # who wrote this book — the
                                          # stream or a REST fetch; the
                                          # approved feed check compares
                                          # stream-written books against
                                          # fresh REST for the same slug
        self.depth_hist[min(n, 50)] = self.depth_hist.get(min(n, 50), 0) + 1
        old = self._books.get(slug)
        if old is not None:
            changed = (old.bids[:3] != book.bids[:3] or old.asks[:3] != book.asks[:3])
            v = self._volatility.get(slug, 0.5)
            self._volatility[slug] = round(0.7 * v + (0.3 if changed else 0.0), 4)
        self._books[slug] = book
        if self.on_put is not None:
            try:
                self.on_put(slug, book)
            except Exception:  # noqa: BLE001 — an observer never breaks a write
                pass

    def volatility_of(self, slug: str) -> float | None:
        """The book's churn EWMA (0 quiet .. 1 busy), or None until two
        fetches have produced a reading. No reading means NOT quiet —
        joining the touch needs evidence, not absence of it."""
        return self._volatility.get(slug)

    def prune(self, universe) -> None:
        """Drop markets no longer tracked so the cache can't grow stale
        entries forever."""
        gone = set(self._books) - set(universe)
        for s in gone:
            self._books.pop(s, None)
            self._volatility.pop(s, None)

    # -- rotation ------------------------------------------------------------

    def _staleness(self, slug: str, now: float) -> float:
        return self.age(slug, now) * (1.0 + 3.0 * self._volatility.get(slug, 0.5))

    def pick_refresh(self, universe, priority, now: float | None = None,
                     budget: int = DEFAULT_BUDGET) -> list[str]:
        """Which books the REST rotation should fetch this pass. Books the
        stream keeps under WS_FRESH_S need nothing; the saved budget flows
        to whatever the stream doesn't cover. Priority markets (defended /
        quoted) take up to budget - PRIORITY_RESERVE slots, oldest first;
        the general rotation keeps the reserve so discovery never starves."""
        now = now or time.time()
        needs = [s for s in universe if self.age(s, now) > WS_FRESH_S]
        prio = sorted((s for s in needs if s in set(priority)),
                      key=lambda s: self.age(s, now), reverse=True)
        rest = sorted((s for s in needs if s not in set(priority)),
                      key=lambda s: self._staleness(s, now), reverse=True)
        take_prio = prio[:max(0, budget - PRIORITY_RESERVE)]
        return take_prio + rest[:budget - len(take_prio)]


def ws_priority(slugs_with_orders, defended, universe, cap: int = 200) -> list[str]:
    """The subscription list for the stream: held and defended markets
    first (they must stay fresh), the rest of the universe filling the
    exchange's 200-slug cap."""
    first = [s for s in universe if s in set(slugs_with_orders) | set(defended)]
    rest = [s for s in universe if s not in set(first)]
    return (first + rest)[:cap]
