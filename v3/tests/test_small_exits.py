"""Small exits sit at the touch outside the give-up budget (owner,
2026-09-02, "Those changes are fine").

The cfb week-1 read: the $4-8/day earners were 1-2 share covers AT a
thin touch — Kansas 3.5 wins measured $6.61/day at 88% of its side.
When the family-wide $5 give-up budget filled on Sunday the exit gate
had nothing to bless, and the cover was pulled 8 ticks back to save 16
cents on a 2-share buy-back. A small exit's reward still has to beat
its fill loss by the gate's margin; only the budget stops applying.
"""

import unittest

from v3.family import FamilyConfig, FamilyOrder
from v3.intents import SELL_SHORT
from v3.scoring import Book
from v3.tests.test_family import LIVE_PROG, A, Rig


def kansas_book(now, ask=0.93):
    # the cfb shape: a few shares at the touch, the wall far behind
    return Book(bids=((0.92, 3.0), (0.01, 20000.0)),
                asks=((ask, 5.0), (0.99, 20000.0)),
                tick=0.01, fetched_at=now)


def rig(cap, book=None, prog=LIVE_PROG):
    cfg = FamilyConfig(name="P", tag="P", capital_usd=0.0,   # exits only
                       exit_giveup_cap_usd=cap)
    r = Rig(cfg=cfg)
    r.add_market(A, book=book or kansas_book(r.now), prog=prog)
    return r


def covers(r):
    return [o for o in r.fam.orders.values() if o.intent == SELL_SHORT]


class TestSmallExits(unittest.TestCase):
    def test_a_two_share_cover_joins_the_touch_with_the_budget_full(self):
        r = rig(cap=0.0)                    # nothing left in the budget
        r.positions[A] = (-2.0, -1.58)      # short 2, sold at 79c
        r.cycle()
        c = covers(r)
        self.assertEqual(len(c), 1)
        # 13c past break-even on 2 shares is a 26c give-up: small, so
        # the budget does not apply and the bid rests at the touch
        self.assertAlmostEqual(c[0].price, 0.92)
        self.assertEqual(c[0].purpose, "sell")

    def test_a_big_cover_still_needs_the_budget(self):
        r = rig(cap=0.0)
        r.positions[A] = (-200.0, -158.0)   # same 79c basis, $26 give-up
        r.cycle()
        c = covers(r)
        self.assertEqual(len(c), 1)
        self.assertLessEqual(c[0].price, 0.79 + 1e-9)

    def test_on_a_wide_book_the_small_cover_joins_rather_than_fronts(self):
        # 92 / 95: the fronts are 93 and 94; joining 92 gives up least
        r = rig(cap=5.0, book=kansas_book(1_000_000.0, ask=0.95))
        r.positions[A] = (-2.0, -1.58)
        r.cycle()
        c = covers(r)
        self.assertEqual(len(c), 1)
        self.assertAlmostEqual(c[0].price, 0.92)

    def test_a_big_cover_never_joins_on_the_small_exits_privilege(self):
        # $26 of give-up at the touch, budget wide open: the gate may
        # still only FRONT (unchanged), never join
        r = rig(cap=100.0, book=kansas_book(1_000_000.0, ask=0.95))
        r.positions[A] = (-200.0, -158.0)
        r.cycle()
        c = covers(r)
        self.assertEqual(len(c), 1)
        self.assertNotAlmostEqual(c[0].price, 0.92)

    def test_small_exits_do_not_drain_the_budget(self):
        r = rig(cap=5.0)
        r.fam.inventory[A] = {"qty": -2.0, "cost": -1.58}
        r.fam.orders["k"] = FamilyOrder(
            id="k", market=A, side="BUY", price=0.92, qty=2.0,
            intent=SELL_SHORT, placed_ts=0.0, purpose="sell")
        self.assertAlmostEqual(r.fam._exit_giveup_in_play(), 0.0)
        r.fam.orders["k"].qty = 200.0
        r.fam.inventory[A] = {"qty": -200.0, "cost": -158.0}
        self.assertAlmostEqual(r.fam._exit_giveup_in_play(), 26.0)

    def test_a_small_exit_still_needs_the_reward_to_pay_for_the_fill(self):
        tiny = {"timePeriods": [{"programId": "p", "rewardPool": 0.01,
                                 "targetSize": 5000, "discountFactor": 0.2,
                                 "status": "LIVE"}]}
        r = rig(cap=0.0, prog=tiny)
        r.positions[A] = (-2.0, -1.58)
        r.cycle()
        c = covers(r)
        self.assertEqual(len(c), 1)
        self.assertLessEqual(c[0].price, 0.79 + 1e-9)


if __name__ == "__main__":
    unittest.main()
