import pygame
from Maze import *
from Intel import *
from Characters import *
from Items import *
from pygame import K_DOWN, K_UP, K_LEFT, K_RIGHT

#Classe Main du jeux avec gestion des movements et l'affichage
class Master:

    def master():
        pygame.init()
        screen = pygame.display.set_mode((Size_Level, Size_Level))
        maze = Level("Map.txt")
        maze.level()
        #Boucle de rafraichisement
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:
                        Characters.move_mg(maze, 'down', screen)
                    if event.key == K_UP:
                        Characters.move_mg(maze, 'up', screen)
                    if event.key == K_LEFT:
                        Characters.move_mg(maze, 'left', screen)
                    if event.key == K_RIGHT:
                        Characters.move_mg(maze, 'right', screen)
            maze.display_wall(screen)
            Characters.blit_mg(maze, screen)
            Characters.move_mg(maze, 'direction', screen)
            Characters.blit_g(maze, screen)
            Items. items_spawn(maze, screen)
            pygame.display.flip()
            
    if __name__ =="__main__":
        master()
