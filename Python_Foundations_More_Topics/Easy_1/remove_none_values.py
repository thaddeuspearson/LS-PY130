"""
Remove all None values from a list using the filter method.
"""

nones = [None, None, None, None, "None"]

no_nones = list(filter(lambda n: n is not None, nones))

assert no_nones == ["None"]
