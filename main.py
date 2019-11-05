import random
from game import *

def begin(): 
	with open('level.txt', 'r') as level:
		lines = level.readlines()
		print("Bienvenue dans mon labyrinthe, c'est partit : \n")
		enum = 0
		start_level = []
		for line in lines:
			x = list(line)
			x.pop()
			start_level.insert(enum, x)
			enum += 1
		start_level[0][0] = "X"
		show_level(start_level)
	play(start_level)

begin()