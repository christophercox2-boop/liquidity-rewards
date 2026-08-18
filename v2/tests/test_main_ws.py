"""Tests for the stream's frame parsing and main's pure helpers."""

import json
import unittest

from v2.books import BookCache
from v2.main import politics_event_sizes, touch_snapshot
from v2.scoring import Book
from v2.ws import Stream


class TestApplyFrame(unittest.TestCase):
    def stream(self):
        cache = BookCache()
        return Stream(cache, lambda: [], "kid", ""), cache

    def test_book_frame_lands_in_the_cache_normalized(self):
        s, cache = self.stream()
        frame = json.dumps({"marketData": {
            "marketSlug": "scc-x",
            "bids": [{"px": "0.44", "qty": "100"}, {"px": "0.45", "qty": "5"}],
            "offers": [{"px": {"value": "0.46"}, "qty": 7}],
        }})
        self.assertEqual(s.apply_frame(frame), "scc-x")
        b = cache.any_age("scc-x")
        self.assertEqual(b.bids[0], (0.45, 5.0))    # sorted best-first
        self.assertEqual(b.asks[0], (0.46, 7.0))    # protobuf px parsed
        self.assertGreater(s.status["last_msg"], 0)

    def test_non_book_and_garbage_frames_never_raise(self):
        s, cache = self.stream()
        self.assertIsNone(s.apply_frame(json.dumps({"subscribed": True})))
        self.assertIsNone(s.apply_frame(b"\x00 not json"))
        self.assertIsNone(cache.any_age("scc-x"))


class StubEventsClient:
    def events_by_tag(self, tag, max_pages=30):
        if tag != "politics":
            return []
        return [
            {"markets": [{"slug": "race-a-dem"}, {"slug": "race-a-rep"},
                         {"slug": "race-a-old", "closed": True}]},
            # a race modeled as two single-market events: the prefix
            # grouping must still count both
            {"markets": [{"slug": "nom-2028-alpha"}]},
            {"markets": [{"slug": "nom-2028-beta"}]},
        ]


class TestEventSizes(unittest.TestCase):
    def test_tag_sizes_widened_by_race_grouping(self):
        sizes = politics_event_sizes(StubEventsClient())
        self.assertEqual(sizes["race-a-dem"], 2)     # closed sibling not counted
        self.assertEqual(sizes["nom-2028-alpha"], 2)  # prefix group beats event size 1
        self.assertEqual(sizes["nom-2028-beta"], 2)


class TestTouchSnapshot(unittest.TestCase):
    def test_publishes_best_prices_totals_and_age(self):
        c = BookCache()
        c.put("m", Book(bids=((0.44, 100.0), (0.40, 50.0)), asks=((0.46, 7.0),),
                        tick=0.01, fetched_at=1000.0))
        c.put("old", Book(bids=((0.10, 1.0),), asks=(), tick=0.01, fetched_at=0.0))
        snap = touch_snapshot(c, ["m", "old", "never"], now=1030.0)
        self.assertEqual(snap["m"], [44.0, 46.0, 150, 7, 30])
        self.assertNotIn("old", snap)    # older than the 600s publish limit
        self.assertNotIn("never", snap)


if __name__ == "__main__":
    unittest.main()
