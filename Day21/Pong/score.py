from turtle import Turtle

class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Courier", 20, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()