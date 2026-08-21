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

    def test_heat_is_continuous_and_decays(self):
        ev = Evidence(clock=lambda: 200000.0)
        ev.fill("m", "BUY", 0.3, ts=100.0)           # two days ago: aged out
        ev.fill("m", "BUY", 0.3, ts=199000.0)        # 17 min ago: ~full weight
        self.assertAlmostEqual(ev.heat("m"), 1.0, places=1)
        ev2 = Evidence(clock=lambda: 200000.0 + 20 * 3600)
        ev2.events = {k: [list(r) for r in v] for k, v in ev.events.items()}
        self.assertLess(ev2.heat("m"), 0.75)         # same fill, cooler later

    def test_confidence_grows_with_fills_and_decays_with_time(self):
        ev = Evidence(clock=lambda: 1000.0)
        self.assertEqual(ev.confidence("m"), 0.0)
        cs = []
        for _ in range(4):
            ev.fill("m", "SELL", 0.45)
            cs.append(ev.confidence("m", ev.band("m")))
        self.assertTrue(cs[0] < cs[1] < cs[3] < 1.0)
        late = Evidence(clock=lambda: 1000.0 + 3 * 86400)
        late.events = {k: [list(r) for r in v] for k, v in ev.events.items()}
        self.assertLess(late.confidence("m", late.band("m")), cs[3])

    def test_bounds_slide_continuously_with_confidence(self):
        from v3.tests.test_family import Rig, A
        r = Rig()
        r.add_market(A)
        r.fam.fairs = lambda s: 0.30
        book = r.exchange.books[A]
        def hi():
            return r.fam._price_bounds(A, book.bids, book.asks, 0.01)[1]
        h0 = hi()
        r.fam.evidence.fill(A, "SELL", 0.45, ts=r.now)
        h1 = hi()
        for _ in range(3):
            r.fam.evidence.fill(A, "SELL", 0.45, ts=r.now)
        h4 = hi()
        self.assertLess(abs(h0 - 0.30), 0.02)        # no evidence: on the model
        self.assertTrue(h0 < h1 < h4)                # each fill earns more room

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


class TestProbing(unittest.TestCase):
    """Owner, 2026-08-21: 'Unless you have all the information you need,
    go out and get some.'"""

    def rig(self):
        from v3.tests.test_family import Rig, A
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet", revive=True,
                           capital_usd=100.0, min_est_day=0.75,
                           probe_usd=5.0)
        return Rig(cfg=cfg)

    def unknowable_book(self, now):
        # a rich pool but a book the planner can't clear the bar in:
        # a lone junk wall each side, no real competition to join
        from v3.scoring import Book
        return Book(bids=((0.05, 9000.0),), asks=((0.95, 9000.0),),
                    tick=0.01, fetched_at=now)

    def test_low_confidence_rich_pool_gets_a_scout(self):
        from v3.tests.test_family import Rig, A
        r = self.rig()
        r.add_market(A, book=self.unknowable_book(1_000_000.0))
        r.cycle()
        probes = [o for o in r.fam.orders.values() if o.purpose == "probe"]
        self.assertEqual(len(probes), 1)
        p = probes[0]
        self.assertLessEqual(p.qty, 1.0)
        self.assertLessEqual(p.price, 0.05)          # behind the wall, cheap
        self.assertIn("scout", p.why)
        # cooldown: no second scout in the same market next cycle
        r.cycle()
        self.assertEqual(len([o for o in r.fam.orders.values()
                              if o.purpose == "probe"]), 1)

    def test_scout_reports_in_after_its_watch(self):
        r = self.rig()
        from v3.tests.test_family import A
        r.add_market(A, book=self.unknowable_book(1_000_000.0))
        r.cycle()
        pid = next(o.id for o in r.fam.orders.values() if o.purpose == "probe")
        r.cycle(advance=r.fam.cfg.probe_ttl_s + 60)
        self.assertNotIn(pid, r.fam.orders)          # rotated out
        self.assertNotIn(pid, r.exchange.live)
        self.assertTrue(any(k.startswith("rest")
                            for _, k, _2 in r.fam.evidence.events.get(A, ())))

    def test_confident_markets_are_not_probed(self):
        r = self.rig()
        from v3.tests.test_family import A
        r.add_market(A, book=self.unknowable_book(1_000_000.0))
        for _ in range(8):
            r.fam.evidence.fill(A, "BUY", 0.05, ts=1_000_000.0)
        r.cycle()
        self.assertEqual([o for o in r.fam.orders.values()
                          if o.purpose == "probe"], [])
