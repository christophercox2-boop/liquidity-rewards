"""Tests for the reward-scoring math.

Run:  python -m unittest discover -s v2/tests -t .
"""

import unittest

from v2.scoring import (
    Book, estimate_join, normalize_book, score_resting, window_levels,
)


def book(bids=(), asks=(), tick=0.01):
    return Book(bids=tuple(bids), asks=tuple(asks), tick=tick)


class TestNormalizeBook(unittest.TestCase):
    def test_sorts_and_cleans(self):
        b = normalize_book(
            bids_raw=[(0.05, 10), (0.07, 5), (0.0, 99), (0.06, -1)],
            asks_raw=[(0.90, 3), (0.11, 2)],
        )
        self.assertEqual(b.bids, ((0.07, 5), (0.05, 10)))
        self.assertEqual(b.asks, ((0.11, 2), (0.90, 3)))
        self.assertEqual(b.tick, 0.01)

    def test_tick_inferred_from_sub_cent_prices(self):
        b = normalize_book(bids_raw=[(0.051, 10)], asks_raw=[])
        self.assertEqual(b.tick, 0.001)


class TestWindowWalk(unittest.TestCase):
    def test_walk_stops_at_target_including_boundary_level(self):
        levels = [(0.10, 500), (0.09, 800), (0.08, 900), (0.07, 100)]
        # target 2000: 500 + 800 + 900 = 2200 >= 2000 at the third level
        self.assertEqual(window_levels(levels, 2000),
                         [(0.10, 500), (0.09, 800), (0.08, 900)])

    def test_no_target_takes_whole_side(self):
        levels = [(0.10, 5), (0.09, 5)]
        self.assertEqual(window_levels(levels, 0), levels)


class TestScoreResting(unittest.TestCase):
    def test_alone_at_best_earns_full_share(self):
        b = book(bids=[(0.76, 3), (0.58, 150), (0.02, 600000)])
        s = score_resting("BUY", 0.76, 3, b, df=0.1, target=2000,
                          daily_side_pool=6.25)
        self.assertTrue(s.earning)
        self.assertEqual(s.ticks, 0)
        self.assertAlmostEqual(s.share, 1.0, places=3)
        self.assertAlmostEqual(s.est_day, 6.25, places=2)

    def test_side_below_target_pays_nobody(self):
        b = book(bids=[(0.76, 3), (0.58, 150)])
        s = score_resting("BUY", 0.76, 3, b, df=0.1, target=2000)
        self.assertFalse(s.earning)
        self.assertIn("pays nobody", s.reason)
        self.assertEqual(s.side_total, 153)

    def test_outside_window_scores_zero(self):
        # 3000 at best fills the 2000 window at the first level; an order
        # 5 ticks back is outside it.
        b = book(bids=[(0.50, 3000), (0.45, 10)])
        s = score_resting("BUY", 0.45, 10, b, df=0.2, target=2000)
        self.assertFalse(s.earning)
        self.assertEqual(s.share, 0.0)
        self.assertIn("outside the Target Size window", s.reason)

    def test_share_diluted_by_others_at_same_level(self):
        # We are 1 of 7 contracts resting at the best price: share 1/7.
        b = book(bids=[(0.50, 7.0)])
        s = score_resting("BUY", 0.50, 1.0, b, df=0.2, target=5)
        self.assertTrue(s.earning)
        self.assertAlmostEqual(s.share, 1 / 7, places=6)

    def test_share_never_above_100pct_when_book_missing_our_order(self):
        # Book shows only 2 at our level but we claim 10 — snapshots are
        # seconds apart. Cap at 100%.
        b = book(bids=[(0.50, 2.0)])
        s = score_resting("BUY", 0.50, 10.0, b, df=0.2, target=1)
        self.assertAlmostEqual(s.share, 1.0)

    def test_df_decay_per_tick(self):
        # One tick off best with df 0.2: our score is size * 0.2.
        b = book(bids=[(0.50, 10.0), (0.49, 5.0)])
        s = score_resting("BUY", 0.49, 5.0, b, df=0.2, target=15)
        self.assertEqual(s.ticks, 1)
        ours = 5.0 * 0.2
        denom = 10.0 + ours
        self.assertAlmostEqual(s.share, ours / denom, places=6)

    def test_ask_side_scored_from_lowest_ask(self):
        b = book(asks=[(0.07, 10.0), (0.08, 5.0)])
        s = score_resting("SELL", 0.08, 5.0, b, df=0.3, target=15)
        self.assertEqual(s.ticks, 1)
        self.assertTrue(s.earning)

    def test_size_ahead_pushes_order_out_of_window(self):
        # 5000 rest at best, target 2000. Whole-level convention says the
        # level is in the window; a known queue position of 2500 ahead of
        # us says the window fills before reaching us.
        b = book(bids=[(0.50, 5000.0)])
        optimistic = score_resting("BUY", 0.50, 10.0, b, df=0.2, target=2000)
        self.assertTrue(optimistic.earning)
        known = score_resting("BUY", 0.50, 10.0, b, df=0.2, target=2000,
                              size_ahead=2500.0)
        self.assertFalse(known.earning)
        self.assertEqual(known.share, 0.0)

    def test_no_book_and_empty_side(self):
        self.assertFalse(score_resting("BUY", 0.5, 1, None, 0.2, 100).earning)
        self.assertFalse(score_resting("BUY", 0.5, 1, book(), 0.2, 100).earning)


class TestEstimateJoin(unittest.TestCase):
    def test_join_occupied_level_is_diluted_not_first_in_line(self):
        # The 1.0 earner-scan bug: joining an occupied level credited us
        # the other participants' size too, as though we were first in
        # line. Correct: our 1 contract scores 1, in a window whose score
        # sum includes the 6 sharing our level and the level behind.
        # Away from the boundary, both readings agree.
        levels = [(0.50, 6.0), (0.49, 100.0)]
        j = estimate_join("BUY", levels, tick=0.01, df=0.2, target=50,
                          price=0.50, qty=1.0)
        self.assertTrue(j.qualifies)
        self.assertTrue(j.in_window)
        self.assertTrue(j.in_window_queue)
        want = 1.0 / (7.0 + 100.0 * 0.2)
        self.assertAlmostEqual(j.share, want, places=6)
        self.assertAlmostEqual(j.share_if_queue, want, places=6)

    def test_boundary_inside_our_level_is_where_the_readings_disagree(self):
        # 6 contracts already at our level, target 5: the target is reached
        # INSIDE our level. Level reading (the acting one, per the owner):
        # the walk reaches our level, the whole level scores. Queue
        # reading: the window fills before reaching us — zero. EXP-1
        # places real orders exactly here and lets payouts decide.
        levels = [(0.50, 6.0), (0.49, 100.0)]
        j = estimate_join("BUY", levels, tick=0.01, df=0.2, target=5,
                          price=0.50, qty=1000.0)
        self.assertTrue(j.qualifies)
        self.assertTrue(j.in_window)
        self.assertAlmostEqual(j.share, 1000.0 / 1006.0, places=6)
        self.assertFalse(j.in_window_queue)
        self.assertEqual(j.share_if_queue, 0.0)

    def test_documented_example_second_best_scores_zero_under_both_readings(self):
        # Straight from the exchange docs: target 20,000 with 25,000 at the
        # best price — an order at the second-best price scores zero. The
        # two readings agree here; only the mid-level boundary is open.
        levels = [(0.50, 25000.0), (0.49, 10.0)]
        j = estimate_join("BUY", levels, tick=0.01, df=0.2, target=20000,
                          price=0.49, qty=10.0)
        self.assertTrue(j.qualifies)
        self.assertFalse(j.in_window)
        self.assertFalse(j.in_window_queue)
        self.assertEqual(j.share, 0.0)
        self.assertEqual(j.share_if_queue, 0.0)

    def test_join_full_level_dilutes_under_level_reading_zero_under_queue(self):
        # 5000 already rest at best against a 2000 target. Level reading:
        # the level is the window, we join it heavily diluted. Queue
        # reading: everyone there is ahead of us and the window fills
        # before reaching us. Another EXP-1 disagreement setup.
        levels = [(0.50, 5000.0)]
        j = estimate_join("BUY", levels, tick=0.01, df=0.2, target=2000,
                          price=0.50, qty=100.0)
        self.assertTrue(j.qualifies)
        self.assertTrue(j.in_window)
        self.assertAlmostEqual(j.share, 100.0 / 5100.0, places=6)
        self.assertFalse(j.in_window_queue)
        self.assertEqual(j.share_if_queue, 0.0)

    def test_improving_the_touch_beats_joining_a_full_level(self):
        levels = [(0.50, 5000.0)]
        j = estimate_join("BUY", levels, tick=0.01, df=0.2, target=2000,
                          price=0.51, qty=100.0)
        self.assertTrue(j.in_window)
        self.assertEqual(j.ticks, 0)  # we are the new best
        self.assertGreater(j.share, 0.0)

    def test_side_short_of_target_reports_gap(self):
        levels = [(0.50, 300.0)]
        j = estimate_join("BUY", levels, tick=0.01, df=0.2, target=2000,
                          price=0.50, qty=200.0)
        self.assertFalse(j.qualifies)
        self.assertEqual(j.gap, 1500.0)
        self.assertEqual(j.share, 0.0)

    def test_qualifying_a_dead_side_takes_most_of_it(self):
        # We bring 1800 to a side holding 300 against a 2000 target: the
        # side now qualifies and we hold the lion's share.
        levels = [(0.50, 300.0)]
        j = estimate_join("BUY", levels, tick=0.01, df=0.2, target=2000,
                          price=0.50, qty=1800.0)
        self.assertTrue(j.qualifies)
        self.assertAlmostEqual(j.share, 1800.0 / 2100.0, places=6)

    def test_empty_side(self):
        j = estimate_join("BUY", [], tick=0.01, df=0.2, target=100,
                          price=0.50, qty=150.0)
        self.assertTrue(j.qualifies)
        self.assertEqual(j.share, 1.0)
        short = estimate_join("BUY", [], tick=0.01, df=0.2, target=100,
                              price=0.50, qty=50.0)
        self.assertFalse(short.qualifies)
        self.assertEqual(short.gap, 50.0)

    def test_ask_side_ordering(self):
        # On the ask side "closer to best" means LOWER prices.
        levels = [(0.07, 10.0), (0.09, 5.0)]
        j = estimate_join("SELL", levels, tick=0.01, df=0.5, target=20,
                          price=0.08, qty=5.0)
        self.assertEqual(j.ticks, 1)
        ours = 5.0 * 0.5
        denom = 10.0 + ours + 5.0 * 0.5 ** 2
        self.assertAlmostEqual(j.share, ours / denom, places=6)


if __name__ == "__main__":
    unittest.main()
