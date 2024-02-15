import pygame
import random

class GameMain:
    # 色の定義
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # ゲームの状態
    STATE_START = 0
    STATE_PLAY = 1
    STATE_END = 2
    state = STATE_START

    # 数字のリスト
    numbers = list(range(1, 11))

    def __init__(self, x=640, y=480, f=60):
        pygame.init()
        screen = pygame.display.set_mode((x,y))
        self.f=f
        self.running = True

    def font(self, n=0):
        font = [pygame.font.SysFont("Arial", 32),]
        return font[n]

    def run(self):
        self.clock = pygame.time.Clock()
        while self.running:
            #イベント処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # elif state ==
                #     pass
                else:
                    pass



            # ゲームの処理を記述

            pygame.display.update()
            self.clock.tick(self.f)
    

# pygame.quit()
if(__name__=="__main__"):
    gm = GameMain(640,480)
    gm.run()

exit()

'''
aaa
'''
