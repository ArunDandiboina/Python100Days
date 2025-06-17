# Global scope
total_pizzas = 0

def order_pizza(count):
    price = count * 100  # Local scope
    print(f"Price: {price}")
    global total_pizzas  # Accessing global variable
    total_pizzas += count  # Modifying global variable

order_pizza(3)
order_pizza(2)
print(f"Total pizzas ordered: {total_pizzas}")


# in Javascript, global keyword is not required 
# but in Python, we need to use the global keyword 
# to modify a global variable inside a function.


# no block scope in Python
print("")
if True:
    local_var = "I am local to this block"
    print(local_var)

print(f"Local variable outside block: {local_var}")