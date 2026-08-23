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
import gzip
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


NAV = (("meter", "."), ("watch", "watch"), ("fills", "fills"), ("status", "status"), ("orders", "orders"),
       ("plan", "plan"), ("model", "silver"),
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
 .tri{display:flex;gap:8px;margin:8px 0 2px}
 .tri-col{flex:1;min-width:0}
 .tri-h{font-size:11px;color:#79856d;margin:0 0 4px;text-transform:uppercase;
        letter-spacing:.4px}
 .tchip{border-radius:8px;padding:5px 8px;margin:4px 0;font-size:12px;
        background:#1a2214;border-left:3px solid #55482a;overflow:hidden}
 .tchip.win{border-left-color:#4c7a2f;background:#1c2a16}
 .tchip .tn{color:#e8ecdf;font-size:12px}
 .tchip .tm{color:#93a08a;font-size:11px}
 @keyframes triL{from{transform:translateX(70%);opacity:0}
                 to{transform:translateX(0);opacity:1}}
 @keyframes triR{from{transform:translateX(-70%);opacity:0}
                 to{transform:translateX(0);opacity:1}}
 .tchip.new-l{animation:triL .7s ease-out}
 .tchip.new-r{animation:triR .7s ease-out}
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
 fetch('/op',{method:'POST',headers:h,body:JSON.stringify(body)})
  .then(function(r){return r.json();}).then(function(j){if(cb)cb(j);load();})
  .catch(function(){alert('unreachable');});
}
function fmtsz(q){if(q>=1e6)return (q/1e6).toFixed(1)+'M';if(q>=1e3)return (q/1e3).toFixed(1)+'k';return ''+Math.round(q);}
function showbook(slug,el){
 var box=document.getElementById(el);
 if(!box)return;
 if(box.innerHTML){box.innerHTML='';return;}
 box.innerHTML='<div class="muted">fetching the book\u2026</div>';
 fetch('/book.json?m='+encodeURIComponent(slug),{headers:hdrs(),cache:'no-store'})
  .then(function(r){return r.json();}).then(function(b){
   if(!b.ok){box.innerHTML='<div class="muted">'+esc(b.note||'no book')+'</div>';return;}
   var oursAt={};(b.ours||[]).forEach(function(o){oursAt[o.side+(o.price*100).toFixed(1)]=o;});
   var g=b.fair!=null?'model '+(b.fair*100).toFixed(1)+'c':(b.band&&b.band.med!=null?'no model \u2014 evidence '+b.band.lo.toFixed(0)+'\u2013'+b.band.hi.toFixed(0)+'c, confidence '+Math.round((b.conf||0)*100)+'%':'NO GROUNDING \u2014 no model, no evidence');
   var h='<div class="muted" style="margin:4px 0">book '+b.age_s+'s old \u00b7 '+g+'</div>';
   h+='<table><tr><th class="r">bid size</th><th class="r">bid</th><th>ask</th><th>ask size</th></tr>';
   var n=Math.max((b.bids||[]).length,(b.asks||[]).length);
   for(var i=0;i<n;i++){
    var bd=(b.bids||[])[i],ak=(b.asks||[])[i];
    var bmark=bd&&oursAt['BUY'+(bd[0]*100).toFixed(1)]?' \u25CF':'';
    var amark=ak&&oursAt['SELL'+(ak[0]*100).toFixed(1)]?' \u25CF':'';
    h+='<tr><td class="r">'+(bd?fmtsz(bd[1]):'')+'</td><td class="r">'+(bd?pc(bd[0])+bmark:'')+'</td>'
      +'<td>'+(ak?pc(ak[0])+amark:'')+'</td><td>'+(ak?fmtsz(ak[1]):'')+'</td></tr>';
   }
   h+='</table><div class="hint">\u25CF marks a level where one of our orders rests.</div>';
   var lad=b.ladder||{};
   if(lad.ok&&lad.sides){
    if(lad.note)h+='<div class="muted">'+esc(lad.note)+'</div>';
    ['BUY','SELL'].forEach(function(side){
     var s=lad.sides[side]||{};var rows=s.rows||[];
     if(!rows.length)return;
     h+='<div class="muted" style="margin-top:8px"><b>'+(side==='BUY'?'bid':'ask')+' ladder</b> \u2014 what resting at each price would do</div>';
     h+='<table><tr><th class="r">price</th><th class="r">size</th><th class="r">share</th><th class="r">$/day</th><th class="r">fill odds</th><th class="r">fill cost</th><th class="r">EV/day</th></tr>';
     rows.forEach(function(r){
      var st=r.picked?' style="font-weight:bold"':(r.clears_bar?'':' class="muted"');
      h+='<tr'+st+'><td class="r">'+pc(r.px)+(r.picked?' \u25C0':'')+'</td><td class="r">'+r.qty+'</td><td class="r">'+Math.round(r.share*100)+'%</td>'
        +'<td class="r">'+usd(r.est)+'</td><td class="r">'+Math.round(r.p_fill*100)+'%</td>'
        +'<td class="r">'+(r.fill_cost*100).toFixed(1)+'c</td><td class="r">'+usd(r.ev)+'</td></tr>';
     });
     h+='</table>';
    });
    h+='<div class="hint">\u25C0 is the planner\u2019s pick; dim rows pay under the '+((lad.bar||0.75)*100).toFixed(0)+'c bar. Fill odds are per day; fill cost is per share.</div>';
   }else if(lad.note){h+='<div class="muted">ladder: '+esc(lad.note)+'</div>';}
   box.innerHTML=h;
  }).catch(function(){box.innerHTML='<div class="bad">unreachable</div>';});
}
function load(){
 fetch('/data.json',{headers:hdrs(),cache:'no-store'}).then(function(r){
  if(r.status===401){document.getElementById('login').style.display='block';
    document.getElementById('view').innerHTML='';return null;}
  return r.json();
 }).then(function(d){
  if(!d)return;
  window._d=d;
  document.getElementById('login').style.display='none';
  // reading protection (owner, 2026-08-22): while you are scrolled into
  // the page, refreshes HOLD — the data keeps arriving, but the page
  // only redraws when you are back near the top, so lists stay put and
  // your place is never lost
  if(window._loaded&&(window.scrollY||0)>120){
   window._held=true;
   var hb=document.getElementById('heldnote');
   if(!hb){hb=document.createElement('div');hb.id='heldnote';
    hb.style.cssText='position:fixed;bottom:10px;right:10px;background:rgba(0,0,0,0.55);color:#cfe3cf;padding:4px 10px;border-radius:8px;font-size:11px;z-index:9';
    hb.textContent='refresh held while you read \\u2014 scroll up to update';
    document.body.appendChild(hb);}
   return;
  }
  var hb2=document.getElementById('heldnote');if(hb2)hb2.remove();
  window._held=false;
  var y=window.scrollY||0;
  document.getElementById('view').innerHTML=render(d);
  if(y>0)window.scrollTo(0,y);
  window._loaded=true;
 }).catch(function(){if(!window._held)document.getElementById('view').innerHTML='<div class="card bad">unreachable</div>';});
}
load();setInterval(load,30000);
if(window.addEventListener)window.addEventListener('scroll',function(){
 if(window._held&&(window.scrollY||0)<=120&&window._d){
  window._held=false;
  var hb=document.getElementById('heldnote');if(hb)hb.remove();
  document.getElementById('view').innerHTML=render(window._d);
 }
});
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
 var bt=(d.boot||{});var btage=(Date.now()/1000)-(bt.ts||0);
 if(age>=180&&bt.pct!=null&&bt.pct<100&&btage<900){
  out+='<div class="card"><span class="warn">\\u23F3 starting up \\u2014 '+esc(bt.stage||'')+'</span>'
   +'<div class="mtrack"><div class="mfill" style="width:'+bt.pct+'%"></div></div>'
   +'<div class="hint">The first cycle after a restart walks the whole board \\u2014 orders, positions, discovery, terms, books. The page fills in when it completes, usually two to five minutes.</div>';
 } else
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
 else if(fz.active&&!fz.done){out+='<div class="ok" style="margin-top:6px">Flat \\u2014 '+(fz.kept_exits||0)+' exits resting and earning. Rebuilding under the family ceilings, best-paying markets first.</div>';}
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
   +'<div class="stat"><div class="lab">resting earns about</div><div class="val">'+usd(Math.min(s.est_day||0,(s.est_rate!=null?s.est_rate:1e9)))+'<span class="u">/day</span></div></div>'
   +'<div class="stat"><div class="lab">earned today so far</div><div class="val">'+usd(s.earned_today)+'</div></div>'
   +'<div class="stat"><div class="lab">orders</div><div class="val">'+(s.orders||[]).length+'<span class="u"> in '+(s.active||0)+' mkts</span></div></div>'
   +'</div>';
  if(s.est_rate!=null&&(s.est_day||0)>s.est_rate*1.2){out+='<div class="muted">orders claim '+usd(s.est_day)+'/day unaudited \u2014 the headline is the meter\u2019s audited rate.</div>';}
  var cap=s.capital_usd||0,sp=s.spent||0;
  out+='<div class="mtrack"><div class="mfill" style="width:'+Math.min(100,cap?100*sp/cap:0)+'%"></div></div>'
   +'<div class="muted">'+usd(sp)+' of the '+usd(cap)+' search ceiling is on the book.'+(s.proven_usd?' Proven markets ('+(s.proven_n||0)+') hold '+usd(s.proven_spent||0)+' more under their own '+usd(s.proven_usd)+' cap.':'')+'</div>';
  if(s.stock_day){out+='<div class="sub">Stock waiting to sell is earning '+usd(s.stock_day)+'/day while it waits.</div>';}
  var inv=s.inventory||{};var invn=Object.keys(inv).length;
  if(invn){out+='<div class="muted">'+invn+' position'+(invn>1?'s':'')+' held from fills \\u2014 see orders page.</div>';}
  var tg=s.triage||{};
  if(tg.total){
   var pctT=Math.min(100,100*(tg.done||0)/tg.total);
   out+='<div class="mtrack"><div class="mfill" style="width:'+pctT+'%;background:#5a7a9a"></div></div>';
   out+='<div class="muted">Triage: '+(tg.done||0)+' of '+tg.total+' markets scored this pass'
    +((tg.done||0)>=tg.total?' \\u2014 all scored; rescanning the oldest first.'
    :' \\u2014 about '+Math.ceil((tg.total-(tg.done||0))/(tg.per_cycle||1))+' min to finish.')+'</div>';
  }
  var tf=s.triage_feed||[];
  if(tf.length){
   if(!window._tseen)window._tseen={};
   var outs='',ins='';
   tf.slice().reverse().slice(0,12).forEach(function(t){
    var key=k+'|'+t.market+'|'+t.ts;
    var fresh=!window._tseen[key];window._tseen[key]=1;
    var info=[];
    if(t.in)info.push('worth '+usd(t.ev)+'/day');
    if(t.in&&t.plan)info.push(t.plan);
    if(t.spread!=null)info.push('spread '+t.spread+'c');
    if(t.pool!=null)info.push('pool '+usd(t.pool)+'/day');
    if(t.conf!=null&&t.conf>0)info.push('conf '+Math.round(t.conf*100)+'%');
    var chip='<div class="tchip '+(t.in?'win':'')+' '+(fresh?(t.in?'new-r':'new-l'):'')+'">'
     +'<div class="tn">'+nm(d,t.market)+'</div>'
     +'<div class="tm">'+esc(info.join(' \\u00b7 '))+(t.in?'':(info.length?' \\u00b7 ':'')+esc(t.why||''))+'</div></div>';
    if(t.in)ins+=chip;else outs+=chip;
   });
   out+='<div class="tri"><div class="tri-col"><div class="tri-h">passed on</div>'+outs+'</div>'
    +'<div class="tri-col"><div class="tri-h">worth budget</div>'+ins+'</div></div>';
  }
  out+='<div class="muted">'+(s.markets||0)+' markets known, '+(s.scanned||0)+' scored'
  if(s.unmeasured_min>1){out+='<div class="muted">'+s.unmeasured_min+' min of today went unmeasured (books too stale to score) \\u2014 counted as zero, never guessed.</div>';}
   +(s.resting_ok===false?' \\u2014 <span class="warn">game window: resting is paused</span>':'')+'.</div>';
  out+='</div>';
 });
 var ws=(d.ws||{});
 if(ws.state){out+='<div class="muted">book stream: '+esc(ws.state)+(ws.subscribed?' ('+ws.subscribed+' markets live)':'')+'</div>';}
 var sv2=(d.silver||{});
 if(sv2.senate_races){out+='<div class="muted">Silver model: '+sv2.senate_races+' senate + '+(sv2.gov_races||0)+' governor races, tables checked '+(sv2.tables_age_min==null?'?':sv2.tables_age_min)+' min ago'+(sv2.tables_changed_h==null?'':' \u00b7 senate numbers last MOVED '+sv2.tables_changed_h+'h ago')+(sv2.gov_changed_h==null?'':' \u00b7 governor '+sv2.gov_changed_h+'h ago')+(sv2.note?' \u00b7 '+esc(sv2.note):'')+(sv2.official_age_h!=null?' \\u00b7 seat simulations from '+sv2.official_age_h+'h ago ('+esc(sv2.official_source||'')+')':'')+'</div>';}
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
function sfair(m){
 var v=prompt('Fair value in CENTS for\\n'+m+'\\n\\nYour number beats the model everywhere fair is used.\\nLeave empty to go back to the model.');
 if(v===null)return;
 var f=(v==='')?'':(parseFloat(v)/100);
 if(v!==''&&!(f>0&&f<1)){alert('enter cents, 0.1 to 99.9');return;}
 post({op:'set_fair',market:m,fair:f},function(j){alert(j.note||'done');});
}
function fold(title,sub,body,open){
 return '<details'+(open?' open':'')+'><summary><b>'+title+'</b> <span class="muted">'+sub+'</span></summary>'+body+'</details>';
}
function orow(d,o){
 var e=(o.live_est!=null?o.live_est:o.est_day);
 var bid='bk_'+esc(o.id);
 return '<div style="margin:9px 0 0;border-top:1px solid #2c3527;padding-top:7px">'
  +'<div class="name" style="cursor:pointer" onclick="showbook(\\''+esc(o.market)+'\\',\\''+bid+'\\')">'+nm(d,o.market)+' <span class="muted">\u25be book</span></div>'
  +'<div id="'+bid+'"></div>'
  +'<div class="muted"><code>'+esc(o.market)+'</code></div>'
  +'<div class="muted">fair: '+((d.owner_fairs&&d.owner_fairs[o.market]!=null)?('<b>'+pc(d.owner_fairs[o.market])+' (yours)</b>'):'model')
  +' <a style="cursor:pointer;text-decoration:underline" onclick="sfair(\\''+esc(o.market)+'\\')">set</a></div>'
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
 out+='<div class="card"><details><summary><b>Place an order by hand</b> <span class="muted">\\u2014 bypasses the switches, keeps every safety rail; the automation never touches it</span></summary>'
  +'<div style="margin:8px 0"><input id="pm" placeholder="market slug" style="width:95%"></div>'
  +'<div style="margin:8px 0"><select id="ps" style="font-size:16px;padding:8px"><option value="BUY">bid (buy)</option><option value="SELL">ask (sell)</option></select>'
  +' <input id="pp" placeholder="price c" style="width:20%"> <input id="pq" placeholder="shares" style="width:20%">'
  +' <button onclick="pl()">Place</button></div><div id="plout"></div></details></div>';
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
  var lg=(d['fam_log_'+k]||[]).filter(function(r){
   return ['place','pull','silent_cancel','reprice','exit','trim','probe','probe_done','zombie_cancelled','window_pull'].indexOf(r.event)>=0;
  }).slice(-14).reverse();
  if(lg.length){
   var lb='';
   lg.forEach(function(r){
    var what={place:'placed',pull:'pulled',silent_cancel:'the exchange dropped it on arrival',
     reprice:'moved',exit:'left the market',trim:'trimmed for the ceiling',
     probe:'scout sent',probe_done:'scout finished its watch',
     zombie_cancelled:'stuck order finally cancelled',window_pull:'pulled for the game window'}[r.event]||r.event;
    lb+='<div class="vrd">'+when(r.ts||0)+' \\u2014 '+what+' \\u2014 '+nm(d,r.market||'')
     +(r.why?' <span class="muted">('+esc(r.why)+')</span>':'')
     +(r.to!=null?' <span class="muted">to '+pc(r.to)+'</span>':'')+'</div>';
   });
   out+=fold('Recent changes','\\u2014 what appeared and what left, and why',lb,false);
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
function pl(){
 var m=document.getElementById('pm').value.trim();
 var s=document.getElementById('ps').value;
 var p=parseFloat(document.getElementById('pp').value)/100;
 var q=parseFloat(document.getElementById('pq').value);
 if(!m||!(p>0&&p<1)||!(q>0)){alert('need a slug, a price in cents, and shares');return;}
 if(!confirm('Place '+(s==='BUY'?'bid':'ask')+' '+q+' @ '+(p*100).toFixed(1)+'c on '+m+'?'))return;
 document.getElementById('plout').innerHTML='<div class="muted">placing\\u2026</div>';
 post({op:'place',market:m,side:s,price:p,qty:q},function(j){
  document.getElementById('plout').innerHTML='<div class="'+(j.ok?'ok':'bad')+'">'+esc(j.note||'')+'</div>';
 });
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
   var pid='pb_'+esc(b.market).replace(/[^a-z0-9]/g,'');
   out+='<div style="margin:8px 0 0;border-top:1px solid #2c3527;padding-top:6px">'
    +'<div class="name" style="cursor:pointer" onclick="showbook(\\''+esc(b.market)+'\\',\\''+pid+'\\')">'+esc(b.name||b.market)+' <span class="muted">\u25be book</span></div>'
    +'<div id="'+pid+'"></div>'
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
  if(sm){out+='<div class="muted">'+usd(sm.spent)+' of '+usd(sm.capital_usd)+' at risk'+(sm.holdings_usd?(sm.holdings_counted?' (incl. holdings worth '+usd(sm.holdings_usd)+' at liquidation)':' \u00b7 plus holdings worth '+usd(sm.holdings_usd)+' at liquidation, not counted'):'')+'; resting earns ~'+usd(Math.min(sm.est_day||0,(sm.est_rate!=null?sm.est_rate:1e9)))+'/day.</div>';}
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

WATCH_JS = """
function wFmtC(v){return Math.round(v*100)+'c';}
function wCurve(rows,X,Y,color){
 if(!rows.length)return '';
 var pts=rows.map(function(r){return [X(r.px),Y(r.ev)];});
 var d='M'+pts[0][0].toFixed(1)+' '+pts[0][1].toFixed(1);
 for(var i=1;i<pts.length;i++){d+=' L'+pts[i][0].toFixed(1)+' '+pts[i][1].toFixed(1);}
 var s='<path d="'+d+'" fill="none" stroke="'+color+'" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" opacity="0.9"/>';
 rows.forEach(function(r){
  s+='<circle cx="'+X(r.px).toFixed(1)+'" cy="'+Y(r.ev).toFixed(1)+'" r="'+(r.picked?5:2.2)+'" fill="'+color+'"'+(r.picked?' stroke="#fff" stroke-width="1.5"':' opacity="0.75"')+'/>';
 });
 return s;
}
function wSnapT(tri,oursAt){
 var pickAt={};(tri.picks||[]).forEach(function(r){pickAt[r.s+(r.px*100).toFixed(1)]=r;});
 function wRows(arr,side,desc){
  var out=arr.filter(function(x){
   var k=side+(x[0]*100).toFixed(1);
   return x[1]>=0.5||pickAt[k]||oursAt[k];   // dust hidden unless marked
  });
  (tri.picks||[]).forEach(function(r){
   if(r.s!==side)return;
   if(out.some(function(x){return Math.abs(x[0]-r.px)<0.0001;}))return;
   out.push([r.px,r.q]);                     // decision rows in price order
  });
  out.sort(function(a,b){return desc?b[0]-a[0]:a[0]-b[0];});
  return out;
 }
 var sb=wRows(tri.book.b||[],'BUY',true),sa=wRows(tri.book.a||[],'SELL',false);
 var age=Math.max(0,Math.round((Date.now()/1000-tri.ts)/60));
 var bt='<div class="muted" style="font-size:12px">the book as the engine saw it \u2014 '+(age<1?'moments':age+' min')+' ago \u00b7 \u25c9 marks the decision</div>';
 bt+='<table><tr><th class="r">bid size</th><th class="r">bid</th><th>ask</th><th>ask size</th></tr>';
 var nrows=Math.min(Math.max(sb.length,sa.length),7);
 for(var i=0;i<nrows;i++){
  var bd=sb[i],ak=sa[i];
  var bm=bd?((pickAt['BUY'+(bd[0]*100).toFixed(1)]?' \u25c9':'')+(oursAt['BUY'+(bd[0]*100).toFixed(1)]?' \u25CF':'')):'';
  var am=ak?((pickAt['SELL'+(ak[0]*100).toFixed(1)]?' \u25c9':'')+(oursAt['SELL'+(ak[0]*100).toFixed(1)]?' \u25CF':'')):'';
  bt+='<tr><td class="r">'+(bd?fmtsz(bd[1]):'')+'</td><td class="r">'+(bd?pc(bd[0])+bm:'')+'</td>'
    +'<td>'+(ak?pc(ak[0])+am:'')+'</td><td>'+(ak?fmtsz(ak[1]):'')+'</td></tr>';
 }
 return bt+'</table>';
}
function wCard(name,slug,b,tri){
 var lad=(b&&b.ladder)||{};var sides=lad.sides||{};
 var bids=(sides.BUY||{}).rows||[],asks=(sides.SELL||{}).rows||[];
 var all=bids.concat(asks);
 var g=b&&b.fair!=null?'model '+(b.fair*100).toFixed(1)+'c':(b&&b.band&&b.band.med!=null?'evidence '+b.band.lo.toFixed(0)+'\u2013'+b.band.hi.toFixed(0)+'c \u00b7 confidence '+Math.round((b.conf||0)*100)+'%':'no grounding');
 var head='<div style="font-size:22px;font-weight:700;line-height:1.2;margin:2px 0">'+esc(name)+'</div>'
  +'<div class="muted">'+esc(g)+(lad.pool_day!=null?' \u00b7 pool $'+lad.pool_day+'/day per side':'')+(lad.note?' \u00b7 '+esc(lad.note):'')+'</div>';
 if(tri&&tri.why)head+='<div class="muted" style="margin:2px 0">'+(tri['in']?'\u2705 worth budget':'\u25cb passed on')+' \u2014 '+esc(tri.why)+'</div>';
 if(!all.length)return head+((tri&&tri.book)?wSnapT(tri,{}):'')+'<div class="muted" style="padding:14px 0">no priced ladder \u2014 '+esc(lad.note||'nothing clears here')+'</div>';
 var W=340,H=210,PL=36,PB=26,PT=14,PR=10;
 var pxs=all.map(function(r){return r.px;});
 var x0=Math.max(Math.min.apply(null,pxs)-0.02,0),x1=Math.min(Math.max.apply(null,pxs)+0.02,1);
 var evs=all.map(function(r){return r.ev;});
 var y1=Math.max(Math.max.apply(null,evs)*1.12,(lad.bar||0.5)*1.4),y0=Math.min(0,Math.min.apply(null,evs));
 function X(p){return PL+(W-PL-PR)*(p-x0)/(x1-x0);}
 function Y(v){return PT+(H-PT-PB)*(1-(v-y0)/(y1-y0));}
 var s='<svg viewBox="0 0 '+W+' '+H+'" style="width:100%;height:auto" role="img" aria-label="EV curve">';
 if(b&&b.band&&b.band.lo!=null&&b.fair==null){
  var bl=Math.max(b.band.lo/100,x0),bh=Math.min(b.band.hi/100,x1);
  if(bh>bl)s+='<rect x="'+X(bl).toFixed(1)+'" y="'+PT+'" width="'+(X(bh)-X(bl)).toFixed(1)+'" height="'+(H-PT-PB)+'" fill="rgba(158,196,154,0.07)"/>';
 }
 [0.25,0.5,0.75,1].forEach(function(f){
  var v=y0+(y1-y0)*f,y=Y(v);
  s+='<line x1="'+PL+'" y1="'+y+'" x2="'+(W-PR)+'" y2="'+y+'" stroke="rgba(255,255,255,0.06)"/>';
  s+='<text x="'+(PL-4)+'" y="'+(y+3)+'" text-anchor="end" font-size="8" fill="rgba(255,255,255,0.4)">$'+v.toFixed(1)+'</text>';
 });
 var yb=Y(lad.bar||0.5);
 s+='<line x1="'+PL+'" y1="'+yb+'" x2="'+(W-PR)+'" y2="'+yb+'" stroke="rgba(255,208,107,0.5)" stroke-dasharray="4 3"/>';
 s+='<text x="'+(W-PR)+'" y="'+(yb-3)+'" text-anchor="end" font-size="8" fill="rgba(255,208,107,0.8)">the '+((lad.bar||0.5)*100).toFixed(0)+'c bar</text>';
 if(Y(0)<H-PB)s+='<line x1="'+PL+'" y1="'+Y(0)+'" x2="'+(W-PR)+'" y2="'+Y(0)+'" stroke="rgba(255,255,255,0.15)"/>';
 if(b&&b.fair!=null&&b.fair>=x0&&b.fair<=x1){
  s+='<line x1="'+X(b.fair).toFixed(1)+'" y1="'+PT+'" x2="'+X(b.fair).toFixed(1)+'" y2="'+(H-PB)+'" stroke="rgba(255,255,255,0.3)" stroke-dasharray="2 3"/>';
  s+='<text x="'+X(b.fair).toFixed(1)+'" y="'+(PT-3)+'" text-anchor="middle" font-size="8" fill="rgba(255,255,255,0.6)">model '+wFmtC(b.fair)+'</text>';
 }
 [x0,(x0+x1)/2,x1].forEach(function(p,i){
  var anch=i===0?'start':(i===2?'end':'middle');
  s+='<text x="'+X(p).toFixed(1)+'" y="'+(H-8)+'" text-anchor="'+anch+'" font-size="8" fill="rgba(255,255,255,0.4)">'+wFmtC(p)+'</text>';
 });
 s+=wCurve(bids,X,Y,'#9ec49a');
 s+=wCurve(asks,X,Y,'#d9b36a');
 s+='</svg>';
 var legend='<div class="muted" style="font-size:12px"><span style="color:#9ec49a">\u25cf</span> bids &nbsp;<span style="color:#d9b36a">\u25cf</span> asks &nbsp;\u00b7 big dot = the pick &nbsp;\u00b7 EV/day at each resting price</div>';
 var notes='';
 ['BUY','SELL'].forEach(function(sd){
  var e=(lad.sides||{})[sd]||{};
  if(e.note)notes+='<div class="muted" style="font-size:12px">'+(sd==='BUY'?'bids: ':'asks: ')+esc(e.note)+'</div>';
 });
 legend+=notes;
 var pkRows=all.filter(function(r){return r.picked;});
 var pk;
 if(tri&&(tri.picks||[]).length){
  pk='<div style="font-size:16px;margin:6px 0"><b>Decision: '+tri.picks.map(function(r){
   return (r.s==='BUY'?'bid':'ask')+' '+r.q+' @ '+wFmtC(r.px)+' \u2192 $'+r.ev.toFixed(2)+'/day';
  }).join(' \u00b7 ')+'</b><div class="muted" style="font-size:12px;font-weight:400">'+esc(tri.why||'')+'</div></div>';
 }else if(pkRows.length){
  pk='<div style="font-size:16px;margin:6px 0"><b>Decision: '+pkRows.map(function(r){
   return (bids.indexOf(r)>=0?'bid':'ask')+' '+r.qty+' @ '+wFmtC(r.px)+' \u2192 $'+r.ev.toFixed(2)+'/day, '+Math.round(r.p_fill*100)+'% fill odds';
  }).join(' \u00b7 ')+'</b>'+pkRows.map(function(r){return r.why?'<div class="muted" style="font-size:12px;font-weight:400">'+esc(r.why)+'</div>':'';}).join('')+'</div>';
 }else{
  pk='<div class="muted" style="margin:6px 0"><b>Decision:</b> nothing here clears the bar</div>';
 }
 var evs='';
 [['bids',bids],['asks',asks]].forEach(function(pr){
  var rs=pr[1].slice().sort(function(x,y){return y.ev-x.ev;}).slice(0,3);
  if(rs.length)evs+='<div class="muted" style="font-size:12px">best '+pr[0]+' by EV/day: '+rs.map(function(r2){return pc(r2.px)+' \u2192 $'+r2.ev.toFixed(2);}).join(' \u00b7 ')+'</div>';
 });
 var oursAt={};(b.ours||[]).forEach(function(o){oursAt[o.side+(o.price*100).toFixed(1)]=o;});
 var bt;
 if(tri&&tri.book&&(tri.book.b||tri.book.a)){
  bt=wSnapT(tri,oursAt);
 }else{
  bt='<table><tr><th class="r">bid size</th><th class="r">bid</th><th>ask</th><th>ask size</th></tr>';
  var nrows=Math.min(Math.max((b.bids||[]).length,(b.asks||[]).length),6);
  for(var i=0;i<nrows;i++){
   var bd=(b.bids||[])[i],ak=(b.asks||[])[i];
   var bm=bd&&oursAt['BUY'+(bd[0]*100).toFixed(1)]?' \u25CF':'';
   var am=ak&&oursAt['SELL'+(ak[0]*100).toFixed(1)]?' \u25CF':'';
   bt+='<tr><td class="r">'+(bd?fmtsz(bd[1]):'')+'</td><td class="r">'+(bd?pc(bd[0])+bm:'')+'</td>'
     +'<td>'+(ak?pc(ak[0])+am:'')+'</td><td>'+(ak?fmtsz(ak[1]):'')+'</td></tr>';
  }
  bt+='</table>';
 }
 var mine='';
 if((b.ours||[]).length){
  mine='<div style="margin:4px 0"><b>Where I am:</b> '+b.ours.map(function(o){
   var tag=o.purpose==='sell'?'exit':o.purpose;
   var earn=(o.est&&o.est>=0.005)?' \u2014 earning ~$'+o.est.toFixed(2)+'/day':(o.verdict?' \u2014 '+esc(o.verdict):' \u2014 earning $0');
   return (o.side==='BUY'?'bid':'ask')+' '+o.qty+' @ '+wFmtC(o.price)+' ['+tag+']'+earn;
  }).join(' \u00b7 ')+'</div>';
 }else{mine='<div class="muted" style="margin:4px 0">no orders resting here yet</div>';}
 if(b.position&&b.position.qty){
  var pq=b.position.qty,pc2=b.position.cost;
  mine+='<div><b>Position:</b> '+pq+' shares'+(pq>0?' at '+((pc2/pq)*100).toFixed(1)+'c average':' (short)')+'</div>';
 }
 return head+s+legend+pk+evs+bt+'<div class="hint">\u25CF marks our order</div>'+mine;
}
function wShow(t){
 fetch('/book.json?m='+encodeURIComponent(t.market),{headers:hdrs(),cache:'no-store'})
  .then(function(r){return r.json();}).then(function(b){
   var el=document.getElementById('spot');
   if(!el)return;
   el.style.opacity=0;
   setTimeout(function(){
    window._watchCurHTML=wCard(nm(window._watchD,t.market),t.market,b,t);
    el.innerHTML=window._watchCurHTML;
    el.style.opacity=1;
    wCount();
   },200);
  }).catch(function(){});
}
function wCount(){
 var el=document.getElementById('wn');
 if(el)el.innerHTML=(window._watchBuf||[]).length
  ? 'next market \u25b8 ('+window._watchBuf.length+' saved)'
  : 'caught up \u2014 the sweep is scoring more';
}
function wNext(){
 var q=window._watchBuf||[];
 if(!q.length){wCount();return;}
 var t=q.shift();
 window._watchSeen=window._watchSeen||{};
 window._watchSeen[t.market]=t.ts;
 wShow(t);
}
function render(d){
 window._watchD=d;
 window._watchBuf=window._watchBuf||[];
 window._watchSeen=window._watchSeen||{};
 var buf=window._watchBuf;
 ['politics'].forEach(function(k){
  var s=(d.summaries||{})[k]||{};
  (s.triage_feed||[]).forEach(function(t){
   if((window._watchSeen[t.market]||0)>=t.ts)return;
   for(var i=0;i<buf.length;i++){
    if(buf[i].market===t.market){if(t.ts>buf[i].ts)buf[i]=t;return;}
   }
   if(buf.length<25)buf.push(t);
  });
 });
 buf.sort(function(a,b){return a.ts-b.ts;});
 if(!window._watchCurHTML&&buf.length)setTimeout(wNext,300);
 return '<div class="card"><div class="muted">One politics market per tap \u2014 what the engine saw as it considered. Up to 25 verdicts wait; the queue refills as the sweep scores.</div>'
  +'<div style="margin:8px 0"><button onclick="wNext()" id="wn" style="font-size:16px;padding:10px 16px;width:100%">next market \u25b8'+(buf.length?' ('+buf.length+' saved)':'')+'</button></div>'
  +'<div id="spot" style="transition:opacity 0.2s ease;min-height:280px">'+(window._watchCurHTML||'')+'</div></div>';
}
"""


GRAPH_JS = """
function fmtT(ts){var d=new Date(ts*1000);return ('0'+d.getHours()).slice(-2)+':'+('0'+d.getMinutes()).slice(-2);}
function drawGraph(name,dots){
 if(!dots||dots.length<2)return '<div class="card"><b>'+esc(name)+'</b><div class="muted">not enough samples yet \u2014 one dot arrives every 20 seconds</div></div>';
 var W=340,H=150,PL=34,PB=18,PT=8,PR=6;
 var t0=dots[0][0],t1=dots[dots.length-1][0];var span=Math.max(t1-t0,60);
 var ymax=0;dots.forEach(function(d){if(d[1]>ymax)ymax=d[1];});
 ymax=Math.max(ymax*1.08,1);
 function X(t){return PL+(W-PL-PR)*(t-t0)/span;}
 function Y(v){return PT+(H-PT-PB)*(1-v/ymax);}
 var s='<svg viewBox="0 0 '+W+' '+H+'" style="width:100%;height:auto" role="img" aria-label="'+esc(name)+' earning rate samples">';
 [0,0.5,1].forEach(function(f){
  var v=ymax*f,y=Y(v);
  s+='<line x1="'+PL+'" y1="'+y+'" x2="'+(W-PR)+'" y2="'+y+'" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>';
  s+='<text x="'+(PL-4)+'" y="'+(y+3)+'" text-anchor="end" font-size="8" fill="rgba(255,255,255,0.45)">$'+v.toFixed(0)+'</text>';
 });
 [t0,(t0+t1)/2,t1].forEach(function(t,i){
  var x=X(t);var anch=i===0?'start':(i===2?'end':'middle');
  s+='<text x="'+x+'" y="'+(H-4)+'" text-anchor="'+anch+'" font-size="8" fill="rgba(255,255,255,0.45)">'+fmtT(t)+'</text>';
 });
 dots.forEach(function(d){
  s+='<circle cx="'+X(d[0]).toFixed(1)+'" cy="'+Y(d[1]).toFixed(1)+'" r="1.6" fill="#9ec49a" fill-opacity="0.85"/>';
 });
 s+='</svg>';
 var last=dots[dots.length-1];
 return '<div class="card"><b>'+esc(name)+'</b> <span class="muted">\u2014 $/day, one dot per 20-second sample \u00b7 now $'+last[1].toFixed(2)+'/day, '+last[2]+' markets in view</span>'+s
  +'<div class="hint">Gaps are minutes the meter could not see a fresh book. The sampling clock is independent \u2014 nothing that places, moves, or cancels orders can touch it.</div></div>';
}
function mWin(sec){
 window._meterWin=sec;
 if(window._meterD){var el=document.getElementById('view');if(el)el.innerHTML=render(window._meterD);}
}
function render(d){
 window._meterD=d;
 var win=window._meterWin||0;
 var btn=function(sec,label){
  var on=(window._meterWin||0)===sec;
  return '<button onclick="mWin('+sec+')" style="font-size:14px;padding:6px 14px;margin-right:8px'+(on?';font-weight:bold;text-decoration:underline':'')+'">'+label+'</button>';
 };
 var out='<div style="margin:2px 0 8px 0">'+btn(900,'last 15 min')+btn(0,'all day')+'</div>';
 var now=Date.now()/1000;
 [['Politics','est_politics'],['College football','est_cfb'],['NFL','est_nfl'],['NBA','est_nba']].forEach(function(p){
  var e=d[p[1]]||{};
  var dots=e.dots||[];
  if(win)dots=dots.filter(function(x){return x[0]>=now-win;});
  if(dots.length||p[1]!=='est_nfl')out+=drawGraph(p[0],dots);
 });
 return out||'<div class="card muted">no samplers armed</div>';
}
"""

GRADES_JS = """
function render(d){
 var rows=(d.grades||[]);
 var out='<div class="card"><b>Estimate vs. what the exchange paid</b>';
 out+='<div style="margin:6px 0"><button onclick="ckrw()">Check for new payouts now</button></div>'+rwcard();
 out+='<div class="hint">The estimate is 3.0\\u2019s own sampler \\u2014 measured on an independent clock, accruing only while books are fresh. Actuals are the account\\u2019s posted rewards (during the transition the older versions\\u2019 books pay into the same number). No fudge factors: a gap means an input was wrong, and the unmeasured minutes say how much of the day went unscored.</div>';
 if(!rows.length){out+='<div class="muted">Nothing to grade yet \\u2014 the first full day under 3.0 lands tomorrow.</div>';}
 var pend=0;
 rows.forEach(function(r){if(r.actual==null&&r.est!=null){pend+=r.est;}});
 var pt=d.paid_total;
 if(!pt){var tot=0,nd=0;rows.forEach(function(r){if(r.actual!=null){tot+=r.actual;nd++;}});pt=nd?{usd:tot,days:nd,since:''}:null;}
 if(pt){out+='<div style="margin:8px 0 2px;font-size:1.15em"><b>'+usd(pt.usd)+' paid in total</b> <span class="muted">over '+pt.days+' posted days'+(pt.since?' since '+esc(pt.since):'')+(pend>0.005?' \\u00b7 '+usd(pend)+' more estimated, not posted yet':'')+'</span></div>';}
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

function rwcard(){
 if(window._rwbusy)return '<div class="muted">checking the exchange\\u2026</div>';
 var j=window._rw||(window._d&&window._d.rewards_last);
 if(!j)return '<div class="muted">The watcher checks every 5 minutes and pushes your phone when rewards post. The button forces a check now.</div>';
 if(!j.ok)return '<div class="bad">'+esc(j.note||'failed')+'</div>';
 var h='<div class="card">';
 if(j.note){h+='<div class="sub">'+esc(j.note)+'</div>';}
 else{h+='<b>'+(j.new_count||0)+' new or changed row'+(j.new_count!==1?'s':'')+'</b>';}
 var dk=Object.keys(j.days||{}).sort().reverse().slice(0,4);
 if(dk.length){
  var dl=dk.map(function(d){return d.slice(5)+' '+usd(j.days[d]);}).join(' \\u00b7 ');
  h+='<div class="muted">Posted day totals: '+dl+'</div>';
 }
 (j.new_rows||[]).slice().reverse().forEach(function(r){
  h+='<div class="sub">'+esc(r.day)+' \\u00b7 '+usd(r.usd)+' \\u00b7 '+esc(r.name)+' <span class="muted">'+esc(r.status)+'</span></div>';
 });
 if(!(j.new_rows||[]).length)h+='<div class="muted">Nothing new since the last check.</div>';
 return h+'</div>';
}
function ckrw(){
 window._rwbusy=true;
 if(window._d)document.getElementById('view').innerHTML=render(window._d);
 post({op:'refresh_rewards'},function(j){
  window._rwbusy=false;
  window._rw=j;
 });
}
"""

SILVER_JS = """
function render(d){
 var sv=d.silver||{};var out='';
 out+='<div class="card"><b>The Silver model, as this system sees it</b>';
 out+='<div class="sub">'+(sv.senate_races||0)+' senate and '+(sv.gov_races||0)+' governor races. Tables checked '+(sv.tables_age_min==null?'?':sv.tables_age_min)+' min ago.'+(sv.official_age_h!=null?' Seat simulations from '+sv.official_age_h+' hours ago ('+esc(sv.official_source||'')+').':'')+'</div>';
 out+='<div class="sub">Model coverage in your scope: <b>'+(sv.priced||0)+'</b> markets priced, '+(sv.unpriced||0)+' without a model number (margins, primaries, the 2028 slate) \\u2014 those run on evidence alone and every card says so.</div>';
 out+='<div class="hint">The feed carries the model\\u2019s odds, not the polls behind them. So this page shows every MOVE in the odds and when this system saw it. The tables update when Silver posts new polling \\u2014 about daily in season, checked every 6 hours. The simulations update only when he reruns the model; past 5 days old, the system widens its bands instead of trusting them alone.</div>';
 out+='</div>';
 var log=(d.silver_log||[]).slice().reverse();
 out+='<div class="card"><b>Model moves seen</b>';
 if(!log.length)out+='<div class="muted">None yet \\u2014 the log starts now and fills as the odds move.</div>';
 var day='';
 log.slice(0,60).forEach(function(r){
  var dt=new Date((r.ts||0)*1000);var dl=dt.toLocaleDateString([], {month:'short',day:'numeric'});
  if(dl!==day){day=dl;out+='<div class="tri-h" style="margin-top:8px">'+esc(dl)+'</div>';}
  var dd=(r.new-r.old);
  out+='<div class="sub">'+esc(r.name)+' ('+esc(r.chamber)+'): R '+r.old+'% \\u2192 '+r.new+'% <span class="'+(Math.abs(dd)>=2?'warn':'muted')+'">('+(dd>0?'+':'')+dd.toFixed(1)+')</span> <span class="muted">'+when(r.ts)+'</span></div>';
 });
 out+='</div>';
 return out;
}
"""

FILLS_JS = """
var _MO=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
function fWhen(ts){var d=new Date(ts*1000);return _MO[d.getMonth()]+' '+d.getDate()+', '+('0'+d.getHours()).slice(-2)+':'+('0'+d.getMinutes()).slice(-2);}
function fUsd(v){return (v<-0.005?'\\u2212$':'+$')+Math.abs(v).toFixed(2);}
function fRest(h){if(h==null)return '';return h<1?Math.round(h*60)+' min':(h<48?h.toFixed(1)+' h':(h/24).toFixed(1)+' days');}
function fParts(f){
 var earned=(f.est_day&&f.rested_h!=null)?f.est_day*f.rested_h/24:0;
 var oq=f.open_qty!=null?f.open_qty:f.qty;
 var flat=f.pos_now!=null&&Math.abs(f.pos_now)<0.005;
 var open=!f.stray_close&&oq>0.005&&!flat;
 var reconciled=!f.stray_close&&oq>0.005&&flat;
 var mk=0;
 if(open){
  if(f.side==='BUY'&&f.now_bid!=null)mk=(f.now_bid-f.px)*oq;
  if(f.side==='SELL'&&f.now_ask!=null)mk=(f.px-f.now_ask)*oq;
 }
 var net=(f.realized||0)+earned+(open?mk+(f.exit_earned||0):0);
 return {open:open,oq:oq,mark:mk,earned:earned,net:net,
         reconciled:reconciled,
         rate:open?(f.exit_rate||0):0};
}
function fTint(net){
 if(net>=1)return 'rgba(96,170,96,0.32)';
 if(net>=0.05)return 'rgba(96,170,96,0.16)';
 if(net<=-1)return 'rgba(200,84,84,0.30)';
 if(net<=-0.05)return 'rgba(200,84,84,0.15)';
 return 'rgba(255,255,255,0.04)';
}
function fFlip(el){
 el.style.transition='transform 0.14s ease';
 el.style.transform='rotateY(90deg)';
 setTimeout(function(){
  var a=el.querySelector('.ffront'),b=el.querySelector('.fback');
  if(a&&b){var sh=a.style.display==='none';a.style.display=sh?'':'none';b.style.display=sh?'none':'';}
  el.style.transform='rotateY(0deg)';
 },140);
}
function fFront(f,p){
 var st=f.stray_close?'CLOSED OUT':(p.open?'OPEN \\u00b7 so far':'CLOSED');
 var tick=p.open&&p.rate>0.005?' <span class="muted" style="font-size:12px">+'+p.rate.toFixed(2)+'/day ticking</span>':'';
 return '<div style="font-size:17px;line-height:1.25"><b>'+esc(f.name||f.market)+'</b></div>'
  +'<div style="font-size:21px;margin:3px 0"><b>'+(f.side==='BUY'?'bought':'sold')+' '+f.qty+' @ '+pc(f.px)+'</b></div>'
  +'<div style="font-size:26px;margin:2px 0"><b class="fnet" data-base="'+p.net.toFixed(4)+'" data-rate="'+p.rate.toFixed(4)+'">'+fUsd(p.net)+'</b> <span class="muted" style="font-size:13px">'+st+'</span>'+tick+'</div>'
  +'<div class="muted" style="font-size:12px">'+esc(f.family||'')+' \\u00b7 '+fWhen(f.ts)+' \\u00b7 tap for the story</div>';
}
function fBack(f,p){
 var out='<div><b>'+esc(f.name||f.market)+'</b> <span class="muted" style="font-size:12px">'+esc(f.family||'')+'</span></div>';
 out+='<div style="font-size:15px;margin:2px 0"><b>'+(f.side==='BUY'?'bought':'sold')+' '+f.qty+' @ '+pc(f.px)+'</b> \\u00b7 '+fWhen(f.ts)+(f.stray_close?' \\u00b7 an exit':'')+'</div>';
 var plan='The order: '+esc(f.why||'(no note)');
 if(f.est_day)plan+=' \\u2014 estimated ~$'+f.est_day.toFixed(2)+'/day while resting';
 if(f.rested_h!=null)plan+=' \\u00b7 rested '+fRest(f.rested_h)+' before filling';
 out+='<div class="muted" style="margin:2px 0">'+plan+'</div>';
 var v='';
 if(f.fair!=null)v='Model said '+pc(f.fair);
 else if(f.band)v='No model \\u2014 evidence put value between '+f.band[0].toFixed(0)+'c and '+f.band[1].toFixed(0)+'c';
 else v='No independent sense of value at the time';
 if(f.touch_bid!=null||f.touch_ask!=null)v+=' \\u00b7 book was '+(f.touch_bid!=null?pc(f.touch_bid):'\\u2014')+'/'+(f.touch_ask!=null?pc(f.touch_ask):'\\u2014');
 out+='<div style="margin:2px 0">'+v+'</div>';
 var lot=(f.conc!=null)?-f.conc*f.qty:null;
 var cl;
 if(f.conc==null)cl='Value unknown then \\u2014 no concession math';
 else if(f.conc>0.0005)cl='Paid '+(f.conc*100).toFixed(1)+'c past value \\u2192 '+fUsd(lot)+' on the lot';
 else if(f.conc<-0.0005)cl='Filled '+(-f.conc*100).toFixed(1)+'c inside value \\u2192 '+fUsd(lot)+' on the lot';
 else cl='Filled right at value';
 if(p.earned)cl+=' \\u00b7 earned ~$'+p.earned.toFixed(2)+' in rewards while it rested';
 out+='<div style="margin:2px 0">'+cl+'</div>';
 if((f.closes||[]).length){
  out+='<div style="margin:2px 0">'+f.closes.map(function(c){
   return '\\u21b3 '+(f.side==='BUY'?'sold':'bought back')+' '+c.qty+' @ '+pc(c.px)+' \\u00b7 '+fWhen(c.ts)+' \\u2192 '+fUsd(c.pl);
  }).join('<br>')+'</div>';
 }
 if(f.stray_close){
  out+='<div class="muted" style="margin:2px 0">This closed stock bought before the journal began \\u2014 no matching purchase on record, so no round-trip math.</div>';
 }else if(p.reconciled){
  out+='<div style="margin:2px 0"><b>Closed by reconciliation</b> \\u2014 the exchange shows this market flat, so the remaining '+p.oq+' closed outside the journal (a correction or an untracked fill; no price recorded). Realized covers only the recorded closes: '+fUsd(f.realized||0)+'.</div>';
 }else if(!p.open){
  out+='<div style="margin:2px 0"><b>Round trip closed \\u2014 realized '+fUsd(f.realized||0)+(p.earned?' \\u00b7 plus ~$'+p.earned.toFixed(2)+' rewards':'')+'</b></div>';
 }else{
  var nw='Now: book '+(f.now_bid!=null?pc(f.now_bid):'\\u2014')+'/'+(f.now_ask!=null?pc(f.now_ask):'\\u2014')+' \\u00b7 position '+(f.pos_now!=null?f.pos_now:'?');
  if(p.oq<f.qty)nw+='<br>Still open: '+p.oq+' of '+f.qty+' \\u00b7 realized so far '+fUsd(f.realized||0);
  nw+='<br>The open part marks '+fUsd(p.mark)+' today';
  if(f.exit_resting)nw+='<br>Exit resting \\u2014 earning ~$'+(f.exit_rate||0).toFixed(2)+'/day, ~$'+(f.exit_earned||0).toFixed(2)+' since it rested';
  else nw+='<br>No exit resting yet \\u2014 the open part earns $0.00/day until one rests';
  out+='<div style="margin:2px 0">'+nw+'</div>';
 }
 out+='<div class="muted" style="font-size:12px;margin-top:4px">tap to flip back</div>';
 return out;
}
function fCard(f){
 var p=fParts(f);
 return '<div class="card" onclick="fFlip(this)" style="cursor:pointer;background:'+fTint(p.net)+'">'
  +'<div class="ffront">'+fFront(f,p)+'</div>'
  +'<div class="fback" style="display:none">'+fBack(f,p)+'</div></div>';
}
function fTick(){
 if(!document.querySelectorAll)return;
 var dt=(Date.now()/1000)-(window._fillT0||0);
 var els=document.querySelectorAll('.fnet');
 for(var i=0;i<els.length;i++){
  var r=parseFloat(els[i].getAttribute('data-rate')||'0');
  if(r>0.005){
   var b=parseFloat(els[i].getAttribute('data-base')||'0');
   els[i].textContent=fUsd(b+r*dt/86400);
  }
 }
}
function fDraw(){
 var el=document.getElementById('fl');
 var j=window._fillsJ;
 if(!el||!j)return;
 if(!j.ok||!(j.fills||[]).length){el.innerHTML='<div class="card muted">No purchases on record yet \\u2014 the journal starts with the next fill.</div>';return;}
 var open=[],closed=[];
 j.fills.forEach(function(f){(fParts(f).open?open:closed).push(f);});
 var tab=(window._fillTab!=null?window._fillTab:1);
 if(tab===1&&!open.length&&closed.length)tab=0;
 var btn=function(t,label,n){
  var on=tab===t;
  return '<button onclick="fTabSet('+t+')" style="font-size:15px;padding:8px 18px;margin-right:8px'+(on?';font-weight:bold;text-decoration:underline':'')+'">'+label+' <span style="opacity:0.7">'+n+'</span></button>';
 };
 var greens=j.open_hidden||0;
 var out='<div style="margin:2px 0 8px 0">'+btn(1,'open',open.length)+(greens?'<span style="color:#9ec49a;font-size:13px;margin-right:8px">+'+greens+' in profit</span>':'')+btn(0,'closed',closed.length)+'</div>';
 var list=tab===1?open:closed;
 if(!list.length)out+='<div class="card muted">nothing '+(tab===1?'open':'closed')+' right now</div>';
 else out+=list.map(fCard).join('');
 window._fillT0=Date.now()/1000;
 el.innerHTML=out;
}
function fTabSet(t){window._fillTab=t;fDraw();}
function render(d){
 fetch('/fills.json',{headers:hdrs(),cache:'no-store'}).then(function(r){return r.json();}).then(function(j){
  window._fillsJ=j;
  fDraw();
  if(!window._fillTick)window._fillTick=setInterval(fTick,1000);
 }).catch(function(){});
 return '<div class="card"><div class="muted">One card per purchase \\u2014 open lots tick as their exits earn; the color grades how it went. Tap a card for the story. Closed cards stay 3 days; open ones stay until they turn profitable.</div></div><div id="fl"><div class="card muted">loading\\u2026</div></div>';
}
"""

PAGES = {
    "/": ("3.0 — the meter", "meter", GRAPH_JS),
    "/fills": ("3.0 — purchases", "fills", FILLS_JS),
    "/status": ("3.0 — status", "status", STATUS_JS),
    "/orders": ("3.0 — orders", "orders", ORDERS_JS),
    "/plan": ("3.0 — the plan", "plan", PLAN_JS),
    "/switch": ("3.0 — switches", "switch", SWITCH_JS),
    "/silver": ("3.0 — the model", "model", SILVER_JS),
    "/grades": ("3.0 — grades", "grades", GRADES_JS),
    "/graph": ("3.0 — the meter", "meter", GRAPH_JS),
    "/watch": ("3.0 — considering", "watch", WATCH_JS),
    "/log": ("3.0 — log", "log", LOG_JS),
}


class WebServer:
    def __init__(self, monitor, port: int | None = None, bind: str = DEFAULT_BIND):
        self.monitor = monitor
        if port is None and os.environ.get("V1_ENABLED", "0") == "0":
            # 1.0 retired: 3.0 IS the front door on the public port
            self.port = int(os.environ.get("PORT", "8080"))
            self.bind = "0.0.0.0"
        else:
            self.port = (port if port is not None
                         else int(os.environ.get("V3_PORT", DEFAULT_PORT)))
            self.bind = bind
        self.password = os.environ.get("DASH_PASSWORD", "")
        self._httpd: ThreadingHTTPServer | None = None

    def data_payload(self) -> dict:
        # boot-time fallback only: once the first cycle completes, the
        # handler serves monitor.payload_json — bytes frozen on the
        # cycle thread, under the cycle lock, so the web thread never
        # serializes live dicts (the 2026-08-22 "unreachable" race)
        return self.monitor.build_phone_payload()

    def handle_op(self, body: dict) -> dict:
        op = str(body.get("op") or "")
        if op.startswith("switch_"):
            return {"ok": True,
                    "state": self.monitor.switch_tap(op[len("switch_"):],
                                                     str(body.get("which") or "master"))}
        if op == "refresh_rewards":
            return self.monitor.refresh_rewards()
        if op == "place":
            return self.monitor.owner_place(
                str(body.get("market") or ""), str(body.get("side") or ""),
                float(body.get("price") or 0), float(body.get("qty") or 0))
        if op in ("cancel", "move"):
            price = body.get("price")
            return self.monitor.order_op(op, str(body.get("order_id") or ""),
                                         float(price) if price is not None else None)
        if op == "set_fair":
            f = body.get("fair")
            return self.monitor.set_owner_fair(
                str(body.get("market") or ""),
                float(f) if f not in (None, "") else None)
        return {"ok": False, "note": f"unknown op {op}"}

    def start(self) -> None:
        server = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *a):  # noqa: A003 — quiet
                pass

            def _send(self, code: int, ctype: str, body: bytes) -> None:
                # gzip when the client accepts it: the data payload is
                # hundreds of KB of JSON, and the owner reads it over a
                # phone connection — 10x smaller on the wire
                enc = ""
                if (len(body) > 2048 and "gzip" in
                        (self.headers.get("Accept-Encoding") or "")):
                    body = gzip.compress(body, 5)
                    enc = "gzip"
                self.send_response(code)
                self.send_header("Content-Type", ctype)
                self.send_header("Cache-Control", "no-store")
                if enc:
                    self.send_header("Content-Encoding", enc)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):  # noqa: N802
                u = urlparse(self.path)
                path = u.path
                if path == "/v3" or path.startswith("/v3/"):
                    path = path[len("/v3"):] or "/"   # old bookmarks
                if path.startswith(("/map", "/lab", "/hunt", "/why",
                                    "/slate", "/unwind", "/v2")):
                    self.send_response(302)           # the old pages retired
                    self.send_header("Location", "/")
                    self.end_headers()
                    return
                route = path.rstrip("/") or "/"
                if route in PAGES:
                    title, here, js = PAGES[route]
                    self._send(200, "text/html; charset=utf-8",
                               _shell(title, here, js).encode())
                    return
                if route == "/book.json":
                    if not authed(self.headers.get, u.query, server.password):
                        self._send(401, "application/json", b'{"error":"key required"}')
                        return
                    from urllib.parse import parse_qs
                    slug = (parse_qs(u.query).get("m") or [""])[0]
                    self._send(200, "application/json",
                               json.dumps(server.monitor.book_view(slug)).encode())
                    return
                if route == "/fills.json":
                    if not authed(self.headers.get, u.query, server.password):
                        self._send(401, "application/json", b'{"error":"key required"}')
                        return
                    self._send(200, "application/json",
                               json.dumps(server.monitor.fills_view()).encode())
                    return
                if route == "/data.json":
                    if not authed(self.headers.get, u.query, server.password):
                        self._send(401, "application/json", b'{"error":"key required"}')
                        return
                    body = getattr(server.monitor, "payload_json", None)
                    if body is None:
                        try:      # first cycle still running: build live
                            body = json.dumps(server.data_payload()).encode()
                        except Exception as e:  # noqa: BLE001 — fail
                            # VISIBLY, never drop the socket
                            self._send(500, "application/json", json.dumps(
                                {"error": f"{type(e).__name__}: {e}"}).encode())
                            return
                    self._send(200, "application/json", body)
                    return
                self._send(404, "text/plain", b"not found")

            def do_POST(self):  # noqa: N802
                u = urlparse(self.path)
                p = u.path
                if p == "/v3" or p.startswith("/v3/"):
                    p = p[len("/v3"):] or "/"
                if p.rstrip("/") != "/op":
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
