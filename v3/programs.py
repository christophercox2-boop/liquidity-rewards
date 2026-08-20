"""Reward programs: picking the paying program, normalizing pools to $/day.

Pure functions over the incentives API's data shapes. No network — the
API layer fetches, this module interprets. Ported closely from 1.0's
track_rewards.py, where every rule below was paid for:

* The pool belongs to the EVENT and splits across the event's open
  markets, then across the two sides:

      per side per day = pool / markets in the event / 2

  SETTLED by the 2026-08-15 payout (program-wide division was out by up
  to 34x; per-event landed within 1.1-1.7x and erred low). Do not
  re-open this. `pool_n` (markets sharing a programId) survives only as
  a fallback for a program with no event size at all.

* Since 2026-08-03 the incentives API spills GLOBAL sports programs
  (mlb_futures, march_madness_futures, a $99,999 "live" sentinel) onto
  EVERY market's timePeriods. Picking one inflated a politics estimate
  ~1,000x. Prefer periods whose programId matches the market's own
  family; failing that, anything that isn't a known spill.

* A market whose own programs have all closed has NO paying program —
  scoring a closed program is the phantom-estimate failure.

* ONLY golf pools are pre-tournament budgets divided over a window, and
  even there the measured flow (~$0.03/market/day before play starts)
  overrides the pool-over-window model. Politics pools pay IN FULL
  DAILY regardless of the program's start/end cycle window — actuals
  held at ~$126-135/day across a window boundary.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, replace


def to_num(x) -> float:
    """Best-effort numeric parse: plain numbers, numeric strings, and the
    protobuf-style dict encodings the trading API uses (units/nanos, value)."""
    if x is None:
        return 0.0
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        try:
            return float(x)
        except ValueError:
            return 0.0
    if isinstance(x, dict):
        if "units" in x or "nanos" in x:
            return float(x.get("units", 0) or 0) + float(x.get("nanos", 0) or 0) / 1e9
        for key in ("value", "amount", "px", "price", "qty", "quantity", "decimal"):
            if key in x:
                return to_num(x[key])
    return 0.0


@dataclass(frozen=True)
class Program:
    """One market's paying reward program, normalized."""

    pool: float          # $ for the whole EVENT per pool period (usually a day)
    target: float        # Target Size in contracts, per side
    df: float            # discount factor per tick (usually 0.1-0.5)
    status: str = ""     # raw status string; empty means assumed live
    pid: str = ""        # programId
    tier: str = ""       # low/mid/high for tiered politics programs
    start: str = ""      # ISO timestamps as the API sends them
    end: str = ""
    event_n: int = 1     # open markets in the event sharing the pool
    pool_n: int = 0      # markets sharing the programId — diagnostic/fallback only

    def is_live(self) -> bool:
        s = self.status.lower()
        return not s or s in ("active", "live", "status_live")


# ONLY golf pools are pre-tournament budgets. Other categories — politics
# (validated by reconciliation) and college basketball (documented daily) —
# are daily pools and must never be divided temporally.
PRETOURNAMENT_PREFIXES = ("tec-pga-", "tec-liv-", "tec-golf-")

# Measured, not modeled: paid actuals for pre-tournament golf days came to
# ~1-4c per market per day. Until play starts, a golf market is worth about
# this much per day, whatever its pool says.
GOLF_PRETOURNAMENT_DAILY = 0.03

# Global programs the API spills onto every market regardless of category.
SPILL_PIDS = ("mlb_futures", "mlb_games_ml_live", "march_madness_futures")


def slug_event_date(slug: str | None) -> dt.date | None:
    """The event date embedded in a slug (a YYYY-MM-DD run of parts), or None."""
    parts = (slug or "").split("-")
    for i in range(len(parts) - 2):
        if (parts[i].isdigit() and len(parts[i]) == 4
                and parts[i + 1].isdigit() and parts[i + 2].isdigit()):
            try:
                return dt.date(int(parts[i]), int(parts[i + 1]), int(parts[i + 2][:2]))
            except ValueError:
                return None
    return None


def family_keywords(slug: str | None) -> tuple[str, ...] | None:
    """programId tokens that identify the market's own reward family, or
    None when the family is unknown (fall back to spill filtering only)."""
    s = slug or ""
    if s.startswith(PRETOURNAMENT_PREFIXES):
        return ("pga", "golf", "liv")
    if s.startswith("tec-nba-"):
        return ("nba",)
    if s.startswith("tec-cbb-"):
        return ("cbb", "ncaa", "college", "march")
    if s.startswith("aec-"):
        return ("table", "tennis", "tt", "ping")
    if s.startswith("tec-"):
        return None
    return ("politics",)


def pid_matches(pid, keywords: tuple[str, ...]) -> bool:
    toks = set(str(pid or "").lower().replace("-", "_").split("_"))
    return bool(toks & set(keywords))


def is_spill(tp: dict) -> bool:
    """A global program spilled onto an unrelated market: a live-game pool
    (resting LP orders on a non-live market can't earn from one), the
    $99,999 sentinel, or a known spilled programId."""
    if str(tp.get("period") or "").lower() == "live":
        return True
    if to_num(tp.get("rewardPool")) >= 99998:
        return True
    return str(tp.get("programId") or "") in SPILL_PIDS


def pick_period(periods: list[dict], slug: str = "",
                today: dt.date | None = None) -> dict | None:
    """The time period that pays TODAY, from a market's raw timePeriods.

    Politics markets carry one active tier program. Golf markets carry
    several concurrently-active programs — pretournament plus one per
    round — so pick by where today falls relative to the tournament
    (round 1 = slug event date minus 3, the Thursday). None means no
    paying program on this market.
    """
    active = [tp for tp in (periods or [])
              if str(tp.get("status", "")).upper() in ("LIVE", "ACTIVE", "STATUS_LIVE")
              ] or list(periods or [])
    kw = family_keywords(slug)
    matched = ([tp for tp in active if pid_matches(tp.get("programId"), kw)]
               if kw is not None else [])
    active = matched or [tp for tp in active if not is_spill(tp)]
    if not active:
        return None
    if len(active) > 1:
        ev = slug_event_date(slug)
        if ev:
            if today is None:
                today = dt.datetime.now(dt.timezone.utc).date()
            t_start = ev - dt.timedelta(days=3)
            want = ("pretournament" if today < t_start
                    else f"round_{min((today - t_start).days + 1, 4)}")
            for tp in active:
                if want in str(tp.get("programId") or ""):
                    return tp
    return active[-1]


def program_from_period(tp: dict) -> Program:
    """Normalize one raw time period into a Program (event_n set by caller)."""
    pid = str(tp.get("programId") or "")
    tier = next((t for t in ("low", "mid", "high") if f"_{t}_" in pid), "")
    return Program(
        pool=to_num(tp.get("rewardPool")), target=to_num(tp.get("targetSize")),
        df=to_num(tp.get("discountFactor")), status=str(tp.get("status") or ""),
        pid=pid, tier=tier, start=str(tp.get("start") or ""), end=str(tp.get("end") or ""),
    )


def with_event_n(prog: Program, event_n: int) -> Program:
    return replace(prog, event_n=max(event_n, 1))


def pool_days(prog: Program, slug: str | None = None) -> float:
    """How many days the pool covers. Daily (1.0) for everything except golf
    tournament programs, which fund the pre-tournament window: program start
    to an explicit end date, or ~tournament start (the slug's event date
    minus 3 days). Politics programs report a start/end cycle window too,
    but reconciliation proved those pools pay in FULL daily — the window
    never divides anything outside golf."""
    try:
        if not (slug and slug.startswith(PRETOURNAMENT_PREFIXES)):
            return 1.0
        if "round" in prog.pid:
            return 1.0  # a per-round pool pays over its single round day
        if prog.start and prog.end:
            sd = dt.datetime.fromisoformat(prog.start.replace("Z", "+00:00"))
            ed = dt.datetime.fromisoformat(prog.end.replace("Z", "+00:00"))
            return max((ed - sd).total_seconds() / 86400.0, 1.0)
        if prog.start:
            ev = slug_event_date(slug)
            if ev:
                sd = dt.datetime.fromisoformat(prog.start.replace("Z", "+00:00")).date()
                t_start = ev - dt.timedelta(days=3)  # Sun finish -> ~Thu start
                return float(max((t_start - sd).days, 1))
    except Exception:  # fall back to daily
        pass
    return 1.0


def daily_pool(prog: Program, slug: str | None = None) -> float:
    """Reward pool normalized to $/day for the market's event: pool over its
    covered days, divided across the open markets of the event. EVENT_N,
    not POOL_N — the pool belongs to the event; a programId shared across
    several events does not make it smaller (settled 2026-08-15)."""
    if (slug and slug.startswith(PRETOURNAMENT_PREFIXES) and "round" not in prog.pid):
        return GOLF_PRETOURNAMENT_DAILY
    n = max(prog.event_n or prog.pool_n or 1, 1)
    return (prog.pool or 0.0) / pool_days(prog, slug) / n


def daily_side_pool(prog: Program, slug: str | None = None) -> float:
    """What one side of this market's book competes for per day."""
    return daily_pool(prog, slug) / 2


# ---------------------------------------------------------------------------
# Market scope filters (standing owner instructions)
# ---------------------------------------------------------------------------

# Slug tokens that mark U.S. politics markets. Token-based on purpose:
# substring matching is too loose (tennis player code 'russer' contains
# 'usse').
US_POLITICS_HINTS = ("midterm", "attgen", "housepop")


def is_us_politics(slug: str) -> bool:
    tokens = slug.split("-")
    if {"dem", "rep"} & set(tokens):
        return True
    return any(t.startswith("us") or t.startswith(US_POLITICS_HINTS) or t.endswith("gov")
               for t in tokens)


def is_econ(slug: str) -> bool:
    """Economic-data markets (CPI prints, jobs numbers, Fed decisions...).
    NEVER traded, by standing owner instruction — even though the
    exchange's politics tag includes them."""
    tokens = slug.lower().split("-")
    return any(
        "cpi" in t or "gdp" in t
        or t.startswith(("fomc", "fedfund", "payroll", "nfp", "unemploy",
                         "inflat", "recess", "jobless"))
        for t in tokens
    )
