from turtle import Turtle

t = Turtle()
t.color("blue")
t.shape("turtle")
t.pensize(5)
# default pen - down

# square
for x in range(4):
    t.forward(100)
    t.right(90)

# end
t.screen.mainloop()