"""
Use map to create a list of lengths of each string in the original list.
"""
strings = ["Oh", "what", "a", "beautiful", "morning"]
str_lengths = list(map(len, strings))

assert list(str_lengths) == [2, 4, 1, 9, 7]
