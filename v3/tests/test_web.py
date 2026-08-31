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
        self.payload_json = None
        self.boot_stage = {}

        class N:
            def label(self, s):
                return f"name:{s}"
        self.names = N()

    # the REAL payload builder, bound to this fake — the contract the
    # pages depend on is main's, not a test double's
    from v3.main import Monitor as _M
    PHONE_KEYS = _M.PHONE_KEYS
    build_phone_payload = _M.build_phone_payload
    boot_payload = _M.boot_payload

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

    def order_op(self, op, order_id, price=None, pin=False, qty=None):
        self.ops.append((op, order_id, price) if qty is None
                        else (op, order_id, price, qty))
        self.pins = getattr(self, "pins", []) + [pin]
        return {"ok": True, "note": "done"}

    def close_position(self, market):
        self.closed = getattr(self, "closed", []) + [market]
        return {"ok": True, "note": "sold"}

    def qualify_ask(self, market):
        self.qualified = getattr(self, "qualified", []) + [market]
        return {"ok": True, "note": "rested"}

    def live_view(self, slug):
        self.live_reads = getattr(self, "live_reads", 0) + 1
        return {"ok": True, "market": slug, "bids": [[0.05, 100.0]],
                "asks": [[0.07, 50.0]], "ours": [], "position": None,
                "tick": 0.01, "name": f"name:{slug}", "ts": 1.0}

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
        import json as _j
        self.mon.payload_json = _j.dumps(
            self.mon.build_phone_payload()).encode()
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

    def test_live_card_ops(self):
        """The live card's ops: a move carries the hand-set pin through,
        and the close-out button routes to close_position."""
        h = {"X-Dash-Key": "pw", "X-Reprice": "1",
             "Content-Type": "application/json"}
        req(self.base + "/op", method="POST", headers=h,
            body={"op": "move", "order_id": "o2", "price": 0.08, "pin": 1})
        self.assertIn(("move", "o2", 0.08), self.mon.ops)
        self.assertIn(True, getattr(self.mon, "pins", []))
        req(self.base + "/op", method="POST", headers=h,
            body={"op": "move", "order_id": "o3", "price": 0.08,
                  "qty": 25.0, "pin": 1})
        self.assertIn(("move", "o3", 0.08, 25.0), self.mon.ops)
        code, body = req(self.base + "/op", method="POST", headers=h,
                         body={"op": "close_position", "market": "m-9"})
        self.assertEqual(json.loads(body)["ok"], True)
        self.assertIn("m-9", self.mon.closed)
        code, body = req(self.base + "/op", method="POST", headers=h,
                         body={"op": "qualify_ask", "market": "m-8"})
        self.assertEqual(json.loads(body)["ok"], True)
        self.assertIn("m-8", self.mon.qualified)

    def test_live_stream_needs_key_and_pushes_the_book(self):
        """/live is the card's open line: locked without the key, and
        with it the first server-sent event carries the fresh book."""
        import urllib.request
        code, _ = req(self.base + "/live?m=m-1")
        self.assertEqual(code, 401)
        r = urllib.request.Request(self.base + "/live?m=m-1&key=pw")
        with urllib.request.urlopen(r, timeout=5) as resp:
            self.assertEqual(resp.status, 200)
            self.assertIn("text/event-stream",
                          resp.headers.get("Content-Type", ""))
            line = resp.readline().decode()
            self.assertTrue(line.startswith("data: "))
            j = json.loads(line[len("data: "):])
            self.assertTrue(j["ok"])
            self.assertEqual(j["market"], "m-1")
            self.assertEqual(j["bids"][0], [0.05, 100.0])
        self.assertGreaterEqual(self.mon.live_reads, 1)

    def test_authed_variants(self):
        hdr = {"X-Dash-Key": "pw"}
        self.assertTrue(authed(hdr.get, "", "pw"))
        self.assertTrue(authed({}.get, "key=pw", "pw"))
        self.assertFalse(authed({}.get, "", ""))     # no password = locked


if __name__ == "__main__":
    unittest.main()


class TestRedesign(unittest.TestCase):
    """The 2026-08-31 redesign: quick look with sub-pages, slim status,
    orders-first orders page, grades renamed pay with a tax reserve."""

    def test_nav_and_routes(self):
        from v3 import web
        labels = [l for l, _h in web.NAV]
        self.assertEqual(labels,
                         ["quick look", "status", "orders", "pay",
                          "log", "switch"])
        # plan and model keep their routes but are off the bar
        self.assertIn("/plan", web.PAGES)
        self.assertIn("/silver", web.PAGES)
        self.assertNotIn("plan", labels)
        self.assertNotIn("model", labels)
        # fills and watch hang under quick look
        self.assertEqual(web.PAGES["/fills"][3], "quick")
        self.assertEqual(web.PAGES["/watch"][3], "quick")
        self.assertEqual(web.PAGES["/pay"][0], "Pay")

    def test_orders_page_has_no_hand_place_form(self):
        from v3 import web
        self.assertNotIn("op:'place'", web.ORDERS_JS)
        self.assertNotIn("Place an order by hand", web.ORDERS_JS)

    def test_pay_page_reserves_22_percent(self):
        from v3 import web
        self.assertIn("0.22", web.PAY_JS)
        self.assertIn("tax at 22%", web.PAY_JS)
        # rows only after the button: the card reads window._rw, never
        # the payload's stored last result
        self.assertIn("var j=window._rw;", web.PAY_JS)

    def test_status_drops_the_rotating_cards_for_a_percentage(self):
        from v3 import web
        self.assertNotIn("tchip", web.STATUS_JS)
        self.assertIn("worth the budget", web.STATUS_JS)


class TestBootPayload(unittest.TestCase):
    """Owner, 2026-08-31: the app booted, served on :8080, and every
    page still read "unreachable" — the pre-first-cycle fallback
    rebuilt the payload from live dicts on the web thread while the
    cycle mutated them (the 2026-08-22 race, back whenever a first
    cycle runs long). /data.json now serves a safe boot snapshot."""

    def test_data_json_serves_a_boot_snapshot_before_the_first_cycle(self):
        import types
        from v3.main import Monitor
        m = FakeMonitor()
        m.payload_json = None
        m.boot_stage = {"stage": "reading the board", "pct": 20}
        m.build = "abc123"
        m.boot_ts = 5.0
        m.master = types.SimpleNamespace(state=lambda: {"on": False})
        m.switches = {}
        m.families = {}
        body = Monitor.boot_payload(m)
        d = json.loads(body)
        self.assertTrue(d["starting"])
        self.assertEqual(d["build"], "abc123")
        self.assertEqual(d["boot"]["pct"], 20)
        self.assertEqual(d["summaries"], {})

    def test_boot_payload_never_raises(self):
        from v3.main import Monitor
        broken = object()          # no attributes at all
        body = Monitor.boot_payload(broken)
        self.assertIn(b"starting", body)
        json.loads(body)           # still valid JSON

    def test_every_page_renders_the_boot_card(self):
        from v3 import web
        for js in (web.GRAPH_JS, web.STATUS_JS, web.ORDERS_JS, web.PAY_JS):
            self.assertIn("if(d.starting)return bootCard(d);", js)
        self.assertIn("function bootCard(d)", web._PLUMBING)


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
        for route, (_title, _here, js, _sub) in web.PAGES.items():
            with tempfile.NamedTemporaryFile("w", suffix=".js",
                                             delete=False) as f:
                f.write(js + web._PLUMBING)
                path = f.name
            r = subprocess.run([node, "--check", path],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0,
                             f"{route}: {r.stderr[:300]}")
