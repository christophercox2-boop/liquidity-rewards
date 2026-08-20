"""Engine tests: the full chain through the real OrderDesk rails against
a fake exchange that actually rests and cancels orders."""

import unittest
from pathlib import Path

from v2.books import BookCache
from v2.engine import Engine, EngineConfig
from v2.intents import REST_SIDE, SELL_LONG
from v2.orders import OrderDesk
from v2.scoring import Book, estimate_join
from v2.silver import SilverFairs
from v2.terms import TermsStore

SEN = "scc-senate-gop-2026-11-03-49"    # model fair ~25.7c
TAIL = "scc-senate-gop-2026-11-03-54"   # model fair ~0.1c, market ~10c
HOUSE = "scc-hrep-rep-2026-11-03-gte210"

REAL_CSV = Path(__file__).resolve().parent.parent.parent / "data" / "silver_senate_races.csv"


class FakeExchange:
    """Plays the exchange for the desk: placements rest, cancels remove."""

    def __init__(self):
        self.next_id = 1
        self.live: dict[str, dict] = {}
        self.posts: list[tuple[str, dict]] = []

    def post(self, url, body, path=None, **kw):
        self.posts.append((url, body))
        if url.endswith("/v1/orders"):
            oid = f"o{self.next_id}"
            self.next_id += 1
            self.live[oid] = {
                "id": oid, "market": body["marketSlug"],
                "side": REST_SIDE[body["intent"]],
                "price": float(body["price"]["value"]),
                "size": float(body["quantity"]), "intent": body["intent"],
            }
            return {"order": {"id": oid}}
        if "/cancel" in url:
            self.live.pop(url.rstrip("/cancel").rsplit("/", 1)[-1], None)
            return {}
        return {}

    def open_orders(self):
        return [dict(o) for o in self.live.values()]


def seats_terms(slugs, pool=100, target=5000):
    st = TermsStore()
    raw = {s: {"timePeriods": [{"programId": "politics_mid_1", "rewardPool": pool,
                                "targetSize": target, "discountFactor": 0.2,
                                "status": "LIVE"}]} for s in slugs}
    st.refresh(raw, {s: (13 if "senate" in s else 12) for s in slugs}, now=1.0)
    return st


def put_book(cache, slug, bid, ask, bid_qty=30.0, ask_qty=30.0, now=0.0):
    # the realistic seats shape: a thin touch, the qualifying wall far back
    cache.put(slug, Book(bids=((bid, bid_qty), (0.02, 600000.0)),
                         asks=((ask, ask_qty), (0.98, 600000.0)),
                         tick=0.01, fetched_at=now))


class Rig:
    def __init__(self, ceiling=100.0, switch=True):
        self.now = 1_000_000.0
        self.exchange = FakeExchange()
        self.cache = BookCache()
        self.switch = switch
        self.alerts = []
        self.desk = OrderDesk(
            client=self.exchange,
            whitelist=lambda s: s.startswith(("scc-senate-gop-", "scc-hrep-rep-")),
            switch_on=lambda: self.switch,
            fresh_book=lambda s: self.cache.fresh(s, 120, self.now),
            log=lambda e: None,
            sleep=lambda s: None, clock=lambda: self.now,
        )
        self.engine = Engine(self.desk, EngineConfig(ceiling_usd=ceiling),
                             alert=lambda t, m: self.alerts.append((t, m)),
                             clock=lambda: self.now)
        self.silver = SilverFairs()
        self.silver.load(REAL_CSV.read_text(), now=self.now)
        self.positions: dict[str, tuple] = {}

    def cycle(self, terms):
        return self.engine.cycle(self.now, self.exchange.open_orders(),
                                 self.positions, self.cache, terms,
                                 self.silver, self.switch)


class TestSwitchAndCeiling(unittest.TestCase):
    def test_switch_off_means_observe_only(self):
        r = Rig(switch=False)
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        s = r.cycle(terms)
        self.assertEqual(s["mode"], "observing")
        self.assertEqual(r.exchange.posts, [])

    def test_places_where_model_and_market_agree(self):
        r = Rig()
        terms = seats_terms([SEN])
        # model ~25.7c, market 20/26 -> mid 23c: tight envelope, earn size
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        s = r.cycle(terms)
        self.assertEqual(s["mode"], "on")
        self.assertGreater(len(s["orders"]), 0)
        self.assertLessEqual(s["used"], 100.0)
        self.assertTrue(any(o["purpose"] == "earn" for o in s["orders"]))

    def test_live_reeval_counts_own_size_once(self):
        # a resting order appears IN the fetched book; re-scoring it as a
        # fresh join counted it twice and halved its share (/orders read
        # $7.84/d while the estimator said $12.27/d for the same books)
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        rec = next(o for o in r.engine.orders.values()
                   if o.side == "BUY" and o.purpose == "earn")
        # the next snapshot carries our order plus one other share at our level
        r.now += 60                          # inside the action cooldown:
        stranger = 1.0                       # re-eval runs, nothing moves
        r.cache.put(SEN, Book(bids=((rec.price, rec.qty + stranger),
                                    (0.02, 600000.0)),
                              asks=((0.14, 30.0), (0.98, 600000.0)),
                              tick=0.01, fetched_at=r.now))
        r.cycle(terms)
        expect = estimate_join("BUY", [(rec.price, stranger), (0.02, 600000.0)],
                               0.01, 0.2, 5000, rec.price, rec.qty)
        pool = 100 / 13 / 2                  # event pool / markets / sides
        self.assertAlmostEqual(rec.live_est, expect.share * pool, places=3)
        # sanity: counted once, our share of the level dwarfs the stranger's
        self.assertGreater(rec.live_est,
                           0.9 * (rec.qty / (rec.qty + stranger)) * pool * 0.2 ** 0)

    def test_disagreement_sends_scouts_not_size(self):
        r = Rig()
        terms = seats_terms([TAIL])
        # model 0.1c vs market ~10c: wide envelope -> 1-share scouts only
        put_book(r.cache, TAIL, 0.09, 0.11, now=r.now)
        s = r.cycle(terms)
        for o in s["orders"]:
            self.assertEqual(o["purpose"], "scout")
            self.assertEqual(o["qty"], 1.0)

    def test_cheap_tail_is_a_ratio_disagreement_not_a_tight_band(self):
        # copula band for this rung is ~[1.9c, 4.4c]; a market at 6/7c makes
        # the envelope under six CENTS wide but more than 3x proportionally —
        # the absolute test alone once sized 400 shares into a tail like
        # this (live, 2026-08-19)
        r = Rig()
        terms = seats_terms([TAIL])
        put_book(r.cache, TAIL, 0.06, 0.07, now=r.now)
        s = r.cycle(terms)
        self.assertTrue(s["orders"])
        for o in s["orders"]:
            self.assertIn(o["purpose"], ("scout", "probe", "exp1"), o)
            self.assertEqual(o["qty"], 1.0)

    def test_an_earning_order_is_resized_when_the_optimum_moves(self):
        """Before 2026-08-19 reprice only fired when an order STOPPED
        earning, and it carried the old size forward — so an earning order
        kept its birth size for life. With every market-side occupied, new
        sizing rules never bit at all: the book sat at $12 an order while
        the ceiling was $300."""
        r = Rig()
        r.engine.cfg.max_order_usd = 3.0      # born small
        r.engine.cfg.size_safety = 1.0
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        born = next(o for o in r.engine.orders.values()
                    if o.side == "BUY" and o.purpose == "earn")
        self.assertLess(born.qty * born.price, 3.5)
        # the cap lifts; the EV optimum is now far above the birth size
        r.engine.cfg.max_order_usd = 75.0
        r.now += 400                          # clear the action cooldown
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        now_resting = [o for o in r.engine.orders.values()
                       if o.side == "BUY" and o.purpose == "earn"]
        self.assertEqual(len(now_resting), 1)   # replaced, not duplicated
        self.assertGreater(now_resting[0].qty, born.qty * 1.5)
        self.assertTrue(any(e.get("event") == "resize"
                            for e in r.engine.log))

    def test_resize_holds_still_when_the_optimum_has_not_moved(self):
        # churn costs queue position; only a material move earns a reprice
        r = Rig()
        r.engine.cfg.size_safety = 1.0
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        before = {o.id: o.qty for o in r.engine.orders.values()}
        for _ in range(3):
            r.now += 400
            put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
            r.cycle(terms)
        after = {o.id: o.qty for o in r.engine.orders.values()}
        kept = set(before) & set(after)
        self.assertTrue(kept, "orders should survive an unchanged book")
        for oid in kept:
            self.assertEqual(before[oid], after[oid])

    def test_size_stops_at_the_ev_peak_not_at_the_cap(self):
        """Owner, 2026-08-19: "at some point, increasing size has no
        marginal earnings benefit on only marginal fill cost, correct?"
        Correct — our share saturates at the whole side pool while fill
        risk stays linear. Improving the touch makes us ~100% of the side
        immediately, so past a small size every extra share is pure risk."""
        r = Rig()
        r.engine.cfg.size_safety = 1.0        # test the peak itself
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        book, prog = r.cache.fresh(SEN, 120, r.now), terms.get(SEN)
        b = r.engine.band(SEN, book, r.silver)
        best = max((c for c in r.engine._candidates(SEN, book, prog, b, r.now)
                    if c["side"] == "BUY"), key=lambda c: c["ev"])
        cap_qty = r.engine.cfg.max_order_usd / best["price"]
        self.assertLess(best["qty"], cap_qty * 0.5,
                        "the cap should not be what decides the size")
        # and it really is a peak: more size is worse, not better
        j_big = estimate_join("BUY", list(book.side("BUY")), book.tick,
                              prog.df, prog.target, best["price"],
                              best["qty"] * 4)
        pool = 100 / 13 / 2
        p_f = r.engine.model.p_fill(SEN, "BUY", j_big.ticks, 86400.0)
        f_c = r.engine.model.fill_cost(SEN, "BUY", best["price"], b[0])
        ev_big = j_big.share * pool - p_f * f_c * best["qty"] * 4
        self.assertLess(ev_big, best["ev"])

    def test_unproven_fill_cost_takes_only_a_fraction_of_the_peak(self):
        # q* scales as 1/sqrt(fill_cost) and fill_cost is still the 2c seed,
        # so until real fills grade it we take half the optimum
        terms = seats_terms([SEN])
        full = Rig(); full.engine.cfg.size_safety = 1.0
        put_book(full.cache, SEN, 0.12, 0.14, now=full.now)
        half = Rig()                          # default 0.5, no graded fills
        put_book(half.cache, SEN, 0.12, 0.14, now=half.now)
        def best(rig):
            book, prog = rig.cache.fresh(SEN, 120, rig.now), terms.get(SEN)
            b = rig.engine.band(SEN, book, rig.silver)
            return max((c for c in rig.engine._candidates(SEN, book, prog, b, rig.now)
                        if c["side"] == "BUY"), key=lambda c: c["ev"])
        self.assertAlmostEqual(best(half)["qty"], best(full)["qty"] / 2, delta=1.0)
        # a family with graded fills behind it gets the full size
        proven = Rig(); proven.engine.cfg.size_safety = 1.0
        proven.engine.model.marks_n["senate-seats"] = 50
        put_book(proven.cache, SEN, 0.12, 0.14, now=proven.now)
        self.assertAlmostEqual(best(proven)["qty"], best(full)["qty"], delta=0.5)

    def test_a_wall_offers_size_but_the_ev_math_still_rules(self):
        """Owner, 2026-08-19: "the size of the walls is also evidence that
        an order won't get filled. That could warrant ramping up spend."
        Depth now opens the size gate on its own — but a wall at our own
        price also dilutes our share of the pool, so the EV bar refuses
        the spot anyway. Both halves matter: the gate opens, the math
        closes it. This is the "not too much on risky decisions" rail
        doing its job."""
        r = Rig()
        terms = seats_terms([TAIL])
        deep = Book(bids=((0.12, 30000.0), (0.02, 600000.0)),
                    asks=((0.14, 30.0), (0.98, 600000.0)),
                    tick=0.01, fetched_at=r.now)
        r.cache.put(TAIL, deep)
        book, prog = r.cache.fresh(TAIL, 120, r.now), terms.get(TAIL)
        b = r.engine.band(TAIL, book, r.silver)
        self.assertFalse(r.engine.band_tight(b[0], b[1]))   # wide: no size by agreement
        # the wall is real and the gate sees it
        self.assertGreaterEqual(
            r.engine._shield(book, "BUY", 0.12),
            r.engine.cfg.shield_size_x * prog.target)
        # ...yet nothing sized survives: our slice of a 30,000 queue is
        # worth pennies while a fill would cost the concession on every share
        for c in r.engine._candidates(TAIL, book, prog, b, r.now):
            if c["side"] == "BUY":
                self.assertEqual(c["qty"], 1.0, c)

    def test_depth_ahead_lowers_the_live_fill_odds(self):
        """The half of the owner's point that always bites: a queue in
        front of an order is evidence against a fill, and the live numbers
        must show it."""
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        rec = next(o for o in r.engine.orders.values()
                   if o.side == "BUY" and o.purpose == "earn")
        # the real book contains our own order; the fixture must too, or
        # subtracting our size erases other people's depth with it
        r.now += 60          # maintenance runs before placement: the live
        r.cache.put(SEN, Book(bids=((rec.price, rec.qty + 30.0),
                                    (0.02, 600000.0)),
                              asks=((0.14, 30.0), (0.98, 600000.0)),
                              tick=0.01, fetched_at=r.now))
        r.cycle(terms)
        thin = rec.live_parts["p_fill"]
        self.assertEqual(rec.live_parts["shield"], 30.0)   # just the thin touch
        # same order, now with a 50,000-contract queue ahead of it
        r.now += 60
        r.cache.put(SEN, Book(bids=((rec.price, rec.qty + 50000.0),
                                    (0.02, 600000.0)),
                              asks=((0.14, 30.0), (0.98, 600000.0)),
                              tick=0.01, fetched_at=r.now))
        r.cycle(terms)
        self.assertEqual(rec.live_parts["shield"], 50000.0)
        self.assertLess(rec.live_parts["p_fill"], thin)
        self.assertGreater(rec.live_parts["p_fill"], 0.0)  # never certainty

    def test_sized_order_withdrawn_when_band_detightens(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)      # tight: earn size
        r.cycle(terms)
        earns = [o for o in r.engine.orders.values() if o.purpose == "earn"]
        self.assertTrue(earns)
        # the market runs away to the tail: band still contains the mid but
        # agreement is gone — the size must come off
        r.now += 400
        put_book(r.cache, SEN, 0.31, 0.33, now=r.now)
        r.cycle(terms)
        left = [o for o in r.engine.orders.values()
                if o.purpose == "earn" and o.id in {e.id for e in earns}]
        self.assertEqual(left, [])
        pulls = [x for x in r.engine.log if x.get("event") == "pull"]
        self.assertTrue(any("tight" in (x.get("why") or "") or
                            "band" in (x.get("why") or "") for x in pulls))

    def test_probe_visits_the_empty_odds_bins(self):
        r = Rig()
        r.engine.cfg.min_ev_day = 999.0        # no normal order clears the bar
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        probes = [o for o in r.engine.orders.values() if o.purpose == "probe"]
        self.assertEqual(len(probes), 1)          # one per cycle, budgeted
        self.assertEqual(probes[0].qty, 1.0)
        fc = r.engine.forecasts[probes[0].id]
        self.assertIsNotNone(fc.get("p_fill"))    # the labeled data point
        # probes rest where they were aimed: unchanged book, same order id
        r.now += 400
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        self.assertIn(probes[0].id, r.engine.orders)

    def test_probe_budget_is_bounded(self):
        SEN2 = "scc-senate-gop-2026-11-03-50"
        r = Rig()
        r.engine.cfg.min_ev_day = 999.0
        r.engine.cfg.probe_max_open = 1
        terms = seats_terms([SEN, SEN2])
        for _ in range(2):
            put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
            put_book(r.cache, SEN2, 0.20, 0.22, now=r.now)
            r.cycle(terms)
            r.now += 400
        probes = [o for o in r.engine.orders.values() if o.purpose == "probe"]
        self.assertLessEqual(len(probes), 1)

    def test_ceiling_binds(self):
        r = Rig(ceiling=0.30)   # 30 cents: a bid scout fits, nothing else
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        s = r.cycle(terms)
        self.assertLessEqual(s["used"], 0.30 + 1e-9)

    def test_overpriced_touch_is_not_bid_when_only_the_model_speaks(self):
        r = Rig()
        terms = seats_terms([SEN])
        # bids only, resting way above the model's 25.7c: band is model-only
        # [15.7c, 35.7c]; a bid at the 50c touch would overpay on any fill
        r.cache.put(SEN, Book(bids=((0.50, 6000.0),), asks=(),
                              tick=0.01, fetched_at=r.now))
        s = r.cycle(terms)
        self.assertFalse(any(o["side"] == "BUY" and o["price"] >= 0.40
                             for o in s["orders"]))


class TestFillsAndSeller(unittest.TestCase):
    def test_fill_detected_by_position_delta_then_resold(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        bid = next(o for o in r.engine.orders.values() if o.side == "BUY")
        # the exchange fills our bid: order gone, position appears
        r.exchange.live.pop(bid.id)
        r.positions = {SEN: (bid.qty, round(bid.price * bid.qty, 2))}
        r.now += 400
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        s = r.cycle(terms)
        self.assertTrue(any("Order filled" in t for t, _ in r.alerts))
        sells = [o for o in s["orders"] if o["purpose"] == "sell"]
        self.assertEqual(len(sells), 1)
        # listed at max(break-even + tick, the ask touch); here the touch
        self.assertAlmostEqual(sells[0]["price"], 0.14)
        self.assertAlmostEqual(sells[0]["qty"], bid.qty)
        # and the NEXT pass reads what the waiting stock earns (owner,
        # 2026-08-20: "how much the stock that is being sold is earning
        # per day?") — an ask at the touch is inside the window here
        r.now += 400
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        s = r.cycle(terms)
        sells = [o for o in s["orders"] if o["purpose"] == "sell"]
        self.assertIsNotNone(sells[0]["live_est"])
        self.assertGreater(sells[0]["live_est"], 0.0)
        self.assertTrue(sells[0]["live_parts"].get("exit"))

    def test_account_positions_are_not_adopted_as_our_inventory(self):
        # The account is shared with 1.0, which holds seats stock of its
        # own. None of it belongs inside 2.0's ceiling, and the seller
        # must never act on it. (This happened: $34 of 1.0's positions
        # appeared as 2.0's "used" on day one.)
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.positions = {SEN: (17.0, 0.95),
                       "scc-senate-gop-2026-11-03-51": (-27.0, 23.64)}
        s = r.cycle(terms)
        self.assertEqual(r.engine.inventory, {})
        self.assertFalse(any(o["purpose"] in ("sell", "close")
                             for o in s["orders"]))
        # used counts only our own resting orders
        own = sum(0 if o["side"] == "SELL" else o["price"] * o["qty"]
                  for o in s["orders"])
        self.assertLessEqual(s["used"], own + 25.0)

    def test_own_fill_builds_inventory_from_the_ledger(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        # a pre-existing 1.0 position sits in the market the whole time
        r.positions = {SEN: (100.0, 20.0)}
        r.cycle(terms)
        bid = next(o for o in r.engine.orders.values() if o.side == "BUY")
        r.exchange.live.pop(bid.id)
        # the position grows by exactly our fill
        r.positions = {SEN: (100.0 + bid.qty, 20.0 + bid.price * bid.qty)}
        r.now += 400
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        inv = r.engine.inventory[SEN]
        self.assertAlmostEqual(inv["qty"], bid.qty)
        self.assertAlmostEqual(inv["cost"], round(bid.price * bid.qty, 4), places=4)

    def test_vanish_without_delta_is_a_silent_cancel_not_a_fill(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        victim = next(iter(r.engine.orders.values()))
        r.exchange.live.pop(victim.id)
        r.now += 400
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        self.assertEqual(r.engine.silent_cancels, 1)
        self.assertFalse(any("Order filled" in t for t, _ in r.alerts))


class TestExitsAndMaintenance(unittest.TestCase):
    def test_dead_program_pulls_our_orders(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        self.assertGreater(len(r.engine.orders), 0)
        # the market's program closes
        terms.refresh({SEN: {"timePeriods": []}}, {}, now=r.now)
        r.now += 400
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        s = r.cycle(terms)
        self.assertEqual(len(s["orders"]), 0)

    def test_cooldown_stops_churn(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        n_posts = len(r.exchange.posts)
        r.now += 30      # well inside the 300s cooldown
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        self.assertEqual(len(r.exchange.posts), n_posts)


class TestExp1(unittest.TestCase):
    def test_boundary_placements_become_scout_experiments(self):
        r = Rig()
        terms = seats_terms([SEN])
        # 6000 resting at the 15c touch (inside the model band, so the
        # information is cheap) vs 5000 target, ask one tick above:
        # improving would cross, deeper is out of window, and joining the
        # fat level is EV-negative at size — pure EV would never test the
        # boundary. The information budget places a 1-share scout instead.
        put_book(r.cache, SEN, 0.15, 0.16, bid_qty=6000.0, now=r.now)
        r.cycle(terms)
        joined = [o for o in r.engine.orders.values()
                  if o.side == "BUY" and abs(o.price - 0.15) < 1e-9]
        self.assertEqual(len(joined), 1)
        self.assertEqual(joined[0].purpose, "exp1")
        self.assertEqual(joined[0].qty, 1.0)
        self.assertGreater(len(r.engine.exp1), 0)
        for row in r.engine.exp1:
            self.assertEqual(row["pred_queue_day"], 0.0)
            self.assertGreater(row["pred_level_day"], 0.0)
        # and the forecast for it is on the record
        f = r.engine.forecasts[joined[0].id]
        self.assertEqual(f["purpose"], "exp1")
        self.assertGreater(f["p_fill"], 0.0)


def foreign(oid, intent, market=SEN, price=0.10, size=45.0, manual=False,
            created=""):
    from v2.intents import REST_SIDE
    return {"id": oid, "market": market, "side": REST_SIDE[intent],
            "price": price, "size": size, "intent": intent, "manual": manual,
            "created": created}


def iso_ago(now, seconds):
    import datetime as dt
    return dt.datetime.fromtimestamp(now - seconds, tz=dt.timezone.utc).isoformat()


class TestHandoverSweep(unittest.TestCase):
    def test_clears_opening_orders_keeps_exits_even_with_switch_off(self):
        from v2.intents import BUY_LONG, BUY_SHORT, SELL_SHORT
        r = Rig(switch=False)
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.exchange.live["f1"] = foreign("f1", BUY_LONG, price=0.19)
        r.exchange.live["f2"] = foreign("f2", BUY_SHORT, price=0.30)
        r.exchange.live["f3"] = foreign("f3", SELL_LONG, price=0.27)
        r.exchange.live["f4"] = foreign("f4", SELL_SHORT, price=0.18)
        r.cycle(terms)
        live = set(r.exchange.live)
        self.assertNotIn("f1", live)    # opening bid: cleared
        self.assertNotIn("f2", live)    # opening short: cleared
        self.assertIn("f3", live)       # exit ask: left to finish
        self.assertIn("f4", live)       # short buy-back: left to finish
        self.assertEqual(r.engine.sweep_count, 2)
        self.assertFalse(r.engine.family_sweep_done)   # done on the clean pass
        # switch off: nothing was PLACED
        self.assertFalse(any(u.endswith("/v1/orders") for u, _ in r.exchange.posts))
        r.now += 60
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        self.assertTrue(r.engine.family_sweep_done)
        self.assertTrue(any("Seats handover done" in t for t, _ in r.alerts))

    def test_sweep_respects_the_per_cycle_budget(self):
        from v2.intents import BUY_LONG
        r = Rig(switch=False)
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        for i in range(20):
            r.exchange.live[f"f{i}"] = foreign(f"f{i}", BUY_LONG, price=0.19)
        r.cycle(terms)
        self.assertEqual(r.engine.sweep_count, 8)      # 8 per cycle, no burst
        r.now += 60
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        self.assertEqual(r.engine.sweep_count, 16)

    def test_after_handover_automation_is_evicted_but_manual_orders_stay(self):
        from v2.intents import BUY_LONG
        r = Rig(switch=True)
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)                                  # sweep completes (no foreign)
        self.assertTrue(r.engine.family_sweep_done)
        r.exchange.live["bot"] = foreign("bot", BUY_LONG, price=0.19,
                                         created=iso_ago(r.now, 3600))
        r.exchange.live["hand"] = foreign("hand", BUY_LONG, price=0.18, manual=True,
                                          created=iso_ago(r.now, 3600))
        r.now += 400
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        self.assertNotIn("bot", r.exchange.live)
        self.assertIn("hand", r.exchange.live)
        self.assertTrue(any(e.get("event") == "foreign_manual_order"
                            for e in r.engine.log))

    def test_fresh_foreign_orders_get_rollover_grace(self):
        # The 2026-08-19 twin fight: during a deploy rollover the other
        # instance's just-placed orders looked foreign and were evicted,
        # and it evicted ours back. Inside the grace window nothing moves.
        from v2.intents import BUY_LONG
        r = Rig(switch=True)
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        r.exchange.live["twin"] = foreign("twin", BUY_LONG, price=0.19,
                                          created=iso_ago(r.now, 60))
        r.exchange.live["nodate"] = foreign("nodate", BUY_LONG, price=0.17)
        r.now += 400
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        self.assertIn("twin", r.exchange.live)      # too young to evict
        self.assertIn("nodate", r.exchange.live)    # unknown age: never evict


class TestRotation(unittest.TestCase):
    def test_worst_holding_is_freed_for_a_decisively_better_idea(self):
        SEN2 = "scc-senate-gop-2026-11-03-50"
        r = Rig(ceiling=13.0)
        r.engine.cfg.max_order_usd = 12.0   # this test is about rotation, not
        r.engine.cfg.size_safety = 1.0      # sizing: pin both so the sizing
                                            # rules can't quietly break it
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)                       # ~$12 lands in SEN
        self.assertTrue(any(o.purpose == "earn"
                            for o in r.engine.orders.values()))
        # SEN's book gets crowded on both sides (our spot dilutes to
        # crumbs) while a thin, juicy book appears in SEN2 — unaffordable
        # at $1 headroom
        terms = seats_terms([SEN, SEN2])
        r.now += 400
        put_book(r.cache, SEN, 0.12, 0.14, bid_qty=6000.0, ask_qty=6000.0,
                 now=r.now)
        put_book(r.cache, SEN2, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        self.assertTrue(any(e.get("event") == "rotate_out"
                            and e.get("for_market") == SEN2
                            for e in r.engine.log))
        self.assertFalse(any(o.market == SEN and o.purpose == "earn"
                             for o in r.engine.orders.values()))


class TestPersistence(unittest.TestCase):
    def test_engine_state_roundtrip(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        r.engine.inventory[SEN] = {"qty": 5.0, "cost": 1.0}   # own ledger
        e2 = Engine(r.desk, r.engine.cfg, clock=lambda: r.now)
        e2.restore(r.engine.to_dict())
        self.assertEqual(set(e2.orders), set(r.engine.orders))
        self.assertEqual(e2.last_action, r.engine.last_action)
        self.assertEqual(e2.inventory, r.engine.inventory)    # ledger_v 2 kept

    def test_pre_migration_inventory_is_dropped_and_its_orders_pulled(self):
        # State written by the build that adopted the account's positions:
        # inventory full of 1.0's stock, sell/close orders resting on it.
        r = Rig(switch=True)
        old = {
            "orders": {"s1": {"id": "s1", "market": SEN, "side": "SELL",
                              "price": 0.20, "qty": 17.0, "intent": SELL_LONG,
                              "placed_ts": 1.0, "purpose": "sell"}},
            "inventory": {SEN: {"qty": 17.0, "cost": 0.95}},
            "family_sweep_done": True, "sweep_count": 31,
        }
        r.engine.restore(old)
        self.assertEqual(r.engine.inventory, {})              # dropped
        self.assertTrue(any(e.get("event") == "ledger_reset"
                            for e in r.engine.log))
        # the orphaned sell order rests on the exchange; next cycle pulls it
        r.exchange.live["s1"] = foreign("s1", SELL_LONG, price=0.20, size=17.0)
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.12, 0.14, now=r.now)
        r.cycle(terms)
        self.assertNotIn("s1", r.exchange.live)
        self.assertNotIn("s1", r.engine.orders)
        self.assertTrue(any(e.get("event") == "orphan_exit_pulled"
                            for e in r.engine.log))


if __name__ == "__main__":
    unittest.main()
