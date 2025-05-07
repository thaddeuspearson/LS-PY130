"""
Write a program that will take a string of digits and return all the possible
consecutive number series of a specified length in that string.

For example, the string "01234" has the following 3-digit series:

    012
    123
    234

Likewise, here are the 4-digit series:

    0123
    1234

Finally, if you ask for a 6-digit series from a 5-digit string, you should
throw an error.
"""


class Series:
    def __init__(self, series_str: str) -> None:
        self.series = series_str

    def slices(self, slice_len: int) -> list[list[int]]:
        if slice_len > len(self.series):
            raise ValueError("Slice cannot be longer than then series")

        return [
            [int(n) for n in self.series[idx: idx + slice_len]]
            for idx in range(0, len(self.series) - slice_len + 1)
        ]
