import time
import pygame

class Game:

    def __init__(self):

        self.start_time = time.time() # calculer le temps d'éxecution d'une fonction
        self.finish = False

    def play(self, my_map, my_character, my_item):

        my_item.place_item(my_map)
        my_map.place_character(my_character)
        my_map.show_level()
        my_map.start_screen()
        my_map.show_level()

        # tant que game.finish est False
        while not self.finish:
            my_character.direction = input().lower()
            if my_character.direction == "d":
                self.move_right(my_map, my_character, my_item)
            elif my_character.direction == "q":
                self.move_left(my_map, my_character, my_item)
            elif my_character.direction == "z":
                self.move_up(my_map, my_character, my_item)
            elif my_character.direction == "s":
                self.move_down(my_map, my_character, my_item)
            else:
                print("Utilisez Z Q S D")

            my_map.show_level()
            my_character.show_info()

        self.finished(my_character)

    def move_up(self, my_map, my_character, my_item):
        my_character.position["x"] -= 1

        if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":
            print("Impossible d'aller ici")
            my_character.position["x"] +=1

        else:
            if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
            my_map.start_level[my_character.position["x"] + 1][my_character.position["y"]] = " "
            my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body

    def move_down(self, my_map, my_character, my_item):
        my_character.position["x"] += 1

        if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":

            print("Impossible d'aller ici")
            my_character.position["x"] -=1

        else:
            if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
            my_map.start_level[my_character.position["x"] - 1][my_character.position["y"]] = " "
            my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body 

    def move_left(self, my_map, my_character, my_item): 
        my_character.position["y"] -= 1

        if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":
            print("Impossible d'aller ici")
            my_character.position["y"] +=1

        else:
            if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
            my_map.start_level[my_character.position["x"]][my_character.position["y"] + 1] = " "
            my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body
    
    def move_right(self, my_map, my_character, my_item): 
        my_character.position["y"] += 1
        if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":
            print("Impossible d'aller ici")
            my_character.position["y"] -=1
        else:
            if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
            my_map.start_level[my_character.position["x"]][my_character.position["y"] - 1] = " "
            my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body

    def finished(self, my_character):
        if my_character.item_taken != 3:

            print("Vous n'avez pas récupéré tous les items, vous etes mort.")
            print("   _____                         ____                 ")
            print("  / ____|                       / __ \                ")
            print(" | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ")
            print(" | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|")
            print(" | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ")
            print("  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ")
            print("                                                      ")

        else:
            print("Felicitation vous avez finit le labyrinthe en %s secondes." % int(time.time() - self.start_time))