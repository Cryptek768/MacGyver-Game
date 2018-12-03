import Main
def map():
    # create window
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Free MacGyver')

    # background
    background = pygame.Surface(WINDOW_SIZE)
    background.fill(COLOR_WHITE)
    screen.blit(background, (0, 0))

    # sprites
    WallSprite.at = [(244, 8)]
    WallSprite.images = [load_image('assets/structures.jpg')]

    ObjectSprite.at = [(872, 0), (2024, 0), (164, 0)]
    ObjectSprite.sizes = [(17, 32), (17, 32), (24, 32)]
    ObjectSprite.images.append(load_image('assets/equipment-32x32.png'))
    ObjectSprite.images.append(load_image('assets/equipment-32x32.png'))
    ObjectSprite.images.append(load_image('assets/lifebar-32x-32.png'))

class WallSprite(pygame.sprite.Sprite):
    at = []
    images = []

    """docstring for WallSprite"""
    def __init__(self):
        super(WallSprite, self).__init__()

        self.image = pygame.Surface(SPRITE_SIZE)
        self.image.blit(self.images[0], (0, 0), (self.at[0], SPRITE_SIZE))

        self.rect = self.image.get_rect()
        
class ObjectSprite(pygame.sprite.Sprite):
    at = []
    sizes = []
    images = []

    index = 0

    """docstring for ObjectSprite"""
    def __init__(self, i):
        super(ObjectSprite, self).__init__()

        self.image = pygame.Surface(self.sizes[i])
        self.image.blit(self.images[i], (0, 0), (self.at[i], self.sizes[i]))
        self.image = pygame.transform.scale(self.image, SPRITE_SIZE)
        self.image.set_colorkey(COLOR_GRAY)

        self.rect = self.image.get_rect()

    def update(self):
        if tiles[self.index] == 'M':
            print ('object kill')
            self.kill()
