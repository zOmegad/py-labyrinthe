import random
from random import randrange

class Item:
    
    def __init__(self):
        self.object = ["A", "B", "C"]

    def place_item(self, my_map):

        for item in self.object:
            # chiffre aléatoire pour avoir une des listes
            random_position_x = random.randint(1,14)

            # on prend une des valeurs de la liste
            random_index = randrange(len(my_map.start_level[random_position_x]))
            
            # on récupère la valeure
            random_item = my_map.start_level[random_position_x][random_index]

            # tant que la valeur n'est pas " ", on en prend une nouvelle dans la même list
            while random_item != " ":
                random_index = randrange(len(my_map.start_level[random_position_x]))
                random_item = my_map.start_level[random_position_x][random_index]

            # et enfin on remplace la valeur par l'item    
            my_map.start_level[random_position_x][random_index] = item
