"""Tests for 2.0's page: auth ways in, routes, and the no-data shell."""

import http.client
import json
import unittest

from v2.web import WebServer, authed


class TestAuthed(unittest.TestCase):
    def test_three_ways_in(self):
        h = {"X-Dash-Key": "pw"}
        self.assertTrue(authed(h.get, "", "pw"))
        self.assertTrue(authed({}.get, "key=pw", "pw"))
        import base64
        basic = {"Authorization": "Basic " + base64.b64encode(b"u:pw").decode()}
        self.assertTrue(authed(basic.get, "", "pw"))

    def test_wrong_or_missing_key_fails(self):
        self.assertFalse(authed({"X-Dash-Key": "nope"}.get, "", "pw"))
        self.assertFalse(authed({}.get, "", "pw"))
        self.assertFalse(authed({"Authorization": "Basic !!!"}.get, "", "pw"))

    def test_no_password_set_means_locked(self):
        self.assertFalse(authed({"X-Dash-Key": ""}.get, "", ""))


class TestWebServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = {"saved_at": 123.0, "mode": "read-only",
                     "estimator": {"earned": 1.23, "rate": 4.56}}
        cls.srv = WebServer(get_state=lambda: cls.state, password="pw",
                            port=0, bind="127.0.0.1")
        cls.srv.start_background()
        cls.port = cls.srv.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()

    def get(self, path, headers=None):
        c = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        c.request("GET", path, headers=headers or {})
        r = c.getresponse()
        body = r.read()
        c.close()
        return r.status, r.getheader("Content-Type", ""), body

    def test_shell_is_public_and_holds_no_data(self):
        status, ctype, body = self.get("/")
        self.assertEqual(status, 200)
        self.assertIn("text/html", ctype)
        self.assertIn(b'href="switch"', body)   # nav links to the sections
        self.assertNotIn(b"1.23", body)      # data never baked into the shell

    def test_data_requires_the_key(self):
        status, _, body = self.get("/data.json")
        self.assertEqual(status, 401)
        status, _, body = self.get("/data.json", {"X-Dash-Key": "pw"})
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)["estimator"]["earned"], 1.23)

    def test_unknown_route_is_404(self):
        self.assertEqual(self.get("/nope")[0], 404)


if __name__ == "__main__":
    unittest.main()
