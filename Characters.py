import Main
import Utils
class Characters: #Characters main class#
    pictures = []
    def __init__(self, Charaters):
    self.Pictures[0]
    self.Pictures.set_colorkey(COLOR_GRAY)
    self.Pictures = pygame.transform.scale(self.image SPRITE_SIZE)
    self.rect = self.Pictures.get_rect()

class MacGyver(Characters): #MacGyver Class#
    def __init__(self):
        super(Characters, self).__init__()
    def update(self):
        step = 0
        key_event = False

        for event in EVENTS:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move = -1
                    if self.index % BORD_WIDTH !=0:
                        key_event = True
                elif event.key == pygame.K_RIGHT:
                    step = 1

                    if (self.index + 1) % BOARD_WIDTH != 0:
                        key_event = True

                elif event.key == pygame.K_UP:
                    step = -BOARD_LENGTH

                    if self.index + step > -1:
                        key_event = True

                elif event.key == pygame.K_DOWN:
                    step = BOARD_LENGTH

                    if self.index + step < BOARD_WIDTH * BOARD_LENGTH:
                        key_event = True

        if key_event:

            if tiles[self.index + step] != 'X':

                if tiles[self.index + step] == 'C':
                    self.objects += 1
                    print ('object collected')

                elif tiles[self.index + step] == 'G':
                    global OVER
                    OVER = True

                    if self.objects == 3:
                        print ('You Win')

                    else:
                        print ('Game Over')

                self.updateRender(step)

    def updateRender(self, step):
        off = posToOffset(indexToPos(self.index + step))
        self.rect.x = off[0]
        self.rect.y = off[1]

        tiles[self.index] = 'O'
        tiles[self.index + step] = 'M'
        self.index += step

class Guardian(Characters): #Guardian Class#
    Pictures = ()
    def __init__(self):
        super(Characters, self).__init__()
