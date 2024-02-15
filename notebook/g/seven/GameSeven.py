import pygame
from mypkg.GameBase import GameBase
from Card import Card
from Deck import Deck
from Player import Player
from Players import Players
from Field import Field

class GameSeven(GameBase):
    def ginit(self,running=True):
        if (running): return
        self.deck = Deck()
        self.field = None

        # 入力ボックスを作成
        input_box = pygame.TextInput()

        # プレイヤー名入力処理
        for self.event in pygame.event.get():
            # 入力ボックスを更新
            input_box.update(self.event)
        # ユーザーが入力するまでループ
        while not input_box.get_text():
            # イベント処理
            for self.event in pygame.event.get():
                # 入力ボックスを更新
                input_box.update(self.event)
        # ユーザーが入力したら、テキストを取得
        text = input_box.get_text()
        # 入力ボックスを非表示
        input_box.set_visible(False)
        # プレイヤーの設定
        players = [text,]
        for n in range(len(players),4,1):
            players.append("")
        print(players)
        self.players = Players(players,self.deck)

    def ginput(self):
        if(self.players is None):
            # players = input("参加者は誰ですか？（スペースで区切って入力）").split()
            players = ["aaa",]
            for n in range(len(players),4,1):
                players.append("")
            print(players)
            self.players = Players(players,self.deck)

        pass

    def gview(self):
        print(self.deck)
        pass

if (__name__=="__main__"): (g := GameSeven()).run()



# input_box = InputBox(100, 100, 140, 32)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         input_box.handle_event(event)

#     screen.fill((30, 30, 30))
#     input_box.draw(screen)

#     pygame.display.flip()



# # 入力ボックスを作成
# input_box = pygame.TextInput()

# # ゲームループ
# while True:
#     # イベント処理
#     for event in pygame.event.get():
#         # 入力ボックスを更新
#         input_box.update(event)

#     # ユーザーが入力するまでループ
#     while not input_box.get_text():
#         # イベント処理
#         for event in pygame.event.get():
#             # 入力ボックスを更新
#             input_box.update(event)

#     # ユーザーが入力したら、テキストを取得
#     text = input_box.get_text()

#     # 入力ボックスを非表示
#     input_box.set_visible(False)

#     # テキストを表示
#     print(text)
