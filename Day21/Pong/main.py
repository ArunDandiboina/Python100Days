import turtle
from paddle import Paddle
from ball import Ball
from score import Score

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Ping Pong")
screen.tracer(0)

# paddles
left_paddle = Paddle(-280)
right_paddle = Paddle(272)
left_score = Score(-100, 260)  # Left paddle score
right_score = Score(100, 260)  # Right paddle score
ball = Ball()

# screen.update()
# Bind keys to paddle movements
screen.onkeypress(left_paddle.go_up, "w")  # Move left paddle up
screen.onkeypress(left_paddle.go_down, "s")  # Move left paddle down
screen.onkeypress(right_paddle.go_up, "Up")  # Move right paddle up
screen.onkeypress(right_paddle.go_down, "Down")  # Move right paddle down
screen.listen()


def game_loop():
    ball.move()  # Move the ball
    screen.update()  # Update the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.xcor() > 254 and ball.distance(right_paddle) < 70) or (ball.xcor() < -260 and ball.distance(left_paddle) < 70):
        ball.bounce_x()
    if ball.xcor() > 290 or ball.xcor() < -290:
        if ball.xcor() > 290:
            left_score.increase_score()
        else:
            right_score.increase_score()
        ball.goto(0, 0)
        ball.bounce_x()
    screen.ontimer(game_loop, 100)  # Call game_loop every 20 milliseconds

game_loop()
# end
screen.mainloop()  