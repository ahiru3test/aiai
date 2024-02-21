import pygame, pygame_gui
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
        text_surface = a.font.render(
            a.m_dict["Title"].title, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (a.width // 2, a.height // 2)
        a.window_surface.blit(text_surface, text_rect)

        # テキストボックスを作成 # 追加
        a.text_box = pygame_gui.elements.ui_text_box.UITextBox(
            html_text="",
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            manager=a.manager
        )
        a.text_box.set_position((a.width // 2 - 100, 50)) # 画面上部
        a.text_box.on_text_changed = self.on_text_changed
        a.text_box.on_text_entry_finished = self.on_text_entry_finished # 追加
    
    def on_text_changed(self, event):
        # テキストボックス内のテキストを取得
        text = event.text

        # テキストをMTitleクラスのtext属性に代入
        self.a.m_dict["Title"].text = text

    def on_text_entry_finished(self, event): # 追加
        # テキストボックスの入力が完了したときにCTitleクラスのinitメソッドを呼び出す
        self.a.c_dict["Title"].init(self.a, event)

class CTitle(metaclass=SingletonMeta):
    def init(self,a, event): # 引数にeventを追加
        # テキストボックスに入力された値を取得するイベントを処理
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                # 入力された値をMTitleクラスのtext属性に代入
                print(event.text)
                a.m_dict["Title"].text = event.text
                # テストコード: MTitleクラスのtext属性を出力
                print("MTitle.text:", a.m_dict["Title"].text)
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

            a.c_dicta.scene.init(a, event) # 引数にeventを追加


class Logic(metaclass=SingletonMeta):
    def do(self, a):
        self.a = a
        pass

class Resolve(metaclass=SingletonMeta):
    def do(self, a):
        self.a = a
        if (a.scene != a.before_scene):
            ###ループの最初や画面遷移の直後に行う初期化
            a.m_dicta.scene.init(a)
            #シーン変更処理完了
            a.before_scene = a.scene
            # print(f"{self.scene} (<-{self.before_scene})")

class View(metaclass=SingletonMeta):
    def do(self, a):
        self.a = a
        a.manager.update(a.time_delta) #guiの更新
        a.window_surface.blit(a.background, (0, 0)) #画面の描画

        ### 描画時に小細工をする場合はこの辺に
        a.v_dicta.scene.init(a)
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
