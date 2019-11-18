import pygame
import time

class Map:

    def __init__(self):

        pygame.init()
        self.mc_gyver_position = {"x": 0, "y": 0}
        self.fenetre = pygame.display.set_mode((450, 450))
        self.start_image = pygame.image.load("ressource/startscreen450.jpg").convert()
        self.fond = pygame.image.load("ressource/fond.jpg").convert()
        self.mcgyver = pygame.image.load("ressource/MacGyver.png").convert_alpha()
        self.mur = pygame.image.load("ressource/mur.jpg").convert()
        self.arrivee = pygame.image.load("ressource/arrive.jpg").convert()
        self.bitcoin = pygame.image.load("ressource/bitcoin.png").convert_alpha()

        self.start_level = []

        with open('level.txt', 'r') as level:
            lines = level.readlines()
            print("Bienvenue dans mon labyrinthe, c'est partit : \n")
            enum = 0
            for line in lines:
                x = list(line)
                x.pop()
                self.start_level.insert(enum, x)
                enum += 1

    def place_character(self, my_character):
        self.start_level[0][0] = my_character.body

    def show_level(self):
        print("\n")
        for line in self.start_level:
            print(''.join(map(str, line)))

        # Pour chaques lists on prend les valeurs et on vérifie si c'est un mur ou non
        y_line = 0
        self.fenetre.blit(self.fond, (0,0))
        for items in self.start_level:
            x_line = 0 # on remet l'abscisse à 0
            for item in items:
                if item == "#":
                    self.fenetre.blit(self.mur, (x_line,y_line))
                elif item == "X":
                    self.fenetre.blit(self.mcgyver, (x_line,y_line))
                elif item == "=":          
                    self.fenetre.blit(self.arrivee, (x_line,y_line))
                elif item == "A" or item == "B" or item == "C":
                    self.fenetre.blit(self.bitcoin, (x_line,y_line))
                else:
                    pass
                x_line += 30 # pixels
            y_line += 30
        pygame.display.flip()

    def start_screen(self):

        self.fenetre.blit(self.start_image, (0,0))
        pygame.display.flip()
