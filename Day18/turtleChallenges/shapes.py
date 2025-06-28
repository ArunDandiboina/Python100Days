from turtle import Turtle

t = Turtle()
t.color("blue")
for x in range(3, 9):
    for y in range(x):
        t.forward(100)
        t.right(360 / x)

# end
t.screen.mainloop()