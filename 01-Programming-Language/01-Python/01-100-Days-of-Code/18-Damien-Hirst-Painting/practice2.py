from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def draw_dash_line(distance):
    x = int(distance / 10)
    for _ in range(x):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

draw_dash_line(100)


screen = Screen()
screen.exitonclick()