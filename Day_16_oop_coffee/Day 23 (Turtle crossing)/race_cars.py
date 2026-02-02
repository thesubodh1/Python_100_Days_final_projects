import random
import time
from turtle import Turtle

COLORS = ["red","green","pink","yellow","white"]
MOVE_INCREMENT = 10

class RaceCars:
    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_INCREMENT

    def create_cars(self):
        random_num = random.randint(1,10)
        if random_num == 6 or random_num == 4:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_len=4,stretch_wid=1.5)
            new_car.color(random.choice(COLORS))
            new_car.goto(380,random.randint(-280,280))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 10



