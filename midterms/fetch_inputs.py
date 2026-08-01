#!/usr/bin/env python3
"""Best-effort auto-updater for midterms/inputs_2026.json.

Pulls recent presidential-approval and generic-congressional-ballot polls
from VoteHub's public polling API and rewrites the two live inputs
(``approval`` and ``generic_ballot_dem_margin``) with a median of recent
polls. Everything else in the inputs file is left untouched.

Designed to fail safely: if the API is unreachable, the response doesn't
parse, too few polls are found, or the numbers are implausible, it exits
non-zero WITHOUT touching the inputs file — the model then simply runs on
the last committed inputs. (The weekly GitHub Action treats a failure here
as non-fatal for exactly that reason.)

Usage:
    python3 midterms/fetch_inputs.py                 # fetch live, update file
    python3 midterms/fetch_inputs.py --dry-run       # fetch live, print only
    python3 midterms/fetch_inputs.py --fixture data/votehub_fixture.json
"""

import argparse
import json
import ssl
import sys
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
API = "https://api.votehub.com/polls?poll_type={kind}&page_size=100"
WINDOW_DAYS = 45     # only use polls ending within this window
MIN_POLLS = 5        # refuse to update from fewer polls than this
UA = "midterm-forecast/1.0 (github.com; polling-average script)"


def fetch_json(kind):
    req = urllib.request.Request(API.format(kind=kind), headers={"User-Agent": UA})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        return json.load(resp)


def poll_list(payload):
    """Accept either a bare list or a wrapper object with a list inside."""
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("data", "polls", "results", "items"):
            if isinstance(payload.get(key), list):
                return payload[key]
    raise ValueError("unrecognized API payload shape")


def parse_end_date(poll):
    for key in ("end_date", "endDate", "end"):
        raw = poll.get(key)
        if not raw:
            continue
        try:
            return datetime.fromisoformat(str(raw).replace("Z", "+00:00")).date()
        except ValueError:
            continue
    return None


def answer_pct(poll, prefixes):
    """Find the pct for an answer whose name starts with any prefix."""
    answers = poll.get("answers") or poll.get("responses") or []
    for a in answers:
        if not isinstance(a, dict):
            continue
        name = str(a.get("choice") or a.get("answer") or a.get("name") or "").lower()
        if any(name.startswith(p) for p in prefixes):
            try:
                return float(a.get("pct") or a.get("percent") or a.get("value"))
            except (TypeError, ValueError):
                return None
    return None


def recent_values(payload, extract, subject=None):
    cutoff = date.today() - timedelta(days=WINDOW_DAYS)
    vals = []
    for poll in poll_list(payload):
        if not isinstance(poll, dict):
            continue
        if subject and subject.lower() not in str(poll.get("subject", subject)).lower():
            continue
        end = parse_end_date(poll)
        if end is None or end < cutoff:
            continue
        v = extract(poll)
        if v is not None:
            vals.append(v)
    return vals


def get_approval(payload):
    vals = recent_values(
        payload,
        lambda p: answer_pct(p, ("approve", "yes")),
        subject="Trump",
    )
    if len(vals) < MIN_POLLS:
        raise ValueError(f"only {len(vals)} usable approval polls (need {MIN_POLLS})")
    m = round(median(vals), 1)
    if not 20 <= m <= 70:
        raise ValueError(f"implausible approval median {m}")
    return m, len(vals)


def get_generic_ballot(payload):
    def margin(p):
        d = answer_pct(p, ("dem",))
        r = answer_pct(p, ("rep", "gop"))
        return None if d is None or r is None else d - r

    vals = recent_values(payload, margin)
    if len(vals) < MIN_POLLS:
        raise ValueError(f"only {len(vals)} usable generic-ballot polls (need {MIN_POLLS})")
    m = round(median(vals), 1)
    if abs(m) > 15:
        raise ValueError(f"implausible generic-ballot median {m:+.1f}")
    return m, len(vals)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true",
                    help="print the numbers, don't touch inputs_2026.json")
    ap.add_argument("--fixture", type=Path,
                    help="parse a saved JSON file (with keys 'approval' and "
                         "'generic_ballot' holding API payloads) instead of "
                         "hitting the network — for testing")
    args = ap.parse_args()

    try:
        if args.fixture:
            with open(args.fixture) as f:
                fx = json.load(f)
            approval_payload = fx["approval"]
            gb_payload = fx["generic_ballot"]
        else:
            approval_payload = fetch_json("approval")
            gb_payload = fetch_json("generic-ballot")

        approval, n_a = get_approval(approval_payload)
        gb, n_g = get_generic_ballot(gb_payload)
    except Exception as e:  # any failure -> leave inputs untouched
        print(f"fetch_inputs: FAILED, inputs left unchanged: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"approval: {approval}% (median of {n_a} polls, last {WINDOW_DAYS}d)")
    print(f"generic ballot: D{gb:+.1f} (median of {n_g} polls, last {WINDOW_DAYS}d)")

    if args.dry_run:
        return

    inputs_path = HERE / "inputs_2026.json"
    with open(inputs_path) as f:
        inp = json.load(f)
    inp["approval"] = approval
    inp["generic_ballot_dem_margin"] = gb
    src = "fixture" if args.fixture else "VoteHub polling API"
    inp["as_of"] = (f"{date.today().isoformat()} (auto: median of {n_a} approval / "
                    f"{n_g} generic-ballot polls, {src})")
    with open(inputs_path, "w") as f:
        json.dump(inp, f, indent=2)
        f.write("\n")
    print(f"updated {inputs_path}")


if __name__ == "__main__":
    main()
