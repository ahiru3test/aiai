import pygame
import pygame_gui

pygame.init()
pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((800, 600))

#---

name_input_window = pygame_gui.windows.UIMessageWindow(
    rect=pygame.Rect(100, 100, 600, 400),
    html_message="名前を入力してください",
    window_title="m1",
    manager=manager
)

name_input_field = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(0.1, 0.2, 0.8, 0.2),
    parent_element=name_input_window,
    initial_text="",
    manager=manager
)

#---

main_game_window = pygame_gui.windows.UIMessageWindow(
    rect=pygame.Rect(100, 100, 600, 400), 
    html_message="メイン",
    window_title="m2",
    manager=manager
)

name_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect(10, 20, 80, 20),
    text="main",
    parent_element=main_game_window,
    manager=manager
)

running = True
current_screen = 0  # 0: メインループ, 1: 名前入力画面, 2: メインゲーム画面

while running:
    time_delta = clock.tick(60) / 1000.0

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)

    # メインループ画面
    if current_screen == 0:
        # 名前がない場合、名前入力画面を表示
        if not name_input_field.get_text():
            current_screen = 1
            name_input_window.show()
        print("0")

    # 名前入力画面
    elif current_screen == 1:
        # 名前を入力したら、メインゲーム画面を表示
        if name_input_field.get_text():
            current_screen = 2
            main_game_window.show()
            name_label.set_text(name_input_field.get_text())
        print("1")

    # メインゲーム画面
    elif current_screen == 2:
        # ゲームロジック
        print("2")
        pass

    # UIの更新
    manager.update(time_delta)

    # 画面の描画
    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))
    manager.draw_ui(screen)
    pygame.display.update()
