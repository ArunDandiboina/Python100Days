# how to modify global variables in a function

# BEST PRACTICE:
# It is generally not a good practice to modify global variables inside functions.
# INSTEAD of accessing global variable in function, 
# we can pass it as an argument to the function

# Global scope
total_enemies = 0

def increase_enemies(enemy):
    return enemy + 1

total_enemies = increase_enemies(total_enemies)
# you can call it as many times as you want

print(f"Total enemies: {total_enemies}")