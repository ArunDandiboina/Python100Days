# function - A block of reusable code 
# that performs a specific task.

# some have all/some.
# takes input 
# act
# output.
# takes input - act - output

# built-in
num_char = len("hello")  # len
print(num_char)          # print

# user-defined
# define a function
def my_function():
    print("Hello from a function")

# call a function
my_function()

# indentation - to let python know - 4 spaces.
# that this is a block of code.
# if, else, for, while, def, class

sky = "clear"
def display_sky():
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("grey")
    print("hello")
print("world")

display_sky()