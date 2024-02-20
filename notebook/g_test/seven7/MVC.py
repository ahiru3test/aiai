import pygame
# from M import M
from M import *
from V import *
from C import C

### Main処理(これが実質Controllerでは？)
class Main(C):
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
        self.pg = PG().init(self)

    def ginit(self):
        self.time_delta = self.clock.tick(self.frame)/1000.0 #ループ毎のClockの設定
        if (self.scene != self.before_scene):
            ###ループの最初や画面遷移の直後に行う初期化
            self.models[self.scene]().init(self)
            #シーン変更処理完了
            self.before_scene = self.scene
            # print(f"{self.scene} (<-{self.before_scene})")
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
        self.manager.update(self.time_delta) #guiの更新
        self.window_surface.blit(self.background, (0, 0)) #画面の描画

        ### 描画時に小細工をする場合はこの辺に
        self.views[self.scene]().init(self)
        ###

        self.manager.draw_ui(self.window_surface) #guiの描画
        pygame.display.update() #pg表示の更新

    def run(self):
        while self.is_running:
            self.ginit()
            self.ginput()
            # self.glogic()
            # self.gresolve()
            self.gview()
            pass
        pass    
    pass

if (__name__=="__main__"): (m := Main()).run()
