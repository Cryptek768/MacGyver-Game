"""Main module for macgyver game"""
import pygame
from Level import *
from Characters import *
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT


def play_the_game(macgyver, screen, current_level,):
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN:
            active = 0
            gameplaying = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                MacGyver.move_mg('down')
            if event.key == K_UP:
                MacGyver.move_mg('up')
            if event.key == K_LEFT:
                MacGyver.move_mg('left')
            if event.key == K_RIGHT:
                MacGyver.move_mg('right')

def set_game():
    """Set the parameters for the game"""
    # Window creation
    screen = pygame.display.set_mode((SIZE_OF_LEVEL, SIZE_OF_LEVEL))

    # Get level structure in list

    current_level = Level('level')
    current_level.generate_level()
    current_level.display_walls(screen)

    Macgyver = macgyver(0, 0, screen, current_level)
    guardian = Guardian(0, 0, screen, current_level)

    active = 1
    gameplaying = 1
    return macgyver, guardian, screen, current_level


def main():
    """Main function for running the game"""


    # Pygame initialisation
    pygame.init()
    screen = pygame.display.set_mode((SIZE_OF_LEVEL, SIZE_OF_LEVEL))
    pygame.display.set_caption(WINDOW_TITLE)

    main = Level("level")
    main.generate_level()
    Macgyver = MacGyver(0, 0, screen, Level)
    guardian = Guardian(0, 0)
    while 1:
        play_the_game(MacGyver, main, screen)
        main.display_walls(screen)
        Macgyver.blit_mg(main.structure, screen)
        Macgyver.move_mg('direction')
        guardian.blit_mg(main.structure, screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
