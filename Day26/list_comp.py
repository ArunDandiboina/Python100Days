# List Comprehension - creating a new list from an existing one
# or any iterable object

# [expression for item in iterable if condition]
# faster loop than a for loop


l = [1, 2, 3]
l_squared = [x**2 for x in l]
print(l_squared)
 
print([x + 1 for x in l])

print([l for l in "Arun"])
print([x * 2 for x in range(1, 6)])

# Using list comprehension with a condition

names = ["Arun", "Radha", "Rajani"]

print([x for x in names if len(x) <= 5])

print([x if len(x) <= 5 else "NO ENTRY" for x in names])