"""Capital at risk with negative-risk netting — generalized past the seats.

2.0 priced the seats ladders honestly (owner, 2026-08-19: negative risk
in the ceiling): mutually exclusive rungs can't all lose, so the family's
risk is the worst single outcome, not the sum of collaterals. But it
only understood scc- rungs. 3.0's politics book spans hundreds of race
GROUPS — the candidates of one primary, the brackets of one margin
ladder, the exact/gte rungs of a seat count — and every one of those
groups has the same structure: ONE outcome resolves YES.

So the sweep is generalized:

* A group whose members parse as NUMERIC rungs (52, gte215, lte45, d4-7
  margin brackets are categorical, not numeric) is priced over the
  underlying integer K, exactly 2.0's sweep — nested gte rungs lose
  together in a wave and the K-sweep prices that with no special case.
* Any other group — candidates, brackets, parties — is priced over
  "which member resolves YES" (each member in turn, and none of them):
  a categorical winner sweep.
* Held inventory nets in full (its gains at an outcome are real).
  Resting ORDERS never get credit for gains — nothing obliges the
  market to fill them; an adversary fills only what hurts. The result
  stays an upper bound on what can actually be lost, which is what a
  ceiling is for.
* Orders in markets that share no group with anything else fall back to
  per-order collateral, unchanged.

The group key is the race key — the slug minus its final token — the
same grouping the pool divisor uses, so the two views of "one event"
can never disagree.
"""

from __future__ import annotations

from .intents import BUY_LONG, BUY_SHORT, capital_at_risk


def race_key(slug: str) -> str:
    return slug.rsplit("-", 1)[0]


def rung_token(slug: str) -> str:
    return slug.rsplit("-", 1)[-1]


def numeric_rung(tok: str) -> bool:
    body = tok[3:] if tok.startswith(("gte", "lte")) else tok
    return body.isdigit()


def rung_pays(tok: str, k: int) -> bool:
    if tok.startswith("gte"):
        return k >= int(tok[3:])
    if tok.startswith("lte"):
        return k <= int(tok[3:])
    return k == int(tok)


class Leg:
    """One exposure, reduced to what resolution does to it.
    pays_on_yes: True for a long, False for a short. stake: dollars
    committed. firm: held inventory (gains real) vs resting order."""

    __slots__ = ("market", "pays_on_yes", "qty", "stake", "firm")

    def __init__(self, market: str, pays_on_yes: bool, qty: float,
                 stake: float, firm: bool):
        self.market = market
        self.pays_on_yes = pays_on_yes
        self.qty = qty
        self.stake = stake
        self.firm = firm

    def loss_if(self, yes: bool) -> float:
        paid = yes == self.pays_on_yes
        return self.stake - (self.qty if paid else 0.0)


def leg_for_order(market: str, intent: str, price: float, qty: float) -> Leg | None:
    """Only OPENING intents commit new capital."""
    if intent == BUY_LONG:
        return Leg(market, True, qty, price * qty, firm=False)
    if intent == BUY_SHORT:
        return Leg(market, False, qty, (1.0 - price) * qty, firm=False)
    return None


def leg_for_inventory(market: str, net: float, cost: float) -> Leg | None:
    if abs(net) < 1e-9:
        return None
    if net > 0:
        return Leg(market, True, net, max(cost, 0.0), firm=True)
    return Leg(market, False, -net, max(-cost, 0.0), firm=True)


def _group_risk(legs: list[Leg]) -> float:
    """Worst case for one mutually-exclusive group."""
    toks = {rung_token(l.market) for l in legs}
    if all(numeric_rung(t) for t in toks):
        marks: set[int] = set()
        for t in toks:
            n = int(t[3:]) if t.startswith(("gte", "lte")) else int(t)
            marks.update((n - 1, n, n + 1))
        worst = 0.0
        for k in marks:
            total = 0.0
            for leg in legs:
                loss = leg.loss_if(rung_pays(rung_token(leg.market), k))
                total += loss if leg.firm else max(loss, 0.0)
            worst = max(worst, total)
        return max(worst, 0.0)
    # categorical: each member wins in turn, or none of them do
    outcomes = sorted({l.market for l in legs} | {""})
    worst = 0.0
    for winner in outcomes:
        total = 0.0
        for leg in legs:
            loss = leg.loss_if(leg.market == winner)
            total += loss if leg.firm else max(loss, 0.0)
        worst = max(worst, total)
    return max(worst, 0.0)


def book_risk(order_legs: list[Leg], inv_legs: list[Leg] = ()) -> float:
    """Worst-case dollars a whole book can lose: groups priced by their
    sweep, singletons by plain collateral."""
    groups: dict[str, list[Leg]] = {}
    for leg in list(order_legs) + list(inv_legs):
        groups.setdefault(race_key(leg.market), []).append(leg)
    total = 0.0
    for legs in groups.values():
        if len({l.market for l in legs}) == 1 and not any(l.firm for l in legs):
            # a lone market: same result, cheaper arithmetic
            total += sum(max(l.loss_if(not l.pays_on_yes), 0.0) for l in legs)
        else:
            total += _group_risk(legs)
    return round(total, 6)


def order_legs(orders) -> list[Leg]:
    """FamilyOrder records (purpose != sell) -> legs."""
    out = []
    for o in orders:
        if o.purpose == "sell":
            continue
        leg = leg_for_order(o.market, o.intent, o.price, o.qty)
        if leg is not None:
            out.append(leg)
    return out


def marginal(orders, market: str, intent: str, price: float, qty: float) -> float:
    """What one more resting order adds to the book's worst case. For a
    bid on a NEW bracket of a race we already quote, this is far less
    than its collateral — the negative-risk credit the owner asked for.
    Never negative."""
    base = order_legs(orders)
    new = leg_for_order(market, intent, price, qty)
    if new is None:
        return 0.0
    return max(book_risk(base + [new]) - book_risk(base), 0.0)
