"""
Write a unittest assertion that will fail if value is not None.
"""
import unittest


class TestNone(unittest.TestCase):
    def test_value_is_none(self):
        value = None
        self.assertIsNone(value)


if __name__ == "__main__":
    unittest.main()
