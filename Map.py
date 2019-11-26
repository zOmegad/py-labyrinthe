import pygame
from pygame.locals import *


class Map:

    def __init__(self):

        pygame.init()
        pygame.font.init()
        self.start_level = []
        self.mc_gyver_position = {"x": 0, "y": 0}
        self.fenetre = pygame.display.set_mode((450, 450))
        self.background = pygame.image.load(
            "ressource/background.jpg").convert()
        self.myfont = pygame.font.Font('ressource/Minecraftia-Regular.ttf', 17)
        self.myfont_minecrafter = pygame.font.Font(
            'ressource/Minecrafter.Reg.ttf', 60)
        self.start_image = pygame.image.load(
            "ressource/startscreen450.jpg").convert()
        self.fond = pygame.image.load("ressource/fond.jpg").convert()
        self.mcgyver = pygame.image.load(
            "ressource/MacGyver.png").convert_alpha()
        self.mur = pygame.image.load("ressource/mur.jpg").convert()
        self.arrivee = pygame.image.load("ressource/arrive.jpg").convert()
        self.bitcoin = pygame.image.load(
            "ressource/bitcoin.png").convert_alpha()

        with open('level.txt', 'r') as level:
            lines = level.readlines()
            print("Program launched")
            enum = 0
            for line in lines:
                x = list(line)
                x.pop()
                self.start_level.insert(enum, x)
                enum += 1

    def place_character(self, my_character):
        self.start_level[0][0] = my_character.body

    def show_level(self, my_character):
        # for each list we take the value and we check if it's a wall or not
        # if it is, we add it to the map as the position given
        y_line = 0
        self.fenetre.blit(self.fond, (0, 0))
        for items in self.start_level:
            x_line = 0  # on remet l'abscisse à 0
            for item in items:
                if item == "#":
                    self.fenetre.blit(self.mur, (x_line, y_line))
                elif item == "X":
                    self.fenetre.blit(self.mcgyver, (x_line, y_line))
                elif item == "=":
                    self.fenetre.blit(self.arrivee, (x_line, y_line))
                elif item == "A" or item == "B" or item == "C":
                    self.fenetre.blit(self.bitcoin, (x_line, y_line))
                else:
                    pass
                x_line += 30  # pixels
            y_line += 30

        # show info at the bottom
        info_bar = self.myfont.render('Lives = ' + str(my_character.live) +
                                      "             Items : " + str(my_character.item_taken), False, (255, 255, 255))
        self.fenetre.blit(info_bar, (20, 420))

        pygame.display.flip()

    def start_screen(self):

        self.fenetre.blit(self.start_image, (0, 0))
        textsurface = self.myfont.render(
            'Press any key to start', False, (237, 156, 17))
        text_surface_rect = textsurface.get_rect(center=(450/2, 300))
        self.fenetre.blit(textsurface, text_surface_rect)
        pygame.display.flip()
        ok = False
        while not ok:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    ok = True

    def finished(self, my_character):

        close = False
        while not close:
            if my_character.item_taken != 3:
                self.fenetre.blit(self.background, (0, 0))
                go_message = self.myfont.render(
                    "You didn't collect all bitcoins", False, (255, 255, 255))
                go_message_rect = go_message.get_rect(center=(450/2, 300))
                self.fenetre.blit(go_message, go_message_rect)
                textsurface = self.myfont_minecrafter.render(
                    'GAME OVER', False, (237, 156, 17))
                self.fenetre.blit(textsurface, (40, 170))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        close = True

            else:
                self.fenetre.blit(self.background, (0, 0))
                gg_message = self.myfont_minecrafter.render(
                    "GG WP", False, (255, 255, 255))
                gg_message_rect = gg_message.get_rect(center=(450/2, 170))
                self.fenetre.blit(gg_message, gg_message_rect)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        close = True
