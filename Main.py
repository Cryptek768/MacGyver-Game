import pygame
from Maze import *
from Intel import *

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
                        maze.move_MG('right')
                    if event.key == K_UP:
                        maze.move_MG('left')
                    if event.key == K_LEFT:
                        maze.move_MG('up')
                    if event.key == K_RIGHT:
                        maze.move_MG('down')
                        
            maze.display_wall(screen)
            screen.blit(item_needle,(maze.item_position_y, maze.item_position_x))
            screen.blit(item_ether,(maze.item_position_y, maze.item_position_x))
            screen.blit(item_tube,(maze.item_position_y, maze.item_position_x))
            screen.blit(maze.image_Macgyver,(MacGyver.position_y, MacGyver.position_x))
            Guardian.blit_g(maze.map_structure, screen)
            pygame.display.flip()
            
    if __name__ =="__main__":
        master()
