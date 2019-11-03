def begin(): 
	with open('level.txt', 'r') as level:
		lines = level.readlines()
		enum = 0
		x_ord = []
		for line in lines:
			x = list(line)
			x.pop() # retire le dernier élément, c'est le \n
			x_ord.insert(enum, x)
			enum += 1
		x_ord[0][0] = "X"
		print("Bienvenue dans mon labyrinthe, c'est partit : \n")
		enum = 0
		start_level = []
		for line in x_ord:
			x = list(line)
			start_level.insert(enum, x)
			print(''.join(map(str, line)))  # transforme chaques list en string
			enum += 1
	play(start_level)


def show_level(level):
	for line in level:
		print(''.join(map(str, line)))  # transforme chaques list en string

def play(start_level):
	print("Utilisez Z Q S D pour déplacer votre personage et atteindre la fin du niveau, bonne chance")
	finish = False
	position = {"x": 0, "y": 0}
	while finish != True:
		print(position["x"])
		print(position["y"])
		direction = input()
		direction = direction.lower()
		if direction == "d":
			position["y"] += 1
			if start_level[position["x"]][position["y"]] == "#":
				print(position["y"])
				print("Impossible d'aller ici")
				position["y"] -= 1
			else:
				if start_level[position["x"]][position["y"]] == '=' : finish = True
				start_level[position["x"]][position["y"] - 1] = " "
				start_level[position["x"]][position["y"]] = "X"
				show_level(start_level)
		elif direction == "q":
			position["y"] -= 1
			if start_level[position["x"]][position["y"]] == "#":
				print("Impossible d'aller ici")
				positionv["y"] += 1
			else:
				if start_level[position["x"]][position["y"]] == '=' : finish = True
				start_level[position["x"]][position["y"] + 1] = " "
				start_level[position["x"]][position["y"]] = "X"
				show_level(start_level)
		elif direction == "z":
			position["x"] -= 1
			if start_level[position["x"]][position["y"]] == "#":
				print("Impossible d'aller ici")
				position["x"] += 1
			else:
				if start_level[position["x"]][position["y"]] == '=' : finish = True
				start_level[position["x"] + 1][position["y"]] = " "
				start_level[position["x"]][position["y"]] = "X"
				show_level(start_level)
		elif direction == "s":
			position["x"] += 1
			if start_level[position["x"]][position["y"]] == "#":
				print("Impossible d'aller ici")
				position["x"] -= 1
			else:
				if start_level[position["x"]][position["y"]] == '=' : finish = True
				start_level[position["x"] - 1][position["y"]] = " "
				start_level[position["x"]][position["y"]] = "X"
				show_level(start_level)
		else:
			print("Utilise Z Q S ou D")

	finished()

def finished():
	print("Felicitation vous avez finit le labyrinthe")

begin()