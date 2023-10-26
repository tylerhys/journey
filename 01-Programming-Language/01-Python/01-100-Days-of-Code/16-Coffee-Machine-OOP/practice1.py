# import turtle

from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("yellow")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()