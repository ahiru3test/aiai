# HItori Numberのルールに従って、パズルを解くクラス
class HitoriSolver:

  # コンストラクタ
  def __init__(self, puzzle):
    # パズルのサイズを取得する
    self.size = len(puzzle)
    # パズルのコピーを作成する
    self.puzzle = [row[:] for row in puzzle]
    # 解答の初期化
    self.answer = [[0 for _ in range(self.size)] for _ in range(self.size)]
    # パズルの数字を辞書に登録する
    self.digits = {}
    for i in range(self.size):
      for j in range(self.size):
        digit = self.puzzle[i][j]
        if digit not in self.digits:
          self.digits[digit] = []
        self.digits[digit].append((i, j))

  # パズルを解くメソッド
  def solve(self):
    # パズルの数字ごとに処理する
    for digit in self.digits:
      # 数字が出現する座標のリストを取得する
      positions = self.digits[digit]
      # 数字が1回しか出現しない場合は、その数字は必ず白マスになる
      if len(positions) == 1:
        i, j = positions[0]
        self.answer[i][j] = 1
      # 数字が2回以上出現する場合は、その数字のうち少なくとも1つは黒マスになる
      else:
        # 数字が同じ行または同じ列にある場合は、その数字は必ず黒マスになる
        for i, j in positions:
          for k, l in positions:
            if i == k or j == l:
              self.answer[i][j] = -1
              self.answer[k][l] = -1
        # 数字が同じ行でも同じ列でもない場合は、その数字は白マスか黒マスかのどちらかになる
        # その場合は、仮定してみて矛盾がないかチェックする
        for i, j in positions:
          if self.answer[i][j] == 0:
            # 仮に白マスにした場合
            self.answer[i][j] = 1
            # 矛盾がないかチェックする
            if self.is_valid():
              # 矛盾がなければそのままにする
              continue
            else:
              # 矛盾があれば元に戻す
              self.answer[i][j] = 0
            # 仮に黒マスにした場合
            self.answer[i][j] = -1
            # 矛盾がないかチェックする
            if self.is_valid():
              # 矛盾がなければそのままにする
              continue
            else:
              # 矛盾があれば元に戻す
              self.answer[i][j] = 0
    # 解答を返す
    return self.answer

  # パズルの解答が正しいかどうかチェックするメソッド
  def is_valid(self):
    # 黒マスの周りに黒マスがないかチェックする
    for i in range(self.size):
      for j in range(self.size):
        if self.answer[i][j] == -1:
          # 上下左右のマスを調べる
          for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = i + di
            nj = j + dj
            # パズルの範囲内かどうかチェックする
            if 0 <= ni < self.size and 0 <= nj < self.size:
              # 黒マスがあれば矛盾
              if self.answer[ni][nj] == -1:
                return False
    # 白マスが連結しているかチェックする
    # 白マスの個数を数える
    white_count = 0
    for i in range(self.size):
      for j in range(self.size):
        if self.answer[i][j] == 1:
          white_count += 1
    # 白マスの一つを選ぶ
    for i in range(self.size):
      for j in range(self.size):
        if self.answer[i][j] == 1:
          # その白マスから連結している白マスの個数を数える
          connected_count = self.count_connected(i, j)
          # 連結している白マスの個数が全体の白マスの個数と一致すればOK
          if connected_count == white_count:
            return True
          else:
            # 一致しなければ矛盾
            return False
    # ここまで来たら正しいと判断する
    return True

  # ある白マスから連結している白マスの個数を数えるメソッド
  def count_connected(self, i, j):
    # 連結している白マスの個数を初期化する
    count = 0
    # 訪問済みのマスを記録する
    visited = [[False for _ in range(self.size)] for _ in range(self.size)]
    # スタックを用意する
    stack = []
    # スタックに最初の白マスを入れる
    stack.append((i, j))
    # スタックが空になるまで繰り返す
    while stack:
      # スタックから白マスを取り出す
      i, j = stack.pop()
      # その白マスを訪問済みにする
      visited[i][j] = True
      # 連結している白マスの個数を増やす
      count += 1
      # 上下左右のマスを調べる
      for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni = i + di
        nj = j + dj
        # パズルの範囲内かどうかチェックする
        if 0 <= ni < self.size and 0 <= nj < self.size:
          # 白マスで未訪問ならスタックに入れる
          if self.answer[ni][nj] == 1 and not visited[ni][nj]:
            stack.append((ni, nj))
    # 連結している白マスの個数を返す
    return count

if __name__ == "__main__":
  n = [
    [1, 2, 2, 1, 5],
    [4, 2, 5, 3, 1],
    [4, 5, 1, 5, 4],
    [5, 4, 5, 1, 2],
    [2, 5, 4, 5, 2],
  ]
  # n = [
  #   [1, 2, 2, 1, 5],
  #   [4, 2, 5, 3, 1],
  #   [4, 5, 1, 5, 4],
  #   [5, 4, 5, 1, 2],
  #   [2, 5, 4, 5, 2],
  # ]

  print(HitoriSolver(n).solve())

