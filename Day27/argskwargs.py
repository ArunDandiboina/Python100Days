# *args - positional arguments
# **kwargs - keyword arguments

def add(*args):
    print(args)

def print_info(**kwargs):
    kwargs['name'] = kwargs.get('name') or "Unknown"
    print(kwargs)
    
# default values
def greet(name="Guest", age=0):
    print(f"Hello {name}, you are {age} years old.")

# args - tuple of positional arguments
# kwargs - dictionary of keyword arguments

# 1 arg + kwargs

def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


add(1, 2, 3, 4)
print_info(name="Arun", age=30, city="New York")
greet()
greet(name="Bob", age=25)
print(calculate(2, add=3, multiply=5))  # Output: 25

# d.get() if key not found, return None
# d.get('key', default_value) if key not found, return default_value