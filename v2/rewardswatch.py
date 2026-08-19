"""Watch the earnings endpoint and push the phone the moment rewards post.

The owner asked for this directly (2026-08-19): "make it so it
continually checks for new rewards and sends me a notification
immediately". Polymarket posts a day's rewards in one batch, one to two
days after the day, historically around midnight–1am ET; before this
module the only checks were 1.0's hourly tracker pass and the button.

This polls /v1/incentives/earnings for the last WINDOW_DAYS every
CHECK_S and alerts on any change: a new day appearing, a day's total
growing, or pending money flipping to paid. It never touches git or
rewards.csv — the hourly tracker still owns the committed history — so
this loop cannot restart the app no matter how often it runs.

First run with no saved signature baselines silently: alerting "new
rewards!" about rows that were already days old on the first boot would
be noise. The signature is persisted in v2 state, so a container
restart neither re-alerts nor misses a change that happened while down
(the next check diffs against the saved signature).
"""

from __future__ import annotations

import time

from v2.api import ApiError
from v2.estimator import et_day

CHECK_S = 300.0        # poll cadence — the push lands within ~5 min of posting
WINDOW_DAYS = 8        # rolling window fetched each check; covers late
                       # PENDING->PAID flips (payouts run ~2 days behind)


def _window_start(now: float) -> str:
    return et_day(now - WINDOW_DAYS * 86400.0)


def _signature(rows: list[dict]) -> dict[str, list[int]]:
    """Per-date [row_count, total_cents, paid_cents] — integers so float
    noise can never masquerade as news."""
    sig: dict[str, list[int]] = {}
    for r in rows:
        day = str(r.get("date", ""))[:10]
        if not day:
            continue
        cents = round(float(r.get("reward_usd", 0) or 0) * 100)
        s = sig.setdefault(day, [0, 0, 0])
        s[0] += 1
        s[1] += cents
        if str(r.get("status", "")).upper() == "PAID":
            s[2] += cents
    return sig


class RewardsWatch:
    def __init__(self, clock=None):
        self._clock = clock or time.time
        self.last_check = 0.0
        self.primed = False
        self.sig: dict[str, list[int]] = {}
        self.last_err = ""

    def check(self, client, notify, now: float | None = None) -> bool:
        """One poll if due. Returns whether an alert went out."""
        now = now if now is not None else self._clock()
        if now - self.last_check < CHECK_S:
            return False
        self.last_check = now
        try:
            rows = client.earnings(_window_start(now))
        except ApiError as e:
            self.last_err = str(e)[:200]
            return False
        except Exception as e:  # noqa: BLE001 — a watcher must never kill the cycle
            self.last_err = f"{type(e).__name__}: {e}"[:200]
            return False
        self.last_err = ""
        sig = _signature(rows)
        if not self.primed:
            self.sig = sig
            self.primed = True
            return False
        posted: list[str] = []
        paid: list[str] = []
        for day in sorted(sig):
            new_n, new_cents, new_paid = sig[day]
            old_n, old_cents, old_paid = self.sig.get(day, [0, 0, 0])
            if new_cents > old_cents or new_n > old_n:
                grew = (new_cents - old_cents) / 100.0
                posted.append(
                    f"{day}: ${new_cents / 100.0:,.2f} across {new_n} markets"
                    + (f" (+${grew:,.2f})" if old_n else ""))
            if new_paid > old_paid:
                paid.append(f"{day}: ${(new_paid - old_paid) / 100.0:,.2f} marked paid")
        # a day leaving the window is not news; only growth and flips are
        self.sig = sig
        if not posted and not paid:
            return False
        title = "Rewards paid" if paid else "Rewards posted"
        message = " · ".join(paid + posted)
        return bool(notify(title, message))

    def status(self, now: float | None = None) -> dict:
        """What the page shows: proof the watcher is alive and what it saw."""
        now = now if now is not None else self._clock()
        latest = max(self.sig) if self.sig else ""
        return {
            "checked_ago_s": round(now - self.last_check) if self.last_check else None,
            "latest_day": latest,
            "latest_usd": round(self.sig[latest][1] / 100.0, 2) if latest else None,
            "latest_paid_usd": round(self.sig[latest][2] / 100.0, 2) if latest else None,
            "err": self.last_err,
        }

    def to_dict(self) -> dict:
        return {"last_check": self.last_check, "primed": self.primed,
                "sig": self.sig, "err": self.last_err}

    @classmethod
    def from_dict(cls, d: dict, clock=None) -> "RewardsWatch":
        w = cls(clock=clock)
        w.last_check = float(d.get("last_check") or 0.0)
        w.primed = bool(d.get("primed"))
        w.sig = {str(k): [int(x) for x in v]
                 for k, v in (d.get("sig") or {}).items()}
        w.last_err = str(d.get("err") or "")
        return w
