# -*- coding: utf-8 -*-
import pygame
import pygame_gui

# ADRモデルのクラス定義
class Action: #MVCのController相当
    # コンストラクタでDomainとResponderを注入する
    def __init__(self, domain, responder):
        self.domain = domain
        self.responder = responder

    # ユーザのリクエストを受け付けて処理する
    def handle_request(self, event):
        # テキストボックスの入力をDomainに渡す
        if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            self.domain.set_text(text_box.get_text()) # ここを変更する
        # OKボタンが押されたらResponderにレスポンスを渡す
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            self.responder.show_message(self.domain.get_text())

class Domain: #MVCのModel相当
    # コンストラクタでテキストを初期化する
    def __init__(self):
        self.text = ""

    # テキストをセットする
    def set_text(self, text):
        self.text = text

    # テキストをゲットする
    def get_text(self):
        return self.text

class Responder: #MVCのView相当
    # コンストラクタでマネージャーとメッセージボックスを作成する
    def __init__(self, manager):
        self.manager = manager
        self.message_box = pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect((100, 100), (300, 200)),
            html_message="",
            manager=self.manager
        )
        self.message_box.hide()

    # メッセージボックスにテキストを表示する
    def show_message(self, text):
        self.message_box.html_message = text
        self.message_box.rebuild()
        self.message_box.show()

# pygameの初期化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ADR Example")
clock = pygame.time.Clock()

# pygame_guiのマネージャーを作成
manager = pygame_gui.UIManager((800, 600))

# ADRモデルのインスタンスを作成
domain = Domain()
responder = Responder(manager)
action = Action(domain, responder)

# テキストボックスとOKボタンを作成
text_box = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((300, 250), (200, 50)),
    manager=manager
)
ok_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((550, 250), (100, 50)),
    text="OK",
    manager=manager
)

# メインループ
running = True
while running:
    # 時間の更新
    time_delta = clock.tick(60) / 1000.0

    # イベントの処理
    for event in pygame.event.get():
        # 終了イベント
        if event.type == pygame.QUIT:
            running = False
        # pygame_guiのイベント
        if event.type == pygame.USEREVENT:
            # Actionにイベントを渡す
            action.handle_request(event)
        # マネージャーにイベントを渡す
        manager.process_events(event)

    # 画面の描画
    screen.fill((255, 255, 255))
    manager.draw_ui(screen)
    pygame.display.update()

    # マネージャーの更新
    manager.update(time_delta)

# pygameの終了
pygame.quit()
