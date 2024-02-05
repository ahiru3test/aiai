import random

class HitoriNumber:
  """
  HItori Numberの回答を作成するクラス
  """

  def __init__(self, n):
    """
    コンストラクタ

    引数:
      n: マス目のサイズ
    """
    # マス目のサイズを保存する
    self.n = n
    # マス目を作成する
    self.puzzle = []
    # 数字のリストを作る
    self.numbers = list(range(1, n + 1))
    # 数字をランダムに配置する
    for i in range(n):
      # 数字のリストをシャッフルする
      random.shuffle(self.numbers)
      # シャッフルしたリストをマス目に追加する
      self.puzzle.append(self.numbers[:])
    # パズルを完成させる
    self.solve()

  def solve(self):
    """
    パズルを完成させるメソッド
    """
    # パズルを完成させるまで繰り返す
    while True:
      # 空白マスを探す
      found = False
      for i in range(self.n):
        for j in range(self.n):
          if self.puzzle[i][j] == 0:
            # 空白マスが見つかったら、その位置を記録する
            found = True
            start_i = i
            start_j = j
            break
        if found:
          break
      # 空白マスがなければ、パズルが完成したということ
      if not found:
        break
      # 空白マスに隣接する数字のマスを探す
      found = False
      for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # 空白マスの上下左右にあるマスの位置を計算する
        i = start_i + di
        j = start_j + dj
        # マス目の範囲内にあるかどうかチェックする
        if 0 <= i < self.n and 0 <= j < self.n:
          # マスに数字が入っているかどうかチェックする
          if self.puzzle[i][j] != 0:
            # 数字が入っているマスが見つかったら、その位置と数字を記録する
            found = True
            end_i = i
            end_j = j
            number = self.puzzle[i][j]
            break
        if found:
          break
      # 隣接する数字のマスがなければ、空白マスは黒マスになる
      if not found:
        self.puzzle[start_i][start_j] = -1 # -1は黒マスを表す
      else:
        # 隣接する数字のマスがあれば、その数字を空白マスに移動する
        self.puzzle[start_i][start_j] = number
        self.puzzle[end_i][end_j] = 0

  def show(self):
    """
    パズルを表示するメソッド
    """
    for row in self.puzzle:
      print(row)


# 例
hitori = HitoriNumber(5)
hitori.show()
