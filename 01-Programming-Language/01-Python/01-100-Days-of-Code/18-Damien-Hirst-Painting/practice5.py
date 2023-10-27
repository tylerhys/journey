from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(2)
timmy.speed("fastest")

def spirograph(gap):
    for _ in range(int(360/gap)):
        timmy.pencolor(randint(1,255),randint(1,255),randint(1,255))   
        timmy.circle(100)
        timmy.setheading(timmy.heading()+gap)


spirograph(1)

screen = Screen()
screen.screensize(100,100)
screen.exitonclick()