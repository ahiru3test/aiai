import pygame
import random

def main(mainx,mainy):
    pygame.init()
    screen = pygame.display.set_mode((mainx,mainy))
    
    #ループ
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ゲームの処理を記述

        pygame.display.update()
        clock.tick(60)

# pygame.quit()
if(__name__=="__main__"):
    main(640,480)
