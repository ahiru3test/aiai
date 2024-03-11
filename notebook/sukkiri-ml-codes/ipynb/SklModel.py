import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class SklModelResult(): #     #         #         #         #         # 
    def __init__(self, data=None):
        self.x_train = data.get('x_train') if data else None
        self.x_val = data.get('x_val') if data else None
        self.y_train = data.get('y_train') if data else None
        self.y_val = data.get('y_val') if data else None
        self.sc_x_train = data.get('sc_x_train') if data else None
        self.sc_x_val = data.get('sc_x_val') if data else None
        self.sc_y_train = data.get('sc_y_train') if data else None
        self.sc_y_val = data.get('sc_y_val') if data else None
        self.is_standardization = data.get(
            'is_standardization') if data else None
        self.sc_x_model = data.get('sc_x_model') if data else None
        self.sc_y_model = data.get('sc_y_model') if data else None
        self.model = data.get('model') if data else None
        self.train_score = data.get('train_score') if data else None
        self.val_score = data.get('val_score') if data else None

class SklModel():
    # dataframe = None

    def __init__(self):
        self.model=None
        self.columns = None
        self.test_parameters = {}
        self.model_parameters = {}
        self.dataframe= None
        # self.dataframe_org= None
        self.filepath = None

    #step1 csvファイルの読込
    def set_filepath(self, filepath):
        self.filepath = filepath
        self.dataframe = pd.read_csv(filepath) # CSV読込
        # self.dataframe_org=self.dataframe.copy()
        return self.dataframe

    #step2 ダミー変数の設定
    def get_dummy_columns(self, df:pd.DataFrame, columns:list, drop=0):
        drop_flag = {0:False,1:True}
        # print(drop_flag[drop])
        for column in columns:
            dummy = pd.get_dummies(
                df[column], drop_first=drop_flag[drop], dtype=int)
            df = pd.concat([df, dummy], axis=1)
        df = df.drop(columns, axis=1)
        return df

    def set_test_parameters(self, parameters):
        self.test_parameters = parameters

    #step3
    def split(self,*parrays):
        # データを分割する
        return train_test_split(*parrays, **self.test_parameters)

    def set_target(self, target_column):
        self.target_column = target_column

        # 特徴量と正解ラベルを分割する
        if self.columns is None:
            columns = self.dataframe.drop(
                self.target_column, axis=1).columns.tolist()
            self.set_columns(columns)
        
        return self.target_column

    def get_target(self): return self.target_column

    def set_columns(self, columns):
        self.columns = columns
        return self.columns
        # return cls.columns := columns

    def get_columns(self):
        return self.columns
    
    def fillna_meaning(self, df) -> pd.DataFrame:
        return df.fillna(df.mean())
    
    def ss_transform(self, df, model=None):
        if (model is None):
            sc_model_x = StandardScaler() #訓練データxの標準化モデル
            sc_model_x.fit(df)
            sc_x = sc_model_x.transform(df) #標準化されたxのdfデータ
            return sc_x, sc_model_x
        else:
            sc_model_x = model
            sc_x = sc_model_x.transform(df) #標準化されたxのdfデータ
            return sc_x

    def set_model_parameters(self, parameters):
        self.model_parameters = parameters

    def get_model_parameters(self):
        return self.model_parameters

    def init_model(self,model_name=""):
        self.models=[
            "DecisionTreeClassifier",
            "DecisionTreeRegressor",
            "LinearRegression",
        ]
        if model_name not in self.models : return None
        self.model_name = model_name
        if model_name == "DecisionTreeClassifier":
            return DecisionTreeClassifier(**self.model_parameters)
        elif model_name == "LinearRegression":
            return LinearRegression(**self.model_parameters)
        elif model_name == "DecisionTreeRegressor":
            return DecisionTreeRegressor(**self.model_parameters)
        else:
            return None

    def learn(self, x, y, is_test_split=False
              , is_standardization=False, x_model=None, y_model=None):
        ###テスト分割
        if (is_test_split == True):
            x_train, x_val, y_train, y_val = train_test_split(
                x, y, **self.test_parameters)
            ### 訓練データを標準化
            if(x_model is None or y_model is None):
                sc_x_model = StandardScaler()
                sc_y_model = StandardScaler()
                sc_x_model.fit(x_train)
                sc_x_train = sc_x_model.transform(x_train)
                sc_y_model.fit(y_train)
                sc_y_train = sc_y_model.transform(y_train)
            else:
                sc_x_train = x_train
                sc_y_train = y_train
            ### 学習
            # model = LinearRegression()
            model = self.init_model(self.model_name)
            model.fit(sc_x_train, sc_y_train)
            ### 検証データを標準化
            sc_x_val = sc_x_model.transform(x_val)
            sc_y_val = sc_y_model.transform(y_val)
            ### 訓練データと検証データの決定係数計算
            train_score = model.score(sc_x_train, sc_y_train)
            val_score = model.score(sc_x_val, sc_y_val)

            ### 戻り値
            ret = {
                'x_train': x_train,
                'x_val': x_val,
                'y_train': y_train,
                'y_val': y_val,
                'sc_x_train': sc_x_train,
                'sc_x_val': sc_x_val,
                'sc_y_train': sc_y_train,
                'sc_y_val': sc_y_val,
                'is_standardization': is_standardization,
                'sc_x_model': sc_x_model,
                'sc_y_model': sc_y_model,
                'model': model,
                'train_score': train_score,
                'val_score': val_score,
            }
        else:
            ### 訓練データを標準化
            x_train=x
            y_train=y
            if(x_model is None or y_model is None):
                sc_x_model = StandardScaler()
                sc_y_model = StandardScaler()
                sc_x_model.fit(x_train)
                sc_x_train = sc_x_model.transform(x_train)
                sc_y_model.fit(y_train)
                sc_y_train = sc_y_model.transform(y_train)
            else:
                sc_x_train = x_train
                sc_y_train = y_train
            ### 学習
            # model = LinearRegression()
            model = self.init_model(self.model_name)
            model.fit(sc_x_train, sc_y_train)
            ### 検証データを標準化
            # sc_x_val = sc_x_model.transform(x_val)
            # sc_y_val = sc_y_model.transform(y_val)
            ### 訓練データと検証データの決定係数計算
            train_score = model.score(sc_x_train, sc_y_train)
            # val_score = model.score(sc_x_val, sc_y_val)

            ### 戻り値
            ret = {
                'x_train': x_train,
                'x_val': None,
                'y_train': y_train,
                'y_val': None,
                'sc_x_train': sc_x_train,
                'sc_x_val': None,
                'sc_y_train': sc_y_train,
                'sc_y_val': None,
                'is_standardization': is_standardization,
                'sc_x_model': sc_x_model,
                'sc_y_model': sc_y_model,
                'model': model,
                'train_score': train_score,
                'val_score': None,
            }
        return SklModelResult(ret)
