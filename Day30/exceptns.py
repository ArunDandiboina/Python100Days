# try except, else and finally blocks
# errors and exception

# try - this block of code will be executed
# except - if an error occurs, this block of code will be executed  
# else - if no error occurs, this block of code will be executed
# finally - this block of code will always be executed, regardless of whether an error occurs or not


# new_file.txt
d = {1: "one", 2: "two", 3: "three"}

try:
    print(d[4])  # This will raise a KeyError
except KeyError as e:
    print(f"KeyError: {e} - The key does not exist in the dictionary.")
    

# Raise an exception
# raise ValueError("This is a custom error message.")
try:
    raise ValueError("This is a custom error message.")
except ValueError as e:
    print(f"ValueError: {e}")
    

# bmi - raise an exception if the height > 3 or height < 0

