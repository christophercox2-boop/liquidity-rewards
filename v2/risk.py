"""Family-level capital at risk with negative-risk netting.

Every market in a seats family is a bet on ONE underlying number — the
party's seat count K. The old accounting priced each order alone, so
seven asks across the Senate's exact-count rungs "risked" seven
collaterals even though at most one rung can resolve YES. The owner
asked for negative risk in the EV math (2026-08-19): price the book
against K, not order by order.

For one family, capital at risk is the worst outcome over K of

      sum over HELD positions       of its signed loss at K
    + sum over resting OPEN orders  of max(loss at K, 0)

floored at zero. Held positions net in full — a held long on 52 pays
out at exactly the K where a short on 52 loses. Unfilled orders never
get credit for their gains, because nothing obliges the market to fill
them: an adversary fills only what hurts. That keeps the number an
upper bound on what can actually be lost, which is what a ceiling is.

The Senate's exact rungs are mutually exclusive, so asks across them
collapse to (roughly) the single worst collateral. The House's gte
rungs are NESTED — a red wave makes every gte short lose together — and
the same K-sweep prices that correctly with no special casing. Anything
that doesn't parse as a seats rung falls back to per-order pricing.
"""

from __future__ import annotations

from dataclasses import dataclass

from .intents import BUY_LONG, BUY_SHORT


def parse_rung(slug: str) -> tuple[str, str] | None:
    """(family, rung) for a seats slug, None for anything else.
    'scc-senate-gop-2026-11-03-52'     -> (…-2026-11-03, '52')
    'scc-hrep-rep-2026-11-03-gte215'   -> (…-2026-11-03, 'gte215')"""
    family, _, rung = slug.rpartition("-")
    if not family:
        return None
    body = rung[3:] if rung.startswith(("gte", "lte")) else rung
    return (family, rung) if body.isdigit() else None


def rung_pays(rung: str, k: int) -> bool:
    if rung.startswith("gte"):
        return k >= int(rung[3:])
    if rung.startswith("lte"):
        return k <= int(rung[3:])
    return k == int(rung)


@dataclass(frozen=True)
class Leg:
    """One exposure, reduced to what resolution does to it.

    pays_on_yes: True for a long (it collects when the rung hits),
    False for a short (its collateral survives when the rung misses).
    stake: the dollars committed — a long's cost, a short's collateral.
    firm: True for held inventory (losses AND gains are real), False for
    a resting order (the adversary fills only what hurts)."""
    rung: str
    pays_on_yes: bool
    qty: float
    stake: float
    firm: bool

    def loss_at(self, k: int) -> float:
        paid = rung_pays(self.rung, k) == self.pays_on_yes
        return self.stake - (self.qty if paid else 0.0)


def leg_for_inventory(rung: str, qty: float, cost: float) -> Leg | None:
    """The ledger keeps longs as qty>0 with cost=cash paid and shorts as
    qty<0 with cost=collateral committed (see engine._on_fill)."""
    if abs(qty) < 1e-9:
        return None
    return Leg(rung=rung, pays_on_yes=qty > 0, qty=abs(qty),
               stake=max(cost, 0.0), firm=True)


def leg_for_order(rung: str, intent: str, price: float, qty: float) -> Leg | None:
    """Only OPENING intents put new capital at risk; SELL_LONG re-offers
    stock already counted and SELL_SHORT closes a short."""
    if intent == BUY_LONG:
        return Leg(rung=rung, pays_on_yes=True, qty=qty,
                   stake=price * qty, firm=False)
    if intent == BUY_SHORT:
        return Leg(rung=rung, pays_on_yes=False, qty=qty,
                   stake=(1.0 - price) * qty, firm=False)
    return None


def family_risk(legs: list[Leg]) -> float:
    """Worst-case dollars this family's book can lose, over every seat
    count K. Payouts are step functions of K, so checking each rung
    boundary and its neighbors covers every region."""
    if not legs:
        return 0.0
    marks: set[int] = set()
    for leg in legs:
        n = int(leg.rung[3:]) if leg.rung[:3] in ("gte", "lte") else int(leg.rung)
        marks.update((n - 1, n, n + 1))
    worst = 0.0
    for k in marks:
        total = 0.0
        for leg in legs:
            loss = leg.loss_at(k)
            total += loss if leg.firm else max(loss, 0.0)
        worst = max(worst, total)
    return max(worst, 0.0)


def marginal_risk(legs: list[Leg], new_leg: Leg | None) -> float:
    """What one more order adds to the family's worst case. Never
    negative for an order leg (max-of-max monotonicity)."""
    if new_leg is None:
        return 0.0
    return max(family_risk(legs + [new_leg]) - family_risk(legs), 0.0)
