from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.new_car()
        self.speed = STARTING_MOVE_DISTANCE


    def new_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
