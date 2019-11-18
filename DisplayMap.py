import pygame
import time

class DisplayMap:

    def __init__(self):

        pygame.init()
        self.mc_gyver_position = {"x": 0, "y": 0}
        self.fenetre = pygame.display.set_mode((450, 450))
        self.start_image = pygame.image.load("ressource/startscreen450.jpg").convert()
        self.fond = pygame.image.load("ressource/fond.jpg").convert()
        self.mcgyver = pygame.image.load("ressource/MacGyver.png").convert_alpha()
        self.mur = pygame.image.load("ressource/mur.jpg").convert()

    def generate(self, my_map):
        # Pour chaques lists on prend les valeurs et on vérifie si c'est un mur ou non
        y_line = 0
        for items in my_map.start_level:
            x_line = 0 # on remet l'abscisse à 0
            for item in items:
                print(item)
                if item == "#":
                    self.fenetre.blit(self.mur, (x_line,y_line))
                elif item == "X":
                    self.fenetre.blit(self.mcgyver, (0,0))                
                else: 
                    pass
                x_line += 30 # pixels
            y_line += 30
        pygame.display.flip()

    def start_screen(self):

        self.fenetre.blit(self.start_image, (0,0))
        self.fenetre.blit(self.fond, (0,0))
        pygame.display.flip()
