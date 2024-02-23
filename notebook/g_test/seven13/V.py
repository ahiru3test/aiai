import pygame
import PG as PG
# import SingletonMeta as SingletonMeta

class SingletonMeta(type):
    # インスタンスを保持する辞書
    _instances = {}

    # インスタンスが存在するかどうかを返すメソッド
    def is_instance(cls):
        return cls in cls._instances

    # クラスのインスタンスを生成するメソッド
    def __new__(cls, name, bases, attrs):
        # メタクラスで定義したクラス変数を派生クラスの属性として追加する
        attrs["_instances"] = cls._instances
        # スーパークラスの__new__メソッドを呼び出す
        return super().__new__(cls, name, bases, attrs)

    # クラスのインスタンスを呼び出すメソッド
    def __call__(cls, *args, **kwargs):
        # インスタンスがない場合は生成する
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class AAA:
    # def __init__(self,name="MVC",width=640,height=480,frame=60):
    def __init__(self,**kwargs): #(self,name="MVC",width=640,height=480,frame=60)
        if any(k not in ["name","width","height","frame"] for k in kwargs.keys()): return
        self.__dict__.update(kwargs)
        self.scene = "Title" #今のシーン
        self.before_scene = "" #前のシーン
        self.is_running = True #ループする
        # self.a_list=[Input,Logic,Resolve,View] #1Fに行うActionList
        self.m = M()
        self.v = V()
        self.c = C()
        self.a_list=[Input] #1Fに行うActionList

        while self.is_running: [a(self.v.pg).do() for a in self.a_list] # MainLoop

# V...V,VTitle,(PG)
# M...M,
# C...C,root

class M: #-------------------------------------------------------------
    def __init__(self):
        self.dict={"":MTitle,"Title":MTitle}
        pass
class MTitle:pass

class V: #-------------------------------------------------------------
    def __init__(self):
        self.dict = {"Title",VTitle}
        # self.vlib = VLib()
        self.pg = PG().init(self)
        
        pass
    

    pass
class VLib:pass
class Input(metaclass=SingletonMeta):
    def __init__(self,a:V):
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
    def do(self):
        pass

class VTitle:
    def __init__(self):
        # root # □
        # back # ■
        # text # a

        self.background
        pass

    def set_root(self,name="",width="640",height="480"):
        pass


class C: #-------------------------------------------------------------
    def __init__(self):
        self.dict={"":CTitle,"Title":CTitle}
        pass
    def run(self):
        pass
class CTitle:pass


if (__name__=="__main__"): a=AAA(name=name,width=640,height=480,frame=60)

