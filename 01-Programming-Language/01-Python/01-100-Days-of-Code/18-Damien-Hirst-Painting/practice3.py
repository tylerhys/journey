from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def draw_shape():
    for x in range(3,11):
        timmy.pencolor(randint(1,255),randint(1,255),randint(1,255))
        for i in range(x):    
            timmy.forward(100)
            timmy.right(360/x)

draw_shape()

screen = Screen()
print(screen.colormode())
screen.exitonclick()