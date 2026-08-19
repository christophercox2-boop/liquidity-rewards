"""Engine tests: the full chain through the real OrderDesk rails against
a fake exchange that actually rests and cancels orders."""

import unittest
from pathlib import Path

from v2.books import BookCache
from v2.engine import Engine, EngineConfig
from v2.intents import REST_SIDE, SELL_LONG
from v2.orders import OrderDesk
from v2.scoring import Book
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
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        s = r.cycle(terms)
        self.assertEqual(s["mode"], "observing")
        self.assertEqual(r.exchange.posts, [])

    def test_places_where_model_and_market_agree(self):
        r = Rig()
        terms = seats_terms([SEN])
        # model ~25.7c, market 20/26 -> mid 23c: tight envelope, earn size
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        s = r.cycle(terms)
        self.assertEqual(s["mode"], "on")
        self.assertGreater(len(s["orders"]), 0)
        self.assertLessEqual(s["used"], 100.0)
        self.assertTrue(any(o["purpose"] == "earn" for o in s["orders"]))

    def test_disagreement_sends_scouts_not_size(self):
        r = Rig()
        terms = seats_terms([TAIL])
        # model 0.1c vs market ~10c: wide envelope -> 1-share scouts only
        put_book(r.cache, TAIL, 0.09, 0.11, now=r.now)
        s = r.cycle(terms)
        for o in s["orders"]:
            self.assertEqual(o["purpose"], "scout")
            self.assertEqual(o["qty"], 1.0)

    def test_ceiling_binds(self):
        r = Rig(ceiling=0.30)   # 30 cents: a bid scout fits, nothing else
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
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
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        bid = next(o for o in r.engine.orders.values() if o.side == "BUY")
        # the exchange fills our bid: order gone, position appears
        r.exchange.live.pop(bid.id)
        r.positions = {SEN: (bid.qty, round(bid.price * bid.qty, 2))}
        r.now += 400
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        s = r.cycle(terms)
        self.assertTrue(any("Order filled" in t for t, _ in r.alerts))
        sells = [o for o in s["orders"] if o["purpose"] == "sell"]
        self.assertEqual(len(sells), 1)
        # listed at max(break-even + tick, the ask touch); here the touch
        self.assertAlmostEqual(sells[0]["price"], 0.26)
        self.assertAlmostEqual(sells[0]["qty"], bid.qty)

    def test_account_positions_are_not_adopted_as_our_inventory(self):
        # The account is shared with 1.0, which holds seats stock of its
        # own. None of it belongs inside 2.0's ceiling, and the seller
        # must never act on it. (This happened: $34 of 1.0's positions
        # appeared as 2.0's "used" on day one.)
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
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
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        # a pre-existing 1.0 position sits in the market the whole time
        r.positions = {SEN: (100.0, 20.0)}
        r.cycle(terms)
        bid = next(o for o in r.engine.orders.values() if o.side == "BUY")
        r.exchange.live.pop(bid.id)
        # the position grows by exactly our fill
        r.positions = {SEN: (100.0 + bid.qty, 20.0 + bid.price * bid.qty)}
        r.now += 400
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        inv = r.engine.inventory[SEN]
        self.assertAlmostEqual(inv["qty"], bid.qty)
        self.assertAlmostEqual(inv["cost"], round(bid.price * bid.qty, 4), places=4)

    def test_vanish_without_delta_is_a_silent_cancel_not_a_fill(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        victim = next(iter(r.engine.orders.values()))
        r.exchange.live.pop(victim.id)
        r.now += 400
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        self.assertEqual(r.engine.silent_cancels, 1)
        self.assertFalse(any("Order filled" in t for t, _ in r.alerts))


class TestExitsAndMaintenance(unittest.TestCase):
    def test_dead_program_pulls_our_orders(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        self.assertGreater(len(r.engine.orders), 0)
        # the market's program closes
        terms.refresh({SEN: {"timePeriods": []}}, {}, now=r.now)
        r.now += 400
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        s = r.cycle(terms)
        self.assertEqual(len(s["orders"]), 0)

    def test_cooldown_stops_churn(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        n_posts = len(r.exchange.posts)
        r.now += 30      # well inside the 300s cooldown
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        self.assertEqual(len(r.exchange.posts), n_posts)


class TestExp1(unittest.TestCase):
    def test_boundary_placements_become_scout_experiments(self):
        r = Rig()
        terms = seats_terms([SEN])
        # 6000 resting at the 25c touch vs 5000 target, ask one tick above:
        # improving would cross, deeper is out of window, and joining the
        # fat level is EV-negative at size — pure EV would never test the
        # boundary. The information budget places a 1-share scout instead.
        put_book(r.cache, SEN, 0.25, 0.26, bid_qty=6000.0, now=r.now)
        r.cycle(terms)
        joined = [o for o in r.engine.orders.values()
                  if o.side == "BUY" and abs(o.price - 0.25) < 1e-9]
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


def foreign(oid, intent, market=SEN, price=0.10, size=45.0, manual=False):
    from v2.intents import REST_SIDE
    return {"id": oid, "market": market, "side": REST_SIDE[intent],
            "price": price, "size": size, "intent": intent, "manual": manual}


class TestHandoverSweep(unittest.TestCase):
    def test_clears_opening_orders_keeps_exits_even_with_switch_off(self):
        from v2.intents import BUY_LONG, BUY_SHORT, SELL_SHORT
        r = Rig(switch=False)
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
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
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        self.assertTrue(r.engine.family_sweep_done)
        self.assertTrue(any("Seats handover done" in t for t, _ in r.alerts))

    def test_sweep_respects_the_per_cycle_budget(self):
        from v2.intents import BUY_LONG
        r = Rig(switch=False)
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        for i in range(20):
            r.exchange.live[f"f{i}"] = foreign(f"f{i}", BUY_LONG, price=0.19)
        r.cycle(terms)
        self.assertEqual(r.engine.sweep_count, 8)      # 8 per cycle, no burst
        r.now += 60
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        self.assertEqual(r.engine.sweep_count, 16)

    def test_after_handover_automation_is_evicted_but_manual_orders_stay(self):
        from v2.intents import BUY_LONG
        r = Rig(switch=True)
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)                                  # sweep completes (no foreign)
        self.assertTrue(r.engine.family_sweep_done)
        r.exchange.live["bot"] = foreign("bot", BUY_LONG, price=0.19)
        r.exchange.live["hand"] = foreign("hand", BUY_LONG, price=0.18, manual=True)
        r.now += 400
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        self.assertNotIn("bot", r.exchange.live)
        self.assertIn("hand", r.exchange.live)
        self.assertTrue(any(e.get("event") == "foreign_manual_order"
                            for e in r.engine.log))


class TestPersistence(unittest.TestCase):
    def test_engine_state_roundtrip(self):
        r = Rig()
        terms = seats_terms([SEN])
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
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
        put_book(r.cache, SEN, 0.20, 0.26, now=r.now)
        r.cycle(terms)
        self.assertNotIn("s1", r.exchange.live)
        self.assertNotIn("s1", r.engine.orders)
        self.assertTrue(any(e.get("event") == "orphan_exit_pulled"
                            for e in r.engine.log))


if __name__ == "__main__":
    unittest.main()
