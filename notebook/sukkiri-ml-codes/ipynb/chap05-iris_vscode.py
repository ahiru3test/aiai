import pandas as pd
import os
import matplotlib.pyplot as plt
 
filename = os.path.dirname(__file__)
 
df = pd.read_csv(filename + '/../datafiles/iris.csv')
 
# 各列の平均値を計算して、colmeanに代入
colmean = df.mean(numeric_only=True)
 
# 平均値で欠損値を穴埋めしてdf2に代入
df2 = df.fillna(colmean)
# 欠損値があるか確認
# df2.isnull().any(axis = 0)
 
xcol = ['がく片長さ', 'がく片幅', '花弁長さ', '花弁幅']
 
x = df2[xcol]
t = df2['種類']
 
# 関数のインポート
from sklearn import tree
# モデルの作成
model = tree.DecisionTreeClassifier(max_depth = 2, random_state=0)
 
# 関数のインポート
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, t,
    test_size = 0.3, random_state = 0)
 
# 訓練データで再学習
model.fit(x_train, y_train)
 
# テストデータの予測結果と実際の答えが合致する正解率を計算
print("Score:", model.score(x_test, y_test))
 
# 描画関数の仕様上、和名の特徴量を英字に直す
x_train.columns = ['gaku_nagasa', 'gaku_haba',
'kaben_nagasa','kaben_haba']
# 描画関数の利用
from sklearn.tree import plot_tree
# plot_tree関数で決定木を描画
plot_tree(model, feature_names = list(x_train.columns), filled = True)
 
plt.show()
