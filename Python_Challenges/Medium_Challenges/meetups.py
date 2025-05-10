"""
Meetups are a great way to meet people who share a common interest. Typically,
meetups happen monthly on the same day of the week. For example, a meetup's
meeting may be set as:

    The first Monday of January 2021
    The third Tuesday of December 2020
    The teenth Wednesday of December 2020
    The last Thursday of January 2021

In this program, we'll construct objects that represent a meetup date. Each
object takes a month number (1-12) and a year (e.g., 2021). Your object should
be able to determine the exact date of the meeting in the specified month and
year. For instance, if you ask for the 2nd Wednesday of May 2021, the object
should be able to determine that the meetup for that month will occur on the
12th of May, 2021.

The descriptors that may be given are strings:

    'first', 'second', 'third', 'fourth', 'fifth', 'last', and 'teenth'.

The case of the strings is not important; that is, 'first' and 'fIrSt' are
equivalent. Note that "teenth" is a made up word. There was a meetup whose
members realized that there are exactly 7 days that end in '-teenth'.
Therefore, it's guaranteed that each day of the week (Monday, Tuesday, ...)
will have exactly one date that is the "teenth" of that day in every month.
That is, every month has exactly one "teenth" Monday, one "teenth" Tuesday,
etc. The fifth day of the month may not happen every month, but some meetup
groups like that irregularity.

The days of the week are given by the strings:

    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', and
    'Sunday'.

Again, the case of the strings is not important.
"""
from datetime import date


class Meetup:
    OCCURANCES = {
        'first': range(1, 8),
        'second': range(8, 15),
        'third': range(15, 22),
        'fourth': range(22, 29),
        'fifth': range(29, 32),
        'teenth': range(13, 20),
        'last': range(31, 21, -1)
    }

    def __init__(self, year: int, month: int) -> None:
        self.year = year
        self.month = month

    def day(self, day_name: str, occurance: str) -> date:
        occurance_range = Meetup.OCCURANCES[occurance.lower()]

        for day in occurance_range:
            try:
                target_date = date(self.year, self.month, day)
            except ValueError:
                if occurance != 'last':
                    return None
            else:
                if target_date.strftime('%A').lower() == day_name.lower():
                    return target_date
