import pygame
import pygame_gui
import os
from mypkg.GameBase import GameBase
from Card import Card
from Deck import Deck
from Player import Player
from Players import Players
from Field import Field

class GameSeven(GameBase):
    def ginit(self,running=True):
        if (running): return
        #デッキの初期化
        self.deck = Deck()
        #フィールドの初期化
        self.field = None

        # ユーザ名の入力
        manager = pygame_gui.UIManager((640, 480)) # UIManagerオブジェクトを作成する
        # ルートコンテナを取得する # この行を追加する
        container = manager.get_root_container()


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

       # テキストボックスをルートコンテナに追加する # この行を変更する
        container.add_element(text_box)

        # # 画面に追加
        # manager.add_element(text_box)

        loop=True
        while loop:
            # time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # イベントを処理する
                manager.process_events(event)

                # Enterキーが押されたらテキストボックスの内容を表示する
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        loop=False
                        text=text_box.get_text()
                        print(text)
            # テキストボックスのオブジェクトを画面に描画する
            manager.update(self.clock.tick(60))
            manager.draw_ui(self.screen)



        # # 入力ボックスを作成
        # input_box = pygame.TextInput()

        # プレイヤー名入力処理
        # for self.event in pygame.event.get():
            # # 入力ボックスを更新
            # input_box.update(self.event)
        # ユーザーが入力するまでループ
        # while not input_box.get_text():
        #     # イベント処理
        #     for self.event in pygame.event.get():
        #         # 入力ボックスを更新
        #         input_box.update(self.event)
        # # ユーザーが入力したら、テキストを取得
        # text = input_box.get_text()
        # # 入力ボックスを非表示
        # input_box.set_visible(False)

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
