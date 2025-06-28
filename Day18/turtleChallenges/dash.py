from turtle import Turtle

t = Turtle()
t.color("blue")
t.shape("turtle")

for x in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


# end
t.screen.mainloop()
