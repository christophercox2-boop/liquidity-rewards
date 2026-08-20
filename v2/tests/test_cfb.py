"""College-football family tests: the full chain through the real OrderDesk
rails against the fake exchange, plus the planner's share/budget math and
the game-day window."""

import datetime as dt
import unittest
from zoneinfo import ZoneInfo

from v2.books import BookCache
from v2.cfb import PREFIX, CfbConfig, CfbFamily, resting_ok, slug_days_out
from v2.orders import OrderDesk
from v2.scoring import Book
from v2.tests.test_engine import FakeExchange

ET = ZoneInfo("America/New_York")

ALA = PREFIX + "2026-11-28-ala-9pt5wins"
ARK = PREFIX + "2026-11-28-ark-5pt5wins"
UGA = PREFIX + "2026-11-28-uga-10pt5wins"

ROW = {"pool": 25.0, "target": 5000.0, "df": 0.5, "event_n": 5, "side_pool": 2.5}


def wednesday(h=12) -> float:
    return dt.datetime(2026, 8, 19, h, 0, tzinfo=ET).timestamp()


class FakeClient(FakeExchange):
    """The fake exchange plus the read APIs the family calls."""

    def __init__(self, books=None):
        super().__init__()
        self.books: dict[str, Book] = books or {}
        self.prog_raw: dict[str, dict] = {}

    def book(self, slug, fetched_at=None):
        b = self.books[slug]
        return Book(bids=b.bids, asks=b.asks, tick=b.tick,
                    fetched_at=fetched_at or b.fetched_at)

    def programs(self, slugs):
        return {s: self.prog_raw[s] for s in slugs if s in self.prog_raw}


def polite_book(now):
    # real touches both sides, qualifying walls far behind
    return Book(bids=((0.44, 20.0), (0.01, 6000.0)),
                asks=((0.47, 20.0), (0.99, 6000.0)),
                tick=0.01, fetched_at=now)


def wall_only_book(now):
    # a lone qualifier wall on the bid side, nothing else in the market
    return Book(bids=((0.01, 6000.0),), asks=(),
                tick=0.01, fetched_at=now)


class Rig:
    def __init__(self, switch=True, now=None, cfg=None):
        self.now = now if now is not None else wednesday()
        self.exchange = FakeClient()
        self.cache = BookCache()
        self.switch = switch
        self.alerts = []
        self.desk = OrderDesk(
            client=self.exchange,
            whitelist=lambda s: s.startswith(PREFIX),
            switch_on=lambda: self.switch,
            fresh_book=lambda s: self.cache.fresh(s, 120, self.now),
            log=lambda e: None,
            sleep=lambda s: None, clock=lambda: self.now,
        )
        self.fam = CfbFamily(self.desk, self.cache, config=cfg or CfbConfig(),
                             alert=lambda t, m: self.alerts.append((t, m)),
                             clock=lambda: self.now)
        self.positions: dict[str, tuple] = {}
        self.survey_terms: dict[str, dict] = {}

    def add_market(self, slug, book):
        self.exchange.books[slug] = book
        self.survey_terms[slug] = dict(ROW)
        self.exchange.prog_raw[slug] = {
            "timePeriods": [{"programId": "cfb_1", "rewardPool": 25.0,
                             "targetSize": 5000, "discountFactor": 0.5,
                             "status": "LIVE"}]}

    def cycle(self):
        return self.fam.cycle(self.now, self.exchange.open_orders(),
                              self.positions, self.exchange,
                              self.survey_terms, self.switch)


class TestWindow(unittest.TestCase):
    def test_week_shape_in_season(self):
        def at(day, hour):        # September 2026: Wed 2 ... Mon 7
            return dt.datetime(2026, 9, day, hour, 0, tzinfo=ET).timestamp()
        self.assertTrue(resting_ok(at(2, 12)))     # Wednesday noon
        self.assertTrue(resting_ok(at(3, 16)))     # Thursday 4pm
        self.assertFalse(resting_ok(at(3, 17)))    # Thursday 5pm — out
        self.assertFalse(resting_ok(at(4, 12)))    # Friday — out
        self.assertFalse(resting_ok(at(5, 12)))    # Saturday — out
        self.assertFalse(resting_ok(at(6, 5)))     # Sunday 5am — out
        self.assertTrue(resting_ok(at(6, 6)))      # Sunday 6am — back in
        self.assertTrue(resting_ok(at(7, 12)))     # Monday

    def test_no_game_days_before_the_season(self):
        # owner, 2026-08-20: "there aren't any games until next week" —
        # before Week 0 the Thursday-Sunday pull must not fire
        for day, hour in ((20, 17), (21, 12), (22, 12), (23, 5)):
            self.assertTrue(resting_ok(
                dt.datetime(2026, 8, day, hour, 0, tzinfo=ET).timestamp()))

    def test_days_out(self):
        self.assertEqual(slug_days_out(ALA, wednesday()), 101)


class TestPlanner(unittest.TestCase):
    def test_polite_share_and_budget(self):
        r = Rig()
        plans = r.fam.plan_market(polite_book(r.now), ROW)
        self.assertEqual({p["side"] for p in plans}, {"BUY", "SELL"})
        for p in plans:
            self.assertLessEqual(p["share"], 0.10 + 1e-9)
            self.assertLessEqual(p["cost"], 0.50 + 1e-9)
            self.assertGreaterEqual(p["est"], 0.02)

    def test_wall_only_gets_probe_money_in_front_of_the_wall(self):
        r = Rig()
        plans = r.fam.plan_market(wall_only_book(r.now), ROW)
        self.assertEqual(len(plans), 1)          # ask side can't qualify
        p = plans[0]
        self.assertEqual(p["side"], "BUY")
        self.assertGreater(p["px"], 0.01)        # in FRONT of the wall
        self.assertLessEqual(p["px"], 0.11 + 1e-9)   # no value anchor: short leash
        self.assertLessEqual(p["cost"], 0.05 + 1e-9)  # probe money only
        self.assertGreaterEqual(p["est"], 0.02)

    def test_below_target_side_is_skipped(self):
        r = Rig()
        thin = Book(bids=((0.44, 20.0), (0.01, 3000.0)),   # 3,020 < 5,000
                    asks=((0.47, 20.0), (0.99, 6000.0)),
                    tick=0.01, fetched_at=r.now)
        plans = r.fam.plan_market(thin, ROW)
        self.assertEqual([p["side"] for p in plans], ["SELL"])


class TestCycle(unittest.TestCase):
    def test_switch_off_places_nothing(self):
        r = Rig(switch=False)
        r.add_market(ALA, polite_book(r.now))
        s = r.cycle()
        self.assertEqual(s["mode"], "observing")
        self.assertEqual(r.exchange.posts, [])

    def test_places_within_market_cap_and_separately(self):
        r = Rig()
        r.add_market(ALA, polite_book(r.now))
        r.cycle()                    # scan pass fills the scoreboard
        s = r.cycle()                # placement pass
        self.assertGreater(len(s["orders"]), 0)
        spent = sum(o["price"] * o["qty"] if o["side"] == "BUY"
                    else (1 - o["price"]) * o["qty"] for o in s["orders"])
        self.assertLessEqual(spent, 1.0 + 1e-9)
        for o in s["orders"]:
            self.assertTrue(o["market"].startswith(PREFIX))
        # the desk refuses anything outside this family
        res = r.desk.place_resting("scc-senate-gop-2026-11-03-49", "BUY",
                                   0.10, 1.0, net_position=0.0)
        self.assertFalse(res.ok)
        self.assertIn("whitelist", res.note)

    def test_game_window_pulls_and_holds(self):
        r = Rig()
        r.add_market(ALA, polite_book(r.now))
        r.cycle()
        s = r.cycle()
        n = len(s["orders"])
        self.assertGreater(n, 0)
        # an in-season Friday: everything non-exit comes out, nothing new in
        r.now = dt.datetime(2026, 9, 4, 12, 0, tzinfo=ET).timestamp()
        for slug in list(r.exchange.books):
            r.exchange.books[slug] = polite_book(r.now)
        s = r.cycle()
        self.assertEqual(s["mode"], "game window")
        s = r.cycle()
        self.assertEqual(len(s["orders"]), 0)

    def test_fill_alerts_and_rests_exit(self):
        r = Rig()
        r.add_market(ALA, polite_book(r.now))
        r.cycle()
        r.cycle()
        bid = next(o for o in r.fam.orders.values() if o.side == "BUY")
        # the exchange fills the bid: order vanishes, position appears
        del r.exchange.live[bid.id]
        r.positions[ALA] = (bid.qty, bid.qty * bid.price)
        r.now += 3600
        r.exchange.books[ALA] = polite_book(r.now)
        s = r.cycle()
        self.assertTrue(any("CFB fill" in t for t, _ in r.alerts))
        exits = [o for o in s["orders"] if o["purpose"] == "sell"]
        self.assertEqual(len(exits), 1)
        self.assertGreaterEqual(exits[0]["price"], bid.price + 0.01 - 1e-9)

    def test_dead_program_pulls(self):
        r = Rig()
        r.add_market(ALA, polite_book(r.now))
        r.cycle()
        r.cycle()
        self.assertGreater(len(r.fam.orders), 0)
        # the pool disappears: live terms refresh sees it dead
        r.exchange.prog_raw[ALA]["timePeriods"][0]["rewardPool"] = 0
        r.fam.last_terms = 0.0
        r.now += 3600
        r.exchange.books[ALA] = polite_book(r.now)
        s = r.cycle()
        self.assertEqual([o for o in s["orders"] if o["purpose"] != "sell"], [])

    def test_state_roundtrip(self):
        r = Rig()
        r.add_market(ALA, polite_book(r.now))
        r.cycle()
        r.cycle()
        d = r.fam.to_dict()
        r2 = Rig()
        r2.fam.restore(d)
        self.assertEqual(set(r2.fam.orders), set(r.fam.orders))
        self.assertEqual(r2.fam.positions_seen, r.fam.positions_seen)


if __name__ == "__main__":
    unittest.main()


class TestScanNeverStarves(unittest.TestCase):
    def test_actives_leave_scan_slots(self):
        # first night's bug: with more active markets than the book budget,
        # active refreshes ate every fetch, the scoreboard never filled,
        # and the family stopped placing — "on but not doing anything"
        r = Rig()
        slugs = [PREFIX + f"2026-11-28-tm{i}-5pt5wins" for i in range(10)]
        for s in slugs:
            r.add_market(s, polite_book(r.now))
        # make all ten active by hand (placement caps don't matter here) —
        # resting on the fake exchange too, or reconcile calls them vanished
        from v2.cfb import CfbOrder
        for i, s in enumerate(slugs):
            r.fam.orders[f"x{i}"] = CfbOrder(
                id=f"x{i}", market=s, side="BUY", price=0.44, qty=1.0,
                intent="ORDER_INTENT_BUY_LONG", placed_ts=r.now, purpose="earn")
            r.exchange.live[f"x{i}"] = {
                "id": f"x{i}", "market": s, "side": "BUY", "price": 0.44,
                "size": 1.0, "intent": "ORDER_INTENT_BUY_LONG"}
        fresh = PREFIX + "2026-11-28-newteam-6pt5wins"
        r.add_market(fresh, polite_book(r.now))
        r.now += 300
        for s in r.exchange.books:
            r.exchange.books[s] = polite_book(r.now)
        r.cycle()
        self.assertIn(fresh, r.fam.scoreboard, "scan starved by active refreshes")
        self.assertTrue(r.fam.scoreboard[fresh].get("plans"))

    def test_scoreboard_survives_restart(self):
        r = Rig()
        r.add_market(ALA, polite_book(r.now))
        r.cycle()
        self.assertTrue(r.fam.scoreboard)
        r2 = Rig()
        r2.fam.restore(r.fam.to_dict())
        self.assertEqual(set(r2.fam.scoreboard), set(r.fam.scoreboard))
