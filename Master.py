import pygame
from Level import *
from Setting import *
#Fichier master du jeux Gestion principale

class Master:
    
    def master():
        pygame.init()
        screen = pygame.display.set_mode((Size_Level, Size_Level))
        master = Level("Map.txt")
        master.level()
        MacGyver = Characters(0, 0, screen, Level)
        Guardian = Characters(0, 0, screen, Level)
        item = Items(0, 0, Level, screen)
        master.display_wall(screen)
        while 1:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        MacGyver.move_MG('down')
                    if event.key == K_UP:
                        MacGyver.move_MG('up')
                    if event.key == K_LEFT:
                        MacGyver.move_MG('left')
                    if event.key == K_RIGHT:
                        MacGyver.move_MG('right')
            master.display_wall(screen)
            "MacGyver.blit_MG(master.map_structure,screen)"
            item.Items_spawn(master.map_structure, screen)
            Guardian.blit_G(master.map_structure, screen)
            pygame.display.flip()
            
    if __name__ =="__main__":
        master()
