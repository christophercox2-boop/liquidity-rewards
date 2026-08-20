"""The football families, migrated from 2.0 so the whole book can live
under one roof when the owner flips the floor.

College keeps its launch behavior on the owner's word ("The collateral is
low, so I wouldn't change anything for now"): it may still price a
minimum-size order in front of a junk wall (`allow_improve`). The NFL —
and every family after it — is behind-the-touch only, per the owner's
2026-08-20 correction, which is the engine default.

Both discover from the exchange's sports event tags, same shape as
politics: names and event divisors come with the feed, so estimates are
never guessed.
"""

from __future__ import annotations

from .family import FamilyConfig
from .names import name_from_market

CFB_PREFIXES = ("aachc-cfb-wins-",)
NFL_PREFIXES = ("tec-nfl-", "aqc-nfl-", "ftsc-nfl-", "fptc-nfl-")


def _feed_discover(tags: tuple[str, ...], prefixes: tuple[str, ...]):
    def discover(client) -> dict[str, dict]:
        out: dict[str, dict] = {}
        order: list[str] = []
        for tag in tags:
            for ev in client.events_by_tag(tag, max_pages=8):
                title = str(ev.get("title") or ev.get("name") or "").strip()
                rows = [m for m in ev.get("markets") or []
                        if m.get("slug") and not m.get("closed")
                        and m["slug"].startswith(prefixes)]
                for m in rows:
                    slug = m["slug"]
                    if slug not in out:
                        order.append(slug)
                    out[slug] = {"event_n": len(rows),
                                 "name": name_from_market(m, title)[:110]}
        groups: dict[str, list[str]] = {}
        for s in order:
            groups.setdefault(s.rsplit("-", 1)[0], []).append(s)
        for s in order:
            g = groups[s.rsplit("-", 1)[0]]
            if len(g) > out[s]["event_n"]:
                out[s]["event_n"] = len(g)
        return out
    return discover


cfb_discover = _feed_discover(("football", "cfb", "college-football"),
                              CFB_PREFIXES)
nfl_discover = _feed_discover(("nfl", "football", "nfl-futures"),
                              NFL_PREFIXES)


def cfb() -> FamilyConfig:
    """Win totals. Week 0 kicks off Saturday 2026-08-29; the weekly
    Thursday-evening-to-Sunday-morning pull starts with that Thursday."""
    return FamilyConfig(
        name="College football", tag="CFB",
        known_ground=False, rest_style="behind", revive=False,
        allow_improve=True,
        capital_usd=150.0, per_market_usd=1.00,
        rest_from=(6, 6), rest_until=(3, 17),      # Sun 06:00 -> Thu 17:00 ET
        season_start=(2026, 8, 27),
        books_per_cycle=12, scan_reserve=6,
        max_actions_per_cycle=6,
    )


def nfl() -> FamilyConfig:
    """NFL futures: awards, title races, playoffs, season stat futures.
    Resting window Tuesday 06:00 -> Thursday 17:00 ET — the NFL plays
    Thursday/Sunday/Monday, so the family is out from Thursday evening
    through Tuesday morning."""
    return FamilyConfig(
        name="NFL futures", tag="NFL",
        known_ground=False, rest_style="behind", revive=False,
        capital_usd=100.0, per_market_usd=1.00,
        rest_from=(1, 6), rest_until=(3, 17),
        season_start=(2026, 8, 20),
        books_per_cycle=10, scan_reserve=4,
        max_actions_per_cycle=6,
    )
