"""Order intents and capital at risk.

The exchange has four order intents and two of them rest on the OPPOSITE
side from what the name suggests. Getting this wrong has put a bid on
the book where an ask was meant, bidding against ourselves. This module
is the single place the mapping lives.

    intent                    opens/closes            rests as
    ORDER_INTENT_BUY_LONG     opens a long            BID
    ORDER_INTENT_BUY_SHORT    opens a short           ASK
    ORDER_INTENT_SELL_LONG    sells held stock        ASK
    ORDER_INTENT_SELL_SHORT   buys back a short       BID

An ask is not a cheap bid: a bid at 5c risks 5c a share; an ask at 5c is
an opening short and risks 95c a share — nineteen times as much. Any
budget that prices them the same funds far more risk than it believes.
"""

from __future__ import annotations

BUY_LONG = "ORDER_INTENT_BUY_LONG"
BUY_SHORT = "ORDER_INTENT_BUY_SHORT"
SELL_LONG = "ORDER_INTENT_SELL_LONG"
SELL_SHORT = "ORDER_INTENT_SELL_SHORT"

# Which side of the book each intent rests on.
REST_SIDE = {
    BUY_LONG: "BUY",
    SELL_SHORT: "BUY",
    BUY_SHORT: "SELL",
    SELL_LONG: "SELL",
}


def rest_side(intent: str) -> str:
    """BUY (bid) or SELL (ask) — the book side the order will rest on."""
    return REST_SIDE[intent]


def intent_for(side: str, net_position: float, size: float,
               close_short: bool = False) -> str:
    """The right intent for resting `size` contracts on book side `side`
    (BUY = bid, SELL = ask), holding `net_position` (positive = long,
    negative = short). Ported from 1.0, where this decision was duplicated
    in three places and always the same shape.

    An ask sells held stock when there is enough of it, otherwise it opens
    a short. A bid opens a long unless it is explicitly buying back a
    short (close_short) — never silently, because SELL_SHORT rests as a
    BID and using it "to place an ask" is the classic self-bidding bug.
    """
    if side == "SELL":
        return SELL_LONG if net_position >= size else BUY_SHORT
    return SELL_SHORT if close_short else BUY_LONG


def capital_at_risk(intent: str, price: float, qty: float) -> float:
    """Dollars this resting order can lose if filled, for the risk ceiling.

    A bid (opening long) risks price x qty. An opening short risks
    (1 - price) x qty. Closing intents free risk rather than adding it:
    SELL_LONG sells stock already owned (its value is at risk whether or
    not the ask rests) and SELL_SHORT closes a short — both count zero
    new capital here. The engine accounts for held inventory separately.
    """
    if intent == BUY_LONG:
        return price * qty
    if intent == BUY_SHORT:
        return (1.0 - price) * qty
    return 0.0
