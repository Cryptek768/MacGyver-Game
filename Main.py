import pygame
import Maze
import Intel

class Master:

    def master():
        pygame.init()
        screen = pygame.display.set_mode((Size_Level, Size_Level))
        maze = Level("Map.txt")
        maze.level()
        maze.items_spawn_needle(master.map_structure)
        maze.items_spawn_ether(master.map_structure)
        maze.items_spawn_tube(master.map_structure)
        maze.display_wall(screen)
        
        while 1:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        MacGyver.move_MG('right')
                    if event.key == K_UP:
                        MacGyver.move_MG('left')
                    if event.key == K_LEFT:
                        MacGyver.move_MG('up')
                    if event.key == K_RIGHT:
                        MacGyver.move_MG('down')
            maze.display_wall(screen)
            screen.blit(maze.item_needle,(item_needle.item_position_y, item_needle.item_position_x))
            screen.blit(maze.item_ether,(item_ether.item_position_y, item_ether.item_position_x))
            screen.blit(maze.item_tube,(item_tube.item_position_y, item_tube.item_position_x))
            screen.blit(maze.image_Macgyver,(MacGyver.position_y, MacGyver.position_x))
            Guardian.blit_G(maze.map_structure, screen)
            pygame.display.flip()
            
    if __name__ =="__main__":
        master()
