"""The floor handshake: want -> halt+ack -> act; every failure mode waits."""

import os
import tempfile
import unittest

from v3 import floor


class TestFloor(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        os.environ["V3_FLOOR_PATH"] = os.path.join(self.dir.name, "f.json")
        os.environ["V1_ACK_PATH"] = os.path.join(self.dir.name, "a1.json")
        os.environ["V2_ACK_PATH"] = os.path.join(self.dir.name, "a2.json")

    def tearDown(self):
        for k in ("V3_FLOOR_PATH", "V1_ACK_PATH", "V2_ACK_PATH"):
            os.environ.pop(k, None)
        self.dir.cleanup()

    def test_no_acks_means_wait(self):
        f = floor.Floor(clock=lambda: 1000.0)
        f.write_want(True)
        self.assertFalse(f.acked())

    def test_both_fresh_acks_release(self):
        f = floor.Floor(clock=lambda: 1000.0)
        f.write_want(True)
        floor.ack("v1", True, clock=lambda: 990.0)
        self.assertFalse(f.acked())              # one ack is not enough
        floor.ack("v2", True, clock=lambda: 995.0)
        self.assertTrue(f.acked())

    def test_stale_ack_means_wait(self):
        f = floor.Floor(clock=lambda: 2000.0)
        floor.ack("v1", True, clock=lambda: 1000.0)   # 1000s old
        floor.ack("v2", True, clock=lambda: 1995.0)
        self.assertFalse(f.acked())

    def test_unhalted_ack_means_wait(self):
        f = floor.Floor(clock=lambda: 1000.0)
        floor.ack("v1", True, clock=lambda: 999.0)
        floor.ack("v2", False, clock=lambda: 999.0)
        self.assertFalse(f.acked())

    def test_want_is_honoured_even_when_stale(self):
        f = floor.Floor(clock=lambda: 1000.0)
        f.write_want(True)
        want, age = floor.wanted(now=99999.0)
        self.assertTrue(want)                    # 1.0 stays halted
        self.assertGreater(age, floor.STALE_ALERT_S)

    def test_release_and_status(self):
        f = floor.Floor(clock=lambda: 1000.0)
        f.write_want(True)
        floor.ack("v1", True, clock=lambda: 999.0)
        floor.ack("v2", True, clock=lambda: 999.0)
        st = f.status()
        self.assertTrue(st["acked"] and st["want"])
        f.write_want(False)
        self.assertFalse(floor.wanted(now=1000.0)[0])

    def test_missing_files_are_calm(self):
        self.assertEqual(floor.wanted(now=1.0), (False, float("inf")))
        self.assertFalse(floor.Floor(clock=lambda: 1.0).acked())


if __name__ == "__main__":
    unittest.main()
