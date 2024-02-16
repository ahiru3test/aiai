import pygame

class GameBase:
    def __init__(self,x=640,y=480,f=60):
        pygame.init()
        self.screen = pygame.display.set_mode((x,y))
        self.f=f
        self.running = False
    
    def __del__(self):
        pygame.quit()

    def run(self):
        self.clock =pygame.time.Clock()
        self.ginit(self.running)
        self.running = True

        while self.running:
            self.ginit()
            self.ginput()
            self.glogic()
            self.gresolve()
            self.gview()
            ###
    
    ### abstract method
    ### init in run loop
    def ginit(self, running=True):
        pass
    
    ### input(or event)
    def ginput(self):
        for self.event in pygame.event.get():
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

if (__name__=="__main__"): (g := GameBase(640,480,60)).run()
