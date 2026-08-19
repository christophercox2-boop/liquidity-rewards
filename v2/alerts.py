"""Phone alerts through ntfy, with the discipline 1.0 arrived at.

The topic name is the password — it lives only in the NTFY_TOPIC env
var, never in code or logs. The rules, each one bought with a noisy
night or a missed money event:

* Dedupe: the same title+message inside the repeat window is held.
  "Never sent" is absence, not timestamp zero.
* A global floor between ANY two pushes, because a message carrying a
  changing number defeats dedupe entirely.
* An always-through list for things that must not wait: fills, money
  in, reward-terms changes, the monitor failing, cancel-all. (1.0 left
  "rewards paid" off this list, so money-in queued behind the floor
  while fills did not — fixed here.)
* Nothing disappears silently: whatever was held back is named on the
  next push that gets through.
* Every decision — sent or suppressed, with the reason — is logged, so
  the source of a noise problem is findable from the log alone.
"""

from __future__ import annotations

import os
import time

import requests

REPEAT_WINDOW_S = 1800.0    # identical alert held this long
GLOBAL_FLOOR_S = 300.0      # minimum gap between any two pushes
LOG_KEEP = 200

# Case-insensitive substrings of the TITLE that skip the global floor
# (still deduped). Keep this list short — everything on it can page the
# owner's phone at any hour.
ALWAYS_THROUGH = (
    "order filled", "orders filled", "rewards paid", "rewards posted",
    "reward pool", "changed terms", "pools changed", "program gone",
    "monitor failing", "cancel all sent", "two orders",
)


class Alerts:
    def __init__(self, topic: str | None = None, server: str | None = None,
                 post=None, clock=None):
        self.topic = topic if topic is not None else os.environ.get("NTFY_TOPIC", "")
        self.server = (server or os.environ.get("NTFY_SERVER", "https://ntfy.sh")).rstrip("/")
        self._post = post if post is not None else self._http_post
        self._clock = clock or time.time
        self._seen: dict[str, float] = {}     # title|message -> last sent
        self._last_push = None                # ts of the last push of any kind
        self._held: list[str] = []            # titles suppressed since last push
        self.log: list[dict] = []             # every decision, capped

    def _http_post(self, title: str, message: str, priority: str) -> None:
        if not self.topic:
            return
        try:
            requests.post(f"{self.server}/{self.topic}", data=message.encode(),
                          headers={"Title": title, "Priority": priority}, timeout=10)
        except Exception:  # alerting must never take the monitor down
            pass

    def _log(self, title: str, message: str, sent: bool, why: str) -> None:
        self.log.append({"ts": round(self._clock(), 1), "title": title,
                         "msg": message[:200], "sent": sent, "why": why})
        del self.log[:-LOG_KEEP]

    def notify(self, title: str, message: str, priority: str = "default") -> bool:
        """Send or suppress. Returns whether it went out."""
        now = self._clock()
        key = f"{title}|{message}"
        last = self._seen.get(key)
        if last is not None and now - last < REPEAT_WINDOW_S:
            self._held.append(title)
            self._log(title, message, False, "same alert again")
            return False
        always = any(t in title.lower() for t in ALWAYS_THROUGH)
        if (not always and self._last_push is not None
                and now - self._last_push < GLOBAL_FLOOR_S):
            self._held.append(title)
            self._log(title, message, False, "under the 5-minute floor")
            return False
        if self._held:
            names = ", ".join(dict.fromkeys(self._held[-5:]))
            message = f"{message} (+{len(self._held)} held back: {names})"
            self._held = []
        self._seen[key] = now
        self._last_push = now
        # garbage-collect old dedupe keys
        cutoff = now - 4 * REPEAT_WINDOW_S
        self._seen = {k: t for k, t in self._seen.items() if t >= cutoff}
        self._post(title, message, priority)
        self._log(title, message, True, "")
        return True
