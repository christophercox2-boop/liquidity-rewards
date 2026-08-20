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
