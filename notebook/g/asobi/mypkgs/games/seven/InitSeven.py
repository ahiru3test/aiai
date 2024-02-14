from datetime import datetime
from GameSeven import *
# from . import GameSeven

#SevenGameの初期化クラス
class InitSeven:
  id = datetime.now()
  g:GameSeven

  def __init__(self, g:GameSeven):
    self.g = g
    pass

  pass



#test
if (__name__=="__main__"):
  print(InitSeven.id)
