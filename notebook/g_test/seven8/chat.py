import pygame
import pygame_gui

# Title画面のモデルクラス
class MTitle(object):
    text = "Input name and push enter key!"

# pygame初期化関連
class PG(object):
    def __init__(self,c):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(c.name)
        c.window_surface = pygame.display.set_mode((c.width, c.height)) #メインウィンドウ
        c.background=pygame.Surface((c.width,c.height))
        c.background.fill(pygame.Color('#000000'))
        c.manager = pygame_gui.UIManager((c.width, c.height)) #guiマネージャ
        c.clock = pygame.time.Clock() #Clockを設定

        c.font = pygame.font.SysFont("Arial",32)

# タイトル画面のView
class VTitle(object):
    def __init__(self,c):
        text_surface = c.font.render(c.models["Title"].text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (c.width // 2, c.height // 2)
        c.window_surface.blit(text_surface, text_rect)

# Main処理(これが実質Controllerでは？)
class Main(object):
    def __init__(self,name="MVC",width=640,height=480,frame=60):
        self.name=name
        self.width=width
        self.height=height
        self.frame=frame
        self.scene = "Title" #今のシーン
        self.before_scene = "" #前のシーン
        self.models={"":MTitle,"Title":MTitle}
        self.views={"":VTitle,"Title":VTitle}
        self.is_running = True #ループする
        self.pg = PG(self)

    def initialize(self):
        self.time_delta = self.clock.tick(self.frame)/1000.0 #ループ毎のClockの設定
        if (self.scene != self.before_scene):
            #ループの最初や画面遷移の直後に行う初期化
            self.modelsself.scene
            #シーン変更処理完了
            self.before_scene = self.scene

    def handle_events(self):
        #イベント周りの処理はこの辺で
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            # add event action
            # if event.type == pygame_gui.UI_BUTTON_PRESSED:
            #     if event.ui_element == hello_button:
            #         print('Hello World!')

            self.manager.process_events(event)

    def draw(self):
        self.manager.update(self.time_delta) #guiの更新
        self.window_surface.blit(self.background, (0, 0)) #画面の描画

        # 描画時に小細工をする場合はこの辺に
        self.viewsself.scene

        self.manager.draw_ui(self.window_surface) #guiの描画
        pygame.display.update() #pg表示の更新

    def run(self):
        while self.is_running:
            self.initialize()
            self.handle_events()
            self.draw()

if (__name__=="__main__"):
    m = Main()
    m.run()
