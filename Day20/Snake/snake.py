from turtle import Turtle, Screen
screen = Screen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_length = 3
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake(self):
        # Initialize the snake body with segments
        for i in range(self.snake_length):
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.penup()
            segment.goto(-20 * i, 0)
            self.snake_body.append(segment)
    
    def move_snake(self):
        # Move the snake body segments
        for i in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[i - 1].xcor()
            y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x, y)

        # Move the head of the snake
        self.snake_body[0].forward(20)
    
    def up(self):
        # Move the snake up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        # Move the snake down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        # Move the snake left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        # Move the snake right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def extend(self):
        # Add a new segment to the snake without showing in the screen
        # invisible first next visible
        segment = Turtle()
        segment.goto(self.snake_body[-1].position())
        segment.color("white")
        segment.shape("square")
        segment.penup()
        self.snake_body.append(segment)
    