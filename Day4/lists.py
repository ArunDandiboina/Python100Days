# list - collection of items in a particular order
# list is mutable, ordered, allows duplicates
# list can be different data types

l = [1, 2, 3, 4, 5]
print(l)
print(l[0])  # Accessing the first element
print(l[-1])  # Accessing the last element
print(l[1:3])  # Slicing the list from index 1 to 2 (exclusive of 3)

# methods
l.append(6)
print(l)
l.pop()
l.pop(0)  # Removes the first element
print(l)

l.extend([7, 8, 9])
print(l)