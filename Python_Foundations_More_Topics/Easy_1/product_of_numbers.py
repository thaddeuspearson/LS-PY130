"""
Calculate the product of all numbers in a list using the reduce function.
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda n, p: n*p, numbers, 1)

assert product == 120
