"""
Write a test that will fail if lst and the return value of lst.process are
different objects.
"""
import unittest


class Lst:
    def __init__(self):
        self.lst = []

    def process(self):
        return self


class TestSameObject(unittest.TestCase):
    def setUp(self):
        self.lst = Lst()

    def test_lst_is_same_object(self):
        self.assertIs(self.lst, self.lst.process())


if __name__ == "__main__":
    unittest.main()
