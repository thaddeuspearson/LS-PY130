"""
Create a generator function that yields numbers from 1 to 5.
"""


def one_through_five_generator():
    for n in range(1, 6):
        yield n


one_through_five = one_through_five_generator()

for n in range(1, 6):
    assert next(one_through_five) == n
