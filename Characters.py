import pygame
from Level import *
from Intel import *
from Setting import *
class Characters:
    
#init de la classe des perso
    def __init__(self, x, y, screen, level_structure):
        self.position_x = x
        self.position_y = y
        self.sprite_x = int(x /30)
        self.sprite_y = int(y /30)
        self.image_Macgyver = pygame.image.load(MacGyver).convert_alpha()
        self.image_Guardian = pygame.image.load(Guardian).convert_alpha()
        
#methode de Macgyver
    def blit_MG(self, level_structure, screen):
        num_line = 0
        for line in level_structure:
            num_col = 0
            for ligne_verti in line:
                position_x = num_col * Sprite_Size
                position_y = num_line * Sprite_Size
                if ligne_verti == str(5):
                    screen.blit(self.image_Macgyver, (position_x, position_y))
                else:
                    if ligne_verti == str(5):
                        self.available_tiles.append((num_col, num_line))
        
#methode du guard                        
    def blit_G(self, level_structure, screen):
        num_line = 14
        for line in level_structure:
            num_col = 14
            for ligne_verti in line:
                position_x = num_col * Sprite_Size
                position_y = num_line * Sprite_Size
                if ligne_verti == str(3):
                    screen.blit(self.image_Guardian, (position_x, position_y))
                else:
                    if ligne_verti ==str(3):
                        self.available_tiles.append((num_col, num_line))
                        
#Methode de deplacemen du joueur
    def move_MG(self, direction):
        if direction == 'down':
            if self.sprite_y (Sprite_Size_Level-1):
                if self.map_structure[self.sprite_y+1][self.sprite_x] != '1':
                    self.position_y += 30
                    self.position_x += 1
        elif direction == 'up':
            if self.sprite_y > 0:
                if self.map_structure[self.sprite_y-1][self.sprite_x] !='1':
                    self.position_y -= 1
        elif direction == 'left':
            if self.sprite_x > 0:                
                if self.map_structure[self.sprite_y][self.sprite_x-1] !='1':
                    self.position_x -= 30
                    self.position_y -= 1
        elif direction == 'right':
            if self.sprite_x < (Sprite_Size_Level-1):
                if self.map_structure[self.sprite_y][self.sprite_x+1] != '1':
                    self.position_x += 30
                    self.sprite_x += 1
                
