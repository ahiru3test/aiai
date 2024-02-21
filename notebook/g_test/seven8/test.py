import pygame
import pygame_gui

### Model -------------------------------------------------------------
class MTitle():
    text = "Input name and push enter key!"
    def init(self,c):pass

### View
class PG():
    def init(self,c):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(c.name)
        c.window_surface = pygame.display.set_mode((c.width, c.height))
        c.background=pygame.Surface((c.width,c.height))
        c.background.fill(pygame.Color('#000000'))
        c.manager = pygame_gui.UIManager((c.width, c.height))
        c.clock = pygame.time.Clock() #Clockを設定

        c.font = pygame.font.SysFont("Arial",32)

        return self

    def view(self):
        print(self.c.scene)

class VTitle():
    def init(self,c):
        text_surface = c.font.render(
            c.models["Title"].text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (c.width // 2, c.height // 2)
        c.window_surface.blit(text_surface, text_rect)

        # テキストボックスを作成 # 追加
        c.text_box = pygame_gui.elements.ui_text_box.UITextBox(
            html_text="",
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            manager=c.manager
        )
        c.text_box.set_position((c.width // 2 - 100, 50)) # 画面上部

### Controller
class Main():
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
        # テキストボックスに入力された文字を保持する変数を用意する # 追加
        self.input_text = ""

    def ginit(self):
        self.time_delta = self.clock.tick(self.frame)/1000.0 #Clock設定
        if (self.scene != self.before_scene):
            ###ループの最初や画面遷移の直後に行う初期化
            self.modelsself.scene.init(self)
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
            # テキストボックスのイベントを検出して、入力された文字を変数に追加する # 追加
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == self.text_box:
                        self.input_text += event.text
                elif event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                    if event.ui_element == self.text_box:
                        self.input_text = event.text
            # Enterキーが押されたら、変数に保持された文字を反映する # 追加
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # ここでは、変数に保持された文字をコンソールに出力する
                    print(self.input_text)
                    # テキストボックスを空にする
                    self.text_box.set_text("")

    def gview(self):
        self.manager.update(self.time_delta) #guiの更新
        self.window_surface.blit(self.background, (0, 0)) #画面の描画

        ### 描画時に小細工をする場合はこの辺に
        self.viewsself.scene.init(self)
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
