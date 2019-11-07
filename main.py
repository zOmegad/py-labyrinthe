import random
from Game import Game
from Map import Map
from Item import Item

my_map = Map()
new_game = Game()
my_items = Item()

my_items.place_items(my_map)
my_map.show_level()

while new_game.finish == False:
    new_game.move(my_map)
    my_map.show_level()

new_game.finished()