import random

# class Players:
#    def __init__(self):
#       self.players = {}
#       self.deck = []

class Player:
    # players:list[Player] = []
    players = {}
    def __init__(self):
        # self.players = {}
        self.deck = []

#参加者を決める
# players = input("参加者は誰ですか？（スペースで区切って入力）").split()
players = ["aaa",]
for n in range(len(players),4,1):
    players.append(f"Player{n+1}")

for n in range(4):
    Player.players[n]=players[n]
    # print(pls.players[n])

#カードを配る
card_dict = {}
for s in ["S","C","H","D"]:
  for n in range(1,14):
    card_dict[s+str(n)]=""

# for k,v in card_dict.items():
#   print(f"{k}:{v}", end=",")
# else:
#   print()
card_list = list(card_dict.keys())
random.shuffle(card_list)

# print(card_list)
# for k in card_dict.keys():
#     card_list.append(k)
n=0
# for c in card_list:
#   p = Player.players[n]
#   p.deck.append(c)
#   print(f"{c}",end=",")
