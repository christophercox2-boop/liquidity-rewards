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

    def fills_view(self):
        return {"ok": True, "fills": [
            {"ts": 1.0, "market": "m-1", "side": "BUY", "qty": 5.0,
             "px": 0.19, "purpose": "earn", "why": "w", "est_day": 1.0,
             "rested_h": 2.0, "fair": 0.1, "band": None, "conf": 1.0,
             "touch_bid": 0.18, "touch_ask": 0.2, "conc": 0.09,
             "pos_after": 5.0, "family": "politics", "name": "name:m-1",
             "now_bid": 0.18, "now_ask": 0.2, "pos_now": 5.0,
             "exit_resting": False}]}


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

    def test_fills_tab_and_feed(self):
        code, body = req(self.base + "/fills")
        self.assertEqual(code, 200)
        self.assertNotIn(b"m-1", body)          # the shell holds no data
        code, _ = req(self.base + "/fills.json")
        self.assertEqual(code, 401)             # the feed demands the key
        code, body = req(self.base + "/fills.json",
                         headers={"X-Dash-Key": "pw"})
        self.assertEqual(code, 200)
        j = json.loads(body)
        self.assertTrue(j["ok"])
        self.assertEqual(j["fills"][0]["market"], "m-1")

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


class TestPageScriptsParse(unittest.TestCase):
    """The grades page shipped with a raw apostrophe inside a JS string
    and every visitor got a permanent 'loading…' (2026-08-21). Every
    page's script must PARSE, checked with a real JS parser."""

    def test_every_page_script_is_valid_javascript(self):
        import shutil
        import subprocess
        import tempfile
        from v3 import web
        node = shutil.which("node")
        if not node:
            self.skipTest("node not available")
        for route, (_title, _here, js) in web.PAGES.items():
            with tempfile.NamedTemporaryFile("w", suffix=".js",
                                             delete=False) as f:
                f.write(js + web._PLUMBING)
                path = f.name
            r = subprocess.run([node, "--check", path],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0,
                             f"{route}: {r.stderr[:300]}")
