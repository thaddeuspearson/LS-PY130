"""
Create a list where each number from the original list is squared using the
map method.
"""

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda n: n**2, numbers))

assert squared_numbers == [1**2, 2**2, 3**2, 4**2, 5**2]
