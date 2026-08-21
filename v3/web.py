"""3.0's pages — a few small ones, each answering one question, in 1.0's
voice: summary before detail, plain English on every number, never a bare
slug where a name will fit.

    /          am I earning, is the data fresh, what is armed?
    /orders    every resting order: its name, its verdict, move/cancel
    /plan      what would 3.0 do next, and why?
    /switch    the switches (master + per family) and the risk line
    /log       what happened recently, in words

Served on localhost; 1.0's monitor is the container's front door and
forwards /v3/* here, so the browser's stored dashKey just works. Pages
are public SHELLS holding no data; data.json underneath demands the key.
The only mutating route is /op — auth plus the X-Reprice CSRF header.
"""

from __future__ import annotations

import base64
import json
import os
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

DEFAULT_PORT = 8092
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


NAV = (("status", "."), ("orders", "orders"), ("plan", "plan"),
       ("grades", "grades"), ("log", "log"), ("switch", "switch"))

_CSS = """
 body{background:#151b12;color:#e8ecdf;font:16px/1.45 -apple-system,system-ui,sans-serif;
      margin:0;padding:14px;max-width:680px;margin:auto}
 h1{font-size:19px;margin:4px 0 6px} .muted{color:#93a08a;font-size:13px}
 .big{font-size:34px;font-weight:700;margin:2px 0}
 .ok{color:#7fd77f}.bad{color:#ff8a7a}.warn{color:#ffd06b}
 table{border-collapse:collapse;width:100%;font-size:13px;margin:6px 0}
 td,th{padding:4px 6px;border-bottom:1px solid #2c3527;text-align:left;
       vertical-align:top}
 td.r,th.r{text-align:right} code{color:#b9d98f;font-size:12px;word-break:break-all}
 .card{background:#1f2818;border-radius:10px;padding:10px 12px;margin:10px 0;
       overflow-x:auto}
 input,button{font-size:16px;padding:8px;border-radius:8px}
 input{background:#12180d;color:#e8ecdf;border:1px solid #3c4a2f;width:60%}
 button{background:#4c7a2f;color:#fff;border:0;margin-left:6px}
 button.off{background:#7a3a2f}
 button.small{font-size:13px;padding:4px 9px;margin:0 0 0 6px}
 .nav{margin:2px 0 10px}
 .nav a,.nav span{margin-right:12px;font-size:15px}
 .nav a{color:#b9d98f;text-decoration:none}
 .nav .here{color:#e8ecdf;font-weight:700}
 .pill{display:inline-block;background:#2c3527;border-radius:6px;padding:1px 7px;
       font-size:12px;margin:1px 3px 1px 0;color:#cfd8c2}
 .pill.on{background:#4c7a2f;color:#fff}
 .stats{display:flex;gap:20px;flex-wrap:wrap;margin:8px 0 2px}
 .stat .lab{color:#93a08a;font-size:12px}
 .stat .val{font-size:22px;font-weight:700}
 .stat .val .u{font-size:13px;font-weight:400;color:#93a08a}
 .sub{color:#b6c1a8;font-size:14px;margin:3px 0}
 .hint{color:#93a08a;font-size:12.5px;margin:5px 0 2px;line-height:1.5}
 details.how{margin:6px 0 0;font-size:12.5px;color:#93a08a;line-height:1.5}
 details.how summary{color:#79856d;font-size:12px;cursor:pointer}
 summary{cursor:pointer}
 .vrd{color:#93a08a;font-size:12px;margin:1px 0 4px}
 .name{font-size:13.5px}
 .mtrack{height:10px;background:#2c3d20;border-radius:5px;margin:8px 0 2px;
         position:relative;overflow:hidden}
 .mfill{position:absolute;left:0;top:0;bottom:0;background:#4c7a2f;
        border-radius:5px}
"""

_PLUMBING = """
function hdrs(){const h=new Headers();h.set('X-Dash-Key',localStorage.getItem('dashKey')||'');return h;}
function saveKey(){localStorage.setItem('dashKey',document.getElementById('k').value);load();}
function usd(x){var v=x||0;return (v<0?'\\u2212$':'$')+Math.abs(v).toFixed(2);}
function pc(x){var v=Math.round((x||0)*1000)/10;return (v%1?v.toFixed(1):''+Math.round(v))+'\\u00A2';}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function when(t){return new Date(t*1000).toLocaleTimeString([], {hour:'numeric',minute:'2-digit'});}
function row(c){return '<tr>'+c.map(function(x,i){return '<td class="'+(i?'r':'')+'">'+x+'</td>';}).join('')+'</tr>';}
function nm(d,s){return esc((d.labels&&d.labels[s])||s);}
function fams(d){var out=[];for(var k in (d.summaries||{})){out.push([k,d.summaries[k]]);}return out;}
function post(body,cb){
 var h=hdrs();h.set('X-Reprice','1');h.set('Content-Type','application/json');
 fetch('op',{method:'POST',headers:h,body:JSON.stringify(body)})
  .then(function(r){return r.json();}).then(function(j){if(cb)cb(j);load();})
  .catch(function(){alert('unreachable');});
}
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
load();setInterval(load,30000);
"""


def _shell(title: str, here: str, render_js: str) -> str:
    nav = "".join(
        (f'<span class="here">{label}</span>' if label == here
         else f'<a href="{href}">{label}</a>')
        for label, href in NAV)
    return f"""<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Cache-Control" content="no-store">
<title>{title}</title><style>{_CSS}</style></head><body>
<h1>{title}</h1><div class="nav">{nav}</div>
<div id="login" style="display:none" class="card">
 <div class="sub">This page needs the dashboard key.</div>
 <input id="k" type="password" placeholder="key"><button onclick="saveKey()">Open</button>
</div>
<div id="view" class="muted">loading&hellip;</div>
<script>{render_js}{_PLUMBING}</script>
</body></html>"""


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

STATUS_JS = """
function render(d){
 var out='';
 var age=Math.max(0,Math.round(Date.now()/1000-(d.saved_at||0)));
 out+='<div class="card">'+(age<180
   ?'<span class="ok">\\u2705 fresh</span> <span class="muted">\\u2014 updated '+age+'s ago</span>'
   :'<span class="bad">\\u274C stale</span> <span class="muted">\\u2014 last update '+Math.round(age/60)+' min ago; the loop may be down</span>');
 var sv=(d.switch_view||{});var m=(sv.master||{});
 out+='<div style="margin-top:6px">'
   +'<span class="pill'+(m.on?' on':'')+'">master '+(m.on?'ON':'off')+'</span>';
 for(var k in sv){if(k==='master')continue;
  out+='<span class="pill'+(sv[k].on?' on':'')+'">'+esc(k)+' '+(sv[k].on?'ON':'off')+'</span>';}
 out+='</div>';
 var fl=(d.floor||{});
 if(m.on&&!fl.acked){out+='<div class="warn" style="margin-top:6px">Armed \\u2014 waiting for 1.0 and 2.0 to stand down (they halt within a minute; nothing is touched until both confirm).</div>';}
 else if(m.on&&fl.acked){out+='<div class="ok" style="margin-top:6px">3.0 has the floor \\u2014 1.0 and 2.0 automation is standing down.</div>';}
 var fz=(d.flatten||{});
 if(fz.active&&fz.phase!=='rebuild'){out+='<div class="warn" style="margin-top:6px">FLATTEN: cancelling every order that isn\\u2019t an exit \\u2014 '+(fz.cancelled_total||0)+' cancelled, '+(fz.kept_exits||0)+' exits kept, '+(fz.remaining||0)+' to go. Nothing that costs money will be placed.</div>';}
 else if(fz.active){out+='<div class="ok" style="margin-top:6px">Flat \\u2014 '+(fz.kept_exits||0)+' exits resting and earning. Rebuilding politics under the $100 ceiling, best-paying markets first.</div>';}
 out+='<div class="hint">Nothing places orders unless the master switch AND that family\\u2019s own switch are on. Master ON hands ALL automation to 3.0: 1.0 and 2.0 halt first, then 3.0 takes over their resting orders and runs them under its own rules. Master OFF hands it back. Flips happen on the switch page, never here.</div></div>';
 fams(d).forEach(function(kv){
  var k=kv[0],s=kv[1];
  out+='<div class="card"><b>'+esc(s.name||k)+'</b> ';
  if(s.error){out+='<div class="bad">cycle error: '+esc(s.error)+'</div></div>';return;}
  out+='<span class="pill">'+esc(s.mode)+'</span>';
  if(s.mode==='observing'){out+='<div class="hint">The switch is off, so this family is watching only \\u2014 scoring the board and showing what it WOULD do on the plan page. Nothing is placed.</div>';}
  if(s.mode==='waiting for the floor'){out+='<div class="warn">Armed, but 1.0/2.0 have not yet confirmed they\\u2019ve stood down \\u2014 acting the moment they do.</div>';}
  if(s.would_adopt){out+='<div class="sub">Will take over <b>'+s.would_adopt+'</b> resting orders from the earlier versions the moment it\\u2019s armed \\u2014 they keep resting; 3.0 just becomes the one maintaining them.</div>';}
  out+='<div class="stats">'
   +'<div class="stat"><div class="lab">resting earns about</div><div class="val">'+usd(s.est_day)+'<span class="u">/day</span></div></div>'
   +'<div class="stat"><div class="lab">earned today so far</div><div class="val">'+usd(s.earned_today)+'</div></div>'
   +'<div class="stat"><div class="lab">orders</div><div class="val">'+(s.orders||[]).length+'<span class="u"> in '+(s.active||0)+' mkts</span></div></div>'
   +'</div>';
  var cap=s.capital_usd||0,sp=s.spent||0;
  out+='<div class="mtrack"><div class="mfill" style="width:'+Math.min(100,cap?100*sp/cap:0)+'%"></div></div>'
   +'<div class="muted">'+usd(sp)+' of the '+usd(cap)+' risk ceiling is on the book \\u2014 the one number that binds.</div>';
  if(s.stock_day){out+='<div class="sub">Stock waiting to sell is earning '+usd(s.stock_day)+'/day while it waits.</div>';}
  var inv=s.inventory||{};var invn=Object.keys(inv).length;
  if(invn){out+='<div class="muted">'+invn+' position'+(invn>1?'s':'')+' held from fills \\u2014 see orders page.</div>';}
  out+='<div class="muted">'+(s.markets||0)+' markets known, '+(s.scanned||0)+' scored'
  if(s.unmeasured_min>1){out+='<div class="muted">'+s.unmeasured_min+' min of today went unmeasured (books too stale to score) \\u2014 counted as zero, never guessed.</div>';}
   +(s.resting_ok===false?' \\u2014 <span class="warn">game window: resting is paused</span>':'')+'.</div>';
  out+='</div>';
 });
 var ws=(d.ws||{});
 if(ws.state){out+='<div class="muted">book stream: '+esc(ws.state)+(ws.subscribed?' ('+ws.subscribed+' markets live)':'')+'</div>';}
 var errs=d.errors||[];
 if(errs.length){out+='<div class="card"><details><summary class="muted">recent notes ('+errs.length+')</summary>';
  errs.slice(-8).reverse().forEach(function(e){out+='<div class="muted">'+esc(e)+'</div>';});
  out+='</details></div>';}
 out+='<details class="how"><summary>what these numbers mean</summary>'
  +'"Resting earns about" is the live arithmetic on real reward terms: our share of each side\\u2019s score times the side\\u2019s daily pool, using the exchange\\u2019s own pool, Target Size and discount factor. No fudge factors \\u2014 if it\\u2019s wrong, an input is wrong. '
  +'"Earned today" adds that rate up through the day, and only while enough books are fresh; blind stretches add nothing rather than a guess. '
  +'A market only ever shows a dollar figure once I\\u2019ve confirmed how many markets share its event\\u2019s pool.</details>';
 out+='<div class="muted" style="margin-top:8px">build '+esc(d.build||'?')+'</div>';
 return out;
}
"""

ORDERS_JS = """
function fold(title,sub,body,open){
 return '<details'+(open?' open':'')+'><summary><b>'+title+'</b> <span class="muted">'+sub+'</span></summary>'+body+'</details>';
}
function orow(d,o){
 var e=(o.live_est!=null?o.live_est:o.est_day);
 return '<div style="margin:9px 0 0;border-top:1px solid #2c3527;padding-top:7px">'
  +'<div class="name">'+nm(d,o.market)+'</div>'
  +'<div class="muted"><code>'+esc(o.market)+'</code></div>'
  +'<div class="sub">'+(o.side==='BUY'?'bid':'ask')+' '+(o.qty||0)+' @ '+pc(o.price)
  +' \\u2014 '+(e==null?'<span class="warn">no estimate yet</span>':usd(e)+'/day')
  +' <span class="pill">'+esc(o.purpose)+'</span></div>'
  +(o.verdict?'<div class="vrd">'+esc(o.verdict)+'</div>':'')
  +(o.why?'<div class="vrd">placed because: '+esc(o.why)+'</div>':'')
  +'<div><button class="small" onclick="mv(\\''+esc(o.id)+'\\','+o.price+')">Move</button>'
  +'<button class="small off" onclick="cx(\\''+esc(o.id)+'\\')">Cancel</button></div>'
  +'</div>';
}
function render(d){
 var out='';var any=false;
 fams(d).forEach(function(kv){
  var k=kv[0],s=kv[1];var os=(s.orders||[]);
  if(!os.length)return; any=true;
  var byest=function(a,b){return ((b.live_est!=null?b.live_est:b.est_day)||0)-((a.live_est!=null?a.live_est:a.est_day)||0);};
  var earn=os.filter(function(o){return o.purpose!=='sell';}).sort(byest);
  var sell=os.filter(function(o){return o.purpose==='sell';}).sort(byest);
  var esum=0;earn.forEach(function(o){esum+=(o.live_est!=null?o.live_est:o.est_day)||0;});
  var ssum=0;sell.forEach(function(o){ssum+=(o.live_est!=null?o.live_est:o.est_day)||0;});
  out+='<div class="card"><b>'+esc(s.name||k)+'</b>';
  if(earn.length){
   var eb='';earn.forEach(function(o){eb+=orow(d,o);});
   out+=fold('Earning','\\u2014 '+earn.length+' order'+(earn.length!==1?'s':'')+', ~'+usd(esum)+'/day',eb,true);
  }else{out+='<div class="muted" style="margin:8px 0 0">No earning orders resting.</div>';}
  if(sell.length){
   var sb='';sell.forEach(function(o){sb+=orow(d,o);});
   out+=fold('Exits','\\u2014 '+sell.length+' order'+(sell.length!==1?'s':'')+', earning ~'+usd(ssum)+'/day while they wait',sb,false);
  }
  out+='</div>';
 });
 if(!any)out+='<div class="card muted">No resting orders. When a family is armed and finds something worth resting in, each order shows here with its name, its verdict, and its own Move/Cancel.</div>';
 return out;
}
function mv(id,px){
 var v=prompt('New price in cents (e.g. 3.4):',(px*100).toFixed(1));
 if(v==null)return; var p=parseFloat(v)/100;
 if(!(p>0&&p<1)){alert('price must be between 0.1c and 99.9c');return;}
 post({op:'move',order_id:id,price:p},function(j){if(!j.ok)alert(j.note||'refused');});
}
function cx(id){
 if(!confirm('Cancel this order?'))return;
 post({op:'cancel',order_id:id},function(j){if(!j.ok)alert(j.note||'refused');});
}
"""

PLAN_JS = """
function render(d){
 var out='';
 fams(d).forEach(function(kv){
  var k=kv[0],s=kv[1];
  out+='<div class="card"><b>'+esc(s.name||k)+'</b> <span class="pill">'+esc(s.mode)+'</span>';
  if(s.mode==='observing'){out+='<div class="hint">Switch is off \\u2014 nothing below will be placed. This is exactly what I would do if you armed it, so it can be judged first.</div>';}
  var best=s.best_idle||[];
  if(!best.length){out+='<div class="muted">Nothing worth entering right now \\u2014 every scored market either pays under the bar, is louder than the courtesy share, resolves too soon, or has a dead side I don\\u2019t revive.</div></div>';return;}
  out+='<div class="sub">Best candidates, best first:</div>';
  best.forEach(function(b){
   out+='<div style="margin:8px 0 0;border-top:1px solid #2c3527;padding-top:6px">'
    +'<div class="name">'+esc(b.name||b.market)+'</div>'
    +'<div class="muted"><code>'+esc(b.market)+'</code> \\u2014 worth ~'+usd(b.est)+'/day</div>';
   (b.plans||[]).forEach(function(p){
    out+='<div class="vrd">'+(p.side==='BUY'?'bid':'ask')+' '+p.qty+' @ '+pc(p.px)
     +' ('+usd(p.cost)+' at risk) \\u2014 '+esc(p.why||'')+'</div>';
   });
   out+='</div>';
  });
  out+='</div>';
 });
 return out;
}
"""

SWITCH_JS = """
function render(d){
 var sv=(d.switch_view||{});var out='';
 var order=['master'];for(var k in sv){if(k!=='master')order.push(k);}
 order.forEach(function(k){
  var s=sv[k]||{};var label=(k==='master'?'Master switch \\u2014 all of 3.0':k+' switch');
  var sm=(d.summaries||{})[k];
  out+='<div class="card"><b>'+esc(label)+'</b> ';
  out+=s.on?'<span class="pill on">ON</span>':(s.armed?'<span class="pill">armed</span>':'<span class="pill">off</span>');
  if(sm){out+='<div class="muted">'+usd(sm.spent)+' of '+usd(sm.capital_usd)+' at risk; resting earns ~'+usd(sm.est_day)+'/day.</div>';}
  if(k==='master'){out+='<div class="hint">Master gates every family, and it moves the whole operation: ON asks 1.0 and 2.0 to halt their automation first \\u2014 3.0 touches nothing until both confirm \\u2014 then 3.0 adopts every resting order in its families and runs the book alone. OFF hands the floor straight back. One tap here stops all of 3.0.</div>';
   var fl=(window._d&&window._d.floor)||{};
   if(s.on){out+=fl.acked?'<div class="ok">1.0 and 2.0 have stood down \\u2014 3.0 has the floor.</div>':'<div class="warn">Waiting for 1.0/2.0 to stand down\\u2026</div>';}}
  if(s.on){out+='<div><button class="off" onclick="tap(\\'off\\',\\''+k+'\\')">Turn OFF</button></div>';}
  else if(s.armed){out+='<div class="sub warn">Armed \\u2014 confirm within '+(s.arm_expires_in||0)+'s to turn on.</div>'
   +'<div><button onclick="tap(\\'confirm\\',\\''+k+'\\')">Confirm ON</button>'
   +'<button class="off" onclick="tap(\\'off\\',\\''+k+'\\')">Never mind</button></div>';}
  else{out+='<div><button onclick="tap(\\'arm\\',\\''+k+'\\')">Arm&hellip;</button></div>'
   +'<div class="hint">Turning on takes two taps (arm, then confirm). Turning off takes one. Every flip is logged and pushed to the phone.</div>';}
  var lg=(s.log||[]);
  if(lg.length){out+='<details class="how"><summary>last flips</summary>';
   lg.slice(-6).reverse().forEach(function(r){out+='<div class="muted">'+when(r.ts)+' \\u2014 '+esc(r.action)+'</div>';});
   out+='</details>';}
  out+='</div>';
 });
 return out;
}
function tap(op,which){post({op:'switch_'+op,which:which});}
"""

LOG_JS = """
function render(d){
 var rows=[];
 fams(d).forEach(function(kv){
  var k=kv[0],s=kv[1];
  ((d['fam_log_'+k])||[]).forEach(function(r){rows.push([r.ts||0,esc(s.name||k),r]);});
 });
 (d.audit||[]).forEach(function(r){rows.push([r.ts||0,'rails',r]);});
 (d.alerts_log||[]).forEach(function(r){rows.push([r.ts||0,'alert',r]);});
 rows.sort(function(a,b){return b[0]-a[0];});
 var out='<div class="card">';
 if(!rows.length)out+='<div class="muted">Nothing yet.</div>';
 rows.slice(0,80).forEach(function(t){
  var r=t[2];var line='';
  if(t[1]==='alert'){line=(r.sent?'pushed':'held')+': '+esc(r.title)+(r.why?' ('+esc(r.why)+')':'');}
  else if(r.event){line=esc(r.event)+(r.market?' \\u2014 '+nm(window._d,r.market):'')
    +(r.why?' \\u2014 '+esc(r.why):'')+(r.note?' \\u2014 '+esc(r.note):'')
    +(r.error?' \\u2014 '+esc(r.error):'');}
  else if(r.op){line=esc(r.op)+(r.market?' \\u2014 '+nm(window._d,r.market):'')
    +(r.refused?' \\u2014 refused: '+esc(r.refused):'')
    +(r.initiator?' ('+esc(r.initiator)+')':'');}
  else{line=esc(JSON.stringify(r)).slice(0,140);}
  out+='<div class="muted" style="margin:4px 0"><span class="pill">'+t[1]+'</span> '
    +when(t[0])+' \\u2014 '+line+'</div>';
 });
 return out+'</div>';
}
"""

GRADES_JS = """
function render(d){
 var rows=(d.grades||[]);
 var out='<div class="card"><b>Estimate vs. what the exchange paid</b>';
 out+='<div style="margin:6px 0"><button onclick="ckrw()">Check for new payouts now</button></div><div id="rwout"></div>';
 out+='<div class="hint">The estimate is 3.0's own sampler \\u2014 measured on an independent clock, accruing only while books are fresh. Actuals are the account's posted rewards (during the transition the older versions' books pay into the same number). No fudge factors: a gap means an input was wrong, and the unmeasured minutes say how much of the day went unscored.</div>';
 if(!rows.length){out+='<div class="muted">Nothing to grade yet \\u2014 the first full day under 3.0 lands tomorrow.</div>';}
 var mx=1;rows.forEach(function(r){mx=Math.max(mx,r.est||0,r.actual||0);});
 rows.slice().reverse().forEach(function(r){
  out+='<div style="margin:10px 0 0"><b>'+esc(r.day)+'</b>';
  out+=' <span class="muted">est '+(r.est==null?'\\u2014':usd(r.est))+' \\u00b7 paid '+(r.actual==null?'not posted yet':usd(r.actual))+(r.unmeasured_min>1?' \\u00b7 '+r.unmeasured_min+'m unmeasured':'')+'</span>';
  if(r.est!=null){out+='<div class="mtrack"><div class="mfill" style="width:'+(100*(r.est||0)/mx)+'%"></div></div>';}
  if(r.actual!=null){out+='<div class="mtrack"><div class="mfill" style="width:'+(100*(r.actual||0)/mx)+'%;background:#8a7a2f"></div></div>';}
  out+='</div>';
 });
 return out+'</div>';
}

function ckrw(){
 var el=document.getElementById('rwout');
 el.innerHTML='<div class="muted">checking the exchange\\u2026</div>';
 post({op:'refresh_rewards'},function(j){
  if(!j.ok){el.innerHTML='<div class="bad">'+esc(j.note||'failed')+'</div>';return;}
  var h='<div class="card"><b>'+(j.new_count||0)+' new or changed row'+(j.new_count!==1?'s':'')+'</b>';
  (j.new_rows||[]).slice().reverse().forEach(function(r){
   h+='<div class="sub">'+esc(r.day)+' \\u00b7 '+usd(r.usd)+' \\u00b7 '+esc(r.name)+' <span class="muted">'+esc(r.status)+'</span></div>';
  });
  if(!(j.new_rows||[]).length)h+='<div class="muted">Nothing new since the last check.</div>';
  el.innerHTML=h+'</div>';
 });
}
"""

PAGES = {
    "/": ("3.0 — status", "status", STATUS_JS),
    "/orders": ("3.0 — orders", "orders", ORDERS_JS),
    "/plan": ("3.0 — the plan", "plan", PLAN_JS),
    "/switch": ("3.0 — switches", "switch", SWITCH_JS),
    "/grades": ("3.0 — grades", "grades", GRADES_JS),
    "/log": ("3.0 — log", "log", LOG_JS),
}


class WebServer:
    def __init__(self, monitor, port: int | None = None, bind: str = DEFAULT_BIND):
        self.monitor = monitor
        self.port = port if port is not None else int(os.environ.get("V3_PORT", DEFAULT_PORT))
        self.bind = bind
        self.password = os.environ.get("DASH_PASSWORD", "")
        self._httpd: ThreadingHTTPServer | None = None

    def data_payload(self) -> dict:
        st = self.monitor.public_state()
        d = {k: v for k, v in st.items() if not k.startswith("fam_")}
        labels: dict[str, str] = {}
        slugs: set[str] = set()
        for key, s in (st.get("summaries") or {}).items():
            for o in s.get("orders") or []:
                slugs.add(o.get("market") or "")
            for b in s.get("best_idle") or []:
                slugs.add(b.get("market") or "")
            slugs.update((s.get("inventory") or {}).keys())
            fam = self.monitor.families.get(key)
            if fam is not None:
                d[f"fam_log_{key}"] = fam.log[-80:]
        for s in slugs:
            if s:
                labels[s] = self.monitor.names.label(s)
        d["labels"] = labels
        d["now"] = time.time()
        return d

    def handle_op(self, body: dict) -> dict:
        op = str(body.get("op") or "")
        if op.startswith("switch_"):
            return {"ok": True,
                    "state": self.monitor.switch_tap(op[len("switch_"):],
                                                     str(body.get("which") or "master"))}
        if op == "refresh_rewards":
            return self.monitor.refresh_rewards()
        if op in ("cancel", "move"):
            price = body.get("price")
            return self.monitor.order_op(op, str(body.get("order_id") or ""),
                                         float(price) if price is not None else None)
        return {"ok": False, "note": f"unknown op {op}"}

    def start(self) -> None:
        server = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *a):  # noqa: A003 — quiet
                pass

            def _send(self, code: int, ctype: str, body: bytes) -> None:
                self.send_response(code)
                self.send_header("Content-Type", ctype)
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):  # noqa: N802
                u = urlparse(self.path)
                route = u.path.rstrip("/") or "/"
                if route in PAGES:
                    title, here, js = PAGES[route]
                    self._send(200, "text/html; charset=utf-8",
                               _shell(title, here, js).encode())
                    return
                if route == "/data.json":
                    if not authed(self.headers.get, u.query, server.password):
                        self._send(401, "application/json", b'{"error":"key required"}')
                        return
                    self._send(200, "application/json",
                               json.dumps(server.data_payload()).encode())
                    return
                self._send(404, "text/plain", b"not found")

            def do_POST(self):  # noqa: N802
                u = urlparse(self.path)
                if u.path.rstrip("/") != "/op":
                    self._send(404, "text/plain", b"not found")
                    return
                if not authed(self.headers.get, u.query, server.password):
                    self._send(401, "application/json", b'{"error":"key required"}')
                    return
                if self.headers.get("X-Reprice") != "1":
                    self._send(403, "text/plain", b"missing X-Reprice header")
                    return
                try:
                    length = int(self.headers.get("Content-Length") or 0)
                    body = json.loads(self.rfile.read(length)) if length else {}
                except Exception:  # noqa: BLE001
                    self._send(400, "application/json", b'{"ok":false,"note":"bad request"}')
                    return
                try:
                    out = server.handle_op(body)
                except Exception as e:  # noqa: BLE001
                    out = {"ok": False, "note": f"{type(e).__name__}: {e}"}
                self._send(200, "application/json", json.dumps(out).encode())

        self._httpd = ThreadingHTTPServer((self.bind, self.port), Handler)
        t = threading.Thread(target=self._httpd.serve_forever, daemon=True)
        t.start()
