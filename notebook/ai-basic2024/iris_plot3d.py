# -*- coding: utf-8 -*-
from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 手書き数字のデータをロードし、変数digitsに格納
#igits = datasets.load_digits()
iris = datasets.load_iris()

# 特徴量のセットを変数Xに、ターゲットを変数yに格納
X = iris.data
y = iris.target

# 特徴量を外花被片の長さ(sepal length)と幅(sepal width)
# 内花被片の長さ(petal length)の3つで3次元グラフを表示
X = X[:,:3]

# ターゲットは2 (iris virginica) でないもの, 
# つまり iris setosa (0) と iris versicolor (1) のみを対象とする
# (領域の2分割)
X = X[y!=2]
y = y[y!=2]
# ターゲットを0 (iris setosa) 以外にする場合の処理, 
#X = X[y!=0]
#y = y[y!=0]

# 3次元グラフの領域を準備
# '111'は、「縦１枚、横１枚、のグラフエリアの１枚目」を表し、
# 表示するグラフが１枚だけであることを意味する
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# x, y, zの3つの軸にラベルの設定
ax.set_xlabel('sepal length')
ax.set_ylabel('sepal width')
ax.set_zlabel('petal lenght')

# setosa,virsicolor,virginicaに対する色指定用の関数
def getcolor(c):
    if c==0:
        return 'orange' # 橙
    elif c==1:
        return 'cyan'   # シアン
    elif c==2:
        return 'green'  # 緑

# 正解の数字(y)に対応する色のリストを用意
cols = list(map(getcolor, y))

# 三次元空間へのデータの色付き描画を行う
# X[:,0] がx軸のデータ
# X[:,1] がy軸のデータ
# X[:,2] がz軸のデータ
ax.scatter(X[:,0], X[:,1], X[:,2], color=cols,linewidths=0.5, edgecolors='black')

# 描画したグラフを表示
plt.show()
