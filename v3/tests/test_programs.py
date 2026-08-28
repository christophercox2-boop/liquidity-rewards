"""Tests for program picking and pool normalization."""

import datetime as dt
import unittest

from v3.intents import (
    BUY_LONG, BUY_SHORT, SELL_LONG, SELL_SHORT,
    capital_at_risk, intent_for, rest_side,
)
from v3.programs import (
    Program, daily_pool, daily_side_pool, is_econ, is_us_politics,
    pick_period, pool_days, program_from_period, slug_event_date, to_num,
    with_event_n,
)


def period(pid="politics_mid_1", pool=200, target=20000, df=0.2,
           status="LIVE", **kw):
    d = {"programId": pid, "rewardPool": pool, "targetSize": target,
         "discountFactor": df, "status": status}
    d.update(kw)
    return d


class TestToNum(unittest.TestCase):
    def test_shapes(self):
        self.assertEqual(to_num(3), 3.0)
        self.assertEqual(to_num("0.15"), 0.15)
        self.assertEqual(to_num({"units": 2, "nanos": 500000000}), 2.5)
        self.assertEqual(to_num({"value": "7"}), 7.0)
        self.assertEqual(to_num(None), 0.0)
        self.assertEqual(to_num("n/a"), 0.0)


class TestPickPeriod(unittest.TestCase):
    def test_politics_market_ignores_spilled_sports_programs(self):
        periods = [
            period(pid="mlb_games_ml_live", pool=99999, period="live"),
            period(pid="march_madness_futures", pool=500),
            period(pid="politics_mid_1"),
        ]
        got = pick_period(periods, "enwc-uspres-nom-rep-2028-rondes")
        self.assertEqual(got["programId"], "politics_mid_1")

    def test_market_with_only_spill_programs_has_no_paying_program(self):
        periods = [period(pid="mlb_futures", pool=1000)]
        self.assertIsNone(pick_period(periods, "enwc-uspres-nom-rep-2028-x"))

    def test_golf_picks_round_by_event_date(self):
        slug = "tec-pga-2026-08-23-somebody"
        periods = [
            period(pid="golf_pretournament", pool=5000),
            period(pid="golf_round_1", pool=1000),
            period(pid="golf_round_2", pool=1000),
        ]
        # Tournament start = event date minus 3 = Aug 20. On Aug 21 we are
        # in round 2.
        got = pick_period(periods, slug, today=dt.date(2026, 8, 21))
        self.assertEqual(got["programId"], "golf_round_2")
        got = pick_period(periods, slug, today=dt.date(2026, 8, 15))
        self.assertEqual(got["programId"], "golf_pretournament")

    def test_boosted_elections_program_beats_stale_low_tier(self):
        # 2026-08-28 (owner's screenshot): the exchange moved the MA
        # margin-of-victory brackets into "elections_boosted_high_20260827"
        # ($1,000/day) while July's $25 low program still read LIVE. The
        # picker must accept "elections" ids on politics markets and, with
        # two live programs, prefer the newest start — not API order.
        periods = [
            period(pid="elections_boosted_high_20260827", pool=1000,
                   target=10000, df=0.2, start="2026-08-27T00:00:00Z"),
            period(pid="politics_low_20260727", pool=25, target=2000,
                   df=0.1, start="2026-07-27T00:00:00Z"),
        ]
        got = pick_period(periods, "vmc-ussep-mov-ma-dem-0-2")
        self.assertEqual(got["programId"], "elections_boosted_high_20260827")
        self.assertEqual(program_from_period(got).tier, "high")

    def test_closed_program_is_not_live(self):
        p = program_from_period(period(status="STATUS_CLOSED"))
        self.assertFalse(p.is_live())
        self.assertTrue(program_from_period(period(status="LIVE")).is_live())
        self.assertTrue(program_from_period(period(status="")).is_live())


class TestPools(unittest.TestCase):
    def test_pool_splits_per_event_then_per_side(self):
        # The settled convention: per side per day = pool / event_n / 2.
        prog = with_event_n(program_from_period(period(pool=200)), 27)
        self.assertAlmostEqual(daily_pool(prog, "ewc-usp-2028-11-07-x"), 200 / 27)
        self.assertAlmostEqual(daily_side_pool(prog, "ewc-usp-2028-11-07-x"),
                               200 / 27 / 2)

    def test_politics_window_never_divides_the_pool(self):
        prog = with_event_n(program_from_period(period(
            pool=200, start="2026-08-10T00:00:00Z", end="2026-08-13T00:00:00Z")), 2)
        self.assertEqual(pool_days(prog, "ussewc-usse-ok-2026-11-03-rep"), 1.0)
        self.assertAlmostEqual(daily_pool(prog, "ussewc-usse-ok-2026-11-03-rep"), 100.0)

    def test_golf_pretournament_uses_measured_daily_flow(self):
        prog = with_event_n(program_from_period(
            period(pid="golf_pretournament", pool=5000)), 20)
        self.assertEqual(daily_pool(prog, "tec-pga-2026-08-23-somebody"), 0.03)

    def test_golf_round_pool_pays_normally(self):
        prog = with_event_n(program_from_period(
            period(pid="golf_round_1", pool=1000)), 20)
        self.assertAlmostEqual(daily_pool(prog, "tec-pga-2026-08-23-somebody"),
                               1000 / 20)

    def test_tier_parsed_from_pid(self):
        self.assertEqual(program_from_period(period(pid="pol_high_x")).tier, "high")
        self.assertEqual(program_from_period(period(pid="dedicated_2028")).tier, "")


class TestScopeAndSlugs(unittest.TestCase):
    def test_event_date_from_slug(self):
        self.assertEqual(slug_event_date("ussewc-usse-ok-2026-11-03-rep"),
                         dt.date(2026, 11, 3))
        self.assertIsNone(slug_event_date("no-date-here"))

    def test_us_politics_tokens(self):
        self.assertTrue(is_us_politics("ussewc-usse-ok-2026-11-03-rep"))
        self.assertTrue(is_us_politics("enwc-uspres-nom-dem-2028-x"))
        # tennis player code containing 'usse' as a substring must NOT match
        self.assertFalse(is_us_politics("aec-tt-russer-vs-someone"))

    def test_econ_always_excluded(self):
        self.assertTrue(is_econ("us-cpi-2026-09"))
        self.assertTrue(is_econ("fomc-decision-2026-09"))
        self.assertFalse(is_econ("ussewc-usse-ok-2026-11-03-rep"))


class TestIntents(unittest.TestCase):
    def test_rest_sides(self):
        self.assertEqual(rest_side(BUY_LONG), "BUY")
        self.assertEqual(rest_side(SELL_SHORT), "BUY")
        self.assertEqual(rest_side(BUY_SHORT), "SELL")
        self.assertEqual(rest_side(SELL_LONG), "SELL")

    def test_ask_sells_stock_when_held_else_opens_short(self):
        self.assertEqual(intent_for("SELL", net_position=10, size=5), SELL_LONG)
        self.assertEqual(intent_for("SELL", net_position=3, size=5), BUY_SHORT)

    def test_bid_never_silently_closes_a_short(self):
        self.assertEqual(intent_for("BUY", net_position=-10, size=5), BUY_LONG)
        self.assertEqual(intent_for("BUY", net_position=-10, size=5,
                                    close_short=True), SELL_SHORT)

    def test_capital_at_risk_per_side(self):
        # A bid at 5c risks 5c a share; an ask at 5c risks 95c a share.
        self.assertAlmostEqual(capital_at_risk(BUY_LONG, 0.05, 100), 5.0)
        self.assertAlmostEqual(capital_at_risk(BUY_SHORT, 0.05, 100), 95.0)
        self.assertEqual(capital_at_risk(SELL_LONG, 0.05, 100), 0.0)
        self.assertEqual(capital_at_risk(SELL_SHORT, 0.05, 100), 0.0)


if __name__ == "__main__":
    unittest.main()
