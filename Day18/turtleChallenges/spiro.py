import turtle
import random

turtle.colormode(255)  # Set color mode to 255 for RGB colors
t = turtle.Turtle()
t.speed("fastest")  # Set the turtle speed to the fastest

def random_color():
    """Generate a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_spirograph(size_of_gap):
    """Draw a spirograph with the given size of gap."""
    for angle in range(0, 360, size_of_gap):
        t.color(random_color())  # Set a random color
        t.setheading(angle)  # Set the heading to the current angle
        t.circle(100)  # Draw a circle with radius 100


# gap = int(input("Enter the degree gap for the spirograph: "))
gap = 5
draw_spirograph(gap)
# end
t.screen.mainloop()