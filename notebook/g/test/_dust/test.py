import pygame
import pygame_gui

class PG:
    def __init__(self,x=640,y=480,f=60):
        pygame.init()
        pass

    def __del__(self):
        pygame.quit()

    def run(self):

        # 画面を作成する
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Pygame-gui Text Box")

        clock = pygame.time.Clock()
        manager = pygame_gui.UIManager((640, 480))

        # テキストボックスのパラメータを設定する
        text_box_parameters = {
            "relative_rect": pygame.Rect((100, 200), (400, 50)), # 位置とサイズ
            #"text": "Enter some text", # 初期テキスト # この行を削除する
            "manager": manager # UIManagerオブジェクト
        }

        # テキストボックスのオブジェクトを作成する
        text_box = pygame_gui.elements.UITextEntryLine(**text_box_parameters)

        # テキストボックスにテキストを設定する # この行を追加する
        text_box.set_text("Enter some text")

        running = True
        pass

if (__name__=="__main__"): (pg := PG()).run()

