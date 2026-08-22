"""The NBA futures family (owner, 2026-08-22: "Also add in NBA.").

Discovery is the exchange's events feed under the basketball tags,
filtered to slug prefixes. tec-nba- is measured (the 2026-08 event
survey: conference winners, $1000/day pool). The other three are the
NBA spellings of the NFL family's futures classes — a prefix that
matches nothing costs nothing, and the nba_tags.yml survey will
confirm the full list once the owner restores GitHub Actions minutes.
Deliberately OUT: pntcbk-nba- (single-game player props — game-time
fill risk, not futures), WNBA, and college basketball; the owner
asked for the NBA only.

The config mirrors the NFL's ("similar to cfb" was the owner's word
for that one): $50 all-in with holdings counted at liquidation value,
behind-the-touch resting, the same dump cap.

No resting window yet: the 2026-27 season opens in late October, and
until then there are no game days at all. The NBA then plays nearly
every day, so football's weekly quiet stretch has no equivalent —
the in-season posture is an owner decision to make before opening
night, not a guess to bake in now.
"""

from __future__ import annotations

from .family import FamilyConfig
from .football import _feed_discover

NBA_PREFIXES = ("tec-nba-", "aqc-nba-", "ftsc-nba-", "fptc-nba-")

nba_discover = _feed_discover(("nba", "basketball", "nba-futures"),
                              NBA_PREFIXES)


def nba() -> FamilyConfig:
    return FamilyConfig(
        name="NBA futures", tag="NBA",
        known_ground=False, rest_style="behind", revive=False,
        allow_improve=True,
        capital_usd=50.0, per_market_usd=1.00,
        holdings_in_ceiling=True,
        dump_usd_day=10.0,
        rest_from=None, rest_until=None,     # offseason: no game days yet
        books_per_cycle=20, scan_reserve=8,
        book_stale_s=300.0, read_age_s=900.0,
        max_actions_per_cycle=6,
        probe_usd=3.0, grow_usd=10.0,
        replan_s=900.0,
    )
