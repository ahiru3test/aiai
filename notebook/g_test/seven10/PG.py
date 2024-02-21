import pygame, pygame_gui

class PG(): #----------------------------------------------------------
    def init(self,c):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(c.name)
        c.window_surface = pygame.display.set_mode((c.width, c.height))
        c.background=pygame.Surface((c.width,c.height))
        c.background.fill(pygame.Color('#000000'))
        c.manager = pygame_gui.UIManager((c.width, c.height))
        c.clock = pygame.time.Clock() #Clockを設定

        c.font = pygame.font.SysFont("Arial",32)

        return self
