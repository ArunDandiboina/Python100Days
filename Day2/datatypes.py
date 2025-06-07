# Datatypes - type of data in cpu(ram)
# good code - readable, scalable(space and time)
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

'''
a = "string" # str - immutable. 
print(a[0])
print(a[::-1])  # reverse string

a = 10
print(type(a))  # <class 'int'>
# readable
print(12_345)  # 12345 (12 thousand 345)

a = 10.5
print(type(a))  # <class 'float'>

a = [1, 2, 3]
print(type(a))  # <class 'list'> mutable

a = (1, 2, 3)
print(type(a))  # <class 'tuple'> immutable

print(int("10"))  # convert string to int

# Boolean
a = True
print(type(a))  # <class 'bool'>