import pygame
import pygame_gui

#初期化
pygame.init()

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
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # イベントを処理する
        manager.process_events(event)

        # Enterキーが押されたらテキストボックスの内容を表示する
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(text_box.get_text())

    # 画面を白色で塗りつぶす
    screen.fill((255, 255, 255))

    # テキストボックスのオブジェクトを画面に描画する
    manager.update(time_delta)
    manager.draw_ui(screen)

    # 画面を更新する
    pygame.display.flip()

pygame.quit()
