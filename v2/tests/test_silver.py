"""Tests for the seat-ladder fair model, including against the real table."""

import unittest
from pathlib import Path

from v2.silver import (
    SENATE_GOP_NOT_UP, SilverFairs, parse_races, rung_fair, seat_pmf,
)

REAL_CSV = Path(__file__).resolve().parent.parent.parent / "data" / "silver_senate_races.csv"


class TestSeatPmf(unittest.TestCase):
    def test_two_coins_exact(self):
        pmf = seat_pmf([0.5, 0.5], not_up=10)
        self.assertAlmostEqual(pmf[10], 0.25)
        self.assertAlmostEqual(pmf[11], 0.50)
        self.assertAlmostEqual(pmf[12], 0.25)
        self.assertAlmostEqual(sum(pmf.values()), 1.0)

    def test_certain_races_just_shift(self):
        pmf = seat_pmf([1.0, 1.0, 0.0], not_up=31)
        self.assertAlmostEqual(pmf[33], 1.0)

    def test_rungs_read_off_the_distribution(self):
        pmf = seat_pmf([0.5, 0.5], not_up=45)   # mass on 45/46/47
        self.assertAlmostEqual(rung_fair(pmf, "46"), 0.50)
        self.assertAlmostEqual(rung_fair(pmf, "gte46"), 0.75)
        self.assertAlmostEqual(rung_fair(pmf, "lte45"), 0.25)
        self.assertEqual(rung_fair(pmf, "weird"), None)


class TestRealTable(unittest.TestCase):
    def test_parses_and_prices_sanely(self):
        s = SilverFairs()
        self.assertTrue(s.load(REAL_CSV.read_text(), now=1.0))
        self.assertEqual(len(s.races), 35)      # 33 Class II + OH & FL specials
        self.assertEqual(s.note, "")            # matches the expected count
        self.assertAlmostEqual(sum(s.pmf.values()), 1.0, places=9)
        # every rung of the real ladder gets a value, they sum to 1
        rungs = ["lte45"] + [str(n) for n in range(46, 57)] + ["gte57"]
        vals = [s.fair(f"scc-senate-gop-2026-11-03-{r}") for r in rungs]
        self.assertTrue(all(v is not None for v in vals))
        self.assertAlmostEqual(sum(vals), 1.0, places=9)
        # sanity band only: as of 2026-08-18 the table implies ~0.38 —
        # anything wildly outside means the holdover constant or parse broke
        control = s.gop_control()
        self.assertGreater(control, 0.15)
        self.assertLess(control, 0.85)
        # house rungs are not priced by this model
        self.assertIsNone(s.fair("scc-hrep-rep-2026-11-03-gte210"))

    def test_missing_race_is_flagged_not_silent(self):
        text = REAL_CSV.read_text()
        lines = text.splitlines()
        s = SilverFairs()
        self.assertTrue(s.load("\n".join(lines[:-1]), now=1.0))  # drop one race
        self.assertIn("34 races", s.note)


if __name__ == "__main__":
    unittest.main()
