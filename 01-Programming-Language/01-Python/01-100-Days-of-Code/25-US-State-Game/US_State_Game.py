import pandas
import turtle

INFILE = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\25-US-State-Game\\50_states.csv"
OUTFILE = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\25-US-State-Game\\states_missed.csv"
IMAGE = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\25-US-State-Game\\blank_states_img.gif"

answers = []
state_missed = []
cnt = 0

# Screen Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# Get Data
data = pandas.read_csv(INFILE)


game_end = False
answer_state = str(screen.textinput(title="Guess the State",prompt="Name a state:")).lower()

while not game_end:
    if answer_state == "exit":
        break

    for state in data["state"]:
        if answer_state == state.lower():
            outstate = turtle.Turtle()
            outstate.hideturtle()
            outstate.penup()
            outstate.goto(data[data.state == state].x.iloc[0],data[data.state == state].y.iloc[0])
            outstate.write(state, align="center",font=("Courier",10,"normal"))

            if not answers.__contains__(answer_state):
                answers.append(answer_state)
                cnt += 1
    
    answer_state = str(screen.textinput(title=f"{cnt}/50 States Correct",prompt="What's another state's name?")).lower()

for state in data["state"]:
    if not answers.__contains__(state.lower()):
        state_missed.append(state)

df = pandas.DataFrame(state_missed)
df.to_csv(OUTFILE)