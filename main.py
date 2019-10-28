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
	for line in level:
		print(''.join(map(str, line)))  # transforme chaque list en string

begin()