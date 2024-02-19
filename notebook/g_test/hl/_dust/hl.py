import pygame
import random

# 画面の初期化
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# フォントの初期化
font = pygame.font.SysFont("Arial", 32)

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# ゲームの状態
STATE_START = 0
STATE_PLAY = 1
STATE_END = 2
state = STATE_START

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
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if state == STATE_PLAY:
                if event.key == pygame.K_4:
                    player_choice = "low"
                elif event.key == pygame.K_6:
                    player_choice = "high"

    # ゲームの状態に応じた処理
    if state == STATE_START:
        # スタート画面の描画
        screen.fill(BLACK)
        text = font.render("High and Low", True, WHITE)
        text_rect = text.get_rect(center=(320, 240))
        screen.blit(text, text_rect)
        text = font.render("Press any key to start", True, WHITE)
        text_rect = text.get_rect(center=(320, 320))
        screen.blit(text, text_rect)
        pygame.display.flip()

        # キー入力待ち
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    waiting = False

        # ゲーム開始
        state = STATE_PLAY

    elif state == STATE_PLAY:
        # ゲーム画面の描画
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
                state = STATE_END
                result = "Win!"
            else:
                state = STATE_END
                result = "Lose..."

        pygame.display.flip()

    elif state == STATE_END:
        # 終了画面の描画
        screen.fill(BLACK)
        text = font.render(result, True, WHITE)
        text_rect = text.get_rect(center=(320, 240))
        screen.blit(text, text_rect)
        text = font.render("Press any key to restart", True, WHITE)
        text_rect = text.get_rect(center=(320, 320))
        screen.blit(text, text_rect)
        pygame.display.flip()
