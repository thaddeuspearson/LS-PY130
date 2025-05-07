"""
Implement octal to decimal conversion. Given an octal input string, your
program should produce a decimal output. Treat invalid input as octal 0. Note
that the only valid digits in an octal number are 0, 1, 2, 3, 4, 5, 6, and 7.

Note: Implement the conversion yourself. Don't use any built-in or library
methods that perform the necessary conversions for you. In this exercise, the
code necessary to perform the conversion is what we're looking for.
"""


class Octal:
    def __init__(self, octal: str) -> None:
        self.octal = Octal._get_valid_octal(octal)

    def to_decimal(self) -> int:
        decimal = 0
        curr_power = len(self.octal) - 1

        for digit in self.octal:
            decimal += int(digit) * (8 ** curr_power)
            curr_power -= 1

        return decimal

    @staticmethod
    def _get_valid_octal(num: str):
        return num if set(num) <= set('01234567') else '0'
