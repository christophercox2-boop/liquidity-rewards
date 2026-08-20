"""Flatten mode: cancel every opening order, keep every exit, then rebuild
under the small ceiling with history guiding the ranking."""

import os
import tempfile
import unittest

from v3 import floor
from v3.main import Monitor, is_exit_order
from v3.intents import BUY_LONG, BUY_SHORT, SELL_LONG, SELL_SHORT


def O(oid, market, intent, price=0.3, size=5.0, manual=False):
    from v3.intents import REST_SIDE
    return {"id": oid, "market": market, "intent": intent,
            "side": REST_SIDE[intent], "price": price, "size": size,
            "manual": manual}


class TestExitClassification(unittest.TestCase):
    def test_every_intent_against_every_position(self):
        long_, short, flat = {"m": (10.0, 3.0)}, {"m": (-10.0, 3.0)}, {}
        cases = [
            (SELL_LONG, long_, True),    # ask while long: exit
            (SELL_SHORT, short, True),   # buy-back bid while short: exit
            (BUY_LONG, short, True),     # any bid while short reduces: exit
            (BUY_SHORT, long_, True),    # any ask while long reduces: exit
            (BUY_LONG, flat, False),     # opening
            (BUY_SHORT, flat, False),    # opening short
            (SELL_LONG, flat, False),    # ask with no stock: not an exit
            (BUY_LONG, long_, False),    # adding to a long: opening
        ]
        for intent, pos, want in cases:
            self.assertEqual(is_exit_order(O("x", "m", intent), pos), want,
                             (intent, pos))


class TestFlattenPass(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        p = self.dir.name
        os.environ["V3_STATE_PATH"] = os.path.join(p, "state.json")
        os.environ["V3_FLOOR_PATH"] = os.path.join(p, "floor.json")
        os.environ["V1_ACK_PATH"] = os.path.join(p, "a1.json")
        os.environ["V2_ACK_PATH"] = os.path.join(p, "a2.json")
        os.environ["V3_FLATTEN"] = "1"
        os.environ["GITHUB_TOKEN"] = ""
        self.mon = Monitor()
        self.cancelled = []
        desk = self.mon.families["politics"].desk
        from v3.orders import OrderResult
        desk.cancel = lambda oid, m, initiator="auto": (
            self.cancelled.append(oid) or OrderResult(ok=True, note="ok",
                                                      order_id=oid))
        self.alerts = []
        self.mon.alerts.notify = lambda t, msg, priority="default": \
            self.alerts.append(t)

    def tearDown(self):
        for k in ("V3_STATE_PATH", "V3_FLOOR_PATH", "V1_ACK_PATH",
                  "V2_ACK_PATH", "V3_FLATTEN"):
            os.environ.pop(k, None)
        self.dir.cleanup()

    def test_openings_cancelled_exits_kept_then_phase_two(self):
        positions = {"mkt-long": (10.0, 3.0), "mkt-short": (-5.0, 2.0)}
        orders = [
            O("open1", "mkt-x", BUY_LONG),
            O("open2", "mkt-long", BUY_LONG),     # ADDS to a long: opening
            O("exit1", "mkt-long", SELL_LONG),
            O("exit2", "mkt-short", SELL_SHORT),
            O("man1", "mkt-y", BUY_SHORT, manual=True),  # all means all
        ]
        s = self.mon._flatten_pass(orders, positions)
        self.assertEqual(set(self.cancelled), {"open1", "open2", "man1"})
        self.assertEqual(s["kept_exits"], 2)
        self.assertFalse(self.mon.flatten_done)      # work happened this pass
        # the clean pass flips to phase two, with the alert
        self.cancelled.clear()
        s = self.mon._flatten_pass([o for o in orders
                                    if o["id"].startswith("exit")], positions)
        self.assertEqual(self.cancelled, [])
        self.assertTrue(self.mon.flatten_done)
        self.assertTrue(any("Flat" in t for t in self.alerts))
        self.assertEqual(s["phase"], "rebuild")

    def test_phase_two_guards_but_spares_the_rebuild(self):
        self.mon.flatten_done = True
        fam = self.mon.families["politics"]
        from v3.family import FamilyOrder
        fam.orders["mine1"] = FamilyOrder(
            id="mine1", market="mkt-z", side="BUY", price=0.3, qty=1.0,
            intent=BUY_LONG, placed_ts=0.0, purpose="earn")
        orders = [O("mine1", "mkt-z", BUY_LONG),     # 3.0's own rebuild order
                  O("stray", "mkt-z", BUY_LONG)]     # nobody's: guard kills it
        self.mon._flatten_pass(orders, {})
        self.assertEqual(self.cancelled, ["stray"])

    def test_flatten_requests_the_floor_even_with_master_off(self):
        self.assertFalse(self.mon.master.on)
        self.mon.floor.write_want(self.mon.master.on or self.mon.flatten)
        self.assertTrue(floor.wanted()[0])


class TestExitsOnlyCycle(unittest.TestCase):
    def test_family_places_no_earn_orders_in_phase_one(self):
        from v3.tests.test_family import Rig, A
        r = Rig()
        r.add_market(A)
        r.fam.inventory[A] = {"qty": 10.0, "cost": 4.0}
        r.positions[A] = (10.0, 4.0)
        r.fam.positions_seen[A] = 10.0
        s = r.fam.cycle(r.now + 60, r.exchange.open_orders(), r.positions,
                        r.exchange, True, exits_only=True)
        self.assertEqual(s["mode"], "flatten — exits only")
        kinds = {o.purpose for o in r.fam.orders.values()}
        self.assertEqual(kinds, {"sell"})            # the exit ask, nothing else


class TestHistoryRanking(unittest.TestCase):
    def test_proven_market_enters_first(self):
        from v3.tests.test_family import Rig, A, C
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet", revive=True,
                           capital_usd=1.0, per_market_usd=2.0)
        r = Rig(cfg=cfg)
        r.add_market(A)
        r.add_market(C, event="House control")
        r.fam.history[C] = 5.0                       # C actually paid us
        r.cycle()
        mkts = {o.market for o in r.fam.orders.values()}
        self.assertEqual(mkts, {C})                  # the ceiling went to C


if __name__ == "__main__":
    unittest.main()


class TestCycleOut(unittest.TestCase):
    def rig(self):
        from v3.tests.test_family import Rig, A, politics_book
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet", revive=True,
                           capital_usd=100.0, per_market_usd=20.0,
                           min_est_day=0.10, weak_pull_s=7200.0,
                           cooldown_s=60.0)
        r = Rig(cfg=cfg)
        r.add_market(A)
        return r, A

    def test_weak_order_is_pulled_after_the_window(self):
        r, A = self.rig()
        r.cycle()
        self.assertTrue(r.fam.orders)
        # the pool collapses to almost nothing: orders now earn ~0.4c/day
        for o in r.exchange.prog_raw.values():
            o["timePeriods"][0]["rewardPool"] = 0.5
        r.cycle(advance=r.fam.cfg.terms_active_s + 1)   # terms re-read, weak starts
        self.assertTrue(any(o.weak_since for o in r.fam.orders.values()))
        r.cycle(advance=7300.0)                          # past the window
        pulls = [l for l in r.fam.log if l.get("event") == "pull"]
        self.assertTrue(any("cycling out" in l.get("why", "") for l in pulls))

    def test_healthy_order_is_not_cycled(self):
        r, A = self.rig()
        r.cycle()
        r.cycle(advance=7300.0)
        pulls = [l for l in r.fam.log if "cycling out" in l.get("why", "")]
        self.assertEqual(pulls, [])
        self.assertTrue(all(not o.weak_since for o in r.fam.orders.values()
                            if o.purpose != "sell"))


class TestFullCycleRegression(unittest.TestCase):
    """The 2026-08-20 22:0x production failure: cycle() died assembling
    state while flatten was active (a local leaked into _state). The whole
    path must run end to end offline."""

    class StubClient:
        def __init__(self):
            self.orders = [O("open1", "m", BUY_LONG)]

        def open_orders(self):
            return list(self.orders)

        def positions_net(self):
            return {}

    def test_cycle_completes_with_flatten_active(self):
        import tempfile
        with tempfile.TemporaryDirectory() as p:
            for k, v in (("V3_STATE_PATH", "state.json"),
                         ("V3_FLOOR_PATH", "floor.json"),
                         ("V1_ACK_PATH", "a1.json"), ("V2_ACK_PATH", "a2.json")):
                os.environ[k] = os.path.join(p, v)
            os.environ["V3_FLATTEN"] = "1"
            os.environ["GITHUB_TOKEN"] = ""
            try:
                mon = Monitor()
                stub = self.StubClient()
                mon.client = stub
                cancelled = []
                from v3.orders import OrderResult

                def cancel(oid, mkt, initiator="auto"):
                    cancelled.append(oid)
                    stub.orders = [o for o in stub.orders if o["id"] != oid]
                    return OrderResult(ok=True, note="ok")
                mon.families["politics"].desk.cancel = cancel
                floor.ack("v1", True)
                floor.ack("v2", True)
                st = mon.cycle()               # must not raise
                self.assertTrue(st["flatten"]["active"])
                self.assertEqual(cancelled, ["open1"])
                st = mon.cycle()               # clean pass -> phase two
                self.assertEqual(st["flatten"]["phase"], "rebuild")
            finally:
                for k in ("V3_STATE_PATH", "V3_FLOOR_PATH", "V1_ACK_PATH",
                          "V2_ACK_PATH", "V3_FLATTEN"):
                    os.environ.pop(k, None)


class TestExitProtection(unittest.TestCase):
    """The 23:12Z incident: adopted position-reducing orders were labelled
    'earn', so maintenance repriced/pulled the owner's exits and their
    collateral blocked the rebuild ceiling."""

    def rig_short(self):
        from v3.tests.test_family import Rig, A
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet", revive=True,
                           capital_usd=0.0)     # no new entries — exits only
        r = Rig(cfg=cfg)
        r.add_market(A)
        # the owner is SHORT 100; a big buy-back bid rests (BUY_LONG,
        # 1.0-style) — an exit by position, an opening by intent
        r.positions[A] = (-100.0, -5.0)
        r.exchange.live["cover"] = {
            "id": "cover", "market": A, "side": "BUY", "price": 0.01,
            "size": 100.0, "intent": BUY_LONG, "manual": False}
        return r, A

    def test_adopted_cover_bid_is_an_exit_not_spend(self):
        r, A = self.rig_short()
        r.cycle()
        rec = r.fam.orders["cover"]
        self.assertEqual(rec.purpose, "sell")
        self.assertEqual(r.fam.family_spent(), 0.0)   # exits never block the ceiling
        # and maintenance never touches it, however long it sits
        r.cycle(advance=8000.0)
        self.assertIn("cover", r.fam.orders)
        self.assertEqual(r.fam.orders["cover"].price, 0.01)

    def test_short_gets_covered_at_touch_under_break_even(self):
        from v3.tests.test_family import Rig, A
        from v3.family import FamilyConfig
        from v3.intents import SELL_SHORT
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet", revive=True,
                           capital_usd=0.0)
        r = Rig(cfg=cfg)
        r.add_market(A)
        # short 100 sold at ~40c (cost -40): no cover resting anywhere
        r.positions[A] = (-100.0, -40.0)
        r.cycle()
        covers = [o for o in r.fam.orders.values()
                  if o.side == "BUY" and o.intent == SELL_SHORT]
        self.assertEqual(len(covers), 1)
        c = covers[0]
        self.assertEqual(c.purpose, "sell")
        self.assertLessEqual(c.price, 0.40 - 0.01)    # never above break-even
        self.assertAlmostEqual(c.qty, 100.0)
        from v3.intents import capital_at_risk
        self.assertEqual(capital_at_risk(c.intent, c.price, c.qty), 0.0)


class TestStalePlansAndPriorities(unittest.TestCase):
    """23:53Z lessons: plans scored under old knobs must not place, and
    the seller outranks new entries for the action budget."""

    def test_stale_scoreboard_cleared_on_config_change(self):
        from v3.tests.test_family import Rig, A
        r = Rig()
        r.add_market(A)
        r.cycle()
        d = r.fam.to_dict()
        self.assertTrue(d["scoreboard"])
        from v3.family import FamilyConfig
        from v3.books import BookCache
        from v3.names import Names
        from v3 import politics
        from v3.family import Family
        fam2 = Family(None, BookCache(), politics.discover,
                      config=FamilyConfig(name="P", per_market_usd=20.0,
                                          min_est_day=0.10),
                      names=Names())
        fam2.restore(d)
        self.assertEqual(fam2.scoreboard, {})        # different knobs: rescan

    def test_under_bar_plan_never_places(self):
        from v3.tests.test_family import Rig, A
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           min_est_day=0.10, capital_usd=100.0)
        r = Rig(cfg=cfg)
        r.add_market(A)
        # a stale crumb plan sneaks into the scoreboard directly
        r.fam.scoreboard[A] = {"ts": r.now, "est": 0.03, "plans": [
            {"side": "BUY", "px": 0.43, "qty": 1.0, "share": 0.01,
             "est": 0.03, "cost": 0.43, "why": "old config"}]}
        r.fam.last_terms_active = r.now
        r.fam.last_terms_full = r.now
        r.fam.cycle(r.now + 1, r.exchange.open_orders(), r.positions,
                    r.exchange, True)
        self.assertNotIn(A, {o.market for o in r.fam.orders.values()})

    def test_seller_outranks_new_entries(self):
        from v3.tests.test_family import Rig, A, C
        from v3.family import FamilyConfig
        from v3.intents import SELL_SHORT
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet", revive=True,
                           capital_usd=100.0, max_actions_per_cycle=1)
        r = Rig(cfg=cfg)
        r.add_market(A)
        r.add_market(C, event="House control")
        r.positions[C] = (-100.0, -40.0)             # a short needs its exit
        r.cycle()
        placed = list(r.fam.orders.values())
        self.assertEqual(len(placed), 1)             # one action, and it went...
        self.assertEqual(placed[0].purpose, "sell")  # ...to the cover, not entry
        self.assertEqual(placed[0].intent, SELL_SHORT)
