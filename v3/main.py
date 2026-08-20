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
import time
from pathlib import Path

from . import politics
from .alerts import Alerts
from .api import ApiError, Client
from .books import BookCache
from .family import Family
from .names import Names
from .orders import OrderDesk
from .state import StateStore
from .switch import MasterSwitch

POLL_S = 60.0
ERROR_BACKOFF_CAP_S = 600.0

# name -> (config fn, discover fn). Adding a family = adding a line.
FAMILIES = {
    "politics": (politics.config, politics.discover),
}


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
                switch_on=lambda s=sw: self.master.on and s.on,
                fresh_book=lambda slug, c=cache: c.fresh(slug, 120.0, time.time()),
                log=self._audit,
            )
            fam.desk = desk
            self.families[key] = fam
            self.switches[key] = sw
        self._restore()
        self.boots = [b for b in self.boots if time.time() - b < 86400]
        self.boots.append(time.time())

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
        self.errors = list(saved.get("errors") or [])
        self.boots = list(saved.get("boots") or [])
        self.audit = list(saved.get("audit") or [])
        age = time.time() - (saved.get("saved_at") or 0)
        armed = [k for k, sw in self.switches.items() if sw.on and self.master.on]
        self._note(f"booted build {self.build}; restored state {age:.0f}s old"
                   + (f"; ARMED: {', '.join(armed)}" if armed else ""))
        if armed and saved.get("build") != self.build:
            self.alerts.notify("3.0: new build with a switch ON",
                               f"build {self.build} booted; may place orders "
                               f"({', '.join(armed)})")

    def _state(self, now: float, summaries: dict) -> dict:
        st = {
            "saved_at": now, "build": self.build, "boot_ts": self.boot_ts,
            "boots": self.boots[-20:], "errors": self.errors,
            "audit": self.audit[-60:],
            "master_switch": self.master.to_dict(),
            "names": self.names.to_dict(),
            "summaries": summaries,
            "alerts_log": self.alerts.log[-30:],
        }
        for key, fam in self.families.items():
            st[f"fam_{key}"] = fam.to_dict()
            st[f"sw_{key}"] = self.switches[key].to_dict()
            st[f"touches_{key}"] = touch_snapshot(fam, now)
        return st

    # -- owner controls -----------------------------------------------------

    def switch_tap(self, op: str, which: str = "master") -> dict:
        """A tap on /v3/switch. Persisted IMMEDIATELY, local and remote —
        a restart between a flip and the next save must not undo it."""
        sw = self.switches.get(which, self.master)
        s = sw.op(op)
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

    def public_state(self) -> dict:
        st = dict(self.last_state) if self.last_state else {"saved_at": 0}
        st["switch_view"] = {
            "master": self.master.state(),
            **{k: self.switches[k].state() for k in self.families}}
        return st

    # -- one poll -----------------------------------------------------------

    def cycle(self, now: float | None = None) -> dict:
        now = now or time.time()
        orders = self.client.open_orders()
        positions = self.client.positions_net()
        summaries = {}
        for key, fam in self.families.items():
            on = self.master.on and self.switches[key].on
            try:
                summaries[key] = fam.cycle(now, orders, positions,
                                           self.client, on)
                summaries[key]["name"] = fam.cfg.name
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
