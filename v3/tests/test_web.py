"""The 3.0 pages: shells are public, data demands the key, /op demands the
key AND the CSRF header, ops route to the monitor."""

import json
import unittest
import urllib.error
import urllib.request

from v3.web import WebServer, authed


class FakeMonitor:
    def __init__(self):
        self.taps = []
        self.ops = []
        self.families = {}

        class N:
            def label(self, s):
                return f"name:{s}"
        self.names = N()

    def public_state(self):
        return {"saved_at": 123.0, "build": "abc",
                "summaries": {"politics": {
                    "name": "Politics", "mode": "observing",
                    "orders": [{"market": "m-1", "id": "o1"}],
                    "best_idle": [{"market": "m-2"}],
                    "inventory": {"m-3": {"qty": 1}}}},
                "switch_view": {"master": {"on": False}}}

    def switch_tap(self, op, which):
        self.taps.append((op, which))
        return {"on": op == "confirm"}

    def order_op(self, op, order_id, price=None):
        self.ops.append((op, order_id, price))
        return {"ok": True, "note": "done"}


def req(url, method="GET", headers=None, body=None):
    r = urllib.request.Request(url, method=method,
                               data=json.dumps(body).encode() if body else None)
    for k, v in (headers or {}).items():
        r.add_header(k, v)
    try:
        with urllib.request.urlopen(r, timeout=5) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


class TestWeb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mon = FakeMonitor()
        cls.srv = WebServer(cls.mon, port=0)
        cls.srv.password = "pw"
        cls.srv.start()
        cls.base = f"http://127.0.0.1:{cls.srv._httpd.server_address[1]}"

    def test_shells_are_public_and_hold_no_data(self):
        for path in ("/", "/orders", "/plan", "/switch", "/log"):
            code, body = req(self.base + path)
            self.assertEqual(code, 200, path)
            self.assertNotIn(b"m-1", body)

    def test_data_needs_the_key_and_carries_labels(self):
        code, _ = req(self.base + "/data.json")
        self.assertEqual(code, 401)
        code, body = req(self.base + "/data.json",
                         headers={"X-Dash-Key": "pw"})
        self.assertEqual(code, 200)
        d = json.loads(body)
        self.assertEqual(d["labels"]["m-1"], "name:m-1")
        self.assertEqual(d["labels"]["m-2"], "name:m-2")
        self.assertEqual(d["labels"]["m-3"], "name:m-3")

    def test_op_needs_key_and_csrf(self):
        code, _ = req(self.base + "/op", method="POST",
                      body={"op": "switch_arm"})
        self.assertEqual(code, 401)
        code, _ = req(self.base + "/op", method="POST",
                      headers={"X-Dash-Key": "pw"}, body={"op": "switch_arm"})
        self.assertEqual(code, 403)

    def test_ops_route(self):
        h = {"X-Dash-Key": "pw", "X-Reprice": "1",
             "Content-Type": "application/json"}
        req(self.base + "/op", method="POST", headers=h,
            body={"op": "switch_arm", "which": "politics"})
        self.assertIn(("arm", "politics"), self.mon.taps)
        req(self.base + "/op", method="POST", headers=h,
            body={"op": "cancel", "order_id": "o1"})
        self.assertIn(("cancel", "o1", None), self.mon.ops)
        code, body = req(self.base + "/op", method="POST", headers=h,
                         body={"op": "move", "order_id": "o1", "price": 0.05})
        self.assertEqual(json.loads(body)["ok"], True)
        self.assertIn(("move", "o1", 0.05), self.mon.ops)

    def test_authed_variants(self):
        hdr = {"X-Dash-Key": "pw"}
        self.assertTrue(authed(hdr.get, "", "pw"))
        self.assertTrue(authed({}.get, "key=pw", "pw"))
        self.assertFalse(authed({}.get, "", ""))     # no password = locked


if __name__ == "__main__":
    unittest.main()
