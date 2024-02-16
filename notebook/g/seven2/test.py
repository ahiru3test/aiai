import pygame
import os

pygame.init()

screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

# 画像を読み込みます
# filename = os.path.dirname(__file__) + "/transp.png" #実行ファイルのパス＋ファイル名
filename = os.path.join(os.path.dirname(__file__), "Tranp3.png")
image = pygame.image.load(filename).convert_alpha()

# 背景サーフェスを作成します
background = pygame.Surface((640,480))
background.fill((0,0,0))

# 背景サーフェスに画像を描画します
background.blit(image, (0,0))

# フォントを作成します
font = pygame.font.SysFont(None, 20)
text_surface = font.render(f"座標: {0}, {0}", True, (255,255,255))

# テキストボックスの境界を作成します
text_box_rect = pygame.Rect(10,420,100,20)

# プレイヤー名のテキストサーフェスを作成します
player_name_surface = font.render("", True, (255,255,255))
text_input = False
player_name=""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # マウスがクリックされたら、現在の位置を取得します
            mouse_pos = pygame.mouse.get_pos()

            # 座標を画面に描画します
            text_surface = font.render(f"座標: {mouse_pos[0]}, {mouse_pos[1]}", True, (255,255,255))

            # テキストボックスがクリックされたら、テキストを入力できるようにします
            if text_box_rect.collidepoint(mouse_pos):
                text_input = True
            else:
                text_input = False

        elif event.type == pygame.KEYDOWN and text_input:
            # テキストボックスにテキストを入力します
            # if event.key == pygame.K_BACKSPACE:
            #     player_name_surface = font.render(player_name_surface.text[:-1], True, (255,255,255))
            # else:
            #     player_name_surface = font.render(player_name_surface.text + event.unicode, True, (255,255,255))

            if event.key == pygame.K_BACKSPACE:
                player_name = player_name[:-1] # この行を修正します
                player_name_surface = font.render(player_name, True, (255,0,255))
            else:
                player_name = player_name + event.unicode # この行を修正します
                player_name_surface = font.render(player_name, True, (255,0,255))


    # 背景サーフェスを画面に描画します
    screen.blit(background, (0,0))

    # 座標を画面に描画します
    screen.blit(text_surface, (10,460))

    # テキストボックスを描画します
    pygame.draw.rect(screen, (0,255,0), text_box_rect)

    # プレイヤー名のテキストを描画します
    screen.blit(player_name_surface, (text_box_rect.x + 5,text_box_rect.y + 5))

    # 画面を更新します
    pygame.display.update()

    # フレームレートを制限します
    clock.tick(60)

pygame.quit()
