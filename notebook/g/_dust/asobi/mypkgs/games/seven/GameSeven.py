# from time import time
# from .. import GameBase
# from ..GameBase import GameBase
# from InitSeven import *
# from . import InitSeven
# from datetime import datetime
from datetime import datetime

from SevenCardDeck import SevenCardDeck
from Card import Card
from SevenPlayer import SevenPlayer

class GameSeven:
    _instance = None

    def __init__(self):
        self.id = datetime.now()
        self.loop = 1

        scd = SevenCardDeck()
        self.card_deck:dict[Card] = scd.card_deck

        self.players:list[SevenPlayer] = spl.players

    def init(self):
        pass

    def run(self):
        while(self.loop>0):
          self.init()
          # input()
          # logic()
          # resolve()
          self.view()
          self.loop+=1

          if(self.loop>=10):
            print(self.loop)
            break # test
        pass

    def view(self):
    #    for c in self.card_deck:
    #        print(f"{c.name}:{c.image}")
        pass

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance = super().__new__(cls)
        return cls._instance


# test GameSeven init input logic check view
if (__name__=="__main__"):
  # gs = None
  gs = GameSeven()
  print(gs.id)
  gs.run()
