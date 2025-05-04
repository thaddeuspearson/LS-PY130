"""
Write a unittest assertion that will fail if the 'xyz' is not in the list lst.
"""
import unittest


class TestIncludedObject(unittest.TestCase):
    def test_object_is_included(self):
        lst = ["xyz", "abc"]
        self.assertIn("xyz", lst)


if __name__ == "__main__":
    unittest.main()
