"""
Obtain only the even numbers from a list using the filter function.
"""

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

assert even_numbers == [2, 4]
