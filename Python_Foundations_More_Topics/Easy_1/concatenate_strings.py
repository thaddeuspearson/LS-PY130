"""
Use reduce to concatenate a list of strings into a single string.
"""
from functools import reduce

strings = "This", " ", "is", " ", "interesting"
concatenated_strings = reduce(lambda s, t: s + t, strings)

assert concatenated_strings == "This is interesting"
