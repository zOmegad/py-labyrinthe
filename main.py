import random
from Game import Game
from Map import Map
from Item import Item
from Character import Character

my_map = Map()
game = Game()
my_item = Item()
my_character = Character()

game.play(my_map, my_character, my_item)