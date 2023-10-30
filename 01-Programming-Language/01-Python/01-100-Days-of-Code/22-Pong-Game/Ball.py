from turtle import Turtle
START_POS = (0,0)
DISTANCE = 10
START_TRJ = 36.87

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(START_POS)
        self.dy = 10
        self.dx = 10
    
    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.dy *= -1
    
    def bounce_x(self):
        self.dx *= -1

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
        