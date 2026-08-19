"""Tests for the seat-ladder fair model, including against the real table."""

import datetime as dt
import unittest
from pathlib import Path

from v2.silver import (
    SENATE_GOP_NOT_UP, SilverFairs, parse_official_dist,
    parse_official_topline, parse_races, rung_fair, seat_pmf,
)

REAL_CSV = Path(__file__).resolve().parent.parent.parent / "data" / "silver_senate_races.csv"
FIX = Path(__file__).resolve().parent / "fixtures"
OFFICIAL_TOP = (FIX / "silver_official_topline.csv").read_text()
OFFICIAL_DIST = (FIX / "silver_official_dist.csv").read_text()
RUN_TS = dt.datetime.fromisoformat("2026-08-10T11:31:32-04:00").timestamp()


class TestSeatPmf(unittest.TestCase):
    def test_two_coins_exact(self):
        pmf = seat_pmf([0.5, 0.5], not_up=10, rho=0.0)
        self.assertAlmostEqual(pmf[10], 0.25)
        self.assertAlmostEqual(pmf[11], 0.50)
        self.assertAlmostEqual(pmf[12], 0.25)
        self.assertAlmostEqual(sum(pmf.values()), 1.0)

    def test_certain_races_just_shift(self):
        pmf = seat_pmf([1.0, 1.0, 0.0], not_up=31, rho=0.0)
        self.assertAlmostEqual(pmf[33], 1.0)

    def test_rungs_read_off_the_distribution(self):
        pmf = seat_pmf([0.5, 0.5], not_up=45, rho=0.0)   # mass on 45/46/47
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


class TestOfficialParse(unittest.TestCase):
    def test_dist_converts_democratic_seats_and_normalizes(self):
        dist = parse_official_dist(OFFICIAL_DIST)
        self.assertEqual(sorted(dist), ["house", "senate"])
        for chamber in dist:
            self.assertEqual(sorted(dist[chamber]), ["classic", "deluxe", "lite"])
            for pmf in dist[chamber].values():
                self.assertAlmostEqual(sum(pmf.values()), 1.0, places=9)
        # hand-checked against the embed: Deluxe Senate, GOP = 100 - D
        dx = dist["senate"]["deluxe"]
        self.assertAlmostEqual(rung_fair(dx, "lte45"), 0.0681, places=4)
        self.assertAlmostEqual(rung_fair(dx, "48"), 0.1641, places=4)
        self.assertAlmostEqual(rung_fair(dx, "gte57"), 0.0009, places=4)
        # and the House in R seats (435 - D)
        self.assertAlmostEqual(rung_fair(dist["house"]["deluxe"], "gte215"),
                               0.1844, places=4)

    def test_topline_metadata(self):
        top = parse_official_topline(OFFICIAL_TOP)
        self.assertEqual(top["date"], "2026-08-10")
        self.assertEqual(top["run"], "2026-08-10T11:31:32-04:00")
        self.assertAlmostEqual(top["d_control"]["senate"]["deluxe"], 0.5796875)
        self.assertAlmostEqual(top["d_control"]["house"]["lite"], 0.848125)

    def test_garbage_is_empty_not_wrong(self):
        self.assertEqual(parse_official_dist("model,chamber,seats,prob\n"), {})
        self.assertEqual(parse_official_topline("nope\n1,2"), {})
        # a flavor missing half its mass is dropped, not served
        broken = "model,chamber,seats,prob\nclassic,Senate,50,40.0\n"
        self.assertEqual(parse_official_dist(broken), {})


class TestOfficialFairs(unittest.TestCase):
    def _fairs(self, now):
        t = [now]
        s = SilverFairs(clock=lambda: t[0])
        self.assertTrue(s.load(REAL_CSV.read_text(), now=now))
        self.assertTrue(s.load_official(OFFICIAL_TOP, OFFICIAL_DIST, now=now))
        return s, t

    def test_control_crosscheck_passes_on_real_data(self):
        s, _ = self._fairs(RUN_TS + 3600)
        self.assertEqual(s.official_note, "")
        # official deluxe beats the copula for the headline number
        self.assertAlmostEqual(s.gop_control(), 0.4203, places=3)

    def test_band_is_the_flavor_spread_when_fresh(self):
        s, _ = self._fairs(RUN_TS + 86400)
        lo, hi = s.fair_range("scc-senate-gop-2026-11-03-48")
        self.assertAlmostEqual(lo, 0.1028, places=4)   # lite
        self.assertAlmostEqual(hi, 0.1641, places=4)   # deluxe
        self.assertAlmostEqual(s.fair("scc-senate-gop-2026-11-03-48"),
                               0.1641, places=4)       # center = deluxe
        fl = s.flavors_fair("scc-senate-gop-2026-11-03-48")
        self.assertEqual(sorted(fl), ["classic", "deluxe", "lite"])

    def test_house_ladder_is_priced_now(self):
        s, _ = self._fairs(RUN_TS + 86400)
        lo, hi = s.fair_range("scc-hrep-rep-2026-11-03-gte215")
        self.assertLess(lo, hi)
        self.assertAlmostEqual(s.fair("scc-hrep-rep-2026-11-03-gte215"),
                               0.1844, places=4)
        # whole-ladder sanity: gte rungs must be monotone decreasing
        vals = [s.fair(f"scc-hrep-rep-2026-11-03-gte{n}")
                for n in (205, 215, 225, 235)]
        self.assertEqual(vals, sorted(vals, reverse=True))

    def test_stale_run_widens_with_the_copula(self):
        s, t = self._fairs(RUN_TS + 86400)
        fresh = s.fair_range("scc-senate-gop-2026-11-03-48")
        t[0] = RUN_TS + 8 * 86400              # run is now 8 days old
        stale = s.fair_range("scc-senate-gop-2026-11-03-48")
        cop = [rung_fair(p, "48") for p in (s.pmf_lo, s.pmf, s.pmf_hi)]
        self.assertLessEqual(stale[0], min(fresh[0], min(cop)))
        self.assertGreaterEqual(stale[1], max(fresh[1], max(cop)))
        # the house band has no copula to widen with; it stays the spread
        self.assertEqual(s.fair_range("scc-hrep-rep-2026-11-03-gte215"),
                         self._fairs(RUN_TS + 86400)[0]
                         .fair_range("scc-hrep-rep-2026-11-03-gte215"))

    def test_without_official_the_copula_still_prices_senate(self):
        s = SilverFairs(clock=lambda: 1.0)
        self.assertTrue(s.load(REAL_CSV.read_text(), now=1.0))
        self.assertIsNotNone(s.fair_range("scc-senate-gop-2026-11-03-50"))
        self.assertIsNone(s.fair_range("scc-hrep-rep-2026-11-03-gte215"))


if __name__ == "__main__":
    unittest.main()
