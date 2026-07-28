// Liquidity Rewards — iOS home-screen widget (Scriptable)
//
// Setup (once):
//   1. Install the free "Scriptable" app from the App Store
//   2. Open Scriptable -> + -> paste this whole file -> name it "Rewards"
//   3. Fill in URL (your dashboard address) and PASSWORD below
//   4. Long-press the home screen -> add a small Scriptable widget ->
//      edit it -> Script: "Rewards"
//
// The widget shows earned-today, the live rate and market count, and
// refreshes itself roughly every 5 minutes (iOS decides the exact timing).

const URL = "https://YOUR-DASHBOARD-ADDRESS/widget.json";
const PASSWORD = "YOUR_DASH_PASSWORD";

const req = new Request(URL);
req.headers = {
  Authorization: "Basic " + Data.fromString("u:" + PASSWORD).toBase64String(),
};
req.timeoutInterval = 15;
let d = null;
try {
  d = await req.loadJSON();
} catch (e) {}

const w = new ListWidget();
w.backgroundColor = new Color("#0d1117");
w.setPadding(14, 14, 14, 14);
if (d && d.earned_today != null) {
  const cap = w.addText("EARNED TODAY");
  cap.font = Font.mediumSystemFont(10);
  cap.textColor = new Color("#8b949e");
  const t1 = w.addText("$" + d.earned_today.toFixed(2));
  t1.font = Font.boldSystemFont(32);
  t1.textColor = new Color("#e6edf3");
  t1.minimumScaleFactor = 0.6;
  w.addSpacer(4);
  const t2 = w.addText("~$" + d.rate_per_day.toFixed(2) + "/day");
  t2.font = Font.mediumSystemFont(14);
  t2.textColor = new Color("#58a6ff");
  const t3 = w.addText(d.markets + " markets" + (d.error ? " · ⚠" : ""));
  t3.font = Font.systemFont(11);
  t3.textColor = new Color(d.error ? "#f85149" : "#8b949e");
  if (d.updated) {
    const t4 = w.addText(d.updated);
    t4.font = Font.systemFont(9);
    t4.textColor = new Color("#484f58");
  }
} else {
  const t = w.addText("monitor unreachable");
  t.font = Font.mediumSystemFont(13);
  t.textColor = new Color("#f85149");
}
w.url = URL.replace("/widget.json", "/");  // tap opens the dashboard
w.refreshAfterDate = new Date(Date.now() + 5 * 60 * 1000);
Script.setWidget(w);
Script.complete();
