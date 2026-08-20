"""NFL family tests: behind-the-touch only (the owner's 2026-08-20
correction), its own weekly window, and prefix separation."""

import datetime as dt
import unittest
from zoneinfo import ZoneInfo

from v2.books import BookCache
from v2.family import Family, nfl, resting_ok
from v2.orders import OrderDesk
from v2.scoring import Book
from v2.tests.test_cfb import FakeClient, polite_book, wall_only_book

ET = ZoneInfo("America/New_York")

PLAYOFF = "aqc-nfl-2027-01-10-playoffq-ne"
MVP = "tec-nfl-mvp-2027-02-11-w-mandel"

ROW = {"pool": 300.0, "target": 5000.0, "df": 0.3, "event_n": 32,
       "side_pool": 4.69}


def wednesday(h=12) -> float:
    return dt.datetime(2026, 8, 19, h, 0, tzinfo=ET).timestamp()


class Rig:
    def __init__(self, switch=True, now=None):
        self.now = now if now is not None else wednesday()
        self.cfg = nfl()
        self.exchange = FakeClient()
        self.cache = BookCache()
        self.switch = switch
        self.alerts = []
        self.desk = OrderDesk(
            client=self.exchange,
            whitelist=lambda s: s.startswith(self.cfg.prefixes),
            switch_on=lambda: self.switch,
            fresh_book=lambda s: self.cache.fresh(s, 120, self.now),
            log=lambda e: None,
            sleep=lambda s: None, clock=lambda: self.now,
        )
        self.fam = Family(self.desk, self.cache, config=self.cfg,
                          alert=lambda t, m: self.alerts.append((t, m)),
                          clock=lambda: self.now)
        self.positions: dict[str, tuple] = {}
        self.survey_terms: dict[str, dict] = {}

    def add_market(self, slug, book):
        self.exchange.books[slug] = book
        self.survey_terms[slug] = dict(ROW)
        self.exchange.prog_raw[slug] = {
            "timePeriods": [{"programId": "nfl_1", "rewardPool": 300.0,
                             "targetSize": 5000, "discountFactor": 0.3,
                             "status": "LIVE"}]}

    def cycle(self):
        return self.fam.cycle(self.now, self.exchange.open_orders(),
                              self.positions, self.exchange,
                              self.survey_terms, self.switch)


class TestWindow(unittest.TestCase):
    def test_week_shape(self):
        cfg = nfl()

        def at(day, hour):
            return resting_ok(
                dt.datetime(2026, 8, day, hour, 0, tzinfo=ET).timestamp(), cfg)
        self.assertFalse(at(17, 12))   # Monday — out (MNF)
        self.assertFalse(at(18, 5))    # Tuesday 5am — out
        self.assertTrue(at(18, 6))     # Tuesday 6am — in
        self.assertTrue(at(19, 12))    # Wednesday — in
        self.assertTrue(at(20, 16))    # Thursday 4pm — in
        self.assertFalse(at(20, 17))   # Thursday 5pm — out (TNF)
        self.assertFalse(at(22, 12))   # Saturday — out
        self.assertFalse(at(23, 12))   # Sunday — out


class TestBehindTheTouch(unittest.TestCase):
    def test_never_prices_in_front_of_the_touch(self):
        r = Rig()
        plans = r.fam.plan_market(polite_book(r.now), ROW)
        self.assertTrue(plans)
        for p in plans:
            if p["side"] == "BUY":
                self.assertLessEqual(p["px"], 0.44 + 1e-9)   # bid touch
            else:
                self.assertGreaterEqual(p["px"], 0.47 - 1e-9)  # ask touch
            self.assertLessEqual(p["share"], 0.10 + 1e-9)
            self.assertNotIn("solo", p)

    def test_wall_only_book_is_skipped_entirely(self):
        # college steps in front of the wall; NFL must not — a side whose
        # only depth is the qualifier wall earns nothing behind the touch,
        # so the family simply stays out of the market
        r = Rig()
        plans = r.fam.plan_market(wall_only_book(r.now), ROW)
        self.assertEqual(plans, [])

    def test_places_only_real_touch_markets(self):
        r = Rig()
        r.add_market(PLAYOFF, polite_book(r.now))
        r.add_market(MVP, wall_only_book(r.now))
        r.cycle()
        s = r.cycle()
        mkts = {o["market"] for o in s["orders"]}
        self.assertIn(PLAYOFF, mkts)
        self.assertNotIn(MVP, mkts)


class TestSeparation(unittest.TestCase):
    def test_prefixes_and_desk(self):
        r = Rig()
        r.survey_terms["aachc-cfb-wins-2026-11-28-ala-9pt5wins"] = dict(ROW)
        r.survey_terms[PLAYOFF] = dict(ROW)
        cat = r.fam.catalogue(r.survey_terms)
        self.assertEqual(set(cat), {PLAYOFF})
        res = r.desk.place_resting("aachc-cfb-wins-2026-11-28-ala-9pt5wins",
                                   "BUY", 0.10, 1.0, net_position=0.0)
        self.assertFalse(res.ok)
        self.assertIn("whitelist", res.note)


if __name__ == "__main__":
    unittest.main()
