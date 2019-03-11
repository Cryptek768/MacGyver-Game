import pygame
import random
from Intel import *
from Setting import *
from Level import *

class Items:
    def __init__(self, x, y, level_structure, screen):
        self.map_structure = level_structure
        self.item_position_x = x
        self.item_position_y = y
        self.sprite_x = int(x /30)
        self.sprite_y = int(y /30)
        self.available_tiles = []
        self.Item_Needle = pygame.image.load(Object_N).convert_alpha()
        self.Item_Ether = pygame.image.load(Object_E).convert_alpha()
        self.Item_Tube = pygame.image.load(Object_T).convert_alpha()
        
    def Items_spawn(self, level_structure, screen):
        num_line = self.item_position_x + random.randint(0,14)
        for line in level_structure:
            num_col = self.item_position_y + random.randint(0, 14)
            for ligne_verti in line:
                item_position_x = num_col * Sprite_Size
                item_position_y = num_line * Sprite_Size
                if ligne_verti == str(0):
                    screen.blit(self.Item_Needle, (item_position_x, item_position_y))
                    
            
