"""Politics: the first family, and the reason 3.0 exists.

Discovery is the events feed under the politics/elections tags — the
authoritative source, not slug heuristics. It carries three things the
engine needs and one it must never lose:

* every open market, with the event it belongs to;
* the EVENT SIZE — the pool divisor. A market discovered here has a
  confirmed divisor by construction, which is the only condition under
  which the engine shows a dollar estimate;
* the feed's own names for everything;
* and a hard NO at the door for economics markets (standing owner rule —
  the exchange's politics tag includes CPI/Fed markets; we never touch
  them, not even read-only in the universe).

Candidate markets of one race are sometimes modeled as separate
single-market events while the pool covers the whole race, so the event
size is raised to the race-group size (slug minus its last token) when
that group is larger — 1.0's rule, kept.

The config: known ground. Join the touch only when the book is provably
quiet, revive dead sides inside tight collateral caps, rest every day
(politics has no game days). The owner's preference verbatim: "rest near
the touch in LOW-volatility markets where fill risk is small. Fills are
usually losses here, not wins."
"""

from __future__ import annotations

from .family import FamilyConfig
from .names import name_from_market
from .programs import is_econ

TAGS = ("politics", "elections")


def discover(client) -> dict[str, dict]:
    """slug -> {event_n, name} for every open, non-econ politics market."""
    out: dict[str, dict] = {}
    order: list[str] = []
    for tag in TAGS:
        try:
            events = client.events_by_tag(tag)
        except Exception:  # noqa: BLE001 — one bad tag must not sink the other
            continue
        for ev in events:
            title = str(ev.get("title") or ev.get("name") or "").strip()
            rows = [m for m in ev.get("markets") or []
                    if m.get("slug") and not m.get("closed")
                    and not is_econ(m["slug"])]
            for m in rows:
                slug = m["slug"]
                if slug not in out:
                    order.append(slug)
                out[slug] = {"event_n": len(rows),
                             "name": name_from_market(m, title)[:110]}
    # single-market events that are really one race sharing one pool
    groups: dict[str, list[str]] = {}
    for s in order:
        groups.setdefault(s.rsplit("-", 1)[0], []).append(s)
    for s in order:
        g = groups[s.rsplit("-", 1)[0]]
        if len(g) > out[s]["event_n"]:
            out[s]["event_n"] = len(g)
    return out


def config() -> FamilyConfig:
    return FamilyConfig(
        name="Politics", tag="POL",
        known_ground=True, rest_style="join_quiet", revive=True,
        vol_quiet=0.15,
        # Owner, 2026-08-20 (the flatten rebuild): "increase the budget
        # to 100" — one hundred dollars of collateral at risk, total —
        # then "It shouldn't be necessarily two dollars per market, feel
        # free to do up to $20 per market. Just be very picky with which
        # ones you're into and if something's not working cycle out."
        # Picky = a 10c/day entry bar (5x the old one) on a $100 book
        # ranked by what actually paid; not-working = measured under that
        # bar for two hours with nothing better at the market.
        # revive up to the full per-market cap (owner, 2026-08-21: "we
        # have to be able to qualify markets that could be winners") —
        # and with negative-risk netting, qualifying several brackets of
        # one race barely moves the ceiling
        capital_usd=100.0, per_market_usd=20.0, revive_max_usd=20.0,
        share_hi=0.10,
        # owner, 2026-08-21: "I would do 30 seconds under 75 cents, but
        # just for politics. There are so many options you can find
        # something better." One bar for entry and culling — nothing
        # places under 75c/day, and two consecutive under-bar readings
        # (the loop runs every 60s) pull the order for the next best spot.
        min_est_day=0.75, weak_pull_s=30.0,
        # owner, 2026-08-21: "it's okay to get filled at reasonable
        # prices" — two ticks of edge earns the touch, four lifts the
        # courtesy share toward 35%; the drift alarm moves above that so
        # the two don't fight
        join_edge_ticks=2.0, share_max=0.35, drift_share=0.45,
        # and fresh money goes ONLY where the fill-and-reward record is
        # deepest: governor and senate races (winners, margins, primaries,
        # seat ladders) and the 2028 presidential slate
        enter_tokens=("usgub", "usse", "senate", "uspres", "usp-2028"),
        rest_from=None, rest_until=None,      # politics rests every day
        min_days_out=3,
        books_per_cycle=36, scan_reserve=8,
        book_stale_s=300.0, read_age_s=900.0,
        max_actions_per_cycle=10,
        terms_slice=300, terms_full_s=1800.0,
    )
