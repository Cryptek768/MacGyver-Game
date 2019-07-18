import pygame
from Intel import *

class Characters:

        def __init__(self, map_pool):
            self.map_pool = map_pool
            self.position_x = 0
            self.position_y = 0
            self.sprite_x = int(0 /30)
            self.sprite_y = int(0 /30)
            self.image_Macgyver = pygame.image.load(MacGyver).convert_alpha()
            self.image_Guardian = pygame.image.load(Guardian).convert_alpha()
            
        #Placement du Gardien
        def blit_mg(self, screen):
            screen.blit(self.image_Macgyver, (self.position_x, self.position_y))
        #Placement de Macgyver
        def blit_g(self, screen):
            num_line = 14
            for line in self.map_structure:
                num_col = 14
                for ligne_verti in line:
                    position_x = num_col * Sprite_Size
                    position_y = num_line * Sprite_Size
                    if ligne_verti == str(3):
                        screen.blit(self.image_Guardian, (position_x, position_y))
                    else:
                        if ligne_verti == str(3):
                            self.available_tiles.append((num_col, num_line))
                        
        #Méthode de déplacement de Macgyver(player)
        def move_mg(self, direction, screen):
            if direction == 'down':
                if self.sprite_y < (Sprite_Size_Level - 1):
                    if self.map_structure[self.sprite_y+1][self.sprite_x] != '1':
                        self.position_y += 30
                        self.sprite_y += 1
                    
            elif direction == 'up':
                if self.sprite_y > 0:
                    if self.map_structure[self.sprite_y-1][self.sprite_x] != '1':
                        self.position_y -= 30
                        self.sprite_y -= 1
                    
            elif direction == 'left':
                if self.sprite_x > 0:                
                    if self.map_structure[self.sprite_y][self.sprite_x-1] != '1':
                        self.position_x -= 30
                        self.sprite_x -= 1
                    
            elif direction == 'right':
                if self.sprite_x < (Sprite_Size_Level - 1):
                    if self.map_structure[self.sprite_y][self.sprite_x+1] != '1':
                       self.position_x += 30
                       self.sprite_x += 1
