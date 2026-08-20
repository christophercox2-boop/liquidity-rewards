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
        for ev in client.events_by_tag(tag):
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
        capital_usd=100.0, per_market_usd=2.0, revive_max_usd=5.0,
        share_hi=0.10,
        rest_from=None, rest_until=None,      # politics rests every day
        min_days_out=3,
        books_per_cycle=16, scan_reserve=6,
        max_actions_per_cycle=6,
    )
