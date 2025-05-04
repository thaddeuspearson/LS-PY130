"""
Write a test that will fail if 'xyz' is one of the elements in the list lst
"""
import unittest


class TestNotIncludedObject(unittest.TestCase):
    def test_object_not_included(self):
        lst = ["123", "abc"]
        self.assertNotIn("xyz", lst)


if __name__ == "__main__":
    unittest.main()
