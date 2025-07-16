# Python Typing - Type Hints and Arrows
# It is a good practice to use type hints in Python 
# to indicate the expected types of function arguments and return values.


def print_age(age: int) -> None:
    """Prints the age."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    print(f"Age: {age}")

# print_age('a') 
# This will raise a TypeError because 'a' is not an integer.

print_age(30)