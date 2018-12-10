class Level:
    """ class representing the level of the game"""

    def __init__(self, Level_file):

        self.Level_file = Level_file
        self.structure = []
        self.generate_level()
        self.available_tiles = []
        self.fond = pygame.image.load(BACKGROUND).convert()
        self.list_of_collectables = []


    def generate_level(self):
        """Generates the level as a table from file 'level' """
        with open(self.Level_file, "r") as Level_file:

            Level_list = []
            for line in Level_file:
                line_list = []
                for char in line:
                    if char != '\n':
                        line_list.append(char)
                Level_list.append(line_list)
        self.structure = Level_list

    def display_walls(self, screen):
        """Reads the level table, displays walls and guardian
        and stores all non-wall tiles in available_tiles"""


        Wall = pygame.image.load(WALLPIC).convert_alpha()
        Guardian = pygame.image.load(GUARDIANPIC).convert_alpha()

        screen.blit(self.fond, (0, 0))

        num_line = 0
        for ligne_horiz in self.structure:
            num_col = 0
            for ligne_vert in ligne_horiz:

                position_x = num_col * SIZE_OF_SPRITE

                position_y = num_line * SIZE_OF_SPRITE

                if ligne_vert == str(1):
                    screen.blit(Wall, (position_x, position_y))
                elif ligne_vert == '9':
                    screen.blit(Guardian, (position_x, position_y))
                else:
                    if ligne_vert == str(0):
                        self.available_tiles.append((num_col, num_line))

                num_col += 1
            num_line += 1
