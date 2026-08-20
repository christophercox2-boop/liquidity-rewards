"""2.0 entry point.

    python -m v2.main          # run the loop
    python -m v2.main --once   # one full cycle, print the snapshot, exit

Watches, scores, integrates, persists — and runs the probe->earn->sell
engine on its whitelisted markets (the two seats families) BEHIND THE
MASTER SWITCH. The switch starts off and every flip is two taps on
/v2/switch; with it off the engine only reconciles reality and the
process is exactly the read-only monitor it was in the first phase.
Every order-touching call goes through the OrderDesk rails; nothing
else in this process imports them.

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
from .engine import Engine, EngineConfig
from .estimator import Estimator
from .orders import OrderDesk
from .rewardswatch import RewardsWatch
from .silver import SilverFairs
from .survey import Survey
from .state import StateStore
from .switch import MasterSwitch
from .terms import TermsStore
from .web import WebServer
from .ws import Stream

POLL_S = 45.0
TERMS_EVERY_S = 300.0
EVENTS_EVERY_S = 900.0
BOOK_BUDGET = 10          # REST book fetches per poll (rate-limit budget)
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
        self.family_slugs: list[str] = []      # the whitelisted families' markets
        self.event_sizes: dict[str, int] = {}
        self.last_terms = 0.0
        self.last_events = 0.0
        self.boot_ts = time.time()
        self.build = build_hash()
        self.errors: list[str] = []
        self.audit: list[dict] = []            # every OrderDesk decision
        self.last_state: dict = {}
        self.switch = MasterSwitch(alert=self.alerts.notify)
        self.silver = SilverFairs(client=self.client)
        self.rewards_watch = RewardsWatch()
        # read-only scout for families we do NOT trade
        self.survey = Survey()
        cfg = EngineConfig()
        self.desk = OrderDesk(
            client=self.client,
            whitelist=lambda s: s.startswith(cfg.whitelist_prefixes),
            switch_on=lambda: self.switch.on,
            fresh_book=lambda s: self.cache.fresh(s, 120.0, time.time()),
            log=self._audit,
        )
        self.engine = Engine(self.desk, cfg, alert=self.alerts.notify)
        self.stream = Stream(self.cache, self._ws_slugs,
                             self.client.key_id, self.client.secret_key)
        self.boots: list[float] = []
        self._restore()
        self.boots = [b for b in self.boots if time.time() - b < 86400]
        self.boots.append(time.time())

    def _kick_tracker(self) -> bool:
        """Ask 1.0 (same container) to refresh rewards.csv on GitHub NOW —
        the exact run the dashboard button starts, so the file keeps one
        writer. Auth is the shared dashboard password plus the CSRF header
        1.0's POST endpoints require."""
        pw = os.environ.get("DASH_PASSWORD", "")
        if not pw:
            return False
        import requests
        r = requests.post(
            f"http://127.0.0.1:{os.environ.get('PORT', '8080')}/track_now",
            json={}, headers={"X-Dash-Key": pw, "X-Reprice": "1"}, timeout=5)
        return r.status_code == 200

    def _sink_terms(self, row: dict) -> None:
        self.terms_history.append(row)
        del self.terms_history[:-TERMS_HISTORY_KEEP]

    def _audit(self, row: dict) -> None:
        self.audit.append(row)
        del self.audit[:-200]

    def _ws_slugs(self) -> list[str]:
        return ws_priority(self.held, self.family_slugs, self.universe)

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
        if saved.get("switch"):
            self.switch.restore(saved["switch"])
        if saved.get("engine_saved"):
            self.engine.restore(saved["engine_saved"])
        if saved.get("rewards_watch"):
            self.rewards_watch = RewardsWatch.from_dict(saved["rewards_watch"])
        if saved.get("survey"):
            self.survey = Survey.from_dict(saved["survey"])
        # errors survive restarts, and every boot leaves a visible marker —
        # a container restart-loop must show on the page, not vanish
        self.errors = list(saved.get("errors") or [])
        self.boots = list(saved.get("boots") or [])
        age = time.time() - (saved.get("saved_at") or 0)
        self._note(f"booted build {self.build}; restored state {age:.0f}s old"
                   f"{'; SWITCH IS ON' if self.switch.on else ''}")
        if self.switch.on and saved.get("build") != self.build:
            # the owner chose persistence over off-after-deploy; the guard
            # that replaces it is this one push
            self.alerts.notify("New build with switch ON",
                               f"build {self.build} booted; 2.0 may place orders")

    def switch_tap(self, op: str) -> dict:
        """An owner tap on /v2/switch. The flip is persisted IMMEDIATELY —
        local and remote, no throttle — because a container restart between
        a flip and the next cycle's save once quietly turned the switch
        back off (2026-08-18, the owner's first ON lasted seconds)."""
        s = self.switch.op(op)
        st = dict(self.last_state) if self.last_state else {}
        st["switch"] = s
        st["saved_at"] = time.time()
        self.last_state = st
        self.store.save_local(st)
        self.store.save_remote(st)
        return s

    def public_state(self) -> dict:
        """What the page sees: the last cycle's state with the LIVE switch
        overlaid, so the display can never show a stale flip."""
        st = dict(self.last_state) if self.last_state else {"saved_at": 0}
        st["switch"] = self.switch.state()
        return st

    # -- one poll cycle -------------------------------------------------------

    def cycle(self, now: float | None = None) -> dict:
        now = now or time.time()
        orders = self.client.open_orders()
        # 2.0's world is its whitelisted families plus wherever it actually
        # has orders or stock — NOT the whole account's 150+ markets. It
        # measured everything for a day (useful for the first comparison);
        # doing so forever meant two systems fetching and scoring the whole
        # board on one small box, which is what the restart loop fed on.
        # 1.0 keeps publishing its own whole-board estimate for comparison.
        engine_mkts = {o.market for o in self.engine.orders.values()}
        self.universe = sorted(set(self.family_slugs) | engine_mkts
                               | set(self.engine.inventory))
        if len(self.universe) > UNIVERSE_CAP:
            self._note(f"{len(self.universe)} markets — scoring the first {UNIVERSE_CAP}")
            self.universe = self.universe[:UNIVERSE_CAP]
        self.held = sorted(engine_mkts)
        self.cache.prune(self.universe)
        in_scope = set(self.universe)
        scoped_orders = [o for o in orders if o["market"] in in_scope]

        if now - self.last_events > EVENTS_EVERY_S:
            self.last_events = now
            try:
                self.event_sizes = politics_event_sizes(self.client)
                self.family_slugs = sorted(
                    s for s in self.event_sizes
                    if s.startswith(self.engine.cfg.whitelist_prefixes))
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

        snap = self.estimator.sample(now, scoped_orders, self.cache, self.terms)

        # every touch the feed delivered teaches the fill model (dt=0
        # samples are ignored inside, so unchanged books cost nothing)
        for slug in self.universe:
            b = self.cache.any_age(slug)
            if b is not None:
                self.engine.model.observe_touch(
                    slug,
                    b.bids[0][0] if b.bids else None,
                    b.asks[0][0] if b.asks else None,
                    b.tick, b.fetched_at)

        # the engine: silver fairs on a slow TTL, positions for fill
        # detection, then one decision cycle behind the switch. NOTHING in
        # this block may prevent the state save below — a cycle that dies
        # before saving is how the first switch flip got lost.
        engine_summary = {"mode": "skipped"}
        try:
            self.silver.refresh(now)
        except Exception as e:  # noqa: BLE001 — engine runs on cached fairs
            self._note(f"silver: {type(e).__name__}: {e}")
        try:
            # positions are only needed when the engine can act or holds
            # anything; while idle, poll them gently — the container is
            # shared with 1.0 and every request costs its CPU and rate limit
            engaged = (self.switch.on or self.engine.orders or self.engine.inventory)
            self._pos_tick = getattr(self, "_pos_tick", 0) + 1
            if engaged or self._pos_tick % 4 == 1:
                positions = self.client.positions_net()
            else:
                positions = None
            if positions is not None:
                engine_summary = self.engine.cycle(
                    now, orders, positions, self.cache, self.terms,
                    self.silver, self.switch.on)
                for a in engine_summary.get("actions") or []:
                    print(f"engine: {a}", flush=True)
            else:
                engine_summary = {"mode": "idle"}
        except Exception as e:  # noqa: BLE001 — never lose the save below
            self._note(f"engine: {type(e).__name__}: {e}")
            engine_summary = {"mode": f"error: {type(e).__name__}"}

        # the rewards watcher: cheap (one windowed earnings fetch every 5
        # minutes), fenced like the engine, and pushes the phone the moment
        # Polymarket posts anything new
        try:
            self.rewards_watch.check(self.client, self.alerts.notify, now,
                                     kick=self._kick_tracker)
        except Exception as e:  # noqa: BLE001 — never lose the save below
            self._note(f"rewards watch: {type(e).__name__}: {e}")

        # the survey: read-only, gentle, and last in line — it may never
        # cost the engine a cycle or the box its rate limit
        try:
            self.survey.refresh_catalogue(self.client, now)
            self.survey.scan_terms(self.client, now)   # cheap: which pay
            self.survey.measure(self.client, now)      # costly: what they pay
        except Exception as e:  # noqa: BLE001 — a scout must never break the loop
            self._note(f"survey: {type(e).__name__}: {e}")

        recent_boots = [b for b in self.boots if now - b < 3600]
        if len(recent_boots) >= 5:
            # title includes "monitor failing" so it skips the alert floor
            self.alerts.notify("v2 monitor failing: restart loop",
                               f"{len(recent_boots)} boots in the last hour — "
                               f"likely memory or health checks on the shared "
                               f"box; DigitalOcean runtime logs show exit codes")

        state = {
            "saved_at": now, "boot_ts": self.boot_ts, "build": self.build,
            "boots": self.boots[-50:], "restart_loop": len(recent_boots),
            "mode": f"engine {engine_summary.get('mode')}",
            "estimator": self.estimator.to_dict(),
            "terms": self.terms.to_dict(),
            "terms_history": self.terms_history[-200:],
            "touch": touch_snapshot(self.cache, self.universe, now),
            "ws": dict(self.stream.status),
            "alert_log": self.alerts.log[-50:],
            "errors": self.errors[-20:],
            "orders_n": len(orders), "markets_n": len(self.universe),
            "switch": self.switch.state(),
            "engine": engine_summary,
            "engine_saved": self.engine.to_dict(),
            "audit": self.audit[-50:],
            "fillmodel": self.engine.model.summary(),
            "forecasts": list(self.engine.forecasts.values())[-100:],
            "fairs": {s: [round(r[0], 4), round(r[1], 4)]
                      for s in self.family_slugs
                      if (r := self.silver.fair_range(s)) is not None},
            "silver_races": {a: round(r["rep"], 4)
                             for a, r in self.silver.races.items()},
            "ladders": {
                s: {"bids": [[p, q] for p, q in b.bids[:6]],
                    "asks": [[p, q] for p, q in b.asks[:6]],
                    "tick": b.tick, "age": int(now - b.fetched_at)}
                for s in self.family_slugs
                if (b := self.cache.any_age(s)) is not None
                and now - b.fetched_at < 900
            },
            "silver": {"age_s": (round(self.silver.age(now)) if self.silver.fetched_at
                                 else None),
                       "source": self.silver.source, "note": self.silver.note,
                       "gop_control": (gc := self.silver.gop_control()) and round(gc, 3),
                       "official": {
                           "run": (self.silver.official_meta or {}).get("run", ""),
                           "date": (self.silver.official_meta or {}).get("date", ""),
                           "sims": (self.silver.official_meta or {}).get("sims", 0),
                           "source": self.silver.official_source,
                           "note": self.silver.official_note,
                           "run_age_d": (round(a / 86400.0, 1)
                                         if (a := self.silver.official_run_age_s(now))
                                         != float("inf") else None),
                       } if self.silver.official else None},
            "silver_flavors": {s: fv for s in self.family_slugs
                               if (fv := self.silver.flavors_fair(s)) is not None},
            "control": {c: cv for c in ("senate", "house")
                        if (cv := self.silver.control(c)) is not None},
            "rewards_watch": self.rewards_watch.to_dict(),
            "survey": self.survey.to_dict(),
            "survey_view": {"status": self.survey.status(now),
                            "families": self.survey.by_family(),
                            "rows": self.survey.ranked(40)},
            "rewards_status": self.rewards_watch.status(now),
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
            WebServer(get_state=self.public_state,
                      switch_op=self.switch_tap).start_background()
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
