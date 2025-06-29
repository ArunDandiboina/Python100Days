# class - blueprint.
# object - instance of a class.

# we can create multiple objects from a class,
# each with its own state.

import turtle
import random

screen = turtle.Screen()

colors = ["red", "blue", "green", "yellow", "purple"]
turtles = []

# input - allow user to select a color from colors
text = screen.textinput("Choose a color", "Enter a color (red, blue, green, yellow, purple):")
# print(text)
end = turtle.Turtle()
end.hideturtle()

for color in colors:
    t = turtle.Turtle()
    t.shape("turtle")
    t.shapesize(2, 2, 1)  # (stretch_wid, stretch_len, outline)
    t.color(color)
    t.penup()
    t.goto(-300, 200 - len(turtles) * 100)
    turtles.append(t)

def race():
    while True:
            for t in turtles:
                t.forward(random.randint(1, 10))
                if t.xcor() > 300:
                    if t.color()[0] == text:
                        end.write(f"{t.color()[0]} turtle wins!", align="center", font=("Arial", 24, "normal"))
                    else:
                        end.write(f"{t.color()[0]} turtle wins, but you chose {text}!", align="center", font=("Arial", 24, "normal"))
                    return


race()

    
# end
screen.mainloop()