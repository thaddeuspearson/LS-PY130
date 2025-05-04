"""
Write a unittest assertion that will fail if value % 2 != 0 is not True.
"""
import unittest


class TestBoolean(unittest.TestCase):
    def test_even(self):
        value = 3
        self.assertTrue(value % 2 != 0, "Value is not odd")


if __name__ == "__main__":
    unittest.main()
