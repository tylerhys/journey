from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",False,ALIGNMENT,FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}",False,ALIGNMENT,FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",False,ALIGNMENT,FONT)
