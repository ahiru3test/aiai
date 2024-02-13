import copy
import numpy as np
from mypkgs.LoopBase import *

# sevenのメインループクラス
class SevenLoop(LoopBase):
    card_deck = []
    seven_players = []
    n=0

    #Sevenの初期化
    def init(self):
        #ゲーム開始時にデッキを作成して各プレイヤーに配布する
        if(not SevenLoop.card_deck and not SevenLoop.seven_players):
            print(f"{SevenLoop.n}:{SevenLoop.seven_players}")
            SevenLoop.card_deck = self.set_card_deck()
        # if(not SevenLoop.seven_players):
            players=[]
            players.append(input("参加者は誰ですか？"))
            self.set_players(players)
            for p in SevenLoop.seven_players:
                print(f"name:{p.name} card_deck:{p.card_deck}")
        pass

    def set_card_deck(self) -> list :
        card_deck =[]
        for s in ["S","C","H","D"]:
            for c in range(1,14,1):
                sss=s+str(c)
                # print(f"sss:{sss}")
                card_deck.append(sss)
        card_deck.sort()
        return copy.deepcopy(card_deck)
    
    def set_players(self,name) -> list:
        players = []
        for p in range(0,4):
            # print(p)
            str = ""
            if p<len(name):
                s=name[p]
            SevenLoop.seven_players.append(SevenPlayer(s))
        SevenLoop.seven_players
        index = 0
        for c in SevenLoop.card_deck:
            print(f"c2: {c}")
            SevenLoop.seven_players[index].card_deck.append(c)
            index += 1
            if index >=4:
                index = 0
        
        print(SevenLoop.seven_players)
        for sp in SevenLoop.seven_players:
            print(sp.name)
            print(sp.card_deck)

        return players
        pass


    def loop(self):
        SevenLoop.n=0
        while(self.loop):
            self.init()
            self.input()
            self.logic()
            self.check()
            self.view()
            if SevenLoop.n>10:
                self.loop=False
            SevenLoop.n+=1
        
    pass



class SevenPlayer:
    player_names = ["Player1","Player2","Player3","Player4"]
    players=[]

    # コンストラクタ
    # self.name
    # self.card_deck
    def __init__(self, name=""):
        if name=="":
            self.name = SevenPlayer.player_names[len(SevenPlayer.players)]
        else:
            self.name = name
        
        self.card_deck = []

        pass

def main():
    sl=SevenLoop()
    sl.loop()

if __name__ == "__main__":
    main()
