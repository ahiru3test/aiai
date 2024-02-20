# controller.py
import pygame
import pygame_gui
# from M import *
# from V import *

class C():
    def __init__(self,c):
        self.c = c
    pass

class Controller(C):
    def __init__(self):
        self.view = View()
        self.scene = "Title" #今のシーン
        self.before_scene = "" #前のシーン
        self.scenes={"":Title,"Title":Title}
        self.is_running = True #ループする

    def ginit(self):
        if (self.scene != self.before_scene):
            ###ループの最初や画面遷移の直後に行う初期化
            self.scenesself.scene
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

            self.view.manager.process_events(event)

    def run(self):
        while self.is_running:
            self.ginit()
            self.ginput()
            # self.glogic()
            # self.gresolve()
            self.view.update()
            pass
        pass    
    pass

if (__name__=="__main__"): (c := Controller()).run()
