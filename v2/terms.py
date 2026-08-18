"""Reward terms as first-class, tracked data.

1.0's most expensive information failure: it recorded only "does this
market have a program, yes/no", never the terms. When the exchange cut
the standard pool from ~$500 to ~$200 per event, nothing noticed and the
day's income halved with no explanation available from the code. Its
late fix then split into two readers that never talked to each other:
the scoring cache kept serving stale pools while the change-watcher
(which also silently skipped whole families, senate seats included)
couldn't write back.

2.0 has ONE store. The estimator, the engine, and the change alerts all
read the same object; there is nothing else to go stale against. Every
change to a market's pool, Target Size, discount factor, event divisor
or program is a change event — alerted, and appended to a history sink
so "what were the terms on the 14th?" is answerable forever. The first
sighting of a market seeds silently (there is nothing to compare
against) but is stamped, so "tracking started here" is explicit.
"""

from __future__ import annotations

import time
from dataclasses import dataclass

from .programs import Program, pick_period, program_from_period, with_event_n


@dataclass(frozen=True)
class TermsChange:
    slug: str
    field: str        # pool / target / df / pid / status / event_n / program_gone / program_new
    old: object
    new: object

    def __str__(self) -> str:
        return f"{self.slug}: {self.field} {self.old} -> {self.new}"


# Fields whose change is worth an alert, in the order they are reported.
_WATCHED = ("pool", "target", "df", "pid", "status")


class TermsStore:
    """Current terms per market plus change detection.

    `history_sink` is called with one dict per recorded row (seed rows
    included) — the caller decides where rows go (a JSONL file committed
    to the repo). `refresh` takes RAW incentives programs (from
    api.Client.programs) plus the event-size map from discovery; picking
    the paying period — spill filtering included — happens here, in one
    place, every time."""

    def __init__(self, history_sink=None):
        self.current: dict[str, Program] = {}
        self.updated_at: dict[str, float] = {}
        self.seeded_at: dict[str, float] = {}
        self._sink = history_sink or (lambda row: None)

    def get(self, slug: str) -> Program | None:
        return self.current.get(slug)

    def age(self, slug: str, now: float | None = None) -> float:
        """Seconds since this market's terms were last confirmed. Markets
        never seen return infinity — unknown terms are infinitely stale."""
        ts = self.updated_at.get(slug)
        return (now or time.time()) - ts if ts else float("inf")

    def refresh(self, raw_programs: dict[str, dict], event_sizes: dict[str, int],
                now: float | None = None) -> list[TermsChange]:
        """Fold a fresh incentives read into the store. Returns the change
        events (empty on a pure seed). A market present in raw_programs
        whose periods yield no paying program records program_gone —
        that is the single largest thing that can happen to its income."""
        now = now or time.time()
        changes: list[TermsChange] = []
        for slug, raw in raw_programs.items():
            tp = pick_period(raw.get("timePeriods") or [], slug)
            new = (with_event_n(program_from_period(tp),
                                max(event_sizes.get(slug, 1), 1))
                   if tp is not None else None)
            old = self.current.get(slug)
            if new is None:
                if old is not None:
                    changes.append(TermsChange(slug, "program_gone", old.pid, None))
                    del self.current[slug]
                    self._record(slug, None, now, "gone")
                continue
            self.updated_at[slug] = now
            if old is None:
                first_ever = slug not in self.seeded_at
                self.current[slug] = new
                if first_ever:
                    self.seeded_at[slug] = now
                    self._record(slug, new, now, "seed")
                else:  # was gone, came back
                    changes.append(TermsChange(slug, "program_new", None, new.pid))
                    self._record(slug, new, now, "new")
                continue
            diffs = [f for f in _WATCHED if getattr(old, f) != getattr(new, f)]
            if old.event_n != new.event_n:
                diffs.append("event_n")
            if diffs:
                for f in diffs:
                    changes.append(TermsChange(slug, f, getattr(old, f), getattr(new, f)))
                self._record(slug, new, now, "change")
            self.current[slug] = new
        return changes

    def _record(self, slug: str, prog: Program | None, now: float, why: str) -> None:
        row = {"ts": round(now, 1), "slug": slug, "why": why}
        if prog is not None:
            row.update(pool=prog.pool, target=prog.target, df=prog.df,
                       pid=prog.pid, status=prog.status, event_n=prog.event_n)
        self._sink(row)

    # -- persistence -----------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "current": {s: [p.pool, p.target, p.df, p.status, p.pid, p.tier,
                            p.start, p.end, p.event_n, p.pool_n]
                        for s, p in self.current.items()},
            "updated_at": self.updated_at,
            "seeded_at": self.seeded_at,
        }

    @classmethod
    def from_dict(cls, d: dict, history_sink=None) -> "TermsStore":
        st = cls(history_sink=history_sink)
        for s, v in (d.get("current") or {}).items():
            st.current[s] = Program(pool=v[0], target=v[1], df=v[2], status=v[3],
                                    pid=v[4], tier=v[5], start=v[6], end=v[7],
                                    event_n=v[8], pool_n=v[9])
        st.updated_at = dict(d.get("updated_at") or {})
        st.seeded_at = dict(d.get("seeded_at") or {})
        return st
