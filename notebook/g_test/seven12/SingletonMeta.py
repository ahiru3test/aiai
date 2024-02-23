class SingletonMeta(type):
    # インスタンスを保持する辞書
    _instances = {}

    # インスタンスが存在するかどうかを返すメソッド
    def is_instance(cls):
        return cls in cls._instances

    # クラスのインスタンスを生成するメソッド
    def __new__(cls, name, bases, attrs):
        # メタクラスで定義したクラス変数を派生クラスの属性として追加する
        attrs["_instances"] = cls._instances
        # スーパークラスの__new__メソッドを呼び出す
        return super().__new__(cls, name, bases, attrs)

    # クラスのインスタンスを呼び出すメソッド
    def __call__(cls, *args, **kwargs):
        # インスタンスがない場合は生成する
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
