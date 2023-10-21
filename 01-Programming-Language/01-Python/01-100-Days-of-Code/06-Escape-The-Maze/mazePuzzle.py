# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    turn_right()
    if not front_is_clear():
        turn_left()
        if not front_is_clear():
            turn_left()
        else:
            move()
    else:
        move()