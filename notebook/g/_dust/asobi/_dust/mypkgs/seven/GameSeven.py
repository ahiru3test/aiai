# from time import time
# from .. import GameBase
# from ..GameBase import GameBase
# from InitSeven import *
# from . import InitSeven
from datetime import datetime

class GameSeven:
  #class変数
  id = datetime.now()
  loop = 1

  #classメソッド
  # @classmethod
  def play(cls):
    while(cls.loop>0):
      if(cls.loop>=10):
        print(f"end loop {cls.loop}")
        break
      cls.loop+=1

    pass

  pass



#test
if (__name__=="__main__"):
  print(GameSeven.id)
  GameSeven.play()
