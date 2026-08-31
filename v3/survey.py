"""Read-only survey: where could a cent of risk hold a real share?

The thing that makes college football work is not a fat reward pool. It
is that a qualifying wall parked up at 99c carries the side over Target
Size while the touch itself holds single digits of shares — so an order
of FORTY-ONE CENTS takes 13% of the side's score. NBA's pools are 2.3x
richer and pay 17x less, because its touch holds hundreds of thousands
of contracts and our share is 0.02%.

So the question this asks of a market is never "how big is the pool".
It is: how much rests near the touch, and what would our own small size
be worth against it (owner, 2026-08-31: "We're getting a high share with
low order size (risk). So that wouldn't quite be an apples to apples
comparison").

Pure arithmetic on a book and a program row — no IO, no orders.
"""

from __future__ import annotations

import datetime as dt
import random
from dataclasses import dataclass, field

from .scoring import estimate_join

# Owner, 2026-08-31: "we'll probably want to stay out of live events
# until I have a way of quoting them better." A market whose game has
# started prices off play, not off a line — and the buffer keeps us out
# of the hour before the whistle too, when the book turns over as the
# lines firm up. Re-checked on every pass, because a market that was
# quiet this morning goes live at kickoff.
LIVE_BUFFER_S = 3600.0


def _epoch(v) -> float | None:
    """The exchange sends times as ISO strings; some feeds send epochs."""
    if v is None or v == "":
        return None
    if isinstance(v, (int, float)):
        f = float(v)
        return f / 1000.0 if f > 1e11 else f     # milliseconds or seconds
    try:
        s = str(v).replace("Z", "+00:00")
        return dt.datetime.fromisoformat(s).timestamp()
    except (TypeError, ValueError):
        return None


def is_live_event(market: dict, now: float,
                  buffer_s: float = LIVE_BUFFER_S) -> bool:
    """Is this market's event under way, or about to be?

    A market with no gameStartTime has no in-play phase — a futures or
    politics market trades the same way all day — so it is never live.
    """
    if not isinstance(market, dict):
        return False
    start = _epoch(market.get("gameStartTime"))
    if start is None:
        return False
    return now >= start - buffer_s

# how far from the touch still carries real scoring weight. Past this the
# discount factor has usually crushed a level's contribution to nothing.
NEAR_TICKS = 3

# the order we would actually place. cfb's real orders are a fraction of
# a share to two shares, median 41c at risk — so that, not an invented
# round number, is what the survey prices (owner, 2026-08-31).
PROBE_QTY = 1.0


def kind_of(slug: str) -> str:
    """The market KIND, so a survey can report what sorts of market a
    tag actually holds. Slugs run <kind>-<date>-<who>, e.g.
    aachc-cfb-wins-2026-11-28-txst-5pt5wins, so everything before the
    first four-digit year is the kind."""
    parts = str(slug).split("-")
    out: list[str] = []
    for p in parts:
        if len(p) == 4 and p.isdigit() and 2000 <= int(p) <= 2100:
            break
        out.append(p)
    return "-".join(out) or str(slug)


@dataclass
class SideProbe:
    """What one side of one book would be worth to us."""

    side: str
    touch_px: float | None = None
    touch_size: float = 0.0        # shares resting AT the touch
    near_size: float = 0.0         # within NEAR_TICKS of it
    total_size: float = 0.0        # the whole side, walls included
    target: float = 0.0
    qualifies: bool = False        # cumulative size reaches Target Size
    share: float = 0.0             # what PROBE_QTY at the touch would score
    est_day: float = 0.0           # that share x the side's daily pool
    risk_usd: float = 0.0          # what those shares would cost us
    note: str = ""

    @property
    def share_per_dollar(self) -> float:
        """The measure cfb is exceptional at: share of a side bought per
        dollar put at risk. Ranking on this rather than on pool size is
        the correction that this whole survey exists for."""
        return (self.share / self.risk_usd) if self.risk_usd > 1e-9 else 0.0

    def row(self, slug: str, kind: str) -> dict:
        return {"market": slug, "kind": kind, "side": self.side,
                "touch_px": round(self.touch_px, 4) if self.touch_px else "",
                "touch_size": round(self.touch_size, 2),
                "near_size": round(self.near_size, 2),
                "total_size": round(self.total_size, 2),
                "target": round(self.target, 0),
                "qualifies": int(self.qualifies),
                "share_pct": round(self.share * 100.0, 4),
                "est_day_usd": round(self.est_day, 4),
                "risk_usd": round(self.risk_usd, 4),
                "share_per_dollar": round(self.share_per_dollar, 4),
                "note": self.note}


def probe_side(book, prog, side: str, side_pool: float | None,
               qty: float = PROBE_QTY) -> SideProbe:
    """Score one side of one market for a PROBE_QTY-share join at the
    touch. `prog` is a programs.Program; `side_pool` is what that side
    competes for per day, already divided by the markets in the event
    and by the two sides."""
    p = SideProbe(side=side, target=float(getattr(prog, "target", 0.0) or 0.0))
    levels = [(px, q) for px, q in book.side(side) if q > 1e-9]
    if not levels:
        p.note = "side is empty"
        return p
    p.touch_px = levels[0][0]
    p.touch_size = levels[0][1]
    p.total_size = sum(q for _px, q in levels)
    tick = book.tick or 0.01
    near_lo = p.touch_px - NEAR_TICKS * tick
    near_hi = p.touch_px + NEAR_TICKS * tick
    p.near_size = sum(q for px, q in levels if near_lo - 1e-9 <= px <= near_hi + 1e-9)
    j = estimate_join(side, levels, tick, float(getattr(prog, "df", 0.0) or 0.0),
                      p.target, p.touch_px, qty)
    p.qualifies = bool(j.qualifies)
    p.share = float(j.share) if (j.qualifies and j.in_window) else 0.0
    if side_pool is not None:
        p.est_day = p.share * side_pool
    # what the shares would cost: a bid pays its price, an ask offers
    # stock we would have to hold, valued the same way
    p.risk_usd = qty * p.touch_px
    if not p.qualifies:
        p.note = "side under Target Size — pays nobody"
    elif p.share <= 0.0:
        p.note = "outside the scoring window"
    return p


def summarise(rows: list[dict]) -> dict:
    """A few numbers per kind, so a tag's market types can be compared
    without reading hundreds of rows."""
    by: dict[str, dict] = {}
    for r in rows:
        k = by.setdefault(r["kind"], {"kind": r["kind"], "sides": 0,
                                      "qualified": 0, "shares": [],
                                      "est": 0.0, "spd": []})
        k["sides"] += 1
        k["qualified"] += int(r["qualifies"])
        if r["qualifies"]:
            k["shares"].append(r["share_pct"])
            k["est"] += r["est_day_usd"]
            k["spd"].append(r["share_per_dollar"])
    out = []
    for k in by.values():
        sh = sorted(k["shares"])
        spd = sorted(k["spd"])
        out.append({
            "kind": k["kind"], "sides": k["sides"],
            "qualified": k["qualified"],
            "median_share_pct": round(sh[len(sh) // 2], 3) if sh else 0.0,
            "best_share_pct": round(sh[-1], 3) if sh else 0.0,
            "est_day_usd": round(k["est"], 2),
            "median_share_per_dollar":
                round(spd[len(spd) // 2], 3) if spd else 0.0,
        })
    out.sort(key=lambda r: -r["median_share_per_dollar"])
    return {"kinds": out}


def _median(xs: list[float]) -> float:
    if not xs:
        return 0.0
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2.0


@dataclass
class PrefixStat:
    """A prefix's running evidence. Recent samples only — books change,
    and a prefix that was juicy last month must not sit at the top for
    ever. The window IS the decay."""

    prefix: str
    markets: int = 0            # distinct markets drawn
    sides: int = 0              # sides scored
    qualified: int = 0
    live_skipped: int = 0
    spd: list = field(default_factory=list)
    share: list = field(default_factory=list)
    touch: list = field(default_factory=list)
    est: list = field(default_factory=list)
    last_ts: float = 0.0

    KEEP = 80                   # samples per prefix before the oldest fall out

    def record(self, p: "SideProbe", now: float) -> None:
        self.sides += 1
        self.last_ts = now
        if not p.qualifies:
            return
        self.qualified += 1
        for lst, v in ((self.spd, p.share_per_dollar),
                       (self.share, p.share * 100.0),
                       (self.touch, p.touch_size),
                       (self.est, p.est_day)):
            lst.append(v)
            del lst[:-self.KEEP]

    def row(self) -> dict:
        return {"prefix": self.prefix, "markets": self.markets,
                "sides": self.sides, "qualified": self.qualified,
                "live_skipped": self.live_skipped,
                "n": len(self.spd),
                "median_spd": round(_median(self.spd), 3),
                "median_share_pct": round(_median(self.share), 3),
                "median_touch": round(_median(self.touch), 0),
                "median_est_day": round(_median(self.est), 4),
                "last_ts": round(self.last_ts, 1)}


# Below this many scored sides a prefix's median is noise, so it is not
# ranked at all — it is listed as still sampling. The AFC South market
# (one share at the touch, 14% share) is exactly the single lucky draw
# that would otherwise crown a prefix (owner, 2026-08-31).
MIN_SAMPLES = 12


def leaderboard(stats: dict, min_samples: int = MIN_SAMPLES) -> dict:
    """Ranked on the MEDIAN share per dollar at risk — never the max,
    and never before there is enough evidence to mean anything."""
    rows = [s.row() for s in stats.values()]
    ranked = [r for r in rows if r["n"] >= min_samples]
    young = [r for r in rows if r["n"] < min_samples]
    ranked.sort(key=lambda r: -r["median_spd"])
    young.sort(key=lambda r: -r["n"])
    return {"ranked": ranked, "sampling": young,
            "min_samples": min_samples}


class Sampler:
    """Stratified round-robin over prefixes, uniformly random within
    each one.

    Uniform over MARKETS would be the obvious choice and the wrong one:
    a prefix holding 8,000 markets would swamp the sample while one
    holding 20 went years without a draw, which is the opposite of a
    prefix leaderboard. So every prefix takes its turn, and which of its
    markets represents it is a random draw without replacement until the
    prefix is exhausted, then reshuffled.

    The seed is kept and reported so any run can be reproduced and
    audited — no hand-picking (owner, 2026-08-31: "so that we can
    guarantee that you'd being random with how you are sampling").
    """

    def __init__(self, seed: int = 0):
        self.seed = int(seed)
        self.rng = random.Random(self.seed)
        self.pools: dict[str, list[str]] = {}
        self.all: dict[str, list[str]] = {}
        self.order: list[str] = []
        self.cursor = 0
        self.passes = 0

    def load(self, slugs) -> None:
        """Group the population by prefix. Adding markets later keeps
        the pools that are part-drawn, so a refresh does not restart the
        sampling."""
        for s in slugs:
            k = kind_of(s)
            bucket = self.all.setdefault(k, [])
            if s not in bucket:
                bucket.append(s)
        for k, v in self.all.items():
            if k not in self.pools:
                self.pools[k] = self._shuffled(v)
        self.order = sorted(self.all)

    def _shuffled(self, slugs: list[str]) -> list[str]:
        out = list(slugs)
        self.rng.shuffle(out)
        return out

    def next_batch(self, k: int) -> list[str]:
        """The next k markets to probe: one prefix at a time, round
        robin, so every prefix gains evidence at the same rate."""
        out: list[str] = []
        if not self.order:
            return out
        for _ in range(k * max(len(self.order), 1)):
            if len(out) >= k:
                break
            pref = self.order[self.cursor % len(self.order)]
            self.cursor += 1
            pool = self.pools.get(pref) or []
            if not pool:                      # exhausted — reshuffle it
                pool = self.pools[pref] = self._shuffled(self.all.get(pref, []))
                self.passes += 1
                if not pool:
                    continue
            out.append(pool.pop())
        return out

    def state(self) -> dict:
        return {"seed": self.seed, "prefixes": len(self.all),
                "population": sum(len(v) for v in self.all.values()),
                "left_this_pass": sum(len(v) for v in self.pools.values()),
                "passes": self.passes}


CSV_COLUMNS = ("market", "kind", "side", "touch_px", "touch_size",
               "near_size", "total_size", "target", "qualifies",
               "share_pct", "est_day_usd", "risk_usd", "share_per_dollar",
               "note")


def to_csv(rows: list[dict]) -> str:
    lines = [",".join(CSV_COLUMNS)]
    for r in rows:
        lines.append(",".join(str(r.get(c, "")).replace(",", " ")
                              for c in CSV_COLUMNS))
    return "\n".join(lines) + "\n"
