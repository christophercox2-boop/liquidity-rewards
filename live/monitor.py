#!/usr/bin/env python3
"""Always-on live earnings monitor.

Runs on any small server (Dockerfile provided — see live/README.md). Every
POLL_SECONDS it scores your resting orders with the same official-formula
code the hourly tracker uses, then integrates the rate over time the way the
exchange does: earned_today += rate x elapsed. Serves a phone-friendly
dashboard with a running "earned today" counter and per-market breakdown.

Environment:
    POLYMARKET_KEY_ID / POLYMARKET_SECRET_KEY   API credentials (required)
    DASH_PASSWORD                               dashboard password (required)
    PORT                                        web port (default 8080)
    POLL_SECONDS                                sample interval (default 30)

The reward day runs midnight-to-midnight Eastern Time, matching Polymarket's
daily pools. State persists to state.json so restarts don't zero the counter
(a full redeploy replaces the disk and starts the day fresh).
"""

from __future__ import annotations

import base64
import datetime as dt
import json
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import track_rewards as tr  # noqa: E402 — reuse the tracker's scoring code

POLL_SECONDS = int(os.environ.get("POLL_SECONDS", "30"))
PORT = int(os.environ.get("PORT", "8080"))
DASH_PASSWORD = os.environ.get("DASH_PASSWORD", "")
STATE_PATH = Path(os.environ.get("STATE_PATH", "state.json"))
ET = ZoneInfo("America/New_York")
MAX_GAP_SECONDS = 300  # an outage never extrapolates more than 5 minutes


class Monitor:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.state: dict = {"day": None, "earned": 0.0, "per_market": {}, "history": []}
        if STATE_PATH.exists():
            try:
                self.state.update(json.loads(STATE_PATH.read_text()))
            except Exception:  # noqa: BLE001 — corrupt state: start fresh
                pass
        self.last_ts: dt.datetime | None = None
        self.rate = 0.0
        self.market_rates: dict[str, float] = {}
        self.orders: list[dict] = []
        self.error: str | None = None
        self.updated: dt.datetime | None = None

    def sample(self, now_utc: dt.datetime, orders: list[dict]) -> None:
        """Integrate earnings since the previous sample, then adopt the new rate."""
        day = now_utc.astimezone(ET).strftime("%Y-%m-%d")
        with self.lock:
            # Integrate the elapsed interval into the day it belongs to…
            if self.last_ts is not None:
                frac = min((now_utc - self.last_ts).total_seconds(), MAX_GAP_SECONDS) / 86400.0
                if frac > 0:
                    self.state["earned"] += self.rate * frac
                    for m, r in self.market_rates.items():
                        self.state["per_market"][m] = self.state["per_market"].get(m, 0.0) + r * frac
            # …then roll the day over at midnight ET.
            if self.state["day"] != day:
                if self.state["day"]:
                    self.state["history"] = (self.state["history"] + [
                        {"day": self.state["day"], "earned": round(self.state["earned"], 2)}
                    ])[-30:]
                self.state.update({"day": day, "earned": 0.0, "per_market": {}})
            self.rate = sum(o.get("est_day") or 0.0 for o in orders)
            self.market_rates = {}
            for o in orders:
                if o.get("est_day"):
                    self.market_rates[o["market"]] = self.market_rates.get(o["market"], 0.0) + o["est_day"]
            self.last_ts = now_utc
            self.orders = orders
            self.updated = now_utc
            try:
                STATE_PATH.write_text(json.dumps(self.state))
            except Exception:  # noqa: BLE001 — read-only disk: keep running in memory
                pass

    def snapshot(self) -> dict:
        with self.lock:
            return {
                "day": self.state["day"],
                "earned_today": round(self.state["earned"], 4),
                "rate_per_day": round(self.rate, 2),
                "per_market_today": {m: round(v, 4) for m, v in sorted(
                    self.state["per_market"].items(), key=lambda kv: -kv[1])},
                "orders": [
                    {k: o.get(k) for k in ("market", "side", "price", "size", "ticks", "share",
                                           "est_day", "verdict", "math")}
                    for o in self.orders
                ],
                "history": self.state["history"][-7:][::-1],
                "updated": (
                    self.updated.astimezone(ET).strftime("%Y-%m-%d %I:%M:%S %p ET")
                    if self.updated else None
                ),
                "error": self.error,
                "poll_seconds": POLL_SECONDS,
            }


MONITOR = Monitor()

DASH_HTML = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Liquidity rewards — live</title>
<style>
 body{font-family:-apple-system,system-ui,sans-serif;margin:0;padding:16px;background:#0d1117;color:#e6edf3}
 .big{font-size:56px;font-weight:700;margin:8px 0}
 .sub{color:#8b949e;font-size:14px}
 .err{background:#3d1418;color:#ffa198;padding:8px 12px;border-radius:8px;margin:10px 0;display:none}
 table{width:100%;border-collapse:collapse;margin-top:14px;font-size:13px}
 td,th{padding:6px 4px;text-align:left;border-bottom:1px solid #21262d}
 td.r,th.r{text-align:right}
 .mkt{color:#8b949e;font-size:11px;word-break:break-all}
 h3{margin:18px 0 4px;font-size:15px}
</style></head><body>
<div class="sub">Earned today (ET) — live estimate</div>
<div class="big" id="earned">…</div>
<div class="sub" id="rate"></div>
<div class="sub" id="updated"></div>
<div class="err" id="err"></div>
<h3>By market today <span class="sub">(tap a row for the math)</span></h3><table id="markets"></table>
<h3>Previous days</h3><table id="history"></table>
<script>
let OPEN = {};
function tgl(i){ OPEN[i] = !OPEN[i];
  const e = document.getElementById('d'+i); if(e) e.style.display = OPEN[i] ? '' : 'none'; }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;'); }
async function refresh(){
  try{
    const r = await fetch('data.json'); const d = await r.json();
    document.getElementById('earned').textContent = '$' + d.earned_today.toFixed(2);
    document.getElementById('rate').textContent =
      'current rate ~$' + d.rate_per_day.toFixed(2) + '/day across ' + d.orders.length + ' orders';
    document.getElementById('updated').textContent = 'updated ' + d.updated + ' · day resets midnight ET · refreshes every ' + d.poll_seconds + 's';
    const err = document.getElementById('err');
    err.style.display = d.error ? 'block' : 'none'; err.textContent = d.error || '';
    document.getElementById('markets').innerHTML =
      Object.entries(d.per_market_today).map(([m,v],i) => {
        const math = d.orders.filter(o => o.market === m).map(o =>
          esc(o.verdict || '') + '\\n' + (o.math || []).map(s => '  · ' + esc(s)).join('\\n')
        ).join('\\n\\n');
        return '<tr onclick="tgl('+i+')"><td class="mkt">'+m+'</td><td class="r">$'+v.toFixed(2)+'</td></tr>' +
          '<tr id="d'+i+'" style="display:'+(OPEN[i]?'':'none')+'"><td colspan="2" class="mkt" ' +
          'style="white-space:pre-wrap;background:#161b22">'+math+'</td></tr>';
      }).join('') || '<tr><td>nothing yet today</td></tr>';
    document.getElementById('history').innerHTML =
      d.history.map(h => '<tr><td>'+h.day+'</td><td class="r">$'+h.earned.toFixed(2)+'</td></tr>').join('')
      || '<tr><td>collecting…</td></tr>';
  }catch(e){}
}
refresh(); setInterval(refresh, 15000);
</script></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def _authed(self) -> bool:
        if not DASH_PASSWORD:
            return False
        header = self.headers.get("Authorization", "")
        if header.startswith("Basic "):
            try:
                decoded = base64.b64decode(header[6:]).decode()
                return decoded.split(":", 1)[1] == DASH_PASSWORD
            except Exception:  # noqa: BLE001
                return False
        return False

    def do_GET(self) -> None:  # noqa: N802 — http.server API
        if not DASH_PASSWORD:
            self._send(503, "text/plain", b"Set the DASH_PASSWORD environment variable to enable the dashboard.")
            return
        if not self._authed():
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="rewards"')
            self.end_headers()
            return
        if self.path.startswith("/data.json"):
            self._send(200, "application/json", json.dumps(MONITOR.snapshot()).encode())
        else:
            self._send(200, "text/html; charset=utf-8", DASH_HTML.encode())

    def _send(self, code: int, ctype: str, body: bytes) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args) -> None:  # quiet
        pass


def poll_loop(key_id: str, secret_key: str) -> None:
    event_sizes: dict[str, int] = {}
    events_refreshed = 0.0
    while True:
        try:
            if time.time() - events_refreshed > 900:  # refresh proration map every 15 min
                events_refreshed = time.time()
                try:
                    _, event_sizes = tr.fetch_politics_events()
                except Exception:  # noqa: BLE001 — keep last known map
                    pass
            orders = tr.fetch_live_orders(key_id, secret_key, event_sizes)
            MONITOR.sample(dt.datetime.now(dt.timezone.utc), orders)
            MONITOR.error = None
        except Exception as e:  # noqa: BLE001 — shown on the dashboard, loop survives
            MONITOR.error = f"{type(e).__name__}: {e}"
        time.sleep(POLL_SECONDS)


def main() -> None:
    key_id = os.environ.get("POLYMARKET_KEY_ID", "").strip()
    secret_key = os.environ.get("POLYMARKET_SECRET_KEY", "").strip()
    if not key_id or not secret_key:
        print("Set POLYMARKET_KEY_ID and POLYMARKET_SECRET_KEY", file=sys.stderr)
        sys.exit(1)
    threading.Thread(target=poll_loop, args=(key_id, secret_key), daemon=True).start()
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"live monitor on :{PORT}, polling every {POLL_SECONDS}s")
    server.serve_forever()


if __name__ == "__main__":
    main()
