import Main
class Utils:
    def load_image(file):
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        str = 'Could not load image "%s" %s'
        raise SystemExit(str % (file, pygame.get_error()))
    return surface.convert()


def load_images(*files):
    surfaces = []
    for file in files:
        surfaces.append(load_image(file))
    return surfaces


def posToIndex(x, y):
    return (y * BOARD_WIDTH) + x


def indexToPos(i):
    return [(i % BOARD_WIDTH), int(i / BOARD_WIDTH)]


def posToOffset(pos):
    return [pos[0] * SPRITE_SIZE[0], pos[1] * SPRITE_SIZE[0]]
