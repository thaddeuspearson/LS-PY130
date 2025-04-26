"""
Unpack values from a tuple of four elements, but only keep the first and last
values.
"""


data = (100, 200, 300, 400)
front, *_, back = data

assert front == 100
assert _ == [200, 300]
assert back == 400
