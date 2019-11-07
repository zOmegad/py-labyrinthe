import random

class Item:
    
    def __init__(self):
        self.items = ["⌘", "♣", "※"]

    def place_items(self, my_map):

        for item in self.items:
            random_position_x = random.randint(1,14)
            random_position_y = random.randint(1,20)
            my_map.start_level[random_position_x][random_position_y] = item