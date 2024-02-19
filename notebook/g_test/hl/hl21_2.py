import pygame
import random

# Pygameを初期化する
pygame.init()

# 画面を作成する
screen = pygame.display.set_mode((640, 480))

# タイトルを設定する
pygame.display.set_caption("High and Low")

# フォントを作成する
font = pygame.font.SysFont("Arial", 32)

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 数字のリスト
numbers = list(range(1, 11))

# CPUの数字
cpu_number1 = random.choice(numbers)
cpu_number2 = random.choice(numbers)

# プレイヤーの選択
player_choice = None

# ゲームのループ
running = True
while running:
    # イベントを処理する
    for event in pygame.event.get():
        # ウィンドウの×ボタンを押したら終了する
        if event.type == pygame.QUIT:
            running = False
        # キーが押されたとき
        elif event.type == pygame.KEYDOWN:
            # 4キーを押したらプレイヤーの選択をLowにする
            if event.key == pygame.K_4:
                player_choice = "low"
            # 6キーを押したらプレイヤーの選択をHighにする
            elif event.key == pygame.K_6:
                player_choice = "high"

    # 画面を黒色で塗りつぶす
    screen.fill(BLACK)

    # CPUの数字の描画
    text = font.render(str(cpu_number1), True, WHITE)
    text_rect = text.get_rect(center=(200, 240))
    screen.blit(text, text_rect)
    text = font.render("?", True, WHITE)
    text_rect = text.get_rect(center=(440, 240))
    screen.blit(text, text_rect)

    # プレイヤーの選択の描画
    if player_choice is not None:
        if player_choice == "low":
            text = font.render("Low", True, GREEN)
        else:
            text = font.render("High", True, RED)
        text_rect = text.get_rect(center=(320, 360))
        screen.blit(text, text_rect)

    # 勝敗判定
    if player_choice is not None:
        if (player_choice == "low" and cpu_number2 < cpu_number1) or (player_choice == "high" and cpu_number2 > cpu_number1):
            result = "You win!"
        else:
            result = "You lose..."
        # 結果の描画
        text = font.render(result, True, WHITE)
        text_rect = text.get_rect(center=(320, 120))
        screen.blit(text, text_rect)

    # 画面を更新する
    pygame.display.flip()

# Pygameを終了する
pygame.quit()
