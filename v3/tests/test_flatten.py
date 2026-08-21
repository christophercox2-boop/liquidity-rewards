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


class TestCeilingEnforcement(unittest.TestCase):
    """00:30Z lesson: reprices grew orders past the $100 ceiling
    ($121.99 on the book). The ceiling binds everywhere, and an
    over-ceiling book trims its worst value first."""

    def test_trim_pulls_worst_value_until_under(self):
        from v3.tests.test_family import Rig, A, C
        from v3.family import FamilyConfig, FamilyOrder
        from v3.intents import BUY_LONG
        cfg = FamilyConfig(name="P", tag="P", capital_usd=1.0)
        r = Rig(cfg=cfg)
        r.add_market(A)
        # two orders on the book: $1.26 at risk vs a $1 ceiling; "good"
        # rests near the touch and earns, "bad" is deep and earns ~nothing
        for oid, px, qty in (("good", 0.43, 2.0),    # $0.86 at risk
                             ("bad", 0.02, 20.0)):   # $0.40 at risk
            r.exchange.live[oid] = {"id": oid, "market": A, "side": "BUY",
                                    "price": px, "size": qty,
                                    "intent": BUY_LONG, "manual": False}
            r.fam.orders[oid] = FamilyOrder(
                id=oid, market=A, side="BUY", price=px, qty=qty,
                intent=BUY_LONG, placed_ts=0.0, purpose="earn")
        r.cycle()
        self.assertNotIn("bad", r.fam.orders)        # worst $/day-per-$ went
        self.assertIn("good", r.fam.orders)
        self.assertLessEqual(r.fam.family_spent(), 1.0 + 1e-9)

    def test_programless_read_is_dead_ground_until_a_program_appears(self):
        from v3.tests.test_family import Rig, A
        r = Rig()
        r.add_market(A)
        # a discovered market with NO program at the incentives API
        r.add_market("ushsscc-ushrsc-wi-2026-11-03-0", event="WI House seats")
        del r.exchange.prog_raw["ushsscc-ushrsc-wi-2026-11-03-0"]
        r.cycle(advance=r.fam.cfg.terms_full_s + 1)
        self.assertIn("ushsscc-ushrsc-wi-2026-11-03-0", r.fam.known_dead)
        self.assertTrue(r.fam._dead_here("ushsscc-ushrsc-wi-2026-11-03-0"))
        # the pool arrives later -> alive again
        from v3.tests.test_family import LIVE_PROG
        import copy
        r.exchange.prog_raw["ushsscc-ushrsc-wi-2026-11-03-0"] = copy.deepcopy(LIVE_PROG)
        r.cycle(advance=r.fam.cfg.terms_full_s + 1)
        self.assertNotIn("ushsscc-ushrsc-wi-2026-11-03-0", r.fam.known_dead)


class TestCoverInTightBooks(unittest.TestCase):
    def test_cover_bid_rests_under_a_locked_ask(self):
        # 00:37Z: cover bids were refused ("bid 4c would cross the best
        # ask 4c") in tight books — the price must duck under the ask
        from v3.tests.test_family import Rig, A
        from v3.family import FamilyConfig
        from v3.scoring import Book
        from v3.intents import SELL_SHORT
        cfg = FamilyConfig(name="P", tag="P", capital_usd=0.0)
        r = Rig(cfg=cfg)
        tight = Book(bids=((0.04, 50.0), (0.02, 60000.0)),
                     asks=((0.04, 40.0), (0.98, 60000.0)),
                     tick=0.01, fetched_at=r.now)
        r.add_market(A, book=tight)
        r.positions[A] = (-100.0, -40.0)     # short, received ~40c
        r.cycle()
        covers = [o for o in r.fam.orders.values() if o.intent == SELL_SHORT]
        self.assertEqual(len(covers), 1)
        self.assertLessEqual(covers[0].price, 0.03)   # under the 4c ask


class TestOwnerDirectives0821(unittest.TestCase):
    """2026-08-21 morning: scope entries to gov/senate/2028, Silver keeps
    us off the wrong side of value, no ghosts after a move."""

    def test_entry_scope_blocks_out_of_family_markets(self):
        from v3.tests.test_family import Rig, A
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", capital_usd=100.0,
                           enter_tokens=("usgub", "usse"))
        r = Rig(cfg=cfg)
        r.add_market(A)                              # vmc-ussemov... contains usse
        r.add_market("paccc-usho-midterms-2026-11-03-rep", event="House control")
        r.cycle()
        mkts = {o.market for o in r.fam.orders.values()}
        self.assertIn(A, mkts)
        self.assertNotIn("paccc-usho-midterms-2026-11-03-rep", mkts)

    def test_silver_fair_blocks_wrong_side(self):
        from v3.tests.test_family import Rig, A
        r = Rig()
        r.add_market(A)
        r.fam.fairs = lambda s: 0.30     # model says 30c; touch is 44c/47c
        r.cycle()
        for o in r.fam.orders.values():
            if o.side == "BUY":
                self.assertLessEqual(o.price, 0.32)  # no bids above fair+2t
        # asks at 0.48 are fine (above fair) — and must still exist
        self.assertTrue(any(o.side == "SELL" for o in r.fam.orders.values()))

    def test_failed_cancel_keeps_original_tracked_and_retries(self):
        from v3.tests.test_family import Rig, A
        r = Rig()
        r.add_market(A)
        r.cycle()
        rec = next(o for o in r.fam.orders.values() if o.side == "BUY")
        # the exchange refuses this order's cancel once, then allows it
        real_post = r.exchange.post
        refuse = {"n": 0}
        def post(url, body, path=None, **kw):
            if "/cancel" in url and rec.id in url and refuse["n"] == 0:
                refuse["n"] = 1
                raise __import__("v3.api", fromlist=["ApiError"]).ApiError("nope", status=500)
            return real_post(url, body, path=path, **kw)
        r.exchange.post = post
        # force a reprice of rec: the touch moves, so the best spot moves
        from v3.tests.test_family import politics_book
        r.exchange.books[A] = politics_book(r.now, bid=0.40, ask=0.47)
        r.fam.last_action.clear()
        r.fam.cfg.reprice_gain_day = -1.0            # any move clears the bar
        r.cycle(advance=3700.0)
        self.assertIn(rec.id, r.fam.orders)          # ghost stays TRACKED
        self.assertIn("retrying", r.fam.orders[rec.id].why)
        self.assertIn(rec.id, r.exchange.live)       # and really still rests
        r.cycle()                                    # retry pass kills it
        self.assertNotIn(rec.id, r.fam.orders)
        self.assertNotIn(rec.id, r.exchange.live)

    def test_race_fair_reads_both_tables(self):
        from v3.silver import SilverFairs
        sf = SilverFairs()
        sf.races = {"ga": {"dem": 0.42, "rep": 0.58}}
        sf.gov_races = {"or": {"dem": 0.88, "rep": 0.12}}
        self.assertEqual(sf.race_fair("ussewc-usse-ga-2026-11-03-rep"), 0.58)
        self.assertEqual(sf.race_fair("usgubewc-usgub-or-2026-11-03-dem"), 0.88)
        self.assertIsNone(sf.race_fair("usgubewc-usgub-ri-2026-11-03-kenblo"))
        self.assertIsNone(sf.race_fair("vmc-usgubmov-or-2026-11-03-d12-15"))

    def test_existing_out_of_scope_orders_are_cycled_out(self):
        from v3.tests.test_family import Rig, A
        r = Rig()
        r.add_market(A)
        r.add_market("paccc-usho-midterms-2026-11-03-rep", event="House control")
        r.cycle()                                    # enters both (no scope yet)
        self.assertIn("paccc-usho-midterms-2026-11-03-rep",
                      {o.market for o in r.fam.orders.values()})
        r.fam.cfg.enter_tokens = ("usse",)           # the owner narrows scope
        r.cycle()
        mkts = {o.market for o in r.fam.orders.values()}
        self.assertNotIn("paccc-usho-midterms-2026-11-03-rep", mkts)
        self.assertIn(A, mkts)                       # in-scope stays


class TestTriageProgress(unittest.TestCase):
    def test_summary_reports_the_sweep(self):
        from v3.tests.test_family import Rig, A, C
        r = Rig()
        r.add_market(A)
        r.add_market(C, event="House control")
        s = r.cycle()
        tg = s["triage"]
        self.assertEqual(tg["total"], 2)
        self.assertEqual(tg["done"], 2)          # both scored on cycle one
        self.assertGreaterEqual(tg["per_cycle"], 1)


class TestPayoutButton(unittest.TestCase):
    def mon(self, rows):
        import tempfile
        self.dir = tempfile.TemporaryDirectory()
        p = self.dir.name
        for k, v in (("V3_STATE_PATH", "s.json"), ("V3_FLOOR_PATH", "f.json"),
                     ("V1_ACK_PATH", "a1.json"), ("V2_ACK_PATH", "a2.json")):
            os.environ[k] = os.path.join(p, v)
        os.environ["V3_FLATTEN"] = "0"
        os.environ["GITHUB_TOKEN"] = ""
        m = Monitor()

        class C:
            def earnings(self, start):
                return list(rows)
        m.client = C()
        return m

    def tearDown(self):
        for k in ("V3_STATE_PATH", "V3_FLOOR_PATH", "V1_ACK_PATH",
                  "V2_ACK_PATH", "V3_FLATTEN"):
            os.environ.pop(k, None)
        self.dir.cleanup()

    def test_first_check_records_a_baseline_not_2566_new_rows(self):
        import datetime as dt
        d0 = (dt.datetime.now(dt.timezone.utc)
              - dt.timedelta(days=1)).strftime("%Y-%m-%d")
        d1 = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
        rows = [{"date": "2026-08-01", "market": "old1",     # OLDER than the
                 "program_type": "lp", "reward_usd": 0.5,    # requested start:
                 "status": "PAID"},                          # the API does this
                # the exchange SPLITS one market-day into rows by status
                {"date": d0, "market": "m1",
                 "program_type": "lp", "reward_usd": 1.5, "status": "PAID"},
                {"date": d0, "market": "m1",
                 "program_type": "lp", "reward_usd": 0.19, "status": "SKIPPED"}]
        m = self.mon(rows)
        r1 = m.refresh_rewards()
        self.assertEqual(r1["new_count"], 0)
        self.assertIn("baseline", r1["note"])
        self.assertEqual(r1["days"][d0], 1.5)        # SKIPPED not in totals
        # second check, nothing changed: split rows must NOT flip-flop
        r2 = m.refresh_rewards()
        self.assertEqual(r2["new_count"], 0)
        self.assertNotIn("note", r2)
        # the API's stray window shifts: an ANCIENT row appears — absorbed
        rows.append({"date": "2026-07-29", "market": "fla-ref",
                     "program_type": "lp", "reward_usd": 2.07, "status": "PAID"})
        r2b = m.refresh_rewards()
        self.assertEqual(r2b["new_count"], 0)
        # a truly new posting appears: exactly one new market-day shows
        rows.append({"date": d1, "market": "m3",
                     "program_type": "lp", "reward_usd": 2.0, "status": "PENDING"})
        r3 = m.refresh_rewards()
        self.assertEqual(r3["new_count"], 1)
        self.assertEqual(r3["new_rows"][0]["day"], d1)


class TestSilverLogAndWatcher(unittest.TestCase):
    def test_race_moves_are_logged(self):
        from v3.silver import SilverFairs
        sf = SilverFairs(clock=lambda: 100.0)
        sf.gov_races = {"ga": {"dem": 0.40, "rep": 0.60, "name": "Georgia"}}
        sf._diff_races(sf.gov_races,
                       {"ga": {"dem": 0.37, "rep": 0.63, "name": "Georgia"}},
                       "governor", 200.0)
        self.assertEqual(len(sf.changes), 1)
        c = sf.changes[0]
        self.assertEqual((c["old"], c["new"]), (60.0, 63.0))
        # a sub-half-point wiggle is noise, not a move
        sf._diff_races({"ga": {"rep": 0.630}},
                       {"ga": {"rep": 0.632, "name": "Georgia"}},
                       "governor", 300.0)
        self.assertEqual(len(sf.changes), 1)

    def test_floor_skips_a_retired_v2(self):
        import tempfile
        from v3 import floor
        with tempfile.TemporaryDirectory() as p:
            os.environ["V3_FLOOR_PATH"] = os.path.join(p, "f.json")
            os.environ["V1_ACK_PATH"] = os.path.join(p, "a1.json")
            os.environ["V2_ACK_PATH"] = os.path.join(p, "a2.json")
            os.environ["V2_ENABLED"] = "0"
            try:
                f = floor.Floor(clock=lambda: 1000.0)
                floor.ack("v1", True, clock=lambda: 999.0)
                self.assertTrue(f.acked())       # no v2 ack needed
                os.environ["V2_ENABLED"] = "1"
                self.assertFalse(f.acked())      # running v2 must ack
            finally:
                for k in ("V3_FLOOR_PATH", "V1_ACK_PATH", "V2_ACK_PATH",
                          "V2_ENABLED"):
                    os.environ.pop(k, None)

    def test_watcher_pushes_only_on_truly_new_rows(self):
        import tempfile
        self.dir = tempfile.TemporaryDirectory()
        p = self.dir.name
        for k, v in (("V3_STATE_PATH", "s.json"), ("V3_FLOOR_PATH", "f.json"),
                     ("V1_ACK_PATH", "a1.json"), ("V2_ACK_PATH", "a2.json")):
            os.environ[k] = os.path.join(p, v)
        os.environ["V3_FLATTEN"] = "0"
        os.environ["GITHUB_TOKEN"] = ""
        try:
            m = Monitor()
            rows = [{"date": "2026-08-19", "market": "m1",
                     "program_type": "lp", "reward_usd": 0.6,
                     "status": "PENDING"}]

            class C:
                def earnings(self, start):
                    return list(rows)
            m.client = C()
            pushes = []
            m.alerts.notify = lambda t, msg, priority="default": pushes.append(t)
            m.refresh_rewards()                  # baseline
            r = m.refresh_rewards()
            self.assertEqual(r["new_count"], 0)  # quiet when nothing new
            rows.append({"date": "2026-08-20", "market": "m2",
                         "program_type": "lp", "reward_usd": 3.0,
                         "status": "PENDING"})
            r = m.refresh_rewards()
            self.assertEqual(r["new_count"], 1)  # the watcher would push this
        finally:
            for k in ("V3_STATE_PATH", "V3_FLOOR_PATH", "V1_ACK_PATH",
                      "V2_ACK_PATH", "V3_FLATTEN"):
                os.environ.pop(k, None)
            self.dir.cleanup()


class TestV1Port(unittest.TestCase):
    """1.0's essentials, now 3.0's: the front door, the repo files, the
    owner's own order form."""

    def test_floor_needs_nobody_when_both_are_retired(self):
        import tempfile
        from v3 import floor
        with tempfile.TemporaryDirectory() as p:
            os.environ["V3_FLOOR_PATH"] = os.path.join(p, "f.json")
            try:
                self.assertEqual(floor.Floor.required(), ())
                self.assertTrue(floor.Floor(clock=lambda: 1.0).acked())
            finally:
                os.environ.pop("V3_FLOOR_PATH", None)

    def test_rewards_csv_preserves_unreachable_history(self):
        import tempfile
        with tempfile.TemporaryDirectory() as p:
            for k, v in (("V3_STATE_PATH", "s.json"),
                         ("V3_FLOOR_PATH", "f.json")):
                os.environ[k] = os.path.join(p, v)
            os.environ["GITHUB_TOKEN"] = ""
            try:
                m = Monitor()
                existing = ("date,market,program_type,reward_usd,status\n"
                            "2026-07-01,ancient,liquidityProgram,9.99,PAID\n"
                            "2026-08-18,m1,liquidityProgram,1.5,PAID\n")
                rows = [{"date": "2026-08-18", "market": "m1",
                         "program_type": "liquidityProgram",
                         "reward_usd": 1.5, "status": "PAID"},
                        {"date": "2026-08-20", "market": "m2",
                         "program_type": "liquidityProgram",
                         "reward_usd": 2.0, "status": "PENDING"}]
                text = m.compose_rewards_csv(rows, existing)
                lines = text.strip().split("\n")
                self.assertEqual(lines[0],
                                 "date,market,program_type,reward_usd,status")
                self.assertIn("2026-07-01,ancient,liquidityProgram,9.99,PAID",
                              lines)          # history beyond the API kept
                self.assertIn("2026-08-20,m2,liquidityProgram,2,PENDING",
                              lines)
                self.assertEqual(len([l for l in lines if ",m1," in l]), 1)
                md = m.compose_status_md(1_787_300_000.0)
                self.assertIn("Politics", md)
                self.assertIn("/day resting", md)
            finally:
                for k in ("V3_STATE_PATH", "V3_FLOOR_PATH"):
                    os.environ.pop(k, None)

    def test_owner_place_routes_and_manual_is_untouchable(self):
        from v3.tests.test_family import Rig, A
        r = Rig()
        r.add_market(A)
        r.cycle()
        res_like = r.fam.desk.place_resting(A, "BUY", 0.30, 3.0,
                                            initiator="owner", verify=False)
        self.assertTrue(res_like.ok)
        from v3.family import FamilyOrder
        r.fam.orders[res_like.order_id] = FamilyOrder(
            id=res_like.order_id, market=A, side="BUY", price=0.30, qty=3.0,
            intent=res_like.intent, placed_ts=r.now, purpose="manual",
            why="placed by the owner")
        # hours pass; the cull would eat a 30c bid measuring ~0 — but
        # manual orders are the owner's and automation never touches them
        r.fam.last_action.clear()
        r.cycle(advance=7200.0)
        self.assertIn(res_like.order_id, r.fam.orders)
        self.assertEqual(r.fam.orders[res_like.order_id].price, 0.30)
