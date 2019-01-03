"""file with all classes for the macgyver game"""
import pygame
from constants import *

class Level:
    """ class representing the level of the game"""

    def __init__(self, level_file):

        self.level_file = level_file
        self.structure = []
        self.generate_level()
        self.available_tiles = []
        self.fond = pygame.image.load(BACKGROUND).convert()


    def generate_level(self):
        """Generates the level as a table from file 'level' """
        with open(self.level_file, "r") as level_file:

            level_list = []
            for line in level_file:
                line_list = []
                for char in line:
                    if char != '\n':
                        line_list.append(char)
                level_list.append(line_list)
        self.structure = level_list

    def display_walls(self, screen):
        """Reads the level table, displays walls
        and stores all non-wall tiles in available_tiles"""


        wall = pygame.image.load(WALLPIC).convert_alpha()
        screen.blit(self.fond, (0, 0))

        num_line = 0
        for ligne_horiz in self.structure:
            num_col = 0
            for ligne_vert in ligne_horiz:

                position_x = num_col * SIZE_OF_SPRITE

                position_y = num_line * SIZE_OF_SPRITE

                if ligne_vert == str(1):
                    screen.blit(wall, (position_x, position_y))
                elif ligne_vert == str(0):
                     self.available_tiles.append((num_col, num_line))

                num_col += 1
            num_line += 1
