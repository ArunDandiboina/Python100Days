# functions without input
# def greet():
#     print("hello")

# greet()

# functions with input
# def greet(name):
#     print(f"Hello {name}!")

# greet("Arun")

# functions with multiple input

# position arguments
def greet_with(name, location):
    print(f"{name}")
    print(f"What is it like in {location}")

greet_with("Arun", "Eluru")

# keyword arguments
def greet_with(name, location):
    print(f"{name}")
    print(f"What is it like in {location}")

greet_with(location="Eluru", name="Arun")

"X".upper()  # Convert to uppercase