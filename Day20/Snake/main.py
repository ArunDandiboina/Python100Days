import turtle
from snake import Snake  # Assuming you have a snake.py file with the Snake class

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)  # Turn off the screen updates for performance

snake = Snake()  # Create an instance of the Snake class

screen.onkey(snake.up, "Up")  # Bind the up arrow key to move the snake up
screen.onkey(snake.down, "Down")  # Bind the down arrow key to move
screen.onkey(snake.left, "Left")  # Bind the left arrow key to move the snake left
screen.onkey(snake.right, "Right")  # Bind the right arrow key to move the snake right
screen.listen()  # Listen for keyboard inputs

def game_loop():
    snake.move_snake()  # Move the snake
    screen.update()
    screen.ontimer(game_loop, 100)  # Call game_loop every 100 milliseconds
    
# Start the game loop
game_loop()


screen.mainloop()  # Keep the window open