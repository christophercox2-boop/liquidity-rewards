"""College football win totals — the launch reward family.

The engine lives in v2/family.py (generalized 2026-08-20 when the owner
approved NFL futures); this module keeps the college family's names and its
original behavior: `allow_improve` stays ON here, which is why some college
orders rest alone in front of a junk qualifier wall — the owner saw that,
said the collateral is low so leave it, and asked that every NEWER family
be modeled behind the touch instead (see family.nfl)."""

from __future__ import annotations

from .family import (  # noqa: F401 — re-exported for callers and tests
    ET,
    Family,
    FamilyConfig,
    FamilyOrder,
    PREFIX,
    college,
    slug_days_out,
)
from .family import resting_ok as _resting_ok

CfbFamily = Family
CfbOrder = FamilyOrder
CfbConfig = college          # CfbConfig() -> the college FamilyConfig


def resting_ok(now: float) -> bool:
    """College window (Sunday 06:00 -> Thursday 17:00 ET), one-arg form."""
    return _resting_ok(now, college())
