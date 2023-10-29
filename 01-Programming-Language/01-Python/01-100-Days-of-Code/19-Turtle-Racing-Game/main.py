from turtle import Turtle, Screen
import random

end = True
screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:").lower()
colors = ['red','orange','yellow','green','blue','purple']
turtles = []

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=(-100+ i * 30))
    turtles.append(tim)

if user_bet:
    end = False

while not end:
    for turtle in turtles:
        distance = random.randint(0,10)
        turtle.forward(distance)
        
        if turtle.xcor() >=240:
            winner = turtle.fillcolor()
            end = True

if user_bet == winner:
    print("Congratulations! You win!!")
else:
    print(f"Sorry, you lose! The winner is {winner}")

    
screen.exitonclick()