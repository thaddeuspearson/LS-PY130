"""
Write a function display_info that takes a positional-only parameter data, and
keyword-only parameters reverse and uppercase.
"""


def display_info(data: str, /, *, reverse: bool = False,
                 uppercase: bool = False) -> str:
    if reverse:
        data = data[::-1]
    if uppercase:
        data = data.upper()
    return data


assert display_info("Launch", reverse=True) == "hcnuaL"
assert display_info("School", uppercase=True) == "SCHOOL"
assert display_info("cat", uppercase=True, reverse=True) == "TAC"
