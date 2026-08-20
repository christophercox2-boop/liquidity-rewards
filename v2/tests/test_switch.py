"""Tests for the master switch and its web route."""

import http.client
import json
import unittest

from v2.switch import MasterSwitch
from v2.web import WebServer


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


class TestSwitchRoute(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sw = MasterSwitch()
        cls.cfb_sw = MasterSwitch(name="CFB switch", scope="college football")
        # same shape as main.switch_tap: op plus which switch
        cls.srv = WebServer(get_state=lambda: {"engine": {"used": 1.0}},
                            password="pw", port=0, bind="127.0.0.1",
                            switch_op=lambda op, which="master":
                                (cls.cfb_sw if which == "cfb" else cls.sw).op(op))
        cls.srv.start_background()
        cls.port = cls.srv.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()

    def post(self, body, headers):
        c = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        c.request("POST", "/switch", body=json.dumps(body), headers=headers)
        r = c.getresponse()
        out = (r.status, r.read())
        c.close()
        return out

    def test_auth_then_csrf_then_op(self):
        self.assertEqual(self.post({"op": "arm"}, {})[0], 401)
        self.assertEqual(self.post({"op": "arm"}, {"X-Dash-Key": "pw"})[0], 403)
        status, body = self.post({"op": "arm"},
                                 {"X-Dash-Key": "pw", "X-Reprice": "1"})
        self.assertEqual(status, 200)
        j = json.loads(body)
        self.assertTrue(j["sw"]["armed"])
        self.assertEqual(j["engine"]["used"], 1.0)
        status, _ = self.post({"op": "nonsense"},
                              {"X-Dash-Key": "pw", "X-Reprice": "1"})
        self.assertEqual(status, 400)

    def test_cfb_switch_is_its_own(self):
        status, body = self.post({"op": "arm", "which": "cfb"},
                                 {"X-Dash-Key": "pw", "X-Reprice": "1"})
        self.assertEqual(status, 200)
        self.assertTrue(json.loads(body)["sw"]["armed"])
        self.assertFalse(self.sw.on)          # the seats switch never moved
        status, _ = self.post({"op": "arm", "which": "nfl"},
                              {"X-Dash-Key": "pw", "X-Reprice": "1"})
        self.assertEqual(status, 400)

    def test_switch_shell_served(self):
        c = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        c.request("GET", "/switch")
        r = c.getresponse()
        self.assertEqual(r.status, 200)
        page = r.read()
        self.assertIn(b"2.0 switches", page)
        self.assertIn(b"College football", page)
        c.close()


if __name__ == "__main__":
    unittest.main()
