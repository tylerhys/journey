from turtle import Turtle
MOVE_DIST = 20

class Paddle(Turtle,):
    def __init__(self,x_pos) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.x_pos = x_pos
        self.goto(x_pos,0)
        

    def moveup(self):
        new_y = self.ycor() + MOVE_DIST
        self.setpos((self.x_pos,new_y))
    
    def movedown(self):
        new_y = self.ycor() - MOVE_DIST
        self.setpos((self.x_pos,new_y))


