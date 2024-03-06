import pandas as pd
import pickle,os
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
    dataframe_hold = None

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

    @classmethod
    def split(cls):
        # 特徴量と正解ラベルを分割する
        if cls.columns is None:
            cls.X = cls.dataframe.drop(cls.target_column, axis=1)
        else:
            cls.X = cls.dataframe[cls.columns]

        cls.y = cls.dataframe[cls.target_column]

        # データを訓練データとテストデータに分割する
        return train_test_split(cls.X, cls.y, **cls.test_parameters)

    def train_only(self,df_X,df_Y):
        # モデルを学習する
        self.model = DecisionTreeClassifier(**self.constructor_parameters)
        self.model.fit(df_X, df_Y)

    def train(self,df_X,df_XT,df_Y,df_YT):
        self.train_only(df_X,df_Y)
        if self.model is None:
            ret = None
        ret = self.model.score(df_XT,df_YT)
        return ret


    def score(self,df_XT,df_YT):
        if self.model is not None:
            return self.model.score(df_XT, df_YT)
        return None
    
    def dump(self,file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self.model, f)



if (__name__=="__main__"):
    # DTCクラスにファイルパスを与える
    # filename = os.path.dirname(__file__) + "/books.csv" #実行ファイルのパス
    DTC.set_filepath(os.path.dirname(__file__)+"/../datafiles/iris.csv")

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
    ###

    # モデルを学習する
    df_X,df_XT,df_Y,df_YT = DTC.split()
    dtc = DTC()
    print(dtc.train(df_X,df_XT,df_Y,df_YT))

    # dtc.dump(os.path.dirname(__file__)+'/irismodel.pkl')
