import turtle
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

turtle.colormode(255)  # set color mode to 255 for RGB colors
t = turtle.Turtle()
t.pensize(15)
t.speed("fastest")  # fastest speed for turtle

for _ in range(100):
    # t.color(random.choice(colors))
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # random RGB color
    t.forward(random.randint(10, 60))
    t.setheading(random.choice(directions))



#end
t.screen.mainloop()