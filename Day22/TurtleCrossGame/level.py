from turtle import Turtle

class Level(Turtle):
    def __init__(self, level_number):
        super().__init__()
        self.level_number = level_number
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-290, 290)  # Position at the top of the screen
        self.write(f"Level: {self.level_number}", align="center", font=("Arial", 12, "normal"))
    
    def update_level(self, new_level):
        self.clear()
        self.level_number = new_level
        self.write(f"Level: {self.level_number}", align="center", font=("Arial", 12, "normal"))