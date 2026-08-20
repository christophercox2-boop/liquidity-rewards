"""Tests for the terms store: seeding, change detection, one source of truth."""

import unittest

from v3.terms import TermsStore


def raw(pid="politics_mid_1", pool=200, target=20000, df=0.2, status="LIVE"):
    return {"timePeriods": [{"programId": pid, "rewardPool": pool,
                             "targetSize": target, "discountFactor": df,
                             "status": status}]}


SLUG = "ussewc-usse-ok-2026-11-03-rep"


class TestTermsStore(unittest.TestCase):
    def test_first_sighting_seeds_silently_but_is_recorded(self):
        rows = []
        st = TermsStore(history_sink=rows.append)
        changes = st.refresh({SLUG: raw()}, {SLUG: 2}, now=100.0)
        self.assertEqual(changes, [])          # nothing to compare against
        self.assertEqual(st.get(SLUG).pool, 200)
        self.assertEqual(st.get(SLUG).event_n, 2)
        self.assertEqual(st.seeded_at[SLUG], 100.0)
        self.assertEqual(rows[0]["why"], "seed")

    def test_pool_cut_is_a_change_event(self):
        # The failure that cost half a day's income unexplained: the pool
        # dropped from $500 to $200 and nothing noticed.
        rows = []
        st = TermsStore(history_sink=rows.append)
        st.refresh({SLUG: raw(pool=500)}, {SLUG: 2}, now=100.0)
        changes = st.refresh({SLUG: raw(pool=200)}, {SLUG: 2}, now=200.0)
        self.assertEqual(len(changes), 1)
        c = changes[0]
        self.assertEqual((c.field, c.old, c.new), ("pool", 500, 200))
        self.assertEqual(rows[-1]["why"], "change")

    def test_all_programs_closing_reports_program_gone(self):
        st = TermsStore()
        st.refresh({SLUG: raw()}, {SLUG: 2}, now=100.0)
        # only a spilled global program remains -> no paying program
        gone = {"timePeriods": [{"programId": "mlb_futures", "rewardPool": 1000,
                                 "targetSize": 100, "discountFactor": 0.2,
                                 "status": "LIVE"}]}
        changes = st.refresh({SLUG: gone}, {SLUG: 2}, now=200.0)
        self.assertEqual(changes[0].field, "program_gone")
        self.assertIsNone(st.get(SLUG))

    def test_program_returning_is_reported_not_reseeded(self):
        st = TermsStore()
        st.refresh({SLUG: raw()}, {SLUG: 2}, now=100.0)
        st.refresh({SLUG: {"timePeriods": []}}, {SLUG: 2}, now=200.0)
        changes = st.refresh({SLUG: raw()}, {SLUG: 2}, now=300.0)
        self.assertEqual(changes[0].field, "program_new")

    def test_event_divisor_change_is_watched(self):
        # A new sibling market halves everyone's per-market pool.
        st = TermsStore()
        st.refresh({SLUG: raw()}, {SLUG: 2}, now=100.0)
        changes = st.refresh({SLUG: raw()}, {SLUG: 3}, now=200.0)
        self.assertEqual([(c.field, c.old, c.new) for c in changes],
                         [("event_n", 2, 3)])

    def test_age_unseen_market_is_infinitely_stale(self):
        st = TermsStore()
        self.assertEqual(st.age("never-seen", now=1000.0), float("inf"))
        st.refresh({SLUG: raw()}, {}, now=900.0)
        self.assertAlmostEqual(st.age(SLUG, now=1000.0), 100.0)

    def test_roundtrip(self):
        st = TermsStore()
        st.refresh({SLUG: raw()}, {SLUG: 2}, now=100.0)
        st2 = TermsStore.from_dict(st.to_dict())
        self.assertEqual(st2.get(SLUG), st.get(SLUG))
        self.assertEqual(st2.seeded_at, st.seeded_at)
        # a re-seen market diffs against the restored copy, not a reseed
        changes = st2.refresh({SLUG: raw(pool=100)}, {SLUG: 2}, now=200.0)
        self.assertEqual(changes[0].field, "pool")


if __name__ == "__main__":
    unittest.main()
