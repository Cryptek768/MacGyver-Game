import Main
import Utils

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

