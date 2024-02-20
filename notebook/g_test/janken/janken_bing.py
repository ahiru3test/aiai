# モジュールのインポート
import tkinter as tk
import random

# Model
# Playerクラス
class Player:
    def __init__(self, name):
        self.name = name # プレイヤーの名前
        self.hand = None # プレイヤーの出した手
        self.result = None # プレイヤーの勝敗結果

# PlayerListクラス
class PlayerList:
    def __init__(self):
        self.players = [] # Playerクラスのインスタンスを格納するリスト

    # プレイヤーを追加するメソッド
    def add_player(self, player):
        self.players.append(player)

    # プレイヤーの数を返すメソッド
    def count(self):
        return len(self.players)

    # プレイヤーの名前のリストを返すメソッド
    def names(self):
        return [player.name for player in self.players]

    # プレイヤーの手のリストを返すメソッド
    def hands(self):
        return [player.hand for player in self.players]

    # プレイヤーの結果のリストを返すメソッド
    def results(self):
        return [player.result for player in self.players]

class Janken:
    def __init__(self):
        self.hands = ["グー", "チョキ", "パー"] # じゃんけんの手の種類
        self.results = ["勝ち", "負け", "あいこ"] # じゃんけんの結果の種類

    def decide_hand(self):
        return random.choice(self.hands)

    def judge(self, player_list):
        # 3人のプレイヤーの手を取得
        hands = player_list.hands()
        # 3人のプレイヤーの手が同じならあいこ
        if len(set(hands)) == 1:
            for player in player_list.players:
                player.result = self.results[2]
        # 3人のプレイヤーの手が異なるなら
        elif len(set(hands)) == 3:
            # グー、チョキ、パーの順に並べる
            sorted_hands = sorted(hands, key=self.hands.index)
            # グーとパーの間にチョキがあるなら、グーが勝ち、チョキとパーが負け
            if sorted_hands[1] == self.hands[1]:
                for player in player_list.players:
                    if player.hand == self.hands[0]:
                        player.result = self.results[0]
                    else:
                        player.result = self.results[1]
            # グーとチョキの間にパーがあるなら、パーが勝ち、グーとチョキが負け
            elif sorted_hands[1] == self.hands[2]:
                for player in player_list.players:
                    if player.hand == self.hands[2]:
                        player.result = self.results[0]
                    else:
                        player.result = self.results[1]
        # 2人のプレイヤーの手が同じなら
        else:
            # 同じ手を出したプレイヤーをあいこにする
            same_hand = list(set(hands))[0]
            for player in player_list.players:
                if player.hand == same_hand:
                    player.result = self.results[2]
            # 異なる手を出したプレイヤーと同じ手を出したプレイヤーの勝敗を判定する
            diff_hand = list(set(hands))[1]
            diff_player = None
            same_player = None
            for player in player_list.players:
                if player.hand == diff_hand:
                    diff_player = player
                elif player.hand == same_hand:
                    same_player = player
            # グーとチョキなら、グーが勝ち、チョキが負け
            if (same_hand, diff_hand) == (self.hands[0], self.hands[1]):
                same_player.result = self.results[0]
                diff_player.result = self.results[1]
            # チョキとパーなら、チョキが勝ち、パーが負け
            elif (same_hand, diff_hand) == (self.hands[1], self.hands[2]):
                same_player.result = self.results[0]
                diff_player.result = self.results[1]
            # パーとグーなら、パーが勝ち、グーが負け
            elif (same_hand, diff_hand) == (self.hands[2], self.hands[0]):
                same_player.result = self.results[0]
                diff_player.result = self.results[1]

class JankenView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller # Controllerのインスタンスを保持
        self.pack()
        # じゃんけんの画面を作成
        self.create_widgets()

    def create_widgets(self):
        self.name_labels = []
        self.result_labels = []
        for i in range(self.controller.player_list.count()):
            name_label = tk.Label(self, text=self.controller.player_list.players[i].name)
            name_label.grid(row=i, column=0, padx=10, pady=10)
            self.name_labels.append(name_label)
            result_label = tk.Label(self, text="")
            result_label.grid(row=i, column=1, padx=10, pady=10)
            self.result_labels.append(result_label)
        self.hand_buttons = []
        for i in range(len(self.controller.janken.hands)):
            hand_button = tk.Button(self, text=self.controller.janken.hands[i])
            hand_button.grid(row=3, column=i, padx=10, pady=10)
            hand_button["command"] = lambda hand=self.controller.janken.hands[i]: self.controller.play(hand)
            self.hand_buttons.append(hand_button)
        self.retry_button = tk

if __name__ == '__main__':
    root=tk.Tk()
    root.geometry('210x280+100+100')
    root.title("Janken")
    app = Janken(master=root)
    app.mainloop()
