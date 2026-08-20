"""Tests for the book cache: age discipline, rotation, WS interlock."""

import unittest

from v3.books import BookCache, ws_priority
from v3.scoring import Book


def book(bid=0.44, ask=0.46, at=0.0):
    return Book(bids=((bid, 100.0),), asks=((ask, 50.0),), tick=0.01, fetched_at=at)


class TestAgeDiscipline(unittest.TestCase):
    def test_fresh_respects_tolerance_and_any_age_does_not(self):
        c = BookCache()
        c.put("m", book(at=1000.0))
        self.assertIsNotNone(c.fresh("m", max_age=60, now=1030.0))
        self.assertIsNone(c.fresh("m", max_age=60, now=1100.0))
        self.assertIsNotNone(c.any_age("m"))
        self.assertIsNone(c.fresh("never", max_age=60, now=0.0))

    def test_coverage_is_the_estimators_quorum(self):
        c = BookCache()
        c.put("a", book(at=1000.0))
        c.put("b", book(at=100.0))
        self.assertAlmostEqual(c.coverage(["a", "b"], max_age=60, now=1030.0), 0.5)
        self.assertEqual(c.coverage([], max_age=60, now=0.0), 1.0)


class TestRotation(unittest.TestCase):
    def test_ws_fresh_books_are_not_refetched(self):
        c = BookCache()
        c.put("streamed", book(at=995.0))   # 5s old — the stream owns it
        c.put("stale", book(at=0.0))
        picks = c.pick_refresh(["streamed", "stale"], priority=[], now=1000.0)
        self.assertEqual(picks, ["stale"])

    def test_priority_markets_lead_but_cannot_starve_the_rotation(self):
        c = BookCache()
        universe = [f"p{i}" for i in range(30)] + [f"r{i}" for i in range(30)]
        picks = c.pick_refresh(universe, priority=[f"p{i}" for i in range(30)],
                               now=1000.0, budget=28)
        self.assertEqual(len(picks), 28)
        self.assertEqual(sum(1 for s in picks if s.startswith("p")), 22)
        self.assertEqual(sum(1 for s in picks if s.startswith("r")), 6)

    def test_churny_books_age_faster(self):
        c = BookCache()
        # same real age; one book keeps moving, the other sat still
        c.put("quiet", book(at=0.0))
        c.put("quiet", book(at=100.0))       # identical top levels -> volatility decays
        c.put("busy", book(bid=0.40, at=0.0))
        c.put("busy", book(bid=0.41, at=100.0))  # top level moved -> volatility rises
        picks = c.pick_refresh(["quiet", "busy"], priority=[], now=200.0, budget=1)
        self.assertEqual(picks, ["busy"])

    def test_prune_drops_untracked_markets(self):
        c = BookCache()
        c.put("keep", book())
        c.put("gone", book())
        c.prune(["keep"])
        self.assertIsNone(c.any_age("gone"))
        self.assertIsNotNone(c.any_age("keep"))


class TestWsPriority(unittest.TestCase):
    def test_held_and_defended_subscribe_first_under_the_cap(self):
        universe = [f"m{i}" for i in range(300)]
        subs = ws_priority(slugs_with_orders=["m250"], defended=["m299"],
                           universe=universe, cap=200)
        self.assertEqual(len(subs), 200)
        self.assertIn("m250", subs[:2])
        self.assertIn("m299", subs[:2])


if __name__ == "__main__":
    unittest.main()
