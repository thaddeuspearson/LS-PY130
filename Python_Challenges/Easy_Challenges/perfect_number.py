"""
The Greek mathematician Nicomachus devised a classification scheme for natural
numbers (1, 2, 3, ...), identifying each as belonging uniquely to the
categories of abundant, perfect, or deficient based on a comparison between the
number and the sum of its positive divisors (the numbers that can be evenly
divided into the target number with no remainder, excluding the number itself).
For instance, the positive divisors of 15 are 1, 3, and 5. This sum is known as
the Aliquot sum.

    Perfect numbers have an Aliquot sum that is equal to the original number.
    Abundant numbers have an Aliquot sum that is greater than the original
    number.
    Deficient numbers have an Aliquot sum that is less than the original
    number.

Examples:

    6 is a perfect number since its divisors are 1, 2, and 3, and
    1 + 2 + 3 = 6.

    28 is a perfect number since its divisors are 1, 2, 4, 7, and 14 and
    1 + 2 + 4 + 7 + 14 = 28.

    15 is a deficient number since its divisors are 1, 3, and 5 and
    1 + 3 + 5 = 9 which is less than 15.

    24 is an abundant number since its divisors are 1, 2, 3, 4, 6, 8, and 12
    and 1 + 2 + 3 + 4 + 6 + 8 + 12 = 36 which is greater than 24.

    Prime numbers 7, 13, etc are always deficient since their only divisor is 1

Write a program that can tell whether a number is perfect, abundant, or
deficient.
"""


class PerfectNumber:
    @staticmethod
    def _get_factors(num: int) -> list:
        return [f for f in range(1, num) if num % f == 0]

    @classmethod
    def classify(cls, number: int) -> str:
        if not isinstance(number, int) or number < 0:
            raise ValueError("Input must be a positive integer")
        factors = cls._get_factors(number)
        sum_of_factors = sum(factors)

        if sum_of_factors > number:
            classification = "abundant"
        elif sum_of_factors == number:
            classification = "perfect"
        else:
            classification = "deficient"
        return classification
