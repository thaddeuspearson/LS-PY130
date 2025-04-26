"""
Create a function concatenate that takes any number of strings and
concatenates them into a single string with a space in between.
"""


def concatenate(*args) -> str:
    return " ".join(args)


assert concatenate("Launch", "School", "is", "great") == \
    "Launch School is great"
assert concatenate("I", "am", "working", "on", "the", "PY130", "course") == \
    "I am working on the PY130 course"
