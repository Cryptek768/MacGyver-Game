import pygame

#Classe du Niveau
class Level:
    
    #Preparation de la Classe
    def __init__(self, map_pool):
        self.map_pool = map_pool
        self.map_structure = []
        self.background = pygame.image.load(Background).convert()
        
#Methode de la classe level qui traite le fichier Map.txt
    def level(self):
        with open (self.map_pool, "r") as map_pool:
            level_structure = []
            for line in map_pool:
                line_level = []
                for char in line:
                    if char != '/n':
                        line_level.append(char)
                level_structure.append(line_level)
        self.map_structure = level_structure
        
#Methode pour afficher les murs et passages du niveau
    def display_wall (self, screen):

        wall = pygame.image.load(Wall).convert_alpha()
        screen.blit(self.background, (0, 0))
        num_line = 0
        for ligne_horiz in self.map_structure:
            num_col = 0
            for ligne_verti in ligne_horiz:
                position_x = num_col * Sprite_Size
                position_y = num_line * Sprite_Size
                if ligne_verti == str(1):
                    screen.blit(wall, (position_x, position_y))
                num_col +=1
            num_line +=1


class Items:
#init de la classe items
    def __init__(self, level_structure, screen):
        self.map_structure = level_structure
        self.item_position_x = 0
        self.item_position_y = 0
        self.Item_Needle = pygame.image.load(Object_N).convert_alpha()
        self.Item_Ether = pygame.image.load(Object_E).convert_alpha()
        self.Item_Tube = pygame.image.load(Object_T).convert_alpha()
        
#Méthode pour spawn les objets
        
    def items_spawn_needle(self, level_structure):
        rand_x = random.randint(0,14)
        rand_y = random.randint(0, 14)
        while level_structure [rand_x][rand_y] != str(0):
            rand_x = random.randint(0,14)
            rand_y = random.randint(0, 14)
        self.item_position_x = rand_x * Sprite_Size
        self.item_position_y = rand_y * Sprite_Size
        
    def items_spawn_ether(self, level_structure):
        rand_x = random.randint(0,14)
        rand_y = random.randint(0, 14)
        while level_structure [rand_x][rand_y] != str(0):
            rand_x = random.randint(0,14)
            rand_y = random.randint(0, 14)
        self.item_position_x = rand_x * Sprite_Size
        self.item_position_y = rand_y * Sprite_Size

    def items_spawn_tube(self, level_structure):
        rand_x = random.randint(0,14)
        rand_y = random.randint(0, 14)
        while level_structure [rand_x][rand_y] != str(0):
            rand_x = random.randint(0,14)
            rand_y = random.randint(0, 14)
        self.item_position_x = rand_x * Sprite_Size
        self.item_position_y = rand_y * Sprite_Size


class Characters:
    
#init de la classe des perso
    def __init__(self, screen, level_structure):
        self.position_x = 0
        self.position_y = 0
        self.sprite_x = int(0 /30)
        self.sprite_y = int(0 /30)
        self.map_structure = level_structure
        self.available_tiles = []
        self.image_Macgyver = pygame.image.load(MacGyver).convert_alpha()
        self.image_Guardian = pygame.image.load(Guardian).convert_alpha()
        
#methode de Macgyver
    def blit_mg(self, level_structure, screen):
        num_line = 0
        for line in level_structure:
            num_col = 0
            for ligne_verti in line:
                position_x = num_col * Sprite_Size
                position_y = num_line * Sprite_Size
                if ligne_verti == str(5):
                    screen.blit(self.image_Macgyver, (position_x, position_y))
                else:
                    if ligne_verti == str(5):
                        self.available_tiles.append((num_col, num_line))
        
#methode du guard                        
    def blit_g(self, level_structure, screen):
        num_line = 14
        for line in level_structure:
            num_col = 14
            for ligne_verti in line:
                position_x = num_col * Sprite_Size
                position_y = num_line * Sprite_Size
                if ligne_verti == str(3):
                    screen.blit(self.image_Guardian, (position_x, position_y))
                else:
                    if ligne_verti == str(3):
                        self.available_tiles.append((num_col, num_line))
                        
#Methode de deplacement du joueur
    def move_mg(self, direction):
        if direction == 'down':
            if self.sprite_y < (Sprite_Size_Level - 1):
                if self.map_structure[self.sprite_y+1][self.sprite_x] != '1':
                    self.position_y += 30
                    self.sprite_y += 1
                    
        elif direction == 'up':
            if self.sprite_y > 0:
                if self.map_structure[self.sprite_y-1][self.sprite_x] != '1':
                    self.position_y -= 30
                    self.sprite_y -= 1
                    
        elif direction == 'left':
            if self.sprite_x > 0:                
                if self.map_structure[self.sprite_y][self.sprite_x-1] != '1':
                    self.position_x -= 30
                    self.sprite_x -= 1
                    
        elif direction == 'right':
            if self.sprite_x < (Sprite_Size_Level - 1):
                if self.map_structure[self.sprite_y][self.sprite_x+1] != '1':
                   self.position_x += 30
                   self.sprite_x += 1
