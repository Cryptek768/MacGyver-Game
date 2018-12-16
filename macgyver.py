"""Main module for macgyver game"""
import pygame
from maze import Maze
from Level import *


def play_the_game(macgyver, screen, current_level, active, gameplaying):

    current_level.display_walls(screen)

def set_game():
    """Set the parameters for the game"""
    # Window creation
    screen = pygame.display.set_mode((SIZE_OF_LEVEL, SIZE_OF_LEVEL))

    # Get level structure in list
    Maze()

    current_level = Level('level_')
    current_level.display_walls(screen)

    active = 1
    gameplaying = 1
    return screen, current_level, active, gameplaying


def main():
    """Main function for running the game"""


    # Pygame initialisation
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.time.Clock().tick(100)
    pygame.key.set_repeat(100, 100)

    # Set the game
    screen, current_level, active, gameplaying = set_game()

    # refresh screen
    pygame.display.flip()


if __name__ == "__main__":
    main()
