import random
import turtle
from tim import Tim
from level import Level
from finish import FinishLine
from car_manager import CarManager

screen = turtle.Screen()
screen.screensize(600, 600)

screen.tracer(0)

tim = Tim()
level = Level(1)
finish_line = FinishLine()
car_manager = CarManager()

screen.update()

screen.onkeypress(tim.move_up, "Up")
screen.onkeypress(tim.move_down, "Down")
screen.listen()

def game_loop():
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    if tim.ycor() > 280:
        tim.reset_position()
        car_manager.increase_speed()
        level.update_level(level.level_number + 1)

    car_manager.delete_cars()
    
    # Check for collisions with cars
    for car in car_manager.cars:
        if tim.distance(car) < 20:
            # game over write 
            game_over_text = turtle.Turtle()
            game_over_text.penup()
            game_over_text.hideturtle()
            game_over_text.write("Game Over", align="center", font=("Arial", 24 , "normal"))
            return
    
    if level.level_number > 5:
        game_win_text = turtle.Turtle()
        game_win_text.penup()
        game_win_text.hideturtle()
        game_win_text.write("You Win!", align="center", font=("Arial", 24 , "normal"))
        return
    
    screen.ontimer(game_loop, 100)  # Update the screen every 100 milliseconds

game_loop()
screen.mainloop()