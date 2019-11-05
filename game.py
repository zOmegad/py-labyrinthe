import random

def place_items(start_level):
    items = ["⌘", "♣", "※"]
    for item in items:
        random_position_x = random.randint(1,14)
        random_position_y = random.randint(1,20)
        start_level[random_position_x][random_position_y] = item
    

def show_level(start_level):
    print("\n")
    for line in start_level:
        print(''.join(map(str, line)))  # transforme chaques list en string

def move(start_level, position, finish, edit_pos, direction, suppression):
    if direction == "right_down" : position[edit_pos] += 1
    if direction == "left_up" : position[edit_pos] -= 1
    if start_level[position["x"]][position["y"]] == "#":
        print("Impossible d'aller ici")
        if direction == "right_down" : position[edit_pos] -= 1
        if direction == "left_up" : position[edit_pos] += 1
    else:
        if start_level[position["x"]][position["y"]] == "=" : finish[0] = True
        if suppression == "right":
            start_level[position["x"]][position["y"] - 1] = " "
            start_level[position["x"]][position["y"]] = "X"
        elif suppression == "left":
            start_level[position["x"]][position["y"] + 1] = " "
            start_level[position["x"]][position["y"]] = "X"
        elif suppression == "up":
            start_level[position["x"] + 1][position["y"]] = " "
            start_level[position["x"]][position["y"]] = "X"
        elif suppression == "down":
            start_level[position["x"] - 1][position["y"]] = " "
            start_level[position["x"]][position["y"]] = "X"
        else:
            pass

def play(start_level):
    place_items(start_level)
    print("Utilisez Z Q S D pour déplacer votre personage et atteindre la fin du niveau, bonne chance")
    finish = [False]
    position = {"x": 0, "y": 0}
    while finish[0] == False:
        direction = input()
        direction = direction.lower()
        if direction == "d":
            move(start_level, position, finish, edit_pos="y", direction="right_down", suppression="right")
            show_level(start_level)
        elif direction == "q":
            move(start_level, position, finish, edit_pos="y", direction="left_up", suppression="left")
            show_level(start_level)
        elif direction == "z":
            move(start_level, position, finish, edit_pos="x", direction="left_up", suppression="up")
            show_level(start_level)
        elif direction == "s":
            move(start_level, position, finish, edit_pos="x", direction="right_down", suppression="down")
            show_level(start_level)
        else:
            print("Utilise Z Q S ou D")

    finished()

def finished():
    print("Felicitation vous avez finit le labyrinthe")