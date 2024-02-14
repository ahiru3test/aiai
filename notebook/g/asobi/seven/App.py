import copy, random
import os
import platform
import numpy as np
from Deck import Deck
from Player import Player
from Players import Players
from Field import Field


# init input logic resolve view
class App:
    def __init__(self):
        self.loop=1
        self.deck = Deck()
        self.players = None
        self.field = None

    def run(self):
        while (self.loop>0) :
            # self.init()
            self.input()
            self.logic()
            # self.resolve()
            self.view()
            #
            if (self.loop>=10):
                print("end loop")
                break
            self.loop+=1
    
    def input(self):
        # if(self.players is None or len(self.players)==0):
        if(self.players is None):
            # players = input("参加者は誰ですか？（スペースで区切って入力）").split()
            players = ["aaa",]

            for n in range(len(players),4,1):
                players.append("")
            print(players)
            self.players = Players(players,self.deck)
    
    def logic(self):
        if(self.field is None):
            self.field = Field()

    def view(self):
        if platform.system() == "Windows":
            os.system('cls')    # Windows
        else:
            os.system('clear') # Linux or Mac
        
        if (len(self.deck.card_deck)==0):
            print("no deck...")
        else:
          for c in self.deck.card_deck:
              print(f"{c.name} {c.image}")
        if (len(self.players.players)==0):
            print("no players...")
        else:
            for p in self.players.players:
                print(f"{p.name}")
                for c in p.card_deck:
                    print(f"{c}",end=",")
                else:
                    print()


if (__name__=="__main__"):
    a=App()
    a.run()
    # for c in scd.card_deck:
    #     print(f"{c.name} {c.image}")
