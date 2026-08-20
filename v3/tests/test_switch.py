"""Tests for the master switch and its web route."""

import http.client
import json
import unittest

from v3.switch import MasterSwitch
from v3.web import WebServer


class FakeClock:
    def __init__(self):
        self.t = 1000.0

    def __call__(self):
        return self.t


class TestMasterSwitch(unittest.TestCase):
    def setUp(self):
        self.alerts = []
        self.clock = FakeClock()
        self.sw = MasterSwitch(alert=lambda t, m: self.alerts.append(t),
                               clock=self.clock)

    def test_on_takes_two_taps(self):
        self.assertFalse(self.sw.op("confirm")["on"])   # no arm, no on
        s = self.sw.op("arm")
        self.assertTrue(s["armed"])
        self.assertFalse(s["on"])
        self.assertTrue(self.sw.op("confirm")["on"])
        self.assertIn("Master switch ON", self.alerts)

    def test_arm_expires(self):
        self.sw.op("arm")
        self.clock.t += 200                              # past the 120s window
        self.assertFalse(self.sw.op("confirm")["on"])

    def test_off_takes_one_tap_and_is_logged(self):
        self.sw.op("arm")
        self.sw.op("confirm")
        s = self.sw.op("off")
        self.assertFalse(s["on"])
        self.assertEqual([e["action"] for e in self.sw.log],
                         ["armed", "ON", "OFF"])
        self.assertIn("Master switch OFF", self.alerts)

    def test_restore_keeps_state_across_deploys(self):
        self.sw.op("arm")
        self.sw.op("confirm")
        sw2 = MasterSwitch(clock=self.clock)
        sw2.restore(self.sw.to_dict())
        self.assertTrue(sw2.on)
        self.assertEqual(len(sw2.log), 2)



if __name__ == "__main__":
    unittest.main()
