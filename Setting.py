import pygame
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
