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
        item_needle = maze.items_spawn_needle(maze.map_structure)
        item_ether = maze.items_spawn_ether(maze.map_structure)
        item_tube = maze.items_spawn_tube(maze.map_structure)
        maze.display_wall(screen)
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:
                        maze.move_mg('right')
                    if event.key == K_UP:
                        maze.move_mg('left')
                    if event.key == K_LEFT:
                        maze.move_mg('up')
                    if event.key == K_RIGHT:
                        maze.move_mg('down')
                        
            maze.display_wall(screen)
            maze.move_mg(maze.image_Macgyver)
            screen.blit(maze.image_Macgyver, (0, 0))
            screen.blit(maze.image_Guardian, (420, 413))
            screen.blit(maze.item_needle, item_needle)
            screen.blit(maze.item_ether, item_ether)
            screen.blit(maze.item_tube, item_tube)
            pygame.display.flip()
            
    if __name__ =="__main__":
        master()
