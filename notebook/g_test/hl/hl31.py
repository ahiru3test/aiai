import random
import pygame

class GameBase:
    def __init__(self,x=640,y=480,f=60):
        pygame.init()
        self.screen = pygame.display.set_mode((x,y))
        self.f=f
        self.running = True
    
    def __del__(self):
        pygame.quit()

    def run(self):
        self.clock =pygame.time.Clock()
        while self.running:
            self.ginit()
            self.ginput()
            self.glogic()
            self.gresolve()
            self.gview()
            ###
    
    ### abstract method
    ### init in run loop
    def ginit(self):
        pass
    
    ### input(or event)
    def ginput(self):
        for self.event in pygame.event.get():
            self.gevent()
            if self.event.type == pygame.QUIT:
                self.running = False
    
    ### main logic
    def glogic(self):
        pass
    
    ### resolve win/lose
    def gresolve(self):
        pass

    ### view screen
    def gview(self):
        pygame.display.update()
        self.clock.tick(self.f)

class GameHL(GameBase):
    def ginput(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.running = False
            
            if self.event.type == pygame.KEYDOWN:
                n1, n2 = random.randint(1,10), random.randint(1,10)

                if self.event.key == pygame.K_6:
                    print(f"My number is {n1}. Your choice is High. Your number is {n2}.")
                    print("You win!" if n1 < n2 else "You lose...")

                if self.event.key == pygame.K_4:
                    print(f"My number is {n1}. Your choice is Low. Your number is {n2}.")
                    print("You win!" if n1 > n2 else "You lose...")

if (__name__=="__main__"):
    g = GameHL(640,480,60)
    g.run()
