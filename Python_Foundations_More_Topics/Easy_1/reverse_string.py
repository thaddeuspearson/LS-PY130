"""
Use a generator expression to yield each character of a string in reverse
order.
"""

string = "Hola"
rev_string_generator = (c for c in string[::-1])

for c in rev_string_generator:
    print(c)
