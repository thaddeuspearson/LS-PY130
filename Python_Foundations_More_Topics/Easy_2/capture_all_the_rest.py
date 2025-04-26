"""
Unpack the first two elements from a list and store the remaining elements in 
another list.
"""


numbers = [1, 2, 3, 4, 5, 6]
first, second, *the_rest = numbers

assert first == 1
assert second == 2
assert the_rest == [3, 4, 5, 6]
