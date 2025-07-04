from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(x_position, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 250:  # Prevent paddle from going out of bounds
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -240:  # Prevent paddle from going out of bounds
            self.goto(self.xcor(), new_y)