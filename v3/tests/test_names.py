"""Names: the feed's words win, the decoder covers the rest."""

import unittest

from v3.names import Names, decode_slug, name_from_market


class TestDecoder(unittest.TestCase):
    CASES = [
        ("erac-usgubp-ak-adv-2026-08-18-adacru",
         "Alaska Governor primary advances — adacru"),
        ("ushsscc-ushrsc-al-2026-11-03-0", "Alabama House seat count exactly 0"),
        ("usgovcc-26mid-rep-2026-11-03-20-21", "Governors count (R) 20–21"),
        ("vmc-usgubmov-or-2026-11-03-d12-15", "Oregon Governor margin D +12–15"),
        ("vmc-usgubmov-or-2026-11-03-dgte21", "Oregon Governor margin D +21 or more"),
        ("scc-senate-gop-2026-11-03-46", "Senate (R) exactly 46"),
        ("scc-hrep-rep-2026-11-03-gte180", "House (R) 180 or more"),
        ("enwc-uspres-nom-dem-2028-petbut", "President nomination (D) petbut"),
        ("paccc-usho-midterms-2026-11-03-rep", "House control (R)"),
        ("vmc-ussemov-ga-2026-11-03-r0-3", "Georgia Senate margin R +0–3"),
        ("ushsscc-ushrsc-ca-2026-11-03-lte2",
         "California House seat count 2 or fewer"),
    ]

    def test_decodes_every_family_shape(self):
        for slug, want in self.CASES:
            self.assertEqual(decode_slug(slug), want, slug)

    def test_date_tokens_never_read_as_brackets(self):
        # the 2026-08-20 defect: "-2026-11-03-46" once became "03–46"
        self.assertNotIn("03–", decode_slug("scc-senate-gop-2026-11-03-46"))

    def test_unknown_slug_survives(self):
        self.assertEqual(decode_slug(""), "")
        self.assertTrue(decode_slug("zzz"))


class TestStore(unittest.TestCase):
    def test_feed_name_beats_decoder(self):
        n = Names()
        slug = "scc-senate-gop-2026-11-03-46"
        self.assertEqual(n.label(slug), "Senate (R) exactly 46")
        n.learn(slug, {"question": "Will Republicans win exactly 46 Senate seats?"})
        self.assertTrue(n.label(slug).startswith("Will Republicans"))

    def test_event_title_plus_subject(self):
        self.assertEqual(
            name_from_market({"subject": {"name": "Pete B."}}, "2028 Dem nominee"),
            "2028 Dem nominee — Pete B.")

    def test_longer_name_wins_and_persists(self):
        n = Names()
        n.learn("s", {"title": "Short"})
        n.learn("s", {"title": "A much more descriptive market name"})
        n.learn("s", {"title": "tiny"})
        self.assertEqual(n.known["s"], "A much more descriptive market name")
        n2 = Names()
        n2.restore(n.to_dict())
        self.assertEqual(n2.known, n.known)


if __name__ == "__main__":
    unittest.main()
