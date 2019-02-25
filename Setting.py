import pygame
from pygame.locals import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT
from Intel import *
from Level import *
from Characters import *

#Fichier parametres du jeux qui prends les parametres du jeux

class Setting:
    
    def setting():
        
        screen = pygame.display.set_mod((Size_Level, Size_Level))
        current_level = Level('Map')
        current_level.display_walls(screen)
        MacGyver = MacGyver(0, 0, screen)
        Guardian = Gurdian(0, 0, screen)
        return MacGyver, Guardian, screen

    def setting_player_move():

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    Characters.move_MG('down')
                if event.key == K_UP:
                    Characters.move_MG('up')
                if event.key == K_LEFT:
                    Characters.move_MG('left')
                if event.key == K_RIGHT:
                    Characters.move_MG('right')
        Characters.blit_MG()
        return active, gameplay
