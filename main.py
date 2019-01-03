"""Main module for macgyver game"""
import pygame
from Level import *
from Characters import *
from pygame.locals import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT


def play_the_game(macgyver, screen, current_level):

    current_level.display_walls(screen)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                Characters.move_mg('down')
            if event.key == K_UP:
                Characters.move_mg('up')
            if event.key == K_LEFT:
                Characters.move_mg('left')
            if event.key == K_RIGHT:
                Characters.move_mg('right')

def set_game():
    """Set the parameters for the game"""
    # Window creation
    screen = pygame.display.set_mode((SIZE_OF_LEVEL, SIZE_OF_LEVEL))

    # Get level structure in list

    current_level = Level('level')
    current_level.generate_level()
    current_level.display_walls(screen)

    Macgyver = macgyver(0, 0, screen, current_level, direction)
    MacGyver.blit_mg(current_level.structure, screen, direction)
    MacGyver.move_mg(current_level.structure, screen, direction)
    guardian = Guardian(0, 0, screen, current_level)
    guardian.blit_mg(current_level.structure, screen)

    active = 1
    gameplaying = 1
    return macgyver, guardian, screen, current_level, direction


def main():
    """Main function for running the game"""


    # Pygame initialisation
    pygame.init()
    screen = pygame.display.set_mode((SIZE_OF_LEVEL, SIZE_OF_LEVEL))
    pygame.display.set_caption(WINDOW_TITLE)

    test = Level("level")
    test.generate_level()
    Macgyver = MacGyver(0, 0)
    guardian = Guardian(0, 0)
    while 1:
        test.display_walls(screen)
        Macgyver.blit_mg(test.structure, screen)
        Macgyver.move_mg('direction')
        guardian.blit_mg(test.structure, screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
