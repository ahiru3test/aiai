import random
import pygame
from mypkg.GameBase import GameBase

class GameHL(GameBase):
    def ginput(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT: self.running = False
            if self.event.type == pygame.KEYDOWN:
                n1, n2 = random.randint(1,10), random.randint(1,10)

                if self.event.key == pygame.K_6:
                    print(f"My number is {n1}. Your choice is High. Your number is {n2}.")
                    print("You win!" if n1 < n2 else "You lose...")

                if self.event.key == pygame.K_4:
                    print(f"My number is {n1}. Your choice is Low. Your number is {n2}.")
                    print("You win!" if n1 > n2 else "You lose...")

if (__name__=="__main__"): (g := GameHL(640,480,60)).run()
