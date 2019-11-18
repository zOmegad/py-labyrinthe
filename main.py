from Game import Game
from Map import Map
from Item import Item
from Character import Character
from DisplayMap import DisplayMap

my_map = Map()
game = Game()
my_item = Item()
my_character = Character()
display_map = DisplayMap()

game.play(my_map, my_character, my_item, display_map)