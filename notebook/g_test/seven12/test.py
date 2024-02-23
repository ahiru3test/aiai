import pytest

class SingletonMeta(type):
    # インスタンスを保持する辞書
    _instances = {}

    # インスタンスが存在するかどうかを返すメソッド
    def is_instance(cls):
        return cls in cls._instances

    # クラスのインスタンスを生成するメソッド
    def __new__(cls, *args, **kwargs):
        # メタクラスで定義したクラス変数を派生クラスの属性として追加する
        attrs["_instances"] = cls._instances
        print("new")
        # スーパークラスの__new__メソッドを呼び出す（引数を変更）
        return super().__new__(cls, *args, **kwargs)

    # クラスのインスタンスを呼び出すメソッド
    def __call__(cls, *args, **kwargs):
        # インスタンスがない場合は生成する
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class TSingleton(metaclass=SingletonMeta):
    def __init__(self):
        print("init")
    
# テスト関数の定義
def test_singleton():
    # インスタンスを2回取得する
    s1 = TSingleton()
    s2 = TSingleton()

    # 同じインスタンスであることを確認する
    assert s1 is s2
