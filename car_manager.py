from turtle import Turtle
import random
COLORS = ["red", "green", "orange", "blue", "yellow", "purple", "pink", "black"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_new_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            rand_y = random.randint(-240, 240)
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
