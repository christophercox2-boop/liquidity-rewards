"""2.0's page — read-only phase: one page answering "is 2.0 measuring,
and what does it see?"

Served by a small stdlib HTTP server bound to localhost; 1.0's monitor
stays the container's front door and forwards /v2/* here (its proxy
route), so the owner reaches this at the same address as everything
else and the browser's stored dashKey just works. The shell itself is
public and holds no data — the same pattern as every 1.0 page — while
data.json underneath demands the key.

No mutating routes exist in this phase, so there is nothing for a CSRF
header to protect yet; the header rail returns with the first
order-touching endpoint.
"""

from __future__ import annotations

import base64
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

DEFAULT_PORT = 8091
DEFAULT_BIND = "127.0.0.1"


def authed(get_header, query_string: str, password: str) -> bool:
    """Same three ways in as 1.0: X-Dash-Key header (localStorage),
    ?key= (widgets/Shortcuts), legacy Basic. No password set = locked."""
    if not password:
        return False
    if get_header("X-Dash-Key") == password:
        return True
    if (parse_qs(query_string).get("key") or [""])[0] == password:
        return True
    header = get_header("Authorization") or ""
    if header.startswith("Basic "):
        try:
            return base64.b64decode(header[6:]).decode().split(":", 1)[1] == password
        except Exception:  # noqa: BLE001
            return False
    return False


SHELL = """<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>2.0</title>
<style>
 body{background:#1a202b;color:#e6e9ef;font:16px/1.45 -apple-system,system-ui,sans-serif;
      margin:0;padding:14px;max-width:640px;margin:auto}
 h1{font-size:19px;margin:4px 0 10px} .muted{color:#8a93a5;font-size:13px}
 .big{font-size:34px;font-weight:700;margin:2px 0}
 .ok{color:#5dd39e}.bad{color:#ff7a7a}.warn{color:#ffce6b}
 table{border-collapse:collapse;width:100%;font-size:14px;margin:6px 0}
 td,th{padding:4px 6px;border-bottom:1px solid #2a3242;text-align:left}
 td.r,th.r{text-align:right} code{color:#9ecbff;font-size:12px;word-break:break-all}
 .card{background:#212a38;border-radius:10px;padding:10px 12px;margin:10px 0}
 input,button{font-size:16px;padding:8px;border-radius:8px}
 input{background:#141a24;color:#e6e9ef;border:1px solid #394456;width:60%}
 button{background:#2d6cdf;color:#fff;border:0;margin-left:6px}
 .nav{margin:2px 0 10px}
 .nav a{color:#9ecbff;text-decoration:none;margin-right:14px;font-size:15px}
 .nav .here{color:#e6e9ef;font-weight:700}
</style></head><body>
<h1>2.0</h1>
<div class="nav"><span class="here">status</span><a href="switch">master switch</a></div>
<div id="login" class="card" style="display:none">
 <div class="muted">password</div>
 <input id="k" type="password"><button onclick="saveKey()">open</button>
</div>
<div id="view"></div>
<script>
function hdrs(){const h=new Headers();h.set('X-Dash-Key',localStorage.getItem('dashKey')||'');return h;}
function saveKey(){localStorage.setItem('dashKey',document.getElementById('k').value);load();}
function usd(x){return '$'+(x||0).toFixed(2);}
function row(c){return '<tr>'+c.map(function(x,i){return '<td class="'+(i?'r':'')+'">'+x+'</td>';}).join('')+'</tr>';}
function load(){
 fetch('data.json',{headers:hdrs(),cache:'no-store'}).then(function(r){
  if(r.status===401){document.getElementById('login').style.display='block';
    document.getElementById('view').innerHTML='';return null;}
  return r.json();
 }).then(function(d){
  if(!d)return;
  document.getElementById('login').style.display='none';
  var age=Math.round(Date.now()/1000-d.saved_at);
  var fresh=age<120?'<span class="ok">&#9679; live</span>':'<span class="bad">&#9679; stale '+age+'s</span>';
  var e=d.estimator||{};
  var h='<div class="card">'+fresh+' <span class="muted">'+(d.mode||'')+' &middot; build '+(d.build||'?')+
    ' &middot; ws '+((d.ws||{}).state||'?')+' &middot; '+(d.orders_n||0)+' orders in '+(d.markets_n||0)+' markets</span>'+
    '<div class="big">'+usd(e.earned)+'<span class="muted" style="font-size:15px"> earned today ('+(e.day||'')+')</span></div>'+
    '<div>'+usd(e.rate)+'/day now'+
    (e.stale_s>60?' <span class="warn">&middot; '+Math.round(e.stale_s/60)+' min unmeasured</span>':'')+'</div></div>';
  var g=d.engine||{};
  var sw=d.switch||{};
  h+='<div class="card"><b>Engine</b> <span class="muted">'+(g.mode||'?')+
    ' &middot; switch '+(sw.on?'<span class="ok">ON</span>':'<span class="muted">off</span>')+'</span>'+
    '<div>at risk '+usd(g.used)+' of '+usd(g.ceiling)+' &middot; headroom '+usd(g.headroom)+'</div>';
  if(g.sweep&&!g.sweep.done){h+='<div class="warn">handover sweep running &middot; '+
    (g.sweep.cancelled||0)+' 1.0 orders cleared so far</div>';}
  else if(g.sweep&&g.sweep.cancelled){h+='<div class="muted">handover done: '+
    g.sweep.cancelled+' 1.0 orders cleared</div>';}
  var go=g.orders||[];
  if(go.length){h+='<table><tr><th>market</th><th class="r">order</th><th class="r">why</th></tr>';
   go.forEach(function(o){h+=row(['<code>'+o.market+'</code>',
     o.side+' '+o.qty+' @ '+(o.price*100).toFixed(1)+'c',o.purpose]);});
   h+='</table>';}
  if(g.silent_cancels){h+='<div class="warn muted">'+g.silent_cancels+' silent cancels seen</div>';}
  h+='</div>';
  var mr=Object.entries(e.market_rates||{}).sort(function(a,b){return b[1]-a[1];});
  if(mr.length){h+='<div class="card"><b>Where the rate comes from</b><table><tr><th>market</th><th class="r">$/day</th><th class="r">earned</th></tr>';
   mr.slice(0,40).forEach(function(kv){h+=row(['<code>'+kv[0]+'</code>',usd(kv[1]),usd((e.per_market||{})[kv[0]])]);});
   h+='</table></div>';}
  var th=(d.terms_history||[]).slice(-15).reverse();
  if(th.length){h+='<div class="card"><b>Reward terms log</b><table>';
   th.forEach(function(t){h+=row([new Date(t.ts*1000).toLocaleString(),'<code>'+t.slug+'</code>',
     t.why+(t.pool!=null?(' $'+t.pool+' / '+t.target+' / df '+t.df+' / &divide;'+t.event_n):'')]);});
   h+='</table></div>';}
  var er=(d.errors||[]).slice(-8).reverse();
  if(er.length){h+='<div class="card"><b class="warn">Recent trouble</b><div class="muted">'+er.join('<br>')+'</div></div>';}
  document.getElementById('view').innerHTML=h;
 }).catch(function(){document.getElementById('view').innerHTML='<div class="card bad">unreachable</div>';});
}
load();setInterval(load,30000);
</script></body></html>"""


SWITCH_SHELL = """<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>2.0 switch</title>
<style>
 body{background:#1a202b;color:#e6e9ef;font:16px/1.5 -apple-system,system-ui,sans-serif;
      margin:0;padding:16px;max-width:480px;margin:auto}
 h1{font-size:19px} .muted{color:#8a93a5;font-size:13px}
 .state{font-size:30px;font-weight:800;margin:10px 0}
 .on{color:#5dd39e}.off{color:#8a93a5}.armed{color:#ffce6b}
 .card{background:#212a38;border-radius:10px;padding:12px;margin:12px 0}
 button{font-size:18px;padding:14px 18px;border-radius:10px;border:0;width:100%;
        margin:6px 0;font-weight:700}
 .b-arm{background:#3a4456;color:#fff}.b-go{background:#2d9d5c;color:#fff}
 .b-off{background:#c0392b;color:#fff}
 input{font-size:16px;padding:8px;border-radius:8px;background:#141a24;
       color:#e6e9ef;border:1px solid #394456;width:60%}
 table{border-collapse:collapse;width:100%;font-size:13px}
 td{padding:3px 6px;border-bottom:1px solid #2a3242}
</style></head><body>
<h1>2.0 master switch</h1>
<div style="margin:2px 0 10px"><a href="." style="color:#9ecbff;text-decoration:none">&larr; status</a></div>
<div id="login" class="card" style="display:none">
 <div class="muted">password</div>
 <input id="k" type="password"><button class="b-arm" style="width:36%;display:inline-block"
  onclick="saveKey()">open</button>
</div>
<div id="view" class="card">loading&hellip;</div>
<div class="muted">ON takes two taps. OFF takes one. Every flip is logged and pushed
to your phone. The state survives deploys; a new build booting with the switch on
sends one push saying so.</div>
<script>
function hdrs(json){const h=new Headers();h.set('X-Dash-Key',localStorage.getItem('dashKey')||'');
 h.set('X-Reprice','1');if(json)h.set('Content-Type','application/json');return h;}
function saveKey(){localStorage.setItem('dashKey',document.getElementById('k').value);load();}
function op(o){fetch('switch',{method:'POST',headers:hdrs(true),body:JSON.stringify({op:o})})
 .then(function(r){if(r.status===401){document.getElementById('login').style.display='block';return null;}
  return r.json();}).then(function(d){if(d)render(d.sw,d.engine);});}
function usd(x){return '$'+(x||0).toFixed(2);}
function render(sw,eng){
 document.getElementById('login').style.display='none';
 var h='';
 if(sw.on){h+='<div class="state on">ON</div><button class="b-off" onclick="op(\\'off\\')">TURN OFF</button>';}
 else if(sw.armed){h+='<div class="state armed">ARMED &middot; '+sw.arm_expires_in+'s</div>'+
  '<button class="b-go" onclick="op(\\'confirm\\')">CONFIRM &mdash; TURN ON</button>'+
  '<button class="b-arm" onclick="op(\\'off\\')">cancel</button>';}
 else{h+='<div class="state off">OFF</div><button class="b-arm" onclick="op(\\'arm\\')">ARM (tap 1 of 2)</button>';}
 if(eng){h+='<div class="muted" style="margin-top:8px">at risk '+usd(eng.used)+' of '+usd(eng.ceiling)+
  ' ceiling &middot; headroom '+usd(eng.headroom)+' &middot; '+
  (eng.orders||[]).length+' orders resting'+
  (eng.silent_cancels?' &middot; '+eng.silent_cancels+' silent cancels':'')+'</div>';}
 if(sw.log&&sw.log.length){h+='<table>';sw.log.slice().reverse().forEach(function(l){
  h+='<tr><td>'+new Date(l.ts*1000).toLocaleString()+'</td><td>'+l.action+'</td></tr>';});h+='</table>';}
 document.getElementById('view').innerHTML=h;
}
function load(){fetch('data.json',{headers:hdrs(false),cache:'no-store'}).then(function(r){
 if(r.status===401){document.getElementById('login').style.display='block';return null;}
 return r.json();}).then(function(d){if(d)render(d.switch||{},d.engine);});}
load();setInterval(load,15000);
</script></body></html>"""


class _Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # noqa: N802 — quiet; the loop logs what matters
        pass

    def _send(self, code: int, ctype: str, body: bytes) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        # a cached page runs old JS against a live payload — never cache
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802 — http.server API
        route = self.path.split("?", 1)[0]
        if route in ("", "/"):
            self._send(200, "text/html; charset=utf-8", SHELL.encode())
            return
        if route == "/switch":
            self._send(200, "text/html; charset=utf-8", SWITCH_SHELL.encode())
            return
        if route == "/data.json":
            qs = urlparse(self.path).query
            if not authed(self.headers.get, qs, self.server.password):
                self._send(401, "application/json", b'{"error": "key required"}')
                return
            state = self.server.get_state() or {}
            self._send(200, "application/json", json.dumps(state).encode())
            return
        self._send(404, "text/plain", b"not found")

    def do_POST(self) -> None:  # noqa: N802 — http.server API
        route = self.path.split("?", 1)[0]
        if route != "/switch" or self.server.switch_op is None:
            self._send(404, "text/plain", b"not found")
            return
        if not authed(self.headers.get, urlparse(self.path).query, self.server.password):
            self._send(401, "application/json", b'{"error": "key required"}')
            return
        # a cross-origin request cannot set a custom header without a CORS
        # preflight that is never granted — the same CSRF rail as 1.0
        if self.headers.get("X-Reprice") != "1":
            self._send(403, "text/plain", b"missing X-Reprice header")
            return
        try:
            body = self.rfile.read(int(self.headers.get("Content-Length") or 0))
            op = str(json.loads(body or b"{}").get("op") or "")
        except ValueError:
            self._send(400, "text/plain", b"bad body")
            return
        if op not in ("arm", "confirm", "off"):
            self._send(400, "text/plain", b"op must be arm/confirm/off")
            return
        sw = self.server.switch_op(op)
        state = self.server.get_state() or {}
        self._send(200, "application/json",
                   json.dumps({"sw": sw, "engine": state.get("engine")}).encode())


class WebServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, get_state, password: str | None = None,
                 port: int | None = None, bind: str | None = None,
                 switch_op=None):
        self.get_state = get_state
        self.switch_op = switch_op
        self.password = (password if password is not None
                         else os.environ.get("DASH_PASSWORD", ""))
        port = port if port is not None else int(os.environ.get("V2_PORT", DEFAULT_PORT))
        bind = bind if bind is not None else os.environ.get("V2_BIND", DEFAULT_BIND)
        super().__init__((bind, port), _Handler)

    def start_background(self) -> None:
        threading.Thread(target=self.serve_forever, daemon=True, name="v2-web").start()
