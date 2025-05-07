"""
Write some code that converts modern decimal numbers into their Roman number
equivalents.

The Romans were a clever bunch. They conquered most of Europe and ruled it for
hundreds of years. They invented concrete and straight roads and even bikinis.
One thing they never discovered though was the number zero. This made writing
and dating extensive histories of their exploits slightly more challenging, but
the system of numbers they came up with is still in use today. For example the
BBC uses Roman numerals to date their programmes.

The Romans wrote numbers using letters - I, V, X, L, C, D, M. Notice that
these letters have lots of straight lines and are hence easy to hack into
stone tablets.

 1  => I
10  => X
 7  => VII


There is no need to be able to convert numbers larger than about 3000. (The
Romans themselves didn't tend to go any higher)

Wikipedia says: Modern Roman numerals ... are written by expressing each digit
separately starting with the left most digit and skipping any digit with a
value of zero.

To see this in practice, consider the example of 1990. In Roman numerals, 1990
is MCMXC:

1000=M
900=CM
90=XC

2008 is written as MMVIII:

2000=MM
8=VIII
"""


class RomanNumeral:
    RANGES = {
        100: ("C", "D", "M"),
        10: ("X", "L", "C"),
        1: ("I", "V", "X")
    }

    def __init__(self, decimal: int) -> None:
        self.decimal = decimal

    def to_roman(self) -> str:
        roman = ""
        decimal = self.decimal

        if decimal >= 1000:
            while decimal >= 1000:
                roman += "M"
                decimal -= 1000

        for base in [100, 10, 1]:
            if decimal >= base:
                roman += self.calculate_roman_char(decimal, base)
                decimal %= base

        return roman

    def calculate_roman_char(self, digit: int, base: int) -> str:
        roman_char = ""
        digit = str(digit)[0]
        roman_range = RomanNumeral.RANGES[base]
        base = roman_range[0]
        half = roman_range[1]
        next_numeral = roman_range[2]

        match digit:
            case '9':
                roman_char = base + next_numeral
            case '8':
                roman_char = half + base * 3
            case '7':
                roman_char = half + base * 2
            case '6':
                roman_char = half + base
            case '5':
                roman_char = half
            case '4':
                roman_char = base + half
            case '3':
                roman_char = base * 3
            case '2':
                roman_char = base * 2
            case '1':
                roman_char = base

        return roman_char
