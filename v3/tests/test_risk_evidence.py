"""Negative-risk netting and the evidence bands — the money math behind
the ceiling and the price bounds."""

import unittest

from v3.evidence import Evidence
from v3.intents import BUY_LONG, BUY_SHORT
from v3.risk import Leg, book_risk, leg_for_inventory, leg_for_order, marginal


def O(market, intent, price=0.4, qty=10.0, purpose="earn"):
    return type("O", (), {"purpose": purpose, "market": market,
                          "intent": intent, "price": price, "qty": qty})()


class TestNegativeRisk(unittest.TestCase):
    def test_sibling_shorts_net_to_the_worst_one(self):
        legs = [leg_for_order("enwc-x-2028-alpha", BUY_SHORT, 0.4, 10),
                leg_for_order("enwc-x-2028-beta", BUY_SHORT, 0.4, 10)]
        self.assertEqual(book_risk(legs), 6.0)       # one winner at most

    def test_sibling_bids_do_not_net(self):
        legs = [leg_for_order("enwc-x-2028-alpha", BUY_LONG, 0.4, 10),
                leg_for_order("enwc-x-2028-beta", BUY_LONG, 0.4, 10)]
        self.assertEqual(book_risk(legs), 8.0)       # a third can beat both

    def test_nested_gte_shorts_lose_together(self):
        legs = [leg_for_order("scc-hrep-rep-2026-11-03-gte215", BUY_SHORT, 0.4, 10),
                leg_for_order("scc-hrep-rep-2026-11-03-gte220", BUY_SHORT, 0.4, 10)]
        self.assertEqual(book_risk(legs), 12.0)      # a red wave pays both

    def test_marginal_credit_for_the_second_sibling_short(self):
        have = [O("enwc-x-2028-alpha", BUY_SHORT)]
        self.assertEqual(marginal(have, "enwc-x-2028-beta", BUY_SHORT, 0.4, 10), 0.0)
        self.assertGreater(marginal(have, "enwc-y-2028-other", BUY_SHORT, 0.4, 10), 0.0)

    def test_held_inventory_nets_in_full(self):
        # long 10 of alpha + a resting SHORT on alpha itself: the pair is
        # hedged — where the short pays out, the long pays us. Worst case
        # is losing the long's cost, never cost plus collateral.
        inv = [leg_for_inventory("enwc-x-2028-alpha", 10.0, 4.0)]
        hedge = [leg_for_order("enwc-x-2028-alpha", BUY_SHORT, 0.4, 10)]
        self.assertEqual(book_risk(hedge, inv), 4.0)   # nobody wins: cost only
        # and a short on a SIBLING does not pretend to be hedged: if the
        # sibling wins, the alpha long pays nothing while the short pays
        # out against us — the losses genuinely stack
        beta = [leg_for_order("enwc-x-2028-beta", BUY_SHORT, 0.4, 10)]
        self.assertEqual(book_risk(beta, inv), 10.0)

    def test_unrelated_markets_sum(self):
        legs = [leg_for_order("a-race-one-x", BUY_LONG, 0.5, 10),
                leg_for_order("b-race-two-y", BUY_LONG, 0.5, 10)]
        self.assertEqual(book_risk(legs), 10.0)


class TestEvidence(unittest.TestCase):
    def test_fills_move_the_band_and_the_model_yields_to_them(self):
        ev = Evidence(clock=lambda: 1000.0)
        b0 = ev.band("m", prior_fair=0.25)
        for _ in range(4):
            ev.fill("m", "SELL", 0.45)               # buyers keep paying 45
        b1 = ev.band("m", prior_fair=0.25)
        self.assertGreater(b1["med"], b0["med"])
        self.assertEqual(b1["fills"], 4)

    def test_quiet_resting_is_weak_and_wide(self):
        ev = Evidence(clock=lambda: 1000.0)
        for _ in range(5):
            ev.rested("m", "BUY", 0.30)
        b = ev.band("m")
        self.assertGreater(b["hi"] - b["lo"], 30)    # honest uncertainty

    def test_heat_counts_recent_fills_only(self):
        ev = Evidence(clock=lambda: 200000.0)
        ev.fill("m", "BUY", 0.3, ts=100.0)           # two days ago
        ev.fill("m", "BUY", 0.3, ts=199000.0)
        self.assertEqual(ev.heat("m"), 1)

    def test_round_trip(self):
        ev = Evidence(clock=lambda: 1000.0)
        ev.fill("m", "BUY", 0.3)
        ev2 = Evidence(clock=lambda: 1000.0)
        ev2.restore(ev.to_dict())
        self.assertEqual(ev2.band("m")["fills"], 1)


class TestPlannerBounds(unittest.TestCase):
    def test_model_binds_until_two_fills_override(self):
        from v3.tests.test_family import Rig, A
        r = Rig()
        r.add_market(A)
        r.fam.fairs = lambda s: 0.30
        # two real fills through our asks at 45c: evidence outranks Silver
        r.fam.evidence.fill(A, "SELL", 0.45, ts=r.now)
        r.fam.evidence.fill(A, "SELL", 0.45, ts=r.now)
        r.cycle()
        bids = [o for o in r.fam.orders.values() if o.side == "BUY"]
        self.assertTrue(any(o.price > 0.32 for o in bids))

    def test_hot_market_loses_the_touch(self):
        from v3.tests.test_family import Rig, A, politics_book
        r = Rig()
        r.add_market(A)
        for _ in range(6):
            r.cache.put(A, politics_book(r.now))     # provably quiet book
        r.fam.evidence.fill(A, "BUY", 0.44, ts=r.now)  # but we just got eaten
        r.cycle()
        for o in r.fam.orders.values():
            if o.side == "BUY":
                self.assertLess(o.price, 0.44)       # no joining the touch
