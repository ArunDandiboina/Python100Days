from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 10
STARTING_MOVE_DISTANCE = 5

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.probability = 6  # Probability of creating a car (1 in 6)

    def create_car(self):
        if random.randint(1, self.probability) == 1:  # Randomly create a car
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            y_position = random.randint(-240, 240)
            new_car.goto(300, y_position)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def increase_speed(self):
        """Increase the speed of the cars."""
        
        self.move_distance += MOVE_DISTANCE
        self.probability -= 1  # Decrease the probability of creating a car
    
    def delete_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                # destroy turtle
                car.hideturtle()
                self.cars.remove(car)
    
