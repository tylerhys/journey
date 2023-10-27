from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(10)
timmy.speed(10)

def random_walk():
    while True:
        timmy.pencolor(randint(1,255),randint(1,255),randint(1,255))   
        timmy.forward(50)
        angle = 90 * randint(1,4)
        timmy.right(angle)
        print(angle)


random_walk()

screen = Screen()
screen.exitonclick()