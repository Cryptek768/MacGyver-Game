import pygame
from pygame.locals import*
pygame.init()

def loadScene():
    directory = os.listdir('levels')

    files = []
    for file in directory:
        if ".fmg" in file:
            files.append(file)

        if len(files) == 0:
            print ('Error no .fmg file(s)')
            return False

    # DEBUG
    # print ('Files in dir: ', files)

    # Load a random lvl
    rand = random.randint(0, len(files) - 1)

    # Get file
    f = open('levels/' + files[rand], 'r')

    fw = ''
    for line in f.readlines():
        fw += line.split('\n')[0]

    # DEBUG
    # print ('number of words: ', len(fw))

    # Test file integrity
    if len(fw) != (BOARD_WIDTH * BOARD_LENGTH):
        print ('Error file too short')

    if 'M' not in fw and 'G' not in fw:
        print ('Error no MacGyver or Guardian in file')

    return fw


def buildScene(scene):
    sprites = pygame.sprite.Group()
    for i in range(len(scene)):
        tiles.append(scene[i])

        sprite = pygame.sprite.Sprite

        isSprite = True
        if scene[i] == 'X':
            sprite = WallSprite()

        elif scene[i] == 'M':
            sprite = MacGyverSprite()
            sprite.index = i

        elif scene[i] == 'G':
            sprite = GuardianSprite()

        elif scene[i] == 'O':
            isSprite = False

        else:
            return False

        if isSprite:
            off = posToOffset(indexToPos(i))
            sprite.rect.x = off[0]
            sprite.rect.y = off[1]

            sprites.add(sprite)

    for i in range(3):
        ok = False
        while not ok:
            rand = random.randint(0, (BOARD_WIDTH * BOARD_LENGTH) - 1)
            if tiles[rand] == 'O':
                # print ('rand -', rand)

                sprite = ObjectSprite(i)
                sprite.index = rand

                off = posToOffset(indexToPos(rand))
                sprite.rect.x = off[0]
                sprite.rect.y = off[1]

                sprites.add(sprite)

                tiles[rand] = 'C'
                ok = True
    """
    for i in range(3):
        sprite = ObjectSprite(i)
        sprite.index = i + 1
        off = posToOffset(indexToPos(i + 1))
        sprite.rect.x = off[0]
        sprite.rect.y = off[1]
        sprites.add(sprite)
        tiles[i + 1] = 'C'
        ok = True
    """
    # DEBUG
    # print (tiles)

    return (tiles, sprites)


def main():
    # Initialization
    pygame.init()

    # create window
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Free MacGyver')

    # background
    background = pygame.Surface(WINDOW_SIZE)
    background.fill(COLOR_WHITE)
    screen.blit(background, (0, 0))

    # sprites
    WallSprite.at = [(244, 8)]
    WallSprite.images = [load_image('assets/tc-image005.jpg')]

    GuardianSprite.images = [load_image('assets/guardian.png')]
    MacGyverSprite.images = [load_image('assets/macgyver.png')]

    ObjectSprite.at = [(872, 0), (2024, 0), (164, 0)]
    ObjectSprite.sizes = [(17, 32), (17, 32), (24, 32)]
    ObjectSprite.images.append(load_image('assets/equipment-32x32.png'))
    ObjectSprite.images.append(load_image('assets/equipment-32x32.png'))
    ObjectSprite.images.append(load_image('assets/extras-32x-32.png'))

    # load the file scene
    scene = loadScene()
    if not scene:
        return False

    # load and prepare sprites
    (tiles, all) = buildScene(scene)
    if not all:
        print ('buildScene return False')
        return False

    global OVER
    global EVENTS

    isAlive = True
    clock = pygame.time.Clock()
    while isAlive:
        OVER = False
        # Events
        EVENTS = pygame.event.get()
        for event in EVENTS:
            if event.type == pygame.QUIT:
                isAlive = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    isAlive = False

        # Logic
        all.update()

        if OVER:
            isAlive = False

        # Render
        all.clear(screen, background)

        all.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    # destruction
    pygame.quit()
