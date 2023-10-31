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
        self.head = self.segs[0]
    
    def create_snake(self):
        for pos in START_POS:
            self.add_seg(pos)
            
    def add_seg(self,pos):
        seg=Turtle("square")
        seg.penup()
        seg.color("white")
        seg.goto(pos)
        self.segs.append(seg)
        
    def extend(self):
        self.add_seg(self.segs[-1].position())

    def move(self):
        for seg in range(len(self.segs)-1,0,-1):
            self.segs[seg].goto(self.segs[seg-1].pos())
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def reset(self):
        for seg in self.segs:
            seg.hideturtle()
        self.segs.clear()
        self.create_snake()
        self.head =self.segs[0]

