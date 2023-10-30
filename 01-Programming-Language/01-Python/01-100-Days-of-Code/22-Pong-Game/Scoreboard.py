from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.show_score()
    
    def show_score(self):
        self.clear()
        self.goto(-120,200)
        self.write(self.l_score, align="center",font=("Courier",70,"normal"))
        self.goto(120,200)
        self.write(self.r_score, align="center",font=("Courier",70,"normal"))

    def l_point(self):
        self.l_score += 1
        self.show_score()

    def r_point(self):
        self.r_score += 1
        self.show_score()
