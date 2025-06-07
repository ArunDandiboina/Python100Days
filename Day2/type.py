# function - input - instructions - output.
# reusable code - functions

# type errors
a = 10
print(type(a))  # <class 'int'>
# len function expects a sequence type
print(len(str(a)))  # convert int to str and get length

print("")
# type checking
print(type(10))  # <class 'int'>
print(type(10.5))  # <class 'float'>    
print(type("Hello"))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type({1, 2, 3}))  # <class 'set'>
print(type({"key": "value"}))  # <class 'dict'>
print(type(True))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>

print("")
# type conversion
a = "123"
b = int(a)  # convert string to int
print(b)  # 123
print(type(b))  # <class 'int'>


# types from print - (+, f-strings, format)

print(f"your name has {len(input("What is your name? "))} letters")  # f-string