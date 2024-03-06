import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class DTC:
    filepath = None
    constructor_parameters = {}
    test_parameters = {}
    target_column = None
    # model = None
    columns = None
    dataframe = None
    dataframe_org = None

    @classmethod
    def set_filepath(cls, filepath):
        cls.filepath = filepath
        cls.dataframe = pd.read_csv(filepath) # CSV読込

    @classmethod
    def set_parameter(cls, parameters):
        cls.constructor_parameters = parameters

    @classmethod
    def set_test_parameter(cls, parameters):
        cls.test_parameters = parameters

    @classmethod
    def set_target(cls, target_column):
        cls.target_column = target_column
    @classmethod
    def get_target(cls):
        return cls.target_column

    @classmethod
    def set_columns(cls, columns):
        cls.columns = columns

    def train(self):
        # 特徴量と正解ラベルを分割する
        if self.columns is None:
            X = self.dataframe.drop(self.target_column, axis=1)
        else:
            X = self.dataframe[self.columns]

        y = self.dataframe[self.target_column]

        # データを訓練データとテストデータに分割する
        X_train, X_test, y_train, y_test = train_test_split(X, y, **self.test_parameters)

        # モデルを学習する
        model = DecisionTreeClassifier(**self.constructor_parameters)
        model.fit(X_train, y_train)
        self.model = model
        self.X_test = X_test
        self.y_test = y_test

    def score(self):
        if self.model is not None:
            return self.model.score(self.X_test, self.y_test)

        return None
    
    def dump(self,file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self.model, f)



if (__name__=="__main__"):
    # DTCクラスにファイルパスを与える
    DTC.set_filepath("../datafiles/iris.csv")

    #test
    # print(DTC.dataframe["種類"].unique())
    # print(DTC.dataframe["種類"].unique()[0])
    # print(DTC.dataframe["種類"].value_counts())

    # DTCクラスにDecisionTreeClassifierのコンストラクタパラメータを与える
    DTC.set_parameter({"max_depth": 2, "random_state": 0})
    # DTCクラスにDecisionTreeClassifierのテストパラメータを与える
    DTC.set_test_parameter({"test_size": 0.3, "random_state": 0})
    # DTCクラスにtargetの項目名を設定する
    DTC.set_target("種類")
    # DTCクラスに特徴量の項目名を設定する
    # DTC.set_columns(['がく片長さ', 'がく片幅', '花弁長さ'])
    DTC.set_columns(['がく片長さ', 'がく片幅', '花弁長さ', '花弁幅'])

    ###DataFlameの加工
    df=DTC.dataframe

    # 各列の平均値を計算して、colmeanに代入
    # colmean = df.mean()
    colmean = df.mean(numeric_only=1)
    colmean

    # 平均値で欠損値を穴埋めしてdf2に代入
    df2 = df.fillna(colmean)
    # 欠損値があるか確認
    df2.isnull().any(axis = 0)

    DTC.dataframe=df2

    # 平均値で欠損値を穴埋めしてdf2に代入
    # df2 = df.fillna(colmean)
    # # 欠損値があるか確認
    # df2.isnull().any(axis = 0)
    ###

    # モデルを学習する
    dtc = DTC()
    dtc.train()
    print(dtc.score())

    dtc.dump('irismodel.pkl')
