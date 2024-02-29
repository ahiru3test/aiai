# import numpy as np

# aaa = np.array([16,9])
# ccc = np.array([0, 0])

# for c in range(1,120,1):
#     bbb = aaa *c
#     if(bbb[1]%8==0):
#         ccc += bbb
#         print(ccc)

# 2000以内の自然数のリストを作成
numbers = list(range(1, 2001))

# 16:9の比率を保つ２値の組み合わせを格納するリストを作成
pairs = []

# numbersの中から２値を選ぶループ
for i in numbers:
    for j in numbers:
        # ２値の比が16:9に等しいか判定
        if i / j == 16 / 9 and i%8==0 and j%8==0 :
            # 等しい場合はpairsに追加
            pairs.append([i, j])

# pairsの中身を表示
print(pairs)
