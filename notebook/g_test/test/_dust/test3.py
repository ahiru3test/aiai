# -*- coding: utf-8 -*-
import pygame
import pygame_gui

# 画面のサイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 画面の色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 画面の番号
SCENE_TITLE = 0
SCENE_INPUT = 1
SCENE_GAME = 2

# pygameの初期化
pygame.init()

# 画面の作成
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame GUI Test")

# 時間管理用のオブジェクト
clock = pygame.time.Clock()

# GUI管理用のオブジェクト
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# タイトル画面用のクラス
class TitleScene:
    def __init__(self):
        # タイトルのラベル
        self.title_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, 0), (SCREEN_WIDTH, 100)),
            text="Pygame GUI Test",
            manager=manager
        )
        self.title_label.set_center_position((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))

        # スタートボタン
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            text="Start",
            manager=manager
        )
        self.start_button.set_center_position((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # 画面の更新
    def update(self):
        pass

    # イベントの処理
    def process_event(self, event):
        global current_scene # 現在の画面を保持する変数
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.start_button:
                    # スタートボタンが押されたら、名前入力画面に切り替える
                    current_scene = SCENE_INPUT

# 名前入力画面用のクラス
class InputScene:
    def __init__(self):
        # 名前入力の説明ラベル
        self.input_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, 0), (SCREEN_WIDTH, 100)),
            text="Please enter your name",
            manager=manager
        )
        self.input_label.set_center_position((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))

        # 名前入力用のテキストボックス
        self.input_box = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            manager=manager
        )
        self.input_box.set_center_position((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # OKボタン
        self.ok_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (100, 50)),
            text="OK",
            manager=manager
        )
        self.ok_button.set_center_position((SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4))

    # 画面の更新
    def update(self):
        pass

    # イベントの処理
    def process_event(self, event):
        global current_scene # 現在の画面を保持する変数
        global name # 名前を保持する変数
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.ok_button:
                    # OKボタンが押されたら、名前を取得して、メインゲーム画面に切り替える
                    name = self.input_box.get_text()
                    current_scene = SCENE_GAME

# メインゲーム画面用のクラス
class GameScene:
    def __init__(self):
        # 名前の表示ラベル
        self.name_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, 0), (SCREEN_WIDTH, 100)),
            text="Hello, " + name,
            manager=manager
        )
        self.name_label.set_center_position((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))

        # ゲームの内容（ここでは適当に四角形を描く）
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.dx = 5
        self.dy = 5

    # 画面の更新
    def update(self):
        # 四角形の移動
        self.rect.move_ip(self.dx, self.dy)
        # 画面の端にぶつかったら反射
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.dy = -self.dy

    # イベントの処理
    def process_event(self, event):
        pass

# 画面のオブジェクトを作成
title_scene = TitleScene()
input_scene = InputScene()
game_scene = None # 名前が決まるまで作成しない

# 現在の画面を保持する変数（最初はタイトル画面）
current_scene = SCENE_TITLE

# 名前を保持する変数
name = ""

# メインループ
running = True
while running:
    # 時間の調整
    time_delta = clock.tick(60) / 1000.0

    # イベントの処理
    for event in pygame.event.get():
        # 終了イベント
        if event.type == pygame.QUIT:
            running = False

        # GUIのイベント
        manager.process_events(event)

        # 現在の画面のイベント
        if current_scene == SCENE_TITLE:
            title_scene.process_event(event)
        elif current_scene == SCENE_INPUT:
            input_scene.process_event(event)
        elif current_scene == SCENE_GAME:
            game_scene.process_event(event)

    # 画面の更新
    manager.update(time_delta)

    if current_scene == SCENE_TITLE:
        title_scene.update()
    elif current_scene == SCENE_INPUT:
        input_scene.update()
    elif current_scene == SCENE_GAME:
        # 名前が決まったら、メインゲーム画面のオブジェクトを作成
        if game_scene is None:
            game_scene = GameScene()
        game_scene.update()

    # 画面の描画
    screen.fill(BLACK) # 画面を黒で塗りつぶす

    if current_scene == SCENE_TITLE:
        pass # タイトル画面では特に描画するものはない
    elif current_scene == SCENE_INPUT:
        pass # 名前入力画面では特に描画するものはない
    elif current_scene == SCENE_GAME:
        # 四角形を描画
        pygame.draw.rect(screen, WHITE, game_scene.rect)

    # GUIの描画
    manager.draw_ui(screen)

    # 画面の反映
    pygame.display.flip()

# pygameの終了
pygame.quit()
