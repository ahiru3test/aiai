import pygame
import random

class GameMain:
    def __init__(self, x=640, y=480, f=60):
        pygame.init()
        screen = pygame.display.set_mode((x,y))
        self.f=f
        self.running = True
    
    def run(self):
        self.clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # ゲームの処理を記述

            pygame.display.update()
            self.clock.tick(self.f)

# pygame.quit()
if(__name__=="__main__"):
    gm = GameMain(640,480)
    gm.run()
