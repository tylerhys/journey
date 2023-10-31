from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Level: {self.score}",False,ALIGNMENT,FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,ALIGNMENT,FONT)