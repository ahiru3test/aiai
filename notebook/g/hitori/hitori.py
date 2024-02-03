def create_ひとりにしてくれ(n):
  """
  ひとりにしてくれを作成する関数

  引数:
    n: マス目のサイズ

  戻り値:
    ひとりにしてくれのパズル
  """

  # マス目を作成する
  puzzle = [[0 for _ in range(n)] for _ in range(n)]

  # 数字を配置する
  for i in range(n):
    for j in range(n):
      if i == 0 or j == 0 or i == n-1 or j == n-1:
        puzzle[i][j] = 1

  # 空白マスをスタート地点とする
  start_i = 1
  start_j = 1

  # パズルを完成させるまで繰り返す
  while True:
    # 移動できる数字があれば、その数字を移動する
    if puzzle[start_i-1][start_j] == 0:
      puzzle[start_i-1][start_j] = puzzle[start_i][start_j]
      puzzle[start_i][start_j] = 0
      start_i -= 1
    elif puzzle[start_i+1][start_j] == 0:
      puzzle[start_i+1][start_j] = puzzle[start_i][start_j]
      puzzle[start_i][start_j] = 0
      start_i += 1
    elif puzzle[start_i][start_j-1] == 0:
      puzzle[start_i][start_j-1] = puzzle[start_i][start_j]
      puzzle[start_i][start_j] = 0
      start_j -= 1
    elif puzzle[start_i][start_j+1] == 0:
      puzzle[start_i][start_j+1] = puzzle[start_i][start_j]
      puzzle[start_i][start_j] = 0
      start_j += 1
    else:
      # 移動できる数字がなければ、スタート地点を移動する
      if start_i == 1:
        start_i += 1
      elif start_i == n-2:
        start_i -= 1
      elif start_j == 1:
        start_j += 1
      elif start_j == n-2:
        start_j -= 1

    # すべての数字が1マスずつ離れたら、パズルが完成する
    if all(all(puzzle[i][j] != puzzle[i+1][j] and puzzle[i][j] != puzzle[i][j+1] for j in range(n-1)) for i in range(n-1)):
      break

  # ひとりにしてくれのパズルを返す
  return puzzle


# 例
puzzle = create_ひとりにしてくれ(5)
for row in puzzle:
  print(row)
