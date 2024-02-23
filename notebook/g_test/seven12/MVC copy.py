import pygame
from pygame_gui import UIManager, UI_TEXT_ENTRY_CHANGED, UI_TEXT_ENTRY_FINISHED
from pygame_gui.elements import UIWindow, UITextEntryBox, UITextBox
from PG import PG
# from SingletonMeta import SingletonMeta

class SingletonMeta(type):
    # インスタンスを保持する辞書
    _instances = {}

    # インスタンスが存在するかどうかを返すメソッド
    # def is_instance(cls):
    #     return False if cls._instances is None else cls in cls._instances

    def is_instance(cls):
        if (cls._instances is None): return False
        return cls in cls._instances

    # クラスのインスタンスを生成するメソッド
    def __new__(cls, name, bases, attrs):
        # メタクラスで定義したメソッドを派生クラスの属性として追加する
        attrs["is_instance"] = cls.is_instance
        # スーパークラスの__new__メソッドを呼び出す
        return super().__new__(cls, name, bases, attrs)

    # クラスのインスタンスを呼び出すメソッド
    def __call__(cls, *args, **kwargs):
        # インスタンスがない場合は生成する
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MTitle():
    title = "Input name and push enter key!"
    text = ""
    def init(self,a):
        self.a = a

class VTitle(metaclass=SingletonMeta):
    def init(self,a):
        print(self.is_instance())

        self.a=a

class CTitle(metaclass=SingletonMeta):
    def init(self,a):
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