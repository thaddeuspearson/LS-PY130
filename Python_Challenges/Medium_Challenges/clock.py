"""
Create a clock that is independent of date.

You should be able to add minutes to and subtract minutes from the time
represented by a given Clock object. Note that you should not mutate Clock
objects when adding and subtracting minutes -- create a new Clock object.

Two clock objects that represent the same time should be equal to each other.

You may not use any built-in date or time functionality; just use arithmetic
operations.
"""


class Clock:
    def __init__(self, hour: int, minute: int) -> None:
        self._hour = hour
        self._minute = minute

    def __str__(self) -> str:
        return f"{self._hour:02d}:{self._minute:02d}"

    def __add__(self, to_add) -> "Clock":
        if not isinstance(to_add, int):
            return NotImplemented
        hour, minute = self._adjust_time(to_add)
        return Clock(hour, minute)

    def __sub__(self, to_subtract) -> "Clock":
        return self.__add__(-to_subtract)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Clock):
            return NotImplemented
        return (
            self._hour == other._hour and
            self._minute == other._minute
        )

    @classmethod
    def at(cls, hour: int, minute: int = 0):
        return cls(hour, minute)

    def _adjust_time(self, delta: int) -> tuple:
        total_minutes = self._hour * 60 + self._minute + delta
        total_minutes %= 24 * 60
        hours, minutes = divmod(total_minutes, 60)
        return hours, minutes
