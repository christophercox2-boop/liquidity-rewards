"""2.0 entry point — READ-ONLY phase.

    python -m v2.main          # run the loop
    python -m v2.main --once   # one full cycle, print the snapshot, exit

This process watches, scores, integrates and persists. It places
NOTHING: v2.orders is not imported here, so there is no code path from
this loop to an order-touching endpoint. The engine arrives behind the
master switch in a later phase, after the read-only estimate has been
compared against published payouts.

Env: POLYMARKET_KEY_ID / POLYMARKET_SECRET_KEY (required),
GITHUB_TOKEN (state survives redeploys; optional),
NTFY_TOPIC / NTFY_SERVER (alerts; optional),
V2_STATE_PATH (default ./v2_state.json).
"""

from __future__ import annotations

import hashlib
import os
import sys
import time
from pathlib import Path

from .alerts import Alerts
from .api import ApiError, Client
from .books import BookCache, ws_priority
from .estimator import Estimator
from .state import StateStore
from .terms import TermsStore
from .web import WebServer
from .ws import Stream

POLL_S = 30.0
TERMS_EVERY_S = 300.0
EVENTS_EVERY_S = 900.0
BOOK_BUDGET = 28          # REST book fetches per poll (rate-limit budget)
UNIVERSE_CAP = 500        # never score more markets than this, loudly
TERMS_HISTORY_KEEP = 2000
ERROR_BACKOFF_CAP_S = 600.0


def build_hash() -> str:
    """Fingerprint of the v2 code actually running, so 'did the deploy
    land?' is answerable from the published state."""
    h = hashlib.sha256()
    for p in sorted(Path(__file__).parent.glob("*.py")):
        h.update(p.read_bytes())
    return h.hexdigest()[:8]


def politics_event_sizes(client: Client) -> dict[str, int]:
    """slug -> open markets in its event, from the exchange's own politics
    tags (authoritative, unlike slug heuristics), widened by race-prefix
    grouping: candidate markets of one race share the pool even when
    modeled as separate single-market events."""
    sizes: dict[str, int] = {}
    for tag in ("politics", "elections"):
        for ev in client.events_by_tag(tag):
            open_slugs = [m["slug"] for m in ev.get("markets") or []
                          if m.get("slug") and not m.get("closed")]
            for s in open_slugs:
                sizes[s] = max(sizes.get(s, 0), len(open_slugs))
    race: dict[str, list[str]] = {}
    for s in sizes:
        race.setdefault(s.rsplit("-", 1)[0], []).append(s)
    for s in sizes:
        sizes[s] = max(sizes[s], len(race[s.rsplit("-", 1)[0]]))
    return sizes


def touch_snapshot(cache: BookCache, universe, now: float) -> dict:
    """Best bid/ask, side totals and age per market — published so anyone
    (owner, a future model) can read the book without the dashboard."""
    out = {}
    for s in universe:
        b = cache.any_age(s)
        if b is None or now - b.fetched_at > 600:
            continue
        out[s] = [
            round(b.bids[0][0] * 100, 1) if b.bids else None,
            round(b.asks[0][0] * 100, 1) if b.asks else None,
            round(sum(q for _, q in b.bids)),
            round(sum(q for _, q in b.asks)),
            int(now - b.fetched_at),
        ]
    return out


class Monitor:
    def __init__(self):
        self.client = Client()
        self.cache = BookCache()
        self.alerts = Alerts()
        self.terms_history: list[dict] = []
        self.terms = TermsStore(history_sink=self._sink_terms)
        self.estimator = Estimator()
        self.store = StateStore(os.environ.get("V2_STATE_PATH", "v2_state.json"))
        self.universe: list[str] = []
        self.held: list[str] = []
        self.event_sizes: dict[str, int] = {}
        self.last_terms = 0.0
        self.last_events = 0.0
        self.boot_ts = time.time()
        self.build = build_hash()
        self.errors: list[str] = []
        self.last_state: dict = {}
        self.stream = Stream(self.cache, self._ws_slugs,
                             self.client.key_id, self.client.secret_key)
        self._restore()

    def _sink_terms(self, row: dict) -> None:
        self.terms_history.append(row)
        del self.terms_history[:-TERMS_HISTORY_KEEP]

    def _ws_slugs(self) -> list[str]:
        return ws_priority(self.held, [], self.universe)

    def _restore(self) -> None:
        saved = self.store.load_best()
        if not saved:
            return
        if saved.get("terms"):
            self.terms = TermsStore.from_dict(saved["terms"],
                                              history_sink=self._sink_terms)
        if saved.get("estimator"):
            self.estimator = Estimator.from_dict(saved["estimator"])
        self.terms_history = list(saved.get("terms_history") or [])

    # -- one poll cycle -------------------------------------------------------

    def cycle(self, now: float | None = None) -> dict:
        now = now or time.time()
        orders = self.client.open_orders()
        self.universe = sorted({o["market"] for o in orders if o["market"]})
        if len(self.universe) > UNIVERSE_CAP:
            self._note(f"{len(self.universe)} markets — scoring the first {UNIVERSE_CAP}")
            self.universe = self.universe[:UNIVERSE_CAP]
        self.held = self.universe
        self.cache.prune(self.universe)

        if now - self.last_events > EVENTS_EVERY_S:
            self.last_events = now
            try:
                self.event_sizes = politics_event_sizes(self.client)
            except ApiError as e:
                self._note(f"event sizes: {e}")

        if now - self.last_terms > TERMS_EVERY_S and self.universe:
            self.last_terms = now
            try:
                raw = self.client.programs(self.universe)
                for c in self.terms.refresh(raw, self.event_sizes, now=now):
                    self.alerts.notify("Reward terms changed", str(c))
            except ApiError as e:
                self._note(f"terms: {e}")  # the store keeps serving, aged

        for slug in self.cache.pick_refresh(self.universe, self.held,
                                            now=now, budget=BOOK_BUDGET):
            try:
                self.cache.put(slug, self.client.book(slug, fetched_at=now))
            except ApiError as e:
                self._note(f"book {slug}: {e}")

        snap = self.estimator.sample(now, orders, self.cache, self.terms)

        state = {
            "saved_at": now, "boot_ts": self.boot_ts, "build": self.build,
            "mode": "read-only",
            "estimator": self.estimator.to_dict(),
            "terms": self.terms.to_dict(),
            "terms_history": self.terms_history[-200:],
            "touch": touch_snapshot(self.cache, self.universe, now),
            "ws": dict(self.stream.status),
            "alert_log": self.alerts.log[-50:],
            "errors": self.errors[-20:],
            "orders_n": len(orders), "markets_n": len(self.universe),
        }
        self.last_state = state
        self.store.save_local(state)
        self.store.maybe_save_remote(state)
        return snap

    def _note(self, msg: str) -> None:
        self.errors.append(f"{time.strftime('%H:%M:%S')} {msg}")
        del self.errors[:-50]

    # -- the loop ----------------------------------------------------------------

    def run(self) -> None:
        self.stream.start()
        try:
            WebServer(get_state=lambda: self.last_state).start_background()
        except OSError as e:  # port taken: measuring still works, the page doesn't
            self._note(f"web server: {e}")
        streak = 0
        while True:
            try:
                snap = self.cycle()
                streak = 0
                print(f"[{snap['day']}] rate ${snap['rate']:.2f}/day "
                      f"earned ${snap['earned']:.2f} "
                      f"({snap['samples']} samples, stale {snap['stale_s']:.0f}s)",
                      flush=True)
            except Exception as e:  # noqa: BLE001 — the loop must survive anything
                streak += 1
                self._note(f"cycle failed: {type(e).__name__}: {e}")
                # ~10 minutes of failure: tell the phone; then roughly hourly
                # (at the backoff cap cycles are 10 minutes apart), because
                # a changing error message would otherwise push every cycle
                if streak == 20 or (streak > 20 and streak % 6 == 0):
                    self.alerts.notify("v2 monitor failing",
                                       self.errors[-1] if self.errors else str(e))
                print(f"cycle error ({streak}): {e}", file=sys.stderr, flush=True)
            time.sleep(min(POLL_S * (2 ** min(streak, 5)), ERROR_BACKOFF_CAP_S)
                       if streak else POLL_S)


def main() -> int:
    if not (os.environ.get("POLYMARKET_KEY_ID") and os.environ.get("POLYMARKET_SECRET_KEY")):
        print("POLYMARKET_KEY_ID / POLYMARKET_SECRET_KEY not set", file=sys.stderr)
        return 2
    m = Monitor()
    if "--once" in sys.argv:
        snap = m.cycle()
        import json as _json
        print(_json.dumps(snap, indent=2))
        return 0
    m.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
