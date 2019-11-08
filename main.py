import random
from Game import Game
from Map import Map
from Item import Item
from Character import Character

my_map = Map()
game = Game()
my_item = Item()
my_character = Character()

my_item.place_item(my_map)
my_map.place_character(my_character)
my_map.show_level()

while game.finish == False:
    game.move(my_map, my_character, my_item)
    my_map.show_level()
    my_character.show_info()

game.finished(my_character)	