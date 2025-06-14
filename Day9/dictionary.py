programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running excepted.",
    "Function": "A piece of code that you can easily call over and over",
    "Loop": "The action of doing something over and over again.",
    sum: "The total of a set of numbers."
}

# key - any data type
# value - any data type

print(programming_dictionary[sum])
print(programming_dictionary["Bug"])

# Adding new items to the dictionary
programming_dictionary["New Key"] = "New Value"
print(programming_dictionary)

# Wipe an existing dictionary
# programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])