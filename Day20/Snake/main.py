import turtle
from snake import Snake  # Assuming you have a snake.py file with the Snake class
from food import Food  # Assuming you have a food.py file with the Food class
from score import Score  # Assuming you have a score.py file with the Score class

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)  # Turn off the screen updates for performance

snake = Snake()  # Create an instance of the Snake class
food = Food()  # Create an instance of the Food class
score = Score()  # Create an instance of the Score class

screen.onkey(snake.up, "Up")  # Bind the up arrow key to move the snake up
screen.onkey(snake.down, "Down")  # Bind the down arrow key to move
screen.onkey(snake.left, "Left")  # Bind the left arrow key to move the snake left
screen.onkey(snake.right, "Right")  # Bind the right arrow key to move the snake right
screen.listen()  # Listen for keyboard inputs

def game_over():
    for segment in snake.snake_body:
        segment.color("gray")
    # Fade food
    food.color("gray")
    
    score.reset()  # Reset the score
    game_over_text = turtle.Turtle()
    game_over_text.hideturtle()
    game_over_text.color("white")
    game_over_text.penup()
    game_over_text.goto(0, 0)
    game_over_text.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

    screen.update()  # Update the screen

def game_loop():
    snake.move_snake()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 290 or snake.head.xcor() < -290 or
        snake.head.ycor() > 290 or snake.head.ycor() < -290
    ):
        game_over()
        return
        

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_over()
            return

    screen.update()
    screen.ontimer(game_loop, 100)  # Call game_loop every 100 milliseconds
    
# Start the game loop
game_loop()


screen.mainloop()  # Keep the window open