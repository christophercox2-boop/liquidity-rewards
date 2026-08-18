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
4. The window boundary. The documentation says: "If Target Size is
   reached before your price level, your order will not score,
   regardless of how close it is to the best price. For example, if
   Target Size is 20,000 and there are 25,000 contracts resting at the
   best price, orders at the second-best price receive zero score."
   That settles BETWEEN levels. It is AMBIGUOUS about an order at the
   level where the target is reached mid-level: does the whole level
   score (level reading) or only the size that fits before the cutoff
   (queue reading)? Unconfirmed either way — see EXP-1 in DESIGN.md.
   Until the experiment settles it, join estimates report BOTH readings
   and anything sizing real money uses the conservative (queue) one.

Separate from the boundary question, share DILUTION at a shared level is
not ambiguous: your score is your own size times df^ticks, never the
level's. 1.0's opportunity scan credited the whole level as its own and
reported 100% of a window it held a seventh of; that bug class is dead
here by construction.

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
    placement time) to apply the QUEUE reading of the window boundary —
    the order is outside the window if the window fills before reaching
    it. That reading is UNCONFIRMED (see EXP-1); when None, the whole
    level is in or out together — the documented example's convention,
    and 1.0's.

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
    """What a new order of `qty` at `price` would earn, under both readings
    of the window-boundary rule (see the module docstring and EXP-1).

    `share`/`in_window` use the conservative QUEUE reading: everyone
    already at our level is ahead of us, and if the window fills before
    reaching us we earn nothing. `share_if_level`/`in_window_level` use
    the LEVEL reading: a level the walk reaches scores whole. Size real
    money by `share`; the gap between the two is the measured stake of
    the open question."""

    qualifies: bool         # side (including our qty) reaches Target Size
    gap: float              # contracts still missing when not qualifying, else 0
    ticks: int              # from the merged book's best on our side
    in_window: bool         # queue reading
    share: float            # queue reading; 0 when out of window / not qualifying
    in_window_level: bool   # level reading
    share_if_level: float   # level reading


def estimate_join(
    side: str,
    levels: tuple[Level, ...] | list[Level],
    tick: float,
    df: float,
    target: float,
    price: float,
    qty: float,
) -> JoinEstimate:
    """Join estimate for any price: joining an occupied level, opening an
    empty one, or improving the touch (then we ARE the new best). Our qty
    is merged into the book (one entry per price level — the
    generalization of 1.0's _probe_share, which only handled the best
    price; the level merge is what kills the credit-others'-size bug).

    Both boundary readings are computed: queue (our order is in the
    window only if all closer levels PLUS the size already resting at our
    level sum below Target Size) and level (our level is in the window if
    the closer levels alone sum below Target Size)."""
    if not levels:
        qualifies = not target or qty >= target
        share = 1.0 if qualifies else 0.0
        return JoinEstimate(
            qualifies=qualifies, gap=0.0 if qualifies else target - qty, ticks=0,
            in_window=qualifies, share=share,
            in_window_level=qualifies, share_if_level=share,
        )
    existing_at_price = sum(q for px, q in levels if abs(px - price) < tick / 2)
    merged = [(px, q) for px, q in levels if abs(px - price) >= tick / 2]
    merged.append((price, existing_at_price + qty))
    merged.sort(key=(lambda x: -x[0]) if side == "BUY" else (lambda x: x[0]))

    total = sum(q for _, q in merged)
    if target and total < target:
        return JoinEstimate(qualifies=False, gap=target - total, ticks=0,
                            in_window=False, share=0.0,
                            in_window_level=False, share_if_level=0.0)

    best = merged[0][0]
    ticks = ticks_from_best(best, price, tick)
    closer = sum(q for px, q in merged if ticks_from_best(best, px, tick) < ticks)
    in_level = not target or closer < target
    in_queue = not target or closer + existing_at_price < target

    window = window_levels(merged, target)
    denom = _window_denom(window, best, tick, df)
    raw = (qty * df ** ticks / denom) if denom else 0.0
    return JoinEstimate(
        qualifies=True, gap=0.0, ticks=ticks,
        in_window=in_queue, share=raw if in_queue else 0.0,
        in_window_level=in_level, share_if_level=raw if in_level else 0.0,
    )
