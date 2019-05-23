import pygame
from Maze import *
from Intel import *
from pygame import K_DOWN, K_UP, K_LEFT, K_RIGHT

class Master:

    def master():
        pygame.init()
        screen = pygame.display.set_mode((Size_Level, Size_Level))
        maze = Level("Map.txt")
        maze.level()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:
                        maze.move_mg('down', screen)
                    if event.key == K_UP:
                        maze.move_mg('up', screen)
                    if event.key == K_LEFT:
                        maze.move_mg('left', screen)
                    if event.key == K_RIGHT:
                        maze.move_mg('right', screen)
            maze.display_wall(screen)
            maze.items_spawn(screen)
            maze.blit_mg(screen)
            maze.blit_g(screen)
            pygame.display.flip()
            
    if __name__ =="__main__":
        master()

"du jeudi 23 a 20h"""
