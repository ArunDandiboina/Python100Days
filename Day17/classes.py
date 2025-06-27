class User:
    pass

user_1 = User()

print(type(user_1))

# PascalCase is used for classes names.

# Attributes are variables that belong to a object.

# It is similar to dictionary and object in javaScript.

# user_1.id = 1
# user_1.username = "john_doe"

# print(user_1.id)

# but more attributes - more typing.
# so use blueprint for classes. a base class.

# constructor is a special method that is called
# when an object is created.

class User:
    def __init__(self, id, username, followers=0):
        self.id = id
        self.username = username
        self.followers = followers

user_1 = User(1, "john_doe")
print(user_1.username)
print(user_1.followers)
        
# Attributes - objects has - variables
# Methods - objects can do - functions
# Datastructures + Algorithms

# self is a reference to the current object.

