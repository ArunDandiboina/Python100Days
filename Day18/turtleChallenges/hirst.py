import turtle
import colorgram
import random

rgb_colors = []
colors = colorgram.extract("hirst.jpg", 40)  # Extract colors from the image

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))  # Append the RGB tuple to the

turtle.colormode(255)  # Set color mode to 255 for RGB colors
t = turtle.Turtle()
t.speed("fastest")  # Set the turtle speed to the fastest

t.hideturtle()  # Hide the turtle cursor
t.penup()  # Lift the pen to avoid drawingwhile moving
t.goto(-200, -200)  # Move to the starting position

for _ in range(10):
    for _ in range(10):
            t.dot(15, random.choice(rgb_colors))
            t.forward(40)
    t.goto(-200, t.ycor() + 40)  # Move to the next row


# random color from hirst color palette




# end
t.screen.mainloop()