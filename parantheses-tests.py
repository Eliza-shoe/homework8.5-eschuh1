import unittest
from parentheses import parentheses_to_remove


class Tests(unittest.TestCase):
    def test_null(self):
        self.assertEqual(parentheses_to_remove(""), 0)

    def test_backwards(self):
        self.assertEqual(parentheses_to_remove(")abc)(("), 4)


if __name__ == "__main__":
    unittest.main()
