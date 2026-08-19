"""2.0's pages — small, phone-first, each answering one question.

    /          am I earning right now, and is the data fresh?
    /orders    what is resting, and what does the engine expect of each order?
    /markets   the ladder view and the filterable market list
    /opps      what is the engine considering, and how calibrated is it?
    /log       what happened recently?
    /switch    the master switch and the risk ceiling

Served by a small stdlib HTTP server bound to localhost; 1.0's monitor
stays the container's front door and forwards /v2/* here, so the
browser's stored dashKey just works. Every page is a public SHELL
holding no data — the same pattern as 1.0 — and everything they render
comes from data.json underneath, which demands the key. The only
mutating route is the switch, guarded by auth plus the custom CSRF
header (a cross-origin request cannot set one without a preflight that
is never granted).
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


NAV = (("status", "."), ("orders", "orders"), ("markets", "markets"),
       ("opps", "opps"), ("log", "log"), ("switch", "switch"))

_CSS = """
 body{background:#1a202b;color:#e6e9ef;font:16px/1.45 -apple-system,system-ui,sans-serif;
      margin:0;padding:14px;max-width:680px;margin:auto}
 h1{font-size:19px;margin:4px 0 6px} .muted{color:#8a93a5;font-size:13px}
 .big{font-size:34px;font-weight:700;margin:2px 0}
 .ok{color:#5dd39e}.bad{color:#ff7a7a}.warn{color:#ffce6b}
 table{border-collapse:collapse;width:100%;font-size:13px;margin:6px 0}
 td,th{padding:4px 6px;border-bottom:1px solid #2a3242;text-align:left;
       vertical-align:top}
 td.r,th.r{text-align:right} code{color:#9ecbff;font-size:12px;word-break:break-all}
 .card{background:#212a38;border-radius:10px;padding:10px 12px;margin:10px 0;
       overflow-x:auto}
 input,button{font-size:16px;padding:8px;border-radius:8px}
 input{background:#141a24;color:#e6e9ef;border:1px solid #394456;width:60%}
 button{background:#2d6cdf;color:#fff;border:0;margin-left:6px}
 .nav{margin:2px 0 10px}
 .nav a,.nav span{margin-right:12px;font-size:15px}
 .nav a{color:#9ecbff;text-decoration:none}
 .nav .here{color:#e6e9ef;font-weight:700}
 .pill{display:inline-block;background:#2a3242;border-radius:6px;padding:1px 7px;
       font-size:12px;margin:1px 3px 1px 0;color:#c6cddb;border:0}
 .pill.on{background:#2d6cdf;color:#fff}
"""

_PLUMBING = """
function hdrs(){const h=new Headers();h.set('X-Dash-Key',localStorage.getItem('dashKey')||'');return h;}
function saveKey(){localStorage.setItem('dashKey',document.getElementById('k').value);load();}
function usd(x){return '$'+(x||0).toFixed(2);}
function pc(x){return ((x||0)*100).toFixed(1)+'c';}
function pct(x){return ((x||0)*100).toFixed(0)+'%';}
function when(t){return new Date(t*1000).toLocaleTimeString([], {hour:'numeric',minute:'2-digit'});}
function row(c){return '<tr>'+c.map(function(x,i){return '<td class="'+(i?'r':'')+'">'+x+'</td>';}).join('')+'</tr>';}
function hrow(c){return '<tr>'+c.map(function(x,i){return '<th class="'+(i?'r':'')+'">'+x+'</th>';}).join('')+'</tr>';}
function load(){
 fetch('data.json',{headers:hdrs(),cache:'no-store'}).then(function(r){
  if(r.status===401){document.getElementById('login').style.display='block';
    document.getElementById('view').innerHTML='';return null;}
  return r.json();
 }).then(function(d){
  if(!d)return;
  window._d=d;
  document.getElementById('login').style.display='none';
  document.getElementById('view').innerHTML=render(d);
 }).catch(function(){document.getElementById('view').innerHTML='<div class="card bad">unreachable</div>';});
}
function rerender(){if(window._d)document.getElementById('view').innerHTML=render(window._d);}
function setF(x){window._filter=x;rerender();}
"""


def _page(active: str, title: str, render_js: str, controls: str = "") -> str:
    nav = "".join(
        (f'<span class="here">{label}</span>' if label == active
         else f'<a href="{href}">{label}</a>')
        for label, href in NAV)
    return f"""<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><style>{_CSS}</style></head><body>
<h1>2.0</h1><div class="nav">{nav}</div>
<div id="login" class="card" style="display:none">
 <div class="muted">password</div>
 <input id="k" type="password"><button onclick="saveKey()">open</button>
</div>
{controls}
<div id="view" class="muted">loading&hellip;</div>
<script>{_PLUMBING}
function render(d){{{render_js}}}
load();setInterval(load,30000);
</script></body></html>"""


# ---------------------------------------------------------------------------
# page bodies (each is the body of render(d) -> html string)
# ---------------------------------------------------------------------------

STATUS_JS = """
 var age=Math.round(Date.now()/1000-d.saved_at);
 var fresh=age<120?'<span class="ok">&#9679; live</span>':'<span class="bad">&#9679; stale '+age+'s</span>';
 var e=d.estimator||{};var g=d.engine||{};var sw=d.switch||{};
 var h='<div class="card">'+fresh+' <span class="muted">build '+(d.build||'?')+
   ' &middot; ws '+((d.ws||{}).state||'?')+' &middot; '+(d.orders_n||0)+' orders in '+(d.markets_n||0)+' markets</span>'+
   '<div class="big">'+usd(e.earned)+'<span class="muted" style="font-size:15px"> earned today ('+(e.day||'')+')</span></div>'+
   '<div>'+usd(e.rate)+'/day now'+
   (e.stale_s>60?' <span class="warn">&middot; '+Math.round(e.stale_s/60)+' min unmeasured</span>':'')+'</div></div>';
 h+='<div class="card"><b>Engine</b> <span class="muted">'+(g.mode||'?')+
   ' &middot; switch '+(sw.on?'<span class="ok">ON</span>':'<span class="muted">off</span>')+'</span>'+
   '<div>at risk '+usd(g.used)+' of '+usd(g.ceiling)+' &middot; headroom '+usd(g.headroom)+'</div>';
 if(g.sweep&&!g.sweep.done){h+='<div class="warn">handover sweep running &middot; '+(g.sweep.cancelled||0)+' cleared so far</div>';}
 var go=g.orders||[];
 if(go.length){h+='<table>'+hrow(['market','order','why']);
  go.forEach(function(o){h+=row(['<code>'+o.market+'</code>',o.side+' '+o.qty+' @ '+pc(o.price),o.purpose]);});
  h+='</table>';}else{h+='<div class="muted">no engine orders resting</div>';}
 if(g.silent_cancels){h+='<div class="warn muted">'+g.silent_cancels+' silent cancels seen</div>';}
 h+='<div class="muted" style="margin-top:4px"><a href="orders" style="color:#9ecbff">orders &rarr;</a></div></div>';
 var mr=Object.entries(e.market_rates||{}).sort(function(a,b){return b[1]-a[1];});
 if(mr.length){h+='<div class="card"><b>Where the rate comes from</b><table>'+hrow(['market','$/day','earned']);
  mr.slice(0,25).forEach(function(kv){h+=row(['<code>'+kv[0]+'</code>',usd(kv[1]),usd((e.per_market||{})[kv[0]])]);});
  h+='</table></div>';}
 var th=(d.terms_history||[]).slice(-10).reverse();
 if(th.length){h+='<div class="card"><b>Reward terms log</b><table>';
  th.forEach(function(t){h+=row([when(t.ts),'<code>'+t.slug+'</code>',
    t.why+(t.pool!=null?(' $'+t.pool+' / '+t.target+' / df '+t.df+' / &divide;'+t.event_n):'')]);});
  h+='</table></div>';}
 var er=(d.errors||[]).slice(-6).reverse();
 if(er.length){h+='<div class="card"><b class="warn">Recent trouble</b><div class="muted">'+er.join('<br>')+'</div></div>';}
 return h;
"""

ORDERS_JS = """
 var g=d.engine||{};var fx={};(d.forecasts||[]).forEach(function(f){if(f.id)fx[f.id]=f;});
 var h='<div class="card"><b>Resting now</b> <span class="muted">what the engine expects of each order</span>';
 var go=g.orders||[];
 if(go.length){h+='<table>'+hrow(['market','order','why','earn/d','p(fill)/d','fill cost','EV/d']);
  go.forEach(function(o){var f=fx[o.id]||{};
   h+=row(['<code>'+o.market+'</code>',o.side+' '+o.qty+' @ '+pc(o.price),o.purpose,
     usd(f.exp_earn),f.p_fill!=null?pct(f.p_fill):'?',
     f.fill_cost!=null?pc(f.fill_cost):'?',f.ev!=null?usd(f.ev):'?']);});
  h+='</table>';}else{h+='<div class="muted">nothing resting</div>';}
 h+='</div>';
 var closed=(d.forecasts||[]).filter(function(f){return f.how;}).reverse();
 if(closed.length){h+='<div class="card"><b>Recent outcomes</b> <span class="muted">predictions vs what happened</span>'+
  '<table>'+hrow(['market','order','predicted','outcome']);
  closed.slice(0,25).forEach(function(f){
   var out=f.how+(f.rested_s?' after '+Math.round(f.rested_s/60)+'m':'');
   if(f.how==='fill'){out='<span class="warn">filled</span> '+(f.filled_qty||'')+
     (f.adverse!=null?' &middot; adverse '+pc(f.adverse):' &middot; mark pending');}
   h+=row(['<code>'+f.market+'</code>',f.side+' '+f.qty+' @ '+pc(f.price),
     'p(fill) '+pct(f.p_fill)+' &middot; EV '+usd(f.ev),out]);});
  h+='</table></div>';}
 return h;
"""

MARKETS_JS = """
 var h='';var fairs=d.fairs||{};var lad=d.ladders||{};var g=d.engine||{};
 var e=d.estimator||{};var ours={};(g.orders||[]).forEach(function(o){
  (ours[o.market]=ours[o.market]||[]).push(o.side[0]+o.qty+'@'+pc(o.price));});
 function rungKey(s){var t=s.split('-').pop();
  if(t.indexOf('lte')===0)return parseInt(t.slice(3))-0.5;
  if(t.indexOf('gte')===0)return parseInt(t.slice(3))+0.5;
  return parseInt(t);}
 [['Senate seats (GOP count)','scc-senate-gop-'],['House seats (GOP &ge; N)','scc-hrep-rep-']]
 .forEach(function(fam){
  var slugs=Object.keys(lad).filter(function(s){return s.indexOf(fam[1])===0;})
    .sort(function(a,b){return rungKey(a)-rungKey(b);});
  if(!slugs.length)return;
  h+='<div class="card"><b>'+fam[0]+'</b><table>'+hrow(['rung','model','bid/ask','ours','$/day']);
  slugs.forEach(function(s){var L=lad[s];var bb=L.bids[0]?pc(L.bids[0][0]):'&mdash;';
   var ba=L.asks[0]?pc(L.asks[0][0]):'&mdash;';
   h+=row([s.split('-').pop(),fairs[s]!=null?pc(fairs[s]):'<span class="muted">&mdash;</span>',
     bb+' / '+ba,(ours[s]||[]).join('<br>')||'<span class="muted">&middot;</span>',
     usd((e.market_rates||{})[s])]);});
  h+='</table><div class="muted">model = seat distribution from Silver per-race odds; blank = no model</div></div>';
 });
 var t=d.touch||{};var q=window._q||'';
 var f=window._filter||'all';
 var rows=Object.keys(t).filter(function(s){
   if(f==='senate')return s.indexOf('scc-senate-gop-')===0;
   if(f==='house')return s.indexOf('scc-hrep-rep-')===0;
   if(f==='other')return s.indexOf('scc-')!==0;
   return true;
 }).filter(function(s){return s.indexOf(q)>=0;})
 .sort(function(a,b){return ((e.market_rates||{})[b]||0)-((e.market_rates||{})[a]||0);});
 h+='<div class="card"><b>All measured markets</b> <span class="muted">'+f+
  (q?' &middot; \\u201c'+q+'\\u201d':'')+'</span>'+
  '<table>'+hrow(['market','bid/ask','depth b/a','$/day']);
 rows.slice(0,60).forEach(function(s){var v=t[s];
  h+=row(['<code>'+s+'</code>',(v[0]||'?')+' / '+(v[1]||'?')+'c',
    (v[2]||0).toLocaleString()+' / '+(v[3]||0).toLocaleString(),
    usd((e.market_rates||{})[s])]);});
 h+='</table><div class="muted">'+rows.length+' markets match</div></div>';
 return h;
"""

OPPS_JS = """
 var g=d.engine||{};var h='';
 var cands=g.cands||[];
 h+='<div class="card"><b>What the engine wants next</b> <span class="muted">ranked by EV per dollar</span>';
 if(cands.length){h+='<table>'+hrow(['market','order','earn/d','p(fill)','fill cost','EV/d','why']);
  cands.forEach(function(c){h+=row(['<code>'+c.market+'</code>',
    c.side+' '+c.qty+' @ '+pc(c.price),usd(c.exp_earn),pct(c.p_fill),
    pc(c.fill_cost),usd(c.ev),c.purpose+(c.exp1_gap?' &middot; EXP-1':'')]);});
  h+='</table>';}else{h+='<div class="muted">nothing above the bar right now</div>';}
 h+='</div>';
 var rej=g.rejected||[];
 if(rej.length){h+='<div class="card"><b>Turned down</b> <span class="muted">best of the rejected — EV under the bar</span>'+
  '<table>'+hrow(['market','order','earn/d','risk cost/d','EV/d']);
  rej.forEach(function(c){h+=row(['<code>'+c.market+'</code>',c.side+' '+c.qty+' @ '+pc(c.price),
    usd(c.exp_earn),usd(c.p_fill*c.fill_cost*c.qty),usd(c.ev)]);});
  h+='</table></div>';}
 var fm=d.fillmodel||{};var hz=fm.hazards||{};
 h+='<div class="card"><b>Calibration</b> <span class="muted">fills/day by distance from the touch &middot; learned from the feed</span><table>'+
  hrow(['family &amp; side','touch','1 back','2 back','3+','hours seen']);
 Object.keys(hz).forEach(function(k){var r=hz[k];
  h+=row([k,(r[0]||{}).per_day,(r[1]||{}).per_day,(r[2]||{}).per_day,(r[3]||{}).per_day,
    (r[0]||{}).hours_observed]);});
 h+='</table><div class="muted">adverse fill markdown: '+JSON.stringify(fm.markdown||{})+
  ' &middot; scoring fraction: '+JSON.stringify(fm.scoring_frac||{})+'</div></div>';
 var ex=((d.engine_saved||{}).exp1||[]).slice(-15).reverse();
 h+='<div class="card"><b>EXP-1 pool</b> <span class="muted">the window-boundary experiment: level says it earns, queue says zero &middot; graded against payouts</span>';
 if(ex.length){h+='<table>'+hrow(['placed','market','order','level says','queue says']);
  ex.forEach(function(x){h+=row([when(x.ts),'<code>'+x.market+'</code>',
    x.side+' '+x.qty+' @ '+pc(x.price),usd(x.pred_level_day)+'/d',usd(x.pred_queue_day)+'/d']);});
  h+='</table>';}else{h+='<div class="muted">no boundary setups placed yet</div>';}
 h+='</div>';
 return h;
"""

LOG_JS = """
 var h='';var es=d.engine_saved||{};
 function card(title,rows,fmt){
  h+='<div class="card"><b>'+title+'</b>';
  if(rows&&rows.length){h+='<table>';rows.slice(-30).reverse().forEach(function(x){h+=fmt(x);});h+='</table>';}
  else{h+='<div class="muted">nothing yet</div>';}
  h+='</div>';}
 card('Engine events',es.log,function(x){
  var rest=Object.keys(x).filter(function(k){return k!=='ts'&&k!=='event';})
   .map(function(k){return k+'='+x[k];}).join(' ');
  return row([when(x.ts),x.event,'<span class="muted">'+rest+'</span>']);});
 card('Order desk',d.audit,function(x){
  var rest=Object.keys(x).filter(function(k){return k!=='ts';})
   .map(function(k){return k+'='+x[k];}).join(' ');
  return row([when(x.ts),'<span class="muted">'+rest+'</span>']);});
 card('Alerts',d.alert_log,function(x){
  return row([when(x.ts),(x.sent?'&#128276;':'<span class="muted">held</span>'),
    x.title+' <span class="muted">'+(x.msg||'')+(x.why?' ('+x.why+')':'')+'</span>']);});
 card('Trouble',(d.errors||[]).map(function(e){return {ts:0,line:e};}),function(x){
  return row(['<span class="muted">'+x.line+'</span>']);});
 return h;
"""


def build_shells() -> dict[str, str]:
    return {
        "/": _page("status", "2.0", STATUS_JS),
        "/orders": _page("orders", "2.0 orders", ORDERS_JS),
        "/markets": _page(
            "markets", "2.0 markets", MARKETS_JS,
            controls='<div style="margin:0 0 8px">'
                     '<button class="pill" onclick="setF(\'all\')">all</button>'
                     '<button class="pill" onclick="setF(\'senate\')">senate seats</button>'
                     '<button class="pill" onclick="setF(\'house\')">house seats</button>'
                     '<button class="pill" onclick="setF(\'other\')">other</button>'
                     ' <input id="q" placeholder="search slug" style="width:38%"'
                     ' oninput="window._q=this.value;rerender()"></div>'),
        "/opps": _page("opps", "2.0 opportunities", OPPS_JS),
        "/log": _page("log", "2.0 log", LOG_JS),
    }


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
 a{color:#9ecbff;text-decoration:none}
</style></head><body>
<h1>2.0 master switch</h1>
<div style="margin:2px 0 10px"><a href=".">status</a> &middot; <a href="orders">orders</a>
 &middot; <a href="markets">markets</a> &middot; <a href="opps">opps</a> &middot; <a href="log">log</a></div>
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
        if route == "":
            route = "/"
        shell = self.server.shells.get(route)
        if shell is not None:
            self._send(200, "text/html; charset=utf-8", shell.encode())
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
        self.shells = build_shells()
        self.password = (password if password is not None
                         else os.environ.get("DASH_PASSWORD", ""))
        port = port if port is not None else int(os.environ.get("V2_PORT", DEFAULT_PORT))
        bind = bind if bind is not None else os.environ.get("V2_BIND", DEFAULT_BIND)
        super().__init__((bind, port), _Handler)

    def start_background(self) -> None:
        threading.Thread(target=self.serve_forever, daemon=True, name="v2-web").start()
