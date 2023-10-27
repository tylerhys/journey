import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

rgb = []
colors = colorgram.extract('01-Programming-Language\\01-Python\\01-100-Days-of-Code\\18-Damien-Hirst-Painting\\img.jpg', 10)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb.append(new_color)

colormode(255)

timmy = Turtle("classic")
timmy.shape()
timmy.pensize(2)
timmy.speed("fastest")

def draw_circle(move):
    timmy.forward(move * 60)
    timmy.pendown()
    timmy.setheading(0)

    for _ in range(10):
        color_picked=choice(rgb)
        timmy.pencolor(color_picked)
        timmy.fillcolor(color_picked)
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(60)
        timmy.pendown()
    
    timmy.penup()
    timmy.home()

for move in range(0,11):
    draw_circle(move)
    timmy.setheading(90)

screen = Screen()
screen.exitonclick()
    