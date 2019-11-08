import random

class Item:
    
    def __init__(self):
        self.object = ["⌘", "♣", "※"]

    def place_item(self, my_map):

        for item in self.object:
            random_position_x = random.randint(1,14)
            random_position_y = random.randint(1,20)
            i = False
            while i == False:
                if my_map.start_level[random_position_x][random_position_y] == " ":
                    my_map.start_level[random_position_x][random_position_y] = item
                    i = True
                elif my_map.start_level[random_position_x][random_position_y] == "#" and random_position_x < 14 and random_position_y < 20:
                    random_position_x += 1
                    if my_map.start_level[random_position_x][random_position_y] == "#" and random_position_x < 14 and random_position_y < 20:
                        random_position_y += 1
                    else:
                        my_map.start_level[random_position_x][random_position_y] = item
                        i = True