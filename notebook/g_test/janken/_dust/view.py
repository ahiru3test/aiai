import tkinter as tk
from model import Player
from model import PlayerList

class View:
    def __init__(self, model):
        self.model = model

        # ウィンドウを作成する
        self.window = tk.Tk()
        self.window.title("じゃんけん")

        # プレイヤーの名前を取得する
        self.player_names = []
        for i in range(3):
            label = tk.Label(self.window, text=f"プレイヤー{i + 1}の名前:")
            label.grid(row=i, column=0)
            entry = tk.Entry(self.window)
            entry.grid(row=i, column=1)
            self.player_names.append(entry)

        # プレイヤーが選択したじゃんけんの手を入力するためのエントリを作成する
        self.choice_entries = []
        for i in range(3):
            label = tk.Label(self.window, text=f"プレイヤー{i + 1}の手:")
            label.grid(row=i, column=2)
            entry = tk.Entry(self.window)
            entry.grid(row=i, column=3)
            self.choice_entries.append(entry)

        # ボタンを作成する
        self.start_button = tk.Button(self.window, text="スタート", command=self.start_game)
        self.start_button.grid(row=3, column=0, columnspan=2)

        # 結果を表示するラベルを作成する
        self.result_label = tk.Label(self.window, text="")
        self.result_label.grid(row=4, column=0, columnspan=2)

# def start_game(self):
#     # ... (same as before)

#     # Assign the choice_entry attribute to the Entry widget for each player
#     for player, choice_entry in zip(players, self.choice_entries):
#         player.choice_entry = choice_entry

#     # ... (same as before)

    def start_game(self):
        # プレイヤーを作成する
        players = []
        for name in self.player_names:
            players.append(Player(name.get()))

        # プレイヤーのリストを作成する
        player_list = PlayerList()
        for player in players:
            player_list.add_player(player)

        # # プレイヤーに選択させる
        # for player in players:
        #     choice = player.choice_entry.get()
        #     player.choose(choice)

        # Assign the choice_entry attribute to the Entry widget for each player
        for player, choice_entry in zip(players, self.choice_entries):
            player.choice_entry = choice_entry


        # 勝者を取得する
        winners = player_list.get_winner()

        # 結果を表示する
        if winners is None:
            self.result_label.config(text="引き分けです。")
        else:
            self.result_label.config(text=f"勝者は{', '.join([winner.name for winner in winners])}です。")

    def run(self):
        self.window.mainloop()
