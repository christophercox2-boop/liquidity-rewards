"""Reward scoring: the arithmetic of Polymarket US liquidity incentives.

Pure functions. No I/O, no network, no clock. Ported closely from 1.0's
track_rewards.py (_score_order / _probe_share), which reproduced the
exchange's published share arithmetic from real books and was checked
against a month of actual payouts.

The formula (https://docs.polymarket.us/incentives/liquidity):

    score = discount_factor ^ (ticks from the best price on your side) x size

You are paid your score divided by the sum of all scores inside the
Target Size window. Four gates decide whether an order earns at all:

1. The side must hold at least Target Size in total, counting everyone's
   orders. Below that the whole side pays nobody.
2. The order must be inside the window: walk out from the best price
   accumulating size until Target Size is reached; anything beyond that
   point scores zero.
3. The reward program must be live (a closed program pays nothing) —
   checked by the program layer before scoring.
4. Queue position: size resting at your price level before you is ahead
   of you. If the window fills before it reaches you, you earn nothing
   however large your order is. 1.0 ignored this in its opportunity scan
   and reported 100% of a window it actually held a seventh of; here
   every join estimate assumes the joining order is LAST at its level.

NO CORRECTION FACTOR, EVER. The estimate is the arithmetic on real
inputs and nothing else (owner's explicit instruction). If the output is
wrong, an input is wrong — fix the input.

Prices are dollars per share (0.001–0.999). Sizes are contracts.
"""

from __future__ import annotations

from dataclasses import dataclass, field

Level = tuple[float, float]  # (price, qty)

# Exchange price bounds: 0.1c to 99.9c.
PRICE_MIN = 0.001
PRICE_MAX = 0.999


@dataclass(frozen=True)
class Book:
    """One market's order book, both sides sorted best-first."""

    bids: tuple[Level, ...]  # highest price first
    asks: tuple[Level, ...]  # lowest price first
    tick: float              # 0.001 or 0.01 dollars
    fetched_at: float = 0.0  # unix time; 0 = unknown. Stale books must not be acted on.

    def side(self, side: str) -> tuple[Level, ...]:
        """The levels a resting order of `side` joins: bids for BUY, asks for SELL."""
        return self.bids if side == "BUY" else self.asks


def normalize_book(bids_raw, asks_raw, fetched_at: float = 0.0) -> Book:
    """Sorted, cleaned levels + inferred tick from raw level lists — one
    normalizer shared by REST fetch and WebSocket stream so both feed
    identical books (ported from 1.0, where diverging normalizers were a
    real risk)."""
    bids = tuple(sorted(((p, q) for p, q in bids_raw if p > 0 and q > 0), key=lambda x: -x[0]))
    asks = tuple(sorted(((p, q) for p, q in asks_raw if p > 0 and q > 0), key=lambda x: x[0]))
    all_px = [p for p, _ in bids + asks]
    tick = 0.001 if any(round(p * 1000) % 10 for p in all_px) else 0.01
    return Book(bids=bids, asks=asks, tick=tick, fetched_at=fetched_at)


@dataclass(frozen=True)
class Score:
    """Outcome of scoring one resting order against a book and a program."""

    earning: bool
    reason: str                     # plain-English, phone-readable
    ticks: int | None = None        # distance from best price on our side
    share: float | None = None      # our score / window score sum (0..1)
    est_day: float | None = None    # $/day, only when a daily side pool was given
    side_total: float = 0.0         # contracts resting on our side (everyone)
    denom: float | None = None      # window score sum
    # For display: (price, qty, ticks, score, is_ours) per window level, first 10.
    window: tuple = field(default_factory=tuple)
    window_more: int = 0            # window levels beyond the first 10


def ticks_from_best(best: float, price: float, tick: float) -> int:
    return round(abs(best - price) / tick)


def window_levels(levels: tuple[Level, ...] | list[Level], target: float) -> list[Level]:
    """Walk out from the best price accumulating size until Target Size is
    reached. The whole boundary level is included — the same convention 1.0
    used and validated. No target means the whole side is the window."""
    out: list[Level] = []
    cum = 0.0
    for px, qty in levels:
        out.append((px, qty))
        cum += qty
        if target and cum >= target:
            break
    return out


def _window_denom(window: list[Level], best: float, tick: float, df: float) -> float:
    return sum(q * df ** ticks_from_best(best, px, tick) for px, q in window)


def score_resting(
    side: str,
    price: float,
    size: float,
    book: Book | None,
    df: float,
    target: float,
    daily_side_pool: float | None = None,
    size_ahead: float | None = None,
) -> Score:
    """Score one resting order. Ported from 1.0's _score_order.

    `size_ahead`: contracts resting at OUR price level that were there
    before us. Pass it when known (the engine records the level's size at
    placement time); the order is outside the window if the window fills
    before reaching it. When None, the whole level is treated as in or
    out together — 1.0's convention, right except at the boundary level.

    The caller is responsible for the book already containing this
    order's remaining size at its level (1.0 topped levels up before
    scoring because books and order snapshots are seconds apart).
    """
    if book is None:
        return Score(earning=False, reason="book unavailable — can't score")
    levels = book.side(side)
    side_name = "bid" if side == "BUY" else "ask"
    if not levels:
        return Score(earning=False, reason=f"{side_name} side empty — score 0")
    tick = book.tick
    best = levels[0][0]
    ticks = ticks_from_best(best, price, tick)

    def mine(px: float) -> bool:
        return abs(px - price) < tick / 2

    if not df:
        return Score(earning=False, reason="program has no discount factor — can't score",
                     ticks=ticks)

    side_total = sum(q for _, q in levels)
    if target and side_total < target:
        return Score(
            earning=False,
            reason=(f"side holds {side_total:,.0f} of {target:,.0f} Target Size "
                    f"— the whole side pays nobody"),
            ticks=ticks, side_total=side_total,
        )

    window = window_levels(levels, target)
    window_end = ticks_from_best(best, window[-1][0], tick)
    denom = _window_denom(window, best, tick, df)
    display = tuple(
        (px, q, ticks_from_best(best, px, tick),
         q * df ** ticks_from_best(best, px, tick), mine(px))
        for px, q in window[:10]
    )

    in_window = any(mine(px) for px, _ in window)
    if in_window and size_ahead is not None and target:
        closer = sum(q for px, q in levels if not mine(px)
                     and ticks_from_best(best, px, tick) < ticks)
        in_window = closer + size_ahead < target
    if not in_window:
        return Score(
            earning=False,
            reason=(f"outside the Target Size window (order {ticks} tick"
                    f"{'s' if ticks != 1 else ''} from best; window ends {window_end})"),
            ticks=ticks, share=0.0, est_day=0.0 if daily_side_pool is not None else None,
            side_total=side_total, denom=denom, window=display,
            window_more=max(len(window) - 10, 0),
        )

    score = size * df ** ticks
    # Order snapshot and book snapshot are seconds apart, so the book may not
    # fully contain this order — never report a share above 100%.
    denom = max(denom, score)
    share = score / denom if denom else 0.0
    est_day = share * daily_side_pool if daily_side_pool is not None else None
    reason = f"scoring — ~{share * 100:.1f}% of the {side_name} side"
    if target:
        reason += f" ({side_total:,.0f} resting >= {target:,.0f} Target Size)"
    return Score(
        earning=True, reason=reason, ticks=ticks, share=share, est_day=est_day,
        side_total=side_total, denom=denom, window=display,
        window_more=max(len(window) - 10, 0),
    )


@dataclass(frozen=True)
class JoinEstimate:
    """What a new order of `qty` at `price` would earn, assuming it rests
    LAST at its level (everyone already there is ahead of it)."""

    qualifies: bool         # side (including our qty) reaches Target Size
    gap: float              # contracts still missing when not qualifying, else 0
    in_window: bool
    share: float            # 0 when not in window or not qualifying
    ticks: int              # from the merged book's best on our side


def estimate_join(
    side: str,
    levels: tuple[Level, ...] | list[Level],
    tick: float,
    df: float,
    target: float,
    price: float,
    qty: float,
) -> JoinEstimate:
    """Queue-aware join estimate — the generalization of 1.0's _probe_share
    (which only handled joining the current best price, and even there
    credited size the window may never reach).

    Works for any price: joining an occupied level, joining an empty
    level, or improving the touch (then we ARE the new best). Our qty is
    merged into the book, and it is in the window only if everything
    ahead of it — all closer levels plus the size already resting at our
    level — sums below Target Size.
    """
    if not levels:
        qualifies = not target or qty >= target
        return JoinEstimate(
            qualifies=qualifies, gap=0.0 if qualifies else target - qty,
            in_window=qualifies, share=1.0 if qualifies else 0.0, ticks=0,
        )
    existing_at_price = sum(q for px, q in levels if abs(px - price) < tick / 2)
    merged = [(px, q) for px, q in levels if abs(px - price) >= tick / 2]
    merged.append((price, existing_at_price + qty))
    merged.sort(key=(lambda x: -x[0]) if side == "BUY" else (lambda x: x[0]))

    total = sum(q for _, q in merged)
    if target and total < target:
        return JoinEstimate(qualifies=False, gap=target - total, in_window=False,
                            share=0.0, ticks=0)

    best = merged[0][0]
    ticks = ticks_from_best(best, price, tick)
    closer = sum(q for px, q in merged if ticks_from_best(best, px, tick) < ticks)
    ahead = closer + existing_at_price
    in_window = not target or ahead < target
    if not in_window:
        return JoinEstimate(qualifies=True, gap=0.0, in_window=False, share=0.0, ticks=ticks)

    window = window_levels(merged, target)
    denom = _window_denom(window, best, tick, df)
    share = (qty * df ** ticks / denom) if denom else 0.0
    return JoinEstimate(qualifies=True, gap=0.0, in_window=True, share=share, ticks=ticks)
