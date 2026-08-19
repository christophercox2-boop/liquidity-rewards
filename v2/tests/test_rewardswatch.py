"""The rewards watcher: alert on new postings, never on old news."""

import unittest

from v2.api import ApiError
from v2.rewardswatch import CHECK_S, RewardsWatch, _signature


def row(date, usd, status="PENDING", market="m1"):
    return {"date": date, "market": market, "program_type": "liquidityProgram",
            "reward_usd": usd, "status": status}


class FakeClient:
    def __init__(self):
        self.rows = []
        self.calls = 0
        self.raise_next = None

    def earnings(self, start_date):
        self.calls += 1
        if self.raise_next:
            e, self.raise_next = self.raise_next, None
            raise e
        return list(self.rows)


class Recorder:
    def __init__(self):
        self.sent = []

    def __call__(self, title, message, priority="default"):
        self.sent.append((title, message))
        return True


class TestSignature(unittest.TestCase):
    def test_integer_cents_per_day(self):
        sig = _signature([row("2026-08-16", 0.1), row("2026-08-16", 0.2, "PAID"),
                          row("2026-08-17", 1.0)])
        self.assertEqual(sig["2026-08-16"], [2, 30, 20])
        self.assertEqual(sig["2026-08-17"], [1, 100, 0])


class TestWatch(unittest.TestCase):
    def setUp(self):
        self.t = [1000.0]
        self.client = FakeClient()
        self.notify = Recorder()
        self.w = RewardsWatch(clock=lambda: self.t[0])

    def tick(self):
        self.t[0] += CHECK_S + 1

    def test_first_check_baselines_silently(self):
        self.client.rows = [row("2026-08-16", 197.03)]
        self.assertFalse(self.w.check(self.client, self.notify))
        self.assertEqual(self.notify.sent, [])
        self.assertTrue(self.w.primed)

    def test_no_change_no_alert_and_rate_limited(self):
        self.client.rows = [row("2026-08-16", 197.03)]
        self.w.check(self.client, self.notify)
        self.w.check(self.client, self.notify)     # within CHECK_S: no fetch
        self.assertEqual(self.client.calls, 1)
        self.tick()
        self.assertFalse(self.w.check(self.client, self.notify))
        self.assertEqual(self.notify.sent, [])

    def test_new_day_posts_alert(self):
        self.client.rows = [row("2026-08-16", 197.03)]
        self.w.check(self.client, self.notify)
        self.client.rows += [row("2026-08-17", 150.0), row("2026-08-17", 51.55, market="m2")]
        self.tick()
        self.assertTrue(self.w.check(self.client, self.notify))
        title, msg = self.notify.sent[-1]
        self.assertEqual(title, "Rewards posted")
        self.assertIn("2026-08-17", msg)
        self.assertIn("$201.55", msg)
        self.assertIn("2 markets", msg)

    def test_pending_to_paid_alerts_as_paid(self):
        self.client.rows = [row("2026-08-16", 197.03)]
        self.w.check(self.client, self.notify)
        self.client.rows = [row("2026-08-16", 197.03, "PAID")]
        self.tick()
        self.assertTrue(self.w.check(self.client, self.notify))
        title, msg = self.notify.sent[-1]
        self.assertEqual(title, "Rewards paid")
        self.assertIn("$197.03 marked paid", msg)

    def test_growing_day_shows_the_growth(self):
        self.client.rows = [row("2026-08-16", 100.0)]
        self.w.check(self.client, self.notify)
        self.client.rows = [row("2026-08-16", 100.0), row("2026-08-16", 25.5, market="m2")]
        self.tick()
        self.w.check(self.client, self.notify)
        _, msg = self.notify.sent[-1]
        self.assertIn("+$25.50", msg)

    def test_day_leaving_window_is_not_news(self):
        self.client.rows = [row("2026-08-01", 50.0), row("2026-08-16", 100.0)]
        self.w.check(self.client, self.notify)
        self.client.rows = [row("2026-08-16", 100.0)]   # old day rolled out
        self.tick()
        self.assertFalse(self.w.check(self.client, self.notify))

    def test_api_error_is_held_not_fatal(self):
        self.client.rows = [row("2026-08-16", 100.0)]
        self.w.check(self.client, self.notify)
        self.client.raise_next = ApiError("boom")
        self.tick()
        self.assertFalse(self.w.check(self.client, self.notify))
        self.assertIn("boom", self.w.last_err)
        self.tick()
        self.assertFalse(self.w.check(self.client, self.notify))  # unchanged data
        self.assertEqual(self.w.last_err, "")

    def test_restart_neither_realerts_nor_misses(self):
        self.client.rows = [row("2026-08-16", 100.0)]
        self.w.check(self.client, self.notify)
        # container restart: state round-trips, new data arrived while down
        w2 = RewardsWatch.from_dict(self.w.to_dict(), clock=lambda: self.t[0])
        self.client.rows += [row("2026-08-17", 60.0)]
        self.tick()
        self.assertTrue(w2.check(self.client, self.notify))
        self.assertIn("2026-08-17", self.notify.sent[-1][1])
        # and the same data again after another round trip: silence
        w3 = RewardsWatch.from_dict(w2.to_dict(), clock=lambda: self.t[0])
        self.tick()
        self.assertFalse(w3.check(self.client, self.notify))

    def test_status_reads_the_latest_day(self):
        self.client.rows = [row("2026-08-16", 197.03), row("2026-08-15", 1352.63, "PAID")]
        self.w.check(self.client, self.notify)
        st = self.w.status()
        self.assertEqual(st["latest_day"], "2026-08-16")
        self.assertEqual(st["latest_usd"], 197.03)
        self.assertEqual(st["latest_paid_usd"], 0.0)
        self.assertEqual(st["err"], "")


if __name__ == "__main__":
    unittest.main()
