"""
Write a unittest assertion that will fail unless employee.hire raises a
NoExperienceError exception.
"""
import unittest


class NoExperienceError(Exception):
    pass


class Employee:
    def __init__(self, experience=False):
        self.experience = experience

    def hire(self):
        if not self.experience:
            raise NoExperienceError()


class TestException(unittest.TestCase):
    def setUp(self):
        self.employee = Employee()

    def test_raise_NoExperienceError(self):
        with self.assertRaises(NoExperienceError):
            self.employee.hire()


if __name__ == "__main__":
    unittest.main()
