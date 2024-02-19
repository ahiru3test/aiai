# HitoriLogicの問題を作成するコード

import random

# 問題のサイズを指定する
n = 5 # 5x5の問題

# 問題の数字をランダムに生成する
problem = [[random.randint(1, n) for _ in range(n)] for _ in range(n)]

# 問題を表示する
print("HitoriLogicの問題")
for row in problem:
    print(*row)

# HitoriLogicの問題を解答するコード

# 問題の数字をコピーする
solution = [row[:] for row in problem]

# 問題の数字を塗りつぶすかどうかを記録する
painted = [[False for _ in range(n)] for _ in range(n)]

# 問題の数字を塗りつぶす関数
def paint(i, j):
    # 塗りつぶす数字を0にする
    solution[i][j] = 0
    # 塗りつぶしたことを記録する
    painted[i][j] = True

# 問題の数字を塗りつぶすルールに従って塗りつぶす
for i in range(n):
    for j in range(n):
        # 同じ行に同じ数字がある場合
        if problem[i].count(problem[i][j]) > 1:
            # 塗りつぶされていない数字を塗りつぶす
            if not painted[i][j]:
                paint(i, j)
        # 同じ列に同じ数字がある場合
        if [row[j] for row in problem].count(problem[i][j]) > 1:
            # 塗りつぶされていない数字を塗りつぶす
            if not painted[i][j]:
                paint(i, j)

# 塗りつぶしたマスが隣り合わないように調整する
for i in range(n):
    for j in range(n):
        # 塗りつぶしたマスの場合
        if painted[i][j]:
            # 上下左右のマスをチェックする
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # 境界を超えない場合
                if 0 <= i + di < n and 0 <= j + dj < n:
                    # 隣のマスも塗りつぶされている場合
                    if painted[i + di][j + dj]:
                        # 元のマスを元の数字に戻す
                        solution[i][j] = problem[i][j]
                        # 塗りつぶしたことを取り消す
                        painted[i][j] = False
                        # ループを抜ける
                        break

# 塗りつぶしたマスで塗りつぶしていないマスを閉じ込めないように調整する
# 塗りつぶしていないマスの連結成分の個数を数える関数
def count_components():
    # 訪問済みのマスを記録する
    visited = [[False for _ in range(n)] for _ in range(n)]
    # 連結成分の個数を記録する
    count = 0
    # すべてのマスについて
    for i in range(n):
        for j in range(n):
            # 塗りつぶしていないマスで、まだ訪問していない場合
            if solution[i][j] != 0 and not visited[i][j]:
                # 連結成分の個数を増やす
                count += 1
                # 幅優先探索で連結成分を訪問する
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop(0)
                    visited[x][y] = True
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if 0 <= x + dx < n and 0 <= y + dy < n:
                            if solution[x + dx][y + dy] != 0 and not visited[x + dx][y + dy]:
                                queue.append((x + dx, y + dy))
    # 連結成分の個数を返す
    return count

# 連結成分の個数が1でない場合
if count_components() != 1:
    # 塗りつぶしたマスをランダムに選んで元に戻す
    while True:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if painted[i][j]:
            solution[i][j] = problem[i][j]
            painted[i][j] = False
            # 連結成分の個数が1になったら終了する
            if count_components() == 1:
                break

# 解答を表示する
print("HitoriLogicの解答")
for row in solution:
    print(*row)
