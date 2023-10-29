from turtle import Turtle
START_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segs=[]
        self.create_snake()
    
    def create_snake(self):
        for pos in START_POS:
            seg=Turtle("square")
            seg.penup()
            seg.color("white")
            seg.goto(pos)
            self.segs.append(seg)

    def move(self):
        for seg in range(len(self.segs)-1,0,-1):
            self.segs[seg].goto(self.segs[seg-1].pos())
        self.segs[0].forward(MOVE_DIST)

    def up(self):
        if self.segs[0].heading() != DOWN:
            self.segs[0].setheading(UP)

    def down(self):
        if self.segs[0].heading() != UP:
            self.segs[0].setheading(DOWN)

    def left(self):
        if self.segs[0].heading() != RIGHT:
            self.segs[0].setheading(LEFT)

    def right(self):
        if self.segs[0].heading() != LEFT:
            self.segs[0].setheading(RIGHT)

