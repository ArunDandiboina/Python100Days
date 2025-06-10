# loops - for, while, break, continue
# one of the control flow statements
# control flow - go to Day3 for more details.

# for loop - use THONNY for better visualization.
fruits = ['apple', 'banana', 'cherry', 'date']
for fruit in fruits:
    print(fruit)
print(fruits)

# python is best at math, math functions and methods.
l = [5, 4, 9, 1]
print(sum(l))  # sum of all elements in the list
print(max(l))  # maximum element in the list
print(min(l))  # minimum element in the list
print(sorted(l))  # sorted list in ascending order
print(sorted(l, reverse=True))  # sorted list in descending order
print(l)  # original list remains unchanged


# l = [5, 4, 9, 1]
# let find max without using max function
# def maximum(l):
#     max_value = l[0]  # assume first element is the maximum
#     for num in l:
#         if num > max_value:
#             max_value = num  # update max_value if current element is greater
#     return max_value
# print(maximum(l))  # should print 9