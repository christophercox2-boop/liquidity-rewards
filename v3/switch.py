"""The master switch — ONE switch for everything that places orders.

The properties that must hold (owner's standing rules, updated by his
2026-08-18 decisions):

* OFF means nothing places. The OrderDesk checks this switch on every
  automated placement; there is no second switch to argue with it.
* Turning ON takes two deliberate taps — arm, then confirm inside the
  window. Turning OFF takes one. Stopping is always easier than
  starting.
* Every flip is logged with a timestamp and pushed to the phone.
* The state PERSISTS across deploys (owner's decision — off-by-default
  after deploys was rejected). The guard instead: when a new build
  boots with the switch on, the owner gets one push saying so.
* It lives on its own page (/v3/switch), never on a status page.
"""

from __future__ import annotations

import time

ARM_WINDOW_S = 120.0


class MasterSwitch:
    def __init__(self, alert=None, clock=None, name: str = "Master switch",
                 scope: str = "3.0"):
        self.on = False
        self.armed_at = 0.0
        self.log: list[dict] = []
        self.alert = alert or (lambda title, msg: None)
        self._clock = clock or time.time
        # one class, many loops: each family gets its own instance with its
        # own name, so a flip's push says WHICH switch moved (the owner's
        # per-loop switch rule)
        self.name = name
        self.scope = scope

    def _note(self, action: str) -> None:
        self.log.append({"ts": round(self._clock(), 1), "action": action})
        del self.log[:-50]

    def op(self, op: str) -> dict:
        """One owner tap: arm / confirm / off. Returns the state to show."""
        now = self._clock()
        if op == "off":
            if self.on:
                self.on = False
                self._note("OFF")
                self.alert(f"{self.name} OFF", f"{self.scope} will not place orders")
            self.armed_at = 0.0
        elif op == "arm":
            if not self.on:
                self.armed_at = now
                self._note("armed")
        elif op == "confirm":
            if self.on:
                pass
            elif self.armed_at and now - self.armed_at <= ARM_WINDOW_S:
                self.on = True
                self.armed_at = 0.0
                self._note("ON")
                self.alert(f"{self.name} ON", f"{self.scope} may now place orders")
            else:
                self.armed_at = 0.0
                self._note("confirm expired")
        return self.state()

    def state(self) -> dict:
        now = self._clock()
        armed = bool(self.armed_at and now - self.armed_at <= ARM_WINDOW_S)
        return {"on": self.on, "armed": armed,
                "arm_expires_in": (int(self.armed_at + ARM_WINDOW_S - now)
                                   if armed else 0),
                "log": self.log[-10:]}

    def to_dict(self) -> dict:
        return {"on": self.on, "log": self.log}

    def restore(self, d: dict) -> None:
        self.on = bool(d.get("on"))
        self.log = list(d.get("log") or [])
