class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
        
user_1 = User(1, "john_doe")
user_2 = User(2, "jane_doe")

user_1.follow(user_2)

print(user_1.followers)  # Output: 0
print(user_1.following)  # Output: 1
print(user_2.followers)  # Output: 1
print(user_2.following)  # Output: 0