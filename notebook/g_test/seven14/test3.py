# -*- coding: utf-8 -*-
import pygame
import pygame_gui
import os

# ADRモデルのクラス定義
class Action:
    # コンストラクタでDomainとResponderを注入する
    def __init__(self, domain, responder):
        self.domain = domain
        self.responder = responder

    # ユーザのリクエストを受け付けて処理する
    def handle_request(self, event):
        # ファイル選択ボタンが押されたら、ファイルダイアログを開く
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == responder.file_button:
            self.responder.open_file_dialog()
        # ファイルダイアログでファイルが選択されたら、Domainにファイル名を渡す
        if event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
            self.domain.load_image(event.text)
        # 画像情報ボタンが押されたら、Responderに画像情報を渡す
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == responder.info_button:
            self.responder.show_image_info(self.domain.get_image_info())

class Domain:
    # コンストラクタで画像と画像情報を初期化する
    def __init__(self):
        self.image = None
        self.image_info = None

    # 画像ファイルを読み込む
    def load_image(self, file_name):
        # ファイル名が有効なら、pygameで画像を読み込む
        if os.path.isfile(file_name):
            self.image = pygame.image.load(file_name).convert()
            # 画像のサイズと色数を取得する
            width, height = self.image.get_size()
            if self.image.get_bitsize() <= 8:
                colors = self.image.get_palette()
            else:
                colors = []
            # 画像情報を文字列に格納する
            self.image_info = f"File name: {file_name}\nSize: {width} x {height}\nColors: {len(colors)}"
        else:
            # ファイル名が無効なら、画像と画像情報をNoneにする
            self.image = None
            self.image_info = None

    # 画像を返す
    def get_image(self):
        return self.image

    # 画像情報を返す
    def get_image_info(self):
        return self.image_info

class Responder:
    # コンストラクタでマネージャーとウィジェットを作成する
    def __init__(self, manager):
        self.manager = manager
        # ファイル選択ボタンを作成する
        self.file_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10, 10), (100, 50)),
            text="Select File",
            manager=self.manager
        )
        # 画像情報ボタンを作成する
        self.info_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((120, 10), (100, 50)),
            text="Show Info",
            manager=self.manager
        )
        # ファイルダイアログを作成する
        self.file_dialog = pygame_gui.windows.UIFileDialog(
            rect=pygame.Rect((200, 200), (400, 300)),
            manager=self.manager,
            window_title="Select an image file",
            initial_file_path=os.getcwd(),
            allow_existing_files_only=True
        )
        self.file_dialog.hide()
        # メッセージボックスを作成する
        self.message_box = pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect((200, 200), (400, 300)),
            html_message="",
            manager=self.manager,
            window_title="Image Info"
        )
        self.message_box.hide()

    # ファイルダイアログを開く
    def open_file_dialog(self):
        self.file_dialog.show()

    # 画像情報をメッセージボックスに表示する
    def show_image_info(self, image_info):
        # 画像情報が有効なら、メッセージボックスに表示する
        if image_info:
            self.message_box.html_message = image_info
            self.message_box.rebuild()
            self.message_box.show()
        else:
            # 画像情報が無効なら、メッセージボックスを隠す
            self.message_box.hide()

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
    # 画像が有効なら、画面に描画する
    image = domain.get_image()
    if image:
        screen.blit(image, (200, 100))
    manager.draw_ui(screen)
    pygame.display.update()

    # マネージャーの更新
    manager.update(time_delta)

# pygameの終了
pygame.quit()
