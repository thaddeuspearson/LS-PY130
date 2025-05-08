"""
Write a program that manages robot factory settings.

When robots come off the factory floor, they have no name. The first time you
boot them up, a random name is generated, such as RX837 or BC811.

Every once in a while, we need to reset a robot to its factory settings, which
means that their name gets wiped. The next time you ask, it will respond with
a new random name.

The names must be random; they should not follow a predictable sequence.
Random names means there is a risk of collisions. Your solution should not
allow using the same name twice.
"""
from random import choices


class Robot:
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    CHAR_COUNT = 2
    DIGIT_COUNT = 3
    names = set()

    def __init__(self) -> None:
        self.name = None
        self.reset()

    @classmethod
    def generate_name(cls) -> str:
        letters = ''.join(choices(cls.CHARS, k=cls.CHAR_COUNT))
        numbers = ''.join(choices(cls.DIGITS, k=cls.DIGIT_COUNT))
        return letters + numbers

    def reset(self) -> None:
        if self.name:
            self.__class__.names.discard(self.name)

        while not self.name:
            candidate = self.__class__.generate_name()
            if candidate not in self.__class__.names:
                self.__class__.names.add(candidate)
                self.name = candidate

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str | None) -> None:
        self._name = name
