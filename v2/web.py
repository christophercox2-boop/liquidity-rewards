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
       ("opps", "opps"), ("calib", "calib"), ("log", "log"),
       ("switch", "switch"))

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
 body{--s1:#3987e5;--s2:#d95926}  /* validated categorical pair on this surface */
 .brow{display:flex;align-items:center;gap:6px;margin:3px 0;font-size:12px}
 .blab{width:54px;color:#8a93a5;text-align:right;flex:none}
 .btrack{flex:1;min-width:0;position:relative}
 .bar{height:8px;border-radius:0 4px 4px 0;min-width:1px}
 .bval{color:#e6e9ef;font-size:11px;margin-left:4px;flex:none;white-space:nowrap}
 .leg{display:inline-block;width:10px;height:10px;border-radius:3px;
      margin:0 4px 0 8px;vertical-align:-1px}
 summary{cursor:pointer}
 .sub{color:#aab3c5;font-size:14px;margin:3px 0}
 .hint{color:#8a93a5;font-size:12.5px;margin:5px 0 2px;line-height:1.5}
 details.how{margin:6px 0 0;font-size:12.5px;color:#8a93a5;line-height:1.5}
 details.how summary{color:#6f7a90;font-size:12px}
 .stats{display:flex;gap:20px;flex-wrap:wrap;margin:8px 0 2px}
 .stat .lab{color:#8a93a5;font-size:12px}
 .stat .val{font-size:22px;font-weight:700}
 .stat .val .u{font-size:13px;font-weight:400;color:#8a93a5}
 .drow{display:flex;align-items:center;gap:8px;margin:2px 0;min-height:20px;cursor:pointer}
 .dlab{width:40px;color:#aab3c5;text-align:right;flex:none;font-size:12px;
       font-variant-numeric:tabular-nums}
 .dtrack{flex:1;min-width:0;position:relative;height:20px}
 .gline{position:absolute;top:0;bottom:0;width:1px;background:#2a3242}
 .range{position:absolute;top:6px;height:8px;background:var(--s1);
        border-radius:4px;min-width:2px;opacity:.5}
 .dot{position:absolute;top:4px;width:8px;height:8px;border-radius:50%;
      border:2px solid #212a38;margin-left:-6px}
 .dot.mdl{background:var(--s1)} .dot.mkt{background:var(--s2)}
 .dval{flex:none;font-size:11px;color:#aab3c5;width:92px;text-align:right;
       font-variant-numeric:tabular-nums;white-space:nowrap}
 .axisr{display:flex;gap:8px;margin:0 0 2px}
 .axisl{width:40px;flex:none} .axisv{width:92px;flex:none}
 .axist{flex:1;position:relative;height:14px;color:#6f7a90;font-size:10.5px}
 .axist span{position:absolute;transform:translateX(-50%)}
 .thresh{display:flex;align-items:center;gap:8px;margin:5px 0;
         color:#ffce6b;font-size:11.5px}
 .thresh:before,.thresh:after{content:"";flex:1;border-top:1px dashed #55482a}
 .tipbox{display:none;background:#1a2230;border-radius:8px;padding:6px 9px;
         font-size:12px;color:#aab3c5;margin:2px 0 6px;line-height:1.55}
 .tipbox.open{display:block}
 .m50{position:absolute;top:-2px;bottom:-2px;width:1px;background:#5b667a}
 .chips{margin:4px 0} .chip{display:inline-block;background:#2a3242;
   border-radius:6px;padding:1px 8px;font-size:12px;margin:2px 4px 2px 0;color:#c6cddb}
 svg.spark{vertical-align:middle;margin-left:10px}
 .mtrack{height:10px;background:#2b3d5c;border-radius:5px;margin:8px 0 2px;
         position:relative;overflow:hidden}
 .mfill{position:absolute;left:0;top:0;bottom:0;background:var(--s1);
        border-radius:5px}
 .you{position:absolute;top:0;bottom:0;width:2px;background:#e6e9ef}
 .wf{display:flex;justify-content:space-between;gap:10px;margin:3px 0;
     font-size:14px;font-variant-numeric:tabular-nums}
 .wf .wl{color:#aab3c5} .wf .wv{white-space:nowrap}
 .wf.tot{border-top:1px solid #2a3242;padding-top:5px;font-weight:700}
"""

_PLUMBING = """
function hdrs(){const h=new Headers();h.set('X-Dash-Key',localStorage.getItem('dashKey')||'');return h;}
function saveKey(){localStorage.setItem('dashKey',document.getElementById('k').value);load();}
function usd(x){var v=x||0;return (v<0?'\\u2212$':'$')+Math.abs(v).toFixed(2);}
function pc(x){var v=Math.round((x||0)*1000)/10;return (v%1?v.toFixed(1):''+Math.round(v))+'\\u00A2';}
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
function rlab(s){var t=s.split('-').pop();
 if(t.indexOf('lte')===0)return '\\u2264'+t.slice(3);
 if(t.indexOf('gte')===0)return t.slice(3)+'+';
 return t;}
function mshort(s){
 if(s.indexOf('scc-senate-gop-')===0)return 'Senate '+rlab(s);
 if(s.indexOf('scc-hrep-rep-')===0)return 'House '+rlab(s);
 return '<code>'+s+'</code>';}
function mtitle(s){var t=s.split('-').pop();
 if(s.indexOf('scc-senate-gop-')===0){
  if(t.indexOf('lte')===0)return 'Senate: '+t.slice(3)+' GOP seats or fewer';
  if(t.indexOf('gte')===0)return 'Senate: '+t.slice(3)+' or more GOP seats';
  return 'Senate: exactly '+t+' GOP seats';}
 if(s.indexOf('scc-hrep-rep-')===0){
  if(t.indexOf('gte')===0)return 'House: '+t.slice(3)+' or more GOP seats';
  if(t.indexOf('lte')===0)return 'House: '+t.slice(3)+' GOP seats or fewer';}
 return s;}
var PMAP={earn:'earning',scout:'scout',exp1:'experiment',probe:'odds probe',
          sell:'selling stock',exit:'exiting'};
function pwhy(p){return PMAP[p]||p;}
function tip(el){var t=el.nextElementSibling;
 if(t&&t.className.indexOf('tipbox')>=0)t.classList.toggle('open');}
function spark(vals,cur){
 var all=vals.concat(cur!=null?[cur]:[]);
 if(all.length<2)return '';
 var W=96,H=26,P=3,mx=Math.max.apply(null,all),mn=Math.min(0,Math.min.apply(null,all));
 if(mx<=mn)mx=mn+1;
 function X(i){return P+(W-2*P)*i/(all.length-1);}
 function Y(v){return H-P-(H-2*P)*(v-mn)/(mx-mn);}
 var pts=all.map(function(v,i){return X(i).toFixed(1)+','+Y(v).toFixed(1);}).join(' ');
 var last=all[all.length-1];
 return '<svg class="spark" width="'+W+'" height="'+H+'" aria-hidden="true">'
  +'<polyline points="'+pts+'" fill="none" stroke="#5b667a" stroke-width="2" stroke-linejoin="round"/>'
  +'<circle cx="'+X(all.length-1).toFixed(1)+'" cy="'+Y(last).toFixed(1)+'" r="4" fill="var(--s1)" stroke="#212a38" stroke-width="2"/></svg>';}
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
 var hist=(e.history||[]).map(function(x){return x.earned||0;});
 var h='<div class="card">'+fresh+' <span class="muted">updated '+when(d.saved_at)+
   ' &middot; switch '+(sw.on?'<span class="ok">ON</span>':'off')+'</span>'+
   '<div class="big">'+usd(e.earned)+spark(hist,null)+'</div>'+
   '<div class="sub">estimated rewards so far today &middot; earning '+usd(e.rate)+
   ' per day at this minute</div>'+
   (e.stale_s>60?'<div class="hint warn">'+Math.round(e.stale_s/60)+
     ' minutes of today could not be measured (restarts or stale books) &mdash; the real number can only be higher</div>':'')+
   (d.restart_loop>=5?'<div class="bad">Restarting repeatedly: '+d.restart_loop+
     ' boots in the last hour. DigitalOcean runtime logs have the exit codes.</div>':'')+
   '';
 var rf=g.risk_families||{};var rfs=Object.keys(rf).map(function(k){
   var lab=k.indexOf('senate')>=0?'Senate book':k.indexOf('hrep')>=0?'House book':k;
   return '<span class="chip">'+lab+' '+usd(rf[k])+'</span>';}).join('');
 h+='<div class="stats">'+
   '<div class="stat"><div class="lab">worst case at risk</div><div class="val">'+usd(g.used)+
     '<span class="u"> of '+usd(g.ceiling)+'</span></div></div>'+
   '<div class="stat"><div class="lab">orders resting</div><div class="val">'+(g.orders||[]).length+'</div></div>'+
   '</div>'+
   '<div class="mtrack"><div class="mfill" style="width:'+
     Math.min(100*(g.used||0)/(g.ceiling||100),100)+'%"></div></div>'+
   (rfs?'<div class="chips">'+rfs+'</div>':'');
 if(g.mode&&g.mode!=='on')h+='<div class="hint">engine: '+g.mode+'</div>';
 if(g.sweep&&!g.sweep.done)h+='<div class="warn">handover sweep running &middot; '+(g.sweep.cancelled||0)+' cleared so far</div>';
 var rw=d.rewards_status||{};
 if(rw.checked_ago_s!=null){h+='<div class="hint">Rewards watch: checked '+
   Math.round(rw.checked_ago_s/60)+'m ago &middot; latest posted <b>'+(rw.latest_day||'?')+'</b> '+
   usd(rw.latest_usd)+(rw.latest_paid_usd>=rw.latest_usd?' <span class="ok">paid</span>':' pending')+
   ' &middot; new postings push your phone and refresh rewards.csv'+
   (rw.err?' &middot; <span class="warn">last check failed</span>':'')+'</div>';}
 h+='<details class="how"><summary>how these numbers work</summary>'+
   'Earned today is a live preview, integrated minute by minute from your resting orders '+
   'and the official scoring formula; Polymarket posts the real number 1&ndash;2 days later. '+
   'The little line (once two days have finished) shows completed days only &mdash; '+
   'today is the big number, never a point on the line. The risk number is the most the whole '+
   'book can actually lose, priced against the seat count itself &mdash; Senate rungs are '+
   'mutually exclusive, so shorts across them mostly share one collateral instead of stacking.'+
   (g.silent_cancels?' ('+g.silent_cancels+' orders so far vanished unfilled: the exchange '+
   'quietly cancels what buying power can&rsquo;t fund; the engine re-places them.)':'')+'</details>'+
   '<div class="muted" style="margin-top:6px"><a href="orders" style="color:#9ecbff">every order &rarr;</a>'+
   ' &nbsp; <a href="opps" style="color:#9ecbff">what it wants next &rarr;</a></div></div>';
 var er=(d.errors||[]).filter(function(x){return x.indexOf('booted build')<0;}).slice(-5).reverse();
 if(er.length){h+='<div class="card"><b class="warn">Recent trouble</b><div class="muted">'+er.join('<br>')+'</div></div>';}
 return h;
"""

ORDERS_JS = """
 var g=d.engine||{};var fx={};(d.forecasts||[]).forEach(function(f){if(f.id)fx[f.id]=f;});
 var go=(g.orders||[]).slice().sort(function(a,b){return (b.live_est||0)-(a.live_est||0);});
 var grp={earn:[],scout:[],exp1:[],stock:[]};
 go.forEach(function(o){
  var k=o.purpose==='earn'?'earn':o.purpose==='exp1'?'exp1':
        (o.purpose==='sell'||o.purpose==='close'||o.purpose==='exit')?'stock':'scout';
  grp[k].push(o);});
 function dsum(l){var t=0;l.forEach(function(o){t+=o.live_est||0;});return t;}
 var tot=dsum(go);
 function tbl(list){
  var t='<table>'+hrow(['market','order','earns','fill odds']);
  list.forEach(function(o){var f=fx[o.id]||{};
   t+=row(['<a href="order?id='+encodeURIComponent(o.id)+'" style="color:#9ecbff;text-decoration:none">'+
       mshort(o.market)+' &rsaquo;</a>',
     '<span style="white-space:nowrap">'+(o.side==='BUY'?'bid':'ask')+' '+o.qty+' @ '+pc(o.price)+'</span>',
     (o.live_est!=null?usd(o.live_est)+'/d':'<span class="muted">&ndash;</span>')+
       '<br><span class="muted">'+(o.live_ev!=null?usd(o.live_ev)+' after risk':'&ndash;')+'</span>',
     f.p_fill!=null?pct(f.p_fill)+'/d':'<span class="muted">&ndash;</span>']);});
  return t+'</table>';}
 var h='<div class="card"><b>Resting now</b>'+
  '<div class="sub">'+go.length+' orders earning about '+usd(tot)+'/day &mdash; '+
  usd(dsum(grp.earn))+' of it from the '+grp.earn.length+' sized orders.</div>';
 if(grp.earn.length)h+=tbl(grp.earn);
 else h+='<div class="muted">no sized orders resting</div>';
 if(grp.scout.length)h+='<details class="how"><summary>'+grp.scout.length+
  ' scouts &amp; probes &middot; '+usd(dsum(grp.scout))+'/d &mdash; 1-share feelers testing prices and odds</summary>'+
  tbl(grp.scout)+'</details>';
 if(grp.exp1.length)h+='<details class="how"><summary>'+grp.exp1.length+
  ' experiments &middot; probing the scoring-window rule</summary>'+tbl(grp.exp1)+'</details>';
 if(grp.stock.length)h+='<details class="how"><summary>'+grp.stock.length+
  ' selling stock &middot; re-offering filled shares at break-even +1 tick</summary>'+tbl(grp.stock)+'</details>';
 h+='<details class="how"><summary>how to read this</summary>'+
  '<b>earns</b> is what the order makes from the reward pool at this book right now; the line '+
  'under it subtracts the expected cost of getting filled (fills are usually losses here, not '+
  'wins). The engine only keeps sized orders whose after-risk number stays positive; scouts and '+
  'experiments pay pennies for information. <b>fill odds</b> is the chance of being filled '+
  'within a day, learned from how often each ladder&rsquo;s best price gets run over. '+
  'A dash means the book was too stale to score this cycle.</details></div>';
 var closed=(d.forecasts||[]).filter(function(f){return f.how;}).reverse();
 if(closed.length){
  var OMAP={fill:'filled',silent_cancel:'exchange cancelled',pulled:'pulled',
    repriced:'repriced',rotated_out:'swapped out',cancelled:'cancelled'};
  var counts={};closed.slice(0,40).forEach(function(f){
    var k=OMAP[f.how]||f.how;counts[k]=(counts[k]||0)+1;});
  h+='<div class="card"><b>What happened to recent orders</b>'+
  '<div class="chips">'+Object.keys(counts).map(function(k){
    return '<span class="chip">'+counts[k]+' '+k+'</span>';}).join('')+'</div>';
  function orow(f){
   var out=(OMAP[f.how]||f.how)+(f.rested_s?' after '+Math.round(f.rested_s/60)+'m':'');
   if(f.how==='fill'){out='<span class="warn">filled</span> '+(f.filled_qty||'')+
     (f.adverse!=null?' &middot; cost '+pc(f.adverse)+'/share an hour later':' &middot; grading in ~1h');}
   return row(['<a href="order?id='+encodeURIComponent(f.id)+'" style="color:#9ecbff;text-decoration:none">'+
     mshort(f.market)+' &rsaquo;</a>',
     '<span style="white-space:nowrap">'+f.side.toLowerCase()+' '+f.qty+' @ '+pc(f.price)+'</span>',
     pct(f.p_fill)+' odds<br><span class="muted">'+usd(f.ev)+'/d</span>',out]);}
  h+='<table>'+hrow(['market','order','predicted','outcome']);
  closed.slice(0,8).forEach(function(f){h+=orow(f);});
  h+='</table>';
  if(closed.length>8){h+='<details class="how"><summary>'+(closed.length-8)+' older</summary><table>';
   closed.slice(8,40).forEach(function(f){h+=orow(f);});h+='</table></details>';}
  h+='<div class="hint">Every placement is a recorded prediction; its outcome lands on the '+
   'same row. That record is what keeps the engine&rsquo;s guesses honest.</div></div>';}
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
 var so=(d.silver||{}).official||null;var fl=d.silver_flavors||{};
 var ctl=d.control||{};
 // ---- headline: who controls Congress, model vs market ----
 function mktControl(){  // market-implied P(GOP Senate control), from the ladder
  var over=0,tot=0,seen=0;
  Object.keys(lad).forEach(function(s){
   if(s.indexOf('scc-senate-gop-')!==0)return;
   var t=s.split('-').pop();var n=t.indexOf('gte')===0?parseInt(t.slice(3)):
     t.indexOf('lte')===0?-1:parseInt(t);
   var L=lad[s];if(!(L.bids[0]&&L.asks[0]))return;
   var mid=(L.bids[0][0]+L.asks[0][0])/2;
   tot+=mid;seen++;if(n>=50)over+=mid;});
  // thin books oversum badly; normalize by the whole ladder so the answer
  // is a probability, and refuse to answer when the ladder is junk
  if(seen<8||tot<0.7||tot>1.6)return null;
  return over/tot;}
 function ctlRange(ch){var c=ctl[ch];if(!c)return null;
  var vs=Object.values(c);return [Math.min.apply(null,vs),Math.max.apply(null,vs)];}
 function pctRange(r){var a=Math.round(r[0]*100),b=Math.round(r[1]*100);
  return Math.round(100*(r[0]+r[1])/2)+'%'+(a===b?'':'<span class="u"> ('+a+'&ndash;'+b+')</span>');}
 var sen=ctlRange('senate'),hou=ctlRange('house'),mk=mktControl();
 if(sen||hou){
  h+='<div class="card"><b>Who keeps Congress?</b>'+
   '<div class="sub">Chance Republicans keep control &mdash; Silver&rsquo;s simulations vs what the market charges.</div>'+
   '<div class="stats">';
  if(sen)h+='<div class="stat"><div class="lab">Senate &middot; model</div><div class="val">'+pctRange(sen)+'</div></div>';
  if(mk!=null)h+='<div class="stat"><div class="lab">Senate &middot; market</div><div class="val">'+Math.round(mk*100)+'%</div></div>';
  if(hou)h+='<div class="stat"><div class="lab">House &middot; model</div><div class="val">'+pctRange(hou)+'</div></div>';
  h+='</div>'+
   (so?'<div class="hint">Silver run of '+(so.date||'?')+
     (so.run_age_d!=null?', '+so.run_age_d+'d old':'')+
     ' &middot; brackets = their three model flavors disagreeing.'+
     (so.run_age_d>5?' <span class="warn">Stale run &mdash; bands widened with the poll model.</span>':'')+'</div>':'')+
   '</div>';}
 // ---- per-rung charts: model band + dots vs market ----
 var LEG='<span style="white-space:nowrap"><span class="leg" style="background:var(--s1)"></span><span class="muted">model</span>'
  +'<span class="leg" style="background:var(--s2)"></span><span class="muted">market</span></span>';
 [['Senate: how many GOP seats?','scc-senate-gop-',49.5,'50+ = GOP keeps the Senate (VP breaks the tie)'],
  ['House: chance of reaching each seat count','scc-hrep-rep-',217.5,'218 = a House majority']]
 .forEach(function(fam,fi){
  var slugs=Object.keys(lad).filter(function(s){return s.indexOf(fam[1])===0;})
    .sort(function(a,b){return rungKey(a)-rungKey(b);});
  var dist=slugs.map(function(s){var L=lad[s];var fr=fairs[s]||null;var fv=fl[s]||{};
    var mid=(L.bids[0]&&L.asks[0])?(L.bids[0][0]+L.asks[0][0])/2:null;
    return {s:s,k:rungKey(s),lab:rlab(s),flo:fr?fr[0]:null,fhi:fr?fr[1]:null,
            dx:fv.deluxe!=null?fv.deluxe:null,cl:fv.classic,li:fv.lite,mid:mid,
            bb:L.bids[0]?L.bids[0][0]:null,ba:L.asks[0]?L.asks[0][0]:null};});
  var mx0=0.01;dist.forEach(function(x){mx0=Math.max(mx0,x.fhi||0,x.mid||0);});
  var step=[0.01,0.02,0.025,0.05,0.1,0.25].filter(function(s){return 4*s>=mx0;})[0]||0.25;
  var mx=4*step;
  if(!dist.length)return;
  h+='<div class="card"><b>'+fam[0]+'</b> '+LEG;
  if(fi===0)h+='<div class="hint">Blue = the model, orange = the market. Together, the engine '+
   'earns at size; apart, it only scouts. Tap a row for the numbers.</div>';
  if(fi===1)h+='<div class="hint">Cumulative rungs &mdash; each row is AT LEAST that many seats, '+
   'so the values step downhill. Tap a row for the numbers.</div>';
  // axis
  var ticks=[0,1,2,3,4].map(function(i){return i*step;});
  h+='<div class="axisr"><span class="axisl"></span><div class="axist">'+
   ticks.map(function(t,i){var last=i===ticks.length-1;
    return '<span style="left:'+(100*t/mx)+'%'+(last?';transform:translateX(-100%)':'')+'">'+
     Math.round(t*100)+(last?'&cent;':'')+'</span>';}).join('')+
   '</div><span class="axisv"></span></div>';
  var glines=ticks.slice(1,4).map(function(t){return '<div class="gline" style="left:'+(100*t/mx)+'%"></div>';}).join('');
  var shown=false;
  dist.forEach(function(x){
   if(!shown&&x.k>fam[2]){h+='<div class="thresh">'+fam[3]+'</div>';shown=true;}
   var track=glines;
   if(x.flo!=null)track+='<div class="range" style="left:'+(100*x.flo/mx)+'%;width:'+
     Math.max(100*(x.fhi-x.flo)/mx,1)+'%"></div>';
   if(x.dx!=null)track+='<div class="dot mdl" style="left:'+(100*x.dx/mx)+'%"></div>';
   if(x.mid!=null)track+='<div class="dot mkt" style="left:'+(100*x.mid/mx)+'%"></div>';
   var val=(x.dx!=null?Math.round(x.dx*100):'&ndash;')+' / '+(x.mid!=null?Math.round(x.mid*100):'&ndash;')+'&cent;';
   h+='<div class="drow" onclick="tip(this)"><span class="dlab">'+x.lab+'</span>'+
    '<div class="dtrack">'+track+'</div><span class="dval">'+val+'</span></div>';
   var tips=[];
   tips.push('<b>'+mtitle(x.s)+'</b>');
   if(x.dx!=null)tips.push('model: Classic '+(x.cl!=null?pc(x.cl):'&ndash;')
     +' &middot; Deluxe '+pc(x.dx)+' &middot; Lite '+(x.li!=null?pc(x.li):'&ndash;'));
   else if(x.flo!=null)tips.push('model band '+pc(x.flo)+'&ndash;'+pc(x.fhi));
   if(x.bb!=null||x.ba!=null)tips.push('market: bid '+(x.bb!=null?pc(x.bb):'&ndash;')+' / ask '+(x.ba!=null?pc(x.ba):'&ndash;'));
   if((ours[x.s]||[]).length)tips.push('ours: '+ours[x.s].join(', '));
   var rate=(e.market_rates||{})[x.s];if(rate)tips.push('earning '+usd(rate)+'/day here');
   h+='<div class="tipbox">'+tips.join('<br>')+'</div>';});
  h+='</div>';});
 // ---- race odds: competitive first ----
 var races=d.silver_races||{};
 var rk=Object.keys(races);
 if(rk.length){
  var comp=rk.filter(function(a){return races[a]>0.10&&races[a]<0.90;})
    .sort(function(a,b){return Math.abs(races[a]-0.5)-Math.abs(races[b]-0.5);});
  var safeR=rk.filter(function(a){return races[a]>=0.90;}).length;
  var safeD=rk.filter(function(a){return races[a]<=0.10;}).length;
  h+='<div class="card"><details><summary><b>The races behind it</b> <span class="muted">'+
   comp.length+' competitive &middot; '+safeR+' safe GOP &middot; '+safeD+' safe Dem</span></summary>'+
   '<div class="hint">Chance the Republican wins each race, from Silver&rsquo;s poll-driven table. '+
   'The gray line is 50/50. These feed the fallback model that takes over if the simulation '+
   'sheet goes stale. 31 GOP seats aren&rsquo;t on the ballot at all.</div>';
  function racerow(a){return '<div class="brow"><span class="blab">'+a.toUpperCase()+'</span>'+
   '<div class="btrack"><div class="bar" style="background:var(--s1);width:'+(races[a]*100)+'%"></div>'+
   '<div class="m50" style="left:50%"></div></div>'+
   '<span class="bval">'+Math.round(races[a]*100)+'%</span></div>';}
  comp.forEach(function(a){h+=racerow(a);});
  var rest=rk.filter(function(a){return comp.indexOf(a)<0;})
    .sort(function(a,b){return races[b]-races[a];});
  if(rest.length){h+='<details class="how"><summary>the '+rest.length+' safe seats</summary>';
   rest.forEach(function(a){h+=racerow(a);});h+='</details>';}
  h+='</details></div>';}
 h+='<div class="card"><details><summary><b>The same ladders as numbers</b> '+
  '<span class="muted">every rung, model band, book, and our orders</span></summary>';
 [['Senate','scc-senate-gop-'],['House','scc-hrep-rep-']].forEach(function(fam){
  var slugs=Object.keys(lad).filter(function(s){return s.indexOf(fam[1])===0;})
    .sort(function(a,b){return rungKey(a)-rungKey(b);});
  if(!slugs.length)return;
  h+='<div style="margin-top:6px"><b>'+fam[0]+'</b></div><table>'+hrow(['rung','model band','bid/ask','ours','$/day']);
  slugs.forEach(function(s){var L=lad[s];var bb=L.bids[0]?pc(L.bids[0][0]):'&mdash;';
   var ba=L.asks[0]?pc(L.asks[0][0]):'&mdash;';var fr=fairs[s]||null;
   h+=row([rlab(s),
     fr?pc(fr[0])+'&ndash;'+pc(fr[1]):'<span class="muted">&mdash;</span>',
     bb+' / '+ba,(ours[s]||[]).join('<br>')||'<span class="muted">&middot;</span>',
     usd((e.market_rates||{})[s])]);});
  h+='</table>';
 });
 h+='<div class="muted">model = the spread across Silver&rsquo;s Classic/Deluxe/Lite runs '
  +'(widened by the poll-driven model when the run is stale); blank = no model</div></details></div>';
 return h;
"""

OPPS_JS = """
 var g=d.engine||{};var h='';
 var cands=g.cands||[];
 h+='<div class="card"><b>What the engine wants next</b>'+
  '<div class="sub">Ideas it liked this cycle, best first. It places the top ones as '+
  'actions and headroom allow.</div>';
 function crow(c){return row([mshort(c.market)+'<br><span class="muted">'+
    pwhy(c.purpose)+(c.exp1_gap?' &middot; boundary':'')+'</span>',
    '<span style="white-space:nowrap">'+(c.side==='BUY'?'bid':'ask')+' '+c.qty+' @ '+pc(c.price)+'</span>',
    usd(c.exp_earn),usd(c.ev),usd(c.cost)]);}
 if(cands.length){h+='<table>'+hrow(['market','order','$/day','after risk','uses']);
  cands.slice(0,8).forEach(function(c){h+=crow(c);});h+='</table>';
  if(cands.length>8){h+='<details class="how"><summary>'+(cands.length-8)+' more ideas</summary><table>';
   cands.slice(8).forEach(function(c){h+=crow(c);});h+='</table></details>';}
 }else{h+='<div class="muted">nothing above the bar right now</div>';}
 h+='<details class="how"><summary>how ideas are scored</summary>'+
  'Size is chosen to maximise value, not filled to a cap: your share of a side '+
  'saturates as the order grows (you can never earn more than the whole side pool), '+
  'while fill risk keeps rising in a straight line &mdash; so there is a peak, and the '+
  'engine stops there. While fill costs are still an estimate rather than measured, it '+
  'takes half that peak. '+
  'For each price level: what it would earn from the pool per day, minus '+
  '(chance of being filled) &times; (what that fill usually costs). Only positive '+
  'after-risk ideas qualify, and <b>uses</b> is how much of the $'+((g.ceiling||0))+
  ' ceiling the order would consume &mdash; measured as what it adds to the worst case, '+
  'so an ask sheltered by a bigger short on a sibling rung can be nearly free.</details></div>';
 var rej=g.rejected||[];
 if(rej.length){
  function rrow(c){return row([mshort(c.market),
    '<span style="white-space:nowrap">'+(c.side==='BUY'?'bid':'ask')+' '+c.qty+' @ '+pc(c.price)+'</span>',
    usd(c.exp_earn),usd(c.p_fill*c.fill_cost*c.qty),usd(c.ev)]);}
  h+='<div class="card"><b>Turned down</b> <span class="muted">closest misses &mdash; the risk math said no</span>'+
  '<table>'+hrow(['market','order','$/day','risk cost/d','after risk']);
  rej.slice(0,5).forEach(function(c){h+=rrow(c);});h+='</table>';
  if(rej.length>5){h+='<details class="how"><summary>'+(rej.length-5)+' more</summary><table>';
   rej.slice(5).forEach(function(c){h+=rrow(c);});h+='</table></details>';}
  h+='</div>';}
 var fm=d.fillmodel||{};var hz=fm.hazards||{};
 var BL={0:'at the touch',1:'1 tick back',2:'2 ticks back',3:'3+ back'};
 var famlab=function(k){var f=k.split(' ')[0];
   return f.indexOf('senate')>=0?'Senate':(f.indexOf('house')>=0||f.indexOf('hrep')>=0)?'House':f;};
 var hzlab=function(k){var p=k.split(' ');
   return famlab(k)+(p[1]?' &middot; '+(p[1]==='BUY'?'bids':'asks'):'');};
 var anyCross=0,hours=0;Object.keys(hz).forEach(function(k){
   hours=Math.max(hours,(hz[k][0]||{}).hours_observed||0);
   [0,1,2,3].forEach(function(b){anyCross+=((hz[k][b]||{}).crossings||0);});});
 var md=fm.markdown||{};var mn=fm.marks_n||{};var sf=fm.scoring_frac||{};
 var costRows=Object.keys(md).map(function(k){
   return famlab(k)+': '+pc(md[k])+' per share <span class="muted">('+(mn[k]||0)+' graded fills)</span>';});
 var sfRows=Object.keys(sf).map(function(k){return famlab(k)+' '+pct(sf[k]);});
 h+='<div class="card"><details><summary><b>What the odds are learned from</b> <span class="muted">'+
  hours+'h watched &middot; '+anyCross+' price crossings</span></summary>'+
  '<div class="hint">Fill odds come from how often each ladder&rsquo;s best price actually gets '+
  'run over, per side and distance from the touch. Fewer crossings farther back = resting deeper '+
  'is safer but earns less.'+
  (anyCross<5?' Almost no real crossings yet, so the bars are mostly the cautious '+
   'starting guesses; they sharpen as watched hours pile up.':'')+'</div>';
 Object.keys(hz).forEach(function(k){var r=hz[k];
  var mx=0;[0,1,2,3].forEach(function(b){mx=Math.max(mx,(r[b]||{}).per_day||0);});
  h+='<div style="margin:8px 0 2px;font-size:13px"><b>'+hzlab(k)+'</b> <span class="muted">'
    +((r[0]||{}).hours_observed||0)+'h watched</span></div>';
  [0,1,2,3].forEach(function(b){var c=r[b]||{};
   h+='<div class="brow"><span class="blab" style="width:70px">'+BL[b]+'</span>'
    +'<div class="btrack"><div class="bar" style="background:var(--s1);width:'+(mx?100*(c.per_day||0)/mx:0)+'%"></div></div>'
    +'<span class="bval">'+((c.per_day||0)).toFixed(2)+'/day <span class="muted">'+(c.crossings||0)+' seen</span></span></div>';});
 });
 h+='<div class="hint" style="margin-top:8px"><b>When a fill does happen, what does it cost?</b> '+
  (costRows.length?costRows.join(' &middot; '):'no graded fills yet &mdash; using the cautious starting guess of 2&cent;/share')+
  '. Each real fill is graded against the market&rsquo;s mid an hour later.</div>'+
  (sfRows.length?'<div class="hint"><b>Share of resting time that actually scores:</b> '+sfRows.join(' &middot; ')+'</div>':'')+
  '</details></div>';
 var ex=((d.engine_saved||{}).exp1||[]).slice(-15).reverse();
 h+='<div class="card"><details><summary><b>The window experiment</b> <span class="muted">'+
  ex.length+' edge cases on record</span></summary>'+
  '<div class="hint">Polymarket&rsquo;s rules are ambiguous about orders at the edge of the scoring '+
  'window: the generous reading says the whole price level earns, the strict one says late joiners '+
  'earn nothing. We act on the generous reading and record BOTH predictions for every edge case; '+
  'the real payouts will crown one.</div>';
 if(ex.length){h+='<table>'+hrow(['placed','market','order','generous says','strict says']);
  ex.forEach(function(x){h+=row([when(x.ts),mshort(x.market),
    x.side.toLowerCase()+' '+x.qty+' @ '+pc(x.price),usd(x.pred_level_day)+'/d',usd(x.pred_queue_day)+'/d']);});
  h+='</table>';}else{h+='<div class="muted">no edge cases placed yet</div>';}
 h+='</details></div>';
 return h;
"""

ORDER_JS = """
 var id=decodeURIComponent((location.search.match(/[?&]id=([^&]+)/)||[])[1]||'');
 var g=d.engine||{};var o=null;(g.orders||[]).forEach(function(x){if(x.id===id)o=x;});
 var f=null;(d.forecasts||[]).forEach(function(x){if(x.id===id)f=x;});
 if(!o&&!f)return '<div class="card">This order is not in the last 100 records. '+
  '<a href="orders" style="color:#9ecbff">&larr; back to orders</a></div>';
 var src=o||f;var mkt=src.market,side=src.side,price=src.price,qty=src.qty;
 var purpose=src.purpose||(f||{}).purpose||'';
 var OMAP={fill:'filled',silent_cancel:'cancelled by the exchange',pulled:'pulled (left the safe band)',
   repriced:'repriced',rotated_out:'swapped for a better idea',cancelled:'cancelled'};
 var h='<div class="card"><b>'+mtitle(mkt)+'</b>'+
  '<div class="sub">'+(side==='BUY'?'bid':'ask')+' '+qty+' @ '+pc(price)+' &middot; '+pwhy(purpose)+
  (o&&o.placed_ts&&d.saved_at?' &middot; resting '+Math.round((d.saved_at-o.placed_ts)/60)+'m':'')+
  (o?'':' &middot; <span class="warn">closed</span>')+'</div>';
 if(!o&&f&&f.how){
  h+='<div class="hint"><b>Outcome:</b> '+(OMAP[f.how]||f.how)+
   (f.rested_s?' after '+Math.round(f.rested_s/60)+' minutes resting':'')+
   (f.how==='fill'&&f.adverse!=null?'. The fill cost '+pc(f.adverse)+'/share, graded against the mid an hour later (it predicted '+pc(f.fill_cost)+').':'.')+'</div>';}
 // where the price sits: band, market, and this order on one strip
 var fr=(d.fairs||{})[mkt];var fl=(d.silver_flavors||{})[mkt]||{};var L=(d.ladders||{})[mkt];
 var mid=(L&&L.bids[0]&&L.asks[0])?(L.bids[0][0]+L.asks[0][0])/2:null;
 var mx0=Math.max(fr?fr[1]:0,mid||0,price,0.01);
 var step=[0.01,0.02,0.025,0.05,0.1,0.25].filter(function(s){return 4*s>=mx0;})[0]||0.25;
 var mx=4*step;var track='';
 [1,2,3].forEach(function(i){track+='<div class="gline" style="left:'+(25*i)+'%"></div>';});
 if(fr)track+='<div class="range" style="left:'+(100*fr[0]/mx)+'%;width:'+Math.max(100*(fr[1]-fr[0])/mx,1)+'%"></div>';
 if(fl.deluxe!=null)track+='<div class="dot mdl" style="left:'+(100*fl.deluxe/mx)+'%"></div>';
 if(mid!=null)track+='<div class="dot mkt" style="left:'+(100*mid/mx)+'%"></div>';
 track+='<div class="you" style="left:'+Math.min(100*price/mx,100)+'%"></div>';
 var offband=fr&&((side==='BUY'&&price>fr[1]+0.011)||(side==='SELL'&&price<fr[0]-0.011));
 h+='<div class="drow" style="cursor:default"><span class="dlab">0</span><div class="dtrack">'+track+
  '</div><span class="dval">'+Math.round(mx*100)+'&cent;</span></div>'+
  '<div class="hint"><span class="leg" style="background:var(--s1)"></span>model band'+
  '<span class="leg" style="background:var(--s2)"></span>market mid &middot; the white line is this order'+
  (offband?' <span class="warn">&middot; outside the band &mdash; the guard pulls it unless the band moves</span>':'')+'</div></div>';
 var lp=o?o.live_parts:null;
 if(lp){
  var earn=lp.share*lp.side_pool;var sf=lp.scoring_frac;
  h+='<div class="card"><b>What it earns</b>';
  if(L){
   var lv=(side==='BUY'?L.bids:L.asks)||[];
   var tgt=(((d.terms||{}).current||{})[mkt]||[])[1]||null;
   var mq=1;lv.forEach(function(x){mq=Math.max(mq,x[1]);});
   var cum=0;
   h+='<div class="hint">The '+(side==='BUY'?'bid':'ask')+' book, best price first. Only the window scores: '+
    'the first levels that together hold the '+(tgt?tgt.toLocaleString():'?')+'-share target.</div>';
   lv.forEach(function(x){
    var inw=tgt?cum<tgt:true;cum+=x[1];
    var yours=Math.abs(x[0]-price)<1e-9;
    h+='<div class="brow"><span class="blab">'+pc(x[0])+'</span>'+
     '<div class="btrack"><div class="bar" style="background:'+(yours?'var(--s1)':'#3a4456')+
     ';width:'+(100*Math.sqrt(x[1])/Math.sqrt(mq))+'%"></div></div>'+
     '<span class="bval">'+Math.round(x[1]).toLocaleString()+
     (yours?' &middot; <b>yours: '+qty+'</b>':'')+
     (inw?'':' <span class="muted">outside</span>')+'</span></div>';});
  }
  h+='<div class="wf"><span class="wl">share of the scoring '+(side==='BUY'?'bid':'ask')+' side</span><span class="wv">'+pct(lp.share)+'</span></div>'+
   '<div class="wf"><span class="wl">&times; this market&rsquo;s daily side pool</span><span class="wv">'+usd(lp.side_pool)+'</span></div>'+
   '<div class="wf"><span class="wl">&times; time actually scoring</span><span class="wv">'+pct(sf)+'</span></div>'+
   '<div class="wf tot"><span class="wl">earns</span><span class="wv ok">+'+usd(earn*sf)+'/d</span></div>'+
   (lp.in_window?'':'<div class="hint warn">Currently OUTSIDE the scoring window &mdash; earning $0 until the book shifts or the engine moves it.</div>')+
   '</div>';
  var fam=mkt.indexOf('scc-senate-gop-')===0?'senate-seats':mkt.indexOf('scc-hrep-rep-')===0?'house-seats':'other';
  var fm=d.fillmodel||{};var hzr=(fm.hazards||{})[fam+' '+side]||{};
  var bi=Math.min(lp.ticks==null?0:lp.ticks,3);var cell=hzr[bi]||{};
  var BL={0:'at the touch',1:'1 tick back',2:'2 ticks back',3:'3+ ticks back'};
  var md=(fm.markdown||{})[fam];var nm=(fm.marks_n||{})[fam]||0;
  var conc=md!=null?Math.max((lp.fill_cost||0)-md,0):0;
  var risk=lp.p_fill*lp.fill_cost*qty;
  h+='<div class="card"><b>What a fill would cost</b>'+
   '<div class="wf"><span class="wl">chance of a fill today ('+BL[bi]+')</span><span class="wv">'+pct(lp.p_fill)+'</span></div>'+
   '<div class="wf"><span class="wl">&times; cost per share if filled</span><span class="wv">'+pc(lp.fill_cost)+'</span></div>'+
   '<div class="wf"><span class="wl">&times; '+qty+' shares</span><span class="wv"></span></div>'+
   '<div class="wf tot"><span class="wl">fill risk</span><span class="wv bad">&minus;'+usd(risk)+'/d</span></div>'+
   '<div class="hint"><b>Evidence for the odds:</b> watched this ladder&rsquo;s '+(side==='BUY'?'bid':'ask')+
   ' side for '+(cell.hours_observed||0)+' hours and saw the price run over '+BL[bi]+' '+(cell.crossings||0)+
   ((cell.crossings||0)===1?' time':' times')+
   ((cell.crossings||0)<3?' &mdash; mostly the cautious starting guess until more hours pile up':'')+'.</div>'+
   '<div class="hint"><b>Evidence for the cost:</b> '+
   (nm?nm+' real fills, graded against the mid an hour later, average '+pc(md):'no graded fills yet &mdash; using the cautious 2&cent; starting guess')+
   (conc>0.001?'; plus this price sits '+pc(conc)+' past the band edge, conceded the moment it fills':'')+'.</div></div>';
  var after=earn*sf-risk;
  h+='<div class="card"><b>The verdict</b>'+
   '<div class="wf"><span class="wl">earns</span><span class="wv ok">+'+usd(earn*sf)+'/d</span></div>'+
   '<div class="wf"><span class="wl">fill risk</span><span class="wv bad">&minus;'+usd(risk)+'/d</span></div>'+
   '<div class="wf tot"><span class="wl">after risk</span><span class="wv '+(after>=0?'ok':'bad')+'">'+usd(after)+'/d</span></div>'+
   (f?'<div class="hint">At placement it predicted '+pct(f.p_fill)+' fill odds and '+usd(f.ev)+'/d after risk. '+
     'Scouts and experiments are allowed to run slightly negative &mdash; they buy information.</div>':'')+'</div>';
 } else if(o){
  h+='<div class="card hint">Re-evaluating against the live book &mdash; the components appear within a cycle (~45 seconds).</div>';
 } else if(f){
  h+='<div class="card"><b>The prediction it was placed with</b>'+
   '<div class="wf"><span class="wl">expected earnings</span><span class="wv">+'+usd(f.exp_earn)+'/d</span></div>'+
   '<div class="wf"><span class="wl">fill odds &times; cost &times; size</span><span class="wv">&minus;'+usd((f.p_fill||0)*(f.fill_cost||0)*qty)+'/d</span></div>'+
   '<div class="wf tot"><span class="wl">after risk</span><span class="wv">'+usd(f.ev)+'/d</span></div></div>';
 }
 h+='<div class="muted"><a href="orders" style="color:#9ecbff">&larr; all orders</a> &nbsp; '+
  '<a href="calib" style="color:#9ecbff">how honest are these predictions? &rarr;</a></div>';
 return h;
"""

CALIB_JS = """
 var fx=d.forecasts||[];
 var closed=fx.filter(function(f){return f.how&&f.p_fill!=null&&f.rested_s!=null;});
 var open=fx.filter(function(f){return !f.how;}).length;
 function pAt(f){return 1-Math.pow(1-f.p_fill,Math.max(f.rested_s,60)/86400);}
 var BINS=[[0,0.01,'<1%'],[0.01,0.03,'1\\u20133%'],[0.03,0.08,'3\\u20138%'],
           [0.08,0.2,'8\\u201320%'],[0.2,1.01,'20%+']];
 var h='<div class="card"><b>Fill odds: predicted vs what happened</b>'+
  '<div class="sub">'+closed.length+' resolved predictions'+(open?' &middot; '+open+' still open':'')+
  '. Each order carried a predicted chance of filling over the time it actually rested; '+
  '1-share probes deliberately visit the under-tested buckets so every row fills in.</div>'+
  '<span class="leg" style="background:var(--s1)"></span><span class="muted">predicted</span>'+
  '<span class="leg" style="background:var(--s2)"></span><span class="muted">happened</span>';
 if(closed.length<8)h+='<div class="hint warn">Small sample &mdash; a sketch, not a verdict, until this grows.</div>';
 var rows=[],wp=0,wr=0,mxr=0.01;
 BINS.forEach(function(b){
  var sel=closed.filter(function(f){var p=pAt(f);return p>=b[0]&&p<b[1];});
  if(!sel.length)return;
  var ap=0,hits=0;sel.forEach(function(f){ap+=pAt(f);if(f.how==='fill')hits++;});
  ap/=sel.length;var real=hits/sel.length;
  wp+=ap*sel.length;wr+=hits;
  mxr=Math.max(mxr,ap,real);
  rows.push({lab:b[2],p:ap,r:real,n:sel.length});});
 rows.forEach(function(x){
  h+='<div class="brow"><span class="blab" style="width:56px">'+x.lab+'</span><div class="btrack">'+
   '<div class="bar" style="background:var(--s1);width:'+(100*x.p/mxr)+'%"></div>'+
   '<div class="bar" style="background:var(--s2);width:'+Math.max(100*x.r/mxr,0.5)+'%;margin-top:2px"></div>'+
   '</div><span class="bval">'+Math.round(x.p*100)+'% &rarr; '+Math.round(x.r*100)+'% <span class="muted">n='+x.n+'</span></span></div>';});
 if(closed.length){
  wp/=closed.length;var wrf=wr/closed.length;
  var verdict=wrf<wp*0.6?'<b>Overconfident about fills</b> &mdash; they happen less than predicted. The safe direction to err, but it may be resting farther back than it needs to.'
   :wrf>wp*1.5?'<b>Underconfident about fills</b> &mdash; they happen more than predicted. Fill risk is being underpriced; expect the engine to pull back as this feeds in.'
   :'<b>Roughly calibrated</b> so far.';
  h+='<div class="hint">Overall: predicted '+Math.round(wp*100)+'%, happened '+Math.round(wrf*100)+'%. '+verdict+'</div>';}
 h+='<details class="how"><summary>how to read this</summary>'+
  'Blue = the engine&rsquo;s predicted fill chance, orange = how often those orders really filled, '+
  'bucketed by confidence. Equal bars = honest odds. Orange shorter = overconfident; longer = '+
  'underconfident. A cancelled order counts as no-fill over the time it rested &mdash; the fair '+
  'comparison, since it never got its full day.</details></div>';
 var marked=fx.filter(function(f){return f.adverse!=null;});
 h+='<div class="card"><b>Fill cost: predicted vs measured</b>';
 if(marked.length){
  var fams={};marked.forEach(function(f){var k=f.market.indexOf('senate')>=0?'Senate':'House';
   (fams[k]=fams[k]||[]).push(f);});
  h+='<table>'+hrow(['ladder','predicted','measured','fills']);
  Object.keys(fams).forEach(function(k){var l=fams[k];var ap=0,ar=0;
   l.forEach(function(x){ap+=x.fill_cost||0;ar+=x.adverse;});
   h+=row([k,pc(ap/l.length)+'/share',pc(ar/l.length)+'/share',l.length]);});
  h+='</table><div class="hint">Measured = each real fill graded against the market&rsquo;s mid an hour '+
   'later. Predicted above measured = the engine charges itself too much for fills and is too shy; '+
   'below = too little, too bold.</div>';
 }else{h+='<div class="muted">No graded fills yet &mdash; each fill grades about an hour after it happens.</div>';}
 h+='</div>';
 h+='<div class="card hint">The scoring-window experiment (generous vs strict readings of the reward '+
  'rule) grades against real payouts as they post &mdash; it lives on '+
  '<a href="opps" style="color:#9ecbff">opps</a>.</div>';
 return h;
"""

LOG_JS = """
 var h='';var es=d.engine_saved||{};
 function card(title,rows,fmt){
  h+='<div class="card"><b>'+title+'</b>';
  if(rows&&rows.length){
   var rev=rows.slice().reverse();
   h+='<table>';rev.slice(0,8).forEach(function(x){h+=fmt(x);});h+='</table>';
   if(rev.length>8){h+='<details class="how"><summary>'+(Math.min(rev.length,40)-8)+
    ' older</summary><table>';rev.slice(8,40).forEach(function(x){h+=fmt(x);});h+='</table></details>';}
  }else{h+='<div class="muted">nothing yet</div>';}
  h+='</div>';}
 var EMAP={place:'placed',fill:'FILLED',silent_cancel:'exchange cancelled',pull:'pulled',
   reprice:'repriced',rotate_out:'swapped out',evict:'evicted foreign order',
   sweep:'handover sweep',refused:'desk refused'};
 card('Engine events',es.log,function(x){
  var rest=Object.keys(x).filter(function(k){return k!=='ts'&&k!=='event'&&k!=='market';})
   .map(function(k){return k+'='+x[k];}).join(' ');
  return row([when(x.ts),(EMAP[x.event]||x.event)+(x.market?' &middot; '+mshort(x.market):''),
   '<span class="muted">'+rest+'</span>']);});
 card('Order desk',d.audit,function(x){
  var rest=Object.keys(x).filter(function(k){return k!=='ts';})
   .map(function(k){return k+'='+x[k];}).join(' ');
  return row([when(x.ts),'<span class="muted">'+rest+'</span>']);});
 card('Alerts',d.alert_log,function(x){
  return row([when(x.ts),(x.sent?'&#128276;':'<span class="muted">held</span>'),
    x.title+' <span class="muted">'+(x.msg||'')+(x.why?' ('+x.why+')':'')+'</span>']);});
 card('Reward terms changes',d.terms_history,function(t){
  return row([when(t.ts),mshort(t.slug),'<span class="muted">'+t.why+
    (t.pool!=null?(' $'+t.pool+' pool / '+t.target+' target / &divide;'+t.event_n+' markets'):'')+'</span>']);});
 card('Trouble',(d.errors||[]).map(function(e){return {ts:0,line:e};}),function(x){
  return row(['<span class="muted">'+x.line+'</span>']);});
 return h;
"""


def build_shells() -> dict[str, str]:
    return {
        "/": _page("status", "2.0", STATUS_JS),
        "/orders": _page("orders", "2.0 orders", ORDERS_JS),
        "/markets": _page("markets", "2.0 markets", MARKETS_JS),
        "/opps": _page("opps", "2.0 opportunities", OPPS_JS),
        "/order": _page("orders", "2.0 order", ORDER_JS),
        "/calib": _page("calib", "2.0 calibration", CALIB_JS),
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
