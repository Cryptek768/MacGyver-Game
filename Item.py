import pygame
import random
from Intel import *
from Setting import *
from Level import *

class Items_Spawn:
    
    def Items_spawn(self, map_structure):
        Items_images = pygame.image.load(str(Objects)).convert_alpha()
        num_line = 0
        for Items_Place_horiz in self.Items_location:
            num_col = 0
            for Items_Place_verti in Items_place_horiz:
                rand_location_x = num_col + random.randint(0,15)
                rand_location_y = num_line + random.randint(0, 15)
                if Items_place_verti == str(0):
                    screen.blit(Items_images (rand_location_x, rand_location_y))
