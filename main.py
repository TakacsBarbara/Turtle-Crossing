import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

turtle = Player()

screen.listen()
screen.onkeypress(turtle.move, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_new_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle.is_at_finish():
        turtle.go_to_start()
        car_manager.speed_up()
        scoreboard.increment_level()


screen.exitonclick()
