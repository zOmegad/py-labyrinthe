import pygame
from pygame.locals import *

class Game:

    def __init__(self):

        self.finish = False

    def play(self, my_map, my_character, my_item):

        my_item.place_item(my_map)
        my_map.place_character(my_character)
        my_map.show_level(my_character)
        my_map.start_screen()

        # tant que game.finish est False
        while not self.finish:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    self.move_right(my_map, my_character, my_item)
                elif event.type == KEYDOWN and event.key == K_LEFT:
                    self.move_left(my_map, my_character, my_item)
                elif event.type == KEYDOWN and event.key == K_UP:
                    self.move_up(my_map, my_character, my_item)
                elif event.type == KEYDOWN and event.key == K_DOWN:
                    self.move_down(my_map, my_character, my_item)
                elif event.type == KEYDOWN and event.key == K_q:
                    pygame.quit()
                else:
                    pass

            my_map.show_level(my_character)

        my_map.finished(my_character)

    def move_up(self, my_map, my_character, my_item):
        my_character.position["x"] -= 1

        if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":
            my_character.position["x"] +=1

        else:
            if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
            my_map.start_level[my_character.position["x"] + 1][my_character.position["y"]] = " "
            my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body

    def move_down(self, my_map, my_character, my_item):
        my_character.position["x"] += 1

        if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":
            my_character.position["x"] -=1

        else:
            if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
            my_map.start_level[my_character.position["x"] - 1][my_character.position["y"]] = " "
            my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body 

    def move_left(self, my_map, my_character, my_item): 
        my_character.position["y"] -= 1

        if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":
            my_character.position["y"] +=1

        else:
            if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
            my_map.start_level[my_character.position["x"]][my_character.position["y"] + 1] = " "
            my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body
    
    def move_right(self, my_map, my_character, my_item): 
        my_character.position["y"] += 1
        if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == "#":
            my_character.position["y"] -=1
        else:
            if any(my_map.start_level[my_character.position["x"]][my_character.position["y"]] in s for s in my_item.object) : my_character.item_taken += 1
            if my_map.start_level[my_character.position["x"]][my_character.position["y"]] == '=' : self.finish = True
            my_map.start_level[my_character.position["x"]][my_character.position["y"] - 1] = " "
            my_map.start_level[my_character.position["x"]][my_character.position["y"]] = my_character.body

    