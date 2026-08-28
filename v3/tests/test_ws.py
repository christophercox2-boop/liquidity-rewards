"""The book stream writes the same cache the REST rotation does."""

import json
import unittest

from v3.books import BookCache, ws_priority
from v3.ws import Stream


class TestStream(unittest.TestCase):
    def test_frame_lands_in_the_cache_normalized(self):
        cache = BookCache()
        s = Stream(cache, lambda: ["m-1"], "k", "c2VjcmV0c2VjcmV0c2VjcmV0c2VjcmV0c2Vjcg==")
        frame = json.dumps({"marketData": {
            "marketSlug": "m-1",
            "bids": [{"px": {"value": "0.44"}, "qty": 20},
                     {"px": {"value": "0.02"}, "qty": 60000}],
            "offers": [{"px": {"value": "0.47"}, "qty": 20}],
        }})
        self.assertEqual(s.apply_frame(frame), "m-1")
        b = cache.any_age("m-1")
        self.assertEqual(b.bids[0], (0.44, 20.0))
        self.assertEqual(b.asks[0], (0.47, 20.0))
        self.assertEqual(s.apply_frame("not json"), None)   # never kills the socket
        self.assertEqual(s.apply_frame(json.dumps({"x": 1})), None)

    def test_frame_shape_sampler_records_what_arrives(self):
        # owner yes, 2026-08-28: the health line shows frames arriving
        # with zero book writes — record every distinct frame shape
        # with a count and one truncated sample, so apply_frame gets
        # fixed from evidence instead of guesses.
        cache = BookCache()
        s = Stream(cache, lambda: ["m-1"], "k", "c2VjcmV0c2VjcmV0c2VjcmV0c2VjcmV0c2Vjcg==")
        s.apply_frame(json.dumps({"marketDataLite": {
            "marketSlug": "m-1", "bestBid": {"value": "0.44"}}}))
        s.apply_frame(json.dumps({"marketDataLite": {
            "marketSlug": "m-1", "bestBid": {"value": "0.45"}}}))
        s.apply_frame(json.dumps({"mysteryBook": {"slug": "m-1",
                                                  "levels": []}}))
        s.apply_frame("not json")                    # never sampled, never fatal
        sigs = list(s.frame_shapes)
        self.assertEqual(len(sigs), 2)
        lite = next(k for k in sigs if "marketDataLite" in k)
        self.assertEqual(s.frame_shapes[lite]["n"], 2)
        odd = next(k for k in sigs if "mysteryBook" in k)
        self.assertIn("mysteryBook", odd)
        self.assertIn("levels", odd)                 # nested keys in the signature
        self.assertIn("mysteryBook", s.frame_shapes[odd]["sample"])

    def test_priority_puts_held_markets_first_under_the_cap(self):
        uni = [f"m-{i}" for i in range(300)]
        out = ws_priority(["m-250"], ["m-299"], uni)
        self.assertEqual(out[0], "m-250")
        self.assertEqual(out[1], "m-299")
        self.assertEqual(len(out), 200)
