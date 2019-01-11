import pygame
from constants import *

class MacGyver:
    "Display Macgyver on the map"
    def __init__(self, x, y, screen, Level):
        self.psox = x
        self.posy = y
        self.sprite_x = int(x /30)
        self.sprite_y = int(y /30)
        self.image = pygame.image.load(MACGYVERPIC).convert_alpha()

    def blit_mg(self, structure, screen):
        num_line = 0
        for ligne_horiz in structure:
            num_col = 0
            for ligne_vert in ligne_horiz:
                position_x = num_col * SIZE_OF_SPRITE
                position_y = num_line * SIZE_OF_SPRITE
                if ligne_vert == str(5):
                    screen.blit(self.image, (position_x, position_y))
                else:
                    if ligne_vert == str(5):
                        self.available_tiles.append((num_col, num_line))

    def move_mg(self, direction):
        if direction =='down':
           if self.sprite_y < (SPRITES_IN_LEVEL-1):
              if self.level.structure[self.sprite_y+1][self.sprite_x] !='1':
                self.posy +=30
                self.sprite_y +=1

        elif direction == 'up':
             if self.sprite_y > 0:
                if self.level.structure[self.sprite_y-1][self.sprite_x] !='1':
                    self.posy -= 30
                    self.sprite_y -= 1

        elif direction == 'left':
             if self.sprite_x > 0:
                if self.level.structure[self.sprite_y][self.sprite_x-1] !='1':
                   self.posy -= 30
                   self.sprite_y -= 1

        elif direction == 'right':
             if self.sprite_x < (SPRITES_IN_LEVEL-1):
                if self.level.structure[self.sprite_y][self.sprite_x+1] != '1':
                   self.psox += 30
                   self.sprite_x += 1

class Guardian:
    "display the guardian on the map"
    def __init__(self, x, y):
        self.psox = x
        self.posy = y
        self.sprite_x = int(x /30)
        self.sprite_y = int(y /30)
        self.image = pygame.image.load(GUARDIANPIC).convert_alpha()

    def blit_mg(self, structure, screen):
        num_line = 14
        for ligne_horiz in structure:
            num_col = 14
            for ligne_vert in ligne_horiz:
                position_x = num_col * SIZE_OF_SPRITE
                position_y = num_line * SIZE_OF_SPRITE
                if ligne_vert == str(3):
                    screen.blit(self.image, (position_x, position_y))
                else:
                    if ligne_vert == str(3):
                        self.available_tiles.append((num_col, num_line))
