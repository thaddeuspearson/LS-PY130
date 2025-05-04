"""
Write a unittest assertion that will fail if value is not an instance of the
Numeric class exactly. value should not be an instance of one of Numeric's
superclasses.
"""
import unittest


class Numeric:
    pass


class TestType(unittest.TestCase):
    def setUp(self):
        self.value = Numeric()

    def test_value_is_numeric_type(self):
        self.assertEqual(type(self.value), Numeric)


if __name__ == "__main__":
    unittest.main()
