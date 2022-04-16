import unittest


##decimal integer to binary integer
def to_binary(n):
    b = bin(n)
    b = int(b.replace("0b", ""))
    return b


# sum every other binary digit (all odd digits)
def sum_every_other(b):
    b = str(b)
    count = 0
    for i in range(0, len(b), 2):
        count += int(b[i])
    return count


class Bin_Tests(unittest.TestCase):
    def test_null(self):
        self.assertEqual(to_binary(0), 0)

    def test_non_null(self):
        self.assertEqual(to_binary(22), 10110)


class Sum_Every_Other_Tests(unittest.TestCase):
    def test_null(self):
        self.assertEqual(sum_every_other(0), 0)

    def test_non_null(self):
        self.assertEqual(sum_every_other(10110), 2)


if __name__ == "__main__":
    print(sum_every_other(10110))
    unittest.main()
