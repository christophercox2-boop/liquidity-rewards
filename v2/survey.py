"""Read-only scout for families 2.0 does not trade yet.

The owner asked what else this strategy could work on (2026-08-19:
"sports futures, culture, anything else you think might be good"). This
module answers that with measurements rather than opinion, and it is
strictly read-only: it never imports OrderDesk and never touches an
order endpoint.

WHY THE DISCOUNT FACTOR LEADS EVERY RANKING. Every program 2.0 trades
today runs df 0.1-0.25, so an order one tick off the touch keeps only
10-25% of its score. That pins us to the touch, which is exactly where
fill risk lives. Polymarket's own docs name MLB futures at df 0.90,
where one tick back keeps 90% and three ticks keeps 73% — the same
earnings from a price a taker is unlikely to ever reach. So the headline
number here is not the pool: it is `safe_day`, what a standard stake
would earn resting THREE TICKS BACK from the touch. That is the money
this strategy can collect without standing in traffic.

Every number comes from the same scoring code the engine uses, so a
survey row is directly comparable to a live one.
"""

from __future__ import annotations

import datetime as dt
import time

from .api import ApiError, Client
from .programs import (
    daily_side_pool, is_econ, pick_period, program_from_period, slug_event_date,
    with_event_n,
)
from .scoring import estimate_join

# Families worth measuring, each with the tag names the exchange might
# use and a search phrase for when none of them resolve. Econ is absent
# on purpose and is filtered again below (standing owner rule).
FAMILIES: tuple[tuple[str, tuple[str, ...], str], ...] = (
    ("Baseball futures", ("mlb", "baseball", "mlb-futures"), "MLB"),
    ("Basketball futures", ("nba", "basketball", "nba-futures"), "NBA"),
    ("Football futures", ("nfl", "football", "nfl-futures"), "NFL"),
    ("Hockey futures", ("nhl", "hockey"), "NHL"),
    ("Soccer futures", ("soccer", "epl", "premier-league", "champions-league"), "soccer"),
    ("Awards & culture", ("awards", "oscars", "emmys", "grammys", "culture",
                          "entertainment"), "awards"),
    ("Science & space", ("science", "space", "tech", "technology"), "space"),
    ("Climate & weather", ("climate", "weather"), "climate"),
)

STAKE_USD = 25.0        # the standard stake every row is measured at
BACK_TICKS = 3          # "safe" means this far behind the touch
MIN_DAYS_OUT = 14       # anything settling sooner is not a resting market
CATALOGUE_TTL_S = 12 * 3600.0
BOOKS_PER_PASS = 6      # gentle: the box is small and shares its rate limit


def _rows_from_events(events: list[dict]) -> tuple[dict[str, int], dict[str, str]]:
    """slug -> markets in its event, and slug -> event label."""
    sizes: dict[str, int] = {}
    labels: dict[str, str] = {}
    for ev in events:
        open_mkts = [m for m in ev.get("markets") or []
                     if m.get("slug") and not m.get("closed")]
        title = str(ev.get("title") or ev.get("name") or "")[:80]
        for m in open_mkts:
            s = m["slug"]
            sizes[s] = max(sizes.get(s, 0), len(open_mkts))
            labels[s] = title
    return sizes, labels


def score_row(slug: str, prog, book, event_n: int, now: float,
              stake: float = STAKE_USD) -> dict | None:
    """What a standard stake would earn here, at the touch and resting
    back. Uses the engine's own scoring, so it is comparable to a live
    order. None when the market cannot be scored at all."""
    side_pool = daily_side_pool(prog, slug)
    if not side_pool:
        return None
    out = {"touch_day": 0.0, "safe_day": 0.0, "safe_ticks": None,
           "spread_c": None, "depth_ratio": None}
    best = None
    for side in ("BUY", "SELL"):
        levels = book.side(side)
        if not levels:
            continue
        touch = levels[0][0]
        sign = 1.0 if side == "BUY" else -1.0
        depth = sum(q for _, q in levels)
        for back in range(0, BACK_TICKS + 1):
            px = round(touch - sign * back * book.tick, 3)
            if not (0.001 <= px <= 0.999):
                continue
            cost_ps = px if side == "BUY" else 1.0 - px
            if cost_ps <= 0:
                continue
            qty = round(stake / cost_ps, 2)
            j = estimate_join(side, list(levels), book.tick, prog.df,
                              prog.target, px, qty)
            if not (j.qualifies and j.in_window):
                continue
            day = j.share * side_pool
            if back == 0 and day > out["touch_day"]:
                out["touch_day"] = day
            if day > out["safe_day"] and back >= 1:
                out["safe_day"], out["safe_ticks"] = day, back
            if best is None or day > best:
                best = day
        if prog.target:
            r = depth / prog.target
            out["depth_ratio"] = min(r, out["depth_ratio"]) if out["depth_ratio"] else r
    if book.bids and book.asks:
        out["spread_c"] = round((book.asks[0][0] - book.bids[0][0]) * 100, 1)
    d = slug_event_date(slug)
    out.update({
        "market": slug, "pool": prog.pool, "target": prog.target, "df": prog.df,
        "event_n": event_n, "side_pool": round(side_pool, 3),
        "touch_day": round(out["touch_day"], 3),
        "safe_day": round(out["safe_day"], 3),
        "resolves": str(d) if d else None,
        "days_out": (d - dt.date.fromtimestamp(now)).days if d else None,
    })
    return out


class Survey:
    """Catalogue + measurements, refreshed slowly and read-only."""

    def __init__(self, clock=None):
        self._clock = clock or time.time
        self.catalogue: dict[str, dict] = {}   # slug -> {family,label,event_n}
        self.rows: dict[str, dict] = {}        # slug -> scored row
        self.catalogue_at = 0.0
        self.note = ""
        self.cursor = 0

    # -- stage 1: what exists -------------------------------------------------

    def refresh_catalogue(self, client: Client, now: float | None = None) -> bool:
        now = now if now is not None else self._clock()
        if self.catalogue and now - self.catalogue_at < CATALOGUE_TTL_S:
            return False
        found: dict[str, dict] = {}
        problems = []
        for label, tags, query in FAMILIES:
            events: list[dict] = []
            for tag in tags:
                try:
                    events.extend(client.events_by_tag(tag, max_pages=5))
                except ApiError as e:
                    problems.append(f"{tag}: {e}"[:60])
            if not events:
                continue
            sizes, labels = _rows_from_events(events)
            for s, n in sizes.items():
                if is_econ(s):
                    continue          # standing owner rule, never traded
                found[s] = {"family": label, "event": labels.get(s, ""),
                            "event_n": n}
        self.catalogue = found
        self.catalogue_at = now
        self.note = "; ".join(problems[:3])
        return True

    # -- stage 2: what it pays ------------------------------------------------

    def measure(self, client: Client, now: float | None = None,
                budget: int = BOOKS_PER_PASS) -> int:
        """Price a few catalogue entries per pass. Round-robin so the
        whole catalogue fills in over time without ever spiking the rate
        limit the box shares with 1.0."""
        now = now if now is not None else self._clock()
        slugs = sorted(self.catalogue)
        if not slugs:
            return 0
        picked, i, seen = [], self.cursor, 0
        while len(picked) < budget and seen < len(slugs):
            s = slugs[i % len(slugs)]
            i, seen = i + 1, seen + 1
            row = self.rows.get(s)
            if row and now - row.get("at", 0) < CATALOGUE_TTL_S:
                continue
            picked.append(s)
        self.cursor = i
        if not picked:
            return 0
        try:
            raw = client.programs(picked)
        except ApiError as e:
            self.note = f"programs: {e}"[:80]
            return 0
        done = 0
        for s in picked:
            tp = pick_period((raw.get(s) or {}).get("timePeriods") or [], s)
            prog = (with_event_n(program_from_period(tp),
                                 max(self.catalogue[s]["event_n"], 1))
                    if tp is not None else None)
            if prog is None or not prog.is_live() or not prog.pool:
                self.rows[s] = {"market": s, "at": now, "skip": "no live pool",
                                **self.catalogue[s]}
                continue
            try:
                book = client.book(s, fetched_at=now)
            except ApiError:
                continue
            row = score_row(s, prog, book, self.catalogue[s]["event_n"], now)
            if row is None:
                self.rows[s] = {"market": s, "at": now, "skip": "unscorable",
                                **self.catalogue[s]}
                continue
            row.update(self.catalogue[s])
            row["at"] = now
            self.rows[s] = row
            done += 1
        return done

    # -- what the page reads --------------------------------------------------

    def ranked(self, limit: int = 40) -> list[dict]:
        """Best first by safe_day: what a standard stake earns resting
        BACK from the touch, which is the earning this strategy can take
        without standing in front of the flow."""
        live = [r for r in self.rows.values()
                if not r.get("skip") and (r.get("days_out") is None
                                          or r["days_out"] >= MIN_DAYS_OUT)]
        live.sort(key=lambda r: -(r.get("safe_day") or 0))
        return live[:limit]

    def by_family(self) -> list[dict]:
        fams: dict[str, dict] = {}
        for r in self.rows.values():
            f = fams.setdefault(r.get("family", "?"),
                                {"family": r.get("family", "?"), "markets": 0,
                                 "priced": 0, "safe_day": 0.0, "best_df": 0.0})
            f["markets"] += 1
            if not r.get("skip"):
                f["priced"] += 1
                f["safe_day"] += r.get("safe_day") or 0
                f["best_df"] = max(f["best_df"], r.get("df") or 0)
        for f in fams.values():
            f["safe_day"] = round(f["safe_day"], 2)
        return sorted(fams.values(), key=lambda f: -f["safe_day"])

    def status(self, now: float | None = None) -> dict:
        now = now if now is not None else self._clock()
        priced = sum(1 for r in self.rows.values() if not r.get("skip"))
        return {"catalogue": len(self.catalogue), "measured": len(self.rows),
                "priced": priced, "stake": STAKE_USD, "back_ticks": BACK_TICKS,
                "age_h": (round((now - self.catalogue_at) / 3600, 1)
                          if self.catalogue_at else None),
                "note": self.note}

    def to_dict(self) -> dict:
        return {"catalogue": self.catalogue, "rows": self.rows,
                "catalogue_at": self.catalogue_at, "cursor": self.cursor,
                "note": self.note}

    @classmethod
    def from_dict(cls, d: dict, clock=None) -> "Survey":
        s = cls(clock=clock)
        s.catalogue = dict(d.get("catalogue") or {})
        s.rows = dict(d.get("rows") or {})
        s.catalogue_at = float(d.get("catalogue_at") or 0.0)
        s.cursor = int(d.get("cursor") or 0)
        s.note = str(d.get("note") or "")
        return s
