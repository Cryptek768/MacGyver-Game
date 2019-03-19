import pygame
import random
from Intel import *
from Setting import *
from Level import *

class Items:
#init de la classe items
    def __init__(self, level_structure, screen):
        self.map_structure = level_structure
        self.item_position_x = 0
        self.item_position_y = 0
        self.Item_Needle = pygame.image.load(Object_N).convert_alpha()
        self.Item_Ether = pygame.image.load(Object_E).convert_alpha()
        self.Item_Tube = pygame.image.load(Object_T).convert_alpha()
        
#Méthode pour spawn les objets
        
    def Items_spawn_Needle(self, level_structure):
        rand_x = random.randint(0,14)
        rand_y = random.randint(0, 14)
        while level_structure [rand_x][rand_y] != str(0):
            rand_x = random.randint(0,14)
            rand_y = random.randint(0, 14)
        self.item_position_x = rand_x * Sprite_Size
        self.item_position_y = rand_y * Sprite_Size
        
    def Items_spawn_Ether(self, level_structure):
        rand_x = random.randint(0,14)
        rand_y = random.randint(0, 14)
        while level_structure [rand_x][rand_y] != str(0):
            rand_x = random.randint(0,14)
            rand_y = random.randint(0, 14)
        self.item_position_x = rand_x * Sprite_Size
        self.item_position_y = rand_y * Sprite_Size

    def Items_spawn_Tube(self, level_structure):
        rand_x = random.randint(0,14)
        rand_y = random.randint(0, 14)
        while level_structure [rand_x][rand_y] != str(0):
            rand_x = random.randint(0,14)
            rand_y = random.randint(0, 14)
        self.item_position_x = rand_x * Sprite_Size
        self.item_position_y = rand_y * Sprite_Size

        
            
            
            
            
        
        
        
