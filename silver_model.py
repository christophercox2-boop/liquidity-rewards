"""Nate Silver's published model numbers, and what they can say about our books.

The source the owner pointed at is Datawrapper chart KQI8W, published by the
silverbulletin workspace and titled "How our Senate forecast has changed over
time". It is a single national time series: one row per day, two columns,
Democrats and Republicans, summing to 100. The chart's own toggles identify it
as the Deluxe model's SENATE WIN PROBABILITY -- so the Democratic column is
P(Democrats control the Senate), not a vote share and not a seat count.

That is a chamber-level number, not a per-race forecast, so it cannot price the
ussewc-/usgubewc- race markets, which is where most of our size lives. There is
simply no state-level figure anywhere in the file.

What it CAN do is anchor the seat-count ladders. Control is a threshold on the
seat count, so a control probability is one exact point on the seat-count CDF:

    Senate: the Vice President is a Republican this cycle, so a 50-50 chamber
            is Republican. Democratic control therefore needs 51+ Democratic
            seats, i.e. 49 or fewer Republican ones.

                P(Dem controls Senate) == P(GOP seats <= 49)

    House:  no tiebreaker, 435 seats, majority is 218.

                P(Dem controls House) == P(Rep seats <= 217)

The scc- markets quote that same distribution, so the model number and the book
can be compared directly at the pivot. A gap there means our resting size in
the ladder is sitting on the wrong side of an outside estimate, which is worth
knowing before it gets filled.

Nothing here places, cancels or reprices anything. It reports.
"""

from __future__ import annotations

import csv
import datetime as dt
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
SERIES_CSV = DATA / "silver_model.csv"

# Republicans hold the Vice Presidency this cycle, so 50 seats is control.
SENATE_GOP_CONTROL_FLOOR = 50
HOUSE_REP_MAJORITY = 218


def load_series(path: Path | str = SERIES_CSV) -> list[tuple[dt.date, float, float]]:
    """Every (date, Democrat %, Republican %) row, oldest first."""
    out: list[tuple[dt.date, float, float]] = []
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            raw = (row.get("modeldate") or "").strip()
            if not raw:
                continue
            day = None
            for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%m/%d/%y"):
                try:
                    day = dt.datetime.strptime(raw, fmt).date()
                    break
                except ValueError:
                    continue
            if day is None:
                continue
            try:
                dem = float(row.get("Democrats") or "")
                rep = float(row.get("Republicans") or "")
            except ValueError:
                continue
            out.append((day, dem, rep))
    out.sort(key=lambda r: r[0])
    return out


def latest(path: Path | str = SERIES_CSV) -> tuple[dt.date, float, float] | None:
    """The most recent row, or None when the file is missing or unusable."""
    try:
        rows = load_series(path)
    except (OSError, csv.Error):
        return None
    return rows[-1] if rows else None


def trend(path: Path | str = SERIES_CSV, days: int = 7) -> float | None:
    """Change in the Democratic number over the last `days` rows, in points."""
    try:
        rows = load_series(path)
    except (OSError, csv.Error):
        return None
    if len(rows) < 2:
        return None
    window = rows[-days:] if len(rows) >= days else rows
    return window[-1][1] - window[0][1]


# --------------------------------------------------------------------------
# turning the ladders into distributions
# --------------------------------------------------------------------------

def _mid(book: dict) -> tuple[float | None, float | None, float | None]:
    """(best bid, best ask, mid) for a normalised book. Any may be None."""
    bids = book.get("bids") or []
    asks = book.get("asks") or []
    bid = max((p for p, q in bids if q > 0), default=None)
    ask = min((p for p, q in asks if q > 0), default=None)
    mid = (bid + ask) / 2 if bid is not None and ask is not None else (bid or ask)
    return bid, ask, mid


def senate_seat_pmf(books: dict[str, dict]) -> dict[str, tuple[float | None, float | None, float | None]]:
    """Per-rung (bid, ask, mid) for the scc-senate-gop exact-seat ladder.

    Keyed by the rung label -- "lte45", "46" ... "56", "gte57" -- so a missing
    rung stays visibly missing instead of being silently treated as zero.
    """
    out = {}
    for slug, book in books.items():
        if "scc-senate-gop" not in slug:
            continue
        rung = slug.rsplit("-", 1)[-1]
        out[rung] = _mid(book)
    return out


def senate_gop_control_prob(pmf: dict[str, tuple]) -> tuple[float | None, float | None, list[str]]:
    """Market-implied P(GOP holds the Senate) as a (bid-sum, ask-sum) bracket.

    Control is >= 50 seats. Returns the bracket plus the rungs that were
    missing from the book, because an incomplete ladder understates the sum
    and the caller has to know that before comparing it to anything.
    """
    wanted, missing = [], []
    for n in range(SENATE_GOP_CONTROL_FLOOR, 57):
        wanted.append(str(n))
    wanted.append("gte57")
    lo = hi = 0.0
    for rung in wanted:
        cell = pmf.get(rung)
        if not cell:
            missing.append(rung)
            continue
        bid, ask, _ = cell
        lo += bid or 0.0
        hi += ask if ask is not None else (bid or 0.0)
    return lo, hi, missing


def house_cdf(books: dict[str, dict]) -> dict[int, tuple[float | None, float | None, float | None]]:
    """Threshold -> (bid, ask, mid) for the scc-hrep-rep gteN ladder.

    Each rung quotes P(Rep seats >= N) outright, so this is already a CDF.
    """
    out = {}
    for slug, book in books.items():
        if "scc-hrep-rep" not in slug:
            continue
        tail = slug.rsplit("-", 1)[-1]
        if not tail.startswith("gte"):
            continue
        try:
            out[int(tail[3:])] = _mid(book)
        except ValueError:
            continue
    return out


def house_rep_majority_prob(cdf: dict[int, tuple]) -> tuple[float | None, str]:
    """Market-implied P(Rep holds the House), interpolated to 218 seats.

    The ladder is quoted in steps of five, so 218 usually falls between two
    rungs and has to be interpolated. The returned note says exactly which
    rungs were used, since an interpolated number is weaker evidence than a
    quoted one and should not be passed off as the same thing.
    """
    pts = sorted((n, m) for n, (_, _, m) in cdf.items() if m is not None)
    if not pts:
        return None, "no house rungs quoted"
    exact = dict(pts)
    if HOUSE_REP_MAJORITY in exact:
        return exact[HOUSE_REP_MAJORITY], f"quoted outright at gte{HOUSE_REP_MAJORITY}"
    below = [(n, m) for n, m in pts if n <= HOUSE_REP_MAJORITY]
    above = [(n, m) for n, m in pts if n >= HOUSE_REP_MAJORITY]
    if not below or not above:
        n, m = (below or above)[-1 if below else 0]
        return m, f"ladder does not straddle 218; nearest rung is gte{n}"
    n0, m0 = below[-1]
    n1, m1 = above[0]
    if n1 == n0:
        return m0, f"quoted at gte{n0}"
    w = (HOUSE_REP_MAJORITY - n0) / (n1 - n0)
    return m0 + w * (m1 - m0), f"interpolated between gte{n0} ({m0:.3f}) and gte{n1} ({m1:.3f})"


def compare(model_dem_pct: float, market_gop_prob: float | None) -> str:
    """One line describing how far the book sits from the model at the pivot."""
    if market_gop_prob is None:
        return "no market number to compare"
    model_gop = 1.0 - model_dem_pct / 100.0
    gap = market_gop_prob - model_gop
    direction = "rich" if gap > 0 else "cheap"
    return (f"model says GOP {model_gop:.1%}, book says {market_gop_prob:.1%} "
            f"-- book is {abs(gap):.1%} {direction}")


# --------------------------------------------------------------------------
# per-race forecasts
# --------------------------------------------------------------------------
#
# Two state-level charts, one per office, sharing a schema:
#
#   kNspD  "Who is favored to win each Senate race?"    -> ussewc-usse-*
#   N13WX  "Who is favored to win each Governor race?"  -> usgubewc-usgub-*
#
# One row per race with each party's win probability as a percentage. Between
# them they cover the two families most of our resting size sits in. The House
# districts and the scc- seat-count ladders still have no per-race counterpart
# and stay unmodelled.

RACES_CSV = DATA / "silver_senate_races.csv"
GOV_RACES_CSV = DATA / "silver_gov_races.csv"

# the Senate file was first pulled under its chart id; keep reading that name
# so an older checkout does not silently produce an empty race table
_LEGACY_SENATE = DATA / "silver_kNspD.csv"


def load_races(path: Path | str = RACES_CSV) -> dict[str, dict]:
    """Two-letter state code -> {'dem': p, 'rep': p, 'state': name, 'rating': r}.

    Probabilities come back as fractions in 0..1, not the percentages the file
    stores, so they can be compared to book prices without a unit slip.
    """
    out: dict[str, dict] = {}
    path = Path(path)
    if not path.exists() and path == Path(RACES_CSV) and _LEGACY_SENATE.exists():
        path = _LEGACY_SENATE
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            abbr = (row.get("abbr") or "").strip().lower()
            if not abbr:
                continue
            try:
                dem = float(row.get("winner_Dparty") or "") / 100.0
                rep = float(row.get("winner_Rparty") or "") / 100.0
            except ValueError:
                continue
            rating = (row.get("rating") or "").strip()
            out[abbr] = {"state": (row.get("state") or "").strip(),
                         "dem": dem, "rep": rep,
                         "rating": float(rating) if rating else None}
    return out


def load_gov_races(path: Path | str = GOV_RACES_CSV) -> dict[str, dict]:
    """Same shape as load_races, for the Governor chart."""
    return load_races(path)


# slug prefix -> which race table answers for it
_OFFICE_PREFIX = {"ussewc-usse-": "senate", "usgubewc-usgub-": "governor"}


def office_of(slug: str) -> str | None:
    """Which race table covers this slug, or None when nothing does."""
    for prefix, office in _OFFICE_PREFIX.items():
        if slug.startswith(prefix):
            return office
    return None


def race_fair(slug: str, races: dict[str, dict],
              gov_races: dict[str, dict] | None = None) -> float | None:
    """Model probability that `slug` resolves YES, or None if unmodelled.

    Senate and Governor slugs resolve against their own table. House districts,
    the scc- seat-count ladders and everything else return None rather than a
    guess -- there is no state-level number for them in this data.
    """
    office = office_of(slug)
    if office is None:
        return None
    table = races if office == "senate" else (gov_races or {})
    parts = slug.split("-")
    if len(parts) < 3:
        return None
    race = table.get(parts[2].lower())
    if not race:
        return None
    if slug.endswith("-dem"):
        return race["dem"]
    if slug.endswith("-rep"):
        return race["rep"]
    return None


def mark_to_model(side: str, price: float, fair: float) -> float:
    """Per-share profit if this resting order filled and the model were right.

    A buy at `price` on something worth `fair` gains fair - price. A sell is
    the mirror. Negative means a fill costs money against the model.
    """
    return (fair - price) if side.upper() == "BUY" else (price - fair)
