import pygame
from pygame_gui import UIManager, UI_TEXT_ENTRY_CHANGED, UI_TEXT_ENTRY_FINISHED
from pygame_gui.elements import UIWindow, UITextEntryBox, UITextBox
from PG import PG
from SingletonMeta import SingletonMeta

class MTitle():
    title = "Input name and push enter key!"
    text = ""
    def init(self,a):
        self.a = a

class VTitle(metaclass=SingletonMeta):
    def init(self,a):
        self.a=a
        a.notepad_window = UIWindow(
            pygame.Rect(50, 20, 300, 400)
            , window_display_title="Pygame Notepad")
        a.text_entry_box = UITextEntryBox(
            relative_rect=pygame.Rect(
                (0, 0),
                a.notepad_window.get_container().get_size()),
            initial_text="",
            container=a.notepad_window)
        #button

class CTitle(metaclass=SingletonMeta):
    def init(self,a):
        print("MTitle.text:", a.m_dict["Title"].text)
        # if c.event.type == pygame.USEREVENT:
        #     if c.event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
        #         # 入力された値をMTitleクラスのtext属性に代入
        #         print(c.event.text)
        #         c.m_dict["Title"].text = c.event.text
        self.a = a

class Input(metaclass=SingletonMeta): #--------------------------------
    def do(self, a):
        self.a=a
        a.time_delta = a.clock.tick(a.frame)/1000.0 #Clock設定
        ###イベント周りの処理はこの辺で
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                a.is_running = False

            ### add event action
            # if event.type == pygame_gui.UI_BUTTON_PRESSED:
            #     if event.ui_element == hello_button:
            #         print('Hello World!')

            a.manager.process_events(event)

            a.c_dict[a.scene]().init(a)


class Logic(metaclass=SingletonMeta):
    def do(self, a):
        self.a = a
        pass

class Resolve(metaclass=SingletonMeta):
    def do(self, a):
        self.a = a
        if (a.scene != a.before_scene):
            ###ループの最初や画面遷移の直後に行う初期化
            a.m_dict[a.scene]().init(a)
            #シーン変更処理完了
            a.before_scene = a.scene
            # print(f"{self.scene} (<-{self.before_scene})")

class View(metaclass=SingletonMeta):
    def do(self, a):
        self.a = a
        a.manager.update(a.time_delta) #guiの更新
        a.window_surface.blit(a.background, (0, 0)) #画面の描画

        ### 描画時に小細工をする場合はこの辺に
        a.v_dict[a.scene]().init(a)
        ###

        a.manager.draw_ui(a.window_surface) #guiの描画
        pygame.display.update() #pg表示の更新

class Main(metaclass=SingletonMeta): # main is a
    def __init__(self,name="MVC",width=640,height=480,frame=60):
        self.name=name
        self.width=width
        self.height=height
        self.frame=frame

        self.scene = "Title" #今のシーン
        self.before_scene = "" #前のシーン
        self.b_list=[Input,Logic,Resolve,View]
        self.m_dict={"":MTitle,"Title":MTitle}
        self.v_dict={"":VTitle,"Title":VTitle}
        self.c_dict={"":CTitle,"Title":CTitle}
        self.is_running = True #ループする

        self.pg = PG().init(self)

        while self.is_running:
            for b in self.b_list:
                b().do(self)

if (__name__=="__main__"): Main()
