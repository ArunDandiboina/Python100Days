# OOP - Object Oriented Programming.
# A programming paradigm based on 
# the concept of "objects", which
# can contain data and code: data
# in the form of fields (often known 
# as attributes or properties), and code, 
# in the form of procedures (often known as methods).

# class - blueprint for creating objects

# if we write in class we can build a lot of modules
# and packages.

from another_module import another_variable
print(another_variable)

import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
# print shape
# print(timmy.shape())
timmy.color("red")
timmy.forward(100)

screen = turtle.Screen()
screen.exitonclick()