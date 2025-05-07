"""
Write a program that, given a natural number and a set of one or more other
numbers, can find the sum of all the multiples of the numbers in the set that
are less than the first number. If the set of numbers is not given, use a
default set of 3 and 5.

For instance, if we list all the natural numbers up to, but not including, 20
that are multiples of either 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18.
The sum of these multiples is 78.
"""


class SumOfMultiples:
    def __init__(self, *bases: int):
        self.bases = bases or (3, 5)

    @classmethod
    def sum_up_to(cls, number) -> int:
        return cls().to(number)

    def to(self, number: int) -> int:
        unique_base_multiples = set()

        for base in self.bases:
            if base > 0 and base < number:
                for num in range(base, number, base):
                    unique_base_multiples.add(num)

        return sum(unique_base_multiples)
