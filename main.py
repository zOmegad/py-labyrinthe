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
		start(x_ord)

def start(level):
	print("Bienvenue dans mon labyrinthe, c'est partit : \n")
	enum = 0
	start_level = []
	for line in level:
		x = list(line)
		start_level.insert(enum, x)
		print(''.join(map(str, line)))  # transforme chaques list en string
		enum += 1
	play(start_level)

def play(start_level):
	print("Utilisez Z Q S D pour déplacer votre personage et atteindre la fin du niveau, bonne chance")
	finish = False
	position_x = 0
	position_y = 0
	while finish != True:
		direction = input()
		direction = direction.lower()
		if direction == "d":
			position_y += 1
			if start_level[position_x][position_y] == "#":
				print(position_y)
				print("Impossible d'aller ici")
				position_y -=1
			else:
				if start_level[position_x][position_y] == '=' : finish = True
				start_level[position_x][position_y - 1] = " "
				start_level[position_x][position_y] = "X"
				for line in start_level:
					print(''.join(map(str, line)))  # transforme chaques list en string
		elif direction == "q":
			position_y -= 1
			if start_level[position_x][position_y] == "#":
				print(position_y)
				print("Impossible d'aller ici")
				position_y +=1
			else:
				if start_level[position_x][position_y] == '=' : finish = True
				start_level[position_x][position_y + 1] = " "
				start_level[position_x][position_y] = "X"
				for line in start_level:
					print(''.join(map(str, line)))  # transforme chaques list en string
		elif direction == "z":
			position_x -= 1
			if start_level[position_x][position_y] == "#":
				print(position_y)
				print("Impossible d'aller ici")
				position_x +=1
			else:
				if start_level[position_x][position_y] == '=' : finish = True
				start_level[position_x + 1][position_y] = " "
				start_level[position_x][position_y] = "X"
				for line in start_level:
					print(''.join(map(str, line)))  # transforme chaques list en string
		elif direction == "s":
			position_x += 1
			if start_level[position_x][position_y] == "#":
				print(position_y)
				print("Impossible d'aller ici")
				position_x -=1
			else:
				if start_level[position_x][position_y] == '=' : finish = True
				start_level[position_x - 1][position_y] = " "
				start_level[position_x][position_y] = "X"
				for line in start_level:
					print(''.join(map(str, line)))  # transforme chaques list en string
		else:
			print("Utilise Z Q S ou D")

	finished()

def finished():
	print("Felicitation vous avez finit le labyrinthe")

begin()