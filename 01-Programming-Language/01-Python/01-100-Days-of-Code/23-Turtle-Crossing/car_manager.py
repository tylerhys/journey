from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
STARTING_GEN_CHANCE = 8
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self) -> None:
        self.cars=[]
        self.move_distance = STARTING_MOVE_DISTANCE
        self.gen_chance = STARTING_GEN_CHANCE

    def create_car(self):
        random_chance = randint(1,self.gen_chance)
        if random_chance == 1:
            newcar = Turtle()
            newcar.shape("square")
            newcar.shapesize(stretch_wid=1,stretch_len=2)
            newcar.color(choice(COLORS))
            newcar.penup()
            newcar.goto(300,randint(-250,250))
            newcar.setheading(180)
            self.cars.append(newcar)

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)
    
    def increase_difficulty(self):
        if self.move_distance < 50:
            self.move_distance += MOVE_INCREMENT
        
        if self.gen_chance > 4 and self.move_distance%2 == 0:
            self.gen_chance -= 1

    def reset(self):
        for car in self.cars:
            car.hideturtle()
        self.cars=[]    