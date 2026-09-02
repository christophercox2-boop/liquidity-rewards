"""The daily ladder record (owner yes, 2026-09-02).

After cfb's week 1 the state file's touch-and-totals could not show
WHAT changed on the books that had paid $4-8/day. Once a day the full
ladders of every earning market — and of every market that earned in
the last week, so a drop has its after picture — go to data/ladders/.
"""

import calendar
import unittest

from v3.family import FamilyOrder
from v3.intents import BUY_LONG
from v3.main import (LADDER_LEVELS, ladder_due, ladder_snapshot,
                     prune_ladder_seen)
from v3.scoring import Book
from v3.tests.test_family import A, Rig, politics_book


def rig_with(book, share=0.5):
    r = Rig()
    r.cache.put(A, book)
    r.fam.orders["x"] = FamilyOrder(
        id="x", market=A, side="BUY", price=0.44, qty=5.0,
        intent=BUY_LONG, placed_ts=r.now, purpose="earn",
        live_share=share, live_est=share * 2.0)
    return r


class TestLadderSnapshot(unittest.TestCase):
    def test_an_earning_market_carries_its_ladder_and_our_orders(self):
        r = rig_with(politics_book(1_000_000.0))
        snap, earning = ladder_snapshot(r.fam, r.now)
        self.assertEqual(earning, {A})
        lad = snap[A]
        self.assertEqual(lad["bids"][0], [0.44, 20.0])   # the touch, whole
        self.assertEqual(lad["asks"][0], [0.47, 20.0])
        self.assertEqual(lad["bid_total"], 60020)          # the wall counts
        self.assertEqual(lad["ours"], [["BUY", 0.44, 5.0, "earn", 0.5, 1.0]])
        self.assertEqual(lad["bids_more"], 0)

    def test_a_market_that_stopped_earning_is_kept_while_recent(self):
        r = rig_with(politics_book(1_000_000.0), share=0.0)
        r.fam.orders["x"].live_est = 0.0
        snap, earning = ladder_snapshot(r.fam, r.now)
        self.assertEqual((snap, earning), ({}, set()))
        # ...unless it earned in the last week: then its after picture
        # is exactly what the record is for
        snap, _ = ladder_snapshot(r.fam, r.now, extra={A: "2026-09-01"})
        self.assertIn(A, snap)
        self.assertEqual(snap[A]["ours"][0][4], 0.0)

    def test_a_stale_book_is_left_out_rather_than_shown_as_current(self):
        r = rig_with(politics_book(1_000_000.0))
        snap, earning = ladder_snapshot(r.fam, r.now + 3600.0)
        self.assertEqual(snap, {})
        self.assertEqual(earning, {A})       # still earning, just unseen

    def test_deep_ladders_keep_the_touch_end_and_the_wall_end(self):
        levels = tuple((round(0.60 - i * 0.01, 2), 10.0 + i)
                       for i in range(40))
        book = Book(bids=levels, asks=((0.61, 5.0),), tick=0.01,
                    fetched_at=1_000_000.0)
        r = rig_with(book)
        snap, _ = ladder_snapshot(r.fam, r.now)
        bids = snap[A]["bids"]
        self.assertEqual(len(bids), LADDER_LEVELS + 4)
        self.assertEqual(bids[0][0], 0.60)                 # the touch
        self.assertEqual(bids[-1][0], 0.21)                # the deepest level
        self.assertEqual(snap[A]["bids_more"], 40 - LADDER_LEVELS - 4)
        self.assertEqual(snap[A]["bid_total"], sum(10 + i for i in range(40)))


class TestLadderClock(unittest.TestCase):
    def test_once_a_day_after_the_hour(self):
        t = calendar.timegm((2026, 9, 2, 15, 59, 0, 0, 0, 0))
        self.assertIsNone(ladder_due(t, ""))                     # before 16Z
        self.assertEqual(ladder_due(t + 120, ""), "2026-09-02")
        self.assertIsNone(ladder_due(t + 120, "2026-09-02"))     # written
        self.assertIsNone(ladder_due(t + 6 * 3600, "2026-09-02"))
        self.assertEqual(ladder_due(t + 86400 + 120, "2026-09-02"),
                         "2026-09-03")

    def test_recent_earners_are_forgotten_after_a_week(self):
        seen = {"old": "2026-08-25", "week": "2026-08-26", "new": "2026-09-01"}
        kept = prune_ladder_seen(seen, "2026-09-02")
        self.assertEqual(set(kept), {"week", "new"})


if __name__ == "__main__":
    unittest.main()
