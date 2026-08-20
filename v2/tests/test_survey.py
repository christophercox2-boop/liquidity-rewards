"""The read-only scout: measures families we do not trade, touches nothing."""

import unittest

from v2.programs import pick_period, program_from_period, with_event_n
from v2.scoring import Book
from v2.survey import FAMILIES, Survey, score_row


def prog_for(pool=100.0, target=5000, df=0.2, event_n=2):
    tp = pick_period([{"programId": "p1", "rewardPool": pool,
                       "targetSize": target, "discountFactor": df,
                       "status": "LIVE"}], "mlb-2026-champ-nyy")
    return with_event_n(program_from_period(tp), event_n)


def book(bid=0.30, ask=0.32, qty=200.0):
    return Book(bids=((bid, qty), (0.02, 900000.0)),
                asks=((ask, qty), (0.98, 900000.0)), tick=0.01, fetched_at=1.0)


class FakeClient:
    def __init__(self, events=None, programs=None, books=None):
        self._events = events or {}
        self._programs = programs or {}
        self._books = books or {}
        self.calls = []

    def events_by_tag(self, tag, max_pages=30):
        self.calls.append(("events", tag))
        return self._events.get(tag, [])

    def programs(self, slugs):
        self.calls.append(("programs", tuple(slugs)))
        return {s: self._programs[s] for s in slugs if s in self._programs}

    def book(self, slug, fetched_at=None):
        self.calls.append(("book", slug))
        return self._books.get(slug, book())


class TestScoring(unittest.TestCase):
    """The discount factor cuts BOTH ways, which is why this module
    measures instead of assuming (caught here, 2026-08-19)."""

    def test_high_df_pays_to_rest_back_when_the_window_is_shallow(self):
        # competition sits at the touch and the window ends just past us:
        # a gentle df keeps our score while theirs is unchanged
        shallow = Book(bids=((0.30, 200.0), (0.29, 300.0), (0.28, 400.0)),
                       asks=((0.32, 200.0), (0.33, 300.0), (0.34, 400.0)),
                       tick=0.01, fetched_at=1.0)
        harsh = score_row("x-2026-12-31-a", prog_for(df=0.1, target=500),
                          shallow, 2, 1.0)
        gentle = score_row("x-2026-12-31-a", prog_for(df=0.9, target=500),
                           shallow, 2, 1.0)
        self.assertGreater(gentle["safe_day"], 2 * harsh["safe_day"])

    def test_high_df_backfires_when_deep_junk_sits_inside_the_window(self):
        """A big Target Size drags the window down to the penny wall that
        exists to satisfy it. At df 0.1 that wall scores nothing; at df
        0.9 it scores plenty, and it dilutes us far worse than the gentler
        discount helps. This is the trap in 'just find a high-df family'."""
        deep = book()          # 900,000 resting at 2c, the seats-book shape
        harsh = score_row("x-2026-12-31-a", prog_for(df=0.1), deep, 2, 1.0)
        gentle = score_row("x-2026-12-31-a", prog_for(df=0.9), deep, 2, 1.0)
        self.assertLess(gentle["touch_day"], harsh["touch_day"])

    def test_reports_the_terms_it_measured(self):
        r = score_row("x-2026-12-31-a",
                      prog_for(pool=250.0, target=3000, df=0.5, event_n=4),
                      book(), 4, 1.0)
        self.assertEqual((r["pool"], r["target"], r["df"], r["event_n"]),
                         (250.0, 3000, 0.5, 4))
        self.assertAlmostEqual(r["side_pool"], 250.0 / 4 / 2, places=3)
        self.assertEqual(r["spread_c"], 2.0)


class TestSurvey(unittest.TestCase):
    def ev(self, *slugs):
        return [{"title": "Champion 2026",
                 "markets": [{"slug": s} for s in slugs]}]

    def test_catalogue_walks_tags_and_drops_econ(self):
        c = FakeClient(events={"mlb": self.ev("mlb-2026-champ-nyy",
                                              "uscpi-2026-12-31-gt3pct")})
        s = Survey(clock=lambda: 100.0)
        self.assertTrue(s.refresh_catalogue(c))
        self.assertIn("mlb-2026-champ-nyy", s.catalogue)
        self.assertNotIn("uscpi-2026-12-31-gt3pct", s.catalogue)  # standing rule
        self.assertEqual(s.catalogue["mlb-2026-champ-nyy"]["event_n"], 2)

    def test_catalogue_is_cached_not_refetched_every_cycle(self):
        c = FakeClient(events={"mlb": self.ev("mlb-2026-champ-nyy")})
        s = Survey(clock=lambda: 100.0)
        s.refresh_catalogue(c, now=100.0)
        n = len(c.calls)
        self.assertFalse(s.refresh_catalogue(c, now=200.0))
        self.assertEqual(len(c.calls), n)

    def test_pools_are_learned_cheaply_before_books_are_spent(self):
        """One batched call learns 40 markets' terms; a book costs a call
        each. Doing both together took 18.6h for one sweep of 8,923
        markets — longer than the catalogue lives (measured live)."""
        slugs = [f"mlb-2026-champ-{i}" for i in range(10)]
        raw = {"timePeriods": [{"programId": "p", "rewardPool": 100,
                                "targetSize": 5000, "discountFactor": 0.9,
                                "status": "LIVE"}]}
        c = FakeClient(events={"mlb": self.ev(*slugs)},
                       programs={s: raw for s in slugs})
        s = Survey(clock=lambda: 100.0)
        s.refresh_catalogue(c, now=100.0)
        # the cheap stage covers everything at once, and fetches no books
        s.scan_terms(c, now=100.0)
        self.assertEqual(len(s.terms), 10)
        self.assertEqual([k for k, _ in c.calls].count("book"), 0)
        # the costly stage is budgeted and only touches markets that pay
        s.measure(c, now=100.0, budget=3)
        self.assertEqual(len(s.rows), 3)
        s.measure(c, now=100.0, budget=3)
        self.assertEqual(len(s.rows), 6)          # moved on, didn't redo

    def test_books_are_never_spent_on_markets_with_no_pool(self):
        slugs = ["mlb-2026-champ-a", "mlb-2026-champ-b"]
        dead = {"timePeriods": [{"programId": "p", "rewardPool": 0,
                                 "targetSize": 5000, "discountFactor": 0.9,
                                 "status": "CLOSED"}]}
        c = FakeClient(events={"mlb": self.ev(*slugs)},
                       programs={s: dead for s in slugs})
        s = Survey(clock=lambda: 100.0)
        s.refresh_catalogue(c, now=100.0)
        s.scan_terms(c, now=100.0)
        self.assertEqual(s.measure(c, now=100.0, budget=5), 0)
        self.assertEqual([k for k, _ in c.calls].count("book"), 0)

    def test_ranked_puts_the_safest_earner_first_and_hides_settling_markets(self):
        s = Survey(clock=lambda: 100.0)
        s.rows = {
            "a": {"market": "a", "safe_day": 0.10, "days_out": 300},
            "b": {"market": "b", "safe_day": 9.00, "days_out": 300},
            "c": {"market": "c", "safe_day": 99.0, "days_out": 2},   # settling
            "d": {"market": "d", "skip": "no live pool"},
        }
        got = [r["market"] for r in s.ranked()]
        self.assertEqual(got, ["b", "a"])

    def test_state_round_trips(self):
        c = FakeClient(events={"mlb": self.ev("mlb-2026-champ-nyy")})
        s = Survey(clock=lambda: 100.0)
        s.refresh_catalogue(c, now=100.0)
        again = Survey.from_dict(s.to_dict(), clock=lambda: 100.0)
        self.assertEqual(again.catalogue, s.catalogue)
        self.assertEqual(again.catalogue_at, s.catalogue_at)

    def test_no_econ_family_is_even_surveyed(self):
        joined = " ".join(t for _, tags, _ in FAMILIES for t in tags)
        for banned in ("cpi", "fed", "fomc", "inflation", "jobs", "econ"):
            self.assertNotIn(banned, joined)


if __name__ == "__main__":
    unittest.main()
