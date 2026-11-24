import unittest
from audit import distance, evaluate


class Scoring(unittest.TestCase):
    def test_single_edits(self):
        for reference, candidate in [("a b", "a"), ("a", "a b"), ("a b", "a c")]:
            self.assertEqual(distance(reference.split(), candidate.split()), 1)

    def test_corpus_includes_silence(self):
        rows = [dict(id="a", reference="One two", candidate="one two"),
                dict(id="b", reference="", candidate="extra")]
        self.assertEqual(evaluate(rows, True)["wer"], .5)
        self.assertEqual(evaluate(rows)["wer"], 1)

    def test_duplicate_id(self):
        row = dict(id="a", reference="one", candidate="")
        with self.assertRaises(ValueError):
            evaluate([row, row])

    def test_empty_corpus(self):
        with self.assertRaises(ValueError):
            evaluate([])
