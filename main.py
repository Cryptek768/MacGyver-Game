import pygame
import intel
import lab

#Fichier master du jeux Gestion principale

class Master:
    
    def master():
        pygame.init()
        screen = pygame.display.set_mode((Size_Level))
        master = Level("Map.txt")
        master.level()
        MacGyver = lab(screen, master.map_structure)
        Guardian = lab(screen, Level)
        item_needle = lab(master.map_structure, screen)
        item_ether = lab(master.map_structure, screen)
        item_tube = lab(master.map_structure, screen)

        MacGyver.move_mg(master.map_structure)
        item_needle.Items_spawn_Needle(master.map_structure)
        item_ether.Items_spawn_Ether(master.map_structure)
        item_tube.Items_spawn_Tube(master.map_structure)
        master.display_wall(screen)
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
            master.display_wall(screen)
            screen.blit(item_needle.Item_Needle,(item_needle.item_position_y, item_needle.item_position_x))
            screen.blit(item_ether.Item_Ether,(item_ether.item_position_y, item_ether.item_position_x))
            screen.blit(item_tube.Item_Tube,(item_tube.item_position_y, item_tube.item_position_x))
            screen.blit(MacGyver.image_Macgyver,(MacGyver.position_y, MacGyver.position_x))
            Guardian.blit_G(master.map_structure, screen)
            pygame.display.flip()
            
    if __name__ =="__main__":
        master()

