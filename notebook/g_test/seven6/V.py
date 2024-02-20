# view.py
import pygame
import pygame_gui
from C import C

class View(C):
    def __init__(self, width=640, height=480, frame=60):
        self.width = width
        self.height = height
        self.frame = frame
        pygame.init()
        pygame.display.set_caption("MVC")
        self.window_surface = pygame.display.set_mode((self.width, self.height)) #メインウィンドウ
        self.background=pygame.Surface((self.width,self.height))
        self.background.fill(pygame.Color('#000000'))
        self.manager = pygame_gui.UIManager((self.width, self.height)) #guiマネージャ
        self.clock = pygame.time.Clock() #Clockを設定
        self.time_delta = 0

    def update(self):
        self.time_delta = self.clock.tick(self.frame)/1000.0 #ループ毎のClockの設定
        self.manager.update(self.time_delta) #guiの更新
        self.window_surface.blit(self.background, (0, 0)) #画面の描画
        self.manager.draw_ui(self.window_surface) #guiの描画
        pygame.display.update() #pg表示の更新
