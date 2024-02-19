
import pygame
import pygame_gui

class PG:
    def __init__(self,window_name:str="PG",x:int=640,y:int=480,f:int=60):
        pygame.init() #pygame初期化
        pygame.display.set_caption(window_name) #ウィンドウタイトル
        self.window_surface = pygame.display.set_mode((x, y)) #メインウィンドウ
        self.background = pygame.Surface((x, y)) #メインの背景
        self.background.fill(pygame.Color('#000000'))
        self.manager = pygame_gui.UIManager((x, y)) #guiマネージャ
        self.scene = "PG" #現在のシーン
        self.before_scene = "" #以前のシーン
        self.scenes={"PG":"self._PG()","Main":"self._Main()"}
        self.clock = pygame.time.Clock() #Clockを設定
        self.frame=f #フレーム設定
        self.is_running = True #ループする

    def ginit(self):
        self.time_delta = self.clock.tick(self.frame)/1000.0 #ループ毎のClockの設定
        if (self.scene != self.before_scene):
            ###ループの最初や画面遷移の直後に行う初期化
            print(self.scene)
            print(self.scenes)
            getattr(self, f"{self.scenes[self.scene]}")()
            #シーン変更処理完了
            self.before_scene == self.scene
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
    
    def _PG(self):
        print(__name__)
        pass
    
    def _Main(self):
        print(__name__)
        pass

class pg1(PG):
    pass

if (__name__=="__main__"): (pg := PG()).run()
