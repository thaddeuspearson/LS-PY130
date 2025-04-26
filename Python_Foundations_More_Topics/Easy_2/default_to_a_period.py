"""
Create a function greet that takes three arguments: a name, a greeting, and a
punctuation mark, with the punctuation defaulting to a period.
"""


def greet(name: str, greeting: str, punctuation_mark: str = ".") -> str:
    return f"{greeting}, {name}{punctuation_mark}"


assert greet("Bob", "Howdy", "!") == "Howdy, Bob!"
