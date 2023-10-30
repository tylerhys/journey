from turtle import  Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect Food Collision
    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Detect Wall Collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect Tail Collision
    for seg in snake.segs[1:]:
        if snake.head.distance(seg.position()) < 10:
            game_is_on=False
            scoreboard.game_over()
screen.exitonclick()