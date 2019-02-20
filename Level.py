import pygame
from Intel import *
from Setting import *

#Classe du Niveau
class Level:
    
    #Preparation de la Classe
    def __init__(self, map_pool):
        self.map_pool = map_pool
        self.map_structure = []
        self.available_tiles = []
        self.background = pygame.image.load(Background).convert()
        
#Methode de la classe level qui traite le fichier Map.txt
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
        
#Methode pour afficher les murs et passages du niveau
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
                elif ligne_verti == str(0):
                    self.available_tiles.append((num_col, num_line))
                num_col +=1
            num_line +=1
        
        
                    
        
