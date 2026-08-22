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

from . import basketball, football, politics
from .alerts import Alerts
from .api import ApiError, Client, GATEWAY
from .books import BookCache
from .family import Family
from .floor import Floor
from .names import Names
from .orders import OrderDesk
from .estimator import Estimator
from .silver import SilverFairs
from .state import StateStore
from .switch import MasterSwitch
from .ws import Stream

try:
    from zoneinfo import ZoneInfo
    ET_STATUS = ZoneInfo("America/New_York")
except Exception:  # noqa: BLE001
    import datetime as _dtz
    ET_STATUS = _dtz.timezone(_dtz.timedelta(hours=-4), "ET")

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
    "nba": (basketball.nba, basketball.nba_discover),
}


def load_history() -> dict[str, float]:
    """Average $/day each market has ACTUALLY paid us, from the committed
    ground truth (data/rewards.csv on main). This is the "most successful
    orders" record the rebuild replicates. Empty on any failure — history
    guides, it never blocks."""
    tok = os.environ.get("GITHUB_TOKEN", "")
    if not tok:
        return {}, {}, {}
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
            return {}, {}, {}
        paid: dict = defaultdict(float)
        days: dict = defaultdict(set)
        day_totals: dict = defaultdict(float)
        r_paid: dict = defaultdict(float)
        r_days: dict = defaultdict(set)
        import datetime as _dt
        cutoff = (_dt.date.today()
                  - _dt.timedelta(days=7)).isoformat()
        for row in csv.DictReader(io.StringIO(r.text)):
            v = float(row.get("reward_usd") or 0)
            if v <= 0:
                continue
            mkt = row.get("market") or ""
            paid[mkt] += v
            days[mkt].add(row.get("date"))
            day_totals[row.get("date") or "?"] += v
            if (row.get("date") or "") >= cutoff:
                r_paid[mkt] += v
                r_days[mkt].add(row.get("date"))
        recent = {mkt: (round(r_paid[mkt] / max(len(r_days[mkt]), 1), 4),
                        len(r_days[mkt])) for mkt in r_paid}
        return ({mkt: round(paid[mkt] / max(len(days[mkt]), 1), 4)
                 for mkt in paid},
                {d: round(v, 2) for d, v in day_totals.items()},
                recent)
    except Exception:  # noqa: BLE001
        return {}, {}, {}


FILLS_CSV_HEADER = ("ts,family,market,side,qty,px,purpose,est_day,"
                    "rested_h,fair,band_lo,band_hi,conf,touch_bid,"
                    "touch_ask,conc,pos_after,why\n")


def fills_csv_append(existing: str | None, rows: list) -> tuple[str, int]:
    """Append-only fills archive (owner, 2026-08-22: 'bound it much
    higher — write to GitHub'). `rows` are (ts, family, journal-row)
    tuples; returns (new file text, rows added). Fills from the same
    cycle share a timestamp, so dedup is by the whole line, not ts."""
    def s(x):
        if x is None:
            return ""
        return f"{x:g}" if isinstance(x, (int, float)) else str(x)
    text = existing if existing else FILLS_CSV_HEADER
    tail = set(text.rstrip().split("\n")[-400:])
    last = 0.0
    body = text.rstrip().rsplit("\n", 1)[-1]
    try:
        last = float(body.split(",", 1)[0])
    except Exception:
        last = 0.0
    added = 0
    for ts, fam, r in sorted(rows, key=lambda x: x[0]):
        if ts < last - 0.05:
            continue
        band = r.get("band") or [None, None]
        why = str(r.get("why") or "").replace(",", ";").replace("\n", " ")[:80]
        line = ",".join([
            f"{ts:.1f}", fam, s(r.get("market")), s(r.get("side")),
            s(r.get("qty")), s(r.get("px")), s(r.get("purpose")),
            s(r.get("est_day")), s(r.get("rested_h")), s(r.get("fair")),
            s(band[0]), s(band[1]), s(r.get("conf")),
            s(r.get("touch_bid")), s(r.get("touch_ask")),
            s(r.get("conc")), s(r.get("pos_after")), why])
        if line in tail:
            continue
        text += line + "\n"
        tail.add(line)
        added += 1
    return text, added


def card_is_open(card: dict) -> bool:
    """A lot is open only while the exchange still shows a position —
    a lot the pairing thinks is open on a FLAT market was closed by a
    correction or an untracked fill (the Florida card, 2026-08-22) and
    counts as closed."""
    if card.get("stray_close"):
        return False
    oq = (card.get("open_qty") if card.get("open_qty") is not None
          else card.get("qty", 0.0))
    if oq <= 0.005:
        return False
    if (card.get("pos_now") is not None
            and abs(card["pos_now"]) < 0.005):
        return False
    return True


def card_net(card: dict) -> float:
    """The card's bottom line, same math the page shows: realized plus
    rewards earned resting, plus (for open lots) the conservative mark
    and what the resting exit has earned."""
    earned = 0.0
    if card.get("est_day") and card.get("rested_h") is not None:
        earned = card["est_day"] * card["rested_h"] / 24.0
    is_open = card_is_open(card)
    net = (card.get("realized") or 0.0) + earned
    if is_open:
        oq = (card.get("open_qty") if card.get("open_qty") is not None
              else card.get("qty", 0.0))
        if card.get("side") == "BUY" and card.get("now_bid") is not None:
            net += (card["now_bid"] - card["px"]) * oq
        if card.get("side") == "SELL" and card.get("now_ask") is not None:
            net += (card["px"] - card["now_ask"]) * oq
        net += card.get("exit_earned") or 0.0
    return net


def card_visible(card: dict, now: float) -> bool:
    """Owner's retention (2026-08-22): closed cards show for 3 days
    after their last close; open cards show until they turn profitable
    (then the journal keeps tracking them silently)."""
    if card_is_open(card):
        return card_net(card) <= 0.005
    last = card.get("last_ts", card.get("ts", 0.0))
    return now - last <= 3 * 86400.0


def pair_fills(fills: list) -> list:
    """Match closes to entries, oldest lot first, per market: a buy pairs
    with the sells that unload it, a short sale with the buys that cover
    it (owner, 2026-08-21: "each should have a matching buy and sell or
    sell short and buy back"). Returns one card per entry lot carrying
    its closes and realized money, plus stray closes of stock the journal
    never saw bought."""
    out: list[dict] = []
    by_mkt: dict[str, list] = {}
    for r in sorted(fills, key=lambda x: x.get("ts", 0.0)):
        by_mkt.setdefault(r.get("market", "?"), []).append(r)
    for evs in by_mkt.values():
        longs: list[dict] = []
        shorts: list[dict] = []
        for r in evs:
            qty = float(r.get("qty") or 0.0)
            opp = shorts if r["side"] == "BUY" else longs
            while qty > 0.005 and opp:
                lot = opp[0]
                take = min(qty, lot["open_qty"])
                pl = ((lot["px"] - r["px"]) if r["side"] == "BUY"
                      else (r["px"] - lot["px"])) * take
                lot["closes"].append({
                    "ts": r["ts"], "px": r["px"], "qty": round(take, 2),
                    "pl": round(pl, 4)})
                lot["realized"] = round(lot["realized"] + pl, 4)
                lot["open_qty"] = round(lot["open_qty"] - take, 2)
                lot["last_ts"] = r["ts"]
                if lot["open_qty"] <= 0.005:
                    opp.pop(0)
                qty = round(qty - take, 2)
            if qty > 0.005:
                lot = dict(r)
                lot["open_qty"] = qty
                lot["closes"] = []
                lot["realized"] = 0.0
                lot["last_ts"] = r["ts"]
                if r.get("purpose") == "sell":
                    # an exit with no purchase to match: it closed stock
                    # bought before the journal — not a new position
                    lot["stray_close"] = True
                    lot["open_qty"] = 0.0
                else:
                    (longs if r["side"] == "BUY" else shorts).append(lot)
                out.append(lot)
    return out


def build_hash() -> str:
    h = hashlib.sha256()
    for p in sorted(Path(__file__).parent.glob("*.py")):
        h.update(p.read_bytes())
    return h.hexdigest()[:8]


class CacheRouter:
    """The stream writes here; frames route to the family that owns the
    market (politics is the fallback). One socket, every family fed."""

    def __init__(self, families: dict):
        self.families = families

    def put(self, slug: str, book) -> None:
        for key in ("cfb", "nfl", "nba"):
            fam = self.families.get(key)
            if fam is not None and slug in fam.universe:
                fam.cache.put(slug, book)
                return
        pol = self.families.get("politics")
        if pol is not None:
            pol.cache.put(slug, book)


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
        # the boot readout: what the first cycle is doing right now, so a
        # restart shows a progress bar instead of a scary red "stale"
        self.boot_stage = {"stage": "starting", "pct": 2, "ts": time.time()}
        self._first_cycle_done = False
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
            # every family's fill model learns from its own book feed
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
        self.stream = (Stream(CacheRouter(self.families), self._ws_slugs,
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
        """The owner's slot order (2026-08-21): every politics market
        he is in seats first — that is the priority — then football
        markets holding orders, then idle candidates rotate through the
        leftover slots. Promising candidates (a measured rate or a
        planned estimate) hold stable seats or rotate often; cold ones
        get a thin rotation lane."""
        from .ws import SUB_CAP
        out: list[str] = []
        seen: set[str] = set()

        def take(slugs, room=None):
            for s in slugs:
                if room is not None and len(out) >= room:
                    break
                if s not in seen:
                    seen.add(s)
                    out.append(s)

        for key in ("politics", "cfb", "nfl", "nba"):
            fam = self.families.get(key)
            if fam is not None:
                take(sorted(fam.active_markets() | set(fam.inventory)),
                     room=SUB_CAP)
        cands: list[tuple[float, str]] = []
        for key in ("politics", "cfb", "nfl", "nba"):
            fam = self.families.get(key)
            if fam is None:
                continue
            est = self.samplers.get(key)
            rates = est.market_rates if est is not None else {}
            for s, sb in fam.scoreboard.items():
                if s in seen:
                    continue
                promise = max(rates.get(s) or 0.0,
                              (sb.get("est") or 0.0) if sb.get("plans")
                              else 0.0)
                cands.append((promise, s))
        cands.sort(key=lambda t: (-t[0], t[1]))
        warm = [s for p, s in cands if p > 0.0]
        cold = [s for p, s in cands if p <= 0.0]
        room = max(SUB_CAP - len(out), 0)
        take(warm[:room // 2], room=SUB_CAP)     # stable seats for the best
        warm_rest = warm[room // 2:]

        def rotate(pool, n, window):
            if not pool or n <= 0:
                return []
            n = min(n, len(pool))
            off = (window * n) % len(pool)
            return (pool + pool)[off:off + n]

        window = int(time.time() // 900)         # a fresh mix every 15 min
        room = max(SUB_CAP - len(out), 0)
        take(rotate(warm_rest, (room * 3) // 4, window), room=SUB_CAP)
        room = max(SUB_CAP - len(out), 0)
        take(rotate(cold, room, window), room=SUB_CAP)
        return out[:SUB_CAP]

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
            "lite_study": self._lite_study(),

            "silver_log": self.silver.changes[-120:],
            "rewards_last": self.rw_last,
            "silver": {
                "priced": sum(1 for s in self.families["politics"].universe
                              if self.families["politics"].enterable(s)
                              and self.silver.model_fair(s) is not None),
                "unpriced": sum(1 for s in self.families["politics"].universe
                                if self.families["politics"].enterable(s)
                                and self.silver.model_fair(s) is None),
                "senate_races": len(self.silver.races),
                "gov_races": len(self.silver.gov_races),
                "tables_age_min": (round((now - self.silver.fetched_at) / 60)
                                   if self.silver.fetched_at else None),
                "tables_changed_h": (round(
                    (now - self.silver.changed_at) / 3600, 1)
                    if getattr(self.silver, "changed_at", 0) else None),
                "gov_changed_h": (round(
                    (now - self.silver.gov_changed_at) / 3600, 1)
                    if getattr(self.silver, "gov_changed_at", 0) else None),
                "note": getattr(self.silver, "note", ""),
                "ak_gov": dict(self.silver.gov_races.get("ak") or {}),
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

    def owner_place(self, market: str, side: str, price: float,
                    qty: float) -> dict:
        """The owner's own hand: bypasses switches, keeps every other
        rail, and the automation never touches the result."""
        from .family import FamilyOrder
        for fam in self.families.values():
            if not fam.knows(market):
                continue
            net = 0.0
            try:
                net = (self.client.positions_net().get(market) or (0.0,))[0]
            except Exception:  # noqa: BLE001
                pass
            r = fam.desk.place_resting(market, side, price, qty,
                                       net_position=net, initiator="owner",
                                       verify=True)
            if r.ok and r.order_id:
                fam.orders[r.order_id] = FamilyOrder(
                    id=r.order_id, market=market, side=side, price=price,
                    qty=qty, intent=r.intent, placed_ts=time.time(),
                    purpose="manual", why="placed by the owner")
            return {"ok": r.ok, "note": r.note, "order_id": r.order_id}
        return {"ok": False,
                "note": "no family knows this market — check the slug"}

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

    # -- the repo files 1.0 used to write (ported; single-writer gated) --

    def _gh_file(self, path: str):
        """(text, sha) of a repo file on main, or (None, None)."""
        tok = os.environ.get("GITHUB_TOKEN", "")
        if not tok:
            return None, None
        import requests
        repo = os.environ.get("GITHUB_REPOSITORY", "wfco223/Liquidity-rewards")
        r = requests.get(
            f"https://api.github.com/repos/{repo}/contents/{path}",
            headers={"Authorization": f"Bearer {tok}",
                     "Accept": "application/vnd.github+json"}, timeout=30)
        if r.status_code >= 400:
            return None, None
        j = r.json()
        import base64
        return base64.b64decode(j.get("content") or "").decode(), j.get("sha")

    def _gh_put(self, path: str, text: str, sha, message: str) -> bool:
        tok = os.environ.get("GITHUB_TOKEN", "")
        if not tok:
            return False
        import base64
        import requests
        repo = os.environ.get("GITHUB_REPOSITORY", "wfco223/Liquidity-rewards")
        body = {"message": message,
                "content": base64.b64encode(text.encode()).decode()}
        if sha:
            body["sha"] = sha
        r = requests.put(
            f"https://api.github.com/repos/{repo}/contents/{path}",
            headers={"Authorization": f"Bearer {tok}",
                     "Accept": "application/vnd.github+json"},
            json=body, timeout=30)
        return r.status_code < 300

    def compose_rewards_csv(self, rows: list[dict], existing: str | None) -> str:
        """The exact 1.0 file shape, with history the API no longer serves
        preserved from the existing file."""
        header = "date,market,program_type,reward_usd,status"
        fetched_min = min((r["date"] for r in rows), default="9999")
        keep = []
        for line in (existing or "").splitlines():
            if not line or line.startswith("date,"):
                continue
            if line.split(",", 1)[0] < fetched_min:
                keep.append(line)
        fresh = [f"{r['date']},{r['market']},{r['program_type']},"
                 f"{r['reward_usd']:g},{r['status']}" for r in rows]
        return "\n".join([header] + keep + fresh) + "\n"

    def compose_status_md(self, now: float) -> str:
        import datetime as _dt2
        ts = _dt2.datetime.fromtimestamp(now, _dt2.timezone.utc)
        et = ts.astimezone(ET_STATUS)
        lines = [f"# Liquidity rewards — 3.0",
                 f"",
                 f"✅ Updated {et.strftime('%b %d, %I:%M %p ET')} — the app "
                 f"writes this file every hour.", ""]
        total_rate = 0.0
        total_today = 0.0
        for key, fam in self.families.items():
            est = self.samplers[key]
            s = (self.last_state.get("summaries") or {}).get(key) or {}
            total_today += est.earned
            rate = est.rate
            total_rate += rate
            lines.append(
                f"- **{fam.cfg.name}**: about ${rate:,.2f}/day resting "
                f"(${est.earned:,.2f} accrued today), "
                f"{len(fam.orders)} orders, "
                f"${fam.family_spent():,.2f} of "
                f"${fam.cfg.capital_usd:,.0f} at risk"
                + (f" — includes holdings worth "
                   f"${fam.holdings_value():,.2f} at liquidation"
                   if fam.cfg.holdings_in_ceiling else "") + ".")
        lines += ["",
                  f"**Whole book: ~${total_rate:,.2f}/day; "
                  f"${total_today:,.2f} accrued today.**", "",
                  "Every number is arithmetic on the exchange's own reward "
                  "terms — no fudge factors. The pages have the detail: "
                  "orders (with plain-English verdicts), the model's moves, "
                  "and grades (estimate vs. what actually paid).", ""]
        return "\n".join(lines)

    def publish_files(self, now: float) -> None:
        """Hourly, and only while 1.0 is retired (one writer per file)."""
        if os.environ.get("V1_ENABLED", "0") != "0":
            return
        if now - getattr(self, "_pub_at", 0.0) < 3600.0:
            return
        self._pub_at = now
        try:
            import datetime as _dt3
            start = (_dt3.datetime.now(_dt3.timezone.utc)
                     - _dt3.timedelta(days=40)).strftime("%Y-%m-%d")
            rows = self.client.earnings(start)
            existing, sha = self._gh_file("data/rewards.csv")
            text = self.compose_rewards_csv(rows, existing)
            if text != existing:
                self._gh_put("data/rewards.csv", text, sha,
                             "Update rewards.csv [skip ci]")
        except Exception as e:  # noqa: BLE001
            self._note(f"rewards.csv publish: {e}")
        try:
            frows = [(r.get("ts", 0.0), tag, r)
                     for tag, fam in self.families.items()
                     for r in fam.fills]
            if frows:
                existing, sha = self._gh_file("data/fills.csv")
                text, added = fills_csv_append(existing, frows)
                if added:
                    self._gh_put("data/fills.csv", text, sha,
                                 f"fills archive: +{added} rows [skip ci]")
        except Exception as e:  # noqa: BLE001
            self._note(f"fills.csv publish: {e}")
        try:
            for path, text in (("data/silver_gov_races.csv",
                                getattr(self.silver, "gov_raw", "")),
                               ("data/silver_senate_races.csv",
                                getattr(self.silver, "senate_raw", ""))):
                if not text:
                    continue
                existing, sha = self._gh_file(path)
                if existing is not None and existing != text:
                    self._gh_put(path, text, sha,
                                 "Silver model refresh [skip ci]")
            existing, sha = self._gh_file("STATUS.md")
            text = self.compose_status_md(now)
            if text != existing:
                self._gh_put("STATUS.md", text, sha,
                             "Update STATUS.md [skip ci]")
        except Exception as e:  # noqa: BLE001
            self._note(f"STATUS.md publish: {e}")

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
        # The exchange splits one market-day into SEVERAL rows (a SKIPPED
        # row and a PAID row of different amounts), and each call returns
        # a different set of ancient strays outside the asked window. So:
        # AGGREGATE per market-day before diffing, remember everything
        # ever seen (never date-pruned, size-capped instead), and only
        # SHOW news from the last few days — older strays are absorbed
        # silently (owner, 2026-08-21: "still off").
        agg: dict[str, dict] = {}
        for r in rows:
            key = f"{r['date']}|{r['market']}"
            a = agg.setdefault(key, {"date": r["date"], "market": r["market"],
                                     "usd": 0.0, "paid": 0.0, "status": set()})
            a["usd"] += r["reward_usd"]
            a["status"].add(r["status"])
            if r["status"] != "SKIPPED":
                a["paid"] += r["reward_usd"]
        seen = self.rewards_seen
        fresh = []
        totals: dict[str, float] = {}
        for key, a in agg.items():
            totals[a["date"]] = totals.get(a["date"], 0.0) + a["paid"]
            if abs(seen.get(key, -1.0) - round(a["usd"], 2)) > 0.005:
                fresh.append(a)
            seen[key] = round(a["usd"], 2)
        if len(seen) > 12000:
            for k in sorted(seen)[:len(seen) - 12000]:
                del seen[k]
        self.rewards_seen = seen
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
        if len(fresh) > max(400, 0.5 * len(agg)):
            # more than half the window "changed" means the memory was
            # lost or its format moved — re-record it, never spam old rows
            latest = max(totals) if totals else "?"
            self._note(f"rewards baseline re-recorded ({len(fresh)} rows)")
            return {"ok": True, "new_rows": [], "new_count": 0, "days": days,
                    "note": (f"I re-recorded the baseline "
                             f"({len(agg):,} market-days through {latest}). "
                             f"From here only true news shows.")}
        show_from = (_dt.datetime.now(_dt.timezone.utc)
                     - _dt.timedelta(days=4)).strftime("%Y-%m-%d")
        shown = [a for a in fresh if a["date"] >= show_from]
        shown.sort(key=lambda a: (a["date"], a["usd"]), reverse=True)
        out_rows = [{"day": a["date"], "market": a["market"],
                     "name": self.names.label(a["market"]),
                     "usd": round(a["usd"], 2),
                     "status": "/".join(sorted(a["status"]))}
                    for a in shown[:40]]
        self._note(f"rewards check: {len(shown)} new market-days shown, "
                   f"{len(fresh) - len(shown)} old strays absorbed")
        return {"ok": True, "new_rows": out_rows, "new_count": len(shown),
                "days": days}

    def _lite_study(self) -> dict:
        """Declared-anchor scoring study (owner, 2026-08-21): what each
        of our markets would pay if scoring anchors on the exchange's
        DECLARED best bid/ask instead of the raw touch. Read-only."""
        if self.stream is None:
            return {"note": "no stream"}
        declared = dict(getattr(self.stream, "declared", {}) or {})
        if not declared:
            return {"note": "no lite frames yet"}
        rows: list[dict] = []
        n_cov = n_div = 0
        tot_cur = tot_alt = 0.0
        for tag, fam in self.families.items():
            for slug in {o.market for o in fam.orders.values()}:
                d = declared.get(slug)
                if not d:
                    continue
                r = fam.lite_recalc(slug, d[0], d[1])
                if r is None:
                    continue
                n_cov += 1
                div = ((r["bb"] is not None and r["raw_bid"] is not None
                        and abs(r["bb"] - r["raw_bid"]) > 0.005)
                       or (r["ba"] is not None and r["raw_ask"] is not None
                           and abs(r["ba"] - r["raw_ask"]) > 0.005))
                r["diverges"] = div
                r["family"] = tag
                n_div += 1 if div else 0
                tot_cur += r["est_cur"]
                tot_alt += r["est_alt"]
                rows.append(r)
        rows.sort(key=lambda x: -abs(x["est_alt"] - x["est_cur"]))
        return {"covered": n_cov, "divergent": n_div,
                "est_current_total": round(tot_cur, 2),
                "est_declared_total": round(tot_alt, 2),
                "rows": rows[:60]}

    def fills_view(self) -> dict:
        """Every purchase as a round trip, newest activity first, joined
        with where the market stands now — one report per entry lot,
        updated as its closes land."""
        rows = []
        hidden_open = 0
        for tag, fam in self.families.items():
            for card in pair_fills(fam.fills):
                card["family"] = tag
                card["name"] = self.names.label(card["market"])
                b = fam.cache.any_age(card["market"])
                card["now_bid"] = (b.bids[0][0]
                                   if b is not None and b.bids else None)
                card["now_ask"] = (b.asks[0][0]
                                   if b is not None and b.asks else None)
                inv = fam.inventory.get(card["market"])
                card["pos_now"] = (round(inv.get("qty", 0.0), 2)
                                   if inv else 0.0)
                exits = [o for o in fam.orders.values()
                         if o.market == card["market"]
                         and o.purpose == "sell"]
                card["exit_resting"] = bool(exits)
                now = time.time()
                card["exit_rate"] = round(sum((o.live_est or 0.0)
                                              for o in exits), 4)
                card["exit_earned"] = round(sum(
                    (o.live_est or 0.0) * (now - o.placed_ts) / 86400.0
                    for o in exits if o.placed_ts > 0), 4)
                card["net"] = round(card_net(card), 4)
                if not card_visible(card, now):
                    if card_is_open(card):
                        hidden_open += 1   # open AND profitable — off
                                           # the list, still counted
                    continue
                rows.append(card)
        # open lots first, newest activity first within each group
        rows.sort(key=lambda x: (
            0 if (x.get("open_qty", 0) > 0.005
                  and not x.get("stray_close")) else 1,
            -x.get("last_ts", x["ts"])))
        return {"ok": True, "fills": rows[:150],
                "open_hidden": hidden_open}

    def book_view(self, slug: str) -> dict:
        """The raw shape of one market's book, with our own orders
        marked — the owner looks at the truth himself."""
        for fam in self.families.values():
            b = fam.cache.any_age(slug)
            if b is None:
                continue
            ours = [{"side": o.side, "price": o.price, "qty": o.qty,
                     "purpose": o.purpose, "est": o.live_est,
                     "verdict": o.verdict}
                    for o in fam.orders.values() if o.market == slug]
            inv = fam.inventory.get(slug)
            return {"ok": True, "market": slug,
                    "name": self.names.label(slug),
                    "age_s": round(time.time() - b.fetched_at, 1),
                    "tick": b.tick,
                    "bids": [[p, q] for p, q in b.bids[:12]],
                    "asks": [[p, q] for p, q in b.asks[:12]],
                    "ours": ours,
                    "fair": (self.silver.model_fair(slug)
                             if hasattr(self, "silver") else None),
                    "band": fam._band(slug, b.bids, b.asks, b.tick),
                    "conf": round(fam.evidence.confidence(slug), 3),
                    "position": ({"qty": round(inv.get("qty", 0), 2),
                                  "cost": round(inv.get("cost", 0), 2)}
                                 if inv else None),
                    "ladder": fam.ladder_view(slug)}
        return {"ok": False, "note": "no book cached for this market yet"}

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

    def _stage(self, stage: str, pct: int) -> None:
        if not self._first_cycle_done:
            self.boot_stage = {"stage": stage, "pct": pct,
                               "ts": round(time.time(), 1)}

    def _cycle_locked(self, now: float) -> dict:
        self._stage("checking the floor and switches", 5)
        self.flatten = flatten_active()
        self.floor.write_want(self.master.on or self.flatten)
        self._floor_ok = self.floor.acked(now)
        self._stage("fetching the account's resting orders", 10)
        orders = self.client.open_orders()
        self._stage("fetching positions", 18)
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
        self.publish_files(now)
        if now - self._history_at > 6 * 3600.0:
            self._history_at = now
            hist, day_totals, recent = load_history()
            if hist:
                for fam in self.families.values():
                    fam.history = hist
                    fam.recent_paid = recent
            if day_totals:
                self.actuals_by_day = day_totals
        summaries = {}
        fam_pct = {"politics": 25, "cfb": 78, "nfl": 88, "nba": 92}
        for key, fam in self.families.items():
            self._stage(f"{fam.cfg.name}: discovering, reading terms, "
                        f"scoring books", fam_pct.get(key, 94))
            if fam.cfg.proven_usd > 0:
                # graduation takes STABILITY and HIGH EARNINGS (owner,
                # 2026-08-22): paid on 3+ of the last 7 days, averaging
                # at least the bar — no reaching back to the old era
                fam.proven = {
                    mkt for mkt, (avg, nd)
                    in getattr(fam, "recent_paid", {}).items()
                    if avg >= fam.cfg.graduate_paid_usd
                    and nd >= fam.cfg.graduate_days}
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
        self._stage("first save", 98)
        st = self._state(now, summaries)
        self.last_state = st
        self.store.save_local(st)
        self.store.maybe_save_remote(st)
        if not self._first_cycle_done:
            self._first_cycle_done = True
            self.boot_stage = {"stage": "running", "pct": 100,
                               "ts": round(time.time(), 1)}
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
