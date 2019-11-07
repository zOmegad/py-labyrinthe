import random
from Game import Game
from Map import Map
from items import Item

my_map = Map()
new_game = Game()
my_items = Item()

my_items.place_items(start_level=my_map.start_level)
my_map.show_level()

while new_game.finish == False:
    new_game.move(start_level=my_map.start_level)
    my_map.show_level()

new_game.finished()