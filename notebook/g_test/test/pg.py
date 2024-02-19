import pygame
import pygame_gui

class PG:
    def __init__(self):
        pygame.init() #pygame初期化
        pygame.display.set_caption('Quick Start') #ウィンドウタイトル
        self.window_surface = pygame.display.set_mode((800, 600)) #メインウィンドウ
        self.background = pygame.Surface((800, 600)) #メインの背景
        self.background.fill(pygame.Color('#000000'))
        self.manager = pygame_gui.UIManager((800, 600)) #guiマネージャ
        self.scene = 0 #現在のシーン
        self.before_scene = -1 #以前のシーン
        self.clock = pygame.time.Clock() #Clockを設定
        self.is_running = True #ループする

    def ginit(self):
        self.time_delta = self.clock.tick(60)/1000.0 #ループ毎のClockの設定
        if (self.scene != self.before_scene):
            ###ループの最初や画面遷移の直後に行う初期化
            pass
        pass


    def ginput(self):
        ###イベント周りの処理はこの辺で
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            ### add event action
            # if event.type == pygame_gui.UI_BUTTON_PRESSED:
            #     if event.ui_element == hello_button:
            #         print('Hello World!')

            self.manager.process_events(event)

    def gview(self):
        ### 描画時に小細工をする場合はこの辺に

        self.manager.update(self.time_delta) #guiの更新
        self.window_surface.blit(self.background, (0, 0)) #画面の描画
        self.manager.draw_ui(self.window_surface) #guiの描画
        pygame.display.update() #pg表示の更新

    def run(self):
        while self.is_running:
            self.ginit()
            self.ginput()
            # self.glogic()
            # self.gresolve()
            self.gview()

if (__name__=="__main__"): (pg := PG()).run()
