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

    def test_no_model_wide_walls_still_quote_but_at_the_frontier(self):
        # Owner, 2026-08-21: "Fine to scout ahead when there's no model
        # as we were doing before" — but never deeper than where the
        # score maxes out
        from v3.tests.test_family import Rig, A
        r = self.rig()
        r.add_market(A, book=self.unknowable_book(1_000_000.0))
        r.cycle()
        self.assertEqual([o for o in r.fam.orders.values()
                          if o.purpose == "probe"], [])
        bids = [o for o in r.fam.orders.values()
                if o.side == "BUY" and o.purpose in ("earn", "solo")]
        self.assertTrue(bids)
        for o in bids:
            self.assertGreater(o.price, 0.05)   # in front of the wall
            self.assertLess(o.price, 0.16)      # but not past the frontier

    def test_grounded_wide_walls_get_a_small_quote_in_front(self):
        # ...and WITH a model, the wide spread is the owner's play: a
        # small order in front captures the score, no probe needed
        from v3.tests.test_family import Rig, A
        r = self.rig()
        r.add_market(A, book=self.unknowable_book(1_000_000.0))
        r.fam.fairs = lambda s: 0.50
        r.cycle()
        self.assertEqual([o for o in r.fam.orders.values()
                          if o.purpose == "probe"], [])
        earns = [o for o in r.fam.orders.values() if o.purpose in
                 ("earn", "solo")]
        self.assertTrue(earns)
        for o in earns:
            if o.side == "BUY":
                self.assertGreater(o.price, 0.05)    # in front of the wall
                self.assertLess(o.price, 0.95 - 0.009)
            self.assertLessEqual(o.price * o.qty, 1.01)   # small money

    def test_scout_reports_in_after_its_watch(self):
        # a bar the planner cannot clear anywhere (est tops out near
        # side_pool x scoring fraction = $40) while the side pool still
        # pays the probe's own worth-it check — the scout goes out
        from v3.tests.test_family import Rig, A
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet", revive=True,
                           capital_usd=100.0, min_est_day=45.0,
                           probe_usd=5.0)
        r = Rig(cfg=cfg)
        r.add_market(A, book=self.unknowable_book(1_000_000.0))
        r.cycle()
        pid = next(o.id for o in r.fam.orders.values() if o.purpose == "probe")
        r.cycle(advance=r.fam.cfg.probe_ttl_s + 60)
        self.assertNotIn(pid, r.fam.orders)          # rotated out
        self.assertNotIn(pid, r.exchange.live)
        self.assertTrue(any(str(row[1]).startswith("rest")
                            for row in r.fam.evidence.events.get(A, ())))

    def test_confident_markets_are_not_probed(self):
        r = self.rig()
        from v3.tests.test_family import A
        r.add_market(A, book=self.unknowable_book(1_000_000.0))
        for _ in range(8):
            r.fam.evidence.fill(A, "BUY", 0.05, ts=1_000_000.0)
        r.cycle()
        self.assertEqual([o for o in r.fam.orders.values()
                          if o.purpose == "probe"], [])


class TestEdgeAggression(unittest.TestCase):
    """Owner, 2026-08-21: 'it's okay to get filled at reasonable prices' —
    edge against value earns the touch and lifts the courtesy share."""

    def rig(self, fair):
        from v3.tests.test_family import Rig
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet", revive=True,
                           capital_usd=100.0, per_market_usd=20.0,
                           join_edge_ticks=2.0, share_max=0.35)
        r = Rig(cfg=cfg)
        r.fam.fairs = (lambda s: fair) if fair is not None else None
        return r

    def test_value_licenses_the_front_without_quiet_proof(self):
        from v3.tests.test_family import A
        r = self.rig(0.52)              # model: worth 52c; bid touch is 44c
        r.add_market(A)
        r.cycle()                       # NO volatility evidence exists
        bids = [o for o in r.fam.orders.values() if o.side == "BUY"]
        self.assertTrue(any(o.price >= 0.44 - 1e-9 for o in bids), bids)

    def test_queue_ahead_shields_the_join(self):
        # Owner, 2026-08-21: joining an occupied level is protected by
        # the shares already there — first come, first served. Thick
        # queue -> lower fill odds at the SAME price.
        from v3.fillmodel import FillModel
        m = FillModel()
        slug = "vmc-ussemov-ga-2026-11-03-d4-7"
        thin = m.p_fill(slug, "BUY", 0, shield=0.5, target=5000.0)
        thick = m.p_fill(slug, "BUY", 0, shield=4000.0, target=5000.0)
        self.assertLess(thick, thin * 0.8)

    def test_share_cap_lifts_with_edge(self):
        from v3.tests.test_family import A
        from v3.scoring import Book
        # thin real competition: joining with size means a BIG share
        thin = Book(bids=((0.40, 6.0), (0.02, 60000.0)),
                    asks=((0.60, 6.0), (0.98, 60000.0)),
                    tick=0.01, fetched_at=1_000_000.0)
        r = self.rig(0.52)              # touch 40c, 12 ticks inside value
        r.add_market(A, book=thin)
        r.cycle()
        bids = [o for o in r.fam.orders.values() if o.side == "BUY"]
        self.assertTrue(bids)
        self.assertGreater(max(o.share for o in bids), 0.10)   # past the old cap
        self.assertLessEqual(max(o.share for o in bids), 0.36)
        # same book, no value information: the old courtesy stands
        r2 = self.rig(None)
        r2.add_market(A, book=thin)
        r2.cycle()
        for o in r2.fam.orders.values():
            if o.side == "BUY":
                self.assertLessEqual(o.share, 0.101)


class TestEVDecision(unittest.TestCase):
    """The owner's 2026-08-19 directive, now in v3: every placement is
    EV = income x scoring fraction - p(fill) x fill cost x size."""

    def rig(self):
        from v3.tests.test_family import Rig
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet", revive=True,
                           capital_usd=100.0, per_market_usd=20.0,
                           join_edge_ticks=2.0, share_max=0.35,
                           min_est_day=0.02)
        return Rig(cfg=cfg)

    def test_ruinous_learned_fill_cost_stops_placement(self):
        from v3.tests.test_family import A
        r1 = self.rig()
        r1.add_market(A)
        r1.cycle()
        self.assertTrue([o for o in r1.fam.orders.values()
                         if o.side == "BUY"])          # baseline: it places
        r2 = self.rig()
        r2.add_market(A)
        # fills here are LEARNED to be ruinous — absurdly so, on
        # purpose: even the touch's five-fold score cannot pay for it
        r2.fam.fillmodel.markdown["margins"] = 500.0
        r2.cycle()
        self.assertEqual([o for o in r2.fam.orders.values()
                          if o.side == "BUY" and o.purpose == "earn"], [])

    def test_plans_carry_the_ev_numbers(self):
        from v3.tests.test_family import A
        r = self.rig()
        r.add_market(A)
        r.cycle()
        sb = r.fam.scoreboard[A]
        for p in sb["plans"]:
            self.assertIn("ev", p)
            self.assertIn("p_fill", p)
            self.assertLessEqual(p["ev"], p["est"] + 1e-9)

    def test_fill_is_graded_an_hour_later(self):
        from v3.tests.test_family import A
        r = self.rig()
        r.add_market(A)
        r.cycle()
        bid = next(o for o in r.fam.orders.values() if o.side == "BUY")
        del r.exchange.live[bid.id]
        r.positions[A] = (bid.qty, bid.qty * bid.price)
        r.cycle()
        self.assertTrue(r.fam.pending_marks)
        before = dict(r.fam.fillmodel.markdown)
        r.cycle(advance=3700.0)
        self.assertNotEqual(r.fam.fillmodel.markdown, before)
        self.assertTrue(any(l.get("event") == "fill_graded"
                            for l in r.fam.log))

    def test_graduated_markets_leave_the_search_ceiling(self):
        from v3.tests.test_family import A, C, Rig
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet",
                           capital_usd=10.0, per_market_usd=20.0,
                           proven_usd=50.0, graduate_paid_usd=0.25)
        r = Rig(cfg=cfg)
        r.add_market(A)
        r.add_market(C, event="House control")
        r.cycle()
        spent_all = r.fam.family_spent()
        # A graduates: its collateral moves to the proven pool
        r.fam.proven = {A}
        self.assertLess(r.fam.family_spent(), spent_all + 1e-9)
        self.assertGreater(r.fam.proven_spent(), 0.0)
        self.assertLessEqual(r.fam.family_spent() + 1e-9, 10.0)


class TestGrowthInvesting(unittest.TestCase):
    """Owner, 2026-08-21: 75c is a GOAL. A market that cannot clear it at
    today's confidence, but would at full confidence, gets a starter."""

    def rig(self):
        from v3.tests.test_family import Rig
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet",
                           capital_usd=100.0, per_market_usd=20.0,
                           min_est_day=0.75, share_max=0.35,
                           grow_usd=30.0, grow_floor=0.10,
                           join_edge_ticks=2.0)
        return Rig(cfg=cfg)

    def thin_book(self, now):
        # tiny real competition in a ONE-TICK spread (no room in front):
        # at the 10% courtesy cap the est stays under the goal, but at
        # the full 35% cap it clears it
        from v3.scoring import Book
        return Book(bids=((0.44, 4.0), (0.02, 60000.0)),
                    asks=((0.45, 4.0), (0.98, 60000.0)),
                    tick=0.01, fetched_at=now)

    SMALL_POOL = {"timePeriods": [{"programId": "politics_mid_1",
                                   "rewardPool": 6.0, "targetSize": 5000,
                                   "discountFactor": 0.2, "status": "LIVE"}]}

    def test_under_goal_market_gets_a_starter_when_potential_clears(self):
        from v3.tests.test_family import A
        r = self.rig()
        r.add_market(A, book=self.thin_book(1_000_000.0),
                     prog=self.SMALL_POOL)
        r.cycle()
        grows = [o for o in r.fam.orders.values() if o.purpose == "grow"]
        self.assertTrue(grows)
        g = grows[0]
        self.assertIn("investing to build the evidence", g.why)
        spent = sum(o.price * o.qty if o.side == "BUY"
                    else (1 - o.price) * o.qty for o in grows)
        self.assertLessEqual(spent, 30.0 + 1e-6)

    def test_growth_off_means_no_starter(self):
        from v3.tests.test_family import A, Rig
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           min_est_day=0.75, grow_usd=0.0)
        r = Rig(cfg=cfg)
        r.add_market(A, book=self.thin_book(1_000_000.0),
                     prog=self.SMALL_POOL)
        r.cycle()
        self.assertEqual([o for o in r.fam.orders.values()
                          if o.purpose == "grow"], [])

    def test_grow_culls_at_its_own_floor_not_the_goal(self):
        from v3.tests.test_family import A
        r = self.rig()
        r.add_market(A, book=self.thin_book(1_000_000.0),
                     prog=self.SMALL_POOL)
        r.cycle()
        g = next(o for o in r.fam.orders.values() if o.purpose == "grow")
        # it measures ~30-70c: under the GOAL but above its 10c floor —
        # hours later it must still be standing
        r.cycle(advance=4000.0)
        self.assertIn(g.id, r.fam.orders)


class TestEvidenceWeighting0821(unittest.TestCase):
    """The owner's Becerra critique, as tests: one vote per resting
    order growing with log-time, and the market's standing depth counted
    by its size."""

    def test_one_order_one_vote_however_long_it_rests(self):
        from v3.evidence import Evidence
        ev = Evidence(clock=lambda: 100_000.0)
        for i in range(12):                      # 12 half-hourly marks
            ev.rest_mark("m", "o1", "SELL", 0.95, started=78_400.0,
                         now=78_400.0 + (i + 1) * 1800)
        rows = [r for r in ev.events["m"] if str(r[1]).startswith("restrec")]
        self.assertEqual(len(rows), 1)           # ONE record, not twelve

    def test_a_week_outweighs_an_hour_but_not_by_168x(self):
        from v3.evidence import Evidence
        hour = Evidence._rest_weight(3600.0)
        day = Evidence._rest_weight(86_400.0)
        week = Evidence._rest_weight(7 * 86_400.0)
        self.assertLess(hour, day)
        self.assertLess(day, week)
        self.assertLess(week / hour, 8)          # log growth, not linear

    def test_million_share_bid_outvotes_our_quiet_ask(self):
        # the owner's exact scenario: our ask rested at 95 for hours, a
        # 1,011,120-share bid stands at 94. Value must land between the
        # touches, not at 88.
        from v3.evidence import Evidence
        ev = Evidence(clock=lambda: 100_000.0)
        ev.rest_mark("m", "o1", "SELL", 0.95, started=78_400.0, now=100_000.0)
        b = ev.band("m", touches=(0.94, 0.95),
                    touch_sizes=(1_011_120.0, 26_693.0))
        self.assertGreaterEqual(b["med"], 93, b)
        self.assertLessEqual(b["med"], 96, b)

    def test_instruments_collect_and_persist(self):
        from v3.fillmodel import FillModel, age_bucket, tod_band
        self.assertEqual(age_bucket(1800), 0)
        self.assertEqual(age_bucket(7200), 1)
        self.assertEqual(age_bucket(3 * 86400), 3)
        fm = FillModel()
        fm.observe_order_age("ussewc-usse-ga-2026-11-03-rep", 7200, 60.0)
        fm.observe_fill_age("ussewc-usse-ga-2026-11-03-rep", 7200)
        self.assertEqual(fm.age_obs["senate|1"], [60.0, 1.0])
        fm.observe_touch("ussewc-usse-ga-2026-11-03-rep", 0.44, 0.47,
                         0.01, 1_000_000.0)
        fm.observe_touch("ussewc-usse-ga-2026-11-03-rep", 0.44, 0.47,
                         0.01, 1_000_060.0)
        self.assertTrue(any(k.startswith("senate|") for k in fm.tod_obs))
        fm2 = FillModel.from_dict(fm.to_dict())
        self.assertEqual(fm2.age_obs, fm.age_obs)
        self.assertEqual(fm2.tod_obs, fm.tod_obs)


# ---- the owner's fill-cost equation (2026-08-21) ----

class TestFillCostEquation(unittest.TestCase):
    def test_fill_cost_credits_exit_earnings(self):
        from v3.fillmodel import FillModel
        m = FillModel()
        base = m.fill_cost("ussewc-usse-mt-2026-11-03-dem", "SELL", 0.30, 0.33)
        # exit earns 1c/share/day, offload seed is 2 days -> 2c credit
        net = m.fill_cost("ussewc-usse-mt-2026-11-03-dem", "SELL", 0.30, 0.33,
                          exit_rate_ps=0.01)
        self.assertAlmostEqual(base - net, 0.02, places=6)

    def test_fill_cost_can_go_negative(self):
        from v3.fillmodel import FillModel
        m = FillModel()
        net = m.fill_cost("ussewc-usse-mt-2026-11-03-dem", "SELL", 0.33, 0.33,
                          exit_rate_ps=0.10)
        self.assertLess(net, 0.0)  # exits that earn more than the fill loses

    def test_offload_days_learned_and_persisted(self):
        from v3.fillmodel import FillModel
        m = FillModel()
        slug = "ussewc-usse-mt-2026-11-03-dem"
        assert m.expected_offload_days(slug) == 2.0  # seed
        m.observe_offload(slug, 0.5)
        d1 = m.expected_offload_days(slug)
        assert 0.5 < d1 < 2.0  # EWMA moved toward the observation
        m2 = FillModel.from_dict(m.to_dict())
        assert m2.expected_offload_days(slug) == d1
        assert m2.offload_n == m.offload_n

    def test_family_times_the_offload(self):
        from v3.tests.test_family import Rig, A
        from v3.family import FamilyOrder
        r = Rig()
        fam = r.fam
        now = 1_000_000.0
        rec = fam.orders["A1"] = FamilyOrder(
            id="A1", market=A, side="BUY",
            price=0.30, qty=10.0, intent="ORDER_INTENT_BUY_LONG",
            placed_ts=now, purpose="earn")
        fam._on_fill(rec, 10.0, now)
        assert fam.inv_since.get(A) == now
        sell = fam.orders["A2"] = FamilyOrder(
            id="A2", market=A, side="SELL",
            price=0.35, qty=10.0, intent="ORDER_INTENT_SELL_LONG",
            placed_ts=now, purpose="sell")
        fam._on_fill(sell, 10.0, now + 86400.0)  # offloaded a day later
        assert A not in fam.inv_since
        d = fam.fillmodel.expected_offload_days(A)
        assert 1.0 < d < 2.0  # EWMA of seed 2.0 and observed 1.0


class TestApproachData(unittest.TestCase):
    def test_approach_minutes_and_dollars_accumulate_and_persist(self):
        from v3.fillmodel import FillModel
        m = FillModel()
        slug = "ussewc-usse-mt-2026-11-03-dem"
        m.observe_approach(slug, "BUY", 0, 60.0, 2.4)   # a minute at the touch
        m.observe_approach(slug, "BUY", 0, 60.0, 2.4)
        m.observe_approach(slug, "BUY", 3, 60.0, 0.3)   # a minute well back
        key0 = "senate|BUY|0"
        self.assertEqual(m.approach_obs[key0][0], 120.0)
        self.assertAlmostEqual(m.approach_obs[key0][1] / m.approach_obs[key0][0],
                               2.4, places=6)           # $/day while resting there
        m2 = FillModel.from_dict(m.to_dict())
        self.assertEqual(set(m2.approach_obs), set(m.approach_obs))


class TestOwnerCorrections0821b(unittest.TestCase):
    """Owner, 2026-08-21 evening: bait measures against FAIR not the
    touch; heat means small retries, not a closed front; exits hunt the
    best-earning profitable slot."""

    def _rig(self, fair=None):
        from v3.tests.test_family import Rig
        from v3.family import FamilyConfig
        cfg = FamilyConfig(name="P", tag="P", known_ground=True,
                           rest_style="join_quiet", revive=True,
                           capital_usd=100.0, per_market_usd=20.0,
                           min_est_day=0.05, share_max=0.35)
        r = Rig(cfg=cfg)
        if fair is not None:
            r.fam.fairs = lambda s: fair
        return r

    def wide_book(self):
        from v3.scoring import Book
        return Book(bids=((0.10, 50000.0), (0.02, 500000.0)),
                    asks=((0.90, 50000.0), (0.98, 500000.0)),
                    tick=0.01, fetched_at=1_000_000.0)

    def test_the_front_stops_at_the_score_frontier(self):
        # Owner, 2026-08-21: the question is 27 vs 28 vs 29 — once the
        # score stops improving, deeper placement is pointless. Model or
        # no model, the front walk stops at the frontier.
        from v3.tests.test_family import A
        for fair in (None, 0.50):
            r = self._rig(fair)
            r.add_market(A, book=self.wide_book())
            r.cycle()
            rows = [p for p in ((r.fam.scoreboard.get(A) or {})
                                .get("plans") or [])
                    if p["side"] == "BUY" and p["px"] > 0.10]
            self.assertTrue(rows, fair)
            for p in rows:
                self.assertLessEqual(p["px"], 0.20)   # frontier, not mid

    def test_heat_shrinks_the_retry_instead_of_closing_the_front(self):
        from v3.tests.test_family import A
        r = self._rig(0.50)
        r.add_market(A, book=self.wide_book())
        r.fam.evidence.fill(A, "BUY", 0.15, ts=999_995.0)   # just filled
        r.cycle()
        bids = [o for o in r.fam.orders.values()
                if o.side == "BUY" and o.purpose == "earn"]
        self.assertTrue(bids)                # the front is NOT closed
        for o in bids:
            self.assertLessEqual(o.qty, 0.011)   # minimum-size retry

    def test_exit_takes_the_open_slot_not_the_crowded_touch(self):
        # the owner's MN example: bought 10 @ 92c; the ask touch at 97c
        # holds 217 shares by a wall, while 94c is open. The exit must
        # rest where it earns, not pile on.
        from v3.tests.test_family import A
        from v3.scoring import Book
        r = self._rig()
        book = Book(bids=((0.92, 30.0), (0.02, 60000.0)),
                    asks=((0.97, 217.0), (0.99, 60000.0)),
                    tick=0.01, fetched_at=1_000_000.0)
        r.add_market(A, book=book)
        r.fam.inventory[A] = {"qty": 10.0, "cost": 9.2}     # 92c each
        r.cycle()
        exits = [o for o in r.fam.orders.values() if o.purpose == "sell"]
        self.assertTrue(exits)
        e = exits[0]
        self.assertLess(e.price, 0.97)          # off the crowded touch
        self.assertGreaterEqual(e.price, 0.93)  # still a profit
        self.assertGreater(e.est_day if e.est_day else 1.0, 0.0)

    def test_lone_misplaced_exit_moves_to_the_better_slot(self):
        from v3.tests.test_family import A
        from v3.family import FamilyOrder
        from v3.scoring import Book
        r = self._rig()
        book = Book(bids=((0.92, 30.0), (0.02, 60000.0)),
                    asks=((0.97, 217.0), (0.99, 60000.0)),
                    tick=0.01, fetched_at=1_000_000.0)
        r.add_market(A, book=book)
        r.fam.inventory[A] = {"qty": 10.0, "cost": 9.2}
        rec = FamilyOrder(id="OLD", market=A, side="SELL", price=0.97,
                          qty=10.0, intent="ORDER_INTENT_SELL_LONG",
                          placed_ts=0.0, purpose="sell", live_est=0.01)
        r.fam.orders["OLD"] = rec
        r.exchange.live["OLD"] = {"id": "OLD", "market": A, "side": "SELL",
                                  "price": 0.97, "size": 10.0}
        r.cycle()
        exits = [o for o in r.fam.orders.values() if o.purpose == "sell"]
        self.assertTrue(exits)
        self.assertTrue(all(o.price < 0.97 for o in exits))  # moved down
