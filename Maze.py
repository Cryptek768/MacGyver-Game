import pygame
import random
from Intel import *

#Classe du Niveau(placement des murs)

class Level:

    #Preparation de la classe
    def __init__(self, map_pool):
        self.map_pool = map_pool
        self.map_structure = []
        self.position_x = 0
        self.position_y = 0
        self.sprite_x = int(0 /30)
        self.sprite_y = int(0 /30)
        self.image_Macgyver = pygame.image.load(MacGyver).convert_alpha()
        self.image_Guardian = pygame.image.load(Guardian).convert_alpha()
        self.background = pygame.image.load(Background).convert()
        
    #Prépartion de la liste pour le fichier map
    def level(self):
        with open (self.map_pool, "r") as map_pool:
            level_structure = []
            for line in map_pool:
                line_level = []
                for char in line:
                    if char != '/n':
                        line_level.append(char)
                level_structure.append(line_level)
        self.map_structure = level_structure
        
    #Placement des murs
    def display_wall (self, screen):

        wall = pygame.image.load(Wall).convert_alpha()
        screen.blit(self.background, (0, 0))
        num_line = 0
        for ligne_horiz in self.map_structure:
            num_col = 0
            for ligne_verti in ligne_horiz:
                position_x = num_col * Sprite_Size
                position_y = num_line * Sprite_Size
                if ligne_verti == str(1):
                    screen.blit(wall, (position_x, position_y))
                num_col +=1
            num_line +=1
