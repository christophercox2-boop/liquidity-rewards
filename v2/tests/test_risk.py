"""Negative-risk netting: the family book priced against seat count K."""

import unittest

from v2.intents import BUY_LONG, BUY_SHORT, SELL_LONG
from v2.risk import (
    Leg, family_risk, leg_for_inventory, leg_for_order, marginal_risk,
    parse_rung, rung_pays,
)


def ask(rung, price, qty=1.0):
    return leg_for_order(rung, BUY_SHORT, price, qty)


def bid(rung, price, qty=1.0):
    return leg_for_order(rung, BUY_LONG, price, qty)


class TestParsing(unittest.TestCase):
    def test_rungs(self):
        self.assertEqual(parse_rung("scc-senate-gop-2026-11-03-52"),
                         ("scc-senate-gop-2026-11-03", "52"))
        self.assertEqual(parse_rung("scc-hrep-rep-2026-11-03-gte215"),
                         ("scc-hrep-rep-2026-11-03", "gte215"))
        self.assertEqual(parse_rung("scc-senate-gop-2026-11-03-lte45"),
                         ("scc-senate-gop-2026-11-03", "lte45"))
        self.assertIsNone(parse_rung("enwc-uspres-nom-dem-2028-jonoss"))

    def test_rung_pays(self):
        self.assertTrue(rung_pays("52", 52))
        self.assertFalse(rung_pays("52", 53))
        self.assertTrue(rung_pays("gte215", 230))
        self.assertFalse(rung_pays("gte215", 214))
        self.assertTrue(rung_pays("lte45", 40))


class TestSingleLegs(unittest.TestCase):
    def test_alone_matches_the_old_accounting(self):
        self.assertAlmostEqual(family_risk([bid("52", 0.10, 5)]), 0.50)
        self.assertAlmostEqual(family_risk([ask("52", 0.10, 5)]), 4.50)

    def test_closing_intents_are_free(self):
        self.assertIsNone(leg_for_order("52", SELL_LONG, 0.5, 5))


class TestExclusiveRungs(unittest.TestCase):
    """Senate exact counts: at most ONE rung resolves YES."""

    def test_asks_share_one_collateral(self):
        legs = [ask("47", 0.08, 13), ask("48", 0.19, 14),
                ask("50", 0.18, 14), ask("53", 0.08, 13)]
        # old accounting: 11.96 + 11.34 + 11.48 + 11.96 = 46.74
        # true worst case: only one rung can hit -> the biggest collateral
        self.assertAlmostEqual(family_risk(legs), 11.96, places=2)

    def test_marginal_ask_under_the_dominant_one_is_free(self):
        legs = [ask("47", 0.08, 13)]                      # worst 11.96
        self.assertAlmostEqual(
            marginal_risk(legs, ask("50", 0.18, 14)), 0.0, places=2)
        # ...but a BIGGER ask raises the worst case by the difference
        self.assertAlmostEqual(
            marginal_risk(legs, ask("51", 0.13, 92)), 92 * 0.87 - 11.96,
            places=2)

    def test_bids_still_sum(self):
        # all exclusive bids CAN lose together (K lands somewhere else)
        legs = [bid("51", 0.13, 92), bid("52", 0.10, 1)]
        self.assertAlmostEqual(family_risk(legs), 92 * 0.13 + 0.10, places=2)

    def test_winning_orders_get_no_credit(self):
        # a bid and an ask on the same rung: whatever K is, the adversary
        # fills only the losing one — never nets a winner we weren't owed
        legs = [bid("52", 0.09, 10), ask("52", 0.11, 10)]
        self.assertAlmostEqual(family_risk(legs), 8.90, places=2)  # ask loses


class TestNestedRungs(unittest.TestCase):
    """House gte rungs are nested — a red wave hits every short at once."""

    def test_nested_asks_stack(self):
        legs = [ask("gte180", 0.86, 10), ask("gte215", 0.32, 10)]
        # K >= 215: both pay YES, both shorts lose their full collateral
        self.assertAlmostEqual(family_risk(legs), 10 * 0.14 + 10 * 0.68,
                               places=2)

    def test_nested_bid_and_ask_spread(self):
        # long gte215 + short gte225 is a spread: worst K is 215..224,
        # where the long pays and the short survives... the short's loss
        # zone (K>=225) is where the long WINS, so they net
        legs = [bid("gte215", 0.30, 10), ask("gte225", 0.10, 10)]
        # K < 215: bid loses 3.00, ask unfilled -> 3.00
        # K in 215..224: bid wins (not filled by adversary), ask survives -> 0
        # K >= 225: ask loses 9.00, bid wins (unfilled) -> 9.00
        self.assertAlmostEqual(family_risk(legs), 9.00, places=2)


class TestInventoryNets(unittest.TestCase):
    def test_held_long_offsets_a_short_where_it_pays(self):
        held = leg_for_inventory("gte215", 10, 3.0)       # long 10 @ 30c
        short = ask("gte225", 0.10, 10)
        # K >= 225: short loses 9.00 but the HELD long pays 10 - 3 = +7
        # K in 215..224: long +7... as a firm leg gains are real
        # K < 215: long loses its 3.00 cost, short survives
        self.assertAlmostEqual(family_risk([held, short]), 3.00, places=2)

    def test_short_inventory_ledger_shape(self):
        # ledger: qty < 0, cost = collateral committed
        held = leg_for_inventory("52", -10, 9.0)          # short 10 @ 10c
        self.assertAlmostEqual(family_risk([held]), 9.0)
        # and it nets against an opposing ask elsewhere only via K logic
        self.assertAlmostEqual(family_risk([held, ask("53", 0.10, 10)]),
                               9.0, places=2)             # exclusive rungs

    def test_dust_inventory_is_no_leg(self):
        self.assertIsNone(leg_for_inventory("52", 0.0, 0.0))


class TestFloors(unittest.TestCase):
    def test_empty_and_profit_books_read_zero(self):
        self.assertEqual(family_risk([]), 0.0)
        held = leg_for_inventory("52", 10, 0.0)           # free stock
        self.assertEqual(family_risk([held]), 0.0)

    def test_marginal_never_negative(self):
        legs = [ask("47", 0.08, 13)]
        self.assertGreaterEqual(marginal_risk(legs, ask("48", 0.50, 1)), 0.0)


if __name__ == "__main__":
    unittest.main()
