from turtle import Turtle

class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.setheading(90)  # Facing up
        self.goto(0, -280)  # Start at the bottom of the screen

    def move_up(self):
        self.forward(10)  # Move forward by 10 units
        
    def move_down(self):
        self.backward(10)
        
    def reset_position(self):
        self.goto(0, -280)