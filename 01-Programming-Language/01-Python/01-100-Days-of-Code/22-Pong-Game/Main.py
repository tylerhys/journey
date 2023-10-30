from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

# Screen Setup
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

screen.listen()

# Scoreboard Setup
scoreboard = Scoreboard()

# Paddle Setup
paddle_l = Paddle(-350)
paddle_r = Paddle(350)


screen.onkey(paddle_l.moveup,"w")
screen.onkey(paddle_l.movedown,"s")

screen.onkey(paddle_r.moveup,"Up")
screen.onkey(paddle_r.movedown,"Down")

# Ball Setup
ball = Ball()
speed = 0.1


# Game Setup
game_is_on = True
while game_is_on:
    
    time.sleep(speed)
    screen.update()
    ball.move()

    #Detect Wall Collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect Paddle Collision
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if speed == 0.02:
            pass
        else:
            speed *= 0.8
    
    #Detect Ball Miss
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
        speed = 0.1
    elif ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()
        speed = 0.1


    








screen.exitonclick()