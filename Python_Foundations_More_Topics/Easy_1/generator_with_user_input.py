"""
Create a generator function that yields user input strings until the word
"stop" is entered.
"""


def get_user_input_generator():
    while True:
        i = input("Enter something, or 'stop' to end: ")
        if i.lower() == "stop":
            break
        yield i


user_input = get_user_input_generator()

for u_i in user_input:
    print(u_i)
