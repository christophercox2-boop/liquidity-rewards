"""3.0 entry point.

    python -m v3.main          # run the loop
    python -m v3.main --once   # one cycle against the live exchange, print, exit

One process, one loop, a list of families. Politics is the first and the
priority; adding a family is one config function and one line in
FAMILIES — exactly how the owner expanded 2.0.

Placing needs BOTH the master switch and the family's own switch ON.
Everything starts OFF; until the owner arms a family it only discovers,
scores, and shows what it would do. Master OFF stops every family with
one tap.

Env: POLYMARKET_KEY_ID / POLYMARKET_SECRET_KEY (required),
GITHUB_TOKEN (state survives redeploys; optional),
NTFY_TOPIC / NTFY_SERVER (alerts; optional),
V3_STATE_PATH (default ./v3_state.json), V3_PORT (default 8092).
"""

from __future__ import annotations

import hashlib
import os
import sys
import threading
import time
from pathlib import Path

from . import football, politics
from .alerts import Alerts
from .api import ApiError, Client
from .books import BookCache
from .family import Family
from .floor import Floor
from .names import Names
from .orders import OrderDesk
from .books import ws_priority
from .estimator import Estimator
from .silver import SilverFairs
from .state import StateStore
from .switch import MasterSwitch
from .ws import Stream

POLL_S = 60.0
ERROR_BACKOFF_CAP_S = 600.0
FLATTEN_CANCELS_PER_CYCLE = 45


def flatten_active() -> bool:
    """Owner, 2026-08-20 evening: "cancel all of my open orders except for
    the ones that are exiting a position that I'm already in... I need to
    have no risk of spending any money." And once flat: "increase the
    budget to 100 and follow the same strategy that was already existing
    in V1 and V2 for politics markets, looking at the orders that were the
    most successful."

    While the marker file ships with the build (v3/FLATTEN), the monitor
    runs the flatten: phase one cancels every opening order on the account
    and keeps every exit; once a pass finds nothing left to cancel, phase
    two lets the armed families rebuild under their (now $100 politics)
    ceilings, history-guided, while the pass keeps guarding against any
    opening order 3.0 does not own. Removing the marker (a redeploy) ends
    the mode entirely. V3_FLATTEN=0/1 overrides for tests."""
    env = os.environ.get("V3_FLATTEN")
    if env is not None:
        return env == "1"
    return os.path.exists(os.path.join(os.path.dirname(__file__), "FLATTEN"))


def is_exit_order(order: dict, positions: dict) -> bool:
    """An order whose FILL reduces a position we already hold: an ask
    while long, or a bid while short. Book side from the INTENT (the
    exchange's side field is not trustworthy for shorts — 1.0's lesson).
    Same classification the owner approved in the dead-programs sweep."""
    from .intents import REST_SIDE
    side = REST_SIDE.get(str(order.get("intent") or ""))
    if side is None:
        return False
    net = (positions.get(order.get("market")) or (0.0, 0.0))[0]
    return (side == "SELL" and net > 0.005) or (side == "BUY" and net < -0.005)

# name -> (config fn, discover fn). Adding a family = adding a line.
# Politics first — it gets the capital, the book budget, and the page.
FAMILIES = {
    "politics": (politics.config, politics.discover),
    "cfb": (football.cfb, football.cfb_discover),
    "nfl": (football.nfl, football.nfl_discover),
}


def load_history() -> dict[str, float]:
    """Average $/day each market has ACTUALLY paid us, from the committed
    ground truth (data/rewards.csv on main). This is the "most successful
    orders" record the rebuild replicates. Empty on any failure — history
    guides, it never blocks."""
    tok = os.environ.get("GITHUB_TOKEN", "")
    if not tok:
        return {}, {}
    import csv
    import io
    from collections import defaultdict

    import requests
    repo = os.environ.get("GITHUB_REPOSITORY", "wfco223/Liquidity-rewards")
    try:
        r = requests.get(
            f"https://api.github.com/repos/{repo}/contents/data/rewards.csv",
            headers={"Authorization": f"Bearer {tok}",
                     "Accept": "application/vnd.github.raw+json"},
            timeout=30)
        if r.status_code >= 400:
            return {}, {}
        paid: dict = defaultdict(float)
        days: dict = defaultdict(set)
        day_totals: dict = defaultdict(float)
        for row in csv.DictReader(io.StringIO(r.text)):
            v = float(row.get("reward_usd") or 0)
            if v <= 0:
                continue
            mkt = row.get("market") or ""
            paid[mkt] += v
            days[mkt].add(row.get("date"))
            day_totals[row.get("date") or "?"] += v
        return ({mkt: round(paid[mkt] / max(len(days[mkt]), 1), 4)
                 for mkt in paid},
                {d: round(v, 2) for d, v in day_totals.items()})
    except Exception:  # noqa: BLE001
        return {}, {}


def build_hash() -> str:
    h = hashlib.sha256()
    for p in sorted(Path(__file__).parent.glob("*.py")):
        h.update(p.read_bytes())
    return h.hexdigest()[:8]


def touch_snapshot(fam: Family, now: float, cap: int = 400) -> dict:
    """Best bid/ask + side totals + age per market the family is in —
    published so the book is readable without the dashboard."""
    out = {}
    slugs = sorted(fam.active_markets() | set(fam.inventory))[:cap]
    for s in slugs:
        b = fam.cache.any_age(s)
        if b is None or now - b.fetched_at > 600:
            continue
        out[s] = [round(b.bids[0][0] * 100, 1) if b.bids else None,
                  round(b.asks[0][0] * 100, 1) if b.asks else None,
                  round(sum(q for _, q in b.bids)),
                  round(sum(q for _, q in b.asks)),
                  int(now - b.fetched_at)]
    return out


class Monitor:
    def __init__(self):
        self.client = Client()
        self.alerts = Alerts()
        self.names = Names()
        self.store = StateStore(os.environ.get("V3_STATE_PATH", "v3_state.json"))
        self.build = build_hash()
        self.boot_ts = time.time()
        self.errors: list[str] = []
        self.audit: list[dict] = []
        self.last_state: dict = {}
        self.boots: list[float] = []
        self.master = MasterSwitch(alert=self.alerts.notify,
                                   name="3.0 master switch", scope="all of 3.0")
        # The floor handshake (v3/floor.py): master ON asks 1.0 and 2.0 to
        # halt their automation; nothing here touches an order until both
        # have acknowledged. _floor_ok is refreshed every cycle and read by
        # every desk's switch closure.
        self.floor = Floor()
        self._floor_ok = False
        self.flatten = flatten_active()
        self.flatten_done = False          # phase two reached (persisted)
        self.flat_stats = {"cancelled": 0, "failed": 0}
        self.last_flat: dict | None = None
        self._history_at = 0.0
        self.silver = SilverFairs(client=self.client)
        self.samplers: dict[str, Estimator] = {}
        self.actuals_by_day: dict[str, float] = {}
        self.rewards_seen: dict[str, float] = {}
        self.rw_last: dict | None = None      # latest payout-check result
        self._rw_at = 0.0
        self._lock = threading.Lock()
        self.families: dict[str, Family] = {}
        self.switches: dict[str, MasterSwitch] = {}
        for key, (cfg_fn, discover) in FAMILIES.items():
            cfg = cfg_fn()
            sw = MasterSwitch(alert=self.alerts.notify,
                              name=f"{cfg.name} switch", scope=cfg.name)
            cache = BookCache()
            fam = Family(None, cache, discover, config=cfg,
                         alert=self.alerts.notify, names=self.names)
            desk = OrderDesk(
                client=self.client,
                whitelist=fam.knows,
                switch_on=lambda s=sw: (self.master.on and s.on
                                        and self._floor_ok),
                fresh_book=lambda slug, c=cache: c.fresh(slug, 120.0, time.time()),
                log=self._audit,
            )
            fam.desk = desk
            if key == "politics":
                fam.fairs = self.silver.model_fair
                cache.on_put = (lambda slug, book, f=fam:
                                f.fillmodel.observe_touch(
                                    slug,
                                    book.bids[0][0] if book.bids else None,
                                    book.asks[0][0] if book.asks else None,
                                    book.tick, book.fetched_at))
            self.families[key] = fam
            self.switches[key] = sw
            self.samplers[key] = Estimator()
        # The book stream: politics markets subscribe first (its cache is
        # the one the stream writes); a dead stream degrades to REST
        # polling through the cache's own age interlock.
        pol = self.families.get("politics")
        self.stream = (Stream(pol.cache, self._ws_slugs,
                              self.client.key_id, self.client.secret_key)
                       if pol is not None else None)
        self._restore()
        self.boots = [b for b in self.boots if time.time() - b < 86400]
        self.boots.append(time.time())
        # A deploy replaces the container and its floor files with it. If the
        # master came back ON, the request must be back on disk before 1.0's
        # first automation pass, not a poll later.
        self.floor.write_want(self.master.on or self.flatten)

    def _ws_slugs(self) -> list[str]:
        fam = self.families["politics"]
        held = sorted(fam.active_markets() | set(fam.inventory))
        top = [s for s, sb in sorted(fam.scoreboard.items(),
                                     key=lambda kv: -(kv[1].get("est") or 0.0))
               if sb.get("plans")][:120]
        return ws_priority(held, [], held + top)

    def _sampler_loop(self) -> None:
        """The independent clock (REBUILD.md's lesson): earnings are
        sampled every 20s by this thread, never by anything that just
        placed an order. Nothing here can touch an order."""
        while True:
            time.sleep(20.0)
            now = time.time()
            with self._lock:
                for key, fam in self.families.items():
                    try:
                        orders = [{"market": o.market, "side": o.side,
                                   "price": o.price, "size": o.qty}
                                  for o in fam.orders.values()]
                        self.samplers[key].sample(
                            now, orders, fam.cache, fam.terms,
                            side_pool=lambda s, p, f=fam: f._side_pool(s, p))
                    except Exception:  # noqa: BLE001 — measuring never breaks
                        pass

    def _audit(self, row: dict) -> None:
        self.audit.append(row)
        del self.audit[:-200]

    def _note(self, msg: str) -> None:
        self.errors.append(f"{time.strftime('%m-%d %H:%M:%S')} {msg}")
        del self.errors[:-40]
        print(f"v3: {msg}", flush=True)

    # -- persistence --------------------------------------------------------

    def _restore(self) -> None:
        saved = self.store.load_best()
        if not saved:
            self._note(f"booted build {self.build}; fresh state — "
                       "every switch is off")
            return
        if saved.get("master_switch"):
            self.master.restore(saved["master_switch"])
        if saved.get("names"):
            self.names.restore(saved["names"])
        for key, fam in self.families.items():
            if saved.get(f"fam_{key}"):
                fam.restore(saved[f"fam_{key}"])
            if saved.get(f"sw_{key}"):
                self.switches[key].restore(saved[f"sw_{key}"])
            if saved.get(f"est_{key}"):
                self.samplers[key] = Estimator.from_dict(saved[f"est_{key}"])
            if saved.get(f"evi_{key}"):
                fam.evidence.restore(saved[f"evi_{key}"])
        self.errors = list(saved.get("errors") or [])
        self.boots = list(saved.get("boots") or [])
        self.audit = list(saved.get("audit") or [])
        self.flatten_done = bool(saved.get("flatten_done"))
        self.flat_stats = dict(saved.get("flat_stats")
                               or {"cancelled": 0, "failed": 0})
        self.rewards_seen = dict(saved.get("rewards_seen") or {})
        self.actuals_by_day = dict(saved.get("actuals_by_day") or {})
        self.silver.changes = list(saved.get("silver_log") or [])
        self.rw_last = saved.get("rewards_last")
        age = time.time() - (saved.get("saved_at") or 0)
        armed = [k for k, sw in self.switches.items() if sw.on and self.master.on]
        self._note(f"booted build {self.build}; restored state {age:.0f}s old"
                   + (f"; ARMED: {', '.join(armed)}" if armed else ""))
        if armed and saved.get("build") != self.build:
            self.alerts.notify("3.0: new build with a switch ON",
                               f"build {self.build} booted; may place orders "
                               f"({', '.join(armed)})")

    def _grades(self) -> list[dict]:
        """Per-day estimate vs what the exchange actually paid. The
        estimate is 3.0's own sampler from the day it took over; the
        actuals are the whole account's postings (during the transition
        the older versions' books pay into the same number — labelled so
        on the page)."""
        est_by_day: dict[str, dict] = {}
        for key, est in self.samplers.items():
            for h in est.history:
                row = est_by_day.setdefault(h["day"], {"est": 0.0, "stale_s": 0.0})
                row["est"] += h.get("earned") or 0.0
                row["stale_s"] += h.get("stale_s") or 0.0
            if est.day:
                row = est_by_day.setdefault(est.day, {"est": 0.0, "stale_s": 0.0})
                row["est"] += est.earned
                row["stale_s"] += est.stale_s
        days = sorted(set(est_by_day) | set(self.actuals_by_day))[-14:]
        return [{"day": d,
                 "est": round(est_by_day.get(d, {}).get("est", 0.0), 2)
                 if d in est_by_day else None,
                 "actual": self.actuals_by_day.get(d),
                 "unmeasured_min": round(
                     est_by_day.get(d, {}).get("stale_s", 0.0) / 60.0, 1)}
                for d in days]

    def _state(self, now: float, summaries: dict) -> dict:
        st = {
            "saved_at": now, "build": self.build, "boot_ts": self.boot_ts,
            "boots": self.boots[-20:], "errors": self.errors,
            "audit": self.audit[-60:],
            "master_switch": self.master.to_dict(),
            "flatten_done": self.flatten_done,
            "flat_stats": self.flat_stats,
            "rewards_seen": self.rewards_seen,
            "actuals_by_day": self.actuals_by_day,
            "names": self.names.to_dict(),
            "summaries": summaries,
            "floor": self.floor.status(now),
            "ws": dict(self.stream.status) if self.stream else {},
            "silver_log": self.silver.changes[-120:],
            "rewards_last": self.rw_last,
            "silver": {
                "senate_races": len(self.silver.races),
                "gov_races": len(self.silver.gov_races),
                "tables_age_min": (round((now - self.silver.fetched_at) / 60)
                                   if self.silver.fetched_at else None),
                "official_source": self.silver.official_source,
                "official_age_h": (round(
                    self.silver.official_run_age_s(now) / 3600, 1)
                    if self.silver.official_meta else None),
                "meta": dict(self.silver.official_meta or {}),
            },
            "grades": self._grades(),
            "flatten": ({"active": self.flatten,
                         "done": self.flatten_done, **(self.last_flat or {})}
                        if self.flatten else {"active": False}),
            "alerts_log": self.alerts.log[-30:],
        }
        for key, fam in self.families.items():
            st[f"fam_{key}"] = fam.to_dict()
            st[f"est_{key}"] = self.samplers[key].to_dict()
            st[f"evi_{key}"] = fam.evidence.to_dict()
            st[f"sw_{key}"] = self.switches[key].to_dict()
            st[f"touches_{key}"] = touch_snapshot(fam, now)
        return st

    # -- owner controls -----------------------------------------------------

    def switch_tap(self, op: str, which: str = "master") -> dict:
        """A tap on /v3/switch. Persisted IMMEDIATELY, local and remote —
        a restart between a flip and the next save must not undo it."""
        sw = self.switches.get(which, self.master)
        s = sw.op(op)
        self.floor.write_want(self.master.on or self.flatten)
        st = dict(self.last_state) if self.last_state else {}
        st["master_switch"] = self.master.to_dict()
        for key in self.families:
            st[f"sw_{key}"] = self.switches[key].to_dict()
        st["saved_at"] = time.time()
        self.last_state = st
        self.store.save_local(st)
        self.store.save_remote(st)
        return s

    def order_op(self, op: str, order_id: str, price: float | None = None) -> dict:
        """Owner move/cancel on one of OUR orders, from the orders page.
        initiator='owner' bypasses the switches but no other rail."""
        for fam in self.families.values():
            rec = fam.orders.get(order_id)
            if rec is None:
                continue
            if op == "cancel":
                r = fam.desk.cancel(order_id, rec.market, initiator="owner")
                if r.ok:
                    del fam.orders[order_id]
                return {"ok": r.ok, "note": r.note}
            if op == "move" and price is not None:
                r = fam.desk.reprice(
                    {"id": rec.id, "market": rec.market, "side": rec.side,
                     "price": rec.price, "size": rec.qty, "intent": rec.intent},
                    price, initiator="owner")
                if r.ok:
                    del fam.orders[order_id]
                    from .family import FamilyOrder
                    fam.orders[r.order_id] = FamilyOrder(
                        id=r.order_id, market=rec.market, side=rec.side,
                        price=price, qty=rec.qty, intent=rec.intent,
                        placed_ts=time.time(), purpose=rec.purpose,
                        why="moved by the owner")
                return {"ok": r.ok, "note": r.note}
            return {"ok": False, "note": f"unknown op {op}"}
        return {"ok": False, "note": "not one of 3.0's orders"}

    def _kick_tracker(self) -> None:
        """Ask 1.0 (same container) to refresh rewards.csv on GitHub so
        the committed record is current when the push lands. The file
        keeps exactly one writer."""
        pw = os.environ.get("DASH_PASSWORD", "")
        if not pw:
            return
        try:
            import requests
            requests.post(
                f"http://127.0.0.1:{os.environ.get('PORT', '8080')}/track_now",
                json={}, headers={"X-Dash-Key": pw, "X-Reprice": "1"},
                timeout=5)
        except Exception:  # noqa: BLE001 — best effort
            pass

    def refresh_rewards(self) -> dict:
        """Owner's button: pull the exchange's posted payouts now, show
        what is new since the last look, and fold the day totals into the
        grades page. Reads only — rewards.csv on GitHub stays 1.0's file
        to write."""
        import datetime as _dt
        start = (_dt.datetime.now(_dt.timezone.utc)
                 - _dt.timedelta(days=6)).strftime("%Y-%m-%d")
        rows = self.client.earnings(start)
        first = not self.rewards_seen
        seen = self.rewards_seen
        fresh = []
        totals: dict[str, float] = {}
        for r in rows:
            key = f"{r['date']}|{r['market']}|{r['program_type']}"
            totals[r["date"]] = totals.get(r["date"], 0.0) + r["reward_usd"]
            if abs(seen.get(key, -1.0) - r["reward_usd"]) > 0.005:
                fresh.append(r)
            seen[key] = r["reward_usd"]
        # prune by the oldest date the API ACTUALLY returned, never by the
        # requested start — the API sends older rows than asked, and
        # pruning to the request made those rows read "new" on every
        # press (owner, 2026-08-21: "still posting the same rows")
        min_date = min((r["date"] for r in rows), default=start)
        self.rewards_seen = {k: v for k, v in seen.items()
                             if k[:10] >= min_date}
        for d, v in totals.items():
            self.actuals_by_day[d] = round(v, 2)
        # the baseline must survive a deploy between now and the next save
        # — local AND remote, immediately (a rebuild replaces the disk)
        if self.last_state:
            self.last_state["rewards_seen"] = self.rewards_seen
            self.last_state["actuals_by_day"] = self.actuals_by_day
            self.store.save_local(self.last_state)
            self.store.save_remote(self.last_state)
        days = {d: round(v, 2) for d, v in sorted(totals.items())}
        if first:
            # the FIRST check has nothing to compare against — every row
            # would read "new". Record the baseline and say so plainly.
            latest = max(totals) if totals else "?"
            self._note(f"rewards baseline: {len(rows)} rows through {latest}")
            return {"ok": True, "new_rows": [], "new_count": 0, "days": days,
                    "note": (f"First check: I recorded a baseline of "
                             f"{len(rows):,} rows through {latest}. From "
                             f"now on this button shows only what is new.")}
        if len(fresh) > max(400, 0.5 * len(rows)):
            # more than half the window "changed" means the baseline was
            # lost (a deploy race), not that thousands of rows posted at
            # once. Re-record it and say so, instead of spamming old rows.
            latest = max(totals) if totals else "?"
            self._note(f"rewards baseline re-recorded ({len(fresh)} rows)")
            return {"ok": True, "new_rows": [], "new_count": 0, "days": days,
                    "note": (f"The baseline was lost in a restart, so I "
                             f"re-recorded it ({len(rows):,} rows through "
                             f"{latest}). Press again later — only true "
                             f"news will show.")}
        fresh.sort(key=lambda r: (r["date"], r["reward_usd"]),
                   reverse=True)               # newest day, biggest first
        out_rows = [{"day": r["date"], "market": r["market"],
                     "name": self.names.label(r["market"]),
                     "usd": round(r["reward_usd"], 2),
                     "status": r["status"]} for r in fresh[:40]]
        self._note(f"rewards check: {len(fresh)} new/changed rows")
        return {"ok": True, "new_rows": out_rows, "new_count": len(fresh),
                "days": days}

    def public_state(self) -> dict:
        st = dict(self.last_state) if self.last_state else {"saved_at": 0}
        st["switch_view"] = {
            "master": self.master.state(),
            **{k: self.switches[k].state() for k in self.families}}
        st["floor"] = self.floor.status()
        return st

    # -- one poll -----------------------------------------------------------

    def _flatten_pass(self, orders: list[dict], positions: dict) -> dict:
        """Cancel opening orders, a batch per cycle for the rate limiter;
        exits are never touched. Runs only once 1.0/2.0 have stood down.
        In phase two (flatten_done) it turns guard: orders the 3.0
        families own are exempt — they are the rebuild."""
        desk = self.families["politics"].desk
        owned = {oid for fam in self.families.values() for oid in fam.orders}
        done = kept = remaining = 0
        for o in orders:
            if not (o.get("id") and o.get("market")):
                continue
            if is_exit_order(o, positions):
                kept += 1
                continue
            if self.flatten_done and o["id"] in owned:
                continue
            if done >= FLATTEN_CANCELS_PER_CYCLE:
                remaining += 1
                continue
            r = desk.cancel(o["id"], o["market"], initiator="flatten")
            if r.ok:
                done += 1
                self.flat_stats["cancelled"] += 1
                for fam in self.families.values():
                    fam.orders.pop(o["id"], None)
            else:
                self.flat_stats["failed"] += 1
            time.sleep(0.2)
        if not self.flatten_done and done == 0 and remaining == 0:
            self.flatten_done = True
            self.alerts.notify(
                "Flat — no spending risk left",
                f"kept {kept} exit orders, cancelled "
                f"{self.flat_stats['cancelled']} opening orders. The $100 "
                f"politics rebuild starts now, guided by what paid best.")
        return {"active": True, "phase": ("rebuild" if self.flatten_done
                                          else "cancelling"),
                "kept_exits": kept, "remaining": remaining,
                "cancelled_now": done,
                "cancelled_total": self.flat_stats["cancelled"],
                "failed_total": self.flat_stats["failed"]}

    def cycle(self, now: float | None = None) -> dict:
        now = now or time.time()
        with self._lock:
            return self._cycle_locked(now)

    def _cycle_locked(self, now: float) -> dict:
        self.flatten = flatten_active()
        self.floor.write_want(self.master.on or self.flatten)
        self._floor_ok = self.floor.acked(now)
        orders = self.client.open_orders()
        positions = self.client.positions_net()
        self.last_flat = None
        if self.flatten and self._floor_ok:
            self.last_flat = self._flatten_pass(orders, positions)
        try:
            self.silver.refresh(now)     # TTL-gated inside
        except Exception as e:  # noqa: BLE001 — the model never kills the loop
            self._note(f"silver: {e}")
        # the payout watcher (ported from 2.0, owner-approved): every five
        # minutes, diff the exchange's posted rewards and push the phone
        # the moment something new lands
        if now - self._rw_at > 300.0:
            self._rw_at = now
            try:
                res = self.refresh_rewards()
                if res.get("new_count"):
                    self.rw_last = res
                    days = sorted((res.get("days") or {}).items())[-2:]
                    line = ", ".join(f"{d[5:]} ${v:,.2f}" for d, v in days)
                    self.alerts.notify(
                        "Rewards posted",
                        f"{res['new_count']} new rows at the exchange; "
                        f"latest day totals: {line}")
                    self._kick_tracker()
            except Exception as e:  # noqa: BLE001 — watching never breaks
                self._note(f"rewards watch: {e}")
        if now - self._history_at > 6 * 3600.0:
            self._history_at = now
            hist, day_totals = load_history()
            if hist:
                for fam in self.families.values():
                    fam.history = hist
            if day_totals:
                self.actuals_by_day = day_totals
        summaries = {}
        for key, fam in self.families.items():
            if fam.cfg.proven_usd > 0:
                per_mkt = self.samplers[key].per_market
                fam.proven = {mkt for mkt, usd in per_mkt.items()
                              if usd >= fam.cfg.graduate_paid_usd}
            on = self.master.on and self.switches[key].on and self._floor_ok
            foreign = {oid for k2, f2 in self.families.items() if k2 != key
                       for oid in f2.orders}
            try:
                exits_only = self.flatten and not self.flatten_done
                summaries[key] = fam.cycle(now, orders, positions,
                                           self.client, on,
                                           foreign_ids=foreign,
                                           exits_only=exits_only)
                summaries[key]["name"] = fam.cfg.name
                est = self.samplers[key]
                summaries[key]["earned_today"] = round(est.earned, 2)
                summaries[key]["est_rate"] = round(est.rate, 2)
                summaries[key]["unmeasured_min"] = round(est.stale_s / 60.0, 1)
                if (self.master.on and self.switches[key].on
                        and not self._floor_ok):
                    summaries[key]["mode"] = "waiting for the floor"
            except ApiError as e:
                self._note(f"{key}: {e}")
                summaries[key] = {"name": fam.cfg.name, "error": str(e)[:120]}
        st = self._state(now, summaries)
        self.last_state = st
        self.store.save_local(st)
        self.store.maybe_save_remote(st)
        return st

    def run(self) -> int:
        from .web import WebServer
        web = WebServer(self)
        web.start()
        if self.stream is not None:
            self.stream.start()
        threading.Thread(target=self._sampler_loop, daemon=True,
                         name="sampler").start()
        self._note(f"serving on :{web.port}")
        backoff = 5.0
        while True:
            t0 = time.time()
            try:
                self.cycle()
                backoff = 5.0
            except Exception as e:  # noqa: BLE001 — the loop survives anything
                self._note(f"cycle failed: {type(e).__name__}: {e}")
                time.sleep(backoff)
                backoff = min(backoff * 2, ERROR_BACKOFF_CAP_S)
            time.sleep(max(POLL_S - (time.time() - t0), 5.0))


def main() -> int:
    m = Monitor()
    if "--once" in sys.argv:
        st = m.cycle()
        import json
        print(json.dumps({k: v for k, v in st.items()
                          if k in ("summaries", "errors", "build")}, indent=1)[:4000])
        return 0
    return m.run()


if __name__ == "__main__":
    sys.exit(main())
