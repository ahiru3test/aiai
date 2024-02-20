import pygame
import pygame_gui

class C():
    def __init__(self,c):
        self.c = c
    pass
class M(C):
    pass
class V(C):
    pass

class PG(V):
    def init(self):
        pygame.init()
        pygame.display.set_caption(self.c.name)
        self.c.window_surface = pygame.display.set_mode((self.c.width, self.c.height)) #メインウィンドウ
        self.c.background=pygame.Surface((self.c.width,self.c.height))
        self.c.background.fill(pygame.Color('#000000'))
        self.c.manager = pygame_gui.UIManager((self.c.width, self.c.height)) #guiマネージャ
        self.c.clock = pygame.time.Clock() #Clockを設定
        return self
    pass

class Scene(M):
    pass

class Title(Scene):
    def init(self,c):
        print("Title")
        pass
    pass

# class Scenes(M):
#     pass

class Main(C):
    def __init__(self,name="MVC",width=640,height=480,frame=60):
        self.name=name
        self.width=width
        self.height=height
        self.frame=frame
        self.scene = "Title" #今のシーン
        self.before_scene = "" #前のシーン
        self.scenes={"":Title,"Title":Title}
        self.is_running = True #ループする

        #---ここから
        # pygame.init()
        # pygame.display.set_caption(self.name)
        # self.window_surface = pygame.display.set_mode((self.width, self.height)) #メインウィンドウ
        # self.background=pygame.Surface((self.width,self.height))
        # self.background.fill(pygame.Color('#000000'))
        # self.manager = pygame_gui.UIManager((self.width, self.height)) #guiマネージャ
        # self.clock = pygame.time.Clock() #Clockを設定

        self.pg = PG(self).init()

    def ginit(self):
        self.time_delta = self.clock.tick(self.frame)/1000.0 #ループ毎のClockの設定
        if (self.scene != self.before_scene):
            ###ループの最初や画面遷移の直後に行う初期化
            self.scenes[self.scene](self)
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
            pass
        pass    
    pass



if (__name__=="__main__"): (m := Main()).run()
