"""
Given a nested tuple data = ((1, 2), (3, 4), (5, 6)), write a code to unpack
this tuple into individual variables a, b, c, d, e, f.
"""

data = ((1, 2), (3, 4), (5, 6))
(a, b), (c, d), (e, f) = data

assert a == 1
assert b == 2
assert c == 3
assert d == 4
assert e == 5
assert f == 6
