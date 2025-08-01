import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.color("blue")
t.shape("turtle")

for x in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


# end
screen.mainloop()
