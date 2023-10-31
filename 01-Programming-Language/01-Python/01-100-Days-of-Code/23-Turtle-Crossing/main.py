import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move,"Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if player.ycor() > FINISH_LINE_Y:
        player.refresh()
        scoreboard.increase_score()
        car_manager.reset()
        car_manager.increase_difficulty()

    for car in car_manager.cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()