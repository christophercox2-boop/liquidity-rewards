"""Tests for the fill model: hazards from touch history, calibration."""

import unittest

from v2.fillmodel import DAY_S, FillModel, family_of

SEN = "scc-senate-gop-2026-11-03-50"


class TestFamilies(unittest.TestCase):
    def test_families(self):
        self.assertEqual(family_of(SEN), "senate-seats")
        self.assertEqual(family_of("scc-hrep-rep-2026-11-03-gte210"), "house-seats")
        self.assertEqual(family_of("ussewc-usse-ok-2026-11-03-rep"), "other")


class TestHazards(unittest.TestCase):
    def test_priors_order_sanely(self):
        m = FillModel()
        p0 = m.p_fill(SEN, "BUY", 0)
        p3 = m.p_fill(SEN, "BUY", 5)
        self.assertGreater(p0, p3)          # the touch fills more than deep
        self.assertLess(p0, 0.5)
        self.assertGreater(p3, 0.0)

    def test_observed_crossings_raise_the_hazard(self):
        m = FillModel()
        t = 0.0
        # a violent book: the ask sweeps down to two ticks under the bid
        # touch every other sample
        for i in range(200):
            t += 30
            if i % 2:
                m.observe_touch(SEN, 0.50, 0.51, 0.01, t)
            else:
                m.observe_touch(SEN, 0.47, 0.48, 0.01, t)
        p_violent = m.p_fill(SEN, "BUY", 0)
        calm = FillModel()
        t = 0.0
        for _ in range(200):
            t += 30
            calm.observe_touch(SEN, 0.50, 0.51, 0.01, t)
        self.assertGreater(p_violent, 3 * calm.p_fill(SEN, "BUY", 0))

    def test_quiet_books_drive_the_hazard_below_the_prior(self):
        m = FillModel()
        t = 0.0
        for _ in range(5000):               # ~41 hours of stillness
            t += 30
            m.observe_touch(SEN, 0.50, 0.51, 0.01, t)
        self.assertLess(m.p_fill(SEN, "BUY", 0),
                        FillModel().p_fill(SEN, "BUY", 0))

    def test_dead_gaps_are_not_exposure(self):
        m = FillModel()
        m.observe_touch(SEN, 0.50, 0.51, 0.01, 1000.0)
        m.observe_touch(SEN, 0.50, 0.51, 0.01, 90_000.0)   # feed was down
        key = m._key("senate-seats", "BUY", 0)
        self.assertNotIn(key, m.obs)          # nothing accrued across the gap


class TestCalibration(unittest.TestCase):
    def test_fill_marks_move_the_markdown(self):
        m = FillModel()
        seed = m.fill_cost(SEN, "BUY", 0.50, fair=None)
        # a bid filled at 50c, market at 44c an hour later: 6c adverse
        adverse = m.observe_fill_mark(SEN, "BUY", 0.50, 0.44)
        self.assertAlmostEqual(adverse, 0.06)
        self.assertGreater(m.fill_cost(SEN, "BUY", 0.50, fair=None), seed)
        # a fill the market bounced back over costs nothing extra
        self.assertEqual(m.observe_fill_mark(SEN, "BUY", 0.50, 0.55), 0.0)

    def test_fill_cost_adds_the_concession_past_fair(self):
        m = FillModel()
        base = m.fill_cost(SEN, "BUY", 0.20, fair=0.25)   # below fair: no excess
        rich = m.fill_cost(SEN, "BUY", 0.30, fair=0.25)   # 5c above fair
        self.assertAlmostEqual(rich - base, 0.05)
        base_a = m.fill_cost(SEN, "SELL", 0.30, fair=0.25)
        rich_a = m.fill_cost(SEN, "SELL", 0.20, fair=0.25)
        self.assertAlmostEqual(rich_a - base_a, 0.05)

    def test_scoring_fraction_learns(self):
        m = FillModel()
        for _ in range(50):
            m.observe_scoring(SEN, False)
        self.assertLess(m.scoring_fraction(SEN), 0.05)

    def test_roundtrip(self):
        m = FillModel()
        m.observe_touch(SEN, 0.50, 0.51, 0.01, 1000.0)
        m.observe_touch(SEN, 0.47, 0.48, 0.01, 1030.0)
        m.observe_fill_mark(SEN, "BUY", 0.50, 0.44)
        m2 = FillModel.from_dict(m.to_dict())
        self.assertEqual(m2.p_fill(SEN, "BUY", 0), m.p_fill(SEN, "BUY", 0))
        self.assertEqual(m2.markdown, m.markdown)


if __name__ == "__main__":
    unittest.main()


class TestShieldDiscount(unittest.TestCase):
    """A wall of resting contracts in front of an order is evidence
    against a fill (owner, 2026-08-19)."""

    def test_no_wall_leaves_the_hazard_alone(self):
        from v2.fillmodel import shield_discount
        self.assertEqual(shield_discount(0, 5000), 1.0)
        self.assertEqual(shield_discount(5000, 0), 1.0)   # no target: unknown scale

    def test_one_target_size_of_wall_halves_it(self):
        from v2.fillmodel import shield_discount
        self.assertAlmostEqual(shield_discount(5000, 5000), 0.5)
        self.assertAlmostEqual(shield_discount(15000, 5000), 0.25)

    def test_floored_because_a_wall_can_vanish(self):
        from v2.fillmodel import shield_discount, SHIELD_FLOOR
        self.assertEqual(shield_discount(10_000_000, 5000), SHIELD_FLOOR)

    def test_p_fill_falls_behind_a_wall_but_never_to_zero(self):
        m = FillModel()
        bare = m.p_fill("scc-senate-gop-2026-11-03-49", "BUY", 0)
        walled = m.p_fill("scc-senate-gop-2026-11-03-49", "BUY", 0,
                          shield=50_000, target=5_000)
        self.assertLess(walled, bare)
        self.assertGreater(walled, 0.2 * bare)
