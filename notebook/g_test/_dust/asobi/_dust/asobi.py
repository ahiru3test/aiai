# from games.seven import *
from .mypkgs.seven import GameSeven

if (__name__=="__main__"):
  #ここにゲーム選択ルーチンを実装する
  #今はGameSevenのみ
  gs = GameSeven()
  gs.play()
  # GameSeven.play()

