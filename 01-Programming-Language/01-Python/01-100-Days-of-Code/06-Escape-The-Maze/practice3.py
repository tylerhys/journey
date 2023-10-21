# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def jump():
    i = 0
    turn_left()
    while wall_on_right():
        move()
        i += 1
    turn_right()
    move()
    turn_right()
    for y in range(i):
        move()
    turn_left()
   
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()