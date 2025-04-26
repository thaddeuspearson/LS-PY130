"""
Write a function build_profile that takes a first name and a last name, and any
number of keyword arguments to add to a user's profile.
"""


def build_profile(first_name: str, last_name: str, **kwargs) -> dict:
    profile = {"first_name": first_name, "last_name": last_name}

    for k, v in kwargs.items():
        profile[k] = v

    return profile


assert build_profile("Max", "Hawkins", location="San Francisco", 
                     field="Software Engineering") == {
    'first_name': 'Max', 
    'last_name': 'Hawkins',
    'location': 'San Francisco',
    'field': 'Software Engineering'
}
