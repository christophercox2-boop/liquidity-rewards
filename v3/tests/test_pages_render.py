"""Every page's render() must actually RUN against representative
data. The grades page shipped with a ReferenceError on 2026-08-23 and
read 'unreachable' for ten hours while the whole suite stayed green —
the pages' JavaScript was the one layer nothing executed."""

import json
import os
import shutil
import subprocess
import tempfile
import unittest

from v3.web import PAGES, _PLUMBING

PAYLOAD = {
    "saved_at": 123.0, "build": "t", "boot_ts": 100.0,
    "errors": ["08-23 00:00:00 note"],
    "audit": [{"op": "place", "market": "m-1", "ts": 1.0}],
    "master_switch": {"on": True, "log": []},
    "flatten": {"active": False},
    "flat_stats": {"cancelled": 0, "failed": 0},
    "summaries": {"politics": {
        "name": "Politics", "mode": "resting", "est_day": 1.2,
        "est_rate": 1.1, "earned_today": 0.5, "spent": 10.0,
        "capital_usd": 250.0, "unmeasured_min": 0.0,
        "markets": 3, "scanned": 3, "resting_ok": True,
        "orders": [{"market": "m-1", "id": "o1", "side": "BUY",
                    "price": 0.4, "qty": 2.0, "purpose": "earn",
                    "verdict": "earning", "why": "w", "est_day": 1.0}],
        "best_idle": [{"market": "m-2", "est": 0.5, "why": "w"}],
        "triage_feed": [{"market": "m-2", "ts": 1.0, "verdict": "pass",
                         "why": "w", "book": {"b": [[0.4, 5]],
                                              "a": [[0.5, 5]]},
                         "picks": []}],
        "inventory": {"m-3": {"qty": 1.0, "cost": 0.2}},
        "holdings_usd": 1.0, "holdings_counted": False}},
    "silver": {"senate_races": 3, "gov_races": 3, "note": "",
               "ak_gov": {}, "meta": {}},
    "silver_log": [],
    "grades": [{"day": "2026-08-20", "est": 1.0, "actual": 2.0,
                "unmeasured_min": 0.0},
               {"day": "2026-08-21", "est": 3.0, "actual": None,
                "unmeasured_min": 5.0}],
    "paid_total": {"usd": 100.0, "days": 9, "since": "2026-07-01"},
    "ws": {"connected": True, "markets": 2},
    "alerts_log": [{"ts": 1.0, "title": "t", "msg": "m", "sent": True,
                    "why": ""}],
    "rewards_last": {"ok": True, "new_rows": [], "new_count": 0,
                     "days": {}},
    "floor": {"want": True, "required": [], "acked": True},
    "switch_view": {"master": {"on": True, "label": "ON"},
                    "politics": {"on": True, "label": "ON"}},
    "est_politics": {"rate": 1.0, "earned": 0.5, "dots": [[1, 1.0]],
                     "market_rates": {"m-1": 1.0}},
    "sw_politics": {"on": True, "log": []},
    "fam_log_politics": [{"ts": 1.0, "event": "place", "market": "m-1"}],
    "labels": {"m-1": "Market One", "m-2": "Market Two",
               "m-3": "Market Three"},
    "now": 124.0, "boot": {},
}

HARNESS = r"""
const el = () => ({style:{}, innerHTML:'', textContent:'',
                   appendChild(){}, remove(){}});
global.window = {_d:null, _rw:null, _rwbusy:false, _held:false,
                 scrollY:0, addEventListener(){}, scrollTo(){},
                 localStorage:{getItem:()=>null, setItem(){}}};
global.document = {getElementById: () => el(),
                   createElement: () => el(),
                   body: {appendChild(){}}};
global.localStorage = window.localStorage;
global.esc = s => String(s == null ? '' : s);
global.usd = x => '$' + Number(x || 0).toFixed(2);
global.pc = x => Math.round(Number(x || 0) * 100) + 'c';
global.hdrs = () => ({});
global.fetch = () => ({then: function(){ return this; },
                       catch: function(){ return this; }});
global.drawGraph = () => '';
global.setInterval = () => 0;
const fs = require('fs');
const js = fs.readFileSync(process.argv[2], 'utf8');
eval(js);
const d = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
window._d = d;
if (typeof render !== 'function') { console.log('NO RENDER'); process.exit(0); }
try {
  const out = render(d);
  if (typeof out !== 'string' || !out.length) throw new Error('empty render');
  console.log('OK');
} catch (e) {
  console.log('THREW: ' + e.constructor.name + ': ' + e.message);
  process.exit(1);
}
"""


@unittest.skipIf(shutil.which("node") is None, "node not installed")
class TestEveryPageRenders(unittest.TestCase):
    def test_render_runs_on_every_page(self):
        with tempfile.TemporaryDirectory() as td:
            hp = os.path.join(td, "h.js")
            pp = os.path.join(td, "p.json")
            with open(hp, "w") as f:
                f.write(HARNESS)
            with open(pp, "w") as f:
                json.dump(PAYLOAD, f)
            failures = []
            seen = set()
            for route, (_t, _h, js, _sub) in PAGES.items():
                if id(js) in seen:
                    continue
                seen.add(id(js))
                jp = os.path.join(td, "page.js")
                with open(jp, "w") as f:
                    f.write(_PLUMBING + "\n" + js)
                r = subprocess.run(["node", hp, jp, pp],
                                   capture_output=True, text=True,
                                   timeout=20)
                out = (r.stdout + r.stderr).strip()
                if r.returncode != 0 or "THREW" in out:
                    failures.append(f"{route}: {out[:200]}")
            self.assertEqual(failures, [])
