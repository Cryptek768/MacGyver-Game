import pygame
from Maze import *
from Intel import *

class Master:

    def master():
        pygame.init()
        screen = pygame.display.set_mode((Size_Level, Size_Level))
        maze = Level("Map.txt")
        maze.level()
        item_needle = Level.items_spawn_needle(maze.map_structure, screen)
        item_ether = Level.items_spawn_ether(maze.map_structure, screen)
        item_tube = Level.items_spawn_tube(maze.map_structure, screen)
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
            screen.blit(item_needle.items_spawn_needle(item_needle.item_position_y, item_needle.item_position_x))
            screen.blit(maze.item_ether,(item_ether.item_position_y, item_ether.item_position_x))
            screen.blit(maze.item_tube,(item_tube.item_position_y, item_tube.item_position_x))
            screen.blit(maze.image_Macgyver,(MacGyver.position_y, MacGyver.position_x))
            Guardian.blit_G(maze.map_structure, screen)
            pygame.display.flip()
            
    if __name__ =="__main__":
        master()
