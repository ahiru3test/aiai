import pygame
import pygame_gui
from C import C

### View基本クラス
class V():
    pass

### pygame初期化関連
class PG(V):
    def init(self,c):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(c.name)
        c.window_surface = pygame.display.set_mode((c.width, c.height)) #メインウィンドウ
        c.background=pygame.Surface((c.width,c.height))
        c.background.fill(pygame.Color('#000000'))
        c.manager = pygame_gui.UIManager((c.width, c.height)) #guiマネージャ
        c.clock = pygame.time.Clock() #Clockを設定

        c.font = pygame.font.SysFont("Arial",32)

        return self
    pass

    def view(self):
        print(self.c.scene)

### タイトル画面のView
class VTitle(V):
    def init(self,c):
        # text_surface = c.font.render("Input name and push enter key!", True, (255, 255, 255))
        text_surface = c.font.render(c.models["Title"].text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (c.width // 2, c.height // 2)
        c.window_surface.blit(text_surface, text_rect)

        pass


