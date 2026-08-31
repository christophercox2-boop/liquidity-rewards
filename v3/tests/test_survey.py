"""The survey exists because pool size is the wrong question.

Owner, 2026-08-31: "We're getting a high share with low order size
(risk). So that wouldn't quite be an apples to apples comparison." A
$50 probe would have flattered NBA, where $50 buys far more shares than
in a 30c politics market. The measure is share of a side per dollar at
risk, priced at the size we actually use.
"""

import unittest

from v3.programs import Program
from v3.scoring import Book
from v3.survey import kind_of, probe_side, summarise, to_csv


def book(bids, asks, tick=0.01):
    return Book(bids=tuple(bids), asks=tuple(asks), tick=tick,
                fetched_at=1000.0)


class TestKind(unittest.TestCase):
    def test_the_kind_is_everything_before_the_date(self):
        self.assertEqual(kind_of("aachc-cfb-wins-2026-11-28-txst-5pt5wins"),
                         "aachc-cfb-wins")
        self.assertEqual(kind_of("tec-nba-westconf-2027-05-29-w-uta"),
                         "tec-nba-westconf")
        self.assertEqual(kind_of("aqc-nfl-2027-01-10-playoffq-ari"), "aqc-nfl")

    def test_a_slug_with_no_date_is_its_own_kind(self):
        self.assertEqual(kind_of("enwc-uspres-nom-rep-elomus"),
                         "enwc-uspres-nom-rep-elomus")


class TestProbe(unittest.TestCase):
    """A thin touch behind a qualifying wall is the cfb shape; a fat
    touch is NBA's, however rich the pool."""

    def test_a_thin_touch_behind_a_wall_takes_a_real_share(self):
        # 6 shares at the touch, a 20k wall out at 99c carrying the side
        # over Target Size — one share should be worth a large slice
        b = book(bids=[(0.30, 6.0), (0.29, 4.0), (0.01, 20000.0)], asks=[])
        prog = Program(pool=100.0, target=7500.0, df=0.25, event_n=2)
        p = probe_side(b, prog, "BUY", side_pool=25.0)
        self.assertTrue(p.qualifies, p.note)
        self.assertEqual(p.touch_size, 6.0)
        self.assertGreater(p.share, 0.05)
        # and it cost 30 cents to get it
        self.assertAlmostEqual(p.risk_usd, 0.30, places=4)
        self.assertGreater(p.share_per_dollar, 0.15)

    def test_a_fat_touch_takes_almost_nothing_however_rich_the_pool(self):
        # NBA's shape: the same probe against 500k resting at the touch
        b = book(bids=[(0.30, 500_000.0)], asks=[])
        prog = Program(pool=200.0, target=10000.0, df=0.25, event_n=1)
        p = probe_side(b, prog, "BUY", side_pool=100.0)
        self.assertTrue(p.qualifies)
        self.assertLess(p.share, 0.001)
        # the pool is FOUR TIMES richer and the order is worth far less
        self.assertLess(p.est_day, 0.25)

    def test_a_side_under_target_size_pays_nobody(self):
        b = book(bids=[(0.30, 6.0)], asks=[])
        prog = Program(pool=100.0, target=7500.0, df=0.25, event_n=1)
        p = probe_side(b, prog, "BUY", side_pool=50.0)
        self.assertFalse(p.qualifies)
        self.assertEqual(p.share, 0.0)
        self.assertEqual(p.est_day, 0.0)
        self.assertIn("Target Size", p.note)

    def test_an_empty_side_is_reported_not_crashed(self):
        p = probe_side(book(bids=[], asks=[(0.5, 3.0)]), Program(pool=1.0, target=1.0, df=0.5),
                       "BUY", side_pool=1.0)
        self.assertEqual(p.note, "side is empty")
        self.assertEqual(p.share_per_dollar, 0.0)

    def test_near_size_counts_only_what_scores(self):
        b = book(bids=[(0.30, 5.0), (0.29, 7.0), (0.10, 900.0)], asks=[])
        p = probe_side(b, Program(pool=10.0, target=1.0, df=0.5, event_n=1),
                       "BUY", side_pool=5.0)
        self.assertEqual(p.touch_size, 5.0)
        self.assertEqual(p.near_size, 12.0)      # the 10c pile is far back
        self.assertEqual(p.total_size, 912.0)


class TestReport(unittest.TestCase):
    def test_kinds_rank_by_share_per_dollar_not_by_pool(self):
        rows = [
            {"kind": "fat-pool", "qualifies": 1, "share_pct": 0.02,
             "est_day_usd": 0.01, "share_per_dollar": 0.06},
            {"kind": "thin-touch", "qualifies": 1, "share_pct": 13.0,
             "est_day_usd": 0.98, "share_per_dollar": 31.0},
        ]
        out = summarise(rows)["kinds"]
        self.assertEqual(out[0]["kind"], "thin-touch")

    def test_csv_has_a_header_and_survives_commas(self):
        b = book(bids=[(0.30, 6.0)], asks=[])
        r = probe_side(b, Program(pool=1.0, target=1.0, df=0.5, event_n=1),
                       "BUY", 1.0).row("a,b", "kind")
        text = to_csv([r])
        self.assertTrue(text.startswith("market,kind,side,"))
        self.assertEqual(len(text.strip().split("\n")), 2)
        self.assertNotIn("a,b", text)            # the comma was neutralised


if __name__ == "__main__":
    unittest.main()
