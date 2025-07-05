from turtle import Turtle

# a finish line at 280
class FinishLine(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("green")
        self.pensize(2)
        self.goto(-300, 280)  # Position at the top of the screen
        self.setheading(0)  # Facing right
        self.pendown()
        self.forward(600)  # Draw a line across the screen
        self.penup()
    