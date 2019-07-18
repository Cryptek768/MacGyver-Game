import pygame
import random
from Intel import *


#Classe des placements d'objets

class Items:

    #Preparation de la classe
    def __init__(self, map_pool):
        self.item_needle = pygame.image.load(Object_N).convert_alpha()
        self.item_ether = pygame.image.load(Object_E).convert_alpha()
        self.item_tube = pygame.image.load(Object_T).convert_alpha()
        
    #Méthode de spawn des objets
    def items_spawn(self, screen):
        while items:
            rand_x = random.randint(0, 14)
            rand_y = random.randint(0, 14)
            if self.map_structure [rand_x][rand_y] == 0:
                screen.blit(self.image_(Object_N), (rand_x, rand_y))
