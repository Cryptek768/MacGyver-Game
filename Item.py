import pygame
import random
from Intel import *
from Setting import *
from Level import *

class Items:
    def __init__(self, level_structure, screen,):
        self.map_strucutre = level_structure
        self.available_tiles = []
        self.Item_Needle = pygame.image.load(Object_N).convert_alpha()
        self.Item_Ether = pygame.image.load(Object_E).convert_alpha()
        self.Item_Tube = pygame.image.load(Object_T).convert_alpha()
        
    def Items_spawn(self, level_structure, screen):
        num_line = 0
        for line in level_structure:
            num_col = 0
            for ligne_verti in line:
                rand_location_x = num_col + random.randint(0,14)
                rand_location_y = num_line + random.randint(0, 14)
                if ligne_verti <= str(0):
                    screen.blit(self.Item_Needle, (rand_location_x, rand_location_y))
                else:
                    if ligne_verti == str(1):
                        self.available_tiles.append((num_col, num_line))
                        """screen.blit(Item_Ether, (rand_location_x, rand_location_y))"""
                        """screen.blit(Item_Tube, (rand_location_x, rand_location_y))"""
