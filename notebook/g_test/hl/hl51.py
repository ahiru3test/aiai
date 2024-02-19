import pygame
import sys
import random

# カードの画像を用意する
# ここでは、1から13までの数字のカードの画像をcardsというリストに格納している
# 画像は、1からダウンロードしたものを使用している
cards = []
for i in range(1, 14):
    cards.append(pygame.image.load(f"card{i}.png"))

class Model:
    def __init__(self):
        # 最初のカードのインデックスをランダムに決める
        self.first_card = random.randint(0, 12)
        # 次のカードのインデックスをランダムに決める
        self.second_card = random.randint(0, 12)
        # プレイヤーの選択を保持する変数
        # Highなら1、Lowなら-1、未選択なら0とする
        self.player_choice = 0
        # ゲームの結果を保持する変数
        # 勝ちなら1、負けなら-1、引き分けなら0とする
        self.game_result = 0

class View:
    def __init__(self, model):
        self.model = model
        self.surface = pygame.Surface((400, 300))

    def draw(self):
        self.surface.fill((0, 0, 0))
        # 最初のカードの画像を表示する
        self.surface.blit(cards[self.model.first_card], (50, 100))
        # 次のカードの画像を表示する
        # ただし、プレイヤーが選択するまでは裏返しにする
        if self.model.player_choice == 0:
            self.surface.blit(pygame.transform.rotate(cards[0], 90), (250, 100))
        else:
            self.surface.blit(cards[self.model.second_card], (250, 100))
        # プレイヤーにHighかLowかを選択させる
        # HighとLowの文字を表示する
        font = pygame.font.SysFont(None, 32)
        high_text = font.render("High", True, (255, 255, 255))
        low_text = font.render("Low", True, (255, 255, 255))
        self.surface.blit(high_text, (100, 50))
        self.surface.blit(low_text, (300, 50))
        # プレイヤーの選択に応じて、HighかLowの文字を赤くする
        if self.model.player_choice == 1:
            high_text = font.render("High", True, (255, 0, 0))
            self.surface.blit(high_text, (100, 50))
        elif self.model.player_choice == -1:
            low_text = font.render("Low", True, (255, 0, 0))
            self.surface.blit(low_text, (300, 50))
        # 結果を判定する
        # プレイヤーが選択した後に、次のカードの数字と比較する
        if self.model.player_choice != 0:
            if self.model.first_card < self.model.second_card:
                # 次のカードの数字が大きい場合
                if self.model.player_choice == 1:
                    # プレイヤーがHighを選んだ場合
                    self.model.game_result = 1 # 勝ち
                else:
                    # プレイヤーがLowを選んだ場合
                    self.model.game_result = -1 # 負け
            elif self.model.first_card > self.model.second_card:
                # 次のカードの数字が小さい場合
                if self.model.player_choice == 1:
                    # プレイヤーがHighを選んだ場合
                    self.model.game_result = -1 # 負け
                else:
                    # プレイヤーがLowを選んだ場合
                    self.model.game_result = 1 # 勝ち
            else:
                # 次のカードの数字が同じ場合
                self.model.game_result = 0 # 引き分け
        # 結果を表示する
        # 結果に応じて、WinかLoseかDrawの文字を表示する
        if self.model.game_result == 1:
            # 勝ちの場合
            win_text = font.render("Win", True, (255, 255, 0))
            self.surface.blit(win_text, (200, 200))
        elif self.model.game_result == -1:
            # 負けの場合
            lose_text = font.render("Lose", True, (255, 255, 0))
            self.surface.blit(lose_text, (200, 200))
        elif self.model.game_result == 0 and self.model.player_choice != 0:
            # 引き分けの場合
            draw_text = font.render("Draw", True, (255, 255, 0))
            self.surface.blit(draw_text, (200, 200))

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # マウスがクリックされたとき
                # クリックされた位置を取得する
                x, y = pygame.mouse.get_pos()
                # HighかLowの文字の範囲内かどうか判定する
                if 100 <= x <= 150 and 50 <= y <= 80:
                    # Highの文字がクリックされた場合
                    self.model.player_choice = 1 # Highを選択
                elif 300 <= x <= 350 and 50 <= y <= 80:
                    # Lowの文字がクリックされた場合
                    self.model.player_choice = -1 # Lowを選択

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()

    model = Model()
    view = View(model)
    controller = Controller(model, view)

    running = True
    while running:
        controller.handle_events()
        view.draw()
        screen.blit(view.surface, (0, 0))
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
