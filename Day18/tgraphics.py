from turtle import Turtle

# documentation - https://docs.python.org/3/library/turtle.html

t = Turtle()

# pencolor, fillcolor - methods. or
# direct - color(pencolor, fillcolor)
# if one color is given, it is the pencolor
# and the fillcolor is set to the same value.

t.shape("turtle")
t.color('red', "blue") 
# from tkcolor string specification string.
# tk - tkinter - python GUI library.
# gui - graphical user interface.
# first - mac os, second - windows, third - linux.

# turtle colors - https://trinket.io/docs/colors
t.pensize(5)
t.pendown()
t.forward(100)
t.right(90)
t.penup()


# bottom.
# t.screen.title('Object-oriented turtle demo')
# t.screen.bgcolor("orange")
t.screen.mainloop()