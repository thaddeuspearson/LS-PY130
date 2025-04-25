"""
Use nested generator expressions to create a flat list of numbers from a list
of lists.
"""

list_of_lists = [[8], [9], [1, 2, 3]]

flat_list = list(n for sub_list in list_of_lists for n in sub_list)

assert flat_list == [8, 9, 1, 2, 3]
