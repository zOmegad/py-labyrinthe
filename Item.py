import random
from random import randrange


class Item:

    def __init__(self):
        self.object = ["A", "B", "C"]

    def place_item(self, my_map):

        for item in self.object:
            # random number to get a list
            random_position_x = random.randint(1, 14)

            # we take a value of the list
            random_index = randrange(
                len(my_map.start_level[random_position_x]))

            # we take the value
            random_item = my_map.start_level[random_position_x][random_index]

            # while the value isn't " " we take another one
            while random_item != " ":
                random_index = randrange(
                    len(my_map.start_level[random_position_x]))
                random_item = my_map.start_level[random_position_x][random_index]

            my_map.start_level[random_position_x][random_index] = item
