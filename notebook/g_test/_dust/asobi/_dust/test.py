# randomモジュールをインポート
import random

# スートとランクのリストを定義
suits = ["S", "C", "H", "D"]
ranks = list(range(1, 14))

# カードのリストを作成
cards = []
for suit in suits:
    for rank in ranks:
        cards.append(suit + str(rank))

# カードをシャッフル
random.shuffle(cards)

# カードを配る
# ここでは4人に配ると仮定
players = 4
hands = [[] for _ in range(players)]
for i in range(len(cards)):
    hands[i % players].append(cards[i])

# 結果を表示
for i in range(players):
    print(f"Player {i + 1}:", ", ".join(hands[i]))
