"""Market names: the owner should never have to read a slug.

Two sources, in order of trust:

1. **The feed's own words.** Discovery and the order feed both carry
   titles — a market question, an event title, a subject (the candidate,
   the bracket). Whatever arrives is harvested here, once, and kept.
2. **The slug decoder.** Politics slugs follow family-code + state +
   date + subject. When the feed has said nothing yet, decode that:
   "ushsscc-ushrsc-al-2026-11-03-0" reads "Alabama House seat count
   exactly 0", which beats the slug on any phone screen.

`label(slug)` is the one call every page and alert goes through.
"""

from __future__ import annotations

MAX_LEN = 110

_SLUG_WORDS = (
    ("usgubp", "Governor primary"), ("usgubmov", "Governor margin"),
    ("usgubsc", "Governor seat count"), ("usgub", "Governor"),
    ("ussep", "Senate primary"), ("ussemov", "Senate margin"),
    ("ussesc", "Senate seat count"), ("usse", "Senate"),
    ("ushrp", "House primary"), ("ushrsc", "House seat count"),
    ("ushrep", "House"), ("ushr", "House"), ("hrep", "House"),
    ("uspresp", "Presidential primary"), ("uspres", "President"),
    ("usp", "President"), ("usho", "House control"),
    ("usgovcc", "Governors count"), ("senate", "Senate"),
    ("midterms", "Midterms"),
    ("cfb", "CFB win total"), ("nfl", "NFL"),
)
_STATES = {
    "al": "Alabama", "ak": "Alaska", "az": "Arizona", "ar": "Arkansas",
    "ca": "California", "co": "Colorado", "ct": "Connecticut", "de": "Delaware",
    "fl": "Florida", "ga": "Georgia", "hi": "Hawaii", "id": "Idaho",
    "il": "Illinois", "in": "Indiana", "ia": "Iowa", "ks": "Kansas",
    "ky": "Kentucky", "la": "Louisiana", "me": "Maine", "md": "Maryland",
    "ma": "Massachusetts", "mi": "Michigan", "mn": "Minnesota",
    "ms": "Mississippi", "mo": "Missouri", "mt": "Montana", "ne": "Nebraska",
    "nv": "Nevada", "nh": "New Hampshire", "nj": "New Jersey",
    "nm": "New Mexico", "ny": "New York", "nc": "North Carolina",
    "nd": "North Dakota", "oh": "Ohio", "ok": "Oklahoma", "or": "Oregon",
    "pa": "Pennsylvania", "ri": "Rhode Island", "sc": "South Carolina",
    "sd": "South Dakota", "tn": "Tennessee", "tx": "Texas", "ut": "Utah",
    "vt": "Vermont", "va": "Virginia", "wa": "Washington",
    "wv": "West Virginia", "wi": "Wisconsin", "wy": "Wyoming",
}


def name_from_market(m: dict, event_title: str = "") -> str:
    """The most descriptive label a feed payload offers, without repeating
    itself: a market question when there is one, otherwise the event title
    with the market's own subject (the candidate, the bracket) appended."""
    q = str(m.get("question") or m.get("title") or m.get("name") or "").strip()
    subj = m.get("subject")
    sub = str((subj or {}).get("name") if isinstance(subj, dict)
              else (subj or "")).strip()
    ev = (event_title or "").strip()
    if q and len(q) > len(sub) + 4:
        return q                       # a real question stands on its own
    tail = sub or q
    if ev and tail and tail.lower() not in ev.lower():
        return f"{ev} — {tail}"
    return ev or tail


def decode_slug(m: str) -> str:
    """A readable guess at what a market is, from its slug alone."""
    parts = [p for p in str(m or "").split("-") if p]
    if not parts:
        return m
    what = ""
    for tok in parts:
        for code, word in _SLUG_WORDS:
            if tok == code or tok.endswith(code):
                what = word
                break
        if what:
            break
    state = next((_STATES[p] for p in parts if p in _STATES), "")
    # Find the date (YYYY or YYYY-MM-DD) so its tokens are never mistaken
    # for a bracket; whatever FOLLOWS the date is the market's subject.
    subj = None
    for i, tok in enumerate(parts):
        if len(tok) == 4 and tok.isdigit() and tok.startswith("20"):
            j = i + 1
            if (i + 2 < len(parts) and parts[i + 1].isdigit()
                    and len(parts[i + 1]) == 2 and parts[i + 2].isdigit()
                    and len(parts[i + 2]) == 2):
                j = i + 3
            subj = parts[j:]
            break
    if subj is None:          # no date in the slug — fall back to the tail
        subj = (parts[-2:] if (len(parts) >= 2 and parts[-1].isdigit()
                               and parts[-2].isdigit()) else parts[-1:])

    def _side(tok: str) -> str:
        return {"d": "D", "r": "R"}.get(tok[:1], "")

    extra = ""
    if len(subj) == 2 and subj[0].isdigit() and subj[1].isdigit():
        extra = f"{subj[0]}–{subj[1]}"          # ...-20-21 -> "20 to 21"
    elif (len(subj) == 2 and _side(subj[0]) and subj[0][1:].isdigit()
            and subj[1].isdigit()):
        # margin bracket over two tokens: d12-15 -> "D +12 to 15"
        extra = f"{_side(subj[0])} +{subj[0][1:]}–{subj[1]}"
    elif len(subj) == 1:
        t = subj[0]
        side = _side(t)
        body = t[1:] if side else t
        if body.startswith("gte") and body[3:].isdigit():
            extra = (f"{side} +{body[3:]}" if side else body[3:]) + " or more"
        elif body.startswith("lte") and body[3:].isdigit():
            extra = (f"{side} +{body[3:]}" if side else body[3:]) + " or fewer"
        elif side and body.isdigit():
            extra = f"{side} +{body}"
        elif t.isdigit():
            extra = f"exactly {t}"
        elif "adv" in parts:
            extra = f"advances — {t}" if t.isalpha() else "advances"
        elif t.isalpha() and t not in ("dem", "rep", "gop") and len(t) >= 5:
            extra = t         # a candidate code the feed will name properly
    elif "adv" in parts:
        extra = "advances"
    if "nom" in parts:
        what = (what + " nomination").strip()
    if "dem" in parts and not ("rep" in parts or "gop" in parts):
        what = (what + " (D)").strip()
    elif ("rep" in parts or "gop" in parts) and "dem" not in parts:
        what = (what + " (R)").strip()
    bits = [b for b in (state, what, extra) if b]
    return " ".join(bits) if bits else m


class Names:
    """The one name store. Feed-harvested names win; the decoder fills in."""

    def __init__(self):
        self.known: dict[str, str] = {}

    def learn(self, slug: str, m: dict | None = None,
              event_title: str = "") -> None:
        if not slug:
            return
        nm = name_from_market(m or {}, event_title)
        if nm and len(nm) > len(self.known.get(slug, "")):
            self.known[slug] = nm[:MAX_LEN]

    def label(self, slug: str) -> str:
        return self.known.get(slug) or decode_slug(slug)

    def to_dict(self) -> dict:
        return {"known": self.known}

    def restore(self, d: dict) -> None:
        self.known.update(d.get("known") or {})


def disambiguate(pairs: list[tuple[str, str]]) -> dict[str, str]:
    """slug -> final label. Where one label covers several sibling
    markets (every 2028 candidate market carries the same event
    question), append each slug's distinguishing tail so the reader can
    tell WHICH candidate the card is about (owner, 2026-08-21: "I can't
    tell from these names who the candidate is")."""
    groups: dict[str, list[str]] = {}
    for slug, label in pairs:
        groups.setdefault(label, []).append(slug)
    out: dict[str, str] = {}
    for label, slugs in groups.items():
        if len(slugs) == 1:
            out[slugs[0]] = label
            continue
        import os.path
        pre = os.path.commonprefix(slugs)
        if "-" in pre:
            pre = pre[:pre.rfind("-") + 1]
        else:
            pre = ""
        for s in slugs:
            tail = s[len(pre):] or s.rsplit("-", 1)[-1]
            out[s] = f"{label} \u2014 {tail}"[:110]
    return out
