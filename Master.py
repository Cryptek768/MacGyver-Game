import pygame
from Level import *
from Setting import *
from Item import *
#Fichier master du jeux Gestion principale

class Master:
    
    def master():
        pygame.init()
        screen = pygame.display.set_mode((Size_Level, Size_Level))
        master = Level("Map.txt")
        master.level()
        Objects = Items_Spawn()
        Objects.Items_spawn(Level)
        MacGyver = Characters(0, 0, screen, Level)
        Guardian = Characters(0, 0, screen, Level)
        while 1:
            master.display_wall(screen)
            MacGyver.blit_MG(master.map_structure,screen)
            MacGyver.move_MG('direction')
            Guardian.blit_G(master.map_structure, screen)
            pygame.display.flip()
            
    if __name__ =="__main__":
        master()
