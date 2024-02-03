import random

def create_ひとりにしてくれ(n):
  """
  ひとりにしてくれを作成する関数

  引数:
    n: マス目のサイズ

  戻り値:
    ひとりにしてくれのパズル
  """

  # マス目を作成する
  puzzle = []

  # 数字のリストを作る
  numbers = list(range(1, n + 1))

  # 数字をランダムに配置する
  for i in range(n):
    # 数字のリストをシャッフルする
    random.shuffle(numbers)
    # シャッフルしたリストをマス目に追加する
    puzzle.append(numbers[:])

  # パズルを完成させる
  while True:
    # 空白マスを探す
    found = False
    for i in range(n):
      for j in range(n):
        if puzzle[i][j] == 0:
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
      if 0 <= i < n and 0 <= j < n:
        # マスに数字が入っているかどうかチェックする
        if puzzle[i][j] != 0:
          # 数字が入っているマスが見つかったら、その位置と数字を記録する
          found = True
          end_i = i
          end_j = j
          number = puzzle[i][j]
          break
      if found:
        break

    # 隣接する数字のマスがなければ、空白マスは黒マスになる
    if not found:
      puzzle[start_i][start_j] = -1 # -1は黒マスを表す
    else:
      # 隣接する数字のマスがあれば、その数字を空白マスに移動する
      puzzle[start_i][start_j] = number
      puzzle[end_i][end_j] = 0

  # ひとりにしてくれのパズルを返す
  return puzzle


# 例
puzzle = create_ひとりにしてくれ(5)
for row in puzzle:
  print(row)
