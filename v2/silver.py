"""Fair values for the Senate seat ladder from the Silver forecast.

The owner wants the Silver model involved because it updates with
polling. 1.0 used the per-race tables only for individual races; the
seat-count ladder was priced off the market's own books, which is
circular. This module derives real model-implied rung values instead:

    P(GOP seats = K) = holdover seats + Poisson-binomial over the
                       per-race GOP win probabilities

i.e. every race is a coin with Silver's weight, the distribution over
the number of heads is computed exactly (no simulation), and each
ladder rung reads straight off it: an exact-count rung is the pmf at K,
gteN / lteN are tail sums.

Independence between races is an assumption the true model does not
make (a polling error moves many races together), so the distribution
here is too NARROW: tails are understated. The band the engine builds
around these fairs must stay wide enough to cover that — this module
reports fair values, not certainty.

House ladder: no per-district source survives in this repo (the House
model died with Actions), so house rungs get no model fair and the
engine treats them as low-confidence.
"""

from __future__ import annotations

import csv
import io
import time
from pathlib import Path

SENATE_URL = "https://static.dwcdn.net/data/kNspD.csv"
SENATE_FALLBACK = Path(__file__).resolve().parent.parent / "data" / "silver_senate_races.csv"
TTL_S = 6 * 3600.0

# GOP seats NOT up in 2026 = 53 currently held minus the 22 GOP-held
# seats on the ballot (20 of Class II: AL AK AR IA ID KS KY LA ME MS MT
# NC NE OK SC SD TN TX WV WY, plus the OH and FL specials). The Silver
# table carries all 35 races (those 22 plus 13 Dem-held Class II). If
# this constant is wrong the whole ladder shifts sideways by the same
# amount — which is why the engine cross-checks the implied
# P(GOP >= 50) against the market's own ladder sum and flags a gross
# disagreement instead of trading on it.
SENATE_GOP_NOT_UP = 31
SENATE_RACES_EXPECTED = 35


def parse_races(text: str) -> dict[str, dict]:
    """Datawrapper race table -> {abbr: {dem, rep, name}} as fractions.
    Same parse as 1.0's, so both read the same table the same way."""
    out: dict[str, dict] = {}
    for row in csv.DictReader(io.StringIO(text)):
        abbr = (row.get("abbr") or "").strip().lower()
        if not abbr:
            continue
        try:
            dem = float(row.get("winner_Dparty") or "") / 100.0
            rep = float(row.get("winner_Rparty") or "") / 100.0
        except ValueError:
            continue
        out[abbr] = {"dem": dem, "rep": rep, "name": (row.get("state") or "").strip()}
    return out


def seat_pmf(rep_probs: list[float], not_up: int = SENATE_GOP_NOT_UP) -> dict[int, float]:
    """Exact Poisson-binomial: P(total GOP seats = K). Standard DP —
    fold each race in, shifting probability mass up by one seat with its
    win probability."""
    dist = [1.0]
    for p in rep_probs:
        p = min(max(p, 0.0), 1.0)
        nxt = [0.0] * (len(dist) + 1)
        for k, m in enumerate(dist):
            nxt[k] += m * (1.0 - p)
            nxt[k + 1] += m * p
        dist = nxt
    return {not_up + k: m for k, m in enumerate(dist)}


def rung_fair(pmf: dict[int, float], rung: str) -> float | None:
    """A ladder rung's model value: '52' -> P(=52), 'gte57' -> P(>=57),
    'lte45' -> P(<=45). None for a rung this pmf cannot price."""
    try:
        if rung.startswith("gte"):
            n = int(rung[3:])
            return sum(v for k, v in pmf.items() if k >= n)
        if rung.startswith("lte"):
            n = int(rung[3:])
            return sum(v for k, v in pmf.items() if k <= n)
        n = int(rung)
        return pmf.get(n, 0.0)
    except ValueError:
        return None


def slug_rung(slug: str) -> str:
    return slug.rsplit("-", 1)[-1]


class SilverFairs:
    """Cached senate-ladder fairs. `refresh` fetches on a slow TTL (call
    it from the engine cycle, never from a web request); `fair` reads
    the cache only and never blocks."""

    def __init__(self, client=None, clock=None):
        self.client = client            # v2.api.Client, for its session/retries
        self._clock = clock or time.time
        self.races: dict[str, dict] = {}
        self.pmf: dict[int, float] = {}
        self.fetched_at = 0.0
        self.source = "none"
        self.note = ""

    def refresh(self, now: float | None = None) -> bool:
        now = now if now is not None else self._clock()
        if self.races and now - self.fetched_at < TTL_S:
            return False
        text = ""
        try:
            if self.client is not None:
                import requests
                r = requests.get(SENATE_URL, timeout=20,
                                 headers={"User-Agent": "liquidity-rewards v2"})
                if r.status_code < 400:
                    text, self.source = r.text, "cdn"
        except Exception as e:  # noqa: BLE001 — fall through to the disk copy
            self.note = f"cdn: {type(e).__name__}"
        if not text:
            try:
                text, self.source = SENATE_FALLBACK.read_text(), "disk"
            except OSError:
                self.note = "no silver table anywhere"
                return False
        return self.load(text, now)

    def load(self, text: str, now: float) -> bool:
        races = parse_races(text)
        if not races:
            self.note = "silver table parsed empty"
            return False
        if len(races) != SENATE_RACES_EXPECTED:
            # a missing race silently shifts the whole ladder — say so
            self.note = f"{len(races)} races, expected {SENATE_RACES_EXPECTED}"
        self.races = races
        self.pmf = seat_pmf([r["rep"] for r in races.values()])
        self.fetched_at = now
        return True

    def age(self, now: float | None = None) -> float:
        return (now if now is not None else self._clock()) - self.fetched_at \
            if self.fetched_at else float("inf")

    def fair(self, slug: str) -> float | None:
        """Model fair for a senate-ladder market, in dollars per share.
        None for anything this model cannot price (house rungs included)."""
        if not self.pmf or not slug.startswith("scc-senate-gop-"):
            return None
        return rung_fair(self.pmf, slug_rung(slug))

    def gop_control(self) -> float | None:
        """Implied P(GOP >= 50 seats) — the engine's cross-check against
        the market ladder sum; a gross disagreement means the holdover
        constant or the table is wrong, and nothing should trade on it."""
        if not self.pmf:
            return None
        return sum(v for k, v in self.pmf.items() if k >= 50)
