from turtle import Turtle
PATH = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\20,21-Snake-Game\\data.txt"
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(open(PATH).read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}",False,ALIGNMENT,FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",False,ALIGNMENT,FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        with open(PATH,mode="w") as file:
            file.write(str(self.highscore))
    
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

