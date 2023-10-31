from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10



class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)

    
