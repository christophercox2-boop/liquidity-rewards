"""The floor: who is allowed to run automation, decided by files.

Owner, 2026-08-20: "don't shut anything down, just make it so that when I
turn on v3, the other versions will immediately halt before anything v3
related happens."

The handshake, three small JSON files in the shared working directory
(all three processes run in one container):

* 3.0 writes `v3_floor.json` {"want": bool, "ts"} — want is simply its
  master switch. Written immediately on every flip and refreshed every
  cycle.
* 1.0 and 2.0 read it every loop. When want is true they halt every
  automated order-touching loop — their own switches stay untouched —
  and write `v1_halted.json` / `v2_halted.json` {"halted": true, "ts"},
  restamped every loop.
* 3.0 takes NO order-touching action until both acknowledgements read
  halted and fresh. Armed but unacknowledged, it shows "waiting for the
  others to stand down" and waits. So the sequence the owner asked for
  holds: the others stop first, then 3.0 moves.

Failure sides are chosen to avoid double-driving, the one real danger:
a stale or missing acknowledgement keeps 3.0 waiting (a process the
launcher is restarting acks again within a minute); a WANTED floor is
honoured by 1.0/2.0 even if the file has gone stale, because a crashed
3.0 places nothing and resuming 1.0 automation underneath a 3.0 that
comes back would briefly run both. Turning 3.0's master off returns the
floor within one loop everywhere.
"""

from __future__ import annotations

import json
import os
import time

ACK_FRESH_S = 600.0        # 3.0 acts only on acks this fresh
STALE_ALERT_S = 900.0      # 1.0 warns when a wanted floor goes quiet


def _path(env: str, default: str) -> str:
    return os.environ.get(env) or default


def floor_path() -> str:
    return _path("V3_FLOOR_PATH", "v3_floor.json")


def ack_path(who: str) -> str:
    return _path(f"{who.upper()}_ACK_PATH", f"{who}_halted.json")


def _read(path: str) -> dict:
    try:
        with open(path) as f:
            return json.load(f) or {}
    except (OSError, ValueError):
        return {}


def _write(path: str, payload: dict) -> None:
    try:
        tmp = path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(payload, f)
        os.replace(tmp, path)
    except OSError:
        pass               # a read-only disk must never take a loop down


# -- 3.0's side --------------------------------------------------------------

class Floor:
    def __init__(self, clock=None):
        self._clock = clock or time.time

    def write_want(self, want: bool) -> None:
        _write(floor_path(), {"want": bool(want), "ts": round(self._clock(), 1)})

    def acked(self, now: float | None = None) -> bool:
        """Every RUNNING older version has halted, recently enough to act
        on. A retired version (V2_ENABLED=0 — owner, 2026-08-21: kill
        2.0) writes no acknowledgement and is not awaited."""
        now = now if now is not None else self._clock()
        for who in self.required():
            ack = _read(ack_path(who))
            if not ack.get("halted"):
                return False
            if now - float(ack.get("ts") or 0) > ACK_FRESH_S:
                return False
        return True

    @staticmethod
    def required() -> tuple[str, ...]:
        if os.environ.get("V2_ENABLED", "1") == "0":
            return ("v1",)
        return ("v1", "v2")

    def status(self, now: float | None = None) -> dict:
        now = now if now is not None else self._clock()
        out = {"want": bool(_read(floor_path()).get("want")),
               "required": list(self.required())}
        for who in self.required():
            ack = _read(ack_path(who))
            out[who] = {"halted": bool(ack.get("halted")),
                        "age": (round(now - float(ack["ts"]), 1)
                                if ack.get("ts") else None)}
        out["acked"] = self.acked(now)
        return out


# -- 1.0's / 2.0's side ------------------------------------------------------

def wanted(now: float | None = None) -> tuple[bool, float]:
    """(3.0 wants the floor, age of the request in seconds). Honoured
    regardless of age — see the module docstring for why."""
    d = _read(floor_path())
    ts = float(d.get("ts") or 0)
    age = (now if now is not None else time.time()) - ts if ts else float("inf")
    return bool(d.get("want")), age


def ack(who: str, halted: bool, clock=None) -> None:
    _write(ack_path(who), {"halted": bool(halted),
                           "ts": round((clock or time.time)(), 1)})
