from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def draw_square():
    for _ in range(4):    
        timmy.forward(100)
        timmy.right(90)

draw_square()


screen = Screen()
screen.exitonclick()