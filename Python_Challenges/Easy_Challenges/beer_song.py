"""
Write a program that can generate the lyrics of the 99 Bottles of Beer song.
See the test suite for the entire song.
"""


class BeerSong:
    @classmethod
    def verse(cls, num: int) -> str:
        if num:
            return (
                f"{num} bottle{'s' if num != 1 else ''} of beer on the "
                f"wall, {num} bottle{'s' if num != 1 else ''} of beer.\n"
                f"Take {"one" if num != 1 else "it"} down and pass it "
                f"around, {num - 1 if num - 1 > 0 else "no more"} bottle"
                f"{'s' if num - 1 != 1 else ''} of beer on the wall.\n"
            )
        return (
            "No more bottles of beer on the wall, no more bottles of "
            "beer.\nGo to the store and buy some more, 99 bottles of "
            "beer on the wall.\n"
        )

    @classmethod
    def verses(cls, start: int, end: int) -> str:
        verses = []

        for num in range(start, end - 1, -1):
            verses.append(cls.verse(num))

        return "\n".join(verses)

    @classmethod
    def lyrics(cls) -> str:
        return cls.verses(99, 0)
