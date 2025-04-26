"""
Create a function create_user that takes a username and requires keyword-only
arguments for email and age.
"""


def create_user(username: str, *, email: str, age: str) -> dict:
    return {"username": username, "email": email, "age": age}


try:
    create_user("B", "bob@b.com", "40")
except TypeError:
    assert create_user("B", email="B@b.com", age="40") == {
        "username": "B", "email": "B@b.com", "age": "40"
    }
