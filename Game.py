import time

class Game:

    def __init__(self):

        self.start_time = time.time() # calculer le temps d'éxecution d'une fonction
        self.finish = False

    def move(self, my_map, my_character, my_item):

        direction = input()
        direction = direction.lower()

        if direction == "d":
            my_character.position["y"] += 1
            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":
                print("Impossible d'aller ici")
                my_character.position["y"] -=1

            else:
                if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
                if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
                my_map.start_level[my_character.position["x"]][my_character.position["y"] - 1] = " "
                my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body

        elif direction == "q":
            my_character.position["y"] -= 1

            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":
                print("Impossible d'aller ici")
                my_character.position["y"] +=1

            else:
                if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
                if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
                my_map.start_level[my_character.position["x"]][my_character.position["y"] + 1] = " "
                my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body

        elif direction == "z":
            my_character.position["x"] -= 1

            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":
                print("Impossible d'aller ici")
                my_character.position["x"] +=1

            else:
                if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
                if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
                my_map.start_level[my_character.position["x"] + 1][my_character.position["y"]] = " "
                my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body

        elif direction == "s":

            my_character.position["x"] += 1

            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":

                print("Impossible d'aller ici")
                my_character.position["x"] -=1

            else:
                if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
                if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
                my_map.start_level[my_character.position["x"] - 1][my_character.position["y"]] = " "
                my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body

        else:

            print("Utilise Z Q S ou D")

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