"""The survey exists because pool size is the wrong question.

Owner, 2026-08-31: "We're getting a high share with low order size
(risk). So that wouldn't quite be an apples to apples comparison." A
$50 probe would have flattered NBA, where $50 buys far more shares than
in a 30c politics market. The measure is share of a side per dollar at
risk, priced at the size we actually use.
"""

import unittest

from v3.programs import Program
from v3.scoring import Book
from v3.survey import (LIVE_BUFFER_S, PrefixStat, Sampler,
                       is_live_event, kind_of, leaderboard,
                       probe_side, summarise, to_csv)


def book(bids, asks, tick=0.01):
    return Book(bids=tuple(bids), asks=tuple(asks), tick=tick,
                fetched_at=1000.0)


class TestKind(unittest.TestCase):
    def test_the_kind_is_everything_before_the_date(self):
        self.assertEqual(kind_of("aachc-cfb-wins-2026-11-28-txst-5pt5wins"),
                         "aachc-cfb-wins")
        self.assertEqual(kind_of("tec-nba-westconf-2027-05-29-w-uta"),
                         "tec-nba-westconf")
        self.assertEqual(kind_of("aqc-nfl-2027-01-10-playoffq-ari"), "aqc-nfl")

    def test_a_slug_with_no_date_is_its_own_kind(self):
        self.assertEqual(kind_of("enwc-uspres-nom-rep-elomus"),
                         "enwc-uspres-nom-rep-elomus")


class TestProbe(unittest.TestCase):
    """A thin touch behind a qualifying wall is the cfb shape; a fat
    touch is NBA's, however rich the pool."""

    def test_a_thin_touch_behind_a_wall_takes_a_real_share(self):
        # 6 shares at the touch, a 20k wall out at 99c carrying the side
        # over Target Size — one share should be worth a large slice
        b = book(bids=[(0.30, 6.0), (0.29, 4.0), (0.01, 20000.0)], asks=[])
        prog = Program(pool=100.0, target=7500.0, df=0.25, event_n=2)
        p = probe_side(b, prog, "BUY", side_pool=25.0)
        self.assertTrue(p.qualifies, p.note)
        self.assertEqual(p.touch_size, 6.0)
        self.assertGreater(p.share, 0.05)
        # and it cost 30 cents to get it
        self.assertAlmostEqual(p.risk_usd, 0.30, places=4)
        self.assertGreater(p.share_per_dollar, 0.15)

    def test_a_fat_touch_takes_almost_nothing_however_rich_the_pool(self):
        # NBA's shape: the same probe against 500k resting at the touch
        b = book(bids=[(0.30, 500_000.0)], asks=[])
        prog = Program(pool=200.0, target=10000.0, df=0.25, event_n=1)
        p = probe_side(b, prog, "BUY", side_pool=100.0)
        self.assertTrue(p.qualifies)
        self.assertLess(p.share, 0.001)
        # the pool is FOUR TIMES richer and the order is worth far less
        self.assertLess(p.est_day, 0.25)

    def test_a_side_under_target_size_pays_nobody(self):
        b = book(bids=[(0.30, 6.0)], asks=[])
        prog = Program(pool=100.0, target=7500.0, df=0.25, event_n=1)
        p = probe_side(b, prog, "BUY", side_pool=50.0)
        self.assertFalse(p.qualifies)
        self.assertEqual(p.share, 0.0)
        self.assertEqual(p.est_day, 0.0)
        self.assertIn("Target Size", p.note)

    def test_an_empty_side_is_reported_not_crashed(self):
        p = probe_side(book(bids=[], asks=[(0.5, 3.0)]), Program(pool=1.0, target=1.0, df=0.5),
                       "BUY", side_pool=1.0)
        self.assertEqual(p.note, "side is empty")
        self.assertEqual(p.share_per_dollar, 0.0)

    def test_near_size_counts_only_what_scores(self):
        b = book(bids=[(0.30, 5.0), (0.29, 7.0), (0.10, 900.0)], asks=[])
        p = probe_side(b, Program(pool=10.0, target=1.0, df=0.5, event_n=1),
                       "BUY", side_pool=5.0)
        self.assertEqual(p.touch_size, 5.0)
        self.assertEqual(p.near_size, 12.0)      # the 10c pile is far back
        self.assertEqual(p.total_size, 912.0)


class TestReport(unittest.TestCase):
    def test_kinds_rank_by_share_per_dollar_not_by_pool(self):
        rows = [
            {"kind": "fat-pool", "qualifies": 1, "share_pct": 0.02,
             "est_day_usd": 0.01, "share_per_dollar": 0.06},
            {"kind": "thin-touch", "qualifies": 1, "share_pct": 13.0,
             "est_day_usd": 0.98, "share_per_dollar": 31.0},
        ]
        out = summarise(rows)["kinds"]
        self.assertEqual(out[0]["kind"], "thin-touch")

    def test_csv_has_a_header_and_survives_commas(self):
        b = book(bids=[(0.30, 6.0)], asks=[])
        r = probe_side(b, Program(pool=1.0, target=1.0, df=0.5, event_n=1),
                       "BUY", 1.0).row("a,b", "kind")
        text = to_csv([r])
        self.assertTrue(text.startswith("market,kind,side,"))
        self.assertEqual(len(text.strip().split("\n")), 2)
        self.assertNotIn("a,b", text)            # the comma was neutralised


class TestLiveEvents(unittest.TestCase):
    """Owner, 2026-08-31: "we'll probably want to stay out of live
    events until I have a way of quoting them better." Re-checked every
    pass, because a market that is quiet in the morning goes live at
    kickoff."""

    NOW = 1_788_200_000.0

    def test_a_game_already_started_is_live(self):
        self.assertTrue(is_live_event(
            {"gameStartTime": self.NOW - 600}, self.NOW))

    def test_the_hour_before_kickoff_is_live_too(self):
        self.assertTrue(is_live_event(
            {"gameStartTime": self.NOW + 600}, self.NOW))
        self.assertFalse(is_live_event(
            {"gameStartTime": self.NOW + LIVE_BUFFER_S + 60}, self.NOW))

    def test_a_market_with_no_game_never_goes_live(self):
        # futures and politics trade the same way all day
        self.assertFalse(is_live_event({"slug": "x"}, self.NOW))
        self.assertFalse(is_live_event({"gameStartTime": None}, self.NOW))
        self.assertFalse(is_live_event({}, self.NOW))

    def test_it_reads_the_exchanges_time_formats(self):
        iso = "2026-09-01T00:00:00Z"
        self.assertFalse(is_live_event({"gameStartTime": iso}, 1_788_100_000.0))
        self.assertTrue(is_live_event({"gameStartTime": iso}, 1_788_300_000.0))
        # milliseconds, as some feeds send
        self.assertTrue(is_live_event(
            {"gameStartTime": self.NOW * 1000}, self.NOW))
        # junk is not a reason to skip a market
        self.assertFalse(is_live_event({"gameStartTime": "soon"}, self.NOW))


class TestSampling(unittest.TestCase):
    """The guarantee he asked for: random within prefix, every prefix
    gets its turn, seeded so a run can be audited."""

    def pop(self):
        return (["big-2026-01-01-%d" % i for i in range(200)]
                + ["small-2026-01-01-%d" % i for i in range(3)])

    def test_a_tiny_prefix_is_sampled_as_often_as_a_huge_one(self):
        # uniform over MARKETS would draw 'small' about 1 time in 68
        s = Sampler(seed=1)
        s.load(self.pop())
        got = s.next_batch(20)
        n_small = sum(1 for x in got if x.startswith("small"))
        self.assertGreaterEqual(n_small, 9, "round robin should alternate")

    def test_the_draw_within_a_prefix_is_not_the_api_order(self):
        s = Sampler(seed=7)
        s.load(self.pop())
        got = [x for x in s.next_batch(40) if x.startswith("big")]
        in_order = ["big-2026-01-01-%d" % i for i in range(len(got))]
        self.assertNotEqual(got, in_order)

    def test_no_market_repeats_until_its_prefix_is_exhausted(self):
        s = Sampler(seed=3)
        s.load(["small-2026-01-01-%d" % i for i in range(3)])
        first = s.next_batch(3)
        self.assertEqual(len(set(first)), 3, "drew the same market twice")

    def test_the_same_seed_reproduces_the_run(self):
        a, b = Sampler(seed=42), Sampler(seed=42)
        a.load(self.pop())
        b.load(self.pop())
        self.assertEqual(a.next_batch(25), b.next_batch(25))
        c = Sampler(seed=43)
        c.load(self.pop())
        self.assertNotEqual(a.next_batch(25), c.next_batch(25))

    def test_the_state_reports_the_seed_and_the_frame(self):
        s = Sampler(seed=99)
        s.load(self.pop())
        st = s.state()
        self.assertEqual(st["seed"], 99)
        self.assertEqual(st["population"], 203)
        self.assertEqual(st["prefixes"], 2)


class TestLeaderboard(unittest.TestCase):
    def probe(self, share, risk):
        p = probe_side(book(bids=[(risk, 50.0)], asks=[]),
                       Program(pool=1.0, target=1.0, df=0.5, event_n=1),
                       "BUY", 1.0)
        p.share, p.risk_usd, p.qualifies = share, risk, True
        return p

    def test_a_prefix_is_not_ranked_on_too_few_samples(self):
        st = PrefixStat(prefix="lucky")
        st.record(self.probe(0.14, 0.47), 1000.0)     # the AFC South outlier
        out = leaderboard({"lucky": st}, min_samples=12)
        self.assertEqual(out["ranked"], [])
        self.assertEqual(out["sampling"][0]["prefix"], "lucky")

    def test_ranking_uses_the_median_not_the_max(self):
        st = PrefixStat(prefix="mixed")
        for _ in range(14):
            st.record(self.probe(0.0001, 0.5), 1000.0)   # mostly awful
        st.record(self.probe(0.90, 0.01), 1000.0)        # one jackpot
        row = leaderboard({"mixed": st}, min_samples=12)["ranked"][0]
        self.assertLess(row["median_spd"], 1.0, "a single outlier won")

    def test_old_samples_fall_out_of_the_window(self):
        st = PrefixStat(prefix="drifty")
        for _ in range(PrefixStat.KEEP + 30):
            st.record(self.probe(0.5, 0.5), 1000.0)
        self.assertEqual(len(st.spd), PrefixStat.KEEP)


if __name__ == "__main__":
    unittest.main()
