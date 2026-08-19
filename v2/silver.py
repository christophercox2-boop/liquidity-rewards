"""Fair values for the Senate seat ladder from the Silver forecast.

The owner wants the Silver model involved because it updates with
polling. 1.0 used the per-race tables only for individual races; the
seat-count ladder was priced off the market's own books, which is
circular. This module derives model-implied rung values instead.

**Races are NOT independent** (owner's correction, 2026-08-19 — the
first version treated them as independent coins, which made the peak
too tall and the tails absurdly thin; a polling error moves every race
the same direction). The model here is a one-factor probit copula —
the standard election-model construction:

    every race keeps EXACTLY Silver's win probability as its marginal;
    a shared national swing S ~ N(0,1) moves them together, with
    latent correlation SWING_RHO between any two races:

        P(GOP wins race i | S) = PHI((PHI^-1(p_i) - sqrt(rho) S)
                                     / sqrt(1 - rho))

    P(GOP seats = K) = holdovers + the exact Poisson-binomial of those
    conditional probabilities, averaged over the swing (numerical
    quadrature, no simulation).

rho = 0 recovers independence; rho = 1 is perfect uniform swing.
SWING_RHO below is an explicit, visible parameter — shown on the page,
not buried — defaulting to the neighborhood polling-error studies put
state-level error correlation in. The distribution's mean equals
holdovers + sum of Silver's probabilities regardless of rho (the copula
preserves marginals); rho only reshapes the spread.

House ladder: no per-district source survives in this repo (the House
model died with Actions), so house rungs get no model fair and the
engine treats them as low-confidence.
"""

from __future__ import annotations

import csv
import io
import math
import time
from pathlib import Path
from statistics import NormalDist

_N = NormalDist()

# Latent correlation between any two races via the shared swing. Its true
# value is genuinely uncertain, and pretending otherwise would just move
# the overconfidence from one place to another — so the model carries a
# RANGE. The ladder is computed at rho 0.2 and 0.6 (the neighborhood
# polling-error studies span) and each rung's fair is an interval: where
# it barely moves across that range the model is confident; where it
# swings the model says so and the engine scouts instead of sizing.
# (Checked against the market on 2026-08-19: its ladder sits between the
# two ends nearly everywhere — the range brackets reality.)
SWING_RHO_LOW = 0.2
SWING_RHO_MID = 0.35   # central curve for display and control estimates
SWING_RHO_HIGH = 0.6
_SWING_NODES = 41      # quadrature nodes over the swing (-4..4 sigma)

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


def _poisson_binomial(probs: list[float]) -> list[float]:
    """Exact distribution of the number of wins among independent races —
    the standard DP, used per swing node (races ARE independent once the
    shared swing is conditioned on)."""
    dist = [1.0]
    for p in probs:
        p = min(max(p, 0.0), 1.0)
        nxt = [0.0] * (len(dist) + 1)
        for k, m in enumerate(dist):
            nxt[k] += m * (1.0 - p)
            nxt[k + 1] += m * p
        dist = nxt
    return dist


def seat_pmf(rep_probs: list[float], not_up: int = SENATE_GOP_NOT_UP,
             rho: float = SWING_RHO_MID) -> dict[int, float]:
    """P(total GOP seats = K) under the one-factor copula: mix the exact
    conditional Poisson-binomial over the national swing. rho=0 is the
    old independent model; marginals match Silver's odds at every rho."""
    if rho <= 0.0:
        dist = _poisson_binomial(rep_probs)
        return {not_up + k: m for k, m in enumerate(dist)}
    rho = min(rho, 0.999)
    x = [_N.inv_cdf(min(max(p, 1e-9), 1 - 1e-9)) for p in rep_probs]
    sq_r, sq_1r = math.sqrt(rho), math.sqrt(1.0 - rho)
    nodes = [-4.0 + 8.0 * i / (_SWING_NODES - 1) for i in range(_SWING_NODES)]
    weights = [math.exp(-s * s / 2.0) for s in nodes]
    wsum = sum(weights)
    mixed = [0.0] * (len(rep_probs) + 1)
    for s, w in zip(nodes, weights):
        cond = [_N.cdf((xi - sq_r * s) / sq_1r) for xi in x]
        dist = _poisson_binomial(cond)
        for k, m in enumerate(dist):
            mixed[k] += m * w / wsum
    return {not_up + k: m for k, m in enumerate(mixed)}


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
        self.pmf: dict[int, float] = {}       # central curve (SWING_RHO_MID)
        self.pmf_lo: dict[int, float] = {}    # rho = SWING_RHO_LOW
        self.pmf_hi: dict[int, float] = {}    # rho = SWING_RHO_HIGH
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
        probs = [r["rep"] for r in races.values()]
        self.pmf = seat_pmf(probs, rho=SWING_RHO_MID)
        self.pmf_lo = seat_pmf(probs, rho=SWING_RHO_LOW)
        self.pmf_hi = seat_pmf(probs, rho=SWING_RHO_HIGH)
        self.fetched_at = now
        return True

    def age(self, now: float | None = None) -> float:
        return (now if now is not None else self._clock()) - self.fetched_at \
            if self.fetched_at else float("inf")

    def fair_range(self, slug: str) -> tuple[float, float] | None:
        """The model's own interval for a rung across the swing-correlation
        range — its honest uncertainty, not a point estimate. None for
        anything this model cannot price (house rungs included)."""
        if not self.pmf or not slug.startswith("scc-senate-gop-"):
            return None
        r = slug_rung(slug)
        vals = [v for pmf in (self.pmf_lo, self.pmf, self.pmf_hi)
                if (v := rung_fair(pmf, r)) is not None]
        if not vals:
            return None
        return min(vals), max(vals)

    def fair(self, slug: str) -> float | None:
        """The central-curve value — display only; the engine uses the range."""
        if not self.pmf or not slug.startswith("scc-senate-gop-"):
            return None
        return rung_fair(self.pmf, slug_rung(slug))

    def gop_control(self) -> float | None:
        """Implied P(GOP >= 50 seats), central curve — the cross-check
        against the market ladder sum; a gross disagreement means the
        holdover constant or the table is wrong."""
        if not self.pmf:
            return None
        return sum(v for k, v in self.pmf.items() if k >= 50)
